# Angular — Cours complet

*Cours magistral et module d'apprentissage exhaustif, fondé sur le plan « Angular — Guide complet » — Angular 22 (octobre 2026)*

## Avant de commencer : comment utiliser ce cours

Ce cours développe, chapitre par chapitre, l'intégralité du plan en **29 chapitres**, regroupés en six parties : **Fondamentaux** (1 à 10), **Avancé** (11 à 15), **Tests** (16 et 17), **Performance** (18 à 20) et **Essentiels** (21 à 29).

Chaque chapitre suit la même trame : *objectifs d'apprentissage → notions et définitions → exemples de code commentés → pièges fréquents → synthèse*.

**Conventions de lecture**

- **(à jour)** : pratique moderne qui remplace une ancienne. **(héritage)** : ancienne approche, encore fréquente dans les projets existants. **(ajout)** : notion absente des anciens guides.
- Le code est écrit en **TypeScript strict**. Les fichiers sont placés sous `src/app/` et suivent la convention de nommage récente (fichier `compteur.ts`, classe `Compteur`, sans suffixe `.component`).
- Chaque exemple est volontairement **autonome** : les imports nécessaires sont toujours indiqués.
- Le cours enseigne l'Angular **actuel** (composants autonomes, signaux, flux de contrôle `@if` / `@for`, zoneless, Vitest, Signal Forms) **et** explique l'ancien (`NgModule`, `*ngIf`, `@Input()`…) pour que vous sachiez lire du code existant.

**Parcours conseillé** : lisez les chapitres 1 à 10 dans l'ordre (ils se construisent les uns sur les autres), puis choisissez librement dans les parties suivantes selon vos besoins.

---

## 1. Introduction à Angular

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : définir Angular et expliquer ce qui le distingue d'une bibliothèque ; décrire le principe d'une application monopage ; distinguer AngularJS d'Angular ; décrire l'architecture générale d'une application ; comparer Angular à React et à Vue ; comprendre le calendrier de versions ; préparer votre environnement de travail.

### 1.1 Qu'est-ce qu'Angular ?

**Angular** est un **framework** open source développé par **Google** et une communauté de contributeurs. Il sert à construire des **applications web monopages** (*SPA*, *Single Page Applications*) et, plus largement, des applications web complètes, rendues dans le navigateur, sur le serveur, ou pré-générées à la compilation. Il est écrit en **TypeScript**.

**Framework ou bibliothèque ?** Une *bibliothèque* (comme React) est une boîte à outils que **vous** appelez quand vous en avez besoin. Un *framework* impose une **structure** et appelle **votre** code : c'est le principe d'**inversion de contrôle**. Angular est un framework **opinionné** (*opinionated*) : il propose une manière standard de structurer, nommer, tester et construire une application. Conséquence pratique : deux projets Angular se ressemblent, ce qui facilite le travail en équipe et la maintenance sur plusieurs années.

Angular est dit « **tout inclus** » (*batteries included*) : il fournit en standard les briques dont une application professionnelle a besoin.

| Brique | Rôle | Chapitre |
| --- | --- | --- |
| **Composants et gabarits** | Construire l'interface | 4, 5 |
| **Directives et tubes** | Étendre le HTML, transformer l'affichage | 6 |
| **Services et injection de dépendances** | Partager la logique et l'état | 7 |
| **Signaux** | Réactivité fine de l'état | 8 |
| **Routeur** | Navigation entre pages | 9 |
| **Formulaires** | Saisie et validation | 10 |
| **Client HTTP** | Communication avec les API | 11 |
| **RxJS** | Flux asynchrones | 12 |
| **Outils de test** | Tests unitaires et E2E | 16, 17 |
| **CLI (`ng`)** | Génération, build, mises à jour | 3 |
| **i18n, SSR, PWA, Material, animations** | Fonctions transverses | 14, 21 à 24 |

### 1.2 Les concepts fondateurs

Avant d'entrer dans le détail, voici le vocabulaire minimal. Chaque terme sera approfondi dans un chapitre dédié.

- **Composant** : brique d'interface qui associe une **classe TypeScript** (données et logique), un **gabarit** HTML et des **styles** CSS. Une application est un **arbre de composants**.
- **Gabarit (*template*)** : HTML enrichi de la syntaxe Angular (interpolation `{{ }}`, liaisons `[ ]` et `( )`, blocs `@if` / `@for`).
- **Liaison de données (*data binding*)** : mécanisme qui synchronise la classe et la vue.
- **Directive** : instruction qui modifie le comportement ou la structure d'un élément du DOM. Un composant est une directive **avec** gabarit.
- **Tube (*pipe*)** : fonction de transformation appliquée à l'**affichage** d'une valeur (`{{ date | date }}`).
- **Service** : classe réutilisable qui porte de la logique métier, de l'accès aux données ou un état partagé.
- **Injection de dépendances (DI)** : mécanisme par lequel Angular **fournit** à une classe les objets dont elle a besoin, au lieu qu'elle les crée elle-même.
- **Signal** : conteneur de valeur **réactif** ; Angular sait précisément quelles parties de la vue en dépendent.
- **Observable** : flux de valeurs dans le temps (RxJS), adapté aux événements et aux appels asynchrones.
- **Route** : association entre une URL et un composant.
- **`NgModule`** *(héritage)* : ancien conteneur de déclarations, remplacé par les composants autonomes.

### 1.3 Architecture générale d'une application

Le schéma suivant résume ce qui se passe au démarrage et à l'exécution.

```text
index.html
   └── <app-root>                      ← élément hôte du composant racine
          └── App (composant racine)
                 └── <router-outlet>   ← zone où le routeur affiche la page courante
                        └── Page (composant)
                               ├── Composant enfant A
                               └── Composant enfant B

Services (singletons) ←— injectés par l'injecteur dans les composants qui en ont besoin
```

**Le flux de données est unidirectionnel.** L'**état** (signaux, propriétés) descend vers la **vue** ; les **événements** de l'utilisateur remontent vers la classe, qui modifie l'état ; Angular met alors la vue à jour. Un composant parent transmet des données à ses enfants par des **entrées** (`input`) et reçoit leurs notifications par des **sorties** (`output`).

**Cycle d'une interaction (mode moderne) :**

1. L'utilisateur clique sur un bouton : l'événement `(click)` appelle une méthode de la classe.
2. La méthode modifie un **signal** (`compteur.update(v => v + 1)`).
3. Angular sait quels gabarits lisent ce signal et **planifie** leur mise à jour.
4. Le DOM est mis à jour **uniquement** aux endroits concernés.

**Cycle de vie d'un projet :**

1. Vous écrivez du TypeScript, des gabarits et des styles.
2. La **compilation AOT** (*Ahead-of-Time*) vérifie les types, y compris dans les gabarits, et transforme le tout en JavaScript optimisé.
3. Le **builder** (esbuild + Vite) produit des **bundles** minifiés et découpés.
4. Le navigateur charge `index.html`, exécute `main.ts` qui appelle `bootstrapApplication()` : Angular crée le composant racine, configure les services et affiche l'application.

### 1.4 Les applications monopages (SPA)

Une **SPA** ne charge **qu'une seule page HTML**. Lors d'un clic sur un lien, le routeur Angular intercepte la navigation, modifie l'URL grâce à l'**History API** du navigateur (`pushState`) et remplace le contenu affiché, **sans recharger la page**. Les données sont obtenues par des appels HTTP (JSON) en arrière-plan.

|  | **Application multipage (MPA)** | **Application monopage (SPA)** |
| --- | --- | --- |
| Navigation | Le serveur renvoie une page HTML complète à chaque clic | Le navigateur remplace des portions de la page |
| Fluidité | Rechargement visible | Transitions fluides, sensation d'application native |
| Premier affichage | Rapide (HTML prêt) | Plus lent si tout est rendu côté client |
| SEO | Naturel | Demande du **SSR** ou du **pré-rendu** |
| Logique | Principalement serveur | Répartie entre client et serveur |

**Limites et remèdes.** Le premier chargement d'une SPA pure peut être lent et mal indexé par certains robots. Angular répond par le **rendu côté serveur (SSR)**, le **pré-rendu (SSG)** et l'**hydratation** (chapitre 22), ainsi que par le **chargement paresseux** (chapitre 19).

### 1.5 AngularJS et Angular : histoire et confusion à éviter

- **2010** : naissance d'**AngularJS** (versions 1.x), en JavaScript, fondé sur les `$scope` et les contrôleurs (architecture de type MVC).
- **2016** : sortie d'**Angular 2**, une **réécriture complète** en TypeScript, fondée sur les composants. Aucune compatibilité directe avec AngularJS.
- **2017 et après** : le projet adopte le **versionnement sémantique** (Angular 4, 5, 6…, la version 3 ayant été sautée pour aligner les paquets). On parle simplement d'« Angular ».
- **2020 (v9)** : **Ivy**, nouveau moteur de compilation et de rendu, activé par défaut.
- **2022 (v14–15)** : composants **autonomes**, fonction `inject()`, gardes fonctionnelles.
- **2023 (v16–17)** : **signaux**, nouveau **flux de contrôle** `@if` / `@for`, `@defer`, builder **esbuild + Vite**.
- **2024–2026 (v18–22)** : zoneless, `linkedSignal`, `resource`, **Signal Forms**, Vitest, Angular Aria.

|  | **AngularJS** (1.x) | **Angular** (2 et suivants) |
| --- | --- | --- |
| Langage | JavaScript | **TypeScript** |
| Architecture | MVC / `$scope` | **Composants** |
| Statut | **Fin de vie en 2022** | Maintenu activement |

> **Attention.** Ne mélangez jamais les deux. Beaucoup de tutoriels anciens parlent d'« Angular » pour AngularJS. **Comment dater un exemple de code ?** `$scope` ou `ng-controller` → AngularJS ; `@NgModule` et `*ngIf` → Angular « classique » ; `imports` dans `@Component`, `@if`, `signal()` → Angular moderne.

### 1.6 Pourquoi choisir Angular ? Forces et limites

**Forces**

- **Structure claire** et conventions fortes : idéal pour de **grandes équipes** et des projets de **longue durée**.
- **Écosystème officiel intégré** : routeur, formulaires, HTTP, i18n, tests, Material, SSR, PWA.
- **Mises à jour guidées** (`ng update`) avec réécriture automatique du code, et **support à long terme**.
- **Typage strict** de bout en bout, y compris dans les gabarits.
- **Performance** : compilation AOT, *tree-shaking*, vues différées, SSR, hydratation, mode **zoneless**.

**Limites**

- Courbe d'apprentissage **plus raide** : de nombreux concepts (DI, RxJS, signaux, routeur).
- Un projet minimal reste plus lourd qu'avec des outils plus légers.
- Un rythme de **versions semestriel** : il faut planifier les mises à jour.
- Une partie du contenu en ligne est **obsolète** (cf. 1.5).

|  | **Angular** | **React** | **Vue** |
| --- | --- | --- | --- |
| Nature | Framework complet | Bibliothèque d'interface | Framework progressif |
| Langage | TypeScript | JavaScript / TypeScript (JSX) | JS / TS (gabarits) |
| Réactivité | Signaux + RxJS | État + hooks | `ref` / `reactive` |
| Routage, formulaires, HTTP | **Inclus** | Bibliothèques tierces | Écosystème officiel |
| Courbe d'apprentissage | Plus raide | Moyenne | Douce |
| Idéal pour | Grandes applications d'entreprise | Flexibilité maximale | Prise en main rapide |

**Quand choisir Angular ?** Application d'entreprise, plusieurs équipes, durée de vie de plusieurs années, besoin de cohérence et de typage. **Quand hésiter ?** Petit site vitrine, prototype jetable, équipe déjà experte dans une autre pile.

### 1.7 Versions, cadence et support *(à jour)*

Angular suit le **versionnement sémantique** et une **cadence fixe** : une version **majeure tous les 6 mois** (mai et novembre), accompagnée de versions mineures et de correctifs intermédiaires.

- **Support** : chaque majeure est supportée **18 mois** = **6 mois de support actif** (nouveautés et correctifs) + **12 mois de support à long terme** (correctifs critiques et de sécurité).
- **Politique de dépréciation** : une API est d'abord **dépréciée** (avertissement, migration proposée) avant d'être retirée dans une version majeure ultérieure ; les retraits sont annoncés à l'avance.
- **Migrations automatiques** : `ng update` exécute des *schematics* qui réécrivent votre code (chapitre 28).

| Version | Date | Points marquants |
| --- | --- | --- |
| **17** | nov. 2023 | Flux de contrôle `@if` / `@for`, `@defer`, esbuild + Vite |
| **18** | mai 2024 | Zoneless (expérimental), Material 3, `@let` |
| **19** | nov. 2024 | Autonome par défaut, hydratation incrémentale, `linkedSignal` et `resource` (aperçus) |
| **20** | mai 2025 | Signaux stables, `httpResource`, nouvelle convention de nommage, Vitest expérimental |
| **21** | nov. 2025 | **Zoneless par défaut**, **Vitest par défaut**, Signal Forms (expérimental), Aria (aperçu) |
| **22** | juin 2026 | **Signal Forms stables**, `resource` / `httpResource` stables, **`OnPush` par défaut**, Aria stable, builders webpack dépréciés |

**Quelle version utiliser ?** La plus récente (ici, **Angular 22**). Chaque version exige des versions minimales de **Node.js** et de **TypeScript** : consultez `angular.dev/reference/versions`.

### 1.8 Prérequis et environnement de travail

**Connaissances requises**

- **HTML** sémantique et **CSS** (sélecteurs, boîte, flexbox, grid).
- **JavaScript moderne (ES2020+)** : `let` / `const`, fonctions fléchées, déstructuration, opérateur de décomposition (`...`), modules `import` / `export`, classes, **promesses** et `async` / `await`, méthodes de tableaux (`map`, `filter`, `reduce`), chaînage optionnel `?.` et coalescence nulle `??`.
- Notions de **TypeScript** (chapitre 2 pour la remise à niveau).

**Outils**

- **Node.js** (version LTS compatible) et **npm** ; **Git**.
- **VS Code** avec l'extension **Angular Language Service** (autocomplétion et vérification de types dans les gabarits).
- **Angular DevTools** (extension de navigateur) : arbre de composants, profilage de la détection des changements.
- Un navigateur moderne.

### 1.9 Glossaire du chapitre

| Terme | Définition courte |
| --- | --- |
| SPA | Application qui ne charge qu'une page HTML et met à jour la vue dynamiquement |
| AOT / JIT | Compilation à la construction / dans le navigateur |
| Ivy | Moteur de compilation et de rendu d'Angular (depuis la v9) |
| Standalone (autonome) | Composant qui déclare lui-même ses dépendances |
| Zoneless | Fonctionnement sans Zone.js, piloté par les signaux |
| SSR / SSG | Rendu côté serveur / génération statique au build |
| Hydratation | Réutilisation du HTML serveur par l'application côté navigateur |
| Schematic | Script du CLI qui génère ou réécrit du code |

### Synthèse du chapitre 1

Angular est un **framework complet, opinionné et typé**, conçu pour des applications durables. Sa force est la **cohérence** : un seul outil (`ng`), une seule manière de faire, des **mises à jour guidées** tous les six mois. L'Angular moderne repose sur des **composants autonomes**, des **signaux** et le mode **zoneless**.

---

## 2. TypeScript pour Angular

**Objectifs d'apprentissage.** Maîtriser les notions de TypeScript indispensables pour lire et écrire du code Angular : types, interfaces, unions, génériques, classes, modules, décorateurs, mode strict.

### 2.1 Pourquoi TypeScript ?

**TypeScript** est un **sur-ensemble** de JavaScript : tout JavaScript valide est du TypeScript valide. Il ajoute un **système de types statique** vérifié à la **compilation**. Le compilateur retire ensuite les types et produit du JavaScript standard : **les types n'existent pas à l'exécution**.

Avantages dans Angular :

- **Erreurs détectées avant l'exécution** (propriété inexistante, mauvais argument, valeur possiblement nulle).
- **Autocomplétion** et **refactorisation** fiables dans l'éditeur.
- **Documentation vivante** : les types décrivent les données.
- Le compilateur Angular vérifie aussi les **gabarits** HTML (`strictTemplates`).

### 2.2 Types de base et inférence

```typescript
// src/app/modeles.ts
let nom: string = 'Alice';
let age: number = 30;               // entiers et décimaux : un seul type `number`
let actif: boolean = true;
let ids: number[] = [1, 2, 3];      // tableau (syntaxe équivalente : Array<number>)
let paire: [string, number] = ['Alice', 30];   // tuple : longueur et types fixés par position
let grand: bigint = 9007199254740993n;

const ville = 'Paris';              // inférence : type littéral 'Paris'
let compteur = 0;                   // inférence : number (pas besoin de l'écrire)
```

**Inférence de types.** TypeScript **déduit** les types à partir des valeurs. On annote **les paramètres de fonctions** et les **API publiques**, et on laisse l'inférence faire le reste.

### 2.3 Types spéciaux : `any`, `unknown`, `never`, `void`, `null`, `undefined`

| Type | Signification | Recommandation |
| --- | --- | --- |
| `any` | Désactive la vérification | **À éviter** |
| `unknown` | Valeur de type inconnu : il faut la **vérifier** avant usage | Préféré à `any` pour les données externes |
| `never` | Valeur qui n'existe jamais (fonction qui lève une exception, cas impossible) | Vérifications d'exhaustivité |
| `void` | Fonction qui ne renvoie rien | Retour des procédures |
| `null` / `undefined` | Absence de valeur | Gérés par `strictNullChecks` |

```typescript
function lireDonnee(brut: unknown): string {
    if (typeof brut === 'string') return brut.toUpperCase();   // rétrécissement de type
    throw new Error('Chaîne attendue');
}
```

### 2.4 Objets : `interface` et `type`

```typescript
export interface Utilisateur {
    id: number;
    nom: string;
    email?: string;              // propriété optionnelle (string | undefined)
    readonly creeLe: Date;       // lecture seule après création
}

export interface Admin extends Utilisateur {   // héritage d'interface
    permissions: string[];
}

export type Role = 'admin' | 'editeur' | 'lecteur';   // alias de type (union de littéraux)
export type Dictionnaire = { [cle: string]: number }; // signature d'index

const u: Utilisateur = { id: 1, nom: 'Alice', creeLe: new Date() };
```

|  | `interface` | `type` |
| --- | --- | --- |
| Décrire un objet | Oui | Oui |
| Étendre | `extends` | Intersection `&` |
| Fusion de déclarations | Oui | Non |
| Unions, tuples, types calculés | Non | **Oui** |

**Règle pratique** : `interface` pour les formes d'objets publiques (modèles, contrats), `type` pour les unions et les types calculés.

### 2.5 Unions, intersections, littéraux et rétrécissement

```typescript
type Id = number | string;                 // union : l'un OU l'autre
type Horodate = { creeLe: Date };
type Article = { titre: string } & Horodate;   // intersection : les DEUX

function afficher(id: Id): string {
    return typeof id === 'number' ? `n°${id}` : id.toUpperCase();   // rétrécissement par typeof
}
```

**Rétrécissement (*narrowing*)** : le compilateur affine le type selon les tests effectués : `typeof`, `instanceof`, `in`, égalité, vérification de nullité.

**Union discriminée** : un champ commun (le *discriminant*) distingue les variantes, ce qui rend le code sûr et exhaustif.

```typescript
type Etat =
    | { statut: 'chargement' }
    | { statut: 'succes'; donnees: string[] }
    | { statut: 'erreur'; message: string };

function decrire(e: Etat): string {
    switch (e.statut) {
        case 'chargement': return 'Chargement…';
        case 'succes': return `${e.donnees.length} éléments`;
        case 'erreur': return e.message;
        default: { const _exhaustif: never = e; return _exhaustif; }   // erreur si un cas est oublié
    }
}
```

**Opérateurs utiles** : `as const` (fige un littéral en type précis), `satisfies` (vérifie la conformité sans élargir le type), assertion non nulle `x!` (**à éviter** : vous promettez au compilateur que la valeur n'est pas nulle).

### 2.6 Fonctions

```typescript
const additionner = (a: number, b: number): number => a + b;

function saluer(nom: string, salutation = 'Bonjour', ...complements: string[]): string {
    return `${salutation} ${nom} ${complements.join(' ')}`.trim();
}

type Rappel = (valeur: number) => void;           // type de fonction
function executer(cb: Rappel): void { cb(42); }
```

Paramètre **optionnel** `x?: T`, valeur **par défaut** `x = 1`, paramètres **restants** `...liste`. Les **fonctions fléchées** conservent le `this` du contexte englobant : elles sont préférées pour les rappels.

### 2.7 Génériques et types utilitaires

Un **générique** paramètre un type : il permet d'écrire du code réutilisable **sans perdre le typage**.

```typescript
function premier<T>(elements: T[]): T | undefined { return elements[0]; }

interface Reponse<T> { donnees: T; statut: number }        // interface générique
function longueur<T extends { length: number }>(x: T): number { return x.length; }   // contrainte

const n = premier([10, 20]);        // T = number
const s = premier(['a', 'b']);      // T = string
```

**Types utilitaires** fournis par TypeScript :

| Utilitaire | Effet |
| --- | --- |
| `Partial<T>` / `Required<T>` | Toutes les propriétés optionnelles / obligatoires |
| `Readonly<T>` | Toutes les propriétés en lecture seule |
| `Pick<T, K>` / `Omit<T, K>` | Garder / retirer des propriétés |
| `Record<K, V>` | Objet de clés `K` et de valeurs `V` |
| `NonNullable<T>` | Retire `null` et `undefined` |
| `ReturnType<F>` | Type de retour d'une fonction |
| `Awaited<T>` | Type résolu d'une promesse |

```typescript
import type { Utilisateur } from './modeles';

type NouvelUtilisateur = Omit<Utilisateur, 'id' | 'creeLe'>;   // utilisé pour les créations (POST)
type Modification = Partial<NouvelUtilisateur>;                // utilisé pour les PATCH
```

### 2.8 Classes

```typescript
abstract class Forme {
    abstract aire(): number;                         // méthode à implémenter
}

class Compte {
    #solde = 0;                                       // champ privé natif (à l'exécution)
    static nombre = 0;                                // membre statique
    constructor(public readonly titulaire: string) {  // « propriété de paramètre » : déclare ET affecte
        Compte.nombre++;
    }
    deposer(montant: number): void { this.#solde += montant; }
    get solde(): number { return this.#solde; }       // accesseur (getter)
}

class Cercle extends Forme {
    constructor(private readonly rayon: number) { super(); }
    override aire(): number { return Math.PI * this.rayon ** 2; }   // `override` : vérifie l'héritage
}

interface Imprimable { imprimer(): void }
class Facture implements Imprimable { imprimer(): void { console.log('Facture'); } }
```

**Modificateurs de visibilité** : `public` (défaut), `protected` (classe et sous-classes), `private` (classe seule, vérifié à la compilation), `#champ` (privé **réel** à l'exécution). En Angular, on utilise surtout `protected` pour ce qui n'est lu que par le gabarit, et `readonly` pour les signaux.

### 2.9 Énumérations et alternatives

```typescript
enum Couleur { Rouge, Vert, Bleu }                       // énumération numérique
const Statut = { Actif: 'actif', Inactif: 'inactif' } as const;   // alternative légère
type Statut = typeof Statut[keyof typeof Statut];        // 'actif' | 'inactif'
```

Préférez souvent l'**union de littéraux** (`'admin' | 'editeur'`) : plus simple, sans code généré.

### 2.10 Modules JavaScript

```typescript
// src/app/mon-service.ts
import { Injectable, signal } from '@angular/core';       // import nommé
import type { Utilisateur } from './modeles';              // import de TYPE uniquement (effacé à la compilation)

@Injectable({ providedIn: 'root' })
export class MonService {                                   // export nommé
    readonly utilisateur = signal<Utilisateur | null>(null);
}

export default class Autre {}                              // export par défaut (un seul par fichier)
```

Import **dynamique** (chargement paresseux) : `const m = await import('./editeur');` — c'est le mécanisme du chargement paresseux d'Angular (chapitre 19). Évitez les **fichiers « baril »** (`index.ts` qui réexporte tout) : ils nuisent au *tree-shaking*.

### 2.11 Décorateurs

Un **décorateur** est une fonction qui **ajoute des métadonnées** à une classe ou à un membre, écrite avec `@`. Angular s'en sert pour déclarer ses artefacts : `@Component`, `@Directive`, `@Pipe`, `@Injectable`, `@NgModule` (héritage), et pour les anciens `@Input()`, `@Output()`, `@ViewChild()`. Le **compilateur Angular** les interprète à la construction : vous n'avez rien à configurer.

```typescript
import { Component } from '@angular/core';

@Component({ selector: 'app-hello', template: `<p>Bonjour</p>` })   // métadonnées du composant
export class Hello {}
```

La tendance actuelle remplace plusieurs décorateurs de membres par des **fonctions** (`input()`, `output()`, `viewChild()`, `inject()`), plus simples à typer.

### 2.12 Asynchronisme

```typescript
async function charger(url: string): Promise<{ nom: string }> {
    const reponse = await fetch(url);                     // attend la promesse
    if (!reponse.ok) throw new Error(`HTTP ${reponse.status}`);
    return (await reponse.json()) as { nom: string };
}
```

Une **promesse** représente **une** valeur future ; un **Observable** (chapitre 12) représente **un flux** de valeurs. Angular utilise les deux ; on convertit avec `firstValueFrom()` et `from()`.

### 2.13 Mode strict et configuration

Les nouveaux projets activent le mode **strict**, qui comprend notamment `noImplicitAny`, `strictNullChecks`, `strictFunctionTypes` et `strictPropertyInitialization`.

```jsonc
// tsconfig.json
{
  "compilerOptions": { "strict": true, "noImplicitOverride": true, "noPropertyAccessFromIndexSignature": true },
  "angularCompilerOptions": { "strictTemplates": true, "strictInjectionParameters": true }
}
```

- **`strictNullChecks`** : `null` et `undefined` ne sont plus assignables à tout. Vous devez gérer l'absence de valeur.
- **`strictTemplates`** : les **gabarits** sont vérifiés comme du code TypeScript (propriétés, types des entrées, événements).
- **`strictInjectionParameters`** : une dépendance non résoluble est une erreur de compilation.

### 2.14 Pièges fréquents

- Utiliser `any` pour « faire taire » le compilateur : préférez `unknown` et un rétrécissement.
- Croire que les types protègent à l'exécution : une réponse HTTP **n'est pas validée** par ses types.
- Muter un objet ou un tableau typé `readonly` : utilisez une copie (`[...liste]`, `{ ...objet }`).
- Oublier `import type` : l'import d'un type seul peut alourdir ou casser l'exécution.

### Synthèse du chapitre 2

TypeScript apporte la **sécurité de typage** sans changer l'exécution. Retenez : l'**inférence**, `unknown` plutôt qu'`any`, les **unions discriminées**, les **génériques** et utilitaires (`Partial`, `Omit`…), les **classes** avec `readonly` / `protected`, les **modules** et `import type`, et le **mode strict**.

---

## 3. Installation et structure d'un projet

**Objectifs d'apprentissage.** Installer l'outillage, créer et lancer un projet, comprendre le rôle de **chaque fichier** généré, maîtriser les commandes du CLI, lire `angular.json`, gérer les environnements et résoudre les problèmes d'installation courants.

### 3.1 Prérequis : Node.js et gestionnaire de paquets

Angular s'exécute **sur Node.js** pendant le développement et la construction (le code final, lui, tourne dans le navigateur). Chaque version d'Angular exige une plage de versions de Node.js : vérifiez-la sur `angular.dev/reference/versions`. Utilisez une version **LTS** (numéro pair).

```bash
node --version        # ex. v22.x : doit être dans la plage supportée par votre version d'Angular
npm --version
```

- **Gestionnaires de paquets** : `npm` (par défaut), `pnpm`, `yarn`, `bun` ; le choix se fait à la création (`--package-manager`).
- **Gestionnaires de versions de Node** : `nvm`, `fnm`, `volta` permettent de basculer d'une version à l'autre selon les projets. Un fichier `.nvmrc` ou le champ `engines` de `package.json` documente la version attendue.
- **Fichier de verrouillage** (`package-lock.json`, `pnpm-lock.yaml`…) : il fige les versions exactes installées ; **versionnez-le** et utilisez `npm ci` en intégration continue pour des installations reproductibles.

### 3.2 Installer l'Angular CLI

Le **CLI** (*Command Line Interface*, commande `ng`) est l'outil central : il crée le projet, génère le code, compile, teste et met à jour.

```bash
npm install -g @angular/cli       # installation globale
ng version                        # affiche les versions du CLI, d'Angular, de Node, de TypeScript
ng help                           # liste des commandes
ng generate --help                # aide d'une commande

npx @angular/cli@latest new mon-app   # sans installation globale
```

**Installation globale ou `npx` ?** Une installation globale est pratique mais fige une version du CLI pour tous vos projets. Avec `npx`, vous utilisez toujours la version demandée. Dans un projet existant, le CLI **local** (`node_modules/.bin/ng`) est utilisé automatiquement quand vous lancez `ng` depuis le dossier du projet.

Au premier lancement, le CLI peut proposer d'activer l'**analyse d'usage** (`ng analytics`) et l'**autocomplétion du terminal** (`ng completion`) : ces choix sont facultatifs.

### 3.3 Créer un projet

```bash
ng new mon-app
```

Un **assistant** pose des questions : feuille de style (CSS, SCSS, Sass, Less), activation du **rendu serveur et du pré-rendu (SSR / SSG)**, et d'autres choix selon la version. Les réponses peuvent être données directement par options.

| Option | Effet |
| --- | --- |
| `--style=scss` | Préprocesseur de styles (`css`, `scss`, `sass`, `less`) |
| `--ssr` | Ajoute le rendu serveur (`@angular/ssr`) |
| `--routing` | Génère le fichier de routes |
| `--skip-git` | Ne crée pas de dépôt Git |
| `--skip-tests` | Ne génère pas les fichiers de test |
| `--skip-install` | N'installe pas les dépendances |
| `--prefix=xyz` | Préfixe des sélecteurs (par défaut `app`) |
| `--inline-template`, `--inline-style` | Gabarit / styles dans le fichier TypeScript |
| `--minimal` | Projet réduit au strict nécessaire |
| `--package-manager=pnpm` | Gestionnaire de paquets |
| `--directory=dossier` | Dossier de destination |
| `--create-application=false` | Espace de travail vide (pour bibliothèques / monorepos, chapitre 15) |
| `--dry-run` | Simule sans écrire de fichiers |

### 3.4 Lancer et utiliser le serveur de développement

```bash
cd mon-app
ng serve --open            # http://localhost:4200, ouvre le navigateur
ng serve --port 4300       # autre port
ng serve --host 0.0.0.0    # accessible depuis le réseau local
ng serve --configuration development
ng serve --proxy-config proxy.conf.json   # redirige /api vers un backend (évite CORS)
```

Le serveur (basé sur **Vite**) **recompile** à chaque modification et **recharge** la page, voire remplace les modules à chaud (*HMR*, *Hot Module Replacement*) pour les styles et les gabarits. Les erreurs de compilation s'affichent dans le terminal **et** dans le navigateur.

### 3.5 Structure d'un projet, fichier par fichier

```text
mon-app/
├── src/
│   ├── app/
│   │   ├── app.ts                  ← composant racine (classe `App`)
│   │   ├── app.html / app.css      ← gabarit et styles du composant racine
│   │   ├── app.config.ts           ← configuration de l'application (providers)
│   │   ├── app.routes.ts           ← définition des routes
│   │   └── app.spec.ts             ← test unitaire du composant racine
│   ├── index.html                  ← page hôte unique (<app-root>)
│   ├── main.ts                     ← point d'entrée : bootstrapApplication()
│   ├── styles.css                  ← styles globaux
│   └── assets/ ou public/          ← ressources statiques (images, polices, favicon)
├── angular.json                    ← configuration du CLI (build, serve, test…)
├── tsconfig.json                   ← configuration TypeScript de base
├── tsconfig.app.json / tsconfig.spec.json
├── package.json                    ← dépendances et scripts npm
├── .editorconfig, .gitignore       ← conventions d'éditeur et exclusions Git
├── .angular/                       ← cache de compilation (ne pas versionner)
├── node_modules/                   ← dépendances installées (ne pas versionner)
└── dist/                           ← sortie du build (après `ng build`)
```

| Fichier | Rôle détaillé |
| --- | --- |
| `package.json` | Liste les `dependencies` (embarquées dans l'application : `@angular/core`, `rxjs`…) et `devDependencies` (outillage : CLI, TypeScript, tests). Contient les **scripts** (`npm start` → `ng serve`, `npm test`, `npm run build`) |
| `angular.json` | Paramètres des projets et de leurs **cibles** (section 3.9) |
| `tsconfig.json` | Options TypeScript communes (mode strict, cible de compilation) et options du compilateur Angular |
| `tsconfig.app.json` | Fichiers inclus dans l'application (exclut les tests) |
| `tsconfig.spec.json` | Configuration des tests |
| `src/index.html` | Seule page HTML : contient `<app-root>` où l'application est montée, et `<base href="/">` pour le routeur |
| `src/main.ts` | Démarre l'application |
| `src/styles.css` | Styles **globaux** (réinitialisation, variables CSS, thème) ; les styles de composants restent dans le composant |
| `public/` ou `assets/` | Fichiers copiés tels quels dans la sortie et servis à la racine |
| `.angular/` | Cache du builder : peut être supprimé sans risque (`ng cache clean`) |

### 3.6 Le point d'entrée : `main.ts` et `app.config.ts`

Tout part de `main.ts`, qui appelle `bootstrapApplication()` avec le **composant racine** et la **configuration de l'application**.

```typescript
// src/main.ts
import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { App } from './app/app';

bootstrapApplication(App, appConfig).catch((erreur) => console.error(erreur));
```

```typescript
// src/app/app.config.ts
import { ApplicationConfig, provideBrowserGlobalErrorListeners, provideZonelessChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient, withFetch } from '@angular/common/http';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
    providers: [
        provideBrowserGlobalErrorListeners(),        // capture les erreurs globales du navigateur et les remonte à Angular
        provideZonelessChangeDetection(),            // détection des changements sans Zone.js
        provideRouter(routes),                       // active le routeur avec la liste de routes
        provideHttpClient(withFetch()),              // active HttpClient en s'appuyant sur fetch
    ],
};
```

**Concept clé : les fonctions `provideXxx()`.** Chaque fonctionnalité d'Angular s'active en ajoutant un **fournisseur** (*provider*) à la liste `providers`. Le chapitre 7 détaille ce mécanisme ; retenez ici que **`app.config.ts` est l'endroit où l'on configure l'application entière**. Les options (`withFetch()`, `withInterceptors()`, `withComponentInputBinding()`…) personnalisent chaque fonctionnalité.

```typescript
// src/app/app.ts : composant racine
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
    selector: 'app-root',
    imports: [RouterOutlet],
    template: `<h1>Bonjour Angular !</h1><router-outlet />`,
})
export class App {}
```

```html
<!-- src/index.html -->
<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8" />
    <title>Mon application</title>
    <base href="/" />
</head>
<body>
    <app-root></app-root>
</body>
</html>
```

**Ce qui se passe au démarrage** : le navigateur charge `index.html` et les scripts générés ; `main.ts` crée l'**injecteur racine** à partir de `appConfig`, instancie `App`, remplace `<app-root>` par son gabarit rendu, puis le routeur affiche la route correspondant à l'URL dans `<router-outlet />`.

> *(héritage)* Dans les projets « à modules », `main.ts` appelle `platformBrowserDynamic().bootstrapModule(AppModule)` et la configuration vit dans `app.module.ts` (voir 4.10).

### 3.7 Les commandes principales du CLI

| Commande | Rôle |
| --- | --- |
| `ng serve` | Serveur de développement avec rechargement |
| `ng build` | Compile pour la production dans `dist/` |
| `ng test` | Lance les tests unitaires (**Vitest** par défaut) |
| `ng generate` (`ng g`) | Génère du code (composant, service, directive, tube, garde, intercepteur, classe, interface, énumération, bibliothèque…) |
| `ng add <paquet>` | Installe **et configure** une bibliothèque (`@angular/material`, `@angular/pwa`, `@angular/ssr`) |
| `ng update` | Met à jour Angular et **migre le code** |
| `ng lint` | Analyse statique (après `ng add angular-eslint`) |
| `ng e2e` | Tests de bout en bout (après ajout d'un outil) |
| `ng deploy` | Déploiement (après ajout d'un *builder* de déploiement) |
| `ng extract-i18n` | Extrait les textes à traduire (chapitre 21) |
| `ng cache clean` | Vide le cache de compilation |
| `ng config` | Lit ou modifie `angular.json` |
| `ng version` | Versions installées |

**Générer du code** : les *schematics* produisent des fichiers conformes aux conventions.

```bash
ng generate component produits/liste        # composant dans src/app/produits/liste/
ng g c carte --inline-template --inline-style --skip-tests
ng g service api/utilisateur
ng g directive surbrillance
ng g pipe tronquer
ng g guard auth                             # propose le type de garde (fonctionnelle)
ng g interceptor jeton
ng g interface modeles/utilisateur
ng g enum role
ng g library ui-kit                         # bibliothèque (chapitre 15)
ng g component carte --dry-run              # simule : liste ce qui serait créé
```

`ng add` exécute un *schematic* fourni par la bibliothèque : en plus de `npm install`, il **modifie votre configuration** (fournisseurs, styles, `angular.json`). Préférez-le à `npm install` quand la bibliothèque le propose.

### 3.8 Le *builder* `application` : esbuild et Vite *(à jour)*

Le *builder* par défaut est **`@angular/build:application`**, fondé sur **esbuild** (compilation très rapide) et **Vite** (serveur de développement). Il gère aussi le **SSR** et le **pré-rendu**. Les anciens *builders* **webpack** (`@angular-devkit/build-angular`) sont **dépréciés** (v22) : voir le chapitre 28.

```bash
ng build                              # production par défaut : optimisation, minification, AOT
ng build --configuration development  # sans optimisation, avec cartes sources
ng build --stats-json                  # statistiques pour analyser le bundle (chapitre 20)
```

La sortie se trouve dans `dist/<nom-du-projet>/browser` (et `server` avec le SSR). Ce dossier est **statique** : il se déploie sur n'importe quel hébergeur de fichiers, à condition de rediriger les URL inconnues vers `index.html` (nécessaire au routeur).

### 3.9 Le fichier `angular.json`

Il décrit les **projets** de l'espace de travail et, pour chacun, des **cibles** (*targets*) dans la section `architect` : `build`, `serve`, `test`, etc. Chaque cible possède un *builder*, des **options** communes et des **configurations** nommées (`production`, `development`).

```jsonc
{
  "$schema": "./node_modules/@angular/cli/lib/config/schema.json",
  "version": 1,
  "newProjectRoot": "projects",
  "projects": {
    "mon-app": {
      "projectType": "application",
      "root": "",
      "sourceRoot": "src",
      "prefix": "app",
      "schematics": { "@schematics/angular:component": { "style": "scss" } },   // valeurs par défaut des générateurs
      "architect": {
        "build": {
          "builder": "@angular/build:application",
          "options": {
            "browser": "src/main.ts",
            "tsConfig": "tsconfig.app.json",
            "assets": [{ "glob": "**/*", "input": "public" }],
            "styles": ["src/styles.scss"]
          },
          "configurations": {
            "production": {
              "budgets": [{ "type": "initial", "maximumWarning": "500kB", "maximumError": "1MB" }],
              "outputHashing": "all"
            },
            "development": { "optimization": false, "extractLicenses": false, "sourceMap": true }
          },
          "defaultConfiguration": "production"
        },
        "serve": {
          "builder": "@angular/build:dev-server",
          "configurations": {
            "production": { "buildTarget": "mon-app:build:production" },
            "development": { "buildTarget": "mon-app:build:development" }
          },
          "defaultConfiguration": "development"
        },
        "test": { "builder": "@angular/build:unit-test" }
      }
    }
  }
}
```

| Option | Rôle |
| --- | --- |
| `assets` | Fichiers statiques copiés dans la sortie |
| `styles` / `scripts` | Fichiers globaux inclus dans la page |
| `polyfills` | Scripts de compatibilité (retirer `zone.js` en mode zoneless) |
| `budgets` | Seuils de taille : **avertissement ou échec** du build |
| `fileReplacements` | Remplace un fichier par un autre selon la configuration (environnements) |
| `outputHashing` | Empreinte dans les noms de fichiers pour le cache longue durée |
| `optimization`, `sourceMap` | Minification, cartes sources |
| `schematics` | Options par défaut des générateurs (style, préfixe, tests…) |

On modifie souvent ce fichier à la main, ou par `ng config projects.mon-app.architect.build.options.styles '["src/styles.scss"]'`.

### 3.10 Environnements et configuration

On distingue **configuration de build** (différente entre développement et production) et **configuration d'exécution**.

```bash
ng generate environments        # crée src/environments/environment.ts et environment.development.ts
```

```typescript
// src/environments/environment.ts (production)
export const environment = { production: true, urlApi: 'https://api.exemple.com' };
```

```typescript
// src/environments/environment.development.ts
export const environment = { production: false, urlApi: 'http://localhost:3000' };
```

La configuration `development` remplace `environment.ts` par `environment.development.ts` grâce à `fileReplacements`. Le code importe toujours `./environments/environment`.

> **Attention.** Ces valeurs sont **incluses dans le bundle** et lisibles par tout utilisateur : **aucun secret** (clé privée, mot de passe) dans les environnements front-end (chapitre 26). Pour une configuration modifiable **sans recompiler** (même image pour plusieurs environnements), chargez un fichier `config.json` au démarrage avec `provideAppInitializer` (chapitre 7).

### 3.11 Conventions de nommage *(à jour)*

- **Depuis la version 20**, le CLI ne génère plus les suffixes `.component`, `.service`, etc. : `compteur.ts` (classe `Compteur`) au lieu de `compteur.component.ts` (classe `CompteurComponent`). Les deux styles restent valides ; les migrations conservent les suffixes des projets existants.
- **Fichiers** en *kebab-case* (`carte-produit.ts`), **classes** en *PascalCase* (`CarteProduit`), **propriétés et méthodes** en *camelCase*.
- **Sélecteurs** de composants : *kebab-case* avec **préfixe** (`app-carte-produit`) ; sélecteurs de directives d'attribut en *camelCase* avec préfixe (`appSurbrillance`).
- Observables suffixés par `$` (`utilisateurs$`).
- Un fichier = **une responsabilité** (une classe principale).

### 3.12 Qualité du code : ESLint et Prettier

```bash
ng add angular-eslint         # configure ESLint avec des règles spécifiques à Angular
ng lint                       # lance l'analyse
npm install -D prettier       # formatage automatique
```

ESLint (`angular-eslint`) détecte des erreurs et applique des bonnes pratiques (ex. : `@for` sans `track`, imports inutilisés). **Prettier** formate le code. `.editorconfig` unifie indentation et fins de ligne entre éditeurs. Ajoutez des **hooks Git** (Husky, lint-staged) et exécutez lint + tests + build en **intégration continue**.

### 3.13 Dépannage courant

| Symptôme | Cause probable et remède |
| --- | --- |
| « Node.js version X is not supported » | Installer une version de Node compatible (voir `reference/versions`) |
| `ng` : commande introuvable | CLI non installé ou PATH incorrect : réinstaller ou utiliser `npx` |
| Port 4200 déjà utilisé | `ng serve --port 4300` ou arrêter l'autre processus |
| Erreurs étranges après mise à jour | `ng cache clean`, supprimer `node_modules` et `package-lock.json`, réinstaller |
| `EACCES` lors de l'installation globale | Problème de droits npm : utiliser un gestionnaire de versions de Node ou `npx` |
| Conflit de dépendances (*peer dependencies*) | Mettre à jour les bibliothèques ; `--legacy-peer-deps` en dernier recours |
| `Can't bind to 'x' since it isn't a known property` | Composant ou module non importé dans `imports` |
| `NG0303` / `NG0304` (élément inconnu) | Même cause : ajouter l'import du composant utilisé |

### Synthèse du chapitre 3

Un projet Angular repose sur **Node.js**, le **CLI** (`ng`) et trois fichiers de configuration (`package.json`, `angular.json`, `tsconfig.json`). Le démarrage passe par `main.ts` → `bootstrapApplication(App, appConfig)` ; **`app.config.ts`** centralise les fournisseurs (routeur, HTTP, détection des changements). Le *builder* `application` (esbuild + Vite) compile en production avec **AOT**, optimisation et budgets.

---

## 4. Composants

**Objectifs d'apprentissage.** Définir un composant et en maîtriser l'anatomie ; créer des composants **autonomes** ; faire communiquer parent et enfant avec `input()`, `output()` et `model()` ; interroger la vue avec `viewChild()` ; connaître le **cycle de vie** et ses hooks modernes ; projeter du contenu ; maîtriser l'**encapsulation des styles** et les **liaisons sur l'hôte** ; savoir lire du code à base de `NgModule`.

### 4.1 Les briques d'une application

Une application Angular est un **arbre de composants**. Un **composant** est une classe TypeScript décorée par `@Component`, qui associe quatre éléments :

| Élément | Rôle |
| --- | --- |
| **Classe TypeScript** | Données (état) et logique (méthodes) |
| **Gabarit** (*template*) | HTML avec syntaxe Angular, décrit **ce qui est affiché** |
| **Styles** | CSS **encapsulé** : il ne s'applique qu'à ce composant |
| **Métadonnées** `@Component` | Sélecteur, imports, gabarit, styles, stratégie de détection… |

**Pourquoi des composants ?** Ils permettent de **découper** une interface en morceaux **réutilisables, testables et isolés**. Un bouton, une carte de produit, une page entière : tout est composant.

### 4.2 Anatomie d'un composant autonome (*standalone*) *(à jour)*

Un composant **autonome** déclare **lui-même** ses dépendances (autres composants, directives, tubes) dans sa propriété `imports` : **aucun `NgModule` n'est nécessaire**. C'est le mode **par défaut depuis la version 19** (la mention `standalone: true` est donc implicite).

```typescript
// src/app/compteur.ts
import { Component, signal, ChangeDetectionStrategy } from '@angular/core';

@Component({
    selector: 'app-compteur',                   // balise : <app-compteur />
    imports: [],                                 // composants, directives, tubes utilisés dans le gabarit
    template: `
        <h2>Compteur : {{ valeur() }}</h2>
        <button (click)="incrementer()">+1</button>
    `,
    styles: `
        h2 { color: steelblue; }
    `,
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class Compteur {
    protected readonly valeur = signal(0);       // visible du gabarit, pas de l'extérieur
    incrementer(): void {                         // publique : appelable depuis un parent
        this.valeur.update((v) => v + 1);
    }
}
```

**Les principales métadonnées de `@Component` :**

| Propriété | Rôle |
| --- | --- |
| `selector` | Comment le composant est utilisé dans un gabarit (voir ci-dessous) |
| `template` / `templateUrl` | Gabarit **en ligne** / **fichier** séparé |
| `styles` / `styleUrl` / `styleUrls` | Styles en ligne / fichier / plusieurs fichiers |
| `imports` | Dépendances utilisables dans le gabarit |
| `providers` / `viewProviders` | Services propres au composant (chapitre 7) |
| `changeDetection` | Stratégie de détection des changements (chapitre 18) |
| `encapsulation` | Isolation des styles (4.8) |
| `host` | Liaisons sur l'élément hôte (4.9) |
| `hostDirectives` | Directives appliquées à l'hôte (chapitre 6) |
| `animations` | Animations *(héritage)* |

**Types de sélecteurs.** `selector: 'app-carte'` (élément, le cas habituel), `'[appCarte]'` (attribut), `'.carte'` (classe), ou combinés (`'button[appBouton]'`). Pour un composant, on utilise presque toujours un **sélecteur d'élément en *kebab-case* avec préfixe** pour éviter les collisions avec les éléments HTML natifs.

**Gabarit et styles séparés.** Dès que le gabarit dépasse quelques lignes, utilisez des fichiers :

```typescript
@Component({
    selector: 'app-profil',
    templateUrl: './profil.html',
    styleUrl: './profil.css',
})
export class Profil {}
```

**Génération** : `ng generate component compteur` crée `compteur.ts`, `compteur.html`, `compteur.css`, `compteur.spec.ts`.

### 4.3 Utiliser un composant dans un autre

Pour utiliser `Compteur` dans un autre composant, on l'**importe** (instruction TypeScript) **et** on l'ajoute à `imports` (déclaration Angular). Les deux sont nécessaires.

```typescript
// src/app/accueil.ts
import { Component } from '@angular/core';
import { Compteur } from './compteur';

@Component({
    selector: 'app-accueil',
    imports: [Compteur],                          // sans cette ligne : erreur « 'app-compteur' is not a known element »
    template: `
        <h1>Accueil</h1>
        <app-compteur />
        <app-compteur />                          <!-- chaque occurrence = une instance indépendante -->
    `,
})
export class Accueil {}
```

Les balises **auto-fermantes** (`<app-compteur />`) sont autorisées dans les gabarits modernes. Chaque occurrence d'un composant crée **une nouvelle instance de la classe**, avec son propre état.

### 4.4 Communication parent → enfant : entrées et sorties avec les **signaux** *(à jour)*

Un composant enfant expose une **API** : ce qu'il **reçoit** (entrées) et ce qu'il **émet** (sorties). Les fonctions **`input()`**, **`output()`** et **`model()`** remplacent les décorateurs `@Input()` / `@Output()`.

```typescript
// src/app/carte-produit.ts
import { Component, input, output, model, computed } from '@angular/core';
import { CurrencyPipe } from '@angular/common';

@Component({
    selector: 'app-carte-produit',
    imports: [CurrencyPipe],
    template: `
        <article>
            <h3>{{ nom() }}</h3>
            <p>{{ prixTtc() | currency: 'EUR' }} (quantité : {{ quantite() }})</p>
            <button (click)="ajouter.emit(nom())">Ajouter</button>
        </article>
    `,
})
export class CarteProduit {
    nom = input.required<string>();                              // entrée OBLIGATOIRE
    prix = input(0);                                              // entrée avec valeur par défaut (type number déduit)
    tva = input(0.2, { alias: 'tauxTva', transform: Number });    // alias public + transformation de la valeur reçue

    ajouter = output<string>();                                   // sortie typée
    quantite = model(1);                                          // entrée + sortie : liaison bidirectionnelle

    prixTtc = computed(() => this.prix() * (1 + this.tva()));
}
```

Utilisation dans le parent :

```typescript
// src/app/catalogue.ts
import { Component, signal } from '@angular/core';
import { CarteProduit } from './carte-produit';

@Component({
    selector: 'app-catalogue',
    imports: [CarteProduit],
    template: `
        <app-carte-produit [nom]="'Livre'" [prix]="12.5" tauxTva="0.055" (ajouter)="surAjout($event)" [(quantite)]="qte" />
        <p>Quantité choisie : {{ qte() }}</p>
    `,
})
export class Catalogue {
    protected readonly qte = signal(1);
    protected surAjout(nom: string): void {
        console.log(`Ajouté : ${nom}`);
    }
}
```

**Règles à retenir**

- Une **entrée** est un **signal en lecture seule** : on la lit avec `nom()`, on **ne peut pas** l'écrire depuis le composant. Seul le parent la modifie.
- `input.required<T>()` : le compilateur **exige** que le parent la fournisse. `input<T>(valeurParDéfaut)` : facultative.
- `transform` convertit la valeur reçue (ex. `booleanAttribute`, `numberAttribute`, ou votre fonction).
- `alias` change le nom public de l'entrée (utile pour les directives, ex. `appSurbrillance`).
- Une **sortie** `output<T>()` émet avec `.emit(valeur)` ; le parent écoute avec `(nomSortie)="..."` et lit la valeur par `$event`.
- `model()` combine entrée et sortie nommée `xChange` : le parent lie avec `[(x)]="signal"` (« banane dans la boîte »). L'enfant peut **écrire** `quantite.set(2)` et le parent est notifié.

| API signal | Remplace | Particularités |
| --- | --- | --- |
| `input<T>()` / `input.required<T>()` | `@Input()` | Lecture par `valeur()`, réactif, typé strictement |
| `output<T>()` | `@Output()` + `EventEmitter` | `.emit(valeur)` |
| `model<T>()` | `@Input()` + `@Output() xChange` | Liaison **bidirectionnelle** `[(x)]` |
| `viewChild()`, `viewChildren()`, `contentChild()`, `contentChildren()` | `@ViewChild` etc. | Requêtes sous forme de signaux |

**Réagir à un changement d'entrée.** Plus besoin de `ngOnChanges` : utilisez `computed()` pour dériver une valeur, `effect()` pour un effet de bord, ou `linkedSignal()` pour un état local réinitialisé par l'entrée (chapitre 8).

> *(héritage)* Les décorateurs restent valides : `@Input() nom!: string;`, `@Input({ required: true })`, `@Output() ajouter = new EventEmitter<string>();`. Migration automatique : `ng generate @angular/core:signal-input-migration` et `output-migration` (chapitre 28).

**Le principe « données descendantes, événements montants ».** Les données circulent du parent vers l'enfant (entrées) ; les événements remontent de l'enfant vers le parent (sorties). L'enfant ne modifie pas l'état du parent directement : il **notifie**. Cela rend le flux **prévisible** et les composants **réutilisables**.

### 4.5 Requêtes sur la vue et le contenu : `viewChild`, `contentChild`

Les **requêtes** donnent accès à un élément, un composant enfant ou une directive de la **vue** du composant.

```typescript
// src/app/recherche.ts
import { Component, viewChild, ElementRef, afterNextRender } from '@angular/core';

@Component({
    selector: 'app-recherche',
    template: `<input #champ type="search" />`,
})
export class Recherche {
    champ = viewChild.required<ElementRef<HTMLInputElement>>('champ');   // cible la variable de référence #champ

    constructor() {
        afterNextRender(() => this.champ().nativeElement.focus());          // après le premier rendu
    }
}
```

| Fonction | Cible |
| --- | --- |
| `viewChild(cible)` | Premier élément **de la vue** (peut être `undefined`) |
| `viewChild.required(cible)` | Idem, mais **doit** exister (erreur sinon) |
| `viewChildren(cible)` | **Tous** les éléments correspondants (signal de tableau) |
| `contentChild()` / `contentChildren()` | Éléments du **contenu projeté** (voir 4.7) |

La **cible** peut être une variable de référence (`'champ'`), une classe de composant ou de directive (`CarteProduit`). L'option `{ read: ViewContainerRef }` choisit **ce qu'on lit** sur l'élément. Les requêtes de type signal sont **réactives** : on peut les utiliser dans `computed()` et `effect()`.

> **Piège.** Une requête n'est résolue qu'**après le rendu** : lire `champ()` dans le constructeur directement donne une erreur ; utilisez `afterNextRender` ou un `effect`. Une requête ne voit pas non plus les éléments situés dans un bloc `@if` **faux**.

*(héritage)* `@ViewChild('champ') champ!: ElementRef;` avec `ngAfterViewInit`.

### 4.6 Cycle de vie d'un composant

Angular crée, met à jour et détruit les composants. Il appelle des **méthodes de cycle de vie** (*hooks*) que la classe peut implémenter.

| Hook | Moment | Usage typique |
| --- | --- | --- |
| `constructor` | Création de l'instance | Injection de dépendances, initialisation de champs |
| `ngOnChanges` | Une entrée **classique** (`@Input`) change | Réagir à un changement d'entrée *(héritage)* |
| `ngOnInit` | Après la première mise à jour des entrées | Chargement initial de données |
| `ngDoCheck` | À chaque détection de changements | Rare |
| `ngAfterContentInit` / `ngAfterContentChecked` | Contenu projeté initialisé / vérifié | Accès au contenu projeté |
| `ngAfterViewInit` / `ngAfterViewChecked` | Vue et enfants initialisés / vérifiés | Accès au DOM, aux requêtes de vue |
| `ngOnDestroy` | Avant la destruction | **Nettoyage** (minuteries, abonnements) |

```typescript
import { Component, OnInit, OnDestroy } from '@angular/core';

@Component({ selector: 'app-horloge', template: `<p>Horloge en marche (voir la console)</p>` })
export class Horloge implements OnInit, OnDestroy {
    private minuteur?: ReturnType<typeof setInterval>;
    ngOnInit(): void { this.minuteur = setInterval(() => console.log('tic'), 1000); }
    ngOnDestroy(): void { clearInterval(this.minuteur); }    // sans cela : fuite mémoire
}
```

**Constructeur ou `ngOnInit` ?** Le constructeur sert à l'**injection** et à l'initialisation simple ; il ne doit pas contenir de logique lourde. Les entrées classiques ne sont **pas encore** disponibles dans le constructeur (les entrées signaux se lisent, elles, dès que le parent les a fournies).

#### Hooks modernes *(à jour)*

Avec les signaux, on préfère des **API fonctionnelles** :

| API | Rôle |
| --- | --- |
| `effect(() => …)` | Réagit aux changements de signaux (effets de bord) |
| `afterNextRender()` / `afterEveryRender()` | Code dépendant du **DOM** ; **jamais exécuté côté serveur** (SSR) |
| `inject(DestroyRef).onDestroy(fn)` | Nettoyage sans implémenter `OnDestroy` |
| `takeUntilDestroyed()` | Désabonnement automatique des observables |

```typescript
import { Component, DestroyRef, inject } from '@angular/core';

@Component({ selector: 'app-horloge-moderne', template: `<p>Horloge en marche (voir la console)</p>` })
export class HorlogeModerne {
    constructor() {
        const id = setInterval(() => console.log('tic'), 1000);
        inject(DestroyRef).onDestroy(() => clearInterval(id));       // nettoyage au plus près de la création
    }
}
```

L'intérêt : **création et nettoyage au même endroit**, plus facile à factoriser dans des fonctions réutilisables.

### 4.7 Projection de contenu (`ng-content`)

La **projection de contenu** permet à un composant de recevoir du HTML (ou d'autres composants) écrit **entre ses balises** par le parent, et de l'afficher à l'endroit voulu. C'est la base des composants de **mise en page** (cartes, panneaux, dialogues).

```typescript
// src/app/panneau.ts
import { Component } from '@angular/core';

@Component({
    selector: 'app-panneau',
    template: `
        <header><ng-content select="[titre]" /></header>     <!-- « slot » nommé : éléments portant l'attribut titre -->
        <section><ng-content /></section>                      <!-- slot par défaut : tout le reste -->
        <footer><ng-content select="app-pied">Pied par défaut</ng-content></footer>   <!-- contenu de repli (v18+) -->
    `,
})
export class Panneau {}
```

```typescript
// src/app/page.ts
import { Component } from '@angular/core';
import { Panneau } from './panneau';

@Component({
    selector: 'app-page',
    imports: [Panneau],
    template: `
        <app-panneau>
            <h2 titre>Mon titre</h2>
            <p>Le contenu du panneau</p>
        </app-panneau>
    `,
})
export class Page {}
```

- `select` accepte un **sélecteur CSS** (`[titre]`, `.entete`, `app-pied`). `ngProjectAs` permet de faire passer un élément pour un autre.
- Le contenu projeté est **créé par le parent**, même s'il est affiché par l'enfant : ses liaisons s'évaluent dans le contexte du **parent**.
- Le composant peut interroger ce contenu avec `contentChild()` / `contentChildren()` et réagir après `ngAfterContentInit`.
- Pour projeter un **gabarit** que l'enfant instancie à la demande, on utilise `ng-template` et `NgTemplateOutlet` (chapitre 5).

### 4.8 Encapsulation des styles

Par défaut, les styles d'un composant **ne s'appliquent qu'à lui** : Angular ajoute des attributs générés (`_ngcontent-xyz`) aux éléments et réécrit les sélecteurs. Les styles du parent **ne fuient pas** dans l'enfant, et inversement.

| Mode | Effet |
| --- | --- |
| `Emulated` (**défaut**) | Isolation simulée par attributs générés |
| `ShadowDom` | **Vrai Shadow DOM** natif : isolation totale, y compris des styles globaux |
| `None` | Aucun isolement : styles **globaux** |

```typescript
import { Component, ViewEncapsulation } from '@angular/core';

@Component({
    selector: 'app-isole',
    template: `<p>Contenu isolé dans un Shadow DOM</p>`,
    styles: `p { color: seagreen; }`,
    encapsulation: ViewEncapsulation.ShadowDom,
})
export class Isole {}
```

**Sélecteurs spéciaux**

- `:host` : l'élément hôte du composant (`:host { display: block; }` — **à définir** car un élément personnalisé est `inline` par défaut). `:host(.actif)` : hôte portant la classe `actif`.
- `:host-context(.sombre)` : hôte dont un ancêtre porte la classe.
- `::ng-deep` : traverse l'encapsulation — **déprécié**, à éviter.

**Comment personnaliser un composant enfant de l'extérieur ?** Par des **variables CSS** (propriétés personnalisées) qui traversent l'encapsulation : l'enfant utilise `color: var(--couleur-carte, black)`, le parent définit `--couleur-carte`.

### 4.9 Liaisons sur l'hôte

L'**hôte** est l'élément qui porte le sélecteur (`<app-bouton>`). La propriété **`host`** de `@Component` (ou `@Directive`) y déclare classes, attributs, propriétés et écouteurs.

```typescript
import { Component, signal } from '@angular/core';

@Component({
    selector: 'app-bouton',
    host: {
        class: 'bouton',                          // classe statique
        '[class.actif]': 'actif()',               // classe conditionnelle
        '[attr.aria-pressed]': 'actif()',         // attribut dynamique (accessibilité)
        '[style.opacity]': 'actif() ? 1 : 0.6',   // style dynamique
        '(click)': 'basculer()',                  // écouteur d'événement
        '(keydown.escape)': 'actif.set(false)',   // filtre de touche
    },
    template: `<ng-content />`,
})
export class Bouton {
    protected readonly actif = signal(false);
    protected basculer(): void { this.actif.update((a) => !a); }
}
```

> **Bonne pratique.** Préférez la propriété **`host`** aux décorateurs `@HostBinding` et `@HostListener` *(héritage)* : tout est au même endroit, mieux typé et vérifié par le compilateur.

### 4.10 Les modules `NgModule` *(héritage)*

Avant la version 14, tout composant devait être **déclaré dans un `NgModule`**, lequel précisait ses dépendances et ce qu'il exportait. Ce modèle est toujours **supporté** mais **n'est plus recommandé** : il ajoutait du code « de liaison » et compliquait le chargement paresseux.

```typescript
// app.module.ts (héritage)
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { CompteurComponent } from './compteur.component';

@NgModule({
    declarations: [AppComponent, CompteurComponent],   // composants, directives, tubes possédés par ce module
    imports: [BrowserModule, FormsModule],             // modules dont on utilise les éléments
    exports: [],                                       // ce qu'on met à disposition des autres modules
    providers: [],                                     // services
    bootstrap: [AppComponent],                         // composant racine
})
export class AppModule {}
```

|  | **Autonome** (*standalone*) | **`NgModule`** *(héritage)* |
| --- | --- | --- |
| Dépendances | `imports` du composant | `declarations` + `imports` du module |
| Amorçage | `bootstrapApplication(App, config)` | `platformBrowserDynamic().bootstrapModule(AppModule)` |
| Services globaux | `provide…()` dans `app.config.ts` | `providers` du module |
| Chargement paresseux | `loadComponent` / `loadChildren` vers des routes | `loadChildren` vers un module |
| Complexité | Moindre | Plus de code de liaison |

**Coexistence.** Un composant autonome peut importer un `NgModule` (ex. `MatButtonModule`, `FormsModule`) et un module peut importer un composant autonome. **Migration** : `ng generate @angular/core:standalone` (trois passes : *convert-to-standalone*, *prune-ng-modules*, *standalone-bootstrap*) — voir chapitre 28.

### 4.11 Création dynamique de composants (aperçu)

On peut créer un composant **par programme** (boîtes de dialogue, widgets chargés à la demande) avec `ViewContainerRef.createComponent(Classe)` ou `createComponent()` (fonction), combiné à un import dynamique pour charger son code seulement au besoin (chapitre 19). Les entrées se fixent avec `componentRef.setInput('nom', valeur)`.

### 4.12 Bonnes pratiques

- Composants **petits** et à responsabilité unique : distinguer **présentation** (reçoit des entrées, émet des sorties) et **conteneur** (obtient les données via des services).
- `ChangeDetectionStrategy.OnPush` (**défaut depuis la v22**) ; état dans des **signaux**.
- `protected` pour ce qui n'est utilisé que dans le gabarit, `readonly` pour les signaux.
- Pas de **logique lourde** dans le gabarit : utilisez `computed()`.
- Pas d'accès direct au DOM : passez par le gabarit, les liaisons, ou `afterNextRender`.
- **Nettoyer** ce que vous créez (`DestroyRef`).
- Un composant **ne modifie pas** ses entrées : il émet un événement.

### Synthèse du chapitre 4

Un composant = **classe + gabarit + styles + métadonnées**. Autonome par défaut, il déclare ses dépendances dans `imports`. L'API publique se définit avec **`input()`**, **`output()`** et **`model()`**, les requêtes avec **`viewChild()`**. Le nettoyage passe par **`DestroyRef`**, le code dépendant du DOM par **`afterNextRender`**. Les styles sont **encapsulés** ; l'hôte se configure via **`host`**. Les `NgModule` sont de l'héritage.

---

## 5. Modèles et liaison de données

**Objectifs d'apprentissage.** Maîtriser la syntaxe des gabarits : interpolation, liaisons de propriétés, d'attributs, de classes, de styles et d'événements ; la liaison bidirectionnelle ; le **flux de contrôle** `@if`, `@for`, `@switch`, `@let` ; les expressions de gabarit et leurs limites ; les variables de référence ; `ng-template` et `ng-container`.

### 5.1 Le gabarit : HTML enrichi

Un **gabarit** (*template*) est du HTML **valide** auquel Angular ajoute une syntaxe : interpolations, liaisons, blocs de contrôle, directives. Le compilateur le transforme en instructions JavaScript efficaces (AOT). Un gabarit se lit toujours **dans le contexte de la classe du composant** : ses propriétés et méthodes y sont accessibles directement (`valeur()` signifie `this.valeur()`).

### 5.2 Les quatre formes de liaison

| Forme | Syntaxe | Sens |
| --- | --- | --- |
| **Interpolation** | `{{ expression }}` | Classe → vue (texte) |
| **Liaison de propriété** | `[propriete]="expression"` | Classe → vue (propriété du DOM, entrée d'un composant) |
| **Liaison d'événement** | `(evenement)="action()"` | Vue → classe |
| **Liaison bidirectionnelle** | `[(ngModel)]="x"` / `[(x)]="signal"` | Les deux sens |

```typescript
// src/app/demo.ts
import { Component, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
    selector: 'app-demo',
    imports: [FormsModule],
    template: `
        <h1>{{ titre() }}</h1>                                           <!-- interpolation -->
        <img [src]="urlImage()" [alt]="titre()" />                      <!-- propriété -->
        <button (click)="saluer()" [disabled]="!actif()">Salut</button>  <!-- événement + propriété -->
        <input [value]="nom()" (input)="nom.set($any($event.target).value)" />
        <input [(ngModel)]="texte" />                                   <!-- bidirectionnelle -->
    `,
})
export class Demo {
    titre = signal('Mon titre');
    urlImage = signal('/img/logo.png');
    actif = signal(true);
    nom = signal('');
    texte = '';
    saluer(): void { console.log('Salut !'); }
}
```

#### Interpolation

`{{ expression }}` évalue l'expression, la **convertit en chaîne** et l'affiche comme **texte** (jamais comme HTML : les caractères `<` et `>` sont échappés, ce qui protège du XSS). Elle s'utilise dans le contenu des éléments et dans les attributs (`title="Bonjour {{ nom() }}"`).

#### Propriété ou attribut ?

Distinction fondamentale : un **attribut HTML** (`<input value="a">`) est la valeur **initiale** écrite dans le HTML ; une **propriété du DOM** (`input.value`) est la valeur **courante** de l'objet. `[value]="x"` lie la **propriété**. Pour les cas sans propriété équivalente (ARIA, `colspan`, `data-*`), on utilise la liaison d'**attribut** `[attr.nom]`.

```html
<td [attr.colspan]="colonnes()" [attr.aria-label]="libelle()">Cellule</td>
<button [attr.data-id]="produit.id">Voir</button>
```

Si l'expression vaut `null` ou `undefined`, l'attribut est **retiré** du DOM.

La même syntaxe `[nom]="…"` lie aussi une **entrée d'un composant** (`<app-carte [nom]="produit.nom" />`) : Angular cherche d'abord une entrée de ce nom, sinon une propriété du DOM.

#### Liaison de classes et de styles

```html
<div [class.actif]="estActif()">Une classe conditionnelle</div>
<div [class]="{ rouge: erreur(), gras: important() }">Plusieurs classes (objet)</div>
<div [class]="['carte', theme()]">Plusieurs classes (tableau)</div>
<div [style.width.px]="largeur()" [style.color]="couleur()">Styles dynamiques</div>
<div [style]="{ 'background-color': fond(), padding: '8px' }">Styles (objet)</div>
```

Les liaisons natives `[class]` et `[style]` acceptent chaînes, objets et tableaux : elles suffisent presque toujours et remplacent `NgClass` et `NgStyle` (chapitre 6). Le suffixe d'unité (`.px`, `.%`, `.rem`) s'ajoute après le nom de la propriété.

#### Liaison d'événements

```html
<button (click)="enregistrer()">Enregistrer</button>
<input (input)="surSaisie($event)" (keyup.enter)="valider()" (keydown.escape)="annuler()" />
<form (submit)="envoyer($event)">…</form>
<a href="/x" (click)="$event.preventDefault(); ouvrir()">Lien</a>
```

- **`$event`** est l'objet d'événement natif (`MouseEvent`, `KeyboardEvent`…) ou la valeur émise par une `output()` d'un composant enfant.
- **Filtres de touches** : `(keyup.enter)`, `(keydown.escape)`, `(keydown.control.s)`.
- Plusieurs instructions sont possibles, séparées par `;`. Appelez de préférence **une seule méthode**.
- Typage : dans un gabarit, `$event.target` est de type `EventTarget | null` ; pour lire `value`, on passe par une **variable de référence** (`#champ` puis `champ.value`) ou une méthode qui reçoit l'événement et le type.

```typescript
// src/app/champ-texte.ts
import { Component, signal } from '@angular/core';

@Component({
    selector: 'app-champ-texte',
    template: `
        <input #champ (input)="texte.set(champ.value)" />    <!-- variable de référence : typé HTMLInputElement -->
        <p>{{ texte() }}</p>
    `,
})
export class ChampTexte {
    protected readonly texte = signal('');
}
```

#### Liaison bidirectionnelle

La syntaxe `[(x)]` (« banane dans la boîte ») est un **raccourci** de `[x]="v" (xChange)="v = $event"`. Elle fonctionne avec :

- `ngModel` (module `FormsModule`) sur les champs de formulaire ;
- une `model()` d'un composant enfant (chapitre 4).

```typescript
// src/app/champ.ts
import { Component, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
    selector: 'app-champ',
    imports: [FormsModule],
    template: `<input [(ngModel)]="nom" /> <p>{{ nom() }}</p>`,
})
export class Champ {
    nom = signal('');     // [(ngModel)] fonctionne directement avec un signal inscriptible
}
```

### 5.3 Flux de contrôle : `@if`, `@for`, `@switch` *(à jour)*

Depuis la **version 17**, le **flux de contrôle intégré** remplace les directives structurelles `*ngIf`, `*ngFor` et `*ngSwitch` : syntaxe plus lisible, **aucun import**, meilleures performances, et vérification de types plus fine.

#### `@if`

```html
@if (utilisateur(); as u) {
    <p>Bonjour {{ u.nom }}</p>
} @else if (chargement()) {
    <p>Chargement…</p>
} @else {
    <p>Veuillez vous connecter.</p>
}
```

La clause `as u` **capture** la valeur évaluée (utile pour éviter de recalculer, et pour **affiner le type** : `u` n'est plus `null`). L'affichage dépend de la **véracité** de l'expression (`null`, `undefined`, `0`, `''`, `false` sont faux).

#### `@for`

```html
<ul>
    @for (produit of produits(); track produit.id; let i = $index, premier = $first) {
        <li [class.premier]="premier">{{ i + 1 }}. {{ produit.nom }}</li>
    } @empty {
        <li>Aucun produit</li>
    }
</ul>
```

- **`track` est obligatoire.** Il indique comment **identifier** chaque élément (`track produit.id`, ou `track $index` pour des valeurs simples non réordonnées). Quand la liste change, Angular **réutilise** les nœuds du DOM correspondant aux mêmes identifiants au lieu de tout recréer : gain de performance majeur et conservation de l'état des éléments (saisie, focus).
- **Variables contextuelles** : `$index`, `$count`, `$first`, `$last`, `$even`, `$odd`, que l'on peut renommer avec `let`.
- **`@empty`** : bloc affiché si la collection est vide.
- Itère tout objet **itérable** (tableaux, `Set`, `Map`…). Pour itérer un objet simple, utilisez le tube `keyvalue`.

> **Pièges.** Un `track` sur un identifiant **non unique** provoque des erreurs et des comportements étranges. `track $index` sur une liste qui s'insère ou se trie recrée inutilement des éléments.

#### `@switch`

```html
@switch (role()) {
    @case ('admin') { <p>Panneau d'administration</p> }
    @case ('editeur') { <p>Espace d'édition</p> }
    @default { <p>Accès refusé</p> }
}
```

La comparaison utilise l'égalité **stricte** (`===`) ; il n'y a **pas de « chute »** (*fall-through*) comme avec le `switch` JavaScript : pas de `break`.

#### Variables locales : `@let`

```html
@let total = prix() * quantite();
<p>Total : {{ total | currency: 'EUR' }}</p>
@let utilisateurCourant = utilisateur$ | async;
```

`@let` déclare une variable **en lecture seule** dans le gabarit, visible dans le bloc courant et ses descendants. Elle évite de répéter une expression ou un tube `async`.

#### Exemple complet

```typescript
// src/app/flux-controle.ts
import { Component, signal } from '@angular/core';
import { CurrencyPipe } from '@angular/common';

interface Produit { id: number; nom: string; }
type Role = 'admin' | 'editeur' | 'lecteur';

@Component({
    selector: 'app-flux-controle',
    imports: [CurrencyPipe],
    template: `
        @if (utilisateur(); as u) {
            <p>Bonjour {{ u.nom }}</p>
        } @else if (chargement()) {
            <p>Chargement…</p>
        } @else {
            <p>Veuillez vous connecter.</p>
        }

        <ul>
            @for (produit of produits(); track produit.id; let i = $index, premier = $first) {
                <li [class.premier]="premier">{{ i + 1 }}. {{ produit.nom }}</li>
            } @empty {
                <li>Aucun produit</li>
            }
        </ul>

        @switch (role()) {
            @case ('admin') { <p>Panneau d'administration</p> }
            @case ('editeur') { <p>Espace d'édition</p> }
            @default { <p>Accès refusé</p> }
        }

        @let total = prix() * quantite();
        <p>Total : {{ total | currency: 'EUR' }}</p>
    `,
})
export class FluxControle {
    protected readonly utilisateur = signal<{ nom: string } | null>({ nom: 'Alice' });
    protected readonly chargement = signal(false);
    protected readonly produits = signal<Produit[]>([{ id: 1, nom: 'Livre' }, { id: 2, nom: 'Stylo' }]);
    protected readonly role = signal<Role>('editeur');
    protected readonly prix = signal(12.5);
    protected readonly quantite = signal(2);
}
```

#### Vues différées : `@defer`

Chargement **paresseux** d'un morceau de gabarit : voir le chapitre 19.

#### Correspondance avec l'ancienne syntaxe *(héritage)*

| Ancienne syntaxe | Nouvelle syntaxe |
| --- | --- |
| `*ngIf="x; else autre"` | `@if (x) { … } @else { … }` |
| `*ngFor="let i of liste; trackBy: fn"` | `@for (i of liste; track i.id) { … }` |
| `[ngSwitch]` / `*ngSwitchCase` | `@switch` / `@case` |

`NgIf`, `NgFor` et `NgSwitch` sont **dépréciés** depuis la version 20. Migration automatique : `ng generate @angular/core:control-flow`. Rappel : le `*` des anciennes directives est un **sucre syntaxique** qui enveloppe l'élément dans un `<ng-template>`.

### 5.4 Expressions de gabarit

Les expressions sont du TypeScript **simplifié**, volontairement limité pour rester **sans effet de bord** et rapide.

**Autorisé** : littéraux, opérateurs arithmétiques, de comparaison et logiques, opérateur ternaire, cha înage optionnel `?.`, coalescence nulle `??`, appels de méthodes et de signaux, tubes (`|`).

**Interdit** : affectations (sauf dans les gestionnaires d'événements), `new`, opérateurs `++` / `--`, instructions (`if`, `for`), accès aux globales comme `window` ou `console` (exposez-les depuis la classe si besoin).

```html
{{ prix() * 1.2 | currency }}
{{ utilisateur()?.adresse?.ville ?? 'Inconnue' }}
{{ liste().length > 0 ? 'Oui' : 'Non' }}
<button (click)="a = 1; b = 2">Plusieurs instructions</button>
```

**Bonnes pratiques d'expressions**

- Elles doivent être **rapides** et **idempotentes** : elles s'exécutent à chaque vérification de la vue. Pas d'appel réseau, pas de calcul lourd, pas de modification d'état.
- Pour une dérivation coûteuse ou répétée, utilisez **`computed()`** (mémoïsé) plutôt qu'une méthode appelée dans le gabarit.
- Le compilateur vérifie les types (`strictTemplates`) : une propriété inexistante est une **erreur de compilation**.

### 5.5 Variables de référence de gabarit

Une **variable de référence** (`#nom`) désigne un élément du DOM, un composant ou une directive, et reste utilisable **dans tout le gabarit**.

```typescript
// src/app/reference.ts
import { Component } from '@angular/core';
import { Compteur } from './compteur';

@Component({
    selector: 'app-reference',
    imports: [Compteur],
    template: `
        <input #nom />
        <button (click)="envoyer(nom.value)">Envoyer</button>

        <app-compteur #c />
        <button (click)="c.incrementer()">Depuis le parent</button>
    `,
})
export class Reference {
    protected envoyer(valeur: string): void { console.log(valeur); }
}
```

Sur un élément HTML, la variable désigne l'**élément** (`HTMLInputElement`) ; sur un composant, l'**instance** (seuls les membres publics sont accessibles) ; avec `exportAs` ou `#f="ngForm"`, l'instance d'une directive.

### 5.6 Gabarits réutilisables : `ng-template`, `ng-container`

- **`<ng-template>`** : un gabarit **non rendu** par défaut ; on le rend à la demande.
- **`<ng-container>`** : un **regroupement logique** qui **n'ajoute aucun élément** au DOM.
- **`NgTemplateOutlet`** : insère un `ng-template`, avec un **contexte** de données.

```typescript
// src/app/gabarits.ts
import { Component, signal } from '@angular/core';
import { NgTemplateOutlet } from '@angular/common';

@Component({
    selector: 'app-gabarits',
    imports: [NgTemplateOutlet],
    template: `
        <ng-template #chargement><p>Chargement…</p></ng-template>

        <ng-template #ligne let-nom let-position="index">
            <li>{{ position }}. {{ nom }}</li>
        </ng-template>

        @if (donnees(); as d) {
            <ul>
                @for (element of d; track element; let i = $index) {
                    <ng-container *ngTemplateOutlet="ligne; context: { $implicit: element, index: i + 1 }" />
                }
            </ul>
        } @else {
            <ng-container *ngTemplateOutlet="chargement" />
        }

        <ng-container>               <!-- regroupe sans ajouter d'élément au DOM -->
            @for (x of liste(); track x) { <span>{{ x }}</span> }
        </ng-container>
    `,
})
export class Gabarits {
    protected readonly donnees = signal<string[] | null>(['a', 'b']);
    protected readonly liste = signal(['a', 'b', 'c']);
}
```

Le contexte fournit des variables : `$implicit` se lie avec `let-nom` (sans valeur), les autres avec `let-position="index"`. C'est le mécanisme qui permet à un composant de **laisser le parent personnaliser le rendu** de ses lignes (listes, tableaux, menus).

### 5.7 Pièges fréquents

- Oublier `[ ]` : `src="urlImage()"` passe la **chaîne** littérale, pas la valeur.
- Écrire `[disabled]="false"` en pensant à l'attribut HTML : c'est la **propriété** booléenne qui est liée (correct).
- Utiliser `*ngIf` sans importer `NgIf` : erreur ; préférez `@if`.
- Oublier d'**appeler** un signal dans le gabarit (`valeur` au lieu de `valeur()`).
- Muter un tableau dans un signal (`liste().push(x)`) : la vue ne se met pas à jour ; créez un **nouveau** tableau.

### Synthèse du chapitre 5

Quatre liaisons : `{{ }}`, `[ ]`, `( )`, `[( )]`. Spécialisations : `[class.x]`, `[style.x.px]`, `[attr.x]`. Contrôle : `@if` / `@else`, `@for` avec **`track`** et `@empty`, `@switch`, `@let`. Les expressions sont **simples et pures** ; la logique va dans `computed()`. `ng-template`, `ng-container` et `NgTemplateOutlet` permettent de **réutiliser et paramétrer** des morceaux de gabarit.

---

## 6. Directives et tubes (*pipes*)

**Objectifs d'apprentissage.** Distinguer les types de directives ; utiliser les directives d'attribut intégrées ; **écrire** une directive d'attribut, une directive composée (`hostDirectives`) et une directive structurelle ; utiliser les **tubes** intégrés ; **créer** un tube ; comprendre tubes **purs** et **impurs** ; choisir entre tube, `computed()` et méthode.

### 6.1 Types de directives

Une **directive** est une classe qui ajoute du comportement à un élément du DOM. Il en existe trois sortes :

| Type | Rôle | Exemples |
| --- | --- | --- |
| **Composant** | Directive **avec gabarit** | `<app-carte />` |
| **Structurelle** | Modifie la **structure** du DOM (ajoute, retire des éléments) | `@if`, `@for` (anciennement `*ngIf`, `*ngFor`) |
| **D'attribut** | Modifie l'**apparence ou le comportement** d'un élément existant | `ngClass`, `ngStyle`, directives personnalisées |

### 6.2 Directives d'attribut intégrées *(à jour)*

```typescript
// src/app/attributs.ts
import { Component, signal } from '@angular/core';
import { NgClass, NgStyle } from '@angular/common';

@Component({
    selector: 'app-attributs',
    imports: [NgClass, NgStyle],
    template: `
        <!-- À préférer : liaisons natives de classes et de styles -->
        <div [class.actif]="actif()" [class]="{ rouge: erreur(), gras: important() }">Classes natives</div>
        <div [style.background-color]="couleur()" [style.width.px]="largeur()">Styles natifs</div>

        <!-- NgClass / NgStyle restent disponibles (import depuis @angular/common) -->
        <div [ngClass]="{ actif: actif() }" [ngStyle]="{ color: couleur() }">NgClass et NgStyle</div>
    `,
})
export class Attributs {
    protected readonly actif = signal(true);
    protected readonly erreur = signal(false);
    protected readonly important = signal(true);
    protected readonly couleur = signal('lightblue');
    protected readonly largeur = signal(200);
}
```

Depuis les versions récentes, `[class]` et `[style]` acceptent objets et tableaux : `NgClass` et `NgStyle` ne sont plus nécessaires. Les autres directives intégrées courantes sont `NgModel` (formulaires), `RouterLink` et `RouterLinkActive` (routeur), `NgOptimizedImage` (images) et `NgTemplateOutlet`.

### 6.3 Créer une directive d'attribut

```bash
ng generate directive surbrillance
```

```typescript
// src/app/surbrillance.ts
import { Directive, input, ElementRef, inject } from '@angular/core';

@Directive({
    selector: '[appSurbrillance]',                  // utilisable comme attribut
    exportAs: 'surbrillance',                       // permet #s="surbrillance" dans un gabarit
    host: {
        '(mouseenter)': 'appliquer(couleur())',
        '(mouseleave)': 'appliquer(\'\')',
    },
})
export class Surbrillance {
    couleur = input('yellow', { alias: 'appSurbrillance' });      // l'attribut sert aussi d'entrée
    private readonly element = inject(ElementRef<HTMLElement>);

    appliquer(c: string): void { this.element.nativeElement.style.backgroundColor = c; }
}
```

```typescript
// src/app/demo-surbrillance.ts
import { Component } from '@angular/core';
import { Surbrillance } from './surbrillance';

@Component({
    selector: 'app-demo-surbrillance',
    imports: [Surbrillance],
    template: `<p appSurbrillance="lightblue">Survolez-moi</p>`,
})
export class DemoSurbrillance {}
```

**Points clés.** Une directive n'a **pas de gabarit**. Elle accède à son élément via `inject(ElementRef)` ; on modifie le DOM avec prudence (préférez les liaisons dans `host`, ou `Renderer2`, plus sûr, notamment avec le SSR). Une directive peut aussi avoir `providers`, des sorties et des liaisons sur l'hôte.

#### Directives composées : `hostDirectives`

On peut **appliquer des directives à l'hôte** d'un composant ou d'une directive, et **choisir** quelles entrées et sorties exposer. C'est la composition de comportements, sans héritage.

```typescript
// src/app/bouton-info.ts
import { Component } from '@angular/core';
import { Surbrillance } from './surbrillance';

@Component({
    selector: 'app-bouton-info',
    hostDirectives: [{ directive: Surbrillance, inputs: ['appSurbrillance: couleur'] }],
    template: `<ng-content />`,
})
export class BoutonInfo {}
```

Utilisation : `<app-bouton-info couleur="orange">Info</app-bouton-info>`.

### 6.4 Directives structurelles personnalisées *(héritage avancé)*

Une directive structurelle reçoit un **`TemplateRef`** (le gabarit) et un **`ViewContainerRef`** (l'endroit où l'insérer) et crée ou détruit la vue. Le préfixe `*` est un sucre syntaxique pour envelopper l'élément dans un `ng-template`.

```typescript
// src/app/si-role.ts
import { Directive, TemplateRef, ViewContainerRef, effect, inject, input } from '@angular/core';
import { AuthService } from './auth/auth';      // défini au chapitre 27

@Directive({ selector: '[appSiRole]' })
export class SiRole {
    appSiRole = input.required<string>();
    private readonly modele = inject(TemplateRef<unknown>);
    private readonly conteneur = inject(ViewContainerRef);
    private readonly auth = inject(AuthService);

    constructor() {
        effect(() => {
            this.conteneur.clear();
            if (this.auth.aLeRole(this.appSiRole())) this.conteneur.createEmbeddedView(this.modele);
        });
    }
}
```

Usage : `<button *appSiRole="'admin'">Supprimer</button>`. Le **flux de contrôle intégré** couvre la grande majorité des besoins : n'écrivez une directive structurelle que pour un comportement vraiment réutilisable. (Rappel : masquer un bouton n'est **pas** de la sécurité, chapitre 27.)

### 6.5 Les tubes (*pipes*) intégrés

Un **tube** transforme une valeur **à l'affichage** : `{{ valeur | tube:argument1:argument2 }}`. Il ne modifie pas la donnée d'origine. On l'importe dans `imports` du composant (`DatePipe`, `CurrencyPipe`…) ou on importe `CommonModule` *(héritage)*.

| Tube | Exemple | Résultat |
| --- | --- | --- |
| `date` | `{{ d \| date: 'dd/MM/yyyy' }}` | `11/10/2026` |
| `currency` | `{{ 1234.5 \| currency: 'EUR' }}` | `€1,234.50` (selon la locale) |
| `number` | `{{ 3.14159 \| number: '1.2-2' }}` | `3.14` |
| `percent` | `{{ 0.256 \| percent }}` | `26%` |
| `uppercase`, `lowercase`, `titlecase` | `{{ 'angular' \| titlecase }}` | `Angular` |
| `slice` | `{{ liste \| slice: 0:3 }}` | 3 premiers éléments |
| `json` | `{{ objet \| json }}` | Débogage |
| `keyvalue` | `@for (e of obj \| keyvalue; track e.key)` | Itérer un objet |
| `async` | `{{ flux$ \| async }}` | S'abonne à un **Observable** / Promise |
| `i18nPlural`, `i18nSelect` |  | Pluriels et sélection (i18n) |

**Format du tube `number`** : `'minEntiers.minDécimales-maxDécimales'` (ex. `'1.2-2'` : au moins 1 chiffre entier, exactement 2 décimales). **Tube `date`** : formats prédéfinis (`'short'`, `'longDate'`, `'fullDate'`, `'shortTime'`) ou personnalisés (`'dd/MM/yyyy HH:mm'`) ; paramètres de fuseau et de locale facultatifs. **Tube `currency`** : code ISO, mode d'affichage (`'symbol'`, `'code'`), format des décimales.

```typescript
// src/app/facture.ts
import { Component } from '@angular/core';
import { DatePipe, CurrencyPipe } from '@angular/common';

@Component({
    selector: 'app-facture',
    imports: [DatePipe, CurrencyPipe],
    template: `<p>{{ date | date: 'longDate' }} — {{ montant | currency: 'EUR' }}</p>`,
})
export class Facture { date = new Date(); montant = 1234.5; }
```

**Chaînage et arguments** : `{{ valeur | uppercase | slice: 0:5 }}`. Dans une expression avec ternaire ou opérateur, mettez des **parenthèses** : `{{ (a ?? b) | date }}`.

**Le tube `async`** s'abonne à un Observable (ou une Promise), renvoie la dernière valeur, **se désabonne automatiquement** à la destruction du composant et déclenche la détection de changements. Les **signaux** et `toSignal()` le remplacent avantageusement dans la plupart des cas.

### 6.6 Créer un tube

```typescript
// src/app/tronquer.ts
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({ name: 'tronquer' })            // pur par défaut
export class Tronquer implements PipeTransform {
    transform(texte: string, longueur = 20, suffixe = '…'): string {
        return texte.length > longueur ? texte.slice(0, longueur) + suffixe : texte;
    }
}
```

```typescript
// src/app/resume.ts
import { Component } from '@angular/core';
import { Tronquer } from './tronquer';

@Component({
    selector: 'app-resume',
    imports: [Tronquer],
    template: `<p>{{ description | tronquer: 50 }}</p>`,
})
export class Resume {
    protected readonly description = 'Angular est un framework open source développé par Google pour créer des applications web.';
}
```

La méthode `transform` reçoit la **valeur d'entrée** en premier paramètre, puis les **arguments** dans l'ordre. Un tube peut injecter des services (`inject(...)`), par exemple pour traduire ou formater selon la locale.

### 6.7 Tubes purs et impurs

|  | **Pur** (défaut) | **Impur** (`pure: false`) |
| --- | --- | --- |
| Exécuté | Seulement si l'**entrée change** (par référence ou valeur primitive) | À **chaque** détection de changements |
| Performance | Excellente | Coûteux |
| Usage | Presque toujours | Rare (ex. `async`) |

Piège classique : un tube **pur** appliqué à un **tableau muté** (`liste.push(x)`) ne se réexécute pas, car la référence est identique. Remède : créer un **nouveau** tableau, ou utiliser un signal.

### 6.8 Tube, `computed()` ou méthode ?

| Besoin | Choix |
| --- | --- |
| Mise en forme **réutilisable** à l'affichage (dates, monnaie, troncature) | **Tube** |
| Valeur **dérivée de l'état** du composant | **`computed()`** (mémoïsé, testable) |
| Gestionnaire d'événement | **Méthode** |
| Calcul lourd appelé dans le gabarit | **Jamais** une méthode : `computed()` |

### Synthèse du chapitre 6

Trois types de directives : **composants**, **structurelles**, **d'attribut**. Les liaisons natives de classes/styles remplacent `NgClass`/`NgStyle`. On écrit une directive avec `@Directive`, `host`, `input()` et `inject(ElementRef)` ; `hostDirectives` compose les comportements. Les **tubes** transforment l'affichage ; ils sont **purs** par défaut. Pour dériver de l'état, préférez `computed()`.

---

## 7. Services et injection de dépendances

**Objectifs d'apprentissage.** Définir un service et l'injection de dépendances (DI) ; créer et injecter un service avec `inject()` ; maîtriser les **portées** de fournisseurs ; utiliser **jetons d'injection** et formes de fournisseurs ; comprendre la **hiérarchie d'injecteurs** et les modificateurs ; exécuter du code à l'initialisation ; diagnostiquer les erreurs d'injection.

### 7.1 Qu'est-ce qu'un service ? Qu'est-ce que la DI ?

Un **service** est une classe qui regroupe de la **logique réutilisable** : accès aux données, état partagé, journalisation, authentification. Les composants s'occupent de l'**affichage** ; les services portent le **reste**.

L'**injection de dépendances** (*Dependency Injection*, DI) est le mécanisme par lequel une classe **déclare** ce dont elle a besoin et **Angular le lui fournit**, au lieu qu'elle l'instancie elle-même (`new Service()`). Vocabulaire :

- **Dépendance** : un objet dont une classe a besoin.
- **Jeton** (*token*) : la **clé** qui identifie la dépendance (le plus souvent la classe elle-même, ou un `InjectionToken`).
- **Fournisseur** (*provider*) : la **recette** qui dit *comment* produire la valeur associée à un jeton.
- **Injecteur** (*injector*) : l'objet qui **résout** un jeton en valeur, en créant et en mémorisant les instances.

| Avantage | Détail |
| --- | --- |
| Réutilisation | Un même service pour plusieurs composants |
| Séparation | Composants = affichage ; services = logique |
| Testabilité | On remplace un service par une **doublure** en test |
| Singletons | Une seule instance partagée (par injecteur) |
| Configuration centralisée | On change l'implémentation sans toucher aux consommateurs |

### 7.2 Créer et injecter un service

```bash
ng generate service tache
```

```typescript
// src/app/tache.ts
import { Injectable, signal, computed } from '@angular/core';

export interface Tache { id: number; titre: string; faite: boolean }

@Injectable({ providedIn: 'root' })            // singleton à l'échelle de l'application, « tree-shakable »
export class TacheService {
    private readonly _taches = signal<Tache[]>([]);
    readonly taches = this._taches.asReadonly();                       // exposé en lecture seule
    readonly restantes = computed(() => this._taches().filter((t) => !t.faite).length);

    ajouter(titre: string): void {
        this._taches.update((liste) => [...liste, { id: Date.now(), titre, faite: false }]);
    }
    basculer(id: number): void {
        this._taches.update((liste) => liste.map((t) => (t.id === id ? { ...t, faite: !t.faite } : t)));
    }
}
```

`@Injectable({ providedIn: 'root' })` fait **deux choses** : il déclare la classe injectable et la **fournit à l'injecteur racine**. Un service jamais injecté n'est **pas inclus** dans le bundle (*tree-shaking*).

> **Note de version.** La v22 introduit un décorateur raccourci `@Service()` pour les services à portée racine (équivalent de `@Injectable({ providedIn: 'root' })`). Vérifiez sa disponibilité et sa syntaxe exacte sur angular.dev avant de l'adopter ; la forme `@Injectable` reste valide partout.

#### Injection avec `inject()` *(à jour)*

```typescript
// src/app/taches.ts
import { Component, inject } from '@angular/core';
import { TacheService } from './tache';

@Component({
    selector: 'app-taches',
    template: `
        <p>{{ service.restantes() }} tâche(s) restante(s)</p>
        @for (t of service.taches(); track t.id) {
            <label><input type="checkbox" [checked]="t.faite" (change)="service.basculer(t.id)" /> {{ t.titre }}</label>
        }
    `,
})
export class Taches {
    protected readonly service = inject(TacheService);          // recommandé
    // constructor(private service: TacheService) {}            // forme historique, toujours valide
}
```

**`inject()` ou injection par constructeur ?** Les deux fonctionnent. `inject()` est **recommandé** : il fonctionne dans les champs initialisés, les fonctions (gardes, intercepteurs, résolveurs), se prête mieux à l'**héritage** (pas de `super(...)` à reproduire) et à la **composition** (fonctions réutilisables). Migration automatique : `ng generate @angular/core:inject`.

> **Contexte d'injection.** `inject()` ne fonctionne que dans un **contexte d'injection** : constructeur, initialisation de champ, fonction passée à `provide…`, garde, intercepteur, ou code exécuté par `runInInjectionContext(injecteur, () => …)`. Appeler `inject()` dans une méthode ordinaire ou un `setTimeout` lève une erreur (NG0203). Capturez la dépendance **à l'initialisation** et réutilisez-la.

### 7.3 Portées des fournisseurs

Où l'on **fournit** un service détermine **combien d'instances** existent et **jusqu'à quand**.

| Où fournir | Portée / durée de vie |
| --- | --- |
| `@Injectable({ providedIn: 'root' })` | **Toute l'application**, instance unique (par défaut) |
| `providers` de `app.config.ts` | Toute l'application (utile pour la configuration) |
| `providers` d'une **route** | Les routes enfants (injecteur d'environnement créé avec la route) |
| `providers` d'un **composant** | **Une instance par composant** (et ses enfants) |
| `viewProviders` | Vue du composant seulement (pas le contenu projeté) |

```typescript
// src/app/formulaire.ts
import { Component, Injectable, inject, signal } from '@angular/core';

@Injectable()                              // pas de providedIn : fourni explicitement
export class BrouillonService {
    readonly texte = signal('');
}

@Component({
    selector: 'app-formulaire',
    providers: [BrouillonService],           // nouvelle instance pour chaque <app-formulaire>
    template: `
        <textarea (input)="brouillon.texte.set($any($event.target).value)"></textarea>
        <p>{{ brouillon.texte().length }} caractère(s)</p>
    `,
})
export class Formulaire {
    protected readonly brouillon = inject(BrouillonService);
}
```

**Quand fournir au niveau d'un composant ?** Pour un **état propre à chaque instance** (brouillon d'un formulaire, état d'un assistant), qui doit être **détruit avec le composant**. Un service fourni dans un composant est créé avec lui et supprimé avec lui.

### 7.4 Jetons d'injection et configuration

Pour injecter autre chose qu'une classe (une URL, un objet de configuration, une fonction, une interface — qui n'existe pas à l'exécution), on crée un **`InjectionToken`**.

```typescript
// src/app/config-app.ts
import { InjectionToken } from '@angular/core';

export interface ConfigApp { urlApi: string; delaiMs: number }
export const CONFIG_APP = new InjectionToken<ConfigApp>('CONFIG_APP', {
    providedIn: 'root',
    factory: () => ({ urlApi: '/api', delaiMs: 5000 }),         // valeur par défaut
});
```

Remplacer la valeur par défaut dans la configuration de l'application :

```typescript
// src/app/app.config.ts
import { ApplicationConfig } from '@angular/core';
import { CONFIG_APP } from './config-app';

export const appConfig: ApplicationConfig = {
    providers: [
        { provide: CONFIG_APP, useValue: { urlApi: 'https://api.exemple.com', delaiMs: 8000 } },
    ],
};
```

Lire la valeur dans un service :

```typescript
// src/app/api.ts
import { Injectable, inject } from '@angular/core';
import { CONFIG_APP } from './config-app';

@Injectable({ providedIn: 'root' })
export class Api {
    private readonly config = inject(CONFIG_APP);
    afficherUrl(): void { console.log(this.config.urlApi); }
}
```

#### Formes de fournisseurs

| Forme | Usage |
| --- | --- |
| `{ provide: A, useClass: B }` | Remplacer une classe par une autre (ex. `ServiceReel` → `ServiceFactice`) |
| `{ provide: T, useValue: valeur }` | Fournir une constante |
| `{ provide: T, useFactory: () => … }` | Construire avec une fonction (peut utiliser `inject()`) |
| `{ provide: A, useExisting: B }` | **Alias** : `A` renvoie l'instance existante de `B` |
| `multi: true` | **Plusieurs** valeurs pour un même jeton (un tableau) |

Le principe d'**inversion des dépendances** consiste à dépendre d'une **abstraction** (classe abstraite ou jeton) et à choisir l'implémentation dans la configuration : on change de comportement (réel, factice, démonstration) **sans modifier** les consommateurs.

```typescript
// src/app/journal.ts
import { Injectable } from '@angular/core';

export abstract class Journal { abstract ecrire(message: string): void; }

@Injectable()
export class JournalConsole extends Journal {
    ecrire(message: string): void { console.log(message); }
}
// Dans app.config.ts : { provide: Journal, useClass: JournalConsole }
```

### 7.5 Modificateurs d'injection

Les **options** de `inject()` adaptent la recherche dans la hiérarchie.

| Option | Effet |
| --- | --- |
| `optional: true` | Renvoie `null` si aucun fournisseur (au lieu d'une erreur) |
| `self: true` | Cherche **uniquement** dans l'injecteur local |
| `skipSelf: true` | Ignore l'injecteur local, commence au **parent** |
| `host: true` | S'arrête à l'élément hôte (cas des composants et projections) |

```typescript
// src/app/enfant.ts
import { Component, Injectable, inject } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class Journal {
    ecrire(message: string): void { console.log(message); }
}

@Injectable()
export class Theme { nom = 'clair'; }

@Component({
    selector: 'app-enfant',
    providers: [Theme],
    template: `<p>Voir la console</p>`,
})
export class Enfant {
    private readonly journal = inject(Journal, { optional: true });                // null si absent
    private readonly local = inject(Theme, { self: true });                         // uniquement l'injecteur local
    private readonly parent = inject(Theme, { skipSelf: true, optional: true });    // injecteur parent (null ici)

    constructor() {
        this.journal?.ecrire(`Thème local : ${this.local.nom}`);
        console.log(this.parent);                                                   // null
    }
}
```

### 7.6 La hiérarchie d'injecteurs

```text
Injecteur de plateforme
   └── Injecteur d'environnement (racine : app.config.ts, providedIn: 'root')
          └── Injecteurs de routes (providers de route, chargement paresseux)
                 └── Injecteurs d'éléments (composants, directives)
```

**Algorithme de résolution.** Pour un jeton demandé par un composant, Angular cherche **d'abord** dans l'injecteur d'éléments du composant, **remonte** aux éléments parents, puis passe à l'injecteur d'environnement (routes, racine) et enfin à la plateforme. Dès qu'un fournisseur est trouvé, l'instance est créée (si elle n'existe pas) et mémorisée **dans cet injecteur**. Sinon : erreur `NullInjectorError` (ou `null` avec `optional`).

Conséquences : un fournisseur **plus proche** masque un fournisseur plus lointain ; deux composants frères fournissant le même service obtiennent **deux instances** distinctes ; un service fourni dans une **route chargée paresseusement** n'existe que pour cette partie de l'application.

### 7.7 Fonctions d'initialisation

`provideAppInitializer()` exécute du code **avant le démarrage** de l'application (chargement de configuration, restauration de session). Il peut renvoyer une promesse : Angular **attend** sa résolution.

```typescript
// src/app/app.config.ts
import { ApplicationConfig, Injectable, inject, provideAppInitializer } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class ConfigService {
    async charger(): Promise<void> {
        console.log('Configuration chargée');
    }
}

export const appConfig: ApplicationConfig = {
    providers: [
        provideAppInitializer(() => inject(ConfigService).charger()),     // exécutée avant le démarrage
    ],
};
```

Une initialisation **lente** retarde l'affichage : gardez-la **courte** ou différez le travail non indispensable.

### 7.8 Erreurs courantes et diagnostic

| Erreur | Cause et remède |
| --- | --- |
| `NullInjectorError: No provider for X` | Aucun fournisseur : ajouter `providedIn: 'root'` ou un `provide…()` (ex. `provideHttpClient()`) |
| NG0203 (`inject()` hors contexte) | Appel hors constructeur / champ : capturer la dépendance à l'initialisation |
| Dépendance **circulaire** (NG0200) | A injecte B qui injecte A : extraire une logique commune dans un troisième service |
| Deux instances « du même » service | Fourni à plusieurs niveaux : vérifier `providers` des composants et des routes |

### 7.9 Bonnes pratiques

- `providedIn: 'root'` **par défaut** ; fournir au niveau d'un composant seulement pour un **état propre à chaque instance**.
- Exposer l'état en **signaux en lecture seule** (`asReadonly()`) ; les modifications passent par des **méthodes** du service.
- Dépendre d'**abstractions** (jetons, classes abstraites) pour faciliter les tests.
- Un service = **une responsabilité** ; éviter les « services fourre-tout ».
- Éviter les dépendances circulaires ; ne pas stocker de données utilisateur dans des singletons **côté serveur** (SSR, chapitre 22).

### Synthèse du chapitre 7

Un **service** porte la logique et l'état ; la **DI** le fournit via un **injecteur**, selon un **jeton** et un **fournisseur**. `inject()` est la forme recommandée ; `providedIn: 'root'` donne un singleton *tree-shakable*. La **portée** dépend de l'endroit où l'on fournit (racine, route, composant). Les `InjectionToken` et les formes `useClass` / `useValue` / `useFactory` / `useExisting` rendent le code **configurable et testable**.

---

## 8. Signaux et réactivité

**Objectifs d'apprentissage.** Comprendre le modèle des signaux ; maîtriser `signal`, `computed`, `effect`, `linkedSignal`, `untracked` ; charger des données avec `resource`, `httpResource`, `rxResource` ; passer des signaux à RxJS et inversement ; choisir entre signaux et RxJS ; connaître les erreurs classiques.

### 8.1 Qu'est-ce qu'un signal ?

Un **signal** est un **conteneur de valeur réactif** : il enveloppe une valeur et **notifie** ceux qui la lisent quand elle change. Angular sait donc **précisément** quels gabarits et quels calculs dépendent de quel signal, et ne met à jour **que ceux-là**. Cette précision est le socle du mode **zoneless** (chapitre 18).

**Modèle mental.** Les signaux forment un **graphe de dépendances** : les `signal()` sont les **sources**, les `computed()` des **nœuds dérivés**, les `effect()` et les gabarits des **consommateurs**. La lecture d'un signal à l'intérieur d'un consommateur crée **automatiquement** une dépendance (suivi dynamique) ; il n'y a pas de liste de dépendances à écrire à la main.

```typescript
// src/app/signaux.ts
import { Component, signal, computed, effect } from '@angular/core';

@Component({
    selector: 'app-signaux',
    template: `<p>Compteur : {{ compteur() }} (double : {{ double() }})</p>`,
})
export class Signaux {
    protected readonly compteur = signal(0);                          // WritableSignal<number>
    protected readonly double = computed(() => this.compteur() * 2);  // valeur dérivée : lecture seule, MÉMOÏSÉE, paresseuse

    constructor() {
        effect(() => console.log(`Compteur : ${this.compteur()}`));   // effet de bord, relancé quand une dépendance change
        this.compteur.set(5);                                          // remplacement
        this.compteur.update((v) => v + 1);                            // mise à jour à partir de l'ancienne valeur
        console.log(this.compteur(), this.double());                   // 6 12 : lecture (on « appelle » le signal)
    }
}
```

| API | Rôle |
| --- | --- |
| `signal(valeur)` | État **inscriptible** |
| `computed(() => …)` | Valeur **dérivée**, en lecture seule, recalculée si ses dépendances changent |
| `effect(() => …)` | **Effet de bord** (journalisation, stockage, DOM manuel) |
| `linkedSignal(…)` | Signal **inscriptible** qui se **réinitialise** quand une source change |
| `untracked(() => …)` | Lire un signal **sans** créer de dépendance |
| `resource()` / `httpResource()` | Données **asynchrones** exposées en signaux |
| `toSignal()` / `toObservable()` | Passerelles avec **RxJS** |

> **À retenir.** Les API de base (`signal`, `computed`, `effect`, `linkedSignal`, `input`, `model`, `viewChild`) sont **stables** depuis la v20 ; `resource`, `rxResource` et `httpResource` le sont depuis la **v22**.

### 8.2 `signal()` : l'état inscriptible

- **Lecture** : on **appelle** le signal : `compteur()`.
- **Écriture** : `set(valeur)` remplace ; `update(fn)` calcule la nouvelle valeur à partir de l'ancienne.
- **Lecture seule** : `asReadonly()` expose un signal non modifiable (à utiliser dans les services).
- **Égalité** : un signal ne notifie que si la nouvelle valeur **diffère** (comparaison `Object.is`, personnalisable avec l'option `equal`).

**Les objets et tableaux se mettent à jour de façon immuable**, car le changement est détecté **par référence** :

```typescript
import { signal } from '@angular/core';

const utilisateur = signal({ nom: 'Alice', age: 30 });
utilisateur.update((u) => ({ ...u, age: u.age + 1 }));     // correct : nouvel objet
console.log(utilisateur());                                  // { nom: 'Alice', age: 31 }

const liste = signal<string[]>([]);
liste.update((l) => [...l, 'nouveau']);                    // correct : nouveau tableau
// liste().push('x');                                       // incorrect : aucune notification
console.log(liste());                                        // ['nouveau']
```

### 8.3 `computed()` : dériver une valeur

```typescript
// src/app/panier.ts
import { Component, computed, signal } from '@angular/core';

@Component({
    selector: 'app-panier',
    template: `<p>Total : {{ total() }}</p>`,
})
export class Panier {
    protected readonly prix = signal(100);
    protected readonly quantite = signal(2);
    protected readonly total = computed(() => this.prix() * this.quantite());       // se met à jour automatiquement
}
```

- **Paresseux** : calculé seulement quand on le **lit** pour la première fois.
- **Mémoïsé** : recalculé **seulement** si une dépendance a changé ; sinon, la valeur en cache est renvoyée.
- **Dépendances dynamiques** : seuls les signaux **réellement lus** lors du dernier calcul sont suivis (`a() ? b() : c()`).
- **Pur** : pas d'effets de bord, et **interdiction d'écrire** dans un signal à l'intérieur.
- **Sans cycle** : un `computed` ne peut pas dépendre de lui-même.

### 8.4 `effect()` : effets de bord

Un **effet** s'exécute **au moins une fois**, puis à chaque changement d'un signal qu'il a lu. Il sert à **synchroniser l'état avec l'extérieur** : stockage, journaux, bibliothèques non Angular, DOM manuel.

```typescript
// src/app/preferences.ts
import { Component, effect, signal } from '@angular/core';

@Component({
    selector: 'app-preferences',
    template: `<button (click)="basculer()">Thème : {{ theme() }}</button>`,
})
export class Preferences {
    protected readonly theme = signal<'clair' | 'sombre'>('clair');

    constructor() {
        // Les effets s'exécutent aussi côté serveur : voir le chapitre 22 pour un code compatible SSR
        effect(() => {
            document.documentElement.dataset['theme'] = this.theme();       // synchroniser avec le DOM
            localStorage.setItem('theme', this.theme());
        });
    }

    protected basculer(): void {
        this.theme.update((t) => (t === 'clair' ? 'sombre' : 'clair'));
    }
}
```

**Caractéristiques**

- Créé dans un **contexte d'injection** (constructeur, champ) ; **détruit automatiquement** avec le composant ou le service qui le contient.
- **Exécution asynchrone** : les effets sont planifiés et regroupés lors de la mise à jour, pas appelés immédiatement à chaque `set`.
- **Nettoyage** : la fonction reçoit `onCleanup`, appelée avant la réexécution et à la destruction.
- `untracked(() => …)` lit un signal **sans** le suivre (évite de relancer l'effet).

```typescript
import { effect, signal, untracked } from '@angular/core';

const intervalle = signal(1000);
const unite = signal('ms');

effect((onCleanup) => {
    const id = setInterval(() => console.log('tic', untracked(unite)), intervalle());   // `unite` non suivi
    onCleanup(() => clearInterval(id));                                                  // nettoyage avant relance
});
```

> **Attention.** **N'utilisez pas `effect` pour propager un état vers un autre signal** : préférez `computed` (valeur dérivée) ou `linkedSignal` (état dérivé modifiable). Les effets sont réservés aux **synchronisations avec l'extérieur**. Pour des effets liés au **rendu**, utilisez `afterRenderEffect()` / `afterNextRender()`.

### 8.5 `linkedSignal()` : état dérivé modifiable

Un **`linkedSignal`** est un signal **inscriptible** dont la valeur est **recalculée** (réinitialisée) quand sa **source** change. Cas typique : une sélection qui doit revenir à une valeur par défaut quand la liste d'options change.

```typescript
import { linkedSignal, signal } from '@angular/core';

const options = signal(['S', 'M', 'L']);
const selection = linkedSignal(() => options()[0]);        // se réinitialise quand `options` change
selection.set('L');                                          // mais reste modifiable
console.log(selection());                                    // 'L'

options.set(['XS', 'S']);
console.log(selection());                                    // 'XS' : réinitialisé
```

Version avancée, avec **mémoire de l'ancienne valeur** :

```typescript
import { linkedSignal, signal } from '@angular/core';

const options = signal(['S', 'M', 'L']);
const selection = linkedSignal<string[], string>({
    source: options,
    computation: (nouvelles, precedent) => (precedent && nouvelles.includes(precedent.value) ? precedent.value : nouvelles[0]),
});

selection.set('M');
options.set(['M', 'L', 'XL']);
console.log(selection());                                    // 'M' : conservé, car toujours disponible
options.set(['XS', 'S']);
console.log(selection());                                    // 'XS' : l'ancienne sélection a disparu
```

### 8.6 `resource` : données asynchrones *(stable en v22)*

Une **resource** relie un **signal de paramètres** à un **chargeur asynchrone** et expose son état sous forme de signaux : `value()`, `isLoading()`, `error()`, `status()`, ainsi que `hasValue()`, `reload()`, `set()` / `update()` (valeur locale). Quand les paramètres changent, le chargement est **relancé** et la requête précédente est **annulée** (`abortSignal`).

```typescript
// src/app/utilisateur-vue.ts
import { Component, resource, signal } from '@angular/core';

@Component({
    selector: 'app-utilisateur',
    template: `
        <input type="number" [value]="id()" (input)="id.set(+$any($event.target).value)" />
        @if (utilisateur.isLoading()) { <p>Chargement…</p> }
        @else if (utilisateur.error()) { <p>Erreur : {{ utilisateur.error() }}</p> }
        @else if (utilisateur.value(); as u) { <p>{{ u.nom }}</p> }
        <button (click)="utilisateur.reload()">Recharger</button>
    `,
})
export class UtilisateurVue {
    id = signal(1);

    utilisateur = resource({
        params: () => ({ id: this.id() }),                  // rechargement automatique quand `id` change
        loader: async ({ params, abortSignal }) => {
            const r = await fetch(`/api/users/${params.id}`, { signal: abortSignal });   // requête précédente annulée
            if (!r.ok) throw new Error(`HTTP ${r.status}`);
            return (await r.json()) as { nom: string };
        },
    });
}
```

> **Note.** Dans les versions 19–20, l'option s'appelait `request` ; elle est devenue **`params`**.

**États** (`status()`) : *idle* (pas de paramètres), *loading* (premier chargement), *reloading* (rechargement avec valeur précédente conservée), *resolved*, *error*, *local* (valeur modifiée localement).

#### `httpResource` : la version « HttpClient »

```typescript
// src/app/liste-utilisateurs.ts
import { Component, signal } from '@angular/core';
import { httpResource } from '@angular/common/http';

interface Utilisateur { id: number; nom: string; }

@Component({
    selector: 'app-liste-utilisateurs',
    template: `
        <button (click)="page.update((p) => p + 1)">Page suivante ({{ page() }})</button>
        @if (utilisateurs.isLoading()) {
            <p>Chargement…</p>
        } @else if (utilisateurs.hasValue()) {
            <ul>
                @for (u of utilisateurs.value(); track u.id) { <li>{{ u.nom }}</li> }
            </ul>
        }
    `,
})
export class ListeUtilisateurs {
    protected readonly page = signal(1);
    // passe par HttpClient (intercepteurs inclus) : nécessite provideHttpClient() dans app.config.ts
    protected readonly utilisateurs = httpResource<Utilisateur[]>(() => `/api/users?page=${this.page()}`);
}
```

#### `rxResource` : à partir d'un Observable

```typescript
// src/app/produits-categorie.ts
import { Component, Injectable, inject, signal } from '@angular/core';
import { rxResource } from '@angular/core/rxjs-interop';
import { Observable, of, delay } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class CatalogueService {
    lister(categorie: string): Observable<string[]> {
        return of([`${categorie} 1`, `${categorie} 2`]).pipe(delay(300));
    }
}

@Component({
    selector: 'app-produits-categorie',
    template: `
        <button (click)="categorie.set('jeux')">Jeux</button>
        @if (produits.isLoading()) { <p>Chargement…</p> }
        @for (p of produits.value() ?? []; track p) { <p>{{ p }}</p> }
    `,
})
export class ProduitsCategorie {
    private readonly service = inject(CatalogueService);
    protected readonly categorie = signal('livres');
    protected readonly produits = rxResource({
        params: () => this.categorie(),
        stream: ({ params }) => this.service.lister(params),
    });
}
```

> **Astuce.** `resource` est conçu pour les **lectures** (chargement de données). Les **écritures** (POST, PUT, DELETE) restent des appels `HttpClient` explicites, déclenchés par un événement.

### 8.7 Interopérabilité RxJS ⇄ signaux

```typescript
// src/app/interop.ts
import { Component, inject, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { toSignal, toObservable } from '@angular/core/rxjs-interop';
import { debounceTime, switchMap } from 'rxjs';

interface Utilisateur { id: number; nom: string; }

@Component({
    selector: 'app-interop',
    template: `
        <p>{{ utilisateurs().length }} utilisateur(s)</p>
        <input (input)="termeRecherche.set($any($event.target).value)" />
        <ul>
            @for (r of resultats(); track r) { <li>{{ r }}</li> }
        </ul>
    `,
})
export class Interop {
    private readonly http = inject(HttpClient);
    protected readonly termeRecherche = signal('');

    // Observable → signal (abonnement et désabonnement automatiques)
    protected readonly utilisateurs = toSignal(this.http.get<Utilisateur[]>('/api/users'), { initialValue: [] });

    // Signal → Observable (pour appliquer des opérateurs RxJS), puis retour en signal pour le gabarit
    private readonly resultats$ = toObservable(this.termeRecherche).pipe(
        debounceTime(300),
        switchMap((t) => this.http.get<string[]>(`/api/recherche?q=${t}`)),
    );
    protected readonly resultats = toSignal(this.resultats$, { initialValue: [] as string[] });
}
```

- `toSignal(obs$, { initialValue })` s'abonne, expose la **dernière valeur** et **se désabonne** à la destruction. Sans `initialValue`, le signal vaut `undefined` avant la première émission. Si l'Observable lève une erreur, la **lecture** du signal relance cette erreur.
- `toObservable(signal)` émet quand le signal change (de façon **asynchrone**, regroupée comme un effet) : seule la dernière valeur d'une rafale est émise.
- Les deux doivent être appelés dans un **contexte d'injection** (ou recevoir un `injector`).

### 8.8 Signaux ou RxJS ?

|  | **Signaux** | **RxJS** |
| --- | --- | --- |
| Nature | **État** (valeur courante, toujours disponible) | **Flux d'événements** dans le temps |
| Usage idéal | État de composant / de service, valeurs dérivées, gabarits | Requêtes annulables, anti-rebond, WebSockets, combinaisons complexes |
| Syntaxe | Simple, synchrone | Opérateurs puissants, plus de concepts |
| Dans les gabarits | `valeur()` | Tube `async` ou `toSignal` |

> **Règle.** **Signaux pour l'état, RxJS pour les flux** ; `toSignal` / `toObservable` pour passer de l'un à l'autre.

### 8.9 Bonnes pratiques et pièges

- Pas de `ChangeDetectorRef.detectChanges()` : modifier un signal suffit.
- Exposez l'état sous forme de **signaux en lecture seule** ; les opérations qui le modifient sont des **méthodes**.
- Gardez les `effect` **rares** ; préférez `computed` et `linkedSignal`.
- **Mutation silencieuse** : `liste().push(x)` ne notifie pas. Créez toujours un nouvel objet ou tableau.
- **Oubli de l'appel** : `valeur` au lieu de `valeur()` dans le gabarit ou une expression (le compilateur le signale souvent).
- **Écriture dans un `computed`** : interdite ; calculer, ne pas modifier.
- Lire un signal dans un `effect` **asynchrone** (après un `await`) : la lecture n'est **plus suivie** ; lisez les signaux **avant** l'`await`.
- Les effets s'exécutent aussi **côté serveur** : protégez l'accès à `window` / `localStorage` (chapitre 22).

### Synthèse du chapitre 8

Les **signaux** sont la base de l'état réactif : `signal` (sources), `computed` (dérivés mémoïsés), `effect` (effets de bord), `linkedSignal` (état dérivé modifiable), `resource` (données asynchrones). Mises à jour **immuables**, effets **rares**. **Signaux pour l'état**, **RxJS pour les flux**, reliés par `toSignal` / `toObservable`.

---

## 9. Routage et navigation

**Objectifs d'apprentissage.** Définir des routes et les activer avec `provideRouter` ; naviguer par liens et par code ; lire paramètres, paramètres de requête et données de route ; organiser des **routes imbriquées** ; charger **paresseusement** ; protéger les routes avec des **gardes** ; précharger les données avec des **résolveurs** ; configurer le routeur (défilement, transitions, titres, événements) ; déployer correctement une application routée.

### 9.1 Le rôle du routeur

Dans une SPA, le **routeur** fait correspondre l'**URL** du navigateur à un **composant** à afficher, sans rechargement de page. Il gère aussi l'historique (boutons Précédent / Suivant), les liens partageables et les marque-pages.

**Vocabulaire**

- **Route** : association entre un **chemin** (`path`) et un composant (ou un groupe de routes).
- **Table de routes** (`Routes`) : tableau de routes, évalué **dans l'ordre**.
- **`<router-outlet />`** : emplacement du gabarit où s'affiche le composant de la route active.
- **Paramètre de chemin** : segment variable (`/produits/:id`).
- **Paramètres de requête** (*query params*) : `?page=2&tri=prix`.
- **Fragment** : `#section`.
- **`UrlTree`** : représentation objet d'une URL (utilisée par les gardes pour rediriger).
- **Garde**, **résolveur**, **stratégie de préchargement** : voir plus bas.

### 9.2 Configurer le routeur

```typescript
// src/app/app.routes.ts
import { Routes } from '@angular/router';
import { Accueil } from './accueil';
import { Introuvable } from './introuvable';

export const routes: Routes = [
    { path: '', component: Accueil, title: 'Accueil' },                       // URL « / »
    { path: 'produits', loadComponent: () => import('./produits/liste').then((m) => m.ListeProduits), title: 'Produits' },
    { path: 'produits/:id', loadComponent: () => import('./produits/detail').then((m) => m.DetailProduit) },
    { path: 'ancienne-page', redirectTo: 'produits', pathMatch: 'full' },       // redirection
    { path: '**', component: Introuvable, title: 'Page introuvable' },          // joker : DOIT être en dernier
];
```

```typescript
// src/app/app.config.ts
import { ApplicationConfig } from '@angular/core';
import { provideRouter, withComponentInputBinding } from '@angular/router';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
    providers: [provideRouter(routes, withComponentInputBinding())],
};
```

```typescript
// src/app/app.ts
import { Component } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

@Component({
    selector: 'app-root',
    imports: [RouterOutlet, RouterLink, RouterLinkActive],
    template: `
        <nav>
            <a routerLink="/" routerLinkActive="actif" [routerLinkActiveOptions]="{ exact: true }">Accueil</a>
            <a routerLink="/produits" routerLinkActive="actif">Produits</a>
        </nav>
        <router-outlet />
    `,
})
export class App {}
```

**Propriétés d'une route**

| Propriété | Rôle |
| --- | --- |
| `path` | Segment d'URL, sans `/` initial ; `''` = racine ; `:nom` = paramètre ; `'**'` = joker |
| `component` | Composant à afficher |
| `loadComponent` / `loadChildren` | Chargement **paresseux** d'un composant / d'un groupe de routes |
| `children` | Routes enfants (imbrication) |
| `redirectTo` + `pathMatch` | Redirection. `pathMatch: 'full'` exige que **tout** le chemin corresponde (indispensable pour `path: ''`) |
| `title` | Titre du document |
| `data` | Données statiques associées à la route |
| `resolve` | Données à charger **avant** l'activation |
| `canActivate`, `canActivateChild`, `canDeactivate`, `canMatch` | Gardes |
| `providers` | Services propres à la route (injecteur d'environnement) |
| `outlet` | Nom d'un *outlet* secondaire |
| `runGuardsAndResolvers` | Quand relancer gardes et résolveurs |

**Ordre d'évaluation.** Le routeur prend la **première** route qui correspond, de haut en bas : mettez les routes **les plus spécifiques d'abord** et le joker `**` **en dernier**. La stratégie `pathMatch: 'prefix'` (défaut) fait correspondre un **début** de chemin ; `'full'` exige l'égalité complète.

**Redirection dynamique.** `redirectTo` peut être une **fonction** qui reçoit la route et renvoie un chemin ou un `UrlTree`.

### 9.3 Naviguer

#### Par liens

```html
<a routerLink="/produits">Produits</a>                                      <!-- absolu -->
<a [routerLink]="['/produits', produit.id]">Détail</a>                      <!-- /produits/42 -->
<a routerLink="details">Relatif</a>                                          <!-- relatif à la route courante -->
<a [routerLink]="['/produits']" [queryParams]="{ page: 2, tri: 'prix' }" fragment="haut">Page 2</a>
<a routerLink="/produits" routerLinkActive="actif">Produits</a>              <!-- classe quand la route est active -->
```

Utilisez **`routerLink`** (sur des `<a>`) plutôt que `href` : `href` provoquerait un **rechargement complet** de la page. `routerLinkActive` ajoute une classe CSS quand l'URL correspond ; avec `[routerLinkActiveOptions]="{ exact: true }"`, la correspondance doit être exacte (utile pour `/`).

#### Par code

```typescript
// src/app/connexion.ts
import { Component, inject } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
    selector: 'app-connexion',
    template: `<button (click)="valider()">Valider</button>`,
})
export class Connexion {
    private readonly router = inject(Router);
    private readonly route = inject(ActivatedRoute);

    async valider(): Promise<void> {
        const ok = await this.router.navigate(['/produits', 42], { queryParams: { page: 2 }, fragment: 'avis' });
        await this.router.navigateByUrl('/produits/42?page=2');                            // par URL complète
        await this.router.navigate(['..'], { relativeTo: this.route });                  // relatif : remonte d'un niveau
        console.log(ok);                                                                    // true si la navigation a abouti
    }
}
```

`navigate()` prend un **tableau de segments** (échappement automatique) ; `navigateByUrl()` prend une **chaîne** d'URL. Les deux renvoient une promesse de booléen. Options utiles : `replaceUrl: true` (remplace l'entrée d'historique), `skipLocationChange`, `state` (données passées sans apparaître dans l'URL).

### 9.4 Paramètres, paramètres de requête et données

**Méthode moderne : liaison des entrées de route.** Avec `withComponentInputBinding()`, le routeur **lie** les paramètres de chemin, les paramètres de requête, les données statiques et les données résolues **aux entrées `input()` du composant** de même nom.

```typescript
// src/app/produits/detail.ts
import { Component, computed, input } from '@angular/core';

@Component({
    selector: 'app-detail-produit',
    template: `
        <h1>Produit n° {{ id() }}</h1>
        <p>Page de commentaires : {{ page() }} — Tri : {{ tri() }}</p>
        <p>Identifiant numérique : {{ idNumerique() }}</p>
    `,
})
export class DetailProduit {
    id = input.required<string>();                                    // :id dans le chemin
    page = input('1');                                                 // ?page=… (chaîne, valeur par défaut si absent)
    tri = input<string | undefined>(undefined);                       // ?tri=…
    idNumerique = computed(() => Number(this.id()));
}
```

Les valeurs arrivent **sous forme de chaînes** ; convertissez-les avec `transform: numberAttribute` ou un `computed()`. Le composant se **met à jour** quand les paramètres changent (même instance si seule la valeur de `:id` change).

**Méthode classique : `ActivatedRoute`.** Elle expose des **Observables** (`paramMap`, `queryParamMap`, `data`, `fragment`) et un **instantané** (`snapshot`) :

```typescript
// src/app/produits/detail-classique.ts
import { Component, inject } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { toSignal } from '@angular/core/rxjs-interop';
import { map } from 'rxjs';

@Component({ selector: 'app-detail-classique', template: `<p>{{ id() }}</p>` })
export class DetailClassique {
    private readonly route = inject(ActivatedRoute);
    protected readonly id = toSignal(this.route.paramMap.pipe(map((p) => p.get('id'))));
    // Instantané : valeur au moment de la création seulement
    private readonly initial = this.route.snapshot.paramMap.get('id');
}
```

> **Piège.** `snapshot` n'est **pas mis à jour** si Angular réutilise le composant pour une autre valeur de paramètre (navigation de `/produits/1` à `/produits/2`). Utilisez les Observables, `toSignal`, ou la liaison d'entrées.

**Données statiques** : `{ path: 'admin', component: Admin, data: { role: 'admin' } }` → entrée `role` avec liaison d'entrées, ou `route.data`.

### 9.5 Routes imbriquées et *outlets*

Une route peut avoir des **`children`** : le composant parent contient alors son propre `<router-outlet />` où s'affichent les enfants. C'est le mécanisme des **mises en page** (barre latérale, onglets).

```typescript
// src/app/app.routes.ts (extrait)
import { Routes } from '@angular/router';
import { Tableau } from './compte/tableau';
import { Profil } from './compte/profil';
import { Securite } from './compte/securite';
import { PageCompte } from './compte/page-compte';

export const routes: Routes = [
    {
        path: 'compte',
        component: PageCompte,                        // contient <router-outlet /> et la navigation interne
        children: [
            { path: '', component: Tableau },                 // /compte
            { path: 'profil', component: Profil },            // /compte/profil
            { path: 'securite', component: Securite },        // /compte/securite
        ],
    },
];
```

```typescript
// src/app/compte/page-compte.ts
import { Component } from '@angular/core';
import { RouterOutlet, RouterLink } from '@angular/router';

@Component({
    selector: 'app-page-compte',
    imports: [RouterOutlet, RouterLink],
    template: `
        <nav><a routerLink="profil">Profil</a> <a routerLink="securite">Sécurité</a></nav>
        <router-outlet />
    `,
})
export class PageCompte {}
```

**Routes sans composant** (« route de regroupement ») : on peut donner `children` sans `component` pour appliquer des gardes ou des `providers` à un groupe de routes. Les **outlets nommés** (`<router-outlet name="aside" />`, route `outlet: 'aside'`, URL `/(aside:aide)`) permettent d'afficher plusieurs zones indépendantes ; usage rare.

### 9.6 Chargement paresseux et préchargement

Le **chargement paresseux** (*lazy loading*) découpe l'application en **morceaux** (*chunks*) téléchargés **à la demande**, ce qui réduit le **bundle initial**.

```typescript
// src/app/app.routes.ts (extrait)
import { Routes } from '@angular/router';

export const routes: Routes = [
    // Un composant unique
    { path: 'a-propos', loadComponent: () => import('./a-propos').then((m) => m.APropos) },

    // Un groupe de routes (fichier de routes distinct)
    { path: 'admin', loadChildren: () => import('./admin/admin.routes').then((m) => m.ADMIN_ROUTES) },
];
```

```typescript
// src/app/admin/admin.routes.ts
import { Routes } from '@angular/router';
import { Utilisateurs } from './utilisateurs';

export const ADMIN_ROUTES: Routes = [
    { path: '', component: Utilisateurs },
];
```

Pour un groupe de routes exporté en `default`, `loadChildren: () => import('./admin/admin.routes')` suffit.

**Préchargement.** Par défaut, un morceau paresseux n'est téléchargé qu'à la **première navigation**. On peut anticiper :

```typescript
import { provideRouter, withPreloading, PreloadAllModules } from '@angular/router';
// providers: [provideRouter(routes, withPreloading(PreloadAllModules))]    // tout précharger en arrière-plan
```

`PreloadAllModules` précharge tout après le démarrage ; on peut écrire une **stratégie personnalisée** (`PreloadingStrategy`) qui précharge selon `data: { preload: true }` ou le type de connexion. Le chapitre 19 approfondit ces techniques.

### 9.7 Gardes de routes *(à jour : fonctionnelles)*

Une **garde** décide si une navigation est **autorisée**. Elle s'écrit sous forme de **fonction** (qui peut appeler `inject()`) et renvoie `boolean`, un `UrlTree` (**redirection**), ou une promesse / un Observable de ceux-ci.

| Garde | Moment |
| --- | --- |
| `canActivate` | Avant d'**activer** la route |
| `canActivateChild` | Avant d'activer une **route enfant** |
| `canDeactivate` | Avant de **quitter** la route (ex. : formulaire non enregistré) |
| `canMatch` | Avant de **faire correspondre** la route (choisit entre plusieurs routes, empêche le chargement du code) |

```typescript
// src/app/auth/auth-garde.ts
import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from './auth';

export const authGarde: CanActivateFn = (route, state) => {
    const auth = inject(AuthService);
    const router = inject(Router);
    return auth.estConnecte()
        ? true
        : router.createUrlTree(['/connexion'], { queryParams: { redirection: state.url } });   // redirection plutôt que `false`
};
```

```typescript
// src/app/auth/role-garde.ts : garde paramétrable (fabrique de garde)
import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from './auth';

export const roleGarde = (roleRequis: string): CanActivateFn => () => {
    const auth = inject(AuthService);
    return auth.aLeRole(roleRequis) ? true : inject(Router).createUrlTree(['/interdit']);
};
```

```typescript
// src/app/formulaire/quitter-garde.ts
import { CanDeactivateFn } from '@angular/router';

export interface AvecChangementsNonSauves { aDesChangements(): boolean; }

export const quitterGarde: CanDeactivateFn<AvecChangementsNonSauves> = (composant) =>
    !composant.aDesChangements() || confirm('Quitter sans enregistrer ?');
```

```typescript
// src/app/app.routes.ts (extrait)
import { Routes } from '@angular/router';
import { authGarde } from './auth/auth-garde';
import { roleGarde } from './auth/role-garde';

export const routes: Routes = [
    {
        path: 'admin',
        canActivate: [authGarde, roleGarde('admin')],
        loadChildren: () => import('./admin/admin.routes').then((m) => m.ADMIN_ROUTES),
    },
];
```

- Les gardes d'une même liste s'exécutent **en séquence** ; la navigation est interrompue au premier refus.
- **`canMatch`** est préférable à `canLoad` *(héritage)* : il empêche aussi le téléchargement du code d'une route protégée.
- Une garde est une **commodité d'expérience utilisateur**, **jamais une sécurité** : un utilisateur peut contourner le code client. Les données doivent être **protégées par le serveur** (chapitre 27).
- Anciennes gardes à base de **classes** (`implements CanActivate`) : toujours possibles mais dépréciées ; migration manuelle simple vers des fonctions.

### 9.8 Résolveurs

Un **résolveur** (`ResolveFn`) charge des **données avant** l'activation de la route : le composant s'affiche avec ses données prêtes.

```typescript
// src/app/produits/produit-resolveur.ts
import { inject } from '@angular/core';
import { ResolveFn, Router } from '@angular/router';
import { catchError, of } from 'rxjs';
import { ProduitService, Produit } from './produit-service';

export const produitResolveur: ResolveFn<Produit | null> = (route) => {
    const router = inject(Router);
    return inject(ProduitService).obtenir(route.paramMap.get('id')!).pipe(
        catchError(() => { router.navigate(['/introuvable']); return of(null); }),
    );
};
```

```typescript
// src/app/app.routes.ts (extrait)
import { Routes } from '@angular/router';
import { produitResolveur } from './produits/produit-resolveur';
import { DetailProduit } from './produits/detail';

export const routes: Routes = [
    { path: 'produits/:id', component: DetailProduit, resolve: { produit: produitResolveur } },
];
```

Dans le composant, la donnée résolue arrive par une entrée du **même nom** : `produit = input<Produit | null>();` (avec `withComponentInputBinding()`).

> **Compromis.** Un résolveur **bloque** la navigation tant que la donnée n'est pas arrivée : l'utilisateur ne voit rien changer. Pour un meilleur ressenti, affichez la page tout de suite avec un **état de chargement** (`resource`, `@defer`, squelettes) et réservez les résolveurs aux données **indispensables**.

### 9.9 Configuration du routeur

Les options s'activent par des fonctions `withXxx()` passées à `provideRouter` :

| Fonction | Effet |
| --- | --- |
| `withComponentInputBinding()` | Lie paramètres / données aux `input()` |
| `withInMemoryScrolling({ scrollPositionRestoration: 'enabled', anchorScrolling: 'enabled' })` | Remonte en haut à chaque navigation, restaure la position à l'arrière, gère les ancres |
| `withViewTransitions()` | Transitions animées entre pages (API View Transitions) |
| `withPreloading(...)` | Préchargement du code paresseux |
| `withRouterConfig({ onSameUrlNavigation: 'reload', paramsInheritanceStrategy: 'always' })` | Options diverses |
| `withHashLocation()` | URL de type `/#/page` (pour des hébergements sans redirection) |
| `withNavigationErrorHandler(fn)` | Gestion centralisée des erreurs de navigation |
| `withDebugTracing()` | Journal des événements du routeur (développement) |

```typescript
// src/app/app.config.ts
import { ApplicationConfig } from '@angular/core';
import { provideRouter, withComponentInputBinding, withInMemoryScrolling, withViewTransitions } from '@angular/router';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
    providers: [
        provideRouter(
            routes,
            withComponentInputBinding(),
            withInMemoryScrolling({ scrollPositionRestoration: 'enabled', anchorScrolling: 'enabled' }),
            withViewTransitions(),
        ),
    ],
};
```

**Titre de page.** `title: 'Produits'` sur la route, ou une fonction (`title: () => inject(Service).titre()`). Une **`TitleStrategy`** personnalisée ajoute un préfixe ou un suffixe commun (« Produits — Ma boutique »). Le titre est important pour l'accessibilité et le référencement.

**Événements du routeur.** `router.events` émet `NavigationStart`, `RoutesRecognized`, `GuardsCheckStart`, `ResolveStart`, `NavigationEnd`, `NavigationCancel`, `NavigationError`… Exemple : afficher un indicateur de chargement.

```typescript
// src/app/indicateur.ts
import { Component, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { NavigationEnd, NavigationStart, NavigationCancel, NavigationError, Router } from '@angular/router';
import { filter, map } from 'rxjs';

@Component({
    selector: 'app-indicateur',
    template: `@if (enCours()) { <div class="barre">Chargement…</div> }`,
})
export class Indicateur {
    private readonly router = inject(Router);
    protected readonly enCours = toSignal(
        this.router.events.pipe(
            filter((e) => e instanceof NavigationStart || e instanceof NavigationEnd || e instanceof NavigationCancel || e instanceof NavigationError),
            map((e) => e instanceof NavigationStart),
        ),
        { initialValue: false },
    );
}
```

### 9.10 Déploiement d'une SPA routée

Quand l'utilisateur recharge `/produits/42`, le navigateur demande **cette URL au serveur**, qui ne connaît pas ce fichier. Le serveur doit donc **renvoyer `index.html`** pour toute URL inconnue (« *fallback* »). Sans cela : erreur 404 au rechargement. Selon l'hébergeur : règle de réécriture (Nginx : `try_files $uri /index.html;`), fichier de configuration (`_redirects`, `firebase.json`, `staticwebapp.config.json`…). Avec le **SSR**, le serveur Node s'en charge. `withHashLocation()` est un dernier recours.

### 9.11 Bonnes pratiques

- **Une route par page**, un fichier de routes par fonctionnalité, **chargement paresseux** par défaut.
- Liaison d'entrées (`withComponentInputBinding`) plutôt que `ActivatedRoute` dans les nouveaux composants.
- Gardes **fonctionnelles** et **toujours** doublées d'une vérification côté serveur.
- Redirection par `UrlTree` plutôt que `router.navigate` dans une garde.
- Route `**` pour les URL inconnues et vraie **réponse 404** côté serveur en SSR.
- Navigation **testée** (`RouterTestingHarness`, chapitre 16).

### Synthèse du chapitre 9

Le routeur associe URL et composant : `Routes` + `provideRouter` + `<router-outlet />`. On navigue par `routerLink` ou `Router.navigate`. Paramètres et données arrivent par **entrées** (`withComponentInputBinding`). Les **routes enfants** composent les mises en page, `loadComponent` / `loadChildren` découpent le code, les **gardes** contrôlent l'accès (UX, pas sécurité), les **résolveurs** préchargent. Le serveur doit renvoyer `index.html` pour les URL inconnues.

---

## 10. Formulaires

**Objectifs d'apprentissage.** Distinguer les **trois approches** de formulaires d'Angular et choisir ; construire un formulaire **piloté par le gabarit** (`ngModel`), un formulaire **réactif** (`FormGroup`, `FormControl`, `FormArray`, `FormBuilder`) et un formulaire à **signaux** (*Signal Forms*) ; valider (validateurs intégrés, personnalisés, inter-champs, asynchrones) ; afficher les erreurs de façon accessible ; gérer la soumission ; créer un contrôle de formulaire personnalisé.

### 10.1 Trois approches

|  | **Piloté par le gabarit** (*template-driven*) | **Réactif** (*reactive*) | **Signal Forms** *(stable en v22)* |
| --- | --- | --- | --- |
| Paquet / import | `FormsModule` | `ReactiveFormsModule` | `@angular/forms/signals` |
| Où vit le modèle | Dans le **gabarit** (`ngModel`) | Dans la **classe** (`FormGroup`…) | Dans un **signal** (le modèle de données) |
| Validation | Attributs HTML (`required`…) | Fonctions `Validators` | Fonctions `required()`, `email()`… dans un **schéma** |
| Réactivité | Implicite | **Observables** (`valueChanges`) | **Signaux** (`value()`, `errors()`) |
| Typage | Faible | Fort (formulaires typés) | Fort (déduit du modèle) |
| Usage idéal | Petits formulaires simples | Formulaires complexes, existants | **Nouveaux projets** |

**Choix.** Pour un **nouveau** projet en Angular 22, privilégiez **Signal Forms**. Les formulaires **réactifs** restent le choix sûr pour le code existant, les cas très dynamiques déjà maîtrisés et les bibliothèques qui s'y appuient (par exemple de nombreux composants UI). Le mode piloté par le gabarit convient aux formulaires de deux ou trois champs. Les trois approches **peuvent coexister** dans une application.

**Notions communes.** Quelle que soit l'approche, un formulaire gère : une **valeur**, un **état de validité** (valide / invalide / en attente), un **état d'interaction** (*touched* : le champ a perdu le focus ; *dirty* : la valeur a été modifiée par l'utilisateur ; leurs contraires *untouched* / *pristine*), des **erreurs** et un état **activé / désactivé**.

### 10.2 Formulaires pilotés par le gabarit

On importe `FormsModule`, on lie chaque champ avec `[(ngModel)]` en lui donnant un attribut `name`, et on déclare la validation par des **attributs HTML**. Angular crée en coulisses le `FormGroup` et les `FormControl`.

```typescript
// src/app/inscription-gabarit.ts
import { Component } from '@angular/core';
import { FormsModule, NgForm } from '@angular/forms';

@Component({
    selector: 'app-inscription-gabarit',
    imports: [FormsModule],
    template: `
        <form #f="ngForm" (ngSubmit)="envoyer(f)" novalidate>
            <label for="nom">Nom</label>
            <input id="nom" name="nom" [(ngModel)]="modele.nom" required minlength="3" #nom="ngModel" />
            @if (nom.invalid && (nom.dirty || nom.touched)) {
                <p role="alert">
                    @if (nom.errors?.['required']) { Le nom est obligatoire. }
                    @else if (nom.errors?.['minlength']) { Au moins {{ nom.errors?.['minlength'].requiredLength }} caractères. }
                </p>
            }

            <label for="courriel">Courriel</label>
            <input id="courriel" name="courriel" type="email" [(ngModel)]="modele.courriel" required email #courriel="ngModel" />

            <button type="submit" [disabled]="f.invalid">S'inscrire</button>
        </form>
    `,
})
export class InscriptionGabarit {
    protected modele = { nom: '', courriel: '' };

    protected envoyer(f: NgForm): void {
        if (f.invalid) return;
        console.log('Valeurs :', f.value);
    }
}
```

**Points clés**

- **`name`** est **obligatoire** sur chaque champ lié à `ngModel` dans un `<form>` (c'est la clé dans le groupe).
- **`#f="ngForm"`** donne accès à l'objet formulaire (`f.valid`, `f.value`, `f.submitted`) ; **`#nom="ngModel"`** donne accès au contrôle d'un champ.
- Angular ajoute des **classes CSS d'état** : `ng-valid` / `ng-invalid`, `ng-pristine` / `ng-dirty`, `ng-untouched` / `ng-touched`, utiles pour le style.
- **`(ngSubmit)`** est émis à la soumission ; `novalidate` désactive la validation native du navigateur pour laisser Angular l'afficher.
- **Limites** : la logique est dans le gabarit, plus difficile à tester, à typer et à rendre dynamique. Au-delà de quelques champs, préférez une autre approche.

### 10.3 Formulaires réactifs

Le modèle du formulaire est un **arbre d'objets** construit **dans la classe**, puis lié au gabarit.

| Classe | Rôle |
| --- | --- |
| `FormControl<T>` | Un **champ** (valeur, état, validateurs) |
| `FormGroup` | Un **groupe** de contrôles nommés (objet) |
| `FormArray` | Une **liste** dynamique de contrôles ou de groupes |
| `FormBuilder` | **Fabrique** abrégée (`group`, `control`, `array`) |
| `AbstractControl` | Classe de base commune (propriétés d'état, `setValue`…) |

```typescript
// src/app/inscription-reactive.ts
import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
    selector: 'app-inscription-reactive',
    imports: [ReactiveFormsModule],
    template: `
        <form [formGroup]="formulaire" (ngSubmit)="envoyer()">
            <label for="nom">Nom</label>
            <input id="nom" formControlName="nom" [attr.aria-invalid]="nom.invalid && nom.touched" />
            @if (nom.touched && nom.errors) {
                <p role="alert">
                    @if (nom.errors['required']) { Le nom est obligatoire. }
                    @if (nom.errors['minlength']) { Trop court. }
                </p>
            }

            <label for="courriel">Courriel</label>
            <input id="courriel" type="email" formControlName="courriel" />

            <fieldset formGroupName="adresse">
                <legend>Adresse</legend>
                <input formControlName="ville" placeholder="Ville" />
            </fieldset>

            <button type="submit" [disabled]="formulaire.invalid">Envoyer</button>
        </form>
    `,
})
export class InscriptionReactive {
    private readonly fb = inject(FormBuilder);

    protected readonly formulaire = this.fb.nonNullable.group({
        nom: ['', [Validators.required, Validators.minLength(3)]],
        courriel: ['', [Validators.required, Validators.email]],
        adresse: this.fb.nonNullable.group({ ville: [''] }),
    });

    protected get nom() { return this.formulaire.controls.nom; }     // accès typé : FormControl<string>

    protected envoyer(): void {
        if (this.formulaire.invalid) { this.formulaire.markAllAsTouched(); return; }
        console.log(this.formulaire.getRawValue());      // { nom: string; courriel: string; adresse: { ville: string } }
    }
}
```

**Formulaires typés.** Depuis la version 14, `FormControl<string>` et `FormGroup<{ nom: FormControl<string> }>` sont **typés** ; `this.fb.nonNullable` crée des contrôles dont la valeur **n'est jamais `null`** après un `reset()` (sans cela, `reset()` remet `null` et le type devient `string | null`).

**Validateurs intégrés** : `Validators.required`, `requiredTrue` (case à cocher), `min`, `max`, `minLength`, `maxLength`, `email`, `pattern`, et leurs combinaisons (`Validators.compose`).

**Propriétés et méthodes d'un contrôle**

| Élément | Rôle |
| --- | --- |
| `value`, `getRawValue()` | Valeur (le groupe omet les contrôles désactivés ; `getRawValue()` les inclut) |
| `valid`, `invalid`, `pending`, `status` | Validité (`VALID`, `INVALID`, `PENDING`, `DISABLED`) |
| `errors` | Objet d'erreurs (ex. `{ required: true }`) ou `null` |
| `touched`, `dirty`, `pristine` | État d'interaction |
| `setValue(v)` | Définit **toute** la valeur (structure complète exigée) |
| `patchValue(v)` | Met à jour **une partie** de la valeur |
| `reset(v?)` | Réinitialise valeur et état |
| `disable()`, `enable()` | Active / désactive |
| `markAsTouched()`, `markAllAsTouched()` | Force l'état d'interaction (pour afficher les erreurs à la soumission) |
| `valueChanges`, `statusChanges` | **Observables** des changements |
| `setValidators()`, `updateValueAndValidity()` | Changer les validateurs dynamiquement |

**Option `updateOn`** : `'change'` (défaut), `'blur'` ou `'submit'` — moment où la valeur et la validation sont mises à jour (utile pour réduire le bruit).

```typescript
// src/app/recherche-reactive.ts
import { Component, inject } from '@angular/core';
import { FormControl, ReactiveFormsModule } from '@angular/forms';
import { toSignal } from '@angular/core/rxjs-interop';
import { debounceTime, distinctUntilChanged } from 'rxjs';

@Component({
    selector: 'app-recherche-reactive',
    imports: [ReactiveFormsModule],
    template: `<input [formControl]="terme" /> <p>Recherche : {{ termeLisse() }}</p>`,
})
export class RechercheReactive {
    protected readonly terme = new FormControl('', { nonNullable: true });
    protected readonly termeLisse = toSignal(
        this.terme.valueChanges.pipe(debounceTime(300), distinctUntilChanged()),   // anti-rebond
        { initialValue: '' },
    );
}
```

#### Validateurs personnalisés

Un validateur est une **fonction** qui reçoit un contrôle et renvoie `null` (valide) ou un **objet d'erreur**.

```typescript
// src/app/validateurs.ts
import { AbstractControl, AsyncValidatorFn, ValidationErrors, ValidatorFn } from '@angular/forms';
import { Observable, map, of, delay } from 'rxjs';

// Validateur synchrone, paramétrable (fabrique)
export function interdire(motInterdit: string): ValidatorFn {
    return (controle: AbstractControl): ValidationErrors | null =>
        String(controle.value ?? '').toLowerCase().includes(motInterdit) ? { interdit: { valeur: controle.value } } : null;
}

// Validateur inter-champs, appliqué au GROUPE
export const motsDePasseIdentiques: ValidatorFn = (groupe: AbstractControl): ValidationErrors | null => {
    const mdp = groupe.get('motDePasse')?.value;
    const confirmation = groupe.get('confirmation')?.value;
    return mdp === confirmation ? null : { motsDePasseDifferents: true };
};

// Validateur asynchrone (ex. : disponibilité d'un nom, normalement via HTTP)
export function nomDisponible(pris: string[]): AsyncValidatorFn {
    return (controle: AbstractControl): Observable<ValidationErrors | null> =>
        of(pris.includes(controle.value)).pipe(delay(300), map((estPris) => (estPris ? { nomPris: true } : null)));
}
```

```typescript
// src/app/creation-compte.ts
import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { interdire, motsDePasseIdentiques, nomDisponible } from './validateurs';

@Component({
    selector: 'app-creation-compte',
    imports: [ReactiveFormsModule],
    template: `
        <form [formGroup]="formulaire">
            <input formControlName="nom" />
            @if (formulaire.controls.nom.pending) { <p>Vérification…</p> }
            <input type="password" formControlName="motDePasse" />
            <input type="password" formControlName="confirmation" />
            @if (formulaire.errors?.['motsDePasseDifferents'] && formulaire.controls.confirmation.touched) {
                <p role="alert">Les mots de passe diffèrent.</p>
            }
        </form>
    `,
})
export class CreationCompte {
    private readonly fb = inject(FormBuilder);
    protected readonly formulaire = this.fb.nonNullable.group(
        {
            nom: ['', [Validators.required, interdire('admin')], [nomDisponible(['alice', 'bob'])]],   // 3e argument : asynchrones
            motDePasse: ['', [Validators.required, Validators.minLength(8)]],
            confirmation: [''],
        },
        { validators: [motsDePasseIdentiques] },       // validateur du groupe
    );
}
```

Les validateurs **asynchrones** ne s'exécutent que lorsque les validateurs **synchrones** sont satisfaits ; le contrôle est `pending` pendant l'attente. Limitez les appels réseau (anti-rebond, `updateOn: 'blur'`).

#### Listes dynamiques : `FormArray`

```typescript
// src/app/liste-competences.ts
import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
    selector: 'app-liste-competences',
    imports: [ReactiveFormsModule],
    template: `
        <form [formGroup]="formulaire">
            <div formArrayName="competences">
                @for (c of competences.controls; track c; let i = $index) {
                    <div>
                        <input [formControlName]="i" />
                        <button type="button" (click)="retirer(i)">Retirer</button>
                    </div>
                }
            </div>
            <button type="button" (click)="ajouter()">Ajouter</button>
        </form>
    `,
})
export class ListeCompetences {
    private readonly fb = inject(FormBuilder);
    protected readonly formulaire = this.fb.nonNullable.group({
        competences: this.fb.nonNullable.array([this.fb.nonNullable.control('Angular', Validators.required)]),
    });
    protected get competences() { return this.formulaire.controls.competences; }

    protected ajouter(): void { this.competences.push(this.fb.nonNullable.control('', Validators.required)); }
    protected retirer(i: number): void { this.competences.removeAt(i); }
}
```

#### Contrôles personnalisés : `ControlValueAccessor`

Pour qu'un **composant personnalisé** (sélecteur d'étoiles, éditeur riche) fonctionne avec `ngModel`, `formControlName` ou `[formControl]`, il implémente **`ControlValueAccessor`** (CVA) — le « pont » entre le modèle du formulaire et le composant.

```typescript
// src/app/champ-note.ts
import { Component, forwardRef, signal } from '@angular/core';
import { ControlValueAccessor, NG_VALUE_ACCESSOR } from '@angular/forms';

@Component({
    selector: 'app-champ-note',
    providers: [{ provide: NG_VALUE_ACCESSOR, useExisting: forwardRef(() => ChampNote), multi: true }],
    template: `
        @for (n of [1, 2, 3, 4, 5]; track n) {
            <button type="button" [disabled]="desactive()" [attr.aria-pressed]="n <= valeur()" (click)="choisir(n)">★</button>
        }
    `,
})
export class ChampNote implements ControlValueAccessor {
    protected readonly valeur = signal(0);
    protected readonly desactive = signal(false);
    private surChangement: (v: number) => void = () => {};
    private surTouche: () => void = () => {};

    writeValue(v: number | null): void { this.valeur.set(v ?? 0); }               // formulaire → composant
    registerOnChange(fn: (v: number) => void): void { this.surChangement = fn; }  // composant → formulaire
    registerOnTouched(fn: () => void): void { this.surTouche = fn; }
    setDisabledState(etat: boolean): void { this.desactive.set(etat); }

    protected choisir(n: number): void {
        this.valeur.set(n);
        this.surChangement(n);
        this.surTouche();
    }
}
```

Usage : `<app-champ-note formControlName="note" />`. Avec **Signal Forms**, un contrôle personnalisé peut au contraire exposer directement des entrées et sorties de type `model()` : consultez le guide « Custom controls » d'angular.dev.

### 10.4 Signal Forms *(stable en v22)*

**Principe.** Le **modèle de données** est un simple **signal**. La fonction `form()` en crée un **arbre de champs** (`FieldTree`) qui reflète sa forme ; la directive `[formField]` lie chaque champ HTML. Valeur, validité, erreurs et état d'interaction sont des **signaux**. Le modèle reste la **source de vérité** : modifier un champ met à jour le signal, et inversement.

```typescript
// src/app/connexion-signal.ts
import { Component, signal } from '@angular/core';
import { form, FormField, required, email, minLength } from '@angular/forms/signals';

interface DonneesConnexion { courriel: string; motDePasse: string; }

@Component({
    selector: 'app-connexion-signal',
    imports: [FormField],
    template: `
        <form (submit)="envoyer($event)">
            <label>Courriel
                <input type="email" [formField]="formulaire.courriel" />
            </label>
            @if (formulaire.courriel().touched() && formulaire.courriel().invalid()) {
                <ul role="alert">
                    @for (erreur of formulaire.courriel().errors(); track erreur) { <li>{{ erreur.message }}</li> }
                </ul>
            }

            <label>Mot de passe
                <input type="password" [formField]="formulaire.motDePasse" />
            </label>
            @if (formulaire.motDePasse().touched() && formulaire.motDePasse().invalid()) {
                <ul role="alert">
                    @for (erreur of formulaire.motDePasse().errors(); track erreur) { <li>{{ erreur.message }}</li> }
                </ul>
            }

            <button type="submit" [disabled]="formulaire().invalid()">Se connecter</button>
            <p>Courriel saisi : {{ formulaire.courriel().value() }}</p>
        </form>
    `,
})
export class ConnexionSignal {
    // 1. Le modèle : un signal
    protected readonly modele = signal<DonneesConnexion>({ courriel: '', motDePasse: '' });

    // 2. L'arbre de champs, avec un schéma de validation
    protected readonly formulaire = form(this.modele, (chemin) => {
        required(chemin.courriel, { message: 'Le courriel est obligatoire' });
        email(chemin.courriel, { message: 'Courriel invalide' });
        required(chemin.motDePasse, { message: 'Le mot de passe est obligatoire' });
        minLength(chemin.motDePasse, 8, { message: 'Au moins 8 caractères' });
    });

    protected envoyer(evenement: Event): void {
        evenement.preventDefault();
        if (this.formulaire().invalid()) return;
        console.log('Connexion avec', this.modele());      // le signal contient les valeurs courantes
    }
}
```

**Éléments à connaître**

- **`form(modele, schema?)`** renvoie un `FieldTree`. **Appeler un nœud comme une fonction** (`formulaire.courriel()`) renvoie son **état** ; appeler la racine (`formulaire()`) donne l'état du formulaire entier.
- **`[formField]`** (classe `FormField` à importer) lie un champ à un `<input>`, `<textarea>`, `<select>`, case à cocher ou bouton radio, et synchronise aussi `required`, `disabled`, `readonly`. Les `<input type="number">` donnent des nombres, `date` / `time` des chaînes ISO. Le `<select multiple>` n'est pas géré.
- Le **schéma** reçoit un **chemin** (`chemin.courriel`) et déclare les règles : `required()`, `email()`, `min()`, `max()`, `minLength()`, `maxLength()`, `pattern()`, ainsi que `debounce()` pour temporiser la mise à jour de la valeur.
- **Valeur** : `formulaire.courriel().value()` (lecture) ; `formulaire.courriel().value.set('x')` (écriture, qui met aussi à jour le modèle).

**Signaux d'état d'un nœud**

| Signal | Signification |
| --- | --- |
| `value()` | Valeur courante |
| `valid()` / `invalid()` | Conforme / en erreur |
| `pending()` | Validation asynchrone en cours |
| `touched()` | Le champ (ou un enfant) a reçu puis perdu le focus |
| `dirty()` | Valeur modifiée par l'utilisateur |
| `disabled()` / `readonly()` | Désactivé / lecture seule |
| `errors()` | Tableau d'erreurs (`kind`, `message`, …) |

**Règles plus avancées** (validation personnalisée avec accès aux autres champs, validation conditionnelle, champs désactivés ou masqués selon d'autres valeurs, validation asynchrone et HTTP, soumission avec `submit()`, erreurs renvoyées par le serveur, validation par schéma standard) sont décrites dans les guides *Validation* et *Field state management* d'angular.dev : les noms et signatures exacts évoluent avec les versions, **vérifiez-les dans la documentation de votre version** avant de les utiliser.

> **Historique des noms.** L'API a changé pendant sa phase expérimentale (v21) : la directive s'est d'abord appelée `[control]` (classe `Control`), puis `[field]` (classe `Field`), avant de devenir `[formField]` (classe `FormField`). Si vous lisez un tutoriel ancien, adaptez ces noms.

**Signal Forms et formulaires réactifs.** Ils reposent sur des modèles différents (signal contre arbre d'objets mutables) : migrez **par formulaire**, pas par morceaux d'un même formulaire. Consultez les guides de migration et d'interopérabilité d'angular.dev pour les ponts éventuels.

### 10.5 Afficher les erreurs de façon accessible

- Chaque champ possède un **`<label>`** associé (`for` / `id`, ou `<label>` englobant) : jamais un simple `placeholder`.
- N'affichez les erreurs qu'**après interaction** (`touched`) ou à la **soumission**, pour ne pas agresser l'utilisateur dès l'arrivée sur la page.
- Signalez l'erreur aux technologies d'assistance : `aria-invalid="true"` sur le champ, `aria-describedby` pointant l'élément de message, `role="alert"` (ou une région `aria-live`) pour l'annonce.
- Ne vous fiez pas à la **couleur seule** : ajoutez un texte clair et, si utile, une icône.
- Messages **précis et actionnables** (« Au moins 8 caractères »), pas « Champ invalide ».
- Au refus de soumission, **placez le focus** sur le premier champ invalide.

```html
<input id="courriel" type="email" [formField]="formulaire.courriel"
       [attr.aria-invalid]="formulaire.courriel().touched() && formulaire.courriel().invalid()"
       aria-describedby="courriel-erreur" />
<p id="courriel-erreur" role="alert">…</p>
```

### 10.6 Soumission du formulaire

1. **Valider** : si le formulaire est invalide, marquer les champs comme touchés (afin d'afficher les erreurs) et s'arrêter.
2. **Empêcher la double soumission** : un signal `enCours` désactive le bouton pendant l'envoi.
3. **Envoyer** via un service (`HttpClient`, chapitre 11).
4. **Gérer la réponse** : succès (redirection, message de confirmation) ou erreurs **serveur** (par exemple « courriel déjà utilisé »), à rattacher au champ concerné.
5. **Ne jamais faire confiance** à la validation côté client : le serveur **revalide toujours**.

```typescript
// src/app/envoi.ts
import { Component, inject, signal } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { finalize } from 'rxjs';

@Component({
    selector: 'app-envoi',
    imports: [ReactiveFormsModule],
    template: `
        <form [formGroup]="formulaire" (ngSubmit)="envoyer()">
            <input formControlName="courriel" />
            <button type="submit" [disabled]="enCours()">{{ enCours() ? 'Envoi…' : 'Envoyer' }}</button>
        </form>
    `,
})
export class Envoi {
    private readonly http = inject(HttpClient);
    private readonly fb = inject(FormBuilder);
    protected readonly enCours = signal(false);
    protected readonly formulaire = this.fb.nonNullable.group({ courriel: ['', [Validators.required, Validators.email]] });

    protected envoyer(): void {
        if (this.formulaire.invalid) { this.formulaire.markAllAsTouched(); return; }
        this.enCours.set(true);
        this.http.post('/api/inscription', this.formulaire.getRawValue()).pipe(finalize(() => this.enCours.set(false))).subscribe({
            next: () => this.formulaire.reset(),
            error: (e) => this.formulaire.controls.courriel.setErrors({ serveur: e.error?.message ?? 'Erreur' }),   // erreur rattachée au champ
        });
    }
}
```

### 10.7 Bonnes pratiques et pièges

- Un **nouveau** formulaire : **Signal Forms** ; pour l'existant, **réactif** ; ne mélangez pas deux approches **dans le même formulaire**.
- Oublier `name` sur un `ngModel` dans un `<form>` : erreur d'exécution.
- Oublier d'importer `ReactiveFormsModule` : erreur « Can't bind to 'formGroup' ».
- `setValue` exige **tous** les champs ; `patchValue` accepte un sous-ensemble.
- Utiliser `nonNullable` pour garder des types précis après `reset()`.
- Se **désabonner** de `valueChanges` : `takeUntilDestroyed()` ou `toSignal()`.
- Valeur d'un `<input type="number">` en réactif : c'est un `number | null`, pas une chaîne.
- Préparer les formulaires à l'**internationalisation** : messages d'erreur traduits (chapitre 21).

### Synthèse du chapitre 10

Trois approches : **gabarit** (`ngModel`), **réactive** (`FormGroup`, `FormControl`, `FormArray`, `FormBuilder`, validateurs fonctions) et **Signal Forms** (`signal` + `form()` + `[formField]` + schéma de validateurs), cette dernière étant recommandée pour les nouveaux projets en v22. Dans tous les cas : validation claire et accessible, soumission contrôlée, revalidation côté serveur.

---

# Partie II — Angular avancé

## 11. Client HTTP

**Objectifs d'apprentissage.** Activer et utiliser `HttpClient` ; envoyer les cinq verbes principaux avec paramètres, en-têtes et corps ; typer les réponses ; gérer les **erreurs** (`HttpErrorResponse`, `catchError`, `retry`) ; écrire des **intercepteurs** fonctionnels (jeton, erreurs, chargement, cache) ; suivre une **progression** ; comprendre CORS, proxy et XSRF ; tester les appels HTTP.

### 11.1 Mise en place

**`HttpClient`** est le service d'Angular pour communiquer avec une **API** (le plus souvent REST/JSON). Il renvoie des **Observables** *froids* : la requête n'est envoyée qu'à l'**abonnement**, et **chaque abonnement** relance une requête.

```typescript
// src/app/app.config.ts
import { ApplicationConfig } from '@angular/core';
import { provideHttpClient, withFetch, withInterceptors } from '@angular/common/http';
import { jetonIntercepteur } from './jeton-intercepteur';

export const appConfig: ApplicationConfig = {
    providers: [
        provideHttpClient(
            withFetch(),                                  // utilise l'API fetch (recommandé, indispensable avec le SSR)
            withInterceptors([jetonIntercepteur]),        // intercepteurs fonctionnels
        ),
    ],
};
```

Sans `provideHttpClient()`, l'injection de `HttpClient` échoue (`NullInjectorError`). *(héritage)* : `HttpClientModule`.

### 11.2 Les requêtes de base

```typescript
// src/app/produit-api.ts
import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Produit { id: number; nom: string; prix: number; }
export type NouveauProduit = Omit<Produit, 'id'>;

@Injectable({ providedIn: 'root' })
export class ProduitApi {
    private readonly http = inject(HttpClient);
    private readonly base = '/api/produits';

    lister(page = 1, tri = 'nom'): Observable<Produit[]> {
        const params = new HttpParams().set('page', page).set('tri', tri);     // ?page=1&tri=nom (HttpParams est immuable)
        return this.http.get<Produit[]>(this.base, { params });
    }
    obtenir(id: number): Observable<Produit> {
        return this.http.get<Produit>(`${this.base}/${id}`);
    }
    creer(p: NouveauProduit): Observable<Produit> {
        return this.http.post<Produit>(this.base, p);                         // corps sérialisé en JSON
    }
    remplacer(p: Produit): Observable<Produit> {
        return this.http.put<Produit>(`${this.base}/${p.id}`, p);              // remplacement complet
    }
    modifier(id: number, partiel: Partial<NouveauProduit>): Observable<Produit> {
        return this.http.patch<Produit>(`${this.base}/${id}`, partiel);        // modification partielle
    }
    supprimer(id: number): Observable<void> {
        return this.http.delete<void>(`${this.base}/${id}`);
    }
    avecEntetes(): Observable<Produit[]> {
        const headers = new HttpHeaders({ 'X-Version': '2', Accept: 'application/json' });
        return this.http.get<Produit[]>(this.base, { headers });
    }
}
```

| Verbe | Usage | Idempotent |
| --- | --- | --- |
| `GET` | Lire | Oui |
| `POST` | Créer / déclencher une action | Non |
| `PUT` | Remplacer une ressource | Oui |
| `PATCH` | Modifier une partie | Non (selon l'API) |
| `DELETE` | Supprimer | Oui |

**Options de requête** : `params` (`HttpParams` ou objet simple), `headers`, `responseType` (`'json'` défaut, `'text'`, `'blob'`, `'arraybuffer'`), `observe` (`'body'` défaut, `'response'` pour accéder au statut et aux en-têtes, `'events'` pour la progression), `withCredentials` (envoyer les cookies entre domaines), `context`, `reportProgress`, `transferCache` (SSR).

```typescript
// Accès au statut et aux en-têtes
this.http.get<Produit[]>('/api/produits', { observe: 'response' }).subscribe((r) => {
    console.log(r.status, r.headers.get('X-Total-Count'), r.body);
});
```

**Utilisation dans un composant.** Le chemin le plus simple et le plus sûr : `toSignal()` ou `httpResource` (chapitre 8) ; sinon le tube `async`.

```typescript
// src/app/liste-produits.ts
import { Component, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { ProduitApi } from './produit-api';

@Component({
    selector: 'app-liste-produits',
    template: `
        @for (p of produits(); track p.id) { <p>{{ p.nom }} — {{ p.prix }} €</p> } @empty { <p>Aucun produit</p> }
    `,
})
export class ListeProduits {
    protected readonly produits = toSignal(inject(ProduitApi).lister(), { initialValue: [] });
}
```

> **Types ≠ validation.** `get<Produit[]>()` **affirme** le type, il ne **vérifie** rien à l'exécution. Pour des données peu fiables, validez avec une bibliothèque de schémas (Zod, Valibot) avant usage.

### 11.3 Gestion des erreurs

Une réponse HTTP **4xx / 5xx**, une coupure réseau ou un délai dépassé produisent une **erreur** de l'Observable, de type **`HttpErrorResponse`**.

| Propriété | Signification |
| --- | --- |
| `status` | Code HTTP (`0` : erreur réseau / CORS / hors ligne) |
| `statusText`, `message` | Description |
| `error` | Corps de la réponse (message du serveur) ou `ProgressEvent` |
| `url`, `headers` | Requête / en-têtes de réponse |

```typescript
// src/app/produit-service.ts
import { Injectable, inject } from '@angular/core';
import { HttpErrorResponse } from '@angular/common/http';
import { Observable, catchError, retry, throwError, timer } from 'rxjs';
import { ProduitApi, Produit } from './produit-api';

@Injectable({ providedIn: 'root' })
export class ProduitService {
    private readonly api = inject(ProduitApi);

    obtenir(id: number): Observable<Produit> {
        return this.api.obtenir(id).pipe(
            retry({ count: 2, delay: (_e, essai) => timer(500 * essai) }),     // 2 nouvelles tentatives, attente croissante
            catchError((e: HttpErrorResponse) => {
                const message = e.status === 0 ? 'Réseau indisponible' : e.status === 404 ? 'Produit introuvable' : 'Erreur serveur';
                return throwError(() => new Error(message));                       // relance une erreur normalisée
            }),
        );
    }
}
```

**Stratégies**

- **`catchError`** convertit l'erreur en autre chose : une valeur de repli (`of([])`), une erreur normalisée (`throwError`), ou une redirection.
- **`retry`** relance la requête : **uniquement pour des opérations idempotentes** (jamais un `POST` de paiement) et avec **attente progressive**.
- Traitez les erreurs **globales** (401, 5xx) dans un **intercepteur**, les erreurs **métier** (409, 422) à l'endroit de l'appel.
- Affichez un message utilisateur **compréhensible**, journalisez le détail technique.

### 11.4 Les intercepteurs *(à jour : fonctionnels)*

Un **intercepteur** est une fonction placée **entre l'application et le réseau** : elle voit chaque requête **sortante** et chaque réponse **entrante**, et peut les **modifier**, les **journaliser**, les **mettre en cache**, ou **réagir aux erreurs**. Les requêtes (`HttpRequest`) sont **immuables** : on les **clone**.

```typescript
// src/app/jeton-intercepteur.ts
import { HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';
import { AuthService } from './auth/auth';

export const jetonIntercepteur: HttpInterceptorFn = (requete, suivant) => {
    const jeton = inject(AuthService).jeton();                    // inject() est autorisé ici
    if (!jeton || !requete.url.startsWith('/api')) return suivant(requete);      // ne jamais envoyer le jeton à un tiers
    return suivant(requete.clone({ setHeaders: { Authorization: `Bearer ${jeton}` } }));
};
```

```typescript
// src/app/erreur-intercepteur.ts
import { HttpErrorResponse, HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';
import { Router } from '@angular/router';
import { catchError, throwError } from 'rxjs';

export const erreurIntercepteur: HttpInterceptorFn = (requete, suivant) => {
    const router = inject(Router);
    return suivant(requete).pipe(
        catchError((e: HttpErrorResponse) => {
            if (e.status === 401) router.navigate(['/connexion']);          // session expirée
            return throwError(() => e);
        }),
    );
};
```

```typescript
// src/app/chargement-intercepteur.ts : indicateur de chargement global
import { HttpInterceptorFn } from '@angular/common/http';
import { Injectable, inject, signal, computed } from '@angular/core';
import { finalize } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class Chargement {
    private readonly compteur = signal(0);
    readonly actif = computed(() => this.compteur() > 0);
    demarrer(): void { this.compteur.update((n) => n + 1); }
    terminer(): void { this.compteur.update((n) => Math.max(0, n - 1)); }
}

export const chargementIntercepteur: HttpInterceptorFn = (requete, suivant) => {
    const chargement = inject(Chargement);
    chargement.demarrer();
    return suivant(requete).pipe(finalize(() => chargement.terminer()));     // appelé en cas de succès, d'erreur OU d'annulation
};
```

```typescript
// src/app/cache-intercepteur.ts : cache simple des GET
import { HttpEvent, HttpInterceptorFn, HttpResponse } from '@angular/common/http';
import { Observable, of, tap } from 'rxjs';

const cache = new Map<string, HttpResponse<unknown>>();

export const cacheIntercepteur: HttpInterceptorFn = (requete, suivant): Observable<HttpEvent<unknown>> => {
    if (requete.method !== 'GET') return suivant(requete);
    const enCache = cache.get(requete.urlWithParams);
    if (enCache) return of(enCache.clone());
    return suivant(requete).pipe(tap((evt) => { if (evt instanceof HttpResponse) cache.set(requete.urlWithParams, evt); }));
};
```

**Ordre d'exécution.** Les intercepteurs s'exécutent **dans l'ordre de la liste** à l'aller (requête) et **en ordre inverse** au retour (réponse) : `withInterceptors([a, b, c])` → `a → b → c → réseau → c → b → a`. Placez le jeton avant la gestion d'erreurs.

**`HttpContext`** transmet des **métadonnées par requête** à un intercepteur (ex. : « ne pas afficher l'indicateur de chargement ») :

```typescript
import { HttpContext, HttpContextToken } from '@angular/common/http';

export const SANS_CHARGEMENT = new HttpContextToken<boolean>(() => false);
// this.http.get('/api/ping', { context: new HttpContext().set(SANS_CHARGEMENT, true) });
// Dans l'intercepteur : if (requete.context.get(SANS_CHARGEMENT)) return suivant(requete);
```

*(héritage)* Intercepteurs à base de **classes** (`implements HttpInterceptor`, déclarés avec `HTTP_INTERCEPTORS`) : toujours supportés ; migration vers les fonctions, plus simples.

### 11.5 Progression, téléversement et téléchargement

```typescript
// src/app/televersement.ts
import { Component, inject, signal } from '@angular/core';
import { HttpClient, HttpEventType } from '@angular/common/http';

@Component({
    selector: 'app-televersement',
    template: `<input type="file" (change)="choisir($event)" /> <progress [value]="progression()" max="100"></progress>`,
})
export class Televersement {
    private readonly http = inject(HttpClient);
    protected readonly progression = signal(0);

    protected choisir(e: Event): void {
        const fichier = (e.target as HTMLInputElement).files?.[0];
        if (!fichier) return;
        const donnees = new FormData();
        donnees.append('fichier', fichier);
        this.http.post('/api/fichiers', donnees, { reportProgress: true, observe: 'events' }).subscribe((evt) => {
            if (evt.type === HttpEventType.UploadProgress && evt.total) this.progression.set(Math.round((100 * evt.loaded) / evt.total));
        });
    }
}
```

Pour un **téléchargement**, utilisez `responseType: 'blob'` puis `URL.createObjectURL(blob)`. Ne fixez **pas** vous-même `Content-Type` pour un `FormData` : le navigateur ajoute la bonne valeur avec la frontière (*boundary*).

### 11.6 CORS, proxy et XSRF

- **CORS** (*Cross-Origin Resource Sharing*) : politique du **navigateur** qui bloque les requêtes vers une autre origine (domaine, port, protocole) sauf si le **serveur** les autorise par des en-têtes (`Access-Control-Allow-Origin`…). L'erreur apparaît comme `status: 0`. La correction se fait **côté serveur**.
- **Proxy de développement** : `ng serve --proxy-config proxy.conf.json` redirige `/api` vers le backend et évite CORS en développement :

```json
{ "/api": { "target": "http://localhost:3000", "secure": false, "changeOrigin": true } }
```

- **XSRF / CSRF** : `HttpClient` lit un cookie (`XSRF-TOKEN`) et renvoie sa valeur dans un en-tête (`X-XSRF-TOKEN`) pour les requêtes mutantes vers la même origine ; configurable avec `withXsrfConfiguration()` (chapitre 26).

### 11.7 Tester les appels HTTP

```typescript
// src/app/produit-api.spec.ts
import { TestBed } from '@angular/core/testing';
import { provideHttpClient } from '@angular/common/http';
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { ProduitApi } from './produit-api';

describe('ProduitApi', () => {
    let api: ProduitApi;
    let http: HttpTestingController;

    beforeEach(() => {
        TestBed.configureTestingModule({ providers: [provideHttpClient(), provideHttpClientTesting()] });
        api = TestBed.inject(ProduitApi);
        http = TestBed.inject(HttpTestingController);
    });
    afterEach(() => http.verify());                      // aucune requête non attendue ne doit rester

    it('récupère un produit', () => {
        let resultat: unknown;
        api.obtenir(1).subscribe((p) => (resultat = p));
        const req = http.expectOne('/api/produits/1');
        expect(req.request.method).toBe('GET');
        req.flush({ id: 1, nom: 'Livre', prix: 12 });    // réponse simulée
        expect(resultat).toEqual({ id: 1, nom: 'Livre', prix: 12 });
    });
});
```

### 11.8 Bonnes pratiques

- Un **service par ressource** ; les composants **ne** connaissent **pas** les URL.
- Typer les modèles, centraliser l'URL de base (jeton d'injection, chapitre 7).
- Lectures avec `httpResource` / `toSignal` ; écritures par méthodes explicites déclenchées par des événements.
- Annuler les requêtes obsolètes (`switchMap`, `resource`), éviter les `subscribe` imbriqués.
- Ne jamais mettre de **secret** dans le code client ; ne pas envoyer de jeton à des domaines tiers.
- Avec le **SSR**, activer `withFetch()` ; le **cache de transfert** évite de refaire les mêmes requêtes côté navigateur (chapitre 22).

### Synthèse du chapitre 11

`provideHttpClient(withFetch(), withInterceptors([...]))` active le client. Les méthodes `get/post/put/patch/delete` renvoient des Observables froids, typés par un générique (non vérifié à l'exécution). Les erreurs sont des `HttpErrorResponse` traitées par `catchError` / `retry`. Les **intercepteurs fonctionnels** centralisent jeton, erreurs, chargement et cache. Les tests utilisent `HttpTestingController`.

---

## 12. RxJS et programmation réactive

**Objectifs d'apprentissage.** Comprendre la notion d'**Observable** ; créer, s'abonner, se désabonner ; maîtriser les opérateurs courants (transformation, filtrage, combinaison, aplatissement, erreurs) ; choisir entre `switchMap`, `mergeMap`, `concatMap`, `exhaustMap` ; utiliser les **Subjects** ; éviter les fuites mémoire ; combiner RxJS et signaux.

### 12.1 Pourquoi RxJS ?

**RxJS** (*Reactive Extensions for JavaScript*) est la bibliothèque de **programmation réactive** d'Angular. Elle modélise les **flux de données asynchrones** (clics, saisies, requêtes HTTP, WebSockets, minuteurs) comme des **Observables**, manipulables avec des **opérateurs** composables.

|  | **Promesse** | **Observable** |
| --- | --- | --- |
| Valeurs | **Une** seule | **Zéro, une ou plusieurs**, dans le temps |
| Exécution | **Immédiate** (eager) | **Au `subscribe`** (lazy) |
| Annulation | Non | **Oui** (`unsubscribe`) |
| Opérateurs | `then`, `catch` | **Plus d'une centaine** |
| Multidiffusion | Naturelle (valeur mémorisée) | Par défaut **unicast** (une exécution par abonné) |

Avec l'arrivée des signaux (chapitre 8), la règle est : **signaux pour l'état, RxJS pour les flux** (anti-rebond, annulation, combinaison d'événements).

### 12.2 Vocabulaire

- **Observable** : producteur de valeurs, **inactif** tant que personne ne s'abonne.
- **Observateur** (*observer*) : objet avec `next`, `error`, `complete`.
- **Abonnement** (*Subscription*) : le lien entre un Observable et un observateur ; sert à se **désabonner**.
- **Opérateur** : fonction qui transforme un Observable en un autre ; on les enchaîne dans **`pipe()`**.
- **Subject** : Observable **et** observateur ; permet de **diffuser** des valeurs à plusieurs abonnés.
- **Flux chaud / froid** : un flux *froid* démarre à chaque abonnement (HTTP) ; un flux *chaud* émet indépendamment des abonnés (événements, Subject).

**Contrat** : un Observable émet **0 à N** valeurs via `next`, puis soit `complete`, soit `error` (**terminaux** : plus rien n'est émis ensuite).

### 12.3 Créer et consommer des Observables

```typescript
// src/app/creation.ts
import { Observable, of, from, interval, timer, fromEvent, EMPTY, throwError, defer } from 'rxjs';
import { map, take } from 'rxjs/operators';

const a$ = of(1, 2, 3);                           // émet 1, 2, 3 puis termine
const b$ = from([10, 20, 30]);                   // depuis un tableau, une promesse ou un itérable
const c$ = interval(1000).pipe(take(3));         // 0, 1, 2 (une valeur par seconde) puis termine
const d$ = timer(2000);                          // une émission après 2 s
const e$ = fromEvent<MouseEvent>(document, 'click');   // flux d'événements DOM

// Créer son propre Observable
const personnalise$ = new Observable<string>((observateur) => {
    observateur.next('A');
    const id = setTimeout(() => { observateur.next('B'); observateur.complete(); }, 500);
    return () => clearTimeout(id);               // fonction de NETTOYAGE, appelée au désabonnement
});

const abonnement = personnalise$.subscribe({
    next: (v) => console.log('Valeur :', v),
    error: (e) => console.error('Erreur :', e),
    complete: () => console.log('Terminé'),
});
abonnement.unsubscribe();                        // stoppe le flux et déclenche le nettoyage
```

**Convention.** Les variables contenant un Observable se terminent par **`$`** (`utilisateurs$`).

**Conversion en promesse** : `firstValueFrom(obs$)` (première valeur) ou `lastValueFrom(obs$)` (dernière avant la fin) ; `toPromise()` est supprimé.

### 12.4 Les opérateurs essentiels

```typescript
// src/app/operateurs.ts
import { of, from } from 'rxjs';
import { map, filter, tap, take, distinctUntilChanged, reduce, scan, startWith } from 'rxjs/operators';

from([1, 2, 3, 4, 5, 6]).pipe(
    filter((n) => n % 2 === 0),                // 2, 4, 6
    map((n) => n * 10),                        // 20, 40, 60
    tap((n) => console.log('Passage de', n)),  // effet de bord sans modifier le flux (débogage)
    scan((somme, n) => somme + n, 0),          // cumul progressif : 20, 60, 120
).subscribe(console.log);
```

| Catégorie | Opérateurs | Rôle |
| --- | --- | --- |
| **Transformation** | `map`, `scan`, `reduce`, `pluck` (supprimé) | Transformer les valeurs |
| **Filtrage** | `filter`, `take`, `takeUntil`, `takeWhile`, `skip`, `first`, `last`, `distinctUntilChanged`, `debounceTime`, `throttleTime`, `auditTime` | Choisir lesquelles passent, et quand |
| **Combinaison** | `combineLatest`, `forkJoin`, `merge`, `concat`, `zip`, `withLatestFrom`, `startWith` | Fusionner plusieurs flux |
| **Aplatissement** (flux de flux) | `switchMap`, `mergeMap`, `concatMap`, `exhaustMap` | Enchaîner des opérations asynchrones |
| **Erreurs** | `catchError`, `retry`, `finalize` | Récupérer, relancer, nettoyer |
| **Utilitaires** | `tap`, `delay`, `timeout`, `share`, `shareReplay` | Effets de bord, délais, partage |

#### Les quatre opérateurs d'aplatissement

Quand chaque valeur déclenche **une nouvelle opération asynchrone** (ex. : une requête par saisie), il faut décider **quoi faire des opérations en cours**.

| Opérateur | Comportement | Usage typique |
| --- | --- | --- |
| **`switchMap`** | **Annule** l'opération précédente, garde la plus récente | **Recherche à la saisie**, navigation |
| **`mergeMap`** | Lance toutes **en parallèle** (ordre non garanti) | Envois indépendants |
| **`concatMap`** | Les exécute **l'une après l'autre**, dans l'ordre | Écritures qui doivent rester ordonnées |
| **`exhaustMap`** | **Ignore** les nouvelles tant qu'une opération est en cours | **Bouton de soumission** (anti double-clic), connexion |

```typescript
// src/app/recherche.ts : l'exemple type du switchMap
import { Component, inject } from '@angular/core';
import { FormControl, ReactiveFormsModule } from '@angular/forms';
import { toSignal } from '@angular/core/rxjs-interop';
import { HttpClient } from '@angular/common/http';
import { catchError, debounceTime, distinctUntilChanged, filter, of, switchMap } from 'rxjs';

@Component({
    selector: 'app-recherche',
    imports: [ReactiveFormsModule],
    template: `
        <input [formControl]="terme" placeholder="Rechercher…" />
        <ul>@for (r of resultats(); track r) { <li>{{ r }}</li> }</ul>
    `,
})
export class Recherche {
    private readonly http = inject(HttpClient);
    protected readonly terme = new FormControl('', { nonNullable: true });

    protected readonly resultats = toSignal(
        this.terme.valueChanges.pipe(
            debounceTime(300),                                    // attendre 300 ms d'inactivité
            distinctUntilChanged(),                               // ignorer si identique à la valeur précédente
            filter((t) => t.length >= 2),                         // au moins 2 caractères
            switchMap((t) => this.http.get<string[]>(`/api/recherche?q=${encodeURIComponent(t)}`).pipe(
                catchError(() => of([] as string[])),             // l'erreur est gérée DANS le switchMap pour ne pas tuer le flux
            )),
        ),
        { initialValue: [] as string[] },
    );
}
```

> **Piège classique.** Une erreur **non rattrapée** dans la chaîne principale **termine** le flux : plus aucune saisie ne sera traitée. Placez `catchError` **à l'intérieur** du `switchMap`.

#### Combinaison de flux

```typescript
import { combineLatest, forkJoin, merge, of, map, delay } from 'rxjs';

const utilisateur$ = of({ nom: 'Alice' }).pipe(delay(100));
const commandes$ = of([1, 2, 3]).pipe(delay(200));

// forkJoin : attend la FIN de tous, émet un tableau final (idéal pour plusieurs requêtes HTTP parallèles)
forkJoin({ utilisateur: utilisateur$, commandes: commandes$ }).subscribe(({ utilisateur, commandes }) => console.log(utilisateur, commandes));

// combineLatest : émet à chaque nouvelle valeur d'un flux, avec les dernières valeurs des autres (filtres combinés)
combineLatest([utilisateur$, commandes$]).pipe(map(([u, c]) => `${u.nom} : ${c.length}`)).subscribe(console.log);

// merge : fusionne les émissions de plusieurs flux au fil de l'eau
merge(utilisateur$, commandes$).subscribe(console.log);
```

| Opérateur | Émet… | Usage |
| --- | --- | --- |
| `forkJoin` | Une fois, quand **tous** sont terminés | Plusieurs requêtes HTTP indépendantes |
| `combineLatest` | À chaque changement, avec les **dernières valeurs** de chacun | Filtres, état dérivé |
| `merge` | Toute valeur de **n'importe quel** flux | Plusieurs sources d'événements |
| `zip` | Par **paires** alignées (1re avec 1re…) | Rare |
| `withLatestFrom` | Valeur du flux principal + dernière de l'autre | Lire un état au moment d'un événement |
| `concat` | Un flux **après** l'autre | Séquences ordonnées |

### 12.5 Subjects : diffuser des valeurs

Un **Subject** est à la fois Observable et observateur : on peut y **pousser** des valeurs (`next`) que **plusieurs** abonnés reçoivent (**multidiffusion**).

| Type | Comportement à l'abonnement |
| --- | --- |
| `Subject` | Ne rejoue **rien** : l'abonné ne reçoit que les valeurs futures |
| `BehaviorSubject` | Possède une **valeur courante** (initiale obligatoire) et la donne immédiatement aux nouveaux abonnés ; `.value` la lit |
| `ReplaySubject(n)` | Rejoue les **n dernières** valeurs |
| `AsyncSubject` | Émet la **dernière** valeur à la complétion |

```typescript
// src/app/notifications.ts
import { Injectable } from '@angular/core';
import { BehaviorSubject, Subject } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class Notifications {
    private readonly _message$ = new Subject<string>();                    // événements ponctuels
    readonly message$ = this._message$.asObservable();                    // expose en lecture seule : ne pas laisser les consommateurs appeler next()

    private readonly _utilisateur$ = new BehaviorSubject<string | null>(null);   // état courant
    readonly utilisateur$ = this._utilisateur$.asObservable();

    notifier(texte: string): void { this._message$.next(texte); }
    connecter(nom: string): void { this._utilisateur$.next(nom); }
}
```

> **En 2026**, pour **l'état**, préférez un **signal** (`signal` + `computed`) à un `BehaviorSubject` : plus simple, sans abonnement. Gardez les `Subject` pour des **événements** (bus de messages, flux d'actions).

**Partage d'une exécution.** `share()` et `shareReplay({ bufferSize: 1, refCount: true })` partagent **une seule** exécution entre plusieurs abonnés (évite deux requêtes HTTP identiques). Pensez à `refCount: true` pour libérer la source quand plus personne n'écoute.

### 12.6 Se désabonner : éviter les fuites mémoire

Un abonnement à un flux **infini** (`interval`, `fromEvent`, `valueChanges`, un Subject) qui n'est jamais fermé **continue de s'exécuter** après la destruction du composant : fuite mémoire et comportements fantômes.

| Technique | Quand | Remarque |
| --- | --- | --- |
| **Tube `async`** / **`toSignal()`** | Affichage dans le gabarit | **Automatique** ; à privilégier |
| **`takeUntilDestroyed()`** | `subscribe` manuel dans un composant, directive ou service | Se désabonne à la destruction |
| `take(1)` / `first()` | Flux dont on n'attend qu'une valeur |  |
| `takeUntil(notificateur$)` | Désabonnement piloté par un événement | Pattern *(héritage)* avec `ngOnDestroy` |
| `subscription.unsubscribe()` | Gestion manuelle | Risque d'oubli |

```typescript
// src/app/abonnement-propre.ts
import { Component, DestroyRef, inject } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { interval } from 'rxjs';

@Component({ selector: 'app-abonnement-propre', template: `<p>Voir la console</p>` })
export class AbonnementPropre {
    constructor() {
        // Dans un contexte d'injection (constructeur, champ) : aucun argument
        interval(1000).pipe(takeUntilDestroyed()).subscribe((n) => console.log('tic', n));
    }

    demarrerPlusTard(): void {
        // Hors contexte d'injection : passer un DestroyRef
        const destroyRef = inject(DestroyRef);             // à capturer dans le constructeur / champ en vrai code
        interval(1000).pipe(takeUntilDestroyed(destroyRef)).subscribe();
    }
}
```

> `HttpClient` **termine** son Observable après la réponse : pas de fuite, mais une requête en cours n'est annulée que si on se désabonne.

### 12.7 Erreurs

```typescript
import { of, throwError, catchError, retry, timer } from 'rxjs';

throwError(() => new Error('Échec')).pipe(
    retry({ count: 3, delay: (_e, n) => timer(2 ** n * 200) }),       // tentatives avec délai exponentiel
    catchError((e) => of('valeur de repli')),                          // remplace l'erreur par une valeur
).subscribe(console.log);
```

- Une erreur **termine** l'Observable (sauf si `catchError` la rattrape et renvoie un autre flux).
- `catchError(e => throwError(() => e))` relance ; renvoyer `EMPTY` termine silencieusement.
- `finalize(() => …)` s'exécute **toujours** (succès, erreur, désabonnement).
- Toujours fournir un gestionnaire `error` à `subscribe` pour les flux susceptibles d'échouer.

### 12.8 Tester des Observables

```typescript
// src/app/flux.spec.ts
import { of } from 'rxjs';
import { map } from 'rxjs/operators';
import { TestScheduler } from 'rxjs/testing';

describe('flux', () => {
    it('double les valeurs (marble testing)', () => {
        const planificateur = new TestScheduler((actuel, attendu) => expect(actuel).toEqual(attendu));
        planificateur.run(({ cold, expectObservable }) => {
            const source$ = cold('a-b-c|', { a: 1, b: 2, c: 3 });
            expectObservable(source$.pipe(map((n) => n * 2))).toBe('a-b-c|', { a: 2, b: 4, c: 6 });
        });
    });

    it('flux synchrone simple', () => {
        const valeurs: number[] = [];
        of(1, 2, 3).pipe(map((n) => n + 1)).subscribe((v) => valeurs.push(v));
        expect(valeurs).toEqual([2, 3, 4]);
    });
});
```

Les **diagrammes à billes** (*marble diagrams*) décrivent le temps par des caractères : `-` (une unité), `a`, `b` (valeurs), `|` (fin), `#` (erreur). Les tests de composants utilisent plutôt des flux synchrones (`of`) et `fakeAsync` (chapitre 16).

### 12.9 Anti-patterns à éviter

- **`subscribe` imbriqués** : utilisez un opérateur d'aplatissement.
- **`subscribe` dans `subscribe`** pour « récupérer » une valeur : composez avec `switchMap` / `combineLatest`.
- **Oublier de se désabonner** d'un flux infini.
- **Exposer un `Subject`** directement : exposez `asObservable()`.
- **`BehaviorSubject` pour tout l'état** : préférez les signaux.
- Mettre de la **logique métier** dans `subscribe` : mettez-la dans le pipeline, `subscribe` ne fait que « consommer ».
- **`mergeMap` pour une recherche** : provoque des réponses dans le désordre ; utilisez `switchMap`.

### Synthèse du chapitre 12

Un **Observable** est un flux **paresseux**, annulable, de 0 à N valeurs. On le transforme avec des **opérateurs** dans `pipe()`. Retenez les quatre aplatisseurs (`switchMap` / `mergeMap` / `concatMap` / `exhaustMap`), les combinateurs (`forkJoin`, `combineLatest`, `merge`), les **Subjects** pour diffuser, et **toujours** gérer le désabonnement (`async`, `toSignal`, `takeUntilDestroyed`). Les signaux gèrent l'état ; RxJS gère le temps et les flux.

---

## 13. Gestion d'état

**Objectifs d'apprentissage.** Définir ce qu'est l'**état** d'une application et ses différentes natures ; choisir le bon niveau de solution ; construire un **store à base de service et de signaux** ; comprendre l'architecture **NgRx** (actions, réducteurs, sélecteurs, effets) ; utiliser **NgRx SignalStore** ; comparer les options et éviter la sur-ingénierie.

### 13.1 Qu'est-ce que l'état, et quand faut-il un état global ?

L'**état** (*state*) est l'ensemble des données dont dépend ce que l'utilisateur voit à un instant donné : utilisateur connecté, contenu d'un panier, filtres, résultats de recherche, éléments chargés depuis l'API, étape d'un assistant. Gérer l'état, c'est décider **où** ces données vivent, **qui** peut les modifier, et **comment** les composants sont prévenus d'un changement.

**Les natures d'état**

| Nature | Exemples | Où la placer |
| --- | --- | --- |
| **Local à un composant** | Menu ouvert, onglet actif, valeur d'un champ | `signal()` dans le composant |
| **Partagé** entre quelques composants | Panier, thème, utilisateur courant | **Service** avec signaux |
| **Global et complexe** | État traçable par de nombreuses fonctionnalités, règles strictes | **NgRx** (Store ou SignalStore) |
| **Serveur** (copie locale de données distantes) | Liste de produits, profil | `resource` / `httpResource` ou bibliothèque de requêtes |
| **URL** | Page, filtres partageables, identifiants | **Routeur** (paramètres de chemin / de requête) |
| **Formulaire** | Saisie en cours, erreurs | API de formulaires (chapitre 10) |

> **Principe directeur.** Gardez l'état **aussi local que possible** et ne le « remontez » que lorsque plusieurs consommateurs en ont besoin. L'état **serveur** (cache de données) n'a pas les mêmes problèmes que l'état **client** (invalidation, rechargement, erreurs) : traitez-les séparément.

**Qualités attendues d'un bon store** : **source de vérité unique** pour chaque donnée, **mises à jour immuables**, **lecture seule** pour les consommateurs, **valeurs dérivées calculées** (jamais dupliquées), **flux unidirectionnel** (action → modification → notification).

### 13.2 Service avec signaux *(recommandé par défaut)*

Un service `providedIn: 'root'` qui encapsule un ou plusieurs signaux suffit dans la **majorité** des applications.

```typescript
// src/app/article.ts
export interface Article { id: number; nom: string; prix: number; quantite: number; }
```

```typescript
// src/app/panier.store.ts
import { Injectable, computed, signal } from '@angular/core';
import { Article } from './article';

@Injectable({ providedIn: 'root' })
export class PanierStore {
    private readonly _articles = signal<Article[]>([]);

    // Lecture seule pour les consommateurs
    readonly articles = this._articles.asReadonly();
    // Valeurs dérivées : calculées, mémoïsées, jamais stockées
    readonly nombre = computed(() => this._articles().length);
    readonly total = computed(() => this._articles().reduce((s, a) => s + a.prix * a.quantite, 0));

    // Seules ces méthodes modifient l'état
    ajouter(article: Article): void {
        this._articles.update((liste) => [...liste, article]);
    }
    retirer(id: number): void {
        this._articles.update((liste) => liste.filter((a) => a.id !== id));
    }
    vider(): void { this._articles.set([]); }
}
```

```typescript
// src/app/panier-vue.ts
import { Component, inject } from '@angular/core';
import { PanierStore } from './panier.store';

@Component({
    selector: 'app-panier-vue',
    template: `
        <p>{{ store.nombre() }} article(s) — total : {{ store.total() }} €</p>
        @for (a of store.articles(); track a.id) {
            <p>{{ a.nom }} <button (click)="store.retirer(a.id)">Retirer</button></p>
        }
    `,
})
export class PanierVue {
    protected readonly store = inject(PanierStore);
}
```

#### Modéliser aussi le chargement et l'erreur

Un état « asynchrone » a au moins quatre cas : *non chargé*, *en chargement*, *réussi*, *en erreur*. Modélisez-les par une **union discriminée** plutôt que par des booléens indépendants (qui permettent des combinaisons impossibles comme « chargement ET erreur »).

```typescript
// src/app/produits.store.ts
import { Injectable, computed, inject, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { firstValueFrom } from 'rxjs';

export interface Produit { id: number; nom: string; }

type EtatProduits =
    | { statut: 'inactif' }
    | { statut: 'chargement' }
    | { statut: 'succes'; produits: Produit[] }
    | { statut: 'erreur'; message: string };

@Injectable({ providedIn: 'root' })
export class ProduitsStore {
    private readonly http = inject(HttpClient);
    private readonly etat = signal<EtatProduits>({ statut: 'inactif' });

    readonly statut = computed(() => this.etat().statut);
    readonly produits = computed(() => {
        const e = this.etat();
        return e.statut === 'succes' ? e.produits : [];
    });
    readonly erreur = computed(() => {
        const e = this.etat();
        return e.statut === 'erreur' ? e.message : null;
    });

    async charger(): Promise<void> {
        this.etat.set({ statut: 'chargement' });
        try {
            const produits = await firstValueFrom(this.http.get<Produit[]>('/api/produits'));
            this.etat.set({ statut: 'succes', produits });
        } catch {
            this.etat.set({ statut: 'erreur', message: 'Impossible de charger les produits' });
        }
    }
}
```

**Modèle de mise à jour optimiste.** Pour une interface réactive, on applique d'abord le changement **localement**, puis on envoie la requête ; si elle échoue, on **restaure** l'état précédent (copie conservée avant la modification) et on prévient l'utilisateur.

**Persistance.** Pour sauvegarder l'état (panier, préférences), utilisez un `effect()` qui écrit dans `localStorage` — en protégeant l'accès pour le SSR (chapitre 22) — et restaurez la valeur à l'initialisation.

### 13.3 NgRx : le Store

**NgRx** est la bibliothèque de gestion d'état de référence dans l'écosystème Angular, inspirée de **Redux**. Elle impose une **architecture stricte** qui rend les changements **traçables et testables**.

**Les concepts**

| Concept | Rôle |
| --- | --- |
| **Store** | Conteneur **unique** et **immuable** de l'état de l'application |
| **Action** | Objet décrivant **ce qui s'est passé** (`[Panier] Ajouter article`) ; seul moyen de provoquer un changement |
| **Réducteur** (*reducer*) | Fonction **pure** `(état, action) → nouvel état` |
| **Sélecteur** (*selector*) | Fonction **pure** qui **extrait** et **dérive** une portion de l'état ; mémoïsé |
| **Effet** (*effect*) | Gère les **effets de bord** (HTTP, navigation) en réagissant aux actions et en émettant de nouvelles actions |
| **Outils de développement** | Historique des actions, **voyage dans le temps**, inspection de l'état |

**Flux unidirectionnel :** composant → `dispatch(action)` → réducteur → nouvel état → sélecteurs → composants. Les effets s'insèrent entre l'action et le résultat pour les opérations asynchrones.

```bash
ng add @ngrx/store
ng add @ngrx/effects
ng add @ngrx/store-devtools
```

```typescript
// src/app/panier.state.ts
import { createActionGroup, props, emptyProps, createFeature, createReducer, on, createSelector } from '@ngrx/store';
import { Article } from './article';

export const PanierActions = createActionGroup({
    source: 'Panier',
    events: {
        'Ajouter article': props<{ article: Article }>(),
        'Retirer article': props<{ id: number }>(),
        'Vider': emptyProps(),
        'Charger': emptyProps(),
        'Chargement reussi': props<{ articles: Article[] }>(),
        'Chargement echoue': props<{ erreur: string }>(),
    },
});

interface EtatPanier { articles: Article[] }
const initial: EtatPanier = { articles: [] };

export const panierFeature = createFeature({
    name: 'panier',
    reducer: createReducer(
        initial,
        on(PanierActions.ajouterArticle, (etat, { article }) => ({ ...etat, articles: [...etat.articles, article] })),
        on(PanierActions.retirerArticle, (etat, { id }) => ({ ...etat, articles: etat.articles.filter((a) => a.id !== id) })),
        on(PanierActions.chargementReussi, (etat, { articles }) => ({ ...etat, articles })),
        on(PanierActions.vider, () => initial),
    ),
    extraSelectors: ({ selectArticles }) => ({
        selectTotal: createSelector(selectArticles, (a) => a.reduce((s, x) => s + x.prix * x.quantite, 0)),
    }),
});
```

- **`createActionGroup`** produit un groupe d'actions typées : l'événement `'Ajouter article'` devient la fonction `ajouterArticle(...)` (nom en *camelCase*).
- **`createFeature`** génère automatiquement le **nom** de la tranche d'état, son **réducteur** et des **sélecteurs** de base (`selectArticles`, `selectPanierState`…) ; `extraSelectors` en ajoute de dérivés.
- **Les réducteurs doivent être purs et immuables** : pas d'appel HTTP, pas de date aléatoire, pas de mutation (`etat.articles.push(...)` est interdit).

```typescript
// src/app/app.config.ts
import { ApplicationConfig } from '@angular/core';
import { provideStore } from '@ngrx/store';
import { provideEffects } from '@ngrx/effects';
import { provideStoreDevtools } from '@ngrx/store-devtools';
import { panierFeature } from './panier.state';
import { chargerArticles } from './panier.effects';

export const appConfig: ApplicationConfig = {
    providers: [
        provideStore({ [panierFeature.name]: panierFeature.reducer }),
        provideEffects({ chargerArticles }),
        provideStoreDevtools({ maxAge: 25 }),            // conserve 25 actions dans l'historique
    ],
};
```

```typescript
// src/app/panier-ngrx.ts
import { Component, inject } from '@angular/core';
import { Store } from '@ngrx/store';
import { Article } from './article';
import { PanierActions, panierFeature } from './panier.state';

@Component({
    selector: 'app-panier-ngrx',
    template: `
        <p>Total : {{ total() }}</p>
        <button (click)="ajouter({ id: 1, nom: 'Livre', prix: 12.5, quantite: 1 })">Ajouter un livre</button>
    `,
})
export class PanierNgrx {
    private readonly store = inject(Store);
    protected readonly total = this.store.selectSignal(panierFeature.selectTotal);       // sélecteur sous forme de signal

    protected ajouter(a: Article): void {
        this.store.dispatch(PanierActions.ajouterArticle({ article: a }));
    }
}
```

Pour une **tranche d'état propre à une route** (chargée paresseusement), on déclare `provideState(panierFeature)` dans les `providers` de la route.

#### Effets : actions asynchrones

Un **effet** écoute le flux d'actions (`Actions`), filtre avec `ofType`, effectue l'opération asynchrone, puis **émet une nouvelle action** (succès ou échec). Le choix de l'opérateur d'aplatissement (chapitre 12) compte : `exhaustMap` ignore les nouvelles demandes pendant un chargement, `switchMap` annule la précédente.

```typescript
// src/app/article.service.ts
import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Article } from './article';

@Injectable({ providedIn: 'root' })
export class ArticleService {
    private readonly http = inject(HttpClient);
    lister(): Observable<Article[]> { return this.http.get<Article[]>('/api/articles'); }
}
```

```typescript
// src/app/panier.effects.ts
import { inject } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { catchError, exhaustMap, map, of } from 'rxjs';
import { ArticleService } from './article.service';
import { PanierActions } from './panier.state';

export const chargerArticles = createEffect(
    (actions$ = inject(Actions), service = inject(ArticleService)) =>
        actions$.pipe(
            ofType(PanierActions.charger),
            exhaustMap(() => service.lister().pipe(
                map((articles) => PanierActions.chargementReussi({ articles })),
                catchError((erreur) => of(PanierActions.chargementEchoue({ erreur: String(erreur) }))),   // l'erreur est gérée DANS le flux interne
            )),
        ),
    { functional: true },
);
```

**Autres éléments de l'écosystème** : `@ngrx/entity` (gestion normalisée de collections avec `createEntityAdapter`), `@ngrx/router-store` (synchronise le routeur avec le store), *meta-reducers* (journalisation, persistance), vérifications d'immuabilité en développement, et tests des réducteurs et sélecteurs comme de simples fonctions pures.

**Bonnes pratiques NgRx**

- Nommer les actions d'après **l'événement** (« Article ajouté »), pas la **commande** (« Mettre à jour la liste »).
- Ne mettre dans le store que l'état **réellement partagé** ; ne pas y placer l'état d'un seul composant.
- **Ne pas dupliquer** de données dérivées : les calculer par sélecteur.
- Découper l'état en **tranches par fonctionnalité** (*feature states*).

### 13.4 NgRx SignalStore *(à jour)*

**SignalStore** (`@ngrx/signals`) est une version **plus légère**, entièrement construite sur les signaux, sans actions ni réducteurs explicites. Un store se **compose** de fonctionnalités (`withState`, `withComputed`, `withMethods`, `withHooks`…).

```typescript
// src/app/panier.signal-store.ts
import { computed, inject } from '@angular/core';
import { signalStore, withState, withComputed, withMethods, patchState } from '@ngrx/signals';
import { firstValueFrom } from 'rxjs';
import { Article } from './article';
import { ArticleService } from './article.service';

export const PanierSignalStore = signalStore(
    { providedIn: 'root' },
    withState({ articles: [] as Article[], chargement: false }),
    withComputed(({ articles }) => ({
        total: computed(() => articles().reduce((s, a) => s + a.prix * a.quantite, 0)),
    })),
    withMethods((store, service = inject(ArticleService)) => ({
        ajouter: (article: Article) => patchState(store, (e) => ({ articles: [...e.articles, article] })),
        async charger() {
            patchState(store, { chargement: true });
            patchState(store, { articles: await firstValueFrom(service.lister()), chargement: false });
        },
    })),
);
```

```typescript
// src/app/panier-signal-store-vue.ts
import { Component, inject } from '@angular/core';
import { PanierSignalStore } from './panier.signal-store';

@Component({
    selector: 'app-panier-signal-store',
    template: `
        <button (click)="store.charger()">Charger</button>
        @if (store.chargement()) { <p>Chargement…</p> }
        <p>Total : {{ store.total() }}</p>
    `,
})
export class PanierSignalStoreVue {
    protected readonly store = inject(PanierSignalStore);
}
```

**Fonctionnement**

- **`withState`** déclare l'état initial ; **chaque propriété** de l'état devient automatiquement un **signal** du store (`store.articles()`, `store.chargement()`).
- **`withComputed`** ajoute des valeurs dérivées ; **`withMethods`** ajoute les opérations (qui peuvent `inject()` des services).
- **`patchState(store, …)`** est la **seule** façon de modifier l'état : l'état n'est **pas modifiable** de l'extérieur.
- Le store est un **service** : fourni à la racine (`providedIn: 'root'`) ou **dans un composant / une route** (`providers: [PanierSignalStore]`) pour un état à **durée de vie limitée**.
- Des **extensions** officielles complètent le noyau (gestion d'entités normalisées, méthodes réactives intégrant RxJS pour les appels HTTP, hooks d'initialisation et de destruction, outils de développement) : consultez la documentation de `@ngrx/signals` pour les noms exacts de votre version.

### 13.5 Autres solutions

| Outil | Remarques |
| --- | --- |
| **NgRx Store** | Standard des grandes applications, très structuré, plus de code |
| **NgRx SignalStore** | Moderne, léger, API simple |
| **NGXS** | Approche à décorateurs, moins de code répétitif |
| **Akita** | **Plus maintenu** : à éviter pour de nouveaux projets |
| **Elf** | Bibliothèque réactive légère |
| **Service + signaux** | **Suffisant pour la plupart des applications** |

### 13.6 Comparaison et critères de choix

| Critère | Service + signaux | NgRx Store | NgRx SignalStore |
| --- | --- | --- | --- |
| Complexité | Faible | Élevée | Moyenne |
| Traçabilité (devtools) | Non | Oui | Oui (avec extensions) |
| Quantité de code | Faible | Élevée | Moyenne |
| Équipes nombreuses / règles strictes | Moyen | Adapté | Adapté |

**Questions à se poser** : plusieurs équipes touchent-elles au même état ? A-t-on besoin d'un **historique** des changements (audit, débogage) ? Les règles de modification sont-elles complexes ? Si la réponse est « non » partout, un **service avec signaux** suffit.

> **Commencez simple** (service + signaux). N'ajoutez NgRx que si la complexité de l'état l'exige : la migration d'un service à un store reste aisée si les composants ne dépendent que d'**API de lecture et de méthodes**.

### Synthèse du chapitre 13

Distinguez l'état **local**, **partagé**, **global**, **serveur**, d'**URL** et de **formulaire**. Par défaut : **service + signaux** (état privé, lecture seule exposée, valeurs dérivées par `computed`, union discriminée pour le chargement). **NgRx Store** apporte actions, réducteurs purs, sélecteurs, effets et traçabilité pour les grandes équipes ; **SignalStore** en offre une version légère. Ne complexifiez pas sans besoin.

---

## 14. Animations

**Objectifs d'apprentissage.** Animer l'entrée et la sortie d'éléments avec les liaisons CSS natives `animate.enter` / `animate.leave` ; utiliser transitions, `@keyframes` et View Transitions ; respecter `prefers-reduced-motion` ; lire et migrer du code utilisant `@angular/animations`.

### 14.1 Animations CSS natives *(à jour)*

Depuis la **version 20.2**, Angular propose des liaisons natives d'entrée et de sortie d'éléments basées sur le **CSS** : **`animate.enter`** et **`animate.leave`**. Le paquet **`@angular/animations`** (langage `trigger`, `state`, `transition`) est **déprécié** au profit de cette approche, plus simple, plus légère (aucun paquet ni fournisseur supplémentaire) et qui profite de l'accélération matérielle du navigateur.

**Principe.** Quand un élément est **ajouté** au DOM (par `@if`, `@for`…), Angular lui applique la ou les classes CSS indiquées dans `animate.enter`. Quand il est **retiré**, Angular applique les classes de `animate.leave` et **attend la fin de l'animation** avant de supprimer réellement l'élément (ce qu'une simple classe ne permettrait pas, car l'élément disparaîtrait immédiatement).

```typescript
// src/app/notification-vue.ts
import { Component, signal } from '@angular/core';

@Component({
    selector: 'app-notification',
    template: `
        @if (visible()) {
            <div class="notif" animate.enter="entree" animate.leave="sortie">Enregistré !</div>
        }
        <button (click)="visible.update((v) => !v)">Basculer</button>
    `,
    styles: `
        .notif { padding: 1rem; background: #e6ffed; }
        .entree { animation: apparition 300ms ease-out; }
        .sortie { animation: disparition 300ms ease-in; }
        @keyframes apparition { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: none; } }
        @keyframes disparition { to { opacity: 0; transform: translateY(-10px); } }
    `,
})
export class NotificationVue {
    protected readonly visible = signal(true);
}
```

**Autres outils CSS**

- **Transitions** : `transition: transform .3s ease, opacity .3s ease;` pour animer le passage d'un état à un autre (classe basculée par une liaison `[class.ouvert]`).
- **`@keyframes`** : animations plus riches en plusieurs étapes.
- **View Transitions** du routeur : `withViewTransitions()` (chapitre 9) anime le passage d'une page à l'autre via l'API du navigateur.
- **`prefers-reduced-motion`** : respecte la préférence système des personnes sensibles au mouvement.

```css
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}
```

**Exemple de transition pilotée par un signal :**

```typescript
// src/app/accordeon.ts
import { Component, signal } from '@angular/core';

@Component({
    selector: 'app-accordeon',
    template: `
        <button [attr.aria-expanded]="ouvert()" (click)="ouvert.update((o) => !o)">Détails</button>
        <div class="contenu" [class.ouvert]="ouvert()"><div>Texte caché puis révélé</div></div>
    `,
    styles: `
        .contenu { display: grid; grid-template-rows: 0fr; transition: grid-template-rows 250ms ease; }
        .contenu.ouvert { grid-template-rows: 1fr; }
        .contenu > div { overflow: hidden; }
    `,
})
export class Accordeon {
    protected readonly ouvert = signal(false);
}
```

(Astuce : la transition `grid-template-rows` de `0fr` à `1fr` anime une hauteur automatique sans animer `height`.)

### 14.2 `@angular/animations` *(héritage)*

Encore présent dans de nombreux projets (et dans Angular Material jusqu'à sa migration). Il repose sur un **langage dédié** déclaré dans la propriété `animations` du composant.

```typescript
// src/app/boite.ts
import { Component, signal } from '@angular/core';
import { trigger, state, style, transition, animate } from '@angular/animations';

@Component({
    selector: 'app-boite',
    animations: [
        trigger('ouverture', [
            state('ferme', style({ height: '0', opacity: 0 })),
            state('ouvert', style({ height: '*', opacity: 1 })),
            transition('ferme <=> ouvert', animate('300ms ease-in-out')),
            transition(':enter', [style({ opacity: 0 }), animate('200ms', style({ opacity: 1 }))]),
            transition(':leave', [animate('200ms', style({ opacity: 0 }))]),
        ]),
    ],
    template: `
        <button (click)="ouvert.update((o) => !o)">Basculer</button>
        <div [@ouverture]="ouvert() ? 'ouvert' : 'ferme'">Contenu</div>
    `,
})
export class Boite {
    protected readonly ouvert = signal(false);
}
```

Fournisseur à ajouter dans la configuration de l'application :

```typescript
// src/app/app.config.ts
import { ApplicationConfig } from '@angular/core';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';

export const appConfig: ApplicationConfig = {
    providers: [provideAnimationsAsync()],      // charge le code d'animation à la demande
};
```

**Vocabulaire** : un **déclencheur** (`trigger`) est lié à une propriété (`[@ouverture]`) ; un **état** (`state`) associe un nom à des styles ; une **transition** (`transition('a => b', …)`) décrit le passage d'un état à l'autre ; `:enter` / `:leave` désignent l'ajout / le retrait (alias de `void => *` et `* => void`) ; `animate('300ms ease-in-out')` définit durée et courbe ; `keyframes`, `query`, `stagger`, `group` et `sequence` composent des animations complexes ; les callbacks `(@ouverture.done)` et `(@ouverture.start)` signalent le début et la fin.

**Migration.** Remplacez progressivement `trigger` / `transition` par des classes CSS et `animate.enter` / `animate.leave` ; consultez le guide de migration d'angular.dev pour les équivalences. Tant que vous utilisez Angular Material avec ses anciennes animations, le fournisseur reste nécessaire.

### 14.3 Bonnes pratiques

- Privilégiez les animations **CSS** et les propriétés **`transform` / `opacity`** (accélérées par le GPU, sans recalcul de mise en page).
- Respectez **`prefers-reduced-motion`**.
- Évitez d'animer `width`, `height`, `top`, `left` (reflux de mise en page).
- Gardez des durées **courtes** (150–400 ms) ; l'animation doit **aider** à comprendre, non retarder l'action.
- Une animation ne doit **jamais** être le seul moyen de transmettre une information (accessibilité).
- Testez sur des appareils modestes : une animation fluide sur un poste de développement peut saccader sur mobile.

### Synthèse du chapitre 14

`animate.enter` / `animate.leave` + CSS (transitions, `@keyframes`) sont la voie **actuelle** ; `@angular/animations` est **déprécié** mais courant. Animer `transform` et `opacity`, durées courtes, respecter `prefers-reduced-motion`.

---

## 15. Bibliothèques et espaces de travail

**Objectifs d'apprentissage.** Créer, structurer, construire et publier une **bibliothèque Angular** ; définir son **API publique** ; appliquer les bonnes pratiques de conception de bibliothèque ; organiser un **espace de travail multi-projets** ou un **monorepo** (Angular CLI, Nx, pnpm, Turborepo).

### 15.1 Créer une bibliothèque Angular

Une **bibliothèque** regroupe des composants, directives, tubes et services **réutilisables** entre plusieurs applications ; elle est compilée avec **ng-packagr** au **format de paquet Angular** (APF), consommable par n'importe quel projet Angular.

```bash
ng new mon-espace --create-application=false      # espace de travail sans application
cd mon-espace
ng generate library ui-kit                        # projects/ui-kit
ng generate application demo                      # application de démonstration
```

```text
projects/ui-kit/
├── src/
│   ├── lib/
│   │   ├── bouton/bouton.ts
│   │   └── ui-kit.ts
│   └── public-api.ts            ← ce que la bibliothèque EXPOSE
├── ng-package.json              ← configuration de ng-packagr (point d'entrée, destination)
└── package.json                 ← métadonnées du paquet publié
```

```typescript
// projects/ui-kit/src/public-api.ts
export * from './lib/bouton/bouton';
```

```typescript
// projects/ui-kit/src/lib/bouton/bouton.ts : composant autonome de bibliothèque
import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
    selector: 'kit-bouton',
    template: `<button><ng-content /></button>`,
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class KitBouton {}
```

**Le fichier `public-api.ts`** est la **frontière** de la bibliothèque : **seul ce qui y est exporté** est accessible aux utilisateurs. Tout le reste est un détail d'implémentation que l'on peut modifier sans rupture.

**`package.json` d'une bibliothèque** : le nom du paquet, la version, et surtout les **`peerDependencies`** (ex. `@angular/core`, `@angular/common` avec une plage de versions) pour que l'application hôte fournisse **une seule** copie d'Angular ; les `dependencies` sont réservées à ce que la bibliothèque embarque réellement.

```json
{
  "name": "@mon-espace/ui-kit",
  "version": "1.0.0",
  "peerDependencies": { "@angular/common": "^22.0.0", "@angular/core": "^22.0.0" },
  "dependencies": { "tslib": "^2.3.0" },
  "sideEffects": false
}
```

`"sideEffects": false` permet l'élagage (*tree-shaking*) efficace du code non utilisé par les applications.

**Points d'entrée secondaires.** Pour permettre des imports séparés (`@mon-espace/ui-kit/bouton`) et réduire le code chargé, on crée des **points d'entrée secondaires** (dossiers avec leur propre `ng-package.json` et `public-api.ts`).

```bash
ng build ui-kit                                  # produit dist/ui-kit
cd dist/ui-kit && npm publish                    # publier sur npm (registre public ou privé)
```

> **Astuce.** En développement, le chemin `@mon-espace/ui-kit` est mappé sur le code source via `paths` dans `tsconfig.json`, ou sur le dossier `dist/`. Pensez à **construire la bibliothèque avant l'application**, ou à utiliser `ng build ui-kit --watch` pendant le travail.

### 15.2 Bonnes pratiques de bibliothèque

- **Composants autonomes** (pas de `NgModule`) ; exposer une API **minimale** et **stable**.
- Utiliser `input()` / `output()`, **`OnPush`**, des fonctions `provideXxx()` pour la configuration (par ex. `provideKit({ theme: 'sombre' })`).
- **Versionnement sémantique** : les changements incompatibles n'arrivent qu'avec une version **majeure** ; aligner les versions majeures sur celles d'Angular facilite la compréhension.
- **Préfixe de sélecteurs** propre à la bibliothèque (`kit-`) pour éviter les collisions.
- **`peerDependencies`** sur `@angular/core` ; ne pas importer d'APIs **privées** d'Angular.
- Compatible **SSR** : pas d'accès direct à `window` / `document` sans protection (chapitre 22).
- Accessible (clavier, ARIA), thémable par **variables CSS**.
- **Documenter** (Storybook, Compodoc), **tester** (chapitre 16), fournir un **journal des modifications**.

### 15.3 Espaces de travail multi-projets et monorepos

Un **espace de travail** Angular (*workspace*) peut contenir plusieurs **applications** et **bibliothèques** (`projects/`) avec un seul `angular.json` et un seul `node_modules`. Pour les très grands dépôts, des outils complémentaires s'imposent :

| Outil | Apport |
| --- | --- |
| **Angular CLI** (multi-projets) | Simple, intégré |
| **Nx** | **Cache de calcul**, `nx affected`, générateurs, règles de dépendances (`enforce-module-boundaries`), graphe de projets |
| **pnpm workspaces**, **Turborepo** | Gestion des paquets, tâches orchestrées |

```bash
npx create-nx-workspace@latest mon-monorepo --preset=angular-monorepo
nx serve app-web
nx affected -t lint test build                   # ne traite que ce qui a changé
nx graph                                         # visualiser les dépendances
```

**Avantages d'un monorepo** : partage de code sans publication, refactorisations transversales atomiques, outils et versions uniformes, cohérence des mises à jour. **Inconvénients** : temps de build qui augmentent (d'où le cache et `affected`), besoin de règles de **frontières** entre modules (qui peut importer quoi), droits d'accès plus délicats.

**Organisation recommandée** : `apps/` (applications), `libs/` (bibliothèques regroupées par domaine fonctionnel et par type : *feature*, *ui*, *data-access*, *util*), et des règles qui interdisent à une bibliothèque d'*ui* de dépendre d'une bibliothèque de *feature*. Voir la section 28 pour l'ajout de Nx à un projet existant.

### Synthèse du chapitre 15

Une bibliothèque Angular = composants autonomes + **`public-api.ts`** + `ng-package.json`, construite par **ng-packagr**, publiée via `npm`. Concevez une **API minimale et stable**, avec `peerDependencies`, `OnPush`, `provideXxx()`, compatibilité SSR et accessibilité. Les **monorepos** (CLI, **Nx**, pnpm, Turborepo) partagent le code ; Nx apporte cache, `affected` et règles de frontières.

---

# Partie III — Tests

## 16. Tests unitaires

**Objectifs d'apprentissage.** Comprendre la place des tests unitaires dans la **pyramide de tests** ; utiliser **Vitest** et **`TestBed`** ; tester composants (entrées signaux, événements, sorties), services, appels HTTP, gardes, intercepteurs, signaux et effets ; utiliser **doublures** et **harnais de composants** ; mesurer la couverture et appliquer les bonnes pratiques.

### 16.1 Pourquoi et comment tester

Un **test unitaire** vérifie **une unité de code isolée** (fonction, service, composant) de façon **rapide**, **automatique** et **répétable**. Il protège contre les **régressions**, documente le comportement attendu et rend les **refactorisations** sûres (par exemple lors d'une migration de version).

**La pyramide de tests** : à la base, **beaucoup** de tests unitaires (rapides, précis) ; au milieu, des tests d'**intégration** (plusieurs unités ensemble) ; au sommet, **peu** de tests **E2E** (lents mais réalistes, chapitre 17).

**Vocabulaire**

- **Suite** (`describe`) : groupe de tests. **Test** (`it` / `test`) : un scénario. **Assertion** (`expect(...)`) : vérification d'un résultat.
- **Doublure** (*test double*) : objet qui remplace une vraie dépendance. Variantes : **factice** (*stub*, renvoie des valeurs prévues), **espion** (*spy*, enregistre les appels), **mock** (stub + vérification des appels).
- **Arrange – Act – Assert** : préparer, agir, vérifier.
- **`TestBed`** : l'environnement de test d'Angular, qui crée un **module de test** avec injecteur pour instancier composants et services.

### 16.2 L'outillage *(à jour)*

|  | **Avant** | **Aujourd'hui** |
| --- | --- | --- |
| Exécuteur | **Karma** (navigateur) — déprécié depuis 2023 | **Vitest** (**par défaut depuis la v21**, stable en v22) |
| Cadre d'assertions | Jasmine | API de Vitest (`describe`, `it`, `expect`, `vi`), proche de Jest et de Jasmine |
| Environnement | Chrome (navigateur réel) | jsdom / happy-dom, ou **mode navigateur** de Vitest |
| Outil Angular | `TestBed` | `TestBed` (inchangé) |

```bash
ng test                      # exécute les tests (surveillance par défaut en local)
ng test --no-watch --coverage
```

**Convention** : le test d'un fichier `compteur.ts` se nomme `compteur.spec.ts` et se place **à côté**. `ng generate` crée ces fichiers (sauf `--skip-tests`).

> **Migration.** Pour passer un projet Karma/Jasmine à Vitest : `ng generate @angular/core:karma-to-vitest` (chapitre 28). Karma et Jasmine restent utilisables sur les projets existants. Dans un environnement simulé (jsdom), vérifiez que les fonctionnalités dépendant du navigateur (mise en page, `IntersectionObserver`…) sont bien couvertes, ou utilisez le **mode navigateur** de Vitest.

### 16.3 Tester un composant

```typescript
// src/app/compteur.spec.ts
import { TestBed } from '@angular/core/testing';
import { describe, it, expect } from 'vitest';               // optionnel : les globales sont disponibles avec `ng test`
import { Compteur } from './compteur';

describe('Compteur', () => {
    it('incrémente la valeur au clic', async () => {
        const fixture = TestBed.createComponent(Compteur);
        await fixture.whenStable();                           // attend le premier rendu (mode zoneless)

        const bouton = fixture.nativeElement.querySelector('button') as HTMLButtonElement;
        bouton.click();
        await fixture.whenStable();                           // attend la mise à jour de la vue

        expect(fixture.nativeElement.querySelector('h2')?.textContent).toContain('1');
    });
});
```

**Rôle de la `fixture`** (`ComponentFixture`) : `componentInstance` (la classe), `nativeElement` (le DOM), `debugElement` (API d'interrogation indépendante de la plateforme), `componentRef.setInput()` (entrées), `whenStable()` (attend la fin des mises à jour), `detectChanges()` (force une détection, surtout avec Zone.js).

**Entrées de type signal** : on ne peut pas affecter `componentInstance.nom = …`, car l'entrée est en lecture seule ; on passe **toujours** par `setInput()`.

```typescript
// src/app/carte-produit.spec.ts
import { TestBed } from '@angular/core/testing';
import { describe, it, expect } from 'vitest';
import { CarteProduit } from './carte-produit';

describe('CarteProduit', () => {
    it('affiche le titre transmis en entrée', async () => {
        const fixture = TestBed.createComponent(CarteProduit);
        fixture.componentRef.setInput('nom', 'Livre');        // entrées signaux : toujours via setInput()
        await fixture.whenStable();
        expect(fixture.nativeElement.textContent).toContain('Livre');
    });

    it('émet une sortie au clic', async () => {
        const fixture = TestBed.createComponent(CarteProduit);
        fixture.componentRef.setInput('nom', 'Livre');
        await fixture.whenStable();

        const emis: string[] = [];
        fixture.componentInstance.ajouter.subscribe((v: string) => emis.push(v));    // une `output()` est abonnable
        (fixture.nativeElement.querySelector('button') as HTMLButtonElement).click();

        expect(emis).toEqual(['Livre']);
    });
});
```

> **À retenir.** Avec des composants **zoneless / signaux**, on attend le rendu avec **`await fixture.whenStable()`**. En mode avec Zone.js, `fixture.detectChanges()` reste utilisable.

**Composant hôte de test.** Pour tester un composant **tel qu'il est utilisé** (projection de contenu, liaisons parent → enfant), on crée un petit composant dans le fichier de test qui l'utilise dans son gabarit.

```typescript
// src/app/panneau.spec.ts
import { Component } from '@angular/core';
import { TestBed } from '@angular/core/testing';
import { describe, it, expect } from 'vitest';
import { Panneau } from './panneau';

@Component({
    imports: [Panneau],
    template: `<app-panneau><h2 titre>Mon titre</h2><p>Corps</p></app-panneau>`,
})
class HoteDeTest {}

describe('Panneau', () => {
    it('projette le titre et le contenu', async () => {
        const fixture = TestBed.createComponent(HoteDeTest);
        await fixture.whenStable();
        const html = fixture.nativeElement as HTMLElement;
        expect(html.querySelector('header h2')?.textContent).toBe('Mon titre');
        expect(html.querySelector('section')?.textContent).toContain('Corps');
    });
});
```

### 16.4 Tester un service

```typescript
// src/app/panier.store.spec.ts
import { TestBed } from '@angular/core/testing';
import { beforeEach, describe, it, expect } from 'vitest';
import { PanierStore } from './panier.store';

describe('PanierStore', () => {
    let store: PanierStore;
    beforeEach(() => {
        TestBed.configureTestingModule({});
        store = TestBed.inject(PanierStore);
    });

    it('calcule le total', () => {
        store.ajouter({ id: 1, nom: 'Livre', prix: 10, quantite: 2 });
        store.ajouter({ id: 2, nom: 'Stylo', prix: 5, quantite: 1 });
        expect(store.total()).toBe(25);
    });
});
```

Chaque test obtient un **`TestBed` neuf** : un service `providedIn: 'root'` est donc recréé, sans état résiduel du test précédent. Un service **sans dépendance** peut même être testé **sans `TestBed`** (`new MonService()`), ce qui est plus rapide.

### 16.5 Tester les appels HTTP

```typescript
// src/app/utilisateur.spec.ts
import { TestBed } from '@angular/core/testing';
import { provideHttpClient } from '@angular/common/http';
import { provideHttpClientTesting, HttpTestingController } from '@angular/common/http/testing';
import { afterEach, beforeEach, describe, it, expect } from 'vitest';
import { Utilisateur, UtilisateurService } from './utilisateur';

describe('UtilisateurService', () => {
    let service: UtilisateurService;
    let http: HttpTestingController;

    beforeEach(() => {
        TestBed.configureTestingModule({ providers: [provideHttpClient(), provideHttpClientTesting()] });
        service = TestBed.inject(UtilisateurService);
        http = TestBed.inject(HttpTestingController);
    });
    afterEach(() => http.verify());                           // aucune requête non attendue

    it('récupère un utilisateur', () => {
        let resultat: Utilisateur | undefined;
        service.trouver(1).subscribe((u) => (resultat = u));

        const requete = http.expectOne('/api/utilisateurs/1');
        expect(requete.request.method).toBe('GET');
        requete.flush({ id: 1, nom: 'Alice', email: 'a@b.fr' });

        expect(resultat?.nom).toBe('Alice');
    });

    it('gère les erreurs', () => {
        let statut = 0;
        service.trouver(9).subscribe({ error: (e) => (statut = e.status) });
        http.expectOne('/api/utilisateurs/9').flush('Introuvable', { status: 404, statusText: 'Not Found' });
        expect(statut).toBe(404);
    });
});
```

- **`expectOne(url)`** exige **exactement une** requête correspondante ; `expectNone` vérifie qu'il n'y en a pas ; `match` en renvoie plusieurs.
- **`flush(corps, options)`** simule la réponse ; `error(événement)` simule une erreur réseau.
- **`http.verify()`** échoue si une requête reste en attente ou n'a pas été attendue.

**Tester un intercepteur** : on l'enregistre avec `provideHttpClient(withInterceptors([monIntercepteur]))`, on émet une requête et on inspecte `requete.request.headers` dans `expectOne`.

### 16.6 Doublures (*mocks*) et injection

```typescript
import { TestBed } from '@angular/core/testing';
import { afterEach, describe, it, expect, vi } from 'vitest';
import { of } from 'rxjs';
import { UtilisateurService } from './utilisateur';

describe('Doublures', () => {
    afterEach(() => vi.useRealTimers());

    it('remplace le service réel par une doublure', () => {
        const serviceFactice = { lister: vi.fn().mockReturnValue(of([{ id: 1, nom: 'Alice', email: 'a@b.fr' }])) };

        TestBed.configureTestingModule({
            providers: [{ provide: UtilisateurService, useValue: serviceFactice }],         // remplace le service réel
        });

        TestBed.inject(UtilisateurService).lister().subscribe((liste) => expect(liste).toHaveLength(1));
        expect(serviceFactice.lister).toHaveBeenCalledTimes(1);
    });

    it('espionne la console et simule le temps', () => {
        const espion = vi.spyOn(console, 'error').mockImplementation(() => {});
        console.error('Erreur simulée');
        expect(espion).toHaveBeenCalledWith('Erreur simulée');

        vi.useFakeTimers();
        const rappel = vi.fn();
        setTimeout(rappel, 1000);
        vi.advanceTimersByTime(1000);
        expect(rappel).toHaveBeenCalledTimes(1);
    });
});
```

- **`vi.fn()`** crée une fonction espion ; `mockReturnValue` fixe sa valeur de retour ; `toHaveBeenCalledWith` vérifie les arguments.
- **`vi.spyOn(objet, 'méthode')`** espionne (et éventuellement remplace) une méthode existante.
- **`vi.useFakeTimers()` + `vi.advanceTimersByTime()`** contrôlent le temps (minuteries, anti-rebond) **sans attente réelle**. `fakeAsync` / `tick` d'Angular dépendent de Zone.js et ne conviennent pas à un projet **zoneless**.
- **Où remplacer ?** `providers: [{ provide: X, useValue: faux }]` dans `TestBed` ; ou `overrideComponent` pour remplacer des fournisseurs propres à un composant.

**Composants avec routeur** : `provideRouter([])` ou une table de routes de test, puis `RouterTestingHarness` pour naviguer et interroger le composant actif.

```typescript
// src/app/navigation.spec.ts
import { TestBed } from '@angular/core/testing';
import { provideRouter } from '@angular/router';
import { RouterTestingHarness } from '@angular/router/testing';
import { describe, it, expect } from 'vitest';
import { DetailProduit } from './produits/detail';

describe('Routage', () => {
    it('affiche le détail pour /produits/42', async () => {
        TestBed.configureTestingModule({ providers: [provideRouter([{ path: 'produits/:id', component: DetailProduit }])] });
        const harnais = await RouterTestingHarness.create();
        const composant = await harnais.navigateByUrl('/produits/42', DetailProduit);
        expect(composant).toBeTruthy();
    });
});
```

**Tester une garde fonctionnelle** : on l'exécute dans un contexte d'injection.

```typescript
// src/app/auth/auth-garde.spec.ts
import { TestBed } from '@angular/core/testing';
import { ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree, provideRouter } from '@angular/router';
import { describe, it, expect } from 'vitest';
import { authGarde } from './auth-garde';
import { AuthService } from './auth';

describe('authGarde', () => {
    it('redirige vers /connexion si non connecté', () => {
        TestBed.configureTestingModule({
            providers: [provideRouter([]), { provide: AuthService, useValue: { estConnecte: () => false } }],
        });
        const resultat = TestBed.runInInjectionContext(() =>
            authGarde({} as ActivatedRouteSnapshot, { url: '/admin' } as RouterStateSnapshot),
        );
        expect(resultat instanceof UrlTree).toBe(true);
    });
});
```

### 16.7 Harnais de composants (*component harnesses*)

Les **harnais** (CDK) offrent une API **stable** pour interagir avec des composants (Material, Aria, ou vos composants) **sans dépendre du HTML interne**. Si l'implémentation de `mat-button` change, vos tests continuent de fonctionner, car ils parlent à une **abstraction** (« clique », « est désactivé »).

```typescript
import { Component } from '@angular/core';
import { TestBed } from '@angular/core/testing';
import { TestbedHarnessEnvironment } from '@angular/cdk/testing/testbed';
import { MatButton } from '@angular/material/button';
import { MatButtonHarness } from '@angular/material/button/testing';
import { describe, it, expect } from 'vitest';

@Component({
    selector: 'app-envoi',
    imports: [MatButton],
    template: `<button mat-button>Envoyer</button>`,
})
class Envoi {}

describe('Envoi', () => {
    it('expose un bouton activé', async () => {
        const fixture = TestBed.createComponent(Envoi);
        const loader = TestbedHarnessEnvironment.loader(fixture);

        const bouton = await loader.getHarness(MatButtonHarness.with({ text: 'Envoyer' }));
        await bouton.click();
        expect(await bouton.isDisabled()).toBe(false);
    });
});
```

Toutes les méthodes d'un harnais sont **asynchrones** (`await`) : elles attendent automatiquement la stabilité de l'application. Vous pouvez écrire des harnais pour vos propres composants (classe qui étend `ComponentHarness` avec un `hostSelector` et des méthodes d'interaction) : très utile pour une **bibliothèque de composants**.

### 16.8 Tester des signaux et effets

```typescript
import { computed, effect, signal } from '@angular/core';
import { TestBed } from '@angular/core/testing';
import { describe, it, expect } from 'vitest';

describe('signaux', () => {
    it('réagit aux signaux', () => {
        TestBed.runInInjectionContext(() => {
            const s = signal(1);
            const d = computed(() => s() * 2);
            s.set(5);
            expect(d()).toBe(10);
        });
    });

    it('exécute un effet', () => {
        const valeurs: number[] = [];
        TestBed.runInInjectionContext(() => {
            const s = signal(1);
            effect(() => valeurs.push(s()));
            TestBed.tick();                      // force l'exécution des effets
            s.set(2);
            TestBed.tick();
        });
        expect(valeurs).toEqual([1, 2]);
    });
});
```

- Un `computed` se teste en **lisant** sa valeur : aucun mécanisme spécial.
- Un `effect` **nécessite** un contexte d'injection (`TestBed.runInInjectionContext`) et s'exécute de façon **planifiée** : `TestBed.tick()` force l'exécution.
- Une `resource` se teste en simulant son chargeur ou, pour `httpResource`, avec `HttpTestingController` (`TestBed.tick()` puis `expectOne`).

### 16.9 Couverture et bonnes pratiques

```bash
ng test --coverage                # rapport dans coverage/
```

**Couverture** : pourcentage de lignes, branches, fonctions exécutées par les tests. Un **seuil minimal** en CI évite la dégradation, mais **100 % ne garantit pas la qualité** : un test qui n'a aucune assertion couvre du code sans rien vérifier.

- Tester le **comportement** (ce que voit l'utilisateur), pas les détails d'implémentation (noms de méthodes privées, structure interne).
- **Un cas par test**, nommé clairement (« affiche une erreur si le courriel est invalide ») ; schéma *Arrange – Act – Assert*.
- Peu de `TestBed` pour la logique pure : testez les fonctions et services **sans `TestBed`** quand c'est possible.
- Isolez les dépendances (HTTP, routeur, horloge, `localStorage`).
- Des tests **indépendants** : aucun ne dépend de l'ordre d'exécution ni de l'état laissé par un autre.
- Pas de **`setTimeout` réels** dans les tests : horloge factice.
- Évitez les tests de **capture instantanée** (*snapshots*) volumineux : ils se valident par réflexe et ne protègent plus rien.
- Exécutez les tests en **CI** (`ng test --no-watch`).

### Synthèse du chapitre 16

Vitest + `TestBed` : on crée la `fixture`, on fixe les entrées avec **`setInput`**, on attend avec **`await fixture.whenStable()`**, on interroge le DOM et on vérifie. Les services se testent avec `TestBed.inject`, le HTTP avec `HttpTestingController`, les dépendances se remplacent par des doublures (`vi.fn`, `useValue`), les composants complexes se pilotent par **harnais**, les signaux et effets dans un **contexte d'injection** avec `TestBed.tick()`.

---

## 17. Tests de bout en bout (E2E)

**Objectifs d'apprentissage.** Définir les tests **E2E** et leur place ; choisir un outil (Playwright, Cypress) ; écrire des tests robustes avec sélecteurs accessibles et attentes automatiques ; simuler l'API ; partager une session authentifiée ; organiser les tests (modèle de page) ; les exécuter en intégration continue.

### 17.1 Panorama *(à jour)*

Les tests **E2E** (*end-to-end*, « de bout en bout ») pilotent un **vrai navigateur** : ils chargent l'application, cliquent, saisissent, et vérifient ce que **voit l'utilisateur**. Ils valident l'**ensemble de la chaîne** (interface, routeur, appels HTTP, parfois le vrai serveur), ce que les tests unitaires ne font pas ; en contrepartie, ils sont **plus lents** et **plus fragiles**.

| Outil | Statut |
| --- | --- |
| **Protractor** | **Fin de vie (2023)** : à migrer |
| **Playwright** | **Recommandé** : multi-navigateurs, rapide, attente automatique, traces |
| **Cypress** | Très répandu, excellente expérience développeur |
| **WebdriverIO**, **Nightwatch**, **TestCafe** | Alternatives |

```bash
ng e2e                              # propose d'ajouter un outil (Playwright, Cypress…)
# ou directement :
npm init playwright@latest
```

### 17.2 Exemple avec Playwright

```typescript
// e2e/connexion.spec.ts
import { test, expect } from '@playwright/test';

test('un utilisateur peut se connecter', async ({ page }) => {
    await page.goto('/connexion');
    await page.getByLabel('E-mail').fill('alice@exemple.com');
    await page.getByLabel('Mot de passe').fill('secret');
    await page.getByRole('button', { name: 'Se connecter' }).click();

    await expect(page).toHaveURL(/tableau-de-bord/);
    await expect(page.getByRole('heading', { name: 'Bonjour Alice' })).toBeVisible();
});

test('affiche une erreur si le mot de passe est faux', async ({ page }) => {
    await page.route('**/api/connexion', (route) => route.fulfill({ status: 401, json: { message: 'Identifiants invalides' } }));   // API simulée
    await page.goto('/connexion');
    await page.getByLabel('E-mail').fill('alice@exemple.com');
    await page.getByLabel('Mot de passe').fill('faux');
    await page.getByRole('button', { name: 'Se connecter' }).click();
    await expect(page.getByText('Identifiants invalides')).toBeVisible();
});
```

```typescript
// playwright.config.ts (extrait)
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
    testDir: './e2e',
    use: { baseURL: 'http://localhost:4200', trace: 'on-first-retry' },
    webServer: { command: 'ng serve', url: 'http://localhost:4200', reuseExistingServer: !process.env['CI'] },
    projects: [{ name: 'chromium', use: { ...devices['Desktop Chrome'] } }, { name: 'firefox', use: { ...devices['Desktop Firefox'] } }],
});
```

**Concepts clés de Playwright**

- **Localisateurs** (`page.getByRole`, `getByLabel`, `getByText`, `getByTestId`) : trouvent un élément de façon **paresseuse** et **réessaient** automatiquement jusqu'à l'apparition de l'élément.
- **Assertions « web-first »** (`await expect(locator).toBeVisible()`) : **réessaient** jusqu'à réussite ou délai d'expiration, ce qui supprime les attentes fixes.
- **Isolation** : chaque test reçoit un **contexte de navigateur neuf** (cookies, stockage vides).
- **`page.route`** : intercepte et simule les requêtes réseau.
- **`webServer`** : lance l'application avant les tests.
- **Traces** (`trace`) : enregistrement rejouable (DOM, réseau, captures) pour comprendre un échec.
- **Exécution** : `npx playwright test`, `--ui` (interface interactive), `--headed` (navigateur visible), `codegen` (génère un test en enregistrant vos actions).

#### Session authentifiée réutilisable

Se connecter **dans chaque test** est lent. On se connecte **une fois** et on réutilise l'état (cookies, stockage local).

```typescript
// e2e/auth.setup.ts
import { test as setup, expect } from '@playwright/test';

setup('connexion', async ({ page }) => {
    await page.goto('/connexion');
    await page.getByLabel('E-mail').fill('alice@exemple.com');
    await page.getByLabel('Mot de passe').fill('secret');
    await page.getByRole('button', { name: 'Se connecter' }).click();
    await expect(page).toHaveURL(/tableau-de-bord/);
    await page.context().storageState({ path: 'e2e/.auth/alice.json' });     // sauvegarde de l'état
});
```

Les projets de test déclarent ensuite `use: { storageState: 'e2e/.auth/alice.json' }` et une dépendance sur le projet de *setup*. Ne **versionnez pas** le dossier `.auth` (ajoutez-le à `.gitignore`).

#### Modèle d'objet de page (*Page Object*)

Pour éviter de répéter les sélecteurs, on regroupe les actions d'une page dans une classe : si l'interface change, on ne corrige qu'**un seul endroit**.

```typescript
// e2e/pages/connexion-page.ts
import { Page, expect } from '@playwright/test';

export class ConnexionPage {
    constructor(private readonly page: Page) {}

    async ouvrir(): Promise<void> { await this.page.goto('/connexion'); }
    async seConnecter(courriel: string, motDePasse: string): Promise<void> {
        await this.page.getByLabel('E-mail').fill(courriel);
        await this.page.getByLabel('Mot de passe').fill(motDePasse);
        await this.page.getByRole('button', { name: 'Se connecter' }).click();
    }
    async verifierErreur(message: string): Promise<void> {
        await expect(this.page.getByText(message)).toBeVisible();
    }
}
```

### 17.3 Exemple avec Cypress

```typescript
// cypress/e2e/connexion.cy.ts
describe('Connexion', () => {
    it('connecte l\'utilisateur', () => {
        cy.visit('/connexion');
        cy.get('input[name=email]').type('alice@exemple.com');
        cy.get('input[name=motDePasse]').type('secret');
        cy.contains('button', 'Se connecter').click();
        cy.url().should('include', '/tableau-de-bord');
    });
});
```

**Particularités de Cypress** : exécution **dans** le navigateur (exécuteur interactif très agréable, retour visuel pas à pas), **réessais automatiques** des commandes et assertions, `cy.intercept()` pour simuler l'API, `cy.session()` pour réutiliser une connexion. Les commandes sont **asynchrones en file d'attente** : on n'utilise pas `await` dessus de la même façon qu'avec Playwright.

**Playwright ou Cypress ?** Playwright : plusieurs navigateurs (Chromium, Firefox, WebKit), parallélisme natif, plusieurs onglets / contextes. Cypress : prise en main et débogage visuel très appréciés. Les deux conviennent ; choisissez selon l'équipe.

### 17.4 Exécution en intégration continue

```yaml
# .github/workflows/e2e.yml (extrait)
name: e2e
on: [push]
jobs:
  e2e:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
      - run: npm ci
      - run: npx playwright install --with-deps
      - run: npx playwright test
      - uses: actions/upload-artifact@v4
        if: failure()
        with:
          name: playwright-report
          path: playwright-report/
```

Conservez le **rapport**, les **traces** et les **captures** en cas d'échec (`if: failure()`). Utilisez des **réessais limités** (`retries: 2` en CI) pour tolérer un échec ponctuel, mais **traquez** les tests instables au lieu de les masquer.

### 17.5 Bonnes pratiques E2E

- Sélectionnez par **rôle / libellé accessible** (`getByRole`, `getByLabel`) ou `data-testid`, **pas** par classes CSS ni par structure du DOM. Bénéfice supplémentaire : vos tests vérifient indirectement l'**accessibilité**.
- Testez les **parcours critiques** (connexion, achat, inscription), pas chaque détail.
- **Isolez les données** : comptes de test dédiés, base de test réinitialisée, ou API simulée.
- Évitez les **attentes fixes** (`waitForTimeout`) : utilisez les attentes automatiques.
- Chaque test est **indépendant** et peut tourner **seul** et en **parallèle**.
- **Un test instable** (*flaky*) est un bug : trouvez la cause (attente implicite, données partagées, animation) plutôt que de relancer.
- Ajoutez des **contrôles d'accessibilité automatisés** (par exemple `@axe-core/playwright`) sur les pages clés.
- Pyramide de tests : **beaucoup** de tests unitaires, **quelques** tests d'intégration, **peu** de tests E2E.

### Synthèse du chapitre 17

Les tests E2E valident des **parcours complets** dans un vrai navigateur. **Playwright** (recommandé) ou **Cypress** ; localisateurs par **rôle / libellé**, **attentes automatiques**, API simulée avec `page.route`, session réutilisée, **modèle de page**, exécution en **CI** avec traces. Peu de tests, sur l'essentiel.

---

# Partie IV — Performance

## 18. Détection des changements

**Objectifs d'apprentissage.** Expliquer **comment et quand** Angular met à jour le DOM ; comparer les modèles **Zone.js** et **zoneless** ; migrer vers le mode zoneless ; maîtriser les stratégies **`Default`** et **`OnPush`** ; utiliser `markForCheck` à bon escient ; comprendre l'erreur NG0100 ; réduire le travail de détection ; **mesurer** avec les bons outils.

### 18.1 Principe

La **détection des changements** (*change detection*) est le mécanisme qui décide **quand** et **quoi** mettre à jour dans le DOM après que l'état de l'application a changé. Elle parcourt l'**arbre de composants** (de la racine vers les feuilles), évalue les **liaisons** de chaque gabarit, compare les valeurs aux précédentes et applique au DOM **uniquement les différences**.

Deux questions se posent : **(1) Comment Angular apprend-il qu'il faut vérifier ?** (le *déclencheur*) et **(2) quelles parties de l'arbre vérifie-t-il ?** (la *portée*). Les modèles ci-dessous répondent différemment à (1), et les stratégies `Default` / `OnPush` à (2).

|  | **Avec Zone.js** (historique) | **Zoneless** (moderne) |
| --- | --- | --- |
| Déclencheur | **Zone.js** intercepte événements, minuteries, promesses, requêtes réseau et lance une vérification de l'arbre | **Signaux**, événements du gabarit, `markForCheck`, tube `async` |
| Précision | Vérifie (tout ou partie de) l'arbre à chaque tâche asynchrone | Met à jour **ce qui a changé** |
| Taille / perf | Zone.js (\~35 Ko), vérifications superflues | Moins de code, plus rapide |
| Débogage | Piles d'appels complexes | Plus lisible |
| Statut | Toujours supporté | **Défaut des nouveaux projets depuis la v21** |

**Qu'est-ce que Zone.js ?** Une bibliothèque qui **modifie (« patche »)** les API asynchrones du navigateur (`setTimeout`, `addEventListener`, `Promise`, `XMLHttpRequest`…) pour savoir **quand une tâche asynchrone se termine**. Angular en déduit « quelque chose a peut-être changé » et relance une vérification. C'est **pratique** (rien à déclarer) mais **coûteux** (vérifications superflues, taille, incompatibilité avec certaines API natives comme `async/await` natif ou certaines classes) et **opaque**.

**Le modèle réactif des signaux.** Avec les signaux, Angular **sait précisément** quel gabarit lit quel signal. Quand un signal change, il **marque** uniquement les vues concernées comme « à vérifier » et **planifie** une mise à jour. Plus besoin de deviner à partir des tâches asynchrones.

### 18.2 Passer en zoneless

```typescript
// src/app/app.config.ts
import { ApplicationConfig, provideZonelessChangeDetection } from '@angular/core';

export const appConfig: ApplicationConfig = {
    providers: [provideZonelessChangeDetection()],
};
```

```jsonc
// angular.json (extrait) : retirer "zone.js" de "polyfills" (et de la cible "test")
{
    "projects": { "mon-app": { "architect": { "build": { "options": { "polyfills": [] } } } } }
}
```

En zoneless, Angular lance une détection de changements lorsque :

1. un **signal lu dans un gabarit** change ;
2. un **écouteur d'événement** du gabarit (`(click)`) s'exécute ;
3. le tube **`async`** reçoit une valeur ;
4. **`ChangeDetectorRef.markForCheck()`** est appelé ;
5. un composant est **créé ou détruit**, ou une vue est attachée / détachée (`ViewContainerRef`) ;
6. `ComponentRef.setInput()` est appelé ;
7. (cas particuliers : `afterRender`, navigation du routeur).

#### Conditions pour qu'un composant soit « compatible zoneless »

- L'état affiché provient de **signaux** (ou du tube `async`).
- **Pas de modifications silencieuses** de champs ordinaires (`this.x = …` dans un `setTimeout`, une promesse ou un rappel de bibliothèque) : utilisez un **signal**.
- Les bibliothèques tierces doivent notifier Angular (`ChangeDetectorRef.markForCheck()` ou un signal).
- **Retirer `NgZone`** de la logique : `NgZone.onStable`, `NgZone.run()`, `runOutsideAngular()` n'ont plus d'effet utile ; les remplacer par `afterNextRender`, `effect`, ou rien.
- Les **tests** doivent eux aussi être zoneless : `await fixture.whenStable()` au lieu de `fixture.detectChanges()` + `fakeAsync` (chapitre 16).

**Migration progressive.** Un projet peut d'abord adopter `OnPush` partout et les signaux, puis activer `provideZonelessChangeDetection()`. Les incompatibilités apparaissent comme des **vues qui ne se rafraîchissent pas** : cherchez les champs modifiés hors d'un signal.

### 18.3 Stratégies : `Default` et `OnPush`

Une **stratégie** précise **quand** un composant est inclus dans la vérification.

| Stratégie | Le composant est vérifié quand… |
| --- | --- |
| `Default` | À **chaque** cycle de détection (toujours) |
| **`OnPush`** | Une **entrée** change (par **référence**), un **événement** du composant se produit, un **signal** lu dans le gabarit change, `markForCheck()` est appelé, le tube `async` émet |

```typescript
// src/app/liste.ts
import { ChangeDetectionStrategy, Component, input } from '@angular/core';

@Component({
    selector: 'app-liste',
    changeDetection: ChangeDetectionStrategy.OnPush,        // par défaut pour les nouveaux composants depuis la v22
    template: `
        <ul>
            @for (article of articles(); track article) { <li>{{ article }}</li> }
        </ul>
    `,
})
export class Liste {
    articles = input<string[]>([]);
}
```

> **v22.** `OnPush` devient la stratégie **par défaut** des nouveaux composants. Pour les composants existants, la migration est automatique et préserve la stratégie `Default` explicite quand elle est nécessaire. Vérifiez dans le guide de migration d'angular.dev la forme exacte de la déclaration explicite de l'ancienne stratégie dans votre version.

**Pourquoi `OnPush` est plus rapide.** Un sous-arbre `OnPush` **non marqué** est **ignoré** pendant la détection : si un grand composant `OnPush` ne reçoit pas de nouvelle entrée et ne contient aucun événement ni signal modifié, Angular ne visite **ni lui ni ses descendants** (à l'exception de ceux qui sont eux-mêmes marqués). Sur un arbre de milliers de nœuds, le gain est considérable.

#### Avec `OnPush`, mettez à jour de façon **immuable**

`OnPush` compare les entrées **par référence** : si vous **mutez** un tableau ou un objet, la référence reste la même et la vue ne se met pas à jour.

```typescript
import { ChangeDetectionStrategy, Component } from '@angular/core';
import { Liste } from './liste';

@Component({
    selector: 'app-articles-immuables',
    imports: [Liste],
    changeDetection: ChangeDetectionStrategy.OnPush,
    template: `
        <app-liste [articles]="articles" />
        <button (click)="ajouter('Nouveau')">Ajouter</button>
    `,
})
export class ArticlesImmuables {
    protected articles: string[] = ['A', 'B'];

    protected ajouter(nouveau: string): void {
        this.articles = [...this.articles, nouveau];            // correct : nouvelle référence
        // this.articles.push(nouveau);                         // incorrect : non détecté (sauf signal)
    }
}
```

La **solution durable** : stocker l'état dans des **signaux**, qui notifient d'eux-mêmes — la règle d'immutabilité reste valable pour les valeurs **à l'intérieur** du signal (chapitre 8).

### 18.4 Outils : `markForCheck`, `detectChanges`, `afterNextRender`

```typescript
import { ChangeDetectorRef, Component, inject } from '@angular/core';

@Component({
    selector: 'app-detection',
    template: `<p>{{ message }}</p>`,
})
export class Detection {
    private readonly cdr = inject(ChangeDetectorRef);
    protected message = 'Initial';

    constructor() {
        setTimeout(() => {
            this.message = 'Modifié';
            this.cdr.markForCheck();          // planifie la vérification du composant (et de ses ancêtres)
            // this.cdr.detectChanges();      // vérification immédiate (à éviter)
        }, 1000);
    }
}
```

| API | Effet |
| --- | --- |
| `markForCheck()` | **Marque** le composant et ses **ancêtres** comme « à vérifier » ; la vérification a lieu au prochain cycle. **Le choix normal** avec du code non-signal |
| `detectChanges()` | Lance **immédiatement** une vérification du composant et de ses enfants. À éviter dans le code applicatif (risque de boucles, de rendus inutiles) ; utile en test |
| `detach()` / `reattach()` | Sort le composant de la détection / le remet (cas extrêmes de performance) |
| `afterNextRender()` / `afterEveryRender()` | Exécute du code **après** le rendu (mesures du DOM) |

> **La bonne pratique.** Au lieu de `markForCheck()`, **convertissez l'état en signal** : le composant se met alors à jour sans aucun appel manuel.

#### L'erreur NG0100 (`ExpressionChangedAfterItHasBeenChecked`)

En mode développement, après chaque détection, Angular **revérifie** les liaisons ; si une valeur a **changé pendant la vérification**, il lève **NG0100**. Cause fréquente : un enfant (ou un hook comme `ngAfterViewInit`) modifie un état déjà affiché par le parent. Remèdes : **remonter** l'état dans un signal modifié **avant** le rendu, utiliser un `computed`, déplacer la modification dans `afterNextRender` suivi d'un signal, ou **repenser** le flux de données (un enfant ne devrait pas modifier le parent directement). Ne masquez pas l'erreur avec un `setTimeout`.

### 18.5 Réduire le travail de détection

| Technique | Effet |
| --- | --- |
| **Signaux + `OnPush`** | Mises à jour ciblées |
| **`track`** dans `@for` | Réutilise le DOM au lieu de le recréer |
| Pas d'appels de **méthodes** lourdes dans le gabarit | Utiliser `computed()` (mémoïsé) ou des **tubes purs** |
| **`@defer`** | Reporter le rendu de zones non critiques (chapitre 19) |
| **`NgZone.runOutsideAngular()`** (avec Zone.js) | Exécuter des tâches fréquentes (animations, `mousemove`) sans déclencher de détection |
| **Défilement virtuel** (`cdk-virtual-scroll-viewport`) | Ne rend que les lignes **visibles** d'une grande liste |
| **Pagination** / chargement progressif | Limite le nombre de nœuds |
| Éviter les **expressions coûteuses** et les nouveaux objets / tableaux littéraux dans les liaisons (`[options]="{ a: 1 }"` crée un objet à chaque cycle sans `OnPush`) | Évite les rendus enfants inutiles |

```typescript
// src/app/grande-liste.ts : défilement virtuel (CDK)
import { ChangeDetectionStrategy, Component } from '@angular/core';
import { ScrollingModule } from '@angular/cdk/scrolling';

@Component({
    selector: 'app-grande-liste',
    imports: [ScrollingModule],
    changeDetection: ChangeDetectionStrategy.OnPush,
    template: `
        <cdk-virtual-scroll-viewport itemSize="40" class="viewport">
            <div *cdkVirtualFor="let ligne of lignes" class="ligne">{{ ligne }}</div>
        </cdk-virtual-scroll-viewport>
    `,
    styles: `.viewport { height: 400px; } .ligne { height: 40px; }`,
})
export class GrandeListe {
    protected readonly lignes = Array.from({ length: 100_000 }, (_, i) => `Ligne ${i + 1}`);
}
```

Seules les lignes visibles (et une marge) existent dans le DOM : 100 000 éléments ne coûtent que quelques dizaines de nœuds.

### 18.6 Mesurer

> **Règle d'or : on n'optimise que ce que l'on a mesuré.**

- **Angular DevTools** (extension Chrome / Firefox) : **profileur** de détection des changements (durée par cycle, par composant), arbre de composants, graphe de signaux, injecteurs.
- **Lighthouse** et **Web Vitals** : **LCP** (affichage du plus grand élément), **INP** (réactivité aux interactions), **CLS** (stabilité visuelle).
- Panneau **Performance** du navigateur : tâches longues, rendus, scripts.
- `ng build --stats-json` pour la taille des bundles (chapitre 20).

### Synthèse du chapitre 18

La détection des changements met à jour le DOM. **Zone.js** déduit les changements des tâches asynchrones ; le mode **zoneless** s'appuie sur les **signaux** et des déclencheurs explicites (défaut des nouveaux projets depuis la **v21**). **`OnPush`** (défaut en **v22**) limite les vérifications aux composants marqués : mises à jour **immuables**, état en **signaux**. `markForCheck` plutôt que `detectChanges`. Réduire le travail : `track`, `computed`, `@defer`, défilement virtuel. **Mesurer** avant d'optimiser.

---

## 19. Chargement paresseux et vues différées

**Objectifs d'apprentissage.** Comprendre l'intérêt du **chargement paresseux** ; découper une application par **routes** ; **précharger** intelligemment ; différer des morceaux de gabarit avec **`@defer`** (déclencheurs, blocs `@placeholder` / `@loading` / `@error`, `prefetch`, hydratation) ; charger du code **à la demande** par import dynamique ; **vérifier** le résultat.

### 19.1 Pourquoi charger paresseusement ?

Un navigateur doit **télécharger, analyser et exécuter** tout le JavaScript du bundle initial avant d'afficher l'application. Plus il est gros, plus l'attente est longue, surtout sur mobile et réseau lent. Le **chargement paresseux** (*lazy loading*) découpe le code en **morceaux** (*chunks*) et ne télécharge que ce qui est **nécessaire maintenant**, le reste étant récupéré **à la demande**. Gains : meilleurs **FCP** (premier affichage) et **LCP**, moindre consommation de données, démarrage plus rapide.

Angular offre trois niveaux de granularité : **par route** (une page entière), **par bloc de gabarit** (`@defer`), **par code** (import dynamique `import()`).

### 19.2 Routes à chargement paresseux

```typescript
// src/app/app.routes.ts
import { Routes } from '@angular/router';
import { Accueil } from './accueil/accueil';

export const routes: Routes = [
    { path: '', component: Accueil },                                                            // dans le bundle initial
    { path: 'produits', loadComponent: () => import('./produits/liste').then((m) => m.Liste) },   // composant paresseux
    { path: 'admin', loadChildren: () => import('./admin/admin.routes').then((m) => m.ADMIN_ROUTES) },   // groupe de routes
];
```

```typescript
// src/app/admin/admin.routes.ts
import { Routes } from '@angular/router';
import { AdminAccueil } from './admin-accueil';
import { AdminService } from './admin.service';

export const ADMIN_ROUTES: Routes = [
    { path: '', component: AdminAccueil, providers: [AdminService] },                // providers propres à ces routes
    { path: 'utilisateurs', loadComponent: () => import('./utilisateurs').then((m) => m.Utilisateurs) },
];
```

```typescript
// src/app/admin/admin.service.ts
import { Injectable } from '@angular/core';

@Injectable()                                   // fourni par les routes d'administration (pas providedIn: 'root')
export class AdminService {
    nom = 'Espace d\'administration';
}
```

**Comment ça marche ?** `import('./liste')` est un **import dynamique** : le **builder** (esbuild) repère ces appels et place le module dans un **fichier séparé** (*chunk*). Le routeur n'exécute la fonction `loadComponent` / `loadChildren` qu'à la **première navigation** vers la route ; il met le résultat en cache pour la suite.

- Raccourci si le composant est exporté **par défaut** : `loadComponent: () => import('./liste')`.
- Les `providers` d'une route lui donnent un **injecteur d'environnement** propre (chapitre 7) : le service n'existe que lorsque cette partie est chargée.
- **Combiner avec `canMatch`** : une garde `canMatch` peut empêcher le **téléchargement** du code d'une section protégée pour un utilisateur non autorisé.

> *(héritage)* Avec les `NgModule` : `loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule)`. Migration automatique : `ng generate @angular/core:route-lazy-loading`.

### 19.3 Stratégies de préchargement

Par défaut, un morceau paresseux n'est téléchargé **qu'au moment de la navigation**, ce qui peut causer un court délai. Le **préchargement** (*preloading*) télécharge les morceaux **en arrière-plan**, une fois l'application stable, pour qu'ils soient prêts quand l'utilisateur naviguera.

| Stratégie | Fonctionnement |
| --- | --- |
| `NoPreloading` | Chargement **à la navigation** (défaut) |
| `PreloadAllModules` | Précharge **tout** une fois l'application stable |
| **Personnalisée** | Choisir quelles routes précharger (réseau, priorité) |

```typescript
// src/app/prechargement-selectif.ts
import { Injectable } from '@angular/core';
import { PreloadingStrategy, Route } from '@angular/router';
import { Observable, of } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class PrechargementSelectif implements PreloadingStrategy {
    preload(route: Route, charger: () => Observable<unknown>): Observable<unknown> {
        return route.data?.['precharger'] ? charger() : of(null);
    }
}
```

```typescript
// src/app/app.config.ts
import { ApplicationConfig } from '@angular/core';
import { provideRouter, withPreloading } from '@angular/router';
import { routes } from './app.routes';
import { PrechargementSelectif } from './prechargement-selectif';

export const appConfig: ApplicationConfig = {
    providers: [provideRouter(routes, withPreloading(PrechargementSelectif))],
};
```

```typescript
// src/app/app.routes.ts (extrait) : cette route sera préchargée
import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: 'rapports',
        loadChildren: () => import('./rapports/rapports.routes').then((m) => m.RAPPORTS_ROUTES),
        data: { precharger: true },
    },
];
```

Une stratégie personnalisée peut tenir compte de la **qualité de connexion** (`navigator.connection.saveData`, type de réseau) pour ne pas gaspiller les données d'un utilisateur en mode économie.

### 19.4 Vues différées : `@defer` *(ajout)*

Le bloc **`@defer`** charge **paresseusement** un composant, une directive ou un tube **à l'intérieur d'un gabarit**, selon un **déclencheur**. Là où le chargement par route découpe par **page**, `@defer` découpe par **zone de page** : graphique lourd, éditeur, commentaires, carte, contenu sous la ligne de flottaison.

```html
@defer (on viewport) {
    <app-graphique-lourd [donnees]="donnees()" />
} @placeholder (minimum 300ms) {
    <div class="squelette">Graphique…</div>
} @loading (after 100ms; minimum 500ms) {
    <app-spinner />
} @error {
    <p>Impossible de charger le graphique.</p>
}
```

**Les blocs**

| Bloc | Rôle |
| --- | --- |
| `@defer { … }` | Le contenu différé (chargé au déclenchement) |
| `@placeholder { … }` | Affiché **avant** le déclenchement (obligatoire pour `on viewport`, `on hover`, `on interaction` sans déclencheur explicite) ; paramètre `minimum` : durée minimale d'affichage (évite un clignotement) |
| `@loading { … }` | Affiché **pendant** le téléchargement ; paramètres `after` (délai avant affichage) et `minimum` |
| `@error { … }` | Affiché si le chargement **échoue** |

**Les déclencheurs**

| Déclencheur | Moment |
| --- | --- |
| `on idle` (**défaut**) | Navigateur inactif |
| `on viewport` | L'élément (ou un placeholder) entre dans la **zone visible** |
| `on interaction` | Clic / focus sur un élément déclencheur |
| `on hover` | Survol |
| `on immediate` | Dès que possible (après le rendu initial) |
| `on timer(5s)` | Après un délai |
| `when condition()` | Quand une expression devient vraie (déclenchement **unique**) |

```html
<button #declencheur>Afficher les commentaires</button>
@defer (on interaction(declencheur); prefetch on idle) {
    <app-commentaires />
}
```

On peut **combiner** plusieurs déclencheurs séparés par `;` (le premier qui se produit l'emporte) : `@defer (on viewport; on timer(10s))`.

Composant hôte de ces deux exemples, avec les trois composants différés (un fichier chacun dans un vrai projet) :

```typescript
// src/app/graphique-lourd.ts
import { Component, input } from '@angular/core';

@Component({ selector: 'app-graphique-lourd', template: `<p>Graphique : {{ donnees().join(', ') }}</p>` })
export class GraphiqueLourd {
    donnees = input<number[]>([]);
}

// src/app/spinner.ts
@Component({ selector: 'app-spinner', template: `<p>Chargement…</p>` })
export class Spinner {}

// src/app/commentaires.ts
@Component({ selector: 'app-commentaires', template: `<p>Aucun commentaire.</p>` })
export class Commentaires {}
```

```typescript
// src/app/differe.ts
import { Component, signal } from '@angular/core';
import { GraphiqueLourd } from './graphique-lourd';
import { Spinner } from './spinner';
import { Commentaires } from './commentaires';

@Component({
    selector: 'app-differe',
    imports: [GraphiqueLourd, Spinner, Commentaires],
    template: `
        @defer (on viewport) {
            <app-graphique-lourd [donnees]="donnees()" />
        } @placeholder (minimum 300ms) {
            <div class="squelette">Graphique…</div>
        } @loading (after 100ms; minimum 500ms) {
            <app-spinner />
        } @error {
            <p>Impossible de charger le graphique.</p>
        }

        <button #declencheur>Afficher les commentaires</button>
        @defer (on interaction(declencheur); prefetch on idle) {
            <app-commentaires />
        }
    `,
})
export class Differe {
    protected readonly donnees = signal([3, 5, 8]);
}
```

- **`prefetch`** : télécharge le code **à l'avance** (sans l'afficher), selon un déclencheur propre : `@defer (on interaction; prefetch on hover)` précharge au survol, affiche au clic.
- **Hydratation incrémentale** (SSR) : `@defer (hydrate on viewport)` hydrate des zones **plus tard** (section 22).
- Les composants différés doivent être **autonomes** et **non référencés ailleurs** dans le même fichier (sinon ils restent dans le bundle initial) : on les liste dans `imports` mais Angular les **extrait** automatiquement du bundle principal s'ils ne sont utilisés que dans des blocs `@defer`.
- **Côté serveur (SSR)**, seul le contenu de `@placeholder` est rendu (sauf avec l'hydratation incrémentale) ; les déclencheurs liés au navigateur (`viewport`, `interaction`, `hover`, `idle`, `timer`) ne s'exécutent pas sur le serveur.
- **Accessibilité et stabilité de mise en page** : réservez la **place** du contenu différé (dimensions du placeholder) pour éviter un décalage visuel (CLS).
- **Tests** : `TestBed` permet de contrôler le comportement des blocs différés (les rendre manuellement ou automatiquement) ; consultez la section « Testing defer blocks » de la documentation.

### 19.5 Chargement conditionnel de code

Pour charger un morceau de code **uniquement** quand un événement précis survient (ouverture d'un éditeur, export PDF), on utilise un **import dynamique** :

```typescript
// src/app/editeur.ts
import { Component } from '@angular/core';

@Component({ selector: 'app-editeur', template: `<textarea></textarea>` })
export class Editeur {}
```

```typescript
// src/app/page-editeur.ts
import { Component, ViewContainerRef, viewChild } from '@angular/core';

@Component({
    selector: 'app-page-editeur',
    template: `
        <button (click)="ouvrirEditeur()">Ouvrir l'éditeur</button>
        <ng-container #conteneur />
    `,
})
export class PageEditeur {
    private readonly conteneur = viewChild.required('conteneur', { read: ViewContainerRef });

    protected async ouvrirEditeur(): Promise<void> {
        const { Editeur } = await import('./editeur');           // import dynamique
        this.conteneur().createComponent(Editeur);
    }
}
```

Même principe pour une **bibliothèque lourde** (génération de PDF, graphiques, éditeur de code) : `const { jsPDF } = await import('jspdf');` au moment de l'action de l'utilisateur plutôt qu'un `import` statique en tête de fichier.

### 19.6 Vérifier le résultat

```bash
ng build --stats-json          # puis analyser avec esbuild analyzer / webpack-bundle-analyzer
```

Dans la sortie du build : **« Initial chunk files »** (bundle de démarrage) vs **« Lazy chunk files »** (chargés à la demande). Objectif : un **bundle initial réduit**. Dans l'onglet **Réseau** des outils du navigateur, vérifiez que les *chunks* paresseux ne sont chargés **qu'à la navigation** (ou au déclencheur du `@defer`).

### 19.7 Bonnes pratiques et pièges

- **Une route principale = un morceau paresseux** (fonctionnalités, administration, rapports).
- Gardez dans le bundle initial **uniquement** la page d'accueil, la mise en page et les services transverses.
- Combinez **préchargement** et **`@defer`** pour la fluidité.
- **Piège n° 1** : un import **statique** d'un composant « paresseux » (`import { Admin } from './admin'` n'importe où) l'inclut dans le bundle initial. Le chargement paresseux ne fonctionne que si **plus aucun import statique** ne le référence.
- **Piège n° 2** : un `providedIn: 'root'` référencé par le bundle initial est **dans** le bundle initial ; pour un service propre à une fonctionnalité paresseuse, fournissez-le dans les `providers` de la route.
- **Piège n° 3** : trop de petits morceaux → trop de requêtes ; privilégiez des morceaux **cohérents**.
- N'utilisez pas `@defer` pour du contenu **critique** visible au premier écran (il dégraderait le LCP).

### Synthèse du chapitre 19

Trois niveaux : **routes** (`loadComponent` / `loadChildren`), **gabarit** (`@defer` + déclencheurs + `prefetch`), **code** (`import()` dynamique). Précharger les routes probables (`withPreloading`), garder le bundle initial minimal, vérifier avec `ng build` et l'onglet Réseau, éviter les imports statiques qui annulent le découpage.

---

## 20. Compilation AOT et optimisation du bundle

**Objectifs d'apprentissage.** Distinguer **JIT** et **AOT** ; exploiter les **vérifications strictes** du compilateur ; configurer le builder `application` (budgets, hachage, optimisation) ; comprendre le **tree shaking** et écrire du code qui s'y prête ; appliquer les optimisations courantes (images, polices, styles, réseau) ; **analyser** un bundle ; utiliser une liste de contrôle de performance.

### 20.1 JIT et AOT

Le code Angular (décorateurs, gabarits HTML) **n'est pas directement exécutable** par un navigateur : il doit être **compilé** en JavaScript. Deux moments possibles :

|  | **JIT** (*Just-in-Time*) | **AOT** (*Ahead-of-Time*) |
| --- | --- | --- |
| Compilation | Dans le **navigateur**, à l'exécution | À la **construction** (build) |
| Taille | Compilateur embarqué (lourd) | **Plus léger** |
| Démarrage | Plus lent | **Plus rapide** |
| Erreurs de gabarit | À l'exécution | **Au build** |
| Statut | Rare (tests) | **Défaut** (`ng serve` et `ng build`) |

L'AOT fonctionne avec le moteur de compilation **Ivy** (par défaut depuis la v9), qui produit du code **ciblé** (chaque composant est compilé en instructions autonomes) et **tree-shakable** (le code inutile peut être supprimé).

**Ce que compile l'AOT.** Pour chaque composant, le compilateur transforme le **gabarit** en une fonction de **création** (construire le DOM la première fois) et une fonction de **mise à jour** (réévaluer les liaisons à chaque détection). Il vérifie les **types** dans les gabarits, résout les **dépendances** (`imports`) et signale les erreurs **avant** la mise en production.

### 20.2 Vérifications du compilateur

Les options du compilateur Angular se placent dans `angularCompilerOptions` de `tsconfig.json`.

```json
{ "angularCompilerOptions": { "strictTemplates": true, "strictInjectionParameters": true, "strictInputAccessModifiers": true,
                              "extendedDiagnostics": { "checks": { "optionalChainNotNullable": "error" } } } }
```

| Option | Effet |
| --- | --- |
| `strictTemplates` | Vérifie les gabarits **comme du TypeScript strict** (types des entrées, événements, expressions) |
| `strictInjectionParameters` | Erreur si un paramètre d'injection ne peut pas être résolu |
| `strictInputAccessModifiers` | Les entrées `private` / `protected` / `readonly` sont vérifiées |
| `extendedDiagnostics` | **Diagnostics supplémentaires**, configurables en `error`, `warning` ou `suppress` |

Le compilateur détecte : propriétés inexistantes dans les gabarits, types incompatibles, `@for` sans `track`, imports inutilisés dans `imports`, opérateurs `?.` inutiles sur des valeurs non nulles, liaisons bidirectionnelles mal formées (`[(x)]` invalide), tubes ou composants non importés. **Activez le mode le plus strict dès le départ** : l'ajouter plus tard coûte cher.

### 20.3 Le builder `application` (esbuild + Vite)

```jsonc
// angular.json (extrait)
{
    "projects": {
        "mon-app": {
            "architect": {
                "build": {
                    "builder": "@angular/build:application",
                    "options": {
                        "browser": "src/main.ts",
                        "server": "src/main.server.ts",         // si SSR
                        "outputMode": "static",                  // ou "server"
                        "polyfills": [],
                        "styles": ["src/styles.css"]
                    },
                    "configurations": {
                        "production": {
                            "budgets": [
                                { "type": "initial", "maximumWarning": "500kB", "maximumError": "1MB" },
                                { "type": "anyComponentStyle", "maximumWarning": "4kB", "maximumError": "8kB" }
                            ],
                            "outputHashing": "all"
                        }
                    }
                }
            }
        }
    }
}
```

| Option | Rôle |
| --- | --- |
| `budgets` | **Alerte ou échoue** si le bundle dépasse une taille (`initial`, `anyComponentStyle`, `bundle`, `allScript`, `any`) |
| `outputHashing` | Noms de fichiers avec **empreinte** (`main-A1B2C3.js`) : cache longue durée, invalidation automatique à chaque changement |
| `optimization` | Minification, suppression de code mort, *inlining* des polices et du CSS critique |
| `sourceMap` | Cartes sources (désactiver ou `hidden` en production : elles exposent votre code lisible) |
| `externalDependencies`, `prerender`, `ssr` | Options du builder |
| `outputMode` | `static` (fichiers statiques, pré-rendu possible) ou `server` (serveur Node pour le SSR) |
| `extractLicenses` | Génère un fichier `3rdpartylicenses.txt` |

**Cibles de compilation.** Le JavaScript produit cible les navigateurs listés dans le fichier **`.browserslistrc`** : plus la liste est récente, moins le code est transformé (plus petit, plus rapide). N'ajoutez des navigateurs anciens que si vos utilisateurs en ont réellement besoin.

**Polyfills.** Scripts qui comblent des fonctionnalités manquantes ; `polyfills: []` est suffisant dans un projet moderne zoneless.

**Les budgets, un garde-fou.** Une pull request qui fait passer le bundle initial de 400 Ko à 700 Ko déclenche un **avertissement**, puis une **erreur** au-delà du seuil : la dérive de taille est visible **tout de suite** plutôt que découverte en production.

### 20.4 Tree shaking et code mort

Le **tree shaking** (« secouer l'arbre ») supprime à la compilation le code **jamais utilisé**. Il repose sur les **modules ES** (`import` / `export` statiques), qui permettent de savoir ce qui est référencé.

```typescript
// Correct : importer précisément
import { debounce } from 'lodash-es';                // build ESM, tree-shakable
// Incorrect : import _ from 'lodash';                     // embarque toute la bibliothèque

const rechercher = debounce((terme: string) => console.log(`Recherche : ${terme}`), 300);
rechercher('angular');
```

| Pratique | Effet |
| --- | --- |
| `providedIn: 'root'` (services **tree-shakables**) | Un service jamais injecté n'est pas inclus |
| Composants **autonomes** et imports ciblés | Pas de modules entiers embarqués |
| Préférer des bibliothèques **ESM** (`lodash-es`, `date-fns`) | Meilleur élagage |
| Éviter les imports de **barils** massifs (`index.ts` qui réexporte tout) | Moins de code inutile |
| `sideEffects: false` dans le `package.json` de vos bibliothèques | Autorise l'élagage |
| Importer par sous-chemin quand c'est possible (`import { x } from 'lib/x'`) | Évite d'embarquer le reste |

**Code à effets de bord.** Un module qui fait quelque chose à l'import (modifier un objet global, enregistrer un écouteur) ne peut pas être élagué sans risque ; c'est pourquoi `sideEffects: false` doit rester **fidèle à la réalité**.

### 20.5 Optimisations fréquentes

| Domaine | Technique |
| --- | --- |
| **Images** | Directive **`NgOptimizedImage`** (`<img ngSrc="…" width height priority>`) : lazy-loading, `srcset`, évite le décalage de mise en page |
| **Polices** | Optimisation et *inlining* automatiques ; `font-display: swap` |
| **Styles** | CSS critique en ligne, composants à styles légers, budgets |
| **Dépendances** | Auditer avec `ng build --stats-json` ; remplacer les bibliothèques lourdes |
| **Rendu** | **SSR / pré-rendu** + hydratation (LCP), `@defer` |
| **Réseau** | Compression **Brotli / gzip**, **HTTP/2**, cache longue durée sur les fichiers hachés, **CDN** |
| **Zone.js** | Passer en **zoneless** |

```typescript
import { Component } from '@angular/core';
import { NgOptimizedImage } from '@angular/common';

@Component({
    selector: 'app-bannieres',
    imports: [NgOptimizedImage],
    template: `
        <img ngSrc="/img/hero.jpg" width="1200" height="600" priority alt="Bannière" />
        <img ngSrc="/img/produit.jpg" width="400" height="300" alt="Produit" />       <!-- paresseuse par défaut -->
    `,
})
export class Bannieres {}
```

**`NgOptimizedImage` en détail**

- **`width` et `height`** (ou `fill` pour remplir le conteneur) sont **obligatoires** : le navigateur réserve l'espace avant le chargement (**pas de décalage de mise en page**, bon CLS).
- **`priority`** : à réserver à l'image **LCP** (la plus grande visible au premier écran) ; elle est alors préchargée et n'est **pas** paresseuse. Ne l'utilisez pas pour toutes les images.
- Par défaut, les images sont chargées **paresseusement** (`loading="lazy"`) avec une priorité de récupération basse.
- **`sizes`** et **`srcset`** : adaptent l'image à la largeur d'affichage ; un **chargeur d'images** (`provideImgixLoader`, `provideCloudflareLoader`, `provideCloudinaryLoader`, etc., ou un chargeur personnalisé) génère les variantes via un CDN d'images.
- Fournit des **avertissements en développement** (image trop grande, `priority` manquant sur l'image LCP).
- Choisissez des formats modernes (**WebP**, **AVIF**) et dimensionnez les images à leur taille d'affichage réelle.

**Polices.** Hébergez-les vous-même ou laissez le builder **inliner** les feuilles de style de polices ; `font-display: swap` affiche un texte de secours en attendant la police (évite le texte invisible) ; `preload` pour les polices critiques ; sous-ensembles de caractères (`unicode-range`) pour limiter le poids.

**Cache HTTP.** Fichiers **hachés** (JS, CSS) : `Cache-Control: public, max-age=31536000, immutable`. `index.html` (non haché) : **cache court ou revalidation** (`no-cache`), afin que les nouvelles versions soient prises en compte.

### 20.6 Analyser le bundle

```bash
ng build --stats-json
npx esbuild-visualizer --metadata dist/mon-app/stats.json --open        # carte des dépendances
# ou : source-map-explorer dist/**/*.js
```

La **carte du bundle** (*treemap*) montre quelles dépendances pèsent le plus. Questions à se poser : une bibliothèque de dates entière est-elle embarquée pour un seul format ? Deux versions de la même bibliothèque coexistent-elles ? Des **locales** inutilisées sont-elles incluses ? Une bibliothèque de graphiques lourde pourrait-elle être **différée** (`@defer`, import dynamique) ?

**Mesures de référence** : taille **initiale** (ce que l'utilisateur doit télécharger pour voir la première page), taille **transférée** (après compression), poids de chaque *chunk* paresseux, **LCP / INP / CLS** réels (RUM) ou simulés (Lighthouse).

### 20.7 Liste de contrôle performance

- [ ] Composants `OnPush` + signaux, `track` dans les boucles
- [ ] Routes **paresseuses**, `@defer` pour le non-critique
- [ ] **Zoneless**
- [ ] SSR / pré-rendu + hydratation (+ incrémentale)
- [ ] `NgOptimizedImage`, polices optimisées
- [ ] Budgets définis, bundle surveillé en CI
- [ ] Compression et cache HTTP configurés
- [ ] `.browserslistrc` à jour, pas de polyfills superflus
- [ ] Aucune source map publique en production
- [ ] Dépendances auditées régulièrement (taille, maintenance, vulnérabilités)

### Synthèse du chapitre 20

L'**AOT** compile à la construction (Ivy, code tree-shakable, erreurs de gabarit détectées au build). Activez les **vérifications strictes**. Le builder `application` (esbuild + Vite) gère **budgets**, **hachage** et **optimisation**. Le **tree shaking** exige des **modules ES** et des bibliothèques ESM ; `NgOptimizedImage`, polices, cache HTTP et compression complètent. **Analysez** avant d'optimiser, **surveillez** en CI.

---

# Partie V — Essentiels

## 21. Internationalisation (i18n)

**Objectifs d'apprentissage.** Distinguer **internationalisation** et **localisation** ; choisir entre l'**i18n intégrée** (compilation) et les **bibliothèques d'exécution** ; marquer, extraire, traduire et construire par langue ; gérer pluriels et genres (format **ICU**) ; localiser dates, nombres et devises ; prendre en compte le **sens d'écriture** et l'expansion du texte.

### 21.1 Vocabulaire et deux approches

- **Internationalisation (i18n)** : concevoir l'application pour qu'elle **puisse** être adaptée à plusieurs langues et régions (« i », 18 lettres, « n »).
- **Localisation (l10n)** : adapter effectivement l'application à **une** langue / région (traductions, formats, images).
- **Locale** : identifiant de langue et de région (`fr`, `fr-FR`, `fr-CA`, `en-US`, `pt-BR`), qui détermine la langue, les formats de date, de nombre, de devise, les règles de pluriel.
- **ICU** (*International Components for Unicode*) : syntaxe standard pour les **pluriels** et les **sélections** (genre).

|  | **i18n intégrée d'Angular** (`$localize`) | **Bibliothèques d'exécution** (Transloco, ngx-translate) |
| --- | --- | --- |
| Traduction | **À la compilation** : un **build par langue** | **À l'exécution** : fichiers JSON, changement de langue à chaud |
| Performance | Excellente (texte déjà traduit) | Un peu moins (chargement des fichiers) |
| Changer de langue | Rechargement / autre URL | **Instantané** |
| Outils | XLIFF / XMB, extraction par le CLI | JSON, très simple |

### 21.2 i18n intégrée

```bash
ng add @angular/localize                 # active $localize
```

#### Marquer les textes

```typescript
import { Component, signal } from '@angular/core';

@Component({
    selector: 'app-accueil-i18n',
    template: `
        <h1 i18n="@@titreAccueil">Bienvenue sur notre site</h1>                       <!-- id explicite (@@) = stable -->
        <p i18n="Message d'accueil|Description pour le traducteur@@intro">Découvrez nos produits.</p>
        <img [src]="logo" i18n-alt alt="Logo de l'entreprise" />                      <!-- attribut -->
        <span i18n>Mise à jour {{ minutes() }} minutes plus tôt</span>
    `,
})
export class AccueilI18n {
    protected readonly logo = '/img/logo.png';
    protected readonly minutes = signal(5);
}
```

- **`i18n`** sur un élément marque son **contenu** ; **`i18n-xxx`** (`i18n-alt`, `i18n-title`, `i18n-aria-label`, `i18n-placeholder`) marque un **attribut**.
- La syntaxe complète est `i18n="signification|description@@identifiant"` : la **signification** distingue deux textes identiques de sens différents, la **description** guide le traducteur, l'**identifiant** (`@@clé`) rend la traduction **stable** (sans lui, un identifiant est dérivé du texte et change quand le texte change).
- **`<ng-container i18n>`** marque un groupe de texte sans ajouter d'élément ; les **interpolations** (`{{ minutes() }}`) deviennent des **paramètres** nommés dans le message traduit.

```typescript
// $localize est fourni par @angular/localize (ajouté par `ng add @angular/localize`)
const message = $localize`:@@erreurReseau:Impossible de joindre le serveur.`;     // dans le code TypeScript
console.error(message);
```

#### Pluriels et sélection (format ICU)

```typescript
import { Component, signal } from '@angular/core';

@Component({
    selector: 'app-messages-icu',
    template: `
        <span i18n>
            {nombre(), plural, =0 {Aucun message} =1 {Un message} other {{{ nombre() }} messages}}
        </span>

        <span i18n>
            {genre(), select, masculin {Il a répondu} feminin {Elle a répondu} other {Réponse reçue}}
        </span>
    `,
})
export class MessagesIcu {
    protected readonly nombre = signal(3);
    protected readonly genre = signal('feminin');
}
```

**Pourquoi ICU ?** Les règles de pluriel **varient** selon les langues : le français distingue peu (0 et 1 au singulier), l'anglais deux formes, le russe ou l'arabe jusqu'à **six** catégories (`zero`, `one`, `two`, `few`, `many`, `other`). Écrire `nombre + ' messages'` est faux dans de nombreuses langues ; ICU délègue la règle à la locale. Les cas `=0`, `=1` sont **exacts** ; `other` est **obligatoire**.

#### Extraire et traduire

```bash
ng extract-i18n --format xlf2 --output-path src/locale        # génère messages.xlf
# → copier en messages.fr.xlf, messages.en.xlf… et traduire les <target>
```

Le fichier **XLIFF** (format d'échange standard des outils de traduction) contient, pour chaque message, un `<source>` (texte d'origine) et, après copie, une balise `<target>` à renseigner. Les traducteurs travaillent avec des outils spécialisés (mémoires de traduction) ; vous pouvez aussi utiliser les formats XMB / JSON selon la version du CLI. Après chaque modification des textes, **réextrayez** et fusionnez avec les traductions existantes ; un message **manquant** déclenche un avertissement (ou une erreur selon `i18nMissingTranslation`).

#### Configurer les langues

```jsonc
// angular.json (extrait)
{
    "projects": {
        "mon-app": {
            "i18n": {
                "sourceLocale": "fr",
                "locales": { "en": "src/locale/messages.en.xlf", "es": "src/locale/messages.es.xlf" }
            },
            "architect": {
                "build": { "options": { "localize": true } }          // ou ["en", "es"]
            }
        }
    }
}
```

```bash
ng build --localize                  # un dossier par langue : dist/mon-app/browser/fr, en, es
ng serve --configuration=en          # servir une langue en développement
```

> Chaque langue est servie sous son propre chemin (`/fr/`, `/en/`) : configurez le serveur ou le CDN en conséquence (redirection selon l'en-tête `Accept-Language`, ou sélecteur de langue explicite). Pour le **référencement**, déclarez les versions alternatives avec des balises `hreflang` et définissez l'attribut `lang` de `<html>`.

### 21.3 Formats localisés

Les tubes `date`, `currency`, `number`, `percent` utilisent la **locale** active (`LOCALE_ID`). Avec l'i18n intégrée, la locale est fixée **par build** ; avec une bibliothèque d'exécution, on enregistre les données de locale et on fournit `LOCALE_ID`.

```typescript
// src/app/app.config.ts
import { ApplicationConfig, LOCALE_ID } from '@angular/core';
import { registerLocaleData } from '@angular/common';
import localeFr from '@angular/common/locales/fr';

registerLocaleData(localeFr);

export const appConfig: ApplicationConfig = {
    providers: [{ provide: LOCALE_ID, useValue: 'fr-FR' }],
};
```

```typescript
import { Component } from '@angular/core';
import { CurrencyPipe, DatePipe } from '@angular/common';

@Component({
    selector: 'app-formats',
    imports: [CurrencyPipe, DatePipe],
    template: `
        <p>{{ 1234.5 | currency: 'EUR' }}</p>     <!-- 1 234,50 € -->
        <p>{{ date | date: 'fullDate' }}</p>      <!-- dimanche 11 octobre 2026 -->
    `,
})
export class Formats {
    protected readonly date = new Date(2026, 9, 11);
}
```

Pour d'autres besoins : l'API **`Intl`** du navigateur (`Intl.NumberFormat`, `Intl.DateTimeFormat`, `Intl.RelativeTimeFormat`, `Intl.PluralRules`, `Intl.ListFormat`), sans dépendance supplémentaire.

**Pièges de formats.** Séparateurs décimaux et de milliers (virgule / point), ordre jour-mois-année, **fuseaux horaires** (afficher dans le fuseau de l'utilisateur, stocker en UTC), devise **distincte** de la langue (un utilisateur français peut voir des prix en dollars), premier jour de la semaine, calendriers non grégoriens.

### 21.4 Traduction à l'exécution avec Transloco *(ajout)*

```bash
ng add @jsverse/transloco
```

```jsonc
// src/assets/i18n/fr.json
{ "accueil": { "titre": "Bienvenue", "salutation": "Bonjour {{ nom }}" } }
```

```jsonc
// src/assets/i18n/en.json
{ "accueil": { "titre": "Welcome", "salutation": "Hello {{ nom }}" } }
```

```typescript
import { Component, inject, signal } from '@angular/core';
import { TranslocoPipe, TranslocoService } from '@jsverse/transloco';

@Component({
    selector: 'app-accueil-transloco',
    imports: [TranslocoPipe],
    template: `
        <h1>{{ 'accueil.titre' | transloco }}</h1>
        <p>{{ 'accueil.salutation' | transloco: { nom: utilisateur() } }}</p>
        <button (click)="changerLangue('fr')">FR</button>
        <button (click)="changerLangue('en')">EN</button>
    `,
})
export class AccueilTransloco {
    private readonly transloco = inject(TranslocoService);
    protected readonly utilisateur = signal('Alice');

    protected changerLangue(l: string): void { this.transloco.setActiveLang(l); }
}
```

`ng add @jsverse/transloco` génère la configuration (langues disponibles, langue par défaut, chargeur de fichiers JSON) ; les **clés** hiérarchiques (`accueil.titre`) organisent les traductions ; les **paramètres** (`{{ nom }}`) évitent la concaténation ; le **chargement paresseux** de fichiers par fonctionnalité limite le volume initial. Alternatives : **ngx-translate** (très répandue), **Lingui**.

### 21.5 Choisir et bonnes pratiques

| Besoin | Choix |
| --- | --- |
| Performance maximale, langues fixes, SEO par URL | **i18n intégrée** |
| Changement de langue **instantané**, textes dynamiques | **Transloco / ngx-translate** |

- **Ne concaténez jamais** des fragments traduits : utilisez des **paramètres** ou le format ICU (l'ordre des mots change d'une langue à l'autre).
- Prévoyez **l'expansion du texte** (l'allemand est plus long, jusqu'à +30 à 40 %) et le **sens d'écriture** (RTL : arabe, hébreu → `dir="rtl"`, propriétés CSS logiques comme `margin-inline-start`).
- Utilisez des **identifiants explicites** (`@@clé`) pour des traductions stables.
- Traduisez aussi `title`, `alt`, `aria-label`, **messages d'erreur** et **titres de pages** (routeur).
- N'intégrez **pas de texte dans les images** ; ne codez **pas de chaînes en dur** dans le TypeScript sans `$localize`.
- Prévoyez des **pseudo-traductions** (texte allongé, accentué) pour détecter tôt les débordements.
- Testez au moins **une langue longue** et **une langue RTL**.

### Synthèse du chapitre 21

Deux approches : **i18n intégrée** (`i18n`, `$localize`, extraction XLIFF, un build par langue, performance maximale) ou **bibliothèque d'exécution** (Transloco, ngx-translate : JSON, changement instantané). Utilisez **ICU** pour pluriels et genres, `LOCALE_ID` + tubes pour les formats, des **identifiants stables**, et anticipez **expansion** et **RTL**.

---

## 22. Rendu côté serveur (SSR), pré-rendu et hydratation

**Objectifs d'apprentissage.** Comparer **CSR**, **SSR**, **SSG** et **hydratation** ; activer et configurer le SSR ; choisir le **mode de rendu par route** ; maîtriser l'**hydratation** (relecture d'événements, hydratation incrémentale) ; écrire du code **compatible serveur** ; gérer SEO, cache de transfert, erreurs d'hydratation et **sécurité**.

### 22.1 Pourquoi rendre côté serveur ?

Une SPA classique (**CSR**) envoie un `index.html` quasiment vide : le navigateur télécharge le JavaScript, l'exécute, puis construit la page. Pendant ce temps l'utilisateur voit un écran blanc, et certains robots (réseaux sociaux, moteurs de recherche) n'exécutent pas le JavaScript. Le rendu serveur résout ces deux problèmes en envoyant du **HTML déjà construit**.

| Mode | Principe | Avantages | Inconvénients |
| --- | --- | --- | --- |
| **CSR** (*client-side rendering*) | Le navigateur construit la page | Simple, hébergement **statique** | Premier affichage lent, SEO limité |
| **SSR** (*server-side rendering*) | Le serveur renvoie du **HTML complet** à **chaque requête** | **SEO**, **LCP** plus rapide, aperçus sociaux corrects | Serveur Node à exploiter, coût par requête |
| **SSG / pré-rendu** (*prerender*) | HTML généré **au build** pour des routes **connues** | Très rapide, **hébergement statique**, SEO | Contenu figé jusqu'au prochain build |
| **Hydratation** | Le navigateur **réutilise** le HTML serveur et l'« active » | Évite scintillement et reconstruction | Exige un HTML identique des deux côtés |

> **À jour.** **Angular Universal** (`@nguniversal/*`) est **abandonné** ; le SSR est **intégré au CLI** (`@angular/ssr`) et au builder `application`.

**Que se passe-t-il, concrètement ?** (1) Le navigateur demande `/produits/42`. (2) Le serveur exécute l'application Angular **dans Node**, résout la route, charge les données, produit le HTML. (3) Le navigateur affiche **immédiatement** ce HTML. (4) Le JavaScript se charge, Angular **s'hydrate** : il s'attache au DOM existant, branche les écouteurs et reprend la main. (5) La navigation suivante est celle d'une SPA normale.

### 22.2 Activer le SSR

```bash
ng new mon-app --ssr                  # nouveau projet
ng add @angular/ssr                   # projet existant
```

L'ajout crée notamment : `server.ts` (serveur Node, Express par défaut), `main.server.ts`, `app.config.server.ts`, `app.routes.server.ts`, et modifie `angular.json` (cible `server`, `outputMode`).

```typescript
// src/app/app.config.ts
import { ApplicationConfig } from '@angular/core';
import { provideHttpClient, withFetch } from '@angular/common/http';
import { provideClientHydration, withEventReplay, withIncrementalHydration } from '@angular/platform-browser';

export const appConfig: ApplicationConfig = {
    providers: [
        provideClientHydration(withEventReplay(), withIncrementalHydration()),
        provideHttpClient(withFetch()),                       // fetch fonctionne côté serveur
    ],
};
```

```typescript
// src/app/app.config.server.ts : configuration propre au serveur, fusionnée avec la précédente
import { ApplicationConfig, mergeApplicationConfig } from '@angular/core';
import { provideServerRendering, withRoutes } from '@angular/ssr';
import { appConfig } from './app.config';
import { serverRoutes } from './app.routes.server';

const configServeur: ApplicationConfig = {
    providers: [provideServerRendering(withRoutes(serverRoutes))],
};

export const config = mergeApplicationConfig(appConfig, configServeur);
```

#### Mode de rendu **par route**

```typescript
// src/app/app.routes.server.ts
import { RenderMode, ServerRoute } from '@angular/ssr';

async function listerIds(): Promise<number[]> {
    return [1, 2, 3];                                                     // en pratique : lecture d'une API ou d'un fichier
}

export const serverRoutes: ServerRoute[] = [
    { path: '', renderMode: RenderMode.Prerender },                      // généré au build
    {
        path: 'produits/:id',
        renderMode: RenderMode.Prerender,
        async getPrerenderParams() { return (await listerIds()).map((id) => ({ id: String(id) })); },   // liste des pages à générer
    },
    { path: 'compte', renderMode: RenderMode.Client },                    // uniquement côté client (zone privée)
    { path: '**', renderMode: RenderMode.Server },                        // rendu à chaque requête
];
```

| `RenderMode` | Usage |
| --- | --- |
| `Prerender` | Pages **publiques stables** (accueil, fiches, articles) |
| `Server` | Contenu **dynamique** ou personnalisé par requête |
| `Client` | Zones **privées**, très interactives ou non référencées |

`getPrerenderParams()` fournit, pour une route à paramètres, l'**ensemble des valeurs** à pré-rendre ; sans elle, une route paramétrée ne peut pas être pré-rendue. Le pré-rendu s'exécute pendant `ng build`.

```bash
ng build                              # produit les pages pré-rendues et/ou le serveur
node dist/mon-app/server/server.mjs   # lance le serveur SSR (variable PORT possible)
```

#### Le serveur Node (`server.ts`)

```typescript
// server.ts (généré par le CLI, simplifié)
import { AngularNodeAppEngine, createNodeRequestHandler, isMainModule, writeResponseToNodeResponse } from '@angular/ssr/node';
import express from 'express';
import { join } from 'node:path';

const dossierNavigateur = join(import.meta.dirname, '../browser');
const app = express();
const angularApp = new AngularNodeAppEngine();

app.use(express.static(dossierNavigateur, { maxAge: '1y', index: false, redirect: false }));    // fichiers statiques hachés
app.use((req, res, next) => {
    angularApp.handle(req).then((reponse) => (reponse ? writeResponseToNodeResponse(reponse, res) : next())).catch(next);
});

if (isMainModule(import.meta.url)) {
    const port = process.env['PORT'] || 4000;
    app.listen(port, () => console.log(`Serveur démarré sur http://localhost:${port}`));
}
export const reqHandler = createNodeRequestHandler(app);       // utilisé par certains hébergeurs sans serveur
```

Vous pouvez **ajouter** vos propres routes Express (API, authentification, redirections) **avant** le gestionnaire Angular. Le serveur est aussi déployable en **fonctions sans serveur** (`reqHandler`) selon l'hébergeur.

### 22.3 Hydratation

L'**hydratation** associe le DOM déjà rendu par le serveur à l'application Angular, au lieu de le **détruire et reconstruire** : plus de scintillement, de perte de focus ni de saut de mise en page, et un LCP préservé.

| Fonctionnalité | Rôle |
| --- | --- |
| `provideClientHydration()` | Active l'hydratation |
| `withEventReplay()` | **Rejoue** les clics et saisies faits **avant** la fin de l'hydratation |
| `withIncrementalHydration()` | Hydrate par **zones** différées : `@defer (hydrate on viewport) { … }` |
| `withHttpTransferCacheOptions(…)` | Règle le **cache de transfert** des requêtes HTTP |
| `ngSkipHydration` | Exclut un composant incompatible (manipulation directe du DOM) |

**Hydratation incrémentale.** Une zone `@defer` peut être **rendue côté serveur immédiatement** mais **activée** plus tard, à un moment choisi : `hydrate on viewport`, `on interaction`, `on hover`, `on idle`, `on immediate`, `on timer(…)`, `when condition`, ou `hydrate never` (zone purement statique, jamais hydratée). Le JavaScript de la zone n'est téléchargé qu'au moment de l'hydratation : **moins de code au démarrage** et un meilleur INP.

```typescript
// src/app/discussion.ts
import { Component } from '@angular/core';
import { Commentaires } from './commentaires';

@Component({
    selector: 'app-discussion',
    imports: [Commentaires],
    template: `
        @defer (hydrate on interaction) {
            <app-commentaires />                     <!-- rendu serveur immédiat, activation au premier clic -->
        } @placeholder { <p>Commentaires</p> }
    `,
})
export class Discussion {}
```

**Erreurs d'hydratation.** Si le HTML du navigateur **ne correspond pas** à celui du serveur (erreurs NG05xx), Angular le signale en développement et peut reconstruire la zone fautive. Causes fréquentes :

- **HTML invalide** (un `<div>` dans un `<p>`, un `<table>` sans `<tbody>`…) que le navigateur corrige différemment ;
- **manipulation directe du DOM** (`innerHTML`, bibliothèques tierces) ;
- contenu **différent** entre serveur et client (date `new Date()`, `Math.random()`, `window.innerWidth`).

Correction : HTML valide, **état déterministe**, DOM modifié seulement dans `afterNextRender`. En dernier recours, `ngSkipHydration` sur l'élément.

### 22.4 Écrire du code compatible SSR

Côté serveur, `window`, `document`, `localStorage`, `navigator`… **n'existent pas**.

```typescript
// src/app/carte.ts
import { Component, PLATFORM_ID, afterNextRender, inject } from '@angular/core';
import { DOCUMENT, isPlatformBrowser } from '@angular/common';

@Component({
    selector: 'app-carte',
    template: `<div id="carte"></div>`,
})
export class Carte {
    private readonly plateforme = inject(PLATFORM_ID);
    private readonly document = inject(DOCUMENT);               // au lieu de la globale `document`

    constructor() {
        afterNextRender(() => {                                  // exécuté UNIQUEMENT dans le navigateur
            const conteneur = this.document.getElementById('carte');
            console.log('Initialisation de la carte dans', conteneur);
        });
        if (isPlatformBrowser(this.plateforme)) {
            console.log(localStorage.getItem('theme'));
        }
    }
}
```

| À faire | Pourquoi |
| --- | --- |
| `afterNextRender` / `afterEveryRender` pour le code lié au DOM | Jamais exécutés sur le serveur |
| `inject(DOCUMENT)` plutôt que la globale `document` | Document **simulé** côté serveur |
| `isPlatformBrowser(plateforme)` pour du code spécifique | Branche explicite |
| Éviter `setInterval` / minuteries longues au démarrage | Elles empêchent l'application d'être jugée **stable** et retardent la réponse |
| Bibliothèques tierces : vérifier la compatibilité SSR, les charger dans `afterNextRender` (import dynamique) | Beaucoup touchent `window` à l'import |

**Stabilité.** Le serveur attend que l'application soit **stable** (plus de requêtes HTTP ni de tâches en attente) avant de sérialiser le HTML. Une tâche asynchrone non suivie risque d'être **omise** du rendu ; une tâche qui ne se termine jamais **bloque** la réponse.

**Cache de transfert HTTP.** Les requêtes `HttpClient` (GET / HEAD) effectuées **côté serveur** sont sérialisées dans la page ; au démarrage, le navigateur **réutilise** ces réponses au lieu de les redemander. Ajustable via `withHttpTransferCacheOptions`. L'état applicatif arbitraire se transfère avec `TransferState`.

**Accès à la requête côté serveur.** Pour lire les en-têtes ou les cookies de la requête entrante (langue, session), Angular fournit des jetons d'injection dédiés (`REQUEST`, `RESPONSE_INIT`, `REQUEST_CONTEXT`) disponibles **uniquement sur le serveur** : injectez-les avec `{ optional: true }` et vérifiez leur existence ; consultez la documentation de votre version pour l'import exact.

**Titre et métadonnées (SEO).** Services `Title` et `Meta` ; balises Open Graph pour les aperçus sociaux.

```typescript
// src/app/produit-seo.ts
import { Component, inject } from '@angular/core';
import { Meta, Title } from '@angular/platform-browser';

@Component({
    selector: 'app-produit-seo',
    template: `<h1>Produit</h1>`,
})
export class ProduitSeo {
    constructor() {
        inject(Title).setTitle('Produit — Ma boutique');
        inject(Meta).updateTag({ name: 'description', content: 'Description du produit' });
        inject(Meta).updateTag({ property: 'og:title', content: 'Produit — Ma boutique' });
    }
}
```

Pensez aussi à : URL **canonique**, `sitemap.xml`, `robots.txt`, **codes de statut** corrects (404 réel pour une page introuvable, non un 200 avec un message), données structurées (JSON-LD).

### 22.5 Bonnes pratiques et sécurité

- **Pré-rendez** les pages publiques stables, utilisez le **SSR** pour le contenu dynamique, le **CSR** pour les zones privées.
- **Ne mettez pas de secrets** dans du code exécuté côté client : tout ce qui est dans le bundle du navigateur est public. Les variables d'environnement **serveur** restent côté serveur.
- **Ne fuyez pas de données utilisateur entre requêtes** : un singleton (`providedIn: 'root'`) est créé **par requête** côté serveur dans Angular SSR, mais une **variable globale de module** (hors Angular) est **partagée** entre toutes les requêtes. Pas d'état utilisateur dans des globales.
- **Contrôlez les en-têtes** (`Host`, `X-Forwarded-*`) : une application SSR qui fait confiance à l'hôte annoncé par la requête s'expose à l'**empoisonnement de l'hôte** et à la **SSRF**. Configurez la liste des **hôtes autorisés** (option de sécurité du builder / du moteur SSR, voir la documentation de votre version) et placez le serveur derrière un proxy qui normalise ces en-têtes.
- **Cookies et authentification** : transmettez-les explicitement aux requêtes serveur → API ; ne mettez pas en cache de réponses personnalisées dans un CDN partagé.
- Surveillez le **TTFB** (temps jusqu'au premier octet) : un SSR lent est pire qu'un CSR. Mettez en cache les pages communes (CDN, `Cache-Control`).
- Mesurez **LCP**, **TTFB**, **INP** ; testez avec le JavaScript désactivé pour valider le HTML initial.

### Synthèse du chapitre 22

**CSR** (simple), **SSR** (HTML à chaque requête, SEO et LCP), **SSG / pré-rendu** (HTML au build), **hydratation** (réutiliser le HTML, `withEventReplay`, hydratation **incrémentale** par `@defer (hydrate …)`). Mode de rendu **par route** (`RenderMode`). Code **compatible serveur** : `afterNextRender`, `DOCUMENT`, pas de globales navigateur. SEO par `Title` / `Meta`, **cache de transfert**, **hôtes autorisés** et **aucun état utilisateur partagé**.

---

## 23. Applications web progressives (PWA)

**Objectifs d'apprentissage.** Définir une **PWA** et ses composants ; ajouter le support avec `@angular/pwa` ; configurer le **cache** (`ngsw-config.json`) ; gérer les **mises à jour** et les **notifications push** ; concevoir l'expérience **hors ligne** ; tester et déboguer ; éviter les pièges.

### 23.1 Qu'est-ce qu'une PWA ?

Une **PWA** (*Progressive Web App*) est une application web qui se comporte comme une application native : **installable** sur l'écran d'accueil, **utilisable hors ligne** ou sur réseau instable, capable de recevoir des **notifications push**. Elle repose sur un **Service Worker** et un **manifeste**.

| Élément | Rôle |
| --- | --- |
| **HTTPS** | Obligatoire (sauf `localhost`) : un Service Worker intercepte tout le trafic, il doit être sûr |
| **Manifeste** (`manifest.webmanifest`) | Nom, icônes, couleurs, mode d'affichage, URL de démarrage (installation) |
| **Service Worker** | Script exécuté **en arrière-plan**, **proxy** entre le navigateur et le réseau : cache, hors ligne, push, synchronisation |

**Cycle de vie d'un Service Worker.** *Enregistrement* (la page demande son installation) → *installation* (il télécharge et met en cache les ressources) → *activation* (il prend le contrôle) → *interception* (événement `fetch` pour chaque requête). Une **nouvelle version** s'installe en parallèle de l'ancienne et ne s'active que lorsque plus aucun onglet ne l'utilise (ou sur demande explicite).

**Le Service Worker d'Angular (`ngsw`).** Angular fournit un Service Worker **déclaratif** : on décrit **quoi** mettre en cache dans `ngsw-config.json`, et le build génère le script correspondant avec les **empreintes** des fichiers. Il gère le **versionnement de l'application** : tous les fichiers d'un même build sont servis ensemble, jamais mélangés avec ceux d'un autre build.

### 23.2 Ajouter le support PWA

```bash
ng add @angular/pwa
```

Ajoute : `manifest.webmanifest`, **icônes**, `ngsw-config.json`, balises `<link rel="manifest">` et `theme-color` dans `index.html`, la dépendance `@angular/service-worker`, et le fournisseur :

```typescript
// src/app/app.config.ts
import { ApplicationConfig, isDevMode } from '@angular/core';
import { provideServiceWorker } from '@angular/service-worker';

export const appConfig: ApplicationConfig = {
    providers: [
        provideServiceWorker('ngsw-worker.js', {
            enabled: !isDevMode(),                              // actif seulement en production
            registrationStrategy: 'registerWhenStable:30000',   // s'enregistre quand l'application est stable, ou après 30 s
        }),
    ],
};
```

**Le manifeste**

```json
{
    "name": "Ma boutique",
    "short_name": "Boutique",
    "start_url": "/",
    "display": "standalone",
    "background_color": "#ffffff",
    "theme_color": "#1976d2",
    "icons": [
        { "src": "icons/icon-192x192.png", "sizes": "192x192", "type": "image/png", "purpose": "any" },
        { "src": "icons/icon-512x512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
    ]
}
```

`display: standalone` retire la barre d'adresse ; les icônes **maskable** s'adaptent aux formes d'icônes des systèmes ; `short_name` s'affiche sous l'icône.

### 23.3 Configurer le cache : `ngsw-config.json`

```json
{
    "index": "/index.html",
    "assetGroups": [
        { "name": "app", "installMode": "prefetch", "resources": { "files": ["/favicon.ico", "/index.html", "/*.css", "/*.js"] } },
        { "name": "assets", "installMode": "lazy", "updateMode": "prefetch", "resources": { "files": ["/assets/**", "/*.(svg|png|jpg|webp|woff2)"] } }
    ],
    "dataGroups": [
        { "name": "api", "urls": ["/api/**"],
          "cacheConfig": { "strategy": "freshness", "maxSize": 100, "maxAge": "1h", "timeout": "5s" } }
    ]
}
```

**Groupes de ressources (`assetGroups`)** : fichiers **versionnés** avec l'application. `installMode: 'prefetch'` télécharge tout à l'installation ; `'lazy'` seulement à la première utilisation. `updateMode` règle le comportement lors d'une mise à jour.

**Groupes de données (`dataGroups`)** : requêtes **d'API**, non versionnées avec l'application, avec une `cacheConfig` :

| Stratégie | Comportement | Usage |
| --- | --- | --- |
| `freshness` | **Réseau d'abord**, cache en secours après un délai (`timeout`) | Données qui doivent être à jour (commandes, solde) |
| `performance` | **Cache d'abord**, réseau en rafraîchissement selon `maxAge` | Données stables (catalogue, références) |

`maxSize` limite le nombre d'entrées, `maxAge` la durée de validité. **Ne mettez pas en cache** de réponses personnelles ou sensibles dans un cache partagé ; vous pouvez exclure une requête du Service Worker en ajoutant le paramètre `ngsw-bypass` à son URL (ou l'en-tête `ngsw-bypass`).

**Navigation hors ligne.** `navigationUrls` indique quelles URL de navigation renvoient `index.html` (SPA) ; la page de repli hors ligne est donc l'application elle-même, qui doit **afficher un état adapté** (voir 23.5).

### 23.4 Mises à jour et notifications

```typescript
// src/app/mises-a-jour.ts
import { Component, inject } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { SwUpdate, VersionReadyEvent, SwPush } from '@angular/service-worker';
import { filter } from 'rxjs';

const CLE_VAPID_PUBLIQUE = 'REMPLACER_PAR_VOTRE_CLE_VAPID_PUBLIQUE';        // générée côté serveur

@Component({
    selector: 'app-mises-a-jour',
    template: `<button (click)="abonnerPush()">Activer les notifications</button>`,
})
export class MisesAJour {
    private readonly maj = inject(SwUpdate);
    private readonly push = inject(SwPush);

    constructor() {
        this.maj.versionUpdates
            .pipe(filter((e): e is VersionReadyEvent => e.type === 'VERSION_READY'), takeUntilDestroyed())
            .subscribe(() => {
                if (confirm('Nouvelle version disponible. Recharger ?')) document.location.reload();
            });
        this.maj.checkForUpdate().catch((erreur) => console.error('Vérification impossible', erreur));
    }

    protected async abonnerPush(): Promise<void> {
        const abonnement = await this.push.requestSubscription({ serverPublicKey: CLE_VAPID_PUBLIQUE });
        await fetch('/api/push/abonner', { method: 'POST', body: JSON.stringify(abonnement) });
    }
}
```

**Cycle d'une mise à jour.** Le Service Worker **vérifie** périodiquement (à chaque démarrage et à la demande par `checkForUpdate()`) si un nouveau build existe, le **télécharge en arrière-plan** (événements `VERSION_DETECTED`, puis `VERSION_READY`). L'utilisateur continue sur l'ancienne version jusqu'au rechargement, ce qui évite de mélanger deux versions dans un même onglet. `activateUpdate()` force l'activation. Le flux `unrecoverable` signale un état irrécupérable (fichier manquant sur le serveur) : **rechargez la page**.

**Notifications push.** Le serveur envoie un message à un **service de push** du navigateur, qui le remet au Service Worker, même **application fermée**. Étapes : (1) générer une paire de clés **VAPID** côté serveur ; (2) demander la **permission** de l'utilisateur et l'**abonnement** (`SwPush.requestSubscription`) ; (3) envoyer l'abonnement à **votre** serveur ; (4) le serveur envoie les notifications ; (5) `SwPush.notificationClicks` et `messages` permettent de réagir côté application.

> **Bonnes pratiques push.** Demandez la permission **après une action explicite** de l'utilisateur (pas au chargement de la page) et expliquez la valeur du service ; limitez la fréquence ; offrez un moyen simple de se désabonner.

**Installation.** Les navigateurs proposent l'installation selon leurs critères (manifeste valide, HTTPS, Service Worker). On peut capter l'événement `beforeinstallprompt` (non standard, absent de certains navigateurs) pour afficher un bouton « Installer » personnalisé.

### 23.5 Concevoir l'expérience hors ligne

Le Service Worker sert l'**application** hors ligne ; mais vos **données** et vos **actions** doivent aussi y être préparées :

- **Détecter** la connexion (événements `online` / `offline`, `navigator.onLine`) et l'afficher (bandeau « Hors ligne ») ; exposer l'état dans un **signal**.
- **Lectures** : cache de données (`dataGroups`) ou stockage local (**IndexedDB**, via une bibliothèque) pour consulter l'essentiel.
- **Écritures** : placer les actions dans une **file d'attente** locale et les **rejouer** au retour de la connexion ; gérer les **conflits** (même ressource modifiée ailleurs). Angular ne fournit pas de *Background Sync* clé en main : il faut l'implémenter (ou utiliser une bibliothèque, ou un Service Worker personnalisé).
- **Messages clairs** : « Cette action sera envoyée dès que vous serez connecté. »

```typescript
// src/app/reseau.ts : état de connexion exposé en signal
import { Injectable, signal } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class Reseau {
    private readonly _enLigne = signal(typeof navigator === 'undefined' ? true : navigator.onLine);   // compatible SSR
    readonly enLigne = this._enLigne.asReadonly();

    constructor() {
        if (typeof window !== 'undefined') {
            window.addEventListener('online', () => this._enLigne.set(true));
            window.addEventListener('offline', () => this._enLigne.set(false));
        }
    }
}
```

### 23.6 Tester et déboguer

Le Service Worker n'est **pas actif** avec `ng serve` (désactivé en développement). Il faut **construire** puis **servir** le résultat :

```bash
ng build
npx http-server -p 8080 -c-1 dist/mon-app/browser
```

Puis **DevTools → Application** : onglets *Service Workers* (état, mise à jour forcée, « Offline »), *Manifest* (validité, installabilité), *Cache Storage* (contenu des caches). **Lighthouse** audite l'installabilité. L'adresse `/ngsw/state` (sur l'origine servie) affiche l'état interne du Service Worker d'Angular : version active, ressources mises en cache, erreurs. Pour repartir de zéro : *Application → Storage → Clear site data* et désenregistrer le Service Worker.

### 23.7 Bonnes pratiques et pièges

- Servir en **HTTPS**, fournir des **icônes** 192 et 512 px (dont une **maskable**).
- Ne **jamais** mettre en cache `index.html` de façon à ce qu'il ne se mette plus à jour : laissez `ngsw` gérer les versions et **fournissez une UX de mise à jour** claire.
- Adapter la **stratégie de cache** par type de ressource (`freshness` pour le dynamique, `performance` pour le stable).
- Ne pas mettre en cache de données **sensibles** ; prévoir l'**invalidation à la déconnexion** (vider caches et stockage local).
- Après un changement d'API incompatible, prévoir la **purge** ou le versionnement des caches de données.
- Un Service Worker **bloqué** sur une ancienne version est un classique : testez le scénario « nouvelle version publiée pendant qu'un utilisateur utilise l'application ».
- Pas de Service Worker en développement : ne vous fiez pas à `ng serve` pour valider le hors ligne.

### Synthèse du chapitre 23

Une PWA = **HTTPS** + **manifeste** + **Service Worker**. `ng add @angular/pwa` + `provideServiceWorker` ; le cache se déclare dans **`ngsw-config.json`** (`assetGroups` versionnés, `dataGroups` avec `freshness` / `performance`). `SwUpdate` pilote les mises à jour, `SwPush` les notifications. L'expérience **hors ligne** se conçoit (détection, file d'attente, messages). Test en **build** servi, jamais avec `ng serve`.

---

## 24. Angular Material, CDK et Aria

**Objectifs d'apprentissage.** Distinguer **Angular Material**, le **CDK** et **Angular Aria** et choisir selon le besoin ; installer et thématiser Material (Material Design 3) ; utiliser les composants courants (formulaires, tables, dialogues, notifications, navigation) ; exploiter les briques du CDK (défilement virtuel, glisser-déposer, *overlay*, point de rupture, accessibilité) ; comprendre l'approche d'Aria ; tester avec les **harnais**.

### 24.1 Les trois bibliothèques

Google maintient, à côté du framework, trois bibliothèques d'interface **complémentaires**, de la plus « habillée » à la plus « nue » :

| Bibliothèque | Contenu | Quand l'utiliser |
| --- | --- | --- |
| **Angular Material** | Composants d'interface **stylés** selon **Material Design 3** (boutons, champs, tables, dialogues, menus…) | Vous voulez une interface cohérente et complète, vite |
| **Angular CDK** (*Component Dev Kit*) | **Briques de comportement sans style** : *overlay*, glisser-déposer, défilement virtuel, accessibilité, observateurs | Vous construisez **vos propres** composants et voulez réutiliser les mécanismes difficiles |
| **Angular Aria** *(stable en v22)* | **Primitives accessibles non stylées** (combobox, listbox, menu, onglets, accordéon, arbre, grille) | Vous avez un **design system** à vous et voulez une accessibilité **correcte par construction** |

**Relations.** Material est **construit sur** le CDK ; Aria fournit les **comportements ARIA** (clavier, rôles, focus) que vous habillez vous-même. Vous pouvez mélanger les trois dans une même application.

### 24.2 Installer Angular Material

```bash
ng add @angular/material
```

Le schematic installe `@angular/material` et `@angular/cdk`, vous propose un **thème** (couleurs prédéfinies), configure la **typographie** (police Roboto), les **icônes** (Material Symbols) et les styles globaux. Pour les animations, les versions récentes n'exigent plus `provideAnimationsAsync()` (les composants utilisent des animations CSS) ; si votre version les demande encore, le schematic l'ajoute.

### 24.3 Utiliser les composants

Chaque composant Material est **autonome** (ou fourni via un module à importer) : on n'importe **que ce que l'on utilise**, ce qui garde le bundle léger.

```typescript
// src/app/profil.ts
import { Component, inject, signal } from '@angular/core';
import { FormControl, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatTableModule } from '@angular/material/table';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
    selector: 'app-profil',
    imports: [MatButtonModule, MatCardModule, MatFormFieldModule, MatInputModule, MatTableModule, ReactiveFormsModule],
    template: `
        <mat-card>
            <mat-card-header><mat-card-title>Profil</mat-card-title></mat-card-header>
            <mat-card-content>
                <mat-form-field appearance="outline">
                    <mat-label>Nom</mat-label>
                    <input matInput [formControl]="nom" />
                    @if (nom.hasError('required')) { <mat-error>Le nom est obligatoire</mat-error> }
                </mat-form-field>
            </mat-card-content>
            <mat-card-actions><button mat-flat-button (click)="enregistrer()">Enregistrer</button></mat-card-actions>
        </mat-card>

        <table mat-table [dataSource]="lignes()">
            <ng-container matColumnDef="nom">
                <th mat-header-cell *matHeaderCellDef>Nom</th>
                <td mat-cell *matCellDef="let l">{{ l.nom }}</td>
            </ng-container>
            <tr mat-header-row *matHeaderRowDef="colonnes"></tr>
            <tr mat-row *matRowDef="let ligne; columns: colonnes"></tr>
        </table>
    `,
})
export class Profil {
    private readonly barre = inject(MatSnackBar);
    protected readonly nom = new FormControl('', { nonNullable: true, validators: [Validators.required] });
    protected readonly colonnes = ['nom'];
    protected readonly lignes = signal([{ nom: 'Alice' }]);

    protected enregistrer(): void {
        this.barre.open('Enregistré !', 'OK', { duration: 3000 });
    }
}
```

**Composants courants :** `mat-toolbar`, `mat-sidenav`, `mat-list`, `mat-select`, `mat-checkbox`, `mat-radio`, `mat-slide-toggle`, `mat-datepicker`, `mat-autocomplete`, `mat-paginator`, `mat-sort`, `mat-tabs`, `mat-stepper`, `mat-expansion-panel`, `mat-menu`, `mat-tooltip`, `mat-chips`, `mat-progress-bar`, `mat-progress-spinner`, `mat-badge`, `mat-icon`, `mat-dialog`, `mat-snack-bar`, `mat-bottom-sheet`.

**Boutons** : plusieurs variantes selon l'importance de l'action (`mat-button` texte, `mat-flat-button` plein, `mat-stroked-button` contour, `mat-icon-button`, `mat-fab`).

**Champs de formulaire** : `mat-form-field` enveloppe un contrôle (`matInput`, `mat-select`…), lui ajoute le libellé flottant (`mat-label`), l'aide (`mat-hint`) et les erreurs (`mat-error`, affichées quand le contrôle est invalide et touché). Il fonctionne avec les formulaires réactifs et `ngModel`.

#### Boîte de dialogue

```typescript
// src/app/confirmation.ts
import { Component, inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';

@Component({
    selector: 'app-confirmation',
    imports: [MatDialogModule, MatButtonModule],
    template: `
        <h2 mat-dialog-title>Supprimer « {{ donnees.nom }} » ?</h2>
        <mat-dialog-content>Cette action est définitive.</mat-dialog-content>
        <mat-dialog-actions>
            <button mat-button mat-dialog-close>Annuler</button>
            <button mat-flat-button [mat-dialog-close]="true">Supprimer</button>
        </mat-dialog-actions>
    `,
})
export class Confirmation {
    protected readonly donnees = inject<{ nom: string }>(MAT_DIALOG_DATA);
}
```

```typescript
// src/app/liste-fichiers.ts
import { Component, inject } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { Confirmation } from './confirmation';

@Component({
    selector: 'app-liste-fichiers',
    imports: [MatButtonModule],
    template: `<button mat-button (click)="supprimer('rapport.pdf')">Supprimer</button>`,
})
export class ListeFichiers {
    private readonly dialogue = inject(MatDialog);

    protected supprimer(nom: string): void {
        this.dialogue.open(Confirmation, { data: { nom }, width: '400px' })
            .afterClosed()
            .subscribe((confirme) => { if (confirme) console.log(`${nom} supprimé`); });
    }
}
```

Le dialogue gère automatiquement le **piégeage du focus**, la fermeture par `Échap`, le retour du focus à l'élément déclencheur et les attributs ARIA (`role="dialog"`, `aria-labelledby`). `afterClosed()` émet la valeur passée à `mat-dialog-close`.

#### Table avec tri et pagination

```typescript
// src/app/table-utilisateurs.ts
import { Component, effect, viewChild } from '@angular/core';
import { MatPaginator, MatPaginatorModule } from '@angular/material/paginator';
import { MatSort, MatSortModule } from '@angular/material/sort';
import { MatTableDataSource, MatTableModule } from '@angular/material/table';

interface Utilisateur { nom: string; age: number; }

@Component({
    selector: 'app-table-utilisateurs',
    imports: [MatTableModule, MatSortModule, MatPaginatorModule],
    template: `
        <table mat-table [dataSource]="source" matSort>
            <ng-container matColumnDef="nom">
                <th mat-header-cell *matHeaderCellDef mat-sort-header>Nom</th>
                <td mat-cell *matCellDef="let u">{{ u.nom }}</td>
            </ng-container>
            <ng-container matColumnDef="age">
                <th mat-header-cell *matHeaderCellDef mat-sort-header>Âge</th>
                <td mat-cell *matCellDef="let u">{{ u.age }}</td>
            </ng-container>
            <tr mat-header-row *matHeaderRowDef="colonnes"></tr>
            <tr mat-row *matRowDef="let ligne; columns: colonnes"></tr>
        </table>
        <mat-paginator [pageSizeOptions]="[5, 10]" showFirstLastButtons />
    `,
})
export class TableUtilisateurs {
    protected readonly colonnes = ['nom', 'age'];
    protected readonly source = new MatTableDataSource<Utilisateur>([
        { nom: 'Alice', age: 30 }, { nom: 'Bob', age: 25 }, { nom: 'Chloé', age: 41 },
    ]);
    private readonly tri = viewChild.required(MatSort);
    private readonly pagination = viewChild.required(MatPaginator);

    constructor() {
        effect(() => {                              // branche tri et pagination quand la vue existe
            this.source.sort = this.tri();
            this.source.paginator = this.pagination();
        });
    }
}
```

`MatTableDataSource` fournit filtrage, tri et pagination **côté client** ; pour de gros volumes, implémentez une source **côté serveur** (le paginateur et le tri émettent des événements que vous transmettez à l'API).

**Sélecteur de date.** `mat-datepicker` exige un **adaptateur de dates** : `provideNativeDateAdapter()` (objets `Date`), ou `@angular/material-date-fns-adapter` / `-luxon-adapter` pour des besoins avancés ; la **locale** se règle avec `MAT_DATE_LOCALE`.

**Navigation latérale.** `mat-sidenav-container` + `mat-sidenav` + `mat-sidenav-content` construisent une mise en page avec menu rétractable ; combinez-les avec `BreakpointObserver` (24.5) pour passer en mode `over` sur mobile.

### 24.4 Thèmes (Material 3)

```scss
// src/styles.scss
@use '@angular/material' as mat;

html {
    @include mat.theme((
        color: mat.$azure-palette,
        typography: Roboto,
        density: 0,
    ));
}
```

- **Palettes** prédéfinies (azure, violet, rose, orange…) ; on peut générer un thème **à partir d'une couleur de marque** avec le schematic dédié (`ng generate @angular/material:theme-color`).
- **Typographie** (famille de police), **densité** (`0` normale, valeurs négatives pour compacter les composants : utile pour les tableaux de bord).
- **Personnalisation par variables CSS** (`--mat-sys-primary`, `--mat-sys-surface`, `--mat-sys-on-surface`…) : on modifie l'apparence **sans recompiler** et on peut basculer **clair / sombre** avec `color-scheme: light dark` (ou en alternant une classe).
- Chaque composant expose aussi des **jetons de conception** (variables CSS) pour des ajustements ciblés.

```css
:root { --mat-sys-primary: #0b6bcb; }          /* surcharge d'une couleur système */
.zone-sombre { color-scheme: dark; }           /* mode sombre sur une zone */
```

> Les noms exacts des mixins et variables ont évolué entre les versions de Material (thème M2 → M3) : suivez le guide de **thématisation** de la version installée.

### 24.5 Le CDK

Le **CDK** ne contient **aucun style** : il fournit des **comportements** complexes à bien implémenter soi-même.

| Module | Usage |
| --- | --- |
| **Overlay** | Fenêtres flottantes ancrées (menus déroulants, info-bulles, popovers), gestion de la position, du défilement, du clic extérieur |
| **Portal** | Rendre un gabarit ou un composant **ailleurs** dans le DOM |
| **Drag and Drop** | Listes réordonnables, transfert entre listes (`cdkDrag`, `cdkDropList`) |
| **Scrolling** | **Défilement virtuel** pour de très grandes listes |
| **Layout** | `BreakpointObserver` : réagir aux tailles d'écran (média queries) |
| **A11y** | Piégeage du focus (`cdkTrapFocus`), annonces (`LiveAnnouncer`), moniteur de focus, navigation au clavier dans les listes (`ListKeyManager`) |
| **Clipboard** | Copier dans le presse-papiers (`cdkCopyToClipboard`) |
| **Table**, **Stepper**, **Menu**, **Listbox**, **Accordion** | Versions **sans style** des composants correspondants |
| **Observers** | `cdkObserveContent` (changements de contenu), observation de taille |
| **Testing** | **Harnais de composants** (chapitre 16) |

```typescript
// src/app/liste-virtuelle.ts
import { Component } from '@angular/core';
import { ScrollingModule } from '@angular/cdk/scrolling';

@Component({
    selector: 'app-liste-virtuelle',
    imports: [ScrollingModule],
    template: `
        <!-- Défilement virtuel : seules les lignes visibles sont dans le DOM -->
        <cdk-virtual-scroll-viewport itemSize="48" style="height: 400px">
            <div *cdkVirtualFor="let element of elements" class="ligne">{{ element }}</div>
        </cdk-virtual-scroll-viewport>
    `,
})
export class ListeVirtuelle {
    protected readonly elements = Array.from({ length: 10000 }, (_, i) => `Ligne ${i + 1}`);
}
```

```typescript
// src/app/adaptatif.ts
import { Component, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { map } from 'rxjs';

@Component({
    selector: 'app-adaptatif',
    template: `<p>{{ mobile() ? 'Affichage mobile' : 'Affichage large' }}</p>`,
})
export class Adaptatif {
    // Réagir au point de rupture
    protected readonly mobile = toSignal(
        inject(BreakpointObserver).observe(Breakpoints.Handset).pipe(map((r) => r.matches)),
        { initialValue: false },
    );
}
```

```typescript
// src/app/taches-reordonnables.ts : glisser-déposer
import { Component, signal } from '@angular/core';
import { CdkDrag, CdkDropList, CdkDragDrop, moveItemInArray } from '@angular/cdk/drag-drop';

@Component({
    selector: 'app-taches-reordonnables',
    imports: [CdkDropList, CdkDrag],
    template: `
        <div cdkDropList (cdkDropListDropped)="deposer($event)">
            @for (t of taches(); track t) { <div cdkDrag class="tache">{{ t }}</div> }
        </div>
    `,
    styles: `.tache { padding: .75rem; border: 1px solid #ccc; cursor: grab; }`,
})
export class TachesReordonnables {
    protected readonly taches = signal(['Écrire', 'Tester', 'Publier']);

    protected deposer(evt: CdkDragDrop<string[]>): void {
        const copie = [...this.taches()];                          // mise à jour immuable (signal)
        moveItemInArray(copie, evt.previousIndex, evt.currentIndex);
        this.taches.set(copie);
    }
}
```

```typescript
// src/app/annonce.ts : annonce pour lecteurs d'écran
import { Component, inject } from '@angular/core';
import { LiveAnnouncer } from '@angular/cdk/a11y';

@Component({
    selector: 'app-annonce',
    template: `<button (click)="ajouter()">Ajouter au panier</button>`,
})
export class Annonce {
    private readonly annonceur = inject(LiveAnnouncer);
    protected ajouter(): void { this.annonceur.announce('Article ajouté au panier'); }   // lu par les lecteurs d'écran
}
```

### 24.6 Angular Aria

Angular Aria propose des **comportements accessibles prêts à l'emploi** — navigation au clavier, rôles et attributs ARIA, gestion du focus et de la sélection — **sans imposer de style** : **vous fournissez le HTML et le CSS**. Les primitives comprennent, entre autres, **combobox / autocomplétion**, **listbox / select**, **menu / barre d'outils**, **onglets**, **accordéon**, **arbre** et **grille**. Chaque primitive est fournie avec des **harnais de test**.

**Pourquoi ?** Écrire un composant accessible (un menu, une liste déroulante) est **difficile** : il faut respecter les modèles d'interaction du WAI-ARIA (flèches, `Début` / `Fin`, recherche par frappe, `aria-activedescendant`…). Aria encapsule ces règles ; vous vous concentrez sur l'apparence.

> Consultez la documentation d'**Angular Aria** sur [angular.dev](https://angular.dev) pour l'API exacte (directives et entrées) : elle a évolué pendant la phase d'aperçu, et je n'en reproduis donc pas ici de signatures détaillées.

### 24.7 Accessibilité, tests et bonnes pratiques

- **N'importez que les composants utilisés** (ils sont autonomes).
- Les composants Material respectent **WAI-ARIA**, mais **vous** restez responsable : **libellés** (`mat-label`, `aria-label` sur les boutons-icônes), **contrastes**, **ordre du focus**, messages d'erreur annoncés.
- Utilisez les **harnais** pour les tests (`MatButtonHarness`, `MatDialogHarness`, `MatTableHarness`…).
- Pour un **design system** propre : **CDK + Aria** plutôt que de combattre le style de Material par des surcharges CSS.
- Utilisez la **densité** et les **jetons** pour ajuster l'apparence plutôt que `::ng-deep`.
- Autres bibliothèques d'interface : **PrimeNG**, **NG-ZORRO**, **Taiga UI**, **Spartan UI** — comparez maintenance, accessibilité et compatibilité (chapitre 25).

### Synthèse du chapitre 24

**Material** = composants stylés M3 ; **CDK** = comportements sans style ; **Aria** = primitives accessibles non stylées. Installation par `ng add @angular/material`, thématisation par `mat.theme(...)` et **variables CSS**. Dialogues, tables, formulaires, notifications ; CDK pour défilement virtuel, glisser-déposer, *overlay*, `BreakpointObserver`, annonces. Testez avec les **harnais**.

---

## 25. Bibliothèques tierces

**Objectifs d'apprentissage.** **Évaluer** et **choisir** une bibliothèque ; intégrer une bibliothèque JavaScript **non Angular** de façon propre (encapsulation, SSR, zoneless, nettoyage) ; gérer les **types manquants**, les modules **CommonJS** et les ressources globales ; limiter les **risques** de maintenance et de **chaîne d'approvisionnement**.

### 25.1 Choisir une bibliothèque

Chaque dépendance est un **engagement** : elle alourdit le bundle, impose ses mises à jour et peut devenir un risque de sécurité ou de blocage lors d'une migration d'Angular. Évaluez avant d'installer.

| Critère | À vérifier |
| --- | --- |
| **Compatibilité** | Version d'Angular supportée (`peerDependencies`), composants **autonomes**, **zoneless**, **SSR** |
| **Maintenance** | Dernière publication, issues et PR en attente, nombre de mainteneurs, politique de versions |
| **Taille** | Coût dans le bundle (Bundlephobia), *tree-shaking* (format **ESM**) |
| **Typage** | Types TypeScript inclus et à jour |
| **Licence** | Compatible avec votre usage (commercial, redistribution) |
| **Accessibilité** | Navigation clavier, ARIA, contrastes |
| **Documentation et communauté** | Exemples, réponses aux questions |
| **Alternatives** | Un petit utilitaire à écrire soi-même coûte parfois moins qu'une dépendance |

```bash
ng add <paquet>          # préférez cette commande quand le paquet fournit un schematic
npm install <paquet>
```

**Règle de décision.** Si la bibliothèque est **essentielle**, **complexe** à refaire (éditeur riche, grille de données, cartographie) et bien maintenue : adoptez-la. Si c'est une **fonction utilitaire** de quelques lignes : écrivez-la. Si elle est **abandonnée** : cherchez un fork actif ou une alternative **avant** d'en dépendre.

### 25.2 Bibliothèques Angular courantes

| Besoin | Bibliothèques |
| --- | --- |
| Interface | Angular Material, **PrimeNG**, **NG-ZORRO**, **Taiga UI**, Spartan UI |
| État | **NgRx**, NGXS |
| Formulaires | Formly, `ngx-mask` |
| Traduction | **Transloco**, ngx-translate |
| Graphiques | **ngx-echarts**, **ng2-charts** (Chart.js), ngx-charts |
| Tableaux de données | AG Grid, Angular Material Table |
| Cartes | `@angular/google-maps`, ngx-leaflet |
| Authentification | `angular-oauth2-oidc`, `angular-auth-oidc-client` |
| Éditeur riche | ngx-quill, TinyMCE, Tiptap |
| Utilitaires | **date-fns**, **Luxon**, lodash-es, RxJS |

Une **bibliothèque Angular** (« wrapper ») expose des composants et des services idiomatiques (entrées, sorties, DI). Une **bibliothèque JavaScript pure** (Chart.js, Leaflet, D3) demande une intégration soignée (25.3).

### 25.3 Intégrer une bibliothèque JavaScript **non Angular**

#### 1) Installer avec ses types

```bash
npm install chart.js
npm install -D @types/leaflet        # si la bibliothèque n'a pas ses propres types
```

#### 2) L'encapsuler dans un composant (côté navigateur uniquement)

Principe : **un composant Angular « enveloppe » la bibliothèque** et en cache les détails ; le reste de l'application ne manipule que des **entrées** et des **sorties**. Ce composant est le seul à connaître l'API de la bibliothèque : si vous la changez, un seul fichier est à modifier (*couche anticorruption*).

```typescript
// src/app/graphique.ts
import {
    ChangeDetectionStrategy, Component, DestroyRef, ElementRef, afterNextRender, effect, inject, input, viewChild,
} from '@angular/core';
import { Chart } from 'chart.js/auto';

@Component({
    selector: 'app-graphique',
    template: `<canvas #toile></canvas>`,
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class Graphique {
    donnees = input.required<number[]>();
    private readonly toile = viewChild.required<ElementRef<HTMLCanvasElement>>('toile');
    private graphique?: Chart;

    constructor() {
        afterNextRender(() => {                                                   // le DOM existe ; jamais côté serveur
            this.graphique = new Chart(this.toile().nativeElement, {
                type: 'line',
                data: { labels: this.donnees().map((_, i) => `J${i + 1}`), datasets: [{ data: this.donnees() }] },
            });
        });

        effect(() => {                                                              // réagit aux changements d'entrée
            const d = this.donnees();
            if (this.graphique) { this.graphique.data.datasets[0].data = d; this.graphique.update(); }
        });

        inject(DestroyRef).onDestroy(() => this.graphique?.destroy());              // libérer les ressources
    }
}
```

Ce modèle suit **quatre règles** réutilisables pour toute bibliothèque :

1. **Créer** l'instance dans `afterNextRender` (le DOM existe, et le code ne tourne pas sur le serveur).
2. **Synchroniser** les entrées Angular vers la bibliothèque dans un `effect` (ou `ngOnChanges`).
3. **Remonter** les événements de la bibliothèque par des `output()` (et mettre à jour des **signaux**, pas des champs ordinaires, pour le mode zoneless).
4. **Détruire** dans `DestroyRef.onDestroy` (écouteurs, minuteries, instances, WebGL).

**Avec Zone.js** : une bibliothèque qui déclenche beaucoup d'événements (carte, `mousemove`) provoque trop de vérifications ; créez-la dans `NgZone.runOutsideAngular(...)` et ne rentrez dans la zone que pour les événements utiles. **En zoneless**, ce problème disparaît : seule la modification d'un **signal** rafraîchit la vue.

#### 3) Types manquants

```typescript
// src/types/ancienne-lib.d.ts
declare module 'ancienne-lib' {
    export function faire(x: number): string;
}
```

Une fois la déclaration en place (le fichier doit être inclus par `tsconfig`), le module s'importe avec ses types :

```typescript
import { faire } from 'ancienne-lib';

console.log(faire(42));
```

Pour une bibliothèque sans types, on peut commencer par déclarer le module `declare module 'x';` (tout est alors `any`) puis typer progressivement **uniquement ce que l'on utilise**. Cherchez d'abord `@types/<nom>` sur npm.

#### 4) Styles et scripts globaux

```jsonc
// angular.json (extrait : options de la cible "build")
{
    "options": {
        "styles": ["node_modules/bibliotheque/dist/style.css"],
        "scripts": ["node_modules/bibliotheque/dist/script.js"]
    }
}
```

Les `scripts` sont chargés **globalement** (hors module) : réservez-les aux bibliothèques qui n'existent que sous cette forme ; préférez un `import` (tree-shakable). Les feuilles de style de bibliothèques se chargent via `styles` ou `@use` / `@import` dans `styles.scss`.

#### 5) Modules CommonJS

Les bibliothèques en **CommonJS** (`require`) ne peuvent pas être élaguées (*tree-shaken*) et alourdissent le bundle ; le builder affiche un **avertissement**. Cherchez une version **ESM** ; en dernier recours, `allowedCommonJsDependencies` dans `angular.json` fait taire l'avertissement pour une dépendance donnée (cela ne règle pas le poids).

### 25.4 Pièges d'intégration

| Problème | Solution |
| --- | --- |
| La bibliothèque modifie le DOM hors d'Angular | Encapsuler dans un composant, `afterNextRender`, `ngSkipHydration` si besoin |
| `window is not defined` (SSR) | `afterNextRender`, `isPlatformBrowser`, **import dynamique** (`await import(...)`) |
| Mises à jour non détectées (zoneless / `OnPush`) | Passer par des **signaux** ou `markForCheck()` |
| Fuites mémoire | `destroy()` dans `DestroyRef.onDestroy` ; se désabonner des événements |
| Module CommonJS lourd | Chercher une version **ESM** ; `allowedCommonJsDependencies` en dernier recours |
| Bibliothèque non compatible avec la version d'Angular | Vérifier les `peerDependencies`, chercher un fork maintenu |
| Conflits de styles globaux | Variables CSS, encapsulation, ou charger les styles dans le composant concerné |
| Dépendance **transitive** vulnérable | `npm audit`, `overrides` (npm) / `resolutions` (yarn), mise à jour |

### 25.5 Bonnes pratiques : maintenance et sécurité de la chaîne d'approvisionnement

- **Auditez** (`npm audit`) et **verrouillez** les versions (`package-lock.json` versionné, `npm ci` en CI).
- **Automatisez** les mises à jour (Renovate, Dependabot) avec une CI qui exécute tests et build : les petites mises à jour fréquentes sont **moins risquées** que de grosses mises à jour rares.
- Limitez le nombre de dépendances : chacune est un risque de **maintenance et de sécurité** (paquets compromis, *typosquatting*, scripts d'installation malveillants). Vérifiez l'orthographe du nom et le propriétaire du paquet.
- Évitez les versions **publiées il y a quelques jours** pour des mises à jour critiques : laissez à la communauté le temps de détecter un éventuel paquet piégé.
- Chargez les bibliothèques **lourdes** de façon **paresseuse** (`import()`, `@defer`).
- Surveillez les **licences** (`license-checker`) : certaines sont incompatibles avec un usage commercial fermé.
- **Documentez** les raisons des choix (ADR, *Architecture Decision Records*) : pourquoi cette bibliothèque, quelles alternatives, comment la remplacer.
- **Isolez** : n'exposez pas les types d'une bibliothèque tierce dans toute l'application ; passez par vos propres interfaces.

### Synthèse du chapitre 25

Choisir une bibliothèque = compatibilité (zoneless, SSR), **maintenance**, **taille**, **typage**, **licence**. Pour une bibliothèque JavaScript pure : composant **enveloppe**, création dans `afterNextRender`, synchronisation par `effect`, événements par `output` et **signaux**, **destruction** dans `DestroyRef`. Types manquants par `.d.ts`, CommonJS à éviter, **audit** et mises à jour automatisées pour la sécurité.

---

## 26. Sécurité

**Objectifs d'apprentissage.** Identifier les **menaces** principales d'une application web (OWASP) ; comprendre la **protection intégrée** d'Angular contre le **XSS** et ses limites ; savoir quand et comment **contourner** l'assainissement sans danger ; configurer **CSP** et **Trusted Types** ; protéger contre **CSRF / XSRF**, le *clickjacking* et les **redirections ouvertes** ; stocker correctement les jetons ; sécuriser la chaîne de dépendances ; disposer d'une **liste de contrôle**.

### 26.1 Principes et panorama des menaces

Une application Angular s'exécute **dans le navigateur de l'utilisateur**, un environnement que **vous ne contrôlez pas** : tout ce qui est dans le bundle est **public**, lisible et **modifiable**. Principe de base : **le client n'est jamais digne de confiance ; seule la vérification côté serveur fait foi**. Le client sert à l'ergonomie, pas à la sécurité.

| Menace | Protection Angular / bonne pratique |
| --- | --- |
| **XSS** (injection de scripts) | **Échappement automatique** des liaisons, assainissement du HTML, **CSP**, **Trusted Types** |
| **CSRF / XSRF** | Jeton XSRF (`withXsrfConfiguration`), cookies `SameSite` |
| **Injection via URL** (`javascript:`) | Assainissement des URL et des ressources |
| **Clickjacking** | `frame-ancestors` / `X-Frame-Options` |
| **Redirection ouverte** | Valider les URL de redirection |
| **Secrets exposés** | Jamais de secrets dans le code client |
| **Dépendances vulnérables** | `npm audit`, mises à jour régulières |
| **Contrôle d'accès contourné** | **Contrôles côté serveur** (les gardes ne suffisent pas) |

Pour structurer la démarche : **OWASP Top 10** (les dix risques les plus courants), **OWASP ASVS** (liste de vérification détaillée) et la **modélisation de menaces** (qui pourrait attaquer quoi, par quel chemin ?).

### 26.2 XSS : la protection intégrée

Le **XSS** (*Cross-Site Scripting*) consiste à faire exécuter **un script de l'attaquant** dans la page d'une victime (via un champ de commentaire, un paramètre d'URL…), avec les droits de la victime : vol de session, actions à sa place, hameçonnage. Angular **traite toute valeur liée comme non fiable** et l'**échappe** automatiquement selon le **contexte** (texte HTML, attribut, style, URL).

```typescript
// src/app/xss.ts
import { Component, signal } from '@angular/core';

@Component({
    selector: 'app-xss',
    template: `
        <p>{{ saisie() }}</p>                     <!-- affiché comme TEXTE, pas exécuté -->
        <div [innerHTML]="saisie()"></div>        <!-- assaini automatiquement (onerror supprimé) -->
    `,
})
export class Xss {
    protected readonly saisie = signal("<img src=x onerror='alert(1)'>");
}
```

Angular distingue plusieurs **contextes de sécurité** et applique la protection adaptée à chacun :

| Contexte | Exemple | Traitement |
| --- | --- | --- |
| **HTML** | `[innerHTML]` | Le HTML est **assaini** : balises et attributs dangereux (`<script>`, `onerror`…) supprimés |
| **Style** | `[style.background]` | Valeurs dangereuses neutralisées |
| **URL** | `[href]`, `[src]` | Les schémas dangereux (`javascript:`) sont préfixés / neutralisés |
| **URL de ressource** | `<iframe [src]>`, `<script src>` | **Refusé** sauf valeur explicitement approuvée |

**Ce que cette protection ne couvre pas :** le code que **vous** écrivez pour contourner le framework (accès direct au DOM, `eval`, bibliothèques tierces), les **gabarits construits à partir de données utilisateur**, et le contenu **déjà approuvé** par `bypassSecurityTrust*`.

#### Contourner l'assainissement : à n'utiliser qu'en dernier recours

Il existe des cas légitimes (afficher un contenu HTML **rédigé par votre équipe**, intégrer une vidéo d'un hébergeur connu). On « approuve » alors explicitement une valeur avec `DomSanitizer`.

```typescript
// src/app/contenu-confiance.ts
import { Component, inject } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
    selector: 'app-contenu-confiance',
    template: `
        <div [innerHTML]="html"></div>
        <iframe [src]="urlVideo" title="Vidéo"></iframe>
    `,
})
export class ContenuConfiance {
    private readonly sanitizer = inject(DomSanitizer);
    private readonly contenuDeConfiance = "<p>Contenu rédigé par l'équipe</p>";

    protected readonly html = this.sanitizer.bypassSecurityTrustHtml(this.contenuDeConfiance);      // ATTENTION : DÉSACTIVE la protection
    protected readonly urlVideo = this.sanitizer.bypassSecurityTrustResourceUrl('https://www.youtube.com/embed/xxxx');
}
```

> **À éviter.** **Ne contournez jamais** l'assainissement pour du contenu venant d'un utilisateur ou d'une API que vous ne maîtrisez pas : vous réintroduisez exactement la faille que le framework empêchait. Si vous devez afficher du **HTML riche** (éditeur WYSIWYG, Markdown converti), **assainissez-le avec une bibliothèque dédiée** (**DOMPurify**) ou l'**API Sanitizer** du navigateur, **puis** seulement approuvez le résultat.

```typescript
// src/app/html-propre.ts : assainir avec DOMPurify avant d'approuver
import { Component, computed, inject, input } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';
import DOMPurify from 'dompurify';

@Component({
    selector: 'app-html-propre',
    template: `<div [innerHTML]="propre()"></div>`,
})
export class HtmlPropre {
    html = input.required<string>();
    private readonly sanitizer = inject(DomSanitizer);
    protected readonly propre = computed(() => this.sanitizer.bypassSecurityTrustHtml(DOMPurify.sanitize(this.html())));
}
```

(DOMPurify requiert un DOM : en SSR, utilisez la variante serveur adaptée ou n'assainissez que côté navigateur.)

#### Pratiques à proscrire

```typescript
// src/app/a-eviter.ts
import { Component, ElementRef, inject } from '@angular/core';

@Component({
    selector: 'app-a-eviter',
    template: `<div></div>`,
})
export class AEviter {
    private readonly element = inject(ElementRef<HTMLElement>);

    afficher(saisie: string): void {
        this.element.nativeElement.innerHTML = saisie;        // Incorrect : contourne Angular
        // document.write(saisie); eval(saisie);              // Incorrect
        // Pas de gabarits construits dynamiquement à partir de données utilisateur
    }
}
```

- `ElementRef.nativeElement.innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write` : **contournent** l'assainissement.
- `eval`, `new Function`, `setTimeout('chaîne')` : exécution de code arbitraire.
- **Compiler un gabarit à l'exécution** à partir de chaînes venant d'utilisateurs (JIT) : équivalent à de l'exécution de code.
- Insérer des valeurs utilisateur dans `[attr.href]`, `[attr.src]`, `[attr.style]` : ces liaisons d'attribut passent aussi par l'assainissement, mais une **URL externe** reste un vecteur d'hameçonnage ; validez le domaine.
- Rendre du **Markdown** sans l'assainir (le HTML produit peut contenir des scripts).
- Faire confiance aux **données d'API** : une API peut renvoyer du contenu saisi par un utilisateur malveillant.

### 26.3 Content Security Policy (CSP) et Trusted Types

Une **CSP** est un en-tête HTTP qui dit au navigateur **quelles sources de contenu sont autorisées**. C'est une **seconde ligne de défense** : même si un script injecté arrivait dans la page, le navigateur **refuserait de l'exécuter**.

```text
Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-ABC123'; style-src 'self' 'nonce-ABC123'; img-src 'self' data:; connect-src 'self' https://api.exemple.com; frame-ancestors 'none'; object-src 'none'; base-uri 'self'; require-trusted-types-for 'script'
```

| Directive | Rôle |
| --- | --- |
| `default-src` | Politique par défaut |
| `script-src` | Sources des scripts (**évitez** `'unsafe-inline'` et `'unsafe-eval'`) |
| `style-src` | Sources des styles |
| `connect-src` | Destinations des requêtes (`fetch`, XHR, WebSocket) |
| `img-src`, `font-src`, `frame-src` | Images, polices, cadres |
| `frame-ancestors` | Qui peut **intégrer votre page** dans un cadre (anti-clickjacking) |
| `object-src 'none'`, `base-uri 'self'` | Durcissement courant |

- Le **nonce** est un jeton **aléatoire généré par le serveur à chaque réponse** ; il autorise les scripts / styles en ligne qu'Angular insère. Fournissez-le à Angular par l'attribut `ngCspNonce` sur `<app-root>` ou par le jeton `CSP_NONCE`. En SSR, le serveur le génère par requête.
- **`autoCsp`** (option du builder, selon la version) peut générer une CSP **stricte** fondée sur des **empreintes** (*hash*) des scripts pour les sites statiques.
- **Trusted Types** : mécanisme du navigateur qui **interdit** d'écrire des chaînes non « typées » dans les API dangereuses (`innerHTML`, `eval`…). Angular est **compatible** (politiques `angular` et `angular#bundler` à autoriser : `trusted-types angular angular#bundler`). Si une bibliothèque tierce écrit du HTML, elle peut **casser** sous Trusted Types : testez.
- Déployez d'abord en mode **rapport seul** (`Content-Security-Policy-Report-Only`) pour détecter les blocages avant d'appliquer la politique.

### 26.4 CSRF / XSRF

Le **CSRF** (*Cross-Site Request Forgery*) abuse du fait que le navigateur **joint automatiquement les cookies** à toute requête vers votre domaine : un site malveillant peut déclencher, depuis le navigateur de la victime connectée, une requête `POST /virement`.

Le client HTTP Angular implémente le **motif du jeton double** : il lit un **cookie** (`XSRF-TOKEN`) et renvoie sa valeur dans un en-tête (`X-XSRF-TOKEN`) pour les requêtes **modifiantes** (POST, PUT, DELETE) vers la **même origine**. Un site tiers ne peut pas lire votre cookie : il ne peut pas fournir l'en-tête.

```typescript
// src/app/app.config.ts
import { ApplicationConfig } from '@angular/core';
import { provideHttpClient, withXsrfConfiguration } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
    providers: [
        provideHttpClient(withXsrfConfiguration({ cookieName: 'XSRF-TOKEN', headerName: 'X-XSRF-TOKEN' })),
    ],
};
```

Le serveur doit **émettre** le cookie et **valider** l'en-tête. Complétez avec des cookies **`SameSite=Lax` ou `Strict`** (le navigateur n'envoie pas le cookie pour la plupart des requêtes intersites), **`Secure`** (HTTPS uniquement) et **`HttpOnly`** (inaccessible à JavaScript, pour les cookies de session). Les API qui s'authentifient **par en-tête `Authorization`** (jeton en mémoire) ne sont pas exposées au CSRF classique, puisque rien n'est joint automatiquement.

### 26.5 Stockage des jetons et données sensibles

| Où | Risque |
| --- | --- |
| `localStorage` / `sessionStorage` | **Lisibles par n'importe quel script** (XSS) : à éviter pour les jetons sensibles |
| **Cookie `HttpOnly`** (+ `Secure`, `SameSite`) | Non lisible par JavaScript : meilleur choix pour les sessions |
| Mémoire (variable / signal) | Disparaît au rechargement ; plus sûr contre le vol persistant |

Des données **personnelles** ou **sensibles** (santé, finances) ne doivent pas rester dans le stockage du navigateur ni dans les caches (Service Worker, chapitre 23) au-delà du nécessaire ; **effacez-les à la déconnexion**.

### 26.6 Redirections ouvertes, clickjacking, messages inter-fenêtres

**Redirection ouverte.** Une page de connexion qui renvoie vers l'URL donnée dans un paramètre (`/connexion?redirection=https://site-pirate.com`) peut servir à l'**hameçonnage**. Validez que la destination est **interne** :

```typescript
// src/app/securite/redirection.ts
export function destinationSure(valeur: string | null | undefined): string {
    // Accepte uniquement un chemin interne : commence par un seul « / », pas « // » ni schéma
    if (valeur && valeur.startsWith('/') && !valeur.startsWith('//') && !valeur.includes('://')) {
        return valeur;
    }
    return '/';
}
// usage : this.router.navigateByUrl(destinationSure(this.route.snapshot.queryParamMap.get('redirection')));
```

**Clickjacking.** Une page malveillante intègre la vôtre dans un `<iframe>` invisible et fait cliquer l'utilisateur dessus. Défense : `Content-Security-Policy: frame-ancestors 'none'` (ou `'self'`), complétée par `X-Frame-Options: DENY` pour les anciens navigateurs.

**`postMessage`.** Vérifiez **toujours** `event.origin` avant de traiter un message reçu d'une autre fenêtre, et ne soyez jamais permissif sur l'origine cible à l'envoi (`targetOrigin` précis, jamais `'*'` pour des données sensibles).

**Liens externes.** Ouvrez-les avec `rel="noopener noreferrer"` (empêche la page ouverte de manipuler la vôtre et de connaître la provenance).

**Téléversements.** Le navigateur ne valide rien de manière fiable : contrôlez **type, taille et contenu côté serveur**, jamais seulement l'extension.

### 26.7 Autres bonnes pratiques

- **HTTPS partout** ; en-têtes : `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `Referrer-Policy`, `Permissions-Policy`.
- **Validez et nettoyez côté serveur** : le client est modifiable par l'utilisateur ; la validation côté client n'est qu'un confort.
- **Aucun secret** (clés d'API privées, mots de passe) dans le code ni dans les environnements front : ils sont dans le bundle (chapitre 3). Une clé « publique » (carte, analytique) doit être **restreinte** par domaine et par quota côté fournisseur.
- **Dépendances** : `npm audit`, `npm ci`, Dependabot / Renovate ; vérifier les paquets avant installation (chapitre 25).
- **CORS** : le serveur n'autorise que les origines nécessaires ; ne renvoyez jamais `Access-Control-Allow-Origin: *` avec des identifiants.
- **Messages d'erreur** génériques côté utilisateur (pas de traces techniques ni de requêtes SQL).
- **Journalisation** : ne consignez ni mots de passe, ni jetons, ni données personnelles.
- **Sources maps** : ne les publiez pas en production (ou en accès restreint).
- **Mettre à jour Angular** : les correctifs de sécurité sont publiés pour les versions supportées (la v22 en a intégré plusieurs, appliqués automatiquement lors de la mise à jour). Suivez les **avis de sécurité** du dépôt Angular.
- **SSR** : hôtes autorisés, pas d'état partagé entre requêtes, cookies transmis explicitement (chapitre 22).
- Revue de sécurité : **OWASP Top 10**, **OWASP ASVS**, guide de sécurité sur [angular.dev/best-practices/security](https://angular.dev/best-practices/security).

### 26.8 Liste de contrôle sécurité

- [ ] Aucune utilisation d'`innerHTML` / `bypassSecurityTrust*` avec des données non maîtrisées
- [ ] HTML riche assaini (DOMPurify) avant affichage
- [ ] CSP stricte (nonce ou empreintes), `frame-ancestors`, Trusted Types si possible
- [ ] Cookies de session `HttpOnly` + `Secure` + `SameSite` ; jetons XSRF si cookies
- [ ] Pas de jetons sensibles dans `localStorage`
- [ ] Redirections validées, liens externes en `noopener noreferrer`
- [ ] Contrôle d'accès **côté serveur** pour chaque action
- [ ] Dépendances auditées et verrouillées, mises à jour automatisées
- [ ] Aucun secret dans le bundle ; source maps non publiques
- [ ] Application mise à jour vers une version supportée d'Angular

### Synthèse du chapitre 26

Le client n'est pas digne de confiance : **la sécurité réelle se fait côté serveur**. Angular **échappe et assainit** par défaut (HTML, style, URL, ressources) : ne contournez cette protection (`bypassSecurityTrust*`, `innerHTML` direct) que pour du contenu **maîtrisé**, et assainissez le HTML riche (DOMPurify). **CSP** et **Trusted Types** forment une seconde ligne de défense ; **XSRF** par jeton double + `SameSite` ; jetons en **cookies `HttpOnly`** plutôt qu'en `localStorage` ; validez les redirections ; auditez les dépendances ; **mettez à jour** Angular.

---

## 27. Authentification et autorisation

**Objectifs d'apprentissage.** Distinguer **authentification** et **autorisation** ; comparer **sessions par cookie**, **JWT**, **OAuth 2.0 / OpenID Connect** et **BFF** ; écrire un service d'authentification à base de signaux ; **intercepter** les requêtes et **rafraîchir** le jeton sans conditions de concurrence ; protéger les routes ; adapter l'interface aux permissions ; intégrer **OIDC avec Authorization Code + PKCE** ; gérer SSR, déconnexion et multi-onglets.

### 27.1 Définitions

|  | **Authentification** (*AuthN*) | **Autorisation** (*AuthZ*) |
| --- | --- | --- |
| Question | **Qui êtes-vous ?** | **Que pouvez-vous faire ?** |
| Exemple | Connexion, SSO, passkey | Rôles, permissions, propriété d'une ressource |
| Où | Fournisseur d'identité / serveur | **Serveur** à chaque requête (le client ne fait que refléter) |

**Vocabulaire**

- **Fournisseur d'identité** (*IdP*) : service qui authentifie (Keycloak, Auth0, Microsoft Entra ID, Google…).
- **Jeton d'accès** (*access token*) : preuve de droits présentée à l'API, de **courte durée**.
- **Jeton de rafraîchissement** (*refresh token*) : permet d'obtenir un nouveau jeton d'accès sans ressaisir ses identifiants.
- **Jeton d'identité** (*ID token*, OIDC) : informations sur l'utilisateur authentifié.
- **Revendications** (*claims*) : informations dans un jeton (identifiant, rôles, expiration).
- **Portée** (*scope*) : droits demandés (`openid profile email`).
- **RBAC** (contrôle par rôles) / **ABAC** (par attributs) : modèles d'autorisation.

### 27.2 Les approches

| Approche | Principe | Remarques |
| --- | --- | --- |
| **Session par cookie** (`HttpOnly`) | Le serveur émet un cookie de session | Simple et sûr pour les applications web ; protéger contre le CSRF (chapitre 26) |
| **JWT** (jeton signé) | Jeton envoyé dans `Authorization: Bearer` | Sans état côté serveur ; **durée de vie courte** + jeton de rafraîchissement |
| **OAuth 2.0 / OpenID Connect** (flux **Authorization Code + PKCE**) | Délégation à un fournisseur d'identité | **Recommandé** pour le SSO et les applications publiques |
| **BFF** (*Backend For Frontend*) | Un petit serveur gère les jetons et expose un **cookie** à l'application | Le plus sûr : **aucun jeton dans le navigateur** |

> **À éviter.** L'ancien flux OAuth « **Implicit** » est **déprécié** : utilisez **Authorization Code avec PKCE**.

**Qu'est-ce qu'un JWT ?** Trois parties encodées en Base64url séparées par des points : **en-tête**, **charge utile** (claims : `sub`, `exp`, `roles`…) et **signature**. Il est **signé**, pas **chiffré** : n'importe qui peut **lire** son contenu. Le navigateur peut décoder la charge pour **afficher** un nom ou connaître l'expiration, mais **seul le serveur** peut en **vérifier la signature** : ne prenez jamais une décision de sécurité sur un JWT décodé côté client.

**PKCE** (*Proof Key for Code Exchange*) : le client génère un secret éphémère (*code verifier*), envoie son empreinte (*code challenge*) à l'IdP, puis le prouve en échangeant le code d'autorisation contre des jetons. Cela empêche un attaquant qui intercepterait le code de l'utiliser. Il remplace le « secret client », impossible à garder dans une application publique.

**Choisir.** Application avec **son propre backend** : sessions par cookie, ou **BFF** + OIDC. Application sans backend propre ou entreprise avec SSO : OIDC code + PKCE avec une bibliothèque certifiée. Évitez de **construire** votre propre système de mots de passe, de jetons et de récupération de compte.

### 27.3 Un service d'authentification avec signaux

```typescript
// src/app/auth/auth.ts
import { Injectable, inject, signal, computed } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { firstValueFrom } from 'rxjs';

export interface Utilisateur { id: number; nom: string; roles: string[] }
interface ReponseConnexion { jeton: string; utilisateur: Utilisateur }

@Injectable({ providedIn: 'root' })
export class AuthService {
    private readonly http = inject(HttpClient);
    private readonly router = inject(Router);

    private readonly _utilisateur = signal<Utilisateur | null>(null);
    private readonly _jeton = signal<string | null>(null);              // en mémoire : pas de localStorage
    private rafraichissement?: Promise<void>;                          // requête de rafraîchissement en cours (partagée)

    readonly utilisateur = this._utilisateur.asReadonly();
    readonly jeton = this._jeton.asReadonly();
    readonly estConnecte = computed(() => this._utilisateur() !== null);

    async connecter(email: string, motDePasse: string): Promise<void> {
        const r = await firstValueFrom(this.http.post<ReponseConnexion>('/api/auth/connexion', { email, motDePasse }));
        this._jeton.set(r.jeton);
        this._utilisateur.set(r.utilisateur);
    }

    /** Rafraîchit le jeton ; plusieurs appels simultanés partagent UNE seule requête. */
    rafraichir(): Promise<void> {
        this.rafraichissement ??= firstValueFrom(this.http.post<ReponseConnexion>('/api/auth/rafraichir', {}))
            .then((r) => { this._jeton.set(r.jeton); this._utilisateur.set(r.utilisateur); })
            .finally(() => { this.rafraichissement = undefined; });
        return this.rafraichissement;
    }

    async deconnecter(): Promise<void> {
        try { await firstValueFrom(this.http.post('/api/auth/deconnexion', {})); } finally {
            this._jeton.set(null);
            this._utilisateur.set(null);
            await this.router.navigateByUrl('/connexion');
        }
    }

    aLeRole(role: string): boolean { return this._utilisateur()?.roles.includes(role) ?? false; }
}
```

Le **jeton de rafraîchissement** est idéalement un **cookie `HttpOnly`** que le serveur lit lui-même sur `/api/auth/rafraichir` : le client n'en voit jamais la valeur. Le jeton d'accès, lui, reste **en mémoire** (donc perdu au rechargement : on le récupère par un rafraîchissement au démarrage, voir 27.5).

### 27.4 Intercepteur avec rafraîchissement du jeton

```typescript
// src/app/http/auth-intercepteur.ts : version avancée de jetonIntercepteur (section 11.4)
import { inject } from '@angular/core';
import { HttpInterceptorFn, HttpErrorResponse, HttpRequest } from '@angular/common/http';
import { catchError, from, switchMap, throwError } from 'rxjs';
import { AuthService } from '../auth/auth';

export const authIntercepteur: HttpInterceptorFn = (req, next) => {
    const auth = inject(AuthService);
    const avecJeton = (r: HttpRequest<unknown>) => {
        const jeton = auth.jeton();
        return jeton && r.url.startsWith('/api') ? r.clone({ setHeaders: { Authorization: `Bearer ${jeton}` } }) : r;
    };

    return next(avecJeton(req)).pipe(
        catchError((e: HttpErrorResponse) => {
            if (e.status === 401 && !req.url.includes('/auth/')) {
                return from(auth.rafraichir()).pipe(                               // un seul rafraîchissement même si 5 requêtes échouent
                    switchMap(() => next(avecJeton(req))),                // rejouer la requête avec le nouveau jeton
                    catchError(() => { void auth.deconnecter(); return throwError(() => e); }),
                );
            }
            return throwError(() => e);
        }),
    );
};
```

Points importants : (1) ne **jamais** joindre le jeton à un domaine tiers (`startsWith('/api')`) ; (2) **exclure** les URL d'authentification (évite une boucle infinie) ; (3) **partager** le rafraîchissement entre requêtes concurrentes (sinon cinq 401 simultanés lancent cinq rafraîchissements, et avec la **rotation** des jetons, les suivants échouent) ; (4) **rejouer** la requête d'origine ; (5) en cas d'échec définitif, **déconnecter**.

### 27.5 Restaurer la session et protéger les routes

```typescript
// src/app/app.config.ts (extrait) : restaurer la session au démarrage
import { ApplicationConfig, inject, provideAppInitializer } from '@angular/core';
import { provideHttpClient, withInterceptors } from '@angular/common/http';
import { AuthService } from './auth/auth';
import { authIntercepteur } from './http/auth-intercepteur';

export const appConfig: ApplicationConfig = {
    providers: [
        provideHttpClient(withInterceptors([authIntercepteur])),
        provideAppInitializer(() => inject(AuthService).rafraichir().catch(() => undefined)),   // pas de session : on continue anonyme
    ],
};
```

```typescript
// src/app/auth/gardes.ts : garde de rôle pour `canMatch`
import { inject } from '@angular/core';
import { CanMatchFn, Router } from '@angular/router';
import { AuthService } from './auth';

export const roleMatchGuard = (role: string): CanMatchFn => () =>
    inject(AuthService).aLeRole(role) || inject(Router).createUrlTree(['/interdit']);
```

Avec `canMatch`, le code de la route n'est même pas téléchargé si l'utilisateur n'a pas le rôle :

```typescript
// src/app/app.routes.ts (extrait)
import { Routes } from '@angular/router';
import { roleMatchGuard } from './auth/gardes';

export const routes: Routes = [
    {
        path: 'admin',
        canMatch: [roleMatchGuard('admin')],
        loadChildren: () => import('./admin/admin.routes').then((m) => m.ADMIN_ROUTES),
    },
];
```

Après connexion, revenez à la page demandée : la garde `authGarde` (chapitre 9) place `redirection` en paramètre ; la page de connexion le lit et le valide avec `destinationSure()` (chapitre 26).

### 27.6 Autorisation dans l'interface

```typescript
// src/app/actions-admin.ts
import { Component, inject } from '@angular/core';
import { AuthService } from './auth/auth';

@Component({
    selector: 'app-actions-admin',
    template: `
        @if (auth.aLeRole('admin')) {
            <button (click)="supprimer()">Supprimer</button>
        }
    `,
})
export class ActionsAdmin {
    protected readonly auth = inject(AuthService);

    protected supprimer(): void {
        console.log('Suppression demandée (le serveur doit la contrôler)');
    }
}
```

Une directive structurelle (`*appSiRole`, chapitre 6) ou un composant `*appPermission` peut centraliser cette logique ; pour des permissions plus fines que les rôles, exposez des **signaux dérivés** (`peutModifier = computed(() => …)`).

> **À éviter.** **Masquer un bouton n'est pas de la sécurité.** Chaque action doit être **contrôlée côté serveur** (rôles, **propriété des ressources**, état du dossier). Les gardes de route ne protègent que l'**expérience** utilisateur : quiconque peut appeler l'API directement. Le serveur doit répondre **401** (non authentifié) ou **403** (interdit) et l'interface doit réagir correctement à ces codes.

### 27.7 OpenID Connect avec Authorization Code + PKCE

Plutôt que d'écrire le flux vous-même, utilisez une **bibliothèque certifiée** (`angular-oauth2-oidc`, `angular-auth-oidc-client`, `oidc-client-ts`) :

```bash
npm install angular-oauth2-oidc          # ou angular-auth-oidc-client, oidc-client-ts
```

```typescript
// src/app/auth-oidc.ts
import { DOCUMENT } from '@angular/common';
import { Injectable, inject } from '@angular/core';
import { AuthConfig, OAuthService } from 'angular-oauth2-oidc';

@Injectable({ providedIn: 'root' })
export class AuthOidc {
    private readonly oauth = inject(OAuthService);
    private readonly document = inject(DOCUMENT);

    async initialiser(): Promise<void> {
        const config: AuthConfig = {
            issuer: 'https://auth.exemple.com/realms/mon-royaume',
            clientId: 'mon-app-angular',
            redirectUri: this.document.location.origin + '/',      // pas de `window` à l'import du module (SSR)
            responseType: 'code',                                  // Authorization Code + PKCE
            scope: 'openid profile email',
            showDebugInformation: false,
        };
        this.oauth.configure(config);
        await this.oauth.loadDiscoveryDocumentAndTryLogin();
    }
    connecter(): void { this.oauth.initCodeFlow(); }
    deconnecter(): void { this.oauth.logOut(); }
    get jeton(): string { return this.oauth.getAccessToken(); }
}
```

Enregistrement dans la configuration de l'application :

```typescript
// src/app/app.config.ts
import { ApplicationConfig, inject, provideAppInitializer } from '@angular/core';
import { provideHttpClient } from '@angular/common/http';
import { provideOAuthClient } from 'angular-oauth2-oidc';
import { AuthOidc } from './auth-oidc';

export const appConfig: ApplicationConfig = {
    providers: [
        provideHttpClient(),
        provideOAuthClient(),
        provideAppInitializer(() => inject(AuthOidc).initialiser()),
    ],
};
```

**Déroulement.** (1) L'utilisateur clique « Se connecter » → `initCodeFlow()` le redirige vers l'IdP avec le *code challenge*. (2) Il s'authentifie chez l'IdP (SSO, MFA, passkey). (3) L'IdP le renvoie vers `redirectUri` avec un **code**. (4) La bibliothèque échange le code (+ *code verifier*) contre les **jetons**. (5) Les appels à l'API portent le jeton d'accès. Avec un **BFF**, l'échange du code se fait **côté serveur** et le navigateur ne reçoit qu'un cookie de session.

### 27.8 SSR, déconnexion et multi-onglets

- **SSR** : l'authentification par **cookie** fonctionne naturellement si le serveur Angular **transmet le cookie** à l'API lors de ses requêtes. Un jeton **en mémoire** n'existe pas côté serveur lors du premier rendu : rendez les zones privées en `RenderMode.Client` (chapitre 22), ou utilisez des cookies. **Ne mettez jamais en cache** (CDN) des pages personnalisées.
- **Déconnexion** : invalider la session **côté serveur**, supprimer jetons et cookies, **vider** les caches (stockage local, Service Worker, état NgRx / signaux), rediriger.
- **Multi-onglets** : synchroniser la déconnexion entre onglets avec `BroadcastChannel` (ou l'événement `storage`) : quand un onglet se déconnecte, les autres aussi.
- **Inactivité** : expiration de session après un délai, avec avertissement préalable.
- **Expiration** : gérer `exp` (rafraîchir **avant** l'expiration plutôt qu'après un 401, si l'IdP le permet).

```typescript
// src/app/auth/synchro-deconnexion.ts
import { Injectable, inject } from '@angular/core';
import { AuthService } from './auth';

@Injectable({ providedIn: 'root' })
export class SynchroDeconnexion {
    private readonly auth = inject(AuthService);
    private readonly canal = typeof BroadcastChannel === 'undefined' ? null : new BroadcastChannel('auth');

    constructor() {
        if (this.canal) this.canal.onmessage = (e) => { if (e.data === 'deconnexion') void this.auth.deconnecter(); };
    }
    annoncer(): void { this.canal?.postMessage('deconnexion'); }
}
```

### 27.9 Tests et pièges

- Testez la garde (utilisateur connecté / non connecté / mauvais rôle), l'intercepteur (ajout de l'en-tête, rejeu après 401, un seul rafraîchissement pour plusieurs 401) avec `HttpTestingController` (chapitre 16).
- Piège : **boucle infinie** si l'URL de rafraîchissement passe elle-même par l'intercepteur (d'où l'exclusion de `/auth/`).
- Piège : stocker le jeton dans `localStorage` « pour survivre au rechargement » : préférez le **rafraîchissement au démarrage**.
- Piège : confondre **authentifié** et **autorisé** : un utilisateur connecté n'a pas tous les droits.
- Piège : redirections post-connexion non validées (chapitre 26).

### 27.10 Bonnes pratiques

- **Cookies `HttpOnly`** ou **BFF** de préférence ; sinon jetons **en mémoire**, de **courte durée**.
- **Rafraîchissement** et **rotation** des jetons, **révocation** à la déconnexion.
- **Ne stockez pas** de mots de passe ; imposez des **règles** et l'**authentification multifacteur** (MFA), **passkeys** (WebAuthn).
- Utilisez des **fournisseurs d'identité** reconnus plutôt que d'implémenter vous-même.
- Journalisez les événements sensibles ; limitez le **débit** des tentatives (côté serveur).
- **Principe du moindre privilège** : rôles et portées aussi limités que possible.

### Synthèse du chapitre 27

**Authentification** (qui ?) ≠ **autorisation** (quoi ?), toujours **vérifiée côté serveur**. Approches : sessions par cookie, JWT, **OIDC code + PKCE**, **BFF** (le plus sûr). Service d'authentification à **signaux**, jeton **en mémoire**, **intercepteur** qui ajoute le jeton, exclut les URL d'auth, **partage** un rafraîchissement unique et **rejoue** la requête. `canMatch` + gardes pour l'expérience, `provideAppInitializer` pour restaurer la session, **bibliothèque certifiée** pour OIDC. Attention à SSR, déconnexion multi-onglets et caches.

---

## 28. Migration et mises à jour

**Objectifs d'apprentissage.** Mettre à jour Angular **version après version** avec `ng update` ; connaître et exécuter les **migrations** vers l'Angular moderne (autonome, flux de contrôle, `inject()`, signaux, Vitest, builder `application`) ; passer en **zoneless** ; planifier la migration d'une **grande application** ; migrer depuis **AngularJS** ; diagnostiquer les problèmes fréquents.

### 28.1 Mettre à jour Angular

Angular publie une version majeure **tous les 6 mois**, avec une **mise à jour guidée** : les changements incompatibles sont annoncés à l'avance (dépréciations) et la plupart sont **réécrits automatiquement** dans votre code par des *schematics*.

```bash
# 1. Consulter le guide : https://angular.dev/update-guide  (choisir version actuelle → cible)
# 2. Travailler sur une branche propre, tests au vert
ng update                                       # liste ce qui peut être mis à jour
ng update @angular/core@22 @angular/cli@22      # mise à jour + migrations automatiques
ng update @angular/material@22                  # bibliothèques associées
```

| Règle | Détail |
| --- | --- |
| **Une version majeure à la fois** | 19 → 20 → 21 → 22 (ne sautez pas de version) |
| **Node.js et TypeScript** | Chaque version exige des versions minimales : [angular.dev/reference/versions](https://angular.dev/reference/versions) |
| **Dépendances** | Mettre à jour (ou remplacer) les bibliothèques tierces incompatibles |
| **Tests** | Avant et après chaque étape ; commit après chaque version |
| **Lire les notes de version** | Changements majeurs, API supprimées, valeurs par défaut modifiées |

> **Astuce.** `ng update` exécute des **schematics** qui **réécrivent votre code** automatiquement ; relisez toujours le **diff Git**.

**Déroulement détaillé d'une mise à jour**

1. **Préparer** : branche dédiée, arbre Git propre (`ng update` refuse sinon, sauf `--allow-dirty`), tests et build **verts** avant de commencer, dépendances installées à partir du verrou (`npm ci`).
2. **Choisir le chemin** dans le guide de mise à jour : il liste, pour votre version de départ et d'arrivée, les **étapes manuelles** (changements non automatisables) et les **migrations automatiques**.
3. **Vérifier l'environnement** : version de **Node.js** et de **TypeScript** exigée par la cible (à mettre à jour avant ou avec `ng update`).
4. **Mettre à jour le noyau** (`@angular/core` et `@angular/cli` **ensemble**) ; le CLI télécharge les paquets, **exécute les migrations** et affiche un résumé.
5. **Mettre à jour les bibliothèques officielles** (`@angular/material`, `@angular/cdk`, `@ngrx/*`) **puis** tierces ; remplacer ou attendre celles qui ne supportent pas encore la cible.
6. **Compiler, tester, lancer** l'application ; corriger les erreurs et avertissements ; **commit**.
7. **Répéter** pour la version majeure suivante.

Options utiles : `--dry-run` (simule sans écrire), `--create-commits` (un commit par migration, pratique pour relire et pour annuler), `--force` (ignore certaines vérifications de compatibilité : à éviter), `--migrate-only --from=X --to=Y` (rejoue seulement les migrations d'un paquet, utile après un échec), `--allow-dirty`. Pour **annuler** : `git reset` / `git revert` des commits de migration.

### 28.2 Migrations vers l'Angular moderne

Chaque migration est un **schematic** exécutable **indépendamment**, en vérifiant le résultat (diff Git). Procédure recommandée : **une migration à la fois**, tests et commit entre chacune.

| Objectif | Commande |
| --- | --- |
| **Composants autonomes** (supprimer les `NgModule`) | `ng generate @angular/core:standalone` |
| **Nouveau flux de contrôle** (`*ngIf` → `@if`) | `ng generate @angular/core:control-flow` |
| **`inject()`** au lieu de l'injection par constructeur | `ng generate @angular/core:inject` |
| **Entrées en signaux** (`@Input` → `input()`) | `ng generate @angular/core:signal-input-migration` |
| **Sorties** (`@Output` → `output()`) | `ng generate @angular/core:output-migration` |
| **Requêtes en signaux** (`@ViewChild` → `viewChild()`) | `ng generate @angular/core:signal-queries-migration` |
| **Routes paresseuses** (`loadChildren` + `NgModule` → composants) | `ng generate @angular/core:route-lazy-loading` |
| **Balises auto-fermantes** | `ng generate @angular/core:self-closing-tag` |
| **Nettoyer les imports inutilisés** | `ng generate @angular/core:cleanup-unused-imports` |
| **Karma → Vitest** | `ng generate @angular/core:karma-to-vitest` |
| **Builder webpack → `application` (esbuild)** | `ng update @angular/cli --name use-application-builder` |

La migration `standalone` se fait en **trois passes**, à relancer **dans l'ordre** : (1) *convert-to-standalone* (transforme composants, directives et tubes en autonomes) → (2) *prune-ng-modules* (supprime les `NgModule` devenus vides) → (3) *standalone-bootstrap* (remplace `bootstrapModule` par `bootstrapApplication` et déplace la configuration dans `app.config.ts`). Compilez et testez **après chaque passe**.

**À savoir sur ces migrations**

- Elles acceptent généralement des options (par exemple limiter à un dossier avec `--path`, ou des modes comme `--best-effort-mode` / `--insert-todos` pour les migrations de signaux, qui laissent des commentaires `TODO` aux endroits non migrables automatiquement) : `ng generate @angular/core:<migration> --help` liste les options de **votre** version.
- Elles sont **conservatrices** : un cas ambigu est laissé tel quel plutôt que mal réécrit. Prévoyez **un passage manuel** sur les restes.
- La migration vers `inject()` peut conserver des constructeurs « rétrocompatibles » pour les classes héritées par des bibliothèques ; la migration des entrées en signaux **ne convertit pas** les usages qui **écrivent** dans la propriété (à réécrire en `model()` ou en événement).
- Après la migration du flux de contrôle, ajoutez un `track` pertinent (la migration utilise `track $index` ou l'identité de l'élément par défaut) : **relisez chaque `@for`**.
- Remplacement d'outils : **TSLint → ESLint** (`ng add angular-eslint`), **Protractor → Playwright / Cypress** (chapitre 17), **Karma → Vitest** (chapitre 16).

### 28.3 Passer en zoneless

Le mode **zoneless** supprime Zone.js (chapitre 18). La migration est **graduelle** :

1. Rendre l'état **réactif** : signaux, tube `async`, `markForCheck` pour le code qu'on ne peut pas encore convertir.
2. Adopter **`OnPush`** partout (cela révèle déjà la plupart des problèmes : ce qui ne fonctionne pas en `OnPush` ne fonctionnera pas en zoneless).
3. Activer `provideZonelessChangeDetection()` et retirer `zone.js` des `polyfills` (application **et** tests).
4. Corriger les composants qui modifiaient des **champs ordinaires** hors du cycle de vie (minuteries, promesses, rappels de bibliothèques) : les convertir en **signaux**.
5. Supprimer l'usage de `NgZone` (`onStable`, `run`, `runOutsideAngular`) devenu inutile.
6. Vérifier les **tests** (`await fixture.whenStable()` au lieu de `fakeAsync` / `detectChanges`) et les **bibliothèques tierces** (compatibilité zoneless).
7. Mesurer : taille du bundle (Zone.js en moins) et nombre de cycles de détection (Angular DevTools).

**Symptôme typique** d'une incompatibilité : « la vue ne se met pas à jour tant qu'on ne clique pas ailleurs ». Cause : une valeur modifiée hors d'un signal. Remède : la placer dans un signal.

### 28.4 Stratégie de migration d'une grande application

1. **Mettre à jour** vers la dernière version majeure (c'est la **première étape** : les migrations modernes supposent une version récente).
2. Migrer vers les **composants autonomes**, puis le **nouveau flux de contrôle**, puis `inject()`.
3. Passer au **builder esbuild** (`application`) ; retirer les options propres à webpack.
4. Adopter progressivement les **signaux** (`input`, `computed`, état de service), puis **zoneless** et **`OnPush`**.
5. Remplacer Karma par **Vitest**, Protractor par **Playwright / Cypress**, TSLint par **ESLint**.
6. Introduire les **Signal Forms** pour les **nouveaux** formulaires ; migrer les anciens au fil des évolutions.

> **À retenir.** Les anciennes et nouvelles approches **cohabitent** : migrez **progressivement**, par fonctionnalité.

**Méthode pour les grands projets**

- **Mesurer** d'abord : nombre de `NgModule`, de `*ngIf`, de constructeurs injectés, de composants `Default`… (une simple recherche donne un tableau de bord de progression).
- **Découper** en petites pull requests (un schematic, un dossier à la fois) plus faciles à relire.
- **Geler** les nouvelles fonctionnalités pendant les migrations les plus larges, ou les écrire **directement** au style moderne.
- **Imposer** le style moderne aux nouveaux fichiers par des **règles ESLint** (interdire `NgModule`, `*ngIf`, `@Input`…) : on arrête d'ajouter de la dette pendant qu'on la rembourse.
- **S'appuyer sur la CI** (build, tests, lint, budgets) pour rendre chaque étape sûre ; garder des **tests E2E** sur les parcours critiques, qui ne dépendent pas de l'implémentation interne.
- **Prévoir** un temps régulier de mise à jour (une version majeure par semestre) plutôt qu'une migration massive tous les trois ans.

### 28.5 Migrer depuis AngularJS (1.x)

AngularJS est **en fin de vie** (2022) : plus de correctifs, y compris de sécurité. Deux voies :

| Voie | Principe | Quand |
| --- | --- | --- |
| **Réécriture** par fonctionnalités | Nouvelle application Angular construite page par page ; l'ancienne reste en service jusqu'au remplacement | Application modeste, équipe disponible |
| **Hybride** (`@angular/upgrade`) | Les deux frameworks **cohabitent** dans la même page : composants AngularJS utilisables depuis Angular et inversement, services partagés | Grande application, migration étalée |

Dans la pratique : planifiez une migration **par pages** (« étrangler » l'ancien code progressivement), avec un **routeur commun** pendant la transition, un **inventaire** des dépendances AngularJS (directives tierces sans équivalent), et une **couverture de tests** suffisante avant de toucher. Préparez d'abord l'ancien code (composants plutôt que contrôleurs, TypeScript, structure par fonctionnalité) : c'est la **préparation** qui fait la différence.

### 28.6 Problèmes fréquents

| Symptôme | Cause / solution |
| --- | --- |
| `ng update` refuse de s'exécuter | Commit en attente (`--allow-dirty`), ou version non supportée : avancer d'**une** version majeure |
| Conflits de dépendances (`peer deps`) | Mettre à jour les bibliothèques, ou `--legacy-peer-deps` temporairement |
| `NullInjectorError` après migration | Fournisseur manquant dans `app.config.ts` (`provideHttpClient()`, `provideRouter()`) |
| Erreurs de gabarit nouvelles | Mode `strictTemplates` : corriger les types |
| Avertissements `NgIf` / `NgFor` dépréciés | Lancer la migration `control-flow` |
| Tests cassés (Zone.js) | Migrer vers `await fixture.whenStable()`, ou conserver Zone.js dans la configuration de test |
| Webpack déprécié | Migrer vers le builder `application` |
| Vues qui ne se rafraîchissent plus (zoneless / `OnPush`) | Valeurs modifiées hors des signaux : les convertir |
| Build plus lent / plus gros après migration | Options webpack résiduelles, dépendances CommonJS, imports statiques qui annulent le chargement paresseux |

### 28.7 Après la migration

- Reconstruire et **comparer les tailles de bundle** et les performances (avant / après).
- Mettre à jour la **CI**, le **Dockerfile** (version de Node), la **documentation**.
- Activer progressivement les nouveaux **diagnostics** du compilateur et règles ESLint.
- Supprimer le **code mort** laissé par les migrations (`cleanup-unused-imports`, anciens modules, polyfills).
- Consigner les **décisions** et les points restants (dette identifiée) pour la prochaine mise à jour.

### Synthèse du chapitre 28

Mettre à jour **une version majeure à la fois** avec `ng update`, sur une branche propre, tests verts, en lisant le **guide de mise à jour**. Les **schematics** de migration (autonome, flux de contrôle, `inject`, signaux, Vitest, builder `application`) se lancent **indépendamment** et se **relisent**. Le **zoneless** se prépare par les signaux et `OnPush`. Pour les grandes applications : migrer **progressivement**, **mesurer**, **interdire** le style ancien par lint, s'appuyer sur la CI. AngularJS : réécriture ou hybride, **par pages**.

---

## 29. Nouveautés par version et bonnes pratiques

**Objectifs d'apprentissage.** Savoir **convertir** les anciennes pratiques en pratiques actuelles ; situer les **versions** dans le temps et leurs fonctionnalités majeures ; appliquer une **liste de bonnes pratiques** par domaine ; organiser un projet ; repérer les **anti-patterns** ; poursuivre sa formation.

### 29.1 Anciennes pratiques → pratiques actuelles

| Avant | Aujourd'hui |
| --- | --- |
| `NgModule`, `declarations` | **Composants autonomes** + `imports` |
| `*ngIf`, `*ngFor`, `*ngSwitch` | **`@if`, `@for` (avec `track`), `@switch`** |
| `@Input()`, `@Output()`, `EventEmitter` | **`input()`, `output()`, `model()`** |
| `@ViewChild`, `@ContentChild` | **`viewChild()`, `contentChild()`** |
| Constructeur pour l'injection | **`inject()`** |
| `BehaviorSubject` pour l'état | **`signal()`**, `computed()` |
| `ngOnChanges` | `computed()` / `effect()` sur les signaux d'entrée |
| `ngOnDestroy` + `Subscription` | **`takeUntilDestroyed()`**, `DestroyRef`, `toSignal` |
| Zone.js | **Zoneless** |
| Détection `Default` | **`OnPush`** (défaut en v22) |
| `HttpClientModule`, intercepteurs en classes | **`provideHttpClient()`**, intercepteurs **fonctionnels** |
| Gardes en classes | **Gardes fonctionnelles** |
| `RouterModule.forRoot()` | **`provideRouter()`** |
| `@Injectable` seul | `providedIn: 'root'` (ou `@Service()` en v22, voir chapitre 7) |
| Formulaires réactifs (nouveau code) | **Signal Forms** |
| `@angular/animations` | **`animate.enter` / `animate.leave`** (CSS) |
| Karma + Jasmine | **Vitest** |
| Protractor | **Playwright / Cypress** |
| TSLint | **ESLint** (`angular-eslint`) |
| Angular Universal | **`@angular/ssr`** |
| webpack | **esbuild / Vite** (`@angular/build:application`) |
| `rxjs/operators` | `import { map } from 'rxjs'` |
| Fichiers `x.component.ts` | `x.ts` (convention v20+) |

### 29.2 Chronologie des fonctionnalités marquantes

| Version | Date | À retenir |
| --- | --- | --- |
| 14 | juin 2022 | Composants autonomes (aperçu), `inject()`, formulaires typés |
| 15 | nov. 2022 | Composants autonomes stables, API `provide*`, gardes fonctionnelles, `NgOptimizedImage` |
| 16 | mai 2023 | **Signaux** (aperçu), hydratation (aperçu), entrées obligatoires |
| 17 | nov. 2023 | **`@if` / `@for` / `@defer`**, esbuild + Vite par défaut, nouveau logo |
| 18 | mai 2024 | Zoneless (expérimental), Material 3, `@let` |
| 19 | nov. 2024 | Autonome par défaut, hydratation incrémentale, `linkedSignal`, `resource` (aperçus) |
| 20 | mai 2025 | Signaux **stables**, `httpResource`, zoneless en aperçu développeur, convention de noms sans suffixes |
| 21 | nov. 2025 | **Zoneless par défaut**, **Vitest par défaut**, Signal Forms (expérimental), Aria (aperçu) |
| **22** | **juin 2026** | **Signal Forms** et **resources** stables, **`OnPush`** par défaut, Aria stable, builders webpack dépréciés, outils pour agents d'IA (compétences « Agent Skills », support expérimental de WebMCP) |

> **À retenir.** Les détails exacts de chaque version se trouvent dans l'**annonce officielle** (« Announcing Angular vNN ») sur [blog.angular.dev](https://blog.angular.dev) et dans le journal des modifications GitHub. Cette chronologie résume les **tendances** : de l'architecture à modules vers les **composants autonomes**, de Zone.js vers les **signaux et le zoneless**, de webpack vers **esbuild / Vite**, de Karma vers **Vitest**, des formulaires à objets mutables vers les **Signal Forms**.

**Lecture de la chronologie.** Trois chantiers structurent la décennie récente : (1) **simplifier** le modèle de composition (autonome, `inject`, `provide*`) ; (2) **rendre la réactivité explicite et fine** (signaux, `linkedSignal`, `resource`, zoneless, `OnPush` par défaut) ; (3) **moderniser l'outillage** (esbuild, Vite, Vitest, SSR intégré, hydratation incrémentale). Chaque version apporte aussi des correctifs de sécurité et des dépréciations : la mise à jour régulière est la manière la moins coûteuse de rester en phase.

### 29.3 Bonnes pratiques générales

| Domaine | Pratique |
| --- | --- |
| **Architecture** | Organiser par **fonctionnalité** (`features/`), séparer *présentation* (composants « bêtes ») et *logique* (services / stores) |
| **Composants** | Autonomes, petits, `OnPush`, état en **signaux**, `computed()` plutôt que des méthodes dans le gabarit |
| **Gabarits** | `@for` avec `track`, pas de logique complexe, `@defer` pour le non-critique |
| **Services** | `providedIn: 'root'`, `inject()`, état exposé en lecture seule |
| **RxJS** | Pour les flux ; `takeUntilDestroyed`, `async` / `toSignal`, jamais de `subscribe` imbriqués |
| **Typage** | Mode strict, `strictTemplates`, pas de `any` |
| **Performance** | Zoneless, routes paresseuses, SSR / pré-rendu, `NgOptimizedImage`, budgets |
| **Tests** | Vitest + TestBed, harnais, Playwright pour les parcours critiques |
| **Qualité** | ESLint (`angular-eslint`), Prettier, hooks Git, CI (build + tests + lint) |
| **Accessibilité** | HTML sémantique, ARIA, navigation au clavier, contrastes (CDK a11y, Angular Aria) |
| **Sécurité** | Aucun contournement d'assainissement, CSP, contrôles côté serveur, dépendances à jour |
| **Mises à jour** | Rester **à jour** : une version majeure tous les 6 mois, migrations automatiques |

**Anti-patterns à repérer en revue de code**

- `any` pour « faire passer » le compilateur ; `!` (assertion non nulle) à répétition.
- `subscribe()` imbriqués ou sans désabonnement ; `BehaviorSubject` exposé et modifié de partout.
- Logique métier ou appels HTTP **dans les composants** plutôt que dans des services.
- Méthodes coûteuses appelées dans les gabarits ; `@for` sans identité stable.
- Mutation d'objets ou de tableaux dans des signaux ou des entrées `OnPush`.
- `effect()` utilisé pour propager un état à un autre signal (utiliser `computed` / `linkedSignal`).
- `innerHTML`, `bypassSecurityTrust*`, secrets ou jetons dans `localStorage` / le bundle.
- Composants géants (plusieurs centaines de lignes de gabarit) et dépendances circulaires.
- Imports statiques qui annulent le chargement paresseux ; bibliothèques lourdes importées entièrement.
- Tests qui dépendent de l'ordre d'exécution, de minuteries réelles ou de détails d'implémentation.

**Liste de contrôle d'une revue de pull request** : typage strict respecté ; composants `OnPush` avec signaux ; `track` présent ; pas de fuite (désabonnement, `DestroyRef`) ; accessibilité (libellés, clavier, contrastes) ; compatibilité SSR (`afterNextRender`) ; tests ajoutés ou mis à jour ; budgets de taille respectés ; aucune donnée sensible exposée ; documentation / changelog mis à jour.

### 29.4 Structure de projet recommandée

Par souci de lisibilité, les exemples de ce cours placent les fichiers à plat sous `src/app/`. Dans un projet réel, rangez-les comme ci-dessous (par exemple `auth/` et `http/` sous `core/`).

```text
src/app/
├── core/                  ← services singleton, intercepteurs, gardes, configuration
│   ├── auth/
│   └── http/
├── shared/                ← composants, directives et tubes réutilisables (sans état global)
├── features/
│   ├── produits/
│   │   ├── produits.routes.ts
│   │   ├── liste/        ← composants de la page
│   │   ├── detail/
│   │   └── produits.store.ts
│   └── compte/
├── app.ts
├── app.config.ts
└── app.routes.ts
```

**Règles de dépendance.** `features` peut dépendre de `shared` et `core` ; `shared` ne dépend d'aucune feature ; une feature ne dépend **pas** d'une autre feature (elles communiquent par des services de `core` ou par l'URL). Dans un monorepo (chapitre 15), faites respecter ces règles par l'outillage (Nx `enforce-module-boundaries`).

### 29.5 Parcours d'apprentissage et ressources

**Parcours conseillé** : (1) chapitres 1 à 8 (bases, composants, gabarits, services, signaux) ; (2) 9 à 12 (routage, formulaires, HTTP, RxJS) ; (3) 16 et 18 à 19 (tests, détection des changements, chargement paresseux) ; (4) 22, 26 et 27 (SSR, sécurité, authentification) selon vos besoins ; (5) le reste en fonction des projets.

- **Documentation officielle** : <https://angular.dev>
- **Tutoriels interactifs** (dans le navigateur) : <https://angular.dev/tutorials>
- **Guide de mise à jour** : <https://angular.dev/update-guide>
- **Blog Angular** : <https://blog.angular.dev>
- **NgRx** : <https://ngrx.io> · **Angular Material** : <https://material.angular.dev> · **Nx** : <https://nx.dev>
- **Sécurité Angular** : <https://angular.dev/best-practices/security>
- **Accessibilité** : <https://angular.dev/best-practices/a11y>

### Synthèse du chapitre 29

L'Angular actuel, c'est : **composants autonomes**, **signaux**, **`@if` / `@for`**, **`inject()`**, **zoneless + `OnPush`**, **Vitest**, **esbuild / Vite**, **SSR intégré** et **Signal Forms**. Appliquez les bonnes pratiques par domaine, structurez par **fonctionnalité**, relisez le code avec une liste de contrôle, et **restez à jour** version après version.

---

*Fin du cours. Bon développement avec Angular !*
