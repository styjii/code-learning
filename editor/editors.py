"""
Les trois éditeurs en ligne et ce qui les distingue, côté serveur.

Un seul modèle (``Project``), une seule API (``/editor/api/<editor>/projects/``) et une seule vue de page servent
les trois éditeurs ; l'éditeur courant est un paramètre d'URL (``codelab-js``, ``codelab-ts`` ou ``codelab-py``).
Tout ce qui diffère d'un éditeur à l'autre vit ici, dans une classe par éditeur :

    - le gabarit de la page ;
    - les champs de contenu d'un projet, leurs valeurs par défaut et leur validation (``Project.data``) ;
    - la génération et la lecture de l'archive .zip du projet.

Ajouter un éditeur = ajouter une classe et l'enregistrer dans ``EDITORS``.
"""
import html as html_lib
import io
import json
import zipfile

from bs4 import BeautifulSoup
from django.http import Http404
from rest_framework import serializers

from . import python_files
from .typescript_config import (
    build_tsconfig,
    effective_compiler_options,
    options_from_tsconfig,
    validate_compiler_options,
)
from .zip_import import read_project_zip, read_python_zip, read_typescript_zip

CODELAB_JS = "codelab-js"
CODELAB_TS = "codelab-ts"
CODELAB_PY = "codelab-py"


class CompilerOptionsField(serializers.JSONField):
    """Options du compilateur TypeScript : vérifiées contre la liste blanche de ``typescript_config.py``."""

    def to_internal_value(self, data):
        clean, errors = validate_compiler_options(super().to_internal_value(data))
        if errors:
            raise serializers.ValidationError(errors)
        return clean


class PythonFilesField(serializers.JSONField):
    """
    Fichiers d'un projet Python : ``[{"name", "content"}]`` vérifié avec les règles de ``python_files.py`` (noms,
    doublons, limites de taille et de nombre). Une liste vide est acceptée : le navigateur ajoute alors ``main.py``.
    """

    def to_internal_value(self, data):
        files = super().to_internal_value(data)
        error = python_files.files_error(files, allow_empty=True)
        if error:
            raise serializers.ValidationError(error)
        # On ne garde que les clés attendues : rien d'autre n'est stocké.
        return [{"name": f["name"], "content": f["content"]} for f in files]


def _text_field():
    return serializers.CharField(required=False, allow_blank=True)


def _body_without_scripts(index_html):
    """Contenu du <body> d'un index.html importé, sans ses <script> (le script du projet a son propre champ)."""
    soup = BeautifulSoup(index_html, "html.parser")
    for tag in soup.find_all("script"):
        tag.extract()
    return soup.body.decode_contents() if soup.body else ""


def _zip_bytes(entries, compression=zipfile.ZIP_STORED):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression) as zf:
        for name, content in entries:
            zf.writestr(name, content)
    return buffer.getvalue()


class Editor:
    """Comportement commun ; une sous-classe par éditeur décrit ses spécificités."""

    id = ""
    label = ""
    template = ""

    def fields(self):
        """Champs de contenu de l'API : ``{nom: champ DRF}``."""
        raise NotImplementedError

    def defaults(self):
        """Contenu d'un projet vide : ``{nom: valeur}`` (mêmes noms que ``fields``)."""
        raise NotImplementedError

    def merge(self, stored, content):
        """Contenu à enregistrer : valeurs par défaut, puis ce qui est stocké, puis ``content`` (clés connues seulement)."""
        base = self.defaults()
        stored = stored if isinstance(stored, dict) else {}
        merged = {key: stored.get(key, default) for key, default in base.items()}
        merged.update({key: value for key, value in content.items() if key in base})
        return merged

    def public(self, stored):
        """Contenu renvoyé au navigateur."""
        return self.merge(stored, {})

    def export_zip(self, project):
        """Octets de l'archive .zip du projet, construite à partir de ce qui est enregistré en base."""
        raise NotImplementedError

    def import_zip(self, fileobj, name):
        """Lit une archive : ``(contenu, messages)`` ; ``contenu`` est fusionné dans ``Project.data``."""
        raise NotImplementedError


