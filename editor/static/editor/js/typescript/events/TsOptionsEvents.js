import { state } from "../state.js";
import { DEFAULT_COMPILER_OPTIONS } from "../TsCompilerOptions.js";
import { TsOptionsManager } from "../TsOptionsManager.js";
import { TsProjectManager } from "../TsProjectManager.js";
import { TsPreviewManager } from "../TsPreviewManager.js";

/**
 * Fenêtre « Options TypeScript » : chaque changement s'applique tout de suite au compilateur,
 * est enregistré avec le projet et relance l'aperçu automatique s'il est activé.
 */
export class TsOptionsEvents {
    static bind() {
        document.getElementById("ts-options-form").addEventListener("submit", (e) => e.preventDefault());

        document.querySelectorAll("[data-ts-option]").forEach((control) => {
            control.addEventListener("change", () => {
                const value = control.type === "checkbox" ? control.checked : control.value;
                this.#change({ ...state.compilerOptions, [control.dataset.tsOption]: value });
            });
        });

        document.getElementById("ts-options-reset").addEventListener("click", () => {
            this.#change({ ...DEFAULT_COMPILER_OPTIONS });
        });
    }

    static #change(options) {
        TsOptionsManager.apply(options);
        TsProjectManager.scheduleSave();
        if (state.autoLive) TsPreviewManager.updateCdnLinks();
    }
}
