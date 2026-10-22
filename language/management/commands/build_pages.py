from django.core.management.base import BaseCommand

from language.config import PAGE_CONFIG
from language.services import get_page_html


class Command(BaseCommand):
    help = "Convertit tous les cours Markdown en HTML et les enregistre en base (régénération forcée)."

    def handle(self, *args, **options):
        for key in PAGE_CONFIG:
            get_page_html(key, force=True)
            self.stdout.write(f"Traité et enregistré : {key}")
