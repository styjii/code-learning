import { loadMonaco } from "./MonacoLoader.js";
import { runJavaScript } from "./JsRunner.js";
import { runTypeScript } from "./TsRunner.js";
import { runInDom, disposePreview, usesDom } from "./DomRunner.js";
import { PythonRunner } from "./PythonRunner.js";

/**
 * Rend exécutables les blocs de code JavaScript, TypeScript et Python des cours.
 *
 * Un bouton « Exécuter » apparaît dans l'en-tête du bloc. Au premier clic, le bloc devient
 * un éditeur Monaco modifiable (Ctrl+Entrée pour relancer) avec sa zone de résultat.
 * Un bloc marqué « ```python norun » dans le Markdown reste en lecture seule.
 *
 * Seules les pages déclarées « runnable=True » dans language/config.py (Python, JavaScript,
 * TypeScript) sont concernées : ailleurs, les blocs restent en lecture seule.
 */
const KINDS = {
    js: "javascript", javascript: "javascript",
    ts: "typescript", typescript: "typescript",
    py: "python", python: "python",
};
const EXTENSIONS = { javascript: "js", typescript: "ts", python: "py" };
const MAX_LINES = 500;

const PLAY = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7 4.5v15a1 1 0 0 0 1.5.86l12-7.5a1 1 0 0 0 0-1.72l-12-7.5A1 1 0 0 0 7 4.5z"/></svg>';
const STOP = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><rect x="6" y="6" width="12" height="12" rx="2"/></svg>';

let counter = 0;

