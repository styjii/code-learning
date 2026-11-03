"""Vérifications de configuration du cache qui porte les compteurs de tentatives de connexion."""

from django.conf import settings
from django.core import checks

DUMMY = "DummyCache"
# Partagés entre processus ET dotés d'un incr() atomique.
SUITABLE = ("RedisCache", "PyMemcacheCache", "PyLibMCCache")


def _backend() -> str:
    return settings.CACHES["default"]["BACKEND"]


@checks.register()
def check_throttle_cache_is_not_dummy(app_configs, **kwargs):
    if _backend().endswith(DUMMY):
        return [checks.Error(
            "Le cache « default » est un DummyCache : il ne conserve rien, la limitation des tentatives "
            "de connexion est donc désactivée.",
            hint="Définissez DJANGO_CACHE_URL (redis://… ou memcached://…) ou laissez le cache par défaut.",
            id="accounts.E001",
        )]
    return []


@checks.register(deploy=True)  # python manage.py check --deploy
def check_throttle_cache_is_shared(app_configs, **kwargs):
    backend = _backend()
    if backend.endswith(SUITABLE) or backend.endswith(DUMMY):
        return []
    if backend.endswith("LocMemCache"):
        problem = "est local à chaque processus : avec plusieurs workers, la limite est multipliée par leur nombre"
    else:
        problem = "ne garantit pas d'incrémentation atomique : des requêtes simultanées peuvent dépasser la limite"
    return [checks.Warning(
        f"Le cache « default » ({backend.rsplit('.', 1)[-1]}) {problem}.",
        hint="Utilisez un cache partagé et atomique : DJANGO_CACHE_URL=redis://127.0.0.1:6379/1",
        id="accounts.W001",
    )]
