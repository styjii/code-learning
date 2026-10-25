"""
Options du compilateur TypeScript de l'éditeur TypeScript : valeurs par défaut, liste blanche, validation.

Même principe que ``monaco_config.py`` : le client ne peut modifier que les clés de ``COMPILER_OPTION_RULES``,
avec un type et une valeur vérifiés. Tout le reste (``outDir``, ``plugins``, ``paths``...) est refusé à
l'écriture et ignoré à la lecture, même si une valeur invalide avait été stockée.

Les options sont propres à chaque projet (comme un ``tsconfig.json``) et sont écrites telles quelles dans
le ``tsconfig.json`` de l'export .zip, puis relues à l'import.
"""

import json

# Cibles proposées. ES2023 manque volontairement : le compilateur embarqué dans Monaco 0.47 ne la connaît pas.
TARGETS = ("ES5", "ES2015", "ES2016", "ES2017", "ES2018", "ES2019", "ES2020", "ES2021", "ES2022", "ESNext")

# Valeurs par défaut des options modifiables (celles d'un projet neuf).
DEFAULT_COMPILER_OPTIONS = {
    "target": "ESNext",
    "strict": True,
    "noImplicitReturns": False,
    "noFallthroughCasesInSwitch": False,
    "noUncheckedIndexedAccess": False,
    "noUnusedLocals": False,
    "noUnusedParameters": False,
    # Vrai : une erreur de type empêche l'exécution (comme la compilation des blocs des cours).
    "noEmitOnError": True,
}

# Imposé par l'application : le script est vérifié et exécuté comme un module (« await » de premier niveau,
# pas de collision avec les noms globaux du DOM). Jamais modifiable, écrit dans le tsconfig.json exporté.
FIXED_COMPILER_OPTIONS = {
    "module": "ESNext",
    "moduleDetection": "force",
}


def _boolean(value):
    return isinstance(value, bool)


def _choice(*allowed):
    return lambda value: isinstance(value, str) and value in allowed


COMPILER_OPTION_RULES = {
    "target": _choice(*TARGETS),
    **{key: _boolean for key, value in DEFAULT_COMPILER_OPTIONS.items() if isinstance(value, bool)},
}

_TARGETS_BY_LOWERCASE = {name.lower(): name for name in TARGETS}


def validate_compiler_options(data):
    """
    Vérifie un dictionnaire d'options envoyé par un client.

    Retourne ``(options_valides, erreurs)`` où ``erreurs`` associe chaque clé refusée à un message.
    L'appelant n'enregistre rien dès que ``erreurs`` n'est pas vide.
    """
    if not isinstance(data, dict):
        return {}, {"_": "Objet JSON attendu."}
    clean, errors = {}, {}
    for key, value in data.items():
        rule = COMPILER_OPTION_RULES.get(key)
        if rule is None:
            errors[key] = "Option non autorisée."
        elif not rule(value):
            errors[key] = "Valeur invalide."
        else:
            clean[key] = value
    return clean, errors


def sanitize_compiler_options(stored):
    """Filtre ce qui est lu en base : ne garde que les clés et valeurs encore valides."""
    return validate_compiler_options(stored)[0]


def effective_compiler_options(stored=None):
    """Options complètes d'un projet : valeurs par défaut, puis ce qui est enregistré (filtré)."""
    return {**DEFAULT_COMPILER_OPTIONS, **sanitize_compiler_options(stored)}


def build_tsconfig(stored=None):
    """Contenu (dictionnaire) du ``tsconfig.json`` exporté avec le projet."""
    options = effective_compiler_options(stored)
    libs = [options["target"], "DOM"]
    if options["target"] != "ES5":
        libs.append("DOM.Iterable")
    return {
        "compilerOptions": {**options, **FIXED_COMPILER_OPTIONS, "lib": libs, "skipLibCheck": True},
        "files": ["script.ts"],
    }


def options_from_tsconfig(text):
    """
    Options reconnues dans le texte d'un ``tsconfig.json`` importé (``{}`` si illisible).

    Seules les clés de la liste blanche sont retenues ; une valeur invalide est ignorée plutôt que de faire
    échouer l'import. Le nom de la cible n'est pas sensible à la casse (``"es2022"`` vaut ``"ES2022"``).
    """
    try:
        compiler_options = json.loads(text).get("compilerOptions", {})
    except (ValueError, AttributeError):
        return {}
    if not isinstance(compiler_options, dict):
        return {}

    clean = {}
    for key, rule in COMPILER_OPTION_RULES.items():
        if key not in compiler_options:
            continue
        value = compiler_options[key]
        if key == "target" and isinstance(value, str):
            value = _TARGETS_BY_LOWERCASE.get(value.lower(), value)
        if rule(value):
            clean[key] = value
    return clean
