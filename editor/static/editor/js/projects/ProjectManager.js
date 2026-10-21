import { state } from "../state/state.js";
import { PreviewManager } from "./PreviewManager.js";

/**
 * Manages CRUD operations for user projects (HTML/CSS/JS sets).
 */
export class ProjectManager {
    /**
     * Fetches all saved projects from the backend and updates state.
     * Sets the first project as the active one if available and loads its contents.
     */
    static async fetchAll() {
        try {
            const res = await fetch("/editor/api/projects");
            if (!res.ok) throw new Error("Failed to fetch projects");

            const data = await res.json();
            state.projects = {};
            data.forEach(p => {
                state.projects[p.name] = { id: p.id, html: p.html, css: p.css, js: p.js };
            });

            // Première utilisation : aucun projet n'existe, on en crée un pour que le travail soit sauvegardé.
            if (!data.length) {
                await this.createDefault();
                return;
            }

            state.currentProject = Object.keys(state.projects)[0] ?? null;
            this.updateDropdown();
            this.load(state.currentProject);
        } catch (err) {
            console.error("Error fetching projects:", err);
        }
    }

    /** Crée le projet par défaut lors de la première ouverture. */
    static async createDefault() {
        const payload = { name: "Mon projet", html: "", css: "", js: "" };
        const res = await fetch("/editor/api/projects/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });
        if (!res.ok) throw new Error("Failed to create default project");
        const data = await res.json();
        state.projects[payload.name] = { ...payload, id: data.id };
        state.currentProject = payload.name;
        this.updateDropdown();
        this.load(payload.name);
    }

    /** Planifie une sauvegarde après une courte pause de frappe. */
    static scheduleSave(delay = 600) {
        clearTimeout(state.saveTimer);
        state.saveTimer = setTimeout(() => this.save(), delay);
    }

    /** Exécute immédiatement une sauvegarde en attente. */
    static async flush() {
        if (state.saveTimer) {
            clearTimeout(state.saveTimer);
            state.saveTimer = null;
            await this.save();
        }
    }

    /**
     * Saves the current project's editor contents to the backend.
     * Creates or updates the project depending on whether an ID exists.
     * 
     * @param {string} [projectName=state.currentProject] - The name of the project to save.
     */
    static async save(projectName = state.currentProject) {
        if (!projectName) return;
        state.saveTimer = null;

        const content = {
            name: projectName,
            html: state.editors.html?.getValue() ?? "",
            css: state.editors.css?.getValue() ?? "",
            js: state.editors.js?.getValue() ?? "",
        };

        const project = state.projects[projectName];
        const isUpdate = !!project?.id;
        const url = isUpdate
            ? `/editor/api/projects/${project.id}/`
            : `/editor/api/projects/`;

        try {
            const res = await fetch(url, {
                method: isUpdate ? "PUT" : "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(content),
            });

            if (!res.ok) throw new Error("Failed to save project");
            const data = await res.json();
            state.projects[projectName] = { ...content, id: data.id };
        } catch (err) {
            console.error("Error saving project:", err);
        }
    }

    /**
     * Creates a new project with the name provided in the input field.
     * Updates the UI dropdown and loads the new, empty project.
     */
    static async create() {
        const input = document.getElementById("create-project");
        const feedback = document.getElementById("create-feedback");
        const success = document.getElementById("create-success");

        const name = input.value.trim();
        if (!name || state.projects[name]) {
            feedback.style.display = "block";
            success.style.display = "none";
            return;
        }

        const payload = { name, html: "", css: "", js: "" };
        const res = await fetch("/editor/api/projects/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });

        if (res.ok) {
            const data = await res.json();
            state.projects[name] = { ...payload, id: data.id };
            state.currentProject = name;
            this.updateDropdown();
            this.load(name);
            feedback.style.display = "none";
            success.style.display = "block";
        }
    }

    /**
     * Deletes the currently selected project from the backend and state.
     * Updates the dropdown and loads the next available project.
     */
    static async delete() {
        const keys = Object.keys(state.projects);
        const feedback = document.getElementById("delete-feedback");
        const success = document.getElementById("delete-success");

        if (keys.length <= 1) {
            feedback.style.display = "block";
            success.style.display = "none";
            return;
        }

        if (!confirm(`Supprimer le projet « ${state.currentProject} » ?`)) return;

        const id = state.projects[state.currentProject].id;
        const res = await fetch(`/editor/api/projects/${id}/`, { method: "DELETE" });

        if (res.ok) {
            delete state.projects[state.currentProject];
            state.currentProject = Object.keys(state.projects)[0] ?? null;
            feedback.style.display = "none";
            success.style.display = "block";
            this.updateDropdown();
            this.load(state.currentProject);
        }
    }

    /**
     * Updates the project selection dropdown in the UI
     * to reflect the current list of saved projects.
     */
    static updateDropdown() {
        const select = document.getElementById("project-select");
        const chip = document.getElementById("current-project");
        if (chip) chip.textContent = state.currentProject ?? "—";
        select.innerHTML = "";

        Object.keys(state.projects).forEach(name => {
            const option = document.createElement("option");
            option.value = name;
            option.textContent = name;
            if (name === state.currentProject) option.selected = true;
            select.appendChild(option);
        });
    }

    /**
     * Switches the current project to another by name.
     * Saves the previous project and loads the selected one.
     * 
     * @param {string} name - The name of the project to switch to.
     */
    static async switch(name) {
        if (!state.projects[name]) return;
        await this.flush();
        state.currentProject = name;
        this.load(name);
        this.updateDropdown();
    }

    /**
     * Loads the project's saved HTML, CSS, and JS into the editors.
     * Also triggers a preview update for the newly loaded content.
     * 
     * @param {string|null} name - The name of the project to load.
     */
    static load(name) {
        const project = state.projects[name];
        if (!project) return;

        // setValue déclenche onDidChangeModelContent : on bloque la sauvegarde pendant le chargement,
        // sinon un projet serait écrasé par un mélange de l'ancien et du nouveau contenu.
        state.isLoading = true;
        try {
            state.editors.html?.setValue(project.html);
            state.editors.css?.setValue(project.css);
            state.editors.js?.setValue(project.js);
        } finally {
            state.isLoading = false;
        }
        PreviewManager.updateCdnLinks();
    }
}
