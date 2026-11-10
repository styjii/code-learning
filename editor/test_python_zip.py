"""
Export / import .zip de l'éditeur Python : ``/editor/api/py-export-zip/`` et ``/editor/api/py-import-zip/``.
"""
import io
import json
import zipfile

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, SimpleTestCase, TestCase, override_settings

from . import python_files
from .tests import make_zip

User = get_user_model()
PASSWORD = "Mot-de-passe-solide-42"
EXPORT_URL = "/editor/api/py-export-zip/"
IMPORT_URL = "/editor/api/py-import-zip/"
JSON = "application/json"


class FilenameRulesTests(SimpleTestCase):
    def test_accepted_names(self):
        for name in ("main.py", "utils.py", "_private.py", "data.json", "notes.txt", "donnees-2024.csv", "README.md"):
            with self.subTest(name=name):
                self.assertIsNone(python_files.filename_error(name))

    def test_refused_names(self):
        refused = {
            "": "vide", "1abc.py": "chiffre", "mon module.py": "espace", "a-b.py": "tiret", "é.py": "accent",
            "dir/mod.py": "dossier", "..\\x.py": "antislash", "../x.py": "remontée", "json.py": "module standard",
            "noext": "sans extension", "x" * 40 + ".py": "trop long", "main.py\n": "retour à la ligne",
        }
        for name, why in refused.items():
            with self.subTest(why=why):
                self.assertIsNotNone(python_files.filename_error(name))


class PythonZipBase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("alice", password=PASSWORD)
        self.client = Client()
        self.client.force_login(self.user)

    def export(self, payload, client=None):
        return (client or self.client).post(EXPORT_URL, json.dumps(payload), content_type=JSON)

    def upload(self, data, name="projet.zip", client=None):
        return (client or self.client).post(IMPORT_URL, {"zip_file": SimpleUploadedFile(name, data)})


class ExportPythonZipTests(PythonZipBase):
    def test_exports_every_file_with_main_first(self):
        files = [{"name": "utils.py", "content": "def f(): ..."}, {"name": "main.py", "content": "import utils"},
                 {"name": "data.json", "content": "{\"é\": 1}"}]
        response = self.export({"files": files})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/zip")
        self.assertIn("python-project.zip", response["Content-Disposition"])
        with zipfile.ZipFile(io.BytesIO(response.content)) as zf:
            self.assertEqual(zf.namelist(), ["main.py", "utils.py", "data.json"])
            self.assertEqual(zf.read("data.json").decode("utf-8"), "{\"é\": 1}")

    def test_invalid_payloads_are_400_never_500(self):
        ok = {"name": "main.py", "content": ""}
        payloads = [
            [], {}, {"files": []}, {"files": "x"}, {"files": [1]}, {"files": [{"name": "main.py"}]},
            {"files": [{"name": "main.py", "content": 5}]},
            {"files": [{"name": "../evil.py", "content": ""}]},
            {"files": [{"name": "json.py", "content": ""}]},
            {"files": [ok, {"name": "MAIN.py", "content": ""}]},
            {"files": [{"name": f"f{i}.py", "content": ""} for i in range(python_files.MAX_FILES + 1)]},
            {"files": [{"name": "main.py", "content": "x" * (python_files.MAX_CHARS + 1)}]},
        ]
        for payload in payloads:
            with self.subTest(payload=str(payload)[:60]):
                response = self.export(payload)
                self.assertEqual(response.status_code, 400)
                self.assertIn("error", response.json())

    def test_malformed_json_is_400(self):
        self.assertEqual(self.client.post(EXPORT_URL, "{pas du json", content_type=JSON).status_code, 400)

    def test_anonymous_is_refused_and_csrf_is_enforced(self):
        self.assertEqual(self.export({"files": [{"name": "main.py", "content": ""}]}, client=Client()).status_code, 401)
        strict = Client(enforce_csrf_checks=True)
        strict.force_login(self.user)
        self.assertEqual(self.export({"files": [{"name": "main.py", "content": ""}]}, client=strict).status_code, 403)


