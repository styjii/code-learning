# Langage Learning

Cours de programmation en français (Markdown -> pages web) + éditeur HTML/CSS/JS en ligne. Django 5.

## Lancer

```bash
pip install -r requirements.txt
cp .env.example .env          # puis renseignez DJANGO_SECRET_KEY (voir le fichier)
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Ouvrir http://127.0.0.1:8000/ : **toute page exige une connexion** (formulaire sur `/accounts/login/`).
Il n'y a pas d'inscription publique : créez les comptes avec `createsuperuser`, ou via `/admin/`
(*Utilisateurs > Ajouter*). Les cours sont convertis à la demande ; ils sont régénérés automatiquement
quand un fichier `.md` de `language/topics/` change.

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

## Configuration (fichier `.env`)

Toutes les valeurs sensibles sont lues dans `.env` (jamais versionné, voir `.gitignore`) ou dans l'environnement.
Modèle commenté : `.env.example`. Le démarrage échoue avec un message explicite si `DJANGO_SECRET_KEY` manque.

| Variable | Rôle |
|---|---|
| `DJANGO_SECRET_KEY` | clé secrète (obligatoire) |
| `DJANGO_DEBUG` | `1` développement, `0` production (défaut `0`) |
| `DJANGO_ALLOWED_HOSTS` | hôtes autorisés, séparés par des virgules |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | origines HTTPS de confiance |
| `DJANGO_HTTPS`, `DJANGO_HSTS_SECONDS`, `DJANGO_BEHIND_PROXY` | cookies `Secure`, redirection HTTPS, HSTS, proxy inverse |
| `DJANGO_SESSION_HOURS` | durée d'une session |
| `DJANGO_LOGIN_MAX_ATTEMPTS`, `DJANGO_LOGIN_LOCKOUT_SECONDS` | blocage après échecs de connexion |

## Sécurité

- `LoginRequiredMiddleware` : toutes les pages redirigent vers la connexion ; l'API REST répond `403` aux anonymes.
- Blocage temporaire après plusieurs échecs (par IP + identifiant). Le compteur utilise le cache Django
  (mémoire locale) : configurez un cache partagé si vous lancez plusieurs processus.
- Déconnexion par `POST` ; protection CSRF sur tous les appels de l'éditeur.
- Les projets de l'éditeur appartiennent à leur utilisateur (chacun ne voit que les siens).
  Projets créés avant l'authentification (sans propriétaire) : rattachez-les avec
  `python manage.py shell -c "from editor.models import Project as P; from django.contrib.auth import get_user_model as g; P.objects.filter(owner=None).update(owner=g().objects.get(username='VOTRE_NOM'))"`.
- L'aperçu de l'éditeur est servi avec `Content-Security-Policy: sandbox` : le code de l'utilisateur ne peut pas utiliser sa session.
- En production, servez les fichiers statiques avec votre serveur web (ou WhiteNoise) et mettez `DJANGO_DEBUG=0`.

## Tests

```bash
python manage.py test accounts   # authentification, isolation des projets, CSRF
python -m pytest core            # conversion Markdown
```
