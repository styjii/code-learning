"""
Garde-fou « authentification obligatoire » : ces tests échouent si une route devient accessible sans connexion.

- ``test_every_route_denies_anonymous`` parcourt **automatiquement toutes les routes** du projet (y compris
  celles ajoutées plus tard) : une nouvelle route publique doit être déclarée ici, en connaissance de cause.
- Les autres tests utilisent un jeu de routes dédié (``urlpatterns`` ci-dessous) pour vérifier les cas limites.
"""

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.test import RequestFactory, TestCase, override_settings
from django.urls import URLResolver, get_resolver, include, path
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.decorators import public_endpoint
from accounts.middleware import StrictLoginRequiredMiddleware

User = get_user_model()

# Seules routes volontairement accessibles sans connexion (page de connexion et connexion de l'admin).
PUBLIC_ROUTES = {"accounts/login/", "admin/login/"}


def iter_routes(patterns, prefix=""):
    for pattern in patterns:
        route = prefix + str(pattern.pattern)
        if isinstance(pattern, URLResolver):
            yield from iter_routes(pattern.url_patterns, route)
        else:
            yield route, pattern.callback


class EveryRouteTests(TestCase):
    def test_middleware_is_installed_after_authentication(self):
        middleware = settings.MIDDLEWARE
        self.assertIn("accounts.middleware.StrictLoginRequiredMiddleware", middleware)
        self.assertNotIn("django.contrib.auth.middleware.LoginRequiredMiddleware", middleware)
        self.assertLess(
            middleware.index("django.contrib.auth.middleware.AuthenticationMiddleware"),
            middleware.index("accounts.middleware.StrictLoginRequiredMiddleware"),
        )

    def test_every_route_denies_anonymous(self):
        middleware = StrictLoginRequiredMiddleware(lambda request: HttpResponse())
        request = RequestFactory().get("/")
        request.user = AnonymousUser()

        routes = list(iter_routes(get_resolver().url_patterns))
        self.assertGreater(len(routes), 30, "le parcours des routes ne trouve presque rien")

        reachable = {
            route for route, callback in routes
            if middleware.process_view(request, callback, (), {}) is None
        }
        self.assertEqual(
            reachable, PUBLIC_ROUTES,
            "Routes accessibles sans connexion différentes de celles attendues. Si l'ouverture est voulue, "
            "ajoutez la route à PUBLIC_ROUTES ; sinon, retirez @login_not_required / @public_endpoint.",
        )


# --- Jeu de routes dédié aux cas limites -------------------------------------------------------------------
class OpenAPIView(APIView):
    """Erreur typique : vue DRF « ouverte » (aucune authentification, tout le monde autorisé)."""
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"ok": True})


def page(request):
    return HttpResponse("page")


def public_page(request):
    return HttpResponse("public")


urlpatterns = [
    path("accounts/", include("accounts.urls")),  # fournit la route « login » vers laquelle on redirige
    path("open-api/", OpenAPIView.as_view()),
    path("public-api/", public_endpoint(OpenAPIView.as_view())),
    path("page/", page),
    path("public-page/", public_endpoint(public_page)),
]


@override_settings(ROOT_URLCONF=__name__)
class EdgeCaseTests(TestCase):
    def test_drf_view_with_allowany_is_still_blocked(self):
        response = self.client.get("/open-api/")
        self.assertEqual(response.status_code, 401)

    def test_explicitly_public_views_are_reachable(self):
        self.assertEqual(self.client.get("/public-api/").status_code, 200)
        self.assertEqual(self.client.get("/public-page/").status_code, 200)

    def test_browser_is_redirected_and_json_client_gets_401(self):
        response = self.client.get("/page/", headers={"Accept": "text/html,application/xhtml+xml,*/*;q=0.8"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response["Location"].startswith("/accounts/login/"))
        self.assertIn("next=/page/", response["Location"])

        self.assertEqual(self.client.get("/page/", headers={"Accept": "application/json"}).status_code, 401)
        self.assertEqual(self.client.get("/page/", headers={"X-Requested-With": "XMLHttpRequest"}).status_code, 401)

    def test_every_http_method_is_refused(self):
        for method in ("get", "post", "put", "patch", "delete"):
            with self.subTest(method=method):
                response = getattr(self.client, method)("/page/")
                self.assertEqual(response.status_code, 302)

    def test_unauthorized_response_is_never_cached(self):
        response = self.client.get("/open-api/")
        self.assertIn("no-store", response["Cache-Control"])

    def test_authenticated_user_gets_through(self):
        self.client.force_login(User.objects.create_user("ada", password="Mot-de-passe-solide-42"))
        self.assertEqual(self.client.get("/page/").status_code, 200)
        self.assertEqual(self.client.get("/open-api/").status_code, 200)


@override_settings(ROOT_URLCONF="editor.urls")
class DrfSecondBarrierTests(TestCase):
    """Même sans le middleware, DRF répond 401 (et non 403) à un anonyme."""

    def test_401_without_the_middleware(self):
        middleware = [m for m in settings.MIDDLEWARE if m != "accounts.middleware.StrictLoginRequiredMiddleware"]
        with override_settings(MIDDLEWARE=middleware):
            response = self.client.get("/api/projects/")
        self.assertEqual(response.status_code, 401)
        self.assertTrue(response["WWW-Authenticate"].startswith("Session"))
