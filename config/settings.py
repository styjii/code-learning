"""
Réglages Django du projet.

Toutes les valeurs sensibles ou propres à l'environnement viennent du fichier ``.env``
(voir ``.env.example``) ou des variables d'environnement.
"""

import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Les variables déjà présentes dans l'environnement restent prioritaires sur le fichier.
load_dotenv(BASE_DIR / ".env")


def env_bool(name: str, default: bool = False) -> bool:
    value = os.environ.get(name, "").strip().lower()
    return default if value == "" else value in {"1", "true", "yes", "on"}


def env_list(name: str) -> list:
    return [item.strip() for item in os.environ.get(name, "").split(",") if item.strip()]


def env_int(name: str, default: int) -> int:
    try:
        return int(os.environ.get(name, "").strip() or default)
    except ValueError:
        raise ImproperlyConfigured(f"{name} doit être un nombre entier.")


# ---------------------------------------------------------------------------
# Sécurité
# ---------------------------------------------------------------------------
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "").strip()
if not SECRET_KEY:
    raise ImproperlyConfigured(
        "DJANGO_SECRET_KEY est absent. Copiez .env.example vers .env et renseignez la clé secrète."
    )

DEBUG = env_bool("DJANGO_DEBUG", False)

ALLOWED_HOSTS = env_list("DJANGO_ALLOWED_HOSTS")
if not DEBUG and not ALLOWED_HOSTS:
    raise ImproperlyConfigured("DJANGO_ALLOWED_HOSTS est obligatoire lorsque DJANGO_DEBUG=0.")

CSRF_TRUSTED_ORIGINS = env_list("DJANGO_CSRF_TRUSTED_ORIGINS")

# HTTPS : actif par défaut en production
HTTPS = env_bool("DJANGO_HTTPS", not DEBUG)
SESSION_COOKIE_SECURE = HTTPS
CSRF_COOKIE_SECURE = HTTPS
SECURE_SSL_REDIRECT = HTTPS
SECURE_HSTS_SECONDS = env_int("DJANGO_HSTS_SECONDS", 0) if HTTPS else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = SECURE_HSTS_SECONDS > 0
BEHIND_PROXY = env_bool("DJANGO_BEHIND_PROXY", False)
if BEHIND_PROXY:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Noms de cookies propres à ce projet. Les cookies sont isolés par hôte et NON par port : sans nom dédié, ce projet
# (HTTPS, cookies « Secure ») et d'autres projets Django en HTTP sur la même IP se disputeraient « csrftoken » et
# « sessionid ». Un cookie « Secure » n'est jamais envoyé en HTTP et ne peut pas y être écrasé : les formulaires des
# autres projets échoueraient alors avec « CSRF cookie not set ». Si vous renommez le cookie CSRF, adaptez aussi
# editor/static/editor/js/utils/csrf.js.
CSRF_COOKIE_NAME = "cl_csrftoken"
SESSION_COOKIE_NAME = "cl_sessionid"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_AGE = env_int("DJANGO_SESSION_HOURS", 168) * 3600
CSRF_COOKIE_SAMESITE = "Lax"  # lisible par le JavaScript de l'éditeur (CSRF_COOKIE_HTTPONLY=False)
X_FRAME_OPTIONS = "DENY"

# Isole le groupe de navigation de l'application : une page d'une autre origine qui l'ouvre (window.open)
# ou qui est ouverte par elle n'obtient pas de référence window.opener (fuites inter-origines, XS-Leaks).
# Valeur par défaut de Django, explicite ici pour qu'elle ne change pas sans qu'on s'en aperçoive.
# Attention : le navigateur ne l'applique que sur une origine fiable (HTTPS ou localhost/127.0.0.1) ;
# en HTTP sur une adresse du réseau local il l'ignore et l'écrit dans la console. Voir README : « HTTPS en développement ».
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin"

# ---------------------------------------------------------------------------
# Authentification : toute route exige une connexion (StrictLoginRequiredMiddleware, accounts/middleware.py)
#   - page sans connexion  -> redirection vers LOGIN_URL ;
#   - API / JSON sans connexion -> 401 (au lieu d'une redirection ou d'un 403).
# ---------------------------------------------------------------------------
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "login"
# Limitation des tentatives (voir accounts/throttle.py). Trois compteurs complémentaires :
#   - par (IP, identifiant)  : LOGIN_MAX_ATTEMPTS, strict ;
#   - par IP, tous identifiants confondus : LOGIN_MAX_ATTEMPTS_PER_IP (« password spraying ») ;
#   - par identifiant, toutes IP confondues : LOGIN_MAX_ATTEMPTS_PER_USERNAME (attaque distribuée).
LOGIN_MAX_ATTEMPTS = env_int("DJANGO_LOGIN_MAX_ATTEMPTS", 5)
LOGIN_MAX_ATTEMPTS_PER_IP = env_int("DJANGO_LOGIN_MAX_ATTEMPTS_PER_IP", 20)
LOGIN_MAX_ATTEMPTS_PER_USERNAME = env_int("DJANGO_LOGIN_MAX_ATTEMPTS_PER_USERNAME", 20)
LOGIN_LOCKOUT_SECONDS = env_int("DJANGO_LOGIN_LOCKOUT_SECONDS", 300)  # 5 minutes
# Durée de validité du cookie « appareil de confiance » posé après une connexion réussie.
LOGIN_TRUSTED_DEVICE_DAYS = env_int("DJANGO_LOGIN_TRUSTED_DEVICE_DAYS", 30)

