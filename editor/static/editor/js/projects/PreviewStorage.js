/**
 * Données ``localStorage`` du code de l'aperçu, conservées par projet dans le navigateur.
 *
 * L'aperçu est dans un bac à sable (origine opaque) et ne peut pas toucher au vrai stockage de l'application ; il
 * reçoit une copie (voir ``preview-storage.js``). Ce module fait le lien :
 *  - ``begin`` : à chaque exécution, retourne les données du projet à embarquer dans l'aperçu ;
 *  - ``handleMessage`` : reçoit les modifications de l'aperçu, les valide et les enregistre.
 *
 * Le message ne désigne jamais où écrire : la clé est celle du projet exécuté, fixée par ``begin``. L'aperçu (code de
 * l'utilisateur, donc non fiable) ne peut écrire que ses propres chaînes de caractères, dans la limite des plafonds
 * ci-dessous (mêmes valeurs que ``preview-storage.js`` et ``views.py``).
 */
const PREFIX = "preview-storage:v1:";
const MAX_CHARS = 256 * 1024;
const MAX_KEYS = 200;

let activeKey = null;

function storage() {
    try { return window.localStorage; } catch { return null; }
}

/** @returns {Record<string, string>|null} ``null`` si ``data`` n'est pas un objet de chaînes dans les plafonds. */
export function validate(data) {
    if (!data || typeof data !== "object" || Array.isArray(data)) return null;
    const entries = Object.entries(data);
    if (entries.length > MAX_KEYS) return null;
    let size = 0;
    for (const [key, value] of entries) {
        if (typeof value !== "string") return null;
        size += key.length + value.length;
    }
    return size > MAX_CHARS ? null : Object.fromEntries(entries);
}

export class PreviewStorage {
    /**
     * À appeler avant chaque aperçu.
     * @param {"web"|"ts"} kind éditeur
     * @param {number|string|undefined} projectId identifiant du projet (stable : le renommage ne change rien)
     * @returns {string} JSON à envoyer au serveur dans le champ ``storage``
     */
    static begin(kind, projectId) {
        activeKey = `${PREFIX}${kind}:${projectId ?? "default"}`;
        try {
            return JSON.stringify(validate(JSON.parse(storage()?.getItem(activeKey) ?? "{}")) ?? {});
        } catch {
            return "{}";
        }
    }

    /** Oublie les données d'un projet supprimé. */
    static forget(kind, projectId) {
        try { storage()?.removeItem(`${PREFIX}${kind}:${projectId}`); } catch { /* stockage bloqué */ }
    }

    /** @param {MessageEvent} event message ``{__storage: true, type: "write", data}`` de l'aperçu */
    static handleMessage(event) {
        const message = event.data;
        if (!message || message.__storage !== true || message.type !== "write") return;

        const frame = document.getElementById("output");
        if (!frame || event.source !== frame.contentWindow || !activeKey) return;

        const data = validate(message.data);
        if (!data) return;
        try {
            const store = storage();
            if (!Object.keys(data).length) store?.removeItem(activeKey);
            else store?.setItem(activeKey, JSON.stringify(data));
        } catch { /* stockage plein ou bloqué : l'aperçu continue, sans conservation */ }
    }
}
