import { state } from "./state.js";
import { applyCompilerOptions, normalizeCompilerOptions, summarizeCompilerOptions } from "./TsCompilerOptions.js";

/**
 * Applique les options du compilateur : état, compilateur de Monaco, formulaire de la fenêtre
 * « Options TypeScript » et résumé de la barre de commandes. Ne sauvegarde rien : l'enregistrement
 * du projet est déclenché par TsOptionsEvents (changement de l'utilisateur) et non au chargement.
 */
export class TsOptionsManager {
    /** @param {object} options options (même incomplètes) : complétées par les valeurs par défaut. */
    static apply(options) {
        state.compilerOptions = normalizeCompilerOptions(options);
        if (window.monaco) applyCompilerOptions(window.monaco, state.compilerOptions);
        this.syncForm();
        this.updateSummary();
    }

    /** Reflète les options actives dans les contrôles de la fenêtre. */
    static syncForm() {
        document.querySelectorAll("[data-ts-option]").forEach((control) => {
            const value = state.compilerOptions[control.dataset.tsOption];
            if (control.type === "checkbox") control.checked = value === true;
            else control.value = String(value);
        });
    }

    static updateSummary() {
        const summary = document.getElementById("ts-summary");
        if (summary) summary.textContent = summarizeCompilerOptions(state.compilerOptions);
    }
}
