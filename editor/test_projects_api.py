"""
Tests de l'API ``/editor/api/projects/`` (et ``/editor/api/ts-projects/`` et ``/editor/api/py-projects/``, qui
partagent le même code) :
création, isolation par utilisateur, suppression, gestion des erreurs et authentification obligatoire.
"""
import json
from unittest import mock

from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from . import python_files
from .models import Project, PythonProject, TypeScriptProject
from .serializers import ProjectSerializer, PythonProjectSerializer, TypeScriptProjectSerializer

User = get_user_model()
PASSWORD = "Mot-de-passe-solide-42"
JSON = "application/json"


def logged_in_client(user):
    # raise_request_exception=False : une exception non gérée devient un vrai 500, comme en production.
    client = Client(raise_request_exception=False)
    client.force_login(user)
    return client


class ProjectsApiTestCase(TestCase):
    """
    Base : deux utilisateurs et un projet d'Alice (``self.project``). Les groupes de tests ci-dessous sont des
    mixins, assemblés pour les éditeurs Web, TypeScript puis Python (mêmes garanties, autre modèle).
    """

    url = "/editor/api/projects/"
    model = Project
    serializer = ProjectSerializer
    payload = {"name": "demo", "html": "<p>a</p>", "css": "p{}", "js": "1"}   # projet existant d'Alice
    new = {"name": "nouveau", "html": "<p>b</p>", "css": "", "js": ""}        # à créer dans les tests
    content_fields = ("html", "css")                                          # champs de contenu à conserver au renommage
    invalid_content = {"name": "ok", "html": None}                            # contenu refusé par le serializer

    def setUp(self):
        self.alice = User.objects.create_user("alice", password=PASSWORD)
        self.bob = User.objects.create_user("bob", password=PASSWORD)
        self.alice_client = logged_in_client(self.alice)
        self.bob_client = logged_in_client(self.bob)
        self.project = self.model.objects.create(owner=self.alice, **self.payload)

    def post(self, client, data=None):
        return client.post(self.url, json.dumps(self.new if data is None else data), content_type=JSON)

    def detail(self, pk):
        return f"{self.url}{pk}/"


class CreateProjectTests:
    def test_create_returns_201_and_binds_the_project_to_the_authenticated_user(self):
        response = self.post(self.alice_client)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.model.objects.get(pk=response.json()["id"]).owner, self.alice)

    def test_owner_sent_by_the_client_is_ignored(self):
        response = self.post(self.alice_client, {**self.new, "owner": self.bob.pk, "owner_id": self.bob.pk})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.model.objects.get(pk=response.json()["id"]).owner, self.alice)
        self.assertFalse(self.model.objects.filter(owner=self.bob).exists())

    def test_minimal_payload_with_only_a_name_is_accepted(self):
        self.assertEqual(self.post(self.alice_client, {"name": "vide"}).status_code, 201)

    def test_duplicate_name_for_same_user_is_400(self):
        self.assertEqual(self.post(self.alice_client).status_code, 201)
        response = self.post(self.alice_client)
        self.assertEqual(response.status_code, 400)
        self.assertIn("name", response.json())

    def test_name_of_an_existing_project_is_400(self):
        self.assertEqual(self.post(self.alice_client, self.payload).status_code, 400)

    def test_same_name_is_allowed_for_two_different_users(self):
        self.assertEqual(self.post(self.alice_client).status_code, 201)
        self.assertEqual(self.post(self.bob_client).status_code, 201)
        self.assertEqual(self.model.objects.filter(name=self.new["name"]).count(), 2)

    def test_simultaneous_duplicate_is_400_not_500(self):
        """
        Deux requêtes passent ensemble le contrôle ``validate_name`` ; la seconde échoue sur la contrainte
        unique en base. Cela donnait un ``IntegrityError`` non géré, donc un 500.
        """
        with mock.patch.object(self.serializer, "validate_name", lambda _self, value: value):
            response = self.post(self.alice_client, self.payload)   # même nom que le projet existant
        self.assertEqual(response.status_code, 400)
        self.assertIn("name", response.json())
        self.assertEqual(self.model.objects.filter(owner=self.alice).count(), 1)

    def test_invalid_payloads_are_400_never_500(self):
        invalid = [
            {}, {"name": ""}, {"name": "   "}, {"name": None}, {"name": "x" * 101},
            self.invalid_content, {"name": ["liste"]}, {"name": {"a": 1}},
        ]
        for data in invalid:
            with self.subTest(data=data):
                self.assertEqual(self.post(self.alice_client, data).status_code, 400)
        self.assertEqual(self.model.objects.count(), 1)   # seul le projet de départ existe

    def test_malformed_json_is_400(self):
        response = self.alice_client.post(self.url, "{pas du json", content_type=JSON)
        self.assertEqual(response.status_code, 400)

    def test_only_json_is_accepted(self):
        response = self.alice_client.post(self.url, {"name": "form"})  # multipart
        self.assertEqual(response.status_code, 415)
        self.assertFalse(self.model.objects.filter(name="form").exists())

    def test_csrf_is_enforced(self):
        strict = Client(enforce_csrf_checks=True)
        strict.force_login(self.alice)
        response = strict.post(self.url, json.dumps(self.new), content_type=JSON)
        self.assertEqual(response.status_code, 403)
        self.assertFalse(self.model.objects.filter(name=self.new["name"]).exists())


