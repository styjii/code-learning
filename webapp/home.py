"""Contenu de la page d'accueil : onglets du catalogue, statistiques réelles des cours, textes et liens du pied de page.

Les chiffres des cartes (sections, exemples de code) sont calculés à partir des fichiers Markdown des cours.
Les valeurs marquées « à adapter » reprennent la maquette : remplacez-les par vos données réelles.
"""

from functools import lru_cache

from language.catalog import grouped_catalog
from language.config import PAGES
from language.services import TOPICS_DIR

# Onglets du catalogue. « in_tabbar » faux : le panneau existe mais s'ouvre seulement depuis le menu (Exercices, Projets).
TABS = [
    {"key": "langages", "title": "Langages Fondamentaux", "icon": "i-code", "categories": ["topics"], "in_tabbar": True},
    {"key": "frameworks", "title": "Frameworks & Bibliothèques", "icon": "i-layers", "categories": ["frameworks", "modules"], "in_tabbar": True},
    {"key": "backend", "title": "Back-end & Systèmes", "icon": "i-server", "categories": ["database", "system"], "in_tabbar": True},
    {"key": "exercices", "title": "Exercices & Corrigés", "icon": "i-target", "categories": ["exercises", "solutions"], "in_tabbar": False},
    {"key": "projets", "title": "Projets", "icon": "i-folder", "categories": ["projects"], "in_tabbar": False},
]

# À adapter : preuve sociale affichée sous les boutons du hero (valeurs de la maquette).
SOCIAL_PROOF = {"developers": "100 000", "rating": "4.8", "rating_label": "Satisfaction des apprenants"}

# À adapter : cible du bouton de la section communauté et réseaux du pied de page (« # » = pas encore de lien).
COMMUNITY_URL = "#community"
SOCIAL_LINKS = [
    {"key": "youtube", "label": "YouTube", "icon": "i-youtube", "url": "#"},
    {"key": "github", "label": "GitHub", "icon": "i-github", "url": "#"},
    {"key": "discord", "label": "Discord", "icon": "i-discord", "url": "#"},
    {"key": "linkedin", "label": "LinkedIn", "icon": "i-linkedin", "url": "#"},
]
FOOTER_LINKS = [
    {"label": "À propos", "url": "#why"},
    {"label": "Cours", "url": "#courses", "tab": "langages"},
    {"label": "Exercices", "url": "#courses", "tab": "exercices"},
    {"label": "Projets", "url": "#courses", "tab": "projets"},
    {"label": "Communauté", "url": "#community"},
    {"label": "FAQ", "url": "#"},
    {"label": "Contact", "url": "#"},
]


@lru_cache(maxsize=256)
def _count(path: str, mtime_ns: int) -> tuple:
    """(sections « ## », blocs de code) d'un fichier Markdown ; les « ## » dans un bloc de code sont ignorés."""
    sections = examples = 0
    fence = ""
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            stripped = line.lstrip()
            marker = stripped[:3]
            if marker in ("```", "~~~"):
                if not fence:
                    fence = marker
                    examples += 1
                elif marker == fence:
                    fence = ""
            elif not fence and line.startswith("## "):
                sections += 1
    return sections, examples


def content_stats(page_key: str) -> dict:
    """Statistiques d'un cours ; vide si le fichier est introuvable."""
    page = PAGES.get(page_key)
    if page is None:
        return {}
    path = TOPICS_DIR / page.file
    try:
        sections, examples = _count(str(path), path.stat().st_mtime_ns)
    except OSError:
        return {}
    return {"sections": sections, "examples": examples}


def home_context() -> dict:
    """Contexte du gabarit d'accueil : onglets (avec cartes), preuve sociale, liens."""
    groups = {group["key"]: group for group in grouped_catalog()}
    tabs = []
    total = 0
    for tab in TABS:
        panel_groups = []
        for key in tab["categories"]:
            group = groups.get(key)
            if not group:
                continue
            pages = [{**page, **content_stats(page["key"])} for page in group["pages"]]
            total += len(pages)
            panel_groups.append({**group, "pages": pages})
        if panel_groups:
            tabs.append({**tab, "groups": panel_groups, "count": sum(len(g["pages"]) for g in panel_groups)})
    return {
        "tabs": tabs,
        "tabbar": [tab for tab in tabs if tab["in_tabbar"]],
        "social_proof": SOCIAL_PROOF,
        "community_url": COMMUNITY_URL,
        "social_links": SOCIAL_LINKS,
        "footer_links": FOOTER_LINKS,
    }
