<div align="center">

# 🅰️ Angular — Guide complet

**Des composants autonomes aux signaux, du SSR aux tests, avec Angular 22**

*Mis à jour pour Angular 22 (octobre 2026)*

</div>

---

## 🧰 Ressources

| Ressource | Lien |
| --- | --- |
| 📘 Documentation officielle | [angular.dev](https://angular.dev) |
| 🔄 Guide de mise à jour | [angular.dev/update-guide](https://angular.dev/update-guide) |
| 📜 Calendrier et versions | [angular.dev/reference/releases](https://angular.dev/reference/releases) |
| 📝 Exercices · ✅ Solutions · 🚀 Projets | Bientôt disponibles |

---

## 🗂️ Sommaire

**🟢 Fondamentaux**

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

**🟡 Avancé**

11. [Client HTTP](#11-client-http)
12. [Observables et RxJS](#12-observables-et-rxjs)
13. [Gestion d'état](#13-gestion-détat)
14. [Animations](#14-animations)
15. [Bibliothèques et espaces de travail](#15-bibliothèques-et-espaces-de-travail)

**🧪 Tests**

16. [Tests unitaires](#16-tests-unitaires)
17. [Tests de bout en bout (E2E)](#17-tests-de-bout-en-bout-e2e)

**⚡ Performance**

18. [Détection des changements](#18-détection-des-changements)
19. [Chargement paresseux et vues différées](#19-chargement-paresseux-et-vues-différées)
20. [Compilation AOT et optimisation du bundle](#20-compilation-aot-et-optimisation-du-bundle)

**🌍 Essentiels**

21. [Internationalisation (i18n)](#21-internationalisation-i18n)
22. [Rendu côté serveur (SSR), pré-rendu et hydratation](#22-rendu-côté-serveur-ssr-pré-rendu-et-hydratation)
23. [Applications web progressives (PWA)](#23-applications-web-progressives-pwa)
24. [Angular Material, CDK et Aria](#24-angular-material-cdk-et-aria)
25. [Bibliothèques tierces](#25-bibliothèques-tierces)
26. [Sécurité](#26-sécurité)
27. [Authentification et autorisation](#27-authentification-et-autorisation)
28. [Migration et mises à jour](#28-migration-et-mises-à-jour)
29. [Nouveautés par version et bonnes pratiques](#29-nouveautés-par-version-et-bonnes-pratiques)

> 💡 **Légende** : *(ajout)* = notion absente du guide d'origine ; *(à jour)* = pratique moderne remplaçant une ancienne ; *(héritage)* = ancienne approche, toujours rencontrée dans les projets existants.
>
> 📌 **Remarque importante** : le guide d'origine décrivait l'Angular « classique » (`NgModule`, `*ngIf`, `*ngFor`, `@Input()`, Karma…). **Angular a profondément changé depuis la version 14** : composants **autonomes** (*standalone*), **signaux**, nouveau **flux de contrôle** `@if` / `@for`, **zoneless**, **Vitest**, **Signal Forms**. Ce guide enseigne l'approche **actuelle** et explique l'ancienne pour pouvoir lire du code existant.

---

# 🟢 Fondamentaux

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
| Statut | **Fin de vie en 2022** | ✅ Maintenu |

> ⚠️ Ne confondez pas : « Angular » désigne aujourd'hui **uniquement** Angular 2+.

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

> 📌 Pour la version à utiliser aujourd'hui : **Angular 22** (ou la plus récente). Consultez [angular.dev/reference/versions](https://angular.dev/reference/versions) pour la compatibilité avec **Node.js** et **TypeScript**.

## 1.5 Prérequis

- **HTML, CSS, JavaScript moderne** (ES2020+), notions de **TypeScript**.
- **Node.js** (version LTS compatible avec la version d'Angular) et **npm**.
- Un éditeur : **VS Code** avec l'extension **Angular Language Service**.

---

# 2. TypeScript pour Angular

*Rappel des notions TypeScript indispensables (voir le guide TypeScript complet pour le détail).*

## 2.1 Types et interfaces

```typescript
let nom: string = "Alice";
let age: number = 30;
let actif: boolean = true;
let ids: number[] = [1, 2, 3];
let paire: [string, number] = ["Alice", 30];

interface Utilisateur {
    id: number;
    nom: string;
    email?: string;              // optionnelle
    readonly creeLe: Date;
}

type Role = "admin" | "editeur" | "lecteur";           // union de littéraux
```

## 2.2 Fonctions, génériques, classes

```typescript
const additionner = (a: number, b: number): number => a + b;

function premier<T>(elements: T[]): T | undefined { return elements[0]; }

class Compte {
    #solde = 0;                                         // privé natif
    constructor(public readonly titulaire: string) {}
    deposer(m: number) { this.#solde += m; }
}
```

## 2.3 Décorateurs

Angular utilise des **décorateurs** (`@Component`, `@Injectable`, `@Directive`, `@Pipe`, `@NgModule`) : des fonctions qui ajoutent des **métadonnées** à une classe. Ils sont fournis par le compilateur Angular ; vous n'avez rien à configurer.

## 2.4 Mode strict

Les nouveaux projets Angular activent le mode **strict** de TypeScript **et** des **gabarits** (`strictTemplates`) : le compilateur vérifie aussi les types **dans les templates HTML**.

```json
// tsconfig.json
{ "compilerOptions": { "strict": true, "noImplicitOverride": true, "noPropertyAccessFromIndexSignature": true },
  "angularCompilerOptions": { "strictTemplates": true, "strictInjectionParameters": true } }
```

## 2.5 Modules JavaScript

```typescript
import { Component, signal } from "@angular/core";
import type { Utilisateur } from "./modeles";          // import de type uniquement
export class MonService { }
```

---

# 3. Installation et structure d'un projet

## 3.1 Installer l'Angular CLI

```bash
node --version                            # Node.js compatible (voir angular.dev/reference/versions)
npm install -g @angular/cli
ng version
```

> 💡 Sans installation globale : `npx @angular/cli@latest new mon-app`.

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

> 📌 **Convention de nommage (à jour)** : depuis la **version 20**, le CLI ne génère plus les suffixes `.component` / `.service` : on obtient `compteur.ts` (classe `Compteur`) au lieu de `compteur.component.ts` (classe `CompteurComponent`). Les deux styles restent valides ; les migrations automatiques conservent les suffixes des projets existants. Dans ce guide, nous utilisons le style **récent**.

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
import { provideHttpClient, withFetch, withInterceptors } from "@angular/common/http";
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
<body><app-root></app-root></body>
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
    protected incrementer(): void {
        this.valeur.update((v) => v + 1);
    }
}
```

Créer un composant : `ng generate component compteur` (génère `compteur.ts`, `compteur.html`, `compteur.css`, `compteur.spec.ts`).

> ✅ **Gabarit séparé** : utilisez `templateUrl: './compteur.html'` et `styleUrl: './compteur.css'` pour les composants non triviaux.

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

@Component({
    selector: "app-carte-produit",
    template: `
        <article>
            <h3>{{ nom() }}</h3>
            <p>{{ prixTtc() | currency: "EUR" }}</p>
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

```html
<app-carte-produit [nom]="'Livre'" [prix]="12.5" (ajouter)="surAjout($event)" [(quantite)]="qte" />
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
export class Horloge implements OnInit, OnDestroy {
    private minuteur?: ReturnType<typeof setInterval>;
    ngOnInit() { this.minuteur = setInterval(() => {}, 1000); }
    ngOnDestroy() { clearInterval(this.minuteur); }
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
export class Horloge {
    constructor() {
        const id = setInterval(() => console.log("tic"), 1000);
        inject(DestroyRef).onDestroy(() => clearInterval(id));
    }
}
```

## 4.7 Projection de contenu (`ng-content`)

```typescript
@Component({
    selector: "app-panneau",
    template: `
        <header><ng-content select="[titre]" /></header>
        <section><ng-content /></section>                  <!-- contenu par défaut -->
    `,
})
export class Panneau {}
```

```html
<app-panneau>
    <h2 titre>Mon titre</h2>
    <p>Le contenu du panneau</p>
</app-panneau>
```

## 4.8 Encapsulation des styles

| Mode | Effet |
| --- | --- |
| `Emulated` (**défaut**) | Styles limités au composant (attributs générés) |
| `ShadowDom` | Vrai Shadow DOM natif |
| `None` | Styles globaux |

```typescript
@Component({ /* … */ encapsulation: ViewEncapsulation.ShadowDom })
```

Sélecteurs spéciaux : `:host` (l'élément du composant), `:host-context()`, `::ng-deep` (déprécié).

## 4.9 Liaisons sur l'hôte

```typescript
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
export class Bouton { actif = signal(false); basculer() { this.actif.update(a => !a); } }
```

> ✅ Préférez la propriété **`host`** de `@Component` aux décorateurs `@HostBinding` / `@HostListener`.

## 4.10 Modules `NgModule` *(héritage)*

Avant la version 14, tout composant devait être **déclaré** dans un **`NgModule`**. Ce modèle est toujours supporté, mais **n'est plus recommandé** pour le nouveau code.

```typescript
@NgModule({
    declarations: [AppComponent, CompteurComponent],
    imports: [BrowserModule, FormsModule],
    providers: [],
    bootstrap: [AppComponent],
})
export class AppModule {}
```

| | **Autonome** (*standalone*) ✅ | **`NgModule`** *(héritage)* |
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
    saluer() { alert("Salut !"); }
}
```

## 5.2 Liaisons spécialisées

```html
<div [class.actif]="estActif()" [class]="{ rouge: erreur(), gras: important() }"></div>
<div [style.width.px]="largeur()" [style.color]="couleur()"></div>
<td [attr.colspan]="colonnes()" [attr.aria-label]="libelle()"></td>
<input #champ (keyup.enter)="valider(champ.value)" />                <!-- variable de référence + filtre de touche -->
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
@let utilisateur = utilisateur$ | async;
<p>Total : {{ total | currency }}</p>
```

### Vues différées : `@defer`

Chargement **paresseux** d'un morceau de gabarit : voir [section 19](#19-chargement-paresseux-et-vues-différées).

### Tableau de correspondance (héritage)

| Ancienne syntaxe | Nouvelle syntaxe |
| --- | --- |
| `*ngIf="x; else autre"` | `@if (x) { … } @else { … }` |
| `*ngFor="let i of liste; trackBy: fn"` | `@for (i of liste; track i.id) { … }` |
| `[ngSwitch]` / `*ngSwitchCase` | `@switch` / `@case` |

> 📌 `NgIf`, `NgFor` et `NgSwitch` sont **dépréciés** depuis la version 20. Migration automatique : `ng generate @angular/core:control-flow`.

## 5.4 Expressions de gabarit

Les expressions sont du TypeScript **simplifié** : pas d'affectation (hors événements), pas de `new`, pas d'opérateurs `++` / `--`, pas d'accès à `window`.

```html
{{ prix() * 1.2 | currency }}
{{ utilisateur()?.adresse?.ville ?? "Inconnue" }}
{{ liste().length > 0 ? "Oui" : "Non" }}
<button (click)="a = 1; b = 2">Plusieurs instructions</button>
```

## 5.5 Variables de référence de gabarit

```html
<input #nom />
<button (click)="envoyer(nom.value)">Envoyer</button>

<app-compteur #c />
<button (click)="c.incrementer()">Depuis le parent</button>
```

## 5.6 Gabarits réutilisables : `ng-template`, `ng-container`

```html
<ng-template #chargement><p>Chargement…</p></ng-template>

@if (donnees(); as d) {
    <app-liste [donnees]="d" />
} @else {
    <ng-container *ngTemplateOutlet="chargement" />
}

<ng-container>               <!-- regroupe sans ajouter d'élément au DOM -->
    @for (x of liste(); track x) { <span>{{ x }}</span> }
</ng-container>
```

## 5.7 Liaison bidirectionnelle avec les signaux

```typescript
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

```html
<!-- Préférez les liaisons natives de classes et de styles -->
<div [class.actif]="actif()" [class]="{ rouge: erreur(), gras: important() }"></div>
<div [style.background-color]="couleur()" [style.width.px]="largeur()"></div>

<!-- NgClass / NgStyle restent disponibles (import depuis @angular/common) -->
<div [ngClass]="{ actif: actif() }" [ngStyle]="{ color: couleur() }"></div>
```

> ✅ Depuis les versions récentes, `[class]` et `[style]` acceptent objets et tableaux : `NgClass` et `NgStyle` ne sont plus nécessaires.

## 6.3 Créer une directive d'attribut

```bash
ng generate directive surbrillance
```

```typescript
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

    protected appliquer(c: string) { this.element.nativeElement.style.backgroundColor = c; }
}
```

```html
<p appSurbrillance="lightblue">Survolez-moi</p>
```

### Directives composées : `hostDirectives`

```typescript
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
import { DatePipe, CurrencyPipe, AsyncPipe } from "@angular/common";

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
import { Pipe, PipeTransform } from "@angular/core";

@Pipe({ name: "tronquer" })            // pur par défaut
export class Tronquer implements PipeTransform {
    transform(texte: string, longueur = 20, suffixe = "…"): string {
        return texte.length > longueur ? texte.slice(0, longueur) + suffixe : texte;
    }
}
```

```html
{{ description | tronquer: 50 }}
```

## 6.7 Tubes purs et impurs

| | **Pur** (défaut) | **Impur** (`pure: false`) |
| --- | --- | --- |
| Exécuté | Seulement si l'**entrée change** (référence) | À **chaque** détection de changements |
| Performance | ✅ Excellente | ❌ Coûteux |
| Usage | Presque toujours | Rare (ex. `async`) |

> 💡 Avec les signaux, un **`computed()`** est souvent plus simple qu'un tube pour dériver une valeur.

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

> 📌 La v22 introduit un décorateur raccourci **`@Service()`** pour les services à portée racine (équivalent de `@Injectable({ providedIn: 'root' })`) : vérifiez-le sur [angular.dev](https://angular.dev).

### Injection avec `inject()` *(à jour)*

```typescript
import { Component, inject } from "@angular/core";

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

> ✅ `inject()` fonctionne dans un **contexte d'injection** (constructeur, initialisation de champ, fonction `provide`/garde/intercepteur). Il facilite l'héritage et la composition.

## 7.3 Portées des fournisseurs

| Où fournir | Portée / durée de vie |
| --- | --- |
| `@Injectable({ providedIn: "root" })` | **Toute l'application**, instance unique (✅ par défaut) |
| `providers` de `app.config.ts` | Toute l'application (utile pour la configuration) |
| `providers` d'une **route** | Toutes les routes enfants (injecteur d'environnement) |
| `providers` d'un **composant** | **Une instance par composant** (et ses enfants) |
| `viewProviders` | Vue du composant seulement (pas le contenu projeté) |

```typescript
@Component({
    selector: "app-formulaire",
    providers: [BrouillonService],           // nouvelle instance pour chaque <app-formulaire>
    template: `…`,
})
export class Formulaire {}
```

## 7.4 Jetons d'injection et configuration

```typescript
import { InjectionToken, inject } from "@angular/core";

export interface ConfigApp { urlApi: string; delaiMs: number }
export const CONFIG_APP = new InjectionToken<ConfigApp>("CONFIG_APP", {
    providedIn: "root",
    factory: () => ({ urlApi: "/api", delaiMs: 5000 }),         // valeur par défaut
});

// Remplacer la valeur
providers: [{ provide: CONFIG_APP, useValue: { urlApi: "https://api.exemple.com", delaiMs: 8000 } }]

const config = inject(CONFIG_APP);
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
const optionnel = inject(Journal, { optional: true });      // null si absent
const local = inject(Service, { self: true });               // uniquement l'injecteur local
const parent = inject(Service, { skipSelf: true });          // injecteur parent
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
import { provideAppInitializer, inject } from "@angular/core";

providers: [
    provideAppInitializer(() => inject(ConfigService).charger()),     // exécutée avant le démarrage (peut renvoyer une promesse)
]
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
import { signal, computed, effect } from "@angular/core";

const compteur = signal(0);                    // WritableSignal<number>

compteur();                                    // lecture : 0 (on « appelle » le signal)
compteur.set(5);                               // remplacement
compteur.update((v) => v + 1);                 // mise à jour à partir de l'ancienne valeur

const double = computed(() => compteur() * 2); // valeur dérivée : lecture seule, MÉMOÏSÉE, paresseuse
double();                                      // 12

effect(() => console.log(`Compteur : ${compteur()}`));    // effet de bord, relancé quand une dépendance change
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

> ✅ Les API de signaux de base (`signal`, `computed`, `effect`, `linkedSignal`, `input`, `model`, `viewChild`) sont **stables** depuis la v20 ; `resource`, `rxResource` et `httpResource` le sont depuis la **v22**.

## 8.2 Signaux d'objets et de tableaux

Les signaux détectent le changement par **référence** : mettez à jour de façon **immuable**.

```typescript
const utilisateur = signal({ nom: "Alice", age: 30 });
utilisateur.update((u) => ({ ...u, age: u.age + 1 }));     // ✅ nouvel objet

const liste = signal<string[]>([]);
liste.update((l) => [...l, "nouveau"]);                    // ✅ nouveau tableau
// liste().push("x");                                       // ❌ aucune notification
```

## 8.3 `computed` : dérivation

```typescript
const prix = signal(100);
const quantite = signal(2);
const total = computed(() => prix() * quantite());          // se met à jour automatiquement

@Component({ template: `<p>Total : {{ total() }}</p>` })
class Panier { prix = prix; quantite = quantite; total = total; }
```

- **Paresseux** : calculé seulement quand on le lit.
- **Mémoïsé** : recalculé seulement si une dépendance change.
- **Pas d'effets de bord** ni d'écriture de signaux à l'intérieur.

## 8.4 `effect` : effets de bord

```typescript
@Component({ /* … */ })
export class Preferences {
    theme = signal<"clair" | "sombre">("clair");

    constructor() {
        effect(() => {
            document.documentElement.dataset["theme"] = this.theme();       // synchroniser avec le DOM
            localStorage.setItem("theme", this.theme());
        });
    }
}
```

> ⚠️ **N'utilisez pas `effect` pour propager un état vers un autre signal** (préférez `computed` ou `linkedSignal`). Les effets sont réservés aux **synchronisations avec l'extérieur** (stockage, journaux, bibliothèques non Angular, DOM).
> Pour des effets liés au **rendu**, utilisez `afterRenderEffect()` / `afterNextRender()`.

## 8.5 `linkedSignal` : état dérivé modifiable

```typescript
const options = signal(["S", "M", "L"]);
const selection = linkedSignal(() => options()[0]);        // se réinitialise quand `options` change
selection.set("L");                                          // mais reste modifiable
```

Version avancée avec mémoire de l'ancienne valeur :

```typescript
const selection = linkedSignal<string[], string>({
    source: options,
    computation: (nouvelles, precedent) => (precedent && nouvelles.includes(precedent.value) ? precedent.value : nouvelles[0]),
});
```

## 8.6 `resource` : données asynchrones *(stable en v22)*

Une **resource** relie un **signal de paramètres** à un **chargeur asynchrone** et expose `value()`, `isLoading()`, `error()`, `status()`.

```typescript
import { resource, signal } from "@angular/core";

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

> ℹ️ Dans les versions 19–20, l'option s'appelait **`request`** ; elle est devenue **`params`**.

### `httpResource` : la version « HttpClient »

```typescript
import { httpResource } from "@angular/common/http";

utilisateurs = httpResource<Utilisateur[]>(() => `/api/users?page=${this.page()}`);     // passe par HttpClient (intercepteurs inclus)
// utilisateurs.value(), .isLoading(), .error(), .hasValue(), .reload()
```

### `rxResource` : à partir d'un Observable

```typescript
import { rxResource } from "@angular/core/rxjs-interop";
produits = rxResource({ params: () => this.categorie(), stream: ({ params }) => this.service.lister(params) });
```

> 💡 `resource` est conçu pour les **lectures** (chargement de données) ; les **écritures** (POST, PUT, DELETE) restent des appels `HttpClient` explicites.

## 8.7 Interopérabilité RxJS ⇄ signaux

```typescript
import { toSignal, toObservable, takeUntilDestroyed } from "@angular/core/rxjs-interop";

// Observable → signal (abonnement et désabonnement automatiques)
const utilisateurs = toSignal(this.http.get<Utilisateur[]>("/api/users"), { initialValue: [] });

// Signal → Observable (pour appliquer des opérateurs RxJS)
const resultats$ = toObservable(this.termeRecherche).pipe(
    debounceTime(300),
    switchMap((t) => this.http.get<string[]>(`/api/recherche?q=${t}`)),
);
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

export const routes: Routes = [
    { path: "", component: Accueil, title: "Accueil" },
    { path: "produits", loadComponent: () => import("./produits/liste").then((m) => m.Liste), title: "Produits" },
    { path: "produits/:id", loadComponent: () => import("./produits/detail").then((m) => m.Detail) },
    { path: "admin", loadChildren: () => import("./admin/admin.routes").then((m) => m.ADMIN_ROUTES), canMatch: [adminGuard] },
    { path: "ancienne-page", redirectTo: "produits", pathMatch: "full" },
    { path: "**", loadComponent: () => import("./introuvable/introuvable").then((m) => m.Introuvable) },     // joker : 404
];
```

```typescript
// app.config.ts
import { provideRouter, withComponentInputBinding, withViewTransitions, withPreloading, PreloadAllModules } from "@angular/router";

providers: [
    provideRouter(routes, withComponentInputBinding(), withViewTransitions(), withPreloading(PreloadAllModules)),
]
```

```html
<!-- app.html -->
<nav>
    <a routerLink="/" routerLinkActive="actif" [routerLinkActiveOptions]="{ exact: true }">Accueil</a>
    <a [routerLink]="['/produits', 42]" [queryParams]="{ tri: 'prix' }">Produit 42</a>
</nav>
<router-outlet />
```

```typescript
@Component({ imports: [RouterOutlet, RouterLink, RouterLinkActive], /* … */ })
```

## 9.3 Paramètres de route *(à jour)*

Avec **`withComponentInputBinding()`**, les paramètres de chemin, de requête et les données de route sont **liés directement à des `input()`** :

```typescript
@Component({ selector: "app-detail", template: `<h1>Produit {{ id() }} — tri : {{ tri() }}</h1>` })
export class Detail {
    id = input.required<string>();            // /produits/:id
    tri = input<string>();                    // ?tri=prix
}
```

Forme classique (toujours valide) :

```typescript
private readonly route = inject(ActivatedRoute);
id$ = this.route.paramMap.pipe(map((p) => p.get("id")));
const id = toSignal(this.route.paramMap.pipe(map((p) => p.get("id"))));
```

## 9.4 Navigation par programme

```typescript
private readonly router = inject(Router);

this.router.navigate(["/produits", id], { queryParams: { tri: "prix" } });
this.router.navigateByUrl("/connexion");
this.router.navigate(["../"], { relativeTo: this.route });       // route relative
```

## 9.5 Routes imbriquées (enfants)

```typescript
{
    path: "compte",
    component: CompteLayout,                       // contient <router-outlet />
    children: [
        { path: "", redirectTo: "profil", pathMatch: "full" },
        { path: "profil", component: Profil },
        { path: "securite", component: Securite },
    ],
}
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
import { CanActivateFn, Router, CanDeactivateFn } from "@angular/router";
import { inject } from "@angular/core";

export const authGuard: CanActivateFn = (route, state) => {
    const auth = inject(AuthService);
    const router = inject(Router);
    return auth.estConnecte() ? true : router.createUrlTree(["/connexion"], { queryParams: { retour: state.url } });
};

export const roleGuard = (role: string): CanActivateFn => () => inject(AuthService).aLeRole(role) || inject(Router).createUrlTree(["/interdit"]);

export const quitterGuard: CanDeactivateFn<{ aDesModifications: () => boolean }> = (composant) =>
    !composant.aDesModifications() || confirm("Quitter sans enregistrer ?");

// Utilisation
{ path: "admin", canActivate: [authGuard, roleGuard("admin")], loadChildren: () => … },
{ path: "edition", component: Edition, canDeactivate: [quitterGuard] },
```

> ⚠️ **Une garde ne remplace pas la sécurité côté serveur** : elle améliore l'expérience, mais le serveur doit refuser les accès non autorisés (voir sections 26 et 27).

## 9.7 Résolveurs : données avant la navigation

```typescript
export const produitResolver: ResolveFn<Produit> = (route) => inject(ProduitService).trouver(route.paramMap.get("id")!);

{ path: "produits/:id", component: Detail, resolve: { produit: produitResolver } }

// Dans le composant (avec withComponentInputBinding)
produit = input.required<Produit>();
```

## 9.8 Chargement paresseux et préchargement

```typescript
{ path: "admin", loadChildren: () => import("./admin/admin.routes").then((m) => m.ADMIN_ROUTES) }
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
    envoyer(valeurs: unknown) { console.log(valeurs); }
}
```

## 10.3 Formulaires réactifs (typés)

```typescript
import { ReactiveFormsModule, NonNullableFormBuilder, Validators, FormArray } from "@angular/forms";

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
this.formulaire.patchValue({ nom: "Alice" });             // mise à jour partielle
this.formulaire.setValue({ /* tout */ });                  // mise à jour complète
this.formulaire.reset();
this.formulaire.valueChanges.pipe(debounceTime(300)).subscribe(console.log);
this.nom.statusChanges; this.nom.disable(); this.nom.setErrors({ personnalise: true });
```

États : `valid`, `invalid`, `pending`, `touched`, `dirty`, `pristine`.

## 10.4 Validation personnalisée

```typescript
import { AbstractControl, ValidationErrors, ValidatorFn, AsyncValidatorFn } from "@angular/forms";

// Validateur synchrone (fabrique)
export const interdire = (mot: string): ValidatorFn => (c: AbstractControl): ValidationErrors | null =>
    String(c.value).toLowerCase().includes(mot) ? { interdit: { mot } } : null;

// Validateur de groupe : confirmation de mot de passe
export const motsDePasseIdentiques: ValidatorFn = (g) =>
    g.get("motDePasse")?.value === g.get("confirmation")?.value ? null : { nonIdentiques: true };

// Validateur asynchrone (ex. e-mail déjà utilisé)
export const emailLibre = (service: UtilisateurService): AsyncValidatorFn => (c) =>
    service.existe(c.value).pipe(map((existe) => (existe ? { emailPris: true } : null)));

this.fb.group({ /* … */ }, { validators: motsDePasseIdentiques });
```

## 10.5 Tableaux dynamiques : `FormArray`

```typescript
formulaire = this.fb.group({ competences: this.fb.array([this.fb.control("")]) });
get competences() { return this.formulaire.controls.competences; }
ajouter() { this.competences.push(this.fb.control("")); }
supprimer(i: number) { this.competences.removeAt(i); }
```

```html
<div formArrayName="competences">
    @for (c of competences.controls; track $index) {
        <input [formControlName]="$index" /> <button type="button" (click)="supprimer($index)">✕</button>
    }
</div>
```

## 10.6 Composants de formulaire personnalisés

Pour qu'un composant fonctionne avec `formControlName` / `ngModel`, il implémente **`ControlValueAccessor`** et se déclare via `NG_VALUE_ACCESSOR`.

## 10.7 Signal Forms *(stables en Angular 22)*

Les **Signal Forms** (paquet `@angular/forms/signals`) construisent le formulaire **autour d'un signal** : le modèle est la **source de vérité**, les validateurs sont décrits dans un **schéma**, et l'état du formulaire (`valid`, `touched`, `errors`…) est lui-même fait de signaux.

```typescript
import { Component, signal } from "@angular/core";
import { form, required, email, minLength } from "@angular/forms/signals";

@Component({ /* … imports de la directive de champ fournie par @angular/forms/signals … */ })
export class Inscription {
    modele = signal({ nom: "", email: "" });

    formulaire = form(this.modele, (chemin) => {
        required(chemin.nom);
        minLength(chemin.nom, 2);
        required(chemin.email);
        email(chemin.email);
    });
}
```

> ⚠️ L'API a **évolué pendant la phase expérimentale** (versions 21.x) : consultez le guide « Signal Forms » sur [angular.dev](https://angular.dev) pour la syntaxe exacte de liaison des champs dans le gabarit et pour les migrations. Les formulaires réactifs et basés sur le gabarit **continuent d'être pris en charge** et peuvent coexister avec les Signal Forms.

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

# 🟡 Avancé

---

# 11. Client HTTP

## 11.1 Configurer `HttpClient` *(à jour)*

Plus de `HttpClientModule` : on utilise des **fonctions de configuration** dans `app.config.ts`.

```typescript
import { provideHttpClient, withFetch, withInterceptors, withXsrfConfiguration } from "@angular/common/http";

providers: [
    provideHttpClient(
        withFetch(),                                    // utilise l'API fetch (recommandé, requis pour SSR efficace)
        withInterceptors([authInterceptor, erreurInterceptor]),
        withXsrfConfiguration({ cookieName: "XSRF-TOKEN", headerName: "X-XSRF-TOKEN" }),
    ),
]
```

> ℹ️ Les anciens intercepteurs sous forme de **classes** (`HttpInterceptor` + `HTTP_INTERCEPTORS`) nécessitent `withInterceptorsFromDi()` ; préférez les **intercepteurs fonctionnels**.

## 11.2 Un service d'accès aux données typé

```typescript
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

> ⚠️ Un `Observable` HTTP est **froid** : **rien ne part tant qu'on ne s'abonne pas** (`subscribe`, tube `async`, `toSignal`), et chaque abonnement relance la requête.

## 11.3 Utiliser les données

```typescript
// Avec un signal (simple)
utilisateurs = toSignal(inject(UtilisateurService).lister(), { initialValue: [] });

// Avec httpResource (lecture réactive, sans RxJS)
utilisateurs = httpResource<Utilisateur[]>(() => `/api/utilisateurs?page=${this.page()}`);

// Avec le tube async
utilisateurs$ = this.service.lister();
// @if (utilisateurs$ | async; as liste) { … }
```

## 11.4 Intercepteurs fonctionnels

```typescript
import { HttpInterceptorFn, HttpErrorResponse } from "@angular/common/http";
import { catchError, throwError } from "rxjs";

export const authInterceptor: HttpInterceptorFn = (req, next) => {
    const jeton = inject(AuthService).jeton();
    const requete = jeton && req.url.startsWith("/api") ? req.clone({ setHeaders: { Authorization: `Bearer ${jeton}` } }) : req;
    return next(requete);
};

export const erreurInterceptor: HttpInterceptorFn = (req, next) =>
    next(req).pipe(
        catchError((erreur: HttpErrorResponse) => {
            if (erreur.status === 401) inject(Router).navigateByUrl("/connexion");
            return throwError(() => erreur);
        }),
    );

export const journalInterceptor: HttpInterceptorFn = (req, next) => {
    const debut = performance.now();
    return next(req).pipe(tap({ finalize: () => console.log(`${req.method} ${req.url} : ${(performance.now() - debut).toFixed(0)} ms`) }));
};
```

Usages : **jeton d'authentification**, **gestion centralisée des erreurs**, **indicateur de chargement**, **cache**, **journalisation**, ajout d'en-têtes (langue, version d'API).

## 11.5 Gestion des erreurs

```typescript
this.service.lister().pipe(
    retry({ count: 3, delay: (erreur, essai) => timer(500 * 2 ** essai) }),     // nouvelle tentative avec attente exponentielle
    catchError((erreur: HttpErrorResponse) => {
        if (erreur.status === 0) console.error("Réseau indisponible");          // erreur côté client / réseau
        else console.error(`Serveur : ${erreur.status}`, erreur.error);
        return of([]);                                                           // valeur de repli
    }),
);
```

## 11.6 Progression, annulation et fichiers

```typescript
this.http.post("/api/upload", formData, { reportProgress: true, observe: "events" }).subscribe((evenement) => {
    if (evenement.type === HttpEventType.UploadProgress && evenement.total) {
        this.progression.set(Math.round((100 * evenement.loaded) / evenement.total));
    }
});
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

```json
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
import { Observable, of, from, interval, fromEvent, timer } from "rxjs";

const nombres$ = of(1, 2, 3);                            // convention : suffixe `$`
const tic$ = interval(1000);
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
```

## 12.2 Opérateurs essentiels

> 📌 Depuis RxJS 7.2, **tous les opérateurs s'importent depuis `"rxjs"`** (et non plus `"rxjs/operators"`).

```typescript
import { map, filter, tap, debounceTime, distinctUntilChanged, switchMap, mergeMap, concatMap, exhaustMap,
         catchError, retry, take, takeUntil, startWith, combineLatest, forkJoin, shareReplay, finalize } from "rxjs";
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
@Component({
    selector: "app-recherche",
    imports: [ReactiveFormsModule],
    template: `
        <input [formControl]="terme" placeholder="Rechercher…" />
        @for (r of resultats(); track r) { <p>{{ r }}</p> }
    `,
})
export class Recherche {
    private readonly http = inject(HttpClient);
    terme = new FormControl("", { nonNullable: true });

    resultats = toSignal(
        this.terme.valueChanges.pipe(
            debounceTime(300),                              // attendre la fin de la saisie
            distinctUntilChanged(),
            filter((t) => t.length >= 2),
            switchMap((t) => this.http.get<string[]>(`/api/recherche?q=${t}`).pipe(catchError(() => of([])))),
        ),
        { initialValue: [] as string[] },
    );
}
```

## 12.3 Combiner des flux

```typescript
forkJoin({ utilisateur: this.http.get<U>("/api/me"), commandes: this.http.get<C[]>("/api/commandes") })
    .subscribe(({ utilisateur, commandes }) => { /* attendre que tout soit terminé */ });

combineLatest([filtre$, tri$]).pipe(map(([f, t]) => ({ f, t })));        // dernière valeur de chaque flux
```

## 12.4 Subjects

| Type | Comportement |
| --- | --- |
| `Subject<T>` | Diffuse les nouvelles valeurs aux abonnés actuels |
| `BehaviorSubject<T>(initial)` | Garde et rejoue la **dernière valeur** (état) |
| `ReplaySubject<T>(n)` | Rejoue les `n` dernières valeurs |
| `AsyncSubject<T>` | Émet la dernière valeur à la **complétion** |

```typescript
@Injectable({ providedIn: "root" })
export class PanierService {
    private readonly articles = new BehaviorSubject<Article[]>([]);
    readonly articles$ = this.articles.asObservable();                 // ne pas exposer le Subject lui-même
    ajouter(a: Article) { this.articles.next([...this.articles.value, a]); }
}
```

> 💡 Pour un **état local ou de service**, un **signal** est aujourd'hui plus simple qu'un `BehaviorSubject`.

## 12.5 Éviter les fuites mémoire *(à jour)*

Un abonnement actif **après la destruction** du composant provoque des fuites.

| Technique | Quand |
| --- | --- |
| **Tube `async`** / **`toSignal`** | Dans le gabarit : gestion automatique ✅ |
| **`takeUntilDestroyed()`** | Dans un composant / service : `flux$.pipe(takeUntilDestroyed()).subscribe(…)` ✅ |
| `take(1)`, `first()` | Flux qui n'émettent qu'une valeur utile |
| `Subscription.unsubscribe()` dans `ngOnDestroy` | Gestion manuelle (héritage) |

```typescript
export class Surveillance {
    constructor() {
        interval(1000).pipe(takeUntilDestroyed()).subscribe((n) => console.log(n));    // dans le constructeur (contexte d'injection)
    }
    private readonly destroyRef = inject(DestroyRef);
    demarrer() { flux$.pipe(takeUntilDestroyed(this.destroyRef)).subscribe(); }          // ailleurs : fournir le DestroyRef
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
| État **partagé** par quelques composants | **Service** avec signaux (suffisant dans la majorité des cas) ✅ |
| État **complexe**, traçable, partagé par beaucoup de fonctionnalités | **NgRx** (Store ou **SignalStore**) |
| État **serveur** (cache de données) | `resource` / `httpResource`, ou bibliothèques de requêtes |

## 13.2 Service avec signaux (recommandé par défaut)

```typescript
@Injectable({ providedIn: "root" })
export class PanierStore {
    private readonly _articles = signal<Article[]>([]);

    readonly articles = this._articles.asReadonly();
    readonly nombre = computed(() => this._articles().length);
    readonly total = computed(() => this._articles().reduce((s, a) => s + a.prix * a.quantite, 0));

    ajouter(article: Article) {
        this._articles.update((liste) => [...liste, article]);
    }
    retirer(id: number) {
        this._articles.update((liste) => liste.filter((a) => a.id !== id));
    }
    vider() { this._articles.set([]); }
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
import { createActionGroup, props, emptyProps, createFeature, createReducer, on, createSelector } from "@ngrx/store";

export const PanierActions = createActionGroup({
    source: "Panier",
    events: {
        "Ajouter article": props<{ article: Article }>(),
        "Retirer article": props<{ id: number }>(),
        "Vider": emptyProps(),
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
        on(PanierActions.vider, () => initial),
    ),
    extraSelectors: ({ selectArticles }) => ({
        selectTotal: createSelector(selectArticles, (a) => a.reduce((s, x) => s + x.prix, 0)),
    }),
});
```

```typescript
// app.config.ts
providers: [provideStore({ [panierFeature.name]: panierFeature.reducer }), provideEffects(PanierEffects), provideStoreDevtools({ maxAge: 25 })]

// Composant
private readonly store = inject(Store);
total = this.store.selectSignal(panierFeature.selectTotal);                     // sélecteur sous forme de signal
ajouter(a: Article) { this.store.dispatch(PanierActions.ajouterArticle({ article: a })); }
```

### Effets (actions asynchrones)

```typescript
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
import { signalStore, withState, withComputed, withMethods, patchState } from "@ngrx/signals";

export const PanierStore = signalStore(
    { providedIn: "root" },
    withState({ articles: [] as Article[], chargement: false }),
    withComputed(({ articles }) => ({
        total: computed(() => articles().reduce((s, a) => s + a.prix, 0)),
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

## 13.5 Autres solutions

| Outil | Remarques |
| --- | --- |
| **NgRx Store** | Standard des grandes applications, très structuré, plus de code |
| **NgRx SignalStore** | Moderne, léger, API simple |
| **NGXS** | Approche à décorateurs, moins de code répétitif |
| **Akita** | ⚠️ **Plus maintenu** : à éviter pour de nouveaux projets |
| **Elf** | Bibliothèque réactive légère |
| **Service + signaux** | **Suffisant pour la plupart des applications** |

## 13.6 Comparaison

| Critère | Service + signaux | NgRx Store | NgRx SignalStore |
| --- | --- | --- | --- |
| Complexité | ⭐ | ⭐⭐⭐ | ⭐⭐ |
| Traçabilité (devtools) | ❌ | ✅ | ✅ (avec extensions) |
| Quantité de code | Faible | Élevée | Moyenne |
| Équipes nombreuses / règles strictes | Moyen | ✅ | ✅ |

> ✅ **Commencez simple** (service + signaux). N'ajoutez NgRx que si la complexité de l'état l'exige.

---

# 14. Animations

## 14.1 Animations CSS natives *(à jour)*

Depuis la **version 20.2**, Angular propose des **liaisons natives** d'entrée / sortie d'éléments basées sur le **CSS** : `animate.enter` et `animate.leave`. Le paquet **`@angular/animations`** (DSL `trigger`, `state`, `transition`) est **déprécié** au profit de cette approche.

```typescript
@Component({
    selector: "app-notification",
    template: `
        @if (visible()) {
            <div class="notif" animate.enter="entree" animate.leave="sortie">Enregistré !</div>
        }
        <button (click)="visible.update(v => !v)">Basculer</button>
    `,
    styles: `
        .notif { padding: 1rem; background: #e6ffed; }
        .entree { animation: apparition 300ms ease-out; }
        .sortie { animation: disparition 300ms ease-in; }
        @keyframes apparition { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: none; } }
        @keyframes disparition { to { opacity: 0; transform: translateY(-10px); } }
    `,
})
export class Notification { visible = signal(true); }
```

Autres outils CSS : **transitions** (`transition: all .3s`), **`@keyframes`**, **View Transitions** du routeur (`withViewTransitions()`), `prefers-reduced-motion` (accessibilité).

## 14.2 `@angular/animations` *(héritage)*

Encore présent dans de nombreux projets (et dans Angular Material jusqu'à migration) :

```typescript
import { trigger, state, style, transition, animate, query, stagger, keyframes } from "@angular/animations";
import { provideAnimationsAsync } from "@angular/platform-browser/animations/async";

// app.config.ts : providers: [provideAnimationsAsync()]

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
    template: `<div [@ouverture]="ouvert() ? 'ouvert' : 'ferme'">Contenu</div>`,
})
export class Boite { ouvert = signal(false); }
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
// Composant autonome de bibliothèque
@Component({ selector: "kit-bouton", template: `<button><ng-content /></button>`, changeDetection: ChangeDetectionStrategy.OnPush })
export class KitBouton {}
```

```bash
ng build ui-kit                                  # dist/ui-kit
cd dist/ui-kit && npm publish                    # publier sur npm
```

> 🛠️ En développement, le chemin `@mon-espace/ui-kit` est mappé sur le code source via `paths` dans `tsconfig.json`. Pensez à construire la bibliothèque avant l'application, ou à utiliser `ng build --watch`.

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

# 🧪 Tests

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

> 🔁 Migrer un projet Karma/Jasmine : `ng generate @angular/core:karma-to-vitest` (voir [section 28](#28-migration-et-mises-à-jour)). Karma et Jasmine restent utilisables sur les projets existants.

## 16.2 Tester un composant

```typescript
// compteur.spec.ts
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

    it("affiche le titre transmis en entrée", async () => {
        const fixture = TestBed.createComponent(CarteProduit);
        fixture.componentRef.setInput("nom", "Livre");        // entrées signaux : toujours via setInput()
        await fixture.whenStable();
        expect(fixture.nativeElement.textContent).toContain("Livre");
    });
});
```

> ✅ Avec des composants **zoneless / signaux**, on attend le rendu avec **`await fixture.whenStable()`**. En mode avec Zone.js, `fixture.detectChanges()` reste utilisable.

## 16.3 Tester un service

```typescript
describe("PanierStore", () => {
    let store: PanierStore;
    beforeEach(() => {
        TestBed.configureTestingModule({});
        store = TestBed.inject(PanierStore);
    });

    it("calcule le total", () => {
        store.ajouter({ id: 1, prix: 10, quantite: 2 });
        store.ajouter({ id: 2, prix: 5, quantite: 1 });
        expect(store.total()).toBe(25);
    });
});
```

## 16.4 Tester les appels HTTP

```typescript
import { provideHttpClient } from "@angular/common/http";
import { provideHttpClientTesting, HttpTestingController } from "@angular/common/http/testing";

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
import { vi } from "vitest";

const serviceFactice = { lister: vi.fn().mockReturnValue(of([{ id: 1, nom: "Alice" }])) };

TestBed.configureTestingModule({
    providers: [{ provide: UtilisateurService, useValue: serviceFactice }],         // remplace le service réel
});

expect(serviceFactice.lister).toHaveBeenCalledTimes(1);
vi.spyOn(console, "error").mockImplementation(() => {});
vi.useFakeTimers(); vi.advanceTimersByTime(1000);
```

Pour des composants avec routeur : `provideRouter([])` et `RouterTestingHarness`.

## 16.6 Harnais de composants (*component harnesses*)

Les **harnais** (CDK) offrent une API **stable** pour interagir avec des composants (Material, Aria, ou vos composants) **sans dépendre du HTML interne**.

```typescript
import { TestbedHarnessEnvironment } from "@angular/cdk/testing/testbed";
import { MatButtonHarness } from "@angular/material/button/testing";

const loader = TestbedHarnessEnvironment.loader(fixture);
const bouton = await loader.getHarness(MatButtonHarness.with({ text: "Envoyer" }));
await bouton.click();
expect(await bouton.isDisabled()).toBe(false);
```

## 16.7 Tester des signaux et effets

```typescript
it("réagit aux signaux", () => {
    TestBed.runInInjectionContext(() => {
        const s = signal(1);
        const d = computed(() => s() * 2);
        s.set(5);
        expect(d()).toBe(10);
    });
});
// Pour les effets : TestBed.tick() (ou await fixture.whenStable()) force leur exécution
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
| **Protractor** | ❌ **Fin de vie (2023)** : à migrer |
| **Playwright** | ✅ **Recommandé** : multi-navigateurs, rapide, attente automatique, traces |
| **Cypress** | ✅ Très répandu, excellente expérience développeur |
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
    // …
    await expect(page.getByText("Identifiants invalides")).toBeVisible();
});
```

```typescript
// playwright.config.ts (extrait)
export default defineConfig({
    testDir: "./e2e",
    use: { baseURL: "http://localhost:4200", trace: "on-first-retry" },
    webServer: { command: "ng serve", url: "http://localhost:4200", reuseExistingServer: !process.env["CI"] },
    projects: [{ name: "chromium", use: { ...devices["Desktop Chrome"] } }, { name: "firefox", use: { ...devices["Desktop Firefox"] } }],
});
```

## 17.3 Exemple avec Cypress

```typescript
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

# ⚡ Performance

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
// app.config.ts
import { provideZonelessChangeDetection } from "@angular/core";
providers: [provideZonelessChangeDetection()]
```

```json
// angular.json : retirer "zone.js" de "polyfills" (et de test)
"polyfills": []
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
@Component({
    selector: "app-liste",
    changeDetection: ChangeDetectionStrategy.OnPush,        // par défaut pour les nouveaux composants depuis la v22
    template: `…`,
})
export class Liste {}
```

> 📌 **v22** : `OnPush` devient la stratégie **par défaut** des nouveaux composants. Pour les composants existants, la migration est automatique et préserve la stratégie `Default` explicite quand elle est nécessaire.

### Avec `OnPush`, mettez à jour de façon **immuable**

```typescript
this.articles = [...this.articles, nouveau];            // ✅ nouvelle référence
// this.articles.push(nouveau);                         // ❌ non détecté (sauf signal)
```

## 18.4 Outils

```typescript
private readonly cdr = inject(ChangeDetectorRef);
this.cdr.markForCheck();          // planifie la vérification du composant (et de ses ancêtres)
this.cdr.detectChanges();         // vérification immédiate (à éviter)
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
export const routes: Routes = [
    { path: "", component: Accueil },                                                            // dans le bundle initial
    { path: "produits", loadComponent: () => import("./produits/liste").then((m) => m.Liste) },   // composant paresseux
    { path: "admin", loadChildren: () => import("./admin/admin.routes").then((m) => m.ADMIN_ROUTES) },   // groupe de routes
];
```

```typescript
// admin/admin.routes.ts
export const ADMIN_ROUTES: Routes = [
    { path: "", component: AdminAccueil, providers: [AdminService] },                // providers propres à ces routes
    { path: "utilisateurs", loadComponent: () => import("./utilisateurs").then((m) => m.Utilisateurs) },
];
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
@Injectable({ providedIn: "root" })
export class PrechargementSelectif implements PreloadingStrategy {
    preload(route: Route, charger: () => Observable<unknown>): Observable<unknown> {
        return route.data?.["precharger"] ? charger() : of(null);
    }
}

provideRouter(routes, withPreloading(PrechargementSelectif));
// { path: "rapports", loadChildren: …, data: { precharger: true } }
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

- **`prefetch`** : télécharge le code à l'avance (sans l'afficher).
- **Hydratation incrémentale** (SSR) : `@defer (hydrate on viewport)` hydrate des zones **plus tard** ([section 22](#22-rendu-côté-serveur-ssr-pré-rendu-et-hydratation)).
- Les composants différés doivent être **autonomes** et **non référencés ailleurs** (sinon ils restent dans le bundle initial).

## 19.5 Chargement conditionnel de code

```typescript
async ouvrirEditeur() {
    const { Editeur } = await import("./editeur");           // import dynamique
    this.conteneur().createComponent(Editeur);
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
| Statut | Rare (tests) | ✅ **Défaut** (`ng serve` et `ng build`) |

L'AOT fonctionne avec le moteur de compilation **Ivy** (par défaut depuis la v9), qui produit du code **ciblé et tree-shakable**.

## 20.2 Vérifications du compilateur

```json
{ "angularCompilerOptions": { "strictTemplates": true, "strictInjectionParameters": true, "strictInputAccessModifiers": true,
                              "extendedDiagnostics": { "checks": { "optionalChainNotNullable": "error" } } } }
```

Le compilateur détecte : propriétés inexistantes dans les gabarits, types incompatibles, `@for` sans `track`, imports inutilisés (diagnostics étendus).

## 20.3 Builder `application` (esbuild + Vite)

```json
// angular.json (extrait)
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
// ✅ Importer précisément
import { debounce } from "lodash-es";            // build ESM, tree-shakable
// ❌ import _ from "lodash";                     // embarque toute la bibliothèque
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

```html
<img ngSrc="/img/hero.jpg" width="1200" height="600" priority alt="Bannière" />
<img ngSrc="/img/produit.jpg" width="400" height="300" alt="Produit" />       <!-- paresseuse par défaut -->
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

# 🌍 Essentiels

---

# 21. Internationalisation (i18n)

## 21.1 Deux approches

| | **i18n intégrée d'Angular** (`$localize`) | **Bibliothèques d'exécution** (Transloco, ngx-translate) |
| --- | --- | --- |
| Traduction | **À la compilation** : un **build par langue** | **À l'exécution** : fichiers JSON, changement de langue à chaud |
| Performance | ✅ Excellente (texte déjà traduit) | Un peu moins (chargement des fichiers) |
| Changer de langue | Rechargement / autre URL | **Instantané** |
| Outils | XLIFF / XMB, extraction par le CLI | JSON, très simple |

## 21.2 i18n intégrée

```bash
ng add @angular/localize                 # active $localize
```

### Marquer les textes

```html
<h1 i18n="@@titreAccueil">Bienvenue sur notre site</h1>                       <!-- id explicite (@@) = stable -->
<p i18n="Message d'accueil|Description pour le traducteur@@intro">Découvrez nos produits.</p>
<img [src]="logo" i18n-alt alt="Logo de l'entreprise" />                      <!-- attribut -->
<span i18n>Mise à jour {{ minutes() }} minutes plus tôt</span>
```

```typescript
const message = $localize`:@@erreurReseau:Impossible de joindre le serveur.`;     // dans le code TypeScript
```

### Pluriels et sélection (format ICU)

```html
<span i18n>
    {nombre, plural, =0 {Aucun message} =1 {Un message} other {{{ nombre }} messages}}
</span>

<span i18n>
    {genre, select, masculin {Il a répondu} feminin {Elle a répondu} other {Réponse reçue}}
</span>
```

### Extraire et traduire

```bash
ng extract-i18n --format xlf2 --output-path src/locale        # génère messages.xlf
# → copier en messages.fr.xlf, messages.en.xlf… et traduire les <target>
```

### Configurer les langues

```json
// angular.json
"i18n": {
    "sourceLocale": "fr",
    "locales": { "en": "src/locale/messages.en.xlf", "es": "src/locale/messages.es.xlf" }
},
"build": { "options": { "localize": true } }          // ou ["en", "es"]
```

```bash
ng build --localize                  # un dossier par langue : dist/mon-app/browser/fr, en, es
ng serve --configuration=en          # servir une langue en développement
```

> Chaque langue est servie sous son propre chemin (`/fr/`, `/en/`) : configurez le serveur ou le CDN en conséquence.

## 21.3 Formats localisés

Les tubes `date`, `currency`, `number`, `percent` utilisent la **locale** active (`LOCALE_ID`) :

```typescript
import { registerLocaleData } from "@angular/common";
import localeFr from "@angular/common/locales/fr";
registerLocaleData(localeFr);

providers: [{ provide: LOCALE_ID, useValue: "fr-FR" }]
```

```html
{{ 1234.5 | currency: "EUR" }}   <!-- 1 234,50 € -->
{{ date | date: "fullDate" }}    <!-- dimanche 11 octobre 2026 -->
```

Pour d'autres besoins : l'API **`Intl`** du navigateur (`Intl.NumberFormat`, `Intl.DateTimeFormat`, `Intl.RelativeTimeFormat`).

## 21.4 Traduction à l'exécution avec Transloco *(ajout)*

```bash
ng add @jsverse/transloco
```

```json
// src/assets/i18n/fr.json
{ "accueil": { "titre": "Bienvenue", "salutation": "Bonjour {{ nom }}" } }
```

```html
<h1>{{ 'accueil.titre' | transloco }}</h1>
<p>{{ 'accueil.salutation' | transloco: { nom: utilisateur() } }}</p>
```

```typescript
private readonly transloco = inject(TranslocoService);
changerLangue(l: string) { this.transloco.setActiveLang(l); }
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

> 📌 **À jour** : **Angular Universal** (`@nguniversal/*`) est **abandonné** ; le SSR est **intégré au CLI** (`@angular/ssr`) et au builder `application`.

## 22.2 Activer le SSR

```bash
ng new mon-app --ssr                  # nouveau projet
ng add @angular/ssr                   # projet existant
```

Ajoute notamment : `server.ts` (serveur Node : Express ou autre), `main.server.ts`, `app.config.server.ts`, `app.routes.server.ts`.

```typescript
// app.config.ts
import { provideClientHydration, withEventReplay, withIncrementalHydration } from "@angular/platform-browser";

providers: [
    provideClientHydration(withEventReplay(), withIncrementalHydration()),
    provideHttpClient(withFetch()),
]
```

```typescript
// app.routes.server.ts : mode de rendu PAR ROUTE
import { RenderMode, ServerRoute } from "@angular/ssr";

export const serverRoutes: ServerRoute[] = [
    { path: "", renderMode: RenderMode.Prerender },                                  // généré au build
    { path: "produits/:id", renderMode: RenderMode.Prerender,
      async getPrerenderParams() { return (await listerIds()).map((id) => ({ id })); } },
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

```html
@defer (hydrate on interaction) {
    <app-commentaires />                     <!-- rendu serveur immédiat, activation au premier clic -->
} @placeholder { <p>Commentaires</p> }
```

## 22.4 Écrire du code compatible SSR

Côté serveur, `window`, `document`, `localStorage`… **n'existent pas**.

```typescript
import { PLATFORM_ID, inject, afterNextRender } from "@angular/core";
import { isPlatformBrowser, DOCUMENT } from "@angular/common";

export class Carte {
    private readonly plateforme = inject(PLATFORM_ID);
    private readonly document = inject(DOCUMENT);               // au lieu de la globale `document`

    constructor() {
        afterNextRender(() => {                                  // exécuté UNIQUEMENT dans le navigateur
            this.initialiserCarteLeaflet();
        });
        if (isPlatformBrowser(this.plateforme)) {
            localStorage.getItem("theme");
        }
    }
}
```

- **Évitez** d'accéder directement à `window` / `document` ; utilisez `afterNextRender`, `DOCUMENT`, `isPlatformBrowser`.
- Les **minuteries** longues (`setInterval`) ne doivent pas bloquer la stabilité de l'application côté serveur.
- Les requêtes `HttpClient` côté serveur sont **mises en cache de transfert** : le navigateur ne les refait pas.
- **Titre et métadonnées** (SEO) : services `Title` et `Meta`.

```typescript
inject(Title).setTitle("Produit — Ma boutique");
inject(Meta).updateTag({ name: "description", content: "Description du produit" });
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
// app.config.ts
import { provideServiceWorker } from "@angular/service-worker";

providers: [
    provideServiceWorker("ngsw-worker.js", {
        enabled: !isDevMode(),                              // actif seulement en production
        registrationStrategy: "registerWhenStable:30000",
    }),
]
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
import { SwUpdate, VersionReadyEvent, SwPush } from "@angular/service-worker";

export class Mises {
    constructor() {
        const maj = inject(SwUpdate);
        maj.versionUpdates.pipe(filter((e): e is VersionReadyEvent => e.type === "VERSION_READY"))
            .subscribe(() => { if (confirm("Nouvelle version disponible. Recharger ?")) document.location.reload(); });
        maj.checkForUpdate();
    }

    async abonnerPush() {
        const abonnement = await inject(SwPush).requestSubscription({ serverPublicKey: CLE_VAPID_PUBLIQUE });
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
import { MatButtonModule } from "@angular/material/button";
import { MatCardModule } from "@angular/material/card";
import { MatFormFieldModule } from "@angular/material/form-field";
import { MatInputModule } from "@angular/material/input";
import { MatTableModule } from "@angular/material/table";
import { MatDialog, MatDialogModule } from "@angular/material/dialog";
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
    private readonly dialogue = inject(MatDialog);
    private readonly barre = inject(MatSnackBar);
    nom = new FormControl("", { nonNullable: true, validators: [Validators.required] });
    colonnes = ["nom"];
    lignes = signal([{ nom: "Alice" }]);

    enregistrer() { this.barre.open("Enregistré !", "OK", { duration: 3000 }); }
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
// Défilement virtuel : seules les lignes visibles sont dans le DOM
```
```html
<cdk-virtual-scroll-viewport itemSize="48" style="height: 400px">
    <div *cdkVirtualFor="let element of elements" class="ligne">{{ element }}</div>
</cdk-virtual-scroll-viewport>
```

```typescript
// Réagir au point de rupture
const mobile = toSignal(inject(BreakpointObserver).observe(Breakpoints.Handset).pipe(map((r) => r.matches)), { initialValue: false });
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

### 4) Styles et scripts globaux

```json
// angular.json
"styles": ["node_modules/bibliotheque/dist/style.css"],
"scripts": ["node_modules/bibliotheque/dist/script.js"]
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
saisie = signal("<img src=x onerror='alert(1)'>");
```

```html
<p>{{ saisie() }}</p>                     <!-- ✅ affiché comme TEXTE, pas exécuté -->
<div [innerHTML]="saisie()"></div>        <!-- ✅ assaini automatiquement (onerror supprimé) -->
```

Angular assainit : **HTML** (`[innerHTML]`), **styles**, **URL** (`href`, `src`) et **URL de ressources** (`<iframe src>`, `<script src>`).

### Contourner l'assainissement : **à n'utiliser qu'en dernier recours**

```typescript
import { DomSanitizer } from "@angular/platform-browser";

private readonly sanitizer = inject(DomSanitizer);
html = this.sanitizer.bypassSecurityTrustHtml(contenuDeConfiance);      // ⚠️ DÉSACTIVE la protection
urlVideo = this.sanitizer.bypassSecurityTrustResourceUrl("https://www.youtube.com/embed/xxxx");
```

> 🚫 **Ne contournez jamais** l'assainissement pour du contenu venant d'un utilisateur ou d'une API non maîtrisée. Si vous devez afficher du HTML riche : assainissez-le avec **DOMPurify** (ou l'**API Sanitizer** du navigateur) **avant**.

### À éviter

```typescript
element.nativeElement.innerHTML = saisie;        // ❌ contourne Angular
document.write(saisie); eval(saisie);             // ❌
// Pas de gabarits construits dynamiquement à partir de données utilisateur
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
provideHttpClient(withXsrfConfiguration({ cookieName: "XSRF-TOKEN", headerName: "X-XSRF-TOKEN" }))
```

Le serveur doit **valider** l'en-tête. Complétez avec des cookies **`SameSite=Lax/Strict`**, **`Secure`**, **`HttpOnly`** (pour les cookies de session).

## 26.5 Stockage des jetons et données sensibles

| Où | Risque |
| --- | --- |
| `localStorage` / `sessionStorage` | **Lisibles par n'importe quel script** (XSS) : à éviter pour les jetons sensibles |
| **Cookie `HttpOnly`** (+ `Secure`, `SameSite`) | ✅ Non lisible par JavaScript : meilleur choix pour les sessions |
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
| **Session par cookie** (`HttpOnly`) | Le serveur émet un cookie de session | ✅ Simple et sûr pour les applications web ; protéger contre le CSRF |
| **JWT** (jeton signé) | Jeton envoyé dans `Authorization: Bearer` | Sans état côté serveur ; **durée de vie courte** + jeton de rafraîchissement |
| **OAuth 2.0 / OpenID Connect** (flux **Authorization Code + PKCE**) | Délégation à un fournisseur d'identité (Keycloak, Auth0, Entra ID, Google…) | ✅ **Recommandé** pour le SSO et les applications publiques |
| **BFF** (*Backend For Frontend*) | Un petit serveur gère les jetons et expose un cookie à l'application | ✅ Le plus sûr : aucun jeton dans le navigateur |

> 🚫 L'ancien flux OAuth « **Implicit** » est **déprécié** : utilisez **Authorization Code avec PKCE**.

## 27.3 Un service d'authentification avec signaux

```typescript
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
// auth.interceptor.ts
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
// Garde et rôles
export const authGuard: CanActivateFn = (_r, state) =>
    inject(AuthService).estConnecte() || inject(Router).createUrlTree(["/connexion"], { queryParams: { retour: state.url } });

export const roleGuard = (role: string): CanMatchFn => () => inject(AuthService).aLeRole(role) || inject(Router).createUrlTree(["/interdit"]);

{ path: "admin", canMatch: [roleGuard("admin")], loadChildren: () => import("./admin/admin.routes").then(m => m.ADMIN_ROUTES) }
```

## 27.5 Autorisation dans l'interface

```html
@if (auth.aLeRole("admin")) {
    <button (click)="supprimer()">Supprimer</button>
}
```

Une directive structurelle ou un composant `*appPermission` peut centraliser cette logique.

> 🚫 **Masquer un bouton n'est pas de la sécurité.** Chaque action doit être **contrôlée côté serveur** (rôles, propriété des ressources). Les gardes de route ne protègent que l'**expérience** utilisateur.

## 27.6 OpenID Connect avec Authorization Code + PKCE

Plutôt que d'écrire le flux vous-même, utilisez une **bibliothèque certifiée** :

```bash
npm install angular-oauth2-oidc          # ou angular-auth-oidc-client, oidc-client-ts
```

```typescript
import { AuthConfig, OAuthService } from "angular-oauth2-oidc";

const configAuth: AuthConfig = {
    issuer: "https://auth.exemple.com/realms/mon-royaume",
    clientId: "mon-app-angular",
    redirectUri: window.location.origin + "/",
    responseType: "code",                                  // Authorization Code + PKCE
    scope: "openid profile email",
    showDebugInformation: false,
};

export class Auth {
    private readonly oauth = inject(OAuthService);
    async initialiser() {
        this.oauth.configure(configAuth);
        await this.oauth.loadDiscoveryDocumentAndTryLogin();
    }
    connecter() { this.oauth.initCodeFlow(); }
    deconnecter() { this.oauth.logOut(); }
    get jeton() { return this.oauth.getAccessToken(); }
}
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

> 💡 `ng update` exécute des **schematics** qui **réécrivent votre code** automatiquement.

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

> ✅ Les anciennes et nouvelles approches **cohabitent** : migrez **progressivement**, par fonctionnalité.

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

> 📌 Les détails exacts de chaque version se trouvent dans l'**annonce officielle** (« Announcing Angular vNN ») sur [blog.angular.dev](https://blog.angular.dev) et dans le journal des modifications GitHub.

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

- 📘 **Documentation officielle** : <https://angular.dev>
- 🎓 **Tutoriels interactifs** (dans le navigateur) : <https://angular.dev/tutorials>
- 🔄 **Guide de mise à jour** : <https://angular.dev/update-guide>
- 📝 **Blog Angular** : <https://blog.angular.dev>
- 📦 **NgRx** : <https://ngrx.io> · **Angular Material** : <https://material.angular.dev> · **Nx** : <https://nx.dev>
- 🔒 **Sécurité Angular** : <https://angular.dev/best-practices/security>
- ♿ **Accessibilité** : <https://angular.dev/best-practices/a11y>

---

<div align="center">

*Bon développement avec Angular ! 🅰️*

</div>
