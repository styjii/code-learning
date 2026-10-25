from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView
from .views import (
    ProjectViewSet,
    ExportZipView,
    ImportZipView,
    LivePreviewView,
    PreviewDisplayView,
    LoadMonacoConfigView,
    SaveMonacoConfigView,
    TypeScriptExportZipView,
    TypeScriptImportZipView,
    TypeScriptProjectViewSet,
)


router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'ts-projects', TypeScriptProjectViewSet, basename='ts-project')

urlpatterns = [
    path('', ensure_csrf_cookie(TemplateView.as_view(template_name='editor/index.html')), name='editor-index'),
    path('python/', ensure_csrf_cookie(TemplateView.as_view(template_name='editor/python.html')), name='python-editor'),
    path('typescript/', ensure_csrf_cookie(TemplateView.as_view(template_name='editor/typescript.html')), name='typescript-editor'),
    path('api/', include(router.urls)),
    path('api/load-monaco-config/', LoadMonacoConfigView.as_view(), name='load-monaco-config'),
    path('api/save-monaco-config/', SaveMonacoConfigView.as_view(), name='save-monaco-config'),
    path('api/export-zip/', ExportZipView.as_view(), name='export_zip'),
    path('api/import-zip/', ImportZipView.as_view(), name='import_zip'),
    path('api/ts-export-zip/', TypeScriptExportZipView.as_view(), name='ts_export_zip'),
    path('api/ts-import-zip/', TypeScriptImportZipView.as_view(), name='ts_import_zip'),
    path("preview/", LivePreviewView.as_view(), name="live-preview"),
    path("preview/<str:preview_id>/", PreviewDisplayView.as_view(), name="preview-display"),
]
