"""
test_markdown_to_tabbed_html.py
===============================

Test Suite for MarkdownToTabbedHTML
-----------------------------------

This module contains unit tests for verifying the functionality of the
`MarkdownToTabbedHTML` class, which converts Markdown content into a
tabbed HTML layout with syntax highlighting and structural enhancements.

Test Coverage
-------------
- Markdown file existence and reading
- Markdown to HTML conversion
- Tab structure generation from <h1> headers
- Code block highlighting
- Table rendering support
- Subheader (<h3>-<h6>) wrapping behavior
- Saving output HTML to file

Dependencies
------------
- pytest
- beautifulsoup4 (bs4)
- markdown
- pygments

Usage
-----
Run all tests:
    pytest test_markdown_to_tabbed_html.py

Check test coverage:
    pytest --cov=api.markdown_to_tabbed_html test_markdown_to_tabbed_html.py

Fixtures
--------
- `sample_md_file`: Temporary Markdown file with sample content.
- `converter_with_sample`: MarkdownToTabbedHTML instance using the sample file.
"""

import pytest
from pathlib import Path
from bs4 import BeautifulSoup
from core.markdown_to_tabbed_html import MarkdownToTabbedHTML

# Sample markdown content for testing
SAMPLE_MARKDOWN: str = """# Tab One

This is **bold** text.

```python
print("Hello, World!")
```

# Tab Two

| A | B |
|---|---|
| 1 | 2 |
"""

@pytest.fixture
def sample_md_file(tmp_path: Path) -> Path:
    """
    Create a temporary Markdown file with sample content.
    """
    file_path = tmp_path / "sample.md"
    file_path.write_text(SAMPLE_MARKDOWN, encoding="utf-8")
    return file_path

@pytest.fixture
def converter_with_sample(sample_md_file: Path) -> MarkdownToTabbedHTML:
    """
    Return a MarkdownToTabbedHTML instance using the sample markdown file.
    """
    return MarkdownToTabbedHTML(sample_md_file)

def test_validate_file_exists(sample_md_file: Path) -> None:
    """
    Ensure file validation passes for existing file and raises for missing file.
    """
    converter = MarkdownToTabbedHTML(sample_md_file)
    converter._validate_file_exists()  # Should not raise

    missing_file = sample_md_file.parent / "missing.md"
    converter_missing = MarkdownToTabbedHTML(missing_file)
    with pytest.raises(FileNotFoundError):
        converter_missing._validate_file_exists()

def test_read_markdown(converter_with_sample: MarkdownToTabbedHTML) -> None:
    """
    Check that the Markdown content is read correctly from file.
    """
    content = converter_with_sample._read_markdown()
    assert SAMPLE_MARKDOWN.strip() == content.strip()

def test_convert_to_html(converter_with_sample: MarkdownToTabbedHTML) -> None:
    """
    Ensure the HTML output contains expected tab, table, and code structure.
    """
    html_output = converter_with_sample.convert()
    assert '<ul class="tab-bar"' in html_output
    assert '<div class="tab-content"' in html_output
    assert 'language-python' in html_output
    assert '<table>' in html_output

def test_save_output_file(sample_md_file: Path) -> None:
    """
    Verify that the HTML is saved to the correct location.
    """
    converter = MarkdownToTabbedHTML(sample_md_file)
    result_msg = converter.save()
    output_html = sample_md_file.with_suffix(".html")

    assert output_html.exists()
    assert "HTML enregistré" in result_msg

    html_text = output_html.read_text(encoding="utf-8")
    assert '<ul class="tab-bar"' in html_text
    assert '<div class="tab-content"' in html_text

def test_sections_have_clean_labels_and_github_ids(sample_md_file: Path) -> None:
    """Les onglets affichent le titre d'origine ; les identifiants suivent la convention GitHub."""
    html_output = MarkdownToTabbedHTML(sample_md_file).convert()
    soup = BeautifulSoup(html_output, "html.parser")
    assert [a.text for a in soup.select(".tab-link")] == ["Tab One", "Tab Two"]
    assert [p["id"] for p in soup.select(".tab-content")] == ["tab-one", "tab-two"]


def test_summary_links_resolve(tmp_path: Path) -> None:
    """Un lien de sommaire Markdown (#1-introduction) doit pointer vers un identifiant existant."""
    md = tmp_path / "doc.md"
    md.write_text("# Titre\n\n## Sommaire\n\n[Aller](#1-introduction)\n\n# 1. Introduction\n\nTexte\n\n# 2. Suite\n\nTexte\n", encoding="utf-8")
    soup = BeautifulSoup(MarkdownToTabbedHTML(md).convert(), "html.parser")
    ids = {el["id"] for el in soup.find_all(id=True)}
    assert "1-introduction" in ids
    assert soup.select_one("header.doc-hero h1.doc-title").text == "Titre"


def test_hero_div_title_is_parsed(tmp_path: Path) -> None:
    """Le titre placé dans <div align="center"> devient le titre du document (pas du texte brut)."""
    md = tmp_path / "doc.md"
    md.write_text('<div align="center">\n\n# Mon guide\n\n*Sous-titre*\n\n</div>\n\n# 1. A\n\nx\n\n# 2. B\n\ny\n', encoding="utf-8")
    html_output = MarkdownToTabbedHTML(md).convert()
    soup = BeautifulSoup(html_output, "html.parser")
    assert soup.select_one(".doc-hero .doc-title").text == "Mon guide"
    assert "# Mon guide" not in html_output


def test_html_transform_to_tabs(tmp_path: Path) -> None:
    """Les <h1> deviennent des sections."""
    html_input = """
    <h1>Tab One</h1>
    <p>Hello</p>
    <h1>Tab Two</h1>
    <p>World</p>
    """
    converter = MarkdownToTabbedHTML(tmp_path / "dummy.md")
    result = converter._tab_transformer.transform(html_input)

    assert '<ul class="tab-bar"' in result
    assert '<div class="tab-content"' in result
    assert 'id="tab-one"' in result and 'id="tab-two"' in result
