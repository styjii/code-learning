import { state } from "./state.js";
import { compileTypeScript } from "./TsCompiler.js";
import { ConsoleManager } from "../console/ConsoleManager.js";

/**
 * Compile le TypeScript, affiche les erreurs dans la console, puis envoie HTML, CSS et JavaScript produit
 * à l'aperçu (même point d'entrée que l'éditeur Web, avec « module=1 » : le script est exécuté comme module).
 */
export class TsPreviewManager {
    /** Identifiant de la dernière exécution : une compilation plus ancienne ne remplace jamais une plus récente. */
    static #runId = 0;

    /** Met à jour la liste des bibliothèques (Bootstrap) selon l'interrupteur, sans lancer l'aperçu. */
    static syncCdnLinks() {
        const bootstrapSwitch = document.getElementById("bootstrapCdnSwitch");
        const baseUrl = `${location.origin}/static/dist`;

        state.cssCdnLinks = [];
        state.jsCdnLinks = [];

        if (bootstrapSwitch?.checked) {
            state.cssCdnLinks.push(`${baseUrl}/css/bootstrap.min.css`);
            state.jsCdnLinks.push(`${baseUrl}/js/bootstrap.bundle.min.js`);
        }
    }

    /** Met à jour les bibliothèques puis relance l'aperçu. */
    static updateCdnLinks() {
        this.syncCdnLinks();
        return this.run();
    }

    /** Affiche la console à la place de l'aperçu. */
    static showConsole() {
        document.getElementById("console").style.display = "block";
        document.getElementById("output").style.display = "none";
        document.getElementById("display-console")?.setAttribute("aria-pressed", "true");
    }

    /**
     * Compile puis lance l'aperçu. Avec « noEmitOnError », une erreur de type empêche l'exécution :
     * les erreurs s'affichent alors dans la console, ouverte automatiquement.
     */
    static async run() {
        const output = document.getElementById("output");
        const consoleEl = document.getElementById("console");
        const editor = state.editors.ts;
        if (!output || !consoleEl || !editor) return;

        const runId = ++this.#runId;
        consoleEl.innerHTML = "";

        let js = "";
        try {
            const result = await compileTypeScript(window.monaco, editor.getModel());
            if (runId !== this.#runId) return;
            this.#report(result.errors);
            if (result.errors.length && state.compilerOptions.noEmitOnError) {
                this.showConsole();
                return;
            }
            js = result.js;
        } catch (err) {
            if (runId !== this.#runId) return;
            this.#log("error", `Erreur du compilateur : ${err.message}`);
            this.showConsole();
            return;
        }

        const formData = new FormData();
        formData.append("html", this.#sanitizeHTML(state.editors.html?.getValue() ?? ""));
        formData.append("css", state.editors.css?.getValue() ?? "");
        formData.append("js", js);
        formData.append("module", "1");
        formData.append("cdn_css", JSON.stringify(state.cssCdnLinks));
        formData.append("cdn_js", JSON.stringify(state.jsCdnLinks));

        try {
            const res = await fetch("/editor/preview/", { method: "POST", body: formData });
            const data = await res.json();
            if (runId === this.#runId) output.src = data.url;
        } catch (err) {
            console.error("Preview error:", err);
        }
    }

    /**
     * Toggles auto live preview on/off.
     * @param {MouseEvent} e
     */
    static toggleLive(e) {
        state.autoLive = !state.autoLive;
        e.currentTarget.textContent = `Auto : ${state.autoLive ? "activé" : "désactivé"}`;
        if (state.autoLive) this.updateCdnLinks();
    }

    static #log(type, text) {
        if (!ConsoleManager.renderer) ConsoleManager.init();
        ConsoleManager.renderer.add({ type, args: [text] });
    }

    static #report(errors) {
        if (!errors.length) return;
        for (const e of errors) {
            this.#log("error", `ligne ${e.line}, col. ${e.column} · TS${e.code} : ${e.message}`);
        }
        const count = `${errors.length} erreur${errors.length > 1 ? "s" : ""} de type`;
        this.#log("warn", state.compilerOptions.noEmitOnError
            ? `Compilation échouée (${count}) : corrigez le code, ou désactivez « noEmitOnError » dans les options.`
            : `${count} : le code est exécuté malgré tout (« noEmitOnError » désactivé).`);
    }

    /** Retire les éléments dangereux du HTML (scripts, iframes, feuilles de style...). */
    static #sanitizeHTML(dirty) {
        const doc = new DOMParser().parseFromString(dirty, "text/html");
        doc.querySelectorAll("script, iframe, object, embed, link, style").forEach((el) => el.remove());
        return doc.body.innerHTML;
    }
}
