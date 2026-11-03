"""Authentification de l'API REST : session Django, mais avec une vraie réponse 401 pour les anonymes."""

from rest_framework.authentication import SessionAuthentication

# Valeur de l'en-tête « WWW-Authenticate » des réponses 401. Le schéma « Session » est volontairement
# inconnu des navigateurs : contrairement à « Basic », il n'ouvre aucune fenêtre de saisie du mot de passe.
API_AUTH_CHALLENGE = 'Session realm="api"'


class SessionAuthentication401(SessionAuthentication):
    """
    ``SessionAuthentication`` de DRF ne définit pas d'en-tête ``WWW-Authenticate`` ; DRF transforme alors
    l'erreur « non authentifié » en **403**. Définir ``authenticate_header`` suffit pour obtenir **401**, le
    code attendu quand les identifiants sont absents (403 reste réservé à un utilisateur connecté sans droit,
    ou à un jeton CSRF invalide).
    """

    def authenticate_header(self, request):
        return API_AUTH_CHALLENGE
