import { loadMonaco } from "../../../language/js/runner/MonacoLoader.js";
import { PythonRunner } from "../../../language/js/runner/PythonRunner.js";
import { ConsoleRenderer } from "../console/ConsoleRenderer.js";
import { DropdownEvents } from "../events/DropdownEvents.js";
import { FileStore, MAIN_FILE, MAX_CHARS, MAX_FILES, validateName } from "./FileStore.js";

/**
 * Éditeur Python en ligne : plusieurs fichiers (main.py + modules importables), Monaco, exécution
 * dans Pyodide (Web Worker), console façon Chrome et input() interactif.
 */

const RUN_TIMEOUT = 5 * 60 * 1000;      // l'élève peut arrêter à tout moment : délai large
const SAVE_DELAY = 400;
const WRAP_KEY = "python-editor:wrap";
const MARKER_OWNER = "python-run";

const LANGUAGES = { py: "python", json: "json", md: "markdown", html: "html", css: "css", js: "javascript" };
const languageOf = (name) => LANGUAGES[name.split(".").pop().toLowerCase()] ?? "plaintext";

const PLAY = '<svg class="icon" viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path fill="currentColor" d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393z"/></svg>';
const STOP = '<svg class="icon" viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><rect x="3.5" y="3.5" width="9" height="9" rx="1.5" fill="currentColor"/></svg>';

const $ = (id) => document.getElementById(id);

function el(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
}

export class PythonEditorApp {
    constructor() {
        this.store = new FileStore();
        this.console = new ConsoleRenderer($("console"));
        this.models = new Map();
        this.viewStates = new Map();
        this.running = false;
        this.job = null;
        this.saveTimer = null;
        this.renaming = null;
        this.monaco = null;
        this.editor = null;
    }

    async start() {
        this.bindUi();
        this.renderTabs();
        this.setStatus("Chargement de l'éditeur…");
        if (!this.store.persistent) {
            this.notify("Le stockage local du navigateur est indisponible : vos fichiers ne seront pas conservés.", true);
        }
        try {
            this.monaco = await loadMonaco();
        } catch (error) {
            this.setStatus("");
            this.notify(error.message, true);
            return;
        }
        await this.createEditor();
        this.activate(this.store.active);
        this.setStatus("");
        $("run-code").disabled = false;
    }

    /* ------------------------------------------------------------------ Monaco */

