import { state } from "../state.js";
import { TsProjectZipManager } from "../TsProjectZipManager.js";

/**
 * Import / export .zip.
 */
export class TsZipEvents {
    static bind() {
        const form = document.getElementById("zip-form");
        const zipManager = new TsProjectZipManager(state);

        form.addEventListener("submit", (e) => e.preventDefault());

        document.getElementById("import-btn").addEventListener("click", async () => await zipManager.importFromZip());
        document.getElementById("export-btn").addEventListener("click", async () => await zipManager.exportToZip());
    }
}
