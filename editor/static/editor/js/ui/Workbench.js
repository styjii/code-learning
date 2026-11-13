/**
 * Comportements de l'interface commune aux trois éditeurs (Web, TypeScript, Python) : menus, panneau de
 * résultat, console intégrée (masquée par défaut), aperçu, état d'enregistrement. Aucune logique métier ici : tout passe par les
 * boutons et les modules existants (projets, import/export, aperçu).
 */
import { Splitters } from "./Splitters.js";

const $ = (id) => document.getElementById(id);
const isPython = () => document.body.classList.contains("py-app");
const stamp = () => new Date().toLocaleTimeString("fr-FR", { hour12: false });
const LAYOUT_KEY = "editor-layout";
const LANGUAGE_LABELS = { html: "HTML", css: "CSS", js: "JavaScript", ts: "TypeScript", py: "Python" };

export class Workbench {
    static init() {
        Workbench.#actions();
        Workbench.#views();
        Workbench.#console();
        Workbench.#preview();
        Workbench.#observers();
        Workbench.#layout();
        Splitters.init();
        Workbench.#restart();
        Workbench.#shortcuts();
    }

    /* ------------------------- API utilisée par les autres modules ------------------------- */

    /**
     * Affiche ou masque le panneau de console (éditeurs Web et TypeScript). Appelée uniquement par le bouton
     * #toggle-console et par la croix #console-close : aucun autre événement (exécution, erreur de compilation,
     * changement d'onglet) n'ouvre la console. Elle est masquée au chargement (data-console="closed" dans le gabarit).
     */
    static setConsoleOpen(open) {
        const container = $("output-container");
        if (!container) return;
        if (open) delete container.dataset.console; else container.dataset.console = "closed";
        if (!open) Workbench.setConsoleMaximized(false);
        const button = $("toggle-console");
        if (button) {
            const label = open ? "Masquer la console" : "Afficher la console";
            button.setAttribute("aria-pressed", String(open));
            button.setAttribute("aria-label", label);
            button.title = label;
        }
        if (open) {
            const consoleEl = $("console");
            if (consoleEl) consoleEl.scrollTop = consoleEl.scrollHeight;
        }
        Workbench.#relayout();
    }

    /**
     * Agrandit la console à tout le panneau de résultat (true) ou la ramène à sa taille précédente (false).
     * La taille réglée avec le séparateur n'est pas touchée : elle revient telle quelle.
     */
    static setConsoleMaximized(maximized) {
        const container = $("output-container");
        if (!container) return;
        container.toggleAttribute("data-console-max", maximized);
        const button = $("console-maximize");
        if (button) {
            const label = maximized ? "Rétablir la taille de la console" : "Agrandir la console";
            button.setAttribute("aria-pressed", String(maximized));
            button.setAttribute("aria-label", label);
            button.title = label;
        }
        Workbench.#relayout();
    }

    static isConsoleOpen() {
        return $("output-container")?.dataset.console !== "closed";
    }

    /** Reflète l'état de l'aperçu automatique dans l'interrupteur, son libellé et le menu Projet. */
    static setLive(on) {
        $("live-code")?.setAttribute("aria-checked", String(on));
        const label = $("live-label");
        if (label) label.textContent = `Aperçu auto : ${on ? "oui" : "non"}`;
        document.querySelectorAll("[data-live-indicator]").forEach((pill) => {
            pill.textContent = on ? "Oui" : "Non";
            pill.closest("[role='menuitemcheckbox']")?.setAttribute("aria-checked", String(on));
        });
    }

    /** Texte de l'indicateur d'enregistrement (l'état — enregistré, en cours, erreur — en est déduit). */
    static setSaveState(text) {
        const node = document.querySelector(".save-state");
        if (node) node.textContent = text;
    }

    /* ------------------------------------ Commandes ------------------------------------ */

