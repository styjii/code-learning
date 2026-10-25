# Code Learning

> Des cours de programmation **en français**, des blocs de code **exécutables dans le navigateur** et des **éditeurs en ligne HTML / CSS / JS, Python et HTML / CSS / TypeScript**, dans une seule application Django.

[![CI](https://github.com/styjii/code-learning/actions/workflows/ci.yml/badge.svg)](https://github.com/styjii/code-learning/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.12%2B-3776ab?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.1%2B-092e20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django%20REST%20framework-3.15%2B-a30000)
![Monaco](https://img.shields.io/badge/Monaco%20Editor-0.47-0078d4)
![Pyodide](https://img.shields.io/badge/Pyodide-Python%203.14-ffd43b)
![Licence](https://img.shields.io/badge/licence-propri%C3%A9taire-lightgrey)

![Aperçu de l'éditeur de code](static/images/editor.png)

## Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Cours disponibles](#cours-disponibles)
- [Stack technique](#stack-technique)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Les éditeurs en ligne](#les-éditeurs-en-ligne)
- [Raccourcis clavier](#raccourcis-clavier)
- [Architecture](#architecture)
- [Ajouter ou modifier un cours](#ajouter-ou-modifier-un-cours)
- [Code exécutable dans les cours](#code-exécutable-dans-les-cours)
- [Configuration (`.env`)](#configuration-env)
- [Sécurité](#sécurité)
- [Déploiement en production](#déploiement-en-production)
- [Tests](#tests)
- [Intégration continue](#intégration-continue)
- [Contribuer](#contribuer)
- [Dépannage](#dépannage)
- [Licence et auteur](#licence-et-auteur)

## Fonctionnalités

**Cours**
- 22 pages de cours écrites en Markdown, converties en pages web à onglets (une section = un onglet).
- Accueil avec catalogue filtrable par catégorie et par texte.
- Dans chaque cours : barre latérale des sections, plan « Sur cette page » avec suivi du défilement, boutons précédent / suivant, recherche plein texte, barre de progression de lecture, bouton « retour en haut ».
- Coloration syntaxique (Pygments), bouton **Copier** sur chaque bloc de code, ancres sur les titres.
- Thème clair / sombre, mémorisé dans le navigateur.

**Code exécutable**
- Les blocs JavaScript, TypeScript et Python ont un bouton **Exécuter** : ils deviennent un éditeur modifiable avec sa zone de résultat.
- Tout s'exécute **dans le navigateur** (Web Worker isolé pour JS, Pyodide pour Python) : aucun code utilisateur n'est exécuté sur le serveur.

**Éditeurs en ligne** (commutateur *Web | Python | TypeScript* en haut de chaque éditeur)
- **Web** (`/editor/`) : onglets HTML / CSS / JS propulsés par Monaco Editor (le moteur de VS Code), avec Emmet et des snippets JavaScript. Aperçu dans une iframe isolée, console intégrée, aperçu automatique avec délai réglable, option Bootstrap en un clic.
- **TypeScript** (`/editor/typescript/`) : mêmes projets, aperçu et import / export, avec onglets HTML / CSS / **TS**. Le code est vérifié et compilé dans le navigateur (compilateur de Monaco) ; les erreurs de type sont soulignées et listées dans la console. **Options du compilateur** par projet (`target`, `strict`, `noUnusedLocals`...), écrites dans le `tsconfig.json` de l'export.
- **Python** (`/editor/python/`) : plusieurs fichiers (`main.py` + modules importables), exécution dans Pyodide, `input()` interactif dans la console, bouton **Arrêter**. Les fichiers sont conservés **dans le navigateur**, pas sur le serveur.
- **Projets** Web et TypeScript enregistrés par utilisateur, **import / export .zip**.
- Préférences d'éditeur (retour à la ligne, taille de tabulation, minimap...) propres à chaque compte.

**Comptes et sécurité**
- Toute page exige une connexion ; pas d'inscription publique (les comptes sont créés par l'administrateur).
- Blocage temporaire après plusieurs échecs de connexion, protection CSRF, aperçu en bac à sable, import zip plafonné. Détails : [Sécurité](#sécurité).

## Cours disponibles

| Catégorie | Contenu |
|---|---|
| **Langages & outils** | CSS, JavaScript, TypeScript, Python, PHP, Langage C, Git, Algorithmique |
| **Frameworks** | Angular, Django |
| **Modules** | Modules Python (bibliothèque standard), BeautifulSoup |
| **Exercices** | JavaScript, TypeScript, C, Algorithmique |
| **Corrigés** | JavaScript, TypeScript, C, Algorithmique |
| **Projets** | JavaScript (Node.js), C |

## Stack technique

| Couche | Technologies |
|---|---|
| Backend | Python, Django 5.1+, Django REST framework |
| Contenu | Markdown, Pygments, BeautifulSoup 4, cache en base (modèle `PageContent`) |
| Données | SQLite (`db.sqlite3`) : utilisateurs, projets, préférences, contenu des cours |
| Frontend | JavaScript natif (modules ES), CSS maison avec thème clair / sombre |
| Éditeur | Monaco Editor 0.47, Emmet |
| Exécution navigateur | Web Workers, TypeScript (compilateur de Monaco), Pyodide (CPython 3.14 en WebAssembly) |
| Option de l'éditeur | Bootstrap 5.3, activable dans l'aperçu |
| Intégration continue | GitHub Actions, GitHub CLI (`gh`) |

Monaco, Pyodide et Bootstrap sont **embarqués** dans le dépôt (`static/`) : l'application ne dépend d'aucun CDN externe.

## Installation

### Prérequis

- Python 3.12 ou plus récent (testé en CI avec Python 3.12 et 3.13, Django 6.1)
- `git` et `pip`

### Étapes

```bash
# 1. Récupérer le code
git clone https://github.com/styjii/code-learning.git
cd code-learning

# 2. Environnement virtuel
python -m venv .venv
source .venv/bin/activate          # Windows (PowerShell) : .venv\Scripts\Activate.ps1

# 3. Dépendances
pip install -r requirements.txt

# 4. Configuration
cp .env.example .env               # Windows : copy .env.example .env
```

Éditez ensuite `.env` :

```ini
DJANGO_SECRET_KEY=<une clé générée, voir ci-dessous>
DJANGO_DEBUG=1                     # développement local
```

Pour générer une clé secrète :

```bash
python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"
```

```bash
# 5. Base de données et premier compte
python manage.py migrate
python manage.py createsuperuser

# 6. Lancer
python manage.py runserver
```

Ouvrez <http://127.0.0.1:8000/> et connectez-vous.

> **Important en local :** gardez `DJANGO_DEBUG=1`. Avec `DJANGO_DEBUG=0` (valeur du `.env.example`), la redirection HTTPS est active et `runserver` ne sert plus les fichiers statiques.

## Utilisation

1. **Connexion** sur `/accounts/login/`. Il n'y a pas d'inscription : créez les comptes avec `createsuperuser`, ou dans `/admin/` (*Utilisateurs > Ajouter*).
2. **Premier lancement** : l'accueil convertit les cours un par un et affiche une barre de progression (annulable). Les pages sont ensuite servies depuis le cache.
3. **Cours** : choisissez une carte sur l'accueil, naviguez par sections, recherchez avec `/` ou `Ctrl + K`.
4. **Éditeurs** : bouton `</>` en haut d'un cours, ou directement <http://127.0.0.1:8000/editor/>. Le commutateur **Web | Python | TypeScript** passe de l'un à l'autre (détails : [Les éditeurs en ligne](#les-éditeurs-en-ligne)).
   - **Web et TypeScript** : onglets de code, bouton **Exécuter**, bouton **Console**. Menu `⋯` : **Projets** (créer, changer, supprimer), **Import / export .zip**, **Aperçu automatique**, **Bibliothèques (CDN)** (active Bootstrap dans l'aperçu, servi depuis le projet) et, en TypeScript, **Options TypeScript**.
   - **Python** : onglets de fichiers, bouton **Exécuter** / **Arrêter**, menu `⋯` : **Nouveau fichier**, **Importer des fichiers**, **Télécharger le fichier actif**, **Remplacer par l'exemple**.

## Les éditeurs en ligne

Les trois éditeurs partagent la même interface (Monaco, console, thème clair / sombre) mais pas le même stockage :

| Éditeur | Langage exécuté | Où sont les fichiers ? | Export |
|---|---|---|---|
| Web | HTML, CSS, JavaScript (aperçu en iframe isolée) | base de données, par utilisateur | `index.html`, `style.css`, `script.js` |
| TypeScript | HTML, CSS, TypeScript compilé en JavaScript | base de données, par utilisateur | `index.html`, `style.css`, `script.ts`, `tsconfig.json` |
| Python | Python 3.14 (Pyodide, Web Worker) | **navigateur** (`localStorage`) | fichier par fichier |

### Éditeur Python

- `main.py` est le point d'entrée : il ne peut être ni renommé ni supprimé. Les autres fichiers `.py` sont importables (`import utils`) ; les fichiers `.txt`, `.json`, `.csv` et `.md` importés sont disponibles à côté du programme.
- `input()` est interactif : tapez directement dans la console. La zone repliable « Entrée standard » permet de préremplir une ligne par `input()`.
- **Enregistrement** : automatique, dans ce navigateur uniquement (indicateur « Enregistré dans ce navigateur », `Ctrl + S` pour forcer). Les fichiers ne suivent pas le compte et disparaissent si vous videz les données du site : utilisez **Télécharger le fichier actif** pour les sauvegarder.
- Le bouton **Arrêter** interrompt le programme ; un délai maximal de 5 minutes s'applique. Pyodide (~13 Mo) est chargé au premier lancement.
- Seules les préférences Monaco sont lues sur le serveur.

### Éditeur TypeScript

- Le TypeScript est compilé **dans le navigateur** ; le JavaScript produit est envoyé à `POST /editor/preview/` avec `module=1` et s'exécute comme **module ES** (`await` au premier niveau permis, variables non globales : pour un `onclick`, écrire `window.maFonction = maFonction`).
- Menu « Options TypeScript » : `target` (ES5 à ESNext), `strict`, `noEmitOnError` (vrai : une erreur de type bloque l'exécution), `noUnusedLocals`, `noUnusedParameters`, `noImplicitReturns`, `noFallthroughCasesInSwitch`, `noUncheckedIndexedAccess`. `module: ESNext` est imposé. Le résumé des options actives s'affiche à côté du bouton **Console**.
- Les options sont enregistrées **par projet** (`TypeScriptProject.compiler_options`) et validées par liste blanche dans `editor/typescript_config.py` (clé inconnue ou valeur invalide : refus en `400`).
- Avec `target: ESNext`, les décorateurs ne sont pas transformés : utiliser `ES2022`.
- L'export ne contient pas de JavaScript : `npx tsc` produit `script.js`, que `index.html` charge en `type="module"` (à servir en HTTP, pas par `file://`). L'import relit `tsconfig.json` et ignore les clés non autorisées.

## Raccourcis clavier

| Contexte | Raccourci | Action |
|---|---|---|
| Cours | `/` ou `Ctrl/Cmd + K` | Ouvrir la recherche |
| Cours | `Échap` | Fermer la recherche |
| Bloc de code exécutable | `Ctrl + Entrée` | Relancer le code |
| Éditeurs | `Ctrl + Entrée` | Exécuter |
| Éditeur Web / TypeScript | `Ctrl + 1` / `2` / `3` | Onglet HTML / CSS / JS (ou TS) |
| Éditeur Web / TypeScript | `Maj + Alt + F` | Formater le document |
| Éditeur Web / TypeScript | `Ctrl + Maj + P` | Palette de commandes |
| Éditeur Web / TypeScript | `Ctrl + Alt + W` | Activer / désactiver le retour à la ligne |
| Éditeur Web / TypeScript | `Ctrl + Alt + L` | Activer / désactiver le défilement après la dernière ligne |
| Éditeur Python | `Ctrl + S` | Enregistrer dans le navigateur |
| Éditeur Python | `F2` / `Suppr` (onglet sélectionné) | Renommer / supprimer le fichier |

## Architecture

```text
code-learning/
├── config/        réglages Django (settings.py), routes, WSGI / ASGI
├── accounts/      connexion avec limitation des tentatives, tests d'accès
├── webapp/        accueil : catalogue des cours, préparation du contenu
├── language/      pages de cours (config.py = catalogue, topics/ = Markdown)
├── core/          conversion Markdown -> HTML à onglets
├── editor/        éditeurs Monaco (Web, Python, TypeScript), projets, aperçu, import/export zip, préférences
├── templates/     base.html et partials partagés (thème, logo, déconnexion)
├── static/        CSS/JS communs, polices, icônes, Bootstrap, Pyodide
├── manage.py
├── requirements.txt
└── .env.example
```

### Comment un cours devient une page

1. `language/config.py` est la **source unique de vérité** : il alimente les routes, l'accueil, le sélecteur de cours et la conversion.
2. À la première visite, `core/markdown_to_tabbed_html.py` convertit le `.md` en HTML structuré (un onglet par section).
3. Le résultat est stocké dans `db.sqlite3` (modèle `language.models.PageContent`), avec une **signature** (version du convertisseur + date et taille du fichier).
4. Quand un `.md` change, ou que `CONVERTER_VERSION` est incrémenté, la page est **régénérée automatiquement** à la visite suivante. Pour tout régénérer d'un coup : `python manage.py build_pages`.

### Éditeur : points d'API

| Route | Rôle |
|---|---|
| `GET/POST /editor/api/projects/` | liste / création des projets de l'utilisateur |
| `GET/PUT/DELETE /editor/api/projects/<id>/` | lecture / modification / suppression |
| `GET /editor/api/load-monaco-config/` | options Monaco de l'utilisateur connecté |
| `POST /editor/api/save-monaco-config/` | enregistre ses préférences (clés autorisées uniquement) |
| `POST /editor/api/export-zip/` | génère le `.zip` du projet |
| `POST /editor/api/import-zip/` | lit un `.zip` (plafonné) |
| `GET/POST /editor/api/ts-projects/`, `GET/PUT/DELETE /editor/api/ts-projects/<id>/` | projets de l'éditeur TypeScript (html, css, ts, `compiler_options`) |
| `POST /editor/api/ts-export-zip/` | `.zip` : `index.html`, `style.css`, `script.ts`, `tsconfig.json` |
| `POST /editor/api/ts-import-zip/` | lit ce `.zip` (mêmes plafonds) et renvoie aussi les options du `tsconfig.json` |
| `POST /editor/preview/` puis `GET /editor/preview/<id>/` | génère puis affiche l'aperçu (cinq derniers conservés) |

L'API répond `403` aux utilisateurs non connectés. L'éditeur Python n'utilise que `load-monaco-config` : ses fichiers restent dans le navigateur.

## Ajouter ou modifier un cours

**Modifier** : éditez le fichier dans `language/topics/`. La page est régénérée à la prochaine visite.

**Ajouter** :

1. Créez le fichier Markdown dans `language/topics/` (ou un sous-dossier).
2. Si besoin, ajoutez une icône SVG dans `static/icons/`.
3. Déclarez la page dans `language/config.py` :

   ```python
   Page("rust", "rust.md", "Rust", "topics", "icons/rust.svg", "#dea584",
        "Un langage système sûr et performant."),
   ```

   Les arguments sont : clé d'URL, fichier, titre, catégorie, icône, couleur d'accent, phrase d'accroche.
4. Rechargez l'accueil : la route `/language/rust/` et la carte du catalogue existent.

**Format Markdown attendu**

- Titre du document : un `<h1>` dans un bloc `<div align="center">`, ou un `# Titre` unique.
- Chaque `# Section` devient un onglet (à défaut, chaque `## Section`).
- Le contenu placé avant la première section devient l'onglet « Présentation ».
- Les titres reçoivent des identifiants façon GitHub : un sommaire `[Intro](#1-introduction)` fonctionne tel quel.

## Code exécutable dans les cours

Les blocs ` ```js `, ` ```ts ` et ` ```python ` ont un bouton **Exécuter** : le bloc devient un éditeur Monaco modifiable (`Ctrl + Entrée` pour relancer) avec sa zone de résultat.

| Langage | Moteur |
|---|---|
| JavaScript | Web Worker isolé (pas d'accès au DOM), arrêt automatique après 8 s |
| TypeScript | compilateur de Monaco (erreurs de type affichées), puis exécution comme JavaScript |
| Python | [Pyodide](https://pyodide.org) (CPython 3.14 en WebAssembly, ~13 Mo, chargé au premier clic), `input()` via la zone « Entrée standard », arrêt après 10 s |

- Seules les pages **Python, JavaScript et TypeScript** (niveau `topics`) ont des blocs exécutables. Pour en activer une autre, passez `runnable=True` sur sa `Page` dans `language/config.py`.
- Pour garder un bloc en lecture seule dans une page exécutable : ` ```python norun `.
- Les extraits JS/TS qui utilisent `import`, `export` ou `require()` ne sont pas exécutables et n'ont pas de bouton.
- Le C / C++ n'est pas encore pris en charge.
- Pyodide est embarqué dans `static/vendor/pyodide/` (licence MPL-2.0).

## Configuration (`.env`)

Toutes les valeurs sensibles sont lues dans `.env` (jamais versionné, voir `.gitignore`) ou dans l'environnement. Modèle commenté : `.env.example`. Le démarrage échoue avec un message explicite si `DJANGO_SECRET_KEY` manque.

| Variable | Rôle | Défaut |
|---|---|---|
| `DJANGO_SECRET_KEY` | clé secrète (**obligatoire**) | — |
| `DJANGO_DEBUG` | `1` développement, `0` production | `0` |
| `DJANGO_ALLOWED_HOSTS` | hôtes autorisés, séparés par des virgules (obligatoire si `DEBUG=0`) | — |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | origines HTTPS de confiance | — |
| `DJANGO_HTTPS` | cookies `Secure` + redirection HTTPS | actif si `DEBUG=0` |
| `DJANGO_HSTS_SECONDS` | durée HSTS en secondes (0 = désactivé) | `0` |
| `DJANGO_BEHIND_PROXY` | `1` derrière un proxy qui envoie `X-Forwarded-Proto` | `0` |
| `DJANGO_SESSION_HOURS` | durée d'une session | `168` |
| `DJANGO_LOGIN_MAX_ATTEMPTS` | échecs tolérés avant blocage | `5` |
| `DJANGO_LOGIN_LOCKOUT_SECONDS` | durée du blocage | `900` |
| `EDITOR_ZIP_MAX_UPLOAD_KB` | taille maximale du `.zip` envoyé | `5120` |
| `EDITOR_ZIP_MAX_FILE_KB` | taille décompressée maximale d'un fichier | `1024` |
| `EDITOR_ZIP_MAX_TOTAL_KB` | total décompressé maximal de l'archive | `5120` |
| `EDITOR_ZIP_MAX_ENTRIES` | nombre maximal de fichiers dans l'archive | `100` |

## Sécurité

- **Authentification** : `LoginRequiredMiddleware` redirige toutes les pages vers la connexion ; l'API REST répond `403` aux anonymes. Déconnexion par `POST` uniquement.
- **Force brute** : blocage temporaire après plusieurs échecs (par IP + identifiant). Le compteur utilise le cache Django (mémoire locale) : configurez un cache partagé si vous lancez plusieurs processus.
- **CSRF** : protection active sur tous les appels de l'éditeur.
- **Isolation des projets** : chaque utilisateur ne voit et ne modifie que les siens. Projets créés avant l'authentification (sans propriétaire) : rattachez-les avec

  ```bash
  python manage.py shell -c "from editor.models import Project as P; from django.contrib.auth import get_user_model as g; P.objects.filter(owner=None).update(owner=g().objects.get(username='VOTRE_NOM'))"
  ```

- **Préférences Monaco** : enregistrées **par utilisateur** en base (`EditorPreferences`), jamais dans un fichier du code source. Seules les clés de la liste blanche de `editor/monaco_config.py` sont acceptées, avec type et plage vérifiés ; `readOnly`, `value`, `theme`... sont refusés. Le thème suit celui du site (navigateur).
- **Import .zip** : taille du fichier, nombre d'entrées, taille de chaque fichier et total décompressé sont plafonnés (`EDITOR_ZIP_*`), contrôlés **avant** toute décompression ; refus en `413`. En production, ajoutez aussi une limite côté serveur web (ex. nginx `client_max_body_size 6m;`).
- **Options TypeScript** : liste blanche dans `editor/typescript_config.py` (type et valeur vérifiés, clés inconnues refusées), à l'écriture comme à la lecture ; `module` est imposé et non modifiable.
- **Aperçu** : servi avec `Content-Security-Policy: sandbox` et dans une iframe `sandbox` : le code de l'utilisateur ne peut pas utiliser sa session.
- **Clickjacking** : `X-Frame-Options: DENY` sur le site (sauf l'aperçu, volontairement intégrable).

## Déploiement en production

1. Dans `.env` : `DJANGO_DEBUG=0`, `DJANGO_SECRET_KEY` unique, `DJANGO_ALLOWED_HOSTS=votre-domaine.fr`, `DJANGO_CSRF_TRUSTED_ORIGINS=https://votre-domaine.fr`.
2. Servez en HTTPS. Derrière un proxy inverse, ajoutez `DJANGO_BEHIND_PROXY=1`. Une fois HTTPS validé, activez HSTS (ex. `DJANGO_HSTS_SECONDS=31536000`).
3. Appliquez les migrations et collectez les fichiers statiques :

   ```bash
   python manage.py migrate
   python manage.py collectstatic
   ```

4. Lancez l'application avec un serveur WSGI de votre choix (gunicorn, uWSGI...) derrière nginx ou Apache.
5. Servez `staticfiles/` avec votre serveur web (ou WhiteNoise). Le dossier est volumineux (Monaco, Pyodide) : activez la compression et le cache navigateur.
6. Le dossier du projet doit être **inscriptible** par l'application : `db.sqlite3` y est créé.
7. Pensez à sauvegarder `db.sqlite3` (comptes, projets). Le contenu des cours (`PageContent`) n'est qu'un cache, régénéré automatiquement.

## Tests

Les tests ont besoin d'une clé secrète : avec un `.env` en place, rien à faire ; sinon `export DJANGO_SECRET_KEY=test DJANGO_DEBUG=1` (PowerShell : `$env:DJANGO_SECRET_KEY="test"; $env:DJANGO_DEBUG="1"`).

```bash
python manage.py test accounts editor language   # authentification, isolation des projets, CSRF, config Monaco, import zip, cache des cours, éditeur TypeScript
python manage.py test editor.test_typescript     # un seul module : options du compilateur, projets TS, zip TS, aperçu en module
python -m pytest core                            # conversion Markdown
python manage.py makemigrations --check --dry-run  # un modèle modifié sans migration fait échouer la commande
```

La syntaxe des modules JavaScript du site est vérifiée en CI (voir ci-dessous) ; en local : `node --check fichier.mjs` (copiez le fichier en `.mjs` pour que `import` / `export` soient acceptés).

## Intégration continue

Le workflow [`.github/workflows/ci.yml`](.github/workflows/ci.yml) se lance à chaque **push** (toutes les branches) et à chaque **Pull Request**. Un push sur une branche qui a déjà une PR ouverte est ignoré (la CI de la PR le couvre) : c'est le job `Contexte (gh)` qui le détecte.

| Job | Quand | Rôle |
|---|---|---|
| `Contexte (gh)` | toujours | vérifie le dépôt visé (`styjii/code-learning`) et évite les doublons push / PR |
| `Tests (Python 3.12 / 3.13)` | push, PR | `manage.py check`, migrations manquantes, tests Django, `pytest core` |
| `Syntaxe JavaScript` | push, PR | `node --check` sur tous les modules du site |
| `Vérifications de la PR (gh)` | PR | `.github/scripts/pr-checks.sh` : fichiers interdits (`.env`, `db.sqlite3`, caches), titre et description, taille, code sans test, étiquettes automatiques |
| `Commentaire de synthèse` | PR du dépôt | un seul commentaire mis à jour à chaque push |
| `Vérifications du push (gh)` | push | aucun fichier sensible versionné, Pull Requests liées au commit |

- Les fichiers sensibles font **échouer** la CI ; titre court, description vide, PR volumineuse (plus de 50 fichiers ou 1500 lignes) ou code sans test ne sont que des **avertissements**.
- Étiquettes posées selon les dossiers touchés : `editor`, `cours`, `site`, `docs`, `tests`, `ci`.
- Aucun secret à configurer : le workflow utilise le jeton automatique et une clé Django de test.
- Les PR venant d'un fork lancent les tests mais ne reçoivent ni étiquettes ni commentaire (jeton en lecture seule).
- Si les étiquettes ou le commentaire échouent avec « Resource not accessible by integration » : *Settings > Actions > General > Workflow permissions > Read and write permissions*.
- Pour **bloquer le merge** sans CI verte : *Settings > Branches > Branch protection rules* puis cochez les jobs `Tests`, `Syntaxe JavaScript` et `Commentaire de synthèse` comme obligatoires.

## Contribuer

1. Créez une branche : `git switch -c feat/ma-modification`.
2. Faites des commits courts au format `type(portée): description` (par exemple `feat(editor): ...`, `docs(topics): ...`, `fix(accounts): ...`).
3. Lancez les [tests](#tests) en local.
4. Ouvrez une Pull Request vers `main` : la [CI](#intégration-continue) s'exécute et commente le résultat. Corrigez, poussez : le commentaire est mis à jour.

## Dépannage

| Symptôme | Cause et solution |
|---|---|
| `DJANGO_SECRET_KEY est absent` | `.env` manquant ou clé vide : `cp .env.example .env` puis renseignez la clé. |
| `DJANGO_ALLOWED_HOSTS est obligatoire` | Vous êtes en `DJANGO_DEBUG=0` : renseignez les hôtes, ou passez à `1` en local. |
| La page redirige vers `https://` en local | `DJANGO_DEBUG=0` active la redirection HTTPS. Mettez `DJANGO_DEBUG=1` (ou `DJANGO_HTTPS=0`). |
| CSS / JS / éditeur non chargés | Fichiers statiques non servis : `DJANGO_DEBUG=1` en local, `collectstatic` + serveur web en production. |
| `no such table: editor_editorpreferences` | Migrations non appliquées : `python manage.py migrate`. |
| Le premier affichage des cours est lent | Normal : conversion des pages et mise en cache au premier passage (barre de progression à l'accueil). |
| Le premier clic sur « Exécuter » en Python est lent | Normal : Pyodide (~13 Mo) est chargé une seule fois. |
| Import zip refusé (erreur 413) | L'archive dépasse une limite : voir les variables `EDITOR_ZIP_*`. |
| Compte bloqué après des échecs | Attendez `DJANGO_LOGIN_LOCKOUT_SECONDS` (15 min par défaut). |
| Éditeur TypeScript : le code ne s'exécute pas, la console liste des `TS…` | `noEmitOnError` est actif : corrigez les erreurs de type, ou désactivez-le dans « Options TypeScript ». |
| Éditeur TypeScript : `ReferenceError: maFonction is not defined` (attribut `onclick`) | Le script est un module : écrivez `window.maFonction = maFonction` ou utilisez `addEventListener`. |
| Éditeur Python : fichiers disparus | Ils sont stockés dans le navigateur : vider les données du site ou changer de navigateur les efface. Téléchargez-les pour les sauvegarder. |
| Les tests échouent avec `DJANGO_SECRET_KEY est absent` | Créez `.env`, ou `export DJANGO_SECRET_KEY=test DJANGO_DEBUG=1` avant de lancer les tests. |
| CI : `Resource not accessible by integration` | Droits du jeton insuffisants : voir [Intégration continue](#intégration-continue). |

## Licence et auteur

Projet privé, © 2025 **styjii**. Tous droits réservés : aucune partie du projet ne peut être copiée, distribuée, modifiée ni utilisée sans l'autorisation écrite de l'auteur (voir [`LICENSE`](LICENSE)).

Dépôt : <https://github.com/styjii/code-learning>
