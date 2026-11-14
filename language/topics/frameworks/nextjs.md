# Cours complet Next.js — Du débutant à l'expert

> **Version de référence : Next.js 16** (publié fin octobre 2025), qui s'appuie sur **React 19.2**. Ce cours est centré sur l'**App Router**. Quand une notion a changé entre Next.js 13, 14, 15 et 16, la différence est signalée par la mention **⚠️ Version**. La documentation officielle (https://nextjs.org/docs) reste la référence en cas de doute, car certaines API évoluent entre versions mineures.

## Comment utiliser ce cours

Chaque chapitre suit la même structure :

1. **Objectifs** : ce que vous saurez faire à la fin.
2. **Notions** : définitions, explications et exemples de code.
3. **Pièges courants** : erreurs fréquentes et leur correction.
4. **À retenir** : synthèse.
5. **Exercices** : mise en pratique.

**Prérequis** : JavaScript moderne (ES2020+, modules, `async/await`, destructuration), bases de React (composants, props, état, hooks `useState`/`useEffect`), HTML/CSS, notions de HTTP (méthodes, codes de statut, en-têtes, cookies). TypeScript est un plus (les exemples sont en TypeScript).

## Table des matières

1. Introduction et installation
2. Structure d'un projet
3. Routing (App Router)
4. Fichiers spéciaux
5. Server Components et Client Components
6. Récupération de données
7. Mise en cache
8. Stratégies de rendu
9. Server Actions et mutations
10. Route Handlers
11. Proxy (ex-Middleware)
12. Navigation
13. Styles
14. Optimisations
15. Métadonnées et SEO
16. Authentification
17. Internationalisation
18. Configuration
19. Variables d'environnement
20. TypeScript
21. Tests
22. Déploiement
23. Pages Router (historique et migration)
24. Bonnes pratiques
25. Aide-mémoire

---

# Chapitre 1 — Introduction et installation

## Objectifs

- Définir Next.js et expliquer les problèmes qu'il résout.
- Distinguer bibliothèque (React) et framework (Next.js).
- Comprendre le cycle de vie d'une requête et les trois « environnements » d'exécution (build, serveur, client).
- Installer et lancer un projet.

## 1.1 Qu'est-ce que Next.js ?

**Next.js** est un **framework full-stack** construit sur **React**. React est une bibliothèque qui sait décrire une interface (composants, état, rendu). Elle ne dit rien sur :

- le **routage** (quelle page pour quelle URL ?),
- le **rendu côté serveur** (comment produire du HTML avant l'arrivée du JavaScript ?),
- la **récupération de données** (où et quand charger les données ?),
- le **découpage du code** (code splitting), le **bundling**, l'**optimisation** des images, polices, scripts,
- le **back-end** (API, authentification, accès base de données),
- le **déploiement**.

Next.js apporte des réponses cohérentes, testées en production, à toutes ces questions. On dit qu'il est **« opinionated »** : il impose des conventions (par exemple, l'organisation des fichiers détermine les URLs) qui réduisent le nombre de décisions à prendre.

### Le problème des Single Page Applications (SPA)

Une SPA React « classique » (créée avec Vite ou l'ancien Create React App) envoie au navigateur un HTML presque vide :

```html
<body>
  <div id="root"></div>
  <script src="/bundle.js"></script>
</body>
```

Le navigateur doit alors : télécharger le bundle JavaScript, l'exécuter, appeler des API pour récupérer les données, puis afficher l'interface. Conséquences :

| Problème | Explication |
|---|---|
| **Affichage tardif** | L'utilisateur voit une page blanche tant que le JS n'est pas chargé et exécuté (mauvais *First Contentful Paint*, *Largest Contentful Paint*). |
| **SEO fragile** | Les robots doivent exécuter du JavaScript pour voir le contenu ; les réseaux sociaux (aperçus de liens) ne le font généralement pas. |
| **Cascades (waterfalls)** | Bundle → composant → requête de données → sous-composant → autre requête… chaque étape attend la précédente. |
| **Bundle volumineux** | Tout le code, y compris la logique qui pourrait rester côté serveur, est envoyé au client. |
| **Secrets impossibles** | Aucune clé d'API ne peut être utilisée côté navigateur sans être exposée. |

Next.js résout ces problèmes en **rendant les composants React sur le serveur**, en envoyant du **HTML déjà complet** et en n'envoyant **que le JavaScript nécessaire** à l'interactivité.

## 1.2 Historique et versions

| Version | Date approx. | Apports majeurs |
|---|---|---|
| 1.0 | 2016 | Rendu serveur React, routage par fichiers (`pages/`) |
| 9 – 12 | 2019–2021 | API Routes, SSG/ISR, `next/image`, Middleware |
| **13** | 2022 | **App Router** (bêta) : layouts imbriqués, Server Components, streaming, Turbopack (alpha) |
| **13.4** | 2023 | App Router déclaré stable |
| **14** | 2023 | **Server Actions** stables, Partial Prerendering (aperçu) |
| **15** | 2024 | React 19, API de requête asynchrones, `fetch` non mis en cache par défaut, `after()` |
| **16** | Oct. 2025 | **Cache Components** (`"use cache"`), **Turbopack par défaut**, `proxy.ts`, React Compiler stable, nouvelles API de cache |

## 1.3 Fonctionnalités clés

1. **Routage par système de fichiers** (App Router et Pages Router).
2. **React Server Components (RSC)** : composants exécutés uniquement côté serveur.
3. **Rendu hybride** : chaque route (voire chaque composant avec Cache Components) peut être statique ou dynamique.
4. **Streaming** : envoi progressif de l'interface avec `Suspense`.
5. **Server Actions / Server Functions** : fonctions serveur appelables depuis l'interface, pour les mutations.
6. **Route Handlers** : endpoints HTTP personnalisés.
7. **Optimisations intégrées** : `next/image`, `next/font`, `next/script`, prefetching des liens.
8. **Proxy** (anciennement Middleware) : interception des requêtes.
9. **Bundlers** : Turbopack (par défaut depuis Next.js 16) ou Webpack.
10. **TypeScript** et **ESLint** supportés.
11. **Variables d'environnement**, **i18n**, **métadonnées/SEO**, **images OpenGraph**, etc.

## 1.4 Les trois environnements d'exécution

Comprendre où le code s'exécute est **la** clé de Next.js. Un même fichier peut s'exécuter dans plusieurs environnements.

| Environnement | Quand ? | Où ? | Exemples |
|---|---|---|---|
| **Build time** (compilation) | Lors de `next build` | Machine de build / CI | Génération des pages statiques, `generateStaticParams` |
| **Serveur (runtime)** | À chaque requête (ou à la revalidation) | Serveur Node.js, Edge, serverless | Server Components dynamiques, Route Handlers, Server Actions, Proxy |
| **Client** | Dans le navigateur | Navigateur de l'utilisateur | Client Components : `useState`, événements, `window` |

### Cycle de vie simplifié d'une requête (App Router)

1. Le navigateur demande `GET /blog/mon-article`.
2. (Optionnel) Le **Proxy** intercepte la requête : redirection, réécriture, en-têtes.
3. Next.js détermine la **route** correspondante dans `app/`.
4. Les **Server Components** s'exécutent, récupèrent leurs données et produisent un **payload RSC** (une description sérialisée de l'arbre React).
5. Next.js génère le **HTML** à partir de ce payload et l'envoie, éventuellement par morceaux (**streaming**).
6. Le navigateur affiche le HTML immédiatement (la page est visible).
7. Le JavaScript des **Client Components** est téléchargé, puis **hydraté** : React « attache » les gestionnaires d'événements au HTML existant, rendant la page interactive.
8. Les navigations suivantes se font **côté client** : seul le payload RSC des segments modifiés est demandé au serveur.

> **Hydratation** : processus par lequel React rend interactif un HTML déjà produit par le serveur, en associant l'arbre de composants au DOM existant. Si le HTML serveur et le premier rendu client diffèrent, on obtient une *erreur d'hydratation* (hydration mismatch).

## 1.4 bis Rappel : nouveautés de React 19 utiles à Next.js

Next.js 15/16 s'appuie sur React 19.x. À connaître :

- **Actions** : fonctions asynchrones passées à `<form action={...}>` ou déclenchées dans une transition.
- **`useActionState`**, **`useFormStatus`**, **`useOptimistic`**.
- **`use(promise)`** / **`use(context)`** : lit une promesse ou un contexte (peut être appelé conditionnellement).
- **`ref` comme prop** dans les composants fonction (plus besoin de `forwardRef`).
- **Métadonnées natives** : `<title>`, `<meta>`, `<link>` rendus depuis n'importe quel composant.
- **React 19.2** : `<Activity>`, `useEffectEvent`, View Transitions.
- **React Compiler** (1.0) : mémoïsation automatique, activable dans Next.js 16.

## 1.5 Prérequis système (⚠️ Version)

- **Node.js** : version 20.9 ou plus récente (Next.js 16 ; Node 18 n'est plus supporté).
- **TypeScript** (si utilisé) : 5.1 ou plus.
- Navigateurs ciblés : navigateurs modernes récents (Chrome, Edge, Firefox, Safari).
- Gestionnaire de paquets : npm, pnpm, yarn ou bun.

## 1.6 Création d'un projet

```bash
npx create-next-app@latest mon-app
```

L'assistant pose des questions (les valeurs par défaut suffisent pour débuter) :

| Question | Signification |
|---|---|
| TypeScript ? | Génère `tsconfig.json` et des fichiers `.tsx` |
| Linter ? | ESLint (ou Biome selon les options) |
| React Compiler ? | Active la mémoïsation automatique |
| Tailwind CSS ? | Installe et configure Tailwind |
| Dossier `src/` ? | Place le code dans `src/` |
| App Router ? | Recommandé : oui |
| Alias d'import (`@/*`) ? | Permet `import x from "@/lib/x"` |

Lancement :

```bash
cd mon-app
npm run dev      # serveur de développement sur http://localhost:3000
```

### Scripts de `package.json`

```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint"
  }
}
```

| Commande | Rôle |
|---|---|
| `next dev` | Serveur de développement avec **Fast Refresh** (rechargement à chaud en conservant l'état React) |
| `next build` | Compilation de production : optimisation, génération statique, analyse des routes |
| `next start` | Démarre le serveur de production (après `build`) |
| `next info` | Affiche des informations de diagnostic (versions, OS) |
| `next typegen` | Génère les types de routes (voir chapitre 20) |

> ⚠️ **Version** : `next lint` a été retiré dans Next.js 16 ; on appelle ESLint directement (`eslint`). De plus, `next build` n'exécute plus le lint automatiquement.

### Turbopack et Webpack (⚠️ Version)

- **Turbopack** est un bundler écrit en Rust, **par défaut** pour `next dev` et `next build` depuis Next.js 16.
- Pour utiliser Webpack : `next dev --webpack` / `next build --webpack`.
- Turbopack propose un **cache sur système de fichiers** (en bêta), qui conserve les artefacts compilés entre deux démarrages.
- Certains loaders Webpack spécifiques peuvent ne pas être compatibles : voir la table de compatibilité de la documentation.

## 1.7 Ce que fait `next build`

À la fin d'un build, Next.js affiche un tableau des routes avec leur mode de rendu (symboles tels que ○ statique, ● SSG avec `generateStaticParams`, ƒ dynamique, ◐ partiellement pré-rendu selon la version). Lire ce tableau permet de **vérifier que vos routes sont bien statiques ou dynamiques comme prévu**.

## Pièges courants

- **Confondre `npm run dev` et production** : certains comportements (prefetching, cache) diffèrent en développement. Testez toujours avec `build` + `start`.
- **Mauvaise version de Node** : erreurs obscures de build.
- **Oublier que le code serveur et client coexistent** : une API navigateur (`window`) appelée dans un composant serveur provoque une erreur.

## À retenir

- Next.js = React + routage + rendu serveur + données + optimisations + déploiement.
- Trois environnements : build, serveur, client.
- Les Server Components envoient du HTML/RSC ; les Client Components sont hydratés.
- Next.js 16 : Turbopack par défaut, Cache Components, `proxy.ts`.

## Exercices

1. Créez un projet avec `create-next-app`, lancez-le et modifiez `app/page.tsx`. Observez le Fast Refresh.
2. Exécutez `npm run build` puis `npm run start`. Relevez le tableau des routes affiché.
3. Expliquez, avec vos mots, la différence entre rendu serveur et hydratation.

---

# Chapitre 2 — Structure d'un projet

## Objectifs

- Connaître le rôle de chaque dossier et fichier de la racine.
- Appliquer les conventions de **colocation** et de dossiers privés.
- Configurer les alias d'import.

## 2.1 Arborescence type

```
mon-app/
├── app/                      # App Router : routes et UI
│   ├── layout.tsx            # Layout racine (obligatoire)
│   ├── page.tsx              # Route "/"
│   ├── globals.css
│   ├── favicon.ico
│   └── ...
├── public/                   # Fichiers statiques
├── components/               # (convention) composants partagés
├── lib/                      # (convention) fonctions utilitaires, accès aux données
├── next.config.ts            # Configuration de Next.js
├── proxy.ts                  # (optionnel) Proxy, ex-middleware.ts
├── instrumentation.ts        # (optionnel) observabilité
├── tsconfig.json
├── eslint.config.mjs
├── package.json
├── .env.local                # Variables d'environnement locales (non commité)
├── .gitignore
└── next-env.d.ts             # Types générés par Next.js (ne pas modifier)
```

### Fichiers et dossiers de la racine

| Élément | Rôle |
|---|---|
| `app/` | Routes de l'App Router |
| `pages/` | Routes du Pages Router (ancien système) |
| `public/` | Fichiers statiques servis à la racine du site : `public/logo.png` → `/logo.png` |
| `src/` | Dossier optionnel qui regroupe `app/`, `components/`, etc. (la config et `proxy.ts` restent à la racine ; `proxy.ts` va dans `src/` si `src/` est utilisé) |
| `next.config.ts` (ou `.js`/`.mjs`) | Configuration |
| `proxy.ts` | Interception des requêtes (⚠️ Version : remplace `middleware.ts`) |
| `instrumentation.ts` | Code exécuté au démarrage du serveur (monitoring, OpenTelemetry) |
| `.next/` | Sortie du build et du cache (**à ignorer dans Git**) |
| `.env*` | Variables d'environnement |
| `next-env.d.ts` | Déclarations de types ; régénéré automatiquement |

## 2.2 Dossier `public/`

Tout fichier placé dans `public/` est servi tel quel à partir de la racine du site. Usages : favicon, images statiques, `robots.txt` (ou génération via `app/robots.ts`), polices, fichiers de vérification de domaine.

```tsx
<img src="/logo.png" alt="Logo" />   // fichier public/logo.png
```

⚠️ Ne mettez jamais de données sensibles dans `public/` : tout est accessible publiquement. Next.js ne met en cache ces fichiers que selon les en-têtes configurés ; si un fichier change, renommez-le ou versionnez-le.

## 2.3 Dossier `src/`

Si vous choisissez `src/`, la structure devient `src/app/`, `src/components/`, `src/lib/`. Seules les configurations (`next.config.ts`, `package.json`, `tsconfig.json`, fichiers `.env`) restent à la racine. `proxy.ts` se place **dans** `src/` à côté de `app/`.

## 2.4 Conventions de nommage des fichiers dans `app/`

Dans `app/`, certains **noms de fichiers sont réservés** (voir chapitre 4) : `page`, `layout`, `loading`, `error`, `not-found`, `route`, `template`, `default`, etc. Les extensions supportées : `.js`, `.jsx`, `.ts`, `.tsx`.

## 2.5 Colocation

Dans l'App Router, **un dossier n'est accessible publiquement que s'il contient un `page` ou un `route`**. Vous pouvez donc placer côte à côte vos composants, styles, tests et utilitaires dans le dossier d'une route sans les exposer :

```
app/blog/
├── page.tsx              # → /blog
├── BlogCard.tsx          # non routable
├── blog.module.css       # non routable
└── utils.ts              # non routable
```

### Dossiers privés

Préfixer un dossier par `_` l'exclut explicitement du routage et signale son caractère privé :

```
app/
├── _components/Header.tsx    # jamais une route
└── _lib/db.ts
```

Pour qu'une URL commence réellement par un underscore, on l'encode : `%5Ffichier`.

### Groupes de routes

`(nom)` regroupe des routes sans modifier l'URL (voir chapitre 3).

## 2.6 Organisation recommandée

Trois stratégies courantes :

1. **Tout en dehors de `app/`** : `app/` ne contient que le routage ; `components/`, `lib/`, etc. sont à la racine ou dans `src/`.
2. **Dossiers partagés dans `app/`** : `app/_components`, `app/_lib`.
3. **Découpage par fonctionnalité (feature-based)** : `features/auth/`, `features/billing/` avec leurs composants, actions, schémas ; `app/` ne fait qu'importer.

Choisissez une stratégie et appliquez-la de façon cohérente dans toute l'équipe.

## 2.7 Alias d'import

Dans `tsconfig.json` (ou `jsconfig.json`) :

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": { "@/*": ["./src/*"] }
  }
}
```

Usage : `import { db } from "@/lib/db";` au lieu de `../../../lib/db`.

## 2.8 Fichiers de configuration courants

- **`next.config.ts`** : options de Next.js (chapitre 18).
- **`eslint.config.mjs`** : configuration ESLint (format « flat config »).
- **`postcss.config.mjs`** : utilisé par Tailwind CSS.
- **`.gitignore`** : doit ignorer `.next/`, `node_modules/`, `.env*.local`, `next-env.d.ts` (selon votre politique).

## Pièges courants

- **Placer un `page.tsx` dans un dossier utilitaire** : il devient une route publique.
- **Mélanger `app/` et `pages/`** avec des routes qui entrent en conflit : build en erreur.
- **Commiter `.env.local`** : fuite de secrets.

## À retenir

- `app/` = routes ; `public/` = statiques ; `src/` optionnel.
- Seuls `page` et `route` rendent un dossier accessible.
- `_dossier` = privé ; `(groupe)` = organisation sans impact sur l'URL.

## Exercices

1. Créez `app/dashboard/page.tsx` puis ajoutez `app/dashboard/_components/Stats.tsx`. Vérifiez que seul `/dashboard` existe.
2. Configurez l'alias `@/*` et refactorez un import relatif.

---

# Chapitre 3 — Routing (App Router)

## Objectifs

- Créer des routes statiques, dynamiques, catch-all.
- Utiliser layouts, templates, groupes, routes parallèles et interceptées.
- Lire les paramètres de route et de requête.
- Pré-générer des routes dynamiques.

## 3.1 Principes

Le routeur de Next.js est **basé sur le système de fichiers** :

- Un **dossier** dans `app/` = un **segment d'URL**.
- Un fichier **`page.tsx`** dans ce dossier rend la route **accessible**.
- Les dossiers imbriqués forment des routes imbriquées.

```
app/page.tsx                → /
app/about/page.tsx          → /about
app/blog/page.tsx           → /blog
app/blog/archive/page.tsx   → /blog/archive
```

### Anatomie d'une URL

```
https://exemple.com/blog/mon-article?tri=date#commentaires
        └ domaine ┘└────── chemin ──────┘└ query ┘└ fragment ┘
                     segments : blog / mon-article
```

- Le **chemin** est mis en correspondance avec l'arbre de dossiers.
- La **query string** (`?tri=date`) est lue via `searchParams`.
- Le **fragment** (`#commentaires`) n'est jamais envoyé au serveur.

### Hiérarchie de composants

Pour une route `/dashboard/settings`, Next.js assemble :

```
<RootLayout>
  <DashboardLayout>
    <SettingsPage />
  </DashboardLayout>
</RootLayout>
```

Chaque layout enveloppe ses enfants ; chaque segment peut aussi avoir son `loading`, `error`, `not-found`, qui deviennent des **frontières** (`Suspense`, *error boundary*) autour du segment.

## 3.2 Pages

```tsx
// app/about/page.tsx
export default function AboutPage() {
  return <h1>À propos</h1>;
}
```

- Une page est un composant exporté **par défaut**.
- Par défaut, c'est un **Server Component**.
- Une page peut être `async`.

## 3.3 Layouts

Un **layout** est une interface **partagée** entre plusieurs pages. Il reçoit `children` : la page ou le layout enfant.

```tsx
// app/layout.tsx — layout racine, obligatoire
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr">
      <body>{children}</body>
    </html>
  );
}
```

Règles :

- Le **layout racine** doit contenir les balises `<html>` et `<body>`.
- Un layout **ne se remonte pas** lors d'une navigation entre ses pages enfants : son état (champ de recherche, scroll de la barre latérale) est **conservé**.
- Un layout **ne reçoit pas** `searchParams` (il ne se re-rend pas quand la query change). Utilisez la page ou un Client Component avec `useSearchParams`.
- Un layout ne peut pas lire le chemin de la page enfant directement ; utilisez `usePathname()` dans un Client Component.
- Les layouts peuvent charger des données ; Next.js déduplique les requêtes identiques.

### Layouts imbriqués

```
app/
├── layout.tsx                    # racine
└── dashboard/
    ├── layout.tsx                # layout du tableau de bord
    ├── page.tsx                  # /dashboard
    └── settings/page.tsx         # /dashboard/settings
```

```tsx
// app/dashboard/layout.tsx
export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex">
      <aside>Menu latéral</aside>
      <main>{children}</main>
    </div>
  );
}
```

## 3.4 Templates

`template.tsx` fonctionne comme un layout, mais **un nouvel exemplaire est créé à chaque navigation**. L'état est **réinitialisé**, les effets sont ré-exécutés, le DOM est recréé.

Cas d'usage : animations d'entrée/sortie, journalisation de vues de page via `useEffect`, états qui doivent être remis à zéro à chaque page.

```tsx
// app/template.tsx
export default function Template({ children }: { children: React.ReactNode }) {
  return <div className="fade-in">{children}</div>;
}
```

Ordre de rendu : `layout` → `template` → `page` (le template se situe entre le layout et ses enfants).

## 3.5 Routes dynamiques

Un dossier entre crochets définit un **segment dynamique** : `[slug]`.

```
app/blog/[slug]/page.tsx   →  /blog/hello, /blog/nextjs-16, ...
```

```tsx
// app/blog/[slug]/page.tsx
export default async function PostPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  return <h1>Article : {slug}</h1>;
}
```

> ⚠️ **Version** : depuis Next.js 15, `params` est une **Promise** ; en Next.js 16, l'accès synchrone est **entièrement retiré**. Il faut `await params`. Dans un Client Component, on utilise le hook `use(params)` ou `useParams()`.

### Plusieurs segments dynamiques

```
app/[categorie]/[produit]/page.tsx   → /chaussures/air-max
```

```tsx
const { categorie, produit } = await params;
```

### Segment catch-all : `[...slug]`

Capture **un ou plusieurs** segments :

```
app/docs/[...slug]/page.tsx
/docs/a            → { slug: ["a"] }
/docs/a/b/c        → { slug: ["a", "b", "c"] }
/docs              → ❌ ne correspond pas
```

### Segment catch-all optionnel : `[[...slug]]`

Capture **zéro, un ou plusieurs** segments :

```
app/docs/[[...slug]]/page.tsx
/docs              → { slug: undefined }
/docs/a/b          → { slug: ["a", "b"] }
```

### Tableau récapitulatif

| Dossier | Exemple d'URL | `params` |
|---|---|---|
| `[id]` | `/produit/42` | `{ id: "42" }` |
| `[...slug]` | `/a/b/c` | `{ slug: ["a","b","c"] }` |
| `[[...slug]]` | `/` ou `/a/b` | `{ slug: undefined }` ou `{ slug: [...] }` |

> **Important** : les valeurs de `params` sont toujours des **chaînes** (ou tableaux de chaînes) ; convertissez-les (`Number(id)`) et **validez-les** (un utilisateur peut taper n'importe quoi dans l'URL).

### Priorité de correspondance

Quand plusieurs routes peuvent correspondre, Next.js privilégie la plus **spécifique** : segment statique > dynamique `[x]` > catch-all `[...x]` > catch-all optionnel `[[...x]]`.

## 3.6 Pré-génération : `generateStaticParams`

Permet de **générer à l'avance** (au build) les pages d'une route dynamique.

```tsx
// app/blog/[slug]/page.tsx
export async function generateStaticParams() {
  const posts = await fetch("https://api.exemple.com/posts").then((r) => r.json());
  return posts.map((post: { slug: string }) => ({ slug: post.slug }));
}
```

- Retourne un tableau d'objets dont les clés correspondent aux noms de segments.
- Pour plusieurs segments : `[{ categorie: "a", produit: "x" }, ...]`.
- Pour un catch-all : `{ slug: ["a", "b"] }`.
- Les requêtes `fetch` de `generateStaticParams` sont dédupliquées avec celles de la page.
- Une route avec `generateStaticParams` est marquée ● (SSG) au build.

### Que se passe-t-il pour une valeur non listée ?

Cela dépend de `dynamicParams` :

```tsx
export const dynamicParams = true;   // (défaut) génération à la demande, puis mise en cache
// export const dynamicParams = false; // toute valeur non listée → 404
```

> ⚠️ **Version** : avec **Cache Components** activé (`cacheComponents: true`), la configuration de segment `dynamicParams` n'est pas supportée ; le comportement dépend de l'usage de `"use cache"` et `Suspense` (voir chapitres 7 et 8). Avec Cache Components, `generateStaticParams` doit retourner au moins un jeu de paramètres pour permettre la validation au build.

## 3.7 Paramètres de requête (`searchParams`)

```tsx
// app/recherche/page.tsx — URL : /recherche?q=next&page=2
export default async function Recherche({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}) {
  const { q, page } = await searchParams;
  return <p>Recherche : {q} (page {page ?? "1"})</p>;
}
```

Points essentiels :

- `searchParams` est une **Promise** (⚠️ Version 15+).
- Lire `searchParams` rend la page **dynamique** (rendue à chaque requête), car la valeur n'est connue qu'à la requête.
- Disponible dans les **pages**, pas dans les layouts.
- Une même clé répétée (`?a=1&a=2`) donne un **tableau**.
- Côté client : `useSearchParams()` (à envelopper dans `<Suspense>` pour ne pas désactiver le pré-rendu statique de toute la page).

## 3.8 Groupes de routes : `(nom)`

Un dossier entre parenthèses **n'apparaît pas dans l'URL**. Utilités :

1. **Organiser** les routes par domaine fonctionnel.
2. **Attribuer des layouts différents** à des groupes de pages.
3. Créer **plusieurs layouts racines** (chacun avec `<html>` et `<body>`).

```
app/
├── (marketing)/
│   ├── layout.tsx
│   ├── page.tsx              → /
│   └── about/page.tsx        → /about
├── (app)/
│   ├── layout.tsx            # layout avec barre latérale
│   └── dashboard/page.tsx    → /dashboard
```

⚠️ Deux groupes ne doivent pas définir **la même URL** (par exemple `(a)/about/page.tsx` et `(b)/about/page.tsx`) : erreur. Naviguer entre deux layouts racines différents provoque un **rechargement complet** de la page.

## 3.9 Routes parallèles : `@slot`

Les **routes parallèles** permettent de rendre **simultanément** plusieurs pages dans un même layout, ou de rendre conditionnellement. Un dossier `@nom` définit un **slot** ; il est passé en **prop** au layout parent (ce n'est pas un segment d'URL).

```
app/
├── layout.tsx
├── page.tsx
├── @analytics/
│   ├── page.tsx
│   └── default.tsx
└── @equipe/
    ├── page.tsx
    └── default.tsx
```

```tsx
// app/layout.tsx
export default function Layout({
  children,
  analytics,
  equipe,
}: {
  children: React.ReactNode;
  analytics: React.ReactNode;
  equipe: React.ReactNode;
}) {
  return (
    <>
      {children}
      <section>{analytics}</section>
      <section>{equipe}</section>
    </>
  );
}
```

Chaque slot a ses propres `loading.tsx` et `error.tsx` : il se charge et échoue **indépendamment** (streaming, résilience).

### `default.tsx`

- Lors d'une **navigation côté client** (soft navigation), Next.js conserve l'état des slots non concernés.
- Lors d'un **chargement complet** (hard navigation, rafraîchissement), un slot dont le contenu ne correspond pas à l'URL affiche son **`default.tsx`** ; sans lui → 404.

> ⚠️ **Version** : Next.js 16 **exige** un fichier `default.tsx` explicite pour chaque slot de route parallèle ; sans lui, le build échoue.

### Cas d'usage

- Tableaux de bord avec panneaux indépendants.
- **Rendu conditionnel** selon le rôle (`@admin` / `@utilisateur`) en choisissant dans le layout.
- Modales (avec routes interceptées).
- Onglets avec leur propre état de navigation.

## 3.10 Routes interceptées

Elles permettent de **charger une route dans le contexte courant** (par exemple en **modale**) lors d'une navigation interne, tout en gardant une **URL partageable** qui, lors d'un accès direct, affiche la page complète.

Syntaxe (relative aux **segments de route**, pas aux dossiers du système de fichiers) :

| Convention | Intercepte |
|---|---|
| `(.)nom` | Le même niveau |
| `(..)nom` | Un niveau au-dessus |
| `(..)(..)nom` | Deux niveaux au-dessus |
| `(...)nom` | Depuis la racine `app/` |

### Exemple : galerie photo avec modale

```
app/
├── layout.tsx                 # reçoit children + modal
├── page.tsx                   # galerie
├── @modal/
│   ├── default.tsx            # retourne null
│   └── (.)photo/[id]/page.tsx # photo affichée en modale
└── photo/[id]/page.tsx        # page complète (accès direct)
```

```tsx
// app/layout.tsx
export default function Layout({
  children,
  modal,
}: {
  children: React.ReactNode;
  modal: React.ReactNode;
}) {
  return (
    <html lang="fr">
      <body>
        {children}
        {modal}
      </body>
    </html>
  );
}
```

```tsx
// app/@modal/default.tsx
export default function Default() {
  return null;
}
```

Fermeture de la modale : `router.back()` dans un Client Component.

Comportement :

- Clic sur un lien `/photo/3` depuis la galerie → modale (interception).
- Rafraîchissement ou lien partagé → page complète `/photo/3`.

## 3.11 Hooks utiles liés au routage

| Hook (Client Component) | Rôle |
|---|---|
| `usePathname()` | Chemin courant (`/blog/a`) |
| `useParams()` | Paramètres dynamiques |
| `useSearchParams()` | Lecture des paramètres de requête |
| `useSelectedLayoutSegment()` | Segment actif juste sous le layout |
| `useSelectedLayoutSegments()` | Tous les segments actifs sous le layout |
| `useRouter()` | Navigation impérative (chapitre 12) |

Exemple : lien actif.

```tsx
"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

export function NavLink({ href, children }: { href: string; children: React.ReactNode }) {
  const pathname = usePathname();
  const active = pathname === href;
  return (
    <Link href={href} aria-current={active ? "page" : undefined} className={active ? "active" : ""}>
      {children}
    </Link>
  );
}
```

## 3.12 Redirections et réécritures au niveau routage

- **Redirections** (`redirects` dans `next.config`) : renvoient un statut 307/308 ; l'URL du navigateur change.
- **Réécritures** (`rewrites`) : servent un autre contenu sans changer l'URL affichée (proxy transparent).
- Voir chapitres 11 et 18.

## 3.13 Types d'aide pour `params` (⚠️ Version)

Next.js 15.5+ / 16 offrent des helpers de types globaux, générés par `next dev`, `next build` ou `next typegen` :

```tsx
export default async function Page(props: PageProps<"/blog/[slug]">) {
  const { slug } = await props.params;
  return <h1>{slug}</h1>;
}
```

Autres helpers : `LayoutProps<"/dashboard">`, `RouteContext<"/api/posts/[id]">`. Ils évitent de retaper les types des paramètres.

## Pièges courants

- **Oublier `await params`** (Next.js 15/16) : erreur ou avertissement.
- **Utiliser `searchParams` dans un layout** : ce n'est pas supporté ; passez par la page.
- **Lire `searchParams` sans le savoir** : la page devient dynamique.
- **Deux routes menant à la même URL** (via groupes) : erreur de build.
- **Oublier `default.tsx`** dans un slot parallèle : build en échec (Next.js 16).
- **Confondre `[...slug]` et `[[...slug]]`** : le premier ne correspond pas à la racine du segment.

## À retenir

- Dossier = segment ; `page.tsx` = route publique.
- `layout` persiste, `template` se recrée.
- `[x]`, `[...x]`, `[[...x]]` pour le dynamique ; `(x)` pour regrouper ; `@x` pour les slots ; `(.)x` pour intercepter.
- `params` et `searchParams` sont asynchrones.
- `generateStaticParams` pré-génère les routes dynamiques.

## Exercices

1. Créez `/blog/[slug]` avec `generateStaticParams` sur trois articles factices ; testez un slug inconnu avec `dynamicParams` à `true` puis `false`.
2. Créez deux groupes `(marketing)` et `(app)` avec deux layouts différents.
3. Implémentez une galerie avec modale (route interceptée + route parallèle `@modal`).
4. Créez `/docs/[[...slug]]` et affichez le fil d'Ariane à partir de `slug`.

---

# Chapitre 4 — Fichiers spéciaux

## Objectifs

- Connaître chaque fichier réservé de l'App Router et son rôle.
- Gérer les états de chargement, d'erreur, de page introuvable.
- Générer des fichiers de métadonnées (icônes, sitemap, manifest…).

## 4.1 Vue d'ensemble

Next.js attribue un **sens particulier** à certains noms de fichiers. Ils se composent **dans un ordre hiérarchique précis** autour de la page :

```
<Layout>
  <Template>
    <ErrorBoundary fallback={<Error />}>
      <Suspense fallback={<Loading />}>
        <ErrorBoundary fallback={<NotFound />}>
          <Page />
        </ErrorBoundary>
      </Suspense>
    </ErrorBoundary>
  </Template>
</Layout>
```

Cette imbrication explique plusieurs comportements : par exemple, `error.tsx` d'un segment **n'intercepte pas** les erreurs du `layout.tsx` du **même** segment (il se trouve à l'intérieur) ; on utilise alors le `error.tsx` du segment parent ou `global-error.tsx`.

| Fichier | Rôle |
|---|---|
| `layout` | UI partagée, persistante |
| `page` | UI unique d'une route (la rend publique) |
| `template` | Layout recréé à chaque navigation |
| `loading` | État de chargement instantané (Suspense) |
| `error` | Frontière d'erreur du segment |
| `global-error` | Frontière d'erreur du layout racine |
| `not-found` | UI « introuvable » (404) |
| `route` | Endpoint HTTP (Route Handler) |
| `default` | Repli d'un slot de route parallèle |
| `forbidden` / `unauthorized` | Pages 403 / 401 (expérimental) |
| `middleware`/`proxy` | Interception des requêtes (racine) |
| `instrumentation` | Hook de démarrage / observabilité |
| `opengraph-image`, `twitter-image`, `icon`, `apple-icon` | Images de métadonnées |
| `sitemap`, `robots`, `manifest` | Fichiers SEO/PWA |

## 4.2 `loading.tsx`

Crée automatiquement une frontière `<Suspense>` autour de la page et de ses enfants. Pendant que la page (asynchrone) charge ses données, l'utilisateur voit immédiatement le **contenu de `loading.tsx`**, et la navigation reste **interruptible**.

```tsx
// app/dashboard/loading.tsx
export default function Loading() {
  return <div className="skeleton">Chargement du tableau de bord…</div>;
}
```

Bonnes pratiques :

- Afficher des **squelettes** (skeletons) fidèles à la mise en page finale pour limiter les décalages visuels.
- `loading.tsx` ne protège **que** ce qui est **sous** lui : un layout qui attend des données n'est pas couvert.
- Pour un contrôle plus fin, utilisez `<Suspense>` directement dans la page autour de composants individuels.

## 4.3 `error.tsx`

Une **frontière d'erreur React** pour le segment : elle capture les erreurs **de rendu** (et d'exécution dans les composants enfants) et affiche une UI de repli, sans casser le reste de l'application (les layouts parents restent affichés).

```tsx
// app/dashboard/error.tsx
"use client"; // obligatoire : les error boundaries sont des Client Components

import { useEffect } from "react";

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error(error); // journaliser vers un service de monitoring
  }, [error]);

  return (
    <div role="alert">
      <h2>Quelque chose s'est mal passé</h2>
      <button onClick={() => reset()}>Réessayer</button>
    </div>
  );
}
```

Points essentiels :

- **`"use client"` obligatoire.**
- `reset()` tente de **re-rendre** le segment.
- **`error.digest`** : identifiant d'erreur. En **production**, les erreurs levées dans les Server Components sont **masquées** au client (le message réel contient peut-être des informations sensibles) ; seul un `digest` générique est transmis, que l'on retrouve dans les logs serveur.
- **Ne capture pas** : les erreurs dans les **gestionnaires d'événements** (utilisez `try/catch` et `useState`), les erreurs asynchrones hors du rendu, les erreurs dans le layout du même segment.
- Pour les **erreurs attendues** dans les Server Actions (validation, conflit), **ne levez pas d'exception** : retournez un objet d'erreur (voir chapitre 9).

### `global-error.tsx`

Capture les erreurs du **layout racine**. Il remplace complètement le layout racine : il doit donc définir `<html>` et `<body>`.

```tsx
// app/global-error.tsx
"use client";

export default function GlobalError({ reset }: { error: Error; reset: () => void }) {
  return (
    <html lang="fr">
      <body>
        <h2>Erreur critique</h2>
        <button onClick={() => reset()}>Réessayer</button>
      </body>
    </html>
  );
}
```

## 4.4 `not-found.tsx` et `notFound()`

```tsx
// app/blog/[slug]/page.tsx
import { notFound } from "next/navigation";

export default async function Post({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const post = await getPost(slug);
  if (!post) notFound(); // lève une exception interne, interrompt le rendu
  return <article>{post.title}</article>;
}
```

```tsx
// app/blog/[slug]/not-found.tsx
export default function NotFound() {
  return <h2>Article introuvable</h2>;
}
```

- `notFound()` renvoie le statut **404** et affiche le `not-found.tsx` le plus proche.
- Un `app/not-found.tsx` à la racine gère **toutes les URLs non correspondantes** de l'application.
- En streaming, si les en-têtes ont déjà été envoyés, le statut peut rester 200 avec une balise `noindex` ajoutée automatiquement.

## 4.5 Redirections : `redirect` et `permanentRedirect`

```tsx
import { redirect, permanentRedirect } from "next/navigation";

redirect("/login");               // 307 (temporaire) ; 303 depuis une Server Action
permanentRedirect("/nouvelle-url"); // 308 (permanente)
```

- Utilisables dans les Server Components, Server Actions, Route Handlers.
- **Elles lèvent une exception interne** : ne les placez **pas** dans un `try/catch` (sinon vous interceptez la redirection), ou relancez l'erreur. Appelez-les en dehors du bloc, ou utilisez `unstable_rethrow(error)` dans le `catch`.
- Côté client (événement) : préférez `router.push`.

## 4.6 `forbidden()` et `unauthorized()` (expérimental)

Pages dédiées aux statuts **403** et **401**, à activer :

```ts
// next.config.ts
const nextConfig = { experimental: { authInterrupts: true } };
export default nextConfig;
```

```tsx
import { forbidden, unauthorized } from "next/navigation";

const session = await verifySession();
if (!session) unauthorized();           // affiche app/unauthorized.tsx (401)
if (session.role !== "admin") forbidden(); // affiche app/forbidden.tsx (403)
```

## 4.7 `route.ts`

Définit un **endpoint HTTP** (voir chapitre 10). Un dossier ne peut pas contenir **à la fois** `page.tsx` et `route.ts` pour la même URL (conflit), sauf si les méthodes/Accept diffèrent selon la configuration ; en pratique, séparez-les.

## 4.8 `default.tsx`

Repli pour un slot de route parallèle (chapitre 3). Obligatoire dans Next.js 16.

## 4.9 `instrumentation.ts`

Exécuté **une fois au démarrage** du serveur. Sert à brancher **OpenTelemetry**, Sentry, Datadog, etc.

```ts
// instrumentation.ts (racine ou src/)
export async function register() {
  if (process.env.NEXT_RUNTIME === "nodejs") {
    await import("./instrumentation-node");
  }
}

export async function onRequestError(
  err: unknown,
  request: { path: string; method: string; headers: Record<string, string | string[] | undefined> },
  context: { routerKind: string; routePath: string; routeType: string; renderSource?: string }
) {
  // envoyer l'erreur à votre outil de monitoring
}
```

## 4.10 Fichiers de métadonnées

### Icônes

- `app/favicon.ico`, `app/icon.png|jpg|svg`, `app/apple-icon.png`.
- Génération dynamique : `app/icon.tsx` retournant une `ImageResponse`.

### Images Open Graph / Twitter

```tsx
// app/blog/[slug]/opengraph-image.tsx
import { ImageResponse } from "next/og";

export const size = { width: 1200, height: 630 };
export const contentType = "image/png";
export const alt = "Image de l'article";

export default async function Image({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  return new ImageResponse(
    <div style={{ fontSize: 64, display: "flex", width: "100%", height: "100%", alignItems: "center", justifyContent: "center" }}>
      {slug}
    </div>,
    size
  );
}
```

### `sitemap.ts`, `robots.ts`, `manifest.ts`

Voir chapitre 15.

## Pièges courants

- **Oublier `"use client"` dans `error.tsx`** : erreur de build.
- **Attendre que `error.tsx` capture une erreur de son propre `layout.tsx`** : placez-le dans le parent.
- **Mettre `redirect()` dans un `try/catch`** : la redirection est avalée.
- **Exposer des messages d'erreur serveur au client** : en production Next.js les masque ; ne les réinjectez pas manuellement.

## À retenir

- Les fichiers spéciaux composent une hiérarchie de frontières : Layout > Template > Error > Suspense (loading) > NotFound > Page.
- `loading` = Suspense automatique ; `error` = error boundary (client) ; `not-found` = 404.
- `redirect` et `notFound` interrompent le rendu en levant une exception.

## Exercices

1. Ajoutez `loading.tsx` à une page qui attend 2 secondes (`await new Promise(r => setTimeout(r, 2000))`).
2. Provoquez une erreur volontaire dans un composant et affichez-la via `error.tsx` avec un bouton « Réessayer ».
3. Créez un `app/not-found.tsx` personnalisé et testez-le avec une URL inexistante.

---

# Chapitre 5 — Server Components et Client Components

## Objectifs

- Comprendre le modèle des **React Server Components (RSC)**.
- Savoir quand choisir un Server ou un Client Component.
- Maîtriser la frontière `"use client"` et les règles de composition.
- Protéger le code et les données sensibles.

## 5.1 Le modèle mental

Dans l'App Router, **tout composant est un Server Component par défaut**. On choisit de basculer vers le client **seulement quand c'est nécessaire**.

### Server Components

Exécutés **uniquement sur le serveur** (au build ou à la requête). Leur code n'est **jamais envoyé** au navigateur ; seul leur **résultat** l'est.

**Avantages :**

- **Accès direct aux ressources back-end** : base de données, système de fichiers, services internes.
- **Sécurité** : secrets et clés d'API ne quittent pas le serveur.
- **Moins de JavaScript** : les bibliothèques lourdes utilisées uniquement côté serveur (Markdown, formatage de dates, ORM) n'alourdissent pas le bundle.
- **Performance** : données chargées près de la source, requêtes rapides, pas de cascade client→API.
- **Streaming** et **cache**.
- **SEO** : contenu présent dans le HTML initial.

**Limites :**

- Pas de **`useState`**, `useReducer`, `useEffect`, `useLayoutEffect`.
- Pas de **gestionnaires d'événements** (`onClick`…).
- Pas d'**API du navigateur** (`window`, `document`, `localStorage`, `navigator`).
- Pas de **Context** (`createContext`/`useContext`).
- Pas de hooks personnalisés qui dépendent des éléments ci-dessus.

### Client Components

Marqués par la directive **`"use client"`**. Ils sont **pré-rendus** sur le serveur (HTML initial) **puis hydratés** dans le navigateur. Ils servent à tout ce qui est **interactif**.

**Utilisations :** état local, événements, effets, API navigateur, contextes, hooks personnalisés, bibliothèques purement clientes (cartes, graphiques interactifs, éditeurs riches).

```tsx
"use client";

import { useState } from "react";

export default function Compteur() {
  const [n, setN] = useState(0);
  return <button onClick={() => setN(n + 1)}>Clics : {n}</button>;
}
```

### Tableau de décision

| Besoin | Server | Client |
|---|:-:|:-:|
| Lire une base de données / un secret | ✅ | ❌ |
| `async/await` directement dans le composant | ✅ | ❌ |
| `useState`, `useEffect`, `useReducer` | ❌ | ✅ |
| `onClick`, `onChange`, `onSubmit` (handlers) | ❌ | ✅ |
| `window`, `localStorage`, `navigator` | ❌ | ✅ |
| `useContext` / providers | ❌ | ✅ |
| Réduire le JS envoyé | ✅ | ❌ |
| Bibliothèque dépendant du navigateur | ❌ | ✅ |

## 5.2 La directive `"use client"`

- À placer **tout en haut du fichier**, avant les imports.
- Déclare une **frontière client–serveur** : **ce fichier et tous les modules qu'il importe** (directement ou indirectement) font partie du bundle client.
- On n'a **pas besoin** de la répéter dans chaque composant enfant importé par un fichier déjà « client ».
- Elle s'applique au **module**, pas à un composant individuel.

```tsx
"use client";
import { Bouton } from "./Bouton";   // Bouton devient automatiquement client
```

### Composants « partagés »

Un composant **sans** directive, sans API serveur ni client spécifique, peut être utilisé **des deux côtés** : il s'exécute selon l'endroit d'où il est importé (serveur s'il est importé par un Server Component, client s'il est importé par un Client Component).

## 5.3 Que se passe-t-il à l'exécution ?

**Au chargement initial (rendu serveur)**

1. React rend les Server Components en un format spécial : le **payload RSC** (représentation compacte de l'arbre, avec des « trous » qui référencent les Client Components).
2. Next.js utilise ce payload et le code des Client Components pour générer le **HTML** pré-rendu, envoyé au navigateur.
3. Côté client, le payload RSC sert à **réconcilier** l'arbre de Server et de Client Components et à mettre à jour le DOM.
4. Les Client Components sont **hydratés**.

**Navigations suivantes**

- Le navigateur demande uniquement le **payload RSC** des segments qui changent ; les Client Components déjà chargés sont réutilisés ; **pas de rechargement complet**.

## 5.4 Règles de composition

### 5.4.1 Un Server Component peut importer un Client Component ✅

```tsx
// Server Component
import Compteur from "./Compteur"; // "use client"

export default function Page() {
  return (
    <>
      <h1>Page serveur</h1>
      <Compteur />
    </>
  );
}
```

### 5.4.2 Un Client Component ne peut pas **importer** un Server Component ❌

Si un fichier `"use client"` importe un composant serveur, ce dernier **devient client** (et perd ses capacités serveur : `async`, `server-only`, etc.).

### 5.4.3 …mais il peut **recevoir** un Server Component en `children` ou en prop ✅

C'est le **pattern d'entrelacement** (interleaving) :

```tsx
// Modal.tsx
"use client";
import { useState } from "react";

export default function Modal({ children }: { children: React.ReactNode }) {
  const [ouvert, setOuvert] = useState(false);
  return (
    <>
      <button onClick={() => setOuvert(true)}>Ouvrir</button>
      {ouvert && <div role="dialog">{children}</div>}
    </>
  );
}
```

```tsx
// page.tsx (Server Component)
import Modal from "./Modal";
import Panier from "./Panier"; // Server Component asynchrone

export default function Page() {
  return (
    <Modal>
      <Panier />  {/* rendu côté serveur, passé comme children */}
    </Modal>
  );
}
```

Le Server Component est rendu **sur le serveur d'abord**, le résultat sérialisé est passé au Client Component comme un « trou » à remplir. Le client n'a pas besoin de son code.

### 5.4.4 Sérialisation des props

Les props passées d'un Server Component à un Client Component doivent être **sérialisables par React** :

| ✅ Autorisé | ❌ Interdit |
|---|---|
| string, number, boolean, null, undefined | **Fonctions** (sauf Server Actions) |
| Tableaux, objets simples | Instances de classes |
| `Date`, `Map`, `Set`, `BigInt`, `Promise` | Symboles non globaux |
| `FormData`, `TypedArray`, éléments JSX | Objets avec méthodes |
| **Server Actions** (fonctions `"use server"`) | Composants passés comme références client non sérialisables |

Astuce : si vous avez besoin de passer une fonction, passez plutôt une **Server Action**, ou déclarez la fonction côté client.

### 5.4.5 Promises comme props et hook `use`

Un Server Component peut passer une **promesse non attendue** à un Client Component, qui la lit avec `use()` (avec `Suspense`) : démarrage de la requête côté serveur, rendu côté client.

```tsx
// Server Component
import { Suspense } from "react";
import Posts from "./Posts";

