<div align="center">

# JavaScript — Exercices

**Des variables aux modules, du DOM à l'asynchrone et à Temporal**

*Mis à jour pour ECMAScript 2026 (octobre 2026)*

</div>

---

## Ressources

| Ressource | Lien |
| --- | --- |
| Cours | [javascript](/language/javascript) |
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

> **Légende** : chaque exercice porte le numéro de la section du cours qu'il illustre (l'exercice 8.4.2 est le deuxième exercice de la section 8.4). Le chapitre 25, qui n'a pas de sections, est numéroté 25.1, 25.2, etc. *(défi)* = exercice plus difficile ; *(ajout)* et *(à jour)* reprennent les mentions du cours ; *(ES20xx)* = exercice nécessitant la version indiquée d'ECMAScript. Aucune solution n'est fournie dans ce document.
>
> **Convention des exercices** : sauf mention contraire, les exercices s'exécutent dans Node.js ou dans la console du navigateur ; les exercices DOM, de stockage et de navigation demandent un navigateur, ceux qui utilisent `fetch` demandent une connexion Internet, et les exercices de modules (`import` / `export`) demandent plusieurs fichiers. Quand l'énoncé demande de « prédire » une sortie, répondez d'abord de tête, puis vérifiez en exécutant le code. Une erreur volontaire doit être entourée d'un `try...catch`.

---

# 1. Introduction

## 1.1 Qu'est-ce que JavaScript ?

**Exercice 1.1.1**

Indiquez si chaque affirmation est vraie ou fausse, en justifiant :

1. JavaScript est un langage compilé à l'avance en code machine, comme le C.
2. JavaScript et Java partagent la même syntaxe et le même moteur d'exécution.
3. ECMAScript est le nom de la norme qui standardise JavaScript.
4. TC39 publie une nouvelle édition d'ECMAScript chaque année.
5. JavaScript ne s'exécute que dans un navigateur.

**Exercice 1.1.2**

Complétez le tableau des environnements d'exécution en donnant, pour chacun, le moteur ou l'environnement et un usage typique :

| Environnement | Moteur / exemple | Usage typique |
| --- | --- | --- |
| Chrome / Edge | | |
| Firefox | | |
| Safari | | |
| Node.js, Deno, Bun | | |
| React Native, Electron, Tauri | | |
| Cloudflare Workers | | |

**Exercice 1.1.3**

Que signifient les termes « interprété / compilé à la volée (JIT) », « dynamique », « multi-paradigme » et « à événements » ? Illustrez chacun par une phrase ou un court extrait de code.

**Exercice 1.1.4**

Quelle est la relation entre JavaScript et TypeScript ? Écrivez un exemple de code valide en JavaScript mais refusé par TypeScript en mode strict.

## 1.2 Exécuter du JavaScript

### Dans une page web

**Exercice 1.2.1**

Créez une page `index.html` qui affiche `Bonjour` dans la console de deux façons : avec un script intégré dans la page, puis avec un fichier externe `script.js`. Où placer la balise `<script>` ? Quel est l'effet des attributs `defer` et `async` ?

**Exercice 1.2.2**

Pourquoi un script placé dans `<head>` sans `defer` ne peut-il pas lire un élément défini plus bas dans la page ? Écrivez un exemple qui échoue puis corrigez-le de deux façons.

### Dans la console du navigateur

**Exercice 1.2.3**

Ouvrez la console de votre navigateur et exécutez `2 + 2`, `"a".toUpperCase()`, `document.title`, `window.innerWidth`. Quelle différence entre `console.log`, `console.warn`, `console.error`, `console.table` et `console.dir` ?

### Avec Node.js

**Exercice 1.2.4**

Créez un fichier `salut.js` qui affiche votre prénom et exécutez-le avec `node salut.js`. Lancez ensuite le REPL de Node.js avec `node`, calculez `Math.sqrt(144)` et quittez avec `.exit`.

**Exercice 1.2.5**

Affichez la version de Node.js (`process.version`), les arguments de la ligne de commande (`process.argv`) et une variable d'environnement (`process.env.HOME` ou `process.env.USERPROFILE`).

## 1.3 Syntaxe de base

**Exercice 1.3.1**

Écrivez un programme avec : un commentaire sur une ligne, un commentaire sur plusieurs lignes, trois instructions séparées par des points-virgules et un bloc. JavaScript est-il sensible à la casse ? Prouvez-le avec trois variables `a`, `A`, `aA`.

**Exercice 1.3.2**

Les points-virgules sont-ils obligatoires ? Écrivez un exemple où l'insertion automatique de points-virgules (ASI) change le comportement d'un `return` placé sur une ligne seule suivi d'un objet sur la ligne suivante.

**Exercice 1.3.3**

Parmi les identifiants suivants, lesquels sont valides : `prix`, `2fois`, `$total`, `_tmp`, `mon-nom`, `class`, `éléphant`, `let`, `Nom_2`, `#secret` ?

**Exercice 1.3.4**

Quelle convention de nommage (camelCase, PascalCase, MAJUSCULES_SNAKE) utilise-t-on pour : une variable, une fonction, une classe, une constante globale ? Écrivez un exemple de chacune.

---

# 2. Variables et portée

## 2.1 Déclarer une variable

**Exercice 2.1.1**

Déclarez une variable avec `let`, une constante avec `const` et une variable avec `var`. Modifiez les trois. Quelle ligne provoque une erreur ?

**Exercice 2.1.2**

Que se passe-t-il pour chacune de ces lignes ? Expliquez :

```js
const a = 5;
a = 6;

const b = [1, 2];
b.push(3);
b = [];

const c = { x: 1 };
c.x = 2;

let d;
console.log(d);

let e = 1;
let e = 2;
```

**Exercice 2.1.3**

Pourquoi recommande-t-on de préférer `const` par défaut, `let` si nécessaire et d'éviter `var` ? Citez trois raisons.

**Exercice 2.1.4**

Déclarez plusieurs variables sur une ligne avec `let a = 1, b = 2, c;`. Pourquoi ce style est-il déconseillé ? Écrivez l'échange de deux variables avec la décomposition (`[a, b] = [b, a]`).

**Exercice 2.1.5**

Que se passe-t-il à l'affectation d'une variable non déclarée (`x = 5` sans `let`) en mode non strict ? En mode strict ?

## 2.2 Portée (*scope*)

**Exercice 2.2.1**

Prédisez la sortie, puis expliquez la différence entre `var` et `let` :

```js
for (var i = 0; i < 3; i++) {}
console.log(i);

for (let j = 0; j < 3; j++) {}
try { console.log(j); } catch (e) { console.log(e.name); }

if (true) {
    var v = "var";
    let l = "let";
}
console.log(v);
try { console.log(l); } catch (e) { console.log(e.name); }
```

**Exercice 2.2.2**

Identifiez les portées (globale, fonction, bloc, module) de chaque variable :

```js
const g = "global";
function f() {
    const loc = "locale";
    if (true) {
        const bloc = "bloc";
        var fonc = "fonction";
    }
    return [g, loc, fonc];
}
```

**Exercice 2.2.3**

Prédisez la sortie, puis expliquez pourquoi `let` donne le résultat attendu et `var` non :

```js
const fa = [];
for (var i = 0; i < 3; i++) fa.push(() => i);
console.log(fa.map(f => f()));

const fb = [];
for (let i = 0; i < 3; i++) fb.push(() => i);
console.log(fb.map(f => f()));
```

**Exercice 2.2.4**

Qu'est-ce que l'ombrage (*shadowing*) ? Écrivez un exemple où une variable d'un bloc masque une variable externe de même nom. Quelle règle de linter (`no-shadow`) le détecte ?

**Exercice 2.2.5**

Quelles variables sont créées sur l'objet global (`window` / `globalThis`) : `var` au niveau supérieur d'un script classique, `let` au niveau supérieur, `var` dans un module ? Vérifiez dans un navigateur.

## 2.3 Hoisting et zone morte temporelle (TDZ)

**Exercice 2.3.1**

Prédisez la sortie :

```js
console.log(a);
var a = 1;

try { console.log(b); } catch (e) { console.log(e.name + " : " + e.message); }
let b = 2;

console.log(typeof f);
function f() {}

console.log(typeof g);
var g = function () {};
```

**Exercice 2.3.2**

Expliquez ce qu'est la zone morte temporelle (TDZ). À partir de quel moment une variable `let` est-elle utilisable ? Écrivez un exemple de TDZ dans un paramètre par défaut (`function f(a = b, b = 1)`).

**Exercice 2.3.3**

Quelle différence de hoisting entre une déclaration de fonction, une expression de fonction et une fonction fléchée ? Pour chacune, peut-on l'appeler avant sa définition ?

**Exercice 2.3.4**

Pourquoi `typeof` n'est-il pas sûr dans la TDZ alors qu'il l'est pour une variable jamais déclarée ? Écrivez les deux cas.

## 2.4 Affectation par décomposition *(destructuring)*

**Exercice 2.4.1**

Décomposez `const t = [10, 20, 30, 40]` pour obtenir : les deux premiers éléments, le premier et le reste, le troisième en ignorant les deux premiers, une valeur par défaut pour un cinquième élément.

**Exercice 2.4.2**

Décomposez `const u = { nom: "Alice", age: 30, adresse: { ville: "Lyon", cp: "69000" } }` pour obtenir : `nom`, `age` renommé en `annees`, `ville` imbriquée, un champ absent avec valeur par défaut, le reste des propriétés avec `...reste`.

**Exercice 2.4.3**

Écrivez une fonction `afficher({ nom, age = 18, role = "user" } = {})` qui décompose son paramètre. Appelez-la avec un objet complet, partiel et sans argument.

**Exercice 2.4.4**

Décomposez le résultat d'une fonction qui renvoie plusieurs valeurs, puis échangez deux valeurs dans un tableau sans variable temporaire.

**Exercice 2.4.5**

Pourquoi `{ a, b } = obj;` en début de ligne provoque-t-il une erreur de syntaxe ? Comment la corriger avec des parenthèses ?

**Exercice 2.4.6**

Que se passe-t-il quand on décompose `null` ou `undefined` (`const { x } = null`) ? Écrivez une protection avec `?? {}`.

---

# 3. Types de valeurs

## 3.1 Primitifs et références

**Exercice 3.1.1**

Citez les sept types primitifs de JavaScript (`string`, `number`, `bigint`, `boolean`, `undefined`, `null`, `symbol`) et donnez un littéral pour chacun. Que signifie « immuable » pour un primitif ?

**Exercice 3.1.2**

Prédisez la sortie :

```js
let a = 5;
let b = a;
b = 10;
console.log(a, b);

const o1 = { v: 1 };
const o2 = o1;
o2.v = 2;
console.log(o1.v, o1 === o2);

const t1 = [1, 2];
const t2 = [1, 2];
console.log(t1 === t2, t1 == t2);

let s = "abc";
s[0] = "X";
console.log(s);
```

**Exercice 3.1.3**

Écrivez une fonction `modifierObjet(o)` qui modifie une propriété de l'objet reçu et une fonction `reaffecter(o)` qui réaffecte son paramètre `o = { x: 99 }`. Quel effet chacune a-t-elle sur la variable de l'appelant ? Qu'en déduisez-vous sur le passage « par partage » ?

**Exercice 3.1.4**

Que renvoient `typeof NaN`, `NaN === NaN`, `Number.isNaN(NaN)`, `Object.is(NaN, NaN)`, `Object.is(0, -0)`, `0 === -0` ?

### Copier un objet

**Exercice 3.1.5**

Copiez `const base = { a: 1, sous: { b: 2 }, liste: [1, 2] }` de quatre manières : `{ ...base }`, `Object.assign({}, base)`, `structuredClone(base)`, `JSON.parse(JSON.stringify(base))`. Modifiez `copie.sous.b` et `copie.liste` et dites, pour chaque copie, si l'original est affecté.

**Exercice 3.1.6**

Quelles données `structuredClone` copie-t-il correctement (`Date`, `Map`, `Set`, références circulaires) ? Quelles données fait-il échouer (fonctions, éléments DOM) ? Quelles données la voie JSON altère-t-elle (`Date`, `undefined`, `NaN`, `Map`) ? Testez chaque cas.

**Exercice 3.1.7**

Écrivez `copieProfonde(valeur)` récursive qui gère objets, tableaux et dates, sans `structuredClone`. *(défi)*

## 3.2 L'opérateur `typeof`

**Exercice 3.2.1**

Prédisez le résultat de `typeof` pour : `42`, `"a"`, `true`, `undefined`, `null`, `[]`, `{}`, `function () {}`, `class A {}`, `Symbol()`, `10n`, `new Date()`, `NaN`, `undeclaredVar`.

**Exercice 3.2.2**

Pourquoi `typeof null` vaut-il `"object"` ? Écrivez une fonction `typeDe(valeur)` qui distingue correctement `null`, `array`, `date`, `regexp`, `object` et les primitifs (`Array.isArray`, `Object.prototype.toString.call`).

**Exercice 3.2.3**

Écrivez une fonction `estObjetSimple(x)` qui renvoie `true` seulement pour les objets littéraux (pas les tableaux, `null`, dates, instances de classes).

## 3.3 Conversions et coercition

**Exercice 3.3.1**

Prédisez : `"5" + 3`, `"5" - 3`, `"5" * "2"`, `true + 1`, `[] + []`, `[] + {}`, `null + 1`, `undefined + 1`, `"b" + "a" + +"a" + "a"`, `+"abc"`, `+""`, `+" 12 "`, `+[]`, `+[5]`.

**Exercice 3.3.2**

Convertissez explicitement : `"42"`, `"42px"`, `"3.14"`, `""`, `null`, `undefined`, `true` en nombre avec `Number()`, `parseInt()`, `parseFloat()` et `+`. Notez les différences.

**Exercice 3.3.3**

Classez en « truthy » ou « falsy » : `0`, `-0`, `0n`, `""`, `" "`, `"0"`, `"false"`, `null`, `undefined`, `NaN`, `[]`, `{}`, `function () {}`, `new Boolean(false)`.

**Exercice 3.3.4**

Écrivez une fonction `versNombre(texte)` qui renvoie un nombre ou `null` pour toute entrée non numérique (y compris la chaîne vide et les espaces), sans accepter `"12abc"`.

**Exercice 3.3.5**

Pourquoi `parseInt("08")`, `parseInt("0x1A")`, `parseInt("101", 2)`, `parseInt(0.0000005)` donnent-ils ces résultats ? Quel est le rôle du second paramètre (base) ?

**Exercice 3.3.6**

Quelles valeurs la fonction `String()` renvoie-t-elle pour `null`, `undefined`, `[1, 2]`, `{}`, `Symbol("x")` ? Quelle différence avec `.toString()` sur `null` ?

## 3.4 Égalité

**Exercice 3.4.1**

Prédisez, pour `==` et `===` : `1 == "1"`, `0 == ""`, `0 == "0"`, `"" == "0"`, `null == undefined`, `null == 0`, `null >= 0`, `NaN == NaN`, `[] == false`, `[1] == 1`, `"b" > "a"`, `"10" < "9"`, `10 < "9"`.

**Exercice 3.4.2**

Pourquoi recommande-t-on `===` systématiquement ? Y a-t-il un cas où `== null` est un idiome accepté ? Écrivez-le.

**Exercice 3.4.3**

Écrivez `egaliteProfonde(a, b)` qui compare récursivement deux valeurs (objets, tableaux, primitifs, dates). *(défi)*

**Exercice 3.4.4**

Quelle est la différence entre `===`, `==`, `Object.is` et `SameValueZero` (utilisé par `includes`, `Set`, `Map`) ? Testez-les sur `NaN`, `0` et `-0`.

---

# 4. Opérateurs

## 4.1 Catégories

**Exercice 4.1.1**

Prédisez : `7 / 2`, `7 % 3`, `-7 % 3`, `2 ** 10`, `2 ** -1`, `(-2) ** 2`, `5 / 0`, `-5 / 0`, `0 / 0`, `10 % 0`, `0.1 + 0.2`, `++x` et `x++` avec `x = 5`.

**Exercice 4.1.2**

Écrivez une fonction `modulo(a, b)` qui renvoie un résultat toujours positif, même pour `a` négatif.

**Exercice 4.1.3**

Évaluez avec les opérateurs bit à bit : `5 & 3`, `5 | 3`, `5 ^ 3`, `~5`, `5 << 2`, `-16 >> 2`, `-16 >>> 28`. Écrivez les opérations de test, d'activation, de désactivation et de bascule d'un bit.

**Exercice 4.1.4**

Quel est le résultat de `"a" + 1 + 2`, `1 + 2 + "a"`, `"3" + 4 * "5"`, `"3" * "4" + "5"` ? Expliquez l'ordre d'évaluation.

**Exercice 4.1.5**

Quelles différences entre `a++` et `++a` quand le résultat est utilisé dans une expression ? Écrivez un programme qui l'illustre.

**Exercice 4.1.6**

Utilisez les opérateurs d'affectation composés (`+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `<<=`, `>>>=`, `&=`, `|=`, `^=`) pour transformer une variable en suivant une séquence d'instructions, puis donnez sa valeur finale.

## 4.2 Fusion nulle `??`

**Exercice 4.2.1**

Prédisez : `0 || 10`, `0 ?? 10`, `"" || "défaut"`, `"" ?? "défaut"`, `null ?? "x"`, `undefined ?? "y"`, `false ?? true`, `NaN ?? 5`.

**Exercice 4.2.2**

Écrivez une fonction `lireConfig(options)` qui lit `options.port`, `options.verbeux`, `options.nom` avec des valeurs par défaut (3000, `false`, `"anonyme"`) sans écraser un `0`, un `false` ou une chaîne vide valides.

**Exercice 4.2.3**

Pourquoi ne peut-on pas mélanger `??` avec `||` ou `&&` sans parenthèses ? Écrivez l'erreur obtenue et sa correction.

## 4.3 Chaînage optionnel `?.`

**Exercice 4.3.1**

Soit `const u = { nom: "Alice", adresse: { ville: "Lyon" }, amis: [{ nom: "Bob" }], saluer() { return "salut"; } }`. Lisez en sécurité : `u.adresse?.ville`, `u.travail?.titre`, `u.amis?.[0]?.nom`, `u.amis?.[5]?.nom`, `u.saluer?.()`, `u.partir?.()`.

**Exercice 4.3.2**

Quelle différence entre `a?.b` et `a && a.b` pour `a = 0`, `a = ""`, `a = null` ? Donnez le résultat de chaque.

**Exercice 4.3.3**

Combinez `?.` et `??` pour afficher `utilisateur?.profil?.langue ?? "fr"`. Écrivez un test avec cinq formes d'`utilisateur`.

**Exercice 4.3.4**

Que se passe-t-il pour `a?.b.c.d` si `a` est `null` ? (court-circuit de toute la chaîne). Que se passe-t-il si `a.b` est `undefined` ?

## 4.4 Affectations logiques

**Exercice 4.4.1**

Prédisez les valeurs finales de `x` pour chaque opérateur, avec `x` initial valant `0`, `null`, `""`, `5` : `x ||= 10`, `x &&= 10`, `x ??= 10`.

**Exercice 4.4.2**

Réécrivez avec `??=` : `if (cache[cle] === undefined) cache[cle] = calculer(cle);`. Écrivez un cache à initialisation paresseuse. Quel est l'avantage du court-circuit (la partie droite n'est pas évaluée si inutile) ?

**Exercice 4.4.3**

Initialisez avec `||=` les options d'une fonction : `options.nom ||= "défaut"`. Quel risque avec une valeur légitime « falsy » ?

## 4.5 Ternaire, `in`, `instanceof`

**Exercice 4.5.1**

Écrivez en une ligne : la valeur absolue d'un nombre, le signe d'un nombre (`"positif"`, `"négatif"`, `"nul"`), le pluriel d'un mot selon un compteur. Réécrivez ensuite le dernier avec `if`/`else`.

**Exercice 4.5.2**

Quelle différence entre `"x" in objet`, `objet.x !== undefined`, `objet.hasOwnProperty("x")` et `Object.hasOwn(objet, "x")` pour une propriété héritée du prototype et une propriété valant `undefined` ?

**Exercice 4.5.3**

Que renvoient `[] instanceof Array`, `[] instanceof Object`, `Object.create(null) instanceof Object`, `5 instanceof Number`, `new Number(5) instanceof Number` ? Pourquoi `instanceof` échoue-t-il entre des fenêtres (iframes) différentes ?

**Exercice 4.5.4**

Que font `delete obj.prop`, `void 0`, `typeof`, et l'opérateur virgule `(1, 2, 3)` ? Écrivez un exemple utile pour chacun.

