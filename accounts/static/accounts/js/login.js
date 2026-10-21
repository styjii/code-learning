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
