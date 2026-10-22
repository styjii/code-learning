"""
Lecture sécurisée d'une archive .zip de projet (index.html, style.css, script.js).

Une archive minuscule peut annoncer des centaines de Mo une fois décompressée (« zip bomb »). Les limites
ci-dessous (réglables dans ``settings.py``) sont donc vérifiées AVANT toute décompression, sur les tailles
annoncées par l'archive, puis la lecture elle-même est plafonnée : une taille falsifiée ne contourne rien.
"""

import zipfile
import zlib

from django.conf import settings


class ZipImportError(Exception):
    """Import refusé. ``status`` est le code HTTP à renvoyer (400 archive invalide, 413 trop volumineuse)."""

    def __init__(self, message, status=400):
        super().__init__(message)
        self.message = message
        self.status = status


def format_size(size):
    """Taille lisible pour les messages d'erreur (« 5 Mo », « 512 Ko »)."""
    if size >= 1024 * 1024:
        return f"{size / (1024 * 1024):g} Mo"
    return f"{max(size // 1024, 1)} Ko"


def read_project_zip(fileobj, name):
    """
    Retourne ``(index_html, style_css, script_js)`` ; une partie absente de l'archive vaut ``""``.

    Lève ``ZipImportError`` si l'archive est invalide, a trop d'entrées, annonce trop de données
    ou contient un fichier trop gros.
    """
    max_entries = settings.EDITOR_ZIP_MAX_ENTRIES
    max_file = settings.EDITOR_ZIP_MAX_FILE_BYTES
    max_total = settings.EDITOR_ZIP_MAX_TOTAL_BYTES

    try:
        with zipfile.ZipFile(fileobj) as zf:
            infos = zf.infolist()
            if len(infos) > max_entries:
                raise ZipImportError(f"Archive refusée : plus de {max_entries} fichiers.", 413)
            if sum(info.file_size for info in infos) > max_total:
                raise ZipImportError(
                    f"Archive refusée : contenu décompressé supérieur à {format_size(max_total)}.", 413)

            by_name = {info.filename: info for info in infos}

            def read_file(filename):
                info = by_name.get(filename)
                if info is None or info.is_dir():
                    return ""
                if info.file_size > max_file:
                    raise ZipImportError(
                        f"« {filename} » dépasse la taille maximale de {format_size(max_file)}.", 413)
                with zf.open(info) as handle:
                    data = handle.read(max_file + 1)  # plafonné même si l'en-tête ment sur la taille
                if len(data) > max_file:
                    raise ZipImportError(
                        f"« {filename} » dépasse la taille maximale de {format_size(max_file)}.", 413)
                try:
                    return data.decode("utf-8")
                except UnicodeDecodeError:
                    raise ZipImportError(f"« {filename} » n'est pas encodé en UTF-8.") from None

            return (
                read_file(f"{name}/index.html") or read_file("index.html"),
                read_file(f"{name}/style.css") or read_file("style.css"),
                read_file(f"{name}/script.js") or read_file("script.js"),
            )
    except ZipImportError:
        raise
    except (zipfile.BadZipFile, zlib.error, EOFError, NotImplementedError, RuntimeError):
        # RuntimeError : archive chiffrée ; NotImplementedError : méthode de compression non gérée.
        raise ZipImportError("Archive zip invalide ou illisible.") from None