## 4.6 Priorité

**Exercice 4.6.1**

Ajoutez les parenthèses implicites et évaluez : `2 + 3 * 4 ** 2`, `!a && b || c`, `a ?? b || c` (erreur ?), `typeof x === "string"`, `-2 ** 2` (erreur ?), `1 + 2 << 3`, `a = b = 5`, `x ? y : z ? w : v`.

**Exercice 4.6.2**

Classez par priorité décroissante : `**`, `*`, `+`, `<<`, `<`, `===`, `&`, `&&`, `||`, `??`, `?:`, `=`, `,`.

## 4.7 Bonnes pratiques

**Exercice 4.7.1**

Réécrivez cette expression dense en plusieurs lignes lisibles avec des variables intermédiaires nommées :

```js
const r = a?.b ?? (c && d ? e : f || g) + (h ?? i) * (j ? 2 : 1);
```

**Exercice 4.7.2**

Listez cinq bonnes pratiques sur les opérateurs (`===`, parenthèses explicites, `??` plutôt que `||` pour les valeurs par défaut, éviter les ternaires imbriqués, `?.` avec modération) et illustrez chacune.

---

# 5. Chaînes de caractères

## 5.1 Déclarer des chaînes

**Exercice 5.1.1**

Écrivez la même chaîne `Il a dit : "Salut, l'ami !"` avec des apostrophes, des guillemets et des accents graves (gabarits). Laquelle ne nécessite aucun échappement ?

**Exercice 5.1.2**

Utilisez un gabarit pour afficher `Total : 3 articles à 12.50 € = 37.50 €` à partir de variables. Utilisez une expression dans `${...}` (calcul, ternaire, appel de fonction).

**Exercice 5.1.3**

Écrivez une chaîne sur plusieurs lignes avec un gabarit et avec la concaténation de `\n`. Comment éviter l'indentation parasite dans un gabarit multiligne ?

### Caractères d'échappement

**Exercice 5.1.4**

Affichez : une tabulation, un retour à la ligne, une barre oblique inverse, un guillemet à l'intérieur d'une chaîne entre guillemets, un caractère Unicode `\u00e9`, un caractère hors du plan basique `\u{1F600}`, et un octet `\x41`. Que fait `String.raw` ?

**Exercice 5.1.5**

Pourquoi `"C:\nouveau\test"` ne s'affiche-t-il pas comme prévu ? Corrigez de trois façons.

### Gabarits étiquetés *(ajout)*

**Exercice 5.1.6**

Écrivez une fonction étiquette `surligner` qui entoure de `**` chaque valeur interpolée : `` surligner`Bonjour ${nom}, vous avez ${n} messages` ``. Affichez les paramètres `chaines` et `valeurs` pour comprendre leur structure.

**Exercice 5.1.7**

Écrivez une étiquette `html` qui échappe les caractères `<`, `>`, `&`, `"` des valeurs interpolées pour éviter une injection. Testez avec `<script>alert(1)</script>`.

**Exercice 5.1.8**

Utilisez `String.raw` comme gabarit étiqueté pour écrire une expression régulière ou un chemin Windows sans doubler les barres obliques inverses.

## 5.2 Propriétés et accès

**Exercice 5.2.1**

Soit `const s = "JavaScript"`. Calculez `s.length`, `s[0]`, `s[s.length - 1]`, `s.at(-1)`, `s.charAt(4)`, `s.charCodeAt(0)`, `s.codePointAt(0)`, `s[100]`, `s.at(100)`.

**Exercice 5.2.2**