export default function Page() {
  const posts = getPosts(); // pas de await
  return (
    <Suspense fallback={<p>Chargement…</p>}>
      <Posts posts={posts} />
    </Suspense>
  );
}
```

```tsx
// Posts.tsx
"use client";
import { use } from "react";

export default function Posts({ posts }: { posts: Promise<{ id: string; title: string }[]> }) {
  const liste = use(posts);
  return <ul>{liste.map((p) => <li key={p.id}>{p.title}</li>)}</ul>;
}
```

## 5.5 Placer la frontière le plus bas possible

Marquer un **grand** composant `"use client"` envoie tout son sous-arbre au navigateur. Préférez **isoler la partie interactive** dans un petit composant.

❌ Mauvais :

```tsx
"use client";
export default function Page() {      // toute la page devient cliente
  const [open, setOpen] = useState(false);
  return (<>
    <HeavyArticle />                  {/* dépend d'une grosse bibliothèque */}
    <button onClick={() => setOpen(!open)}>Menu</button>
  </>);
}
```

✅ Bon :

```tsx
// Page serveur
import MenuToggle from "./MenuToggle"; // petit composant client
export default function Page() {
  return (<>
    <HeavyArticle />
    <MenuToggle />
  </>);
}
```

## 5.6 Fournisseurs de contexte (Context Providers)

`createContext` n'est pas disponible dans les Server Components. On crée un **Client Component Provider** et on l'insère **le plus bas possible**.

```tsx
// theme-provider.tsx
"use client";
import { createContext, useContext, useState } from "react";

const ThemeContext = createContext<"light" | "dark">("light");
export const useTheme = () => useContext(ThemeContext);

export default function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme] = useState<"light" | "dark">("light");
  return <ThemeContext.Provider value={theme}>{children}</ThemeContext.Provider>;
}
```

```tsx
// app/layout.tsx (serveur)
import ThemeProvider from "./theme-provider";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr">
      <body>
        <ThemeProvider>{children}</ThemeProvider>
      </body>
    </html>
  );
}
```

Les `children` (Server Components) restent rendus côté serveur grâce au pattern d'entrelacement.

## 5.7 Bibliothèques tierces

Beaucoup de bibliothèques utilisent `useState` ou des effets sans déclarer `"use client"`. Les importer directement dans un Server Component provoque une erreur. Solution : un **wrapper** :

```tsx
// carousel.tsx
"use client";
import { Carousel } from "acme-carousel";
export default Carousel;
```

## 5.8 Protéger le code serveur : `server-only` et `client-only`

```bash
npm install server-only client-only
```

```ts
// lib/data.ts
import "server-only"; // erreur de build si importé par un Client Component
export async function getSecrets() { /* ... */ }
```

- **`server-only`** empêche un module (qui utilise des secrets, la base de données) d'être importé côté client.
- **`client-only`** empêche l'inverse (module dépendant de `window`).

### Variables d'environnement

Seules les variables préfixées **`NEXT_PUBLIC_`** sont inlinées dans le code client ; les autres sont remplacées par une chaîne vide côté client (chapitre 19).

### API de « taint » (expérimentale)

React propose `experimental_taintObjectReference` et `experimental_taintUniqueValue` pour **interdire** qu'un objet ou une valeur sensible (jeton, utilisateur complet) soit passé à un Client Component. À activer via `experimental.taint`. Elle **complète** mais ne remplace pas une bonne **couche d'accès aux données (DAL)** qui ne renvoie que des **DTO** (objets minimaux).

## 5.9 Chargement dynamique et `ssr: false`

```tsx
// Client Component
"use client";
import dynamic from "next/dynamic";

const Carte = dynamic(() => import("./Carte"), {
  ssr: false,              // ne pas pré-rendre côté serveur
  loading: () => <p>Chargement de la carte…</p>,
});
```

⚠️ `ssr: false` n'est **autorisé que dans un Client Component** (⚠️ Version 15+).

## 5.10 Erreurs d'hydratation

Causes fréquentes :

- Utiliser `Date.now()`, `Math.random()`, `window.innerWidth` dans le rendu (valeurs différentes serveur/client).
- Imbriquer du HTML invalide (`<p>` dans `<p>`, `<div>` dans `<p>`).
- Extensions de navigateur qui modifient le DOM.
- Formats de date/langue dépendant du fuseau.

Solutions : déplacer le code dépendant du client dans `useEffect`, utiliser un état « monté », ou `suppressHydrationWarning` (à utiliser avec parcimonie, sur un seul niveau d'élément).

## Pièges courants

- **Marquer toute la page `"use client"` « pour que ça marche »** : perte des bénéfices des RSC.
- **Importer un module serveur secret dans un composant client** sans `server-only`.
- **Passer une fonction en prop** d'un Server à un Client Component.
- **Oublier `Suspense`** autour d'un composant qui lit une promesse avec `use`.
- **Utiliser `useContext` dans un Server Component**.

## À retenir

- Par défaut : Server Component. `"use client"` seulement pour l'interactivité.
- La frontière est définie au niveau du **module**.
- Entrelacez : Server Component en `children` d'un Client Component.
- Props sérialisables ; secrets protégés (`server-only`, DAL, DTO).

## Exercices

1. Transformez une page entièrement cliente en page serveur + petit composant client interactif.
2. Créez un `ThemeProvider` client et utilisez-le depuis le layout racine.
3. Provoquez volontairement une erreur d'hydratation avec `Math.random()` puis corrigez-la.
4. Créez un module `lib/secret.ts` avec `import "server-only"` et essayez de l'importer dans un composant client.

---

# Chapitre 6 — Récupération de données (Data Fetching)

## Objectifs

- Charger des données dans les Server Components (fetch, ORM).
- Organiser les requêtes en parallèle ou en séquence.
- Utiliser le streaming avec `Suspense`.
- Charger des données côté client lorsque nécessaire.
- Connaître les API de requête (`cookies`, `headers`, etc.).

## 6.1 Principe

Dans l'App Router, **un composant serveur peut être `async`** et attendre directement ses données :

```tsx
export default async function Page() {
  const res = await fetch("https://api.exemple.com/posts");
  if (!res.ok) throw new Error("Échec du chargement");
  const posts: { id: number; title: string }[] = await res.json();

  return (
    <ul>
      {posts.map((p) => (
        <li key={p.id}>{p.title}</li>
      ))}
    </ul>
  );
}
```

Pas de `useEffect`, pas d'état de chargement manuel : la requête s'exécute **sur le serveur**, avant l'envoi du HTML.

## 6.2 Sources de données

### 6.2.1 `fetch` (API externes)

- L'API Web standard `fetch` est **étendue** par Next.js (options `cache`, `next.revalidate`, `next.tags`).
- ⚠️ **Version 15+** : les requêtes `fetch` **ne sont plus mises en cache par défaut** ; vous choisissez explicitement la mise en cache (ou, avec Cache Components, vous utilisez `"use cache"`).
- Gérez toujours les erreurs : `res.ok`, codes HTTP, expirations.

### 6.2.2 Base de données / ORM / SDK

Comme le code s'exécute sur le serveur, on peut appeler directement Prisma, Drizzle, un client SQL, un SDK de CMS :

```tsx
import { db } from "@/lib/db";

