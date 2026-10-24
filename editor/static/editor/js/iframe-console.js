/**
 * Exécuté dans l'iframe d'aperçu, avant le code de l'utilisateur : branche la console de la page sur
 * celle de l'éditeur. La sérialisation et les méthodes de console viennent de console-runtime.js.
 */
(function () {
    const post = (message) => parent.postMessage(message, "*");

    // mirror : on garde aussi la console native (outils de développement du navigateur).
    ConsoleRuntime.install(console, post, { mirror: true });

    window.onerror = (message, source, line, column, error) => {
        post(ConsoleRuntime.errorMessage(error || `${message} (${source}:${line}:${column})`));
        return true;
    };

    window.addEventListener("unhandledrejection", (event) => {
        post(ConsoleRuntime.errorMessage(event.reason === undefined ? "Unhandled Promise Rejection" : event.reason, { inPromise: true }));
    });
})();
