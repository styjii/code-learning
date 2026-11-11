"""
Export / import .zip de l'éditeur codelab-py : ``/editor/api/codelab-py/projects/<id>/export-zip/`` et
``.../import-zip/``. L'archive est construite à partir de la base et l'import y écrit directement.
"""
import io
import zipfile

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, SimpleTestCase, TestCase, override_settings

from . import python_files
from .models import Project
from .test_support import PY, TS, export_url, import_url
from .tests import make_zip

User = get_user_model()
PASSWORD = "Mot-de-passe-solide-42"
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
        self.project = self.make_project("demo", [{"name": "main.py", "content": "print('avant')"}])

    def make_project(self, name, files, owner=None, editor=PY):
        return Project.objects.create(owner=owner or self.user, editor=editor, name=name, data={"files": files})

    def stored_files(self):
        """Les fichiers du projet créé par l'import."""
        return self.imported().latest("id").data["files"]

    def export(self, project=None, client=None, editor=PY):
        return (client or self.client).get(export_url(editor, (project or self.project).pk))

    def upload(self, data, name="projet.zip", client=None):
        return (client or self.client).post(import_url(PY), {"zip_file": SimpleUploadedFile(name, data)})

    def imported(self):
        """Les projets créés par un import (tous sauf celui du départ)."""
        return Project.objects.filter(owner=self.user, editor=PY).exclude(pk=self.project.pk)


class ExportPythonZipTests(PythonZipBase):
    def test_exports_every_file_of_the_database_with_main_first(self):
        files = [{"name": "utils.py", "content": "def f(): ..."}, {"name": "main.py", "content": "import utils"},
                 {"name": "data.json", "content": "{\"é\": 1}"}]
        project = self.make_project("Mon TP", files)
        response = self.export(project)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/zip")
        self.assertIn("Mon%20TP.zip", response["Content-Disposition"])      # nom du projet
        with zipfile.ZipFile(io.BytesIO(response.content)) as zf:
            self.assertEqual(zf.namelist(), ["main.py", "utils.py", "data.json"])
            self.assertEqual(zf.read("data.json").decode("utf-8"), "{\"é\": 1}")

    def test_export_reflects_what_is_saved_in_the_database(self):
        self.project.data = {"files": [{"name": "main.py", "content": "print('enregistré')"}]}
        self.project.save()
        with zipfile.ZipFile(io.BytesIO(self.export().content)) as zf:
            self.assertEqual(zf.read("main.py").decode(), "print('enregistré')")

    def test_invalid_stored_files_are_400_never_500(self):
        ok = {"name": "main.py", "content": ""}
        stored = [
            [], [1], [{"name": "main.py"}], [{"name": "main.py", "content": 5}],
            [{"name": "../evil.py", "content": ""}], [{"name": "json.py", "content": ""}],
            [ok, {"name": "MAIN.py", "content": ""}],
            [{"name": f"f{i}.py", "content": ""} for i in range(python_files.MAX_FILES + 1)],
            [{"name": "main.py", "content": "x" * (python_files.MAX_CHARS + 1)}],
        ]
        for files in stored:
            with self.subTest(files=str(files)[:60]):
                project = self.make_project(f"p{len(Project.objects.all())}", files)
                response = self.export(project)
                self.assertEqual(response.status_code, 400)
                self.assertIn("error", response.json())

    def test_only_the_owner_gets_the_archive_and_only_through_the_right_editor(self):
        bob = User.objects.create_user("bob", password=PASSWORD)
        bob_client = Client()
        bob_client.force_login(bob)
        self.assertEqual(self.export(client=Client()).status_code, 401)
        self.assertEqual(self.export(client=bob_client).status_code, 404)
        self.assertEqual(self.export(editor=TS).status_code, 404)
        self.assertEqual(self.client.get(export_url(PY, 999999)).status_code, 404)

    def test_csrf_is_enforced_on_import(self):
        strict = Client(enforce_csrf_checks=True)
        strict.force_login(self.user)
        archive = SimpleUploadedFile("p.zip", make_zip({"main.py": "1"}))
        self.assertEqual(strict.post(import_url(PY), {"zip_file": archive}).status_code, 403)


@override_settings(
    EDITOR_ZIP_MAX_ENTRIES=30,
    EDITOR_ZIP_MAX_FILE_BYTES=8 * 1024,
    EDITOR_ZIP_MAX_TOTAL_BYTES=64 * 1024,
)
class ImportPythonZipTests(PythonZipBase):
    def test_valid_archive_is_stored_with_main_first(self):
        body = self.upload(make_zip({"utils.py": "X = 1\n", "main.py": "import utils\n", "data.csv": "a,b\n1,2\n"})).json()
        self.assertEqual([f["name"] for f in body["files"]], ["main.py", "utils.py", "data.csv"])
        self.assertEqual(body["files"][0]["content"], "import utils\n")
        self.assertEqual(body["skipped"], [])

    def test_export_then_import_round_trip(self):
        files = [{"name": "main.py", "content": "print('é')\n"}, {"name": "m.py", "content": "Y = 2\n"},
                 {"name": "d.json", "content": "[1, 2]"}]
        source = self.make_project("source", files)
        archive = self.export(source).content
        self.assertEqual(self.upload(archive).json()["files"], files)
        self.assertEqual(self.stored_files(), files)             # écrit en base, dans un nouveau projet

    def test_import_creates_a_new_project_in_the_database_and_touches_no_other(self):
        other = self.make_project("autre", [{"name": "main.py", "content": "intact"}])
        body = self.upload(make_zip({"main.py": "nouveau\n", "utils.py": "X = 1\n"}), "Mon TP.zip").json()
        self.assertEqual(body["name"], "Mon TP")                                 # nom du fichier
        self.assertNotIn(body["id"], (self.project.pk, other.pk))
        self.assertEqual([f["name"] for f in self.stored_files()], ["main.py", "utils.py"])
        for project, content in ((self.project, "print('avant')"), (other, "intact")):
            project.refresh_from_db()
            self.assertEqual(project.data["files"][0]["content"], content)

    def test_a_refused_archive_creates_nothing(self):
        for data in (b"pas un zip", make_zip({"a b.py": "x"}), make_zip({"main.py": "a" * (9 * 1024)})):
            self.assertIn(self.upload(data).status_code, (400, 413))
        self.assertFalse(self.imported().exists())

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
        self.assertEqual(self.client.post(import_url(PY), {}).status_code, 400)
        self.assertEqual(self.upload(make_zip({"main.py": "1"}), client=Client()).status_code, 401)
