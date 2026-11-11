"""
Éditeur Python : erreurs, autocomplétion, infobulles et aide aux appels.

``language_service.py`` s'exécute dans le navigateur (Pyodide), mais c'est du Python ordinaire : on le charge ici
avec les mêmes wheels vendorées (jedi, parso, pyflakes), extraites dans un dossier temporaire, pour tester sa
logique sous CPython sans rien installer. Le dialogue avec Monaco (JavaScript) n'est pas couvert par ces tests.
"""

import contextlib
import hashlib
import importlib.util
import io
import json
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

from django.contrib.auth import get_user_model
from django.contrib.staticfiles import finders
from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse

TOOLS = Path(finders.find("vendor/python-tools"))
SERVICE_FILE = Path(finders.find("editor/js/python/language/language_service.py"))


def load_service():
    """Charge language_service.py avec les wheels vendorées ; renvoie (module, dossier temporaire)."""
    root = Path(tempfile.mkdtemp(prefix="pyls-test-"))
    site = root / "site"
    for wheel in json.loads((TOOLS / "manifest.json").read_text())["wheels"]:
        zipfile.ZipFile(TOOLS / wheel["file"]).extractall(site)
    sys.path.insert(0, str(site))

    spec = importlib.util.spec_from_file_location("pyls_under_test", SERVICE_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.PROJECT_DIR = str(root / "project")
    module.HIDDEN_PATHS = {str(site)}
    return module, root, str(site)


# Une seule extraction pour tout ce fichier : jedi reste en mémoire (sys.modules) après le premier import et
# continue de lire ses données (typeshed) dans le dossier d'origine, qui ne doit donc pas disparaître avant la fin.
SERVICE = None


def setUpModule():
    global SERVICE
    SERVICE = load_service()


def tearDownModule():
    module, root, site = SERVICE
    sys.path.remove(site)
    for name in [n for n, m in sys.modules.items() if str(getattr(m, "__file__", "") or "").startswith(site)]:
        del sys.modules[name]
    shutil.rmtree(root, ignore_errors=True)


class ServiceTestCase(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ls, cls.root, cls.site = SERVICE

    def lint(self, source):
        return json.loads(self.ls.lint(source, "main.py"))

    def complete(self, snippet, prelude=""):
        """``snippet`` contient « | » à l'emplacement du curseur."""
        result = json.loads(self.ls.complete(*self.at(prelude + snippet), "main.py"))
        return [item["label"] for item in result["items"]], result

    def at(self, text):
        lines = text.split("\n")
        row = next(i for i, line in enumerate(lines) if "|" in line)
        column = lines[row].index("|") + 1
        lines[row] = lines[row].replace("|", "", 1)
        return "\n".join(lines), row + 1, column

    def hover(self, text):
        return json.loads(self.ls.hover(*self.at(text), "main.py"))

    def signature(self, text):
        return json.loads(self.ls.signature(*self.at(text), "main.py"))


class VendoredToolsTests(SimpleTestCase):
    def test_manifest_matches_the_wheels(self):
        """Une wheel modifiée ou tronquée serait refusée par le worker : le manifeste doit rester juste."""
        wheels = json.loads((TOOLS / "manifest.json").read_text())["wheels"]
        self.assertEqual([w["file"].split("-")[0] for w in wheels], ["parso", "jedi", "pyflakes"])  # parso avant jedi
        for wheel in wheels:
            data = (TOOLS / wheel["file"]).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), wheel["sha256"], wheel["file"])
            self.assertEqual(len(data), wheel["size"], wheel["file"])

    def test_jedi_and_parso_versions_are_the_ones_pyodide_lists(self):
        """Versions testées avec cette version de Pyodide (voir README du dossier)."""
        lock = json.loads(Path(finders.find("vendor/pyodide/pyodide-lock.json")).read_text())["packages"]
        files = [w["file"] for w in json.loads((TOOLS / "manifest.json").read_text())["wheels"]]
        for package in ("jedi", "parso"):
            wheel = next(name for name in files if name.startswith(package + "-"))
            self.assertTrue(wheel.startswith(f"{package}-{lock[package]['version']}-"), (wheel, lock[package]["version"]))


