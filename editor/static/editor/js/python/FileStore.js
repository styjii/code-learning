/**
 * Fichiers du projet courant de l'éditeur Python, tenus en mémoire (copie de travail).
 * Fichiers « à plat » : main.py est le point d'entrée, les autres .py sont importables
 * (« import utils ») et les autres extensions (.txt, .json, .csv…) lisibles avec open().
 *
 * L'enregistrement est assuré par ``PythonProjectManager`` (projets sur le serveur). Avant les projets, les fichiers
 * étaient gardés dans le navigateur (localStorage) : ``readLegacyProject`` permet de les récupérer une fois.
 */
const LEGACY_STORAGE_KEY = "python-editor:v1";

export const MAIN_FILE = "main.py";
export const MAX_FILES = 20;
export const MAX_CHARS = 200_000;

/** Modules standard courants : un fichier de ce nom les masquerait et casserait les imports. */
const STANDARD_MODULES = new Set([
    "abc", "argparse", "array", "ast", "asyncio", "base64", "bisect", "builtins", "calendar", "collections",
    "copy", "csv", "dataclasses", "datetime", "decimal", "enum", "fractions", "functools", "glob", "hashlib",
    "heapq", "html", "io", "itertools", "json", "logging", "math", "operator", "os", "pathlib", "pickle",
    "queue", "random", "re", "statistics", "string", "struct", "sys", "tempfile", "textwrap", "threading",
    "time", "types", "typing", "unittest", "urllib", "uuid", "warnings",
]);

export const SAMPLE = `# Bienvenue dans l'éditeur Python !
#  • Ctrl+Entrée exécute main.py
#  • input() est interactif : tapez directement dans la console
#  • Ajoutez d'autres fichiers .py avec « + » et importez-les (import utils)

nom = input("Votre nom : ")
print(f"Bonjour {nom} !")

carres = [n ** 2 for n in range(1, 6)]
print("Carrés :", carres)
`;

/** Ajoute « .py » si le nom n'a pas d'extension. */
export function normalizeName(raw) {
    const name = String(raw ?? "").trim();
    return name && !/\.[A-Za-z0-9]+$/.test(name) ? `${name}.py` : name;
}

/**
 * @param {string} raw nom saisi
 * @param {string[]} existing noms déjà utilisés
 * @param {{ignore?: string}} [options] nom à ignorer (renommage d'un fichier vers lui-même)
 * @returns {{name: string, error: string|null}}
 */
export function validateName(raw, existing, { ignore } = {}) {
    const name = normalizeName(raw);
    const fail = (error) => ({ name, error });

    if (!name) return fail("Le nom du fichier est vide.");
    if (name.length > 40) return fail("Nom trop long (40 caractères maximum).");
    if (/[\\/]/.test(name)) return fail("Les dossiers ne sont pas gérés : pas de « / » dans le nom.");
    const isPython = name.endsWith(".py");
    const pattern = isPython ? /^[A-Za-z_][A-Za-z0-9_]*\.py$/ : /^[A-Za-z0-9_][A-Za-z0-9_.-]*\.[A-Za-z0-9]{1,8}$/;
    if (!pattern.test(name)) {
        return fail(isPython
            ? "Un module Python s'écrit avec des lettres, chiffres et « _ », sans commencer par un chiffre."
            : "Caractères autorisés : lettres, chiffres, « _ », « - » et « . ».");
    }
    if (isPython && STANDARD_MODULES.has(name.slice(0, -3))) {
        return fail(`« ${name} » masquerait le module standard « ${name.slice(0, -3)} » : choisissez un autre nom.`);
    }
    const taken = existing.some((other) => other !== ignore && other.toLowerCase() === name.toLowerCase());
    if (taken) return fail(`Un fichier « ${name} » existe déjà.`);
    return { name, error: null };
}

/**
 * Fichiers que l'éditeur gardait dans le navigateur avant les projets enregistrés, ou ``null`` s'il n'y en a pas.
 * Les fichiers sont renvoyés tels quels : ``FileStore.replaceAll`` les revalide.
 * @returns {{name: string, content: string}[]|null}
 */
export function readLegacyProject() {
    try {
        const data = JSON.parse(window.localStorage.getItem(LEGACY_STORAGE_KEY) ?? "null");
        const files = Array.isArray(data?.files) ? data.files.filter((f) => f && typeof f.name === "string" && typeof f.content === "string") : [];
        return files.length ? files : null;
    } catch {
        return null;       // stockage bloqué ou contenu illisible
    }
}

/** Supprime les fichiers d'avant les projets, une fois repris dans un projet enregistré. */
export function clearLegacyProject() {
    try { window.localStorage.removeItem(LEGACY_STORAGE_KEY); } catch { /* stockage bloqué */ }
}

