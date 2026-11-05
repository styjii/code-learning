"""
Service de langage Python de l'éditeur : détection d'erreurs, autocomplétion, survol et aide aux appels.

Ce module s'exécute dans un Pyodide dédié (voir python-language.worker.js), jamais dans celui qui exécute
le programme de l'utilisateur. Il s'appuie sur :

- ``ast`` et ``pyflakes`` : erreurs de syntaxe, noms non définis, imports ou variables inutilisés ;
- ``jedi`` : analyse statique pour l'autocomplétion, les infobulles et les signatures de fonctions.

Chaque fonction publique prend du texte et des nombres, et renvoie du JSON sous forme de texte : rien ne
traverse la frontière Python/JavaScript sous forme d'objet Python, et aucune exception n'en sort.

Conventions de position, celles de Monaco : lignes et colonnes **à partir de 1**, colonnes comptées en
unités UTF-16 (comme les chaînes JavaScript). Python compte en points de code et ``ast`` en octets UTF-8 :
les conversions sont faites ici, sinon les accents et les émojis décaleraient les soulignements.
"""

import ast
import inspect
import json
import keyword
import os
import re
import sys

import jedi
from jedi.api.environment import InterpreterEnvironment
from pyflakes.checker import Checker

PROJECT_DIR = "/project"
MAIN_FILE = "main.py"
MAX_COMPLETIONS = 200
MAX_DOC_CHARS = 1200
MAX_DOC_LINES = 14

# Dossiers où l'on a installé les outils eux-mêmes (jedi, parso, pyflakes) : le programme de l'utilisateur
# ne peut pas les importer, donc ils ne doivent jamais apparaître dans les suggestions.
HIDDEN_PATHS = {"/opt/lsp"}

_SAFE_NAME = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_.\-]*\Z")
_IDENTIFIER = re.compile(r"\w+")


# --------------------------------------------------------------------------------------------------------------
# Positions
# --------------------------------------------------------------------------------------------------------------
def _split_lines(source):
    """Découpe comme Monaco (\\n ou \\r\\n uniquement), contrairement à ``str.splitlines``."""
    return [line[:-1] if line.endswith("\r") else line for line in source.split("\n")]


def _cp_to_u16(text, index):
    """Index en points de code -> index en unités UTF-16."""
    return len(text[:index].encode("utf-16-le", "surrogatepass")) // 2


def _u16_to_cp(text, units):
    """Index en unités UTF-16 -> index en points de code."""
    seen = 0
    for index, char in enumerate(text):
        if seen >= units:
            return index
        seen += 2 if ord(char) > 0xFFFF else 1
    return len(text)


def _byte_to_u16(text, offset):
    """Décalage en octets UTF-8 (``ast``) -> index en unités UTF-16."""
    return _cp_to_u16(text, len(text.encode("utf-8")[:offset].decode("utf-8", "ignore")))


def _line_text(lines, number):
    return lines[number - 1] if 1 <= number <= len(lines) else ""


