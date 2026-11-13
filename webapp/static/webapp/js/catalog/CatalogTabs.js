/**
 * Catalogue de cours : onglets de catégories (ARIA « tabs »), recherche transversale et ouverture d'un onglet
 * depuis le menu ou le pied de page (liens [data-open-tab]).
 *
 * - Changer d'onglet rejoue un fondu + glissement vers le haut, en cascade sur les cartes (classe .is-entering).
 * - La recherche (barre du haut, Ctrl/Cmd + K) filtre toutes les catégories à la fois ; vider le champ rétablit l'onglet.
 */
const normalize = (text) => text.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");

export class CatalogTabs {
    static init() {
        const root = document.getElementById("courses");
        const input = document.getElementById("course-search");
        if (!root) return;

        const tabs = Array.from(root.querySelectorAll('[role="tab"]'));
        const panels = Array.from(root.querySelectorAll('[role="tabpanel"]'));
        const empty = document.getElementById("no-results");
        const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)");
        if (!panels.length) return;

        let current = panels[0].dataset.panel;
        let searching = false;

        const enter = (panel) => {
            if (reduceMotion.matches) return;
            panel.classList.remove("is-entering");
            void panel.offsetWidth; // relance l'animation
            panel.classList.add("is-entering");
        };

        const select = (name, { animate = true } = {}) => {
            current = name;
            searching = false;
            root.classList.remove("is-searching");
            tabs.forEach((tab) => {
                const on = tab.dataset.tab === name;
                tab.classList.toggle("is-active", on);
                tab.setAttribute("aria-selected", String(on));
                tab.tabIndex = on ? 0 : -1;
            });
            // Panneau sans onglet (Exercices, Projets) : aucun onglet actif, le premier reste atteignable au clavier.
            if (!tabs.some((tab) => tab.dataset.tab === name) && tabs[0]) tabs[0].tabIndex = 0;
            panels.forEach((panel) => {
                const on = panel.dataset.panel === name;
                panel.hidden = !on;
                panel.querySelectorAll(".lang-card, .panel-group").forEach((node) => { node.hidden = false; });
                if (on && animate) enter(panel);
            });
            if (empty) empty.hidden = true;
            tabs.find((tab) => tab.dataset.tab === name)?.scrollIntoView({ block: "nearest", inline: "nearest" });
        };

        const search = () => {
            const query = normalize(input.value.trim());
            if (!query) {
                if (searching) select(current, { animate: true });
                return;
            }
            searching = true;
            root.classList.add("is-searching");
            tabs.forEach((tab) => { tab.classList.remove("is-active"); tab.setAttribute("aria-selected", "false"); });
            let total = 0;
            panels.forEach((panel) => {
                let visiblePanel = 0;
                panel.querySelectorAll(".panel-group").forEach((group) => {
                    let visible = 0;
                    group.querySelectorAll(".lang-card").forEach((card) => {
                        const match = normalize(card.dataset.search).includes(query);
                        card.hidden = !match;
                        if (match) visible++;
                    });
                    group.hidden = visible === 0;
                    visiblePanel += visible;
                });
                panel.hidden = visiblePanel === 0;
                total += visiblePanel;
            });
            if (empty) empty.hidden = total > 0;
        };

        tabs.forEach((tab, index) => {
            tab.addEventListener("click", () => {
                if (input) input.value = "";
                select(tab.dataset.tab);
            });
            tab.addEventListener("keydown", (event) => {
                const last = tabs.length - 1;
                const next = { ArrowRight: index === last ? 0 : index + 1, ArrowLeft: index === 0 ? last : index - 1, Home: 0, End: last }[event.key];
                if (next === undefined) return;
                event.preventDefault();
                if (input) input.value = "";
                select(tabs[next].dataset.tab);
                tabs[next].focus();
            });
        });

        // Liens du menu / du pied de page : ouvrent l'onglet puis font défiler jusqu'au catalogue.
        document.querySelectorAll("[data-open-tab]").forEach((link) => {
            link.addEventListener("click", (event) => {
                const name = link.dataset.openTab;
                if (!panels.some((panel) => panel.dataset.panel === name)) return;
                event.preventDefault();
                if (input) input.value = "";
                select(name);
                root.scrollIntoView({ behavior: reduceMotion.matches ? "auto" : "smooth", block: "start" });
                history.replaceState(null, "", "#courses");
            });
        });

        if (input) {
            let scrolled = false;
            input.addEventListener("input", () => {
                search();
                if (input.value.trim() && !scrolled) {
                    scrolled = true;
                    root.scrollIntoView({ behavior: reduceMotion.matches ? "auto" : "smooth", block: "start" });
                }
                if (!input.value.trim()) scrolled = false;
            });
            input.addEventListener("keydown", (event) => {
                if (event.key === "Escape") { input.value = ""; search(); input.blur(); }
            });
            document.addEventListener("keydown", (event) => {
                const typing = /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName ?? "");
                if ((event.key.toLowerCase() === "k" && (event.ctrlKey || event.metaKey)) || (event.key === "/" && !typing)) {
                    event.preventDefault();
                    // Sur mobile la recherche est dans le menu burger : on l'ouvre d'abord.
                    const burger = document.getElementById("nav-burger");
                    if (burger?.getAttribute("aria-expanded") === "false" && matchMedia("(max-width: 1099px)").matches) burger.click();
                    input.focus();
                    input.select();
                }
            });
        }
    }
}
