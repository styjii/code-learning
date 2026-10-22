import io
import json
import struct
import zipfile
from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings

from .models import EditorPreferences
from .monaco_config import DEFAULT_PREFERENCES, FIXED_OPTIONS, effective_options

User = get_user_model()
PASSWORD = "Mot-de-passe-solide-42"
SAVE_URL = "/editor/api/save-monaco-config/"
LOAD_URL = "/editor/api/load-monaco-config/"
IMPORT_URL = "/editor/api/import-zip/"


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
    """L'import refuse les archives piégées avant de les décompresser."""

    def setUp(self):
        self.user = User.objects.create_user("alice", password=PASSWORD)
        self.client = Client()
        self.client.force_login(self.user)

    def upload(self, data, name="project.zip"):
        return self.client.post(IMPORT_URL, {"zip_file": SimpleUploadedFile(name, data)})

    def test_valid_archive_is_imported(self):
        data = make_zip({
            "index.html": "<html><body><p>Salut é</p><script>evil()</script></body></html>",
            "style.css": "p { color: red; }",
            "script.js": "console.log(1)",
        })
        body = self.upload(data).json()
        self.assertEqual(body["html"], "<p>Salut é</p>")        # <script> retiré, comme avant
        self.assertEqual(body["css"], "p { color: red; }")
        self.assertEqual(body["js"], "console.log(1)")
        self.assertEqual(body["project"], "project")

    def test_archive_with_project_folder_is_imported(self):
        data = make_zip({"project/index.html": "<body>x</body>", "project/style.css": "a{}", "project/script.js": "1"})
        body = self.upload(data).json()
        self.assertEqual((body["html"], body["css"], body["js"]), ("x", "a{}", "1"))

    def test_missing_files_give_empty_strings(self):
        body = self.upload(make_zip({"readme.txt": "rien"})).json()
        self.assertEqual((body["html"], body["css"], body["js"]), ("", "", ""))

    def test_zip_bomb_is_refused_without_decompressing(self):
        data = make_zip({"index.html": "<body>" + "a" * (3 * 1024 * 1024) + "</body>"})
        self.assertLess(len(data), 8 * 1024)                    # petit à l'envoi, énorme une fois décompressé
        response = self.upload(data)
        self.assertEqual(response.status_code, 413)
        self.assertIn("error", response.json())

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

    def test_invalid_archives_are_400_without_internal_details(self):
        for data in (b"pas un zip", b"PK\x03\x04" + b"\0" * 50, b""):
            with self.subTest(size=len(data)):
                response = self.upload(data) if data else self.client.post(IMPORT_URL, {})
                self.assertEqual(response.status_code, 400)
                self.assertNotIn("details", response.json())

    def test_non_utf8_content_is_400(self):
        self.assertEqual(self.upload(make_zip({"style.css": b"\xff\xfe\x00bad"})).status_code, 400)

    def test_corrupted_data_is_400(self):
        data = bytearray(make_zip({"style.css": "body { margin: 0 }" * 20}, zipfile.ZIP_STORED))
        data[data.index(b"body") + 2] ^= 0xFF                    # contenu altéré : CRC invalide
        self.assertEqual(self.upload(bytes(data)).status_code, 400)

    def test_anonymous_still_gets_403(self):
        self.assertEqual(Client().post(IMPORT_URL, {}).status_code, 403)
