/**
 * Chargement paresseux de Monaco (le même que l'éditeur en ligne).
 * Rien n'est téléchargé tant qu'aucun bloc de code n'est ouvert pour exécution.
 */
let loading = null;

const THEMES = {
    dark: { base: "vs-dark", bg: "#0f141b", line: "#5b6676" },
    light: { base: "vs", bg: "#f6f8fa", line: "#8692a4" },
};

const currentTheme = () => (document.documentElement.dataset.theme === "light" ? "light" : "dark");

function configure(monaco) {
    for (const [name, { base, bg, line }] of Object.entries(THEMES)) {
        monaco.editor.defineTheme(`course-${name}`, {
            base,
            inherit: true,
            rules: [],
            colors: {
                "editor.background": bg,
                "editor.lineHighlightBackground": "#00000000",
                "editorLineNumber.foreground": line,
                "editorGutter.background": bg,
            },
        });
    }
    monaco.editor.setTheme(`course-${currentTheme()}`);
    document.addEventListener("themechange", () => monaco.editor.setTheme(`course-${currentTheme()}`));

    // Chaque bloc est un module indépendant (pas de conflit entre variables de deux blocs).
    // module ESNext + cible ≥ ES2017 : indispensable pour que « await » (et « for await ») au niveau
    // supérieur soit accepté (TS1378 / TS1432 avec CommonJS). Le « export {} » ajouté par TypeScript
    // est retiré avant exécution (voir TsRunner.js). ES2022 fournit aussi Promise.any, Array.at, etc.
    const ts = monaco.languages.typescript;
    ts.typescriptDefaults.setCompilerOptions({
        // 9 = ES2022. L'énumération ScriptTarget de Monaco n'a pas ce nom (ts.ScriptTarget.ES2022 vaut
        // undefined et la cible retomberait sur ES5), et ESNext laisserait passer les décorateurs et
        // « accessor » tels quels, que le navigateur refuse : ES2022 les transforme.
        target: 9,
        module: ts.ModuleKind.ESNext,
        moduleResolution: ts.ModuleResolutionKind.NodeJs,
        moduleDetection: 3, // « force » : tout fichier est un module
        strict: true,
        allowNonTsExtensions: true,
        noEmitOnError: false,
    });
    ts.typescriptDefaults.setEagerModelSync(true);
    // Les extraits JavaScript sont souvent des fragments : on ne garde que la syntaxe.
    ts.javascriptDefaults.setDiagnosticsOptions({ noSemanticValidation: true, noSyntaxValidation: false });
}

/** @returns {Promise<typeof import("monaco-editor")>} */
export function loadMonaco() {
    if (loading) return loading;

    const base = document.body.dataset.monaco;
    loading = new Promise((resolve, reject) => {
        const script = document.createElement("script");
        script.src = `${base}/loader.js`;
        script.onerror = () => reject(new Error("Impossible de charger l'éditeur de code."));
        script.onload = () => {
            window.require.config({
                paths: { vs: base },
                "vs/nls": { availableLanguages: { "*": "fr" } },
            });
            window.require(["vs/editor/editor.main"], () => {
                configure(window.monaco);
                resolve(window.monaco);
            }, reject);
        };
        document.head.appendChild(script);
    });
    loading.catch(() => { loading = null; }); // permet de réessayer
    return loading;
}
