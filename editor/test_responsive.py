"""
Garde-fous du responsive des trois éditeurs (Web, Python, TypeScript).

Le rendu lui-même (débordements, menus, modales, tailles de cibles) se vérifie dans un navigateur ; ces tests
protègent ce qui se casse silencieusement dans les gabarits et les feuilles de style.
"""
import re
from pathlib import Path

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

CSS_DIR = Path(__file__).resolve().parent / "static" / "editor" / "css"
EDITOR_URLS = ("codelab-js", "codelab-py", "codelab-ts")


class EditorTemplatesResponsiveTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user("alice", password="Mot-de-passe-solide-42")
        self.client = Client()
        self.client.force_login(user)

    def html(self, name):
        response = self.client.get(reverse("editor", args=[name]))
        self.assertEqual(response.status_code, 200)
        return response.content.decode()

    def test_editors_declare_viewport_with_safe_areas(self):
        for name in EDITOR_URLS:
            with self.subTest(page=name):
                viewport = re.search(r'<meta name="viewport" content="([^"]+)"', self.html(name)).group(1)
                self.assertIn("width=device-width", viewport)
                self.assertIn("initial-scale=1", viewport)
                self.assertIn("viewport-fit=cover", viewport)      # zones sûres (encoche, barre d'accueil iOS)
                self.assertNotIn("maximum-scale", viewport)         # ne jamais interdire le zoom (accessibilité)
                self.assertNotIn("user-scalable", viewport)

    def test_other_pages_keep_the_default_viewport(self):
        viewport = re.search(r'<meta name="viewport" content="([^"]+)"', self.client.get("/").content.decode()).group(1)
        self.assertEqual(viewport, "width=device-width, initial-scale=1")

    def test_logo_link_has_an_accessible_name_when_the_word_is_hidden(self):
        # Sous 900 px le texte « Éditeur » est masqué : sans aria-label, le lien n'aurait plus de nom.
        for name in EDITOR_URLS:
            with self.subTest(page=name):
                self.assertIn('aria-label="Éditeur : retour à l\'accueil"', self.html(name))

    def test_header_is_shared_by_the_three_editors(self):
        for name in EDITOR_URLS:
            with self.subTest(page=name):
                page = self.html(name)
                for needle in ('class="app-header"', 'class="mode-switch"', 'class="topbar-actions"', "editor/css/layout.css", "editor/css/navigation.css"):
                    self.assertIn(needle, page)


class EditorStylesheetsResponsiveTests(TestCase):
    """Les règles qui évitent les régressions les plus coûteuses à retrouver."""

    def css(self, name):
        return (CSS_DIR / name).read_text(encoding="utf-8")

    def test_body_uses_dynamic_viewport_height(self):
        # 100vh dépasse la zone visible sur mobile (barre d'adresse) : la barre du bas passerait dessous.
        layout = self.css("layout.css")
        self.assertIn("100dvh", layout)
        self.assertRegex(layout, r"min-height:\s*0")

    def test_phone_header_and_menus_have_a_narrow_layout(self):
        self.assertIn("max-width: 599.98px", self.css("layout.css"))
        self.assertIn("max-width: 599.98px", self.css("navigation.css"))

    def test_touch_targets_follow_the_pointer_type(self):
        layout = self.css("layout.css")
        self.assertRegex(layout, r"@media \(pointer: coarse\)\s*\{\s*body\.editor-app\s*\{[^}]*--tap:\s*44px")

    def test_iframe_cannot_overflow_its_container(self):
        # Un <iframe> a une hauteur minimale automatique de 150 px : sans min-height: 0 il recouvre la barre du bas.
        self.assertRegex(self.css("editor.css"), r"#output\s*\{[^}]*min-height:\s*0")

    def test_text_inputs_stay_at_16px_on_touch_screens(self):
        # En dessous, Safari iOS zoome sur le champ à la saisie.
        self.assertRegex(self.css("modal.css"), r"font-size:\s*max\(16px,\s*1em\)")

    def test_modals_never_exceed_the_screen(self):
        self.assertRegex(self.css("modal.css"), r"\.custom-modal\s*\{[^}]*max-height:\s*100%")
