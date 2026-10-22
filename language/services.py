"""Accès au contenu des pages : conversion Markdown -> HTML à la demande, avec mise en cache en base."""

import threading
from pathlib import Path
from typing import Optional

from core.markdown_to_tabbed_html import CONVERTER_VERSION, MarkdownToTabbedHTML
from .config import PAGE_CONFIG
from .models import PageContent

SRC_DIR = Path(__file__).resolve().parent.parent
TOPICS_DIR = SRC_DIR / "language" / "topics"

_lock = threading.Lock()


def _signature(key: str) -> str:
    """Empreinte de la source : version du convertisseur + date/taille du fichier Markdown."""
    stat = (TOPICS_DIR / PAGE_CONFIG[key][0]).stat()
    return f"{CONVERTER_VERSION}:{stat.st_mtime_ns}:{stat.st_size}"


def stale_keys() -> list:
    """Clés dont le contenu est absent ou périmé (fichier modifié, convertisseur mis à jour)."""
    stored = dict(PageContent.objects.values_list("key", "signature"))
    return [key for key in PAGE_CONFIG if stored.get(key) != _signature(key)]


def get_page_html(key: str, force: bool = False) -> Optional[str]:
    """
    Retourne le HTML d'une page, en le (re)générant si nécessaire.

    Lève KeyError pour une clé inconnue et FileNotFoundError si le Markdown manque.
    """
    if key not in PAGE_CONFIG:
        raise KeyError(key)

    with _lock:
        signature = _signature(key)
        if not force:
            page = PageContent.objects.filter(key=key, signature=signature).first()
            if page is not None:
                return page.content

        converter = MarkdownToTabbedHTML(TOPICS_DIR / PAGE_CONFIG[key][0])
        content = converter.convert()
        PageContent.objects.update_or_create(
            key=key,
            defaults={"content": content, "signature": signature},
        )
        return content
