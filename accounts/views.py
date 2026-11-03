from django.contrib.auth.views import LoginView
from django.utils.functional import cached_property
from django.utils.translation import gettext as _

from .netutils import get_client_ip
from .throttle import LoginThrottle, is_trusted_device, normalize_username, trust_device


class ThrottledLoginView(LoginView):
    """
    Page de connexion avec limitation des tentatives (détails : ``accounts/throttle.py``).

    Chaque tentative est comptée avant l'authentification, par (IP, identifiant), par IP et par identifiant.
    L'IP est celle du client, y compris derrière un proxy inverse (``accounts/netutils.py``).
    """

    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    _reserved = False  # la tentative a-t-elle été comptée ?

    # --- limitation ----------------------------------------------------------
    @cached_property
    def throttle(self) -> LoginThrottle:
        username = self.request.POST.get("username", "")
        return LoginThrottle(
            get_client_ip(self.request), username,
            trusted_device=is_trusted_device(self.request, username),
        )

    def _has_credentials(self) -> bool:
        # Un champ vide n'est pas une tentative d'authentification : on ne la compte pas.
        return bool(normalize_username(self.request.POST.get("username", ""))) and bool(
            self.request.POST.get("password", "")
        )

    def _lockout_message(self) -> str:
        minutes = max(1, -(-self.throttle.lock_remaining() // 60))
        return _("Trop de tentatives échouées. Réessayez dans %(minutes)d minute(s).") % {"minutes": minutes}

    # --- formulaire -----------------------------------------------------------
    def _customize(self, form):
        form.fields["username"].widget.attrs.update(
            {"autocomplete": "username", "autofocus": True, "spellcheck": "false", "autocapitalize": "none"}
        )
        form.fields["password"].widget.attrs.update({"autocomplete": "current-password"})
        # Seule règle de saisie rappelée à la connexion : le champ ne doit pas être vide.
        # Aucune longueur minimale n'est imposée ni affichée ici (elle ne concerne que la création du compte).
        form.fields["username"].error_messages["required"] = _("Le nom d'utilisateur est obligatoire.")
        form.fields["password"].error_messages["required"] = _("Le mot de passe est obligatoire.")
        return form

    def get_form(self, form_class=None):
        return self._customize(super().get_form(form_class))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        remaining = self.throttle.lock_remaining() if self.request.method == "POST" else 0
        context["locked"] = remaining > 0
        context["lock_seconds"] = remaining
        context["lock_message"] = self._lockout_message() if remaining else ""
        return context

    def _locked_response(self):
        # Formulaire NON lié : un formulaire lié lancerait authenticate() dès que le gabarit lit ses erreurs,
        # c'est-à-dire qu'il vérifierait le mot de passe d'une requête pourtant refusée.
        form = self._customize(self.get_form_class()(
            request=self.request, initial={"username": self.request.POST.get("username", "")},
        ))
        return self.render_to_response(self.get_context_data(form=form), status=429)

    # --- cycle de vie ---------------------------------------------------------
    def post(self, request, *args, **kwargs):
        if self._has_credentials():
            if not self.throttle.reserve():  # atomique, avant toute authentification
                return self._locked_response()
            self._reserved = True
        return super().post(request, *args, **kwargs)

    def form_invalid(self, form):
        if self._reserved:
            self.throttle.register_failure()  # pose le blocage si la limite vient d'être atteinte
        return super().form_invalid(form)

    def form_valid(self, form):
        if self._reserved:
            self.throttle.register_success()
        response = super().form_valid(form)
        trust_device(response, self.request.POST.get("username", ""))
        return response
