"""Adresse IP du client, y compris derrière un proxy inverse."""

import ipaddress
from functools import lru_cache
from typing import Optional

from django.conf import settings

# Utilisés quand DJANGO_TRUSTED_PROXIES est vide : loopback et réseaux privés.
DEFAULT_TRUSTED_PROXIES = ("127.0.0.0/8", "::1/128", "10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16", "fc00::/7")

IPv6_PREFIX = 64  # un client IPv6 dispose d'un /64 entier : on regroupe par préfixe


def parse_ip(value: str) -> Optional[ipaddress._BaseAddress]:
    """Analyse une IP (avec port éventuel : « 1.2.3.4:5678 », « [::1]:80 »). None si invalide."""
    value = (value or "").strip()
    if not value:
        return None
    if value.startswith("[") and "]" in value:           # [IPv6]:port
        value = value[1:value.index("]")]
    elif value.count(":") == 1 and "." in value:         # IPv4:port
        value = value.split(":", 1)[0]
    try:
        address = ipaddress.ip_address(value.split("%", 1)[0])  # retire un éventuel « %eth0 »
    except ValueError:
        return None
    return address.ipv4_mapped or address if address.version == 6 else address


@lru_cache(maxsize=8)
def _networks(entries: tuple) -> tuple:
    networks = []
    for entry in entries or DEFAULT_TRUSTED_PROXIES:
        try:
            networks.append(ipaddress.ip_network(entry, strict=False))
        except ValueError:
            continue
    return tuple(networks)


def is_trusted_proxy(address: Optional[ipaddress._BaseAddress]) -> bool:
    return address is not None and any(
        address.version == net.version and address in net for net in _networks(tuple(settings.TRUSTED_PROXIES))
    )


def client_key(address: Optional[ipaddress._BaseAddress]) -> str:
    """Forme canonique servant de clé de compteur (IPv6 : préfixe /64)."""
    if address is None:
        return "?"
    if address.version == 6:
        return str(ipaddress.ip_network(f"{address}/{IPv6_PREFIX}", strict=False).network_address) + f"/{IPv6_PREFIX}"
    return str(address)


def get_client_ip(request) -> str:
    """
    Clé d'identification du client pour la limitation des tentatives.

    Sans proxy : ``REMOTE_ADDR``. Avec ``DJANGO_BEHIND_PROXY=1`` : l'en-tête de proxy n'est lu que si la
    connexion TCP provient d'un proxy de confiance (sinon un client pourrait forger l'en-tête et choisir
    son IP). Dans ``X-Forwarded-For``, les entrées de gauche sont fournies par le client et donc falsifiables :
    on remonte depuis la droite en sautant les proxys de confiance ; la première adresse restante est le client.
    """
    remote = request.META.get("REMOTE_ADDR", "")
    peer = parse_ip(remote)

    if not getattr(settings, "BEHIND_PROXY", False):
        return client_key(peer)

    # REMOTE_ADDR vide = socket Unix (gunicorn derrière nginx) : le pair ne peut être que le proxy local.
    if not (is_trusted_proxy(peer) or (peer is None and not remote.strip())):
        return client_key(peer)

    header = "HTTP_" + settings.PROXY_IP_HEADER.upper().replace("-", "_")
    raw = request.META.get(header, "")
    if not raw.strip():
        return client_key(peer)

    if settings.PROXY_IP_HEADER.lower() != "x-forwarded-for":  # en-tête à valeur unique (X-Real-IP, CF-Connecting-IP)
        return client_key(parse_ip(raw) or peer)

    hops = [parse_ip(part) for part in raw.split(",")]
    for hop in reversed(hops):
        if hop is None:               # entrée illisible : on ne peut pas s'y fier
            return client_key(peer)
        if not is_trusted_proxy(hop):
            return client_key(hop)
    return client_key(hops[0] if hops else peer)  # toute la chaîne est interne : le client est à gauche
