"""
localStorage du code de l'aperçu : copie fournie dans le bac à sable (``preview-storage.js``), sans jamais le desserrer.
"""
import json
import re
from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import Client, SimpleTestCase, TestCase

from .views import PREVIEW_STORAGE_MAX_CHARS, PREVIEW_STORAGE_MAX_KEYS, clean_preview_storage

User = get_user_model()
PASSWORD = "Mot-de-passe-solide-42"
DATA = re.compile(r'<script id="preview-storage-data" type="application/json">(.*?)</script>', re.S)


class CleanPreviewStorageTests(SimpleTestCase):
    def test_valid_objects_are_kept(self):
        self.assertEqual(clean_preview_storage('{"tasks": "[1]", "a": ""}'), {"tasks": "[1]", "a": ""})
        self.assertEqual(clean_preview_storage(""), {})

    def test_anything_else_is_dropped_to_empty(self):
        too_many = json.dumps({f"k{i}": "" for i in range(PREVIEW_STORAGE_MAX_KEYS + 1)})
        too_big = json.dumps({"k": "x" * PREVIEW_STORAGE_MAX_CHARS})
        for raw in ("pas du json", "[1, 2]", '"texte"', "null", "5", '{"n": 1}', '{"o": {"a": 1}}', '{"l": ["x"]}',
                    too_many, too_big):
            with self.subTest(raw=raw[:30]):
                self.assertEqual(clean_preview_storage(raw), {})

    def test_limits_are_inclusive(self):
        self.assertEqual(len(clean_preview_storage(json.dumps({f"k{i}": "" for i in range(PREVIEW_STORAGE_MAX_KEYS)}))),
                         PREVIEW_STORAGE_MAX_KEYS)
        self.assertEqual(len(clean_preview_storage(json.dumps({"k": "x" * (PREVIEW_STORAGE_MAX_CHARS - 1)}))["k"]),
                         PREVIEW_STORAGE_MAX_CHARS - 1)


class PreviewPageTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.create_user("alice", password=PASSWORD))

    def page(self, **extra):
        url = self.client.post("/editor/preview/", {"html": "<p>x</p>", "css": "", "js": "1", **extra}).json()["url"]
        response = self.client.get(url)
        return response, response.content.decode()

    def test_sandbox_is_never_relaxed(self):
        response, _ = self.page(storage='{"tasks": "[1]"}')
        policy = response["Content-Security-Policy"]
        self.assertEqual(policy, "sandbox allow-scripts allow-modals allow-forms")
        for dangerous in ("allow-same-origin", "allow-top-navigation", "allow-popups", "allow-downloads"):
            self.assertNotIn(dangerous, policy)

    def test_iframes_keep_their_sandbox_attribute(self):
        for template in ("editor/codelab-js.html", "editor/codelab-ts.html"):
            with self.subTest(template=template):
                # L'iframe d'aperçu vit dans le partiel partagé par les deux éditeurs : on lit la page et ses partiels.
                folder = Path(settings.BASE_DIR) / "editor" / "templates" / "editor"
                html = "".join((folder / name).read_text(encoding="utf-8") for name in (Path(template).name, "_pane_output.html"))
                self.assertIn('sandbox="allow-scripts allow-modals allow-forms"', html)
                for dangerous in ("allow-same-origin", "allow-top-navigation", "allow-popups"):
                    self.assertNotIn(dangerous, html)

    def test_stored_data_is_embedded_and_the_shim_loads_first(self):
        _, page = self.page(storage='{"tasks": "[{\\"id\\": 1}]"}')
        self.assertEqual(json.loads(DATA.search(page).group(1)), {"tasks": '[{"id": 1}]'})
        shim = page.index("editor/js/preview-storage.js")
        self.assertLess(shim, page.index("console-runtime.js"))
        self.assertLess(shim, page.index("<!-- custom html -->"))     # avant le HTML et le JS de l'élève

    def test_values_cannot_break_out_of_the_data_block(self):
        _, page = self.page(storage=json.dumps({"x": "</script><script>alert(1)</script>"}))
        self.assertNotIn("<script>alert(1)</script>", page)
        self.assertEqual(json.loads(DATA.search(page).group(1)), {"x": "</script><script>alert(1)</script>"})

    def test_missing_or_invalid_storage_gives_an_empty_block(self):
        for extra in ({}, {"storage": "oups"}, {"storage": '{"n": 1}'}):
            with self.subTest(extra=extra):
                _, page = self.page(**extra)
                self.assertEqual(json.loads(DATA.search(page).group(1)), {})