class ProjectIsolationTests:
    def test_list_only_contains_own_projects(self):
        self.model.objects.create(owner=self.bob, name="bob-only")
        self.assertEqual([p["name"] for p in self.alice_client.get(self.url).json()], ["demo"])
        self.assertEqual([p["name"] for p in self.bob_client.get(self.url).json()], ["bob-only"])

    def test_foreign_project_is_404_for_every_method(self):
        url = self.detail(self.project.pk)
        body = json.dumps({"name": "pwn", "html": "x", "css": "x", "js": "x"})
        responses = {
            "GET": self.bob_client.get(url),
            "PUT": self.bob_client.put(url, body, content_type=JSON),
            "PATCH": self.bob_client.patch(url, body, content_type=JSON),
            "DELETE": self.bob_client.delete(url),
        }
        for method, response in responses.items():
            with self.subTest(method=method):
                self.assertEqual(response.status_code, 404)
        self.project.refresh_from_db()
        self.assertEqual((self.project.name, self.project.owner), ("demo", self.alice))

    def test_404_does_not_reveal_whether_the_project_exists(self):
        foreign = self.bob_client.get(self.detail(self.project.pk))
        missing = self.bob_client.get(self.detail(self.project.pk + 999))
        self.assertEqual((foreign.status_code, foreign.content), (missing.status_code, missing.content))

    def test_owner_cannot_be_changed_by_an_update(self):
        url = self.detail(self.project.pk)
        response = self.alice_client.put(
            url, json.dumps({**self.payload, "owner": self.bob.pk}), content_type=JSON)
        self.assertEqual(response.status_code, 200)
        self.project.refresh_from_db()
        self.assertEqual(self.project.owner, self.alice)

    def test_update_to_a_name_already_used_by_the_same_user_is_400(self):
        other = self.model.objects.create(owner=self.alice, name="autre")
        response = self.alice_client.put(
            self.detail(other.pk), json.dumps({"name": "demo"}), content_type=JSON)
        self.assertEqual(response.status_code, 400)

    def test_simultaneous_duplicate_on_update_is_400_not_500(self):
        other = self.model.objects.create(owner=self.alice, name="autre")
        with mock.patch.object(self.serializer, "validate_name", lambda _self, value: value):
            response = self.alice_client.put(
                self.detail(other.pk), json.dumps({"name": "demo"}), content_type=JSON)
        self.assertEqual(response.status_code, 400)
        other.refresh_from_db()
        self.assertEqual(other.name, "autre")

    def test_projects_without_owner_are_invisible_and_untouchable(self):
        """Les anciens projets d'avant la migration 0002 (owner NULL) ne sont à personne."""
        orphan = self.model.objects.create(owner=None, name="orphelin")
        for client in (self.alice_client, self.bob_client):
            self.assertNotIn("orphelin", [p["name"] for p in client.get(self.url).json()])
            self.assertEqual(client.get(self.detail(orphan.pk)).status_code, 404)
            self.assertEqual(client.delete(self.detail(orphan.pk)).status_code, 404)
        self.assertTrue(self.model.objects.filter(pk=orphan.pk).exists())

    def test_no_api_call_can_create_a_project_without_owner(self):
        self.post(self.bob_client)
        self.alice_client.put(self.detail(self.project.pk), json.dumps({"name": "b"}), content_type=JSON)
        self.assertFalse(self.model.objects.filter(owner__isnull=True).exists())