    async #preferences() {
        try {
            const response = await fetch("/editor/api/load-monaco-config/");
            return response.ok ? await response.json() : {};
        } catch {
            return {};
        }
    }

    async createEditor() {
        const monaco = this.monaco;
        const prefs = await this.#preferences();
        let wrap = null;
        try { wrap = localStorage.getItem(WRAP_KEY); } catch { /* stockage bloqué */ }

        this.editor = monaco.editor.create($("py-editor"), {
            minimap: { enabled: false },
            scrollBeyondLastLine: false,
            tabSize: 4,
            insertSpaces: true,
            fontSize: 14,
            ...prefs,
            ...(wrap ? { wordWrap: wrap } : {}),
            model: null,
            automaticLayout: true,
            ariaLabel: "Code Python",
        });
        this.editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, () => this.run());
        this.editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyS, () => this.saveNow());
    }

    modelFor(name) {
        let model = this.models.get(name);
        if (!model) {
            model = this.monaco.editor.createModel(this.store.content(name), languageOf(name), this.monaco.Uri.parse(`file:///${name}`));
            model.onDidChangeContent(() => this.onEdit(name, model));
            this.models.set(name, model);
        }
        return model;
    }

    onEdit(name, model) {
        this.store.setContent(name, model.getValue());
        this.clearMarkers();
        this.setSaveState("Modifications non enregistrées…");
        clearTimeout(this.saveTimer);
        this.saveTimer = setTimeout(() => this.saveNow(), SAVE_DELAY);
    }

    saveNow() {
        clearTimeout(this.saveTimer);
        const ok = this.store.save();
        this.setSaveState(ok ? "Enregistré dans ce navigateur" : "Enregistrement impossible");
    }

    /* ------------------------------------------------------------------ Onglets */

    activate(name) {
        if (!this.editor || !this.store.has(name)) name = MAIN_FILE;
        const current = this.editor.getModel();
        if (current) this.viewStates.set(current.uri.path.slice(1), this.editor.saveViewState());
        this.editor.setModel(this.modelFor(name));
        const state = this.viewStates.get(name);
        if (state) this.editor.restoreViewState(state);
        this.store.active = name;
        this.renderTabs();
        if (!this.renaming) this.editor.focus();
        this.store.save();
    }

    renderTabs() {
        const list = $("py-tabs");
        list.replaceChildren();
        for (const name of this.store.names()) {
            const tab = el("div", `py-tab${name === this.store.active ? " is-active" : ""}`);
            tab.dataset.name = name;

            const button = el("button", "py-tab-label");
            button.type = "button";
            button.setAttribute("role", "tab");
            button.setAttribute("aria-selected", String(name === this.store.active));
            button.tabIndex = name === this.store.active ? 0 : -1;
            button.title = name === MAIN_FILE ? "Point d'entrée : exécuté par « Exécuter »" : "Double-clic ou F2 pour renommer";
            if (name === MAIN_FILE) button.append(el("span", "py-entry", "▶"));
            button.append(el("span", "py-tab-name", name));
            button.addEventListener("click", () => this.activate(name));
            button.addEventListener("dblclick", () => this.startRename(name));
            button.addEventListener("keydown", (event) => this.onTabKey(event, name));
            tab.append(button);

            if (name !== MAIN_FILE) {
                const close = el("button", "py-tab-close", "×");
                close.type = "button";
                close.setAttribute("aria-label", `Supprimer ${name}`);
                close.title = `Supprimer ${name}`;
                close.addEventListener("click", () => this.removeFile(name));
                tab.append(close);
            }
            list.append(tab);
        }
        $("py-add").disabled = this.store.files.length >= MAX_FILES;
    }

    onTabKey(event, name) {
        const names = this.store.names();
        const index = names.indexOf(name);
        if (event.key === "F2" && name !== MAIN_FILE) { event.preventDefault(); this.startRename(name); return; }
        if (event.key === "Delete" && name !== MAIN_FILE) { event.preventDefault(); this.removeFile(name); return; }
        const next = { ArrowRight: 1, ArrowLeft: -1 }[event.key];
        if (!next) return;
        event.preventDefault();
        this.activate(names[(index + next + names.length) % names.length]);
        $("py-tabs").querySelector('[aria-selected="true"]')?.focus();
    }

    addFile(name = this.store.freeName(), content = "") {
        const result = this.store.add(name, content);
        if (!result.ok) { this.notify(result.error, true); return null; }
        this.saveNow();
        return result.name;
    }

    newFile() {
        const name = this.addFile();
        if (!name) return;
        this.activate(name);
        this.startRename(name);
    }

    removeFile(name) {
        if (!window.confirm(`Supprimer « ${name} » ? Cette action est définitive.`)) return;
        if (!this.store.remove(name)) return;
        this.models.get(name)?.dispose();
        this.models.delete(name);
        this.viewStates.delete(name);
        this.saveNow();
        this.activate(this.store.active);
    }

    startRename(name) {
        if (name === MAIN_FILE || this.renaming) return;
        const tab = [...$("py-tabs").children].find((node) => node.dataset.name === name);
        if (!tab) return;
        this.renaming = name;

        const label = tab.querySelector(".py-tab-label");
        const input = el("input", "py-rename");
        input.type = "text";
        input.value = name;
        input.maxLength = 40;
        input.spellcheck = false;
        input.setAttribute("aria-label", `Nouveau nom de ${name}`);
        label.replaceWith(input);
        input.focus();
        input.setSelectionRange(0, name.lastIndexOf("."));

        let done = false;
        const finish = (commit) => {
            if (done) return;
            if (commit && input.value.trim() !== name) {
                const result = this.store.rename(name, input.value);
                if (!result.ok) {
                    input.setAttribute("aria-invalid", "true");
                    this.notify(result.error, true);
                    return;                      // on garde le champ ouvert pour corriger
                }
                this.applyRename(name, result.name);
            }
            done = true;
            this.renaming = null;
            this.notify("");
            this.renderTabs();
            this.editor?.focus();
        };
        input.addEventListener("keydown", (event) => {
            if (event.key === "Enter") { event.preventDefault(); finish(true); }
            else if (event.key === "Escape") { event.preventDefault(); input.value = name; finish(false); }
        });
        input.addEventListener("blur", () => {
            if (!done && input.value.trim() !== name && validateName(input.value, this.store.names(), { ignore: name }).error) {
                input.value = name;              // saisie invalide abandonnée : on revient au nom d'origine
            }
            finish(true);
        });
    }

    applyRename(oldName, newName) {
        const old = this.models.get(oldName);
        if (old) {
            const wasActive = this.editor.getModel() === old;
            const content = old.getValue();
            this.models.delete(oldName);
            this.viewStates.delete(oldName);
            if (wasActive) this.editor.setModel(null);
            old.dispose();
            this.store.setContent(newName, content);
            if (wasActive) this.editor.setModel(this.modelFor(newName));
        }
        this.store.active = this.store.active === oldName ? newName : this.store.active;
        this.saveNow();
    }

    /* ------------------------------------------------------------------ Exécution */

    async run() {
        if (this.running || !this.editor) return;
        this.saveNow();
        this.clearMarkers();
        this.console.clear();
        this.notify("");

        const code = this.store.content(MAIN_FILE);
        const everything = this.store.files.map((file) => file.content).join("\n");
        if (!PythonRunner.canPrompt && /\binput\s*\(/.test(everything)) this.showStdin();

        this.setRunning(true);
        this.setStatus("Exécution en cours…");
        const hooks = {
            out: (kind, text) => this.console.add({
                type: { err: "error", warn: "warn" }[kind] || "log",
                args: [text],
                plain: true,                       // une sortie de print() : pas de regroupement des lignes identiques
                muted: kind === "info",
            }),
            status: (text) => this.setStatus(text),
            input: (prompt, options) => {
                this.setStatus("En attente de saisie…");
                return this.console.ask(prompt, { ...options, onEnd: () => this.setStatus("") });
            },
            mode: (mode) => { if (mode === "batch") this.showStdin(); },
        };

        const started = performance.now();
        this.job = PythonRunner.run(code, hooks, {
            stdin: $("py-stdin").hidden ? "" : $("py-stdin-text").value,
            files: this.store.runFiles(),
            filename: MAIN_FILE,
            timeout: RUN_TIMEOUT,
        });
        const result = await this.job.promise;
        this.job = null;
        this.console.cancelAsk();
        this.setRunning(false);

        const elapsed = Math.round(performance.now() - started);
        if (result.ok) {
            if (this.console.rowCount === 0) this.console.add({ type: "log", args: ["(aucune sortie)"], muted: true });
            this.setStatus(`✓ Terminé en ${elapsed} ms`);
        } else if (result.reason === "stopped") {
            this.setStatus("Exécution arrêtée");
        } else {
            this.setStatus("✗ Échec");
            this.markError();
        }
    }

    stop() {
        this.job?.stop();
    }

    setRunning(running) {
        this.running = running;
        const button = $("run-code");
        button.innerHTML = running ? `${STOP} Arrêter` : `${PLAY} Exécuter`;
        button.setAttribute("aria-label", running ? "Arrêter l'exécution" : "Exécuter main.py");
        button.title = running ? "Arrêter l'exécution" : "Exécuter main.py (Ctrl+Entrée)";
        button.classList.toggle("is-running", running);
    }

    /** Souligne dans l'éditeur la dernière ligne de la trace d'erreur qui appartient à un de nos fichiers. */
    markError() {
        const rows = [...$("console").querySelectorAll(".cc-row.cc-error .cc-content")].map((node) => node.textContent);
        // main.py apparaît tel quel ; les modules importés avec leur chemin (/home/pyodide/utils.py).
        const frame = /File "(?:\/home\/pyodide\/)?([\w.-]+)", line (\d+)/;
        const trace = rows.reverse().find((text) => frame.test(text));
        if (!trace) return;
        const frames = [...trace.matchAll(new RegExp(frame, "g"))].filter((m) => this.store.has(m[1]));
        const last = frames[frames.length - 1];
        if (!last) return;

        const [, name, lineText] = last;
        const model = this.modelFor(name);
        const line = Math.min(Number(lineText), model.getLineCount());
        const message = trace.trim().split("\n").filter(Boolean).pop();
        this.monaco.editor.setModelMarkers(model, MARKER_OWNER, [{
            severity: this.monaco.MarkerSeverity.Error,
            message,
            startLineNumber: line,
            startColumn: model.getLineFirstNonWhitespaceColumn(line) || 1,
            endLineNumber: line,
            endColumn: model.getLineMaxColumn(line),
        }]);
        if (this.store.active !== name) this.activate(name);
        this.editor.revealLineInCenter(line);
    }

    clearMarkers() {
        if (!this.monaco) return;
        for (const model of this.models.values()) this.monaco.editor.setModelMarkers(model, MARKER_OWNER, []);
    }

    showStdin() {
        $("py-stdin").hidden = false;
    }

    /* ------------------------------------------------------------------ Fichiers (import / export) */

    download(name = this.store.active) {
        const blob = new Blob([this.store.content(name)], { type: "text/plain;charset=utf-8" });
        const link = el("a");
        link.href = URL.createObjectURL(blob);
        link.download = name;
        document.body.append(link);
        link.click();
        link.remove();
        setTimeout(() => URL.revokeObjectURL(link.href), 1000);
    }

    async importFiles(fileList) {
        const problems = [];
        let last = null;
        for (const file of fileList) {
            if (file.size > MAX_CHARS * 4) { problems.push(`« ${file.name} » est trop volumineux.`); continue; }
            let { name, error } = validateName(file.name, this.store.names());
            if (error && error.includes("existe déjà")) {
                const dot = file.name.lastIndexOf(".");
                name = this.store.freeName(file.name.slice(0, dot > 0 ? dot : undefined), dot > 0 ? file.name.slice(dot) : ".py");
                ({ error } = validateName(name, this.store.names()));
            }
            if (error) { problems.push(`« ${file.name} » : ${error}`); continue; }
            const added = this.addFile(name, await file.text());
            if (added) last = added;
        }
        if (last) this.activate(last);
        this.notify(problems.join(" "), problems.length > 0);
    }

    resetProject() {
        if (!window.confirm("Remplacer tous vos fichiers par l'exemple de départ ? Cette action est définitive.")) return;
        for (const model of this.models.values()) model.dispose();
        this.models.clear();
        this.viewStates.clear();
        this.store.reset();
        this.saveNow();
        this.console.clear();
        this.activate(MAIN_FILE);
    }

    toggleWrap() {
        const next = this.editor.getOption(this.monaco.editor.EditorOption.wordWrap) === "off" ? "on" : "off";
        this.editor.updateOptions({ wordWrap: next });
        try { localStorage.setItem(WRAP_KEY, next); } catch { /* stockage bloqué */ }
    }

    /* ------------------------------------------------------------------ Interface */

    setStatus(text) { $("py-status").textContent = text; }
    setSaveState(text) { $("py-save-state").textContent = text; }

    notify(text, isError = false) {
        const box = $("py-message");
        box.textContent = text;
        box.hidden = !text;
        box.classList.toggle("is-error", isError);
    }

    bindUi() {
        DropdownEvents.bind();
        $("run-code").disabled = true;
        $("run-code").addEventListener("click", () => (this.running ? this.stop() : this.run()));
        $("py-clear").addEventListener("click", () => { this.console.clear(); this.setStatus(""); });
        $("py-add").addEventListener("click", () => this.newFile());
        $("py-new").addEventListener("click", () => this.newFile());
        $("py-download").addEventListener("click", () => this.download());
        $("py-wrap").addEventListener("click", () => this.toggleWrap());
        $("py-reset").addEventListener("click", () => this.resetProject());
        $("py-import").addEventListener("click", () => $("py-import-input").click());
        $("py-import-input").addEventListener("change", async (event) => {
            await this.importFiles([...event.target.files]);
            event.target.value = "";
        });

        document.addEventListener("keydown", (event) => {
            if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
                event.preventDefault();
                if (!this.running) this.run();
            } else if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "s") {
                event.preventDefault();
                this.saveNow();
            }
        });
        window.addEventListener("pagehide", () => this.saveNow());
        window.addEventListener("beforeunload", () => this.job?.stop());
    }
}
