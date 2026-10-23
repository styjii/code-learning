import { runJavaScript } from "./JsRunner.js";

/** Aplati un message de diagnostic TypeScript (chaîne ou chaîne de messages). */
function flatten(message) {
    if (typeof message === "string") return message;
    return [message.messageText, ...(message.next ?? []).map(flatten)].join(" ");
}

/**
 * Avec « module: ESNext », TypeScript ajoute « export {}; » à tout fichier traité comme un module.
 * Le worker exécute le code dans une fonction asynchrone (où « await » de premier niveau est permis)
 * et non comme un module : cette instruction y serait une SyntaxError.
 */
const stripSyntheticExport = (js) => js.replace(/^[ \t]*export\s*\{\s*\}\s*;?[ \t]*$/gm, "");

/**
 * Vérifie les types avec le compilateur intégré à Monaco, puis exécute le JavaScript produit.
 * Si des erreurs de type existent, le code n'est pas exécuté (comme une vraie compilation).
 * « execute(js, hooks) » choisit où tourne le JavaScript produit (worker par défaut, iframe pour le DOM).
 */
export function runTypeScript(monaco, model, hooks, execute = runJavaScript) {
    let stopped = false;
    let inner = null;

    const promise = (async () => {
        hooks.status("Compilation…");
        const getWorker = await monaco.languages.typescript.getTypeScriptWorker();
        const worker = await getWorker(model.uri);
        const uri = model.uri.toString();

        const [syntax, semantic] = await Promise.all([
            worker.getSyntacticDiagnostics(uri),
            worker.getSemanticDiagnostics(uri),
        ]);
        const errors = [...syntax, ...semantic].filter((d) => d.category === 1);

        if (errors.length) {
            for (const diagnostic of errors) {
                const { lineNumber, column } = model.getPositionAt(diagnostic.start ?? 0);
                hooks.out("err", `ligne ${lineNumber}, col. ${column} · TS${diagnostic.code} : ${flatten(diagnostic.messageText)}`);
            }
            hooks.out("warn", "Compilation échouée : corrigez les erreurs de type pour exécuter le code.");
            return { ok: false, reason: "compile" };
        }

        const emitted = await worker.getEmitOutput(uri);
        const js = stripSyntheticExport(emitted.outputFiles.find((f) => f.name.endsWith(".js"))?.text ?? "");
        if (stopped) return { ok: false, reason: "stopped" };

        hooks.status("");
        inner = execute(js, hooks);
        return inner.promise;
    })().catch((error) => {
        hooks.out("err", `Erreur du compilateur : ${error.message}`);
        return { ok: false, reason: "error" };
    });

    return { promise, stop: () => { stopped = true; inner?.stop(); } };
}
