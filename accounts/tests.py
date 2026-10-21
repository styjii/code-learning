from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.test import Client, TestCase, override_settings
from django.urls import reverse

from editor.models import Project

User = get_user_model()
PASSWORD = "Mot-de-passe-solide-42"

# Pages web : redirigées vers la connexion par LoginRequiredMiddleware
PROTECTED = [
    "/",
    "/language/css/",
    "/language/frameworks/django/",
    "/editor/",
    "/populate-step/?index=0",
]

# API REST (DRF) : réponse 403 JSON via la permission IsAuthenticated (plus adaptée à fetch())
PROTECTED_API_READ = ["/editor/api/projects/", "/editor/api/load-monaco-config/"]
PROTECTED_API_WRITE = ["/editor/api/projects/", "/editor/preview/", "/editor/api/export-zip/",
                       "/editor/api/import-zip/", "/editor/api/save-monaco-config/"]


class AuthenticationRequiredTests(TestCase):
    """Tout accès sans connexion doit être redirigé vers la page de connexion."""

    def test_anonymous_is_redirected_everywhere(self):
        for url in PROTECTED:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 302)
                self.assertTrue(response["Location"].startswith(reverse("login")), response["Location"])

    def test_anonymous_api_is_forbidden(self):
        for url in PROTECTED_API_READ:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 403)
        for url in PROTECTED_API_WRITE:
            with self.subTest(url=url):
                self.assertEqual(self.client.post(url, {}).status_code, 403)

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


class ProjectIsolationTests(TestCase):
    """Chaque utilisateur ne voit que ses propres projets."""

    def setUp(self):
        self.ada = User.objects.create_user("ada", password=PASSWORD)
        self.bob = User.objects.create_user("bob", password=PASSWORD)
        self.project = Project.objects.create(owner=self.ada, name="secret", html="<p>x</p>")

    def test_list_is_scoped(self):
        bob = Client()
        bob.force_login(self.bob)
        self.assertEqual(bob.get("/editor/api/projects/").json(), [])

        ada = Client()
        ada.force_login(self.ada)
        self.assertEqual([p["name"] for p in ada.get("/editor/api/projects/").json()], ["secret"])

    def test_cannot_read_modify_or_delete_foreign_project(self):
        bob = Client()
        bob.force_login(self.bob)
        url = f"/editor/api/projects/{self.project.pk}/"
        self.assertEqual(bob.get(url).status_code, 404)
        self.assertEqual(bob.put(url, {"name": "pwn", "html": "", "css": "", "js": ""},
                                 content_type="application/json").status_code, 404)
        self.assertEqual(bob.delete(url).status_code, 404)
        self.assertTrue(Project.objects.filter(pk=self.project.pk).exists())

    def test_owner_is_forced_and_names_are_unique_per_user(self):
        bob = Client()
        bob.force_login(self.bob)
        payload = {"name": "secret", "html": "", "css": "", "js": "", "owner": self.ada.pk}
        response = bob.post("/editor/api/projects/", payload, content_type="application/json")
        self.assertEqual(response.status_code, 201)          # même nom qu'Ada : autorisé
        self.assertEqual(Project.objects.get(pk=response.json()["id"]).owner, self.bob)
        duplicate = bob.post("/editor/api/projects/", payload, content_type="application/json")
        self.assertEqual(duplicate.status_code, 400)          # doublon chez Bob : refusé

    def test_csrf_is_enforced_for_logged_in_users(self):
        strict = Client(enforce_csrf_checks=True)
        strict.force_login(self.ada)
        response = strict.post("/editor/api/projects/", {"name": "x", "html": "", "css": "", "js": ""},
                               content_type="application/json")
        self.assertEqual(response.status_code, 403)

    def test_preview_is_sandboxed(self):
        ada = Client()
        ada.force_login(self.ada)
        url = ada.post("/editor/preview/", {"html": "<p>a</p>", "css": "", "js": ""}).json()["url"]
        response = ada.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("sandbox", response["Content-Security-Policy"])
