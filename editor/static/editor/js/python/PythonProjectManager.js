import { FileStore, MAIN_FILE, SAMPLE, clearLegacyProject, readLegacyProject } from "./FileStore.js";

const API = "/editor/api/py-projects/";
const DEFAULT_NAME = "Mon projet";
const MAX_NAME_LENGTH = 100;

const $ = (id) => document.getElementById(id);

/** Affiche un message de retour (``type`` : « error » ou « success ») et masque son pendant. */
function feedback(errorId, successId, type, text) {
    const error = $(errorId);
    const success = $(successId);
    const shown = type === "error" ? error : success;
    const hidden = type === "error" ? success : error;
    if (text !== undefined) shown.textContent = text;
    shown.style.display = "block";
    hidden.style.display = "none";
}

/** Copie indépendante des fichiers : le magasin de l'éditeur modifie les siens en place. */
const copyFiles = (files) => files.map(({ name, content }) => ({ name, content }));

/**
 * Gère les projets Python de l'utilisateur (une liste de fichiers par projet), enregistrés sur le serveur.
 * Calqué sur ``TsProjectManager`` (éditeur TypeScript) et ``ProjectManager`` (éditeur Web) : mêmes éléments dans
 * la modale « Projets », même API (``/editor/api/py-projects/``), mêmes messages.
 *
 * Les fichiers du projet courant vivent dans ``app.store`` (FileStore) ; ce gestionnaire les enregistre, en
 * charge d'autres au changement de projet et tient la liste des projets (nom -> {id, files}).
 */
export class PythonProjectManager {
    /** @param {import("./PythonEditorApp.js").PythonEditorApp} app */
    constructor(app) {
        this.app = app;
        /** @type {Map<string, {id: number, files: {name: string, content: string}[]}>} ordre = celui de la liste */
        this.projects = new Map();
        this.currentProject = null;
        this.saveTimer = null;
        this.pending = Promise.resolve();   // les enregistrements s'exécutent l'un après l'autre
        this.isCreating = false;
        this.isDeleting = false;
        this.isRenaming = false;
    }

    /** Récupère tous les projets et ouvre le premier. */
    async fetchAll({ allowCreateDefault = true } = {}) {
        try {
            const res = await fetch(API);
            if (!res.ok) throw new Error("Failed to fetch projects");

            const data = await res.json();
            this.projects = new Map(data.map((p) => [p.name, { id: p.id, files: copyFiles(p.files ?? []) }]));

            // Première utilisation : aucun projet n'existe, on en crée un pour que le travail soit sauvegardé.
            if (!data.length && allowCreateDefault) {
                await this.createDefault();
                return;
            }

            this.currentProject = this.projects.keys().next().value ?? null;
            this.updateDropdown();
            this.load(this.currentProject);
        } catch (err) {
            console.error("Error fetching projects:", err);
            this.app.notify("Impossible de charger vos projets : vos modifications ne seront pas enregistrées. Rechargez la page.", true);
            this.app.setSaveState("Enregistrement impossible");
        }
    }

