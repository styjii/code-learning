from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt
from django.template.loader import render_to_string
from django.conf import settings
from django.db import transaction
from .models import EditorPreferences, Project, TypeScriptProject
from .monaco_config import effective_options, sanitize_preferences, validate_preferences
from .services import id
from .serializers import ProjectSerializer, TypeScriptProjectSerializer
from .typescript_config import build_tsconfig, options_from_tsconfig, effective_compiler_options
from .zip_import import ZipImportError, format_size, read_project_zip, read_typescript_zip
from bs4 import BeautifulSoup
import html as html_lib
import io
import json
import zipfile
from urllib.parse import quote

MAX_PREVIEWS = 5

# Marge pour l'enveloppe multipart (délimiteurs, en-têtes) autour du fichier envoyé.
UPLOAD_OVERHEAD_BYTES = 64 * 1024


class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Project instances.

    This viewset provides `list`, `create`, `retrieve`, `update`, and `destroy` actions
    for Project model objects using Django REST Framework.
    """
    serializer_class = ProjectSerializer

    def get_queryset(self):
        # Chaque utilisateur ne voit et ne modifie que ses propres projets.
        return Project.objects.filter(owner=self.request.user).order_by("id")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TypeScriptProjectViewSet(ProjectViewSet):
    """
    Même API que ``ProjectViewSet`` pour les projets de l'éditeur TypeScript (HTML, CSS, TypeScript et
    options du compilateur). Les deux types de projets sont indépendants : un projet Web n'apparaît jamais ici.
    """
    serializer_class = TypeScriptProjectSerializer

    def get_queryset(self):
        return TypeScriptProject.objects.filter(owner=self.request.user).order_by("id")


class SaveMonacoConfigView(APIView):
    """
    API endpoint pour enregistrer les préférences Monaco de l'utilisateur connecté (wordWrap, tabSize...).

    Le corps JSON ne peut contenir que des clés de la liste blanche (voir ``monaco_config.py``) ; sinon la
    requête est refusée en bloc (400) et rien n'est enregistré. Les préférences sont fusionnées avec les
    précédentes et stockées en base, par utilisateur : elles n'affectent jamais les autres comptes.
    """
    parser_classes = [JSONParser]

    def post(self, request):
        clean, errors = validate_preferences(request.data)
        if errors:
            return Response({'error': 'Options invalides.', 'details': errors},
                            status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            prefs, _ = EditorPreferences.objects.select_for_update().get_or_create(user=request.user)
            prefs.monaco = {**sanitize_preferences(prefs.monaco), **clean}
            prefs.save(update_fields=['monaco', 'updated_at'])
        return Response({'status': 'success'}, status=status.HTTP_200_OK)

class LoadMonacoConfigView(APIView):
    """
    API endpoint pour charger la configuration Monaco de l'utilisateur connecté.

    Retourne les options par défaut, ses préférences enregistrées (filtrées par la liste blanche) puis les
    réglages imposés par l'application.
    """
    def get(self, request):
        prefs = EditorPreferences.objects.filter(user=request.user).first()
        return Response(effective_options(prefs.monaco if prefs else {}), status=status.HTTP_200_OK)

class ExportZipView(APIView):
    """
    API endpoint that generates a ZIP file from HTML, CSS, and JavaScript content.

    Parses project content from a POST request in JSON format and returns a ZIP
    file containing the content as 'index.html', 'style.css', and 'script.js'.
    """
    parser_classes = [JSONParser]

    def post(self, request):
        """
        Handle POST request to export project data as a ZIP file.

        Returns:
            HttpResponse: A downloadable ZIP file containing the project.
        """
        data = request.data
        project_name = str(data.get('project') or 'project')
        safe_title = html_lib.escape(project_name)
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{safe_title}</title>
    <link rel="stylesheet" href="./style.css" />
</head>
<body>
{data.get('html', '')}
<script src="./script.js"></script>
</body>
</html>
"""

        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zf:
            zf.writestr("index.html", html_content)
            zf.writestr("style.css", data.get('css', ''))
            zf.writestr("script.js", data.get('js', ''))

        zip_buffer.seek(0)
        response = HttpResponse(zip_buffer.read(), content_type='application/zip')
        response['Content-Disposition'] = f"attachment; filename*=UTF-8''{quote(project_name)}.zip"
        return response

