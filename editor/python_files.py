"""
Règles des fichiers de l'éditeur Python, côté serveur (export et import de .zip).

Ce sont les mêmes que celles du navigateur (``static/editor/js/python/FileStore.js`` : ``validateName``,
``MAX_FILES``, ``MAX_CHARS``). Le serveur les revérifie : une archive ne vient jamais d'une source de confiance,
et un fichier accepté ici l'est aussi par ``FileStore`` à la restauration.
"""
import re

MAX_FILES = 20
MAX_CHARS = 200_000
MAX_NAME_LENGTH = 40
MAIN_FILE = "main.py"

# Un fichier de ce nom masquerait le module standard correspondant et casserait les imports.
STANDARD_MODULES = frozenset({
    "abc", "argparse", "array", "ast", "asyncio", "base64", "bisect", "builtins", "calendar", "collections",
    "copy", "csv", "dataclasses", "datetime", "decimal", "enum", "fractions", "functools", "glob", "hashlib",
    "heapq", "html", "io", "itertools", "json", "logging", "math", "operator", "os", "pathlib", "pickle",
    "queue", "random", "re", "statistics", "string", "struct", "sys", "tempfile", "textwrap", "threading",
    "time", "types", "typing", "unittest", "urllib", "uuid", "warnings",
})

_PYTHON_NAME = re.compile(r"[A-Za-z_][A-Za-z0-9_]*\.py")
_OTHER_NAME = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_.-]*\.[A-Za-z0-9]{1,8}")


def filename_error(name):
    """Message d'erreur (français) si ``name`` n'est pas un nom de fichier valide pour l'éditeur, sinon ``None``."""
    if not isinstance(name, str) or not name:
        return "nom de fichier vide"
    if len(name) > MAX_NAME_LENGTH:
        return f"nom trop long ({MAX_NAME_LENGTH} caractères maximum)"
    if "/" in name or "\\" in name:
        return "les dossiers ne sont pas gérés"
    if name.endswith(".py"):
        if not _PYTHON_NAME.fullmatch(name):
            return "un module Python s'écrit avec des lettres, chiffres et « _ », sans commencer par un chiffre"
        if name[:-3] in STANDARD_MODULES:
            return f"« {name} » masquerait le module standard « {name[:-3]} »"
    elif not _OTHER_NAME.fullmatch(name):
        return "caractères autorisés : lettres, chiffres, « _ », « - » et « . »"
    return None
