/**
 * Service de langage Python dans un Web Worker (de type module).
 *
 * C'est un Pyodide à part, distinct de celui qui exécute le programme de l'élève : une analyse ne bloque
 * jamais une exécution (ni l'inverse), et ne peut pas être gelée par un `input()` en attente ou une boucle
 * infinie. Il charge jedi et pyflakes (voir static/vendor/python-tools/) puis `language_service.py`, qui
 * fait le travail ; ce fichier-ci ne fait que le transport.
 *
 * Entrant : {id, method, args}. Le premier message est « init » : {indexURL, toolsURL, serviceURL}.
 * Sortant : {id, ok: true, result} ou {id, ok: false, error}.
 */
const TOOLS_DIR = "/opt/lsp";    // doit rester synchronisé avec HIDDEN_PATHS dans language_service.py
const METHODS = ["sync_project", "lint", "complete", "completion_doc", "hover", "signature"];

let api = null;
let ready = null;

async function fetchOk(url) {
    const response = await fetch(url);
    if (!response.ok) throw new Error(`${url} : HTTP ${response.status}`);
    return response;
}

/** Détecte un fichier tronqué ou corrompu avant d'en faire une erreur Python incompréhensible. */
async function verify(buffer, expected, file) {
    if (!expected || !globalThis.crypto?.subtle) return;     // crypto.subtle n'existe qu'en contexte sécurisé
    const digest = await crypto.subtle.digest("SHA-256", buffer);
    const actual = [...new Uint8Array(digest)].map((byte) => byte.toString(16).padStart(2, "0")).join("");
    if (actual !== expected) throw new Error(`${file} : empreinte SHA-256 inattendue (fichier corrompu ?)`);
}

async function init({ indexURL, toolsURL, serviceURL }) {
    const { loadPyodide } = await import(`${indexURL}pyodide.mjs`);
    const pyodide = await loadPyodide({ indexURL, stderr: (line) => console.warn("[python-language]", line) });

    const { wheels } = await (await fetchOk(`${toolsURL}manifest.json`)).json();
    pyodide.FS.mkdirTree(TOOLS_DIR);
    for (const { file, sha256 } of wheels) {
        const buffer = await (await fetchOk(`${toolsURL}${file}`)).arrayBuffer();
        await verify(buffer, sha256, file);
        pyodide.unpackArchive(buffer, "wheel", { extractDir: TOOLS_DIR });
    }
    pyodide.runPython(`import sys\nsys.path.insert(0, ${JSON.stringify(TOOLS_DIR)})`);
    pyodide.FS.writeFile(`${TOOLS_DIR}/pyls.py`, await (await fetchOk(serviceURL)).text());

    const service = pyodide.pyimport("pyls");
    api = Object.fromEntries(METHODS.map((name) => [name, service[name]]));    // résolus une fois : pas de proxy par appel
    service.warm_up();
}

const reply = (id, ok, payload) => self.postMessage(ok ? { id, ok, result: payload } : { id, ok, error: payload });

self.onmessage = async ({ data: { id, method, args = [] } }) => {
    try {
        if (method === "init") {
            ready ??= init(args[0]);
            await ready;
            return reply(id, true, null);
        }
        if (!METHODS.includes(method)) throw new Error(`méthode inconnue : ${method}`);
        await ready;
        if (!api) throw new Error("le service n'est pas initialisé");
        const raw = api[method](...args);
        reply(id, true, typeof raw === "string" ? JSON.parse(raw) : null);
    } catch (error) {
        reply(id, false, String(error?.message ?? error));
    }
};
