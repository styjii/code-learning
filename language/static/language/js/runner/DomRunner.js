/**
 * Exécute du JavaScript qui a besoin du navigateur (document, window, localStorage, événements…)
 * dans un <iframe> isolé : « sandbox="allow-scripts" » sans « allow-same-origin », donc sans accès
 * aux cookies, au stockage ni à la session du site.
 *
 * Le runtime est celui du worker (js.worker.js : console, minuteurs, suivi de fetch, await de
 * premier niveau…) : son code est lu une seule fois puis exécuté dans l'iframe avec un « self »
 * redirigé, de sorte que les deux modes se comportent de la même façon.
 *
 * Contrat identique aux autres runners : { promise: Promise<{ok, reason?}>, stop() }.
 * Une fois l'exécution terminée, l'iframe reste vivante : les boutons et événements du résultat
 * continuent de fonctionner (et leurs console.log s'affichent). Elle est détruite par disposePreview().
 */

/** Mots-clés qui signalent un code dépendant du DOM / des API de la page. */
const DOM_PATTERN = new RegExp(
    "\\b(?:document|window|localStorage|sessionStorage|navigator|location|history|customElements|"
    + "HTML\\w*Element|(?:Mutation|Intersection|Resize)Observer|getComputedStyle|requestAnimationFrame|"
    + "cancelAnimationFrame|CustomEvent|DOMParser)\\b"
    + "|\\b(?:globalThis|self)\\.(?:document|window)\\b",
);

