/**
 * Loads JavaScript snippets from a JSON URL and registers them
 * as Monaco completion items for JavaScript language.
 */
export class JsSnippetLoader {
    /**
     * @param {string} url URL to JSON snippet definitions
     * @param {() => void} [callback] Optional callback when loading completes
     */
    constructor(url, callback) {
        this.url = url;
        this.callback = callback;
    }

    /**
     * Fetches snippet JSON and registers completion provider.
     * @returns {Promise<void>}
     */
    async load() {
        const res = await fetch(this.url);
        if (!res.ok)
            throw new Error(`Failed to load snippets from ${this.url}`);

        const json = await res.json();

        const suggestions = Object.entries(json).map(([key, snippet]) => ({
            label: snippet.prefix,
            kind: monaco.languages.CompletionItemKind.Snippet,
            insertText: Array.isArray(snippet.body)
                ? snippet.body.join("\n")
                : snippet.body,
            insertTextRules:
                monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            documentation: snippet.description,
            sortText: snippet.prefix || key,
            range: null,
        }));

        monaco.languages.registerCompletionItemProvider("javascript", {
            provideCompletionItems: (model, position) => {
                const word = model.getWordUntilPosition(position);
                const range = {
                    startLineNumber: position.lineNumber,
                    endLineNumber: position.lineNumber,
                    startColumn: word.startColumn,
                    endColumn: word.endColumn,
                };
                return {
                    suggestions: suggestions.map((s) => ({ ...s, range })),
                };
            },
        });

        if (this.callback) this.callback();
    }
}
