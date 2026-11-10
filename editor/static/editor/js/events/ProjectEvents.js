import { ProjectManager } from "../projects/ProjectManager.js";
import { ProjectRenameBinder } from "../projects/ProjectRenameBinder.js";

/**
 * ProjectEvents handles project selection, creation, renaming, and deletion.
 */
export class ProjectEvents {
    /**
     * Binds project management controls.
     */
    static bind() {
        const select = document.getElementById("project-select");
        const form = document.getElementById("project-form");

        form.addEventListener("submit", e => e.preventDefault());

        select.addEventListener("change", async (e) => {
            await ProjectManager.switch(e.target.value);
        });

        document.getElementById("create-btn").addEventListener("click", async () => await ProjectManager.create());
        document.getElementById("delete-btn").addEventListener("click", async () => await ProjectManager.delete());
        ProjectRenameBinder.bind(ProjectManager);
    }
}