export default async function Utilisateurs() {
  const users = await db.user.findMany({ select: { id: true, name: true } });
  return <ul>{users.map((u) => <li key={u.id}>{u.name}</li>)}</ul>;
}
```

### 6.2.3 Système de fichiers

```tsx
import { readFile } from "node:fs/promises";
import path from "node:path";

export default async function Page() {
  const contenu = await readFile(path.join(process.cwd(), "content/a-propos.md"), "utf8");
  return <pre>{contenu}</pre>;
}
```

## 6.3 Déduplication des requêtes

Dans **un même passage de rendu**, plusieurs composants peuvent demander les mêmes données sans surcoût : Next.js **mémoïse** les `fetch` GET identiques (*Request Memoization*). Pour les accès **sans `fetch`** (ORM, SDK), utilisez **`React.cache`** :

```ts
// lib/data.ts
import { cache } from "react";
import { db } from "./db";

export const getUser = cache(async (id: string) => {
  return db.user.findUnique({ where: { id } });
});
```

Le layout, la page et un composant enfant peuvent tous appeler `getUser("42")` : **une seule** requête est faite par rendu. Ce cache vit le **temps d'une requête serveur** (il est distinct du cache persistant du chapitre 7).

> **Conseil** : au lieu de « remonter » les données dans un parent pour les passer en props, **récupérez-les là où vous en avez besoin**, grâce à la déduplication.

## 6.4 Requêtes parallèles et séquentielles

### Séquentielles (cascade, « waterfall »)

```tsx
const artiste = await getArtiste(id);        // 1) attendre
const albums = await getAlbums(artiste.id);  // 2) dépend du résultat précédent
```

Acceptable **uniquement** si la 2ᵉ requête **dépend** de la 1ʳᵉ.

### Parallèles

```tsx
const [artiste, albums] = await Promise.all([getArtiste(id), getAlbums(id)]);
```

Si une requête peut échouer sans bloquer l'autre : `Promise.allSettled`.

### Pattern « preload »

Démarrer une requête tôt, l'attendre plus tard :

```tsx
const promesse = getAlbums(id);       // lancée
const artiste = await getArtiste(id); // on attend l'autre
const albums = await promesse;        // probablement déjà prête
```

### Cascades implicites par composants

Si un parent `async` attend ses données avant de rendre un enfant `async`, les requêtes s'enchaînent. Atténuez avec **`Suspense`** (les deux composants rendent indépendamment) ou en remontant les requêtes avec `Promise.all`.

## 6.5 Streaming avec Suspense et `loading.tsx`

Le **streaming** envoie le HTML **par morceaux** : la coque de la page arrive tout de suite, puis chaque zone lente arrive quand elle est prête.

```tsx
import { Suspense } from "react";

export default function Dashboard() {
  return (
    <>
      <h1>Tableau de bord</h1>               {/* envoyé immédiatement */}
      <Suspense fallback={<Skeleton />}>
        <Statistiques />                     {/* lent */}
      </Suspense>
      <Suspense fallback={<Skeleton />}>
        <DernieresCommandes />               {/* lent, indépendant */}
      </Suspense>
    </>
  );
}
```

Avantages : meilleur **TTFB** perçu, interaction plus tôt (hydratation sélective), isolement des lenteurs.

## 6.6 Données dans les Client Components

Quand les données dépendent de l'interactivité (saisie, polling, temps réel), plusieurs options :

1. **Promesse passée depuis le serveur** + `use()` (voir chapitre 5).
2. **Bibliothèques** : **SWR** ou **TanStack Query** (cache, revalidation, déduplication, états de chargement).
3. **Route Handler** (`/api/...`) appelé depuis le client.

```tsx
"use client";
import useSWR from "swr";

const fetcher = (url: string) => fetch(url).then((r) => r.json());

export default function Profil() {
  const { data, error, isLoading } = useSWR("/api/profil", fetcher);
  if (isLoading) return <p>Chargement…</p>;
  if (error) return <p>Erreur</p>;
  return <p>{data.nom}</p>;
}
```

> **À éviter** : appeler **depuis un Server Component** votre propre Route Handler (`fetch("/api/...")`). Cela ajoute un aller-retour réseau inutile ; appelez directement la fonction partagée.

## 6.7 API de requête dynamiques

Ces API lisent des informations **propres à la requête** : leur utilisation rend la portion concernée **dynamique**.

```tsx
import { cookies, headers, draftMode } from "next/headers";
import { connection } from "next/server";

const cookieStore = await cookies();
const theme = cookieStore.get("theme")?.value;

const headerList = await headers();
const ua = headerList.get("user-agent");

const { isEnabled } = await draftMode();

await connection(); // « attendre une vraie requête » avant de continuer (rend le rendu dynamique)
```

> ⚠️ **Version** : `cookies()`, `headers()`, `draftMode()`, `params`, `searchParams` sont **asynchrones** ; Next.js 16 supprime l'accès synchrone. Un **codemod** est fourni : `npx @next/codemod@canary upgrade latest`.

- `cookies()` : lecture seule dans les Server Components ; **écriture** (`set`, `delete`) uniquement dans les **Server Actions** et **Route Handlers** (car les en-têtes sont déjà partis lors d'un rendu en streaming).
- `connection()` remplace l'ancien `unstable_noStore()` pour signaler « ne pas pré-rendre ceci ».
- Avec **Cache Components**, ces API ne sont **pas utilisables à l'intérieur** d'un périmètre `"use cache"` : lisez-les **à l'extérieur** et passez les valeurs en arguments.

## 6.8 Exemple : pagination et filtre via l'URL

L'URL est une excellente source d'état **partageable**.

```tsx
// app/produits/page.tsx
export default async function Produits({
  searchParams,
}: {
  searchParams: Promise<{ page?: string; q?: string }>;
}) {
  const { page = "1", q = "" } = await searchParams;
  const numero = Math.max(1, Number(page) || 1);
  const produits = await db.produit.findMany({
    where: { nom: { contains: q } },
    skip: (numero - 1) * 20,
    take: 20,
  });

  return (
    <>
      <FormulaireRecherche valeur={q} />
      <ListeProduits produits={produits} />
      <Pagination page={numero} />
    </>
  );
}
```

## 6.9 Exécuter du code **après** la réponse : `after()`

Pour la journalisation, les statistiques ou les notifications **sans retarder** la réponse :

```tsx
import { after } from "next/server";

export default async function Page() {
  after(() => {
    enregistrerVisite(); // s'exécute après l'envoi de la réponse
  });
  return <h1>Bonjour</h1>;
}
```

Utilisable dans Server Components, Server Actions, Route Handlers, Proxy. (Stable depuis Next.js 15.1.)

## 6.10 Gestion des erreurs de données

| Situation | Stratégie |
|---|---|
| Ressource absente | `notFound()` |
| Erreur inattendue | Laisser remonter l'exception → `error.tsx` |
| Erreur attendue (Server Action) | Retourner `{ error: "..." }` |
| Échec partiel d'un composant | Isoler avec `Suspense` + `error.tsx` de segment / slot |
| Réseau lent | Délai d'expiration (`AbortSignal.timeout(5000)`) |

```ts
const res = await fetch(url, { signal: AbortSignal.timeout(5000) });
```

## 6.11 Sécurité des données : la couche d'accès (DAL)

Principes :

- **Centraliser** l'accès aux données dans un module `server-only`.
- **Vérifier l'autorisation** dans chaque fonction d'accès, **pas seulement** dans la page ou le proxy.
- Retourner des **DTO** (objets minimaux) et non des enregistrements bruts (évite de fuiter un `passwordHash`).

```ts
// lib/dal.ts
import "server-only";
import { cache } from "react";
import { verifySession } from "./session";

export const getProfil = cache(async () => {
  const session = await verifySession();         // redirige si non connecté
  const user = await db.user.findUnique({ where: { id: session.userId } });
  return { id: user!.id, nom: user!.nom };       // DTO
});
```

## Pièges courants

- **Cascades involontaires** : `await` en série de requêtes indépendantes.
- **Fetch côté client « par réflexe »** alors qu'un Server Component suffit.
- **Utiliser `cookies()`/`headers()` sans le savoir** : toute la route devient dynamique.
- **Oublier de gérer `res.ok`** : `fetch` ne lève **pas** d'exception sur un 404/500.
- **Retourner des objets entiers de la base de données** au client.

## À retenir

- Les Server Components chargent les données directement, de façon `async`.
- `React.cache` déduplique les accès sans `fetch` ; `Promise.all` parallélise.
- `Suspense` + streaming réduisent le temps d'affichage perçu.
- Les API de requête (`cookies`, `headers`, `searchParams`) sont asynchrones et rendent le rendu dynamique.
- Sécurisez via une DAL et des DTO.

## Exercices

1. Chargez une liste depuis une API publique dans un Server Component, avec gestion d'erreur.
2. Écrivez deux composants indépendants avec `Suspense` et comparez le temps d'affichage à un `await` séquentiel.
3. Créez une page de produits paginée et filtrable via `searchParams`.
4. Implémentez `getProfil()` avec `React.cache`, `server-only` et un DTO.

---

# Chapitre 7 — Mise en cache (Caching)

## Objectifs

- Comprendre pourquoi et où Next.js met des choses en cache.
- Maîtriser le modèle **Cache Components** (`"use cache"`, `cacheLife`, `cacheTag`).
- Utiliser les API de **revalidation** (`revalidateTag`, `updateTag`, `refresh`, `revalidatePath`).
- Comprendre le modèle **classique** (Next.js ≤ 15, ou `cacheComponents` désactivé) pour maintenir du code existant.

> ⚠️ **Version.** Le cache est **le sujet qui a le plus évolué** : Next.js 13/14 mettait beaucoup de choses en cache **implicitement** ; Next.js 15 a supprimé la plupart des caches par défaut ; **Next.js 16 introduit un modèle explicite : Cache Components**. Ce chapitre présente les deux, en commençant par le modèle récent.

## 7.1 Pourquoi mettre en cache ?

Le cache évite de **refaire un travail coûteux** (requête de base de données, appel d'API, rendu d'un composant) lorsque le résultat n'a pas changé. Bénéfices : **rapidité**, **moindre charge**, **coût réduit**. Risque : **servir des données périmées** (*stale*). Toute stratégie de cache consiste donc à décider :

1. **Quoi** mettre en cache ?
2. **Pendant combien de temps** ?
3. **Comment invalider** quand les données changent ?

### Vocabulaire

| Terme | Définition |
|---|---|
| **Cache hit / miss** | La donnée est trouvée / absente dans le cache |
| **TTL** (time to live) | Durée de vie d'une entrée |
| **Stale** | Donnée périmée mais encore servable |
| **Stale-while-revalidate (SWR)** | Servir la donnée périmée immédiatement, la rafraîchir en arrière-plan |
| **Revalidation** | Mise à jour d'une entrée de cache |
| **Invalidation** | Marquer une entrée comme périmée |
| **Mémoïsation** | Réutiliser un résultat pendant un temps très court (ici : une requête de rendu) |

## 7.2 Le modèle Cache Components (Next.js 16)

### Principe

Avec **Cache Components**, le comportement par défaut est : **le code s'exécute à la requête (dynamique)**. Vous **choisissez explicitement** ce qui est mis en cache avec la directive **`"use cache"`**. Le résultat : une page peut mélanger, **dans la même route**, une **coque statique** (pré-rendue, servie instantanément), des **îlots mis en cache** et des **zones dynamiques** diffusées en streaming. Ce modèle s'appuie sur le *Partial Prerendering (PPR)* et le remplace comme option expérimentale.

### Activation

```ts
// next.config.ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  cacheComponents: true,
};

export default nextConfig;
```

### Les trois catégories de contenu

Avec Cache Components, chaque morceau de rendu relève de l'une de ces catégories :

| Catégorie | Exemple | Comportement |
|---|---|---|
| **Statique** (déterministe) | JSX pur, calculs purs, imports de modules, lecture de fichier au build | **Inclus dans la coque statique** au build |
| **Mis en cache** (`"use cache"`) | Données d'API, requêtes de catalogue | Calculé, **stocké**, réutilisé ; inclus dans la coque si possible |
| **Dynamique** | `cookies()`, `headers()`, `searchParams`, fetch non mis en cache, `Math.random()`/`Date.now()` | **Calculé à chaque requête**, doit être **enveloppé dans `<Suspense>`** |

> **Règle de sécurité du framework :** si Next.js détecte, au rendu, un accès à des données dynamiques **hors d'une frontière `<Suspense>`** et hors d'un `"use cache"`, il **signale une erreur** (message du type « *Uncached data was accessed outside of `<Suspense>`* »). Vous devez alors : (1) mettre en cache la donnée avec `"use cache"`, ou (2) envelopper le composant dans `<Suspense>` avec un *fallback*. Cela force à **décider explicitement** du comportement.

### Exemple complet

```tsx
// app/produits/page.tsx
import { Suspense } from "react";
import { cacheLife, cacheTag } from "next/cache";
import { cookies } from "next/headers";

async function Catalogue() {
  "use cache";
  cacheLife("hours");          // profil de durée
  cacheTag("catalogue");       // étiquette pour l'invalidation

  const produits = await db.produit.findMany();
  return (
    <ul>
      {produits.map((p) => <li key={p.id}>{p.nom}</li>)}
    </ul>
  );
}

async function Bienvenue() {
  const nom = (await cookies()).get("nom")?.value ?? "invité";  // dynamique
  return <p>Bonjour {nom}</p>;
}

export default function Page() {
  return (
    <>
      <h1>Produits</h1>                       {/* statique : dans la coque */}
      <Suspense fallback={<p>…</p>}>
        <Bienvenue />                         {/* dynamique : streaming */}
      </Suspense>
      <Catalogue />                           {/* mis en cache */}
    </>
  );
}
```

## 7.3 La directive `"use cache"`

### Où la placer ?

- **En haut d'un fichier** : tout ce que le module exporte (composants, fonctions asynchrones) est mis en cache.
- **Au début d'un composant asynchrone** ou **d'une fonction asynchrone**.

```ts
// Niveau fonction
export async function getArticles() {
  "use cache";
  return db.article.findMany();
}
```

```tsx
// Niveau fichier
"use cache";
export default async function Page() { /* ... */ }
```

### Comment la clé de cache est-elle calculée ?

La clé combine : l'**identifiant de la fonction**, ses **arguments sérialisables**, les **valeurs capturées par fermeture** (closures) qui sont sérialisables, et le **build**. Deux appels avec les mêmes arguments partagent l'entrée ; des arguments différents produisent des entrées différentes.

```ts
async function getProduit(id: string) {
  "use cache";
  cacheTag(`produit-${id}`);
  return db.produit.findUnique({ where: { id } }); // une entrée par id
}
```

### Règles et limites

1. **Arguments et valeurs de retour sérialisables** (types primitifs, objets simples, tableaux, `Date`, `Map`, `Set`, éléments JSX, etc.). Les fonctions et instances de classe ne le sont pas.
2. **Pas d'API de requête à l'intérieur** : `cookies()`, `headers()`, `searchParams` ne peuvent pas être lus **dans** un contexte `"use cache"` (le résultat dépendrait de la requête). **Lisez-les à l'extérieur** et passez les valeurs **en arguments** :

```tsx
export default async function Page() {
  const lang = (await cookies()).get("lang")?.value ?? "fr";   // dynamique, dehors
  return (
    <Suspense fallback={null}>
      <Contenu lang={lang} />
    </Suspense>
  );
}

async function Contenu({ lang }: { lang: string }) {
  "use cache";                                 // la clé inclut `lang`
  return <p>{await traduire(lang)}</p>;
}
```

3. **Les `children` et les props de type JSX** peuvent traverser un composant mis en cache sans être lus (**pass-through**) : un composant en cache peut envelopper du contenu dynamique placé par le parent.
4. Les **Server Actions** passées en props peuvent être transmises sans être exécutées dans le cache.
5. **`Date.now()`, `Math.random()`, `crypto.randomUUID()`** : dans un contexte de cache, la valeur est **figée** avec l'entrée. Hors cache et hors `connection()`, Next.js signale ces appels pour éviter des pages « statiques » aux valeurs surprenantes.

### Variantes avancées

| Directive | Usage |
|---|---|
| `"use cache"` | Cache par défaut, partagé côté serveur |
| `"use cache: private"` | Autorise la lecture de `cookies()`/`headers()` dans le périmètre ; mis en cache **uniquement dans la mémoire du navigateur** de l'utilisateur (données personnalisées) |
| `"use cache: remote"` | Utilise un **cache distant partagé** (handler de cache dédié) dans des contextes dynamiques ; utile en serverless |

Ces variantes sont plus récentes et spécialisées : consultez la documentation de votre version avant de les adopter.

## 7.4 `cacheLife` : la durée de vie

```ts
import { cacheLife } from "next/cache";
```

### Trois paramètres de temps

| Propriété | Signification |
|---|---|
| **`stale`** | Durée pendant laquelle le **client** peut utiliser la valeur sans demander au serveur |
| **`revalidate`** | Après ce délai, la valeur est considérée périmée côté serveur : elle est servie une dernière fois (SWR) **et régénérée en arrière-plan** |
| **`expire`** | Après ce délai sans trafic, l'entrée est **supprimée** : la prochaine requête est **bloquante** (régénération synchrone) |

Contrainte : `stale` ≤ `revalidate` ≤ `expire`.

### Profils prédéfinis

`"seconds"`, `"minutes"`, `"hours"`, `"days"`, `"weeks"`, `"max"` (et un profil par défaut si on n'appelle pas `cacheLife`). Les durées exactes sont définies par le framework (par exemple « hours » ≈ revalidation toutes les heures ; « days » ≈ chaque jour ; « max » ≈ très long) ; vérifiez le tableau de la documentation pour les valeurs précises de votre version.

```ts
async function getActualites() {
  "use cache";
  cacheLife("minutes");
  /* ... */
}
```

### Durées personnalisées

Inline :

```ts
cacheLife({ stale: 60, revalidate: 300, expire: 3600 }); // en secondes
```

Profils nommés dans la configuration :

```ts
// next.config.ts
const nextConfig = {
  cacheComponents: true,
  cacheLife: {
    editorial: { stale: 300, revalidate: 900, expire: 86400 },
  },
};
```

```ts
cacheLife("editorial");
```

## 7.5 `cacheTag` : étiqueter pour invalider

```ts
import { cacheTag } from "next/cache";

async function getPosts() {
  "use cache";
  cacheTag("posts");
  return db.post.findMany();
}
```

Plusieurs étiquettes possibles : `cacheTag("posts", "homepage")`. On invalide ensuite **toutes les entrées portant cette étiquette**, quel que soit l'endroit où elles sont utilisées.

## 7.6 Revalidation et invalidation

Toutes ces fonctions viennent de **`next/cache`**.

### `revalidateTag(tag, profil)` — stale-while-revalidate

```ts
import { revalidateTag } from "next/cache";

revalidateTag("posts", "max");
```

- Marque les entrées comme périmées ; **sert la valeur périmée immédiatement** puis régénère **en arrière-plan** (SWR).
- ⚠️ **Version 16** : le **second argument** (profil de cache, par exemple `"max"`, `"hours"` ou un objet `{ expire: ... }`) est **requis** ; la forme à un seul argument est dépréciée. `"max"` est généralement recommandé.
- Utilisable dans les **Server Actions** et **Route Handlers**.

### `updateTag(tag)` — « lire ses propres écritures »

```ts
"use server";
import { updateTag } from "next/cache";

export async function creerPost(formData: FormData) {
  await db.post.create({ data: { titre: String(formData.get("titre")) } });
  updateTag("posts");        // expire immédiatement ET rafraîchit dans la même requête
}
```

- **Uniquement dans les Server Actions.**
- Invalide **immédiatement** : l'utilisateur qui vient de muter voit **sa donnée à jour** dans la même navigation (*read-your-writes*), contrairement à `revalidateTag` (SWR).

### `refresh()` — rafraîchir ce qui n'est pas en cache

```ts
"use server";
import { refresh } from "next/cache";

export async function marquerLu(id: string) {
  await db.notification.update({ where: { id }, data: { lu: true } });
  refresh();   // re-rend la route courante (données non mises en cache, compteurs, etc.)
}
```

- **Uniquement dans les Server Actions.** Ne touche **pas** au cache : il rafraîchit le routeur côté client et les données dynamiques.

### `revalidatePath(chemin, type?)`

```ts
import { revalidatePath } from "next/cache";

revalidatePath("/blog");                     // une page
revalidatePath("/blog/[slug]", "page");      // un motif de route dynamique
revalidatePath("/blog", "layout");           // un layout et ses enfants
revalidatePath("/", "layout");               // tout le site
```

Invalide le cache **associé à un chemin** (rendu de la route). Plus grossier que les tags.

### Quel outil choisir ?

| Besoin | Outil |
|---|---|
| L'auteur doit voir immédiatement son changement | `updateTag` |
| Contenu partagé, fraîcheur « raisonnable » | `revalidateTag(tag, "max")` |
| Rafraîchir de l'UI non mise en cache | `refresh()` |
| Invalider une page entière | `revalidatePath` |
| Depuis un webhook (CMS) | `revalidateTag` dans un Route Handler |

### Revalidation à la demande depuis un webhook

```ts
// app/api/revalidate/route.ts
import { revalidateTag } from "next/cache";
import { NextResponse } from "next/server";

export async function POST(request: Request) {
  const secret = request.headers.get("x-webhook-secret");
  if (secret !== process.env.REVALIDATE_SECRET) {
    return NextResponse.json({ ok: false }, { status: 401 });
  }
  const { tag } = await request.json();
  revalidateTag(tag, "max");
  return NextResponse.json({ ok: true });
}
```

## 7.7 Ce que Cache Components change pour les anciennes options

Avec `cacheComponents: true` :

- `experimental.ppr` et `experimental.dynamicIO` sont **supprimés** (fusionnés dans Cache Components).
- Les **options de segment** `export const dynamic`, `export const revalidate`, `export const fetchCache`, `export const dynamicParams` (selon cas) et `runtime = "edge"` ne sont **pas supportées** dans ce mode : on les remplace par `"use cache"`, `cacheLife`, `Suspense`, `connection()`.
- `unstable_cache` est remplacé par `"use cache"` ; `unstable_cacheLife` et `unstable_cacheTag` deviennent **`cacheLife`** et **`cacheTag`** (stables).
- L'option `fetch(..., { cache: "force-cache" })` n'est plus le mécanisme recommandé pour piloter le cache : on met en cache **la fonction ou le composant** qui encapsule le `fetch`.

## 7.8 Le modèle classique (Next.js ≤ 15, ou sans Cache Components)

Utile pour comprendre et maintenir du code existant.

### Les quatre mécanismes historiques

| Mécanisme | Où | Contenu | Durée |
|---|---|---|---|
| **Request Memoization** | Serveur | Résultats des `fetch` GET identiques | Une requête de rendu |
| **Data Cache** | Serveur | Réponses de `fetch` | Persistant (jusqu'à revalidation) |
| **Full Route Cache** | Serveur | HTML + payload RSC des routes **statiques** | Persistant (jusqu'à revalidation/redéploiement) |
| **Router Cache** | Client | Payload RSC des segments visités/préchargés | Session ou durée limitée |

### Options de `fetch`

```ts
fetch(url, { cache: "force-cache" });             // met en cache (Data Cache)
fetch(url, { cache: "no-store" });                // jamais en cache
fetch(url, { next: { revalidate: 3600 } });       // revalidation temporelle (ISR-like)
fetch(url, { next: { tags: ["posts"] } });        // étiquette pour revalidateTag
```

> ⚠️ **Version 15** : sans option, `fetch` n'est **pas** mis en cache. Les Route Handlers `GET` ne sont plus mis en cache par défaut (`export const dynamic = "force-static"` pour l'activer). Le Router Cache ne conserve plus par défaut les segments **page** (`staleTime = 0`) ; layouts et états de chargement restent partagés.

### Options de segment (historique)

```ts
export const dynamic = "auto" | "force-dynamic" | "force-static" | "error";
export const revalidate = false | 0 | number;   // secondes
export const fetchCache = "auto" | "default-cache" | "only-cache" | "force-cache" | "force-no-cache" | "default-no-store" | "only-no-store";
export const dynamicParams = true | false;
export const runtime = "nodejs" | "edge";
export const preferredRegion = "auto" | "home" | "global" | string | string[];
export const maxDuration = 30;                  // plateformes supportées
```

### `unstable_cache` (pour ORM/SDK)

```ts
import { unstable_cache } from "next/cache";

