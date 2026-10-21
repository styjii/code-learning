from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from language.catalog import grouped_catalog
from language.services import stale_keys
from .services import process_language_entry


@require_GET
def populate_step(request):
    """Prépare une page de cours (l'indice est donné par ?index=)."""
    try:
        index = int(request.GET.get("index", -1))
    except ValueError:
        return JsonResponse({"status": "error", "message": "index invalide"}, status=400)

    try:
        return JsonResponse(process_language_entry(index))
    except Exception as error:  # noqa: BLE001 - renvoyé au client pour affichage
        return JsonResponse({"status": "error", "message": str(error)}, status=500)


def index(request):
    """Accueil : catalogue des cours + préparation du contenu si nécessaire."""
    catalog = grouped_catalog()
    return render(request, "webapp/index.html", {
        "catalog": catalog,
        "total_pages": sum(len(group["pages"]) for group in catalog),
        "is_populating": bool(stale_keys()),
    })
