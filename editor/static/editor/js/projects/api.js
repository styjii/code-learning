/**
 * Adresses de l'API des projets, communes aux trois éditeurs : ``/editor/api/<éditeur>/projects/...``.
 * L'éditeur est l'un des identifiants ci-dessous ; le serveur applique les règles propres à chacun (``editors.py``).
 */
export const CODELAB_JS = "codelab-js";
export const CODELAB_TS = "codelab-ts";
export const CODELAB_PY = "codelab-py";

/** Liste des projets d'un éditeur, ou un projet précis si ``id`` est donné. */
export const projectsUrl = (editor, id) => `/editor/api/${editor}/projects/${id === undefined ? "" : `${id}/`}`;

/** Archive .zip d'un projet construite par le serveur à partir de la base. */
export const exportZipUrl = (editor, id) => `${projectsUrl(editor, id)}export-zip/`;

/** Import d'une archive .zip : le serveur crée un nouveau projet en base (le projet ouvert n'est pas touché). */
export const importZipUrl = (editor) => `${projectsUrl(editor)}import-zip/`;

/**
 * Lit en mémoire le fichier .zip choisi. Un navigateur qui relit un fichier du disque au moment de l'envoi peut le
 * trouver verrouillé ou modifié (téléchargement tout juste terminé, antivirus...) et abandonner la requête avec le
 * seul message « Failed to fetch » ; lu une fois ici, il peut aussi être renvoyé (écraser, renommer) sans nouvelle lecture.
 * @param {File} file
 * @returns {Promise<{buffer: ArrayBuffer, name: string}>}
 */
export async function readZip(file) {
    try {
        return { buffer: await file.arrayBuffer(), name: file.name };
    } catch {
        throw new Error("fichier illisible (déplacé, modifié ou verrouillé). Sélectionnez-le de nouveau.");
    }
}

/**
 * Corps (``FormData``) d'un import : l'archive et, au besoin, ``name`` (nom imposé) et ``on_conflict`` (``overwrite``).
 * @param {{buffer: ArrayBuffer, name: string}} archive
 * @param {Record<string, string>} [fields]
 * @returns {FormData}
 */
export function zipForm(archive, fields = {}) {
    const formData = new FormData();
    formData.append("zip_file", new Blob([archive.buffer], { type: "application/zip" }), archive.name);
    for (const [key, value] of Object.entries(fields)) formData.append(key, value);
    return formData;
}

/**
 * Envoie l'import. Une requête qui n'aboutit pas du tout (serveur arrêté ou redémarré, certificat refusé,
 * connexion coupée) lève « Failed to fetch » : on la remplace par un message qui dit quoi faire.
 * @param {string} url
 * @param {FormData} formData
 * @returns {Promise<Response>}
 */
export async function postZip(url, formData) {
    try {
        return await fetch(url, { method: "POST", body: formData });
    } catch {
        throw new Error("le serveur n'a pas répondu (connexion interrompue). Vérifiez qu'il tourne toujours, rechargez la page (Ctrl + Maj + R) puis réessayez.");
    }
}
