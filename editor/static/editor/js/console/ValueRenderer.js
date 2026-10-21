/**
 * Renders JavaScript values into DOM nodes with interactive structure.
 */
export class ValueRenderer {
    /**
     * Recursively renders a value to an HTML element.
     * @param {any} val - The value to render.
     * @param {number} depth - Current render depth (default: 0).
     * @returns {HTMLElement}
     */
    static render(val, depth = 0) {
        const maxDepth = 5;

        if (depth > maxDepth) {
            const wrapper = document.createElement("span");
            wrapper.textContent = "...";
            return wrapper;
        }

        const span = document.createElement("span");
        span.classList.add("console-value");

        if (val === null) return this.#renderNull(span);
        if (val === undefined) return this.#renderUndefined(span);
        if (typeof val === "string") return this.#renderString(span, val);
        if (typeof val === "number") return this.#renderNumber(span, val);
        if (typeof val === "boolean") return this.#renderBoolean(span, val);
        if (typeof val === "function") return this.#renderFunction(span);
        if (typeof val === "symbol") return this.#renderSymbol(span, val);

        if (Array.isArray(val)) return this.#renderArray(val, depth);
        return this.#renderObject(val, depth);
    }

    static #renderNull(span) {
        span.textContent = "null";
        span.classList.add("null");
        return span;
    }

    static #renderUndefined(span) {
        span.textContent = "undefined";
        span.classList.add("undefined");
        return span;
    }

    static #renderString(span, val) {
        span.textContent = `"${val}"`;
        span.classList.add("string");
        return span;
    }

    static #renderNumber(span, val) {
        span.textContent = String(val);
        span.classList.add("number");
        return span;
    }

    static #renderBoolean(span, val) {
        span.textContent = String(val);
        span.classList.add("boolean");
        return span;
    }

    static #renderFunction(span) {
        span.textContent = "ƒ";
        span.classList.add("function");
        return span;
    }

    static #renderSymbol(span, val) {
        span.textContent = val.toString();
        span.classList.add("symbol");
        return span;
    }

    static #renderArray(val, depth) {
        const details = document.createElement("details");
        const summary = document.createElement("summary");
        summary.textContent = `Array(${val.length})`;
        details.appendChild(summary);

        val.forEach((item, index) => {
            const div = document.createElement("div");
            div.className = "console-entry";
            const keySpan = document.createElement("span");
            keySpan.textContent = `${index}: `;
            div.appendChild(keySpan);
            div.appendChild(ValueRenderer.render(item, depth + 1));
            details.appendChild(div);
        });
        return details;
    }

    static #renderObject(val, depth) {
        const keys = Object.keys(val);
        const details = document.createElement("details");
        const summary = document.createElement("summary");
        summary.textContent = `Object { ${keys.slice(0, 3).join(", ")}${keys.length > 3 ? ", …" : ""} }`;
        details.appendChild(summary);

        keys.forEach((k) => {
            const div = document.createElement("div");
            div.className = "console-entry";
            const keySpan = document.createElement("span");
            keySpan.textContent = `${k}: `;
            div.appendChild(keySpan);
            div.appendChild(ValueRenderer.render(val[k], depth + 1));
            details.appendChild(div);
        });
        return details;
    }
}
