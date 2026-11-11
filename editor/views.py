from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt
from django.template.loader import render_to_string
from django.conf import settings
from django.db import IntegrityError, transaction
from . import editors, project_names
from .models import EditorPreferences, Project
from .monaco_config import effective_options, sanitize_preferences, validate_preferences
from .services import id
from .serializers import DUPLICATE_NAME_MESSAGE, ProjectSerializer
from .zip_import import ZipImportError, format_size
import json
import uuid
from urllib.parse import quote

MAX_PREVIEWS = 5
# Données localStorage du code de l'aperçu (voir static/editor/js/preview-storage.js) : mêmes plafonds que le navigateur.
PREVIEW_STORAGE_MAX_CHARS = 256 * 1024
PREVIEW_STORAGE_MAX_KEYS = 200

# Marge pour l'enveloppe multipart (délimiteurs, en-têtes) autour du fichier envoyé.
UPLOAD_OVERHEAD_BYTES = 64 * 1024


@method_decorator(ensure_csrf_cookie, name="dispatch")
class EditorPageView(TemplateView):
    """
    Page d'un éditeur : une seule vue pour les trois, l'éditeur courant (``codelab-js``, ``codelab-ts`` ou
    ``codelab-py``) vient de l'URL. Le gabarit est celui de l'éditeur (voir ``editors.py``).
    """

    def get_template_names(self):
        return [editors.get(self.kwargs["editor"]).template]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["editor"] = self.kwargs["editor"]
        context["editors"] = list(editors.EDITORS.values())      # sélecteur d'éditeur de l'en-tête
        return context


class ProjectViewSet(viewsets.ModelViewSet):
    """
    CRUD des projets de l'utilisateur connecté pour l'éditeur de l'URL (``/editor/api/<editor>/projects/``) :
    ``list``, ``create``, ``retrieve``, ``update``, ``partial_update`` et ``destroy``. Une seule vue pour les trois
    éditeurs : ce qui diffère (champs de contenu, validation) est décrit par ``editors.py``.

    Isolation :
        - ``get_queryset`` ne renvoie que les projets de l'utilisateur ET de l'éditeur de l'URL : un projet d'un autre
          compte, d'un autre éditeur (ou sans propriétaire) est introuvable (404), sans révéler son existence ;
        - le propriétaire n'est jamais lu dans le corps de la requête : il est imposé à la création.

    Robustesse :
        - un doublon de nom (même utilisateur, même éditeur) détecté seulement à l'écriture (requêtes simultanées)
          donne un 400, pas un 500 ;
        - seul le JSON est accepté (415 sinon).
    """
    serializer_class = ProjectSerializer
    # Déjà imposé par REST_FRAMEWORK et par StrictLoginRequiredMiddleware : explicite ici par défense en profondeur.
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    @cached_property
    def editor(self):
        return editors.get(self.kwargs["editor"])

    def get_serializer_context(self):
        return {**super().get_serializer_context(), "editor": self.editor}

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Project.objects.none()
        # Chaque utilisateur ne voit et ne modifie que ses propres projets, dans l'éditeur de l'URL.
        return Project.objects.filter(owner=user, editor=self.editor.id).order_by("id")

    def perform_create(self, serializer):
        self._save_or_reject_duplicate(serializer, owner=self.request.user)

    def perform_update(self, serializer):
        # Le propriétaire et l'éditeur ne changent jamais : ils ne sont pas dans les champs du serializer.
        self._save_or_reject_duplicate(serializer)

    @staticmethod
    def _save_or_reject_duplicate(serializer, **extra):
        """
        Enregistre ; une violation de la contrainte « nom unique par propriétaire et par éditeur » devient un 400.

        ``atomic`` isole l'écriture : l'échec d'un INSERT n'invalide pas une transaction englobante.
        """
        try:
            with transaction.atomic():
                serializer.save(**extra)
        except IntegrityError:
            raise ValidationError({"name": [DUPLICATE_NAME_MESSAGE]})


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

class ProjectZipMixin:
    """Le projet d'un export ou d'un import : celui de l'utilisateur, dans l'éditeur de l'URL (404 sinon)."""

    def get_project(self, request, editor, pk):
        return get_object_or_404(Project, pk=pk, owner=request.user, editor=editors.get(editor).id)


class ProjectExportZipView(ProjectZipMixin, APIView):
    """
    ``GET /editor/api/<editor>/projects/<id>/export-zip/`` : l'archive .zip du projet, construite à partir de ce qui est
    enregistré en base (le navigateur enregistre d'abord ses modifications en attente). Le contenu de l'archive
    dépend de l'éditeur (voir ``editors.py``).
    """

    def get(self, request, editor, pk):
        project = self.get_project(request, editor, pk)
        try:
            data = editors.get(editor).export_zip(project)
        except ValueError as error:
            return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)

        response = HttpResponse(data, content_type='application/zip')
        response['Content-Disposition'] = f"attachment; filename*=UTF-8''{quote(project.name or 'project')}.zip"
        return response


