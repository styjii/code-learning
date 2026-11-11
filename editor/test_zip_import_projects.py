"""
Import .zip = création d'un nouveau projet (``POST /editor/api/<editor>/projects/import-zip/``), pour les trois éditeurs :

    - le nom par défaut est celui du fichier ;
    - un doublon (même utilisateur, même éditeur, même nom) n'écrit rien et renvoie un 409 : écraser ou renommer ;
    - un nom invalide ou trop long donne le nom de secours ``projet-import-{id}`` ;
    - le projet ouvert n'est jamais modifié.
"""
from unittest import mock

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import IntegrityError
from django.db.models.query import QuerySet
from django.test import Client, TestCase

from . import editors, project_names
from .models import Project
from .test_support import JS, PY, TS, import_url
from .tests import make_zip

User = get_user_model()
PASSWORD = "Mot-de-passe-solide-42"

ARCHIVES = {
    JS: {"index.html": "<body><p>js</p></body>", "style.css": "p{}", "script.js": "1"},
    TS: {"index.html": "<body><p>ts</p></body>", "script.ts": "let a: number = 1", "tsconfig.json": "{}"},
    PY: {"main.py": "print('py')\n", "utils.py": "X = 1\n"},
}


class ImportAsNewProjectTests(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user("alice", password=PASSWORD)
        self.client = Client()
        self.client.force_login(self.alice)

    def upload(self, editor, filename="Mon TP.zip", client=None, files=None, **fields):
        archive = SimpleUploadedFile(filename, make_zip(files or ARCHIVES[editor]))
        return (client or self.client).post(import_url(editor), {"zip_file": archive, **fields})

    def projects(self, editor):
        return Project.objects.filter(owner=self.alice, editor=editor)

    # --- nom par défaut -------------------------------------------------------------------------------------
    def test_each_editor_creates_a_project_named_after_the_file(self):
        for editor in editors.EDITORS:
            with self.subTest(editor=editor):
                response = self.upload(editor)
                self.assertEqual(response.status_code, 201)
                body = response.json()
                self.assertEqual((body["name"], body["created"], body["renamed"]), ("Mon TP", True, False))
                project = self.projects(editor).get(name="Mon TP")
                self.assertEqual(project.pk, body["id"])
                self.assertEqual(set(project.data), set(editors.get(editor).defaults()))

    def test_content_is_written_in_the_database_for_each_editor(self):
        self.assertEqual(self.projects(JS).get(pk=self.upload(JS).json()["id"]).data["js"], "1")
        ts = self.projects(TS).get(pk=self.upload(TS).json()["id"]).data
        self.assertEqual(ts["ts"], "let a: number = 1")
        self.assertIn("strict", ts["compiler_options"])
        py = self.projects(PY).get(pk=self.upload(PY).json()["id"]).data
        self.assertEqual([f["name"] for f in py["files"]], ["main.py", "utils.py"])

    def test_the_response_has_the_same_fields_as_the_projects_api(self):
        for editor, keys in ((JS, {"html", "css", "js"}), (TS, {"html", "css", "ts", "compiler_options"}), (PY, {"files"})):
            with self.subTest(editor=editor):
                body = self.upload(editor, f"p-{editor}.zip").json()
                self.assertEqual(set(body) - {"id", "name", "created", "renamed", "skipped"}, keys)

    def test_no_file_is_400(self):
        self.assertEqual(self.client.post(import_url(JS), {}).status_code, 400)

    def test_unknown_editor_and_anonymous(self):
        self.assertEqual(self.client.post("/editor/api/python/projects/import-zip/", {}).status_code, 404)
        self.assertEqual(Client().post(import_url(PY), {}).status_code, 401)

    # --- doublons -------------------------------------------------------------------------------------------
    def test_a_duplicate_writes_nothing_and_asks_what_to_do(self):
        for editor in editors.EDITORS:
            with self.subTest(editor=editor):
                self.upload(editor)
                before = list(self.projects(editor).values_list("pk", "data"))
                response = self.upload(editor)
                self.assertEqual(response.status_code, 409)
                body = response.json()
                self.assertEqual(body["conflict"]["name"], "Mon TP")
                self.assertEqual(body["conflict"]["id"], self.projects(editor).get().pk)
                self.assertIn("Mon TP", body["error"])
                self.assertEqual(list(self.projects(editor).values_list("pk", "data")), before)

    def test_the_same_name_in_another_editor_or_for_another_user_is_not_a_duplicate(self):
        bob = User.objects.create_user("bob", password=PASSWORD)
        Project.objects.create(owner=bob, editor=JS, name="Mon TP")
        Project.objects.create(owner=self.alice, editor=TS, name="Mon TP")
        self.assertEqual(self.upload(JS).status_code, 201)

    def test_overwrite_replaces_the_content_of_the_existing_project(self):
        for editor in editors.EDITORS:
            with self.subTest(editor=editor):
                first = self.upload(editor, files=ARCHIVES[editor]).json()
                other = Project.objects.create(owner=self.alice, editor=editor, name="autre")
                new_files = {JS: {"index.html": "<body>v2</body>"}, TS: {"script.ts": "v2"}, PY: {"main.py": "v2"}}[editor]
                response = self.upload(editor, files=new_files, on_conflict="overwrite")
                self.assertEqual(response.status_code, 200)
                body = response.json()
                self.assertEqual((body["id"], body["name"], body["created"]), (first["id"], "Mon TP", False))
                self.assertEqual(self.projects(editor).filter(name="Mon TP").count(), 1)
                self.assertEqual(self.projects(editor).count(), 2)           # aucun projet en plus
                stored = self.projects(editor).get(name="Mon TP").data
                self.assertNotEqual(stored, editors.get(editor).merge({}, {}))
                self.assertIn("v2", str(stored))
                self.assertNotIn("print('py')", str(stored))                  # l'ancien contenu a disparu
                other.refresh_from_db()
                self.assertEqual(other.data, {})                              # les autres projets ne bougent pas

    def test_overwrite_also_resets_what_the_new_archive_does_not_contain(self):
        self.upload(JS, files={"index.html": "<body>a</body>", "style.css": "a{}", "script.js": "1"})
        self.upload(JS, files={"index.html": "<body>b</body>"}, on_conflict="overwrite")
        self.assertEqual(self.projects(JS).get().data, {"html": "b", "css": "", "js": ""})

    def test_overwrite_without_a_duplicate_just_creates_the_project(self):
        response = self.upload(JS, on_conflict="overwrite")
        self.assertEqual((response.status_code, response.json()["created"]), (201, True))

    def test_renaming_creates_a_second_project_and_keeps_the_first(self):
        self.upload(JS)
        response = self.upload(JS, name="Mon TP v2")
        self.assertEqual((response.status_code, response.json()["name"]), (201, "Mon TP v2"))
        self.assertEqual(sorted(self.projects(JS).values_list("name", flat=True)), ["Mon TP", "Mon TP v2"])

    def test_a_chosen_name_that_is_also_taken_is_a_new_conflict(self):
        self.upload(JS)
        self.upload(JS, "autre.zip")
        response = self.upload(JS, name="autre")
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json()["conflict"]["name"], "autre")

    def test_overwrite_targets_the_chosen_name(self):
        self.upload(JS, "autre.zip")
        response = self.upload(JS, files={"index.html": "<body>x</body>"}, name="autre", on_conflict="overwrite")
        self.assertEqual((response.status_code, response.json()["name"]), (200, "autre"))
        self.assertEqual(self.projects(JS).count(), 1)

    def test_a_chosen_name_is_trimmed(self):
        self.assertEqual(self.upload(JS, name="  Nom choisi  ").json()["name"], "Nom choisi")

    def test_invalid_chosen_names_are_400_and_nothing_is_written(self):
        for name in ("   ", "x" * 101, "a\x00b", "a\nb"):
            with self.subTest(name=repr(name)[:30]):
                response = self.upload(JS, name=name)
                self.assertEqual(response.status_code, 400)
                self.assertIn("error", response.json())
        self.assertFalse(self.projects(JS).exists())

    def test_a_name_of_exactly_the_maximum_length_is_kept(self):
        name = "n" * project_names.MAX_NAME_LENGTH
        self.assertEqual(self.upload(JS, f"{name}.zip").json()["name"], name)

    def test_a_duplicate_detected_only_at_write_time_is_a_409_not_a_500(self):
        existing = Project.objects.create(owner=self.alice, editor=JS, name="Mon TP")
        with mock.patch.object(QuerySet, "first", side_effect=[None, existing]), \
                mock.patch.object(Project.objects, "create", side_effect=IntegrityError):
            response = self.upload(JS)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json()["conflict"]["id"], existing.pk)

    # --- nom de secours -------------------------------------------------------------------------------------
    def test_an_unusable_file_name_gives_projet_import_followed_by_the_project_id(self):
        for filename in ("x" * 101 + ".zip", ".zip", "   .zip", "x" * 5000 + ".zip"):      # Django retire déjà les caractères de contrôle
            with self.subTest(filename=repr(filename)[:25]):
                response = self.upload(JS, filename)
                self.assertEqual(response.status_code, 201)
                body = response.json()
                self.assertEqual(body["name"], f"projet-import-{body['id']}")
                self.assertTrue(body["renamed"])
                self.assertEqual(Project.objects.get(pk=body["id"]).name, body["name"])

    def test_fallback_names_are_unique_per_project(self):
        names = {self.upload(JS, ".zip").json()["name"] for _ in range(3)}
        self.assertEqual(len(names), 3)

    def test_fallback_name_is_made_unique_if_it_is_already_taken(self):
        next_pk = Project.objects.order_by("-pk").values_list("pk", flat=True).first() or 0
        Project.objects.create(owner=self.alice, editor=JS, name=f"projet-import-{next_pk + 2}")   # pk next_pk + 1
        body = self.upload(JS, ".zip").json()                                                         # pk next_pk + 2
        self.assertEqual(body["id"], next_pk + 2)
        self.assertEqual(body["name"], f"projet-import-{next_pk + 2}-2")

    def test_the_fallback_name_never_overwrites_anything(self):
        existing = self.upload(JS, ".zip").json()
        response = self.upload(JS, ".zip", on_conflict="overwrite")
        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.json()["id"], existing["id"])

    def test_the_fallback_name_may_be_the_name_of_a_project_of_another_editor(self):
        body = self.upload(TS, ".zip").json()
        Project.objects.create(owner=self.alice, editor=JS, name=body["name"])
        self.assertEqual(self.upload(JS, ".zip").status_code, 201)


class ProjectNameHelpersTests(TestCase):
    def test_clean_name(self):
        self.assertEqual(project_names.clean_name("  Mon projet  "), "Mon projet")
        for bad in (None, 5, "", "   ", "x" * 101, "a\tb", "a\x7fb"):
            self.assertIsNone(project_names.clean_name(bad), repr(bad))

    def test_name_from_filename(self):
        self.assertEqual(project_names.name_from_filename("Rapport final.zip"), "Rapport final")
        self.assertEqual(project_names.name_from_filename("C:\\Users\\a\\TP.ZIP"), "TP")
        self.assertEqual(project_names.name_from_filename("dir/TP.zip"), "TP")
        self.assertIsNone(project_names.name_from_filename(".zip"))
        self.assertIsNone(project_names.name_from_filename(None))
        self.assertIsNone(project_names.name_from_filename("y" * 200 + ".zip"))
