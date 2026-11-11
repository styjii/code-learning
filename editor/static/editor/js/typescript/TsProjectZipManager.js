import { CODELAB_TS, exportZipUrl } from "../projects/api.js";
import { ZipImporter } from "../projects/ZipImporter.js";
import { TsProjectManager } from "./TsProjectManager.js";

/**
 * Import / export en .zip (index.html, style.css, script.ts, tsconfig.json).
 *
 * L'archive est lue et construite par le serveur directement à partir de la base de données. L'import crée un nouveau
 * projet (nom du fichier) ; en cas de doublon, ``ZipImporter`` demande d'écraser le projet existant ou de le renommer.
 */
export class TsProjectZipManager {
    /** @param {import("./state.js").TsState} state */
    constructor(state) {
        this.state = state;
        this.importer = new ZipImporter({ editor: CODELAB_TS, open: (project) => TsProjectManager.openImported(project) });
    }

    /** Importe l'archive choisie comme nouveau projet. */
    async importFromZip() {
        await this.importer.start();
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
