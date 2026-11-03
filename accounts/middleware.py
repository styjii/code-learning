"""Authentification obligatoire sur TOUTES les routes (refus par défaut)."""

from django.contrib.auth.middleware import LoginRequiredMiddleware
from django.http import JsonResponse
from django.utils.cache import add_never_cache_headers
from django.utils.translation import gettext as _
from rest_framework.views import APIView

from .authentication import API_AUTH_CHALLENGE


def is_drf_view(view_func) -> bool:
    """``APIView.as_view()`` et ``ViewSet.as_view()`` posent l'attribut ``cls`` sur la vue produite."""
    cls = getattr(view_func, "cls", None)
    return isinstance(cls, type) and issubclass(cls, APIView)


def is_api_request(request, view_func) -> bool:
    """La réponse attendue est-elle du JSON (API) plutôt qu'une page HTML ?"""
    if is_drf_view(view_func) or getattr(view_func, "is_api", False):  # voir accounts.decorators.api_endpoint
        return True
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return True
    # Une navigation de navigateur annonce toujours text/html ; un client d'API demande du JSON seul.
    accept = request.headers.get("Accept", "")
    return "application/json" in accept and "text/html" not in accept


def unauthorized_response() -> JsonResponse:
    """401 JSON. ``detail`` suit la convention DRF ; ``status`` et ``message`` gardent le format d'erreur
    déjà lu par le JavaScript de l'application (voir ``populate_step``)."""
    message = _("Authentification requise.")
    response = JsonResponse({"detail": message, "status": "error", "message": message}, status=401)
    response["WWW-Authenticate"] = API_AUTH_CHALLENGE
    add_never_cache_headers(response)
    return response


class StrictLoginRequiredMiddleware(LoginRequiredMiddleware):
    """
    ``LoginRequiredMiddleware`` de Django, complété sur deux points :

    1. **Aucune exemption implicite pour DRF.** DRF marque toutes ses vues ``login_required = False`` et
       laisse ses permissions décider ; une vue déclarée par erreur avec ``AllowAny`` ou
       ``permission_classes = []`` serait alors publique. Ici, une vue DRF exige une connexion, quelles que
       soient ses permissions, sauf si elle est marquée explicitement avec ``@public_endpoint``.
    2. **Réponse adaptée au type de requête** : redirection vers la page de connexion pour une page, mais
       **401 JSON** pour un appel d'API (rediriger un ``fetch()`` renverrait du HTML de connexion avec un 200).

    Les vues déjà exemptées par Django (``@login_not_required`` : page de connexion, connexion de l'admin)
    restent publiques. Les permissions DRF s'appliquent ensuite, en seconde barrière.
    """

    def process_view(self, request, view_func, view_args, view_kwargs):
        if is_drf_view(view_func) and not getattr(view_func, "is_public", False):
            if request.user.is_authenticated:
                return None
            return self.handle_no_permission(request, view_func)
        return super().process_view(request, view_func, view_args, view_kwargs)

    def handle_no_permission(self, request, view_func):
        if is_api_request(request, view_func):
            return unauthorized_response()
        return super().handle_no_permission(request, view_func)  # redirection vers LOGIN_URL (?next=…)
