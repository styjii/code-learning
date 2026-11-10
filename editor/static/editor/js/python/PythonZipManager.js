/**
 * Import / export du projet de l'éditeur Python au format .zip.
 *
 * Même fenêtre « Import / export » et mêmes éléments que l'éditeur Web (``ProjectZipManager``) : l'export envoie les
 * fichiers du projet au serveur qui construit l'archive, l'import fait valider l'archive par le serveur (plafonds de
 * taille, noms de fichiers) puis restaure le projet dans le stockage local du navigateur.
 */
const EXPORT_URL = "/editor/api/py-export-zip/";
const IMPORT_URL = "/editor/api/py-import-zip/";
const ARCHIVE_NAME = "python-project.zip";

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

    /** Valide l'archive côté serveur, demande confirmation, puis remplace les fichiers du projet. */
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

        const formData = new FormData();
        formData.append("zip_file", zipInput.files[0]);

        try {
            const res = await fetch(IMPORT_URL, { method: "POST", body: formData });
            if (!res.ok) {
                // Le serveur explique le refus (fichier trop volumineux, archive invalide, aucun fichier importable...).
                const body = await res.json().catch(() => ({}));
                throw new Error(body.error || "Failed to import project");
            }
            const data = await res.json();

            const replaced = plural(this.app.store.files.length, "fichier");
            if (!window.confirm(`Remplacer vos ${replaced} par les ${plural(data.files.length, "fichier")} de l'archive ? Cette action est définitive.`)) {
                return;
            }

            const result = this.app.restoreFiles(data.files);
            const ignored = [...(data.skipped ?? []), ...result.skipped];
            show(success, `Archive importée : ${plural(result.count, "fichier")}.${result.sampleMain ? " Pas de main.py dans l'archive : l'exemple de départ a été ajouté." : ""}`);
            if (ignored.length) show(skipped, `Ignorés : ${ignored.join(" ")}`);
        } catch (err) {
            show(feedback, `Échec de l'import : ${err.message}`);
        }
    }

    /** Télécharge tous les fichiers du projet dans un .zip. */
    async exportToZip() {
        const feedback = $("export-feedback");
        hide(feedback);
        try {
            this.app.saveNow();
            const res = await fetch(EXPORT_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ files: this.app.store.files }),
            });

            if (!res.ok) {
                const body = await res.json().catch(() => ({}));
                throw new Error(body.error || "Failed to export ZIP");
            }

            const blob = await res.blob();
            const link = document.createElement("a");
            link.href = URL.createObjectURL(blob);
            link.download = ARCHIVE_NAME;
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
