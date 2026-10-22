import os
import tempfile
from pathlib import Path
from unittest import mock

from django.test import TestCase

from language import services
from language.config import PAGE_CONFIG
from language.models import PageContent


class PageCacheTests(TestCase):
    def setUp(self):
        self.key = next(iter(PAGE_CONFIG))

    def test_page_is_generated_then_served_from_database(self):
        self.assertFalse(PageContent.objects.exists())
        html = services.get_page_html(self.key)
        self.assertTrue(html)
        self.assertEqual(PageContent.objects.get(key=self.key).content, html)

        with mock.patch.object(services, "MarkdownToTabbedHTML") as converter:
            self.assertEqual(services.get_page_html(self.key), html)
            converter.assert_not_called()

    def test_force_regenerates(self):
        services.get_page_html(self.key)
        with mock.patch.object(services, "MarkdownToTabbedHTML") as converter:
            converter.return_value.convert.return_value = "<p>neuf</p>"
            self.assertEqual(services.get_page_html(self.key, force=True), "<p>neuf</p>")
        self.assertEqual(PageContent.objects.get(key=self.key).content, "<p>neuf</p>")
        self.assertEqual(PageContent.objects.filter(key=self.key).count(), 1)

    def test_outdated_signature_triggers_regeneration(self):
        services.get_page_html(self.key)
        PageContent.objects.filter(key=self.key).update(signature="perimee")
        self.assertIn(self.key, services.stale_keys())
        services.get_page_html(self.key)
        self.assertNotIn(self.key, services.stale_keys())

    def test_stale_keys_lists_missing_pages(self):
        self.assertEqual(services.stale_keys(), list(PAGE_CONFIG))

    def test_unknown_key(self):
        with self.assertRaises(KeyError):
            services.get_page_html("inconnue")


class RunnablePagesTests(TestCase):
    """Le bouton « Exécuter » n'existe que dans les cours Python, JavaScript et TypeScript."""

    EXPECTED = {"python", "javascript", "typescript"}

    def test_config_flags(self):
        from language.config import PAGES

        self.assertEqual({k for k, p in PAGES.items() if p.runnable}, self.EXPECTED)

    def test_body_attribute(self):
        from django.contrib.auth import get_user_model
        from django.urls import reverse
        from language.config import PAGES

        get_user_model().objects.create_user("lecteur", password="Mot-de-passe-solide-42")
        self.client.login(username="lecteur", password="Mot-de-passe-solide-42")
        with mock.patch("language.views.get_page_html", return_value="<p>x</p>"):
            for key in PAGES:
                html = self.client.get(reverse(key)).content.decode()
                expected = "true" if key in self.EXPECTED else "false"
                self.assertIn(f'data-runnable="{expected}"', html, key)

    def test_code_blocks_are_read_only_outside_runnable_pages(self):
        from django.contrib.auth import get_user_model
        from django.urls import reverse

        get_user_model().objects.create_user("lecteur2", password="Mot-de-passe-solide-42")
        self.client.login(username="lecteur2", password="Mot-de-passe-solide-42")
        html = (
            '<pre><code class="language-python">print(1)</code></pre>'
            '<pre><code class="language-js" data-run="false">1</code></pre>'
            "<p><code>inline</code></p>"
        )
        with mock.patch("language.views.get_page_html", return_value=html):
            for key in ("modules/python", "exercises/algorithm", "solutions/javascript", "projects/javascript"):
                body = self.client.get(reverse(key)).content.decode()
                self.assertEqual(body.count('data-run="false"'), 2, key)
                self.assertIn("<code>inline</code>", body)
            for key in ("python", "javascript", "typescript"):
                body = self.client.get(reverse(key)).content.decode()
                self.assertEqual(body.count('data-run="false"'), 1, key)  # seul le bloc « norun » d'origine
