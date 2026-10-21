from django.urls import path

from .config import PAGE_CONFIG
from .views import MarkdownPageView

urlpatterns = [
    path(f"{key}/", MarkdownPageView.as_view(key=key), name=key)
    for key in PAGE_CONFIG
]