const getUtilisateurs = unstable_cache(
  async () => db.user.findMany(),
  ["utilisateurs"],                       // clé
  { revalidate: 3600, tags: ["users"] }
);
```

### Router Cache : ajuster `staleTimes` (expérimental)

```ts
// next.config.ts
const nextConfig = {
  experimental: { staleTimes: { dynamic: 30, static: 180 } },
};
```

Le routeur côté client peut aussi être rafraîchi avec `router.refresh()`.

## 7.9 Cache du navigateur et en-têtes HTTP

En complément du cache de Next.js, les **en-têtes `Cache-Control`** pilotent les caches du navigateur et des CDN :

- Fichiers statiques de `_next/static/` : **immutables**, longue durée (noms hachés).
- Images optimisées : `images.minimumCacheTTL` (⚠️ défaut de 4 heures en Next.js 16).
- Pages : `s-maxage` et `stale-while-revalidate` ajoutés automatiquement pour ISR sur certaines plateformes ; personnalisables via `headers()` dans `next.config`.

## 7.10 Auto-hébergement et cache partagé

Par défaut, le cache est **local au processus/serveur** (mémoire + disque `.next/`). En **multi-instances** (plusieurs conteneurs, Kubernetes), chaque instance a son propre cache : la revalidation n'est pas partagée. Solutions : **handler de cache personnalisé** (`cacheHandler`, `cacheHandlers` pour Cache Components) branché sur Redis/S3, ou une plateforme qui fournit un cache partagé.

## 7.11 Cache et sécurité

- **Ne mettez jamais en cache des données propres à un utilisateur** dans un cache **partagé** : la fuite entre utilisateurs est le risque principal. Avec `"use cache"`, **lisez les cookies/headers à l'extérieur** et incluez l'identifiant dans les arguments, ou utilisez `"use cache: private"`.
- Un cache mal configuré derrière un CDN peut servir une page personnalisée à un autre visiteur : vérifiez les en-têtes `Vary`/`Cache-Control`.

## Pièges courants

- **Oublier d'invalider** après une mutation → l'utilisateur voit des données obsolètes.
- **Mettre en cache une fonction qui lit des cookies** : erreur ou fuite entre utilisateurs.
- **Confondre `revalidateTag` (SWR) et `updateTag` (immédiat)**.
- **Appeler `updateTag`/`refresh` hors d'une Server Action** : non autorisé.
- **Mélanger options de segment (`dynamic`, `revalidate`) et Cache Components** : incompatible.
- **Penser que le mode développement reflète la production** : testez avec `build` + `start`.

## À retenir

- **Next.js 16 : dynamique par défaut, cache explicite avec `"use cache"`.**
- `cacheLife` règle `stale` / `revalidate` / `expire` ; `cacheTag` étiquette.
- `updateTag` (immédiat, Server Actions) ≠ `revalidateTag` (SWR) ≠ `refresh` (non-cache).
- Le modèle classique reste utile pour le code existant (`fetch` options, ISR, `unstable_cache`).

## Exercices

1. Activez `cacheComponents`, mettez en cache une liste avec `"use cache"` + `cacheLife("minutes")` + `cacheTag("liste")`.
2. Ajoutez un formulaire qui crée un élément et appelle `updateTag("liste")` ; vérifiez la mise à jour immédiate.
3. Créez un webhook `POST /api/revalidate` protégé par un secret qui appelle `revalidateTag`.
4. Provoquez l'erreur « accès dynamique hors Suspense » puis corrigez-la de deux façons.

---

# Chapitre 8 — Stratégies de rendu : SSR, SSG, ISR, PPR, CSR

## Objectifs

- Définir précisément chaque stratégie de rendu.
- Savoir comment Next.js décide qu'une route est statique ou dynamique.
- Choisir la stratégie adaptée à un cas d'usage.
- Comprendre les métriques de performance (Core Web Vitals).

## 8.1 Définitions

| Stratégie | Quand le HTML est-il produit ? | Où ? | Idéal pour |
|---|---|---|---|
| **SSG** — Static Site Generation | **Au build** | Machine de build | Blogs, docs, pages marketing |
| **SSR** — Server-Side Rendering | **À chaque requête** | Serveur | Contenu personnalisé ou toujours frais |
| **ISR** — Incremental Static Regeneration | Au build **puis régénéré** (délai ou événement) | Serveur | Catalogues, actualités |
| **CSR** — Client-Side Rendering | **Dans le navigateur** | Client | Zones très interactives, tableaux de bord privés |
| **Streaming** | Progressivement, par morceaux | Serveur → client | Pages avec zones lentes |
| **PPR** — Partial Prerendering (maintenant via Cache Components) | Coque au build + trous dynamiques à la requête | Mixte | La plupart des pages modernes |

### SSG

Le HTML est **calculé une fois** puis servi comme un fichier (idéalement par un **CDN**). Très rapide, peu coûteux. Limite : les données sont figées jusqu'au prochain build (sauf ISR).

### SSR

Le HTML est **généré à chaque requête** : données toujours fraîches et personnalisables (cookies, en-têtes). Coût : latence serveur, charge, TTFB plus élevé.

### ISR

Page statique **régénérée en arrière-plan** :

- **Temporelle** : toutes les *n* secondes (modèle classique : `revalidate`) ; avec Cache Components : `cacheLife`.
- **À la demande** : `revalidateTag`, `revalidatePath`, `updateTag`.
- Comportement SWR : un visiteur reçoit la version existante ; la régénération se produit en arrière-plan ; les suivants reçoivent la nouvelle.

### CSR

Le serveur envoie un squelette ; le navigateur charge les données (SWR/TanStack Query). Convient aux zones **derrière authentification** sans besoin de SEO, ou très interactives.

### PPR → Cache Components

Une **même route** combine :

1. une **coque statique** (layout, titres, navigation, éléments en cache) servie instantanément depuis un CDN ;
2. des **trous dynamiques** (`Suspense`) remplis en streaming depuis le serveur.

C'est le modèle recommandé de Next.js 16 (voir chapitre 7).

## 8.2 Comment Next.js choisit : statique ou dynamique ?

### Modèle classique (sans Cache Components)

Une route est **statique par défaut** et devient **dynamique** quand elle utilise :

- `cookies()`, `headers()`, `draftMode()` (dans leurs formes actuelles asynchrones),
- `searchParams` (props de page),
- `connection()`,
- un `fetch` avec `cache: "no-store"` ou `revalidate: 0`,
- `export const dynamic = "force-dynamic"`,
- un Route Handler avec méthode non-GET ou utilisant l'objet `Request` dynamiquement.

### Avec Cache Components

Tout ce qui est **dynamique** doit être sous **`<Suspense>`** (ou mis en cache avec `"use cache"`). Ce qui est déterministe et mis en cache est inclus dans la **coque statique**. Le tableau des routes affiché par `next build` indique alors, par exemple, les routes **partiellement pré-rendues**.

## 8.3 Pré-génération de routes dynamiques

`generateStaticParams` (chapitre 3) génère au build les pages d'une route dynamique. Stratégie courante : **pré-générer les pages les plus visitées** (liste courte) et laisser les autres être générées **à la demande** puis mises en cache.

## 8.4 Runtimes d'exécution

| Runtime | Description | Remarques |
|---|---|---|
| **Node.js** | Par défaut ; accès complet aux API Node | Recommandé |
| **Edge** | Environnement léger (API Web), démarrage très rapide, déploiement proche de l'utilisateur | API limitées ; ⚠️ non supporté avec Cache Components ; le **Proxy** de Next.js 16 s'exécute sur **Node.js** |

```ts
export const runtime = "nodejs"; // (modèle classique) ou "edge" pour un Route Handler/une page concernée
```

## 8.5 Core Web Vitals : mesurer le résultat

| Métrique | Définition | Seuil « bon » |
|---|---|---|
| **TTFB** (Time To First Byte) | Délai avant le premier octet reçu | < 0,8 s |
| **FCP** (First Contentful Paint) | Premier contenu affiché | < 1,8 s |
| **LCP** (Largest Contentful Paint) | Affichage du plus grand élément visible | < 2,5 s |
| **INP** (Interaction to Next Paint) | Réactivité aux interactions (remplace FID) | < 200 ms |
| **CLS** (Cumulative Layout Shift) | Stabilité visuelle (décalages) | < 0,1 |

Mesure dans Next.js :

```tsx
"use client";
import { useReportWebVitals } from "next/web-vitals";

export function WebVitals() {
  useReportWebVitals((metric) => {
    console.log(metric); // envoyer vers votre outil d'analyse
  });
  return null;
}
```

## 8.6 Guide de décision

| Contenu | Stratégie conseillée |
|---|---|
| Page statique (À propos, docs) | SSG / coque statique |
| Articles de blog | SSG + `generateStaticParams`, revalidation via CMS |
| Catalogue produit | `"use cache"` + `cacheLife` + `cacheTag`, invalidation par webhook |
| Page produit + stock en temps réel | Coque en cache + stock en `Suspense` dynamique |
| Tableau de bord utilisateur | Dynamique (cookies) avec streaming ; éventuellement CSR pour les widgets |
| Recherche | Dynamique (`searchParams`) ou CSR avec SWR |
| Contenu très personnalisé | SSR / `Suspense` |

## 8.7 Export statique

```ts
// next.config.ts
const nextConfig = { output: "export" };
export default nextConfig;
```

Génère un dossier `out/` de fichiers HTML/CSS/JS à héberger sur n'importe quel serveur statique. **Limites** : pas de Server Actions, pas de Route Handlers dynamiques, pas de Proxy, pas de rendu dynamique, pas d'optimisation d'images par défaut (loader personnalisé nécessaire), pas d'ISR.

## Pièges courants

- **Croire qu'une page est statique** alors qu'un composant lit `cookies()` ou `searchParams`.
- **Ne pas lire le tableau de build** pour vérifier le mode de rendu.
- **SSR partout « par défaut »** : coût inutile quand le cache suffit.
- **CSR partout** : perte de SEO et de performance perçue.

## À retenir

- SSG = au build ; SSR = à la requête ; ISR = statique régénéré ; CSR = navigateur ; PPR/Cache Components = coque statique + trous dynamiques.
- Le caractère statique/dynamique découle de **ce que vos composants utilisent**.
- Mesurez avec les Core Web Vitals.

## Exercices

1. Créez trois pages : une statique, une qui lit `cookies()`, une avec `generateStaticParams`. Comparez le tableau de `next build`.
2. Construisez une page produit avec coque en cache + stock dynamique en `Suspense`.
3. Ajoutez `useReportWebVitals` et observez les métriques en local.

---

# Chapitre 9 — Server Actions et mutations

## Objectifs

- Définir et appeler des Server Actions (formulaires et événements).
- Gérer validation, erreurs, états de chargement et mises à jour optimistes.
- Revalider le cache et rediriger après une mutation.
- Sécuriser les actions.

## 9.1 Définition

Une **Server Action** (plus largement, une **Server Function**) est une **fonction asynchrone exécutée sur le serveur**, appelable depuis le client. Elle sert aux **mutations** (créer, modifier, supprimer) et à tout traitement qui ne doit pas s'exécuter dans le navigateur.

> **Terminologie.** *Server Function* : toute fonction serveur appelable par le client. *Server Action* : une Server Function utilisée comme **action** (passée à `<form action>` ou appelée dans une transition), généralement pour une mutation.

### Fonctionnement technique

- Next.js génère un **identifiant** pour chaque action et un **endpoint** interne ; l'appel est une requête **`POST`** envoyée au serveur.
- Les **arguments** et le **résultat** sont sérialisés.
- Les actions ne sont pas appelées en parallèle : Next.js les traite **l'une après l'autre** (file d'attente) pour un même client.
- Les variables capturées par fermeture sont **chiffrées** ; les actions **non utilisées** sont éliminées du build.

## 9.2 Créer une Server Action

### Option 1 : dans un fichier dédié (recommandé)

```ts
// app/actions.ts
"use server";   // toutes les fonctions exportées sont des Server Actions

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";

export async function creerPost(formData: FormData) {
  const titre = String(formData.get("titre") ?? "");
  await db.post.create({ data: { titre } });
  revalidatePath("/blog");
  redirect("/blog");
}
```

### Option 2 : directive en ligne dans un Server Component

```tsx
export default function Page() {
  async function supprimer(formData: FormData) {
    "use server";
    await db.post.delete({ where: { id: String(formData.get("id")) } });
  }
  return (
    <form action={supprimer}>
      <input type="hidden" name="id" value="42" />
      <button>Supprimer</button>
    </form>
  );
}
```

> Dans un **Client Component**, on **ne peut pas** définir une action en ligne : il faut l'**importer** depuis un fichier `"use server"`.

## 9.3 Utilisation dans un formulaire

Passer l'action à l'attribut **`action`** de `<form>` :

```tsx
import { creerPost } from "./actions";

export default function Formulaire() {
  return (
    <form action={creerPost}>
      <input name="titre" required />
      <textarea name="contenu" />
      <button type="submit">Publier</button>
    </form>
  );
}
```

- L'action reçoit un objet **`FormData`** natif.
- **Amélioration progressive** : dans un Server Component, le formulaire **fonctionne même sans JavaScript** (soumission HTML classique) ; après hydratation, il est envoyé sans rechargement.
- Lire les champs : `formData.get("nom")`, `formData.getAll("tags")`, `Object.fromEntries(formData)`.

## 9.4 Passer des arguments supplémentaires : `bind`

```tsx
import { supprimerPost } from "./actions";

export function BoutonSupprimer({ id }: { id: string }) {
  const supprimerAvecId = supprimerPost.bind(null, id); // 1er argument lié
  return (
    <form action={supprimerAvecId}>
      <button>Supprimer</button>
    </form>
  );
}
```

```ts
export async function supprimerPost(id: string, formData: FormData) { /* ... */ }
```

## 9.5 Appels depuis des Client Components

### Depuis un gestionnaire d'événement

```tsx
"use client";
import { useTransition } from "react";
import { aimer } from "./actions";

export function Like({ id }: { id: string }) {
  const [pending, startTransition] = useTransition();
  return (
    <button
      disabled={pending}
      onClick={() => startTransition(async () => { await aimer(id); })}
    >
      {pending ? "…" : "J'aime"}
    </button>
  );
}
```

### Depuis `useEffect`

Possible, mais à réserver aux cas particuliers (par exemple compteur de vues).

## 9.6 État du formulaire : `useActionState`

```tsx
"use client";
import { useActionState } from "react";
import { inscrire } from "./actions";

type Etat = { erreurs?: { email?: string[] }; message?: string } | null;

export default function Inscription() {
  const [etat, action, pending] = useActionState<Etat, FormData>(inscrire, null);

  return (
    <form action={action}>
      <input name="email" type="email" aria-invalid={!!etat?.erreurs?.email} />
      {etat?.erreurs?.email && <p role="alert">{etat.erreurs.email[0]}</p>}
      <button disabled={pending}>{pending ? "Envoi…" : "S'inscrire"}</button>
      {etat?.message && <p>{etat.message}</p>}
    </form>
  );
}
```

L'action reçoit **l'état précédent** en premier argument :

```ts
// actions.ts
"use server";
import { z } from "zod";

const schema = z.object({ email: z.string().email("Email invalide") });

export async function inscrire(prev: unknown, formData: FormData) {
  const resultat = schema.safeParse({ email: formData.get("email") });
  if (!resultat.success) {
    return { erreurs: resultat.error.flatten().fieldErrors };
  }
  await db.inscrit.create({ data: { email: resultat.data.email } });
  return { message: "Inscription réussie !" };
}
```

`useActionState` retourne `[état, actionEnveloppée, enCours]`.

## 9.7 Indicateur de chargement : `useFormStatus`

```tsx
"use client";
import { useFormStatus } from "react-dom";

export function BoutonEnvoyer() {
  const { pending } = useFormStatus();
  return <button disabled={pending}>{pending ? "Envoi…" : "Envoyer"}</button>;
}
```

⚠️ `useFormStatus` doit être appelé dans un composant **enfant** du `<form>`, pas dans le composant qui rend le `<form>`.

## 9.8 Mises à jour optimistes : `useOptimistic`

Afficher immédiatement le résultat attendu, puis le réconcilier avec la réponse serveur.

```tsx
"use client";
import { useOptimistic } from "react";
import { ajouterTache } from "./actions";

export function Taches({ taches }: { taches: { id: string; titre: string }[] }) {
  const [optimistes, ajouterOptimiste] = useOptimistic(
    taches,
    (etat, titre: string) => [...etat, { id: "temp", titre }]
  );

  async function action(formData: FormData) {
    const titre = String(formData.get("titre"));
    ajouterOptimiste(titre);          // mise à jour immédiate de l'UI
    await ajouterTache(titre);        // vraie mutation
  }

  return (
    <>
      <ul>{optimistes.map((t) => <li key={t.id}>{t.titre}</li>)}</ul>
      <form action={action}><input name="titre" /><button>Ajouter</button></form>
    </>
  );
}
```

En cas d'échec, l'état revient automatiquement à la valeur réelle.

## 9.9 Validation des données

**Ne faites jamais confiance au client.** Validez **toujours côté serveur** (schémas **Zod**, Valibot, ArkType…), même si le formulaire valide déjà côté client (la validation client n'est qu'un confort).

```ts
const Schema = z.object({
  titre: z.string().min(3).max(120),
  prix: z.coerce.number().positive(),     // coerce : FormData envoie des chaînes
  tags: z.array(z.string()).max(5).default([]),
});

const parsed = Schema.safeParse({
  titre: formData.get("titre"),
  prix: formData.get("prix"),
  tags: formData.getAll("tags"),
});
```

## 9.10 Gestion des erreurs

| Type | Traitement |
|---|---|
| **Erreurs attendues** (validation, email déjà pris, droits insuffisants) | **Retourner** un objet d'erreur (`{ erreur: "..." }`) |
| **Erreurs inattendues** (bug, base indisponible) | Laisser **l'exception** remonter : `error.tsx` l'attrape |

Évitez `throw` pour les erreurs de validation : l'utilisateur perdrait la saisie du formulaire.

## 9.11 Revalider, rafraîchir, rediriger

```ts
"use server";
import { updateTag, revalidatePath, refresh } from "next/cache";
import { redirect } from "next/navigation";

export async function modifierPost(id: string, data: FormData) {
  await db.post.update({ where: { id }, data: { titre: String(data.get("titre")) } });

  updateTag("posts");            // lecture immédiate des données à jour (Next.js 16)
  // ou revalidateTag("posts", "max"); revalidatePath("/blog"); refresh();

  redirect(`/blog/${id}`);       // en dernier : lève une exception interne
}
```

⚠️ **`redirect()` doit venir après** la revalidation et **hors `try/catch`**.

## 9.12 Cookies dans les actions

```ts
"use server";
import { cookies } from "next/headers";

export async function choisirTheme(theme: "clair" | "sombre") {
  const store = await cookies();
  store.set("theme", theme, { httpOnly: true, secure: true, sameSite: "lax", path: "/", maxAge: 60 * 60 * 24 * 365 });
}
```

Les Server Actions et Route Handlers sont les **seuls** endroits où l'on peut **écrire** des cookies côté serveur.

## 9.13 Téléversement de fichiers

```ts
"use server";
export async function televerser(formData: FormData) {
  const fichier = formData.get("fichier") as File;
  if (!fichier || fichier.size === 0) return { erreur: "Aucun fichier" };
  if (fichier.size > 2 * 1024 * 1024) return { erreur: "Fichier trop volumineux" };
  if (!["image/png", "image/jpeg"].includes(fichier.type)) return { erreur: "Type refusé" };
  const octets = Buffer.from(await fichier.arrayBuffer());
  // enregistrer dans un stockage objet (S3, etc.)
}
```

Formulaire : `<form action={televerser}><input type="file" name="fichier" /></form>`.
La limite de taille de corps des actions est de **1 Mo par défaut** ; ajustez :

```ts
// next.config.ts
const nextConfig = { experimental: { serverActions: { bodySizeLimit: "5mb" } } };
```

Pour de gros fichiers : **URL pré-signées** pour téléverser directement vers le stockage.

## 9.14 Le composant `<Form>` de `next/form`

```tsx
import Form from "next/form";

export default function Recherche() {
  return (
    <Form action="/recherche">
      <input name="q" />
      <button>Chercher</button>
    </Form>
  );
}
```

Pour les formulaires de **recherche (GET)** : navigation **côté client** avec préchargement de l'UI de chargement et conservation de l'état des layouts, et **amélioration progressive**.

## 9.15 Sécurité des Server Actions

Les Server Actions sont des **endpoints HTTP publics**. Appliquez la même rigueur qu'à une API :

1. **Authentification et autorisation** dans **chaque** action (vérifier la session et les droits à l'intérieur de l'action).
2. **Validation** des entrées (types, tailles, formats).
3. **Protection CSRF** : Next.js n'accepte que `POST` et compare les en-têtes `Origin` et `Host` ; autorisez des domaines additionnels avec `serverActions.allowedOrigins` si nécessaire (reverse proxy).
4. **Chiffrement** des variables capturées par fermeture (clé configurable pour les déploiements multi-instances via `NEXT_SERVER_ACTIONS_ENCRYPTION_KEY`).
5. **Limitation de débit** (rate limiting) pour les actions sensibles (login, envoi d'e-mail).
6. **Ne jamais renvoyer** de données sensibles superflues.
7. Les identifiants d'actions non utilisées ne sont pas exposés, mais **les actions exportées restent appelables** : vérifiez toujours les droits.

## 9.16 Quand préférer un Route Handler ?

| Server Action | Route Handler |
|---|---|
| Mutation déclenchée par **votre** interface | **API publique**, consommée par des clients tiers (mobile, partenaires) |
| Formulaires, amélioration progressive | **Webhooks**, endpoints REST/GraphQL |
| Revalidation intégrée | Réponses non-JSON, streaming, formats personnalisés |

## Pièges courants

- **Oublier l'autorisation** dans l'action (« la page est protégée, donc l'action aussi » : faux).
- **`redirect()` dans un `try/catch`**.
- **Utiliser une action pour **lire** des données** : privilégiez les Server Components (les actions sont mises en file et ne conviennent pas au chargement).
- **`useFormStatus` au mauvais niveau**.
- **Retourner des valeurs non sérialisables**.
- **Valider seulement côté client**.

## À retenir

- `"use server"` + `<form action>` = mutation avec amélioration progressive.
- `useActionState`, `useFormStatus`, `useOptimistic` pour l'UX.
- Après mutation : `updateTag` / `revalidateTag` / `revalidatePath` puis `redirect`.
- **Toujours** valider et autoriser côté serveur.

## Exercices

1. Créez un formulaire de contact avec validation Zod et messages d'erreur via `useActionState`.
2. Ajoutez un bouton « J'aime » avec `useOptimistic`.
3. Créez un formulaire de téléversement avec contrôle de type et de taille.
4. Protégez une action de suppression par un contrôle de rôle.

---

# Chapitre 10 — Route Handlers (API)

## Objectifs

- Créer des endpoints HTTP avec `route.ts`.
- Utiliser `Request`, `NextRequest` et `NextResponse`.
- Gérer paramètres dynamiques, cookies, en-têtes, CORS, streaming et webhooks.

## 10.1 Principe

Un **Route Handler** est défini dans un fichier **`route.ts`** (ou `.js`) à l'intérieur d'`app/`. Il exporte des **fonctions nommées d'après les méthodes HTTP** : `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`. Il s'appuie sur les API Web standard **`Request`** et **`Response`**.

```ts
// app/api/bonjour/route.ts  →  /api/bonjour
export async function GET() {
  return Response.json({ message: "Bonjour" });
}
```

- `OPTIONS` est implémenté automatiquement si vous ne le définissez pas.
- Une méthode non exportée renvoie **405 Method Not Allowed**.
- Un dossier ne peut pas avoir à la fois un `page` et un `route` pour la **même URL**.

## 10.2 Lire la requête

```ts
import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest) {
  const q = request.nextUrl.searchParams.get("q");        // paramètres de requête
  const jeton = request.headers.get("authorization");     // en-têtes
  const session = request.cookies.get("session")?.value;  // cookies
  return NextResponse.json({ q, aSession: !!session });
}

export async function POST(request: Request) {
  const donnees = await request.json();                   // corps JSON
  // autres : await request.formData(), await request.text(), await request.arrayBuffer()
  return NextResponse.json({ recu: donnees }, { status: 201 });
}
```

## 10.3 Segments dynamiques

```ts
// app/api/posts/[id]/route.ts
export async function GET(
  _request: Request,
  { params }: { params: Promise<{ id: string }> }
) {
  const { id } = await params;
  const post = await db.post.findUnique({ where: { id } });
  if (!post) return Response.json({ erreur: "Introuvable" }, { status: 404 });
  return Response.json(post);
}

export async function DELETE(_req: Request, ctx: RouteContext<"/api/posts/[id]">) {
  const { id } = await ctx.params;
  await db.post.delete({ where: { id } });
  return new Response(null, { status: 204 });
}
```

(`RouteContext<...>` est un type helper généré par Next.js ; voir chapitre 20.)

## 10.4 Construire des réponses

```ts
// JSON
return NextResponse.json({ ok: true }, { status: 200, headers: { "X-Custom": "1" } });

// Texte / HTML / autre
return new Response("<h1>Salut</h1>", { headers: { "Content-Type": "text/html; charset=utf-8" } });

// Redirection
return NextResponse.redirect(new URL("/login", request.url));

// Cookies en réponse
const res = NextResponse.json({ ok: true });
res.cookies.set("visite", "1", { httpOnly: true, maxAge: 3600 });
return res;
```

Cookies/headers via les API serveur :

```ts
import { cookies, headers } from "next/headers";
const store = await cookies();
store.set("a", "b");
```

## 10.5 Codes de statut courants

| Code | Sens | Usage |
|---|---|---|
| 200 | OK | Lecture réussie |
| 201 | Created | Ressource créée |
| 204 | No Content | Suppression réussie |
| 301/308 | Redirection permanente | |
| 302/307 | Redirection temporaire | |
| 400 | Bad Request | Entrée invalide |
| 401 | Unauthorized | Non authentifié |
| 403 | Forbidden | Authentifié mais interdit |
| 404 | Not Found | Ressource absente |
| 409 | Conflict | Doublon, état incompatible |
| 422 | Unprocessable Entity | Validation échouée |
| 429 | Too Many Requests | Limitation de débit |
| 500 | Internal Server Error | Erreur serveur |

## 10.6 Mise en cache des Route Handlers

- ⚠️ **Version 15+** : les handlers `GET` **ne sont pas mis en cache par défaut**.
- **Modèle classique** : `export const dynamic = "force-static"` permet de les pré-rendre au build (utile pour un flux RSS, un `sitemap` personnalisé) ; `export const revalidate = 3600` pour une régénération temporelle.
- **Avec Cache Components** : le handler est **dynamique par défaut** ; pour mettre en cache, extrayez la logique dans une **fonction `"use cache"`** appelée par le handler (la directive ne se place pas dans le corps de la méthode du handler lui-même).

```ts
// avec Cache Components
async function getStats() {
  "use cache";
  cacheLife("minutes");
  return db.stats.compute();
}
export async function GET() {
  return Response.json(await getStats());
}
```

## 10.7 CORS

```ts
const entetesCors = {
  "Access-Control-Allow-Origin": "https://app.exemple.com",
  "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
};

export async function OPTIONS() {
  return new Response(null, { status: 204, headers: entetesCors });
}

export async function GET() {
  return Response.json({ ok: true }, { headers: entetesCors });
}
```

Évitez `Access-Control-Allow-Origin: *` pour les API qui exigent des identifiants.

## 10.8 Webhooks

Exemple de réception d'un webhook avec **vérification de signature** (le **corps brut** est nécessaire) :

```ts
import crypto from "node:crypto";

export async function POST(request: Request) {
  const brut = await request.text();                          // corps brut, pas .json()
  const signature = request.headers.get("x-signature") ?? "";
  const attendu = crypto.createHmac("sha256", process.env.WEBHOOK_SECRET!).update(brut).digest("hex");

  const ok =
    signature.length === attendu.length &&
    crypto.timingSafeEqual(Buffer.from(signature), Buffer.from(attendu));
  if (!ok) return new Response("Signature invalide", { status: 401 });

  const evenement = JSON.parse(brut);
  // traiter l'événement de façon idempotente ; répondre vite (2xx)
  return new Response(null, { status: 204 });
}
```

## 10.9 Streaming et Server-Sent Events

```ts
export async function GET() {
  const encodeur = new TextEncoder();
  const flux = new ReadableStream({
    async start(controller) {
      for (let i = 0; i < 5; i++) {
        controller.enqueue(encodeur.encode(`data: tick ${i}\n\n`));
        await new Promise((r) => setTimeout(r, 1000));
      }
      controller.close();
    },
  });
  return new Response(flux, {
    headers: { "Content-Type": "text/event-stream", "Cache-Control": "no-cache", Connection: "keep-alive" },
  });
}
```

## 10.10 Appeler un Route Handler

- Depuis un **Client Component** : `fetch("/api/...")`, SWR, TanStack Query.
- Depuis un **client externe** : `curl`, application mobile, service tiers.
- **Pas** depuis un Server Component : appelez directement la fonction partagée.

```bash
curl -X POST http://localhost:3000/api/posts \
  -H "Content-Type: application/json" \
  -d '{"titre":"Salut"}'