class PageTests(TestCase):
    def test_page_exposes_the_tools_location_and_the_status_label(self):
        self.client.force_login(get_user_model().objects.create_user("alice", password="Mot-de-passe-solide-42"))
        html = self.client.get(reverse("editor", args=["codelab-py"])).content.decode()
        self.assertIn("data-python-tools=", html)
        self.assertIn("vendor/python-tools/", html)
        self.assertIn('id="py-lang-state"', html)

    def test_static_files_of_the_language_service_exist(self):
        for path in ("editor/js/python/language/PythonLanguageService.js",
                     "editor/js/python/language/python-language.worker.js",
                     "editor/js/python/language/language_service.py",
                     "vendor/python-tools/manifest.json", "vendor/python-tools/README.md"):
            self.assertIsNotNone(finders.find(path), path)

    def test_anonymous_cannot_load_the_editor(self):
        self.assertEqual(Client().get(reverse("editor", args=["codelab-py"])).status_code, 302)


class LintTests(ServiceTestCase):
    def test_clean_code_has_no_diagnostics(self):
        self.assertEqual(self.lint("import math\nprint(math.pi)\n"), [])
        self.assertEqual(self.lint(""), [])

    def test_syntax_error_is_reported_in_french_with_a_visible_range(self):
        (item,) = self.lint("if True\n    pass\n")
        self.assertEqual((item["line"], item["severity"], item["code"]), (1, "error", "SyntaxError"))
        self.assertIn("« : » attendu", item["message"])
        self.assertGreater(item["endCol"], item["col"], "un soulignement de largeur nulle est invisible")

    def test_common_beginner_mistakes_are_translated(self):
        cases = {
            "print 'bonjour'\n": "parenthèses manquantes",
            "x = [1 2]\n": "virgule oubliée",
            "if x = 5:\n    pass\n": "vouliez-vous écrire « == »",
            "print('a'\n": "n'est jamais refermé",
            "def f():\nx = 1\n": "bloc indenté attendu après la définition de fonction",
            "x = f'{1 +}'\n": "f-string",     # contient des accolades : ne doit pas faire échouer la traduction
        }
        for source, expected in cases.items():
            with self.subTest(source=source):
                (item,) = self.lint(source)
                self.assertIn(expected, item["message"])

    def test_pyflakes_findings_and_their_severity(self):
        items = {d["code"]: d for d in self.lint("import os\n\ndef f():\n    unused = 1\n    return nope\n")}
        self.assertEqual(items["UndefinedName"]["severity"], "error")
        self.assertIn("« nope »", items["UndefinedName"]["message"])
        self.assertEqual(items["UnusedImport"]["severity"], "warning")
        self.assertTrue(items["UnusedImport"]["unused"] and items["UnusedVariable"]["unused"])
        self.assertFalse(items["UndefinedName"]["unused"])

    def test_top_level_await_is_allowed_and_does_not_hide_uses(self):
        """Pyodide l'accepte ; pyflakes abandonnerait l'analyse et déclarerait asyncio « inutilisé »."""
        self.assertEqual(self.lint("import asyncio\nawait asyncio.sleep(1)\n"), [])
        (item,) = self.lint("await nope()\n")
        self.assertEqual(item["code"], "UndefinedName")

    def test_columns_count_utf16_units_not_bytes_or_code_points(self):
        # « é » = 2 octets UTF-8, « 😀 » = 4 octets UTF-8 mais 2 unités UTF-16 : ast et Monaco ne comptent pas pareil.
        line = 'print("é😀", nope)'
        (item,) = self.lint(line + "\n")
        start = line.encode("utf-16-le").find("nope".encode("utf-16-le")) // 2
        self.assertEqual((item["col"], item["endCol"]), (start + 1, start + 1 + len("nope")))

    def test_crlf_line_endings(self):
        (item,) = self.lint("x = 1\r\nprint(nope)\r\n")
        self.assertEqual((item["line"], item["col"]), (2, 7))

    def test_multiline_statement_underlines_its_first_line_only(self):
        items = self.lint("from os import (\n    path,\n    sep,\n)\n")
        self.assertTrue(items)
        for item in items:
            self.assertEqual(item["line"], item["endLine"])


