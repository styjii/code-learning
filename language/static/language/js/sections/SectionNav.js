/**
 * Navigation entre les sections d'un cours : barre latérale, hash d'URL,
 * liens internes du contenu, boutons précédent / suivant.
 */
const LEVEL_MARK = /^(?:[\u{1F7E0}-\u{1F7EB}]|\u{1F534})/u;
const NUMBERED = /^(\d+)\.\s+(.*)$/;

export const normalize = (text) =>
    text.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");

export class SectionNav {
    constructor() {
        this.panels = Array.from(document.querySelectorAll(".doc > .tab-content"));
        this.nav = document.getElementById("section-nav");
        this.items = [];
        this.current = -1;
        this.storageKey = `section:${document.body.dataset.lang}`;
    }

    init() {
        if (!this.panels.length) return;

        this.buildSidebar();
        this.bindFilter();
        this.bindContentLinks();
        window.addEventListener("popstate", () => this.goTo(location.hash, { push: false }));

        // Section de départ : hash > dernière visite > première section
        if (!this.goTo(location.hash, { push: false, scroll: true })) {
            let saved = -1;
            try { saved = Number(localStorage.getItem(this.storageKey)); } catch { /* ignoré */ }
            this.activate(saved >= 0 && saved < this.panels.length ? saved : 0);
        }
        document.getElementById("sidebar-foot").hidden = false;
    }

    /* ---------- Barre latérale ---------- */
    buildSidebar() {
        // La barre d'onglets générée côté serveur est remplacée par la navigation latérale.
        document.querySelector(".doc > .tab-bar")?.setAttribute("hidden", "");

        const frag = document.createDocumentFragment();
        this.panels.forEach((panel, index) => {
            const label = panel.dataset.label || panel.id;
            const link = document.createElement("a");
            link.href = `#${panel.id}`;
            link.className = "nav-item";
            link.dataset.index = index;
            link.dataset.search = normalize(label);

            const numbered = label.match(NUMBERED);
            if (LEVEL_MARK.test(label)) {
                link.classList.add("is-group");
                link.textContent = label;
            } else if (numbered) {
                const num = document.createElement("span");
                num.className = "nav-num";
                num.textContent = numbered[1];
                const text = document.createElement("span");
                text.textContent = numbered[2];
                link.append(num, text);
            } else {
                link.textContent = label;
            }

            link.addEventListener("click", (event) => {
                event.preventDefault();
                this.activate(index, { push: true });
                document.dispatchEvent(new CustomEvent("sidebar:close"));
            });
            this.items.push(link);
            frag.appendChild(link);
        });
        this.nav.appendChild(frag);
    }

    bindFilter() {
        const input = document.getElementById("section-filter");
        const empty = document.getElementById("nav-empty");
        input?.addEventListener("input", () => {
            const query = normalize(input.value.trim());
            let visible = 0;
            this.items.forEach((item) => {
                const match = item.dataset.search.includes(query);
                item.hidden = !match;
                if (match) visible++;
            });
            empty.hidden = visible > 0;
        });
    }

    /* ---------- Liens internes (sommaire, renvois) ---------- */
    bindContentLinks() {
        document.querySelector(".doc-main").addEventListener("click", (event) => {
            const link = event.target.closest('a[href^="#"]');
            if (!link || link.classList.contains("pager-link")) return;
            if (this.goTo(link.getAttribute("href"), { push: true, scroll: true })) {
                event.preventDefault();
            }
        });
    }

    /** Retrouve un élément par id, en tolérant les tirets multiples. */
    resolve(hash) {
        let id = hash.replace(/^#/, "");
        if (!id) return null;
        try { id = decodeURIComponent(id); } catch { /* id déjà décodé */ }

        const exact = document.getElementById(id);
        if (exact) return exact;

        const squash = (s) => s.replace(/-+/g, "-");
        return Array.from(document.querySelectorAll("[id]")).find((el) => squash(el.id) === squash(id)) ?? null;
    }

    /** Affiche la section contenant la cible puis y fait défiler. */
    goTo(hash, { push = true, scroll = true } = {}) {
        const target = this.resolve(hash);
        const panel = target?.closest(".tab-content");
        const index = this.panels.indexOf(panel);
        if (!target || index < 0) return false;

        const changed = index !== this.current;
        this.activate(index, { push: false });
        if (push && location.hash !== `#${target.id}`) {
            history.pushState(null, "", `#${target.id}`);
        }

        if (scroll) {
            requestAnimationFrame(() => {
                if (target === panel) {
                    if (changed) window.scrollTo(0, 0);
                } else {
                    target.scrollIntoView({ block: "start" });
                    target.classList.remove("flash");
                    void target.offsetWidth; // relance l'animation
                    target.classList.add("flash");
                }
            });
        }
        return true;
    }

    /* ---------- Activation d'une section ---------- */
    activate(index, { push = false } = {}) {
        if (index < 0 || index >= this.panels.length) return;
        const changed = index !== this.current;
        this.current = index;

        this.panels.forEach((panel, i) => {
            panel.hidden = i !== index;
            panel.classList.toggle("is-active", i === index);
        });
        this.items.forEach((item, i) => {
            item.classList.toggle("is-active", i === index);
            if (i === index) {
                item.setAttribute("aria-current", "true");
                item.scrollIntoView({ block: "nearest" });
            } else {
                item.removeAttribute("aria-current");
            }
        });

        const panel = this.panels[index];
        document.getElementById("section-count").textContent = `Section ${index + 1} sur ${this.panels.length}`;
        document.getElementById("section-bar").style.width = `${((index + 1) / this.panels.length) * 100}%`;
        this.renderPager(index);

        try { localStorage.setItem(this.storageKey, String(index)); } catch { /* ignoré */ }

        if (changed) {
            if (push) {
                history.pushState(null, "", `#${panel.id}`);
                window.scrollTo(0, 0);
            }
            document.dispatchEvent(new CustomEvent("section:change", { detail: { panel } }));
        }
    }

    renderPager(index) {
        const pager = document.getElementById("pager");
        if (!pager) return;
        pager.replaceChildren();

        const make = (target, direction) => {
            if (!target) return;
            const link = document.createElement("a");
            link.className = `pager-link ${direction}`;
            link.href = `#${target.id}`;
            const hint = document.createElement("span");
            hint.className = "pager-hint";
            hint.textContent = direction === "prev" ? "← Précédent" : "Suivant →";
            const title = document.createElement("span");
            title.className = "pager-title";
            title.textContent = target.dataset.label;
            link.append(hint, title);
            link.addEventListener("click", (event) => {
                event.preventDefault();
                this.activate(this.panels.indexOf(target), { push: true });
            });
            pager.appendChild(link);
        };
        make(this.panels[index - 1], "prev");
        make(this.panels[index + 1], "next");
    }
}
