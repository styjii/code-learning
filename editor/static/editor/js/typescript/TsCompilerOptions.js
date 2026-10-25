/**
 * Options du compilateur TypeScript : valeurs par défaut, correspondance avec Monaco, résumé affiché.
 * Les mêmes clés et valeurs sont validées côté serveur (editor/typescript_config.py).
 */

/**
 * Valeurs numériques de ScriptTarget dans le compilateur embarqué par Monaco 0.47.
 * L'énumération « monaco.languages.typescript.ScriptTarget » s'arrête à ES2020 : ES2021 (8) et
 * ES2022 (9) ne sont donc pas lisibles par leur nom.
 */
export const TARGETS = {
    ES5: 1,
    ES2015: 2,
    ES2016: 3,
    ES2017: 4,
    ES2018: 5,
    ES2019: 6,
    ES2020: 7,
    ES2021: 8,
    ES2022: 9,
    ESNext: 99,
};

export const DEFAULT_COMPILER_OPTIONS = Object.freeze({
    target: "ESNext",
    strict: true,
    noImplicitReturns: false,
    noFallthroughCasesInSwitch: false,
    noUncheckedIndexedAccess: false,
    noUnusedLocals: false,
    noUnusedParameters: false,
    noEmitOnError: true,
});

/**
 * Complète des options reçues (serveur, formulaire) : seules les clés connues et de bon type sont gardées,
 * le reste reprend la valeur par défaut.
 * @param {object} [raw]
 * @returns {Record<string, string|boolean>}
 */
export function normalizeCompilerOptions(raw = {}) {
    const options = { ...DEFAULT_COMPILER_OPTIONS };
    for (const [key, fallback] of Object.entries(DEFAULT_COMPILER_OPTIONS)) {
        const value = raw?.[key];
        if (typeof value !== typeof fallback) continue;
        if (key === "target" && !(value in TARGETS)) continue;
        options[key] = value;
    }
    return options;
}

/**
 * Options au format attendu par Monaco (setCompilerOptions).
 * « noEmitOnError » n'en fait pas partie : le blocage de l'exécution est décidé par TsPreviewManager,
 * qui a besoin de la sortie JavaScript même quand il y a des erreurs (pour les afficher).
 * @param {typeof import("monaco-editor")} monaco
 * @param {Record<string, string|boolean>} options
 */
export function toMonacoOptions(monaco, options) {
    const ts = monaco.languages.typescript;
    return {
        target: TARGETS[options.target] ?? TARGETS.ESNext,
        // Imposés (voir FIXED_COMPILER_OPTIONS côté serveur) : le script est un module.
        module: ts.ModuleKind.ESNext,
        moduleResolution: ts.ModuleResolutionKind.NodeJs,
        moduleDetection: 3, // « force » : tout fichier est un module
        strict: options.strict,
        noImplicitReturns: options.noImplicitReturns,
        noFallthroughCasesInSwitch: options.noFallthroughCasesInSwitch,
        noUncheckedIndexedAccess: options.noUncheckedIndexedAccess,
        noUnusedLocals: options.noUnusedLocals,
        noUnusedParameters: options.noUnusedParameters,
        allowNonTsExtensions: true,
        noEmitOnError: false,
    };
}

/** Applique les options au compilateur de Monaco : vérification, soulignements et JavaScript produit. */
export function applyCompilerOptions(monaco, options) {
    monaco.languages.typescript.typescriptDefaults.setCompilerOptions(toMonacoOptions(monaco, options));
}

/** Résumé court des options actives, affiché dans la barre de commandes (« ESNext · strict »). */
export function summarizeCompilerOptions(options) {
    const extras = Object.keys(DEFAULT_COMPILER_OPTIONS).filter(
        (key) => !["target", "strict", "noEmitOnError"].includes(key) && options[key]
    ).length;
    const parts = [options.target, options.strict ? "strict" : "non strict"];
    if (extras) parts.push(`+${extras} option${extras > 1 ? "s" : ""}`);
    if (!options.noEmitOnError) parts.push("non bloquant");
    return parts.join(" · ");
}
