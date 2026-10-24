/**
 * Fichiers du projet de l'éditeur Python, conservés dans le navigateur (localStorage).
 * Fichiers « à plat » : main.py est le point d'entrée, les autres .py sont importables
 * (« import utils ») et les autres extensions (.txt, .json, .csv…) lisibles avec open().
 */
const STORAGE_KEY = "python-editor:v1";

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

function browserStorage() {
    try {
        const storage = window.localStorage;
        storage.getItem(STORAGE_KEY);      // lève une exception si le stockage est bloqué
        return storage;
    } catch {
        return null;
    }
}

export class FileStore {
    /** @param {Storage|null} [storage] injecté dans les tests ; par défaut localStorage */
    constructor(storage = browserStorage()) {
        this.storage = storage;
        /** @type {{name: string, content: string}[]} */
        this.files = [];
        this.active = MAIN_FILE;
        this.persistent = !!storage;
        this.#load();
    }

    #load() {
        let data = null;
        try { data = JSON.parse(this.storage?.getItem(STORAGE_KEY) ?? "null"); } catch { data = null; }

        const seen = new Set();
        for (const file of Array.isArray(data?.files) ? data.files : []) {
            if (!file || typeof file.name !== "string" || typeof file.content !== "string") continue;
            const key = file.name.toLowerCase();
            if (seen.has(key) || validateName(file.name, []).error) continue;
            seen.add(key);
            this.files.push({ name: file.name, content: file.content.slice(0, MAX_CHARS) });
            if (this.files.length >= MAX_FILES) break;
        }
        if (!this.files.some((file) => file.name === MAIN_FILE)) this.files.unshift({ name: MAIN_FILE, content: SAMPLE });
        this.#sortMainFirst();
        this.active = this.has(data?.active) ? data.active : MAIN_FILE;
    }

    #sortMainFirst() {
        this.files.sort((a, b) => (a.name === MAIN_FILE ? -1 : b.name === MAIN_FILE ? 1 : 0));
    }

    /** @returns {boolean} false si le navigateur refuse d'écrire (stockage plein ou bloqué) */
    save() {
        if (!this.storage) return false;
        try {
            this.storage.setItem(STORAGE_KEY, JSON.stringify({ version: 1, active: this.active, files: this.files }));
            return true;
        } catch {
            this.persistent = false;
            return false;
        }
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
}
