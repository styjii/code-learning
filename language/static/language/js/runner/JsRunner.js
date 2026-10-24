/**
 * Exécute du JavaScript dans un worker jetable.
 * Contrat commun à tous les runners : { promise: Promise<{ok, reason?}>, stop() }.
 */
export function runJavaScript(code, hooks, { timeout = 8000 } = {}) {
    const worker = new Worker(new URL("./js.worker.js", import.meta.url));
    let finish = () => {};

    const promise = new Promise((resolve) => {
        let timer = null;
        const done = (result) => {
            clearTimeout(timer);
            worker.terminate();
            resolve(result);
        };
        finish = done;

        timer = setTimeout(() => {
            hooks.out("warn", `Exécution interrompue après ${timeout / 1000} s (boucle infinie ou minuteur toujours actif ?).`);
            done({ ok: false, reason: "timeout" });
        }, timeout);

        worker.onmessage = ({ data }) => {
            if (data.type === "console") {
                hooks.console(data.msg);
            } else if (data.type === "done") {
                done({ ok: true });
            } else if (data.type === "error") {
                if (data.msg) hooks.console(data.msg);
                else hooks.out("err", data.text);
                if (data.hint) hooks.out("info", data.hint);
                done({ ok: false, reason: "error" });
            }
        };
        worker.onerror = (event) => {
            hooks.out("err", event.message || "Erreur d'exécution.");
            done({ ok: false, reason: "error" });
        };
        worker.postMessage({ code });
    });

    return { promise, stop: () => finish({ ok: false, reason: "stopped" }) };
}