class ImportZipView(APIView):
    """
    API endpoint for importing a ZIP file and extracting HTML, CSS, and JS content.

    Parses the uploaded ZIP file, extracts its contents, and returns them
    as a JSON response suitable for restoring a project. Les tailles sont plafonnées
    (voir ``zip_import.py`` et les réglages ``EDITOR_ZIP_*``) : refus en 413 au-delà.
    """
    parser_classes = [MultiPartParser, FormParser]

    def initial(self, request, *args, **kwargs):
        # Refus avant toute lecture du corps : DRF/Django l'analysent (et l'écrivent sur disque)
        # dès l'authentification, donc un contrôle placé dans post() arriverait trop tard.
        try:
            length = int(request.META.get('CONTENT_LENGTH') or 0)
        except ValueError:
            length = 0
        limit = settings.EDITOR_ZIP_MAX_UPLOAD_BYTES
        if length > limit + UPLOAD_OVERHEAD_BYTES:
            raise ZipImportError(f"Fichier trop volumineux (maximum {format_size(limit)}).", 413)
        super().initial(request, *args, **kwargs)

    def handle_exception(self, exc):
        if isinstance(exc, ZipImportError):
            return Response({'error': exc.message}, status=exc.status)
        return super().handle_exception(exc)

    def post(self, request):
        """
        Handle POST request to import project data from a ZIP file.

        Returns:
            Response: A JSON object with 'html', 'css', 'js', and 'project' name,
                      or an error message if the ZIP file is invalid or too large.
        """
        uploaded_file = request.FILES.get('zip_file')
        if not uploaded_file:
            return Response({'error': 'No zip file provided.'}, status=status.HTTP_400_BAD_REQUEST)

        limit = settings.EDITOR_ZIP_MAX_UPLOAD_BYTES
        if uploaded_file.size > limit:
            raise ZipImportError(f"Fichier trop volumineux (maximum {format_size(limit)}).", 413)

        name = uploaded_file.name.replace(".zip", "")
        index_html, style_css, script_js = read_project_zip(uploaded_file, name)

        soup = BeautifulSoup(index_html, 'html.parser')
        for tag in soup.find_all('script'):
            tag.extract()
        body_content = soup.body.decode_contents() if soup.body else ''

        return Response({
            'project': name,
            'html': body_content,
            'css': style_css,
            'js': script_js
        })

class TypeScriptExportZipView(APIView):
    """
    API endpoint qui génère le .zip d'un projet TypeScript.

    Le JSON reçu contient ``project``, ``html``, ``css``, ``ts`` et ``compilerOptions``. L'archive contient
    'index.html', 'style.css', 'script.ts' et 'tsconfig.json' : ``npx tsc`` produit ensuite 'script.js',
    chargé par 'index.html' comme module.
    """
    parser_classes = [JSONParser]

    def post(self, request):
        data = request.data
        project_name = str(data.get('project') or 'project')
        safe_title = html_lib.escape(project_name)
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{safe_title}</title>
    <link rel="stylesheet" href="./style.css" />