    /**
     * Crée le projet par défaut lors de la première ouverture. Les fichiers que l'éditeur gardait jusque-là dans
     * le navigateur (avant les projets enregistrés) en deviennent le contenu : rien n'est perdu.
     */
    async createDefault() {
        const legacy = readLegacyProject();
        const store = new FileStore();
        if (legacy) store.replaceAll(legacy);      // mêmes règles de noms et de taille que partout ailleurs
        const payload = { name: DEFAULT_NAME, files: copyFiles(store.files) };

        const res = await fetch(API, {
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
        clearLegacyProject();
        this.projects.set(payload.name, { id: data.id, files: payload.files });
        this.currentProject = payload.name;
        this.updateDropdown();
        this.load(payload.name);
    }

    /** Planifie un enregistrement après une courte pause de frappe. */
    scheduleSave(delay = 600) {
        clearTimeout(this.saveTimer);
        this.saveTimer = setTimeout(() => this.save(), delay);
    }

    /** Exécute immédiatement un enregistrement en attente. */
    async flush() {
        if (this.saveTimer) {
            clearTimeout(this.saveTimer);
            this.saveTimer = null;
            await this.save();
        }
    }

    /**
     * Enregistre les fichiers du projet courant sur le serveur.
     *
     * Seuls les fichiers sont envoyés (``PATCH { files }``), jamais le nom : un enregistrement différé qui
     * arriverait pendant un renommage ne peut donc pas rétablir l'ancien nom.
     *
     * @param {string} [projectName=this.currentProject]
     * @returns {Promise<boolean>} true si le serveur a enregistré
     */
    save(projectName = this.currentProject) {
        clearTimeout(this.saveTimer);
        this.saveTimer = null;
        const project = this.projects.get(projectName);
        if (!project) {
            this.app.setSaveState("Enregistrement impossible");      // aucun projet ouvert (chargement en échec)
            return Promise.resolve(false);
        }

        // Deux enregistrements simultanés pourraient arriver dans le désordre : on les enchaîne.
        const files = copyFiles(this.app.store.files);
        this.app.setSaveState("Enregistrement…");
        const run = this.pending.then(() => this.#send(project, files));
        this.pending = run;
        return run;
    }

    async #send(project, files) {
        try {
            const res = await fetch(`${API}${project.id}/`, {
                method: "PATCH",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ files }),
            });
            if (res.status === 404) throw new Error("Ce projet n'existe plus. Rechargez la page.");
            if (!res.ok) throw new Error("Failed to save project");
            project.files = files;
            this.app.setSaveState("Enregistré");
            return true;
        } catch (err) {
            console.error("Error saving project:", err);
            this.app.setSaveState("Enregistrement impossible");
            return false;
        }
    }

    /** Crée un projet avec le nom saisi dans le champ de la modale et l'ouvre. */
    async create() {
        if (this.isCreating) return;       // un double-clic enverrait deux POST identiques

        const input = $("create-project");
        const name = input.value.trim();
        if (!name || this.projects.has(name)) {
            feedback("create-feedback", "create-success", "error", "Nom vide ou déjà utilisé.");
            return;
        }
        if (name.length > MAX_NAME_LENGTH) {
            feedback("create-feedback", "create-success", "error", `Le nom ne doit pas dépasser ${MAX_NAME_LENGTH} caractères.`);
            return;
        }

        this.isCreating = true;
        try {
            await this.flush();            // le projet qu'on quitte garde ses dernières modifications
            const payload = { name, files: [{ name: MAIN_FILE, content: "" }] };
            const res = await fetch(API, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload),
            });

