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
if env_bool("DJANGO_BEHIND_PROXY", False):
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_AGE = env_int("DJANGO_SESSION_HOURS", 168) * 3600
CSRF_COOKIE_SAMESITE = "Lax"  # lisible par le JavaScript de l'éditeur (CSRF_COOKIE_HTTPONLY=False)
X_FRAME_OPTIONS = "DENY"

# ---------------------------------------------------------------------------
# Authentification : toute page exige une connexion (LoginRequiredMiddleware)
# ---------------------------------------------------------------------------
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "login"
LOGIN_MAX_ATTEMPTS = env_int("DJANGO_LOGIN_MAX_ATTEMPTS", 5)
LOGIN_LOCKOUT_SECONDS = env_int("DJANGO_LOGIN_LOCKOUT_SECONDS", 900)

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
    "django.contrib.auth.middleware.LoginRequiredMiddleware",
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
# API REST : réservée aux utilisateurs connectés, JSON uniquement
# ---------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ["rest_framework.authentication.SessionAuthentication"],
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
