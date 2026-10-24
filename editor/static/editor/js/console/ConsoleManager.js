import { ConsoleRenderer } from "./ConsoleRenderer.js";

/**
 * Reçoit les messages postés par l'iframe d'aperçu (iframe-console.js) et les confie au
 * ConsoleRenderer. Seuls les messages de l'iframe d'aperçu sont acceptés.
 */
export class ConsoleManager {
    static renderer = null;

    /** Crée le moteur d'affichage dans l'élément #console. */
    static init() {
        const root = document.getElementById("console");
        ConsoleManager.renderer = new ConsoleRenderer(root);
    }

    /** @param {MessageEvent} event message {__console: true, type, args, …} */
    static handleMessage(event) {
        const message = event.data;
        if (!message || message.__console !== true || !message.type) return;

        const frame = document.getElementById("output");
        if (frame && event.source !== frame.contentWindow) return;

        if (!ConsoleManager.renderer) ConsoleManager.init();
        ConsoleManager.renderer.add(message);
    }
}
