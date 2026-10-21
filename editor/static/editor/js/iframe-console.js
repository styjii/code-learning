/**
 * Class that overrides native console methods to serialize arguments
 * and post messages to the parent window, enabling advanced logging
 * with support for circular references and special objects.
 */
class EnhancedConsole {
    constructor() {
        /**
         * Stores the original console methods so they can be called later.
         * @type {Object<string, Function>}
         * @private
         */
        this._original = {};

        /**
         * Serializer function to safely serialize values.
         * @type {function(any): any}
         * @private
         */
        this._serialize = this._createSerializer();
    }

    /**
     * Initializes the EnhancedConsole by overriding console methods and
     * setting up global error handlers.
     */
    init() {
        this._overrideBasicMethods();
        this._overrideExtendedMethods();
        this._setupGlobalErrorHandlers();
    }

    /**
     * Creates a serializer function that safely serializes values,
     * handling circular references and special objects.
     * @returns {function(any): any} Serializer function.
     * @private
     */
    _createSerializer() {
        return (val => {
            const seen = new WeakSet();

            /**
             * Recursively serialize a value.
             * @param {any} val The value to serialize.
             * @returns {any} Serialized representation.
             */
            function _serialize(val) {
                if (val === null || typeof val !== "object") {
                    if (typeof val === "symbol") return val.toString();
                    if (typeof val === "function") return val.toString();
                    return val;
                }

                if (seen.has(val)) return "[Circular]";
                seen.add(val);

                if (val instanceof Element) {
                    return {
                        __type: "DOMElement",
                        tagName: val.tagName,
                        outerHTML: val.outerHTML
                    };
                }

                if (val instanceof Set) {
                    return {
                        __type: "Set",
                        value: Array.from(val).map(_serialize)
                    };
                }

                if (val instanceof Map) {
                    return {
                        __type: "Map",
                        value: Array.from(val.entries()).map(([k, v]) => [
                            typeof k === "object" ? "[object]" : k,
                            _serialize(v)
                        ])
                    };
                }

                if (val instanceof Error) {
                    return {
                        __type: "Error",
                        value: val.message,
                        stack: val.stack
                    };
                }

                if (val instanceof Date) {
                    return {
                        __type: "Date",
                        value: val.toISOString()
                    };
                }

                if (val instanceof RegExp) {
                    return {
                        __type: "RegExp",
                        value: val.toString()
                    };
                }

                if (Array.isArray(val)) {
                    return val.map(_serialize);
                }

                const result = {};
                for (const key in val) {
                    if (Object.prototype.hasOwnProperty.call(val, key)) {
                        const v = val[key];
                        result[key] = typeof v === "function" ? "[Function]" : _serialize(v);
                    }
                }
                return result;
            }

            return _serialize(val);
        });
    }

    /**
     * Overrides basic console methods: log, info, warn, error, debug, trace.
     * Posts serialized data to parent and calls original console methods.
     * @private
     */
    _overrideBasicMethods() {
        const methods = ["log", "info", "warn", "error", "debug", "trace"];
        methods.forEach(type => {
            const original = console[type];
            this._original[type] = original;
            console[type] = (...args) => {
                parent.postMessage({ type, args: args.map(this._serialize) }, "*");
                original.apply(console, args);
            };
        });
    }

    /**
     * Overrides extended console methods like assert, count, countReset, dir, group, time, clear, table, etc.
     * Posts serialized data to parent and calls original console methods.
     * @private
     */
    _overrideExtendedMethods() {
        const o = this._original;

        o.assert = console.assert;
        o.count = console.count;
        o.countReset = console.countReset;
        o.dir = console.dir;
        o.dirxml = console.dirxml;
        o.group = console.group;
        o.groupCollapsed = console.groupCollapsed;
        o.groupEnd = console.groupEnd;
        o.time = console.time;
        o.timeEnd = console.timeEnd;
        o.clear = console.clear;
        o.table = console.table;

        console.assert = (cond, ...args) => {
            if (!cond) parent.postMessage({ type: "assert", args: args.map(this._serialize) }, "*");
            return o.assert(cond, ...args);
        };

        console.count = (label = "default") => {
            parent.postMessage({ type: "count", label }, "*");
            return o.count(label);
        };

        console.countReset = (label = "default") => {
            parent.postMessage({ type: "countReset", label }, "*");
            return o.countReset(label);
        };

        console.dir = obj => {
            parent.postMessage({ type: "dir", obj: this._serialize(obj) }, "*");
            return o.dir(obj);
        };

        console.dirxml = (...data) => {
            parent.postMessage({ type: "dirxml", data: data.map(this._serialize) }, "*");
            return o.dirxml(...data);
        };

        console.group = (...label) => {
            parent.postMessage({ type: "group", label: label.map(this._serialize) }, "*");
            return o.group(...label);
        };

        console.groupCollapsed = (...label) => {
            parent.postMessage({ type: "groupCollapsed", label: label.map(this._serialize) }, "*");
            return o.groupCollapsed(...label);
        };

        console.groupEnd = () => {
            parent.postMessage({ type: "groupEnd" }, "*");
            return o.groupEnd();
        };

        console.time = (label = "default") => {
            parent.postMessage({ type: "time", label }, "*");
            return o.time(label);
        };

        console.timeEnd = (label = "default") => {
            parent.postMessage({ type: "timeEnd", label }, "*");
            return o.timeEnd(label);
        };

        console.clear = () => {
            parent.postMessage({ type: "clear" }, "*");
            return o.clear();
        };

        console.table = (data, columns) => {
            parent.postMessage({ type: "table", data: this._serialize(data), columns }, "*");
            return o.table(data, columns);
        };
    }

    /**
     * Sets up global error handlers for window.onerror and unhandled promise rejections.
     * Posts serialized error info to parent window.
     * @private
     */
    _setupGlobalErrorHandlers() {
        window.onerror = (message, source, lineno, colno) => {
            parent.postMessage({
                type: "error",
                args: [this._serialize(`${message} at ${source}:${lineno}:${colno}`)]
            }, "*");
        };

        window.addEventListener("unhandledrejection", event => {
            parent.postMessage({
                type: "error",
                args: [this._serialize(event.reason?.stack || event.reason || "Unhandled Promise Rejection")]
            }, "*");
        });
    }
}

const enhancedConsole = new EnhancedConsole();
enhancedConsole.init();