function detectKind(code) {
    const match = (code.className || "").match(/language-([\w+#-]+)/);
    return match ? KINDS[match[1].toLowerCase()] ?? null : null;
}

/**
 * Les extraits Node/ES modules ne peuvent pas tourner dans un worker isolé :
 * import/export statiques, require() et import() dynamique (« await import("./module.js") »).
 */
function isRunnable(kind, source, code) {
    if (code.dataset.run === "false" || !source.trim()) return false;
    if (kind !== "python" && /^\s*(import|export)\s|\brequire\s*\(|\bimport\s*\(/m.test(source)) return false;
    return true;
}

function el(tag, className, html) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (html !== undefined) node.innerHTML = html;
    return node;
}

class RunnableBlock {
    constructor(host, kind, source) {
        this.host = host;
        this.kind = kind;
        this.source = source;
        this.id = ++counter;
        this.pre = host.querySelector("pre");
        this.running = false;
        this.job = null;
        this.editor = null;
        this.activating = null;
        this.lines = 0;
        this.buildButtons();
        host.runApi = { getValue: () => this.editor?.getValue() };
    }

    /* ---------- Boutons de l'en-tête ---------- */
    buildButtons() {
        const actions = this.host.querySelector(".code-actions");
        this.runBtn = el("button", "run-button", `${PLAY}<span>Exécuter</span>`);
        this.runBtn.type = "button";
        this.runBtn.title = "Exécuter le code (Ctrl+Entrée)";
        this.runBtn.addEventListener("click", () => this.running ? this.stop() : this.run());

        this.resetBtn = el("button", "reset-button", "Réinitialiser");
        this.resetBtn.type = "button";
        this.resetBtn.hidden = true;
        this.resetBtn.addEventListener("click", () => {
            this.editor?.setValue(this.source);
            this.clearOutput();
            disposePreview(this.previewEl);
            this.outEl.hidden = true;
        });

        actions.prepend(this.runBtn);
        actions.prepend(this.resetBtn);
        this.host.classList.add("is-runnable");
    }

    setRunning(running) {
        this.running = running;
        this.runBtn.classList.toggle("is-running", running);
        this.runBtn.innerHTML = running ? `${STOP}<span>Arrêter</span>` : `${PLAY}<span>Exécuter</span>`;
        this.host.classList.toggle("is-busy", running);
    }

    /* ---------- Éditeur Monaco ---------- */
    activate() {
        this.activating ??= this.createEditor();
        return this.activating;
    }

    async createEditor() {
        this.pre.hidden = true;

        this.editorEl = el("div", "run-editor");
        this.editorEl.style.height = `${Math.min(Math.max(this.source.split("\n").length * 21 + 24, 80), 440)}px`;
        this.editorEl.textContent = "Chargement de l'éditeur…";
        this.pre.after(this.editorEl);

        this.outEl = el("div", "run-output");
        this.outEl.hidden = true;
        this.outEl.setAttribute("role", "region");
        this.outEl.setAttribute("aria-label", "Résultat de l'exécution");
        this.outEl.setAttribute("aria-live", "polite");
        this.statusEl = el("span", "run-status");
        this.linesEl = el("div", "run-lines");
        const head = el("div", "run-output-head");
        head.append(el("span", "", "Résultat"), this.statusEl);
        this.outEl.append(head, this.linesEl);
        this.editorEl.after(this.outEl);

        // Aperçu du DOM : n'apparaît que pour le code qui construit une page (voir DomRunner.js).
        this.previewEl = el("div", "run-preview");
        this.previewEl.hidden = true;
        this.outEl.after(this.previewEl);

        let monaco;
        try {
            monaco = await loadMonaco();
        } catch (error) {
            this.editorEl.textContent = error.message;
            this.pre.hidden = false;
            this.activating = null;
            throw error;
        }
        this.monaco = monaco;
        this.editorEl.textContent = "";

        this.model = monaco.editor.createModel(
            this.source,
            this.kind,
            monaco.Uri.parse(`file:///course/block-${this.id}.${EXTENSIONS[this.kind]}`),
        );
        this.editor = monaco.editor.create(this.editorEl, {
            model: this.model,
            automaticLayout: true,
            minimap: { enabled: false },
            scrollBeyondLastLine: false,
            lineNumbersMinChars: 3,
            folding: false,
            renderLineHighlight: "none",
            overviewRulerLanes: 0,
            hideCursorInOverviewRuler: true,
            fixedOverflowWidgets: true,
            padding: { top: 10, bottom: 10 },
            fontFamily: '"JetBrains Mono", ui-monospace, Menlo, Consolas, monospace',
            fontSize: 13.5,
            tabSize: 4,
            scrollbar: { alwaysConsumeMouseWheel: false },
            ariaLabel: "Éditeur de code",
        });
        this.editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, () => this.run());
        this.editor.onDidContentSizeChange(() => this.fit());
        this.fit();
        this.resetBtn.hidden = false;
        this.maybeAddStdin();
    }

    fit() {
        const height = Math.min(Math.max(this.editor.getContentHeight(), 80), 440);
        this.editorEl.style.height = `${height}px`;
        this.editor.layout();
    }

    /** Python : zone de saisie pour les appels à input(). */
    maybeAddStdin() {
        if (this.kind !== "python" || this.stdinEl || !/\binput\s*\(/.test(this.editor.getValue())) return;
        if (PythonRunner.canPrompt && !this.needsStdin) return;      // input() interactif : pas besoin de saisie préalable
        const details = el("details", "run-stdin");
        details.open = true;
        details.append(el("summary", "", "Entrée standard (pour input())"));
        this.stdinEl = el("textarea");
        this.stdinEl.rows = 2;
        this.stdinEl.placeholder = "Une ligne par appel à input()";
        this.stdinEl.setAttribute("aria-label", "Entrée standard");
        details.append(this.stdinEl);
        this.editorEl.after(details);
    }

    /**
     * input() interactif : affiche l'invite dans « Résultat » avec un champ de saisie (Entrée valide,
     * Ctrl+D sur un champ vide signale la fin d'entrée -> EOFError côté Python).
     * « secret » (getpass) : champ masqué, valeur jamais réaffichée dans la sortie.
     * @returns {Promise<string|null>}
     */
    ask(prompt, { secret = false } = {}) {
        this.cancelAsk();
        return new Promise((resolve) => {
            const line = el("div", "run-line is-out");
            const field = el("input", "run-input");
            field.type = secret ? "password" : "text";
            field.autocomplete = secret ? "new-password" : "off";
            field.spellcheck = false;
            field.setAttribute("aria-label", prompt || "Saisie demandée par input()");
            line.append(document.createTextNode(prompt), field);
            this.linesEl.append(line);
            this.lines++;
            this.statusEl.textContent = "En attente de saisie…";
            field.focus({ preventScroll: true });
            line.scrollIntoView({ block: "nearest" });

            const close = (value) => {
                field.replaceWith(document.createTextNode(secret ? "" : field.value));
                this.statusEl.textContent = "";
                this.pendingAsk = null;
                resolve(value);
            };
            field.addEventListener("keydown", (event) => {
                if (event.key === "Enter") {
                    event.preventDefault();
                    close(field.value);
                } else if (event.key.toLowerCase() === "d" && event.ctrlKey && !field.value) {
                    event.preventDefault();
                    close(null);
                }
            });
            this.pendingAsk = { line, field, resolve };
        });
    }

    /** Ferme un champ de saisie resté ouvert (exécution arrêtée, interrompue ou terminée). */
    cancelAsk() {
        const pending = this.pendingAsk;
        if (!pending) return;
        this.pendingAsk = null;
        pending.field.replaceWith(document.createTextNode(pending.field.type === "password" ? "" : pending.field.value));
        pending.resolve(null);
    }

    /* ---------- Sortie ---------- */
    clearOutput() {
        this.cancelAsk();
        this.linesEl?.replaceChildren();
        this.lines = 0;
        if (this.statusEl) this.statusEl.textContent = "";
    }

    print(kind, text) {
        if (this.lines >= MAX_LINES) {
            if (this.lines === MAX_LINES) {
                this.linesEl.append(el("div", "run-line is-warn", "… sortie tronquée"));
                this.lines++;
            }
            return;
        }
        const line = el("div", `run-line is-${kind}`);
        line.textContent = text;
        this.linesEl.append(line);
        this.lines++;
        if (kind === "err" && /EOFError/.test(text) && this.stdinEl) {
            this.print("info", "Ce programme attend une saisie : renseignez « Entrée standard » sous l'éditeur.");
        }
    }

    /* ---------- Exécution ---------- */
    async run() {
        if (this.running) return;
        try {
            await this.activate();
        } catch {
            return;
        }
        this.maybeAddStdin();
        this.clearOutput();
        disposePreview(this.previewEl);
        this.outEl.hidden = false;
        this.setRunning(true);

        const hooks = {
            out: (kind, text) => this.print(kind, text),
            status: (text) => { this.statusEl.textContent = text; },
            input: (prompt, options) => this.ask(prompt, options),
            // Python sans JSPI : retombe sur la zone « Entrée standard »
            mode: (mode) => { if (mode === "batch") { this.needsStdin = true; this.maybeAddStdin(); } },
        };
        const code = this.editor.getValue();
        const started = performance.now();

        // Le code qui touche au DOM (document, window, localStorage…) ne peut pas tourner dans un
        // worker : il s'exécute dans un iframe isolé dont le résultat s'affiche sous « Résultat ».
        const execute = usesDom(code)
            ? (js, h) => runInDom(js, h, { container: this.previewEl })
            : runJavaScript;

        if (this.kind === "python") {
            this.job = PythonRunner.run(code, hooks, { stdin: this.stdinEl?.value ?? "" });
        } else if (this.kind === "typescript") {
            this.job = runTypeScript(this.monaco, this.model, hooks, execute);
        } else {
            this.job = execute(code, hooks);
        }

        const result = await this.job.promise;
        this.job = null;
        this.cancelAsk();
        this.setRunning(false);

        const elapsed = Math.round(performance.now() - started);
        if (result.ok) {
            if (!this.lines) this.print("info", "(aucune sortie)");
            this.statusEl.textContent = `✓ Terminé en ${elapsed} ms`;
        } else if (result.reason === "stopped") {
            this.statusEl.textContent = "Exécution arrêtée";
        } else {
            this.statusEl.textContent = "✗ Échec";
        }
    }

    stop() {
        this.job?.stop();
    }
}

export class RunnableBlocks {
    static init() {
        if (document.body.dataset.runnable !== "true") return;
        document.querySelectorAll(".markdown-body .code-block").forEach((host) => {
            const code = host.querySelector("pre code");
            const kind = code && detectKind(code);
            if (!kind || !isRunnable(kind, code.textContent, code)) return;
            new RunnableBlock(host, kind, code.textContent.replace(/\n$/, ""));
        });
    }
}
