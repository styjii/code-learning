/**
 * Exécuté dans l'iframe d'aperçu, avant tout autre script : fournit ``localStorage`` et ``sessionStorage``.
 *
 * L'aperçu est dans un bac à sable SANS « allow-same-origin » (origine opaque) : c'est ce qui empêche le code de
 * l'utilisateur d'atteindre la session et les données de l'application. Le navigateur y refuse donc
 * ``window.localStorage`` (« SecurityError : the document is sandboxed… »). On ne desserre pas le bac à sable : on
 * remplace ces deux objets, dans la page seulement, par des copies qui se comportent comme le vrai ``Storage``.
 *
 *  - ``sessionStorage`` : en mémoire, vide à chaque exécution ;
 *  - ``localStorage``   : en mémoire, initialisé avec les données conservées pour le projet (JSON embarqué dans la
 *    page par le serveur) ; chaque modification est envoyée à l'éditeur (message ``__storage``), qui la valide et la
 *    garde dans le navigateur. Le code de l'utilisateur ne voit jamais le vrai stockage de l'application.
 *
 * Mêmes plafonds que ``PreviewStorage.js`` (éditeur) et ``views.py`` (serveur).
 */
(function () {
    "use strict";

    try { void window.localStorage; return; } catch { /* bac à sable : on installe les copies */ }

    const MAX_CHARS = 256 * 1024;     // somme des longueurs des clés et des valeurs
    const MAX_KEYS = 200;

    function quotaError() {
        return new DOMException("The quota has been exceeded.", "QuotaExceededError");
    }

    /**
     * @param {Record<string, string>} initial contenu de départ
     * @param {(data: Record<string, string>) => void} [persist] appelé après chaque modification
     */
    function createStorage(initial, persist) {
        const data = new Map(Object.entries(initial));
        const size = () => { let n = 0; for (const [k, v] of data) n += k.length + v.length; return n; };
        const changed = () => { if (persist) persist(Object.fromEntries(data)); };

        const methods = {
            getItem(key) { key = String(key); return data.has(key) ? data.get(key) : null; },
            setItem(key, value) {
                key = String(key); value = String(value);
                const previous = data.get(key);
                data.set(key, value);
                if (size() > MAX_CHARS || data.size > MAX_KEYS) {
                    if (previous === undefined) data.delete(key); else data.set(key, previous);
                    throw quotaError();
                }
                changed();
            },
            removeItem(key) { if (data.delete(String(key))) changed(); },
            clear() { if (data.size) { data.clear(); changed(); } },
            key(index) { return [...data.keys()][Number(index)] ?? null; },
        };

        // Même prototype que le vrai Storage (instanceof, toString) ; accès par propriété : storage.clé, storage["clé"].
        const target = Object.create(typeof Storage === "function" ? Storage.prototype : Object.prototype);
        for (const [name, fn] of Object.entries(methods)) {
            Object.defineProperty(target, name, { value: fn, configurable: true, writable: true });
        }
        Object.defineProperty(target, "length", { get: () => data.size, configurable: true });

        return new Proxy(target, {
            get(t, prop, receiver) {
                if (typeof prop === "string" && data.has(prop) && !(prop in methods) && prop !== "length") return data.get(prop);
                return Reflect.get(t, prop, receiver);
            },
            set(t, prop, value) {
                if (typeof prop === "symbol") return Reflect.set(t, prop, value);
                methods.setItem(prop, value);
                return true;
            },
            deleteProperty(t, prop) {
                if (typeof prop === "string") methods.removeItem(prop);
                return true;
            },
            has(t, prop) { return (typeof prop === "string" && data.has(prop)) || Reflect.has(t, prop); },
            ownKeys() { return [...data.keys()]; },
            getOwnPropertyDescriptor(t, prop) {
                if (typeof prop === "string" && data.has(prop)) {
                    return { value: data.get(prop), writable: true, enumerable: true, configurable: true };
                }
                return undefined;
            },
        });
    }

    let initial = {};
    try {
        const parsed = JSON.parse(document.getElementById("preview-storage-data")?.textContent || "{}");
        if (parsed && typeof parsed === "object" && !Array.isArray(parsed)) {
            for (const [key, value] of Object.entries(parsed)) if (typeof value === "string") initial[key] = value;
        }
    } catch { initial = {}; }

    // Envoi groupé : une rafale de setItem ne produit qu'un message.
    let timer = null;
    let latest = null;
    const flush = () => {
        clearTimeout(timer);
        timer = null;
        if (latest === null) return;
        const data = latest;
        latest = null;
        try { parent.postMessage({ __storage: true, type: "write", data }, "*"); } catch { /* page ouverte seule */ }
    };
    const persist = (data) => { latest = data; if (timer === null) timer = setTimeout(flush, 150); };
    window.addEventListener("pagehide", flush);

    const local = createStorage(initial, persist);
    const session = createStorage({});
    for (const [name, value] of [["localStorage", local], ["sessionStorage", session]]) {
        try {
            Object.defineProperty(window, name, { get: () => value, configurable: true, enumerable: true });
        } catch { /* le navigateur refuse : l'aperçu garde l'erreur d'origine, sans danger */ }
    }
})();