class CompletionTests(ServiceTestCase):
    def test_standard_library_members(self):
        labels, _ = self.complete("import math\nmath.sq|")
        self.assertEqual(labels, ["sqrt"])
        labels, _ = self.complete('s = "abc"\ns.upp|')
        self.assertEqual(labels, ["upper"])

    def test_names_defined_in_the_file(self):
        labels, _ = self.complete("def calculer_total(a):\n    return a\n\ncalc|")
        self.assertIn("calculer_total", labels)

    def test_keyword_arguments_are_inserted_with_their_equal_sign(self):
        _, result = self.complete("def f(nom, age=3): pass\nf(ag|")
        item = next(i for i in result["items"] if i["label"] == "age=")
        self.assertEqual(item["insert"], "age=")

    def test_no_suggestions_in_comments_or_strings(self):
        self.assertEqual(self.complete("# impor|")[0], [])
        self.assertEqual(self.complete('print("impor|")')[0], [])
        self.assertNotEqual(self.complete('x = "#"; impor|')[0], [], "un # dans une chaîne n'est pas un commentaire")

    def test_other_project_files_are_importable(self):
        self.ls.sync_project(json.dumps({"files": {"utils.py": "def double(n):\n    return n * 2\n\ndef triple(n):\n    return n * 3\n"}, "remove": []}))
        labels, _ = self.complete("from utils import |")
        self.assertTrue({"double", "triple"} <= set(labels))
        labels, _ = self.complete("import utils\nutils.dou|")
        self.assertEqual(labels, ["double"])

        self.ls.sync_project(json.dumps({"files": {"utils.py": "def quadruple(n): pass\n"}, "remove": []}))
        labels, _ = self.complete("from utils import |")
        self.assertIn("quadruple", labels)
        self.assertNotIn("triple", labels)

        self.ls.sync_project(json.dumps({"files": {}, "remove": ["utils.py"]}))
        self.assertEqual(self.complete("import utils\nutils.|")[0], [])

    def test_sync_ignores_unsafe_names(self):
        self.ls.sync_project(json.dumps({"files": {"../evil.py": "x = 1", "a/b.py": "x = 1", ".hidden": ""}, "remove": ["../x"]}))
        self.assertFalse((Path(self.ls.PROJECT_DIR).parent / "evil.py").exists())
        self.assertFalse((Path(self.ls.PROJECT_DIR) / "a").exists())

    def test_the_analysis_tools_themselves_are_not_offered(self):
        """Dans le navigateur, jedi/pyflakes sont installés à part : le programme de l'élève ne peut pas les importer,
        donc ils ne doivent pas être suggérés. On le vérifie avec un module factice, quelle que soit la machine."""
        hidden = Path(self.site) / "zz_outil_masque.py"
        visible_dir = Path(self.root) / "visible"
        visible_dir.mkdir(exist_ok=True)
        hidden.write_text("X = 1\n")
        (visible_dir / "zz_module_visible.py").write_text("X = 1\n")
        sys.path.append(str(visible_dir))
        self.addCleanup(sys.path.remove, str(visible_dir))

        self.assertEqual(self.complete("import zz_outil|")[0], [])
        self.assertEqual(self.complete("import zz_module|")[0], ["zz_module_visible"])
        self.assertIn("random", self.complete("import rando|")[0])

    def test_documentation_is_fetched_separately_and_discarded_when_stale(self):
        labels, result = self.complete("import math\nmath.sq|")
        index = result["items"][labels.index("sqrt")]["index"]
        self.assertIn("square root", json.loads(self.ls.completion_doc(result["token"], index)))
        self.assertEqual(json.loads(self.ls.completion_doc(result["token"] + 1, index)), "")
        self.assertEqual(json.loads(self.ls.completion_doc(result["token"], 10_000)), "")

    def test_runtime_documentation_fills_the_gaps_of_the_stubs(self):
        """typeshed n'a pas de texte d'aide pour str.upper : on le lit sur l'objet réel."""
        info = self.hover('s = "abc"\ns.upper|')
        self.assertIn("uppercase", info["markdown"])


