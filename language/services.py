"""Accès au contenu des pages : conversion Markdown -> HTML à la demande, avec mise en cache en base."""

import threading
from pathlib import Path
from typing import Optional

from core.database_manager import Database
from core.markdown_to_tabbed_html import CONVERTER_VERSION, MarkdownToTabbedHTML
from .config import PAGE_CONFIG

SRC_DIR = Path(__file__).resolve().parent.parent
TOPICS_DIR = SRC_DIR / "language" / "topics"

_lock = threading.Lock()


def _signature(key: str) -> str:
    """Empreinte de la source : version du convertisseur + date/taille du fichier Markdown."""
    stat = (TOPICS_DIR / PAGE_CONFIG[key][0]).stat()
    return f"{CONVERTER_VERSION}:{stat.st_mtime_ns}:{stat.st_size}"


def is_up_to_date(db: Database, key: str) -> bool:
    return db.read(key) is not None and db.get_signature(key) == _signature(key)


def stale_keys() -> list:
    """Clés dont le contenu est absent ou périmé (fichier modifié, convertisseur mis à jour)."""
    with Database() as db:
        return [key for key in PAGE_CONFIG if not is_up_to_date(db, key)]


def get_page_html(key: str, force: bool = False) -> Optional[str]:
    """
    Retourne le HTML d'une page, en le (re)générant si nécessaire.

    Lève KeyError pour une clé inconnue et FileNotFoundError si le Markdown manque.
    """
    if key not in PAGE_CONFIG:
        raise KeyError(key)

    with _lock, Database() as db:
        if not force and is_up_to_date(db, key):
            return db.read(key)

        converter = MarkdownToTabbedHTML(TOPICS_DIR / PAGE_CONFIG[key][0])
        content = converter.convert()
        db.create_or_update(key, content, _signature(key))
        return content
