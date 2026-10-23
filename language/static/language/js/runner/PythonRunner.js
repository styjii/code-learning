/**
 * Pilote le worker Pyodide. Les exécutions sont mises en file d'attente (un seul interpréteur).
 * En cas de dépassement de délai ou d'arrêt manuel, le worker est détruit puis recréé à la demande.
 */
let worker = null;
let queue = Promise.resolve();
let nextId = 1;

/** JSPI : nécessaire pour suspendre Python pendant un input() (Chrome / Edge récents). */
const canPrompt = typeof WebAssembly !== "undefined" && "Suspending" in WebAssembly;

const getWorker = () => (worker ??= new Worker(new URL("./python.worker.js", import.meta.url), { type: "module" }));

export const PythonRunner = {
    /** true si input() peut être saisi pendant l'exécution (sinon : zone « Entrée standard »). */
    canPrompt,

    /**
     * @param {string} code
     * @param {{out: Function, status: Function, input?: (prompt: string, options: {secret: boolean}) => Promise<string|null>, mode?: Function}} hooks
     * @param {{stdin?: string, timeout?: number}} options
     */
    run(code, hooks, { stdin = "", timeout = 10000 } = {}) {
        let cancelled = false;
        let abort = null;

        const execute = () => new Promise((resolve) => {
            if (cancelled) return resolve({ ok: false, reason: "stopped" });

            const w = getWorker();
            const id = nextId++;
            let timer = null;
            let settled = false;

            const finish = (result) => {
                if (settled) return;
                settled = true;
                clearTimeout(timer);
                w.removeEventListener("message", onMessage);
                w.removeEventListener("error", onError);
                resolve(result);
            };
            const kill = () => {
                w.terminate();
                if (worker === w) worker = null;
            };
            // Le délai ne court pas pendant qu'on attend la frappe de l'utilisateur.
            const armTimeout = () => {
                clearTimeout(timer);
                timer = setTimeout(() => {
                    hooks.out("warn", `Exécution interrompue après ${timeout / 1000} s (boucle infinie ?).`);
                    kill();
                    finish({ ok: false, reason: "timeout" });
                }, timeout);
            };
            const onMessage = ({ data }) => {
                if (data.id !== id) return;
                switch (data.type) {
                    case "status": hooks.status(data.text); break;
                    case "mode": hooks.mode?.(data.text); break;
                    case "started": armTimeout(); break;
                    case "input":
                        clearTimeout(timer);
                        Promise.resolve(hooks.input ? hooks.input(data.text, { secret: !!data.secret }) : null).then((text) => {
                            if (settled) return;
                            armTimeout();
                            w.postMessage({ type: "answer", text });
                        });
                        break;
                    case "out": hooks.out("out", data.text); break;
                    case "err": hooks.out("err", data.text); break;
                    case "done": finish({ ok: true }); break;
                    case "error": hooks.out("err", data.text); finish({ ok: false, reason: "error" }); break;
                }
            };
            const onError = () => {
                hooks.out("err", "Impossible de démarrer Python (fichiers Pyodide introuvables ?).");
                kill();
                finish({ ok: false, reason: "error" });
            };

            abort = () => { kill(); finish({ ok: false, reason: "stopped" }); };
            w.addEventListener("message", onMessage);
            w.addEventListener("error", onError);

            // Délai large pour le premier chargement de Pyodide ; remplacé dès « started ».
            timer = setTimeout(() => {
                hooks.out("warn", "Le chargement de Python a pris trop de temps.");
                kill();
                finish({ ok: false, reason: "timeout" });
            }, 90000);

            w.postMessage({ id, code, stdin, indexURL: document.body.dataset.pyodide, interactive: canPrompt && !!hooks.input });
        });

        const promise = (queue = queue.then(execute, execute));
        return { promise, stop: () => { cancelled = true; abort?.(); } };
    },
};
