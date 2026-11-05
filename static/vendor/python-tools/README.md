# Outils d'analyse Python pour l'éditeur

Wheels **inchangées**, téléchargées depuis PyPI, chargées dans un Pyodide dédié à l'analyse du code
(voir `editor/static/editor/js/python/language/`). Toutes sont en Python pur, sous licence MIT.

| Paquet     | Version | Rôle                                                        |
|------------|---------|-------------------------------------------------------------|
| `parso`    | 0.8.6   | analyseur syntaxique (dépendance de jedi)                   |
| `jedi`     | 0.19.2  | autocomplétion, infobulles, aide aux appels de fonction     |
| `pyflakes` | 4.1.0   | erreurs : noms non définis, imports et variables inutilisés |

`manifest.json` est la liste de référence : nom des fichiers (dans l'ordre d'installation) et empreinte
SHA-256, vérifiée par le worker avant l'installation.

## Mettre à jour

Les versions de `jedi` et `parso` doivent rester celles de `pyodide-lock.json` (dossier `vendor/pyodide/`), qui
les liste déjà : ce sont celles testées avec cette version de Pyodide.

```bash
cd static/vendor/python-tools
rm -f *.whl
pip download --no-deps --only-binary=:all: "jedi==X.Y.Z" "parso==X.Y.Z" pyflakes -d .
# puis mettre à jour manifest.json (noms + sha256) :
sha256sum *.whl
```
