# Django — Cours complet

*Module d'apprentissage détaillé, rédigé section par section à partir du plan fourni (Django 6.1, octobre 2026)*

## Avant de commencer : mode d'emploi du cours

**À qui s'adresse ce cours ?** À toute personne qui connaît les bases de Python (variables, fonctions, classes, modules, exceptions, compréhensions de listes, annotations de types) et qui veut apprendre à construire, tester et déployer des applications web professionnelles avec Django.

**Fil rouge.** Tous les exemples s'appuient sur un même projet en français : un **blog** (articles, catégories, commentaires) et une **boutique** (produits, commandes). Vous retrouverez donc toujours les mêmes noms : `Article`, `Categorie`, `Commentaire`, `Produit`, `Commande`, `Utilisateur`.

**Structure de chaque section.** Chaque chapitre suit le même schéma : *objectifs d'apprentissage* → *concepts et définitions* → *exemples commentés* → *pièges et bonnes pratiques* → *à retenir*.

**Légende.** *(ajout)* = notion absente du guide d'origine ; *(à jour)* = pratique moderne qui remplace une ancienne ; *(5.x / 6.x)* = version de Django qui introduit la fonctionnalité.

> **Note sur les nouveautés récentes.** Les fonctionnalités propres à Django 6.0 et 6.1 (framework de tâches, CSP intégrée, `fetch_mode`, `MAILERS`, `on_delete` au niveau base…) sont présentées telles que décrites dans le plan fourni. Comme toute fonctionnalité récente, vérifiez le détail exact de l'API dans les notes de version officielles (docs.djangoproject.com) avant de l'employer en production.

---

## 1. Introduction à Django

### Objectifs d'apprentissage

À la fin de cette section, vous saurez : définir ce qu'est un framework web et situer Django parmi les autres ; décrire le cycle d'une requête HTTP dans Django ; expliquer le motif MTV et les principes de conception du framework ; choisir une version de Django adaptée à votre projet ; décider, argument à l'appui, si Django est le bon outil.

### 1.1 Rappels indispensables : le web et HTTP

Un site web repose sur un dialogue **client–serveur** :

1. Le **client** (navigateur, application mobile, script) envoie une **requête HTTP** à une adresse (**URL**).
2. Le **serveur** exécute du code, éventuellement interroge une **base de données**, puis renvoie une **réponse HTTP**.
3. Le client affiche ou exploite la réponse (page HTML, données JSON, image…).

Une requête HTTP comprend : une **méthode** (*verbe*), une **URL**, des **en-têtes** (*headers*), et parfois un **corps** (*body*).

| Méthode | Sens habituel | Propriétés |
| --- | --- | --- |
| `GET` | Lire une ressource | **Sûre** (ne modifie rien) et **idempotente** |
| `POST` | Créer / déclencher une action | Ni sûre ni idempotente |
| `PUT` | Remplacer entièrement une ressource | Idempotente |
| `PATCH` | Modifier partiellement | Pas nécessairement idempotente |
| `DELETE` | Supprimer | Idempotente |

> **Définition — idempotence.** Une opération est idempotente quand l'appliquer une fois ou dix fois produit le même état final. Cette notion reviendra pour les tâches en arrière-plan (section 23) et les webhooks (section 21).

La réponse comporte un **code de statut** : `2xx` succès (`200 OK`, `201 Created`, `204 No Content`), `3xx` redirection (`301`, `302`), `4xx` erreur du client (`400`, `401`, `403`, `404`), `5xx` erreur du serveur (`500`, `503`). HTTP est **sans état** (*stateless*) : le serveur ne « se souvient » pas de la requête précédente ; c'est pourquoi on a inventé les **cookies** et les **sessions** (section 12 et 13).

### 1.2 Qu'est-ce qu'un framework ?

Une **bibliothèque** est un ensemble de fonctions que *vous* appelez. Un **framework** impose une **structure** et c'est *lui* qui appelle votre code (principe d'**inversion de contrôle**, dit « principe d'Hollywood » : *ne nous appelez pas, nous vous appellerons*). Avec Django, vous ne démarrez pas le serveur à la main : vous écrivez des vues, des modèles, des routes, et Django les appelle au bon moment.

**Django** est un framework web Python **« tout inclus »** (*batteries included*), de haut niveau, qui vise un développement **rapide**, **sûr** et **propre**. Sa devise : *« le framework web pour perfectionnistes avec des échéances »*.

| Domaine | Ce que Django apporte nativement |
| --- | --- |
| **Données** | **ORM** (*Object-Relational Mapper*) : manipuler des tables SQL comme des objets Python ; **migrations** automatiques ; validation |
| **Administration** | Back-office complet **généré** à partir de vos modèles |
| **Routage et vues** | Association URL → code ; vues fonctions et classes |
| **Templates** | Langage de gabarits (DTL, *Django Template Language*) sécurisé |
| **Formulaires** | Génération, validation, nettoyage, protection CSRF |
| **Authentification** | Utilisateurs, groupes, permissions, sessions, mots de passe hachés |
| **Sécurité** | Protections contre XSS, CSRF, injection SQL, clickjacking ; HTTPS/HSTS ; CSP (6.0) |
| **Internationalisation** | Traduction, fuseaux horaires, formats régionaux |
| **Outils** | Serveur de développement, tests, commandes de gestion, cache, e-mail, signaux |
| **Asynchrone** | ASGI, vues et ORM asynchrones, framework de tâches (6.0) |

> **Définition — ORM.** Couche logicielle qui fait correspondre des **classes** à des **tables**, des **instances** à des **lignes**, des **attributs** à des **colonnes**. Vous écrivez `Article.objects.filter(statut="publie")` ; Django produit le `SELECT … WHERE statut = 'publie'` adapté à votre base (PostgreSQL, MySQL, SQLite…).

### 1.3 Histoire

| Année | Événement |
| --- | --- |
| 2003 | Créé par **Adrian Holovaty** et **Simon Willison** au journal *Lawrence Journal-World* (Kansas), pour produire des sites d'actualité sous contrainte de temps |
| 2005 | Publié en **open source** (licence BSD) ; nommé d'après le guitariste **Django Reinhardt** |
| 2008 | Création de la **Django Software Foundation** (DSF), qui porte la gouvernance |
| 2017 | Django **2.0** : Python 3 uniquement ; nouvelle syntaxe `path()` |
| 2019 | Django 3.0 : prise en charge d'**ASGI** |
| 2021–2023 | Django 4.0, puis **4.2 LTS** |
| 2024–2025 | Django 5.0 → **5.2 LTS** (avril 2025) |
| 2025–2026 | **Django 6.0** (décembre 2025), puis **6.1** (5 août 2026) |

Cette origine explique la philosophie : le framework est né d'un besoin **éditorial** (contenu, administration par des non-développeurs, délais courts). D'où l'admin intégrée et l'importance de l'ORM.

### 1.4 Versions, cycle de publication et support *(à jour)*

Django publie une version « feature » **environ tous les 8 mois** (numérotées `A.B`, ex. 6.1) ; des correctifs (`A.B.C`) paraissent régulièrement entre deux. Certaines versions sont **LTS** (*Long Term Support*) : support de **sécurité** d'au moins trois ans.

| Version | Sortie | Type | Fin du support | Python |
| --- | --- | --- | --- | --- |
| 4.2 | avril 2023 | LTS | terminé (avril 2026) | 3.8 – 3.12 |
| **5.2** | avril 2025 | **LTS** | **avril 2028** | 3.10 – 3.13 |
| 6.0 | déc. 2025 | Standard | 2027 | **3.12 – 3.14** |
| **6.1** | **5 août 2026** | Standard | fin 2027 | 3.12 – 3.14 |
| **6.2** | avril 2027 (prévue) | **LTS** | ≥ 3 ans après sa sortie | 3.12 – 3.14 |

**Politique de dépréciation.** Une fonctionnalité n'est pas supprimée brutalement : elle est d'abord **dépréciée** (avertissement `DeprecationWarning`) pendant au moins deux versions, puis retirée. Conséquence pratique : si votre projet ne produit **aucun avertissement** sur la version N, il fonctionnera sur N+1. D'où l'intérêt de lancer les tests avec `-W error::DeprecationWarning` (voir section 30).

**Que choisir ?**

- **Nouveau projet** : la dernière version stable (6.1).
- **Production à très long terme, équipe réduite** : la **LTS** (5.2, puis 6.2 quand elle sortira).
- **Dans tous les cas** : appliquer *sans délai* les versions de correctifs de sécurité (ex. 6.1.2 du 6 octobre 2026 citée dans le plan).

### 1.5 Le motif MTV

Django suit le motif **MTV** (**M**odèle – **T**emplate – **V**ue), variante du célèbre MVC.

| Django | Équivalent MVC | Rôle |
| --- | --- | --- |
| **Modèle** (*Model*) | Modèle | Structure des données et accès à la base |
| **Template** | Vue | Présentation (HTML) |
| **Vue** (*View*) | Contrôleur | Logique : reçoit la requête, prépare les données, renvoie la réponse |
| **URLconf** | Routage | Associe une URL à une vue |

> **Attention au vocabulaire.** Ce que Django appelle « vue » correspond au **contrôleur** du MVC. Le « contrôleur » de Django, c'est en réalité le framework lui-même (routage, middleware) ; le **template** joue le rôle de la « vue » MVC.

```text
Requête HTTP
   │
   v
Middleware ──> URLconf (urls.py) ──> Vue (views.py) ──> Modèle (ORM) ──> Base de données
                                          │
                                          v
                                  Template (HTML) ──> Réponse HTTP ──> Middleware ──> Navigateur
```

**Déroulé détaillé d'une requête :**

1. Le serveur d'application (Gunicorn, Uvicorn…) reçoit la requête et construit un objet **`HttpRequest`**.
2. La requête traverse la pile de **middlewares** « en descendant » (sécurité, session, authentification…).
3. Django consulte l'**URLconf** et trouve la **vue** correspondante.
4. La vue interroge éventuellement les **modèles** (donc la base), puis choisit un **template** et un **contexte**.
5. Le template est **rendu** en HTML ; la vue renvoie un **`HttpResponse`**.
6. La réponse remonte la pile de middlewares « en remontant », puis est envoyée au client.

### 1.6 Principes de conception

