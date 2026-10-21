import { state } from "../state/state.js";
import { PreviewManager } from "./PreviewManager.js";

/**
 * Binds settings-related DOM controls to global state and triggers preview updates.
 */
export class SettingsBinder {
    /**
     * Attaches event listeners to the settings UI components.
     * Initializes values from state and localStorage.
     */
    static bindListeners() {
        this._initializeDelay();
        this._initializeBootstrapToggle();
    }

    /**
     * Initializes debounce delay input from state.
     * Syncs label and listens for user input to update global delay.
     * @private
     */
    static _initializeDelay() {
        const delayInput = document.getElementById("delay");
        const delayValueLabel = document.getElementById("delay-value");

        // Initialize UI with state value
        delayInput.value = state.debounceDelay;
        delayValueLabel.textContent = `${state.debounceDelay}ms`;

        delayInput.addEventListener("input", (e) => {
            const newDelay = parseInt(e.target.value, 10);
            state.debounceDelay = newDelay;
            delayValueLabel.textContent = `${newDelay}ms`;
        });
    }

    /**
     * Initializes the Bootstrap CDN toggle from localStorage,
     * binds change listener, and updates the preview accordingly.
     * @private
     */
    static _initializeBootstrapToggle() {
        const bootstrapToggle = document.getElementById("bootstrapCdnSwitch");

        // Restore saved state
        const stored = localStorage.getItem("useBootstrap");
        bootstrapToggle.checked = stored === "true";

        // Update CDN links on load if Bootstrap is enabled
        if (bootstrapToggle.checked) {
            PreviewManager.updateCdnLinks();
        }

        // Bind toggle change
        bootstrapToggle.addEventListener("change", () => {
            localStorage.setItem("useBootstrap", bootstrapToggle.checked);
            PreviewManager.updateCdnLinks();
        });
    }
}
