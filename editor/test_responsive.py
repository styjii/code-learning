"""
Garde-fous du responsive des trois éditeurs (Web, Python, TypeScript).

Le rendu lui-même (débordements, menus, modales, tailles de cibles) se vérifie dans un navigateur ; ces tests
protègent ce qui se casse silencieusement dans les gabarits et les feuilles de style.
"""
import re
from pathlib import Path

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

CSS_DIR = Path(__file__).resolve().parent / "static" / "editor" / "css"
EDITOR_URLS = ("codelab-js", "codelab-py", "codelab-ts")


class EditorTemplatesResponsiveTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user("alice", password="Mot-de-passe-solide-42")
        self.client = Client()
        self.client.force_login(user)

    def html(self, name):
        response = self.client.get(reverse("editor", args=[name]))
        self.assertEqual(response.status_code, 200)
        return response.content.decode()

    def test_editors_declare_viewport_with_safe_areas(self):
        for name in EDITOR_URLS:
            with self.subTest(page=name):
                viewport = re.search(r'<meta name="viewport" content="([^"]+)"', self.html(name)).group(1)
                self.assertIn("width=device-width", viewport)
                self.assertIn("initial-scale=1", viewport)
                self.assertIn("viewport-fit=cover", viewport)      # zones sûres (encoche, barre d'accueil iOS)
                self.assertNotIn("maximum-scale", viewport)         # ne jamais interdire le zoom (accessibilité)
                self.assertNotIn("user-scalable", viewport)

    def test_other_pages_keep_the_default_viewport(self):
        viewport = re.search(r'<meta name="viewport" content="([^"]+)"', self.client.get("/").content.decode()).group(1)
        self.assertEqual(viewport, "width=device-width, initial-scale=1")

    def test_logo_link_has_an_accessible_name_when_the_word_is_hidden(self):
        # Sous 900 px le texte « Éditeur » est masqué : sans aria-label, le lien n'aurait plus de nom.
        for name in EDITOR_URLS:
            with self.subTest(page=name):
                self.assertIn('aria-label="Éditeur : retour à l\'accueil"', self.html(name))

    def test_header_is_shared_by_the_three_editors(self):
        for name in EDITOR_URLS:
            with self.subTest(page=name):
                page = self.html(name)
                for needle in ('class="app-header"', 'class="mode-switch"', 'class="topbar-actions"', "editor/css/layout.css", "editor/css/navigation.css"):
                    self.assertIn(needle, page)


class EditorStylesheetsResponsiveTests(TestCase):
    """Les règles qui évitent les régressions les plus coûteuses à retrouver."""

    def css(self, name):
        return (CSS_DIR / name).read_text(encoding="utf-8")

    def test_body_uses_dynamic_viewport_height(self):
        # 100vh dépasse la zone visible sur mobile (barre d'adresse) : la barre du bas passerait dessous.
        layout = self.css("layout.css")
        self.assertIn("100dvh", layout)
        self.assertRegex(layout, r"min-height:\s*0")

    def test_phone_header_and_menus_have_a_narrow_layout(self):
        self.assertIn("max-width: 599.98px", self.css("layout.css"))
        self.assertIn("max-width: 599.98px", self.css("navigation.css"))

    def test_touch_targets_follow_the_pointer_type(self):
        layout = self.css("layout.css")
        self.assertRegex(layout, r"@media \(pointer: coarse\)\s*\{\s*body\.editor-app\s*\{[^}]*--tap:\s*44px")

    def test_iframe_cannot_overflow_its_container(self):
        # Un <iframe> a une hauteur minimale automatique de 150 px : sans min-height: 0 il recouvre la barre du bas.
        self.assertRegex(self.css("editor.css"), r"#output\s*\{[^}]*min-height:\s*0")

    def test_text_inputs_stay_at_16px_on_touch_screens(self):
        # En dessous, Safari iOS zoome sur le champ à la saisie.
        self.assertRegex(self.css("modal.css"), r"font-size:\s*max\(16px,\s*1em\)")

    def test_modals_never_exceed_the_screen(self):
        self.assertRegex(self.css("modal.css"), r"\.custom-modal\s*\{[^}]*max-height:\s*100%")


