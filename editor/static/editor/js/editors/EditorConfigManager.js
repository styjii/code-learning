import { state } from "../state/state.js";
import { patchPassiveTouchStart } from "./utils.js";

/**
 * Manages loading, saving, updating, and applying Monaco Editor configurations.
 */
export class EditorConfigManager {
    /**
     * @param {{editors: Record<string, any>}} [editorState] état qui porte les éditeurs à configurer
     *        (celui de l'éditeur Web par défaut ; l'éditeur TypeScript passe le sien)
     */
    constructor(editorState = state) {
        this.state = editorState;

        /** @type {object} current config */
        this.editorConfig = {};

        /** @type {Promise<void>} file d'attente : les enregistrements partent dans l'ordre des clics */
        this._saving = Promise.resolve();

        // Patch event listeners for performance
        patchPassiveTouchStart();
    }

    /**
     * Loads the current user's Monaco config from backend (defaults + saved preferences) or sets defaults.
     * @returns {Promise<object>} Loaded or default config
     */
    async loadConfig() {
        try {
            const res = await fetch("/editor/api/load-monaco-config/");
            if (!res.ok) throw new Error("Failed to fetch config");
            this.editorConfig = await res.json();
        } catch (err) {
            console.warn("Falling back to default Monaco config:", err);
            this.editorConfig = {
                wordWrap: "on",
                scrollBeyondLastLine: true,
                tabSize: 4,
                insertSpaces: true,
                minimap: { enabled: true },
            };
        }
        return this.editorConfig;
    }

    /**
     * Saves one preference for the current user (fire and forget).
     * Only the changed option is sent: the server accepts a whitelist of keys and merges it
     * with the user's previous preferences. Requests are chained to keep their order.
     * @param {string} key Option key
     * @param {any} value Option value
     */
    savePreference(key, value) {
        this._saving = this._saving
            .then(() =>
                fetch("/editor/api/save-monaco-config/", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ [key]: value }),
                })
            )
            .then((res) => {
                if (!res.ok) console.warn("Monaco preference refused by the server:", key, res.status);
            })
            .catch((err) => {
                console.warn("Failed to save Monaco preference:", err);
            });
    }

    /**
     * Updates a user preference: applies it to all editors and saves it for this user.
     * @param {string} key Option key
     * @param {any} value Option value
     */
    updateOption(key, value) {
        Object.values(this.state.editors).forEach((editor) => {
            if (editor?.updateOptions) {
                editor.updateOptions({ [key]: value });
            }
        });
        this.editorConfig[key] = value;
        this.savePreference(key, value);
    }

    /**
     * Gets current editor configuration copy.
     * @returns {object}
     */
    getConfig() {
        return { ...this.editorConfig };
    }

    /**
     * Registers UI buttons and keyboard shortcuts for Monaco editor commands.
     */
    registerCommands() {
        const getActiveEditor = () => {
            const activeTabId = document.querySelector(".tab.active")?.id?.replace("-tab", "");
            return this.state.editors[activeTabId];
        };

        const toggleWordWrap = () => {
            const current = this.editorConfig.wordWrap;
            this.updateOption("wordWrap", current === "on" ? "off" : "on");
        };

        const toggleScrollPadding = () => {
            const current = this.editorConfig.scrollBeyondLastLine;
            this.updateOption("scrollBeyondLastLine", !current);
        };

        document.getElementById("format-document")?.addEventListener("click", () => {
            const editor = getActiveEditor();
            if (editor) {
                editor.focus();
                editor.getAction("editor.action.formatDocument")?.run();
            }
        });

        document.getElementById("command-palette")?.addEventListener("click", () => {
            const editor = getActiveEditor();
            if (editor) {
                editor.focus();
                editor.getAction("editor.action.quickCommand")?.run();
            }
        });

        document.getElementById("text-wrap")?.addEventListener("click", toggleWordWrap);
        document.getElementById("toggle-scroll-padding")?.addEventListener("click", toggleScrollPadding);

        window.addEventListener("keydown", (e) => {
            if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
                e.preventDefault();
                document.getElementById("run-code")?.click();
            }
            if (e.shiftKey && e.altKey && e.code === "KeyF") {
                document.getElementById("format-document")?.click();
            }
            if (e.ctrlKey && e.shiftKey && e.code === "KeyP") {
                document.getElementById("command-palette")?.click();
            }
            if (e.ctrlKey && e.altKey && e.code === "KeyW") {
                e.preventDefault();
                toggleWordWrap();
            }
            if (e.ctrlKey && e.altKey && e.code === "KeyL") {
                e.preventDefault();
                toggleScrollPadding();
            }
        });
    }
}