    static #actions() {
        const run = {
            "new-project": () => setTimeout(() => $("create-project")?.focus(), 60),
            "open-project": () => setTimeout(() => $("project-select")?.focus(), 60),
            "rename-project": () => setTimeout(() => { const row = $("rename-row"); if (row?.hidden) $("rename-btn")?.click(); $("rename-input")?.focus(); }, 60),
            "export-zip": () => $("export-btn")?.click(),
            "delete-project": () => setTimeout(() => $("delete-btn")?.click(), 60),
            "toggle-live": () => $("live-code")?.click(),
        };
        document.addEventListener("click", (event) => {
            const button = event.target.closest("[data-action]");
            if (button) run[button.dataset.action]?.();
        });
    }

    static #shortcuts() {
        document.addEventListener("keydown", (event) => {
            if (event.altKey && !event.ctrlKey && !event.metaKey && event.key.toLowerCase() === "n") {
                event.preventDefault();
                document.querySelector('[data-action="new-project"]')?.click();
            } else if ((event.ctrlKey || event.metaKey) && event.shiftKey && event.key.toLowerCase() === "e") {
                event.preventDefault();
                $("export-btn")?.click();
            }
        });
    }

    /* ------------------------------ Panneau de résultat ------------------------------ */

    static #views() {
        $("toggle-console")?.addEventListener("click", () => Workbench.setConsoleOpen(!Workbench.isConsoleOpen()));
        $("console-maximize")?.addEventListener("click", () => {
            Workbench.setConsoleMaximized($("output-container")?.hasAttribute("data-console-max") === false);
        });
        $("console-close")?.addEventListener("click", () => Workbench.setConsoleOpen(false));
        $("focus-editor")?.addEventListener("click", (event) => {
            const on = document.body.classList.toggle("is-focus");
            event.currentTarget.setAttribute("aria-pressed", String(on));
            Workbench.#relayout();
        });
    }

    static #console() {
        const consoleEl = $("console");
        if (!consoleEl) return;
        const count = $("console-count");
        const update = () => {
            const rows = consoleEl.querySelectorAll(".cc-row");
            rows.forEach((row) => { if (!row.dataset.time) row.dataset.time = stamp(); });
            if (count) count.textContent = String(rows.length);
        };
        new MutationObserver(update).observe(consoleEl, { childList: true, subtree: true });
        update();
        // Web / TypeScript : la corbeille vide la console (Python a son propre bouton, #py-clear).
        $("console-clear")?.addEventListener("click", () => consoleEl.replaceChildren());
    }

    static #preview() {
        const frame = $("output");
        if (!frame) return;
        const url = $("preview-url");
        if (url) url.textContent = `${location.hostname || "localhost"} / index.html`;

        const size = $("preview-size");
        new ResizeObserver(() => { if (size) size.textContent = `${Math.round(frame.clientWidth)} • ${Math.round(frame.clientHeight)}`; }).observe(frame);

        let updatedAt = 0;
        const label = $("preview-updated");
        const refreshLabel = () => {
            if (!label || !updatedAt) return;
            const seconds = Math.round((Date.now() - updatedAt) / 1000);
            label.textContent = seconds < 10 ? "Mis à jour à l'instant" : seconds < 60 ? `Mis à jour il y a ${seconds} s` : `Mis à jour il y a ${Math.round(seconds / 60)} min`;
        };
        frame.addEventListener("load", () => {
            if (!frame.getAttribute("src") || frame.getAttribute("src") === "about:blank") return;
            updatedAt = Date.now();
            refreshLabel();
        });
        setInterval(refreshLabel, 15000);

        $("reload-preview")?.addEventListener("click", () => $("run-code")?.click());
        $("open-preview")?.addEventListener("click", () => {
            const src = frame.getAttribute("src");
            if (src && src !== "about:blank") window.open(src, "_blank", "noopener");
        });
    }

    /* --------------------------- Observateurs de l'interface --------------------------- */

    static #observers() {
        // État d'enregistrement : le texte est écrit par les gestionnaires de projet, l'état s'en déduit.
        const saveNode = document.querySelector(".save-state");
        if (saveNode) {
            const derive = () => {
                const text = saveNode.textContent;
                saveNode.dataset.state = /impossible/i.test(text) ? "error" : /…|\.\.\./.test(text) ? "pending" : "saved";
                saveNode.title = text;
            };
            new MutationObserver(derive).observe(saveNode, { childList: true, characterData: true, subtree: true });
            derive();
        }

        // Nom du projet : recopié dans l'en-tête du menu Projet.
        const name = $("current-project");
        const copyName = () => document.querySelectorAll("[data-project-name]").forEach((node) => { node.textContent = name.textContent; });
        if (name) {
            new MutationObserver(copyName).observe(name, { childList: true, characterData: true, subtree: true });
            copyName();
        }

        // Fichier actif : message d'information (index.html seulement) et langage du pied de panneau.
        const container = $("editor-container");
        const tabs = document.querySelector(".file-tabs");
        const syncTab = () => {
            const active = tabs?.querySelector(".tab.active");
            if (!active || !container) return;
            const id = active.id.replace("-tab", "");
            container.dataset.activeTab = id;
            const lang = $("pane-lang");
            if (lang) lang.textContent = LANGUAGE_LABELS[id] ?? lang.textContent;
        };
        if (tabs) {
            new MutationObserver(syncTab).observe(tabs, { attributes: true, attributeFilter: ["class"], subtree: true });
            syncTab();
        }

        // Monaco ne redimensionne pas ses éditeurs tout seul (hors Python) : on le fait quand leur panneau change.
        if (container) new ResizeObserver(() => Workbench.#relayout()).observe(container);
    }

    static #relayout() {
        requestAnimationFrame(() => window.monaco?.editor.getEditors().forEach((editor) => editor.layout()));
    }

    /* ------------------------------------ Disposition ------------------------------------ */

    static #layout() {
        const main = $("main-editor");
        if (!main) return;
        const apply = (value) => {
            if (value === "auto") delete main.dataset.layout; else main.dataset.layout = value;
            document.querySelectorAll("[data-layout]").forEach((item) => {
                if (item !== main) item.setAttribute("aria-checked", String(item.dataset.layout === value));
            });
            Workbench.#relayout();
        };
        let saved = "auto";
        try { saved = localStorage.getItem(LAYOUT_KEY) || "auto"; } catch { /* stockage bloqué */ }
        apply(saved);
        document.querySelectorAll("button[data-layout]").forEach((button) => {
            button.addEventListener("click", () => {
                apply(button.dataset.layout);
                try { localStorage.setItem(LAYOUT_KEY, button.dataset.layout); } catch { /* stockage bloqué */ }
            });
        });
    }

    /* ------------------------------------ Redémarrer ------------------------------------ */

    static #restart() {
        const clear = () => (isPython() ? $("py-clear") : $("console-clear"))?.click();
        $("restart-btn")?.addEventListener("click", () => {
            if (isPython()) {
                const app = window.pythonEditor;
                if (app?.running) app.stop();
                clear();
            } else {
                clear();
                $("run-code")?.click();
            }
        });
        $("restart-preview")?.addEventListener("click", () => $("run-code")?.click());
        $("restart-clear")?.addEventListener("click", clear);
    }
}