Pourquoi `"\u{1D11E}".length` (le symbole musical « clé de sol », hors du plan multilingue de base) vaut-il 2 ? Comparez `"\u{1D11E}".length`, `[..."\u{1D11E}"].length`, `Array.from("\u{1D11E}").length`, puis `"e\u0301".length` (la lettre « e » suivie d'un accent combinant) et `"\u00e9".length`. Comment compter les « vrais » caractères perçus par l'utilisateur (`Intl.Segmenter`) ? *(défi)*

**Exercice 5.2.3**

Parcourez une chaîne de quatre façons : boucle `for` avec indices, `for...of`, `forEach` sur un tableau (`[...s]`), `Array.from`. Quelle méthode gère correctement les paires de substitution ?

**Exercice 5.2.4**

Pourquoi `s[0] = "X"` est-il sans effet (ou une erreur en mode strict) ? Comment « modifier » le premier caractère d'une chaîne ?

## 5.3 Méthodes principales

**Exercice 5.3.1**

Pour chacune des méthodes suivantes, écrivez un exemple de code et le résultat : `toUpperCase`, `toLowerCase`, `trim`, `trimStart`, `trimEnd`, `padStart`, `padEnd`, `repeat`, `slice`, `substring`, `substr` (obsolète), `split`, `join`, `includes`, `startsWith`, `endsWith`, `indexOf`, `lastIndexOf`, `search`, `replace`, `replaceAll`, `localeCompare`, `normalize`, `at`.

**Exercice 5.3.2**

Quelle différence entre `slice(-3)`, `substring(-3)` et `substr(-3)` ? Entre `slice(2, 5)` et `slice(5, 2)` ? Entre `substring(5, 2)` et `substring(2, 5)` ?

**Exercice 5.3.3**

Pourquoi `"a-b-c".replace("-", "+")` ne remplace-t-il que la première occurrence ? Réalisez le remplacement global de trois façons : `replaceAll`, expression régulière avec `g`, `split`/`join`.

**Exercice 5.3.4**

Écrivez `capitaliser(texte)`, `titre(texte)` (chaque mot avec majuscule), `inverser(texte)`, `estPalindrome(texte)` (insensible à la casse, aux espaces et à la ponctuation), `compterVoyelles(texte)`, `tronquer(texte, n)` (avec `…`).

**Exercice 5.3.5**

Écrivez `slugifier(texte)` : minuscules, suppression des accents (`normalize("NFD")` et suppression des diacritiques), remplacement des espaces et caractères spéciaux par des tirets. Testez avec `"Éléphant à l'été !"`.

**Exercice 5.3.6**

Écrivez `compterMots(texte)` qui renvoie un objet (ou une `Map`) des fréquences de chaque mot, insensible à la casse et à la ponctuation, puis les trois mots les plus fréquents.

**Exercice 5.3.7**

Triez `["éclair", "zèbre", "abricot", "Éléphant"]` avec `sort()` seul puis avec `localeCompare("fr")` et `Intl.Collator`. Pourquoi les résultats diffèrent-ils ?

**Exercice 5.3.8**

Quelle est l'utilité de `isWellFormed()` et `toWellFormed()` ? Écrivez un exemple avec une chaîne contenant une paire de substitution isolée. *(ES2024)*

**Exercice 5.3.9**

Écrivez une fonction de chiffrement de César `cesar(texte, decalage)` qui conserve la casse et ignore les caractères non alphabétiques, puis son déchiffrement.

## 5.4 Bonnes pratiques

**Exercice 5.4.1**

Mesurez le temps de construction d'une chaîne de 100 000 morceaux par concaténation (`+=`) et par `tableau.join("")`. Que concluez-vous ? Les moteurs modernes optimisent-ils `+=` ?

**Exercice 5.4.2**

Listez cinq bonnes pratiques sur les chaînes (gabarits, `includes` plutôt que `indexOf`, `replaceAll`, `normalize` pour les comparaisons accentuées, `Intl` pour le tri) et illustrez chacune.

---

# 6. Nombres et `Math`

## 6.1 Le type `number`

**Exercice 6.1.1**

Écrivez les littéraux `255` en décimal, hexadécimal (`0xFF`), octal (`0o377`), binaire (`0b11111111`), avec séparateur (`1_000_000`), avec exposant (`1.5e3`). Affichez leur valeur et leur type.

**Exercice 6.1.2**

Quelles sont les valeurs de `Number.MAX_SAFE_INTEGER`, `Number.MIN_SAFE_INTEGER`, `Number.MAX_VALUE`, `Number.MIN_VALUE`, `Number.EPSILON`, `Infinity`, `-Infinity` ? Que renvoie `Number.MAX_SAFE_INTEGER + 2` ? Pourquoi ?

**Exercice 6.1.3**

Écrivez des fonctions `estEntier(x)`, `estEntierSur(x)`, `estFini(x)`, en utilisant `Number.isInteger`, `Number.isSafeInteger`, `Number.isFinite`. Quelle différence avec les versions globales `isNaN` et `isFinite` ?

**Exercice 6.1.4**

Quelles opérations produisent `NaN` ? Testez : `0 / 0`, `Math.sqrt(-1)`, `parseInt("abc")`, `undefined + 1`, `Infinity - Infinity`, `"a" * 2`. Comment détecter `NaN` de façon fiable ?

### Précision des flottants

**Exercice 6.1.5**

Expliquez pourquoi `0.1 + 0.2 !== 0.3`, puis écrivez `egauxApprox(a, b)` avec `Number.EPSILON`. Quelle approche utilisez-vous pour les montants d'argent (entiers en centimes, `BigInt`, bibliothèque décimale) ?

**Exercice 6.1.6**

Calculez `1.005 * 100`, `Math.round(1.005 * 100) / 100`, `(1.005).toFixed(2)`, `Math.round((1.005 + Number.EPSILON) * 100) / 100`. Écrivez `arrondir(x, decimales)` fiable.

**Exercice 6.1.7**

Quelle valeur renvoie `0.1 * 3`, `0.7 + 0.1`, `0.3 - 0.1`, `9007199254740993` ? Pourquoi certains calculs sont-ils exacts et d'autres non ?

## 6.2 Méthodes et propriétés de `Number`

**Exercice 6.2.1**

Utilisez `toFixed`, `toPrecision`, `toExponential`, `toString(2)`, `toString(16)`, `Number.parseFloat`, `Number.parseInt` sur `1234.5678`. Que renvoie `toFixed` (un nombre ou une chaîne) ?

**Exercice 6.2.2**

Écrivez `versBinaire(n)`, `depuisBinaire(chaine)`, `versHex(n)` en utilisant les méthodes natives. Écrivez ensuite un convertisseur manuel vers une base quelconque de 2 à 36.

**Exercice 6.2.3**

Pourquoi `5.toString()` est-il une erreur de syntaxe alors que `5..toString()` et `(5).toString()` fonctionnent ?

## 6.3 `BigInt` *(ajout)*

**Exercice 6.3.1**

Calculez `2n ** 100n`, `Number.MAX_SAFE_INTEGER + 2` et `BigInt(Number.MAX_SAFE_INTEGER) + 2n`. Quelle est la limite de précision du type `number` ?

**Exercice 6.3.2**

Que se passe-t-il pour `1n + 1` ? `5n / 2n` ? `typeof 1n` ? `1n == 1` ? `1n === 1` ? `BigInt(1.5)` ? Comment convertir proprement entre `number` et `bigint` ?

**Exercice 6.3.3**

Écrivez une fonction `factorielle(n)` avec `BigInt` et calculez `50n` !. Combien de chiffres a `100!` ?

**Exercice 6.3.4**

Pourquoi `JSON.stringify({ x: 1n })` échoue-t-il ? Écrivez deux façons de sérialiser des `BigInt` (fonction de remplacement, `toJSON`).

## 6.4 L'objet `Math`

**Exercice 6.4.1**

Calculez : `Math.round(2.5)`, `Math.round(-2.5)`, `Math.round(2.4)`, `Math.floor(-2.1)`, `Math.ceil(-2.1)`, `Math.trunc(-2.9)`, `Math.sign(-3)`, `Math.abs(-4)`, `Math.max()`, `Math.min()`, `Math.max(...[3, 1, 2])`, `Math.hypot(3, 4)`, `Math.cbrt(27)`, `Math.pow(2, 8)`.

**Exercice 6.4.2**

Écrivez `entierAleatoire(min, max)` (bornes incluses), `choixAleatoire(tableau)`, `melanger(tableau)` (Fisher-Yates) et `lancerDe(faces)`. Pourquoi `[...tableau].sort(() => Math.random() - 0.5)` donne-t-il un mauvais mélange ?

**Exercice 6.4.3**

Écrivez une fonction `distance(p1, p2)` entre deux points, `aireCercle(r)`, `degresVersRadians(d)` avec `Math.PI`, `Math.hypot`, `Math.sin`, `Math.cos`.

**Exercice 6.4.4**

Que fait `Math.random()` ? Pourquoi ne convient-il pas à la cryptographie ? Quelle API utiliser (`crypto.getRandomValues`, `crypto.randomUUID`) ?

**Exercice 6.4.5**

Utilisez `Math.sumPrecise` pour additionner `[0.1, 0.2, 0.3]` et comparez avec `reduce`. *(ES2026)*

**Exercice 6.4.6**

Écrivez `limiter(valeur, min, max)` (*clamp*), `interpoler(a, b, t)` et `normaliser(valeur, min, max)`.

## 6.5 Formater les nombres avec `Intl` *(à jour)*

**Exercice 6.5.1**

Formatez `1234567.891` avec `toLocaleString` pour `fr-FR`, `en-US`, `de-DE`, `en-IN`. Quelles différences de séparateurs ?

**Exercice 6.5.2**

Utilisez `Intl.NumberFormat` pour formater une monnaie (`style: "currency"`, `currency: "EUR"`), un pourcentage, une unité (`kilometer-per-hour`), une notation compacte (`1,2 M`), des chiffres minimaux et maximaux.

**Exercice 6.5.3**

Utilisez `Intl.PluralRules`, `Intl.ListFormat` et `Intl.RelativeTimeFormat` pour afficher « 1 fichier / 2 fichiers », « A, B et C », « il y a 3 jours ».

**Exercice 6.5.4**

Pourquoi préférer `Intl` aux fonctions de formatage maison ? Quels sont les avantages de créer une fois le formateur et de le réutiliser ?

---

# 7. Conditions et boucles

## 7.1 Conditions

**Exercice 7.1.1**

Écrivez un programme qui affiche la mention d'une note sur 20 (`< 10` : refusé, `10 à 12` : passable, `12 à 14` : assez bien, `14 à 16` : bien, `≥ 16` : très bien) avec `if` / `else if` / `else`.

**Exercice 7.1.2**

Écrivez `estBissextile(annee)`, `typeTriangle(a, b, c)`, `resoudreSecondDegre(a, b, c)` en vérifiant les cas particuliers.

**Exercice 7.1.3**

Réécrivez avec des clauses de garde (retours anticipés) :

```js
function traiter(u) {
    if (u) {
        if (u.actif) {
            if (u.age >= 18) {
                return "Bienvenue " + u.nom;
            } else {
                return "Mineur";
            }
        } else {
            return "Inactif";
        }
    } else {
        return "Inconnu";
    }
}
```

**Exercice 7.1.4**

Pourquoi `if (x = 5)` est-il presque toujours une erreur ? Quelle règle de linter (`no-cond-assign`) l'interdit-elle ?

### `switch`

**Exercice 7.1.5**

Écrivez `nomDuJour(n)` avec `switch` (1 à 7), avec `default`. Que se passe-t-il quand on oublie un `break` (chute, *fall-through*) ? Utilisez la chute à bon escient pour regrouper des cas.

**Exercice 7.1.6**

Écrivez `switch (true)` pour classer une température. Quels sont les avantages et inconvénients de cette forme par rapport à `if`/`else if` ?

**Exercice 7.1.7**

Remplacez un `switch` par un objet de correspondance (ou une `Map`) de fonctions. Quand cette alternative est-elle préférable ?

### Ternaire et opérateurs logiques

**Exercice 7.1.8**

Utilisez `&&` et `||` pour exécuter conditionnellement une fonction et pour définir une valeur par défaut. Quels sont les pièges de `||` avec `0` et `""` ?

**Exercice 7.1.9**

Écrivez une fonction qui renvoie `"pair"` ou `"impair"` avec un ternaire, puis une version à trois branches (`"zéro"`) avec ternaires imbriqués. Réécrivez-la avec `if` pour la lisibilité.

## 7.2 Boucles

**Exercice 7.2.1**

Affichez les entiers de 1 à 10 avec `for`, `while`, `do...while`. Quelle différence essentielle entre `while` et `do...while` ?

**Exercice 7.2.2**

Calculez : la somme de 1 à 100, la factorielle de 10, la somme des chiffres d'un entier, le nombre de chiffres d'un entier, le PGCD de deux entiers (Euclide), les nombres premiers inférieurs à 100.

**Exercice 7.2.3**

Écrivez le programme FizzBuzz de 1 à 100, puis la table de multiplication de 1 à 10 sous forme de grille alignée avec `padStart`.

**Exercice 7.2.4**

Parcourez un tableau avec `for`, `for...of`, `forEach`, `for...in`. Parcourez un objet avec `for...in`, `Object.keys`, `Object.entries`. Quel est le piège de `for...in` sur un tableau ? Sur un objet avec un prototype ?

**Exercice 7.2.5**

Prédisez la sortie, puis expliquez :

```js
for (const i in ["a", "b"]) console.log(typeof i, i);
for (const x of ["a", "b"]) console.log(x);
for (const ch of "hé\u{1D11E}") console.log(ch);
for (const [k, v] of Object.entries({ a: 1, b: 2 })) console.log(k, v);
```

**Exercice 7.2.6**

Écrivez la suite de Collatz à partir d'un entier donné avec `while`, et la suite de Fibonacci jusqu'à `n` termes.

**Exercice 7.2.7**

Quand préférer `for...of` à `forEach` ? Pourquoi `await` ne fonctionne-t-il pas comme attendu dans `forEach` ? Écrivez un exemple avec un `async`.

### `break`, `continue` et étiquettes

**Exercice 7.2.8**

Utilisez `break` pour trouver le premier multiple de 7 supérieur à 100 et `continue` pour sauter les multiples de 3 de 1 à 20.

**Exercice 7.2.9**

Utilisez une boucle étiquetée (`externe: for ...`) pour sortir de deux boucles imbriquées dès qu'une paire de nombres vérifie une condition (par exemple `a * b === 42`). Proposez une alternative avec une fonction et `return`.

**Exercice 7.2.10**

Affichez les triangles d'étoiles suivants pour `n = 5` à l'aide de boucles imbriquées, puis le damier 8×8 :

```text
*
**
***
****
*****
```

```text
    *
   ***
  *****
 *******
*********
```

## 7.3 Bonnes pratiques

**Exercice 7.3.1**

Pourquoi faut-il éviter de modifier un tableau pendant qu'on le parcourt ? Montrez le problème avec `splice` dans une boucle et corrigez-le de deux façons.

**Exercice 7.3.2**

Remplacez des boucles impératives par des méthodes de tableau (`map`, `filter`, `reduce`, `some`, `every`, `find`) dans trois exemples de votre choix.

---

# 8. Tableaux

## 8.1 Créer et accéder

**Exercice 8.1.1**

Créez un tableau par littéral, avec `new Array(3)`, `Array.of(3)`, `Array.from("abc")`, `Array.from({ length: 5 }, (_, i) => i * 2)`, `[...Array(3).keys()]`, `Array(3).fill(0)`. Quel piège avec `new Array(3)` (cases « vides ») ?

**Exercice 8.1.2**

Soit `const t = [10, 20, 30, 40, 50]`. Calculez `t[0]`, `t[t.length - 1]`, `t.at(-1)`, `t.at(-2)`, `t[10]`, `t.length`, `t.slice(1, 3)`, `t.slice(-2)`. Que se passe-t-il quand on écrit `t.length = 2` ? Quand on affecte `t[10] = 1` ?

**Exercice 8.1.3**

Quelle différence entre `Array.isArray`, `instanceof Array` et `typeof` pour détecter un tableau ? Testez avec un tableau, un objet, une `NodeList`, un objet « array-like ».

**Exercice 8.1.4**

Convertissez un objet « array-like » (`{ 0: "a", 1: "b", length: 2 }`) et une `NodeList` en vrai tableau de trois façons (`Array.from`, spread, `Array.prototype.slice.call`).

## 8.2 Ajouter, retirer, modifier

**Exercice 8.2.1**

Utilisez `push`, `pop`, `shift`, `unshift`, `splice`, `fill`, `copyWithin`, `reverse`, `sort` et indiquez pour chacune : valeur de retour et mutation ou non du tableau.

**Exercice 8.2.2**

Avec `splice`, écrivez : insérer en position 2, supprimer 2 éléments à partir de la position 1, remplacer un élément, supprimer le dernier. Quelles sont les valeurs retournées ?

**Exercice 8.2.3**

Pourquoi `["10", "9", "1"].sort()` donne-t-il `["1", "10", "9"]` ? Triez correctement des nombres, des chaînes accentuées et des objets selon une propriété.

**Exercice 8.2.4**

Écrivez `supprimerDoublons(tableau)` (avec `Set`), `supprimerElement(tableau, valeur)` (sans mutation), `inserer(tableau, index, valeur)` (sans mutation), `deplacer(tableau, de, vers)`.

### Versions **non mutantes** *(ES2023, à jour)*

**Exercice 8.2.5**

Utilisez `toSorted`, `toReversed`, `toSpliced`, `with` sur un tableau et vérifiez que l'original n'est pas modifié. Écrivez l'équivalent de chaque méthode avec spread et `slice`. *(ES2023)*

**Exercice 8.2.6**

Pourquoi les versions non mutantes sont-elles utiles avec des frameworks réactifs (React, Vue) ? Écrivez la mise à jour immuable d'un élément d'un tableau d'objets.

## 8.3 Parcourir

**Exercice 8.3.1**

Parcourez `["a", "b", "c"]` avec `for`, `for...of`, `forEach`, `entries()`, `keys()`, `values()`. Affichez `0: a`, `1: b`, `2: c`.

**Exercice 8.3.2**

Parcourez un tableau en sens inverse, en sautant un élément sur deux, et de deux tableaux en parallèle (avec indices).

**Exercice 8.3.3**

Que se passe-t-il à l'exécution de `[1, 2, 3].forEach(x => { if (x === 2) return; console.log(x); })` ? Comment interrompre un `forEach` ? Quelle méthode utiliser à la place (`some`, `every`, `for...of`) ?

## 8.4 Méthodes d'ordre supérieur

**Exercice 8.4.1**

Avec `map`, `filter`, `reduce` : à partir de `[1, 2, 3, 4, 5, 6]`, obtenez les carrés, les nombres pairs, la somme, le produit, le maximum (sans `Math.max`), la moyenne, et la somme des carrés des nombres impairs.

**Exercice 8.4.2**

Que renvoie `["1", "2", "3"].map(parseInt)` ? Pourquoi ? Comment corriger ?

**Exercice 8.4.3**

Écrivez avec `reduce` : `compter(tableau)` (objet des fréquences), `grouper(tableau, cle)`, `aplatir(tableau)`, `inverser(tableau)`, `fromEntries` à la main. Que se passe-t-il avec `reduce` sans valeur initiale sur un tableau vide ?

**Exercice 8.4.4**

Quelle différence entre `reduce` et `reduceRight` ? Écrivez la composition de fonctions de droite à gauche avec `reduceRight`.

### Rechercher

**Exercice 8.4.5**

Utilisez `find`, `findIndex`, `findLast`, `findLastIndex`, `indexOf`, `lastIndexOf`, `includes`, `some`, `every` sur `[5, 12, 8, 130, 44]` avec la condition `> 10`. Qu'est-ce qui différencie `find` de `filter` ?

**Exercice 8.4.6**

Pourquoi `[NaN].indexOf(NaN)` vaut `-1` alors que `[NaN].includes(NaN)` vaut `true` ? Comment chercher un objet dans un tableau par valeur de propriété ?

### Regrouper *(ES2024)*

**Exercice 8.4.7**

Utilisez `Object.groupBy` et `Map.groupBy` pour regrouper une liste d'utilisateurs par rôle. Quelle différence entre les deux résultats (objet sans prototype, `Map`) ? *(ES2024)*

**Exercice 8.4.8**

Regroupez des nombres en `pairs` et `impairs`, des mots par première lettre, des produits par tranche de prix avec `Object.groupBy`. *(ES2024)*

### Autres

**Exercice 8.4.9**

Utilisez `flat`, `flatMap`, `join`, `concat`, `slice`, `Array.from`, `entries`, `at`, `Array.fromAsync` sur des exemples. Comment aplatir complètement un tableau imbriqué (`flat(Infinity)`) ? *(Array.fromAsync : ES2026)*

**Exercice 8.4.10**

Écrivez `chunk(tableau, taille)` (découpage en lots), `zip(a, b)`, `unzip(paires)`, `intersection(a, b)`, `difference(a, b)`, `union(a, b)`, `rotation(tableau, n)`, `transposer(matrice)`, `produitCartesien(a, b)`.

## 8.5 Spread, rest et décomposition

**Exercice 8.5.1**

Utilisez le spread pour : copier un tableau, concaténer deux tableaux, insérer des éléments au milieu, passer des éléments à `Math.max`, convertir une chaîne ou un `Set` en tableau.

**Exercice 8.5.2**

Écrivez une fonction `somme(...nombres)` avec un paramètre rest et une fonction qui reçoit un premier paramètre fixe suivi de `...reste`. Quelle différence entre rest et spread ?

**Exercice 8.5.3**

Pourquoi `[...tableau]` est-il une copie superficielle ? Montrez le problème avec un tableau d'objets.

## 8.6 Tableaux d'objets

**Exercice 8.6.1**

Soit une liste de produits `{ nom, prix, categorie, stock }`. Écrivez : les produits en stock, les noms triés par prix décroissant, le prix moyen, le produit le plus cher, le total du stock par catégorie, l'existence d'un produit gratuit.

**Exercice 8.6.2**

Écrivez des fonctions d'immutabilité sur un tableau d'objets : ajouter, modifier un champ par `id`, supprimer par `id`, sans muter l'original.

**Exercice 8.6.3**

Écrivez un tri multi-critères (catégorie croissante puis prix décroissant puis nom croissant). Utilisez `localeCompare` pour les textes.

**Exercice 8.6.4**

Écrivez `indexerPar(tableau, cle)` qui transforme un tableau d'objets en objet (ou `Map`) indexé par une propriété, en O(n), pour accélérer des recherches répétées.

## 8.7 Bonnes pratiques

**Exercice 8.7.1**

Listez cinq bonnes pratiques sur les tableaux (méthodes non mutantes, éviter `for...in`, `includes` plutôt que `indexOf`, ne pas créer de tableaux creux, vérifier `Array.isArray`) et illustrez chacune.

**Exercice 8.7.2**

Mesurez le temps de recherche d'un élément avec `includes` dans un tableau de 10⁵ éléments et dans un `Set` de même taille.

---

# 9. Objets, `Map` et `Set`

## 9.1 Les objets

**Exercice 9.1.1**

Créez un objet `voiture` avec des propriétés (`marque`, `annee`), une méthode (`demarrer()`) et un objet imbriqué (`moteur`). Lisez les propriétés avec la notation pointée et la notation crochets. Quand la notation crochets est-elle obligatoire ?

**Exercice 9.1.2**

Ajoutez, modifiez et supprimez des propriétés (`delete`). Testez l'existence d'une propriété avec `in`, `hasOwn`, `!== undefined`. Que se passe-t-il à la lecture d'une propriété absente ?

**Exercice 9.1.3**

Écrivez une fonction qui reçoit un objet et renvoie une version sans les propriétés `null` ou `undefined`, sans muter l'original.

### Propriétés calculées et raccourcis

**Exercice 9.1.4**

Créez un objet avec une clé calculée (`[prefixe + "Nom"]: ...`), des raccourcis de propriétés (`{ nom, age }`) et de méthodes (`saluer() {}`). Écrivez `creerObjet(cle, valeur)` qui renvoie `{ [cle]: valeur }`.

**Exercice 9.1.5**

Définissez des accesseurs (`get` / `set`) dans un objet littéral pour une propriété calculée `nomComplet` à partir de `prenom` et `nom`. Que se passe-t-il à l'affectation si le `set` est absent ?

### Méthodes utilitaires de `Object`

**Exercice 9.1.6**

Utilisez `Object.keys`, `values`, `entries`, `fromEntries`, `assign`, `freeze`, `isFrozen`, `seal`, `defineProperty`, `getOwnPropertyNames`, `getPrototypeOf` sur un objet de votre choix.

**Exercice 9.1.7**

Écrivez `mapperValeurs(obj, fn)`, `filtrerCles(obj, predicat)`, `inverser(obj)` (clés et valeurs échangées), `choisir(obj, cles)` (`pick`), `omettre(obj, cles)` (`omit`) avec `Object.entries` et `Object.fromEntries`.

**Exercice 9.1.8**

Quelle différence entre `Object.freeze` (superficiel) et un gel profond ? Écrivez `geleProfond(obj)` récursif. Que se passe-t-il à l'écriture sur un objet gelé en mode strict et non strict ?

**Exercice 9.1.9**

Avec `Object.defineProperty`, créez une propriété non énumérable, non modifiable, puis un accesseur. Quels sont les trois attributs d'un descripteur de données ?

### Décomposition d'objet

**Exercice 9.1.10**

Écrivez une fonction `creerUtilisateur({ nom, age = 18, ...autres })` avec décomposition et valeurs par défaut. Utilisez `...autres` pour copier le reste des propriétés dans le résultat.

**Exercice 9.1.11**

Fusionnez deux objets avec spread (`{ ...a, ...b }`) et `Object.assign`. Qui l'emporte en cas de conflit ? Écrivez une fusion profonde récursive.

### Itération

**Exercice 9.1.12**

Parcourez un objet avec `for...in` (avec `hasOwn`), `Object.keys().forEach`, `for (const [k, v] of Object.entries(obj))`. Dans quel ordre les clés sont-elles parcourues (entiers croissants puis chaînes dans l'ordre d'insertion) ? Vérifiez avec `{ b: 1, 2: 1, a: 1, 1: 1 }`.

### Pièges des objets-dictionnaires

**Exercice 9.1.13**

Pourquoi `{}["constructor"]` ou `{}["toString"]` ne sont-ils pas `undefined` ? Comment créer un dictionnaire sans prototype (`Object.create(null)`) ? Écrivez un compteur de mots qui échoue avec un mot « constructor ».

**Exercice 9.1.14**

Quels risques présentent les clés `__proto__` (pollution de prototype) lors de la fusion d'objets venant d'une source non fiable ? Écrivez un exemple et une parade.

## 9.2 `Map` : un vrai dictionnaire

**Exercice 9.2.1**

Créez une `Map`, ajoutez des paires (`set`), lisez (`get`), testez (`has`), supprimez (`delete`), comptez (`size`), parcourez (`for...of`, `forEach`, `keys`, `values`, `entries`). Utilisez des clés de types différents (objet, fonction, nombre, `NaN`).

**Exercice 9.2.2**

Convertissez un objet en `Map` (`new Map(Object.entries(obj))`) et une `Map` en objet (`Object.fromEntries(map)`). Que se passe-t-il pour les clés non chaînes lors de la conversion en objet ?

**Exercice 9.2.3**

Écrivez un compteur de fréquences de caractères avec `Map`, puis un cache avec limite de taille (LRU simple en utilisant l'ordre d'insertion de la `Map`).

**Exercice 9.2.4**

Utilisez `Map.prototype.getOrInsert` et `getOrInsertComputed` pour simplifier un regroupement. Comparez avec le motif `if (!map.has(k)) map.set(k, []); map.get(k).push(v)`. *(ES2026)*

### `Map` ou objet ?

**Exercice 9.2.5**

Complétez le tableau comparatif `Map` / objet (types de clés, ordre, taille, itération, sérialisation JSON, performances pour les ajouts/suppressions fréquents, prototype).

**Exercice 9.2.6**

Pour chaque besoin, choisissez `Map` ou objet : configuration fixe, dictionnaire dynamique avec beaucoup d'ajouts, clés qui sont des objets DOM, données à sérialiser en JSON, compteur de mots.

## 9.3 `Set` : des valeurs uniques

**Exercice 9.3.1**

Créez un `Set` à partir d'un tableau avec doublons, ajoutez (`add`), testez (`has`), supprimez (`delete`), videz (`clear`), parcourez. Comment convertir en tableau ? Comment `Set` compare-t-il `NaN`, `0` et `-0` ?

**Exercice 9.3.2**

Que se passe-t-il quand on ajoute deux objets littéraux identiques dans un `Set` ? Comment obtenir un ensemble d'objets uniques par une propriété ?

**Exercice 9.3.3**

Écrivez `aDesDoublons(tableau)`, `premierDoublon(tableau)`, `lettresCommunes(a, b)`, `estPangramme(texte)` avec des `Set`.

### Opérations ensemblistes *(ES2025, à jour)*

**Exercice 9.3.4**

Avec `a = new Set([1, 2, 3, 4])` et `b = new Set([3, 4, 5, 6])`, calculez `union`, `intersection`, `difference`, `symmetricDifference`, `isSubsetOf`, `isSupersetOf`, `isDisjointFrom`. *(ES2025)*

**Exercice 9.3.5**

Écrivez les mêmes opérations avec la méthode « ancienne » (spread, `filter`, `has`) pour un environnement qui ne supporte pas ES2025.

## 9.4 `WeakMap` et `WeakSet` *(ajout)*

**Exercice 9.4.1**

Quelle est la particularité des références faibles ? Pourquoi les clés d'une `WeakMap` doivent-elles être des objets (ou des symboles non enregistrés) ? Pourquoi une `WeakMap` n'est-elle pas itérable et n'a-t-elle pas de `size` ?

**Exercice 9.4.2**

Utilisez une `WeakMap` pour associer des données privées à des objets sans les modifier ni provoquer de fuite mémoire. Écrivez un cache de résultats de calcul indexé par objet.

**Exercice 9.4.3**

Utilisez un `WeakSet` pour marquer des éléments DOM déjà traités. Que se passe-t-il quand l'élément est supprimé de la page et n'a plus d'autres références ?

**Exercice 9.4.4**

Que font `WeakRef` et `FinalizationRegistry` ? Pourquoi sont-ils déconseillés pour le code d'application courant ?

## 9.5 Choisir la bonne structure

**Exercice 9.5.1**

Pour chacun des besoins suivants, choisissez la structure (tableau, objet, `Map`, `Set`, `WeakMap`, `WeakSet`) et justifiez : liste ordonnée avec doublons, inventaire par identifiant, ensemble de visiteurs uniques, cache lié à des éléments DOM, comptage de mots, file d'attente, annuaire clé / valeur dynamique.

**Exercice 9.5.2**

Écrivez un petit programme qui analyse un texte et utilise un `Set` (mots uniques), une `Map` (fréquences), un tableau (tri) et un objet (résultat final sérialisé en JSON).

---

# 10. `globalThis`

## 10.1 Pourquoi `globalThis` ?

**Exercice 10.1.1**

Quel est l'objet global dans un navigateur (`window`), dans un worker (`self`), dans Node.js (`global`) ? Pourquoi `globalThis` a-t-il été introduit (ES2020) ? Écrivez un code qui affiche `globalThis === window` dans un navigateur et `globalThis === global` dans Node.js.

**Exercice 10.1.2**

Écrivez une fonction `environnement()` qui renvoie `"navigateur"`, `"worker"`, `"node"` ou `"inconnu"` en testant la présence de `window`, `self`, `process` ou `WorkerGlobalScope`, sans lever d'erreur de référence.

**Exercice 10.1.3**

Listez quelques propriétés de l'objet global et indiquez dans quel environnement elles existent : `document`, `localStorage`, `fetch`, `setTimeout`, `process`, `require`, `__dirname`, `structuredClone`, `crypto`, `navigator`.

## 10.2 Cas d'usage

**Exercice 10.2.1**

Écrivez une fonction utilitaire qui détecte la disponibilité d'une API (`typeof globalThis.fetch === "function"`, `"IntersectionObserver" in globalThis`) et propose un repli.

**Exercice 10.2.2**

Écrivez un « polyfill » minimal pour `Array.prototype.at` qui ne s'installe que si la méthode est absente. Pourquoi ne faut-il pas écraser une méthode native existante ?

**Exercice 10.2.3**

Créez une propriété globale partagée entre scripts avec `globalThis.CONFIG = {...}`. Quels sont les inconvénients (collisions, dépendances cachées) et quelles alternatives (modules, injection) ?

## 10.3 Pièges

**Exercice 10.3.1**

Que se passe-t-il à l'affectation sans déclaration en mode non strict (`variableMagique = 1`) ? Comment l'empêcher (`"use strict"`, modules) ? Quelle est la valeur de `this` dans une fonction ordinaire appelée seule, en mode strict et non strict ?

**Exercice 10.3.2**

Pourquoi les variables déclarées avec `let` et `const` au niveau supérieur ne deviennent-elles pas des propriétés de `globalThis` ? Vérifiez avec `var`, `let`, `const`, `function` dans un script classique du navigateur.

**Exercice 10.3.3**

Quels risques de sécurité et de maintenance présente la pollution de l'espace global ? Citez trois bonnes pratiques pour l'éviter.

---

# 11. Expressions régulières

## 11.1 Créer une expression régulière

**Exercice 11.1.1**

Créez la même expression régulière avec un littéral (`/ab+c/i`) et avec le constructeur (`new RegExp("ab+c", "i")`). Quand le constructeur est-il nécessaire (motif dynamique) ? Pourquoi faut-il doubler les barres obliques inverses dans la chaîne ?

**Exercice 11.1.2**

Écrivez une fonction `echapperRegex(texte)` qui échappe les caractères spéciaux d'une chaîne pour l'utiliser dans une expression régulière. Comparez avec `RegExp.escape`. *(ES2025)*

**Exercice 11.1.3**

Construisez dynamiquement une expression régulière qui reconnaît n'importe quel mot d'une liste fournie par l'utilisateur, sans risque d'injection.

## 11.2 Méthodes

**Exercice 11.2.1**

Utilisez `test`, `exec`, `match`, `matchAll`, `replace`, `replaceAll`, `search`, `split` sur un même texte et notez le type de retour de chacune.

**Exercice 11.2.2**

Pourquoi une expression régulière avec le drapeau `g` et la méthode `test` donne-t-elle des résultats surprenants en cas d'appels successifs (propriété `lastIndex`) ? Montrez-le et corrigez.

**Exercice 11.2.3**

Utilisez `replace` avec une fonction de rappel pour mettre en majuscules la première lettre de chaque mot, et avec une chaîne de remplacement (`$1`, `$<nom>`, `$&`).

**Exercice 11.2.4**

Écrivez `split` avec une expression régulière pour découper selon des séparateurs multiples (virgule, point-virgule, espaces) et conserver ou non les séparateurs (groupe de capture).

## 11.3 Syntaxe courante

**Exercice 11.3.1**

Pour chaque élément de syntaxe, écrivez un exemple de correspondance et de non-correspondance : `.`, `\d`, `\w`, `\s`, `\b`, `^`, `$`, `[abc]`, `[^abc]`, `[a-z]`, `a|b`, `*`, `+`, `?`, `{2,4}`, `*?` (paresseux), `(?=...)`, `(?!...)`, `(?<=...)`, `(?<!...)`.

**Exercice 11.3.2**

Écrivez les expressions régulières pour : un code postal français (5 chiffres), un numéro de téléphone français (`06 12 34 56 78`, `+33 6 12 34 56 78`), une date `JJ/MM/AAAA`, une couleur hexadécimale (`#fff`, `#a1b2c3`), un identifiant JavaScript valide.

**Exercice 11.3.3**

Quelle différence entre un quantificateur gourmand (`.*`) et paresseux (`.*?`) ? Extrayez les balises d'un texte HTML simple avec les deux variantes.

**Exercice 11.3.4**

Qu'est-ce que le « retour sur trace catastrophique » (*ReDoS*) ? Donnez un exemple d'expression régulière dangereuse (`(a+)+$`) et un texte qui la fait ralentir. Comment s'en prémunir ?

## 11.4 Drapeaux (*flags*)

**Exercice 11.4.1**

Décrivez l'effet de chaque drapeau : `g`, `i`, `m`, `s`, `u`, `v`, `y`, `d`. Écrivez un exemple pour chacun.

**Exercice 11.4.2**

Utilisez le drapeau `u` et les classes de propriétés Unicode (`\p{L}`, `\p{Emoji}`, `\p{Script=Greek}`) pour reconnaître des lettres de tous les alphabets. Pourquoi `\w` ne suffit-il pas pour des lettres accentuées ?

**Exercice 11.4.3**

Utilisez le drapeau `v` pour des opérations ensemblistes dans une classe de caractères (`[\p{L}--[a-z]]`). Quel est l'avantage par rapport à `u` ? *(ES2024)*

**Exercice 11.4.4**

Utilisez le drapeau `d` pour obtenir les indices des groupes (`match.indices`). À quoi cela sert-il (coloration syntaxique, édition de texte) ?

## 11.5 Groupes de capture

**Exercice 11.5.1**

Extrayez l'année, le mois et le jour d'une date `2026-10-21` avec des groupes numérotés, puis avec des groupes nommés (`(?<annee>\d{4})`). Utilisez la décomposition de `match.groups`.

**Exercice 11.5.2**

Utilisez une référence arrière (`\1`, `\k<nom>`) pour détecter des mots répétés (`"le le chat"`) et des guillemets appariés.

**Exercice 11.5.3**

Écrivez un groupe non capturant `(?:...)` et expliquez son intérêt. Réécrivez une expression pour qu'elle ne produise que les groupes utiles.

**Exercice 11.5.4**

Utilisez les groupes nommés dupliqués dans des alternatives (`(?<annee>\d{4})-|(?<annee>\d{2})/`) et les modificateurs de motif `(?i:...)`. *(ES2025)*

## 11.6 Exemples utiles

**Exercice 11.6.1**

Écrivez des fonctions de validation : adresse électronique simple, URL, mot de passe fort (8 caractères, majuscule, minuscule, chiffre, symbole avec des assertions positives avancées), nom d'utilisateur (lettres, chiffres, tiret bas, 3 à 16 caractères).

**Exercice 11.6.2**

Écrivez `extraireHashtags(texte)`, `extraireNombres(texte)`, `normaliserEspaces(texte)`, `camelVersSnake(texte)`, `snakeVersCamel(texte)`, `masquerCarte(numero)` (n'afficher que les 4 derniers chiffres).

**Exercice 11.6.3**

Écrivez un petit analyseur de journaux : pour des lignes `2026-10-21 14:03:05 [ERROR] Message`, extrayez la date, l'heure, le niveau et le message avec des groupes nommés, et comptez le nombre d'erreurs par niveau.

**Exercice 11.6.4**

Écrivez un mini moteur de gabarit qui remplace `{{ nom }}` par la valeur correspondante d'un objet (avec `replace` et une fonction).

## 11.7 Bonnes pratiques

**Exercice 11.7.1**

Listez cinq bonnes pratiques sur les expressions régulières (les nommer et les commenter, groupes nommés, ne pas parser du HTML avec une regex, tester avec des cas limites, prévenir le ReDoS) et illustrez chacune.

**Exercice 11.7.2**

Utilisez un outil en ligne (par exemple regex101) pour mettre au point et expliquer l'expression d'un exercice précédent. Notez les cas limites que l'outil vous fait découvrir.

---

# 12. Fonctions, portée et fermetures

## 12.1 Déclarer une fonction

**Exercice 12.1.1**

Écrivez `addition(a, b)` de quatre façons : déclaration de fonction, expression de fonction, fonction fléchée avec bloc, fonction fléchée à retour implicite. Quelles sont les différences de hoisting ?

**Exercice 12.1.2**

Écrivez des fonctions fléchées qui renvoient un objet littéral (`() => ({ x: 1 })`). Pourquoi les parenthèses sont-elles nécessaires ?

**Exercice 12.1.3**

Quelle différence de comportement entre une fonction anonyme, nommée et fléchée dans les traces de pile (`fn.name`) ? Que vaut `(function () {}).name` ? `(() => {}).name` ? `const f = () => {}; f.name` ?

### Fonctions fléchées vs classiques

**Exercice 12.1.4**

Complétez le tableau comparatif fonction classique / fonction fléchée : `this`, `arguments`, `new`, `prototype`, hoisting, constructeur, méthodes d'objet.

**Exercice 12.1.5**

Prédisez la sortie, puis expliquez :

```js
const obj = {
    nom: "Alice",
    classique() { return this.nom; },
    flechee: () => typeof this,
    differee() { return [1].map(() => this.nom); },
};
console.log(obj.classique(), obj.flechee(), obj.differee());
const f = obj.classique;
try { console.log(f()); } catch (e) { console.log(e.name); }
```

## 12.2 Paramètres et arguments

**Exercice 12.2.1**

Écrivez `saluer(nom = "inconnu", titre = "M.")`. Appelez-la avec `saluer()`, `saluer("Alice")`, `saluer(undefined, "Mme")`, `saluer(null)`. Quelle différence entre `undefined` et `null` pour les valeurs par défaut ?

**Exercice 12.2.2**

Écrivez `somme(...nombres)` et `moyenne(...nombres)` avec paramètre rest. Que contient `arguments` dans une fonction classique et dans une fonction fléchée ?

**Exercice 12.2.3**

Écrivez une fonction avec un objet d'options (`creerBouton({ texte, couleur = "bleu", taille = "m" } = {})`) pour éviter des paramètres positionnels trop nombreux.

**Exercice 12.2.4**

Une valeur par défaut peut utiliser un paramètre précédent ou appeler une fonction (`function f(a, b = a * 2, c = calcul())`). Quand l'expression par défaut est-elle évaluée (à chaque appel) ? Montrez la différence avec Python.

**Exercice 12.2.5**

Que valent `function f(a, b) {}` → `f.length`, et `function g(a, b = 1, ...c) {}` → `g.length` ?

## 12.3 Valeur de retour

**Exercice 12.3.1**

Que renvoie une fonction sans `return` ? Avec `return;` ? Avec `return` suivi d'un saut de ligne puis d'une valeur (piège ASI) ?

**Exercice 12.3.2**

Écrivez une fonction qui renvoie plusieurs valeurs sous forme de tableau, puis sous forme d'objet, et décomposez-les à l'appel. Quand préférer l'objet ?

**Exercice 12.3.3**

Écrivez une fonction qui renvoie une autre fonction (`multiplicateur(n)`) et l'utilise pour créer `double` et `triple`.

## 12.4 Portée lexicale

**Exercice 12.4.1**

Prédisez la sortie, puis expliquez la portée lexicale (statique) :

```js
const x = "global";
function a() { return x; }
function b() {
    const x = "local de b";
    return a();
}
console.log(b());
```

**Exercice 12.4.2**

Dessinez la chaîne des portées (*scope chain*) pour un code à trois niveaux de fonctions imbriquées, et listez les variables accessibles depuis la plus interne.

## 12.5 Fermetures (*closures*)

**Exercice 12.5.1**

Écrivez `creerCompteur()` qui renvoie un objet avec `incrementer()`, `decrementer()`, `valeur()` et dont l'état est privé (inaccessible de l'extérieur).

**Exercice 12.5.2**

Écrivez `once(fn)` (exécute `fn` une seule fois), `memoire(fn)`, `limiter(fn, n)` (n appels maximum) et `compteAppels(fn)` en utilisant des fermetures.

**Exercice 12.5.3**

Écrivez `debounce(fn, delai)` et `throttle(fn, delai)`. Quelle est la différence de comportement ? Dans quels cas d'usage chacune est-elle adaptée (champ de recherche, défilement) ?

**Exercice 12.5.4**

Prédisez, puis expliquez le résultat de la boucle avec `setTimeout` pour `var` et pour `let`. Réécrivez la version `var` avec une IIFE pour obtenir 0, 1, 2.

**Exercice 12.5.5**

Quel est le risque de fuite mémoire d'une fermeture qui capture un gros objet ? Écrivez un exemple et une façon de l'éviter.

**Exercice 12.5.6**

Écrivez une fabrique `creerBanque()` qui encapsule un solde privé, avec `deposer`, `retirer` (refus si solde insuffisant) et `historique()` qui renvoie une copie.

## 12.6 `this`, `call`, `apply`, `bind`

**Exercice 12.6.1**

Prédisez la valeur de `this` dans : une fonction appelée seule, une méthode d'objet, une méthode extraite dans une variable, une fonction fléchée dans une méthode, un gestionnaire d'événement classique, un constructeur appelé avec `new`.

**Exercice 12.6.2**

Utilisez `call`, `apply` et `bind` pour exécuter `function presenter(salut, ponct) { return salut + ", " + this.nom + ponct; }` avec différents contextes. Quelles différences de syntaxe ?

**Exercice 12.6.3**

Écrivez votre propre version de `bind` (`monBind(fn, contexte, ...args)`) et de `call`. *(défi)*

**Exercice 12.6.4**

Pourquoi `[1, 2, 3].map(obj.methode)` perd-il `this` ? Corrigez de trois façons (`bind`, fonction fléchée, second paramètre de `map`).

**Exercice 12.6.5**

Empruntez une méthode de tableau pour un objet « array-like » avec `Array.prototype.map.call` et pour calculer le maximum avec `Math.max.apply`.

## 12.7 Fonctions d'ordre supérieur et composition

**Exercice 12.7.1**

Écrivez `compose(...fns)` (de droite à gauche) et `pipe(...fns)` (de gauche à droite), puis composez `trim`, `toLowerCase`, `slugifier`.

**Exercice 12.7.2**

Écrivez la curryfication : `curry(fn)` qui transforme `f(a, b, c)` en `f(a)(b)(c)` et accepte aussi `f(a, b)(c)`. Utilisez `fn.length`. *(défi)*

**Exercice 12.7.3**

Écrivez `partielle(fn, ...argsFixes)` (application partielle) et utilisez-la pour créer `ajouterTVA` à partir d'une fonction `calculerPrix(taux, prixHT)`.

**Exercice 12.7.4**

Écrivez `parPropriete(cle)` qui renvoie un comparateur pour `sort`, et `negation(predicat)`, `tous(...predicats)`, `unDes(...predicats)`.

## 12.8 Fonctions immédiatement invoquées (IIFE)

**Exercice 12.8.1**

Écrivez une IIFE qui définit une variable privée et expose une API (« motif module »). Pourquoi les IIFE sont-elles moins utiles depuis les modules ES et `let`/`const` ?

**Exercice 12.8.2**

Écrivez une IIFE asynchrone (`(async () => { ... })()`) et expliquez pourquoi elle était nécessaire avant l'`await` de haut niveau.

## 12.9 Récursivité

**Exercice 12.9.1**

Écrivez de manière récursive : `factorielle`, `somme(tableau)`, `puissance(x, n)`, `fibonacci`, `inverser(chaine)`, `estPalindrome`, `pgcd`, `aplatir(tableau)`, `profondeur(objet)`.

**Exercice 12.9.2**

Provoquez une erreur de dépassement de pile (`RangeError: Maximum call stack size exceeded`) puis transformez la récursion en boucle. Quelle est la profondeur maximale typique dans votre environnement ?

**Exercice 12.9.3**

JavaScript optimise-t-il la récursion terminale ? Écrivez une version récursive terminale et une version par « trampoline » qui évite le débordement de pile. *(défi)*

**Exercice 12.9.4**

Écrivez le parcours récursif d'un arbre (objets imbriqués avec `enfants`) : affichage indenté, comptage des nœuds, recherche d'un nœud par identifiant.

**Exercice 12.9.5**

Écrivez la résolution des tours de Hanoï, la génération de toutes les permutations d'un tableau et de tous les sous-ensembles (ensemble des parties).

## 12.10 Mémoïsation *(ajout)*

**Exercice 12.10.1**

Écrivez `memoiser(fn)` avec une `Map` et une clé construite à partir des arguments (`JSON.stringify`). Appliquez-la à un Fibonacci récursif et comparez les temps pour `fib(40)` avec et sans mémoïsation.

**Exercice 12.10.2**

Quelles sont les limites de la mémoïsation (fonctions impures, arguments objets, croissance mémoire) ? Écrivez une variante avec limite de taille.

**Exercice 12.10.3**

Écrivez une mémoïsation par `WeakMap` pour une fonction dont l'argument est un objet. Pourquoi évite-t-elle les fuites mémoire ?

## 12.11 Bonnes pratiques

**Exercice 12.11.1**

Réécrivez cette fonction trop longue en petites fonctions pures, bien nommées :

```js
function traiter(commandes) {
    let total = 0;
    for (let i = 0; i < commandes.length; i++) {
        if (commandes[i].statut === "payee") {
            for (let j = 0; j < commandes[i].lignes.length; j++) {
                total += commandes[i].lignes[j].prix * commandes[i].lignes[j].qte;
            }
        }
    }
    console.log("Total :", total);
    return total;
}
```

**Exercice 12.11.2**

Qu'est-ce qu'une fonction pure ? Classez en pures ou impures : `Math.max`, `Math.random`, `arr.push`, `arr.concat`, `Date.now`, `JSON.parse`, `console.log`, une fonction qui lit une variable globale.

**Exercice 12.11.3**

Listez cinq bonnes pratiques sur les fonctions (petite taille, nom explicite, éviter les effets de bord, paramètres par défaut, retour anticipé) et illustrez chacune.

---

# 13. Itérateurs et générateurs

## 13.1 Le protocole d'itération

**Exercice 13.1.1**

Distinguez itérable (`[Symbol.iterator]()`) et itérateur (`next()`). Écrivez manuellement un itérateur sur un tableau avec `next()` qui renvoie `{ value, done }`.

**Exercice 13.1.2**

Quelles constructions consomment un itérable : `for...of`, spread, décomposition, `Array.from`, `new Set`, `Promise.all` ? Testez-les sur un objet itérable personnalisé.

**Exercice 13.1.3**

Écrivez un objet itérable `intervalle(debut, fin, pas)` avec `[Symbol.iterator]`. Utilisez-le dans `for...of` et le spread.

**Exercice 13.1.4**

Écrivez une classe `ListeChainee` itérable avec `ajouter(valeur)` et `[Symbol.iterator]`. Écrivez une classe `Arbre` dont l'itération parcourt les valeurs en profondeur.

**Exercice 13.1.5**

Quel est le rôle de la méthode optionnelle `return()` d'un itérateur (appelée lors d'un `break`) ? Écrivez un exemple qui libère une ressource.

