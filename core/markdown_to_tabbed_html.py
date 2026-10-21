"""
markdown_to_tabbed_html.py
==========================

Convertit un fichier Markdown en HTML structuré pour les pages de cours.

Structure produite
------------------
::

    <div class="doc" data-sections="N">
      <header class="doc-hero">      <- titre du document + texte d'introduction (optionnel)
      <ul class="tab-bar">           <- une entrée par section (omis s'il n'y a qu'une section)
      <div class="tab-content" id="…" role="tabpanel" data-label="…">
        <h1 class="section-title">…</h1> …
      </div>
      …
    </div>

Règles
------
- Le titre du document est soit le premier ``<h1>`` d'un bloc ``<div align="center">``,
  soit un ``<h1>`` unique, soit un premier ``<h1>`` suivi de sections ``<h2>``.
- Chaque ``<h1>`` restant devient une section ; s'il n'y en a pas, chaque ``<h2>`` en devient une.
- Le contenu situé avant la première section devient une section « Présentation ».
- Les titres reçoivent un identifiant de type GitHub (``1-introduction``) : les liens de
  sommaire écrits en Markdown (``[Intro](#1-introduction)``) fonctionnent donc tels quels.

Dépendances : ``markdown``, ``beautifulsoup4``, ``pygments``.
"""

import re
from pathlib import Path
from typing import List, Optional, Set, Union

import markdown
from bs4 import BeautifulSoup, Tag
from markdown.extensions.extra import ExtraExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension

from core.highlighted_code_extension import CodeHiliteWithLanguage

# À incrémenter quand le format du HTML produit change : les pages en base sont régénérées.
CONVERTER_VERSION = "3"

_NON_SLUG_CHARS = re.compile(r"[^\w\s-]", re.UNICODE)
_SPACES = re.compile(r"\s")


def slugify(text: str, separator: str = "-") -> str:
    """Identifiant façon GitHub : minuscules, ponctuation et emojis retirés, espaces -> tirets."""
    text = _NON_SLUG_CHARS.sub("", text.strip().lower())
    return _SPACES.sub(separator, text) or "section"


def _toc_slugify(value: str, separator: str) -> str:
    return slugify(value, separator)


class _TabTransformer:
    """Transforme le HTML brut en documents à sections (voir l'en-tête du module)."""

    LEAD_TAGS = {"p", "blockquote"}

    # ---- helpers -------------------------------------------------------
    @staticmethod
    def _tags(parent: Tag) -> List[Tag]:
        return [child for child in parent.children if isinstance(child, Tag)]

    @staticmethod
    def _trim_rules(nodes: List[Tag]) -> List[Tag]:
        """Retire les <hr> en début et fin de section."""
        while nodes and nodes[0].name == "hr":
            nodes.pop(0)
        while nodes and nodes[-1].name == "hr":
            nodes.pop()
        return nodes

    @staticmethod
    def _unique(candidate: str, used: Set[str]) -> str:
        slug, n = candidate, 1
        while slug in used:
            slug = f"{candidate}-{n}"
            n += 1
        used.add(slug)
        return slug

    def _find_hero(self, nodes: List[Tag]) -> Optional[Tag]:
        """Bloc <div class="doc-center"> contenant le titre, situé avant tout <h1> de premier niveau."""
        for node in nodes:
            if node.name == "h1":
                return None
            if node.name == "div" and "doc-center" in (node.get("class") or []) \
                    and node.find("h1", recursive=False):
                return node
        return None

    def _is_title_h1(self, nodes: List[Tag]) -> bool:
        """Le premier <h1> est un titre (et non une section) s'il est seul ou suivi de sections <h2>."""
        h1_positions = [i for i, n in enumerate(nodes) if n.name == "h1"]
        if not h1_positions:
            return False
        if len(h1_positions) == 1:
            return True
        between = nodes[h1_positions[0] + 1:h1_positions[1]]
        return any(n.name == "h2" for n in between)

    # ---- transformation ------------------------------------------------
    def transform(self, html: str) -> str:
        soup = BeautifulSoup(html, "html.parser")
        nodes = self._tags(soup)
        if not nodes:
            return html

        used_ids: Set[str] = {t["id"] for t in soup.find_all(id=True)}

        # 1. Titre du document + introduction
        title: Optional[Tag] = None
        lead: List[Tag] = []
        hero_div = self._find_hero(nodes)
        if hero_div is not None:
            title = hero_div.find("h1", recursive=False)
            lead = [t for t in self._tags(hero_div) if t is not title]
            nodes.remove(hero_div)
        elif self._is_title_h1(nodes):
            idx = next(i for i, n in enumerate(nodes) if n.name == "h1")
            title = nodes.pop(idx)
            while idx < len(nodes) and nodes[idx].name in self.LEAD_TAGS:
                lead.append(nodes.pop(idx))

        # 2. Niveau de découpage en sections
        tab_level = "h1" if any(n.name == "h1" for n in nodes) else "h2"

        preamble: List[Tag] = []
        sections: List[dict] = []
        for node in nodes:
            if node.name == tab_level:
                sections.append({"heading": node, "nodes": []})
            elif sections:
                sections[-1]["nodes"].append(node)
            else:
                preamble.append(node)

        preamble = self._trim_rules(preamble)
        if preamble and sections:
            heading = soup.new_tag(tab_level)
            heading.string = "Présentation"
            sections.insert(0, {"heading": heading, "nodes": preamble, "synthetic": True})
        elif preamble:
            heading = soup.new_tag("h1")
            heading.string = title.get_text(strip=True) if title else "Contenu"
            sections.append({"heading": heading, "nodes": preamble, "synthetic": True, "hide_heading": True})

        # 3. Construction du résultat
        doc = soup.new_tag("div", **{"class": "doc"})
        doc["data-sections"] = str(len(sections))

        if title is not None or lead:
            hero = soup.new_tag("header", **{"class": "doc-hero"})
            if title is not None:
                title.attrs = {"class": "doc-title"}
                hero.append(title)
            for el in lead:
                hero.append(el.extract())
            doc.append(hero)

        tab_list = soup.new_tag("ul", **{"class": "tab-bar", "role": "tablist"})
        panels: List[Tag] = []

        for index, section in enumerate(sections):
            heading: Tag = section["heading"]
            label = heading.get_text(" ", strip=True)
            existing = heading.get("id")
            if existing and not section.get("synthetic"):
                used_ids.discard(existing)
                section_id = self._unique(existing, used_ids)
            else:
                section_id = self._unique(slugify(label), used_ids)

            panel = soup.new_tag("div", **{"class": "tab-content", "id": section_id, "role": "tabpanel"})
            panel["data-label"] = label

            if not section.get("hide_heading"):
                heading.attrs = {"class": "section-title"}
                panel.append(heading.extract() if heading.parent else heading)
            for el in self._trim_rules(section["nodes"]):
                panel.append(el.extract())
            panels.append(panel)

            item = soup.new_tag("li", **{"class": "tab-item", "aria-selected": str(index == 0).lower()})
            link = soup.new_tag("a", href=f"#{section_id}", **{
                "aria-controls": section_id, "class": "tab-link", "role": "tab",
            })
            link.string = label
            item.append(link)
            tab_list.append(item)

        if len(panels) > 1:
            doc.append(tab_list)
        for panel in panels:
            doc.append(panel)
        return str(doc)


