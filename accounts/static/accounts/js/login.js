/** Bouton « Afficher / Masquer » du mot de passe. */
document.querySelector(".toggle-password")?.addEventListener("click", (event) => {
    const button = event.currentTarget;
    const input = document.querySelector('input[name="password"]');
    const show = input.type === "password";
    input.type = show ? "text" : "password";
    button.textContent = show ? "Masquer" : "Afficher";
    button.setAttribute("aria-pressed", String(show));
    button.setAttribute("aria-label", show ? "Masquer le mot de passe" : "Afficher le mot de passe");
});

/**
 * Validation du formulaire de connexion.
 *
 * - Un champ vide empêche l'envoi et affiche un message explicite sous le champ.
 * - Aucune règle de longueur n'est vérifiée ici : seul le caractère « vide » compte.
 * - Quand la limite de tentatives est atteinte, le bouton est désactivé jusqu'à la fin du blocage.
 *   Le serveur reste l'autorité (réponse 429) ; ceci n'est qu'un retour visuel.
 */
const form = document.getElementById("login-form");

if (form) {
    const submit = document.getElementById("login-submit");
    const hint = document.getElementById("lock-hint");
    const STORAGE_KEY = "login-lock";

    const fields = [
        { input: form.elements.username, error: document.getElementById("username-error"), trim: true },
        { input: form.elements.password, error: document.getElementById("password-error"), trim: false },
    ];

    // --- champs vides ---------------------------------------------------
    const isEmpty = ({ input, trim }) => (trim ? input.value.trim() : input.value) === "";

    const showError = (field) => {
        field.error.textContent = field.error.dataset.requiredMessage;
        field.error.hidden = false;
        field.input.setAttribute("aria-invalid", "true");
        field.input.setAttribute("aria-describedby", field.error.id);
    };

    const clearError = (field) => {
        field.error.textContent = "";
        field.error.hidden = true;
        field.input.removeAttribute("aria-invalid");
        field.input.removeAttribute("aria-describedby");
    };

    fields.forEach((field) => {
        field.input.addEventListener("input", () => clearError(field));
    });

    // --- blocage par tentatives ----------------------------------------
    let lockUntil = 0;
    let timer = null;

    const usernameKey = () => fields[0].input.value.trim().normalize("NFKC").toLowerCase();

    const readStored = () => {
        try {
            return JSON.parse(localStorage.getItem(STORAGE_KEY) || "null");
        } catch {
            return null;
        }
    };

    const writeStored = (value) => {
        try {
            if (value) localStorage.setItem(STORAGE_KEY, JSON.stringify(value));
            else localStorage.removeItem(STORAGE_KEY);
        } catch {
            /* stockage indisponible : le serveur applique de toute façon le blocage */
        }
    };

    const formatRemaining = (ms) => {
        const total = Math.max(0, Math.ceil(ms / 1000));
        const minutes = String(Math.floor(total / 60)).padStart(2, "0");
        const seconds = String(total % 60).padStart(2, "0");
        return `${minutes}:${seconds}`;
    };

    // Retire l'état bloqué de l'interface (sans oublier le blocage mémorisé).
    const release = () => {
        clearInterval(timer);
        timer = null;
        lockUntil = 0;
        submit.disabled = false;
        submit.removeAttribute("aria-disabled");
        hint.hidden = true;
        hint.textContent = "";
    };

    // Fin du blocage : on réactive le bouton et on oublie le blocage.
    const unlock = () => {
        release();
        writeStored(null);
    };

    const tick = () => {
        const remaining = lockUntil - Date.now();
        if (remaining <= 0) return unlock();
        hint.textContent = `Connexion indisponible. Réessayez dans ${formatRemaining(remaining)}.`;
    };

    const lock = (until) => {
        lockUntil = until;
        submit.disabled = true;
        submit.setAttribute("aria-disabled", "true");
        hint.hidden = false;
        tick();
        clearInterval(timer);
        timer = setInterval(tick, 1000);
    };

    // Le blocage vaut pour un identifiant donné : on le réapplique si l'utilisateur
    // revient sur la page ou saisit de nouveau cet identifiant.
    const restoreLock = () => {
        const stored = readStored();
        if (!stored || stored.until <= Date.now()) {
            if (stored) writeStored(null);
            return;
        }
        if (stored.user === usernameKey()) {
            if (stored.until !== lockUntil) lock(stored.until);
        } else if (lockUntil) {
            release();
        }
    };

    const serverSeconds = Number(form.dataset.lockSeconds) || 0;
    if (serverSeconds > 0) {
        const until = Date.now() + serverSeconds * 1000;
        writeStored({ user: usernameKey(), until });
        lock(until);
    } else {
        restoreLock();
    }

    fields[0].input.addEventListener("input", () => {
        restoreLock();
    });

    // --- soumission -----------------------------------------------------
    form.addEventListener("submit", (event) => {
        if (lockUntil > Date.now()) {
            event.preventDefault();
            return;
        }

        const invalid = fields.filter(isEmpty);
        fields.forEach((field) => (invalid.includes(field) ? showError(field) : clearError(field)));

        if (invalid.length) {
            event.preventDefault();
            invalid[0].input.focus();
        }
    });
}