```

## 10.11 Bonnes pratiques d'API

- Valider les entrées (Zod) ; renvoyer des erreurs **cohérentes** (`{ erreur, details }`).
- Authentifier/autoriser **chaque** handler.
- Pagination, tri, limites par défaut.
- Idempotence pour les webhooks et paiements.
- Journalisation + identifiants de corrélation.
- Versionner si l'API est publique (`/api/v1/...`).

## Pièges courants

- **Lire le corps deux fois** (`json()` puis `text()`) : le flux est consommé.
- **Oublier `await params`**.
- **Compter sur le cache par défaut** (supprimé en 15).
- **Définir CORS ouvert partout**.
- **Écrire un Route Handler pour ce qu'une Server Action ferait mieux** (formulaires internes).

## À retenir

- `route.ts` + fonctions `GET/POST/...` basées sur `Request`/`Response`.
- `NextRequest`/`NextResponse` ajoutent `nextUrl`, `cookies`, helpers de redirection.
- Idéal pour API publiques, webhooks, flux, endpoints non-JSON.

## Exercices

1. CRUD complet de `/api/taches` (GET liste, POST création, GET/PUT/DELETE par id) avec validation.
2. Webhook avec vérification HMAC.
3. Endpoint SSE qui envoie l'heure chaque seconde.

---

# Chapitre 11 — Proxy (ex-Middleware)

## Objectifs

- Comprendre le rôle et les limites du Proxy.
- Écrire des règles de redirection, réécriture, en-têtes, cookies.
- Configurer le `matcher`.
- Migrer de `middleware.ts` vers `proxy.ts`.

## 11.1 Définition

Le **Proxy** est un code qui s'exécute **avant** qu'une requête n'atteigne une route (page, Route Handler, fichier statique). Il peut **lire** la requête et **modifier** la réponse : rediriger, réécrire l'URL, ajouter des en-têtes ou des cookies, ou répondre directement.

> ⚠️ **Version 16** : le fichier **`middleware.ts`** est **renommé `proxy.ts`** (et la fonction exportée `middleware` devient `proxy`) pour clarifier qu'il agit comme une **frontière réseau** devant l'application. La logique reste identique. `proxy.ts` s'exécute sur le runtime **Node.js**. `middleware.ts` fonctionne encore (déprécié) et reste nécessaire si vous avez besoin du runtime **Edge**.

Migration automatique :

```bash
npx @next/codemod@canary middleware-to-proxy .
```

## 11.2 Emplacement et structure

Un seul fichier à la **racine du projet** (ou dans `src/` si utilisé), au même niveau que `app/`.

```ts
// proxy.ts
import { NextResponse, type NextRequest } from "next/server";

export function proxy(request: NextRequest) {
  const { pathname } = request.nextUrl;

  // 1) Redirection
  if (pathname.startsWith("/ancien-blog")) {
    return NextResponse.redirect(new URL(pathname.replace("/ancien-blog", "/blog"), request.url));
  }

  // 2) Protection optimiste
  const session = request.cookies.get("session")?.value;
  if (pathname.startsWith("/dashboard") && !session) {
    return NextResponse.redirect(new URL("/login", request.url));
  }

  // 3) En-têtes
  const reponse = NextResponse.next();
  reponse.headers.set("x-pathname", pathname);
  return reponse;
}

export const config = {
  matcher: ["/dashboard/:path*", "/ancien-blog/:path*"],
};
```

## 11.3 Opérations possibles

| Opération | Code |
|---|---|
| Continuer | `NextResponse.next()` |
| Rediriger | `NextResponse.redirect(url)` |
| Réécrire (URL inchangée côté navigateur) | `NextResponse.rewrite(url)` |
| Répondre directement | `NextResponse.json(...)` / `new NextResponse(body, { status })` |
| Modifier en-têtes de **requête** transmis à l'app | `NextResponse.next({ request: { headers } })` |
| Poser des cookies | `reponse.cookies.set(...)` |
| Travail différé | `event.waitUntil(promesse)` |

```ts
// Passer des en-têtes de requête aux routes
const entetes = new Headers(request.headers);
entetes.set("x-user-id", "42");
return NextResponse.next({ request: { headers: entetes } });
```

```ts
// Réécriture : A/B test
const variante = request.cookies.get("ab")?.value ?? (Math.random() < 0.5 ? "a" : "b");
const reponse = NextResponse.rewrite(new URL(`/accueil-${variante}`, request.url));
reponse.cookies.set("ab", variante);
return reponse;
```

## 11.3 bis Cas d'usage

- Redirections conditionnelles (langue, pays, ancienne URL).
- **Vérifications d'authentification optimistes** (présence d'un cookie).
- Tests A/B, *feature flags*.
- En-têtes de sécurité (CSP avec *nonce*), CORS simple.
- Détection d'appareil, bot, géolocalisation (selon la plateforme).
- Réécriture multi-locataire (`client.exemple.com` → `/client`).

## 11.4 Le `matcher`

Sans `matcher`, le proxy s'exécute sur **toutes** les requêtes, y compris les fichiers statiques. Filtrez :

```ts
export const config = {
  matcher: [
    // toutes les routes sauf api, assets Next et fichiers statiques
    "/((?!api|_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)",
  ],
};
```

Syntaxe :

| Motif | Signification |
|---|---|
| `/dashboard` | Chemin exact |
| `/dashboard/:path*` | Zéro ou plus de segments |
| `/dashboard/:path+` | Un ou plusieurs segments |
| `/blog/:slug?` | Segment optionnel |
| Expression régulière entre parenthèses | Motifs avancés |

Conditions avancées :

```ts
export const config = {
  matcher: [
    {
      source: "/api/:path*",
      has: [{ type: "header", key: "Authorization" }],
      missing: [{ type: "cookie", key: "bypass" }],
    },
  ],
};
```

Les valeurs du `matcher` doivent être des **constantes** analysables au build.

## 11.5 Ordre d'exécution

Pour une requête entrante :

1. `headers` (de `next.config`)
2. `redirects` (de `next.config`)
3. **Proxy** (`proxy.ts`)
4. `rewrites` `beforeFiles`
5. Fichiers du système de fichiers (`public/`, `_next/static`, pages)
6. `rewrites` `afterFiles`
7. Routes dynamiques
8. `rewrites` `fallback`

## 11.6 Limites et bonnes pratiques

- **Léger et rapide** : le Proxy s'exécute sur chaque requête concernée. Évitez les appels réseau lents et les requêtes de base de données.
- **Pas de source de vérité pour l'autorisation.** Utilisez le Proxy pour des **contrôles rapides** (cookie présent, redirection), puis **revérifiez** l'identité et les droits **au plus près des données** (DAL, Server Actions, Route Handlers).
- **Rappel de sécurité** : en mars 2025, la faille **CVE-2025-29927** a montré qu'un en-tête interne spécifique permettait de **contourner** le middleware dans certaines versions ; des correctifs ont été publiés. Conséquence : ne faites **jamais** reposer toute la sécurité sur le proxy, et gardez Next.js à jour.
- **Pas de partage d'état** entre requêtes ; évitez les variables globales.
- Pas d'accès direct à vos composants React ni aux Server Actions.
- Utilisez `config.matcher` pour limiter l'exécution.

## 11.7 Proxy vs Route Handlers vs `next.config`

| Besoin | Outil |
|---|---|
| Redirection simple, statique | `redirects` dans `next.config` |
| Réécriture simple | `rewrites` dans `next.config` |
| Logique conditionnelle sur la requête | **Proxy** |
| Logique métier, accès aux données | Route Handler / Server Action |

## Pièges courants

- **Matcher trop large** → proxy exécuté sur des images, fichiers `_next`.
- **Boucles de redirection** (`/login` redirige vers `/login`).
- **Auth uniquement dans le proxy**.
- **Oublier de renommer** `middleware` en `proxy` (Next.js 16).
- **Requêtes lourdes** dans le proxy.

## À retenir

- Proxy = interception **avant** les routes ; Node.js dans Next.js 16.
- Redirect / rewrite / headers / cookies.
- `matcher` pour cibler ; **jamais** seule barrière de sécurité.

## Exercices

1. Redirigez `/dashboard` vers `/login` si un cookie `session` est absent.
2. Ajoutez des en-têtes de sécurité (`X-Content-Type-Options`, `Referrer-Policy`) via le proxy.
3. Mettez en place un test A/B avec réécriture et cookie.

---

# Chapitre 12 — Navigation

## Objectifs

- Naviguer avec `<Link>`, `useRouter`, `redirect`.
- Comprendre prefetching, navigation douce (soft) et dure (hard), restauration du scroll.
- Utiliser `next/form`, `useLinkStatus`, et l'API History.

## 12.1 Mécanisme de navigation

Next.js remplace le comportement par défaut du navigateur par une **navigation côté client** :

1. **Prefetching** : le contenu des routes visibles (liens `<Link>`) est **préchargé** en arrière-plan.
2. **Navigation douce (soft)** : au clic, seuls les **segments modifiés** sont récupérés ; les **layouts partagés sont conservés** (état inchangé) ; pas de rechargement.
3. **Streaming** : les parties lentes arrivent progressivement avec `loading.tsx`/`Suspense`.
4. **Historique** : les boutons précédent/suivant restaurent l'état et la position de défilement.

Une **navigation dure (hard)** (rechargement complet) a lieu pour un lien `<a>` classique, une URL tapée, un changement de layout racine, ou quand le prefetch n'est pas applicable.

> ⚠️ **Version 16** : le routage a été optimisé : **déduplication des layouts** lors du prefetch (un layout partagé n'est téléchargé qu'une fois) et **préchargement incrémental** (seules les parties absentes du cache sont demandées, avec annulation des requêtes de liens qui sortent de la vue).

## 12.2 Le composant `<Link>`

```tsx
import Link from "next/link";

export default function Menu() {
  return (
    <nav>
      <Link href="/">Accueil</Link>
      <Link href="/blog">Blog</Link>
      <Link href={`/blog/${slug}`}>Article</Link>
      <Link href={{ pathname: "/recherche", query: { q: "next" } }}>Recherche</Link>
    </nav>
  );
}
```

### Props principales

| Prop | Rôle |
|---|---|
| `href` | Destination (chaîne ou objet `{ pathname, query }`) — **obligatoire** |
| `replace` | Remplace l'entrée d'historique au lieu d'en ajouter une |
| `scroll` | `false` : ne remonte pas en haut de page après navigation |
| `prefetch` | `true` / `false` / (défaut : automatique) |
| `onNavigate` | Callback avant navigation ; `e.preventDefault()` l'annule |
| `className`, `target`, `rel`, etc. | Comme `<a>` |

### Prefetching en détail

- Actif **en production** uniquement (désactivé en développement).
- **Routes statiques** : préchargées en totalité.
- **Routes dynamiques** : préchargées **jusqu'à la première frontière `loading.tsx`** (d'où l'importance d'un `loading.tsx` pour une navigation instantanée).
- `prefetch={false}` : désactive (utile sur de très longues listes de liens).
- Les liens sont préchargés **quand ils entrent dans le viewport**.

### Liens externes

Utilisez un `<a>` classique (avec `rel="noopener noreferrer"` pour `target="_blank"`) ; `<Link>` est destiné à la navigation interne.

### Ancres (`#`)

```tsx
<Link href="/doc#installation">Installation</Link>
```

## 12.3 Navigation impérative : `useRouter`

```tsx
"use client";
import { useRouter } from "next/navigation";

export function Actions() {
  const router = useRouter();
  return (
    <>
      <button onClick={() => router.push("/dashboard")}>Aller</button>
      <button onClick={() => router.replace("/login")}>Remplacer</button>
      <button onClick={() => router.back()}>Retour</button>
      <button onClick={() => router.forward()}>Avancer</button>
      <button onClick={() => router.refresh()}>Rafraîchir</button>
      <button onClick={() => router.prefetch("/blog")}>Précharger</button>
    </>
  );
}
```

| Méthode | Effet |
|---|---|
| `push(href, { scroll })` | Navigue et ajoute à l'historique |
| `replace(href, { scroll })` | Navigue sans ajouter à l'historique |
| `back()` / `forward()` | Historique |
| `refresh()` | Re-demande les données du serveur pour la route courante (le cache client est invalidé ; l'état client est conservé) |
| `prefetch(href)` | Précharge manuellement |

⚠️ `useRouter` de **`next/navigation`** (App Router) diffère de celui de `next/router` (Pages Router) : il n'expose pas `router.events`, ni `pathname`/`query` (utilisez `usePathname`, `useSearchParams`).

## 12.4 Redirection côté serveur

```tsx
import { redirect } from "next/navigation";

export default async function Page() {
  const session = await getSession();
  if (!session) redirect("/login");   // 307
  return <p>Bienvenue</p>;
}
```

Voir chapitre 4 pour `permanentRedirect`, `notFound`, `forbidden`, `unauthorized`.

## 12.5 Lire l'URL côté client

```tsx
"use client";
import { usePathname, useSearchParams, useParams } from "next/navigation";

export function Debug() {
  const pathname = usePathname();      // "/blog/mon-article"
  const search = useSearchParams();    // lecture seule (URLSearchParams)
  const params = useParams();          // { slug: "mon-article" }
  return <pre>{pathname} {search.get("q")} {JSON.stringify(params)}</pre>;
}
```

`useSearchParams` exige un `<Suspense>` autour du composant pour ne pas rendre toute la page dynamique au build.

### Mettre à jour la query string

```tsx
"use client";
import { useRouter, usePathname, useSearchParams } from "next/navigation";

export function Filtre() {
  const router = useRouter();
  const pathname = usePathname();
  const search = useSearchParams();

  function changer(valeur: string) {
    const params = new URLSearchParams(search.toString());
    params.set("tri", valeur);
    router.replace(`${pathname}?${params.toString()}`, { scroll: false });
  }
  return <select onChange={(e) => changer(e.target.value)}><option>date</option><option>prix</option></select>;
}
```

## 12.6 Indicateur de navigation : `useLinkStatus`

```tsx
"use client";
import Link from "next/link";
import { useLinkStatus } from "next/link";

function Spinner() {
  const { pending } = useLinkStatus();
  return pending ? <span aria-hidden>⏳</span> : null;
}

export function LienAvecIndicateur({ href, children }: { href: string; children: React.ReactNode }) {
  return <Link href={href}>{children}<Spinner /></Link>;
}
```

`useLinkStatus` doit être utilisé **dans un enfant** de `<Link>` ; il indique si la navigation de ce lien est en cours (utile quand le prefetch n'a pas eu lieu).

## 12.7 API History native

`window.history.pushState` et `replaceState` sont **intégrés au routeur** : ils mettent à jour `usePathname` et `useSearchParams` **sans rechargement** ni requête serveur. Pratique pour trier/filtrer instantanément côté client.

```tsx
"use client";
export function Tri() {
  return <button onClick={() => {
    const p = new URLSearchParams(window.location.search);
    p.set("tri", "prix");
    window.history.pushState(null, "", `?${p.toString()}`);
  }}>Trier</button>;
}
```

## 12.8 Défilement (scroll)

- Par défaut, après une navigation, Next.js **fait défiler jusqu'en haut** du nouveau segment (ou jusqu'à l'ancre), **sauf** s'il est déjà visible.
- Désactiver : `<Link scroll={false}>` ou `router.push(url, { scroll: false })`.
- Boutons précédent/suivant : restauration de la position.

## 12.9 Navigation vs `loading.tsx` : le ressenti utilisateur

Une navigation **instantanée** demande : (1) un **prefetch** de la coque, (2) un **`loading.tsx`** ou des `Suspense` bien placés, (3) des données **en cache** quand c'est possible. Sans `loading.tsx`, une route dynamique peut attendre le serveur avant d'afficher quoi que ce soit.

## 12.10 Transitions de vue (expérimental)

Avec React 19.2, Next.js peut activer les **View Transitions** (animations natives entre états) via un réglage expérimental (`experimental.viewTransition`) ; consultez la documentation de votre version.

## Pièges courants

- **Utiliser `<a>` pour une navigation interne** : rechargement complet, perte d'état.
- **Appeler `router.push` dans le rendu** (au lieu d'un événement/effet).
- **Importer `useRouter` depuis `next/router`** dans l'App Router.
- **Utiliser `useSearchParams` sans `Suspense`**.
- **Tester le prefetch en développement** (il est désactivé).

## À retenir

- `<Link>` pour la navigation déclarative ; `useRouter` pour l'impératif ; `redirect` côté serveur.
- Prefetching + layouts persistants + streaming = navigation fluide.
- L'URL est un excellent conteneur d'état partageable (`searchParams`).

## Exercices

1. Créez un menu avec lien actif (`usePathname`) et indicateur `useLinkStatus`.
2. Implémentez un filtre qui met à jour `?tri=` via `router.replace`.
3. Ajoutez un `loading.tsx` et observez la différence de ressenti en production (`build` + `start`).

---

# Chapitre 13 — Styles

## Objectifs

- Utiliser CSS global, CSS Modules, Tailwind CSS, Sass.
- Comprendre la compatibilité du CSS-in-JS avec les Server Components.
- Mettre en place un thème clair/sombre.

## 13.1 Vue d'ensemble

| Approche | Portée | Quand l'utiliser |
|---|---|---|
| **CSS global** | Toute l'application | Reset, variables, typographie |
| **CSS Modules** | Locale au composant | Styles scopés sans configuration |
| **Tailwind CSS** | Classes utilitaires | Prototypage rapide, design system |
| **Sass/SCSS** | Global ou module | Variables, imbrication, mixins |
| **CSS-in-JS** | Composant | Avec précautions (Client Components) |
| **Styles en ligne** | Élément | Valeurs dynamiques ponctuelles |

## 13.2 CSS global

```css
/* app/globals.css */
:root {
  --couleur-fond: #ffffff;
  --couleur-texte: #111111;
}
body {
  background: var(--couleur-fond);
  color: var(--couleur-texte);
  font-family: system-ui, sans-serif;
}
```

```tsx
// app/layout.tsx
import "./globals.css";
```

Bonnes pratiques : importez le CSS global **dans le layout racine**, limitez-le aux styles réellement globaux (reset, variables, typographie de base).

## 13.3 CSS Modules

Un fichier **`nom.module.css`** génère des **noms de classes uniques** (hachés) : pas de collision.

```css
/* bouton.module.css */
.primaire {
  background: royalblue;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 6px;
}
.primaire:hover { filter: brightness(1.1); }
```

```tsx
import styles from "./bouton.module.css";

export default function Bouton({ children }: { children: React.ReactNode }) {
  return <button className={styles.primaire}>{children}</button>;
}
```

- Utilisable dans les Server **et** Client Components.
- Combinaison de classes : `` `${styles.a} ${styles.b}` `` ou la bibliothèque **`clsx`**.
- Sélecteurs globaux explicites : `:global(.nom)`.

## 13.4 Tailwind CSS

Framework de **classes utilitaires** (`flex`, `p-4`, `text-lg`). `create-next-app` peut le configurer. Principe avec Tailwind v4 :

```bash
npm install tailwindcss @tailwindcss/postcss postcss
```

```js
// postcss.config.mjs
export default { plugins: { "@tailwindcss/postcss": {} } };
```

```css
/* app/globals.css */
@import "tailwindcss";
```

```tsx
export default function Carte() {
  return (
    <article className="rounded-xl border p-4 shadow-sm hover:shadow-md dark:bg-zinc-900">
      <h2 className="text-xl font-semibold">Titre</h2>
    </article>
  );
}
```

Points clés :

- **Variantes** : `hover:`, `focus:`, `md:` (responsive), `dark:` (mode sombre).
- **Thème personnalisable** (v4 : directive `@theme` dans le CSS).
- Pour fusionner des classes conditionnelles : `clsx` + `tailwind-merge` (utilitaire `cn()`).
- Les classes doivent apparaître **en entier** dans le code (pas de concaténation dynamique `text-${couleur}-500`) pour être détectées.

## 13.5 Sass

```bash
npm install --save-dev sass
```

Renommez vos fichiers en `.scss`/`.module.scss`. Options dans `next.config.ts` :

```ts
const nextConfig = { sassOptions: { includePaths: ["./styles"] } };
```

⚠️ **Turbopack** : l'import avec tilde (`@import "~bibliotheque/..."`) n'est **pas supporté** ; utilisez des chemins standards sans `~`.

## 13.6 CSS-in-JS

- Les bibliothèques **à l'exécution** (styled-components, Emotion) reposent sur le contexte React et les effets : elles ne fonctionnent que dans les **Client Components** et demandent un **registre de styles** pour le rendu serveur.
- **styled-jsx** (livré avec Next.js) fonctionne uniquement dans les Client Components.
- Alternatives compatibles RSC : **CSS Modules**, **Tailwind**, et des solutions **« zero-runtime »** (vanilla-extract, Panda CSS, StyleX).
- Recommandation : préférez une approche qui génère du **CSS statique** pour tirer parti des Server Components.

## 13.7 Mode sombre (thème)

### Avec CSS et `prefers-color-scheme`

```css
:root { --fond: #fff; --texte: #111; }
@media (prefers-color-scheme: dark) {
  :root { --fond: #0b0b0b; --texte: #eee; }
}
```

### Avec bascule manuelle : `next-themes`

```tsx
// providers.tsx
"use client";
import { ThemeProvider } from "next-themes";

export function Providers({ children }: { children: React.ReactNode }) {
  return <ThemeProvider attribute="class" defaultTheme="system" enableSystem>{children}</ThemeProvider>;
}
```

```tsx
// app/layout.tsx
<html lang="fr" suppressHydrationWarning>  {/* la classe est ajoutée avant hydratation */}
  <body><Providers>{children}</Providers></body>
</html>
```

## 13.8 Ordre et chargement du CSS

- Le CSS est **découpé par route** et chargé uniquement quand nécessaire.
- L'**ordre d'import** détermine la priorité de cascade : gardez un ordre cohérent entre composants (évitez de dépendre de l'ordre pour la correction visuelle).
- Les feuilles externes peuvent être déclarées avec `<link rel="stylesheet" href="..." precedence="default" />` (React 19).

## Pièges courants

- **Importer du CSS global dans plusieurs composants** : effets de bord imprévisibles.
- **Classes Tailwind construites dynamiquement** (non détectées).
- **Utiliser styled-components dans un Server Component** : erreur.
- **Flash de thème** (FOUC) mal géré lors du mode sombre.

## À retenir

- CSS Modules et Tailwind conviennent bien aux Server Components.
- CSS-in-JS d'exécution → Client Components seulement.
- Variables CSS + `next-themes` pour le mode sombre.

## Exercices

1. Stylisez un bouton avec un CSS Module, puis avec Tailwind.
2. Ajoutez un commutateur de thème clair/sombre sans flash au chargement.

---

# Chapitre 14 — Optimisations

## Objectifs

- Optimiser images, polices et scripts avec les composants natifs.
- Réduire la taille des bundles (lazy loading, imports ciblés).
- Utiliser le React Compiler et mesurer les performances.

## 14.1 Images : `next/image`

### Problèmes résolus

Les images sont la **première source de poids** et de **décalages visuels (CLS)**. `next/image` fournit :

- **Redimensionnement** selon l'appareil (`srcset` généré).
- **Formats modernes** (WebP, AVIF) selon le navigateur.
- **Chargement paresseux** (*lazy loading*) par défaut.
- **Réservation d'espace** (évite le CLS).
- **Optimisation à la demande** (mise en cache sur le serveur).

### Utilisation de base

```tsx
import Image from "next/image";
import photo from "./photo.jpg"; // import statique : largeur/hauteur/blur automatiques

export default function Exemple() {
  return (
    <>
      <Image src={photo} alt="Description de la photo" placeholder="blur" />
      <Image src="/logo.png" alt="Logo" width={200} height={60} />
      <Image src="https://images.exemple.com/p.jpg" alt="Distante" width={800} height={600} />
    </>
  );
}
```

### Props importantes

| Prop | Rôle |
|---|---|
| `src` | Chemin local, import statique ou URL distante |
| `alt` | **Obligatoire** : texte alternatif (accessibilité, SEO) ; `alt=""` pour une image décorative |
| `width`, `height` | **Obligatoires** pour les images non importées, sauf avec `fill` |
| `fill` | L'image remplit son parent (`position: relative` requis sur le parent) |
| `sizes` | Largeur occupée selon le viewport (ex. `(max-width: 768px) 100vw, 50vw`) : **essentiel** avec `fill` ou pour des images responsives |
| `quality` | 1–100 (⚠️ par défaut 75 ; en Next.js 16, les valeurs autorisées se configurent via `images.qualities`) |
| `priority` / `preload` | Précharge l'image (pour l'élément **LCP**, au-dessus de la ligne de flottaison). ⚠️ Next.js 16 déprécie `priority` au profit de `preload` : vérifiez la documentation de votre version |
| `loading` | `"lazy"` (défaut) ou `"eager"` |
| `placeholder` | `"blur"` (avec `blurDataURL` si image distante) ou `"empty"` |
| `unoptimized` | Désactive l'optimisation pour cette image |
| `loader` | Fonction de génération d'URL (CDN d'images) |
| `style`, `className` | Styles |
| `onLoad`, `onError` | Événements (Client Components) |

### Image responsive avec `fill`

```tsx
<div style={{ position: "relative", aspectRatio: "16 / 9" }}>
  <Image
    src="/banniere.jpg"
    alt="Bannière"
    fill
    sizes="(max-width: 768px) 100vw, 50vw"
    style={{ objectFit: "cover" }}
  />
</div>
```

### Autoriser des images distantes

```ts
// next.config.ts
const nextConfig = {
  images: {
    remotePatterns: [
      { protocol: "https", hostname: "images.exemple.com", pathname: "/produits/**" },
    ],
  },
};
```

Toujours **restreindre** les domaines (sécurité, coûts d'optimisation).

### Autres réglages (`images` dans la config)

| Option | Rôle |
|---|---|
| `formats` | `["image/avif", "image/webp"]` |
| `deviceSizes` / `imageSizes` | Largeurs générées |
| `minimumCacheTTL` | Durée de cache minimale des images optimisées (⚠️ défaut de 4 h en Next.js 16) |
| `localPatterns` | Chemins locaux autorisés (⚠️ requis en Next.js 16 pour les images locales avec *query string*) |
| `qualities` | Liste des qualités autorisées |
| `loader` / `loaderFile` | Loader personnalisé (Cloudinary, Imgix…) |
| `dangerouslyAllowSVG` | Autorise l'optimisation des SVG (à manier avec prudence) |
| `unoptimized` | Désactive globalement (utile en export statique) |

### Bonnes pratiques

- Fournissez **toujours** `alt` et des dimensions (ou `fill` + parent dimensionné).
- Marquez l'image **LCP** avec `preload`/`priority`.
- Utilisez des `sizes` précis pour éviter de télécharger des images trop grandes.
- Préférez les SVG pour les logos/icônes (balises `<img>` ou composants).

## 14.2 Polices : `next/font`

Avantages : **auto-hébergement** (aucune requête vers Google à l'exécution, meilleure confidentialité), **zéro décalage de mise en page** (métriques de repli ajustées), chargement optimisé.

### Google Fonts

```tsx
// app/layout.tsx
import { Inter, Playfair_Display } from "next/font/google";

const inter = Inter({ subsets: ["latin"], display: "swap", variable: "--font-inter" });
const playfair = Playfair_Display({ subsets: ["latin"], weight: ["400", "700"], variable: "--font-playfair" });

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr" className={`${inter.variable} ${playfair.variable}`}>
      <body className={inter.className}>{children}</body>
    </html>
  );
}
```

- Les **polices variables** n'exigent pas `weight`.
- `subsets` : jeux de caractères à inclure.
- `display` : stratégie d'affichage (`swap`, `optional`…).
- `variable` : expose la police via une **variable CSS** (pratique avec Tailwind).

### Polices locales

```tsx
import localFont from "next/font/local";

const maPolice = localFont({
  src: [
    { path: "./fonts/Marque-Regular.woff2", weight: "400", style: "normal" },
    { path: "./fonts/Marque-Bold.woff2", weight: "700", style: "normal" },
  ],
  variable: "--font-marque",
});
```

## 14.3 Scripts : `next/script`

```tsx
import Script from "next/script";

<Script src="https://exemple.com/widget.js" strategy="afterInteractive" />
```

| Stratégie | Moment de chargement |
|---|---|
| `beforeInteractive` | Avant l'hydratation (scripts critiques) ; **uniquement dans le layout racine** |
| `afterInteractive` (défaut) | Juste après l'hydratation (analytics, tag managers) |
| `lazyOnload` | Pendant les temps d'inactivité (widgets de chat) |
| `worker` | Dans un Web Worker (expérimental, via Partytown) |

- Callbacks (Client Components) : `onLoad`, `onReady`, `onError`.
- Scripts **en ligne** : fournir un `id`.
- Package **`@next/third-parties`** : composants optimisés pour Google Analytics, Google Tag Manager, YouTube, Google Maps.

```tsx
import { GoogleAnalytics } from "@next/third-parties/google";
<GoogleAnalytics gaId="G-XXXXXXX" />
```

## 14.4 Réduire le JavaScript envoyé

1. **Server Components par défaut** : la logique reste côté serveur.
2. **Chargement dynamique** (`next/dynamic`, `React.lazy`) pour les composants lourds non critiques :

```tsx
"use client";
import dynamic from "next/dynamic";
const Editeur = dynamic(() => import("./Editeur"), { loading: () => <p>…</p> });
```

3. **Importer à la demande** les bibliothèques lourdes :

```ts
async function exporter() {
  const { default: jsPDF } = await import("jspdf");
  /* ... */
}
```

4. **Imports ciblés** : `import debounce from "lodash/debounce"` plutôt que `import _ from "lodash"` ; l'option `experimental.optimizePackageImports` optimise les paquets à nombreux exports (icônes, etc.).
5. **Analyse** : `@next/bundle-analyzer` pour visualiser la composition des bundles.
6. **Éviter les doublons** de dépendances (`npm ls`, `npm dedupe`).
7. **Paquets externes côté serveur** : `serverExternalPackages` pour exclure du bundling certains modules natifs.

## 14.5 React Compiler

Outil de build qui **mémoïse automatiquement** composants et valeurs (équivalent d'un `useMemo`/`useCallback`/`memo` posé partout où utile), sans changer votre code.

```bash
npm install --save-dev babel-plugin-react-compiler
```

```ts
// next.config.ts
const nextConfig = { reactCompiler: true };
```

- Stable depuis Next.js 16 (compilateur 1.0).
- Allonge légèrement les temps de compilation.
- Exclusion locale : directive `"use no memo"`.
- Respectez les **règles de React** (composants purs, pas de mutation d'état).

## 14.6 Précharger et préconnecter

```tsx
import { preload, preconnect } from "react-dom";

preconnect("https://api.exemple.com");   // ouvre tôt la connexion
preload("/hero.jpg", { as: "image" });   // précharge une ressource critique
```

## 14.7 Éviter les décalages de mise en page (CLS)

- Dimensions explicites pour images, vidéos, iframes.
- `next/font` pour éviter les sauts de police.
- Réserver l'espace des contenus chargés tardivement (squelettes de même taille).
- Ne pas insérer de contenu au-dessus du contenu existant après chargement.

## 14.8 Mesurer

- **Lighthouse**, **PageSpeed Insights**, onglet *Performance* de Chrome DevTools.
- `useReportWebVitals` (chapitre 8), **Vercel Speed Insights** ou outil RUM (Real User Monitoring).
- `next build` : taille de chaque route (« First Load JS »).
- Surveillez régulièrement : LCP, INP, CLS, TTFB, taille de bundle.

## 14.9 Liste de contrôle de production

- [ ] Images via `next/image`, `sizes` correctes, LCP préchargé.
- [ ] Polices via `next/font`.
- [ ] Scripts tiers via `next/script` ou `@next/third-parties`.
- [ ] Composants lourds chargés dynamiquement.
- [ ] Cache configuré (chapitre 7) ; routes dynamiques justifiées.
- [ ] `loading.tsx`/`Suspense` aux bons endroits.
- [ ] Métadonnées complètes (chapitre 15).
- [ ] En-têtes de sécurité (chapitre 18).
- [ ] Monitoring et suivi des erreurs.

## Pièges courants

- **Oublier `sizes`** avec `fill` : l'image la plus grande est téléchargée.
- **Autoriser tous les hôtes distants** (`hostname: "**"`) : risque d'abus.
- **Précharger trop d'images** (`priority` partout) : annule le gain.
- **Charger Google Analytics en `beforeInteractive`** : bloque le rendu.

## À retenir

- `next/image`, `next/font`, `next/script` automatisent des optimisations majeures.
- Moins de JS = Server Components + chargement dynamique + imports ciblés.
- Mesurer avant et après chaque optimisation.

## Exercices

1. Remplacez des `<img>` par `<Image>` avec `sizes` et mesurez le gain avec Lighthouse.
2. Chargez dynamiquement un composant d'éditeur et comparez le « First Load JS ».
3. Activez le React Compiler et comparez les rendus avec React DevTools.

---

# Chapitre 15 — Métadonnées et SEO

## Objectifs

- Définir des métadonnées statiques et dynamiques.
- Générer images Open Graph, sitemap, robots, manifest.
- Appliquer les bonnes pratiques SEO techniques.

## 15.1 Pourquoi les métadonnées ?

Les **métadonnées** (`<title>`, `<meta name="description">`, Open Graph, Twitter Cards, `<link rel="canonical">`…) décrivent la page aux **moteurs de recherche**, aux **réseaux sociaux** et aux **navigateurs**. L'API Metadata de Next.js les gère de façon **typée** et **côté serveur**.

> Les métadonnées se définissent **uniquement dans les Server Components** (`layout.tsx` et `page.tsx`).

## 15.2 Métadonnées statiques

```tsx
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Mon site",
  description: "Description de moins de 160 caractères.",
  keywords: ["next.js", "react"],
  authors: [{ name: "Alice" }],
  openGraph: {
    title: "Mon site",
    description: "Description pour les réseaux sociaux",
    url: "https://exemple.com",
    siteName: "Mon site",
    images: [{ url: "/og.png", width: 1200, height: 630, alt: "Aperçu" }],
    locale: "fr_FR",
    type: "website",
  },
  twitter: { card: "summary_large_image", title: "Mon site", images: ["/og.png"] },
  robots: { index: true, follow: true },
  alternates: { canonical: "https://exemple.com" },
};
```

## 15.3 Métadonnées dynamiques

```tsx
import type { Metadata, ResolvingMetadata } from "next";

export async function generateMetadata(
  { params }: { params: Promise<{ slug: string }> },
  parent: ResolvingMetadata
): Promise<Metadata> {
  const { slug } = await params;
  const post = await getPost(slug);                   // dédupliqué avec la page si fetch/cache
  const imagesParentes = (await parent).openGraph?.images ?? [];

  return {
    title: post.titre,
    description: post.extrait,
    openGraph: { images: [post.image, ...imagesParentes] },
  };
}
```

- Peut être `async`, lit `params` et `searchParams`.
- Les requêtes de données sont **dédupliquées** avec celles de la page (via `fetch` ou `React.cache`).
- Le *streaming* des métadonnées est géré : la page peut commencer à s'envoyer pendant le calcul (les robots reçoivent les métadonnées dans le `<head>` ; pour les navigateurs, elles peuvent être injectées plus tard).

## 15.4 Fusion et héritage

- Les métadonnées se **fusionnent** du layout racine vers la page (la plus profonde l'emporte, **champ par champ au premier niveau**) : un `openGraph` défini dans une page **remplace entièrement** l'objet `openGraph` du layout parent (pas de fusion profonde).
- **Template de titre** :

```tsx
// app/layout.tsx
export const metadata: Metadata = {
  metadataBase: new URL("https://exemple.com"),   // base pour résoudre les URLs relatives
  title: { default: "Mon site", template: "%s | Mon site" },
};

// app/blog/page.tsx
export const metadata: Metadata = { title: "Blog" };   // → "Blog | Mon site"

// forcer un titre exact :
export const metadata: Metadata = { title: { absolute: "Titre exact" } };
```

- **`metadataBase`** : indispensable pour des URLs relatives dans `openGraph.images`, `alternates`, etc.

## 15.5 Viewport et couleur de thème

Depuis Next.js 14, `viewport` est séparé :

```tsx
import type { Viewport } from "next";

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#ffffff" },
    { media: "(prefers-color-scheme: dark)", color: "#000000" },
  ],
};
// ou : export function generateViewport() { ... }
```

## 15.6 Autres champs utiles

| Champ | Rôle |
|---|---|
| `alternates.canonical` | URL canonique (évite le contenu dupliqué) |
| `alternates.languages` | Balises `hreflang` (versions linguistiques) |
| `icons` | Favicons, icônes Apple |
| `manifest` | Lien vers le manifeste PWA |
| `verification` | Vérification Search Console, etc. |
| `appleWebApp`, `formatDetection` | Options mobiles |
| `other` | Balises `<meta>` personnalisées |

## 15.7 Fichiers de métadonnées (conventions)

### Icônes

- `app/favicon.ico` ; `app/icon.(png|svg|jpg)` ; `app/apple-icon.png`.
- Génération dynamique : `app/icon.tsx` (retourne une `ImageResponse`).

### Images Open Graph / Twitter

- Statiques : `opengraph-image.png`, `twitter-image.png` (+ `.alt.txt`).
- Dynamiques : `opengraph-image.tsx` (voir chapitre 4) avec `ImageResponse` de `next/og`.

Limites d'`ImageResponse` : sous-ensemble de CSS (flexbox, pas de grid), taille de bundle limitée (~500 Ko), polices à charger explicitement (`fetch` d'un fichier de police).

### `sitemap.ts`

```ts
import type { MetadataRoute } from "next";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const posts = await getPosts();
  return [
    { url: "https://exemple.com", lastModified: new Date(), changeFrequency: "weekly", priority: 1 },
    ...posts.map((p) => ({ url: `https://exemple.com/blog/${p.slug}`, lastModified: p.updatedAt })),
  ];
}
```

Pour plus de 50 000 URLs : `generateSitemaps()` découpe en plusieurs fichiers.

### `robots.ts`

```ts
import type { MetadataRoute } from "next";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [{ userAgent: "*", allow: "/", disallow: ["/api/", "/dashboard/"] }],
    sitemap: "https://exemple.com/sitemap.xml",
  };
}
```

### `manifest.ts` (PWA)

```ts
import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "Mon application",
    short_name: "App",
    start_url: "/",
    display: "standalone",
    background_color: "#ffffff",
    theme_color: "#000000",
    icons: [{ src: "/icon-192.png", sizes: "192x192", type: "image/png" }],
  };
}
```

## 15.8 Données structurées (JSON-LD)

```tsx
export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const post = await getPost(slug);

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: post.titre,
    datePublished: post.date,
    author: { "@type": "Person", name: post.auteur },
  };

  return (
    <article>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd).replace(/</g, "\\u003c") }}
      />
      {/* contenu */}
    </article>
  );
}
```

Le remplacement de `<` évite l'injection de balises (XSS) si des champs proviennent d'utilisateurs.

## 15.9 Bonnes pratiques SEO techniques

1. **Titres uniques** (≈ 50–60 caractères) et **descriptions** (≈ 150–160) par page.
2. **Structure HTML sémantique** : un seul `<h1>`, hiérarchie `h2`/`h3`, `<main>`, `<nav>`, `<article>`.
3. **URL propres et lisibles**, pas de paramètres inutiles ; **canonical** sur les variantes.
4. **Rendu côté serveur** (ou statique) du contenu important : visible sans JavaScript.
5. **Performances** (Core Web Vitals) : facteur de classement.
6. **Images** : `alt` pertinent, tailles optimisées.
7. **Maillage interne** avec `<Link>` et textes d'ancre explicites.
8. **Sitemap** et **robots** à jour ; `noindex` pour les pages privées (`robots: { index: false }`).
9. **hreflang** pour les sites multilingues.
10. **Codes HTTP** corrects : 404 réels (`notFound()`), redirections 301/308 pour les URLs migrées.
11. **Données structurées** pertinentes.
12. **Accessibilité** : bénéfique aussi au SEO.

## Pièges courants

- **Oublier `metadataBase`** : URLs relatives incorrectes dans Open Graph.
- **Croire que `openGraph` fusionne en profondeur** (il remplace).
- **Exporter `metadata` depuis un Client Component** : non supporté.
- **Exporter `metadata` et `generateMetadata` dans le même segment** : conflit.
- **Pages privées indexées** par oubli de `noindex`.

## À retenir

- `metadata` (statique) ou `generateMetadata` (dynamique), côté serveur uniquement.
- Fichiers conventionnels pour icônes, OG, sitemap, robots, manifest.
- Le SEO repose autant sur le contenu et les performances que sur les balises.

## Exercices

1. Définissez un template de titre au niveau du layout racine et un titre par page.
2. Créez `generateMetadata` + `opengraph-image.tsx` pour des articles de blog.
3. Générez un `sitemap.ts` à partir de vos articles et un `robots.ts`.

---

# Chapitre 16 — Authentification

## Objectifs

- Distinguer authentification, session et autorisation.
- Implémenter une session sécurisée (cookies, JWT).
- Appliquer l'autorisation à plusieurs niveaux (proxy, DAL, composants, actions).
- Choisir une bibliothèque d'authentification.

## 16.1 Concepts

| Notion | Définition |
|---|---|
| **Authentification** (AuthN) | Vérifier **qui** est l'utilisateur (login, mot de passe, OAuth, passkey) |
| **Session** | Maintenir l'identité entre les requêtes |
| **Autorisation** (AuthZ) | Vérifier **ce que** l'utilisateur peut faire (rôles, permissions) |

### Méthodes d'authentification

- **Identifiant + mot de passe** (stockage haché : **argon2** ou **bcrypt**, jamais en clair).
- **OAuth 2.0 / OpenID Connect** (« Se connecter avec Google/GitHub »).
- **Lien magique / code à usage unique** par e-mail.
- **Passkeys / WebAuthn** (sans mot de passe, résistant au hameçonnage).
- **Authentification multifacteur (MFA)** : TOTP, SMS (moins sûr), clé matérielle.
- **SSO d'entreprise** (SAML, OIDC).

### Types de session

| Type | Principe | Avantages | Inconvénients |
|---|---|---|---|
| **Sans état (stateless)** | Un **jeton signé/chiffré** (JWT) est stocké dans un cookie | Pas de base de sessions, rapide | Révocation difficile, taille limitée |
| **En base de données** | Un **identifiant de session opaque** dans le cookie ; données en base/Redis | Révocation immédiate, contrôle total | Une lecture par requête |

### Cookie de session sécurisé

| Attribut | Rôle |
|---|---|
| `HttpOnly` | Inaccessible au JavaScript (limite le vol via XSS) |
| `Secure` | Envoyé en HTTPS uniquement |
| `SameSite=Lax` (ou `Strict`) | Limite l'envoi inter-sites (défense CSRF) |
| `Path=/` | Portée |
| `Expires` / `Max-Age` | Durée de vie |

## 16.2 Session sans état avec `jose`

```bash
npm install jose
openssl rand -base64 32   # générer SESSION_SECRET
```

```ts
// lib/session.ts
import "server-only";
import { SignJWT, jwtVerify } from "jose";
import { cookies } from "next/headers";

