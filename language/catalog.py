"""Données de navigation partagées : accueil, sélecteur de langage, fil d'Ariane."""

from django.templatetags.static import static
from django.urls import reverse

from .config import CATEGORIES, PAGES, Page


def page_url(page: Page) -> str:
    return reverse(page.key)


def serialize(page: Page) -> dict:
    return {
        "key": page.key,
        "title": page.title,
        "description": page.description,
        "category": page.category,
        "color": page.color,
        "icon": static(page.icon),
        "url": page_url(page),
        "runnable": page.runnable,
    }


def grouped_catalog() -> list:
    """[{key, title, description, pages: [...]}, …] dans l'ordre des catégories."""
    groups = []
    for key, title, description in CATEGORIES:
        pages = [serialize(p) for p in PAGES.values() if p.category == key]
        if pages:
            groups.append({"key": key, "title": title, "description": description, "pages": pages})
    return groups


def category_title(key: str) -> str:
    return next((title for k, title, _ in CATEGORIES if k == key), "")
