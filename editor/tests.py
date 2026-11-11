import io
import json
import struct
import zipfile
from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from django.urls import reverse

from .models import EditorPreferences, Project
from .monaco_config import DEFAULT_PREFERENCES, FIXED_OPTIONS, effective_options
from .test_support import JS, PY, import_url, page_url

User = get_user_model()
PASSWORD = "Mot-de-passe-solide-42"
SAVE_URL = "/editor/api/save-monaco-config/"
LOAD_URL = "/editor/api/load-monaco-config/"


def make_zip(files, compression=zipfile.ZIP_DEFLATED):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression) as zf:
        for name, content in files.items():
            zf.writestr(name, content)
    return buffer.getvalue()


class MonacoConfigTests(TestCase):
    """La configuration Monaco est propre à chaque utilisateur et limitée à une liste blanche de clés."""

    def setUp(self):
        self.alice = User.objects.create_user("alice", password=PASSWORD)
        self.bob = User.objects.create_user("bob", password=PASSWORD)
        self.alice_client, self.bob_client = Client(), Client()
        self.alice_client.force_login(self.alice)
        self.bob_client.force_login(self.bob)

    def save(self, client, payload):
        return client.post(SAVE_URL, json.dumps(payload), content_type="application/json")

    def test_alice_cannot_lock_the_editor_for_bob(self):
        """Scénario de la faille : {"readOnly": true, "value": "HACK"}."""
        response = self.save(self.alice_client, {"readOnly": True, "value": "HACK"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(set(response.json()["details"]), {"readOnly", "value"})

        for client in (self.alice_client, self.bob_client):
            options = client.get(LOAD_URL).json()
            self.assertNotIn("readOnly", options)
            self.assertNotIn("value", options)
        self.assertFalse(EditorPreferences.objects.exists())

    def test_one_forbidden_key_rejects_the_whole_request(self):
        response = self.save(self.alice_client, {"wordWrap": "on", "readOnly": True})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.alice_client.get(LOAD_URL).json()["wordWrap"], DEFAULT_PREFERENCES["wordWrap"])

    def test_theme_and_fixed_options_are_not_user_settable(self):
        for key, value in [("theme", "vs"), ("automaticLayout", False), ("contextmenu", True),
                           ("scrollbar", {"verticalScrollbarSize": 100}), ("__proto__", {})]:
            with self.subTest(key=key):
                self.assertEqual(self.save(self.alice_client, {key: value}).status_code, 400)

    def test_values_are_type_and_range_checked(self):
        invalid = [
            {"wordWrap": "sideways"}, {"wordWrap": True}, {"tabSize": "4"}, {"tabSize": 0}, {"tabSize": 999},
            {"tabSize": True}, {"tabSize": 2.5}, {"insertSpaces": "yes"}, {"insertSpaces": 1},
            {"minimap": True}, {"minimap": {"enabled": "x"}}, {"minimap": {"enabled": True, "side": "left"}},
            {"lineNumbers": ["on"]}, {"formatOnType": None},
        ]
        for payload in invalid:
            with self.subTest(payload=payload):
                self.assertEqual(self.save(self.alice_client, payload).status_code, 400)

    def test_body_must_be_a_json_object(self):
        for body in ([], [{"wordWrap": "on"}], "wordWrap", 3, None):
            with self.subTest(body=body):
                self.assertEqual(self.save(self.alice_client, body).status_code, 400)

    def test_valid_preferences_are_per_user_and_merged(self):
        self.assertEqual(self.save(self.alice_client, {"wordWrap": "on"}).status_code, 200)
        self.assertEqual(self.save(self.alice_client, {"tabSize": 2, "minimap": {"enabled": False}}).status_code, 200)

        alice_options = self.alice_client.get(LOAD_URL).json()
        self.assertEqual(alice_options["wordWrap"], "on")           # conservé après le 2e enregistrement
        self.assertEqual(alice_options["tabSize"], 2)
        self.assertEqual(alice_options["minimap"], {"enabled": False})

        bob_options = self.bob_client.get(LOAD_URL).json()          # Bob garde les valeurs par défaut
        self.assertEqual(bob_options["wordWrap"], DEFAULT_PREFERENCES["wordWrap"])
        self.assertEqual(bob_options["tabSize"], DEFAULT_PREFERENCES["tabSize"])
        self.assertFalse(EditorPreferences.objects.filter(user=self.bob).exists())

    def test_load_returns_defaults_and_fixed_options(self):
        options = self.bob_client.get(LOAD_URL).json()
        self.assertEqual(options, effective_options())
        for key, value in FIXED_OPTIONS.items():
            self.assertEqual(options[key], value)

    def test_load_ignores_invalid_data_already_in_database(self):
        EditorPreferences.objects.create(user=self.alice, monaco={
            "readOnly": True, "value": "HACK", "tabSize": 99, "wordWrap": "on"})
        options = self.alice_client.get(LOAD_URL).json()
        self.assertNotIn("readOnly", options)
        self.assertNotIn("value", options)
        self.assertEqual(options["tabSize"], DEFAULT_PREFERENCES["tabSize"])
        self.assertEqual(options["wordWrap"], "on")

    def test_fixed_options_win_over_stored_values(self):
        EditorPreferences.objects.create(user=self.alice, monaco={"contextmenu": True, "automaticLayout": False})
        options = self.alice_client.get(LOAD_URL).json()
        self.assertIs(options["contextmenu"], False)
        self.assertIs(options["automaticLayout"], True)

    def test_nothing_is_written_to_the_source_tree(self):
        self.save(self.alice_client, {"wordWrap": "on"})
        self.assertFalse((Path(settings.BASE_DIR) / "editor" / "config").exists())

    def test_form_encoded_body_is_refused(self):
        self.assertEqual(self.alice_client.post(SAVE_URL, {"wordWrap": "on"}).status_code, 415)


@override_settings(
    EDITOR_ZIP_MAX_UPLOAD_BYTES=64 * 1024,
    EDITOR_ZIP_MAX_ENTRIES=10,
    EDITOR_ZIP_MAX_FILE_BYTES=8 * 1024,
    EDITOR_ZIP_MAX_TOTAL_BYTES=16 * 1024,
)
class ImportZipLimitsTests(TestCase):
    """
    L'import crée un **nouveau projet** en base (``POST /editor/api/codelab-js/projects/import-zip/``) et refuse les
    archives piégées avant de les décompresser : une archive refusée ne laisse rien en base.
    """

    def setUp(self):
        self.user = User.objects.create_user("alice", password=PASSWORD)
        self.client = Client()
        self.client.force_login(self.user)
        self.project = Project.objects.create(
            owner=self.user, editor=JS, name="demo", data={"html": "<p>avant</p>", "css": "a{}", "js": "avant()"})
        self.import_url = import_url(JS)

    def upload(self, data, name="project.zip", **fields):
        return self.client.post(self.import_url, {"zip_file": SimpleUploadedFile(name, data), **fields})

    def imported(self):
        """Les projets créés par l'import (tous sauf celui du départ)."""
        return Project.objects.filter(owner=self.user, editor=JS).exclude(pk=self.project.pk)

    def assertUntouched(self):
        self.project.refresh_from_db()
        self.assertEqual(self.project.data, {"html": "<p>avant</p>", "css": "a{}", "js": "avant()"})
        self.assertFalse(self.imported().exists())

    def test_valid_archive_creates_a_new_project_named_after_the_file(self):
        data = make_zip({
            "index.html": "<html><body><p>Salut é</p><script>evil()</script></body></html>",
            "style.css": "p { color: red; }",
            "script.js": "console.log(1)",
        })
        response = self.upload(data, "Mon TP.zip")
        self.assertEqual(response.status_code, 201)
        body = response.json()
        self.assertEqual(body["html"], "<p>Salut é</p>")        # <script> retiré, comme avant
        self.assertEqual(body["css"], "p { color: red; }")
        self.assertEqual(body["js"], "console.log(1)")
        self.assertEqual((body["name"], body["created"], body["renamed"]), ("Mon TP", True, False))
        project = self.imported().get()
        self.assertEqual(project.pk, body["id"])
        self.assertEqual(project.name, "Mon TP")                 # nom du fichier sans « .zip »
        self.assertEqual(project.data, {"html": "<p>Salut é</p>", "css": "p { color: red; }", "js": "console.log(1)"})

    def test_the_open_project_is_never_modified(self):
        self.upload(make_zip({"index.html": "<body>nouveau</body>", "script.js": "1"}), "autre.zip")
        self.project.refresh_from_db()
        self.assertEqual(self.project.data, {"html": "<p>avant</p>", "css": "a{}", "js": "avant()"})
        self.assertEqual(self.imported().get().data["html"], "nouveau")

    def test_the_extension_is_removed_whatever_its_case(self):
        for filename, expected in (("a.ZIP", "a"), ("b.Zip", "b"), ("c.tar.zip", "c.tar"), ("d", "d"), ("  e  .zip", "e")):
            with self.subTest(filename=filename):
                self.assertEqual(self.upload(make_zip({"index.html": "<body></body>"}), filename).json()["name"], expected)

    def test_a_refused_archive_leaves_nothing_in_the_database(self):
        for data in (b"pas un zip", make_zip({"style.css": "a" * (9 * 1024)})):
            self.assertIn(self.upload(data).status_code, (400, 413))
        self.assertUntouched()

    def test_archive_with_project_folder_is_imported(self):
        data = make_zip({"project/index.html": "<body>x</body>", "project/style.css": "a{}", "project/script.js": "1"})
        body = self.upload(data, "project.zip").json()
        self.assertEqual((body["html"], body["css"], body["js"]), ("x", "a{}", "1"))

    def test_missing_files_give_empty_strings(self):
        body = self.upload(make_zip({"readme.txt": "rien"})).json()
        self.assertEqual((body["html"], body["css"], body["js"]), ("", "", ""))
        self.assertEqual(self.imported().get().data, {"html": "", "css": "", "js": ""})

    def test_zip_bomb_is_refused_without_decompressing(self):
        data = make_zip({"index.html": "<body>" + "a" * (3 * 1024 * 1024) + "</body>"})
        self.assertLess(len(data), 8 * 1024)                    # petit à l'envoi, énorme une fois décompressé
        response = self.upload(data)
        self.assertEqual(response.status_code, 413)
        self.assertIn("error", response.json())
        self.assertUntouched()

    def test_total_declared_size_is_capped(self):
        files = {f"data{i}.bin": "a" * 5000 for i in range(4)}   # 20 Ko > 16 Ko, aucun fichier lu pourtant
        self.assertEqual(self.upload(make_zip(files)).status_code, 413)

    def test_single_file_size_is_capped(self):
        data = make_zip({"style.css": "a" * (9 * 1024)})         # 9 Ko > 8 Ko (total 16 Ko non dépassé)
        self.assertEqual(self.upload(data).status_code, 413)

    def test_too_many_entries_are_refused(self):
        data = make_zip({f"f{i}.txt": "x" for i in range(11)})
        self.assertEqual(self.upload(data).status_code, 413)

    def test_upload_larger_than_limit_is_refused_before_parsing(self):
        data = make_zip({"index.html": "x"}, zipfile.ZIP_STORED) + b"\0" * (200 * 1024)
        self.assertEqual(self.upload(data).status_code, 413)     # Content-Length > limite + marge

    def test_upload_slightly_over_limit_is_refused(self):
        with override_settings(EDITOR_ZIP_MAX_UPLOAD_BYTES=1024):
            data = make_zip({"index.html": "x"}, zipfile.ZIP_STORED) + b"\0" * 2000
            self.assertEqual(self.upload(data).status_code, 413)  # sous la marge multipart, rattrapé dans post()

    def test_falsified_header_size_cannot_bypass_the_cap(self):
        data = bytearray(make_zip({"style.css": "a" * (20 * 1024)}))   # 20 Ko réels > 8 Ko autorisés
        central = data.index(b"PK\x01\x02")
        data[central + 24:central + 28] = struct.pack("<I", 100)        # le répertoire central annonce 100 octets
        info = zipfile.ZipFile(io.BytesIO(bytes(data))).infolist()[0]
        self.assertEqual(info.file_size, 100)                          # la falsification est bien en place
        response = self.upload(bytes(data))
        self.assertIn(response.status_code, (400, 413))                # jamais 200 avec 20 Ko de contenu
        self.assertNotIn("css", response.json())
        self.assertUntouched()

    def test_invalid_archives_are_400_without_internal_details(self):
        for data in (b"pas un zip", b"PK\x03\x04" + b"\0" * 50, b""):
            with self.subTest(size=len(data)):
                response = self.upload(data) if data else self.client.post(self.import_url, {})
                self.assertEqual(response.status_code, 400)
                self.assertNotIn("details", response.json())

    def test_non_utf8_content_is_400(self):
        self.assertEqual(self.upload(make_zip({"style.css": b"\xff\xfe\x00bad"})).status_code, 400)

    def test_corrupted_data_is_400(self):
        data = bytearray(make_zip({"style.css": "body { margin: 0 }" * 20}, zipfile.ZIP_STORED))
        data[data.index(b"body") + 2] ^= 0xFF                    # contenu altéré : CRC invalide
        self.assertEqual(self.upload(bytes(data)).status_code, 400)

    def test_anonymous_gets_401(self):
        self.assertEqual(Client().post(self.import_url, {}).status_code, 401)


class PythonEditorPageTests(TestCase):
    """Page de l'éditeur Python : protégée par la connexion, et reliée aux autres pages."""

    def setUp(self):
        self.user = User.objects.create_user("alice", password=PASSWORD)
        self.client = Client()

    def test_page_requires_login(self):
        url = page_url(PY)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response["Location"])
        self.assertIn(f"next={url}", response["Location"])

    def test_page_contains_the_editor_and_runtime_settings(self):
        self.client.force_login(self.user)
        response = self.client.get(page_url(PY))
        self.assertEqual(response.status_code, 200)
        html = response.content.decode()
        for fragment in ('id="py-editor"', 'id="py-tabs"', 'id="console"', 'id="run-code"', 'id="py-stdin"',
                         "data-pyodide=", "data-monaco=", "editor/js/python/main.js",
                         # modale « Projets » : mêmes éléments que dans les éditeurs Web et TypeScript
                         'id="current-project"', 'data-target="#project-controls"', 'id="project-controls"',
                         'id="project-select"', 'id="create-btn"', 'id="delete-btn"', 'id="rename-btn"',
                         'id="project-current-name"'):
            self.assertIn(fragment, html)

    def test_editors_and_home_link_to_each_other(self):
        self.client.force_login(self.user)
        python_url = page_url(PY)
        web_url = page_url(JS)
        self.assertContains(self.client.get(web_url), f'href="{python_url}"')
        self.assertContains(self.client.get(python_url), f'href="{web_url}"')
        self.assertContains(self.client.get(reverse("index")), f'href="{python_url}"')

    def test_static_files_used_by_the_page_exist(self):
        """Les modules chargés par la page (et leurs dépendances inter-applications) sont bien servis."""
        from django.contrib.staticfiles import finders

        for path in (
            "editor/js/python/main.js", "editor/js/python/PythonEditorApp.js", "editor/js/python/FileStore.js",
            "editor/js/python/PythonProjectManager.js", "editor/js/projects/ProjectRenameBinder.js",
            "editor/js/projects/api.js", "editor/js/projects/ZipImporter.js",
            "editor/js/console/ConsoleRenderer.js", "editor/css/python.css",
            "language/js/runner/MonacoLoader.js", "language/js/runner/PythonRunner.js",
            "language/js/runner/python.worker.js", "vendor/pyodide/pyodide.mjs",
        ):
            self.assertIsNotNone(finders.find(path), path)