# --------------------------------------------------------------------------------------------------------------
# Détection d'erreurs
# --------------------------------------------------------------------------------------------------------------
# Traductions des messages de pyflakes, par nom de classe. Le texte reçoit message_args ({0}, {1}).
_PYFLAKES_FR = {
    "UnusedImport": "« {0} » est importé mais jamais utilisé",
    "UnusedVariable": "La variable « {0} » reçoit une valeur mais n'est jamais utilisée",
    "UnusedAnnotation": "La variable « {0} » est annotée mais jamais utilisée",
    "UndefinedName": "Nom non défini : « {0} »",
    "UndefinedExport": "« {0} » figure dans __all__ mais n'est pas défini",
    "UndefinedLocal": "La variable locale « {0} » est utilisée avant d'être assignée",
    "RedefinedWhileUnused": "« {0} » est redéfini sans avoir été utilisé (première définition : ligne {1})",
    "ImportShadowedByLoopVar": "L'import « {0} » (ligne {1}) est masqué par une variable de boucle",
    "ImportStarUsed": "« from {0} import * » empêche de repérer les noms non définis : préférez des imports explicites",
    "ImportStarUsage": "« {0} » est peut-être non défini, ou vient d'un « import * » ({1})",
    "ImportStarNotPermitted": "« from {0} import * » n'est autorisé qu'au niveau du module",
    "DuplicateArgument": "Argument « {0} » en double dans la définition de la fonction",
    "ReturnOutsideFunction": "« return » en dehors d'une fonction",
    "YieldOutsideFunction": "« yield » en dehors d'une fonction",
    "ContinueOutsideLoop": "« continue » en dehors d'une boucle",
    "BreakOutsideLoop": "« break » en dehors d'une boucle",
    "DefaultExceptNotLast": "« except: » sans type doit être le dernier gestionnaire",
    "IfTuple": "« if » sur un tuple : la condition est toujours vraie (virgule en trop ?)",
    "AssertTuple": "« assert » sur un tuple : l'assertion est toujours vraie (parenthèses en trop ?)",
    "IsLiteral": "Comparez à un littéral avec « == » ou « != », pas avec « is »",
    "RaiseNotImplemented": "Utilisez « raise NotImplementedError » (et non « NotImplemented »)",
    "FStringMissingPlaceholders": "f-string sans champ de remplacement : le « f » est inutile",
}

# Erreurs probables à l'exécution ; tout le reste de pyflakes est un avertissement.
_PYFLAKES_ERRORS = {
    "UndefinedName", "UndefinedExport", "UndefinedLocal", "DuplicateArgument", "ReturnOutsideFunction",
    "YieldOutsideFunction", "ContinueOutsideLoop", "BreakOutsideLoop", "DefaultExceptNotLast",
    "TwoStarredExpressions", "TooManyExpressionsInStarredAssignment", "ForwardAnnotationSyntaxError",
    "LateFutureImport", "FutureFeatureNotDefined", "ImportStarNotPermitted", "InvalidPrintSyntax",
}
# Affichés « grisés » dans l'éditeur plutôt que soulignés.
_PYFLAKES_UNUSED = {"UnusedImport", "UnusedVariable", "UnusedAnnotation"}

_STATEMENTS = {"function definition": "la définition de fonction", "class definition": "la définition de classe"}
_TARGETS = {"literal": "un littéral", "function call": "un appel de fonction", "expression": "une expression",
            "comparison": "une comparaison"}


def _statement(name):
    match = re.fullmatch(r"'(\w+)' statement", name)
    return f"l'instruction « {match.group(1)} »" if match else _STATEMENTS.get(name, name)


