import { state } from "../state/state.js";
import { Workbench } from "../ui/Workbench.js";
import { PreviewStorage } from "./PreviewStorage.js";
import { CODELAB_JS } from "./api.js";

/**
 * Handles updating, sanitizing, and running the live preview logic.
 */
export class PreviewManager {
    /**
     * Updates CDN links based on UI toggle.
     */
    static updateCdnLinks() {
        const bootstrapSwitch = document.getElementById("bootstrapCdnSwitch");
        const baseUrl = `${location.origin}/static/dist`;

        state.cssCdnLinks = [];
        state.jsCdnLinks = [];

        if (bootstrapSwitch?.checked) {
            state.cssCdnLinks.push(`${baseUrl}/css/bootstrap.min.css`);
            state.jsCdnLinks.push(`${baseUrl}/js/bootstrap.bundle.min.js`);
        }

        this.run();
    }

    /**
     * Runs the live preview by sending content and CDN info to the backend.
     */
    static run() {
        const output = document.getElementById("output");
        const consoleEl = document.getElementById("console");
        if (!output || !consoleEl) return;

        // La console persiste d'une exécution à l'autre, comme celle d'un navigateur : seul le bouton « Effacer »
        // (ou console.clear() dans le code) la vide.
        const formData = new FormData();
        formData.append("html", this.#sanitizeHTML(state.editors.html?.getValue() ?? ""));
        formData.append("css", state.editors.css?.getValue() ?? "");
        formData.append("js", state.editors.js?.getValue() ?? "");
        formData.append("cdn_css", JSON.stringify(state.cssCdnLinks));
        formData.append("cdn_js", JSON.stringify(state.jsCdnLinks));
        formData.append("storage", PreviewStorage.begin(CODELAB_JS, state.projects[state.currentProject]?.id));

        fetch("/editor/preview/", {
            method: "POST",
            body: formData,
        })
            .then(res => res.json())
            .then(data => {
                output.src = data.url;
            })
            .catch(err => console.error("Preview error:", err));
    }

    /**
     * Toggles auto live preview on/off.
     * @param {MouseEvent} e
     */
    static toggleLive(e) {
        state.autoLive = !state.autoLive;
        Workbench.setLive(state.autoLive);
        if (state.autoLive) this.updateCdnLinks();
    }

    /**
     * Sanitizes HTML by removing unsafe elements.
     * @param {string} dirty
     * @returns {string}
     */
    static #sanitizeHTML(dirty) {
        const doc = new DOMParser().parseFromString(dirty, "text/html");
        doc.querySelectorAll("script, iframe, object, embed, link, style").forEach(el => el.remove());
        return doc.body.innerHTML;
    }
}
