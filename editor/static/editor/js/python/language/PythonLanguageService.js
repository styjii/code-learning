/**
 * Détection d'erreurs, autocomplétion, infobulles et aide aux appels pour Python dans Monaco.
 *
 * Monaco embarque un service de langage complet pour JavaScript et TypeScript, mais aucun pour Python : sans
 * ce module, l'éditeur Python ne fait que la coloration syntaxique. L'analyse est faite par jedi et pyflakes
 * dans un Pyodide dédié (voir python-language.worker.js et language_service.py) ; ce fichier relie ce worker
 * aux mécanismes de Monaco.
 *
 * Si le service ne démarre pas (réseau coupé, navigateur trop ancien…), l'éditeur reste pleinement utilisable :
 * seules ces aides disparaissent, et `onState("failed", erreur)` en avertit l'interface.
 */

const MARKER_OWNER = "python-lint";
const LINT_DELAY = 500;                  // ms après la dernière frappe
const REQUEST_TIMEOUT = 8000;            // une complétion plus lente que ça n'a plus d'intérêt
const START_TIMEOUT = 180000;            // premier chargement de Pyodide sur une connexion lente
const START_RETRY_DELAYS = [2000, 10000, 30000];   // relances automatiques si le démarrage échoue (réseau instable…)
const RETRY_AFTER = 30000;               // après un échec définitif : nouvelle tentative à la requête suivante, au plus toutes les 30 s
const MAX_TIMEOUTS = 3;                  // réponses manquées de suite avant de relancer le worker
const MAX_RESTARTS = 2;

const nameOf = (model) => model.uri.path.slice(1);

/** Dialogue avec le worker : une requête = une promesse, avec délai d'attente. */
export class LanguageClient {
    #settings;
    #limits;
    #onState;
    #worker = null;
    #starting = null;
    #pending = new Map();
    #nextId = 1;
    #timeouts = 0;
    #restarts = 0;
    #startRetries = 0;
    #failedAt = 0;

    /** @type {"idle"|"loading"|"ready"|"failed"} */
    state = "idle";

    /** Appelé chaque fois que le service devient prêt (premier démarrage, relance, reprise après échec). */
    onReady = null;

    constructor(settings, onState = () => {}) {
        this.#settings = settings;
        this.#limits = { request: settings.requestTimeout ?? REQUEST_TIMEOUT, start: settings.startTimeout ?? START_TIMEOUT };
        this.#onState = onState;
    }

    /** Démarre le worker (une seule fois ; les appels suivants renvoient la même promesse). */
    start() {
        if (this.#starting) return this.#starting;
        this.#setState("loading");
        this.#starting = this.#boot().then(
            () => {
                this.#startRetries = 0;
                this.#setState("ready");
            },
            (error) => this.#startFailed(error),
        );
        return this.#starting;
    }

    /**
     * Un démarrage raté (coupure réseau, délai dépassé) n'est plus définitif : les fichiers déjà téléchargés sont
     * en cache, donc la relance est bien plus rapide. L'état reste « loading » pendant les relances.
     */
    #startFailed(error) {
        this.#teardown(error);
        if (!error?.fatal && this.#startRetries < START_RETRY_DELAYS.length) {
            const delay = START_RETRY_DELAYS[this.#startRetries++];
            return new Promise((resolve) => setTimeout(() => {
                this.#starting = null;
                resolve(this.start());
            }, delay));
        }
        this.#fail(error);
    }