## 13.2 Générateurs

**Exercice 13.2.1**

Écrivez les générateurs : `compteARebours(n)`, `fibonacci()` (infini), `nombresPremiers()` (infini), `lignes(texte)` (ligne par ligne), `intervalle(debut, fin, pas)`.

**Exercice 13.2.2**

Prédisez la sortie, puis expliquez comment `yield` suspend l'exécution :

```js
function* g() {
    console.log("début");
    const a = yield 1;
    console.log("a =", a);
    const b = yield 2;
    console.log("b =", b);
    return "fin";
}
const it = g();
console.log(it.next("ignoré"));
console.log(it.next("A"));
console.log(it.next("B"));
console.log(it.next());
```

**Exercice 13.2.3**

Utilisez `yield*` pour déléguer à un autre générateur et pour aplatir un tableau imbriqué récursivement. Que vaut la valeur de `yield*` ?

**Exercice 13.2.4**

Utilisez `it.return(valeur)` et `it.throw(erreur)` pour terminer ou interrompre un générateur. Que se passe-t-il pour les blocs `finally` ?

**Exercice 13.2.5**

Écrivez un générateur qui produit des identifiants uniques (`id-1`, `id-2`, …) et un générateur qui parcourt un arbre binaire en ordre infixe.

**Exercice 13.2.6**

Écrivez une fonction `prendre(iterable, n)`, `mapper(iterable, fn)`, `filtrer(iterable, pred)` comme générateurs pour composer un traitement paresseux. Quel est l'avantage face aux méthodes de tableau (mémoire, arrêt anticipé) ?

## 13.3 Assistants d'itérateurs *(ES2025, à jour)*

**Exercice 13.3.1**

Avec un générateur infini `naturels()`, écrivez : les cinq premiers carrés pairs, la somme des dix premiers multiples de 3, le premier nombre divisible par 7 et supérieur à 100. Utilisez `filter`, `map`, `take`, `drop`, `find`, `reduce`, `toArray`. *(ES2025)*

**Exercice 13.3.2**

Utilisez `Iterator.from(...)`, `flatMap`, `some`, `every`, `forEach` sur un itérateur. Quelle différence avec les méthodes de tableau ? *(ES2025)*

**Exercice 13.3.3**

Utilisez `Iterator.concat` pour concaténer trois itérables. *(ES2026)*

**Exercice 13.3.4**

Pourquoi les assistants d'itérateurs sont-ils « paresseux » ? Montrez avec un `console.log` dans `map` que seuls les éléments nécessaires sont traités.

## 13.4 Générateurs asynchrones

**Exercice 13.4.1**

Écrivez `async function* compteur(n)` qui produit une valeur par seconde et consommez-la avec `for await...of`.

**Exercice 13.4.2**

Écrivez un générateur asynchrone qui lit une API paginée (page par page) et produit chaque élément. Arrêtez-vous quand il n'y a plus de pages.

**Exercice 13.4.3**

Utilisez `Array.fromAsync` pour collecter les résultats d'un générateur asynchrone, et lisez un `ReadableStream` avec `for await...of` (ligne par ligne). *(ES2026)*

---

# 14. `eval` et ses alternatives

## 14.1 Qu'est-ce que `eval` ?

**Exercice 14.1.1**

Que fait `eval("2 + 3 * 4")` ? Que renvoie `eval("var x = 5; x * 2")` ? Quelle différence entre `eval` direct et indirect (`(0, eval)("...")`) pour la portée ?

**Exercice 14.1.2**

Que fait le constructeur `new Function("a", "b", "return a + b")` ? Quelle différence de portée avec `eval` ?

## 14.2 Pourquoi l'éviter ?

**Exercice 14.2.1**

Citez quatre raisons d'éviter `eval` : sécurité (injection de code), performance (désoptimisation), débogage, politique de sécurité du contenu (CSP). Écrivez un exemple d'injection (`eval("alert(" + saisie + ")")`) et expliquez la faille.

**Exercice 14.2.2**

Comment une politique de sécurité du contenu (`Content-Security-Policy`) peut-elle bloquer `eval` ? Quelle directive (`unsafe-eval`) l'autorise ?

**Exercice 14.2.3**

Pourquoi le mode strict limite-t-il `eval` (variables non propagées à la portée appelante) ?

## 14.3 Alternatives sûres

**Exercice 14.3.1**

Remplacez `eval` par `JSON.parse` pour lire des données, par `obj[nom]` pour un accès dynamique à une propriété, par un objet de fonctions pour appeler une fonction dont le nom est dynamique.

**Exercice 14.3.2**

Écrivez une petite calculatrice qui évalue `"2 + 3 * (4 - 1)"` sans `eval`, avec un analyseur à descente récursive (jetons, expressions, termes, facteurs). *(défi)*

**Exercice 14.3.3**

Écrivez un moteur de gabarit sûr qui remplace `{{ chemin.vers.valeur }}` par la valeur lue dans un objet, sans exécuter de code.

**Exercice 14.3.4**

Pour exécuter du code utilisateur de façon isolée, quelles solutions existent (iframe `sandbox`, Web Worker, `vm` de Node.js, ShadowRealm) ? Quelles sont leurs limites de sécurité ?

---

# 15. Gestion des erreurs et mode strict

## 15.1 Types d'erreurs

**Exercice 15.1.1**

Provoquez volontairement chacune de ces erreurs et notez le message : `ReferenceError`, `TypeError`, `SyntaxError`, `RangeError`, `URIError`, `EvalError`, `AggregateError`. Quel code les déclenche ?

**Exercice 15.1.2**

Distinguez erreur de syntaxe (détectée avant exécution) et erreur d'exécution. Pourquoi un `try...catch` ne peut-il pas attraper une `SyntaxError` du code qui l'entoure ?

**Exercice 15.1.3**

Quelles propriétés possède un objet `Error` (`name`, `message`, `stack`, `cause`) ? Affichez-les pour une erreur provoquée.

## 15.2 `try` / `catch` / `finally`

**Exercice 15.2.1**

Écrivez `parserJSON(texte)` qui renvoie l'objet ou `null` en cas de `SyntaxError`, en laissant passer les autres erreurs.

**Exercice 15.2.2**

Prédisez la sortie, puis expliquez le rôle de `finally` :

```js
function f() {
    try {
        console.log("try");
        return "retour try";
    } catch (e) {
        console.log("catch");
    } finally {
        console.log("finally");
    }
}
console.log(f());

function g() {
    try { return "a"; } finally { return "b"; }
}
console.log(g());
```

**Exercice 15.2.3**

Utilisez la liaison de `catch` optionnelle (`catch { ... }`) quand l'erreur n'est pas utilisée. Quand est-ce acceptable ?

**Exercice 15.2.4**

Écrivez une fonction qui relance l'erreur dans le `catch` après l'avoir enregistrée, et une qui distingue les types d'erreurs avec `instanceof`.

**Exercice 15.2.5**

Écrivez un `finally` qui libère une ressource (verrou, fichier) même en cas d'erreur. Montrez ensuite la même logique avec `using`. *(voir 19.8)*

## 15.3 Lever et personnaliser des erreurs

**Exercice 15.3.1**

Écrivez `diviser(a, b)` qui lève une `RangeError` si `b` vaut 0, et `validerAge(age)` qui lève un `TypeError` ou une `RangeError` selon le cas. Pourquoi lever des objets `Error` plutôt que des chaînes ?

