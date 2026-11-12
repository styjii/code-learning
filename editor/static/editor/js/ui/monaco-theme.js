/**
 * Thèmes Monaco de l'éditeur (sombre et clair), assortis à la palette de layout.css.
 */
const DARK = {
    base: "vs-dark",
    colors: {
        "editor.background": "#0f0f12",
        "editor.foreground": "#e2e2ea",
        "editor.lineHighlightBackground": "#1d1a30",
        "editor.lineHighlightBorder": "#00000000",
        "editor.selectionBackground": "#3b3361",
        "editor.inactiveSelectionBackground": "#2a2545",
        "editorCursor.foreground": "#b9a1f7",
        "editorLineNumber.foreground": "#5b5b6b",
        "editorLineNumber.activeForeground": "#b0b0c4",
        "editorIndentGuide.background1": "#23232c",
        "editorIndentGuide.activeBackground1": "#3a3a48",
        "editorWidget.background": "#16161b",
        "editorSuggestWidget.background": "#16161b",
        "editorSuggestWidget.selectedBackground": "#2c2549",
        "editorGutter.background": "#0f0f12",
        "minimap.background": "#0f0f12",
    },
    rules: [
        { token: "comment", foreground: "6b6b80", fontStyle: "italic" },
        { token: "keyword", foreground: "c4a7ff" },
        { token: "string", foreground: "c9e48c" },
        { token: "number", foreground: "f9a875" },
        { token: "type", foreground: "7dd3fc" },
        { token: "tag", foreground: "ff7b9c" },
        { token: "metatag", foreground: "ff7b9c" },
        { token: "delimiter.html", foreground: "ff7b9c" },
        { token: "attribute.name", foreground: "7dd3fc" },
        { token: "attribute.value", foreground: "c9e48c" },
        { token: "attribute.name.css", foreground: "7dd3fc" },
        { token: "attribute.value.css", foreground: "f9a875" },
        { token: "attribute.value.number.css", foreground: "f9a875" },
        { token: "attribute.value.unit.css", foreground: "f9a875" },
        { token: "tag.css", foreground: "ff7b9c" },
    ],
};

const LIGHT = {
    base: "vs",
    colors: {
        "editor.background": "#ffffff",
        "editor.foreground": "#25222f",
        "editor.lineHighlightBackground": "#f1edff",
        "editor.lineHighlightBorder": "#00000000",
        "editor.selectionBackground": "#d9cffb",
        "editorCursor.foreground": "#6a4fd8",
        "editorLineNumber.foreground": "#a29db4",
        "editorLineNumber.activeForeground": "#4a4560",
        "editorIndentGuide.background1": "#ece9f5",
        "editorGutter.background": "#ffffff",
    },
    rules: [
        { token: "comment", foreground: "8a869a", fontStyle: "italic" },
        { token: "keyword", foreground: "7a3fe0" },
        { token: "string", foreground: "3a7d0a" },
        { token: "number", foreground: "c2570c" },
        { token: "type", foreground: "0b73a8" },
        { token: "tag", foreground: "d6336c" },
        { token: "metatag", foreground: "d6336c" },
        { token: "delimiter.html", foreground: "d6336c" },
        { token: "attribute.name", foreground: "0b73a8" },
        { token: "attribute.value", foreground: "3a7d0a" },
        { token: "attribute.name.css", foreground: "0b73a8" },
        { token: "attribute.value.css", foreground: "c2570c" },
    ],
};

/** Nom du thème Monaco pour un thème du site ("light" | "dark"). */
export function monacoThemeName(siteTheme = document.documentElement.dataset.theme) {
    return siteTheme === "light" ? "codelab-light" : "codelab-dark";
}

/** Déclare les deux thèmes (idempotent). */
export function defineMonacoThemes(monaco) {
    monaco.editor.defineTheme("codelab-dark", { ...DARK, inherit: true });
    monaco.editor.defineTheme("codelab-light", { ...LIGHT, inherit: true });
}

/** Déclare les thèmes, applique celui du site et le suit quand il change (Python : pas de gestionnaire dédié). */
export function applyMonacoTheme(monaco) {
    defineMonacoThemes(monaco);
    monaco.editor.setTheme(monacoThemeName());
    document.addEventListener("themechange", (event) => monaco.editor.setTheme(monacoThemeName(event.detail)));
}