            if (res.ok) {
                const data = await res.json();
                this.projects.set(name, { id: data.id, files: payload.files });
                this.currentProject = name;
                this.updateDropdown();
                this.load(name);
                input.value = "";
                feedback("create-feedback", "create-success", "success");
                return;
            }
            // 400 : nom invalide ou déjà pris ; autre code : problème serveur ou session expirée.
            feedback("create-feedback", "create-success", "error",
                res.status === 400 ? "Nom vide ou déjà utilisé." : "Impossible de créer le projet. Réessayez.");
        } catch (err) {
            console.error("Error creating project:", err);
            feedback("create-feedback", "create-success", "error", "Impossible de créer le projet. Réessayez.");
        } finally {
            this.isCreating = false;
        }
    }

    /** Supprime le projet courant et ouvre le suivant. Le dernier projet ne peut pas être supprimé. */
    async delete() {
        if (this.isDeleting) return;

        if (this.projects.size <= 1) {
            feedback("delete-feedback", "delete-success", "error", "Il faut garder au moins un projet.");
            return;
        }
        if (!window.confirm(`Supprimer le projet « ${this.currentProject} » ? Cette action est définitive.`)) return;

        this.isDeleting = true;
        try {
            // Un enregistrement différé ne doit pas se déclencher (ni échouer) pendant la suppression.
            clearTimeout(this.saveTimer);
            this.saveTimer = null;
            await this.pending;

            const name = this.currentProject;
            const res = await fetch(`${API}${this.projects.get(name).id}/`, { method: "DELETE" });

            // 404 : déjà supprimé (autre onglet) -> même résultat final côté interface.
            if (res.ok || res.status === 404) {
                this.projects.delete(name);
                this.currentProject = this.projects.keys().next().value ?? null;
                this.updateDropdown();
                this.load(this.currentProject);
                feedback("delete-feedback", "delete-success", "success");
                return;
            }
            feedback("delete-feedback", "delete-success", "error", "Suppression impossible. Réessayez.");
        } catch (err) {
            console.error("Error deleting project:", err);
            feedback("delete-feedback", "delete-success", "error", "Suppression impossible. Réessayez.");
        } finally {
            this.isDeleting = false;
        }
    }

    /**
     * Renomme le projet courant via l'API (``PATCH { name }``) puis met l'interface à jour.
     *
     * Le contenu en attente d'enregistrement est enregistré d'abord, sous l'ancien nom, pour qu'aucun
     * enregistrement différé ne rétablisse ensuite l'ancien nom.
     *
     * @param {string} newName - Nouveau nom saisi par l'utilisateur.
     * @returns {Promise<{ok: boolean, unchanged?: boolean, message?: string}>}
     */
    async rename(newName) {
        if (this.isRenaming) return { ok: false, message: "Renommage en cours." };

        const oldName = this.currentProject;
        const project = this.projects.get(oldName);
        const name = String(newName ?? "").trim();

        if (!project?.id) return { ok: false, message: "Projet introuvable." };
        if (!name) return { ok: false, message: "Le nom ne peut pas être vide." };
        if (name.length > MAX_NAME_LENGTH) return { ok: false, message: `Le nom ne doit pas dépasser ${MAX_NAME_LENGTH} caractères.` };
        if (name === oldName) return { ok: true, unchanged: true };
        if (this.projects.has(name)) return { ok: false, message: "Un projet porte déjà ce nom." };

        this.isRenaming = true;
        try {
            await this.flush();
            await this.pending;
            const res = await fetch(`${API}${project.id}/`, {
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
            this.projects = new Map([...this.projects].map(([key, value]) => [key === oldName ? data.name : key, value]));
            this.currentProject = data.name;
            this.updateDropdown();
            return { ok: true };
        } catch (err) {
            console.error("Error renaming project:", err);
            return { ok: false, message: "Renommage impossible. Réessayez." };
        } finally {
            this.isRenaming = false;
        }
    }

    /** Met à jour la pastille de l'en-tête, le libellé du projet courant et la liste déroulante de la modale. */
    updateDropdown() {
        const select = $("project-select");
        const chip = $("current-project");
        if (chip) chip.textContent = this.currentProject ?? "—";
        const label = $("project-current-name");
        if (label) {
            label.textContent = this.currentProject ?? "—";
            label.title = this.currentProject ?? "Projet en cours";
        }
        // Le projet courant a changé (sélection, création, suppression, renommage) : l'édition du nom en cours est caduque.
        document.dispatchEvent(new CustomEvent("project:current-changed"));
        select.innerHTML = "";

        for (const name of this.projects.keys()) {
            const option = document.createElement("option");
            option.value = name;
            option.textContent = name;
            if (name === this.currentProject) option.selected = true;
            select.appendChild(option);
        }
    }

    /**
     * Ouvre un autre projet par son nom (le projet qu'on quitte est enregistré d'abord).
     * @param {string} name
     */
    async switch(name) {
        if (!this.projects.has(name) || name === this.currentProject) return;
        await this.flush();
        await this.pending;
        this.currentProject = name;
        this.load(name);
        this.updateDropdown();
    }

    /**
     * Charge les fichiers du projet dans l'éditeur.
     * @param {string|null} name
     */
    load(name) {
        const project = this.projects.get(name);
        if (!project) return;
        // Un projet sans fichier (créé hors de l'éditeur) reçoit main.py avec l'exemple de départ.
        this.app.showFiles(project.files.length ? project.files : [{ name: MAIN_FILE, content: SAMPLE }]);
    }
}