# Adresse IP réelle du client derrière un proxy inverse (voir accounts/netutils.py).
# Les en-têtes de proxy ne sont lus que si DJANGO_BEHIND_PROXY=1 ET si la connexion TCP vient
# d'un proxy de confiance : DJANGO_TRUSTED_PROXIES (IP ou réseaux CIDR, séparés par des virgules).
# Vide = loopback + réseaux privés (cas courant : nginx sur la même machine ou en conteneur).
TRUSTED_PROXIES = env_list("DJANGO_TRUSTED_PROXIES")
# En-tête portant l'IP du client : X-Forwarded-For (liste), ou X-Real-IP / CF-Connecting-IP (valeur unique).
PROXY_IP_HEADER = os.environ.get("DJANGO_PROXY_IP_HEADER", "").strip() or "X-Forwarded-For"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "webapp",
    "accounts",
    "language",
    "editor",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "accounts.middleware.StrictLoginRequiredMiddleware",  # après AuthenticationMiddleware : refus par défaut
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # base.html et partials partagés
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# ---------------------------------------------------------------------------
# Cache Django : stocke les compteurs de tentatives de connexion.
# Il doit être PARTAGÉ entre tous les processus (sinon chaque worker a son propre compteur
# et la limite est multipliée par leur nombre) et offrir un incr() atomique.
#   DJANGO_CACHE_URL=redis://127.0.0.1:6379/1          (recommandé ; pip install redis)
#   DJANGO_CACHE_URL=memcached://127.0.0.1:11211        (pip install pymemcache)
#   vide = mémoire locale : acceptable en développement, un seul processus.
# ---------------------------------------------------------------------------
def cache_from_url(url: str) -> dict:
    url = (url or "").strip()
    if not url:
        return {"BACKEND": "django.core.cache.backends.locmem.LocMemCache", "LOCATION": "code-learning"}
    scheme, _, rest = url.partition("://")
    if scheme in ("redis", "rediss"):
        return {"BACKEND": "django.core.cache.backends.redis.RedisCache", "LOCATION": url,
                "KEY_PREFIX": "code-learning"}
    if scheme == "memcached" and rest:
        return {"BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
                "LOCATION": [host.strip() for host in rest.split(",") if host.strip()],
                "KEY_PREFIX": "code-learning"}
    raise ImproperlyConfigured("DJANGO_CACHE_URL doit commencer par redis://, rediss:// ou memcached://.")


CACHES = {"default": cache_from_url(os.environ.get("DJANGO_CACHE_URL", ""))}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "fr"
TIME_ZONE = "Indian/Antananarivo"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "webapp" / "static",
    BASE_DIR / "language" / "static",
    BASE_DIR / "editor" / "static",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------------------------------------------------------------------
# API REST : réservée aux utilisateurs connectés, JSON uniquement.
# SessionAuthentication401 : un anonyme reçoit 401 (et non 403) ; le middleware ci-dessus le refuse déjà
# avant la vue, ces réglages DRF sont la seconde barrière.
# ---------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ["accounts.authentication.SessionAuthentication401"],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
}

# ---------------------------------------------------------------------------
# Import .zip de l'éditeur : plafonds contre les archives piégées (« zip bombs »)
# ---------------------------------------------------------------------------
EDITOR_ZIP_MAX_UPLOAD_BYTES = env_int("EDITOR_ZIP_MAX_UPLOAD_KB", 5 * 1024) * 1024   # fichier envoyé
EDITOR_ZIP_MAX_ENTRIES = env_int("EDITOR_ZIP_MAX_ENTRIES", 100)                       # fichiers dans l'archive
EDITOR_ZIP_MAX_FILE_BYTES = env_int("EDITOR_ZIP_MAX_FILE_KB", 1024) * 1024            # un fichier décompressé
EDITOR_ZIP_MAX_TOTAL_BYTES = env_int("EDITOR_ZIP_MAX_TOTAL_KB", 5 * 1024) * 1024      # total décompressé
