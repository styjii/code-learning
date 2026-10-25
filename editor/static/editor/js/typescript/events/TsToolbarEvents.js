import { TsPreviewManager } from "../TsPreviewManager.js";

/**
 * Barre de commandes : exécuter, aperçu automatique, afficher / masquer la console.
 */
export class TsToolbarEvents {
    static bind() {
        document.getElementById("run-code").addEventListener("click", () => TsPreviewManager.run());
        document.getElementById("live-code").addEventListener("click", (e) => TsPreviewManager.toggleLive(e));
        document.getElementById("display-console").addEventListener("click", () => {
            const consoleEl = document.getElementById("console");
            const output = document.getElementById("output");
            const showConsole = consoleEl.style.display === "none";
            consoleEl.style.display = showConsole ? "block" : "none";
            output.style.display = showConsole ? "none" : "block";
            document.getElementById("display-console").setAttribute("aria-pressed", String(showConsole));
        });
    }
}
