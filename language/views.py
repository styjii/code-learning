import logging
import re

from django.http import Http404
from django.views.generic import TemplateView

from .catalog import category_title, grouped_catalog, serialize
from .config import PAGES
from .services import get_page_html

logger = logging.getLogger(__name__)

_CODE_TAG = re.compile(r"<code\b[^>]*\blanguage-[^>]*>")


def mark_read_only(html: str) -> str:
    """
    Ajoute ``data-run="false"`` à chaque bloc de code du HTML.

    Utilisé pour les pages non exécutables : même un ancien ``RunnableBlocks.js`` resté dans le cache
    du navigateur ne leur ajoutera pas de bouton « Exécuter ».
    """
    def mark(match: re.Match) -> str:
        tag = match.group(0)
        return tag if "data-run=" in tag else f'{tag[:-1]} data-run="false">'

    return _CODE_TAG.sub(mark, html)


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
            if content and not page.runnable:
                content = mark_read_only(content)
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
