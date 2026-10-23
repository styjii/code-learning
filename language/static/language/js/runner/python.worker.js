/**
 * Python dans un Web Worker (de type module) grâce à Pyodide (CPython compilé en WebAssembly).
 * Le worker reste en vie entre deux exécutions pour éviter de recharger Pyodide.
 *
 * Entrant : {id, code, stdin, indexURL, interactive}   puis, pendant l'exécution : {type: "answer", text}
 * Sortant : {id, type: "status" | "mode" | "started" | "input" | "out" | "err" | "done" | "error", text?, secret?}
 *
 * input() interactif : Python est suspendu (JSPI, pyodide.ffi.run_sync) le temps que l'utilisateur
 * tape sa réponse dans la page ; le worker reste réactif et reçoit « answer ». Sans JSPI, on retombe
 * sur la zone « Entrée standard » (texte fourni à l'avance).
 */
let pyodide = null;
let hooked = false;          // le remplacement de input() n'est installé qu'une fois par worker
let currentId = 0;
let pendingAnswer = null;    // résolveur de la saisie en cours

const HOOK_FILE = "<course-input>";    // nom de fichier du hook : ses lignes sont retirées des traces d'erreur

/** Remplace input() et sys.stdin.readline() par des versions qui demandent à la page. */
const INTERACTIVE_HOOK = `
import builtins, sys
from pyodide.ffi import run_sync
import _course_io

def _ask(prompt="", secret=False):
    sys.stdout.flush()
    text = run_sync(_course_io.ask(str(prompt), bool(secret)))
    if text is None:
        raise EOFError("EOF when reading a line")
    return str(text)

class _Stdin:
    """readline()/itération interactifs ; le reste (read, readlines…) reste géré par l'ancien stdin."""
    def __init__(self, old): self._old = old
    def readline(self, size=-1):
        try: return _ask("") + "\\n"
        except EOFError: return ""
    def __iter__(self): return self
    def __next__(self):
        line = self.readline()
        if not line: raise StopIteration
        return line
    def __getattr__(self, name): return getattr(self._old, name)

builtins.input = _ask
sys.stdin = _Stdin(sys.stdin)

import getpass
getpass.getpass = lambda prompt="Password: ", stream=None: _ask(prompt, True)   # saisie masquée

def _breakpoint(*args, **kwargs):
    """breakpoint() : pdb interactif, sans s'arrêter dans le code interne de Pyodide/asyncio."""
    import pdb
    skip = ["asyncio.*", "_pyodide.*", "pyodide.*", "concurrent.*", "bdb", "pdb", "cmd"]
    pdb.Pdb(skip=skip).set_trace(sys._getframe(1))
sys.breakpointhook = _breakpoint
`;

/** Retire les lignes internes de Pyodide pour ne garder que le code de l'élève. */
function cleanTraceback(message) {
    // Retire les cadres du hook d'input() (File "<course-input>" + la ligne de code qui suit).
    const lines = message.split("\n").filter((line, i, all) =>
        !line.includes(`File "${HOOK_FILE}"`) && !(i > 0 && all[i - 1].includes(`File "${HOOK_FILE}"`) && /^\s{4}/.test(line)));
    const first = lines.findIndex((line) => line.includes('File "<exec>"'));
    if (first === -1) return message.trim();
    const head = lines[0].startsWith("Traceback") ? [lines[0]] : [];
    return [...head, ...lines.slice(first)].join("\n").trim();
}

self.onmessage = async ({ data }) => {
    if (data.type === "answer") {            // réponse à un input() en attente
        const resolve = pendingAnswer;
        pendingAnswer = null;
        resolve?.(data.text ?? undefined);    // fin d'entrée (null) -> undefined, converti en None (null deviendrait jsnull)
        return;
    }
    const { id, code, stdin, indexURL, interactive } = data;
    currentId = id;
    const post = (type, text) => self.postMessage({ id, type, text });

    try {
        if (!pyodide) {
            post("status", "Chargement de Python (premier lancement)…");
            const { loadPyodide } = await import(`${indexURL}pyodide.mjs`);
            pyodide = await loadPyodide({ indexURL });
        }

        // JSPI disponible (Chrome/Edge récents) : input() interactif ; sinon zone « Entrée standard ».
        let canPrompt = false;
        if (interactive) {
            // can_run_sync() n'est vrai que dans un appel asynchrone (runPythonAsync), comme celui du code de l'élève.
            try { canPrompt = !!(await pyodide.runPythonAsync("from pyodide.ffi import can_run_sync; can_run_sync()")); } catch { /* ancien Pyodide */ }
        }
        if (canPrompt && !hooked) {
            pyodide.registerJsModule("_course_io", {
                ask: (prompt, secret) => new Promise((resolve) => {
                    pendingAnswer = resolve;
                    self.postMessage({ id: currentId, type: "input", text: String(prompt ?? ""), secret: !!secret });
                }),
            });
            await pyodide.runPythonAsync(INTERACTIVE_HOOK, { filename: HOOK_FILE });
            hooked = true;
        }
        post("mode", canPrompt && hooked ? "interactive" : "batch");

        const lines = stdin ? stdin.split("\n") : [];
        pyodide.setStdin({ stdin: () => (lines.length ? lines.shift() : undefined) });
        pyodide.setStdout({ batched: (line) => post("out", line) });
        pyodide.setStderr({ batched: (line) => post("err", line) });

        post("status", "");
        post("started");

        const globals = pyodide.globals.get("dict")();
        globals.set("__name__", "__main__");     // sans cela, « if __name__ == "__main__": » ne s'exécute jamais
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
