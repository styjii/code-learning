import { ConsoleRenderer } from "./ConsoleRenderer.js";

/**
 * Manages incoming console messages and delegates rendering.
 */
export class ConsoleManager {
    static renderer = null;

    /**
     * Initializes the ConsoleManager by creating a ConsoleRenderer instance 
     * attached to the console root DOM element.
     */
    static init() {
        const root = document.getElementById("console");
        ConsoleManager.renderer = new ConsoleRenderer(root);
    }

    /**
     * Handles console messages received via the window message event.
     * Initializes the renderer if not present. Delegates message types 
     * (clear, log, group, table, etc.) to the ConsoleRenderer.
     * 
     * @param {MessageEvent} event - The message event containing console data.
     */
    static handleMessage(event) {
        const { type, args = [], data, columns, label } = event.data;
        if (!type || (!args.length && !data && !label)) return;

        if (!ConsoleManager.renderer) {
            ConsoleManager.init();
        }

        if (type === "clear") {
            ConsoleManager.renderer.clear();
            return;
        }

        ConsoleManager.renderer.logMessage(type, args, data, columns, label);
    }
}
