import { CODELAB_PY, exportZipUrl } from "../projects/api.js";
import { ZipImporter } from "../projects/ZipImporter.js";

/**
 * Import / export du projet de l'éditeur Python au format .zip.
 *
 * Même fenêtre « Import / export » et mêmes éléments que les autres éditeurs. L'archive est construite et lue par le
 * serveur directement à partir de la base de données : l'export télécharge ce qui est enregistré ; l'import crée un
 * nouveau projet (nom du fichier) et, en cas de doublon, ``ZipImporter`` demande d'écraser le projet existant ou de
 * le renommer. Le projet ouvert n'est jamais modifié par un import.
 */
const $ = (id) => document.getElementById(id);

function show(element, text) {
    if (text !== undefined) element.textContent = text;
    element.style.display = "block";
}

export class PythonZipManager {
    /** @param {import("./PythonEditorApp.js").PythonEditorApp} app */
    constructor(app) {
        this.app = app;
        this.importer = new ZipImporter({ editor: CODELAB_PY, open: (project) => app.projects.openImported(project) });
    }

    bind() {
        $("zip-form").addEventListener("submit", (e) => e.preventDefault());
        $("import-btn").addEventListener("click", async () => await this.importer.start());
        $("export-btn").addEventListener("click", async () => await this.exportToZip());
    }

    /** Télécharge le .zip du projet courant, construit par le serveur à partir de la base. */
    async exportToZip() {
        const feedback = $("export-feedback");
        feedback.style.display = "none";
        try {
            const project = this.app.projects.current();
            if (!project) throw new Error("Aucun projet ouvert.");
            await this.app.projects.save();      // l'archive reflète ce qui est à l'écran

            const res = await fetch(exportZipUrl(CODELAB_PY, project.id));
            if (!res.ok) {
                const body = await res.json().catch(() => ({}));
                throw new Error(body.error || "Failed to export ZIP");
            }

            const blob = await res.blob();
            const link = document.createElement("a");
            link.href = URL.createObjectURL(blob);
            link.download = `${this.app.projects.currentProject || "project"}.zip`;
            document.body.append(link);
            link.click();
            link.remove();
            setTimeout(() => URL.revokeObjectURL(link.href), 1000);
        } catch (err) {
            console.error("Error exporting ZIP:", err);
            show(feedback, `Échec de l'export : ${err.message}`);
        }
    }
}