@override_settings(
    EDITOR_ZIP_MAX_ENTRIES=30,
    EDITOR_ZIP_MAX_FILE_BYTES=8 * 1024,
    EDITOR_ZIP_MAX_TOTAL_BYTES=64 * 1024,
)
class ImportPythonZipTests(PythonZipBase):
    def test_valid_archive_is_deserialized_with_main_first(self):
        body = self.upload(make_zip({"utils.py": "X = 1\n", "main.py": "import utils\n", "data.csv": "a,b\n1,2\n"})).json()
        self.assertEqual([f["name"] for f in body["files"]], ["main.py", "utils.py", "data.csv"])
        self.assertEqual(body["files"][0]["content"], "import utils\n")
        self.assertEqual(body["skipped"], [])

    def test_export_then_import_round_trip(self):
        files = [{"name": "main.py", "content": "print('é')\n"}, {"name": "m.py", "content": "Y = 2\n"},
                 {"name": "d.json", "content": "[1, 2]"}]
        archive = self.export({"files": files}).content
        self.assertEqual(self.upload(archive).json()["files"], files)

    def test_single_root_folder_is_stripped(self):
        body = self.upload(make_zip({"projet/main.py": "1", "projet/utils.py": "2"})).json()
        self.assertEqual([f["name"] for f in body["files"]], ["main.py", "utils.py"])

    def test_system_junk_is_ignored_silently(self):
        body = self.upload(make_zip({"main.py": "1", "__MACOSX/._main.py": "x", ".DS_Store": "x", "Thumbs.db": "x"})).json()
        self.assertEqual([f["name"] for f in body["files"]], ["main.py"])
        self.assertEqual(body["skipped"], [])

    def test_invalid_entries_are_skipped_and_reported(self):
        archive = make_zip({
            "main.py": "1", "mon module.py": "x", "json.py": "x", "sub/dir.py": "x", "1abc.py": "x", "ok.py": "2",
        })
        body = self.upload(archive).json()
        self.assertEqual([f["name"] for f in body["files"]], ["main.py", "ok.py"])
        self.assertEqual(len(body["skipped"]), 4)
        self.assertTrue(any("json" in message for message in body["skipped"]))
        self.assertTrue(any("dossiers" in message for message in body["skipped"]))

    def test_case_insensitive_duplicates_keep_the_first(self):
        body = self.upload(make_zip({"main.py": "1", "Notes.txt": "a", "notes.txt": "b"})).json()
        self.assertEqual([(f["name"], f["content"]) for f in body["files"]], [("main.py", "1"), ("Notes.txt", "a")])
        self.assertEqual(len(body["skipped"]), 1)

    def test_non_utf8_and_oversized_text_are_skipped_not_fatal(self):
        archive = make_zip({"main.py": "1", "bin.txt": b"\xff\xfe\x00bad", "big.txt": "a" * (python_files.MAX_CHARS + 1)})
        with override_settings(EDITOR_ZIP_MAX_FILE_BYTES=512 * 1024, EDITOR_ZIP_MAX_TOTAL_BYTES=1024 * 1024):
            body = self.upload(archive).json()
        self.assertEqual([f["name"] for f in body["files"]], ["main.py"])
        self.assertEqual(len(body["skipped"]), 2)

    def test_utf8_bom_is_removed(self):
        body = self.upload(make_zip({"main.py": b"\xef\xbb\xbfprint(1)"})).json()
        self.assertEqual(body["files"][0]["content"], "print(1)")

    def test_file_limit_never_drops_main_py(self):
        files = {f"f{i}.py": "x" for i in range(24)}
        files["main.py"] = "entrée"                                 # dernier dans l'archive
        body = self.upload(make_zip(files)).json()
        names = [f["name"] for f in body["files"]]
        self.assertEqual(len(names), python_files.MAX_FILES)
        self.assertEqual(names[0], "main.py")
        self.assertEqual(len(body["skipped"]), 25 - python_files.MAX_FILES)

    def test_archive_without_any_importable_file_is_400(self):
        response = self.upload(make_zip({"a b.py": "x", "dir/x.py": "y"}))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Aucun fichier importable", response.json()["error"])

    def test_invalid_archives_are_400(self):
        for data in (b"pas un zip", b"PK\x03\x04" + b"\0" * 50, b""):
            with self.subTest(size=len(data)):
                self.assertEqual(self.upload(data).status_code, 400)

    def test_zip_bomb_is_refused_without_decompressing(self):
        data = make_zip({"main.py": "a" * (3 * 1024 * 1024)})
        self.assertLess(len(data), 8 * 1024)
        self.assertEqual(self.upload(data).status_code, 413)

    def test_size_and_entry_limits_are_refused(self):
        self.assertEqual(self.upload(make_zip({"main.py": "a" * (9 * 1024)})).status_code, 413)           # fichier trop gros
        self.assertEqual(self.upload(make_zip({f"f{i}.py": "x" for i in range(31)})).status_code, 413)    # trop d'entrées
        self.assertEqual(self.upload(make_zip({f"f{i}.txt": "a" * 7000 for i in range(10)})).status_code, 413)  # total

    def test_missing_file_is_400_and_anonymous_is_401(self):
        self.assertEqual(self.client.post(IMPORT_URL, {}).status_code, 400)
        self.assertEqual(self.upload(make_zip({"main.py": "1"}), client=Client()).status_code, 401)
