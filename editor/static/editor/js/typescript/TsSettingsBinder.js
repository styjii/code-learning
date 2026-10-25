import { state } from "./state.js";
import { TsPreviewManager } from "./TsPreviewManager.js";

/**
 * Branche les réglages de l'aperçu : délai de l'aperçu automatique et Bootstrap.
 */
export class TsSettingsBinder {
    static bindListeners() {
        this.#initializeDelay();
        this.#initializeBootstrapToggle();
    }

    static #initializeDelay() {
        const delayInput = document.getElementById("delay");
        const delayValueLabel = document.getElementById("delay-value");

        delayInput.value = state.debounceDelay;
        delayValueLabel.textContent = `${state.debounceDelay}ms`;

        delayInput.addEventListener("input", (e) => {
            const newDelay = parseInt(e.target.value, 10);
            state.debounceDelay = newDelay;
            delayValueLabel.textContent = `${newDelay}ms`;
        });
    }

    static #initializeBootstrapToggle() {
        const bootstrapToggle = document.getElementById("bootstrapCdnSwitch");

        // Réglage propre à cet éditeur (l'éditeur Web a le sien).
        let stored = null;
        try { stored = localStorage.getItem("typescript-editor:useBootstrap"); } catch { /* stockage indisponible */ }
        bootstrapToggle.checked = stored === "true";
        TsPreviewManager.syncCdnLinks(); // l'aperçu est lancé par le chargement du projet

        bootstrapToggle.addEventListener("change", () => {
            try { localStorage.setItem("typescript-editor:useBootstrap", bootstrapToggle.checked); } catch { /* idem */ }
            TsPreviewManager.updateCdnLinks();
        });
    }
}
