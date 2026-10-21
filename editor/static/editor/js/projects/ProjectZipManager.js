/**
 * Handles importing and exporting projects as ZIP files.
 */
export class ProjectZipManager {
    /**
     * @param {import("../state/state.js").State} state - Global app state.
     */
    constructor(state) {
        this.state = state;
    }

    /**
     * Imports a project from a ZIP file and updates editor contents.
     */
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

        const formData = new FormData();
        formData.append("zip_file", zipInput.files[0]);

        try {
            const res = await fetch("/editor/api/import-zip/", {
                method: "POST",
                body: formData,
            });

            if (!res.ok) throw new Error("Failed to import project");

            const data = await res.json();

            this.state.editors.html?.setValue(data.html ?? "");
            this.state.editors.css?.setValue(data.css ?? "");
            this.state.editors.js?.setValue(data.js ?? "");

            importFeedback.style.display = "none";
            importSuccess.style.display = "block";
        } catch (err) {
            importFeedback.textContent = `Échec de l'import : ${err.message}`;
            importFeedback.style.display = "block";
            importSuccess.style.display = "none";
        }
    }

    /**
     * Exports the current project to a ZIP file and triggers download.
     */
    async exportToZip() {
        try {
            const res = await fetch("/editor/api/export-zip/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    project: this.state.currentProject,
                    html: this.state.editors.html?.getValue() ?? "",
                    css: this.state.editors.css?.getValue() ?? "",
                    js: this.state.editors.js?.getValue() ?? "",
                }),
            });

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
