"""
Configuration de Monaco : valeurs imposées par l'application + préférences propres à chaque utilisateur.

Le client n'a le droit de modifier que les clés de ``PREFERENCE_RULES`` (liste blanche), avec un type et une
plage vérifiés. Tout le reste (``readOnly``, ``value``, ``theme``, ``scrollbar``...) est refusé à l'écriture
et ignoré à la lecture, même si une valeur invalide avait été stockée.
"""

import copy

# Imposé par l'application : jamais modifiable par l'utilisateur, et prioritaire sur ses préférences.
FIXED_OPTIONS = {
    "automaticLayout": True,
    "contextmenu": False,
    "scrollbar": {"verticalScrollbarSize": 8, "horizontalScrollbarSize": 8},
}

# Valeurs par défaut des préférences modifiables.
DEFAULT_PREFERENCES = {
    "lineNumbers": "on",
    "minimap": {"enabled": True},
    "wordWrap": "off",
    "tabSize": 4,
    "insertSpaces": True,
    "formatOnType": True,
    "formatOnPaste": True,
    "scrollBeyondLastLine": True,
}
# Le thème n'en fait pas partie : il suit celui du site (voir static/js/theme.js), côté navigateur.


def _boolean(value):
    return isinstance(value, bool)


def _choice(*allowed):
    return lambda value: isinstance(value, str) and value in allowed


def _integer(low, high):
    # bool est un sous-type de int en Python : True ne doit pas passer pour 1.
    return lambda value: isinstance(value, int) and not isinstance(value, bool) and low <= value <= high


def _minimap(value):
    return isinstance(value, dict) and set(value) == {"enabled"} and isinstance(value["enabled"], bool)


PREFERENCE_RULES = {
    "lineNumbers": _choice("on", "off", "relative"),
    "minimap": _minimap,
    "wordWrap": _choice("on", "off"),
    "tabSize": _integer(1, 8),
    "insertSpaces": _boolean,
    "formatOnType": _boolean,
    "formatOnPaste": _boolean,
    "scrollBeyondLastLine": _boolean,
}


def validate_preferences(data):
    """
    Vérifie un dictionnaire de préférences envoyé par un client.

    Retourne ``(préférences_valides, erreurs)`` où ``erreurs`` associe chaque clé refusée à un message.
    L'appelant n'enregistre rien dès que ``erreurs`` n'est pas vide.
    """
    if not isinstance(data, dict):
        return {}, {"_": "Objet JSON attendu."}
    clean, errors = {}, {}
    for key, value in data.items():
        rule = PREFERENCE_RULES.get(key)
        if rule is None:
            errors[key] = "Option non autorisée."
        elif not rule(value):
            errors[key] = "Valeur invalide."
        else:
            clean[key] = copy.deepcopy(value)
    return clean, errors


def sanitize_preferences(stored):
    """Filtre ce qui est lu en base : ne garde que les clés et valeurs encore valides."""
    return validate_preferences(stored)[0]


def effective_options(stored=None):
    """Options Monaco complètes d'un utilisateur : défauts, puis ses préférences, puis le réglage imposé."""
    return {
        **copy.deepcopy(DEFAULT_PREFERENCES),
        **sanitize_preferences(stored),
        **copy.deepcopy(FIXED_OPTIONS),
    }