class MarkdownToTabbedHTML:
    """
    Convertit un fichier Markdown en HTML à sections.

    >>> converter = MarkdownToTabbedHTML("README.md")
    >>> html = converter.convert()
    >>> converter.save("output.html")
    """

    _CENTER_DIV = re.compile(r'^<div align="center">[ \t]*$', re.MULTILINE)
    _BARE_DETAILS = re.compile(r"^<details>[ \t]*$", re.MULTILINE)

    def __init__(self, markdown_file_path: Union[str, Path]) -> None:
        self.markdown_file_path: Path = Path(markdown_file_path)
        self._tab_transformer = _TabTransformer()

    def _validate_file_exists(self) -> None:
        if not self.markdown_file_path.exists():
            raise FileNotFoundError(f"Fichier introuvable : {self.markdown_file_path}")

    def _read_markdown(self) -> str:
        self._validate_file_exists()
        return self.markdown_file_path.read_text(encoding="utf-8")

    def _prepare(self, text: str) -> str:
        """Active le Markdown à l'intérieur des blocs HTML (centrage, <details>)."""
        text = self._CENTER_DIV.sub('<div class="doc-center" markdown="1">', text)
        return self._BARE_DETAILS.sub('<details markdown="1">', text)

    def convert(self) -> str:
        """Markdown -> HTML avec coloration syntaxique, identifiants de titres et sections."""
        raw_html = markdown.markdown(
            self._prepare(self._read_markdown()),
            extensions=[
                ExtraExtension(),
                TableExtension(),
                FencedCodeExtension(),
                CodeHiliteWithLanguage(),
                "toc",
            ],
            extension_configs={"toc": {"slugify": _toc_slugify, "permalink": False}},
            tab_length=4,
        )
        return self._tab_transformer.transform(raw_html)

    def save(self, output_path: Optional[Union[str, Path]] = None) -> str:
        """Enregistre le HTML dans un fichier (par défaut à côté du .md)."""
        html_output = self.convert()
        target = Path(output_path) if output_path else self.markdown_file_path.with_suffix(".html")
        target.write_text(html_output, encoding="utf-8")
        return f"HTML enregistré : {target}"


if __name__ == "__main__":
    root_dir = Path(__file__).resolve().parent.parent
    input_md = root_dir / "language" / "topics" / "python.md"
    output_html = root_dir / "core" / "python.html"
    print(MarkdownToTabbedHTML(input_md).save(output_html))
