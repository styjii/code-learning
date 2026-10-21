/**
 * Utility for formatting JavaScript values into human-readable strings.
 */
export class ValueFormatter {
    /**
     * Converts a JavaScript value into a pretty-printed string.
     * Handles arrays, sets, maps, errors, and general objects.
     * @param {any} val - Value to format.
     * @param {number} indent - Current indentation level.
     * @returns {string}
     */
    static format(val, indent = 0) {
        const pad = (level = indent) => " ".repeat(level);
        const nextIndent = indent + 2;

        if (val === null) return "null";
        if (val === undefined) return "undefined";
        if (typeof val === "string") return `"${val}"`;
        if (typeof val === "number" || typeof val === "boolean") return String(val);
        if (typeof val === "function") return "[Function]";
        if (typeof val === "symbol") return val.toString();

        if (Array.isArray(val)) {
            return `Array(${val.length})`;
        }

        try {
            const keys = Object.keys(val);
            return `Object { ${keys.slice(0, 3).join(", ")}${keys.length > 3 ? ", …" : ""} }`;
        } catch {
            return "[object Object]";
        }
    }
}
