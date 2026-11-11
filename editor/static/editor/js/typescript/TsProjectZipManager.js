import { CODELAB_TS, exportZipUrl, importZipUrl, postZip, zipFormData } from "../projects/api.js";
import { TsProjectManager } from "./TsProjectManager.js";

/**
 * Import / export du projet courant en .zip (index.html, style.css, script.ts, tsconfig.json).
 *
 * L'archive est lue et construite par le serveur directement à partir de la base de données : le navigateur
 * enregistre d'abord ses modifications en attente, puis ne fait que téléverser ou télécharger l'archive.
 */
export class TsProjectZipManager {
    /** @param {import("./state.js").TsState} state */
    constructor(state) {
        this.state = state;
    }

    /** Importe une archive .zip dans le projet courant : le serveur remplace son contenu et ses options en base. */
    async importFromZip() {
        const zipInput = document.getElementById("zip-input");
        const importFeedback = document.getElementById("import-feedback");
        const importSuccess = document.getElementById("import-success");

        if (!zipInput.files.length) {
            importFeedback.textContent = "Sélectionnez un fichier .zip.";
            importFeedback.style.display = "block";
            importSuccess.style.display = "none";
            return;
        }

        try {
            const formData = await zipFormData(zipInput.files[0]);
            const project = this.state.projects[this.state.currentProject];
            if (!project?.id) throw new Error("Aucun projet ouvert.");
            await TsProjectManager.save();     // une sauvegarde différée ne doit pas écraser l'import

            const res = await postZip(importZipUrl(CODELAB_TS, project.id), formData);

            if (!res.ok) {
                // Le serveur explique le refus (fichier trop volumineux, archive invalide...).
                const body = await res.json().catch(() => ({}));
                throw new Error(body.error || "Failed to import project");
            }

            TsProjectManager.adopt(await res.json());     // contenu et options déjà en base : on les affiche

            importFeedback.style.display = "none";
            importSuccess.style.display = "block";
        } catch (err) {
            importFeedback.textContent = `Échec de l'import : ${err.message}`;
            importFeedback.style.display = "block";
            importSuccess.style.display = "none";
        }
    }

    /** Télécharge l'archive .zip du projet courant, telle qu'elle est enregistrée en base. */
    async exportToZip() {
        try {
            const project = this.state.projects[this.state.currentProject];
            if (!project?.id) throw new Error("Aucun projet ouvert.");
            await TsProjectManager.save();     // l'archive reflète ce qui est à l'écran

            const res = await fetch(exportZipUrl(CODELAB_TS, project.id));
            if (!res.ok) throw new Error("Failed to export ZIP");

            const blob = await res.blob();
            const a = document.createElement("a");
            a.href = URL.createObjectURL(blob);
            a.download = `${this.state.currentProject || "project"}.zip`;
            a.click();
            URL.revokeObjectURL(a.href);
        } catch (err) {
            console.error("Error exporting ZIP:", err);
        }
    }
}
