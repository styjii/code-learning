# Langage Learning

Cours de programmation en français (Markdown -> pages web) + éditeur HTML/CSS/JS en ligne. Django 5.

## Lancer

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Ouvrir http://127.0.0.1:8000/ . Les cours sont convertis à la demande (et préparés depuis l'accueil) ;
ils sont régénérés automatiquement quand un fichier `.md` de `language/topics/` change.

## Structure

| Dossier | Rôle |
|---|---|
| `templates/` | `base.html` et partials partagés (thème, logo) |
| `webapp/` | accueil : catalogue des cours |
| `language/` | pages de cours (`config.py` = catalogue, `topics/` = Markdown) |
| `core/` | conversion Markdown -> HTML à sections, accès SQLite |
| `editor/` | éditeur Monaco, projets, aperçu, import/export zip |

Ajouter un cours : créer le `.md` dans `language/topics/`, puis l'ajouter dans `language/config.py`.

## Code exécutable dans les cours

Les blocs ` ```js `, ` ```ts ` et ` ```python ` des cours ont un bouton **Exécuter** : le bloc devient un éditeur
Monaco modifiable (Ctrl+Entrée pour relancer) avec sa zone de résultat. Tout s'exécute dans le navigateur :

| Langage | Moteur |
|---|---|
| JavaScript | Web Worker isolé (pas d'accès au DOM), arrêt automatique après 8 s |
| TypeScript | compilateur de Monaco (erreurs de type affichées), puis exécution comme JavaScript |
| Python | [Pyodide](https://pyodide.org) (CPython 3.14 en WebAssembly, ~13 Mo, chargé au premier clic), `input()` via la zone « Entrée standard », arrêt après 10 s |

Pour garder un bloc en lecture seule : ` ```python norun `. Les extraits JS/TS qui utilisent `import`, `export` ou
`require()` ne sont pas exécutables et n'ont pas de bouton. Pyodide est vendorisé dans `static/vendor/pyodide/`
(licence MPL-2.0). Le C/C++ n'est pas encore pris en charge.

## Configuration (variables d'environnement)

`DJANGO_SECRET_KEY`, `DJANGO_DEBUG` (`1` par défaut), `DJANGO_ALLOWED_HOSTS` (liste séparée par des virgules).

## Tests

```bash
python -m pytest core
```
