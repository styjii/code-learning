/**
 * Vérifie un modèle TypeScript et produit son JavaScript, avec le compilateur intégré à Monaco
 * (le même que celui des blocs exécutables des cours, voir language/js/runner/TsRunner.js).
 */

/** Aplati un message de diagnostic TypeScript (chaîne ou chaîne de messages). */
function flatten(message) {
    if (typeof message === "string") return message;
    return [message.messageText, ...(message.next ?? []).map(flatten)].join(" ");
}

/**
 * @param {typeof import("monaco-editor")} monaco
 * @param {monaco.editor.ITextModel} model
 * @returns {Promise<{errors: {line: number, column: number, code: number, message: string}[], js: string}>}
 *          « errors » : erreurs de syntaxe et de type, dans l'ordre du fichier ; « js » : JavaScript produit
 *          (module ES, avec « export {}; » si le fichier n'importe ni n'exporte rien).
 */
export async function compileTypeScript(monaco, model) {
    const getWorker = await monaco.languages.typescript.getTypeScriptWorker();
    const worker = await getWorker(model.uri);
    const uri = model.uri.toString();

    const [syntax, semantic] = await Promise.all([
        worker.getSyntacticDiagnostics(uri),
        worker.getSemanticDiagnostics(uri),
    ]);

    const errors = [...syntax, ...semantic]
        .filter((diagnostic) => diagnostic.category === 1) // 1 = erreur (les avertissements sont ignorés)
        .map((diagnostic) => {
            const { lineNumber, column } = model.getPositionAt(diagnostic.start ?? 0);
            return { line: lineNumber, column, code: diagnostic.code, message: flatten(diagnostic.messageText) };
        })
        .sort((a, b) => a.line - b.line || a.column - b.column);

    const emitted = await worker.getEmitOutput(uri);
    const js = emitted.outputFiles.find((file) => file.name.endsWith(".js"))?.text ?? "";
    return { errors, js };
}
