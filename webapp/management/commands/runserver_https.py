"""
``python manage.py runserver_https`` : serveur de développement en HTTPS.

Pourquoi : les navigateurs ne tiennent compte de l'en-tête ``Cross-Origin-Opener-Policy`` (et d'autres
protections comme ``Secure`` sur les cookies) que sur une origine « potentiellement fiable » :
HTTPS, ou ``http://localhost`` / ``http://127.0.0.1``. Une page servie en HTTP sur une adresse du réseau local
(``http://192.168.x.x:8000``) déclenche l'avertissement « The Cross-Origin-Opener-Policy header has been
ignored, because the URL's origin was untrustworthy ».

Deux solutions, au choix :
  1. rester sur ``http://localhost:8000`` (ou 127.0.0.1) avec ``runserver`` ;
  2. servir en HTTPS avec cette commande, y compris sur le réseau local (certificat de développement,
     voir README : « HTTPS en développement »).

Ce serveur sert uniquement au développement : en production, le TLS est terminé par un proxy inverse.
"""
import ssl
from pathlib import Path

from django.conf import settings
from django.contrib.staticfiles.management.commands.runserver import Command as StaticRunserverCommand
from django.core.management.base import CommandError
from django.core.servers.basehttp import WSGIServer

DEFAULT_CERT = Path(settings.BASE_DIR) / "certs" / "dev.pem"
DEFAULT_KEY = Path(settings.BASE_DIR) / "certs" / "dev-key.pem"

MKCERT_HELP = (
    "Générez un certificat de développement avec mkcert (https://github.com/FiloSottile/mkcert) :\n"
    "    mkcert -install\n"
    "    mkdir -p certs\n"
    "    mkcert -cert-file certs/dev.pem -key-file certs/dev-key.pem localhost 127.0.0.1 ::1 <IP-DU-RÉSEAU-LOCAL>\n"
    "puis relancez la commande (ou indiquez --cert et --key)."
)


def make_tls_server_class(cert_file, key_file):
    """Serveur WSGI de Django dont la socket d'écoute parle TLS (1.2 minimum)."""
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(certfile=str(cert_file), keyfile=str(key_file))

    class TLSWSGIServer(WSGIServer):
        def server_bind(self):
            super().server_bind()
            # Poignée de main TLS différée : elle se fait dans le thread de la requête, jamais dans la
            # boucle d'acceptation (un client lent ou muet ne bloque donc pas le serveur).
            self.socket = context.wrap_socket(self.socket, server_side=True, do_handshake_on_connect=False)

        def handle_error(self, request, client_address):
            import sys
            exc = sys.exc_info()[1]
            if isinstance(exc, (ssl.SSLError, ConnectionResetError)):
                # Navigateur qui refuse le certificat, requête HTTP en clair sur le port HTTPS, etc. :
                # sans gravité, pas de trace d'erreur.
                return
            super().handle_error(request, client_address)

    return TLSWSGIServer


class Command(StaticRunserverCommand):
    help = "Serveur de développement en HTTPS (certificat local, par exemple généré avec mkcert)."
    protocol = "https"
    default_port = "8443"

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument("--cert", default=str(DEFAULT_CERT), help="Certificat PEM (défaut : certs/dev.pem).")
        parser.add_argument("--key", default=str(DEFAULT_KEY), help="Clé privée PEM (défaut : certs/dev-key.pem).")

    def handle(self, *args, **options):
        cert, key = Path(options["cert"]), Path(options["key"])
        missing = [str(p) for p in (cert, key) if not p.is_file()]
        if missing:
            raise CommandError(f"Fichier(s) introuvable(s) : {', '.join(missing)}.\n{MKCERT_HELP}")
        try:
            self.server_cls = make_tls_server_class(cert, key)
        except (ssl.SSLError, OSError) as exc:
            raise CommandError(f"Certificat ou clé illisible : {exc}\n{MKCERT_HELP}")
        super().handle(*args, **options)

    def get_handler(self, *args, **options):
        inner = super().get_handler(*args, **options)

        def https_application(environ, start_response):
            # Django se fie à wsgi.url_scheme : sans cela, request.is_secure() serait faux derrière notre
            # socket TLS (redirection HTTPS en boucle, cookies « Secure » refusés).
            environ["wsgi.url_scheme"] = "https"
            environ["HTTPS"] = "on"
            return inner(environ, start_response)

        return https_application
