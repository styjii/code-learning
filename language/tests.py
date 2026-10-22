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
