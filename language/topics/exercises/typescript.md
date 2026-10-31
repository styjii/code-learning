<div align="center">

# TypeScript — Exercices

**Du premier type aux génériques, aux frameworks et à la configuration moderne**

*Mis à jour pour TypeScript 6.0 / 7.0 (octobre 2026)*

</div>

---

## Outils

| Ressource | Lien |
| --- | --- |
| Cours | [typescript](/language/typescript) |
| Documentation officielle | [typescriptlang.org](https://www.typescriptlang.org/docs/) |
| Bac à sable en ligne | [TypeScript Playground](https://www.typescriptlang.org/play) |

---

## Sommaire

**Niveau débutant**

1. [Introduction à TypeScript](#1-introduction-à-typescript)
2. [Types de base](#2-types-de-base)
3. [Fonctions et annotations de types](#3-fonctions-et-annotations-de-types)
4. [Tableaux et tuples](#4-tableaux-et-tuples)
5. [Énumérations (`enum`) et alternatives](#5-énumérations-enum-et-alternatives)
6. [Interfaces](#6-interfaces)
7. [Alias de types, unions et types littéraux](#7-alias-de-types-unions-et-types-littéraux)

**Niveau intermédiaire**

8. [Classes et programmation orientée objet](#8-classes-et-programmation-orientée-objet)
9. [Génériques](#9-génériques)
10. [Modules et espaces de noms](#10-modules-et-espaces-de-noms)
11. [Types avancés](#11-types-avancés)
12. [Fichiers de déclaration de types](#12-fichiers-de-déclaration-de-types)

**Niveau avancé**

13. [Types utilitaires](#13-types-utilitaires)
14. [Décorateurs](#14-décorateurs)
15. [Programmation asynchrone](#15-programmation-asynchrone)
16. [Manipuler le DOM](#16-manipuler-le-dom)
17. [Mixins et composition](#17-mixins-et-composition)
18. [TypeScript et frameworks front-end](#18-typescript-et-frameworks-front-end)
19. [TypeScript côté serveur](#19-typescript-côté-serveur)
20. [Configuration du projet (`tsconfig.json`)](#20-configuration-du-projet-tsconfigjson)
21. [Linting et formatage](#21-linting-et-formatage)

**Bonus**

22. [TypeScript et bases de données](#22-typescript-et-bases-de-données)
23. [TypeScript et tests](#23-typescript-et-tests)
24. [Nouveautés par version et bonnes pratiques](#24-nouveautés-par-version-et-bonnes-pratiques)

> **Légende** : chaque exercice porte le numéro de la section du cours qu'il illustre (l'exercice 7.2.3 est le troisième exercice de la section 7.2). *(défi)* = exercice plus difficile ; *(TS x.y)* = exercice nécessitant la version indiquée. Sauf mention contraire, les exercices supposent `strict: true` et TypeScript 6 ou 7. Quand l'énoncé demande si une ligne « compile », il s'agit de la vérification de types (`tsc --noEmit`), pas de l'exécution. Aucune solution n'est fournie dans ce document.

---

# Niveau débutant

---

# 1. Introduction à TypeScript

## 1.1 Qu'est-ce que TypeScript ?

**Exercice 1.1.1**

Indiquez si chaque affirmation est vraie ou fausse, en justifiant :

1. TypeScript est un langage distinct de JavaScript qui s'exécute dans son propre moteur.
2. Tout code JavaScript valide est du TypeScript valide.
3. Les types TypeScript existent encore à l'exécution.
4. TypeScript est développé et maintenu par Microsoft.
5. Le typage de TypeScript est statique et structurel.

**Exercice 1.1.2**

Expliquez avec vos mots la phrase « TypeScript = JavaScript + types statiques ». Qu'est-ce que le compilateur vérifie, et qu'est-ce qu'il produit ?

**Exercice 1.1.3**

Recopiez un script JavaScript de dix lignes dans un fichier `.ts`. Quelles erreurs le compilateur signale-t-il d'emblée ? Lesquelles révèlent des bugs potentiels ?

## 1.2 Pourquoi l'utiliser ?

**Exercice 1.2.1**

Voici un code JavaScript qui plante à l'exécution. Expliquez pourquoi, puis écrivez la version TypeScript dans laquelle l'erreur est détectée avant l'exécution :

```js
function aire(rectangle) {
  return rectangle.largeur * rectangle.hauteur;
}
console.log(aire({ largeur: 3, haut: 4 }));
console.log(aire("3x4").toFixed(2));
```

**Exercice 1.2.2**

Citez quatre bénéfices concrets de TypeScript (détection d'erreurs, autocomplétion, refactorisation, documentation) et, pour chacun, un exemple tiré de votre pratique ou de votre éditeur.

**Exercice 1.2.3**

TypeScript a-t-il un coût ? Listez au moins trois inconvénients ou limites (étape de build, courbe d'apprentissage, types non vérifiés à l'exécution) et une façon d'en atténuer chacun.

## 1.3 L'état de TypeScript en 2026 *(à jour)*

**Exercice 1.3.1**

Complétez le tableau suivant :

| Version | Date | Rôle ou nouveauté principale |
| --- | --- | --- |
| 5.x | | |
| 6.0 | | |
| 7.0 | | |

**Exercice 1.3.2**

Pourquoi TypeScript 6.0 est-il appelé « version passerelle » ? Quelle conséquence cela a-t-il sur votre `tsconfig.json` ?

**Exercice 1.3.3**

Le compilateur de TypeScript 7 est écrit en Go. Citez deux conséquences pratiques pour un développeur (vitesse, mémoire, parallélisme, compatibilité des outils qui utilisent l'API du compilateur).

## 1.4 Installer TypeScript

**Exercice 1.4.1**

Dans un dossier vide, initialisez un projet npm, installez TypeScript en dépendance de développement et vérifiez la version avec `npx tsc --version`. Pourquoi préférer une installation locale à une installation globale ?

**Exercice 1.4.2**

Quelles sont les différences entre `npm install -D typescript`, `pnpm add -D typescript` et `bun add -d typescript` ? Quel fichier de verrouillage chacun produit-il ?

### Compilateur natif (TypeScript 7)

**Exercice 1.4.3**

Installez `typescript@latest`, relancez `npx tsc -p .` sur un petit projet et notez le temps de compilation. Comparez-le avec celui de la version 6 installée dans un autre dossier. Quelle commande utilise-t-on pour lancer le compilateur natif ? *(TS 7)*

## 1.5 Écrire et exécuter un premier fichier

**Exercice 1.5.1**

Créez `bonjour.ts` contenant une fonction `saluer(nom: string): string` et un appel qui affiche le résultat. Compilez avec `npx tsc`, examinez le fichier `.js` produit, puis exécutez-le avec Node.js.

**Exercice 1.5.2**

Exécutez le même fichier directement, sans étape de compilation, avec trois outils différents parmi : Node.js (effacement de types), `tsx`, Bun, Deno. Notez les avantages et limites de chacun. Ces outils vérifient-ils les types ?

**Exercice 1.5.3**

Introduisez volontairement une erreur de type dans `bonjour.ts` (`saluer(42)`). Que font respectivement `tsc`, `tsx` et Node.js avec l'effacement de types ? Quelle commande faut-il ajouter en CI pour ne pas laisser passer l'erreur ?

**Exercice 1.5.4**

Observez avec l'option `--noEmitOnError` ce qui se passe quand le code contient une erreur de type. Quelle est la différence avec le comportement par défaut ?

## 1.6 Démarrer un projet

**Exercice 1.6.1**

Créez un projet complet : `npm init -y`, installation de TypeScript, génération d'un `tsconfig.json` avec `npx tsc --init`, dossier `src/` et `dist/`, scripts `build`, `dev` et `typecheck` dans `package.json`.

**Exercice 1.6.2**

Quelles options minimales mettriez-vous dans le `tsconfig.json` d'un petit programme Node.js ? Justifiez au moins cinq options.

**Exercice 1.6.3**

Ajoutez un fichier `.gitignore` adapté (dossiers `node_modules` et `dist`) et un script `clean`. Quel est l'intérêt de séparer `src` et `dist` ?

## 1.7 Les outils du quotidien

**Exercice 1.7.1**

Associez chaque outil à son rôle : VS Code, TypeScript Playground, tsx, Vite, esbuild, SWC, typescript-eslint, Prettier, Biome, Vitest, Jest.

**Exercice 1.7.2**

Pourquoi Vite, esbuild et SWC « suppriment les types sans les vérifier » ? Quel outil doit alors garantir la vérification des types dans votre chaîne de livraison ?

**Exercice 1.7.3**

Utilisez le Playground pour essayer un extrait de code, partagez le lien et notez les options du compilateur activables dans l'interface. Comment voir le JavaScript généré ?

## 1.8 Résumé

**Exercice 1.8.1**

Rédigez, sans consulter le cours, un résumé de huit lignes sur ce qu'est TypeScript, la différence entre `tsc --noEmit` et un outil comme `tsx`, et la version actuelle.

**Exercice 1.8.2**

Vrai ou faux, en justifiant : « Si mon éditeur ne montre aucune erreur rouge, mon code est correct à l'exécution. »

---

# 2. Types de base

## 2.1 Les types primitifs

**Exercice 2.1.1**

Déclarez une variable de chacun des types primitifs suivants avec une annotation explicite : `string`, `number`, `boolean`, `bigint`, `symbol`, `null`, `undefined`.

**Exercice 2.1.2**

Quelles lignes ne compilent pas ? Expliquez :

```ts
let age: number = "25";
let nom: string = 'Alice';
let actif: boolean = 1;
let grand: bigint = 100;
let id: symbol = Symbol("id");
let rien: null = undefined;
let x: number = 0xff;
let y: number = 1_000_000;
```

**Exercice 2.1.3**

Quelle différence entre `number` et `bigint` ? Écrivez le calcul de `2n ** 64n` et expliquez pourquoi `1n + 1` ne compile pas.

**Exercice 2.1.4**

Quelle différence entre `string` et `String` (objet enveloppe) ? Pourquoi ne faut-il jamais utiliser les types `Number`, `String`, `Boolean`, `Object` ?

**Exercice 2.1.5**

Utilisez un littéral de gabarit avec une variable typée pour afficher une phrase. Quel est le type du résultat ?

## 2.2 Inférence de types

**Exercice 2.2.1**

Donnez le type inféré de chaque variable (survolez dans votre éditeur pour vérifier) :

```ts
let a = 3;
const b = 3;
let c = "x";
const d = "x";
let e = [1, 2, 3];
let f = [1, "a"];
const g = { nom: "Alice", age: 30 };
let h = null;
let i;
const j = [] ;
```

**Exercice 2.2.2**

Pourquoi `const b = 3` a-t-il pour type `3` alors que `let a = 3` a pour type `number` ? Qu'est-ce que l'élargissement de type (*widening*) ?

**Exercice 2.2.3**

Quand faut-il annoter explicitement une variable plutôt que de se reposer sur l'inférence ? Donnez trois cas (variable sans valeur initiale, paramètres de fonction, valeur de retour publique).

**Exercice 2.2.4**

Pourquoi `let i;` a-t-il un type différent selon les affectations suivantes (typage « évolutif » de `any`) ? Quel risque cela présente-t-il avec `noImplicitAny` ?

## 2.3 Types spéciaux

### `any` : l'échappatoire (à éviter)

**Exercice 2.3.1**

Écrivez un code où `any` laisse passer une erreur qui plantera à l'exécution (`let x: any = 5; x.toUpperCase();`). Réécrivez-le sans `any` pour que le compilateur détecte l'erreur.

**Exercice 2.3.2**

Qu'est-ce que `noImplicitAny` ? Quelles lignes déclenchent une erreur avec cette option : un paramètre sans annotation, une variable initialisée sans type, un tableau vide ?

**Exercice 2.3.3**

Citez deux usages acceptables de `any` (migration progressive, interopérabilité temporaire) et la façon de les limiter (`// @ts-expect-error`, commentaires de justification, règles ESLint).

### `unknown` : la version sûre

**Exercice 2.3.4**

Écrivez une fonction `parser(json: string): unknown` et une fonction qui consomme son résultat en restreignant d'abord le type (`typeof`, `in`, `instanceof`).

**Exercice 2.3.5**

Comparez `any` et `unknown` : que peut-on faire d'une valeur `unknown` sans restriction ? Quelles lignes compilent ?

```ts
const v: unknown = "abc";
v.length;
v + 1;
const s: string = v;
if (typeof v === "string") v.length;
```

**Exercice 2.3.6**

Écrivez une fonction `estTableauDeNombres(x: unknown): x is number[]`. Utilisez-la pour restreindre un résultat de `JSON.parse`.

### `void`, `never`, `object`

**Exercice 2.3.7**

Quel est le type de retour d'une fonction qui ne renvoie rien ? Pourquoi un `callback: () => void` accepte-t-il une fonction qui renvoie un nombre ?

**Exercice 2.3.8**

Écrivez une fonction `echec(message: string): never` qui lève toujours une exception et une autre qui boucle indéfiniment. Quelle différence entre `void` et `never` ?

**Exercice 2.3.9**

Quelle différence entre `object`, `Object` et `{}` ? Lesquelles de ces affectations compilent : `let a: object = {}`, `let b: object = 5`, `let c: {} = 5`, `let d: object = [1]` ?

## 2.4 `null` et `undefined` en mode strict

**Exercice 2.4.1**

Que change `strictNullChecks` ? Écrivez une fonction `trouver(id: number): Utilisateur | undefined` et utilisez son résultat de façon sûre.

**Exercice 2.4.2**

Utilisez l'opérateur de chaînage optionnel `?.` et l'opérateur de coalescence `??` pour lire `utilisateur?.adresse?.ville ?? "Inconnue"`. Quelle différence entre `??` et `||` avec la valeur `0` ?

**Exercice 2.4.3**

Quand l'opérateur de non-nullité `!` est-il acceptable ? Écrivez un exemple où il masque un bug et la version sûre correspondante.

**Exercice 2.4.4**

Que fait l'opérateur d'affectation `??=` ? Écrivez un cache simple d'initialisation paresseuse avec cet opérateur.

## 2.5 Assertions de type

**Exercice 2.5.1**

Écrivez une assertion `as` pour un élément du DOM (`document.getElementById("champ") as HTMLInputElement`). Quel risque prend-on ? Proposez une version plus sûre.

**Exercice 2.5.2**

Quelles assertions compilent, lesquelles sont refusées ? Pourquoi `as unknown as T` contourne-t-il la vérification et pourquoi est-ce dangereux ?

```ts
const a = "abc" as string;
const b = "abc" as number;
const c = 5 as unknown as string;
const d = { x: 1 } as { x: number; y: number };
```

**Exercice 2.5.3**

Quelle différence entre une assertion de type (`as`) et une conversion de type (`Number("5")`) ? Quand chacune est-elle appropriée ?

## 2.6 `as const` et `satisfies` *(ajout)*

**Exercice 2.6.1**

Donnez le type de `const config = { mode: "dev", ports: [80, 443] }` avec et sans `as const`. Que signifie `readonly` dans le type obtenu ?

**Exercice 2.6.2**

Utilisez `satisfies` pour valider qu'un objet respecte un type tout en conservant son type précis :

```ts
type Couleurs = Record<string, string | number[]>;

const palette = {
  rouge: [255, 0, 0],
  vert: "#00ff00",
} satisfies Couleurs;
```

Quelle erreur obtient-on si l'on remplace `satisfies` par une annotation `: Couleurs` quand on écrit `palette.rouge.map(...)` ?

**Exercice 2.6.3**

Combinez `as const` et `satisfies` pour définir un tableau de routes dont les chemins sont des littéraux, tout en vérifiant la forme de chaque route.

**Exercice 2.6.4**

Quand utiliser une annotation de type, `as const`, `satisfies` ou une assertion `as` ? Complétez le tableau avec un exemple pour chacun.

## 2.7 Types propres aux objets et fonctions (aperçu)

**Exercice 2.7.1**

Écrivez un type littéral d'objet pour un utilisateur (`nom`, `age`, `email?`) et un type de fonction pour une fonction de rappel `(valeur: number) => boolean`. Affectez-leur des valeurs.

**Exercice 2.7.2**

Pourquoi `{ nom: string; age: number }` accepte-t-il un objet qui a des propriétés supplémentaires lorsqu'il est passé par une variable, mais pas lorsqu'il est écrit directement (vérification des propriétés excédentaires) ? Illustrez avec un exemple.

---

# 3. Fonctions et annotations de types

## 3.1 Annoter paramètres et retour

**Exercice 3.1.1**

Écrivez, avec annotations complètes, les fonctions : `additionner(a, b)`, `estPair(n)`, `longueur(texte)`, `premier(tableau: number[])`, `saluer(nom)` qui affiche un message sans rien renvoyer.

**Exercice 3.1.2**

Que se passe-t-il pour chaque appel de `function f(a: number, b: number): number` : `f(1)`, `f(1, 2, 3)`, `f("1", 2)`, `f(1, 2)` ?

**Exercice 3.1.3**

Quand faut-il annoter explicitement le type de retour (fonctions publiques, récursives, `isolatedDeclarations`) ? Écrivez une fonction récursive qui exige l'annotation.

**Exercice 3.1.4**

Écrivez la même fonction sous la forme d'une déclaration, d'une expression de fonction et d'une fonction fléchée, avec annotations. Quelles différences de `this` et de remontée (*hoisting*) ?

## 3.2 Paramètres optionnels, par défaut et *rest*

**Exercice 3.2.1**

Écrivez `creerUtilisateur(nom: string, age?: number)`. Quel est le type de `age` dans le corps de la fonction ?

**Exercice 3.2.2**

Écrivez `puissance(base: number, exposant = 2)`. Quel type est inféré pour `exposant` ? Que se passe-t-il pour `puissance(3, undefined)` ?

**Exercice 3.2.3**

Écrivez `somme(...nombres: number[]): number` et `joindre(sep: string, ...morceaux: string[])`. Appelez-les avec un tableau déplié (`...tableau`).

**Exercice 3.2.4**

Pourquoi un paramètre optionnel ne peut-il pas précéder un paramètre obligatoire ? Écrivez deux alternatives (paramètre par défaut, objet d'options).

**Exercice 3.2.5**

Écrivez une fonction `ouvrir(options: { chemin: string; lecture?: boolean; encodage?: string })` avec une déstructuration et des valeurs par défaut typées.

## 3.3 Types de fonctions

**Exercice 3.3.1**

Écrivez un alias `type Operation = (a: number, b: number) => number` puis `addition`, `multiplication` et une fonction `appliquer(op: Operation, a: number, b: number)`.

**Exercice 3.3.2**

Écrivez le type d'une fonction qui reçoit une fonction de rappel `(erreur: Error | null, donnees?: string) => void`. Implémentez une fonction `lire` qui l'appelle.

**Exercice 3.3.3**

Quelle différence entre la syntaxe `(x: number) => void` et la syntaxe de signature d'appel `{ (x: number): void }` ? Écrivez un type de fonction qui possède aussi une propriété (`description: string`).

**Exercice 3.3.4**

Pourquoi les noms de paramètres dans un type de fonction n'ont-ils pas besoin de correspondre à ceux de l'implémentation ? Pourquoi une fonction avec moins de paramètres est-elle assignable à un type qui en prévoit plus ?

## 3.4 Surcharges de fonctions

**Exercice 3.4.1**

Écrivez une fonction `formater` surchargée : `formater(valeur: string): string`, `formater(valeur: number, decimales: number): string`. Écrivez l'implémentation compatible avec les deux signatures.

**Exercice 3.4.2**

Pourquoi la signature d'implémentation n'est-elle pas visible de l'extérieur ? Montrez un appel qui est refusé alors que l'implémentation l'accepterait.

**Exercice 3.4.3**

Quand préférer une union de types ou un paramètre générique à des surcharges ? Réécrivez ainsi une fonction à deux surcharges inutiles.

**Exercice 3.4.4**

Écrivez des surcharges pour `creerElement(tag: "a"): HTMLAnchorElement`, `creerElement(tag: "canvas"): HTMLCanvasElement`, et un cas général. Quel est l'ordre des signatures et pourquoi est-il important ?

## 3.5 Le paramètre `this`

**Exercice 3.5.1**

Écrivez une fonction avec un paramètre `this` typé (`function afficher(this: Utilisateur)`). Que se passe-t-il si on l'appelle sans contexte ?

**Exercice 3.5.2**

Pourquoi la fonction fléchée capture-t-elle le `this` lexical ? Écrivez un exemple de classe où un gestionnaire d'événement perd son `this`, puis corrigez-le avec une fonction fléchée ou `bind`.

**Exercice 3.5.3**

Utilisez `ThisParameterType` et `OmitThisParameter` sur une fonction qui déclare `this`.

## 3.6 Restriction de type (*narrowing*) et gardes de type

**Exercice 3.6.1**

Écrivez une fonction `afficher(valeur: string | number | boolean | null)` qui restreint le type avec `typeof`, une comparaison à `null` et l'égalité stricte. Quel est le type dans chaque branche ?

**Exercice 3.6.2**

Utilisez `instanceof` pour restreindre `Date | RegExp | Error`, `in` pour restreindre `Chat | Chien` selon la présence d'une méthode, et la restriction par vérité (`if (x)`). Quels pièges avec `0`, `""` et `NaN` ?

**Exercice 3.6.3**

Écrivez une fonction `longueur(x: string | string[])` qui utilise `Array.isArray`. Pourquoi `typeof x === "object"` serait-il insuffisant ?

**Exercice 3.6.4**

Décrivez le fonctionnement de l'analyse de flux de contrôle : comment le type d'une variable évolue-t-il après chaque `if`, `return`, affectation ? Écrivez un exemple avec trois restrictions successives.

### Gardes de type personnalisées (*type predicates*)

**Exercice 3.6.5**

Écrivez `estChaine(x: unknown): x is string` et `estUtilisateur(x: unknown): x is Utilisateur` qui vérifie les propriétés de `x`. Pourquoi le compilateur ne contrôle-t-il pas que votre garde est correcte ?

**Exercice 3.6.6**

Utilisez une garde de type dans `tableau.filter(...)` pour passer de `(string | null)[]` à `string[]`. Depuis TS 5.5, dans quel cas la garde est-elle inférée automatiquement ? *(TS 5.5)*

**Exercice 3.6.7**

Écrivez une garde avec `asserts`-less : `estPoint(x: unknown): x is { x: number; y: number }` et une garde sur une union discriminée.

### Fonctions d'assertion

**Exercice 3.6.8**

Écrivez `assertDefini<T>(valeur: T | null | undefined, message: string): asserts valeur is T` et utilisez-la pour éliminer `null` du type d'une variable.

**Exercice 3.6.9**

Écrivez `assert(condition: unknown): asserts condition`. Quelle différence entre une fonction d'assertion et une garde de type ?

## 3.7 Valeur de retour `never` et exhaustivité

**Exercice 3.7.1**

Écrivez une fonction `aireForme` qui traite une union `Cercle | Carre | Triangle` avec un `switch` et une fonction `verifierExhaustivite(x: never): never` dans la branche `default`. Que se passe-t-il à la compilation quand on ajoute une nouvelle forme à l'union sans mettre à jour le `switch` ?

**Exercice 3.7.2**

Réécrivez l'exercice précédent avec `satisfies never` ou une affectation à une variable de type `never`.

**Exercice 3.7.3**

Pourquoi l'exhaustivité est-elle plus fiable que des tests unitaires pour détecter l'oubli d'un cas ? Quelle option du compilateur (`noImplicitReturns`) aide aussi ?

## 3.8 Fonctions génériques (aperçu)

**Exercice 3.8.1**

Écrivez `identite<T>(x: T): T` et `premier<T>(tableau: T[]): T | undefined`. Appelez-les en laissant l'inférence travailler, puis avec un argument de type explicite.

**Exercice 3.8.2**

Écrivez `paire<A, B>(a: A, b: B): [A, B]` et `echanger<A, B>(p: [A, B]): [B, A]`.

**Exercice 3.8.3**

Pourquoi `function f<T>(x: T): T { return x + 1; }` est-il refusé ? Quelle contrainte faudrait-il pour le rendre valide ?

---

# 4. Tableaux et tuples

## 4.1 Tableaux

**Exercice 4.1.1**

Déclarez un tableau de nombres de deux façons (`number[]` et `Array<number>`), un tableau de chaînes, un tableau d'objets `{ nom: string; age: number }`, et un tableau vide correctement typé (`const t: string[] = []`).

**Exercice 4.1.2**

Quelles lignes ne compilent pas ?

```ts
const a: number[] = [1, 2, 3];
a.push("4");
const b: (number | string)[] = [1, "2"];
const c = [1, 2, 3];
c[0] = "x";
const d: number[][] = [[1], [2, 3]];
const e = [];
e.push(1);
```

**Exercice 4.1.3**

Écrivez une fonction `moyenne(valeurs: number[]): number`, une fonction `unique<T>(valeurs: T[]): T[]` et une fonction `grouperPar<T, K extends string>(valeurs: T[], cle: (v: T) => K): Record<K, T[]>`.

### Méthodes typées

**Exercice 4.1.4**

Quel est le type inféré du résultat de : `[1, 2, 3].map(String)`, `["a", "b"].map(s => s.length)`, `[1, 2, 3].filter(n => n > 1)`, `[1, 2, 3].reduce((a, b) => a + b, 0)`, `["a", "b"].find(s => s === "a")`, `[1, 2, 3].some(n => n > 2)`, `[[1], [2]].flat()`, `[1, 2, 3].includes(2)` ?

**Exercice 4.1.5**

Que se passe-t-il avec `[1, 2, 3].includes("2")` ? Comment contourner ce problème sans `as any` pour un tableau de littéraux déclaré avec `as const` ?

**Exercice 4.1.6**

Écrivez `[ "a", "b" ].reduce(...)` pour construire un objet `Record<string, number>`. Quel type donner à l'accumulateur initial ?

### Tableaux en lecture seule

**Exercice 4.1.7**

Déclarez `readonly number[]` et `ReadonlyArray<number>`. Quelles méthodes disparaissent ? Pourquoi accepter `readonly T[]` dans les paramètres d'une fonction est-il une bonne pratique ?

**Exercice 4.1.8**

Pourquoi un `number[]` est-il assignable à un `readonly number[]` mais pas l'inverse ? Écrivez les deux affectations.

**Exercice 4.1.9**

Utilisez `as const` pour obtenir un tuple en lecture seule `readonly ["a", "b", "c"]` et dérivez-en le type union `"a" | "b" | "c"` avec `(typeof tableau)[number]`.

### Accès sûr aux indices : `noUncheckedIndexedAccess`

**Exercice 4.1.10**

Quel est le type de `tableau[0]` avec et sans `noUncheckedIndexedAccess` ? Pourquoi cette option est-elle recommandée ? Écrivez une boucle `for` avec indices qui gère correctement le cas `undefined`.

**Exercice 4.1.11**

Comment parcourir un tableau sans avoir à tester `undefined` à chaque accès (`for...of`, `entries()`, `at()`) ? Écrivez les trois versions.

## 4.2 Tuples

**Exercice 4.2.1**

Déclarez un tuple `[string, number]`, un tuple avec éléments nommés `[nom: string, age: number]`, un tuple avec élément optionnel `[number, number?]` et un tuple avec reste `[string, ...number[]]`.

**Exercice 4.2.2**

Quelles lignes compilent ?

```ts
const p: [string, number] = ["a", 1];
p[2];
p.push(3);
const q: [string, number] = [1, "a"];
const r: readonly [number, number] = [1, 2];
r[0] = 3;
const [x, y] = p;
```

**Exercice 4.2.3**

Écrivez une fonction qui renvoie un tuple `[valeur, erreur]` à la manière de Go ou de React (`useState`), puis déstructurez-la.

**Exercice 4.2.4**

Écrivez un type `Point3D = [x: number, y: number, z: number]` et une fonction `distance(a: Point3D, b: Point3D)`.

**Exercice 4.2.5**

Quelle différence entre un tuple et un tableau d'union ? Pourquoi `push` sur un tuple est-il une faille connue de TypeScript ? Comment s'en protéger ?

**Exercice 4.2.6**

Utilisez les tuples variadiques pour typer une fonction `concat<A extends unknown[], B extends unknown[]>(a: [...A], b: [...B]): [...A, ...B]`. *(défi)*

---

# 5. Énumérations (`enum`) et alternatives

## 5.1 Enums numériques

**Exercice 5.1.1**

Définissez `enum Direction { Haut, Bas, Gauche, Droite }`. Quelles sont les valeurs de chaque membre ? Définissez la même énumération en démarrant à `1`, puis avec des valeurs explicites quelconques.

**Exercice 5.1.2**

Écrivez le code JavaScript généré par un `enum` numérique (consultez le résultat dans le Playground). Qu'est-ce que le « mappage inverse » ? Écrivez `Direction[0]`.

**Exercice 5.1.3**

Pourquoi un enum numérique est-il peu sûr (n'importe quel nombre est assignable dans les anciennes versions) ? Quelle est la situation depuis TS 5.0 (enums unifiés) ?

**Exercice 5.1.4**

Écrivez un enum de drapeaux binaires (`Lecture = 1 << 0`, `Ecriture = 1 << 1`, `Execution = 1 << 2`) et combinez-les avec `|`, testez avec `&`.

## 5.2 Enums de chaînes

**Exercice 5.2.1**

Définissez `enum Statut { Actif = "ACTIF", Inactif = "INACTIF" }`. Que se passe-t-il pour `const s: Statut = "ACTIF"` ? Pourquoi les enums de chaînes sont-ils « nominaux » ?

**Exercice 5.2.2**

Écrivez une fonction `libelle(statut: Statut): string` avec un `switch` exhaustif.

**Exercice 5.2.3**

Pourquoi les enums de chaînes n'ont-ils pas de mappage inverse ? Comment retrouver le nom d'un membre à partir de sa valeur ?

## 5.3 `const enum` et `declare enum`

**Exercice 5.3.1**

Définissez un `const enum`, utilisez-le, puis inspectez le JavaScript généré. Quelle est la différence de code produit avec un `enum` ordinaire ?

**Exercice 5.3.2**

Pourquoi `const enum` est-il problématique avec `isolatedModules` et les transpileurs (Babel, esbuild, SWC) ? Que propose `preserveConstEnums` ?

**Exercice 5.3.3**

À quoi sert `declare enum` ? Dans quels fichiers le rencontre-t-on ?

## 5.4 Les alternatives modernes aux enums *(à jour)*

**Exercice 5.4.1**

Pourquoi le cours recommande-t-il d'éviter les enums dans le code moderne ? Citez trois raisons (JS généré, `erasableSyntaxOnly`, typage nominal des enums de chaînes, compatibilité avec les outils d'effacement de types).

### Union de littéraux

**Exercice 5.4.2**

Remplacez `enum Direction` par un type union `"haut" | "bas" | "gauche" | "droite"`. Réécrivez une fonction `deplacer(direction)` avec `switch` exhaustif.

**Exercice 5.4.3**

Quels sont les inconvénients d'une union de littéraux par rapport à un enum (itération sur les valeurs, documentation, renommage) ? Comment les contourner ?

### Objet `as const` + type dérivé

**Exercice 5.4.4**

Écrivez :

```ts
const Statut = {
  Actif: "ACTIF",
  Inactif: "INACTIF",
  Suspendu: "SUSPENDU",
} as const;
```

puis dérivez le type `Statut` (union des valeurs) et le type des clés. Écrivez un `for` qui parcourt les valeurs.

**Exercice 5.4.5**

Écrivez une fonction générique `valeursDe<T extends Record<string, string | number>>(obj: T): T[keyof T][]` et utilisez-la avec l'objet précédent.

**Exercice 5.4.6**

Convertissez un enum existant du projet (au choix) vers l'objet `as const` + type dérivé, et listez les changements à faire dans les usages (imports de valeurs et de types).

---

# 6. Interfaces

## 6.1 Définir une interface

**Exercice 6.1.1**

Définissez une interface `Utilisateur` avec `id: number`, `nom: string`, `email?: string` et `readonly creeLe: Date`. Créez-en deux instances valides et deux instances invalides, en expliquant l'erreur de chacune.

**Exercice 6.1.2**

Quelle différence entre une propriété optionnelle (`?`) et une propriété qui vaut `undefined` (`x: string | undefined`) ? Quel est l'effet de `exactOptionalPropertyTypes` ?

**Exercice 6.1.3**

Que se passe-t-il quand on modifie une propriété `readonly` ? `readonly` protège-t-il à l'exécution ? Écrivez une fonction qui reçoit un objet `Readonly<Utilisateur>` et tente de le modifier.

**Exercice 6.1.4**

Définissez des interfaces imbriquées : `Adresse` et `Client` qui contient une `Adresse`. Écrivez une fonction `formaterAdresse(client: Client): string`.

**Exercice 6.1.5**

Expliquez le typage structurel (*duck typing*) : un objet qui possède les propriétés requises est-il accepté même sans déclarer qu'il « implémente » l'interface ? Écrivez un exemple avec deux interfaces de noms différents mais de forme identique.

## 6.2 Méthodes, fonctions et signatures d'index

**Exercice 6.2.1**

Définissez une interface `Minuteur` avec une méthode `demarrer(): void`, une propriété de type fonction `surFin: () => void` et une méthode avec paramètre optionnel. Quelle différence entre la syntaxe méthode et la syntaxe propriété (`bivariance`, `strictFunctionTypes`) ?

**Exercice 6.2.2**

Définissez une interface décrivant une fonction (`interface Comparateur { (a: number, b: number): number }`) et une interface avec signature d'index (`interface Dictionnaire { [cle: string]: number }`).

**Exercice 6.2.3**

Quelles lignes compilent pour `interface Notes { [matiere: string]: number; moyenne: number; }` et `{ nom: string; [k: string]: number }` ? Pourquoi la seconde est-elle refusée ?

**Exercice 6.2.4**

Quel est le type de `dict["absent"]` avec et sans `noUncheckedIndexedAccess` ? Comparez avec `Record<string, number>` et `Map<string, number>`.

**Exercice 6.2.5**

Définissez une interface avec une signature d'index `` [cle: `data-${string}`]: string ``. Quelles clés sont acceptées ? *(TS 4.4)*

**Exercice 6.2.6**

Définissez une interface décrivant un constructeur (`new (...args) => ...`) et une usine qui l'utilise.

## 6.3 Héritage d'interfaces

**Exercice 6.3.1**

Définissez `Animal` (nom), `Chien extends Animal` (race) et `ChienGuide extends Chien` (maitre). Créez un objet de chaque type.

**Exercice 6.3.2**

Faites hériter une interface de deux autres (`extends A, B`). Que se passe-t-il quand A et B déclarent la même propriété avec des types incompatibles ?

**Exercice 6.3.3**

Une interface peut-elle étendre un alias de type objet ? Une interface peut-elle étendre une union ? Essayez et notez les erreurs.

**Exercice 6.3.4**

Affinez un type hérité : dans `interface Specifique extends Base`, restreignez le type d'une propriété (`string` vers un littéral). Pourquoi l'élargir est-il impossible ?

## 6.4 Implémentation par une classe

**Exercice 6.4.1**

Écrivez une interface `Forme` (`aire(): number`, `nom: string`) et deux classes qui l'implémentent (`Cercle`, `Rectangle`). Quelles erreurs obtient-on si une méthode est absente ?

**Exercice 6.4.2**

Une classe peut-elle implémenter plusieurs interfaces ? Écrivez `class Robot implements Mobile, Parlant`.

**Exercice 6.4.3**

`implements` hérite-t-il des implémentations ? Illustrez que `implements` ne fait que vérifier la forme et ne copie ni code ni modificateurs d'accès.

## 6.5 Fusion de déclarations (*declaration merging*)

**Exercice 6.5.1**

Déclarez deux fois `interface Configuration` avec des propriétés différentes. Quel est le type résultant ? Le même exercice fonctionne-t-il avec `type` ?

**Exercice 6.5.2**

Étendez une interface globale (`Window`, `Array`, `Process`) avec une nouvelle propriété ou méthode (par exemple `Array.prototype.dernier`). Dans quel fichier placer la déclaration ?

**Exercice 6.5.3**

Quelle est la règle quand deux déclarations d'une même méthode surchargent ? Quelle déclaration est prioritaire ?

**Exercice 6.5.4**

Citez un risque de la fusion de déclarations (collision de noms, surprise dans un grand projet).

## 6.6 `interface` ou `type` ?

**Exercice 6.6.1**

Complétez le tableau comparatif `interface` / `type` : fusion de déclarations, unions, tuples, types mappés, types primitifs, héritage (`extends` vs `&`), `implements`, messages d'erreur.

**Exercice 6.6.2**

Pour chaque besoin, choisissez `interface` ou `type` : forme d'un objet public d'une bibliothèque, union de chaînes, tuple, type de fonction, type conditionnel, forme d'un objet destiné à être étendu par les utilisateurs.

**Exercice 6.6.3**

Réécrivez le même modèle de données avec `interface` puis avec `type`. Les deux versions sont-elles équivalentes pour le compilateur ?

---

# 7. Alias de types, unions et types littéraux

## 7.1 Alias de types

**Exercice 7.1.1**

Écrivez des alias pour : `Identifiant` (`string | number`), `Point` (objet avec `x` et `y`), `Predicat<T>` (fonction qui renvoie un booléen), `Json` (type récursif des valeurs JSON).

**Exercice 7.1.2**

Un alias crée-t-il un nouveau type ou seulement un nouveau nom ? Montrez que `type Euro = number` et `type Dollar = number` sont interchangeables, puis expliquez comment on peut les distinguer (voir les types marqués au chapitre 11).

**Exercice 7.1.3**

Écrivez un alias générique `Paire<T> = [T, T]` et `Resultat<T, E = Error> = { ok: true; valeur: T } | { ok: false; erreur: E }`.

## 7.2 Types union (`|`) : « l'un OU l'autre »

**Exercice 7.2.1**

Écrivez une fonction `formater(x: string | number | Date)` qui restreint chaque cas. Que peut-on faire d'une valeur d'union sans restriction ?

**Exercice 7.2.2**

Pourquoi `function f(x: string | number) { return x.toFixed(2); }` est-il refusé ? Corrigez-le de deux façons.

**Exercice 7.2.3**

Quel est le type de `(string | number)[]` et de `string[] | number[]` ? Pourquoi `.map` est-il parfois difficile à appeler sur la seconde (appelabilité des unions de tableaux) ?

### Unions discriminées (*discriminated unions*)

**Exercice 7.2.4**

Modélisez un état de requête avec trois cas : `{ statut: "chargement" }`, `{ statut: "succes"; donnees: string[] }`, `{ statut: "erreur"; message: string }`. Écrivez `afficher(etat)` avec un `switch` sur `statut` et une branche exhaustive.

**Exercice 7.2.5**

Modélisez des formes (`cercle` avec `rayon`, `rectangle` avec `largeur` et `hauteur`, `triangle` avec `base` et `hauteur`) et écrivez `aire`, `perimetre`. Pourquoi la propriété discriminante doit-elle être un type littéral ?

**Exercice 7.2.6**

Modélisez des événements d'application (`{ type: "connexion"; utilisateur: string }`, `{ type: "achat"; montant: number }`, `{ type: "deconnexion" }`) et un réducteur `(etat, evenement) => etat`.

**Exercice 7.2.7**

Donnez un exemple d'« état impossible » que permet une modélisation par un objet aux propriétés optionnelles (`{ chargement: boolean; donnees?: T; erreur?: string }`) et comment l'union discriminée l'interdit.

**Exercice 7.2.8**

Extrayez le type d'un membre d'une union par son discriminant : `Extract<Evenement, { type: "achat" }>`.

## 7.3 Types intersection (`&`) : « l'un ET l'autre »

**Exercice 7.3.1**

Combinez `{ nom: string }` et `{ age: number }` avec `&`. Créez un objet valide et un objet invalide.

**Exercice 7.3.2**

Que vaut `string & number` ? Que se passe-t-il quand deux types d'objets déclarent la même propriété avec des types incompatibles dans une intersection ?

**Exercice 7.3.3**

Comparez `A & B` et `interface C extends A, B` : messages d'erreur, conflits de propriétés, performances.

**Exercice 7.3.4**

Utilisez une intersection pour ajouter des métadonnées à un type existant : `type AvecId<T> = T & { id: string }`.

## 7.4 Types littéraux

**Exercice 7.4.1**

Écrivez `type Direction = "haut" | "bas" | "gauche" | "droite"` et `type Des = 1 | 2 | 3 | 4 | 5 | 6`. Écrivez une fonction `lancer(): Des`. Quelles affectations sont refusées ?

**Exercice 7.4.2**

Pourquoi `let d = "haut"` a-t-il le type `string`, alors que `const d = "haut"` a le type `"haut"` ? Comment passer `d` à une fonction qui attend `Direction` sans assertion ?

**Exercice 7.4.3**

Écrivez une fonction `ouvrir(mode: "r" | "w" | "a")`. Que se passe-t-il pour `ouvrir(modeSaisi)` où `modeSaisi: string` ? Écrivez une garde de type qui restreint `string` à ce type littéral.

**Exercice 7.4.4**

Utilisez des littéraux booléens et numériques : `type Vrai = true`, une fonction dont le retour dépend d'un paramètre `boolean` littéral (avec surcharges).

## 7.5 Types littéraux de gabarit (*template literal types*)

**Exercice 7.5.1**

Écrivez `` type Evenement = `on${"Click" | "Hover"}` ``. Quelles chaînes sont acceptées ? Combien de membres a l'union `` `${"a" | "b"}-${1 | 2 | 3}` `` ?

**Exercice 7.5.2**

Écrivez `` type CssLongueur = `${number}px` | `${number}rem` `` et une fonction qui l'accepte. Quelles valeurs sont refusées ?

**Exercice 7.5.3**

Écrivez un type `` Route = `/users/${string}` `` et vérifiez quelles chaînes sont acceptées.

**Exercice 7.5.4**

Utilisez `Uppercase`, `Lowercase`, `Capitalize` et `Uncapitalize` pour générer `` type Getter = `get${Capitalize<"nom" | "age">}` ``.

## 7.6 Restriction (*narrowing*) : récapitulatif

**Exercice 7.6.1**

Dressez un tableau récapitulatif des techniques de restriction : `typeof`, `instanceof`, `in`, égalité, vérité, `Array.isArray`, garde personnalisée, discriminant, assertion. Pour chacune, donnez un exemple.

**Exercice 7.6.2**

Quel est le type de `x` à chaque ligne commentée ?

```ts
function f(x: string | number | null | undefined) {
  // (1)
  if (x == null) return;
  // (2)
  if (typeof x === "number") {
    // (3)
    return;
  }
  // (4)
}
```

**Exercice 7.6.3**

Écrivez une fonction qui perd la restriction à l'intérieur d'une fonction de rappel (`tableau.forEach`) quand la variable est un `let` modifiée plus tard. Comment conserver la restriction (copie dans une `const`) ?

## 7.7 `type` ou `interface` ?

**Exercice 7.7.1**

Rédigez, en cinq lignes, votre règle d'équipe pour choisir entre `type` et `interface`, puis appliquez-la à cinq déclarations de votre choix.

---

# Niveau intermédiaire

---

# 8. Classes et programmation orientée objet

## 8.1 Définir une classe

**Exercice 8.1.1**

Écrivez une classe `Compteur` avec une propriété `valeur` initialisée à 0, des méthodes `incrementer`, `decrementer`, `reinitialiser` et un constructeur qui accepte une valeur de départ facultative. Instanciez-la et manipulez-la.

**Exercice 8.1.2**

Que fait l'option `strictPropertyInitialization` ? Quelles propriétés de la classe suivante déclenchent une erreur ? Corrigez chacune de plusieurs façons (valeur initiale, constructeur, `?`, `!`) :

```ts
class Profil {
  nom: string;
  age: number;
  bio?: string;
  avatar: string | undefined;
  id!: number;
}
```

**Exercice 8.1.3**

Écrivez une classe `Rectangle` avec `largeur`, `hauteur`, une méthode `aire()`, un accesseur `get perimetre()` et un mutateur `set largeur(...)` qui refuse les valeurs négatives. Quel est le type du paramètre d'un `set` ?

**Exercice 8.1.4**

Écrivez une classe avec une propriété de type fonction fléchée (`gerer = () => {...}`) et une méthode ordinaire. Montrez la différence de comportement de `this` quand on les passe en callback.

**Exercice 8.1.5**

Que sont les champs privés natifs de JavaScript (`#secret`) ? Écrivez une classe qui en utilise, et comparez avec le modificateur TypeScript `private`.

## 8.2 Modificateurs d'accès

**Exercice 8.2.1**

Écrivez une classe `CompteBancaire` avec un solde `private`, une méthode publique `deposer`, une méthode `retirer` et un getter public `solde`. Quelles lignes sont refusées quand on essaie d'accéder directement au solde ?

**Exercice 8.2.2**

Pour chaque combinaison de modificateurs (`public`, `protected`, `private`, `readonly`, `#champ`), dites où l'on peut accéder au membre : dans la classe, dans une sous-classe, à l'extérieur, dans le JavaScript généré.

**Exercice 8.2.3**

Pourquoi `private` de TypeScript est-il une vérification à la compilation seulement ? Montrez comment le contourner avec `obj["champ"]` ou `as any`. Qu'apporte `#champ` en plus ?

**Exercice 8.2.4**

Écrivez une classe avec une propriété `readonly` initialisée dans le constructeur. Peut-on la modifier ailleurs ? Peut-on modifier le contenu d'un tableau `readonly` ?

## 8.3 Propriétés de paramètres (raccourci de constructeur)

**Exercice 8.3.1**

Réécrivez cette classe avec des propriétés de paramètres :

```ts
class Personne {
  private nom: string;
  readonly age: number;
  constructor(nom: string, age: number) {
    this.nom = nom;
    this.age = age;
  }
}
```

**Exercice 8.3.2**

Pourquoi `erasableSyntaxOnly` interdit-il les propriétés de paramètres ? Quelle alternative utiliser dans un projet qui active cette option ? *(TS 5.8)*

## 8.4 Propriétés et méthodes statiques

**Exercice 8.4.1**

Écrivez une classe `Identifiant` avec un compteur statique et une méthode statique `suivant()`. Écrivez aussi une classe `Utilitaires` avec des constantes statiques `readonly`.

**Exercice 8.4.2**

Écrivez un bloc d'initialisation statique (`static { ... }`) qui remplit un registre statique.

**Exercice 8.4.3**

Écrivez le patron « Singleton » avec un constructeur privé et un accesseur statique `instance`. Discutez des inconvénients de ce patron pour les tests.

**Exercice 8.4.4**

Écrivez une méthode de fabrique statique `Utilisateur.depuisJson(json: string)` qui renvoie une instance et valide les champs.

## 8.5 Héritage

**Exercice 8.5.1**

Écrivez `Animal` (nom, `parler()`) et `Chien extends Animal` qui redéfinit `parler()` et appelle `super.parler()`. Qu'est-ce qui oblige à appeler `super()` dans le constructeur de la classe fille avant d'utiliser `this` ?

**Exercice 8.5.2**

Utilisez le mot-clé `override` et l'option `noImplicitOverride`. Que se passe-t-il si la méthode du parent est renommée ?

**Exercice 8.5.3**

Peut-on réduire la visibilité d'un membre hérité (de `public` à `private`) ? L'augmenter (de `protected` à `public`) ? Essayez les deux.

**Exercice 8.5.4**

Une sous-classe peut-elle changer le type d'une propriété héritée ? Dans quelle mesure (covariance des propriétés) ? Quel risque cela présente-t-il ?

**Exercice 8.5.5**

Écrivez une hiérarchie à trois niveaux (`Vehicule`, `Voiture`, `VoitureElectrique`) et une fonction qui accepte un `Vehicule` et utilise `instanceof` pour réagir selon le sous-type.

## 8.6 Classes abstraites

**Exercice 8.6.1**

Écrivez une classe abstraite `Forme` avec une méthode abstraite `aire()` et une méthode concrète `decrire()` qui l'utilise. Écrivez `Cercle` et `Carre`. Que se passe-t-il quand on instancie `Forme` ?

**Exercice 8.6.2**

Quelle différence entre une classe abstraite et une interface ? Quand préférer l'une ou l'autre ? Complétez le tableau (code partagé, état, héritage multiple, existence à l'exécution).

**Exercice 8.6.3**

Utilisez `abstract` pour une propriété et un accesseur abstraits. Écrivez la patron « méthode gabarit » : une méthode concrète qui appelle des étapes abstraites.

## 8.7 Implémenter des interfaces

**Exercice 8.7.1**

Écrivez une interface `Serialisable` (`serialiser(): string`) et une interface `Identifiable` (`id: string`). Faites-les implémenter par une classe `Produit`.

**Exercice 8.7.2**

Écrivez une classe qui implémente une interface générique (`Depot<T>`), par exemple un dépôt en mémoire. Utilisez-la pour deux types différents.

**Exercice 8.7.3**

Que se passe-t-il si une classe implémente une interface mais déclare une méthode avec une signature plus large ou plus étroite ? Testez.

## 8.8 Le mot-clé `accessor` et la classe comme type

**Exercice 8.8.1**

Écrivez une classe avec `accessor nom = "x"`. Que génère le compilateur ? Quel est l'intérêt avec les décorateurs ? *(TS 4.9)*

**Exercice 8.8.2**

Une classe est à la fois une valeur et un type. Écrivez une fonction qui prend un paramètre de type `Utilisateur` (la classe) et une autre qui prend `typeof Utilisateur` (le constructeur). Quelle différence ?

**Exercice 8.8.3**

Écrivez un type `Constructeur<T> = new (...args: any[]) => T` et une fonction `creer<T>(classe: Constructeur<T>): T`.

## 8.9 Typage structurel : attention aux surprises

**Exercice 8.9.1**

Deux classes `Chat` et `Chien` ont la même forme (`nom: string`). Pourquoi une variable de type `Chat` accepte-t-elle une instance de `Chien` ? Comment rendre les deux types incompatibles (propriété `private`, propriété discriminante, type marqué) ?

**Exercice 8.9.2**

Les membres `private` et `protected` rendent-ils le typage nominal ? Écrivez un exemple.

**Exercice 8.9.3**

Pourquoi `instanceof` et le typage structurel peuvent-ils donner des résultats différents ? Écrivez un objet littéral qui respecte la forme de `Chien` mais n'est pas `instanceof Chien`.

## 8.10 Principes et bonnes pratiques

**Exercice 8.10.1**

Refactorisez une classe qui fait trop de choses (calcul, affichage, persistance) en trois classes respectant la responsabilité unique. Appliquez la composition plutôt que l'héritage quand c'est pertinent.

**Exercice 8.10.2**

Listez cinq règles pour des classes TypeScript propres (membres `readonly`, `private` par défaut, `override`, `implements` pour les contrats, éviter l'héritage profond) et appliquez-les à un exemple de votre choix.

---

# 9. Génériques

## 9.1 Le problème

**Exercice 9.1.1**

Écrivez trois fonctions `premierNombre`, `premiereChaine`, `premierBooleen` dupliquant la même logique, puis une version avec `any`, puis une version générique. Comparez la sûreté des trois.

**Exercice 9.1.2**

Expliquez pourquoi `function id(x: any): any` perd l'information de type entre l'entrée et la sortie, et comment un paramètre de type la conserve.

## 9.2 Fonctions génériques

**Exercice 9.2.1**

Écrivez `inverser<T>(tableau: T[]): T[]`, `dernier<T>(tableau: T[]): T | undefined`, `filtrer<T>(tableau: T[], predicat: (x: T) => boolean): T[]` et `mapper<T, U>(tableau: T[], f: (x: T) => U): U[]`.

**Exercice 9.2.2**

Quel est le type inféré de `T` pour `inverser([1, 2, 3])`, `inverser(["a", 1])`, `inverser([])` ? Quand faut-il préciser explicitement `inverser<number>(...)` ?

**Exercice 9.2.3**

Écrivez `fusionner<A, B>(a: A, b: B): A & B` avec `Object.assign`. Appelez-la avec deux objets littéraux.

**Exercice 9.2.4**

Écrivez `grouperPar<T, K extends PropertyKey>(valeurs: T[], cle: (v: T) => K): Record<K, T[]>` et utilisez-la sur une liste d'utilisateurs par rôle.

**Exercice 9.2.5**

Pourquoi `function f<T>(): T { return {} as T; }` est-il une mauvaise pratique ? Comment un paramètre de type qui n'apparaît qu'une fois est-il un signal d'alerte ?

## 9.3 Contraintes : `extends`

**Exercice 9.3.1**

Écrivez `longueur<T extends { length: number }>(x: T): number` et appelez-la avec une chaîne, un tableau, un objet `{ length: 3 }` et un nombre (erreur attendue).

**Exercice 9.3.2**

Écrivez `prop<T, K extends keyof T>(objet: T, cle: K): T[K]`. Quel est le type du résultat pour `prop({ a: 1, b: "x" }, "b")` ? Que se passe-t-il pour `"c"` ?

**Exercice 9.3.3**

Écrivez `plusGrand<T extends number | string>(a: T, b: T): T`. Pourquoi `plusGrand(1, "a")` est-il rejeté alors que T est contraint par une union ?

**Exercice 9.3.4**

Écrivez `fusionnerProps<T extends object, U extends object>(a: T, b: U): T & U`. Pourquoi contraindre à `object` plutôt qu'à `{}` ou `any` ?

**Exercice 9.3.5**

Écrivez une fonction générique `trier<T>(valeurs: T[], comparer: (a: T, b: T) => number): T[]` qui ne modifie pas le tableau d'origine. Ajoutez une version avec `T extends Comparable<T>` où `Comparable<T>` est une interface avec `compareA(autre: T): number`.

## 9.4 Interfaces et alias génériques

**Exercice 9.4.1**

Écrivez `interface Boite<T> { contenu: T }`, `type Resultat<T, E = Error>` et `interface ReponseApi<T> { statut: number; donnees: T }`. Utilisez-les avec différents types.

**Exercice 9.4.2**

Écrivez `interface Depot<T extends { id: number }>` avec `trouver(id: number): T | undefined`, `ajouter(element: T): void`, `lister(): T[]`.

**Exercice 9.4.3**

Écrivez un type `Pagination<T>` (`elements: T[]`, `page: number`, `total: number`) et une fonction qui le renvoie à partir d'un tableau.

**Exercice 9.4.4**

Écrivez un alias générique d'une fonction de rappel `Rappel<T> = (erreur: Error | null, donnees?: T) => void` et une version « promisifiée ».

## 9.5 Classes génériques

**Exercice 9.5.1**

Écrivez une classe générique `Pile<T>` avec `empiler`, `depiler`, `sommet`, `taille`. Utilisez-la avec `number` et avec `string`.

**Exercice 9.5.2**

Écrivez une classe générique `File<T>`, `Cache<K, V>` (avec limite de taille) et `EmetteurEvenements<Evts extends Record<string, unknown[]>>`.

**Exercice 9.5.3**

Écrivez une classe `Paire<A, B>` avec une méthode `echanger(): Paire<B, A>`.

**Exercice 9.5.4**

Pourquoi les membres statiques d'une classe générique ne peuvent-ils pas utiliser son paramètre de type ? Écrivez l'erreur obtenue.

**Exercice 9.5.5**

Écrivez une classe `ListeChainee<T>` avec une classe interne générique `Noeud<T>`, des méthodes `ajouter`, `supprimer`, `parcourir` (itérateur avec `[Symbol.iterator]`).

## 9.6 Valeurs par défaut des paramètres de type

**Exercice 9.6.1**

Écrivez `interface Reponse<T = unknown, E = Error>` et déclarez `Reponse` sans arguments, `Reponse<string>` et `Reponse<string, string>`.

**Exercice 9.6.2**

Quand une valeur par défaut est-elle utile (compatibilité ascendante d'une API publique, cas courant) ? Quel est l'ordre imposé entre paramètres avec et sans défaut ?

## 9.7 Paramètres de type `const` *(TS 5.0, ajout)*

**Exercice 9.7.1**

Écrivez `function creer<const T>(x: T): T` et appelez-la avec `creer({ a: [1, 2] })`. Comparez le type inféré avec la version sans `const`. *(TS 5.0)*

**Exercice 9.7.2**

Écrivez une fonction `routes<const T extends readonly string[]>(chemins: T): T` qui conserve les littéraux. Comparez avec `as const` à l'appel.

## 9.8 `NoInfer` *(TS 5.4, ajout)*

**Exercice 9.8.1**

Écrivez `function choisir<T extends string>(options: T[], defaut: T): T`. Quel type est inféré pour `choisir(["a", "b"], "c")` ? Corrigez avec `NoInfer<T>` pour que `"c"` soit refusé. *(TS 5.4)*

**Exercice 9.8.2**

Écrivez une fonction `creerMachine<E extends string>(etats: E[], initial: NoInfer<E>)`. Expliquez pourquoi `initial` ne doit pas participer à l'inférence. *(TS 5.4)*

## 9.9 Variance explicite *(ajout)*

**Exercice 9.9.1**

Définissez les termes covariance, contravariance, invariance. Donnez un exemple pour chacun (tableau en lecture seule, paramètre de fonction, référence modifiable).

**Exercice 9.9.2**

Utilisez les annotations `in` et `out` sur un paramètre de type d'une interface : `interface Producteur<out T>`, `interface Consommateur<in T>`, `interface Echange<in out T>`. Que vérifie le compilateur ?

**Exercice 9.9.3**

Pourquoi `Array<Chat>` est-il assignable à `Array<Animal>` en TypeScript, malgré les risques de `push` ? Écrivez le cas problématique.

## 9.10 Exemple concret : fonction de requête typée

**Exercice 9.10.1**

Écrivez `async function requete<T>(url: string): Promise<T>` qui appelle `fetch` et renvoie `response.json()` typé. Quel est le risque de cette approche (les types ne sont pas vérifiés à l'exécution) ? Ajoutez un paramètre « validateur » pour y remédier.

**Exercice 9.10.2**

Écrivez un client d'API typé : un objet décrivant les routes (`{ "/users": { reponse: Utilisateur[] }, "/users/:id": { reponse: Utilisateur } }`) et une fonction `get<R extends keyof Routes>(route: R): Promise<Routes[R]["reponse"]>`. *(défi)*

---

# 10. Modules et espaces de noms

## 10.1 Modules ES (la norme)

**Exercice 10.1.1**

Créez `maths.ts` qui exporte deux fonctions nommées, une constante et un export par défaut. Importez-les dans `main.ts` de toutes les façons : nommé, par défaut, renommé (`as`), en bloc (`* as`).

**Exercice 10.1.2**

Qu'est-ce qui fait d'un fichier un « module » aux yeux de TypeScript ? Que se passe-t-il pour un fichier sans `import` ni `export` (portée globale) ? Comment le transformer en module avec `export {}` ?

**Exercice 10.1.3**

Quelle différence entre un export nommé et un export par défaut ? Pourquoi la plupart des guides de style recommandent-ils les exports nommés ?

### Réexporter

**Exercice 10.1.4**

Créez un fichier `index.ts` (« barrel ») qui réexporte les symboles de plusieurs modules (`export * from`, `export { x } from`, `export { default as Y } from`). Quels sont les inconvénients des barrels (cycles, performances, arbre de dépendances) ?

### Imports de types : `verbatimModuleSyntax` *(à jour)*

**Exercice 10.1.5**

Écrivez `import type { Utilisateur } from "./types"` et `import { type Utilisateur, creer } from "./utilisateur"`. Quelle erreur avec `verbatimModuleSyntax` si l'on importe un type sans `type` ?

**Exercice 10.1.6**

Que génère le compilateur pour un `import` qui n'est utilisé que comme type, avec et sans `verbatimModuleSyntax` ? Pourquoi est-ce important pour les effets de bord à l'import ?

**Exercice 10.1.7**

Écrivez un `export type { ... }` et un `export type * from "./types"`. À quoi servent-ils ?

## 10.2 CommonJS et ES modules

**Exercice 10.2.1**

Dans Node.js, comment indiquer qu'un projet utilise ESM (`"type": "module"`, extension `.mjs`) ou CommonJS (`.cjs`) ? Que change-t-on dans `tsconfig.json` (`module`, `moduleResolution`) ?

**Exercice 10.2.2**

Écrivez un même module en CommonJS (`require`, `module.exports`) puis en ESM. Quelles sont les principales différences (liaisons dynamiques, `this`, `__dirname`, imports synchrones ou asynchrones) ?

**Exercice 10.2.3**

Avec `module: "nodenext"`, pourquoi doit-on écrire l'extension dans les chemins relatifs (`"./utils.js"`) même pour un fichier `utils.ts` ? Que fait `rewriteRelativeImportExtensions` ? *(TS 5.7)*

**Exercice 10.2.4**

Quel rôle jouent `esModuleInterop` et `allowSyntheticDefaultImports` ? Pourquoi sont-ils toujours actifs en TS 6 ?

**Exercice 10.2.5**

Depuis TS 5.8 et Node.js récent, un module CommonJS peut `require()` un module ES. Quelles restrictions subsistent (modules asynchrones avec `await` au niveau supérieur) ? *(TS 5.8)*

## 10.3 Importer du JSON et des ressources

**Exercice 10.3.1**

Importez un fichier `donnees.json` avec `resolveJsonModule` et la syntaxe `with { type: "json" }`. Quel est le type obtenu ? Pourquoi l'ancienne syntaxe `assert` est-elle dépréciée ?

**Exercice 10.3.2**

Déclarez dans un fichier `.d.ts` le type des modules `*.svg`, `*.css` et `*.png` (`declare module "*.svg"`) pour que leur import compile avec un bundler.

## 10.4 Espaces de noms (*namespaces*) : historique

**Exercice 10.4.1**

Écrivez un `namespace Geometrie` avec des fonctions exportées et une classe, puis utilisez-le. Quel code JavaScript est généré ?

**Exercice 10.4.2**

Réécrivez cet espace de noms sous forme de module ES. Pourquoi les modules sont-ils préférables ?

**Exercice 10.4.3**

Dans quels cas les `namespace` restent-ils utiles (fichiers de déclaration `.d.ts`, bibliothèques globales) ? Que fait `erasableSyntaxOnly` à leur sujet ?

**Exercice 10.4.4**

Quelle est la différence entre `module Nom {}` (déprécié) et `namespace Nom {}` ? Quelle version rend l'ancienne forme invalide ? *(TS 6.0)*

## 10.5 Imports dynamiques et chemins

**Exercice 10.5.1**

Écrivez un chargement paresseux avec `const m = await import("./lourd.js")`. Quel est le type de `m` ? Quand utiliser un import dynamique (division du code, chargement conditionnel) ?

**Exercice 10.5.2**

Configurez des alias de chemin dans `tsconfig.json` (`paths`) pour que `@/utils/format` désigne `src/utils/format`. Que faut-il configurer en plus dans le bundler ou le runtime ?

**Exercice 10.5.3**

Pourquoi les `paths` n'affectent-ils que la vérification de types et pas le JavaScript généré par `tsc` ? Citez deux solutions (plugin de bundler, `tsx`, imports de sous-chemins dans `package.json`).

**Exercice 10.5.4**

Utilisez les imports de sous-chemins Node.js (`"imports": { "#utils/*": "./src/utils/*" }`) et vérifiez qu'ils sont reconnus par TypeScript.

---

# 11. Types avancés

## 11.1 `keyof`, `typeof` et types indexés

**Exercice 11.1.1**

Pour `interface Utilisateur { id: number; nom: string; actif: boolean }`, calculez `keyof Utilisateur`, `Utilisateur["nom"]`, `Utilisateur["id" | "actif"]`, `Utilisateur[keyof Utilisateur]`.

**Exercice 11.1.2**

Utilisez `typeof` pour dériver un type à partir d'une valeur : `const config = { port: 3000, hote: "localhost" }; type Config = typeof config;`. Dérivez le type d'une fonction (`typeof maFonction`).

**Exercice 11.1.3**

Écrivez `type Element<T> = T extends readonly (infer E)[] ? E : never` d'abord sans `infer` avec `T[number]`. Utilisez-le avec un tableau et un tuple.

**Exercice 11.1.4**

Écrivez `type Cles<T> = keyof T` et `type Valeurs<T> = T[keyof T]`. Quel est le type de `keyof any` ? De `keyof string` ? De `keyof { [k: string]: number }` ?

**Exercice 11.1.5**

Écrivez `type DeepKeys<T>` qui calcule toutes les clés en notation pointée (`"a" | "a.b" | "a.c"`) d'un objet imbriqué. *(défi)*

## 11.2 Types mappés (*mapped types*)

**Exercice 11.2.1**

Écrivez vos propres versions de `Partial<T>`, `Required<T>`, `Readonly<T>` et `Pick<T, K>` avec des types mappés.

**Exercice 11.2.2**

Utilisez les modificateurs `+readonly`, `-readonly`, `+?` et `-?` pour écrire `Mutable<T>` (supprime `readonly`) et `Concret<T>` (supprime `?`).

**Exercice 11.2.3**

Écrivez un type `Getters<T>` qui transforme `{ nom: string; age: number }` en `{ getNom: () => string; getAge: () => number }` grâce au remappage de clés (`as`) et aux types de gabarit. *(TS 4.1)*

**Exercice 11.2.4**

Écrivez un type qui filtre les clés d'un objet selon le type de leur valeur : `PropsDeType<T, V>` ne garde que les propriétés dont la valeur est de type `V`. *(défi)*

**Exercice 11.2.5**

Écrivez `Nullable<T>` qui rend chaque propriété `T[K] | null`, puis `DeepReadonly<T>` qui est récursif.

**Exercice 11.2.6**

Écrivez un type mappé sur une union de chaînes : `{ [K in "a" | "b" | "c"]: number }`. Qu'est-ce qu'un type mappé homomorphe ?

## 11.3 Types conditionnels

**Exercice 11.3.1**

Écrivez `type EstChaine<T> = T extends string ? true : false` et évaluez-le pour `string`, `"a"`, `number`, `string | number`, `never`. Expliquez le résultat sur l'union (distributivité).

**Exercice 11.3.2**

Écrivez `type Exclure<T, U> = T extends U ? never : T` et `type Extraire<T, U> = T extends U ? T : never` (reproduisent `Exclude` et `Extract`). Appliquez-les à une union.

**Exercice 11.3.3**

Écrivez `type Aplatir<T> = T extends (infer U)[] ? U : T`. Que vaut `Aplatir<number[]>` ? `Aplatir<string>` ? `Aplatir<(string | number)[]>` ?

**Exercice 11.3.4**

Comment désactiver la distributivité (`[T] extends [U]`) ? Écrivez un exemple où cela change le résultat (par exemple pour tester si `T` est `never`).

**Exercice 11.3.5**

Écrivez `type EstUnion<T>` qui renvoie `true` si `T` est une union. *(défi)*

## 11.4 `infer` : extraire un type

**Exercice 11.4.1**

Écrivez vos propres versions de `ReturnType<T>`, `Parameters<T>`, `Awaited<T>`, `InstanceType<T>` avec `infer`.

**Exercice 11.4.2**

Écrivez `type PremierArgument<F>`, `type DernierElement<T extends unknown[]>` et `type SansPremier<T extends unknown[]>` avec `infer`.

**Exercice 11.4.3**

Écrivez un type qui extrait le type des éléments d'une `Promise<Promise<number>>` récursivement.

**Exercice 11.4.4**

Utilisez `infer` avec des contraintes (`infer U extends string`) pour analyser un type de gabarit. *(TS 4.7)*

## 11.5 Types littéraux de gabarit et manipulation de chaînes

**Exercice 11.5.1**

Écrivez `type Decouper<S extends string, D extends string>` qui transforme `"a,b,c"` en `["a", "b", "c"]` avec le séparateur `","`.

**Exercice 11.5.2**

Écrivez `type CamelVersSnake<S extends string>` qui convertit `"nomUtilisateur"` en `"nom_utilisateur"`, et son inverse. *(défi)*

**Exercice 11.5.3**

Écrivez un type `ParamsRoute<R extends string>` qui extrait les paramètres d'une route : `ParamsRoute<"/users/:id/posts/:postId">` donne `"id" | "postId"`.

**Exercice 11.5.4**

Écrivez `` type Evenements<T> = { [K in keyof T as `on${Capitalize<string & K>}Change`]: (valeur: T[K]) => void } `` et appliquez-le à `{ nom: string; age: number }`.

## 11.6 Types récursifs

**Exercice 11.6.1**

Écrivez le type `Json` : `string | number | boolean | null | Json[] | { [cle: string]: Json }`. Pourquoi ce type récursif est-il accepté ?

**Exercice 11.6.2**

Écrivez `Arbre<T>` (une feuille ou un nœud avec enfants) et une fonction générique `profondeur(arbre)`.

**Exercice 11.6.3**

Écrivez `DeepPartial<T>` et `DeepRequired<T>` récursifs. Que se passe-t-il avec les tableaux, les fonctions et les dates ?

**Exercice 11.6.4**

Écrivez un type récursif qui calcule la longueur d'un tuple ou qui produit un tuple de longueur `N` (`Repeter<T, N>`). *(défi)*

**Exercice 11.6.5**

Quelle limite de profondeur de récursion TypeScript applique-t-il aux types ? Quelle erreur obtient-on en cas de dépassement ?

## 11.7 `satisfies`, `as const` et inférence avancée

**Exercice 11.7.1**

Définissez un objet de configuration de routes avec `as const satisfies Routes`. Dérivez-en un type union des chemins. Quelle erreur détecte `satisfies` si une route est mal formée ?

**Exercice 11.7.2**

Écrivez un petit « DSL » typé : une fonction `definirEvenements` qui reçoit un objet et en infère les types d'arguments de chaque événement.

## 11.8 Gardes d'exhaustivité et types marqués (*branded types*) *(ajout)*

**Exercice 11.8.1**

Écrivez un type marqué : `type EuroEnCentimes = number & { readonly __marque: "euro" }` et `type DollarEnCentimes = ...`. Écrivez des fonctions de construction. Pourquoi une addition `Euro + Dollar` devient-elle une erreur ?

**Exercice 11.8.2**

Écrivez un type marqué générique `Marque<T, M extends string> = T & { readonly __marque: M }`, puis `IdUtilisateur`, `IdCommande` et une fonction `chercher(id: IdUtilisateur)`.

**Exercice 11.8.3**

Écrivez des fonctions de validation qui créent des types marqués (`email(valeur: string): Email | null`), pour qu'une fonction n'accepte que des chaînes déjà validées.

**Exercice 11.8.4**

Utilisez `unique symbol` pour créer une marque qui ne peut pas être contrefaite. Comparez avec l'approche par chaîne.

## 11.9 Conseils

**Exercice 11.9.1**

Listez cinq conseils pour des types avancés lisibles (nommer les étapes, tester avec des types d'exemple, limiter la récursion, documenter, préférer des types simples). Appliquez-les en refactorisant un type conditionnel imbriqué de votre choix.

**Exercice 11.9.2**

Écrivez des « tests de types » pour vos utilitaires (avec une fonction `Equal<A, B>` et `Expect<T extends true>`) et vérifiez les types de cet exercice. *(voir 23.5)*

---

# 12. Fichiers de déclaration de types

## 12.1 Qu'est-ce qu'un fichier `.d.ts` ?

**Exercice 12.1.1**

Écrivez le fichier `.d.ts` qui décrit un petit module JavaScript contenant `addition`, une classe et une constante. Quelle est la différence entre une déclaration et une implémentation ?

**Exercice 12.1.2**

Qu'est-ce que le mot-clé `declare` ? Écrivez `declare const`, `declare function`, `declare class`, `declare namespace`, `declare module`, `declare global`.

**Exercice 12.1.3**

Pourquoi un fichier `.d.ts` ne peut-il pas contenir du code exécutable ? Que se passe-t-il à la compilation d'un `.d.ts` ?

## 12.2 Générer des déclarations

**Exercice 12.2.1**

Activez `declaration` et `declarationMap` dans un projet, compilez-le, et examinez les `.d.ts` générés. Que fait `emitDeclarationOnly` ?

**Exercice 12.2.2**

Qu'apporte `isolatedDeclarations` ? Quelles annotations de type devient-on obligé d'écrire (type de retour des fonctions exportées) ? *(TS 5.5)*

**Exercice 12.2.3**

Dans le `package.json` d'une bibliothèque, remplissez les champs `types`, `exports` (avec conditions `types`, `import`, `require`), `files`. Pourquoi la condition `types` doit-elle venir en premier ?

## 12.3 DefinitelyTyped : `@types`

**Exercice 12.3.1**

Installez `@types/node` et `@types/express` pour un projet. Que changent-ils dans l'éditeur ? Pourquoi sont-ils des dépendances de développement ?

**Exercice 12.3.2**

Comment savoir si un paquet fournit ses propres types (champ `types`/`typings` dans son `package.json`) ou s'il faut installer `@types/...` ? Vérifiez pour `lodash`, `zod` et `axios`.

**Exercice 12.3.3**

Avec `types: []` par défaut depuis TS 6.0, comment faire voir `@types/node` ou les globales de test (`describe`, `it`) ? Écrivez la configuration correspondante. *(TS 6.0)*

## 12.4 Où TypeScript cherche-t-il les types ?

**Exercice 12.4.1**

Décrivez l'ordre dans lequel TypeScript cherche les types d'un module importé : fichiers `.ts`, `.d.ts`, champ `types` du `package.json`, `@types`, déclarations ambiantes. Utilisez `tsc --traceResolution` pour le vérifier.

**Exercice 12.4.2**

Que fait l'option `typeRoots` ? Que fait `types` ? Quelle différence entre les deux ?

## 12.5 Écrire ses propres déclarations

### Module sans types

**Exercice 12.5.1**

Importez un module JavaScript sans types et corrigez l'erreur « implicitement de type any » avec `declare module "nom-du-module";`. Puis écrivez des déclarations plus précises.

**Exercice 12.5.2**

Écrivez les déclarations complètes d'une petite bibliothèque JavaScript de votre choix (une fonction par défaut, deux fonctions nommées, une interface d'options).

**Exercice 12.5.3**

Écrivez les déclarations d'une bibliothèque qui exporte par `module.exports = fonction` (`export =`) et une qui expose à la fois un module et une variable globale (UMD).

### Variables et fonctions globales

**Exercice 12.5.4**

Déclarez une variable globale `VERSION_APP` injectée par un bundler et une fonction globale `journaliser(message: string)`. Dans quel fichier placez-vous ces déclarations ?

**Exercice 12.5.5**

Quelle est la différence entre un fichier `.d.ts` « global » et un fichier « module » ? Comment faire une déclaration globale à l'intérieur d'un module avec `declare global { ... }` ?

### Étendre les types d'une bibliothèque (*module augmentation*)

**Exercice 12.5.6**

Ajoutez une propriété `utilisateur` à l'interface `Request` d'Express par augmentation de module. Quelles précautions de configuration (`include`, `files`) pour que la déclaration soit prise en compte ?

**Exercice 12.5.7**

Ajoutez une méthode `Array.prototype.somme` : déclaration dans une augmentation globale, implémentation à l'exécution. Pourquoi est-il déconseillé de modifier les prototypes natifs ?

## 12.6 Configuration

**Exercice 12.6.1**

Quelles options du `tsconfig.json` concernent les fichiers de déclaration (`include`, `files`, `typeRoots`, `types`, `skipLibCheck`, `declaration`) ? Pour chacune, décrivez en une phrase son rôle.

**Exercice 12.6.2**

Pourquoi `skipLibCheck: true` accélère-t-il la compilation et quels risques comporte-t-il ?

## 12.7 Conseils

**Exercice 12.7.1**

Listez cinq conseils pour les fichiers de déclaration (préférer les types fournis, déclarer au plus précis, tester les déclarations, ne pas utiliser `any` partout, contribuer à DefinitelyTyped).

**Exercice 12.7.2**

Écrivez un test de déclaration pour la bibliothèque de l'exercice 12.5.2 avec `// @ts-expect-error` pour les appels invalides.

---

# Niveau avancé

---

# 13. Types utilitaires

## 13.1 Les types intégrés

**Exercice 13.1.1**

Pour `interface Utilisateur { id: number; nom: string; email: string; admin: boolean }`, calculez à la main puis vérifiez dans l'éditeur : `Partial<Utilisateur>`, `Required<Utilisateur>`, `Readonly<Utilisateur>`, `Pick<Utilisateur, "id" | "nom">`, `Omit<Utilisateur, "email">`, `Record<"a" | "b", number>`.

**Exercice 13.1.2**

Calculez : `Exclude<"a" | "b" | "c", "a">`, `Extract<string | number | (() => void), Function>`, `NonNullable<string | null | undefined>`.

**Exercice 13.1.3**

Calculez : `ReturnType<typeof f>`, `Parameters<typeof f>`, `ConstructorParameters<typeof Date>`, `InstanceType<typeof Date>`, `Awaited<Promise<Promise<string>>>` pour une fonction `f(a: number, b: string): boolean` de votre choix.

**Exercice 13.1.4**

À quoi servent `Uppercase`, `Lowercase`, `Capitalize`, `Uncapitalize`, `ThisType`, `NoInfer`, `ReadonlyArray`, `ReadonlyMap`, `ReadonlySet`, `PromiseLike` ? Donnez un exemple de chacun.

**Exercice 13.1.5**

Quelle est la différence entre `Omit<T, K>` et `Exclude<keyof T, K>` ? Pourquoi `Omit` accepte-t-il des clés qui n'existent pas ?

## 13.2 Combiner des utilitaires

**Exercice 13.2.1**

Écrivez `type MiseAJour<T extends { id: number }> = Partial<Omit<T, "id">> & Pick<T, "id">`. Appliquez-le à `Utilisateur`.

**Exercice 13.2.2**

Écrivez `type CreationUtilisateur = Omit<Utilisateur, "id" | "creeLe">` et `type VueUtilisateur = Readonly<Pick<Utilisateur, "id" | "nom">>`.

**Exercice 13.2.3**

Écrivez `type ValeursDe<T> = T[keyof T]`, `type Rendre<T, K extends keyof T> = Omit<T, K> & Required<Pick<T, K>>` et `type ModifierPropriete<T, K extends keyof T, V> = Omit<T, K> & { [P in K]: V }`.

**Exercice 13.2.4**

Quelle difficulté posent les types d'intersection obtenus (lisibilité dans l'infobulle) ? Comment les « aplatir » avec `type Aplatir<T> = { [K in keyof T]: T[K] } & {}` ?

## 13.3 Cas d'usage

**Exercice 13.3.1**

Écrivez un type `FormulaireEtat<T>` qui, pour chaque champ de `T`, associe `{ valeur: T[K]; erreur?: string; modifie: boolean }`.

**Exercice 13.3.2**

Écrivez les types de l'API d'un service CRUD : `Creer<T>`, `MettreAJour<T>`, `Lire<T>`, `Supprimer`, à partir d'une entité `T` avec `id`.

**Exercice 13.3.3**

Écrivez le type de retour d'une fonction qui reçoit un objet de configuration et renvoie un objet « résolu » (toutes les options facultatives remplacées par leurs valeurs par défaut) : `Resolu<Options, Defauts>`.

**Exercice 13.3.4**

Typez un objet de traductions : `Record<Langue, Record<CleTraduction, string>>` avec `Langue = "fr" | "en"`. Quelle erreur obtient-on si une clé manque dans l'une des langues ?

## 13.4 Écrire ses propres utilitaires

**Exercice 13.4.1**

Écrivez `Modifiable<T>` (retire `readonly`), `ProprietesFonctions<T>` (clés dont la valeur est une fonction), `Sans<T, V>` (retire les clés dont la valeur est `V`), `Unifier<U>` (union en intersection). *(défi pour le dernier)*

**Exercice 13.4.2**

Écrivez `Egaux<A, B>` (type de test d'égalité stricte) et utilisez-le pour vérifier vos types avec `type _ = Expect<Egaux<Modifiable<{ readonly a: 1 }>, { a: 1 }>>`.

**Exercice 13.4.3**

Résolvez cinq défis du dépôt *Type Challenges* de niveau facile ou moyen (`Pick`, `Readonly`, `First`, `Length`, `Exclude`) et notez vos solutions.

---

# 14. Décorateurs

## 14.1 Deux versions à connaître *(à jour)*

**Exercice 14.1.1**

Complétez le tableau : décorateurs standard (TS 5.x, ECMAScript) et décorateurs expérimentaux (`experimentalDecorators`) : option de configuration, signatures, métadonnées, paramètres décorables, usage dans Angular et NestJS.

**Exercice 14.1.2**

Comment savoir quelle version de décorateurs votre projet utilise ? Que se passe-t-il si l'on active `experimentalDecorators` ? Quelle est la position de TypeScript sur son avenir ?

## 14.2 Décorateurs standard (TS 5.x)

### Décorateur de classe

**Exercice 14.2.1**

Écrivez un décorateur de classe `@journalise` qui affiche un message à la création de chaque instance (en retournant une sous-classe). Utilisez le type `ClassDecoratorContext`. *(TS 5.0)*

**Exercice 14.2.2**

Écrivez un décorateur de classe `@scelle` qui appelle `Object.seal` sur le constructeur et son prototype.

### Décorateur de méthode

**Exercice 14.2.3**

Écrivez un décorateur de méthode `@chronometre` qui mesure et affiche le temps d'exécution. Typez-le avec `ClassMethodDecoratorContext`. Vérifiez la conservation de `this`.

**Exercice 14.2.4**

Écrivez un décorateur paramétré `@reessayer(n)` qui relance une méthode asynchrone `n` fois en cas d'échec.

**Exercice 14.2.5**

Écrivez un décorateur `@memoiser` qui met en cache le résultat d'une méthode en fonction de ses arguments (clé JSON).

**Exercice 14.2.6**

Écrivez un décorateur `@lier` (équivalent de `bind`) en utilisant `context.addInitializer`. À quel moment l'initialiseur est-il exécuté ?

### Décorateur de champ et `accessor`

**Exercice 14.2.7**

Écrivez un décorateur de champ `@valeurParDefaut(x)` (qui renvoie une fonction d'initialisation) et un décorateur sur `accessor` qui valide toute affectation (`@positif`).

**Exercice 14.2.8**

Écrivez un décorateur `@observable` sur un `accessor` qui notifie des abonnés à chaque modification.

### Contexte et initialiseurs

**Exercice 14.2.9**

Affichez le contenu de l'objet `context` (`kind`, `name`, `static`, `private`, `access`, `metadata`) dans un décorateur appliqué à chaque sorte de membre. Remplissez un tableau récapitulatif.

**Exercice 14.2.10**

Utilisez `Symbol.metadata` et `context.metadata` pour associer des informations à une classe (par exemple, la liste des champs à valider). *(défi)*

## 14.3 Décorateurs expérimentaux (hérités)

**Exercice 14.3.1**

Activez `experimentalDecorators` et écrivez un décorateur de classe, de méthode, de propriété et de paramètre avec la signature historique. Comparez avec la version standard.

**Exercice 14.3.2**

Qu'est-ce que `emitDecoratorMetadata` et `reflect-metadata` ? Pourquoi NestJS et Angular en dépendent-ils pour l'injection de dépendances ?

**Exercice 14.3.3**

Migrez un décorateur de méthode expérimental vers la version standard : quelles sont les différences de signature et de comportement ?

## 14.4 Cas d'usage

**Exercice 14.4.1**

Décrivez trois cas d'usage typiques (journalisation, validation, injection de dépendances, routage, cache, autorisation). Pour chacun, écrivez un exemple de décorateur de dix lignes.

**Exercice 14.4.2**

Écrivez un décorateur `@autorise("admin")` pour une méthode qui lève une erreur si l'utilisateur courant n'a pas le rôle requis.

**Exercice 14.4.3**

Écrivez un mini-framework de routage où `@route("GET", "/chemin")` enregistre une méthode dans une table, puis un « routeur » qui appelle la méthode correspondante.

## 14.5 Bonnes pratiques

**Exercice 14.5.1**

Listez cinq bonnes pratiques pour les décorateurs (rester simples, typer le contexte, éviter la magie, documenter, tester) et leurs pièges (ordre d'évaluation et d'application, interférence avec `this`).

**Exercice 14.5.2**

Quand plusieurs décorateurs sont empilés (`@a @b méthode()`), dans quel ordre sont-ils évalués et appliqués ? Écrivez un exemple qui l'affiche.

---

# 15. Programmation asynchrone

## 15.1 Promesses typées

**Exercice 15.1.1**

Écrivez une fonction `attendre(ms: number): Promise<void>` et `chargerUtilisateur(id: number): Promise<Utilisateur>` qui simule un délai.

**Exercice 15.1.2**

Écrivez `new Promise<number>((resolve, reject) => ...)` qui se résout après un délai ou se rejette. Pourquoi faut-il préciser le paramètre de type ?

**Exercice 15.1.3**

Quel est le type de `p.then(x => x.length)` si `p: Promise<string>` ? Chaînez trois `.then` en suivant les types, puis un `.catch` et un `.finally`.

**Exercice 15.1.4**

Convertissez une fonction à rappel `lire(chemin, (err, data) => ...)` en promesse (`promisifier`). Typez correctement `util.promisify`.

## 15.2 `async` / `await`

**Exercice 15.2.1**

Réécrivez avec `async`/`await` une chaîne de trois `.then`. Quel est le type de retour d'une fonction `async` qui renvoie un nombre ?

**Exercice 15.2.2**

Écrivez `async function afficher(): Promise<void>` qui attend le résultat de deux fonctions asynchrones l'une après l'autre. Comparez avec leur exécution parallèle (15.4).

**Exercice 15.2.3**

Que se passe-t-il si on oublie `await` devant un appel asynchrone ? Quelle règle ESLint (`no-floating-promises`) détecte l'oubli ? Que se passe-t-il à la compilation pour `if (verifier())` où `verifier` est asynchrone ?

**Exercice 15.2.4**

Utilisez l'`await` au niveau supérieur d'un module ES. Quelles options (`module`, `target`) l'autorisent ?

**Exercice 15.2.5**

Écrivez une boucle `for await...of` sur un générateur asynchrone `async function*` qui produit des pages de résultats.

## 15.3 Gérer les erreurs : `unknown`

**Exercice 15.3.1**

Pourquoi, avec `useUnknownInCatchVariables`, le paramètre d'un `catch` est-il de type `unknown` ? Écrivez le bloc `catch` qui restreint l'erreur (`instanceof Error`) pour afficher son message.

**Exercice 15.3.2**

Écrivez une fonction `messageErreur(e: unknown): string` qui gère `Error`, `string`, objets avec `message` et autres valeurs.

**Exercice 15.3.3**

Écrivez des classes d'erreur personnalisées (`ErreurHttp` avec `statut`, `ErreurValidation`) en étendant `Error`. Pourquoi faut-il parfois appeler `Object.setPrototypeOf` en cibles anciennes ? Utilisez l'option `cause`.

### Le motif « résultat » plutôt que les exceptions (option)

**Exercice 15.3.4**

Définissez `type Resultat<T, E> = { ok: true; valeur: T } | { ok: false; erreur: E }` et écrivez `essayer<T>(f: () => Promise<T>): Promise<Resultat<T, Error>>`. Utilisez-le pour éviter les `try/catch` imbriqués.

**Exercice 15.3.5**

Écrivez des fonctions `ok`, `erreur`, `mapper`, `chaine` sur ce type `Resultat`. Comparez ce style au chaînage d'exceptions.

## 15.4 Exécution parallèle

**Exercice 15.4.1**

Utilisez `Promise.all` pour charger en parallèle un utilisateur, ses commandes et ses messages. Quel est le type inféré du résultat (tuple) ? Que se passe-t-il si l'une des promesses échoue ?

**Exercice 15.4.2**

Comparez `Promise.all`, `Promise.allSettled`, `Promise.race` et `Promise.any` avec trois promesses de durées et d'états différents. Quels sont les types des résultats ?

**Exercice 15.4.3**

Écrivez `limiterConcurrence<T>(taches: (() => Promise<T>)[], limite: number): Promise<T[]>` qui exécute au plus `limite` tâches simultanées. *(défi)*

**Exercice 15.4.4**

Écrivez `reessayer<T>(f: () => Promise<T>, tentatives: number, delai: number)` avec attente exponentielle.

## 15.5 Annulation et délai d'expiration

**Exercice 15.5.1**

Utilisez `AbortController` et `AbortSignal` pour annuler un `fetch`. Utilisez `AbortSignal.timeout(ms)` pour un délai maximal. Gérez l'erreur `AbortError`.

**Exercice 15.5.2**

Écrivez `avecDelai<T>(promesse: Promise<T>, ms: number): Promise<T>` avec `Promise.race`.

**Exercice 15.5.3**

Écrivez une fonction de recherche « avec anti-rebond » (*debounce*) qui annule la requête précédente à chaque nouvelle frappe.

## 15.6 Typer les API asynchrones

**Exercice 15.6.1**

Écrivez un client `fetch` typé : `async function appeler<T>(url: string, options?: RequestInit): Promise<T>` qui vérifie `response.ok` et lève `ErreurHttp`. Utilisez-le avec une interface de réponse.

**Exercice 15.6.2**

Ajoutez une validation à l'exécution avec un schéma (par exemple Zod) pour que le type de la réponse soit vérifié, pas seulement affirmé. Comparez le code avec et sans validation.

**Exercice 15.6.3**

Écrivez un type `AsyncFunction<A extends unknown[], R> = (...args: A) => Promise<R>` et `Promisifie<T>` qui transforme toutes les méthodes d'un objet en versions asynchrones.

## 15.7 Rappels (*callbacks*) et événements typés

**Exercice 15.7.1**

Écrivez un émetteur d'événements typé `Emetteur<Evts>` avec `on`, `off`, `emit` où le nom de l'événement détermine le type des arguments.

**Exercice 15.7.2**

Utilisez la classe `EventEmitter` de Node.js avec les types génériques (`EventEmitter<{ message: [string]; fin: [] }>`) pour typer les événements.

**Exercice 15.7.3**

Convertissez un émetteur d'événements en promesse (`once`) et en itérateur asynchrone (`on` de `node:events`).

## 15.8 Programmation réactive avec RxJS

**Exercice 15.8.1**

Créez un `Observable<number>` qui émet toutes les secondes. Appliquez `map`, `filter`, `take` et abonnez-vous. Quel est le type de chaque étape du `pipe` ?

**Exercice 15.8.2**

Écrivez une recherche avec `debounceTime`, `distinctUntilChanged` et `switchMap` (saisie utilisateur vers requête HTTP typée). Pourquoi `switchMap` est-il préférable à `mergeMap` ici ?

**Exercice 15.8.3**

Comparez `Promise` et `Observable` (valeurs multiples, annulation, paresse). Convertissez l'un en l'autre.

## 15.9 Bonnes pratiques

**Exercice 15.9.1**

Listez cinq bonnes pratiques asynchrones (toujours gérer les rejets, paralléliser quand c'est possible, typer les erreurs en `unknown`, annulation, ne pas mélanger `then` et `await`) et illustrez chacune par un contre-exemple corrigé.

---

# 16. Manipuler le DOM

## 16.1 Typer les éléments

**Exercice 16.1.1**

Quel est le type de `document.querySelector("div")`, de `document.querySelector(".classe")`, de `document.getElementById("x")`, de `document.createElement("input")` ? Pourquoi les types diffèrent-ils selon le sélecteur ?

**Exercice 16.1.2**

Écrivez `const champ = document.querySelector<HTMLInputElement>("#nom")` et lisez `champ.value`. Quelle est la différence avec une assertion `as` ?

**Exercice 16.1.3**

Associez chaque élément à son interface : `<a>`, `<button>`, `<input>`, `<form>`, `<canvas>`, `<img>`, `<select>`, `<textarea>`, `<video>`.

**Exercice 16.1.4**

Écrivez une fonction `$<T extends HTMLElement>(sélecteur: string): T` qui lève une erreur claire si l'élément est introuvable.

**Exercice 16.1.5**

Quelles bibliothèques de types (`lib`) faut-il activer pour `document` et `window` (`"dom"`, `"dom.iterable"`) ? Que se passe-t-il dans un projet Node.js sans ces bibliothèques ?

## 16.2 Gestion de la valeur `null`

**Exercice 16.2.1**

Pourquoi `document.getElementById("x")` renvoie-t-il `HTMLElement | null` ? Écrivez trois façons d'utiliser le résultat : test explicite, chaînage optionnel, fonction d'assertion.

**Exercice 16.2.2**

Quand utiliser `!` ou `as` pour un élément dont on est certain de l'existence ? Quels sont les risques si le HTML change ?

**Exercice 16.2.3**

Écrivez `function requis<T extends Element>(el: T | null, nom: string): T` qui lève une erreur parlante.

## 16.3 Événements typés

**Exercice 16.3.1**

Écrivez un gestionnaire `click` sur un bouton avec un paramètre `MouseEvent`. Pourquoi `addEventListener("click", ...)` infère-t-il automatiquement le type de l'événement ?

**Exercice 16.3.2**

Écrivez un gestionnaire d'événement `input` sur un champ texte qui lit `event.target.value`. Pourquoi `event.target` est-il de type `EventTarget | null` et non `HTMLInputElement` ? Utilisez `event.currentTarget`.

**Exercice 16.3.3**

Écrivez un gestionnaire `submit` de formulaire qui appelle `preventDefault()` et lit les champs avec `FormData`.

**Exercice 16.3.4**

Écrivez un gestionnaire `keydown` qui réagit aux touches `Enter` et `Escape` (`KeyboardEvent`). Quel est le type de `event.key` ?

**Exercice 16.3.5**

Écrivez la délégation d'événements : un seul gestionnaire `click` sur une liste `<ul>` qui identifie l'élément `<li>` cliqué avec `closest`.

**Exercice 16.3.6**

Écrivez des gestionnaires pour `drag`/`drop`, `touchstart`, `scroll` et `resize`. Utilisez l'option `{ passive: true }` et `AbortSignal` pour retirer plusieurs écouteurs d'un coup.

## 16.4 Événements personnalisés typés

**Exercice 16.4.1**

Déclarez dans `HTMLElementEventMap` un événement `"panier:ajout"` de type `CustomEvent<{ id: number }>` (augmentation d'interface). Émettez-le avec `dispatchEvent` et écoutez-le avec un type correct.

**Exercice 16.4.2**

Écrivez un petit bus d'événements pour des composants sans framework, typé par une table d'événements.

## 16.5 Créer et modifier des éléments

**Exercice 16.5.1**

Créez dynamiquement une liste d'éléments à partir d'un tableau d'objets typés : `createElement`, `textContent`, `classList.add`, `appendChild`/`append`, `dataset`.

**Exercice 16.5.2**

Pourquoi faut-il préférer `textContent` à `innerHTML` pour insérer du texte venant d'un utilisateur (faille XSS) ? Écrivez un exemple de contenu malveillant et la parade.

**Exercice 16.5.3**

Écrivez une fonction `h<K extends keyof HTMLElementTagNameMap>(tag: K, props?: Partial<HTMLElementTagNameMap[K]>, ...enfants)` qui crée un élément typé. *(défi)*

**Exercice 16.5.4**

Utilisez `template` et `cloneNode`, ou `insertAdjacentHTML`, pour insérer du HTML. Quelles précautions de sécurité ?

## 16.6 Observateurs et API du navigateur

**Exercice 16.6.1**

Utilisez `IntersectionObserver` pour charger des images paresseusement. Typez le rappel `(entries: IntersectionObserverEntry[]) => void`.

**Exercice 16.6.2**

Utilisez `MutationObserver` et `ResizeObserver` pour réagir aux changements d'un élément. Quand déconnecter l'observateur ?

**Exercice 16.6.3**

Utilisez `localStorage` avec des types : écrivez `lireStockage<T>(cle: string): T | null` et `ecrireStockage<T>(cle: string, valeur: T)` avec sérialisation JSON et validation.

**Exercice 16.6.4**

Utilisez l'API `fetch`, `URL`, `URLSearchParams`, `history.pushState` et `navigator.clipboard` avec des types.

## 16.7 Bonnes pratiques

**Exercice 16.7.1**

Listez cinq bonnes pratiques DOM en TypeScript (types précis des sélecteurs, test de `null`, délégation, `textContent`, nettoyage des écouteurs) et illustrez chacune.

**Exercice 16.7.2**

Mini-projet : une liste de tâches sans framework (ajout, suppression, filtrage, persistance dans `localStorage`) entièrement typée, sans `any` ni assertion non justifiée.

---

# 17. Mixins et composition

## 17.1 Pourquoi ?

**Exercice 17.1.1**

Expliquez le « problème du diamant » et la limite de l'héritage simple en JavaScript. Dans quels cas souhaite-t-on réutiliser des comportements issus de plusieurs sources ?

**Exercice 17.1.2**

Comparez trois approches pour partager un comportement (journalisation, horodatage) entre des classes sans lien : héritage, mixin, composition.

## 17.2 Mixins de classes

**Exercice 17.2.1**

Écrivez un type `Constructeur<T = {}> = new (...args: any[]) => T` et un mixin `Horodate` qui ajoute `creeLe` et `touche()` à n'importe quelle classe. Appliquez-le à une classe `Document`.

**Exercice 17.2.2**

Écrivez un mixin `Journalise` qui ajoute une méthode `journaliser(message)` et un mixin `Activable` qui ajoute `actif` et `activer()`. Composez-les : `class Service extends Journalise(Activable(Base)) {}`. Quel est le type de `Service` ?

**Exercice 17.2.3**

Pourquoi le constructeur d'un mixin doit-il avoir la signature `(...args: any[])` ? Que se passe-t-il pour une classe de base avec des paramètres de constructeur précis ?

**Exercice 17.2.4**

Écrivez un utilitaire `appliquerMixins(classeCible, ...sources)` à l'ancienne (copie des propriétés du prototype) et son type. Comparez avec les mixins par fonction.

## 17.3 Mixins avec contraintes

**Exercice 17.3.1**

Écrivez un mixin qui exige que la classe de base possède une propriété `id: string` (`Constructeur<{ id: string }>`) et utilise cette propriété. Montrez l'erreur quand la base ne la possède pas.

**Exercice 17.3.2**

Écrivez un mixin `AvecEvenements` dont les types d'événements dépendent de la classe qu'il enrichit. *(défi)*

**Exercice 17.3.3**

Les membres `private` et `protected` sont-ils permis dans la classe retournée par un mixin ? Essayez avec `declaration` activé et notez l'erreur éventuelle.

## 17.4 Composition par objets et fonctions

**Exercice 17.4.1**

Écrivez des fonctions « capacités » (`peutVoler`, `peutNager`) qui renvoient des objets de méthodes, puis composez-les par déploiement d'objet (`{ ...a, ...b }`) pour créer un `Canard`. Typez le résultat avec une intersection.

**Exercice 17.4.2**

Écrivez une fabrique `creerRobot(nom: string)` qui combine des comportements par composition et ne dépend d'aucune classe.

**Exercice 17.4.3**

Écrivez `pipe` et `compose` génériques à trois fonctions avec des types qui s'enchaînent. *(défi)*

### Composition par délégation (injection)

**Exercice 17.4.4**

Écrivez une classe `Commande` qui reçoit dans son constructeur un `Logger` et un `Paiement` (interfaces). Écrivez deux implémentations de `Paiement` (réelle et factice) pour les tests.

**Exercice 17.4.5**

Écrivez un petit conteneur d'injection de dépendances manuel : une table qui associe un identifiant à une fabrique, avec un typage fort des identifiants et des types résolus.

## 17.5 Pièges

**Exercice 17.5.1**

Reproduisez les pièges des mixins (ordre d'application, collisions de noms, `instanceof` qui échoue, types difficiles à lire) et notez pour chacun la parade.

**Exercice 17.5.2**

Écrivez deux mixins qui définissent la même méthode `decrire()` et montrez laquelle l'emporte selon l'ordre de composition. Comment appeler les deux via `super` ?

## 17.6 Mixins ou composition ?

**Exercice 17.6.1**

Pour chacune des situations suivantes, choisissez héritage, mixin ou composition et justifiez : plusieurs services partageant la journalisation, un jeu avec des entités cumulant des capacités, un composant d'interface utilisateur, un modèle de domaine.

**Exercice 17.6.2**

Refactorisez une hiérarchie de classes profonde (`Animal` → `AnimalTerrestre` → `Mammifere` → `Chien`) vers une conception par composition de capacités.

---

# 18. TypeScript et frameworks front-end

## 18.1 Démarrer un projet : **Vite**

**Exercice 18.1.1**

Créez un projet avec `npm create vite@latest` en choisissant un modèle TypeScript (vanilla, React, Vue). Examinez `package.json`, `tsconfig.json` (et `tsconfig.app.json` / `tsconfig.node.json`), `vite.config.ts` et `index.html`.

**Exercice 18.1.2**

Pourquoi Vite lance-t-il le serveur de développement sans vérifier les types ? Quel script ajouter pour vérifier les types en parallèle (`tsc --noEmit --watch`) et quel script en CI ?

**Exercice 18.1.3**

Ajoutez un alias de chemin `@` dans `tsconfig.app.json` (`paths`) et dans `vite.config.ts` (`resolve.alias`). Que se passe-t-il si l'on oublie l'un des deux ?

**Exercice 18.1.4**

Typez les variables d'environnement de Vite : déclarez `interface ImportMetaEnv` dans `vite-env.d.ts` pour `VITE_API_URL`. Pourquoi seules les variables préfixées par `VITE_` sont-elles exposées au navigateur ?

## 18.2 React

### Composants et props

**Exercice 18.2.1**

Écrivez un composant fonction `Bonjour` avec une interface de props (`nom: string`, `enfants?: ReactNode`). Quelle différence entre annoter les props directement et utiliser `React.FC` ?

**Exercice 18.2.2**

Écrivez un composant `Bouton` qui accepte toutes les props d'un `<button>` natif (`ComponentPropsWithoutRef<"button">`) plus une prop `variante: "primaire" | "secondaire"`.

**Exercice 18.2.3**

Typez des props d'un composant avec des variantes exclusives par union discriminée : un composant `Alerte` qui accepte soit `{ type: "lien"; href: string }`, soit `{ type: "bouton"; onClick: () => void }`.

**Exercice 18.2.4**

Écrivez le typage d'un composant qui accepte une prop `render: (item: T) => ReactNode` (props de rendu) et un `as` polymorphe (`as?: ElementType`).

**Exercice 18.2.5**

Typez un gestionnaire d'événement : `onChange` d'un `<input>` (`ChangeEvent<HTMLInputElement>`), `onSubmit` d'un formulaire (`FormEvent<HTMLFormElement>`), `onClick` (`MouseEvent<HTMLButtonElement>`).

### Hooks

**Exercice 18.2.6**

Typez `useState` pour : un nombre, une chaîne, un objet, une valeur `null` au départ (`useState<Utilisateur | null>(null)`), un tableau initialement vide. Pourquoi faut-il parfois préciser le type générique ?

**Exercice 18.2.7**

Typez `useRef` pour un élément DOM (`useRef<HTMLInputElement>(null)`) et pour une valeur modifiable. Quelle différence entre `RefObject` et `MutableRefObject` ? Comment la gère React 19 ?

**Exercice 18.2.8**

Écrivez un hook personnalisé générique `useFetch<T>(url: string)` qui renvoie `{ donnees: T | null; erreur: Error | null; chargement: boolean }` (ou une union discriminée).

**Exercice 18.2.9**

Écrivez le hook `useLocalStorage<T>(cle: string, initial: T): [T, (v: T) => void]`. Typez `useCallback`, `useMemo` et `useContext` (avec un contexte dont la valeur par défaut est `null`).

### Composants génériques et `useReducer`

**Exercice 18.2.10**

Écrivez un composant générique `Liste<T>` qui reçoit `elements: T[]`, `cle: (e: T) => string` et `rendu: (e: T) => ReactNode`. Utilisez-le avec deux types différents.

**Exercice 18.2.11**

Écrivez un `useReducer` typé avec une union discriminée d'actions (`ajouter`, `supprimer`, `basculer`) pour une liste de tâches. Ajoutez la vérification d'exhaustivité du réducteur.

**Exercice 18.2.12**

Typez un composant de formulaire générique `Champ<T extends keyof Valeurs>` qui associe un nom de champ au type de sa valeur.

**Exercice 18.2.13**

Typez un contexte React avec un hook d'accès qui lève une erreur si le fournisseur est absent, pour éviter `null` dans tous les composants consommateurs.

## 18.3 Angular

**Exercice 18.3.1**

Écrivez un composant Angular autonome avec `@Component`, une propriété typée, une méthode et un gabarit. Pourquoi Angular dépend-il de décorateurs et de métadonnées ?

**Exercice 18.3.2**

Écrivez un service injectable (`@Injectable({ providedIn: "root" })`) qui utilise `HttpClient` pour renvoyer un `Observable<Utilisateur[]>`. Consommez-le avec `async` ou `toSignal`.

**Exercice 18.3.3**

Utilisez les signaux typés (`signal<number>`, `computed`, `effect`) et les entrées/sorties basées sur des fonctions (`input<string>()`, `output<number>()`, `model<boolean>()`). Comparez avec les décorateurs `@Input()` et `@Output()`.

**Exercice 18.3.4**

Typez un formulaire réactif (`FormGroup<{ nom: FormControl<string>; age: FormControl<number | null> }>`). Pourquoi les formulaires sont-ils fortement typés depuis Angular 14 ?

**Exercice 18.3.5**

Pourquoi la vérification stricte des gabarits (`strictTemplates`) est-elle recommandée ? Quel type d'erreur détecte-t-elle ?

## 18.4 Vue

**Exercice 18.4.1**

Écrivez un composant avec `<script setup lang="ts">` : props typées avec `defineProps<{ titre: string; compte?: number }>()`, événements avec `defineEmits<{ (e: "valider", valeur: string): void }>()`, valeurs par défaut avec `withDefaults`.

**Exercice 18.4.2**

Typez `ref<number>(0)`, `ref<Utilisateur | null>(null)`, `reactive<{ ... }>()`, `computed(() => ...)` et `useTemplateRef`. Quelle différence de typage entre `ref` et `reactive` ?

**Exercice 18.4.3**

Écrivez un composable typé (`useCompteur`) qui renvoie un objet `{ valeur, incrementer }`. Utilisez `provide`/`inject` avec une clé typée (`InjectionKey<T>`).

**Exercice 18.4.4**

Quels outils vérifient les types des fichiers `.vue` (`vue-tsc`, extension Volar) ? Pourquoi `tsc` seul ne suffit-il pas ?

## 18.5 Autres frameworks

**Exercice 18.5.1**

Écrivez un petit composant TypeScript dans Svelte (`<script lang="ts">`), dans Solid et dans Next.js (composant serveur avec `async`). Notez les spécificités de typage de chacun (props, événements, données de route).

**Exercice 18.5.2**

Comparez le typage des routes dans un framework de votre choix (Next.js, React Router, TanStack Router, Nuxt, SvelteKit) : routes typées, paramètres, chargeurs de données.

## 18.6 Bonnes pratiques

**Exercice 18.6.1**

Listez cinq bonnes pratiques de typage front-end (props explicites, unions discriminées pour les états, pas de `any` dans les gestionnaires, validation des données reçues d'API, types partagés avec le back-end) et illustrez chacune.

**Exercice 18.6.2**

Mini-projet : une application de liste de films (API publique, recherche avec anti-rebond, favoris persistés) dans le framework de votre choix, sans `any`, avec vérification de types en CI.

---

# 19. TypeScript côté serveur

## 19.1 Node.js avec TypeScript

**Exercice 19.1.1**

Créez un projet Node.js TypeScript minimal : `@types/node`, `tsconfig.json` pour `module: "nodenext"`, un fichier `src/index.ts` qui lit un fichier avec `node:fs/promises`.

### Exécuter du TypeScript

**Exercice 19.1.2**

Comparez quatre façons de lancer un fichier `.ts` : `tsc` puis `node`, Node.js avec effacement de types (`node fichier.ts`), `tsx`, `ts-node`. Pour chacune : vérification de types, vitesse, prise en charge des enums et des `namespace`, usage en production.

**Exercice 19.1.3**

Quelles syntaxes TypeScript ne sont pas supportées par l'effacement de types natif de Node.js (enums, `namespace`, propriétés de paramètres) ? Quelle option du compilateur (`erasableSyntaxOnly`) aide à les éviter ?

**Exercice 19.1.4**

Écrivez les scripts `dev`, `build`, `start`, `typecheck` d'un projet Node.js avec `tsx watch`, `tsc` et `node --watch`.

**Exercice 19.1.5**

Typez l'accès aux variables d'environnement : écrivez un module `env.ts` qui lit `process.env`, valide chaque variable (présence, type, valeurs par défaut) et exporte un objet typé. Pourquoi `process.env.X` est-il de type `string | undefined` ?

## 19.2 Express (v5)

**Exercice 19.2.1**

Écrivez un serveur Express avec trois routes (`GET /`, `GET /utilisateurs/:id`, `POST /utilisateurs`) et typez la requête et la réponse (`Request<Params, ResBody, ReqBody, Query>`).

**Exercice 19.2.2**

Écrivez un intergiciel (*middleware*) d'authentification typé qui ajoute `req.utilisateur` à la requête (augmentation de l'interface `Request`). Où placer la déclaration ?

**Exercice 19.2.3**

Écrivez un gestionnaire d'erreurs centralisé `(err: unknown, req, res, next)`. Que change Express 5 pour les gestionnaires asynchrones (les promesses rejetées sont transmises automatiquement) ?

**Exercice 19.2.4**

Écrivez une fonction utilitaire `route<P, B, R>(handler)` qui type les paramètres, le corps et la réponse, et vérifie le corps avec un schéma.

**Exercice 19.2.5**

Structurez une API en couches : routes, contrôleurs, services, dépôts. Définissez les types de données partagés et les interfaces entre couches.

## 19.3 NestJS

**Exercice 19.3.1**

Écrivez un module NestJS avec un contrôleur (`@Controller("utilisateurs")`, `@Get`, `@Post`, `@Param`, `@Body`) et un service injectable. Expliquez l'injection de dépendances par le constructeur.

**Exercice 19.3.2**

Écrivez un DTO validé avec `class-validator` (`@IsString`, `@IsEmail`, `@Min`) et activez `ValidationPipe`. Pourquoi les DTO sont-ils des classes et non des interfaces ?

**Exercice 19.3.3**

Écrivez un garde (`CanActivate`), un intercepteur et un filtre d'exception. Dans quel ordre s'exécutent-ils pour une requête ?

**Exercice 19.3.4**

Pourquoi NestJS exige-t-il `experimentalDecorators` et `emitDecoratorMetadata` ? Quelle est la situation avec les décorateurs standard ?

## 19.4 Gestion des erreurs côté serveur

**Exercice 19.4.1**

Définissez une hiérarchie d'erreurs HTTP typées (`ErreurHttp` avec `statut` et `code`, `NonTrouve`, `Interdit`, `Invalide`) et un gestionnaire qui les transforme en réponses JSON cohérentes.

**Exercice 19.4.2**

Pourquoi ne faut-il jamais renvoyer la pile d'appels ou les messages internes au client en production ? Écrivez le gestionnaire final qui enregistre l'erreur et renvoie un message générique.

**Exercice 19.4.3**

Gérez les erreurs non interceptées (`unhandledRejection`, `uncaughtException`) et l'arrêt gracieux du serveur (`SIGTERM`, fermeture des connexions).

**Exercice 19.4.4**

Typez une réponse d'API sous forme d'union discriminée (`{ ok: true; donnees: T } | { ok: false; erreur: { code: string; message: string } }`) et utilisez-la côté serveur et côté client.

## 19.5 Valider les données : types **et** exécution *(ajout)*

**Exercice 19.5.1**

Expliquez pourquoi les types TypeScript ne protègent pas contre des données invalides arrivant à l'exécution (corps de requête, JSON, variables d'environnement). Donnez un exemple de faille que le compilateur ne voit pas.

**Exercice 19.5.2**

Écrivez avec Zod (ou Valibot, ArkType) un schéma `UtilisateurSchema` et dérivez le type TypeScript avec `z.infer`. Validez une entrée inconnue avec `safeParse`.

**Exercice 19.5.3**

Écrivez un intergiciel Express générique `valider(schema)` qui valide `req.body` et renvoie une erreur 400 détaillée.

**Exercice 19.5.4**

Écrivez des schémas avec transformation (chaîne vers date, valeurs par défaut, champs optionnels, unions discriminées, schémas récursifs). Quel est le type d'entrée et le type de sortie d'un schéma avec transformation ?

**Exercice 19.5.5**

Comparez trois approches de la validation : garde de type écrite à la main, bibliothèque de schémas, génération de validateurs à partir des types. Avantages, inconvénients, performances.

## 19.6 Bonnes pratiques serveur

**Exercice 19.6.1**

Listez cinq bonnes pratiques (valider toutes les entrées, typer les erreurs, configuration validée au démarrage, couches séparées, journalisation structurée) et appliquez-les à une API minimale.

**Exercice 19.6.2**

Mini-projet : une API REST de gestion de tâches avec Express ou NestJS, validation Zod, tests, gestion d'erreurs centralisée, types partagés avec un client.

---

# 20. Configuration du projet (`tsconfig.json`)

## 20.1 Rôle

**Exercice 20.1.1**

Que fait un fichier `tsconfig.json` ? Quelle est la différence entre le fichier de configuration du projet et les options de la ligne de commande ? Quelle commande utilise `tsconfig.json` et laquelle l'ignore (`tsc fichier.ts`) ?

**Exercice 20.1.2**

Affichez la configuration effective d'un projet avec `tsc --showConfig` et la liste des fichiers compilés avec `tsc --listFiles`. Que révèle `tsc --explainFiles` ?

## 20.2 Nouveaux défauts de TypeScript 6.0 *(à jour)*

**Exercice 20.2.1**

Complétez le tableau des nouveaux défauts de TS 6.0 : `strict`, `module`, `target`, `types`, `rootDir`, `noUncheckedSideEffectImports`, `libReplacement`.

**Exercice 20.2.2**

Migrez un `tsconfig.json` écrit pour TS 5.x : quelles options explicites deviennent inutiles car elles sont désormais les valeurs par défaut ? Quelles erreurs nouvelles peut-on attendre ?

### Options **dépréciées** en 6.0 (et **supprimées** en 7.0)

**Exercice 20.2.3**

Relevez dans un `tsconfig.json` ancien les options dépréciées (par exemple `target: es5`, `moduleResolution: node10`, `baseUrl`, `outFile`, `module: amd/umd/system`, `downlevelIteration`, `alwaysStrict: false`, `esModuleInterop: false`) et proposez leur remplacement.

**Exercice 20.2.4**

Utilisez l'option `ignoreDeprecations: "6.0"` pour faire passer temporairement la compilation, puis supprimez-la en corrigeant chaque option. Pourquoi ne faut-il pas la garder longtemps ? *(TS 6.0)*

## 20.3 Options essentielles

**Exercice 20.3.1**

Complétez le tableau des options essentielles : `target`, `module`, `moduleResolution`, `lib`, `outDir`, `rootDir`, `include`, `exclude`, `strict`, `skipLibCheck`, `sourceMap`, `declaration`, `noEmit`, `isolatedModules`, `verbatimModuleSyntax`, `resolveJsonModule`.

**Exercice 20.3.2**

Quel `target` choisir pour un projet Node.js récent ? Pour un site destiné à des navigateurs modernes ? Quelles fonctionnalités JavaScript sont transformées ou conservées selon le `target` ?

**Exercice 20.3.3**

Quelle différence entre `target` et `lib` ? Que se passe-t-il si `lib` ne contient pas `ES2022` mais que le code utilise `Array.prototype.at` ?

**Exercice 20.3.4**

Qu'apporte `isolatedModules` ? Quelles constructions interdit-il (`const enum` ambiants, réexport de types sans `type`) ? Pourquoi est-il requis avec Vite, esbuild, SWC ?

**Exercice 20.3.5**

Que fait `noEmit` ? Dans quel cas l'utiliser (vérification seule avec un autre outil qui produit le JavaScript) ?

### Ce que contient `strict`

**Exercice 20.3.6**

Listez les options activées par `strict` : `noImplicitAny`, `strictNullChecks`, `strictFunctionTypes`, `strictBindCallApply`, `strictPropertyInitialization`, `noImplicitThis`, `useUnknownInCatchVariables`, `alwaysStrict`, `strictBuiltinIteratorReturn`. Pour chacune, écrivez un exemple de code qui devient une erreur.

**Exercice 20.3.7**

Quelles options supplémentaires non couvertes par `strict` recommandez-vous (`noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, `noImplicitOverride`, `noImplicitReturns`, `noFallthroughCasesInSwitch`, `noPropertyAccessFromIndexSignature`, `noUnusedLocals`, `noUnusedParameters`) ? Justifiez et donnez un exemple pour chacune.

**Exercice 20.3.8**

Migrez progressivement un projet JavaScript vers `strict` : proposez un plan (activer `allowJs` et `checkJs`, `// @ts-check`, corrections par fichier, activation des options une par une).

## 20.4 Alias de chemins (`paths`)

**Exercice 20.4.1**

Configurez `paths` (`"@/*": ["./src/*"]`) sans `baseUrl` (déprécié en TS 6). Quelle valeur faut-il utiliser pour `paths` si l'on n'a plus `baseUrl` ?

**Exercice 20.4.2**

Pourquoi `paths` ne suffit-il pas pour l'exécution ? Citez trois façons de faire fonctionner l'alias à l'exécution (bundler, `tsx`, imports de sous-chemins `#`).

**Exercice 20.4.3**

Comparez `paths` et `package.json#imports`. Dans quel cas préférer l'un ou l'autre ?

## 20.5 Résolution des modules

**Exercice 20.5.1**

Comparez les stratégies `node16`/`nodenext`, `bundler` et `node10` (dépréciée). Pour chaque stratégie : extension obligatoire, prise en charge de `exports`, usage recommandé.

**Exercice 20.5.2**

Quelle combinaison `module` / `moduleResolution` choisir pour : un serveur Node.js, une application Vite, une bibliothèque publiée sur npm en ESM et CommonJS, un script exécuté avec Bun ?

**Exercice 20.5.3**

Utilisez `customConditions` pour résoudre un champ `exports` personnalisé dans un monorepo. Que fait `resolvePackageJsonExports` ?

## 20.6 Configurations types

### Application Node.js

**Exercice 20.6.1**

Écrivez un `tsconfig.json` complet pour une application Node.js avec ESM : `target`, `module`, `moduleResolution`, `strict`, `outDir`, `rootDir`, `include`, `types`, `skipLibCheck`, `sourceMap`, options de rigueur supplémentaires.

### Application front-end (Vite)

**Exercice 20.6.2**

Écrivez les fichiers `tsconfig.json` (références), `tsconfig.app.json` (code client, `lib: ["ES2022", "DOM", "DOM.Iterable"]`, `jsx`, `noEmit`) et `tsconfig.node.json` (fichiers de configuration de Vite) pour un projet Vite + React.

**Exercice 20.6.3**

Écrivez le `tsconfig.json` d'une bibliothèque publiable : `declaration`, `declarationMap`, `outDir`, `target` large, `exports` correspondants, `isolatedDeclarations`.

## 20.7 Héritage et projets multiples

**Exercice 20.7.1**

Créez un `tsconfig.base.json` partagé et plusieurs `tsconfig.json` qui l'étendent (`extends`). Quelles options sont fusionnées et lesquelles sont remplacées ? Comment étendre plusieurs fichiers (tableau) ?

**Exercice 20.7.2**

Utilisez les références de projet (`references`, `composite`, `tsc -b`) pour un monorepo de trois paquets (`commun`, `serveur`, `client`). Quel est l'intérêt de la compilation incrémentale ?

**Exercice 20.7.3**

Que fait `extends` avec un paquet npm (`@tsconfig/node22`, `@tsconfig/strictest`) ? Comparez la maintenance d'une base personnalisée avec une base communautaire.

**Exercice 20.7.4**

Configurez un fichier `tsconfig.test.json` qui inclut les tests et les types de test (`vitest/globals`) sans polluer le code de production.

## 20.8 Erreurs fréquentes

**Exercice 20.8.1**

Pour chaque message d'erreur suivant, expliquez la cause et la correction : « Cannot find module './x' or its corresponding type declarations », « File is not under rootDir », « Option 'baseUrl' is deprecated », « This syntax requires an imported helper », « Cannot use import statement outside a module », « The 'import.meta' meta-property is only allowed when 'module' is... ».

**Exercice 20.8.2**

Pourquoi l'erreur « Cannot find name 'describe' / 'process' / 'document' » apparaît-elle ? Quelles options (`types`, `lib`) la corrigent ?

**Exercice 20.8.3**

Pourquoi un fichier absent de `include` n'est-il pas compilé mais peut-il être compilé quand il est importé ? Quelle différence avec `files` et `exclude` ?

## 20.9 TypeScript 7 et le compilateur natif *(à jour)*

**Exercice 20.9.1**

Quelles différences pratiques entre `tsc` (TS 6, JavaScript) et le compilateur natif de TS 7 : vitesse, mémoire, serveur de langage, compatibilité de l'API, plugins ? Mesurez le temps de vérification d'un projet important avec les deux.

**Exercice 20.9.2**

Préparez la migration vers TS 7 : listez les actions à effectuer dans votre projet (supprimer les options dépréciées, vérifier les outils qui dépendent de l'API du compilateur, mettre à jour les plugins d'éditeur).

**Exercice 20.9.3**

Quels outils de la chaîne (ESLint avec typescript-eslint, ts-jest, ts-node, plugins du service de langage) peuvent être affectés par le changement d'architecture ? Pourquoi ?

---

# 21. Linting et formatage

## 21.1 Pourquoi ?

**Exercice 21.1.1**

Différenciez : vérification de types (compilateur), linter (règles de qualité et de bogues) et formateur (mise en forme). Donnez un exemple de problème détecté uniquement par chaque outil.

**Exercice 21.1.2**

Pourquoi un compilateur strict ne remplace-t-il pas un linter ? Citez trois erreurs que `tsc` laisse passer mais qu'ESLint détecte (promesses flottantes, `any` explicites, variables inutilisées dans certaines configurations).

## 21.2 ESLint avec typescript-eslint (configuration « flat »)

**Exercice 21.2.1**

Installez `eslint`, `typescript-eslint` et `@eslint/js` et écrivez un fichier `eslint.config.js` avec `tseslint.config(...)` et les configurations `recommended` puis `strictTypeChecked` et `stylisticTypeChecked`. Quelle différence entre les règles « typées » et les règles sans types ?

**Exercice 21.2.2**

Activez l'analyse avec informations de types (`languageOptions.parserOptions.projectService: true`). Pourquoi est-elle plus lente mais plus précise ? À quelles règles est-elle nécessaire ?

**Exercice 21.2.3**

Configurez des règles différentes pour les fichiers de test (`files: ["**/*.test.ts"]`) et pour les fichiers de configuration JavaScript (désactivation des règles typées).

### Règles à retenir

**Exercice 21.2.4**

Pour chacune de ces règles, écrivez un exemple de code qui la viole et sa correction : `no-explicit-any`, `no-floating-promises`, `no-misused-promises`, `no-unsafe-assignment`, `no-unsafe-member-access`, `no-unnecessary-condition`, `consistent-type-imports`, `no-non-null-assertion`, `switch-exhaustiveness-check`, `prefer-nullish-coalescing`, `no-unused-vars`, `await-thenable`.

**Exercice 21.2.5**

Pourquoi faut-il désactiver la règle ESLint de base `no-unused-vars` au profit de la version TypeScript ? Que se passe-t-il pour les paramètres préfixés par `_` ?

**Exercice 21.2.6**

Comment ignorer une règle sur une ligne, un bloc ou un fichier ? Quelle règle (`ban-ts-comment`) encadre l'usage de `// @ts-ignore` et `// @ts-expect-error` ? Quand préférer `@ts-expect-error` ?

## 21.3 Prettier

**Exercice 21.3.1**

Installez Prettier, créez `.prettierrc` (`semi`, `singleQuote`, `trailingComma`, `printWidth`) et `.prettierignore`, puis formatez le projet (`prettier --write .`). Quelle option vérifie sans modifier (`--check`) ?

**Exercice 21.3.2**

Comment éviter les conflits entre ESLint et Prettier (`eslint-config-prettier`) ? Pourquoi est-il déconseillé d'exécuter Prettier comme règle ESLint ?

**Exercice 21.3.3**

Activez le formatage à l'enregistrement dans VS Code (`editor.formatOnSave`, `editor.defaultFormatter`) et vérifiez avec `.editorconfig` que tous les éditeurs de l'équipe respectent les mêmes conventions.

## 21.4 Alternative tout-en-un : Biome

**Exercice 21.4.1**

Installez Biome, initialisez `biome.json` et lancez `biome check --write`. Comparez la vitesse avec ESLint + Prettier sur un même projet.

**Exercice 21.4.2**

Quelles sont les limites actuelles de Biome face à typescript-eslint (règles nécessitant le système de types complet) ? Dans quel cas choisir l'un ou l'autre ?

**Exercice 21.4.3**

Migrez un projet de la combinaison ESLint + Prettier vers Biome (`biome migrate eslint`, `biome migrate prettier`). Notez les règles sans équivalent.

## 21.5 Intégration à l'éditeur et à la CI

**Exercice 21.5.1**

Configurez les extensions ESLint et Prettier (ou Biome) dans VS Code avec correction automatique à l'enregistrement (`editor.codeActionsOnSave`).

**Exercice 21.5.2**

Écrivez un flux de travail GitHub Actions (ou équivalent) qui exécute `npm ci`, `tsc --noEmit`, `eslint .`, `prettier --check .`, les tests, et échoue à la première erreur. Quel cache accélère l'installation ?

**Exercice 21.5.3**

Ajoutez `husky` et `lint-staged` pour exécuter le linter et le formateur sur les fichiers modifiés avant chaque `git commit`. Quelles limites a un crochet de pré-commit (contournable avec `--no-verify`) ?

## 21.6 Organisation type d'un projet

**Exercice 21.6.1**

Dessinez l'arborescence d'un projet TypeScript bien organisé (`src/`, `tests/`, `dist/`, `tsconfig*.json`, `eslint.config.js`, `.prettierrc`, `package.json`, `.gitignore`, `.editorconfig`, `.github/workflows`). Justifiez chaque élément.

**Exercice 21.6.2**

Créez un modèle de projet (gabarit) réutilisable qui contient toute cette configuration, avec un script `npm run verifier` qui lance tous les contrôles.

---

# Bonus

---

# 22. TypeScript et bases de données

## 22.1 Principes

**Exercice 22.1.1**

Pourquoi les types TypeScript ne garantissent-ils pas la forme des lignes renvoyées par une base de données ? Citez trois sources de décalage (schéma qui évolue, jointures, valeurs `NULL`, conversions de types).

**Exercice 22.1.2**

Comparez quatre approches : SQL brut avec types écrits à la main, générateur de types à partir du schéma (par exemple `pgtyped`, `kysely-codegen`), constructeur de requêtes typé (Kysely), ORM (Prisma, Drizzle, TypeORM). Pour chaque approche : sûreté de types, contrôle, courbe d'apprentissage.

**Exercice 22.1.3**

Pourquoi concaténer des chaînes dans une requête SQL est-il dangereux ? Écrivez un exemple d'injection SQL et la parade avec des requêtes paramétrées.

## 22.2 PostgreSQL avec `pg`

**Exercice 22.2.1**

Écrivez une fonction `trouverUtilisateur(pool: Pool, id: number): Promise<Utilisateur | null>` avec `pool.query<Utilisateur>("SELECT ... WHERE id = $1", [id])`. Pourquoi ce typage est-il une affirmation et non une vérification ?

**Exercice 22.2.2**

Écrivez une transaction (`BEGIN`, `COMMIT`, `ROLLBACK`) avec un client obtenu du pool et libéré dans un `finally`. Typez une fonction `avecTransaction<T>(fn: (client: PoolClient) => Promise<T>): Promise<T>`.

**Exercice 22.2.3**

Écrivez une fonction d'insertion qui renvoie l'enregistrement créé (`RETURNING *`) avec un type pour les données d'entrée (`Omit<Utilisateur, "id">`).

**Exercice 22.2.4**

Comment `pg` convertit-il les types SQL (`bigint`, `numeric`, `timestamp`) en JavaScript ? Écrivez une configuration de `types.setTypeParser` pour obtenir des `Date` ou des `bigint` corrects, et notez les pièges de précision.

## 22.3 MongoDB

### Pilote officiel

**Exercice 22.3.1**

Utilisez `MongoClient` et `Collection<Utilisateur>` pour insérer, rechercher, modifier et supprimer des documents. Quel est le type de `_id` (`ObjectId`) et comment le gérer dans l'interface ?

**Exercice 22.3.2**

Typez des filtres (`Filter<Utilisateur>`) et des mises à jour (`UpdateFilter<Utilisateur>`) et observez les erreurs de types sur un champ inexistant.

### Mongoose

**Exercice 22.3.3**

Écrivez un schéma Mongoose et déduisez le type du document (`InferSchemaType`). Comparez avec une interface écrite à la main.

**Exercice 22.3.4**

Écrivez un modèle avec méthodes d'instance et statiques typées, des hooks et des champs virtuels. Quelles difficultés de typage rencontre-t-on ?

## 22.4 ORM et constructeurs de requêtes

### Prisma (exemple)

**Exercice 22.4.1**

Écrivez un `schema.prisma` pour `Utilisateur` et `Article` (relation un-à-plusieurs), générez le client (`prisma generate`) et écrivez des requêtes avec `include`, `select` et `where`. Observez comment le type du résultat dépend de `select`/`include`.

**Exercice 22.4.2**

Utilisez `Prisma.UtilisateurGetPayload` ou `Prisma.validator` pour obtenir le type d'une requête partielle. Écrivez une fonction qui renvoie ce type.

**Exercice 22.4.3**

Écrivez une migration avec `prisma migrate dev` et un script d'amorçage (*seed*). Quel est l'intérêt d'avoir le schéma comme source de vérité unique ?

### Drizzle (exemple)

**Exercice 22.4.4**

Définissez les tables en TypeScript avec Drizzle (`pgTable`, `serial`, `text`, `relations`) et dérivez les types `typeof table.$inferSelect` et `$inferInsert`. Écrivez des requêtes `select`, `insert`, `update`, `delete` avec jointure.

**Exercice 22.4.5**

Comparez Prisma (schéma séparé et génération de code) et Drizzle (schéma en TypeScript, proche du SQL) : expérience de développement, performances, taille du client, portabilité.

### TypeORM (exemple)

**Exercice 22.4.6**

Écrivez des entités TypeORM avec décorateurs (`@Entity`, `@PrimaryGeneratedColumn`, `@Column`, `@OneToMany`, `@ManyToOne`) et un dépôt (`Repository<Utilisateur>`). Quel est le lien avec les décorateurs expérimentaux ?

**Exercice 22.4.7**

Écrivez le même modèle avec Kysely (constructeur de requêtes sans ORM) : une interface `Database` décrit les tables, les requêtes sont vérifiées par le compilateur. Observez les erreurs de types sur une colonne inexistante.

## 22.5 Motif « dépôt » (*repository*) pour découpler

**Exercice 22.5.1**

Écrivez une interface `DepotUtilisateurs` (`trouver`, `ajouter`, `modifier`, `supprimer`, `lister`) et deux implémentations : en mémoire (pour les tests) et PostgreSQL. Faites dépendre un service de l'interface.

**Exercice 22.5.2**

Écrivez un dépôt générique `Depot<T extends { id: string }>` avec une implémentation en mémoire et un test qui s'applique à toute implémentation.

**Exercice 22.5.3**

Quels types doivent traverser la frontière du dépôt : entités du domaine ou lignes de base de données ? Écrivez des fonctions de conversion (« mappeurs ») entre les deux.

## 22.6 Bonnes pratiques

**Exercice 22.6.1**

Listez cinq bonnes pratiques d'accès aux données (requêtes paramétrées, validation des lignes lues, pool de connexions, transactions, migrations versionnées) et illustrez-les.

**Exercice 22.6.2**

Mini-projet : une petite API de blog (utilisateurs, articles, commentaires) avec un ORM de votre choix, des migrations, un dépôt typé, des tests d'intégration sur une base jetable.

---

# 23. TypeScript et tests

## 23.1 Choisir un outil de test

**Exercice 23.1.1**

Complétez le tableau comparatif : Vitest, Jest, Mocha + Chai, `node:test` : support natif de TypeScript, vitesse, configuration, API compatible avec Jest, mocks intégrés, mode « watch ».

**Exercice 23.1.2**

Pour chacun des projets suivants, choisissez un outil de test et justifiez : projet Vite, projet NestJS, bibliothèque Node.js, monorepo, projet qui dépend de Babel.

## 23.2 Vitest

**Exercice 23.2.1**

Installez Vitest, écrivez une fonction `estPalindrome` et un fichier `estPalindrome.test.ts` avec `describe`, `it`, `expect`. Lancez les tests en mode « watch ».

**Exercice 23.2.2**

Utilisez `it.each` (ou `test.each`) pour tester plusieurs jeux de valeurs avec des types conservés. Utilisez `expect().toThrow`, `toEqual`, `toStrictEqual`, `toMatchObject`, `toBeCloseTo`, `resolves`, `rejects`.

**Exercice 23.2.3**

Écrivez des tests asynchrones (`async`/`await`) pour une fonction qui charge des données, avec `vi.useFakeTimers` pour contrôler le temps.

**Exercice 23.2.4**

Mesurez la couverture avec `vitest --coverage` (`v8` ou `istanbul`). Définissez des seuils minimums dans la configuration.

**Exercice 23.2.5**

Utilisez les tests dans la source (`import.meta.vitest`) et les instantanés (`toMatchSnapshot`, `toMatchInlineSnapshot`). Quand les utiliser et quand les éviter ?

**Exercice 23.2.6**

Testez un composant d'interface (React ou Vue) avec `@testing-library` et l'environnement `jsdom` ou `happy-dom`.

## 23.3 Jest avec TypeScript

**Exercice 23.3.1**

Configurez Jest avec `ts-jest` (ou `@swc/jest`) et `@types/jest`. Écrivez un test, lancez-le et notez la différence entre la vérification de types de `ts-jest` et la transpilation seule de SWC.

**Exercice 23.3.2**

Configurez les alias de chemin dans Jest (`moduleNameMapper`) en cohérence avec `tsconfig.json`.

**Exercice 23.3.3**

Utilisez `jest.fn<(a: number) => string>()`, `jest.spyOn`, `jest.mock` avec des types corrects (`jest.Mocked<T>`, `jest.MockedFunction`).

**Exercice 23.3.4**

Pourquoi l'ESM natif est-il délicat avec Jest ? Quelles options (`--experimental-vm-modules`, `extensionsToTreatAsEsm`) sont nécessaires ?

## 23.4 Mocha + Chai

**Exercice 23.4.1**

Installez Mocha, Chai et `tsx` (ou `ts-node`), et écrivez des tests avec `describe`, `it`, `expect` (Chai) et des tests asynchrones. Comment Mocha exécute-t-il des fichiers TypeScript ?

**Exercice 23.4.2**

Quelle bibliothèque de doublures utiliser avec Mocha (Sinon) ? Écrivez un test avec `sinon.stub` et `sinon.spy` correctement typés.

## 23.5 Tester les types

**Exercice 23.5.1**

Écrivez des tests de types avec `expectTypeOf` (Vitest) pour : le type de retour d'une fonction, les paramètres d'une fonction, les clés d'un objet, l'égalité entre deux types, un type conditionnel.

**Exercice 23.5.2**

Écrivez les utilitaires `Equal<A, B>` et `Expect<T extends true>` à la main et testez vos propres types utilitaires (`DeepPartial`, `Getters`). Pourquoi ces tests n'ont-ils aucune exécution à l'exécution mais font échouer `tsc` ?

**Exercice 23.5.3**

Utilisez `// @ts-expect-error` pour vérifier qu'un appel invalide est bien rejeté par le compilateur. Que se passe-t-il si le code devient valide par erreur (« Unused '@ts-expect-error' directive ») ?

**Exercice 23.5.4**

Utilisez les outils `tsd` ou `expect-type` ou `vitest typecheck` pour automatiser les tests de types d'une bibliothèque publiée. Quelle intégration en CI proposez-vous ?

## 23.6 Doublures : mocks, stubs, espions

**Exercice 23.6.1**

Définissez mock, stub, espion (*spy*) et faux (*fake*) avec un exemple pour chacun sur une fonction qui envoie un courriel.

**Exercice 23.6.2**

Écrivez un test qui remplace `fetch` par un `vi.fn` typé et vérifie l'appel (`toHaveBeenCalledWith`) et le résultat. Comment restaurer l'original (`vi.restoreAllMocks`) ?

**Exercice 23.6.3**

Écrivez un test avec injection de dépendances : une classe `Commande` qui reçoit `Paiement` et `Courriel`. Remplacez-les par des doublures typées par l'interface, pas par `any`.

**Exercice 23.6.4**

Utilisez `vi.mock("./module")` pour remplacer un module entier, avec des types fidèles (`vi.mocked`, `vi.importActual`). Quels sont les risques d'une doublure qui ne ressemble plus au vrai module ?

**Exercice 23.6.5**

Simulez le réseau avec une bibliothèque de simulation d'API (par exemple `msw`) et écrivez un test d'intégration qui ne dépend pas du serveur réel.

## 23.7 Sécurité des types dans les tests

**Exercice 23.7.1**

Pourquoi les tests ne doivent-ils pas utiliser `any` pour construire des données ? Écrivez une fabrique de données de test typée (`creerUtilisateur(surcharges?: Partial<Utilisateur>): Utilisateur`).

**Exercice 23.7.2**

Pourquoi les assertions `as` dans les tests peuvent-elles masquer des défauts ? Écrivez un exemple où un test passe alors que le type est faux, et corrigez-le.

**Exercice 23.7.3**

Comment vérifier que les fichiers de test sont bien analysés par `tsc` (inclusion dans `tsconfig.json`) ? Pourquoi les erreurs de types dans les tests doivent-elles faire échouer la CI ?

## 23.8 Bonnes pratiques

**Exercice 23.8.1**

Listez cinq bonnes pratiques de test (tests rapides, indépendants, lisibles, nommage, ne tester que le comportement public, éviter la sur-utilisation des doublures) et illustrez chacune.

**Exercice 23.8.2**

Appliquez la pyramide des tests à un petit projet : écrivez des tests unitaires, un test d'intégration et un test de bout en bout, et justifiez la proportion de chaque.

**Exercice 23.8.3**

Écrivez des tests pilotés par les propriétés avec `fast-check` pour une fonction de tri ou de sérialisation. Quels invariants vérifier ?

---

# 24. Nouveautés par version et bonnes pratiques

## 24.1 Chronologie des fonctionnalités

**Exercice 24.1.1**

Associez chaque fonctionnalité à la version qui l'a introduite : `satisfies`, paramètres de type `const`, `using`, `NoInfer`, prédicats de type inférés, `erasableSyntaxOnly`, `verbatimModuleSyntax`, décorateurs standard, `enum` unifiés, `--module nodenext` stable, compilateur natif.

**Exercice 24.1.2**

Pour chaque fonctionnalité de la liste précédente, écrivez un exemple de code de cinq lignes maximum qui l'illustre et indiquez le problème qu'elle résout.

**Exercice 24.1.3**

Modernisez ce code écrit dans un style TypeScript 3.x en utilisant les fonctionnalités récentes :

```ts
enum Role { Admin = "ADMIN", User = "USER" }

function estUtilisateur(x: any): x is Utilisateur {
  return x && typeof x.nom === "string";
}

const config = <Config>{ port: 3000 };

namespace Outils {
  export function formater(x: number) { return x.toFixed(2); }
}

import { Utilisateur } from "./types";
```

**Exercice 24.1.4**

Quelles fonctionnalités de TypeScript sont du JavaScript « standard » et lesquelles sont propres à TypeScript (enums, `namespace`, propriétés de paramètres, décorateurs expérimentaux) ? Pourquoi cette distinction compte-t-elle pour l'effacement de types natif ?

## 24.2 Gestion de ressources : `using` *(TS 5.2, ajout)*

**Exercice 24.2.1**

Écrivez une classe `Connexion` qui implémente `[Symbol.dispose]()` et utilisez-la avec `using conn = new Connexion()`. Dans quel ordre les ressources sont-elles libérées en sortie de bloc, y compris en cas d'exception ? *(TS 5.2)*

**Exercice 24.2.2**

Écrivez une ressource asynchrone avec `[Symbol.asyncDispose]()` et `await using`. Quand préférer `await using` à `using` ? *(TS 5.2)*

**Exercice 24.2.3**

Écrivez un utilitaire qui transforme une fonction de nettoyage en objet jetable (`DisposableStack`, `AsyncDisposableStack`) pour gérer plusieurs ressources dans une même portée.

**Exercice 24.2.4**

Quelles bibliothèques `lib` et cibles faut-il configurer (`esnext.disposable`) et quel est le support dans les moteurs JavaScript actuels ? Comment compléter si le moteur ne le supporte pas (polyfill) ?

**Exercice 24.2.5**

Réécrivez avec `using` un code qui ouvre un fichier, un verrou et une transaction avec trois `try/finally` imbriqués.

## 24.3 Bonnes pratiques

**Exercice 24.3.1**

Réalisez une revue de code d'un petit projet TypeScript en vous appuyant sur les bonnes pratiques du cours (`strict` activé, pas de `any`, `unknown` plus `narrowing`, unions discriminées, types dérivés, validation des entrées, `satisfies`, `import type`, `readonly`). Produisez une liste de remarques classées par gravité.

**Exercice 24.3.2**

Établissez la liste de vos dix règles d'équipe pour TypeScript (configuration, types, style, structure, tests, CI) et justifiez chacune en une phrase.

**Exercice 24.3.3**

Corrigez ces mauvaises pratiques courantes :

```ts
function traiter(donnees: any) {
  return donnees.items.map((i: any) => i.nom);
}

const el = document.getElementById("x")!;
const n = (valeur as unknown) as number;

type Config = { [cle: string]: any };

export default class Utilitaires {
  static x = 1;
}
```

**Exercice 24.3.4**

Concevez un plan de migration progressive d'un projet JavaScript de 200 fichiers vers TypeScript strict (étapes, ordre des fichiers, outils, critères de réussite, gestion de l'équipe).

## 24.4 Ressources

**Exercice 24.4.1**

Parcourez la documentation officielle, le manuel (*Handbook*) et les notes de version de la dernière version. Choisissez deux nouveautés absentes du cours et résumez-les avec un exemple.

**Exercice 24.4.2**

Faites quinze défis du dépôt *Type Challenges* (facile et moyen) et rédigez, pour trois d'entre eux, une explication détaillée de la solution.

**Exercice 24.4.3**

Consultez le dépôt DefinitelyTyped et contribuez (même symboliquement, en local) un correctif de types sur un paquet de votre choix. Quels tests faut-il fournir ?

**Exercice 24.4.4** *(défi)*

Projet de synthèse : réalisez une application complète (client et serveur) avec un contrat d'API partagé et typé de bout en bout, des données validées à l'exécution, un `tsconfig` strict, ESLint et Prettier (ou Biome), des tests (unitaires, de types, d'intégration) et une intégration continue.

---

<div align="center">

*Bon courage, et que vos types soient toujours justes !*

</div>
