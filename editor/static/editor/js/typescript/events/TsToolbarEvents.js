import { TsPreviewManager } from "../TsPreviewManager.js";

/**
 * Barre de commandes : exécuter, aperçu automatique, afficher / masquer la console.
 */
export class TsToolbarEvents {
    static bind() {
        document.getElementById("run-code").addEventListener("click", () => TsPreviewManager.run());
        document.getElementById("live-code").addEventListener("click", (e) => TsPreviewManager.toggleLive(e));
    }
}