class HoverTests(ServiceTestCase):
    PRELUDE = 'import math\nx = 5\n\ndef greet(name: str, times: int = 2) -> str:\n    """Salue quelqu\'un."""\n    return name * times\n\n'

    def test_function_signature_and_docstring(self):
        info = self.hover(self.PRELUDE + "gree|t")
        self.assertIn("def greet(name: str, times: int", info["markdown"])
        self.assertIn("Salue quelqu'un.", info["markdown"])

    def test_standard_library_function(self):
        self.assertIn("square root", self.hover(self.PRELUDE + "math.sqr|t(4)")["markdown"])

    def test_variable_shows_its_inferred_type(self):
        self.assertIn("(variable) x: int", self.hover(self.PRELUDE + "x|")["markdown"])

    def test_range_covers_the_word_in_utf16_units(self):
        info = self.hover('s = "😀"; x = 1; x|')
        word_start = len('s = "😀"; x = 1; '.encode("utf-16-le")) // 2 + 1
        self.assertEqual((info["startCol"], info["endCol"]), (word_start, word_start + 1))

    def test_nothing_on_keywords_numbers_strings_comments_or_blank_space(self):
        for text in ("de|f f(): pass", "y = 4|2", 'print("bon|jour")', "# x|", "x = 1\n|"):
            with self.subTest(text=text):
                self.assertIsNone(self.hover(text))

    def test_docstring_cannot_break_out_of_the_code_fence(self):
        info = self.hover('def f():\n    """avant ``` après"""\n\nf|()')
        self.assertEqual(info["markdown"].count("```"), 4)    # deux blocs ouverts et fermés, rien de plus


class SignatureTests(ServiceTestCase):
    def test_active_parameter_follows_the_commas(self):
        source = "def f(a, b, c): pass\nf(1, 2, |"
        result = self.signature(source)
        self.assertEqual(result["signatures"][0]["label"], "f(a, b, c)")
        self.assertEqual(result["param"], 2)
        self.assertEqual(self.signature("def f(a, b, c): pass\nf(|")["param"], 0)

    def test_parameter_offsets_point_at_the_right_substrings(self):
        result = self.signature("def f(a, ab, abc): pass\nf(|")
        label = result["signatures"][0]["label"]
        self.assertEqual([label[s:e] for s, e in result["signatures"][0]["params"]], ["a", "ab", "abc"])

    def test_builtin_function(self):
        self.assertIn("print(", self.signature("print(|")["signatures"][0]["label"])

    def test_overloaded_functions_give_every_signature(self):
        source = ("from typing import overload\n@overload\ndef f(a: int) -> int: ...\n@overload\n"
                  "def f(a: str, b: str) -> str: ...\ndef f(a, b=None): return a\nf(|")
        labels = [s["label"] for s in self.signature(source)["signatures"]]
        self.assertEqual(labels, ["f(a: int) -> int", "f(a: str, b: str) -> str"])

    def test_nothing_outside_a_call(self):
        self.assertIsNone(self.signature("def f(a): pass\nf(1)|"))
        self.assertIsNone(self.signature("# f(|"))


class RobustnessTests(ServiceTestCase):
    """Le service ne doit jamais lever d'exception : il est appelé à chaque frappe sur du code inachevé."""

    SOURCES = ["", "\n", "(", ")", "'''", "def", "class A(", "x = (1,\n", "\x00", "é" * 5000, "a" * 100_000,
               "if x:\n" * 500, "x = " + "(" * 400, "\t\n  \n", "lambda: (yield)", "async def f():\n    await", "@", "a.b.c.", "import", "from . import"]

    def test_no_function_raises_on_any_input_or_position(self):
        with contextlib.redirect_stderr(io.StringIO()):      # le service journalise ces positions absurdes
            self._check_all_inputs()

    def _check_all_inputs(self):
        for source in self.SOURCES:
            for line, column in ((1, 1), (1, 400), (2, 1), (999, 1), (0, 0), (-1, -1)):
                with self.subTest(source=source[:20], line=line, column=column):
                    for result in (self.ls.lint(source, "main.py"),
                                   self.ls.complete(source, line, column, "main.py"),
                                   self.ls.hover(source, line, column, "main.py"),
                                   self.ls.signature(source, line, column, "main.py")):
                        json.loads(result)      # toujours du JSON valide

    def test_unknown_or_dangerous_file_names_fall_back_to_main_py(self):
        for name in ("", "../x.py", "a/b.py", None):
            with self.subTest(name=name):
                json.loads(self.ls.complete("import os\nos.", 2, 4, name))

    def test_warm_up(self):
        self.assertEqual(self.ls.warm_up(), "ok")
