from django.utils.crypto import get_random_string


class ID:
    """Générateur d'identifiants aléatoires (un nouvel identifiant à chaque appel)."""

    def __init__(self, length: int = 16) -> None:
        self.length = length

    def get_id(self) -> str:
        """Retourne un nouvel identifiant aléatoire."""
        return get_random_string(self.length)


# Instance partagée par l'application
id = ID()
