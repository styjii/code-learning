from rest_framework import serializers

from .models import Project


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
        duplicates = Project.objects.filter(owner=user, name=value)
        if self.instance is not None:
            duplicates = duplicates.exclude(pk=self.instance.pk)
        if duplicates.exists():
            raise serializers.ValidationError("Un projet porte déjà ce nom.")
        return value