- **DRY** (*Don't Repeat Yourself*) : chaque connaissance a une représentation unique. Exemple : le modèle décrit une fois les champs ; formulaire, admin et migration en dérivent.
- **Couplage faible** : les composants ne dépendent pas fortement les uns des autres (le template ne connaît pas la base, l'ORM ne connaît pas HTTP).
- **Explicite plutôt qu'implicite** (hérité de la philosophie de Python) : peu de « magie » cachée.
- **Convention plutôt que configuration** : arborescence et noms standardisés (`models.py`, `urls.py`, `templates/`), pour qu'un développeur s'oriente vite dans un projet inconnu.
- **Sécurité par défaut** : l'échappement HTML, le CSRF, les requêtes paramétrées sont actifs sans effort.
- **Applications réutilisables** : un **projet** est une collection d'**applications** (*apps*) faiblement couplées.

### 1.7 Django face aux autres frameworks

|  | **Django** | **Flask** | **FastAPI** | **Laravel** (PHP) | **Rails** (Ruby) |
| --- | --- | --- | --- | --- | --- |
| Philosophie | Tout inclus | Micro-framework | API asynchrone + types | Tout inclus | Tout inclus |
| ORM / admin intégrés | Oui / Oui | Non (extensions) | Non | Oui / Non | Oui / Non |
| Idéal pour | Sites complets, back-offices, API (+ DRF/Ninja) | Petits services, prototypes | **API** performantes, validation | Sites PHP | Sites Ruby |
| Courbe d'apprentissage | Moyenne | Faible | Faible à moyenne | Moyenne | Moyenne |

**Quand choisir Django ?** Applications avec **base de données**, **administration**, **authentification**, **contenu** ; équipes qui veulent une **structure éprouvée** et une **sécurité solide**. Il est utilisé par Instagram, Pinterest, Mozilla, Disqus, la NASA…

**Quand hésiter ?** Un micro-service minuscule sans base de données (Flask ou FastAPI suffisent) ; une API purement asynchrone à très haute concurrence (FastAPI est plus naturel, même si Django Ninja et l'async de Django réduisent l'écart) ; un besoin de très grande liberté d'architecture où l'on refuse les conventions.

### 1.8 Premier contact : « Bonjour » en trois fichiers

```python
# blog/views.py
from django.http import HttpRequest, HttpResponse

def bonjour(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Bonjour, monde !")
```

```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [path("bonjour/", views.bonjour, name="bonjour")]
```

```python
# config/urls.py
from django.urls import include, path

urlpatterns = [path("blog/", include("blog.urls"))]
```

En visitant `/blog/bonjour/`, le middleware laisse passer, l'URLconf racine délègue à `blog.urls`, la vue renvoie le texte : vous venez de parcourir tout le cycle décrit en 1.5.

### À retenir

- Django est un framework **tout inclus**, structuré en **MTV**, qui privilégie **DRY**, la **convention** et la **sécurité par défaut**.
- Une requête traverse : serveur → middlewares → URLconf → vue → (modèle, template) → réponse.
- Choisissez la **dernière version stable** pour un nouveau projet, la **LTS** pour la stabilité, et appliquez toujours les correctifs de sécurité.

---

## 2. Environnement de développement et outillage des éditeurs

### Objectifs d'apprentissage

Mettre en place un environnement isolé et reproductible ; installer Django ; créer un projet et une application ; maîtriser les commandes `manage.py` ; configurer l'éditeur (VS Code, PyCharm, Vim/Neovim) avec **stubs de types**, **linter** et **formateur** ; utiliser les outils de débogage.

### 2.1 Prérequis

- **Python** compatible avec votre version de Django (3.12 ou plus pour Django 6.x ; voir le tableau de la section 1.4). Vérifiez : `python --version`.
- **PostgreSQL** pour la production (SQLite, livré avec Python, suffit pour apprendre).
- **Git** (gestion de versions) et un éditeur de code.

### 2.2 Environnement virtuel et installation *(à jour)*

> **Définition — environnement virtuel.** Dossier contenant un interpréteur Python et un jeu de paquets **propres à un projet**. Il évite que deux projets s'écrasent mutuellement leurs dépendances (le projet A veut Django 5.2, le projet B veut 6.1) et rend l'installation **reproductible**.

**Avec `uv` (moderne, très rapide)** :

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh      # installer uv (ou : pip install uv)
uv init mon-site && cd mon-site
uv add django                                        # ajoute Django à pyproject.toml et crée .venv
uv run django-admin startproject config .
uv run python manage.py runserver
```

`uv add` modifie `pyproject.toml` (la liste des dépendances **souhaitées**) et génère `uv.lock` (les versions **exactes** résolues). `uv run` exécute une commande dans l'environnement du projet sans l'activer manuellement.

**Avec `venv` + `pip` (classique)** :

```bash
python -m venv .venv
source .venv/bin/activate              # Linux/macOS
.venv\Scripts\activate                 # Windows
pip install "django>=6.1,<6.2"
pip freeze > requirements.txt          # ou mieux : pyproject.toml + fichier de verrouillage
django-admin --version
```

**Bonnes pratiques** : épinglez vos dépendances (fichier de verrouillage `uv.lock`, `poetry.lock` ou `requirements.txt` généré) ; **ne versionnez jamais** `.venv/` (ajoutez-le à `.gitignore`) ; documentez la commande d'installation dans le `README`.

### 2.3 Créer un projet et une application

```bash
django-admin startproject config .            # le « . » crée le projet dans le dossier courant
python manage.py startapp blog                # une application
python manage.py runserver                    # http://127.0.0.1:8000
```

- `django-admin` : outil global d'administration (créer des projets).
- `manage.py` : **enveloppe locale** du projet qui positionne automatiquement la variable `DJANGO_SETTINGS_MODULE` ; c'est elle que vous utiliserez au quotidien.

Enregistrez ensuite l'application dans la configuration :

```python
# config/settings.py
INSTALLED_APPS = [
    "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes",
    "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles",
    "blog",                                    # ← l'application (ou "blog.apps.BlogConfig")
]
```

```bash
python manage.py migrate                      # crée les tables de base (auth, sessions, admin…)
python manage.py createsuperuser              # compte administrateur
python manage.py check                        # vérifie la configuration
```

### Commandes `manage.py` essentielles

| Commande | Rôle |
| --- | --- |
| `runserver [port]` | Serveur de développement avec **rechargement automatique** (ne jamais l'utiliser en production) |
| `makemigrations` / `migrate` | Créer / appliquer les migrations de schéma |
| `createsuperuser`, `changepassword` | Gestion des comptes |
| `shell` | Console Python avec Django chargé (**importe automatiquement les modèles** depuis 5.2) |
| `startapp`, `startproject` | Générer des squelettes |
| `collectstatic` | Rassembler les fichiers statiques pour la production |
| `test` | Lancer les tests |
| `check [--deploy]` | Contrôles système (et contrôles spécifiques au déploiement) |
| `dumpdata` / `loaddata` | Exporter / importer des **fixtures** (données sérialisées) |
| `makemessages` / `compilemessages` | Traductions (section 17) |
| `dbshell`, `sqlmigrate`, `showmigrations`, `inspectdb`, `flush` | Base de données |

### 2.4 Outillage des éditeurs : stubs de types et analyse *(ajout)*

**Le problème.** Django repose beaucoup sur la **métaprogrammation** : les champs de modèle deviennent des attributs d'instance, `objects` est ajouté dynamiquement, les relations inverses (`article.commentaires`) sont créées à l'exécution, `request.user` est ajouté par un middleware. Sans aide, les éditeurs et les vérificateurs de types **ne comprennent pas** `Article.objects.filter(...)`, `article.auteur` ou `request.user` : pas de complétion, faux positifs.

**La solution.** Installer des **stubs de types** (fichiers décrivant les types de Django) et, pour mypy, un **plugin** qui comprend l'ORM ; puis configurer l'éditeur pour qu'il utilise **l'interpréteur du venv du projet**.

```bash
uv add --dev django-stubs[compatible-mypy] djangorestframework-stubs mypy
uv add --dev ruff django-debug-toolbar django-extensions ipython pytest-django
uv add --dev djlint                  # linter/formateur de templates Django
uv add --dev pyright                 # (optionnel) ou basedpyright
uv add --dev django-types            # (optionnel) alternative aux stubs pour pyright / Pylance
```

| Paquet | Rôle |
| --- | --- |
| **`django-stubs`** (+ extra `compatible-mypy`) | Stubs de types de Django et **plugin mypy** (comprend l'ORM, `settings`, `request.user`) |
| **`djangorestframework-stubs`** | Stubs et plugin mypy pour DRF |
| **`mypy`** | Vérificateur de types qui charge les plugins |
| **`pyright`** / **`basedpyright`** + **`django-types`** | Alternative compatible **Pylance (VS Code)** et les clients **LSP** de Vim/Neovim |
| **`ruff`** | Linter **et** formateur ultra-rapide ; règles `DJ` (bonnes pratiques Django) ; remplace flake8, isort, black |
| **`djlint`** | Formatage et analyse des templates `.html` Django |
| **`django-extensions`** | `shell_plus`, `runserver_plus`, `graph_models`, `show_urls` |
| **`django-debug-toolbar`** | Barre de débogage : requêtes SQL, templates, cache |
| **`pre-commit`** | Exécute ruff, mypy, djlint avant chaque commit |

**Configuration de mypy avec `django-stubs`** :

```toml
# pyproject.toml
[tool.mypy]
python_version = "3.13"
strict = true
plugins = ["mypy_django_plugin.main", "mypy_drf_plugin.main"]

[tool.django-stubs]
django_settings_module = "config.settings"   # obligatoire : chemin Python vers settings
```

```bash
mypy .                                       # vérification des types
```

**Annoter son code** : le plugin déduit déjà beaucoup de choses ; les annotations explicites aident le reste.

```python
# apps/blog/models.py
from django.conf import settings
from django.db import models
from django.http import HttpRequest, HttpResponse

class Article(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")

    objects: models.Manager["Article"]       # précise le gestionnaire pour certains outils

def accueil(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Bienvenue")
```

**Pyright / Pylance** :

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

#### Vim / Neovim *(ajout)*

Vim ne « comprend » pas Django seul : il faut un **client LSP** (*Language Server Protocol* : protocole qui permet à un éditeur de dialoguer avec un « serveur de langage » fournissant complétion, diagnostics, navigation) et des serveurs installés **dans votre environnement**.

| Besoin | Outil | Remarque |
| --- | --- | --- |
| Complétion / types Python | **Pyright** (`pyright-langserver`), **basedpyright**, ou **Pylsp** + `pylsp-mypy` | Installer `django-stubs` / `django-types` dans le **même venv** |
| Lint et formatage | **`ruff server`** (LSP intégré à ruff) | Remplace `ruff-lsp` |
| Templates Django | **`djlsp`** (*django-template-lsp*) + **`djlint`** | Complétion de balises, filtres, `{% url %}`, `{% static %}` |
| Détection de type de fichier | Associer les `*.html` des templates à `htmldjango` | Voir ci-dessous |
| Plugins | `nvim-lspconfig`, `mason.nvim`, `nvim-cmp`, `conform.nvim`, `nvim-lint` | Neovim ; clients LSP : **coc.nvim**, **vim-lsp**, **ALE** pour Vim |

```lua
-- Neovim (nvim-lspconfig) : exemple minimal
local lsp = require("lspconfig")
lsp.pyright.setup({
    settings = { python = { analysis = { typeCheckingMode = "standard", autoSearchPaths = true, useLibraryCodeForTypes = true } } },
})
lsp.ruff.setup({})                                   -- ruff server (lint + format)
lsp.djlsp.setup({ init_options = { django_settings_module = "config.settings" } })

vim.filetype.add({ pattern = { [".*/templates/.*%.html"] = "htmldjango" } })
```

```vim
" Vim classique (~/.vimrc)
autocmd BufRead,BufNewFile */templates/*.html set filetype=htmldjango
```

> **Trois pièges fréquents.** (1) L'éditeur doit utiliser l'**interpréteur du venv** du projet, sinon les stubs sont introuvables. (2) `DJANGO_SETTINGS_MODULE` doit être renseigné (pour `djlsp`, `django-stubs`, `pytest-django`). (3) Lancez le serveur LSP **depuis la racine du projet** (là où se trouvent `manage.py` et `pyproject.toml`).

#### VS Code et PyCharm

- **VS Code** : extensions *Python*, *Pylance*, *Ruff*, une extension *Django* pour la coloration des templates, *djLint*. Réglages utiles :

```json
{ "python.defaultInterpreterPath": ".venv/bin/python",
  "files.associations": { "**/templates/**/*.html": "django-html" },
  "[django-html]": { "editor.defaultFormatter": "monosans.djlint" },
  "[python]": { "editor.defaultFormatter": "charliermarsh.ruff" } }
```

- **PyCharm Professional** : support Django intégré (templates, ORM, console, débogueur, `manage.py`). L'édition Community nécessite les stubs.

#### Configuration de Ruff

```toml
# pyproject.toml
[tool.ruff]
target-version = "py313"
line-length = 100
extend-exclude = ["migrations"]

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP", "DJ", "S", "C4", "SIM"]   # DJ = flake8-django ; S = bandit (sécurité)
ignore = ["S101"]                                             # assert autorisé (tests)
```

- `E`/`F` : erreurs de style et erreurs logiques ; `I` : tri des imports ; `B` : pièges courants ; `UP` : modernisation de la syntaxe ; `DJ` : règles Django ; `S` : sécurité ; `C4`, `SIM` : simplifications.

#### Hooks `pre-commit`

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

**`django-upgrade`** réécrit automatiquement votre code vers les API récentes de Django (utile à chaque montée de version, section 30).

### 2.5 Outils de débogage

```python
# config/urls.py (à la suite de urlpatterns)
from django.conf import settings
from django.urls import include, path

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
```

(N'oubliez pas d'ajouter `"debug_toolbar"` à `INSTALLED_APPS`, son middleware, et `INTERNAL_IPS = ["127.0.0.1"]`.)

```bash
python manage.py shell_plus --print-sql          # shell avec tous les modèles et affichage du SQL
python manage.py show_urls                       # toutes les routes
python manage.py graph_models -a -o modeles.png  # diagramme des modèles
python -m pdb manage.py runserver --noreload     # débogueur ; ou breakpoint() dans le code
```

- `breakpoint()` ouvre le débogueur `pdb` à l'endroit voulu (commandes : `n` suivant, `s` entrer, `c` continuer, `p expr` afficher, `q` quitter).
- `--noreload` évite que le rechargeur automatique ne lance deux processus pendant le débogage.

### 2.6 Modèles de projet

| Outil | Apport |
| --- | --- |
| **`cookiecutter-django`** | Gabarit **complet pour la production** (Docker, Celery, DRF, Sentry, tests, CI) |
| `django-admin startproject --template` | Votre propre gabarit |
| **`copier`**, **`django-startproject`** | Gabarits pouvant être mis à jour de façon incrémentale |

### À retenir

- **Un environnement virtuel par projet**, dépendances **verrouillées**, `.venv/` jamais versionné.
- `manage.py` est votre porte d'entrée quotidienne ; apprenez `makemigrations`, `migrate`, `shell`, `test`, `check --deploy`.
- Un éditeur bien configuré (stubs + ruff + djlint + interpréteur du venv) fait gagner un temps considérable.

---

## 3. Structure d'un projet et d'applications

### Objectifs d'apprentissage

Distinguer **projet** et **application** ; lire l'arborescence générée par Django et connaître le rôle de chaque fichier ; configurer une classe `AppConfig` ; organiser un projet réel (réglages multiples, dossier `apps/`, services) ; comprendre pourquoi il faut un **modèle utilisateur personnalisé** dès le départ.

### 3.1 Projet ≠ application

|  | **Projet** | **Application** (*app*) |
| --- | --- | --- |
| Définition | Ensemble de la configuration et des apps qui forment un site | **Module Python** qui fait **une seule chose** (blog, comptes, paiement) |
| Nombre | 1 par site | **Plusieurs**, réutilisables d'un projet à l'autre |
| Contient | `settings.py`, `urls.py`, `wsgi.py`, `asgi.py` | `models.py`, `views.py`, `urls.py`, `admin.py`, `tests`, `migrations/`… |

> **Définition — application Django.** Un paquet Python, enregistré dans `INSTALLED_APPS`, qui regroupe des modèles, des vues, des templates, des fichiers statiques, des migrations, etc. autour d'une **responsabilité unique**. Django charge les apps au démarrage (registre d'applications) pour découvrir leurs modèles, leurs templates, leurs commandes de gestion et leurs traductions.

Un **critère simple pour découper** : si vous pouvez décrire l'app en une phrase sans utiliser le mot « et », elle est bien dimensionnée (« gère les articles et les commentaires » : acceptable ; « gère les articles, les paiements et les e-mails » : à découper).

### 3.2 Arborescence générée

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

Le nom `config` pour le paquet du projet (au lieu du nom du site) évite la confusion classique « dossier `mon-site/mon-site/` » et se répète d'un projet à l'autre.

### 3.3 Rôle des fichiers du projet

| Fichier | Rôle |
| --- | --- |
| `manage.py` | Exécute les commandes (`python manage.py <commande>`) ; définit `DJANGO_SETTINGS_MODULE` |
| `settings.py` | Configuration : applications, base, middleware, templates, sécurité… |
| `urls.py` | Routage racine (`urlpatterns`) |
| `wsgi.py` | Interface **WSGI** (Gunicorn, uWSGI) : expose l'objet `application` |
| `asgi.py` | Interface **ASGI** (Uvicorn, Daphne, Hypercorn) : expose `application` |
| `__init__.py` | Marque un dossier comme **paquet** Python ; sert aussi à initialiser (ex. Celery, section 23) |

> **Définition — WSGI / ASGI.** Interfaces standard entre un serveur d'application et un framework Python. **WSGI** est synchrone (une requête occupe un thread/processus) ; **ASGI** est asynchrone et gère aussi WebSockets et SSE (section 22).

### 3.4 La classe `AppConfig`

Chaque application possède une classe de configuration, utilisée au démarrage.

```python
# blog/apps.py
from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"   # type des clés primaires automatiques
    name = "blog"                                           # chemin Python complet du paquet
    verbose_name = "Blog"                                   # nom lisible (admin)

    def ready(self) -> None:                                # exécuté UNE fois au démarrage, apps toutes chargées
        from . import signals  # noqa: F401  (section 16)
```

- **`name`** doit être le chemin Python complet (`"apps.blog"` si l'app vit dans `apps/`).
- **`ready()`** sert à brancher les **signaux** et à enregistrer des vérifications. Ne faites **ni requête de base de données ni travail lourd** dans `ready()` : il s'exécute aussi pour `migrate`, `collectstatic`, etc.
- Depuis Django **6.0**, `BigAutoField` est le type **par défaut** des clés automatiques (aucune configuration nécessaire pour les nouveaux projets).

### 3.5 Organisation recommandée pour un projet réel *(à jour)*

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

**Règles d'organisation :**

- **Une app = une responsabilité** ; noms **courts**, au pluriel ou métier (`comptes`, `commandes`).
- Enregistrez-les avec `"apps.blog"` et mettez `name = "apps.blog"` dans `AppConfig`.
- **Réglages scindés** : `base.py` contient l'essentiel ; `dev.py`, `prod.py`, `test.py` font `from .base import *` puis surchargent. On choisit via `DJANGO_SETTINGS_MODULE=config.settings.prod`.
- Mettez la **logique métier** dans des **services** (`services.py`) ou dans les modèles/gestionnaires, **pas dans les vues** : les vues restent minces et testables (voir sections 6 et 8).
- Templates **globaux** (page de base, erreurs) dans `templates/` ; templates **propres à une app** dans `apps/<app>/templates/<app>/` (l'espace de noms évite les collisions de noms entre apps).

```python
# apps/blog/services.py : exemple de service (logique métier hors des vues)
from django.db import transaction
from .models import Article

@transaction.atomic
def publier_article(article: Article) -> Article:
    article.publier()                    # méthode du modèle (section 8.7)
    return article
```

### 3.6 Un modèle utilisateur personnalisé dès le départ

> **Règle d'or : faites-le avant la **première** migration.** Remplacer le modèle utilisateur en cours de projet oblige à réécrire les clés étrangères, les migrations et les données : c'est très pénible. Créer un modèle *vide* au début ne coûte presque rien.

```python
# apps/comptes/models.py
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    pass                      # ajoutez ensuite vos champs (avatar, téléphone…)

# settings.py
AUTH_USER_MODEL = "comptes.Utilisateur"
```

Les détails (connexion par e-mail, profil, bonnes pratiques) sont dans la section 12.

### 3.7 Pièges fréquents

| Piège | Conséquence | Remède |
| --- | --- | --- |
| Application oubliée dans `INSTALLED_APPS` | Modèles ignorés, templates introuvables | L'enregistrer |
| Une seule « super-app » | Code impossible à réutiliser et à tester | Découper par responsabilité |
| `import` circulaires entre apps | `ImportError` au démarrage | Référencer les modèles par chaîne (`"blog.Article"`), utiliser `apps.get_model` |
| Travail dans `ready()` | Démarrage lent, erreurs en `migrate` | Limiter à l'enregistrement de signaux |
| `.env` versionné | Fuite de secrets | `.gitignore` + `.env.example` |

### À retenir

- **Projet** = configuration ; **app** = fonctionnalité réutilisable. Une app, une responsabilité.
- Scindez les réglages (`base`/`dev`/`prod`/`test`) et gardez les vues minces.
- **Modèle utilisateur personnalisé avant la première migration.**

---

## 4. Configuration (`settings.py`)

### Objectifs d'apprentissage

Comprendre ce qu'est un *réglage* et comment Django le charge ; maîtriser les réglages essentiels (sécurité, base de données, templates, statiques, cache, e-mail, journalisation) ; externaliser les secrets dans des **variables d'environnement** ; définir ses propres réglages.

### 4.1 Principe

La configuration est un **module Python** (`config/settings.py`) dont les noms **en MAJUSCULES** sont lus par Django. Le module à utiliser est indiqué par la variable d'environnement **`DJANGO_SETTINGS_MODULE`** (renseignée par `manage.py`). On y accède dans le code via `django.conf.settings`, jamais par import direct du module.

```python
# config/settings/base.py
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(BASE_DIR / ".env")          # django-environ : lit le fichier .env

SECRET_KEY = env("SECRET_KEY")                   # jamais dans le code ni dans Git
DEBUG = env("DEBUG")                             # False en production !
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

LANGUAGE_CODE = "fr"
TIME_ZONE = "Europe/Paris"
USE_I18N = True
USE_TZ = True                                    # datetimes en UTC en base, convertis à l'affichage
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
```

| Réglage | Rôle |
| --- | --- |
| `SECRET_KEY` | Signature des sessions, jetons, liens de réinitialisation : **secrète et unique** par environnement |
| `DEBUG` | Pages d'erreur détaillées : **`False` en production** (sinon fuite d'informations : code, variables, réglages) |
| `ALLOWED_HOSTS` | Noms d'hôte autorisés (obligatoire quand `DEBUG = False`) : protection contre les attaques par en-tête `Host` |
| `ROOT_URLCONF` | Module des routes racine |
| `USE_TZ` | Datetimes **aware** (avec fuseau) ; recommandé et `True` par défaut depuis Django 5.0 |

> **Définition — datetime « aware ».** Date-heure qui connaît son fuseau horaire, par opposition à *naive* (sans fuseau). Stockez en UTC, affichez dans le fuseau de l'utilisateur (section 17.6).

### 4.2 Applications installées et middleware

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
    "whitenoise.middleware.WhiteNoiseMiddleware",             # statiques en production (juste après Security)
    "corsheaders.middleware.CorsMiddleware",                  # CORS (avant CommonMiddleware)
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.csp.ContentSecurityPolicyMiddleware",  # (6.0) en-tête CSP
    "django_htmx.middleware.HtmxMiddleware",
]
```

- **`INSTALLED_APPS`** : l'ordre compte pour la résolution des templates et des fichiers statiques (la première app qui fournit un fichier gagne), et pour les surcharges (placez vos apps avant celles que vous souhaitez surcharger).
- **`MIDDLEWARE`** : **l'ordre compte** (descente à la requête, remontée à la réponse ; section 15). `LoginRequiredMiddleware` (5.1), qui rend toutes les vues privées par défaut, n'est pas activé ici (section 12.4).

### 4.3 Base de données

```python
import dj_database_url

# Variante 1 : à partir de DATABASE_URL
DATABASES = {
    "default": dj_database_url.config(default=env("DATABASE_URL"), conn_max_age=600, conn_health_checks=True),
}
# Variante 2 : configuration explicite (à utiliser à la place de la variante 1)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"), "USER": env("DB_USER"), "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST", default="localhost"), "PORT": "5432",
        "CONN_MAX_AGE": 0,                     # avec un pool, laisser à 0
        "OPTIONS": {"pool": True},             # (5.1) pool de connexions psycopg 3
    }
}
```

| Base | Moteur | Pilote |
| --- | --- | --- |
| **PostgreSQL** (recommandée) | `django.db.backends.postgresql` | **`psycopg[binary,pool]`** (psycopg **3**) |
| MySQL / MariaDB | `django.db.backends.mysql` | `mysqlclient` |
| SQLite | `django.db.backends.sqlite3` | intégré (développement, petits sites) |
| Oracle | `django.db.backends.oracle` | `oracledb` |
| SQL Server | `mssql-django` | `mssql-django` |

- **`CONN_MAX_AGE`** : durée (secondes) pendant laquelle une connexion est réutilisée entre requêtes ; `0` = fermer après chaque requête (comportement historique). **Un pool** (`"pool": True`) gère les connexions de façon plus fine : ne cumulez pas les deux.
- **PostgreSQL** est le choix de production : types riches (JSONB, tableaux), recherche plein texte, index avancés, `django.contrib.postgres`.

### 4.4 Templates, fichiers statiques, médias, stockage

```python
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"],              # dossiers de templates globaux
    "APP_DIRS": True,                             # cherche aussi dans <app>/templates/
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.request",
        "django.template.context_processors.csp",   # (6.0) expose csp_nonce
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"            # cible de collectstatic (production)
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

STORAGES = {                                       # (4.2+) remplace DEFAULT_FILE_STORAGE / STATICFILES_STORAGE
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}
```

Un **processeur de contexte** (*context processor*) est une fonction qui ajoute des variables à tous les templates (section 7.6). Le réglage `STORAGES` décrit où et comment sont stockés les fichiers : « default » pour les médias, « staticfiles » pour les statiques (section 14).

### 4.5 Cache, e-mail, journalisation

```python
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",   # intégré depuis Django 4.0
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

> **Django 6.1** introduit le réglage **`MAILERS`** (plusieurs « expéditeurs » nommés, chacun avec son backend et ses options) qui **remplace** `EMAIL_BACKEND`, `EMAIL_HOST`… ; les anciens réglages **fonctionnent jusqu'à Django 7.0**. Consultez la page officielle *Migrating email to mailers*. Pour un service d'envoi (Mailgun, SES, Brevo…), utilisez **`django-anymail`**.

Le **backend console** affiche les e-mails dans le terminal : idéal en développement, aucun serveur SMTP requis.

```python
LOGGING = {
    "version": 1, "disable_existing_loggers": False,
    "formatters": {"simple": {"format": "{asctime} {levelname} {name} {message}", "style": "{"}},
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {"django.request": {"handlers": ["console"], "level": "WARNING", "propagate": False}},
}
```

La journalisation de Django repose sur le module standard `logging` : un **logger** émet des messages, un **handler** les envoie quelque part, un **formatter** les met en forme. En conteneur ou PaaS, journalisez **sur la sortie standard** : la plateforme les collecte.

### 4.6 Sécurité (aperçu ; détails en section 26)

```python
# config/settings/prod.py
from .base import *

DEBUG = False
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")   # derrière un proxy (Nginx, load balancer)
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ["https://exemple.fr"]                   # schéma obligatoire
SECURE_CONTENT_TYPE_NOSNIFF = True
```

- **HSTS** (*HTTP Strict Transport Security*) indique au navigateur de ne contacter le site qu'en HTTPS pendant la durée donnée.
- **`SECURE_PROXY_SSL_HEADER`** : à n'activer que si votre proxy **écrase** cet en-tête ; sinon un client pourrait le falsifier.

### 4.7 Variables d'environnement et réglages multiples

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

`check --deploy` signale les réglages dangereux pour la production (HTTPS, cookies, HSTS, `DEBUG`…). Principe des *douze facteurs* : la configuration qui varie entre environnements vit **dans l'environnement**, pas dans le code.

### 4.8 Réglages personnalisés

```python
# settings.py
ARTICLES_PAR_PAGE = env.int("ARTICLES_PAR_PAGE", default=10)

# Utilisation (par exemple dans python manage.py shell)
from django.conf import settings
print(settings.ARTICLES_PAR_PAGE)        # 10 (valeur par défaut)
```

Préfixez vos réglages par le nom de l'app si vous publiez un paquet réutilisable (`BLOG_ARTICLES_PAR_PAGE`) pour éviter les collisions.

### 4.9 Réglages de bibliothèques tierces

Chaque bibliothèque a son dictionnaire ou son préfixe : `REST_FRAMEWORK`, `SIMPLE_JWT`, `CELERY_*`, `CORS_ALLOWED_ORIGINS`, `SPECTACULAR_SETTINGS`… Ils sont détaillés dans les sections concernées (19, 20, 23).

### Pièges fréquents

| Piège | Remède |
| --- | --- |
| `DEBUG = True` en production | Lire `DEBUG` depuis l'environnement, défaut `False` |
| `ALLOWED_HOSTS = ["*"]` | Lister les domaines réels |
| `SECRET_KEY` committée | La changer immédiatement (elle est compromise), utiliser l'environnement |
| Importer `settings.py` directement | Toujours `from django.conf import settings` |
| Mélanger `CONN_MAX_AGE` et pool | Choisir l'un ou l'autre |

### À retenir

- La configuration est du Python ; ce qui varie selon l'environnement vient de **variables d'environnement**.
- `DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS`, HTTPS/cookies/HSTS sont les réglages à ne jamais négliger ; `check --deploy` les vérifie.
- Préférez PostgreSQL, Redis pour le cache, et `STORAGES` pour fichiers statiques et médias.

---

## 5. URLs et routage

### Objectifs d'apprentissage

Expliquer comment Django associe une URL à une vue ; écrire des `URLconf` modulaires avec `path()`, `include()` et espaces de noms ; utiliser les convertisseurs (intégrés et personnalisés) et `re_path` ; **nommer** et **inverser** les URL ; gérer redirections, pages d'erreur, fichiers médias en développement, URL internationalisées et routes d'API ; diagnostiquer un problème de routage.

### 5.1 Principe

Django associe chaque **URL** à une **vue** grâce à des **URLconfs** (fichiers `urls.py`). Il parcourt la liste `urlpatterns` **dans l'ordre** et retient la **première** correspondance ; si aucune ne convient, il renvoie une erreur 404. Seul le **chemin** compte : le nom de domaine, la chaîne de requête (`?a=1`) et la méthode HTTP ne participent pas à la recherche.

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

`include()` **retire** le préfixe déjà reconnu et transmet le reste à l'URLconf de l'app : l'app ne connaît pas son point de montage, ce qui la rend réutilisable (**couplage faible**).

```python
# apps/blog/urls.py
from django.urls import path
from . import views

app_name = "blog"                                    # espace de noms : blog:detail

urlpatterns = [
    path("", views.ListeArticles.as_view(), name="liste"),
    path("nouveau/", views.CreerArticle.as_view(), name="creer"),
    path("<int:pk>/", views.DetailArticle.as_view(), name="detail"),
    path("archives/<int:annee>/<int:mois>/", views.archives, name="archives"),
    path("<slug:slug>/", views.detail_par_slug, name="detail-slug"),   # motif générique : en dernier
]
```

```python
# apps/accueil/urls.py
from django.urls import path
from .views import Accueil, ExportCsv

urlpatterns = [
    path("", Accueil.as_view(), name="accueil"),
    path("export.csv", ExportCsv.as_view(), name="export-csv"),
]
```

- **`app_name`** définit un **espace de noms** : deux apps peuvent avoir chacune une route nommée `detail` sans conflit (`blog:detail`, `boutique:detail`).
- **L'ordre compte** : placez les motifs **les plus spécifiques d'abord** (`nouveau/` avant `<slug:slug>/`, sinon `nouveau` serait pris pour un slug).
- Une **vue basée sur une classe** se branche toujours avec `.as_view()`.

### 5.2 Convertisseurs de chemin

Les parties entre chevrons `<convertisseur:nom>` capturent un segment de l'URL et le transmettent à la vue **comme argument nommé**, déjà converti en type Python.

| Convertisseur | Reconnaît | Type Python |
| --- | --- | --- |
| `str` (défaut) | Chaîne non vide **sans** `/` | `str` |
| `int` | Entier ≥ 0 | `int` |
| `slug` | Lettres, chiffres, `-`, `_` | `str` |
| `uuid` | UUID formaté | `uuid.UUID` |
| `path` | Chaîne **avec** `/` | `str` |

```python
# apps/blog/urls.py (extrait)
from django.http import HttpResponse
from django.urls import path
from . import views

def fichier(request, chemin: str) -> HttpResponse:
    return HttpResponse(f"Fichier demandé : {chemin}")

urlpatterns = [
    path("articles/<int:pk>/", views.detail_article),      # /articles/42/ → detail_article(request, pk=42)
    path("fichiers/<path:chemin>", fichier),               # /fichiers/a/b/c.txt → "a/b/c.txt"
]
```

> `<int:pk>` ne reconnaît que les entiers positifs : `/articles/abc/` donne directement une 404 sans que votre vue ne s'exécute.

#### Convertisseur personnalisé

Un convertisseur est une classe avec un attribut `regex` et deux méthodes : `to_python` (URL → Python) et `to_url` (Python → URL, pour l'inversion).

```python
# apps/blog/converters.py
class AnneeQuatreChiffres:
    regex = r"[0-9]{4}"

    def to_python(self, valeur: str) -> int:
        return int(valeur)

    def to_url(self, valeur: int) -> str:
        return f"{valeur:04d}"
```

```python
# apps/blog/urls.py
from django.urls import path, register_converter
from . import views
from .converters import AnneeQuatreChiffres

register_converter(AnneeQuatreChiffres, "annee")

urlpatterns = [
    path("archives/<annee:annee>/", views.archives, name="archives-annee"),
]
```

#### Expressions régulières : `re_path`

```python
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^articles/(?P<annee>[0-9]{4})/$", views.archives),   # pour les cas complexes seulement
]
```

Préférez `path()` : plus lisible, plus sûr. Réservez `re_path` aux motifs impossibles à exprimer autrement.

### 5.3 Noms d'URL et inversion

> **Règle : ne codez jamais une URL en dur.** Nommez la route (`name=`) et **inversez-la**. Si l'URL change, tout le site se met à jour sans modification.

```python
# python manage.py shell
from django.urls import reverse

print(reverse("blog:detail", kwargs={"pk": 42}))   # /blog/42/
print(reverse("blog:liste"))                      # /blog/
```

```django
<a href="{% url 'blog:detail' pk=article.pk %}">{{ article.titre }}</a>
```

```python
# apps/blog/models.py : URL canonique
from django.db import models
from django.urls import reverse

class Article(models.Model):
    def get_absolute_url(self) -> str:
        return reverse("blog:detail", kwargs={"pk": self.pk})
```

`get_absolute_url()` est une convention reconnue par l'admin (bouton « voir sur le site »), par `redirect(objet)` et par les sitemaps. Dans le code chargé à l'import (attributs de classe, `success_url`), utilisez **`reverse_lazy`** : l'inversion est alors différée jusqu'à l'utilisation.

### 5.4 Redirections et raccourcis

```python
# apps/blog/views.py
from django.shortcuts import get_object_or_404, redirect
from .models import Article

def vers_liste(request):
    return redirect("blog:liste")                   # par nom d'URL

def vers_detail(request):
    return redirect("blog:detail", pk=42)           # par nom, avec arguments

def vers_article(request, pk: int):
    article = get_object_or_404(Article, pk=pk)
    return redirect(article)                        # utilise get_absolute_url()

def vers_site_externe(request):
    return redirect("https://exemple.com")          # URL absolue
```

```python
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path("ancienne-page/", RedirectView.as_view(pattern_name="blog:liste", permanent=True)),
]
```

- `permanent=True` envoie un **301** (les moteurs de recherche transfèrent le référencement) ; sinon **302** (temporaire).
- Après un `POST` réussi, redirigez toujours (motif **Post/Redirect/Get**, section 6.2).

### 5.5 Pages d'erreur personnalisées

```python
# config/urls.py
handler404 = "apps.accueil.views.page_introuvable"
handler500 = "apps.accueil.views.erreur_serveur"
handler403 = "apps.accueil.views.acces_refuse"
handler400 = "apps.accueil.views.mauvaise_requete"
```

```python
# apps/accueil/views.py
from django.shortcuts import render

def page_introuvable(request, exception):
    return render(request, "404.html", status=404)

def erreur_serveur(request):
    return render(request, "500.html", status=500)

def acces_refuse(request, exception):
    return render(request, "403.html", status=403)

def mauvaise_requete(request, exception):
    return render(request, "400.html", status=400)
```

Plus simple : créez `templates/404.html` et `templates/500.html` ; Django les utilise automatiquement quand `DEBUG = False`. Attention : en `DEBUG = True`, Django affiche sa page technique à la place.

### 5.6 Fichiers statiques et médias en développement

```python
# config/urls.py (à la suite de urlpatterns)
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Cet utilitaire ne fonctionne **qu'avec `DEBUG = True`** : en production, un serveur web frontal ou un stockage cloud sert les médias (section 14).

### 5.7 Internationalisation des URL

```python
from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from django.utils.translation import gettext_lazy as _

from apps.accueil import views

urlpatterns += i18n_patterns(
    path(_("a-propos/"), views.a_propos, name="a-propos"),   # /fr/a-propos/ · /en/about/
    prefix_default_language=False,
)
```

`i18n_patterns` ajoute un préfixe de langue (`/en/…`) et permet de traduire les segments eux-mêmes ; `prefix_default_language=False` laisse la langue par défaut sans préfixe.

### 5.8 URL pour les API REST

```python
# apps/blog/urls_api.py (détails : section 19)
from rest_framework.routers import DefaultRouter
from .views_api import ArticleViewSet

router = DefaultRouter()
router.register("articles", ArticleViewSet, basename="article")
urlpatterns = router.urls

# config/urls.py
urlpatterns += [path("api/v1/", include("apps.blog.urls_api"))]
```

**Conventions REST** : noms de ressources au **pluriel** (`/articles/`), **verbes HTTP** pour les actions (plutôt que `/supprimer-article/`), **versionnement** dans l'URL (`/api/v1/`).

### 5.9 Diagnostiquer les problèmes de routage

| Symptôme | Piste |
| --- | --- |
| `404` inattendue | Ordre des motifs, `/` final manquant (`APPEND_SLASH = True` par défaut redirige `/blog` vers `/blog/`, mais pas pour les `POST`), `include` mal placé |
| `NoReverseMatch` | Nom ou espace de noms incorrect, arguments manquants ou de mauvais type |
| Un motif en « masque » un autre | Placer le motif **le plus spécifique** en premier |
| URL non reconnue avec `i18n_patterns` | Préfixe de langue manquant |

```bash
python manage.py show_urls            # (django-extensions) liste toutes les routes
```

### À retenir

- URLconf = liste ordonnée ; **première correspondance gagnante**.
- `include` + `app_name` = routage modulaire ; **nommez** et **inversez** toujours (`reverse`, `{% url %}`, `get_absolute_url`).
- Les convertisseurs typent les arguments ; `re_path` en dernier recours.

---

## 6. Vues

### Objectifs d'apprentissage

Définir ce qu'est une vue ; écrire des vues fonctions (FBV) et classes (CBV) ; gérer les méthodes HTTP, le motif Post/Redirect/Get et les erreurs ; maîtriser les vues génériques et les mixins ; choisir FBV ou CBV ; écrire une vue asynchrone ; organiser les vues d'une grosse application.

### 6.1 Qu'est-ce qu'une vue ?

> **Définition.** Une **vue** est un *appelable* Python qui reçoit un objet **`HttpRequest`** (et les paramètres capturés dans l'URL) et renvoie un objet **`HttpResponse`** (HTML, JSON, redirection, fichier, erreur…) ou lève une exception HTTP.

Django convertit les exceptions `Http404` et `PermissionDenied` en réponses 404 et 403 ; toute autre exception non gérée produit une 500.

### 6.2 Vues basées sur des fonctions (FBV)

```python
# apps/blog/views.py
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Article

def liste_articles(request: HttpRequest) -> HttpResponse:
    articles = Article.objects.publies().select_related("auteur")
    return render(request, "blog/liste.html", {"articles": articles})

def detail_article(request: HttpRequest, pk: int) -> HttpResponse:
    article = get_object_or_404(Article.objects.publies(), pk=pk)    # 404 automatique si absent
    return render(request, "blog/detail.html", {"article": article})

def detail_par_slug(request: HttpRequest, slug: str) -> HttpResponse:
    article = get_object_or_404(Article.objects.publies(), slug=slug)
    return render(request, "blog/detail.html", {"article": article})

def archives(request: HttpRequest, annee: int, mois: int | None = None) -> HttpResponse:
    articles = Article.objects.publies().filter(publie_le__year=annee)
    if mois is not None:
        articles = articles.filter(publie_le__month=mois)
    return render(request, "blog/liste.html", {"articles": articles})

def api_articles(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"articles": list(Article.objects.values("id", "titre"))})
```

- **`render(request, gabarit, contexte)`** charge un template, le rend avec le contexte et renvoie un `HttpResponse`.
- **`get_object_or_404`** évite le `try/except DoesNotExist` répétitif. Lui passer un **QuerySet filtré** (`Article.objects.publies()`) applique la règle métier : un brouillon donne 404.
- Un `QuerySet` étant paresseux, rien ne s'exécute tant que le template ne l'itère pas.

#### Gérer les méthodes HTTP : le motif Post/Redirect/Get

```python
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from .forms import ArticleForm

@require_http_methods(["GET", "POST"])
def creer_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.auteur = request.user
            article.save()
            form.save_m2m()                     # nécessaire après commit=False (relations ManyToMany)
            return redirect(article)            # Post/Redirect/Get
    else:
        form = ArticleForm()
    return render(request, "blog/formulaire.html", {"form": form})
```

**Post/Redirect/Get (PRG)** : après un `POST` valide, on **redirige** vers une page en `GET`. Ainsi, rafraîchir la page ne renvoie pas le formulaire (pas de double création) et le bouton « précédent » se comporte normalement.

#### Objets `request` et réponses utiles

| `request` | Contenu |
| --- | --- |
| `request.method` | `"GET"`, `"POST"`… |
| `request.GET`, `request.POST` | Dictionnaires de paramètres (`QueryDict`, accepte plusieurs valeurs par clé : `getlist`) |
| `request.FILES` | Fichiers envoyés |
| `request.body`, `request.headers`, `request.COOKIES`, `request.META` | Corps brut, en-têtes, cookies, variables d'environnement WSGI |
| `request.user`, `request.session` | Utilisateur et session (ajoutés par les middlewares) |
| `request.htmx` | Requête HTMX (avec `django-htmx`) |

Réponses : `HttpResponse`, `JsonResponse`, `HttpResponseRedirect`, `FileResponse`, `StreamingHttpResponse`, `HttpResponseNotFound`, `HttpResponseForbidden`, `HttpResponseNotAllowed`, et le raccourci `render()`.

### 6.3 Décorateurs de vue

```python
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

@login_required                                                 # redirige vers LOGIN_URL
@permission_required("blog.publish_article", raise_exception=True)
@cache_page(60 * 15)
def tableau_de_bord(request):
    return HttpResponse("Tableau de bord")
```

Décorateurs usuels : `require_GET`, `require_POST`, `require_http_methods`, `login_required`, `permission_required`, `cache_page`, `never_cache`, `vary_on_headers`. `csrf_exempt` (désactivation de la protection CSRF) est **à éviter** : voir la section 26. Avec **`LoginRequiredMiddleware`** (5.1), toutes les vues exigent la connexion **par défaut** ; exemptez les vues publiques avec `@login_not_required`.

### 6.4 Vues basées sur des classes (CBV)

Une CBV regroupe la logique **par méthode HTTP** (méthodes `get`, `post`…) et permet l'**héritage** et les **mixins**.

```python
# apps/accueil/views.py
import csv

from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from apps.blog.models import Article

class Accueil(TemplateView):
    template_name = "accueil.html"

    def get_context_data(self, **kwargs):
        contexte = super().get_context_data(**kwargs)
        contexte["derniers"] = Article.objects.publies()[:5]
        return contexte

class ExportCsv(View):
    def get(self, request, *args, **kwargs):
        reponse = HttpResponse(content_type="text/csv")
        ecrivain = csv.writer(reponse)
        ecrivain.writerow(["id", "titre"])
        for article in Article.objects.publies():
            ecrivain.writerow([article.pk, article.titre])
        return reponse

    def post(self, request, *args, **kwargs):
        return HttpResponse(status=204)
```

Manœuvre interne : `as_view()` crée une fonction qui **instancie la classe à chaque requête**, appelle `setup()` puis `dispatch()`, qui route vers la méthode correspondant au verbe HTTP (ou renvoie 405). **N'enregistrez donc pas d'état par requête dans des attributs de classe** : ils seraient partagés.

### 6.5 Vues génériques

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
# apps/blog/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ArticleForm
from .models import Article

class ListeArticles(ListView):
    model = Article
    template_name = "blog/liste.html"
    context_object_name = "articles"
    paginate_by = 10
    ordering = ["-publie_le"]

    def get_queryset(self):
        qs = super().get_queryset().publies().select_related("auteur")
        if q := self.request.GET.get("q"):
            qs = qs.filter(titre__icontains=q)
        return qs

class DetailArticle(DetailView):
    model = Article                                  # template par défaut : blog/article_detail.html

    def get_queryset(self):
        return Article.objects.publies()             # évalué à chaque requête (et non à l'import)

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
        return self.get_object().auteur == self.request.user   # seul l'auteur peut modifier
```

**Points clés des vues génériques :**

- Les noms de templates par défaut suivent une convention : `<app>/<modèle>_list.html`, `_detail.html`, `_form.html`, `_confirm_delete.html`.
- **Points d'extension** : `get_queryset()` (quelles données), `get_context_data()` (quel contexte), `form_valid()` / `form_invalid()` (traitement du formulaire), `get_success_url()`.
- Dans l'objet, le contexte contient `object` / `object_list` et le nom explicite si `context_object_name` est défini ; avec `paginate_by`, les variables `page_obj`, `paginator`, `is_paginated`.
- **Mixins d'accès** (`LoginRequiredMixin`, `PermissionRequiredMixin`, `UserPassesTestMixin`) : **placez-les avant la vue générique** dans la liste d'héritage, car l'ordre de résolution des méthodes (MRO) fait que le mixin doit intercepter `dispatch()` en premier.
- Référence indispensable : *Classy Class-Based Views* (ccbv.co.uk) montre toutes les méthodes et attributs de chaque vue générique.

### FBV ou CBV ?

|  | **FBV** | **CBV** |
| --- | --- | --- |
| Lisibilité | **Explicite, simple** | Plus abstraite (héritage) |
| Réutilisation | Décorateurs, fonctions | **Mixins, héritage** |
| CRUD standard | Plus de code | **Très concis** |
| Cas particuliers | **Plus souple** | Peut devenir complexe |

> **Règle pratique** : **CBV génériques** pour le CRUD standard, **FBV** pour la logique atypique. Les deux se mélangent librement dans un même projet.

### 6.6 Vues asynchrones *(ajout)*

```python
# apps/blog/views.py
from django.http import JsonResponse
from .models import Article

async def statut(request):
    articles = [a async for a in Article.objects.publies()[:5]]   # ORM asynchrone
    total = await Article.objects.acount()
    return JsonResponse({"total": total, "titres": [a.titre for a in articles]})
```

Une vue déclarée `async def` s'exécute dans la boucle d'événements (sous ASGI) et peut `await` des opérations d'E/S. Voir la section 22 pour les règles (ne jamais bloquer la boucle).

### 6.7 Gestion des erreurs dans les vues

```python
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponse
from .models import Article

def vue(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        raise Http404("Article introuvable")
    if not request.user.has_perm("blog.view_article"):
        raise PermissionDenied                       # → 403
    return HttpResponse(article.titre)
```

Codes de réponse à connaître : **400** requête invalide, **401** non authentifié, **403** interdit, **404** introuvable, **405** méthode non autorisée, **409** conflit, **422** données non traitables, **429** trop de requêtes, **500** erreur serveur.

### 6.8 Organiser les vues

- Une app avec beaucoup de vues : **un paquet** `views/` (`views/articles.py`, `views/commentaires.py`) dont `__init__.py` réexporte les noms utiles.
- **Vues minces** : la **validation** va dans les **formulaires**, les **requêtes** dans les **gestionnaires / QuerySets**, la **logique métier** dans des **services**. Une vue ne devrait pas dépasser quelques dizaines de lignes.
- Testez la logique métier comme de simples fonctions, et les vues via le client de test (section 25).

### Pièges fréquents

| Piège | Remède |
| --- | --- |
| Requête non paginée renvoyant des milliers de lignes | `paginate_by`, pagination par curseur |
| `get_queryset` évalué à l'import (`queryset = Article.objects.all()` pour des données temporelles) | Surcharger `get_queryset()` |
| Oublier `form.save_m2m()` après `commit=False` | Toujours l'appeler |
| Mixin placé après la vue générique | Mixins d'abord |
| Logique métier dans la vue | La déplacer dans un service ou le modèle |

### À retenir

- Une vue transforme une `HttpRequest` en `HttpResponse` ; gardez-la **mince**.
- **PRG** après chaque `POST` réussi ; `get_object_or_404` avec un QuerySet filtré.
- CBV génériques pour le CRUD, FBV pour le spécifique ; mixins d'accès **avant** la vue générique.

---

## 7. Templates

### Objectifs d'apprentissage

Lire et écrire le langage de templates Django (variables, balises, filtres) ; structurer les pages par **héritage** et **inclusion** ; employer les balises et filtres intégrés, y compris `querystring` (5.1) et les **fragments** `partialdef` (6.0) ; créer ses propres balises, filtres et processeurs de contexte ; comprendre l'échappement automatique ; savoir quand envisager Jinja2 ; déboguer un template.

### 7.1 Le langage de templates Django (DTL)

Un **template** est un fichier texte (le plus souvent HTML) contenant des **variables** `{{ }}`, des **balises** `{% %}` et des **filtres** `|`. Le moteur le **rend** en combinant le template et un **contexte** (dictionnaire de variables fourni par la vue).

| Syntaxe | Rôle |
| --- | --- |
| `{{ variable }}` | Affiche une valeur (échappée) |
| `{{ valeur\|filtre:arg }}` | Transforme une valeur avant affichage |
| `{% balise %}` | Logique (condition, boucle, héritage…) |
| `{# commentaire #}` | Commentaire non rendu |

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

**Résolution d'une variable** : pour `article.titre`, Django essaie dans l'ordre : recherche par clé de dictionnaire, par attribut, par appel de méthode sans argument, puis par indice de liste. Cette « notation pointée » unifie dictionnaires, objets et listes. **Un template ne peut pas appeler une méthode avec arguments** : c'est voulu, la logique reste dans le code Python. La variable spéciale `forloop` fournit `counter`, `counter0`, `first`, `last`, `revcounter`, `parentloop`.

> **Échappement automatique.** `{{ variable }}` convertit `<`, `>`, `&`, `'`, `"` en entités HTML : c'est la protection contre le **XSS** (*Cross-Site Scripting*, injection de script). N'utilisez `|safe`, `mark_safe` ou `{% autoescape off %}` que pour du contenu **de confiance** que *vous* avez produit ou assaini.

### 7.2 Héritage de templates

L'héritage applique le principe **DRY** à la présentation : un template **parent** définit le squelette et des **blocs** surchargeables ; les **enfants** ne remplissent que les blocs.

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
{# apps/blog/templates/blog/liste.html #}
{% extends "base.html" %}
{% block titre %}Articles — {{ block.super }}{% endblock %}
{% block contenu %}
    {% for article in articles %}{% include "blog/_carte.html" with article=article only %}{% endfor %}
{% endblock %}
```

- `{% extends %}` doit être la **première** balise du fichier.
- `{{ block.super }}` inclut le contenu du bloc parent au lieu de le remplacer.
- `{% include "x.html" with a=1 only %}` : `with` passe des variables ; `only` **limite** le contexte à celles-ci (plus prévisible et plus rapide).
- **Organisation** : `templates/` (global) et `app/templates/app/` (**espace de noms** : évite que `blog/liste.html` n'entre en collision avec `boutique/liste.html`).
- Convention : préfixez par `_` les fragments destinés à `include` (`_carte.html`).

### 7.3 Balises et filtres intégrés

| Balises | Rôle |
| --- | --- |
| `if / elif / else`, `for / empty`, `with`, `block`, `extends`, `include` | Contrôle et structure |
| `url`, `static`, `csrf_token`, `load`, `now`, `cycle`, `firstof`, `ifchanged`, `regroup`, `spaceless`, `verbatim`, `widthratio`, `comment`, `autoescape` | Utilitaires |
| **`querystring`** *(5.1)* | Construire / modifier la chaîne de requête (pagination, filtres) |
| **`partialdef` / `partial`** *(6.0)* | **Fragments** nommés de template réutilisables |

| Filtres courants | Catégorie |
| --- | --- |
| `default`, `default_if_none`, `length`, `first`, `last`, `join`, `slice`, `dictsort` | Valeurs et listes |
| `lower`, `upper`, `title`, `capfirst`, `truncatechars`, `truncatewords`, `slugify`, `linebreaks`, `urlize`, `wordcount` | Texte |
| `date`, `time`, `timesince`, `timeuntil` | Dates |
| `floatformat`, `intcomma`, `filesizeformat`, `pluralize` | Nombres |
| `safe`, `escape`, `escapejs`, `json_script` | Sécurité / JavaScript |

```django
{# Pagination qui conserve les autres paramètres : balise querystring (5.1) #}
<a href="{% querystring page=page_obj.next_page_number %}">Suivant</a>

{# Passer des données à JavaScript en toute sécurité #}
{{ donnees|json_script:"donnees-page" }}
<script>const donnees = JSON.parse(document.getElementById("donnees-page").textContent);</script>
```

- `{% querystring page=3 %}` reprend les paramètres actuels (`?q=django&statut=publie`) et ne remplace que `page` : fini les liens de pagination qui perdent les filtres.
- `json_script` est la méthode **sûre** pour transmettre du JSON à JavaScript sans XSS, et elle est compatible avec une CSP stricte.

### 7.4 Fragments de template : `partialdef` *(6.0, à jour)*

Définissez un **fragment nommé** dans un template et **rendez-le seul** : idéal avec **HTMX**, qui attend des réponses HTML partielles.

```django
{# apps/blog/templates/blog/liste.html #}
{% extends "base.html" %}
{% block contenu %}
    {% partialdef liste-articles inline %}
        <ul id="articles">{% for a in articles %}<li>{{ a.titre }}</li>{% endfor %}</ul>
    {% endpartialdef %}
{% endblock %}
```

```python
# apps/blog/views.py
from django.shortcuts import render
from .models import Article

def liste(request):
    articles = Article.objects.publies()
    return render(request, "blog/liste.html#liste-articles", {"articles": articles})   # ne rend QUE le fragment
```

```django
{% partial liste-articles %}        {# réutiliser le fragment ailleurs #}
```

L'option `inline` fait que le fragment est rendu à sa place **et** reste appelable seul via la syntaxe `nom_du_template#nom_du_fragment`. Avant Django 6.0, le paquet `django-template-partials` offrait cette fonction.

### 7.5 Balises et filtres personnalisés

```python
# apps/blog/templatetags/blog_extras.py
from django import template
from apps.blog.models import Article

register = template.Library()

@register.filter
def temps_de_lecture(texte: str) -> int:
    return max(1, len(texte.split()) // 200)

@register.simple_tag(takes_context=True)
def url_page(context, page: int) -> str:
    requete = context["request"].GET.copy()
    requete["page"] = page
    return f"?{requete.urlencode()}"

@register.inclusion_tag("blog/_derniers.html")
def derniers_articles(n: int = 5):
    return {"articles": Article.objects.publies()[:n]}
```

```django
{% load blog_extras %}
{{ article.contenu|temps_de_lecture }} min · {% derniers_articles 3 %}
```

| Type | Décorateur | Usage |
| --- | --- | --- |
| **Filtre** | `@register.filter` | Transformer une valeur (`valeur\|filtre`) |
| **Balise simple** | `@register.simple_tag` | Calculer et afficher une valeur |
| **Balise d'inclusion** | `@register.inclusion_tag(gabarit)` | Rendre un sous-template avec son propre contexte |
| **Balise de bloc** | `Node` / `parser` | Structures avec corps (avancé) |

> Ajoutez un fichier `__init__.py` dans `templatetags/` et **redémarrez** le serveur après la création du module (il n'est chargé qu'au démarrage).

### 7.6 Processeurs de contexte

Un **processeur de contexte** est une fonction qui reçoit la requête et renvoie un dictionnaire injecté dans **tous** les templates rendus avec `RequestContext`.

```python
# apps/accueil/context_processors.py
from django.utils import timezone

def site(request):
    return {"NOM_SITE": "Mon site", "ANNEE": timezone.now().year}

# settings.py → TEMPLATES[0]["OPTIONS"]["context_processors"] += ["apps.accueil.context_processors.site"]
```

Utilisez-les **avec parcimonie** : ils s'exécutent à **chaque** rendu. Pas de requête coûteuse ici sans cache. Exemples intégrés : `request`, `auth` (donne `user` et `perms`), `messages`, `csp` (6.0, donne `csp_nonce`).

### 7.7 Fichiers statiques, formulaires, internationalisation

```django
{% load static i18n %}
<img src="{% static 'img/logo.png' %}" alt="">
<form method="post">{% csrf_token %}{{ form }}<button>Envoyer</button></form>
{% translate "Bienvenue" %} · {% blocktranslate with nom=user.first_name %}Bonjour {{ nom }}{% endblocktranslate %}
```

`{% load %}` doit être répété dans **chaque** template qui utilise une bibliothèque de balises (il n'est pas hérité du parent).

### 7.8 Jinja2 et autres moteurs

Django peut utiliser **Jinja2** (`django.template.backends.jinja2.Jinja2`) : plus rapide et plus expressif (appels de méthodes avec arguments, macros), mais **incompatible** avec les templates de l'admin et de nombreuses bibliothèques tierces, et il faut réécrire les balises. **Gardez le DTL** sauf besoin précis. Alternatives orientées **composants** : `django-cotton`, `django-components`, `django-slippers`.

### 7.9 Déboguer les templates

- `TEMPLATES[0]["OPTIONS"]["debug"]` (déduit de `DEBUG`) : page d'erreur détaillée indiquant la ligne fautive.
- Une `{{ variable }}` **absente** produit une **chaîne vide silencieuse** : utilisez `string_if_invalid` en développement ou `django-debug-toolbar` (onglets *Templates* et *Context*).
- `{% debug %}` affiche tout le contexte ; le filtre `|pprint` formate un objet.

### Pièges fréquents

| Piège | Remède |
| --- | --- |
| Logique métier ou requêtes dans le template | Préparer les données dans la vue ; `select_related` / `prefetch_related` |
| `\|safe` sur du contenu utilisateur | Laisser l'échappement ; assainir (`nh3`) si HTML riche |
| Oubli de `{% csrf_token %}` | Erreur 403 à l'envoi du formulaire |
| Oubli de `{% load static %}` | `TemplateSyntaxError` sur `{% static %}` |
| Balise personnalisée introuvable | `__init__.py` manquant, serveur non redémarré, `{% load %}` oublié |

### À retenir

- Le DTL **sépare** présentation et logique ; il **échappe** par défaut.
- Héritage (`extends`/`block`) + inclusion (`include`) + fragments (`partialdef`) = pages DRY.
- Balises personnalisées et processeurs de contexte : à utiliser avec mesure.

---

# Données et interface

---

## 8. Modèles

### Objectifs d'apprentissage

Définir des modèles et choisir les bons types de champs et options ; modéliser des relations (`ForeignKey`, `OneToOneField`, `ManyToManyField` avec table intermédiaire) et comprendre `on_delete` ; gérer le schéma par **migrations** (y compris migrations de données) ; valider, ajouter des méthodes et gestionnaires ; maîtriser l'héritage de modèles ; utiliser du SQL brut en sécurité.

### 8.1 Définir un modèle

> **Définition.** Un **modèle** est une classe Python héritant de `django.db.models.Model` qui décrit une **table** : chaque attribut de type `Field` devient une **colonne**, chaque instance une **ligne**. Le modèle est la **source unique de vérité** (principe DRY) : migrations, formulaires, admin et API en dérivent.

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
    class Statut(models.TextChoices):                         # énumération de choix
        BROUILLON = "brouillon", "Brouillon"
        PUBLIE = "publie", "Publié"
        ARCHIVE = "archive", "Archivé"

    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date="publie_le")
    contenu = models.TextField()
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    categories = models.ManyToManyField(Categorie, blank=True, related_name="articles")
    statut = models.CharField(max_length=10, choices=Statut, default=Statut.BROUILLON)
    note = models.PositiveSmallIntegerField(db_default=0)      # valeur par défaut côté BASE (5.0)
    cree_le = models.DateTimeField(auto_now_add=True)
    modifie_le = models.DateTimeField(auto_now=True)
    publie_le = models.DateTimeField(default=timezone.now)

    objects = ArticleQuerySet.as_manager()

    class Meta:
        ordering = ["-publie_le"]
        permissions = [("publish_article", "Peut publier un article")]
        indexes = [models.Index(fields=["statut", "-publie_le"])]
        constraints = [
            models.CheckConstraint(condition=models.Q(note__gte=0, note__lte=5), name="article_note_0_5"),
        ]

    def __str__(self) -> str:
        return self.titre

    def get_absolute_url(self) -> str:
        return reverse("blog:detail", kwargs={"pk": self.pk})
```

**Lecture guidée :**

- `class Meta` regroupe les **méta-données** : `ordering` (tri par défaut), `permissions` (permissions personnalisées), `indexes`, `constraints`, `verbose_name`, `db_table`, `unique_together` (préférez `UniqueConstraint`).
- `TextChoices` / `IntegerChoices` : énumérations de choix ; la valeur stockée est le premier élément, le libellé le second.
- `unique_for_date="publie_le"` : le slug doit être unique **pour un jour donné**.
- Depuis Django 5.1, `CheckConstraint` utilise le paramètre **`condition=`** (l'ancien `check=` est déprécié).
- `__str__` définit la représentation textuelle (admin, shell, listes déroulantes) : **toujours le définir**.

### 8.2 Types de champs

| Catégorie | Champs |
| --- | --- |
| **Texte** | `CharField(max_length)`, `TextField`, `SlugField`, `EmailField`, `URLField`, `UUIDField` |
| **Nombres** | `IntegerField`, `BigIntegerField`, `SmallIntegerField`, `PositiveIntegerField`, `FloatField`, `DecimalField(max_digits, decimal_places)` (recommandé pour l'argent) |
| **Booléen** | `BooleanField` |
| **Dates** | `DateField`, `DateTimeField`, `TimeField`, `DurationField` (`auto_now`, `auto_now_add`) |
| **Fichiers** | `FileField`, `ImageField` (nécessite **Pillow**) |
| **Structurés** | **`JSONField`** (JSON natif, requêtes sur les clés), `GenericIPAddressField`, `BinaryField` |
| **Relations** | `ForeignKey`, `OneToOneField`, `ManyToManyField` |
| **Calculé** | **`GeneratedField`** *(5.0)* : valeur calculée par la **base** |
| **PostgreSQL** | `ArrayField`, `HStoreField`, `DateRangeField`, `SearchVectorField` (`django.contrib.postgres`) |

**Pourquoi `DecimalField` pour l'argent ?** Les `float` sont binaires et inexacts (`0.1 + 0.2 != 0.3`) ; `Decimal` est exact. `auto_now_add` fixe la date à la création ; `auto_now` la met à jour à chaque `save()`.

#### Options communes

| Option | Rôle |
| --- | --- |
| `null=True` | Stocke `NULL` en base (évitez pour `CharField`/`TextField` : préférez la chaîne vide `""`, sinon deux « vides » coexistent) |
| `blank=True` | Champ **facultatif dans les formulaires** (c'est de la validation, pas du stockage) |
| `default`, `db_default` | Valeur par défaut côté Python / côté **base** (5.0) |
| `unique`, `db_index` | Unicité, index |
| `choices` | Liste, énumération `TextChoices` / `IntegerChoices`, ou **dictionnaire** (5.0) |
| `validators`, `help_text`, `verbose_name`, `editable`, `db_column` | Validation, aide, libellés, visibilité dans les formulaires, nom de colonne |

> **`null` vs `blank`** : `null` concerne la **base** ; `blank` concerne la **validation**. Un `DateField(null=True, blank=True)` est facultatif partout ; un `CharField(blank=True)` sans `null` stocke `""`.

```python
# apps/boutique/models.py
from decimal import Decimal

from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=150)
    prix_ht = models.DecimalField(max_digits=10, decimal_places=2)
    tva = models.DecimalField(max_digits=4, decimal_places=3, default=Decimal("0.200"))
    prix_ttc = models.GeneratedField(                         # colonne calculée par la base (5.0)
        expression=models.F("prix_ht") * (1 + models.F("tva")),
        output_field=models.DecimalField(max_digits=12, decimal_places=2),
        db_persist=True,
    )
    quantite = models.PositiveIntegerField(default=0)         # stock disponible
    metadonnees = models.JSONField(default=dict, blank=True)
```

### 8.3 Clés primaires

Par défaut, Django ajoute un champ `id` (**`BigAutoField`**). Autres choix :

```python
# apps/boutique/models.py
import uuid

from django.db import models

class Commande(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    # ou UUID7 côté base (6.1)

class LigneCommande(models.Model):                                                 # clé composite (5.2)
    pk = models.CompositePrimaryKey("commande_id", "produit_id")
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
```

- **UUID** : identifiants non devinables, pratiques pour les API publiques et la génération côté client ; légèrement plus coûteux qu'un entier.
- **Clé composite** (`CompositePrimaryKey`, 5.2) : la clé est formée de plusieurs colonnes, utile pour les tables d'association ; certaines fonctions (admin, `ForeignKey` vers un tel modèle) ont des limites, consultez la documentation.

### 8.4 Relations

```python
# apps/blog/models.py
from django.conf import settings
from django.db import models

class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="commentaires")  # plusieurs → un
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    texte = models.TextField()
    cree_le = models.DateTimeField(auto_now_add=True)
    valide = models.BooleanField(default=True)

class Etiquette(models.Model):
    nom = models.CharField(max_length=50)
    articles = models.ManyToManyField(Article, through="Classement")                              # plusieurs → plusieurs

class Classement(models.Model):                                                                    # table intermédiaire
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    etiquette = models.ForeignKey(Etiquette, on_delete=models.CASCADE)
    rang = models.PositiveSmallIntegerField(default=0)
```

```python
# apps/comptes/models.py
class Profil(models.Model):
    utilisateur = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)       # un → un
```

| Relation | Champ | Exemple |
| --- | --- | --- |
| **Plusieurs → un** | `ForeignKey` (sur le côté « plusieurs ») | Un article a un auteur, un auteur a plusieurs articles |
| **Un → un** | `OneToOneField` | Utilisateur ↔ profil |
| **Plusieurs → plusieurs** | `ManyToManyField` (+ `through` pour porter des données) | Article ↔ catégories |

`related_name` nomme la **relation inverse** (`article.commentaires`) ; sans lui, Django utilise `commentaire_set`. On peut référencer un modèle par chaîne (`"blog.Article"`) pour éviter les imports circulaires.

| `on_delete` | Comportement à la suppression de l'objet référencé |
| --- | --- |
| `CASCADE` | Supprime aussi les objets liés |
| `PROTECT` | Interdit la suppression (`ProtectedError`) |
| `RESTRICT` | Interdit, sauf suppression en cascade par un autre chemin |
| `SET_NULL` / `SET_DEFAULT` / `SET(valeur)` | Remplace la référence (`SET_NULL` exige `null=True`) |
| `DO_NOTHING` | Rien (la base peut refuser) |
| **`DB_CASCADE`**, **`DB_SET_NULL`**, **`DB_SET_DEFAULT`** *(6.1)* | **Délégué à la base de données** (contraintes `ON DELETE`) : plus rapide, sans charger les objets |

```python
# python manage.py shell
article = Article.objects.first()
categorie = Categorie.objects.first()

print(article.commentaires.all())                       # relation inverse (related_name)
article.categories.add(categorie)                       # ManyToMany : add / remove / set / clear
print(Article.objects.filter(categories__slug="python"))
```

### 8.5 Migrations

> **Définition.** Une **migration** est un fichier Python qui décrit une **évolution du schéma** (créer une table, ajouter une colonne…). L'ensemble forme l'**historique** versionné du schéma, applicable de façon reproductible sur toute base.

```bash
python manage.py makemigrations                 # détecte les changements de modèles → fichiers dans migrations/
python manage.py makemigrations blog -n ajout_note
python manage.py migrate                        # applique
python manage.py showmigrations
python manage.py sqlmigrate blog 0002           # voir le SQL
python manage.py migrate blog 0001              # revenir en arrière
python manage.py makemigrations --check --dry-run   # (CI) échoue s'il manque une migration
python manage.py squashmigrations blog 0001 0020    # condenser l'historique
```

Cycle de travail : **1)** modifier `models.py` ; **2)** `makemigrations` ; **3)** relire le fichier généré ; **4)** `migrate` ; **5)** committer modèles **et** migrations ensemble.

**Migration de données** (`RunPython`) :

```python
# apps/blog/migrations/0004_remplir_slugs.py
from django.db import migrations
from django.utils.text import slugify

def remplir_slugs(apps, schema_editor):
    Article = apps.get_model("blog", "Article")        # modèle HISTORIQUE, jamais l'import direct
    for a in Article.objects.filter(slug=""):
        a.slug = slugify(a.titre)
        a.save(update_fields=["slug"])

class Migration(migrations.Migration):
    dependencies = [("blog", "0003_article_slug")]
    operations = [migrations.RunPython(remplir_slugs, migrations.RunPython.noop)]
```

- Le **modèle historique** (`apps.get_model`) reflète le schéma **à ce point de l'historique** ; l'importer directement casserait la migration dès que le modèle évolue.
- Le second argument de `RunPython` (ici `noop`) est l'opération **inverse**, nécessaire pour pouvoir annuler la migration.

> **Règles d'or** : **versionnez** les migrations dans Git ; **ne modifiez jamais** une migration déjà appliquée en production (créez-en une nouvelle) ; ajoutez une colonne `NOT NULL` en **plusieurs étapes** (nullable → remplissage → contrainte) pour ne pas verrouiller de grosses tables (voir section 28.6).

### 8.6 Validation et nettoyage

```python
# apps/blog/models.py : méthode à ajouter dans la classe Article
from django.core.exceptions import ValidationError

class Article(models.Model):
    # ... champs de la section 8.1 ...

    def clean(self):        # validation globale (appelée par full_clean et les ModelForm)
        if self.statut == self.Statut.PUBLIE and len(self.contenu) < 100:
            raise ValidationError({"contenu": "Un article publié doit contenir au moins 100 caractères."})
```

> **Piège capital** : `save()` n'appelle **pas** `full_clean()` automatiquement. La validation s'exécute dans les **formulaires** (`ModelForm`) et l'admin, pas lors d'un `Article.objects.create(...)`. Les **contraintes de base** (`CheckConstraint`, `UniqueConstraint`) sont plus fiables que la seule validation Python, car elles protègent aussi contre les écritures directes et les accès concurrents.

### 8.7 Méthodes, propriétés et gestionnaires

```python
class Article(models.Model):
    # ... champs de la section 8.1 ...

    @property
    def temps_de_lecture(self) -> int:
        return max(1, len(self.contenu.split()) // 200)

    def publier(self) -> None:                                   # logique métier dans le modèle
        self.statut = self.Statut.PUBLIE
        self.publie_le = timezone.now()
        self.save(update_fields=["statut", "publie_le"])
```

```python
class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("auteur")
```

- Un **gestionnaire** (*manager*, `objects`) est l'interface de requête d'un modèle ; on peut en définir de personnalisés. Pour des méthodes chaînables, préférez un **QuerySet personnalisé** converti en gestionnaire par `as_manager()` (section 9.10).
- Modèle **« gras »** (*fat model*) : la logique propre à une entité vit dans le modèle ; la logique **transverse** (plusieurs modèles, services externes) dans des services.

### 8.8 Héritage de modèles

| Type | Table(s) | Usage |
| --- | --- | --- |
| **Classe abstraite** (`Meta: abstract = True`) | Aucune table pour le parent ; les champs sont **copiés** dans chaque enfant | **Champs communs** (horodatage) |
| **Multi-table** | Une table par modèle, liées par un `OneToOne` implicite | Hiérarchie avec requêtes sur le parent (attention aux jointures) |
| **Proxy** (`proxy = True`) | Aucune nouvelle | Changer le **comportement** (gestionnaire, méthodes, tri) sans changer le schéma |

```python
from django.db import models

class Horodate(models.Model):
    cree_le = models.DateTimeField(auto_now_add=True)
    modifie_le = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Note(Horodate):                                           # hérite de cree_le et modifie_le
    texte = models.TextField()
```

### 8.9 Performances (aperçu)

`select_related` / `prefetch_related` (problème N+1), `only()` / `defer()`, index, `bulk_create` : voir la section 9.

### 8.10 SQL brut

```python
# python manage.py shell
from django.db import connection

# paramètres : toujours liés (%s), jamais de f-string
for article in Article.objects.raw("SELECT * FROM blog_article WHERE note > %s", [3]):
    print(article.titre)

with connection.cursor() as curseur:
    curseur.execute("SELECT COUNT(*) FROM blog_article WHERE statut = %s", ["publie"])
    print(curseur.fetchone())                                   # (nombre,)
```

> **Ne construisez jamais du SQL avec des f-strings ou l'opérateur `%`** sur des données utilisateur : c'est l'**injection SQL**. Les paramètres liés (`%s` + liste) sont transmis séparément au pilote, qui les protège.

### Pièges fréquents

| Piège | Remède |
| --- | --- |
| `null=True` sur `CharField` | Préférer `""` |
| Float pour de l'argent | `DecimalField` |
| Compter sur `save()` pour valider | `full_clean()` ou contraintes de base |
| Modèle utilisateur importé directement | `settings.AUTH_USER_MODEL` |
| Migration modifiée après déploiement | Nouvelle migration |

### À retenir

- Le modèle est la **source de vérité** ; choisissez types, options, contraintes et index avec soin.
- `ForeignKey` + `on_delete` réfléchi ; `through` pour les relations portant des données.
- Les migrations sont du code **versionné** : relues, committées, jamais réécrites après déploiement.

---

## 9. ORM : requêtes et optimisation

### Objectifs d'apprentissage

Effectuer toutes les opérations CRUD avec l'ORM ; comprendre la **paresse** et le **cache** des QuerySets ; composer des filtres avec lookups, `Q` et `F` ; agréger et annoter (expressions, sous-requêtes, fenêtrage) ; **éliminer le problème N+1** (`select_related`, `prefetch_related`, `fetch_mode`) ; optimiser ; gérer les transactions, l'asynchrone, plusieurs bases, les gestionnaires personnalisés et la recherche plein texte.

### 9.1 Opérations de base

Un **QuerySet** est une requête *en cours de construction* ; un **gestionnaire** (`Article.objects`) en produit. Les exemples ci-dessous se tapent dans `python manage.py shell` (les modèles y sont importés automatiquement depuis Django 5.2).

```python
from datetime import timedelta
from django.utils import timezone

user = Utilisateur.objects.first()                      # un auteur existant

# Créer
article = Article.objects.create(titre="Bonjour", slug="bonjour", contenu="…", auteur=user)
a = Article(titre="X", slug="x", contenu="…", auteur=user)
a.save()
Article.objects.bulk_create(
    [Article(titre=f"T{i}", slug=f"t{i}", contenu="…", auteur=user) for i in range(100)], batch_size=500
)

# Lire
print(Article.objects.all())
print(Article.objects.get(pk=article.pk))               # DoesNotExist / MultipleObjectsReturned
print(Article.objects.filter(statut="publie").exclude(auteur=user))
print(Article.objects.first(), Article.objects.last(), Article.objects.exists(), Article.objects.count())
print(Article.objects.get_or_create(slug="x2", defaults={"titre": "X2", "contenu": "…", "auteur": user}))  # (objet, créé)
print(Article.objects.update_or_create(slug="x2", defaults={"titre": "Y"}))

# Modifier
article.titre = "Nouveau"
article.save(update_fields=["titre"])
print(Article.objects.filter(statut="brouillon").update(statut="archive"))   # UPDATE en une requête : nb de lignes
objets = list(Article.objects.filter(titre__startswith="T"))
for objet in objets:
    objet.note = 3
Article.objects.bulk_update(objets, ["note"])

# Supprimer
article.delete()
limite = timezone.now() - timedelta(days=365)
print(Article.objects.filter(cree_le__lt=limite).delete())                   # (nombre total, détail par modèle)
```

**Comprendre les méthodes :**

- `get()` renvoie **un seul** objet et lève `DoesNotExist` ou `MultipleObjectsReturned` ; `filter()` renvoie toujours un QuerySet (éventuellement vide).
- `save(update_fields=[...])` n'écrit que les colonnes citées (plus rapide, évite d'écraser des modifications concurrentes).
- `update()` et `delete()` sur un QuerySet s'exécutent en **une seule requête SQL** et **ne déclenchent ni `save()` ni les signaux `post_save`** (voir section 16).
- `bulk_create` / `bulk_update` regroupent les écritures ; eux non plus n'appellent pas `save()`.

> **Un QuerySet est paresseux.** Le SQL n'est exécuté qu'à l'**évaluation** : itération, `list()`, `len()`, découpage avec pas, `bool()`, `repr`. Une fois évalué, il est **mis en cache** (le deuxième parcours ne refait pas de requête). Chaîner `.filter().exclude().order_by()` ne crée que des objets de requête : une seule requête part, tout à la fin.

### 9.2 Filtres et lookups

Un **lookup** s'écrit `champ__opérateur=valeur`.

| Lookup | SQL | Exemple |
| --- | --- | --- |
| `exact`, `iexact` | `=` | `titre__iexact="django"` |
| `contains`, `icontains` | `LIKE '%…%'` | `titre__icontains="py"` |
| `startswith`, `endswith` | `LIKE` | `titre__startswith="Dj"` |
| `in` | `IN (…)` | `pk__in=[1, 2, 3]` |
| `gt`, `gte`, `lt`, `lte` | `>`, `>=`… | `note__gte=4` |
| `range` | `BETWEEN` | `cree_le__range=(debut, fin)` |
| `isnull` | `IS NULL` | `auteur__isnull=True` |
| `year`, `month`, `day`, `date`, `week_day` | dates | `publie_le__year=2026` |
| `regex`, `iregex` | expression régulière | `titre__regex=r"^Dj"` |
| Relations | `__` | `auteur__username="alice"`, `categories__slug="python"` |
| JSON | `__clé` | `metadonnees__couleur="rouge"` |

```python
from django.db.models import F, Q

print(Article.objects.filter(Q(titre__icontains="django") | Q(contenu__icontains="django")))   # OR
print(Article.objects.filter(~Q(statut="brouillon"), note__gte=3))                               # NOT + AND
print(Article.objects.filter(modifie_le__gt=F("cree_le")))                                       # comparer deux champs
Article.objects.filter(note__lt=5).update(note=F("note") + 1)                                    # incrément atomique
```

- Plusieurs arguments dans un même `filter()` s'**associent par AND** ; `Q` permet `|` (OR), `&` (AND) et `~` (NOT).
- **`F()`** référence la valeur d'une colonne **dans la base** : l'opération est atomique et évite la « course » lecture-modification-écriture en Python.
- Attention aux filtres sur des relations *plusieurs* : `filter(categories__slug="a", categories__nom="B")` dans **un seul** `filter` exige la même catégorie ; dans deux `filter` chaînés, des catégories potentiellement différentes.

### 9.3 Tri, découpage, valeurs

```python
print(Article.objects.order_by("-publie_le", "titre"))
print(Article.objects.order_by("?"))                    # aléatoire (coûteux)
print(Article.objects.all()[:10])                       # LIMIT 10 (pagination : [20:30])
print(Article.objects.values("id", "titre"))            # dictionnaires
print(Article.objects.values_list("titre", flat=True))  # liste de valeurs
print(Article.objects.in_bulk([1, 2]))                  # {id: objet}
print(Article.objects.distinct(), Article.objects.reverse(), Article.objects.none())
```

Le découpage `[a:b]` se traduit par `LIMIT`/`OFFSET` ; il n'accepte pas d'indices négatifs. `values()` / `values_list()` évitent d'instancier des objets : plus léger pour de gros volumes.

### 9.4 Agrégation et annotation

- **`aggregate()`** calcule une valeur sur **tout** le QuerySet (résultat : un dictionnaire).
- **`annotate()`** ajoute une valeur calculée **à chaque objet** (résultat : un QuerySet). Combiné à `values()`, il fait un `GROUP BY`.

```python
from django.db.models import Avg, Count, Max

print(Article.objects.aggregate(total=Count("id"), moyenne=Avg("note"), maxi=Max("publie_le")))

auteurs = (Utilisateur.objects
           .annotate(nb_articles=Count("articles", distinct=True), note_moyenne=Avg("articles__note"))
           .filter(nb_articles__gte=1)
           .order_by("-nb_articles"))
for a in auteurs:
    print(a.username, a.nb_articles)
```

#### Expressions et fonctions

```python
from django.db.models import Case, CharField, Count, Exists, F, OuterRef, Subquery, Value, When, Window
from django.db.models.functions import RowNumber, TruncMonth

niveaux = Article.objects.annotate(niveau=Case(
    When(note__gte=4, then=Value("excellent")), When(note__gte=2, then=Value("bon")),
    default=Value("faible"), output_field=CharField()))

dernier = Commentaire.objects.filter(article=OuterRef("pk")).order_by("-cree_le")
avec_dernier = Article.objects.annotate(dernier_commentaire=Subquery(dernier.values("texte")[:1]))

print(Article.objects.filter(Exists(Commentaire.objects.filter(article=OuterRef("pk")))))     # articles commentés

classement = Article.objects.annotate(
    rang=Window(expression=RowNumber(), partition_by=F("auteur"), order_by=F("note").desc()))  # fenêtrage

print(Article.objects.annotate(mois=TruncMonth("publie_le")).values("mois").annotate(n=Count("id")))
```

| Outil | Rôle |
| --- | --- |
| `Case` / `When` | Équivalent SQL de `CASE WHEN` (logique conditionnelle) |
| `Subquery` + `OuterRef` | Sous-requête corrélée (référence la ligne externe) |
| `Exists` | Test d'existence efficace (`EXISTS`) |
| `Window` + `RowNumber`, `Rank`, `Lag`… | Fonctions de **fenêtrage** (classements, cumuls par groupe) |
| `TruncMonth`, `TruncDate`, `Coalesce`, `Lower`, `Concat`… | Fonctions de base de données |

### 9.5 Relations et jointures : éviter le problème N+1

> **Définition — N+1.** Anti-patron où l'on exécute **1** requête pour lister N objets, puis **N** requêtes supplémentaires (une par objet) pour charger une relation. Avec 100 articles : 101 requêtes au lieu de 1 ou 2. C'est la cause n°1 des sites Django lents.

```python
from django.db.models import Prefetch

# Mauvais : N+1 (1 requête + 1 par article)
for a in Article.objects.all():
    print(a.auteur.username)

# Bon : select_related : JOIN pour les relations « vers un » (ForeignKey, OneToOne)
for a in Article.objects.select_related("auteur", "auteur__profil"):
    print(a.auteur.username)

# Bon : prefetch_related : 2e requête groupée pour « vers plusieurs » (ManyToMany, relations inverses)
for a in Article.objects.prefetch_related("categories", "commentaires"):
    print(a.titre, a.commentaires.count())

# Préchargement filtré
articles = Article.objects.prefetch_related(
    Prefetch("commentaires", queryset=Commentaire.objects.filter(valide=True), to_attr="commentaires_valides")
)
for a in articles:
    print(a.titre, len(a.commentaires_valides))
```

|  | `select_related` | `prefetch_related` |
| --- | --- | --- |
| Relations | `ForeignKey`, `OneToOne` (vers un) | `ManyToMany`, relations inverses (vers plusieurs), GenericForeignKey |
| Mécanisme | **Une** requête avec `JOIN` | **Une requête supplémentaire** par relation, jointure faite en Python |
| Coût | Lignes plus larges | Requêtes `IN (…)` |

Attention : dans la boucle ci-dessus, `a.commentaires.count()` refait une requête même après `prefetch_related` ; utilisez `len(a.commentaires.all())` pour exploiter le cache préchargé, ou une annotation `Count`.

#### Modes de chargement des champs *(6.1, ajout)*

Django 6.1 permet de **choisir le comportement** du chargement à la demande pour contrer le N+1 **sans** modifier chaque requête (détail exact de l'API : notes de version 6.1) :

```python
from django.db import models

articles = Article.objects.fetch_mode(models.FETCH_PEERS)   # charge la relation pour TOUS les objets « pairs » en une requête
for a in articles:
    print(a.auteur.username)                                # 2 requêtes au total, malgré la boucle

# FETCH_ONE (comportement classique) · FETCH_RAISE : lève une erreur si un chargement à la demande a lieu
#                                                         (détecter les N+1 dans les tests)
```

### 9.6 Optimiser les requêtes

| Technique | Effet |
| --- | --- |
| `select_related` / `prefetch_related` | Supprime le N+1 |
| **`only()` / `defer()`** | Ne charge que (ou exclut) certaines colonnes |
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
from django.db import connection
from django.test.utils import CaptureQueriesContext

print(Article.objects.filter(statut="publie").explain(analyze=True))

with CaptureQueriesContext(connection) as ctx:
    print([a.auteur.username for a in Article.objects.select_related("auteur")])
print(len(ctx), "requête(s)")                            # 1 requête
```

**Méthode** : *mesurez d'abord*, optimisez ensuite. Un index inutile ralentit les écritures ; un `select_related` excessif ramène trop de colonnes.

### 9.7 Transactions

> **Définition.** Une **transaction** regroupe plusieurs opérations en un bloc **atomique** : tout réussit, ou rien n'est enregistré (propriétés ACID).

```python
# apps/boutique/services.py
from django.db import transaction
from django.db.models import F

from .models import Commande, Produit
from .tasks import envoyer_confirmation                   # tâche présentée en section 23

@transaction.atomic                                        # tout ou rien
def passer_commande(lignes: list[tuple[int, int]]) -> Commande:
    commande = Commande.objects.create()
    for produit_id, quantite in lignes:
        Produit.objects.select_for_update().filter(pk=produit_id).update(quantite=F("quantite") - quantite)
    transaction.on_commit(lambda: envoyer_confirmation.delay(str(commande.pk)))   # APRÈS la validation
    return commande
```

- `transaction.atomic` s'utilise en **décorateur** ou en **gestionnaire de contexte** (`with transaction.atomic():`) ; les blocs imbriqués créent des *savepoints*.
- `select_for_update()` **verrouille** les lignes jusqu'à la fin de la transaction (empêche deux commandes de se partager le même stock).
- `transaction.on_commit(fonction)` diffère une action (envoi d'e-mail, mise en file d'une tâche) **après** la validation : sinon le worker pourrait chercher un objet pas encore enregistré.
- `ATOMIC_REQUESTS = True` (dans `DATABASES`) enveloppe chaque requête HTTP dans une transaction.

### 9.8 ORM asynchrone *(ajout)*

Préfixe `a` pour les opérations **terminales** (`aget`, `acreate`, `acount`, `afirst`, `aexists`…), `async for` pour l'itération :

```python
import asyncio

async def exemples():
    auteur = await Utilisateur.objects.afirst()
    article = await Article.objects.aget(pk=1)
    nb = await Article.objects.filter(statut="publie").acount()
    await Article.objects.acreate(titre="X", slug="x-async", contenu="…", auteur=auteur)
    async for a in Article.objects.filter(statut="publie"):
        print(a.titre)
    existe = await Article.objects.filter(slug="x-async").aexists()
    print(article.titre, nb, existe)

asyncio.run(exemples())      # dans un script ; dans une vue asynchrone, utilisez directement await
```

Les opérations non encore natives peuvent être appelées avec `sync_to_async` (section 22). Le **traitement** de la requête reste exécuté dans un pool de threads côté pilote : l'async de l'ORM apporte surtout la *compatibilité* avec les vues asynchrones.

### 9.9 Plusieurs bases de données

```python
# settings.py
DATABASES = {
    "default": env.db("DATABASE_URL"),
    "lecture": env.db("DATABASE_REPLICA_URL"),
}
DATABASE_ROUTERS = ["config.routers.LectureEcriture"]
```

```python
# config/routers.py
class LectureEcriture:
    def db_for_read(self, model, **hints):
        return "lecture"

    def db_for_write(self, model, **hints):
        return "default"

    def allow_relation(self, o1, o2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == "default"
```

```python
print(Article.objects.using("lecture").all())            # forcer une base précise
```

Un **routeur** décide quelle base utiliser pour chaque lecture/écriture/migration. Attention au **retard de réplication** : lire sur le réplica juste après une écriture peut renvoyer des données anciennes.

### 9.10 Gestionnaires et QuerySets personnalisés

```python
# apps/blog/models.py (extrait)
from django.db import models

class ArticleQuerySet(models.QuerySet):
    def publies(self):
        return self.filter(statut="publie")

    def de(self, user):
        return self.filter(auteur=user)

class Article(models.Model):
    # ... champs de la section 8.1 ...
    objects = ArticleQuerySet.as_manager()
```

```python
user = Utilisateur.objects.first()
print(Article.objects.publies().de(user))                # chaînable
```

`as_manager()` expose les méthodes du QuerySet sur le gestionnaire **et** sur les résultats chaînés : `Article.objects.publies().de(user)` fonctionne, ce que ne permet pas un gestionnaire classique. C'est le meilleur endroit pour les **requêtes réutilisables** (principe : vues minces).

### 9.11 Recherche plein texte (PostgreSQL)

```python
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

vecteur = SearchVector("titre", weight="A") + SearchVector("contenu", weight="B")
resultats = (Article.objects
             .annotate(rang=SearchRank(vecteur, SearchQuery("django orm", config="french")))
             .filter(rang__gt=0.1)
             .order_by("-rang"))
print([(a.titre, a.rang) for a in resultats])
```

Le **plein texte** analyse la langue (radicalisation, mots vides) et classe par pertinence, contrairement à `icontains`. Les poids `A`/`B` donnent plus d'importance au titre. Pour de gros besoins : `django-haystack`, `django-elasticsearch-dsl`, **Meilisearch**, **Typesense**.

### Pièges fréquents

| Piège | Remède |
| --- | --- |
| `len(qs)` / `if qs:` sur un gros QuerySet | `count()` / `exists()` |
| Boucle d'`save()` pour des milliers d'objets | `bulk_create` / `bulk_update` / `update()` |
| Accès à une relation dans une boucle | `select_related` / `prefetch_related` |
| `order_by("?")` sur grosse table | Échantillonnage côté base ou identifiants |
| Lecture-modification-écriture en Python | `F()` ou `select_for_update()` |
| Signal attendu après `update()` / `bulk_*` | Appeler explicitement |

### À retenir

- **Paresse + cache** : le SQL part à l'évaluation ; enchaînez librement.
- Attaquez le **N+1** avec `select_related` / `prefetch_related` (ou `fetch_mode`), mesurez avec `assertNumQueries` et la debug toolbar.
- Poussez le travail vers la base : `F`, agrégats, annotations, `bulk_*`, index.

---

## 10. Interface d'administration

### Objectifs d'apprentissage

Activer l'admin et créer un superutilisateur ; enregistrer et personnaliser un modèle (`ModelAdmin`, `inlines`, filtres, recherche, actions, champs calculés) ; gérer permissions et groupes ; personnaliser l'apparence ; connaître les paquets d'extension ; sécuriser l'admin.

### 10.1 Activer et utiliser l'admin

L'**admin** est un back-office **généré automatiquement** à partir des modèles : idéal pour la gestion de contenu et les outils internes. Il est conçu pour le **personnel de confiance**, pas pour les utilisateurs finaux.

```python
# config/urls.py
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),      # en production, changez l'URL (« gestion-x7k2/ ») et protégez l'accès
]
```

```bash
python manage.py createsuperuser
```

### 10.2 Enregistrer et personnaliser un modèle

```python
# apps/blog/admin.py
from django.contrib import admin
from django.db.models import Count
from .models import Article, Categorie, Commentaire

class CommentaireInline(admin.TabularInline):                  # modifier les commentaires dans la page de l'article
    model = Commentaire
    extra = 0
    readonly_fields = ["cree_le"]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["titre", "auteur", "statut", "publie_le", "nb_commentaires"]
    list_filter = ["statut", "categories", "publie_le"]
    list_editable = ["statut"]
    list_select_related = ["auteur"]                           # évite le N+1 dans la liste
    search_fields = ["titre", "contenu", "auteur__username"]
    date_hierarchy = "publie_le"
    prepopulated_fields = {"slug": ("titre",)}
    autocomplete_fields = ["auteur"]                           # nécessite search_fields sur UtilisateurAdmin
    filter_horizontal = ["categories"]
    readonly_fields = ["cree_le", "modifie_le"]
    inlines = [CommentaireInline]
    actions = ["publier"]
    show_facets = admin.ShowFacets.ALLOW                       # (5.0) compteurs dans les filtres
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

    def has_delete_permission(self, request, obj=None):        # contrôle d'accès fin
        return request.user.is_superuser

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ["nom", "slug"]
    prepopulated_fields = {"slug": ("nom",)}
```

Pour `autocomplete_fields`, l'administration du modèle utilisateur doit définir `search_fields` :

```python
# apps/comptes/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur

@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    search_fields = ["username", "email"]
```

| Option de `ModelAdmin` | Rôle |
| --- | --- |
| `list_display`, `list_display_links`, `list_editable`, `list_filter`, `search_fields`, `date_hierarchy`, `ordering`, `list_per_page` | **Liste** : colonnes, liens, édition en ligne, filtres latéraux, recherche, navigation par date, tri, pagination |
| `fields`, `fieldsets`, `readonly_fields`, `prepopulated_fields`, `filter_horizontal`, `autocomplete_fields`, `raw_id_fields`, `formfield_overrides` | **Formulaire** : champs, regroupements, lecture seule, préremplissage, widgets de relations |
| `inlines` (`TabularInline`, `StackedInline`) | Objets liés éditables sur la même page |
| `actions` | Actions groupées sur la sélection |
| `save_model`, `get_queryset`, `get_form`, `has_*_permission` | Personnalisation avancée |
| `show_facets` | Facettes (5.0) |

**Points d'attention :** `list_select_related` et l'annotation dans `get_queryset` évitent le N+1 dans la liste ; `@admin.display` décrit une colonne calculée (libellé, tri possible via `ordering`) ; `@admin.action` définit une action groupée.

### 10.3 Permissions et groupes

Chaque modèle reçoit **4 permissions** automatiques : `add`, `change`, `delete`, `view`. Créez des **groupes** (ex. « Rédacteurs ») et attribuez-leur des permissions dans l'admin ; limitez le nombre de **superutilisateurs** (qui ont tous les droits). Les surcharges `has_add_permission`, `has_change_permission`, `has_delete_permission`, `has_view_permission` permettent un contrôle par objet ou par utilisateur.

### 10.4 Personnaliser l'apparence

```python
from django.contrib import admin

admin.site.site_header = "Administration — Mon site"
admin.site.site_title = "Mon site"
admin.site.index_title = "Tableau de bord"
```

- Surcharger les templates : `templates/admin/base_site.html` (`{% extends "admin/base.html" %}`).
- Thèmes et interfaces modernes : voir ci-dessous.

### 10.5 Paquets pour l'admin

| Paquet | Apport |
| --- | --- |
| **`django-unfold`** | Interface **moderne** (Tailwind), tableaux de bord, widgets |
| **`django-jazzmin`**, **`django-grappelli`**, **`django-admin-interface`** | Thèmes |
| **`django-import-export`** | Import / export CSV, Excel, JSON |
| **`django-simple-history`** | **Historique** des modifications (qui, quand, quoi) |
| **`django-reversion`** | Versions et **restauration** |
| **`django-admin-sortable2`**, **`django-adminactions`** | Tri par glisser-déposer, actions avancées |
| **`django-ckeditor-5`**, **`django-tinymce`** | Éditeur riche (`django-ckeditor` v4 est **abandonné**) |
| **`django-otp`** / `django-two-factor-auth` | **Double authentification** pour l'admin |
| **`django-axes`** | Blocage des tentatives de connexion répétées |

### 10.6 Sécurité de l'admin

- URL **non standard**, **HTTPS** obligatoire, **2FA**, accès restreint par IP / VPN si possible.
- Comptes **nominatifs**, permissions minimales, journal d'activité (`LogEntry`) consulté régulièrement.
- N'exposez pas l'admin à des utilisateurs non fiables : il est conçu pour le **personnel**.

### À retenir

- Quelques lignes suffisent pour un back-office complet ; configurez `list_display`, `search_fields`, `list_filter`, `inlines`.
- Soignez les requêtes (`list_select_related`, `get_queryset`) et les **permissions**.
- Sécurisez l'admin : HTTPS, 2FA, URL changeante, comptes nominatifs.

---

## 11. Formulaires

### Objectifs d'apprentissage

Comprendre le rôle d'un formulaire Django (génération, validation, nettoyage) ; écrire des `Form` et des `ModelForm` avec validation par champ et globale ; traiter un formulaire dans une vue ; rendre les formulaires dans les templates ; utiliser formsets et téléversements de fichiers ; maîtriser le CSRF et l'accessibilité.

### 11.1 Formulaires simples

> **Définition.** Un **formulaire Django** est une classe qui (1) **décrit** des champs, (2) **valide** les données reçues et les **convertit** en types Python (`cleaned_data`), (3) **génère** le HTML correspondant. Il remplace la validation à la main de `request.POST`, source classique de failles.

```python
# apps/accueil/forms.py
from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, label="Votre nom")
    email = forms.EmailField()
    sujet = forms.ChoiceField(choices=[("q", "Question"), ("b", "Bogue")])
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}), min_length=10)
    copie = forms.BooleanField(required=False, label="Recevoir une copie")

    def clean_email(self):                    # validation d'UN champ : clean_<champ>
        email = self.cleaned_data["email"]
        if email.endswith("@spam.test"):
            raise ValidationError("Domaine non autorisé.")
        return email

    def clean(self):                          # validation GLOBALE (plusieurs champs)
        donnees = super().clean()
        if donnees.get("sujet") == "b" and len(donnees.get("message", "")) < 50:
            self.add_error("message", "Décrivez le bogue en détail (50 caractères minimum).")
        return donnees
```

**Cycle de validation** (`form.is_valid()`) : pour chaque champ, conversion (`to_python`) → validateurs → `clean_<champ>()` ; puis `clean()` global. Les erreurs sont collectées dans `form.errors` ; les données valides finissent dans `form.cleaned_data`. Un formulaire est **lié** (*bound*) s'il reçoit des données (`ContactForm(request.POST)`), **non lié** sinon.

### 11.2 Traiter un formulaire dans une vue

```python
# apps/accueil/views.py
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactForm

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        send_mail(form.cleaned_data["sujet"], form.cleaned_data["message"], None, ["contact@exemple.fr"])
        messages.success(request, "Message envoyé, merci !")
        return redirect("accueil")               # Post/Redirect/Get : évite le double envoi
    return render(request, "contact.html", {"form": form})
```

```python
# apps/accueil/urls.py (route à ajouter)
urlpatterns += [path("contact/", views.contact, name="contact")]
```

Schéma standard : **GET** → formulaire vide ; **POST invalide** → réaffichage avec erreurs ; **POST valide** → traitement puis **redirection**.

### 11.3 ModelForm

Un **`ModelForm`** génère ses champs **à partir d'un modèle** (DRY) et sait enregistrer l'objet.

```python
# apps/blog/forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["titre", "slug", "contenu", "categories", "statut"]    # liste EXPLICITE
        widgets = {"contenu": forms.Textarea(attrs={"rows": 12})}
        labels = {"titre": "Titre de l'article"}
        help_texts = {"slug": "Utilisé dans l'URL."}

    def clean_titre(self):
        titre = self.cleaned_data["titre"]
        if Article.objects.filter(titre__iexact=titre).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Ce titre existe déjà.")
        return titre
```

```python
# apps/blog/views.py
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ArticleForm
from .models import Article

def modifier_article(request, pk):
    article = get_object_or_404(Article, pk=pk, auteur=request.user)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)   # instance → modification
    if request.method == "POST" and form.is_valid():
        article = form.save(commit=False)
        article.auteur = request.user
        article.save()
        form.save_m2m()                                      # indispensable après commit=False
        return redirect(article)
    return render(request, "blog/formulaire.html", {"form": form})
```

- `form.save()` crée ou met à jour l'instance et les relations `ManyToMany` ; `commit=False` renvoie l'objet **sans l'enregistrer** pour que vous le complétiez (ici l'auteur), d'où l'obligation d'appeler `save_m2m()` ensuite.
- Le `ModelForm` exécute aussi `Model.clean()` et la validation d'unicité du modèle.
- Le filtre `get_object_or_404(…, auteur=request.user)` impose la **propriété** (voir IDOR, section 26).

> **N'utilisez jamais `fields = "__all__"` ni `exclude` sur un formulaire public** : un utilisateur pourrait modifier des champs sensibles (`is_staff`, `auteur`…) en ajoutant des paramètres à la requête. C'est la faille de **mass assignment**. Listez explicitement les champs.

### 11.4 Rendu dans les templates *(à jour)*

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

Personnalisation : **`FORM_RENDERER`**, templates `django/forms/div.html`, attributs de widgets (`attrs={"class": "input"}`). `novalidate` désactive la validation HTML du navigateur pour laisser Django afficher ses messages.

| Paquet | Apport |
| --- | --- |
| **`django-crispy-forms`** + `crispy-bootstrap5` / `crispy-tailwind` | Rendu thématisé : `{{ form\|crispy }}` |
| **`django-widget-tweaks`** | Ajouter classes et attributs **dans le template** : `{% render_field form.titre class="input" %}` |
| **`django-formtools`** | Assistants multi-étapes (*wizard*) |

### 11.5 Widgets et champs utiles

Widgets : `TextInput`, `Textarea`, `Select`, `SelectMultiple`, `CheckboxSelectMultiple`, `RadioSelect`, `DateInput` (`type="date"`), `FileInput`, `ClearableFileInput`, `HiddenInput`, `PasswordInput`. Champs : `ModelChoiceField`, `ModelMultipleChoiceField`, `DateField`, `DecimalField`, `FileField`, `ImageField`, `JSONField`, `SlugField`, `RegexField`. Un **widget** gère la **présentation HTML** ; le **champ** gère la **validation et la conversion**.

### 11.6 Jeux de formulaires (*formsets*)

Un **formset** gère **plusieurs formulaires du même type** sur une page (lignes de commande, commentaires éditables).

```python
# apps/blog/views.py
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, render
from .models import Article, Commentaire

CommentaireFormSet = inlineformset_factory(Article, Commentaire, fields=["texte"], extra=2, can_delete=True)

def commentaires(request, pk):
    article = get_object_or_404(Article, pk=pk)
    formset = CommentaireFormSet(request.POST or None, instance=article)
    if request.method == "POST" and formset.is_valid():
        formset.save()
    return render(request, "blog/commentaires.html", {"formset": formset})
```

Le template doit afficher `{{ formset.management_form }}` (champs cachés qui comptent les formulaires ; sans eux, la validation échoue). `inlineformset_factory` lie les formulaires enfants à un objet parent.

### 11.7 Téléversement de fichiers

```python
# apps/blog/forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["fichier"]

    def clean_fichier(self):
        f = self.cleaned_data["fichier"]
        if f.size > 5 * 1024 * 1024:
            raise ValidationError("5 Mo maximum.")
        if f.content_type not in {"application/pdf", "image/png", "image/jpeg"}:
            raise ValidationError("Type non autorisé.")
        return f
```

> **`enctype="multipart/form-data"`** est **obligatoire** dans le `<form>`, et la vue doit passer `request.FILES`. Ne vous fiez ni à l'extension ni au `content_type` envoyé par le client (falsifiables) : validez le **contenu réel** (section 14.4 et 26).

### 11.8 CSRF

> **Définition — CSRF** (*Cross-Site Request Forgery*). Attaque où un site malveillant fait envoyer par le navigateur d'un utilisateur connecté une requête modifiante vers votre site (le navigateur joint automatiquement les cookies). Parade : un **jeton secret** que seul votre propre formulaire connaît.

`{% csrf_token %}` est **obligatoire** dans tout formulaire `POST` (le `CsrfViewMiddleware` vérifie le jeton ; sinon, erreur 403). Pour **AJAX / HTMX**, envoyez le jeton dans l'en-tête `X-CSRFToken` :

```html
<body hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'>        <!-- HTMX -->
```

### 11.9 Formulaires et accessibilité

Chaque champ doit avoir un `<label>` ; les erreurs doivent être associées au champ (`aria-describedby`) ; testez la navigation **au clavier**. Django fournit déjà des étiquettes et des messages d'aide structurés ; ne les supprimez pas lors de la personnalisation.

### À retenir

- Un formulaire **décrit, valide, nettoie et affiche** ; `ModelForm` dérive du modèle.
- Validation : `clean_<champ>` (un champ) et `clean` (global). **Liste explicite** de champs.
- Toujours `{% csrf_token %}`, `enctype` pour les fichiers, PRG après succès.

---

## 12. Authentification et autorisation

### Objectifs d'apprentissage

Distinguer **authentification** (qui êtes-vous ?) et **autorisation** (que pouvez-vous faire ?) ; créer un modèle utilisateur personnalisé ; utiliser les vues intégrées (connexion, mots de passe) et l'inscription ; protéger vues et templates (décorateurs, mixins, `LoginRequiredMiddleware`) ; gérer mots de passe, backends personnalisés, connexion sociale/2FA et sessions.

### 12.1 Le système intégré

`django.contrib.auth` fournit : **utilisateurs**, **groupes**, **permissions**, **sessions**, vues de **connexion / déconnexion / mots de passe**, et un **hachage** sécurisé (PBKDF2 par défaut, **Argon2** recommandé).

| Notion | Définition |
| --- | --- |
| **Authentification** | Vérifier l'identité (identifiant + mot de passe, jeton…) |
| **Autorisation** | Déterminer les actions permises (permissions, groupes, propriété d'objet) |
| **Hachage** | Transformation à sens unique du mot de passe (jamais stocké en clair) |
| **Session** | État serveur lié à un cookie, qui « mémorise » l'utilisateur connecté |

### 12.2 Modèle utilisateur personnalisé

```python
# apps/comptes/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    email = models.EmailField("adresse e-mail", unique=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True)

    USERNAME_FIELD = "email"                  # connexion par e-mail
    REQUIRED_FIELDS = ["username"]
```

```python
# settings.py
AUTH_USER_MODEL = "comptes.Utilisateur"
```

Toujours référencer l'utilisateur ainsi :

```python
# Dans le code
from django.contrib.auth import get_user_model
User = get_user_model()

# Dans les modèles
from django.conf import settings
from django.db import models

auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

> **`AbstractUser`** (modèle complet à étendre) suffit dans la grande majorité des cas ; **`AbstractBaseUser` + `PermissionsMixin`** donne un contrôle total (champs minimaux, gestionnaire personnalisé). Un **profil** séparé (`OneToOneField`) est une alternative pour des données volumineuses ou facultatives. Pour `USERNAME_FIELD = "email"`, un `UserManager` adapté est parfois nécessaire selon vos besoins.

### 12.3 Vues d'authentification intégrées

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

> Depuis Django 5.0, la déconnexion exige une requête **POST** (formulaire avec `{% csrf_token %}`), pas un simple lien : un lien `GET` pourrait déconnecter l'utilisateur à son insu (via une image piégée, par exemple).

#### Inscription

```python
# apps/comptes/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Utilisateur

class InscriptionForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Utilisateur
        fields = ("username", "email")

class Inscription(CreateView):
    form_class = InscriptionForm
    template_name = "registration/inscription.html"
    success_url = reverse_lazy("login")
```

`UserCreationForm` valide les mots de passe avec les validateurs configurés et hache le mot de passe. Django ne fournit pas de vue d'inscription prête à l'emploi (ni vérification d'e-mail) : voir `django-allauth` (12.7).

### 12.4 Contrôle d'accès

```python
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.views import View

# Fonctions
@login_required
@permission_required("blog.add_article", raise_exception=True)
def vue_fonction(request):
    return HttpResponse("Accès autorisé")

# Classes
class VueClasse(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "blog.change_article"

    def get(self, request):
        return HttpResponse("Accès autorisé")

# Dans le code
def verifier(request):
    est_connecte = request.user.is_authenticated
    peut_creer = request.user.has_perm("blog.add_article")
    est_redacteur = request.user.groups.filter(name="Rédacteurs").exists()
    return HttpResponse(f"connecté : {est_connecte} ; peut créer : {peut_creer} ; rédacteur : {est_redacteur}")
```

```django
{% if perms.blog.add_article %}<a href="{% url 'blog:creer' %}">Nouvel article</a>{% endif %}
{% if user.is_authenticated %}Bonjour {{ user.username }}{% endif %}
```

`@permission_required(..., raise_exception=True)` renvoie un **403** au lieu de rediriger vers la connexion (utile quand l'utilisateur est déjà connecté mais non autorisé). Un **superutilisateur** passe tous les contrôles.

#### Authentification obligatoire par défaut *(5.1, ajout)*

```python
# settings.py
MIDDLEWARE += ["django.contrib.auth.middleware.LoginRequiredMiddleware"]    # toutes les vues exigent la connexion

# apps/accueil/views.py
from django.contrib.auth.decorators import login_not_required
from django.http import HttpResponse

@login_not_required
def page_publique(request):
    return HttpResponse("Page accessible sans connexion")
```

C'est une approche « **fermé par défaut** » : on ne risque plus d'oublier de protéger une vue ; on **ouvre** explicitement les pages publiques.

#### Permissions d'objet

Les permissions natives sont **par modèle** (« peut modifier les articles »). Pour des permissions **par objet** (« seul l'auteur peut modifier *cet* article ») : `UserPassesTestMixin`, un filtre sur le QuerySet (`auteur=request.user`), ou **`django-guardian`** / **`django-rules`**.

### 12.5 Mots de passe

```python
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",      # pip install argon2-cffi
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",      # conservé pour relire les anciens hachages
]
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", "OPTIONS": {"min_length": 12}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
```

Le premier hacheur de la liste sert aux **nouveaux** mots de passe ; les suivants permettent de vérifier les anciens, qui sont **mis à niveau** automatiquement à la prochaine connexion. Les validateurs refusent les mots de passe trop courts, trop communs, numériques ou proches des informations de l'utilisateur.

### 12.6 Backends d'authentification personnalisés

```python
# apps/comptes/backends.py
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email__iexact=username)
        except User.DoesNotExist:
            return None
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
```

```python
# settings.py
AUTHENTICATION_BACKENDS = ["apps.comptes.backends.EmailBackend", "django.contrib.auth.backends.ModelBackend"]
```

Django essaie les backends **dans l'ordre** ; le premier qui renvoie un utilisateur l'emporte. Utile pour une connexion par e-mail, LDAP, SSO.

### 12.7 Connexion sociale, SSO et 2FA *(ajout)*

| Besoin | Paquet |
| --- | --- |
| **Inscription, e-mail vérifié, Google / GitHub / Microsoft, 2FA, passkeys** | **`django-allauth`** (le plus complet) ; mode **headless** pour SPA / API |
| OAuth 2 / OpenID Connect **fournisseur** | **`django-oauth-toolkit`** |
| Connexion sociale (alternative) | **`social-auth-app-django`** |
| **2FA** (TOTP, codes de secours) | **`django-otp`**, **`django-two-factor-auth`** |
| **SSO d'entreprise** (SAML, OIDC, LDAP) | `mozilla-django-oidc`, `djangosaml2`, `django-auth-ldap` |
| Protection force brute | **`django-axes`** |

```python
# django-allauth (extrait)
INSTALLED_APPS += ["django.contrib.sites", "allauth", "allauth.account", "allauth.socialaccount",
                   "allauth.socialaccount.providers.google"]
MIDDLEWARE += ["allauth.account.middleware.AccountMiddleware"]
AUTHENTICATION_BACKENDS += ["allauth.account.auth_backends.AuthenticationBackend"]
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
```

### 12.8 Sessions

```python
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"   # db | cache | cached_db | file | signed_cookies
SESSION_COOKIE_AGE = 60 * 60 * 24 * 14
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
```

```python
# apps/blog/views.py
from django.http import JsonResponse

def ajouter_au_panier(request):
    request.session["panier"] = {"1": 2}                # écriture (sérialisable en JSON)
    return JsonResponse(request.session["panier"])      # lecture

def vider_session(request):
    request.session.flush()                             # vider + régénérer la clé
    return JsonResponse({})
```

| Moteur | Principe | Remarque |
| --- | --- | --- |
| `db` | Table de base de données | Simple, fiable |
| `cache` | Cache (Redis) | Rapide ; données perdues si le cache est vidé |
| `cached_db` | Cache + base | Bon compromis |
| `signed_cookies` | Données dans le cookie signé | Pas de stockage serveur ; lisibles par le client |

Cookie de session : **`HttpOnly`** (illisible par JavaScript), **`Secure`** (HTTPS uniquement), **`SameSite`** (limite l'envoi inter-sites, aide contre le CSRF). Django **régénère la clé de session à la connexion** (anti-fixation).

### 12.9 Bonnes pratiques

- **Modèle personnalisé dès le début**, **Argon2**, validateurs de mots de passe, **2FA** pour le personnel.
- **Limitation des tentatives** (`django-axes`), messages d'erreur **identiques** (anti-énumération des comptes).
- **Ne stockez pas** de mots de passe en clair, ne les journalisez jamais.
- Testez les accès (`self.client.force_login(user)`), y compris les **cas refusés**.

### Pièges fréquents

| Piège | Remède |
| --- | --- |
| Lien `GET` pour se déconnecter | Formulaire `POST` |
| Vérifier la connexion dans le template seulement | Protéger la **vue** ; le template ne sécurise rien |
| Oublier le contrôle de propriété | Filtrer par `request.user` |
| `User` importé directement | `get_user_model()` / `settings.AUTH_USER_MODEL` |

### À retenir

- Authentification ≠ autorisation ; **modèle personnalisé** dès le départ ; **Argon2** et validateurs.
- Décorateurs/mixins pour les vues ; `LoginRequiredMiddleware` pour « fermé par défaut » ; permissions d'objet à la main ou avec guardian/rules.
- `django-allauth` pour l'inscription complète, le social et la 2FA.

---

## 13. Messages, sessions et cache

### Objectifs d'apprentissage

Utiliser le framework de **messages** (notifications éphémères) ; comprendre les **niveaux de cache** de Django (site, vue, fragment, bas niveau, en-têtes HTTP) ; configurer un backend (Redis) ; maîtriser l'invalidation et les clés de cache ; reconnaître les risques d'un cache mal conçu. (Les sessions sont détaillées en 12.8.)

### 13.1 Framework de messages

> **Définition.** Le framework de **messages** stocke des notifications **à usage unique** (« Article enregistré ») pour les afficher à la **prochaine** page vue par l'utilisateur, typiquement après une redirection (PRG).

```python
# apps/blog/views.py
from django.contrib import messages
from django.shortcuts import redirect

def enregistrer(request):
    messages.success(request, "Article enregistré.")
    messages.error(request, "Une erreur est survenue.")
    messages.add_message(request, messages.WARNING, "Attention.", extra_tags="important")
    # niveaux : DEBUG, INFO, SUCCESS, WARNING, ERROR
    return redirect("blog:liste")
```

```django
{% if messages %}
<ul class="messages">
{% for message in messages %}<li class="{{ message.tags }}" role="alert">{{ message }}</li>{% endfor %}
</ul>
{% endif %}
```

```python
# settings.py
from django.contrib.messages import constants as niveaux_messages

MESSAGE_STORAGE = "django.contrib.messages.storage.fallback.FallbackStorage"   # cookie puis session
MESSAGE_TAGS = {niveaux_messages.ERROR: "danger"}                                  # compatibilité Bootstrap
```

- Les messages sont **consommés à l'itération** : une fois affichés, ils disparaissent.
- `FallbackStorage` essaie d'abord le **cookie**, puis la **session** si le message est trop volumineux.
- `message.tags` fournit une classe CSS (`success`, `error`, `warning`, `info`, plus vos `extra_tags`) ; `MESSAGE_TAGS` permet d'ajuster le vocabulaire (Bootstrap attend `danger`).
- Dans une vue de classe : `SuccessMessageMixin` (`success_message = "Créé !"`). Avec **HTMX / AJAX** : renvoyez les messages dans un fragment ou via un en-tête `HX-Trigger`.

### 13.2 Cache : vue d'ensemble

> **Définition.** Un **cache** mémorise le résultat d'un calcul coûteux pour le réutiliser. Il échange de la **fraîcheur** contre de la **vitesse**. La difficulté centrale : savoir **quand l'invalider**.

| Niveau | Outil | Granularité |
| --- | --- | --- |
| **Site entier** | Middlewares `UpdateCacheMiddleware` / `FetchFromCacheMiddleware` | Toutes les pages publiques |
| **Vue** | `@cache_page(60 * 15)` | Une réponse HTTP complète |
| **Fragment de template** | `{% cache 500 sidebar request.user.id %}…{% endcache %}` | Un bloc de page |
| **Bas niveau** | `cache.get/set/get_or_set/delete/incr` | Une valeur arbitraire |
| **En-têtes HTTP** | `@cache_control`, `@etag`, `@last_modified`, `@condition` | Cache du navigateur / CDN |

```python
# python manage.py shell
from django.core.cache import cache

def calculer_stats():
    print("calcul en cours...")
    return {"articles": 42}

cache.set("stats", {"articles": 42}, timeout=300)
print(cache.get("stats", default=None))                   # {'articles': 42}
print(cache.get_or_set("stats", calculer_stats, 300))     # valeur déjà en cache : calculer_stats n'est pas appelée
cache.set("visites", 0)
print(cache.incr("visites"))                              # 1
cache.delete_many(["stats", "visites"])
```

```python
# apps/accueil/views.py
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

@cache_page(60 * 15, key_prefix="accueil")
def accueil(request):
    return HttpResponse("Accueil")
```

```django
{% load cache %}
{% cache 600 liste_articles page_obj.number %}{% for a in articles %}…{% endfor %}{% endcache %}
```

- `timeout` : durée de vie en secondes (`None` = sans expiration, `0` = ne pas mettre en cache).
- `get_or_set` évite le motif « lire, tester, calculer, écrire ».
- Dans `{% cache %}`, les arguments suivants la durée et le nom forment la **clé de variation** (ici le numéro de page).

### Backends

| Backend | Usage |
| --- | --- |
| **`RedisCache`** (intégré) | Production (partagé entre processus) ; nécessite le paquet `redis` (`django-redis` pour des fonctions avancées) |
| `MemcachedCache` / `PyMemcacheCache` | Alternative |
| `DatabaseCache` | Si pas de Redis |
| `LocMemCache` | Développement / tests (**par processus**, non partagé) |
| `FileBasedCache`, `DummyCache` | Spécifiques (`DummyCache` ne cache rien : utile pour désactiver) |

> **Invalidation — règles pratiques.** Donnez toujours une **durée de vie** ; incluez dans la **clé** tout ce qui fait varier le contenu (utilisateur, langue, page) ; ne mettez pas en cache de données **personnelles** dans une clé partagée (fuite entre utilisateurs) ; invalidez explicitement (`cache.delete`) lors des modifications importantes, souvent via `transaction.on_commit`.

### À retenir

- Messages = notifications à usage unique, affichées après redirection.
- Cache : choisir le **niveau** adapté, **Redis** en production, clés **variantes**, durée de vie obligatoire.
- Un cache mal clé peut **servir la page d'un utilisateur à un autre** : vérifiez toujours la variation.

---

## 14. Fichiers statiques et médias

### Objectifs d'apprentissage

Distinguer **statiques** et **médias** ; configurer `STATIC_*` / `MEDIA_*` ; servir les statiques en production (WhiteNoise, Nginx, CDN) ; gérer les médias (noms sûrs, stockage cloud avec `django-storages`) ; sécuriser les téléversements ; dépanner les problèmes courants.

### 14.1 Deux notions distinctes

|  | **Statiques** | **Médias** |
| --- | --- | --- |
| Contenu | CSS, JS, images du **site** | Fichiers **envoyés par les utilisateurs** |
| Source | Dépôt de code | Formulaires, admin |
| Réglages | `STATIC_URL`, `STATIC_ROOT`, `STATICFILES_DIRS` | `MEDIA_URL`, `MEDIA_ROOT` |
| Sécurité | Publics | **À valider** (taille, type, noms) |

### 14.2 Fichiers statiques

```python
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]           # sources globales
STATIC_ROOT = BASE_DIR / "staticfiles"             # cible de collectstatic (production)
```

```django
{% load static %}
<link rel="stylesheet" href="{% static 'css/site.css' %}">
<img src="{% static 'img/logo.svg' %}" alt="Logo">
```

```bash
python manage.py collectstatic --noinput           # copie tous les statiques vers STATIC_ROOT
```

Les **finders** de `staticfiles` cherchent les fichiers dans `STATICFILES_DIRS` et dans le dossier `static/` de chaque app. `collectstatic` les **rassemble** (y compris ceux de l'admin et des paquets tiers) dans `STATIC_ROOT`, dossier que le serveur web publie. En **développement**, `runserver` sert les statiques automatiquement (si `DEBUG = True`). En **production**, **jamais** par Django lui-même.

#### Servir les statiques en production

| Solution | Quand |
| --- | --- |
| **WhiteNoise** | Simple : servi par l'application avec compression et empreintes |
| **Nginx / Caddy** | Serveur web frontal (performances maximales) |
| **CDN** (CloudFront, Cloudflare) + stockage S3 | Trafic important |

```python
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STORAGES = {"staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"}}   # fichiers hachés + compression
```

Le stockage « **Manifest** » ajoute une **empreinte** au nom (`site.3f9a1c.css`) : on peut alors les mettre en cache « pour toujours » côté navigateur, car tout changement produit un nouveau nom (*cache busting*). WhiteNoise doit être placé **juste après** `SecurityMiddleware`.

### 14.3 Fichiers médias

```python
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
```

```python
# apps/blog/models.py
import uuid
from pathlib import Path

from django.db import models

# Nom de fichier sûr et unique
def chemin_avatar(instance, nom):
    return f"avatars/{instance.pk}/{uuid.uuid4().hex}{Path(nom).suffix.lower()}"

class Document(models.Model):
    fichier = models.FileField(upload_to="documents/%Y/%m/")
    image = models.ImageField(upload_to="images/", blank=True)        # nécessite Pillow
    avatar = models.ImageField(upload_to=chemin_avatar, blank=True)
```

```django
<img src="{{ document.image.url }}" alt="">
```

- `upload_to` accepte un chemin (avec `strftime` : `%Y/%m/`) ou une **fonction** qui produit un nom sûr (ne réutilisez pas le nom fourni par l'utilisateur).
- `fichier.url`, `fichier.path`, `fichier.size`, `fichier.name` : attributs d'un `FieldFile`.
- Un `ImageField` stocke seulement le **chemin** ; le fichier vit dans le stockage (`default` de `STORAGES`).

#### Stockage dans le cloud : `django-storages`

```python
STORAGES = {
    "default": {"BACKEND": "storages.backends.s3.S3Storage",
                "OPTIONS": {"bucket_name": env("S3_BUCKET"), "region_name": "eu-west-3"}},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}
```

Compatible **Amazon S3**, **Cloudflare R2**, **Google Cloud Storage**, **Azure**, **MinIO**… Servez les médias **privés** par **URL signées** (`querystring_auth`), à durée limitée. Avantage du cloud : pas de disque local à sauvegarder, plusieurs instances d'application partagent les mêmes fichiers.

### 14.4 Sécurité des fichiers téléversés

- Limiter **taille** (`DATA_UPLOAD_MAX_MEMORY_SIZE`, `FILE_UPLOAD_MAX_MEMORY_SIZE`) et **type** (validation du **contenu réel** avec `python-magic` / Pillow, pas seulement l'extension).
- **Renommer** les fichiers (pas de nom fourni par l'utilisateur : risque de traversée de chemin), stocker **hors** de la racine web ou sur un stockage dédié.
- **Ne jamais exécuter** ni servir en `text/html` un fichier utilisateur (risque XSS) ; en-tête `X-Content-Type-Options: nosniff`.
- Fichiers **privés** : vue protégée qui renvoie un `FileResponse` (ou `X-Accel-Redirect` avec Nginx).

### 14.5 Dépanner

| Symptôme | Cause |
| --- | --- |
| Statiques absents en production | `collectstatic` oublié, `STATIC_ROOT` incorrect, serveur non configuré |
| `ValueError: Missing staticfiles manifest entry` | Fichier absent lors de `collectstatic` avec stockage « Manifest » |
| Médias en 404 en développement | `static(MEDIA_URL, …)` manquant dans `urls.py` |
| Images non traitées | **Pillow** non installé |

### À retenir

- **Statiques** = fichiers du site, collectés et servis par WhiteNoise/Nginx/CDN ; **médias** = fichiers utilisateurs, **à ne jamais faire confiance**.
- Stockage cloud avec `django-storages` ; noms générés ; URL signées pour le privé.

---

## 15. Middleware

### Objectifs d'apprentissage

Comprendre le modèle en « oignon » des middlewares ; connaître les middlewares intégrés ; écrire un middleware (classe, hooks, version sync/async) ; maîtriser l'ordre ; savoir quand **ne pas** en écrire.

### 15.1 Principe

> **Définition.** Un **middleware** est une couche qui **intercepte** chaque requête **avant** qu'elle atteigne la vue, et chaque réponse **après** la vue. Les middlewares sont empilés comme des couches d'oignon.

```text
Requête  → SecurityMiddleware → Session → Auth → … → VUE
Réponse  ← SecurityMiddleware ← Session ← Auth ← … ←
```

Chaque middleware peut : **modifier la requête**, **court-circuiter** (renvoyer directement une réponse sans appeler la suite), **modifier la réponse**, ou **capter une exception**.

### 15.2 Middlewares intégrés importants

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
| `ConditionalGetMiddleware` | ETag, réponses 304 |

### 15.3 Écrire un middleware

```python
# apps/accueil/middleware.py
import logging
import time

logger = logging.getLogger(__name__)

class ChronoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response                      # initialisation (une seule fois, au démarrage)

    def __call__(self, request):
        debut = time.perf_counter()
        reponse = self.get_response(request)                  # appelle la suite (autres middlewares + vue)
        duree = (time.perf_counter() - debut) * 1000
        reponse["X-Temps-Ms"] = f"{duree:.1f}"
        if duree > 500:
            logger.warning("Requête lente : %s %s (%.0f ms)", request.method, request.path, duree)
        return reponse

    def process_view(self, request, view_func, view_args, view_kwargs):
        return None                                           # avant la vue (facultatif)

    def process_exception(self, request, exception):
        return None                                           # si la vue lève une exception

    def process_template_response(self, request, response):
        return response

# settings.py : MIDDLEWARE += ["apps.accueil.middleware.ChronoMiddleware"]
```

- `__init__` s'exécute **une fois** (au démarrage) ; `__call__` s'exécute **à chaque requête**. Le code **avant** `get_response` est la phase « requête » ; le code **après**, la phase « réponse ».
- Hooks facultatifs : `process_view` (juste avant la vue), `process_exception`, `process_template_response`.
- Ne conservez pas d'état par requête dans `self` : une seule instance sert toutes les requêtes (et plusieurs threads).

#### Middleware compatible sync / async

```python
from asgiref.sync import iscoroutinefunction, markcoroutinefunction

class MonMiddleware:
    sync_capable = True
    async_capable = True

    def __init__(self, get_response):
        self.get_response = get_response
        if iscoroutinefunction(get_response):
            markcoroutinefunction(self)

    def __call__(self, request):
        if iscoroutinefunction(self):
            return self.__acall__(request)
        return self.get_response(request)

    async def __acall__(self, request):
        return await self.get_response(request)
```

Un middleware **synchrone** placé dans une pile asynchrone force des **conversions** thread ↔ boucle coûteuses : déclarez `sync_capable` et `async_capable` pour éviter ces passages.

### 15.4 Ordre et bonnes pratiques

- **Ordre** : sécurité / statiques en premier, puis sessions → auth → le reste. Un middleware qui dépend de `request.user` doit être **après** `AuthenticationMiddleware`.
- Gardez les middlewares **rapides** : ils s'exécutent à **chaque** requête (y compris les statiques en développement).
- **Pas de logique métier** : un middleware sert des **préoccupations transversales** (journaux, en-têtes, authentification, détection de locataire/*tenant*).
- Déboguez avec `django-debug-toolbar` et en **commentant** progressivement les middlewares suspects.

### À retenir

- Un middleware = fonction/classe qui enveloppe le traitement de **toutes** les requêtes ; **l'ordre compte**.
- Si le besoin ne concerne qu'une vue, préférez un **décorateur** ou un mixin.

---

## 16. Signaux

### Objectifs d'apprentissage

Comprendre le motif *observateur* et les signaux de Django ; brancher un récepteur correctement (`@receiver`, `ready()`) ; créer un signal personnalisé ; connaître les pièges (`bulk_*`, boucles, lenteur) et les alternatives (services explicites).

### 16.1 Principe

> **Définition.** Un **signal** est un mécanisme de notification découplé (motif **observateur**) : un **émetteur** (*sender*) annonce qu'un événement s'est produit ; des **récepteurs** (*receivers*) enregistrés réagissent, sans que l'émetteur les connaîsse.

| Signal | Quand |
| --- | --- |
| `pre_save` / `post_save` | Avant / après `save()` |
| `pre_delete` / `post_delete` | Suppression |
| `m2m_changed` | Modification d'une relation ManyToMany |
| `request_started` / `request_finished` | Cycle de requête |
| `user_logged_in` / `user_logged_out` / `user_login_failed` | Authentification |
| `post_migrate` | Après `migrate` |

### 16.2 Utilisation

```python
# apps/comptes/signals.py
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profil

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def creer_profil(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(utilisateur=instance)
```

```python
# apps/comptes/apps.py
from django.apps import AppConfig

class ComptesConfig(AppConfig):
    name = "apps.comptes"

    def ready(self):
        from . import signals  # noqa: F401      # sinon le récepteur n'est jamais branché
```

- Un récepteur reçoit toujours `sender`, `**kwargs` ; pour `post_save` : `instance`, `created` (booléen), `raw`, `update_fields`.
- Le récepteur n'est actif que si le module qui le contient est **importé** : d'où l'import dans `ready()` (cause n°1 du « mon signal ne se déclenche pas »).
- `sender=` limite le récepteur à un modèle ; sans lui, il réagit à **tous** les modèles.

#### Signal personnalisé

```python
# apps/boutique/signals.py
from django.dispatch import Signal, receiver

from .models import Commande

commande_payee = Signal()                                   # (plus de providing_args)

@receiver(commande_payee)
def prevenir_client(sender, commande, **kwargs):
    print(f"Commande {commande.pk} payée")

# python manage.py shell
commande = Commande.objects.create()
commande_payee.send(sender=Commande, commande=commande)     # affiche : Commande <identifiant> payée
```

`Signal.send()` appelle les récepteurs **de façon synchrone, dans l'ordre**, et une exception d'un récepteur remonte à l'appelant ; `send_robust()` capture les exceptions. Il existe aussi `asend` pour les récepteurs asynchrones.

### 16.3 Précautions et alternatives

| Piège | Remède |
| --- | --- |
| Logique **cachée** (difficile à suivre) | Préférez un **appel explicite** (méthode du modèle, service) |
| `bulk_create`, `update()` **ne déclenchent pas** `post_save` | Appeler explicitement |
| Boucles infinies (un récepteur re-sauvegarde l'objet) | `update_fields`, gardes |
| Travail lent dans le récepteur | **Tâche en arrière-plan** (section 23) avec `transaction.on_commit` |
| Tests difficiles | Tester le récepteur comme une fonction |

> **Règle** : utilisez les signaux pour **découpler des apps** (ex. : une app tierce réagit à la création d'un utilisateur) ; **sinon** préférez les **services explicites**, plus faciles à lire, à déboguer et à tester.

### À retenir

- Signal = notification découplée ; récepteur branché dans `ready()`.
- Les opérations en lot ne déclenchent pas `post_save`.
- Dans votre propre code, un appel de service explicite vaut presque toujours mieux.

---

## 17. Internationalisation et localisation

### Objectifs d'apprentissage

Distinguer i18n, l10n et fuseaux horaires ; configurer langues et chemins de traduction ; marquer les textes (Python et templates, pluriels) ; extraire, traduire et compiler les messages ; internationaliser les URL ; traduire le contenu des modèles ; gérer correctement les fuseaux horaires.

### 17.1 Principes

| Terme | Signification |
| --- | --- |
| **i18n** (*internationalization*) | Rendre le site **traduisible** (marquer les textes, structurer) |
| **l10n** (*localization*) | Adapter à une **langue / région** (traductions, formats de date, de nombre) |
| **Fuseaux horaires** | `USE_TZ = True`, `zoneinfo` |

```python
LANGUAGE_CODE = "fr"
LANGUAGES = [("fr", "Français"), ("en", "English")]
LOCALE_PATHS = [BASE_DIR / "locale"]
USE_I18N = True
# MIDDLEWARE : ajouter "django.middleware.locale.LocaleMiddleware" juste après SessionMiddleware
```

`LocaleMiddleware` choisit la langue de chaque requête selon, dans l'ordre : le préfixe d'URL, le cookie de langue, l'en-tête `Accept-Language` du navigateur, puis `LANGUAGE_CODE`.

### 17.2 Marquer les textes

```python
# apps/blog/models.py
from django.db import models
from django.utils.translation import gettext_lazy

class Article(models.Model):
    titre = models.CharField(gettext_lazy("titre"), max_length=200)    # gettext_lazy : traduit à l'affichage
```

```python
# python manage.py shell
from django.utils.translation import gettext as _, ngettext

print(_("Bienvenue"))                                                # traduit à l'appel
n = 3
print(ngettext("%(n)d article", "%(n)d articles", n) % {"n": n})     # pluriels : 3 articles
```

```django
{% load i18n %}
{% translate "Bienvenue" %}
{% blocktranslate count n=articles|length %}{{ n }} article{% plural %}{{ n }} articles{% endblocktranslate %}
```

| Fonction | Usage |
| --- | --- |
| `gettext` (`_`) | Traduction immédiate (dans une vue ou une fonction) |
| **`gettext_lazy`** | Traduction **différée** : obligatoire pour les attributs de classe (modèles, formulaires, constantes) qui sont évalués à l'import, avant que la langue de la requête soit connue |
| `ngettext` | Pluriels (certaines langues ont plus de deux formes) |
| `pgettext` | Traduction avec **contexte** (distinguer deux sens d'un même mot) |
| `{% translate %}`, `{% blocktranslate %}` | Équivalents pour les templates |

### 17.3 Extraire, traduire, compiler

```bash
python manage.py makemessages -l en -l fr --ignore=.venv      # crée locale/<langue>/LC_MESSAGES/django.po
# → traduire les msgstr dans django.po (Poedit, Weblate, Transifex)
python manage.py compilemessages                              # produit django.mo
```

> Nécessite **GNU gettext** installé (`apt install gettext` / `brew install gettext`).

Le fichier **`.po`** (*Portable Object*) liste les paires `msgid` (texte source) / `msgstr` (traduction) ; le **`.mo`** est sa version binaire compilée, celle qu'utilise Django. Relancez `makemessages` après chaque ajout de texte, puis `compilemessages`.

### 17.4 URLs, sélecteur de langue, formats

```python
# config/urls.py (à la suite de urlpatterns)
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path

urlpatterns += i18n_patterns(path("", include("apps.blog.urls")), prefix_default_language=False)
urlpatterns += [path("i18n/", include("django.conf.urls.i18n"))]      # vue set_language
```

La vue `set_language` reçoit un `POST` avec la langue choisie et enregistre la préférence dans un cookie. Formats localisés : `{{ valeur|date:"DATE_FORMAT" }}`, `{{ nombre|floatformat:2 }}` ; balises `localize` / `unlocalize`.

### 17.5 Traduire le contenu des **modèles**

| Paquet | Approche |
| --- | --- |
| **`django-modeltranslation`** | Colonnes supplémentaires par langue (`titre_fr`, `titre_en`) |
| **`django-parler`** | Table de traductions séparée |
| **`django-rosetta`** | Interface web pour éditer les `.po` |

Django traduit l'**interface** (gettext) ; le **contenu** saisi en base (titres d'articles) n'est pas traduit automatiquement, d'où ces paquets.

### 17.6 Fuseaux horaires

```python
from django.utils import timezone

maintenant = timezone.now()
print(maintenant)                                  # datetime « aware » en UTC
print(timezone.localtime(maintenant))              # converti vers le fuseau actif
with timezone.override("Indian/Antananarivo"):
    print(timezone.localtime(maintenant))          # converti vers un autre fuseau
```

**Règle** : stockez en **UTC** (`USE_TZ = True`) ; convertissez **à l'affichage** selon le fuseau de l'utilisateur. Utilisez `timezone.now()` plutôt que `datetime.now()` (qui est *naïf*).

### À retenir

- **Marquez** (`gettext`/`_lazy`), **extrayez** (`makemessages`), **traduisez** (`.po`), **compilez** (`compilemessages`).
- `gettext_lazy` pour tout ce qui est défini à l'import ; UTC en base, conversion à l'affichage.

---

## 18. Commandes de gestion personnalisées

### Objectifs d'apprentissage

Créer une commande `manage.py` (arguments, sorties colorées, erreurs) ; savoir quand en utiliser une ; la rendre **idempotente** et journalisée ; l'appeler depuis le code ; choisir entre commande, cron et file de tâches.

### 18.1 Créer une commande

Une **commande de gestion** est un script exécutable via `python manage.py <nom>` avec **tout l'environnement Django chargé** (modèles, réglages).

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
        if options["jours"] < 1:
            raise CommandError("Le nombre de jours doit être positif.")
        limite = timezone.now() - timedelta(days=options["jours"])
        qs = Article.objects.filter(statut="publie", publie_le__lt=limite)
        if options["dry_run"]:
            self.stdout.write(f"{qs.count()} article(s) seraient archivés.")
            return
        n = qs.update(statut="archive")
        self.stdout.write(self.style.SUCCESS(f"{n} article(s) archivé(s)."))
```

```bash
python manage.py archiver_articles --jours 180 --dry-run
```

- Le **nom du fichier** devient le nom de la commande ; la classe doit s'appeler `Command`.
- `add_arguments` utilise `argparse` (options, valeurs par défaut, aide automatique `--help`).
- `handle()` contient la logique ; `CommandError` produit un message propre et un code de sortie non nul ; `self.stdout.write` et `self.style.SUCCESS/WARNING/ERROR` gèrent l'affichage coloré.
- Le paramètre `--dry-run` (simulation) est une excellente habitude pour toute opération destructive.

### 18.2 Usages

| Usage | Exemple |
| --- | --- |
| **Tâches planifiées** (cron, Kubernetes CronJob) | Nettoyage, rapports, synchronisations |
| **Import / export** de données | CSV, API externes |
| **Maintenance** | Réindexation, recalcul de champs |
| **Démarrage** | Création de données initiales (`loaddata`, fixtures) |

> Rendez les commandes **idempotentes** (rejouables sans dommage) et **journalisées** ; pour des traitements longs, répétés ou déclenchés par l'utilisateur, préférez une **file de tâches** (section 23). Appel depuis le code (tests, autres commandes) : `call_command("archiver_articles", jours=30)`.

### À retenir

- Un fichier `management/commands/<nom>.py` + une classe `Command` suffisent.
- Prévoyez `--dry-run`, des messages clairs et l'idempotence.

---

# API, asynchrone et frontend

---

## 19. API REST avec Django REST Framework

### Objectifs d'apprentissage

Comprendre ce qu'est une API REST et le rôle de DRF ; écrire des **sérialiseurs** (validation, relations), des **vues et ViewSets**, des **routeurs** ; configurer **pagination, filtrage, tri, recherche, limitation de débit, versionnement** et gestion d'erreurs ; documenter avec **OpenAPI** ; tester une API ; appliquer les bonnes pratiques (N+1, sécurité).

### 19.1 Pourquoi DRF ?

> **Définition — API REST.** Une interface de programmation qui expose des **ressources** (articles, commandes) identifiées par des **URL**, manipulées avec les **verbes HTTP** (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) et échangées le plus souvent en **JSON**, de façon **sans état** (chaque requête porte tout ce qu'il faut, y compris l'authentification).

**Django REST Framework** (DRF) est la bibliothèque de référence pour construire des API REST avec Django : **sérialiseurs**, **vues génériques**, **routeurs**, authentification, permissions, pagination, filtrage, limitation de débit, documentation, **API navigable** dans le navigateur.

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

Ce dictionnaire fixe les **réglages globaux** : qui peut appeler (`authentication`, `permission`), comment on pagine, quels filtres sont disponibles, combien de requêtes sont tolérées par minute, et comment générer le schéma OpenAPI. Chaque vue peut les surcharger.

### 19.2 Sérialiseurs

Un **sérialiseur** convertit **objets ↔ JSON** et **valide** les entrées (rôle comparable à celui d'un formulaire pour une API).

```python
# apps/blog/serializers.py
from rest_framework import serializers
from .models import Article, Categorie

class ArticleSerializer(serializers.ModelSerializer):
    auteur = serializers.StringRelatedField(read_only=True)
    categories = serializers.SlugRelatedField(slug_field="slug", many=True, queryset=Categorie.objects.all(), required=False)
    nb_commentaires = serializers.IntegerField(read_only=True)       # annotation du QuerySet

    class Meta:
        model = Article
        fields = ["id", "titre", "slug", "contenu", "auteur", "categories", "statut", "publie_le", "nb_commentaires"]
        read_only_fields = ["id", "publie_le"]

    def validate_titre(self, valeur: str) -> str:                    # validation d'un champ
        if len(valeur) < 5:
            raise serializers.ValidationError("Titre trop court.")
        return valeur

    def validate(self, attrs):                                       # validation globale
        if attrs.get("statut") == "publie" and not attrs.get("contenu"):
            raise serializers.ValidationError("Contenu requis pour publier.")
        return attrs
```

- **Sérialisation** (objet → JSON) : `ArticleSerializer(article).data`. **Désérialisation** (JSON → données validées) : `ArticleSerializer(data=request.data)`, puis `is_valid()` et `serializer.save()`.
- **Champs de relation** : `StringRelatedField` (représentation texte), `SlugRelatedField` (un slug), `PrimaryKeyRelatedField` (identifiant), sérialiseur imbriqué (objet complet), `HyperlinkedRelatedField` (URL).
- `read_only_fields` : acceptés en sortie, ignorés en entrée (protection contre le *mass assignment*).
- `nb_commentaires` est calculé par **annotation** dans la vue : on évite une requête par objet.

### 19.3 Vues et ViewSets

```python
# apps/blog/views_api.py
from django.db.models import Count
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer

class EstAuteurOuLectureSeule(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.auteur == request.user

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, EstAuteurOuLectureSeule]
    filterset_fields = ["statut", "categories__slug", "auteur"]
    search_fields = ["titre", "contenu"]
    ordering_fields = ["publie_le", "titre"]

    def get_queryset(self):                                          # optimiser ici (N+1)
        return (Article.objects.select_related("auteur").prefetch_related("categories")
                .annotate(nb_commentaires=Count("commentaires")))

    def perform_create(self, serializer):
        serializer.save(auteur=self.request.user)

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def publier(self, request, pk=None):                             # POST /articles/{id}/publier/
        article = self.get_object()
        article.publier()
        return Response({"statut": article.statut})
```

| Niveau | Classes |
| --- | --- |
| Bas niveau | `APIView` (comme une CBV) |
| Génériques | `ListAPIView`, `RetrieveUpdateDestroyAPIView`, `ListCreateAPIView`… |
| **ViewSets** | `ModelViewSet`, `ReadOnlyModelViewSet`, `GenericViewSet` + mixins |
| Fonctions | `@api_view(["GET", "POST"])` |

Un **ViewSet** regroupe les actions d'une ressource (`list`, `retrieve`, `create`, `update`, `partial_update`, `destroy`) en une classe ; un **routeur** en déduit les URL. `@action` ajoute des routes personnalisées. `perform_create` est le point d'extension pour compléter les données (ici l'auteur, qu'on **ne lit jamais** dans le corps de la requête). Les **permissions de niveau objet** (`has_object_permission`) ne s'appliquent que lorsque la vue appelle `get_object()`.

### 19.4 Routeurs

```python
# apps/blog/urls_api.py
from rest_framework.routers import DefaultRouter
from .views_api import ArticleViewSet

router = DefaultRouter()
router.register("articles", ArticleViewSet, basename="article")

urlpatterns = router.urls

# config/urls.py
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns += [
    path("api/v1/", include("apps.blog.urls_api")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema")),
]
```

Routes générées : `GET/POST /articles/`, `GET/PUT/PATCH/DELETE /articles/{id}/`, plus les `@action` (ex. `POST /articles/{id}/publier/`). `DefaultRouter` ajoute aussi une page racine listant les ressources.

### 19.5 Pagination, filtrage, tri, recherche

```python
# apps/blog/pagination.py
from rest_framework.pagination import CursorPagination

class PaginationCurseur(CursorPagination):                 # stable et rapide sur de gros volumes
    page_size = 20
    ordering = "-publie_le"
```

```python
# apps/blog/filters.py (django-filter : filtres personnalisés)
import django_filters
from .models import Article

class ArticleFilter(django_filters.FilterSet):
    depuis = django_filters.DateTimeFilter(field_name="publie_le", lookup_expr="gte")
    titre = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Article
        fields = ["statut", "auteur"]
```

Branchement dans `ArticleViewSet` : `filterset_class = ArticleFilter` (à la place de `filterset_fields`) et `pagination_class = PaginationCurseur`. URL d'exemple : `/api/v1/articles/?statut=publie&search=django&ordering=-publie_le&page=2`.

| Pagination | Principe | Quand |
| --- | --- | --- |
| `PageNumberPagination` | `?page=2` | Interfaces avec numéros de pages |
| `LimitOffsetPagination` | `?limit=20&offset=40` | Flexibilité ; lente sur de grands `offset` |
| **`CursorPagination`** | Curseur opaque basé sur l'ordre | **Gros volumes**, flux, pas de saut de pages |

### 19.6 Limitation de débit, versionnement, erreurs

```python
# config/api.py
from rest_framework.views import exception_handler

def gestionnaire_erreurs(exc, context):                     # format d'erreur uniforme
    reponse = exception_handler(exc, context)
    if reponse is not None:
        reponse.data = {"erreur": {"code": reponse.status_code, "details": reponse.data}}
    return reponse
```

```python
# settings.py
REST_FRAMEWORK["DEFAULT_VERSIONING_CLASS"] = "rest_framework.versioning.NamespaceVersioning"   # /api/v1/ · /api/v2/
REST_FRAMEWORK["EXCEPTION_HANDLER"] = "config.api.gestionnaire_erreurs"
```

Le **throttling** limite le nombre de requêtes par client (réponse `429`) ; réglages par vue : `throttle_classes`, `throttle_scope`. Le **versionnement** permet de faire évoluer l'API sans casser les clients existants. Format d'erreur standard recommandé : **RFC 9457** (*Problem Details*) ; l'important est la **cohérence** d'un format unique.

### 19.7 Documentation OpenAPI

```python
# settings.py
SPECTACULAR_SETTINGS = {"TITLE": "Mon API", "VERSION": "1.0.0", "SERVE_INCLUDE_SCHEMA": False}
```

```python
# apps/blog/views_api.py
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerializer

class ArticlesPublies(APIView):
    @extend_schema(parameters=[OpenApiParameter("q", str, description="Recherche")],
                   responses=ArticleSerializer(many=True))
    def get(self, request):
        articles = Article.objects.publies().filter(titre__icontains=request.GET.get("q", ""))
        return Response(ArticleSerializer(articles, many=True).data)
```

```bash
python manage.py spectacular --file schema.yml     # export OpenAPI 3 ; génération de clients (openapi-generator, orval)
```

**OpenAPI** est une description normalisée de l'API (points d'accès, paramètres, schémas). Elle alimente la documentation interactive (Swagger UI, ReDoc) et permet de **générer des clients** typés (TypeScript, Python…).

### 19.8 Tests d'API

```python
# apps/blog/tests/test_api.py
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()

class ArticleAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("alice", "alice@exemple.fr", "x")
        self.client.force_authenticate(self.user)

    def test_creation(self):
        donnees = {"titre": "Titre valide", "slug": "titre-valide", "contenu": "…", "statut": "brouillon"}
        r = self.client.post("/api/v1/articles/", donnees, format="json")
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        self.assertEqual(r.data["auteur"], str(self.user))

    def test_anonyme_ne_peut_pas_creer(self):
        self.client.force_authenticate(None)
        self.assertEqual(self.client.post("/api/v1/articles/", {}).status_code, 401)
```

### 19.9 Bonnes pratiques DRF

- **Optimisez** `get_queryset()` (`select_related`, `prefetch_related`, annotations) : le **N+1** est le piège n°1 (un sérialiseur qui accède à une relation l'exécute pour chaque objet).
- Séparez les sérialiseurs de **lecture** et d'**écriture** si nécessaire (`get_serializer_class`).
- **Versionnez** l'API, **paginez** toujours les listes, **limitez** le débit.
- Ne divulguez pas d'**identifiants séquentiels** sensibles (UUID / slug) ni de champs internes ; vérifiez la **propriété** des objets (IDOR).
- Documentez avec **drf-spectacular** et testez avec `APIClient`.

### À retenir

- DRF = sérialiseurs (validation) + ViewSets (actions) + routeurs (URL) + réglages globaux.
- Pagination, filtres, throttling et versionnement sont des **fondamentaux**, pas des options.
- Optimisez le QuerySet ; testez les cas refusés.

---

## 20. Authentification des API : JWT et alternatives

*(Section ajoutée : JWT et jetons étaient absents du guide d'origine.)*

### Objectifs d'apprentissage

Choisir une méthode d'authentification adaptée à l'application ; comprendre la structure et les limites d'un **JWT** ; configurer `djangorestframework-simplejwt` (jetons d'accès et de rafraîchissement, rotation, liste noire) ; stocker les jetons côté client de façon sûre ; configurer CORS et CSRF pour un front séparé.

### 20.1 Quelle méthode choisir ?

| Méthode | Principe | Idéal pour | Remarques |
| --- | --- | --- | --- |
| **Session + cookie** (+ CSRF) | Cookie `HttpOnly` géré par Django | **SPA du même domaine**, applications web | Simple et sûr ; protéger contre le CSRF |
| **Jeton DRF (`TokenAuthentication`)** | Un jeton **opaque** stocké en base | Scripts, services internes | Pas d'expiration native, un jeton par utilisateur |
| **JWT** (*JSON Web Token*) | Jeton **signé** et **autoporteur** (accès court + rafraîchissement) | Applications **mobiles**, **SPA** multi-domaines, microservices | **Sans état** côté serveur ; révocation à gérer (liste noire) |
| **OAuth 2.0 / OpenID Connect** | Délégation à un fournisseur d'identité | **SSO**, API publiques, « se connecter avec… » | `django-oauth-toolkit`, `django-allauth` |
| **Clé d'API** | Secret statique par client | Intégrations serveur-à-serveur | `djangorestframework-api-key` |

> **Définition — JWT.** Un **JSON Web Token** est une chaîne `en-tête.charge_utile.signature`, chaque partie étant encodée en Base64URL. L'**en-tête** indique l'algorithme, la **charge utile** (*payload*) contient des **revendications** (*claims* : `sub` sujet, `exp` expiration, `iat` émission, vos champs), la **signature** garantit l'intégrité. Le serveur peut vérifier un jeton **sans consulter la base** (d'où « sans état »). **Il est encodé, pas chiffré** : tout le monde peut lire son contenu.

### 20.2 JWT avec `djangorestframework-simplejwt`

```bash
uv add djangorestframework-simplejwt
```

```python
# settings.py
from datetime import timedelta

REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] = ["rest_framework_simplejwt.authentication.JWTAuthentication"]

INSTALLED_APPS += ["rest_framework_simplejwt", "rest_framework_simplejwt.token_blacklist"]   # blacklist : révocation des refresh

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),        # court !
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,                         # un nouveau refresh à chaque renouvellement
    "BLACKLIST_AFTER_ROTATION": True,                      # l'ancien refresh est révoqué
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": "HS256",                                  # ou RS256 / ES256 avec clés publique/privée
    "SIGNING_KEY": SECRET_KEY,                             # idéalement une clé DÉDIÉE
    "AUTH_HEADER_TYPES": ("Bearer",),
}
```

```python
# config/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns += [
    path("api/auth/jeton/", TokenObtainPairView.as_view(), name="jeton"),         # POST {username, password} → {access, refresh}
    path("api/auth/jeton/rafraichir/", TokenRefreshView.as_view(), name="jeton-refresh"),
    path("api/auth/jeton/verifier/", TokenVerifyView.as_view()),
    path("api/auth/deconnexion/", TokenBlacklistView.as_view()),                  # révoque un refresh
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

**Flux complet :** (1) le client envoie identifiants → (2) reçoit **access** (court, 10 min) et **refresh** (long, 7 jours) → (3) envoie `Authorization: Bearer <access>` sur chaque appel → (4) quand l'access expire (`401`), il présente le **refresh** pour en obtenir un nouveau → (5) à la déconnexion, le refresh est mis sur **liste noire**. Pourquoi deux jetons ? Un access volé est dangereux peu de temps ; le refresh, plus précieux, circule rarement et peut être révoqué.

#### Personnaliser le contenu du jeton

```python
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MonSerializerJeton(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["nom"] = user.get_full_name()                  # revendications : peu de données, jamais de secrets
        token["roles"] = list(user.groups.values_list("name", flat=True))
        return token

class MonJetonView(TokenObtainPairView):
    serializer_class = MonSerializerJeton
```

**Connexion par e-mail** : définissez `USERNAME_FIELD = "email"` sur le modèle utilisateur ; le sérialiseur l'utilise automatiquement.

### 20.3 Où stocker les jetons côté client ?

| Stockage | Risque | Avis |
| --- | --- | --- |
| `localStorage` / `sessionStorage` | **Lisible par n'importe quel script** (XSS) | À éviter pour le refresh token |
| **Cookie `HttpOnly` + `Secure` + `SameSite`** | Non lisible par JS ; protéger du CSRF | Recommandé pour le **refresh** (ou les deux) |
| Mémoire JS (variable) | Perdu au rechargement | Pour l'**access token** de courte durée |
| Mobile : Keychain / Keystore | — | Recommandé |

> `simplejwt` ne gère **pas** les cookies nativement : utilisez un paquet dédié (ex. **`dj-rest-auth`** avec `JWT_AUTH_COOKIE`, ou **`django-allauth` headless**) ou écrivez des vues qui posent le refresh en cookie `HttpOnly`.

### 20.4 Bonnes pratiques JWT

- **Access court** (5–15 min) + **refresh** plus long, **rotation** et **liste noire**.
- **HTTPS obligatoire** ; clé de signature **secrète et dédiée** (ou **RS256/ES256** pour des clients qui vérifient sans connaître le secret).
- **Ne mettez pas de données sensibles** dans le jeton : il est **encodé, pas chiffré**.
- Vérifiez **`exp`**, `iss`, `aud` ; prévoyez la **révocation** (changement de mot de passe, déconnexion).
- Un JWT n'est **pas** toujours le bon choix : pour une application web classique ou une SPA du même domaine, les **sessions + cookies** sont plus simples et plus sûres.

### 20.5 Alternatives et compléments

| Paquet | Rôle |
| --- | --- |
| **`dj-rest-auth`** | Points d'accès prêts : connexion, déconnexion, inscription, réinitialisation, JWT/cookies (s'appuie sur allauth) |
| **`django-allauth` (headless)** | API d'authentification complète (sessions ou jetons), réseaux sociaux, 2FA, passkeys |
| **`django-rest-knox`** | Jetons **opaques** hachés, **un par appareil**, expiration, révocation |
| **`django-oauth-toolkit`** | Serveur **OAuth 2.0 / OIDC** |
| **`djangorestframework-api-key`** | Clés d'API par client |
| **`django-ninja-jwt`** | JWT pour **Django Ninja** (port de simplejwt) |
| **`PyJWT`** | Bibliothèque de bas niveau (encoder / décoder des JWT) |

### 20.6 CORS et API consommées par un front séparé

> **Définition — CORS** (*Cross-Origin Resource Sharing*). Mécanisme du navigateur qui bloque, par défaut, les requêtes JavaScript vers une **autre origine** (schéma + domaine + port). Le serveur doit autoriser explicitement les origines de confiance par des en-têtes de réponse.

```bash
uv add django-cors-headers
```

```python
INSTALLED_APPS += ["corsheaders"]
MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")      # avant CommonMiddleware
CORS_ALLOWED_ORIGINS = ["https://app.exemple.fr", "http://localhost:5173"]
CORS_ALLOW_CREDENTIALS = True                                      # uniquement si cookies / sessions
CSRF_TRUSTED_ORIGINS = ["https://app.exemple.fr"]
```

> **N'utilisez jamais** `CORS_ALLOW_ALL_ORIGINS = True` en production, surtout avec `CORS_ALLOW_CREDENTIALS = True`. CORS **ne remplace pas** l'authentification : c'est une protection du **navigateur**, pas du serveur.

### 20.7 Sessions + CSRF pour une SPA du même site

```python
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_HTTPONLY = False          # le JS doit lire le cookie csrftoken pour l'envoyer en en-tête X-CSRFToken
```

Le client envoie `X-CSRFToken` sur les requêtes modifiantes ; DRF `SessionAuthentication` applique la vérification CSRF.

### À retenir

- Application web / SPA même domaine : **sessions + CSRF**. Mobile ou multi-domaines : **JWT court + refresh** en rotation.
- Un JWT est **lisible** par tous ; stockez le refresh dans un cookie `HttpOnly` ou le trousseau sécurisé.
- **CORS** est restrictif par liste blanche ; jamais ouvert à tous.

---

## 21. Django Ninja, GraphQL et API externes

*(Section ajoutée : frameworks et approches complémentaires.)*

### Objectifs d'apprentissage

Écrire une API typée avec **Django Ninja** et la comparer à DRF ; comprendre les principes de **GraphQL** et le rôle de Strawberry ; **consommer des API externes** de façon robuste (délais, erreurs, cache, tests) ; recevoir des **webhooks** en sécurité.

### 21.1 Django Ninja : API typées, façon FastAPI

**Django Ninja** utilise les **annotations de types** Python et **Pydantic** : peu de code, validation automatique, **OpenAPI** intégrée, support **async**. Le type d'un paramètre décrit à la fois sa **validation** et sa **documentation**.

```bash
uv add django-ninja
```

```python
# apps/blog/api.py
from django.utils.text import slugify
from ninja import Field, ModelSchema, NinjaAPI, Query, Schema
from ninja.pagination import paginate
from ninja.security import HttpBearer

from apps.comptes.models import Utilisateur
from .models import Article

api = NinjaAPI(title="Mon API", version="1.0.0")                      # docs : /api/docs

class Jeton(HttpBearer):                                                # authentification par jeton
    def authenticate(self, request, token):
        return Utilisateur.objects.filter(api_jeton=token).first()      # suppose un champ api_jeton (CharField unique)

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
    article = Article.objects.create(auteur=request.auth, slug=slugify(donnees.titre), **donnees.model_dump())
    return 201, article

@api.get("/articles/{article_id}", response=ArticleOut)
async def detail(request, article_id: int):                            # vue asynchrone
    return await Article.objects.aget(pk=article_id)
```

```python
# config/urls.py
from django.urls import path
from apps.blog.api import api

urlpatterns += [path("api/", api.urls)]
```

**Lecture guidée :** un **`Schema`** (Pydantic) décrit les données d'entrée/sortie ; `response=` fixe le schéma de réponse par code HTTP (`{201: ArticleOut}`) ; `Query[Filtres]` lit les paramètres d'URL ; `@paginate` ajoute la pagination ; `auth=` branche l'authentification ; une fonction `async def` est naturellement asynchrone.

|  | **DRF** | **Django Ninja** |
| --- | --- | --- |
| Validation | Sérialiseurs | **Pydantic** (types Python) |
| Syntaxe | Classes (ViewSets) | **Fonctions annotées** |
| Documentation | drf-spectacular | **Intégrée** (OpenAPI) |
| Async | Partiel | **Natif** |
| Écosystème | **Immense** (filtres, auth, extensions) | Plus récent, en croissance |
| Idéal | Grandes API, écosystème riche | API rapides à écrire, équipes à l'aise avec FastAPI |

Authentification JWT : **`django-ninja-jwt`**.

### 21.2 GraphQL avec Strawberry

> **Définition — GraphQL.** Langage de requête pour API où le **client décrit précisément les champs** voulus et reçoit exactement cela, en **un seul point d'entrée** (`/graphql/`). Il évite le *sur-chargement* (champs inutiles) et le *sous-chargement* (plusieurs appels REST) mais déplace la complexité vers le serveur.

```bash
uv add strawberry-graphql-django
```

```python
# apps/blog/schema.py
import strawberry
import strawberry_django
from strawberry import auto

from apps.comptes.models import Utilisateur
from .models import Article

@strawberry_django.type(Utilisateur)
class UtilisateurType:
    id: auto
    username: auto

@strawberry_django.type(Article)
class ArticleType:
    id: auto
    titre: auto
    auteur: UtilisateurType

@strawberry.type
class Query:
    articles: list[ArticleType] = strawberry_django.field()

schema = strawberry.Schema(query=Query)
```

```python
# config/urls.py
from django.urls import path
from strawberry.django.views import GraphQLView
from apps.blog.schema import schema

urlpatterns += [path("graphql/", GraphQLView.as_view(schema=schema))]
```

Alternatives : **Graphene-Django**, **Ariadne**. **Points d'attention :** GraphQL expose un langage de requête : **limitez la profondeur et la complexité** (une requête imbriquée peut coûter très cher), évitez le **N+1** (*DataLoaders*, optimiseurs de `strawberry-django`), gérez les permissions **par champ**, et désactivez l'**introspection** en production si nécessaire.

### 21.3 Consommer des API externes

```bash
uv add httpx
```

```python
# apps/blog/services.py
import httpx
from django.conf import settings

def meteo(ville: str) -> dict:
    with httpx.Client(timeout=5.0) as client:                        # TOUJOURS un délai d'expiration
        r = client.get(
            "https://api.exemple.com/meteo",
            params={"q": ville},
            headers={"Authorization": f"Bearer {settings.METEO_CLE}"},
        )
        r.raise_for_status()
        return r.json()

async def meteo_async(ville: str) -> dict:                            # dans une vue asynchrone
    async with httpx.AsyncClient(timeout=5.0) as client:
        r = await client.get("https://api.exemple.com/meteo", params={"q": ville})
        r.raise_for_status()
        return r.json()
```

| Bonne pratique | Détail |
| --- | --- |
| **Délai d'expiration** | Sans `timeout`, une API lente peut **bloquer tous vos workers** |
| **Ne pas bloquer** une requête web sur une API lente | Déportez vers une **tâche en arrière-plan** (section 23) |
| **Cache** | Mettre en cache les réponses (`cache.get_or_set`) |
| **Nouvelles tentatives** et limites | `tenacity`, transports `httpx` avec *retries* ; attention à l'idempotence |
| **Erreurs** | Gérer `httpx.HTTPError`, délais, formats inattendus |
| **Secrets** | Clés dans les variables d'environnement |
| **Tests** | `respx` (httpx), `responses` / `requests-mock` ; **jamais** de réseau réel dans les tests |
| **SSRF** | Valider les URL fournies par l'utilisateur (liste blanche, interdire les IP privées) |

### 21.4 Webhooks (recevoir des événements)

> **Définition — webhook.** Appel HTTP que **le service externe** (paiement, GitHub…) envoie **à votre serveur** quand un événement se produit : c'est un « rappel » inversé, qui évite d'interroger sans cesse l'API.

```python
# apps/boutique/views.py
import hashlib
import hmac

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt          # justifié ici : requête serveur-à-serveur authentifiée par signature
from django.views.decorators.http import require_POST

from apps.blog.tasks import traiter_evenement                 # tâche présentée en section 23

@csrf_exempt
@require_POST
def webhook_paiement(request):
    signature = request.headers.get("X-Signature", "")
    attendu = hmac.new(settings.WEBHOOK_SECRET.encode(), request.body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(signature, attendu):            # comparaison à temps constant
        return HttpResponseBadRequest("signature invalide")
    traiter_evenement.delay(request.body.decode())              # répondre vite (2xx), traiter en arrière-plan
    return HttpResponse(status=202)
```

- **Pourquoi `csrf_exempt` ici ?** Il n'y a pas de navigateur ni de cookie : le CSRF n'a pas de sens ; l'authenticité est garantie par la **signature HMAC**.
- **Toujours vérifier la signature**, avec une **comparaison à temps constant** (`hmac.compare_digest`) pour éviter les attaques par chronométrie.
- Rendre le traitement **idempotent** (l'émetteur peut renvoyer un événement : mémorisez son identifiant) et **répondre rapidement** (2xx) en déportant le travail.

### À retenir

- **Ninja** = API rapides à écrire, typées, async ; **DRF** = écosystème le plus riche ; **GraphQL** = requêtes flexibles mais à encadrer.
- Appels sortants : **timeout**, erreurs gérées, cache, tests sans réseau. Webhooks : **signature** + idempotence + réponse rapide.

---

## 22. Programmation asynchrone, ASGI et WebSockets

### Objectifs d'apprentissage

Expliquer la différence WSGI/ASGI et synchrone/asynchrone ; écrire des vues asynchrones et **mélanger** sync/async correctement ; mettre en place des **WebSockets** avec Channels ; utiliser les **SSE** ; déployer en ASGI.

### 22.1 WSGI et ASGI

|  | **WSGI** | **ASGI** |
| --- | --- | --- |
| Modèle | **Synchrone** (une requête = un thread) | **Asynchrone**, HTTP + **WebSockets** + SSE |
| Serveurs | Gunicorn, uWSGI | **Uvicorn**, **Daphne**, **Hypercorn**, **Granian** |
| Point d'entrée | `config/wsgi.py` | `config/asgi.py` |
| Usage | Applications classiques | Temps réel, nombreuses E/S concurrentes |

> **Concept — boucle d'événements.** En asynchrone, **un seul thread** exécute plusieurs tâches de façon **coopérative** : quand une tâche attend (`await` une réponse réseau), la boucle en fait avancer une autre. Idéal pour les **E/S** (réseau, base) ; inutile pour le calcul pur (CPU), qui bloquerait la boucle.

Django s'exécute très bien en **WSGI** (Gunicorn). Passez en **ASGI** si vous avez besoin de **WebSockets**, de **SSE**, ou de nombreuses **E/S concurrentes** (appels d'API en parallèle).

### 22.2 Vues asynchrones

```python
import asyncio

import httpx
from django.http import JsonResponse

from apps.blog.models import Article

async def tableau_de_bord(request):
    async with httpx.AsyncClient(timeout=5) as client:
        meteo, actus = await asyncio.gather(                   # appels externes en PARALLÈLE
            client.get("https://api.a.fr/meteo"), client.get("https://api.b.fr/actus"))
    total = await Article.objects.acount()
    return JsonResponse({"meteo": meteo.json(), "actus": actus.json(), "articles": total})
```

`asyncio.gather` lance les deux appels **en même temps** : la durée totale est celle du plus lent, pas la somme.

#### Mélanger synchrone et asynchrone

```python
import asyncio

from asgiref.sync import async_to_sync, sync_to_async

def fonction_synchrone(x: int) -> int:
    return x * 2

async def fonction_async(x: int) -> int:
    return x + 1

async def exemple():
    resultat = await sync_to_async(fonction_synchrone)(21)   # appeler du code sync depuis async
    print(resultat)                                          # 42

asyncio.run(exemple())

valeur = async_to_sync(fonction_async)(41)                   # l'inverse : appeler du code async depuis du sync
print(valeur)                                                # 42
```

> **Ne bloquez jamais la boucle d'événements** (appels `requests`, `time.sleep`, calculs lourds) : utilisez `httpx.AsyncClient`, `asyncio.sleep`, ou `sync_to_async` / une tâche en arrière-plan. Les **middlewares** synchrones forcent des conversions : préférez des middlewares **compatibles async** (section 15). Django interdit certaines opérations de base de données synchrones dans un contexte asynchrone (`SynchronousOnlyOperation`) pour vous protéger.

### 22.3 Django Channels : WebSockets

> **Définition — WebSocket.** Canal de communication **bidirectionnel et persistant** entre navigateur et serveur, idéal pour le temps réel (chat, notifications, tableaux de bord). Django seul ne les gère pas : on ajoute **Channels**.

```bash
uv add channels channels-redis daphne
```

```python
# settings.py
INSTALLED_APPS = ["daphne", *INSTALLED_APPS, "channels"]                # daphne en premier : runserver devient ASGI
ASGI_APPLICATION = "config.asgi.application"
CHANNEL_LAYERS = {"default": {"BACKEND": "channels_redis.core.RedisChannelLayer", "CONFIG": {"hosts": [env("REDIS_URL")]}}}
# Tests / développement : "channels.layers.InMemoryChannelLayer"
```

```python
# config/asgi.py
import os
from django.core.asgi import get_asgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django_asgi = get_asgi_application()                                      # avant d'importer le code des apps

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
            await self.close(code=4401)
            return
        await self.channel_layer.group_add(self.groupe, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.groupe, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.groupe,
            {"type": "message.chat", "texte": data["texte"], "auteur": self.scope["user"].username},
        )

    async def message_chat(self, event):                                   # type « message.chat » → méthode message_chat
        await self.send(text_data=json.dumps({"texte": event["texte"], "auteur": event["auteur"]}))
```

```python
# apps/chat/routing.py
from django.urls import path
from .consumers import SalonConsumer

websocket_urlpatterns = [path("ws/salon/<str:salon>/", SalonConsumer.as_asgi())]
```

**Vocabulaire Channels :** un **consumer** est l'équivalent d'une vue pour un WebSocket ; la **couche de canaux** (*channel layer*, Redis) permet à des consommateurs de **s'envoyer des messages** et de former des **groupes** (tous les connectés d'un salon) ; `scope` contient l'utilisateur et les paramètres de route ; `type` d'un message est converti en nom de méthode (les `.` deviennent `_`).

> **Sécurité :** authentifiez les WebSockets (cookie de session via `AuthMiddlewareStack`, ou jeton dans la chaîne de requête / premier message), validez l'**origine** (`AllowedHostsOriginValidator`) et limitez la taille et la fréquence des messages.

### 22.4 Événements envoyés par le serveur (SSE)

Plus simples que les WebSockets pour du **flux unidirectionnel** (notifications, progression d'une tâche) :

```python
import asyncio

from django.http import StreamingHttpResponse

async def flux(request):
    async def generateur():
        for i in range(10):
            yield f"data: {i}\n\n"
            await asyncio.sleep(1)
    return StreamingHttpResponse(generateur(), content_type="text/event-stream")
```

Le navigateur consomme ce flux avec l'API `EventSource` ; la reconnexion automatique est intégrée. Fonctionne sur HTTP ordinaire (traverse mieux proxys et pare-feu qu'un WebSocket).

### 22.5 Déployer en ASGI

```bash
uvicorn config.asgi:application --host 0.0.0.0 --port 8000 --workers 4
# ou Gunicorn + worker Uvicorn (paquet uvicorn-worker)
gunicorn config.asgi:application -k uvicorn_worker.UvicornWorker -w 4 -b 0.0.0.0:8000
daphne -b 0.0.0.0 -p 8000 config.asgi:application
```

Derrière Nginx, relayez les en-têtes `Upgrade` et `Connection` pour les WebSockets (section 28.4).

### À retenir

- ASGI = HTTP + WebSockets + SSE, async natif ; **ne bloquez jamais la boucle**.
- `sync_to_async` / `async_to_sync` assurent la passerelle ; `asyncio.gather` parallélise les E/S.
- Channels pour le temps réel : consumers, groupes, couche Redis, authentification et origine à vérifier.

---

## 23. Tâches en arrière-plan

### Objectifs d'apprentissage

Comprendre pourquoi et quand déporter un traitement hors de la requête HTTP ; connaître l'architecture producteur / file / worker ; utiliser le **framework de tâches intégré** (Django 6.0) et **Celery** (tâches, nouvelles tentatives, planification, chaînes, supervision) ; appliquer les règles d'**idempotence** et de **transaction** ; choisir la bonne solution.

### 23.1 Pourquoi déporter des traitements ?

Une requête web doit répondre en **quelques centaines de millisecondes**. Les opérations **lentes ou fragiles** (envoi d'e-mails, génération de PDF, appels d'API tierces, traitement d'images, rapports, synchronisations) ne doivent **pas** s'exécuter dans la requête : elles ralentissent l'utilisateur, occupent un worker web et échouent avec la requête si le service externe tombe. On les **met en file d'attente** ; un **worker** (processus séparé) les exécute.

```text
Vue ──enqueue──> File (Redis, RabbitMQ, base) ──> Worker ──> exécute la tâche
  ↓ réponse immédiate
```

| Terme | Définition |
| --- | --- |
| **Producteur** | Le code (vue, service) qui **met la tâche en file** |
| **File / courtier** (*broker*) | Stockage intermédiaire des messages (Redis, RabbitMQ, PostgreSQL) |
| **Worker** | Processus qui **consomme** la file et exécute les tâches |
| **Backend de résultats** | Lieu où l'on retrouve l'état et le résultat d'une tâche |
| **Planificateur** (*beat*) | Déclenche des tâches **périodiques** (cron applicatif) |
| **Idempotence** | Rejouer une tâche ne produit pas d'effet supplémentaire |

**Garantie de livraison.** La plupart des systèmes offrent *« au moins une fois »* : une tâche peut s'exécuter **deux fois** (worker interrompu, nouvelle tentative). C'est pourquoi **toute tâche doit être idempotente**.

### 23.2 Framework de tâches intégré *(Django 6.0, ajout)*

Django 6.0 introduit une **API standard** pour définir et mettre en file des tâches. Django fournit l'**interface** ; l'**exécution en production** est confiée à un **backend** (implémentation) externe.

```python
# settings.py
TASKS = {"default": {"BACKEND": "django.tasks.backends.immediate.ImmediateBackend"}}   # exécution immédiate (développement / tests)
# Production : un backend externe (ex. paquet django-tasks avec un backend base de données, ou d'autres backends tiers)
```

```python
# apps/blog/tasks.py
from django.core.mail import send_mail
from django.tasks import task

from apps.comptes.models import Utilisateur

@task
def envoyer_bienvenue(utilisateur_id: int) -> None:
    utilisateur = Utilisateur.objects.get(pk=utilisateur_id)
    send_mail("Bienvenue", "Merci de votre inscription.", None, [utilisateur.email])

# Dans une vue / un modèle
def inscrire(utilisateur):
    resultat = envoyer_bienvenue.enqueue(utilisateur.pk)           # met en file (et n'appelle PAS la fonction)
    print(resultat.id)
```

**Ce qu'il faut comprendre :**

- `@task` transforme la fonction en objet *tâche* ; **`.enqueue(...)`** la met en file et renvoie immédiatement un **résultat** (identifiant, état). Appeler la fonction directement l'exécute « normalement », sans file.
- Les arguments doivent être **sérialisables** (nombres, textes, listes, dictionnaires) : passez un **identifiant**, pas un objet de modèle (voir 23.3).
- Le **backend immédiat** exécute la tâche sur-le-champ, dans le même processus : parfait pour développer et tester, **inutilisé en production**.
- Le framework définit aussi des réglages par tâche (file nommée, priorité, exécution différée) ; leur disponibilité dépend du **backend** choisi.

> **Mise en garde.** Le framework intégré **ne fournit pas de worker de production** : vérifiez la documentation officielle (« Tasks ») et l'état des backends tiers avant de l'adopter ; **Celery** reste la solution la plus éprouvée.

### 23.3 Celery

**Celery** est le système de tâches distribuées de référence : files multiples, planification, nouvelles tentatives, chaînes, résultats, supervision.

```bash
uv add celery redis django-celery-beat django-celery-results flower
```

```python
# config/celery.py
import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")      # réglages préfixés CELERY_
app.autodiscover_tasks()                                                  # trouve tasks.py dans les apps

# config/__init__.py
from .celery import app as celery_app

__all__ = ("celery_app",)
```

```python
# settings.py
CELERY_BROKER_URL = env("REDIS_URL", default="redis://localhost:6379/0")
CELERY_RESULT_BACKEND = "django-db"                                       # django-celery-results
CELERY_TIMEZONE = "Europe/Paris"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 300                                              # tue la tâche après 300 s
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler" # tâches périodiques éditables dans l'admin
```

- `config_from_object(..., namespace="CELERY")` fait lire à Celery les réglages Django qui commencent par `CELERY_`.
- `autodiscover_tasks()` importe automatiquement le fichier `tasks.py` de chaque app installée.
- Le `import` dans `config/__init__.py` garantit que l'application Celery est chargée au démarrage de Django (nécessaire pour `@shared_task`).

#### Écrire et appeler des tâches

```python
# apps/blog/tasks.py
import json
import logging

from celery import shared_task
from django.core.mail import send_mail
from django.db import transaction

from apps.comptes.models import Utilisateur

logger = logging.getLogger(__name__)

@shared_task(bind=True, autoretry_for=(ConnectionError,), retry_backoff=True, retry_kwargs={"max_retries": 5})
def envoyer_bienvenue(self, utilisateur_id: int) -> None:
    utilisateur = Utilisateur.objects.get(pk=utilisateur_id)             # passer des IDENTIFIANTS, pas des objets
    send_mail("Bienvenue", "Merci de votre inscription.", None, [utilisateur.email])

@shared_task
def envoyer_confirmation(commande_id: str) -> None:
    logger.info("Confirmation envoyée pour la commande %s", commande_id)

@shared_task
def traiter_evenement(corps: str) -> None:
    evenement = json.loads(corps)
    logger.info("Événement reçu : %s", evenement.get("type"))

# Appels (dans une vue ou un service)
def inscrire(utilisateur):
    envoyer_bienvenue.delay(utilisateur.pk)                                           # file immédiatement
    envoyer_bienvenue.apply_async(args=[utilisateur.pk], countdown=60)                # dans 60 s
    # Après la validation de la transaction (sinon le worker peut ne pas trouver l'objet)
    transaction.on_commit(lambda: envoyer_bienvenue.delay(utilisateur.pk))
```

| Notion | Explication |
| --- | --- |
| `@shared_task` | Crée une tâche **indépendante de l'instance Celery** (idéal pour les apps réutilisables) |
| `.delay(*args)` | Raccourci de `.apply_async(args=...)` : met en file |
| `.apply_async(countdown=, eta=, queue=, expires=)` | Contrôle fin : délai, heure précise, file, expiration |
| `bind=True` | La tâche reçoit `self` (état, nouvelles tentatives manuelles `self.retry()`) |
| `autoretry_for` + `retry_backoff` | Nouvelle tentative **automatique** sur certaines exceptions, avec délai **exponentiel** |
| `max_retries` | Nombre maximal de tentatives |

**Deux règles critiques :**

1. **Passez des identifiants (JSON sérialisable), jamais des instances de modèle** : l'objet peut avoir changé entre la mise en file et l'exécution, et la sérialisation échouerait. La tâche **relit** l'objet.
2. **`transaction.on_commit`** : si vous mettez en file **avant** la validation de la transaction, le worker (très rapide) peut chercher une ligne **pas encore visible** et échouer.

```bash
celery -A config worker -l info          # worker
celery -A config beat -l info            # planificateur (tâches périodiques)
celery -A config flower                  # supervision web (http://localhost:5555)
```

#### Chaînes, groupes, accords (*canvas*)

```python
from celery import chain, chord, group, shared_task

@shared_task
def telecharger(url: str) -> str:
    return f"contenu de {url}"

@shared_task
def traiter(contenu: str) -> str:
    return contenu.upper()

@shared_task
def notifier(resultat: str) -> str:
    return f"notifié : {resultat}"

@shared_task
def redimensionner(image_id: int) -> int:
    return image_id

@shared_task
def callback(resultats: list[int]) -> int:
    return sum(resultats)

chain(telecharger.s("https://exemple.fr"), traiter.s(), notifier.s())()       # l'une après l'autre (le résultat est transmis)
group(redimensionner.s(i) for i in [1, 2, 3])()                                # en parallèle
chord(group(redimensionner.s(i) for i in [1, 2, 3]))(callback.s())             # parallèle + rappel final
```

- **`chain`** : enchaîne des tâches, chaque résultat devenant le premier argument de la suivante.
- **`group`** : lance des tâches **en parallèle**.
- **`chord`** : un groupe suivi d'un **rappel** quand **toutes** ont fini.
- `.s()` crée une **signature** (appel différé d'une tâche avec ses arguments).

#### Tâches périodiques

```python
# apps/blog/tasks.py
from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from .models import Article

@shared_task
def nettoyer() -> int:
    limite = timezone.now() - timedelta(days=90)
    nombre, _ = Article.objects.filter(statut="brouillon", cree_le__lt=limite).delete()
    return nombre

# settings.py
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "nettoyage-nocturne": {"task": "apps.blog.tasks.nettoyer", "schedule": crontab(hour=3, minute=0)},
}
```

Avec `django-celery-beat`, le planning vit **en base** et se modifie dans l'**admin** sans redéploiement. **Ne lancez qu'une seule instance de `beat`**, sinon les tâches se déclenchent en double.

#### Bonnes pratiques Celery

- **Idempotentes**, **petites**, avec **délai maximal** (`time_limit`, `soft_time_limit`).
- **Surveillez** (Flower, Sentry), configurez **nouvelles tentatives** avec *backoff* et **files dédiées** (`task_routes`) pour isoler les tâches lourdes des rapides.
- Testez avec `CELERY_TASK_ALWAYS_EAGER = True` (exécution immédiate) ou en appelant directement la fonction.
- Ne bloquez pas un worker sur une tâche qui attend le résultat d'une autre (risque d'interblocage) : utilisez des chaînes.

### 23.4 Alternatives et choix

| Outil | Caractéristiques |
| --- | --- |
| **Django Tasks** (6.0) | API **intégrée**, standard ; backends en évolution |
| **Celery** | Le plus complet : planification, files multiples, flux (*canvas*) |
| **Huey** | **Léger**, simple (Redis) |
| **Dramatiq** (`django-dramatiq`) | Fiable, plus simple que Celery |
| **RQ** (`django-rq`) | Très simple, basé sur Redis |
| **Procrastinate** | File de tâches **sur PostgreSQL** (pas de courtier à exploiter) |
| **Django-Q2** | Tâches simples avec l'ORM comme courtier |
| **Cron + commandes de gestion** | Tâches périodiques simples |

> **Choix** : besoin simple → **Django Tasks / Huey / Procrastinate / cron** ; besoin riche (planification, flux, forte volumétrie) → **Celery**.

### Pièges fréquents

| Piège | Remède |
| --- | --- |
| Passer un objet de modèle en argument | Passer l'identifiant |
| Mise en file avant la validation de la transaction | `transaction.on_commit` |
| Tâche non idempotente rejouée (double e-mail, double facturation) | Clé d'idempotence, test d'état avant action |
| Aucun délai maximal | `time_limit` |
| Plusieurs `beat` | Une seule instance |

### À retenir

- Tout ce qui est lent ou externe se déporte dans un **worker** ; la vue répond immédiatement.
- Livraison *au moins une fois* → **idempotence** obligatoire ; **identifiants** en arguments ; **`on_commit`**.
- Django Tasks pour les besoins simples ; Celery pour les besoins riches.

---

## 24. Frontend moderne avec Django

*(Section ajoutée : les approches actuelles pour construire l'interface.)*

### Objectifs d'apprentissage

Choisir l'approche front adaptée à un projet ; construire une interface dynamique avec **HTMX** et des **fragments de template** ; intégrer Tailwind et Vite ; organiser une **SPA** consommant une API Django ; appliquer le principe « commencer simple ».

### 24.1 Panorama des approches

| Approche | Principe | Idéal pour |
| --- | --- | --- |
| **Templates Django classiques** | HTML **rendu côté serveur** | Sites de contenu, back-offices |
| **HTMX + Alpine.js** | Le serveur renvoie des **fragments HTML** ; interactivité sans SPA | Applications riches **sans** framework JavaScript lourd |
| **Composants de template** (`django-cotton`, `django-components`) | Composants réutilisables en HTML | Design systems côté serveur |
| **Tailwind CSS** (+ Vite) | Classes utilitaires CSS | Interfaces modernes |
| **SPA** (React, Vue, Svelte) + **DRF / Ninja** | Front séparé, API JSON | Applications très interactives, équipes front dédiées |
| **Inertia.js** (`inertia-django`) | Pages React/Vue pilotées par les vues Django, **sans API** | Monolithe moderne |

> **Définition — SPA** (*Single-Page Application*). Application dont le navigateur charge **une seule page**, puis gère la navigation et l'affichage en JavaScript, en échangeant des **données JSON** avec le serveur. **Rendu côté serveur (SSR)** : le serveur produit le HTML complet à chaque page (approche classique de Django). Le choix entre les deux conditionne l'architecture, l'équipe, le référencement et la complexité.

### 24.2 HTMX avec `django-htmx`

> **Définition — HTMX.** Petite bibliothèque JavaScript qui permet à **n'importe quel élément HTML** d'envoyer une requête (`hx-get`, `hx-post`…) et d'**insérer la réponse HTML** dans la page (`hx-target`, `hx-swap`), sans écrire de JavaScript. Le serveur reste la source de vérité et renvoie des **fragments**.

```bash
uv add django-htmx
```

```python
INSTALLED_APPS += ["django_htmx"]
MIDDLEWARE += ["django_htmx.middleware.HtmxMiddleware"]                 # ajoute request.htmx
```

```django
<script src="https://unpkg.com/htmx.org@2.0.4" defer></script>
<body hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'>

<input type="search" name="q" placeholder="Rechercher…"
       hx-get="{% url 'blog:liste' %}" hx-trigger="input changed delay:300ms" hx-target="#resultats" hx-push-url="true">
<div id="resultats">{% partial liste-articles %}</div>
```

```python
# apps/blog/views.py
from django.shortcuts import render
from .models import Article

def liste(request):
    q = request.GET.get("q", "")
    articles = Article.objects.publies().filter(titre__icontains=q)
    gabarit = "blog/liste.html#liste-articles" if request.htmx else "blog/liste.html"   # fragment (6.0) si requête HTMX
    return render(request, gabarit, {"articles": articles})
```

**Lecture guidée :**

- `hx-get` : requête `GET` déclenchée par `hx-trigger` (ici : à chaque saisie, avec 300 ms d'anti-rebond, c'est-à-dire une requête seulement quand l'utilisateur s'arrête de taper).
- `hx-target="#resultats"` : élément qui reçoit la réponse ; `hx-swap` (par défaut `innerHTML`) précise comment l'insérer ; `hx-push-url="true"` met à jour l'URL du navigateur (retour arrière, partage de lien).
- `request.htmx` (fourni par `django-htmx`) permet à **la même vue** de servir la page complète (premier chargement, robots d'indexation) **ou** le seul fragment (requête HTMX).
- Le **CSRF** passe par l'en-tête `X-CSRFToken` défini une fois sur `<body>`.

> Avec les **partiels de template** (Django 6.0, section 7.4), une seule page sert à la fois la **page complète** et le **fragment** : fini les dizaines de petits fichiers `_fragment.html`.

**Cas d'usage typiques :** recherche instantanée, pagination/« voir plus », validation de champ à la volée, édition « en ligne », suppression sans rechargement, onglets, notifications par `HX-Trigger`.

**Alpine.js** complète HTMX pour les **petits comportements purement client** (menu déroulant, modale, onglet) : `<div x-data="{ ouvert: false }"><button @click="ouvert = !ouvert">Menu</button><nav x-show="ouvert">…</nav></div>`.

### 24.3 Tailwind et ressources front

| Besoin | Outil |
| --- | --- |
| **Tailwind CSS** | `django-tailwind-cli` (sans Node) ou `django-tailwind` ; ou compilation par Vite |
| **Vite** (JS, CSS, rechargement à chaud) | **`django-vite`** |
| Bibliothèques JS | `npm` + bundler, ou *import maps* |
| Compression / empreintes | **WhiteNoise**, `django-compressor` |
| Composants | `django-cotton`, `django-components`, `django-slippers` |
| Icônes | `django-heroicons`, `django-lucide` |

**Tailwind** est un framework CSS « utilitaire » : on compose l'apparence avec de petites classes (`px-4 py-2 rounded bg-blue-600 text-white`) au lieu d'écrire du CSS. **Vite** est un outil de compilation (*bundler*) rapide qui assemble JS/CSS et offre le **rechargement à chaud** ; `django-vite` fait le lien : en développement il pointe vers le serveur Vite, en production vers les fichiers compilés (avec empreintes) collectés par `collectstatic`.

### 24.4 SPA + Django

- **API** : DRF ou Ninja ; **authentification** : sessions (même domaine) ou JWT (section 20) ; **CORS** configuré.
- **Servir le build** du front : par Nginx / CDN, ou via `TemplateView` + WhiteNoise pour une SPA simple.
- **Types partagés** : générez des clients TypeScript depuis le schéma **OpenAPI** (`drf-spectacular` + `openapi-typescript` / `orval`) : les contrats d'API restent synchronisés.
- En développement : Vite sur le port `5173` + Django sur `8000`, avec un **proxy** Vite vers Django ou CORS.
- **Coût caché d'une SPA** : deux bases de code, deux déploiements, authentification et CORS à gérer, référencement (SEO) à traiter, état à synchroniser. À n'assumer que si le besoin le justifie.

### 24.5 Ordre de conseil

1. **Commencez simple** : templates + **HTMX** couvrent l'immense majorité des besoins.
2. Ajoutez **Alpine.js** pour de petits comportements côté client.
3. Passez à une **SPA** seulement si l'interactivité (éditeur riche, tableaux complexes, mode hors-ligne) l'exige.

### À retenir

- Le rendu **serveur** + **HTMX** est souvent le meilleur rapport simplicité / interactivité pour Django.
- Une SPA ajoute une API, du CORS/JWT, du SEO à gérer : à choisir en connaissance de cause.
- Les **partiels** (6.0) permettent de servir page complète et fragment depuis un même template.

---

# Qualité et production

---

## 25. Tests

### Objectifs d'apprentissage

Situér les niveaux de tests et choisir l'outil adapté ; écrire des tests Django (`TestCase`, client HTTP, `assertNumQueries`) puis des tests `pytest-django` ; fabriquer des données avec `factory_boy` ; isoler le temps, le réseau et les tâches (mocks) ; accélérer la suite ; écrire des tests E2E ; mettre en place couverture et intégration continue.

### 25.1 Pourquoi et quoi tester

> **Définition.** Un **test automatisé** est un programme qui exécute votre code dans des conditions contrôlées et **vérifie** un résultat attendu. Il documente le comportement, détecte les **régressions** (une modification qui casse l'existant) et rend les mises à jour de Django et le refactoring sûrs.

| Niveau | Cible | Outils |
| --- | --- | --- |
| **Unitaires** | Fonctions, modèles, formulaires, services | `TestCase`, `pytest` |
| **Intégration** | Vues + base + templates | `Client`, `APIClient` |
| **Bout en bout (E2E)** | Navigateur réel | **Playwright**, Selenium |
| **Non-régression, performance** | Requêtes SQL, charge | `assertNumQueries`, `locust`, `k6` |

La **pyramide des tests** recommande beaucoup de tests unitaires (rapides, précis), un nombre modéré de tests d'intégration, et peu de tests E2E (lents, fragiles mais proches de l'utilisateur).

### 25.2 Tests Django (`unittest`)

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
        cls.article = Article.objects.create(titre="Bonjour", slug="bonjour", contenu="…" * 50,
                                             auteur=cls.alice, statut="publie")

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
        r = self.client.post(reverse("blog:creer"),
                             {"titre": "Nouveau", "slug": "nouveau", "contenu": "x" * 120, "statut": "brouillon"})
        self.assertEqual(r.status_code, 302)
        self.assertTrue(Article.objects.filter(titre="Nouveau", auteur=self.alice).exists())

    def test_nombre_de_requetes(self):
        with self.assertNumQueries(2):                              # détecte les régressions N+1
            self.client.get(reverse("blog:liste"))

    @override_settings(EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend")
    def test_email(self):
        self.client.post(reverse("contact"),
                         {"nom": "A", "email": "a@b.fr", "sujet": "q", "message": "Bonjour tout le monde"})
        self.assertEqual(len(mail.outbox), 1)
```

```bash
python manage.py test                              # tous les tests
python manage.py test apps.blog.tests.test_views.ArticleTests.test_creation
python manage.py test --parallel --keepdb          # en parallèle, en conservant la base de test
```

**Mécanique.** Django crée une **base de test** vide (préfixe `test_`), applique les migrations, exécute les tests, puis la détruit : **vos données réelles ne sont jamais touchées**. Avec `TestCase`, chaque test s'exécute dans une **transaction annulée** à la fin : les tests restent indépendants et rapides. `setUpTestData` crée les données **une fois par classe** (les objets sont remis à neuf pour chaque test) ; `setUp` s'exécute avant **chaque** test.

| Classe | Usage |
| --- | --- |
| `SimpleTestCase` | Sans base de données |
| `TestCase` | Chaque test dans une **transaction annulée** |
| `TransactionTestCase` | Teste le comportement transactionnel (`on_commit`, verrous), plus lent |
| `LiveServerTestCase` / `StaticLiveServerTestCase` | Serveur réel pour Selenium / Playwright |

Outils : `Client` (HTTP complet, cookies, session), `RequestFactory` (vue isolée, sans middlewares), `override_settings`, `mail.outbox`, `assertContains`, `assertRedirects`, `assertFormError`, `assertNumQueries`, `skipUnless`, `self.client.force_login(user)`.

### 25.3 `pytest-django`

```bash
uv add --dev pytest pytest-django pytest-cov pytest-xdist factory-boy faker pytest-factoryboy
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

def test_admin(admin_client):
    assert admin_client.get("/admin/").status_code == 200
```

**Pourquoi pytest ?** Tests en **fonctions simples** avec `assert` (messages d'échec détaillés), **fixtures** composables, **paramétrage** (`@pytest.mark.parametrize`), écosystème de plugins. Le marqueur **`django_db`** (ou la fixture `db`) autorise l'accès à la base : sans lui, un test qui interroge la base échoue (protection contre des accès accidentels). Fixtures utiles : `client`, `admin_client`, `rf`, `db`, `transactional_db`, `settings`, `mailoutbox`, `django_assert_num_queries`, `live_server`.

### 25.4 Données de test : `factory_boy`

```python
# apps/blog/tests/factories.py
import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from apps.blog.models import Article

User = get_user_model()

class UtilisateurFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda o: f"{o.username}@exemple.fr")
    password = factory.PostGenerationMethodCall("set_password", "motdepasse")

class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    titre = factory.Faker("sentence", locale="fr_FR")
    slug = factory.Sequence(lambda n: f"article-{n}")
    contenu = factory.Faker("paragraph", nb_sentences=8, locale="fr_FR")
    auteur = factory.SubFactory(UtilisateurFactory)

# conftest.py
from pytest_factoryboy import register          # fixtures article_factory, utilisateur_factory

from apps.blog.tests.factories import ArticleFactory, UtilisateurFactory

register(UtilisateurFactory)
register(ArticleFactory)
```

- `Sequence` produit une valeur **unique** par objet ; `LazyAttribute` calcule une valeur **à partir des autres champs** ; `SubFactory` crée l'objet lié (l'auteur) ; `Faker` génère du contenu réaliste.
- **Factories plutôt que fixtures JSON** : plus lisibles, plus faciles à maintenir quand le modèle change ; on ne spécifie que ce qui compte pour le test (`statut="publie"`). Alternative : **`model_bakery`**.

### 25.5 Tester des API

Voir 19.8 (`APIClient`). Authentification : `client.force_authenticate(user)` ou `client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")`. Testez les **codes** (201, 400, 401, 403, 404), le **format** des erreurs, la pagination et les **permissions par rôle**.

### 25.6 Mocks, temps et services externes

> **Définition — mock.** Objet de remplacement qui simule une dépendance (API externe, horloge, envoi d'e-mail) pour rendre le test **rapide, déterministe et sans effet de bord**.

```python
from datetime import timedelta
from unittest import mock

from django.utils import timezone
from freezegun import freeze_time              # ou time-machine

from apps.blog.models import Article
from apps.blog.services import meteo
from apps.blog.tasks import traiter_evenement

@freeze_time("2026-10-14 12:00")
def test_publication_planifiee(db, django_user_model):
    auteur = django_user_model.objects.create_user("alice", "alice@exemple.fr", "x")
    Article.objects.create(titre="Futur", slug="futur", contenu="x", auteur=auteur, statut="publie",
                           publie_le=timezone.now() + timedelta(days=1))
    assert Article.objects.publies().count() == 0              # l'article planifié n'est pas encore visible

@mock.patch("apps.blog.services.httpx.Client.get")
def test_meteo(mock_get, settings):
    settings.METEO_CLE = "cle-de-test"
    mock_get.return_value.json.return_value = {"temp": 20}
    assert meteo("Paris") == {"temp": 20}

# Tâches Celery : appeler la fonction directement (sans worker ni courtier)
def test_tache_appelee_directement():
    assert traiter_evenement('{"type": "paiement"}') is None
```

- **Règle du `mock.patch`** : on remplace le nom **là où il est utilisé** (`apps.blog.services.httpx...`), pas là où il est défini.
- `freeze_time` fige l'horloge : indispensable pour tester dates d'expiration, publications planifiées, périodes d'essai.
- Outils : **`respx`** (httpx), **`responses`** / `requests-mock`, **`moto`** (AWS), `pytest-mock`. **Aucun appel réseau réel** dans les tests unitaires.

### 25.7 Réglages de test rapides

```python
# config/settings/test.py
from .base import *

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]       # TESTS UNIQUEMENT : hachage rapide
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
CACHES = {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.InMemoryStorage"},
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
}
CELERY_TASK_ALWAYS_EAGER = True
```

Le hachage de mots de passe est volontairement lent (sécurité) : un hacheur rapide **dans les tests uniquement** accélère nettement une suite qui crée beaucoup d'utilisateurs. Autres accélérateurs : `--reuse-db` / `--keepdb`, `pytest -n auto` (parallèle), `setUpTestData`, SQLite en mémoire pour les tests simples (mais **testez sur PostgreSQL en CI** si vous utilisez ses fonctions spécifiques).

### 25.8 Tests E2E avec Playwright

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

Un test E2E pilote un **vrai navigateur**. Repérez les éléments par **rôle, libellé ou texte** (`get_by_role`, `get_by_label`), comme un utilisateur (et comme un lecteur d'écran), plutôt que par classes CSS fragiles. Réservez-les aux **parcours critiques** (inscription, paiement). Avec `pytest-django`, utilisez `live_server` ; en mode `unittest`, `StaticLiveServerTestCase`.

### 25.9 Couverture et intégration continue

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

La **couverture** (*coverage*) mesure la part du code exécutée par les tests ; c'est un **indicateur** (un code non couvert est forcément non testé), pas une garantie de qualité (un code couvert peut être mal vérifié). L'**intégration continue (CI)** exécute automatiquement lint, types, contrôle des migrations et tests à chaque `push`, sur une base **PostgreSQL réelle**.

### 25.10 Bonnes pratiques

- Un test = **un comportement**, nom explicite, **indépendant** des autres (méthode **Arrange – Act – Assert** : préparer, agir, vérifier).
- Testez **cas nominaux, limites et refusés** (permissions !) ; un bogue corrigé appelle un test qui l'aurait attrapé.
- **`assertNumQueries`** sur les pages sensibles ; mode `fetch_mode(FETCH_RAISE)` (6.1) pour repérer les N+1.
- Vérifiez en CI : `makemigrations --check`, `manage.py check --deploy`, linting, types.
- Ne testez pas Django lui-même : testez **votre** logique.

### À retenir

- **Pyramide** : beaucoup d'unitaires, quelques intégrations, peu d'E2E.
- `TestCase` / pytest-django + factories + mocks (réseau, temps) + `assertNumQueries`.
- Une CI qui exécute lint, types, migrations, tests sur PostgreSQL est le filet de sécurité du projet.

---

## 26. Sécurité

### Objectifs d'apprentissage

Connaître les protections intégrées de Django et leurs limites ; appliquer la liste de contrôle de production ; configurer une **Content Security Policy** ; identifier et corriger les vulnérabilités courantes (OWASP) ; gérer secrets, dépendances, limitation de débit et sécurité d'infrastructure.

### 26.1 Les protections intégrées

Django est **sûr par défaut** à condition de ne pas contourner ses mécanismes.

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

> **Définition — clickjacking.** Attaque qui charge votre site dans un `<iframe>` invisible sur une page piégée pour tromper l'utilisateur et lui faire cliquer sur vos boutons à son insu. `X-Frame-Options: DENY` interdit l'inclusion dans un cadre.

### 26.2 Liste de contrôle de production

```bash
python manage.py check --deploy
```

```python
DEBUG = False
SECRET_KEY = env("SECRET_KEY")                          # longue, aléatoire, jamais versionnée ; rotation via SECRET_KEY_FALLBACKS
ALLOWED_HOSTS = ["exemple.fr", "www.exemple.fr"]

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_HSTS_SECONDS = 31_536_000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ["https://exemple.fr"]
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "same-origin"
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin"
X_FRAME_OPTIONS = "DENY"
DATA_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024
```

| Réglage | Effet |
| --- | --- |
| `SECURE_SSL_REDIRECT` | Redirige tout le HTTP vers HTTPS |
| `SECURE_HSTS_*` | Le navigateur n'utilise plus que HTTPS pour ce domaine (commencez par une durée courte avant d'activer `PRELOAD`, difficile à annuler) |
| `*_COOKIE_SECURE` / `HTTPONLY` / `SAMESITE` | Cookies HTTPS seul / illisibles par JS / limités en contexte inter-sites |
| `SECURE_CONTENT_TYPE_NOSNIFF` | Interdit au navigateur de « deviner » le type d'un fichier |
| `SECURE_REFERRER_POLICY` | Limite l'URL transmise au site de destination |
| `SECURE_CROSS_ORIGIN_OPENER_POLICY` | Isole la fenêtre des autres origines |
| `DATA_UPLOAD_MAX_MEMORY_SIZE` | Plafond de la taille d'un corps de requête |

### 26.3 Content Security Policy *(Django 6.0, ajout)*

> **Définition — CSP.** Politique, annoncée par un en-tête HTTP, qui dit au navigateur **de quelles sources** il peut charger scripts, styles, images, cadres, etc. Même si un attaquant réussit à injecter du HTML (XSS), le navigateur **refuse d'exécuter** un script non autorisé : l'impact est très réduit.

Django 6.0 l'intègre :

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

- Une **directive** (`script-src`, `img-src`…) liste les sources permises ; `CSP.SELF` = votre propre origine ; `CSP.NONE` = rien.
- Un **nonce** est une valeur aléatoire **unique par requête** : seuls les scripts portant ce nonce s'exécutent. C'est ce qui permet des scripts en ligne **sans** `'unsafe-inline'`.
- **Démarche** : d'abord `SECURE_CSP_REPORT_ONLY` (le navigateur **signale** les violations sans rien bloquer), corrigez ce qui est signalé, puis activez `SECURE_CSP`.
- Évitez `'unsafe-inline'` et `'unsafe-eval'`, qui annulent l'intérêt de la CSP. `json_script` (7.3) est compatible avec une CSP stricte. Pour les versions antérieures : **`django-csp`**.

### 26.4 Les vulnérabilités à connaître

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

**Comprendre chaque famille :**

- **XSS** (*Cross-Site Scripting*) : un script fourni par un attaquant est exécuté dans le navigateur de la victime (vol de session, actions à sa place). Django l'empêche par défaut en échappant le HTML ; la faille apparaît quand **vous** désactivez cet échappement.
- **IDOR** (*Insecure Direct Object Reference*) : changer `/commandes/42/` en `/commandes/43/` donne accès à la commande d'un autre. Parade : ne jamais faire confiance à l'identifiant, **toujours filtrer par propriétaire**.
- **Mass assignment** : un attaquant ajoute `is_staff=on` à un formulaire ; avec `fields = "__all__"`, le champ serait pris en compte.
- **Redirection ouverte** : `?next=https://site-pirate.fr` utilisé pour une phishing crédible ; on vérifie que la cible est un hôte autorisé.
- **SSRF** (*Server-Side Request Forgery*) : l'attaquant fait appeler par **votre serveur** une adresse interne (métadonnées cloud, base interne).

```python
from django.http import HttpResponseRedirect
from django.utils.http import url_has_allowed_host_and_scheme

def apres_connexion(request):
    suivant = request.POST.get("next", "")
    if not url_has_allowed_host_and_scheme(suivant, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
        suivant = "/"
    return HttpResponseRedirect(suivant)
```

```python
from django.http import HttpResponse
from django.views.decorators.debug import sensitive_post_parameters

@sensitive_post_parameters("motdepasse")          # masquées dans les rapports d'erreur
def connexion(request):
    return HttpResponse("Connexion")
```

### 26.5 Secrets et configuration

- **Jamais** de secrets dans Git : `.env` ignoré, **variables d'environnement**, gestionnaires de secrets (Vault, AWS/GCP Secret Manager, SOPS).
- Une **`SECRET_KEY` différente** par environnement ; **rotation** avec `SECRET_KEY_FALLBACKS` (les anciennes clés restent valides en lecture le temps de la transition).
- Comptes de base de données aux **privilèges minimaux** (principe du moindre privilège) ; **TLS** vers la base.
- Un secret **déjà commité** est **compromis** : il faut le **renouveler**, pas seulement le supprimer du dépôt (l'historique Git le conserve).

### 26.6 Dépendances et mises à jour

```bash
uv run pip-audit                           # vulnérabilités connues dans les dépendances
uv add --dev bandit && bandit -r apps      # analyse statique de sécurité (ou règles « S » de ruff)
```

- **Appliquez les correctifs de sécurité** Django rapidement : ils sont annoncés sur **django-announce** (et `security@djangoproject.com` pour signaler une faille). Suivez uniquement les versions **supportées** (5.2 LTS, 6.0, 6.1).
- **Dependabot / Renovate** pour les mises à jour automatiques ; verrouillez les versions ; relisez les nouveaux paquets avant installation (risque de paquets malveillants).

### 26.7 Limitation de débit et protection des comptes

```python
INSTALLED_APPS += ["axes"]
AUTHENTICATION_BACKENDS = ["axes.backends.AxesStandaloneBackend", "django.contrib.auth.backends.ModelBackend"]
MIDDLEWARE += ["axes.middleware.AxesMiddleware"]
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = 1                    # 5 échecs → blocage 1 heure
```

```python
from django.http import HttpResponse
from django_ratelimit.decorators import ratelimit

@ratelimit(key="ip", rate="5/m", block=True)
def connexion(request):
    return HttpResponse("Connexion")
```

Le **blocage par IP** est contournable (adresses multiples) et peut pénaliser des réseaux partagés : combinez-le avec un blocage **par compte**, la **2FA** et la détection d'anomalies.

### 26.8 Sécurité de l'infrastructure

- **HTTPS** (Let's Encrypt, Caddy), **HSTS**, TLS ≥ 1.2.
- Conteneurs : **utilisateur non root**, images minimales, pas de secrets dans les images.
- **Pare-feu**, base **non exposée**, sauvegardes **chiffrées et testées** (une sauvegarde jamais restaurée n'est pas une sauvegarde).
- **Journaux** d'audit, alertes (Sentry), surveillance.
- Références : **OWASP Top 10**, guide « Security in Django » de la documentation officielle.

### À retenir

- Django protège par défaut : **ne contournez pas** l'échappement, le CSRF, l'ORM paramétré.
- `check --deploy` + HTTPS/HSTS/cookies sécurisés + **CSP** (commencer en mode rapport).
- Les failles réelles sont surtout **logiques** (IDOR, mass assignment) : filtrez par propriétaire, listez les champs.

---

## 27. Performances

### Objectifs d'apprentissage

Adopter une démarche **mesurer → corriger → re-mesurer** ; utiliser les bons outils de profilage (développement et production) ; appliquer par ordre d'impact les optimisations (base, cache, tâches, statiques, connexions, serveur) ; gérer pagination et gros volumes ; régler Gunicorn/ASGI ; optimiser côté réseau et navigateur.

### 27.1 Mesurer d'abord

> **Règle d'or.** *« L'optimisation prématurée est la racine de tous les maux »* (Knuth). On n'optimise **jamais sans mesure** : l'intuition se trompe presque toujours sur l'endroit où le temps est perdu. Un **profil** montre où va le temps ; une **mesure avant/après** prouve le gain.

| Outil | Usage |
| --- | --- |
| **`django-debug-toolbar`** | Requêtes SQL, doublons, temps, templates (développement) |
| **`django-silk`**, **`django-querycount`** | Profilage de requêtes / SQL |
| **Sentry Performance**, **OpenTelemetry**, **Datadog**, **New Relic** | Production (APM : *Application Performance Monitoring*) |
| `EXPLAIN ANALYZE` (`.explain()`), `pg_stat_statements` | Base de données |
| **`py-spy`**, `cProfile`, **Scalene** | Profilage Python |
| **`locust`**, **`k6`**, `wrk` | Tests de charge |

Indicateurs à suivre : **latence** (médiane et surtout **p95 / p99**, car la moyenne cache les requêtes lentes), **débit** (requêtes par seconde), **taux d'erreur**, **nombre de requêtes SQL par page**, **utilisation mémoire / CPU**.

### 27.2 Les gains les plus importants (par ordre d'impact)

1. **Base de données** : supprimer le **N+1**, ajouter les **index** utiles, `only()` / `values()`, paginer, agréger en SQL (section 9). C'est presque toujours **là** que se trouve le goulot.
2. **Cache** : fragments, vues, objets coûteux, Redis (section 13).
3. **Tâches lentes en arrière-plan** (section 23).
4. **Statiques via CDN / serveur web**, compression, cache HTTP.
5. **Connexions** : pool psycopg (`"pool": True`) ou **PgBouncer** ; `CONN_MAX_AGE`.
6. **Serveur d'application** : nombre de workers adapté, `gthread` / async si E/S.

**Pourquoi les connexions comptent.** Établir une connexion PostgreSQL coûte plusieurs millisecondes (négociation, authentification). Sans réutilisation, chaque requête la paie. Un **pool** garde des connexions ouvertes et les prête ; **PgBouncer** joue ce rôle au niveau de l'infrastructure quand de nombreux processus se connectent à la même base (PostgreSQL gère mal des milliers de connexions simultanées).

### 27.3 Pagination et gros volumes

```python
# python manage.py shell
from django.core.paginator import Paginator

qs = Article.objects.publies()
paginator = Paginator(qs, 25)                                   # ou CursorPagination (DRF) : pagination par « curseur » stable et rapide
print(paginator.num_pages, len(paginator.page(1).object_list))

for article in qs.iterator(chunk_size=2000):                    # mémoire constante
    print(article.titre)

auteur = Utilisateur.objects.first()
objets = [Article(titre=f"Lot {i}", slug=f"lot-{i}", contenu="x", auteur=auteur) for i in range(5000)]
Article.objects.bulk_create(objets, batch_size=1000)
```

- `Paginator` compte le total (une requête `COUNT(*)`, coûteuse sur de grandes tables) puis découpe avec `LIMIT/OFFSET`.
- **`iterator(chunk_size=…)`** lit par paquets via un curseur serveur : la mémoire reste constante même sur des millions de lignes, mais le cache du QuerySet est désactivé (on ne peut parcourir qu'une fois).
- **`bulk_create`** regroupe les insertions : 5 000 insertions en quelques requêtes au lieu de 5 000.

> **`OFFSET` élevé est lent** sur de très grandes tables (la base doit lire puis jeter toutes les lignes précédentes). Préférez la **pagination par curseur** (« donne-moi les 20 lignes après la clé d'ordre X ») : coût constant, résultats stables si des données arrivent pendant la navigation.

### 27.4 Modèles et templates

- `{% cache %}` pour les blocs coûteux ; le chargeur de templates **mis en cache** est activé automatiquement hors `DEBUG` (les fichiers ne sont pas relus à chaque requête).
- Évitez les **requêtes dans les templates** (boucles sur des relations non préchargées) ; préparez les données dans la vue.
- `django.contrib.humanize` et filtres lourds : à utiliser avec mesure.
- Index de base : un index **composite** (`Meta.indexes`) qui correspond à vos filtres+tris les plus fréquents vaut mieux que plusieurs index isolés ; vérifiez avec `explain()` qu'il est utilisé.

### 27.5 Serveur d'application

```bash
gunicorn config.wsgi:application --workers 5 --threads 2 --worker-class gthread --timeout 30 --max-requests 1000 --max-requests-jitter 100 --bind 0.0.0.0:8000
```

| Réglage | Conseil |
| --- | --- |
| `--workers` | Environ **(2 × cœurs) + 1** pour des charges mixtes (à ajuster selon la mémoire disponible) |
| `--threads` | Quelques threads (`gthread`) pour les E/S |
| `--max-requests` (+ `jitter`) | Recycle les processus (limite les fuites mémoire) ; le *jitter* évite que tous redémarrent ensemble |
| `--timeout` | Bas : un worker bloqué est tué et remplacé |
| ASGI | `uvicorn` / `granian` pour l'asynchrone |

Un **worker** est un processus Python indépendant : il consomme de la mémoire (donc `workers × mémoire par worker` doit tenir dans la machine) et utilise un cœur à la fois (à cause du GIL). Les **threads** permettent d'avancer sur d'autres requêtes pendant qu'une attend la base ou le réseau. Chaque worker ouvre ses connexions à la base : **dimensionnez le total des connexions** (`workers × threads`) par rapport aux limites de PostgreSQL.

### 27.6 Performances côté réseau et navigateur

- **GZip / Brotli** (au niveau Nginx / CDN), `ConditionalGetMiddleware`, en-têtes `Cache-Control` sur les statiques hachés.
- Images optimisées (**WebP/AVIF**, tailles multiples avec `sorl-thumbnail` / `easy-thumbnails` / `django-imagekit`), chargement paresseux (`loading="lazy"`).
- HTTP/2 ou 3, CDN pour statiques et médias.
- Côté navigateur, souvent plus déterminant que le serveur : poids des images, JavaScript bloquant, polices. Mesurez avec Lighthouse / les **Core Web Vitals**.

### Pièges fréquents

| Piège | Remède |
| --- | --- |
| Optimiser sans mesurer | Profil avant/après, p95 |
| Cache qui masque un N+1 | Corriger la requête d'abord, cacher ensuite |
| Trop de workers (mémoire / connexions SQL saturées) | Dimensionner selon RAM et limites de la base |
| `OFFSET` immense | Pagination par curseur |
| Tests de charge sur une base vide | Jeu de données réaliste |

### À retenir

- **Mesurer d'abord** ; le gain principal vient presque toujours de la **base de données** (N+1, index, agrégats).
- Puis cache, tâches déportées, statiques/CDN, pool de connexions et dimensionnement des workers.
- Suivez la **latence p95**, pas seulement la moyenne.

---

## 28. Déploiement

### Objectifs d'apprentissage

Schematiser une architecture de production ; appliquer la liste de contrôle de mise en ligne ; conteneuriser avec Docker (multi-étapes, `uv`) et orchestrer avec Compose ; configurer un proxy inverse (Nginx/Caddy) ; mettre en place santé et supervision ; réaliser des migrations **sans interruption** ; choisir une plateforme ; construire un pipeline CI/CD.

### 28.1 Vue d'ensemble

```text
Internet ─> Proxy / CDN (Nginx, Caddy, Cloudflare)
              ├─> Statiques (WhiteNoise / Nginx / CDN)
              └─> Gunicorn / Uvicorn (Django) ──> PostgreSQL · Redis
                                                  └─> Workers (Celery / Tasks) · Beat
```

| Élément | Rôle |
| --- | --- |
| **Proxy inverse** | Termine HTTPS, sert les statiques, protège, relaie vers l'application |
| **Serveur d'application** | Exécute Django (Gunicorn en WSGI ; Uvicorn/Daphne/Granian en ASGI) |
| **Base de données** | PostgreSQL (jamais exposée publiquement) |
| **Redis** | Cache, sessions, courtier de tâches, couche Channels |
| **Workers + planificateur** | Tâches en arrière-plan (une seule instance de `beat`) |

### 28.2 Liste de contrôle

- [ ] `DEBUG = False`, `SECRET_KEY` et secrets en **variables d'environnement**
- [ ] `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, HTTPS, HSTS (voir section 26)
- [ ] **PostgreSQL** (pas SQLite), sauvegardes automatiques **testées**
- [ ] `collectstatic` exécuté, statiques servis efficacement
- [ ] **Migrations** appliquées (étape de déploiement dédiée)
- [ ] Journaux vers la sortie standard, **Sentry** pour les erreurs
- [ ] Serveur d'application (Gunicorn / Uvicorn), **proxy inverse**, **workers** et planificateur
- [ ] **Surveillance** (santé, métriques, alertes), `check --deploy` au vert

### 28.3 Docker et Compose

> **Définition — conteneur.** Processus isolé embarquant l'application **et** ses dépendances : le même **image** tourne à l'identique sur votre poste, en CI et en production. Un **Dockerfile** décrit comment construire l'image ; **Docker Compose** orchestre plusieurs conteneurs (web, base, Redis, workers).

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

**Pourquoi ce Dockerfile ?**

- **Multi-étapes** (`AS base`, `AS deps`, `AS final`) : l'étape des dépendances est **mise en cache** tant que `pyproject.toml` / `uv.lock` ne changent pas → constructions rapides ; l'image finale ne contient que le nécessaire.
- `uv sync --frozen --no-dev` : installe **exactement** les versions verrouillées, sans outils de développement.
- **Utilisateur non root** (`USER app`) : si l'application est compromise, l'attaquant n'a pas les pleins pouvoirs dans le conteneur.
- `collectstatic` à la **construction** avec une `SECRET_KEY` factice (Django exige un réglage valide pour démarrer, mais cette valeur n'est pas conservée dans l'image déployée).
- `HEALTHCHECK` : l'orchestrateur sait quand le conteneur est réellement opérationnel (vue `/sante/`, 28.5).

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
    environment: { POSTGRES_DB: monsite, POSTGRES_USER: monsite, POSTGRES_PASSWORD: "${DB_PASSWORD}" }
    volumes: [pgdata:/var/lib/postgresql/data]
    healthcheck: { test: ["CMD-SHELL", "pg_isready -U monsite"], interval: 5s, retries: 10 }
  redis:
    image: redis:7-alpine
volumes:
  pgdata:
```

> Exécutez les **migrations** dans une **étape de déploiement** (`python manage.py migrate --noinput` en *release command* / *init container*), **pas** dans chaque instance au démarrage : sinon plusieurs instances lancent la même migration simultanément.

### 28.4 Nginx (proxy inverse)

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

- `X-Forwarded-Proto` informe Django que la requête d'origine était en **HTTPS** (sans cela, `SECURE_SSL_REDIRECT` provoquerait une boucle de redirections) ; ce mécanisme n'est sûr que si **seul** le proxy peut joindre l'application.
- `client_max_body_size` doit être cohérent avec vos limites de téléversement ; `expires 1y` + `immutable` conviennent aux statiques **hachés**.
- **Caddy** (HTTPS automatique, configuration minimale) : `exemple.fr { reverse_proxy 127.0.0.1:8000 }`.

### 28.5 Vue de santé et supervision

```python
# apps/accueil/views.py
from django.db import connection
from django.http import JsonResponse

def sante(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"statut": "ok"})
    except Exception:
        return JsonResponse({"statut": "erreur"}, status=503)

# apps/accueil/urls.py : urlpatterns += [path("sante/", sante, name="sante")]
```

Outils : **`django-health-check`**, **Sentry** (`sentry-sdk[django]`), Prometheus (`django-prometheus`), OpenTelemetry, journaux JSON (`python-json-logger`, `structlog`).

```python
import sentry_sdk

sentry_sdk.init(dsn=env("SENTRY_DSN"), send_default_pii=False, traces_sample_rate=0.1, environment="production")
```

`send_default_pii=False` évite d'envoyer des données personnelles à Sentry ; `traces_sample_rate=0.1` n'échantillonne que 10 % des requêtes pour limiter le coût. Les **trois piliers de l'observabilité** : **journaux** (ce qui s'est passé), **métriques** (chiffres agrégés dans le temps), **traces** (le parcours d'une requête).

### 28.6 Déploiements sans interruption

Appliquez le motif **expand / contract** (« étendre puis contracter ») : (1) **ajouter** colonnes/tables de façon **rétrocompatible** ; (2) déployer le code qui gère les **deux** schémas ; (3) **nettoyer** ensuite (supprimer l'ancien). Pendant un déploiement progressif, l'**ancienne** et la **nouvelle** version du code tournent **en même temps** sur la **même base** : le schéma doit convenir aux deux.

```python
# Exemple : ajouter un index sans verrouiller la table (PostgreSQL)
from django.contrib.postgres.operations import AddIndexConcurrently
from django.db import migrations, models

class Migration(migrations.Migration):
    atomic = False                                   # obligatoire pour les opérations « CONCURRENTLY »
    dependencies = [("blog", "0005_article_note")]
    operations = [AddIndexConcurrently("article", models.Index(fields=["statut"], name="article_statut_idx"))]
```

- **Ajouter une colonne `NOT NULL`** : (1) la créer `null=True` (ou avec `db_default`), (2) remplir par lots, (3) poser la contrainte ensuite.
- **Renommer / supprimer une colonne** : ne jamais dans le même déploiement que le code qui cesse de l'utiliser ; supprimez **après** le déploiement du code qui l'ignore.
- Évitez les migrations qui **réécrivent** ou **verrouillent** de grosses tables ; ajoutez les index avec `AddIndexConcurrently` ; utilisez des **déploiements progressifs** (*rolling*) et des **sondes de santé**.

### 28.7 Plateformes d'hébergement

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

**Comment choisir ?** Une équipe petite ou un MVP : un **PaaS** (zéro administration système, mise à l'échelle simple, coût plus élevé à grande échelle). Un contrôle fin et un coût maîtrisé : un **VPS** + Docker Compose / Kamal (vous gérez mises à jour système, sauvegardes, sécurité). De fortes exigences de disponibilité et d'échelle : **cloud managé** ou **Kubernetes** (puissant, mais lourd à opérer).

### 28.8 Intégration et livraison continues

Pipeline typique : **lint + types + tests** → **construction de l'image** → **analyse** (`pip-audit`, Trivy) → **déploiement** (migrations, `collectstatic`, redémarrage) → **vérification de santé** → **retour arrière** automatique en cas d'échec.

- **CI** (*Continuous Integration*) : chaque modification est construite et testée automatiquement. **CD** (*Continuous Delivery / Deployment*) : la livraison en production est automatisée (ou déclenchée en un clic).
- Une image **immuable** (identifiée par le hachage du commit) est promue telle quelle de test à production : on ne reconstruit pas « pour la prod ».
- Prévoyez le **retour arrière** (redéployer l'image précédente) — et pour la base, des migrations **rétrocompatibles** (28.6).

### Pièges fréquents

| Piège | Remède |
| --- | --- |
| `migrate` lancé par chaque instance au démarrage | Étape de déploiement unique |
| Boucle de redirections HTTPS derrière un proxy | `SECURE_PROXY_SSL_HEADER` + `X-Forwarded-Proto` |
| Statiques manquants en production | `collectstatic` + proxy/WhiteNoise configurés |
| Sauvegardes jamais restaurées | Tester régulièrement la restauration |
| Secrets dans l'image Docker | Variables d'environnement / gestionnaire de secrets |
| Migration qui verrouille une grosse table | `AddIndexConcurrently`, découpage en étapes |

### À retenir

- Architecture : **proxy → application → PostgreSQL/Redis + workers** ; **migrations en étape dédiée**.
- **Docker multi-étapes**, utilisateur non root, secrets hors de l'image ; santé + Sentry + métriques.
- Migrations **rétrocompatibles** (expand / contract) pour déployer sans interruption.

---

## 29. Écosystème : paquets essentiels

*(Section ajoutée : les paquets utiles avec Django, y compris ceux qui manquaient au guide d'origine.)*

### Objectifs d'apprentissage

Savoir **quel paquet** répond à quel besoin ; composer un `pyproject.toml` de départ cohérent ; **évaluer** la qualité et le risque d'une dépendance avant de l'adopter ; reconnaître les cas où **ne pas** ajouter de paquet.

### 29.1 Pourquoi un écosystème ?

Django est « tout inclus » mais volontairement **extensible** : des milliers de paquets tiers (*apps réutilisables*) ajoutent des fonctions prêtes à l'emploi. Ils s'installent avec `uv add` / `pip install`, s'enregistrent dans `INSTALLED_APPS` (et parfois `MIDDLEWARE`, `urls.py`), et s'intègrent grâce à l'architecture MTV et aux signaux. Le répertoire de référence est **Django Packages** (djangopackages.org).

### 29.2 Carte des paquets par besoin

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
| **Recherche** | `django-haystack`, `django-elasticsearch-dsl`, clients Meilisearch / Typesense, `pgvector` (`pgvector-python`) pour les embeddings |
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

**Quelques notions à retenir sur ces familles :**

- **`django.contrib`** : Django embarque lui-même des apps optionnelles (`admin`, `auth`, `sessions`, `messages`, `staticfiles`, `sitemaps`, `postgres`, `gis`, `humanize`…) qui s'activent dans `INSTALLED_APPS`.
- **Machines d'états** (`django-fsm`) : modéliser un cycle de vie (commande : `brouillon → payée → expédiée`) avec des transitions explicites et validées plutôt qu'un champ texte modifié à volonté.
- **Suppression logique** (*soft delete*) : marquer une ligne comme supprimée au lieu de l'effacer (audit, restauration) ; attention aux requêtes qui doivent toutes filtrer les lignes « supprimées ».
- **Embeddings / `pgvector`** : stocker des vecteurs (recherche sémantique, IA) directement dans PostgreSQL.
- **CMS** : **Wagtail** est le CMS Django de référence (pages structurées, éditeur, workflows) ; à considérer avant de réinventer un système de contenu.

### 29.3 Exemple de `pyproject.toml` de départ

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

- `dependencies` : nécessaires **en production** ; `dev` : outils de développement et de test (non installés dans l'image de production avec `--no-dev`).
- `"django>=6.1,<6.2"` : accepte les correctifs `6.1.x` mais **pas** la version suivante (montée de version volontaire, section 30.2).
- Ne gardez que ce dont **vous avez besoin** : chaque paquet ajoute de la maintenance, de la surface d'attaque et des incompatibilités futures.

### 29.4 Choisir un paquet tiers

| Critère | À vérifier |
| --- | --- |
| **Compatibilité** | Versions de **Django** et **Python** supportées (classifiers PyPI, notes de version) |
| **Maintenance** | Dernière publication, issues ouvertes, nombre de mainteneurs |
| **Popularité** | Étoiles, téléchargements, **Django Packages** (djangopackages.org) |
| **Sécurité** | Historique de vulnérabilités, `pip-audit` |
| **Besoin réel** | Parfois quelques lignes de Django suffisent |

> Un paquet **abandonné** (ex. `django-ckeditor` v4, anciennes versions de `django-grappelli`…) est une **dette** : vérifiez avant d'adopter, et prévoyez une sortie si le projet s'arrête.

**Hygiène de la chaîne d'approvisionnement** (*supply chain*) : vérifiez l'orthographe du nom (attaques par *typosquatting* : un paquet au nom proche d'un paquet connu), verrouillez les versions (`uv.lock`), relisez les nouvelles dépendances et les mises à jour majeures, auditez régulièrement (`pip-audit`, Dependabot/Renovate).

### À retenir

- Un paquet répond à presque chaque besoin courant ; consultez **Django Packages** avant de coder.
- Évaluez : compatibilité, maintenance, sécurité, besoin réel. Évitez les paquets abandonnés.
- Verrouillez et auditez vos dépendances.

---

## 30. Nouveautés par version, bonnes pratiques et ressources

### Objectifs d'apprentissage

Situer les apports de chaque version de Django (4.2 → 6.1) ; **mettre à jour** un projet méthodiquement ; synthétiser les bonnes pratiques et les erreurs classiques ; savoir où continuer à apprendre.

### 30.1 Nouveautés notables (4.2 → 6.1)

| Version | Points marquants |
| --- | --- |
| **4.2 LTS** | Réglage `STORAGES`, `psycopg` 3, commentaires de colonnes, backend de cache Redis intégré (4.0) |
| **5.0** | **`db_default`**, **`GeneratedField`**, rendu des formulaires en `div` et `as_field_group`, **facettes** de l'admin, choix par mapping, `USE_TZ = True` par défaut, `ZoneInfo` |
| **5.1** | **`LoginRequiredMiddleware`**, balise **`{% querystring %}`**, **pool de connexions** PostgreSQL, `CheckConstraint(condition=…)`, suppression de `DEFAULT_FILE_STORAGE` / `index_together` |
| **5.2 LTS** | **Clés primaires composites** (`CompositePrimaryKey`), `shell` qui importe automatiquement les modèles, améliorations de l'admin et de l'ORM |
| **6.0** | **Framework de tâches** (`django.tasks`), **CSP intégrée**, **partiels de template** (`{% partialdef %}`), `BigAutoField` par défaut, Python 3.12+ |
| **6.1** | **Modes de chargement** (`fetch_mode`), `on_delete` **au niveau base** (`DB_CASCADE`…), réglage **`MAILERS`**, fonctions `UUID4` / `UUID7`, `JSONNull`, agrégats de bits |
| **6.2 LTS** *(prévue avril 2027)* | Prochaine version à support long terme |

**Lecture pédagogique :** ces apports se rattachent aux sections du cours.

| Thème | Où le retrouver |
| --- | --- |
| Stockage (`STORAGES`), `db_default`, `GeneratedField`, clés composites, `on_delete` en base | Sections 4.4, 8 |
| `LoginRequiredMiddleware`, `fetch_mode` | Sections 12.4, 9.5 |
| `{% querystring %}`, `partialdef`, rendu `div` / `as_field_group` | Sections 7, 11 |
| Pool de connexions, UUID7 | Sections 4.3, 8.3, 27 |
| Framework de tâches, CSP | Sections 23.2, 26.3 |
| `MAILERS` | Section 4.5 |

> Pour le détail exact (et les suppressions de fonctionnalités dépréciées), lisez les **notes de version** : [docs.djangoproject.com/en/6.1/releases/](https://docs.djangoproject.com/en/6.1/releases/). Les fonctionnalités les plus récentes (6.0, 6.1) sont à vérifier particulièrement avant un usage en production.

### 30.2 Mettre à jour Django *(ajout)*

1. **Passez de LTS en LTS** ou version par version (ne sautez pas plusieurs versions d'un coup).
2. Lisez les **notes de version** et la section « *Features deprecated* ».
3. Lancez les tests avec les avertissements visibles ou transformés en erreurs :

   ```bash
   python -Wa manage.py test           # affiche les DeprecationWarning
   pytest -W error::DeprecationWarning
   ```
4. **`django-upgrade`** réécrit automatiquement le code : `django-upgrade --target-version 6.1 $(git ls-files '*.py')`.
5. Vérifiez la **compatibilité des paquets tiers** et la **version de Python**.
6. Testez, déployez en **préproduction**, surveillez.

**Pourquoi cette méthode ?** Grâce à la politique de dépréciation (section 1.4), un projet **sans avertissement** sur la version N passe sur N+1 : traiter les avertissements **au fil de l'eau** transforme les montées de version en opérations de routine. Le pire scénario est le projet figé sur une version en fin de support, qui doit sauter plusieurs versions d'un coup sous la pression d'une faille de sécurité.

Exemples de suppressions courantes lors des migrations récentes : `DEFAULT_FILE_STORAGE` / `STATICFILES_STORAGE` → `STORAGES` ; `USE_L10N` et **pytz** → `zoneinfo` ; `CheckConstraint(check=…)` → `condition=` ; `index_together` → `indexes` ; `EMAIL_*` → `MAILERS` (avant Django 7.0).

### 30.3 Bonnes pratiques générales

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

### 30.4 Les erreurs classiques

- `DEBUG = True` en production · secrets dans Git · `ALLOWED_HOSTS = ["*"]`.
- **N+1** non détecté · absence d'index · `len(qs)` au lieu de `qs.count()`.
- `fields = "__all__"` · pas de contrôle de propriété (**IDOR**) · logique dans les templates.
- Modèle utilisateur par défaut puis changement tardif · migrations modifiées après déploiement.
- Tâche Celery lancée **avant** la validation de la transaction · objets passés aux tâches au lieu d'identifiants.
- Bloquer la boucle asynchrone avec du code synchrone · CORS ouvert à tous.

### 30.5 Ressources

- **Documentation officielle** : <https://docs.djangoproject.com/fr/>
- **Tutoriel officiel** (sondages) : <https://docs.djangoproject.com/fr/6.1/intro/tutorial01/>
- **Notes de version** : <https://docs.djangoproject.com/en/6.1/releases/>
- **Django Packages** : <https://djangopackages.org> · **PyPI** : <https://pypi.org>
- **Classy Class-Based Views** : <https://ccbv.co.uk> · **Classy DRF** : <https://www.cdrf.co>
- **DRF** : <https://www.django-rest-framework.org> · **Django Ninja** : <https://django-ninja.dev> · **Celery** : <https://docs.celeryq.dev>
- **Sécurité Django** : <https://docs.djangoproject.com/fr/6.1/topics/security/> · **OWASP** : <https://owasp.org>
- *Two Scoops of Django* (Greenfeld & Roy), *Django for Professionals / APIs* (William S. Vincent), blog d'**Adam Johnson**, blog de **Simon Willison**, **Django News** (newsletter).

### 30.6 Parcours d'apprentissage suggéré

| Étape | Sections | Objectif |
| --- | --- | --- |
| **1. Bases** | 1 à 7 | Créer un site de pages dynamiques (URLs, vues, templates) |
| **2. Données** | 8 à 11 | Modèles, ORM, admin, formulaires : un blog complet avec CRUD |
| **3. Comptes et services** | 12 à 18 | Authentification, cache, fichiers, middleware, signaux, i18n, commandes |
| **4. API et temps réel** | 19 à 24 | API sécurisée, tâches, asynchrone, interface moderne |
| **5. Production** | 25 à 30 | Tests, sécurité, performances, déploiement, maintenance |

**Projet de synthèse proposé.** Construisez une mini-boutique : catalogue (modèles + admin), panier (sessions), commande atomique (transactions + `select_for_update`), paiement simulé (webhook signé), e-mails de confirmation (tâche), API de consultation (DRF + JWT), interface avec HTMX, tests et CI, conteneurisation et déploiement. C'est l'ensemble du cours mis en pratique.

### Glossaire récapitulatif

| Terme | Définition courte |
| --- | --- |
| **ASGI / WSGI** | Interfaces serveur–framework (asynchrone / synchrone) |
| **Application (app)** | Module Django à responsabilité unique, enregistré dans `INSTALLED_APPS` |
| **CBV / FBV** | Vue basée sur une classe / sur une fonction |
| **Context processor** | Fonction qui ajoute des variables à tous les templates |
| **CORS** | Mécanisme du navigateur contrôlant les requêtes inter-origines |
| **CSP** | Politique limitant les sources de contenu autorisées (anti-XSS) |
| **CSRF** | Requête modifiante forgée depuis un autre site ; parade : jeton |
| **DRY** | Ne pas se répéter : une seule source de vérité |
| **Fixture / factory** | Données de test sérialisées / fabriquées par code |
| **Idempotence** | Rejouer une opération ne change pas le résultat final |
| **IDOR** | Accès à l'objet d'un autre par simple changement d'identifiant |
| **JWT** | Jeton signé, autoporteur, encodé (non chiffré) |
| **Manager / QuerySet** | Interface de requête d'un modèle / requête paresseuse et chaînable |
| **Middleware** | Couche qui enveloppe le traitement de chaque requête |
| **Migration** | Fichier versionné décrivant une évolution du schéma |
| **MTV** | Modèle–Template–Vue : le motif architectural de Django |
| **N+1** | 1 requête + N requêtes pour charger des relations |
| **ORM** | Correspondance classes ↔ tables, objets ↔ lignes |
| **PRG** | Post/Redirect/Get : rediriger après un POST réussi |
| **Signal** | Notification découplée entre composants (motif observateur) |
| **SSRF** | Faire appeler une adresse interne par le serveur |
| **Transaction** | Groupe d'opérations atomique (tout ou rien) |
| **URLconf** | Table d'association URL → vue |
| **Worker** | Processus qui exécute des tâches en arrière-plan (ou des requêtes) |
| **XSS** | Injection de script exécuté dans le navigateur de la victime |

### À retenir

- Restez sur une version **supportée** ; traitez les dépréciations **au fil de l'eau** ; passez de LTS en LTS.
- Les bonnes pratiques se résument en : **structure claire, base optimisée, sécurité par défaut, tests et CI, déploiement reproductible**.
- La documentation officielle et les notes de version restent votre référence finale.

---

*Fin du cours. Bon développement avec Django !*
