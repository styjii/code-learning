import io
import json
import zipfile

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from django.urls import reverse

from .models import Project, TypeScriptProject
from .tests import make_zip
from .typescript_config import (
    DEFAULT_COMPILER_OPTIONS,
    build_tsconfig,
    effective_compiler_options,
    options_from_tsconfig,
    sanitize_compiler_options,
    validate_compiler_options,
)

User = get_user_model()
PASSWORD = "Mot-de-passe-solide-42"
PROJECTS_URL = "/editor/api/ts-projects/"
EXPORT_URL = "/editor/api/ts-export-zip/"
IMPORT_URL = "/editor/api/ts-import-zip/"


class CompilerOptionsConfigTests(TestCase):
    """Les options du compilateur sont limitées à une liste blanche, avec type et valeur vérifiés."""

    def test_defaults_are_strict_esnext(self):
        self.assertIs(DEFAULT_COMPILER_OPTIONS["strict"], True)
        self.assertEqual(DEFAULT_COMPILER_OPTIONS["target"], "ESNext")

    def test_valid_options_are_accepted(self):
        clean, errors = validate_compiler_options({"target": "ES2022", "strict": False, "noUnusedLocals": True})
        self.assertEqual(errors, {})
        self.assertEqual(clean, {"target": "ES2022", "strict": False, "noUnusedLocals": True})

    def test_unknown_and_fixed_options_are_refused(self):
        for key in ("module", "moduleDetection", "outDir", "plugins", "paths", "__proto__", "lib"):
            with self.subTest(key=key):
                self.assertIn(key, validate_compiler_options({key: "x"})[1])

    def test_values_are_type_checked(self):
        invalid = [{"target": "ES2099"}, {"target": "es2022"}, {"target": 9}, {"target": None},
                   {"strict": "true"}, {"strict": 1}, {"noEmitOnError": None}, {"noUnusedLocals": []}]
        for payload in invalid:
            with self.subTest(payload=payload):
                self.assertTrue(validate_compiler_options(payload)[1])

    def test_non_object_is_refused(self):
        for body in ([], "strict", 3, None):
            with self.subTest(body=body):
                self.assertTrue(validate_compiler_options(body)[1])

    def test_stored_garbage_is_ignored_on_read(self):
        stored = {"target": "ES2020", "strict": "oui", "outDir": "/etc", "noUnusedLocals": True}
        self.assertEqual(sanitize_compiler_options(stored), {"target": "ES2020", "noUnusedLocals": True})
        effective = effective_compiler_options(stored)
        self.assertIs(effective["strict"], True)                 # valeur invalide : retour au défaut
        self.assertNotIn("outDir", effective)

    def test_tsconfig_contains_fixed_options_and_files(self):
        config = build_tsconfig({"target": "ES2020", "strict": False})
        options = config["compilerOptions"]
        self.assertEqual((options["target"], options["strict"]), ("ES2020", False))
        self.assertEqual((options["module"], options["moduleDetection"]), ("ESNext", "force"))
        self.assertEqual(options["lib"], ["ES2020", "DOM", "DOM.Iterable"])
        self.assertEqual(config["files"], ["script.ts"])

    def test_es5_tsconfig_has_no_iterable_dom_lib(self):
        self.assertEqual(build_tsconfig({"target": "ES5"})["compilerOptions"]["lib"], ["ES5", "DOM"])

    def test_options_from_tsconfig(self):
        text = '{"compilerOptions": {"target": "es2021", "strict": false, "outDir": "dist", "noUnusedLocals": "x"}}'
        self.assertEqual(options_from_tsconfig(text), {"target": "ES2021", "strict": False})

    def test_unreadable_tsconfig_gives_nothing(self):
        for text in ("", "pas du json", "[]", "3", '{"compilerOptions": 3}', '{"compilerOptions": []}'):
            with self.subTest(text=text):
                self.assertEqual(options_from_tsconfig(text), {})


