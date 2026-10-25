import { state } from "./state.js";
import { JsSnippetLoader } from "../editors/JsSnippetLoader.js";
import { TsOptionsManager } from "./TsOptionsManager.js";

/**
 * Initialise les trois éditeurs Monaco (html, css, ts) et gère le changement d'onglet.
 * Calqué sur MonacoEditorManager (éditeur Web) : le JavaScript est remplacé par TypeScript,
 * dont les erreurs sont soulignées par le service de langage de Monaco.
 */
export class TsEditorManager {
    /** @param {import("../editors/EditorConfigManager.js").EditorConfigManager} configManager */
    constructor(configManager) {
        this.configManager = configManager;
    }

    /**
     * @param {() => void} callback appelé une fois les éditeurs et les snippets prêts
     */
    async initializeEditors(callback) {
        require.config({
            paths: { vs: "/static/editor/monaco-editor/min/vs" },
            "vs/nls": { availableLanguages: { "*": "fr" } }, // interface de Monaco en français
        });

        require(["vs/editor/editor.main"], async () => {
            if (window.emmetMonaco) {
                emmetMonaco.emmetHTML(monaco, ["html"]);
                emmetMonaco.emmetCSS(monaco, ["css"]);
            }

            try {
                await this.configManager.loadConfig();
                const baseOptions = this.configManager.getConfig();

                // Le thème suit celui du site (et n'est pas une préférence enregistrée côté serveur).
                const commonOptions = {
                    ...baseOptions,
                    theme: document.documentElement.dataset.theme === "light" ? "vs" : "vs-dark",
                };

                document.addEventListener("themechange", (event) => {
                    monaco.editor.setTheme(event.detail === "light" ? "vs" : "vs-dark");
                });

                // Options du compilateur avant la création du modèle : la première vérification les utilise.
                TsOptionsManager.apply(state.compilerOptions);
                monaco.languages.typescript.typescriptDefaults.setEagerModelSync(true);

                state.editors.html = monaco.editor.create(document.getElementById("html-editor"), {
                    ...commonOptions,
                    language: "html",
                });

                state.editors.css = monaco.editor.create(document.getElementById("css-editor"), {
                    ...commonOptions,
                    language: "css",
                });

                // Nom de fichier en .ts : le compilateur le traite comme un vrai fichier TypeScript.
                const tsModel = monaco.editor.createModel("", "typescript", monaco.Uri.parse("file:///main.ts"));
                state.editors.ts = monaco.editor.create(document.getElementById("ts-editor"), {
                    ...commonOptions,
                    model: tsModel,
                });

                const snippetLoader = new JsSnippetLoader("/static/editor/snippets/javascript.json", callback, "typescript");
                await snippetLoader.load();
            } catch (err) {
                console.error("Failed to initialize editors:", err);
            }
        });
    }

    /**
     * Switches the visible editor tab between 'html', 'css', and 'ts'.
     * @param {'html'|'css'|'ts'} tab
     */
    switchTab(tab) {
        ["html", "css", "ts"].forEach((id) => {
            document.getElementById(id + "-editor").style.display = "none";
        });

        document.getElementById(tab + "-editor").style.display = "block";

        document.querySelectorAll(".tab").forEach((btn) => btn.classList.remove("active"));
        document.getElementById(`${tab}-tab`).classList.add("active");

        const editor = state.editors[tab];
        if (editor) editor.layout();
    }
}