# (motif de Python 3.14, gabarit français ; {0}, {1} = groupes capturés, déjà traduits par la fonction éventuelle)
_SYNTAX_FR = [
    (r"invalid syntax", "syntaxe invalide", None),
    (r"invalid syntax\. Perhaps you forgot a comma\?", "syntaxe invalide : virgule oubliée ?", None),
    (r"invalid syntax\. Maybe you meant '==' or ':=' instead of '='\?",
     "syntaxe invalide : vouliez-vous écrire « == » (comparaison) à la place de « = » (affectation) ?", None),
    (r"expected '(.+)'", "« {0} » attendu", None),
    (r"Expected one or more names after 'import'", "au moins un nom est attendu après « import »", None),
    (r"unexpected indent", "indentation inattendue", None),
    (r"unindent does not match any outer indentation level",
     "ce retrait ne correspond à aucun niveau d'indentation précédent", None),
    (r"inconsistent use of tabs and spaces in indentation",
     "mélange de tabulations et d'espaces dans l'indentation", None),
    (r"expected an indented block after (.+) on line (\d+)", "bloc indenté attendu après {0} (ligne {1})", (_statement,)),
    (r"unterminated string literal \(detected at line (\d+)\)", "chaîne de caractères non terminée (détectée ligne {0})", None),
    (r"unterminated triple-quoted string literal \(detected at line (\d+)\)",
     "chaîne entre triples guillemets non terminée (détectée ligne {0})", None),
    (r"'(.)' was never closed", "« {0} » n'est jamais refermé", None),
    (r"unmatched '(.)'", "« {0} » n'a pas de correspondance", None),
    (r"closing parenthesis '(.)' does not match opening parenthesis '(.)'", "« {0} » ne correspond pas à « {1} »", None),
    (r"Missing parentheses in call to '(\w+)'\. Did you mean (.+)\?",
     "parenthèses manquantes dans l'appel à « {0} » : écrivez {1}", None),
    (r"cannot assign to (.+) here\. Maybe you meant '==' instead of '='\?",
     "on ne peut pas affecter une valeur à {0} : vouliez-vous écrire « == » ?", (lambda t: _TARGETS.get(t, t),)),
    (r"cannot assign to (.+)", "on ne peut pas affecter une valeur à {0}", (lambda t: _TARGETS.get(t, t),)),
    (r"positional argument follows keyword argument", "un argument positionnel ne peut pas suivre un argument nommé", None),
    (r"expected 'except' or 'finally' block", "bloc « except » ou « finally » attendu", None),
    (r"invalid decimal literal", "nombre invalide (un nom ne peut pas commencer par un chiffre)", None),
    (r"invalid character '(.)' \(U\+([0-9A-Fa-f]+)\)", "caractère invalide « {0} » (U+{1})", None),
    (r"f-string: expecting '=', or '!', or ':', or '}'", "f-string : « = », « ! », « : » ou « }} » attendu", None),
    (r"unexpected EOF while parsing", "fin de fichier inattendue", None),
    (r"EOL while scanning string literal", "chaîne de caractères non terminée", None),
]


def _translate_syntax(message):
    for pattern, french, converters in _SYNTAX_FR:
        match = re.fullmatch(pattern, message)
        if match:
            groups = list(match.groups())
            for index, convert in enumerate(converters or ()):
                groups[index] = convert(groups[index])
            try:
                return french.format(*groups)
            except (IndexError, KeyError, ValueError):
                break
    return message


def _diagnostic(line, col, end_line, end_col, severity, message, code, unused=False):
    return {"line": line, "col": col, "endLine": end_line, "endCol": end_col,
            "severity": severity, "message": message, "code": code, "unused": unused}


def _syntax_diagnostic(exc, lines):
    line = max(exc.lineno or 1, 1)
    text = _line_text(lines, line)
    start = max((exc.offset or 1) - 1, 0)
    end_line = exc.end_lineno or line
    end = (exc.end_offset - 1) if (exc.end_offset and end_line == line) else len(text)

    first, last = _cp_to_u16(text, start), _cp_to_u16(text, end)
    if last <= first:                      # erreur en fin de ligne (« : » oublié...) : on souligne le dernier caractère
        width = _cp_to_u16(text, len(text))
        first, last = (max(width - 1, 0), width) if first >= width and width else (first, first + 1)
    label = "Erreur d'indentation" if isinstance(exc, IndentationError) else "Erreur de syntaxe"
    message = f"{label} : {_translate_syntax(exc.msg or 'syntaxe invalide')}"
    return _diagnostic(line, first + 1, line, last + 1, "error", message, "SyntaxError")


def _node_spans(tree):
    """Pour chaque position de départ, l'étendue du plus petit nœud qui y commence."""
    spans = {}
    for node in ast.walk(tree):
        if getattr(node, "end_lineno", None) is None:
            continue
        key = (node.lineno, node.col_offset)
        size = (node.end_lineno - node.lineno, node.end_col_offset - node.col_offset)
        if key not in spans or size < spans[key][0]:
            spans[key] = (size, node.end_lineno, node.end_col_offset)
    return spans