    #fail(error) {
        this.#failedAt = Date.now();
        this.#setState("failed", error);
    }

    async #boot() {
        const missing = ["indexURL", "toolsURL", "serviceURL"].filter((key) => !this.#settings[key]);
        if (missing.length) throw Object.assign(new Error(`réglage manquant : ${missing.join(", ")}`), { fatal: true });

        const worker = new Worker(new URL("./python-language.worker.js", import.meta.url), { type: "module" });
        this.#worker = worker;
        worker.onmessage = ({ data }) => this.#onMessage(data);
        worker.onerror = (event) => {
            event.preventDefault?.();
            const error = new Error(event.message || "erreur dans le worker");
            this.#teardown(error);
            // Pendant le démarrage, le rejet de « init » déclenche les relances ; ensuite, le service est perdu.
            if (this.state !== "loading") this.#fail(error);
        };
        await this.#send("init", [this.#settings], this.#limits.start);
    }

    /**
     * @returns {Promise<any>} le résultat, ou `undefined` si le service est indisponible, trop lent ou en erreur
     *   (`null` est un résultat valide : « rien à signaler »).
     */
    async request(method, args) {
        if (this.state === "failed") {
            if (Date.now() - this.#failedAt < RETRY_AFTER) return undefined;
            this.#startRetries = 0;          // l'élève continue d'écrire : on retente le démarrage
            this.#restarts = 0;
            this.#starting = null;
        }
        await this.start();
        if (this.state !== "ready") return undefined;
        try {
            const result = await this.#send(method, args, this.#limits.request);
            this.#timeouts = 0;
            return result;
        } catch (error) {
            if (error?.timeout && ++this.#timeouts >= MAX_TIMEOUTS) this.#restart();
            return undefined;
        }
    }

    dispose() {
        this.#teardown(new Error("service arrêté"));
        this.#starting = null;
        this.#setState("idle");
    }

    #send(method, args, timeout) {
        return new Promise((resolve, reject) => {
            const id = this.#nextId++;
            const timer = setTimeout(() => {
                this.#pending.delete(id);
                reject(Object.assign(new Error(`délai dépassé : ${method}`), { timeout: true }));
            }, timeout);
            this.#pending.set(id, { resolve, reject, timer });
            this.#worker.postMessage({ id, method, args });
        });
    }

    #onMessage({ id, ok, result, error }) {
        const request = this.#pending.get(id);
        if (!request) return;               // réponse tardive à une requête déjà abandonnée
        clearTimeout(request.timer);
        this.#pending.delete(id);
        if (ok) request.resolve(result);
        else request.reject(new Error(error));
    }

    /** Un worker qui ne répond plus ne peut pas être interrompu : on le remplace. */
    #restart() {
        this.#timeouts = 0;
        this.#teardown(new Error("worker relancé"));
        this.#starting = null;
        if (++this.#restarts > MAX_RESTARTS) {
            this.#fail(new Error("le service d'analyse ne répond plus"));
            return;
        }
        this.#setState("idle");
        this.start();
    }

    #teardown(reason) {
        this.#worker?.terminate();
        this.#worker = null;
        for (const { reject, timer } of this.#pending.values()) {
            clearTimeout(timer);
            reject(reason);
        }
        this.#pending.clear();
    }

    #setState(state, detail) {
        this.state = state;
        this.#onState(state, detail);
        if (state === "ready") this.onReady?.();
    }
}

/** Client prêt à l'emploi : n'a pas besoin de Monaco, donc peut démarrer (et télécharger Pyodide) tout de suite. */
export function createLanguageClient(onState) {
    return new LanguageClient({
        indexURL: document.body.dataset.pyodide,
        toolsURL: document.body.dataset.pythonTools,
        serviceURL: new URL("./language_service.py", import.meta.url).href,
    }, onState);
}

export class PythonLanguageService {
    #monaco;
    #client;
    #getFiles;
    #synced = new Map();                 // nom -> contenu déjà transmis au worker
    #relints = new Set();                // une fonction « ré-analyser maintenant » par modèle suivi
    #disposables = [];

    /**
     * @param monaco l'objet Monaco chargé par loadMonaco()
     * @param {object} options
     * @param {() => Record<string, string>} options.getFiles tous les fichiers du projet (nom -> contenu)
     * @param {(state: string, detail?: Error) => void} [options.onState]
     * @param {object} [options.client] remplace le dialogue avec le worker (tests)
     */
    constructor(monaco, { getFiles, onState, client } = {}) {
        this.#monaco = monaco;
        this.#getFiles = getFiles;
        this.#client = client ?? createLanguageClient(onState);
        // Dès que le service est prêt (ou revient après une panne) : le worker repart de zéro, donc on lui renvoie
        // le projet et on ré-analyse tous les fichiers ouverts, sans attendre la prochaine frappe.
        this.#client.onReady = () => this.#relintAll();
        this.#register();
    }

    /** Lance le chargement en arrière-plan (sans attendre : l'éditeur ne doit pas en dépendre). */
    start() {
        return this.#client.start();
    }

    /** Souligne les erreurs de `model` pendant qu'on le modifie. À appeler une fois par modèle Python. */
    watch(model) {
        if (model.getLanguageId() !== "python") return;
        let timer = null;
        const schedule = (delay) => {
            clearTimeout(timer);
            timer = setTimeout(() => this.#lint(model), delay);
        };
        const subscription = model.onDidChangeContent(() => schedule(LINT_DELAY));
        model.onWillDispose(() => {
            clearTimeout(timer);
            subscription.dispose();
            this.#relints.delete(schedule);
        });
        this.#relints.add(schedule);
        schedule(0);
    }

    #relintAll() {
        this.#synced.clear();
        for (const schedule of this.#relints) schedule(0);
    }

    dispose() {
        for (const disposable of this.#disposables) disposable.dispose();
        this.#disposables = [];
        this.#client.dispose?.();
    }

    /* ------------------------------------------------------------------ Détection d'erreurs */

    async #lint(model) {
        if (model.isDisposed()) return;
        const version = model.getVersionId();
        const diagnostics = await this.#call("lint", [model.getValue(), nameOf(model)]);
        // Réponse périmée (le texte a changé entre-temps) ou modèle fermé : un autre calcul la remplacera.
        if (!diagnostics || model.isDisposed() || model.getVersionId() !== version) return;
        this.#monaco.editor.setModelMarkers(model, MARKER_OWNER, diagnostics.map((item) => this.#toMarker(item)));
    }

    #toMarker(item) {
        const { MarkerSeverity, MarkerTag } = this.#monaco;
        return {
            severity: item.severity === "error" ? MarkerSeverity.Error : MarkerSeverity.Warning,
            message: item.message,
            startLineNumber: item.line,
            startColumn: item.col,
            endLineNumber: item.endLine,
            endColumn: item.endCol,
            source: item.code === "SyntaxError" ? "Python" : "pyflakes",
            code: item.code,
            tags: item.unused ? [MarkerTag.Unnecessary] : undefined,    // estompé, comme l'éditeur TypeScript
        };
    }

