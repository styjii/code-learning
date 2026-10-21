import logging

from django.http import Http404
from django.views.generic import TemplateView

from .catalog import category_title, grouped_catalog, serialize
from .config import PAGES
from .services import get_page_html

logger = logging.getLogger(__name__)


class MarkdownPageView(TemplateView):
    """
    Affiche une page de cours générée depuis un fichier Markdown.

    Attributes:
        key: clé de la page dans ``language.config.PAGES``.
    """
    template_name = "language/index.html"
    key: str = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        page = PAGES.get(self.key)
        if page is None:
            raise Http404(f"Page inconnue : {self.key}")

        content, notice = None, None
        try:
            content = get_page_html(self.key)
        except FileNotFoundError:
            logger.exception("Fichier Markdown introuvable pour %s", self.key)
            notice = "Le fichier source de ce cours est introuvable."
        except Exception:
            logger.exception("Erreur de chargement pour %s", self.key)
            notice = "Impossible de charger ce cours pour le moment."

        context.update({
            "page": serialize(page),
            "page_title": page.title,
            "category_title": category_title(page.category),
            "catalog": grouped_catalog(),
            "content": content,
            "notice": notice,
        })
        return context