class _StripTopLevelAwait(ast.NodeTransformer):
    """Pyodide exécute le programme avec « await » permis au niveau du module, mais pyflakes le signale et
    abandonne alors l'analyse de l'expression : un import utilisé seulement là passerait pour inutilisé.
    On remplace donc ``await x`` par ``x`` hors de toute fonction avant de lui confier l'arbre."""

    def __init__(self):
        self.depth = 0

    def _in_function(self, node):
        self.depth += 1
        self.generic_visit(node)
        self.depth -= 1
        return node

    visit_FunctionDef = visit_AsyncFunctionDef = visit_Lambda = _in_function

    def visit_Await(self, node):
        self.generic_visit(node)
        return node.value if self.depth == 0 else node


def _pyflakes_message(message, name):
    template = _PYFLAKES_FR.get(name)
    if template:
        try:
            return template.format(*message.message_args)
        except (IndexError, KeyError, ValueError):
            pass
    try:
        return message.message % message.message_args
    except (TypeError, ValueError):
        return message.message


def lint(source, filename=MAIN_FILE):
    """Liste de diagnostics (JSON) : erreur de syntaxe, ou avertissements/erreurs de pyflakes."""
    try:
        return json.dumps(_lint(source, filename))
    except Exception as exc:  # noqa: BLE001 - un bug d'analyse ne doit jamais remonter jusqu'à l'éditeur
        print(f"lint: {exc!r}", file=sys.stderr)
        return "[]"


def _lint(source, filename):
    lines = _split_lines(source)
    try:
        tree = ast.parse(source, filename)
    except SyntaxError as exc:
        return [_syntax_diagnostic(exc, lines)]
    except (ValueError, RecursionError, MemoryError):
        return []

    spans = _node_spans(tree)
    try:
        messages = Checker(_StripTopLevelAwait().visit(tree), filename=filename).messages
    except RecursionError:
        return []

    result = []
    for message in sorted(messages, key=lambda m: (m.lineno, m.col)):
        name = type(message).__name__
        key = (message.lineno, message.col)
        text = _line_text(lines, message.lineno)
        start = _byte_to_u16(text, message.col)
        _, end_line, end_col = spans.get(key, (None, message.lineno, None))
        if end_col is not None and end_line == message.lineno:
            end = _byte_to_u16(text, end_col)
        else:                              # nœud sur plusieurs lignes : on souligne sa première ligne
            end = _cp_to_u16(text, len(text.rstrip()))
        if end <= start:
            end = start + 1

        severity = "error" if name in _PYFLAKES_ERRORS else "warning"
        result.append(_diagnostic(message.lineno, start + 1, message.lineno, end + 1, severity,
                                  _pyflakes_message(message, name), name, name in _PYFLAKES_UNUSED))
    return result


# --------------------------------------------------------------------------------------------------------------
# Jedi : projet, autocomplétion, survol, signatures
# --------------------------------------------------------------------------------------------------------------
class _Environment(InterpreterEnvironment):
    """Environnement de jedi : le Pyodide courant, sans subprocess (indisponible dans le navigateur),
    et sans les dossiers des outils d'analyse."""

    def get_sys_path(self):
        return [path for path in sys.path if path not in HIDDEN_PATHS]


_environment = _Environment()
_project = None


def _get_project():
    global _project
    if _project is None:
        os.makedirs(PROJECT_DIR, exist_ok=True)
        _project = jedi.Project(PROJECT_DIR)
    return _project


