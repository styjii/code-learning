import { state } from "../state/state.js";
import { PreviewManager } from "./PreviewManager.js";
import { PreviewStorage } from "./PreviewStorage.js";
import { CODELAB_JS, projectsUrl } from "./api.js";

/**
 * Manages CRUD operations for user projects (HTML/CSS/JS sets).
 */
export class ProjectManager {
    /**
     * Fetches all saved projects from the backend and updates state.
     * Sets the first project as the active one if available and loads its contents.
     */
    static async fetchAll({ allowCreateDefault = true } = {}) {
        try {
            const res = await fetch(projectsUrl(CODELAB_JS));
            if (!res.ok) throw new Error("Failed to fetch projects");

            const data = await res.json();
            state.projects = {};
            data.forEach(p => {
                state.projects[p.name] = { id: p.id, html: p.html, css: p.css, js: p.js };
            });

            // Première utilisation : aucun projet n'existe, on en crée un pour que le travail soit sauvegardé.
            if (!data.length && allowCreateDefault) {
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
        const res = await fetch(projectsUrl(CODELAB_JS), {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });
        if (res.status === 400) {
            // Un autre onglet (ou une requête simultanée) a déjà créé le projet par défaut : on le récupère.
            await this.fetchAll({ allowCreateDefault: false });
            return;
        }
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
            ? projectsUrl(CODELAB_JS, project.id)
            : projectsUrl(CODELAB_JS);

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
        if (this.isCreating) return; // un double-clic enverrait deux POST identiques

        const input = document.getElementById("create-project");
        const feedback = document.getElementById("create-feedback");
        const success = document.getElementById("create-success");

        const name = input.value.trim();
        if (!name || state.projects[name]) {
            feedback.textContent = "Nom vide ou déjà utilisé.";
            feedback.style.display = "block";
            success.style.display = "none";
            return;
        }

        this.isCreating = true;
        try {
            const payload = { name, html: "", css: "", js: "" };
            const res = await fetch(projectsUrl(CODELAB_JS), {
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
                return;
            }

            // 400 : nom invalide ou déjà pris ; autre code : problème serveur ou session expirée.
            feedback.textContent = res.status === 400
                ? "Nom vide ou déjà utilisé."
                : "Impossible de créer le projet. Réessayez.";
            feedback.style.display = "block";
            success.style.display = "none";
        } catch (err) {
            console.error("Error creating project:", err);
            feedback.textContent = "Impossible de créer le projet. Réessayez.";
            feedback.style.display = "block";
            success.style.display = "none";
        } finally {
            this.isCreating = false;
        }
    }

    /**
     * Deletes the currently selected project from the backend and state.
     * Updates the dropdown and loads the next available project.
     */
    static async delete() {
        if (this.isDeleting) return;

        const keys = Object.keys(state.projects);
        const feedback = document.getElementById("delete-feedback");
        const success = document.getElementById("delete-success");

        if (keys.length <= 1) {
            feedback.textContent = "Il faut garder au moins un projet.";
            feedback.style.display = "block";
            success.style.display = "none";
            return;
        }

        if (!confirm(`Supprimer le projet « ${state.currentProject} » ?`)) return;

        this.isDeleting = true;
        try {
            // Une sauvegarde différée ne doit pas se déclencher (ni recréer le projet) pendant la suppression.
            clearTimeout(state.saveTimer);
            state.saveTimer = null;

            const id = state.projects[state.currentProject].id;
            const res = await fetch(projectsUrl(CODELAB_JS, id), { method: "DELETE" });

            // 404 : déjà supprimé (autre onglet) -> même résultat final côté interface.
            if (res.ok || res.status === 404) {
                PreviewStorage.forget(CODELAB_JS, id);   // données localStorage de l'aperçu de ce projet
                delete state.projects[state.currentProject];
                state.currentProject = Object.keys(state.projects)[0] ?? null;
                feedback.style.display = "none";
                success.style.display = "block";
                this.updateDropdown();
                this.load(state.currentProject);
                return;
            }

            feedback.textContent = "Suppression impossible. Réessayez.";
            feedback.style.display = "block";
            success.style.display = "none";
        } catch (err) {
            console.error("Error deleting project:", err);
            feedback.textContent = "Suppression impossible. Réessayez.";
            feedback.style.display = "block";
            success.style.display = "none";
        } finally {
            this.isDeleting = false;
        }
    }

    /**
     * Renomme le projet courant via l'API (``PATCH { name }``) puis met l'interface à jour.
     *
     * Le contenu en attente de sauvegarde est enregistré d'abord, sous l'ancien nom, pour qu'aucune
     * sauvegarde différée ne rétablisse ensuite l'ancien nom.
     *
     * @param {string} newName - Nouveau nom saisi par l'utilisateur.
     * @returns {Promise<{ok: boolean, unchanged?: boolean, message?: string}>}
     */
    static async rename(newName) {
        if (this.isRenaming) return { ok: false, message: "Renommage en cours." };

        const oldName = state.currentProject;
        const project = state.projects[oldName];
        const name = String(newName ?? "").trim();

        if (!project?.id) return { ok: false, message: "Projet introuvable." };
        if (!name) return { ok: false, message: "Le nom ne peut pas être vide." };
        if (name.length > 100) return { ok: false, message: "Le nom ne doit pas dépasser 100 caractères." };
        if (name === oldName) return { ok: true, unchanged: true };
        if (state.projects[name]) return { ok: false, message: "Un projet porte déjà ce nom." };

        this.isRenaming = true;
        try {
            await this.flush();
            const id = project.id;
            const res = await fetch(projectsUrl(CODELAB_JS, id), {
                method: "PATCH",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name }),
            });

            if (res.status === 400) {
                // Nom invalide ou déjà pris (aussi en cas de requêtes simultanées) : message du serveur.
                const errors = await res.json().catch(() => ({}));
                return { ok: false, message: errors.name?.[0] ?? "Nom invalide." };
            }
            if (res.status === 404) return { ok: false, message: "Ce projet n'existe plus. Rechargez la page." };
            if (!res.ok) throw new Error("Failed to rename project");

            const data = await res.json();
            // On change la clé en gardant l'ordre des projets (celui de la liste déroulante).
            state.projects = Object.fromEntries(
                Object.entries(state.projects).map(([key, value]) => [key === oldName ? data.name : key, value])
            );
            state.currentProject = data.name;
            this.updateDropdown();
            return { ok: true };
        } catch (err) {
            console.error("Error renaming project:", err);
            return { ok: false, message: "Renommage impossible. Réessayez." };
        } finally {
            this.isRenaming = false;
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
        const label = document.getElementById("project-current-name");
        if (label) {
            label.textContent = state.currentProject ?? "—";
            label.title = state.currentProject ?? "Projet en cours";
        }
        // Le projet courant a changé (sélection, création, suppression, renommage) : l'édition du nom en cours est caduque.
        document.dispatchEvent(new CustomEvent("project:current-changed"));
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
    /**
     * Ouvre le projet que le serveur vient de créer (ou d'écraser) par un import .zip : le contenu est déjà en base.
     *
     * Le projet qu'on quitte est enregistré d'abord ; si c'est le projet écrasé lui-même, ses modifications en
     * attente sont abandonnées (elles ne doivent pas remplacer l'archive importée).
     * @param {{id: number, name: string, html: string, css: string, js: string}} data
     */
    static async openImported(data) {
        clearTimeout(state.saveTimer);
        state.saveTimer = null;
        if (data.name !== state.currentProject) await this.save();
        state.projects[data.name] = { id: data.id, html: data.html, css: data.css, js: data.js };
        state.currentProject = data.name;
        this.updateDropdown();
        this.load(data.name);
    }

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
