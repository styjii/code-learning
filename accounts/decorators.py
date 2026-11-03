"""Décorateurs de vues liés à l'authentification (voir ``accounts/middleware.py``)."""

from django.contrib.auth.decorators import login_not_required


def api_endpoint(view_func):
    """
    Déclare une vue Django classique comme point d'entrée JSON.

    Sans connexion, elle répond alors 401 en JSON au lieu d'une redirection vers la page de connexion
    (inutile pour un ``fetch()``). À placer au-dessus des autres décorateurs. Les vues DRF n'en ont pas besoin.
    """
    view_func.is_api = True
    return view_func


def public_endpoint(view_func):
    """
    Rend une vue accessible SANS connexion. À réserver aux cas voulus (page de connexion, sonde de santé…).

    Pour une vue DRF, ``login_not_required`` seul ne suffit pas : DRF le pose déjà sur toutes ses vues, et le
    middleware l'ignore pour elles (voir ``StrictLoginRequiredMiddleware``). Ce décorateur ajoute le marqueur
    explicite que le middleware reconnaît ; la vue DRF doit en plus déclarer ``permission_classes = [AllowAny]``.
    """
    view_func.is_public = True
    return login_not_required(view_func)