def sync_project(payload):
    """Dépose les fichiers du projet pour que jedi résolve ``import utils`` ou ``from utils import f``.

    ``payload`` : ``{"files": {nom: contenu}, "remove": [nom, ...]}`` (uniquement les changements)."""
    try:
        data = json.loads(payload)
        os.makedirs(PROJECT_DIR, exist_ok=True)
        for name in data.get("remove", []):
            if _SAFE_NAME.match(name):
                try:
                    os.remove(os.path.join(PROJECT_DIR, name))
                except FileNotFoundError:
                    pass
        for name, content in data.get("files", {}).items():
            if _SAFE_NAME.match(name):
                with open(os.path.join(PROJECT_DIR, name), "w", encoding="utf-8", newline="") as handle:
                    handle.write(content)
    except Exception as exc:  # noqa: BLE001 - ne jamais lever vers JavaScript
        print(f"sync_project: {exc!r}", file=sys.stderr)


def _script(source, filename):
    name = filename if _SAFE_NAME.match(filename or "") else MAIN_FILE
    return jedi.Script(source, path=os.path.join(PROJECT_DIR, name), project=_get_project(), environment=_environment)


def _cursor(source, line, column):
    """Position de Monaco (1, UTF-16) -> position de jedi (ligne 1, colonne en points de code à partir de 0)."""
    text = _line_text(_split_lines(source), line)
    return line, _u16_to_cp(text, max(column - 1, 0)), text


def _clip(doc):
    doc = (doc or "").strip().replace("```", "'''")
    lines = doc.splitlines()
    clipped = len(lines) > MAX_DOC_LINES or len(doc) > MAX_DOC_CHARS
    doc = "\n".join(lines[:MAX_DOC_LINES])[:MAX_DOC_CHARS].rstrip()
    return doc + "\n…" if clipped else doc


def _in_comment(before_cursor):
    """Le curseur est-il dans un commentaire ``#`` de sa ligne (hors chaîne de caractères) ?"""
    quote, i = None, 0
    while i < len(before_cursor):
        char = before_cursor[i]
        if quote:
            if char == "\\":
                i += 1
            elif before_cursor.startswith(quote, i):
                i += len(quote) - 1
                quote = None
        elif char in "'\"":
            quote = char * 3 if before_cursor.startswith(char * 3, i) else char
            i += len(quote) - 1
        elif char == "#":
            return True
        i += 1
    return False


def _runtime_doc(name):
    """Documentation lue sur l'objet réel quand les stubs de typeshed n'en ont pas (``str.upper``...).
    Uniquement pour un module déjà importé : on n'exécute jamais le code de l'utilisateur."""
    full_name = getattr(name, "full_name", None)
    if not full_name:
        return ""
    root, *path = full_name.split(".")
    obj = sys.modules.get(root)
    if obj is None or root in {"jedi", "parso", "pyflakes", "pyls"}:
        return ""
    try:
        for part in path:
            obj = getattr(obj, part)
        return inspect.getdoc(obj) or ""
    except Exception:  # noqa: BLE001 - propriété qui lève, objet exotique...
        return ""


def _doc_of(name):
    return _clip(name.docstring(raw=True) or _runtime_doc(name))


_KIND = {"module": "module", "class": "class", "instance": "variable", "function": "function", "param": "variable",
         "path": "file", "keyword": "keyword", "property": "property", "statement": "variable"}

_last_completions = {"token": 0, "items": []}


def complete(source, line, column, filename=MAIN_FILE):
    """Suggestions à la position du curseur. Le texte de documentation, coûteux, est demandé à part
    (``completion_doc``) et seulement pour la suggestion sélectionnée."""
    try:
        row, col, text = _cursor(source, line, column)
        if _in_comment(text[:col]):
            return json.dumps({"token": 0, "items": []})
        found = _script(source, filename).complete(row, col)[:MAX_COMPLETIONS]
    except Exception as exc:  # noqa: BLE001
        print(f"complete: {exc!r}", file=sys.stderr)
        return json.dumps({"token": 0, "items": []})

    _last_completions["token"] += 1
    _last_completions["items"] = found

    items = []
    for index, item in enumerate(found):
        name = item.name
        rank = 0 if item.type == "param" else 3 if name.startswith("__") else 2 if name.startswith("_") else 1
        items.append({
            "label": name,
            "insert": item.name_with_symbols if item.type == "param" else name,
            "kind": _KIND.get(item.type, "text"),
            "detail": item.description,
            "sort": f"{rank}{name.lower()}",
            "index": index,
        })
    return json.dumps({"token": _last_completions["token"], "items": items})