class DeleteProjectTests:
    def test_owner_can_delete_then_gets_404(self):
        url = self.detail(self.project.pk)
        self.assertEqual(self.alice_client.delete(url).status_code, 204)
        self.assertFalse(self.model.objects.filter(pk=self.project.pk).exists())
        self.assertEqual(self.alice_client.delete(url).status_code, 404)   # double suppression : pas de 500
        self.assertEqual(self.alice_client.get(url).status_code, 404)

    def test_delete_only_removes_the_targeted_project(self):
        keep = self.model.objects.create(owner=self.alice, name="garde")
        bob_same_name = self.model.objects.create(owner=self.bob, name="demo")
        self.alice_client.delete(self.detail(self.project.pk))
        self.assertTrue(self.model.objects.filter(pk=keep.pk).exists())
        self.assertTrue(self.model.objects.filter(pk=bob_same_name.pk).exists())

    def test_delete_unknown_or_malformed_id_is_404(self):
        for pk in ("999999", "abc", "-1", "1.5", "0"):
            with self.subTest(pk=pk):
                self.assertEqual(self.alice_client.delete(f"{self.url}{pk}/").status_code, 404)

    def test_deleting_a_user_removes_their_projects_only(self):
        self.model.objects.create(owner=self.bob, name="bob")
        self.alice.delete()
        self.assertEqual(list(self.model.objects.values_list("name", flat=True)), ["bob"])

    def test_method_not_allowed_on_collection_delete(self):
        self.assertEqual(self.alice_client.delete(self.url).status_code, 405)
        self.assertTrue(self.model.objects.filter(pk=self.project.pk).exists())


class RenameProjectTests:
    """Renommage depuis la modale « Projets » : ``PATCH {"name": ...}`` sur le projet courant."""

    def rename(self, client, pk, name):
        return client.patch(self.detail(pk), json.dumps({"name": name}), content_type=JSON)

    def test_patch_name_renames_and_keeps_the_content(self):
        response = self.rename(self.alice_client, self.project.pk, "renommé")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "renommé")
        self.project.refresh_from_db()
        self.assertEqual(self.project.name, "renommé")
        for field in self.content_fields:
            self.assertEqual(getattr(self.project, field), self.payload[field], field)

    def test_renaming_to_its_own_name_is_accepted(self):
        self.assertEqual(self.rename(self.alice_client, self.project.pk, "demo").status_code, 200)

    def test_rename_to_a_name_used_by_another_project_is_400_and_changes_nothing(self):
        other = self.model.objects.create(owner=self.alice, name="autre")
        response = self.rename(self.alice_client, other.pk, "demo")
        self.assertEqual(response.status_code, 400)
        self.assertIn("name", response.json())
        other.refresh_from_db()
        self.assertEqual(other.name, "autre")

    def test_rename_to_a_name_used_by_someone_else_is_allowed(self):
        self.model.objects.create(owner=self.bob, name="pris-par-bob")
        self.assertEqual(self.rename(self.alice_client, self.project.pk, "pris-par-bob").status_code, 200)

    def test_rename_with_an_empty_or_too_long_name_is_400(self):
        for name in ("", "x" * 101):
            with self.subTest(length=len(name)):
                self.assertEqual(self.rename(self.alice_client, self.project.pk, name).status_code, 400)
        self.project.refresh_from_db()
        self.assertEqual(self.project.name, "demo")

    def test_cannot_rename_a_foreign_project(self):
        self.assertEqual(self.rename(self.bob_client, self.project.pk, "volé").status_code, 404)
        self.project.refresh_from_db()
        self.assertEqual(self.project.name, "demo")


