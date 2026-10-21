import { PreviewManager } from "../projects/PreviewManager.js";

/**
 * ToolbarEvents handles event binding for toolbar actions:
 * - Run code
 * - Toggle live preview
 * - Toggle console visibility
 */
export class ToolbarEvents {
    /**
     * Binds all toolbar-related events.
     */
    static bind() {
        document.getElementById("run-code").addEventListener("click", () => PreviewManager.run());
        document.getElementById("live-code").addEventListener("click", (e) => PreviewManager.toggleLive(e));
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
