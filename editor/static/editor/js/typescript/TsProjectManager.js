import { state } from "./state.js";
import { TsPreviewManager } from "./TsPreviewManager.js";
import { TsOptionsManager } from "./TsOptionsManager.js";
import { DEFAULT_COMPILER_OPTIONS, normalizeCompilerOptions } from "./TsCompilerOptions.js";

const API = "/editor/api/ts-projects/";

/**
 * Gère les projets TypeScript de l'utilisateur (HTML, CSS, TypeScript et options du compilateur).
 * Calqué sur ProjectManager (éditeur Web), avec une API et un état distincts.
 */
export class TsProjectManager {
    /** Fetches all saved projects and loads the first one. */
    static async fetchAll() {
        try {
            const res = await fetch(API);
            if (!res.ok) throw new Error("Failed to fetch projects");

            const data = await res.json();
            state.projects = {};
            data.forEach((p) => {
                state.projects[p.name] = {
                    id: p.id,
                    html: p.html,
                    css: p.css,
                    ts: p.ts,
                    compilerOptions: normalizeCompilerOptions(p.compiler_options),
                };
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
        const payload = this.#emptyProject("Mon projet");
        const res = await fetch(API, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });
        if (!res.ok) throw new Error("Failed to create default project");
        const data = await res.json();
        state.projects[payload.name] = this.#toState(payload, data.id);
        state.currentProject = payload.name;
        this.updateDropdown();
        this.load(payload.name);
    }

    static #emptyProject(name) {
        return { name, html: "", css: "", ts: "", compiler_options: { ...DEFAULT_COMPILER_OPTIONS } };
    }

    static #toState(payload, id) {
        return {
            id,
            html: payload.html,
            css: payload.css,
            ts: payload.ts,
            compilerOptions: normalizeCompilerOptions(payload.compiler_options),
        };
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
     * Saves the current project's editor contents and compiler options to the backend.
     * @param {string} [projectName=state.currentProject]
     */
    static async save(projectName = state.currentProject) {
        if (!projectName) return;
        state.saveTimer = null;

        const content = {
            name: projectName,
            html: state.editors.html?.getValue() ?? "",
            css: state.editors.css?.getValue() ?? "",
            ts: state.editors.ts?.getValue() ?? "",
            compiler_options: { ...state.compilerOptions },
        };

        const project = state.projects[projectName];
        const isUpdate = !!project?.id;
        const url = isUpdate ? `${API}${project.id}/` : API;

        try {
            const res = await fetch(url, {
                method: isUpdate ? "PUT" : "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(content),
            });

            if (!res.ok) throw new Error("Failed to save project");
            const data = await res.json();
            state.projects[projectName] = this.#toState(content, data.id);
        } catch (err) {
            console.error("Error saving project:", err);
        }
    }

    /** Creates a new project with the name provided in the input field. */
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

        const payload = this.#emptyProject(name);
        const res = await fetch(API, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });

        if (res.ok) {
            const data = await res.json();
            state.projects[name] = this.#toState(payload, data.id);
            state.currentProject = name;
            this.updateDropdown();
            this.load(name);
            feedback.style.display = "none";
            success.style.display = "block";
        } else {
            feedback.style.display = "block";
            success.style.display = "none";
        }
    }

    /** Deletes the currently selected project and loads the next available one. */
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

        // Une sauvegarde différée ne doit pas recréer le projet supprimé.
        clearTimeout(state.saveTimer);
        state.saveTimer = null;

        const id = state.projects[state.currentProject].id;
        const res = await fetch(`${API}${id}/`, { method: "DELETE" });

        if (res.ok) {
            delete state.projects[state.currentProject];
            state.currentProject = Object.keys(state.projects)[0] ?? null;
            feedback.style.display = "none";
            success.style.display = "block";
            this.updateDropdown();
            this.load(state.currentProject);
        }
    }

    /** Updates the project selection dropdown in the UI. */
    static updateDropdown() {
        const select = document.getElementById("project-select");
        const chip = document.getElementById("current-project");
        if (chip) chip.textContent = state.currentProject ?? "—";
        select.innerHTML = "";

        Object.keys(state.projects).forEach((name) => {
            const option = document.createElement("option");
            option.value = name;
            option.textContent = name;
            if (name === state.currentProject) option.selected = true;
            select.appendChild(option);
        });
    }

    /**
     * Switches the current project to another by name (saves the previous one first).
     * @param {string} name
     */
    static async switch(name) {
        if (!state.projects[name]) return;
        await this.flush();
        state.currentProject = name;
        this.load(name);
        this.updateDropdown();
    }

    /**
     * Loads the project's HTML, CSS, TypeScript and compiler options into the editors,
     * then triggers a preview update.
     * @param {string|null} name
     */
    static load(name) {
        const project = state.projects[name];
        if (!project) return;

        // setValue déclenche onDidChangeModelContent : on bloque la sauvegarde pendant le chargement,
        // sinon un projet serait écrasé par un mélange de l'ancien et du nouveau contenu.
        state.isLoading = true;
        try {
            TsOptionsManager.apply(project.compilerOptions);
            state.editors.html?.setValue(project.html);
            state.editors.css?.setValue(project.css);
            state.editors.ts?.setValue(project.ts);
        } finally {
            state.isLoading = false;
        }
        TsPreviewManager.updateCdnLinks();
    }
}
