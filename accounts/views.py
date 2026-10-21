from django.conf import settings
from django.contrib.auth.views import LoginView
from django.core.cache import cache
from django.utils.translation import gettext as _


class ThrottledLoginView(LoginView):
    """
    Page de connexion avec limitation des tentatives.

    Après ``LOGIN_MAX_ATTEMPTS`` échecs pour un même couple (adresse IP, identifiant),
    la connexion est bloquée ``LOGIN_LOCKOUT_SECONDS`` secondes. Le compteur est stocké dans
    le cache Django (mémoire locale par défaut : configurez un cache partagé avec plusieurs processus).
    """

    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    # --- compteur d'échecs -------------------------------------------------
    def _key(self) -> str:
        ip = self.request.META.get("REMOTE_ADDR", "?")
        username = self.request.POST.get("username", "").strip().lower()[:150]
        return f"login-failures:{ip}:{username}"

    def _is_locked(self) -> bool:
        return cache.get(self._key(), 0) >= settings.LOGIN_MAX_ATTEMPTS

    def _register_failure(self) -> None:
        key = self._key()
        cache.add(key, 0, timeout=settings.LOGIN_LOCKOUT_SECONDS)
        try:
            cache.incr(key)
        except ValueError:  # clé expirée entre-temps
            cache.set(key, 1, timeout=settings.LOGIN_LOCKOUT_SECONDS)

    # --- cycle de vie du formulaire ----------------------------------------
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["username"].widget.attrs.update(
            {"autocomplete": "username", "autofocus": True, "spellcheck": "false", "autocapitalize": "none"}
        )
        form.fields["password"].widget.attrs.update({"autocomplete": "current-password"})
        return form

    def post(self, request, *args, **kwargs):
        if self._is_locked():
            form = self.get_form()
            minutes = max(1, settings.LOGIN_LOCKOUT_SECONDS // 60)
            form.add_error(None, _("Trop de tentatives échouées. Réessayez dans %(minutes)d minute(s).") % {"minutes": minutes})
            return self.render_to_response(self.get_context_data(form=form), status=429)
        return super().post(request, *args, **kwargs)

    def form_invalid(self, form):
        self._register_failure()
        return super().form_invalid(form)

    def form_valid(self, form):
        cache.delete(self._key())
        return super().form_valid(form)
