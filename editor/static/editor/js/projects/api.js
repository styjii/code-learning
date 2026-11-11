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

/** Import d'une archive .zip dans un projet : le serveur remplace son contenu en base. */
export const importZipUrl = (editor, id) => `${projectsUrl(editor, id)}import-zip/`;

/**
 * Corps (``FormData``) d'un import .zip. Le fichier choisi est d'abord lu en mémoire : un navigateur qui relit un
 * fichier du disque au moment de l'envoi peut le trouver verrouillé ou modifié (téléchargement tout juste terminé,
 * antivirus...) et abandonner la requête avec le seul message « Failed to fetch ».
 * @param {File} file
 * @returns {Promise<FormData>}
 */
export async function zipFormData(file) {
    let buffer;
    try {
        buffer = await file.arrayBuffer();
    } catch {
        throw new Error("fichier illisible (déplacé, modifié ou verrouillé). Sélectionnez-le de nouveau.");
    }
    const formData = new FormData();
    formData.append("zip_file", new Blob([buffer], { type: "application/zip" }), file.name);
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
