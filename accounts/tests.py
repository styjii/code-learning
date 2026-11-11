from unittest import mock

from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.test import Client, TestCase, override_settings
from django.urls import reverse
from django.utils.html import escape

from editor.models import Project

User = get_user_model()
PASSWORD = "Mot-de-passe-solide-42"

# Pages web : redirigées vers la connexion par StrictLoginRequiredMiddleware
PROTECTED = [
    "/",
    "/language/css/",
    "/language/frameworks/django/",
    "/editor/",                  # anciennes adresses : la connexion passe avant la redirection
    "/editor/codelab-js/",
    "/editor/codelab-ts/",
    "/editor/codelab-py/",
]

# Points d'entrée JSON : réponse 401 (sans redirection, inutile pour un fetch())
PROTECTED_API_READ = ["/editor/api/codelab-js/projects/", "/editor/api/codelab-ts/projects/",
                      "/editor/api/codelab-py/projects/", "/editor/api/codelab-js/projects/1/export-zip/",
                      "/editor/api/load-monaco-config/", "/populate-step/?index=0"]
PROTECTED_API_WRITE = ["/editor/api/codelab-js/projects/", "/editor/preview/",
                       "/editor/api/codelab-js/projects/1/import-zip/", "/editor/api/save-monaco-config/"]


class AuthenticationRequiredTests(TestCase):
    """Tout accès sans connexion est refusé : redirection (pages) ou 401 (API)."""

    def test_anonymous_is_redirected_everywhere(self):
        for url in PROTECTED:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 302)
                self.assertTrue(response["Location"].startswith(reverse("login")), response["Location"])

    def test_anonymous_api_is_unauthorized(self):
        for url in PROTECTED_API_READ:
            with self.subTest(method="GET", url=url):
                self.assertEqual(self.client.get(url).status_code, 401)
        for url in PROTECTED_API_WRITE:
            with self.subTest(method="POST", url=url):
                self.assertEqual(self.client.post(url, {}).status_code, 401)

    def test_anonymous_api_response_is_json_with_challenge(self):
        for url in ("/editor/api/codelab-js/projects/", "/populate-step/?index=0"):
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response["Content-Type"], "application/json")
                self.assertTrue(response["WWW-Authenticate"].startswith("Session"))
                self.assertIn("detail", response.json())
                self.assertIn("message", response.json())  # lu par ProgressMain.js

    def test_anonymous_preview_is_not_served(self):
        self.assertEqual(self.client.get("/editor/preview/abcdef/").status_code, 302)

    def test_login_page_is_public(self):
        self.assertEqual(self.client.get(reverse("login")).status_code, 200)

    def test_admin_login_uses_our_form(self):
        response = self.client.get("/admin/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")

    def test_next_is_preserved_and_external_redirect_refused(self):
        User.objects.create_user("ada", password=PASSWORD)
        response = self.client.post(reverse("login") + "?next=/language/css/",
                                    {"username": "ada", "password": PASSWORD, "next": "/language/css/"})
        self.assertRedirects(response, "/language/css/", fetch_redirect_response=False)

        self.client.logout()
        response = self.client.post(reverse("login"), {"username": "ada", "password": PASSWORD,
                                                       "next": "https://evil.example/"})
        self.assertRedirects(response, reverse("index"), fetch_redirect_response=False)


