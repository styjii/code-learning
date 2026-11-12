/**
 * Barre d'état : problèmes, langage, position du curseur, indentation et nombre de lignes de l'éditeur visible.
 * Fonctionne pour les trois éditeurs : elle écoute tous les éditeurs Monaco de la page.
 */
const LANGUAGES = { html: "HTML", css: "CSS", javascript: "JavaScript", typescript: "TypeScript", python: "Python", json: "JSON", markdown: "Markdown", plaintext: "Texte" };
const $ = (id) => document.getElementById(id);

export class StatusBar {
    /** @param {typeof import("monaco-editor")} monaco */
    static init(monaco) {
        if (!monaco || StatusBar.started) return;
        StatusBar.started = true;
        let queued = false;
        const refresh = () => {
            queued = false;
            StatusBar.render(monaco);
        };
        const schedule = () => {
            if (queued) return;
            queued = true;
            requestAnimationFrame(refresh);
        };

        const track = (editor) => {
            editor.onDidChangeModelContent(schedule);
            editor.onDidChangeCursorPosition(schedule);
            editor.onDidChangeModel(schedule);
        };
        monaco.editor.getEditors().forEach(track);
        monaco.editor.onDidCreateEditor((editor) => { track(editor); schedule(); });
        monaco.editor.onDidChangeMarkers(schedule);

        // Changement d'onglet (clic ou Ctrl+1/2/3) : l'éditeur visible n'est plus le même.
        document.addEventListener("click", (event) => { if (event.target.closest(".tab, .py-tab")) setTimeout(schedule, 30); });
        document.addEventListener("keydown", () => setTimeout(schedule, 30));
        schedule();
    }

    static visibleEditor(monaco) {
        return monaco.editor.getEditors().find((editor) => {
            const node = editor.getContainerDomNode();
            return node && node.offsetParent !== null && editor.getModel();
        });
    }

    static render(monaco) {
        const editor = StatusBar.visibleEditor(monaco);
        if (!editor) return;
        const model = editor.getModel();
        const position = editor.getPosition() ?? { lineNumber: 1, column: 1 };
        const options = model.getOptions();

        const markers = monaco.editor.getModelMarkers({ resource: model.uri });
        const errors = markers.filter((m) => m.severity >= monaco.MarkerSeverity.Error).length;
        const warnings = markers.filter((m) => m.severity === monaco.MarkerSeverity.Warning).length;
        const issues = $("sb-issues");
        const text = $("sb-issues-text");
        if (issues && text) {
            issues.dataset.level = errors ? "error" : warnings ? "warn" : "ok";
            const parts = [];
            if (errors) parts.push(`${errors} erreur${errors > 1 ? "s" : ""}`);
            if (warnings) parts.push(`${warnings} avertissement${warnings > 1 ? "s" : ""}`);
            text.textContent = parts.length ? parts.join(", ") : "Aucun problème";
        }

        const set = (id, value) => { const node = $(id); if (node && node.textContent !== value) node.textContent = value; };
        set("sb-lang", LANGUAGES[model.getLanguageId()] ?? model.getLanguageId());
        set("sb-cursor", `Ln ${position.lineNumber}, Col ${position.column}`);
        set("sb-indent", `${options.insertSpaces ? "Espaces" : "Tabulations"} : ${options.tabSize}`);
        set("sb-lines", `Lignes : ${model.getLineCount()}`);
    }
}
