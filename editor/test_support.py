"""Aides communes aux tests : adresses des trois éditeurs et de leur API de projets."""
from django.urls import reverse

from . import editors

JS, TS, PY = editors.CODELAB_JS, editors.CODELAB_TS, editors.CODELAB_PY


def page_url(editor):
    return reverse("editor", args=[editor])


def projects_url(editor, pk=None):
    return f"/editor/api/{editor}/projects/" + (f"{pk}/" if pk is not None else "")


def export_url(editor, pk):
    return projects_url(editor, pk) + "export-zip/"


def import_url(editor, pk):
    return projects_url(editor, pk) + "import-zip/"