def completion_doc(token, index):
    """Documentation d'une suggestion de la dernière réponse de ``complete`` ('' si elle est périmée)."""
    try:
        if token != _last_completions["token"]:
            return json.dumps("")
        return json.dumps(_doc_of(_last_completions["items"][index]))
    except Exception:  # noqa: BLE001
        return json.dumps("")


def _word_at(text, index):
    for match in _IDENTIFIER.finditer(text):
        if match.start() <= index <= match.end():
            return match
    return None


_LABEL = {"param": "parameter", "statement": "variable", "instance": "variable", "property": "property"}


def hover(source, line, column, filename=MAIN_FILE):
    """Infobulle du mot sous le curseur : signature ou type, puis documentation. ``null`` s'il n'y a rien."""
    try:
        row, col, text = _cursor(source, line, column)
        word = _word_at(text, col)
        if word is None or keyword.iskeyword(word.group()) or word.group().isdigit() or _in_comment(text[:col]):
            return "null"

        script = _script(source, filename)
        inferred = script.infer(row, col)
        definitions = script.goto(row, col, follow_imports=True, follow_builtin_imports=True)
        primary = inferred[0] if inferred else (definitions[0] if definitions else None)
        if primary is None:
            return "null"

        name = word.group()
        if primary.type == "function":
            signatures = primary.get_signatures()
            header = f"def {signatures[0].to_string()}" if signatures else f"def {primary.name}()"
        elif primary.type == "class":
            header = f"class {primary.name}"
        elif primary.type == "module":
            header = f"(module) {primary.full_name or primary.name}"
        else:
            label = _LABEL.get(definitions[0].type if definitions else primary.type, "variable")
            hint = primary.get_type_hint()
            header = f"({label}) {name}: {hint}" if hint else f"({label}) {name}"

        parts = [f"```python\n{header}\n```"]
        doc = _doc_of(primary) if primary.type in ("function", "class", "module") else ""
        if doc:
            parts.append(f"```text\n{doc}\n```")
        return json.dumps({
            "markdown": "\n\n".join(parts),
            "line": row,
            "startCol": _cp_to_u16(text, word.start()) + 1,
            "endCol": _cp_to_u16(text, word.end()) + 1,
        })
    except Exception as exc:  # noqa: BLE001
        print(f"hover: {exc!r}", file=sys.stderr)
        return "null"


def signature(source, line, column, filename=MAIN_FILE):
    """Aide à la saisie des arguments d'un appel de fonction. ``null`` hors d'un appel."""
    try:
        row, col, text = _cursor(source, line, column)
        if _in_comment(text[:col]):
            return "null"
        found = _script(source, filename).get_signatures(row, col)
        if not found:
            return "null"

        signatures = []
        for item in found:
            label = item.to_string()
            offsets, cursor = [], 0
            for param in item.params:
                text = param.to_string()
                start = label.find(text, cursor)
                if start < 0:
                    offsets.append(None)
                    continue
                offsets.append([start, start + len(text)])
                cursor = start + len(text)
            signatures.append({"label": label, "doc": _doc_of(item), "params": offsets})
        return json.dumps({"signatures": signatures, "active": 0, "param": found[0].index or 0})
    except Exception as exc:  # noqa: BLE001
        print(f"signature: {exc!r}", file=sys.stderr)
        return "null"


def warm_up():
    """Charge jedi et pyflakes à vide : la première vraie requête de l'utilisateur est alors rapide."""
    _get_project()
    _lint("import os\nos.getcwd()\n", MAIN_FILE)
    complete("import os\nos.", 2, 4, MAIN_FILE)
    return "ok"
