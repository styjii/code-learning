<div align="center">

# Angular — Guide complet

**Des composants autonomes aux signaux, du SSR aux tests, avec Angular 22**

*Mis à jour pour Angular 22 (octobre 2026)*

</div>

---

## Ressources

| Ressource | Lien |
| --- | --- |
| Documentation officielle | [angular.dev](https://angular.dev) |
| Guide de mise à jour | [angular.dev/update-guide](https://angular.dev/update-guide) |
| Calendrier et versions | [angular.dev/reference/releases](https://angular.dev/reference/releases) |
| Exercices, solutions et projets | Bientôt disponibles |

---

## Sommaire

**Fondamentaux**

1. [Introduction à Angular](#1-introduction-à-angular)
2. [TypeScript pour Angular](#2-typescript-pour-angular)
3. [Installation et structure d'un projet](#3-installation-et-structure-dun-projet)
4. [Composants](#4-composants)
5. [Modèles et liaison de données](#5-modèles-et-liaison-de-données)
6. [Directives et tubes (*pipes*)](#6-directives-et-tubes-pipes)
7. [Services et injection de dépendances](#7-services-et-injection-de-dépendances)
8. [Signaux et réactivité](#8-signaux-et-réactivité)
9. [Routage et navigation](#9-routage-et-navigation)
10. [Formulaires](#10-formulaires)

**Avancé**

11. [Client HTTP](#11-client-http)
12. [Observables et RxJS](#12-observables-et-rxjs)
13. [Gestion d'état](#13-gestion-détat)
14. [Animations](#14-animations)
15. [Bibliothèques et espaces de travail](#15-bibliothèques-et-espaces-de-travail)

**Tests**

16. [Tests unitaires](#16-tests-unitaires)
17. [Tests de bout en bout (E2E)](#17-tests-de-bout-en-bout-e2e)

**Performance**

18. [Détection des changements](#18-détection-des-changements)
19. [Chargement paresseux et vues différées](#19-chargement-paresseux-et-vues-différées)
20. [Compilation AOT et optimisation du bundle](#20-compilation-aot-et-optimisation-du-bundle)

**Essentiels**

21. [Internationalisation (i18n)](#21-internationalisation-i18n)
22. [Rendu côté serveur (SSR), pré-rendu et hydratation](#22-rendu-côté-serveur-ssr-pré-rendu-et-hydratation)
23. [Applications web progressives (PWA)](#23-applications-web-progressives-pwa)
24. [Angular Material, CDK et Aria](#24-angular-material-cdk-et-aria)
25. [Bibliothèques tierces](#25-bibliothèques-tierces)
26. [Sécurité](#26-sécurité)
27. [Authentification et autorisation](#27-authentification-et-autorisation)
28. [Migration et mises à jour](#28-migration-et-mises-à-jour)
29. [Nouveautés par version et bonnes pratiques](#29-nouveautés-par-version-et-bonnes-pratiques)

> **Légende** : *(ajout)* = notion absente du guide d'origine ; *(à jour)* = pratique moderne remplaçant une ancienne ; *(héritage)* = ancienne approche, toujours rencontrée dans les projets existants.
>
> **Remarque importante** : le guide d'origine décrivait l'Angular « classique » (`NgModule`, `*ngIf`, `*ngFor`, `@Input()`, Karma…). **Angular a profondément changé depuis la version 14** : composants **autonomes** (*standalone*), **signaux**, nouveau **flux de contrôle** `@if` / `@for`, **zoneless**, **Vitest**, **Signal Forms**. Ce guide enseigne l'approche **actuelle** et explique l'ancienne pour pouvoir lire du code existant.

---

# Fondamentaux

---

# 1. Introduction à Angular

## 1.1 Qu'est-ce qu'Angular ?

**Angular** est un **framework** open source, développé par **Google**, pour créer des **applications web monopages** (*SPA*) et des applications web complètes. Il est écrit en **TypeScript** et fournit « tout inclus » : composants, routage, formulaires, client HTTP, injection de dépendances, tests, outils de build.

| Caractéristique | Détail |
| --- | --- |
| Architecture | **Composants** + **services** + **injection de dépendances** |
| Langage | **TypeScript** (obligatoire en pratique) |
| Réactivité | **Signaux** (`signal`) et **RxJS** (flux asynchrones) |
| Rendu | Côté client, côté serveur (**SSR**), pré-rendu (**SSG**), hydratation |
| Outils | **Angular CLI** (`ng`) : génération, build, tests, mises à jour |
| Cadence | Une version majeure **tous les 6 mois** (mai et novembre), avec un guide de migration automatisé |

## 1.2 AngularJS ≠ Angular

| | **AngularJS** (1.x) | **Angular** (2+) |
| --- | --- | --- |
| Langage | JavaScript | **TypeScript** |
| Architecture | MVC / `$scope` | **Composants** |
| Statut | **Fin de vie en 2022** | Maintenu |

> **Attention** : ne confondez pas les deux ; « Angular » désigne aujourd'hui **uniquement** Angular 2+.

## 1.3 Pourquoi choisir Angular ?

- **Structure claire** et conventions fortes : idéal pour de **grandes équipes** et des projets **long terme**.
- **Écosystème officiel intégré** : routeur, formulaires, HTTP, i18n, tests, Material.
- **Mises à jour guidées** (`ng update`) et **support à long terme**.
- **Performance** : compilation AOT, *tree-shaking*, vues différées, SSR, hydratation, **zoneless**.

### Comparaison avec React et Vue

| | **Angular** | **React** | **Vue** |
| --- | --- | --- | --- |
| Type | Framework complet | Bibliothèque d'interface | Framework progressif |
| Langage | TypeScript | JavaScript / TypeScript (JSX) | JS / TS (gabarits) |
| Réactivité | Signaux + RxJS | État + hooks | `ref` / `reactive` |
| Routage / formulaires / HTTP | **Inclus** | Bibliothèques tierces | Écosystème officiel |
| Courbe d'apprentissage | Plus raide | Moyenne | Douce |
| Idéal pour | Grandes applications d'entreprise | Flexibilité maximale | Prise en main rapide |

## 1.4 Versions et support *(à jour)*

Chaque version majeure est supportée **18 mois** (6 mois de support actif + 12 mois de correctifs critiques).

| Version | Date | Points marquants |
| --- | --- | --- |
| **17** | nov. 2023 | Nouveau flux de contrôle `@if/@for`, **`@defer`**, builder **esbuild + Vite**, projets **autonomes** |
| **18** | mai 2024 | Zoneless (expérimental), Material 3, `@let` |
| **19** | nov. 2024 | Composants **autonomes par défaut**, hydratation incrémentale, `linkedSignal` et `resource` (aperçus) |
| **20** | mai 2025 | **API de signaux stables**, `httpResource`, nouvelle convention de nommage des fichiers, Vitest expérimental |
| **21** | nov. 2025 | **Zoneless par défaut**, **Vitest par défaut**, Signal Forms (expérimental), Angular Aria (aperçu) |
| **22** | **juin 2026** | **Signal Forms stables**, `resource` / `httpResource` stables, **`OnPush` par défaut**, Angular Aria stable, builders **webpack dépréciés**, outils pour agents d'IA |

> **À retenir** : la version à utiliser aujourd'hui est **Angular 22** (ou la plus récente). Consultez [angular.dev/reference/versions](https://angular.dev/reference/versions) pour la compatibilité avec **Node.js** et **TypeScript**.

## 1.5 Prérequis

- **HTML, CSS, JavaScript moderne** (ES2020+), notions de **TypeScript**.
- **Node.js** (version LTS compatible avec la version d'Angular) et **npm**.
- Un éditeur : **VS Code** avec l'extension **Angular Language Service**.

---

# 2. TypeScript pour Angular

*Rappel des notions TypeScript indispensables (voir le guide TypeScript complet pour le détail).*

## 2.1 Types et interfaces

```typescript
// src/app/modeles.ts
let nom: string = "Alice";
let age: number = 30;
let actif: boolean = true;
let ids: number[] = [1, 2, 3];
let paire: [string, number] = ["Alice", 30];

export interface Utilisateur {
    id: number;
    nom: string;
    email?: string;              // optionnelle
    readonly creeLe: Date;
}

export type Role = "admin" | "editeur" | "lecteur";           // union de littéraux

const utilisateur: Utilisateur = { id: 1, nom, creeLe: new Date() };
const role: Role = "admin";
console.log(nom, age, actif, ids, paire, utilisateur, role);
```

## 2.2 Fonctions, génériques, classes

```typescript
const additionner = (a: number, b: number): number => a + b;

function premier<T>(elements: T[]): T | undefined { return elements[0]; }

class Compte {
    #solde = 0;                                         // privé natif
    constructor(public readonly titulaire: string) {}
    deposer(m: number): void { this.#solde += m; }
    get solde(): number { return this.#solde; }
}

const compte = new Compte("Alice");
compte.deposer(50);
console.log(additionner(2, 3));                         // 5
console.log(premier(["a", "b"]));                       // "a"
console.log(compte.titulaire, compte.solde);            // "Alice" 50
```

## 2.3 Décorateurs

Angular utilise des **décorateurs** (`@Component`, `@Injectable`, `@Directive`, `@Pipe`, `@NgModule`) : des fonctions qui ajoutent des **métadonnées** à une classe. Ils sont fournis par le compilateur Angular ; vous n'avez rien à configurer.

## 2.4 Mode strict

Les nouveaux projets Angular activent le mode **strict** de TypeScript **et** des **gabarits** (`strictTemplates`) : le compilateur vérifie aussi les types **dans les templates HTML**.

```jsonc
// tsconfig.json
{ "compilerOptions": { "strict": true, "noImplicitOverride": true, "noPropertyAccessFromIndexSignature": true },
  "angularCompilerOptions": { "strictTemplates": true, "strictInjectionParameters": true } }
```

## 2.5 Modules JavaScript

```typescript
// src/app/mon-service.ts
import { Injectable, signal } from "@angular/core";
import type { Utilisateur } from "./modeles";          // import de type uniquement (fichier de la section 2.1)

@Injectable({ providedIn: "root" })
export class MonService {
    readonly utilisateur = signal<Utilisateur | null>(null);
}
```

---

# 3. Installation et structure d'un projet

## 3.1 Installer l'Angular CLI

```bash
node --version                            # Node.js compatible (voir angular.dev/reference/versions)
npm install -g @angular/cli
ng version
```

> **Astuce** : pour éviter l'installation globale, utilisez `npx @angular/cli@latest new mon-app`.

## 3.2 Créer et lancer un projet

```bash
ng new mon-app                            # assistant : style (CSS/SCSS), SSR ?, etc.
cd mon-app
ng serve --open                           # serveur de développement : http://localhost:4200
```

Options utiles : `--ssr` (rendu serveur), `--style=scss`, `--routing`, `--skip-git`.

## 3.3 Commandes principales du CLI

| Commande | Rôle |
| --- | --- |
| `ng serve` | Serveur de développement avec rechargement à chaud |
| `ng build` | Compile pour la production (`dist/`) |
| `ng test` | Lance les tests unitaires (**Vitest** par défaut) |
| `ng generate component x` (`ng g c x`) | Génère un composant |
| `ng g service`, `directive`, `pipe`, `guard`, `interceptor`, `class`, `interface`, `enum`, `library` | Autres générateurs |
| `ng add <paquet>` | Installe **et configure** une bibliothèque (`@angular/material`, `@angular/pwa`, `@angular/ssr`) |
| `ng update` | Met à jour Angular et migre le code |
| `ng lint` | Analyse du code (ESLint, après `ng add angular-eslint`) |
| `ng e2e` | Tests de bout en bout (après ajout d'un outil) |
| `ng deploy` | Déploie (après ajout d'un builder de déploiement) |

## 3.4 Structure d'un projet

```text
mon-app/
├── src/
│   ├── app/
│   │   ├── app.ts                  ← composant racine (classe `App`)
│   │   ├── app.html / app.css      ← gabarit et styles
│   │   ├── app.config.ts           ← configuration de l'application (providers)
│   │   ├── app.routes.ts           ← routes
│   │   └── app.spec.ts             ← test unitaire
│   ├── index.html                  ← page hôte (<app-root>)
│   ├── main.ts                     ← point d'entrée : bootstrapApplication()
│   ├── styles.css                  ← styles globaux
│   └── assets/ ou public/          ← ressources statiques
├── angular.json                    ← configuration du CLI (build, test, serve…)
├── tsconfig.json
└── package.json
```

> **Convention de nommage (à jour)** : depuis la **version 20**, le CLI ne génère plus les suffixes `.component` / `.service` : on obtient `compteur.ts` (classe `Compteur`) au lieu de `compteur.component.ts` (classe `CompteurComponent`). Les deux styles restent valides ; les migrations automatiques conservent les suffixes des projets existants. Dans ce guide, nous utilisons le style **récent**.

## 3.5 Le point d'entrée : `main.ts` et `app.config.ts`

```typescript
// src/main.ts
import { bootstrapApplication } from "@angular/platform-browser";
import { appConfig } from "./app/app.config";
import { App } from "./app/app";

bootstrapApplication(App, appConfig).catch((erreur) => console.error(erreur));
```

```typescript
// src/app/app.config.ts
import { ApplicationConfig, provideBrowserGlobalErrorListeners, provideZonelessChangeDetection } from "@angular/core";
import { provideRouter } from "@angular/router";
import { provideHttpClient, withFetch } from "@angular/common/http";
import { routes } from "./app.routes";

export const appConfig: ApplicationConfig = {
    providers: [
        provideBrowserGlobalErrorListeners(),
        provideZonelessChangeDetection(),                       // sans Zone.js (par défaut dans les nouveaux projets)
        provideRouter(routes),
        provideHttpClient(withFetch()),
    ],
};
```

Le **composant racine** :

```typescript
// src/app/app.ts
import { Component } from "@angular/core";
import { RouterOutlet } from "@angular/router";

@Component({
    selector: "app-root",
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

## 3.6 Construire l'application *(à jour)*

Le builder par défaut est **`@angular/build:application`** (basé sur **esbuild** et **Vite**) : builds et rechargements **très rapides**, SSR et pré-rendu intégrés. Les anciens builders **webpack** (`@angular-devkit/build-angular`) sont **dépréciés** (v22) : voir [section 28](#28-migration-et-mises-à-jour).

```bash
ng build                           # production par défaut : optimisation, minification, AOT
ng build --configuration development
ng build --stats-json              # statistiques pour analyser le bundle
```

## 3.7 Le fichier `angular.json`

Définit les projets, les **cibles** (`build`, `serve`, `test`) et les **configurations** (`production`, `development`) : budgets de taille, fichiers de remplacement (environnements), assets, styles globaux, SSR, etc.

---

# 4. Composants

## 4.1 Les briques d'une application

Une application Angular est un **arbre de composants**. Un **composant** associe :

| Élément | Rôle |
| --- | --- |
| **Classe TypeScript** | Données et logique |
| **Gabarit** (*template*) | HTML avec syntaxe Angular |
| **Styles** | CSS **encapsulé** par composant |
| **Métadonnées** `@Component` | Sélecteur, imports, gabarit, styles… |

## 4.2 Composants autonomes (*standalone*) *(à jour)*

Un composant **autonome** déclare **lui-même** ses dépendances dans `imports` : **plus besoin de `NgModule`**. C'est le mode **par défaut** depuis la version 19.

```typescript
import { Component, signal, ChangeDetectionStrategy } from "@angular/core";

@Component({
    selector: "app-compteur",                    // balise : <app-compteur />
    imports: [],                                  // composants, directives, tubes utilisés dans le gabarit
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
    protected readonly valeur = signal(0);
    incrementer(): void {                           // publique : appelable depuis un parent (voir section 5.5)
        this.valeur.update((v) => v + 1);
    }
}
```

Créer un composant : `ng generate component compteur` (génère `compteur.ts`, `compteur.html`, `compteur.css`, `compteur.spec.ts`).

> **Gabarit séparé** : utilisez `templateUrl: './compteur.html'` et `styleUrl: './compteur.css'` pour les composants non triviaux.

## 4.3 Utiliser un composant dans un autre

```typescript
import { Component } from "@angular/core";
import { Compteur } from "./compteur";

@Component({
    selector: "app-accueil",
    imports: [Compteur],                          // on importe le composant utilisé
    template: `<app-compteur />`,
})
export class Accueil {}
```

> Balises **auto-fermantes** (`<app-compteur />`) autorisées dans les gabarits Angular modernes.

## 4.4 Entrées et sorties avec les **signaux** *(à jour)*

Les fonctions **`input()`**, **`output()`** et **`model()`** remplacent les décorateurs `@Input()` / `@Output()`.

```typescript
import { Component, input, output, model, computed } from "@angular/core";
import { CurrencyPipe } from "@angular/common";

@Component({
    selector: "app-carte-produit",
    imports: [CurrencyPipe],
    template: `
        <article>
            <h3>{{ nom() }}</h3>
            <p>{{ prixTtc() | currency: "EUR" }} (quantité : {{ quantite() }})</p>
            <button (click)="ajouter.emit(nom())">Ajouter</button>
        </article>
    `,
})
export class CarteProduit {
    nom = input.required<string>();                         // entrée OBLIGATOIRE (signal en lecture seule)
    prix = input(0);                                         // entrée avec valeur par défaut
    tva = input(0.2, { alias: "tauxTva", transform: Number });   // alias et transformation

    ajouter = output<string>();                              // sortie typée (remplace EventEmitter)
    quantite = model(1);                                     // entrée + sortie : liaison bidirectionnelle

    prixTtc = computed(() => this.prix() * (1 + this.tva()));
}
```

Utilisation par le parent :

```typescript
import { Component, signal } from "@angular/core";
import { CarteProduit } from "./carte-produit";

@Component({
    selector: "app-catalogue",
    imports: [CarteProduit],
    template: `
        <app-carte-produit [nom]="'Livre'" [prix]="12.5" (ajouter)="surAjout($event)" [(quantite)]="qte" />
    `,
})
export class Catalogue {
    protected readonly qte = signal(1);
    protected surAjout(nom: string): void {
        console.log(`Ajouté : ${nom}`);
    }
}
```

| API signal | Remplace | Particularités |
| --- | --- | --- |
| `input<T>()` / `input.required<T>()` | `@Input()` | Lecture via `valeur()`, réactif, typé strictement |
| `output<T>()` | `@Output() + EventEmitter` | `.emit(valeur)` |
| `model<T>()` | `@Input() + @Output() xChange` | Liaison **bidirectionnelle** `[(x)]` |
| `viewChild()`, `viewChildren()`, `contentChild()`, `contentChildren()` | `@ViewChild` etc. | Requêtes sous forme de signaux |

> *(héritage)* Les décorateurs `@Input()` / `@Output()` restent valides. Migration automatique : `ng generate @angular/core:signal-input-migration` (voir section 28).

## 4.5 Requêtes sur la vue : `viewChild`

```typescript
import { Component, viewChild, ElementRef, afterNextRender } from "@angular/core";

@Component({
    selector: "app-recherche",
    template: `<input #champ type="search" />`,
})
export class Recherche {
    champ = viewChild.required<ElementRef<HTMLInputElement>>("champ");

    constructor() {
        afterNextRender(() => this.champ().nativeElement.focus());      // après le premier rendu
    }
}
```

## 4.6 Cycle de vie

| Hook | Moment |
| --- | --- |
| `constructor` | Création (injection de dépendances) |
| `ngOnChanges` | Une entrée **classique** change |
| `ngOnInit` | Après l'initialisation des entrées |
| `ngDoCheck` | À chaque détection de changements |
| `ngAfterContentInit` / `Checked` | Contenu projeté initialisé |
| `ngAfterViewInit` / `Checked` | Vue et enfants initialisés |
| `ngOnDestroy` | Avant la destruction : **nettoyage** |

```typescript
import { Component, OnInit, OnDestroy } from "@angular/core";

@Component({
    selector: "app-horloge",
    template: `<p>Horloge en marche (voir la console)</p>`,
})
export class Horloge implements OnInit, OnDestroy {
    private minuteur?: ReturnType<typeof setInterval>;
    ngOnInit(): void { this.minuteur = setInterval(() => console.log("tic"), 1000); }
    ngOnDestroy(): void { clearInterval(this.minuteur); }
}
```

### Hooks modernes *(à jour)*

Avec les signaux, on préfère :

| API | Rôle |
| --- | --- |
| `effect(() => …)` | Réagit aux changements de signaux |
| `afterNextRender()` / `afterEveryRender()` | Code dépendant du **DOM** (jamais exécuté côté serveur) |
| `inject(DestroyRef).onDestroy(fn)` | Nettoyage sans implémenter `OnDestroy` |
| `takeUntilDestroyed()` | Désabonnement automatique des observables |

```typescript
import { Component, DestroyRef, inject } from "@angular/core";

@Component({
    selector: "app-horloge-moderne",
    template: `<p>Horloge en marche (voir la console)</p>`,
})
export class HorlogeModerne {
    constructor() {
        const id = setInterval(() => console.log("tic"), 1000);
        inject(DestroyRef).onDestroy(() => clearInterval(id));
    }
}
```

## 4.7 Projection de contenu (`ng-content`)

```typescript
import { Component } from "@angular/core";

@Component({
    selector: "app-panneau",
    template: `
        <header><ng-content select="[titre]" /></header>
        <section><ng-content /></section>                  <!-- contenu par défaut -->
    `,
})
export class Panneau {}
```

```typescript
import { Component } from "@angular/core";
import { Panneau } from "./panneau";

@Component({
    selector: "app-page",
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

## 4.8 Encapsulation des styles

| Mode | Effet |
| --- | --- |
| `Emulated` (**défaut**) | Styles limités au composant (attributs générés) |
| `ShadowDom` | Vrai Shadow DOM natif |
| `None` | Styles globaux |

```typescript
import { Component, ViewEncapsulation } from "@angular/core";

@Component({
    selector: "app-isole",
    template: `<p>Contenu isolé dans un Shadow DOM</p>`,
    styles: `p { color: seagreen; }`,
    encapsulation: ViewEncapsulation.ShadowDom,
})
export class Isole {}
```

Sélecteurs spéciaux : `:host` (l'élément du composant), `:host-context()`, `::ng-deep` (déprécié).

## 4.9 Liaisons sur l'hôte

```typescript
import { Component, signal } from "@angular/core";

@Component({
    selector: "app-bouton",
    host: {
        class: "bouton",
        "[class.actif]": "actif()",
        "[attr.aria-pressed]": "actif()",
        "(click)": "basculer()",
    },
    template: `<ng-content />`,
})
export class Bouton {
    protected readonly actif = signal(false);
    protected basculer(): void { this.actif.update((a) => !a); }
}
```

> **Bonne pratique** : préférez la propriété **`host`** de `@Component` aux décorateurs `@HostBinding` / `@HostListener`.

## 4.10 Modules `NgModule` *(héritage)*

Avant la version 14, tout composant devait être **déclaré** dans un **`NgModule`**. Ce modèle est toujours supporté, mais **n'est plus recommandé** pour le nouveau code.

```typescript
import { NgModule } from "@angular/core";
import { BrowserModule } from "@angular/platform-browser";
import { FormsModule } from "@angular/forms";
import { AppComponent } from "./app.component";
import { CompteurComponent } from "./compteur.component";

@NgModule({
    declarations: [AppComponent, CompteurComponent],
    imports: [BrowserModule, FormsModule],
    providers: [],
    bootstrap: [AppComponent],
})
export class AppModule {}
```

| | **Autonome** (*standalone*) | **`NgModule`** *(héritage)* |
| --- | --- | --- |
| Dépendances | `imports` du composant | `declarations` + `imports` du module |
| Amorçage | `bootstrapApplication(App, config)` | `platformBrowserDynamic().bootstrapModule(AppModule)` |
| Services globaux | `provide…()` dans `app.config.ts` | `providers` du module |
| Chargement paresseux | `loadComponent` / `loadChildren` vers des routes | `loadChildren` vers un module |
| Complexité | Moindre | Plus de code « de liaison » |

Migration : `ng generate @angular/core:standalone` (voir [section 28](#28-migration-et-mises-à-jour)). Les `NgModule` de bibliothèques (ex. `MatButtonModule`) restent importables directement dans `imports`.

## 4.11 Bonnes pratiques

- Composants **petits** et à responsabilité unique (présentation vs. logique).
- `ChangeDetectionStrategy.OnPush` (par défaut depuis la v22) ; état dans des **signaux**.
- `protected` pour ce qui n'est utilisé que dans le gabarit ; `readonly` pour les signaux.
- Pas de logique lourde dans le gabarit : utilisez `computed()`.

---

# 5. Modèles et liaison de données

## 5.1 Les quatre formes de liaison

| Forme | Syntaxe | Sens |
| --- | --- | --- |
| **Interpolation** | `{{ expression }}` | Classe → vue |
| **Liaison de propriété** | `[propriete]="expression"` | Classe → vue |
| **Liaison d'événement** | `(evenement)="action()"` | Vue → classe |
| **Liaison bidirectionnelle** | `[(ngModel)]="x"` / `[(x)]="signal"` | Les deux sens |

```typescript
import { Component, signal } from "@angular/core";
import { FormsModule } from "@angular/forms";

@Component({
    selector: "app-demo",
    imports: [FormsModule],
    template: `
        <h1>{{ titre() }}</h1>                                      <!-- interpolation -->
        <img [src]="urlImage()" [alt]="titre()" />                 <!-- propriété -->
        <button (click)="saluer()" [disabled]="!actif()">Salut</button>   <!-- événement + propriété -->
        <input [value]="nom()" (input)="nom.set($any($event.target).value)" />
        <input [(ngModel)]="texte" />                              <!-- bidirectionnelle -->
    `,
})
export class Demo {
    titre = signal("Mon titre");
    urlImage = signal("/img/logo.png");
    actif = signal(true);
    nom = signal("");
    texte = "";
    saluer(): void { console.log("Salut !"); }
}
```

## 5.2 Liaisons spécialisées

```typescript
import { Component, signal } from "@angular/core";

@Component({
    selector: "app-liaisons",
    template: `
        <div [class.actif]="estActif()" [class]="{ rouge: erreur(), gras: important() }">Texte</div>
        <div [style.width.px]="largeur()" [style.color]="couleur()">Barre</div>
        <table><tr><td [attr.colspan]="colonnes()" [attr.aria-label]="libelle()">Cellule</td></tr></table>
        <input #champ (keyup.enter)="valider(champ.value)" />     <!-- variable de référence + filtre de touche -->
    `,
})
export class Liaisons {
    protected readonly estActif = signal(true);
    protected readonly erreur = signal(false);
    protected readonly important = signal(true);
    protected readonly largeur = signal(120);
    protected readonly couleur = signal("steelblue");
    protected readonly colonnes = signal(2);
    protected readonly libelle = signal("Cellule de démonstration");
    protected valider(valeur: string): void { console.log(valeur); }
}
```

> Les **attributs** (`attr.`) servent aux attributs sans propriété DOM équivalente (ARIA, `colspan`, `data-*`).

## 5.3 Flux de contrôle : `@if`, `@for`, `@switch` *(à jour)*

Depuis la **version 17**, le **flux de contrôle intégré** remplace les directives structurelles `*ngIf`, `*ngFor` et `*ngSwitch` : syntaxe plus claire, **sans import**, plus rapide.

### `@if`

```html
@if (utilisateur(); as u) {
    <p>Bonjour {{ u.nom }}</p>
} @else if (chargement()) {
    <p>Chargement…</p>
} @else {
    <p>Veuillez vous connecter.</p>
}
```

### `@for`

```html
<ul>
    @for (produit of produits(); track produit.id; let i = $index, premier = $first) {
        <li [class.premier]="premier">{{ i + 1 }}. {{ produit.nom }}</li>
    } @empty {
        <li>Aucun produit</li>
    }
</ul>
```

- **`track` est obligatoire** : il identifie chaque élément (`track produit.id`, ou `track $index` pour des valeurs simples) afin de **réutiliser le DOM** : c'est un gain de performance majeur.
- Variables : `$index`, `$count`, `$first`, `$last`, `$even`, `$odd`.

### `@switch`

```html
@switch (role()) {
    @case ("admin") { <p>Panneau d'administration</p> }
    @case ("editeur") { <p>Espace d'édition</p> }
    @default { <p>Accès refusé</p> }
}
```

### Variables locales : `@let`

```html
@let total = prix() * quantite();
<p>Total : {{ total | currency }}</p>
```

### Exemple complet

Les quatre constructions précédentes réunies dans un composant exécutable :

```typescript
import { Component, signal } from "@angular/core";
import { CurrencyPipe } from "@angular/common";

interface Produit { id: number; nom: string; }
type Role = "admin" | "editeur" | "lecteur";

@Component({
    selector: "app-flux-controle",
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
            @case ("admin") { <p>Panneau d'administration</p> }
            @case ("editeur") { <p>Espace d'édition</p> }
            @default { <p>Accès refusé</p> }
        }

        @let total = prix() * quantite();
        <p>Total : {{ total | currency: "EUR" }}</p>
    `,
})
export class FluxControle {
    protected readonly utilisateur = signal<{ nom: string } | null>({ nom: "Alice" });
    protected readonly chargement = signal(false);
    protected readonly produits = signal<Produit[]>([{ id: 1, nom: "Livre" }, { id: 2, nom: "Stylo" }]);
    protected readonly role = signal<Role>("editeur");
    protected readonly prix = signal(12.5);
    protected readonly quantite = signal(2);
}
```

### Vues différées : `@defer`

Chargement **paresseux** d'un morceau de gabarit : voir [section 19](#19-chargement-paresseux-et-vues-différées).

### Tableau de correspondance (héritage)

| Ancienne syntaxe | Nouvelle syntaxe |
| --- | --- |
| `*ngIf="x; else autre"` | `@if (x) { … } @else { … }` |
| `*ngFor="let i of liste; trackBy: fn"` | `@for (i of liste; track i.id) { … }` |
| `[ngSwitch]` / `*ngSwitchCase` | `@switch` / `@case` |

> **À retenir** : `NgIf`, `NgFor` et `NgSwitch` sont **dépréciés** depuis la version 20. Migration automatique : `ng generate @angular/core:control-flow`.

## 5.4 Expressions de gabarit

Les expressions sont du TypeScript **simplifié** : pas d'affectation (hors événements), pas de `new`, pas d'opérateurs `++` / `--`, pas d'accès à `window`. Les exemples ci-dessous supposent que la classe du composant expose les signaux `prix`, `utilisateur` et `liste`, ainsi que les propriétés `a` et `b`.

```html
{{ prix() * 1.2 | currency }}
{{ utilisateur()?.adresse?.ville ?? "Inconnue" }}
{{ liste().length > 0 ? "Oui" : "Non" }}
<button (click)="a = 1; b = 2">Plusieurs instructions</button>
```

## 5.5 Variables de référence de gabarit

```typescript
import { Component } from "@angular/core";
import { Compteur } from "./compteur";

@Component({
    selector: "app-reference",
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

## 5.6 Gabarits réutilisables : `ng-template`, `ng-container`

```typescript
import { Component, signal } from "@angular/core";
import { NgTemplateOutlet } from "@angular/common";

@Component({
    selector: "app-gabarits",
    imports: [NgTemplateOutlet],
    template: `
        <ng-template #chargement><p>Chargement…</p></ng-template>

        @if (donnees(); as d) {
            <ul>@for (element of d; track element) { <li>{{ element }}</li> }</ul>
        } @else {
            <ng-container *ngTemplateOutlet="chargement" />
        }

        <ng-container>               <!-- regroupe sans ajouter d'élément au DOM -->
            @for (x of liste(); track x) { <span>{{ x }}</span> }
        </ng-container>
    `,
})
export class Gabarits {
    protected readonly donnees = signal<string[] | null>(null);
    protected readonly liste = signal(["a", "b", "c"]);
}
```

## 5.7 Liaison bidirectionnelle avec les signaux

```typescript
import { Component, signal } from "@angular/core";
import { FormsModule } from "@angular/forms";

@Component({
    selector: "app-champ",
    imports: [FormsModule],
    template: `<input [(ngModel)]="nom" /> <p>{{ nom() }}</p>`,
})
export class Champ {
    nom = signal("");              // [(ngModel)] fonctionne directement avec un signal inscriptible
}
```

---

# 6. Directives et tubes (*pipes*)

## 6.1 Types de directives

| Type | Rôle | Exemples |
| --- | --- | --- |
| **Composant** | Directive **avec gabarit** | `<app-carte />` |
| **Structurelle** | Modifie la **structure** du DOM | `@if`, `@for` (anciennement `*ngIf`, `*ngFor`) |
| **D'attribut** | Modifie l'**apparence ou le comportement** | `ngClass`, `ngStyle`, directives personnalisées |

## 6.2 Directives d'attribut intégrées *(à jour)*

```typescript
import { Component, signal } from "@angular/core";
import { NgClass, NgStyle } from "@angular/common";

@Component({
    selector: "app-attributs",
    imports: [NgClass, NgStyle],
    template: `
        <!-- Préférez les liaisons natives de classes et de styles -->
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
    protected readonly couleur = signal("lightblue");
    protected readonly largeur = signal(200);
}
```

> **À retenir** : depuis les versions récentes, `[class]` et `[style]` acceptent objets et tableaux : `NgClass` et `NgStyle` ne sont plus nécessaires.

## 6.3 Créer une directive d'attribut

```bash
ng generate directive surbrillance
```

```typescript
// src/app/surbrillance.ts
import { Directive, input, ElementRef, inject } from "@angular/core";

@Directive({
    selector: "[appSurbrillance]",
    host: {
        "(mouseenter)": "appliquer(couleur())",
        "(mouseleave)": "appliquer('')",
    },
})
export class Surbrillance {
    couleur = input("yellow", { alias: "appSurbrillance" });
    private readonly element = inject(ElementRef<HTMLElement>);

    appliquer(c: string): void { this.element.nativeElement.style.backgroundColor = c; }
}
```

```typescript
import { Component } from "@angular/core";
import { Surbrillance } from "./surbrillance";

@Component({
    selector: "app-demo-surbrillance",
    imports: [Surbrillance],
    template: `<p appSurbrillance="lightblue">Survolez-moi</p>`,
})
export class DemoSurbrillance {}
```

### Directives composées : `hostDirectives`

```typescript
import { Component } from "@angular/core";
import { Surbrillance } from "./surbrillance";

@Component({
    selector: "app-bouton-info",
    hostDirectives: [{ directive: Surbrillance, inputs: ["appSurbrillance: couleur"] }],
    template: `<ng-content />`,
})
export class BoutonInfo {}
```

## 6.4 Directives structurelles personnalisées *(héritage avancé)*

Les directives structurelles personnalisées (`*appSiRole`) existent toujours (`TemplateRef` + `ViewContainerRef`), mais le **flux de contrôle intégré** couvre la grande majorité des besoins.

## 6.5 Tubes (*pipes*) intégrés

Un **tube** transforme une valeur **à l'affichage** : `{{ valeur | tube:argument }}`. Importez-le dans `imports` (ex. `DatePipe`, `CurrencyPipe`) ou importez `CommonModule`.

| Tube | Exemple | Résultat |
| --- | --- | --- |
| `date` | `{{ d \| date: "dd/MM/yyyy" }}` | `11/10/2026` |
| `currency` | `{{ 1234.5 \| currency: "EUR" }}` | `€1,234.50` (selon la locale) |
| `number` | `{{ 3.14159 \| number: "1.2-2" }}` | `3.14` |
| `percent` | `{{ 0.256 \| percent }}` | `26%` |
| `uppercase`, `lowercase`, `titlecase` | `{{ "angular" \| titlecase }}` | `Angular` |
| `slice` | `{{ liste \| slice: 0:3 }}` | 3 premiers éléments |
| `json` | `{{ objet \| json }}` | Débogage |
| `keyvalue` | `@for (e of obj \| keyvalue; track e.key)` | Itérer un objet |
| `async` | `{{ flux$ \| async }}` | S'abonne à un **Observable** / Promise |
| `i18nPlural`, `i18nSelect` | | Pluriels et sélection (i18n) |

```typescript
import { Component } from "@angular/core";
import { DatePipe, CurrencyPipe } from "@angular/common";

@Component({
    selector: "app-facture",
    imports: [DatePipe, CurrencyPipe],
    template: `<p>{{ date | date: "longDate" }} — {{ montant | currency: "EUR" }}</p>`,
})
export class Facture { date = new Date(); montant = 1234.5; }
```

Chaînage et arguments : `{{ valeur | uppercase | slice: 0:5 }}`.

## 6.6 Créer un tube

```typescript
// src/app/tronquer.ts
import { Pipe, PipeTransform } from "@angular/core";

@Pipe({ name: "tronquer" })            // pur par défaut
export class Tronquer implements PipeTransform {
    transform(texte: string, longueur = 20, suffixe = "…"): string {
        return texte.length > longueur ? texte.slice(0, longueur) + suffixe : texte;
    }
}
```

```typescript
import { Component } from "@angular/core";
import { Tronquer } from "./tronquer";

@Component({
    selector: "app-resume",
    imports: [Tronquer],
    template: `<p>{{ description | tronquer: 50 }}</p>`,
})
export class Resume {
    protected readonly description = "Angular est un framework open source développé par Google pour créer des applications web.";
}
```

## 6.7 Tubes purs et impurs

| | **Pur** (défaut) | **Impur** (`pure: false`) |
| --- | --- | --- |
| Exécuté | Seulement si l'**entrée change** (référence) | À **chaque** détection de changements |
| Performance | Excellente | Coûteux |
| Usage | Presque toujours | Rare (ex. `async`) |

> **Astuce** : avec les signaux, un **`computed()`** est souvent plus simple qu'un tube pour dériver une valeur.

---

# 7. Services et injection de dépendances

## 7.1 Qu'est-ce qu'un service ?

Un **service** est une classe qui regroupe de la **logique réutilisable** (accès aux données, état partagé, journalisation). Angular l'**injecte** là où elle est nécessaire : c'est l'**injection de dépendances** (DI).

| Avantage | Détail |
| --- | --- |
| Réutilisation | Un même service pour plusieurs composants |
| Séparation | Composants = affichage ; services = logique |
| Testabilité | Remplacer un service par une **doublure** en test |
| Singletons | Une seule instance partagée (par injecteur) |

## 7.2 Créer et injecter un service

```bash
ng generate service tache
```

```typescript
// src/app/tache.ts
import { Injectable, signal, computed } from "@angular/core";

export interface Tache { id: number; titre: string; faite: boolean }

@Injectable({ providedIn: "root" })            // singleton à l'échelle de l'application, « tree-shakable »
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

> **À retenir** : la v22 introduit un décorateur raccourci **`@Service()`** pour les services à portée racine (équivalent de `@Injectable({ providedIn: 'root' })`) : vérifiez-le sur [angular.dev](https://angular.dev).

### Injection avec `inject()` *(à jour)*

```typescript
// src/app/taches.ts
import { Component, inject } from "@angular/core";
import { TacheService } from "./tache";

@Component({
    selector: "app-taches",
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

> **À retenir** : `inject()` fonctionne dans un **contexte d'injection** (constructeur, initialisation de champ, fonction `provide`/garde/intercepteur). Il facilite l'héritage et la composition.

## 7.3 Portées des fournisseurs

| Où fournir | Portée / durée de vie |
| --- | --- |
| `@Injectable({ providedIn: "root" })` | **Toute l'application**, instance unique (par défaut) |
| `providers` de `app.config.ts` | Toute l'application (utile pour la configuration) |
| `providers` d'une **route** | Toutes les routes enfants (injecteur d'environnement) |
| `providers` d'un **composant** | **Une instance par composant** (et ses enfants) |
| `viewProviders` | Vue du composant seulement (pas le contenu projeté) |

```typescript
import { Component, Injectable, inject, signal } from "@angular/core";

@Injectable()
export class BrouillonService {
    readonly texte = signal("");
}

@Component({
    selector: "app-formulaire",
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

## 7.4 Jetons d'injection et configuration

```typescript
// src/app/config-app.ts
import { InjectionToken } from "@angular/core";

export interface ConfigApp { urlApi: string; delaiMs: number }
export const CONFIG_APP = new InjectionToken<ConfigApp>("CONFIG_APP", {
    providedIn: "root",
    factory: () => ({ urlApi: "/api", delaiMs: 5000 }),         // valeur par défaut
});
```

Remplacer la valeur par défaut dans la configuration de l'application :

```typescript
// src/app/app.config.ts
import { ApplicationConfig } from "@angular/core";
import { CONFIG_APP } from "./config-app";

export const appConfig: ApplicationConfig = {
    providers: [
        { provide: CONFIG_APP, useValue: { urlApi: "https://api.exemple.com", delaiMs: 8000 } },
    ],
};
```

Lire la valeur dans un service :

```typescript
// src/app/api.ts
import { Injectable, inject } from "@angular/core";
import { CONFIG_APP } from "./config-app";

@Injectable({ providedIn: "root" })
export class Api {
    private readonly config = inject(CONFIG_APP);
    afficherUrl(): void { console.log(this.config.urlApi); }
}
```

### Formes de fournisseurs

| Forme | Usage |
| --- | --- |
| `{ provide: A, useClass: B }` | Remplacer une classe par une autre (ex. `ServiceReel` → `ServiceFactice`) |
| `{ provide: T, useValue: valeur }` | Fournir une constante |
| `{ provide: T, useFactory: () => … }` | Construire avec une fonction (peut utiliser `inject()`) |
| `{ provide: A, useExisting: B }` | Alias |
| `multi: true` | Plusieurs valeurs pour un même jeton |

## 7.5 Modificateurs d'injection

```typescript
import { Component, Injectable, inject } from "@angular/core";

@Injectable({ providedIn: "root" })
export class Journal {
    ecrire(message: string): void { console.log(message); }
}

@Injectable()
export class Theme { nom = "clair"; }

@Component({
    selector: "app-enfant",
    providers: [Theme],
    template: `<p>Voir la console</p>`,
})
export class Enfant {
    private readonly journal = inject(Journal, { optional: true });                // null si absent
    private readonly local = inject(Theme, { self: true });                         // uniquement l'injecteur local
    private readonly parent = inject(Theme, { skipSelf: true, optional: true });    // injecteur parent (null ici : aucun parent ne le fournit)

    constructor() {
        this.journal?.ecrire(`Thème local : ${this.local.nom}`);
        console.log(this.parent);                                                   // null
    }
}
```

## 7.6 Hiérarchie d'injecteurs

```text
Injecteur de plateforme
   └── Injecteur d'environnement (racine : app.config.ts, providedIn: 'root')
          └── Injecteurs de routes (providers de route, chargement paresseux)
                 └── Injecteurs d'éléments (composants, directives)
```

Angular remonte la hiérarchie jusqu'à trouver un fournisseur ; sinon : erreur `NullInjectorError` (ou `null` avec `optional`).

## 7.7 Fonctions d'initialisation

```typescript
import { ApplicationConfig, Injectable, inject, provideAppInitializer } from "@angular/core";

@Injectable({ providedIn: "root" })
export class ConfigService {
    async charger(): Promise<void> {
        console.log("Configuration chargée");
    }
}

export const appConfig: ApplicationConfig = {
    providers: [
        provideAppInitializer(() => inject(ConfigService).charger()),     // exécutée avant le démarrage (peut renvoyer une promesse)
    ],
};
```

## 7.8 Bonnes pratiques

- `providedIn: "root"` par défaut ; fournir au niveau d'un composant seulement pour un **état propre à chaque instance**.
- Exposer l'état via des **signaux en lecture seule** (`asReadonly()`).
- Dépendre d'**abstractions** (jetons, classes abstraites) pour faciliter les tests.
- Éviter les dépendances circulaires.

---

# 8. Signaux et réactivité

*(Section ajoutée : les signaux sont le socle de l'Angular moderne.)*

## 8.1 Qu'est-ce qu'un signal ?

Un **signal** est un **conteneur de valeur réactif** : Angular sait **précisément** quels gabarits et calculs en dépendent et ne met à jour **que ceux-là**. C'est ce qui permet le mode **zoneless** et des performances prévisibles.

```typescript
import { Component, signal, computed, effect } from "@angular/core";

@Component({
    selector: "app-signaux",
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

> **À retenir** : les API de signaux de base (`signal`, `computed`, `effect`, `linkedSignal`, `input`, `model`, `viewChild`) sont **stables** depuis la v20 ; `resource`, `rxResource` et `httpResource` le sont depuis la **v22**.

## 8.2 Signaux d'objets et de tableaux

Les signaux détectent le changement par **référence** : mettez à jour de façon **immuable**.

```typescript
import { signal } from "@angular/core";

const utilisateur = signal({ nom: "Alice", age: 30 });
utilisateur.update((u) => ({ ...u, age: u.age + 1 }));     // correct : nouvel objet
console.log(utilisateur());                                  // { nom: "Alice", age: 31 }

const liste = signal<string[]>([]);
liste.update((l) => [...l, "nouveau"]);                    // correct : nouveau tableau
// liste().push("x");                                       // incorrect : aucune notification
console.log(liste());                                        // ["nouveau"]
```

## 8.3 `computed` : dérivation

```typescript
import { Component, computed, signal } from "@angular/core";

@Component({
    selector: "app-panier",
    template: `<p>Total : {{ total() }}</p>`,
})
export class Panier {
    protected readonly prix = signal(100);
    protected readonly quantite = signal(2);
    protected readonly total = computed(() => this.prix() * this.quantite());       // se met à jour automatiquement
}
```

- **Paresseux** : calculé seulement quand on le lit.
- **Mémoïsé** : recalculé seulement si une dépendance change.
- **Pas d'effets de bord** ni d'écriture de signaux à l'intérieur.

## 8.4 `effect` : effets de bord

```typescript
import { Component, effect, signal } from "@angular/core";

@Component({
    selector: "app-preferences",
    template: `<button (click)="basculer()">Thème : {{ theme() }}</button>`,
})
export class Preferences {
    protected readonly theme = signal<"clair" | "sombre">("clair");

    constructor() {
        // Les effets s'exécutent aussi côté serveur : voir la section 22.4 pour un code compatible SSR
        effect(() => {
            document.documentElement.dataset["theme"] = this.theme();       // synchroniser avec le DOM
            localStorage.setItem("theme", this.theme());
        });
    }

    protected basculer(): void {
        this.theme.update((t) => (t === "clair" ? "sombre" : "clair"));
    }
}
```

> **Attention** : **n'utilisez pas `effect` pour propager un état vers un autre signal** (préférez `computed` ou `linkedSignal`). Les effets sont réservés aux **synchronisations avec l'extérieur** (stockage, journaux, bibliothèques non Angular, DOM).
> Pour des effets liés au **rendu**, utilisez `afterRenderEffect()` / `afterNextRender()`.

## 8.5 `linkedSignal` : état dérivé modifiable

```typescript
import { linkedSignal, signal } from "@angular/core";

const options = signal(["S", "M", "L"]);
const selection = linkedSignal(() => options()[0]);        // se réinitialise quand `options` change
selection.set("L");                                          // mais reste modifiable
console.log(selection());                                    // "L"

options.set(["XS", "S"]);
console.log(selection());                                    // "XS" : réinitialisé
```

Version avancée avec mémoire de l'ancienne valeur :

```typescript
import { linkedSignal, signal } from "@angular/core";

const options = signal(["S", "M", "L"]);
const selection = linkedSignal<string[], string>({
    source: options,
    computation: (nouvelles, precedent) => (precedent && nouvelles.includes(precedent.value) ? precedent.value : nouvelles[0]),
});

selection.set("M");
options.set(["M", "L", "XL"]);
console.log(selection());                                    // "M" : conservé, car toujours disponible
options.set(["XS", "S"]);
console.log(selection());                                    // "XS" : l'ancienne sélection a disparu
```

## 8.6 `resource` : données asynchrones *(stable en v22)*

Une **resource** relie un **signal de paramètres** à un **chargeur asynchrone** et expose `value()`, `isLoading()`, `error()`, `status()`.

```typescript
import { Component, resource, signal } from "@angular/core";

@Component({
    selector: "app-utilisateur",
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

> **Note** : dans les versions 19–20, l'option s'appelait **`request`** ; elle est devenue **`params`**.

### `httpResource` : la version « HttpClient »

```typescript
import { Component, signal } from "@angular/core";
import { httpResource } from "@angular/common/http";

interface Utilisateur { id: number; nom: string; }

@Component({
    selector: "app-liste-utilisateurs",
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
    // utilisateurs.value(), .isLoading(), .error(), .hasValue(), .reload()
}
```

### `rxResource` : à partir d'un Observable

```typescript
import { Component, Injectable, inject, signal } from "@angular/core";
import { rxResource } from "@angular/core/rxjs-interop";
import { Observable, of, delay } from "rxjs";

@Injectable({ providedIn: "root" })
export class CatalogueService {
    lister(categorie: string): Observable<string[]> {
        return of([`${categorie} 1`, `${categorie} 2`]).pipe(delay(300));
    }
}

@Component({
    selector: "app-produits-categorie",
    template: `
        <button (click)="categorie.set('jeux')">Jeux</button>
        @if (produits.isLoading()) { <p>Chargement…</p> }
        @for (p of produits.value() ?? []; track p) { <p>{{ p }}</p> }
    `,
})
export class ProduitsCategorie {
    private readonly service = inject(CatalogueService);
    protected readonly categorie = signal("livres");
    protected readonly produits = rxResource({
        params: () => this.categorie(),
        stream: ({ params }) => this.service.lister(params),
    });
}
```

> **Astuce** : `resource` est conçu pour les **lectures** (chargement de données) ; les **écritures** (POST, PUT, DELETE) restent des appels `HttpClient` explicites.

## 8.7 Interopérabilité RxJS ⇄ signaux

```typescript
import { Component, inject, signal } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { toSignal, toObservable } from "@angular/core/rxjs-interop";
import { debounceTime, switchMap } from "rxjs";

interface Utilisateur { id: number; nom: string; }

@Component({
    selector: "app-interop",
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
    protected readonly termeRecherche = signal("");

    // Observable → signal (abonnement et désabonnement automatiques)
    protected readonly utilisateurs = toSignal(this.http.get<Utilisateur[]>("/api/users"), { initialValue: [] });

    // Signal → Observable (pour appliquer des opérateurs RxJS), puis retour en signal pour le gabarit
    private readonly resultats$ = toObservable(this.termeRecherche).pipe(
        debounceTime(300),
        switchMap((t) => this.http.get<string[]>(`/api/recherche?q=${t}`)),
    );
    protected readonly resultats = toSignal(this.resultats$, { initialValue: [] as string[] });
}
```

## 8.8 Signaux ou RxJS ?

| | **Signaux** | **RxJS** |
| --- | --- | --- |
| Nature | **État** (valeur courante) | **Flux d'événements** dans le temps |
| Usage idéal | État de composant / de service, valeurs dérivées, gabarits | Requêtes annulables, anti-rebond, WebSockets, combinaisons complexes |
| Syntaxe | Simple, synchrone | Opérateurs puissants, plus de concepts |
| Dans les gabarits | `valeur()` | Tube `async` ou `toSignal` |

> **Règle** : **signaux pour l'état, RxJS pour les flux** ; `toSignal` / `toObservable` pour passer de l'un à l'autre.

## 8.9 Formes futures et conseils

- Pas de `ChangeDetectorRef.detectChanges()` : un signal modifié suffit.
- Exposez l'état sous forme de **signaux en lecture seule** ; les opérations qui le modifient sont des **méthodes**.
- Gardez les `effect` **rares**.

---

# 9. Routage et navigation

## 9.1 Principe

Le **routeur** associe une **URL** à un **composant** affiché dans une balise `<router-outlet />`, sans recharger la page.

## 9.2 Configurer les routes

```typescript
// app.routes.ts
import { Routes } from "@angular/router";
import { Accueil } from "./accueil/accueil";
import { authGuard } from "./auth/gardes";            // défini à la section 9.6

export const routes: Routes = [
    { path: "", component: Accueil, title: "Accueil" },
    { path: "produits", loadComponent: () => import("./produits/liste").then((m) => m.Liste), title: "Produits" },
    { path: "produits/:id", loadComponent: () => import("./produits/detail").then((m) => m.Detail) },
    { path: "admin", loadChildren: () => import("./admin/admin.routes").then((m) => m.ADMIN_ROUTES), canActivate: [authGuard] },
    { path: "ancienne-page", redirectTo: "produits", pathMatch: "full" },
    { path: "**", loadComponent: () => import("./introuvable/introuvable").then((m) => m.Introuvable) },     // joker : 404
];
```

Les composants `Accueil`, `Liste`, `Detail`, `Introuvable` et le fichier `admin/admin.routes.ts` (qui exporte `ADMIN_ROUTES`) sont supposés exister dans le projet.

```typescript
// src/app/app.config.ts
import { ApplicationConfig } from "@angular/core";
import { provideRouter, withComponentInputBinding, withViewTransitions, withPreloading, PreloadAllModules } from "@angular/router";
import { routes } from "./app.routes";

export const appConfig: ApplicationConfig = {
    providers: [
        provideRouter(routes, withComponentInputBinding(), withViewTransitions(), withPreloading(PreloadAllModules)),
    ],
};
```

```typescript
// src/app/app.ts
import { Component } from "@angular/core";
import { RouterOutlet, RouterLink, RouterLinkActive } from "@angular/router";

@Component({
    selector: "app-root",
    imports: [RouterOutlet, RouterLink, RouterLinkActive],
    template: `
        <nav>
            <a routerLink="/" routerLinkActive="actif" [routerLinkActiveOptions]="{ exact: true }">Accueil</a>
            <a [routerLink]="['/produits', 42]" [queryParams]="{ tri: 'prix' }">Produit 42</a>
        </nav>
        <router-outlet />
    `,
})
export class App {}
```



## 9.3 Paramètres de route *(à jour)*

Avec **`withComponentInputBinding()`**, les paramètres de chemin, de requête et les données de route sont **liés directement à des `input()`** :

```typescript
import { Component, input } from "@angular/core";

@Component({ selector: "app-detail", template: `<h1>Produit {{ id() }} — tri : {{ tri() }}</h1>` })
export class Detail {
    id = input.required<string>();            // /produits/:id
    tri = input<string>();                    // ?tri=prix
}
```

Forme classique (toujours valide) :

```typescript
import { Component, inject } from "@angular/core";
import { ActivatedRoute } from "@angular/router";
import { toSignal } from "@angular/core/rxjs-interop";
import { map } from "rxjs";

@Component({
    selector: "app-detail-classique",
    template: `<h1>Produit {{ id() }}</h1>`,
})
export class DetailClassique {
    private readonly route = inject(ActivatedRoute);
    private readonly id$ = this.route.paramMap.pipe(map((p) => p.get("id")));
    protected readonly id = toSignal(this.id$);
}
```

## 9.4 Navigation par programme

```typescript
import { Component, inject } from "@angular/core";
import { ActivatedRoute, Router } from "@angular/router";

@Component({
    selector: "app-navigation",
    template: `
        <button (click)="aller(42)">Produit 42</button>
        <button (click)="connexion()">Connexion</button>
        <button (click)="remonter()">Retour</button>
    `,
})
export class Navigation {
    private readonly router = inject(Router);
    private readonly route = inject(ActivatedRoute);

    protected aller(id: number): void {
        this.router.navigate(["/produits", id], { queryParams: { tri: "prix" } });
    }
    protected connexion(): void {
        this.router.navigateByUrl("/connexion");
    }
    protected remonter(): void {
        this.router.navigate(["../"], { relativeTo: this.route });       // route relative
    }
}
```

## 9.5 Routes imbriquées (enfants)

```typescript
// src/app/app.routes.ts (extrait)
import { Routes } from "@angular/router";
import { CompteLayout } from "./compte/compte-layout";
import { Profil } from "./compte/profil";
import { Securite } from "./compte/securite";

export const routes: Routes = [
    {
        path: "compte",
        component: CompteLayout,                       // contient <router-outlet />
        children: [
            { path: "", redirectTo: "profil", pathMatch: "full" },
            { path: "profil", component: Profil },
            { path: "securite", component: Securite },
        ],
    },
];
```

## 9.6 Gardes fonctionnelles *(à jour)*

Les gardes sont des **fonctions** (les anciennes gardes sous forme de classes `implements CanActivate` sont **dépréciées**).

| Garde | Moment |
| --- | --- |
| `canActivate` | Avant d'**activer** une route |
| `canActivateChild` | Avant d'activer une route enfant |
| `canMatch` | Avant de **faire correspondre** la route (empêche aussi le chargement du code) |
| `canDeactivate` | Avant de **quitter** (ex. formulaire non enregistré) |
| `resolve` | **Précharge des données** avant l'activation |

```typescript
// src/app/auth/gardes.ts
import { inject } from "@angular/core";
import { CanActivateFn, CanDeactivateFn, Router } from "@angular/router";
import { AuthService } from "./auth";                   // défini à la section 27.3

export const authGuard: CanActivateFn = (route, state) => {
    const auth = inject(AuthService);
    const router = inject(Router);
    return auth.estConnecte() ? true : router.createUrlTree(["/connexion"], { queryParams: { retour: state.url } });
};

export const roleGuard = (role: string): CanActivateFn => () =>
    inject(AuthService).aLeRole(role) || inject(Router).createUrlTree(["/interdit"]);

export const quitterGuard: CanDeactivateFn<{ aDesModifications: () => boolean }> = (composant) =>
    !composant.aDesModifications() || confirm("Quitter sans enregistrer ?");
```

Utilisation dans les routes :

```typescript
// src/app/app.routes.ts (extrait)
import { Routes } from "@angular/router";
import { authGuard, roleGuard, quitterGuard } from "./auth/gardes";
import { Edition } from "./edition/edition";

export const routes: Routes = [
    {
        path: "admin",
        canActivate: [authGuard, roleGuard("admin")],
        loadChildren: () => import("./admin/admin.routes").then((m) => m.ADMIN_ROUTES),
    },
    { path: "edition", component: Edition, canDeactivate: [quitterGuard] },
];
```

Le composant protégé par `quitterGuard` doit exposer `aDesModifications()` :

```typescript
// src/app/edition/edition.ts
import { Component, signal } from "@angular/core";

@Component({
    selector: "app-edition",
    template: `<textarea (input)="modifie.set(true)"></textarea>`,
})
export class Edition {
    protected readonly modifie = signal(false);
    aDesModifications(): boolean { return this.modifie(); }
}
```

> **Attention** : **une garde ne remplace pas la sécurité côté serveur** : elle améliore l'expérience, mais le serveur doit refuser les accès non autorisés (voir sections 26 et 27).

## 9.7 Résolveurs : données avant la navigation

```typescript
// src/app/produits/produit.ts
import { Injectable } from "@angular/core";
import { Observable, of } from "rxjs";

export interface Produit { id: string; nom: string; }

@Injectable({ providedIn: "root" })
export class ProduitService {
    trouver(id: string): Observable<Produit> {
        return of({ id, nom: `Produit ${id}` });
    }
}
```

```typescript
// src/app/produits/produit.resolver.ts
import { inject } from "@angular/core";
import { ResolveFn, Routes } from "@angular/router";
import { Produit, ProduitService } from "./produit";
import { DetailProduit } from "./detail-produit";

export const produitResolver: ResolveFn<Produit> = (route) => inject(ProduitService).trouver(route.paramMap.get("id")!);

export const routes: Routes = [
    { path: "produits/:id", component: DetailProduit, resolve: { produit: produitResolver } },
];
```

```typescript
// src/app/produits/detail-produit.ts
import { Component, input } from "@angular/core";
import { Produit } from "./produit";

@Component({ selector: "app-detail-produit", template: `<h1>{{ produit().nom }}</h1>` })
export class DetailProduit {
    produit = input.required<Produit>();       // reçoit les données résolues (avec withComponentInputBinding)
}
```

## 9.8 Chargement paresseux et préchargement

```typescript
// src/app/app.routes.ts (extrait)
import { Routes } from "@angular/router";

export const routes: Routes = [
    { path: "admin", loadChildren: () => import("./admin/admin.routes").then((m) => m.ADMIN_ROUTES) },
];
```

```typescript
// src/app/admin/admin.routes.ts
import { Routes } from "@angular/router";
import { AdminAccueil } from "./admin-accueil";

export const ADMIN_ROUTES: Routes = [
    { path: "", component: AdminAccueil },
];
```

| Stratégie de préchargement | Effet |
| --- | --- |
| `NoPreloading` (défaut) | Rien n'est préchargé |
| `PreloadAllModules` | Précharge tout en arrière-plan |
| **Personnalisée** (`PreloadingStrategy`) | Précharge selon une règle (`data: { preload: true }`) |

Détails à la [section 19](#19-chargement-paresseux-et-vues-différées).

## 9.9 Autres fonctionnalités

| Fonctionnalité | Usage |
| --- | --- |
| `title` / `TitleStrategy` | Titre de page par route |
| `withViewTransitions()` | Transitions animées entre pages (View Transitions API) |
| `withInMemoryScrolling({ scrollPositionRestoration: "enabled" })` | Restaurer le défilement |
| Routes **nommées** (`outlet`), **auxiliaires** | Plusieurs zones de routage |
| `withHashLocation()` | URL avec `#` (hébergements statiques simples) |
| `Router.events` | Suivre la navigation (`NavigationStart`, `NavigationEnd`…) |

## 9.10 Exemple complet : garde + chargement paresseux

```typescript
// src/app/app.routes.ts
import { Routes } from "@angular/router";
import { authGuard } from "./auth/gardes";
import { Accueil } from "./accueil/accueil";
import { Connexion } from "./connexion/connexion";

export const routes: Routes = [
    { path: "", component: Accueil },
    { path: "connexion", component: Connexion },
    {
        path: "tableau-de-bord",
        canActivate: [authGuard],
        loadChildren: () => import("./tableau/tableau.routes").then((m) => m.TABLEAU_ROUTES),
    },
];
```

---

# 10. Formulaires

## 10.1 Les trois approches *(à jour)*

| Approche | Principe | Quand l'utiliser |
| --- | --- | --- |
| **Basée sur le gabarit** (*template-driven*) | `ngModel` dans le HTML | Formulaires **simples** |
| **Réactive** (*reactive forms*) | Modèle construit en **TypeScript** (`FormGroup`, `FormControl`) | Formulaires **complexes**, dynamiques, testables |
| **Signal Forms** *(stables en v22)* | Modèle = **signal**, validation par schéma | **Nouveau code** (approche recommandée à terme) |

## 10.2 Formulaires basés sur le gabarit

```typescript
import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";

@Component({
    selector: "app-contact",
    imports: [FormsModule],
    template: `
        <form #f="ngForm" (ngSubmit)="envoyer(f.value)">
            <input name="nom" [(ngModel)]="modele.nom" required minlength="2" #nom="ngModel" />
            @if (nom.invalid && nom.touched) { <small>Nom invalide (2 caractères minimum)</small> }

            <input name="email" type="email" [(ngModel)]="modele.email" required email />
            <button [disabled]="f.invalid">Envoyer</button>
        </form>
    `,
})
export class Contact {
    modele = { nom: "", email: "" };
    envoyer(valeurs: unknown): void { console.log(valeurs); }
}
```

## 10.3 Formulaires réactifs (typés)

```typescript
import { Component, inject } from "@angular/core";
import { ReactiveFormsModule, NonNullableFormBuilder, Validators } from "@angular/forms";

@Component({
    selector: "app-inscription",
    imports: [ReactiveFormsModule],
    template: `
        <form [formGroup]="formulaire" (ngSubmit)="envoyer()">
            <input formControlName="nom" />
            @if (nom.invalid && (nom.touched || nom.dirty)) {
                @if (nom.errors?.["required"]) { <small>Le nom est obligatoire.</small> }
                @if (nom.errors?.["minlength"]) { <small>2 caractères minimum.</small> }
            }

            <input formControlName="email" type="email" />
            <input formControlName="motDePasse" type="password" />

            <div formGroupName="adresse">
                <input formControlName="ville" placeholder="Ville" />
            </div>

            <button type="submit" [disabled]="formulaire.invalid">S'inscrire</button>
        </form>
    `,
})
export class Inscription {
    private readonly fb = inject(NonNullableFormBuilder);          // contrôles non nullables par défaut

    formulaire = this.fb.group({
        nom: ["", [Validators.required, Validators.minLength(2)]],
        email: ["", [Validators.required, Validators.email]],
        motDePasse: ["", [Validators.required, Validators.minLength(8)]],
        adresse: this.fb.group({ ville: [""] }),
    });

    get nom() { return this.formulaire.controls.nom; }              // entièrement typé

    envoyer() {
        if (this.formulaire.invalid) { this.formulaire.markAllAsTouched(); return; }
        const valeurs = this.formulaire.getRawValue();               // type : { nom: string; email: string; … }
        console.log(valeurs);
    }
}
```

### Opérations utiles

```typescript
import { Component, inject } from "@angular/core";
import { takeUntilDestroyed } from "@angular/core/rxjs-interop";
import { ReactiveFormsModule, NonNullableFormBuilder, Validators } from "@angular/forms";
import { debounceTime } from "rxjs";

@Component({
    selector: "app-operations-formulaire",
    imports: [ReactiveFormsModule],
    template: `
        <form [formGroup]="formulaire">
            <input formControlName="nom" />
            <input formControlName="ville" />
        </form>
        <button type="button" (click)="exemples()">Exécuter les exemples</button>
    `,
})
export class OperationsFormulaire {
    private readonly fb = inject(NonNullableFormBuilder);
    protected readonly formulaire = this.fb.group({
        nom: ["", Validators.required],
        ville: [""],
    });

    constructor() {
        this.formulaire.valueChanges.pipe(debounceTime(300), takeUntilDestroyed()).subscribe((valeurs) => console.log(valeurs));
    }

    protected exemples(): void {
        this.formulaire.patchValue({ nom: "Alice" });                    // mise à jour partielle
        this.formulaire.setValue({ nom: "Alice", ville: "Paris" });      // mise à jour complète
        this.formulaire.reset();

        const nom = this.formulaire.controls.nom;
        nom.statusChanges.subscribe((statut) => console.log(statut));
        nom.disable();
        nom.enable();
        nom.setErrors({ personnalise: true });
    }
}
```

États : `valid`, `invalid`, `pending`, `touched`, `dirty`, `pristine`.

## 10.4 Validation personnalisée

```typescript
// src/app/validateurs.ts
import { AbstractControl, ValidationErrors, ValidatorFn, AsyncValidatorFn } from "@angular/forms";
import { map } from "rxjs";
import { UtilisateurService } from "./utilisateur";           // défini à la section 11.2

// Validateur synchrone (fabrique)
export const interdire = (mot: string): ValidatorFn => (c: AbstractControl): ValidationErrors | null =>
    String(c.value).toLowerCase().includes(mot) ? { interdit: { mot } } : null;

// Validateur de groupe : confirmation de mot de passe
export const motsDePasseIdentiques: ValidatorFn = (g) =>
    g.get("motDePasse")?.value === g.get("confirmation")?.value ? null : { nonIdentiques: true };

// Validateur asynchrone (ex. e-mail déjà utilisé)
export const emailLibre = (service: UtilisateurService): AsyncValidatorFn => (c) =>
    service.existe(c.value).pipe(map((existe) => (existe ? { emailPris: true } : null)));
```

Utilisation dans un formulaire :

```typescript
import { Component, inject } from "@angular/core";
import { ReactiveFormsModule, NonNullableFormBuilder, Validators } from "@angular/forms";
import { UtilisateurService } from "./utilisateur";
import { interdire, motsDePasseIdentiques, emailLibre } from "./validateurs";

@Component({
    selector: "app-inscription-confirmation",
    imports: [ReactiveFormsModule],
    template: `
        <form [formGroup]="formulaire">
            <input formControlName="email" type="email" />
            @if (formulaire.controls.email.errors?.["interdit"]) { <small>Mot interdit.</small> }
            @if (formulaire.controls.email.errors?.["emailPris"]) { <small>E-mail déjà utilisé.</small> }

            <input formControlName="motDePasse" type="password" />
            <input formControlName="confirmation" type="password" />
            @if (formulaire.errors?.["nonIdentiques"]) { <small>Les mots de passe diffèrent.</small> }
        </form>
    `,
})
export class InscriptionConfirmation {
    private readonly fb = inject(NonNullableFormBuilder);
    private readonly utilisateurs = inject(UtilisateurService);

    protected readonly formulaire = this.fb.group(
        {
            email: ["", [Validators.required, interdire("test")], [emailLibre(this.utilisateurs)]],
            motDePasse: ["", [Validators.required, Validators.minLength(8)]],
            confirmation: [""],
        },
        { validators: motsDePasseIdentiques },
    );
}
```

## 10.5 Tableaux dynamiques : `FormArray`

```typescript
import { Component, inject } from "@angular/core";
import { ReactiveFormsModule, NonNullableFormBuilder } from "@angular/forms";

@Component({
    selector: "app-competences",
    imports: [ReactiveFormsModule],
    template: `
        <form [formGroup]="formulaire">
            <div formArrayName="competences">
                @for (c of competences.controls; track $index) {
                    <input [formControlName]="$index" /> <button type="button" (click)="supprimer($index)">×</button>
                }
            </div>
            <button type="button" (click)="ajouter()">Ajouter une compétence</button>
        </form>
    `,
})
export class Competences {
    private readonly fb = inject(NonNullableFormBuilder);
    protected readonly formulaire = this.fb.group({ competences: this.fb.array([this.fb.control("")]) });

    protected get competences() { return this.formulaire.controls.competences; }
    protected ajouter(): void { this.competences.push(this.fb.control("")); }
    protected supprimer(i: number): void { this.competences.removeAt(i); }
}
```



## 10.6 Composants de formulaire personnalisés

Pour qu'un composant fonctionne avec `formControlName` / `ngModel`, il implémente **`ControlValueAccessor`** et se déclare via `NG_VALUE_ACCESSOR`.

## 10.7 Signal Forms *(stables en Angular 22)*

Les **Signal Forms** (paquet `@angular/forms/signals`) construisent le formulaire **autour d'un signal** : le modèle est la **source de vérité**, les validateurs sont décrits dans un **schéma**, et l'état du formulaire (`valid`, `touched`, `errors`…) est lui-même fait de signaux.

```typescript
import { Component, signal } from "@angular/core";
import { form, FormField, required, email, minLength } from "@angular/forms/signals";

@Component({
    selector: "app-inscription-signaux",
    imports: [FormField],                                         // directive de liaison [formField]
    template: `
        <form (submit)="envoyer($event)">
            <input [formField]="formulaire.nom" />
            @if (formulaire.nom().touched() && formulaire.nom().invalid()) {
                <small>Nom invalide (2 caractères minimum).</small>
            }

            <input type="email" [formField]="formulaire.email" />
            <button type="submit" [disabled]="formulaire().invalid()">S'inscrire</button>
        </form>
    `,
})
export class InscriptionSignaux {
    protected readonly modele = signal({ nom: "", email: "" });    // source de vérité

    protected readonly formulaire = form(this.modele, (chemin) => {
        required(chemin.nom);
        minLength(chemin.nom, 2);
        required(chemin.email);
        email(chemin.email);
    });

    protected envoyer(evenement: Event): void {
        evenement.preventDefault();
        if (this.formulaire().valid()) {
            console.log(this.modele());
        }
    }
}
```

> **Attention** : l'API a **évolué pendant la phase expérimentale** (versions 21.x) : consultez le guide « Signal Forms » sur [angular.dev](https://angular.dev) pour la syntaxe exacte (directive `FormField`, soumission avec `submit()` ou `FormRoot`) et pour les migrations. Les formulaires réactifs et basés sur le gabarit **continuent d'être pris en charge** et peuvent coexister avec les Signal Forms.

## 10.8 Choisir

| Besoin | Approche |
| --- | --- |
| Petit formulaire (recherche, contact) | Gabarit ou **Signal Forms** |
| Formulaire complexe existant, validation asynchrone avancée | **Réactif** |
| Nouveau projet 100 % signaux | **Signal Forms** |

## 10.9 Bonnes pratiques

- **Valider côté serveur aussi** : la validation côté client n'est qu'une aide.
- Afficher les erreurs **après interaction** (`touched` / `dirty`).
- Désactiver le bouton d'envoi **pendant l'envoi** (éviter les doublons).
- Lier les libellés (`<label for>`) et les messages d'erreur (`aria-describedby`) : **accessibilité**.

---

# Avancé

---

# 11. Client HTTP

## 11.1 Configurer `HttpClient` *(à jour)*

Plus de `HttpClientModule` : on utilise des **fonctions de configuration** dans `app.config.ts`.

```typescript
// src/app/app.config.ts
import { ApplicationConfig } from "@angular/core";
import { provideHttpClient, withFetch, withInterceptors, withXsrfConfiguration } from "@angular/common/http";
import { authInterceptor, erreurInterceptor, journalInterceptor } from "./http/intercepteurs";     // définis à la section 11.4

export const appConfig: ApplicationConfig = {
    providers: [
        provideHttpClient(
            withFetch(),                                    // utilise l'API fetch (recommandé, requis pour SSR efficace)
            withInterceptors([authInterceptor, erreurInterceptor, journalInterceptor]),
            withXsrfConfiguration({ cookieName: "XSRF-TOKEN", headerName: "X-XSRF-TOKEN" }),
        ),
    ],
};
```

> **Note** : les anciens intercepteurs sous forme de **classes** (`HttpInterceptor` + `HTTP_INTERCEPTORS`) nécessitent `withInterceptorsFromDi()` ; préférez les **intercepteurs fonctionnels**.

## 11.2 Un service d'accès aux données typé

```typescript
// src/app/utilisateur.ts
import { Injectable, inject } from "@angular/core";
import { HttpClient, HttpParams } from "@angular/common/http";
import { Observable } from "rxjs";

export interface Utilisateur { id: number; nom: string; email: string }

@Injectable({ providedIn: "root" })
export class UtilisateurService {
    private readonly http = inject(HttpClient);
    private readonly url = "/api/utilisateurs";

    lister(page = 1): Observable<Utilisateur[]> {
        const params = new HttpParams().set("page", page).set("taille", 20);
        return this.http.get<Utilisateur[]>(this.url, { params });
    }
    trouver(id: number): Observable<Utilisateur> { return this.http.get<Utilisateur>(`${this.url}/${id}`); }
    creer(u: Omit<Utilisateur, "id">): Observable<Utilisateur> { return this.http.post<Utilisateur>(this.url, u); }
    modifier(id: number, u: Partial<Utilisateur>): Observable<Utilisateur> { return this.http.patch<Utilisateur>(`${this.url}/${id}`, u); }
    supprimer(id: number): Observable<void> { return this.http.delete<void>(`${this.url}/${id}`); }
    existe(email: string): Observable<boolean> { return this.http.get<boolean>(`${this.url}/existe`, { params: { email } }); }
}
```

| Méthode | Usage |
| --- | --- |
| `get<T>()` | Lire |
| `post<T>()` | Créer |
| `put<T>()` / `patch<T>()` | Remplacer / modifier |
| `delete<T>()` | Supprimer |
| `request()` | Requête personnalisée |
| Options | `params`, `headers`, `observe: "response"`, `responseType: "blob" \| "text"`, `reportProgress`, `withCredentials` |

> **Attention** : un `Observable` HTTP est **froid** : **rien ne part tant qu'on ne s'abonne pas** (`subscribe`, tube `async`, `toSignal`), et chaque abonnement relance la requête.

## 11.3 Utiliser les données

```typescript
import { Component, inject, signal } from "@angular/core";
import { AsyncPipe } from "@angular/common";
import { httpResource } from "@angular/common/http";
import { toSignal } from "@angular/core/rxjs-interop";
import { Utilisateur, UtilisateurService } from "./utilisateur";

@Component({
    selector: "app-utilisateurs",
    imports: [AsyncPipe],
    template: `
        <p>{{ utilisateurs().length }} utilisateur(s) via toSignal</p>
        <p>{{ utilisateursResource.value()?.length ?? 0 }} utilisateur(s) via httpResource</p>
        @if (utilisateurs$ | async; as liste) {
            <p>{{ liste.length }} utilisateur(s) via le tube async</p>
        }
    `,
})
export class Utilisateurs {
    private readonly service = inject(UtilisateurService);
    protected readonly page = signal(1);

    // Avec un signal (simple)
    protected readonly utilisateurs = toSignal(this.service.lister(), { initialValue: [] });

    // Avec httpResource (lecture réactive, sans RxJS)
    protected readonly utilisateursResource = httpResource<Utilisateur[]>(() => `/api/utilisateurs?page=${this.page()}`);

    // Avec le tube async
    protected readonly utilisateurs$ = this.service.lister();
}
```

## 11.4 Intercepteurs fonctionnels

```typescript
// src/app/http/intercepteurs.ts
import { inject } from "@angular/core";
import { Router } from "@angular/router";
import { HttpInterceptorFn, HttpErrorResponse } from "@angular/common/http";
import { catchError, tap, throwError } from "rxjs";
import { AuthService } from "../auth/auth";                  // défini à la section 27.3

export const authInterceptor: HttpInterceptorFn = (req, next) => {
    const jeton = inject(AuthService).jeton();
    const requete = jeton && req.url.startsWith("/api") ? req.clone({ setHeaders: { Authorization: `Bearer ${jeton}` } }) : req;
    return next(requete);
};

export const erreurInterceptor: HttpInterceptorFn = (req, next) => {
    const router = inject(Router);
    return next(req).pipe(
        catchError((erreur: HttpErrorResponse) => {
            if (erreur.status === 401) router.navigateByUrl("/connexion");
            return throwError(() => erreur);
        }),
    );
};

export const journalInterceptor: HttpInterceptorFn = (req, next) => {
    const debut = performance.now();
    return next(req).pipe(tap({ finalize: () => console.log(`${req.method} ${req.url} : ${(performance.now() - debut).toFixed(0)} ms`) }));
};
```

Usages : **jeton d'authentification**, **gestion centralisée des erreurs**, **indicateur de chargement**, **cache**, **journalisation**, ajout d'en-têtes (langue, version d'API).

## 11.5 Gestion des erreurs

```typescript
import { Component, inject } from "@angular/core";
import { toSignal } from "@angular/core/rxjs-interop";
import { HttpErrorResponse } from "@angular/common/http";
import { catchError, of, retry, timer } from "rxjs";
import { Utilisateur, UtilisateurService } from "./utilisateur";

@Component({
    selector: "app-utilisateurs-securises",
    template: `<p>{{ utilisateurs().length }} utilisateur(s)</p>`,
})
export class UtilisateursSecurises {
    private readonly service = inject(UtilisateurService);

    protected readonly utilisateurs = toSignal(
        this.service.lister().pipe(
            retry({ count: 3, delay: (erreur, essai) => timer(500 * 2 ** essai) }),     // nouvelle tentative avec attente exponentielle
            catchError((erreur: HttpErrorResponse) => {
                if (erreur.status === 0) console.error("Réseau indisponible");          // erreur côté client / réseau
                else console.error(`Serveur : ${erreur.status}`, erreur.error);
                return of([] as Utilisateur[]);                                          // valeur de repli
            }),
        ),
        { initialValue: [] as Utilisateur[] },
    );
}
```

## 11.6 Progression, annulation et fichiers

```typescript
import { Component, inject, signal } from "@angular/core";
import { HttpClient, HttpEventType } from "@angular/common/http";

@Component({
    selector: "app-televersement",
    template: `
        <input type="file" (change)="choisir($any($event.target).files[0])" />
        <p>Progression : {{ progression() }} %</p>
    `,
})
export class Televersement {
    private readonly http = inject(HttpClient);
    protected readonly progression = signal(0);

    protected choisir(fichier: File): void {
        const formData = new FormData();
        formData.append("fichier", fichier);

        this.http.post("/api/upload", formData, { reportProgress: true, observe: "events" }).subscribe((evenement) => {
            if (evenement.type === HttpEventType.UploadProgress && evenement.total) {
                this.progression.set(Math.round((100 * evenement.loaded) / evenement.total));
            }
        });
    }
}
```

Annulation : `switchMap` (changement de requête), `takeUntilDestroyed()`, ou `unsubscribe()`.

## 11.7 Fonctionnalités avancées

| Fonctionnalité | Description |
| --- | --- |
| `withFetch()` | Utilise `fetch` au lieu de `XMLHttpRequest` (streaming, SSR) |
| **Cache de transfert SSR** | Réutilise les réponses faites côté serveur pendant l'hydratation (activé avec `provideClientHydration`) |
| `HttpContext` | Passer des métadonnées à un intercepteur |
| `HttpClient` + **`resource`** | Chargement déclaratif piloté par signaux |
| **Proxy de développement** | `ng serve` avec `proxy.conf.json` pour éviter CORS en local |

```jsonc
// proxy.conf.json
{ "/api": { "target": "http://localhost:3000", "secure": false, "changeOrigin": true } }
```

## 11.8 Bonnes pratiques

- **Typer** les réponses (et valider les données externes sensibles).
- Centralisez les URL (jeton d'injection `API_URL`).
- Gérez **chargement / erreur / vide** dans l'interface.
- Ne mettez **aucun secret** dans le code client.
- Utilisez `HttpTestingController` pour tester ([section 16](#16-tests-unitaires)).

---

# 12. Observables et RxJS

## 12.1 Les bases

**RxJS** est la bibliothèque de **programmation réactive** utilisée par Angular. Un **Observable** est un **flux de valeurs dans le temps** auquel on s'**abonne**.

| Concept | Rôle |
| --- | --- |
| **Observable** | Source de valeurs (0, 1 ou N, éventuellement infinie) |
| **Observer** | `{ next, error, complete }` : reçoit les valeurs |
| **Subscription** | L'abonnement (annulable avec `unsubscribe()`) |
| **Opérateurs** | Fonctions qui transforment un flux (`pipe(...)`) |
| **Subject** | Observable **et** observateur : émet à plusieurs abonnés |

```typescript
import { Observable, of, from, interval, fromEvent, take } from "rxjs";

const nombres$ = of(1, 2, 3);                            // convention : suffixe `$`
const lettres$ = from(["a", "b", "c"]);                  // à partir d'un tableau
const tic$ = interval(1000);                             // 0, 1, 2… toutes les secondes
const clics$ = fromEvent(document, "click");

const manuel$ = new Observable<number>((observateur) => {
    observateur.next(1);
    observateur.next(2);
    observateur.complete();
    return () => console.log("Nettoyage");               // fonction de désabonnement
});

const abonnement = manuel$.subscribe({
    next: (v) => console.log(v),
    error: (e) => console.error(e),
    complete: () => console.log("Terminé"),
});
abonnement.unsubscribe();

nombres$.subscribe((n) => console.log(n));               // 1, 2, 3
lettres$.subscribe((l) => console.log(l));               // "a", "b", "c"
tic$.pipe(take(3)).subscribe((n) => console.log(`tic ${n}`));
clics$.pipe(take(1)).subscribe(() => console.log("Premier clic"));
```

## 12.2 Opérateurs essentiels

> **À retenir** : depuis RxJS 7.2, **tous les opérateurs s'importent depuis `"rxjs"`** (et non plus `"rxjs/operators"`).

```typescript
import { of, map, filter, tap, debounceTime, distinctUntilChanged, switchMap, mergeMap, concatMap, exhaustMap,
         catchError, retry, take, takeUntil, startWith, combineLatest, forkJoin, shareReplay, finalize } from "rxjs";

of(1, 2, 3, 4).pipe(
    filter((n) => n % 2 === 0),
    map((n) => n * 10),
    tap((n) => console.log("valeur :", n)),
).subscribe();                                           // valeur : 20, valeur : 40
```

| Catégorie | Opérateurs | Rôle |
| --- | --- | --- |
| **Transformation** | `map`, `scan` | Transformer chaque valeur |
| **Filtrage** | `filter`, `take`, `first`, `distinctUntilChanged`, `debounceTime`, `throttleTime` | Choisir / limiter |
| **Aplatissement** (flux de flux) | `switchMap`, `mergeMap`, `concatMap`, `exhaustMap` | Enchaîner des appels asynchrones |
| **Combinaison** | `combineLatest`, `forkJoin`, `merge`, `zip`, `withLatestFrom` | Combiner plusieurs flux |
| **Erreurs** | `catchError`, `retry` | Récupération |
| **Utilitaires** | `tap`, `delay`, `finalize`, `shareReplay`, `startWith` | Effets de bord, partage |

### Quelle « map » choisir ? (aplatissement)

| Opérateur | Comportement | Cas d'usage |
| --- | --- | --- |
| **`switchMap`** | **Annule** le précédent flux interne au profit du nouveau | **Recherche en direct**, navigation |
| **`mergeMap`** | Lance en **parallèle** | Appels indépendants |
| **`concatMap`** | **Un après l'autre**, dans l'ordre | Sauvegardes ordonnées |
| **`exhaustMap`** | **Ignore** les nouvelles valeurs tant qu'un flux est actif | **Soumission de formulaire** (anti double-clic) |

### Exemple : recherche en direct

```typescript
import { Component, inject } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { FormControl, ReactiveFormsModule } from "@angular/forms";
import { toSignal } from "@angular/core/rxjs-interop";
import { catchError, debounceTime, distinctUntilChanged, filter, of, switchMap } from "rxjs";

@Component({
    selector: "app-recherche-directe",
    imports: [ReactiveFormsModule],
    template: `
        <input [formControl]="terme" placeholder="Rechercher…" />
        @for (r of resultats(); track r) { <p>{{ r }}</p> }
    `,
})
export class RechercheDirecte {
    private readonly http = inject(HttpClient);
    terme = new FormControl("", { nonNullable: true });

    resultats = toSignal(
        this.terme.valueChanges.pipe(
            debounceTime(300),                              // attendre la fin de la saisie
            distinctUntilChanged(),
            filter((t) => t.length >= 2),
            switchMap((t) => this.http.get<string[]>(`/api/recherche?q=${t}`).pipe(catchError(() => of([] as string[])))),
        ),
        { initialValue: [] as string[] },
    );
}
```

## 12.3 Combiner des flux

```typescript
import { Component, inject } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { takeUntilDestroyed } from "@angular/core/rxjs-interop";
import { BehaviorSubject, combineLatest, forkJoin, map } from "rxjs";

interface Utilisateur { id: number; nom: string; }
interface Commande { id: number; total: number; }

@Component({
    selector: "app-combinaison",
    template: `<p>Résultats dans la console</p>`,
})
export class Combinaison {
    private readonly http = inject(HttpClient);
    private readonly filtre$ = new BehaviorSubject("tous");
    private readonly tri$ = new BehaviorSubject("prix");

    constructor() {
        forkJoin({
            utilisateur: this.http.get<Utilisateur>("/api/me"),
            commandes: this.http.get<Commande[]>("/api/commandes"),
        }).subscribe(({ utilisateur, commandes }) => {
            console.log(utilisateur.nom, commandes.length);               // attendre que tout soit terminé
        });

        combineLatest([this.filtre$, this.tri$])
            .pipe(map(([f, t]) => ({ f, t })), takeUntilDestroyed())      // dernière valeur de chaque flux
            .subscribe((criteres) => console.log(criteres));
    }
}
```

## 12.4 Subjects

| Type | Comportement |
| --- | --- |
| `Subject<T>` | Diffuse les nouvelles valeurs aux abonnés actuels |
| `BehaviorSubject<T>(initial)` | Garde et rejoue la **dernière valeur** (état) |
| `ReplaySubject<T>(n)` | Rejoue les `n` dernières valeurs |
| `AsyncSubject<T>` | Émet la dernière valeur à la **complétion** |

```typescript
// src/app/article.ts
export interface Article { id: number; nom: string; prix: number; quantite: number; }
```

```typescript
// src/app/panier.service.ts
import { Injectable } from "@angular/core";
import { BehaviorSubject } from "rxjs";
import { Article } from "./article";

@Injectable({ providedIn: "root" })
export class PanierService {
    private readonly articles = new BehaviorSubject<Article[]>([]);
    readonly articles$ = this.articles.asObservable();                 // ne pas exposer le Subject lui-même

    ajouter(a: Article): void {
        this.articles.next([...this.articles.value, a]);
    }
}
```

> **Astuce** : pour un **état local ou de service**, un **signal** est aujourd'hui plus simple qu'un `BehaviorSubject`.

## 12.5 Éviter les fuites mémoire *(à jour)*

Un abonnement actif **après la destruction** du composant provoque des fuites.

| Technique | Quand |
| --- | --- |
| **Tube `async`** / **`toSignal`** | Dans le gabarit : gestion automatique |
| **`takeUntilDestroyed()`** | Dans un composant / service : `flux$.pipe(takeUntilDestroyed()).subscribe(…)` |
| `take(1)`, `first()` | Flux qui n'émettent qu'une valeur utile |
| `Subscription.unsubscribe()` dans `ngOnDestroy` | Gestion manuelle (héritage) |

```typescript
import { Component, DestroyRef, inject } from "@angular/core";
import { takeUntilDestroyed } from "@angular/core/rxjs-interop";
import { interval } from "rxjs";

@Component({
    selector: "app-surveillance",
    template: `<button (click)="demarrer()">Démarrer</button>`,
})
export class Surveillance {
    private readonly destroyRef = inject(DestroyRef);

    constructor() {
        interval(1000).pipe(takeUntilDestroyed()).subscribe((n) => console.log(n));    // dans le constructeur (contexte d'injection)
    }

    protected demarrer(): void {
        interval(500).pipe(takeUntilDestroyed(this.destroyRef)).subscribe((n) => console.log(`rapide ${n}`));   // ailleurs : fournir le DestroyRef
    }
}
```

> Les requêtes `HttpClient` **se terminent seules** : pas besoin de se désabonner pour elles.

## 12.6 Chaud et froid, partage

- **Froid** : chaque abonné relance la source (requête HTTP).
- **Chaud** : la source émet indépendamment des abonnés (événements).
- **`shareReplay({ bufferSize: 1, refCount: true })`** : partage une exécution entre abonnés et met en cache la dernière valeur.

## 12.7 Bonnes pratiques

- Un seul `subscribe` à la **fin** de la chaîne ; préférez `async` / `toSignal`.
- N'imbriquez **jamais** des `subscribe` : utilisez `switchMap` et compagnie.
- Gérez les **erreurs** (`catchError`) *dans* le flux interne pour ne pas tuer le flux externe.
- Utilisez des **signaux** pour l'état, RxJS pour les **flux asynchrones complexes** ([section 8.8](#88-signaux-ou-rxjs-)).

---

# 13. Gestion d'état

## 13.1 Quand un état global est-il nécessaire ?

| Niveau | Solution |
| --- | --- |
| État **local** à un composant | `signal()` dans le composant |
| État **partagé** par quelques composants | **Service** avec signaux (suffisant dans la majorité des cas) |
| État **complexe**, traçable, partagé par beaucoup de fonctionnalités | **NgRx** (Store ou **SignalStore**) |
| État **serveur** (cache de données) | `resource` / `httpResource`, ou bibliothèques de requêtes |

## 13.2 Service avec signaux (recommandé par défaut)

```typescript
// src/app/panier.store.ts
import { Injectable, computed, signal } from "@angular/core";
import { Article } from "./article";

@Injectable({ providedIn: "root" })
export class PanierStore {
    private readonly _articles = signal<Article[]>([]);

    readonly articles = this._articles.asReadonly();
    readonly nombre = computed(() => this._articles().length);
    readonly total = computed(() => this._articles().reduce((s, a) => s + a.prix * a.quantite, 0));

    ajouter(article: Article): void {
        this._articles.update((liste) => [...liste, article]);
    }
    retirer(id: number): void {
        this._articles.update((liste) => liste.filter((a) => a.id !== id));
    }
    vider(): void { this._articles.set([]); }
}
```

## 13.3 NgRx

**NgRx** est la bibliothèque d'état de référence (inspirée de Redux) : **Store** (état immuable), **actions**, **réducteurs**, **sélecteurs**, **effets**, **outils de développement** (historique, « voyage dans le temps »).

```bash
ng add @ngrx/store
ng add @ngrx/effects
ng add @ngrx/store-devtools
```

```typescript
// src/app/panier.state.ts
import { createActionGroup, props, emptyProps, createFeature, createReducer, on, createSelector } from "@ngrx/store";
import { Article } from "./article";

export const PanierActions = createActionGroup({
    source: "Panier",
    events: {
        "Ajouter article": props<{ article: Article }>(),
        "Retirer article": props<{ id: number }>(),
        "Vider": emptyProps(),
        "Charger": emptyProps(),
        "Chargement reussi": props<{ articles: Article[] }>(),
        "Chargement echoue": props<{ erreur: string }>(),
    },
});

interface EtatPanier { articles: Article[] }
const initial: EtatPanier = { articles: [] };

export const panierFeature = createFeature({
    name: "panier",
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

```typescript
// src/app/app.config.ts
import { ApplicationConfig } from "@angular/core";
import { provideStore } from "@ngrx/store";
import { provideEffects } from "@ngrx/effects";
import { provideStoreDevtools } from "@ngrx/store-devtools";
import { panierFeature } from "./panier.state";
import { chargerArticles } from "./panier.effects";

export const appConfig: ApplicationConfig = {
    providers: [
        provideStore({ [panierFeature.name]: panierFeature.reducer }),
        provideEffects({ chargerArticles }),
        provideStoreDevtools({ maxAge: 25 }),
    ],
};
```

```typescript
// src/app/panier-ngrx.ts
import { Component, inject } from "@angular/core";
import { Store } from "@ngrx/store";
import { Article } from "./article";
import { PanierActions, panierFeature } from "./panier.state";

@Component({
    selector: "app-panier-ngrx",
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

### Effets (actions asynchrones)

```typescript
// src/app/article.service.ts
import { Injectable, inject } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { Article } from "./article";

@Injectable({ providedIn: "root" })
export class ArticleService {
    private readonly http = inject(HttpClient);
    lister(): Observable<Article[]> { return this.http.get<Article[]>("/api/articles"); }
}
```

```typescript
// src/app/panier.effects.ts
import { inject } from "@angular/core";
import { Actions, createEffect, ofType } from "@ngrx/effects";
import { catchError, exhaustMap, map, of } from "rxjs";
import { ArticleService } from "./article.service";
import { PanierActions } from "./panier.state";

export const chargerArticles = createEffect(
    (actions$ = inject(Actions), service = inject(ArticleService)) =>
        actions$.pipe(
            ofType(PanierActions.charger),
            exhaustMap(() => service.lister().pipe(
                map((articles) => PanierActions.chargementReussi({ articles })),
                catchError((erreur) => of(PanierActions.chargementEchoue({ erreur: String(erreur) }))),
            )),
        ),
    { functional: true },
);
```

## 13.4 NgRx SignalStore *(à jour)*

Une version **plus légère**, entièrement basée sur les signaux :

```typescript
// src/app/panier.signal-store.ts
import { computed, inject } from "@angular/core";
import { signalStore, withState, withComputed, withMethods, patchState } from "@ngrx/signals";
import { firstValueFrom } from "rxjs";
import { Article } from "./article";
import { ArticleService } from "./article.service";

export const PanierSignalStore = signalStore(
    { providedIn: "root" },
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

Utilisation dans un composant :

```typescript
import { Component, inject } from "@angular/core";
import { PanierSignalStore } from "./panier.signal-store";

@Component({
    selector: "app-panier-signal-store",
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

## 13.5 Autres solutions

| Outil | Remarques |
| --- | --- |
| **NgRx Store** | Standard des grandes applications, très structuré, plus de code |
| **NgRx SignalStore** | Moderne, léger, API simple |
| **NGXS** | Approche à décorateurs, moins de code répétitif |
| **Akita** | **Plus maintenu** : à éviter pour de nouveaux projets |
| **Elf** | Bibliothèque réactive légère |
| **Service + signaux** | **Suffisant pour la plupart des applications** |

## 13.6 Comparaison

| Critère | Service + signaux | NgRx Store | NgRx SignalStore |
| --- | --- | --- | --- |
| Complexité | Faible | Élevée | Moyenne |
| Traçabilité (devtools) | Non | Oui | Oui (avec extensions) |
| Quantité de code | Faible | Élevée | Moyenne |
| Équipes nombreuses / règles strictes | Moyen | Adapté | Adapté |

> **Commencez simple** (service + signaux). N'ajoutez NgRx que si la complexité de l'état l'exige.

---

# 14. Animations

## 14.1 Animations CSS natives *(à jour)*

Depuis la **version 20.2**, Angular propose des **liaisons natives** d'entrée / sortie d'éléments basées sur le **CSS** : `animate.enter` et `animate.leave`. Le paquet **`@angular/animations`** (DSL `trigger`, `state`, `transition`) est **déprécié** au profit de cette approche.

```typescript
import { Component, signal } from "@angular/core";

@Component({
    selector: "app-notification",
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

Autres outils CSS : **transitions** (`transition: all .3s`), **`@keyframes`**, **View Transitions** du routeur (`withViewTransitions()`), `prefers-reduced-motion` (accessibilité).

## 14.2 `@angular/animations` *(héritage)*

Encore présent dans de nombreux projets (et dans Angular Material jusqu'à migration) :

```typescript
// src/app/boite.ts
import { Component, signal } from "@angular/core";
import { trigger, state, style, transition, animate } from "@angular/animations";

@Component({
    selector: "app-boite",
    animations: [
        trigger("ouverture", [
            state("ferme", style({ height: "0", opacity: 0 })),
            state("ouvert", style({ height: "*", opacity: 1 })),
            transition("ferme <=> ouvert", animate("300ms ease-in-out")),
            transition(":enter", [style({ opacity: 0 }), animate("200ms", style({ opacity: 1 }))]),
            transition(":leave", [animate("200ms", style({ opacity: 0 }))]),
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
import { ApplicationConfig } from "@angular/core";
import { provideAnimationsAsync } from "@angular/platform-browser/animations/async";

export const appConfig: ApplicationConfig = {
    providers: [provideAnimationsAsync()],
};
```

Fonctions : `state`, `transition`, `animate`, `keyframes`, `query`, `stagger`, `group`, `sequence`, callbacks `(@ouverture.done)`.

## 14.3 Bonnes pratiques

- Privilégiez les animations **CSS** et les propriétés **`transform` / `opacity`** (accélérées par le GPU).
- Respectez **`prefers-reduced-motion`**.
- Évitez d'animer `width`, `height`, `top`, `left` (reflux de mise en page).
- Gardez des durées **courtes** (150–400 ms).

---

# 15. Bibliothèques et espaces de travail

## 15.1 Créer une bibliothèque Angular

Une **bibliothèque** regroupe des composants, directives, tubes et services **réutilisables** entre applications (compilée avec **ng-packagr**).

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
├── ng-package.json
└── package.json
```

```typescript
// public-api.ts
export * from "./lib/bouton/bouton";
```

```typescript
// projects/ui-kit/src/lib/bouton/bouton.ts : composant autonome de bibliothèque
import { ChangeDetectionStrategy, Component } from "@angular/core";

@Component({
    selector: "kit-bouton",
    template: `<button><ng-content /></button>`,
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class KitBouton {}
```

```bash
ng build ui-kit                                  # dist/ui-kit
cd dist/ui-kit && npm publish                    # publier sur npm
```

> **Astuce** : en développement, le chemin `@mon-espace/ui-kit` est mappé sur le code source via `paths` dans `tsconfig.json`. Pensez à construire la bibliothèque avant l'application, ou à utiliser `ng build --watch`.

## 15.2 Bonnes pratiques de bibliothèque

- **Composants autonomes** (pas de `NgModule`) ; exposer une API **minimale**.
- Utiliser `input()` / `output()`, `OnPush`, `provideXxx()` pour la configuration.
- Versionnement **sémantique**, `peerDependencies` sur `@angular/core`.
- Documenter (Storybook, Compodoc) et tester.

## 15.3 Espaces de travail multi-projets et monorepos

Un **espace de travail** Angular peut contenir plusieurs **applications** et **bibliothèques** (`projects/`). Pour de grands dépôts :

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

Voir aussi la [section 28](#28-migration-et-mises-à-jour) pour l'ajout de Nx à un projet existant.

---

# Tests

---

# 16. Tests unitaires

## 16.1 L'outillage *(à jour)*

| | **Avant** | **Aujourd'hui** |
| --- | --- | --- |
| Exécuteur | **Karma** (navigateur) — déprécié depuis 2023 | **Vitest** (**par défaut depuis la v21**, stable en v22) |
| Cadre d'assertions | Jasmine | API de Vitest (`describe`, `it`, `expect`, `vi`), compatible Jasmine/Jest dans l'esprit |
| Environnement | Chrome (navigateur réel) | jsdom / happy-dom, ou **mode navigateur** de Vitest |
| Outil Angular | `TestBed` | `TestBed` (inchangé) |

```bash
ng test                      # exécute les tests (surveillance par défaut en local)
ng test --no-watch --coverage
```

> **Migration** : migrer un projet Karma/Jasmine : `ng generate @angular/core:karma-to-vitest` (voir [section 28](#28-migration-et-mises-à-jour)). Karma et Jasmine restent utilisables sur les projets existants.

## 16.2 Tester un composant

```typescript
// src/app/compteur.spec.ts
import { TestBed } from "@angular/core/testing";
import { describe, it, expect } from "vitest";               // optionnel : les globales sont disponibles avec `ng test`
import { Compteur } from "./compteur";

describe("Compteur", () => {
    it("incrémente la valeur au clic", async () => {
        const fixture = TestBed.createComponent(Compteur);
        await fixture.whenStable();                           // attend le premier rendu (mode zoneless)

        const bouton = fixture.nativeElement.querySelector("button") as HTMLButtonElement;
        bouton.click();
        await fixture.whenStable();                           // attend la mise à jour de la vue

        expect(fixture.nativeElement.querySelector("h2")?.textContent).toContain("1");
    });
});
```

Tester une entrée de type signal :

```typescript
// src/app/carte-produit.spec.ts
import { TestBed } from "@angular/core/testing";
import { describe, it, expect } from "vitest";
import { CarteProduit } from "./carte-produit";

describe("CarteProduit", () => {
    it("affiche le titre transmis en entrée", async () => {
        const fixture = TestBed.createComponent(CarteProduit);
        fixture.componentRef.setInput("nom", "Livre");        // entrées signaux : toujours via setInput()
        await fixture.whenStable();
        expect(fixture.nativeElement.textContent).toContain("Livre");
    });
});
```

> **À retenir** : avec des composants **zoneless / signaux**, on attend le rendu avec **`await fixture.whenStable()`**. En mode avec Zone.js, `fixture.detectChanges()` reste utilisable.

## 16.3 Tester un service

```typescript
// src/app/panier.store.spec.ts
import { TestBed } from "@angular/core/testing";
import { beforeEach, describe, it, expect } from "vitest";
import { PanierStore } from "./panier.store";

describe("PanierStore", () => {
    let store: PanierStore;
    beforeEach(() => {
        TestBed.configureTestingModule({});
        store = TestBed.inject(PanierStore);
    });

    it("calcule le total", () => {
        store.ajouter({ id: 1, nom: "Livre", prix: 10, quantite: 2 });
        store.ajouter({ id: 2, nom: "Stylo", prix: 5, quantite: 1 });
        expect(store.total()).toBe(25);
    });
});
```

## 16.4 Tester les appels HTTP

```typescript
// src/app/utilisateur.spec.ts
import { TestBed } from "@angular/core/testing";
import { provideHttpClient } from "@angular/common/http";
import { provideHttpClientTesting, HttpTestingController } from "@angular/common/http/testing";
import { afterEach, beforeEach, describe, it, expect } from "vitest";
import { Utilisateur, UtilisateurService } from "./utilisateur";

describe("UtilisateurService", () => {
    let service: UtilisateurService;
    let http: HttpTestingController;

    beforeEach(() => {
        TestBed.configureTestingModule({ providers: [provideHttpClient(), provideHttpClientTesting()] });
        service = TestBed.inject(UtilisateurService);
        http = TestBed.inject(HttpTestingController);
    });
    afterEach(() => http.verify());                           // aucune requête non attendue

    it("récupère un utilisateur", () => {
        let resultat: Utilisateur | undefined;
        service.trouver(1).subscribe((u) => (resultat = u));

        const requete = http.expectOne("/api/utilisateurs/1");
        expect(requete.request.method).toBe("GET");
        requete.flush({ id: 1, nom: "Alice", email: "a@b.fr" });

        expect(resultat?.nom).toBe("Alice");
    });

    it("gère les erreurs", () => {
        let statut = 0;
        service.trouver(9).subscribe({ error: (e) => (statut = e.status) });
        http.expectOne("/api/utilisateurs/9").flush("Introuvable", { status: 404, statusText: "Not Found" });
        expect(statut).toBe(404);
    });
});
```

## 16.5 Doublures (*mocks*) et injection

```typescript
import { TestBed } from "@angular/core/testing";
import { afterEach, describe, it, expect, vi } from "vitest";
import { of } from "rxjs";
import { UtilisateurService } from "./utilisateur";

describe("Doublures", () => {
    afterEach(() => vi.useRealTimers());

    it("remplace le service réel par une doublure", () => {
        const serviceFactice = { lister: vi.fn().mockReturnValue(of([{ id: 1, nom: "Alice", email: "a@b.fr" }])) };

        TestBed.configureTestingModule({
            providers: [{ provide: UtilisateurService, useValue: serviceFactice }],         // remplace le service réel
        });

        TestBed.inject(UtilisateurService).lister().subscribe((liste) => expect(liste).toHaveLength(1));
        expect(serviceFactice.lister).toHaveBeenCalledTimes(1);
    });

    it("espionne la console et simule le temps", () => {
        const espion = vi.spyOn(console, "error").mockImplementation(() => {});
        console.error("Erreur simulée");
        expect(espion).toHaveBeenCalledWith("Erreur simulée");

        vi.useFakeTimers();
        const rappel = vi.fn();
        setTimeout(rappel, 1000);
        vi.advanceTimersByTime(1000);
        expect(rappel).toHaveBeenCalledTimes(1);
    });
});
```

Pour des composants avec routeur : `provideRouter([])` et `RouterTestingHarness`.

## 16.6 Harnais de composants (*component harnesses*)

Les **harnais** (CDK) offrent une API **stable** pour interagir avec des composants (Material, Aria, ou vos composants) **sans dépendre du HTML interne**.

```typescript
import { Component } from "@angular/core";
import { TestBed } from "@angular/core/testing";
import { TestbedHarnessEnvironment } from "@angular/cdk/testing/testbed";
import { MatButton } from "@angular/material/button";
import { MatButtonHarness } from "@angular/material/button/testing";
import { describe, it, expect } from "vitest";

@Component({
    selector: "app-envoi",
    imports: [MatButton],
    template: `<button mat-button>Envoyer</button>`,
})
class Envoi {}

describe("Envoi", () => {
    it("expose un bouton activé", async () => {
        const fixture = TestBed.createComponent(Envoi);
        const loader = TestbedHarnessEnvironment.loader(fixture);

        const bouton = await loader.getHarness(MatButtonHarness.with({ text: "Envoyer" }));
        await bouton.click();
        expect(await bouton.isDisabled()).toBe(false);
    });
});
```

## 16.7 Tester des signaux et effets

```typescript
import { computed, effect, signal } from "@angular/core";
import { TestBed } from "@angular/core/testing";
import { describe, it, expect } from "vitest";

describe("signaux", () => {
    it("réagit aux signaux", () => {
        TestBed.runInInjectionContext(() => {
            const s = signal(1);
            const d = computed(() => s() * 2);
            s.set(5);
            expect(d()).toBe(10);
        });
    });

    it("exécute un effet", () => {
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

## 16.8 Couverture et bonnes pratiques

```bash
ng test --coverage                # rapport dans coverage/
```

- Tester le **comportement** (ce que voit l'utilisateur), pas les détails d'implémentation.
- **Un cas par test**, nommé clairement ; schéma *Arrange – Act – Assert*.
- Peu de `TestBed` pour la logique pure : testez les fonctions et services **sans TestBed** quand c'est possible.
- Isolez les dépendances (HTTP, routeur, horloge).
- Exécutez les tests en **CI** (`ng test --no-watch`).

---

# 17. Tests de bout en bout (E2E)

## 17.1 Panorama *(à jour)*

Les tests **E2E** pilotent un **vrai navigateur** pour valider des parcours utilisateur complets.

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

## 17.2 Exemple avec Playwright

```typescript
// e2e/connexion.spec.ts
import { test, expect } from "@playwright/test";

test("un utilisateur peut se connecter", async ({ page }) => {
    await page.goto("/connexion");
    await page.getByLabel("E-mail").fill("alice@exemple.com");
    await page.getByLabel("Mot de passe").fill("secret");
    await page.getByRole("button", { name: "Se connecter" }).click();

    await expect(page).toHaveURL(/tableau-de-bord/);
    await expect(page.getByRole("heading", { name: "Bonjour Alice" })).toBeVisible();
});

test("affiche une erreur si le mot de passe est faux", async ({ page }) => {
    await page.route("**/api/connexion", (route) => route.fulfill({ status: 401, json: { message: "Identifiants invalides" } }));   // API simulée
    await page.goto("/connexion");
    await page.getByLabel("E-mail").fill("alice@exemple.com");
    await page.getByLabel("Mot de passe").fill("faux");
    await page.getByRole("button", { name: "Se connecter" }).click();
    await expect(page.getByText("Identifiants invalides")).toBeVisible();
});
```

```typescript
// playwright.config.ts (extrait)
import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
    testDir: "./e2e",
    use: { baseURL: "http://localhost:4200", trace: "on-first-retry" },
    webServer: { command: "ng serve", url: "http://localhost:4200", reuseExistingServer: !process.env["CI"] },
    projects: [{ name: "chromium", use: { ...devices["Desktop Chrome"] } }, { name: "firefox", use: { ...devices["Desktop Firefox"] } }],
});
```

## 17.3 Exemple avec Cypress

```typescript
// cypress/e2e/connexion.cy.ts
describe("Connexion", () => {
    it("connecte l'utilisateur", () => {
        cy.visit("/connexion");
        cy.get("input[name=email]").type("alice@exemple.com");
        cy.get("input[name=motDePasse]").type("secret");
        cy.contains("button", "Se connecter").click();
        cy.url().should("include", "/tableau-de-bord");
    });
});
```

## 17.4 Bonnes pratiques E2E

- Sélectionnez par **rôle / libellé accessible** (`getByRole`, `getByLabel`) ou `data-testid`, pas par classes CSS.
- Testez les **parcours critiques** (connexion, achat), pas chaque détail.
- **Isolez les données** (comptes de test, API simulée ou base de test).
- Évitez les **attentes fixes** (`waitForTimeout`) : utilisez les attentes automatiques.
- Exécutez en **CI** ; conservez **traces et captures** en cas d'échec.
- Pyramide de tests : **beaucoup** de tests unitaires, **quelques** tests d'intégration, **peu** de tests E2E.

---

# Performance

---

# 18. Détection des changements

## 18.1 Principe

La **détection des changements** (*change detection*) décide **quand** mettre à jour le DOM. Il existe deux modèles.

| | **Avec Zone.js** (historique) | **Zoneless** (moderne) |
| --- | --- | --- |
| Déclencheur | **Zone.js** intercepte événements, minuteries, promesses et lance une vérification de l'arbre | **Signaux**, événements du gabarit, `markForCheck`, tube `async` |
| Précision | Vérifie (tout ou partie de) l'arbre | Met à jour **ce qui a changé** |
| Taille / perf | Zone.js (~35 Ko), vérifications superflues | Moins de code, plus rapide |
| Débogage | Piles d'appels complexes | Plus lisible |
| Statut | Toujours supporté | **Défaut des nouveaux projets depuis la v21** |

## 18.2 Passer en zoneless

```typescript
// src/app/app.config.ts
import { ApplicationConfig, provideZonelessChangeDetection } from "@angular/core";

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

### Conditions pour qu'un composant soit « compatible zoneless »

- L'état affiché provient de **signaux** (ou du tube `async`).
- Pas de dépendance à des **modifications silencieuses** de champs ordinaires (`this.x = …` dans un `setTimeout`) : utilisez un **signal**.
- Les bibliothèques tierces doivent notifier Angular (`ChangeDetectorRef.markForCheck()` ou un signal).

## 18.3 Stratégies : `Default` et `OnPush`

| Stratégie | Le composant est vérifié quand… |
| --- | --- |
| `Default` | À chaque cycle de détection |
| **`OnPush`** | Une **entrée** change (par référence), un **événement** du composant se produit, un **signal** lu dans le gabarit change, `markForCheck()` est appelé |

```typescript
// src/app/liste.ts
import { ChangeDetectionStrategy, Component, input } from "@angular/core";

@Component({
    selector: "app-liste",
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

> **v22** : `OnPush` devient la stratégie **par défaut** des nouveaux composants. Pour les composants existants, la migration est automatique et préserve la stratégie `Default` explicite quand elle est nécessaire.

### Avec `OnPush`, mettez à jour de façon **immuable**

```typescript
import { ChangeDetectionStrategy, Component } from "@angular/core";
import { Liste } from "./liste";

@Component({
    selector: "app-articles-immuables",
    imports: [Liste],
    changeDetection: ChangeDetectionStrategy.OnPush,
    template: `
        <app-liste [articles]="articles" />
        <button (click)="ajouter('Nouveau')">Ajouter</button>
    `,
})
export class ArticlesImmuables {
    protected articles: string[] = ["A", "B"];

    protected ajouter(nouveau: string): void {
        this.articles = [...this.articles, nouveau];            // correct : nouvelle référence
        // this.articles.push(nouveau);                         // incorrect : non détecté (sauf signal)
    }
}
```

## 18.4 Outils

```typescript
import { ChangeDetectorRef, Component, inject } from "@angular/core";

@Component({
    selector: "app-detection",
    template: `<p>{{ message }}</p>`,
})
export class Detection {
    private readonly cdr = inject(ChangeDetectorRef);
    protected message = "Initial";

    constructor() {
        setTimeout(() => {
            this.message = "Modifié";
            this.cdr.markForCheck();          // planifie la vérification du composant (et de ses ancêtres)
            // this.cdr.detectChanges();      // vérification immédiate (à éviter)
        }, 1000);
    }
}
```

## 18.5 Réduire le travail de détection

| Technique | Effet |
| --- | --- |
| **Signaux + `OnPush`** | Mises à jour ciblées |
| **`track`** dans `@for` | Réutilise le DOM |
| Pas d'appels de **méthodes** lourdes dans le gabarit | Utiliser `computed()` ou des tubes purs |
| **`@defer`** | Reporter le rendu de zones non critiques |
| **`NgZone.runOutsideAngular()`** (avec Zone.js) | Exécuter des tâches fréquentes (animations, `mousemove`) sans déclencher de détection |
| **Défilement virtuel** (`cdk-virtual-scroll-viewport`) | Grandes listes |

## 18.6 Mesurer

- **Angular DevTools** (extension Chrome / Firefox) : profileur de détection des changements, arbre de composants, graphe de signaux.
- **Lighthouse**, **Web Vitals** (LCP, INP, CLS), panneau *Performance* du navigateur.

---

# 19. Chargement paresseux et vues différées

## 19.1 Pourquoi ?

Charger **uniquement le code nécessaire** réduit le temps de chargement initial (**FCP / LCP**) : le reste est téléchargé **à la demande**.

## 19.2 Routes à chargement paresseux

```typescript
// src/app/app.routes.ts
import { Routes } from "@angular/router";
import { Accueil } from "./accueil/accueil";

export const routes: Routes = [
    { path: "", component: Accueil },                                                            // dans le bundle initial
    { path: "produits", loadComponent: () => import("./produits/liste").then((m) => m.Liste) },   // composant paresseux
    { path: "admin", loadChildren: () => import("./admin/admin.routes").then((m) => m.ADMIN_ROUTES) },   // groupe de routes
];
```

```typescript
// src/app/admin/admin.routes.ts
import { Routes } from "@angular/router";
import { AdminAccueil } from "./admin-accueil";
import { AdminService } from "./admin.service";

export const ADMIN_ROUTES: Routes = [
    { path: "", component: AdminAccueil, providers: [AdminService] },                // providers propres à ces routes
    { path: "utilisateurs", loadComponent: () => import("./utilisateurs").then((m) => m.Utilisateurs) },
];
```

```typescript
// src/app/admin/admin.service.ts
import { Injectable } from "@angular/core";

@Injectable()                                   // fourni par les routes d'administration (pas providedIn: "root")
export class AdminService {
    nom = "Espace d'administration";
}
```

Raccourci si le composant est exporté **par défaut** : `loadComponent: () => import("./liste")`.

> *(héritage)* Avec les `NgModule` : `loadChildren: () => import("./admin/admin.module").then(m => m.AdminModule)`. Migration : `ng generate @angular/core:route-lazy-loading`.

## 19.3 Stratégies de préchargement

| Stratégie | Fonctionnement |
| --- | --- |
| `NoPreloading` | Chargement **à la navigation** (défaut) |
| `PreloadAllModules` | Précharge **tout** une fois l'application stable |
| **Personnalisée** | Choisir quelles routes précharger (réseau, priorité) |

```typescript
// src/app/prechargement-selectif.ts
import { Injectable } from "@angular/core";
import { PreloadingStrategy, Route } from "@angular/router";
import { Observable, of } from "rxjs";

@Injectable({ providedIn: "root" })
export class PrechargementSelectif implements PreloadingStrategy {
    preload(route: Route, charger: () => Observable<unknown>): Observable<unknown> {
        return route.data?.["precharger"] ? charger() : of(null);
    }
}
```

```typescript
// src/app/app.config.ts
import { ApplicationConfig } from "@angular/core";
import { provideRouter, withPreloading } from "@angular/router";
import { routes } from "./app.routes";
import { PrechargementSelectif } from "./prechargement-selectif";

export const appConfig: ApplicationConfig = {
    providers: [provideRouter(routes, withPreloading(PrechargementSelectif))],
};
```

```typescript
// src/app/app.routes.ts (extrait) : cette route sera préchargée
import { Routes } from "@angular/router";

export const routes: Routes = [
    {
        path: "rapports",
        loadChildren: () => import("./rapports/rapports.routes").then((m) => m.RAPPORTS_ROUTES),
        data: { precharger: true },
    },
];
```

## 19.4 Vues différées : `@defer` *(ajout)*

Le bloc **`@defer`** charge **paresseusement** un composant, une directive ou un tube **dans un gabarit**, selon un **déclencheur**.

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

| Déclencheur | Moment |
| --- | --- |
| `on idle` (**défaut**) | Navigateur inactif |
| `on viewport` | L'élément (ou un placeholder) entre dans la **zone visible** |
| `on interaction` | Clic / focus sur un élément déclencheur |
| `on hover` | Survol |
| `on immediate` | Dès que possible (après le rendu initial) |
| `on timer(5s)` | Après un délai |
| `when condition()` | Quand une expression devient vraie |

```html
<button #declencheur>Afficher les commentaires</button>
@defer (on interaction(declencheur); prefetch on idle) {
    <app-commentaires />
}
```

Composant hôte de ces deux exemples, avec les trois composants différés (un fichier chacun dans un vrai projet) :

```typescript
// src/app/graphique-lourd.ts
import { Component, input } from "@angular/core";

@Component({ selector: "app-graphique-lourd", template: `<p>Graphique : {{ donnees().join(", ") }}</p>` })
export class GraphiqueLourd {
    donnees = input<number[]>([]);
}

// src/app/spinner.ts
@Component({ selector: "app-spinner", template: `<p>Chargement…</p>` })
export class Spinner {}

// src/app/commentaires.ts
@Component({ selector: "app-commentaires", template: `<p>Aucun commentaire.</p>` })
export class Commentaires {}
```

```typescript
// src/app/differe.ts
import { Component, signal } from "@angular/core";
import { GraphiqueLourd } from "./graphique-lourd";
import { Spinner } from "./spinner";
import { Commentaires } from "./commentaires";

@Component({
    selector: "app-differe",
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

- **`prefetch`** : télécharge le code à l'avance (sans l'afficher).
- **Hydratation incrémentale** (SSR) : `@defer (hydrate on viewport)` hydrate des zones **plus tard** ([section 22](#22-rendu-côté-serveur-ssr-pré-rendu-et-hydratation)).
- Les composants différés doivent être **autonomes** et **non référencés ailleurs** (sinon ils restent dans le bundle initial).

## 19.5 Chargement conditionnel de code

```typescript
// src/app/editeur.ts
import { Component } from "@angular/core";

@Component({ selector: "app-editeur", template: `<textarea></textarea>` })
export class Editeur {}
```

```typescript
// src/app/page-editeur.ts
import { Component, ViewContainerRef, viewChild } from "@angular/core";

@Component({
    selector: "app-page-editeur",
    template: `
        <button (click)="ouvrirEditeur()">Ouvrir l'éditeur</button>
        <ng-container #conteneur />
    `,
})
export class PageEditeur {
    private readonly conteneur = viewChild.required("conteneur", { read: ViewContainerRef });

    protected async ouvrirEditeur(): Promise<void> {
        const { Editeur } = await import("./editeur");           // import dynamique
        this.conteneur().createComponent(Editeur);
    }
}
```

## 19.6 Vérifier le résultat

```bash
ng build --stats-json          # puis analyser avec esbuild analyzer / webpack-bundle-analyzer
```

Dans la sortie du build : **« Initial chunk files »** (bundle de démarrage) vs **« Lazy chunk files »** (chargés à la demande). Objectif : un **bundle initial réduit**.

## 19.7 Bonnes pratiques

- **Une route principale = un morceau paresseux** (fonctionnalités, administration, rapports).
- Gardez dans le bundle initial **uniquement** la page d'accueil, la mise en page et les services transverses.
- Combinez **préchargement** et **`@defer`** pour la fluidité.
- Évitez qu'un import **statique** d'un module paresseux l'inclue dans le bundle initial.

---

# 20. Compilation AOT et optimisation du bundle

## 20.1 JIT et AOT

| | **JIT** (*Just-in-Time*) | **AOT** (*Ahead-of-Time*) |
| --- | --- | --- |
| Compilation | Dans le **navigateur**, à l'exécution | À la **construction** (build) |
| Taille | Compilateur embarqué (lourd) | **Plus léger** |
| Démarrage | Plus lent | **Plus rapide** |
| Erreurs de gabarit | À l'exécution | **Au build** |
| Statut | Rare (tests) | **Défaut** (`ng serve` et `ng build`) |

L'AOT fonctionne avec le moteur de compilation **Ivy** (par défaut depuis la v9), qui produit du code **ciblé et tree-shakable**.

## 20.2 Vérifications du compilateur

```json
{ "angularCompilerOptions": { "strictTemplates": true, "strictInjectionParameters": true, "strictInputAccessModifiers": true,
                              "extendedDiagnostics": { "checks": { "optionalChainNotNullable": "error" } } } }
```

Le compilateur détecte : propriétés inexistantes dans les gabarits, types incompatibles, `@for` sans `track`, imports inutilisés (diagnostics étendus).

## 20.3 Builder `application` (esbuild + Vite)

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
| `budgets` | **Alerte ou échoue** si le bundle dépasse une taille |
| `outputHashing` | Noms de fichiers avec empreinte (cache longue durée) |
| `optimization` | Minification, suppression de code mort, inlining des polices et CSS critiques |
| `sourceMap` | Cartes sources (désactiver ou `hidden` en production) |
| `externalDependencies`, `prerender`, `ssr` | Options du builder |

## 20.4 Tree shaking et code mort

Le **tree shaking** supprime le code **non utilisé** à la compilation.

```typescript
// Correct : importer précisément
import { debounce } from "lodash-es";                // build ESM, tree-shakable
// Incorrect : import _ from "lodash";                     // embarque toute la bibliothèque

const rechercher = debounce((terme: string) => console.log(`Recherche : ${terme}`), 300);
rechercher("angular");
```

| Pratique | Effet |
| --- | --- |
| `providedIn: "root"` (services **tree-shakables**) | Un service jamais injecté n'est pas inclus |
| Composants **autonomes** et imports ciblés | Pas de modules entiers embarqués |
| Préférer des bibliothèques **ESM** (`lodash-es`, `date-fns`) | Meilleur élagage |
| Éviter les imports de **barils** massifs (`index.ts` qui réexporte tout) | Moins de code inutile |
| `sideEffects: false` dans le `package.json` de vos bibliothèques | Autorise l'élagage |

## 20.5 Optimisations fréquentes

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
import { Component } from "@angular/core";
import { NgOptimizedImage } from "@angular/common";

@Component({
    selector: "app-bannieres",
    imports: [NgOptimizedImage],
    template: `
        <img ngSrc="/img/hero.jpg" width="1200" height="600" priority alt="Bannière" />
        <img ngSrc="/img/produit.jpg" width="400" height="300" alt="Produit" />       <!-- paresseuse par défaut -->
    `,
})
export class Bannieres {}
```

## 20.6 Analyser le bundle

```bash
ng build --stats-json
npx esbuild-visualizer --metadata dist/mon-app/stats.json --open        # carte des dépendances
# ou : source-map-explorer dist/**/*.js
```

## 20.7 Liste de contrôle performance

- [ ] Composants `OnPush` + signaux, `track` dans les boucles
- [ ] Routes **paresseuses**, `@defer` pour le non-critique
- [ ] **Zoneless**
- [ ] SSR / pré-rendu + hydratation (+ incrémentale)
- [ ] `NgOptimizedImage`, polices optimisées
- [ ] Budgets définis, bundle surveillé en CI
- [ ] Compression et cache HTTP configurés

---

# Essentiels

---

# 21. Internationalisation (i18n)

## 21.1 Deux approches

| | **i18n intégrée d'Angular** (`$localize`) | **Bibliothèques d'exécution** (Transloco, ngx-translate) |
| --- | --- | --- |
| Traduction | **À la compilation** : un **build par langue** | **À l'exécution** : fichiers JSON, changement de langue à chaud |
| Performance | Excellente (texte déjà traduit) | Un peu moins (chargement des fichiers) |
| Changer de langue | Rechargement / autre URL | **Instantané** |
| Outils | XLIFF / XMB, extraction par le CLI | JSON, très simple |

## 21.2 i18n intégrée

```bash
ng add @angular/localize                 # active $localize
```

### Marquer les textes

```typescript
import { Component, signal } from "@angular/core";

@Component({
    selector: "app-accueil-i18n",
    template: `
        <h1 i18n="@@titreAccueil">Bienvenue sur notre site</h1>                       <!-- id explicite (@@) = stable -->
        <p i18n="Message d'accueil|Description pour le traducteur@@intro">Découvrez nos produits.</p>
        <img [src]="logo" i18n-alt alt="Logo de l'entreprise" />                      <!-- attribut -->
        <span i18n>Mise à jour {{ minutes() }} minutes plus tôt</span>
    `,
})
export class AccueilI18n {
    protected readonly logo = "/img/logo.png";
    protected readonly minutes = signal(5);
}
```

```typescript
// $localize est fourni par @angular/localize (ajouté par `ng add @angular/localize`)
const message = $localize`:@@erreurReseau:Impossible de joindre le serveur.`;     // dans le code TypeScript
console.error(message);
```

### Pluriels et sélection (format ICU)

```typescript
import { Component, signal } from "@angular/core";

@Component({
    selector: "app-messages-icu",
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
    protected readonly genre = signal("feminin");
}
```

### Extraire et traduire

```bash
ng extract-i18n --format xlf2 --output-path src/locale        # génère messages.xlf
# → copier en messages.fr.xlf, messages.en.xlf… et traduire les <target>
```

### Configurer les langues

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

> Chaque langue est servie sous son propre chemin (`/fr/`, `/en/`) : configurez le serveur ou le CDN en conséquence.

## 21.3 Formats localisés

Les tubes `date`, `currency`, `number`, `percent` utilisent la **locale** active (`LOCALE_ID`) :

```typescript
// src/app/app.config.ts
import { ApplicationConfig, LOCALE_ID } from "@angular/core";
import { registerLocaleData } from "@angular/common";
import localeFr from "@angular/common/locales/fr";

registerLocaleData(localeFr);

export const appConfig: ApplicationConfig = {
    providers: [{ provide: LOCALE_ID, useValue: "fr-FR" }],
};
```

```typescript
import { Component } from "@angular/core";
import { CurrencyPipe, DatePipe } from "@angular/common";

@Component({
    selector: "app-formats",
    imports: [CurrencyPipe, DatePipe],
    template: `
        <p>{{ 1234.5 | currency: "EUR" }}</p>     <!-- 1 234,50 € -->
        <p>{{ date | date: "fullDate" }}</p>      <!-- dimanche 11 octobre 2026 -->
    `,
})
export class Formats {
    protected readonly date = new Date(2026, 9, 11);
}
```

Pour d'autres besoins : l'API **`Intl`** du navigateur (`Intl.NumberFormat`, `Intl.DateTimeFormat`, `Intl.RelativeTimeFormat`).

## 21.4 Traduction à l'exécution avec Transloco *(ajout)*

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
import { Component, inject, signal } from "@angular/core";
import { TranslocoPipe, TranslocoService } from "@jsverse/transloco";

@Component({
    selector: "app-accueil-transloco",
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
    protected readonly utilisateur = signal("Alice");

    protected changerLangue(l: string): void { this.transloco.setActiveLang(l); }
}
```



Alternatives : **ngx-translate** (très répandue), **Lingui**.

## 21.5 Choisir et bonnes pratiques

| Besoin | Choix |
| --- | --- |
| Performance maximale, langues fixes, SEO par URL | **i18n intégrée** |
| Changement de langue **instantané**, textes dynamiques | **Transloco / ngx-translate** |

- **Ne concaténez jamais** des fragments traduits : utilisez des **paramètres** ou le format ICU.
- Prévoyez **l'expansion du texte** (l'allemand est plus long) et le **sens d'écriture** (RTL : arabe, hébreu → `dir="rtl"`).
- Utilisez des **identifiants explicites** (`@@clé`) pour des traductions stables.
- Traduisez aussi `title`, `alt`, `aria-label`, et les **messages d'erreur**.

---

# 22. Rendu côté serveur (SSR), pré-rendu et hydratation

## 22.1 Pourquoi ?

| Mode | Principe | Avantages |
| --- | --- | --- |
| **CSR** (*client-side rendering*) | Le navigateur construit la page | Simple, hébergement statique |
| **SSR** (*server-side rendering*) | Le serveur renvoie du **HTML complet** à chaque requête | **SEO**, **LCP** plus rapide, aperçus sociaux |
| **SSG / pré-rendu** (*prerender*) | HTML généré **au build** pour des routes connues | Très rapide, hébergement statique, SEO |
| **Hydratation** | Le navigateur **réutilise** le HTML serveur et l'« active » | Évite le scintillement et la reconstruction |

> **À jour** : **Angular Universal** (`@nguniversal/*`) est **abandonné** ; le SSR est **intégré au CLI** (`@angular/ssr`) et au builder `application`.

## 22.2 Activer le SSR

```bash
ng new mon-app --ssr                  # nouveau projet
ng add @angular/ssr                   # projet existant
```

Ajoute notamment : `server.ts` (serveur Node : Express ou autre), `main.server.ts`, `app.config.server.ts`, `app.routes.server.ts`.

```typescript
// src/app/app.config.ts
import { ApplicationConfig } from "@angular/core";
import { provideHttpClient, withFetch } from "@angular/common/http";
import { provideClientHydration, withEventReplay, withIncrementalHydration } from "@angular/platform-browser";

export const appConfig: ApplicationConfig = {
    providers: [
        provideClientHydration(withEventReplay(), withIncrementalHydration()),
        provideHttpClient(withFetch()),
    ],
};
```

```typescript
// src/app/app.routes.server.ts : mode de rendu PAR ROUTE
import { RenderMode, ServerRoute } from "@angular/ssr";

async function listerIds(): Promise<number[]> {
    return [1, 2, 3];                                                                // en pratique : lecture d'une API ou d'un fichier
}

export const serverRoutes: ServerRoute[] = [
    { path: "", renderMode: RenderMode.Prerender },                                  // généré au build
    { path: "produits/:id", renderMode: RenderMode.Prerender,
      async getPrerenderParams() { return (await listerIds()).map((id) => ({ id: String(id) })); } },
    { path: "compte", renderMode: RenderMode.Client },                               // uniquement côté client
    { path: "**", renderMode: RenderMode.Server },                                   // rendu à chaque requête
];
```

```bash
ng build                              # produit le serveur et/ou les pages pré-rendues
node dist/mon-app/server/server.mjs   # lancer le serveur SSR
```

## 22.3 Hydratation

L'**hydratation** associe le DOM déjà rendu par le serveur à l'application Angular, au lieu de le **détruire et reconstruire**.

| Fonctionnalité | Rôle |
| --- | --- |
| `provideClientHydration()` | Active l'hydratation |
| `withEventReplay()` | **Rejoue** les clics et saisies faits **avant** la fin de l'hydratation |
| `withIncrementalHydration()` | Hydrate par **zones** différées : `@defer (hydrate on viewport) { … }` |
| `ngSkipHydration` | Exclut un composant incompatible (manipulation directe du DOM) |

```typescript
import { Component } from "@angular/core";
import { Commentaires } from "./commentaires";

@Component({
    selector: "app-discussion",
    imports: [Commentaires],
    template: `
        @defer (hydrate on interaction) {
            <app-commentaires />                     <!-- rendu serveur immédiat, activation au premier clic -->
        } @placeholder { <p>Commentaires</p> }
    `,
})
export class Discussion {}
```

## 22.4 Écrire du code compatible SSR

Côté serveur, `window`, `document`, `localStorage`… **n'existent pas**.

```typescript
import { Component, PLATFORM_ID, afterNextRender, inject } from "@angular/core";
import { DOCUMENT, isPlatformBrowser } from "@angular/common";

@Component({
    selector: "app-carte",
    template: `<div id="carte"></div>`,
})
export class Carte {
    private readonly plateforme = inject(PLATFORM_ID);
    private readonly document = inject(DOCUMENT);               // au lieu de la globale `document`

    constructor() {
        afterNextRender(() => {                                  // exécuté UNIQUEMENT dans le navigateur
            const conteneur = this.document.getElementById("carte");
            console.log("Initialisation de la carte dans", conteneur);
        });
        if (isPlatformBrowser(this.plateforme)) {
            console.log(localStorage.getItem("theme"));
        }
    }
}
```

- **Évitez** d'accéder directement à `window` / `document` ; utilisez `afterNextRender`, `DOCUMENT`, `isPlatformBrowser`.
- Les **minuteries** longues (`setInterval`) ne doivent pas bloquer la stabilité de l'application côté serveur.
- Les requêtes `HttpClient` côté serveur sont **mises en cache de transfert** : le navigateur ne les refait pas.
- **Titre et métadonnées** (SEO) : services `Title` et `Meta`.

```typescript
import { Component, inject } from "@angular/core";
import { Meta, Title } from "@angular/platform-browser";

@Component({
    selector: "app-produit-seo",
    template: `<h1>Produit</h1>`,
})
export class ProduitSeo {
    constructor() {
        inject(Title).setTitle("Produit — Ma boutique");
        inject(Meta).updateTag({ name: "description", content: "Description du produit" });
    }
}
```

## 22.5 Bonnes pratiques et sécurité

- **Pré-rendez** les pages publiques stables, utilisez le **SSR** pour le contenu dynamique, **CSR** pour les zones privées.
- **Ne mettez pas de secrets** dans le code exécuté côté client **et** côté serveur sans distinction : les variables d'environnement serveur restent côté serveur.
- Ne **fuyez pas de données utilisateur** entre requêtes (pas de singletons stockant des données de session côté serveur).
- Contrôlez les **en-têtes** (`Host`, `X-Forwarded-*`) et configurez les hôtes autorisés (protection SSRF / empoisonnement de l'hôte), en suivant les consignes des versions récentes.
- Mesurez : **LCP**, **TTFB**, **INP**.

---

# 23. Applications web progressives (PWA)

## 23.1 Qu'est-ce qu'une PWA ?

Une **PWA** est une application web **installable**, utilisable **hors ligne** et pouvant recevoir des **notifications push**, grâce à un **Service Worker** et un **manifeste**.

| Élément | Rôle |
| --- | --- |
| **HTTPS** | Obligatoire (sauf `localhost`) |
| **Manifeste** (`manifest.webmanifest`) | Nom, icônes, couleurs, mode d'affichage (installation) |
| **Service Worker** | Proxy réseau : **cache**, hors ligne, push, synchronisation |

## 23.2 Ajouter le support PWA

```bash
ng add @angular/pwa
```

Ce qui est ajouté : `manifest.webmanifest`, **icônes**, `ngsw-config.json`, balises dans `index.html`, et le fournisseur du Service Worker :

```typescript
// src/app/app.config.ts
import { ApplicationConfig, isDevMode } from "@angular/core";
import { provideServiceWorker } from "@angular/service-worker";

export const appConfig: ApplicationConfig = {
    providers: [
        provideServiceWorker("ngsw-worker.js", {
            enabled: !isDevMode(),                              // actif seulement en production
            registrationStrategy: "registerWhenStable:30000",
        }),
    ],
};
```

## 23.3 Configurer le cache : `ngsw-config.json`

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

| Stratégie de données | Comportement |
| --- | --- |
| `freshness` | Réseau d'abord, cache en secours (**données à jour**) |
| `performance` | Cache d'abord (**rapidité**, données parfois périmées) |

## 23.4 Mises à jour et notifications

```typescript
import { Component, inject } from "@angular/core";
import { takeUntilDestroyed } from "@angular/core/rxjs-interop";
import { SwUpdate, VersionReadyEvent, SwPush } from "@angular/service-worker";
import { filter } from "rxjs";

const CLE_VAPID_PUBLIQUE = "REMPLACER_PAR_VOTRE_CLE_VAPID_PUBLIQUE";        // générée côté serveur

@Component({
    selector: "app-mises-a-jour",
    template: `<button (click)="abonnerPush()">Activer les notifications</button>`,
})
export class MisesAJour {
    private readonly maj = inject(SwUpdate);
    private readonly push = inject(SwPush);

    constructor() {
        this.maj.versionUpdates
            .pipe(filter((e): e is VersionReadyEvent => e.type === "VERSION_READY"), takeUntilDestroyed())
            .subscribe(() => {
                if (confirm("Nouvelle version disponible. Recharger ?")) document.location.reload();
            });
        this.maj.checkForUpdate().catch((erreur) => console.error("Vérification impossible", erreur));
    }

    protected async abonnerPush(): Promise<void> {
        const abonnement = await this.push.requestSubscription({ serverPublicKey: CLE_VAPID_PUBLIQUE });
        await fetch("/api/push/abonner", { method: "POST", body: JSON.stringify(abonnement) });
    }
}
```

## 23.5 Tester une PWA

Le Service Worker n'est **pas actif** avec `ng serve`. Construire puis servir :

```bash
ng build
npx http-server -p 8080 -c-1 dist/mon-app/browser
```

Puis **DevTools → Application** (Service Workers, Manifest, Cache Storage) et **Lighthouse** (audit PWA). Testez le mode **hors ligne** (case « Offline »).

## 23.6 Bonnes pratiques

- Servir en **HTTPS**, fournir des **icônes** (192 et 512 px, « maskable »).
- Prévoir une **page de repli hors ligne** et une UX de **mise à jour** claire.
- Adapter la **stratégie de cache** par type de ressource.
- Ne pas mettre en cache de données **sensibles** ; prévoir l'invalidation à la déconnexion.

---

# 24. Angular Material, CDK et Aria

## 24.1 Les trois bibliothèques

| Bibliothèque | Contenu |
| --- | --- |
| **Angular Material** | Composants d'interface selon **Material Design 3** (boutons, tables, dialogues…) |
| **Angular CDK** (*Component Dev Kit*) | **Briques de comportement** sans style : overlay, glisser-déposer, défilement virtuel, accessibilité |
| **Angular Aria** *(stable en v22)* | **Primitives accessibles non stylées** (combobox, listbox, menu, onglets, accordéon, arbre, grille) à habiller avec votre propre design |

## 24.2 Installer Angular Material

```bash
ng add @angular/material
```

Choisissez un thème ; le CLI configure les polices, icônes et styles.

## 24.3 Utiliser les composants

```typescript
import { Component, inject, signal } from "@angular/core";
import { FormControl, ReactiveFormsModule, Validators } from "@angular/forms";
import { MatButtonModule } from "@angular/material/button";
import { MatCardModule } from "@angular/material/card";
import { MatFormFieldModule } from "@angular/material/form-field";
import { MatInputModule } from "@angular/material/input";
import { MatTableModule } from "@angular/material/table";
import { MatSnackBar } from "@angular/material/snack-bar";

@Component({
    selector: "app-profil",
    imports: [MatButtonModule, MatCardModule, MatFormFieldModule, MatInputModule, MatTableModule, ReactiveFormsModule],
    template: `
        <mat-card>
            <mat-card-header><mat-card-title>Profil</mat-card-title></mat-card-header>
            <mat-card-content>
                <mat-form-field appearance="outline">
                    <mat-label>Nom</mat-label>
                    <input matInput [formControl]="nom" />
                    @if (nom.hasError("required")) { <mat-error>Le nom est obligatoire</mat-error> }
                </mat-form-field>
            </mat-card-content>
            <mat-card-actions><button mat-flat-button (click)="enregistrer()">Enregistrer</button></mat-card-actions>
        </mat-card>

        <table mat-table [dataSource]="lignes()">
            <ng-container matColumnDef="nom"><th mat-header-cell *matHeaderCellDef>Nom</th><td mat-cell *matCellDef="let l">{{ l.nom }}</td></ng-container>
            <tr mat-header-row *matHeaderRowDef="colonnes"></tr>
            <tr mat-row *matRowDef="let ligne; columns: colonnes"></tr>
        </table>
    `,
})
export class Profil {
    private readonly barre = inject(MatSnackBar);
    protected readonly nom = new FormControl("", { nonNullable: true, validators: [Validators.required] });
    protected readonly colonnes = ["nom"];
    protected readonly lignes = signal([{ nom: "Alice" }]);

    protected enregistrer(): void {
        this.barre.open("Enregistré !", "OK", { duration: 3000 });
    }
}
```

Composants courants : `mat-toolbar`, `mat-sidenav`, `mat-list`, `mat-select`, `mat-checkbox`, `mat-datepicker`, `mat-paginator`, `mat-sort`, `mat-tabs`, `mat-stepper`, `mat-menu`, `mat-tooltip`, `mat-chips`, `mat-progress-bar`, `mat-dialog`, `mat-snack-bar`.

## 24.4 Thèmes (Material 3)

```scss
// styles.scss
@use "@angular/material" as mat;

html {
    @include mat.theme((
        color: mat.$azure-palette,
        typography: Roboto,
        density: 0,
    ));
}
```

Personnalisation par **variables CSS** (`--mat-sys-primary`, etc.) : changement de thème clair/sombre sans recompiler (`color-scheme: light dark`).

## 24.5 Le CDK

| Module | Usage |
| --- | --- |
| **Overlay** | Fenêtres flottantes, menus déroulants, info-bulles |
| **Drag and Drop** | Listes réordonnables (`cdkDrag`, `cdkDropList`) |
| **Scrolling** | **Défilement virtuel** pour de très grandes listes |
| **Layout** | `BreakpointObserver` : réagir aux tailles d'écran |
| **A11y** | Piégeage du focus (`cdkTrapFocus`), annonces (`LiveAnnouncer`) |
| **Clipboard**, **Portal**, **Table**, **Stepper**, **Testing** (harnais) | |


```typescript
import { Component } from "@angular/core";
import { ScrollingModule } from "@angular/cdk/scrolling";

@Component({
    selector: "app-liste-virtuelle",
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
import { Component, inject } from "@angular/core";
import { toSignal } from "@angular/core/rxjs-interop";
import { BreakpointObserver, Breakpoints } from "@angular/cdk/layout";
import { map } from "rxjs";

@Component({
    selector: "app-adaptatif",
    template: `<p>{{ mobile() ? "Affichage mobile" : "Affichage large" }}</p>`,
})
export class Adaptatif {
    // Réagir au point de rupture
    protected readonly mobile = toSignal(
        inject(BreakpointObserver).observe(Breakpoints.Handset).pipe(map((r) => r.matches)),
        { initialValue: false },
    );
}
```

## 24.6 Angular Aria

Des **comportements accessibles prêts à l'emploi** (navigation clavier, rôles et attributs ARIA, gestion du focus) **sans imposer de style** : vous fournissez le HTML et le CSS. Les primitives comprennent, entre autres, **combobox / autocomplétion**, **listbox / select**, **menu / barre d'outils**, **onglets**, **accordéon**, **arbre** et **grille**. Chaque primitive est fournie avec des **harnais de test**.

> Consultez la documentation d'**Angular Aria** sur [angular.dev](https://angular.dev) pour l'API exacte (elle a évolué pendant la phase d'aperçu).

## 24.7 Bonnes pratiques

- **N'importez que les composants utilisés** (autonomes).
- Utilisez les **harnais** pour les tests.
- Respectez l'**accessibilité** (libellés, contrastes, ordre du focus).
- Pour un **design system** propre : **CDK + Aria** plutôt que de combattre le style de Material.
- Autres bibliothèques d'interface : **PrimeNG**, **NG-ZORRO**, **Taiga UI**, **Spartan UI**.

---

# 25. Bibliothèques tierces

## 25.1 Choisir une bibliothèque

| Critère | À vérifier |
| --- | --- |
| **Compatibilité** | Version d'Angular supportée (`peerDependencies`), composants **autonomes**, **zoneless**, SSR |
| **Maintenance** | Dernière publication, issues ouvertes, nombre de mainteneurs |
| **Taille** | Coût dans le bundle (Bundlephobia), *tree-shaking* (ESM) |
| **Typage** | Types TypeScript inclus |
| **Licence** | Compatible avec votre usage |
| **Accessibilité** | Navigation clavier, ARIA |

```bash
ng add <paquet>          # préférez cette commande quand le paquet fournit un schematic
npm install <paquet>
```

## 25.2 Bibliothèques Angular courantes

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

## 25.3 Intégrer une bibliothèque JavaScript **non Angular**

### 1) Installer avec ses types

```bash
npm install chart.js
npm install -D @types/leaflet        # si la bibliothèque n'a pas ses propres types
```

### 2) L'encapsuler dans un composant (côté navigateur uniquement)

```typescript
import {
    ChangeDetectionStrategy, Component, DestroyRef, ElementRef, afterNextRender, effect, inject, input, viewChild,
} from "@angular/core";
import { Chart } from "chart.js/auto";

@Component({
    selector: "app-graphique",
    template: `<canvas #toile></canvas>`,
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class Graphique {
    donnees = input.required<number[]>();
    private readonly toile = viewChild.required<ElementRef<HTMLCanvasElement>>("toile");
    private graphique?: Chart;

    constructor() {
        afterNextRender(() => {                                                   // le DOM existe ; jamais côté serveur
            this.graphique = new Chart(this.toile().nativeElement, {
                type: "line",
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

### 3) Types manquants

```typescript
// src/types/ancienne-lib.d.ts
declare module "ancienne-lib" {
    export function faire(x: number): string;
}
```

Une fois la déclaration en place, le module s'importe avec ses types :

```typescript
import { faire } from "ancienne-lib";

console.log(faire(42));
```

### 4) Styles et scripts globaux

```jsonc
// angular.json (extrait : options de la cible "build")
{
    "options": {
        "styles": ["node_modules/bibliotheque/dist/style.css"],
        "scripts": ["node_modules/bibliotheque/dist/script.js"]
    }
}
```

## 25.4 Pièges d'intégration

| Problème | Solution |
| --- | --- |
| La bibliothèque modifie le DOM hors d'Angular | Encapsuler dans un composant, `afterNextRender`, `ngSkipHydration` si besoin |
| `window is not defined` (SSR) | `afterNextRender`, `isPlatformBrowser`, import dynamique |
| Mises à jour non détectées (zoneless / `OnPush`) | Passer par des **signaux** ou `markForCheck()` |
| Fuites mémoire | `destroy()` dans `DestroyRef.onDestroy` |
| Module CommonJS lourd | Chercher une version **ESM** ; `allowedCommonJsDependencies` en dernier recours |
| Bibliothèque non compatible avec la version d'Angular | Vérifier les `peerDependencies`, chercher un fork maintenu |

## 25.5 Bonnes pratiques

- **Auditez** (`npm audit`) et **verrouillez** les versions (`package-lock.json`).
- Limitez le nombre de dépendances : chacune est un risque de **maintenance et de sécurité**.
- Chargez les bibliothèques **lourdes** de façon **paresseuse** (`import()`, `@defer`).
- Documentez les raisons des choix (ADR).

---

# 26. Sécurité

## 26.1 Principes

| Menace | Protection Angular / bonne pratique |
| --- | --- |
| **XSS** (injection de scripts) | **Échappement automatique** des liaisons, assainissement du HTML, CSP, Trusted Types |
| **CSRF / XSRF** | Jeton XSRF (`withXsrfConfiguration`), cookies `SameSite` |
| **Injection via URL** (`javascript:`) | Assainissement des URL et des ressources |
| **Secrets exposés** | Jamais de secrets dans le code client |
| **Dépendances vulnérables** | `npm audit`, mises à jour régulières |
| **Contrôle d'accès contourné** | **Contrôles côté serveur** (les gardes ne suffisent pas) |

## 26.2 XSS : la protection intégrée

Angular **traite toute valeur liée comme non fiable** et l'**échappe** automatiquement.

```typescript
import { Component, signal } from "@angular/core";

@Component({
    selector: "app-xss",
    template: `
        <p>{{ saisie() }}</p>                     <!-- affiché comme TEXTE, pas exécuté -->
        <div [innerHTML]="saisie()"></div>        <!-- assaini automatiquement (onerror supprimé) -->
    `,
})
export class Xss {
    protected readonly saisie = signal("<img src=x onerror='alert(1)'>");
}
```



Angular assainit : **HTML** (`[innerHTML]`), **styles**, **URL** (`href`, `src`) et **URL de ressources** (`<iframe src>`, `<script src>`).

### Contourner l'assainissement : **à n'utiliser qu'en dernier recours**

```typescript
import { Component, inject } from "@angular/core";
import { DomSanitizer } from "@angular/platform-browser";

@Component({
    selector: "app-contenu-confiance",
    template: `
        <div [innerHTML]="html"></div>
        <iframe [src]="urlVideo" title="Vidéo"></iframe>
    `,
})
export class ContenuConfiance {
    private readonly sanitizer = inject(DomSanitizer);
    private readonly contenuDeConfiance = "<p>Contenu rédigé par l'équipe</p>";

    protected readonly html = this.sanitizer.bypassSecurityTrustHtml(this.contenuDeConfiance);      // ATTENTION : DÉSACTIVE la protection
    protected readonly urlVideo = this.sanitizer.bypassSecurityTrustResourceUrl("https://www.youtube.com/embed/xxxx");
}
```

> **À éviter** : **ne contournez jamais** l'assainissement pour du contenu venant d'un utilisateur ou d'une API non maîtrisée. Si vous devez afficher du HTML riche : assainissez-le avec **DOMPurify** (ou l'**API Sanitizer** du navigateur) **avant**.

### À éviter

```typescript
import { Component, ElementRef, inject } from "@angular/core";

@Component({
    selector: "app-a-eviter",
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

## 26.3 Content Security Policy (CSP) et Trusted Types

```text
Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-ABC123'; style-src 'self' 'nonce-ABC123'; require-trusted-types-for 'script'
```

- Le **nonce** est injecté par le serveur ; en SSR, fournissez-le avec le jeton `CSP_NONCE` ; `autoCsp` (builder) peut générer une CSP **stricte** basée sur des empreintes.
- **Trusted Types** : Angular est compatible (`trusted-types angular angular#bundler`).

## 26.4 CSRF / XSRF

Le client HTTP Angular lit un **cookie** (`XSRF-TOKEN`) et renvoie sa valeur dans un en-tête (`X-XSRF-TOKEN`) pour les requêtes **modifiantes** (POST, PUT, DELETE) vers la **même origine**.

```typescript
// src/app/app.config.ts
import { ApplicationConfig } from "@angular/core";
import { provideHttpClient, withXsrfConfiguration } from "@angular/common/http";

export const appConfig: ApplicationConfig = {
    providers: [
        provideHttpClient(withXsrfConfiguration({ cookieName: "XSRF-TOKEN", headerName: "X-XSRF-TOKEN" })),
    ],
};
```

Le serveur doit **valider** l'en-tête. Complétez avec des cookies **`SameSite=Lax/Strict`**, **`Secure`**, **`HttpOnly`** (pour les cookies de session).

## 26.5 Stockage des jetons et données sensibles

| Où | Risque |
| --- | --- |
| `localStorage` / `sessionStorage` | **Lisibles par n'importe quel script** (XSS) : à éviter pour les jetons sensibles |
| **Cookie `HttpOnly`** (+ `Secure`, `SameSite`) | Non lisible par JavaScript : meilleur choix pour les sessions |
| Mémoire (variable / signal) | Disparaît au rechargement ; plus sûr contre le vol persistant |

## 26.6 Autres bonnes pratiques

- **HTTPS partout** ; en-têtes : `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `Referrer-Policy`, `Permissions-Policy`.
- **Validez et nettoyez côté serveur** : le client est modifiable par l'utilisateur.
- **Aucun secret** (clés d'API privées, mots de passe) dans le code ni dans les environnements front.
- **Dépendances** : `npm audit`, `npm ci`, Dependabot/Renovate ; vérifier les paquets avant installation.
- **Ouvrir des liens externes** avec `rel="noopener noreferrer"`.
- **Messages d'erreur** génériques (pas de traces techniques).
- **Mettre à jour Angular** : les correctifs de sécurité sont publiés pour les versions supportées (la v22 en a intégré plusieurs, appliqués automatiquement lors de la mise à jour).
- Revue de sécurité : **OWASP Top 10**, **OWASP ASVS**, guide de sécurité sur [angular.dev/best-practices/security](https://angular.dev/best-practices/security).

---

# 27. Authentification et autorisation

## 27.1 Définitions

| | **Authentification** | **Autorisation** |
| --- | --- | --- |
| Question | **Qui êtes-vous ?** | **Que pouvez-vous faire ?** |
| Exemple | Connexion, SSO | Rôles, permissions |

## 27.2 Les approches

| Approche | Principe | Remarques |
| --- | --- | --- |
| **Session par cookie** (`HttpOnly`) | Le serveur émet un cookie de session | Simple et sûr pour les applications web ; protéger contre le CSRF |
| **JWT** (jeton signé) | Jeton envoyé dans `Authorization: Bearer` | Sans état côté serveur ; **durée de vie courte** + jeton de rafraîchissement |
| **OAuth 2.0 / OpenID Connect** (flux **Authorization Code + PKCE**) | Délégation à un fournisseur d'identité (Keycloak, Auth0, Entra ID, Google…) | **Recommandé** pour le SSO et les applications publiques |
| **BFF** (*Backend For Frontend*) | Un petit serveur gère les jetons et expose un cookie à l'application | Le plus sûr : aucun jeton dans le navigateur |

> **À éviter** : l'ancien flux OAuth « **Implicit** » est **déprécié** : utilisez **Authorization Code avec PKCE**.

## 27.3 Un service d'authentification avec signaux

```typescript
// src/app/auth/auth.ts
import { Injectable, inject, signal, computed } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Router } from "@angular/router";
import { firstValueFrom } from "rxjs";

interface Utilisateur { id: number; nom: string; roles: string[] }
interface ReponseConnexion { jeton: string; utilisateur: Utilisateur }

@Injectable({ providedIn: "root" })
export class AuthService {
    private readonly http = inject(HttpClient);
    private readonly router = inject(Router);

    private readonly _utilisateur = signal<Utilisateur | null>(null);
    private readonly _jeton = signal<string | null>(null);              // en mémoire : pas de localStorage

    readonly utilisateur = this._utilisateur.asReadonly();
    readonly jeton = this._jeton.asReadonly();
    readonly estConnecte = computed(() => this._utilisateur() !== null);

    async connecter(email: string, motDePasse: string): Promise<void> {
        const r = await firstValueFrom(this.http.post<ReponseConnexion>("/api/auth/connexion", { email, motDePasse }));
        this._jeton.set(r.jeton);
        this._utilisateur.set(r.utilisateur);
    }

    async rafraichir(): Promise<void> {
        const r = await firstValueFrom(this.http.post<ReponseConnexion>("/api/auth/rafraichir", {}));
        this._jeton.set(r.jeton);
        this._utilisateur.set(r.utilisateur);
    }

    async deconnecter(): Promise<void> {
        await firstValueFrom(this.http.post("/api/auth/deconnexion", {}));
        this._jeton.set(null);
        this._utilisateur.set(null);
        await this.router.navigateByUrl("/connexion");
    }

    aLeRole(role: string): boolean { return this._utilisateur()?.roles.includes(role) ?? false; }
}
```

## 27.4 Intercepteur, garde et rafraîchissement du jeton

```typescript
// src/app/http/intercepteurs.ts (extrait) : version avancée de authInterceptor, qui remplace celle de la section 11.4
import { inject } from "@angular/core";
import { HttpInterceptorFn, HttpErrorResponse } from "@angular/common/http";
import { catchError, from, switchMap, throwError } from "rxjs";
import { AuthService } from "../auth/auth";

export const authInterceptor: HttpInterceptorFn = (req, next) => {
    const auth = inject(AuthService);
    const jeton = auth.jeton();
    const requete = jeton && req.url.startsWith("/api") ? req.clone({ setHeaders: { Authorization: `Bearer ${jeton}` } }) : req;

    return next(requete).pipe(
        catchError((e: HttpErrorResponse) => {
            if (e.status === 401 && !req.url.includes("/auth/")) {
                return from(auth.rafraichir()).pipe(                              // tenter un rafraîchissement, puis rejouer
                    switchMap(() => next(req.clone({ setHeaders: { Authorization: `Bearer ${auth.jeton()}` } }))),
                    catchError(() => { auth.deconnecter(); return throwError(() => e); }),
                );
            }
            return throwError(() => e);
        }),
    );
};
```

```typescript
// src/app/auth/gardes.ts (complément à la section 9.6) : garde de rôle pour `canMatch`
import { inject } from "@angular/core";
import { CanMatchFn, Router } from "@angular/router";
import { AuthService } from "./auth";

export const roleMatchGuard = (role: string): CanMatchFn => () =>
    inject(AuthService).aLeRole(role) || inject(Router).createUrlTree(["/interdit"]);
```

Avec `canMatch`, le code de la route n'est même pas téléchargé si l'utilisateur n'a pas le rôle :

```typescript
// src/app/app.routes.ts (extrait)
import { Routes } from "@angular/router";
import { roleMatchGuard } from "./auth/gardes";

export const routes: Routes = [
    {
        path: "admin",
        canMatch: [roleMatchGuard("admin")],
        loadChildren: () => import("./admin/admin.routes").then((m) => m.ADMIN_ROUTES),
    },
];
```

## 27.5 Autorisation dans l'interface

```typescript
import { Component, inject } from "@angular/core";
import { AuthService } from "./auth/auth";

@Component({
    selector: "app-actions-admin",
    template: `
        @if (auth.aLeRole("admin")) {
            <button (click)="supprimer()">Supprimer</button>
        }
    `,
})
export class ActionsAdmin {
    protected readonly auth = inject(AuthService);

    protected supprimer(): void {
        console.log("Suppression demandée (le serveur doit la contrôler)");
    }
}
```

Une directive structurelle ou un composant `*appPermission` peut centraliser cette logique.

> **À éviter** : **masquer un bouton n'est pas de la sécurité.** Chaque action doit être **contrôlée côté serveur** (rôles, propriété des ressources). Les gardes de route ne protègent que l'**expérience** utilisateur.

## 27.6 OpenID Connect avec Authorization Code + PKCE

Plutôt que d'écrire le flux vous-même, utilisez une **bibliothèque certifiée** :

```bash
npm install angular-oauth2-oidc          # ou angular-auth-oidc-client, oidc-client-ts
```

```typescript
// src/app/auth-oidc.ts
import { Injectable, inject } from "@angular/core";
import { AuthConfig, OAuthService } from "angular-oauth2-oidc";

const configAuth: AuthConfig = {
    issuer: "https://auth.exemple.com/realms/mon-royaume",
    clientId: "mon-app-angular",
    redirectUri: window.location.origin + "/",
    responseType: "code",                                  // Authorization Code + PKCE
    scope: "openid profile email",
    showDebugInformation: false,
};

@Injectable({ providedIn: "root" })
export class AuthOidc {
    private readonly oauth = inject(OAuthService);

    async initialiser(): Promise<void> {
        this.oauth.configure(configAuth);
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
import { ApplicationConfig, inject, provideAppInitializer } from "@angular/core";
import { provideHttpClient } from "@angular/common/http";
import { provideOAuthClient } from "angular-oauth2-oidc";
import { AuthOidc } from "./auth-oidc";

export const appConfig: ApplicationConfig = {
    providers: [
        provideHttpClient(),
        provideOAuthClient(),
        provideAppInitializer(() => inject(AuthOidc).initialiser()),
    ],
};
```

## 27.7 Bonnes pratiques

- **Cookies `HttpOnly`** ou **BFF** de préférence ; sinon jetons **en mémoire**, de **courte durée**.
- **Rafraîchissement** et **rotation** des jetons, **révocation** à la déconnexion.
- **Ne stockez pas** de mots de passe ; imposez des **règles** et l'**authentification multifacteur** (MFA), **passkeys** (WebAuthn).
- Utilisez des **fournisseurs d'identité** reconnus plutôt que d'implémenter vous-même.
- Journalisez les événements sensibles ; limitez le **débit** des tentatives (côté serveur).

---

# 28. Migration et mises à jour

## 28.1 Mettre à jour Angular

Angular publie une version majeure **tous les 6 mois**, avec une **mise à jour guidée** :

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

> **Astuce** : `ng update` exécute des **schematics** qui **réécrivent votre code** automatiquement.

## 28.2 Migrations vers l'Angular moderne

Chaque migration est un **schematic** exécutable **indépendamment**, en vérifiant le résultat (diff Git) :

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

La migration `standalone` se fait en **trois passes** : *convert-to-standalone* → *prune-ng-modules* → *standalone-bootstrap*.

## 28.3 Passer en zoneless

1. Rendre l'état **réactif** (signaux, tube `async`, `markForCheck`).
2. Activer `provideZonelessChangeDetection()` et retirer `zone.js` des `polyfills`.
3. Corriger les composants qui modifiaient des champs ordinaires hors du cycle de vie.
4. Vérifier les tests (`await fixture.whenStable()`) et les bibliothèques tierces.

## 28.4 Stratégie de migration d'une grande application

1. **Mettre à jour** vers la dernière version majeure (c'est la **première étape**).
2. Migrer vers les **composants autonomes**, puis le **nouveau flux de contrôle**, puis `inject()`.
3. Passer au **builder esbuild** (`application`).
4. Adopter progressivement les **signaux** (`input`, `computed`, état de service), puis **zoneless** et **`OnPush`**.
5. Remplacer Karma par **Vitest**, Protractor par **Playwright / Cypress**, TSLint par **ESLint**.
6. Introduire les **Signal Forms** pour les nouveaux formulaires.

> **À retenir** : les anciennes et nouvelles approches **cohabitent** : migrez **progressivement**, par fonctionnalité.

## 28.5 Migrer depuis AngularJS (1.x)

AngularJS est **en fin de vie** (2022). Deux voies : **réécriture** par fonctionnalités, ou migration **hybride** avec `@angular/upgrade` (cohabitation temporaire). Dans la pratique, planifiez une migration **par pages**, avec un routeur commun pendant la transition.

## 28.6 Problèmes fréquents

| Symptôme | Cause / solution |
| --- | --- |
| `ng update` refuse de s'exécuter | Commit en attente (`--allow-dirty`), ou version non supportée : avancer d'**une** version majeure |
| Conflits de dépendances (`peer deps`) | Mettre à jour les bibliothèques, ou `--legacy-peer-deps` temporairement |
| `NullInjectorError` après migration | Fournisseur manquant dans `app.config.ts` (`provideHttpClient()`, `provideRouter()`) |
| Erreurs de gabarit nouvelles | Mode `strictTemplates` : corriger les types |
| Avertissements `NgIf` / `NgFor` dépréciés | Lancer la migration `control-flow` |
| Tests cassés (Zone.js) | Migrer vers `await fixture.whenStable()`, ou conserver Zone.js dans la configuration de test |
| Webpack déprécié | Migrer vers le builder `application` |

## 28.7 Après la migration

- Reconstruire et **comparer les tailles de bundle** et les performances.
- Mettre à jour la **CI**, le **Dockerfile** (version de Node), la **documentation**.
- Activer progressivement les nouveaux **diagnostics** et règles ESLint.

---

# 29. Nouveautés par version et bonnes pratiques

## 29.1 Anciennes pratiques → pratiques actuelles

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
| `@Injectable` seul | `providedIn: "root"` (ou `@Service()` en v22) |
| Formulaires réactifs (nouveau code) | **Signal Forms** |
| `@angular/animations` | **`animate.enter` / `animate.leave`** (CSS) |
| Karma + Jasmine | **Vitest** |
| Protractor | **Playwright / Cypress** |
| TSLint | **ESLint** (`angular-eslint`) |
| Angular Universal | **`@angular/ssr`** |
| webpack | **esbuild / Vite** (`@angular/build:application`) |
| `rxjs/operators` | `import { map } from "rxjs"` |
| Fichiers `x.component.ts` | `x.ts` (convention v20+) |

## 29.2 Chronologie des fonctionnalités marquantes

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

> **À retenir** : les détails exacts de chaque version se trouvent dans l'**annonce officielle** (« Announcing Angular vNN ») sur [blog.angular.dev](https://blog.angular.dev) et dans le journal des modifications GitHub.

## 29.3 Bonnes pratiques générales

| Domaine | Pratique |
| --- | --- |
| **Architecture** | Organiser par **fonctionnalité** (`features/`), séparer *présentation* (composants « bêtes ») et *logique* (services / stores) |
| **Composants** | Autonomes, petits, `OnPush`, état en **signaux**, `computed()` plutôt que des méthodes dans le gabarit |
| **Gabarits** | `@for` avec `track`, pas de logique complexe, `@defer` pour le non-critique |
| **Services** | `providedIn: "root"`, `inject()`, état exposé en lecture seule |
| **RxJS** | Pour les flux ; `takeUntilDestroyed`, `async` / `toSignal`, jamais de `subscribe` imbriqués |
| **Typage** | Mode strict, `strictTemplates`, pas de `any` |
| **Performance** | Zoneless, routes paresseuses, SSR / pré-rendu, `NgOptimizedImage`, budgets |
| **Tests** | Vitest + TestBed, harnais, Playwright pour les parcours critiques |
| **Qualité** | ESLint (`angular-eslint`), Prettier, hooks Git, CI (build + tests + lint) |
| **Accessibilité** | HTML sémantique, ARIA, navigation au clavier, contrastes (CDK a11y, Angular Aria) |
| **Sécurité** | Aucun contournement d'assainissement, CSP, contrôles côté serveur, dépendances à jour |
| **Mises à jour** | Rester **à jour** : une version majeure tous les 6 mois, migrations automatiques |

## 29.4 Structure de projet recommandée

Par souci de lisibilité, les exemples de ce guide placent les fichiers à plat sous `src/app/`. Dans un projet réel, rangez-les comme ci-dessous (par exemple `auth/` et `http/` sous `core/`).

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

## 29.5 Ressources

- **Documentation officielle** : <https://angular.dev>
- **Tutoriels interactifs** (dans le navigateur) : <https://angular.dev/tutorials>
- **Guide de mise à jour** : <https://angular.dev/update-guide>
- **Blog Angular** : <https://blog.angular.dev>
- **NgRx** : <https://ngrx.io> · **Angular Material** : <https://material.angular.dev> · **Nx** : <https://nx.dev>
- **Sécurité Angular** : <https://angular.dev/best-practices/security>
- **Accessibilité** : <https://angular.dev/best-practices/a11y>

---

<div align="center">

*Bon développement avec Angular !*

</div>
