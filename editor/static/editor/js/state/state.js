/**
 * Holds global state for editor controls, editor instances, and project management.
 */
export class State {
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

        /** @type {{html: monaco.editor.IStandaloneCodeEditor|null, css: monaco.editor.IStandaloneCodeEditor|null, js: monaco.editor.IStandaloneCodeEditor|null}} */
        this.editors = {
            html: null,
            css: null,
            js: null,
        };

        /** @type {string|null} Current project identifier or null if none selected */
        this.currentProject = null;

        /** @type {Record<string, any>} Collection of projects keyed by project ID or name */
        this.projects = {};

        /** @type {string[]} Array of CSS CDN URLs */
        this.cssCdnLinks = [];

        /** @type {string[]} Array of JS CDN URLs */
        this.jsCdnLinks = [];
    }
}

export const state = new State();
