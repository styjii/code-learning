from django.conf import settings
from django.db import models


class Project(models.Model):
    """
    Projet front-end (HTML/CSS/JS) appartenant à un utilisateur.

    Fields:
        - owner: utilisateur propriétaire (chacun ne voit que ses projets).
        - name: nom du projet, unique par utilisateur.
        - html, css, js: code source.
    """
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="editor_projects",
    )
    name = models.CharField(max_length=100)
    html = models.TextField(blank=True)
    css = models.TextField(blank=True)
    js = models.TextField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["owner", "name"], name="unique_project_name_per_owner"),
        ]

    def __str__(self):
        return self.name


class EditorPreferences(models.Model):
    """
    Préférences de l'éditeur propres à un utilisateur.

    ``monaco`` ne contient que des clés de la liste blanche (voir ``monaco_config.py``) : elles sont
    validées avant écriture et filtrées à nouveau à la lecture.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="editor_preferences",
    )
    monaco = models.JSONField(default=dict, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Préférences de {self.user}"
