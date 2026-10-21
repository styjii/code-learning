<div align="center">

# 🎨 CSS — Guide complet

**Des sélecteurs à Flexbox, Grid, aux conteneurs, aux animations et au CSS moderne**

*Mis à jour pour le CSS de 2026 (octobre 2026)*

</div>

---

## 🗂️ Sommaire

**🟢 Fondamentaux**

1. [Introduction à CSS](#1-introduction-à-css)
2. [Syntaxe et sélecteurs](#2-syntaxe-et-sélecteurs)
3. [Ajouter du CSS à une page](#3-ajouter-du-css-à-une-page)
4. [Cascade, spécificité et héritage](#4-cascade-spécificité-et-héritage)
5. [Couleurs et unités](#5-couleurs-et-unités)
6. [Le modèle de boîte](#6-le-modèle-de-boîte)
7. [Texte et polices](#7-texte-et-polices)

**🟡 Mise en page**

8. [Affichage, positionnement et débordement](#8-affichage-positionnement-et-débordement)
9. [Flexbox](#9-flexbox)
10. [CSS Grid](#10-css-grid)
11. [Arrière-plans, bordures, ombres et effets](#11-arrière-plans-bordures-ombres-et-effets)

**🔴 CSS dynamique et moderne**

12. [Variables CSS (propriétés personnalisées)](#12-variables-css-propriétés-personnalisées)
13. [Transitions, animations et transformations](#13-transitions-animations-et-transformations)
14. [Design responsive](#14-design-responsive)
15. [Fonctionnalités modernes : imbrication, `:has()`, couches, `@scope`, ancrage…](#15-fonctionnalités-modernes)
16. [Accessibilité et CSS](#16-accessibilité-et-css)

**🛠️ Outils et pratique**

17. [Frameworks CSS](#17-frameworks-css)
18. [Préprocesseurs et outils de build](#18-préprocesseurs-et-outils-de-build)
19. [Organiser son CSS](#19-organiser-son-css)
20. [Performances et optimisation](#20-performances-et-optimisation)
21. [Compatibilité entre navigateurs](#21-compatibilité-entre-navigateurs)
22. [CSS et JavaScript](#22-css-et-javascript)
23. [Outils de développement](#23-outils-de-développement)
24. [Composants et projets](#24-composants-et-projets)
25. [Aide-mémoire et ressources](#25-aide-mémoire-et-ressources)

> 💡 **Légende** : *(ajout)* = notion absente du guide d'origine ; *(à jour)* = pratique moderne remplaçant une ancienne ; *(héritage)* = technique ancienne, encore rencontrée.
>
> 📌 **À propos du support des navigateurs** : l'état de disponibilité des fonctionnalités récentes évolue vite. Les mentions « **Baseline** » (*newly available* = disponible dans les dernières versions de tous les navigateurs majeurs ; *widely available* = disponible depuis ≥ 30 mois) sont données à titre indicatif : **vérifiez toujours sur [MDN](https://developer.mozilla.org) ou [caniuse.com](https://caniuse.com)** avant d'utiliser une fonctionnalité sans solution de repli.

---

# 🟢 Fondamentaux

---

# 1. Introduction à CSS

## 1.1 Qu'est-ce que CSS ?

**CSS** (*Cascading Style Sheets*, « feuilles de style en cascade ») est le langage qui décrit la **présentation** d'un document HTML : couleurs, polices, espacements, mise en page, animations, adaptation aux écrans.

| Langage | Rôle |
| --- | --- |
| **HTML** | **Structure et contenu** (titres, paragraphes, liens) |
| **CSS** | **Présentation** (apparence, mise en page) |
| **JavaScript** | **Comportement** (interactions, logique) |

**Pourquoi CSS ?**

- **Sépare** le contenu du design : un seul fichier CSS peut styliser tout un site.
- **Maintenance facilitée** : on change un style à un seul endroit.
- **Responsive** : une même page s'adapte au mobile, à la tablette, au bureau.
- **Accessibilité et préférences** : mode sombre, mouvement réduit, contraste élevé.
- **Performance** : le CSS est mis en cache et décodé efficacement par le navigateur.

## 1.2 Comment le navigateur applique le CSS

```text
HTML ──▶ DOM ─┐
              ├─▶ Arbre de rendu ──▶ Mise en page (layout) ──▶ Peinture ──▶ Composition ──▶ Écran
CSS  ──▶ CSSOM ┘
```

1. Le navigateur construit le **DOM** (à partir du HTML) et le **CSSOM** (à partir du CSS).
2. Il les combine : pour chaque élément, la **cascade** détermine les valeurs finales.
3. Il calcule la **mise en page** (tailles, positions), **peint** les pixels, puis **compose** les couches.

## 1.3 Un premier exemple

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Ma première page</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Bonjour CSS !</h1>
    <p class="intro">Ceci est un paragraphe stylisé.</p>
</body>
</html>
```

```css
/* style.css */
body {
    font-family: system-ui, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 2rem;
}

h1 { color: rebeccapurple; }

.intro {
    font-size: 1.25rem;
    color: #444;
}
```

## 1.4 Les « niveaux » de CSS

Il n'y a plus de « CSS4 » : CSS est découpé en **modules** indépendants (Sélecteurs niveau 4, Couleurs niveau 5, Grid niveau 2, Imbrication, Conteneurs, etc.) qui évoluent séparément au sein du **W3C (CSS Working Group)**. On parle simplement de « **CSS moderne** » ou de **CSS 2026**.

---

# 2. Syntaxe et sélecteurs

## 2.1 Anatomie d'une règle

```css
sélecteur {
    propriété: valeur;
    autre-propriété: valeur;
}
```

```css
h1 {
    color: blue;           /* propriété : valeur ; */
    font-size: 2rem;
}
```

| Élément | Rôle |
| --- | --- |
| **Sélecteur** | Désigne les éléments HTML à styliser |
| **Déclaration** | Une paire `propriété: valeur;` |
| **Bloc** | Les déclarations entre `{ }` |
| **Règle @** | Instruction spéciale : `@media`, `@font-face`, `@layer`, `@keyframes`, `@supports`, `@container`… |

Les espaces et sauts de ligne sont libres. Les noms de propriétés et de valeurs sont **insensibles à la casse**, mais les **noms de classes, d'identifiants** (et les valeurs d'attributs) sont **sensibles à la casse** dans le HTML.

## 2.2 Commentaires

```css
/* Commentaire sur une ligne */

/*
   Commentaire
   sur plusieurs lignes
*/
```

> Il n'existe pas de commentaire `//` en CSS pur (il est disponible en Sass/SCSS).

## 2.3 Sélecteurs de base

| Sélecteur | Syntaxe | Cible |
| --- | --- | --- |
| **Universel** | `*` | Tous les éléments |
| **Type (balise)** | `p`, `h1`, `a` | Tous les éléments de ce type |
| **Classe** | `.carte` | Éléments avec `class="carte"` |
| **Identifiant** | `#entete` | L'élément avec `id="entete"` (unique dans la page) |

```css
* { box-sizing: border-box; }
p { margin-block: 1em; }
.alerte { color: crimson; }
#menu-principal { display: flex; }
button.primaire { background: royalblue; }     /* <button class="primaire"> uniquement */
.carte.mise-en-avant { border-color: gold; }   /* élément avec les DEUX classes */
```

> ✅ Préférez les **classes** aux identifiants pour le style (réutilisables, spécificité plus basse).

## 2.4 Regrouper et combiner

```css
h1, h2, h3 { font-family: Georgia, serif; }      /* liste : mêmes styles pour plusieurs sélecteurs */
```

| Combinateur | Syntaxe | Cible |
| --- | --- | --- |
| **Descendant** | `article p` | Tout `<p>` **dans** `<article>` (à tout niveau) |
| **Enfant direct** | `ul > li` | `<li>` **enfants directs** de `<ul>` |
| **Frère adjacent** | `h2 + p` | Le `<p>` **immédiatement après** un `<h2>` |
| **Frères suivants** | `h2 ~ p` | **Tous** les `<p>` frères **après** un `<h2>` |

```css
nav ul { list-style: none; }
.menu > li { display: inline-block; }
h2 + p { font-weight: bold; }
h2 ~ p { color: gray; }
```

## 2.5 Sélecteurs d'attribut

```css
a[target] { }                            /* possède l'attribut */
a[target="_blank"] { }                   /* valeur exacte */
a[href^="https"] { }                     /* commence par */
a[href$=".pdf"] { }                      /* se termine par */
a[href*="exemple"] { }                   /* contient */
[class~="alerte"] { }                    /* contient le mot (séparé par des espaces) */
[lang|="fr"] { }                         /* « fr » ou « fr-… » */
input[type="email" i] { }                /* insensible à la casse (drapeau i) */
```

## 2.6 Pseudo-classes

Une **pseudo-classe** cible un **état** ou une **position** (`:` simple).

| Catégorie | Pseudo-classes |
| --- | --- |
| **Interaction** | `:hover`, `:active`, `:focus`, **`:focus-visible`** ✅, `:focus-within`, `:target` |
| **Liens** | `:link`, `:visited` (propriétés limitées pour la vie privée), `:any-link` |
| **Formulaires** | `:checked`, `:disabled`, `:enabled`, `:required`, `:optional`, `:placeholder-shown`, `:read-only`, `:valid`, `:invalid`, **`:user-valid` / `:user-invalid`** ✅ (après interaction), `:in-range`, `:out-of-range`, `:indeterminate` |
| **Position** | `:first-child`, `:last-child`, `:only-child`, `:nth-child(…)`, `:nth-last-child(…)`, `:first-of-type`, `:last-of-type`, `:nth-of-type(…)` |
| **Structure** | `:root`, `:empty`, `:defined` |
| **Fonctionnelles** | **`:not()`**, **`:is()`**, **`:where()`**, **`:has()`** ✅ |
| **Autres** | `:dir()`, `:lang()`, `:modal`, `:popover-open`, `:fullscreen` |

```css
a:hover { color: red; }
button:focus-visible { outline: 3px solid royalblue; outline-offset: 2px; }   /* focus clavier uniquement */
li:nth-child(odd) { background: #eee; }          /* impairs */
li:nth-child(3n + 1) { }                         /* 1, 4, 7… */
li:nth-child(-n + 3) { }                         /* les 3 premiers */
li:last-child { border-bottom: 0; }
input:checked + label { font-weight: 700; }
input:user-invalid { border-color: crimson; }    /* invalide ET déjà modifié par l'utilisateur */
```

### Les pseudo-classes fonctionnelles modernes

```css
/* :is() — regroupe, SANS répéter les sélecteurs */
:is(h1, h2, h3):hover { color: tomato; }
:is(article, section) :is(h2, h3) { margin-block: 1em; }

/* :where() — comme :is() mais spécificité ZÉRO (idéal pour les styles de base) */
:where(ul, ol) { padding-inline-start: 1.5rem; }

/* :not() — exclut ; accepte une liste */
a:not([class]) { text-decoration: underline; }
li:not(:last-child) { margin-bottom: .5rem; }

/* :has() — « sélecteur parent » : l'élément qui CONTIENT… */
.carte:has(img) { display: grid; }                          /* carte contenant une image */
label:has(input:checked) { background: #e8f0ff; }           /* sélectionne le <label> parent */
form:has(:user-invalid) .envoyer { opacity: .5; }
h2:has(+ p) { margin-bottom: .25em; }                       /* titre suivi d'un paragraphe */
```

> ✅ **`:has()`** est disponible dans tous les navigateurs modernes depuis fin 2023 (Baseline *widely available*). Il évite de nombreux scripts.

## 2.7 Pseudo-éléments

Un **pseudo-élément** cible une **partie** d'un élément (`::` double deux-points).

| Pseudo-élément | Cible |
| --- | --- |
| `::before`, `::after` | Contenu **généré** (nécessite `content`) |
| `::first-line`, `::first-letter` | Première ligne / lettre |
| `::selection` | Texte sélectionné |
| `::placeholder` | Texte d'indication d'un champ |
| `::marker` | Puce ou numéro d'une liste |
| `::backdrop` | Arrière-plan d'un `<dialog>` modal / élément plein écran / popover |
| `::file-selector-button` | Bouton d'un `<input type="file">` |
| `::cue`, `::part()`, `::slotted()` | Sous-titres / composants web (Shadow DOM) |
| `::details-content` | Contenu d'un `<details>` |
| `::view-transition-*` | Transitions de vue (section 13) |

```css
p::first-letter { font-size: 2em; float: left; }
a[href^="http"]::after { content: " ↗"; }
.note::before { content: "Note : "; font-weight: bold; }
::selection { background: gold; color: black; }
input::placeholder { color: #999; }
li::marker { color: tomato; }
dialog::backdrop { background: rgb(0 0 0 / .5); }
```

## 2.8 Imbrication native *(à jour)*

Le CSS accepte désormais l'**imbrication** de règles, **sans préprocesseur** (disponible dans tous les navigateurs modernes depuis 2023) :

```css
.carte {
    padding: 1rem;
    border: 1px solid #ddd;

    h2 { font-size: 1.25rem; }                 /* .carte h2 */
    &:hover { box-shadow: 0 2px 8px rgb(0 0 0 / .15); }   /* .carte:hover */
    &.active { border-color: royalblue; }      /* .carte.active */
    .titre & { color: red; }                   /* .titre .carte */

    @media (min-width: 48rem) {                /* règles @ imbriquées */
        padding: 2rem;
    }
}
```

## 2.9 Bonnes pratiques

- Sélecteurs **simples et peu profonds** (≤ 3 niveaux) : plus lisibles et plus faciles à surcharger.
- Évitez de styliser avec des **identifiants** et `!important`.
- Utilisez des **classes sémantiques** (`.carte-produit`) plutôt que présentatives (`.rouge-gras`).

---

# 3. Ajouter du CSS à une page

## 3.1 Les trois méthodes

| Méthode | Où | Quand |
| --- | --- | --- |
| **Externe** ✅ | Fichier `.css` lié avec `<link>` | **Presque toujours** : mise en cache, réutilisation |
| **Interne** | Balise `<style>` dans le `<head>` | Page unique, **CSS critique** en ligne, démos |
| **En ligne** (*inline*) | Attribut `style="…"` | Valeurs **dynamiques** (JS), e-mails HTML ; à éviter sinon |

```html
<!-- 1. Externe -->
<link rel="stylesheet" href="css/style.css">
<link rel="stylesheet" href="print.css" media="print">                 <!-- seulement à l'impression -->
<link rel="stylesheet" href="grand-ecran.css" media="(min-width: 64rem)">

<!-- 2. Interne -->
<style>
    body { font-family: system-ui, sans-serif; }
</style>

<!-- 3. En ligne -->
<p style="color: blue; font-weight: bold;">Paragraphe bleu</p>
<div style="--progression: 70%;">…</div>                                   <!-- injecter une variable CSS -->
```

### Comparaison

| | Externe | Interne | En ligne |
| --- | --- | --- | --- |
| Réutilisable entre pages | ✅ | ❌ | ❌ |
| Mis en cache | ✅ | ❌ | ❌ |
| Priorité (spécificité) | Normale | Normale | **Très haute** |
| Maintenance | ✅ | Moyenne | ❌ |
| Compatible avec une CSP stricte | ✅ | Nécessite un `nonce` | Nécessite `'unsafe-inline'` (déconseillé) |

## 3.2 L'ordre compte

Si deux règles ont la **même spécificité**, **la dernière** l'emporte. L'ordre des fichiers et des balises `<link>` / `<style>` est donc important.

## 3.3 `@import` (à éviter)

```css
@import url("autre.css");                 /* ❌ bloque le chargement en série */
@import url("theme.css") layer(theme);    /* possible avec une couche */
```

> ⚠️ `@import` force le navigateur à télécharger les fichiers **les uns après les autres** : préférez plusieurs `<link>` (chargés en parallèle) ou un outil de **build** qui regroupe le CSS (section 18).

## 3.4 Charger le CSS efficacement

```html
<link rel="preload" href="/polices/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="critique.css">
<link rel="stylesheet" href="reste.css" media="print" onload="this.media='all'">    <!-- chargement différé (CSS non critique) -->
```

Le CSS est **bloquant pour le rendu** (le navigateur attend le CSS avant d'afficher) : gardez-le **léger**.

---

# 4. Cascade, spécificité et héritage

## 4.1 Pourquoi « en cascade » ?

Plusieurs règles peuvent viser **le même élément et la même propriété** : la **cascade** détermine laquelle gagne. Les critères, dans l'ordre :

| # | Critère | Explication |
| --- | --- | --- |
| 1 | **Origine et importance** | Navigateur < auteur < utilisateur ; `!important` **inverse** l'ordre |
| 2 | **Contexte et couches** (`@layer`) | Une couche **déclarée plus tard** l'emporte (hors `!important`) |
| 3 | **Spécificité** | Le sélecteur le plus spécifique gagne |
| 4 | **Ordre d'apparition** | À égalité, la **dernière** règle l'emporte |

## 4.2 La spécificité *(à jour : calcul correct)*

La spécificité s'exprime comme **trois colonnes (A, B, C)**, comparées **de gauche à droite** (et non comme un nombre décimal) :

| Colonne | Compte… | Exemples |
| --- | --- | --- |
| **A** | Sélecteurs d'**identifiant** | `#menu` |
| **B** | Sélecteurs de **classe**, d'**attribut**, **pseudo-classes** | `.carte`, `[type="text"]`, `:hover` |
| **C** | Sélecteurs de **type** et **pseudo-éléments** | `p`, `::before` |

```css
p                     /* (0,0,1) */
.titre                /* (0,1,0) */
p.titre               /* (0,1,1) */
#titre                /* (1,0,0) */
nav ul li a:hover     /* (0,1,4) */
:is(#a, .b)           /* (1,0,0) — :is() prend la spécificité de son argument le plus spécifique */
:where(#a, .b)        /* (0,0,0) — :where() vaut toujours zéro */
:not(.x)              /* (0,1,0) — comme son argument */
*                     /* (0,0,0) */
```

> ⚠️ **Idée reçue** : « ID = 100, classe = 10, balise = 1 » est une **simplification**. Avec 11 classes, vous **ne battez pas** un identifiant : (0,11,0) < (1,0,0), car les colonnes ne « débordent » jamais l'une sur l'autre.
> Les **styles en ligne** (`style="…"`) l'emportent sur tous les sélecteurs (au-dessus de la colonne A) ; `!important` passe devant tout.

```css
#titre { color: blue; }     /* (1,0,0) */
.titre { color: red; }      /* (0,1,0) */
h1     { color: green; }    /* (0,0,1) */
/* <h1 id="titre" class="titre"> → bleu */
```

## 4.3 `!important`

```css
.bouton { background: gray !important; }     /* ⚠️ à éviter */
```

À réserver aux **classes utilitaires** (`.cache { display: none !important; }`) et à la surcharge de styles tiers impossibles à modifier. Préférez les **couches** (`@layer`) ou une spécificité maîtrisée.

## 4.4 Cascade layers : `@layer` *(ajout, à jour)*

Les **couches de cascade** permettent de **contrôler l'ordre de priorité** par bloc, **indépendamment de la spécificité** (Baseline depuis 2022).

```css
/* 1. Déclarer l'ORDRE des couches : la dernière a la priorité la plus haute */
@layer reset, base, composants, utilitaires;

@layer reset {
    *, *::before, *::after { box-sizing: border-box; margin: 0; }
}

@layer base {
    body { font-family: system-ui, sans-serif; line-height: 1.5; }
    a { color: royalblue; }
}

@layer composants {
    .bouton { padding: .5em 1em; background: royalblue; color: white; }
}

@layer utilitaires {
    .texte-centre { text-align: center; }          /* l'emporte sur les couches précédentes, même avec une spécificité plus basse */
}

/* Les styles NON placés dans une couche l'emportent sur toutes les couches (hors !important) */
```

| Usage | Intérêt |
| --- | --- |
| Isoler un **framework / une bibliothèque** : `@import url("bootstrap.css") layer(framework);` | Vos styles gagnent **toujours**, sans `!important` |
| Architecture **reset → base → composants → utilitaires** | Ordre explicite et prévisible |
| Couches **imbriquées** : `@layer composants.bouton { … }` | Organisation fine |

## 4.5 Portée des styles : `@scope` *(ajout)*

`@scope` limite des règles à une **sous-arborescence** (avec une **borne inférieure** facultative) ; la **proximité** départage les conflits.

```css
@scope (.carte) to (.contenu) {          /* dans .carte, mais pas dans .contenu */
    img { border-radius: .5rem; }
    h2 { font-size: 1.25rem; }
}
```

> Baseline *newly available* en 2026 ; alternative native à BEM et aux CSS Modules pour limiter la portée.

## 4.6 Héritage

Certaines propriétés sont **héritées** des éléments parents (**texte** : `color`, `font-*`, `line-height`, `text-align`, `visibility`, `cursor`…). D'autres **non** (mise en page : `margin`, `padding`, `border`, `background`, `width`, `display`…).

```css
body { color: #333; font-family: system-ui, sans-serif; }     /* hérité par tous les descendants */
```

### Mots-clés de contrôle

| Mot-clé | Effet |
| --- | --- |
| `inherit` | Force la valeur du **parent** |
| `initial` | Valeur **initiale** de la spécification |
| `unset` | `inherit` si la propriété est héritée, sinon `initial` |
| `revert` | Revient à la valeur du **navigateur** (ou de l'utilisateur) |
| `revert-layer` | Revient à la valeur de la **couche précédente** |
| `all: unset` | Réinitialise **toutes** les propriétés |

```css
button { font: inherit; color: inherit; }            /* les boutons n'héritent pas de la police par défaut */
a { color: inherit; text-decoration: none; }
```

## 4.7 Déboguer la cascade

Dans les **DevTools** (F12 → onglet *Styles*) : les règles sont listées par priorité, les déclarations **barrées** sont surchargées, l'onglet **Computed** donne la valeur finale et sa règle d'origine (voir section 23).

---

# 5. Couleurs et unités

## 5.1 Formats de couleur

| Format | Exemple | Remarques |
| --- | --- | --- |
| **Nom** | `red`, `rebeccapurple`, `lightblue` | 148 couleurs nommées |
| **Hexadécimal** | `#ff0000`, `#f00`, `#ff000080` (avec alpha) | Très répandu |
| **`rgb()`** | `rgb(255 0 0)`, `rgb(255 0 0 / 50%)` | Syntaxe **moderne** : espaces et `/` pour l'alpha |
| **`hsl()`** | `hsl(240 100% 50%)`, `hsl(240 100% 50% / .3)` | Teinte (0–360°), saturation, luminosité : intuitif |
| **`hwb()`** | `hwb(240 0% 0%)` | Teinte, blanc, noir |
| **`oklch()`** ✅ | `oklch(70% 0.15 250)` | Luminosité, chroma, teinte : **perceptuellement uniforme**, gamme étendue |
| **`oklab()`**, `lab()`, `lch()` | | Espaces perceptuels |
| **`color()`** | `color(display-p3 1 0 0)` | Espaces à gamut large (écrans P3) |
| **`currentColor`** | `border-color: currentColor;` | Valeur courante de `color` |
| **`transparent`** | | `rgb(0 0 0 / 0)` |

```css
p {
    color: rgb(0 128 0);                          /* vert */
    background: rgb(255 0 0 / 50%);                /* rouge semi-transparent (remplace rgba()) */
    border-color: hsl(210 80% 50%);
}
```

> 📌 **À jour** : les formes **`rgba()`** et **`hsla()`** et les **virgules** (`rgb(255, 0, 0)`) sont **historiques** mais restent valides. La syntaxe moderne (`rgb(r g b / a)`) est équivalente et plus cohérente.

### Fonctions de couleur modernes *(ajout)*

```css
/* color-mix() : mélanger deux couleurs */
.bouton:hover { background: color-mix(in oklch, royalblue 85%, black); }
.survol { background: color-mix(in srgb, currentColor 10%, transparent); }

/* Syntaxe de couleur relative : dériver une couleur d'une autre */
:root {
    --marque: oklch(60% 0.2 260);
    --marque-claire: oklch(from var(--marque) calc(l + 0.2) c h);
    --marque-translucide: rgb(from var(--marque) r g b / 40%);
}

/* light-dark() : valeur selon le thème clair / sombre (nécessite color-scheme) */
:root { color-scheme: light dark; }
body { background: light-dark(#fff, #121212); color: light-dark(#222, #eee); }

/* contrast-color() : couleur de texte lisible sur un fond donné (support récent) */
.badge { background: var(--fond); color: contrast-color(var(--fond)); }
```

## 5.2 Opacité

```css
div { opacity: .5; }                     /* ⚠️ affecte l'élément ET tous ses enfants */
div { background: rgb(0 0 0 / .5); }     /* ✅ seulement le fond */
```

## 5.3 Unités de longueur

### Absolues

| Unité | Description |
| --- | --- |
| `px` | Pixel CSS (unité de base) |
| `cm`, `mm`, `in`, `pt`, `pc`, `Q` | Unités physiques (surtout pour l'impression) |

### Relatives à la **typographie**

| Unité | Relative à… |
| --- | --- |
| `em` | **Taille de police** de l'élément (de son parent pour `font-size`) |
| `rem` | Taille de police de l'élément **racine** (`<html>`) ✅ |
| `ch` | Largeur du caractère « 0 » (idéal pour limiter la longueur de ligne : `max-width: 65ch`) |
| `ex`, `cap`, `ic` | Hauteur du « x », des majuscules, d'un idéogramme |
| `lh`, `rlh` | **Hauteur de ligne** de l'élément / de la racine |

### Relatives à la **fenêtre** (viewport) *(à jour)*

| Unité | Signification |
| --- | --- |
| `vw`, `vh` | 1 % de la largeur / hauteur de la fenêtre |
| `vmin`, `vmax` | 1 % de la plus petite / plus grande dimension |
| **`svh`, `lvh`, `dvh`** ✅ | Hauteur **petite** (barre d'adresse visible), **grande** (masquée), **dynamique** (s'adapte) |
| `svw`, `dvw`… ; `vi`, `vb` | Équivalents horizontaux ; axes **logiques** (inline / block) |

```css
.hero { min-height: 100dvh; }            /* ✅ sur mobile, 100vh dépasse l'écran visible à cause de la barre d'adresse */
```

### Relatives au **conteneur** *(ajout)*

| Unité | Signification |
| --- | --- |
| `cqw`, `cqh` | 1 % de la largeur / hauteur du **conteneur** (voir section 14) |
| `cqi`, `cqb`, `cqmin`, `cqmax` | Axes logiques et min/max |

### Autres

| Unité | Usage |
| --- | --- |
| `%` | Pourcentage du parent (dépend de la propriété) |
| `fr` | Fraction de l'espace disponible (**Grid**) |
| `deg`, `rad`, `turn` | Angles |
| `s`, `ms` | Durées |
| `dpi`, `dppx` | Résolution |

```css
html { font-size: 100%; }                 /* 16px par défaut : respecte les préférences de l'utilisateur */
h1 { font-size: 2rem; margin-block: 1.5rem; }
.contenu { max-width: 65ch; }
.panneau { width: 80%; }
.hero { height: 50svh; }
```

> **Choisir** : `rem` pour les **polices et espacements** (accessibilité : suit les réglages de l'utilisateur) ; `em` pour les composants qui doivent **s'adapter à leur propre taille** ; `px` pour les **bordures fines** ; `%`, `fr`, `dvh`, `cq*` pour la **mise en page**.

## 5.4 Fonctions mathématiques *(ajout)*

```css
width: calc(100% - 2rem);                              /* mélange d'unités */
width: min(90%, 60rem);                                /* la plus petite valeur */
padding: max(1rem, 3vw);                               /* la plus grande */
font-size: clamp(1rem, 0.9rem + 1vw, 1.5rem);         /* min, valeur fluide, max */
height: round(down, 100%, 8px);                        /* arrondi à un multiple (round, mod, rem) */
transform: rotate(calc(var(--i) * 15deg));
width: calc(var(--colonnes) * 1fr);
```

Fonctions disponibles : `calc()`, `min()`, `max()`, `clamp()`, `round()`, `mod()`, `rem()`, `abs()`, `sign()`, trigonométriques (`sin()`, `cos()`, `tan()`, `atan2()`), `pow()`, `sqrt()`, `hypot()`, `log()`, `exp()`.

---

# 6. Le modèle de boîte

## 6.1 Tout élément est une boîte

```text
┌──────────────────────── margin (marge) ────────────────────────┐
│  ┌───────────────────── border (bordure) ──────────────────┐   │
│  │  ┌──────────────── padding (marge intérieure) ───────┐  │   │
│  │  │                                                   │  │   │
│  │  │                  content (contenu)                │  │   │
│  │  │                                                   │  │   │
│  │  └───────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

| Zone | Rôle | Fond de l'élément ? |
| --- | --- | --- |
| **Contenu** | Texte, images | ✅ |
| **Padding** | Espace **intérieur** entre le contenu et la bordure | ✅ |
| **Bordure** | Contour | ✅ |
| **Marge** | Espace **extérieur** (transparent) | ❌ |

## 6.2 `box-sizing`

Par défaut (`content-box`), `width` ne concerne que le **contenu** : padding et bordure s'**ajoutent** (et la boîte devient plus large que prévu).

```css
.boite { width: 300px; padding: 20px; border: 5px solid; }
/* content-box : largeur réelle = 300 + 2×20 + 2×5 = 350px
   border-box  : largeur réelle = 300px (le contenu rétrécit) */
```

```css
/* ✅ Réglage universel recommandé */
*, *::before, *::after { box-sizing: border-box; }
```

## 6.3 Largeur et hauteur

```css
.boite {
    width: 50%;
    height: auto;                          /* défaut : s'adapte au contenu */
    min-width: 200px;  max-width: 100%;
    min-height: 100px; max-height: 80vh;
    aspect-ratio: 16 / 9;                  /* ✅ rapport largeur/hauteur (remplace le « padding hack ») */
}

.contenu {
    width: fit-content;                    /* mots-clés intrinsèques */
    width: min-content;  width: max-content;
    max-inline-size: 65ch;
}
```

| Valeur | Effet |
| --- | --- |
| `auto` | Selon le type d'élément (bloc : pleine largeur ; hauteur : contenu) |
| `fit-content` | S'ajuste au contenu mais **plafonné** par l'espace disponible |
| `min-content` / `max-content` | Plus petite / plus grande largeur possible du contenu |
| `stretch` | Remplit l'espace disponible (marges comprises) |

> 💡 **`max-width` + `width: 100%`** pour des éléments flexibles ; **`min-height`** plutôt que `height` fixe pour laisser respirer le contenu.

## 6.4 Marges et espacement intérieur

```css
.boite {
    margin: 10px;                          /* les 4 côtés */
    margin: 10px 20px;                     /* vertical | horizontal */
    margin: 10px 20px 30px;                /* haut | horizontal | bas */
    margin: 10px 20px 30px 40px;           /* haut | droite | bas | gauche (sens horaire) */
    margin: 0 auto;                        /* centre horizontalement un bloc de largeur définie */

    padding: 1rem 2rem;                    /* même logique que margin */
}
```

### Fusion des marges (*margin collapsing*)

Les **marges verticales** de blocs adjacents **fusionnent** (la plus grande l'emporte) ; ce n'est **pas** le cas dans **Flexbox/Grid**, ni avec du `padding`/`border` entre les éléments, ni pour les marges horizontales.

```css
h2 { margin-bottom: 2rem; }
p  { margin-top: 1rem; }               /* l'espace entre h2 et p vaut 2rem, pas 3rem */
```

> ✅ **Astuce moderne** : utilisez **`gap`** (Flexbox/Grid) ou un seul sens de marge (`margin-block-end`) pour espacer les éléments de façon prévisible.

## 6.5 Propriétés logiques *(à jour)*

Les propriétés **logiques** s'adaptent au **sens d'écriture** (gauche-à-droite, droite-à-gauche, vertical) : indispensables pour l'internationalisation.

| Physique | Logique |
| --- | --- |
| `width` / `height` | `inline-size` / `block-size` |
| `margin-left` / `margin-right` | `margin-inline-start` / `margin-inline-end` |
| `margin-top` / `margin-bottom` | `margin-block-start` / `margin-block-end` |
| `padding-left` + `padding-right` | `padding-inline` |
| `padding-top` + `padding-bottom` | `padding-block` |
| `top`, `right`, `bottom`, `left` | `inset-block-start`, `inset-inline-end`, `inset-block-end`, `inset-inline-start` |
| `text-align: left` | `text-align: start` |
| `border-left` | `border-inline-start` |
| `border-top-left-radius` | `border-start-start-radius` |

```css
.carte {
    padding-inline: 1.5rem;                 /* gauche + droite */
    padding-block: 1rem;                    /* haut + bas */
    margin-inline: auto;                    /* centre */
    border-inline-start: 4px solid tomato;  /* à gauche en LTR, à droite en RTL */
    max-inline-size: 40rem;
}
```

## 6.6 Bordures et contours

```css
.boite {
    border: 2px solid black;               /* largeur | style | couleur */
    border-top: 1px dashed gray;
    border-radius: 8px;                    /* coins arrondis */
    border-radius: 50%;                    /* cercle / ellipse */
    border-radius: 10px 20px 30px 40px;    /* haut-gauche, haut-droite, bas-droite, bas-gauche */
}
```

Styles : `solid`, `dashed`, `dotted`, `double`, `groove`, `ridge`, `inset`, `outset`, `none`, `hidden`.

### `outline` : contour qui ne prend pas de place

```css
button:focus-visible {
    outline: 3px solid royalblue;
    outline-offset: 2px;
}
```

> ⚠️ **Ne supprimez jamais** `outline` sans le remplacer (`outline: none` rend la navigation au clavier impossible). Utilisez `:focus-visible` pour n'afficher l'anneau qu'au clavier.

## 6.7 Débordement et affichage du modèle de boîte

```css
.boite {
    overflow: hidden;                      /* voir section 8 */
    box-sizing: border-box;
}
```

Un élément **en ligne** (`inline`) ignore `width`/`height` et les marges verticales ; un **bloc** (`block`) occupe toute la largeur ; un **inline-block** combine les deux (voir section 8).

## 6.8 Bonnes pratiques

- `box-sizing: border-box` partout.
- Utiliser des **unités relatives** (`rem`, `%`, `ch`) et `max-width` plutôt que des largeurs fixes en pixels.
- Espacer avec **`gap`**, `margin-block`/`padding-inline` et une **échelle d'espacement** (variables : `--esp-1`, `--esp-2`…).
- Adopter les **propriétés logiques**.

---

# 7. Texte et polices

## 7.1 Propriétés de texte

```css
p {
    color: #333;
    text-align: start;                       /* start | end | center | justify (⚠️ left/right physiques) */
    text-indent: 2em;                        /* retrait de la première ligne */
    text-decoration: underline wavy red;     /* ligne | style | couleur */
    text-transform: capitalize;
}
```

### `text-decoration` (raccourci)

```css
a {
    text-decoration-line: underline;         /* none | underline | overline | line-through */
    text-decoration-style: solid;            /* solid | double | dotted | dashed | wavy */
    text-decoration-color: tomato;
    text-decoration-thickness: .1em;
    text-underline-offset: .2em;             /* distance entre le texte et le soulignement */
    text-decoration-skip-ink: auto;          /* évite de traverser les jambages */
}
```

### `text-transform`

`none` · `uppercase` · `lowercase` · `capitalize` · `full-width`

## 7.2 Polices

```css
body {
    font-family: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;     /* liste de repli */
    font-size: 1rem;
    font-weight: 400;                        /* 100 à 900 (ou normal = 400, bold = 700) */
    font-style: italic;                      /* normal | italic | oblique */
    font-variant-numeric: tabular-nums;      /* chiffres de largeur fixe (tableaux) */
}
```

| Famille générique | Exemples |
| --- | --- |
| `serif` | Georgia, Times |
| `sans-serif` | Arial, Helvetica |
| `monospace` | Courier, Consolas |
| `system-ui` ✅ | Police système (rapide, native) |
| `ui-serif`, `ui-sans-serif`, `ui-monospace`, `ui-rounded` | Variantes système |
| `cursive`, `fantasy`, `math` | Spécifiques |

### Raccourci `font`

```css
p { font: italic 700 1.125rem/1.6 "Georgia", serif; }
/*     style poids taille/hauteur-de-ligne famille — « taille » et « famille » sont obligatoires */
```

## 7.3 Polices web : `@font-face`

```css
@font-face {
    font-family: "Inter";
    src: url("/polices/inter-var.woff2") format("woff2");      /* WOFF2 : format recommandé */
    font-weight: 100 900;                                       /* police VARIABLE : plage de graisses */
    font-style: normal;
    font-display: swap;                                         /* affiche le texte tout de suite avec une police de repli */
    unicode-range: U+0000-00FF;                                 /* ne télécharge que si ces caractères sont utilisés */
}
```

| `font-display` | Comportement |
| --- | --- |
| `swap` | Texte visible immédiatement avec la police de repli, puis échange |
| `fallback` | Courte période d'invisibilité, échange limité dans le temps |
| `optional` | La police web n'est utilisée que si elle est déjà chargée (meilleur pour les performances) |

### Polices variables *(ajout)*

Un seul fichier contient **toutes les graisses / largeurs / inclinaisons** :

```css
h1 { font-variation-settings: "wght" 650, "wdth" 110; }
.fin { font-weight: 300; }
.large { font-stretch: 125%; }
```

### Conseils de performance

- Format **WOFF2**, **sous-ensembles** (`unicode-range`), `font-display: swap/optional`.
- **Préchargez** la police critique : `<link rel="preload" as="font" type="font/woff2" crossorigin>`.
- Limitez le nombre de familles / graisses ; privilégiez une **police variable** ou la **pile système**.
- Héberger **localement** (RGPD, performance) plutôt que via un CDN tiers.
- Réduire le décalage de mise en page avec `size-adjust`, `ascent-override` (métriques de la police de repli).

## 7.4 Espacement du texte

```css
p {
    line-height: 1.6;                       /* ✅ SANS unité : multiple de la taille de police */
    letter-spacing: .02em;                  /* espacement des lettres */
    word-spacing: .1em;                     /* espacement des mots */
}
h1 { line-height: 1.2; letter-spacing: -.02em; }
```

> ✅ **`line-height` sans unité** (1.5 – 1.7 pour le texte courant) est héritée comme **facteur** ; avec une unité (`24px`), la valeur calculée est héritée telle quelle, ce qui peut poser problème.

## 7.5 Gestion de l'espace blanc et du retour à la ligne

| Propriété | Valeurs utiles |
| --- | --- |
| `white-space` | `normal`, `nowrap` (pas de retour), `pre` (préserve), `pre-wrap`, `pre-line`, `break-spaces` |
| `overflow-wrap` | `anywhere`, `break-word` : coupe les mots trop longs |
| `word-break` | `normal`, `break-all`, `keep-all` (CJK) |
| `hyphens` | `manual`, `auto` (coupure avec `lang` défini) |
| `text-wrap` ✅ | `balance` (titres équilibrés), `pretty` (évite les lignes orphelines), `nowrap`, `stable` |
| `text-overflow` | `ellipsis` (avec `overflow: hidden; white-space: nowrap`) |

```css
h1, h2, h3 { text-wrap: balance; }        /* lignes de longueur équilibrée */
p { text-wrap: pretty; hyphens: auto; overflow-wrap: break-word; }

.une-ligne {                              /* une ligne tronquée par « … » */
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.trois-lignes {                           /* troncature multiligne (largement supporté) */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    line-clamp: 3;
    overflow: hidden;
}
```

## 7.6 Style de texte avancé

```css
.etiquette { font-variant-caps: all-small-caps; }
.chiffre { font-feature-settings: "tnum" 1; }                    /* fonctionnalités OpenType */
.colonnes { column-count: 2; column-gap: 2rem; column-rule: 1px solid #ddd; }   /* colonnes de journal */
.vertical { writing-mode: vertical-rl; }
.degrade { background: linear-gradient(90deg, red, blue); background-clip: text; color: transparent; }   /* texte dégradé */
.lettrine::first-letter { initial-letter: 3; }                   /* lettrine (support partiel) */
p { text-box-trim: trim-both; text-box-edge: cap alphabetic; }   /* aligner sur la hauteur des capitales (support récent) */
```

## 7.7 Taille de texte fluide *(ajout)*

```css
:root {
    --texte: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
    --titre: clamp(1.75rem, 1.2rem + 2.5vw, 3rem);
}
body { font-size: var(--texte); }
h1 { font-size: var(--titre); }
```

## 7.8 Accessibilité du texte

- Taille de base **16 px** (ne pas descendre sous 1 rem) ; unités **`rem`** pour respecter les préférences de zoom.
- **Contraste** suffisant : **4,5 : 1** pour le texte courant (WCAG AA), **3 : 1** pour le grand texte.
- **Longueur de ligne** de 45 à 75 caractères (`max-width: 65ch`).
- Ne pas utiliser `text-align: justify` sans `hyphens: auto`.

---

# 🟡 Mise en page

---

# 8. Affichage, positionnement et débordement

## 8.1 La propriété `display`

`display` définit **comment un élément se comporte** dans le flux de la page (et comment ses enfants sont disposés).

| Valeur | Comportement |
| --- | --- |
| `block` | Occupe **toute la largeur**, commence sur une **nouvelle ligne** ; `width`, `height`, marges acceptés (`<div>`, `<p>`, `<h1>`) |
| `inline` | S'insère **dans la ligne de texte** ; ignore `width`/`height` et les marges verticales (`<span>`, `<a>`) |
| `inline-block` | En ligne **mais** accepte `width`, `height`, marges |
| `none` | **Retire** l'élément (et ses enfants) de la page et de l'arbre d'accessibilité |
| `flex` / `inline-flex` | Conteneur **Flexbox** (section 9) |
| `grid` / `inline-grid` | Conteneur **Grid** (section 10) |
| `flow-root` | Crée un **contexte de formatage de bloc** (contient les flottants, évite la fusion des marges) |
| `contents` | L'élément « disparaît » : ses **enfants** deviennent enfants de son parent |
| `table`, `table-row`, `table-cell` | Comportements de tableau |
| `list-item` | Comme un `<li>` (avec puce) |

```css
.cache { display: none; }
.bouton { display: inline-block; padding: .5em 1em; }
.parent { display: flow-root; }          /* contient ses enfants flottants, sans « clearfix » */
```

> ♿ `display: none` et `visibility: hidden` **masquent aussi aux lecteurs d'écran**. Pour masquer **visuellement** seulement, voir la classe `.sr-only` (section 16).

| | `display: none` | `visibility: hidden` | `opacity: 0` |
| --- | --- | --- | --- |
| Prend de la place | ❌ | ✅ | ✅ |
| Interactif (clics, focus) | ❌ | ❌ | ✅ |
| Lecteurs d'écran | ❌ | ❌ | ✅ |
| Animable | ❌ (transition spéciale, voir 13.4) | ✅ | ✅ |

## 8.2 La propriété `position`

| Valeur | Comportement |
| --- | --- |
| `static` (défaut) | Flux normal ; `top`/`left`… sans effet |
| `relative` | Reste dans le flux ; peut être **décalé** ; sert de **repère** aux enfants `absolute` |
| `absolute` | **Sorti du flux** ; positionné par rapport à l'**ancêtre positionné** le plus proche |
| `fixed` | Sorti du flux ; positionné par rapport à la **fenêtre** (reste visible au défilement) |
| `sticky` | Hybride : `relative` jusqu'à un **seuil de défilement**, puis « collé » |

```css
.parent { position: relative; }                       /* repère */
.badge {
    position: absolute;
    inset-block-start: -8px;                          /* haut */
    inset-inline-end: -8px;                           /* droite */
}

.entete { position: fixed; inset: 0 0 auto 0; }       /* top/right/left = 0, bottom = auto */

.titre-section {
    position: sticky;
    top: 0;                                           /* seuil obligatoire */
    background: white;
}

.recouvrir { position: absolute; inset: 0; }          /* remplit entièrement le parent positionné */
```

> `inset` est le raccourci de `top`, `right`, `bottom`, `left` (comme `margin`). `sticky` ne fonctionne pas si un **ancêtre** a `overflow: hidden/auto` (sauf s'il est le conteneur de défilement voulu).

## 8.3 Centrer un élément

| Besoin | Solution moderne |
| --- | --- |
| Texte centré horizontalement | `text-align: center;` |
| Bloc de largeur définie, horizontalement | `margin-inline: auto;` |
| **Centrer dans les deux axes** ✅ | `display: grid; place-items: center;` |
| Idem avec Flexbox | `display: flex; justify-content: center; align-items: center;` |
| Élément absolu | `position: absolute; inset: 0; margin: auto; width: …; height: …;` |
| Absolu (méthode classique) | `top: 50%; left: 50%; translate: -50% -50%;` |

```css
.centre { display: grid; place-items: center; min-height: 100dvh; }
```

## 8.4 `z-index` et contextes d'empilement

`z-index` contrôle l'**ordre d'empilement** (axe Z) des éléments **positionnés** (ou éléments flex / grid).

```css
.fond   { position: relative; z-index: 1; }
.modale { position: fixed; z-index: 1000; }
.negatif { position: relative; z-index: -1; }          /* passe derrière */
```

### Contextes d'empilement (*stacking contexts*)

Un élément crée un **contexte d'empilement** quand il a, entre autres : `position` (≠ `static`) + `z-index` ≠ `auto` ; `opacity` < 1 ; `transform`, `filter`, `perspective`, `will-change` ; `isolation: isolate` ; `mix-blend-mode`. Ses enfants sont empilés **à l'intérieur** de ce contexte : leur `z-index` **ne peut pas dépasser** celui de leur contexte parent.

```css
.composant { isolation: isolate; }          /* ✅ crée un contexte sans effet visuel : évite les « guerres de z-index » */
```

### Bonnes pratiques

- Définir une **échelle** de variables (`--z-menu: 100; --z-modale: 1000; --z-toast: 1100;`).
- Pour les modales et menus : l'élément **`<dialog>`** et l'attribut **`popover`** utilisent la **couche supérieure** (*top layer*) : **plus besoin de `z-index`** (section 24).

## 8.5 Débordement : `overflow`

Détermine ce qui se passe quand le **contenu dépasse** la boîte.

| Valeur | Effet |
| --- | --- |
| `visible` (défaut) | Le contenu **déborde** |
| `hidden` | **Rogné**, pas de barre de défilement |
| `scroll` | Barres **toujours** affichées |
| `auto` | Barres **seulement si nécessaire** ✅ |
| `clip` | Rogné **sans** créer de conteneur de défilement |

```css
.zone-defilement { max-height: 300px; overflow-y: auto; }
.carrousel { overflow-x: auto; overscroll-behavior-x: contain; }
.rogne { overflow: hidden; border-radius: 1rem; }                   /* contient aussi les coins arrondis */
.tableau-large { overflow-x: auto; }                                 /* tableau défilant horizontalement sur mobile */
```

Propriétés associées :

| Propriété | Rôle |
| --- | --- |
| `overflow-x` / `overflow-y` | Contrôle par axe |
| `overscroll-behavior` | Évite la propagation du défilement (modales, panneaux) |
| `scrollbar-gutter: stable` | Réserve la place de la barre (évite le décalage de mise en page) |
| `scrollbar-width`, `scrollbar-color` | Style des barres de défilement (standard) |
| `scroll-behavior: smooth` | Défilement fluide (respecter `prefers-reduced-motion`) |
| `scroll-margin-top`, `scroll-padding-top` | Décalage pour les ancres sous un en-tête collant |
| `scroll-snap-type`, `scroll-snap-align` | **Accroche** au défilement (carrousels) |

```css
html { scroll-behavior: smooth; scroll-padding-top: 4rem; }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
```

## 8.6 Éléments remplacés : images, vidéos

```css
img, video {
    max-width: 100%;
    height: auto;
    display: block;                           /* supprime l'espace sous l'image (alignement sur la ligne de base) */
}
.vignette { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; object-position: center; }
```

| `object-fit` | Comportement |
| --- | --- |
| `fill` | Étire (déforme) |
| `contain` | Image entière visible (marges possibles) |
| `cover` | Remplit en **rognant** |
| `none`, `scale-down` | Taille d'origine / réduction seule |

## 8.7 Les flottants : `float` et `clear` *(héritage)*

`float` retire l'élément du flux et le place à gauche/droite, le texte s'enroulant autour. C'était **l'outil de mise en page avant Flexbox/Grid**.

```css
.image-article { float: left; margin: 0 1rem 1rem 0; shape-outside: circle(50%); }   /* habillage de texte */
.apres { clear: both; }                                                              /* se place sous les flottants */
```

> ✅ **Aujourd'hui**, `float` ne sert **plus** qu'à **habiller une image avec du texte**. Pour les mises en page : **Flexbox** et **Grid**.
> Le « *clearfix* » (`::after { content: ""; display: table; clear: both; }`) est **remplacé** par `display: flow-root` sur le parent.

## 8.8 Comparaison des méthodes de mise en page

| Besoin | Outil |
| --- | --- |
| **Une dimension** (barre de navigation, rangée de boutons, centrer) | **Flexbox** |
| **Deux dimensions** (page, galerie, tableau de bord) | **Grid** |
| Texte autour d'une image | `float` + `shape-outside` |
| Placer un badge, une infobulle, une superposition | `position` / **ancrage** (section 15) |
| Colonnes de texte | `columns` |

---

# 9. Flexbox

## 9.1 Principe

**Flexbox** dispose des éléments **sur un axe** (ligne ou colonne) en répartissant l'espace et en gérant l'alignement.

```text
Axe principal (main axis)   ──────────────────▶   (flex-direction : row)
┌─────────┬─────────┬─────────┐ ▲
│  item 1 │  item 2 │  item 3 │ │ Axe secondaire (cross axis)
└─────────┴─────────┴─────────┘ ▼
```

```css
.conteneur { display: flex; }          /* les enfants directs deviennent des « éléments flex » */
```

## 9.2 Propriétés du **conteneur**

| Propriété | Valeurs | Rôle |
| --- | --- | --- |
| `flex-direction` | `row` (défaut), `row-reverse`, `column`, `column-reverse` | Axe principal |
| `flex-wrap` | `nowrap` (défaut), `wrap`, `wrap-reverse` | Retour à la ligne |
| `flex-flow` | `row wrap` | Raccourci direction + wrap |
| `justify-content` | `flex-start`, `center`, `flex-end`, `space-between`, `space-around`, `space-evenly` | Alignement sur l'**axe principal** |
| `align-items` | `stretch` (défaut), `flex-start`, `center`, `flex-end`, `baseline` | Alignement sur l'**axe secondaire** |
| `align-content` | idem `justify-content` | Répartition des **lignes** (avec `wrap`) |
| **`gap`** | `1rem`, `1rem 2rem` | **Espacement** entre éléments (✅ remplace les marges) |

```css
.barre {
    display: flex;
    justify-content: space-between;          /* logo à gauche, menu à droite */
    align-items: center;                     /* centrés verticalement */
    gap: 1rem;
    flex-wrap: wrap;
}
```

## 9.3 Propriétés des **éléments**

| Propriété | Rôle |
| --- | --- |
| `flex-grow` | Part de l'espace **excédentaire** à absorber (0 par défaut) |
| `flex-shrink` | Capacité à **rétrécir** (1 par défaut) |
| `flex-basis` | Taille **de départ** sur l'axe principal (`auto`, `200px`, `30%`) |
| **`flex`** (raccourci) | `grow shrink basis` |
| `align-self` | Alignement **individuel** sur l'axe secondaire |
| `order` | Ordre d'affichage (⚠️ n'affecte pas l'ordre de navigation au clavier ni de lecture) |
| `min-width: 0` | Autorise un élément flex à **rétrécir** sous la taille de son contenu |

```css
.item { flex: 1; }                  /* = 1 1 0 : partage équitablement l'espace */
.item-fixe { flex: 0 0 200px; }     /* ne grandit ni ne rétrécit : 200px */
.principal { flex: 1 1 20rem; }     /* base 20rem, grandit et rétrécit */
.dernier { margin-inline-start: auto; }       /* pousse l'élément à l'extrémité (astuce « auto ») */
.special { align-self: flex-end; }
```

| Raccourci | Équivalent | Usage |
| --- | --- | --- |
| `flex: 1` | `1 1 0%` | Partage égal |
| `flex: auto` | `1 1 auto` | Selon le contenu puis s'étire |
| `flex: none` | `0 0 auto` | Taille fixe |
| `flex: 0 1 auto` | (défaut) | |

## 9.4 Exemples courants

### Barre de navigation

```css
.nav { display: flex; align-items: center; gap: 1.5rem; padding-inline: 1rem; }
.nav .logo { margin-inline-end: auto; }       /* pousse le reste à droite */
```

### Cartes qui s'adaptent (sans media query)

```css
.cartes { display: flex; flex-wrap: wrap; gap: 1rem; }
.carte { flex: 1 1 15rem; }                   /* au moins 15rem, partage l'espace restant */
```

### Pied de page collé en bas

```css
body { min-height: 100dvh; display: flex; flex-direction: column; }
main { flex: 1; }                              /* occupe l'espace restant, pousse le footer */
```

### Centrage parfait

```css
.centre { display: flex; justify-content: center; align-items: center; min-height: 100dvh; }
```

### Barre d'outils / formulaire inline

```css
.recherche { display: flex; gap: .5rem; }
.recherche input { flex: 1; }
```

## 9.5 Pièges fréquents

| Problème | Solution |
| --- | --- |
| Le contenu **dépasse** de l'élément flex | `min-width: 0` (ou `overflow: hidden`) sur l'élément |
| Les éléments **s'écrasent** | `flex-wrap: wrap` ou `flex-shrink: 0` |
| `justify-content` sans effet | Vérifier `flex-direction` (l'axe principal change avec `column`) |
| `margin: auto` « pousse » | C'est un outil : il absorbe tout l'espace libre |
| `order` modifie l'ordre visuel seulement | Garder un **ordre DOM logique** (accessibilité) |

## 9.6 Flexbox ou Grid ?

Flexbox est **unidimensionnel** : il excelle pour aligner des éléments **dans une rangée ou une colonne**. Dès que vous pensez en **lignes ET colonnes** (alignement sur les deux axes), utilisez **Grid** (section 10). Ils se **combinent** : Grid pour la page, Flexbox pour les composants.

---

# 10. CSS Grid

## 10.1 Principe

**Grid** dispose des éléments dans une **grille à deux dimensions** (lignes et colonnes).

```css
.grille {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;      /* 3 colonnes : 25 % 50 % 25 % de l'espace */
    grid-template-rows: auto 1fr auto;
    gap: 1rem;                                /* (grid-gap est l'ancien nom) */
}
```

## 10.2 Propriétés du **conteneur**

| Propriété | Rôle |
| --- | --- |
| `grid-template-columns` / `grid-template-rows` | Définit les **pistes** (colonnes / lignes) |
| `grid-template-areas` | Définit des **zones nommées** |
| `gap`, `row-gap`, `column-gap` | Gouttières |
| `grid-auto-rows` / `grid-auto-columns` | Taille des pistes **créées automatiquement** |
| `grid-auto-flow` | `row` (défaut), `column`, `dense` (comble les trous) |
| `justify-items`, `align-items`, `place-items` | Alignement du contenu **dans chaque cellule** |
| `justify-content`, `align-content`, `place-content` | Alignement **de la grille** dans le conteneur |

### Unités et fonctions de Grid

```css
grid-template-columns: 200px 1fr 1fr;                       /* fixe + flexibles */
grid-template-columns: repeat(3, 1fr);                      /* 3 colonnes égales */
grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));    /* ✅ nombre de colonnes AUTOMATIQUE (responsive sans media query) */
grid-template-columns: minmax(0, 1fr) auto;
grid-template-columns: [debut] 1fr [milieu] 2fr [fin];     /* lignes nommées */
grid-template-rows: auto 1fr auto;
```

| Valeur | Signification |
| --- | --- |
| `fr` | Fraction de l'**espace restant** |
| `minmax(min, max)` | Taille comprise entre deux valeurs |
| `auto-fit` | Crée autant de colonnes que possible et **étire** les colonnes pour remplir |
| `auto-fill` | Crée autant de colonnes que possible, sans étirer (laisse des colonnes vides) |
| `fit-content()`, `min-content`, `max-content` | Tailles selon le contenu |

## 10.3 Placer des éléments

```css
.entete  { grid-column: 1 / -1; }              /* de la 1re à la dernière ligne : occupe toute la largeur */
.large   { grid-column: span 2; }              /* s'étend sur 2 colonnes */
.haut    { grid-row: 1 / 3; }                  /* de la ligne 1 à la ligne 3 */
.cellule { grid-area: 2 / 1 / 3 / 3; }         /* ligne-début / col-début / ligne-fin / col-fin */
.centre  { place-self: center; }               /* align-self + justify-self */
```

### Zones nommées : mise en page lisible

```css
.page {
    display: grid;
    grid-template-columns: 15rem 1fr;
    grid-template-rows: auto 1fr auto;
    grid-template-areas:
        "entete entete"
        "menu   contenu"
        "pied   pied";
    min-height: 100dvh;
    gap: 1rem;
}
.page > header { grid-area: entete; }
.page > nav    { grid-area: menu; }
.page > main   { grid-area: contenu; }
.page > footer { grid-area: pied; }

@media (max-width: 40rem) {                    /* réorganiser sur mobile : seulement la définition des zones change */
    .page {
        grid-template-columns: 1fr;
        grid-template-areas: "entete" "menu" "contenu" "pied";
    }
}
```

## 10.4 Exemples

### Galerie responsive (sans media query)

```css
.galerie {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 14rem), 1fr));    /* min(100%, …) évite le débordement sur petit écran */
    gap: 1rem;
}
.galerie img { width: 100%; aspect-ratio: 1; object-fit: cover; }
```

### Disposition « Saint Graal » (en-tête, 3 colonnes, pied)

```css
.layout { display: grid; grid-template: auto 1fr auto / 12rem 1fr 12rem; min-height: 100dvh; }
.layout > header, .layout > footer { grid-column: 1 / -1; }
```

### Tableau de bord avec cartes de tailles variées

```css
.tableau-de-bord { display: grid; grid-template-columns: repeat(4, 1fr); grid-auto-rows: 10rem; gap: 1rem; grid-auto-flow: dense; }
.widget-large { grid-column: span 2; }
.widget-haut  { grid-row: span 2; }
```

## 10.5 Subgrid *(ajout, à jour)*

Une **grille imbriquée** peut **hériter des pistes** de sa grille parente : les contenus de plusieurs cartes s'alignent entre eux (titres, images, pieds de cartes à la même hauteur).

```css
.cartes { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
.carte {
    display: grid;
    grid-row: span 3;                          /* la carte occupe 3 lignes de la grille parente */
    grid-template-rows: subgrid;               /* et réutilise ces 3 lignes pour ses propres éléments */
}
```

> ✅ **Subgrid** est disponible dans tous les navigateurs modernes depuis fin 2023 (Baseline *widely available*).

## 10.6 Autres fonctionnalités

- **`masonry`** (disposition en maçonnerie) : fonctionnalité **en cours de standardisation** (`display: grid-lanes` / `grid-template-rows: masonry` selon les propositions) : support **expérimental** à vérifier.
- `grid-template-columns: masonry`, `anchor` + Grid, `align-tracks` : ne pas utiliser en production sans vérifier.
- **Débogage** : les DevTools affichent une **superposition de grille** avec numéros de lignes et noms de zones.

## 10.7 Grid ou Flexbox ?

| | **Flexbox** | **Grid** |
| --- | --- | --- |
| Dimensions | **1** (ligne *ou* colonne) | **2** (lignes *et* colonnes) |
| Approche | Pilotée par le **contenu** | Pilotée par la **mise en page** |
| Idéal pour | Barres, boutons, centrage, petits composants | Page entière, galeries, tableaux de bord, alignement multi-lignes |
| Alignement sur les deux axes | Un axe à la fois (par ligne) | Natif |

> ✅ Ils se **combinent** : Grid pour la structure globale, Flexbox à l'intérieur des cellules.

---

# 11. Arrière-plans, bordures, ombres et effets

## 11.1 Arrière-plans

```css
.hero {
    background-color: #f0f0f0;
    background-image: url("hero.jpg");
    background-repeat: no-repeat;                /* repeat | repeat-x | repeat-y | space | round */
    background-position: center;                 /* ou « 50% 20% », « top right » */
    background-size: cover;                      /* cover | contain | 100% auto | 200px */
    background-attachment: fixed;                /* effet de parallaxe (⚠️ coûteux, désactivé sur mobile) */
    background-clip: padding-box;                /* border-box | padding-box | content-box | text */
    background-origin: padding-box;
}

/* Raccourci : couleur, image, position / taille, répétition… */
.bandeau { background: #222 url("motif.svg") center / cover no-repeat; }

/* Plusieurs arrière-plans (le premier est au-dessus) */
.multi {
    background:
        linear-gradient(rgb(0 0 0 / .4), rgb(0 0 0 / .4)),         /* voile sombre */
        url("photo.jpg") center / cover;
}
```

> 💡 Une image **de contenu** (informative) va dans `<img>` avec `alt` ; une image **décorative** dans `background-image`.

## 11.2 Dégradés

```css
background: linear-gradient(to right, red, yellow);                      /* direction */
background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);          /* angle + arrêts */
background: radial-gradient(circle at top left, white, transparent 60%);
background: conic-gradient(from 0deg, red, yellow, green, red);         /* camembert, roue chromatique */
background: repeating-linear-gradient(45deg, #eee 0 10px, #ddd 10px 20px);   /* rayures */
background: linear-gradient(in oklch, red, blue);                        /* interpolation dans un espace perceptuel (dégradés plus vifs) */
```

## 11.3 Ombres

```css
.carte { box-shadow: 0 2px 8px rgb(0 0 0 / .15); }
/*                    x y flou   (étalement)  couleur  (inset) */

.profond { box-shadow: 0 1px 2px rgb(0 0 0 / .1), 0 8px 24px rgb(0 0 0 / .15); }     /* ombres multiples : plus naturel */
.creuse  { box-shadow: inset 0 2px 4px rgb(0 0 0 / .2); }
.anneau  { box-shadow: 0 0 0 3px royalblue; }                                          /* faux contour (suit border-radius) */

h1 { text-shadow: 1px 1px 2px #999; }
.logo { filter: drop-shadow(0 2px 4px rgb(0 0 0 / .3)); }                              /* suit la FORME (PNG/SVG transparents) */
```

## 11.4 Filtres, fusion et formes

```css
img { filter: grayscale(100%) blur(2px) brightness(1.1) contrast(1.2); }
.verre { backdrop-filter: blur(10px) saturate(1.5); background: rgb(255 255 255 / .3); }   /* effet « verre dépoli » */
.melange { mix-blend-mode: multiply; }
.forme { clip-path: polygon(50% 0, 100% 100%, 0 100%); }               /* triangle */
.cercle { clip-path: circle(50%); }
.masque { mask-image: linear-gradient(black, transparent); }           /* fondu */
.rond { border-radius: 50%; aspect-ratio: 1; object-fit: cover; }
```

## 11.5 Bordures avancées

```css
.degrade-bordure {
    border: 4px solid transparent;
    background: linear-gradient(white, white) padding-box, linear-gradient(90deg, red, blue) border-box;   /* bordure en dégradé */
}
.image-bordure { border: 10px solid; border-image: linear-gradient(red, blue) 1; }
.arrondi-ellipse { border-radius: 50% / 10%; }
```

*(Chromium)* `corner-shape` (coins « squircle », biseautés) : fonctionnalité récente, support partiel.

## 11.6 Curseurs, sélection, sélecteurs de formulaire

```css
button { cursor: pointer; }
.desactive { cursor: not-allowed; pointer-events: none; }
.non-selectionnable { user-select: none; }
input[type="checkbox"], input[type="radio"], input[type="range"] { accent-color: royalblue; }     /* colore les contrôles natifs */
textarea { field-sizing: content; }                    /* le champ s'adapte au texte (Chromium, support en extension) */
```

## 11.7 Listes

```css
ul { list-style: none; padding: 0; }
ol { list-style-type: lower-roman; }
li::marker { color: tomato; font-weight: bold; }
ul.custom { list-style: "→ "; }                         /* puce personnalisée */
ul { list-style-position: inside; }
```

## 11.8 Tableaux

```css
table { border-collapse: collapse; width: 100%; }
th, td { padding: .5rem .75rem; border-block-end: 1px solid #ddd; text-align: start; }
tbody tr:nth-child(even) { background: #f7f7f7; }
thead th { position: sticky; top: 0; background: white; }          /* en-tête collant */
.defilement { overflow-x: auto; }                                    /* conteneur pour les tableaux larges */
```

---

# 🔴 CSS dynamique et moderne

---

# 12. Variables CSS (propriétés personnalisées)

## 12.1 Définir et utiliser

Une **propriété personnalisée** commence par `--`. Elle se **lit** avec `var()`, **hérite** comme une propriété normale et se **calcule à l'exécution** (contrairement aux variables Sass, résolues à la compilation).

```css
:root {
    --couleur-principale: #3498db;
    --espacement: 1rem;
    --rayon: .5rem;
    --police-titre: "Georgia", serif;
}

.bouton {
    background: var(--couleur-principale);
    padding: var(--espacement) calc(var(--espacement) * 2);
    border-radius: var(--rayon);
}

p { color: var(--couleur-texte, #333); }                 /* valeur de REPLI si la variable n'existe pas */
```

## 12.2 Portée et héritage

```css
:root { --texte: #222; }                                 /* globale (élément racine) */

.carte { --texte: white; background: #222; color: var(--texte); }       /* redéfinie localement : vaut pour .carte et ses descendants */

.bouton { --fond: royalblue; background: var(--fond); }
.bouton.danger { --fond: crimson; }                                       /* variante par simple redéfinition */
.bouton:hover  { --fond: color-mix(in oklch, var(--fond) 85%, black); }
```

## 12.3 Cas d'usage

| Usage | Exemple |
| --- | --- |
| **Thèmes** (clair / sombre, marque) | Redéfinir les variables sous `[data-theme="sombre"]` |
| **Design tokens** | Couleurs, espacements, rayons, ombres, échelles typographiques |
| **Composants configurables** | `.avatar { --taille: 3rem; width: var(--taille); }` |
| **Valeurs dynamiques depuis JS** | `element.style.setProperty("--x", valeur)` |
| **Calculs** | `calc(var(--colonnes) * 1fr)` |
| **Éviter la répétition** | Une valeur, un seul endroit |

```css
:root {
    /* Échelle d'espacement */
    --esp-1: .25rem; --esp-2: .5rem; --esp-3: 1rem; --esp-4: 1.5rem; --esp-5: 3rem;
    /* Typographie fluide */
    --texte-m: clamp(1rem, .95rem + .25vw, 1.125rem);
}
```

## 12.4 Thème sombre *(à jour)*

```css
/* 1. Déclarer les schémas pris en charge */
:root { color-scheme: light dark; }

/* 2. Utiliser light-dark() */
:root {
    --fond: light-dark(#ffffff, #121212);
    --texte: light-dark(#1a1a1a, #eaeaea);
    --accent: light-dark(#0b57d0, #8ab4f8);
}
body { background: var(--fond); color: var(--texte); }

/* 3. Respecter le choix manuel de l'utilisateur (bouton de bascule) */
:root[data-theme="clair"]  { color-scheme: light; }
:root[data-theme="sombre"] { color-scheme: dark; }
```

> `color-scheme` adapte aussi les **contrôles natifs** (barres de défilement, champs de formulaire). Approche classique (toujours valide) :
> ```css
> @media (prefers-color-scheme: dark) { :root { --fond: #121212; --texte: #eee; } }
> ```

## 12.5 Basculer avec JavaScript

```js
document.documentElement.dataset.theme = "sombre";                        // change le thème
document.documentElement.style.setProperty("--couleur-principale", "tomato");
getComputedStyle(document.documentElement).getPropertyValue("--espacement");   // lire
```

## 12.6 Propriétés enregistrées : `@property` *(ajout)*

`@property` **type** une variable : valeur initiale, héritage, et surtout **animation** de variables (impossible autrement).

```css
@property --angle {
    syntax: "<angle>";                      /* <color> | <length> | <number> | <percentage> | <integer>… */
    inherits: false;
    initial-value: 0deg;
}

.roue {
    background: conic-gradient(from var(--angle), red, yellow, red);
    animation: tourner 4s linear infinite;
}
@keyframes tourner { to { --angle: 360deg; } }          /* animation d'un dégradé */
```

> Baseline *widely available* (2024).

## 12.7 Pièges

| Problème | Explication |
| --- | --- |
| Valeur invalide sans erreur visible | Une variable invalide rend la propriété **« invalide au moment du calcul »** (`unset`) : vérifier dans les DevTools |
| Pas utilisable dans les **requêtes média** | `@media (min-width: var(--x))` ❌ ; utilisez les requêtes de **conteneur** ou des valeurs fixes |
| Noms **sensibles à la casse** | `--Couleur` ≠ `--couleur` |
| Variables et `calc()` | Mettre des **unités** : `calc(var(--n) * 1px)` si `--n` est un nombre |

---

# 13. Transitions, animations et transformations

## 13.1 Transitions

Une **transition** anime le **passage** d'une valeur à une autre quand elle change (survol, focus, classe ajoutée).

```css
.bouton {
    background: royalblue;
    transition: background-color .3s ease, transform .2s ease-out;
    /*          propriété         durée  fonction  (délai) */
}
.bouton:hover { background: navy; transform: translateY(-2px); }
```

| Propriété | Rôle |
| --- | --- |
| `transition-property` | Propriétés animées (`all` à éviter : liste explicite) |
| `transition-duration` | Durée (`.3s`, `300ms`) |
| `transition-timing-function` | `ease`, `linear`, `ease-in`, `ease-out`, `ease-in-out`, `cubic-bezier(…)`, **`steps()`**, **`linear(…)`** (courbes à points : ressorts, rebonds) |
| `transition-delay` | Délai |
| `transition-behavior` | `allow-discrete` : permet de transitionner `display`, `overlay`… (voir 13.4) |

```css
.ressort { transition: transform .6s linear(0, .6 18%, 1.05 36%, .98 54%, 1 72%, 1); }     /* courbe d'accélération « ressort » */
```

## 13.2 Animations par images clés : `@keyframes`

```css
@keyframes apparition {
    from { opacity: 0; transform: translateY(1rem); }
    to   { opacity: 1; transform: none; }
}

@keyframes pulsation {
    0%, 100% { transform: scale(1); }
    50%      { transform: scale(1.1); }
}

.carte { animation: apparition .5s ease-out both; }
.coeur { animation: pulsation 1.2s ease-in-out infinite; }
```

### Propriétés d'animation

| Propriété | Valeurs |
| --- | --- |
| `animation-name` | Nom du `@keyframes` |
| `animation-duration` | `1s`, `300ms` |
| `animation-timing-function` | Comme les transitions |
| `animation-delay` | Délai (négatif = démarre « en cours ») |
| `animation-iteration-count` | `1`, `3`, `infinite` |
| `animation-direction` | `normal`, `reverse`, `alternate`, `alternate-reverse` |
| `animation-fill-mode` | `none`, `forwards` (garde l'état final), `backwards`, `both` |
| `animation-play-state` | `running`, `paused` |
| `animation-composition` | `replace`, `add`, `accumulate` |
| `animation-timeline` | `auto`, **`scroll()`**, **`view()`** (voir 13.7) |
| **`animation`** (raccourci) | `nom durée fonction délai répétition direction remplissage` |

```css
.chargement { animation: tourner 1s linear infinite; }
@keyframes tourner { to { transform: rotate(1turn); } }
```

## 13.3 Transformations

```css
.element {
    transform: translate(20px, 10px) rotate(15deg) scale(1.2) skew(10deg);       /* ordre important : appliqué de droite à gauche */
    transform-origin: top left;                                                   /* point d'ancrage (centre par défaut) */
}

/* ✅ Propriétés de transformation INDIVIDUELLES (plus simples à animer séparément) */
.moderne { translate: 20px 10px; rotate: 15deg; scale: 1.2; }
.moderne:hover { scale: 1.3; }
```

| Fonction | Rôle |
| --- | --- |
| `translate(x, y)`, `translateX()`, `translateY()`, `translateZ()` | Déplacer |
| `rotate(angle)` (`rotateX/Y/Z`) | Pivoter |
| `scale(x, y)` | Redimensionner |
| `skew(x, y)` | Incliner |
| `matrix()`, `matrix3d()` | Combinaison |

### 3D

```css
.scene { perspective: 800px; }
.carte3d { transform-style: preserve-3d; transition: transform .6s; }
.carte3d:hover { transform: rotateY(180deg); }
.face { backface-visibility: hidden; }
```

## 13.4 Animer l'apparition et la disparition (`display: none`) *(ajout, à jour)*

Jusqu'à récemment, animer un élément **de `display: none` à visible** exigeait du JavaScript. Trois outils le permettent désormais :

```css
.panneau {
    opacity: 1;
    transform: none;
    transition: opacity .3s, transform .3s, display .3s allow-discrete;       /* display devient « animable » (discret) */

    @starting-style {                                                          /* état de DÉPART à l'apparition */
        opacity: 0;
        transform: translateY(1rem);
    }
}
.panneau.cache {
    display: none;
    opacity: 0;
    transform: translateY(1rem);
}
```

- **`@starting-style`** : définit les valeurs **initiales** d'un élément qui vient d'être inséré ou affiché (Baseline *newly available*).
- **`transition-behavior: allow-discrete`** : autorise les transitions de propriétés **discrètes** comme `display` et `overlay`.
- Applicable aux `<dialog>` et éléments **`popover`** (section 24).

### Animer vers `height: auto` *(support récent)*

```css
:root { interpolate-size: allow-keywords; }       /* Chromium : permet de transitionner height: auto */
.accordeon { height: 0; overflow: clip; transition: height .3s; }
.accordeon.ouvert { height: auto; }
```

## 13.5 Performance des animations

| Bon (composition GPU) | Mauvais (déclenche la mise en page) |
| --- | --- |
| `transform` (`translate`, `rotate`, `scale`) | `width`, `height`, `margin`, `top`, `left` |
| `opacity` | `box-shadow` (repeinture) animé à grande échelle |
| `filter` (avec prudence) | |

```css
.mobile { will-change: transform; }          /* ⚠️ à utiliser avec parcimonie, uniquement pour des éléments qui vont VRAIMENT s'animer */
```

- Animez **`transform` et `opacity`** de préférence.
- Évitez `transition: all` : listez les propriétés.
- Limitez le nombre d'éléments animés simultanément.

## 13.6 Respecter les préférences : mouvement réduit *(ajout)*

```css
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: .01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: .01ms !important;
        scroll-behavior: auto !important;
    }
}
/* ou, plus fin : n'activer les animations que pour les utilisateurs qui les acceptent */
@media (prefers-reduced-motion: no-preference) {
    .carte { animation: apparition .5s ease-out both; }
}
```

> ♿ Les animations de **mouvement** (translation, zoom, parallaxe) peuvent provoquer des **malaises** (troubles vestibulaires) : respectez toujours cette préférence.

## 13.7 Animations liées au défilement *(ajout)*

Les **animations pilotées par le défilement** (*scroll-driven animations*) lient la **progression** d'une animation à la **position de défilement** (ou à la visibilité d'un élément), **sans JavaScript**.

```css
/* Barre de progression de lecture */
.progression {
    position: fixed; inset: 0 0 auto 0; height: 4px; background: royalblue;
    transform-origin: left;
    animation: grandir linear;
    animation-timeline: scroll(root block);              /* liée au défilement de la page */
}
@keyframes grandir { from { transform: scaleX(0); } to { transform: scaleX(1); } }

/* Apparition quand un élément entre dans la fenêtre */
.revele {
    animation: apparition linear both;
    animation-timeline: view();                          /* liée à la visibilité de l'élément */
    animation-range: entry 0% cover 40%;                 /* sur quelle portion de la visibilité */
}
```

> ⚠️ Support : Chromium et Safari ; Firefox à vérifier selon la version. **Amélioration progressive** : entourez de `@supports (animation-timeline: scroll())` et prévoyez un état final lisible sans animation.

## 13.8 Transitions de vue (*View Transitions*) *(ajout)*

Animations fluides **entre deux états de page** (changement de contenu, navigation) avec très peu de code :

```js
document.startViewTransition(() => mettreAJourLeDOM());       // même document
```

```css
::view-transition-old(root) { animation: .3s ease-out both fondu-sortie; }
::view-transition-new(root) { animation: .3s ease-in both fondu-entree; }

.vignette { view-transition-name: image-produit; }            /* l'élément « voyage » entre les deux états */

@view-transition { navigation: auto; }                         /* navigations entre pages du même site (multi-pages) */
```

> Transitions **dans le même document** : Baseline (2025). Transitions **entre documents** (`@view-transition`) : support en cours d'extension.

---

# 14. Design responsive

## 14.1 Principes

Le **design responsive** adapte une page à toutes les tailles d'écran **avec le même code**. Il repose sur :

1. **Mise en page fluide** (pourcentages, `fr`, `minmax`, `clamp`).
2. **Images et médias flexibles**.
3. **Requêtes média** et **requêtes de conteneur**.
4. L'approche **mobile d'abord** (*mobile-first*).

## 14.2 La balise `viewport`

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Sans elle, les mobiles affichent la page comme sur un écran de bureau (« dézoomée »). **Ne désactivez pas le zoom** (`user-scalable=no`, `maximum-scale=1`) : problème d'accessibilité.

## 14.3 Requêtes média (*media queries*)

```css
/* Mobile d'abord : styles de base pour les petits écrans… */
.conteneur { padding: 1rem; }

/* …puis on ENRICHIT avec min-width */
@media (min-width: 48rem) {                        /* ≥ 768px */
    .conteneur { padding: 2rem; display: grid; grid-template-columns: 1fr 2fr; }
}
@media (min-width: 64rem) {                        /* ≥ 1024px */
    .conteneur { max-width: 70rem; margin-inline: auto; }
}
```

### Syntaxe d'intervalle *(à jour)*

```css
@media (width >= 48rem) { }                        /* équivaut à (min-width: 48rem) */
@media (width < 40rem) { }
@media (40rem <= width <= 64rem) { }
@media (400px <= width <= 700px) { }
```

### Types de requêtes

| Critère | Exemple |
| --- | --- |
| Taille | `width`, `height`, `aspect-ratio`, `orientation: landscape` |
| Support | `print`, `screen`, `@media print { }` |
| **Préférences** | `prefers-color-scheme: dark`, `prefers-reduced-motion: reduce`, `prefers-contrast: more`, `prefers-reduced-transparency`, `forced-colors: active` |
| **Capacités** | `hover: hover`, `pointer: coarse` (tactile), `any-hover` |
| Résolution | `resolution >= 2dppx` (écrans HD) |

```css
@media (hover: hover) { .lien:hover { text-decoration: underline; } }       /* survol uniquement sur appareils qui le permettent */
@media (pointer: coarse) { .bouton { min-height: 3rem; } }                   /* cibles tactiles plus grandes */
@media print { nav, footer { display: none; } a::after { content: " (" attr(href) ")"; } }
```

## 14.4 Points de rupture (*breakpoints*)

| Taille | Largeur indicative | Appareil |
| --- | --- | --- |
| Petit | < 40 rem (640 px) | Téléphones |
| Moyen | ≥ 48 rem (768 px) | Tablettes |
| Grand | ≥ 64 rem (1024 px) | Portables |
| Très grand | ≥ 80 rem (1280 px) | Bureau |

> ✅ **Choisissez les points de rupture selon votre contenu** (quand la mise en page « casse »), pas selon des appareils précis. Exprimez-les en **`rem`/`em`** (respecte le zoom du texte).

## 14.5 Requêtes de conteneur : `@container` *(ajout, à jour)*

Les **requêtes de conteneur** adaptent un composant à la taille de **son conteneur** (et non de la fenêtre) : un même composant fonctionne dans une barre latérale étroite comme dans la zone principale.

```css
.carte-conteneur { container-type: inline-size; container-name: carte; }       /* déclare un conteneur */

.carte { display: grid; gap: 1rem; }

@container carte (min-width: 30rem) {                       /* selon la largeur du conteneur */
    .carte { grid-template-columns: 10rem 1fr; }
}
@container (width < 20rem) { .carte img { display: none; } }

.titre { font-size: clamp(1rem, 4cqi, 1.75rem); }           /* unités de conteneur : cqi = 1 % de la largeur du conteneur */
```

| Élément | Rôle |
| --- | --- |
| `container-type: inline-size` | Conteneur de **taille** sur l'axe en ligne (largeur) ✅ ; `size` = les deux axes ; `normal` = pour les requêtes de style |
| `container-name` | Nom (facultatif) |
| `container: carte / inline-size` | Raccourci |
| `@container (…)` | Requête de taille |
| `cqw`, `cqh`, `cqi`, `cqb`, `cqmin`, `cqmax` | Unités relatives au conteneur |
| `@container style(--theme: sombre)` | **Requêtes de style** sur les variables (support en progression) |
| `@container scroll-state(stuck: top)` | Requêtes sur l'**état de défilement** (collé, accroché ; Chromium) |

> ✅ **Requêtes de taille de conteneur** : Baseline *widely available* depuis 2023. **Media queries** pour la **mise en page globale**, **container queries** pour les **composants**.

## 14.6 Unités et mises en page fluides

```css
.conteneur { width: min(100% - 2rem, 70rem); margin-inline: auto; }      /* largeur max, marges latérales automatiques */
.grille { grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr)); }     /* aucune media query */
h1 { font-size: clamp(2rem, 1rem + 4vw, 4rem); }                        /* typographie fluide */
.section { padding-block: clamp(2rem, 6vw, 6rem); }
```

## 14.7 Images et vidéos responsives

```html
<!-- Choisir la bonne taille selon l'écran -->
<img src="image-800.jpg"
     srcset="image-400.jpg 400w, image-800.jpg 800w, image-1600.jpg 1600w"
     sizes="(min-width: 60rem) 50vw, 100vw"
     alt="Description" width="800" height="600" loading="lazy" decoding="async">

<!-- Direction artistique et formats modernes -->
<picture>
    <source media="(min-width: 60rem)" srcset="large.avif" type="image/avif">
    <source srcset="petit.webp" type="image/webp">
    <img src="petit.jpg" alt="Description" width="400" height="300">
</picture>
```

```css
img, video, svg { max-width: 100%; height: auto; }
.video { aspect-ratio: 16 / 9; width: 100%; }
.fond { background-image: image-set(url("fond.avif") type("image/avif"), url("fond.jpg") type("image/jpeg")); }
```

> 💡 Renseignez toujours **`width` et `height`** (ou `aspect-ratio`) sur les images : cela évite les **décalages de mise en page** (CLS). `loading="lazy"` pour les images hors écran.

## 14.8 Tableaux et grilles sur mobile

```css
.tableau { overflow-x: auto; }                           /* défilement horizontal */
.menu { display: flex; flex-wrap: wrap; gap: .5rem; }
```

## 14.9 Tester

- **Mode appareil** des DevTools (Ctrl+Maj+M), redimensionnement, zoom 200 %, taille de police augmentée.
- Tester sur de **vrais appareils** (iOS Safari, Android Chrome).
- Vérifier **portrait / paysage**, **tactile**, **mode sombre**, **mouvement réduit**.

---

# 15. Fonctionnalités modernes

*(Section ajoutée : le CSS a beaucoup évolué depuis 2022. Chaque fonctionnalité est déjà détaillée dans sa section thématique ; voici une vue d'ensemble.)*

## 15.1 Tableau de synthèse

| Fonctionnalité | Rôle | Statut approximatif (octobre 2026) |
| --- | --- | --- |
| **Imbrication** (`&`) | Imbriquer les règles sans préprocesseur | ✅ Largement disponible |
| **`:has()`** | Sélecteur « parent » | ✅ Largement disponible |
| **`@layer`** | Couches de cascade | ✅ Largement disponible |
| **Requêtes de conteneur** (taille) | Composants adaptatifs | ✅ Largement disponible |
| **Subgrid** | Grilles imbriquées alignées | ✅ Largement disponible |
| **Propriétés logiques** | Sens d'écriture | ✅ Largement disponible |
| `color-mix()`, `oklch()`, syntaxe de couleur relative | Couleurs modernes | ✅ Largement / récemment disponible |
| `light-dark()` | Valeur selon le thème | ✅ Disponible |
| `text-wrap: balance / pretty` | Typographie | ✅ Disponible |
| `@starting-style`, `transition-behavior` | Animer `display` | ✅ Disponible (récent) |
| `@property` | Variables typées / animables | ✅ Disponible |
| **Transitions de vue** (même document) | Animations d'interface | ✅ Disponible |
| **`@scope`** | Portée des styles | ✅ Récemment disponible (2026) |
| **Positionnement par ancrage** | Infobulles, menus sans JS | ✅ Récemment disponible (début 2026, noyau) |
| `sibling-index()` / `sibling-count()` | Mise en page selon la position | ✅ Récemment disponible |
| **Animations liées au défilement** | Animations sans JS | ⚠️ Selon les navigateurs (vérifier) |
| `if()`, `@function`, mixins CSS | Logique conditionnelle, fonctions | ⚠️ Expérimental (Chromium) |
| `field-sizing`, `interpolate-size`, `corner-shape`, `contrast-color()`, `shape()` | Divers | ⚠️ Support partiel / récent |
| `masonry`, gap decorations, `reading-flow` | Mises en page avancées | ⚠️ En cours de standardisation |

## 15.2 Positionnement par ancrage (*Anchor Positioning*)

Attacher un élément flottant (infobulle, menu, popover) à un **autre élément**, **en CSS pur**, avec gestion des **débordements** de fenêtre :

```css
.bouton-menu { anchor-name: --menu; }

.menu {
    position: fixed;                                  /* ou absolute */
    position-anchor: --menu;                          /* lié à l'ancre */
    position-area: bottom span-right;                 /* placé sous l'ancre */
    margin-top: .25rem;
    position-try-fallbacks: flip-block, flip-inline;  /* se retourne s'il n'y a pas de place */
}
```

Combiné à l'attribut HTML **`popover`** (section 24), il remplace Floating UI / Popper.js dans de nombreux cas. Le **noyau** (`anchor-name`, `position-anchor`, `position-area`, `anchor()`) est Baseline *newly available* depuis janvier 2026 ; les fonctionnalités annexes (`anchor-scope`, certains `position-try`) peuvent varier : **vérifiez** et prévoyez une solution de repli.

## 15.3 `sibling-index()` et `sibling-count()`

```css
.liste > li {
    --i: sibling-index();                              /* 1, 2, 3… */
    transition-delay: calc(var(--i) * 50ms);           /* apparitions en cascade, sans variables manuelles */
}
.liste > li { rotate: calc((sibling-index() - 1) * 360deg / sibling-count()); }
```

## 15.4 Conditions, fonctions et mixins *(expérimental)*

```css
/* if() : valeur conditionnelle (support actuel : Chromium) */
.bouton { padding: if(media(width >= 48rem): 1.5rem; else: 1rem); }

/* @function : fonctions CSS personnalisées (Chromium) */
@function --double(--x) { result: calc(var(--x) * 2); }
.boite { width: --double(10px); }
```

> ⚠️ **Ne les utilisez que derrière `@supports`** ou comme amélioration progressive ; leur syntaxe peut encore évoluer.

## 15.5 Quand utiliser quoi (récapitulatif)

| Besoin | Fonctionnalité moderne | Remplace |
| --- | --- | --- |
| Styler un parent selon ses enfants | `:has()` | JavaScript |
| Imbriquer | Imbrication native | Sass (imbrication) |
| Contrôler l'ordre de priorité | `@layer` | `!important`, spécificité |
| Composant adaptatif | `@container` | Media queries + hacks |
| Aligner des contenus de cartes | `subgrid` | Hauteurs fixes, JS |
| Thème clair/sombre | `light-dark()` + `color-scheme` | Doublons de variables |
| Infobulle / menu positionné | Ancrage + `popover` | Floating UI, Popper.js |
| Animer l'apparition | `@starting-style` | JS avec `requestAnimationFrame` |
| Animation au défilement | `animation-timeline` | IntersectionObserver, bibliothèques |
| Couleurs dérivées | `color-mix()`, couleur relative | Sass `lighten()`/`darken()` |
| Texte équilibré | `text-wrap: balance` | Balises `<br>` manuelles |

---

# 16. Accessibilité et CSS

*(Section ajoutée : le CSS a un impact direct sur l'accessibilité.)*

## 16.1 Contraste et couleur

- **Contraste** minimal (WCAG AA) : **4,5 : 1** (texte normal), **3 : 1** (grand texte, composants d'interface).
- Ne transmettez **jamais une information par la seule couleur** (ajoutez icône, texte, motif).
- Testez avec les DevTools (outil de contraste) et en **niveaux de gris**.

```css
@media (prefers-contrast: more) { :root { --bordure: 2px solid currentColor; } }
@media (forced-colors: active) {                       /* mode Contraste élevé de Windows */
    .bouton { border: 1px solid ButtonText; }
}
```

## 16.2 Focus visible

```css
:focus-visible {
    outline: 3px solid var(--accent, royalblue);
    outline-offset: 3px;
}
:focus:not(:focus-visible) { outline: none; }        /* pas d'anneau au clic souris, présent au clavier */
```

> 🚫 **Ne retirez jamais l'indicateur de focus** sans le remplacer par un équivalent **visible**.

## 16.3 Cibles tactiles

```css
button, a.bouton, input { min-block-size: 2.75rem; min-inline-size: 2.75rem; }       /* ~44 px (WCAG 2.2 : au moins 24 px, 44 px recommandé) */
```

## 16.4 Masquer visuellement mais pas aux lecteurs d'écran

```css
.sr-only {                                           /* « visually hidden » */
    position: absolute;
    width: 1px; height: 1px;
    margin: -1px; padding: 0;
    overflow: hidden;
    clip-path: inset(50%);
    white-space: nowrap;
    border: 0;
}
```

| Technique | Visible | Lecteurs d'écran |
| --- | --- | --- |
| `.sr-only` | ❌ | ✅ |
| `display: none`, `hidden`, `visibility: hidden` | ❌ | ❌ |
| `aria-hidden="true"` | ✅ | ❌ |

## 16.5 Préférences utilisateur

| Préférence | Requête média |
| --- | --- |
| Mouvement réduit | `prefers-reduced-motion: reduce` |
| Thème sombre | `prefers-color-scheme: dark` |
| Contraste renforcé | `prefers-contrast: more` |
| Transparence réduite | `prefers-reduced-transparency: reduce` |
| Couleurs forcées | `forced-colors: active` |
| Taille de texte | Utiliser `rem` ; ne pas bloquer le zoom |

## 16.6 Le CSS peut changer le sens de lecture

- `order` (Flexbox), `grid-area`, `position` : changent l'ordre **visuel** mais **pas** l'ordre de **tabulation / lecture** : conservez un **ordre DOM logique**.
- `content` (`::before`/`::after`) peut être **lu** par certains lecteurs d'écran : n'y mettez pas d'information essentielle.
- `text-transform: uppercase` : certains lecteurs épellent ; privilégiez le HTML.

## 16.7 Liste de contrôle

- [ ] Contraste suffisant, information non portée par la couleur seule
- [ ] Focus **toujours visible**
- [ ] Taille de texte relative (`rem`), zoom 200 % sans perte de contenu
- [ ] `prefers-reduced-motion` respecté
- [ ] Cibles tactiles suffisantes
- [ ] Ordre visuel = ordre logique
- [ ] Éléments masqués avec la bonne technique

---

# 🛠️ Outils et pratique

---

# 17. Frameworks CSS

## 17.1 Pourquoi un framework ?

Un **framework CSS** fournit des **styles prêts à l'emploi** (grille, composants, utilitaires) pour développer plus vite avec une apparence cohérente.

| ✅ Avantages | ❌ Inconvénients |
| --- | --- |
| Développement rapide, design cohérent | Poids et dépendance au framework |
| Composants testés, responsive intégré | Sites qui se ressemblent (sans personnalisation) |
| Documentation et communauté | Courbe d'apprentissage des conventions |

> ✅ Le CSS moderne (Grid, Flexbox, variables, `@layer`, conteneurs) permet aujourd'hui de **se passer d'un framework** pour de nombreux projets.

## 17.2 Principaux frameworks

| Framework | Approche | Points forts |
| --- | --- | --- |
| **Bootstrap** (5.3) | **Composants** + grille + utilitaires | Très répandu, nombreux composants (modales, barres de navigation), **modes de couleur** (`data-bs-theme="dark"`), sans jQuery depuis la v5 |
| **Tailwind CSS** (v4) | **Utilitaires** (*utility-first*) : on compose les classes dans le HTML | Rapidité, cohérence, pas de CSS inutilisé, moteur **très rapide** |
| **Bulma**, **Pico CSS**, **Foundation** | Composants / CSS « sémantique » | Légers, simples |
| **UnoCSS** | Utilitaires générés à la demande | Souple, très rapide |
| **Open Props**, **Utopia** | **Variables / échelles** (design tokens) | Bases de design systèmes |
| **Material**, **shadcn/ui**, **Radix**, **DaisyUI** | Bibliothèques de composants | Selon l'écosystème |

## 17.3 Bootstrap (exemple)

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
<!-- version à ajuster ; avec un build : npm install bootstrap -->

<div class="container">
    <div class="row g-3">
        <div class="col-12 col-md-6 col-lg-4"><div class="card p-3">Carte 1</div></div>
        <div class="col-12 col-md-6 col-lg-4"><div class="card p-3">Carte 2</div></div>
    </div>
    <button class="btn btn-primary">Envoyer</button>
</div>
```

Grille en **12 colonnes**, points de rupture `sm`, `md`, `lg`, `xl`, `xxl`. Personnalisation par **variables CSS** (`--bs-primary`) ou par Sass.

## 17.4 Tailwind CSS v4 *(à jour)*

La version 4 est **configurée en CSS** (plus de `tailwind.config.js` obligatoire) et s'appuie sur les **couches de cascade**, les **variables CSS** et un moteur Rust.

```bash
npm install tailwindcss @tailwindcss/vite        # (ou @tailwindcss/postcss)
```

```css
/* app.css */
@import "tailwindcss";

@theme {                                     /* design tokens : générés en variables CSS */
    --color-marque: oklch(0.62 0.19 260);
    --font-titre: "Inter", sans-serif;
    --breakpoint-3xl: 120rem;
}
```

```html
<div class="mx-auto max-w-3xl rounded-lg bg-white p-6 shadow-md dark:bg-zinc-900">
    <h1 class="font-titre text-2xl font-bold text-marque">Bonjour</h1>
    <button class="mt-4 rounded bg-marque px-4 py-2 text-white hover:opacity-90 focus-visible:outline-2 md:px-6">Envoyer</button>
</div>
```

| Concept | Description |
| --- | --- |
| **Utilitaires** | `p-4`, `flex`, `grid`, `text-lg`… |
| **Variantes** | `hover:`, `focus-visible:`, `md:` (responsive), `dark:`, `group-hover:`, `@container` (`@md:`) |
| **`@theme`** | Définit couleurs, polices, espacements |
| **`@apply`** | Extrait des classes utilitaires dans une règle CSS (à utiliser avec modération) |
| **Purge automatique** | Seules les classes utilisées sont générées |

> ⚠️ Avantage : cohérence et vitesse ; inconvénient : HTML chargé de classes. Extraire des **composants** (framework JS, partiels) pour éviter la répétition.

## 17.5 Choisir

| Besoin | Choix |
| --- | --- |
| Prototype rapide avec composants prêts | **Bootstrap** |
| Design sur mesure, équipe à l'aise avec les utilitaires | **Tailwind** |
| Petit site, HTML sémantique | **Pico CSS** ou **CSS natif** |
| Design system maison | **CSS natif** + variables + `@layer` |

---

# 18. Préprocesseurs et outils de build

## 18.1 Préprocesseurs : Sass et Less

Un **préprocesseur** ajoute des fonctionnalités (variables, imbrication, fonctions, mixins, partiels) et **compile** vers du CSS standard.

| | **Sass / SCSS** | **Less** | **Stylus** |
| --- | --- | --- | --- |
| Popularité | ✅ La plus répandue | En déclin | Rare |
| Syntaxe | SCSS (proche de CSS) ou indentée | Proche de CSS | Souple |
| Compilateur | **Dart Sass** (`sass`) | `lessc` (JavaScript) | Node |

```scss
// _variables.scss
$couleur-principale: #3498db;
$points: (petit: 40rem, moyen: 48rem, grand: 64rem);

// _mixins.scss
@mixin a-partir-de($taille) {
    @media (min-width: map-get($points, $taille)) { @content; }
}

// style.scss
@use "variables" as *;                       // ✅ @use / @forward (le système de modules)
@use "mixins" as m;

.carte {
    color: $couleur-principale;
    &:hover { color: darken($couleur-principale, 10%); }
    @include m.a-partir-de(moyen) { padding: 2rem; }
}
```

```bash
npm install -D sass
npx sass --watch src/scss:dist/css          # compilation en continu
```

> 📌 **À jour** : `@import` de Sass est **déprécié** (remplacé par **`@use`** / **`@forward`**) ; **LibSass / node-sass** sont abandonnés : utilisez **Dart Sass**.

## 18.2 Le CSS natif remplace une partie des préprocesseurs

| Fonction de Sass | Équivalent CSS natif |
| --- | --- |
| Variables `$x` | **Propriétés personnalisées** `--x` (dynamiques, modifiables en JS) |
| Imbrication | **Imbrication native** `&` |
| `darken()`, `lighten()`, `mix()` | **`color-mix()`**, couleur relative |
| `calc`, `min`, `max`, `clamp` | Fonctions mathématiques natives |
| Partiels / modules | `@import` + `@layer`, ou outil de build |
| Mixins, fonctions, boucles, conditions | ❌ (partiellement `@function` / `if()` expérimentaux) → toujours utiles dans Sass |

> ✅ **Aujourd'hui**, Sass n'est plus **indispensable** ; il reste pertinent pour les **mixins, boucles, fonctions** et les bases de code existantes.

## 18.3 PostCSS, Lightning CSS et Autoprefixer

| Outil | Rôle |
| --- | --- |
| **PostCSS** | Plateforme de **transformations JS** du CSS (plugins) |
| **Autoprefixer** | Ajoute les **préfixes** nécessaires selon `browserslist` |
| **postcss-preset-env** | Transpile le CSS moderne pour des navigateurs plus anciens |
| **Lightning CSS** | Outil **très rapide (Rust)** : minification, préfixes, transpilation, imbrication, regroupement |
| **cssnano** | Minification |
| **Vite / webpack / esbuild** | Outils de build qui intègrent la plupart de ces fonctions |

```json
// package.json — navigateurs ciblés
{ "browserslist": [">= 0.5%", "last 2 versions", "not dead"] }
```

```js
// postcss.config.js
export default { plugins: { "postcss-preset-env": { stage: 2 }, autoprefixer: {}, cssnano: {} } };
```

## 18.4 Un flux de travail moderne

```text
CSS moderne (imbrication, @layer, variables…)
        │
   Vite / Lightning CSS (build)
        │  ├─ imbrication transpilée si nécessaire
        │  ├─ préfixes selon browserslist
        │  └─ minification + regroupement
        ▼
   CSS optimisé (+ compression Brotli)
```

---

# 19. Organiser son CSS

## 19.1 Les problèmes du CSS à grande échelle

Portée **globale**, conflits de noms, **spécificité** qui monte, code mort impossible à supprimer. Plusieurs **méthodologies** y répondent.

## 19.2 Méthodologies de nommage et d'architecture

| Méthode | Principe | Exemple |
| --- | --- | --- |
| **BEM** (Block Element Modifier) | Convention de nommage **plate** | `.carte`, `.carte__titre`, `.carte--mise-en-avant` |
| **OOCSS** | Séparer **structure** et **apparence** ; réutiliser des « objets » | `.media`, `.btn` + `.btn-primaire` |
| **SMACSS** | Catégories : Base, Layout, Module, State, Theme | `.is-active`, `.l-grille` |
| **ITCSS** | Couches du plus **générique** au plus **spécifique** (Settings → Tools → Generic → Elements → Objects → Components → Utilities) | Se réalise avec **`@layer`** |
| **Utility-first** (Tailwind) | Classes utilitaires atomiques | `p-4 flex gap-2` |
| **CSS Modules** | Classes **locales** à un composant (noms générés au build) | `styles.carte` |
| **CSS-in-JS** | Styles dans le JavaScript | Voir ci-dessous |

### BEM en pratique

```css
.carte { border: 1px solid #ddd; }
.carte__titre { font-size: 1.25rem; }
.carte__image { aspect-ratio: 16 / 9; object-fit: cover; }
.carte--mise-en-avant { border-color: gold; }
```

```html
<article class="carte carte--mise-en-avant">
    <img class="carte__image" src="…" alt="">
    <h2 class="carte__titre">Titre</h2>
</article>
```

### CSS-in-JS : état des lieux

- **Exécution** (*runtime*) : styled-components, Emotion : pratiques mais **coût de performance**, compatibilité avec les **composants serveur** limitée ; **styled-components est passé en mode maintenance** (annonce des mainteneurs en 2025).
- **À la compilation** (*zero-runtime*) : Vanilla Extract, Panda CSS, StyleX, Linaria : CSS extrait au build.
- Tendance : **CSS natif + CSS Modules**, ou **utilitaires**.

## 19.3 L'architecture moderne : couches + portée

```css
@layer reset, tokens, base, layout, composants, utilitaires;

@layer composants {
    .carte {
        padding: var(--esp-3);

        @scope (.carte) { h2 { font-size: 1.25rem; } }       /* portée locale sans convention de nommage */
    }
}
```

## 19.4 Structure de fichiers

```text
styles/
├── main.css              ← @import des couches dans l'ordre (ou point d'entrée du bundler)
├── 00-reset.css
├── 01-tokens.css         ← variables : couleurs, espacements, typographie
├── 02-base.css           ← éléments HTML (body, a, h1…)
├── 03-layout.css         ← grilles, conteneurs
├── composants/
│   ├── bouton.css
│   ├── carte.css
│   └── modale.css
└── 99-utilitaires.css
```

## 19.5 Réinitialisation (*reset*)

```css
/* Reset moderne minimal */
*, *::before, *::after { box-sizing: border-box; }
* { margin: 0; }
html { -webkit-text-size-adjust: 100%; text-size-adjust: 100%; }
body { min-height: 100dvh; line-height: 1.5; -webkit-font-smoothing: antialiased; }
img, picture, video, canvas, svg { display: block; max-width: 100%; height: auto; }
input, button, textarea, select { font: inherit; color: inherit; }
p, h1, h2, h3, h4, h5, h6 { overflow-wrap: break-word; }
h1, h2, h3, h4 { text-wrap: balance; line-height: 1.2; }
p { text-wrap: pretty; }
:target { scroll-margin-block: 5ex; }
@media (prefers-reduced-motion: reduce) { html:focus-within { scroll-behavior: auto; } }
```

Alternatives : **normalize.css**, **modern-normalize**, **the-new-css-reset**.

## 19.6 Conventions d'équipe

- **Ordre des déclarations** cohérent (positionnement → modèle de boîte → typographie → visuel → divers), ou ordre alphabétique ; automatisé par **Stylelint** / Prettier.
- **Variables** pour tout ce qui se répète (couleurs, espacements, rayons, ombres).
- **Commentaires** de section, noms **explicites**.
- **Pas d'`!important`** (sauf utilitaires) ; sélecteurs **peu spécifiques**.
- Supprimer le **code mort** (voir l'outil *Coverage*, section 23).

```json
// .stylelintrc.json
{ "extends": ["stylelint-config-standard"], "rules": { "selector-class-pattern": null, "declaration-no-important": true } }
```

---

# 20. Performances et optimisation

## 20.1 Objectifs

Le CSS est **bloquant pour le rendu** : le navigateur n'affiche rien avant de l'avoir téléchargé et analysé. Un CSS **léger** et **bien livré** améliore le **LCP**, le **CLS** et l'**INP** (Core Web Vitals).

## 20.2 Réduire et livrer efficacement

| Technique | Effet |
| --- | --- |
| **Minification** (cssnano, Lightning CSS, Vite) | Supprime espaces et commentaires |
| **Compression** Brotli / gzip côté serveur | Divise la taille par 4 à 5 |
| **Supprimer le CSS inutilisé** (PurgeCSS, outils de build, Tailwind) | Moins de poids |
| **CSS critique** en ligne dans `<head>` + reste chargé **sans bloquer** | Meilleur premier affichage |
| **Cache longue durée** + noms hachés (`style.a1b2c3.css`) | Pas de re-téléchargement |
| **Préchargement** des ressources critiques (`rel="preload"`) | Polices, CSS critique |
| **Éviter `@import`** | Évite les chargements en série |
| **Découper** par page / route (CSS « code-splitting ») | Ne charge que le nécessaire |

> 📌 **À jour** : l'ancien conseil « regrouper tous les fichiers pour réduire les requêtes HTTP » est **moins important** avec **HTTP/2 et HTTP/3** (multiplexage). Regrouper reste utile pour la compression et la simplicité, mais n'est plus une règle absolue.

## 20.3 Performance de rendu

```css
.section-lourde {
    content-visibility: auto;                  /* ne rend pas ce qui est hors écran */
    contain-intrinsic-size: auto 600px;        /* taille réservée en attendant le rendu */
}
.widget { contain: layout paint; }             /* isole le calcul : un changement interne n'affecte pas le reste */
```

| Bonne pratique | Raison |
| --- | --- |
| **Animer `transform` / `opacity`** | Évite recalcul de mise en page et repeinture |
| Éviter `box-shadow`/`filter` animés sur de grandes surfaces | Coûteux (repeinture) |
| Limiter la **taille du DOM** | Moins de styles à calculer |
| `will-change` **ponctuel** | Évite la surconsommation de mémoire |
| Éviter la **« thrashing »** (JS qui lit puis écrit la mise en page en boucle) | Regroupe lectures et écritures |
| Réserver l'espace des images / polices (`width`/`height`, `size-adjust`) | Évite le CLS |
| `font-display: swap` / `optional` ; polices **WOFF2** variables | Texte rapide, moins de fichiers |

> 💡 **Mythe** : la complexité des sélecteurs (`div > ul li a`) a **très peu d'impact** sur les navigateurs modernes. Concentrez-vous sur la **taille du CSS**, la **mise en cache** et la **taille du DOM**.

## 20.4 Mesurer

- **Lighthouse** (DevTools) et **PageSpeed Insights** : LCP, CLS, INP, blocage du rendu.
- Onglet **Coverage** : pourcentage de CSS **non utilisé**.
- Onglet **Performance** : recalcul de styles, mise en page, repeinture.
- **WebPageTest**, **Web Vitals** (extension).

---

# 21. Compatibilité entre navigateurs

## 21.1 L'état des lieux

Les moteurs majeurs (**Blink** : Chrome/Edge ; **WebKit** : Safari ; **Gecko** : Firefox) convergent grâce au programme **Interop**. Le projet **Baseline** résume la disponibilité d'une fonctionnalité :

| Étiquette | Signification |
| --- | --- |
| **Newly available** | Disponible dans les **dernières versions** de tous les navigateurs majeurs |
| **Widely available** | Disponible depuis **au moins 30 mois** : utilisable sans précaution pour la plupart des sites |
| *Limited availability* | Pas encore dans tous les navigateurs : **amélioration progressive** |

Sources : **MDN**, **caniuse.com**, **web.dev/baseline**.

## 21.2 Amélioration progressive et `@supports`

Écrivez d'abord un style **de base qui fonctionne partout**, puis **enrichissez** pour les navigateurs capables :

```css
/* Repli : la déclaration non comprise est simplement ignorée */
.carte {
    background: #4a6cf7;                                         /* repli */
    background: oklch(60% 0.2 260);                              /* moderne : ignoré par les navigateurs qui ne le comprennent pas */
    width: 100%;
    width: min(100%, 60rem);
}

/* Requêtes de fonctionnalité */
@supports (display: grid) { .galerie { display: grid; } }
@supports not (backdrop-filter: blur(1px)) { .verre { background: rgb(255 255 255 / .9); } }
@supports selector(:has(*)) { .carte:has(img) { padding: 0; } }
@supports (animation-timeline: scroll()) { .revele { animation-timeline: view(); } }
@supports (position-anchor: --x) { .menu { position-anchor: --menu; } }
```

> ⚠️ Un sélecteur ou un bloc **invalide** invalide **toute la règle** : n'écrivez pas `:is(:has-inconnu, .a)` dans une liste commune ; utilisez `@supports selector(…)`.

## 21.3 Préfixes de fournisseurs *(à jour)*

Les préfixes (`-webkit-`, `-moz-`, `-ms-`) étaient utilisés pour les fonctionnalités **expérimentales**. Les navigateurs ont **abandonné** cette pratique : on active désormais par **drapeaux**. Il reste quelques préfixes courants :

| Préfixe encore utile | Usage |
| --- | --- |
| `-webkit-line-clamp` (+ `-webkit-box`) | Troncature multiligne |
| `-webkit-text-size-adjust` | Mobile |
| `-webkit-background-clip: text` | Texte dégradé |
| `-webkit-backdrop-filter` | Anciennes versions de Safari |
| `-webkit-mask-*` | Anciennes versions |

**Ne les écrivez pas à la main** : laissez **Autoprefixer** / **Lightning CSS** (selon `browserslist`) les ajouter.

## 21.4 Réinitialisation et différences de style par défaut

Les navigateurs ont des **feuilles de style par défaut** différentes : un **reset** (section 19.5) ou **normalize** les harmonise. Éléments de formulaire : `font: inherit`, `appearance: none` (avec prudence).

## 21.5 Tester

- **DevTools** : émulation de préférences (`prefers-*`), mode appareil.
- **Navigateurs réels** : Chrome, Firefox, Safari (macOS **et iOS** : indispensable), Edge.
- Services : **BrowserStack**, **LambdaTest**, **Playwright** (tests visuels multi-moteurs).
- **Stylelint** + `stylelint-no-unsupported-browser-features` (selon `browserslist`).

## 21.6 Navigateurs anciens

- Définir une **politique de support** (`browserslist`) fondée sur vos **statistiques d'audience**.
- Internet Explorer est **abandonné** (fin de support en 2022) : ne le prenez plus en charge.
- Pour les anciens navigateurs : **repli lisible** plutôt que rendu identique (principe d'**amélioration progressive**).

---

# 22. CSS et JavaScript

## 22.1 Modifier les styles

```js
const el = document.querySelector(".carte");

// 1) Classes (✅ méthode recommandée : le CSS reste dans la feuille de style)
el.classList.add("active");
el.classList.remove("cachee");
el.classList.toggle("ouverte");
el.classList.contains("active");
el.classList.replace("ancienne", "nouvelle");

// 2) Style en ligne (valeurs dynamiques)
el.style.color = "tomato";
el.style.backgroundColor = "rgb(0 0 0 / .1)";          // camelCase
el.style.cssText = "color: red; margin: 0;";
el.style.removeProperty("color");

// 3) Variables CSS (✅ idéal pour passer des valeurs dynamiques au CSS)
el.style.setProperty("--progression", "70%");
document.documentElement.style.setProperty("--couleur-principale", "tomato");
```

```css
.barre { width: var(--progression, 0%); transition: width .3s; }
```

## 22.2 Lire les styles

```js
const styles = getComputedStyle(el);                      // valeurs CALCULÉES (lecture seule)
styles.getPropertyValue("--couleur-principale");
styles.width;                                             // "320px"

el.getBoundingClientRect();                               // position et taille à l'écran
el.offsetWidth; el.clientHeight; el.scrollHeight;
```

> ⚠️ Lire des dimensions **puis** modifier le style **en boucle** force des recalculs de mise en page (*layout thrashing*) : regroupez lectures et écritures, ou utilisez `requestAnimationFrame`.

## 22.3 Requêtes média et fonctionnalités en JavaScript

```js
const sombre = matchMedia("(prefers-color-scheme: dark)");
sombre.addEventListener("change", (e) => appliquerTheme(e.matches ? "sombre" : "clair"));

matchMedia("(prefers-reduced-motion: reduce)").matches;
CSS.supports("display", "grid");                          // true / false
CSS.supports("selector(:has(*))");
```

## 22.4 Animations en JavaScript

```js
// Web Animations API : les mêmes moteurs que les animations CSS, pilotables par JS
const animation = el.animate(
    [{ transform: "translateY(20px)", opacity: 0 }, { transform: "none", opacity: 1 }],
    { duration: 400, easing: "ease-out", fill: "both" },
);
animation.pause(); animation.play(); animation.reverse();
animation.finished.then(() => console.log("terminé"));

el.addEventListener("transitionend", () => { /* fin d'une transition CSS */ });
el.addEventListener("animationend", () => { /* fin d'une animation CSS */ });
```

Autres outils : `IntersectionObserver` (déclencher selon la visibilité), `ResizeObserver` (réagir aux tailles), `requestAnimationFrame`, `document.startViewTransition()`.

## 22.5 Feuilles de style dynamiques

```js
const feuille = new CSSStyleSheet();
feuille.replaceSync(".nouveau { color: red; }");
document.adoptedStyleSheets = [...document.adoptedStyleSheets, feuille];        // partageable avec les Shadow DOM

CSS.registerProperty({ name: "--angle", syntax: "<angle>", inherits: false, initialValue: "0deg" });   // équivalent de @property
```

## 22.6 Dialogues, popovers et état en HTML

Le HTML moderne gère déjà ouverture/fermeture, focus et couche supérieure : le CSS ne fait que **styler** les états (`:modal`, `:popover-open`, `[open]`).

```js
dialogue.showModal();  dialogue.close();
menu.togglePopover();  menu.showPopover();  menu.hidePopover();
```

## 22.7 Bonnes pratiques

- **Basculer des classes** plutôt que manipuler `style` directement.
- Utiliser les **variables CSS** comme **interface** entre JS et CSS.
- Préférer les **animations CSS / WAAPI** aux animations par `setInterval`.
- Respecter `prefers-reduced-motion` dans le code JS aussi.

---

# 23. Outils de développement

## 23.1 Les DevTools du navigateur (F12)

| Panneau / outil | Usage |
| --- | --- |
| **Éléments** → **Styles** | Voir et **modifier en direct** les règles appliquées ; déclarations **barrées** = surchargées |
| **Calculé** (*Computed*) | Valeur **finale** de chaque propriété et la règle d'origine |
| **Modèle de boîte** | Visualisation des marges, bordures, paddings |
| **Superpositions Flexbox / Grid** | Badges `flex` / `grid` dans l'arbre DOM : affichage des axes, lignes, zones, gouttières |
| **Conteneurs** | Badge `container` : voir les conteneurs de requêtes et leur taille |
| **Couches** (*Layers*) | Ordre des couches de cascade |
| **Sélecteur d'état** (`:hov`) | Forcer `:hover`, `:focus`, `:active`, `:focus-visible`… |
| **Rendu** (*Rendering*) | **Émuler** `prefers-color-scheme`, `prefers-reduced-motion`, `forced-colors`, vision des couleurs (daltonisme), `print` |
| **Appareils** (Ctrl+Maj+M) | Mode responsive, capteurs, réseau |
| **Animations** | Inspecter et ralentir les animations / transitions |
| **Couverture** (*Coverage*) | % de **CSS inutilisé** |
| **Performance / Lighthouse** | Mesures de rendu et Core Web Vitals |
| **Accessibilité** | Arbre d'accessibilité, contraste |

### Astuces

- **Ctrl+clic** sur une propriété dans le panneau Styles : aller à sa définition.
- **Clic sur un nuancier** : sélecteur de couleur avec vérification du **contraste**.
- Éditeur d'**ombres**, de **dégradés**, de **courbes d'animation** (`cubic-bezier`, `linear()`).
- Ajouter une règle de test : bouton « + » (nouvelle règle de style) ; *Copier → Copier le style*.
- Les modifications des DevTools **ne sont pas enregistrées** : reportez-les dans votre code (ou activez les **Espaces de travail**).

## 23.2 Débogage de la mise en page

```css
/* Outline temporaire pour visualiser les boîtes */
* { outline: 1px solid rgb(255 0 0 / .3); }
```

| Symptôme | Pistes |
| --- | --- |
| Style non appliqué | Sélecteur incorrect, **spécificité**, ordre, faute de frappe (propriété barrée dans *Styles*) |
| Élément « déborde » | `box-sizing`, `min-width: 0` (flex), largeur fixe |
| Marges bizarres | **Fusion de marges**, `display` de l'élément |
| `z-index` sans effet | **Contexte d'empilement**, `position` manquant |
| `sticky` ne colle pas | `top` manquant, ancêtre avec `overflow` |
| Hauteur 100 % ne marche pas | La hauteur du parent doit être définie (ou utiliser `min-height: 100dvh`, Flexbox/Grid) |

## 23.3 Éditeurs et extensions

| Outil | Apport |
| --- | --- |
| **VS Code** | Complétion CSS, aperçu des couleurs, **Emmet** (`div.carte>h2+p` + Tab), Live Server |
| **Stylelint** | Analyse et corrections automatiques |
| **Prettier** | Formatage |
| **Tailwind CSS IntelliSense** | Complétion pour Tailwind |
| **CSS Peek**, **Intellisense for CSS class names** | Navigation entre HTML et CSS |
| **Can I use** (dans l'éditeur) | Compatibilité |

## 23.4 Ressources utiles

- **MDN Web Docs** : référence complète de CSS.
- **web.dev/learn/css** : cours gratuit de Google.
- **caniuse.com**, **web.dev/baseline** : compatibilité.
- **CSS-Tricks**, **Every Layout**, **Modern CSS Solutions**, **modern-css.com**.
- **Can I use… / MDN Browser Compatibility Data**.

---

# 24. Composants et projets

## 24.1 Carte

```html
<article class="carte">
    <img src="photo.jpg" alt="Description" width="400" height="250">
    <div class="carte__corps">
        <h2>Titre</h2>
        <p>Un court résumé de la carte.</p>
        <a class="bouton" href="#">Lire la suite</a>
    </div>
</article>
```

```css
.carte {
    --rayon: .75rem;
    display: grid;
    border-radius: var(--rayon);
    overflow: hidden;
    background: Canvas;
    box-shadow: 0 1px 3px rgb(0 0 0 / .12), 0 8px 24px rgb(0 0 0 / .08);
    transition: transform .2s, box-shadow .2s;

    &:hover { transform: translateY(-4px); }
    img { width: 100%; aspect-ratio: 16 / 10; object-fit: cover; }
    .carte__corps { padding: 1rem 1.25rem; display: grid; gap: .5rem; }
}
```

## 24.2 Bouton

```css
.bouton {
    --fond: royalblue;
    display: inline-flex; align-items: center; gap: .5em;
    padding: .6em 1.2em;
    border: 0; border-radius: .5rem;
    background: var(--fond); color: white;
    font: inherit; font-weight: 600; text-decoration: none; cursor: pointer;
    transition: background-color .2s, transform .1s;

    &:hover { background: color-mix(in oklch, var(--fond), black 15%); }
    &:active { transform: scale(.98); }
    &:focus-visible { outline: 3px solid var(--fond); outline-offset: 3px; }
    &[disabled], &[aria-disabled="true"] { opacity: .5; cursor: not-allowed; }
    &.danger { --fond: crimson; }
}
```

## 24.3 Modale avec `<dialog>`

```html
<button onclick="document.querySelector('#modale').showModal()">Ouvrir</button>

<dialog id="modale">
    <h2>Confirmer</h2>
    <p>Voulez-vous continuer ?</p>
    <form method="dialog"><button>Annuler</button><button value="ok">OK</button></form>
</dialog>
```

```css
dialog {
    border: 0; border-radius: 1rem; padding: 1.5rem; max-width: min(90vw, 30rem);
    opacity: 0; translate: 0 1rem;
    transition: opacity .25s, translate .25s, overlay .25s allow-discrete, display .25s allow-discrete;

    &[open] { opacity: 1; translate: 0; }
    @starting-style { &[open] { opacity: 0; translate: 0 1rem; } }
    &::backdrop { background: rgb(0 0 0 / .5); transition: background .25s, overlay .25s allow-discrete, display .25s allow-discrete; }
}
body:has(dialog[open]) { overflow: hidden; }            /* bloque le défilement de la page */
```

> ✅ `<dialog>` + `showModal()` fournit **gratuitement** : piégeage du focus, fermeture avec Échap, fond inerte, **couche supérieure** (pas de `z-index`).

## 24.4 Menu déroulant avec `popover` et ancrage

```html
<button popovertarget="menu" id="declencheur">Menu ▾</button>
<ul id="menu" popover>
    <li><a href="#">Profil</a></li>
    <li><a href="#">Paramètres</a></li>
</ul>
```

```css
#declencheur { anchor-name: --declencheur; }
#menu {
    position-anchor: --declencheur;
    position-area: bottom span-right;
    margin: .25rem 0 0; padding: .5rem; border-radius: .5rem; list-style: none;
    position-try-fallbacks: flip-block;
}
```

**Menu CSS seul (technique classique)** :

```css
.deroulant { position: relative; }
.deroulant .menu { display: none; position: absolute; inset-block-start: 100%; }
.deroulant:hover .menu,
.deroulant:focus-within .menu { display: block; }          /* :focus-within : accessible au clavier */
```

> ♿ `:hover` seul **n'est pas accessible** au clavier et au tactile : combinez avec `:focus-within`, ou préférez `popover` / `<details>`.

## 24.5 Accordéon avec `<details>`

```html
<details name="faq" open><summary>Question 1</summary><p>Réponse 1</p></details>
<details name="faq"><summary>Question 2</summary><p>Réponse 2</p></details>    <!-- même name = un seul ouvert à la fois -->
```

```css
details { border-block-end: 1px solid #ddd; }
summary { cursor: pointer; padding: .75rem 0; font-weight: 600; list-style: none; }
summary::after { content: "+"; float: right; }
details[open] summary::after { content: "−"; }
details::details-content { transition: height .3s, content-visibility .3s allow-discrete; height: 0; overflow: clip; }
details[open]::details-content { height: auto; }               /* avec interpolate-size: allow-keywords (Chromium) */
```

## 24.6 Interrupteur (case à cocher stylée)

```html
<label class="interrupteur"><input type="checkbox" role="switch"><span>Notifications</span></label>
```

```css
.interrupteur input {
    appearance: none; inline-size: 2.75rem; block-size: 1.5rem; border-radius: 1rem;
    background: #bbb; position: relative; cursor: pointer; transition: background .2s;

    &::after { content: ""; position: absolute; inset: 2px auto 2px 2px; aspect-ratio: 1; border-radius: 50%; background: white; transition: translate .2s; }
    &:checked { background: royalblue; }
    &:checked::after { translate: 1.25rem 0; }
    &:focus-visible { outline: 3px solid royalblue; outline-offset: 2px; }
}
```

## 24.7 Carrousel avec défilement par accroche (*scroll snap*)

```html
<div class="carrousel" tabindex="0" aria-label="Galerie">
    <figure><img src="1.jpg" alt="…"></figure>
    <figure><img src="2.jpg" alt="…"></figure>
    <figure><img src="3.jpg" alt="…"></figure>
</div>
```

```css
.carrousel {
    display: grid; grid-auto-flow: column; grid-auto-columns: 100%;
    overflow-x: auto; scroll-snap-type: x mandatory; scroll-behavior: smooth;
    overscroll-behavior-x: contain; scrollbar-width: thin;

    > figure { margin: 0; scroll-snap-align: center; }
    img { width: 100%; aspect-ratio: 16 / 9; object-fit: cover; }
}
```

> ✅ Cette approche (défilement **natif**, tactile, clavier) est **plus accessible** que l'ancienne technique « boutons radio `:checked` ». Chromium propose en plus des **pseudo-éléments de carrousel** (`::scroll-button()`, `::scroll-marker`) pour créer boutons et pastilles **sans JavaScript** (support partiel : à vérifier).

## 24.8 Barre de navigation responsive

```css
.nav { display: flex; flex-wrap: wrap; align-items: center; gap: 1rem; padding: 1rem; }
.nav ul { display: flex; gap: 1rem; list-style: none; padding: 0; margin: 0; margin-inline-start: auto; }
.nav a { padding: .5rem; text-decoration: none; }
.nav a[aria-current="page"] { font-weight: 700; text-decoration: underline; text-underline-offset: .3em; }

@media (max-width: 40rem) { .nav ul { flex-direction: column; width: 100%; margin: 0; } }
```

## 24.9 Mise en page de page complète

```css
body { display: grid; grid-template-rows: auto 1fr auto; min-height: 100dvh; }

.contenu {
    display: grid;
    grid-template-columns: [plein-debut] minmax(1rem, 1fr) [contenu-debut] minmax(0, 65ch) [contenu-fin] minmax(1rem, 1fr) [plein-fin];
}
.contenu > * { grid-column: contenu; }
.contenu > .pleine-largeur { grid-column: plein; }         /* éléments qui dépassent la colonne de lecture */
```

## 24.10 Projets suggérés

| Niveau | Projet | Compétences |
| --- | --- | --- |
| 🟢 | **Page de présentation / CV** | Typographie, boîte, Flexbox, variables |
| 🟢 | **Carte de profil + galerie** | Grid, `aspect-ratio`, survols, transitions |
| 🟡 | **Portfolio responsive** | Grid, mobile-first, requêtes de conteneur, thème sombre (`light-dark`) |
| 🟡 | **Tableau de bord** | Grid + subgrid, composants, tableaux responsives |
| 🟡 | **Système de design** (tokens, boutons, formulaires, modale, `@layer`) | Architecture, variables, accessibilité |
| 🔴 | **Page d'atterrissage animée** (sans JS) | `@keyframes`, animations liées au défilement, `@starting-style`, transitions de vue |
| 🔴 | **Bibliothèque de composants** (accordéon, onglets, carrousel, infobulles ancrées) | `popover`, ancrage, `:has()`, `@scope` |
| 🔴 | **Reproduire une interface existante** (pixel-perfect, responsive) | Analyse, Grid/Flexbox, précision |

---

# 25. Aide-mémoire et ressources

## 25.1 Recettes essentielles

| Besoin | Code |
| --- | --- |
| Centrer (2 axes) | `display: grid; place-items: center;` |
| Largeur de lecture centrée | `max-width: 65ch; margin-inline: auto;` |
| Conteneur avec marges latérales | `width: min(100% - 2rem, 70rem); margin-inline: auto;` |
| Colonnes responsive sans media query | `grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));` |
| Pied de page en bas | `body { min-height: 100dvh; display: grid; grid-template-rows: auto 1fr auto; }` |
| Espacer des enfants | `display: grid; gap: 1rem;` (ou flex + `gap`) |
| Image qui remplit sans déformer | `width: 100%; aspect-ratio: 16/9; object-fit: cover;` |
| Texte tronqué (1 ligne) | `white-space: nowrap; overflow: hidden; text-overflow: ellipsis;` |
| Titre équilibré | `text-wrap: balance;` |
| Carré / cercle | `aspect-ratio: 1; border-radius: 50%;` |
| Coller en haut au défilement | `position: sticky; top: 0;` |
| Superposer plein parent | `position: absolute; inset: 0;` |
| Thème clair/sombre | `:root { color-scheme: light dark; } … light-dark(clair, sombre)` |
| Anneau de focus clavier | `:focus-visible { outline: 3px solid royalblue; outline-offset: 2px; }` |
| Cacher visuellement (lecteurs d'écran) | classe `.sr-only` (section 16.4) |
| Défilement fluide respectueux | `@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }` |
| Composant adaptatif | `.parent { container-type: inline-size; } @container (min-width: 30rem) { … }` |

## 25.2 Ordre de lecture d'une déclaration de composant (suggestion)

```css
.composant {
    /* 1. Variables locales */   --fond: white;
    /* 2. Affichage / position */ display: grid; position: relative; inset: 0; z-index: 1;
    /* 3. Modèle de boîte */      width: 100%; margin-block: 1rem; padding: 1rem; border: 1px solid;
    /* 4. Typographie */          font: 1rem/1.5 system-ui; color: #222;
    /* 5. Visuel */               background: var(--fond); border-radius: .5rem; box-shadow: …;
    /* 6. Divers */               transition: …; cursor: pointer;
}
```

## 25.3 Les 12 règles d'or du CSS moderne

1. **`box-sizing: border-box`** partout.
2. Unités **relatives** (`rem`, `%`, `ch`, `fr`, `dvh`) ; `px` pour les fines bordures.
3. **Mobile d'abord**, points de rupture selon le contenu.
4. **Flexbox** pour une dimension, **Grid** pour deux ; **`gap`** pour espacer.
5. **Variables CSS** pour tout ce qui se répète (tokens).
6. **Sélecteurs simples**, classes plutôt qu'identifiants, **pas d'`!important`** ; `@layer` pour maîtriser la cascade.
7. **Propriétés logiques** (`inline` / `block`).
8. **Animez `transform` et `opacity`** ; respectez `prefers-reduced-motion`.
9. **Accessibilité** : contraste, focus visible, ordre logique, cibles tactiles.
10. **Amélioration progressive** : repli d'abord, `@supports` pour le reste.
11. **Mesurez** (DevTools, Lighthouse) avant d'optimiser.
12. **Vérifiez le support** (MDN, caniuse, Baseline) avant d'adopter une nouveauté.

## 25.4 Ressources pour progresser

- 📘 **MDN — CSS** : <https://developer.mozilla.org/fr/docs/Web/CSS>
- 🎓 **web.dev — Learn CSS** : <https://web.dev/learn/css>
- 🧭 **Spécifications du W3C (CSSWG)** : <https://www.w3.org/Style/CSS/>
- ✅ **Baseline** : <https://web.dev/baseline> · **Can I use** : <https://caniuse.com>
- 🧪 **CSS-Tricks**, **Every Layout**, **Modern CSS Solutions**, **Kevin Powell** (vidéos)
- 🎮 **Flexbox Froggy**, **Grid Garden**, **CSS Diner** (jeux d'apprentissage)

---

<div align="center">

*Bon style ! 🎨*

</div>
