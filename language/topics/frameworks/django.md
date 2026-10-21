<div align="center">

# 🎸 Django — Guide complet

**Des premiers pas au déploiement : ORM, API, JWT, tâches asynchrones, tests et écosystème**

*Mis à jour pour Django 6.1 (octobre 2026)*

</div>

---

## 🗂️ Sommaire

**🟢 Fondamentaux**

1. [Introduction à Django](#1-introduction-à-django)
2. [Environnement de développement et outillage des éditeurs](#2-environnement-de-développement-et-outillage-des-éditeurs)
3. [Structure d'un projet et d'applications](#3-structure-dun-projet-et-dapplications)
4. [Configuration (`settings.py`)](#4-configuration-settingspy)
5. [URLs et routage](#5-urls-et-routage)
6. [Vues](#6-vues)
7. [Templates](#7-templates)

**🟡 Données et interface**

8. [Modèles](#8-modèles)
9. [ORM : requêtes et optimisation](#9-orm--requêtes-et-optimisation)
10. [Interface d'administration](#10-interface-dadministration)
11. [Formulaires](#11-formulaires)
12. [Authentification et autorisation](#12-authentification-et-autorisation)
13. [Messages, sessions et cache](#13-messages-sessions-et-cache)
14. [Fichiers statiques et médias](#14-fichiers-statiques-et-médias)
15. [Middleware](#15-middleware)
16. [Signaux](#16-signaux)
17. [Internationalisation et localisation](#17-internationalisation-et-localisation)
18. [Commandes de gestion personnalisées](#18-commandes-de-gestion-personnalisées)

**🔴 API, asynchrone et frontend**

19. [API REST avec Django REST Framework](#19-api-rest-avec-django-rest-framework)
20. [Authentification des API : JWT et alternatives](#20-authentification-des-api--jwt-et-alternatives)
21. [Django Ninja, GraphQL et API externes](#21-django-ninja-graphql-et-api-externes)
22. [Programmation asynchrone, ASGI et WebSockets](#22-programmation-asynchrone-asgi-et-websockets)
23. [Tâches en arrière-plan](#23-tâches-en-arrière-plan)
24. [Frontend moderne avec Django](#24-frontend-moderne-avec-django)

**🛡️ Qualité et production**

25. [Tests](#25-tests)
26. [Sécurité](#26-sécurité)
27. [Performances](#27-performances)
28. [Déploiement](#28-déploiement)
29. [Écosystème : paquets essentiels](#29-écosystème--paquets-essentiels)
30. [Nouveautés par version, bonnes pratiques et ressources](#30-nouveautés-par-version-bonnes-pratiques-et-ressources)

> 💡 **Légende** : *(ajout)* = notion absente du guide d'origine ; *(à jour)* = pratique moderne remplaçant une ancienne ; *(5.x / 6.x)* = version de Django qui introduit la fonctionnalité.
>
> 📌 Les exemples utilisent un projet fil rouge en français (blog et boutique). Vérifiez les détails des nouveautés récentes sur la documentation officielle : [docs.djangoproject.com](https://docs.djangoproject.com/fr/).

---

# 🟢 Fondamentaux

---

# 1. Introduction à Django

## 1.1 Qu'est-ce que Django ?

**Django** est un **framework web Python** « tout inclus » (*batteries included*), de haut niveau, qui encourage un développement **rapide**, **sûr** et **propre**. Il fournit nativement :

| Domaine | Ce que Django apporte |
| --- | --- |
| **Données** | **ORM**, migrations automatiques, validation |
| **Interface d'administration** | Générée automatiquement à partir des modèles |
| **Routage et vues** | Routage par URL, vues fonctions et classes |
| **Templates** | Langage de gabarits (DTL) sécurisé |
| **Formulaires** | Génération, validation, protection CSRF |
| **Authentification** | Utilisateurs, groupes, permissions, sessions |
| **Sécurité** | Protections XSS, CSRF, injection SQL, clickjacking, HTTPS/HSTS, CSP |
| **Internationalisation** | Traduction, fuseaux horaires, formats locaux |
| **Outils** | Serveur de développement, tests, commandes de gestion, cache, e-mail, signaux |
| **Asynchrone** | ASGI, vues et ORM asynchrones, tâches en arrière-plan (6.0) |

> *« Le framework web pour perfectionnistes avec des échéances. »*

## 1.2 Histoire

| Année | Événement |
| --- | --- |
| 2003 | Créé par **Adrian Holovaty** et **Simon Willison** au journal *Lawrence Journal-World* (Kansas) |
| 2005 | Publié en **open source** (licence BSD) ; nommé d'après le guitariste **Django Reinhardt** |
| 2008 | Création de la **Django Software Foundation** (DSF) |
| 2017 | Django **2.0** : Python 3 uniquement, nouvelle syntaxe `path()` |
| 2019 | Django 3.0 : **ASGI** |
| 2021 | Django 4.0 ; **4.2 LTS** en 2023 |
| 2024–2025 | Django 5.0 → **5.2 LTS** (avril 2025) |
| **2025–2026** | **Django 6.0** (décembre 2025) puis **6.1** (5 août 2026) |

## 1.3 Versions et support *(à jour)*

Django publie une version **tous les 8 mois** ; certaines sont des **LTS** (*Long Term Support*, support de sécurité d'au moins 3 ans).

| Version | Sortie | Type | Fin du support | Python |
| --- | --- | --- | --- | --- |
| 4.2 | avril 2023 | LTS | ❌ terminé (avril 2026) | 3.8 – 3.12 |
| **5.2** | avril 2025 | **LTS** | **avril 2028** | 3.10 – 3.13 |
| 6.0 | déc. 2025 | Standard | 2027 | **3.12 – 3.14** |
| **6.1** | **5 août 2026** | Standard | fin 2027 | 3.12 – 3.14 |
| **6.2** | avril 2027 (prévue) | **LTS** | ≥ 3 ans après sa sortie | 3.12 – 3.14 |

> 📌 **Recommandations** : nouveau projet → **la dernière version stable (6.1)** ; production à long terme → **5.2 LTS** (puis 6.2 LTS). **Appliquez toujours les correctifs de sécurité** (ex. : 6.1.2 du 6 octobre 2026) : voir [section 26](#26-sécurité).

## 1.4 Le modèle MTV

Django suit le motif **MTV** (**M**odèle – **T**emplate – **V**ue), variante de MVC :

| Django | MVC équivalent | Rôle |
| --- | --- | --- |
| **Modèle** (*Model*) | Modèle | Structure des données et accès à la base |
| **Template** | Vue | Présentation (HTML) |
| **Vue** (*View*) | Contrôleur | Logique : reçoit la requête, renvoie la réponse |
| **URLconf** | Routage | Associe URL → vue |

```text
Requête HTTP
   │
   ▼
Middleware ──▶ URLconf (urls.py) ──▶ Vue (views.py) ──▶ Modèle (ORM) ──▶ Base de données
                                          │
                                          ▼
                                  Template (HTML) ──▶ Réponse HTTP ──▶ Middleware ──▶ Navigateur
```

## 1.5 Principes de conception

- **DRY** (*Don't Repeat Yourself*) et **couplage faible**.
- **Explicite plutôt qu'implicite**.
- **Convention plutôt que configuration** (structure de projet standardisée).
- **Sécurité par défaut**.
- Applications **réutilisables** (un projet = une collection d'« apps »).

## 1.6 Django face aux autres frameworks

| | **Django** | **Flask** | **FastAPI** | **Laravel** (PHP) | **Rails** (Ruby) |
| --- | --- | --- | --- | --- | --- |
| Philosophie | Tout inclus | Micro-framework | API asynchrone + types | Tout inclus | Tout inclus |
| ORM / admin intégrés | ✅ / ✅ | ❌ (extensions) | ❌ | ✅ / ❌ | ✅ / ❌ |
| Idéal pour | Sites complets, back-offices, API (+ DRF/Ninja) | Petits services, prototypes | **API** performantes, validation de données | Sites PHP | Sites Ruby |
| Courbe d'apprentissage | Moyenne | Faible | Faible à moyenne | Moyenne | Moyenne |

> ✅ **Quand choisir Django ?** Applications avec **base de données**, **administration**, **authentification**, **contenu** ; équipes qui veulent une **structure éprouvée** et une **sécurité solide**. Utilisé par **Instagram**, **Pinterest**, **Mozilla**, **Disqus**, **NASA**, etc.

---

# 2. Environnement de développement et outillage des éditeurs

## 2.1 Prérequis

- **Python** compatible avec votre version de Django (3.12 ou plus pour Django 6.x ; voir 1.3).
- **PostgreSQL** pour la production (SQLite suffit pour apprendre).
- **Git**, un éditeur de code.

```bash
python --version
```

## 2.2 Environnement virtuel et installation *(à jour)*

Isolez **chaque projet** dans un environnement virtuel.

### Avec `uv` (moderne, très rapide) ✅

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh        # installer uv (ou : pip install uv)
uv init mon-site && cd mon-site
uv add django                                           # ajoute Django à pyproject.toml + crée .venv
uv run django-admin startproject config .
uv run python manage.py runserver
```

### Avec `venv` + `pip` (classique)

```bash
python -m venv .venv
source .venv/bin/activate              # Linux/macOS
.venv\Scripts\activate                 # Windows
pip install "django>=6.1,<6.2"
pip freeze > requirements.txt          # ou mieux : pyproject.toml + lock (uv, pip-tools, Poetry)
django-admin --version
```

> ✅ **Épinglez** vos dépendances (fichier de verrouillage `uv.lock` / `poetry.lock` / `requirements.txt` généré) et **ne versionnez jamais** `.venv/`.

## 2.3 Créer un projet et une application

```bash
django-admin startproject config .            # le « . » crée le projet dans le dossier courant
python manage.py startapp blog                # une application
python manage.py runserver                    # http://127.0.0.1:8000
```

```python
# config/settings.py
INSTALLED_APPS = [
    "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes",
    "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles",
    "blog",                                    # ← enregistrer l'application (ou "blog.apps.BlogConfig")
]
```

```bash
python manage.py migrate                      # crée les tables de base
python manage.py createsuperuser              # compte administrateur
python manage.py check                        # vérifie la configuration
```

### Commandes `manage.py` essentielles

| Commande | Rôle |
| --- | --- |
| `runserver [port]` | Serveur de développement (rechargement automatique) |
| `makemigrations` / `migrate` | Créer / appliquer les migrations |
| `createsuperuser`, `changepassword` | Gestion des comptes |
| `shell` | Console Python avec Django chargé (**importe automatiquement les modèles** depuis Django 5.2) |
| `startapp`, `startproject` | Générer des squelettes |
| `collectstatic` | Rassembler les fichiers statiques |
| `test` | Lancer les tests |
| `check [--deploy]` | Contrôles système (et contrôles de déploiement) |
| `dumpdata` / `loaddata` | Exporter / importer des fixtures |
| `makemessages` / `compilemessages` | Traductions |
| `dbshell`, `sqlmigrate`, `showmigrations`, `inspectdb`, `flush` | Base de données |

## 2.4 Outillage des éditeurs : stubs de types et analyse *(ajout)*

Django repose beaucoup sur la **métaprogrammation** (champs de modèles, gestionnaires `objects`, relations inverses) : sans aide, les éditeurs et vérificateurs de types **ne comprennent pas** `Article.objects.filter(...)`, `article.auteur`, `request.user`. Il faut donc des **stubs de types** et l'**analyse du projet**.

### Paquets à installer (environnement de développement)

```bash
uv add --dev django-stubs[compatible-mypy] djangorestframework-stubs mypy
uv add --dev ruff django-debug-toolbar django-extensions ipython pytest-django
uv add --dev djlint                                       # linter/formateur de templates Django
# Optionnels :
uv add --dev pyright                                      # (ou basedpyright) vérificateur de types alternatif
uv add --dev django-types                                 # alternative à django-stubs pour pyright / Pylance
```

| Paquet | Rôle |
| --- | --- |
| **`django-stubs`** (+ extra `compatible-mypy`) | **Stubs de types** de Django et **plugin mypy** (comprend l'ORM, `settings`, `request.user`…) |
| **`djangorestframework-stubs`** | Stubs et plugin mypy pour **DRF** |
| **`mypy`** | Vérificateur de types (utilise les plugins Django) |
| **`pyright`** / **`basedpyright`** + **`django-types`** | Alternative : fonctionne avec **Pylance (VS Code)** et les clients **LSP de Vim/Neovim** |
| **`ruff`** | Linter + formateur **ultra-rapide** (règles `DJ` = bonnes pratiques Django, remplace flake8, isort, black) |
| **`djlint`** | Formatage et lint des **templates** `.html` Django |
| **`django-extensions`** | `shell_plus` (importe tous les modèles), `runserver_plus`, `graph_models`, `show_urls` |
| **`django-debug-toolbar`** | Barre de débogage : requêtes SQL, templates, cache |
| **`ipython`** | Shell interactif plus confortable |
| **`pre-commit`** | Exécute ruff / mypy / djlint avant chaque commit |

### Configuration de mypy avec `django-stubs`

```toml
# pyproject.toml
[tool.mypy]
python_version = "3.13"
strict = true
plugins = ["mypy_django_plugin.main", "mypy_drf_plugin.main"]

[tool.django-stubs]
django_settings_module = "config.settings"                 # ⚠️ obligatoire : chemin Python vers settings
```

```bash
mypy .                                                      # vérification des types
```

Annoter les modèles et gestionnaires :

```python
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import AbstractUser

class Article(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="articles")

    objects: models.Manager["Article"]                      # précise le gestionnaire pour certains outils

def accueil(request: HttpRequest) -> HttpResponse: ...
```

### Pyright / Pylance (VS Code) / LSP (Vim, Neovim)

```json
// pyrightconfig.json  (ou [tool.pyright] dans pyproject.toml)
{
    "include": ["config", "blog"],
    "venvPath": ".",
    "venv": ".venv",
    "pythonVersion": "3.13",
    "typeCheckingMode": "standard"
}
```

Avec **`django-types`** installé, Pyright/Pylance comprend l'ORM sans plugin.

### Vim / Neovim *(ajout)*

Vim ne « comprend » pas Django seul : il faut un **client LSP** et des **serveurs de langage** installés dans votre environnement.

| Besoin | Outil | Remarque |
| --- | --- | --- |
| **Complétion / types Python** | Serveur **Pyright** (`pyright-langserver`) ou **basedpyright**, ou **Pylsp** + `pylsp-mypy` | Installer **`django-stubs`** / **`django-types`** dans le **même venv** que le projet |
| **Lint et formatage** | **`ruff server`** (serveur LSP intégré à ruff) | Remplace `ruff-lsp` |
| **Templates Django** | **`djlsp`** (*django-template-lsp*) + **`djlint`** | Complétion de balises, filtres, `{% url %}`, `{% static %}` |
| **Détection de filetype** | Associer `*.html` des templates à `htmldjango` | Voir ci-dessous |
| **Plugins** | `nvim-lspconfig`, `mason.nvim`, `nvim-cmp`, `conform.nvim`, `nvim-lint` | Neovim ; clients LSP : **coc.nvim**, **vim-lsp**, **ALE** pour Vim |

```lua
-- Neovim (nvim-lspconfig) : exemple minimal
local lsp = require("lspconfig")
lsp.pyright.setup({
    settings = { python = { analysis = { typeCheckingMode = "standard", autoSearchPaths = true, useLibraryCodeForTypes = true } } },
})
lsp.ruff.setup({})                                          -- ruff server (lint + format)
lsp.djlsp.setup({                                           -- templates Django
    init_options = { django_settings_module = "config.settings" },
})

vim.filetype.add({ pattern = { [".*/templates/.*%.html"] = "htmldjango" } })     -- templates → htmldjango
```

```vim
" Vim classique : associer les templates (dans ~/.vimrc ou un autocmd)
autocmd BufRead,BufNewFile */templates/*.html set filetype=htmldjango
```

> ⚠️ **Trois pièges fréquents** : (1) l'éditeur doit utiliser **l'interpréteur du venv** du projet (sinon les stubs sont introuvables) ; (2) `DJANGO_SETTINGS_MODULE` doit être renseigné (pour `djlsp`, `django-stubs`, `pytest-django`) ; (3) lancez le serveur LSP **depuis la racine du projet** (là où se trouvent `manage.py` et `pyproject.toml`).

### VS Code et PyCharm

- **VS Code** : extensions **Python**, **Pylance**, **Ruff**, **Django** (Baptiste Darthenay) ou **Django Template** pour la coloration, **djLint**. Réglage utile :
  ```json
  { "python.defaultInterpreterPath": ".venv/bin/python",
    "files.associations": { "**/templates/**/*.html": "django-html" },
    "[django-html]": { "editor.defaultFormatter": "monosans.djlint" },
    "[python]": { "editor.defaultFormatter": "charliermarsh.ruff" } }
  ```
- **PyCharm Professional** : support Django intégré (templates, ORM, console, débogueur, `manage.py`) ; l'édition Community nécessite les stubs.

### Configuration de Ruff

```toml
# pyproject.toml
[tool.ruff]
target-version = "py313"
line-length = 100
extend-exclude = ["migrations"]

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP", "DJ", "S", "C4", "SIM"]      # DJ = flake8-django ; S = bandit (sécurité)
ignore = ["S101"]                                                  # assert autorisé (tests)
```

### Hooks `pre-commit`

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.14.0                       # à ajuster
    hooks: [{ id: ruff-check, args: [--fix] }, { id: ruff-format }]
  - repo: https://github.com/adamchainz/django-upgrade
    rev: 1.25.0                        # à ajuster
    hooks: [{ id: django-upgrade, args: [--target-version, "6.1"] }]
  - repo: https://github.com/djlint/djLint
    rev: v1.36.4                       # à ajuster
    hooks: [{ id: djlint-django }]
```

> 💡 **`django-upgrade`** réécrit automatiquement votre code vers les API récentes de Django.

## 2.5 Outils de débogage

```python
# settings.py (développement uniquement)
INSTALLED_APPS += ["debug_toolbar", "django_extensions"]
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
INTERNAL_IPS = ["127.0.0.1"]

# urls.py
from django.conf import settings
if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
```

```bash
python manage.py shell_plus --print-sql          # shell avec tous les modèles et affichage du SQL
python manage.py show_urls                       # toutes les routes
python manage.py graph_models -a -o modeles.png  # diagramme des modèles
python -m pdb manage.py runserver --noreload     # débogueur ; ou breakpoint() dans le code
```

## 2.6 Modèles de projet

| Outil | Apport |
| --- | --- |
| **`cookiecutter-django`** | Gabarit de projet **complet pour la production** (Docker, Celery, DRF, Sentry, tests, CI) |
| `django-admin startproject --template` | Votre propre gabarit |
| **`copier`**, **`django-startproject`** | Gabarits mis à jour de façon incrémentale |

---

# 3. Structure d'un projet et d'applications

## 3.1 Projet ≠ application

| | **Projet** | **Application** (*app*) |
| --- | --- | --- |
| Définition | Ensemble de la configuration et des apps | **Module Python** qui fait **une chose** (blog, comptes, paiement) |
| Nombre | 1 | **Plusieurs**, réutilisables |
| Contient | `settings.py`, `urls.py`, `wsgi.py`, `asgi.py` | `models.py`, `views.py`, `urls.py`, `admin.py`, `tests`, `migrations/`… |

## 3.2 Arborescence générée

```text
mon-site/
├── manage.py                    ← outil en ligne de commande
├── pyproject.toml
├── config/                      ← paquet du PROJET (renommé « config » avec startproject config .)
│   ├── __init__.py
│   ├── settings.py              ← configuration
│   ├── urls.py                  ← routes racine
│   ├── wsgi.py                  ← point d'entrée WSGI (serveurs synchrones)
│   └── asgi.py                  ← point d'entrée ASGI (async, WebSockets)
└── blog/                        ← une application
    ├── __init__.py
    ├── admin.py                 ← enregistrement dans l'admin
    ├── apps.py                  ← classe de configuration (AppConfig)
    ├── models.py                ← modèles
    ├── views.py                 ← vues
    ├── tests.py                 ← tests
    ├── urls.py                  ← (à créer) routes de l'app
    ├── forms.py                 ← (à créer) formulaires
    ├── migrations/              ← historique du schéma
    ├── templates/blog/          ← (à créer) templates
    └── static/blog/             ← (à créer) fichiers statiques
```

## 3.3 Rôle des fichiers du projet

| Fichier | Rôle |
| --- | --- |
| `manage.py` | Exécute les commandes (`python manage.py <commande>`) |
| `settings.py` | Configuration (applications, base, middleware, templates, sécurité…) |
| `urls.py` | Routage racine (`urlpatterns`) |
| `wsgi.py` | Interface **WSGI** (Gunicorn, uWSGI) : `application` |
| `asgi.py` | Interface **ASGI** (Uvicorn, Daphne, Hypercorn) : `application` |
| `__init__.py` | Marque un dossier comme **paquet** Python ; sert à initialiser (ex. Celery) |

## 3.4 La classe `AppConfig`

```python
# blog/apps.py
from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"     # type des clés primaires automatiques
    name = "blog"
    verbose_name = "Blog"

    def ready(self) -> None:                                  # exécuté au démarrage : branchement des signaux, vérifications
        from . import signals  # noqa: F401
```

> 📌 Depuis Django **6.0**, `BigAutoField` est le type **par défaut** des clés automatiques (aucune configuration nécessaire pour les nouveaux projets).

## 3.5 Organisation recommandée pour un projet réel *(à jour)*

```text
mon-site/
├── manage.py
├── pyproject.toml / uv.lock
├── .env.example                     ← modèle de variables d'environnement (jamais .env lui-même dans Git)
├── Dockerfile · compose.yaml
├── config/
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py                  ← réglages communs
│   │   ├── dev.py                   ← développement
│   │   ├── prod.py                  ← production
│   │   └── test.py                  ← tests
│   ├── urls.py · wsgi.py · asgi.py · celery.py
├── apps/
│   ├── comptes/                     ← utilisateurs, profils
│   ├── blog/
│   └── boutique/
├── templates/                       ← templates globaux (base.html, 404.html…)
├── static/                          ← statiques globaux
├── locale/                          ← traductions
└── tests/                           ← tests d'intégration transverses
```

- **Une app = une responsabilité** ; noms **courts, au pluriel ou métier** (`comptes`, `commandes`).
- Enregistrez-les avec `"apps.blog"` (et `name = "apps.blog"` dans `AppConfig`).
- Mettez la **logique métier** dans des **services** (`services.py`) ou dans les modèles/gestionnaires, pas dans les vues.

## 3.6 Un modèle utilisateur personnalisé dès le départ

> 🚫 **Faites-le avant la première migration** : changer le modèle utilisateur en cours de projet est très pénible.

```python
# apps/comptes/models.py
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    pass                                                       # ajoutez ensuite vos champs

# settings.py
AUTH_USER_MODEL = "comptes.Utilisateur"
```

Voir [section 12](#12-authentification-et-autorisation).

---

# 4. Configuration (`settings.py`)

## 4.1 Réglages essentiels

```python
# config/settings/base.py
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(BASE_DIR / ".env")                        # django-environ : lit le fichier .env

SECRET_KEY = env("SECRET_KEY")                                 # ⚠️ jamais dans le code ni dans Git
DEBUG = env("DEBUG")                                           # False en production !
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

LANGUAGE_CODE = "fr"
TIME_ZONE = "Europe/Paris"
USE_I18N = True
USE_TZ = True                                                  # ✅ toujours : datetimes en UTC en base, convertis à l'affichage
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
```

| Réglage | Rôle |
| --- | --- |
| `SECRET_KEY` | Signature des sessions, jetons, mots de passe oubliés : **secrète et unique** |
| `DEBUG` | Pages d'erreur détaillées : **`False` en production** (sinon fuite d'informations) |
| `ALLOWED_HOSTS` | Noms d'hôte autorisés (obligatoire quand `DEBUG = False`) |
| `ROOT_URLCONF` | Module des routes racine |
| `USE_TZ` | Datetimes **aware** (recommandé ; `True` par défaut depuis Django 5.0) |

## 4.2 Applications installées et middleware

```python
INSTALLED_APPS = [
    # Django
    "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes",
    "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles",
    # Tiers
    "rest_framework", "corsheaders", "django_filters", "django_htmx",
    # Vos applications
    "apps.comptes", "apps.blog",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",              # statiques en production (juste après Security)
    "corsheaders.middleware.CorsMiddleware",                   # CORS (avant CommonMiddleware)
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.LoginRequiredMiddleware",  # (5.1) exige la connexion par défaut
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.csp.ContentSecurityPolicyMiddleware",   # (6.0) en-tête CSP
    "django_htmx.middleware.HtmxMiddleware",
]
```

> ⚠️ **L'ordre du middleware compte** (descente à la requête, remontée à la réponse). Voir [section 15](#15-middleware).

## 4.3 Base de données

```python
import dj_database_url

DATABASES = {
    "default": dj_database_url.config(default=env("DATABASE_URL"), conn_max_age=600, conn_health_checks=True),
}
# ou, explicitement :
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"), "USER": env("DB_USER"), "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST", default="localhost"), "PORT": "5432",
        "CONN_MAX_AGE": 0,                                      # avec un pool, laisser à 0
        "OPTIONS": {"pool": True},                              # (5.1) pool de connexions psycopg 3
    }
}
```

| Base | Moteur | Pilote |
| --- | --- | --- |
| **PostgreSQL** ✅ (recommandée) | `django.db.backends.postgresql` | **`psycopg[binary,pool]`** (psycopg **3**) |
| MySQL / MariaDB | `django.db.backends.mysql` | `mysqlclient` |
| SQLite | `django.db.backends.sqlite3` | intégré (développement, petits sites) |
| Oracle | `django.db.backends.oracle` | `oracledb` |
| SQL Server | `mssql-django` | `mssql-django` |

> ✅ **PostgreSQL** pour la production (JSONB, recherche plein texte, index avancés, `django.contrib.postgres`). Installer **`psycopg`** (v3), plus récent que `psycopg2`.

## 4.4 Templates, fichiers statiques, médias, stockage

```python
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.request",
        "django.template.context_processors.csp",              # (6.0) expose csp_nonce
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"                         # cible de collectstatic (production)
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

STORAGES = {                                                   # (4.2+) remplace DEFAULT_FILE_STORAGE / STATICFILES_STORAGE
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}
```

## 4.5 Cache, e-mail, journalisation

```python
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",      # intégré depuis Django 4.0
        "LOCATION": env("REDIS_URL", default="redis://127.0.0.1:6379/1"),
    }
}

# E-mail (configuration classique, valable jusqu'à Django 7.0)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST"); EMAIL_PORT = 587; EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_USER"); EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")
DEFAULT_FROM_EMAIL = "Mon site <noreply@exemple.fr>"
# En développement : EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

> 📌 **Django 6.1** introduit le réglage **`MAILERS`** (plusieurs « expéditeurs » nommés, chacun avec son backend et ses options) qui **remplace** `EMAIL_BACKEND`, `EMAIL_HOST`… ; les anciens réglages **fonctionnent jusqu'à Django 7.0**. Voir la page officielle « *Migrating email to mailers* ».
> Pour un service d'envoi (Mailgun, SES, Brevo…), utilisez **`django-anymail`**.

```python
LOGGING = {
    "version": 1, "disable_existing_loggers": False,
    "formatters": {"simple": {"format": "{asctime} {levelname} {name} {message}", "style": "{"}},
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {"django.request": {"handlers": ["console"], "level": "WARNING", "propagate": False}},
}
```

> ✅ En conteneur / PaaS : journaliser **sur la sortie standard** (console), collectée par la plateforme.

## 4.6 Sécurité (aperçu : détails en section 26)

```python
# config/settings/prod.py
from .base import *

DEBUG = False
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")     # derrière un proxy (Nginx, load balancer)
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ["https://exemple.fr"]                      # schéma obligatoire
SECURE_CONTENT_TYPE_NOSNIFF = True
```

## 4.7 Variables d'environnement et réglages multiples

```bash
# .env  (jamais versionné ; fournir .env.example)
SECRET_KEY=change-me
DEBUG=True
DATABASE_URL=postgres://utilisateur:motdepasse@localhost:5432/monsite
REDIS_URL=redis://localhost:6379/0
ALLOWED_HOSTS=localhost,127.0.0.1
```

| Bibliothèque | Rôle |
| --- | --- |
| **`django-environ`** | Lit `.env`, convertit les types (`env.bool`, `env.list`, `env.db`) |
| **`python-decouple`** | Alternative simple |
| **`dj-database-url`** | Analyse `DATABASE_URL` |
| **`pydantic-settings`** | Configuration typée et validée (approche moderne) |

```bash
DJANGO_SETTINGS_MODULE=config.settings.prod python manage.py check --deploy
```

> 🔒 `python manage.py check --deploy` signale les réglages dangereux pour la production.

## 4.8 Réglages personnalisés

```python
# settings.py
ARTICLES_PAR_PAGE = env.int("ARTICLES_PAR_PAGE", default=10)

# Utilisation
from django.conf import settings
settings.ARTICLES_PAR_PAGE
```

## 4.9 Réglages de bibliothèques tierces

Chaque bibliothèque a son dictionnaire (`REST_FRAMEWORK`, `SIMPLE_JWT`, `CELERY_*`, `CORS_ALLOWED_ORIGINS`, `SPECTACULAR_SETTINGS`…) : voir les sections concernées.

---

# 5. URLs et routage

## 5.1 Principe

Django associe chaque **URL** à une **vue** grâce à des **URLconfs** (`urls.py`). Il parcourt la liste `urlpatterns` **dans l'ordre** et retient la **première** correspondance.

```python
# config/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("apps.blog.urls")),        # délègue à l'application
    path("", include("apps.accueil.urls")),
]
```

```python
# apps/blog/urls.py
from django.urls import path
from . import views

app_name = "blog"                                    # espace de noms : blog:detail

urlpatterns = [
    path("", views.ListeArticles.as_view(), name="liste"),
    path("<int:pk>/", views.DetailArticle.as_view(), name="detail"),
    path("<slug:slug>/", views.detail_par_slug, name="detail-slug"),
    path("archives/<int:annee>/<int:mois>/", views.archives, name="archives"),
]
```

## 5.2 Convertisseurs de chemin

| Convertisseur | Reconnaît | Type Python |
| --- | --- | --- |
| `str` (défaut) | Chaîne non vide **sans** `/` | `str` |
| `int` | Entier ≥ 0 | `int` |
| `slug` | Lettres, chiffres, `-`, `_` | `str` |
| `uuid` | UUID formaté | `uuid.UUID` |
| `path` | Chaîne **avec** `/` | `str` |

```python
path("articles/<int:pk>/", vue)                  # /articles/42/ → vue(request, pk=42)
path("fichiers/<path:chemin>", vue)              # /fichiers/a/b/c.txt
```

### Convertisseur personnalisé

```python
# apps/blog/converters.py
class AnneeQuatreChiffres:
    regex = r"[0-9]{4}"
    def to_python(self, valeur: str) -> int: return int(valeur)
    def to_url(self, valeur: int) -> str: return f"{valeur:04d}"

# urls.py
from django.urls import register_converter
register_converter(AnneeQuatreChiffres, "annee")
path("archives/<annee:annee>/", views.archives)
```

### Expressions régulières : `re_path`

```python
from django.urls import re_path
re_path(r"^articles/(?P<annee>[0-9]{4})/$", views.archives)      # pour les cas complexes seulement
```

## 5.3 Noms d'URL et inversion

**Ne codez jamais une URL en dur** : nommez-la et **inversez-la**.

```python
from django.urls import reverse
reverse("blog:detail", kwargs={"pk": 42})                # "/blog/42/"
reverse("blog:liste")
```

```django
<a href="{% url 'blog:detail' pk=article.pk %}">{{ article.titre }}</a>
```

```python
# Dans un modèle : URL canonique
from django.urls import reverse
class Article(models.Model):
    def get_absolute_url(self) -> str:
        return reverse("blog:detail", kwargs={"pk": self.pk})
```

## 5.4 Redirections et raccourcis

```python
from django.shortcuts import redirect
redirect("blog:liste")                                     # par nom (à retourner depuis la vue : return redirect(...))
redirect("blog:detail", pk=42)
redirect(article)                                          # utilise get_absolute_url()
redirect("https://exemple.com")

from django.views.generic import RedirectView
path("ancienne-page/", RedirectView.as_view(pattern_name="blog:liste", permanent=True))
```

## 5.5 Pages d'erreur personnalisées

```python
# config/urls.py
handler404 = "apps.accueil.views.page_introuvable"
handler500 = "apps.accueil.views.erreur_serveur"
handler403 = "apps.accueil.views.acces_refuse"
handler400 = "apps.accueil.views.mauvaise_requete"
```

Ou simplement créer `templates/404.html` et `500.html`.

## 5.6 Fichiers statiques et médias en développement

```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 5.7 Internationalisation des URL

```python
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns += i18n_patterns(
    path(_("a-propos/"), views.a_propos, name="a-propos"),    # /fr/a-propos/ · /en/about/
    prefix_default_language=False,
)
```

## 5.8 URL pour les API REST

```python
# DRF : routeurs (section 19)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("articles", ArticleViewSet, basename="article")
urlpatterns = [path("api/v1/", include(router.urls))]
```

Conventions : noms de ressources **au pluriel**, **verbes HTTP** pour les actions, versionnement (`/api/v1/`).

## 5.9 Diagnostiquer les problèmes de routage

| Symptôme | Piste |
| --- | --- |
| `404` inattendue | Ordre des motifs, `/` final manquant (`APPEND_SLASH = True` par défaut), `include` mal placé |
| `NoReverseMatch` | Nom ou espace de noms incorrect, arguments manquants |
| Un motif en « masque » un autre | Placer le motif **le plus spécifique** en premier |
| URL non reconnue en `i18n_patterns` | Préfixe de langue manquant |

```bash
python manage.py show_urls            # (django-extensions) liste toutes les routes
```

---

# 6. Vues

## 6.1 Qu'est-ce qu'une vue ?

Une **vue** reçoit un objet **`HttpRequest`** et renvoie un objet **`HttpResponse`** (HTML, JSON, redirection, fichier, erreur).

## 6.2 Vues basées sur des fonctions (FBV)

```python
from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

def liste_articles(request: HttpRequest) -> HttpResponse:
    articles = Article.objects.filter(publie=True).select_related("auteur")
    return render(request, "blog/liste.html", {"articles": articles})

def detail_article(request: HttpRequest, pk: int) -> HttpResponse:
    article = get_object_or_404(Article, pk=pk, publie=True)       # 404 automatique si absent
    return render(request, "blog/detail.html", {"article": article})

def api_articles(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"articles": list(Article.objects.values("id", "titre"))})
```

### Gérer les méthodes HTTP

```python
from django.views.decorators.http import require_http_methods, require_POST, require_GET

@require_http_methods(["GET", "POST"])
def creer_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.auteur = request.user
            article.save()
            return redirect(article)                                # motif Post/Redirect/Get
    else:
        form = ArticleForm()
    return render(request, "blog/formulaire.html", {"form": form})
```

### Objets `request` et réponses utiles

| `request` | Contenu |
| --- | --- |
| `request.method` | `"GET"`, `"POST"`… |
| `request.GET`, `request.POST` | Dictionnaires de paramètres (`QueryDict`) |
| `request.FILES` | Fichiers envoyés |
| `request.body`, `request.headers`, `request.COOKIES`, `request.META` | Corps brut, en-têtes… |
| `request.user`, `request.session` | Utilisateur et session (middlewares) |
| `request.htmx` | Requête HTMX (avec `django-htmx`) |

Réponses : `HttpResponse`, `JsonResponse`, `HttpResponseRedirect`, `FileResponse`, `StreamingHttpResponse`, `HttpResponseNotFound`, `HttpResponseForbidden`, `HttpResponseNotAllowed`, `render()`.

## 6.3 Décorateurs de vue

```python
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.views.decorators.cache import cache_page, never_cache
from django.views.decorators.csrf import csrf_exempt            # ⚠️ à éviter
from django.views.decorators.http import require_POST

@login_required                                                  # redirige vers LOGIN_URL
@permission_required("blog.publish_article", raise_exception=True)
@cache_page(60 * 15)
def tableau_de_bord(request): ...
```

> ✅ Avec **`LoginRequiredMiddleware`** (5.1), toutes les vues exigent la connexion **par défaut** ; exemptez les vues publiques avec `@login_not_required`.

## 6.4 Vues basées sur des classes (CBV)

Une CBV regroupe la logique par **méthode HTTP** et permet l'**héritage** et les **mixins**.

```python
from django.views import View
from django.views.generic import TemplateView

class Accueil(TemplateView):
    template_name = "accueil.html"

    def get_context_data(self, **kwargs):
        contexte = super().get_context_data(**kwargs)
        contexte["derniers"] = Article.objects.publies()[:5]
        return contexte

class ExportCsv(View):
    def get(self, request, *args, **kwargs):
        ...
    def post(self, request, *args, **kwargs):
        ...
```

```python
path("", Accueil.as_view(), name="accueil")                     # toujours as_view()
```

## 6.5 Vues génériques

| Vue | Usage |
| --- | --- |
| `TemplateView` | Page statique avec contexte |
| `ListView` | Liste d'objets (pagination incluse) |
| `DetailView` | Un objet |
| `CreateView` / `UpdateView` / `DeleteView` | Formulaires CRUD |
| `FormView` | Formulaire sans modèle |
| `RedirectView` | Redirection |
| `ArchiveIndexView`, `YearArchiveView`, `MonthArchiveView`… | Archives par date |

```python
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class ListeArticles(ListView):
    model = Article
    template_name = "blog/liste.html"
    context_object_name = "articles"
    paginate_by = 10
    ordering = ["-publie_le"]

    def get_queryset(self):
        qs = super().get_queryset().filter(publie=True).select_related("auteur")
        if q := self.request.GET.get("q"):
            qs = qs.filter(titre__icontains=q)
        return qs

class DetailArticle(DetailView):
    model = Article                                              # template par défaut : blog/article_detail.html
    queryset = Article.objects.filter(publie=True)

class CreerArticle(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("blog:liste")

    def form_valid(self, form):
        form.instance.auteur = self.request.user
        return super().form_valid(form)

class ModifierArticle(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ["titre", "contenu"]
    def test_func(self) -> bool:
        return self.get_object().auteur == self.request.user     # seul l'auteur peut modifier
```

> ⚠️ Dans les classes, **placez les mixins d'accès avant la vue générique** (`LoginRequiredMixin, CreateView`).
> 💡 La [référence « ccbv.co.uk »](https://ccbv.co.uk) montre toutes les méthodes et attributs de chaque vue générique.

### FBV ou CBV ?

| | **FBV** | **CBV** |
| --- | --- | --- |
| Lisibilité | ✅ Explicite, simple | Plus abstraite (héritage) |
| Réutilisation | Décorateurs, fonctions | ✅ Mixins, héritage |
| CRUD standard | Plus de code | ✅ Très concis |
| Cas particuliers | ✅ Plus souple | Peut devenir complexe |

> ✅ Règle pratique : **CBV génériques** pour le CRUD standard, **FBV** pour la logique atypique.

## 6.6 Vues asynchrones *(ajout)*

```python
async def statut(request):
    articles = [a async for a in Article.objects.filter(publie=True)[:5]]       # ORM asynchrone
    total = await Article.objects.acount()
    return JsonResponse({"total": total, "titres": [a.titre for a in articles]})
```

Voir [section 22](#22-programmation-asynchrone-asgi-et-websockets).

## 6.7 Gestion des erreurs dans les vues

```python
from django.core.exceptions import PermissionDenied, ValidationError
from django.http import Http404

def vue(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        raise Http404("Article introuvable")
    if not request.user.has_perm("blog.view_article"):
        raise PermissionDenied                                    # → 403
```

## 6.8 Organiser les vues

- Une app avec beaucoup de vues : **un paquet** `views/` (`views/articles.py`, `views/commentaires.py`) réexportées dans `__init__.py`.
- **Vues minces** : validation dans les **formulaires**, requêtes dans les **gestionnaires / QuerySets**, logique métier dans des **services**.

---

# 7. Templates

## 7.1 Le langage de templates Django (DTL)

Un **template** est un fichier texte (HTML) contenant des **variables** `{{ }}`, des **balises** `{% %}` et des **filtres** `|`.

```django
{# Commentaire #}
<h1>{{ article.titre|title }}</h1>
<p>Publié le {{ article.publie_le|date:"d/m/Y" }} par {{ article.auteur.get_full_name|default:"anonyme" }}</p>

{% if articles %}
    <ul>
    {% for a in articles %}
        <li class="{% cycle 'pair' 'impair' %}">{{ forloop.counter }}. <a href="{% url 'blog:detail' pk=a.pk %}">{{ a.titre }}</a></li>
    {% empty %}
        <li>Aucun article.</li>
    {% endfor %}
    </ul>
{% else %}
    <p>Rien à afficher.</p>
{% endif %}
```

> 🔒 **Échappement automatique** : `{{ variable }}` échappe le HTML (protection XSS). N'utilisez `|safe` ou `{% autoescape off %}` que pour du contenu **de confiance**.

## 7.2 Héritage de templates

```django
{# templates/base.html #}
{% load static %}
<!DOCTYPE html>
<html lang="{{ LANGUAGE_CODE }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block titre %}Mon site{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/site.css' %}">
    {% block extra_head %}{% endblock %}
</head>
<body>
    {% include "partials/navigation.html" %}
    {% if messages %}{% for m in messages %}<div class="alerte {{ m.tags }}">{{ m }}</div>{% endfor %}{% endif %}
    <main>{% block contenu %}{% endblock %}</main>
    {% block scripts %}{% endblock %}
</body>
</html>
```

```django
{# blog/templates/blog/liste.html #}
{% extends "base.html" %}
{% block titre %}Articles — {{ block.super }}{% endblock %}
{% block contenu %}
    {% for article in articles %}{% include "blog/_carte.html" with article=article only %}{% endfor %}
{% endblock %}
```

- `{% extends %}` doit être la **première** balise du fichier.
- `{% include "x.html" with a=1 only %}` : `only` limite le contexte.
- **Organisation** : `templates/` (global) et `app/templates/app/` (**espace de noms** : évite les collisions).

## 7.3 Balises et filtres intégrés

| Balises | Rôle |
| --- | --- |
| `if / elif / else`, `for / empty`, `with`, `block`, `extends`, `include` | Contrôle et structure |
| `url`, `static`, `csrf_token`, `load`, `now`, `cycle`, `firstof`, `ifchanged`, `regroup`, `spaceless`, `verbatim`, `widthratio`, `comment`, `autoescape` | Utilitaires |
| **`querystring`** *(5.1)* | Construire/modifier la chaîne de requête (pagination, filtres) |
| **`partialdef` / `partial`** *(6.0)* | **Fragments** nommés de template réutilisables |

| Filtres courants | |
| --- | --- |
| `default`, `default_if_none`, `length`, `first`, `last`, `join`, `slice`, `dictsort` | Valeurs et listes |
| `lower`, `upper`, `title`, `capfirst`, `truncatechars`, `truncatewords`, `slugify`, `linebreaks`, `urlize`, `wordcount` | Texte |
| `date`, `time`, `timesince`, `timeuntil` | Dates |
| `floatformat`, `intcomma`, `filesizeformat`, `pluralize` | Nombres |
| `safe`, `escape`, `escapejs`, `json_script` | Sécurité / JS |

```django
{# Pagination qui conserve les autres paramètres : balise querystring (5.1) #}
<a href="{% querystring page=page_obj.next_page_number %}">Suivant</a>

{# Passer des données à JavaScript en toute sécurité #}
{{ donnees|json_script:"donnees-page" }}
<script>const donnees = JSON.parse(document.getElementById("donnees-page").textContent);</script>
```

## 7.4 Fragments de template : `partialdef` *(6.0, à jour)*

Définissez un **fragment nommé** dans un template et **rendez-le seul** : idéal avec **HTMX** (réponses partielles).

```django
{# blog/liste.html #}
{% extends "base.html" %}
{% block contenu %}
    {% partialdef liste-articles inline %}
        <ul id="articles">{% for a in articles %}<li>{{ a.titre }}</li>{% endfor %}</ul>
    {% endpartialdef %}
{% endblock %}
```

```python
def liste(request):
    articles = Article.objects.publies()
    return render(request, "blog/liste.html#liste-articles", {"articles": articles})       # ne rend QUE le fragment
```

```django
{% partial liste-articles %}                                     {# réutiliser le fragment ailleurs #}
```

## 7.5 Balises et filtres personnalisés

```python
# blog/templatetags/blog_extras.py
from django import template
register = template.Library()

@register.filter
def temps_de_lecture(texte: str) -> int:
    return max(1, len(texte.split()) // 200)

@register.simple_tag(takes_context=True)
def url_page(context, page: int) -> str:
    requete = context["request"].GET.copy(); requete["page"] = page
    return f"?{requete.urlencode()}"

@register.inclusion_tag("blog/_derniers.html")
def derniers_articles(n: int = 5):
    return {"articles": Article.objects.publies()[:n]}
```

```django
{% load blog_extras %}
{{ article.contenu|temps_de_lecture }} min · {% derniers_articles 3 %}
```

> Ajoutez un fichier `__init__.py` dans `templatetags/` et **redémarrez** le serveur après création.

## 7.6 Processeurs de contexte

Injectent des variables dans **tous** les templates :

```python
# apps/accueil/context_processors.py
def site(request):
    return {"NOM_SITE": "Mon site", "ANNEE": timezone.now().year}

# settings.py → TEMPLATES[...]["OPTIONS"]["context_processors"] += ["apps.accueil.context_processors.site"]
```

> ⚠️ Utilisez-les avec **parcimonie** : ils s'exécutent à **chaque** rendu.

## 7.7 Fichiers statiques, formulaires, internationalisation

```django
{% load static i18n %}
<img src="{% static 'img/logo.png' %}" alt="">
<form method="post">{% csrf_token %}{{ form }}<button>Envoyer</button></form>
{% translate "Bienvenue" %} · {% blocktranslate with nom=user.first_name %}Bonjour {{ nom }}{% endblocktranslate %}
```

## 7.8 Jinja2 et autres moteurs

Django peut utiliser **Jinja2** (`django.template.backends.jinja2.Jinja2`) : plus rapide et plus expressif, mais **sans** la compatibilité avec les templates de l'admin et de nombreuses bibliothèques. **Gardez le DTL** sauf besoin précis. Alternatives de **composants** : `django-cotton`, `django-components`, `django-slippers`.

## 7.9 Déboguer les templates

- `TEMPLATES[0]["OPTIONS"]["debug"] = True` (déduit de `DEBUG`) : page d'erreur détaillée avec la ligne fautive.
- `{{ variable }}` absente → **chaîne vide silencieuse** : utilisez `string_if_invalid` en développement ou `django-debug-toolbar` (onglet *Templates* / *Context*).
- `{% debug %}` affiche le contexte ; filtre `|pprint`.

---

# 🟡 Données et interface

---

# 8. Modèles

## 8.1 Définir un modèle

Un **modèle** est une classe Python qui décrit une **table** : chaque attribut `Field` devient une **colonne**.

```python
# apps/blog/models.py
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

class Categorie(models.Model):
    nom = models.CharField("nom", max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "catégorie"
        verbose_name_plural = "catégories"
        ordering = ["nom"]

    def __str__(self) -> str:
        return self.nom

class ArticleQuerySet(models.QuerySet):
    def publies(self):
        return self.filter(statut=Article.Statut.PUBLIE, publie_le__lte=timezone.now())

class Article(models.Model):
    class Statut(models.TextChoices):                                # énumération de choix
        BROUILLON = "brouillon", "Brouillon"
        PUBLIE = "publie", "Publié"

    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date="publie_le")
    contenu = models.TextField()
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    categories = models.ManyToManyField(Categorie, blank=True, related_name="articles")
    statut = models.CharField(max_length=10, choices=Statut, default=Statut.BROUILLON)
    note = models.PositiveSmallIntegerField(db_default=0)             # valeur par défaut côté BASE (5.0)
    cree_le = models.DateTimeField(auto_now_add=True)
    modifie_le = models.DateTimeField(auto_now=True)
    publie_le = models.DateTimeField(default=timezone.now)

    objects = ArticleQuerySet.as_manager()

    class Meta:
        ordering = ["-publie_le"]
        indexes = [models.Index(fields=["statut", "-publie_le"])]
        constraints = [
            models.CheckConstraint(condition=models.Q(note__gte=0, note__lte=5), name="article_note_0_5"),
        ]

    def __str__(self) -> str:
        return self.titre

    def get_absolute_url(self) -> str:
        return reverse("blog:detail", kwargs={"pk": self.pk})
```

> 📌 Depuis Django 5.1, `CheckConstraint` utilise le paramètre **`condition=`** (l'ancien `check=` est déprécié).

## 8.2 Types de champs

| Catégorie | Champs |
| --- | --- |
| **Texte** | `CharField(max_length)`, `TextField`, `SlugField`, `EmailField`, `URLField`, `UUIDField` |
| **Nombres** | `IntegerField`, `BigIntegerField`, `SmallIntegerField`, `PositiveIntegerField`, `FloatField`, `DecimalField(max_digits, decimal_places)` (✅ pour l'argent) |
| **Booléen** | `BooleanField` |
| **Dates** | `DateField`, `DateTimeField`, `TimeField`, `DurationField` (`auto_now`, `auto_now_add`) |
| **Fichiers** | `FileField`, `ImageField` (nécessite **Pillow**) |
| **Structurés** | **`JSONField`** (JSON natif, requêtes sur les clés), `GenericIPAddressField`, `BinaryField` |
| **Relations** | `ForeignKey`, `OneToOneField`, `ManyToManyField` |
| **Calculé** | **`GeneratedField`** *(5.0)* : valeur calculée par la **base** |
| **PostgreSQL** | `ArrayField`, `HStoreField`, `DateRangeField`, `SearchVectorField` (`django.contrib.postgres`) |

### Options communes

| Option | Rôle |
| --- | --- |
| `null=True` | Stocke `NULL` en base (⚠️ évitez pour `CharField`/`TextField` : préférez `""`) |
| `blank=True` | Champ **facultatif dans les formulaires** (validation) |
| `default`, `db_default` | Valeur par défaut (Python / **base**, 5.0) |
| `unique`, `db_index` | Unicité, index |
| `choices` | Liste, énumération `TextChoices` / `IntegerChoices`, ou **dictionnaire** (5.0) |
| `validators`, `help_text`, `verbose_name`, `editable`, `db_column` | |

```python
from django.db.models.functions import Lower

class Produit(models.Model):
    prix_ht = models.DecimalField(max_digits=10, decimal_places=2)
    tva = models.DecimalField(max_digits=4, decimal_places=3, default=0.2)
    prix_ttc = models.GeneratedField(                                  # colonne calculée par la base (5.0)
        expression=models.F("prix_ht") * (1 + models.F("tva")),
        output_field=models.DecimalField(max_digits=12, decimal_places=2),
        db_persist=True,
    )
    metadonnees = models.JSONField(default=dict, blank=True)
```

## 8.3 Clés primaires

Par défaut, Django ajoute `id` (**`BigAutoField`**). Autres choix :

```python
import uuid
class Commande(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)      # ou UUID7 côté base (6.1)

class LigneCommande(models.Model):                                                   # clé composite (5.2)
    pk = models.CompositePrimaryKey("commande_id", "produit_id")
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
```

## 8.4 Relations

```python
class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="commentaires")   # plusieurs → un
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

class Profil(models.Model):
    utilisateur = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)         # un → un

class Etiquette(models.Model):
    articles = models.ManyToManyField(Article, through="Classement")                                # plusieurs → plusieurs
```

| `on_delete` | Comportement à la suppression de l'objet référencé |
| --- | --- |
| `CASCADE` | Supprime aussi les objets liés |
| `PROTECT` | Interdit la suppression (`ProtectedError`) |
| `RESTRICT` | Interdit sauf suppression en cascade par un autre chemin |
| `SET_NULL` / `SET_DEFAULT` / `SET(valeur)` | Remplace la référence |
| `DO_NOTHING` | Rien (la base peut refuser) |
| **`DB_CASCADE`**, **`DB_SET_NULL`**, **`DB_SET_DEFAULT`** *(6.1)* | **Délégué à la base de données** (contraintes `ON DELETE`) : plus rapide, sans charger les objets |

```python
article.commentaires.all()          # relation inverse (related_name)
article.categories.add(cat)         # ManyToMany
Article.objects.filter(categories__slug="python")
```

## 8.5 Migrations

Les **migrations** versionnent le **schéma** de la base.

```bash
python manage.py makemigrations                 # détecte les changements de modèles → fichiers dans migrations/
python manage.py makemigrations blog -n ajout_note
python manage.py migrate                        # applique
python manage.py showmigrations
python manage.py sqlmigrate blog 0002           # voir le SQL
python manage.py migrate blog 0001              # revenir en arrière
python manage.py makemigrations --check --dry-run          # (CI) échoue s'il manque une migration
python manage.py squashmigrations blog 0001 0020           # condenser l'historique
```

```python
# Migration de données
from django.db import migrations

def remplir_slugs(apps, schema_editor):
    Article = apps.get_model("blog", "Article")           # ⚠️ modèle HISTORIQUE, jamais l'import direct
    for a in Article.objects.filter(slug=""):
        a.slug = slugify(a.titre); a.save(update_fields=["slug"])

class Migration(migrations.Migration):
    dependencies = [("blog", "0003_article_slug")]
    operations = [migrations.RunPython(remplir_slugs, migrations.RunPython.noop)]
```

> ✅ **Versionnez les migrations** dans Git ; **ne modifiez jamais** une migration déjà appliquée en production. Ajoutez une colonne `NOT NULL` en **plusieurs étapes** (nullable → remplissage → contrainte) pour éviter de verrouiller de grosses tables.

## 8.6 Validation et nettoyage

```python
from django.core.exceptions import ValidationError

class Article(models.Model):
    def clean(self):                                               # validation globale (appelée par full_clean et les ModelForm)
        if self.statut == self.Statut.PUBLIE and len(self.contenu) < 100:
            raise ValidationError({"contenu": "Un article publié doit contenir au moins 100 caractères."})
```

> ⚠️ `save()` n'appelle **pas** `full_clean()` automatiquement. Les **contraintes de base** (`CheckConstraint`, `UniqueConstraint`) sont plus fiables que la validation Python seule.

## 8.7 Méthodes, propriétés et gestionnaires

```python
class Article(models.Model):
    @property
    def temps_de_lecture(self) -> int: return max(1, len(self.contenu.split()) // 200)

    def publier(self) -> None:                                      # logique métier dans le modèle
        self.statut = self.Statut.PUBLIE
        self.publie_le = timezone.now()
        self.save(update_fields=["statut", "publie_le"])
```

```python
class ArticleManager(models.Manager):
    def get_queryset(self): return super().get_queryset().select_related("auteur")
```

## 8.8 Héritage de modèles

| Type | Table(s) | Usage |
| --- | --- | --- |
| **Classe abstraite** (`Meta: abstract = True`) | Aucune pour la base ; champs copiés dans les enfants | **Champs communs** (horodatage) ✅ |
| **Multi-table** | Une table par modèle, liée par `OneToOne` | Hiérarchie avec requêtes sur le parent (⚠️ jointures) |
| **Proxy** (`proxy = True`) | Aucune nouvelle | Changer le comportement (gestionnaire, méthodes) |

```python
class Horodate(models.Model):
    cree_le = models.DateTimeField(auto_now_add=True)
    modifie_le = models.DateTimeField(auto_now=True)
    class Meta: abstract = True

class Article(Horodate): ...
```

## 8.9 Performances (aperçu)

`select_related` / `prefetch_related` (N+1), `only()` / `defer()`, index, `bulk_create` : voir [section 9](#9-orm--requêtes-et-optimisation).

## 8.10 SQL brut

```python
Article.objects.raw("SELECT * FROM blog_article WHERE note > %s", [3])           # paramètres : toujours liés (%s), jamais f-string
from django.db import connection
with connection.cursor() as c:
    c.execute("SELECT COUNT(*) FROM blog_article WHERE statut = %s", ["publie"]); c.fetchone()
```

> 🔒 **Ne construisez jamais du SQL avec des f-strings ou `%`** sur des données utilisateur (injection SQL).

---

# 9. ORM : requêtes et optimisation

## 9.1 Opérations de base

```python
# Créer
article = Article.objects.create(titre="Bonjour", contenu="…", auteur=user)
a = Article(titre="X"); a.save()
Article.objects.bulk_create([Article(titre=f"T{i}", auteur=user) for i in range(100)], batch_size=500)

# Lire
Article.objects.all()
Article.objects.get(pk=1)                               # DoesNotExist / MultipleObjectsReturned
Article.objects.filter(statut="publie").exclude(auteur=user)
Article.objects.first(); Article.objects.last(); Article.objects.exists(); Article.objects.count()
Article.objects.get_or_create(slug="x", defaults={"titre": "X"})      # (objet, créé)
Article.objects.update_or_create(slug="x", defaults={"titre": "Y"})

# Modifier
article.titre = "Nouveau"; article.save(update_fields=["titre"])
Article.objects.filter(statut="brouillon").update(statut="archive")  # UPDATE en une requête
Article.objects.bulk_update(objets, ["note"])

# Supprimer
article.delete()
Article.objects.filter(cree_le__lt=limite).delete()
```

> 💡 Un **QuerySet est paresseux** : le SQL n'est exécuté qu'à l'**évaluation** (itération, `list()`, `len()`, slicing avec pas, `bool()`) ; il est **mis en cache** après évaluation.

## 9.2 Filtres et lookups

| Lookup | SQL | Exemple |
| --- | --- | --- |
| `exact`, `iexact` | `=` | `titre__iexact="django"` |
| `contains`, `icontains` | `LIKE '%…%'` | `titre__icontains="py"` |
| `startswith`, `endswith` | | |
| `in` | `IN (…)` | `pk__in=[1, 2, 3]` |
| `gt`, `gte`, `lt`, `lte` | `>`, `>=`… | `note__gte=4` |
| `range` | `BETWEEN` | `cree_le__range=(debut, fin)` |
| `isnull` | `IS NULL` | `auteur__isnull=True` |
| `year`, `month`, `day`, `date`, `week_day` | dates | `publie_le__year=2026` |
| `regex`, `iregex` | | |
| Relations | `__` | `auteur__username="alice"`, `categories__slug="python"` |
| JSON | `__clé` | `metadonnees__couleur="rouge"` |

```python
from django.db.models import Q, F, Count, Avg, Sum, Max, Min

Article.objects.filter(Q(titre__icontains="django") | Q(contenu__icontains="django"))      # OR
Article.objects.filter(~Q(statut="brouillon"), note__gte=3)                                  # NOT + AND
Article.objects.filter(modifie_le__gt=F("cree_le"))                                          # comparer deux champs
Article.objects.update(note=F("note") + 1)                                                   # incrément atomique (évite les conflits)
```

## 9.3 Tri, découpage, valeurs

```python
Article.objects.order_by("-publie_le", "titre")
Article.objects.order_by("?")                          # aléatoire (coûteux)
Article.objects.all()[:10]                             # LIMIT 10 (pagination : [20:30])
Article.objects.values("id", "titre")                  # dictionnaires
Article.objects.values_list("titre", flat=True)        # liste de valeurs
Article.objects.distinct(); Article.objects.in_bulk([1, 2]); Article.objects.reverse(); Article.objects.none()
```

## 9.4 Agrégation et annotation

```python
Article.objects.aggregate(total=Count("id"), moyenne=Avg("note"), maxi=Max("publie_le"))      # un seul résultat (dict)

auteurs = (Utilisateur.objects
           .annotate(nb_articles=Count("articles", distinct=True), note_moyenne=Avg("articles__note"))
           .filter(nb_articles__gte=1)
           .order_by("-nb_articles"))
for a in auteurs: print(a.username, a.nb_articles)    # chaque objet porte l'annotation
```

### Expressions et fonctions

```python
from django.db.models import Case, When, Value, CharField, Subquery, OuterRef, Exists, Window
from django.db.models.functions import Lower, Concat, Coalesce, Now, TruncMonth, RowNumber, UUID7   # (UUID4/UUID7 : 6.1)

Article.objects.annotate(niveau=Case(
    When(note__gte=4, then=Value("excellent")), When(note__gte=2, then=Value("bon")),
    default=Value("faible"), output_field=CharField()))

dernier = Commentaire.objects.filter(article=OuterRef("pk")).order_by("-cree_le")
Article.objects.annotate(dernier_commentaire=Subquery(dernier.values("texte")[:1]))
Article.objects.filter(Exists(Commentaire.objects.filter(article=OuterRef("pk"))))          # articles commentés

Article.objects.annotate(rang=Window(expression=RowNumber(), partition_by=F("auteur"), order_by=F("note").desc()))   # fonction de fenêtrage
Article.objects.annotate(mois=TruncMonth("publie_le")).values("mois").annotate(n=Count("id"))
```

## 9.5 Relations et jointures : éviter le problème N+1

```python
# ❌ N+1 : 1 requête + 1 par article
for a in Article.objects.all():
    print(a.auteur.username)

# ✅ select_related : JOIN pour les relations « vers un » (ForeignKey, OneToOne)
Article.objects.select_related("auteur", "auteur__profil")

# ✅ prefetch_related : 2e requête groupée pour « vers plusieurs » (ManyToMany, relations inverses)
Article.objects.prefetch_related("categories", "commentaires")

# Préchargement filtré
from django.db.models import Prefetch
Article.objects.prefetch_related(Prefetch("commentaires", queryset=Commentaire.objects.filter(valide=True), to_attr="commentaires_valides"))
```

### Modes de chargement des champs *(6.1, ajout)*

Django 6.1 permet de **choisir le comportement** du chargement à la demande pour contrer le N+1 **sans** modifier chaque requête :

```python
from django.db import models

articles = Article.objects.fetch_mode(models.FETCH_PEERS)        # charge la relation pour TOUS les objets « pairs » en une seule requête
for a in articles:
    print(a.auteur.nom)                                          # 2 requêtes au total, malgré la boucle

# FETCH_ONE (comportement classique) · FETCH_RAISE : lève une erreur si un chargement à la demande a lieu (détecter les N+1 dans les tests)
```

## 9.6 Optimiser les requêtes

| Technique | Effet |
| --- | --- |
| `select_related` / `prefetch_related` | Supprime le N+1 |
| **`only()` / `defer()`** | Ne charge que certaines colonnes |
| **`values()` / `values_list()`** | Évite l'instanciation d'objets |
| **`exists()`** au lieu de `len()` / `bool()` | `SELECT 1 … LIMIT 1` |
| **`count()`** au lieu de `len(qs)` | `SELECT COUNT(*)` |
| **`iterator(chunk_size=…)`** | Gros volumes, mémoire constante |
| **`bulk_create` / `bulk_update`** | Insertions / mises à jour en lot |
| **Index** (`db_index`, `Meta.indexes`) | Accélère filtres et tris |
| **`F()`** | Opérations dans la base |
| `.explain()` | Plan d'exécution SQL |
| `django-debug-toolbar`, `connection.queries`, `django-silk` | Mesurer |

```python
print(Article.objects.filter(statut="publie").explain(analyze=True))
from django.test.utils import CaptureQueriesContext
with CaptureQueriesContext(connection) as ctx: ...; print(len(ctx))
```

## 9.7 Transactions

```python
from django.db import transaction

@transaction.atomic                                           # tout ou rien
def passer_commande(panier): ...

with transaction.atomic():
    commande = Commande.objects.create(...)
    for ligne in lignes:
        Stock.objects.select_for_update().filter(pk=ligne.produit_id).update(quantite=F("quantite") - ligne.quantite)

transaction.on_commit(lambda: envoyer_confirmation.delay(commande.pk))      # ✅ exécuter APRÈS la validation de la transaction
```

> ⚙️ `ATOMIC_REQUESTS = True` (dans `DATABASES`) enveloppe chaque requête HTTP dans une transaction.

## 9.8 ORM asynchrone *(ajout)*

Préfixe `a` pour les opérations **terminales**, `async for` pour l'itération :

```python
article = await Article.objects.aget(pk=1)
nb = await Article.objects.filter(statut="publie").acount()
await Article.objects.acreate(titre="X", auteur=user)
async for a in Article.objects.filter(statut="publie"): ...
existe = await Article.objects.filter(slug="x").aexists()
```

> Les opérations qui ne sont pas encore natives asynchrones peuvent être appelées avec `sync_to_async` (voir section 22).

## 9.9 Plusieurs bases de données

```python
DATABASES = {"default": {...}, "lecture": {...}}
DATABASE_ROUTERS = ["config.routers.LectureEcriture"]

class LectureEcriture:
    def db_for_read(self, model, **hints): return "lecture"
    def db_for_write(self, model, **hints): return "default"
    def allow_relation(self, o1, o2, **hints): return True
    def allow_migrate(self, db, app_label, model_name=None, **hints): return db == "default"

Article.objects.using("lecture").all()
```

## 9.10 Gestionnaires et QuerySets personnalisés

```python
class ArticleQuerySet(models.QuerySet):
    def publies(self): return self.filter(statut="publie")
    def de(self, user): return self.filter(auteur=user)

class Article(models.Model):
    objects = ArticleQuerySet.as_manager()

Article.objects.publies().de(user)                      # chaînable ✅
```

## 9.11 Recherche plein texte (PostgreSQL)

```python
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
vecteur = SearchVector("titre", weight="A") + SearchVector("contenu", weight="B")
Article.objects.annotate(rang=SearchRank(vecteur, SearchQuery("django orm", config="french"))).filter(rang__gt=0.1).order_by("-rang")
```

Pour les gros besoins : **`django-haystack`**, **`django-elasticsearch-dsl`**, **Meilisearch**, **Typesense**.

---

# 10. Interface d'administration

## 10.1 Activer et utiliser l'admin

L'**admin** est un back-office **généré automatiquement** à partir des modèles : idéal pour la gestion de contenu et les outils internes.

```python
# config/urls.py
path("admin/", admin.site.urls)        # ⚠️ en production, changez l'URL (« gestion-x7k2/ ») et protégez l'accès
```

```bash
python manage.py createsuperuser
```

## 10.2 Enregistrer et personnaliser un modèle

```python
# apps/blog/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Article, Categorie, Commentaire

class CommentaireInline(admin.TabularInline):                       # modifier les commentaires dans la page de l'article
    model = Commentaire
    extra = 0
    readonly_fields = ["cree_le"]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["titre", "auteur", "statut", "publie_le", "nb_commentaires"]
    list_filter = ["statut", "categories", "publie_le"]
    list_editable = ["statut"]
    list_select_related = ["auteur"]                                # évite le N+1 dans la liste
    search_fields = ["titre", "contenu", "auteur__username"]
    date_hierarchy = "publie_le"
    prepopulated_fields = {"slug": ("titre",)}
    autocomplete_fields = ["auteur"]                                # champ de recherche (nécessite search_fields sur UtilisateurAdmin)
    filter_horizontal = ["categories"]
    readonly_fields = ["cree_le", "modifie_le"]
    inlines = [CommentaireInline]
    actions = ["publier"]
    show_facets = admin.ShowFacets.ALLOW                            # (5.0) compteurs dans les filtres
    ordering = ["-publie_le"]
    list_per_page = 25

    fieldsets = [
        (None, {"fields": ["titre", "slug", "auteur"]}),
        ("Contenu", {"fields": ["contenu", "categories"]}),
        ("Publication", {"fields": ["statut", "publie_le"], "classes": ["collapse"]}),
    ]

    @admin.display(description="Commentaires", ordering="nb_commentaires")
    def nb_commentaires(self, obj) -> int:
        return obj.nb_commentaires

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(nb_commentaires=Count("commentaires"))

    @admin.action(description="Publier les articles sélectionnés")
    def publier(self, request, queryset):
        n = queryset.update(statut=Article.Statut.PUBLIE)
        self.message_user(request, f"{n} article(s) publié(s).")

    def has_delete_permission(self, request, obj=None):             # contrôle d'accès fin
        return request.user.is_superuser
```

| Option de `ModelAdmin` | Rôle |
| --- | --- |
| `list_display`, `list_display_links`, `list_editable`, `list_filter`, `search_fields`, `date_hierarchy`, `ordering`, `list_per_page` | Liste |
| `fields`, `fieldsets`, `readonly_fields`, `prepopulated_fields`, `filter_horizontal`, `autocomplete_fields`, `raw_id_fields`, `formfield_overrides` | Formulaire |
| `inlines` (`TabularInline`, `StackedInline`) | Objets liés |
| `actions` | Actions groupées |
| `save_model`, `get_queryset`, `get_form`, `has_*_permission` | Personnalisation avancée |
| `show_facets` | Facettes (5.0) |

## 10.3 Permissions et groupes

Chaque modèle reçoit **4 permissions** (`add`, `change`, `delete`, `view`). Créez des **groupes** (ex. « Rédacteurs ») et attribuez-leur des permissions dans l'admin ; limitez le nombre de **superutilisateurs**.

## 10.4 Personnaliser l'apparence

```python
admin.site.site_header = "Administration — Mon site"
admin.site.site_title = "Mon site"
admin.site.index_title = "Tableau de bord"
```

- Surcharger les templates : `templates/admin/base_site.html` (`{% extends "admin/base.html" %}`).
- Thèmes et interfaces modernes : voir ci-dessous.

## 10.5 Paquets pour l'admin

| Paquet | Apport |
| --- | --- |
| **`django-unfold`** | Interface **moderne** (Tailwind), tableaux de bord, widgets |
| **`django-jazzmin`**, **`django-grappelli`**, **`django-admin-interface`** | Thèmes |
| **`django-import-export`** | Import / export CSV, Excel, JSON |
| **`django-simple-history`** | **Historique** des modifications (qui, quand, quoi) |
| **`django-reversion`** | Versions et **restauration** |
| **`django-admin-sortable2`**, **`django-adminactions`** | Tri par glisser-déposer, actions avancées |
| **`django-ckeditor-5`**, **`django-tinymce`** | Éditeur riche (⚠️ `django-ckeditor` v4 est **abandonné**) |
| **`django-otp`** / `django-two-factor-auth` | **Double authentification** pour l'admin |
| **`django-axes`** | Blocage des tentatives de connexion répétées |

## 10.6 Sécurité de l'admin

- URL **non standard**, **HTTPS** obligatoire, **2FA**, accès restreint par IP / VPN si possible.
- Comptes **nominatifs**, permissions minimales, journal (`LogEntry`) consulté.
- N'exposez pas l'admin à des utilisateurs non fiables : il est conçu pour le **personnel**.

---

# 11. Formulaires

## 11.1 Formulaires simples

```python
# apps/blog/forms.py
from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, label="Votre nom")
    email = forms.EmailField()
    sujet = forms.ChoiceField(choices=[("q", "Question"), ("b", "Bogue")])
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}), min_length=10)
    copie = forms.BooleanField(required=False, label="Recevoir une copie")

    def clean_email(self):                                         # validation d'UN champ : clean_<champ>
        email = self.cleaned_data["email"]
        if email.endswith("@spam.test"):
            raise ValidationError("Domaine non autorisé.")
        return email

    def clean(self):                                               # validation GLOBALE
        donnees = super().clean()
        if donnees.get("sujet") == "b" and len(donnees.get("message", "")) < 50:
            self.add_error("message", "Décrivez le bogue en détail (50 caractères minimum).")
        return donnees
```

## 11.2 Traiter un formulaire dans une vue

```python
from django.contrib import messages
from django.core.mail import send_mail

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        send_mail(form.cleaned_data["sujet"], form.cleaned_data["message"], None, ["contact@exemple.fr"])
        messages.success(request, "Message envoyé, merci !")
        return redirect("accueil")                                  # Post/Redirect/Get : évite le double envoi
    return render(request, "contact.html", {"form": form})
```

## 11.3 ModelForm

Génère un formulaire **à partir d'un modèle** :

```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["titre", "slug", "contenu", "categories", "statut"]     # ✅ liste EXPLICITE (jamais « __all__ » sans réflexion)
        widgets = {"contenu": forms.Textarea(attrs={"rows": 12})}
        labels = {"titre": "Titre de l'article"}
        help_texts = {"slug": "Utilisé dans l'URL."}

    def clean_titre(self):
        titre = self.cleaned_data["titre"]
        if Article.objects.filter(titre__iexact=titre).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Ce titre existe déjà.")
        return titre

form = ArticleForm(request.POST, request.FILES, instance=article)       # instance → modification
article = form.save(commit=False); article.auteur = request.user; article.save(); form.save_m2m()
```

> 🔒 N'utilisez **jamais** `fields = "__all__"` ni `exclude` sur un formulaire public : un utilisateur pourrait modifier des champs sensibles (`is_staff`, `auteur`…).

## 11.4 Rendu dans les templates *(à jour)*

```django
<form method="post" enctype="multipart/form-data" novalidate>
    {% csrf_token %}
    {{ form }}                                {# rendu par défaut : un <div> par champ (depuis Django 5.0) #}

    {# Ou champ par champ : #}
    {{ form.non_field_errors }}
    {% for champ in form %}
        <div class="champ">
            {{ champ.as_field_group }}        {# (5.0) label + aide + erreurs + widget #}
        </div>
    {% endfor %}
    <button type="submit">Enregistrer</button>
</form>
```

Personnalisation : **`FORM_RENDERER`**, templates `django/forms/div.html`, attributs de widgets (`attrs={"class": "input"}`).

### Bibliothèques de rendu

| Paquet | Apport |
| --- | --- |
| **`django-crispy-forms`** + `crispy-bootstrap5` / `crispy-tailwind` | Rendu thématisé : `{{ form\|crispy }}` |
| **`django-widget-tweaks`** | Ajouter classes et attributs **dans le template** : `{% render_field form.titre class="input" %}` |
| **`django-formtools`** | Assistants multi-étapes (*wizard*) |

## 11.5 Widgets et champs utiles

`TextInput`, `Textarea`, `Select`, `SelectMultiple`, `CheckboxSelectMultiple`, `RadioSelect`, `DateInput` (`type="date"`), `FileInput`, `ClearableFileInput`, `HiddenInput`, `PasswordInput`. Champs : `ModelChoiceField`, `ModelMultipleChoiceField`, `DateField`, `DecimalField`, `FileField`, `ImageField`, `JSONField`, `SlugField`, `RegexField`.

## 11.6 Jeux de formulaires (*formsets*)

```python
from django.forms import inlineformset_factory, formset_factory
CommentaireFormSet = inlineformset_factory(Article, Commentaire, fields=["texte"], extra=2, can_delete=True)
formset = CommentaireFormSet(request.POST or None, instance=article)
```

## 11.7 Téléversement de fichiers

```python
class DocumentForm(forms.ModelForm):
    class Meta: model = Document; fields = ["fichier"]

    def clean_fichier(self):
        f = self.cleaned_data["fichier"]
        if f.size > 5 * 1024 * 1024: raise ValidationError("5 Mo maximum.")
        if f.content_type not in {"application/pdf", "image/png", "image/jpeg"}: raise ValidationError("Type non autorisé.")
        return f
```

> 🔒 Ne vous fiez pas à l'extension ni au `content_type` envoyé par le client : voir la [section 26](#26-sécurité). `enctype="multipart/form-data"` est **obligatoire** dans le `<form>`.

## 11.8 CSRF

`{% csrf_token %}` est **obligatoire** dans tout formulaire `POST` (le middleware `CsrfViewMiddleware` vérifie le jeton). Pour **AJAX / HTMX** : envoyez le jeton dans l'en-tête `X-CSRFToken`.

```html
<body hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'>        <!-- HTMX -->
```

## 11.9 Formulaires et accessibilité

Chaque champ doit avoir un `<label>` ; les erreurs sont associées (`aria-describedby`) ; testez au clavier. Django fournit déjà des étiquettes et des messages d'aide structurés.

---

# 12. Authentification et autorisation

## 12.1 Le système intégré

`django.contrib.auth` fournit : **utilisateurs**, **groupes**, **permissions**, **sessions**, vues de **connexion / déconnexion / mots de passe**, **hachage** sécurisé (PBKDF2 par défaut, **Argon2** recommandé).

## 12.2 Modèle utilisateur personnalisé ✅

```python
# apps/comptes/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    email = models.EmailField("adresse e-mail", unique=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True)

    USERNAME_FIELD = "email"                                       # connexion par e-mail
    REQUIRED_FIELDS = ["username"]

# settings.py
AUTH_USER_MODEL = "comptes.Utilisateur"

# Toujours référencer l'utilisateur ainsi
from django.contrib.auth import get_user_model
User = get_user_model()                                            # dans le code
author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    # dans les modèles
```

> 💡 `AbstractBaseUser` + `PermissionsMixin` pour un contrôle total ; `AbstractUser` suffit dans 95 % des cas. Un **profil** séparé (`OneToOneField`) est une alternative pour des données volumineuses.

## 12.3 Vues d'authentification intégrées

```python
# config/urls.py
urlpatterns += [path("comptes/", include("django.contrib.auth.urls"))]
# fournit : login/, logout/, password_change/, password_reset/, reset/<uidb64>/<token>/ …
```

```python
# settings.py
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "accueil"
LOGOUT_REDIRECT_URL = "accueil"
```

```django
{# templates/registration/login.html #}
<form method="post">{% csrf_token %}{{ form }}<button>Connexion</button></form>
```

> ⚠️ Depuis Django 5.0, la déconnexion exige une requête **POST** (formulaire avec `{% csrf_token %}`), pas un simple lien.

### Inscription

```python
from django.contrib.auth.forms import UserCreationForm
class InscriptionForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Utilisateur; fields = ("username", "email")

class Inscription(CreateView):
    form_class = InscriptionForm
    template_name = "registration/inscription.html"
    success_url = reverse_lazy("login")
```

## 12.4 Contrôle d'accès

```python
# Fonctions
@login_required
@permission_required("blog.add_article", raise_exception=True)
def vue(request): ...

# Classes
class Vue(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "blog.change_article"

# Dans le code et les templates
request.user.is_authenticated; request.user.has_perm("blog.add_article"); request.user.groups.filter(name="Rédacteurs").exists()
```

```django
{% if perms.blog.add_article %}<a href="{% url 'blog:creer' %}">Nouvel article</a>{% endif %}
{% if user.is_authenticated %}Bonjour {{ user.username }}{% endif %}
```

### Authentification obligatoire par défaut *(5.1, ajout)*

```python
MIDDLEWARE += ["django.contrib.auth.middleware.LoginRequiredMiddleware"]       # toutes les vues exigent la connexion

from django.contrib.auth.decorators import login_not_required
@login_not_required
def page_publique(request): ...
```

### Permissions d'objet

Les permissions natives sont **par modèle**. Pour des permissions **par objet** (« seul l'auteur peut modifier ») : `UserPassesTestMixin`, ou **`django-guardian`** / **`django-rules`**.

## 12.5 Mots de passe

```python
PASSWORD_HASHERS = ["django.contrib.auth.hashers.Argon2PasswordHasher", "django.contrib.auth.hashers.PBKDF2PasswordHasher"]     # pip install argon2-cffi
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", "OPTIONS": {"min_length": 12}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
```

## 12.6 Backends d'authentification personnalisés

```python
class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try: user = User.objects.get(email__iexact=username)
        except User.DoesNotExist: return None
        return user if user.check_password(password) and self.user_can_authenticate(user) else None

AUTHENTICATION_BACKENDS = ["apps.comptes.backends.EmailBackend", "django.contrib.auth.backends.ModelBackend"]
```

## 12.7 Connexion sociale, SSO et 2FA *(ajout)*

| Besoin | Paquet |
| --- | --- |
| **Inscription, e-mail vérifié, Google / GitHub / Microsoft / etc.**, 2FA, passkeys | **`django-allauth`** ✅ (le plus complet) ; mode **headless** pour les SPA / API |
| OAuth 2 / OpenID Connect **fournisseur** | **`django-oauth-toolkit`** |
| Connexion sociale (alternative) | **`social-auth-app-django`** |
| **2FA** (TOTP, codes de secours) | **`django-otp`**, **`django-two-factor-auth`** |
| **SSO d'entreprise** (SAML, OIDC, LDAP) | `mozilla-django-oidc`, `djangosaml2`, `django-auth-ldap` |
| Protection force brute | **`django-axes`** |

```python
# django-allauth (extrait)
INSTALLED_APPS += ["django.contrib.sites", "allauth", "allauth.account", "allauth.socialaccount", "allauth.socialaccount.providers.google"]
MIDDLEWARE += ["allauth.account.middleware.AccountMiddleware"]
AUTHENTICATION_BACKENDS += ["allauth.account.auth_backends.AuthenticationBackend"]
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
```

## 12.8 Sessions

```python
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"       # db | cache | cached_db | file | signed_cookies
SESSION_COOKIE_AGE = 60 * 60 * 24 * 14
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
```

```python
request.session["panier"] = {"1": 2}              # lecture / écriture (sérialisable en JSON)
request.session.flush()                           # vider + régénérer la clé
```

## 12.9 Bonnes pratiques

- **Modèle personnalisé dès le début**, **Argon2**, validateurs de mots de passe, **2FA** pour le personnel.
- **Limitation des tentatives** (`django-axes`), messages d'erreur **identiques** (anti-énumération).
- **Ne stockez pas** de mots de passe en clair, ne les journalisez jamais.
- Testez les accès (`self.client.force_login(user)`), y compris les **cas refusés**.

---

# 13. Messages, sessions et cache

## 13.1 Framework de messages

```python
from django.contrib import messages
messages.success(request, "Article enregistré.")
messages.error(request, "Une erreur est survenue.")
messages.add_message(request, messages.WARNING, "Attention.", extra_tags="important")
# niveaux : DEBUG, INFO, SUCCESS, WARNING, ERROR
```

```django
{% if messages %}
<ul class="messages">
{% for message in messages %}<li class="{{ message.tags }}" role="alert">{{ message }}</li>{% endfor %}
</ul>
{% endif %}
```

```python
MESSAGE_STORAGE = "django.contrib.messages.storage.fallback.FallbackStorage"       # cookie puis session
MESSAGE_TAGS = {messages.ERROR: "danger"}                                              # compatibilité Bootstrap
```

Dans une vue de classe : `SuccessMessageMixin` (`success_message = "Créé !"`). Avec **HTMX / AJAX** : renvoyez les messages dans un fragment ou un en-tête `HX-Trigger`.

## 13.2 Cache : vue d'ensemble

| Niveau | Outil |
| --- | --- |
| **Site entier** | Middlewares `UpdateCacheMiddleware` / `FetchFromCacheMiddleware` |
| **Vue** | `@cache_page(60 * 15)` |
| **Fragment de template** | `{% cache 500 sidebar request.user.id %}…{% endcache %}` |
| **Bas niveau** | `cache.get/set/get_or_set/delete/incr` |
| **En-têtes HTTP** | `@cache_control`, `@etag`, `@last_modified`, `@condition` |

```python
from django.core.cache import cache

cache.set("stats", valeur, timeout=300)
cache.get("stats", default=None)
stats = cache.get_or_set("stats", calculer_stats, 300)           # ✅ calcule une seule fois
cache.delete_many(["a", "b"]); cache.incr("visites")

from django.views.decorators.cache import cache_page
@cache_page(60 * 15, key_prefix="accueil")
def accueil(request): ...
```

```django
{% load cache %}
{% cache 600 liste_articles page_obj.number %}{% for a in articles %}…{% endfor %}{% endcache %}
```

### Backends

| Backend | Usage |
| --- | --- |
| **`RedisCache`** (intégré) ✅ | Production (partagé entre processus) ; nécessite le paquet `redis` (`django-redis` pour des fonctions avancées) |
| `MemcachedCache` / `PyMemcacheCache` | Alternative |
| `DatabaseCache` | Si pas de Redis |
| `LocMemCache` | Développement / tests (**par processus**) |
| `FileBasedCache`, `DummyCache` | Spécifiques |

> ⚠️ Invalidation : donnez toujours une **durée de vie**, incluez dans la **clé** tout ce qui fait varier le contenu (utilisateur, langue), et n'entreposez pas de données sensibles partagées.

---

# 14. Fichiers statiques et médias

## 14.1 Deux notions distinctes

| | **Statiques** | **Médias** |
| --- | --- | --- |
| Contenu | CSS, JS, images du **site** | Fichiers **envoyés par les utilisateurs** |
| Source | Dépôt de code | Formulaires, admin |
| Réglages | `STATIC_URL`, `STATIC_ROOT`, `STATICFILES_DIRS` | `MEDIA_URL`, `MEDIA_ROOT` |
| Sécurité | Publics | **À valider** (taille, type, noms) |

## 14.2 Fichiers statiques

```python
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]                          # sources globales
STATIC_ROOT = BASE_DIR / "staticfiles"                            # cible de collectstatic (production)
```

```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/site.css' %}">
<img src="{% static 'img/logo.svg' %}" alt="Logo">
```

```bash
python manage.py collectstatic --noinput                          # copie tous les statiques vers STATIC_ROOT
```

En **développement**, `runserver` les sert (si `DEBUG = True`). En **production**, **jamais** par Django lui-même :

### Servir les statiques en production

| Solution | Quand |
| --- | --- |
| **WhiteNoise** ✅ | Simple : servi par l'application avec compression et empreintes |
| **Nginx / Caddy** | Serveur web frontal (performances maximales) |
| **CDN** (CloudFront, Cloudflare) + stockage S3 | Trafic important |

```python
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STORAGES = {"staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"}}    # fichiers hachés + compression
```

## 14.3 Fichiers médias

```python
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
```

```python
class Document(models.Model):
    fichier = models.FileField(upload_to="documents/%Y/%m/")
    image = models.ImageField(upload_to="images/", blank=True)       # nécessite Pillow

# Nom de fichier sûr et unique
def chemin_avatar(instance, nom):
    return f"avatars/{instance.pk}/{uuid.uuid4().hex}{Path(nom).suffix.lower()}"
```

```django
<img src="{{ document.image.url }}" alt="">
```

### Stockage dans le cloud : `django-storages`

```python
STORAGES = {
    "default": {"BACKEND": "storages.backends.s3.S3Storage", "OPTIONS": {"bucket_name": env("S3_BUCKET"), "region_name": "eu-west-3"}},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}
```

Compatible **Amazon S3**, **Cloudflare R2**, **Google Cloud Storage**, **Azure**, **MinIO**… Servez les médias privés par **URL signées** (`querystring_auth`).

## 14.4 Sécurité des fichiers téléversés

- Limiter **taille** (`DATA_UPLOAD_MAX_MEMORY_SIZE`, `FILE_UPLOAD_MAX_MEMORY_SIZE`) et **type** (validation du **contenu réel** avec `python-magic` / Pillow).
- **Renommer** les fichiers (pas de nom fourni par l'utilisateur), stocker **hors** de la racine web ou sur un stockage dédié.
- **Ne jamais exécuter** ni servir en `text/html` un fichier utilisateur ; `X-Content-Type-Options: nosniff`.
- Fichiers privés : vue protégée qui renvoie `FileResponse` (ou `X-Accel-Redirect`).

## 14.5 Dépanner

| Symptôme | Cause |
| --- | --- |
| Statiques absents en production | `collectstatic` oublié, `STATIC_ROOT` incorrect, serveur non configuré |
| `ValueError: Missing staticfiles manifest entry` | Fichier absent lors de `collectstatic` avec stockage « Manifest » |
| Médias en 404 en développement | `static(MEDIA_URL, …)` manquant dans `urls.py` |
| Images non traitées | **Pillow** non installé |

---

# 15. Middleware

## 15.1 Principe

Un **middleware** est une couche qui **intercepte** chaque requête **avant** la vue et chaque réponse **après** elle (comme des « oignons »).

```text
Requête  → SecurityMiddleware → Session → Auth → … → VUE
Réponse  ← SecurityMiddleware ← Session ← Auth ← … ←
```

## 15.2 Middlewares intégrés importants

| Middleware | Rôle |
| --- | --- |
| `SecurityMiddleware` | HTTPS, HSTS, `nosniff`, politique de référent |
| `SessionMiddleware` / `AuthenticationMiddleware` | Sessions, `request.user` |
| `LoginRequiredMiddleware` *(5.1)* | Authentification exigée par défaut |
| `CommonMiddleware` | `APPEND_SLASH`, `www`, longueur d'URL |
| `CsrfViewMiddleware` | Protection CSRF |
| `MessageMiddleware` | Messages |
| `LocaleMiddleware` | Langue selon la requête |
| `XFrameOptionsMiddleware` | Anti-clickjacking |
| **`ContentSecurityPolicyMiddleware`** *(6.0)* | **En-tête CSP** |
| `GZipMiddleware` | Compression |
| `ConditionalGetMiddleware` | ETag, 304 |

## 15.3 Écrire un middleware

```python
# apps/accueil/middleware.py
import time, logging
logger = logging.getLogger(__name__)

class ChronoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response                           # initialisation (une seule fois)

    def __call__(self, request):
        debut = time.perf_counter()
        reponse = self.get_response(request)                       # appelle la suite (autres middlewares + vue)
        duree = (time.perf_counter() - debut) * 1000
        reponse["X-Temps-Ms"] = f"{duree:.1f}"
        if duree > 500: logger.warning("Requête lente : %s %s (%.0f ms)", request.method, request.path, duree)
        return reponse

    def process_view(self, request, view_func, view_args, view_kwargs): ...        # avant la vue (facultatif)
    def process_exception(self, request, exception): ...                           # si la vue lève une exception
    def process_template_response(self, request, response): ...
```

### Middleware compatible sync / async

```python
from asgiref.sync import iscoroutinefunction, markcoroutinefunction

class MonMiddleware:
    sync_capable = True
    async_capable = True
    def __init__(self, get_response):
        self.get_response = get_response
        if iscoroutinefunction(get_response): markcoroutinefunction(self)
    def __call__(self, request):
        if iscoroutinefunction(self): return self.__acall__(request)
        return self.get_response(request)
    async def __acall__(self, request):
        return await self.get_response(request)
```

## 15.4 Ordre et bonnes pratiques

- **Ordre** : sécurité / statiques en premier, puis sessions → auth → le reste.
- Gardez les middlewares **rapides** (ils s'exécutent à **chaque** requête).
- Pas de logique métier : un middleware sert à des **préoccupations transversales** (journaux, en-têtes, authentification, tenant).
- Déboguez avec `django-debug-toolbar` et en **commentant** progressivement.

---

# 16. Signaux

## 16.1 Principe

Les **signaux** permettent à du code d'être **notifié** quand une action se produit ailleurs (*observer*).

| Signal | Quand |
| --- | --- |
| `pre_save` / `post_save` | Avant / après `save()` |
| `pre_delete` / `post_delete` | Suppression |
| `m2m_changed` | Modification d'une relation ManyToMany |
| `request_started` / `request_finished` | Cycle de requête |
| `user_logged_in` / `user_logged_out` / `user_login_failed` | Authentification |
| `post_migrate` | Après `migrate` |

## 16.2 Utilisation

```python
# apps/comptes/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def creer_profil(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(utilisateur=instance)

# apps/comptes/apps.py
class ComptesConfig(AppConfig):
    name = "apps.comptes"
    def ready(self): from . import signals             # ⚠️ sinon le récepteur n'est jamais branché
```

### Signal personnalisé

```python
from django.dispatch import Signal
commande_payee = Signal()                               # (plus de providing_args)
commande_payee.send(sender=Commande, commande=commande)
```

## 16.3 Précautions et alternatives

| Piège | Remède |
| --- | --- |
| Logique **cachée** (difficile à suivre) | Préférez un **appel explicite** (méthode du modèle, service) |
| `bulk_create`, `update()` **ne déclenchent pas** `post_save` | Appeler explicitement |
| Boucles infinies (un récepteur re-sauvegarde l'objet) | `update_fields`, gardes |
| Travail lent dans le récepteur | **Tâche en arrière-plan** (section 23) avec `transaction.on_commit` |
| Tests difficiles | Tester le récepteur comme une fonction |

> ✅ **Règle** : utilisez les signaux pour **découpler des apps** (ex. : une app tierce réagit à la création d'un utilisateur) ; **sinon** préférez les **services explicites**.

---

# 17. Internationalisation et localisation

## 17.1 Principes

| Terme | Signification |
| --- | --- |
| **i18n** | Rendre le site **traduisible** |
| **l10n** | Adapter à une **langue / région** (formats de date, nombre) |
| **Fuseaux horaires** | `USE_TZ = True`, `zoneinfo` |

```python
LANGUAGE_CODE = "fr"
LANGUAGES = [("fr", "Français"), ("en", "English")]
LOCALE_PATHS = [BASE_DIR / "locale"]
USE_I18N = True
# MIDDLEWARE : ajouter "django.middleware.locale.LocaleMiddleware" juste après SessionMiddleware
```

## 17.2 Marquer les textes

```python
from django.utils.translation import gettext as _, gettext_lazy, ngettext, pgettext

message = _("Bienvenue")
class Article(models.Model):
    titre = models.CharField(gettext_lazy("titre"), max_length=200)        # gettext_lazy : traduit à l'affichage (modèles, formulaires, constantes)
ngettext("%(n)d article", "%(n)d articles", n) % {"n": n}                   # pluriels
```

```django
{% load i18n %}
{% translate "Bienvenue" %}
{% blocktranslate count n=articles|length %}{{ n }} article{% plural %}{{ n }} articles{% endblocktranslate %}
```

## 17.3 Extraire, traduire, compiler

```bash
python manage.py makemessages -l en -l fr --ignore=.venv      # crée locale/<langue>/LC_MESSAGES/django.po
# → traduire les msgstr dans django.po (Poedit, Weblate, Transifex)
python manage.py compilemessages                              # produit django.mo
```

> 🛠️ Nécessite **GNU gettext** installé (`apt install gettext` / `brew install gettext`).

## 17.4 URLs, sélecteur de langue, formats

```python
urlpatterns += i18n_patterns(path("", include("apps.blog.urls")), prefix_default_language=False)
urlpatterns += [path("i18n/", include("django.conf.urls.i18n"))]          # vue set_language
```

Formats localisés : `{{ valeur|date:"DATE_FORMAT" }}`, `{{ nombre|floatformat:2 }}` ; `localize` / `unlocalize`.

## 17.5 Traduire le contenu des **modèles**

| Paquet | Approche |
| --- | --- |
| **`django-modeltranslation`** | Colonnes supplémentaires par langue (`titre_fr`, `titre_en`) |
| **`django-parler`** | Table de traductions séparée |
| **`django-rosetta`** | Interface web pour éditer les `.po` |

## 17.6 Fuseaux horaires

```python
from django.utils import timezone
timezone.now()                                       # datetime « aware » en UTC
timezone.localtime(dt)                               # converti vers le fuseau actif
with timezone.override("Indian/Antananarivo"): ...
```

Stockez en UTC (`USE_TZ = True`) ; convertissez **à l'affichage** (selon l'utilisateur).

---

# 18. Commandes de gestion personnalisées

## 18.1 Créer une commande

```python
# apps/blog/management/commands/archiver_articles.py
# (créer aussi management/__init__.py et management/commands/__init__.py)
from datetime import timedelta
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from apps.blog.models import Article

class Command(BaseCommand):
    help = "Archive les articles publiés depuis plus de N jours."

    def add_arguments(self, parser):
        parser.add_argument("--jours", type=int, default=365)
        parser.add_argument("--dry-run", action="store_true", help="Simuler sans modifier")

    def handle(self, *args, **options):
        limite = timezone.now() - timedelta(days=options["jours"])
        qs = Article.objects.filter(statut="publie", publie_le__lt=limite)
        if options["jours"] < 1:
            raise CommandError("Le nombre de jours doit être positif.")
        if options["dry_run"]:
            self.stdout.write(f"{qs.count()} article(s) seraient archivés.")
            return
        n = qs.update(statut="archive")
        self.stdout.write(self.style.SUCCESS(f"{n} article(s) archivé(s)."))
```

```bash
python manage.py archiver_articles --jours 180 --dry-run
```

## 18.2 Usages

| Usage | Exemple |
| --- | --- |
| **Tâches planifiées** (cron, Kubernetes CronJob) | Nettoyage, rapports, synchronisations |
| **Import / export** de données | CSV, API externes |
| **Maintenance** | Réindexation, recalcul de champs |
| **Démarrage** | Création de données initiales (`loaddata`, fixtures) |

> ✅ Rendez les commandes **idempotentes** et **journalisées** ; pour des traitements longs ou répétés, préférez une **file de tâches** (section 23). Appel depuis le code : `call_command("archiver_articles", jours=30)`.

---

# 🔴 API, asynchrone et frontend

---

# 19. API REST avec Django REST Framework

## 19.1 Pourquoi DRF ?

**Django REST Framework** (DRF) est la bibliothèque de référence pour construire des **API REST** avec Django : **sérialiseurs**, **vues génériques**, **routeurs**, authentification, permissions, pagination, filtrage, limitation de débit, documentation, **API navigable**.

```bash
uv add djangorestframework django-filter drf-spectacular django-cors-headers
```

```python
INSTALLED_APPS += ["rest_framework", "django_filters", "drf_spectacular", "corsheaders"]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ["rest_framework_simplejwt.authentication.JWTAuthentication"],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticatedOrReadOnly"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend",
                                "rest_framework.filters.SearchFilter", "rest_framework.filters.OrderingFilter"],
    "DEFAULT_THROTTLE_CLASSES": ["rest_framework.throttling.AnonRateThrottle", "rest_framework.throttling.UserRateThrottle"],
    "DEFAULT_THROTTLE_RATES": {"anon": "60/min", "user": "600/min"},
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}
```

## 19.2 Sérialiseurs

Un **sérialiseur** convertit modèles ⇄ JSON et **valide** les entrées.

```python
# apps/blog/serializers.py
from rest_framework import serializers
from .models import Article, Categorie

class ArticleSerializer(serializers.ModelSerializer):
    auteur = serializers.StringRelatedField(read_only=True)
    categories = serializers.SlugRelatedField(slug_field="slug", many=True, queryset=Categorie.objects.all(), required=False)
    nb_commentaires = serializers.IntegerField(read_only=True)                 # annotation du QuerySet

    class Meta:
        model = Article
        fields = ["id", "titre", "slug", "contenu", "auteur", "categories", "statut", "publie_le", "nb_commentaires"]
        read_only_fields = ["id", "publie_le"]

    def validate_titre(self, valeur: str) -> str:                              # validation d'un champ
        if len(valeur) < 5: raise serializers.ValidationError("Titre trop court.")
        return valeur

    def validate(self, attrs):                                                 # validation globale
        if attrs.get("statut") == "publie" and not attrs.get("contenu"):
            raise serializers.ValidationError("Contenu requis pour publier.")
        return attrs
```

## 19.3 Vues et ViewSets

```python
# apps/blog/views_api.py
from django.db.models import Count
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class EstAuteurOuLectureSeule(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.auteur == request.user

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, EstAuteurOuLectureSeule]
    filterset_fields = ["statut", "categories__slug", "auteur"]
    search_fields = ["titre", "contenu"]
    ordering_fields = ["publie_le", "titre"]

    def get_queryset(self):                                                    # ✅ optimiser ici (N+1)
        return (Article.objects.select_related("auteur").prefetch_related("categories")
                .annotate(nb_commentaires=Count("commentaires")))

    def perform_create(self, serializer):
        serializer.save(auteur=self.request.user)

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def publier(self, request, pk=None):                                       # POST /articles/{id}/publier/
        article = self.get_object()
        article.publier()
        return Response({"statut": article.statut})
```

| Niveau | Classes |
| --- | --- |
| Bas niveau | `APIView` (comme une CBV) |
| Génériques | `ListAPIView`, `RetrieveUpdateDestroyAPIView`, `ListCreateAPIView`… |
| **ViewSets** ✅ | `ModelViewSet`, `ReadOnlyModelViewSet`, `GenericViewSet` + mixins |
| Fonctions | `@api_view(["GET", "POST"])` |

## 19.4 Routeurs

```python
# apps/blog/urls_api.py
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("articles", ArticleViewSet, basename="article")

# config/urls.py
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
urlpatterns += [
    path("api/v1/", include("apps.blog.urls_api")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema")),
]
```

Routes générées : `GET/POST /articles/`, `GET/PUT/PATCH/DELETE /articles/{id}/`, plus les `@action`.

## 19.5 Pagination, filtrage, tri, recherche

```python
from rest_framework.pagination import CursorPagination, LimitOffsetPagination

class PaginationCurseur(CursorPagination):                  # ✅ stable et rapide sur de gros volumes
    page_size = 20
    ordering = "-publie_le"

# django-filter : filtres personnalisés
import django_filters
class ArticleFilter(django_filters.FilterSet):
    depuis = django_filters.DateTimeFilter(field_name="publie_le", lookup_expr="gte")
    titre = django_filters.CharFilter(lookup_expr="icontains")
    class Meta: model = Article; fields = ["statut", "auteur"]
```

URL : `/api/v1/articles/?statut=publie&search=django&ordering=-publie_le&page=2`.

## 19.6 Limitation de débit, versionnement, erreurs

```python
REST_FRAMEWORK["DEFAULT_VERSIONING_CLASS"] = "rest_framework.versioning.NamespaceVersioning"       # /api/v1/ · /api/v2/

from rest_framework.views import exception_handler
def gestionnaire_erreurs(exc, context):                              # format d'erreur uniforme
    reponse = exception_handler(exc, context)
    if reponse is not None:
        reponse.data = {"erreur": {"code": reponse.status_code, "details": reponse.data}}
    return reponse
REST_FRAMEWORK["EXCEPTION_HANDLER"] = "config.api.gestionnaire_erreurs"
```

Format d'erreur standard recommandé : **RFC 9457** (*Problem Details*). Réglages de débit par vue : `throttle_classes`, `throttle_scope`.

## 19.7 Documentation OpenAPI

```python
SPECTACULAR_SETTINGS = {"TITLE": "Mon API", "VERSION": "1.0.0", "SERVE_INCLUDE_SCHEMA": False}

from drf_spectacular.utils import extend_schema, OpenApiParameter
class VueX(APIView):
    @extend_schema(parameters=[OpenApiParameter("q", str, description="Recherche")], responses=ArticleSerializer(many=True))
    def get(self, request): ...
```

```bash
python manage.py spectacular --file schema.yml            # export OpenAPI 3 ; génération de clients (openapi-generator, orval)
```

## 19.8 Tests d'API

```python
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class ArticleAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("alice", password="x")
        self.client.force_authenticate(self.user)

    def test_creation(self):
        r = self.client.post("/api/v1/articles/", {"titre": "Titre valide", "contenu": "…", "statut": "brouillon"}, format="json")
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        self.assertEqual(r.data["auteur"], "alice")

    def test_anonyme_ne_peut_pas_creer(self):
        self.client.force_authenticate(None)
        self.assertEqual(self.client.post("/api/v1/articles/", {}).status_code, 401)
```

## 19.9 Bonnes pratiques DRF

- **Optimisez** `get_queryset()` (`select_related`, `prefetch_related`, annotations) : le N+1 est le piège n° 1.
- Séparez les sérialiseurs de **lecture** et d'**écriture** si nécessaire (`get_serializer_class`).
- **Versionnez** l'API, **paginez** toujours les listes, **limitez** le débit.
- Ne divulguez pas d'**identifiants séquentiels** sensibles (UUID / slug) ni de champs internes.
- Documentez avec **drf-spectacular** et testez avec `APIClient`.

---

# 20. Authentification des API : JWT et alternatives

*(Section ajoutée : JWT et jetons étaient absents du guide d'origine.)*

## 20.1 Quelle méthode choisir ?

| Méthode | Principe | Idéal pour | Remarques |
| --- | --- | --- | --- |
| **Session + cookie** (+ CSRF) | Cookie `HttpOnly` géré par Django | **SPA du même domaine** (même site), applications web | ✅ Simple et sûr ; protéger contre le CSRF |
| **Jeton DRF (`TokenAuthentication`)** | Un jeton **opaque** stocké en base | Scripts, services internes | Pas d'expiration native, un jeton par utilisateur |
| **JWT** (*JSON Web Token*) | Jeton **signé** et **autoporteur** (accès court + rafraîchissement) | Applications **mobiles**, **SPA** multi-domaines, microservices | **Sans état** côté serveur ; révocation à gérer (liste noire) |
| **OAuth 2.0 / OpenID Connect** | Délégation à un fournisseur d'identité | **SSO**, API publiques, « se connecter avec… » | `django-oauth-toolkit`, `django-allauth` |
| **Clé d'API** | Secret statique par client | Intégrations serveur-à-serveur | `djangorestframework-api-key` |

## 20.2 JWT avec `djangorestframework-simplejwt` ✅

```bash
uv add djangorestframework-simplejwt
```

```python
# settings.py
from datetime import timedelta

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ["rest_framework_simplejwt.authentication.JWTAuthentication"],
}

INSTALLED_APPS += ["rest_framework_simplejwt", "rest_framework_simplejwt.token_blacklist"]      # blacklist : révocation des jetons de rafraîchissement

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),            # court !
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,                             # un nouveau refresh à chaque renouvellement
    "BLACKLIST_AFTER_ROTATION": True,                          # l'ancien refresh est révoqué
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": "HS256",                                      # ou RS256 / ES256 avec clés publique/privée
    "SIGNING_KEY": SECRET_KEY,                                 # idéalement une clé DÉDIÉE
    "AUTH_HEADER_TYPES": ("Bearer",),
}
```

```python
# config/urls.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView

urlpatterns += [
    path("api/auth/jeton/", TokenObtainPairView.as_view(), name="jeton"),               # POST {username, password} → {access, refresh}
    path("api/auth/jeton/rafraichir/", TokenRefreshView.as_view(), name="jeton-refresh"),
    path("api/auth/jeton/verifier/", TokenVerifyView.as_view()),
    path("api/auth/deconnexion/", TokenBlacklistView.as_view()),                        # révoque un refresh
]
```

```bash
# Obtenir les jetons
curl -X POST http://localhost:8000/api/auth/jeton/ -H "Content-Type: application/json" -d '{"username":"alice","password":"secret"}'
# → {"refresh": "eyJ…", "access": "eyJ…"}

# Appeler l'API
curl http://localhost:8000/api/v1/articles/ -H "Authorization: Bearer eyJ…"

# Renouveler l'accès
curl -X POST http://localhost:8000/api/auth/jeton/rafraichir/ -H "Content-Type: application/json" -d '{"refresh":"eyJ…"}'
```

### Personnaliser le contenu du jeton

```python
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MonSerializerJeton(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["nom"] = user.get_full_name()                    # revendications (claims) : peu de données, jamais de secrets
        token["roles"] = list(user.groups.values_list("name", flat=True))
        return token

class MonJetonView(TokenObtainPairView):
    serializer_class = MonSerializerJeton
```

### Connexion par e-mail

Définissez `USERNAME_FIELD = "email"` sur le modèle utilisateur : le serializer l'utilise automatiquement.

## 20.3 Où stocker les jetons côté client ?

| Stockage | Risque | Avis |
| --- | --- | --- |
| `localStorage` / `sessionStorage` | **Lisible par n'importe quel script** (XSS) | ⚠️ À éviter pour le refresh token |
| **Cookie `HttpOnly` + `Secure` + `SameSite`** | Non lisible par JS ; protéger du CSRF | ✅ Recommandé pour le **refresh** (ou les deux) |
| Mémoire JS (variable) | Perdu au rechargement | ✅ Pour l'**access token** de courte durée |
| Mobile : Keychain / Keystore | — | ✅ |

> ⚠️ `simplejwt` ne gère **pas** les cookies nativement : utilisez un paquet dédié (ex. **`dj-rest-auth`** avec `JWT_AUTH_COOKIE`, ou **`django-allauth` headless**) ou écrivez des vues qui posent le refresh en cookie `HttpOnly`.

## 20.4 Bonnes pratiques JWT

- **Access court** (5–15 min) + **refresh** plus long, **rotation** et **liste noire**.
- **HTTPS obligatoire** ; clé de signature **secrète et dédiée** (ou **RS256/ES256** pour des clients vérifiant sans le secret).
- **Ne mettez pas de données sensibles** dans le jeton : il est **encodé, pas chiffré** (lisible par tous).
- Vérifiez **`exp`**, `iss`, `aud` ; prévoyez la **révocation** (changement de mot de passe, déconnexion).
- Un JWT n'est **pas** toujours le bon choix : pour une application web classique ou une SPA du même domaine, les **sessions + cookies** sont plus simples et plus sûres.

## 20.5 Alternatives et compléments

| Paquet | Rôle |
| --- | --- |
| **`dj-rest-auth`** | Points d'accès prêts : connexion, déconnexion, inscription, réinitialisation, JWT/cookies (s'appuie sur allauth) |
| **`django-allauth` (headless)** | API d'authentification complète (sessions ou jetons), réseaux sociaux, 2FA, passkeys |
| **`django-rest-knox`** | Jetons **opaques** hachés, **un par appareil**, expiration, révocation |
| **`django-oauth-toolkit`** | Serveur **OAuth 2.0 / OIDC** |
| **`djangorestframework-api-key`** | Clés d'API par client |
| **`django-ninja-jwt`** | JWT pour **Django Ninja** (port de simplejwt) |
| **`PyJWT`** | Bibliothèque de bas niveau (encoder / décoder des JWT) |

## 20.6 CORS et API consommées par un front séparé

```bash
uv add django-cors-headers
```

```python
INSTALLED_APPS += ["corsheaders"]
MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")             # avant CommonMiddleware
CORS_ALLOWED_ORIGINS = ["https://app.exemple.fr", "http://localhost:5173"]
CORS_ALLOW_CREDENTIALS = True                                             # uniquement si cookies / sessions
CSRF_TRUSTED_ORIGINS = ["https://app.exemple.fr"]
```

> 🚫 **N'utilisez jamais** `CORS_ALLOW_ALL_ORIGINS = True` en production, surtout avec `CORS_ALLOW_CREDENTIALS = True`.

## 20.7 Sessions + CSRF pour une SPA du même site

```python
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_HTTPONLY = False                       # le JS doit lire le cookie csrftoken pour l'envoyer en en-tête X-CSRFToken
```

Le client envoie `X-CSRFToken` sur les requêtes modifiantes ; DRF `SessionAuthentication` applique la vérification CSRF.

---

# 21. Django Ninja, GraphQL et API externes

*(Section ajoutée : frameworks et approches complémentaires.)*

## 21.1 Django Ninja : API typées, façon FastAPI

**Django Ninja** utilise les **annotations de types** et **Pydantic** : peu de code, validation automatique, **OpenAPI** intégrée, support **async**.

```bash
uv add django-ninja
```

```python
# apps/blog/api.py
from ninja import NinjaAPI, Router, Schema, ModelSchema, Query, Field
from ninja.security import HttpBearer
from ninja.pagination import paginate
from django.shortcuts import get_object_or_404

api = NinjaAPI(title="Mon API", version="1.0.0")                        # docs : /api/docs

class Jeton(HttpBearer):                                                  # authentification par jeton
    def authenticate(self, request, token):
        return Utilisateur.objects.filter(api_jeton=token).first()

class ArticleOut(ModelSchema):
    class Meta:
        model = Article
        fields = ["id", "titre", "contenu", "publie_le"]

class ArticleIn(Schema):
    titre: str = Field(min_length=5, max_length=200)
    contenu: str

class Filtres(Schema):
    q: str | None = None

@api.get("/articles", response=list[ArticleOut])
@paginate
def lister(request, filtres: Query[Filtres]):
    qs = Article.objects.publies()
    return qs.filter(titre__icontains=filtres.q) if filtres.q else qs

@api.post("/articles", response={201: ArticleOut}, auth=Jeton())
def creer(request, donnees: ArticleIn):
    return 201, Article.objects.create(auteur=request.auth, **donnees.dict())

@api.get("/articles/{article_id}", response=ArticleOut)
async def detail(request, article_id: int):                              # vue asynchrone
    return await Article.objects.aget(pk=article_id)

# config/urls.py : path("api/", api.urls)
```

| | **DRF** | **Django Ninja** |
| --- | --- | --- |
| Validation | Sérialiseurs | **Pydantic** (types Python) |
| Syntaxe | Classes (ViewSets) | **Fonctions annotées** |
| Documentation | drf-spectacular | **Intégrée** (OpenAPI) |
| Async | Partiel | **Natif** |
| Écosystème | **Immense** (filtres, auth, extensions) | Plus récent, en croissance |
| Idéal | Grandes API, écosystème riche | API rapides à écrire, équipes à l'aise avec FastAPI |

Authentification JWT : **`django-ninja-jwt`**.

## 21.2 GraphQL avec Strawberry

```bash
uv add strawberry-graphql-django
```

```python
import strawberry, strawberry_django
from strawberry import auto

@strawberry_django.type(Article)
class ArticleType:
    id: auto
    titre: auto
    auteur: "UtilisateurType"

@strawberry.type
class Query:
    articles: list[ArticleType] = strawberry_django.field()

schema = strawberry.Schema(query=Query)

# urls.py
from strawberry.django.views import GraphQLView
path("graphql/", GraphQLView.as_view(schema=schema))
```

Alternatives : **Graphene-Django**, **Ariadne**. ⚠️ GraphQL expose un langage de requête : **limitez la profondeur et la complexité**, évitez le N+1 (*DataLoaders*, optimiseurs), et désactivez l'introspection en production si nécessaire.

## 21.3 Consommer des API externes

```bash
uv add httpx
```

```python
import httpx

def meteo(ville: str) -> dict:
    with httpx.Client(timeout=5.0) as client:                              # ✅ TOUJOURS un délai d'expiration
        r = client.get("https://api.exemple.com/meteo", params={"q": ville}, headers={"Authorization": f"Bearer {settings.METEO_CLE}"})
        r.raise_for_status()
        return r.json()

async def meteo_async(ville: str) -> dict:                                  # dans une vue asynchrone
    async with httpx.AsyncClient(timeout=5.0) as client:
        r = await client.get("https://api.exemple.com/meteo", params={"q": ville})
        r.raise_for_status(); return r.json()
```

| Bonne pratique | Détail |
| --- | --- |
| **Ne pas bloquer** une requête web sur une API lente | Déportez vers une **tâche en arrière-plan** (section 23) |
| **Cache** | Mettre en cache les réponses (`cache.get_or_set`) |
| **Nouvelles tentatives** et limites | `tenacity`, `httpx` transports avec retries |
| **Erreurs** | Gérer `httpx.HTTPError`, délais, formats inattendus |
| **Secrets** | Clés dans les variables d'environnement |
| **Tests** | `respx` (httpx), `responses` / `requests-mock` ; ne jamais appeler le réseau réel dans les tests |
| **SSRF** | Valider les URL fournies par l'utilisateur |

## 21.4 Webhooks (recevoir des événements)

```python
import hmac, hashlib
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt          # justifié ici : requête serveur-à-serveur authentifiée par signature
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def webhook_paiement(request):
    signature = request.headers.get("X-Signature", "")
    attendu = hmac.new(settings.WEBHOOK_SECRET.encode(), request.body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(signature, attendu):                         # comparaison à temps constant
        return HttpResponseBadRequest("signature invalide")
    traiter_evenement.delay(request.body.decode())                           # répondre vite (2xx), traiter en arrière-plan
    return HttpResponse(status=202)
```

- **Vérifiez toujours la signature**, rendez le traitement **idempotent** (identifiant d'événement), répondez **rapidement**.

---

# 22. Programmation asynchrone, ASGI et WebSockets

## 22.1 WSGI et ASGI

| | **WSGI** | **ASGI** |
| --- | --- | --- |
| Modèle | **Synchrone** (une requête = un thread) | **Asynchrone**, HTTP + **WebSockets** + SSE |
| Serveurs | Gunicorn, uWSGI | **Uvicorn**, **Daphne**, **Hypercorn**, **Granian** |
| Point d'entrée | `config/wsgi.py` | `config/asgi.py` |
| Usage | Applications classiques | Temps réel, nombreuses E/S concurrentes |

> ✅ Django s'exécute très bien en **WSGI** (Gunicorn). Passez en **ASGI** si vous avez besoin de **WebSockets**, de **SSE**, ou de nombreuses **E/S concurrentes** (appels d'API).

## 22.2 Vues asynchrones

```python
import asyncio, httpx
from django.http import JsonResponse

async def tableau_de_bord(request):
    async with httpx.AsyncClient(timeout=5) as client:
        meteo, actus = await asyncio.gather(                    # appels externes en PARALLÈLE
            client.get("https://api.a.fr/meteo"), client.get("https://api.b.fr/actus"))
    total = await Article.objects.acount()
    return JsonResponse({"meteo": meteo.json(), "actus": actus.json(), "articles": total})
```

### Mélanger synchrone et asynchrone

```python
from asgiref.sync import sync_to_async, async_to_sync

resultat = await sync_to_async(fonction_synchrone)(arg)         # appeler du code sync (ORM non async, bibliothèques bloquantes) depuis async
valeur = async_to_sync(fonction_async)(arg)                      # l'inverse
```

> ⚠️ **Ne bloquez jamais la boucle d'événements** (appels `requests`, `time.sleep`, calculs lourds) : utilisez `httpx.AsyncClient`, `asyncio.sleep`, ou `sync_to_async` / une tâche en arrière-plan. Les **middlewares** synchrones forcent des conversions : préférez des middlewares **compatibles async**.

## 22.3 Django Channels : WebSockets

```bash
uv add channels channels-redis daphne
```

```python
# settings.py
INSTALLED_APPS = ["daphne", *INSTALLED_APPS, "channels"]              # daphne en premier : runserver devient ASGI
ASGI_APPLICATION = "config.asgi.application"
CHANNEL_LAYERS = {"default": {"BACKEND": "channels_redis.core.RedisChannelLayer", "CONFIG": {"hosts": [env("REDIS_URL")]}}}
# Tests / développement : "channels.layers.InMemoryChannelLayer"
```

```python
# config/asgi.py
import os
from django.core.asgi import get_asgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django_asgi = get_asgi_application()                                   # ⚠️ avant d'importer le code des apps

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from apps.chat.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": django_asgi,
    "websocket": AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(websocket_urlpatterns))),
})
```

```python
# apps/chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SalonConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.groupe = f"salon_{self.scope['url_route']['kwargs']['salon']}"
        if not self.scope["user"].is_authenticated:
            await self.close(code=4401); return
        await self.channel_layer.group_add(self.groupe, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.groupe, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(self.groupe, {"type": "message.chat", "texte": data["texte"], "auteur": self.scope["user"].username})

    async def message_chat(self, event):                               # type « message.chat » → méthode message_chat
        await self.send(text_data=json.dumps({"texte": event["texte"], "auteur": event["auteur"]}))

# apps/chat/routing.py
from django.urls import path
websocket_urlpatterns = [path("ws/salon/<str:salon>/", SalonConsumer.as_asgi())]
```

> 🔒 Authentifiez les WebSockets (cookie de session via `AuthMiddlewareStack`, ou jeton dans la chaîne de requête / premier message), validez l'**origine** et limitez les messages.

## 22.4 Événements envoyés par le serveur (SSE)

Plus simples que les WebSockets pour du **flux unidirectionnel** (notifications, progression) :

```python
from django.http import StreamingHttpResponse
async def flux(request):
    async def generateur():
        for i in range(10):
            yield f"data: {i}\n\n"; await asyncio.sleep(1)
    return StreamingHttpResponse(generateur(), content_type="text/event-stream")
```

## 22.5 Déployer en ASGI

```bash
uvicorn config.asgi:application --host 0.0.0.0 --port 8000 --workers 4
# ou Gunicorn + worker Uvicorn (paquet uvicorn-worker)
gunicorn config.asgi:application -k uvicorn_worker.UvicornWorker -w 4 -b 0.0.0.0:8000
daphne -b 0.0.0.0 -p 8000 config.asgi:application
```

---

# 23. Tâches en arrière-plan

## 23.1 Pourquoi ?

Les opérations **lentes ou fragiles** (e-mails, PDF, appels d'API, traitements d'images, rapports) ne doivent **pas** s'exécuter dans la requête HTTP : on les **met en file d'attente** pour qu'un **worker** les traite.

```text
Vue ──enqueue──▶ File (Redis, RabbitMQ, base) ──▶ Worker ──▶ exécute la tâche
  ↓ réponse immédiate
```

## 23.2 Framework de tâches intégré *(Django 6.0, ajout)*

Django 6.0 introduit une **API standard** pour définir et mettre en file des tâches. Django fournit l'**interface** ; l'**exécution en production** est confiée à un **backend** tiers.

```python
# settings.py
TASKS = {"default": {"BACKEND": "django.tasks.backends.immediate.ImmediateBackend"}}      # exécution immédiate (développement / tests)
# Production : un backend externe (ex. paquet django-tasks avec un backend base de données, ou d'autres backends tiers)
```

```python
# apps/blog/tasks.py
from django.tasks import task
from django.core.mail import send_mail

@task
def envoyer_bienvenue(utilisateur_id: int) -> None:
    ...

# Dans une vue / un modèle
resultat = envoyer_bienvenue.enqueue(utilisateur.pk)            # met en file (et non appelle)
```

> ⚠️ Le framework intégré **ne fournit pas de worker de production** : vérifiez la documentation officielle (« Tasks ») et l'état des backends tiers avant de l'adopter ; **Celery** reste la solution la plus éprouvée.

## 23.3 Celery ✅

**Celery** est le système de tâches distribuées de référence (files, planification, nouvelles tentatives, chaînes, résultats).

```bash
uv add celery redis django-celery-beat django-celery-results flower
```

```python
# config/celery.py
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")        # réglages préfixés CELERY_
app.autodiscover_tasks()                                                    # trouve tasks.py dans les apps

# config/__init__.py
from .celery import app as celery_app
__all__ = ("celery_app",)
```

```python
# settings.py
CELERY_BROKER_URL = env("REDIS_URL", default="redis://localhost:6379/0")
CELERY_RESULT_BACKEND = "django-db"                                         # django-celery-results
CELERY_TIMEZONE = "Europe/Paris"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 300
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"   # tâches périodiques éditables dans l'admin
```

```python
# apps/blog/tasks.py
from celery import shared_task

@shared_task(bind=True, autoretry_for=(ConnectionError,), retry_backoff=True, retry_kwargs={"max_retries": 5})
def envoyer_bienvenue(self, utilisateur_id: int) -> None:
    utilisateur = Utilisateur.objects.get(pk=utilisateur_id)                # ✅ passer des IDENTIFIANTS, pas des objets
    send_mail("Bienvenue", "…", None, [utilisateur.email])

# Appel
envoyer_bienvenue.delay(utilisateur.pk)
envoyer_bienvenue.apply_async(args=[utilisateur.pk], countdown=60)          # dans 60 s

# ✅ Après la validation de la transaction (sinon le worker peut ne pas trouver l'objet)
from django.db import transaction
transaction.on_commit(lambda: envoyer_bienvenue.delay(utilisateur.pk))
```

```bash
celery -A config worker -l info                       # worker
celery -A config beat -l info                         # planificateur (tâches périodiques)
celery -A config flower                               # supervision web (http://localhost:5555)
```

### Chaînes, groupes, périodiques

```python
from celery import chain, group, chord
chain(telecharger.s(url), traiter.s(), notifier.s())()              # l'un après l'autre
group(redimensionner.s(i) for i in images)()                          # en parallèle
chord(group(...))(callback.s())                                       # parallèle + rappel final
```

```python
CELERY_BEAT_SCHEDULE = {"nettoyage-nocturne": {"task": "apps.blog.tasks.nettoyer", "schedule": crontab(hour=3, minute=0)}}
```

### Bonnes pratiques Celery

- **Tâches idempotentes** (peuvent être rejouées sans dommage), **petites**, avec **délai maximal**.
- Passer des **identifiants** (JSON sérialisable), pas des instances de modèle.
- `transaction.on_commit` pour mettre en file après la transaction.
- Surveiller (**Flower**, Sentry), configurer **nouvelles tentatives** et files dédiées (`task_routes`).
- Tester avec `CELERY_TASK_ALWAYS_EAGER = True` (les tâches s'exécutent immédiatement) ou en appelant la fonction directement.

## 23.4 Alternatives

| Outil | Caractéristiques |
| --- | --- |
| **Django Tasks** (6.0) | API **intégrée**, standard ; backends en évolution |
| **Celery** | Le plus complet : planification, files multiples, flux (*canvas*) |
| **Huey** (`huey` + Redis) | **Léger**, simple |
| **Dramatiq** (`django-dramatiq`) | Fiable, plus simple que Celery |
| **RQ** (`django-rq`) | Très simple, basé sur Redis |
| **Procrastinate** | File de tâches **sur PostgreSQL** (pas de courtier) |
| **Django-Q2** | Tâches simples avec l'ORM comme courtier |
| **Cron + commandes de gestion** | Tâches périodiques simples |

> ✅ **Choix** : besoin simple → **Django Tasks / Huey / Procrastinate / cron** ; besoin riche (planification, flux, forte volumétrie) → **Celery**.

---

# 24. Frontend moderne avec Django

*(Section ajoutée : les approches actuelles pour construire l'interface.)*

## 24.1 Panorama

| Approche | Principe | Idéal pour |
| --- | --- | --- |
| **Templates Django classiques** | HTML rendu côté serveur | Sites de contenu, back-offices |
| **HTMX + Alpine.js** ✅ | Le serveur renvoie des **fragments HTML** ; interactivité sans SPA | Applications riches **sans** framework JavaScript lourd |
| **Composants de template** (`django-cotton`, `django-components`) | Composants réutilisables en HTML | Design systems côté serveur |
| **Tailwind CSS** (+ Vite) | Utilitaires CSS | Interfaces modernes |
| **SPA** (React, Vue, Svelte) + **DRF / Ninja** | Front séparé, API JSON | Applications très interactives, équipes front dédiées |
| **Inertia.js** (`inertia-django`) | Pages React/Vue pilotées par les vues Django, **sans API** | Monolithe moderne |

## 24.2 HTMX avec `django-htmx`

```bash
uv add django-htmx
```

```python
INSTALLED_APPS += ["django_htmx"]
MIDDLEWARE += ["django_htmx.middleware.HtmxMiddleware"]                  # request.htmx
```

```django
<script src="https://unpkg.com/htmx.org@2.0.4" defer></script>
<body hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'>

<input type="search" name="q" placeholder="Rechercher…"
       hx-get="{% url 'blog:liste' %}" hx-trigger="input changed delay:300ms" hx-target="#resultats" hx-push-url="true">
<div id="resultats">{% include "blog/_liste.html" %}</div>
```

```python
def liste(request):
    articles = Article.objects.publies().filter(titre__icontains=request.GET.get("q", ""))
    gabarit = "blog/liste.html#resultats" if request.htmx else "blog/liste.html"      # fragment (6.0) si requête HTMX
    return render(request, gabarit, {"articles": articles})
```

> ✅ Avec les **partiels de template** (Django 6.0), une seule page sert à la fois la **page complète** et le **fragment**.

## 24.3 Tailwind et ressources front

| Besoin | Outil |
| --- | --- |
| **Tailwind CSS** | `django-tailwind-cli` (sans Node) ou `django-tailwind` ; ou compilation par Vite |
| **Vite** (JS, CSS, rechargement à chaud) | **`django-vite`** |
| Bibliothèques JS | `npm` + bundler, ou *import maps* |
| Compression / empreintes | **WhiteNoise**, `django-compressor` |
| Composants | `django-cotton`, `django-components`, `django-slippers` |
| Icônes | `django-heroicons`, `django-lucide` |

## 24.4 SPA + Django

- **API** : DRF ou Ninja ; **authentification** : sessions (même domaine) ou JWT (section 20) ; **CORS** configuré.
- **Servir le build** du front : par Nginx / CDN, ou via `TemplateView` + WhiteNoise pour une SPA simple.
- **Types partagés** : générez des clients TypeScript depuis le schéma **OpenAPI** (`drf-spectacular` + `openapi-typescript` / `orval`).
- En développement : Vite sur `5173` + Django sur `8000`, proxy ou CORS.

## 24.5 Ordre de conseil

1. **Commencez simple** : templates + **HTMX** couvrent l'immense majorité des besoins.
2. Ajoutez **Alpine.js** pour de petits comportements côté client.
3. Passez à une **SPA** seulement si l'interactivité (éditeur, tableaux complexes, hors-ligne) l'exige.

---

# 🛡️ Qualité et production

---

# 25. Tests

## 25.1 Pourquoi et quoi tester

| Niveau | Cible | Outils |
| --- | --- | --- |
| **Unitaires** | Fonctions, modèles, formulaires, services | `TestCase`, `pytest` |
| **Intégration** | Vues + base de données + templates | `Client`, `APIClient` |
| **Bout en bout (E2E)** | Navigateur réel | **Playwright**, Selenium |
| **Non-régression, performance** | Requêtes SQL, charge | `assertNumQueries`, `locust`, `k6` |

## 25.2 Tests Django (`unittest`)

```python
# apps/blog/tests/test_views.py
from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse
from apps.blog.models import Article

User = get_user_model()

class ArticleTests(TestCase):
    @classmethod
    def setUpTestData(cls):                                         # exécuté UNE fois par classe (rapide)
        cls.alice = User.objects.create_user("alice", "a@exemple.fr", "motdepasse-solide")
        cls.article = Article.objects.create(titre="Bonjour", contenu="…" * 50, auteur=cls.alice, statut="publie")

    def test_liste_affiche_les_articles_publies(self):
        r = self.client.get(reverse("blog:liste"))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "Bonjour")
        self.assertTemplateUsed(r, "blog/liste.html")

    def test_creation_exige_la_connexion(self):
        r = self.client.get(reverse("blog:creer"))
        self.assertRedirects(r, f"{reverse('login')}?next={reverse('blog:creer')}")

    def test_creation(self):
        self.client.force_login(self.alice)
        r = self.client.post(reverse("blog:creer"), {"titre": "Nouveau", "slug": "nouveau", "contenu": "x" * 120, "statut": "brouillon"})
        self.assertEqual(r.status_code, 302)
        self.assertTrue(Article.objects.filter(titre="Nouveau", auteur=self.alice).exists())

    def test_nombre_de_requetes(self):
        with self.assertNumQueries(2):                              # ✅ détecte les régressions N+1
            self.client.get(reverse("blog:liste"))

    @override_settings(EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend")
    def test_email(self):
        self.client.post(reverse("contact"), {"nom": "A", "email": "a@b.fr", "sujet": "q", "message": "Bonjour tout le monde"})
        self.assertEqual(len(mail.outbox), 1)
```

```bash
python manage.py test                              # tous les tests
python manage.py test apps.blog.tests.test_views.ArticleTests.test_creation
python manage.py test --parallel --keepdb          # en parallèle, en conservant la base de test
```

| Classe | Usage |
| --- | --- |
| `SimpleTestCase` | Sans base de données |
| `TestCase` | Chaque test dans une **transaction annulée** ✅ |
| `TransactionTestCase` | Teste le comportement transactionnel (plus lent) |
| `LiveServerTestCase` / `StaticLiveServerTestCase` | Serveur réel pour Selenium / Playwright |

Outils : `Client` (HTTP complet), `RequestFactory` (vue isolée), `override_settings`, `mail.outbox`, `assertContains`, `assertRedirects`, `assertFormError`, `assertNumQueries`, `skipUnless`.

## 25.3 `pytest-django` ✅

```bash
uv add --dev pytest pytest-django pytest-cov pytest-xdist factory-boy faker
```

```ini
# pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = config.settings.test
python_files = tests.py test_*.py *_tests.py
addopts = --reuse-db --strict-markers -ra
```

```python
import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_liste(client, article_factory):                       # `client` : fourni par pytest-django
    article_factory.create_batch(3, statut="publie")
    r = client.get(reverse("blog:liste"))
    assert r.status_code == 200 and r.context["articles"].count() == 3

def test_requetes(client, django_assert_num_queries, db):
    with django_assert_num_queries(2):
        client.get(reverse("blog:liste"))

def test_admin(admin_client): assert admin_client.get("/admin/").status_code == 200
```

Fixtures utiles : `client`, `admin_client`, `rf`, `db`, `transactional_db`, `settings`, `mailoutbox`, `django_assert_num_queries`, `live_server`.

## 25.4 Données de test : `factory_boy`

```python
# apps/blog/tests/factories.py
import factory
from factory.django import DjangoModelFactory

class UtilisateurFactory(DjangoModelFactory):
    class Meta: model = User
    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda o: f"{o.username}@exemple.fr")
    password = factory.PostGenerationMethodCall("set_password", "motdepasse")

class ArticleFactory(DjangoModelFactory):
    class Meta: model = Article
    titre = factory.Faker("sentence", locale="fr_FR")
    contenu = factory.Faker("paragraph", nb_sentences=8, locale="fr_FR")
    auteur = factory.SubFactory(UtilisateurFactory)

# conftest.py
from pytest_factoryboy import register          # (paquet pytest-factoryboy) → fixtures article_factory, utilisateur_factory
register(UtilisateurFactory); register(ArticleFactory)
```

> ✅ **Factories** plutôt que fixtures JSON : plus lisibles, plus faciles à maintenir. Alternative : **`model_bakery`**.

## 25.5 Tester des API

Voir [19.8](#198-tests-dapi) (`APIClient`). Authentification : `client.force_authenticate(user)` ou `client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")`.

## 25.6 Mocks, temps et services externes

```python
from unittest import mock
from freezegun import freeze_time              # ou time-machine

@freeze_time("2026-10-14 12:00")
def test_publication_planifiee(db): ...

@mock.patch("apps.blog.services.httpx.Client.get")
def test_meteo(mock_get):
    mock_get.return_value.json.return_value = {"temp": 20}
    ...

# Tâches Celery : exécuter immédiatement, ou appeler la fonction directement
@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
def test_avec_taches_immediates(): ...
```

Outils : **`respx`** (httpx), **`responses`** / `requests-mock`, **`moto`** (AWS), `pytest-mock`. **Aucun appel réseau réel** dans les tests unitaires.

## 25.7 Réglages de test rapides

```python
# config/settings/test.py
from .base import *
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]       # ⚠️ TESTS UNIQUEMENT : hachage rapide
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
CACHES = {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}
STORAGES = {"default": {"BACKEND": "django.core.files.storage.InMemoryStorage"}, "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"}}
CELERY_TASK_ALWAYS_EAGER = True
```

## 25.8 Tests E2E avec Playwright

```bash
uv add --dev pytest-playwright && playwright install
```

```python
def test_connexion(live_server, page):
    page.goto(f"{live_server.url}/comptes/login/")
    page.get_by_label("Nom d'utilisateur").fill("alice")
    page.get_by_label("Mot de passe").fill("motdepasse")
    page.get_by_role("button", name="Connexion").click()
    assert page.get_by_text("Bonjour alice").is_visible()
```

(Avec `pytest-django`, utilisez `live_server` ; en mode `unittest`, `StaticLiveServerTestCase`.)

## 25.9 Couverture et intégration continue

```bash
pytest --cov=apps --cov-report=term-missing --cov-fail-under=80
```

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:17
        env: { POSTGRES_PASSWORD: postgres, POSTGRES_DB: test }
        ports: ["5432:5432"]
        options: >-
          --health-cmd pg_isready --health-interval 5s --health-timeout 5s --health-retries 10
    env:
      DATABASE_URL: postgres://postgres:postgres@localhost:5432/test
      SECRET_KEY: test-key
      DJANGO_SETTINGS_MODULE: config.settings.test
    steps:
      - uses: actions/checkout@v6
      - uses: astral-sh/setup-uv@v6
      - run: uv sync --frozen
      - run: uv run ruff check . && uv run ruff format --check .
      - run: uv run mypy .
      - run: uv run python manage.py makemigrations --check --dry-run
      - run: uv run pytest -n auto --cov=apps
```

## 25.10 Bonnes pratiques

- Un test = **un comportement**, nom explicite, **indépendant** des autres.
- Testez **cas nominaux, limites et refusés** (permissions !).
- **`assertNumQueries`** sur les pages sensibles ; mode `fetch_mode(FETCH_RAISE)` pour repérer les N+1.
- Vérifiez en CI : `makemigrations --check`, `manage.py check --deploy`, linting, types.

---

# 26. Sécurité

## 26.1 Les protections intégrées

| Menace | Protection Django |
| --- | --- |
| **Injection SQL** | ORM et requêtes **paramétrées** |
| **XSS** | Échappement automatique des templates ; **CSP** (6.0) |
| **CSRF** | Middleware + `{% csrf_token %}` |
| **Clickjacking** | `XFrameOptionsMiddleware` (`X_FRAME_OPTIONS`) |
| **Fixation / vol de session** | Cookies `HttpOnly`, clé régénérée à la connexion |
| **Mots de passe** | Hachage PBKDF2 / Argon2, validateurs |
| **Host header** | `ALLOWED_HOSTS` |
| **Téléversements** | Noms nettoyés, limites de taille |
| **HTTPS** | `SECURE_SSL_REDIRECT`, HSTS |

## 26.2 Liste de contrôle de production

```bash
python manage.py check --deploy
```

```python
DEBUG = False
SECRET_KEY = env("SECRET_KEY")                          # longue, aléatoire, jamais versionnée ; rotation possible via SECRET_KEY_FALLBACKS
ALLOWED_HOSTS = ["exemple.fr", "www.exemple.fr"]

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_HSTS_SECONDS = 31_536_000; SECURE_HSTS_INCLUDE_SUBDOMAINS = True; SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True; SESSION_COOKIE_HTTPONLY = True; SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SECURE = True; CSRF_TRUSTED_ORIGINS = ["https://exemple.fr"]
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "same-origin"
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin"
X_FRAME_OPTIONS = "DENY"
DATA_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024
```

## 26.3 Content Security Policy *(Django 6.0, ajout)*

La **CSP** limite les sources de scripts, styles, images…, et réduit fortement l'impact d'un **XSS**. Django 6.0 l'intègre :

```python
from django.utils.csp import CSP

MIDDLEWARE += ["django.middleware.csp.ContentSecurityPolicyMiddleware"]
TEMPLATES[0]["OPTIONS"]["context_processors"] += ["django.template.context_processors.csp"]

SECURE_CSP_REPORT_ONLY = {                               # 1) commencer en mode « rapport » seulement
    "default-src": [CSP.SELF],
    "script-src": [CSP.SELF, CSP.NONCE],                 # nonce généré par requête
    "style-src": [CSP.SELF, CSP.NONCE],
    "img-src": [CSP.SELF, "data:", "https:"],
    "object-src": [CSP.NONE],
    "base-uri": [CSP.NONE],
    "frame-ancestors": [CSP.NONE],
    "report-uri": "/csp-report/",
}
# 2) puis passer à l'application stricte : SECURE_CSP = {...}
```

```django
<script nonce="{{ csp_nonce }}">/* script en ligne autorisé */</script>
```

> ✅ Évitez `'unsafe-inline'` et `'unsafe-eval'`. Pour les versions antérieures : **`django-csp`**.

## 26.4 Les vulnérabilités à connaître

| Faille | Cause | Parade |
| --- | --- | --- |
| **XSS** | `\|safe`, `mark_safe`, `innerHTML` avec des données utilisateur | Laisser l'échappement ; assainir avec **`nh3`** / `bleach` si HTML riche ; CSP |
| **Injection SQL** | `raw()` / `extra()` / `cursor.execute` avec f-strings | **Paramètres** (`%s`) ; ORM |
| **CSRF** | Pas de jeton | `{% csrf_token %}`, `X-CSRFToken`, cookies `SameSite` |
| **IDOR** (accès direct à un objet) | Pas de contrôle de propriété | **Filtrer par utilisateur** (`get_object_or_404(Article, pk=pk, auteur=request.user)`), permissions d'objet |
| **Mass assignment** | `fields = "__all__"` | Liste **explicite** de champs |
| **Redirection ouverte** | `redirect(request.GET["next"])` | `url_has_allowed_host_and_scheme()` |
| **Traversée de chemin / upload** | Nom de fichier utilisateur | Valider, renommer, hors racine web |
| **SSRF** | Appeler une URL fournie par l'utilisateur | Liste blanche, bloquer les IP privées |
| **Désérialisation** | `pickle` sur des données non fiables | JSON uniquement |
| **Fuite d'informations** | `DEBUG = True`, traces d'erreurs | `DEBUG = False`, Sentry, pages d'erreur génériques |
| **Énumération** | Messages « utilisateur inconnu » | Messages identiques |
| **Force brute** | Connexions illimitées | `django-axes`, `django-ratelimit`, throttling DRF |

```python
from django.utils.http import url_has_allowed_host_and_scheme
suivant = request.POST.get("next", "")
if not url_has_allowed_host_and_scheme(suivant, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
    suivant = "/"
```

```python
from django.views.decorators.debug import sensitive_post_parameters, sensitive_variables
@sensitive_post_parameters("motdepasse")          # masquées dans les rapports d'erreur
def connexion(request): ...
```

## 26.5 Secrets et configuration

- **Jamais** de secrets dans Git (utiliser `.env` ignoré, **variables d'environnement**, gestionnaires de secrets : Vault, AWS/GCP Secret Manager, SOPS).
- Une **`SECRET_KEY` différente** par environnement ; rotation avec `SECRET_KEY_FALLBACKS`.
- Comptes de base de données aux **privilèges minimaux** ; **TLS** vers la base.

## 26.6 Dépendances et mises à jour

```bash
uv run pip-audit                           # vulnérabilités connues dans les dépendances
uv add --dev bandit && bandit -r apps      # analyse statique de sécurité (ou règles « S » de ruff)
```

- **Appliquez les correctifs de sécurité** Django rapidement : ils sont annoncés sur **django-announce** (et `security@djangoproject.com` pour signaler). Suivez les versions **supportées** (5.2 LTS, 6.0, 6.1).
- **Dependabot / Renovate** pour les mises à jour automatiques ; verrouillez les versions ; relisez les nouveaux paquets avant installation.

## 26.7 Limitation de débit et protection des comptes

```python
INSTALLED_APPS += ["axes"]
AUTHENTICATION_BACKENDS = ["axes.backends.AxesStandaloneBackend", "django.contrib.auth.backends.ModelBackend"]
MIDDLEWARE += ["axes.middleware.AxesMiddleware"]
AXES_FAILURE_LIMIT = 5; AXES_COOLOFF_TIME = 1                    # 5 échecs → blocage 1 heure
```

```python
from django_ratelimit.decorators import ratelimit
@ratelimit(key="ip", rate="5/m", block=True)
def connexion(request): ...
```

## 26.8 Sécurité de l'infrastructure

- **HTTPS** (Let's Encrypt, Caddy), **HSTS**, TLS ≥ 1.2.
- Conteneurs : **utilisateur non root**, images minimales, pas de secrets dans les images.
- **Pare-feu**, base **non exposée**, sauvegardes **chiffrées et testées**.
- **Journaux** d'audit, alertes (Sentry), surveillance.
- Référence : **OWASP Top 10**, guide « Security in Django » de la documentation officielle.

---

# 27. Performances

## 27.1 Mesurer d'abord

| Outil | Usage |
| --- | --- |
| **`django-debug-toolbar`** | Requêtes SQL, doublons, temps, templates (développement) |
| **`django-silk`**, **`django-querycount`** | Profilage de requêtes / SQL |
| **Sentry Performance**, **OpenTelemetry**, **Datadog**, **New Relic** | Production (APM) |
| `EXPLAIN ANALYZE` (`.explain()`), `pg_stat_statements` | Base de données |
| **`py-spy`**, `cProfile`, **Scalene** | Profilage Python |
| **`locust`**, **`k6`**, `wrk` | Tests de charge |

## 27.2 Les gains les plus importants (par ordre d'impact)

1. **Base de données** : supprimer le **N+1**, ajouter les **index** utiles, `only()` / `values()`, paginer, agréger en SQL ([section 9](#9-orm--requêtes-et-optimisation)).
2. **Cache** : fragments, vues, objets coûteux, Redis ([section 13](#13-messages-sessions-et-cache)).
3. **Tâches lentes en arrière-plan** ([section 23](#23-tâches-en-arrière-plan)).
4. **Statiques via CDN / serveur web**, compression, cache HTTP.
5. **Connexions** : pool psycopg (`"pool": True`) ou **PgBouncer** ; `CONN_MAX_AGE`.
6. **Serveur d'application** : nombre de workers adapté, `gthread`/async si E/S.

## 27.3 Pagination et gros volumes

```python
paginator = Paginator(qs, 25)                                   # ou CursorPagination (DRF) : pagination par « curseur » stable et rapide
for lot in qs.iterator(chunk_size=2000): ...                    # mémoire constante
Article.objects.bulk_create(objets, batch_size=1000)
```

> ⚠️ `OFFSET` élevé est lent sur de très grandes tables : préférez la **pagination par curseur** (clé d'ordre).

## 27.4 Modèles et templates

- `{% cache %}` pour les blocs coûteux ; le chargeur de templates **mis en cache** est activé automatiquement hors `DEBUG`.
- Évitez les **requêtes dans les templates** (boucles sur des relations non préchargées).
- `django.contrib.humanize` et filtres lourds : à utiliser avec mesure.

## 27.5 Serveur d'application

```bash
gunicorn config.wsgi:application --workers 5 --threads 2 --worker-class gthread --timeout 30 --max-requests 1000 --max-requests-jitter 100 --bind 0.0.0.0:8000
```

| Réglage | Conseil |
| --- | --- |
| `--workers` | Environ **(2 × cœurs) + 1** pour des charges mixtes (ajuster selon la mémoire) |
| `--threads` | Quelques threads (`gthread`) pour les E/S |
| `--max-requests` | Recycle les processus (limite les fuites mémoire) |
| `--timeout` | Bas : un worker bloqué est tué |
| ASGI | `uvicorn` / `granian` pour l'asynchrone |

## 27.6 Performances côté réseau et navigateur

- **GZip / Brotli** (au niveau Nginx / CDN), `ConditionalGetMiddleware`, en-têtes `Cache-Control` sur les statiques hachés.
- Images optimisées (**WebP/AVIF**, tailles multiples avec `sorl-thumbnail` / `easy-thumbnails` / `django-imagekit`), chargement paresseux.
- HTTP/2 ou 3, CDN pour statiques et médias.

---

# 28. Déploiement

## 28.1 Vue d'ensemble

```text
Internet ─▶ Proxy / CDN (Nginx, Caddy, Cloudflare)
              ├─▶ Statiques (WhiteNoise / Nginx / CDN)
              └─▶ Gunicorn / Uvicorn (Django) ──▶ PostgreSQL · Redis
                                                  └─▶ Workers (Celery / Tasks) · Beat
```

## 28.2 Liste de contrôle

- [ ] `DEBUG = False`, `SECRET_KEY` et secrets en **variables d'environnement**
- [ ] `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, HTTPS, HSTS (voir section 26)
- [ ] **PostgreSQL** (pas SQLite), sauvegardes automatiques **testées**
- [ ] `collectstatic` exécuté, statiques servis efficacement
- [ ] **Migrations** appliquées (étape de déploiement dédiée)
- [ ] Journaux vers la sortie standard, **Sentry** pour les erreurs
- [ ] Serveur d'application (Gunicorn / Uvicorn), **proxy inverse**, **workers** et planificateur
- [ ] **Surveillance** (santé, métriques, alertes), `check --deploy` au vert

## 28.3 Dockerfile (multi-étapes avec `uv`)

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.13-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
WORKDIR /app

FROM base AS deps
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv uv sync --frozen --no-dev --no-install-project

FROM base AS final
RUN useradd --create-home --uid 1000 app
COPY --from=deps /app/.venv /app/.venv
COPY . .
ENV PATH="/app/.venv/bin:$PATH" DJANGO_SETTINGS_MODULE=config.settings.prod
RUN SECRET_KEY=build-only python manage.py collectstatic --noinput
USER app
EXPOSE 8000
HEALTHCHECK --interval=30s CMD python -c "import urllib.request as u; u.urlopen('http://localhost:8000/sante/')"
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--access-logfile", "-"]
```

```yaml
# compose.yaml (développement / petite production)
services:
  web:
    build: .
    env_file: .env
    ports: ["8000:8000"]
    depends_on: { db: { condition: service_healthy }, redis: { condition: service_started } }
  worker:
    build: .
    command: celery -A config worker -l info
    env_file: .env
    depends_on: [db, redis]
  beat:
    build: .
    command: celery -A config beat -l info
    env_file: .env
    depends_on: [db, redis]
  db:
    image: postgres:17
    environment: { POSTGRES_DB: monsite, POSTGRES_USER: monsite, POSTGRES_PASSWORD: ${DB_PASSWORD} }
    volumes: [pgdata:/var/lib/postgresql/data]
    healthcheck: { test: ["CMD-SHELL", "pg_isready -U monsite"], interval: 5s, retries: 10 }
  redis:
    image: redis:7-alpine
volumes:
  pgdata:
```

> ✅ Exécutez les **migrations** dans une **étape de déploiement** (`python manage.py migrate --noinput` en *release command* / *init container*), pas dans chaque instance au démarrage.

## 28.4 Nginx (proxy inverse)

```nginx
server {
    listen 443 ssl http2;
    server_name exemple.fr;
    ssl_certificate     /etc/letsencrypt/live/exemple.fr/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/exemple.fr/privkey.pem;

    client_max_body_size 10m;

    location /static/ { alias /app/staticfiles/; expires 1y; add_header Cache-Control "public, immutable"; }
    location /media/  { alias /app/media/; }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;          # utilisé par SECURE_PROXY_SSL_HEADER
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Upgrade $http_upgrade;               # WebSockets (ASGI)
        proxy_set_header Connection "upgrade";
    }
}
```

**Caddy** (HTTPS automatique) : `exemple.fr { reverse_proxy 127.0.0.1:8000 }`.

## 28.5 Vue de santé et supervision

```python
from django.db import connection
from django.http import JsonResponse

def sante(request):
    try:
        with connection.cursor() as c: c.execute("SELECT 1")
        return JsonResponse({"statut": "ok"})
    except Exception:
        return JsonResponse({"statut": "erreur"}, status=503)
```

Outils : **`django-health-check`**, **Sentry** (`sentry-sdk[django]`), Prometheus (`django-prometheus`), OpenTelemetry, journaux JSON (`python-json-logger`, `structlog`).

```python
import sentry_sdk
sentry_sdk.init(dsn=env("SENTRY_DSN"), send_default_pii=False, traces_sample_rate=0.1, environment="production")
```

## 28.6 Déploiements sans interruption

Appliquez le motif **expand / contract** : (1) **ajouter** colonnes/tables de façon **rétrocompatible**, (2) déployer le code qui gère les **deux** schémas, (3) **nettoyer** ensuite. Évitez les migrations qui **verrouillent** de grosses tables ; ajoutez les index avec `AddIndexConcurrently` (PostgreSQL). Utilisez des **déploiements progressifs** (*rolling*) et des **sondes de santé**.

## 28.7 Plateformes d'hébergement

| Type | Exemples |
| --- | --- |
| **PaaS** (le plus simple) | Render, Railway, **Fly.io**, Heroku, Scalingo, PythonAnywhere, Platform.sh |
| **Cloud** | AWS (ECS / App Runner / Elastic Beanstalk), Google Cloud Run, Azure App Service |
| **Serveur (VPS)** | Debian + Nginx/Caddy + **systemd** (Gunicorn) ou **Docker Compose** ; **Kamal**, Coolify, Dokku (déploiement auto-hébergé) |
| **Kubernetes** | Grands déploiements : Deployment (web), Deployment (workers), CronJob, Job de migration, Ingress |

```ini
# /etc/systemd/system/monsite.service  (VPS sans Docker)
[Unit]
Description=Gunicorn - Mon site
After=network.target

[Service]
User=app
WorkingDirectory=/srv/monsite
EnvironmentFile=/srv/monsite/.env
ExecStart=/srv/monsite/.venv/bin/gunicorn config.wsgi:application --workers 4 --bind unix:/run/monsite.sock
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

## 28.8 Intégration et livraison continues

Pipeline typique : **lint + types + tests** → **construction de l'image** → **analyse** (pip-audit, Trivy) → **déploiement** (migrations, collectstatic, redémarrage) → **vérification de santé** → **retour arrière** automatique en cas d'échec.

---

# 29. Écosystème : paquets essentiels

*(Section ajoutée : les paquets utiles avec Django, y compris ceux qui manquaient au guide d'origine.)*

## 29.1 Carte des paquets par besoin

| Besoin | Paquets recommandés |
| --- | --- |
| **API REST** | `djangorestframework`, `django-filter`, `drf-spectacular`, `django-cors-headers`, **Django Ninja** |
| **JWT / jetons** | **`djangorestframework-simplejwt`**, `dj-rest-auth`, `django-rest-knox`, `django-ninja-jwt`, `PyJWT` |
| **Authentification avancée** | **`django-allauth`**, `django-oauth-toolkit`, `social-auth-app-django`, `django-otp`, `django-two-factor-auth` |
| **Permissions** | `django-guardian` (objets), `django-rules` |
| **Sécurité** | `django-axes`, `django-ratelimit`, `django-csp` (avant 6.0), `django-defender`, `pip-audit`, `bandit` |
| **GraphQL** | `strawberry-graphql-django`, `graphene-django`, `ariadne` |
| **Tâches asynchrones** | **Celery** (+ `django-celery-beat`, `django-celery-results`, Flower), Django Tasks (6.0), `huey`, `dramatiq`, `django-rq`, `procrastinate` |
| **Temps réel** | `channels`, `channels-redis`, `daphne` |
| **Serveurs** | `gunicorn`, `uvicorn`, `granian`, `hypercorn` |
| **Cache / files** | `redis`, `django-redis`, `django-cacheops` |
| **Configuration** | `django-environ`, `python-decouple`, `dj-database-url`, `pydantic-settings` |
| **Statiques / médias** | `whitenoise`, `django-storages` + `boto3`, `django-compressor`, `django-vite`, `sorl-thumbnail` / `django-imagekit` |
| **Admin** | `django-unfold`, `django-jazzmin`, `django-import-export`, `django-simple-history`, `django-reversion`, `django-admin-sortable2` |
| **Éditeur riche** | `django-ckeditor-5`, `django-tinymce`, `django-prose` |
| **Formulaires** | `django-crispy-forms`, `django-widget-tweaks`, `django-formtools`, `django-select2`, `django-autocomplete-light` |
| **Frontend** | `django-htmx`, `django-cotton`, `django-components`, `django-tailwind-cli`, `inertia-django`, `django-template-partials` (avant 6.0) |
| **Modèles utiles** | `django-model-utils`, `django-extensions`, `django-taggit`, `django-mptt` / `django-treebeard` (arbres), `django-polymorphic`, `django-money`, `django-phonenumber-field`, `django-countries`, `django-fsm` (machines d'états), `django-softdelete` |
| **Recherche** | `django-haystack`, `django-elasticsearch-dsl`, Meilisearch / Typesense clients, `pgvector` (`pgvector-python`) pour les embeddings |
| **E-mail** | `django-anymail` (Mailgun, SES, Brevo…), `django-mailer` |
| **Internationalisation** | `django-modeltranslation`, `django-parler`, `django-rosetta` |
| **CMS / e-commerce** | **Wagtail** (CMS), `django-cms`, **Saleor**, `django-oscar`, `Mezzanine` |
| **Géospatial** | `django.contrib.gis` + PostGIS, `django-leaflet` |
| **SEO / sitemaps** | `django.contrib.sitemaps`, `django-meta` |
| **Surveillance** | `sentry-sdk`, `django-prometheus`, `django-health-check`, `opentelemetry-instrumentation-django` |
| **Débogage / profilage** | `django-debug-toolbar`, `django-silk`, `django-querycount`, `django-extensions` |
| **Tests** | `pytest-django`, `factory-boy`, `model-bakery`, `faker`, `freezegun`, `respx`, `pytest-xdist`, `pytest-playwright`, `coverage` |
| **Qualité / outillage** | `ruff`, `mypy` + **`django-stubs`**, `djangorestframework-stubs`, `djlint`, `django-upgrade`, `pre-commit` |
| **Gabarits de projet** | `cookiecutter-django` |

## 29.2 Exemple de `pyproject.toml` de départ

```toml
[project]
name = "monsite"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "django>=6.1,<6.2",
    "psycopg[binary,pool]>=3.2",
    "django-environ",
    "whitenoise",
    "gunicorn",
    "djangorestframework",
    "djangorestframework-simplejwt",
    "drf-spectacular",
    "django-filter",
    "django-cors-headers",
    "django-htmx",
    "django-allauth",
    "celery[redis]",
    "django-celery-beat",
    "django-storages[s3]",
    "sentry-sdk[django]",
    "argon2-cffi",
    "pillow",
]

[dependency-groups]
dev = [
    "django-stubs[compatible-mypy]", "djangorestframework-stubs", "mypy",
    "ruff", "djlint", "pre-commit", "django-upgrade",
    "pytest", "pytest-django", "pytest-cov", "pytest-xdist", "factory-boy", "pytest-factoryboy", "freezegun", "respx",
    "django-debug-toolbar", "django-extensions", "ipython", "pip-audit",
]
```

## 29.3 Choisir un paquet tiers

| Critère | À vérifier |
| --- | --- |
| **Compatibilité** | Versions de **Django** et **Python** supportées (classifiers PyPI, notes de version) |
| **Maintenance** | Dernière publication, issues, nombre de mainteneurs |
| **Popularité** | Étoiles, téléchargements, **Django Packages** (djangopackages.org) |
| **Sécurité** | Historique de vulnérabilités, `pip-audit` |
| **Besoin réel** | Parfois quelques lignes de Django suffisent |

> ⚠️ Un paquet **abandonné** (ex. `django-ckeditor` v4, `django-grappelli` ancien, Akita…) est une **dette** : vérifiez avant d'adopter.

---

# 30. Nouveautés par version, bonnes pratiques et ressources

## 30.1 Nouveautés notables (4.2 → 6.1)

| Version | Points marquants |
| --- | --- |
| **4.2 LTS** | Réglage `STORAGES`, `psycopg` 3, commentaires de colonnes, backend de cache Redis intégré (4.0) |
| **5.0** | **`db_default`**, **`GeneratedField`**, rendu des formulaires en `div` et `as_field_group`, **facettes** de l'admin, choix par mapping, `USE_TZ = True` par défaut, `ZoneInfo` |
| **5.1** | **`LoginRequiredMiddleware`**, balise **`{% querystring %}`**, **pool de connexions** PostgreSQL, `CheckConstraint(condition=…)`, suppression de `DEFAULT_FILE_STORAGE` / `index_together` |
| **5.2 LTS** | **Clés primaires composites** (`CompositePrimaryKey`), `shell` qui importe automatiquement les modèles, améliorations de l'admin et de l'ORM |
| **6.0** | **Framework de tâches** (`django.tasks`), **CSP intégrée**, **partiels de template** (`{% partialdef %}`), `BigAutoField` par défaut, Python 3.12+ |
| **6.1** | **Modes de chargement** (`fetch_mode`), `on_delete` **au niveau base** (`DB_CASCADE`…), réglage **`MAILERS`**, fonctions `UUID4` / `UUID7`, `JSONNull`, agrégats de bits |
| **6.2 LTS** *(prévue avril 2027)* | Prochaine version à support long terme |

> 📌 Pour le détail exact (et les suppressions de fonctionnalités dépréciées), lisez les **notes de version** : [docs.djangoproject.com/en/6.1/releases/](https://docs.djangoproject.com/en/6.1/releases/).

## 30.2 Mettre à jour Django *(ajout)*

1. **Passez de LTS en LTS** ou version par version (ne sautez pas de versions majeures de plusieurs pas).
2. Lisez les **notes de version** et la section « *Features deprecated* ».
3. Lancez les tests avec les avertissements en erreurs :
   ```bash
   python -Wa manage.py test           # affiche les DeprecationWarning
   pytest -W error::DeprecationWarning
   ```
4. **`django-upgrade`** réécrit automatiquement le code : `django-upgrade --target-version 6.1 $(git ls-files '*.py')`.
5. Vérifiez la **compatibilité des paquets tiers** et la **version de Python**.
6. Testez, déployez en **préproduction**, surveillez.

Exemples de suppressions courantes lors des migrations récentes : `DEFAULT_FILE_STORAGE` / `STATICFILES_STORAGE` → `STORAGES` ; `USE_L10N` et **pytz** → `zoneinfo` ; `CheckConstraint(check=…)` → `condition=` ; `index_together` → `indexes` ; `EMAIL_*` → `MAILERS` (avant Django 7.0).

## 30.3 Bonnes pratiques générales

| Domaine | Pratique |
| --- | --- |
| **Structure** | Apps petites et cohérentes, réglages séparés (`base`/`dev`/`prod`/`test`), **modèle utilisateur personnalisé dès le départ** |
| **Modèles** | Contraintes en base, index adaptés, `select_related`/`prefetch_related`, **logique métier** dans des services / QuerySets |
| **Vues** | Minces ; CBV génériques pour le CRUD, FBV pour le particulier |
| **Sécurité** | `check --deploy`, HTTPS/HSTS, CSP, secrets hors du dépôt, mises à jour de sécurité immédiates |
| **API** | DRF ou Ninja, versionnement, pagination, limitation de débit, **JWT court + rafraîchissement** ou sessions |
| **Asynchrone** | Tâches lentes en arrière-plan, `transaction.on_commit`, tâches **idempotentes** |
| **Tests** | `pytest-django` + factories, `assertNumQueries`, CI avec `makemigrations --check` |
| **Qualité** | `ruff`, `mypy` + `django-stubs`, `djlint`, `pre-commit` |
| **Déploiement** | Docker, Gunicorn/Uvicorn, PostgreSQL, Redis, WhiteNoise/CDN, Sentry, sauvegardes testées |
| **Mises à jour** | Rester sur une version **supportée** ; migrer de LTS en LTS |

## 30.4 Les erreurs classiques

- `DEBUG = True` en production · secrets dans Git · `ALLOWED_HOSTS = ["*"]`.
- **N+1** non détecté · absence d'index · `len(qs)` au lieu de `qs.count()`.
- `fields = "__all__"` · pas de contrôle de propriété (**IDOR**) · logique dans les templates.
- Modèle utilisateur par défaut puis changement tardif · migrations modifiées après déploiement.
- Tâche Celery lancée **avant** la validation de la transaction · objets passés aux tâches au lieu d'identifiants.
- Bloquer la boucle asynchrone avec du code synchrone · CORS ouvert à tous.

## 30.5 Ressources

- 📘 **Documentation officielle** : <https://docs.djangoproject.com/fr/>
- 🎓 **Tutoriel officiel** (sondages) : <https://docs.djangoproject.com/fr/6.1/intro/tutorial01/>
- 📜 **Notes de version** : <https://docs.djangoproject.com/en/6.1/releases/>
- 📦 **Django Packages** : <https://djangopackages.org> · **PyPI** : <https://pypi.org>
- 🔍 **Classy Class-Based Views** : <https://ccbv.co.uk> · **Classy DRF** : <https://www.cdrf.co>
- 🌐 **DRF** : <https://www.django-rest-framework.org> · **Django Ninja** : <https://django-ninja.dev> · **Celery** : <https://docs.celeryq.dev>
- 🔒 **Sécurité Django** : <https://docs.djangoproject.com/fr/6.1/topics/security/> · **OWASP** : <https://owasp.org>
- 📚 *Two Scoops of Django* (Greenfeld & Roy), *Django for Professionals / APIs* (William S. Vincent), blog de **Adam Johnson**, **Simon Willison**, **Django News** (newsletter)

---

<div align="center">

*Bon développement avec Django ! 🎸*

</div>
