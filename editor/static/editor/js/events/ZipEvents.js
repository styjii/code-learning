import { state } from "../state/state.js";
import { ProjectZipManager } from "../projects/ProjectZipManager.js";

/**
 * ZipEvents handles import/export of project ZIP files.
 */
export class ZipEvents {
    /**
     * Binds ZIP form controls for import and export.
     */
    static bind() {
        const form = document.getElementById("zip-form");
        const zipManager = new ProjectZipManager(state);

        form.addEventListener("submit", (e) => e.preventDefault());

        document.getElementById("import-btn").addEventListener("click", async () => await zipManager.importFromZip());
        document.getElementById("export-btn").addEventListener("click", async () => await zipManager.exportToZip());
    }
}
