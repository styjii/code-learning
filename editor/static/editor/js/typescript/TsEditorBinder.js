import { state } from "./state.js";
import { TsProjectManager } from "./TsProjectManager.js";
import { TsPreviewManager } from "./TsPreviewManager.js";

/**
 * Branche les écouteurs de changement des éditeurs : sauvegarde différée du projet et
 * aperçu automatique (avec délai) s'il est activé.
 */
export class TsEditorBinder {
    static bindChangeListeners() {
        ["html", "css", "ts"].forEach((type) => {
            state.editors[type].onDidChangeModelContent(() => {
                if (state.isLoading) return; // contenu posé par le chargement d'un projet
                TsProjectManager.scheduleSave();

                if (state.autoLive) {
                    clearTimeout(state.debounceTimer);
                    state.debounceTimer = setTimeout(() => TsPreviewManager.updateCdnLinks(), state.debounceDelay);
                }
            });
        });
    }
}