const cle = new TextEncoder().encode(process.env.SESSION_SECRET);

type Payload = { userId: string; role: "user" | "admin"; expiresAt: number };

export async function chiffrer(payload: Payload) {
  return new SignJWT(payload)
    .setProtectedHeader({ alg: "HS256" })
    .setIssuedAt()
    .setExpirationTime("7d")
    .sign(cle);
}

export async function dechiffrer(jeton: string | undefined) {
  if (!jeton) return null;
  try {
    const { payload } = await jwtVerify(jeton, cle, { algorithms: ["HS256"] });
    return payload as unknown as Payload;
  } catch {
    return null;
  }
}

export async function creerSession(userId: string, role: "user" | "admin") {
  const expiresAt = Date.now() + 7 * 24 * 60 * 60 * 1000;
  const jeton = await chiffrer({ userId, role, expiresAt });
  (await cookies()).set("session", jeton, {
    httpOnly: true,
    secure: true,
    sameSite: "lax",
    path: "/",
    expires: new Date(expiresAt),
  });
}

export async function supprimerSession() {
  (await cookies()).delete("session");
}
```

> Un JWT **signé** (HS256) est **lisible** par le client (non chiffré). N'y placez aucune donnée sensible ; utilisez un chiffrement (JWE) si nécessaire.

## 16.3 Connexion et déconnexion (Server Actions)

```ts
// app/login/actions.ts
"use server";
import { z } from "zod";
import bcrypt from "bcryptjs";
import { redirect } from "next/navigation";
import { creerSession, supprimerSession } from "@/lib/session";

const Schema = z.object({ email: z.string().email(), motDePasse: z.string().min(8) });

export async function connexion(_prev: unknown, formData: FormData) {
  const parsed = Schema.safeParse({
    email: formData.get("email"),
    motDePasse: formData.get("motDePasse"),
  });
  if (!parsed.success) return { erreur: "Identifiants invalides" };

  const user = await db.user.findUnique({ where: { email: parsed.data.email } });
  const ok = user && (await bcrypt.compare(parsed.data.motDePasse, user.motDePasseHash));
  if (!ok) return { erreur: "Identifiants invalides" };   // message identique : pas d'énumération de comptes

  await creerSession(user.id, user.role);
  redirect("/dashboard");
}

export async function deconnexion() {
  await supprimerSession();
  redirect("/login");
}
```

Bonnes pratiques de connexion : message d'erreur **générique**, **limitation de débit**, **délai constant** de comparaison, verrouillage progressif, MFA pour les comptes sensibles.

## 16.4 Autoriser à plusieurs niveaux

### Niveau 1 — Proxy : vérification **optimiste**

```ts
// proxy.ts
import { NextResponse, type NextRequest } from "next/server";
import { dechiffrer } from "@/lib/session";

const protegees = ["/dashboard", "/admin"];

export async function proxy(request: NextRequest) {
  const estProtegee = protegees.some((p) => request.nextUrl.pathname.startsWith(p));
  const session = await dechiffrer(request.cookies.get("session")?.value);

  if (estProtegee && !session) return NextResponse.redirect(new URL("/login", request.url));
  return NextResponse.next();
}

export const config = { matcher: ["/((?!api|_next/static|_next/image|.*\\.png$).*)"] };
```

⚠️ Optimiste = rapide mais **non suffisant** (pas d'accès base de données, contournable en cas de faille).

### Niveau 2 — Data Access Layer (DAL) : vérification **sûre**

```ts
// lib/dal.ts
import "server-only";
import { cache } from "react";
import { cookies } from "next/headers";
import { redirect } from "next/navigation";
import { dechiffrer } from "./session";

export const verifierSession = cache(async () => {
  const jeton = (await cookies()).get("session")?.value;
  const session = await dechiffrer(jeton);
  if (!session?.userId) redirect("/login");
  return { userId: session.userId, role: session.role };
});

export const getUtilisateur = cache(async () => {
  const { userId } = await verifierSession();
  const user = await db.user.findUnique({ where: { id: userId } });
  return user ? { id: user.id, nom: user.nom, email: user.email } : null; // DTO
});
```

### Niveau 3 — Composants et actions

```tsx
// Server Component
import { verifierSession } from "@/lib/dal";
import { forbidden } from "next/navigation";

export default async function Admin() {
  const { role } = await verifierSession();
  if (role !== "admin") forbidden();   // nécessite experimental.authInterrupts
  return <AdminPanel />;
}
```

```ts
// Server Action
"use server";
export async function supprimerUtilisateur(id: string) {
  const { role } = await verifierSession();
  if (role !== "admin") throw new Error("Interdit");
  await db.user.delete({ where: { id } });
}
```

### Piège majeur : les layouts

Un **layout ne se re-rend pas** à chaque navigation entre pages enfants (rendu partiel). **Ne placez pas votre contrôle d'accès uniquement dans un layout** : une page enfant pourrait être servie sans revérification. Vérifiez l'accès **dans la page** et/ou **au moment de l'accès aux données** (DAL).

### Autorisation par rôles (RBAC)

```ts
const permissions = { user: ["lire"], editeur: ["lire", "ecrire"], admin: ["lire", "ecrire", "supprimer"] } as const;
export function peut(role: keyof typeof permissions, action: string) {
  return (permissions[role] as readonly string[]).includes(action);
}
```

Pour des règles plus fines : **ABAC** (basé sur attributs), **ReBAC** (relations), ou des bibliothèques dédiées (CASL, Oso, OpenFGA).

## 16.5 Bibliothèques et services

| Solution | Type | Notes |
|---|---|---|
| **Auth.js (NextAuth)** | Bibliothèque open source | OAuth, e-mail, credentials ; adaptateurs de bases de données |
| **Better Auth** | Bibliothèque open source TypeScript | Plugins MFA, organisations, passkeys |
| **Clerk** | Service hébergé | UI prête à l'emploi, gestion d'organisations |
| **Auth0**, **WorkOS**, **Kinde**, **Stytch**, **Descope** | Services | SSO/entreprise, MFA |
| **Supabase Auth**, **Firebase Auth** | BaaS | Intégré au backend associé |

Critères de choix : coût, hébergement des données, SSO, MFA, passkeys, personnalisation de l'UI, verrouillage fournisseur, maturité et maintenance.

## 16.6 Sécurité complémentaire

- **CSRF** : cookies `SameSite`, contrôle d'origine des Server Actions (intégré).
- **XSS** : échappement par défaut de React ; **ne jamais** utiliser `dangerouslySetInnerHTML` avec du contenu non nettoyé (utilisez DOMPurify) ; **CSP** avec *nonce* (via proxy).
- **Rate limiting** : connexion, réinitialisation de mot de passe, API publiques.
- **Journalisation** des événements d'authentification.
- **Rotation et expiration** des sessions ; invalidation à la déconnexion/changement de mot de passe.
- **Secrets** hors du dépôt ; rotation des clés.
- **Mots de passe** : longueur minimale, vérification contre les fuites connues, pas de règles de composition rigides.
- **Réinitialisation de mot de passe** : jetons à usage unique, courte durée, stockés hachés.

## Pièges courants

- **Vérifier l'auth seulement dans le proxy ou le layout.**
- **Stocker des données sensibles dans un JWT non chiffré.**
- **Message d'erreur distinguant « email inconnu » et « mauvais mot de passe »** (énumération de comptes).
- **Cookie sans `HttpOnly`/`Secure`.**
- **Renvoyer l'objet utilisateur complet** (avec hash) aux composants.

## À retenir

- Authentifier → créer une session → **autoriser au plus près des données**.
- Proxy = optimiste ; DAL = source de vérité.
- Cookies `HttpOnly` + `Secure` + `SameSite`.
- Ne réinventez pas la cryptographie ; envisagez une bibliothèque éprouvée.

## Exercices

1. Implémentez login/logout avec session JWT dans un cookie.
2. Créez un `verifierSession()` mis en cache avec `React.cache` et utilisez-le dans trois pages.
3. Ajoutez un rôle `admin` et protégez une Server Action de suppression.

---

# Chapitre 17 — Internationalisation (i18n)

## Objectifs

- Mettre en place un routage par langue dans l'App Router.
- Charger des dictionnaires de traductions côté serveur.
- Détecter la langue, gérer le SEO multilingue, formater dates et nombres.

## 17.1 Concepts

| Terme | Définition |
|---|---|
| **i18n** (internationalisation) | Préparer l'application à plusieurs langues/régions |
| **l10n** (localisation) | Adapter le contenu à une langue/région précise |
| **Locale** | Code langue-région : `fr`, `fr-FR`, `en-US`, `ar-MA` |
| **RTL** | Écriture de droite à gauche (arabe, hébreu) : `dir="rtl"` |
| **Pluriels / genre / ICU** | Règles linguistiques complexes (`{count, plural, one {# élément} other {# éléments}}`) |

## 17.2 Stratégies de routage

| Stratégie | Exemple | Remarques |
|---|---|---|
| **Sous-chemin** | `/fr/blog`, `/en/blog` | Simple, bon pour le SEO, recommandé |
| **Sous-domaine** | `fr.exemple.com` | Séparation nette |
| **Domaine dédié** | `exemple.fr`, `exemple.com` | Marché par pays |
| **Cookie / en-tête** (sans URL) | `/blog` | Moins bon pour le SEO (une URL, plusieurs contenus) |

## 17.3 Mise en place avec un segment `[lang]`

> **App Router** : pas d'option `i18n` intégrée dans `next.config`. On utilise un **segment dynamique** et le **proxy**.

```
app/
└── [lang]/
    ├── layout.tsx
    ├── page.tsx
    └── dictionaries/
        ├── fr.json
        └── en.json
```

### Dictionnaires

```json
// app/[lang]/dictionaries/fr.json
{ "accueil": { "titre": "Bienvenue", "cta": "Commencer" } }
```

```ts
// app/[lang]/dictionaries.ts
import "server-only";

const dictionnaires = {
  fr: () => import("./dictionaries/fr.json").then((m) => m.default),
  en: () => import("./dictionaries/en.json").then((m) => m.default),
};

export type Locale = keyof typeof dictionnaires;
export const hasLocale = (l: string): l is Locale => l in dictionnaires;
export const getDictionary = async (l: Locale) => dictionnaires[l]();
```

### Layout et page

```tsx
// app/[lang]/layout.tsx
import { notFound } from "next/navigation";
import { hasLocale } from "./dictionaries";

export async function generateStaticParams() {
  return [{ lang: "fr" }, { lang: "en" }];
}

export default async function Layout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ lang: string }>;
}) {
  const { lang } = await params;
  if (!hasLocale(lang)) notFound();
  return (
    <html lang={lang} dir={lang === "ar" ? "rtl" : "ltr"}>
      <body>{children}</body>
    </html>
  );
}
```

```tsx
// app/[lang]/page.tsx
import { getDictionary, hasLocale } from "./dictionaries";
import { notFound } from "next/navigation";

export default async function Page({ params }: { params: Promise<{ lang: string }> }) {
  const { lang } = await params;
  if (!hasLocale(lang)) notFound();
  const t = await getDictionary(lang);
  return <h1>{t.accueil.titre}</h1>;
}
```

Les dictionnaires étant chargés **côté serveur**, ils **n'alourdissent pas** le bundle client.

## 17.4 Détection de la langue et redirection (Proxy)

```bash
npm install @formatjs/intl-localematcher negotiator
npm install --save-dev @types/negotiator
```

```ts
// proxy.ts
import { NextResponse, type NextRequest } from "next/server";
import { match } from "@formatjs/intl-localematcher";
import Negotiator from "negotiator";

const locales = ["fr", "en"];
const defaut = "fr";

function getLocale(request: NextRequest) {
  const entetes = { "accept-language": request.headers.get("accept-language") ?? "" };
  const langues = new Negotiator({ headers: entetes }).languages();
  return match(langues, locales, defaut);
}

export function proxy(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const aLocale = locales.some((l) => pathname === `/${l}` || pathname.startsWith(`/${l}/`));
  if (aLocale) return;

  const locale = request.cookies.get("NEXT_LOCALE")?.value ?? getLocale(request);
  request.nextUrl.pathname = `/${locale}${pathname}`;
  return NextResponse.redirect(request.nextUrl);
}

export const config = {
  matcher: ["/((?!_next|api|favicon.ico|.*\\..*).*)"],
};
```

Ordre de détection habituel : **URL** > **cookie** (choix mémorisé) > **`Accept-Language`** > langue par défaut.

## 17.5 SEO multilingue

```tsx
export async function generateMetadata({ params }: { params: Promise<{ lang: string }> }) {
  const { lang } = await params;
  return {
    alternates: {
      canonical: `https://exemple.com/${lang}`,
      languages: { fr: "https://exemple.com/fr", en: "https://exemple.com/en", "x-default": "https://exemple.com/fr" },
    },
  };
}
```

- Balises **`hreflang`** (via `alternates.languages`) pour relier les versions.
- `<html lang="...">` correct.
- **Sitemap** listant toutes les versions linguistiques.
- Ne **pas** rediriger automatiquement les robots uniquement selon `Accept-Language` sans offrir d'URL stables par langue.

## 17.6 Formatage selon la locale

Utilisez l'API native **`Intl`** :

```ts
new Intl.DateTimeFormat("fr-FR", { dateStyle: "long" }).format(new Date());       // 14 novembre 2026
new Intl.NumberFormat("fr-FR", { style: "currency", currency: "EUR" }).format(1234.5); // 1 234,50 €
new Intl.RelativeTimeFormat("fr", { numeric: "auto" }).format(-1, "day");         // hier
new Intl.PluralRules("fr").select(2);                                             // "other"
new Intl.ListFormat("fr", { type: "conjunction" }).format(["a", "b", "c"]);       // a, b et c
```

## 17.7 Bibliothèques

| Bibliothèque | Points forts |
|---|---|
| **next-intl** | Conçue pour l'App Router : routage, `useTranslations`/`getTranslations`, ICU, formatage, middleware/proxy de locale |
| **next-international** | Typage fort des clés |
| **react-i18next / i18next** | Écosystème large, fonctionne côté client et serveur |
| **Paraglide (inlang)** | Messages compilés, bundles réduits |
| **Lingui** | Extraction de messages, ICU |

Avec une bibliothèque, vous gagnez : pluriels ICU, interpolation sûre, typage des clés, outils d'extraction, gestion du routage.

## 17.8 Pages Router (historique)

Le Pages Router propose une configuration **native** :

```ts
// next.config.ts
const nextConfig = {
  i18n: { locales: ["fr", "en"], defaultLocale: "fr", localeDetection: true },
};
```

Next.js gère alors le préfixe de locale et l'objet `locale` (`useRouter().locale`). Cette option **n'existe pas** dans l'App Router.

## Pièges courants

- **Oublier `await params`** avant de lire `lang`.
- **Charger tous les dictionnaires côté client** (bundle gonflé).
- **Dupliquer le contenu** sans canonical/hreflang.
- **Concaténer des chaînes** au lieu d'utiliser des messages ICU (pluriels et ordre des mots).
- **Oublier `dir="rtl"`** pour les langues RTL.

## À retenir

- Sous-chemin `[lang]` + proxy de détection + dictionnaires côté serveur.
- SEO : `hreflang`, canonical, sitemap par langue.
- `Intl` pour formater dates, nombres, pluriels.

## Exercices

1. Ajoutez `fr` et `en` avec un sélecteur de langue qui enregistre un cookie `NEXT_LOCALE`.
2. Générez un sitemap listant les versions FR et EN de chaque article.
3. Formatez une date et un prix selon la locale.

---

# Chapitre 18 — Configuration

## Objectifs

- Maîtriser `next.config.ts` : redirections, réécritures, en-têtes, images, sortie.
- Configurer Turbopack/Webpack, les paquets externes, les options expérimentales.
- Appliquer des en-têtes de sécurité.

## 18.1 Le fichier de configuration

Fichiers acceptés : `next.config.ts`, `next.config.js`, `next.config.mjs`, `next.config.cjs`.

```ts
// next.config.ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  /* options */
};