class WebProjectsApiTests(CreateProjectTests, ProjectIsolationTests, DeleteProjectTests, RenameProjectTests,
                           ProjectsApiTestCase):
    """API de l'éditeur Web (HTML/CSS/JS)."""


class TypeScriptProjectsApiTests(CreateProjectTests, ProjectIsolationTests, DeleteProjectTests,
                                 RenameProjectTests, ProjectsApiTestCase):
    """L'API TypeScript hérite du même code : mêmes garanties, sur son propre modèle."""

    url = "/editor/api/ts-projects/"
    model = TypeScriptProject
    serializer = TypeScriptProjectSerializer
    payload = {"name": "demo", "html": "<p>a</p>", "css": "p{}", "ts": "const a: number = 1"}
    new = {"name": "nouveau", "html": "", "css": "", "ts": ""}

    def test_web_and_typescript_projects_are_independent(self):
        Project.objects.create(owner=self.alice, name="web")
        self.assertEqual([p["name"] for p in self.alice_client.get(self.url).json()], ["demo"])


class PythonProjectsApiTests(CreateProjectTests, ProjectIsolationTests, DeleteProjectTests,
                             RenameProjectTests, ProjectsApiTestCase):
    """L'API Python hérite du même code : mêmes garanties, sur son propre modèle (liste de fichiers)."""

    url = "/editor/api/py-projects/"
    model = PythonProject
    serializer = PythonProjectSerializer
    payload = {"name": "demo", "files": [{"name": "main.py", "content": "print('a')"}]}
    new = {"name": "nouveau", "files": [{"name": "main.py", "content": ""}]}
    content_fields = ("files",)
    invalid_content = {"name": "ok", "files": None}

    def test_python_web_and_typescript_projects_are_independent(self):
        Project.objects.create(owner=self.alice, name="web")
        TypeScriptProject.objects.create(owner=self.alice, name="ts")
        self.assertEqual([p["name"] for p in self.alice_client.get(self.url).json()], ["demo"])
        self.assertEqual(self.alice_client.get("/editor/api/projects/").json()[0]["name"], "web")

    def test_files_are_stored_and_returned_as_sent(self):
        files = [{"name": "main.py", "content": "import utils"}, {"name": "utils.py", "content": "X = 1"},
                 {"name": "data.json", "content": "{}"}]
        response = self.post(self.alice_client, {"name": "multi", "files": files})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["files"], files)
        self.assertEqual(self.model.objects.get(name="multi").files, files)

    def test_unexpected_keys_of_a_file_are_dropped(self):
        files = [{"name": "main.py", "content": "", "owner": self.bob.pk, "extra": [1]}]
        response = self.post(self.alice_client, {"name": "propre", "files": files})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["files"], [{"name": "main.py", "content": ""}])

    def test_files_are_optional_and_may_be_empty(self):
        for name, data in (("sans", {"name": "sans"}), ("vide", {"name": "vide", "files": []})):
            with self.subTest(name=name):
                response = self.post(self.alice_client, data)
                self.assertEqual(response.status_code, 201)
        self.assertEqual(self.model.objects.get(name="sans").files, [])

    def test_invalid_files_are_400_and_nothing_is_stored(self):
        too_many = [{"name": f"m{i}.py", "content": ""} for i in range(python_files.MAX_FILES + 1)]
        invalid = {
            "pas une liste": "main.py",
            "élément sans contenu": [{"name": "main.py"}],
            "contenu non textuel": [{"name": "main.py", "content": 1}],
            "élément qui n'est pas un objet": ["main.py"],
            "nom avec dossier": [{"name": "dir/main.py", "content": ""}],
            "nom qui remonte": [{"name": "../main.py", "content": ""}],
            "module standard masqué": [{"name": "json.py", "content": ""}],
            "doublon (casse ignorée)": [{"name": "utils.py", "content": ""}, {"name": "Utils.py", "content": ""}],
            "trop de fichiers": too_many,
            "contenu trop long": [{"name": "main.py", "content": "x" * (python_files.MAX_CHARS + 1)}],
        }
        for why, files in invalid.items():
            with self.subTest(why=why):
                response = self.post(self.alice_client, {"name": "refuse", "files": files})
                self.assertEqual(response.status_code, 400)
                self.assertIn("files", response.json())
        self.assertFalse(self.model.objects.filter(name="refuse").exists())

    def test_patch_files_saves_the_content_and_never_touches_the_name(self):
        """C'est ce que fait l'éditeur à chaque enregistrement : un enregistrement tardif ne peut pas défaire un renommage."""
        files = [{"name": "main.py", "content": "print(2)"}]
        response = self.alice_client.patch(self.detail(self.project.pk), json.dumps({"files": files}), content_type=JSON)
        self.assertEqual(response.status_code, 200)
        self.project.refresh_from_db()
        self.assertEqual((self.project.name, self.project.files), ("demo", files))

    def test_invalid_files_on_update_are_400_and_keep_the_stored_ones(self):
        response = self.alice_client.patch(
            self.detail(self.project.pk), json.dumps({"files": [{"name": "1abc.py", "content": ""}]}), content_type=JSON)
        self.assertEqual(response.status_code, 400)
        self.project.refresh_from_db()
        self.assertEqual(self.project.files, self.payload["files"])


