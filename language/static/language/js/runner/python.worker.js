/**
 * Python dans un Web Worker (de type module) grâce à Pyodide (CPython compilé en WebAssembly).
 * Le worker reste en vie entre deux exécutions pour éviter de recharger Pyodide.
 *
 * Entrant : {id, code, stdin, indexURL}
 * Sortant : {id, type: "status" | "started" | "out" | "err" | "done" | "error", text?}
 */
let pyodide = null;

/** Retire les lignes internes de Pyodide pour ne garder que le code de l'élève. */
function cleanTraceback(message) {
    const lines = message.split("\n");
    const first = lines.findIndex((line) => line.includes('File "<exec>"'));
    if (first === -1) return message.trim();
    const head = lines[0].startsWith("Traceback") ? [lines[0]] : [];
    return [...head, ...lines.slice(first)].join("\n").trim();
}

self.onmessage = async ({ data: { id, code, stdin, indexURL } }) => {
    const post = (type, text) => self.postMessage({ id, type, text });

    try {
        if (!pyodide) {
            post("status", "Chargement de Python (premier lancement)…");
            const { loadPyodide } = await import(`${indexURL}pyodide.mjs`);
            pyodide = await loadPyodide({ indexURL });
        }

        const lines = stdin ? stdin.split("\n") : [];
        pyodide.setStdin({ stdin: () => (lines.length ? lines.shift() : undefined) });
        pyodide.setStdout({ batched: (line) => post("out", line) });
        pyodide.setStderr({ batched: (line) => post("err", line) });

        post("status", "");
        post("started");

        const globals = pyodide.globals.get("dict")();
        try {
            await pyodide.runPythonAsync(code, { globals });
            pyodide.runPython("import sys; sys.stdout.flush(); sys.stderr.flush()");
        } finally {
            globals.destroy();
        }
        post("done");
    } catch (error) {
        post("error", cleanTraceback(String(error?.message ?? error)));
    }
};