class _WebPage:
    """Page ``index.html`` exportée par les éditeurs HTML/CSS (JavaScript ou TypeScript)."""

    @staticmethod
    def render(title, body, module=False):
        script = '<script type="module" src="./script.js"></script>' if module else '<script src="./script.js"></script>'
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html_lib.escape(title)}</title>
    <link rel="stylesheet" href="./style.css" />
</head>
<body>
{body}
{script}
</body>
</html>
"""


class JavaScriptEditor(Editor):
    """Éditeur HTML / CSS / JavaScript. Archive : index.html, style.css, script.js."""

    id = CODELAB_JS
    label = "Web"
    template = "editor/codelab-js.html"

    def fields(self):
        return {"html": _text_field(), "css": _text_field(), "js": _text_field()}

    def defaults(self):
        return {"html": "", "css": "", "js": ""}

    def export_zip(self, project):
        data = self.public(project.data)
        page = _WebPage.render(project.name, data["html"])
        return _zip_bytes([("index.html", page), ("style.css", data["css"]), ("script.js", data["js"])])

    def import_zip(self, fileobj, name):
        index_html, style_css, script_js = read_project_zip(fileobj, name)
        return {"html": _body_without_scripts(index_html), "css": style_css, "js": script_js}, []


class TypeScriptEditor(Editor):
    """
    Éditeur HTML / CSS / TypeScript. Archive : index.html, style.css, script.ts et tsconfig.json : ``npx tsc``
    produit ensuite script.js, chargé par index.html comme module.
    """

    id = CODELAB_TS
    label = "TypeScript"
    template = "editor/codelab-ts.html"

    def fields(self):
        return {
            "html": _text_field(),
            "css": _text_field(),
            "ts": _text_field(),
            "compiler_options": CompilerOptionsField(required=False),
        }

    def defaults(self):
        return {"html": "", "css": "", "ts": "", "compiler_options": {}}

    def public(self, stored):
        data = super().public(stored)
        # Le navigateur reçoit toujours des options complètes (valeurs par défaut + celles du projet).
        data["compiler_options"] = effective_compiler_options(data["compiler_options"])
        return data

    def export_zip(self, project):
        data = self.public(project.data)
        page = _WebPage.render(project.name, data["html"], module=True)
        tsconfig = json.dumps(build_tsconfig(data["compiler_options"]), indent=2) + "\n"
        return _zip_bytes([
            ("index.html", page),
            ("style.css", data["css"]),
            ("script.ts", data["ts"]),
            ("tsconfig.json", tsconfig),
        ])

    def import_zip(self, fileobj, name):
        index_html, style_css, script_ts, tsconfig = read_typescript_zip(fileobj, name)
        content = {
            "html": _body_without_scripts(index_html),
            "css": style_css,
            "ts": script_ts,
            "compiler_options": effective_compiler_options(options_from_tsconfig(tsconfig)),
        }
        return content, []


class PythonEditor(Editor):
    """
    Éditeur Python : une liste de fichiers « à plat » par projet. Archive : ces fichiers, ``main.py`` en tête.
    Les noms et tailles sont revérifiés à l'export : une archive exportée est toujours réimportable.
    """

    id = CODELAB_PY
    label = "Python"
    template = "editor/codelab-py.html"

    def fields(self):
        return {"files": PythonFilesField(required=False)}

    def defaults(self):
        return {"files": []}

    def export_zip(self, project):
        files = self.public(project.data)["files"]
        error = python_files.files_error(files)
        if error:
            raise ValueError(error)
        ordered = sorted(files, key=lambda f: f["name"] != python_files.MAIN_FILE)
        return _zip_bytes(((f["name"], f["content"]) for f in ordered), zipfile.ZIP_DEFLATED)

    def import_zip(self, fileobj, name):
        files, skipped = read_python_zip(fileobj)
        return {"files": files}, skipped


# Ordre = ordre d'affichage du sélecteur d'éditeur (Web | Python | TypeScript).
EDITORS = {editor.id: editor for editor in (JavaScriptEditor(), PythonEditor(), TypeScriptEditor())}


def get(editor_id):
    """L'éditeur d'identifiant ``editor_id`` ; 404 s'il n'existe pas."""
    try:
        return EDITORS[editor_id]
    except KeyError:
        raise Http404("Éditeur inconnu.")


def choices():
    """Choix du champ ``Project.editor``."""
    return [(editor.id, editor.label) for editor in EDITORS.values()]
