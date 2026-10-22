<div align="center">

# JavaScript — Guide complet

**Des variables aux modules, du DOM à l'asynchrone et à Temporal**

*Mis à jour pour ECMAScript 2026 (octobre 2026)*

</div>

---

## Ressources

| Ressource | Lien |
| --- | --- |
| Exercices | [exercises](/language/exercises/javascript) |
| Solutions | [solutions](/language/solutions/javascript) |
| Projets | [projects](/language/projects/javascript) |
| Module : éditeur de code | [Monaco Editor](https://microsoft.github.io/monaco-editor/) |
| Référence officielle | [MDN Web Docs (fr)](https://developer.mozilla.org/fr/docs/Web/JavaScript) |
| Spécification | [ECMA-262](https://tc39.es/ecma262/) · [Propositions TC39](https://github.com/tc39/proposals) |

---

## Sommaire

1. [Introduction](#1-introduction)
2. [Variables et portée](#2-variables-et-portée)
3. [Types de valeurs](#3-types-de-valeurs)
4. [Opérateurs](#4-opérateurs)
5. [Chaînes de caractères](#5-chaînes-de-caractères)
6. [Nombres et `Math`](#6-nombres-et-math)
7. [Conditions et boucles](#7-conditions-et-boucles)
8. [Tableaux](#8-tableaux)
9. [Objets, `Map` et `Set`](#9-objets-map-et-set)
10. [`globalThis`](#10-globalthis)
11. [Expressions régulières](#11-expressions-régulières)
12. [Fonctions, portée et fermetures](#12-fonctions-portée-et-fermetures)
13. [Itérateurs et générateurs](#13-itérateurs-et-générateurs)
14. [`eval` et ses alternatives](#14-eval-et-ses-alternatives)
15. [Gestion des erreurs et mode strict](#15-gestion-des-erreurs-et-mode-strict)
16. [JavaScript asynchrone](#16-javascript-asynchrone)
17. [APIs web, `fetch` et JSON](#17-apis-web-fetch-et-json)
18. [Constructeurs, prototypes et héritage](#18-constructeurs-prototypes-et-héritage)
19. [Classes et programmation orientée objet](#19-classes-et-programmation-orientée-objet)
20. [Modules (`import` / `export`)](#20-modules-import--export)
21. [DOM et événements](#21-dom-et-événements)
22. [Environnement du navigateur (BOM) et stockage](#22-environnement-du-navigateur-bom-et-stockage)
23. [Dates et heures : `Date` et `Temporal`](#23-dates-et-heures--date-et-temporal)
24. [Outils et écosystème](#24-outils-et-écosystème)
25. [Nouveautés par version d'ECMAScript](#25-nouveautés-par-version-decmascript)

> **Légende** : *(ajout)* = notion absente du guide d'origine ; *(à jour)* = pratique moderne remplaçant une ancienne.
>
> **Convention des exemples** : `console.log` affiche un résultat ; `console.error` signale une erreur volontaire (le code fautif est alors entouré d'un `try...catch`). Chaque exemple est autonome et s'exécute dans Node.js ou dans la console du navigateur ; les exemples DOM, de stockage et de navigation demandent un navigateur, ceux qui utilisent `fetch` demandent une connexion Internet, et les exemples de modules (`import` / `export`) demandent les fichiers indiqués en commentaire.

---

# 1. Introduction

## 1.1 Qu'est-ce que JavaScript ?

**JavaScript** (JS) est un langage de programmation **interprété / compilé à la volée (JIT)**, **dynamique**, **multi-paradigme** (impératif, objet, fonctionnel) et **à événements**. Créé en **1995** par Brendan Eich chez Netscape, il est standardisé sous le nom **ECMAScript** (ECMA-262) et évolue **chaque année** via le comité **TC39**.

| Où s'exécute-t-il ? | Environnement |
| --- | --- |
| **Navigateur** | Chrome / Edge (V8), Firefox (SpiderMonkey), Safari (JavaScriptCore) |
| **Serveur / outils** | **Node.js**, **Deno**, **Bun** |
| **Mobile et bureau** | React Native, Electron, Tauri… |
| **Embarqué / edge** | Cloudflare Workers, Deno Deploy… |

> **JavaScript ≠ Java.** Les deux langages n'ont aucun lien, hormis le nom.
> **TypeScript** est un sur-ensemble typé de JavaScript, compilé (ou « dé-typé ») vers du JS. Voir [section 24](#24-outils-et-écosystème).

## 1.2 Exécuter du JavaScript

### Dans une page web

```html
<!-- Script classique, chargé sans bloquer l'analyse du HTML -->
<script src="app.js" defer></script>

<!-- Module ES (différé par défaut, mode strict automatique) -->
<script type="module" src="main.js"></script>
```

### Dans la console du navigateur

`F12` → onglet **Console**. On y teste du code immédiatement.

### Avec Node.js

```bash
node script.js
node --watch script.js      # relance à chaque modification
node                        # console interactive (REPL)
```

```javascript
console.log("Bonjour le monde !");
console.table([{ nom: "Alice", age: 30 }]);
console.error("Une erreur");   // affichée comme un message d'erreur
```

## 1.3 Syntaxe de base

```javascript
// Commentaire sur une ligne
/* Commentaire
   sur plusieurs lignes */

let message = "Salut";   // les points-virgules sont recommandés
console.log(message);    // "Salut"
```

- JavaScript est **sensible à la casse** (`nom` ≠ `Nom`).
- Les identifiants commencent par une lettre, `_` ou `$` ; convention **`camelCase`** (variables, fonctions), **`PascalCase`** (classes), **`MAJUSCULES`** (constantes globales).

---

# 2. Variables et portée

## 2.1 Déclarer une variable

| Mot-clé | Portée | Réaffectation | Redéclaration | Hoisting |
| --- | --- | --- | --- | --- |
| `var` *(ancien)* | Fonction | Oui | Oui | Remontée, valeur `undefined` |
| `let` | **Bloc** | Oui | Non | Remontée, mais en **zone morte temporelle** (TDZ) |
| `const` | **Bloc** | Non | Non | Idem `let` |

```javascript
let ville = "Tokyo";
ville = "Kyoto";               // réaffectation autorisée
console.log(ville);            // "Kyoto"

const pays = "Japon";
try {
    pays = "Corée";            // erreur : const n'est pas réaffectable
} catch (e) {
    console.error(e.name, e.message);   // TypeError Assignment to constant variable.
}

const utilisateur = { nom: "Alice" };
utilisateur.nom = "Bob";       // l'objet reste modifiable : const protège le lien, pas le contenu
console.log(utilisateur);      // { nom: "Bob" }
```

> **Bonne pratique** *(à jour)* : utilisez **`const` par défaut**, `let` si vous devez réaffecter, et **évitez `var`**.

## 2.2 Portée (*scope*)

```javascript
function saluer() {
    var message = "Bonjour";     // portée de fonction
    console.log(message);        // "Bonjour"
}
saluer();

{
    let x = 10;                  // portée de bloc
    const y = 20;
    console.log(x + y);          // 30
}

try {
    console.log(x);              // erreur : x n'existe pas hors du bloc
} catch (e) {
    console.error(e.name, e.message);   // ReferenceError x is not defined
}
```

| Portée | Description |
| --- | --- |
| **Globale** | Visible partout (`globalThis`) |
| **Module** | Propre à un fichier ES module |
| **Fonction** | Variables déclarées dans la fonction |
| **Bloc** | Entre `{ }` pour `let` / `const` |

## 2.3 Hoisting et zone morte temporelle (TDZ)

Les déclarations sont « remontées » au début de leur portée :

```javascript
console.log(a);   // undefined (var remontée, mais sans sa valeur)
var a = 5;

try {
    console.log(b);   // erreur : b est dans la TDZ
} catch (e) {
    console.error(e.name, e.message);   // ReferenceError Cannot access 'b' before initialization
}
let b = 10;

saluer();         // "Salut" : les déclarations de fonction sont remontées en entier
function saluer() { console.log("Salut"); }
```

## 2.4 Affectation par décomposition *(destructuring)*

```javascript
let [a, b, ...reste] = [1, 2, 3, 4];     // a=1, b=2, reste=[3, 4]
const { nom, age = 18, ville: v } = { nom: "Alice", ville: "Paris" };
console.log(a, b, reste);                // 1 2 [3, 4]
console.log(nom, age, v);                // "Alice" 18 "Paris" (valeur par défaut et renommage)

[a, b] = [b, a];                         // échange de valeurs
console.log(a, b);                       // 2 1
```

---

# 3. Types de valeurs

## 3.1 Primitifs et références

**Primitifs** (immuables, copiés **par valeur**) :

| Type | Exemple |
| --- | --- |
| `string` | `"Bonjour"` |
| `number` | `42`, `3.14`, `NaN`, `Infinity` |
| `boolean` | `true`, `false` |
| `null` | `null` (absence volontaire de valeur) |
| `undefined` | Variable non initialisée |
| `bigint` | `1234567890123456789n` |
| `symbol` | `Symbol("id")` |

**Références** (mutables, copiées **par référence**) : `Object`, `Array`, `Function`, `Date`, `RegExp`, `Map`, `Set`, etc.

```javascript
let a = 10;
let b = a;
b = 20;
console.log(a);          // 10 (copie indépendante)
console.log(b);          // 20

const o1 = { nom: "Tom" };
const o2 = o1;           // même objet !
o2.nom = "Jerry";
console.log(o1.nom);     // "Jerry"
```

### Copier un objet

```javascript
const o1 = { nom: "Tom", date: new Date(0) };

const copie1 = { ...o1 };                  // copie superficielle
const copie2 = Object.assign({}, o1);      // idem
const copie3 = structuredClone(o1);        // copie PROFONDE (à jour)

console.log(copie1.date === o1.date);      // true  : la date est partagée
console.log(copie2.date === o1.date);      // true
console.log(copie3.date === o1.date);      // false : copie indépendante

// JSON.parse(JSON.stringify(o)) perd les dates, Map, Set, undefined, fonctions…
console.log(JSON.parse(JSON.stringify(o1)).date);   // "1970-01-01T00:00:00.000Z" (une chaîne, plus une Date)
```

## 3.2 L'opérateur `typeof`

```javascript
console.log(typeof "Salut");        // "string"
console.log(typeof 42);             // "number"
console.log(typeof true);           // "boolean"
console.log(typeof undefined);      // "undefined"
console.log(typeof 10n);            // "bigint"
console.log(typeof Symbol());       // "symbol"
console.log(typeof function () {}); // "function"
console.log(typeof null);           // "object" (bug historique)
console.log(typeof []);             // "object" : utilisez Array.isArray([])
console.log(typeof {});             // "object"
console.log(Array.isArray([]));     // true
```

## 3.3 Conversions et coercition

```javascript
console.log(Number("42"));        // 42
console.log(Number("abc"));       // NaN
console.log(parseInt("42px"));    // 42
console.log(parseFloat("3.14"));  // 3.14
console.log(String(123));         // "123"
console.log(Boolean(0));          // false

console.log("5" + 3);             // "53"  (concaténation)
console.log("5" - 3);             // 2     (conversion numérique)
```

**Valeurs « falsy »** (converties en `false`) : `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined`, `NaN`. **Tout le reste est « truthy »**, y compris `"0"`, `[]` et `{}`.

## 3.4 Égalité

| Opérateur | Comportement |
| --- | --- |
| `===` / `!==` | Égalité **stricte**, sans conversion (recommandée) |
| `==` / `!=` | Égalité **souple**, avec conversions surprenantes |
| `Object.is(a, b)` | Comme `===`, mais `Object.is(NaN, NaN)` est `true` |

```javascript
console.log(0 == "0");            // true  (conversion implicite : piège)
console.log(0 === "0");           // false (comparaison stricte : recommandée)
console.log(null == undefined);   // true
console.log(NaN === NaN);         // false : utilisez Number.isNaN(x)
console.log(Number.isNaN(NaN));   // true
```

---

# 4. Opérateurs

## 4.1 Catégories

| Catégorie | Opérateurs |
| --- | --- |
| **Arithmétiques** | `+` `-` `*` `/` `%` `**` `++` `--` |
| **Affectation** | `=` `+=` `-=` `*=` `/=` `%=` `**=` |
| **Comparaison** | `==` `===` `!=` `!==` `>` `<` `>=` `<=` |
| **Logiques** | `&&` `\|\|` `!` |
| **Bit à bit** | `&` `\|` `^` `~` `<<` `>>` `>>>` |
| **Type** | `typeof` `instanceof` `in` |
| **Ternaire** | `condition ? a : b` |
| **Fusion nulle** | `??` |
| **Chaînage optionnel** | `?.` |
| **Affectation logique** | `&&=` `\|\|=` `??=` |
| **Décomposition / reste** | `...` |

```javascript
console.log(2 ** 10);     // 1024
console.log(7 % 3);       // 1
let i = 5;
i++;
console.log(i);           // 6
```

## 4.2 Fusion nulle `??`

Renvoie la valeur de droite **seulement si** la gauche est `null` ou `undefined` (contrairement à `||` qui réagit à toutes les valeurs falsy).

```javascript
const quantite = 0;
console.log(quantite || 10);     // 10 (piège : 0 est falsy)
console.log(quantite ?? 10);     // 0  (seuls null et undefined déclenchent la valeur par défaut)
```

## 4.3 Chaînage optionnel `?.`

```javascript
const utilisateur = { adresse: { ville: "Paris" } };
const vide = {};
const liste = [];
const objet = { methode() { return "appelée"; } };

console.log(utilisateur?.adresse?.ville);   // "Paris"
console.log(vide?.adresse?.ville);          // undefined (un maillon est absent)
console.log(liste?.[0]);                    // undefined
console.log(objet.methode?.());             // "appelée"
console.log(objet.autre?.());               // undefined (la méthode n'existe pas : pas d'appel)
```

## 4.4 Affectations logiques

```javascript
let a = null;
a ||= "  défaut  ";        // a = a || "  défaut  "
console.log(a);            // "  défaut  "
a &&= a.trim();            // a = a && a.trim()
console.log(a);            // "défaut"

let n;
n ??= 0;                   // n = n ?? 0
console.log(n);            // 0
```

## 4.5 Ternaire, `in`, `instanceof`

```javascript
const age = 20;
const utilisateur = { nom: "Alice" };
const tableau = [1, 2];

const statut = age >= 18 ? "majeur" : "mineur";
console.log(statut);                    // "majeur"
console.log("nom" in utilisateur);      // true (propriété présente ?)
console.log(tableau instanceof Array);  // true
```

## 4.6 Priorité

En cas de doute, **utilisez des parenthèses**. Ordre approximatif (haut → bas) : `()` → `**` → `* / %` → `+ -` → comparaisons → `&&` → `||` / `??` → ternaire → affectation.

> **Attention :** On ne peut pas mélanger `??` avec `&&` / `||` sans parenthèses.

## 4.7 Bonnes pratiques

- Utilisez toujours `===` et `!==`.
- Préférez `??` à `||` pour les valeurs par défaut quand `0` ou `""` sont valides.
- Limitez les ternaires imbriqués.

---

# 5. Chaînes de caractères

## 5.1 Déclarer des chaînes

```javascript
const s1 = 'simple';
const s2 = "double";
const s3 = `gabarit`;             // template literal (backticks)
console.log(s1, s2, s3);

const nom = "Alice";
console.log(`Bonjour ${nom}, 2 + 3 = ${2 + 3}`);   // interpolation

const multi = `Ligne 1
Ligne 2`;                          // chaîne multiligne
console.log(multi);
```

### Caractères d'échappement

| Séquence | Signification |
| --- | --- |
| `\n` | Saut de ligne |
| `\t` | Tabulation |
| `\\` | Antislash |
| `\'` `\"` | Guillemets |
| `\u00E9` / `\u{1F600}` | Caractère Unicode (`é` / un caractère hors du plan de base, comme un smiley) |

### Gabarits étiquetés *(ajout)*

```javascript
function surligner(chaines, ...valeurs) {
    return chaines.reduce((r, c, i) => r + c + (valeurs[i] !== undefined ? `<b>${valeurs[i]}</b>` : ""), "");
}
console.log(surligner`Bonjour ${"Alice"}, vous avez ${3} messages`);
// "Bonjour <b>Alice</b>, vous avez <b>3</b> messages"
```

## 5.2 Propriétés et accès

Les chaînes sont **immuables**.

```javascript
const s = "JavaScript";
console.log(s.length);   // 10
console.log(s[0]);       // "J"
console.log(s.at(-1));   // "t" (accès depuis la fin, ES2022)

(function () {
    "use strict";
    try {
        s[0] = "j";      // erreur en mode strict : les chaînes sont immuables
    } catch (e) {
        console.error(e.name, e.message);   // TypeError
    }
})();
console.log(s);          // "JavaScript" (inchangée ; hors mode strict, l'écriture est simplement ignorée)
```

## 5.3 Méthodes principales

| Méthode | Rôle | Exemple |
| --- | --- | --- |
| `toUpperCase()` / `toLowerCase()` | Casse | `"abc".toUpperCase()` → `"ABC"` |
| `trim()` / `trimStart()` / `trimEnd()` | Supprime les espaces | |
| `slice(début, fin)` | Extrait une sous-chaîne (accepte négatifs) | `"abcdef".slice(1, 3)` → `"bc"` |
| `substring(début, fin)` | Extrait (pas de négatifs) | |
| `indexOf()` / `lastIndexOf()` | Position | |
| `includes()` / `startsWith()` / `endsWith()` | Test | `"abc".includes("b")` → `true` |
| `replace()` / `replaceAll()` | Remplace (1re occurrence / toutes) | `"a-b-c".replaceAll("-", "+")` |
| `split(sep)` | Découpe en tableau | `"a,b".split(",")` → `["a","b"]` |
| `repeat(n)` | Répète | `"ab".repeat(2)` → `"abab"` |
| `padStart()` / `padEnd()` | Complète | `"5".padStart(3, "0")` → `"005"` |
| `charAt()` / `charCodeAt()` / `codePointAt()` | Caractère / code | |
| `localeCompare()` | Comparaison selon la langue | `"é".localeCompare("f", "fr")` |
| `normalize()` | Normalisation Unicode | |
| `match()` / `matchAll()` / `search()` | Expressions régulières | voir [section 11](#11-expressions-régulières) |
| `isWellFormed()` / `toWellFormed()` | Vérifie / corrige l'Unicode (ES2024) | |

```javascript
console.log("  Bonjour  ".trim());              // "Bonjour"
console.log(["a", "b", "c"].join("-"));         // "a-b-c"
console.log([..."héllo"].length);               // 5 (itère par caractères Unicode)
```

## 5.4 Bonnes pratiques

- Préférez les **gabarits** (`` `...` ``) à la concaténation avec `+`.
- Pour comparer des textes accentués, utilisez `localeCompare` ou `Intl.Collator`.
- Attention : `length` compte des **unités UTF-16**, pas des caractères visibles (les emojis valent souvent 2).

---

# 6. Nombres et `Math`

## 6.1 Le type `number`

Tous les nombres ordinaires sont des **flottants 64 bits (IEEE 754)**.

```javascript
const entier = 42;
const decimal = 3.14;
const grand = 1_000_000;        // séparateurs de lisibilité
const hexa = 0xff;              // 255
const bin = 0b1010;             // 10
const sci = 1.5e3;              // 1500
console.log(entier, decimal, grand, hexa, bin, sci);

console.log(typeof NaN);        // "number"
console.log(1 / 0);             // Infinity
```

### Précision des flottants

```javascript
console.log(0.1 + 0.2);                                   // 0.30000000000000004
console.log(Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON);  // true (comparaison tolérante)
console.log((0.1 + 0.2).toFixed(2));                      // "0.30" (renvoie une CHAÎNE)
```

Pour la monnaie : travaillez en **centimes (entiers)** ou utilisez `Intl.NumberFormat`.

## 6.2 Méthodes et propriétés de `Number`

| Élément | Rôle |
| --- | --- |
| `Number.isInteger(x)` | Entier ? |
| `Number.isFinite(x)` / `Number.isNaN(x)` | Test **strict** (sans conversion) |
| `Number.isSafeInteger(x)` | Entier sûr (≤ 2⁵³ − 1) ? |
| `Number.parseFloat()` / `Number.parseInt()` | Conversion |
| `Number.MAX_SAFE_INTEGER` | 9 007 199 254 740 991 |
| `Number.EPSILON` | Plus petit écart entre deux flottants |
| `x.toFixed(n)` | Nombre de décimales (chaîne) |
| `x.toString(base)` | Conversion en base 2 à 36 |

## 6.3 `BigInt` *(ajout)*

Pour les entiers **arbitrairement grands** :

```javascript
const enorme = 9007199254740993n;
console.log(enorme * 2n);        // 18014398509481986n
console.log(BigInt(10) + 5n);    // 15n

try {
    console.log(1n + 1);         // erreur : on ne mélange pas BigInt et number
} catch (e) {
    console.error(e.name, e.message);   // TypeError Cannot mix BigInt and other types...
}
```

## 6.4 L'objet `Math`

| Méthode | Rôle |
| --- | --- |
| `Math.round()` `floor()` `ceil()` `trunc()` | Arrondis |
| `Math.abs()` `sign()` | Valeur absolue, signe |
| `Math.max(...)` `Math.min(...)` | Extrêmes |
| `Math.pow()` `sqrt()` `cbrt()` `hypot()` | Puissances, racines |
| `Math.random()` | Nombre aléatoire dans [0 ; 1[ |
| `Math.sin()` `cos()` `tan()` `atan2()`… | Trigonométrie |
| `Math.log()` `log2()` `log10()` `exp()` | Logarithmes, exponentielle |
| `Math.PI` `Math.E` | Constantes |
| `Math.sumPrecise(iterable)` | Somme **précise** de nombres *(ES2026)* |

```javascript
console.log(Math.floor(Math.random() * 10) + 1);   // entier aléatoire de 1 à 10
console.log(Math.max(...[3, 9, 4]));               // 9
```

> **Sécurité :** `Math.random()` **n'est pas cryptographiquement sûr** : pour des jetons ou mots de passe, utilisez `crypto.getRandomValues()` ou `crypto.randomUUID()`.

## 6.5 Formater les nombres avec `Intl` *(à jour)*

```javascript
console.log(new Intl.NumberFormat("fr-FR", { style: "currency", currency: "EUR" }).format(1234.5));
// "1 234,50 €"
console.log(new Intl.NumberFormat("fr-FR", { style: "percent" }).format(0.256));   // "26 %"
console.log((1234567.891).toLocaleString("fr-FR"));                                // "1 234 567,891"
```

---

# 7. Conditions et boucles

## 7.1 Conditions

```javascript
const note = 14;

if (note >= 16) {
    console.log("Très bien");
} else if (note >= 10) {
    console.log("Passable");   // affiché pour 14
} else {
    console.log("Insuffisant");
}
```

### `switch`

Compare avec `===`. N'oubliez pas `break` (sinon, exécution en cascade).

```javascript
const jour = "dimanche";

switch (jour) {
    case "samedi":
    case "dimanche":
        console.log("Week-end");   // affiché pour "dimanche"
        break;
    default:
        console.log("Semaine");
}
```

### Ternaire et opérateurs logiques

```javascript
const age = 20;
const utilisateur = { nom: "Alice" };
const afficher = (u) => console.log(`Utilisateur : ${u.nom}`);
const saisie = null;

const acces = age >= 18 ? "autorisé" : "refusé";
console.log(acces);                          // "autorisé"
utilisateur && afficher(utilisateur);        // court-circuit : afficher() n'est appelée que si utilisateur est défini
const nom = saisie ?? "Anonyme";
console.log(nom);                            // "Anonyme"
```

> Pour de nombreux `case`, une **table de correspondance** (objet ou `Map`) est souvent plus lisible :
>
> ```javascript
> const ajouter = () => console.log("Ajout");
> const supprimer = () => console.log("Suppression");
> const commande = "ajouter";
>
> const actions = { ajouter, supprimer };
> actions[commande]?.();     // "Ajout"
> actions.inconnue?.();      // rien : la commande n'existe pas
> ```

## 7.2 Boucles

| Boucle | Usage |
| --- | --- |
| `for` | Nombre d'itérations connu |
| `while` | Tant qu'une condition est vraie |
| `do...while` | Au moins une exécution |
| `for...of` | **Valeurs** d'un itérable (tableau, chaîne, `Map`, `Set`…) : à privilégier |
| `for...in` | **Clés** énumérables d'un objet (à éviter sur les tableaux) |

```javascript
for (let i = 0; i < 3; i++) console.log(i);   // 0 1 2

let n = 0;
while (n < 3) { n++; }
console.log(n);                               // 3

do { n--; } while (n > 0);
console.log(n);                               // 0

for (const fruit of ["pomme", "banane"]) console.log(fruit);

for (const [cle, valeur] of Object.entries({ a: 1, b: 2 })) {
    console.log(cle, valeur);
}

for (const cle in { x: 1, y: 2 }) console.log(cle);   // "x", "y"
```

### `break`, `continue` et étiquettes

```javascript
for (let i = 0; i < 10; i++) {
    if (i === 3) continue;     // passe à l'itération suivante
    if (i === 6) break;        // quitte la boucle
    console.log(i);            // 0 1 2 4 5
}

externe: for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        if (j === 1) continue externe;
        console.log(i, j);     // 0 0, puis 1 0, puis 2 0
    }
}
```

> **Attention :** `forEach` **n'attend pas** les `await` de son callback : utilisez `for...of` pour des boucles asynchrones séquentielles.

## 7.3 Bonnes pratiques

- Préférez `for...of` et les méthodes de tableaux (`map`, `filter`, `reduce`) aux boucles `for` indexées.
- Évitez de modifier une collection pendant qu'on la parcourt.
- Sortez tôt (**clauses de garde**) plutôt que d'imbriquer des `if`.

---

# 8. Tableaux

## 8.1 Créer et accéder

```javascript
const fruits = ["pomme", "banane", "cerise"];
const vide = [];
const zeros = new Array(3).fill(0);                        // [0, 0, 0]
const suite = Array.from({ length: 5 }, (_, i) => i);      // [0, 1, 2, 3, 4]
const lettres = Array.from("abc");                         // ["a", "b", "c"]
console.log(vide, zeros, suite, lettres);

console.log(fruits[0]);              // "pomme"
console.log(fruits.at(-1));          // "cerise" (ES2022)
console.log(fruits.length);          // 3
console.log(Array.isArray(fruits));  // true
```

## 8.2 Ajouter, retirer, modifier

| Méthode | Effet | Mute ? |
| --- | --- | --- |
| `push(x)` / `pop()` | Ajoute / retire à la **fin** | Oui |
| `unshift(x)` / `shift()` | Ajoute / retire au **début** | Oui |
| `splice(i, n, ...ajouts)` | Supprime / insère à une position | Oui |
| `sort()` / `reverse()` | Trie / inverse | Oui |
| `fill()` / `copyWithin()` | Remplit / copie interne | Oui |
| `slice(début, fin)` | Sous-tableau | Non (renvoie une copie) |
| `concat()` / `[...a, ...b]` | Assemble | Non (renvoie une copie) |

### Versions **non mutantes** *(ES2023, à jour)*

```javascript
const nombres = [3, 1, 2];
console.log(nombres.toSorted());        // [1, 2, 3]
console.log(nombres.toReversed());      // [2, 1, 3]
console.log(nombres.toSpliced(1, 1));   // [3, 2]
console.log(nombres.with(0, 99));       // [99, 1, 2]
console.log(nombres);                   // [3, 1, 2] (inchangé)
```

> **Attention :** `sort()` sans argument trie en **ordre alphabétique** : `[10, 2, 1].sort()` → `[1, 10, 2]`. Utilisez `sort((a, b) => a - b)`.

## 8.3 Parcourir

```javascript
const fruits = ["pomme", "banane", "cerise"];

for (const f of fruits) console.log(f);
fruits.forEach((f, i) => console.log(i, f));
for (const [i, f] of fruits.entries()) console.log(i, f);
```

## 8.4 Méthodes d'ordre supérieur

```javascript
const nums = [1, 2, 3, 4, 5];

console.log(nums.map(x => x * 2));                  // [2, 4, 6, 8, 10]
console.log(nums.filter(x => x % 2 === 0));         // [2, 4]
console.log(nums.reduce((somme, x) => somme + x, 0));   // 15
console.log(nums.find(x => x > 2));                 // 3
console.log(nums.findIndex(x => x > 2));            // 2
console.log(nums.findLast(x => x < 5));             // 4 (ES2023)
console.log(nums.some(x => x > 4));                 // true
console.log(nums.every(x => x > 0));                // true
console.log(nums.flatMap(x => [x, x * 10]));        // aplatit d'un niveau
console.log([[1, [2]], [3]].flat(Infinity));        // [1, 2, 3]
```

### Rechercher

```javascript
const fruits = ["pomme", "banane", "cerise"];

console.log(fruits.includes("pomme"));    // true
console.log(fruits.indexOf("banane"));    // 1
```

### Regrouper *(ES2024)*

```javascript
const personnes = [{ nom: "A", age: 20 }, { nom: "B", age: 30 }, { nom: "C", age: 20 }];

console.log(Object.groupBy(personnes, p => p.age));
// { 20: [{ nom: "A", ... }, { nom: "C", ... }], 30: [{ nom: "B", ... }] }
console.log(Map.groupBy(personnes, p => p.age));   // même chose, sous forme de Map
```

### Autres

```javascript
async function* nombres() {
    yield 1;
    yield 2;
    yield 3;
}

// ES2026 : version asynchrone d'Array.from
Array.fromAsync(nombres()).then(console.log);       // [1, 2, 3]
console.log(["a", "b"].join(", "));                  // "a, b"
```

## 8.5 Spread, rest et décomposition

```javascript
const a = [1, 2];
const b = [...a, 3, 4];                // copie + ajout
console.log(b);                        // [1, 2, 3, 4]
console.log(Math.max(...b));           // 4
const [premier, ...autres] = b;
console.log(premier, autres);          // 1 [2, 3, 4]
```

## 8.6 Tableaux d'objets

```javascript
const users = [{ id: 1, nom: "Alice" }, { id: 2, nom: "Bob" }];

console.log(users.map(u => u.nom));                          // ["Alice", "Bob"]
console.log(users.find(u => u.id === 2));                    // { id: 2, nom: "Bob" }
console.log(users.toSorted((x, y) => x.nom.localeCompare(y.nom)));   // ordre alphabétique : Alice, puis Bob
```

## 8.7 Bonnes pratiques

- Préférez les méthodes **non mutantes** et le **spread** pour éviter les effets de bord.
- Utilisez `Array.isArray()` pour tester un tableau.
- Pour tester l'appartenance fréquemment sur de grandes collections, utilisez un **`Set`**.
- Chaînez les méthodes avec modération : lisibilité d'abord.

---

# 9. Objets, `Map` et `Set`

## 9.1 Les objets

Un **objet** est une collection de paires **clé → valeur** (propriétés). C'est la structure de base de JavaScript, souvent utilisée comme « dictionnaire ».

```javascript
const personne = {
    nom: "Alice",
    age: 30,
    "code postal": "75001",          // clé avec espace : entre guillemets
    saluer() { return `Bonjour, je suis ${this.nom}`; },   // méthode
};

console.log(personne.nom);                  // "Alice" (notation pointée)
console.log(personne["code postal"]);       // "75001" (notation crochets : clés dynamiques)
personne.ville = "Paris";                   // ajout
delete personne.age;                        // suppression
console.log("nom" in personne);             // true
console.log(Object.hasOwn(personne, "nom"));   // true (à jour : remplace hasOwnProperty)
console.log(personne.saluer());             // "Bonjour, je suis Alice"
console.log(personne);
```

### Propriétés calculées et raccourcis

```javascript
const cle = "couleur";
const nom = "Alice", age = 30;
const o = { [cle]: "rouge", nom, age };
console.log(o);                           // { couleur: "rouge", nom: "Alice", age: 30 }
```

### Méthodes utilitaires de `Object`

| Méthode | Rôle |
| --- | --- |
| `Object.keys(o)` | Tableau des clés |
| `Object.values(o)` | Tableau des valeurs |
| `Object.entries(o)` | Tableau de paires `[clé, valeur]` |
| `Object.fromEntries(paires)` | Reconstruit un objet depuis des paires |
| `Object.assign(cible, ...sources)` | Copie des propriétés (muter la cible) |
| `Object.freeze(o)` | Rend l'objet **immuable** (superficiellement) |
| `Object.seal(o)` | Interdit ajout/suppression |
| `Object.defineProperty(o, nom, desc)` | Définit une propriété avec attributs |
| `Object.groupBy(it, fn)` | Regroupe *(ES2024)* |
| `structuredClone(o)` | Copie profonde |

```javascript
const prix = { pomme: 1, poire: 2 };
const defauts = { theme: "clair", langue: "fr" };
const options = { langue: "en" };

console.log(Object.entries({ a: 1, b: 2 }));         // [["a", 1], ["b", 2]]
console.log(Object.fromEntries(Object.entries(prix).map(([k, v]) => [k, v * 1.2])));   // transformer les valeurs
console.log({ ...defauts, ...options });             // fusion (la dernière valeur gagne) : { theme: "clair", langue: "en" }
```

### Décomposition d'objet

```javascript
const personne = { nom: "Alice", age: 30, ville: "Paris" };

const { nom, ...reste } = personne;
console.log(nom, reste);                 // "Alice" { age: 30, ville: "Paris" }

function afficher({ nom, age = 18 }) {
    console.log(`${nom} a ${age} ans`);
}
afficher({ nom: "Bob" });                // "Bob a 18 ans"
```

### Itération

```javascript
const personne = { nom: "Alice", age: 30 };

for (const [cle, valeur] of Object.entries(personne)) console.log(cle, valeur);
```

### Pièges des objets-dictionnaires

- Les clés sont des **chaînes ou symboles** (`1` devient `"1"`).
- Risque de collision avec le prototype (`"constructor"`, `"toString"`) : créez un dictionnaire « pur » avec `Object.create(null)` ou, mieux, utilisez une **`Map`**.
- `__proto__` comme clé est dangereux avec des données externes (pollution de prototype).

## 9.2 `Map` : un vrai dictionnaire

Accepte **n'importe quel type de clé**, conserve l'**ordre d'insertion** et fournit directement sa taille.

```javascript
const scores = new Map();
scores.set("Alice", 15).set("Bob", 12);
console.log(scores.get("Alice"));     // 15
console.log(scores.has("Bob"));       // true
scores.delete("Bob");
console.log(scores.size);             // 1

scores.set("Chloé", 18);
for (const [nom, note] of scores) console.log(nom, note);
console.log([...scores.keys()]);      // ["Alice", "Chloé"]
console.log([...scores.values()]);    // [15, 18]
console.log([...scores.entries()]);

const depuisObjet = new Map(Object.entries({ a: 1 }));
const versObjet = Object.fromEntries(scores);
console.log(depuisObjet, versObjet);

// ES2026 : getOrInsert (évite le motif « si absent, créer »)
const groupes = new Map();
groupes.getOrInsert("fruits", []).push("pomme");
groupes.getOrInsertComputed("legumes", () => []).push("carotte");
console.log(groupes);                 // Map { "fruits" => ["pomme"], "legumes" => ["carotte"] }
```

### `Map` ou objet ?

| Critère | Objet | `Map` |
| --- | --- | --- |
| Types de clés | Chaîne / symbole | **Tous** (objets, fonctions…) |
| Ordre | Complexe (entiers d'abord) | **Ordre d'insertion** |
| Taille | `Object.keys(o).length` | `map.size` |
| Itération | Via `Object.entries` | Directe |
| Performances (ajouts/retraits fréquents) | Moyennes | **Meilleures** |
| Sérialisation JSON | Native | À convertir |
| Usage conseillé | Données structurées à clés fixes | Dictionnaire dynamique |

## 9.3 `Set` : des valeurs uniques

```javascript
const tableau = [1, 2, 2, 3, 3, 3];

const unique = new Set([1, 2, 2, 3]);    // Set {1, 2, 3}
unique.add(4);
console.log(unique.has(2));              // true
unique.delete(1);
console.log(unique.size);                // 3
console.log(unique);                     // Set {2, 3, 4}

const sansDoublons = [...new Set(tableau)];
console.log(sansDoublons);               // [1, 2, 3]
```

### Opérations ensemblistes *(ES2025, à jour)*

```javascript
const a = new Set([1, 2, 3]);
const b = new Set([3, 4]);

console.log(a.union(b));                // Set {1, 2, 3, 4}
console.log(a.intersection(b));         // Set {3}
console.log(a.difference(b));           // Set {1, 2}
console.log(a.symmetricDifference(b));  // Set {1, 2, 4}
console.log(a.isSubsetOf(b));           // false
console.log(a.isSupersetOf(b), a.isDisjointFrom(b));   // false false
```

## 9.4 `WeakMap` et `WeakSet` *(ajout)*

Leurs clés sont des **objets tenus faiblement** : si l'objet n'est plus référencé ailleurs, il peut être collecté par le ramasse-miettes. Utiles pour associer des données privées ou un cache à des objets sans fuite de mémoire. Non itérables.

```javascript
const element = { id: "carte-1" };   // la clé doit être un objet
const meta = new WeakMap();
meta.set(element, { clics: 0 });

meta.get(element).clics++;
console.log(meta.get(element));      // { clics: 1 }
console.log(meta.has(element));      // true
// Quand `element` n'est plus référencé, l'entrée peut être ramassée par le ramasse-miettes.
```

## 9.5 Choisir la bonne structure

| Besoin | Structure |
| --- | --- |
| Liste ordonnée | `Array` |
| Données structurées (enregistrement) | Objet |
| Dictionnaire dynamique | `Map` |
| Valeurs uniques, tests d'appartenance rapides | `Set` |
| Cache lié à des objets | `WeakMap` |

---

# 10. `globalThis`

## 10.1 Pourquoi `globalThis` ?

L'objet global porte des noms différents selon l'environnement :

| Environnement | Objet global |
| --- | --- |
| Navigateur | `window` (ou `self`) |
| Web Worker | `self` |
| Node.js | `global` |

**`globalThis`** (ES2020) est **le même nom partout** :

```javascript
console.log(globalThis.setTimeout === setTimeout);     // true
globalThis.maVariable = 42;                             // pollue l'espace global : à éviter
console.log(globalThis.maVariable);                     // 42
console.log(globalThis.console === console);            // true
```

## 10.2 Cas d'usage

```javascript
// Détection de fonctionnalités, code isomorphe
if (typeof globalThis.fetch === "function") {
    console.log("fetch est disponible");
}

// Polyfill
if (!globalThis.structuredClone) {
    globalThis.structuredClone = (v) => JSON.parse(JSON.stringify(v));
}
console.log(structuredClone({ a: 1 }));   // { a: 1 }
```

## 10.3 Pièges

- `var` et les fonctions déclarées au niveau global d'un **script classique** deviennent des propriétés de `globalThis` ; **`let` / `const` n'y sont pas** ajoutés, et **les modules** ont leur propre portée.
- Évitez de créer des variables globales : elles causent des collisions.
- Dans un module ou Node.js (CommonJS), `this` au niveau supérieur n'est **pas** `globalThis`.

---

# 11. Expressions régulières

## 11.1 Créer une expression régulière

```javascript
const re1 = /ab+c/i;                       // littéral
const re2 = new RegExp("ab+c", "i");       // constructeur (motif dynamique)
console.log(re1.test("xABBCx"), re2.test("abc"));     // true true

const saisieUtilisateur = "a.b*c";
const sur = new RegExp(RegExp.escape(saisieUtilisateur));   // RegExp.escape (ES2025)
console.log(sur.test("a.b*c"), sur.test("aXbbc"));    // true false
```

## 11.2 Méthodes

| Méthode | Rôle |
| --- | --- |
| `re.test(texte)` | `true` / `false` |
| `re.exec(texte)` | Première correspondance (détails) ou `null` |
| `texte.match(re)` | Correspondances (avec `g` : tableau de toutes) |
| `texte.matchAll(re)` | **Itérateur** de toutes les correspondances détaillées (flag `g` obligatoire) |
| `texte.replace(re, rempl)` / `replaceAll` | Remplacement |
| `texte.split(re)` | Découpe |
| `texte.search(re)` | Position de la première correspondance |

## 11.3 Syntaxe courante

| Motif | Signification |
| --- | --- |
| `.` | N'importe quel caractère (sauf saut de ligne) |
| `\d` `\D` | Chiffre / non-chiffre |
| `\w` `\W` | Caractère de mot `[A-Za-z0-9_]` / contraire |
| `\s` `\S` | Espace blanc / contraire |
| `^` `$` | Début / fin |
| `\b` | Frontière de mot |
| `*` `+` `?` | 0 ou plus / 1 ou plus / 0 ou 1 |
| `{n}` `{n,}` `{n,m}` | Répétitions |
| `*?` `+?` | Quantificateurs **paresseux** |
| `[abc]` `[^abc]` `[a-z]` | Classe de caractères |
| `(a\|b)` | Groupe / alternative |
| `(?:…)` | Groupe non capturant |
| `(?<nom>…)` | **Groupe nommé** |
| `\1` `\k<nom>` | Référence arrière |
| `(?=…)` `(?!…)` | Anticipation positive / négative |
| `(?<=…)` `(?<!…)` | **Rétrospection** positive / négative |
| `\p{L}` | Propriété Unicode (avec flag `u` ou `v`) |

## 11.4 Drapeaux (*flags*)

| Flag | Effet |
| --- | --- |
| `g` | Global : toutes les correspondances |
| `i` | Insensible à la casse |
| `m` | `^` et `$` agissent sur chaque ligne |
| `s` | `.` correspond aussi au saut de ligne |
| `u` | Mode Unicode |
| `v` | Mode Unicode étendu : opérations sur classes, propriétés de chaînes (ES2024) |
| `y` | Collant (*sticky*) |
| `d` | Fournit les **indices** des correspondances (ES2022) |

## 11.5 Groupes de capture

```javascript
const m = "2026-10-11".match(/(?<annee>\d{4})-(?<mois>\d{2})-(?<jour>\d{2})/);
console.log(m.groups.annee);        // "2026"

console.log("Alice Dupont".replace(/(\w+) (\w+)/, "$2 $1"));        // "Dupont Alice"
console.log("2026-10-11".replace(/(?<a>\d+)-(?<m>\d+)-(?<j>\d+)/, "$<j>/$<m>/$<a>"));   // "11/10/2026"

for (const r of "a1b22".matchAll(/\d+/g)) console.log(r[0], r.index);   // "1" 1, puis "22" 3
```

## 11.6 Exemples utiles

```javascript
const email = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;          // validation simple (non exhaustive)
const telFr = /^(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}$/;
const espaces = /\s+/g;

console.log(email.test("alice@exemple.fr"));         // true
console.log(email.test("alice@exemple"));            // false
console.log(telFr.test("06 12 34 56 78"));           // true
console.log("a   b".replace(espaces, " "));          // "a b"
```

## 11.7 Bonnes pratiques

- Gardez les motifs **simples et commentés** ; testez-les sur [regex101.com](https://regex101.com).
- Évitez les motifs à **retours arrière catastrophiques** (ex. `(a+)+$`) : risque de blocage (ReDoS) avec des entrées non fiables.
- Pour valider un e-mail ou une URL, préférez une validation **native** (`type="email"`, `URL.canParse()`) ou une bibliothèque.
- Échappez toute saisie utilisateur intégrée à un motif (`RegExp.escape`).

---

# 12. Fonctions, portée et fermetures

## 12.1 Déclarer une fonction

```javascript
// Déclaration (hoistée)
function additionner(a, b) {
    return a + b;
}

// Expression de fonction (non hoistée)
const soustraire = function (a, b) { return a - b; };

// Fonction fléchée
const multiplier = (a, b) => a * b;
const carre = x => x ** 2;              // 1 paramètre : parenthèses facultatives
const creer = () => ({ nom: "Alice" }); // retour d'objet : parenthèses obligatoires

console.log(additionner(2, 3));    // 5
console.log(soustraire(5, 3));     // 2
console.log(multiplier(4, 3));     // 12
console.log(carre(5));             // 25
console.log(creer());              // { nom: "Alice" }
```

### Fonctions fléchées vs classiques

| | Fléchée `=>` | Classique `function` |
| --- | --- | --- |
| `this` | **Hérité** du contexte englobant (lexical) | Dépend de l'appel |
| `arguments` | Non | Oui |
| Constructeur (`new`) | Non | Oui |
| Usage idéal | Callbacks, petites fonctions | Méthodes, constructeurs |

## 12.2 Paramètres et arguments

```javascript
function saluer(nom = "inconnu", ...titres) {    // valeur par défaut + paramètre rest
    return `Bonjour ${titres.join(" ")} ${nom}`;
}
console.log(saluer());                       // "Bonjour  inconnu"
console.log(saluer("Alice", "Dr", "Pr"));    // "Bonjour Dr Pr Alice"

const nombres = [1, 2, 3];
console.log(Math.max(...nombres));           // 3 (spread à l'appel)

function config({ port = 3000, hote = "localhost" } = {}) {   // paramètres nommés
    return `${hote}:${port}`;
}
console.log(config());                       // "localhost:3000"
console.log(config({ port: 8080 }));         // "localhost:8080"
```

## 12.3 Valeur de retour

Une fonction sans `return` renvoie `undefined`. Pour retourner plusieurs valeurs, retournez un tableau ou un objet.

```javascript
const minMax = (t) => ({ min: Math.min(...t), max: Math.max(...t) });
const { min, max } = minMax([3, 1, 4]);
console.log(min, max);   // 1 4
```

## 12.4 Portée lexicale

Une fonction a accès aux variables de la portée où elle est **définie** (et non où elle est appelée).

```javascript
const global = "G";
function externe() {
    const local = "L";
    function interne() { return `${global}${local}`; }
    return interne();
}
console.log(externe());   // "GL" : interne() voit les variables de externe() et la variable globale
```

## 12.5 Fermetures (*closures*)

Une **fermeture** est une fonction qui **conserve l'accès aux variables** de la portée où elle a été créée, même après la fin de celle-ci.

```javascript
function creerCompteur() {
    let compte = 0;                  // variable « privée »
    return {
        incrementer: () => ++compte,
        valeur: () => compte,
    };
}
const c = creerCompteur();
c.incrementer();
c.incrementer();
console.log(c.valeur());             // 2
console.log(c.compte);               // undefined : la variable n'est pas accessible de l'extérieur
```

Usages : données privées, fonctions « fabriques », mémoïsation, *callbacks*.

```javascript
// Piège classique avec var
for (var i = 0; i < 3; i++) setTimeout(() => console.log("var :", i));   // 3 3 3
// Correction avec let : une variable par itération
for (let j = 0; j < 3; j++) setTimeout(() => console.log("let :", j));   // 0 1 2
```

## 12.6 `this`, `call`, `apply`, `bind`

`this` dépend de **la façon dont la fonction est appelée** :

| Appel | Valeur de `this` |
| --- | --- |
| `objet.methode()` | `objet` |
| `fonction()` | `undefined` (mode strict) ou `globalThis` |
| `new Fonction()` | La nouvelle instance |
| Fonction fléchée | Celui de la portée englobante |

```javascript
function presenter(salutation, ponctuation) {
    return `${salutation}, ${this.nom}${ponctuation}`;
}
const alice = { nom: "Alice" };

console.log(presenter.call(alice, "Salut", "!"));      // appel immédiat, arguments séparés
console.log(presenter.apply(alice, ["Salut", "!"]));   // appel immédiat, arguments en tableau
const lie = presenter.bind(alice, "Salut");            // renvoie une NOUVELLE fonction liée
console.log(lie("?"));                                 // "Salut, Alice?"
```

> **Attention :** Une méthode passée en *callback* perd son `this` : `setTimeout(obj.methode, 0)` → utilisez `obj.methode.bind(obj)` ou une fonction fléchée.

## 12.7 Fonctions d'ordre supérieur et composition

```javascript
const appliquerDeuxFois = (f, x) => f(f(x));
console.log(appliquerDeuxFois(x => x * 2, 3));   // 12

const ajouter = n => x => x + n;                 // curryfication
console.log(ajouter(2)(3));                      // 5

const composer = (...fns) => x => fns.reduceRight((acc, f) => f(acc), x);
const incrementerPuisDoubler = composer(x => x * 2, x => x + 1);   // x + 1 est appliquée en premier
console.log(incrementerPuisDoubler(5));          // 12
```

## 12.8 Fonctions immédiatement invoquées (IIFE)

```javascript
(function () {
    const prive = "isolé";
    console.log(prive);      // "isolé"
})();
console.log(typeof prive);   // "undefined" : la variable n'existe pas en dehors de la fonction
```

Moins utiles depuis que les **modules** et le **bloc `{}`** (avec `let`/`const`) offrent leur propre portée.

## 12.9 Récursivité

```javascript
const factorielle = n => (n <= 1 ? 1 : n * factorielle(n - 1));
console.log(factorielle(5));   // 120
```

La pile d'appels est limitée (`RangeError: Maximum call stack size exceeded`) : préférez une boucle pour de grandes profondeurs.

## 12.10 Mémoïsation *(ajout)*

```javascript
function memoiser(fn) {
    const cache = new Map();
    return (arg) => cache.has(arg) ? cache.get(arg) : (cache.set(arg, fn(arg)), cache.get(arg));
}

const carreLent = (n) => {
    console.log("calcul de", n);
    return n * n;
};
const carreMemoise = memoiser(carreLent);

console.log(carreMemoise(4));   // "calcul de 4", puis 16
console.log(carreMemoise(4));   // 16 (lu dans le cache : pas de nouveau calcul)
```

## 12.11 Bonnes pratiques

- Fonctions **courtes**, à responsabilité unique, bien nommées (verbes : `calculerTotal`).
- Limitez le nombre de paramètres ; au-delà de 3, utilisez **un objet**.
- Évitez les effets de bord et les variables globales.
- Préférez les fonctions fléchées pour les *callbacks*.
- Documentez avec **JSDoc** :

```javascript
/**
 * Calcule l'aire d'un rectangle.
 * @param {number} largeur
 * @param {number} hauteur
 * @returns {number}
 */
function aire(largeur, hauteur) { return largeur * hauteur; }

console.log(aire(3, 4));   // 12
```

---

# 13. Itérateurs et générateurs

*(Section ajoutée.)*

## 13.1 Le protocole d'itération

Un **itérable** possède une méthode `[Symbol.iterator]()` qui renvoie un **itérateur** (objet avec `next()` → `{ value, done }`). Tableaux, chaînes, `Map`, `Set` et `NodeList` sont itérables ; on les parcourt avec `for...of`, `...` et la décomposition.

```javascript
const it = [10, 20][Symbol.iterator]();
console.log(it.next());   // { value: 10, done: false }
console.log(it.next());   // { value: 20, done: false }
console.log(it.next());   // { value: undefined, done: true }
```

## 13.2 Générateurs

Une fonction `function*` utilise `yield` pour produire des valeurs **à la demande** et suspend son exécution entre deux.

```javascript
function* compteARebours(n) {
    while (n > 0) yield n--;
}
console.log([...compteARebours(3)]);   // [3, 2, 1]

function* naturels() { let i = 0; while (true) yield i++; }   // séquence infinie
const gen = naturels();
console.log(gen.next().value, gen.next().value, gen.next().value);   // 0 1 2
```

Rendre un objet itérable :

```javascript
class Playlist {
    #titres = ["A", "B"];
    *[Symbol.iterator]() { yield* this.#titres; }
}
console.log([...new Playlist()]);      // ["A", "B"]
for (const titre of new Playlist()) console.log(titre);
```

## 13.3 Assistants d'itérateurs *(ES2025, à jour)*

Chaînage **paresseux** sur n'importe quel itérateur :

```javascript
function* naturels() { let i = 0; while (true) yield i++; }

console.log(
    naturels()
        .filter(n => n % 2 === 0)
        .map(n => n * n)
        .take(5)
        .toArray()            // [0, 4, 16, 36, 64]
);

// ES2026 : concaténer des itérables
console.log(Iterator.concat([1, 2], [3, 4]).toArray());   // [1, 2, 3, 4]
```

Autres : `drop`, `flatMap`, `reduce`, `some`, `every`, `find`, `forEach`.

## 13.4 Générateurs asynchrones

```javascript
// Simule une API paginée (avec fetch : yield await (await fetch(`${url}?page=${p}`)).json())
async function* pages(total) {
    for (let p = 1; p <= total; p++) {
        await new Promise((resolve) => setTimeout(resolve, 200));   // latence simulée
        yield { page: p, items: [`élément ${p}`] };
    }
}

(async () => {
    for await (const page of pages(3)) console.log(page);
})();
```

---

# 14. `eval` et ses alternatives

## 14.1 Qu'est-ce que `eval` ?

`eval(chaine)` **exécute du code JavaScript contenu dans une chaîne**.

```javascript
const resultat = eval("2 + 3 * 4");
console.log(resultat);     // 14
```

## 14.2 Pourquoi l'éviter ?

| Risque | Détail |
| --- | --- |
| **Sécurité** | Injection de code (XSS) si la chaîne contient des données non fiables |
| **Performances** | Empêche de nombreuses optimisations du moteur |
| **Portée** | Accède à la portée locale et peut créer/modifier des variables |
| **CSP** | Bloqué par une *Content Security Policy* stricte (`unsafe-eval`) |
| **Débogage** | Code difficile à lire, tester et analyser |

> **Règle** : n'utilisez **jamais** `eval` avec des données provenant d'un utilisateur ou du réseau.

## 14.3 Alternatives sûres

```javascript
console.log(JSON.parse('{"a": 1}'));            // { a: 1 } : lire des données (au lieu de eval)

const operations = { "+": (a, b) => a + b, "-": (a, b) => a - b };
const op = "+", x = 4, y = 3;
console.log(operations[op](x, y));               // 7 : table de fonctions plutôt que code dynamique

const obj = { couleur: "rouge" };
const nomDePropriete = "couleur";
console.log(obj[nomDePropriete]);                // "rouge" : accès dynamique sans eval
```

- Pour évaluer des expressions mathématiques : une bibliothèque dédiée (ex. **math.js**) ou un analyseur maison.
- `new Function("a", "b", "return a + b")` est un peu plus isolé (portée globale uniquement) mais **présente les mêmes risques**.
- **`eval` indirect** `(0, eval)("…")` s'exécute dans la portée globale.
- En **mode strict**, `eval` a sa propre portée de variables.

---

# 15. Gestion des erreurs et mode strict

## 15.1 Types d'erreurs

| Type | Cause |
| --- | --- |
| `SyntaxError` | Code invalide |
| `ReferenceError` | Variable inexistante / en TDZ |
| `TypeError` | Opération sur un mauvais type (`null.x`) |
| `RangeError` | Valeur hors limites (`new Array(-1)`) |
| `URIError` | Mauvais usage de `encodeURI` / `decodeURI` |
| `EvalError` | Historique (`eval`) |
| `AggregateError` | Regroupe plusieurs erreurs (`Promise.any`) |

## 15.2 `try` / `catch` / `finally`

```javascript
const texte = "{ pas du JSON";

try {
    const donnees = JSON.parse(texte);
    console.log(donnees);
} catch (erreur) {
    console.error(erreur.name, erreur.message);   // SyntaxError ...
} finally {
    console.log("Toujours exécuté");
}

try { JSON.parse("{"); } catch { console.error("JSON invalide (liaison facultative : l'erreur ne sert pas)"); }
```

## 15.3 Lever et personnaliser des erreurs

```javascript
function diviser(a, b) {
    if (b === 0) throw new RangeError("Division par zéro");
    return a / b;
}

class ErreurValidation extends Error {
    constructor(message, champ, options) {
        super(message, options);
        this.name = "ErreurValidation";
        this.champ = champ;
    }
}

try {
    console.log(diviser(6, 3));    // 2
    console.log(diviser(1, 0));    // lève une RangeError
} catch (e) {
    console.error(e.name, e.message);   // RangeError Division par zéro
}

try {
    throw new ErreurValidation("Champ obligatoire", "email");
} catch (e) {
    console.error(e.name, e.champ, e.message);   // ErreurValidation email Champ obligatoire
    console.log(e instanceof ErreurValidation);  // true
}

try {
    try { JSON.parse("{"); }
    catch (e) { throw new Error("Configuration illisible", { cause: e }); }   // cause (ES2022)
} catch (e) {
    console.error(e.message, "<-", e.cause.name);   // Configuration illisible <- SyntaxError
}
```

Propriétés utiles : `name`, `message`, `stack`, `cause`.
`Error.isError(valeur)` *(ES2026)* teste de façon fiable si une valeur est une erreur, même venant d'un autre contexte (iframe).

## 15.4 Erreurs asynchrones

```javascript
const url = "https://jsonplaceholder.typicode.com/todos/99999";   // cette ressource n'existe pas (404)

// Avec async/await
(async () => {
    try {
        const r = await fetch(url);
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
    } catch (e) {
        console.error("async/await :", e.message);   // HTTP 404
    }
})();

// Avec les promesses
fetch(url)
    .then((r) => { if (!r.ok) throw new Error(`HTTP ${r.status}`); })
    .catch((e) => console.error("promesses :", e.message));

// Filets de sécurité globaux
if (typeof window !== "undefined") {
    window.addEventListener("error", (e) => console.error("Erreur non interceptée :", e.message));
    window.addEventListener("unhandledrejection", (e) => console.error("Promesse rejetée :", e.reason));
} else {
    process.on("uncaughtException", (e) => console.error("Erreur non interceptée :", e.message));
    process.on("unhandledRejection", (raison) => console.error("Promesse rejetée :", raison));
}
```

## 15.5 Mode strict (`"use strict"`)

Le **mode strict** rend le langage plus sûr : il transforme des erreurs silencieuses en exceptions.

```javascript
"use strict";                  // en début de fichier ou de fonction

// Exécute un code fautif et affiche l'erreur levée
const essayer = (description, code) => {
    try {
        code();
    } catch (e) {
        console.error(`${description} : ${e.name}`);
    }
};

essayer("variable non déclarée", () => { x = 10; });                          // ReferenceError
essayer("suppression de Object.prototype", () => { delete Object.prototype; });   // TypeError
essayer("paramètres dupliqués", () => new Function('"use strict"; function f(a, a) {}'));   // SyntaxError
essayer("écriture sur un objet gelé", () => {
    const o = Object.freeze({ a: 1 });
    o.a = 2;                                                                   // TypeError (silencieux hors mode strict)
});
```

| Changement en mode strict | Effet |
| --- | --- |
| Variables non déclarées | Erreur |
| `this` d'une fonction simple | `undefined` (au lieu de `globalThis`) |
| Écritures interdites (`freeze`, propriétés en lecture seule) | Erreur |
| Mots réservés futurs (`let`, `static`, `implements`…) | Interdits comme identifiants |
| Octal `010`, `with` | Interdits |
| `arguments` | Non lié aux paramètres |

> **Les modules ES et les classes sont automatiquement en mode strict** : le `"use strict"` explicite n'est plus nécessaire dans du code moderne.

## 15.6 Bonnes pratiques

- Attrapez les erreurs **là où vous pouvez les traiter**.
- Ne **taisez** jamais une erreur (`catch {}` vide).
- Lancez des objets `Error` (jamais des chaînes).
- Journalisez avec contexte, affichez des messages **compréhensibles** à l'utilisateur.

---

# 16. JavaScript asynchrone

## 16.1 Synchrone, asynchrone et boucle d'événements

JavaScript exécute le code sur **un seul fil**. Les opérations longues (réseau, minuteries, fichiers) sont déléguées, puis leurs *callbacks* sont replacés dans des files traitées par la **boucle d'événements** (*event loop*).

Ordre d'exécution : **pile d'appels** → **microtâches** (`Promise.then`, `queueMicrotask`) → **macrotâches** (`setTimeout`, événements).

```javascript
console.log("1");
setTimeout(() => console.log("4 (macrotâche)"), 0);
Promise.resolve().then(() => console.log("3 (microtâche)"));
console.log("2");
// Ordre d'affichage : 1, 2, 3, 4
```

## 16.2 Minuteries

```javascript
const id = setTimeout(() => console.log("Jamais affiché"), 2000);
clearTimeout(id);                                    // annulé avant l'échéance

let n = 0;
const iv = setInterval(() => {
    console.log("Tick", ++n);                        // toutes les secondes
    if (n === 3) clearInterval(iv);                  // arrêt après 3 exécutions
}, 1000);

setTimeout((a, b) => console.log(a + b), 100, 1, 2); // arguments supplémentaires : affiche 3
```

### `setTimeout` récursif vs `setInterval`

`setInterval` ne tient pas compte de la durée du traitement : les appels peuvent s'empiler. Un `setTimeout` **récursif** garantit un délai entre la **fin** d'un traitement et le début du suivant :

```javascript
let essais = 0;
const faireQuelqueChose = () => Promise.resolve(console.log("Tâche n°", ++essais));

function boucle() {
    if (essais >= 3) return;                         // arrêt pour l'exemple
    faireQuelqueChose().finally(() => setTimeout(boucle, 1000));
}
boucle();
```

> **Attention :** Le délai est un **minimum** (non garanti). Les onglets en arrière-plan ralentissent les minuteries. Pour l'animation, utilisez **`requestAnimationFrame`**.

## 16.3 *Callbacks* (rappels)

```javascript
function lireDonnees(callback) {
    setTimeout(() => callback(null, { id: 1 }), 500);
}
lireDonnees((err, data) => {
    if (err) return console.error(err);
    console.log(data);                               // { id: 1 }
});
```

Imbriqués, ils mènent à l'**enfer des callbacks** (*callback hell*) : on leur préfère les promesses.

## 16.4 Promesses (`Promise`)

Une **promesse** représente le résultat futur d'une opération : **en attente** (*pending*) → **tenue** (*fulfilled*) ou **rejetée** (*rejected*).

```javascript
const attendre = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
attendre(500).then(() => console.log("500 ms écoulées"));

const promesse = new Promise((resolve, reject) => {
    const ok = true;
    ok ? resolve("Succès") : reject(new Error("Échec"));
});

promesse
    .then(valeur => valeur.toUpperCase())     // chaînage : retourne une nouvelle promesse
    .then(console.log)                        // "SUCCÈS"
    .catch(console.error)                     // intercepte toute erreur de la chaîne
    .finally(() => console.log("Terminé"));
```

## 16.5 `async` / `await`

Syntaxe plus lisible, basée sur les promesses. Une fonction `async` **retourne toujours une promesse**.

```javascript
async function chargerUtilisateur(id) {
    try {
        const reponse = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
        if (!reponse.ok) throw new Error(`HTTP ${reponse.status}`);
        return await reponse.json();
    } catch (e) {
        console.error("Chargement impossible :", e.message);
        throw e;
    }
}

chargerUtilisateur(1).then((u) => console.log(u.name));     // un utilisateur existant
chargerUtilisateur(99999).catch(() => console.error("Échec attendu : cet utilisateur n'existe pas"));
```

Dans un module (fichier `.mjs` ou `<script type="module">`), `await` s'utilise directement au niveau supérieur (ES2022) :

```javascript
const config = await (await fetch("https://jsonplaceholder.typicode.com/todos/1")).json();
console.log(config);
```

## 16.6 Combiner plusieurs opérations

| Méthode | Comportement |
| --- | --- |
| `Promise.all([…])` | Attend **toutes** ; rejette dès la **première** erreur |
| `Promise.allSettled([…])` | Attend toutes ; renvoie le **statut** de chacune (jamais rejetée) |
| `Promise.race([…])` | Première **terminée** (réussie ou non) |
| `Promise.any([…])` | Première **réussie** ; `AggregateError` si toutes échouent |
| `Promise.withResolvers()` | Crée `{ promise, resolve, reject }` (ES2024) |
| `Promise.try(fn)` | Exécute `fn` (synchrone ou asynchrone) et renvoie toujours une promesse (ES2025) |

```javascript
const attendre = (ms, valeur) => new Promise((resolve) => setTimeout(() => resolve(valeur), ms));
const chargerA = () => attendre(500, "A");
const chargerB = () => attendre(500, "B");

(async () => {
    // Séquentiel (lent) : B démarre seulement quand A est terminée
    console.time("séquentiel");
    const a = await chargerA();
    const b = await chargerB();
    console.timeEnd("séquentiel");                  // environ 1000 ms

    // Parallèle (rapide)
    console.time("parallèle");
    const [x, y] = await Promise.all([chargerA(), chargerB()]);
    console.timeEnd("parallèle");                   // environ 500 ms
    console.log(a, b, x, y);                        // "A" "B" "A" "B"

    const resultats = await Promise.allSettled([chargerA(), Promise.reject(new Error("échec"))]);
    console.log(resultats.filter((r) => r.status === "fulfilled"));          // la promesse tenue
    console.error(resultats.filter((r) => r.status === "rejected").map((r) => r.reason.message));   // ["échec"]
})();
```

## 16.7 Annulation et délais : `AbortController` *(ajout)*

```javascript
const url = "https://jsonplaceholder.typicode.com/todos/1";

const controleur = new AbortController();
controleur.abort();            // annulation immédiate pour l'exemple (en pratique : setTimeout(() => controleur.abort(), 5000))

(async () => {
    try {
        await fetch(url, { signal: controleur.signal });
    } catch (e) {
        if (e.name === "AbortError") console.error("Requête annulée");
        else throw e;
    }
})();

// Raccourci : annulation automatique après un délai
fetch(url, { signal: AbortSignal.timeout(5000) })
    .then((r) => console.log("Réponse reçue :", r.status));
```

## 16.8 Bonnes pratiques

- Préférez `async` / `await` aux chaînes `.then()` longues.
- **Gérez toujours les erreurs** (`try/catch` ou `.catch`) : une promesse rejetée non traitée génère un avertissement, voire un arrêt (Node.js).
- Parallélisez les tâches indépendantes avec `Promise.all`.
- Ne mettez pas de `await` dans `forEach` : utilisez `for...of` ou `Promise.all(tableau.map(...))`.
- Prévoyez **délais d'expiration** et **annulation**.

---

# 17. APIs web, `fetch` et JSON

## 17.1 Qu'est-ce qu'une API ?

Une **API** (*Application Programming Interface*) est une interface qui permet à deux programmes de communiquer. Les **API REST** utilisent HTTP et échangent généralement du **JSON**.

| Méthode HTTP | Usage |
| --- | --- |
| `GET` | Lire |
| `POST` | Créer |
| `PUT` / `PATCH` | Remplacer / modifier |
| `DELETE` | Supprimer |

| Famille de codes | Signification |
| --- | --- |
| `2xx` | Succès (`200 OK`, `201 Created`, `204 No Content`) |
| `3xx` | Redirection |
| `4xx` | Erreur client (`400`, `401`, `403`, `404`, `429`) |
| `5xx` | Erreur serveur |

## 17.2 `fetch`

```javascript
(async () => {
    const reponse = await fetch("https://jsonplaceholder.typicode.com/users");
    if (!reponse.ok) throw new Error(`Erreur HTTP ${reponse.status}`);
    const users = await reponse.json();
    console.log(users.length);                  // 10

    // fetch ne rejette PAS sur un 404 ou un 500 : il faut tester reponse.ok
    const absent = await fetch("https://jsonplaceholder.typicode.com/users/99999");
    console.log(absent.ok, absent.status);      // false 404
})();
```

> **Attention :** `fetch` ne rejette que sur une **erreur réseau** : vérifiez toujours `response.ok`.

Lecture du corps : `.json()`, `.text()`, `.blob()`, `.arrayBuffer()`, `.formData()` (une seule lecture possible ; `.clone()` sinon).

### Requêtes `POST`, `PUT`, `DELETE`

```javascript
const jeton = "abc123";
const id = 1;

(async () => {
    const r = await fetch("https://jsonplaceholder.typicode.com/users", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${jeton}`,
        },
        body: JSON.stringify({ nom: "Alice", age: 30 }),
        signal: AbortSignal.timeout(8000),
    });
    console.log(r.status, await r.json());      // 201 { nom: "Alice", age: 30, id: 11 }

    const suppression = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`, { method: "DELETE" });
    console.log(suppression.status);            // 200
})();
```

### Paramètres d'URL

```javascript
const url = new URL("https://api.exemple.com/search");
url.searchParams.set("q", "café & thé");     // encodage automatique
console.log(url.href);                       // https://api.exemple.com/search?q=caf%C3%A9+%26+th%C3%A9
console.log(URL.canParse("https://exemple.com"));   // true : validation
console.log(URL.canParse("pas une url"));           // false
```

### Fonction utilitaire réutilisable

```javascript
async function requeteJSON(url, options = {}) {
    const r = await fetch(url, { headers: { Accept: "application/json" }, ...options });
    if (!r.ok) throw new Error(`HTTP ${r.status} – ${await r.text()}`);
    return r.status === 204 ? null : r.json();
}

requeteJSON("https://jsonplaceholder.typicode.com/todos/1").then(console.log);
requeteJSON("https://jsonplaceholder.typicode.com/todos/99999").catch((e) => console.error(e.message));   // HTTP 404 – {}
```

### Sécurité et CORS

- Les requêtes entre origines différentes sont soumises au **CORS** : le serveur doit autoriser l'origine (`Access-Control-Allow-Origin`).
- **Ne mettez jamais de clé secrète** dans du JavaScript client : tout visiteur peut la lire.
- Pour envoyer des cookies : `credentials: "include"`.

## 17.3 JSON

**JSON** (*JavaScript Object Notation*) est un format texte léger d'échange de données.

```json
{
  "nom": "Alice",
  "age": 30,
  "actif": true,
  "langues": ["fr", "en"],
  "adresse": { "ville": "Paris" },
  "note": null
}
```

Règles : clés **entre guillemets doubles**, pas de commentaires, pas de virgule finale, pas de `undefined` / fonctions / dates natives.

### `JSON.stringify()` et `JSON.parse()`

```javascript
const objet = { nom: "Alice", age: 30, mdp: "secret" };

const texte = JSON.stringify({ a: 1, b: [1, 2] });
console.log(texte);                                              // '{"a":1,"b":[1,2]}'
console.log(JSON.stringify(objet, null, 2));                     // formaté (indentation 2)
console.log(JSON.stringify(objet, ["nom", "age"]));              // ne garde que ces clés
console.log(JSON.stringify(objet, (cle, val) => (cle === "mdp" ? undefined : val)));   // retire le mot de passe

console.log(JSON.parse('{"a":1}'));                              // { a: 1 }
const avecDate = JSON.parse('{"date":"2026-10-11"}', (cle, val) => (cle === "date" ? new Date(val) : val));   // reviver
console.log(avecDate.date instanceof Date);                      // true
```

Comportements à connaître :

- `Date` → chaîne ISO (via `toJSON()`) ; `Map`, `Set` → `{}` ; `undefined`, fonctions et symboles sont ignorés ; `NaN`/`Infinity` → `null`.
- **`JSON.parse` avec accès au texte source** *(ES2026)* : le *reviver* reçoit un 3ᵉ paramètre `contexte.source`, ce qui permet de lire les grands entiers sans perte de précision. `JSON.rawJSON()` permet d'écrire de tels nombres.

### Gérer les erreurs

```javascript
const entree = "{ invalide";

try {
    const data = JSON.parse(entree);
    console.log(data);
} catch (e) {
    console.error("JSON invalide :", e.message);     // SyntaxError
}
```

### Importer un fichier JSON *(ES2025)*

```javascript
// config.json (dans le même dossier) : { "port": 3000 }
import config from "./config.json" with { type: "json" };
console.log(config.port);   // 3000
```

## 17.4 Bonnes pratiques

- Validez les données reçues (bibliothèques : **Zod**, **Valibot**…) ; ne faites jamais confiance à une API externe.
- Prévoyez les états *chargement*, *erreur* et *vide* dans l'interface.
- Mettez en cache et limitez le débit (*debounce*) pour les recherches en direct.
- Utilisez toujours HTTPS.

---

# 18. Constructeurs, prototypes et héritage

## 18.1 Rappel : les objets

Il existe plusieurs façons de créer des objets :

```javascript
function Personne(nom, age) {
    this.nom = nom;
    this.age = age;
}

const litteral = { nom: "Alice" };                    // littéral : le plus courant
const vide = Object.create(null);                     // sans prototype
const instance = new Personne("Alice", 30);           // constructeur

console.log(litteral, Object.getPrototypeOf(vide), instance);
// { nom: "Alice" } null Personne { nom: "Alice", age: 30 }
```

## 18.2 Fonctions constructeurs

Une **fonction constructeur** (nom en `PascalCase`) crée des objets similaires avec `new`.

```javascript
function Personne(nom, age) {
    this.nom = nom;
    this.age = age;
}

const alice = new Personne("Alice", 30);
console.log(alice);                      // Personne { nom: "Alice", age: 30 }
```

### Ce que fait `new`

1. Crée un **nouvel objet vide**.
2. Lie son **prototype** à `Personne.prototype`.
3. Exécute le constructeur avec `this` = ce nouvel objet.
4. Retourne l'objet (sauf si le constructeur renvoie lui-même un objet).

> **Attention :** Oublier `new` fait pointer `this` vers `undefined` (mode strict) ou `globalThis`. Protégez-vous avec `if (!new.target) throw …` ou utilisez une **classe** (qui refuse l'appel sans `new`).

## 18.3 Prototypes et chaîne de prototypes

Chaque objet possède un **prototype** (accessible par `Object.getPrototypeOf(obj)`), qui lui-même a un prototype, etc. jusqu'à `null` : c'est la **chaîne de prototypes**. Quand une propriété est introuvable sur l'objet, JavaScript la cherche dans sa chaîne.

```javascript
function Personne(nom, age) {
    this.nom = nom;
    this.age = age;
}
const alice = new Personne("Alice", 30);

// Les méthodes partagées se placent sur le prototype (une seule copie en mémoire)
Personne.prototype.saluer = function () {
    return `Bonjour, je suis ${this.nom}`;
};

console.log(alice.saluer());                                         // trouvé via le prototype
console.log(Object.getPrototypeOf(alice) === Personne.prototype);    // true
console.log(alice.hasOwnProperty("saluer"));                         // false
console.log(Object.hasOwn(alice, "nom"));                            // true
```

> **Attention :** N'utilisez pas `__proto__` dans du nouveau code : préférez `Object.getPrototypeOf` / `Object.setPrototypeOf`.

### Héritage avec les prototypes

```javascript
function Personne(nom, age) {
    this.nom = nom;
    this.age = age;
}
Personne.prototype.saluer = function () {
    return `Bonjour, je suis ${this.nom}`;
};

function Etudiant(nom, age, filiere) {
    Personne.call(this, nom, age);          // appel du « super constructeur »
    this.filiere = filiere;
}
Etudiant.prototype = Object.create(Personne.prototype);
Etudiant.prototype.constructor = Etudiant;  // rétablir la référence

console.log(new Etudiant("Bob", 20, "Maths").saluer());   // "Bonjour, je suis Bob"
```

Aujourd'hui, on utilise de préférence la syntaxe **`class ... extends`** (voir [section 19](#19-classes-et-programmation-orientée-objet)), qui est du sucre syntaxique sur ce mécanisme.

## 18.4 `Object.create`

Crée un objet avec un **prototype choisi**, sans constructeur.

```javascript
const animal = {
    parler() { return `${this.nom} fait un bruit`; },
};
const chien = Object.create(animal, { nom: { value: "Rex", enumerable: true } });
console.log(chien.parler());      // "Rex fait un bruit"
```

| | Constructeur / classe | `Object.create` |
| --- | --- | --- |
| Initialisation | Via le constructeur | Manuelle |
| Héritage | `extends` / `prototype` | Prototype choisi directement |
| Usage | Types d'objets avec état | Délégation simple, objets sans prototype |

## 18.5 Constructeurs intégrés

`Object`, `Array`, `Function`, `String`, `Number`, `Boolean`, `Date`, `RegExp`, `Map`, `Set`, `Promise`, `Error`, `Proxy`…

```javascript
console.log(new Date(0));             // 1970-01-01T00:00:00.000Z
console.log(new Map([["a", 1]]));     // Map(1) { "a" => 1 }
console.log(new Set([1, 2]));         // Set(2) { 1, 2 }
console.log(new Error("msg").message);   // "msg"
```

> **Attention :** Évitez `new String("a")`, `new Number(1)`, `new Boolean(false)` : ils créent des **objets enveloppes** (*wrappers*) et non des primitives (`new Boolean(false)` est *truthy* !). Utilisez `String(x)`, `Number(x)`, `Boolean(x)` sans `new`.

Les primitives se comportent comme des objets grâce à des enveloppes temporaires : `"abc".length` crée un `String` éphémère.

## 18.6 Motifs de création

### Fabrique (*factory function*)

```javascript
function creerPersonne(nom, age) {
    return {
        nom,
        age,
        saluer() { return `Bonjour, je suis ${nom}`; },
    };
}
console.log(creerPersonne("Alice", 30).saluer());   // "Bonjour, je suis Alice"
```

**Avantages** : pas de `new` ni de `this`, confidentialité par fermeture. **Inconvénient** : une copie des méthodes par objet.

### Encapsulation par fermeture

```javascript
function creerCompte(solde = 0) {
    return {
        deposer(m) { solde += m; },
        get solde() { return solde; },      // solde n'est pas modifiable de l'extérieur
    };
}

const compte = creerCompte(100);
compte.deposer(50);
console.log(compte.solde);                  // 150

try {
    compte.solde = 1000;                    // pas de setter : erreur en mode strict, ignoré sinon
} catch (e) {
    console.error(e.name);                  // TypeError
}
console.log(compte.solde);                  // 150
```

### Factory vs constructeur

| | Fabrique | Constructeur / classe |
| --- | --- | --- |
| `new` requis | Non | Oui |
| `instanceof` | Non | Oui |
| Données privées | Fermetures | Champs `#privés` |
| Mémoire des méthodes | Copie par objet | Partagées via le prototype |

## 18.7 Membres statiques

Appartiennent au **constructeur** lui-même, pas aux instances.

```javascript
function Personne(nom, age) {
    this.nom = nom;
    this.age = age;
}

Personne.especes = "Homo sapiens";
Personne.comparerAge = (a, b) => a.age - b.age;

const groupe = [new Personne("Bob", 40), new Personne("Alice", 30)];
console.log(Personne.especes);                              // "Homo sapiens"
console.log(groupe.sort(Personne.comparerAge).map(p => p.nom));   // ["Alice", "Bob"]
```

(Avec les classes : mot-clé `static`, voir plus bas.)

## 18.8 Mixins et composition

La **composition** assemble des comportements plutôt que d'empiler des héritages (« *composition over inheritance* »).

```javascript
const peutNager = { nager() { return `${this.nom} nage`; } };
const peutVoler = { voler() { return `${this.nom} vole`; } };

class Canard { constructor(nom) { this.nom = nom; } }
Object.assign(Canard.prototype, peutNager, peutVoler);

const donald = new Canard("Donald");
console.log(donald.nager(), "/", donald.voler());   // "Donald nage / Donald vole"

// Mixin sous forme de fonction (avec classes)
const Journalisable = (Base) => class extends Base {
    journal(msg) { console.log(`[${this.constructor.name}] ${msg}`); }
};
class Service extends Journalisable(Object) {}
new Service().journal("démarré");                   // "[Service] démarré"
```

## 18.9 Tester le type : `instanceof` et `constructor`

```javascript
function Personne(nom) { this.nom = nom; }
const alice = new Personne("Alice");
const x = new Date();

console.log(alice instanceof Personne);                    // true : Personne.prototype est dans la chaîne
console.log(alice.constructor === Personne);               // true (fragile : la propriété peut être écrasée)
console.log(Personne.prototype.isPrototypeOf(alice));      // true
console.log(Array.isArray([1, 2]));                        // true : plus fiable que instanceof Array (iframes)
console.log(Object.prototype.toString.call(x));            // "[object Date]"
```

Limites : `instanceof` échoue entre **contextes différents** (iframes), et `constructor` est écrasé si on remplace le prototype sans le rétablir.

Personnaliser `instanceof` :

```javascript
class Pair { static [Symbol.hasInstance](n) { return n % 2 === 0; } }
console.log(2 instanceof Pair);   // true
console.log(3 instanceof Pair);   // false
```

## 18.10 Usages avancés : `Proxy` et `Reflect` *(ajout)*

Un **`Proxy`** intercepte les opérations sur un objet (lecture, écriture, appel, `new`…).

```javascript
const surveille = new Proxy({}, {
    get(cible, cle, recepteur) {
        console.log(`Lecture de ${String(cle)}`);
        return Reflect.get(cible, cle, recepteur);
    },
    set(cible, cle, valeur) {
        if (cle === "age" && valeur < 0) throw new RangeError("Âge invalide");
        return Reflect.set(cible, cle, valeur);
    },
});

surveille.nom = "Alice";
console.log(surveille.nom);        // "Lecture de nom", puis "Alice"

try {
    surveille.age = -5;
} catch (e) {
    console.error(e.name, e.message);   // RangeError Âge invalide
}
```

Utilisé par les frameworks de réactivité (Vue 3) et pour la validation.

## 18.11 Déboguer les constructeurs et prototypes

```javascript
function Personne(nom) { this.nom = nom; }
Personne.prototype.saluer = function () { return `Bonjour, je suis ${this.nom}`; };
const alice = new Personne("Alice");

console.dir(alice);                                       // inspection détaillée (avec [[Prototype]] dans les DevTools)
console.log(Object.getPrototypeOf(alice));                // { saluer: [Function (anonymous)] }
console.log(Object.getOwnPropertyNames(Personne.prototype));   // ["constructor", "saluer"]
console.log(alice.constructor.name);                      // "Personne"
```

Dans les **DevTools** (F12 → *Sources*), posez des points d'arrêt dans le constructeur et inspectez `[[Prototype]]` dans le panneau des variables.

Erreurs fréquentes : oubli de `new`, `this` perdu dans un callback, prototype remplacé sans `constructor`, méthodes définies dans le constructeur (gaspillage mémoire).

---

# 19. Classes et programmation orientée objet

## 19.1 Définir une classe

Les **classes** (ES2015) sont une syntaxe claire au-dessus des prototypes.

```javascript
class Personne {
    // Champ public avec valeur par défaut
    espece = "humain";
    // Champ privé (ES2022) : inaccessible de l'extérieur
    #age;

    // Champ statique
    static compteur = 0;

    constructor(nom, age) {
        this.nom = nom;
        this.#age = age;
        Personne.compteur++;
    }

    // Méthode d'instance (placée sur le prototype)
    saluer() {
        return `Bonjour, je suis ${this.nom}`;
    }

    // Accesseurs
    get age() { return this.#age; }
    set age(valeur) {
        if (valeur < 0) throw new RangeError("Âge invalide");
        this.#age = valeur;
    }

    // Méthode privée
    #secret() { return "caché"; }
    reveler() { return this.#secret(); }      // seule la classe peut appeler #secret()

    // Méthode statique
    static creerAnonyme() { return new Personne("Anonyme", 0); }

    // Bloc d'initialisation statique (ES2022)
    static { Personne.registre = new Map(); }

    toString() { return `${this.nom} (${this.#age} ans)`; }
}

const alice = new Personne("Alice", 30);
console.log(alice.saluer());                  // "Bonjour, je suis Alice"
alice.age = 31;
console.log(alice.age);                       // 31
console.log(String(alice));                   // "Alice (31 ans)"
console.log(alice.reveler());                 // "caché"
console.log(Personne.creerAnonyme().nom);     // "Anonyme"
console.log(Personne.compteur);               // 2
console.log(Personne.registre instanceof Map);   // true

try {
    alice.age = -1;                           // le setter refuse la valeur
} catch (e) {
    console.error(e.name, e.message);         // RangeError Âge invalide
}

try {
    new Function("p", "return p.#age;");      // champ privé utilisé hors de la classe
} catch (e) {
    console.error(e.name);                    // SyntaxError
}
```

> **À retenir :** Les classes sont **toujours en mode strict**, **ne sont pas hoistées** de la même manière que les fonctions (TDZ) et **ne peuvent pas être appelées sans `new`**.

### Expression de classe

```javascript
const Animal = class {
    parler() { return "..."; }
};
console.log(new Animal().parler());   // "..."
console.log(Animal.name);             // "Animal"
```

## 19.2 Héritage : `extends` et `super`

```javascript
class Personne {
    constructor(nom, age) {
        this.nom = nom;
        this.age = age;
    }
    saluer() { return `Bonjour, je suis ${this.nom}`; }
}

class Etudiant extends Personne {
    constructor(nom, age, filiere) {
        super(nom, age);            // obligatoire avant d'utiliser this
        this.filiere = filiere;
    }

    saluer() {                       // redéfinition (override)
        return `${super.saluer()} et j'étudie ${this.filiere}`;
    }
}

const bob = new Etudiant("Bob", 20, "Maths");
console.log(bob.saluer());           // "Bonjour, je suis Bob et j'étudie Maths"
console.log(bob instanceof Personne);   // true
```

On peut étendre des classes natives (`Array`, `Error`, `Map`…).

## 19.3 Membres statiques et héritage

```javascript
class Maths {
    static PI = 3.14159;
    static carre(x) { return x * x; }
    static #privee() { return "statique privée"; }    // ES2022
    static test() { return Maths.#privee(); }
}
console.log(Maths.carre(4));    // 16
console.log(Maths.PI);          // 3.14159
console.log(Maths.test());      // "statique privée"
```

Les membres statiques sont **hérités** par les sous-classes (`class B extends Maths`). Usages : utilitaires, fabriques, compteurs, constantes.

## 19.4 Encapsulation

| Mécanisme | Description |
| --- | --- |
| **Champs / méthodes `#privés`** (recommandé) | Vraiment inaccessibles de l'extérieur (garanti par le langage) |
| Convention `_nom` | Simple indication « usage interne » (non protégé) |
| Fermetures | Variables privées dans une fonction fabrique |
| `Symbol` / `WeakMap` | Techniques anciennes pour la confidentialité |

```javascript
class Compte {
    #solde = 0;
    deposer(m) { if (m <= 0) throw new Error("Montant invalide"); this.#solde += m; return this; }
    get solde() { return this.#solde; }
    static estCompte(o) { return #solde in o; }     // test de marque privée (ES2022)
}

const compte = new Compte().deposer(50).deposer(25);   // chaînage grâce à « return this »
console.log(compte.solde);                  // 75
console.log(Compte.estCompte(compte));      // true
console.log(Compte.estCompte({}));          // false

try {
    compte.deposer(-5);
} catch (e) {
    console.error(e.message);               // "Montant invalide"
}
```

## 19.5 Abstraction

Exposer une interface simple et masquer les détails. JavaScript n'a pas de classes abstraites natives : on simule.

```javascript
class Forme {
    constructor() {
        if (new.target === Forme) throw new TypeError("Forme est abstraite");
    }
    aire() { throw new Error("À implémenter"); }
    decrire() { return `Aire : ${this.aire().toFixed(2)}`; }
}

class Cercle extends Forme {
    constructor(r) { super(); this.r = r; }
    aire() { return Math.PI * this.r ** 2; }
}

console.log(new Cercle(1).decrire());   // "Aire : 3.14"

try {
    new Forme();                        // une classe abstraite ne s'instancie pas
} catch (e) {
    console.error(e.name, e.message);   // TypeError Forme est abstraite
}
```

## 19.6 Polymorphisme et *duck typing*

```javascript
class Forme { aire() { throw new Error("À implémenter"); } }

class Cercle extends Forme {
    constructor(r) { super(); this.r = r; }
    aire() { return Math.PI * this.r ** 2; }
}

class Rectangle extends Forme {
    constructor(l, h) { super(); this.l = l; this.h = h; }
    aire() { return this.l * this.h; }
}

const formes = [new Cercle(1), new Rectangle(2, 3)];
console.log(formes.map(f => f.aire()));       // [3.141592653589793, 6] : chaque objet répond à sa manière
```

> En JavaScript, ce qui compte est **ce que l'objet sait faire**, pas sa classe.

## 19.7 Méthodes et symboles spéciaux

| Symbole / méthode | Rôle |
| --- | --- |
| `toString()` / `[Symbol.toPrimitive]` | Conversion en texte / valeur primitive |
| `toJSON()` | Personnalise `JSON.stringify` |
| `[Symbol.iterator]` | Rend l'objet itérable |
| `[Symbol.asyncIterator]` | Itérable asynchrone |
| `[Symbol.hasInstance]` | Personnalise `instanceof` |
| `valueOf()` | Valeur utilisée dans les opérations |

## 19.8 Gestion explicite des ressources : `using` *(nouveauté)*

Le mot-clé **`using`** (*Explicit Resource Management*) libère automatiquement une ressource à la fin du bloc, via `[Symbol.dispose]()`. Il a atteint le stade 4 en 2026 (publication prévue dans ES2027). Vérifiez la prise en charge dans vos environnements.

```javascript
function ouvrirFichier(nom) {
    console.log("ouverture de", nom);
    return { nom, [Symbol.dispose]() { console.log("fermeture de", nom); } };
}

{
    using fichier = ouvrirFichier("a.txt");     // fichier[Symbol.dispose]() est appelé à la sortie du bloc
    console.log("travail avec", fichier.nom);
}
// ouverture de a.txt, travail avec a.txt, puis fermeture de a.txt

// Pour les ressources asynchrones : « await using » avec Symbol.asyncDispose
```

## 19.9 Classes ou fonctions ? Quand utiliser quoi

| Situation | Choix conseillé |
| --- | --- |
| Entité avec **état** et comportements liés, héritage | **Classe** |
| Simple transformation de données | **Fonctions pures** |
| Données privées légères | Fabrique + fermeture |
| Assemblage de comportements | Composition / mixins |

## 19.10 Bonnes pratiques

- Une classe = **une responsabilité**, petite et cohérente.
- Préférez la **composition** à l'héritage profond.
- Utilisez les **champs privés `#`** pour protéger l'état.
- Définissez `toString()` / `toJSON()` si nécessaire.
- Appelez `super()` en premier dans un constructeur dérivé.

---

# 20. Modules (`import` / `export`)

## 20.1 Pourquoi des modules ?

Les **modules ES** (ESM) découpent le code en fichiers réutilisables, avec leur **propre portée** (pas de pollution globale), des dépendances **explicites** et un chargement optimisé.

## 20.2 Activer les modules

```html
<script type="module" src="main.js"></script>
```

- **Navigateur** : `type="module"` ; les modules sont **différés** par défaut, en **mode strict**, et servis via **HTTP(S)** (pas `file://`).
- **Node.js** : extension **`.mjs`**, ou `"type": "module"` dans `package.json`.

## 20.3 `export`

```javascript
// maths.js
export const PI = 3.14159;
export function additionner(a, b) { return a + b; }
export class Calculatrice {
    multiplier(a, b) { return a * b; }
}

// Export par défaut (un seul par module)
export default function soustraire(a, b) { return a - b; }

// Regroupés / renommés
export { additionner as somme, PI as PI_COURT };
export * from "./autres.js";                  // réexporter (autres.js : export const E = 2.718;)
```

## 20.4 `import`

```javascript
// main.js (à côté de maths.js et autres.js)
import soustraire from "./maths.js";                  // défaut
import { PI, additionner } from "./maths.js";         // nommés
import { additionner as plus } from "./maths.js";     // alias
import * as maths from "./maths.js";                  // tout, dans un espace de noms
import "./effets-de-bord.js";                         // exécution seule (effets-de-bord.js : console.log("chargé");)

console.log(soustraire(5, 3));        // 2
console.log(PI, additionner(2, 3));   // 3.14159 5
console.log(plus(1, 1));              // 2
console.log(maths.E, maths.somme(4, 4));   // 2.718 8
```

> Le **chemin relatif** doit commencer par `./` ou `../` et inclure l'**extension** `.js`.

### Import dynamique (chargement à la demande)

```javascript
// graphique.js : export function dessiner() { console.log("Graphique dessiné"); }
document.body.innerHTML = `<button id="graphique">Afficher le graphique</button>`;

const bouton = document.querySelector("#graphique");
bouton.addEventListener("click", async () => {
    const { dessiner } = await import("./graphique.js");     // code chargé seulement au clic
    dessiner();                                              // "Graphique dessiné"
});
bouton.click();                                              // simule le clic
```

### Import de JSON et attributs d'import

```javascript
// donnees.json (dans le même dossier) : { "total": 3 }
import donnees from "./donnees.json" with { type: "json" };
console.log(donnees.total);   // 3
```

## 20.5 Fonctionnement

- **Liaisons vivantes** (*live bindings*) : un import est une **référence** à la variable exportée ; si le module exportateur la modifie, les importateurs voient le changement. On ne peut pas la réaffecter depuis l'importateur.
- Chaque module n'est **évalué qu'une seule fois** (mis en cache).
- **Dépendances circulaires** possibles mais à éviter.
- `import.meta.url` : URL du module courant ; `import.meta.dirname` / `filename` dans Node.js.
- **`await` au niveau supérieur** est autorisé dans les modules.

## 20.6 Modules ES et CommonJS

| | ESM | CommonJS (Node historique) |
| --- | --- | --- |
| Syntaxe | `import` / `export` | `require()` / `module.exports` |
| Chargement | Statique, asynchrone | Dynamique, synchrone |
| Standard | Oui | Spécifique à Node |

Node.js permet désormais de `require()` des modules ES synchrones, ce qui facilite la cohabitation.

## 20.7 Structure de projet type

```text
projet/
├── index.html
├── package.json
└── src/
    ├── main.js
    ├── utils/
    │   └── format.js
    └── composants/
        └── bouton.js
```

## 20.8 Pièges courants

| Problème | Solution |
| --- | --- |
| *Failed to load module script* (`file://`, CORS) | Servir via un serveur local (`npx vite`, `python -m http.server`) |
| Extension `.js` oubliée | L'ajouter dans le chemin d'import |
| `import` hors module (« Cannot use import statement outside a module ») | `type="module"` ou `.mjs` |
| `export default` + nommés mélangés | Rester cohérent dans le projet |
| Dépendances circulaires | Réorganiser le code |

---

# 21. DOM et événements

## 21.1 Qu'est-ce que le DOM ?

Le **DOM** (*Document Object Model*) représente la page HTML sous forme **d'arbre d'objets** que JavaScript peut lire et modifier. Le point d'entrée est l'objet **`document`**.

```text
document
 └── html
      ├── head
      └── body
           ├── h1
           └── div#app
                └── p.texte
```

Types de nœuds : **élément**, **texte**, **commentaire**, **document**.

## 21.2 Sélectionner des éléments

```javascript
document.body.innerHTML = `
    <div class="conteneur">
        <p id="titre" class="carte actif">Premier</p>
        <p class="carte">Second</p>
    </div>`;

const element = document.querySelector("#titre");

console.log(document.querySelector("#titre"));                // premier correspondant (sélecteur CSS)
console.log(document.querySelectorAll(".carte").length);      // 2 : NodeList (itérable) de tous
console.log(document.getElementById("titre") === element);    // true
console.log(element.closest(".conteneur"));                   // ancêtre le plus proche
console.log(element.matches(".actif"));                       // true : correspond au sélecteur ?
console.log(element.parentElement.children.length, element.nextElementSibling.textContent);   // 2 "Second"
```

> `getElementsByClassName` / `getElementsByTagName` renvoient des **collections vivantes** (`HTMLCollection`) qui se mettent à jour automatiquement ; `querySelectorAll` renvoie une liste **statique**.

## 21.3 Lire et modifier le contenu

```javascript
document.body.innerHTML = `
    <h1 id="titre">Ancien titre</h1>
    <div id="conteneur"></div>
    <a id="lien" href="/ancien" disabled>Lien</a>
    <input id="champ" type="checkbox" checked>`;

const titre = document.querySelector("#titre");
const conteneur = document.querySelector("#conteneur");
const element = document.querySelector("#lien");
const input = document.querySelector("#champ");

titre.textContent = "Nouveau titre";                 // sûr : traite le texte comme du texte
console.log(titre.textContent);

conteneur.innerHTML = "<b>Gras</b>";                  // interprète le HTML : risque de XSS avec des données non fiables
console.log(conteneur.children.length);               // 1 (un élément <b> a été créé)
conteneur.textContent = "<b>Gras</b>";                // affiché tel quel, sans créer d'élément
console.log(conteneur.children.length);               // 0

element.setAttribute("href", "/accueil");
console.log(element.getAttribute("href"));            // "/accueil"
element.removeAttribute("disabled");
element.dataset.userId = "42";                        // attribut data-user-id
console.log(element.outerHTML);                       // <a id="lien" href="/accueil" data-user-id="42">Lien</a>
console.log(input.checked);                           // true (champs de formulaire : value, checked)
```

> **N'insérez jamais de saisie utilisateur avec `innerHTML`.** Utilisez `textContent`, ou créez des éléments avec `createElement`, ou assainissez le HTML (API *Sanitizer* / bibliothèque DOMPurify).

## 21.4 Créer, insérer et supprimer

```javascript
document.body.innerHTML = `
    <ul id="liste"><li id="reference">Référence</li></ul>
    <template id="modele"><li>Depuis le modèle</li></template>`;

const liste = document.querySelector("#liste");
const reference = document.querySelector("#reference");
const modele = document.querySelector("#modele");
const creerLi = (texte) => Object.assign(document.createElement("li"), { textContent: texte });

const li = creerLi("Nouvel élément");
li.classList.add("item");

liste.append(li, "texte");                 // à la fin (accepte plusieurs nœuds / textes)
liste.prepend(creerLi("Premier"));         // au début
reference.before(creerLi("Avant la référence"));
reference.after(creerLi("Après la référence"));
reference.replaceWith(creerLi("Remplaçant"));
li.remove();                               // supprimer
liste.insertAdjacentHTML("beforeend", "<li>Rapide</li>");   // beforebegin | afterbegin | beforeend | afterend

liste.append(modele.content.cloneNode(true));          // avec <template>

const fragment = document.createDocumentFragment();    // regrouper avant insertion (moins de reflows)
for (let i = 1; i <= 3; i++) fragment.append(creerLi(`Lot ${i}`));
liste.append(fragment);

console.log([...liste.children].map(e => e.textContent));
```

## 21.5 Classes et styles

```javascript
document.body.innerHTML = `<div id="boite" class="a cache">Boîte</div>`;
const element = document.querySelector("#boite");

element.classList.add("actif");
element.classList.remove("cache");
element.classList.toggle("ouvert");
console.log(element.classList.contains("actif"));     // true
element.classList.replace("a", "b");
console.log(element.className);                       // "b actif ouvert"

element.style.color = "red";                          // style en ligne
element.style.setProperty("--couleur", "tomato");     // variable CSS
console.log(getComputedStyle(element).color);         // "rgb(255, 0, 0)" : style calculé (lecture)
```

> **Bonne pratique :** Préférez **basculer des classes CSS** plutôt que manipuler `style` directement.

## 21.6 Dimensions et positionnement

```javascript
document.body.innerHTML = `<div id="boite" style="width: 200px; height: 100px; overflow: auto;">Boîte</div>`;
const element = document.querySelector("#boite");

console.log(element.getBoundingClientRect());    // { x, y, width, height, top, left… } relatif à la fenêtre
console.log(element.offsetWidth, element.clientHeight);
console.log(element.scrollHeight, element.scrollTop);
element.scrollIntoView({ behavior: "smooth" });
window.scrollTo({ top: 0, behavior: "smooth" });
```

## 21.7 Les événements

```javascript
document.body.innerHTML = `<button id="bouton">Cliquer</button>`;
const bouton = document.querySelector("#bouton");

bouton.addEventListener("click", (evenement) => {
    console.log(evenement.target);          // élément réellement cliqué
    console.log(evenement.currentTarget);   // élément portant l'écouteur
    evenement.preventDefault();             // annule l'action par défaut (envoi de formulaire, lien…)
    evenement.stopPropagation();            // arrête la propagation
});
bouton.click();                             // simule un clic

function gestionnaire() { console.log("Clic géré"); }
bouton.addEventListener("click", gestionnaire);
bouton.removeEventListener("click", gestionnaire);     // il faut la MÊME référence de fonction
bouton.click();                                        // « Clic géré » n'est pas affiché
```

### Options de `addEventListener`

```javascript
document.body.innerHTML = `<button id="bouton">Cliquer</button>`;
const bouton = document.querySelector("#bouton");
const controleur = new AbortController();

const gestionnaire = () => console.log("Clic reçu");
bouton.addEventListener("click", gestionnaire, {
    once: true,                       // se désinscrit après le premier appel
    passive: true,                    // promet de ne pas appeler preventDefault (scroll fluide)
    signal: controleur.signal,        // désinscription groupée via AbortController
});

bouton.click();                       // "Clic reçu"
bouton.click();                       // rien : l'écouteur était « once »
controleur.abort();                   // retire en une fois tous les écouteurs liés à ce signal
```

### Événements courants

| Catégorie | Événements |
| --- | --- |
| **Souris / pointeur** | `click`, `dblclick`, `contextmenu`, `pointerdown`, `pointermove`, `pointerup`, `mouseenter`, `mouseleave` |
| **Clavier** | `keydown`, `keyup` (`event.key`, `event.code`) |
| **Formulaire** | `input`, `change`, `submit`, `focus`, `blur`, `reset` |
| **Fenêtre / document** | `DOMContentLoaded`, `load`, `resize`, `scroll`, `beforeunload`, `visibilitychange` |
| **Tactile** | `touchstart`, `touchmove`, `touchend` (ou événements *pointer*) |
| **Glisser-déposer** | `dragstart`, `dragover`, `drop` |
| **Média / réseau** | `play`, `pause`, `online`, `offline` |

> **Bonne pratique :** Préférez les **événements Pointer** (`pointerdown`…) qui unifient souris, tactile et stylet.

### Propagation : capture, cible, bulle

Un événement traverse l'arbre : **capture** (de `window` vers la cible) → **cible** → **bulle** (retour vers `window`). Par défaut, les écouteurs réagissent pendant la **bulle** ; `{ capture: true }` écoute pendant la capture.

### Délégation d'événements

Un seul écouteur sur le parent gère tous les enfants (même ajoutés plus tard) :

```javascript
document.body.innerHTML = `<ul id="liste"><li>Pomme</li><li>Poire</li></ul>`;
const liste = document.querySelector("#liste");

// Un seul écouteur sur le parent gère aussi les éléments ajoutés plus tard
liste.addEventListener("click", (e) => {
    const item = e.target.closest("li");
    if (!item || !liste.contains(item)) return;
    console.log("Clic sur", item.textContent);
});

liste.querySelector("li:last-child").click();     // "Clic sur Poire"
```

### Événements personnalisés

```javascript
document.body.innerHTML = `<div id="panier"></div>`;
const element = document.querySelector("#panier");

element.addEventListener("commande:ajoutee", e => console.log(e.detail.id));    // 7
element.dispatchEvent(new CustomEvent("commande:ajoutee", { detail: { id: 7 }, bubbles: true }));
```

### Formulaires

```javascript
document.body.innerHTML = `
    <form id="formulaire">
        <input name="nom" value="Alice">
        <input name="age" value="30">
    </form>`;
const formulaire = document.querySelector("#formulaire");

formulaire.addEventListener("submit", (e) => {
    e.preventDefault();
    const donnees = new FormData(formulaire);
    const objet = Object.fromEntries(donnees);
    console.log(objet);                     // { nom: "Alice", age: "30" }
});
formulaire.requestSubmit();                 // simule l'envoi du formulaire
```

Utilisez aussi la **validation native** (`required`, `pattern`, `type="email"`, `form.checkValidity()`).

## 21.8 Quand le DOM est-il prêt ?

```javascript
function demarrer() {
    console.log("DOM construit", document.readyState);
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", demarrer);   // DOM pas encore construit : on attend
} else {
    demarrer();                                                // DOM déjà prêt : on exécute tout de suite
}
// Plus simple : <script defer> ou <script type="module"> (déjà différés)
```

## 21.9 Observateurs modernes *(ajout)*

| API | Rôle |
| --- | --- |
| `IntersectionObserver` | Détecter l'entrée d'un élément à l'écran (chargement différé, défilement infini) |
| `ResizeObserver` | Réagir aux changements de taille d'un élément |
| `MutationObserver` | Réagir aux modifications du DOM |

```javascript
document.body.innerHTML = `<p class="apparition">Je deviens visible</p>`;

const obs = new IntersectionObserver((entrees) => {
    entrees.forEach(e => {
        if (e.isIntersecting) {
            e.target.classList.add("visible");
            console.log("Visible :", e.target.textContent);
        }
    });
}, { threshold: 0.2 });
document.querySelectorAll(".apparition").forEach(el => obs.observe(el));
```

## 21.10 Shadow DOM et composants web

Le **Shadow DOM** isole structure et styles d'un composant. Associé aux **éléments personnalisés** (*Custom Elements*), il permet de créer des composants réutilisables sans framework.

```javascript
class CarteUtilisateur extends HTMLElement {
    connectedCallback() {
        const racine = this.attachShadow({ mode: "open" });
        racine.innerHTML = `
            <style>p { color: steelblue; }</style>
            <p>Bonjour, ${this.getAttribute("nom") ?? "inconnu"}</p>`;
    }
}
customElements.define("carte-utilisateur", CarteUtilisateur);

document.body.innerHTML = `<carte-utilisateur nom="Alice"></carte-utilisateur>`;
console.log(document.querySelector("carte-utilisateur").shadowRoot.querySelector("p").textContent);   // "Bonjour, Alice"
```

## 21.11 Animations

- **CSS** (transitions, `@keyframes`) : à privilégier pour les animations simples.
- **`requestAnimationFrame`** : synchronisation avec le rafraîchissement de l'écran.
- **Web Animations API** :

```javascript
document.body.innerHTML = `<div id="boite">Animation</div>`;
const element = document.querySelector("#boite");

const animation = element.animate(
    [{ opacity: 0, transform: "translateY(20px)" }, { opacity: 1, transform: "none" }],
    { duration: 400, easing: "ease-out", fill: "forwards" },
);
animation.finished.then(() => console.log("Animation terminée"));
```

## 21.12 Référence : interfaces principales

| Interface | Rôle |
| --- | --- |
| `EventTarget` | `addEventListener`, `removeEventListener`, `dispatchEvent` |
| `Node` | Base des nœuds : `parentNode`, `childNodes`, `textContent`, `cloneNode()` |
| `Element` | Éléments : `classList`, `attributes`, `querySelector`, `closest`, `getBoundingClientRect` |
| `HTMLElement` | Éléments HTML : `style`, `dataset`, `hidden`, `focus()`, `click()` |
| `Document` | La page : `body`, `head`, `title`, `createElement`, `cookie` |
| `NodeList` / `HTMLCollection` | Collections de nœuds |
| `Event` / `MouseEvent` / `KeyboardEvent` / `PointerEvent` | Types d'événements |
| `CSSStyleDeclaration` | `element.style` |

## 21.13 Bonnes pratiques

- Minimisez les accès au DOM et regroupez les modifications (fragment, classes CSS).
- Utilisez la **délégation d'événements** pour les listes dynamiques.
- Préférez `textContent` à `innerHTML` ; **assainissez** tout HTML externe.
- Pensez à l'**accessibilité** : éléments sémantiques (`<button>`, `<dialog>`), attributs ARIA, focus clavier.
- Retirez les écouteurs devenus inutiles (ou utilisez `signal`).
- Pour de grosses interfaces, utilisez un framework (React, Vue, Svelte…) ou des composants web.

---

# 22. Environnement du navigateur (BOM) et stockage

## 22.1 Le BOM

Le **BOM** (*Browser Object Model*) regroupe les objets qui permettent d'interagir avec le **navigateur** (et non avec le contenu de la page). Il n'est pas standardisé de façon unique mais est largement uniforme.

| Objet | Rôle |
| --- | --- |
| `window` | Objet global du navigateur : fenêtre, dimensions, minuteries |
| `navigator` | Infos sur le navigateur (langue, en ligne, géolocalisation, presse-papiers) |
| `location` | URL courante, navigation |
| `history` | Historique de navigation |
| `screen` | Informations sur l'écran |
| `localStorage` / `sessionStorage` | Stockage clé-valeur |

```javascript
console.log(window.innerWidth, window.innerHeight);
console.log(window.matchMedia("(prefers-color-scheme: dark)").matches);   // true si le thème sombre est actif
// window.open("https://example.com", "_blank", "noopener");   // ouvre un onglet (peut être bloqué par le navigateur)

console.log(navigator.language);                 // "fr-FR"
console.log(navigator.onLine);                   // true

navigator.clipboard.writeText("copié !")         // exige une page active et, selon le navigateur, une autorisation
    .then(() => console.log("Texte copié"))
    .catch((e) => console.error("Copie impossible :", e.message));

navigator.geolocation.getCurrentPosition(        // demande l'autorisation de l'utilisateur
    (pos) => console.log(pos.coords.latitude, pos.coords.longitude),
    (err) => console.error("Position refusée ou indisponible :", err.message),
);

console.log(location.href, location.hostname, location.pathname, location.search, location.hash);
location.hash = "#section-2";                    // change le fragment sans recharger la page
console.log(location.hash);                      // "#section-2"

// Ces appels quittent la page : ils sont rangés dans un objet et appelés seulement à la demande
const navigation = {
    avecHistorique: () => location.assign("/page"),     // navigue (garde l'historique)
    sansHistorique: () => location.replace("/page"),    // navigue (sans entrée d'historique)
    recharger: () => location.reload(),
};
// navigation.recharger();

window.addEventListener("popstate", e => console.log("popstate :", e.state));
history.pushState({ page: 2 }, "", "?page=2");   // change l'URL sans recharger (SPA)
console.log(location.search);                    // "?page=2"
history.back();                                  // déclenche popstate (état null : entrée initiale)
// history.forward();  history.go(-2);

console.log(screen.width, screen.height, screen.colorDepth);
```

### Boîtes de dialogue

`alert()`, `confirm()`, `prompt()` **bloquent** la page et sont peu esthétiques : préférez l'élément HTML **`<dialog>`** :

```javascript
document.body.innerHTML = `
    <dialog>
        <p>Bonjour depuis la boîte de dialogue</p>
        <form method="dialog"><button>Fermer</button></form>
    </dialog>`;

const boite = document.querySelector("dialog");
boite.showModal();
console.log(boite.open);     // true
```

## 22.2 Comparer les mécanismes de stockage

| | Cookie | `localStorage` | `sessionStorage` | IndexedDB |
| --- | --- | --- | --- | --- |
| Capacité | ~4 Ko | ~5 Mo | ~5 Mo | Très grande (centaines de Mo+) |
| Durée | Selon `Max-Age` | **Permanente** | **Onglet** (jusqu'à fermeture) | Permanente |
| Envoyé au serveur | Oui, à chaque requête | Non | Non | Non |
| API | Chaîne `document.cookie` | Synchrone, texte | Synchrone, texte | Asynchrone, objets |
| Accessible par | Serveur et client | Client | Client | Client |

## 22.3 Cookies

```javascript
// Écrire (chaque affectation ajoute/modifie UN cookie)
document.cookie = "theme=sombre; Max-Age=31536000; Path=/; SameSite=Lax; Secure";
document.cookie = "langue=fr; Max-Age=31536000; Path=/; SameSite=Lax; Secure";

// Lire (tous les cookies, en une chaîne)
console.log(document.cookie);       // "theme=sombre; langue=fr"
const cookies = Object.fromEntries(document.cookie.split("; ").map(c => c.split("=")));
console.log(cookies.theme);         // "sombre"

// Supprimer : durée de vie expirée
document.cookie = "theme=; Max-Age=0; Path=/";
console.log(document.cookie);       // "langue=fr"
// Remarque : avec « Secure », le cookie n'est enregistré qu'en HTTPS (ou sur localhost).
```

| Attribut | Rôle |
| --- | --- |
| `Max-Age` / `Expires` | Durée de vie |
| `Path` / `Domain` | Portée |
| `Secure` | Envoyé uniquement en HTTPS |
| `HttpOnly` | **Inaccessible à JavaScript** (défini par le serveur uniquement) |
| `SameSite` | `Strict` / `Lax` / `None` : protège contre le CSRF |

> **Sécurité :** Les cookies de **session et d'authentification** doivent être posés par le **serveur** avec `HttpOnly; Secure; SameSite`. N'y stockez jamais de données sensibles lisibles par JavaScript.
> **Remarque :** La **Cookie Store API** (`cookieStore.get()` / `.set()`) offre une alternative asynchrone moderne.

## 22.4 `localStorage`

Stockage **persistant**, propre à l'**origine** (protocole + domaine + port), de **chaînes uniquement**.

```javascript
localStorage.setItem("theme", "sombre");
console.log(localStorage.getItem("theme"));          // "sombre" (null si absent)
localStorage.removeItem("theme");
console.log(localStorage.getItem("theme"));          // null

// Objets et tableaux : sérialiser en JSON
localStorage.setItem("panier", JSON.stringify([{ id: 1, qte: 2 }]));
const panier = JSON.parse(localStorage.getItem("panier") ?? "[]");
console.log(panier);                                 // [{ id: 1, qte: 2 }]
console.log(localStorage.length, localStorage.key(0));

// Réagir aux modifications faites dans un AUTRE onglet (l'événement ne se déclenche pas dans l'onglet qui écrit)
window.addEventListener("storage", e => console.log(e.key, e.newValue));

localStorage.clear();                                // efface TOUT le stockage de ce site
console.log(localStorage.length);                    // 0
```

**Limites** : ~5 Mo, **synchrone** (bloque le fil principal), texte uniquement, **lisible par tout script de la page (XSS)**, indisponible dans certains modes de navigation privée ou si le quota est dépassé (`QuotaExceededError`).

Usages : thème, préférences, brouillons, petit cache. Ne stockez jamais de mots de passe, jetons sensibles ou données personnelles.

```javascript
function lireStockage(cle, defaut) {
    try { return JSON.parse(localStorage.getItem(cle)) ?? defaut; }
    catch { return defaut; }
}

localStorage.setItem("prefs", JSON.stringify({ theme: "sombre" }));
console.log(lireStockage("prefs", {}));              // { theme: "sombre" }
console.log(lireStockage("absent", []));             // [] : valeur par défaut
localStorage.setItem("casse", "{ pas du JSON");
console.log(lireStockage("casse", "défaut"));        // "défaut" : JSON invalide
```

## 22.5 `sessionStorage`

Même API que `localStorage`, mais les données sont **propres à l'onglet** et **supprimées à sa fermeture** (conservées lors d'un rechargement).

```javascript
sessionStorage.setItem("etape", "2");
console.log(sessionStorage.getItem("etape"));        // "2"
sessionStorage.clear();
console.log(sessionStorage.getItem("etape"));        // null
```

Usages : état d'un formulaire multi-étapes, filtres temporaires, données liées à une session d'onglet.

## 22.6 Pour aller plus loin

- **IndexedDB** (via une bibliothèque comme `idb` ou **Dexie**) pour de gros volumes ou des données structurées.
- **Cache API** et **Service Workers** pour le mode hors-ligne (PWA).

---

# 23. Dates et heures : `Date` et `Temporal`

## 23.1 L'objet `Date` (historique)

```javascript
const maintenant = new Date();
console.log(maintenant);
console.log(new Date("2026-10-11T14:30:00Z"));       // chaîne ISO 8601 (fiable)
console.log(new Date(2026, 9, 11).getMonth());       // 9 : les mois vont de 0 à 11, donc 9 = octobre
console.log(new Date(0));                            // timestamp en millisecondes (epoch 1970)
console.log(Date.now());                             // timestamp actuel
```

### Lire

| Méthode | Renvoie |
| --- | --- |
| `getFullYear()` | Année |
| `getMonth()` | Mois **0–11** |
| `getDate()` | Jour du mois 1–31 |
| `getDay()` | Jour de la semaine 0 (dimanche)–6 |
| `getHours()` `getMinutes()` `getSeconds()` `getMilliseconds()` | Heure locale |
| `getTime()` | Timestamp en ms |
| `getTimezoneOffset()` | Décalage UTC en minutes |
| `getUTC…()` | Équivalents en UTC |

### Modifier (mutent l'objet)

`setFullYear()`, `setMonth()`, `setDate()`, `setHours()`, `setMinutes()`, `setSeconds()`, `setTime()`…

```javascript
const d = new Date(2026, 0, 31);             // 31 janvier 2026
d.setMonth(d.getMonth() + 1);                // débordement : le 31 février n'existe pas
console.log(d.toLocaleDateString("fr-FR"));  // "03/03/2026" : on obtient le 3 mars, pas le 28 février
```

### Formater

```javascript
const d = new Date("2026-10-11T14:30:00Z");

console.log(d.toISOString());                                         // "2026-10-11T14:30:00.000Z"
console.log(d.toLocaleDateString("fr-FR", { dateStyle: "full", timeZone: "UTC" }));   // "dimanche 11 octobre 2026"
console.log(d.toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit", timeZone: "UTC" }));   // "14:30"
console.log(new Intl.DateTimeFormat("fr-FR", { dateStyle: "long", timeStyle: "short", timeZone: "Indian/Antananarivo" }).format(d));
// "11 octobre 2026 à 17:30"
console.log(new Intl.RelativeTimeFormat("fr", { numeric: "auto" }).format(-1, "day"));   // "hier"
```

### Différence entre deux dates

```javascript
const date1 = new Date(2026, 2, 1);
const date2 = new Date(2026, 2, 31);

const jours = Math.round((date2 - date1) / 86_400_000);   // attention : ignore les changements d'heure
console.log(jours);                                       // 30
```

### Défauts de `Date`

Mois indexés à 0, objet **mutable**, analyse de chaînes incohérente, **fuseaux horaires limités** (local ou UTC seulement), pas de calendriers non grégoriens, arithmétique source d'erreurs.

## 23.2 `Temporal` : le remplaçant moderne *(à jour)*

**`Temporal`** corrige les défauts de `Date` : objets **immuables**, mois de **1 à 12**, **vrais fuseaux horaires**, calendriers multiples, arithmétique fiable, précision à la **nanoseconde**.

> **Statut (octobre 2026)** : `Temporal` a atteint le **stade 4** de TC39 en 2026 ; sa publication officielle est prévue dans **ES2027** (ES2026 ne l'inclut pas). Il est déjà disponible dans **Firefox 139+** et **Chrome / Edge 144+** ; la prise en charge de **Safari** peut varier : vérifiez sur [caniuse.com](https://caniuse.com/temporal). Un *polyfill* existe (`@js-temporal/polyfill`).

| Type | Représente | Exemple |
| --- | --- | --- |
| `Temporal.Instant` | Un instant précis (UTC) | `Temporal.Now.instant()` |
| `Temporal.ZonedDateTime` | Date + heure + **fuseau** | `Temporal.Now.zonedDateTimeISO()` |
| `Temporal.PlainDate` | Une date sans heure | `2026-10-11` |
| `Temporal.PlainTime` | Une heure sans date | `14:30` |
| `Temporal.PlainDateTime` | Date + heure sans fuseau | |
| `Temporal.PlainYearMonth` / `PlainMonthDay` | Mois d'année / jour récurrent (anniversaire) | |
| `Temporal.Duration` | Une durée | `{ days: 3, hours: 2 }` |

```javascript
const aujourdHui = Temporal.Now.plainDateISO();            // ex. 2026-10-21
const noel = Temporal.PlainDate.from("2026-12-25");

console.log(aujourdHui.until(noel).days);                  // jours restants
console.log(aujourdHui.add({ months: 1 }).toString());     // un mois plus tard (immuable : nouvel objet)
console.log(aujourdHui.dayOfWeek);                         // 1 (lundi) à 7 (dimanche)

const reunion = Temporal.ZonedDateTime.from("2026-10-11T14:30[Indian/Antananarivo]");
console.log(reunion.withTimeZone("Europe/Paris").toString());   // conversion de fuseau

console.log(reunion.toLocaleString("fr-FR", { dateStyle: "full", timeStyle: "short" }));

const a = Temporal.PlainDate.from("2026-01-01");
const b = Temporal.PlainDate.from("2026-06-01");
console.log(Temporal.PlainDate.compare(a, b));             // -1, 0 ou 1
```

### `Date` → `Temporal`

```javascript
const instant = new Date().toTemporalInstant();            // si disponible
console.log(instant.toString());
```

> **Bonne pratique :** Pour un nouveau projet : utilisez `Temporal` (ou, en attendant, des bibliothèques comme **date-fns**, **Luxon** ou **Day.js**). Stockez et échangez les dates en **ISO 8601 / UTC**, et ne convertissez en heure locale qu'à l'**affichage**.

---

# 24. Outils et écosystème

*(Section ajoutée.)*

## 24.1 Node.js et gestionnaires de paquets

```bash
node --version              # utilisez une version LTS (ex. Node.js 24)
npm init -y                 # crée package.json
npm install lodash          # ajoute une dépendance
npm install -D vitest       # dépendance de développement
npm run build               # exécute un script de package.json
npx vite                    # exécute un outil sans l'installer globalement
```

Alternatives : **pnpm**, **Yarn**, **Bun**. Versionnez `package.json` et le fichier de verrouillage (`package-lock.json`, `pnpm-lock.yaml`), jamais `node_modules/`.

## 24.2 Outils de qualité et de build

| Besoin | Outils |
| --- | --- |
| **Serveur de dev et bundler** | **Vite**, esbuild, Rollup, webpack |
| **Lint** | **ESLint**, Biome, oxlint |
| **Formatage** | **Prettier**, Biome |
| **Tests** | **Vitest**, Jest, `node:test` (intégré à Node), Playwright (E2E) |
| **Typage** | **TypeScript** |
| **Transpilation** | Babel, SWC (pour cibler d'anciens navigateurs) |

## 24.3 TypeScript

Sur-ensemble de JavaScript ajoutant un **système de types** vérifié à la compilation. Les versions récentes de Node.js savent exécuter directement des fichiers `.ts` simples (suppression des types).

```typescript
function additionner(a: number, b: number): number {
    return a + b;
}

console.log(additionner(2, 3));   // 5
```

## 24.4 Frameworks et bibliothèques courants

| Domaine | Exemples |
| --- | --- |
| Interfaces | React, Vue, Svelte, Angular, Solid |
| Méta-frameworks | Next.js, Nuxt, SvelteKit, Astro, Remix |
| Serveur | Express, Fastify, Hono, NestJS |
| Composants natifs | Web Components, Lit |

## 24.5 Débogage

```javascript
const x = 5;
const tableau = [{ a: 1 }, { a: 2 }];
const objet = { nom: "Alice", details: { ville: "Paris" } };

console.log(x);
console.table(tableau);
console.dir(objet, { depth: null });

console.time("calcul");
let somme = 0;
for (let i = 0; i < 1_000_000; i++) somme += i;
console.timeEnd("calcul");

console.assert(x > 0, "x doit être positif");          // condition vraie : rien n'est affiché
console.assert(x < 0, "x doit être négatif");          // condition fausse : affiche « Assertion failed »
debugger;                                              // point d'arrêt dans les DevTools (sans effet s'ils sont fermés)
```

Les **DevTools** (F12) : *Console*, *Sources* (points d'arrêt), *Network* (requêtes), *Application* (cookies, stockage), *Performance*.

---

# 25. Nouveautés par version d'ECMAScript

| Édition | Année | Fonctionnalités marquantes |
| --- | --- | --- |
| **ES2015** (ES6) | 2015 | `let` / `const`, fonctions fléchées, classes, modules, promesses, gabarits, décomposition, `Map` / `Set`, générateurs, `Symbol` |
| **ES2016–2017** | 2016–17 | `**`, `includes()`, `async` / `await`, `Object.entries()` / `values()`, `padStart()` |
| **ES2018–2019** | 2018–19 | Spread d'objets, `finally()`, regex (groupes nommés, rétrospection), `flat()`, `flatMap()`, `Object.fromEntries()` |
| **ES2020** | 2020 | `?.`, `??`, `BigInt`, `globalThis`, `import()` dynamique, `matchAll()`, `Promise.allSettled()` |
| **ES2021** | 2021 | `replaceAll()`, `??=` / `\|\|=` / `&&=`, `Promise.any()`, séparateurs numériques |
| **ES2022** | 2022 | Champs et méthodes **privés `#`**, blocs `static`, `at()`, `Object.hasOwn()`, `await` de haut niveau, `Error.cause` |
| **ES2023** | 2023 | `toSorted()`, `toReversed()`, `toSpliced()`, `with()`, `findLast()` |
| **ES2024** | 2024 | `Object.groupBy()` / `Map.groupBy()`, `Promise.withResolvers()`, flag regex `v`, `isWellFormed()` |
| **ES2025** | 2025 | Assistants d'itérateurs, méthodes de `Set` (`union`…), `Promise.try()`, `RegExp.escape()`, `Float16Array`, import de JSON (`with { type: "json" }`), modificateurs et groupes nommés dupliqués en regex |
| **ES2026** | 2026 *(approuvée le 30 juin 2026)* | `Array.fromAsync()`, `Error.isError()`, `Math.sumPrecise()`, méthodes base64/hexadécimales de `Uint8Array`, `Iterator.concat()`, accès au texte source dans `JSON.parse`, `Map` / `WeakMap` `getOrInsert()` |
| **ES2027** *(en préparation)* | 2027 | `Temporal`, gestion explicite des ressources (`using`), etc. : déjà au stade 4 |

> **Note :** Les listes de fonctionnalités par édition circulent avec des contradictions sur Internet : la source de référence est le tableau des **propositions terminées** de TC39 ([github.com/tc39/proposals](https://github.com/tc39/proposals/blob/main/finished-proposals.md)). Vérifiez toujours la **compatibilité navigateur** sur [caniuse.com](https://caniuse.com) et [MDN](https://developer.mozilla.org/fr/).

## Ressources pour progresser

- **MDN Web Docs** : <https://developer.mozilla.org/fr/docs/Web/JavaScript>
- **javascript.info** (en français) : <https://fr.javascript.info>
- **Spécification** : <https://tc39.es/ecma262/>
- **Exercices** : voir la section « Ressources » en début de guide

---

<div align="center">

*Bon code !*

</div>
