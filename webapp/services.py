from language.config import PAGE_CONFIG
from language.services import get_page_html


def process_language_entry(index: int) -> dict:
    """
    Prépare une page de cours (conversion Markdown -> HTML + mise en base).

    Args:
        index: position de la page dans PAGE_CONFIG.

    Returns:
        {"status": "ok", "index": …, "title": …} ou {"status": "done"} quand tout est traité.
    """
    keys = list(PAGE_CONFIG.keys())
    if index < 0 or index >= len(keys):
        return {"status": "done"}

    key = keys[index]
    get_page_html(key)
    return {"status": "ok", "index": index, "title": PAGE_CONFIG[key][1]}
