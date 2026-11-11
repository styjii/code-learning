import { CODELAB_PY, exportZipUrl, importZipUrl, postZip, zipFormData } from "../projects/api.js";

/**
 * Import / export du projet de l'éditeur Python au format .zip.
 *
 * Même fenêtre « Import / export » et mêmes éléments que les autres éditeurs. L'archive est construite et lue par le
 * serveur directement à partir de la base de données : l'export télécharge ce qui est enregistré, l'import fait
 * valider l'archive par le serveur (plafonds de taille, noms de fichiers) qui remplace les fichiers du projet en base.
 */
const $ = (id) => document.getElementById(id);

function show(element, text) {
    if (text !== undefined) element.textContent = text;
    element.style.display = "block";
}

function hide(...elements) {
    elements.forEach((element) => { element.style.display = "none"; });
}

const plural = (n, word) => `${n} ${word}${n > 1 ? "s" : ""}`;

export class PythonZipManager {
    /** @param {import("./PythonEditorApp.js").PythonEditorApp} app */
    constructor(app) {
        this.app = app;
    }

    bind() {
        $("zip-form").addEventListener("submit", (e) => e.preventDefault());
        $("import-btn").addEventListener("click", async () => await this.importFromZip());
        $("export-btn").addEventListener("click", async () => await this.exportToZip());
    }

    /** Demande confirmation, puis le serveur remplace les fichiers du projet courant par ceux de l'archive. */
    async importFromZip() {
        const zipInput = $("zip-input");
        const feedback = $("import-feedback");
        const success = $("import-success");
        const skipped = $("import-skipped");
        hide(feedback, success, skipped);

        if (!zipInput.files.length) {
            show(feedback, "Sélectionnez un fichier .zip.");
            return;
        }

        try {
            const project = this.app.projects.current();
            if (!project) throw new Error("Aucun projet ouvert.");

            // L'archive est écrite en base dès son envoi : la confirmation passe avant.
            const replaced = plural(this.app.store.files.length, "fichier");
            if (!window.confirm(`Remplacer vos ${replaced} du projet « ${this.app.projects.currentProject} » par le contenu de l'archive ? Cette action est définitive.`)) {
                return;
            }

            const formData = await zipFormData(zipInput.files[0]);      // fichier lu avant toute modification
            await this.app.projects.save();      // une sauvegarde différée ne doit pas écraser l'import
            const res = await postZip(importZipUrl(CODELAB_PY, project.id), formData);
            if (!res.ok) {
                // Le serveur explique le refus (fichier trop volumineux, archive invalide, aucun fichier importable...).
                const body = await res.json().catch(() => ({}));
                throw new Error(body.error || "Failed to import project");
            }
            const data = await res.json();

            // Les fichiers sont déjà en base : on les affiche et le cache les reprend.
            const result = this.app.showFiles(data.files);
            this.app.projects.adopt(data.files);
            // L'exemple ajouté (pas de main.py) ou un fichier écarté côté navigateur ne sont pas encore en base.
            if (result.sampleMain || result.skipped.length) this.app.saveNow();

            const ignored = [...(data.skipped ?? []), ...result.skipped];
            show(success, `Archive importée : ${plural(result.count, "fichier")}.${result.sampleMain ? " Pas de main.py dans l'archive : l'exemple de départ a été ajouté." : ""}`);
            if (ignored.length) show(skipped, `Ignorés : ${ignored.join(" ")}`);
        } catch (err) {
            show(feedback, `Échec de l'import : ${err.message}`);
        }
    }

    /** Télécharge le .zip du projet courant, construit par le serveur à partir de la base. */
    async exportToZip() {
        const feedback = $("export-feedback");
        hide(feedback);
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
