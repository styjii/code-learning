import { importZipUrl, postZip, readZip, zipForm } from "./api.js";

const $ = (id) => document.getElementById(id);
const MAX_NAME_LENGTH = 100;

/**
 * Import d'une archive .zip, commun aux trois éditeurs : le serveur crée un **nouveau projet** (nommé d'après le
 * fichier) et le projet ouvert n'est jamais modifié.
 *
 * Si un projet de ce nom existe déjà, le bloc d'import est remplacé par un bloc de confirmation (``#import-conflict``) :
 * écraser le projet existant, importer sous un autre nom, ou annuler. L'archive reste en mémoire pour être renvoyée.
 */
export class ZipImporter {
    /**
     * @param {object} options
     * @param {string} options.editor identifiant de l'éditeur (``codelab-js``, ``codelab-ts`` ou ``codelab-py``)
     * @param {(project: object) => Promise<{note?: string, warning?: string}|void>} options.open
     *        ouvre dans l'éditeur le projet que le serveur vient de créer (ou d'écraser) ; peut renvoyer un complément
     *        de message (``note``) et un avertissement (``warning``)
     */
    constructor({ editor, open }) {
        this.editor = editor;
        this.open = open;
        this.archive = null;          // le .zip en attente de confirmation
        this.conflictName = null;     // nom du projet existant
        this.busy = false;            // un envoi à la fois : un double clic créerait un doublon

        $("import-overwrite-btn").addEventListener("click", () => this.#overwrite());
        $("import-rename-btn").addEventListener("click", () => this.#rename());
        $("import-cancel-btn").addEventListener("click", () => this.#cancel());
        $("import-rename-input").addEventListener("keydown", (e) => {
            if (e.key === "Enter") { e.preventDefault(); this.#rename(); }
        });
    }

    /** Lit le fichier choisi et demande au serveur de créer le projet. */
    async start() {
        if (this.busy) return;
        this.#resetMessages();
        const input = $("zip-input");
        if (!input.files.length) {
            this.#show("import-feedback", "Sélectionnez un fichier .zip.");
            return;
        }
        try {
            this.archive = await readZip(input.files[0]);
        } catch (err) {
            this.#show("import-feedback", `Échec de l'import : ${err.message}`);
            return;
        }
        await this.#send({});
    }

    async #send(fields) {
        if (this.busy) return;
        this.busy = true;
        this.#setDisabled(true);
        const inConflict = $("import-conflict").style.display !== "none";
        const errorId = inConflict ? "import-conflict-error" : "import-feedback";
        try {
            const res = await postZip(importZipUrl(this.editor), zipForm(this.archive, fields));
            const body = await res.json().catch(() => ({}));

            if (res.status === 409 && body.conflict) {
                this.#showConflict(body.conflict.name, inConflict);
                return;
            }
            if (!res.ok) throw new Error(body.error || "Failed to import project");
            await this.#done(body);
        } catch (err) {
            this.#show(errorId, inConflict ? err.message : `Échec de l'import : ${err.message}`);
        } finally {
            this.busy = false;
            this.#setDisabled(false);
        }
    }

    /** Remplace le bloc d'import par le bloc de confirmation. */
    #showConflict(name, alreadyShown) {
        this.conflictName = name;
        $("import-conflict-message").textContent = `Un projet « ${name} » existe déjà. Voulez-vous l'écraser, ou importer l'archive sous un autre nom ?`;
        $("import-conflict-error").style.display = "none";
        if (alreadyShown) {
            // Le nom choisi est lui aussi pris : on reste dans le bloc, avec un message précis.
            this.#show("import-conflict-error", `Le nom « ${name} » est déjà utilisé : choisissez-en un autre.`);
            return;
        }
        $("import-rename-input").value = `${name.slice(0, MAX_NAME_LENGTH - 9)} (copie)`;
        $("import-block").style.display = "none";
        $("import-conflict").style.display = "flex";
        $("import-rename-input").focus();
        $("import-rename-input").select();
    }

    #overwrite() {
        $("import-conflict-error").style.display = "none";
        return this.#send({ name: this.conflictName, on_conflict: "overwrite" });
    }

    #rename() {
        const name = $("import-rename-input").value.trim();
        if (!name) {
            this.#show("import-conflict-error", "Saisissez un nouveau nom.");
            return;
        }
        if (name.length > MAX_NAME_LENGTH) {
            this.#show("import-conflict-error", `Le nom ne doit pas dépasser ${MAX_NAME_LENGTH} caractères.`);
            return;
        }
        $("import-conflict-error").style.display = "none";
        return this.#send({ name });
    }

    /** Annule : retour au bloc d'import, rien n'a été écrit. */
    #cancel() {
        if (this.busy) return;
        this.#closeConflict();
        this.#clearFile();
        this.#resetMessages();
    }

    async #done(project) {
        this.#closeConflict();
        const extra = (await this.open(project)) ?? {};

        let text = project.created ? `Projet « ${project.name} » créé.` : `Projet « ${project.name} » écrasé.`;
        if (project.renamed) text += " Le nom du fichier étant inutilisable, le projet porte un nom de secours.";
        if (extra.note) text += ` ${extra.note}`;
        this.#resetMessages();
        this.#show("import-success", text);

        const warnings = [...(project.skipped ?? []), ...(extra.warning ? [extra.warning] : [])];
        if (warnings.length && $("import-skipped")) this.#show("import-skipped", `Ignorés : ${warnings.join(" ")}`);
        this.#clearFile();
    }

    #closeConflict() {
        $("import-conflict").style.display = "none";
        $("import-block").style.display = "";
        this.archive = null;
        this.conflictName = null;
    }

    #clearFile() {
        $("zip-input").value = "";
        const label = $("file-name");
        if (label) label.textContent = "Aucun fichier";
    }

    #resetMessages() {
        for (const id of ["import-feedback", "import-success", "import-skipped", "import-conflict-error"]) {
            const element = $(id);
            if (element) element.style.display = "none";
        }
    }

    #show(id, text) {
        const element = $(id);
        element.textContent = text;
        element.style.display = "block";
    }

    #setDisabled(disabled) {
        for (const id of ["import-btn", "import-overwrite-btn", "import-rename-btn", "import-cancel-btn"]) {
            $(id).disabled = disabled;
        }
    }
}