class EditorWorkbenchMarkupTests(TestCase):
    """Nouvelle interface : onglets de fichiers, console intégrée, barre d'état et menu Projet dans les trois éditeurs."""

    def setUp(self):
        user = get_user_model().objects.create_user("bob", password="Mot-de-passe-solide-42")
        self.client = Client()
        self.client.force_login(user)

    def html(self, name):
        return self.client.get(reverse("editor", args=[name])).content.decode()

    def test_every_editor_has_the_shared_workbench_parts(self):
        for name in EDITOR_URLS:
            with self.subTest(page=name):
                page = self.html(name)
                for needle in ('class="file-tabs', 'class="console-dock"', 'class="status-bar"', 'class="drop-menu project-menu"',
                               'id="current-project"', 'id="focus-editor"', 'id="restart-btn"', 'id="console"', 'id="run-code"'):
                    self.assertIn(needle, page)

    def test_project_menu_reuses_the_existing_modals(self):
        for name in EDITOR_URLS:
            with self.subTest(page=name):
                page = self.html(name)
                for target in ("#project-controls", "#zip-controls"):
                    self.assertIn(f'data-target="{target}"', page)
                for action in ("new-project", "rename-project", "export-zip", "delete-project"):
                    self.assertIn(f'data-action="{action}"', page)

    def test_preview_editors_keep_auto_preview_and_cdn_controls(self):
        for name in ("codelab-js", "codelab-ts"):
            with self.subTest(page=name):
                page = self.html(name)
                for needle in ('id="live-code"', 'role="switch"', 'id="delay"', 'id="bootstrapCdnSwitch"', 'data-target="#head-controls"',
                               'id="toggle-console"', 'id="console-close"', 'id="reload-preview"'):
                    self.assertIn(needle, page)
                self.assertNotIn('id="display-console"', page)
                self.assertNotIn('id="display-preview"', page)

    def test_console_is_hidden_by_default_and_driven_by_its_own_button(self):
        for name in ("codelab-js", "codelab-ts"):
            with self.subTest(page=name):
                page = self.html(name)
                self.assertIn('id="output-container" aria-label="Résultat" data-view="preview" data-console="closed"', page)
                self.assertIn('id="toggle-console"', page)
                self.assertIn('aria-controls="console-dock"', page)
                self.assertIn('id="console-dock"', page)
        # Aucun autre module n'ouvre la console : seul Workbench.js touche à data-console.
        js_dir = CSS_DIR.parent / "js"
        for path in js_dir.rglob("*.js"):
            if path.name == "Workbench.js":
                continue
            source = path.read_text(encoding="utf-8")
            with self.subTest(script=path.name):
                self.assertNotIn("dataset.console", source)
                self.assertNotIn("showConsole", source)
                self.assertNotIn("setView(", source)

    def test_python_has_no_preview_parts(self):
        page = self.html("codelab-py")
        for needle in ('id="live-code"', 'id="bootstrapCdnSwitch"', 'id="output"'):
            self.assertNotIn(needle, page)
        self.assertIn('id="py-save-state"', page)

    def test_the_file_tabs_keep_the_ids_used_by_the_scripts(self):
        self.assertIn('id="js-tab"', self.html("codelab-js"))
        for tab in ("html-tab", "css-tab", "ts-tab"):
            self.assertIn(f'id="{tab}"', self.html("codelab-ts"))

    def test_console_rows_are_only_restyled_inside_the_editor_dock(self):
        # chrome-console.css est partagé avec les blocs exécutables des cours : l'habillage « heure + niveau » reste confiné.
        editor_css = (CSS_DIR / "editor.css").read_text(encoding="utf-8")
        chrome_css = (CSS_DIR / "chrome-console.css").read_text(encoding="utf-8")
        self.assertIn(".console-dock .cc-row", editor_css)
        self.assertNotIn("data-time", chrome_css)


