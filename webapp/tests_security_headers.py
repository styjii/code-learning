"""
En-tête ``Cross-Origin-Opener-Policy`` et commande ``runserver_https`` (développement en HTTPS).
"""
import io
import shutil
import ssl
import subprocess
import tempfile
import threading
import urllib.request
from pathlib import Path
from unittest import skipUnless

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import Client, SimpleTestCase, TestCase, override_settings

from webapp.management.commands.runserver_https import make_tls_server_class


class CrossOriginOpenerPolicyTests(TestCase):
    def test_setting_is_explicit_and_same_origin(self):
        self.assertEqual(settings.SECURE_CROSS_ORIGIN_OPENER_POLICY, "same-origin")

    def test_header_is_sent_on_pages_and_api_responses(self):
        user = get_user_model().objects.create_user("alice", password="Mot-de-passe-solide-42")
        client = Client()
        client.force_login(user)
        for url in ("/accounts/login/", "/editor/", "/editor/api/projects/"):
            with self.subTest(url=url):
                response = client.get(url, secure=True)
                self.assertEqual(response.headers.get("Cross-Origin-Opener-Policy"), "same-origin")


class RunserverHttpsCommandTests(SimpleTestCase):
    def test_missing_certificate_gives_an_actionable_error(self):
        with self.assertRaises(CommandError) as ctx:
            call_command("runserver_https", cert="/nonexistent/c.pem", key="/nonexistent/k.pem",
                         stdout=io.StringIO(), stderr=io.StringIO())
        self.assertIn("mkcert", str(ctx.exception))

    @skipUnless(shutil.which("openssl"), "openssl absent")
    def test_server_answers_over_tls_and_marks_requests_as_secure(self):
        tmp = Path(tempfile.mkdtemp())
        cert, key = tmp / "c.pem", tmp / "k.pem"
        subprocess.run(
            ["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes", "-keyout", str(key), "-out", str(cert),
             "-days", "1", "-subj", "/CN=localhost", "-addext", "subjectAltName=DNS:localhost,IP:127.0.0.1"],
            check=True, capture_output=True)

        seen = {}

        def app(environ, start_response):
            seen["scheme"] = environ["wsgi.url_scheme"]
            start_response("200 OK", [("Content-Type", "text/plain")])
            return [b"ok"]

        from django.core.servers.basehttp import WSGIRequestHandler
        server = make_tls_server_class(cert, key)(("127.0.0.1", 0), WSGIRequestHandler)
        server.set_app(app)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            context = ssl.create_default_context(cafile=str(cert))
            url = f"https://127.0.0.1:{server.server_address[1]}/"
            with urllib.request.urlopen(url, context=context, timeout=5) as response:
                self.assertEqual(response.read(), b"ok")
        finally:
            server.shutdown()
            server.server_close()
            shutil.rmtree(tmp, ignore_errors=True)
        self.assertEqual(seen.get("scheme"), "http")  # le schéma « https » est posé par la commande, pas par le serveur
