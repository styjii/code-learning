from django.shortcuts import redirect
from django.urls import path, register_converter

from . import editors
from .views import (
    EditorPageView,
    LivePreviewView,
    LoadMonacoConfigView,
    PreviewDisplayView,
    ProjectExportZipView,
    ProjectImportZipView,
    ProjectViewSet,
    SaveMonacoConfigView,
)


class EditorConverter:
    """Segment d'URL ``codelab-js`` | ``codelab-ts`` | ``codelab-py`` : l'éditeur courant, passé aux vues."""
    regex = "|".join(editors.EDITORS)

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value


register_converter(EditorConverter, "editor")


def legacy_redirect(editor_id):
    """Anciennes adresses (/editor/, /editor/python/, /editor/typescript/) : redirigées vers le nouvel identifiant."""
    return lambda request: redirect("editor", editor=editor_id, permanent=True)


project_list = ProjectViewSet.as_view({'get': 'list', 'post': 'create'})
project_detail = ProjectViewSet.as_view({
    'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy',
})

urlpatterns = [
    path('', legacy_redirect(editors.CODELAB_JS)),
    path('python/', legacy_redirect(editors.CODELAB_PY)),
    path('typescript/', legacy_redirect(editors.CODELAB_TS)),
    # Une seule vue pour les trois éditeurs : l'éditeur courant est le paramètre de l'URL.
    path('<editor:editor>/', EditorPageView.as_view(), name='editor'),
    path('api/<editor:editor>/projects/', project_list, name='project-list'),
    path('api/<editor:editor>/projects/<int:pk>/', project_detail, name='project-detail'),
    path('api/<editor:editor>/projects/<int:pk>/export-zip/', ProjectExportZipView.as_view(), name='project-export-zip'),
    path('api/<editor:editor>/projects/<int:pk>/import-zip/', ProjectImportZipView.as_view(), name='project-import-zip'),
    path('api/load-monaco-config/', LoadMonacoConfigView.as_view(), name='load-monaco-config'),
    path('api/save-monaco-config/', SaveMonacoConfigView.as_view(), name='save-monaco-config'),
    path("preview/", LivePreviewView.as_view(), name="live-preview"),
    path("preview/<str:preview_id>/", PreviewDisplayView.as_view(), name="preview-display"),
]