class ProjectImportZipView(APIView):
    """
    ``POST /editor/api/<editor>/projects/import-zip/`` : crée un **nouveau projet** à partir d'une archive .zip (champ
    ``zip_file``) ; le projet ouvert n'est jamais modifié. Le contenu est lu par le serveur (plafonds de tailles, voir
    ``zip_import.py`` et les réglages ``EDITOR_ZIP_*`` : 413 au-delà) et écrit directement en base.

    Nom du projet :
        - par défaut, celui du fichier sans ``.zip`` ;
        - si ce nom est invalide ou dépasse la longueur maximale de la base, ``projet-import-{id du projet}`` ;
        - ``name`` (champ optionnel) impose un nom : refusé en 400 s'il est invalide (jamais de nom de secours).

    Doublon (même utilisateur, même éditeur, même nom) :
        - par défaut, rien n'est écrit et la réponse est un 409 qui décrit le conflit : le navigateur demande à
          l'utilisateur d'écraser le projet existant ou de choisir un autre nom ;
        - avec ``on_conflict=overwrite``, le contenu du projet existant est remplacé (son id et son nom restent).

    Réponse : le projet (mêmes champs que l'API des projets), ``created`` (False si écrasé), ``renamed`` (True si le
    nom de secours a été utilisé) et ``skipped``, les messages pour les entrées ignorées. 201 si créé, 200 si écrasé.
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

    def post(self, request, editor):
        spec = editors.get(editor)

        uploaded_file = request.FILES.get('zip_file')
        if not uploaded_file:
            return Response({'error': 'No zip file provided.'}, status=status.HTTP_400_BAD_REQUEST)

        limit = settings.EDITOR_ZIP_MAX_UPLOAD_BYTES
        if uploaded_file.size > limit:
            raise ZipImportError(f"Fichier trop volumineux (maximum {format_size(limit)}).", 413)

        # Lecture et validation de l'archive avant toute écriture : une archive refusée ne laisse rien en base.
        content, skipped = spec.import_zip(uploaded_file, project_names.stem_of(uploaded_file.name))
        data = spec.merge({}, content)

        requested = request.data.get('name')
        if requested:
            name = project_names.clean_name(requested)
            if name is None:
                return Response(
                    {'error': f"Nom invalide : 1 à {project_names.MAX_NAME_LENGTH} caractères, sans caractère de contrôle."},
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            name = project_names.name_from_filename(uploaded_file.name)      # None : nom de secours

        projects = Project.objects.filter(owner=request.user, editor=spec.id)
        if name is not None:
            existing = projects.filter(name=name).first()
            if existing is not None:
                if request.data.get('on_conflict') != 'overwrite':
                    return self._conflict(name, existing)
                existing.data = data
                existing.save(update_fields=['data'])
                return self._created(request, spec, existing, skipped, created=False, renamed=False)

        try:
            with transaction.atomic():
                project = Project.objects.create(
                    owner=request.user, editor=spec.id, data=data,
                    # Nom provisoire unique : le nom de secours contient l'id, connu seulement une fois créé.
                    name=name if name is not None else f"~import-{uuid.uuid4().hex}")
                if name is None:
                    project.name = project_names.fallback_name(request.user, spec.id, project.pk)
                    project.save(update_fields=['name'])
        except IntegrityError:
            # Un projet de ce nom a été créé entre-temps (requêtes simultanées) : même réponse qu'un doublon.
            existing = projects.filter(name=name).first()
            if existing is None:
                raise
            return self._conflict(name, existing)
        return self._created(request, spec, project, skipped, created=True, renamed=name is None)

    @staticmethod
    def _conflict(name, existing):
        return Response(
            {'error': f"Un projet « {name} » existe déjà.", 'conflict': {'name': name, 'id': existing.pk}},
            status=status.HTTP_409_CONFLICT)

    @staticmethod
    def _created(request, spec, project, skipped, *, created, renamed):
        body = ProjectSerializer(project, context={'request': request, 'editor': spec}).data
        return Response({**body, 'created': created, 'renamed': renamed, 'skipped': skipped},
                        status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)


def clean_preview_storage(raw):
    """
    Données ``localStorage`` envoyées par l'éditeur pour l'aperçu : un objet « clé -> chaîne », dans les plafonds.
    Tout le reste (JSON invalide, mauvais types, trop gros) est ignoré : l'aperçu démarre alors avec un stockage vide.
    """
    try:
        data = json.loads(raw or "{}")
    except ValueError:
        return {}
    if not isinstance(data, dict) or len(data) > PREVIEW_STORAGE_MAX_KEYS:
        return {}
    if not all(isinstance(v, str) for v in data.values()):
        return {}
    if sum(len(k) + len(v) for k, v in data.items()) > PREVIEW_STORAGE_MAX_CHARS:
        return {}
    return data


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
            "storage": clean_preview_storage(request.POST.get("storage", "")),
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
        # « allow-forms » : sans lui le navigateur ne déclenche même pas l'évènement « submit » d'un formulaire
        # (le bouton « Ajouter » d'une application de tâches reste muet). Il ne donne pas accès à la session :
        # l'origine reste opaque, donc les cookies SameSite ne partent pas et le contrôle CSRF de l'API refuse.
        # Ni « allow-same-origin », ni « allow-top-navigation », ni « allow-popups ».
        response["Content-Security-Policy"] = "sandbox allow-scripts allow-modals allow-forms"
        return response
