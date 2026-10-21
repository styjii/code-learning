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
from .models import Project
from .services import id
from .serializers import ProjectSerializer
from bs4 import BeautifulSoup
import html as html_lib
import io
import json
import os
import zipfile
from urllib.parse import quote

MAX_PREVIEWS = 5


class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Project instances.

    This viewset provides `list`, `create`, `retrieve`, `update`, and `destroy` actions
    for Project model objects using Django REST Framework.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SaveMonacoConfigView(APIView):
    """
    API endpoint to save Monaco Editor configuration (like wordWrap, scrollBeyondLastLine).

    Expects JSON body, saves to a file like monacoOptions.json in the static directory.
    """
    def post(self, request):
        try:
            config_data = request.data
            static_config_path = os.path.join(settings.BASE_DIR, 'editor', 'config')
            os.makedirs(static_config_path, exist_ok=True)

            config_file = os.path.join(static_config_path, 'monacoOptions.json')
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config_data, f, indent=4)

            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoadMonacoConfigView(APIView):
    """
    API endpoint to load the Monaco Editor configuration.

    This view reads the JSON configuration file (monacoOptions.json) from the static directory
    and returns it as a JSON response. It allows the frontend to dynamically load editor options
    like wordWrap, scrollBeyondLastLine, etc.
    """
    def get(self, request):
        try:
            config_path = os.path.join(settings.BASE_DIR, 'editor', 'config', 'monacoOptions.json')
            with open(config_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return Response(data, status=status.HTTP_200_OK)
        except FileNotFoundError:
            return Response({'error': 'Config not found'}, status=status.HTTP_404_NOT_FOUND)

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
    as a JSON response suitable for restoring a project.
    """
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        """
        Handle POST request to import project data from a ZIP file.

        Returns:
            Response: A JSON object with 'html', 'css', 'js', and 'project' name,
                      or an error message if the ZIP file is invalid.
        """
        uploaded_file = request.FILES.get('zip_file')
        if not uploaded_file:
            return Response({'error': 'No zip file provided.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with zipfile.ZipFile(uploaded_file) as zf:
                name = uploaded_file.name.replace(".zip", "")
                file_list = zf.namelist()

                def read_file(filename):
                    return zf.read(filename).decode('utf-8') if filename in file_list else ''

                index_html = read_file(f"{name}/index.html") or read_file("index.html")
                style_css = read_file(f"{name}/style.css") or read_file("style.css")
                script_js = read_file(f"{name}/script.js") or read_file("script.js")
        except Exception as e:
            return Response({'error': 'Invalid zip file or structure', 'details': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

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

class LivePreviewView(APIView):
    def post(self, request):
        """
        Handles POST requests to generate a live preview of HTML, CSS, and JavaScript code.

        - Extracts HTML, CSS, JS, and optional CDN links from the POST request.
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

        context = {
            "html": html,
            "css": css,
            "js": js,
            "cdn_css": cdn_css,
            "cdn_js": cdn_js,
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
        return HttpResponse(content)
