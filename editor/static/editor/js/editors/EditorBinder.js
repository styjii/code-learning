import { state } from "../state/state.js";
import { ProjectManager } from "../projects/ProjectManager.js";
import { PreviewManager } from "../projects/PreviewManager.js";

/**
 * Handles binding change listeners to Monaco editors and triggering save/preview logic.
 */
export class EditorBinder {
    /**
     * Attaches change listeners to HTML, CSS, and JS editors.
     * - Sauvegarde le projet (différée, regroupe les frappes).
     * - Triggers live preview if enabled, with debounce.
     */
    static bindChangeListeners() {
        ["html", "css", "js"].forEach((type) => {
            state.editors[type].onDidChangeModelContent(() => {
                if (state.isLoading) return; // contenu posé par le chargement d'un projet
                ProjectManager.scheduleSave();

                if (state.autoLive) {
                    clearTimeout(state.debounceTimer);
                    state.debounceTimer = setTimeout(
                        () => PreviewManager.updateCdnLinks(),
                        state.debounceDelay
                    );
                }
            });
        });
    }
}
