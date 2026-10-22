import { state } from "../state/state.js";
import { JsSnippetLoader } from "./JsSnippetLoader.js";
import { EditorConfigManager } from "./EditorConfigManager.js";

/**
 * Manages initialization and interaction with Monaco Editor instances,
 * including diagnostics and editor tab switching.
 */
export class MonacoEditorManager {
    /**
     * @param {EditorConfigManager} configManager
     */
    constructor(configManager) {
        this.configManager = configManager;
        this.updateMarkersDebounced = this._createDebouncedMarkerUpdater();
    }

    /**
     * Creates a debounced function to update Monaco markers.
     * @returns {function(monaco.editor.ITextModel, string, monaco.editor.IMarkerData[], number=): void}
     */
    _createDebouncedMarkerUpdater() {
        let timeoutId;
        return (model, owner, markers, delay = 100) => {
            clearTimeout(timeoutId);
            timeoutId = setTimeout(() => {
                monaco.editor.setModelMarkers(model, owner, markers);
            }, delay);
        };
    }

    /**
     * Updates JS editor diagnostics markers in a debounced way.
     * @param {monaco.editor.IMarkerData[]} diagnostics
     */
    updateJsDiagnostics(diagnostics) {
        const jsEditor = state.editors.js;
        if (!jsEditor) return;
        const model = jsEditor.getModel();
        if (!model) return;
        this.updateMarkersDebounced(model, "jsDiagnostics", diagnostics);
    }

    /**
     * Initializes Monaco editors for html, css, js,
     * loads JS snippets, sets up diagnostics update on JS content change.
     * @param {() => void} callback Called after snippets loaded
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
                    const monacoTheme = event.detail === "light" ? "vs" : "vs-dark";
                    monaco.editor.setTheme(monacoTheme);
                });

                state.editors.html = monaco.editor.create(document.getElementById("html-editor"), {
                    ...commonOptions,
                    language: "html",
                });

                state.editors.css = monaco.editor.create(document.getElementById("css-editor"), {
                    ...commonOptions,
                    language: "css",
                });

                state.editors.js = monaco.editor.create(document.getElementById("js-editor"), {
                    ...commonOptions,
                    language: "javascript",
                });

                state.editors.js.onDidChangeModelContent(() => {
                    this.updateJsDiagnostics([]);
                });

                const snippetLoader = new JsSnippetLoader("/static/editor/snippets/javascript.json", callback);
                await snippetLoader.load();
            } catch (err) {
                console.error("Failed to initialize editors:", err);
            }
        });
    }

    /**
     * Switches the visible editor tab between 'html', 'css', and 'js'.
     * Hides others and activates the selected tab and editor.
     * @param {'html'|'css'|'js'} tab
     */
    switchTab(tab) {
        ["html", "css", "js"].forEach((id) => {
            document.getElementById(id + "-editor").style.display = "none";
        });

        const activeEditorEl = document.getElementById(tab + "-editor");
        activeEditorEl.style.display = "block";

        document.querySelectorAll(".tab").forEach((btn) => btn.classList.remove("active"));
        document.getElementById(`${tab}-tab`).classList.add("active");

        const editor = state.editors[tab];
        if (editor) editor.layout();
    }
}