    /* ------------------------------------------------------------------ Dialogue avec le worker */

    /** Transmet d'abord les fichiers modifiés depuis le dernier échange (jedi lit les autres modules sur disque). */
    async #syncProject() {
        const files = Object.fromEntries(Object.entries(this.#getFiles()).filter(([name]) => name.endsWith(".py")));
        const changed = Object.fromEntries(Object.entries(files).filter(([name, content]) => this.#synced.get(name) !== content));
        const removed = [...this.#synced.keys()].filter((name) => !(name in files));
        if (!Object.keys(changed).length && !removed.length) return;

        // Le worker traite les messages dans l'ordre : la requête suivante verra ces fichiers sans attendre l'accusé.
        for (const [name, content] of Object.entries(changed)) this.#synced.set(name, content);
        for (const name of removed) this.#synced.delete(name);
        const done = await this.#client.request("sync_project", [JSON.stringify({ files: changed, remove: removed })]);
        if (done === undefined) this.#synced.clear();       // non remis : on renverra tout la prochaine fois
    }

    async #call(method, args) {
        await this.#syncProject();
        return this.#client.request(method, args);
    }

    /* ------------------------------------------------------------------ Fournisseurs Monaco */

    #register() {
        const { languages, Range } = this.#monaco;
        const kinds = languages.CompletionItemKind;
        const KIND = {
            module: kinds.Module, class: kinds.Class, function: kinds.Function, variable: kinds.Variable,
            property: kinds.Property, keyword: kinds.Keyword, file: kinds.File, text: kinds.Text,
        };
        const at = (model, position) => [model.getValue(), position.lineNumber, position.column, nameOf(model)];

        this.#disposables.push(
            languages.registerCompletionItemProvider("python", {
                triggerCharacters: ["."],
                provideCompletionItems: async (model, position, _context, token) => {
                    const result = await this.#call("complete", at(model, position));
                    if (!result || token.isCancellationRequested) return { suggestions: [] };
                    const word = model.getWordUntilPosition(position);
                    const range = new Range(position.lineNumber, word.startColumn, position.lineNumber, word.endColumn);
                    return {
                        suggestions: result.items.map((item) => ({
                            label: item.label,
                            kind: KIND[item.kind] ?? kinds.Text,
                            insertText: item.insert,
                            detail: item.detail,
                            sortText: item.sort,
                            range,
                            // Pour resolveCompletionItem : la documentation n'est demandée qu'à la suggestion sélectionnée.
                            _doc: { token: result.token, index: item.index },
                        })),
                    };
                },
                resolveCompletionItem: async (item) => {
                    if (!item._doc) return item;
                    const doc = await this.#client.request("completion_doc", [item._doc.token, item._doc.index]);
                    if (doc) item.documentation = { value: `\`\`\`text\n${doc}\n\`\`\`` };
                    return item;
                },
            }),

            languages.registerHoverProvider("python", {
                provideHover: async (model, position) => {
                    const result = await this.#call("hover", at(model, position));
                    if (!result) return null;
                    return {
                        range: new Range(result.line, result.startCol, result.line, result.endCol),
                        contents: [{ value: result.markdown }],
                    };
                },
            }),

            languages.registerSignatureHelpProvider("python", {
                signatureHelpTriggerCharacters: ["(", ","],
                signatureHelpRetriggerCharacters: [")"],
                provideSignatureHelp: async (model, position) => {
                    const result = await this.#call("signature", at(model, position));
                    if (!result) return null;
                    return {
                        value: {
                            signatures: result.signatures.map((signature) => ({
                                label: signature.label,
                                documentation: signature.doc ? { value: `\`\`\`text\n${signature.doc}\n\`\`\`` } : undefined,
                                parameters: signature.params.map((offsets) => ({ label: offsets ?? [0, 0] })),
                            })),
                            activeSignature: 0,
                            activeParameter: result.param,
                        },
                        dispose() {},
                    };
                },
            }),
        );
    }
}