export default nextConfig;
```

Forme **fonction** (accès à la phase de lancement) :

```ts
import { PHASE_DEVELOPMENT_SERVER } from "next/constants";
import type { NextConfig } from "next";

export default function (phase: string): NextConfig {
  if (phase === PHASE_DEVELOPMENT_SERVER) return { /* dev */ };
  return { /* production */ };
}
```

Le fichier est lu **au démarrage** de Next.js (pas à chaque requête, pas inclus dans le bundle client) : **redémarrez** le serveur après modification.

## 18.2 Options générales

| Option | Rôle |
|---|---|
| `reactStrictMode` | Active le Strict Mode de React (double rendu en dev pour détecter les effets de bord) — activé par défaut avec l'App Router |
| `basePath` | Préfixe de chemin si l'app est servie sous un sous-chemin (`/docs`) |
| `assetPrefix` | Préfixe d'URL des ressources statiques (CDN) |
| `trailingSlash` | `true` : `/about/` plutôt que `/about` |
| `output` | `"standalone"` (déploiement minimal Node), `"export"` (statique) |
| `distDir` | Dossier de build (défaut `.next`) |
| `generateBuildId` | Identifiant de build personnalisé (utile en multi-instances) |
| `compress` | Compression gzip des réponses (désactivez si un reverse proxy compresse) |
| `poweredByHeader` | `false` pour retirer l'en-tête `X-Powered-By` |
| `pageExtensions` | Extensions considérées comme pages |
| `typedRoutes` | Routes typées (chapitre 20) |
| `cacheComponents` | Active le modèle Cache Components |
| `cacheLife` | Profils de durée de cache personnalisés |
| `reactCompiler` | Active le React Compiler |
| `serverExternalPackages` | Paquets non bundlés côté serveur (modules natifs, ORM) |
| `transpilePackages` | Paquets (monorepo) à transpiler |
| `allowedDevOrigins` | Origines autorisées à accéder au serveur de dev |
| `logging` | Journalisation (par exemple des `fetch`) |
| `env` | Variables inlinées au build (préférez les fichiers `.env`) |
| `experimental` | Fonctionnalités non stables |

## 18.3 Redirections

```ts
async redirects() {
  return [
    { source: "/ancien", destination: "/nouveau", permanent: true },           // 308
    { source: "/blog/:slug", destination: "/articles/:slug", permanent: false },// 307
    { source: "/:path((?!public).*)", destination: "/maintenance", permanent: false,
      has: [{ type: "cookie", key: "maintenance", value: "on" }] },
  ];
},
```

- `permanent: true` → **308** ; `false` → **307**.
- Paramètres de chemin (`:slug`, `:path*`), conditions `has` / `missing` (en-tête, cookie, query, host).
- Exécutées **avant** le proxy (voir chapitre 11).

## 18.4 Réécritures

```ts
async rewrites() {
  return {
    beforeFiles: [{ source: "/blog", destination: "/actualites" }],
    afterFiles: [{ source: "/api/:path*", destination: "https://api.exemple.com/:path*" }],
    fallback: [{ source: "/:path*", destination: "https://ancien-site.exemple.com/:path*" }],
  };
},
```

- **Sans changement d'URL** visible : c'est un **proxy transparent**.
- Usages : masquer un domaine d'API (évite le CORS), migration progressive d'un ancien site (`fallback`), multi-zones.
- Forme simple : retourner directement un tableau (équivalent à `afterFiles`).

## 18.5 En-têtes HTTP

```ts
async headers() {
  return [
    {
      source: "/(.*)",
      headers: [
        { key: "X-Content-Type-Options", value: "nosniff" },
        { key: "X-Frame-Options", value: "DENY" },
        { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
        { key: "Permissions-Policy", value: "camera=(), microphone=(), geolocation=()" },
        { key: "Strict-Transport-Security", value: "max-age=63072000; includeSubDomains; preload" },
      ],
    },
    {
      source: "/static/:path*",
      headers: [{ key: "Cache-Control", value: "public, max-age=31536000, immutable" }],
    },
  ];
},
```

### Politique de sécurité du contenu (CSP)

- **Statique** : `Content-Security-Policy` dans `headers()` (ne permet pas de *nonce* par requête).
- **Avec *nonce*** : générer un nonce par requête dans le proxy et l'injecter dans l'en-tête CSP ; cela rend les pages **dynamiques** (le nonce change à chaque requête). Exemple de directive : `script-src 'self' 'nonce-XXXX' 'strict-dynamic'`.
- En développement, `'unsafe-eval'` est parfois nécessaire (Fast Refresh) ; ne le laissez pas en production.

| En-tête | Protège contre |
|---|---|
| `Content-Security-Policy` | XSS, injection de ressources |
| `X-Frame-Options` / `frame-ancestors` | Clickjacking |
| `X-Content-Type-Options` | Interprétation MIME erronée |
| `Referrer-Policy` | Fuite d'URL via `Referer` |
| `Strict-Transport-Security` | Rétrogradation HTTP |
| `Permissions-Policy` | Accès non voulu aux API du navigateur |

## 18.6 Sortie de build : `output`

| Valeur | Effet |
|---|---|
| (absent) | Build standard ; nécessite `node_modules` à l'exécution |
| `"standalone"` | Produit `.next/standalone` : serveur minimal avec **uniquement** les dépendances utilisées (idéal Docker) |
| `"export"` | Site statique dans `out/` (voir chapitre 8) |

## 18.7 Turbopack et Webpack

```ts
const nextConfig: NextConfig = {
  turbopack: {
    resolveAlias: { "ancien-module": "nouveau-module" },
    rules: {
      "*.svg": { loaders: ["@svgr/webpack"], as: "*.js" },
    },
  },
};
```

- Turbopack est le bundler **par défaut** ; l'option `turbopack` est un champ **de premier niveau** (⚠️ Version 16 ; auparavant sous `experimental.turbopack`).
- Pour rester sur **Webpack** : `next build --webpack`, et personnalisation via :

```ts
webpack: (config, { isServer }) => {
  config.module.rules.push({ test: /\.svg$/, use: ["@svgr/webpack"] });
  return config;
},
```

> Si une fonction `webpack` personnalisée existe et que vous lancez Turbopack, le build échoue pour signaler l'incompatibilité : basculez vers `--webpack` ou migrez la configuration.

## 18.8 Autres notions de configuration

- **Alias de chemins** : `tsconfig.json` (`paths`) — Next.js les lit automatiquement.
- **Monorepo** : `transpilePackages`, `outputFileTracingRoot`.
- **Logs de requêtes `fetch`** : `logging: { fetches: { fullUrl: true } }`.
- **Indicateurs de dev** : `devIndicators`.
- **Sécurité des origines en dev** : `allowedDevOrigins: ["*.local"]` si accès depuis un autre appareil.
- **Taille du corps des actions** : `experimental.serverActions.bodySizeLimit`.
- **TypeScript/ESLint au build** : `typescript: { ignoreBuildErrors: true }` (déconseillé).

## Pièges courants

- **Modifier `next.config` sans redémarrer**.
- **`rewrites` vers une API sans contrôle d'accès**.
- **CSP trop stricte** qui bloque vos propres scripts (testez en mode *report-only* d'abord).
- **Mélanger options Webpack et Turbopack**.

## À retenir

- `next.config.ts` centralise redirections, réécritures, en-têtes, images, sortie, bundler.
- En-têtes de sécurité systématiques.
- `output: "standalone"` pour Docker.

## Exercices

1. Ajoutez les en-têtes de sécurité de base et vérifiez-les dans l'onglet Réseau.
2. Redirigez `/ancien-blog/:slug` vers `/blog/:slug` en 308.
3. Utilisez un `rewrite` pour proxifier `/api-externe/*` vers un service tiers.

---

# Chapitre 19 — Variables d'environnement

## Objectifs

- Utiliser les fichiers `.env` et comprendre leur ordre de priorité.
- Distinguer variables serveur et publiques.
- Valider et sécuriser la configuration.

## 19.1 Fichiers `.env`

| Fichier | Environnement | Commité ? |
|---|---|---|
| `.env` | Toujours (valeurs par défaut) | Oui (sans secrets) |
| `.env.development` | `next dev` | Oui |
| `.env.production` | `next build`/`next start` | Oui |
| `.env.test` | Tests (`NODE_ENV=test`) | Oui |
| `.env.local` | Local, **prioritaire** (sauf test) | **Non** |
| `.env.development.local`, `.env.production.local`, `.env.test.local` | Surcharge locale par environnement | **Non** |

### Ordre de priorité (du plus au moins prioritaire)

1. `process.env` (variables réelles du système/CI)
2. `.env.$(NODE_ENV).local`
3. `.env.local` (non chargé quand `NODE_ENV=test`)
4. `.env.$(NODE_ENV)`
5. `.env`

### Syntaxe et expansion

```bash
# .env
DATABASE_URL="postgres://user:pass@localhost:5432/app"
APP_URL=http://localhost:3000
CALLBACK=$APP_URL/auth/callback      # expansion de variable
```

(`\$` pour un dollar littéral.)

## 19.2 Variables côté serveur et côté client

```ts
process.env.DATABASE_URL                 // serveur uniquement
process.env.NEXT_PUBLIC_API_URL          // disponible aussi côté navigateur
```

- **Sans préfixe** : accessible **uniquement côté serveur** (Server Components, Server Actions, Route Handlers, Proxy). Dans le code client, la valeur est **absente**.
- **`NEXT_PUBLIC_`** : **inlinée dans le bundle JavaScript au moment du build** (remplacement textuel). Donc :
  - **visible par tout le monde** : jamais de secret ici ;
  - **figée au build** : changer la variable exige de **reconstruire** (une même image Docker ne peut pas servir plusieurs environnements avec des valeurs `NEXT_PUBLIC_` différentes sans rebuild).
- L'inlining ne fonctionne que pour un accès **statique** : `process.env.NEXT_PUBLIC_X` est remplacé, mais pas `process.env[nom]` ni la déstructuration dynamique.

### Lire des variables à l'**exécution** (runtime)

Pour des valeurs qui changent selon l'environnement de déploiement **sans rebuild** :

- Lire `process.env.MA_VARIABLE` dans un **Server Component dynamique** (après `await connection()` si besoin), puis la **passer en prop** au client ;
- ou exposer un Route Handler `/api/config`.

⚠️ `serverRuntimeConfig` / `publicRuntimeConfig` ont été **supprimés** (Next.js 16).

## 19.3 Validation de la configuration

Échouez **tôt** si une variable manque ou est invalide :

```ts
// lib/env.ts
import "server-only";
import { z } from "zod";

const schema = z.object({
  DATABASE_URL: z.string().url(),
  SESSION_SECRET: z.string().min(32),
  STRIPE_SECRET_KEY: z.string().startsWith("sk_"),
});

export const env = schema.parse(process.env);
```

Pour un schéma client/serveur unifié : bibliothèques comme `@t3-oss/env-nextjs`.

## 19.4 Variables et environnement de test / scripts

Hors de Next.js (scripts, tests Jest/Vitest), chargez les fichiers `.env` avec `@next/env` :

```ts
import { loadEnvConfig } from "@next/env";
loadEnvConfig(process.cwd());
```

## 19.5 Bonnes pratiques

- **Jamais** de secrets dans le dépôt, ni dans `NEXT_PUBLIC_*`.
- Fournir un **`.env.example`** (sans valeurs sensibles) pour l'équipe.
- Utiliser le **gestionnaire de secrets** de la plateforme (Vercel, AWS Secrets Manager, Vault, Kubernetes Secrets).
- **Rotation** régulière des clés ; clés distinctes par environnement.
- Principe du **moindre privilège** (clé d'API restreinte).
- Valider les variables au démarrage.

## Pièges courants

- **Préfixer par `NEXT_PUBLIC_` une clé secrète** : exposée publiquement.
- **Changer une variable `NEXT_PUBLIC_` sans rebuild**.
- **Commiter `.env.local`**.
- **Oublier de définir les variables dans l'environnement de production**.

## À retenir

- Sans préfixe = serveur ; `NEXT_PUBLIC_` = public et figé au build.
- Priorité : `process.env` > `.env.*.local` > `.env.local` > `.env.*` > `.env`.
- Validez avec un schéma.

## Exercices

1. Créez `lib/env.ts` avec validation Zod et faites échouer le build sur une variable manquante.
2. Vérifiez qu'une variable sans préfixe est `undefined` dans un Client Component.

---

# Chapitre 20 — TypeScript

## Objectifs

- Configurer TypeScript pour Next.js.
- Utiliser les types fournis (Metadata, NextConfig, props de pages, routes typées).
- Typer Server Actions, params et données.

## 20.1 Mise en place

- Créez un fichier `.ts`/`.tsx` : Next.js propose d'installer TypeScript et génère `tsconfig.json` et `next-env.d.ts`.
- Exigence : TypeScript ≥ 5.1 (⚠️ Version 16).

```json
// tsconfig.json (extrait typique)
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "strict": true,
    "noEmit": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "incremental": true,
    "plugins": [{ "name": "next" }],
    "paths": { "@/*": ["./src/*"] }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

- Le **plugin `next`** de l'éditeur vérifie les directives, les options de segment, les types d'exports de pages/layouts.
- `next-env.d.ts` : ne pas modifier.
- `strict: true` : fortement recommandé.
- La vérification de types s'exécute pendant `next build` (une erreur de type fait échouer le build).

## 20.2 Types fournis par Next.js

```ts
import type { Metadata, Viewport, NextConfig } from "next";
import type { NextRequest, NextResponse } from "next/server";
import type { MetadataRoute } from "next";
```

### Pages, layouts, params (⚠️ asynchrones)

```tsx
export default async function Page({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string }>;
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}) {
  const { slug } = await params;
  const sp = await searchParams;
  /* ... */
}
```

### Helpers de types générés : `PageProps`, `LayoutProps`, `RouteContext`

Disponibles globalement après génération des types (au `next dev`, `next build` ou via **`npx next typegen`**) :

```tsx
export default async function Page(props: PageProps<"/blog/[slug]">) {
  const { slug } = await props.params;           // typé : string
  return <h1>{slug}</h1>;
}

export default function Layout(props: LayoutProps<"/dashboard">) {
  return <section>{props.children}</section>;   // les slots de routes parallèles sont aussi typés
}

export async function GET(_req: Request, ctx: RouteContext<"/api/posts/[id]">) {
  const { id } = await ctx.params;
  return Response.json({ id });
}
```

## 20.3 Routes typées (`typedRoutes`)

```ts
// next.config.ts
const nextConfig = { typedRoutes: true };
```

Next.js génère un type **`Route`** : un `href` inexistant provoque une **erreur de compilation**.

```tsx
import Link from "next/link";
<Link href="/blog/mon-article">OK</Link>
<Link href="/page-inexistante">Erreur de type</Link>
```

Pour un lien dynamique construit à l'exécution : `href={url as Route}` (avec prudence).

## 20.4 Bonnes pratiques de typage

- **Valider à la frontière** (Zod) puis **inférer** les types : `type Entree = z.infer<typeof Schema>`.
- Typer les **DTO** retournés par la couche d'accès aux données.
- Utiliser **`satisfies`** pour vérifier un objet sans élargir son type :

```ts
export const metadata = { title: "Accueil" } satisfies Metadata;
```

- **Props de composants** : interfaces explicites ; `React.ReactNode` pour `children`.
- **Server Actions** :

```ts
type Etat = { ok: true } | { ok: false; erreurs: Record<string, string[]> };
export async function sauver(_prev: Etat | null, fd: FormData): Promise<Etat> { /* ... */ }
```

- **Variables d'environnement** : déclarez-les (schéma Zod ou `declare namespace NodeJS { interface ProcessEnv { ... } }`).
- Éviter `any` ; préférer `unknown` + validation.

## 20.5 Erreurs fréquentes

| Erreur | Cause | Correctif |
|---|---|---|
| « `params` is a Promise » | Types de Next.js 15/16 | `Promise<{...}>` + `await` |
| Type de page invalide | Export non autorisé dans `page.tsx` | N'exporter que les éléments permis (`default`, `metadata`, `generateMetadata`, options de segment…) |
| `Cannot find module '@/...'` | Alias non configuré | `paths` dans `tsconfig` |
| Build échoue sur un type | Vérification de types à la compilation | Corriger (éviter `ignoreBuildErrors`) |

## À retenir

- `strict`, plugin `next`, `next-env.d.ts`.
- Helpers `PageProps`/`LayoutProps`/`RouteContext` + `typedRoutes`.
- Valider puis inférer ; typer les frontières (actions, handlers, DTO).

## Exercices

1. Activez `typedRoutes` et corrigez un lien invalide.
2. Convertissez une page à `PageProps<"/blog/[slug]">`.
3. Typez une Server Action avec une union discriminée d'états.

---

# Chapitre 21 — Tests

## Objectifs

- Choisir le bon type de test pour chaque couche.
- Configurer Jest ou Vitest, et Playwright/Cypress.
- Tester composants, utilitaires, actions et parcours utilisateur.

## 21.1 Pyramide de tests

| Niveau | Outils | Cible | Quantité |
|---|---|---|---|
| **Unitaires** | Jest, Vitest | Fonctions pures, validations, DAL (avec mocks) | Beaucoup |
| **Composants** | React Testing Library | Client Components, comportements d'UI | Moyen |
| **Intégration** | Vitest/Jest + base de test | Server Actions, Route Handlers | Moyen |
| **End-to-end (E2E)** | Playwright, Cypress | Parcours complets dans un vrai navigateur | Peu, critiques |
| **Visuels / a11y** | Storybook, axe | Régressions visuelles, accessibilité | Selon besoin |

> **Important** : les **Server Components asynchrones** sont mal supportés par les testeurs unitaires (React Testing Library ne sait pas les rendre). **Testez-les en E2E**, ou extrayez la logique dans des fonctions testables unitairement.

## 21.2 Vitest + React Testing Library

```bash
npm install -D vitest @vitejs/plugin-react jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom vite-tsconfig-paths
```

```ts
// vitest.config.mts
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";
import tsconfigPaths from "vite-tsconfig-paths";

export default defineConfig({
  plugins: [tsconfigPaths(), react()],
  test: { environment: "jsdom", setupFiles: ["./vitest.setup.ts"] },
});
```

```ts
// vitest.setup.ts
import "@testing-library/jest-dom/vitest";
```

```tsx
// __tests__/compteur.test.tsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { expect, test } from "vitest";
import Compteur from "@/components/Compteur";

test("incrémente au clic", async () => {
  render(<Compteur />);
  await userEvent.click(screen.getByRole("button"));
  expect(screen.getByRole("button")).toHaveTextContent("1");
});
```

Script : `"test": "vitest"`.

## 21.3 Jest

```bash
npm install -D jest jest-environment-jsdom @testing-library/react @testing-library/jest-dom ts-node @types/jest
```

```ts
// jest.config.ts
import nextJest from "next/jest.js";

const createJestConfig = nextJest({ dir: "./" });   // charge next.config et .env, gère CSS/images/SWC

export default createJestConfig({
  testEnvironment: "jsdom",
  setupFilesAfterEnv: ["<rootDir>/jest.setup.ts"],
  moduleNameMapper: { "^@/(.*)$": "<rootDir>/src/$1" },
});
```


## 21.4 Mocker des modules Next.js

```tsx
import { vi } from "vitest";

vi.mock("next/navigation", () => ({
  useRouter: () => ({ push: vi.fn(), replace: vi.fn(), refresh: vi.fn() }),
  usePathname: () => "/",
  useSearchParams: () => new URLSearchParams(),
}));
```

- `next/image` : se comporte comme un `<img>` en test ; mock rarement nécessaire.
- `next/headers` (`cookies`, `headers`) : mockez pour tester la DAL et les actions.
- Réseau : **MSW** (Mock Service Worker) pour simuler les API.

## 21.5 Tester une Server Action ou la logique serveur

Une Server Action est une **fonction asynchrone** : testez-la comme telle en mockant ses dépendances.

```ts
import { vi, test, expect } from "vitest";
vi.mock("next/cache", () => ({ revalidatePath: vi.fn(), updateTag: vi.fn() }));
vi.mock("@/lib/dal", () => ({ verifierSession: vi.fn().mockResolvedValue({ userId: "1", role: "admin" }) }));

import { supprimerPost } from "@/app/actions";

test("refuse sans droits", async () => {
  /* configurer le mock role: "user" et vérifier l'erreur */
});
```

## 21.6 Playwright (E2E)

```bash
npm init playwright@latest
```

```ts
// playwright.config.ts
import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "./e2e",
  use: { baseURL: "http://localhost:3000", trace: "on-first-retry" },
  webServer: {
    command: "npm run build && npm run start",   // tester la version de production
    url: "http://localhost:3000",
    reuseExistingServer: !process.env.CI,
  },
});
```

```ts
// e2e/connexion.spec.ts
import { test, expect } from "@playwright/test";

test("un utilisateur peut se connecter", async ({ page }) => {
  await page.goto("/login");
  await page.getByLabel("Email").fill("alice@exemple.com");
  await page.getByLabel("Mot de passe").fill("motdepasse123");
  await page.getByRole("button", { name: "Se connecter" }).click();
  await expect(page).toHaveURL("/dashboard");
  await expect(page.getByRole("heading", { name: "Tableau de bord" })).toBeVisible();
});
```

Conseils : sélecteurs **sémantiques** (`getByRole`, `getByLabel`), tests **indépendants**, données de test dédiées, authentification réutilisée via `storageState`, exécution en CI avec rapports/traces.

## 21.7 Cypress

Alternative à Playwright : tests E2E et **tests de composants** (`cypress run --component`). Le support des Server Components asynchrones est limité côté composant ; privilégiez l'E2E.

## 21.8 Accessibilité automatisée

`@axe-core/playwright` ou `jest-axe` détectent une partie des problèmes (contraste, libellés, rôles). Ils **ne remplacent pas** un audit manuel (clavier, lecteurs d'écran).

## 21.9 Bonnes pratiques

- Tester le **comportement** visible, pas l'implémentation.
- Extraire la logique métier hors des composants pour la tester simplement.
- **Base de données de test** isolée (conteneur, SQLite en mémoire, transactions annulées).
- Intégrer les tests, le lint, le type-check et le build dans la **CI**.
- Couverture : un indicateur, pas un objectif absolu.

## Pièges courants

- **Essayer de rendre un Server Component `async` avec RTL**.
- **Tests E2E fragiles** (sélecteurs CSS, attentes fixes `waitForTimeout`).
- **Tester en mode développement** (comportement de cache/prefetch différent).
- **Dépendance à des services externes réels** dans les tests.

## À retenir

- Unitaires/composants (Vitest/Jest + RTL) + E2E (Playwright/Cypress).
- Les Server Components async se testent surtout en E2E.
- Mockez `next/navigation`, `next/headers`, `next/cache`.

## Exercices

1. Testez un Client Component avec Vitest + RTL.
2. Écrivez un test E2E de connexion avec Playwright.
3. Ajoutez un test d'accessibilité sur la page d'accueil.

---

# Chapitre 22 — Déploiement

## Objectifs

- Connaître les modes de déploiement (Node.js, Docker, statique, plateformes).
- Construire une image Docker optimisée.
- Gérer cache, variables, reverse proxy et observabilité en production.

## 22.1 Options de déploiement

| Option | Description | Fonctionnalités |
|---|---|---|
| **Serveur Node.js** | `next build` puis `next start` | **Toutes** |
| **Docker** | Conteneur (souvent `output: "standalone"`) | **Toutes** |
| **Export statique** | HTML/CSS/JS dans `out/` | Limitées (pas de serveur) |
| **Vercel** | Plateforme du créateur de Next.js, zéro config | Toutes, intégrations natives |
| **Autres plateformes** (AWS Amplify, Netlify, Cloudflare, Google Cloud Run, Azure, Fly.io, Railway, Render…) | Adaptateurs/Docker | Variable selon la plateforme |

> **Adaptateurs de build** : Next.js propose une **API d'adaptateurs de build** (stabilisée dans les versions 16.x récentes) pour que les plateformes tierces supportent l'ensemble des fonctionnalités (proxy, cache, ISR). Consultez la documentation de votre hébergeur pour savoir ce qu'il supporte.

## 22.2 Serveur Node.js

```bash
npm ci
npm run build
npm run start      # écoute sur le port 3000 (variable PORT, option -p)
```

- Exécutez derrière un **reverse proxy** (Nginx, Caddy, Traefik) pour TLS, compression, limites.
- Gestionnaire de processus : **PM2**, systemd, Kubernetes.
- `HOSTNAME=0.0.0.0` pour écouter sur toutes les interfaces en conteneur.

## 22.3 Docker avec `standalone`

```ts
// next.config.ts
const nextConfig = { output: "standalone" };
```

```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

