/**
 * Utilitaires de texte pour la console façon Chrome DevTools (aucune dépendance DOM).
 */

/** Identifiant JavaScript valide : affiché sans guillemets comme clé d'objet. */
export const IDENTIFIER = /^[A-Za-z_$][\w$]*$/;

/**
 * Met une chaîne entre guillemets comme DevTools : apostrophes par défaut, guillemets doubles si la
 * chaîne contient une apostrophe, accent grave si elle contient les deux.
 */
export function quoteString(text) {
    let quote = "'";
    if (text.includes("'")) {
        if (!text.includes('"')) quote = '"';
        else if (!text.includes("`")) quote = "`";
    }
    const escaped = text
        .replace(/\\/g, "\\\\")
        .replace(/\n/g, "\\n")
        .replace(/\r/g, "\\r")
        .replace(/\t/g, "\\t");
    return quote + (quote === "'" ? escaped.replace(/'/g, "\\'") : escaped) + quote;
}

/** Tronque un texte et ajoute « … » (compté en caractères, pas en octets). */
export function truncate(text, max) {
    return text.length > max ? `${text.slice(0, max)}…` : text;
}

/** Éléments HTML sans balise fermante. */
export const VOID_ELEMENTS = new Set([
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr",
]);

/** Texte court d'un nœud DOM imbriqué dans un objet : « div#app.box.large ». */
export function elementLabel(node) {
    if (node.nt !== 1) return node.tag || "#node";
    const attrs = Object.fromEntries(node.attrs || []);
    let label = node.tag;
    if (attrs.id) label += `#${attrs.id}`;
    if (attrs.class) label += attrs.class.trim().split(/\s+/).map((c) => `.${c}`).join("");
    return label;
}

/**
 * Styles autorisés pour « %c » : seulement de la décoration de texte, jamais de positionnement ni
 * d'URL (pas de fuite de données ni de superposition à l'interface).
 */
const SAFE_CSS = new Set([
    "color", "background", "background-color", "font-weight", "font-style", "font-size", "font-family",
    "text-decoration", "text-shadow", "padding", "padding-left", "padding-right", "padding-top", "padding-bottom",
    "border", "border-radius", "letter-spacing", "line-height", "text-transform",
]);

export function sanitizeCss(css) {
    return String(css)
        .split(";")
        .map((declaration) => {
            const colon = declaration.indexOf(":");
            return colon < 0 ? null : [declaration.slice(0, colon).trim().toLowerCase(), declaration.slice(colon + 1).trim()];
        })
        .filter((entry) => entry && SAFE_CSS.has(entry[0])
            && !/url\s*\(|expression|@import|javascript:/i.test(entry[1])
            && !(entry[0] === "font-size" && parseFloat(entry[1]) > 40))
        .map(([name, value]) => `${name}:${value}`)
        .join(";");
}