export const usesDom = (source) => DOM_PATTERN.test(source.replace(/\/\/.*$|\/\*[\s\S]*?\*\//gm, ""));

let workerSource = null;
const loadWorkerSource = () => (workerSource ??= fetch(new URL("./js.worker.js", import.meta.url)).then((r) => {
    if (!r.ok) throw new Error(`js.worker.js introuvable (HTTP ${r.status})`);
    return r.text();
}).catch((error) => { workerSource = null; throw error; }));

/**
 * Démarré dans l'iframe. Reçoit {type:"init", token, workerSource, code}, installe un stockage
 * en mémoire (localStorage est interdit dans une iframe isolée), exécute le runtime du worker
 * avec un « self » redirigé vers window et relaie ses messages au parent.
 */
const BOOTSTRAP = `
(() => {
    const makeStorage = () => {
        const data = new Map();
        const api = {
            getItem: (k) => (data.has(String(k)) ? data.get(String(k)) : null),
            setItem: (k, v) => { data.set(String(k), String(v)); },
            removeItem: (k) => { data.delete(String(k)); },
            clear: () => data.clear(),
            key: (i) => [...data.keys()][i] ?? null,
        };
        return new Proxy(api, {
            get: (t, k) => (k === "length" ? data.size : k in t ? t[k] : typeof k === "string" && data.has(k) ? data.get(k) : undefined),
            set: (t, k, v) => { data.set(String(k), String(v)); return true; },
            deleteProperty: (t, k) => { data.delete(String(k)); return true; },
            has: (t, k) => k in t || data.has(k),
            ownKeys: () => [...data.keys()],
            getOwnPropertyDescriptor: (t, k) => (data.has(k) ? { value: data.get(k), enumerable: true, configurable: true, writable: true } : undefined),
        });
    };
    for (const name of ["localStorage", "sessionStorage"]) {
        try { Object.defineProperty(window, name, { value: makeStorage(), configurable: true }); } catch {}
    }

    // document.cookie lève une SecurityError dans un document isolé : jar en mémoire équivalent.
    const jar = new Map();
    try {
        Object.defineProperty(document, "cookie", {
            configurable: true,
            get: () => [...jar].map(([k, v]) => k + "=" + v).join("; "),
            set: (text) => {
                const [pair, ...attrs] = String(text).split(";");
                const eq = pair.indexOf("=");
                const name = (eq < 0 ? "" : pair.slice(0, eq)).trim();
                const value = (eq < 0 ? pair : pair.slice(eq + 1)).trim();
                let expired = false;
                for (const attr of attrs) {
                    const [key, ...rest] = attr.split("=");
                    const val = rest.join("=").trim();
                    if (key.trim().toLowerCase() === "max-age" && Number(val) <= 0) expired = true;
                    if (key.trim().toLowerCase() === "expires" && Date.parse(val) <= Date.now()) expired = true;
                }
                if (expired) jar.delete(name); else jar.set(name, value);
            },
        });
    } catch {}

    // pushState/replaceState avec une URL sont refusés (origine opaque) : on garde l'état, sans l'URL.
    for (const method of ["pushState", "replaceState"]) {
        const native = history[method].bind(history);
        history[method] = (state, title, url) => {
            try { return native(state, title, url); }
            catch (error) { if (error && error.name === "SecurityError") return native(state, title); throw error; }
        };
    }

    window.addEventListener("message", (event) => {
        if (event.source !== parent || !event.data || event.data.type !== "init") return;
        const { token, workerSource, code } = event.data;
        const post = (message) => parent.postMessage({ course: token, ...message }, "*");
        let onmessage = null;

        const proxy = new Proxy(window, {
            get(target, key) {
                if (key === "postMessage") return post;
                if (key === "onmessage") return onmessage;
                const value = target[key];
                return typeof value === "function" && !/^[A-Z]/.test(String(key)) ? value.bind(target) : value;
            },
            set(target, key, value) {
                if (key === "onmessage") onmessage = value;
                else target[key] = value;
                return true;
            },
        });

        const report = () => post({
            type: "size",
            height: Math.ceil(document.documentElement.getBoundingClientRect().height),
            empty: !document.body || (!document.body.childElementCount && !document.body.textContent.trim()),
        });
        // Un conteneur masqué (display:none) n'a pas de mise en page : le ResizeObserver seul ne
        // préviendrait jamais le parent que du contenu est apparu, d'où le MutationObserver.
        new ResizeObserver(report).observe(document.documentElement);
        new MutationObserver(report).observe(document, { childList: true, subtree: true, characterData: true, attributes: true });

        try {
            new Function("self", workerSource)(proxy);
        } catch (error) {
            post({ type: "error", text: "Erreur d'initialisation : " + error.message });
            return;
        }
        onmessage({ data: { code } });
    }, { once: true });
})();
`;

const PAGE_STYLE = "html{color-scheme:light}body{margin:12px;font:14px/1.5 system-ui,sans-serif;color:#1f2328;background:#fff}";

/** Détruit l'aperçu d'un conteneur (iframe + écouteur de messages) et le masque. */
export function disposePreview(container) {
    container?._disposePreview?.();
}

/**
 * @param {string} code JavaScript à exécuter (le TypeScript est déjà compilé).
 * @param {{out: Function}} hooks
 * @param {{container: HTMLElement, timeout?: number}} options container : zone d'aperçu de la page.
 */
export function runInDom(code, hooks, { container, timeout = 8000 }) {
    disposePreview(container);
    const token = Math.random().toString(36).slice(2);
    const frame = document.createElement("iframe");
    frame.className = "run-preview-frame";
    frame.title = "Aperçu de l'exécution";
    frame.setAttribute("sandbox", "allow-scripts");
    frame.srcdoc = `<!doctype html><html><head><meta charset="utf-8"><style>${PAGE_STYLE}</style>`
        + `<script>${BOOTSTRAP}<\/script></head><body></body></html>`;

    let finish = () => {};
    let timer = null;
    let finished = false;   // l'aperçu reste visible pendant l'exécution (le DOM a besoin d'une mise en page réelle)
    let empty = true;

    const onMessage = (event) => {
        if (event.source !== frame.contentWindow || event.data?.course !== token) return;
        const data = event.data;
        if (data.type === "log") {
            hooks.out(data.kind, data.text);
        } else if (data.type === "size") {
            empty = !!data.empty;
            if (finished) container.hidden = empty;
            if (!empty) frame.style.height = `${Math.min(Math.max(data.height, 40), 520)}px`;
        } else if (data.type === "done") {
            settle({ ok: true });
        } else if (data.type === "error") {
            hooks.out("err", data.text);
            if (data.hint) hooks.out("info", data.hint);
            settle({ ok: false, reason: "error" });
        }
    };

    const settle = (result) => {
        finished = true;
        container.hidden = empty;
        finish(result);
    };

    const dispose = () => {
        clearTimeout(timer);
        window.removeEventListener("message", onMessage);
        frame.remove();
        container.hidden = true;
        container._disposePreview = null;
    };
    window.addEventListener("message", onMessage);
    container._disposePreview = dispose;

    const promise = new Promise((resolve) => {
        finish = (result) => {
            clearTimeout(timer);
            resolve(result);
        };
        timer = setTimeout(() => {
            hooks.out("warn", `Exécution interrompue après ${timeout / 1000} s (boucle infinie ou minuteur toujours actif ?).`);
            dispose();
            resolve({ ok: false, reason: "timeout" });
        }, timeout);

        loadWorkerSource().then((source) => {
            frame.addEventListener("load", () => {
                frame.contentWindow.postMessage({ type: "init", token, workerSource: source, code }, "*");
            }, { once: true });
            const label = el("div", "run-preview-label", "Aperçu");
            container.replaceChildren(label, frame);
            container.hidden = false;
        }, (error) => {
            hooks.out("err", error.message);
            dispose();
            resolve({ ok: false, reason: "error" });
        });
    });

    return {
        promise,
        stop: () => { dispose(); finish({ ok: false, reason: "stopped" }); },
    };
}

function el(tag, className, text) {
    const node = document.createElement(tag);
    node.className = className;
    node.textContent = text;
    return node;
}