**Exercice 15.3.2**

Définissez `class ErreurValidation extends Error` avec une propriété `champ`, un `name` personnalisé et une `cause`. Instanciez-la, lancez-la et attrapez-la avec `instanceof`.

**Exercice 15.3.3**

Écrivez une hiérarchie : `ErreurApplication`, `ErreurReseau` (avec `statut`), `ErreurValidation` (avec `champs`). Écrivez un gestionnaire central qui réagit selon le type.

**Exercice 15.3.4**

Utilisez l'option `cause` pour chaîner : capturer une erreur bas niveau (`JSON.parse`) et lever une erreur métier qui la contient. Affichez la chaîne des causes.

**Exercice 15.3.5**

Utilisez `Error.isError(valeur)` pour reconnaître une erreur venant d'un autre contexte (iframe) mieux que `instanceof Error`. *(ES2026)*

**Exercice 15.3.6**

Écrivez une fonction `assert(condition, message)` qui lève une erreur, et utilisez-la pour valider les arguments d'une fonction. Quelle différence avec `console.assert` ?

## 15.4 Erreurs asynchrones

**Exercice 15.4.1**

Pourquoi ce `try...catch` n'attrape-t-il pas l'erreur ? Corrigez de deux façons :

```js
try {
    setTimeout(() => { throw new Error("boum"); }, 0);
} catch (e) {
    console.log("attrapée");
}
```

**Exercice 15.4.2**

Attrapez une erreur dans une chaîne de promesses avec `.catch`, dans une fonction `async` avec `try...catch`. Que se passe-t-il avec une promesse rejetée sans gestionnaire (événement `unhandledrejection` / `process.on("unhandledRejection")`) ?

**Exercice 15.4.3**

Écrivez un gestionnaire global d'erreurs : `window.addEventListener("error", ...)` et `"unhandledrejection"` dans un navigateur, `process.on("uncaughtException")` dans Node.js. Quelles précautions prendre (journalisation puis arrêt propre) ?

**Exercice 15.4.4**

Utilisez `Promise.try` pour traiter de la même façon les erreurs synchrones et asynchrones d'une fonction qui peut être l'une ou l'autre. *(ES2025)*

## 15.5 Mode strict (`"use strict"`)

**Exercice 15.5.1**

Écrivez trois situations qui lèvent une erreur uniquement en mode strict : affectation à une variable non déclarée, écriture sur une propriété non modifiable, suppression d'une variable, noms de paramètres dupliqués, `this` indéfini dans une fonction simple, octal littéral `010`.

**Exercice 15.5.2**

Comment active-t-on le mode strict (directive en tête de fichier, de fonction) ? Quels contextes sont automatiquement en mode strict (modules ES, corps de classe) ?

**Exercice 15.5.3**

Quels avantages offre le mode strict (erreurs silencieuses transformées en exceptions, optimisations) ? Pourquoi la directive globale dans un fichier concaténé est-elle risquée ?

## 15.6 Bonnes pratiques

**Exercice 15.6.1**

Listez cinq bonnes pratiques de gestion des erreurs (ne jamais avaler une erreur, lever des `Error`, ajouter du contexte, traiter au bon niveau, gérer les rejets) et corrigez ces mauvais exemples :

```js
try { traiter(); } catch (e) {}

throw "erreur";

promesse.then(ok);

function lire(c) { try { return JSON.parse(c); } catch (e) { return null; } }
```

**Exercice 15.6.2**

Écrivez une fonction `reessayer(fn, tentatives, delai)` qui relance une opération asynchrone en cas d'échec avec attente exponentielle, et lève une erreur finale avec la liste des causes (`AggregateError`).

---

# 16. JavaScript asynchrone

## 16.1 Synchrone, asynchrone et boucle d'événements

**Exercice 16.1.1**

