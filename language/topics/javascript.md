<div align="center">

# 🟨 JavaScript — Guide complet

**Des variables aux modules, du DOM à l'asynchrone et à Temporal**

*Mis à jour pour ECMAScript 2026 (octobre 2026)*

</div>

---

## 🧰 Ressources

| Ressource | Lien |
| --- | --- |
| 📝 Exercices | [exercises](/language/exercises/javascript) |
| ✅ Solutions | [solutions](/language/solutions/javascript) |
| 🚀 Projets | [projects](/language/projects/javascript) |
| 🧩 Module : éditeur de code | [Monaco Editor](https://microsoft.github.io/monaco-editor/) |
| 📘 Référence officielle | [MDN Web Docs (fr)](https://developer.mozilla.org/fr/docs/Web/JavaScript) |
| 📜 Spécification | [ECMA-262](https://tc39.es/ecma262/) · [Propositions TC39](https://github.com/tc39/proposals) |

---

## 🗂️ Sommaire

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

> 💡 **Légende** : *(ajout)* = notion absente du guide d'origine ; *(à jour)* = pratique moderne remplaçant une ancienne.

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

> ℹ️ **JavaScript ≠ Java.** Les deux langages n'ont aucun lien, hormis le nom.
> ℹ️ **TypeScript** est un sur-ensemble typé de JavaScript, compilé (ou « dé-typé ») vers du JS. Voir [section 24](#24-outils-et-écosystème).

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
console.error("Une erreur");
```

## 1.3 Syntaxe de base

```javascript
// Commentaire sur une ligne
/* Commentaire
   sur plusieurs lignes */

let message = "Salut";   // les points-virgules sont recommandés
```

- JavaScript est **sensible à la casse** (`nom` ≠ `Nom`).
- Les identifiants commencent par une lettre, `_` ou `$` ; convention **`camelCase`** (variables, fonctions), **`PascalCase`** (classes), **`MAJUSCULES`** (constantes globales).

---

# 2. Variables et portée

## 2.1 Déclarer une variable

| Mot-clé | Portée | Réaffectation | Redéclaration | Hoisting |
| --- | --- | --- | --- | --- |
| `var` *(ancien)* | Fonction | ✅ | ✅ | Remontée, valeur `undefined` |
| `let` | **Bloc** | ✅ | ❌ | Remontée, mais en **zone morte temporelle** (TDZ) |
| `const` | **Bloc** | ❌ | ❌ | Idem `let` |

```javascript
let ville = "Tokyo";
ville = "Kyoto";               // ✅ réaffectation

const pays = "Japon";
// pays = "Corée";             // ❌ TypeError : const non réaffectable

const utilisateur = { nom: "Alice" };
utilisateur.nom = "Bob";       // ✅ l'objet reste modifiable : const protège le lien, pas le contenu
```

> ✅ **Bonne pratique** *(à jour)* : utilisez **`const` par défaut**, `let` si vous devez réaffecter, et **évitez `var`**.

## 2.2 Portée (*scope*)

```javascript
function saluer() {
    var message = "Bonjour";     // portée de fonction
}
// console.log(message);         // ❌ ReferenceError

{
    let x = 10;                  // portée de bloc
    const y = 20;
}
// console.log(x);               // ❌ ReferenceError
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

console.log(b);   // ❌ ReferenceError : b est dans la TDZ
let b = 10;

saluer();         // ✅ les déclarations de fonction sont remontées en entier
function saluer() { console.log("Salut"); }
```

## 2.4 Affectation par décomposition *(destructuring)*

```javascript
const [a, b, ...reste] = [1, 2, 3, 4];     // a=1, b=2, reste=[3, 4]
const { nom, age = 18, ville: v } = { nom: "Alice", ville: "Paris" };
// nom="Alice", age=18 (défaut), v="Paris" (renommage)

[a, b] = [b, a];                           // échange de valeurs
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

const o1 = { nom: "Tom" };
const o2 = o1;           // même objet !
o2.nom = "Jerry";
console.log(o1.nom);     // "Jerry"
```

### Copier un objet

```javascript
const copie1 = { ...o1 };                  // copie superficielle
const copie2 = Object.assign({}, o1);      // idem
const copie3 = structuredClone(o1);        // ✅ copie PROFONDE (à jour)
// JSON.parse(JSON.stringify(o)) perd les dates, Map, Set, undefined, fonctions…
```

## 3.2 L'opérateur `typeof`

```javascript
typeof "Salut";        // "string"
typeof 42;             // "number"
typeof true;           // "boolean"
typeof undefined;      // "undefined"
typeof 10n;            // "bigint"
typeof Symbol();       // "symbol"
typeof function () {}; // "function"
typeof null;           // "object"  ⚠️ bug historique
typeof [];             // "object"  → utilisez Array.isArray([])
typeof {};             // "object"
```

## 3.3 Conversions et coercition

```javascript
Number("42");        // 42
Number("abc");       // NaN
parseInt("42px");    // 42
parseFloat("3.14");  // 3.14
String(123);         // "123"
Boolean(0);          // false

"5" + 3;             // "53"  (concaténation)
"5" - 3;             // 2     (conversion numérique)
```

**Valeurs « falsy »** (converties en `false`) : `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined`, `NaN`. **Tout le reste est « truthy »**, y compris `"0"`, `[]` et `{}`.

## 3.4 Égalité

| Opérateur | Comportement |
| --- | --- |
| `===` / `!==` | Égalité **stricte**, sans conversion ✅ recommandé |
| `==` / `!=` | Égalité **souple**, avec conversions surprenantes |
| `Object.is(a, b)` | Comme `===`, mais `Object.is(NaN, NaN)` est `true` |

```javascript
0 == "0";       // true  😬
0 === "0";      // false ✅
null == undefined;   // true
NaN === NaN;         // false → utilisez Number.isNaN(x)
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
2 ** 10;                 // 1024
7 % 3;                   // 1
let i = 5; i++;          // 6
```

## 4.2 Fusion nulle `??`

Renvoie la valeur de droite **seulement si** la gauche est `null` ou `undefined` (contrairement à `||` qui réagit à toutes les valeurs falsy).

```javascript
const quantite = 0;
quantite || 10;     // 10  😬 (0 est falsy)
quantite ?? 10;     // 0   ✅
```

## 4.3 Chaînage optionnel `?.`

```javascript
const ville = utilisateur?.adresse?.ville;         // undefined si un maillon est absent
const nb = liste?.[0];
const res = objet.methode?.();                     // appelle seulement si la méthode existe
```

## 4.4 Affectations logiques

```javascript
a ||= "défaut";   // a = a || "défaut"
a &&= a.trim();   // a = a && a.trim()
a ??= 0;          // a = a ?? 0
```

## 4.5 Ternaire, `in`, `instanceof`

```javascript
const statut = age >= 18 ? "majeur" : "mineur";
"nom" in utilisateur;              // propriété présente ?
tableau instanceof Array;          // true
```

## 4.6 Priorité

En cas de doute, **utilisez des parenthèses**. Ordre approximatif (haut → bas) : `()` → `**` → `* / %` → `+ -` → comparaisons → `&&` → `||` / `??` → ternaire → affectation.

> ⚠️ On ne peut pas mélanger `??` avec `&&` / `||` sans parenthèses.

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

const nom = "Alice";
console.log(`Bonjour ${nom}, 2 + 3 = ${2 + 3}`);   // interpolation

const multi = `Ligne 1
Ligne 2`;                          // chaîne multiligne
```

### Caractères d'échappement

| Séquence | Signification |
| --- | --- |
| `\n` | Saut de ligne |
| `\t` | Tabulation |
| `\\` | Antislash |
| `\'` `\"` | Guillemets |
| `\u00E9` / `\u{1F600}` | Caractère Unicode (`é` / 😀) |

### Gabarits étiquetés *(ajout)*

```javascript
function surligner(chaines, ...valeurs) {
    return chaines.reduce((r, c, i) => r + c + (valeurs[i] !== undefined ? `<b>${valeurs[i]}</b>` : ""), "");
}
surligner`Bonjour ${"Alice"}, vous avez ${3} messages`;
```

## 5.2 Propriétés et accès

Les chaînes sont **immuables**.

```javascript
const s = "JavaScript";
s.length;        // 10
s[0];            // "J"
s.at(-1);        // "t"  (accès depuis la fin, ES2022)
s[0] = "j";      // ❌ sans effet (erreur en mode strict)
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
"  Bonjour  ".trim();              // "Bonjour"
["a", "b", "c"].join("-");         // "a-b-c"
[..."héllo"].length;               // 5 (itère par caractères Unicode)
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

typeof NaN;                     // "number"
1 / 0;                          // Infinity
```

### Précision des flottants

```javascript
0.1 + 0.2;                                  // 0.30000000000000004
Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON; // ✅ comparaison tolérante
(0.1 + 0.2).toFixed(2);                     // "0.30" (⚠️ renvoie une CHAÎNE)
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
enorme * 2n;                // 18014398509481986n
// 1n + 1;                  // ❌ TypeError : on ne mélange pas BigInt et number
BigInt(10) + 5n;
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
Math.floor(Math.random() * 10) + 1;   // entier aléatoire de 1 à 10
Math.max(...[3, 9, 4]);               // 9
```

> 🔒 `Math.random()` **n'est pas cryptographiquement sûr** : pour des jetons ou mots de passe, utilisez `crypto.getRandomValues()` ou `crypto.randomUUID()`.

## 6.5 Formater les nombres avec `Intl` *(à jour)*

```javascript
new Intl.NumberFormat("fr-FR", { style: "currency", currency: "EUR" }).format(1234.5);
// "1 234,50 €"
new Intl.NumberFormat("fr-FR", { style: "percent" }).format(0.256);   // "26 %"
(1234567.891).toLocaleString("fr-FR");                                // "1 234 567,891"
```

---

# 7. Conditions et boucles

## 7.1 Conditions

```javascript
if (note >= 16) {
    console.log("Très bien");
} else if (note >= 10) {
    console.log("Passable");
} else {
    console.log("Insuffisant");
}
```

### `switch`

Compare avec `===`. N'oubliez pas `break` (sinon, exécution en cascade).

```javascript
switch (jour) {
    case "samedi":
    case "dimanche":
        console.log("Week-end");
        break;
    default:
        console.log("Semaine");
}
```

### Ternaire et opérateurs logiques

```javascript
const acces = age >= 18 ? "autorisé" : "refusé";
utilisateur && afficher(utilisateur);       // court-circuit
const nom = saisie ?? "Anonyme";
```

> Pour de nombreux `case`, une **table de correspondance** (objet ou `Map`) est souvent plus lisible :
> ```javascript
> const actions = { ajouter: ajouter, supprimer: supprimer };
> actions[commande]?.();
> ```

## 7.2 Boucles

| Boucle | Usage |
| --- | --- |
| `for` | Nombre d'itérations connu |
| `while` | Tant qu'une condition est vraie |
| `do...while` | Au moins une exécution |
| `for...of` | **Valeurs** d'un itérable (tableau, chaîne, `Map`, `Set`…) ✅ |
| `for...in` | **Clés** énumérables d'un objet (à éviter sur les tableaux) |

```javascript
for (let i = 0; i < 3; i++) console.log(i);

let n = 0;
while (n < 3) { n++; }

do { n--; } while (n > 0);

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
}

externe: for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        if (j === 1) continue externe;
    }
}
```

> ⚠️ `forEach` **n'attend pas** les `await` de son callback : utilisez `for...of` pour des boucles asynchrones séquentielles.

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
const zeros = new Array(3).fill(0);      // [0, 0, 0]
const suite = Array.from({ length: 5 }, (_, i) => i);   // [0, 1, 2, 3, 4]
const lettres = Array.from("abc");       // ["a", "b", "c"]

fruits[0];             // "pomme"
fruits.at(-1);         // "cerise" (ES2022)
fruits.length;         // 3
Array.isArray(fruits); // true
```

## 8.2 Ajouter, retirer, modifier

| Méthode | Effet | Mute ? |
| --- | --- | --- |
| `push(x)` / `pop()` | Ajoute / retire à la **fin** | ✅ |
| `unshift(x)` / `shift()` | Ajoute / retire au **début** | ✅ |
| `splice(i, n, ...ajouts)` | Supprime / insère à une position | ✅ |
| `sort()` / `reverse()` | Trie / inverse | ✅ |
| `fill()` / `copyWithin()` | Remplit / copie interne | ✅ |
| `slice(début, fin)` | Sous-tableau | ❌ copie |
| `concat()` / `[...a, ...b]` | Assemble | ❌ copie |

### Versions **non mutantes** *(ES2023, à jour)*

```javascript
const nombres = [3, 1, 2];
nombres.toSorted();             // [1, 2, 3]   (nombres inchangé)
nombres.toReversed();           // [2, 1, 3]
nombres.toSpliced(1, 1);        // [3, 2]
nombres.with(0, 99);            // [99, 1, 2]
```

> ⚠️ `sort()` sans argument trie en **ordre alphabétique** : `[10, 2, 1].sort()` → `[1, 10, 2]`. Utilisez `sort((a, b) => a - b)`.

## 8.3 Parcourir

```javascript
for (const f of fruits) console.log(f);
fruits.forEach((f, i) => console.log(i, f));
for (const [i, f] of fruits.entries()) console.log(i, f);
```

## 8.4 Méthodes d'ordre supérieur

```javascript
const nums = [1, 2, 3, 4, 5];

nums.map(x => x * 2);                 // [2, 4, 6, 8, 10]
nums.filter(x => x % 2 === 0);        // [2, 4]
nums.reduce((somme, x) => somme + x, 0);   // 15
nums.find(x => x > 2);                // 3
nums.findIndex(x => x > 2);           // 2
nums.findLast(x => x < 5);            // 4 (ES2023)
nums.some(x => x > 4);                // true
nums.every(x => x > 0);               // true
nums.flatMap(x => [x, x * 10]);       // aplatit d'un niveau
[[1, [2]], [3]].flat(Infinity);       // [1, 2, 3]
```

### Rechercher

```javascript
fruits.includes("pomme");    // true
fruits.indexOf("banane");    // 1
```

### Regrouper *(ES2024)*

```javascript
const personnes = [{ nom: "A", age: 20 }, { nom: "B", age: 30 }, { nom: "C", age: 20 }];
Object.groupBy(personnes, p => p.age);
// { 20: [{...A}, {...C}], 30: [{...B}] }
Map.groupBy(personnes, p => p.age);     // même chose, sous forme de Map
```

### Autres

```javascript
Array.fromAsync(iterableAsynchrone);    // ES2026 : version asynchrone d'Array.from
["a", "b"].join(", ");                  // "a, b"
```

## 8.5 Spread, rest et décomposition

```javascript
const a = [1, 2];
const b = [...a, 3, 4];                // copie + ajout
Math.max(...b);
const [premier, ...autres] = b;
```

## 8.6 Tableaux d'objets

```javascript
const users = [{ id: 1, nom: "Alice" }, { id: 2, nom: "Bob" }];
users.map(u => u.nom);                        // ["Alice", "Bob"]
users.find(u => u.id === 2);                  // { id: 2, nom: "Bob" }
users.toSorted((x, y) => x.nom.localeCompare(y.nom));
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

personne.nom;                // notation pointée
personne["code postal"];     // notation crochets (clés dynamiques)
personne.ville = "Paris";    // ajout
delete personne.age;         // suppression
"nom" in personne;           // true
Object.hasOwn(personne, "nom");   // true (à jour : remplace hasOwnProperty)
```

### Propriétés calculées et raccourcis

```javascript
const cle = "couleur";
const nom = "Alice", age = 30;
const o = { [cle]: "rouge", nom, age };       // { couleur: "rouge", nom: "Alice", age: 30 }
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
Object.entries({ a: 1, b: 2 });                     // [["a", 1], ["b", 2]]
Object.fromEntries(Object.entries(prix).map(([k, v]) => [k, v * 1.2]));   // transformer les valeurs
const fusion = { ...defauts, ...options };          // fusion (la dernière valeur gagne)
```

### Décomposition d'objet

```javascript
const { nom, ...reste } = personne;
function afficher({ nom, age = 18 }) { /* … */ }
```

### Itération

```javascript
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
scores.get("Alice");          // 15
scores.has("Bob");            // true
scores.delete("Bob");
scores.size;                  // 1

for (const [nom, note] of scores) console.log(nom, note);
[...scores.keys()];  [...scores.values()];  [...scores.entries()];

const depuisObjet = new Map(Object.entries({ a: 1 }));
const versObjet = Object.fromEntries(scores);

// ES2026 : getOrInsert (évite le motif « si absent, créer »)
const groupes = new Map();
groupes.getOrInsert("fruits", []).push("pomme");
groupes.getOrInsertComputed("legumes", () => []).push("carotte");
```

### `Map` ou objet ?

| Critère | Objet | `Map` |
| --- | --- | --- |
| Types de clés | Chaîne / symbole | **Tous** (objets, fonctions…) |
| Ordre | Complexe (entiers d'abord) | **Ordre d'insertion** |
| Taille | `Object.keys(o).length` | `map.size` |
| Itération | Via `Object.entries` | Directe |
| Performances (ajouts/retraits fréquents) | Moyennes | **Meilleures** |
| Sérialisation JSON | ✅ native | ❌ à convertir |
| Usage conseillé | Données structurées à clés fixes | Dictionnaire dynamique |

## 9.3 `Set` : des valeurs uniques

```javascript
const unique = new Set([1, 2, 2, 3]);    // Set {1, 2, 3}
unique.add(4);
unique.has(2);                           // true
unique.delete(1);
unique.size;

const sansDoublons = [...new Set(tableau)];
```

### Opérations ensemblistes *(ES2025, à jour)*

```javascript
const a = new Set([1, 2, 3]);
const b = new Set([3, 4]);
a.union(b);                  // Set {1, 2, 3, 4}
a.intersection(b);           // Set {3}
a.difference(b);             // Set {1, 2}
a.symmetricDifference(b);    // Set {1, 2, 4}
a.isSubsetOf(b);             // false
a.isSupersetOf(b);  a.isDisjointFrom(b);
```

## 9.4 `WeakMap` et `WeakSet` *(ajout)*

Leurs clés sont des **objets tenus faiblement** : si l'objet n'est plus référencé ailleurs, il peut être collecté par le ramasse-miettes. Utiles pour associer des données privées ou un cache à des objets sans fuite de mémoire. Non itérables.

```javascript
const meta = new WeakMap();
meta.set(element, { clics: 0 });
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
globalThis.setTimeout === setTimeout;     // true
globalThis.maVariable = 42;               // ⚠️ pollue l'espace global
console.log(globalThis.console === console);
```

## 10.2 Cas d'usage

```javascript
// Détection de fonctionnalités, code isomorphe
if (typeof globalThis.fetch === "function") { /* … */ }

// Polyfill
if (!globalThis.structuredClone) {
    globalThis.structuredClone = (v) => JSON.parse(JSON.stringify(v));
}
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
const sûr = new RegExp(RegExp.escape(saisieUtilisateur));   // RegExp.escape (ES2025)
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
m.groups.annee;        // "2026"

"Alice Dupont".replace(/(\w+) (\w+)/, "$2 $1");        // "Dupont Alice"
"2026-10-11".replace(/(?<a>\d+)-(?<m>\d+)-(?<j>\d+)/, "$<j>/$<m>/$<a>");   // "11/10/2026"

for (const r of "a1b22".matchAll(/\d+/g)) console.log(r[0], r.index);
```

## 11.6 Exemples utiles

```javascript
const email = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;          // validation simple (non exhaustive)
const telFr = /^(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}$/;
const espaces = /\s+/g;
"a   b".replace(espaces, " ");                        // "a b"
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
```

### Fonctions fléchées vs classiques

| | Fléchée `=>` | Classique `function` |
| --- | --- | --- |
| `this` | **Hérité** du contexte englobant (lexical) | Dépend de l'appel |
| `arguments` | ❌ | ✅ |
| Constructeur (`new`) | ❌ | ✅ |
| Usage idéal | Callbacks, petites fonctions | Méthodes, constructeurs |

## 12.2 Paramètres et arguments

```javascript
function saluer(nom = "inconnu", ...titres) {    // valeur par défaut + paramètre rest
    return `Bonjour ${titres.join(" ")} ${nom}`;
}
saluer();                           // "Bonjour  inconnu"
saluer("Alice", "Dr", "Pr");

const nombres = [1, 2, 3];
Math.max(...nombres);               // spread à l'appel

function config({ port = 3000, hote = "localhost" } = {}) { /* paramètres nommés */ }
```

## 12.3 Valeur de retour

Une fonction sans `return` renvoie `undefined`. Pour retourner plusieurs valeurs, retournez un tableau ou un objet.

```javascript
const minMax = (t) => ({ min: Math.min(...t), max: Math.max(...t) });
const { min, max } = minMax([3, 1, 4]);
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
c.incrementer(); c.incrementer();
c.valeur();                          // 2
```

Usages : données privées, fonctions « fabriques », mémoïsation, *callbacks*.

```javascript
// Piège classique avec var
for (var i = 0; i < 3; i++) setTimeout(() => console.log(i));   // 3 3 3
for (let j = 0; j < 3; j++) setTimeout(() => console.log(j));   // 0 1 2 ✅
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

presenter.call(alice, "Salut", "!");      // appel immédiat, arguments séparés
presenter.apply(alice, ["Salut", "!"]);   // appel immédiat, arguments en tableau
const lie = presenter.bind(alice, "Salut");   // renvoie une NOUVELLE fonction liée
lie("?");                                 // "Salut, Alice?"
```

> ⚠️ Une méthode passée en *callback* perd son `this` : `setTimeout(obj.methode, 0)` → utilisez `obj.methode.bind(obj)` ou une fonction fléchée.

## 12.7 Fonctions d'ordre supérieur et composition

```javascript
const appliquerDeuxFois = (f, x) => f(f(x));
const ajouter = n => x => x + n;          // curryfication
ajouter(2)(3);                            // 5

const composer = (...fns) => x => fns.reduceRight((acc, f) => f(acc), x);
```

## 12.8 Fonctions immédiatement invoquées (IIFE)

```javascript
(function () {
    const prive = "isolé";
})();
```

Moins utiles depuis que les **modules** et le **bloc `{}`** (avec `let`/`const`) offrent leur propre portée.

## 12.9 Récursivité

```javascript
const factorielle = n => (n <= 1 ? 1 : n * factorielle(n - 1));
```

La pile d'appels est limitée (`RangeError: Maximum call stack size exceeded`) : préférez une boucle pour de grandes profondeurs.

## 12.10 Mémoïsation *(ajout)*

```javascript
function memoiser(fn) {
    const cache = new Map();
    return (arg) => cache.has(arg) ? cache.get(arg) : (cache.set(arg, fn(arg)), cache.get(arg));
}
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
```

---

# 13. Itérateurs et générateurs

*(Section ajoutée.)*

## 13.1 Le protocole d'itération

Un **itérable** possède une méthode `[Symbol.iterator]()` qui renvoie un **itérateur** (objet avec `next()` → `{ value, done }`). Tableaux, chaînes, `Map`, `Set` et `NodeList` sont itérables ; on les parcourt avec `for...of`, `...` et la décomposition.

```javascript
const it = [10, 20][Symbol.iterator]();
it.next();   // { value: 10, done: false }
it.next();   // { value: 20, done: false }
it.next();   // { value: undefined, done: true }
```

## 13.2 Générateurs

Une fonction `function*` utilise `yield` pour produire des valeurs **à la demande** et suspend son exécution entre deux.

```javascript
function* compteARebours(n) {
    while (n > 0) yield n--;
}
console.log([...compteARebours(3)]);   // [3, 2, 1]

function* naturels() { let i = 0; while (true) yield i++; }   // séquence infinie
```

Rendre un objet itérable :

```javascript
class Playlist {
    #titres = ["A", "B"];
    *[Symbol.iterator]() { yield* this.#titres; }
}
```

## 13.3 Assistants d'itérateurs *(ES2025, à jour)*

Chaînage **paresseux** sur n'importe quel itérateur :

```javascript
naturels()
    .filter(n => n % 2 === 0)
    .map(n => n * n)
    .take(5)
    .toArray();            // [0, 4, 16, 36, 64]

Iterator.concat(a, b);     // ES2026 : concaténer des itérables
```

Autres : `drop`, `flatMap`, `reduce`, `some`, `every`, `find`, `forEach`.

## 13.4 Générateurs asynchrones

```javascript
async function* pages(url) {
    for (let p = 1; p <= 3; p++) yield await (await fetch(`${url}?page=${p}`)).json();
}
for await (const page of pages("/api/items")) console.log(page);
```

---

# 14. `eval` et ses alternatives

## 14.1 Qu'est-ce que `eval` ?

`eval(chaine)` **exécute du code JavaScript contenu dans une chaîne**.

```javascript
const resultat = eval("2 + 3 * 4");     // 14
```

## 14.2 Pourquoi l'éviter ?

| Risque | Détail |
| --- | --- |
| 🔒 **Sécurité** | Injection de code (XSS) si la chaîne contient des données non fiables |
| 🐌 **Performances** | Empêche de nombreuses optimisations du moteur |
| 🧩 **Portée** | Accède à la portée locale et peut créer/modifier des variables |
| 🛡️ **CSP** | Bloqué par une *Content Security Policy* stricte (`unsafe-eval`) |
| 🐞 **Débogage** | Code difficile à lire, tester et analyser |

> **Règle** : n'utilisez **jamais** `eval` avec des données provenant d'un utilisateur ou du réseau.

## 14.3 Alternatives sûres

```javascript
JSON.parse('{"a": 1}');                        // lire des données (au lieu de eval)
const operations = { "+": (a, b) => a + b, "-": (a, b) => a - b };
operations[op](x, y);                          // table de fonctions plutôt que code dynamique
obj[nomDePropriete];                           // accès dynamique sans eval
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
try {
    const donnees = JSON.parse(texte);
} catch (erreur) {
    console.error(erreur.name, erreur.message);
} finally {
    console.log("Toujours exécuté");
}

try { /* … */ } catch { /* liaison facultative si l'erreur ne sert pas */ }
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
    try { JSON.parse("{"); }
    catch (e) { throw new Error("Configuration illisible", { cause: e }); }   // cause (ES2022)
} catch (e) {
    console.log(e.cause);
}
```

Propriétés utiles : `name`, `message`, `stack`, `cause`.
`Error.isError(valeur)` *(ES2026)* teste de façon fiable si une valeur est une erreur, même venant d'un autre contexte (iframe).

## 15.4 Erreurs asynchrones

```javascript
// Avec async/await
try {
    const r = await fetch(url);
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
} catch (e) { /* … */ }

// Avec les promesses
fetch(url).then(/* … */).catch(e => console.error(e));

// Filets de sécurité globaux
window.addEventListener("error", e => /* journaliser */ {});
window.addEventListener("unhandledrejection", e => /* journaliser */ {});
```

## 15.5 Mode strict (`"use strict"`)

Le **mode strict** rend le langage plus sûr : il transforme des erreurs silencieuses en exceptions.

```javascript
"use strict";                  // en début de fichier ou de fonction

x = 10;                        // ❌ ReferenceError (variable non déclarée)
delete Object.prototype;       // ❌ TypeError
function f(a, a) {}            // ❌ SyntaxError (paramètres dupliqués)
const o = Object.freeze({ a: 1 });
o.a = 2;                       // ❌ TypeError (écriture silencieuse sinon)
```

| Changement en mode strict | Effet |
| --- | --- |
| Variables non déclarées | Erreur |
| `this` d'une fonction simple | `undefined` (au lieu de `globalThis`) |
| Écritures interdites (`freeze`, propriétés en lecture seule) | Erreur |
| Mots réservés futurs (`let`, `static`, `implements`…) | Interdits comme identifiants |
| Octal `010`, `with` | Interdits |
| `arguments` | Non lié aux paramètres |

> ✅ **Les modules ES et les classes sont automatiquement en mode strict** : le `"use strict"` explicite n'est plus nécessaire dans du code moderne.

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
// 1, 2, 3, 4
```

## 16.2 Minuteries

```javascript
const id = setTimeout(() => console.log("Après 2 s"), 2000);
clearTimeout(id);

const iv = setInterval(() => console.log("Toutes les secondes"), 1000);
clearInterval(iv);

setTimeout((a, b) => console.log(a + b), 100, 1, 2);     // arguments supplémentaires
```

### `setTimeout` récursif vs `setInterval`

`setInterval` ne tient pas compte de la durée du traitement : les appels peuvent s'empiler. Un `setTimeout` **récursif** garantit un délai entre la **fin** d'un traitement et le début du suivant :

```javascript
function boucle() {
    faireQuelqueChose().finally(() => setTimeout(boucle, 1000));
}
boucle();
```

> ⚠️ Le délai est un **minimum** (non garanti). Les onglets en arrière-plan ralentissent les minuteries. Pour l'animation, utilisez **`requestAnimationFrame`**.

## 16.3 *Callbacks* (rappels)

```javascript
function lireDonnees(callback) {
    setTimeout(() => callback(null, { id: 1 }), 500);
}
lireDonnees((err, data) => { if (err) return; console.log(data); });
```

Imbriqués, ils mènent à l'**enfer des callbacks** (*callback hell*) : on leur préfère les promesses.

## 16.4 Promesses (`Promise`)

Une **promesse** représente le résultat futur d'une opération : **en attente** (*pending*) → **tenue** (*fulfilled*) ou **rejetée** (*rejected*).

```javascript
const attendre = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

const promesse = new Promise((resolve, reject) => {
    const ok = true;
    ok ? resolve("Succès") : reject(new Error("Échec"));
});

promesse
    .then(valeur => valeur.toUpperCase())     // chaînage : retourne une nouvelle promesse
    .then(console.log)
    .catch(console.error)                     // intercepte toute erreur de la chaîne
    .finally(() => console.log("Terminé"));
```

## 16.5 `async` / `await`

Syntaxe plus lisible, basée sur les promesses. Une fonction `async` **retourne toujours une promesse**.

```javascript
async function chargerUtilisateur(id) {
    try {
        const reponse = await fetch(`/api/users/${id}`);
        if (!reponse.ok) throw new Error(`HTTP ${reponse.status}`);
        return await reponse.json();
    } catch (e) {
        console.error(e);
        throw e;
    }
}

// await au niveau supérieur d'un module (ES2022)
const config = await (await fetch("/config.json")).json();
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
// Séquentiel (lent) vs parallèle (rapide)
const a = await chargerA();
const b = await chargerB();                         // attend A d'abord ❌

const [x, y] = await Promise.all([chargerA(), chargerB()]);   // en parallèle ✅

const resultats = await Promise.allSettled(urls.map(u => fetch(u)));
resultats.filter(r => r.status === "fulfilled");
```

## 16.7 Annulation et délais : `AbortController` *(ajout)*

```javascript
const controleur = new AbortController();
setTimeout(() => controleur.abort(), 5000);

try {
    const r = await fetch(url, { signal: controleur.signal });
} catch (e) {
    if (e.name === "AbortError") console.log("Requête annulée");
}

// Raccourcis
fetch(url, { signal: AbortSignal.timeout(5000) });
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
const reponse = await fetch("https://api.exemple.com/users");
if (!reponse.ok) throw new Error(`Erreur HTTP ${reponse.status}`);   // ⚠️ fetch ne rejette PAS sur un 404/500
const users = await reponse.json();
```

> ⚠️ `fetch` ne rejette que sur une **erreur réseau** : vérifiez toujours `response.ok`.

Lecture du corps : `.json()`, `.text()`, `.blob()`, `.arrayBuffer()`, `.formData()` (une seule lecture possible ; `.clone()` sinon).

### Requêtes `POST`, `PUT`, `DELETE`

```javascript
const r = await fetch("/api/users", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${jeton}`,
    },
    body: JSON.stringify({ nom: "Alice", age: 30 }),
    signal: AbortSignal.timeout(8000),
});

await fetch(`/api/users/${id}`, { method: "DELETE" });
```

### Paramètres d'URL

```javascript
const url = new URL("https://api.exemple.com/search");
url.searchParams.set("q", "café & thé");     // encodage automatique
fetch(url);
URL.canParse("https://exemple.com");         // true : validation
```

### Fonction utilitaire réutilisable

```javascript
async function requeteJSON(url, options = {}) {
    const r = await fetch(url, { headers: { Accept: "application/json" }, ...options });
    if (!r.ok) throw new Error(`HTTP ${r.status} – ${await r.text()}`);
    return r.status === 204 ? null : r.json();
}
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
const texte = JSON.stringify({ a: 1, b: [1, 2] });            // '{"a":1,"b":[1,2]}'
JSON.stringify(objet, null, 2);                               // formaté (indentation 2)
JSON.stringify(objet, ["nom", "age"]);                        // ne garde que ces clés
JSON.stringify(objet, (cle, val) => (cle === "mdp" ? undefined : val));

const objet = JSON.parse('{"a":1}');
JSON.parse(texte, (cle, val) => (cle === "date" ? new Date(val) : val));   // reviver
```

Comportements à connaître :

- `Date` → chaîne ISO (via `toJSON()`) ; `Map`, `Set` → `{}` ; `undefined`, fonctions et symboles sont ignorés ; `NaN`/`Infinity` → `null`.
- **`JSON.parse` avec accès au texte source** *(ES2026)* : le *reviver* reçoit un 3ᵉ paramètre `contexte.source`, ce qui permet de lire les grands entiers sans perte de précision. `JSON.rawJSON()` permet d'écrire de tels nombres.

### Gérer les erreurs

```javascript
try {
    const data = JSON.parse(entree);
} catch (e) {
    console.error("JSON invalide :", e.message);     // SyntaxError
}
```

### Importer un fichier JSON *(ES2025)*

```javascript
import config from "./config.json" with { type: "json" };
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
const litteral = { nom: "Alice" };                    // littéral ✅ le plus courant
const vide = Object.create(null);                     // sans prototype
const instance = new Personne("Alice", 30);           // constructeur
```

## 18.2 Fonctions constructeurs

Une **fonction constructeur** (nom en `PascalCase`) crée des objets similaires avec `new`.

```javascript
function Personne(nom, age) {
    this.nom = nom;
    this.age = age;
}

const alice = new Personne("Alice", 30);
```

### Ce que fait `new`

1. Crée un **nouvel objet vide**.
2. Lie son **prototype** à `Personne.prototype`.
3. Exécute le constructeur avec `this` = ce nouvel objet.
4. Retourne l'objet (sauf si le constructeur renvoie lui-même un objet).

> ⚠️ Oublier `new` fait pointer `this` vers `undefined` (mode strict) ou `globalThis`. Protégez-vous avec `if (!new.target) throw …` ou utilisez une **classe** (qui refuse l'appel sans `new`).

## 18.3 Prototypes et chaîne de prototypes

Chaque objet possède un **prototype** (accessible par `Object.getPrototypeOf(obj)`), qui lui-même a un prototype, etc. jusqu'à `null` : c'est la **chaîne de prototypes**. Quand une propriété est introuvable sur l'objet, JavaScript la cherche dans sa chaîne.

```javascript
// Les méthodes partagées se placent sur le prototype (une seule copie en mémoire)
Personne.prototype.saluer = function () {
    return `Bonjour, je suis ${this.nom}`;
};

alice.saluer();                                         // trouvé via le prototype
Object.getPrototypeOf(alice) === Personne.prototype;    // true
alice.hasOwnProperty("saluer");                         // false
Object.hasOwn(alice, "nom");                            // true
```

> ⚠️ N'utilisez pas `__proto__` dans du nouveau code : préférez `Object.getPrototypeOf` / `Object.setPrototypeOf`.

### Héritage avec les prototypes

```javascript
function Etudiant(nom, age, filiere) {
    Personne.call(this, nom, age);          // appel du « super constructeur »
    this.filiere = filiere;
}
Etudiant.prototype = Object.create(Personne.prototype);
Etudiant.prototype.constructor = Etudiant;  // rétablir la référence

new Etudiant("Bob", 20, "Maths").saluer();
```

Aujourd'hui, on utilise de préférence la syntaxe **`class ... extends`** (voir [section 19](#19-classes-et-programmation-orientée-objet)), qui est du sucre syntaxique sur ce mécanisme.

## 18.4 `Object.create`

Crée un objet avec un **prototype choisi**, sans constructeur.

```javascript
const animal = {
    parler() { return `${this.nom} fait un bruit`; },
};
const chien = Object.create(animal, { nom: { value: "Rex", enumerable: true } });
chien.parler();
```

| | Constructeur / classe | `Object.create` |
| --- | --- | --- |
| Initialisation | Via le constructeur | Manuelle |
| Héritage | `extends` / `prototype` | Prototype choisi directement |
| Usage | Types d'objets avec état | Délégation simple, objets sans prototype |

## 18.5 Constructeurs intégrés

`Object`, `Array`, `Function`, `String`, `Number`, `Boolean`, `Date`, `RegExp`, `Map`, `Set`, `Promise`, `Error`, `Proxy`…

```javascript
new Date();  new Map();  new Set();  new Error("msg");
```

> ⚠️ Évitez `new String("a")`, `new Number(1)`, `new Boolean(false)` : ils créent des **objets enveloppes** (*wrappers*) et non des primitives (`new Boolean(false)` est *truthy* !). Utilisez `String(x)`, `Number(x)`, `Boolean(x)` sans `new`.

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
```

✅ Pas de `new` ni de `this`, confidentialité par fermeture · ❌ Une copie des méthodes par objet.

### Encapsulation par fermeture

```javascript
function creerCompte(solde = 0) {
    return {
        deposer(m) { solde += m; },
        get solde() { return solde; },      // solde n'est pas modifiable de l'extérieur
    };
}
```

### Factory vs constructeur

| | Fabrique | Constructeur / classe |
| --- | --- | --- |
| `new` requis | ❌ | ✅ |
| `instanceof` | ❌ | ✅ |
| Données privées | Fermetures | Champs `#privés` |
| Mémoire des méthodes | Copie par objet | Partagées via le prototype |

## 18.7 Membres statiques

Appartiennent au **constructeur** lui-même, pas aux instances.

```javascript
Personne.especes = "Homo sapiens";
Personne.comparerAge = (a, b) => a.age - b.age;
```

(Avec les classes : mot-clé `static`, voir plus bas.)

## 18.8 Mixins et composition

La **composition** assemble des comportements plutôt que d'empiler des héritages (« *composition over inheritance* »).

```javascript
const peutNager = { nager() { return `${this.nom} nage`; } };
const peutVoler = { voler() { return `${this.nom} vole`; } };

class Canard { constructor(nom) { this.nom = nom; } }
Object.assign(Canard.prototype, peutNager, peutVoler);

// Mixin sous forme de fonction (avec classes)
const Journalisable = (Base) => class extends Base {
    journal(msg) { console.log(`[${this.constructor.name}] ${msg}`); }
};
class Service extends Journalisable(Object) {}
```

## 18.9 Tester le type : `instanceof` et `constructor`

```javascript
alice instanceof Personne;            // true : Personne.prototype est dans la chaîne
alice.constructor === Personne;       // true (⚠️ fragile)
Personne.prototype.isPrototypeOf(alice);
Array.isArray(x);                     // plus fiable que instanceof Array (iframes)
Object.prototype.toString.call(x);    // "[object Date]"…
```

Limites : `instanceof` échoue entre **contextes différents** (iframes), et `constructor` est écrasé si on remplace le prototype sans le rétablir.

Personnaliser `instanceof` :

```javascript
class Pair { static [Symbol.hasInstance](n) { return n % 2 === 0; } }
2 instanceof Pair;   // true
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
```

Utilisé par les frameworks de réactivité (Vue 3) et pour la validation.

## 18.11 Déboguer les constructeurs et prototypes

```javascript
console.dir(alice);                       // inspection détaillée (avec [[Prototype]])
Object.getPrototypeOf(alice);
Object.getOwnPropertyNames(Personne.prototype);
alice.constructor.name;
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

    // Méthode statique
    static creerAnonyme() { return new Personne("Anonyme", 0); }

    // Bloc d'initialisation statique (ES2022)
    static { Personne.registre = new Map(); }

    toString() { return `${this.nom} (${this.#age} ans)`; }
}

const alice = new Personne("Alice", 30);
alice.saluer();
alice.age = 31;
// alice.#age;                 // ❌ SyntaxError : champ privé
Personne.creerAnonyme();
```

> ✅ Les classes sont **toujours en mode strict**, **ne sont pas hoistées** de la même manière que les fonctions (TDZ) et **ne peuvent pas être appelées sans `new`**.

### Expression de classe

```javascript
const Animal = class { /* … */ };
```

## 19.2 Héritage : `extends` et `super`

```javascript
class Etudiant extends Personne {
    constructor(nom, age, filiere) {
        super(nom, age);            // ⚠️ obligatoire avant d'utiliser this
        this.filiere = filiere;
    }

    saluer() {                       // redéfinition (override)
        return `${super.saluer()} et j'étudie ${this.filiere}`;
    }
}

const bob = new Etudiant("Bob", 20, "Maths");
bob instanceof Personne;      // true
```

On peut étendre des classes natives (`Array`, `Error`, `Map`…).

## 19.3 Membres statiques et héritage

```javascript
class Maths {
    static PI = 3.14159;
    static carre(x) { return x * x; }
    static #privee() { return "statique privée"; }    // ES2022
}
Maths.carre(4);
```

Les membres statiques sont **hérités** par les sous-classes (`class B extends Maths`). Usages : utilitaires, fabriques, compteurs, constantes.

## 19.4 Encapsulation

| Mécanisme | Description |
| --- | --- |
| **Champs / méthodes `#privés`** ✅ | Vraiment inaccessibles de l'extérieur (garanti par le langage) |
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
```

## 19.6 Polymorphisme et *duck typing*

```javascript
const formes = [new Cercle(1), new Rectangle(2, 3)];
formes.map(f => f.aire());       // chaque objet répond à sa manière
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
{
    using fichier = ouvrirFichier("a.txt");     // fichier[Symbol.dispose]() appelé à la sortie du bloc
    // …
}
// await using pour les ressources asynchrones
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
export class Calculatrice { /* … */ }

// Export par défaut (un seul par module)
export default function soustraire(a, b) { return a - b; }

// Regroupés / renommés
export { additionner as somme, PI };
export * from "./autres.js";                  // réexporter
```

## 20.4 `import`

```javascript
import soustraire from "./maths.js";                  // défaut
import { PI, additionner } from "./maths.js";         // nommés
import { additionner as plus } from "./maths.js";     // alias
import * as maths from "./maths.js";                  // tout, dans un espace de noms
import soustraire, { PI } from "./maths.js";
import "./effets-de-bord.js";                         // exécution seule
```

> Le **chemin relatif** doit commencer par `./` ou `../` et inclure l'**extension** `.js`.

### Import dynamique (chargement à la demande)

```javascript
const bouton = document.querySelector("#graphique");
bouton.addEventListener("click", async () => {
    const { dessiner } = await import("./graphique.js");     // code chargé seulement au clic
    dessiner();
});
```

### Import de JSON et attributs d'import

```javascript
import donnees from "./donnees.json" with { type: "json" };
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
| Standard | ✅ Oui | Spécifique à Node |

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
document.querySelector("#titre");              // premier correspondant (sélecteur CSS)
document.querySelectorAll(".carte");           // NodeList (itérable) de tous
document.getElementById("titre");
element.closest(".conteneur");                 // ancêtre le plus proche
element.matches(".actif");                     // correspond au sélecteur ?
element.children;  element.parentElement;  element.nextElementSibling;
```

> `getElementsByClassName` / `getElementsByTagName` renvoient des **collections vivantes** (`HTMLCollection`) qui se mettent à jour automatiquement ; `querySelectorAll` renvoie une liste **statique**.

## 21.3 Lire et modifier le contenu

```javascript
titre.textContent = "Nouveau titre";      // ✅ sûr : traite le texte comme du texte
conteneur.innerHTML = "<b>Gras</b>";      // ⚠️ interprète le HTML : risque de XSS avec des données non fiables
element.setAttribute("href", "/accueil");
element.getAttribute("href");
element.removeAttribute("disabled");
element.dataset.userId = "42";            // attribut data-user-id
input.value;  input.checked;              // champs de formulaire
```

> 🔒 **N'insérez jamais de saisie utilisateur avec `innerHTML`.** Utilisez `textContent`, ou créez des éléments avec `createElement`, ou assainissez le HTML (API *Sanitizer* / bibliothèque DOMPurify).

## 21.4 Créer, insérer et supprimer

```javascript
const li = document.createElement("li");
li.textContent = "Nouvel élément";
li.classList.add("item");

liste.append(li, "texte");                 // à la fin (accepte plusieurs nœuds / textes)
liste.prepend(li);                         // au début
reference.before(li);  reference.after(li);
reference.replaceWith(autre);
li.remove();                               // supprimer
liste.insertAdjacentHTML("beforeend", "<li>Rapide</li>");   // beforebegin | afterbegin | beforeend | afterend

const clone = modele.content.cloneNode(true);   // avec <template>
const fragment = document.createDocumentFragment();   // regrouper avant insertion (moins de reflows)
```

## 21.5 Classes et styles

```javascript
element.classList.add("actif");
element.classList.remove("cache");
element.classList.toggle("ouvert");
element.classList.contains("actif");
element.classList.replace("a", "b");

element.style.color = "red";                       // style en ligne
element.style.setProperty("--couleur", "tomato");  // variable CSS
getComputedStyle(element).width;                   // style calculé (lecture)
```

> ✅ Préférez **basculer des classes CSS** plutôt que manipuler `style` directement.

## 21.6 Dimensions et positionnement

```javascript
element.getBoundingClientRect();    // { x, y, width, height, top, left… } relatif à la fenêtre
element.offsetWidth;  element.clientHeight;
element.scrollHeight;  element.scrollTop;
element.scrollIntoView({ behavior: "smooth" });
window.scrollTo({ top: 0, behavior: "smooth" });
```

## 21.7 Les événements

```javascript
bouton.addEventListener("click", (evenement) => {
    console.log(evenement.target);          // élément réellement cliqué
    console.log(evenement.currentTarget);   // élément portant l'écouteur
    evenement.preventDefault();             // annule l'action par défaut (envoi de formulaire, lien…)
    evenement.stopPropagation();            // arrête la propagation
});

bouton.removeEventListener("click", gestionnaire);    // il faut la MÊME référence de fonction
```

### Options de `addEventListener`

```javascript
bouton.addEventListener("click", gestionnaire, {
    once: true,                       // se désinscrit après le premier appel
    passive: true,                    // promet de ne pas appeler preventDefault (scroll fluide)
    signal: controleur.signal,        // désinscription groupée via AbortController
});
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

> ✅ Préférez les **événements Pointer** (`pointerdown`…) qui unifient souris, tactile et stylet.

### Propagation : capture, cible, bulle

Un événement traverse l'arbre : **capture** (de `window` vers la cible) → **cible** → **bulle** (retour vers `window`). Par défaut, les écouteurs réagissent pendant la **bulle** ; `{ capture: true }` écoute pendant la capture.

### Délégation d'événements

Un seul écouteur sur le parent gère tous les enfants (même ajoutés plus tard) :

```javascript
liste.addEventListener("click", (e) => {
    const item = e.target.closest("li");
    if (!item || !liste.contains(item)) return;
    console.log("Clic sur", item.textContent);
});
```

### Événements personnalisés

```javascript
element.dispatchEvent(new CustomEvent("commande:ajoutee", { detail: { id: 7 }, bubbles: true }));
element.addEventListener("commande:ajoutee", e => console.log(e.detail.id));
```

### Formulaires

```javascript
formulaire.addEventListener("submit", (e) => {
    e.preventDefault();
    const donnees = new FormData(formulaire);
    const objet = Object.fromEntries(donnees);
    console.log(objet);
});
```

Utilisez aussi la **validation native** (`required`, `pattern`, `type="email"`, `form.checkValidity()`).

## 21.8 Quand le DOM est-il prêt ?

```javascript
document.addEventListener("DOMContentLoaded", () => { /* DOM construit */ });
// Plus simple : <script defer> ou <script type="module"> (déjà différés)
```

## 21.9 Observateurs modernes *(ajout)*

| API | Rôle |
| --- | --- |
| `IntersectionObserver` | Détecter l'entrée d'un élément à l'écran (chargement différé, défilement infini) |
| `ResizeObserver` | Réagir aux changements de taille d'un élément |
| `MutationObserver` | Réagir aux modifications du DOM |

```javascript
const obs = new IntersectionObserver((entrees) => {
    entrees.forEach(e => e.isIntersecting && e.target.classList.add("visible"));
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
// <carte-utilisateur nom="Alice"></carte-utilisateur>
```

## 21.11 Animations

- **CSS** (transitions, `@keyframes`) : à privilégier pour les animations simples.
- **`requestAnimationFrame`** : synchronisation avec le rafraîchissement de l'écran.
- **Web Animations API** :

```javascript
element.animate(
    [{ opacity: 0, transform: "translateY(20px)" }, { opacity: 1, transform: "none" }],
    { duration: 400, easing: "ease-out", fill: "forwards" },
);
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
window.innerWidth;  window.innerHeight;
window.open("https://exemple.com", "_blank", "noopener");
window.matchMedia("(prefers-color-scheme: dark)").matches;

navigator.language;                 // "fr-FR"
navigator.onLine;
await navigator.clipboard.writeText("copié !");
navigator.geolocation.getCurrentPosition(pos => console.log(pos.coords));   // avec autorisation

location.href;  location.hostname;  location.pathname;  location.search;  location.hash;
location.assign("/page");           // navigue (garde l'historique)
location.replace("/page");          // navigue (sans entrée d'historique)
location.reload();

history.back();  history.forward();  history.go(-2);
history.pushState({ page: 2 }, "", "/page-2");     // change l'URL sans recharger (SPA)
window.addEventListener("popstate", e => console.log(e.state));

screen.width;  screen.height;  screen.colorDepth;
```

### Boîtes de dialogue

`alert()`, `confirm()`, `prompt()` **bloquent** la page et sont peu esthétiques : préférez l'élément HTML **`<dialog>`** :

```javascript
document.querySelector("dialog").showModal();
```

## 22.2 Comparer les mécanismes de stockage

| | Cookie | `localStorage` | `sessionStorage` | IndexedDB |
| --- | --- | --- | --- | --- |
| Capacité | ~4 Ko | ~5 Mo | ~5 Mo | Très grande (centaines de Mo+) |
| Durée | Selon `Max-Age` | **Permanente** | **Onglet** (jusqu'à fermeture) | Permanente |
| Envoyé au serveur | ✅ À chaque requête | ❌ | ❌ | ❌ |
| API | Chaîne `document.cookie` | Synchrone, texte | Synchrone, texte | Asynchrone, objets |
| Accessible par | Serveur et client | Client | Client | Client |

## 22.3 Cookies

```javascript
// Écrire (chaque affectation ajoute/modifie UN cookie)
document.cookie = "theme=sombre; Max-Age=31536000; Path=/; SameSite=Lax; Secure";

// Lire (tous les cookies, en une chaîne)
document.cookie;       // "theme=sombre; langue=fr"
const cookies = Object.fromEntries(document.cookie.split("; ").map(c => c.split("=")));

// Supprimer : durée de vie expirée
document.cookie = "theme=; Max-Age=0; Path=/";
```

| Attribut | Rôle |
| --- | --- |
| `Max-Age` / `Expires` | Durée de vie |
| `Path` / `Domain` | Portée |
| `Secure` | Envoyé uniquement en HTTPS |
| `HttpOnly` | **Inaccessible à JavaScript** (défini par le serveur uniquement) |
| `SameSite` | `Strict` / `Lax` / `None` : protège contre le CSRF |

> 🔒 Les cookies de **session et d'authentification** doivent être posés par le **serveur** avec `HttpOnly; Secure; SameSite`. N'y stockez jamais de données sensibles lisibles par JavaScript.
> ℹ️ La **Cookie Store API** (`cookieStore.get()` / `.set()`) offre une alternative asynchrone moderne.

## 22.4 `localStorage`

Stockage **persistant**, propre à l'**origine** (protocole + domaine + port), de **chaînes uniquement**.

```javascript
localStorage.setItem("theme", "sombre");
localStorage.getItem("theme");          // "sombre" (null si absent)
localStorage.removeItem("theme");
localStorage.clear();
localStorage.length;  localStorage.key(0);

// Objets et tableaux : sérialiser en JSON
localStorage.setItem("panier", JSON.stringify([{ id: 1, qte: 2 }]));
const panier = JSON.parse(localStorage.getItem("panier") ?? "[]");

// Réagir aux modifications faites dans un AUTRE onglet
window.addEventListener("storage", e => console.log(e.key, e.newValue));
```

**Limites** : ~5 Mo, **synchrone** (bloque le fil principal), texte uniquement, **lisible par tout script de la page (XSS)**, indisponible dans certains modes de navigation privée ou si le quota est dépassé (`QuotaExceededError`).

Usages : thème, préférences, brouillons, petit cache. ❌ Jamais de mots de passe, jetons sensibles ou données personnelles.

```javascript
function lireStockage(cle, defaut) {
    try { return JSON.parse(localStorage.getItem(cle)) ?? defaut; }
    catch { return defaut; }
}
```

## 22.5 `sessionStorage`

Même API que `localStorage`, mais les données sont **propres à l'onglet** et **supprimées à sa fermeture** (conservées lors d'un rechargement).

```javascript
sessionStorage.setItem("etape", "2");
sessionStorage.getItem("etape");
sessionStorage.clear();
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
new Date("2026-10-11T14:30:00Z");       // chaîne ISO 8601 (fiable)
new Date(2026, 9, 11);                  // ⚠️ mois de 0 à 11 : 9 = octobre
new Date(0);                            // timestamp en millisecondes (epoch 1970)
Date.now();                             // timestamp actuel
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

### Modifier (⚠️ mutent l'objet)

`setFullYear()`, `setMonth()`, `setDate()`, `setHours()`, `setMinutes()`, `setSeconds()`, `setTime()`…

```javascript
const d = new Date("2026-01-31");
d.setMonth(d.getMonth() + 1);            // 😬 débordement : 3 mars et non 28 février
```

### Formater

```javascript
d.toISOString();                         // "2026-10-11T14:30:00.000Z"
d.toLocaleDateString("fr-FR", { dateStyle: "full" });          // "dimanche 11 octobre 2026"
d.toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit" });
new Intl.DateTimeFormat("fr-FR", { dateStyle: "long", timeStyle: "short", timeZone: "Indian/Antananarivo" }).format(d);
new Intl.RelativeTimeFormat("fr", { numeric: "auto" }).format(-1, "day");   // "hier"
```

### Différence entre deux dates

```javascript
const jours = Math.round((date2 - date1) / 86_400_000);   // ⚠️ ignore les changements d'heure
```

### Défauts de `Date`

Mois indexés à 0, objet **mutable**, analyse de chaînes incohérente, **fuseaux horaires limités** (local ou UTC seulement), pas de calendriers non grégoriens, arithmétique source d'erreurs.

## 23.2 `Temporal` : le remplaçant moderne *(à jour)*

**`Temporal`** corrige les défauts de `Date` : objets **immuables**, mois de **1 à 12**, **vrais fuseaux horaires**, calendriers multiples, arithmétique fiable, précision à la **nanoseconde**.

> 📌 **Statut (octobre 2026)** : `Temporal` a atteint le **stade 4** de TC39 en 2026 ; sa publication officielle est prévue dans **ES2027** (ES2026 ne l'inclut pas). Il est déjà disponible dans **Firefox 139+** et **Chrome / Edge 144+** ; la prise en charge de **Safari** peut varier : vérifiez sur [caniuse.com](https://caniuse.com/temporal). Un *polyfill* existe (`@js-temporal/polyfill`).

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
const aujourdHui = Temporal.Now.plainDateISO();            // ex. 2026-10-11
const noel = Temporal.PlainDate.from("2026-12-25");

aujourdHui.until(noel).days;                               // jours restants
aujourdHui.add({ months: 1 });                             // 2026-11-11 (immuable : nouvel objet)
aujourdHui.dayOfWeek;                                      // 1 (lundi) à 7 (dimanche)

const reunion = Temporal.ZonedDateTime.from("2026-10-11T14:30[Indian/Antananarivo]");
reunion.withTimeZone("Europe/Paris").toString();           // conversion de fuseau

reunion.toLocaleString("fr-FR", { dateStyle: "full", timeStyle: "short" });
Temporal.PlainDate.compare(a, b);                          // -1, 0 ou 1
```

### `Date` → `Temporal`

```javascript
const instant = new Date().toTemporalInstant();            // si disponible
```

> ✅ Pour un nouveau projet : utilisez `Temporal` (ou, en attendant, des bibliothèques comme **date-fns**, **Luxon** ou **Day.js**). Stockez et échangez les dates en **ISO 8601 / UTC**, et ne convertissez en heure locale qu'à l'**affichage**.

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
console.log(x);   console.table(tableau);   console.dir(objet);
console.time("calcul"); /* … */ console.timeEnd("calcul");
console.assert(x > 0, "x doit être positif");
debugger;                                    // point d'arrêt dans les DevTools
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

> 📌 Les listes de fonctionnalités par édition circulent avec des contradictions sur Internet : la source de référence est le tableau des **propositions terminées** de TC39 ([github.com/tc39/proposals](https://github.com/tc39/proposals/blob/main/finished-proposals.md)). Vérifiez toujours la **compatibilité navigateur** sur [caniuse.com](https://caniuse.com) et [MDN](https://developer.mozilla.org/fr/).

## Ressources pour progresser

- 📘 **MDN Web Docs** : <https://developer.mozilla.org/fr/docs/Web/JavaScript>
- 📗 **javascript.info** (en français) : <https://fr.javascript.info>
- 📜 **Spécification** : <https://tc39.es/ecma262/>
- 🧪 **Exercices** : voir la section « Ressources » en début de guide

---

<div align="center">

*Bon code ! 🟨*

</div>