class AuthenticationRequiredTests(TestCase):
    """Aucune route de l'API de l'éditeur n'est accessible sans connexion."""

    API_ROUTES = [
        ("get", "/editor/api/projects/"),
        ("post", "/editor/api/projects/"),
        ("get", "/editor/api/projects/1/"),
        ("put", "/editor/api/projects/1/"),
        ("patch", "/editor/api/projects/1/"),
        ("delete", "/editor/api/projects/1/"),
        ("get", "/editor/api/ts-projects/"),
        ("post", "/editor/api/ts-projects/"),
        ("get", "/editor/api/ts-projects/1/"),
        ("delete", "/editor/api/ts-projects/1/"),
        ("get", "/editor/api/py-projects/"),
        ("post", "/editor/api/py-projects/"),
        ("get", "/editor/api/py-projects/1/"),
        ("patch", "/editor/api/py-projects/1/"),
        ("delete", "/editor/api/py-projects/1/"),
        ("get", "/editor/api/load-monaco-config/"),
        ("post", "/editor/api/save-monaco-config/"),
        ("post", "/editor/api/export-zip/"),
        ("post", "/editor/api/import-zip/"),
        ("post", "/editor/api/ts-export-zip/"),
        ("post", "/editor/api/ts-import-zip/"),
        ("post", "/editor/preview/"),
        ("get", "/editor/api/"),   # racine de l'API navigable du routeur
    ]

    def test_anonymous_gets_401_json_on_every_api_route(self):
        client = Client(raise_request_exception=False)
        for method, url in self.API_ROUTES:
            with self.subTest(method=method, url=url):
                response = getattr(client, method)(url, "{}", content_type=JSON) if method != "get" \
                    else client.get(url, HTTP_ACCEPT=JSON)
                self.assertEqual(response.status_code, 401)
                self.assertEqual(response.json()["detail"], "Authentification requise.")

    def test_anonymous_cannot_read_a_stored_preview(self):
        response = Client().get("/editor/preview/abcdef/")
        self.assertEqual(response.status_code, 302)
        self.assertIn("login", response["Location"])

    def test_anonymous_write_never_touches_the_database(self):
        owner = User.objects.create_user("owner", password=PASSWORD)
        project = Project.objects.create(owner=owner, name="secret")
        anon = Client()
        anon.delete(f"/editor/api/projects/{project.pk}/", HTTP_ACCEPT=JSON)
        anon.put(f"/editor/api/projects/{project.pk}/", json.dumps({"name": "x"}), content_type=JSON)
        anon.post("/editor/api/projects/", json.dumps({"name": "x"}), content_type=JSON)
        self.assertEqual(list(Project.objects.values_list("name", "owner_id")), [("secret", owner.pk)])

    def test_viewsets_declare_permissions_explicitly(self):
        from rest_framework.permissions import IsAuthenticated

        from .views import ProjectViewSet, PythonProjectViewSet, TypeScriptProjectViewSet
        for view in (ProjectViewSet, TypeScriptProjectViewSet, PythonProjectViewSet):
            self.assertEqual(view.permission_classes, [IsAuthenticated])
