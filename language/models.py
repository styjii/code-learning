from django.db import models


class PageContent(models.Model):
    """
    HTML généré à partir d'un fichier Markdown de ``language/topics/``.

    Fields:
        - key: clé de la page dans ``language.config.PAGES`` (ex. ``"frameworks/django"``).
        - content: HTML à onglets produit par ``MarkdownToTabbedHTML``.
        - signature: empreinte de la source (version du convertisseur + date/taille du .md).
          Quand elle diffère de l'empreinte actuelle, la page est régénérée.
        - updated_at: date de la dernière génération.
    """
    key = models.CharField(max_length=100, unique=True)
    content = models.TextField(blank=True)
    signature = models.CharField(max_length=100, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["key"]

    def __str__(self):
        return self.key
