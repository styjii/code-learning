"""
Lecture sécurisée d'une archive .zip de projet (index.html, style.css, script.js ou script.ts + tsconfig.json).

Une archive minuscule peut annoncer des centaines de Mo une fois décompressée (« zip bomb »). Les limites
ci-dessous (réglables dans ``settings.py``) sont donc vérifiées AVANT toute décompression, sur les tailles
annoncées par l'archive, puis la lecture elle-même est plafonnée : une taille falsifiée ne contourne rien.
"""

import zipfile
import zlib

from django.conf import settings

from . import python_files


# RuntimeError : archive chiffrée ; NotImplementedError : méthode de compression non gérée.
_ARCHIVE_ERRORS = (zipfile.BadZipFile, zlib.error, EOFError, NotImplementedError, RuntimeError)


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
    return _read_project_files(fileobj, name, ("index.html", "style.css", "script.js"))


def read_typescript_zip(fileobj, name):
    """
    Retourne ``(index_html, style_css, script_ts, tsconfig_json)`` ; une partie absente vaut ``""``.

    Mêmes plafonds et mêmes erreurs que ``read_project_zip``.
    """
    return _read_project_files(fileobj, name, ("index.html", "style.css", "script.ts", "tsconfig.json"))


def _checked_infos(zf):
    """Entrées de l'archive, après vérification du nombre de fichiers et de la taille décompressée annoncée."""
    max_entries = settings.EDITOR_ZIP_MAX_ENTRIES
    max_total = settings.EDITOR_ZIP_MAX_TOTAL_BYTES

    infos = zf.infolist()
    if len(infos) > max_entries:
        raise ZipImportError(f"Archive refusée : plus de {max_entries} fichiers.", 413)
    if sum(info.file_size for info in infos) > max_total:
        raise ZipImportError(
            f"Archive refusée : contenu décompressé supérieur à {format_size(max_total)}.", 413)
    return infos


def _read_text(zf, info, label):
    """Lit une entrée en UTF-8, avec le plafond par fichier (vérifié aussi sur les octets réellement lus)."""
    max_file = settings.EDITOR_ZIP_MAX_FILE_BYTES
    if info.file_size > max_file:
        raise ZipImportError(f"« {label} » dépasse la taille maximale de {format_size(max_file)}.", 413)
    with zf.open(info) as handle:
        data = handle.read(max_file + 1)  # plafonné même si l'en-tête ment sur la taille
    if len(data) > max_file:
        raise ZipImportError(f"« {label} » dépasse la taille maximale de {format_size(max_file)}.", 413)
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        raise ZipImportError(f"« {label} » n'est pas encodé en UTF-8.") from None


def _read_project_files(fileobj, name, filenames):
    """Lit les fichiers demandés (à la racine ou dans le dossier ``name/``), avec tous les plafonds."""
    try:
        with zipfile.ZipFile(fileobj) as zf:
            by_name = {info.filename: info for info in _checked_infos(zf)}

            def read_file(filename):
                info = by_name.get(filename)
                if info is None or info.is_dir():
                    return ""
                return _read_text(zf, info, filename)

            return tuple(read_file(f"{name}/{filename}") or read_file(filename) for filename in filenames)
    except ZipImportError:
        raise
    except _ARCHIVE_ERRORS:
        # RuntimeError : archive chiffrée ; NotImplementedError : méthode de compression non gérée.
        raise ZipImportError("Archive zip invalide ou illisible.") from None


def read_python_zip(fileobj):
    """
    Lit l'archive d'un projet de l'éditeur Python : retourne ``(files, skipped)``.

    - ``files`` : liste de ``{"name", "content"}`` valides (règles de ``python_files.py``), ``main.py`` en premier ;
    - ``skipped`` : messages lisibles pour chaque entrée ignorée (nom invalide, dossier, doublon, trop gros...).

    Un seul dossier racine commun (archive faite à la main depuis un dossier) est ignoré. Les fichiers parasites
    (``__MACOSX/``, ``.DS_Store``...) sont écartés sans bruit. Mêmes plafonds de taille et mêmes erreurs que
    ``read_project_zip`` ; ``ZipImportError`` aussi si aucun fichier n'est importable.
    """
    try:
        with zipfile.ZipFile(fileobj) as zf:
            entries = []
            for info in _checked_infos(zf):
                path = info.filename
                parts = [part for part in path.split("/") if part]
                if info.is_dir() or not parts or _is_junk(parts):
                    continue
                entries.append((parts, info))

            # Un dossier racine unique (« projet/main.py ») est retiré ; sinon les chemins restent tels quels.
            roots = {parts[0] for parts, _ in entries}
            if len(roots) == 1 and all(len(parts) > 1 for parts, _ in entries):
                entries = [(parts[1:], info) for parts, info in entries]

            # main.py d'abord : la limite de fichiers ne doit jamais le faire écarter.
            entries.sort(key=lambda entry: entry[0] != [python_files.MAIN_FILE])

            files, skipped, seen = [], [], set()
            for parts, info in entries:
                name = "/".join(parts)
                error = python_files.filename_error(name) if len(parts) == 1 else "les dossiers ne sont pas gérés"
                if error is None and name.lower() in seen:
                    error = "un fichier de ce nom existe déjà"
                if error is None and len(files) >= python_files.MAX_FILES:
                    error = f"limite de {python_files.MAX_FILES} fichiers atteinte"
                if error is None:
                    try:
                        content = _read_text(zf, info, name)
                    except ZipImportError as exc:
                        if exc.status == 413:
                            raise
                        error = "pas du texte UTF-8"
                    else:
                        content = content.removeprefix("\ufeff")   # BOM ajouté par certains éditeurs Windows
                        if len(content) > python_files.MAX_CHARS:
                            error = f"plus de {python_files.MAX_CHARS:,} caractères".replace(",", " ")
                if error:
                    skipped.append(f"« {name} » : {error}")
                    continue
                seen.add(name.lower())
                files.append({"name": name, "content": content})
    except ZipImportError:
        raise
    except _ARCHIVE_ERRORS:
        raise ZipImportError("Archive zip invalide ou illisible.") from None

    if not files:
        detail = f" ({'; '.join(skipped[:3])})" if skipped else ""
        raise ZipImportError(f"Aucun fichier importable dans l'archive{detail}.")
    return files, skipped


def _is_junk(parts):
    """Fichiers créés par le système (macOS, Windows), jamais du code de l'élève."""
    return "__MACOSX" in parts or parts[-1] in {".DS_Store", "Thumbs.db"} or parts[-1].startswith("._")
