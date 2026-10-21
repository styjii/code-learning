"""Routes du projet. Toutes exigent une connexion, sauf la page de connexion (voir accounts)."""

from django.contrib import admin
from django.contrib.auth.decorators import login_not_required
from django.urls import include, path
from django.views.decorators.cache import never_cache

from accounts.views import ThrottledLoginView


@never_cache
@login_not_required
def admin_login(request, extra_context=None):
    """Le formulaire de connexion de l'admin est remplacé par le nôtre (avec limitation des tentatives)."""
    return ThrottledLoginView.as_view(redirect_authenticated_user=False)(request)


admin.site.login = admin_login

urlpatterns = [
    path("accounts/", include("accounts.urls")),
    path("admin/", admin.site.urls),
    path("", include("webapp.urls")),
    path("language/", include("language.urls")),
    path("editor/", include("editor.urls")),
]
