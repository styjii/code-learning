import { normalize } from "../sections/SectionNav.js";

/**
 * Recherche plein texte dans le cours affiché (titres puis paragraphes).
 * Ouverture : bouton, « / » ou Ctrl/Cmd + K.
 */
const MAX_RESULTS = 40;

export class SearchDialog {
    constructor(sectionNav) {
        this.sectionNav = sectionNav;
        this.overlay = document.getElementById("search-overlay");
        this.input = document.getElementById("search-input");
        this.results = document.getElementById("search-results");
        this.hint = document.getElementById("search-hint");
        this.index = null;
        this.active = -1;
    }

    init() {
        if (!this.overlay || !this.sectionNav.panels.length) {
            document.getElementById("search-open")?.setAttribute("hidden", "");
            return;
        }

        document.getElementById("search-open").addEventListener("click", () => this.open());
        this.overlay.addEventListener("mousedown", (e) => { if (e.target === this.overlay) this.close(); });
        this.input.addEventListener("input", () => this.search(this.input.value));
        this.input.addEventListener("keydown", (e) => this.onKey(e));

        document.addEventListener("keydown", (e) => {
            const typing = /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName);
            if ((e.key === "k" && (e.ctrlKey || e.metaKey)) || (e.key === "/" && !typing)) {
                e.preventDefault();
                this.open();
            } else if (e.key === "Escape" && !this.overlay.hidden) {
                this.close();
            }
        });
    }

    buildIndex() {
        const entries = [];
        for (const panel of this.sectionNav.panels) {
            const section = panel.dataset.label;
            panel.querySelectorAll("h1, h2, h3, h4, p, li, td").forEach((el) => {
                if (el.closest("pre")) return;
                if (el.tagName === "LI" && el.querySelector("p, ul, ol")) return; // évite les doublons
                const text = el.textContent.replace(/#$/, "").replace(/\s+/g, " ").trim();
                if (text.length < 3) return;
                const heading = /^H\d$/.test(el.tagName);
                const target = heading ? el : this.nearestHeading(el) ?? panel;
                entries.push({ text, norm: normalize(text), section, id: target.id || panel.id, heading });
            });
        }
        return entries;
    }

    /** Titre h2-h4 le plus proche situé avant l'élément (pour y faire défiler). */
    nearestHeading(el) {
        let node = el;
        while (node && !node.classList?.contains("tab-content")) {
            let prev = node.previousElementSibling;
            while (prev) {
                if (/^H[2-4]$/.test(prev.tagName) && prev.id) return prev;
                prev = prev.previousElementSibling;
            }
            node = node.parentElement;
        }
        return null;
    }

    open() {
        this.index ??= this.buildIndex();
        this.overlay.hidden = false;
        document.body.classList.add("modal-open");
        this.input.value = "";
        this.search("");
        this.input.focus();
    }

    close() {
        this.overlay.hidden = true;
        document.body.classList.remove("modal-open");
    }

    search(raw) {
        const terms = normalize(raw.trim()).split(/\s+/).filter(Boolean);
        this.results.replaceChildren();
        this.active = -1;

        if (!terms.length || terms.join("").length < 2) {
            this.hint.textContent = "Tapez au moins 2 caractères · ↑ ↓ pour naviguer · Entrée pour ouvrir";
            return;
        }

        const matches = this.index.filter((e) => terms.every((t) => e.norm.includes(t)));
        matches.sort((a, b) => Number(b.heading) - Number(a.heading));
        const shown = matches.slice(0, MAX_RESULTS);

        this.hint.textContent = shown.length
            ? `${matches.length} résultat${matches.length > 1 ? "s" : ""}${matches.length > MAX_RESULTS ? ` (${MAX_RESULTS} affichés)` : ""}`
            : "Aucun résultat.";

        for (const entry of shown) {
            const li = document.createElement("li");
            const link = document.createElement("a");
            link.href = `#${entry.id}`;
            link.setAttribute("role", "option");
            link.dataset.id = entry.id;

            const path = document.createElement("span");
            path.className = "res-path";
            path.textContent = entry.section;
            const text = document.createElement("span");
            text.className = `res-text${entry.heading ? " is-heading" : ""}`;
            this.appendSnippet(text, entry, terms);

            link.append(path, text);
            link.addEventListener("click", (e) => { e.preventDefault(); this.go(entry.id); });
            li.appendChild(link);
            this.results.appendChild(li);
        }
    }

    /** Extrait centré sur la première occurrence, avec les termes surlignés. */
    appendSnippet(container, entry, terms) {
        const at = Math.max(0, entry.norm.indexOf(terms[0]));
        const start = Math.max(0, at - 50);
        const slice = entry.text.slice(start, start + 140);
        const normSlice = normalize(slice);
        const marks = [];
        terms.forEach((t) => {
            let i = normSlice.indexOf(t);
            while (i !== -1) { marks.push([i, i + t.length]); i = normSlice.indexOf(t, i + t.length); }
        });
        marks.sort((a, b) => a[0] - b[0]);

        if (start > 0) container.append("… ");
        let pos = 0;
        for (const [from, to] of marks) {
            if (from < pos) continue;
            container.append(slice.slice(pos, from));
            const mark = document.createElement("mark");
            mark.textContent = slice.slice(from, to);
            container.append(mark);
            pos = to;
        }
        container.append(slice.slice(pos));
        if (start + 140 < entry.text.length) container.append(" …");
    }

    onKey(event) {
        const links = Array.from(this.results.querySelectorAll("a"));
        if (!links.length) return;
        if (event.key === "ArrowDown" || event.key === "ArrowUp") {
            event.preventDefault();
            const step = event.key === "ArrowDown" ? 1 : -1;
            this.active = (this.active + step + links.length) % links.length;
            links.forEach((l, i) => l.classList.toggle("is-active", i === this.active));
            links[this.active].scrollIntoView({ block: "nearest" });
        } else if (event.key === "Enter") {
            event.preventDefault();
            this.go(links[Math.max(this.active, 0)].dataset.id);
        }
    }

    go(id) {
        this.close();
        this.sectionNav.goTo(`#${id}`, { push: true, scroll: true });
    }
}