FROM node:22-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
# Variables NEXT_PUBLIC_* : à fournir ici (figées au build)
ARG NEXT_PUBLIC_API_URL
ENV NEXT_PUBLIC_API_URL=$NEXT_PUBLIC_API_URL
RUN npm run build

FROM node:22-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
ENV HOSTNAME=0.0.0.0
ENV PORT=3000
RUN addgroup -S nodejs && adduser -S nextjs -G nodejs
COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static
USER nextjs
EXPOSE 3000
CMD ["node", "server.js"]
```

Points essentiels :

- Le dossier **`standalone`** ne contient **pas** `public/` ni `.next/static/` : copiez-les (ou servez-les via un CDN).
- Utilisez un utilisateur **non-root**.
- Les variables **secrètes** sont injectées à l'**exécution** (pas dans l'image).
- Le point d'entrée est `server.js`.
- L'optimisation d'images nécessite `sharp` (inclus automatiquement avec `standalone` dans les versions récentes ; vérifiez pour la vôtre).

## 22.4 Export statique

`output: "export"` + `next build` → dossier `out/` à déposer sur un hébergeur statique (S3 + CloudFront, GitHub Pages, Netlify). Limites : voir chapitre 8. Pensez à `images.unoptimized` ou à un loader externe, et à `trailingSlash` selon l'hébergeur.

## 22.5 Cache, ISR et multi-instances

- Par défaut, le cache est **local à chaque instance** : avec plusieurs conteneurs, les revalidations ne se propagent pas.
- Solution : **handler de cache partagé** (`cacheHandler` / `cacheHandlers`) sur Redis, S3, etc. ; ou plateforme avec cache distribué.
- Un **CDN** devant l'application met en cache les assets (`/_next/static/*` : immutables, 1 an) et, selon l'en-tête `Cache-Control`, certaines pages.
- Cohérence de **build** : utilisez le même `buildId` (`generateBuildId`) sur toutes les instances d'un même déploiement pour éviter les incohérences d'actions/assets.

## 22.6 Streaming derrière un proxy

Le streaming nécessite que le proxy **ne mette pas les réponses en tampon**. Exemple Nginx :

```nginx
location / {
  proxy_pass http://app:3000;
  proxy_http_version 1.1;
  proxy_set_header Host $host;
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  proxy_set_header X-Forwarded-Proto $scheme;
  proxy_buffering off;
}
```

(Ou renvoyer l'en-tête `X-Accel-Buffering: no`.)

## 22.7 Variables d'environnement en production

- `NEXT_PUBLIC_*` : à fournir **au build**.
- Secrets : à l'**exécution**, depuis le gestionnaire de secrets de la plateforme.
- Distinguer `NODE_ENV=production` (défini par `next build/start`) des environnements applicatifs (staging, prod) — utilisez une variable dédiée (`APP_ENV`).

## 22.8 Observabilité

- **Journaux** structurés (JSON), niveaux, identifiants de corrélation.
- **Erreurs** : `instrumentation.ts` + `onRequestError` vers Sentry/Datadog/etc.
- **Traces** : OpenTelemetry via `@vercel/otel` ou le SDK OpenTelemetry.
- **Métriques** : latence, taux d'erreur, mémoire, cache hit ratio.
- **Santé** : endpoint `/api/health` (vérifie base de données, dépendances) pour les sondes de liveness/readiness.

## 22.9 Intégration continue et livraison (CI/CD)

Pipeline type : `npm ci` → lint → type-check (`tsc --noEmit`) → tests unitaires → `next build` → tests E2E sur le build → image Docker → déploiement (blue/green ou canary) → vérifications post-déploiement.

## 22.10 Liste de contrôle avant la mise en production

- [ ] `next build` sans erreur ; tableau des routes conforme.
- [ ] Variables d'environnement définies ; `NEXT_PUBLIC_*` présentes au build.
- [ ] En-têtes de sécurité + HTTPS/HSTS.
- [ ] Domaines d'images (`remotePatterns`) restreints.
- [ ] `robots`/`sitemap` ; pages privées en `noindex`.
- [ ] Gestion des erreurs : `error.tsx`, `global-error.tsx`, `not-found.tsx`.
- [ ] Monitoring, journalisation, alertes.
- [ ] Stratégie de cache et d'invalidation validée (multi-instances).
- [ ] Sauvegardes/migrations de base de données automatisées.
- [ ] Tests E2E des parcours critiques passés.
- [ ] Plan de retour arrière (rollback).

## Pièges courants

- **Oublier de copier `public/` et `.next/static`** dans l'image standalone.
- **Valeurs `NEXT_PUBLIC_` incorrectes** car absentes au build.
- **Cache non partagé** entre instances.
- **Proxy qui met le streaming en tampon**.
- **Exécuter le conteneur en root**.

## À retenir

- Node/Docker = toutes les fonctionnalités ; export statique = limité.
- `standalone` + Docker multi-étapes.
- Cache partagé, buildId cohérent, streaming non bufferisé.

## Exercices

1. Construisez et lancez l'image Docker ci-dessus localement.
2. Ajoutez un endpoint `/api/health` et une sonde Docker `HEALTHCHECK`.
3. Écrivez un pipeline CI exécutant lint, types, tests et build.

---

# Chapitre 23 — Pages Router (historique et migration)

## Objectifs

- Lire et maintenir une application Pages Router.
- Connaître les équivalences avec l'App Router.
- Migrer progressivement.

## 23.1 Structure

```
pages/
├── _app.tsx            # composant racine (layout global, providers)
├── _document.tsx       # HTML personnalisé (<Html>, <Head>, <Main>, <NextScript>)
├── index.tsx           # /
├── about.tsx           # /about
├── blog/
│   ├── index.tsx       # /blog
│   └── [slug].tsx      # /blog/:slug
├── 404.tsx             # page 404 personnalisée
├── 500.tsx             # page 500 personnalisée
└── api/
    └── hello.ts        # API Route
```

- Le **chemin du fichier** détermine l'URL ; chaque fichier = une page.
- Tous les composants sont des **composants clients** « classiques » (pré-rendus puis hydratés) ; **pas de Server Components**.

## 23.2 `_app.tsx` et `_document.tsx`

```tsx
// pages/_app.tsx
import type { AppProps } from "next/app";
import "../styles/globals.css";

export default function App({ Component, pageProps }: AppProps) {
  return (
    <Layout>
      <Component {...pageProps} />
    </Layout>
  );
}
```

```tsx
// pages/_document.tsx
import { Html, Head, Main, NextScript } from "next/document";

export default function Document() {
  return (
    <Html lang="fr">
      <Head />
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}
```

## 23.3 Récupération de données

### `getStaticProps` (SSG / ISR)

```tsx
import type { GetStaticProps } from "next";

export const getStaticProps: GetStaticProps = async () => {
  const posts = await fetch("https://api.exemple.com/posts").then((r) => r.json());
  return {
    props: { posts },
    revalidate: 60,        // ISR : régénération au plus toutes les 60 s
    // notFound: true,     // → 404
    // redirect: { destination: "/", permanent: false },
  };
};

export default function Blog({ posts }: { posts: { id: number; title: string }[] }) {
  return <ul>{posts.map((p) => <li key={p.id}>{p.title}</li>)}</ul>;
}
```

### `getStaticPaths` (routes dynamiques statiques)

```tsx
import type { GetStaticPaths } from "next";

export const getStaticPaths: GetStaticPaths = async () => ({
  paths: [{ params: { slug: "a" } }, { params: { slug: "b" } }],
  fallback: "blocking",   // false → 404 ; true → page de repli puis données ; "blocking" → SSR bloquant puis cache
});
```

### `getServerSideProps` (SSR)

```tsx
import type { GetServerSideProps } from "next";

export const getServerSideProps: GetServerSideProps = async ({ req, res, params, query, locale }) => {
  const session = await getSession(req);
  if (!session) return { redirect: { destination: "/login", permanent: false } };
  return { props: { user: session.user } };
};
```

### Autres

- `getInitialProps` (hérité, déconseillé : désactive l'optimisation statique).
- Récupération **côté client** : SWR / TanStack Query.

## 23.4 API Routes

```ts
// pages/api/posts/[id].ts
import type { NextApiRequest, NextApiResponse } from "next";

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  const { id } = req.query;
  switch (req.method) {
    case "GET":
      return res.status(200).json({ id });
    case "DELETE":
      return res.status(204).end();
    default:
      res.setHeader("Allow", ["GET", "DELETE"]);
      return res.status(405).end(`Méthode ${req.method} non autorisée`);
  }
}
```

## 23.5 Métadonnées, navigation, styles

- **Métadonnées** : `<Head>` de `next/head`.
- **Navigation** : `useRouter` de **`next/router`** (expose `pathname`, `query`, `asPath`, `locale`, `events`).
- **i18n** : option `i18n` native dans `next.config`.
- **Styles** : CSS global **uniquement** dans `_app.tsx`.

```tsx
import Head from "next/head";
<Head><title>Mon titre</title><meta name="description" content="..." /></Head>
```

## 23.6 Table d'équivalences

| Pages Router | App Router |
|---|---|
| `pages/index.tsx` | `app/page.tsx` |
| `_app.tsx` / `_document.tsx` | `app/layout.tsx` (root layout) |
| `getStaticProps` | Server Component `async` + `fetch` (cache) / `"use cache"` |
| `getServerSideProps` | Server Component `async` dynamique (`cookies()`, `connection()`) |
| `getStaticPaths` | `generateStaticParams` |
| `revalidate` (dans `getStaticProps`) | `cacheLife` / options de cache |
| `res.revalidate("/path")` | `revalidatePath` / `revalidateTag` |
| `pages/api/*` | `app/api/*/route.ts` |
| `next/head` | `metadata` / `generateMetadata` |
| `next/router` | `next/navigation` (`useRouter`, `usePathname`, `useSearchParams`) |
| `router.query` | `params` (props), `useParams`, `useSearchParams` |
| `router.events` | Pas d'équivalent direct : effet sur `usePathname`/`useSearchParams` |
| `pages/404.tsx` | `app/not-found.tsx` |
| `pages/_error.tsx` | `error.tsx` / `global-error.tsx` |
| `next.config` `i18n` | Segment `[lang]` + proxy |
| `middleware.ts` | `proxy.ts` (identique entre routeurs) |

## 23.7 Stratégie de migration progressive

Les deux routeurs **coexistent** : on peut migrer **route par route**.

1. **Mettre à niveau** Next.js et React ; exécuter les **codemods** officiels.
2. Créer **`app/layout.tsx`** (balises `<html>`/`<body>`, polices, providers, CSS global).
3. Migrer d'abord les **pages simples** (statiques) ; supprimer la page correspondante de `pages/` (**une URL ne peut exister que dans un routeur**).
4. Remplacer `next/head` par `metadata`.
5. Remplacer les fonctions de données par des **Server Components `async`**.
6. Extraire l'interactivité dans des **Client Components** (`"use client"`).
7. Remplacer `next/router` par `next/navigation`.
8. Migrer les **API Routes** vers des Route Handlers (ou des Server Actions pour les formulaires).
9. Migrer `i18n`, authentification, middleware.
10. Retirer `pages/` quand tout est migré.

Points d'attention : `getServerSideProps` + `req/res` → `cookies()`/`headers()` ; les bibliothèques sans `"use client"` ; l'ordre CSS global ; les tests E2E comme **filet de sécurité** pendant toute la migration.

## À retenir

- Pages Router = pages clientes + fonctions de données dédiées + API Routes ; toujours supporté.
- App Router apporte RSC, layouts imbriqués, streaming, Server Actions, nouveau modèle de cache.
- Migration possible **progressivement**, route par route.

## Exercices

1. Migrez une page `getStaticProps` vers un Server Component avec cache.
2. Migrez une API Route simple vers un Route Handler.
3. Remplacez `next/head` et `useRouter` dans une page migrée.

---

# Chapitre 24 — Bonnes pratiques

## 24.1 Architecture

- **Server Components par défaut** ; frontière `"use client"` la plus basse possible.
- **Colocation** logique ; organisation par fonctionnalité pour les gros projets.
- **Couche d'accès aux données (DAL)** `server-only` : requêtes, autorisations, DTO.
- **Validation** à chaque frontière (formulaires, API, variables d'environnement).
- Fonctions **pures** et testables, séparées de l'UI.
- Éviter les composants « dieux » ; composition plutôt qu'héritage.

## 24.2 Données et cache

- Charger les données **là où elles servent**, en **parallèle** ; éviter les cascades.
- **Streaming** (`Suspense`, `loading.tsx`) pour les zones lentes.
- Mettre en cache **explicitement** (`"use cache"`) avec `cacheLife` et `cacheTag` adaptés.
- Invalider avec `updateTag`/`revalidateTag` après mutation.
- Ne jamais mettre en cache des données personnelles dans un cache partagé.
- Dédupliquer avec `React.cache`.

## 24.3 Sécurité

- **Autorisation côté serveur** dans chaque action, handler et accès aux données.
- **Cookies** `HttpOnly`, `Secure`, `SameSite`.
- **Secrets** hors du code et hors de `NEXT_PUBLIC_*`.
- **En-têtes de sécurité** + CSP ; HTTPS/HSTS.
- Protection contre XSS (pas de `dangerouslySetInnerHTML` non nettoyé), CSRF, injections SQL (requêtes paramétrées/ORM), SSRF (valider les URLs côté serveur), téléversements (type, taille, stockage isolé).
- **Rate limiting** sur les endpoints sensibles.
- **Dépendances** : audit régulier (`npm audit`), mises à jour de sécurité de Next.js/React rapides.
- Ne pas exposer d'erreurs détaillées aux utilisateurs.

## 24.4 Performance

- Réduire le JS client ; `next/dynamic` pour le non critique.
- `next/image`, `next/font`, `next/script`.
- Éviter les décalages de mise en page.
- Mesurer : Core Web Vitals, Lighthouse, RUM.
- Surveiller la taille de bundle en CI.

## 24.5 Accessibilité

- HTML sémantique, hiérarchie de titres, `alt`, libellés de formulaire (`<label>`).
- Navigation **au clavier**, focus visible, gestion du focus dans les modales.
- Contraste suffisant, `prefers-reduced-motion`.
- ARIA seulement si le HTML natif ne suffit pas.
- Annoncer les changements de route et les erreurs (`role="alert"`).

## 24.6 Gestion des erreurs et observabilité

- `error.tsx` par segment critique, `global-error.tsx`, `not-found.tsx`.
- Erreurs **attendues** → valeurs retournées ; **inattendues** → exceptions.
- Journalisation structurée ; suivi des erreurs ; alertes.
- Identifiants de requête pour corréler logs, traces, erreurs.

## 24.7 Qualité de code et outillage

- TypeScript `strict`, ESLint, Prettier, hooks Git (Husky/lint-staged).
- Revues de code avec liste de contrôle (ci-dessous).
- Tests : unitaires + E2E sur les parcours critiques.
- Conventions de nommage et dossiers documentées.
- Mises à jour **régulières** et progressives (ne pas accumuler des versions de retard).

## 24.8 Stratégie de mise à jour

```bash
npx @next/codemod@canary upgrade latest      # met à niveau Next.js/React et applique les codemods
npx @next/codemod@canary next-async-request-api .   # (si besoin) accès asynchrones à params/cookies/headers
npx @next/codemod@canary middleware-to-proxy .      # middleware → proxy
```

1. Lire les **notes de version** et le **guide de migration**.
2. Mettre à jour sur une **branche**, lancer lint/types/tests/build.
3. Tester en **staging**.
4. Déployer progressivement.

## 24.9 Anti-patrons fréquents

| Anti-patron | Pourquoi c'est un problème | Alternative |
|---|---|---|
| `"use client"` en haut de chaque fichier | Perd les bénéfices des RSC | Frontière client minimale |
| `useEffect` + `fetch` pour tout | Cascades, SEO, JS | Server Component `async` |
| Appeler son propre Route Handler depuis un Server Component | Aller-retour inutile | Fonction partagée |
| Auth uniquement dans le proxy/layout | Contournable | DAL + vérif. au plus près des données |
| Tout en `force-dynamic` | Coût, lenteur | Cache explicite + `Suspense` |
| Secrets dans `NEXT_PUBLIC_*` | Fuite | Variables serveur |
| Retourner l'objet utilisateur complet | Fuite de champs sensibles | DTO |
| Ignorer les erreurs de type (`ignoreBuildErrors`) | Bugs en production | Corriger |
| `<img>` partout | Poids, CLS | `next/image` |
| Valider seulement côté client | Contournable | Validation serveur |

## 24.10 Liste de contrôle de revue de code

- [ ] Composant serveur ou client : choix justifié ?
- [ ] Requêtes en parallèle ? Pas de cascade inutile ?
- [ ] Données sensibles filtrées (DTO) ?
- [ ] Autorisation vérifiée côté serveur ?
- [ ] Entrées validées ?
- [ ] Cache/invalidations cohérents ?
- [ ] États de chargement/erreur/vide gérés ?
- [ ] Accessibilité de base respectée ?
- [ ] Métadonnées/SEO présentes ?
- [ ] Tests ajoutés/mis à jour ?
- [ ] Aucune variable d'environnement exposée par erreur ?

---

# Chapitre 25 — Aide-mémoire et glossaire

## 25.1 Importations fréquentes

```ts
import Link from "next/link";
import Image from "next/image";
import dynamic from "next/dynamic";
import Script from "next/script";
import Form from "next/form";
import { Inter } from "next/font/google";
import localFont from "next/font/local";
import { cookies, headers, draftMode } from "next/headers";
import {
  redirect, permanentRedirect, notFound, forbidden, unauthorized,
  useRouter, usePathname, useSearchParams, useParams,
  useSelectedLayoutSegment, useSelectedLayoutSegments,
} from "next/navigation";
import { NextRequest, NextResponse, after, connection, userAgent } from "next/server";
import {
  revalidatePath, revalidateTag, updateTag, refresh, cacheLife, cacheTag,
} from "next/cache";
import { ImageResponse } from "next/og";
import type { Metadata, Viewport, NextConfig, MetadataRoute } from "next";
```

## 25.2 Directives

| Directive | Effet |
|---|---|
| `"use client"` | Frontière Client Component (module + imports) |
| `"use server"` | Server Actions (fichier ou fonction) |
| `"use cache"` | Met en cache le résultat (Cache Components) |
| `"use cache: private"` / `"use cache: remote"` | Variantes avancées |

## 25.3 Fichiers de l'App Router

| Fichier | Rôle |
|---|---|
| `layout` | UI partagée persistante |
| `page` | Route publique |
| `template` | Layout recréé à chaque navigation |
| `loading` | Suspense / chargement |
| `error` / `global-error` | Gestion d'erreurs (client) |
| `not-found` | 404 |
| `route` | Route Handler |
| `default` | Repli de slot parallèle |
| `forbidden` / `unauthorized` | 403 / 401 |
| `proxy` (ex-`middleware`) | Interception de requêtes |
| `instrumentation` | Observabilité |
| `icon`, `apple-icon`, `opengraph-image`, `twitter-image` | Images de métadonnées |
| `sitemap`, `robots`, `manifest` | SEO / PWA |

## 25.4 Segments de route

| Dossier | Signification |
|---|---|
| `nom` | Segment statique |
| `[x]` | Dynamique |
| `[...x]` | Catch-all |
| `[[...x]]` | Catch-all optionnel |
| `(x)` | Groupe (sans effet sur l'URL) |
| `@x` | Slot de route parallèle |
| `(.)x`, `(..)x`, `(..)(..)x`, `(...)x` | Route interceptée |
| `_x` | Dossier privé |

## 25.5 API de cache

| API | Rôle | Où |
|---|---|---|
| `"use cache"` | Met en cache | Fonctions, composants, fichiers |
| `cacheLife(profil)` | Durée (`stale`/`revalidate`/`expire`) | Dans un périmètre `"use cache"` |
| `cacheTag(tag)` | Étiquette | Dans un périmètre `"use cache"` |
| `revalidateTag(tag, profil)` | Invalide (SWR) | Actions, Route Handlers |
| `updateTag(tag)` | Invalide **immédiatement** (lecture de ses écritures) | **Server Actions** seulement |
| `refresh()` | Rafraîchit les données non mises en cache | **Server Actions** seulement |
| `revalidatePath(chemin)` | Invalide une route | Actions, Route Handlers |
| `React.cache(fn)` | Déduplication sur la durée d'une requête | Serveur |

## 25.6 Hooks et API (client)

| Hook | Rôle |
|---|---|
| `useRouter` | Navigation impérative |
| `usePathname` | Chemin courant |
| `useSearchParams` | Paramètres de requête (lecture) |
| `useParams` | Paramètres dynamiques |
| `useSelectedLayoutSegment(s)` | Segment(s) actif(s) |
| `useLinkStatus` | État de navigation d'un lien |
| `useActionState` | État d'une action |
| `useFormStatus` | État d'envoi du formulaire parent |
| `useOptimistic` | UI optimiste |
| `useTransition` | Transition non bloquante |
| `use` | Lire une promesse/un contexte |
| `useReportWebVitals` | Mesure des Web Vitals |

## 25.7 Options de `fetch` (modèle classique)

| Option | Effet |
|---|---|
| `cache: "force-cache"` | Met en cache |
| `cache: "no-store"` | Pas de cache |
| `next: { revalidate: n }` | Revalidation toutes les `n` s |
| `next: { tags: [...] }` | Étiquettes |
| `signal: AbortSignal.timeout(ms)` | Délai d'expiration |

## 25.8 Options de segment (modèle classique ; incompatibles avec `cacheComponents`)

`dynamic`, `dynamicParams`, `revalidate`, `fetchCache`, `runtime`, `preferredRegion`, `maxDuration`.

## 25.9 Commandes CLI

| Commande | Rôle |
|---|---|
| `next dev` | Dev avec Fast Refresh |
| `next build` | Build de production |
| `next start` | Serveur de production |
| `next typegen` | Génère les types de routes |
| `next info` | Diagnostic |
| `--webpack` | Utiliser Webpack au lieu de Turbopack |
| `-p`, `--port` | Port |

## 25.10 Choisir : Server Action, Route Handler ou Server Component ?

| Besoin | Choix |
|---|---|
| Afficher des données | Server Component |
| Mutation depuis votre UI | Server Action |
| API publique / webhook / mobile | Route Handler |
| Interactivité (état, événements) | Client Component |
| Intercepter avant routage | Proxy |

## 25.11 Glossaire (A–Z)

- **App Router** : routeur basé sur `app/`, avec layouts imbriqués, Server Components, streaming.
- **Cache Components** : modèle de cache explicite de Next.js 16 (`"use cache"`), fondé sur PPR.
- **Catch-all** : segment dynamique capturant plusieurs segments d'URL.
- **Client Component** : composant hydraté dans le navigateur (`"use client"`).
- **Code splitting** : découpage du JavaScript en morceaux chargés à la demande.
- **Colocation** : placer composants/tests/styles à côté de la route sans les exposer.
- **Core Web Vitals** : LCP, INP, CLS — métriques d'expérience utilisateur.
- **CSR** : rendu côté client.
- **DAL** (Data Access Layer) : couche centralisant l'accès aux données et l'autorisation.
- **Default (`default.tsx`)** : repli d'un slot de route parallèle.
- **Draft Mode** : mode d'aperçu de contenu non publié.
- **DTO** : objet de transfert de données, version minimale d'une entité.
- **Dynamic rendering** : rendu à chaque requête.
- **Edge runtime** : environnement d'exécution léger basé sur les API Web.
- **Fast Refresh** : rechargement à chaud conservant l'état React.
- **Hydratation** : activation d'un HTML pré-rendu en y attachant React.
- **Intercepting routes** : routes chargées dans le contexte courant (modale) avec URL partageable.
- **ISR** : régénération statique incrémentale.
- **JSON-LD** : données structurées pour moteurs de recherche.
- **Layout** : UI partagée persistante entre routes.
- **Matcher** : filtre des chemins sur lesquels le proxy s'exécute.
- **Middleware** : ancien nom du proxy (≤ Next.js 15).
- **Pages Router** : routeur historique basé sur `pages/`.
- **Parallel routes** : plusieurs pages rendues simultanément via des slots `@x`.
- **PPR** : pré-rendu partiel (coque statique + trous dynamiques).
- **Prefetching** : préchargement des routes liées.
- **Proxy** : interception des requêtes avant routage (`proxy.ts`).
- **RSC (React Server Components)** : composants exécutés uniquement côté serveur.
- **Request Memoization** : déduplication des requêtes identiques pendant un rendu.
- **Route Group** : dossier `(x)` qui organise sans changer l'URL.
- **Route Handler** : endpoint HTTP défini dans `route.ts`.
- **SEO** : optimisation pour les moteurs de recherche.
- **Server Action / Server Function** : fonction serveur appelable depuis le client.
- **SSG** : génération statique au build.
- **SSR** : rendu côté serveur à chaque requête.
- **Stale-while-revalidate** : servir une valeur périmée pendant sa régénération.
- **Standalone** : sortie de build minimale pour Docker.
- **Streaming** : envoi progressif du HTML/RSC.
- **Suspense** : mécanisme React d'attente avec UI de repli.
- **Tag (cache)** : étiquette servant à invalider des entrées de cache.
- **Template** : layout recréé à chaque navigation.
- **Turbopack** : bundler Rust, par défaut depuis Next.js 16.
- **TTFB** : délai avant le premier octet.
- **Typed Routes** : vérification statique des liens.

## 25.12 Parcours d'apprentissage suggéré

1. **Semaine 1** : chapitres 1–4 (bases, routing) → site statique multi-pages.
2. **Semaine 2** : chapitres 5–6 → blog avec données chargées côté serveur.
3. **Semaine 3** : chapitres 7–8 → cache, ISR, streaming, mesure de performance.
4. **Semaine 4** : chapitres 9–12 → formulaires, API, proxy, navigation fluide.
5. **Semaine 5** : chapitres 13–17 → design, SEO, authentification, i18n.
6. **Semaine 6** : chapitres 18–22 → configuration, tests, déploiement.
7. **Semaine 7** : chapitres 23–24 → migration, revue qualité, projet final.

### Projet fil rouge proposé : « Blog + espace membre »

- Pages : accueil, liste d'articles (pagination, recherche via `searchParams`), article (`generateStaticParams`, métadonnées dynamiques, OG image).
- Espace membre : inscription/connexion (session cookie), tableau de bord protégé (DAL + rôles).
- Contenu : CRUD d'articles via Server Actions avec validation Zod, `updateTag` après mutation.
- Commentaires : mise à jour optimiste (`useOptimistic`).
- API publique : Route Handler `/api/articles` + webhook de revalidation.
- Qualité : i18n FR/EN, tests Vitest + Playwright, en-têtes de sécurité, Docker, CI/CD.

## 25.13 Ressources

- Documentation officielle : https://nextjs.org/docs
- Tutoriel officiel « Learn Next.js » : https://nextjs.org/learn
- Blog et notes de version : https://nextjs.org/blog
- Guides de mise à niveau : https://nextjs.org/docs/app/guides/upgrading
- Dépôt GitHub : https://github.com/vercel/next.js
- Documentation React : https://react.dev

> Les API de Next.js évoluent. En cas de divergence entre ce cours et votre version, **la documentation officielle de votre version fait foi.**
