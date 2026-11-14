/**
 * Éditeur de démonstration du hero (modèle de l'éditeur web : index.html, style.css, script.ts).
 *  - le reflet lumineux suit le pointeur (--mx / --my, une mise à jour par image) ;
 *  - les onglets de fichiers suivent le motif ARIA « tabs » (flèches, Début, Fin) et mettent à jour la barre d'état ;
 *  - « Exécuter » relance l'aperçu et remet le compteur à zéro ; « Découvrir » incrémente le compteur, comme script.ts.
 * La lévitation et le halo au survol sont purement CSS (voir style.css).
 */
export class HeroEditor {
    static init() {
        const ide = document.querySelector("[data-ide]");
        if (!ide) return;

        HeroEditor.#trackPointer(ide);
        HeroEditor.#bindTabs(ide);
        HeroEditor.#bindPreview(ide);
    }

    static #trackPointer(ide) {
        if (!matchMedia("(hover: hover) and (pointer: fine)").matches) return;

        let frame = 0;
        ide.addEventListener("pointermove", (event) => {
            if (frame) return;
            frame = requestAnimationFrame(() => {
                frame = 0;
                const rect = ide.getBoundingClientRect();
                ide.style.setProperty("--mx", `${(((event.clientX - rect.left) / rect.width) * 100).toFixed(1)}%`);
                ide.style.setProperty("--my", `${(((event.clientY - rect.top) / rect.height) * 100).toFixed(1)}%`);
            });
        });
    }

    static #bindTabs(ide) {
        const tabs = [...ide.querySelectorAll('[role="tab"]')];
        const lang = ide.querySelector("[data-ide-lang]");
        const pos = ide.querySelector("[data-ide-pos]");
        const lines = ide.querySelector("[data-ide-lines]");
        if (!tabs.length) return;

        const select = (selected, { focus = false } = {}) => {
            for (const tab of tabs) {
                const on = tab === selected;
                const panel = document.getElementById(tab.getAttribute("aria-controls"));
                tab.setAttribute("aria-selected", String(on));
                tab.tabIndex = on ? 0 : -1;
                if (!panel) continue;
                panel.hidden = !on;
                if (!on) continue;

                panel.classList.remove("is-entering");
                void panel.offsetWidth; // relance l'animation d'entrée
                panel.classList.add("is-entering");
                if (lang) lang.textContent = panel.dataset.lang ?? "";
                if (pos) pos.textContent = panel.dataset.pos ?? "";
                if (lines) lines.textContent = `Lignes : ${panel.dataset.lines ?? ""}`;
            }
            if (focus) selected.focus();
        };

        tabs.forEach((tab) => tab.addEventListener("click", () => select(tab)));
        tabs.forEach((tab, index) => {
            tab.addEventListener("keydown", (event) => {
                const target = {
                    ArrowRight: tabs[(index + 1) % tabs.length],
                    ArrowLeft: tabs[(index - 1 + tabs.length) % tabs.length],
                    Home: tabs[0],
                    End: tabs[tabs.length - 1],
                }[event.key];
                if (!target) return;
                event.preventDefault();
                select(target, { focus: true });
            });
        });
    }

    static #bindPreview(ide) {
        const page = ide.querySelector("[data-ide-page]");
        const run = ide.querySelector("[data-ide-run]");
        const button = ide.querySelector("[data-ide-cta]");
        const label = ide.querySelector("[data-ide-count]");
        let clics = 0;

        const reset = () => {
            clics = 0;
            if (!label) return;
            label.hidden = true;
            label.textContent = "";
        };

        // Même logique que script.ts affiché dans l'éditeur.
        button?.addEventListener("click", () => {
            clics += 1;
            if (!label) return;
            label.hidden = false;
            label.textContent = `Clics : ${clics}`;
            label.classList.remove("is-pop");
            void label.offsetWidth;
            label.classList.add("is-pop");
        });

        run?.addEventListener("click", () => {
            reset();
            if (!page) return;
            page.classList.remove("is-running");
            void page.offsetWidth;
            page.classList.add("is-running");
        });
    }
}