export class FileStore {
    constructor() {
        /** @type {{name: string, content: string}[]} */
        this.files = [{ name: MAIN_FILE, content: SAMPLE }];
        this.active = MAIN_FILE;
    }

    #sortMainFirst() {
        this.files.sort((a, b) => (a.name === MAIN_FILE ? -1 : b.name === MAIN_FILE ? 1 : 0));
    }

    names() { return this.files.map((file) => file.name); }
    has(name) { return this.files.some((file) => file.name === name); }
    content(name) { return this.files.find((file) => file.name === name)?.content ?? ""; }

    setContent(name, content) {
        const file = this.files.find((f) => f.name === name);
        if (file) file.content = String(content).slice(0, MAX_CHARS);
    }

    /** @returns {{ok: boolean, name: string, error: string|null}} */
    add(raw, content = "") {
        const { name, error } = validateName(raw, this.names());
        if (error) return { ok: false, name, error };
        if (this.files.length >= MAX_FILES) return { ok: false, name, error: `Limite de ${MAX_FILES} fichiers atteinte.` };
        this.files.push({ name, content: String(content).slice(0, MAX_CHARS) });
        return { ok: true, name, error: null };
    }

    /** Nom disponible du type « module.py », « module_2.py »… */
    freeName(base = "module", extension = ".py") {
        let candidate = `${base}${extension}`;
        for (let i = 2; this.names().some((n) => n.toLowerCase() === candidate.toLowerCase()); i++) candidate = `${base}_${i}${extension}`;
        return candidate;
    }

    rename(oldName, raw) {
        if (oldName === MAIN_FILE) return { ok: false, name: oldName, error: "main.py est le point d'entrée : il ne peut pas être renommé." };
        const { name, error } = validateName(raw, this.names(), { ignore: oldName });
        if (error) return { ok: false, name, error };
        const file = this.files.find((f) => f.name === oldName);
        if (!file) return { ok: false, name, error: "Fichier introuvable." };
        file.name = name;
        if (this.active === oldName) this.active = name;
        return { ok: true, name, error: null };
    }

    remove(name) {
        if (name === MAIN_FILE) return false;
        const before = this.files.length;
        this.files = this.files.filter((file) => file.name !== name);
        if (this.active === name) this.active = MAIN_FILE;
        return this.files.length < before;
    }

    /** Fichiers à déposer à côté de main.py pour l'exécution (main.py lui-même est exécuté tel quel). */
    runFiles() {
        return Object.fromEntries(this.files.filter((file) => file.name !== MAIN_FILE).map((file) => [file.name, file.content]));
    }

    reset() {
        this.files = [{ name: MAIN_FILE, content: SAMPLE }];
        this.active = MAIN_FILE;
    }

    /**
     * Remplace tout le projet (changement de projet, restauration d'une archive .zip). Chaque fichier repasse par les mêmes règles que
     * ``add`` (nom, doublons, limites) : ce qui ne les respecte pas est écarté et signalé, jamais enregistré.
     * Sans main.py dans l'archive, l'exemple de départ en tient lieu.
     *
     * @param {{name: string, content: string}[]} files
     * @returns {{count: number, skipped: string[], sampleMain: boolean}}
     */
    replaceAll(files) {
        const kept = [];
        const skipped = [];
        // main.py d'abord : la limite de fichiers ne doit jamais le faire écarter.
        const incoming = (Array.isArray(files) ? [...files] : []).sort((a, b) => (b?.name === MAIN_FILE) - (a?.name === MAIN_FILE));
        for (const file of incoming) {
            const label = `« ${file?.name} »`;
            if (typeof file?.content !== "string") { skipped.push(`${label} : contenu invalide.`); continue; }
            if (kept.length >= MAX_FILES) { skipped.push(`${label} : limite de ${MAX_FILES} fichiers atteinte.`); continue; }
            const { name, error } = validateName(file.name, kept.map((f) => f.name));
            if (error) { skipped.push(`${label} : ${error}`); continue; }
            kept.push({ name, content: file.content.slice(0, MAX_CHARS) });
        }
        const sampleMain = !kept.some((file) => file.name === MAIN_FILE);
        if (sampleMain) {
            // L'exemple prend la place de main.py : on ne dépasse pas la limite.
            if (kept.length >= MAX_FILES) skipped.push(`« ${kept.pop().name} » : limite de ${MAX_FILES} fichiers atteinte.`);
            kept.unshift({ name: MAIN_FILE, content: SAMPLE });
        }
        this.files = kept;
        this.#sortMainFirst();
        this.active = MAIN_FILE;
        return { count: kept.length, skipped, sampleMain };
    }
}
