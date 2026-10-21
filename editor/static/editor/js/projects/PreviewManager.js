import { state } from "../state/state.js";

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

        consoleEl.innerHTML = "";

        const formData = new FormData();
        formData.append("html", this.#sanitizeHTML(state.editors.html?.getValue() ?? ""));
        formData.append("css", state.editors.css?.getValue() ?? "");
        formData.append("js", state.editors.js?.getValue() ?? "");
        formData.append("cdn_css", JSON.stringify(state.cssCdnLinks));
        formData.append("cdn_js", JSON.stringify(state.jsCdnLinks));

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
        e.currentTarget.textContent = `Auto : ${state.autoLive ? "activé" : "désactivé"}`;
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
