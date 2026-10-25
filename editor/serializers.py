from rest_framework import serializers

from .models import Project, TypeScriptProject
from .typescript_config import effective_compiler_options, validate_compiler_options


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer du modèle Project (champs : id, name, html, css, js).
    Le propriétaire n'est jamais fourni par le client : il est fixé côté serveur.
    """

    class Meta:
        model = Project
        fields = ["id", "name", "html", "css", "js"]

    def validate_name(self, value):
        """Le nom doit être unique parmi les projets de l'utilisateur."""
        user = self.context["request"].user
        duplicates = self.Meta.model.objects.filter(owner=user, name=value)
        if self.instance is not None:
            duplicates = duplicates.exclude(pk=self.instance.pk)
        if duplicates.exists():
            raise serializers.ValidationError("Un projet porte déjà ce nom.")
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
