/**
 * Ajoute à chaque bloc de code un en-tête (langage) et un bouton « Copier ».
 */
const LABELS = {
    js: "JavaScript", javascript: "JavaScript", ts: "TypeScript", typescript: "TypeScript",
    py: "Python", python: "Python", pycon: "Python", html: "HTML", css: "CSS", json: "JSON",
    php: "PHP", c: "C", cpp: "C++", sql: "SQL", yaml: "YAML", yml: "YAML", xml: "XML",
    bash: "Terminal", sh: "Terminal", shell: "Terminal", console: "Terminal", powershell: "PowerShell",
    django: "Django", jinja: "Jinja", diff: "Diff", md: "Markdown", markdown: "Markdown",
    text: "Texte", txt: "Texte", ini: "INI", toml: "TOML", scss: "SCSS", java: "Java",
};

const COPY_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg>';
const DONE_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5 9-10"/></svg>';

export class CodeBlockUtils {
    /** @param {HTMLElement} code élément <code> avec une classe « language-xxx » */
    static getLang(code) {
        const match = (code.className || "").match(/language-([\w+#-]+)/);
        if (!match) return "Texte";
        const lang = match[1].toLowerCase();
        return LABELS[lang] ?? lang.charAt(0).toUpperCase() + lang.slice(1);
    }

    static async copy(text) {
        try {
            await navigator.clipboard.writeText(text);
        } catch {
            const area = document.createElement("textarea");
            area.value = text;
            area.style.position = "fixed";
            area.style.opacity = "0";
            document.body.appendChild(area);
            area.select();
            document.execCommand("copy");
            area.remove();
        }
    }

    static initCodeBlockHeaders() {
        document.querySelectorAll(".markdown-body pre").forEach((pre) => {
            if (pre.closest(".code-block")) return;
            const code = pre.querySelector("code") ?? pre;

            let host = pre.parentElement;
            if (!host.classList.contains("codehilite")) {
                host = document.createElement("div");
                pre.replaceWith(host);
                host.appendChild(pre);
            }
            host.classList.add("code-block");

            const header = document.createElement("div");
            header.className = "code-header";
            const label = document.createElement("span");
            label.className = "code-lang";
            label.textContent = CodeBlockUtils.getLang(code);

            const button = document.createElement("button");
            button.type = "button";
            button.className = "copy-button";
            button.innerHTML = `${COPY_ICON}<span>Copier</span>`;
            button.addEventListener("click", async () => {
                await CodeBlockUtils.copy(host.runApi?.getValue() ?? code.textContent.replace(/\n$/, ""));
                button.classList.add("is-done");
                button.innerHTML = `${DONE_ICON}<span>Copié !</span>`;
                setTimeout(() => {
                    button.classList.remove("is-done");
                    button.innerHTML = `${COPY_ICON}<span>Copier</span>`;
                }, 1800);
            });

            const actions = document.createElement("div");
            actions.className = "code-actions";
            actions.append(button);
            header.append(label, actions);
            host.insertBefore(header, pre);
        });
    }
}
