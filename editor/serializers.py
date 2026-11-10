from rest_framework import serializers

from . import python_files
from .models import Project, PythonProject, TypeScriptProject
from .typescript_config import effective_compiler_options, validate_compiler_options

DUPLICATE_NAME_MESSAGE = "Un projet porte déjà ce nom."


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer du modèle Project (champs : id, name, html, css, js).
    Le propriétaire n'est jamais fourni par le client : il est fixé côté serveur.
    """

    class Meta:
        model = Project
        fields = ["id", "name", "html", "css", "js"]

    def validate_name(self, value):
        """
        Le nom doit être unique parmi les projets de l'utilisateur.

        Ce contrôle donne un message clair dans le cas courant ; la contrainte en base
        (``unique_project_name_per_owner``) reste la garantie finale, et la vue transforme son
        ``IntegrityError`` en 400 (deux requêtes simultanées peuvent passer ce contrôle ensemble).
        """
        user = self.context["request"].user
        duplicates = self.Meta.model.objects.filter(owner=user, name=value)
        if self.instance is not None:
            duplicates = duplicates.exclude(pk=self.instance.pk)
        if duplicates.exists():
            raise serializers.ValidationError(DUPLICATE_NAME_MESSAGE)
        return value


class TypeScriptProjectSerializer(ProjectSerializer):
    """
    Serializer du modèle TypeScriptProject (champs : id, name, html, css, ts, compiler_options).

    ``compiler_options`` est vérifié contre la liste blanche (400 sinon) ; en lecture, le client reçoit toujours
    des options complètes (valeurs par défaut + celles du projet).
    """
    compiler_options = serializers.JSONField(required=False)

    class Meta:
        model = TypeScriptProject
        fields = ["id", "name", "html", "css", "ts", "compiler_options"]

    def validate_compiler_options(self, value):
        clean, errors = validate_compiler_options(value)
        if errors:
            raise serializers.ValidationError(errors)
        return clean

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["compiler_options"] = effective_compiler_options(instance.compiler_options)
        return data


class PythonProjectSerializer(ProjectSerializer):
    """
    Serializer du modèle PythonProject (champs : id, name, files).

    ``files`` est la liste ``[{"name", "content"}]`` du projet ; elle est vérifiée avec les règles de
    ``python_files.py`` (noms, doublons, limites de taille et de nombre : 400 sinon). Une liste vide est acceptée :
    le navigateur ajoute alors ``main.py``.
    """
    files = serializers.JSONField(required=False)

    class Meta:
        model = PythonProject
        fields = ["id", "name", "files"]

    def validate_files(self, value):
        error = python_files.files_error(value, allow_empty=True)
        if error:
            raise serializers.ValidationError(error)
        # On ne garde que les clés attendues : rien d'autre n'est stocké.
        return [{"name": f["name"], "content": f["content"]} for f in value]
