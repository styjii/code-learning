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
    }
}