class TypeScriptProjectApiTests(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user("alice", password=PASSWORD)
        self.bob = User.objects.create_user("bob", password=PASSWORD)
        self.alice_client, self.bob_client = Client(), Client()
        self.alice_client.force_login(self.alice)
        self.bob_client.force_login(self.bob)

    def post(self, client, payload):
        return client.post(PROJECTS_URL, json.dumps(payload), content_type="application/json")

    def test_anonymous_gets_403(self):
        self.assertEqual(Client().get(PROJECTS_URL).status_code, 403)
        self.assertEqual(Client().post(PROJECTS_URL, "{}", content_type="application/json").status_code, 403)

    def test_create_returns_complete_default_options(self):
        response = self.post(self.alice_client, {"name": "Test", "html": "<p>", "css": "p{}", "ts": "let a = 1"})
        self.assertEqual(response.status_code, 201)
        body = response.json()
        self.assertEqual((body["html"], body["css"], body["ts"]), ("<p>", "p{}", "let a = 1"))
        self.assertEqual(body["compiler_options"], DEFAULT_COMPILER_OPTIONS)
        self.assertEqual(TypeScriptProject.objects.get().owner, self.alice)

    def test_options_are_saved_and_returned_complete(self):
        project_id = self.post(self.alice_client, {"name": "A"}).json()["id"]
        response = self.alice_client.put(
            f"{PROJECTS_URL}{project_id}/",
            json.dumps({"name": "A", "ts": "x", "compiler_options": {"strict": False, "target": "ES2017"}}),
            content_type="application/json")
        self.assertEqual(response.status_code, 200)
        options = self.alice_client.get(f"{PROJECTS_URL}{project_id}/").json()["compiler_options"]
        self.assertEqual(options, {**DEFAULT_COMPILER_OPTIONS, "strict": False, "target": "ES2017"})

    def test_update_without_options_keeps_them(self):
        project_id = self.post(self.alice_client, {"name": "A", "compiler_options": {"strict": False}}).json()["id"]
        self.alice_client.put(f"{PROJECTS_URL}{project_id}/", json.dumps({"name": "A", "ts": "y"}),
                              content_type="application/json")
        self.assertIs(TypeScriptProject.objects.get().compiler_options["strict"], False)

    def test_invalid_options_are_refused_and_nothing_is_saved(self):
        for options in ({"outDir": "/tmp"}, {"target": "ES2099"}, {"strict": "yes"}, {"module": "CommonJS"}, [], "x"):
            with self.subTest(options=options):
                response = self.post(self.alice_client, {"name": "Bad", "compiler_options": options})
                self.assertEqual(response.status_code, 400)
                self.assertIn("compiler_options", response.json())
        self.assertFalse(TypeScriptProject.objects.exists())

    def test_projects_are_private_to_their_owner(self):
        project_id = self.post(self.alice_client, {"name": "Secret", "ts": "x"}).json()["id"]
        self.assertEqual(self.bob_client.get(PROJECTS_URL).json(), [])
        self.assertEqual(self.bob_client.get(f"{PROJECTS_URL}{project_id}/").status_code, 404)
        self.assertEqual(self.bob_client.delete(f"{PROJECTS_URL}{project_id}/").status_code, 404)
        self.assertEqual(self.bob_client.put(f"{PROJECTS_URL}{project_id}/", json.dumps({"name": "x"}),
                                             content_type="application/json").status_code, 404)

    def test_names_are_unique_per_user_only(self):
        self.assertEqual(self.post(self.alice_client, {"name": "Même nom"}).status_code, 201)
        self.assertEqual(self.post(self.alice_client, {"name": "Même nom"}).status_code, 400)
        self.assertEqual(self.post(self.bob_client, {"name": "Même nom"}).status_code, 201)

    def test_web_and_typescript_projects_are_independent(self):
        Project.objects.create(owner=self.alice, name="Web", js="1")
        self.assertEqual(self.alice_client.get(PROJECTS_URL).json(), [])
        self.assertEqual(self.post(self.alice_client, {"name": "Web"}).status_code, 201)   # même nom permis
        self.assertEqual(len(self.alice_client.get("/editor/api/projects/").json()), 1)    # l'éditeur Web est inchangé

    def test_owner_cannot_be_set_by_client(self):
        self.post(self.alice_client, {"name": "A", "owner": self.bob.pk})
        self.assertEqual(TypeScriptProject.objects.get().owner, self.alice)


class TypeScriptZipTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("alice", password=PASSWORD)
        self.client = Client()
        self.client.force_login(self.user)

    def export(self, payload):
        response = self.client.post(EXPORT_URL, json.dumps(payload), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        return zipfile.ZipFile(io.BytesIO(response.content))

    def upload(self, data, name="project.zip"):
        return self.client.post(IMPORT_URL, {"zip_file": SimpleUploadedFile(name, data)})

    def test_export_contains_the_four_files(self):
        archive = self.export({"project": "Démo <b>", "html": "<p>Salut</p>", "css": "p{color:red}", "ts": "const a: number = 1;",
                               "compilerOptions": {"target": "ES2020", "strict": False}})
        self.assertEqual(sorted(archive.namelist()), ["index.html", "script.ts", "style.css", "tsconfig.json"])
        index = archive.read("index.html").decode()
        self.assertIn("<p>Salut</p>", index)
        self.assertIn("&lt;b&gt;", index)                                   # titre échappé
        self.assertIn('<script type="module" src="./script.js"></script>', index)
        self.assertEqual(archive.read("script.ts").decode(), "const a: number = 1;")
        tsconfig = json.loads(archive.read("tsconfig.json"))
        self.assertEqual((tsconfig["compilerOptions"]["target"], tsconfig["compilerOptions"]["strict"]), ("ES2020", False))

    def test_export_ignores_invalid_options(self):
        archive = self.export({"project": "p", "compilerOptions": {"outDir": "/etc", "target": "nope"}})
        options = json.loads(archive.read("tsconfig.json"))["compilerOptions"]
        self.assertNotIn("outDir", options)
        self.assertEqual(options["target"], DEFAULT_COMPILER_OPTIONS["target"])

    def test_export_without_options_uses_defaults(self):
        options = json.loads(self.export({"project": "p"}).read("tsconfig.json"))["compilerOptions"]
        self.assertIs(options["strict"], True)

    def test_round_trip(self):
        archive_bytes = self.client.post(EXPORT_URL, json.dumps({
            "project": "Rond", "html": "<h1>Titre é</h1>", "css": "h1{}", "ts": "let x: string = 'é';",
            "compilerOptions": {"target": "ES2018", "strict": False, "noUnusedLocals": True}}),
            content_type="application/json").content
        body = self.upload(archive_bytes, "Rond.zip").json()
        self.assertEqual(body["project"], "Rond")
        self.assertEqual(body["html"].strip(), "<h1>Titre é</h1>")
        self.assertEqual((body["css"], body["ts"]), ("h1{}", "let x: string = 'é';"))
        self.assertEqual(body["compiler_options"],
                         {**DEFAULT_COMPILER_OPTIONS, "target": "ES2018", "strict": False, "noUnusedLocals": True})

    def test_import_without_tsconfig_gives_defaults_and_removes_scripts(self):
        data = make_zip({"index.html": "<body><p>x</p><script>evil()</script></body>", "script.ts": "let a = 1"})
        body = self.upload(data).json()
        self.assertEqual(body["html"], "<p>x</p>")
        self.assertEqual(body["ts"], "let a = 1")
        self.assertEqual(body["css"], "")
        self.assertEqual(body["compiler_options"], DEFAULT_COMPILER_OPTIONS)

    def test_import_ignores_forbidden_tsconfig_keys(self):
        tsconfig = json.dumps({"compilerOptions": {"outDir": "/etc", "strict": False}})
        body = self.upload(make_zip({"tsconfig.json": tsconfig})).json()
        self.assertNotIn("outDir", body["compiler_options"])
        self.assertIs(body["compiler_options"]["strict"], False)

    def test_import_in_project_folder(self):
        data = make_zip({"proj/index.html": "<body>x</body>", "proj/script.ts": "1", "proj/tsconfig.json": "{}"})
        self.assertEqual(self.upload(data, "proj.zip").json()["ts"], "1")

    def test_import_without_file_is_400(self):
        self.assertEqual(self.client.post(IMPORT_URL, {}).status_code, 400)

    def test_invalid_archive_is_400(self):
        self.assertEqual(self.upload(b"pas un zip").status_code, 400)

    @override_settings(EDITOR_ZIP_MAX_UPLOAD_BYTES=64 * 1024, EDITOR_ZIP_MAX_ENTRIES=10,
                       EDITOR_ZIP_MAX_FILE_BYTES=8 * 1024, EDITOR_ZIP_MAX_TOTAL_BYTES=16 * 1024)
    def test_size_limits_apply_like_the_web_import(self):
        self.assertEqual(self.upload(make_zip({"script.ts": "a" * (3 * 1024 * 1024)})).status_code, 413)
        self.assertEqual(self.upload(make_zip({"tsconfig.json": "a" * (9 * 1024)})).status_code, 413)
        self.assertEqual(self.upload(make_zip({f"f{i}.txt": "x" for i in range(11)})).status_code, 413)

    def test_anonymous_gets_403(self):
        self.assertEqual(Client().post(EXPORT_URL, "{}", content_type="application/json").status_code, 403)
        self.assertEqual(Client().post(IMPORT_URL, {}).status_code, 403)

    def test_web_import_is_unchanged_by_the_refactoring(self):
        data = make_zip({"index.html": "<body>w</body>", "style.css": "a{}", "script.js": "1", "script.ts": "ignoré"})
        body = self.client.post("/editor/api/import-zip/", {"zip_file": SimpleUploadedFile("w.zip", data)}).json()
        self.assertEqual((body["html"], body["css"], body["js"]), ("w", "a{}", "1"))
        self.assertNotIn("ts", body)


class TypeScriptPreviewTests(TestCase):
    """L'aperçu exécute le JavaScript compilé comme module ; l'éditeur Web garde son comportement."""

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.create_user("alice", password=PASSWORD))

    def preview(self, **extra):
        url = self.client.post("/editor/preview/", {"html": "<p>x</p>", "css": "", "js": "await 1;", **extra}).json()["url"]
        response = self.client.get(url)
        self.assertIn("sandbox", response["Content-Security-Policy"])
        return response.content.decode()

    def test_module_flag_runs_script_as_module(self):
        page = self.preview(module="1")
        self.assertIn('<script type="module">', page)
        self.assertIn("await 1;", page)
        self.assertNotIn("window.onerror(e.message", page)

    def test_default_preview_is_unchanged(self):
        page = self.preview()
        self.assertNotIn('type="module"', page)
        self.assertIn("window.onerror(e.message", page)


class TypeScriptEditorPageTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("alice", password=PASSWORD)
        self.client = Client()

    def test_page_requires_login(self):
        url = reverse("typescript-editor")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response["Location"])

    def test_page_contains_the_editor_and_options(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("typescript-editor"))
        self.assertEqual(response.status_code, 200)
        html = response.content.decode()
        for fragment in ('id="html-editor"', 'id="css-editor"', 'id="ts-editor"', 'id="ts-tab"', 'id="run-code"',
                         'id="ts-options"', 'data-ts-option="strict"', 'data-ts-option="target"',
                         'value="ESNext"', "editor/js/typescript/main.js"):
            self.assertIn(fragment, html)
        self.assertNotIn('id="js-editor"', html)

    def test_every_option_of_the_server_has_a_form_control(self):
        self.client.force_login(self.user)
        html = self.client.get(reverse("typescript-editor")).content.decode()
        for key in DEFAULT_COMPILER_OPTIONS:
            self.assertIn(f'data-ts-option="{key}"', html)

    def test_editors_and_home_link_to_each_other(self):
        self.client.force_login(self.user)
        ts_url = reverse("typescript-editor")
        for name in ("editor-index", "python-editor"):
            self.assertContains(self.client.get(reverse(name)), f'href="{ts_url}"')
        self.assertContains(self.client.get(ts_url), f'href="{reverse("editor-index")}"')
        self.assertContains(self.client.get(ts_url), f'href="{reverse("python-editor")}"')
        self.assertContains(self.client.get(reverse("index")), f'href="{ts_url}"')

    def test_static_files_used_by_the_page_exist(self):
        from django.contrib.staticfiles import finders

        for path in (
            "editor/js/typescript/main.js", "editor/js/typescript/state.js", "editor/js/typescript/TsCompiler.js",
            "editor/js/typescript/TsCompilerOptions.js", "editor/js/typescript/TsEditorManager.js",
            "editor/js/typescript/TsEditorBinder.js", "editor/js/typescript/TsOptionsManager.js",
            "editor/js/typescript/TsPreviewManager.js", "editor/js/typescript/TsProjectManager.js",
            "editor/js/typescript/TsProjectZipManager.js", "editor/js/typescript/TsSettingsBinder.js",
            "editor/js/typescript/events/index.js", "editor/js/typescript/events/TsOptionsEvents.js",
            "editor/css/typescript.css", "editor/icons/ts.svg", "editor/snippets/javascript.json",
        ):
            self.assertIsNotNone(finders.find(path), path)
