"""
Limitation des tentatives de connexion.

Trois compteurs complémentaires, chacun avec son seuil et sa fenêtre (``LOGIN_LOCKOUT_SECONDS``) :

=========  =========================  ===========================================================
Portée     Clé                        Rôle
=========  =========================  ===========================================================
``pair``   (IP, identifiant)           seuil strict ; un attaquant ne peut bloquer que sa propre IP
``ip``     IP seule                   un même poste qui essaie beaucoup d'identifiants (« spraying »)
``user``   identifiant seul           attaque distribuée sur un compte depuis de nombreuses IP
=========  =========================  ===========================================================

Un compteur par identifiant seul permettrait de bloquer le compte de quelqu'un d'autre depuis n'importe
où. Deux garde-fous limitent ce risque : son seuil est nettement plus haut que celui de ``pair``, et un
**appareil de confiance** (cookie signé posé après une connexion réussie) n'y est pas soumis. L'attaquant,
qui n'a jamais ouvert de session sur ce compte, reste bloqué ; le propriétaire, lui, peut se connecter.
Le seuil ``pair`` reste toujours appliqué, y compris aux appareils de confiance.

Atomicité : chaque tentative est *réservée* (compteurs incrémentés) AVANT d'être authentifiée, avec des
opérations atomiques du cache. Des requêtes simultanées ne peuvent donc pas dépasser la limite : seules les
N premières sont évaluées. Une réservation est remboursée si la tentative réussit (portées ``ip`` et ``user``)
ou si elle est refusée, de sorte que les compteurs mesurent bien des *échecs*.

Le cache doit être partagé entre les processus et fournir un ``incr()`` atomique (Redis, Memcached) ; voir
``DJANGO_CACHE_URL`` et ``accounts/checks.py``.
"""

import hashlib
import math
import sys
import time
import unicodedata
from dataclasses import dataclass
from typing import Dict, List

from django.conf import settings
from django.core.cache import cache

PAIR, IP, USER = "pair", "ip", "user"
DEVICE_EXEMPT = {IP, USER}  # portées dont un appareil de confiance est dispensé (jamais PAIR)

DEVICE_SALT = "accounts.trusted-device"


def normalize_username(raw: str) -> str:
    """Même normalisation que ``UsernameField`` (NFKC, espaces), plus la casse : « ａDA » == « ada »."""
    return unicodedata.normalize("NFKC", raw or "").strip().casefold()[:150]


def _digest(*parts: str) -> str:
    return hashlib.sha256("\0".join(parts).encode("utf-8")).hexdigest()


# --- opérations de compteur --------------------------------------------------------------------------
def _hit(key: str, window: int) -> int:
    """Incrémente de façon atomique le compteur ``key`` (fenêtre fixe de ``window`` secondes)."""
    for _ in range(3):
        if cache.add(key, 1, timeout=window):  # création atomique, avec durée de vie
            return 1
        try:
            count = cache.incr(key)
        except ValueError:  # la clé a expiré entre add() et incr() : on réessaie
            continue
        if count == 1:
            # incr() a lui-même créé la clé, sans durée de vie (Redis : la clé a expiré juste après
            # le test d'existence). Sans correction le compteur ne s'éteindrait jamais.
            cache.touch(key, window)
        return count
    return sys.maxsize  # cache incohérent : on refuse plutôt que de laisser passer


def _refund(key: str) -> None:
    try:
        cache.decr(key)
    except ValueError:  # déjà expiré : rien à rembourser
        pass


@dataclass(frozen=True)
class Scope:
    name: str
    digest: str
    limit: int

    @property
    def counter_key(self) -> str:
        return f"login:count:{self.name}:{self.digest}"

    @property
    def lock_key(self) -> str:
        return f"login:lock:{self.name}:{self.digest}"


