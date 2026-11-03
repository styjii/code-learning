"""Limitation des tentatives : atomicité, cache partagé, IP derrière un proxy, stratégie multi-compteurs."""

import multiprocessing
import os
import unittest
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from unittest import mock

from django.contrib.auth import authenticate, get_user_model
from django.core.cache import cache
from django.core.exceptions import ImproperlyConfigured
from django.test import Client, RequestFactory, SimpleTestCase, TestCase, override_settings
from django.urls import reverse

from accounts import checks
from accounts.netutils import get_client_ip
from accounts.throttle import LoginThrottle
from config.settings import cache_from_url

User = get_user_model()
PASSWORD = "Mot-de-passe-solide-42"
LOGIN = "login"
# Les tests qui simulent l'écoulement du temps (time.time) exigent un cache dont l'expiration suit cette horloge.
LOCMEM = override_settings(CACHES={"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}})
FAST_HASH = override_settings(PASSWORD_HASHERS=["django.contrib.auth.hashers.MD5PasswordHasher"])


# ---------------------------------------------------------------------------------------------------
# 3. IP du client derrière un proxy inverse
# ---------------------------------------------------------------------------------------------------
class ClientIpTests(SimpleTestCase):
    def ip(self, remote, **headers):
        return get_client_ip(RequestFactory().get("/", REMOTE_ADDR=remote, **headers))

    def test_without_proxy_the_header_is_ignored(self):
        self.assertEqual(self.ip("203.0.113.9", HTTP_X_FORWARDED_FOR="1.1.1.1"), "203.0.113.9")

    @override_settings(BEHIND_PROXY=True, TRUSTED_PROXIES=[])
    def test_forwarded_for_is_used_when_the_peer_is_a_trusted_proxy(self):
        self.assertEqual(self.ip("10.0.0.5", HTTP_X_FORWARDED_FOR="198.51.100.7"), "198.51.100.7")
        self.assertEqual(self.ip("127.0.0.1", HTTP_X_FORWARDED_FOR="198.51.100.7"), "198.51.100.7")

    @override_settings(BEHIND_PROXY=True, TRUSTED_PROXIES=[])
    def test_forged_left_entries_are_ignored(self):
        # Le client envoie « 6.6.6.6 » ; le proxy ajoute à droite l'adresse qu'il a réellement vue.
        self.assertEqual(self.ip("10.0.0.5", HTTP_X_FORWARDED_FOR="6.6.6.6, 198.51.100.7"), "198.51.100.7")

    @override_settings(BEHIND_PROXY=True, TRUSTED_PROXIES=[])
    def test_chain_of_trusted_proxies_is_skipped(self):
        self.assertEqual(self.ip("10.0.0.5", HTTP_X_FORWARDED_FOR="198.51.100.7, 10.0.0.9"), "198.51.100.7")

    @override_settings(BEHIND_PROXY=True, TRUSTED_PROXIES=[])
    def test_untrusted_peer_cannot_forge_its_address(self):
        self.assertEqual(self.ip("203.0.113.9", HTTP_X_FORWARDED_FOR="1.1.1.1"), "203.0.113.9")

    @override_settings(BEHIND_PROXY=True, TRUSTED_PROXIES=["203.0.113.0/24"])
    def test_explicit_trusted_proxies_replace_the_defaults(self):
        self.assertEqual(self.ip("203.0.113.9", HTTP_X_FORWARDED_FOR="198.51.100.7"), "198.51.100.7")
        self.assertEqual(self.ip("10.0.0.5", HTTP_X_FORWARDED_FOR="198.51.100.7"), "10.0.0.5")

    @override_settings(BEHIND_PROXY=True, TRUSTED_PROXIES=[], PROXY_IP_HEADER="CF-Connecting-IP")
    def test_single_value_header(self):
        self.assertEqual(self.ip("10.0.0.5", HTTP_CF_CONNECTING_IP="198.51.100.7"), "198.51.100.7")

    @override_settings(BEHIND_PROXY=True, TRUSTED_PROXIES=[])
    def test_unreadable_header_falls_back_to_the_peer(self):
        self.assertEqual(self.ip("10.0.0.5", HTTP_X_FORWARDED_FOR="n'importe quoi"), "10.0.0.5")
        self.assertEqual(self.ip("10.0.0.5"), "10.0.0.5")

    @override_settings(BEHIND_PROXY=True, TRUSTED_PROXIES=[])
    def test_unix_socket_peer_is_the_local_proxy(self):
        self.assertEqual(self.ip("", HTTP_X_FORWARDED_FOR="198.51.100.7"), "198.51.100.7")

    @override_settings(BEHIND_PROXY=True, TRUSTED_PROXIES=[])
    def test_ports_and_ipv4_mapped_addresses_are_normalised(self):
        self.assertEqual(self.ip("10.0.0.5", HTTP_X_FORWARDED_FOR="198.51.100.7:51234"), "198.51.100.7")
        self.assertEqual(self.ip("::ffff:198.51.100.7"), "198.51.100.7")

    def test_ipv6_clients_are_grouped_by_64_prefix(self):
        a = self.ip("2001:db8:1:2:aaaa::1")
        b = self.ip("2001:db8:1:2:bbbb::9")
        c = self.ip("2001:db8:1:3::1")
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)


# ---------------------------------------------------------------------------------------------------
# 4. Cache partagé : configuration et vérifications
# ---------------------------------------------------------------------------------------------------
class CacheConfigTests(SimpleTestCase):
    def test_default_is_local_memory(self):
        self.assertTrue(cache_from_url("")["BACKEND"].endswith("LocMemCache"))

    def test_redis_url(self):
        config = cache_from_url("redis://127.0.0.1:6379/1")
        self.assertTrue(config["BACKEND"].endswith("RedisCache"))
        self.assertEqual(config["LOCATION"], "redis://127.0.0.1:6379/1")

    def test_memcached_url(self):
        config = cache_from_url("memcached://10.0.0.1:11211,10.0.0.2:11211")
        self.assertTrue(config["BACKEND"].endswith("PyMemcacheCache"))
        self.assertEqual(config["LOCATION"], ["10.0.0.1:11211", "10.0.0.2:11211"])

    def test_unknown_scheme_is_rejected(self):
        with self.assertRaises(ImproperlyConfigured):
            cache_from_url("ftp://example.com")

    def _caches(self, backend):
        return override_settings(CACHES={"default": {"BACKEND": backend}})

    def test_dummy_cache_is_an_error(self):
        with self._caches("django.core.cache.backends.dummy.DummyCache"):
            self.assertEqual([m.id for m in checks.check_throttle_cache_is_not_dummy(None)], ["accounts.E001"])

    def test_local_or_non_atomic_caches_are_flagged_for_deployment(self):
        for backend in ("django.core.cache.backends.locmem.LocMemCache",
                        "django.core.cache.backends.filebased.FileBasedCache",
                        "django.core.cache.backends.db.DatabaseCache"):
            with self.subTest(backend=backend), self._caches(backend):
                self.assertEqual([m.id for m in checks.check_throttle_cache_is_shared(None)], ["accounts.W001"])

    def test_shared_atomic_caches_are_accepted(self):
        for backend in ("django.core.cache.backends.redis.RedisCache",
                        "django.core.cache.backends.memcached.PyMemcacheCache"):
            with self.subTest(backend=backend), self._caches(backend):
                self.assertEqual(checks.check_throttle_cache_is_shared(None), [])
                self.assertEqual(checks.check_throttle_cache_is_not_dummy(None), [])


# ---------------------------------------------------------------------------------------------------
# 1. Atomicité : des requêtes simultanées ne dépassent pas la limite
# ---------------------------------------------------------------------------------------------------
@override_settings(LOGIN_MAX_ATTEMPTS=5, LOGIN_MAX_ATTEMPTS_PER_IP=1000, LOGIN_MAX_ATTEMPTS_PER_USERNAME=1000)
class AtomicityTests(SimpleTestCase):
    def setUp(self):
        cache.clear()

    def test_parallel_reservations_never_exceed_the_limit(self):
        with ThreadPoolExecutor(max_workers=32) as pool:
            results = list(pool.map(lambda _: LoginThrottle("203.0.113.1", "ada").reserve(), range(300)))
        self.assertEqual(sum(results), 5)

    def test_rejected_reservations_are_refunded_on_shared_counters(self):
        for _ in range(50):
            LoginThrottle("203.0.113.1", "ada").reserve()
        # Les 45 refus n'ont pas consommé le budget « par IP » : un autre identifiant de la même IP passe.
        self.assertTrue(LoginThrottle("203.0.113.1", "bob").reserve())


@FAST_HASH
class LoginThrottlingTests(TestCase):
    def setUp(self):
        cache.clear()
        User.objects.create_user("ada", password=PASSWORD)

    def post(self, username="ada", password="faux", ip="127.0.0.1", client=None, **extra):
        return (client or self.client).post(reverse(LOGIN), {"username": username, "password": password},
                                            REMOTE_ADDR=ip, **extra)

    # --- 1. atomicité au niveau de la vue ------------------------------------------------------------
    @override_settings(LOGIN_MAX_ATTEMPTS=3)
    def test_blocked_attempts_are_not_even_authenticated(self):
        for _ in range(3):
            self.post()
        with mock.patch("django.contrib.auth.forms.authenticate", wraps=authenticate) as spy:
            response = self.post(password=PASSWORD)
        self.assertEqual(response.status_code, 429)
        spy.assert_not_called()

    @override_settings(LOGIN_MAX_ATTEMPTS=1)
    def test_attempt_is_counted_before_it_is_authenticated(self):
        """Une requête qui arrive pendant l'authentification d'une autre voit déjà sa tentative comptée."""
        inner = []

        def slow_authenticate(request=None, **credentials):
            if not inner:
                inner.append(self.post(password=PASSWORD, client=Client()))  # requête « simultanée »
            return None

        with mock.patch("django.contrib.auth.forms.authenticate", side_effect=slow_authenticate) as fake:
            self.post()
        self.assertEqual(len(inner), 1)
        self.assertEqual(inner[0].status_code, 429)   # refusée alors qu'elle avait le bon mot de passe
        self.assertEqual(fake.call_count, 1)          # et jamais authentifiée

    # --- 2. stratégie IP / identifiant ---------------------------------------------------------------
    @override_settings(LOGIN_MAX_ATTEMPTS=3, LOGIN_MAX_ATTEMPTS_PER_USERNAME=100)
    def test_one_ip_cannot_lock_the_account_for_everyone_else(self):
        for _ in range(3):
            self.post(ip="198.51.100.1")
        self.assertEqual(self.post(password=PASSWORD, ip="198.51.100.1").status_code, 429)
        self.assertEqual(self.post(password=PASSWORD, ip="198.51.100.2").status_code, 302)

    @override_settings(LOGIN_MAX_ATTEMPTS=3, LOGIN_MAX_ATTEMPTS_PER_USERNAME=6)
    def test_changing_ip_does_not_reset_the_account_counter(self):
        for n in range(6):                          # 6 échecs, chacun depuis une IP différente
            self.assertEqual(self.post(ip=f"198.51.100.{n + 1}").status_code, 200)
        response = self.post(password=PASSWORD, ip="203.0.113.77")   # bon mot de passe, IP encore inconnue
        self.assertEqual(response.status_code, 429)

    @override_settings(LOGIN_MAX_ATTEMPTS=3, LOGIN_MAX_ATTEMPTS_PER_USERNAME=6)
    def test_trusted_device_keeps_working_during_a_distributed_attack(self):
        owner = Client()
        self.assertEqual(self.post(password=PASSWORD, ip="192.0.2.10", client=owner).status_code, 302)
        owner.post(reverse("logout"))
        self.assertIn("ld_", "".join(owner.cookies))   # cookie d'appareil de confiance posé

        for n in range(6):                              # attaque distribuée sur « ada »
            self.post(ip=f"198.51.100.{n + 1}", client=Client())

        stranger = self.post(password=PASSWORD, ip="192.0.2.99", client=Client())
        self.assertEqual(stranger.status_code, 429)     # sans cookie : bloqué
        self.assertEqual(self.post(password=PASSWORD, ip="192.0.2.99", client=owner).status_code, 302)

    @override_settings(LOGIN_MAX_ATTEMPTS=3, LOGIN_MAX_ATTEMPTS_PER_USERNAME=100)
    def test_trusted_device_is_still_subject_to_the_strict_limit(self):
        owner = Client()
        self.post(password=PASSWORD, ip="192.0.2.10", client=owner)
        owner.post(reverse("logout"))
        for _ in range(3):
            self.post(ip="192.0.2.10", client=owner)
        self.assertEqual(self.post(password=PASSWORD, ip="192.0.2.10", client=owner).status_code, 429)

    @override_settings(LOGIN_MAX_ATTEMPTS_PER_IP=4)
    def test_one_ip_spraying_many_usernames_is_limited(self):
        for n in range(4):
            self.assertEqual(self.post(username=f"inconnu{n}", ip="198.51.100.5").status_code, 200)
        self.assertEqual(self.post(username="inconnu-encore", ip="198.51.100.5").status_code, 429)
        self.assertEqual(self.post(username="inconnu-encore", ip="198.51.100.6").status_code, 200)

    @override_settings(LOGIN_MAX_ATTEMPTS_PER_IP=3)
    def test_successful_logins_do_not_consume_the_ip_budget(self):
        for _ in range(8):
            self.assertEqual(self.post(password=PASSWORD, ip="198.51.100.5").status_code, 302)
            self.client.post(reverse("logout"))

    @override_settings(LOGIN_MAX_ATTEMPTS_PER_IP=4)
    def test_logging_into_own_account_does_not_reset_the_ip_counter(self):
        self.post(username="a1", ip="198.51.100.5")
        self.post(password=PASSWORD, ip="198.51.100.5")           # « succès » intercalé
        self.client.post(reverse("logout"))
        self.post(username="a2", ip="198.51.100.5")
        self.post(password=PASSWORD, ip="198.51.100.5")
        self.client.post(reverse("logout"))
        self.post(username="a3", ip="198.51.100.5")
        self.post(username="a4", ip="198.51.100.5")                # 4e échec : limite atteinte
        self.assertEqual(self.post(username="a5", ip="198.51.100.5").status_code, 429)

    @LOCMEM
    @override_settings(LOGIN_MAX_ATTEMPTS=3, LOGIN_LOCKOUT_SECONDS=900)
    def test_hammering_a_locked_account_does_not_extend_the_lock(self):
        now = [1000.0]
        with mock.patch("time.time", lambda: now[0]):
            self.post()                             # 1er échec : la fenêtre du compteur court jusqu'à t=1900
            now[0] = 1800
            self.post()
            self.post()                             # limite atteinte à t=1800 : blocage jusqu'à t=2700
            now[0] = 2000                           # le compteur a expiré mais le blocage court encore
            for _ in range(40):
                self.assertEqual(self.post().status_code, 429)   # ne doivent rien incrémenter
            now[0] = 2701                           # blocage terminé : le propriétaire peut se connecter
            self.assertEqual(self.post(password=PASSWORD).status_code, 302)

    # --- 3. proxy inverse ----------------------------------------------------------------------------
    @override_settings(BEHIND_PROXY=True, TRUSTED_PROXIES=[], LOGIN_MAX_ATTEMPTS=3, LOGIN_MAX_ATTEMPTS_PER_USERNAME=100)
    def test_users_behind_the_same_proxy_do_not_share_a_counter(self):
        def via_proxy(client_ip, password):
            return self.post(password=password, ip="10.0.0.2", HTTP_X_FORWARDED_FOR=client_ip)

        for _ in range(3):
            via_proxy("198.51.100.1", "faux")
        self.assertEqual(via_proxy("198.51.100.1", PASSWORD).status_code, 429)
        self.assertEqual(via_proxy("198.51.100.2", PASSWORD).status_code, 302)

    @override_settings(BEHIND_PROXY=True, TRUSTED_PROXIES=[], LOGIN_MAX_ATTEMPTS=3)
    def test_a_forged_header_does_not_help_a_direct_client(self):
        for n in range(3):   # connexion directe (IP publique) : l'en-tête forgé est ignoré
            self.post(ip="203.0.113.50", HTTP_X_FORWARDED_FOR=f"6.6.6.{n}")
        self.assertEqual(self.post(password=PASSWORD, ip="203.0.113.50", HTTP_X_FORWARDED_FOR="6.6.6.99").status_code, 429)


# ---------------------------------------------------------------------------------------------------
# 1 + 4. Plusieurs PROCESSUS (comme des workers gunicorn) : exige un vrai cache partagé.
#   TEST_REDIS_URL=redis://127.0.0.1:6379/15 python manage.py test accounts.test_throttle
# ---------------------------------------------------------------------------------------------------
def _reserve_in_worker(_):
    return LoginThrottle("203.0.113.1", "ada").reserve()


@unittest.skipUnless(os.environ.get("TEST_REDIS_URL"), "définir TEST_REDIS_URL pour tester un cache partagé")
@override_settings(LOGIN_MAX_ATTEMPTS=5, LOGIN_MAX_ATTEMPTS_PER_IP=1000, LOGIN_MAX_ATTEMPTS_PER_USERNAME=1000)
class SharedCacheAcrossProcessesTests(SimpleTestCase):
    def test_workers_share_one_counter(self):
        with override_settings(CACHES={"default": cache_from_url(os.environ["TEST_REDIS_URL"])}):
            cache.clear()
            context = multiprocessing.get_context("fork")
            with ProcessPoolExecutor(max_workers=8, mp_context=context) as pool:
                results = list(pool.map(_reserve_in_worker, range(400)))
            cache.clear()
        self.assertEqual(sum(results), 5)