class LoginLogoutTests(TestCase):
    def setUp(self):
        cache.clear()
        self.user = User.objects.create_user("ada", password=PASSWORD)

    def test_login_then_access_then_logout(self):
        response = self.client.post(reverse("login"), {"username": "ada", "password": PASSWORD})
        self.assertRedirects(response, reverse("index"), fetch_redirect_response=False)
        self.assertEqual(self.client.get("/language/css/").status_code, 200)

        # La déconnexion exige POST
        self.assertEqual(self.client.get(reverse("logout")).status_code, 405)
        self.client.post(reverse("logout"))
        self.assertEqual(self.client.get("/language/css/").status_code, 302)

    def test_wrong_password_is_refused(self):
        response = self.client.post(reverse("login"), {"username": "ada", "password": "faux"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.get("/").status_code, 302)

    @override_settings(LOGIN_MAX_ATTEMPTS=3)
    def test_lockout_after_repeated_failures(self):
        for _ in range(3):
            self.assertEqual(self.client.post(reverse("login"), {"username": "ada", "password": "faux"}).status_code, 200)
        # Même avec le bon mot de passe, le compte est bloqué
        response = self.client.post(reverse("login"), {"username": "ada", "password": PASSWORD})
        self.assertEqual(response.status_code, 429)
        self.assertEqual(self.client.get("/").status_code, 302)


    @override_settings(LOGIN_MAX_ATTEMPTS=3)
    def test_lockout_cannot_be_bypassed_with_unicode_variant_of_username(self):
        for _ in range(3):
            self.client.post(reverse("login"), {"username": "ada", "password": "faux"})
        # « ａda » (a pleine chasse) est normalisé en « ada » par le formulaire
        for variant in ("\uff41da", " ada ", "ADA"):
            with self.subTest(variant=variant):
                response = self.client.post(reverse("login"), {"username": variant, "password": PASSWORD})
                self.assertEqual(response.status_code, 429)
                self.assertEqual(self.client.get("/").status_code, 302)

    @override_settings(LOGIN_MAX_ATTEMPTS=3, LOGIN_LOCKOUT_SECONDS=900,
                       CACHES={"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}})
    def test_lockout_lasts_full_duration_from_the_last_failure(self):
        now = [1000.0]
        with mock.patch("time.time", lambda: now[0]):
            self.client.post(reverse("login"), {"username": "ada", "password": "faux"})
            now[0] += 890                       # la limite est atteinte 890 s après le premier échec
            for _ in range(2):
                self.client.post(reverse("login"), {"username": "ada", "password": "faux"})
            now[0] += 20                        # 20 s après le blocage : toujours bloqué
            response = self.client.post(reverse("login"), {"username": "ada", "password": PASSWORD})
            self.assertEqual(response.status_code, 429)
            now[0] += 900                       # blocage écoulé : la connexion est de nouveau possible
            response = self.client.post(reverse("login"), {"username": "ada", "password": PASSWORD})
            self.assertRedirects(response, reverse("index"), fetch_redirect_response=False)


class LoginFormStateTests(TestCase):
    """Champs vides, absence de règle de longueur et état du bouton."""

    def setUp(self):
        cache.clear()
        User.objects.create_user("ada", password=PASSWORD)

    def test_empty_fields_show_explicit_messages(self):
        for data, expected in [
            ({"username": "", "password": ""}, ["Le nom d'utilisateur est obligatoire.", "Le mot de passe est obligatoire."]),
            ({"username": "ada", "password": ""}, ["Le mot de passe est obligatoire."]),
            ({"username": "   ", "password": "x"}, ["Le nom d'utilisateur est obligatoire."]),
        ]:
            with self.subTest(data=data):
                response = self.client.post(reverse("login"), data)
                self.assertEqual(response.status_code, 200)
                for message in expected:
                    # texte réellement affiché sous le champ (et non l'attribut data-* du gabarit)
                    self.assertContains(response, f">{escape(message)}</p>")

    def test_no_length_rule_is_displayed_or_enforced(self):
        response = self.client.get(reverse("login"))
        self.assertNotContains(response, "minlength")
        # 1 caractère : accepté par le formulaire (seule l'authentification échoue, sans message de longueur)
        response = self.client.post(reverse("login"), {"username": "a", "password": "b"})
        self.assertEqual(response.status_code, 200)
        for message in ("Le nom d'utilisateur est obligatoire.", "Le mot de passe est obligatoire."):
            self.assertNotContains(response, f">{escape(message)}</p>")
        for word in ("au moins", "minimum", "trop court", "caractères"):
            self.assertNotContains(response, word)

    @override_settings(LOGIN_MAX_ATTEMPTS=3)
    def test_empty_submissions_do_not_count_as_attempts(self):
        for _ in range(5):
            self.client.post(reverse("login"), {"username": "ada", "password": ""})
        response = self.client.post(reverse("login"), {"username": "ada", "password": PASSWORD})
        self.assertRedirects(response, reverse("index"), fetch_redirect_response=False)

    @override_settings(LOGIN_MAX_ATTEMPTS=3)
    def test_submit_button_is_disabled_once_the_limit_is_reached(self):
        self.assertNotContains(self.client.get(reverse("login")), "disabled")
        for attempt in range(1, 4):
            response = self.client.post(reverse("login"), {"username": "ada", "password": "faux"})
            self.assertEqual(response.status_code, 200)
            if attempt < 3:
                self.assertNotContains(response, 'id="login-submit" disabled')
        # la 3e erreur atteint la limite : le bouton est déjà désactivé dans cette réponse
        self.assertContains(response, 'id="login-submit" disabled')
        self.assertContains(response, "Trop de tentatives")
        self.assertGreater(response.context["lock_seconds"], 0)
        # et il le reste tant que le blocage court
        response = self.client.post(reverse("login"), {"username": "ada", "password": PASSWORD})
        self.assertEqual(response.status_code, 429)
        self.assertContains(response, 'id="login-submit" disabled', status_code=429)


class LockoutCountdownTests(TestCase):
    """Durée de 5 minutes et temps restant affiché à l'utilisateur."""

    def setUp(self):
        cache.clear()
        User.objects.create_user("ada", password=PASSWORD)

    def test_format_remaining(self):
        from accounts.views import format_remaining
        for seconds, expected in [(300, "5 min 00 s"), (299, "4 min 59 s"), (65, "1 min 05 s"), (9, "0 min 09 s"), (0, "0 min 00 s")]:
            with self.subTest(seconds=seconds):
                self.assertEqual(format_remaining(seconds), expected)

    @override_settings(LOGIN_MAX_ATTEMPTS=3, LOGIN_LOCKOUT_SECONDS=300)
    def test_lock_lasts_five_minutes_and_page_shows_the_remaining_time(self):
        for _ in range(3):
            response = self.client.post(reverse("login"), {"username": "ada", "password": "faux"})
        self.assertEqual(response.context["lock_seconds"], 300)
        self.assertEqual(response.context["lock_time"], "5 min 00 s")
        self.assertContains(response, 'class="lock-countdown"')
        self.assertContains(response, "5 min 00 s")
        self.assertContains(response, 'data-lock-seconds="300"')

    @override_settings(LOGIN_MAX_ATTEMPTS=3, LOGIN_LOCKOUT_SECONDS=300,
                       CACHES={"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}})
    def test_remaining_time_decreases_and_lock_ends_after_five_minutes(self):
        now = [1000.0]
        with mock.patch("time.time", lambda: now[0]):
            for _ in range(3):
                self.client.post(reverse("login"), {"username": "ada", "password": "faux"})
            now[0] += 61
            response = self.client.post(reverse("login"), {"username": "ada", "password": PASSWORD})
            self.assertEqual(response.status_code, 429)
            self.assertEqual(response.context["lock_time"], "3 min 59 s")
            self.assertEqual(response.context["lock_seconds"], 239)
            now[0] = 1000 + 301
            response = self.client.post(reverse("login"), {"username": "ada", "password": PASSWORD})
            self.assertRedirects(response, reverse("index"), fetch_redirect_response=False)

    def test_default_lockout_setting_is_five_minutes(self):
        import importlib, os
        from unittest import mock as _mock
        with _mock.patch.dict(os.environ, {"DJANGO_LOGIN_LOCKOUT_SECONDS": ""}):
            import config.settings as settings_module
            reloaded = importlib.reload(settings_module)
            try:
                self.assertEqual(reloaded.LOGIN_LOCKOUT_SECONDS, 300)
            finally:
                importlib.reload(settings_module)


class ProjectIsolationTests(TestCase):
    """Chaque utilisateur ne voit que ses propres projets."""

    def setUp(self):
        self.ada = User.objects.create_user("ada", password=PASSWORD)
        self.bob = User.objects.create_user("bob", password=PASSWORD)
        self.project = Project.objects.create(owner=self.ada, name="secret", data={"html": "<p>x</p>"})

    def test_list_is_scoped(self):
        bob = Client()
        bob.force_login(self.bob)
        self.assertEqual(bob.get("/editor/api/codelab-js/projects/").json(), [])

        ada = Client()
        ada.force_login(self.ada)
        self.assertEqual([p["name"] for p in ada.get("/editor/api/codelab-js/projects/").json()], ["secret"])

    def test_cannot_read_modify_or_delete_foreign_project(self):
        bob = Client()
        bob.force_login(self.bob)
        url = f"/editor/api/codelab-js/projects/{self.project.pk}/"
        self.assertEqual(bob.get(url).status_code, 404)
        self.assertEqual(bob.put(url, {"name": "pwn", "html": "", "css": "", "js": ""},
                                 content_type="application/json").status_code, 404)
        self.assertEqual(bob.delete(url).status_code, 404)
        self.assertTrue(Project.objects.filter(pk=self.project.pk).exists())

    def test_owner_is_forced_and_names_are_unique_per_user(self):
        bob = Client()
        bob.force_login(self.bob)
        payload = {"name": "secret", "html": "", "css": "", "js": "", "owner": self.ada.pk}
        response = bob.post("/editor/api/codelab-js/projects/", payload, content_type="application/json")
        self.assertEqual(response.status_code, 201)          # même nom qu'Ada : autorisé
        self.assertEqual(Project.objects.get(pk=response.json()["id"]).owner, self.bob)
        duplicate = bob.post("/editor/api/codelab-js/projects/", payload, content_type="application/json")
        self.assertEqual(duplicate.status_code, 400)          # doublon chez Bob : refusé

    def test_csrf_is_enforced_for_logged_in_users(self):
        strict = Client(enforce_csrf_checks=True)
        strict.force_login(self.ada)
        response = strict.post("/editor/api/codelab-js/projects/", {"name": "x", "html": "", "css": "", "js": ""},
                               content_type="application/json")
        self.assertEqual(response.status_code, 403)

    def test_preview_is_sandboxed(self):
        ada = Client()
        ada.force_login(self.ada)
        url = ada.post("/editor/preview/", {"html": "<p>a</p>", "css": "", "js": ""}).json()["url"]
        response = ada.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("sandbox", response["Content-Security-Policy"])
