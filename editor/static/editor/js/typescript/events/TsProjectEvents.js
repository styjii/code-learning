import { TsProjectManager } from "../TsProjectManager.js";

/**
 * Sélection, création et suppression des projets.
 */
export class TsProjectEvents {
    static bind() {
        const select = document.getElementById("project-select");
        const form = document.getElementById("project-form");

        form.addEventListener("submit", (e) => e.preventDefault());

        select.addEventListener("change", async (e) => {
            await TsProjectManager.switch(e.target.value);
        });

        document.getElementById("create-btn").addEventListener("click", async () => await TsProjectManager.create());
        document.getElementById("delete-btn").addEventListener("click", async () => await TsProjectManager.delete());
    }
}
