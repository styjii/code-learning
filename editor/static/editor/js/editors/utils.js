/**
 * Forces all 'touchstart' and 'touchmove' event listeners to be passive by default,
 * to avoid scroll-blocking warnings in Chrome.
 */
export function patchPassiveTouchStart() {
    const originalAddEventListener = EventTarget.prototype.addEventListener;

    EventTarget.prototype.addEventListener = function (type, listener, options) {
        if (type === "touchstart" || type === "touchmove") {
            if (options === undefined) {
                options = { passive: true };
            } else if (typeof options === "boolean") {
                options = { capture: options, passive: true };
            } else if (typeof options === "object" && options.passive !== false) {
                options = { ...options, passive: true };
            }
        }
        return originalAddEventListener.call(this, type, listener, options);
    };
}
