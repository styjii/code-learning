import { DEFAULT_COMPILER_OPTIONS } from "./TsCompilerOptions.js";

/**
 * État global de l'éditeur TypeScript (même rôle que state/state.js pour l'éditeur Web) :
 * éditeurs, projets, aperçu automatique et options du compilateur du projet courant.
 */
export class TsState {
    constructor() {
        /** @type {boolean} */
        this.autoLive = false;

        /** @type {boolean} true pendant le chargement d'un projet : aucune sauvegarde déclenchée */
        this.isLoading = false;

        /** @type {number|null} Minuteur de sauvegarde différée */
        this.saveTimer = null;

        /** @type {number|null} Timer ID for debounce */
        this.debounceTimer = null;

        /** @type {number} Debounce delay in ms */
        this.debounceDelay = 500;

        /** @type {{html: monaco.editor.IStandaloneCodeEditor|null, css: monaco.editor.IStandaloneCodeEditor|null, ts: monaco.editor.IStandaloneCodeEditor|null}} */
        this.editors = {
            html: null,
            css: null,
            ts: null,
        };

        /** @type {string|null} Current project identifier or null if none selected */
        this.currentProject = null;

        /** @type {Record<string, {id: number, html: string, css: string, ts: string, compilerOptions: object}>} */
        this.projects = {};

        /** @type {string[]} Array of CSS CDN URLs */
        this.cssCdnLinks = [];

        /** @type {string[]} Array of JS CDN URLs */
        this.jsCdnLinks = [];

        /** @type {Record<string, string|boolean>} Options du compilateur du projet courant */
        this.compilerOptions = { ...DEFAULT_COMPILER_OPTIONS };
    }
}

export const state = new TsState();