</head>
<body>
{data.get('html', '')}
<script type="module" src="./script.js"></script>
</body>
</html>
"""
        tsconfig = json.dumps(build_tsconfig(data.get('compilerOptions')), indent=2) + "\n"

        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zf:
            zf.writestr("index.html", html_content)
            zf.writestr("style.css", str(data.get('css', '')))
            zf.writestr("script.ts", str(data.get('ts', '')))
            zf.writestr("tsconfig.json", tsconfig)

        zip_buffer.seek(0)
        response = HttpResponse(zip_buffer.read(), content_type='application/zip')
        response['Content-Disposition'] = f"attachment; filename*=UTF-8''{quote(project_name)}.zip"
        return response

class TypeScriptImportZipView(ImportZipView):
    """
    API endpoint d'import d'un .zip de projet TypeScript : renvoie ``html``, ``css``, ``ts`` et
    ``compiler_options`` (lues dans 'tsconfig.json', complétées par les valeurs par défaut).

    Mêmes plafonds de taille que ``ImportZipView`` (contrôle avant lecture, refus en 413).
    """

    def post(self, request):
        uploaded_file = request.FILES.get('zip_file')
        if not uploaded_file:
            return Response({'error': 'No zip file provided.'}, status=status.HTTP_400_BAD_REQUEST)

        limit = settings.EDITOR_ZIP_MAX_UPLOAD_BYTES
        if uploaded_file.size > limit:
            raise ZipImportError(f"Fichier trop volumineux (maximum {format_size(limit)}).", 413)

        name = uploaded_file.name.replace(".zip", "")
        index_html, style_css, script_ts, tsconfig = read_typescript_zip(uploaded_file, name)

        soup = BeautifulSoup(index_html, 'html.parser')
        for tag in soup.find_all('script'):
            tag.extract()
        body_content = soup.body.decode_contents() if soup.body else ''

        return Response({
            'project': name,
            'html': body_content,
            'css': style_css,
            'ts': script_ts,
            'compiler_options': effective_compiler_options(options_from_tsconfig(tsconfig)),
        })


class LivePreviewView(APIView):
    def post(self, request):
        """
        Handles POST requests to generate a live preview of HTML, CSS, and JavaScript code.

        - Extracts HTML, CSS, JS, and optional CDN links from the POST request
          (``module=1`` : le JS est exécuté comme module ES, cas du JavaScript compilé depuis TypeScript).
        - Renders the code into a preview HTML template.
        - Generates a random preview ID and stores the rendered content in the user's session.
        - Returns a JSON response with a URL pointing to the preview endpoint.

        Returns:
            JsonResponse: A JSON object containing the preview URL.
        """
        html = request.POST.get("html", "")
        css = request.POST.get("css", "")
        js = request.POST.get("js", "")
        cdn_css = json.loads(request.POST.get("cdn_css", "[]"))
        cdn_js = json.loads(request.POST.get("cdn_js", "[]"))
        # L'éditeur TypeScript envoie le JavaScript compilé avec module=1 : il est exécuté comme module ES.
        module = request.POST.get("module") == "1"

        context = {
            "html": html,
            "css": css,
            "js": js,
            "cdn_css": cdn_css,
            "cdn_js": cdn_js,
            "module": module,
        }

        rendered_html = render_to_string("editor/preview.html", context)
        preview_id = id.get_id()
        request.session[f"preview_{preview_id}"] = rendered_html

        # Ne conserver que les derniers aperçus : la session ne doit pas grossir à chaque exécution.
        history = request.session.get("preview_ids", [])
        history.append(preview_id)
        for old_id in history[:-MAX_PREVIEWS]:
            request.session.pop(f"preview_{old_id}", None)
        request.session["preview_ids"] = history[-MAX_PREVIEWS:]

        return JsonResponse({"url": f"/editor/preview/{preview_id}/"})

@method_decorator(xframe_options_exempt, name="dispatch")
class PreviewDisplayView(View):
    def get(self, request, preview_id):
        """
        Handles GET requests to display a previously generated code preview.

        - Retrieves the preview content from the session using the provided preview ID.
        - If found, returns the HTML content as an HTTP response.
        - If not found (e.g. expired or invalid ID), returns a 404 Not Found response.

        Args:
            request (HttpRequest): The HTTP request object.
            preview_id (str): The ID used to retrieve the stored preview content.

        Returns:
            HttpResponse or HttpResponseNotFound: The rendered preview or a 404 error.
        """
        content = request.session.get(f"preview_{preview_id}")
        if not content:
            return HttpResponseNotFound("Preview not found or expired.")
        response = HttpResponse(content)
        # Même ouvert directement dans un onglet, l'aperçu s'exécute dans un bac à sable
        # (origine opaque) : le code de l'utilisateur ne peut pas utiliser sa session.
        response["Content-Security-Policy"] = "sandbox allow-scripts allow-modals"
        return response
