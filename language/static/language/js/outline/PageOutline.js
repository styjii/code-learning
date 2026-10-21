/**
 * Plan de la section affichée (colonne « Sur cette page ») avec suivi du défilement.
 */
export class PageOutline {
    constructor() {
        this.toc = document.getElementById("toc");
        this.list = document.getElementById("toc-list");
        this.observer = null;
        this.links = new Map();
    }

    init() {
        if (!this.toc) return;
        document.addEventListener("section:change", (event) => this.build(event.detail.panel));
    }

    build(panel) {
        this.observer?.disconnect();
        this.links.clear();
        this.list.replaceChildren();

        const headings = Array.from(panel.querySelectorAll("h2:not(.section-title), h3:not(.section-title)"))
            .filter((h) => h.id)
            .slice(0, 60);
        this.toc.hidden = headings.length < 2;
        if (this.toc.hidden) return;

        for (const heading of headings) {
            const item = document.createElement("li");
            item.className = `toc-${heading.tagName.toLowerCase()}`;
            const link = document.createElement("a");
            link.href = `#${heading.id}`;
            link.textContent = heading.textContent.replace(/#$/, "").trim();
            item.appendChild(link);
            this.list.appendChild(item);
            this.links.set(heading, link);
        }

        const visible = new Set();
        this.observer = new IntersectionObserver((entries) => {
            for (const entry of entries) {
                entry.isIntersecting ? visible.add(entry.target) : visible.delete(entry.target);
            }
            const first = headings.find((h) => visible.has(h));
            if (first) this.highlight(first);
        }, { rootMargin: "-72px 0px -70% 0px" });
        headings.forEach((h) => this.observer.observe(h));
    }

    highlight(heading) {
        this.links.forEach((link, h) => {
            link.classList.toggle("is-active", h === heading);
            if (h === heading) link.scrollIntoView({ block: "nearest" });
        });
    }
}
