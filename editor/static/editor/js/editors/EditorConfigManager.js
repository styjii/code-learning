import { state } from "../state/state.js";
import { patchPassiveTouchStart } from "./utils.js";

/**
 * Manages loading, saving, updating, and applying Monaco Editor configurations.
 */
export class EditorConfigManager {
    constructor() {
        /** @type {object} current config */
        this.editorConfig = {};

        // Patch event listeners for performance
        patchPassiveTouchStart();
    }

    /**
     * Loads Monaco editor config from backend or sets defaults.
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
     * Saves current config to backend (fire and forget).
     */
    saveConfig() {
        fetch("/editor/api/save-monaco-config/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(this.editorConfig),
        }).catch((err) => {
            console.warn("Failed to save Monaco config:", err);
        });
    }

    /**
     * Updates an option in config, applies to all editors and saves.
     * @param {string} key Option key
     * @param {any} value Option value
     */
    updateOption(key, value) {
        Object.values(state.editors).forEach((editor) => {
            if (editor?.updateOptions) {
                editor.updateOptions({ [key]: value });
            }
        });
        this.editorConfig[key] = value;
        this.saveConfig();
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
            return state.editors[activeTabId];
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