class EditorNoEmojiAndHeaderTests(TestCase):
    """Aucun emoji / glyphe-symbole dans l'interface de l'éditeur ; l'en-tête passe sur deux lignes sous 1024 px."""

    GLYPHS = re.compile("[\u2190-\u21ff\u2300-\u23ff\u2460-\u27bf\u2900-\u2bff\U0001F000-\U0001FAFF\uFE0F]")

    def test_editor_interface_files_contain_no_emoji_or_symbol_glyph(self):
        root = Path(__file__).resolve().parent
        files = list((root / "templates" / "editor").glob("*.html"))
        files += [p for p in (root / "static" / "editor" / "css").glob("*.css")]
        files += [p for p in (root / "static" / "editor" / "js").rglob("*.js") if "console" not in p.parts]
        for path in files:
            with self.subTest(file=path.name):
                found = self.GLYPHS.findall(path.read_text(encoding="utf-8"))
                self.assertEqual(found, [], f"{path.name} contient des glyphes : {found}")

    def test_header_stacks_on_two_rows_below_1024px(self):
        css = (CSS_DIR / "layout.css").read_text(encoding="utf-8")
        self.assertRegex(css, r"@media \(max-width: 1023\.98px\)\s*\{\s*\.app-header\s*\{[^}]*display:\s*grid")

    def test_page_never_scrolls_horizontally_and_restart_is_not_pushed_out(self):
        layout = (CSS_DIR / "layout.css").read_text(encoding="utf-8")
        editor = (CSS_DIR / "editor.css").read_text(encoding="utf-8")
        self.assertIn("html:has(body.editor-app) { overflow: hidden", layout)
        self.assertNotRegex(editor, r"\.restart\s*\{[^}]*margin-right:\s*-")


class EditorHeaderLayoutTests(TestCase):
    """En-tête : état d'enregistrement sans collision, paramètres et options à l'extrême droite, deux menus identiques."""

    def setUp(self):
        user = get_user_model().objects.create_user("carol", password="Mot-de-passe-solide-42")
        self.client = Client()
        self.client.force_login(user)

    def header(self, name):
        page = self.client.get(reverse("editor", args=[name])).content.decode()
        return re.search(r'<header class="app-header">.*?</header>', page, re.S).group(0)

    def test_settings_and_options_are_the_last_children_of_the_right_group(self):
        for name in EDITOR_URLS:
            with self.subTest(page=name):
                header = self.header(name)
                end = header[header.index('<div class="header-end">'):]
                # ordre dans le groupe de droite : état, paramètres (engrenage), options (•••) — et rien après
                self.assertLess(end.index('class="save-state"'), end.index('drop-project'))
                self.assertLess(end.index('drop-project'), end.index('drop-more'))
                self.assertNotIn('topbar-actions', end)
                # les raccourcis (cours, thème, déconnexion) sont avant le groupe de droite
                self.assertLess(header.index('class="topbar-actions"'), header.index('class="header-end"'))

    def test_options_menu_has_the_same_structure_as_the_settings_menu(self):
        for name in EDITOR_URLS:
            with self.subTest(page=name):
                header = self.header(name)
                menus = re.findall(r'<ul class="drop-menu project-menu" role="menu">(.*?)</ul>', header, re.S)
                self.assertEqual(len(menus), 2, "paramètres et options partagent la même classe de menu")
                for menu in menus:
                    for part in ('class="drop-head"', 'class="drop-sep"', 'class="drop-note"', "<svg"):
                        self.assertIn(part, menu)

    def test_the_title_truncates_instead_of_colliding_with_the_save_state(self):
        css = (CSS_DIR / "layout.css").read_text(encoding="utf-8")
        self.assertRegex(css, r"\.doc-title\s*\{[^}]*overflow:\s*hidden")
        self.assertRegex(css, r"\.doc-rename\s*\{[^}]*flex-shrink:\s*0")
        # Sous 720 px le texte d'état se réduit au point : il ne peut plus passer sous le titre.
        self.assertRegex(css, r"@media \(max-width: 719\.98px\)[^{]*\{\s*\.save-state\s*\{[^}]*font-size:\s*0")
