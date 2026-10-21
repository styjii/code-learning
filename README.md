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

## Configuration (variables d'environnement)

`DJANGO_SECRET_KEY`, `DJANGO_DEBUG` (`1` par défaut), `DJANGO_ALLOWED_HOSTS` (liste séparée par des virgules).

## Tests

```bash
python -m pytest core
```
