"""Page d'accueil : maquette CodeLearn (hero, éditeur de démonstration, catalogue à onglets, sections, pied de page)."""

import re
import tempfile
from pathlib import Path
from unittest import mock

from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from . import home

STATIC = Path(__file__).resolve().parent / "static" / "webapp"


class ContentStatsTests(SimpleTestCase):
    def count(self, text):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "cours.md"
            path.write_text(text, encoding="utf-8")
            return home._count(str(path), path.stat().st_mtime_ns)

    def test_counts_sections_and_code_blocks(self):
        sections, examples = self.count("# Titre\n\n## Un\n\n```py\nx = 1\n```\n\n## Deux\n\n```js\nlet a;\n```\n")
        self.assertEqual((sections, examples), (2, 2))

    def test_ignores_headings_inside_code_blocks(self):
        sections, examples = self.count("## Vrai\n\n```bash\n## commentaire shell\n```\n\n~~~\n## encore un commentaire\n~~~\n")
        self.assertEqual((sections, examples), (1, 2))

    def test_unknown_page_has_no_stats(self):
        self.assertEqual(home.content_stats("inexistant"), {})

    def test_real_course_has_stats(self):
        stats = home.content_stats("javascript")
        self.assertGreater(stats["sections"], 5)
        self.assertGreater(stats["examples"], 5)


class HomeContextTests(SimpleTestCase):
    def test_tabbar_matches_the_mockup_and_extra_panels_exist(self):
        context = home.home_context()
        self.assertEqual([t["title"] for t in context["tabbar"]],
                         ["Langages Fondamentaux", "Frameworks & Bibliothèques", "Back-end & Systèmes"])
        keys = [t["key"] for t in context["tabs"]]
        self.assertIn("exercices", keys)
        self.assertIn("projets", keys)

    def test_every_catalog_page_is_reachable_from_a_tab(self):
        from language.catalog import grouped_catalog
        expected = {page["key"] for group in grouped_catalog() for page in group["pages"]}
        shown = {page["key"] for tab in home.home_context()["tabs"] for group in tab["groups"] for page in group["pages"]}
        self.assertEqual(shown, expected)


class HomePageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user("eleve", password="mot-de-passe-solide-123")

    def setUp(self):
        self.client.force_login(self.user)
        with mock.patch("webapp.views.stale_keys", return_value=[]):
            self.page = self.client.get(reverse("index")).content.decode()

    def test_hero_texts_and_buttons(self):
        for text in ("Maîtrisez le code,", "concrétisez", "vos idées", "Commencer à apprendre", "Explorer les codes",
                     "4.8/5", "Satisfaction des apprenants", "Apprendre", "Pratiquer", "Réussir"):
            self.assertIn(text, self.page)
        self.assertEqual(len(re.findall(r'<li><svg viewBox="0 0 40 40"><use href="#av-\d"', self.page)), 4)

    def test_demo_editor_matches_the_mockup(self):
        for text in ("Explorer", "mon-projet", "components", "App.jsx", "Header.jsx", "package.json", "README.md",
                     "Prévisualisation", "Apprendre à coder", "Découvrir", "data-ide"):
            self.assertIn(text, self.page)

    def test_editor_links_are_kept(self):
        for name in ("codelab-js", "codelab-ts", "codelab-py"):
            self.assertContains(self.client.get(reverse("index")), f'href="{reverse("editor", args=[name])}"')

    def test_tabs_are_accessible_and_filter_real_courses(self):
        self.assertEqual(self.page.count('role="tab"'), 3)
        self.assertIn('role="tablist"', self.page)
        self.assertIn('aria-selected="true"', self.page)
        self.assertEqual(self.page.count('role="tabpanel"'), 5)
        for title in ("JavaScript", "TypeScript", "Python", "Django", "PostgreSQL", "Commandes Linux"):
            self.assertIn(f'<span class="lang-title">{title}</span>', self.page)
        self.assertRegex(self.page, r"\d+ sections? <i[^>]*>&bull;</i> \d+ exemples?")

    def test_secondary_sections_and_footer(self):
        for text in ("Pourquoi nous choisir ?", "Apprentissage pratique", "Accompagnement humain", "Projets réels",
                     "Suivi de progression", "Rejoignez notre communauté de développeurs !", "Rejoignez la communauté",
                     "Ensemble,", "allons plus loin !", "Apprendre aujourd'hui. Créer demain.", "À propos", "FAQ", "Contact"):
            self.assertIn(text, self.page)
        for label in ("YouTube", "GitHub", "Discord", "LinkedIn"):
            self.assertIn(f'aria-label="{label}"', self.page)

    def test_scroll_reveal_markup(self):
        self.assertGreaterEqual(self.page.count("data-reveal"), 8)

    def test_logout_form_for_authenticated_user(self):
        self.assertIn(reverse("logout"), self.page)
        self.assertIn("Déconnexion", self.page)


class HomeAssetsTests(SimpleTestCase):
    def css(self):
        return (STATIC / "css" / "style.css").read_text(encoding="utf-8")

    def test_animations_use_compositor_properties_only(self):
        css = re.sub(r"/\*.*?\*/", "", self.css(), flags=re.S)
        bodies = []
        for match in re.finditer(r"@keyframes\s+[\w-]+\s*\{", css):
            depth, index = 1, match.end()
            while depth:
                depth += {"{": 1, "}": -1}.get(css[index], 0)
                index += 1
            bodies.append(css[match.end():index - 1])
        self.assertGreaterEqual(len(bodies), 8)
        for body in bodies:
            # Propriétés déclarées dans les images clés : uniquement transform / opacity (stroke-dashoffset pour les traits).
            declared = set(re.findall(r"([\w-]+)\s*:\s*[^;{}]+;", body))
            self.assertLessEqual(declared, {"transform", "opacity"}, body)

    def test_hover_effects_requested_by_the_design(self):
        css = self.css()
        self.assertIn(".ide:hover { transform: rotateY(-2deg) rotateX(0.5deg) translate3d(0, -6px, 0) scale(1.012); }", css)
        self.assertIn(".ide:hover .ide-glow { opacity: 0.95;", css)
        self.assertIn(".lang-card:hover { z-index: 2; transform: scale(1.05);", css)
        self.assertIn(".lang-card:hover .lang-go svg { transform: translate3d(4px, 0, 0); }", css)
        self.assertIn("@keyframes card-in", css)
        self.assertIn("@keyframes shine", css)
        self.assertIn("@keyframes pulse", css)

    def test_no_emoji_in_the_home_files(self):
        emoji = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B50\u2B06\u2B07\u2705]")
        for path in [STATIC / "css" / "style.css", *(STATIC / "js").rglob("*.js"),
                     Path(__file__).resolve().parent / "templates" / "webapp" / "index.html"]:
            self.assertIsNone(emoji.search(path.read_text(encoding="utf-8")), path.name)

    def test_illustration_is_a_valid_svg(self):
        import xml.dom.minidom
        xml.dom.minidom.parse(str(STATIC / "img" / "community.svg"))