class LoginThrottle:
    def __init__(self, ip: str, username: str, trusted_device: bool = False):
        user = normalize_username(username)
        self.trusted_device = trusted_device
        self.scopes: List[Scope] = [
            Scope(PAIR, _digest(ip, user), settings.LOGIN_MAX_ATTEMPTS),
            Scope(IP, _digest(ip), settings.LOGIN_MAX_ATTEMPTS_PER_IP),
            Scope(USER, _digest(user), settings.LOGIN_MAX_ATTEMPTS_PER_USERNAME),
        ]
        self._counts: Dict[str, int] = {}

    # --- état ------------------------------------------------------------------------------------------
    @property
    def _window(self) -> int:
        return settings.LOGIN_LOCKOUT_SECONDS

    def _enforced(self) -> List[Scope]:
        return [s for s in self.scopes if not (self.trusted_device and s.name in DEVICE_EXEMPT)]

    def lock_remaining(self) -> int:
        """Secondes de blocage restantes pour cette requête (0 = non bloquée)."""
        now, remaining = time.time(), 0
        for scope in self._enforced():
            until = cache.get(scope.lock_key)
            if until:
                remaining = max(remaining, 1, math.ceil(float(until) - now))
        return remaining

    def _lock(self, scope: Scope) -> None:
        # add() : un blocage déjà posé n'est jamais prolongé ; il dure LOGIN_LOCKOUT_SECONDS
        # à partir du moment où la limite est atteinte.
        cache.add(scope.lock_key, time.time() + self._window, timeout=self._window)

    # --- cycle d'une tentative -------------------------------------------------------------------------
    def reserve(self) -> bool:
        """
        À appeler avant d'authentifier. Renvoie True si la tentative peut être évaluée.

        Une requête déjà bloquée n'incrémente rien : marteler un compte bloqué ne prolonge donc pas
        le blocage de son propriétaire.
        """
        if self.lock_remaining():
            return False

        enforced = {s.name for s in self._enforced()}
        allowed = True
        for scope in self.scopes:
            count = self._counts[scope.name] = _hit(scope.counter_key, self._window)
            if count > scope.limit:  # des requêtes simultanées ont déjà consommé le quota
                self._lock(scope)
                allowed = allowed and scope.name not in enforced

        if not allowed:  # tentative non évaluée : on rend les réservations qui ne dépassent pas la limite
            for scope in self.scopes:
                if self._counts[scope.name] <= scope.limit:
                    _refund(scope.counter_key)
        return allowed

    def register_failure(self) -> int:
        """Échec d'authentification : pose le blocage dès que la limite est atteinte. Renvoie le temps restant."""
        for scope in self.scopes:
            if self._counts.get(scope.name, 0) >= scope.limit:
                self._lock(scope)
        return self.lock_remaining()

    def register_success(self) -> None:
        for scope in self.scopes:
            if scope.name == PAIR:
                cache.delete(scope.counter_key)  # (IP, identifiant) prouvé légitime : on repart de zéro
            else:
                # Remboursement de la seule réservation de cette tentative. Un succès ne remet JAMAIS à zéro
                # un compteur partagé : sinon un attaquant alternerait ses essais avec une connexion à son
                # propre compte pour effacer l'historique de ses échecs.
                _refund(scope.counter_key)


# --- appareil de confiance -----------------------------------------------------------------------------
def _device_cookie(username: str) -> str:
    return "ld_" + _digest(normalize_username(username))[:16]


def is_trusted_device(request, username: str) -> bool:
    if not normalize_username(username):
        return False
    return request.get_signed_cookie(
        _device_cookie(username), default=None, salt=DEVICE_SALT,
        max_age=settings.LOGIN_TRUSTED_DEVICE_DAYS * 86400,
    ) == "1"


def trust_device(response, username: str) -> None:
    """Pose le cookie signé après une connexion réussie (lié à cet identifiant par son nom et sa signature)."""
    if not normalize_username(username):
        return
    response.set_signed_cookie(
        _device_cookie(username), "1", salt=DEVICE_SALT,
        max_age=settings.LOGIN_TRUSTED_DEVICE_DAYS * 86400,
        secure=settings.SESSION_COOKIE_SECURE, httponly=True, samesite="Lax",
    )
