"""
Noms des projets créés par un import .zip.

Par défaut, le projet importé porte le nom du fichier (sans ``.zip``). Si ce nom est inutilisable (vide, trop long pour
la base, caractères de contrôle), le projet reçoit un nom de secours unique, ``projet-import-{id du projet}``.
"""
from .models import Project

MAX_NAME_LENGTH = Project._meta.get_field("name").max_length
FALLBACK_PREFIX = "projet-import-"


def clean_name(raw):
    """Le nom nettoyé (espaces de début et de fin retirés), ou ``None`` s'il est invalide."""
    if not isinstance(raw, str):
        return None
    name = raw.strip()
    if not name or len(name) > MAX_NAME_LENGTH:
        return None
    if any(ord(char) < 32 or ord(char) == 127 for char in name):
        return None
    return name


def stem_of(filename):
    """Nom du fichier sans son extension ``.zip`` (casse ignorée)."""
    name = (filename or "").replace("\\", "/").rsplit("/", 1)[-1]
    return name[:-4] if name.lower().endswith(".zip") else name


def name_from_filename(filename):
    """Nom du projet pour ce fichier .zip, ou ``None`` s'il est invalide ou trop long (nom de secours à utiliser)."""
    return clean_name(stem_of(filename))


def fallback_name(owner, editor, pk):
    """``projet-import-{pk}``, rendu unique si l'utilisateur a déjà un projet de ce nom dans cet éditeur."""
    taken = set(Project.objects.filter(owner=owner, editor=editor, name__startswith=FALLBACK_PREFIX)
                .values_list("name", flat=True))
    name, n = f"{FALLBACK_PREFIX}{pk}", 2
    while name in taken:
        name, n = f"{FALLBACK_PREFIX}{pk}-{n}", n + 1
    return name
