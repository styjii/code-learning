from django.conf import settings
from django.db import models

from . import editors


class Project(models.Model):
    """
    Projet d'un des éditeurs en ligne (``codelab-js``, ``codelab-ts`` ou ``codelab-py``) appartenant à un utilisateur.

    Fields:
        - owner: utilisateur propriétaire (chacun ne voit que ses projets).
        - editor: éditeur du projet. Le nom d'un projet n'est unique que dans son éditeur.
        - name: nom du projet.
        - data: contenu du projet ; les clés dépendent de l'éditeur (voir ``editors.py``) :
          ``html``/``css``/``js`` (codelab-js), ``html``/``css``/``ts``/``compiler_options`` (codelab-ts) ou
          ``files`` (codelab-py). Validé par l'API avant écriture.

    Unicité : (owner, editor, name) -- deux éditeurs peuvent avoir un projet de même nom, jamais un même éditeur.
    """
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="editor_projects",
    )
    editor = models.CharField(max_length=20, choices=editors.choices(), default=editors.CODELAB_JS)
    name = models.CharField(max_length=100)
    data = models.JSONField(default=dict, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["owner", "editor", "name"], name="unique_project_name_per_owner_and_editor"),
        ]

    def __str__(self):
        return f"{self.name} ({self.editor})"


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
