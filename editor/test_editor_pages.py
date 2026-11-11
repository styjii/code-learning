"""
Une seule vue de page pour les trois éditeurs : l'éditeur courant (``codelab-js``, ``codelab-ts`` ou ``codelab-py``)
est un paramètre d'URL ; les anciens identifiants ne sont plus utilisés nulle part.
"""
import re
from pathlib import Path

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import resolve, reverse

from . import editors
from .models import Project
from .views import EditorPageView, ProjectViewSet

User = get_user_model()
PASSWORD = "Mot-de-passe-solide-42"
APP_DIR = Path(__file__).resolve().parent


class EditorPageViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.create_user("alice", password=PASSWORD))

    def test_the_three_pages_are_served_by_the_same_view_with_the_editor_as_parameter(self):
        for editor in editors.EDITORS:
            with self.subTest(editor=editor):
                match = resolve(f"/editor/{editor}/")
                self.assertIs(match.func.view_class, EditorPageView)
                self.assertEqual(match.kwargs, {"editor": editor})
                self.assertEqual(reverse("editor", kwargs={"editor": editor}), f"/editor/{editor}/")

    def test_the_three_apis_are_served_by_the_same_viewset(self):
        for editor in editors.EDITORS:
            with self.subTest(editor=editor):
                self.assertIs(resolve(f"/editor/api/{editor}/projects/").func.cls, ProjectViewSet)
                self.assertIs(resolve(f"/editor/api/{editor}/projects/3/").func.cls, ProjectViewSet)

    def test_each_editor_gets_its_own_template(self):
        for editor, template in (("codelab-js", "editor/codelab-js.html"), ("codelab-ts", "editor/codelab-ts.html"),
                                 ("codelab-py", "editor/codelab-py.html")):
            with self.subTest(editor=editor):
                response = self.client.get(f"/editor/{editor}/")
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, template)
                self.assertTemplateUsed(response, "editor/_mode_switch.html")

    def test_the_editor_switch_lists_all_editors_and_marks_the_current_one(self):
        for current in editors.EDITORS:
            html = self.client.get(f"/editor/{current}/").content.decode()
            switch = re.search(r'<nav class="mode-switch".*?</nav>', html, re.S).group(0)
            for editor in editors.EDITORS:
                with self.subTest(current=current, editor=editor):
                    self.assertIn(f'href="/editor/{editor}/"', switch)
            self.assertEqual(switch.count("aria-current"), 1)
            self.assertRegex(switch, rf'href="/editor/{current}/" aria-current="page"')

    def test_the_import_modal_has_the_confirmation_block_in_every_editor(self):
        """Doublon à l'import : le bloc d'import (#import-block) est remplacé par #import-conflict (ZipImporter.js)."""
        for editor in editors.EDITORS:
            html = self.client.get(f"/editor/{editor}/").content.decode()
            with self.subTest(editor=editor):
                self.assertTemplateUsed(self.client.get(f"/editor/{editor}/"), "editor/_import_conflict.html")
                for element_id in ("import-block", "import-conflict", "import-conflict-message", "import-rename-input",
                                   "import-rename-btn", "import-overwrite-btn", "import-cancel-btn", "import-conflict-error",
                                   "zip-input", "import-btn", "import-feedback", "import-success"):
                    self.assertIn(f'id="{element_id}"', html)
                self.assertRegex(html, r'id="import-conflict"[^>]*style="display: none;"')      # masqué au départ

    def test_unknown_editors_are_404(self):
        for editor in ("web", "ts", "py", "js", "codelab", "codelab-rb", "api"):
            with self.subTest(editor=editor):
                self.assertEqual(self.client.get(f"/editor/{editor}/").status_code, 404)

    def test_old_addresses_redirect_to_the_new_ones(self):
        for old, new in (("/editor/", "codelab-js"), ("/editor/python/", "codelab-py"), ("/editor/typescript/", "codelab-ts")):
            with self.subTest(old=old):
                response = self.client.get(old)
                self.assertEqual(response.status_code, 301)
                self.assertEqual(response["Location"], f"/editor/{new}/")

    def test_anonymous_is_sent_to_the_login_page(self):
        for editor in editors.EDITORS:
            response = Client().get(f"/editor/{editor}/")
            self.assertEqual(response.status_code, 302)
            self.assertIn("/accounts/login/", response["Location"])

    def test_the_page_sets_the_csrf_cookie(self):
        self.assertIn("csrftoken", self.client.get("/editor/codelab-py/").cookies)

    def test_every_editor_has_a_choice_in_the_model(self):
        self.assertEqual([value for value, _ in Project._meta.get_field("editor").choices], list(editors.EDITORS))


class NoLegacyIdentifierTests(TestCase):
    """Les anciennes adresses d'API et les anciens noms d'éditeurs ne subsistent ni dans les gabarits ni dans le JS."""

    FORBIDDEN = re.compile(
        r"ts-projects|py-projects|api/projects|api/(?:ts-|py-)?(?:import|export)-zip|editor-index|"
        r"typescript-editor|python-editor(?!:v1)|editor/(?:python|typescript)/")

    def test_sources_use_the_codelab_identifiers(self):
        files = [*(APP_DIR / "templates").rglob("*.html"), *(APP_DIR / "static" / "editor" / "js").rglob("*.js"),
                 *(APP_DIR.parent / "webapp" / "templates").rglob("*.html"),
                 *(APP_DIR.parent / "language" / "templates").rglob("*.html")]
        for path in files:
            with self.subTest(file=str(path.relative_to(APP_DIR.parent))):
                self.assertIsNone(self.FORBIDDEN.search(path.read_text(encoding="utf-8")))