Prédisez l'ordre d'affichage, puis expliquez (pile d'appels, file des tâches, file des micro-tâches) :

```js
console.log("A");
setTimeout(() => console.log("B"), 0);
Promise.resolve().then(() => console.log("C"));
queueMicrotask(() => console.log("D"));
(async () => { console.log("E"); await null; console.log("F"); })();
console.log("G");
```

**Exercice 16.1.2**

Écrivez un programme qui bloque la boucle d'événements (boucle `while` de 2 secondes) et montrez l'effet sur un `setTimeout` et sur l'interface d'une page. Comment éviter de bloquer (découpage, Web Worker) ?

**Exercice 16.1.3**

Dessinez le schéma de la boucle d'événements : pile, API Web, file de macro-tâches, file de micro-tâches, `requestAnimationFrame`. Où sont placées les promesses résolues ? Les `setTimeout` ? Les événements du DOM ?

## 16.2 Minuteries

**Exercice 16.2.1**

Utilisez `setTimeout` pour afficher un message après 2 secondes et `clearTimeout` pour l'annuler. Utilisez `setInterval` pour compter de 1 à 5 puis `clearInterval`.

**Exercice 16.2.2**

Pourquoi `setTimeout(fn, 0)` n'exécute-t-il pas `fn` immédiatement ? Quel est le délai minimal réel ? Écrivez une fonction `reporter(fn)` qui exécute `fn` après le code courant.

**Exercice 16.2.3**

Écrivez `attendre(ms)` qui renvoie une promesse, et utilisez-la dans une fonction `async` pour afficher un compte à rebours.

**Exercice 16.2.4**

Écrivez un chronomètre avec `setInterval` et `performance.now()`. Pourquoi `setInterval` accumule-t-il une dérive ? Comment la corriger ?

### `setTimeout` récursif vs `setInterval`

**Exercice 16.2.5**

Écrivez un « sondage » (*polling*) qui interroge une fonction toutes les secondes : version `setInterval`, puis version `setTimeout` récursif attendant la fin de l'appel précédent. Pourquoi la seconde est-elle plus sûre pour des appels dont la durée varie ?

**Exercice 16.2.6**

Utilisez `requestAnimationFrame` pour une animation fluide (déplacement d'un élément) et `cancelAnimationFrame` pour l'arrêter. Quelle différence avec `setInterval(…, 16)` ?

## 16.3 *Callbacks* (rappels)

**Exercice 16.3.1**

Écrivez une fonction `lireUtilisateur(id, callback)` qui simule un appel asynchrone avec `setTimeout` et renvoie `(erreur, donnees)` selon la convention Node.js. Appelez-la avec succès et avec erreur.

**Exercice 16.3.2**

Écrivez trois opérations dépendantes l'une de l'autre avec des rappels imbriqués (« enfer des rappels »). Que représente la pyramide ? Réécrivez avec des promesses puis `async`/`await`.

**Exercice 16.3.3**

Convertissez une fonction à rappel en fonction qui renvoie une promesse (`promisifier(fn)`). Utilisez `util.promisify` dans Node.js.

## 16.4 Promesses (`Promise`)

**Exercice 16.4.1**

Écrivez une fonction `diviserAsync(a, b)` qui renvoie une promesse résolue avec le quotient ou rejetée si `b === 0`. Utilisez `then`, `catch`, `finally`.

**Exercice 16.4.2**

Prédisez la sortie, puis expliquez le chaînage et la propagation des erreurs :

```js
Promise.resolve(1)
    .then(x => x + 1)
    .then(x => { throw new Error("oups " + x); })
    .then(x => console.log("jamais", x))
    .catch(e => { console.log(e.message); return "repris"; })
    .then(x => console.log(x))
    .finally(() => console.log("fin"));
```

**Exercice 16.4.3**

Quels sont les trois états d'une promesse (*pending*, *fulfilled*, *rejected*) ? Une promesse peut-elle changer d'état plusieurs fois ? Que se passe-t-il à des appels multiples de `resolve` ?

**Exercice 16.4.4**

Quelle différence entre `return valeur` et `return Promise.resolve(valeur)` dans un `then` ? Que se passe-t-il si l'on oublie le `return` dans un `then` ?

**Exercice 16.4.5**

Utilisez `Promise.resolve`, `Promise.reject` et `Promise.withResolvers` pour créer des promesses et en exposer la résolution à l'extérieur. Écrivez une file d'attente d'événements avec `withResolvers`. *(ES2024)*

**Exercice 16.4.6**

Écrivez votre propre version simplifiée de `Promise` (états, `then`, `catch`) avec les micro-tâches. *(défi)*

## 16.5 `async` / `await`

**Exercice 16.5.1**

Réécrivez avec `async`/`await` la chaîne de promesses de l'exercice 16.4.2. Que renvoie toujours une fonction `async` ?

**Exercice 16.5.2**

Pourquoi l'exécution séquentielle de plusieurs `await` est-elle lente quand les opérations sont indépendantes ? Comparez le temps de trois attentes de 1 seconde, séquentielles et parallèles.

**Exercice 16.5.3**

Écrivez une fonction `async` qui utilise `try...catch...finally` autour d'un `await` et une autre qui renvoie `await` ou `return` d'une promesse (différence dans la pile d'appels et le `try`).

**Exercice 16.5.4**

Utilisez l'`await` de haut niveau dans un module. Quels environnements le supportent ? Que se passe-t-il pour les modules qui importent un module avec `await` de haut niveau ?

**Exercice 16.5.5**

Utilisez `await` dans une boucle `for...of` (traitement séquentiel) et dans `map` + `Promise.all` (traitement parallèle). Quand chaque approche est-elle adaptée ? Pourquoi `forEach(async ...)` est-il un piège ?

**Exercice 16.5.6**

Prédisez l'ordre d'affichage :

```js
async function a() { console.log(1); await b(); console.log(2); }
async function b() { console.log(3); }
a();
console.log(4);
```

## 16.6 Combiner plusieurs opérations

**Exercice 16.6.1**

Comparez `Promise.all`, `Promise.allSettled`, `Promise.race`, `Promise.any` avec trois promesses (une rapide qui réussit, une lente qui réussit, une très rapide qui échoue). Notez le résultat de chacune.

**Exercice 16.6.2**

Chargez en parallèle un utilisateur et ses articles (deux appels simulés) avec `Promise.all`, puis décomposez le résultat. Que se passe-t-il si l'une des deux promesses échoue ?

**Exercice 16.6.3**

Écrivez `avecDelai(promesse, ms)` avec `Promise.race` qui rejette si la promesse met trop de temps. Écrivez `limiterConcurrence(taches, n)` qui exécute au plus `n` tâches en parallèle. *(défi)*

**Exercice 16.6.4**

Écrivez `traiterParLots(elements, tailleLot, fn)` qui traite un grand tableau par lots séquentiels de `Promise.all`.

**Exercice 16.6.5**

Utilisez `Promise.any` pour interroger plusieurs miroirs et prendre la première réponse réussie. Que contient l'`AggregateError` si tous échouent ?

## 16.7 Annulation et délais : `AbortController` *(ajout)*

**Exercice 16.7.1**

Annulez un `fetch` avec `AbortController` et gérez l'erreur `AbortError`. Annulez-le automatiquement après 3 secondes avec `AbortSignal.timeout(3000)`.

**Exercice 16.7.2**

Combinez deux signaux (`AbortSignal.any([a, b])`) : annulation manuelle et délai d'expiration.

**Exercice 16.7.3**

Rendez votre propre fonction asynchrone annulable : elle accepte un `signal`, vérifie `signal.aborted` ou écoute l'événement `abort`, et lève `signal.reason`. Appliquez-la à `attendre(ms, { signal })`.

**Exercice 16.7.4**

Écrivez une recherche « avec anti-rebond » qui annule la requête précédente à chaque nouvelle saisie pour ne jamais afficher une réponse périmée.

## 16.8 Bonnes pratiques

**Exercice 16.8.1**

Listez cinq bonnes pratiques de l'asynchrone (`async`/`await` plutôt que chaînage, paralléliser, toujours gérer les erreurs, annuler, ne pas mélanger rappels et promesses) et corrigez ces exemples :

```js
async function charger() {
    const a = await lireA();
    const b = await lireB();
    return [a, b];
}

items.forEach(async (i) => { await sauvegarder(i); });

new Promise(async (resolve) => { resolve(await x()); });

function f() { return fetch(u).then(r => r.json()); }
```

---

# 17. APIs web, `fetch` et JSON

## 17.1 Qu'est-ce qu'une API ?

**Exercice 17.1.1**

Définissez API, point d'accès (*endpoint*), méthode HTTP, code d'état, en-tête, corps de requête, REST. Associez les méthodes `GET`, `POST`, `PUT`, `PATCH`, `DELETE` à leur rôle usuel.

**Exercice 17.1.2**

Citez les familles de codes d'état (2xx, 3xx, 4xx, 5xx) et donnez la signification de `200`, `201`, `204`, `301`, `304`, `400`, `401`, `403`, `404`, `409`, `429`, `500`, `503`.

**Exercice 17.1.3**

Analysez une réponse d'API publique dans l'onglet « Réseau » des outils de développement : méthode, URL, en-têtes de requête et de réponse, durée, taille.

## 17.2 `fetch`

**Exercice 17.2.1**

Interrogez une API publique JSON (par exemple une API de blagues ou de météo) avec `fetch` et affichez un champ de la réponse. Utilisez `then` puis `async`/`await`.

**Exercice 17.2.2**

Pourquoi `fetch` ne rejette-t-il pas la promesse pour une réponse `404` ou `500` ? Écrivez le test `response.ok` et la levée d'une erreur personnalisée avec le statut.

**Exercice 17.2.3**

Quelles méthodes de lecture du corps existent (`json()`, `text()`, `blob()`, `arrayBuffer()`, `formData()`) ? Pourquoi ne peut-on lire le corps qu'une seule fois ? Comment utiliser `response.clone()` ?

**Exercice 17.2.4**

Lisez les en-têtes d'une réponse (`response.headers.get("content-type")`, itération) et l'état (`status`, `statusText`, `url`, `redirected`).

### Requêtes `POST`, `PUT`, `DELETE`

**Exercice 17.2.5**

Envoyez un objet JSON avec `POST` (en-tête `Content-Type: application/json`, `JSON.stringify`). Envoyez ensuite un formulaire avec `FormData` (sans définir manuellement `Content-Type`). Pourquoi ne faut-il pas définir l'en-tête pour `FormData` ?

**Exercice 17.2.6**

Écrivez des fonctions `creer`, `lire`, `modifier`, `supprimer` pour une API REST de tâches (par exemple JSONPlaceholder) avec `fetch`.

**Exercice 17.2.7**

Envoyez un fichier avec `FormData` et suivez la progression (`XMLHttpRequest` ou flux). Pourquoi `fetch` n'offre-t-il pas directement la progression d'envoi ?

### Paramètres d'URL

**Exercice 17.2.8**

Construisez une URL avec `URL` et `URLSearchParams` (ajout, lecture, suppression de paramètres). Pourquoi est-ce plus sûr que la concaténation de chaînes (encodage des caractères spéciaux) ? Utilisez `encodeURIComponent`.

### Fonction utilitaire réutilisable

**Exercice 17.2.9**

Écrivez `requete(url, options)` qui : ajoute une URL de base, définit les en-têtes JSON, applique un délai d'expiration, vérifie `response.ok`, analyse le JSON et lève une `ErreurHttp` détaillée. Ajoutez une nouvelle tentative automatique pour les erreurs 5xx.

**Exercice 17.2.10**

Écrivez un petit client typé (objet avec méthodes `get`, `post`, `put`, `delete`) basé sur la fonction précédente et ajoutez un intercepteur pour le jeton d'authentification.

### Sécurité et CORS

**Exercice 17.2.11**

Qu'est-ce que la politique de même origine et CORS ? Provoquez une erreur CORS en interrogeant une API qui n'autorise pas votre origine et lisez le message. Quelle est la différence entre une requête « simple » et une requête préliminaire (`OPTIONS`) ?

**Exercice 17.2.12**

Pourquoi ne faut-il jamais mettre de clés secrètes dans le code client ? Où stocker un jeton (cookie `HttpOnly`, mémoire) ? Quelles protections contre XSS et CSRF ? Citez-en deux.

## 17.3 JSON

**Exercice 17.3.1**

Écrivez un objet JSON valide (clés entre guillemets doubles, pas de commentaires, pas de virgule finale). Corrigez ces JSON invalides : `{ nom: "A" }`, `{ 'nom': 'A' }`, `{ "x": undefined }`, `{ "a": 1, }`, `[1, 2, 3,]`.

**Exercice 17.3.2**

Quels types JavaScript sont représentables en JSON ? Quelles valeurs sont perdues ou transformées (`undefined`, fonctions, symboles, `NaN`, `Infinity`, `Date`, `Map`, `Set`, `BigInt`) ? Testez chacune avec `JSON.stringify`.

### `JSON.stringify()` et `JSON.parse()`

**Exercice 17.3.3**

Utilisez `JSON.stringify(objet, null, 2)` pour une sortie indentée, avec un tableau de clés en deuxième paramètre et avec une fonction de remplacement (masquer un mot de passe).

**Exercice 17.3.4**

Utilisez `JSON.parse(texte, reviver)` pour reconvertir des chaînes de date ISO en objets `Date`. Utilisez `toJSON()` pour personnaliser la sérialisation d'une classe.

**Exercice 17.3.5**

Pourquoi la copie via `JSON.parse(JSON.stringify(x))` est-elle limitée ? Que fait `JSON.parse` avec un nombre de plus de 16 chiffres ? Utilisez l'accès au texte source (`context.source` dans le reviver) pour préserver les grands entiers. *(ES2026)*

**Exercice 17.3.6**

Écrivez `jsonStringifySansCycle(objet)` qui gère les références circulaires avec un `WeakSet`. Quelle erreur obtient-on sans cela (`TypeError: Converting circular structure to JSON`) ?

### Gérer les erreurs

**Exercice 17.3.7**

Écrivez `lireJSON(texte)` qui renvoie un résultat ou une erreur claire avec la position du problème. Testez avec un JSON tronqué. Que dit le message d'erreur dans votre environnement ?

### Importer un fichier JSON *(ES2025)*

**Exercice 17.3.8**

Importez un fichier JSON avec `import data from "./donnees.json" with { type: "json" }` et lisez une propriété. Quels environnements le supportent ? Quelle alternative avec `fetch` ? *(ES2025)*

## 17.4 Bonnes pratiques

**Exercice 17.4.1**

Listez cinq bonnes pratiques sur les API (vérifier `response.ok`, gérer le délai d'expiration, valider les données reçues, URL via `URL`, ne pas exposer de secrets) et corrigez ce code :

```js
async function charger(nom) {
    const r = await fetch("https://api.exemple.com/users?nom=" + nom);
    const d = await r.json();
    document.body.innerHTML = "<h1>" + d.titre + "</h1>";
}
```

**Exercice 17.4.2**

Mini-projet : une page de météo ou de recherche qui interroge une API publique, affiche les résultats, gère les états de chargement et d'erreur, annule la requête précédente et met en cache les réponses en mémoire.

---

# 18. Constructeurs, prototypes et héritage

## 18.1 Rappel : les objets

**Exercice 18.1.1**

Créez un objet de trois façons : littéral, `new Object()`, `Object.create(proto)`. Quelle différence de chaîne de prototypes ?

**Exercice 18.1.2**

Quelle est la différence entre une propriété propre et une propriété héritée ? Vérifiez avec `hasOwn`, `in`, `Object.keys`, `for...in`.

## 18.2 Fonctions constructeurs

**Exercice 18.2.1**

Écrivez un constructeur `Personne(nom, age)` avec une méthode `saluer()` définie dans le constructeur, puis instanciez deux personnes avec `new`. La méthode est-elle partagée ou dupliquée ?

**Exercice 18.2.2**

Que se passe-t-il quand on appelle un constructeur sans `new` en mode non strict ? Écrivez la protection `if (!new.target) throw ...`. Que vaut `new.target` ?

**Exercice 18.2.3**

Que renvoie un constructeur qui contient `return` d'un objet ? D'un primitif ? Testez.

### Ce que fait `new`

**Exercice 18.2.4**

Décrivez les quatre étapes de `new` (création d'un objet, liaison du prototype, exécution du constructeur avec `this`, retour de l'objet). Écrivez une fonction `monNew(Constructeur, ...args)` qui les reproduit. *(défi)*

## 18.3 Prototypes et chaîne de prototypes

**Exercice 18.3.1**

Soit `function Chien(nom) { this.nom = nom; }`. Ajoutez une méthode `aboyer` à `Chien.prototype`. Vérifiez : `chien.__proto__ === Chien.prototype`, `Object.getPrototypeOf(chien)`, `chien.constructor`, `Chien.prototype.constructor`.

**Exercice 18.3.2**

Dessinez la chaîne de prototypes de `[]`, `function () {}`, `{}`, `new Chien("Rex")`, `Object.create(null)`. Où s'arrête-t-elle ?

**Exercice 18.3.3**

Que se passe-t-il à la lecture d'une propriété absente de l'objet ? À l'écriture d'une propriété qui existe sur le prototype (propriété masquée) ? Illustrez avec un exemple.

**Exercice 18.3.4**

Pourquoi définir les méthodes sur le prototype est-il plus économe en mémoire que dans le constructeur ? Mesurez avec 100 000 instances.

**Exercice 18.3.5**

Pourquoi faut-il éviter de modifier `Object.prototype` ou les prototypes natifs (`Array.prototype`) ? Écrivez un exemple de problème avec `for...in`.

### Héritage avec les prototypes

**Exercice 18.3.6**

Écrivez `Animal(nom)` avec `manger()` sur son prototype et `Chat(nom)` qui hérite d'`Animal` : appel de `Animal.call(this, nom)`, `Chat.prototype = Object.create(Animal.prototype)`, restauration de `constructor`, méthode `miauler`. Vérifiez avec `instanceof`.

**Exercice 18.3.7**

Appelez une méthode du parent depuis une méthode redéfinie : `Animal.prototype.manger.call(this)`. Comparez avec `super` dans les classes (chapitre 19).

**Exercice 18.3.8**

Quelle est l'erreur de `Chat.prototype = Animal.prototype` ? Montrez comment elle crée un bogue (la modification du prototype enfant affecte le parent).

## 18.4 `Object.create`

**Exercice 18.4.1**

Utilisez `Object.create(proto, descripteurs)` pour créer un objet qui hérite d'un autre. Créez un objet sans prototype (`Object.create(null)`) et expliquez son utilité (dictionnaire).

**Exercice 18.4.2**

Implémentez un héritage entre objets littéraux (modèle OLOO : *objects linking to other objects*) avec `Object.create` et des méthodes d'initialisation.

**Exercice 18.4.3**

Utilisez `Object.setPrototypeOf` et `Object.getPrototypeOf`. Pourquoi `__proto__` et `setPrototypeOf` sont-ils déconseillés pour la performance ?

## 18.5 Constructeurs intégrés

**Exercice 18.5.1**

Quels sont les constructeurs intégrés (`Object`, `Array`, `Function`, `String`, `Number`, `Boolean`, `Date`, `RegExp`, `Error`, `Map`, `Set`, `Promise`, `Symbol`) ? Pourquoi ne faut-il pas utiliser `new String("a")` ou `new Number(5)` ? Montrez la différence avec les primitifs (`typeof`, `===`).

**Exercice 18.5.2**

Comment un primitif accède-t-il à des méthodes (`"abc".toUpperCase()`) ? Décrivez l'objet enveloppe temporaire.

**Exercice 18.5.3**

Étendez un constructeur intégré avec une classe (`class MonTableau extends Array`) et utilisez `map` : quel est le type du résultat ? Pourquoi (`Symbol.species`) ?

## 18.6 Motifs de création

### Fabrique (*factory function*)

**Exercice 18.6.1**

Écrivez une fabrique `creerUtilisateur(nom, role)` qui renvoie un objet avec des méthodes, sans `new` ni `this`. Quels avantages (pas de `this` perdu, composition) ?

### Encapsulation par fermeture

**Exercice 18.6.2**

Écrivez `creerCompte(soldeInitial)` avec un solde privé accessible uniquement via `deposer`, `retirer`, `solde()`. Comparez avec les champs privés `#` des classes.

### Factory vs constructeur

**Exercice 18.6.3**

Complétez un tableau comparatif fabrique / constructeur / classe (`new`, `instanceof`, `this`, mémoire des méthodes, héritage, encapsulation).

**Exercice 18.6.4**

Écrivez le patron Singleton (une seule instance) de deux façons : module (objet littéral), fermeture. Quels sont ses inconvénients (état global, tests) ?

## 18.7 Membres statiques

**Exercice 18.7.1**

Ajoutez une propriété et une méthode statiques à un constructeur (`Personne.compter`, `Personne.depuisJSON`). Pourquoi ne sont-elles pas accessibles depuis les instances ?

**Exercice 18.7.2**

Écrivez `Utilisateur.creerAdmin(nom)` comme méthode de fabrique statique et un compteur d'instances.

## 18.8 Mixins et composition

**Exercice 18.8.1**

Écrivez un mixin `Horodate` sous forme d'objet de méthodes copié avec `Object.assign(Cible.prototype, Horodate)`, puis un mixin sous forme de fonction de classe (`const Journal = Base => class extends Base {...}`).

**Exercice 18.8.2**

Composez deux comportements (`peutVoler`, `peutNager`) pour créer un `Canard`. Comparez à l'héritage multiple impossible en JavaScript.

**Exercice 18.8.3**

Quels sont les pièges des mixins (collisions de noms, ordre d'application, `instanceof`) ? Écrivez un exemple de collision.

## 18.9 Tester le type : `instanceof` et `constructor`

**Exercice 18.9.1**

Utilisez `instanceof`, `constructor.name`, `Object.prototype.toString.call`, `Symbol.toStringTag` pour identifier le type de valeurs variées. Quel est le plus fiable ?

**Exercice 18.9.2**

Que fait `Symbol.hasInstance` ? Écrivez une classe dont `instanceof` accepte tout objet possédant une méthode `lire` (typage structurel).

**Exercice 18.9.3**

Pourquoi `constructor` n'est-il pas fiable (modifiable, perdu par `Object.create(null)`) ? Donnez un exemple.

## 18.10 Usages avancés : `Proxy` et `Reflect` *(ajout)*

**Exercice 18.10.1**

Écrivez un `Proxy` qui journalise chaque lecture et écriture de propriétés d'un objet (`get`, `set`) et utilise `Reflect.get` / `Reflect.set`.

**Exercice 18.10.2**

Écrivez un proxy de validation : refuser d'écrire un `age` négatif ou non numérique, lever une erreur pour une propriété inconnue.

**Exercice 18.10.3**

Écrivez un proxy de « valeurs par défaut » (renvoie `0` pour toute propriété absente) et un proxy qui permet `obj.a.b.c` sans erreur quand une propriété intermédiaire est absente.

**Exercice 18.10.4**

Écrivez un objet réactif minimal : un proxy qui appelle une fonction de rappel à chaque modification (principe de Vue 3). Gérez les objets imbriqués. *(défi)*

**Exercice 18.10.5**

Listez les pièges de `Proxy` (identité `===` entre cible et proxy, champs privés `#`, performances) et les autres traps (`has`, `deleteProperty`, `ownKeys`, `apply`, `construct`).

**Exercice 18.10.6**

À quoi sert `Reflect` ? Comparez `Reflect.has(obj, "x")` et `"x" in obj`, `Reflect.ownKeys` et `Object.keys`.

## 18.11 Déboguer les constructeurs et prototypes

**Exercice 18.11.1**

Inspectez la chaîne de prototypes d'un objet dans la console (`console.dir`, `Object.getPrototypeOf`, développeur). Écrivez une fonction `chaine(obj)` qui renvoie la liste des prototypes jusqu'à `null`.

**Exercice 18.11.2**

Listez les erreurs courantes (oubli de `new`, `this` perdu, méthode redéfinie sur l'instance, prototype partagé mutable) et reproduisez-en trois avec leur correction.

**Exercice 18.11.3**

Quel piège présente un tableau défini sur le prototype (`Chien.prototype.jouets = []`) ? Montrez-le avec deux instances et corrigez.

---

# 19. Classes et programmation orientée objet

## 19.1 Définir une classe

**Exercice 19.1.1**

Écrivez une classe `Rectangle` avec un constructeur, des propriétés `largeur` et `hauteur`, une méthode `aire()`, un accesseur `get perimetre()` et un mutateur `set largeur(v)` qui refuse les valeurs négatives. Instanciez-la et utilisez ses membres.

**Exercice 19.1.2**

Que devient une classe à l'exécution ? Vérifiez `typeof Rectangle`, `Rectangle.prototype.aire`, `Object.getPrototypeOf(new Rectangle(1, 2)) === Rectangle.prototype`. Quelles différences avec un constructeur (pas de hoisting, appel sans `new` interdit, mode strict automatique, méthodes non énumérables) ?

**Exercice 19.1.3**

Écrivez une classe avec des champs publics (`compteur = 0`), des champs fléchés (`gerer = () => {...}`) et une méthode ordinaire. Pourquoi un champ fléché conserve-t-il `this` quand on le passe en rappel ? Quel est son coût (une copie par instance) ?

**Exercice 19.1.4**

Écrivez une classe `Temperature` avec `celsius` stocké et un accesseur `fahrenheit` en lecture/écriture. Que se passe-t-il à l'affectation d'un accesseur sans mutateur ?

**Exercice 19.1.5**

Écrivez une classe avec une méthode `[Symbol.iterator]`, une méthode `toString`, une méthode `toJSON` et `[Symbol.toPrimitive]`. Utilisez-les dans une conversion en chaîne, en nombre et dans la sérialisation JSON.

### Expression de classe

**Exercice 19.1.6**

Écrivez une expression de classe anonyme assignée à une variable, une expression de classe nommée, et une fabrique de classes qui renvoie une classe selon un paramètre. À quoi sert le nom interne d'une expression de classe nommée ?

## 19.2 Héritage : `extends` et `super`

**Exercice 19.2.1**

Écrivez `Animal` (nom, `parler()`) et `Chien extends Animal` qui redéfinit `parler()` et appelle `super.parler()`. Pourquoi faut-il appeler `super()` avant d'utiliser `this` dans le constructeur de la classe fille ?

**Exercice 19.2.2**

Écrivez une hiérarchie `Vehicule` → `Voiture` → `VoitureElectrique` avec des constructeurs qui appellent `super(...)`. Testez avec `instanceof` et affichez la chaîne de prototypes.

**Exercice 19.2.3**

Étendez des classes intégrées : `class MonErreur extends Error`, `class Pile extends Array`, `class MonMap extends Map`. Quelles précautions (`name`, `cause`, `Symbol.species`) ?

**Exercice 19.2.4**

Redéfinissez un accesseur hérité et appelez `super.propriete`. Que se passe-t-il si une classe fille redéfinit seulement le `get` et pas le `set` ?

**Exercice 19.2.5**

Appelez une méthode redéfinie depuis le constructeur parent. Que se passe-t-il si la méthode redéfinie utilise un champ de la classe fille pas encore initialisé ? Expliquez l'ordre d'initialisation.

## 19.3 Membres statiques et héritage

**Exercice 19.3.1**

Écrivez des membres `static` (propriété, méthode, bloc `static {}`) et vérifiez qu'ils sont hérités par les classes filles. Appelez `super.methodeStatique()` depuis une méthode statique de la classe fille.

**Exercice 19.3.2**

Écrivez une méthode de fabrique statique `Utilisateur.depuisJSON(json)` qui renvoie `new this(...)` pour fonctionner avec les sous-classes. Quelle différence avec `new Utilisateur(...)` ?

**Exercice 19.3.3**

Écrivez un compteur d'instances statique privé (`static #compteur`) avec un identifiant incrémenté à chaque création.

## 19.4 Encapsulation

**Exercice 19.4.1**

Écrivez une classe `CompteBancaire` avec un solde privé (`#solde`), des méthodes `deposer`, `retirer`, un accesseur public `solde` et une méthode privée `#journaliser`. Que se passe-t-il quand on accède à `compte.#solde` de l'extérieur (`SyntaxError`) ?

**Exercice 19.4.2**

Comparez trois mécanismes d'encapsulation : champs privés `#`, convention `_nom`, fermetures, `WeakMap`, `Symbol`. Pour chacun : vraie confidentialité, héritage, lisibilité.

**Exercice 19.4.3**

Écrivez `static estCompte(obj) { return #solde in obj; }` (vérification de marque). Pourquoi est-ce plus sûr que `instanceof` ? *(ES2022)*

**Exercice 19.4.4**

Les champs privés sont-ils accessibles aux sous-classes ? Écrivez un exemple avec accès au champ du parent, et la solution avec une méthode protégée par convention.

**Exercice 19.4.5**

Que se passe-t-il avec les champs privés et un `Proxy` ? Écrivez un exemple de `TypeError` et sa solution.

## 19.5 Abstraction

**Exercice 19.5.1**

Écrivez une classe « abstraite » `Forme` dont le constructeur lève une erreur si on l'instancie directement (`new.target === Forme`) et dont `aire()` lève une erreur « non implémentée ». Écrivez `Cercle` et `Carre`.

**Exercice 19.5.2**

Écrivez le patron « méthode gabarit » : une méthode concrète `executer()` qui appelle des étapes (`lire`, `traiter`, `ecrire`) que les sous-classes implémentent.

**Exercice 19.5.3**

Comment simuler une interface en JavaScript (vérification de la présence de méthodes à la construction, duck typing) ? Écrivez `verifierInterface(obj, ["lire", "ecrire"])`.

## 19.6 Polymorphisme et *duck typing*

**Exercice 19.6.1**

Écrivez trois classes (`Canard`, `Robot`, `Chat`) qui ont toutes une méthode `bouger()` sans lien d'héritage et une fonction `deplacer(entites)` qui l'appelle. Quel principe est illustré ?

**Exercice 19.6.2**

Écrivez une fonction `aireTotale(formes)` qui additionne les aires de formes variées par polymorphisme. Que se passe-t-il quand un objet n'a pas la méthode attendue ? Comment le gérer (`?.()`, vérification) ?

**Exercice 19.6.3**

Comparez `instanceof` et le duck typing pour tester le type d'un objet. Quels sont les avantages et risques de chaque approche ?

## 19.7 Méthodes et symboles spéciaux

**Exercice 19.7.1**

Implémentez dans une classe `Vecteur` : `[Symbol.toPrimitive](hint)`, `toString()`, `valueOf()`, `toJSON()`, `[Symbol.iterator]`, `[Symbol.toStringTag]`. Testez dans des opérations (`+`, gabarit, `Number()`, `JSON.stringify`, spread, `Object.prototype.toString`).

**Exercice 19.7.2**

Écrivez une classe `Fraction` avec addition, soustraction, multiplication, division, simplification, comparaison (`compareTo`) et conversion en chaîne. JavaScript n'a pas de surcharge d'opérateurs : comment contourner ?

**Exercice 19.7.3**

Utilisez `Symbol.species`, `Symbol.asyncIterator`, `Symbol.hasInstance`, `Symbol.isConcatSpreadable` sur un exemple chacun.

## 19.8 Gestion explicite des ressources : `using` *(nouveauté)*

**Exercice 19.8.1**

Écrivez une classe `Connexion` avec `[Symbol.dispose]()` qui affiche « fermeture » et utilisez `using conn = new Connexion()` dans un bloc. Dans quel ordre les ressources sont-elles libérées quand plusieurs `using` se suivent, y compris en cas d'exception ?

**Exercice 19.8.2**

Écrivez une ressource asynchrone avec `[Symbol.asyncDispose]()` et `await using`. Comparez avec un `try...finally` équivalent.

**Exercice 19.8.3**

Utilisez `DisposableStack` pour regrouper plusieurs ressources et `AsyncDisposableStack` pour des ressources asynchrones. Vérifiez la disponibilité dans votre environnement.

## 19.9 Classes ou fonctions ? Quand utiliser quoi

**Exercice 19.9.1**

Pour chaque situation, choisissez classe, fabrique, fonctions pures + objets, ou module, et justifiez : modèle avec comportement et identité, utilitaire sans état, composant avec état interne et cycle de vie, service singleton, structure de données de type pile.

**Exercice 19.9.2**

Écrivez la même « pile » avec une classe, une fabrique à fermeture et des fonctions pures sur un tableau. Comparez : lisibilité, encapsulation, performance, testabilité.

## 19.10 Bonnes pratiques

**Exercice 19.10.1**

Listez cinq bonnes pratiques sur les classes (privé par défaut, composition plutôt qu'héritage, petites classes, éviter l'héritage profond, constructeurs simples) et refactorisez une hiérarchie de trois niveaux en composition.

**Exercice 19.10.2**

Mini-projet : un système de gestion de bibliothèque (`Livre`, `Membre`, `Bibliotheque`) avec classes, champs privés, erreurs personnalisées, sérialisation JSON et tests simples avec `console.assert` ou `node:test`.

---

# 20. Modules (`import` / `export`)

## 20.1 Pourquoi des modules ?

**Exercice 20.1.1**

Énumérez les problèmes d'un projet fait de nombreuses balises `<script>` sans modules (pollution de l'espace global, ordre de chargement, dépendances cachées, collisions de noms). Montrez-en un exemple concret avec deux scripts qui définissent la même variable.

**Exercice 20.1.2**

Quels avantages apportent les modules (encapsulation, dépendances explicites, réutilisation, chargement à la demande, analyse statique pour l'élimination du code mort) ? Citez-en trois et illustrez-les.

## 20.2 Activer les modules

**Exercice 20.2.1**

Dans une page web, activez les modules avec `<script type="module" src="main.js">`. Quelles différences avec un script classique (mode strict, portée du module, `defer` implicite, une seule exécution, CORS) ?

**Exercice 20.2.2**

Dans Node.js, activez les modules avec l'extension `.mjs` ou `"type": "module"` dans `package.json`. Que se passe-t-il pour un fichier `.js` sans cette configuration ?

**Exercice 20.2.3**

Pourquoi un fichier HTML ouvert avec le protocole `file://` ne peut-il pas charger un module (CORS) ? Quelle solution (serveur local : `npx serve`, `python -m http.server`) ?

## 20.3 `export`

**Exercice 20.3.1**

Créez un fichier `maths.js` qui exporte : deux fonctions nommées, une constante, une classe, et un export par défaut. Utilisez les deux syntaxes (`export` devant la déclaration et `export { ... }` en fin de fichier).

**Exercice 20.3.2**

Quelle différence entre un export nommé et un export par défaut ? Pourquoi un fichier ne peut-il avoir qu'un seul export par défaut ? Quelle approche privilégient la plupart des guides de style ?

**Exercice 20.3.3**

Réexportez des éléments d'autres modules : `export { x } from "./a.js"`, `export * from "./b.js"`, `export { default as C } from "./c.js"`, `export * as outils from "./d.js"`. Créez un fichier « baril » (`index.js`).

**Exercice 20.3.4**

Quelle différence entre un export de valeur et un export de « liaison vivante » (*live binding*) ? Écrivez un module qui exporte un compteur et une fonction qui l'incrémente, et montrez que l'importateur voit la mise à jour mais ne peut pas la modifier.

## 20.4 `import`

**Exercice 20.4.1**

Importez les éléments de l'exercice 20.3.1 de toutes les façons : nommés, renommés (`as`), par défaut, en bloc (`* as`), les deux à la fois, pour les effets de bord seulement (`import "./init.js"`).

**Exercice 20.4.2**

Pourquoi les imports sont-ils « remontés » (*hoisted*) et exécutés avant le reste du module ? Pourquoi ne peut-on pas écrire un `import` statique dans un bloc `if` ?

**Exercice 20.4.3**

Un module est-il exécuté plusieurs fois s'il est importé par plusieurs autres ? Prouvez avec un `console.log` au niveau supérieur et trois importateurs.

### Import dynamique (chargement à la demande)

**Exercice 20.4.4**

Utilisez `const module = await import("./lourd.js")` pour charger un module au clic sur un bouton. Quel est le type de retour de `import()` ? Quels avantages (division du code, chargement conditionnel selon la langue ou la fonctionnalité) ?

**Exercice 20.4.5**

Écrivez `chargerLangue(code)` qui importe dynamiquement `./langues/${code}.js` et gère l'erreur si le fichier n'existe pas. Quels sont les risques d'un chemin construit à partir d'une entrée utilisateur ?

### Import de JSON et attributs d'import

**Exercice 20.4.6**

Importez un fichier JSON avec `with { type: "json" }` en import statique et en import dynamique (`import("./a.json", { with: { type: "json" } })`). Que se passe-t-il sans l'attribut ? *(ES2025)*

## 20.5 Fonctionnement

**Exercice 20.5.1**

Décrivez les trois phases du chargement d'un module (construction du graphe de dépendances, instanciation des liaisons, évaluation). Que se passe-t-il lors d'une dépendance circulaire (`a.js` importe `b.js` qui importe `a.js`) ? Écrivez un exemple et observez les valeurs.

**Exercice 20.5.2**

Écrivez un exemple de dépendance circulaire qui provoque une `ReferenceError` (accès à une liaison dans la zone morte temporelle) et une façon de la résoudre (extraire du code commun, import dynamique).

**Exercice 20.5.3**

Que signifie `import.meta` ? Affichez `import.meta.url` et utilisez-le pour calculer un chemin relatif au fichier courant (équivalent de `__dirname`).

## 20.6 Modules ES et CommonJS

**Exercice 20.6.1**

Écrivez le même module en CommonJS (`require`, `module.exports`) et en ES (`import`, `export`). Listez les différences : chargement synchrone ou asynchrone, liaisons vivantes ou copies, mode strict, `this` de haut niveau, `__dirname` / `__filename`, extensions de fichier obligatoires.

**Exercice 20.6.2**

Comment importer un module CommonJS depuis un module ES (import par défaut) ? Comment utiliser un module ES depuis CommonJS (`import()` dynamique, ou `require` dans les versions récentes de Node.js) ?

**Exercice 20.6.3**

Utilisez les champs `exports` et `main` du `package.json` pour exposer plusieurs points d'entrée (ESM et CommonJS) d'une petite bibliothèque. Quelle est la condition `"import"` / `"require"` / `"default"` ?

## 20.7 Structure de projet type

**Exercice 20.7.1**

Organisez un petit projet en modules (`src/main.js`, `src/modeles/`, `src/services/`, `src/utils/`, `src/index.js`). Écrivez les fichiers et vérifiez que le graphe d'imports est sans cycle.

**Exercice 20.7.2**

Pourquoi faut-il écrire l'extension (`./utils.js`) dans les imports relatifs du navigateur et de Node.js ESM ? Comment les bundlers assouplissent-ils cette règle ?

**Exercice 20.7.3**

Utilisez une « carte d'import » (`<script type="importmap">`) pour associer un nom abstrait (`"lodash"`) à une URL, et importez-le dans un module du navigateur.

## 20.8 Pièges courants

**Exercice 20.8.1**

Reproduisez et corrigez les erreurs courantes : « Cannot use import statement outside a module », « Unexpected token 'export' », « The requested module does not provide an export named », « Failed to resolve module specifier », « Module not found » (extension oubliée), « require is not defined in ES module scope ».

**Exercice 20.8.2**

Pourquoi l'import d'un fichier `.json` ou `.css` nécessite-t-il un traitement particulier ? Quelles sont les options (attributs d'import, bundler, `fetch`) ?

---

# 21. DOM et événements

> Les exercices de ce chapitre demandent un navigateur ; créez une page `index.html` avec un fichier `script.js` chargé par `<script type="module">` ou avec `defer`.

## 21.1 Qu'est-ce que le DOM ?

**Exercice 21.1.1**

Dessinez l'arbre DOM d'une page simple (`html`, `head`, `body`, un titre, une liste de deux éléments, un paragraphe avec du texte). Quels sont les types de nœuds (document, élément, texte, commentaire, attribut) ?

**Exercice 21.1.2**

Quelle différence entre le HTML source et le DOM (le DOM est modifiable et peut différer du code source : correction automatique du HTML invalide, modifications par JavaScript) ? Affichez dans la console `document.documentElement`, `document.body`, `document.head`, `document.title`.

**Exercice 21.1.3**

Quelle différence entre `Node` et `Element`, `childNodes` et `children`, `firstChild` et `firstElementChild`, `parentNode` et `parentElement`, `nextSibling` et `nextElementSibling` ?

**Exercice 21.1.4**

Parcourez le DOM d'une page de votre choix : écrivez une fonction récursive qui affiche l'arborescence des balises avec indentation.

## 21.2 Sélectionner des éléments

**Exercice 21.2.1**

Utilisez `getElementById`, `getElementsByClassName`, `getElementsByTagName`, `querySelector`, `querySelectorAll` pour sélectionner : un élément par id, tous les `<li>` d'une liste, le premier lien externe, les `<input type="checkbox">` cochés (`:checked`).

**Exercice 21.2.2**

Quelle différence entre une `HTMLCollection` (vivante) et une `NodeList` (statique pour `querySelectorAll`) ? Montrez la différence en ajoutant un élément après la sélection.

**Exercice 21.2.3**

Utilisez `closest`, `matches`, `contains` et les sélecteurs de relation (`>`, `+`, `~`, `:is`, `:has`, `:not`, `:nth-child`). Écrivez trois sélecteurs avancés pour une liste de cartes.

**Exercice 21.2.4**

Pourquoi `querySelector` renvoie-t-il `null` quand rien ne correspond ? Écrivez une fonction `$(selecteur)` qui lève une erreur claire si l'élément est absent.

## 21.3 Lire et modifier le contenu

**Exercice 21.3.1**

Comparez `textContent`, `innerText`, `innerHTML`, `outerHTML` sur un élément contenant du texte caché et des balises. Quand chacun est-il approprié ?

**Exercice 21.3.2**

Pourquoi `innerHTML` avec du contenu fourni par un utilisateur est-il dangereux (XSS) ? Écrivez un exemple d'injection (`<img src=x onerror=alert(1)>`) et trois parades (`textContent`, `createElement`, bibliothèque d'assainissement ou `setHTML` avec l'API Sanitizer).

**Exercice 21.3.3**

Lisez et modifiez des attributs avec `getAttribute`, `setAttribute`, `removeAttribute`, `hasAttribute`, `toggleAttribute`, les propriétés (`el.id`, `el.href`, `el.value`) et `dataset` (`data-*`). Quelle différence entre attribut et propriété (par exemple `value`, `checked`) ?

**Exercice 21.3.4**

Écrivez un compteur de caractères qui met à jour un `<span>` pendant la saisie dans un `<textarea>`.

## 21.4 Créer, insérer et supprimer

**Exercice 21.4.1**

Créez dynamiquement une liste d'éléments à partir d'un tableau avec `createElement`, `append`, `prepend`, `before`, `after`, `replaceWith`, `remove`, `insertAdjacentHTML`, `insertAdjacentElement`.

**Exercice 21.4.2**

Utilisez un `DocumentFragment` ou un `<template>` avec `cloneNode(true)` pour insérer 1000 lignes en une seule opération. Pourquoi est-ce plus rapide que 1000 insertions directes (recalcul de mise en page) ?

**Exercice 21.4.3**

Écrivez `creerCarte({ titre, texte, image })` qui construit un élément `<article>` complet sans utiliser `innerHTML`.

**Exercice 21.4.4**

Écrivez une liste de tâches dynamique : saisie, ajout, suppression, marquage comme fait, compteur de tâches restantes, sans bibliothèque.

**Exercice 21.4.5**

Utilisez `replaceChildren()` pour vider et remplir un conteneur, `cloneNode(true)` pour dupliquer un élément, `isConnected` pour savoir s'il est dans la page.

## 21.5 Classes et styles

**Exercice 21.5.1**

Utilisez `classList.add`, `remove`, `toggle` (avec second paramètre), `contains`, `replace` pour changer l'apparence d'un bouton selon son état. Pourquoi préférer `classList` à `className` ?

**Exercice 21.5.2**

Modifiez des styles en ligne avec `el.style.couleur` / `el.style.setProperty("--ma-variable", "red")`. Lisez le style calculé avec `getComputedStyle`. Quelle différence avec `el.style` ?

**Exercice 21.5.3**

Écrivez un interrupteur de thème clair/sombre qui bascule une classe sur `<html>`, modifie une variable CSS et mémorise le choix dans `localStorage`. Respectez la préférence système (`matchMedia("(prefers-color-scheme: dark)")`).

## 21.6 Dimensions et positionnement

**Exercice 21.6.1**

Quelle différence entre `offsetWidth`, `clientWidth`, `scrollWidth` et `getBoundingClientRect().width` ? Affichez-les pour un élément avec marges, bordures, remplissage et barres de défilement.

**Exercice 21.6.2**

Faites défiler la page jusqu'à un élément avec `scrollIntoView({ behavior: "smooth" })` et lisez `window.scrollY`. Écrivez une fonction qui indique si un élément est visible dans la fenêtre (`getBoundingClientRect`). Quelle API moderne le fait mieux ?

**Exercice 21.6.3**

Écrivez un « retour en haut de page » : un bouton fixé en bas à droite qui apparaît quand `scrollY > 300` et remonte en douceur au clic. Utilisez `throttle` pour limiter les calculs.

## 21.7 Les événements

**Exercice 21.7.1**

Écrivez un bouton qui incrémente un compteur au clic avec `addEventListener`. Pourquoi préférer `addEventListener` à l'attribut `onclick` du HTML et à la propriété `el.onclick` ? Retirez un écouteur avec `removeEventListener` (la fonction doit être nommée).

**Exercice 21.7.2**

Utilisez l'objet événement : `event.type`, `event.target`, `event.currentTarget`, `event.clientX`, `event.key`, `event.preventDefault()`, `event.stopPropagation()`. Quelle différence entre `target` et `currentTarget` ?

**Exercice 21.7.3**

Que vaut `this` dans un gestionnaire d'événement écrit avec une fonction classique ? Avec une fonction fléchée ? Pourquoi `event.currentTarget` est-il plus fiable ?

### Options de `addEventListener`

**Exercice 21.7.4**

Utilisez les options `{ once: true }`, `{ passive: true }`, `{ capture: true }`, `{ signal }`. Retirez plusieurs écouteurs d'un coup avec un `AbortController`.

**Exercice 21.7.5**

À quoi sert `passive: true` pour les événements `touchstart`/`wheel` (performances du défilement) ? Quel effet sur `preventDefault()` ?

### Événements courants

**Exercice 21.7.6**

Écrivez des gestionnaires pour : `click`, `dblclick`, `contextmenu`, `mouseenter`/`mouseleave`, `mousemove`, `keydown`/`keyup`, `input`, `change`, `focus`/`blur`/`focusin`, `submit`, `scroll`, `resize`, `load`, `DOMContentLoaded`, `beforeunload`, `pointerdown`. Pour chacun, notez un cas d'usage.

**Exercice 21.7.7**

Quelle différence entre `input` et `change` ? Entre `mouseenter` et `mouseover` ? Entre `keydown`, `keypress` (obsolète) et `keyup` ? Entre `mousedown`/`mouseup` et `pointerdown`/`pointerup` ?

**Exercice 21.7.8**

Écrivez des raccourcis clavier (`Ctrl + S`, `Échap`, flèches) avec `event.key`, `event.ctrlKey`, `event.metaKey`, `event.code`. Quelle différence entre `key` et `code` ?

**Exercice 21.7.9**

Écrivez un glisser-déposer simple (`dragstart`, `dragover`, `drop`) ou, mieux, un déplacement d'élément avec les événements de pointeur (`pointerdown`, `pointermove`, `pointerup`, `setPointerCapture`). *(défi)*

### Propagation : capture, cible, bulle

**Exercice 21.7.10**

Construisez trois éléments imbriqués avec un écouteur de clic sur chacun, en phase de bulle puis de capture. Prédisez, puis vérifiez, l'ordre d'exécution. Que change `stopPropagation()` ? Que fait `stopImmediatePropagation()` ?

**Exercice 21.7.11**

Quels événements ne remontent pas (`focus`, `blur`, `load`, `mouseenter`) ? Comment les intercepter malgré tout (capture, `focusin`) ?

### Délégation d'événements

**Exercice 21.7.12**

Au lieu d'un écouteur par `<li>`, écrivez un seul écouteur sur le `<ul>` qui identifie l'élément cliqué avec `event.target.closest("li")`. Pourquoi cela fonctionne-t-il pour les éléments ajoutés dynamiquement ?

**Exercice 21.7.13**

Appliquez la délégation à un tableau avec des boutons « modifier » et « supprimer » dans chaque ligne, identifiés par `data-action`. Écrivez une table de correspondance action vers fonction.

### Événements personnalisés

**Exercice 21.7.14**

Créez un `CustomEvent("panier:ajout", { detail: { id: 5 }, bubbles: true })`, émettez-le avec `dispatchEvent` et écoutez-le. Comment passer des données (`detail`) ?

**Exercice 21.7.15**

Écrivez un petit bus d'événements (`on`, `off`, `emit`) basé sur `EventTarget`. Utilisez-le pour faire communiquer deux composants indépendants.

### Formulaires

**Exercice 21.7.16**

Écrivez un formulaire d'inscription (nom, e-mail, mot de passe, case à cocher) et gérez `submit` : `preventDefault()`, lecture avec `FormData`, `Object.fromEntries(new FormData(form))`, affichage des erreurs sous les champs.

**Exercice 21.7.17**

Utilisez l'API de validation native (`required`, `pattern`, `minlength`, `type="email"`, `checkValidity()`, `reportValidity()`, `setCustomValidity()`, `validity`). Écrivez une règle personnalisée (confirmation du mot de passe).

**Exercice 21.7.18**

Écrivez un champ de recherche avec anti-rebond qui filtre une liste en direct, un compteur de caractères et un indicateur de force de mot de passe.

## 21.8 Quand le DOM est-il prêt ?

**Exercice 21.8.1**

Pourquoi un script placé dans `<head>` ne trouve-t-il pas les éléments du `<body>` ? Corrigez avec `defer`, `type="module"`, placement en fin de `<body>`, `DOMContentLoaded`.

**Exercice 21.8.2**

Quelle différence entre `DOMContentLoaded` (DOM construit) et `load` (toutes les ressources chargées) ? Écrivez un code qui affiche `document.readyState` à chaque changement (`readystatechange`).

**Exercice 21.8.3**

Écrivez une fonction `quandPret(fn)` qui exécute `fn` immédiatement si le DOM est déjà prêt, sinon à `DOMContentLoaded`.

## 21.9 Observateurs modernes *(ajout)*

**Exercice 21.9.1**

Utilisez `IntersectionObserver` pour charger des images en différé (`data-src`) et pour déclencher un défilement infini (observer un « sentinelle » en bas de liste).

**Exercice 21.9.2**

Utilisez `ResizeObserver` pour afficher la taille d'un élément redimensionnable et adapter son contenu. Pourquoi est-ce mieux que l'événement `resize` de la fenêtre ?

**Exercice 21.9.3**

Utilisez `MutationObserver` pour réagir à l'ajout d'éléments dans un conteneur et aux changements d'attributs. Quand faut-il appeler `disconnect()` ?

**Exercice 21.9.4**

Écrivez une barre de progression de lecture et un menu qui met en surbrillance la section visible, avec `IntersectionObserver`.

## 21.10 Shadow DOM et composants web

**Exercice 21.10.1**

Créez un élément personnalisé `<ma-carte>` avec `class MaCarte extends HTMLElement`, `customElements.define("ma-carte", MaCarte)`, un Shadow DOM (`attachShadow({ mode: "open" })`) et un style encapsulé. Utilisez-le dans la page.

**Exercice 21.10.2**

Utilisez les méthodes de cycle de vie (`connectedCallback`, `disconnectedCallback`, `attributeChangedCallback`, `static observedAttributes`) pour réagir à un attribut `titre`.

**Exercice 21.10.3**

Utilisez `<slot>` pour accepter du contenu extérieur dans votre composant et `::part` / variables CSS pour le personnaliser depuis l'extérieur. Quelle différence entre `mode: "open"` et `"closed"` ?

**Exercice 21.10.4**

Écrivez un composant `<mon-compteur>` avec un état, des boutons et un événement personnalisé `changement` qui remonte la valeur. Pourquoi l'événement doit-il être `composed: true` pour traverser le Shadow DOM ?

## 21.11 Animations

**Exercice 21.11.1**

Animez un élément avec une transition CSS déclenchée par une classe, puis avec `element.animate([...keyframes], { duration, iterations })` (API Web Animations). Comment attendre la fin (`animation.finished`) ?

**Exercice 21.11.2**

Écrivez une animation avec `requestAnimationFrame` (déplacement d'une balle qui rebondit dans un `<canvas>`) en calculant le temps écoulé entre deux images pour une vitesse indépendante du taux de rafraîchissement.

**Exercice 21.11.3**

Quelles propriétés CSS sont économiques à animer (`transform`, `opacity`) et lesquelles provoquent des recalculs de mise en page (`width`, `top`, `margin`) ? Quel est le rôle de `will-change` ?

**Exercice 21.11.4**

Utilisez les transitions de vue (`document.startViewTransition`) pour animer un changement d'état du DOM. Vérifiez la prise en charge. *(selon les navigateurs)*

## 21.12 Référence : interfaces principales

**Exercice 21.12.1**

Associez chaque interface à son rôle : `EventTarget`, `Node`, `Element`, `HTMLElement`, `Document`, `DocumentFragment`, `Window`, `NodeList`, `HTMLCollection`, `DOMTokenList`, `CSSStyleDeclaration`.

**Exercice 21.12.2**

Pour chaque élément HTML suivant, indiquez l'interface DOM : `<a>`, `<input>`, `<form>`, `<canvas>`, `<img>`, `<select>`, `<dialog>`, `<template>`, `<video>`, `<table>`.

**Exercice 21.12.3**

Utilisez l'élément `<dialog>` : ouverture modale (`showModal()`), fermeture (`close()`), événement `close`, valeur de retour. Écrivez une boîte de confirmation réutilisable qui renvoie une promesse.

## 21.13 Bonnes pratiques

**Exercice 21.13.1**

Listez cinq bonnes pratiques sur le DOM (limiter les accès, fragments, délégation, `textContent` pour les données utilisateur, nettoyer les écouteurs) et corrigez ce code :

```js
const liste = document.getElementById("liste");
for (let i = 0; i < 1000; i++) {
    liste.innerHTML += "<li>" + donnees[i] + "</li>";
}
document.querySelectorAll("li").forEach(li => li.addEventListener("click", () => alert(li.textContent)));
```

**Exercice 21.13.2**

Mini-projet : un quiz interactif (questions chargées depuis un fichier JSON, score, barre de progression, résultats, rejouer), sans bibliothèque, avec délégation d'événements et gestion du clavier.

---

# 22. Environnement du navigateur (BOM) et stockage

## 22.1 Le BOM

**Exercice 22.1.1**

Listez les objets du BOM : `window`, `navigator`, `location`, `history`, `screen`, `document`, `localStorage`, `performance`. Pour chacun, lisez deux propriétés dans la console (`navigator.language`, `screen.width`, `location.href`, `history.length`, `window.innerHeight`).

**Exercice 22.1.2**

Utilisez `location` : lisez `href`, `origin`, `pathname`, `search`, `hash`, `host`. Naviguez avec `location.assign`, `replace` et `reload`. Quelle différence entre `assign` et `replace` pour l'historique ?

**Exercice 22.1.3**

Utilisez l'API `history` : `pushState`, `replaceState`, l'événement `popstate`, `history.back()`, `forward()`, `go()`. Écrivez un mini-routeur côté client qui change le contenu selon `location.pathname` sans recharger la page.

**Exercice 22.1.4**

Utilisez `navigator` : `userAgent`, `language`, `languages`, `onLine`, `clipboard.writeText`, `geolocation.getCurrentPosition`, `share`. Quelles demandent une autorisation ou un contexte sécurisé (HTTPS) ?

**Exercice 22.1.5**

Pourquoi la détection du navigateur par `userAgent` est-elle fragile ? Quelle approche privilégier (détection de fonctionnalités, `"api" in globalThis`, `@supports`, `matchMedia`) ?

**Exercice 22.1.6**

Écrivez un indicateur de connexion qui réagit aux événements `online` et `offline`, et affiche un message quand la connexion tombe.

**Exercice 22.1.7**

Utilisez `matchMedia` pour détecter une largeur d'écran, le mode sombre et la préférence de mouvement réduit (`prefers-reduced-motion`). Réagissez aux changements avec l'événement `change`.

**Exercice 22.1.8**

Mesurez des durées avec `performance.now()`, `performance.mark` / `measure` et affichez les métriques de chargement de la page (`performance.getEntriesByType("navigation")`).

### Boîtes de dialogue

**Exercice 22.1.9**

Utilisez `alert`, `confirm` et `prompt`. Quels sont leurs inconvénients (bloquantes, non personnalisables, parfois supprimées par le navigateur) ? Remplacez `confirm` par un `<dialog>` qui renvoie une promesse.

## 22.2 Comparer les mécanismes de stockage

**Exercice 22.2.1**

Complétez le tableau comparatif : cookies, `localStorage`, `sessionStorage`, IndexedDB, Cache API (capacité, durée de vie, envoi au serveur, accessible depuis JavaScript, synchrone ou asynchrone, portée).

**Exercice 22.2.2**

Pour chaque donnée, choisissez le mécanisme de stockage approprié et justifiez : jeton de session, thème préféré, brouillon d'un formulaire, panier d'un visiteur, grandes données hors ligne, fichiers mis en cache pour une application hors ligne.

## 22.3 Cookies

**Exercice 22.3.1**

Écrivez des fonctions `ecrireCookie(nom, valeur, jours)`, `lireCookie(nom)`, `supprimerCookie(nom)` avec `document.cookie`. Pourquoi faut-il encoder les valeurs ?

**Exercice 22.3.2**

Quels attributs sécurisent un cookie : `Secure`, `HttpOnly`, `SameSite` (`Strict`, `Lax`, `None`), `Path`, `Domain`, `Max-Age`, `Expires` ? Lesquels JavaScript ne peut-il pas lire ou définir ?

**Exercice 22.3.3**

Utilisez l'API `cookieStore` (asynchrone) pour lire et écrire un cookie, si votre navigateur la supporte. Quels avantages sur `document.cookie` ?

**Exercice 22.3.4**

Écrivez un bandeau de consentement aux cookies qui mémorise le choix et n'active les traceurs qu'après acceptation.

## 22.4 `localStorage`

**Exercice 22.4.1**

Utilisez `setItem`, `getItem`, `removeItem`, `clear`, `key`, `length`. Que renvoie `getItem` pour une clé absente ? Que se passe-t-il quand on stocke un objet sans le sérialiser ?

**Exercice 22.4.2**

Écrivez `sauver(cle, valeur)` et `charger(cle, defaut)` qui sérialisent en JSON, gèrent les erreurs (JSON invalide, quota dépassé, stockage désactivé en navigation privée).

**Exercice 22.4.3**

Écrivez un petit module de stockage avec expiration (`sauverAvecExpiration(cle, valeur, ttl)`) et préfixe d'espace de noms.

**Exercice 22.4.4**

Écoutez l'événement `storage` pour synchroniser deux onglets (thème, panier). Pourquoi l'événement ne se déclenche-t-il pas dans l'onglet qui a effectué la modification ?

**Exercice 22.4.5**

Quelles données ne faut-il jamais stocker dans `localStorage` (jetons d'authentification sensibles, mots de passe, données personnelles) ? Expliquez le risque lié au XSS.

**Exercice 22.4.6**

Écrivez une liste de tâches persistante : ajout, suppression, marquage, sauvegarde dans `localStorage` à chaque modification et rechargement au démarrage.

## 22.5 `sessionStorage`

**Exercice 22.5.1**

Utilisez `sessionStorage` pour mémoriser l'étape d'un formulaire en plusieurs pages. Quelle est sa durée de vie ? Est-il partagé entre deux onglets du même site ?

**Exercice 22.5.2**

Écrivez un brouillon automatique d'un formulaire : sauvegarde à la saisie (avec anti-rebond) dans `sessionStorage`, restauration au rechargement, suppression à l'envoi.

## 22.6 Pour aller plus loin

**Exercice 22.6.1**

Utilisez IndexedDB (directement ou avec la petite bibliothèque `idb`) : ouvrir une base, créer un magasin d'objets avec index, ajouter, lire par clé, lire par index, mettre à jour, supprimer. Pourquoi son API est-elle asynchrone ? *(défi)*

**Exercice 22.6.2**

Utilisez la Cache API et un *service worker* pour mettre en cache des ressources et répondre hors ligne. Quelle stratégie (cache d'abord, réseau d'abord, périmé pendant la revalidation) pour chaque type de ressource ? *(défi)*

**Exercice 22.6.3**

Utilisez `navigator.storage.estimate()` et `navigator.storage.persist()` pour connaître le quota disponible et demander un stockage persistant.

---

# 23. Dates et heures : `Date` et `Temporal`

## 23.1 L'objet `Date` (historique)

**Exercice 23.1.1**

Créez des dates de plusieurs façons : `new Date()`, `new Date(0)`, `new Date("2026-10-21")`, `new Date("2026-10-21T14:30:00")`, `new Date(2026, 9, 21)`, `new Date(2026, 9, 21, 14, 30)`. Que vaut le mois `9` ? Pourquoi `new Date("2026-10-21")` (UTC) et `new Date("2026-10-21T00:00:00")` (local) ne donnent-ils pas le même instant ?

**Exercice 23.1.2**

Qu'est-ce que le temps Unix (millisecondes depuis le 1er janvier 1970 UTC) ? Affichez `Date.now()`, `new Date().getTime()`, `+new Date()` et convertissez en date lisible.

### Lire

**Exercice 23.1.3**

Lisez les composantes d'une date avec `getFullYear`, `getMonth`, `getDate`, `getDay`, `getHours`, `getMinutes`, `getSeconds`, `getMilliseconds`, `getTimezoneOffset` et leurs versions UTC. Pourquoi `getDate` donne-t-il le jour du mois et `getDay` le jour de la semaine ?

### Modifier (mutent l'objet)

**Exercice 23.1.4**

Utilisez `setFullYear`, `setMonth`, `setDate`, `setHours`. Ajoutez 45 jours à une date et vérifiez le report automatique des mois. Que renvoie `new Date(2026, 0, 31)` après `setMonth(1)` ? Pourquoi ?

**Exercice 23.1.5**

Écrivez `ajouterJours(date, n)` sans muter l'original, `debutDeJournee(date)`, `finDeMois(date)`, `numeroDeSemaine(date)`, `estWeekEnd(date)`.

### Formater

**Exercice 23.1.6**

Affichez une date avec `toISOString`, `toString`, `toDateString`, `toLocaleDateString`, `toLocaleTimeString`, `toLocaleString` pour `fr-FR` et `en-US` avec des options (`weekday`, `year`, `month`, `day`, `hour`, `timeZone`).

**Exercice 23.1.7**

Utilisez `Intl.DateTimeFormat` et `Intl.RelativeTimeFormat` pour afficher « jeudi 22 octobre 2026 » et « il y a 3 jours ». Écrivez `ilYa(date)` qui choisit l'unité appropriée.

### Différence entre deux dates

**Exercice 23.1.8**

Calculez le nombre de jours entre deux dates avec la différence de timestamps. Pourquoi le résultat peut-il être faux autour d'un changement d'heure (heure d'été) ? Écrivez `joursEntre(a, b)` robuste (en UTC).

**Exercice 23.1.9**

Calculez l'âge exact d'une personne (en années, mois, jours) à partir de sa date de naissance, et le nombre de jours avant son prochain anniversaire.

### Défauts de `Date`

**Exercice 23.1.10**

Listez les défauts de `Date` (mutable, mois indexés à partir de 0, analyse ambiguë des chaînes, fuseaux horaires limités à UTC et local, pas de calendriers non grégoriens, arithmétique manuelle) et illustrez-en trois par un code surprenant.

**Exercice 23.1.11**

Testez des dates invalides : `new Date("n'importe quoi")`, `new Date(NaN)`, `new Date(2026, 1, 31)`. Écrivez `dateValide(date)` avec `Number.isNaN(date.getTime())`.

## 23.2 `Temporal` : le remplaçant moderne *(à jour)*

> Vérifiez la prise en charge de `Temporal` dans votre navigateur ou installez le polyfill `@js-temporal/polyfill`.

**Exercice 23.2.1**

Créez des objets `Temporal.PlainDate`, `PlainTime`, `PlainDateTime`, `ZonedDateTime`, `Instant`, `Duration` à partir de littéraux et de chaînes ISO. Pour chacun, indiquez à quoi il sert et quand le choisir.

**Exercice 23.2.2**

Obtenez la date du jour, l'heure actuelle et l'instant présent avec `Temporal.Now`. Calculez le nombre de jours jusqu'au prochain 1er janvier avec `until()`.

**Exercice 23.2.3**

Ajoutez 1 mois, 15 jours et 3 heures à des objets `Temporal` avec `add()` et `subtract()`. Montrez qu'ils sont immuables (l'original ne change pas). Quelle est la valeur de `PlainDate.from("2026-01-31").add({ months: 1 })` ?

**Exercice 23.2.4**

Convertissez une réunion de `14:30` à Antananarivo en heure de Paris, de New York et de Tokyo avec `ZonedDateTime` et `withTimeZone`. Gérez le changement d'heure (heure d'été) avec une date avant et après le passage.

**Exercice 23.2.5**

Comparez deux dates avec `Temporal.PlainDate.compare` et `equals`. Triez un tableau de dates avec `Temporal.PlainDate.compare` comme comparateur.

**Exercice 23.2.6**

Utilisez `Temporal.Duration` : créer, additionner, arrondir (`round`), convertir en total d'heures (`total({ unit: "hours" })`). Calculez la durée entre deux `ZonedDateTime`.

**Exercice 23.2.7**

Utilisez `PlainYearMonth` et `PlainMonthDay` pour représenter un mois de facturation et un anniversaire. Écrivez une fonction qui renvoie le prochain anniversaire à partir d'un `PlainMonthDay`.

**Exercice 23.2.8**

Formatez des objets `Temporal` avec `toLocaleString` (`dateStyle`, `timeStyle`, `timeZoneName`) et `toString()` (ISO 8601). Quelle différence avec `Date` ?

**Exercice 23.2.9**

Écrivez un calendrier mensuel (grille de semaines commençant le lundi) avec `Temporal.PlainDate`, `daysInMonth`, `dayOfWeek`. Comparez avec la version `Date` : lisibilité, nombre de pièges. *(défi)*

**Exercice 23.2.10**

Utilisez d'autres calendriers (`withCalendar("japanese")`, `"hebrew"`, `"islamic"`). Quel est l'intérêt de la prise en charge native des calendriers non grégoriens ?

### `Date` → `Temporal`

**Exercice 23.2.11**

Convertissez une `Date` existante en `Temporal.Instant` (`toTemporalInstant()`), puis en `ZonedDateTime`, et inversement un `Instant` en `Date`. Écrivez une fonction de migration qui accepte les deux types.

**Exercice 23.2.12**

Migrez ce code écrit avec `Date` vers `Temporal`, en corrigeant ses défauts :

```js
function joursAvant(noel) {
    const maintenant = new Date();
    const cible = new Date(maintenant.getFullYear(), 11, 25);
    if (cible < maintenant) cible.setFullYear(cible.getFullYear() + 1);
    return Math.ceil((cible - maintenant) / (1000 * 60 * 60 * 24));
}
```

**Exercice 23.2.13**

Quelle règle de bon sens appliquez-vous pour stocker et échanger des dates (ISO 8601, UTC) et pour les afficher (heure locale, au dernier moment) ? Écrivez une paire de fonctions `versStockage(date)` et `versAffichage(chaine, fuseau, langue)`.

---

# 24. Outils et écosystème

## 24.1 Node.js et gestionnaires de paquets

**Exercice 24.1.1**

Installez Node.js (via `nvm`, `fnm`, `volta` ou le site officiel). Vérifiez `node -v`, `npm -v`. Pourquoi utiliser un gestionnaire de versions plutôt qu'une installation unique ?

**Exercice 24.1.2**

Créez un projet : `npm init -y`, installez une dépendance (`npm install dayjs`) et une dépendance de développement (`npm install -D vitest`), ajoutez des scripts (`start`, `test`, `lint`). Examinez `package.json`, `package-lock.json`, `node_modules`. Que signifient `^1.2.3` et `~1.2.3` ?

**Exercice 24.1.3**

Comparez `npm`, `pnpm`, `yarn`, `bun` : vitesse, espace disque, fichier de verrouillage, gestion des espaces de travail. Installez le même projet avec deux gestionnaires et comparez le temps et la taille de `node_modules`.

**Exercice 24.1.4**

Que fait `npx` ? Exécutez un outil sans l'installer globalement (`npx cowsay`). Pourquoi éviter les installations globales ?

**Exercice 24.1.5**

Écrivez un script Node.js qui lit un fichier, utilise les arguments de la ligne de commande et affiche le résultat, avec `node:fs/promises` et `node:path`. Utilisez le préfixe `node:` pour les modules intégrés. Pourquoi est-il recommandé ?

**Exercice 24.1.6**

Utilisez le lanceur de tests natif de Node.js (`node --test`) avec `node:test` et `node:assert` pour tester une fonction.

**Exercice 24.1.7**

Quels risques présente la chaîne d'approvisionnement logicielle (paquets malveillants, dépendances vulnérables) ? Utilisez `npm audit`, `npm outdated`, `npm ci`, le fichier de verrouillage et la vérification des mainteneurs. Quelle bonne pratique pour mettre à jour (versions précises, délais, revue) ?

## 24.2 Outils de qualité et de build

**Exercice 24.2.1**

Installez ESLint avec une configuration « flat » (`eslint.config.js`) et lancez-le sur un projet. Corrigez trois avertissements (variable inutilisée, `==`, `var`).

**Exercice 24.2.2**

Installez Prettier ou Biome, configurez le formatage à l'enregistrement dans votre éditeur et appliquez-le à un projet. Quelle différence entre un linter et un formateur ?

**Exercice 24.2.3**

Créez un projet avec Vite (`npm create vite@latest`) : lancez le serveur de développement avec rechargement à chaud, construisez pour la production (`npm run build`) et examinez le dossier `dist`. Que font un bundler et un minificateur ?

**Exercice 24.2.4**

Comparez Vite, esbuild, Rollup, webpack, Parcel, Rolldown et Turbopack : usage, vitesse, écosystème. Dans quel cas un bundler est-il inutile (modules natifs, cartes d'import) ?

**Exercice 24.2.5**

Utilisez Babel ou SWC pour compiler une syntaxe récente vers une cible plus ancienne et `browserslist` pour définir les navigateurs visés. Qu'est-ce qu'un polyfill ? Quand en ajouter un (`core-js`) ?

**Exercice 24.2.6**

Mettez en place un crochet de pré-commit avec `husky` et `lint-staged` qui lance le linter et le formateur sur les fichiers modifiés, et une intégration continue qui lance les tests.

## 24.3 TypeScript

**Exercice 24.3.1**

Convertissez un petit fichier JavaScript en TypeScript : ajoutez des types aux paramètres et au retour de deux fonctions, définissez une interface pour un objet, et vérifiez avec `tsc --noEmit`.

**Exercice 24.3.2**

Utilisez `// @ts-check` et des annotations JSDoc (`@param`, `@returns`, `@typedef`) pour obtenir de la vérification de types sans quitter JavaScript. Quels sont les avantages et limites ?

**Exercice 24.3.3**

Exécutez un fichier TypeScript directement avec Node.js (effacement de types), `tsx`, Deno ou Bun. Quelles constructions TypeScript ne sont pas supportées par l'effacement de types simple (enums, `namespace`) ?

**Exercice 24.3.4**

Pourquoi les types TypeScript ne protègent-ils pas contre des données invalides arrivant à l'exécution (JSON d'une API) ? Quelle bibliothèque de validation (Zod, Valibot) utiliser pour la garantie à l'exécution ?

## 24.4 Frameworks et bibliothèques courants

**Exercice 24.4.1**

Pour chacun de ces outils, indiquez en une phrase son rôle et un cas d'usage : React, Vue, Angular, Svelte, Solid, Next.js, Nuxt, Astro, Express, Fastify, NestJS, Jest, Vitest, Playwright, Cypress, D3, Three.js, Lodash, date-fns, Zod.

**Exercice 24.4.2**

Choisissez un framework et écrivez un composant « compteur » (état, événement, rendu). Comparez avec la version en JavaScript natif (exercice 21.4.4) : quantité de code, lisibilité, performances.

**Exercice 24.4.3**

Écrivez un petit serveur HTTP en Node.js avec le module `node:http`, puis avec Express ou Fastify. Quelles fonctionnalités le framework apporte-t-il (routage, intergiciels, analyse du corps, gestion d'erreurs) ?

**Exercice 24.4.4**

Comment choisir une bibliothèque (maintenance active, nombre de dépendances, taille, licence, sécurité, documentation, compatibilité) ? Appliquez cette grille pour comparer deux bibliothèques de dates ou de requêtes HTTP.

## 24.5 Débogage

**Exercice 24.5.1**

Utilisez les méthodes de `console` : `log`, `info`, `warn`, `error`, `table`, `group`/`groupEnd`, `time`/`timeEnd`, `count`, `assert`, `dir`, `trace`, `%c` (style). Écrivez un petit module de journalisation avec niveaux.

**Exercice 24.5.2**

Utilisez l'instruction `debugger` et les points d'arrêt dans les outils de développement : points d'arrêt conditionnels, « logpoints », points d'arrêt sur événements, sur exceptions, pile d'appels, inspection des portées, surveillance d'expressions.

**Exercice 24.5.3**

Déboguez un programme Node.js avec `node --inspect` (ou `--inspect-brk`) et les outils de développement de Chrome, ou avec le débogueur de votre éditeur.

**Exercice 24.5.4**

Utilisez l'onglet « Réseau » pour analyser les requêtes d'une page (durées, tailles, en-têtes, cache), l'onglet « Performance » pour repérer une tâche longue, l'onglet « Mémoire » pour détecter une fuite.

**Exercice 24.5.5**

Utilisez les cartes de source (*source maps*) pour déboguer du code minifié ou transpilé. Comment les activer dans votre outil de build ?

**Exercice 24.5.6**

Reproduisez et corrigez trois bogues classiques : `this` perdu, comparaison de types (`"5" + 3`), fermeture dans une boucle `var`. Pour chacun, indiquez l'outil qui vous a permis de le repérer.

---

# 25. Nouveautés par version d'ECMAScript

**Exercice 25.1**

Associez chaque fonctionnalité à l'édition qui l'a introduite : `let` / `const`, `async` / `await`, `?.` et `??`, `replaceAll()`, champs privés `#`, `toSorted()`, `Object.groupBy()`, méthodes de `Set` (`union`), `Promise.try()`, `Array.fromAsync()`, `Iterator.concat()`, `Temporal`, `using`.

**Exercice 25.2**

Pour chaque édition de ES2015 à ES2026, écrivez un court exemple de code (3 à 6 lignes) qui illustre l'une de ses nouveautés et le problème qu'elle résout.

**Exercice 25.3**

Modernisez ce code écrit dans le style ES5 en utilisant les fonctionnalités récentes :

```js
var utilisateurs = [{ nom: "A", age: 30 }, { nom: "B", age: 17 }];
var adultes = [];
for (var i = 0; i < utilisateurs.length; i++) {
    if (utilisateurs[i].age >= 18) {
        adultes.push(utilisateurs[i].nom);
    }
}
var message = "Adultes : " + adultes.join(", ");
var ville = (utilisateurs[0] && utilisateurs[0].adresse && utilisateurs[0].adresse.ville) || "inconnue";
function Compteur() { this.n = 0; }
Compteur.prototype.inc = function () { this.n++; };
```

**Exercice 25.4**

Écrivez un programme de détection de fonctionnalités qui teste la présence de plusieurs API récentes (`Array.prototype.toSorted`, `Object.groupBy`, `Set.prototype.union`, `Promise.try`, `Temporal`, `structuredClone`, `Iterator.prototype.map`) et affiche un tableau de compatibilité pour l'environnement courant.

**Exercice 25.5**

Pour trois fonctionnalités de votre choix, écrivez un « polyfill » minimal conditionnel (qui n'écrase pas une version native) et testez-le dans un environnement où la fonctionnalité est absente ou simulée.

**Exercice 25.6**

Consultez la liste des propositions terminées de TC39 (stade 4) et choisissez trois propositions absentes du tableau du cours. Pour chacune, résumez son intérêt, écrivez un exemple et vérifiez sa compatibilité sur caniuse.com ou MDN.

**Exercice 25.7**

Comment vérifier la compatibilité d'une fonctionnalité avant de l'utiliser (`caniuse`, MDN, `browserslist`, tests de détection) ? Établissez une stratégie pour un projet destiné aux navigateurs de ces trois dernières années.

## Ressources pour progresser

**Exercice 25.8**

Parcourez MDN, javascript.info et la spécification ECMA-262. Choisissez une notion du cours qui vous paraît encore floue (par exemple les fermetures, la boucle d'événements, les prototypes) et rédigez une explication d'une page avec trois exemples de code, sans consulter le cours.

**Exercice 25.9** *(défi)*

Projet de synthèse : réalisez une petite application web complète (par exemple un gestionnaire de tâches ou de notes) qui met en oeuvre : modules ES, classes avec champs privés, DOM et événements délégués, `fetch` avec gestion des erreurs et annulation, stockage local, dates avec `Temporal` (ou `Intl`), tests avec `node:test` ou Vitest, ESLint et Prettier, et un `README` décrivant l'architecture.

---

<div align="center">

*Bon code !*

</div>
