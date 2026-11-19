# CSS — Cours complet

*Cours magistral et module d'apprentissage exhaustif, fondé sur le plan « CSS — Guide complet » — CSS moderne (novembre 2026)*

## Avant de commencer : comment utiliser ce cours

Ce cours développe, chapitre par chapitre, l'intégralité du plan en **32 chapitres**, regroupés en cinq parties : **Fondamentaux** (1 à 10), **CSS avancé** (11 à 19), **Tests** (20 et 21), **Performance** (22 à 24) et **Essentiels** (25 à 32).

Chaque chapitre suit la même trame : *objectifs d'apprentissage → notions et définitions → exemples de code commentés → pièges fréquents → synthèse*.

**Conventions de lecture**

- **(à jour)** : pratique moderne qui remplace une ancienne. **(héritage)** : ancienne technique, encore fréquente dans les projets existants. **(ajout)** : notion absente des anciens guides.
- Le code est écrit en **CSS moderne** (imbrication native, couches de cascade, propriétés logiques). Les exemples utilisent des noms de classes en français et sont volontairement **autonomes** : chaque extrait peut être copié dans une feuille de style vide.
- Le cours enseigne le CSS **actuel** (Flexbox, Grid, requêtes de conteneur, `@layer`, couleurs OKLCH, `:has()`, transitions de vue) **et** explique l'ancien (`float`, *clearfix*, préfixes, `@import`) pour que vous sachiez lire du code existant.
- **Support des navigateurs.** Le projet **Baseline** résume la disponibilité d'une fonctionnalité : *newly available* (dans les dernières versions de tous les navigateurs majeurs) et *widely available* (disponible depuis au moins 30 mois). Ces indications sont données à titre indicatif : vérifiez toujours sur MDN ou caniuse.com avant d'utiliser une fonctionnalité sans solution de repli.

**Parcours conseillé** : lisez les chapitres 1 à 10 dans l'ordre (ils se construisent les uns sur les autres), puis choisissez librement dans les parties suivantes selon vos besoins.

---

## 1. Introduction à CSS

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez définir CSS et situer son rôle par rapport à HTML et JavaScript, décrire les étapes par lesquelles un navigateur transforme un document et une feuille de style en pixels, écrire et lier une première feuille de style, et comprendre pourquoi on ne parle plus de « CSS4 » mais de modules.

### 1.1 Qu'est-ce que CSS ?

**CSS** est l'acronyme de *Cascading Style Sheets*, en français « feuilles de style en cascade ». C'est un langage **déclaratif** : on ne décrit pas une suite d'opérations à exécuter, on décrit un **résultat souhaité** (« les titres sont violets, les paragraphes ont une interligne de 1,6 »), et c'est le navigateur qui détermine comment l'obtenir. CSS décrit la **présentation** d'un document structuré, le plus souvent HTML : couleurs, polices, espacements, mise en page, animations, adaptation à la taille et aux préférences de l'utilisateur.

CSS a été proposé au milieu des années 1990 pour répondre à un problème précis : les premières pages web mélangeaient contenu et mise en forme dans les mêmes balises, ce qui rendait les sites difficiles à maintenir. Les spécifications sont publiées par le **CSS Working Group du W3C**, qui rassemble des représentants des éditeurs de navigateurs et d'autres organisations.

#### Les trois langages du web

Une page web repose sur trois langages complémentaires, qu'il faut savoir distinguer :

| Langage | Rôle | Question à laquelle il répond |
| --- | --- | --- |
| **HTML** | Structure et contenu : titres, paragraphes, liens, images, formulaires | Qu'est-ce que c'est ? |
| **CSS** | Présentation : apparence et mise en page | À quoi cela ressemble-t-il ? |
| **JavaScript** | Comportement : interactions, logique, communication avec un serveur | Que se passe-t-il quand on agit ? |

Cette séparation des responsabilités est un principe de conception fondamental : on écrit un HTML **sémantique** qui reste compréhensible sans style, on lui applique du CSS, et on n'ajoute du JavaScript que pour ce que les deux autres ne savent pas faire. Beaucoup de comportements autrefois scriptés (menus, accordéons, thèmes, animations au défilement) sont aujourd'hui réalisables en CSS seul, comme nous le verrons dans la suite du cours.

#### Les avantages de CSS

- **Séparation du contenu et du design.** Un seul fichier CSS peut styliser tout un site de plusieurs milliers de pages.
- **Maintenance facilitée.** Pour changer la couleur d'un bouton sur tout le site, on modifie une seule déclaration.
- **Responsive.** Une même page s'adapte au téléphone, à la tablette, à l'ordinateur ou à l'impression, sans dupliquer le HTML.
- **Accessibilité et préférences utilisateur.** CSS permet de respecter le mode sombre, la réduction des animations, le contraste élevé, l'agrandissement du texte.
- **Performance.** Un fichier CSS est mis en cache par le navigateur et traité très efficacement ; il est réutilisé d'une page à l'autre.
- **Cohérence.** Des règles communes garantissent que tous les boutons, titres ou formulaires se ressemblent.

### 1.2 Les concepts fondateurs

Toute la suite du cours repose sur une dizaine de notions. Les repérer dès maintenant permet de savoir où chacune sera approfondie.

| Concept | Idée essentielle | Chapitre |
| --- | --- | --- |
| **Sélecteur** | Motif qui désigne les éléments auxquels une règle s'applique | 2 |
| **Déclaration** | Paire propriété et valeur : la mise en forme demandée | 2 |
| **Cascade** | Algorithme qui désigne la déclaration gagnante quand plusieurs règles se contredisent | 4 |
| **Spécificité** | Mesure de la précision d'un sélecteur, utilisée par la cascade | 4 |
| **Héritage** | Transmission automatique de certaines propriétés du parent aux enfants | 4 |
| **Valeurs et unités** | Couleurs, longueurs, fonctions de calcul | 5 |
| **Modèle de boîte** | Tout élément est un rectangle : contenu, padding, bordure, marge | 6 |
| **Flux normal** | Ordre par défaut dans lequel les boîtes se placent dans la page | 8 |
| **Contexte de mise en page** | Mode de disposition des enfants d'un élément : flux normal, Flexbox, Grid | 9 et 10 |
| **Variables (propriétés personnalisées)** | Valeurs nommées, réutilisables et modifiables à l'exécution | 12 |
| **Requêtes** | Conditions sur la fenêtre (média) ou sur un conteneur qui activent des règles | 14 |

Trois idées traversent tout le cours : CSS est **déclaratif** (on décrit un résultat), **tolérant** (une déclaration invalide est ignorée et le reste continue de s'appliquer) et **évolutif** (les nouveautés s'ajoutent sans casser l'existant, ce qui impose de prévoir des replis).

### 1.3 Architecture : comment le navigateur applique le CSS

Comprendre le pipeline de rendu évite beaucoup d'incompréhensions sur le comportement du CSS et sur les performances. Le schéma simplifié est le suivant :

```text
HTML --> DOM  --+
                +--> Arbre de rendu --> Mise en page --> Peinture --> Composition --> Écran
CSS  --> CSSOM -+
```

1. **Analyse du HTML : le DOM.** Le navigateur lit le HTML et construit le **DOM** (*Document Object Model*), un arbre dont chaque noeud représente un élément, un attribut ou un texte.
2. **Analyse du CSS : le CSSOM.** En parallèle, il lit toutes les feuilles de style (externes, internes, attributs `style`, feuilles du navigateur) et construit le **CSSOM** (*CSS Object Model*), l'arbre des règles.
3. **Calcul des styles.** Pour chaque élément, le navigateur applique la **cascade** (chapitre 4) afin de déterminer, pour chaque propriété, la valeur gagnante. Cette valeur passe par plusieurs états : la **valeur déclarée** (ce qui est écrit dans les règles), la **valeur calculée** (après résolution de l'héritage et des valeurs relatives comme `2em`), la **valeur utilisée** (après la mise en page, par exemple une largeur en pixels pour `width: 50%`) et la **valeur réelle** (après arrondis imposés par l'appareil).
4. **Arbre de rendu.** DOM et styles calculés sont combinés. Les éléments non affichés (`display: none`) n'y figurent pas.
5. **Mise en page (*layout*, ou *reflow*).** Le navigateur calcule la taille et la position exacte de chaque boîte.
6. **Peinture (*paint*).** Il dessine les pixels : textes, couleurs, bordures, ombres, images.
7. **Composition.** Les différentes couches sont assemblées, éventuellement par le processeur graphique, pour produire l'image finale.

Deux conséquences pratiques en découlent. D'abord, le CSS est une ressource **bloquante pour le rendu** : le navigateur attend d'avoir reçu et analysé le CSS avant d'afficher la page, afin d'éviter l'affichage temporaire d'un contenu non stylé (le « flash de contenu sans style »). Il est donc important de garder le CSS léger (chapitre 22). Ensuite, toute modification d'une propriété ne coûte pas le même prix : modifier une propriété qui change la géométrie (`width`, `margin`) déclenche à nouveau la mise en page, la peinture et la composition ; modifier une couleur ne déclenche que la peinture et la composition ; modifier `transform` ou `opacity` peut se limiter à la composition. Nous réutiliserons cette idée au chapitre 13.

### 1.4 Un premier exemple

Voici une page HTML minimale liée à une feuille de style.

```html
<!DOCTYPE html>
<html lang='fr'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <title>Ma première page</title>
    <link rel='stylesheet' href='style.css'>
</head>
<body>
    <h1>Bonjour CSS !</h1>
    <p class='intro'>Ceci est un paragraphe stylisé.</p>
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

**Analyse du HTML.** La déclaration `<!DOCTYPE html>` active le mode de rendu standard du navigateur ; sans elle, le navigateur bascule en « mode quirks » et interprète certaines règles selon d'anciens comportements. L'attribut `lang='fr'` indique la langue du document, utile pour les lecteurs d'écran, la césure et la correction orthographique. La balise `meta charset` déclare l'encodage des caractères. La balise `meta viewport` est indispensable au design responsive sur mobile : sans elle, les téléphones affichent la page comme sur un grand écran réduit (chapitre 14). Enfin `<link rel='stylesheet' href='style.css'>` relie la feuille de style.

**Analyse du CSS.** Le sélecteur `body` cible l'élément `<body>`. `font-family: system-ui, sans-serif` demande la police système de l'utilisateur, avec un repli générique. `line-height: 1.6` fixe l'interligne à 1,6 fois la taille de police (une valeur sans unité est recommandée, car elle se recalcule pour chaque élément). `margin: 0` supprime la marge par défaut du navigateur, et `padding: 2rem` ajoute un espacement intérieur de deux fois la taille de police racine. Le titre reçoit une couleur nommée, `rebeccapurple`. La classe `.intro` agrandit le texte et lui donne un gris foncé. Remarquez que le `<p>` hérite de la police et de l'interligne définies sur `body` : c'est l'**héritage** (chapitre 4).

### 1.5 Histoire : les « niveaux » de CSS

Historiquement, CSS était publié en versions numérotées : CSS1 (1996), CSS2 (1998), puis CSS 2.1 (finalisé en 2011), qui reste la base de référence. À partir de CSS3, la spécification a été **découpée en modules indépendants**, chacun avec son propre numéro de niveau et son propre rythme : Sélecteurs niveau 4, Couleurs niveau 5, Grid niveau 2, Imbrication, Conteneurs, Valeurs et unités, etc. Il n'y a donc pas de « CSS4 » : on parle simplement de **CSS moderne**, ici « CSS 2026 », pour désigner l'ensemble des modules disponibles dans les navigateurs actuels.

Chaque module passe par des étapes de maturité (brouillon de travail, candidate à la recommandation, recommandation), mais ce qui importe au quotidien est le **support effectif dans les navigateurs**, d'où l'intérêt de Baseline, de MDN et de caniuse.com. Un bon réflexe : avant d'adopter une nouveauté, consulter son statut de support, prévoir un **repli** pour les navigateurs qui ne la connaissent pas, et utiliser `@supports` lorsque c'est utile (chapitre 25).

### 1.6 Pourquoi apprendre CSS ? Forces et limites

CSS est le seul langage de présentation natif du web : tous les frameworks, toutes les bibliothèques de composants et tous les préprocesseurs aboutissent, au bout du compte, à du CSS exécuté par le navigateur. Le maîtriser est donc un investissement durable, quels que soient les outils utilisés par-dessus.

**Forces**

- **Standard universel et durable** : un même CSS fonctionne dans tous les navigateurs, et une feuille écrite il y a vingt ans s'affiche encore.
- **Déclaratif et tolérant** : on décrit le résultat ; une erreur n'interrompt pas la page.
- **Performant** : le navigateur optimise le rendu, et certaines animations s'exécutent sur le processeur graphique.
- **Adaptatif** : requêtes média et de conteneur, unités fluides, préférences de l'utilisateur (thème, mouvement, contraste).
- **De plus en plus puissant** : Grid, variables, imbrication, couches de cascade, `:has()` et animations liées au défilement réduisent le besoin de JavaScript et de préprocesseurs.
- **Accessible par construction** : bien utilisé, il respecte le zoom, le thème et les préférences du système.

**Limites**

- **Portée globale** : toute règle peut affecter toute la page ; sur un grand projet, cela provoque des conflits de noms et une escalade de spécificité (chapitres 4 et 19).
- **Cascade parfois déroutante** : comprendre pourquoi un style l'emporte demande de la méthode (chapitre 4) et des outils (chapitre 27).
- **Support inégal des nouveautés** : une fonctionnalité récente n'est pas disponible partout (chapitres 15 et 25).
- **Peu de logique** : pas de boucles ni de fonctions universelles ; `calc()` et les fonctions mathématiques comblent une partie du besoin, et les préprocesseurs restent utiles (chapitre 18).
- **Héritage historique** : des mécanismes anciens (`float`, `clearfix`, préfixes) subsistent dans le code existant et doivent être reconnus.

#### CSS natif ou outil par-dessus ?

| Critère | CSS natif | Sass (préprocesseur) | Utilitaires (Tailwind) | CSS-in-JS |
| --- | --- | --- | --- | --- |
| Courbe d'apprentissage | Faible à moyenne | Faible une fois CSS connu | Moyenne (vocabulaire de classes) | Moyenne |
| Étape de build | Facultative | Obligatoire | Obligatoire | Souvent obligatoire |
| Variables dynamiques | Oui (propriétés personnalisées) | Non (résolues à la compilation) | Via variables CSS | Oui (JavaScript) |
| Portée locale | `@scope`, `@layer`, conventions | Conventions (BEM) | Naturelle (classes atomiques) | Native (noms générés) |
| Poids livré | Faible | Faible | Faible (classes utilisées) | Plus élevé (code d'exécution) |
| Idéal pour | Sites, systèmes de design | Bases existantes, logique complexe | Prototypage rapide, équipes | Applications à composants |

Quel que soit l'outil, c'est du CSS natif que le navigateur exécute : apprendre les fondamentaux d'abord permet de déboguer et de changer d'outil sans repartir de zéro.

### 1.7 Versions, modules et suivi des évolutions *(à jour)*

CSS n'a plus de numéro de version global (voir 1.5) : chaque module évolue à son rythme. Les navigateurs sont, eux, **évolutifs** (*evergreen*) : ils se mettent à jour automatiquement, à raison d'une nouvelle version environ toutes les quatre semaines pour Chrome et Edge, et à un rythme comparable pour Firefox et Safari. De nouvelles fonctionnalités CSS arrivent donc en continu.

| Statut d'un module (W3C) | Signification | Fiabilité |
| --- | --- | --- |
| Brouillon (*Editor's Draft*, *Working Draft*) | Proposition en discussion | Peut changer profondément |
| Candidate à la recommandation | Spécification stable, en attente d'implémentations | Fiable, détails mineurs possibles |
| Recommandation | Standard finalisé | Stable |

Le statut W3C n'indique **pas** le support réel : un module encore en brouillon peut être implémenté partout, et un module stable peut manquer dans un navigateur. Pour décider d'utiliser une fonctionnalité, on consulte :

- **MDN** et **caniuse.com** : tableaux de compatibilité par navigateur et par version ;
- **Baseline** (web.dev/baseline) : synthèse *newly available*, *widely available* ou limitée ;
- les **notes de version** des navigateurs et le programme **Interop**, par lequel les éditeurs s'accordent chaque année sur des priorités de compatibilité.

Règle pratique : une fonctionnalité *widely available* s'utilise sans précaution ; une fonctionnalité *newly available* s'utilise avec un repli si l'audience est ancienne ; une fonctionnalité à disponibilité limitée s'utilise en **amélioration progressive**, derrière `@supports` (chapitre 25).

### 1.8 Prérequis et environnement de travail

**Prérequis.** Des notions de base en HTML suffisent : structure d'un document, éléments courants, attributs `class` et `id`. Aucune connaissance en programmation n'est nécessaire, sauf pour le chapitre 26 (CSS et JavaScript).

**Environnement minimal.** Un navigateur moderne récent (Chrome, Edge, Firefox ou Safari) avec ses outils de développement, et un éditeur de texte (Visual Studio Code est recommandé, avec l'extension *Live Server* pour rafraîchir la page automatiquement). Aucune installation n'est requise pour débuter : un fichier HTML et un fichier CSS suffisent. Node.js ne devient utile que pour les outils de build (chapitres 18 et 24).

**Structure de départ.**

```text
mon-site/
|-- index.html
|-- css/
|   +-- style.css
+-- images/
```

1. Créez le dossier et les deux fichiers, puis reliez la feuille de style avec `<link rel='stylesheet' href='css/style.css'>` (voir 1.4).
2. Ouvrez la page dans le navigateur, puis les outils de développement (touche F12).
3. Dans l'onglet des éléments, sélectionnez un élément et vérifiez que les règles de votre feuille de style apparaissent dans le panneau des styles : c'est le réflexe de contrôle que vous utiliserez tout au long du cours.

### 1.9 Glossaire du chapitre

| Terme | Définition |
| --- | --- |
| **CSS** | *Cascading Style Sheets* : langage déclaratif de présentation |
| **DOM** | Arbre des éléments du document, construit à partir du HTML |
| **CSSOM** | Arbre des règles de style, construit à partir des feuilles de style |
| **Règle** | Sélecteur suivi d'un bloc de déclarations |
| **Sélecteur** | Motif qui désigne les éléments concernés par une règle |
| **Déclaration** | Paire propriété et valeur, terminée par un point-virgule |
| **Propriété** | Caractéristique à modifier (`color`, `margin`, `display`) |
| **Cascade** | Algorithme qui choisit la déclaration gagnante parmi plusieurs candidates |
| **Spécificité** | Mesure de la précision d'un sélecteur, utilisée pour départager les règles |
| **Héritage** | Transmission d'une valeur du parent à ses enfants pour certaines propriétés |
| **Valeur calculée** | Valeur d'une propriété après résolution de l'héritage et des valeurs relatives |
| **Boîte** | Rectangle (contenu, padding, bordure, marge) que le navigateur dessine pour chaque élément |
| **Flux normal** | Mode de placement par défaut des boîtes, de haut en bas et de gauche à droite |
| **Reflow (mise en page)** | Recalcul de la taille et de la position des boîtes |
| **Repaint (peinture)** | Redessin des pixels sans recalcul de la géométrie |
| **Module** | Partie indépendante de la spécification CSS, avec son propre niveau |
| **Baseline** | Indicateur de disponibilité d'une fonctionnalité dans les navigateurs majeurs |
| **Repli** | Déclaration ou comportement de secours pour un navigateur qui ignore une nouveauté |
| **Viewport** | Zone visible de la page dans la fenêtre du navigateur |

### Synthèse du chapitre 1

- CSS est un langage déclaratif de présentation ; HTML structure, JavaScript anime.
- Le navigateur construit DOM et CSSOM, calcule les styles par la cascade, puis met en page, peint et compose.
- Le CSS bloque le rendu : on le garde léger.
- Les propriétés ne coûtent pas toutes le même prix : géométrie, peinture, composition.
- CSS n'est plus versionné globalement mais organisé en modules ; on vérifie toujours le support.

---

## 2. Syntaxe et sélecteurs

**Objectifs d'apprentissage.** Vous saurez lire et écrire une règle CSS complète, utiliser les commentaires, choisir le sélecteur adapté pour cibler précisément des éléments, et maîtriser les combinateurs, les sélecteurs d'attribut, les pseudo-classes, les pseudo-éléments et l'imbrication native.

### 2.1 Anatomie d'une règle

Une feuille de style est une suite de **règles**. La forme générale d'une règle ordinaire est :

```css
selecteur {
    propriete: valeur;
    autre-propriete: valeur;
}
```

Exemple concret :

```css
h1 {
    color: blue;      /* propriété : valeur ; */
    font-size: 2rem;
}
```

| Élément | Définition |
| --- | --- |
| **Sélecteur** | Désigne les éléments HTML auxquels la règle s'applique |
| **Bloc de déclarations** | L'ensemble des déclarations placées entre accolades |
| **Déclaration** | Une paire `propriété: valeur;` |
| **Propriété** | La caractéristique à modifier (`color`, `margin`, `display`) |
| **Valeur** | Le réglage appliqué à la propriété (`blue`, `2rem`, `flex`) |
| **Règle @** (*at-rule*) | Instruction spéciale introduite par `@` : `@media`, `@font-face`, `@layer`, `@keyframes`, `@supports`, `@container`, etc. |

**Points de syntaxe à connaître.**

- Les **espaces et sauts de ligne** sont libres : on indente par convention pour la lisibilité.
- Le **point-virgule** termine chaque déclaration ; il est facultatif après la dernière, mais on le met toujours pour éviter les oublis lors d'un ajout ultérieur.
- Les **noms de propriétés** et les **mots-clés de valeurs** sont insensibles à la casse (`COLOR: Blue` fonctionne), mais la convention est le minuscule avec tirets (`font-size`). En revanche, les **noms de classes, d'identifiants** et les valeurs d'attributs sont **sensibles à la casse** dans le HTML : `.Carte` et `.carte` sont différents.
- Une **déclaration invalide** (propriété inconnue, valeur incorrecte) est **ignorée** sans bloquer le reste de la feuille. Cette tolérance aux erreurs est ce qui permet l'amélioration progressive : un navigateur qui ne connaît pas une nouveauté saute la déclaration et applique la précédente.

```css
.bloc {
    width: 50%;
    width: calc(100% - 2rem);   /* ignorée par un navigateur qui ne comprendrait pas calc() */
}
```

- Une **propriété raccourcie** (*shorthand*) regroupe plusieurs propriétés détaillées (*longhands*) : `margin` regroupe `margin-top`, `margin-right`, `margin-bottom`, `margin-left`. Attention : un raccourci **réinitialise** les propriétés non précisées à leur valeur initiale.

### 2.2 Commentaires

```css
/* Commentaire sur une ligne */

/*
   Commentaire
   sur plusieurs lignes
*/
```

CSS pur ne connaît **que** la syntaxe `/* … */`. Le commentaire `//` n'existe pas en CSS standard ; il est disponible dans les préprocesseurs comme Sass/SCSS (chapitre 18), qui le suppriment avant de produire le CSS final. Les commentaires servent à documenter l'intention (le « pourquoi ») et à désactiver temporairement du code pendant le débogage.

### 2.3 Sélecteurs de base

Un **sélecteur** est un motif qui décrit quels éléments du document sont concernés. Les quatre sélecteurs de base sont :

| Sélecteur | Syntaxe | Cible |
| --- | --- | --- |
| **Universel** | `*` | Tous les éléments |
| **Type** (ou balise) | `p`, `h1`, `a` | Tous les éléments de ce type |
| **Classe** | `.carte` | Les éléments portant `class='carte'` |
| **Identifiant** | `#entete` | L'élément portant `id='entete'` (unique dans la page) |

```css
* { box-sizing: border-box; }
p { margin-block: 1em; }
.alerte { color: crimson; }
#menu-principal { display: flex; }
button.primaire { background: royalblue; }     /* seulement <button class='primaire'> */
.carte.mise-en-avant { border-color: gold; }   /* élément ayant les DEUX classes */
```

Plusieurs sélecteurs simples **collés sans espace** forment un **sélecteur composé** : `button.primaire` cible un bouton ayant la classe `primaire`. Un élément peut porter **plusieurs classes** séparées par des espaces (`class='carte mise-en-avant'`), ce qui permet de composer des variantes ; en revanche un identifiant doit être **unique** dans le document.

**Pourquoi préférer les classes aux identifiants pour le style ?** Les classes sont réutilisables sur de nombreux éléments, et leur spécificité est plus basse (chapitre 4), donc plus faciles à surcharger. Les identifiants servent plutôt d'ancres de navigation (`#section-2`), de cibles pour les libellés de formulaires ou pour JavaScript.

### 2.4 Regrouper et combiner

#### Liste de sélecteurs

La virgule permet d'appliquer les mêmes déclarations à plusieurs sélecteurs :

```css
h1, h2, h3 { font-family: Georgia, serif; }
```

C'est strictement équivalent à écrire trois règles séparées. Attention : dans une liste classique, **un seul sélecteur invalide invalide toute la règle**. Les pseudo-classes `:is()` et `:where()` (section 2.6) sont, elles, « tolérantes » : un sélecteur inconnu à l'intérieur est simplement ignoré.

#### Combinateurs

Un **combinateur** exprime une relation de position entre deux éléments dans l'arbre HTML.

| Combinateur | Syntaxe | Cible |
| --- | --- | --- |
| **Descendant** (un espace) | `article p` | Tout `<p>` situé **dans** un `<article>`, à n'importe quelle profondeur |
| **Enfant direct** | `ul > li` | Les `<li>` qui sont **enfants directs** d'un `<ul>` |
| **Frère adjacent** | `h2 + p` | Le `<p>` placé **immédiatement après** un `<h2>`, au même niveau |
| **Frères suivants** | `h2 ~ p` | **Tous** les `<p>` frères qui suivent un `<h2>` |

```css
nav ul { list-style: none; }
.menu > li { display: inline-block; }
h2 + p { font-weight: bold; }
h2 ~ p { color: gray; }
```

Le combinateur descendant est le plus large : `nav ul` atteint aussi les listes imbriquées dans un sous-menu. Le combinateur enfant `>` est plus précis. Les combinateurs de frères ne regardent que **vers l'avant** dans le document : on ne peut pas sélectionner un frère précédent avec eux (la pseudo-classe `:has()` répond à ce besoin, voir 2.6).

### 2.5 Sélecteurs d'attribut

Ils ciblent des éléments d'après la présence ou la valeur d'un attribut HTML, ce qui évite d'ajouter des classes.

```css
a[target] { }                            /* possède l'attribut */
a[target='_blank'] { }                   /* valeur exacte */
a[href^='https'] { }                     /* commence par */
a[href$='.pdf'] { }                      /* se termine par */
a[href*='exemple'] { }                   /* contient la sous-chaîne */
[class~='alerte'] { }                    /* contient le mot (séparé par des espaces) */
[lang|='fr'] { }                         /* « fr » ou « fr-… » (fr-FR, fr-CA) */
input[type='email' i] { }                /* insensible à la casse (drapeau i) */
```

Exemples d'usage : marquer les liens externes, styliser les liens vers des fichiers PDF, cibler un type d'`<input>`. Par défaut la comparaison des valeurs est sensible à la casse pour la plupart des attributs ; le drapeau `i` la rend insensible, et `s` la force sensible.

### 2.6 Pseudo-classes

Une **pseudo-classe** cible un **état** ou une **position** d'un élément, qui ne peut pas être exprimé par une simple balise ou classe. Elle s'écrit avec **un seul deux-points** : `a:hover`. Le navigateur l'applique et la retire dynamiquement selon ce qui se passe dans la page.

| Catégorie | Pseudo-classes |
| --- | --- |
| **Interaction** | `:hover`, `:active`, `:focus`, `:focus-visible`, `:focus-within`, `:target` |
| **Liens** | `:link`, `:visited`, `:any-link` |
| **Formulaires** | `:checked`, `:disabled`, `:enabled`, `:required`, `:optional`, `:placeholder-shown`, `:read-only`, `:valid`, `:invalid`, `:user-valid`, `:user-invalid`, `:in-range`, `:out-of-range`, `:indeterminate` |
| **Position** | `:first-child`, `:last-child`, `:only-child`, `:nth-child()`, `:nth-last-child()`, `:first-of-type`, `:last-of-type`, `:nth-of-type()` |
| **Structure** | `:root`, `:empty`, `:defined` |
| **Fonctionnelles** | `:not()`, `:is()`, `:where()`, `:has()` |
| **Autres** | `:dir()`, `:lang()`, `:modal`, `:popover-open`, `:fullscreen` |

#### Pseudo-classes d'interaction

- `:hover` : le pointeur survole l'élément. Elle n'existe pas sur un écran tactile pur : ne cachez jamais une information essentielle derrière un survol.
- `:active` : l'élément est en cours d'activation (bouton de la souris enfoncé).
- `:focus` : l'élément possède le focus clavier ou programmatique.
- `:focus-visible` : le focus est affiché **seulement quand le navigateur juge que c'est utile**, typiquement lors d'une navigation au clavier. C'est le sélecteur à utiliser pour les anneaux de focus, car il évite de dessiner un contour après un simple clic de souris tout en conservant l'accessibilité clavier.
- `:focus-within` : un élément **ou l'un de ses descendants** a le focus ; pratique pour styliser un groupe de champs ou un menu.
- `:target` : l'élément dont l'identifiant correspond au fragment de l'URL (`page.html#section-2`).

#### Pseudo-classes de liens

`:link` cible les liens non visités, `:visited` les liens déjà visités, `:any-link` les deux. Pour protéger la vie privée (empêcher un site de deviner l'historique de l'utilisateur), `:visited` ne peut modifier qu'un nombre limité de propriétés, essentiellement des couleurs. L'ordre classique « LoVe HAte » (`:link`, `:visited`, `:hover`, `:active`) reste utile quand les règles ont même spécificité.

#### Pseudo-classes de formulaires

Elles reflètent l'état d'un champ : `:checked` (case cochée, bouton radio sélectionné, option choisie), `:disabled` et `:enabled`, `:required` et `:optional`, `:placeholder-shown` (le texte d'indication est affiché, donc le champ est vide), `:read-only`, `:in-range` et `:out-of-range` (valeur dans ou hors des bornes `min` et `max`), `:indeterminate` (case à état indéterminé).

La validation mérite une explication : `:valid` et `:invalid` s'appliquent **dès le chargement de la page**, ce qui affiche des erreurs avant même que l'utilisateur ait commencé à saisir. Les pseudo-classes **`:user-valid`** et **`:user-invalid`** ne s'appliquent qu'**après une interaction de l'utilisateur** avec le champ, ce qui est le comportement idéal pour afficher un retour d'erreur.

#### Pseudo-classes de position

Elles sélectionnent un élément d'après son rang parmi ses frères. `:first-child` et `:last-child` visent le premier et le dernier enfant de leur parent ; `:only-child` vise un enfant unique. Les variantes `-of-type` comptent seulement les frères du **même type de balise**.

`:nth-child()` accepte une formule de la forme **an + b**, où `n` prend les valeurs 0, 1, 2, 3… :

| Expression | Sélectionne |
| --- | --- |
| `:nth-child(3)` | Le troisième enfant |
| `:nth-child(odd)` ou `2n + 1` | Les enfants impairs (1, 3, 5…) |
| `:nth-child(even)` ou `2n` | Les enfants pairs (2, 4, 6…) |
| `:nth-child(3n + 1)` | 1, 4, 7, 10… |
| `:nth-child(-n + 3)` | Les trois premiers |
| `:nth-last-child(-n + 2)` | Les deux derniers |
| `:nth-child(n + 4)` | Tous à partir du quatrième |
| `:nth-child(2n of .actif)` | Un élément sur deux parmi ceux qui ont la classe `actif` |

```css
a:hover { color: red; }
button:focus-visible { outline: 3px solid royalblue; outline-offset: 2px; }   /* focus clavier uniquement */
li:nth-child(odd) { background: #eee; }          /* lignes alternées */
li:nth-child(3n + 1) { }                         /* 1, 4, 7… */
li:nth-child(-n + 3) { }                         /* les 3 premiers */
li:last-child { border-bottom: 0; }
input:checked + label { font-weight: 700; }      /* étiquette suivant une case cochée */
input:user-invalid { border-color: crimson; }    /* invalide ET déjà modifié */
```

#### Pseudo-classes structurelles et autres

`:root` cible l'élément racine du document (en HTML, `<html>`), avec une spécificité de classe : c'est l'endroit habituel pour déclarer des variables globales (chapitre 12). `:empty` cible un élément sans enfant (ni texte). `:defined` cible les éléments connus, utile avec les composants web. `:dir()` et `:lang()` dépendent de la direction et de la langue du texte. `:modal`, `:popover-open` et `:fullscreen` correspondent aux états d'un `<dialog>` ouvert en modal, d'un popover ouvert et d'un élément en plein écran.

#### Les pseudo-classes fonctionnelles modernes

Ces quatre pseudo-classes prennent un **argument** entre parenthèses et changent profondément la façon d'écrire des sélecteurs.

**`:is()`** regroupe une liste de sélecteurs **sans répéter** le reste du sélecteur. Sa spécificité est celle de son argument le plus spécifique. Elle est « tolérante » : un sélecteur invalide dans la liste est ignoré sans invalider tout le reste.

```css
:is(h1, h2, h3):hover { color: tomato; }
:is(article, section) :is(h2, h3) { margin-block: 1em; }   /* remplace 4 sélecteurs */
```

**`:where()`** fonctionne comme `:is()` mais avec une **spécificité toujours nulle**. Elle est idéale pour les styles de base (réinitialisations, thèmes) qu'on veut pouvoir surcharger très facilement.

```css
:where(ul, ol) { padding-inline-start: 1.5rem; }
```

**`:not()`** exclut des éléments et accepte une liste.

```css
a:not([class]) { text-decoration: underline; }
li:not(:last-child) { margin-bottom: .5rem; }
```

**`:has()`**, souvent appelée le « sélecteur parent », sélectionne un élément **qui contient** ou **qui est suivi de** ce que décrit l'argument. C'est l'une des nouveautés les plus importantes de CSS : elle permet de styliser un élément en fonction de son contenu ou de l'état de ses descendants, ce qui nécessitait auparavant du JavaScript.

```css
.carte:has(img) { display: grid; }                          /* carte contenant une image */
label:has(input:checked) { background: #e8f0ff; }           /* sélectionne le <label> parent */
form:has(:user-invalid) .envoyer { opacity: .5; }           /* bouton atténu si un champ est invalide */
h2:has(+ p) { margin-bottom: .25em; }                       /* titre suivi d'un paragraphe */
```

`:has()` est disponible dans tous les navigateurs modernes depuis fin 2023 (Baseline *widely available*). Pour la performance, on évite de l'appliquer à des éléments très généraux comme `body:has(...)` avec des arguments très larges lorsque ce n'est pas nécessaire.

### 2.7 Pseudo-éléments

Un **pseudo-élément** cible non pas un état mais une **partie** d'un élément, ou un élément généré par CSS. Il s'écrit avec **deux deux-points** (`::before`). La distinction avec les pseudo-classes est importante : `:hover` sélectionne un élément dans un certain état, `::first-line` sélectionne une portion de cet élément.

| Pseudo-élément | Cible |
| --- | --- |
| `::before`, `::after` | Contenu **généré**, inséré avant ou après le contenu (nécessite `content`) |
| `::first-line`, `::first-letter` | Première ligne, première lettre |
| `::selection` | Texte sélectionné par l'utilisateur |
| `::placeholder` | Texte d'indication d'un champ |
| `::marker` | Puce ou numéro d'un élément de liste |
| `::backdrop` | Arrière-plan d'un `<dialog>` modal, d'un élément plein écran ou d'un popover |
| `::file-selector-button` | Bouton d'un `<input type='file'>` |
| `::cue`, `::part()`, `::slotted()` | Sous-titres, parties de composants web (Shadow DOM) |
| `::details-content` | Contenu dépliable d'un `<details>` |
| `::view-transition-*` | Transitions de vue (chapitre 13) |

```css
p::first-letter { font-size: 2em; float: left; }              /* lettrine */
a[href^='http']::after { content: ' ↗'; }                    /* icône de lien externe */
.note::before { content: 'Note : '; font-weight: bold; }
::selection { background: gold; color: black; }
input::placeholder { color: #999; }
li::marker { color: tomato; }
dialog::backdrop { background: rgb(0 0 0 / .5); }
```

**Le contenu généré avec `::before` et `::after`.** Ces deux pseudo-éléments créent une boîte enfant, placée respectivement avant ou après le contenu réel de l'élément. Ils **n'apparaissent que si la propriété `content` est définie**, même à une chaîne vide (`content: ''`), ce qui est fréquent pour dessiner des formes décoratives. Leur contenu **n'existe pas dans le DOM** : on ne peut ni le sélectionner à la souris, ni le modifier avec JavaScript, et son annonce par les lecteurs d'écran varie. Il faut donc le réserver à la **décoration**, jamais à une information essentielle.

**Limites de `::first-line` et `::first-letter`.** Seul un sous-ensemble de propriétés (typographie, couleur, arrière-plan, et pour la lettrine quelques propriétés de boîte et de flottement) est autorisé ; la partie concernée est déterminée dynamiquement selon la mise en page.

### 2.8 Imbrication native *(à jour)*

Historiquement, imbriquer des règles nécessitait un préprocesseur (Sass, Less). Le CSS accepte désormais l'**imbrication native** dans tous les navigateurs modernes depuis 2023, ce qui réduit les répétitions de sélecteurs et regroupe visuellement les styles d'un composant.

```css
.carte {
    padding: 1rem;
    border: 1px solid #ddd;

    h2 { font-size: 1.25rem; }                            /* .carte h2 */
    &:hover { box-shadow: 0 2px 8px rgb(0 0 0 / .15); }   /* .carte:hover */
    &.active { border-color: royalblue; }                 /* .carte.active */
    .titre & { color: red; }                              /* .titre .carte */

    @media (min-width: 48rem) {                           /* règle @ imbriquée */
        padding: 2rem;
    }
}
```

**Le symbole `&`** représente le sélecteur parent. Sans lui, un sélecteur imbriqué est traité comme un descendant (`h2` devient `.carte h2`). Avec lui, on peut coller une pseudo-classe ou une classe au parent (`&:hover`, `&.active`) ou placer le parent **après** un contexte (`.titre &`). Les **règles @** (`@media`, `@supports`, `@container`, `@layer`) peuvent être imbriquées directement : les déclarations qu'elles contiennent s'appliquent alors au sélecteur parent.

Deux points de vigilance. D'abord, la spécificité d'un sélecteur imbriqué est celle du sélecteur complet résultant, avec la spécificité du parent calculée comme si on avait écrit `:is(parent)`. Ensuite, imbriquer trop profond reproduit les défauts de sélecteurs longs : on garde l'imbrication à **deux ou trois niveaux** au maximum. La concaténation de suffixes façon Sass (`&-titre`) n'est pas valide en CSS natif : on écrit le sélecteur complet.

### 2.9 Bonnes pratiques

- Utilisez des sélecteurs **simples et peu profonds** (trois niveaux au plus) : ils sont plus lisibles, plus rapides à évaluer et plus faciles à surcharger.
- Évitez de styliser avec des **identifiants** et avec `!important`, qui compliquent la maintenance (chapitre 4).
- Préférez des **classes sémantiques** (`.carte-produit`) à des classes présentatives (`.rouge-gras`) : le nom décrit le rôle, pas l'apparence, donc il survit à un changement de design.
- Ne dépendez pas de la structure HTML précise (`div > div > div > span`) : une modification du balisage casserait le style.
- Utilisez `:where()` pour les styles de base et `:is()` pour factoriser.

### Synthèse du chapitre 2

- Une règle = sélecteur + bloc de déclarations ; une déclaration invalide est ignorée.
- Quatre sélecteurs de base, quatre combinateurs, sept formes de sélecteurs d'attribut.
- Pseudo-classe (`:`) pour un état ou une position ; pseudo-élément (`::`) pour une partie ou un contenu généré.
- `:is()`, `:where()`, `:not()` et `:has()` simplifient radicalement les sélecteurs.
- L'imbrication native avec `&` remplace une grande partie de l'intérêt de Sass.

---

## 3. Ajouter du CSS à une page

**Objectifs d'apprentissage.** Vous saurez relier du CSS à un document de trois manières, choisir la méthode adaptée à chaque situation, comprendre le rôle de l'ordre des règles, et charger vos feuilles de style de façon efficace.

### 3.1 Les trois méthodes

| Méthode | Où | Quand l'utiliser |
| --- | --- | --- |
| **Externe** | Fichier `.css` lié par `<link>` | Presque toujours : mise en cache, réutilisation |
| **Interne** | Balise `<style>` dans le `<head>` | Page unique, CSS critique intégré, démonstrations |
| **En ligne** (*inline*) | Attribut `style` sur un élément | Valeurs dynamiques calculées par JavaScript, e-mails HTML ; à éviter sinon |

```html
<!-- 1. Externe -->
<link rel='stylesheet' href='css/style.css'>
<link rel='stylesheet' href='print.css' media='print'>                 <!-- seulement à l'impression -->
<link rel='stylesheet' href='grand-ecran.css' media='(min-width: 64rem)'>

<!-- 2. Interne -->
<style>
    body { font-family: system-ui, sans-serif; }
</style>

<!-- 3. En ligne -->
<p style='color: blue; font-weight: bold;'>Paragraphe bleu</p>
<div style='--progression: 70%;'>…</div>     <!-- injecter une variable CSS -->
```

**La feuille externe** est la méthode de référence. Le navigateur la télécharge une fois, la met en cache et la réutilise pour toutes les pages du site. L'attribut `media` permet de ne l'appliquer que dans certaines conditions (impression, écran large), le navigateur pouvant alors la charger avec une priorité moindre si elle ne s'applique pas.

**La feuille interne** convient à une page unique, à une démo, ou au **CSS critique** : le minimum de styles nécessaires à l'affichage de la partie visible, intégré dans le HTML pour éviter une requête supplémentaire.

**Le style en ligne** a la priorité la plus élevée (hors `!important`), ce qui le rend difficile à surcharger. Il ne peut pas exprimer les pseudo-classes, les pseudo-éléments ni les requêtes média. Son usage légitime principal est de transmettre une valeur dynamique à une **variable CSS** (`style='--progression: 70%'`), le reste du style restant dans la feuille.

#### Comparaison

|  | Externe | Interne | En ligne |
| --- | --- | --- | --- |
| Réutilisable entre pages | Oui | Non | Non |
| Mis en cache | Oui | Non | Non |
| Priorité (spécificité) | Normale | Normale | Très haute |
| Maintenance | Facile | Moyenne | Difficile |
| Compatible avec une CSP stricte | Oui | Nécessite un `nonce` | Nécessite `'unsafe-inline'` (déconseillé) |

Une **CSP** (*Content Security Policy*) est une politique de sécurité qui limite les ressources qu'une page peut charger ; une CSP stricte interdit par défaut le CSS en ligne, ce qui est un argument de plus pour les feuilles externes.

### 3.2 L'ordre compte

Lorsque deux règles ont **la même spécificité**, **la dernière déclarée l'emporte**. L'ordre des balises `<link>` et `<style>` dans le `<head>`, ainsi que l'ordre des règles dans un fichier, influent donc directement sur le résultat. On charge généralement les styles généraux (réinitialisation, base) avant les styles de composants, puis les utilitaires en dernier. Les **couches de cascade** (`@layer`, chapitre 4) rendent cet ordre explicite et indépendant de l'ordre des fichiers.

### 3.3 `@import` (à éviter)

```css
@import url('autre.css');                 /* à éviter : bloque le chargement en série */
@import url('theme.css') layer(theme);    /* possible avec une couche */
```

La règle `@import` doit se placer **tout en haut** de la feuille. Son défaut principal est technique : le navigateur ne découvre le fichier importé qu'après avoir téléchargé et analysé le fichier qui l'importe, ce qui force un téléchargement **en cascade** (les uns après les autres) et retarde l'affichage. On préfère plusieurs balises `<link>`, chargées en parallèle, ou un **outil de build** qui regroupe le CSS en un seul fichier (chapitre 18). `@import` garde un intérêt pour rattacher une feuille à une couche (`layer(...)`) dans un contexte où le build l'inline.

### 3.4 Charger le CSS efficacement

```html
<link rel='preload' href='/polices/inter.woff2' as='font' type='font/woff2' crossorigin>
<link rel='stylesheet' href='critique.css'>
<link rel='stylesheet' href='reste.css' media='print' onload='this.media="all"'>    <!-- chargement différé -->
```

Le CSS est **bloquant pour le rendu** : le navigateur retarde l'affichage tant qu'il n'a pas reçu les feuilles qui s'appliquent. Plusieurs stratégies permettent d'en limiter l'impact :

- Garder le CSS **léger** (supprimer le code mort, minifier, compresser en Brotli ou gzip).
- **Précharger** (`rel='preload'`) les ressources critiques découvertes tardivement, comme une police web référencée depuis le CSS (l'attribut `crossorigin` est obligatoire pour les polices).
- Intégrer le **CSS critique** dans le HTML et charger le reste de façon **différée**. L'astuce `media='print'` avec `onload` rend une feuille non bloquante : le navigateur la charge sans bloquer, puis la bascule vers `all`.
- Utiliser l'attribut `media` pour les feuilles qui ne s'appliquent qu'à un contexte précis.

### Synthèse du chapitre 3

- Feuille externe par défaut ; interne pour le CSS critique ; en ligne pour injecter des valeurs dynamiques.
- À spécificité égale, la dernière règle gagne : l'ordre des feuilles est significatif.
- Évitez `@import` pour charger des fichiers : préférez `<link>` ou un build.
- Le CSS bloque le rendu : gardez-le petit et chargez intelligemment le non critique.

---

## 4. Cascade, spécificité et héritage

**Objectifs d'apprentissage.** Vous saurez expliquer pourquoi une règle l'emporte sur une autre, calculer la spécificité d'un sélecteur, maîtriser les couches de cascade et la portée des styles, utiliser les mots-clés de contrôle de l'héritage et déboguer un conflit de styles.

### 4.1 Pourquoi « en cascade » ?

Un même élément est souvent visé par **plusieurs règles qui définissent la même propriété** : la feuille par défaut du navigateur, votre feuille, un framework, un style en ligne. La **cascade** est l'algorithme qui désigne la déclaration gagnante. Elle examine les critères suivants **dans cet ordre** et s'arrête dès qu'un critère départage les candidats :

| Rang | Critère | Explication |
| --- | --- | --- |
| 1 | **Origine et importance** | Trois origines : navigateur, utilisateur, auteur (vous). Normalement auteur > utilisateur > navigateur ; `!important` **inverse** cet ordre |
| 2 | **Contexte et couches** | Une couche déclarée plus tard l'emporte (hors `!important`, où l'ordre s'inverse aussi) ; les styles hors couche l'emportent sur les couches |
| 3 | **Spécificité** | Le sélecteur le plus spécifique gagne |
| 4 | **Ordre d'apparition** | À égalité totale, la **dernière** déclaration l'emporte |

Ce qui compte, c'est la déclaration individuelle : deux règles peuvent coexister sur un même élément, chacune contribuant les propriétés que l'autre ne définit pas. Le style final d'un élément est donc un **assemblage** de déclarations gagnantes provenant de nombreuses règles.

### 4.2 La spécificité *(à jour : calcul correct)*

La **spécificité** mesure la précision d'un sélecteur. Elle s'exprime par **trois colonnes (A, B, C)**, comparées **de gauche à droite**, et non comme un nombre décimal :

| Colonne | Compte | Exemples |
| --- | --- | --- |
| **A** | Sélecteurs d'**identifiant** | `#menu` |
| **B** | Sélecteurs de **classe**, d'**attribut** et **pseudo-classes** | `.carte`, `[type='text']`, `:hover` |
| **C** | Sélecteurs de **type** et **pseudo-éléments** | `p`, `::before` |

```css
p { }                     /* (0,0,1) */
.titre { }                /* (0,1,0) */
p.titre { }               /* (0,1,1) */
#titre { }                /* (1,0,0) */
nav ul li a:hover { }     /* (0,1,4) : 4 types + 1 pseudo-classe */
:is(#a, .b) { }           /* (1,0,0) : :is() prend le plus spécifique de ses arguments */
:where(#a, .b) { }        /* (0,0,0) : :where() vaut toujours zéro */
:not(.x) { }              /* (0,1,0) : comme son argument */
* { }                     /* (0,0,0) : l'universel et les combinateurs ne comptent pas */
```

**Comment comparer.** On compare d'abord la colonne A ; si elle est égale, la colonne B ; puis C. Une valeur plus grande dans une colonne de gauche l'emporte quelle que soit la valeur des colonnes de droite.

> **Idée reçue à corriger.** Beaucoup de supports enseignent « identifiant = 100, classe = 10, balise = 1 ». C'est une simplification : avec onze classes, on **ne bat pas** un identifiant, car (0,11,0) reste inférieur à (1,0,0). Les colonnes ne « débordent » jamais l'une sur l'autre.

**Au-dessus de la colonne A** se trouvent les **styles en ligne** (`style='...'`), qui l'emportent sur n'importe quel sélecteur, puis `!important`, qui passe devant tout, dans la même origine.

```css
#titre { color: blue; }     /* (1,0,0) */
.titre { color: red; }      /* (0,1,0) */
h1     { color: green; }    /* (0,0,1) */
/* <h1 id='titre' class='titre'> s'affiche en bleu */
```

**Cas particuliers.** Les pseudo-classes fonctionnelles prennent la spécificité de leur argument (`:is()`, `:not()`, `:has()`), sauf `:where()` qui vaut zéro. Les propriétés héritées n'ont **aucune** spécificité : une valeur déclarée directement sur un élément, même avec le plus faible des sélecteurs (`*`), l'emporte toujours sur une valeur simplement héritée.

### 4.3 `!important`

```css
.bouton { background: gray !important; }     /* à éviter */
```

Le marqueur `!important` place la déclaration dans une **catégorie prioritaire**. Il casse la logique normale de la cascade : pour le surcharger, il faut un autre `!important` plus spécifique ou plus tardif, ce qui crée des escalades difficiles à démêler. On le réserve à deux cas : les **classes utilitaires** dont la raison d'être est de toujours gagner (`.cache { display: none !important; }`), et la surcharge d'un style tiers impossible à modifier. Dans tous les autres cas, on préfère les **couches** (`@layer`) ou une spécificité maîtrisée.

### 4.4 Couches de cascade : `@layer` *(ajout, à jour)*

Les **couches de cascade** permettent de définir un **ordre de priorité par blocs de code**, **indépendamment de la spécificité** (Baseline depuis 2022). Elles résolvent le problème classique d'avoir à augmenter la spécificité pour battre un style préexistant.

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
    .texte-centre { text-align: center; }    /* l'emporte sur les couches précédentes, même avec une spécificité plus basse */
}

/* Les styles NON placés dans une couche l'emportent sur toutes les couches (hors !important) */
```

**Règles de fonctionnement.**

- La première instruction `@layer nom1, nom2, nom3;` **fixe l'ordre** : `nom3` aura la priorité sur `nom2`, qui aura la priorité sur `nom1`.
- La spécificité n'est comparée qu'**à l'intérieur d'une même couche**. Un sélecteur `.a` dans une couche tardive bat `#identifiant` dans une couche précoce.
- Les styles **hors couche** sont traités comme appartenant à une couche implicite finale, donc prioritaires sur les couches nommées.
- Avec `!important`, l'ordre des couches est **inversé** : une déclaration `!important` dans une couche précoce l'emporte sur une déclaration `!important` dans une couche tardive.

| Usage | Intérêt |
| --- | --- |
| Isoler un framework : `@import url('bootstrap.css') layer(framework);` | Vos styles gagnent toujours, sans `!important` |
| Architecture reset, base, composants, utilitaires | Ordre explicite et prévisible |
| Couches imbriquées : `@layer composants.bouton { ... }` | Organisation fine par composant |

### 4.5 Portée des styles : `@scope` *(ajout)*

`@scope` limite des règles à une **sous-arborescence** du document, délimitée par une **racine** et, facultativement, par une **borne inférieure** (« donut scope »). Les conflits sont départagés par la **proximité** : le style dont la racine est la plus proche de l'élément l'emporte, avant même la comparaison de l'ordre d'apparition.

```css
@scope (.carte) to (.contenu) {          /* dans .carte, mais pas à l'intérieur de .contenu */
    img { border-radius: .5rem; }
    h2 { font-size: 1.25rem; }
}
```

Dans un bloc `@scope`, la pseudo-classe `:scope` désigne la racine. `@scope` est Baseline *newly available* en 2026 ; il constitue une alternative native à BEM et aux CSS Modules pour limiter la portée des styles sans conventions de nommage lourdes. On vérifie le support avant de s'y fier sans repli.

### 4.6 Héritage

Certaines propriétés sont **héritées** : si un élément ne la définit pas, il reprend la valeur calculée de son **parent**. Il s'agit surtout des propriétés de **texte** : `color`, `font-family` et les autres `font-*`, `line-height`, `text-align`, `letter-spacing`, `visibility`, `cursor`, `list-style`. D'autres ne le sont **pas** : toutes les propriétés de **mise en page et de boîte** (`margin`, `padding`, `border`, `background`, `width`, `height`, `display`, `position`). Ce choix est logique : on veut qu'un lien dans un paragraphe reprenne la police du paragraphe, mais on ne veut pas qu'il hérite de sa bordure.

```css
body { color: #333; font-family: system-ui, sans-serif; }     /* hérité par tous les descendants */
```

Cette particularité explique une bonne pratique : on définit la typographie de base **une fois sur `body`** (ou `:root`), et chaque élément en profite sans règle supplémentaire.

#### Mots-clés de contrôle

| Mot-clé | Effet |
| --- | --- |
| `inherit` | Force la valeur du **parent**, même pour une propriété non héritée |
| `initial` | Valeur **initiale** définie par la spécification (pas celle du navigateur) |
| `unset` | Équivaut à `inherit` si la propriété est héritée, sinon à `initial` |
| `revert` | Revient à la valeur de la feuille du **navigateur** (ou de l'utilisateur) |
| `revert-layer` | Revient à la valeur de la **couche précédente** |
| `all: unset` | Réinitialise **toutes** les propriétés (sauf `direction` et `unicode-bidi`) |

```css
button { font: inherit; color: inherit; }            /* les boutons n'héritent pas de la police par défaut */
a { color: inherit; text-decoration: none; }
```

La différence entre `initial` et `revert` est subtile mais importante : `display: initial` donne `inline` pour tous les éléments (valeur initiale de la propriété), alors que `display: revert` redonne `block` à un `<div>` (valeur de la feuille du navigateur pour cet élément).

### 4.7 Déboguer la cascade

Quand un style ne s'applique pas, on suit une démarche systématique : vérifier que la règle est bien chargée et que le sélecteur correspond à l'élément, vérifier que la propriété et la valeur sont valides, puis chercher une règle concurrente plus spécifique ou plus tardive. Dans les **DevTools** (F12, onglet *Styles*), les règles sont listées par priorité décroissante, les déclarations **barrées** sont celles qui sont surchargées, un avertissement signale les valeurs invalides, et l'onglet *Computed* indique la valeur finale ainsi que la règle qui l'a produite (chapitre 27).

### Synthèse du chapitre 4

- La cascade tranche dans l'ordre : origine et importance, couches, spécificité, ordre d'apparition.
- La spécificité est un triplet (A, B, C) comparé de gauche à droite, sans débordement.
- `:where()` vaut zéro ; `:is()`, `:not()` et `:has()` prennent leur argument le plus spécifique.
- `@layer` maîtrise la priorité sans spécificité ; `@scope` limite la portée par proximité.
- Les propriétés de texte sont héritées, celles de boîte ne le sont pas ; `inherit`, `initial`, `unset`, `revert` et `revert-layer` contrôlent ce comportement.

---

## 5. Couleurs et unités

**Objectifs d'apprentissage.** Vous saurez exprimer une couleur dans tous les formats CSS, choisir entre eux, utiliser les fonctions de couleur modernes, gérer la transparence, connaître toutes les familles d'unités de longueur et savoir laquelle employer, et manipuler les fonctions mathématiques.

### 5.1 Formats de couleur

Une couleur peut s'écrire de plusieurs façons, qui désignent toutes un point d'un **espace colorimétrique**.

| Format | Exemple | Remarques |
| --- | --- | --- |
| **Nom** | `red`, `rebeccapurple`, `lightblue` | 148 couleurs nommées, pratiques pour les essais |
| **Hexadécimal** | `#ff0000`, `#f00`, `#ff000080` (avec alpha) | Très répandu ; 3, 4, 6 ou 8 chiffres |
| **`rgb()`** | `rgb(255 0 0)`, `rgb(255 0 0 / 50%)` | Syntaxe moderne : espaces et `/` pour l'alpha |
| **`hsl()`** | `hsl(240 100% 50%)`, `hsl(240 100% 50% / .3)` | Teinte (0 à 360 degrés), saturation, luminosité : intuitif |
| **`hwb()`** | `hwb(240 0% 0%)` | Teinte, blanc, noir |
| **`oklch()`** | `oklch(70% 0.15 250)` | Luminosité, chroma, teinte : **perceptuellement uniforme**, gamme étendue |
| **`oklab()`, `lab()`, `lch()`** | `lab(60% 40 20)` | Espaces perceptuels |
| **`color()`** | `color(display-p3 1 0 0)` | Espaces à gamut large (écrans P3) |
| **`currentColor`** | `border-color: currentColor;` | Reprend la valeur courante de `color` |
| **`transparent`** | `transparent` | Équivaut à `rgb(0 0 0 / 0)` |

**L'hexadécimal.** `#rrggbb` donne les composantes rouge, vert, bleu en base 16 (00 à ff). La forme abrégée `#rgb` double chaque chiffre : `#f00` vaut `#ff0000`. Deux chiffres supplémentaires (`#rrggbbaa`) ajoutent la **transparence** (alpha).

**RGB.** Trois canaux de 0 à 255 (ou en pourcentage). C'est le modèle naturel des écrans, mais il n'est pas intuitif pour « éclaircir » une couleur.

**HSL.** La **teinte** est un angle sur le cercle chromatique (0 rouge, 120 vert, 240 bleu), la **saturation** va du gris (0 %) à la couleur pure (100 %), la **luminosité** du noir (0 %) au blanc (100 %). HSL facilite la création de variantes d'une couleur en ne modifiant qu'un paramètre. Son défaut : deux couleurs de même luminosité HSL peuvent paraître de clartés très différentes à l'œil.

**OKLCH.** Ce format répond à ce défaut : sa **luminosité (L)** correspond à la clarté perçue, son **chroma (C)** à l'intensité, sa **teinte (H)** à un angle. Il permet de produire des palettes régulières et de calculer des contrastes prévisibles ; il donne aussi accès à des couleurs plus vives que le sRGB sur les écrans compatibles.

```css
p {
    color: rgb(0 128 0);                          /* vert */
    background: rgb(255 0 0 / 50%);                /* rouge semi-transparent (remplace rgba()) */
    border-color: hsl(210 80% 50%);
}
```

> **À jour.** Les formes **`rgba()`** et **`hsla()`** ainsi que les **virgules** (`rgb(255, 0, 0)`) sont historiques mais restent valides. La syntaxe moderne `rgb(r g b / a)` est équivalente et plus cohérente.

#### Fonctions de couleur modernes *(ajout)*

**`color-mix()`** mélange deux couleurs dans un espace choisi, selon des proportions données.

```css
.bouton:hover { background: color-mix(in oklch, royalblue 85%, black); }   /* assombrit légèrement */
.survol { background: color-mix(in srgb, currentColor 10%, transparent); } /* voile translucide */
```

**La syntaxe de couleur relative** dérive une couleur d'une autre en accédant à ses canaux (`l`, `c`, `h`, ou `r`, `g`, `b`), ce qui permet de construire toute une palette à partir d'une seule couleur de marque.

```css
:root {
    --marque: oklch(60% 0.2 260);
    --marque-claire: oklch(from var(--marque) calc(l + 0.2) c h);
    --marque-translucide: rgb(from var(--marque) r g b / 40%);
}
```

**`light-dark()`** retourne la première valeur en thème clair et la seconde en thème sombre ; elle nécessite que `color-scheme` autorise les deux thèmes.

```css
:root { color-scheme: light dark; }
body { background: light-dark(#fff, #121212); color: light-dark(#222, #eee); }
```

**`contrast-color()`** choisit une couleur de texte lisible (noir ou blanc) pour un fond donné. Son support est récent : on prévoit un repli.

```css
.badge { background: var(--fond); color: contrast-color(var(--fond)); }
```

### 5.2 Opacité

```css
div { opacity: .5; }                     /* attention : affecte l'élément ET tous ses enfants */
div { background: rgb(0 0 0 / .5); }     /* seulement le fond */
```

`opacity` s'applique à l'élément **entier** (fond, texte, bordure, descendants) et crée un contexte d'empilement. Pour ne rendre transparent que le fond, on utilise un canal alpha dans la couleur. `opacity: 0` rend un élément invisible mais **toujours présent** (il prend de la place et reste cliquable) ; `visibility: hidden` et `display: none` ont des effets différents (chapitre 8).

### 5.3 Unités de longueur

Une longueur est un nombre suivi d'une **unité** (sans espace). Zéro est la seule valeur qui n'exige pas d'unité.

#### Unités absolues

| Unité | Description |
| --- | --- |
| `px` | Pixel CSS, unité de référence (pas forcément un pixel physique : 96 px CSS valent 1 pouce CSS) |
| `cm`, `mm`, `in`, `pt`, `pc`, `Q` | Unités physiques : centimètre, millimètre, pouce, point, pica, quart de millimètre ; surtout utiles à l'impression |

#### Unités relatives à la typographie

| Unité | Relative à |
| --- | --- |
| `em` | **Taille de police** de l'élément (de son parent lorsqu'on l'emploie dans `font-size`) |
| `rem` | Taille de police de l'élément **racine** (`<html>`) |
| `ch` | Largeur du caractère « 0 » : idéal pour limiter la longueur de ligne (`max-width: 65ch`) |
| `ex`, `cap`, `ic` | Hauteur du « x », des majuscules, d'un idéogramme |
| `lh`, `rlh` | **Hauteur de ligne** de l'élément, de la racine |

Le piège de `em` est sa **composition** : un `em` dans un `font-size` se calcule par rapport au parent, donc des éléments imbriqués à `1.2em` se multiplient. `rem` évite ce problème car il se réfère toujours à la racine.

#### Unités relatives à la fenêtre (*viewport*) *(à jour)*

| Unité | Signification |
| --- | --- |
| `vw`, `vh` | 1 % de la largeur, de la hauteur de la fenêtre |
| `vmin`, `vmax` | 1 % de la plus petite, de la plus grande dimension |
| `svh`, `lvh`, `dvh` | Hauteur **petite** (barre d'adresse visible), **grande** (barre masquée), **dynamique** (s'adapte en continu) |
| `svw`, `lvw`, `dvw` ; `vi`, `vb` | Équivalents horizontaux ; axes **logiques** (inline, block) |

```css
.hero { min-height: 100dvh; }   /* sur mobile, 100vh dépasse la zone visible à cause de la barre d'adresse */
```

Les unités `s`, `l` et `d` résolvent un vieux problème des navigateurs mobiles : la barre d'adresse apparaît et disparaît au défilement, de sorte que `100vh` correspond à la fenêtre la plus grande, ce qui déborde quand la barre est visible.

#### Unités relatives au conteneur *(ajout)*

| Unité | Signification |
| --- | --- |
| `cqw`, `cqh` | 1 % de la largeur, de la hauteur du **conteneur** (chapitre 14) |
| `cqi`, `cqb`, `cqmin`, `cqmax` | Axes logiques, minimum et maximum |

#### Autres unités

| Unité | Usage |
| --- | --- |
| `%` | Pourcentage d'une référence qui dépend de la propriété (largeur du parent pour `width`, taille de police du parent pour `font-size`) |
| `fr` | Fraction de l'espace disponible (**Grid**) |
| `deg`, `rad`, `grad`, `turn` | Angles |
| `s`, `ms` | Durées |
| `dpi`, `dpcm`, `dppx` (`x`) | Résolution |

```css
html { font-size: 100%; }                 /* 16px par défaut : respecte les préférences de l'utilisateur */
h1 { font-size: 2rem; margin-block: 1.5rem; }
.contenu { max-width: 65ch; }
.panneau { width: 80%; }
.hero { height: 50svh; }
```

> **Comment choisir.** `rem` pour les **polices et les espacements** (accessibilité : suit le réglage de taille de texte de l'utilisateur) ; `em` pour les composants qui doivent **s'adapter à leur propre taille** ; `px` pour les **bordures fines** ; `%`, `fr`, `dvh` et `cq*` pour la **mise en page**.

Un point d'accessibilité important : ne fixez pas `html { font-size: 62.5% }` ou `font-size` en pixels sans réflexion. Utiliser `100%` (ou ne rien définir) laisse le navigateur appliquer la taille choisie par l'utilisateur dans ses préférences.

### 5.4 Fonctions mathématiques *(ajout)*

CSS offre des fonctions de calcul qui permettent de combiner des unités différentes et de créer des valeurs fluides sans JavaScript.

```css
.exemple-calc   { width: calc(100% - 2rem); }                         /* mélange d'unités */
.exemple-min    { width: min(90%, 60rem); }                           /* la plus petite valeur */
.exemple-max    { padding: max(1rem, 3vw); }                          /* la plus grande */
.exemple-clamp  { font-size: clamp(1rem, 0.9rem + 1vw, 1.5rem); }    /* minimum, valeur fluide, maximum */
.exemple-round  { height: round(down, 100%, 8px); }                   /* arrondi à un multiple */
.exemple-rotate { --i: 2; transform: rotate(calc(var(--i) * 15deg)); }
.exemple-grille { --colonnes: 3; display: grid; grid-template-columns: repeat(var(--colonnes), 1fr); }
```

- **`calc()`** effectue des additions, soustractions, multiplications et divisions. Les opérateurs `+` et `-` doivent être entourés d'espaces. Elle permet de mélanger par exemple pourcentages et `rem`.
- **`min()`** et **`max()`** retournent la plus petite ou la plus grande des valeurs ; `min(90%, 60rem)` crée un plafond de largeur sans `max-width`.
- **`clamp(minimum, préférée, maximum)`** borne une valeur variable entre deux limites ; c'est l'outil principal de la typographie fluide (section 7.7).
- **`round()`**, **`mod()`**, **`rem()`** arrondissent ou calculent un reste ; **`abs()`** et **`sign()`** donnent la valeur absolue et le signe.
- Fonctions **trigonométriques** : `sin()`, `cos()`, `tan()`, `asin()`, `acos()`, `atan()`, `atan2()` ; fonctions **exponentielles** : `pow()`, `sqrt()`, `hypot()`, `log()`, `exp()`.

Ces fonctions se combinent avec les variables CSS (`var()`), ce qui ouvre la voie à des mises en page paramétrées entièrement en CSS.

### Synthèse du chapitre 5

- Préférez la syntaxe moderne `rgb(r g b / a)` ; `oklch()` pour des palettes cohérentes ; `color-mix()` et la couleur relative pour dériver des variantes.
- `opacity` affecte tout l'élément ; un canal alpha n'affecte que la couleur.
- `rem` pour texte et espacements, `em` pour l'adaptation locale, `ch` pour la mesure de ligne, `dvh` pour la hauteur d'écran mobile, `cq*` pour les conteneurs.
- `calc()`, `min()`, `max()` et `clamp()` permettent des valeurs fluides sans media query.

---

## 6. Le modèle de boîte

**Objectifs d'apprentissage.** Vous saurez décrire les quatre zones d'une boîte, maîtriser `box-sizing`, dimensionner un élément avec les valeurs fixes, relatives et intrinsèques, gérer marges et espacements, comprendre la fusion des marges, adopter les propriétés logiques et styliser bordures et contours.

### 6.1 Tout élément est une boîte

Pour le moteur de rendu, **chaque élément est un rectangle** composé de quatre couches emboîtées : le contenu, le padding, la bordure et la marge.

```text
+----------------------- margin (marge) -----------------------+
|  +------------------- border (bordure) -------------------+  |
|  |  +-------------- padding (marge intérieure) -------+   |  |
|  |  |                                                 |   |  |
|  |  |                content (contenu)                |   |  |
|  |  |                                                 |   |  |
|  |  +-------------------------------------------------+   |  |
|  +--------------------------------------------------------+  |
+--------------------------------------------------------------+
```

| Zone | Rôle | Reçoit le fond de l'élément ? |
| --- | --- | --- |
| **Contenu** | Texte, images, éléments enfants | Oui |
| **Padding** | Espace **intérieur** entre le contenu et la bordure | Oui |
| **Bordure** | Contour de la boîte | Oui (le fond passe sous la bordure par défaut) |
| **Marge** | Espace **extérieur**, toujours transparent | Non |

La **marge** sert à éloigner la boîte de ses voisines ; le **padding** sert à donner de l'air au contenu à l'intérieur de la boîte. Cette différence se perçoit à l'effet du fond : la couleur de fond s'étend sous le padding mais pas sous la marge.

### 6.2 `box-sizing`

Par défaut (`content-box`), `width` et `height` ne concernent que le **contenu** : le padding et la bordure s'**ajoutent** à la taille déclarée, et la boîte devient plus grande que prévu. Ce comportement est source de nombreux débordements.

```css
.boite { width: 300px; padding: 20px; border: 5px solid; }
/* content-box : largeur réelle = 300 + 2x20 + 2x5 = 350px
   border-box  : largeur réelle = 300px (le contenu rétrécit pour compenser) */
```

Avec `border-box`, `width` désigne la largeur **totale** (contenu, padding et bordure). C'est plus intuitif, surtout avec les pourcentages : deux boîtes à `width: 50%` avec padding et bordure tiennent côte à côte.

```css
/* Réglage universel recommandé */
*, *::before, *::after { box-sizing: border-box; }
```

La marge n'est jamais incluse dans `width`, quel que soit le mode.

### 6.3 Largeur et hauteur

```css
.boite {
    width: 50%;
    height: auto;                          /* défaut : s'adapte au contenu */
    min-width: 200px;  max-width: 100%;
    min-height: 100px; max-height: 80vh;
    aspect-ratio: 16 / 9;                  /* rapport largeur/hauteur (remplace le « padding hack ») */
}

.contenu {
    width: fit-content;                    /* mots-clés intrinsèques */
    width: min-content;  width: max-content;
    max-inline-size: 65ch;
}
```

| Valeur | Effet |
| --- | --- |
| `auto` | Selon le type d'élément : un bloc occupe toute la largeur disponible ; la hauteur suit le contenu |
| `fit-content` | S'ajuste au contenu mais **plafonné** par l'espace disponible |
| `min-content` | Plus petite largeur possible sans débordement (le contenu se replie au maximum) |
| `max-content` | Plus grande largeur utile (le contenu ne se replie pas) |
| `stretch` | Remplit l'espace disponible, marges comprises |

Les propriétés `min-*` et `max-*` **bornent** une dimension et l'emportent sur `width` et `height`. `aspect-ratio` fixe un rapport entre la largeur et la hauteur, ce qui remplace l'ancienne technique du « padding hack » (un padding en pourcentage pour simuler un rapport).

> **Recommandation.** Combinez `width: 100%` et `max-width` pour des éléments flexibles. Préférez **`min-height`** à `height` : une hauteur fixe fait déborder le texte quand il est agrandi ou traduit.

### 6.4 Marges et espacement intérieur

Les raccourcis `margin` et `padding` acceptent de une à quatre valeurs.

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

Les marges peuvent être **négatives** (la boîte empiète sur sa voisine), les paddings **jamais**. `margin: auto` sur l'axe horizontal répartit l'espace restant de part et d'autre, ce qui centre un bloc dont la largeur est limitée.

#### Fusion des marges (*margin collapsing*)

Les **marges verticales** de blocs adjacents **fusionnent** : au lieu de s'additionner, c'est la plus grande qui l'emporte. Ce comportement s'applique aux marges entre frères successifs, entre un parent et son premier ou dernier enfant lorsque rien ne les sépare, et aux blocs vides. Il ne se produit **pas** : dans un conteneur **Flexbox ou Grid**, avec des marges **horizontales**, lorsqu'un `padding`, une `border` ou un contenu sépare les marges, ni lorsque le parent établit un nouveau contexte de formatage (par exemple avec `overflow` autre que `visible`, ou `display: flow-root`).

```css
h2 { margin-bottom: 2rem; }
p  { margin-top: 1rem; }               /* l'espace entre h2 et p vaut 2rem, et non 3rem */
```

> **Astuce moderne.** Utilisez **`gap`** (Flexbox et Grid) ou un seul sens de marge (`margin-block-end`) pour espacer les éléments de façon prévisible et éviter les surprises de fusion.

### 6.5 Propriétés logiques *(à jour)*

Les propriétés **physiques** (`left`, `width`, `margin-top`) sont liées à la géométrie de l'écran. Les propriétés **logiques** sont liées au **sens d'écriture** : l'axe **inline** est le sens de lecture d'une ligne, l'axe **block** est celui dans lequel les lignes s'empilent. En français (gauche à droite, haut vers bas), inline correspond à l'horizontale et block à la verticale ; en arabe (droite à gauche), inline est inversé ; en japonais vertical, les deux axes permutent. Les propriétés logiques s'adaptent donc automatiquement, ce qui est indispensable pour l'internationalisation.

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

Le raccourci `inset` remplace `top`, `right`, `bottom`, `left` ensemble (`inset: 0` étire un élément positionné sur tout son parent).

### 6.6 Bordures et contours

```css
.boite {
    border: 2px solid black;               /* largeur | style | couleur */
    border-top: 1px dashed gray;
    border-radius: 8px;                    /* coins arrondis */
    border-radius: 50%;                    /* cercle ou ellipse */
    border-radius: 10px 20px 30px 40px;    /* haut-gauche, haut-droite, bas-droite, bas-gauche */
}
```

Le raccourci `border` combine `border-width`, `border-style` et `border-color`. **Le style est obligatoire** : sans lui, la bordure n'apparaît pas (la valeur par défaut est `none`). Styles disponibles : `solid`, `dashed`, `dotted`, `double`, `groove`, `ridge`, `inset`, `outset`, `none`, `hidden`. `border-radius` accepte aussi deux valeurs séparées par `/` pour des coins elliptiques.

#### `outline` : un contour qui ne prend pas de place

```css
button:focus-visible {
    outline: 3px solid royalblue;
    outline-offset: 2px;
}
```

Contrairement à la bordure, `outline` est dessiné **hors de la boîte** : il ne modifie ni la taille ni la mise en page, et il suit les coins arrondis dans les navigateurs modernes. `outline-offset` l'éloigne de la bordure.

> **Ne supprimez jamais `outline` sans le remplacer.** `outline: none` rend la navigation au clavier impossible pour de nombreux utilisateurs. Utilisez `:focus-visible` pour afficher l'anneau uniquement lors d'une navigation au clavier.

### 6.7 Débordement et affichage du modèle de boîte

```css
.boite {
    overflow: hidden;                      /* voir chapitre 8 */
    box-sizing: border-box;
}
```

Le comportement d'une boîte dépend de son type d'affichage. Un élément **en ligne** (`inline`) **ignore** `width` et `height` ainsi que les marges verticales ; un **bloc** (`block`) occupe toute la largeur disponible et accepte toutes les dimensions ; un **inline-block** se place dans le flux du texte tout en acceptant les dimensions (chapitre 8).

### 6.8 Bonnes pratiques

- Appliquez `box-sizing: border-box` partout.
- Utilisez des **unités relatives** (`rem`, `%`, `ch`) et `max-width` plutôt que des largeurs fixes en pixels.
- Espacez avec **`gap`**, `margin-block` et `padding-inline`, en vous appuyant sur une **échelle d'espacement** (variables `--esp-1`, `--esp-2`, etc.) pour garder une cohérence visuelle.
- Adoptez les **propriétés logiques** pour un code prêt à l'internationalisation.
- Ne supprimez jamais l'indicateur de focus sans alternative.

### Synthèse du chapitre 6

- Une boîte = contenu, padding, bordure, marge ; la marge est transparente.
- `border-box` fait de `width` la largeur totale hors marge.
- Les marges verticales fusionnent dans le flux normal, pas dans Flexbox ni Grid.
- Propriétés logiques : `inline` (sens de lecture) et `block` (empilement).
- `outline` ne prend pas de place et sert au focus ; ne le supprimez pas.

---

## 7. Texte et polices

**Objectifs d'apprentissage.** Vous saurez contrôler l'alignement, la décoration et la casse du texte, choisir et déclarer des polices (système, web, variables), régler interlignage et espacement, maîtriser les retours à la ligne et la troncature, utiliser les fonctions typographiques avancées, mettre en place une taille de texte fluide et respecter les exigences d'accessibilité du texte.

### 7.1 Propriétés de texte

```css
p {
    color: #333;
    text-align: start;                       /* start | end | center | justify */
    text-indent: 2em;                        /* retrait de la première ligne */
    text-decoration: underline wavy red;     /* ligne | style | couleur */
    text-transform: capitalize;
}
```

- **`color`** fixe la couleur du texte. Elle est héritée et sert aussi de valeur à `currentColor`.
- **`text-align`** aligne le contenu en ligne dans son bloc : `start` et `end` (logiques, selon le sens d'écriture), `center`, `justify`, ainsi que `left` et `right` (physiques, à éviter pour l'internationalisation). `justify` étire les espaces pour que chaque ligne atteigne les deux bords.
- **`text-indent`** décale la première ligne d'un bloc, comme dans un livre.
- **`vertical-align`** (pour les éléments en ligne et les cellules de tableau) aligne verticalement par rapport à la ligne de base : `baseline`, `middle`, `sub`, `super`, `top`, `bottom`.

#### `text-decoration` et ses propriétés détaillées

```css
a {
    text-decoration-line: underline;         /* none | underline | overline | line-through */
    text-decoration-style: solid;            /* solid | double | dotted | dashed | wavy */
    text-decoration-color: tomato;
    text-decoration-thickness: .1em;
    text-underline-offset: .2em;             /* distance entre le texte et le soulignement */
    text-decoration-skip-ink: auto;          /* évite de traverser les jambages (g, p, y) */
}
```

Le raccourci `text-decoration` regroupe ligne, style, couleur et épaisseur. Régler `text-underline-offset` et `text-decoration-thickness` en `em` donne un soulignement plus aéré et plus lisible que le défaut du navigateur. Retirer le soulignement d'un lien (`text-decoration: none`) n'est acceptable que si le lien reste identifiable autrement (couleur contrastée, gras, icône).

#### `text-transform`

Les valeurs sont `none`, `uppercase`, `lowercase`, `capitalize` (première lettre de chaque mot) et `full-width`. La transformation est purement visuelle : le texte source reste inchangé pour les lecteurs d'écran et pour la copie, ce qui est un avantage sur une réécriture en majuscules dans le HTML.

### 7.2 Polices

```css
body {
    font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;   /* liste de repli */
    font-size: 1rem;
    font-weight: 400;                        /* 100 à 900 (normal = 400, bold = 700) */
    font-style: italic;                      /* normal | italic | oblique */
    font-variant-numeric: tabular-nums;      /* chiffres de largeur fixe (tableaux) */
}
```

**`font-family`** prend une **liste** de polices séparées par des virgules. Le navigateur utilise la première disponible. On termine toujours par une **famille générique** qui garantit un repli. Les noms contenant des espaces ou des caractères spéciaux se mettent entre guillemets.

**`font-size`** définit la taille ; on l'exprime en `rem`. **`font-weight`** fixe la graisse, de 100 (très fin) à 900 (très gras) ; seules les graisses effectivement fournies par la police sont rendues fidèlement, les autres sont approximées. **`font-style`** choisit entre droit (`normal`), italique (dessin spécifique) et oblique (inclinaison mécanique). **`font-variant-numeric`** règle le rendu des chiffres : `tabular-nums` aligne les colonnes de nombres.

| Famille générique | Exemples et usage |
| --- | --- |
| `serif` | Polices à empattements : Georgia, Times |
| `sans-serif` | Polices sans empattements : Arial, Helvetica |
| `monospace` | Chasse fixe : Courier, Consolas (code) |
| `system-ui` | Police système de l'utilisateur : rapide, native, sans téléchargement |
| `ui-serif`, `ui-sans-serif`, `ui-monospace`, `ui-rounded` | Variantes système |
| `cursive`, `fantasy`, `math` | Familles spécifiques, rendu variable selon la plateforme |

#### Le raccourci `font`

```css
p { font: italic 700 1.125rem/1.6 Georgia, serif; }
/* style poids taille/hauteur-de-ligne famille : taille et famille sont obligatoires */
```

Attention : comme tout raccourci, `font` **réinitialise** les propriétés qu'il ne mentionne pas (`font-variant`, `font-stretch`, etc.) à leur valeur initiale.

### 7.3 Polices web : `@font-face`

La règle `@font-face` permet de charger une police depuis un fichier et de lui donner un nom utilisable dans `font-family`.

```css
@font-face {
    font-family: 'Inter';
    src: url('/polices/inter-var.woff2') format('woff2');      /* WOFF2 : format recommandé */
    font-weight: 100 900;                                       /* police VARIABLE : plage de graisses */
    font-style: normal;
    font-display: swap;                                         /* texte affiché tout de suite avec un repli */
    unicode-range: U+0000-00FF;                                 /* téléchargé seulement si ces caractères sont utilisés */
}
```

Le **format WOFF2** est le format recommandé : il est compressé et pris en charge par tous les navigateurs modernes. `unicode-range` découpe une police en **sous-ensembles** (latin, cyrillique, etc.) et n'en télécharge que ce qui est utilisé.

| `font-display` | Comportement |
| --- | --- |
| `auto` | Décision du navigateur (souvent comme `block`) |
| `block` | Courte période d'invisibilité, puis échange |
| `swap` | Texte visible immédiatement avec la police de repli, puis échange dès que la police est prête |
| `fallback` | Période d'invisibilité très courte, échange limité dans le temps |
| `optional` | La police web n'est utilisée que si elle est déjà disponible (meilleur pour les performances) |

Le compromis est le suivant : `swap` garantit la lisibilité mais peut provoquer un saut de mise en page quand la police arrive (le *Cumulative Layout Shift*) ; `optional` évite tout saut au prix d'un affichage parfois sans la police choisie.

#### Polices variables *(ajout)*

Une **police variable** est un fichier unique qui contient un continuum de variations (graisse, largeur, inclinaison, parfois d'autres axes), au lieu d'un fichier par style. Elle réduit le nombre de requêtes et permet des valeurs intermédiaires.

```css
h1 { font-variation-settings: 'wght' 650, 'wdth' 110; }   /* axes par leur nom de 4 lettres */
.fin { font-weight: 300; }
.large { font-stretch: 125%; }
```

On préfère les propriétés standard (`font-weight`, `font-stretch`, `font-style`) à `font-variation-settings` lorsqu'elles existent, car cette dernière ne se combine pas avec le reste de la cascade.

#### Conseils de performance

- Utilisez le format **WOFF2**, des **sous-ensembles** (`unicode-range`) et `font-display: swap` ou `optional`.
- **Préchargez** la police critique : `<link rel='preload' as='font' type='font/woff2' crossorigin>`.
- Limitez le nombre de familles et de graisses ; privilégiez une **police variable** ou la **pile système**.
- Hébergez les polices **localement** plutôt que via un CDN tiers (conformité au RGPD, performances, absence de dépendance).
- Réduisez le décalage de mise en page avec `size-adjust`, `ascent-override` et `descent-override`, qui alignent les métriques de la police de repli sur celles de la police web.

### 7.4 Espacement du texte

```css
p {
    line-height: 1.6;                       /* SANS unité : multiple de la taille de police */
    letter-spacing: .02em;                  /* espacement des lettres */
    word-spacing: .1em;                     /* espacement des mots */
}
h1 { line-height: 1.2; letter-spacing: -.02em; }
```

> **`line-height` sans unité** (1,5 à 1,7 pour le texte courant) est héritée comme **facteur** et recalculée pour chaque élément selon sa propre taille de police. Avec une unité (`24px`), c'est la valeur **calculée** qui est héritée telle quelle : un titre plus grand hériterait alors d'un interligne trop serré.

Les grands titres demandent un interligne plus faible (1,1 à 1,3) que le texte courant, et parfois un `letter-spacing` légèrement négatif. Les petites capitales et les textes en majuscules gagnent à recevoir un `letter-spacing` positif.

### 7.5 Gestion de l'espace blanc et du retour à la ligne

| Propriété | Valeurs utiles |
| --- | --- |
| `white-space` | `normal`, `nowrap` (aucun retour), `pre` (préserve espaces et sauts), `pre-wrap`, `pre-line`, `break-spaces` |
| `overflow-wrap` | `normal`, `break-word`, `anywhere` : coupe les mots trop longs pour éviter le débordement |
| `word-break` | `normal`, `break-all`, `keep-all` (utile pour le chinois, le japonais et le coréen) |
| `hyphens` | `manual`, `auto` (césure automatique, nécessite l'attribut `lang`) |
| `text-wrap` | `balance` (titres équilibrés), `pretty` (évite les lignes orphelines), `nowrap`, `stable` |
| `text-overflow` | `clip`, `ellipsis` (avec `overflow: hidden` et `white-space: nowrap`) |

```css
h1, h2, h3 { text-wrap: balance; }        /* lignes de longueur équilibrée */
p { text-wrap: pretty; hyphens: auto; overflow-wrap: break-word; }

.une-ligne {                              /* une ligne tronquée par des points de suspension */
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.trois-lignes {                           /* troncature multiligne (largement supportée) */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    line-clamp: 3;
    overflow: hidden;
}
```

Par défaut (`white-space: normal`), le navigateur **fusionne** les espaces consécutifs et les sauts de ligne du HTML en un seul espace. `pre` conserve la mise en forme (utile pour du code), `pre-wrap` la conserve tout en autorisant le retour automatique. `overflow-wrap: break-word` coupe un mot trop long uniquement s'il déborderait, et `anywhere` le fait aussi lors du calcul des tailles intrinsèques. La troncature `text-overflow: ellipsis` ne fonctionne que sur un bloc dont le débordement est caché et dont le texte ne passe pas à la ligne. Pour la troncature sur plusieurs lignes, la technique historique avec le préfixe `-webkit-` reste la plus compatible, `line-clamp` standard étant en cours d'adoption.

### 7.6 Style de texte avancé

```css
.etiquette { font-variant-caps: all-small-caps; }
.chiffre { font-feature-settings: 'tnum' 1; }                     /* fonctionnalités OpenType */
.colonnes { column-count: 2; column-gap: 2rem; column-rule: 1px solid #ddd; }   /* colonnes de journal */
.vertical { writing-mode: vertical-rl; }
.degrade { background: linear-gradient(90deg, red, blue); background-clip: text; color: transparent; }   /* texte dégradé */
.lettrine::first-letter { initial-letter: 3; }                    /* lettrine (support partiel) */
p { text-box-trim: trim-both; text-box-edge: cap alphabetic; }    /* aligner sur la hauteur des capitales (support récent) */
```

- **`font-variant-caps`** active les petites capitales ; **`font-feature-settings`** active des fonctionnalités OpenType par leur code (`tnum` pour des chiffres tabulaires, `liga` pour les ligatures). Préférez les propriétés `font-variant-*` quand elles existent.
- **Colonnes de journal** : `column-count` fixe le nombre de colonnes, `column-width` leur largeur idéale, `column-gap` la gouttière, `column-rule` le filet.
- **`writing-mode`** change le sens d'écriture (`horizontal-tb`, `vertical-rl`, `vertical-lr`).
- **Texte dégradé** : le fond est découpé selon la forme des lettres avec `background-clip: text`, et le texte rendu transparent. Prévoyez un repli de couleur pour les contextes où le fond n'est pas rendu.
- **`initial-letter`** crée une lettrine sur un nombre de lignes donné. **`text-box-trim`** et **`text-box-edge`** retirent l'espace vide au-dessus et au-dessous du texte pour l'aligner sur les capitales ou la ligne de base : ces deux propriétés sont récentes, à vérifier avant usage.

### 7.7 Taille de texte fluide *(ajout)*

Au lieu de définir une taille par point de rupture, on peut faire **varier le texte continuellement** avec `clamp()` : la taille croît avec la largeur de la fenêtre, entre un minimum et un maximum.

```css
:root {
    --texte: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
    --titre: clamp(1.75rem, 1.2rem + 2.5vw, 3rem);
}
body { font-size: var(--texte); }
h1 { font-size: var(--titre); }
```

Pour que la valeur intermédiaire reste accessible, on mélange une partie en `rem` et une partie en `vw` (`0.95rem + 0.25vw`) : une valeur uniquement en `vw` ne réagirait pas au zoom du texte de l'utilisateur. On vérifie que le texte atteint bien le double de sa taille lorsque l'utilisateur zoome à 200 %.

### 7.8 Accessibilité du texte

- Taille de base **16 px** (ne pas descendre sous 1 rem) ; utilisez des **`rem`** pour respecter les préférences de zoom.
- **Contraste** suffisant : **4,5 pour 1** pour le texte courant (niveau AA des WCAG), **3 pour 1** pour le grand texte (au moins 24 px, ou 18,66 px en gras).
- **Longueur de ligne** de 45 à 75 caractères (`max-width: 65ch`).
- **Interligne** d'au moins 1,5 pour le texte courant.
- N'utilisez pas `text-align: justify` sans `hyphens: auto` : les grands espaces (« rivières ») gênent la lecture, notamment pour les personnes dyslexiques.
- Le texte doit rester lisible si l'utilisateur modifie l'interligne, l'espacement des lettres et des mots (critère de succès 1.4.12 des WCAG) : ne fixez pas de hauteurs rigides sur les conteneurs de texte.

### Synthèse du chapitre 7

- Texte : `text-align: start`, interligne sans unité, décoration réglée en `em`.
- `font-family` toujours avec un repli générique ; WOFF2, sous-ensembles et `font-display` pour les polices web ; polices variables pour moins de fichiers.
- `text-wrap: balance` pour les titres, `pretty` pour les paragraphes, `ellipsis` pour la troncature.
- `clamp()` avec un mélange `rem` et `vw` produit une typographie fluide et accessible.
- Contraste 4,5 pour 1, lignes de 45 à 75 caractères, tailles en `rem`.

---

---

## 8. Affichage, positionnement et débordement

**Objectifs d'apprentissage.** Vous saurez choisir le bon type d'affichage, positionner un élément avec `position`, centrer dans toutes les situations, maîtriser l'empilement avec `z-index` et les contextes d'empilement, gérer le débordement et le défilement, traiter correctement les images et vidéos, comprendre les flottants hérités et savoir quel outil de mise en page choisir.

### 8.1 La propriété `display`

`display` définit **comment un élément se comporte dans le flux de la page**, et comment ses enfants sont disposés. Elle combine en réalité deux notions : le **type d'affichage extérieur** (comment l'élément se place par rapport à ses frères : bloc ou en ligne) et le **type d'affichage intérieur** (comment il dispose son propre contenu : flux normal, Flexbox, Grid).

| Valeur | Comportement |
| --- | --- |
| `block` | Occupe **toute la largeur disponible** et commence sur une **nouvelle ligne** ; accepte `width`, `height` et toutes les marges (`<div>`, `<p>`, `<h1>`) |
| `inline` | S'insère **dans la ligne de texte** ; **ignore** `width`, `height` et les marges verticales (`<span>`, `<a>`) |
| `inline-block` | Se place en ligne **mais** accepte `width`, `height` et les marges |
| `none` | **Retire** l'élément et ses enfants de la page et de l'arbre d'accessibilité |
| `flex` / `inline-flex` | Conteneur **Flexbox** (chapitre 9) |
| `grid` / `inline-grid` | Conteneur **Grid** (chapitre 10) |
| `flow-root` | Crée un **contexte de formatage de bloc** : contient les flottants et empêche la fusion des marges |
| `contents` | L'élément « disparaît » de la mise en page : ses **enfants** deviennent des enfants de son parent |
| `table`, `table-row`, `table-cell` | Comportements de tableau appliqués à n'importe quel élément |
| `list-item` | Se comporte comme un `<li>`, avec une puce |

```css
.cache { display: none; }
.bouton { display: inline-block; padding: .5em 1em; }
.parent { display: flow-root; }          /* contient ses enfants flottants, sans clearfix */
```

Plusieurs points méritent d'être détaillés :

- **Bloc et en ligne.** Un élément `block` s'étend sur la largeur de son parent et se place sous le précédent. Un élément `inline` suit le fil du texte, passe à la ligne avec lui et n'a pas de dimensions propres. `inline-block` combine les deux : il se positionne comme un mot dans la ligne mais se dimensionne comme un bloc.
- **`flow-root`** résout deux problèmes classiques : un parent dont tous les enfants sont flottants s'effondre à une hauteur nulle ; `flow-root` l'oblige à les contenir. Il empêche aussi la fusion des marges entre le parent et son premier ou dernier enfant.
- **`display: contents`** est utile pour qu'un élément d'encapsulation n'interfère pas avec une grille ou un conteneur flex. Attention : appliqué à des éléments sémantiques (boutons, listes, tableaux), il a pu supprimer leur rôle d'accessibilité selon les navigateurs ; testez avec un lecteur d'écran.

> **Accessibilité.** `display: none` et `visibility: hidden` masquent l'élément **aussi aux lecteurs d'écran**. Pour masquer **visuellement** seulement, on utilise la technique `.sr-only` (chapitre 16).

#### Trois manières de cacher un élément

|  | `display: none` | `visibility: hidden` | `opacity: 0` |
| --- | --- | --- | --- |
| Prend de la place | Non | Oui | Oui |
| Interactif (clic, focus) | Non | Non | Oui |
| Lu par les lecteurs d'écran | Non | Non | Oui |
| Animable | Non (transition spéciale, voir 13.4) | Oui | Oui |

`opacity: 0` est le plus piégeux : l'élément est invisible mais reste cliquable et focalisable, ce qui déroute les utilisateurs au clavier. On l'associe à `visibility: hidden` ou `pointer-events: none` si l'élément doit devenir réellement inactif.

### 8.2 La propriété `position`

`position` détermine la méthode de placement d'un élément, et active ou non les propriétés de décalage `top`, `right`, `bottom`, `left` (ou leur raccourci `inset`).

| Valeur | Comportement |
| --- | --- |
| `static` (défaut) | Flux normal ; les propriétés de décalage sont sans effet |
| `relative` | Reste dans le flux ; peut être **décalé** par rapport à sa position normale ; sert de **repère** aux enfants `absolute` |
| `absolute` | **Sorti du flux** ; positionné par rapport à l'**ancêtre positionné** le plus proche (ou à défaut le bloc conteneur initial) |
| `fixed` | Sorti du flux ; positionné par rapport à la **fenêtre** et reste visible au défilement |
| `sticky` | Hybride : `relative` jusqu'à un **seuil de défilement**, puis « collé » |

```css
.parent { position: relative; }                       /* définit le repère */
.badge {
    position: absolute;
    inset-block-start: -8px;                          /* haut */
    inset-inline-end: -8px;                           /* droite en LTR */
}

.entete { position: fixed; inset: 0 0 auto 0; }       /* top, right, left = 0, bottom = auto */

.titre-section {
    position: sticky;
    top: 0;                                           /* seuil obligatoire */
    background: white;
}

.recouvrir { position: absolute; inset: 0; }          /* remplit entièrement le parent positionné */
```

**Sortir du flux.** Un élément `absolute` ou `fixed` n'occupe plus de place pour ses voisins : ils se comportent comme s'il n'existait pas. Sa largeur par défaut s'ajuste à son contenu, et non plus à celle de son parent.

**Le repère d'un élément absolu.** C'est le plus proche ancêtre dont `position` n'est pas `static`. L'oubli classique consiste à positionner un enfant en `absolute` sans avoir donné `position: relative` à son parent : l'enfant se place alors par rapport à la page entière.

**`sticky`** nécessite au moins un seuil (`top`, `bottom`, `left` ou `right`). Il ne fonctionne pas si un **ancêtre** a `overflow: hidden`, `auto` ou `scroll` (qui devient alors le conteneur de défilement de référence), sauf si cet ancêtre est précisément le conteneur de défilement voulu. Il reste confiné dans son parent : il cesse de coller quand le parent sort de l'écran.

> `inset` est le raccourci de `top`, `right`, `bottom`, `left`, avec la même syntaxe à une à quatre valeurs que `margin`. `inset: 0` étire un élément positionné sur tout son repère.

### 8.3 Centrer un élément

Le centrage, longtemps une difficulté proverbiale du CSS, se résout aujourd'hui simplement. Le bon outil dépend de la situation.

| Besoin | Solution moderne |
| --- | --- |
| Texte centré horizontalement | `text-align: center;` |
| Bloc de largeur définie, horizontalement | `margin-inline: auto;` |
| **Centrer dans les deux axes** | `display: grid; place-items: center;` |
| Idem avec Flexbox | `display: flex; justify-content: center; align-items: center;` |
| Élément absolu avec dimensions | `position: absolute; inset: 0; margin: auto; width: ...; height: ...;` |
| Absolu (méthode classique) | `top: 50%; left: 50%; translate: -50% -50%;` |

```css
.centre { display: grid; place-items: center; min-height: 100dvh; }
```

La méthode Grid est la plus courte : `place-items` est le raccourci de `align-items` et `justify-items`. La méthode absolue avec `translate` décale l'élément de la moitié de sa propre taille pour compenser le fait que `top: 50%` place son bord haut, et non son centre, au milieu.

### 8.4 `z-index` et contextes d'empilement

Les éléments d'une page se superposent selon un ordre d'empilement sur l'axe Z. `z-index` le contrôle pour les éléments **positionnés** (`position` autre que `static`) ainsi que pour les enfants directs d'un conteneur flex ou grid.

```css
.fond    { position: relative; z-index: 1; }
.modale  { position: fixed; z-index: 1000; }
.derriere { position: relative; z-index: -1; }          /* passe derrière */
```

Sans `z-index`, l'ordre suit celui du document : le dernier élément positionné se dessine au-dessus. Un `z-index` plus grand passe au-dessus, un `z-index` négatif passe derrière le contenu du contexte courant.

#### Contextes d'empilement (*stacking contexts*)

C'est la notion qui explique la plupart des mystères du `z-index`. Un élément crée un **contexte d'empilement** lorsqu'il possède notamment : `position` (autre que `static`) avec un `z-index` autre que `auto` ; une `opacity` inférieure à 1 ; `transform`, `filter`, `perspective` ou `will-change` ; `isolation: isolate` ; `mix-blend-mode`. Les enfants d'un tel élément sont empilés **à l'intérieur** de son contexte : leur `z-index` **ne peut jamais dépasser** celui du contexte parent dans le contexte supérieur.

Conséquence : un enfant avec `z-index: 9999` peut rester sous un élément voisin de `z-index: 2`, si son parent est dans un contexte de rang inférieur. Augmenter indéfiniment les valeurs ne résout alors rien.

```css
.composant { isolation: isolate; }     /* crée un contexte sans effet visuel : évite les guerres de z-index */
```

#### Bonnes pratiques

- Définissez une **échelle** de variables : `--z-menu: 100; --z-modale: 1000; --z-toast: 1100;`.
- Isolez chaque composant avec `isolation: isolate` pour que ses `z-index` internes restent locaux.
- Pour les modales et les menus, utilisez l'élément **`<dialog>`** et l'attribut **`popover`** : ils s'affichent dans la **couche supérieure** (*top layer*) du navigateur, au-dessus de tout, sans aucun `z-index` (chapitre 28).

### 8.5 Débordement : `overflow`

Lorsqu'un contenu dépasse la taille de sa boîte, `overflow` décide de ce qui se passe.

| Valeur | Effet |
| --- | --- |
| `visible` (défaut) | Le contenu **déborde** de la boîte |
| `hidden` | Contenu **rogné**, sans barre de défilement (mais toujours défilable par programme) |
| `scroll` | Barres de défilement **toujours** affichées |
| `auto` | Barres **seulement si nécessaire** |
| `clip` | Rogné **sans** créer de conteneur de défilement |

```css
.zone-defilement { max-height: 300px; overflow-y: auto; }
.carrousel { overflow-x: auto; overscroll-behavior-x: contain; }
.rogne { overflow: hidden; border-radius: 1rem; }       /* rogne aussi aux coins arrondis */
.tableau-large { overflow-x: auto; }                    /* tableau défilant horizontalement sur mobile */
```

Si vous définissez `overflow` sur un seul axe avec une valeur autre que `visible`, l'autre axe, resté à `visible`, passe automatiquement à `auto`. `overflow-x` et `overflow-y` contrôlent chaque axe séparément. Tout `overflow` autre que `visible` et `clip` crée aussi un contexte de formatage de bloc.

#### Propriétés associées au défilement

| Propriété | Rôle |
| --- | --- |
| `overflow-x`, `overflow-y` | Contrôle par axe |
| `overscroll-behavior` | Empêche la propagation du défilement à la page (modales, panneaux) |
| `scrollbar-gutter: stable` | Réserve la place de la barre, évitant un décalage de mise en page quand elle apparaît |
| `scrollbar-width`, `scrollbar-color` | Style standard des barres de défilement |
| `scroll-behavior: smooth` | Défilement animé vers les ancres ; à désactiver si `prefers-reduced-motion` |
| `scroll-margin-top`, `scroll-padding-top` | Décalage des ancres sous un en-tête collant |
| `scroll-snap-type`, `scroll-snap-align` | **Accroche** au défilement (carrousels, galeries) |

```css
html { scroll-behavior: smooth; scroll-padding-top: 4rem; }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }

.galerie { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; gap: 1rem; }
.galerie > * { flex: 0 0 80%; scroll-snap-align: center; }
```

Pour que les liens d'ancre ne passent pas sous un en-tête fixe, `scroll-padding-top` s'applique au conteneur de défilement (généralement `html`) et `scroll-margin-top` à la cible. Avec l'accroche, `mandatory` force le défilement à se caler sur un point, tandis que `proximity` ne le fait que lorsque l'utilisateur s'arrête près d'un point.

### 8.6 Éléments remplacés : images et vidéos

Un **élément remplacé** (`<img>`, `<video>`, `<canvas>`, `<iframe>`) tire son contenu d'une ressource externe et possède des dimensions intrinsèques. Par défaut ces éléments sont de type `inline`, ce qui crée un petit espace sous l'image, dû à l'alignement sur la ligne de base du texte.

```css
img, video {
    max-width: 100%;
    height: auto;
    display: block;                           /* supprime l'espace sous l'image */
}
.vignette { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; object-position: center; }
```

`max-width: 100%` empêche l'image de dépasser son parent sans l'agrandir au-delà de sa taille naturelle ; `height: auto` conserve ses proportions. Renseigner les attributs HTML `width` et `height` sur `<img>`, en plus de ce CSS, permet au navigateur de réserver la place avant le chargement et d'éviter un saut de mise en page.

| `object-fit` | Comportement |
| --- | --- |
| `fill` | Étire l'image pour remplir la boîte (la déforme) |
| `contain` | Image entière visible, avec des marges si les proportions diffèrent |
| `cover` | Remplit la boîte en **rognant** ce qui dépasse |
| `none` | Taille d'origine, rognée si nécessaire |
| `scale-down` | Comme `none` ou `contain`, selon ce qui est le plus petit |

`object-position` choisit le point d'ancrage de l'image dans sa boîte (par exemple `top` pour garder un visage en haut d'une photo rognée).

### 8.7 Les flottants : `float` et `clear` *(héritage)*

`float` retire l'élément du flux normal et le place à gauche ou à droite de son conteneur, le texte s'enroulant autour. C'était l'outil de mise en page avant Flexbox et Grid.

```css
.image-article { float: left; margin: 0 1rem 1rem 0; shape-outside: circle(50%); }   /* habillage de texte */
.apres { clear: both; }                                                              /* se place sous les flottants */
```

`clear` (`left`, `right`, `both`) oblige un élément à se placer sous les flottants correspondants. `shape-outside` fait épouser au texte une forme (cercle, ellipse, polygone, ou la forme de l'image selon sa transparence).

> **Aujourd'hui**, `float` ne sert plus qu'à **habiller une image avec du texte**. Pour les mises en page, on utilise **Flexbox** et **Grid**. Le « clearfix » historique (`::after { content: ''; display: table; clear: both; }`) est **remplacé** par `display: flow-root` sur le parent.

### 8.8 Comparaison des méthodes de mise en page

| Besoin | Outil |
| --- | --- |
| **Une dimension** (barre de navigation, rangée de boutons, centrage) | **Flexbox** |
| **Deux dimensions** (page, galerie, tableau de bord) | **Grid** |
| Texte autour d'une image | `float` et `shape-outside` |
| Badge, infobulle, superposition | `position` ou **ancrage** (chapitre 15) |
| Colonnes de texte | `columns` |

La règle pratique : Flexbox quand le contenu dicte la disposition le long d'une ligne ou d'une colonne ; Grid quand la disposition dicte la place du contenu dans un tableau de lignes et de colonnes. On les combine souvent : Grid pour la structure globale de la page, Flexbox pour l'intérieur des composants.

### Synthèse du chapitre 8

- `display` règle le comportement extérieur et intérieur ; `flow-root` contient les flottants ; `none` retire aussi à l'accessibilité.
- `absolute` se réfère à l'ancêtre positionné ; `sticky` exige un seuil et un ancêtre sans `overflow` parasite.
- Centrer : `place-items: center` en Grid, `margin-inline: auto` pour un bloc.
- Un contexte d'empilement borne les `z-index` de ses enfants ; `isolation: isolate`, `<dialog>` et `popover` évitent les guerres de `z-index`.
- `overflow`, `scroll-snap`, `scroll-padding` gèrent le défilement ; `object-fit` gère les images.
- `float` ne sert plus qu'à habiller du texte autour d'une image.

---

## 9. Flexbox

**Objectifs d'apprentissage.** Vous saurez expliquer le modèle des deux axes, utiliser toutes les propriétés du conteneur et des éléments flex, comprendre précisément comment `flex-grow`, `flex-shrink` et `flex-basis` se combinent, réaliser les dispositions courantes (navigation, cartes, pied de page, centrage, formulaire) et éviter les pièges habituels.

### 9.1 Principe

**Flexbox** (*Flexible Box Layout*) dispose des éléments **le long d'un axe**, ligne ou colonne, en répartissant l'espace disponible et en gérant leur alignement. Son point fort est l'adaptation du contenu à un espace de taille inconnue ou variable.

```text
Axe principal (main axis)   ------------------>   (flex-direction : row)
+---------+---------+---------+ ^
|  item 1 |  item 2 |  item 3 | |  Axe secondaire (cross axis)
+---------+---------+---------+ v
```

Toute la logique de Flexbox repose sur deux axes :

- L'**axe principal** (*main axis*) est celui dans lequel les éléments se suivent. Il est défini par `flex-direction`.
- L'**axe secondaire** (*cross axis*) lui est perpendiculaire.

Ces axes sont **relatifs à la direction** : en `row`, l'axe principal est horizontal ; en `column`, il devient vertical, et `justify-content` agit alors verticalement. C'est la source de confusion la plus fréquente chez les débutants.

```css
.conteneur { display: flex; }          /* les enfants directs deviennent des éléments flex */
```

Il faut distinguer le **conteneur flex** (l'élément qui porte `display: flex`) et les **éléments flex** (ses enfants **directs** uniquement ; les petits-enfants ne sont pas concernés). `display: inline-flex` produit un conteneur qui se comporte comme un élément en ligne vis-à-vis de l'extérieur. Un élément flex est automatiquement « blockifié » : `float`, `clear` et `vertical-align` n'ont plus d'effet sur lui.

### 9.2 Propriétés du conteneur

| Propriété | Valeurs | Rôle |
| --- | --- | --- |
| `flex-direction` | `row` (défaut), `row-reverse`, `column`, `column-reverse` | Définit l'axe principal et le sens |
| `flex-wrap` | `nowrap` (défaut), `wrap`, `wrap-reverse` | Autorise le retour à la ligne |
| `flex-flow` | `row wrap` | Raccourci direction et wrap |
| `justify-content` | `flex-start`, `center`, `flex-end`, `space-between`, `space-around`, `space-evenly` | Alignement sur l'**axe principal** |
| `align-items` | `stretch` (défaut), `flex-start`, `center`, `flex-end`, `baseline` | Alignement sur l'**axe secondaire** |
| `align-content` | mêmes valeurs que `justify-content` | Répartition des **lignes** (nécessite `wrap` et plusieurs lignes) |
| **`gap`** | `1rem`, `1rem 2rem` | **Espacement** entre éléments (remplace les marges) |

```css
.barre {
    display: flex;
    justify-content: space-between;          /* logo à gauche, menu à droite */
    align-items: center;                     /* centrés verticalement */
    gap: 1rem;
    flex-wrap: wrap;
}
```

**`flex-direction`.** `row` place les éléments dans le sens de lecture, `row-reverse` les inverse, `column` les empile du haut vers le bas, `column-reverse` les empile du bas vers le haut. Les variantes inverses ne changent que l'ordre visuel, pas l'ordre du DOM ni de navigation au clavier.

**`flex-wrap`.** Par défaut (`nowrap`), tous les éléments restent sur **une seule ligne**, quitte à rétrécir ou à déborder. Avec `wrap`, ils passent à la ligne lorsque la place manque, ce qui forme plusieurs **lignes flex** indépendantes.

**`justify-content`.** Répartit l'espace libre sur l'axe principal : `flex-start` (au début), `flex-end` (à la fin), `center`, `space-between` (premier et dernier collés aux bords, espaces égaux entre les éléments), `space-around` (demi-espace aux extrémités) et `space-evenly` (espaces strictement égaux, y compris aux extrémités). Les valeurs `start` et `end`, logiques, sont aussi acceptées.

**`align-items`.** Aligne chaque élément, dans sa ligne, sur l'axe secondaire. `stretch` étire les éléments à la hauteur de la ligne (c'est pourquoi des colonnes flex ont par défaut la même hauteur), `baseline` aligne les lignes de base du texte.

**`align-content`.** Contrairement à `align-items`, elle répartit les **lignes entre elles** et ne produit un effet que s'il y a plusieurs lignes (`flex-wrap: wrap`) et un espace libre sur l'axe secondaire.

**`gap`, `row-gap`, `column-gap`.** Espace **uniquement entre** les éléments (jamais aux bords), contrairement aux marges. C'est la méthode recommandée : plus de marge parasite sur le dernier élément, plus de correctif `:last-child`.

### 9.3 Propriétés des éléments

| Propriété | Rôle |
| --- | --- |
| `flex-grow` | Part de l'espace **excédentaire** que l'élément absorbe (0 par défaut) |
| `flex-shrink` | Capacité à **rétrécir** quand l'espace manque (1 par défaut) |
| `flex-basis` | Taille **de départ** sur l'axe principal (`auto`, `200px`, `30%`) |
| **`flex`** (raccourci) | `grow shrink basis` |
| `align-self` | Alignement **individuel** sur l'axe secondaire |
| `order` | Ordre d'affichage (0 par défaut) ; n'affecte pas l'ordre de navigation au clavier ni de lecture |
| `min-width: 0` | Autorise un élément flex à **rétrécir** sous la taille de son contenu |

```css
.item { flex: 1; }                              /* = 1 1 0 : partage équitablement l'espace */
.item-fixe { flex: 0 0 200px; }                 /* ne grandit ni ne rétrécit : 200px */
.principal { flex: 1 1 20rem; }                 /* base 20rem, grandit et rétrécit */
.dernier { margin-inline-start: auto; }         /* pousse l'élément à l'extrémité */
.special { align-self: flex-end; }
```

#### Comment le navigateur calcule les tailles

Le calcul se déroule en trois temps :

1. **Taille de départ.** Chaque élément reçoit sa `flex-basis` (ou, si elle vaut `auto`, sa `width` ou la taille de son contenu).
2. **Calcul de l'espace libre.** On compare la somme des tailles de départ à la taille du conteneur. Si la somme est inférieure, il y a un **excédent** ; si elle est supérieure, il y a un **déficit**.
3. **Répartition.** L'excédent est distribué aux éléments **proportionnellement à leur `flex-grow`**. Le déficit est retiré **proportionnellement à leur `flex-shrink` pondéré par leur taille de départ**. Un élément avec `flex-grow: 0` ne grandit jamais ; un élément avec `flex-shrink: 0` ne rétrécit jamais. Les bornes `min-width` et `max-width` restent respectées et peuvent modifier la répartition.

Exemple : un conteneur de 600 px avec trois éléments de base 100 px et `flex-grow` respectifs de 1, 1 et 2 dispose de 300 px d'excédent ; ils reçoivent 75, 75 et 150 px, soit des largeurs finales de 175, 175 et 250 px.

| Raccourci | Équivaut à | Usage |
| --- | --- | --- |
| `flex: 1` | `1 1 0%` | Partage égal de l'espace |
| `flex: auto` | `1 1 auto` | Taille selon le contenu, puis s'étire |
| `flex: none` | `0 0 auto` | Taille fixe, ni grandit ni rétrécit |
| `flex: 0 1 auto` | (défaut) | Taille du contenu, peut rétrécir mais ne grandit pas |

Prenez l'habitude d'utiliser le raccourci `flex` plutôt que les trois propriétés séparément : il applique des valeurs initiales sensées (avec un seul nombre, `flex: 1` met la base à `0%`, ce qui donne un partage vraiment égal).

#### Les marges automatiques

Dans un conteneur flex, `margin: auto` absorbe **tout l'espace libre** dans sa direction. C'est un outil puissant : `margin-inline-start: auto` sur le dernier élément le pousse à l'extrémité opposée, et `margin: auto` centre un élément unique dans les deux axes.

### 9.4 Exemples courants

#### Barre de navigation

```css
.nav { display: flex; align-items: center; gap: 1.5rem; padding-inline: 1rem; }
.nav .logo { margin-inline-end: auto; }       /* pousse le reste à droite */
```

#### Cartes qui s'adaptent, sans media query

```css
.cartes { display: flex; flex-wrap: wrap; gap: 1rem; }
.carte { flex: 1 1 15rem; }                   /* au moins 15rem, partage l'espace restant */
```

Chaque carte demande au moins 15 rem ; quand la ligne est pleine, la suivante passe à la ligne et toutes les cartes de la ligne se partagent l'espace restant. Attention : la dernière ligne, incomplète, voit ses cartes s'étirer plus que celles des lignes pleines ; Grid avec `auto-fill` résout ce défaut (chapitre 10).

#### Pied de page collé en bas

```css
body { min-height: 100dvh; display: flex; flex-direction: column; }
main { flex: 1; }                              /* occupe l'espace restant, pousse le footer */
```

#### Centrage parfait

```css
.centre { display: flex; justify-content: center; align-items: center; min-height: 100dvh; }
```

#### Barre d'outils ou formulaire en ligne

```css
.recherche { display: flex; gap: .5rem; }
.recherche input { flex: 1; }
```

### 9.5 Pièges fréquents

| Problème | Solution |
| --- | --- |
| Le contenu **dépasse** de l'élément flex | `min-width: 0` (ou `overflow: hidden`) sur l'élément |
| Les éléments **s'écrasent** | `flex-wrap: wrap` ou `flex-shrink: 0` |
| `justify-content` sans effet | Vérifier `flex-direction` : l'axe principal change avec `column` |
| `margin: auto` « pousse » | C'est un outil : il absorbe tout l'espace libre |
| `order` modifie l'ordre visuel seulement | Garder un **ordre DOM logique** (accessibilité) |

Le premier piège s'explique ainsi : par défaut, un élément flex a `min-width: auto`, c'est-à-dire qu'il refuse de devenir plus petit que son contenu (un long mot, une image, un bloc de code). Pour lui permettre de rétrécir, on lui donne `min-width: 0` ; c'est la correction qu'on applique le plus souvent à un élément flex qui contient du texte ou un bloc `<pre>` débordant.

Pour l'accessibilité, rappelons que `order`, `row-reverse` et `column-reverse` ne changent que l'**affichage**. Les lecteurs d'écran et la tabulation suivent l'ordre du DOM : un décalage entre ordre visuel et ordre logique déroute les utilisateurs au clavier.

### 9.6 Flexbox ou Grid ?

Flexbox est **unidimensionnel** : il excelle pour aligner des éléments **dans une rangée ou une colonne**, et c'est le **contenu** qui dicte la disposition. Dès que vous raisonnez en **lignes et colonnes à la fois**, ou que la **structure** doit dicter la place du contenu, utilisez **Grid** (chapitre 10). Les deux se **combinent** : Grid pour la page, Flexbox pour l'intérieur des composants.

### Synthèse du chapitre 9

- Deux axes : principal (défini par `flex-direction`) et secondaire ; `justify-content` agit sur le premier, `align-items` sur le second.
- `gap` remplace les marges d'espacement ; `flex: 1` partage l'espace, `flex: none` fixe une taille.
- Le calcul distribue l'excédent selon `flex-grow` et retire le déficit selon `flex-shrink` pondéré par la taille.
- `margin: auto` absorbe l'espace libre ; `min-width: 0` résout les débordements de contenu.
- `order` et les directions inverses ne changent pas l'ordre de lecture : gardez un DOM logique.

---

## 10. CSS Grid

**Objectifs d'apprentissage.** Vous saurez maîtriser le vocabulaire de Grid (pistes, lignes, cellules, zones), définir une grille explicite et implicite, utiliser `fr`, `minmax()`, `repeat()`, `auto-fit` et `auto-fill`, placer des éléments par numéros de lignes ou par zones nommées, réaliser galeries et mises en page de page entière, et utiliser subgrid.

### 10.1 Principe et vocabulaire

**Grid** dispose des éléments dans une **grille à deux dimensions**, lignes et colonnes. Contrairement à Flexbox, on définit d'abord la **structure** (les pistes de la grille), puis on y place le contenu.

```css
.grille {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;      /* 3 colonnes : 25 %, 50 %, 25 % de l'espace */
    grid-template-rows: auto 1fr auto;
    gap: 1rem;                                /* grid-gap est l'ancien nom */
}
```

| Terme | Définition |
| --- | --- |
| **Conteneur grid** | L'élément qui porte `display: grid` |
| **Élément grid** | Un enfant direct du conteneur |
| **Piste** (*track*) | Une colonne ou une ligne de la grille |
| **Ligne** (*grid line*) | Une séparation entre pistes ; numérotée à partir de 1 (et de -1 en partant de la fin) |
| **Cellule** | Le croisement d'une ligne et d'une colonne |
| **Zone** (*area*) | Un rectangle de cellules |
| **Gouttière** (*gap*) | L'espace entre les pistes |
| **Grille explicite** | Les pistes définies par `grid-template-*` |
| **Grille implicite** | Les pistes créées automatiquement quand le contenu dépasse la grille explicite ; leur taille est réglée par `grid-auto-rows` et `grid-auto-columns` |

Une grille de 3 colonnes possède **4 lignes verticales** numérotées 1, 2, 3, 4 (et -1 pour la dernière). C'est cette numérotation qui sert au placement.

### 10.2 Propriétés du conteneur

| Propriété | Rôle |
| --- | --- |
| `grid-template-columns`, `grid-template-rows` | Définissent les **pistes** |
| `grid-template-areas` | Définit des **zones nommées** |
| `grid-template` | Raccourci pour lignes, colonnes et zones |
| `gap`, `row-gap`, `column-gap` | Gouttières |
| `grid-auto-rows`, `grid-auto-columns` | Taille des pistes **créées automatiquement** |
| `grid-auto-flow` | `row` (défaut), `column`, `dense` (comble les trous) |
| `justify-items`, `align-items`, `place-items` | Alignement du contenu **dans chaque cellule** |
| `justify-content`, `align-content`, `place-content` | Alignement **de la grille** dans son conteneur (s'il reste de la place) |

#### Unités et fonctions de Grid

```css
.grille-fixe   { display: grid; grid-template-columns: 200px 1fr 1fr; }                      /* fixe + flexibles */
.grille-egale  { display: grid; grid-template-columns: repeat(3, 1fr); }                     /* 3 colonnes égales */
.grille-auto   { display: grid; grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr)); }   /* colonnes automatiques */
.grille-minmax { display: grid; grid-template-columns: minmax(0, 1fr) auto; }
.grille-nommee { display: grid; grid-template-columns: [debut] 1fr [milieu] 2fr [fin]; }     /* lignes nommées */
```

| Valeur | Signification |
| --- | --- |
| `fr` | Fraction de l'**espace restant** après attribution des pistes de taille fixe |
| `repeat(n, taille)` | Répète un motif de pistes |
| `minmax(min, max)` | Taille comprise entre deux valeurs |
| `auto-fit` | Crée autant de colonnes que possible et **étire** les colonnes pour remplir l'espace |
| `auto-fill` | Crée autant de colonnes que possible **sans étirer** (des colonnes vides peuvent subsister) |
| `fit-content()`, `min-content`, `max-content`, `auto` | Tailles selon le contenu |

**Précisions sur `fr`.** `1fr 2fr` partage l'espace restant en trois parts : la première colonne en reçoit une, la seconde deux. Un `fr` seul a un minimum implicite égal à la taille du contenu (`auto`) : un contenu large peut donc faire déborder la colonne. La forme **`minmax(0, 1fr)`** supprime ce minimum et force des colonnes réellement égales.

**`auto-fit` et `auto-fill`.** Lorsque la grille est plus large que ce que le contenu occupe, `auto-fill` conserve les colonnes vides (les éléments gardent leur taille), alors que `auto-fit` réduit les colonnes vides à zéro et étire les colonnes occupées. Avec peu d'éléments, `auto-fit` donne donc des éléments plus larges ; avec beaucoup, les deux se comportent de la même façon.

### 10.3 Placer des éléments

Par défaut, les éléments remplissent les cellules dans l'ordre du document (placement automatique). On peut aussi les placer explicitement.

```css
.entete  { grid-column: 1 / -1; }              /* de la première à la dernière ligne : toute la largeur */
.large   { grid-column: span 2; }              /* s'étend sur 2 colonnes */
.haut    { grid-row: 1 / 3; }                  /* de la ligne 1 à la ligne 3 */
.cellule { grid-area: 2 / 1 / 3 / 3; }         /* ligne-début / colonne-début / ligne-fin / colonne-fin */
.centre  { place-self: center; }               /* align-self et justify-self */
```

`grid-column: a / b` place l'élément entre les lignes `a` et `b` (la ligne de fin est exclue). `span n` indique un nombre de pistes occupées. Les lignes négatives comptent depuis la fin de la grille **explicite**. On peut superposer des éléments en les plaçant dans les mêmes cellules, l'ordre d'empilement suivant alors `z-index`.

#### Zones nommées : une mise en page lisible

```css
.page {
    display: grid;
    grid-template-columns: 15rem 1fr;
    grid-template-rows: auto 1fr auto;
    grid-template-areas:
        'entete entete'
        'menu   contenu'
        'pied   pied';
    min-height: 100dvh;
    gap: 1rem;
}
.page > header { grid-area: entete; }
.page > nav    { grid-area: menu; }
.page > main   { grid-area: contenu; }
.page > footer { grid-area: pied; }

@media (max-width: 40rem) {                    /* sur mobile, seule la définition des zones change */
    .page {
        grid-template-columns: 1fr;
        grid-template-areas: 'entete' 'menu' 'contenu' 'pied';
    }
}
```

Le dessin du `grid-template-areas` ressemble à la page elle-même, ce qui rend le code très lisible. Chaque zone doit former un **rectangle** ; un point (`.`) désigne une cellule vide.

### 10.4 Exemples

#### Galerie responsive, sans media query

```css
.galerie {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 14rem), 1fr));
    gap: 1rem;
}
.galerie img { width: 100%; aspect-ratio: 1; object-fit: cover; }
```

La fonction `min(100%, 14rem)` évite le débordement sur un écran plus étroit que 14 rem.

#### Disposition « Saint Graal » : en-tête, trois colonnes, pied

```css
.layout { display: grid; grid-template: auto 1fr auto / 12rem 1fr 12rem; min-height: 100dvh; }
.layout > header, .layout > footer { grid-column: 1 / -1; }
```

#### Tableau de bord aux cartes de tailles variées

```css
.tableau-de-bord { display: grid; grid-template-columns: repeat(4, 1fr); grid-auto-rows: 10rem; gap: 1rem; grid-auto-flow: dense; }
.widget-large { grid-column: span 2; }
.widget-haut  { grid-row: span 2; }
```

`grid-auto-flow: dense` comble les trous en réordonnant visuellement les éléments : à utiliser avec prudence, car l'ordre visuel s'écarte alors de l'ordre du DOM.

### 10.5 Subgrid *(ajout, à jour)*

Une **grille imbriquée** peut **hériter des pistes** de sa grille parente : les contenus de plusieurs cartes s'alignent alors entre eux (titres, images et pieds de cartes à la même hauteur).

```css
.cartes { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
.carte {
    display: grid;
    grid-row: span 3;                          /* la carte occupe 3 lignes de la grille parente */
    grid-template-rows: subgrid;               /* et réutilise ces 3 lignes pour ses propres éléments */
}
```

**Subgrid** est disponible dans tous les navigateurs modernes depuis fin 2023 (Baseline *widely available*).

### 10.6 Autres fonctionnalités

- **Maçonnerie (*masonry*)** : disposition en colonnes de hauteurs inégales. Elle est **en cours de standardisation** (les propositions varient entre `display: grid-lanes` et `grid-template-rows: masonry`) : le support est à vérifier avant tout usage en production.
- **Débogage** : les DevTools affichent une **superposition de grille** avec numéros de lignes et noms de zones (chapitre 27).

### 10.7 Grid ou Flexbox ?

|  | **Flexbox** | **Grid** |
| --- | --- | --- |
| Dimensions | **1** (ligne ou colonne) | **2** (lignes et colonnes) |
| Approche | Pilotée par le **contenu** | Pilotée par la **mise en page** |
| Idéal pour | Barres, boutons, centrage, petits composants | Page entière, galeries, tableaux de bord, alignement multi-lignes |
| Alignement sur les deux axes | Un axe à la fois (par ligne) | Natif |

Ils se **combinent** : Grid pour la structure globale, Flexbox à l'intérieur des cellules.

### Synthèse du chapitre 10

- On définit les pistes (`grid-template-*`), puis on place le contenu ; `fr`, `minmax()` et `repeat()` décrivent les tailles.
- `repeat(auto-fit, minmax(...))` produit une grille responsive sans media query ; `minmax(0, 1fr)` empêche les débordements.
- Placement par lignes (`1 / -1`, `span`) ou par zones nommées (`grid-template-areas`).
- Subgrid aligne le contenu des cartes sur la grille parente.
- Flexbox pour une dimension, Grid pour deux.

---

# Partie II — CSS avancé

## 11. Arrière-plans, bordures, ombres et effets

**Objectifs d'apprentissage.** Vous saurez habiller une boîte : arrière-plans multiples, dégradés linéaires, radiaux et coniques, ombres, filtres, fusion, découpes et masques, bordures avancées, curseurs, listes et tableaux.

### 11.1 Arrière-plans

```css
.hero {
    background-color: #f0f0f0;
    background-image: url('hero.jpg');
    background-repeat: no-repeat;                /* repeat | repeat-x | repeat-y | space | round */
    background-position: center;                 /* ou 50% 20%, top right */
    background-size: cover;                      /* cover | contain | 100% auto | 200px */
    background-attachment: fixed;                /* effet de parallaxe : coûteux, désactivé sur mobile */
    background-clip: padding-box;                /* border-box | padding-box | content-box | text */
    background-origin: padding-box;
}

/* Raccourci : couleur, image, position / taille, répétition */
.bandeau { background: #222 url('motif.svg') center / cover no-repeat; }

/* Plusieurs arrière-plans : le premier est au-dessus */
.multi {
    background:
        linear-gradient(rgb(0 0 0 / .4), rgb(0 0 0 / .4)),        /* voile sombre */
        url('photo.jpg') center / cover;
}
```

`background-size: cover` agrandit l'image jusqu'à couvrir entièrement la boîte (en rognant), `contain` la réduit pour qu'elle tienne entièrement (avec des marges possibles). `background-clip` délimite la zone où le fond est peint, `background-origin` la zone par rapport à laquelle la position est calculée.

> **Astuce.** Une image **de contenu** (informative) va dans `<img>` avec un attribut `alt` ; une image **décorative** peut aller dans `background-image`.

### 11.2 Dégradés

Un dégradé est une **image générée** : on peut l'utiliser partout où une image est attendue.

```css
.degrade-direction { background: linear-gradient(to right, red, yellow); }                      /* direction */
.degrade-angle     { background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%); }          /* angle et arrêts */
.degrade-radial    { background: radial-gradient(circle at top left, white, transparent 60%); }
.degrade-conique   { background: conic-gradient(from 0deg, red, yellow, green, red); }         /* camembert, roue chromatique */
.degrade-rayures   { background: repeating-linear-gradient(45deg, #eee 0 10px, #ddd 10px 20px); }
.degrade-oklch     { background: linear-gradient(in oklch, red, blue); }                        /* interpolation perceptuelle */
```

Un dégradé est défini par une direction ou un point d'origine, et par des **arrêts de couleur** placés en pourcentage ou en longueur. Deux arrêts à la même position produisent une transition franche. `linear-gradient` suit une ligne, `radial-gradient` rayonne depuis un point, `conic-gradient` tourne autour d'un centre. Les variantes `repeating-*` répètent le motif. L'option `in oklch` interpole dans un espace perceptuel et évite les zones grises du mélange en sRGB.

### 11.3 Ombres

```css
.carte { box-shadow: 0 2px 8px rgb(0 0 0 / .15); }
/*                  x y flou  (étalement)  couleur  (inset) */

.profond { box-shadow: 0 1px 2px rgb(0 0 0 / .1), 0 8px 24px rgb(0 0 0 / .15); }   /* ombres multiples : plus naturel */
.creuse  { box-shadow: inset 0 2px 4px rgb(0 0 0 / .2); }                           /* ombre intérieure */
.anneau  { box-shadow: 0 0 0 3px royalblue; }                                        /* faux contour (suit border-radius) */

h1 { text-shadow: 1px 1px 2px #999; }
.logo { filter: drop-shadow(0 2px 4px rgb(0 0 0 / .3)); }                           /* suit la FORME (PNG, SVG transparents) */
```

`box-shadow` décale l'ombre de la boîte (x, y), la floute, l'étale (valeur facultative) et la colore ; `inset` la place à l'intérieur. Une ombre ne prend aucune place dans la mise en page. Superposer une ombre courte et une ombre longue donne un résultat plus réaliste. `drop-shadow()` (un filtre) suit la silhouette d'une image transparente alors que `box-shadow` suit toujours le rectangle.

### 11.4 Filtres, fusion et formes

```css
img    { filter: grayscale(100%) blur(2px) brightness(1.1) contrast(1.2); }
.verre { backdrop-filter: blur(10px) saturate(1.5); background: rgb(255 255 255 / .3); }   /* verre dépoli */
.melange { mix-blend-mode: multiply; }
.forme   { clip-path: polygon(50% 0, 100% 100%, 0 100%); }              /* triangle */
.cercle  { clip-path: circle(50%); }
.masque  { mask-image: linear-gradient(black, transparent); }          /* fondu */
.rond    { border-radius: 50%; aspect-ratio: 1; object-fit: cover; }
```

- **`filter`** applique des effets à l'élément : `blur`, `brightness`, `contrast`, `grayscale`, `hue-rotate`, `invert`, `opacity`, `saturate`, `sepia`, `drop-shadow`.
- **`backdrop-filter`** applique l'effet à ce qui se trouve **derrière** l'élément ; l'élément doit avoir un fond au moins partiellement transparent.
- **`mix-blend-mode`** et **`background-blend-mode`** mélangent des couches selon des modes de fusion (`multiply`, `screen`, `overlay`).
- **`clip-path`** découpe l'élément selon une forme ; **`mask-image`** le masque selon la transparence d'une image ou d'un dégradé.

Attention aux performances : `filter` et `backdrop-filter` sont coûteux sur de grandes surfaces et sur mobiles modestes.

### 11.5 Bordures avancées

```css
.degrade-bordure {
    border: 4px solid transparent;
    background: linear-gradient(white, white) padding-box, linear-gradient(90deg, red, blue) border-box;   /* bordure en dégradé */
}
.image-bordure { border: 10px solid; border-image: linear-gradient(red, blue) 1; }
.arrondi-ellipse { border-radius: 50% / 10%; }
```

La technique de la bordure en dégradé superpose deux fonds : l'un limité au `padding-box` (couleur pleine), l'autre étendu au `border-box` (dégradé visible sous la bordure transparente) ; elle conserve les coins arrondis, contrairement à `border-image`. Dans les navigateurs Chromium, `corner-shape` (coins « squircle », biseautés) est une fonctionnalité récente à support partiel.

### 11.6 Curseurs, sélection et contrôles de formulaire

```css
button { cursor: pointer; }
.desactive { cursor: not-allowed; pointer-events: none; }
.non-selectionnable { user-select: none; }
input[type='checkbox'], input[type='radio'], input[type='range'] { accent-color: royalblue; }   /* colore les contrôles natifs */
textarea { field-sizing: content; }      /* le champ s'adapte au texte (support à vérifier) */
```

`cursor` change l'apparence du pointeur ; `pointer-events: none` rend l'élément transparent aux clics (attention : il reste focalisable au clavier) ; `user-select: none` empêche la sélection de texte (à éviter sur du contenu à copier) ; `accent-color` recolore les cases, boutons radio et curseurs natifs sans les reconstruire.

### 11.7 Listes

```css
ul { list-style: none; padding: 0; }
ol { list-style-type: lower-roman; }
li::marker { color: tomato; font-weight: bold; }
ul.custom { list-style: '→ '; }                         /* puce personnalisée */
ul { list-style-position: inside; }
```

Note d'accessibilité : dans certains navigateurs, `list-style: none` retire la sémantique de liste aux lecteurs d'écran ; on peut la restaurer avec `role='list'` sur l'élément concerné si la liste est importante pour la compréhension.

### 11.8 Tableaux

```css
table { border-collapse: collapse; width: 100%; }
th, td { padding: .5rem .75rem; border-block-end: 1px solid #ddd; text-align: start; }
tbody tr:nth-child(even) { background: #f7f7f7; }
thead th { position: sticky; top: 0; background: white; }          /* en-tête collé */
.defilement { overflow-x: auto; }                                    /* conteneur pour les tableaux larges */
```

`border-collapse: collapse` fusionne les bordures des cellules adjacentes (au lieu de les séparer par `border-spacing`). Un tableau large se place dans un conteneur `overflow-x: auto` pour défiler sur mobile sans casser la page.

### Synthèse du chapitre 11

- Plusieurs arrière-plans se superposent (le premier au-dessus) ; `cover` rogne, `contain` conserve tout.
- Trois dégradés (linéaire, radial, conique) et leurs variantes répétées ; `in oklch` pour des transitions plus vives.
- `box-shadow` suit le rectangle, `drop-shadow()` suit la forme ; combinez plusieurs ombres.
- `filter`, `backdrop-filter`, `clip-path`, `mask-image` ajoutent effets et découpes, au prix de performances.
- Contrôles natifs : `accent-color` ; tableaux : `border-collapse`, en-tête `sticky`, conteneur défilant.

---

## 12. Variables CSS (propriétés personnalisées)

**Objectifs d'apprentissage.** Vous saurez définir et utiliser des variables CSS, maîtriser leur portée et leur héritage, construire des design tokens et des thèmes (dont le thème sombre), les piloter depuis JavaScript, typer et animer une variable avec `@property`, et éviter les pièges classiques.

### 12.1 Définir et utiliser

Une **propriété personnalisée** (couramment appelée variable CSS) porte un nom commençant par deux tirets, `--`. Elle se **lit** avec la fonction `var()`, **hérite** comme une propriété ordinaire, et se **calcule dans le navigateur au moment du rendu**. C'est la différence essentielle avec les variables Sass, résolues à la compilation : une variable CSS peut changer en cours d'exécution (survol, thème, JavaScript, requête de conteneur) et le style se met à jour.

```css
:root {
    --couleur-principale: #3498db;
    --espacement: 1rem;
    --rayon: .5rem;
    --police-titre: 'Georgia', serif;
}

.bouton {
    background: var(--couleur-principale);
    padding: var(--espacement) calc(var(--espacement) * 2);
    border-radius: var(--rayon);
}

p { color: var(--couleur-texte, #333); }     /* valeur de REPLI si la variable n'existe pas */
```

La **valeur de repli** (deuxième argument de `var()`) s'applique si la variable n'est pas définie ; elle peut elle-même contenir un `var()`. On déclare généralement les variables globales sur `:root`, de façon qu'elles soient disponibles dans tout le document.

### 12.2 Portée et héritage

Une variable est visible dans l'élément où elle est déclarée et **dans tous ses descendants**. On peut donc la **redéfinir localement**.

```css
:root { --texte: #222; }                                  /* globale */

.carte { --texte: white; background: #222; color: var(--texte); }   /* locale : vaut pour .carte et ses descendants */

.bouton { --fond: royalblue; background: var(--fond); }
.bouton.danger { --fond: crimson; }                      /* variante par simple redéfinition */
.bouton:hover  { --fond: color-mix(in oklch, var(--fond) 85%, black); }
```

Ce mécanisme est l'un des plus puissants de CSS : le composant ne réfléchit qu'en termes de variables, et ses variantes (couleur, taille, thème) s'obtiennent en changeant quelques variables, sans réécrire de règles.

### 12.3 Cas d'usage

| Usage | Exemple |
| --- | --- |
| **Thèmes** (clair, sombre, marque) | Redéfinir les variables sous `[data-theme='sombre']` |
| **Design tokens** | Couleurs, espacements, rayons, ombres, échelles typographiques |
| **Composants configurables** | `.avatar { --taille: 3rem; width: var(--taille); }` |
| **Valeurs dynamiques depuis JavaScript** | `element.style.setProperty('--x', valeur)` |
| **Calculs** | `calc(var(--n) * 1rem)` |
| **Éviter la répétition** | Une valeur, un seul endroit |

Les **design tokens** sont les valeurs de base d'un système de design, nommées une fois pour toutes :

```css
:root {
    /* Échelle d'espacement */
    --esp-1: .25rem; --esp-2: .5rem; --esp-3: 1rem; --esp-4: 1.5rem; --esp-5: 3rem;
    /* Typographie fluide */
    --texte-m: clamp(1rem, .95rem + .25vw, 1.125rem);
}
```

### 12.4 Thème sombre *(à jour)*

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

/* 3. Respecter un choix manuel de l'utilisateur (bouton de bascule) */
:root[data-theme='clair']  { color-scheme: light; }
:root[data-theme='sombre'] { color-scheme: dark; }
```

`color-scheme` indique au navigateur les thèmes pris en charge : il adapte alors les **contrôles natifs** (barres de défilement, champs de formulaire, fonds par défaut). `light-dark(a, b)` choisit `a` en thème clair et `b` en thème sombre, selon la valeur courante de `color-scheme`. L'approche classique reste valide :

```css
@media (prefers-color-scheme: dark) { :root { --fond: #121212; --texte: #eee; } }
```

Pour un thème sombre réussi, on ne se contente pas d'inverser les couleurs : on réduit la saturation, on évite le noir pur et le blanc pur, on vérifie les contrastes dans les deux thèmes.

### 12.5 Basculer avec JavaScript

```js
document.documentElement.dataset.theme = 'sombre';                                   // change le thème
document.documentElement.style.setProperty('--couleur-principale', 'tomato');        // modifie une variable

const espacement = getComputedStyle(document.documentElement).getPropertyValue('--espacement');
console.log(espacement.trim());                                                      // '1rem' (valeur déclarée dans :root)
```

`style.setProperty` écrit une variable sur un élément ; `getComputedStyle(...).getPropertyValue` la lit (la valeur est renvoyée sous forme de texte, avec d'éventuels espaces à retirer par `trim()`). C'est le moyen idéal de transmettre une donnée dynamique (position de la souris, progression) au CSS.

### 12.6 Propriétés enregistrées : `@property` *(ajout)*

Par défaut, une variable est une simple chaîne de texte, que le navigateur ne comprend pas. `@property` la **type** : on déclare sa syntaxe, son héritage et sa valeur initiale. Surtout, cela permet d'**animer** une variable, ce qui est impossible autrement (le navigateur ne sait pas interpoler du texte).

```css
@property --angle {
    syntax: '<angle>';                      /* <color> | <length> | <number> | <percentage> | <integer> … */
    inherits: false;
    initial-value: 0deg;
}

.roue {
    width: 10rem;
    aspect-ratio: 1;
    border-radius: 50%;
    background: conic-gradient(from var(--angle), red, yellow, red);
    animation: tourner-angle 4s linear infinite;
}
@keyframes tourner-angle { to { --angle: 360deg; } }       /* animation d'un dégradé */
```

`@property` est Baseline *widely available* depuis 2024.

### 12.7 Pièges

| Problème | Explication |
| --- | --- |
| Valeur invalide sans erreur visible | Une variable invalide rend la propriété « invalide au moment du calcul » (elle retombe sur `unset`) : vérifier dans les DevTools |
| Inutilisable dans les **requêtes média** | `@media (min-width: var(--x))` est invalide ; utilisez des requêtes de **conteneur** ou des valeurs fixes |
| Noms **sensibles à la casse** | `--Couleur` et `--couleur` sont distinctes |
| Variables et `calc()` | Préciser l'**unité** : `calc(var(--n) * 1px)` si `--n` est un nombre |

### Synthèse du chapitre 12

- Les variables CSS se calculent à l'exécution, se transmettent par héritage et se redéfinissent localement.
- Design tokens et thèmes : on change des variables, pas des règles.
- `color-scheme` et `light-dark()` simplifient le thème sombre.
- `@property` type les variables et permet de les animer.

---

## 13. Transitions, animations et transformations

**Objectifs d'apprentissage.** Vous saurez créer des transitions et des animations par images clés, transformer des éléments en 2D et 3D, animer l'apparition et la disparition d'un élément, choisir les propriétés performantes, respecter le mouvement réduit, utiliser les animations pilotées par le défilement et les transitions de vue.

### 13.1 Transitions

Une **transition** anime le **passage** d'une valeur à une autre lorsque celle-ci change (survol, focus, ajout d'une classe). Elle se déclare sur l'état de **départ et d'arrivée** : le navigateur calcule tous les états intermédiaires.

```css
.bouton {
    background: royalblue;
    transition: background-color .3s ease, transform .2s ease-out;
    /*          propriété         durée fonction  (délai) */
}
.bouton:hover { background: navy; transform: translateY(-2px); }
```

| Propriété | Rôle |
| --- | --- |
| `transition-property` | Propriétés animées (évitez `all` : listez-les) |
| `transition-duration` | Durée (`.3s`, `300ms`) |
| `transition-timing-function` | `ease`, `linear`, `ease-in`, `ease-out`, `ease-in-out`, `cubic-bezier(…)`, `steps()`, `linear(…)` (courbes à points : ressorts, rebonds) |
| `transition-delay` | Délai avant le départ |
| `transition-behavior` | `allow-discrete` : permet de faire transitionner `display`, `overlay`… (voir 13.4) |

```css
.ressort { transition: transform .6s linear(0, .6 18%, 1.05 36%, .98 54%, 1 72%, 1); }   /* accélération en ressort */
```

La **fonction de temporisation** décrit la vitesse au cours du temps : `linear` est constante, `ease-out` démarre vite et ralentit (naturel pour une apparition), `ease-in` fait l'inverse. Une transition ne fonctionne que sur des propriétés **interpolables** (nombres, longueurs, couleurs, transformations) ; elle est déclarée sur l'élément lui-même, généralement dans son état de base, de façon à s'appliquer dans les deux sens.

### 13.2 Animations par images clés : `@keyframes`

Une **animation** va plus loin qu'une transition : elle peut comporter **plusieurs étapes**, démarrer seule, se répéter et alterner.

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

| Propriété | Valeurs |
| --- | --- |
| `animation-name` | Nom du `@keyframes` |
| `animation-duration` | `1s`, `300ms` |
| `animation-timing-function` | Comme pour les transitions |
| `animation-delay` | Délai (négatif : démarre « en cours ») |
| `animation-iteration-count` | `1`, `3`, `infinite` |
| `animation-direction` | `normal`, `reverse`, `alternate`, `alternate-reverse` |
| `animation-fill-mode` | `none`, `forwards` (garde l'état final), `backwards` (applique l'état initial pendant le délai), `both` |
| `animation-play-state` | `running`, `paused` |
| `animation-composition` | `replace`, `add`, `accumulate` |
| `animation-timeline` | `auto`, `scroll()`, `view()` (voir 13.7) |
| **`animation`** (raccourci) | `nom durée fonction délai répétition direction remplissage` |

```css
.chargement { animation: tourner 1s linear infinite; }
@keyframes tourner { to { transform: rotate(1turn); } }
```

Sans `animation-fill-mode: both`, l'élément retourne à son état de base à la fin de l'animation (un élément qui apparaissait en fondu disparaîtrait de nouveau). Une animation sans `to` ou `from` explicite part de l'état courant de l'élément.

### 13.3 Transformations

Les transformations déplacent, tournent, redimensionnent ou inclinent un élément **sans modifier la mise en page** : les voisins ne bougent pas, l'espace d'origine reste réservé.

```css
.element {
    transform: translate(20px, 10px) rotate(15deg) scale(1.2) skew(10deg);   /* l'ordre compte */
    transform-origin: top left;                                               /* point d'ancrage (centre par défaut) */
}

/* Propriétés de transformation INDIVIDUELLES : plus simples à animer séparément */
.moderne { translate: 20px 10px; rotate: 15deg; scale: 1.2; }
.moderne:hover { scale: 1.3; }
```

| Fonction | Rôle |
| --- | --- |
| `translate(x, y)`, `translateX()`, `translateY()`, `translateZ()` | Déplacer |
| `rotate(angle)` (`rotateX`, `rotateY`, `rotateZ`) | Pivoter |
| `scale(x, y)` | Redimensionner |
| `skew(x, y)` | Incliner |
| `matrix()`, `matrix3d()` | Combinaison complète |

**L'ordre des fonctions est significatif** : elles se composent de droite à gauche dans le repère de l'élément, donc `translate` puis `rotate` ne donne pas le même résultat que `rotate` puis `translate`. Les propriétés individuelles `translate`, `rotate` et `scale` s'appliquent dans un ordre fixe et peuvent être animées indépendamment, ce qui évite de réécrire toute la liste `transform`.

#### Transformations 3D

```css
.scene { perspective: 800px; }                                /* profondeur, sur le PARENT */
.carte3d { transform-style: preserve-3d; transition: transform .6s; }
.carte3d:hover { transform: rotateY(180deg); }
.face { backface-visibility: hidden; }                       /* masque le dos de la face */
```

`perspective` (sur le parent) donne l'effet de profondeur ; `transform-style: preserve-3d` fait que les enfants gardent leur position dans l'espace 3D ; `backface-visibility: hidden` masque la face arrière, pour réaliser par exemple une carte retournable avec une face avant et une face arrière.

### 13.4 Animer l'apparition et la disparition *(ajout, à jour)*

Jusqu'à récemment, animer un élément qui passe de `display: none` à visible exigeait du JavaScript, car `display` n'est pas interpolable et l'élément n'a pas d'état de départ au moment de son insertion. Deux outils résolvent ce problème.

```css
.panneau {
    opacity: 1;
    transform: none;
    transition: opacity .3s, transform .3s, display .3s allow-discrete;   /* display devient « animable » (discret) */

    @starting-style {                                                      /* état de DÉPART à l'apparition */
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

- **`@starting-style`** définit les valeurs **initiales** d'un élément qui vient d'être inséré ou affiché (Baseline *newly available*).
- **`transition-behavior: allow-discrete`** autorise la transition des propriétés **discrètes** comme `display` et `overlay` : la valeur bascule au début ou à la fin de la durée, de sorte que l'élément reste affiché pendant l'animation de sortie.
- Ce mécanisme s'applique aux `<dialog>` et aux éléments `popover` (chapitre 28).

#### Animer vers `height: auto` *(support récent)*

```css
:root { interpolate-size: allow-keywords; }       /* permet de transitionner vers height: auto */
.accordeon { height: 0; overflow: clip; transition: height .3s; }
.accordeon.ouvert { height: auto; }
```

Animer vers `auto` (ou `min-content`, `max-content`) n'était pas possible en CSS ; `interpolate-size` l'autorise dans les navigateurs qui le prennent en charge. Vérifiez le support, et prévoyez un comportement acceptable sans animation.

### 13.5 Performance des animations

Rappel du pipeline (chapitre 1) : modifier la géométrie recalcule la mise en page, ce qui est coûteux ; `transform` et `opacity` peuvent être gérés par la composition sur le processeur graphique.

| Bon (composition) | Mauvais (déclenche la mise en page) |
| --- | --- |
| `transform` (`translate`, `rotate`, `scale`) | `width`, `height`, `margin`, `top`, `left` |
| `opacity` | `box-shadow` (repeinture) animé à grande échelle |
| `filter` (avec prudence) |  |

```css
.mobile { will-change: transform; }     /* à utiliser avec parcimonie, pour des éléments qui vont vraiment s'animer */
```

- Animez de préférence `transform` et `opacity`.
- Évitez `transition: all` : listez les propriétés.
- Limitez le nombre d'éléments animés simultanément.
- `will-change` réserve des ressources mémoire : ne l'appliquez pas partout et retirez-le après l'animation si possible.

### 13.6 Respecter les préférences : mouvement réduit *(ajout)*

```css
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: .01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: .01ms !important;
        scroll-behavior: auto !important;
    }
}

/* Ou, plus fin : n'activer les animations que pour ceux qui les acceptent */
@media (prefers-reduced-motion: no-preference) {
    .carte { animation: apparition .5s ease-out both; }
}
```

> **Accessibilité.** Les animations de **mouvement** (translation, zoom, parallaxe) peuvent provoquer des malaises (troubles vestibulaires). Respectez toujours cette préférence : on réduit ou supprime le mouvement, on conserve les changements d'opacité ou de couleur qui transmettent l'information.

### 13.7 Animations liées au défilement *(ajout)*

Les **animations pilotées par le défilement** (*scroll-driven animations*) lient la **progression** d'une animation à la **position de défilement** ou à la **visibilité** d'un élément, **sans JavaScript**.

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

`scroll()` lie l'animation à la progression du défilement d'un conteneur ; `view()` la lie à la progression de visibilité de l'élément lui-même ; `animation-range` choisit la portion utile (`entry`, `exit`, `cover`, `contain`).

> **Support et amélioration progressive.** Pris en charge dans Chromium et Safari ; vérifier pour Firefox selon la version. Entourez ces règles de `@supports (animation-timeline: scroll())` et prévoyez un état final lisible sans animation.

### 13.8 Transitions de vue (*View Transitions*) *(ajout)*

Elles produisent des animations fluides **entre deux états de page** (changement de contenu, navigation) avec très peu de code : le navigateur prend une capture de l'ancien état, applique la modification, puis anime de l'ancien vers le nouveau.

```js
function mettreAJourLeDOM() {
    document.querySelector('.vignette').classList.toggle('agrandie');
}

if (document.startViewTransition) {
    document.startViewTransition(() => mettreAJourLeDOM());     // même document
} else {
    mettreAJourLeDOM();                                         // repli : changement sans animation
}
```

```css
::view-transition-old(root) { animation: .3s ease-out both fondu-sortie; }
::view-transition-new(root) { animation: .3s ease-in both fondu-entree; }

.vignette { view-transition-name: image-produit; }          /* l'élément « voyage » entre les deux états */

@keyframes fondu-sortie { to { opacity: 0; } }
@keyframes fondu-entree { from { opacity: 0; } }

@view-transition { navigation: auto; }                       /* navigations entre pages d'un même site */
```

Par défaut, la transition est un fondu enchaîné de la page entière ; les pseudo-éléments `::view-transition-old()` et `::view-transition-new()` permettent de la personnaliser, et `view-transition-name` isole un élément pour qu'il se déplace et se redimensionne entre les deux états. Les transitions **dans un même document** sont Baseline depuis 2025 ; celles **entre documents** (`@view-transition`) voient leur support s'étendre : gardez toujours un repli sans animation.

### Synthèse du chapitre 13

- Transition : d'un état à un autre ; animation : plusieurs étapes, autonome, répétable.
- Les transformations n'altèrent pas la mise en page ; leur ordre est significatif.
- `@starting-style` et `allow-discrete` rendent possibles les apparitions et disparitions animées.
- Animez `transform` et `opacity` ; respectez `prefers-reduced-motion`.
- Défilement et vues : `animation-timeline` et View Transitions, avec repli si non supportés.

---

## 14. Design responsive

**Objectifs d'apprentissage.** Vous saurez appliquer les principes du design responsive, configurer la balise viewport, écrire des requêtes média (y compris la syntaxe d'intervalle et les requêtes de préférences), choisir des points de rupture, utiliser les requêtes de conteneur, construire des mises en page fluides, servir des images adaptées et tester vos pages.

### 14.1 Principes

Le **design responsive** adapte une page à toutes les tailles d'écran **avec le même code**, au lieu de maintenir une version mobile et une version bureau distinctes. Il repose sur quatre piliers :

1. **Une mise en page fluide** : pourcentages, `fr`, `minmax()`, `clamp()` plutôt que des largeurs fixes.
2. **Des images et des médias flexibles** qui s'adaptent à leur conteneur.
3. **Des requêtes média** (selon l'appareil et ses préférences) et **des requêtes de conteneur** (selon l'espace réellement alloué à un composant).
4. **L'approche mobile d'abord** (*mobile-first*) : on écrit d'abord les styles de base pour les petits écrans, puis on les enrichit pour les grands.

### 14.2 La balise `viewport`

```html
<meta name='viewport' content='width=device-width, initial-scale=1'>
```

Sans cette balise, les navigateurs mobiles supposent une page conçue pour un écran de bureau et la réduisent pour la faire tenir (« dézoomée »), ce qui annule le travail responsive. `width=device-width` aligne la largeur de la page sur celle de l'appareil, `initial-scale=1` fixe le zoom initial à 100 %. **Ne désactivez pas le zoom** (`user-scalable=no`, `maximum-scale=1`) : c'est un obstacle d'accessibilité pour les personnes malvoyantes.

### 14.3 Requêtes média (*media queries*)

Une requête média applique un bloc de règles **seulement si** une condition portant sur l'appareil ou le contexte est vraie.

```css
/* Mobile d'abord : styles de base pour les petits écrans */
.conteneur { padding: 1rem; }

/* Puis on ENRICHIT avec min-width */
@media (min-width: 48rem) {                        /* ≥ 768 px */
    .conteneur { padding: 2rem; display: grid; grid-template-columns: 1fr 2fr; }
}
@media (min-width: 64rem) {                        /* ≥ 1024 px */
    .conteneur { max-width: 70rem; margin-inline: auto; }
}
```

Avec l'approche mobile d'abord, les styles sans requête ciblent le plus petit écran et `min-width` ajoute de la complexité pour les écrans plus grands. Elle est généralement plus légère et plus simple à maintenir que l'approche inverse (`max-width`).

#### Syntaxe d'intervalle *(à jour)*

```css
@media (width >= 48rem) { }                        /* équivaut à (min-width: 48rem) */
@media (width < 40rem) { }
@media (40rem <= width <= 64rem) { }
@media (400px <= width <= 700px) { }
```

Les opérateurs de comparaison (`<`, `<=`, `>`, `>=`, `=`) rendent les intervalles plus lisibles que le couple `min-width` et `max-width`, et évitent les erreurs d'un pixel entre deux requêtes consécutives.

#### Types de requêtes

| Critère | Exemple |
| --- | --- |
| Taille | `width`, `height`, `aspect-ratio`, `orientation: landscape` |
| Support | `screen`, `print` |
| **Préférences** | `prefers-color-scheme: dark`, `prefers-reduced-motion: reduce`, `prefers-contrast: more`, `prefers-reduced-transparency`, `forced-colors: active` |
| **Capacités** | `hover: hover`, `pointer: coarse` (tactile), `any-hover` |
| Résolution | `resolution >= 2dppx` (écrans haute densité) |

```css
@media (hover: hover) { .lien:hover { text-decoration: underline; } }       /* survol seulement si l'appareil le permet */
@media (pointer: coarse) { .bouton { min-height: 3rem; } }                   /* cibles tactiles plus grandes */
@media print { nav, footer { display: none; } a::after { content: ' (' attr(href) ')'; } }
```

Les requêtes de **préférences** sont l'une des applications les plus importantes : elles adaptent la page aux besoins de l'utilisateur (thème sombre, réduction des animations, contraste renforcé, couleurs forcées). Les requêtes de **capacités** distinguent les appareils tactiles des appareils à pointeur précis. Le style d'**impression** (`@media print`) masque la navigation et peut afficher l'adresse des liens.

Les requêtes se combinent avec `and`, `or` (ou la virgule) et `not` : `@media screen and (min-width: 48rem) and (orientation: landscape)`.

### 14.4 Points de rupture (*breakpoints*)

| Taille | Largeur indicative | Appareil |
| --- | --- | --- |
| Petit | moins de 40 rem (640 px) | Téléphones |
| Moyen | ≥ 48 rem (768 px) | Tablettes |
| Grand | ≥ 64 rem (1024 px) | Portables |
| Très grand | ≥ 80 rem (1280 px) | Bureau |

> **Choisissez vos points de rupture selon votre contenu**, c'est-à-dire là où la mise en page « casse », et non selon des appareils précis, dont les tailles changent sans cesse. Exprimez-les en **`rem` ou `em`**, de façon qu'ils suivent le zoom du texte.

La démarche pratique : réduisez progressivement la fenêtre du navigateur ; là où la mise en page devient inconfortable (lignes trop longues, colonnes trop étroites), placez un point de rupture. Moins il y en a, plus le CSS est simple.

### 14.5 Requêtes de conteneur : `@container` *(ajout, à jour)*

Les requêtes média observent la **fenêtre**. Or un composant réutilisable (une carte) peut se trouver dans une barre latérale étroite ou dans la zone principale, pour une même largeur de fenêtre. Les **requêtes de conteneur** adaptent le composant à la taille de **son conteneur**.

```css
.carte-conteneur { container-type: inline-size; container-name: carte; }   /* déclare un conteneur */

.carte { display: grid; gap: 1rem; }

@container carte (min-width: 30rem) {                        /* selon la largeur du conteneur */
    .carte { grid-template-columns: 10rem 1fr; }
}
@container (width < 20rem) { .carte img { display: none; } }

.titre { font-size: clamp(1rem, 4cqi, 1.75rem); }           /* cqi = 1 % de la largeur du conteneur */
```

| Élément | Rôle |
| --- | --- |
| `container-type: inline-size` | Conteneur de **taille** sur l'axe en ligne (largeur) ; `size` : les deux axes ; `normal` : pour les requêtes de style |
| `container-name` | Nom (facultatif) |
| `container: carte / inline-size` | Raccourci |
| `@container (…)` | Requête de taille |
| `cqw`, `cqh`, `cqi`, `cqb`, `cqmin`, `cqmax` | Unités relatives au conteneur |
| `@container style(--theme: sombre)` | Requêtes de **style** sur les variables (support en progression) |
| `@container scroll-state(stuck: top)` | Requêtes sur l'**état de défilement** (collé, accroché ; Chromium) |

Un point important : un élément ne peut pas être son propre conteneur de requête ; la règle `@container` s'applique aux **descendants** de l'élément déclaré conteneur. Le conteneur doit aussi avoir une taille indépendante de son contenu (d'où le rôle de `inline-size`).

> Les requêtes de taille de conteneur sont Baseline *widely available* depuis 2023. **Media queries** pour la **mise en page globale**, **container queries** pour les **composants**.

### 14.6 Unités et mises en page fluides

```css
.conteneur { width: min(100% - 2rem, 70rem); margin-inline: auto; }     /* largeur max, marges latérales automatiques */
.grille { grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr)); }   /* aucune media query */
h1 { font-size: clamp(2rem, 1rem + 4vw, 4rem); }                       /* typographie fluide */
.section { padding-block: clamp(2rem, 6vw, 6rem); }
```

Ces techniques rendent la page adaptable **de façon continue**, sans seuil : un espacement ou une taille de police varient progressivement avec l'écran.

### 14.7 Images et vidéos responsives

```html
<!-- Choisir la bonne taille selon l'écran -->
<img src='image-800.jpg'
     srcset='image-400.jpg 400w, image-800.jpg 800w, image-1600.jpg 1600w'
     sizes='(min-width: 60rem) 50vw, 100vw'
     alt='Description' width='800' height='600' loading='lazy' decoding='async'>

<!-- Direction artistique et formats modernes -->
<picture>
    <source media='(min-width: 60rem)' srcset='large.avif' type='image/avif'>
    <source srcset='petit.webp' type='image/webp'>
    <img src='petit.jpg' alt='Description' width='400' height='300'>
</picture>
```

```css
img, video, svg { max-width: 100%; height: auto; }
.video { aspect-ratio: 16 / 9; width: 100%; }
.fond { background-image: image-set(url('fond.avif') type('image/avif'), url('fond.jpg') type('image/jpeg')); }
```

- **`srcset`** avec des largeurs (`400w`) liste les versions disponibles ; **`sizes`** indique la largeur d'affichage prévue ; le navigateur choisit la meilleure source selon la taille et la densité de l'écran.
- **`<picture>`** permet la **direction artistique** (un recadrage différent selon l'écran) et le choix du **format** (AVIF, WebP, avec repli JPEG).
- **`image-set()`** fait la même chose pour les images de fond CSS.

> **Astuce.** Renseignez toujours **`width` et `height`** (ou `aspect-ratio`) sur les images : le navigateur réserve la place avant le chargement et évite les **décalages de mise en page** (CLS). Utilisez `loading='lazy'` pour les images hors de l'écran initial, mais jamais pour l'image principale visible dès le chargement.

### 14.8 Tableaux et grilles sur mobile

```css
.tableau { overflow-x: auto; }                           /* défilement horizontal */
.menu { display: flex; flex-wrap: wrap; gap: .5rem; }
```

### 14.9 Tester

- Utilisez le **mode appareil** des DevTools (Ctrl+Maj+M), redimensionnez la fenêtre, testez le zoom à **200 %** et une **taille de police augmentée**.
- Testez sur de **vrais appareils** (Safari sur iOS, Chrome sur Android) : les simulateurs ne reproduisent pas tout (barres d'adresse, clavier virtuel, performances).
- Vérifiez le **portrait et le paysage**, le **tactile**, le **mode sombre** et le **mouvement réduit**.

### Synthèse du chapitre 14

- Mobile d'abord, `min-width` (ou syntaxe d'intervalle), points de rupture dictés par le contenu et exprimés en `rem`.
- Les requêtes de préférences et de capacités adaptent la page à l'utilisateur et à son appareil.
- `@container` pour les composants, `@media` pour la structure globale.
- `min()`, `clamp()`, `auto-fit` : la fluidité avant les seuils.
- `srcset`, `sizes`, `<picture>`, `width` et `height` pour des images rapides et stables.

---

## 15. Fonctionnalités modernes

*Le CSS a beaucoup évolué depuis 2022. Chaque fonctionnalité est déjà détaillée dans le chapitre thématique correspondant ; ce chapitre en donne une vue d'ensemble et présente celles qui n'ont pas encore été abordées.*

**Objectifs d'apprentissage.** Vous saurez situer l'état de disponibilité des principales nouveautés, utiliser le positionnement par ancrage, `sibling-index()` et `sibling-count()`, connaître les fonctionnalités expérimentales (conditions, fonctions) et choisir l'outil moderne adapté à chaque besoin.

### 15.1 Tableau de synthèse

| Fonctionnalité | Rôle | Statut approximatif (fin 2026) |
| --- | --- | --- |
| **Imbrication** (`&`) | Imbriquer les règles sans préprocesseur | Largement disponible |
| **`:has()`** | Sélecteur « parent » | Largement disponible |
| **`@layer`** | Couches de cascade | Largement disponible |
| **Requêtes de conteneur** (taille) | Composants adaptatifs | Largement disponible |
| **Subgrid** | Grilles imbriquées alignées | Largement disponible |
| **Propriétés logiques** | Sens d'écriture | Largement disponible |
| `color-mix()`, `oklch()`, couleur relative | Couleurs modernes | Largement ou récemment disponible |
| `light-dark()` | Valeur selon le thème | Disponible |
| `text-wrap: balance` et `pretty` | Typographie | Disponible |
| `@starting-style`, `transition-behavior` | Animer `display` | Disponible (récent) |
| `@property` | Variables typées et animables | Disponible |
| **Transitions de vue** (même document) | Animations d'interface | Disponible |
| **`@scope`** | Portée des styles | Récemment disponible (2026) |
| **Positionnement par ancrage** | Infobulles, menus sans JavaScript | Récemment disponible (début 2026, noyau) |
| `sibling-index()`, `sibling-count()` | Mise en page selon la position | Récemment disponible |
| **Animations liées au défilement** | Animations sans JavaScript | Selon les navigateurs (à vérifier) |
| `if()`, `@function`, mixins CSS | Logique conditionnelle, fonctions | Expérimental (Chromium) |
| `field-sizing`, `interpolate-size`, `corner-shape`, `contrast-color()`, `shape()` | Divers | Support partiel ou récent |
| `masonry`, décorations de gouttières, `reading-flow` | Mises en page avancées | En cours de standardisation |

Ce tableau est indicatif : le support évolue vite. Avant d'utiliser une fonctionnalité non « largement disponible », consultez MDN, caniuse.com ou Baseline, et prévoyez un repli.

### 15.2 Positionnement par ancrage (*Anchor Positioning*)

Il permet d'attacher un élément flottant (infobulle, menu, popover) à un **autre élément**, **en CSS pur**, avec gestion automatique des **débordements** de la fenêtre.

```css
.bouton-menu { anchor-name: --menu; }

.menu {
    position: fixed;                                   /* ou absolute */
    position-anchor: --menu;                           /* lié à l'ancre */
    position-area: bottom span-right;                  /* placé sous l'ancre */
    margin-top: .25rem;
    position-try-fallbacks: flip-block, flip-inline;   /* se retourne s'il n'y a pas de place */
}
```

- **`anchor-name`** donne un nom à l'élément qui sert d'ancre.
- **`position-anchor`** relie l'élément positionné à cette ancre.
- **`position-area`** choisit la zone, autour de l'ancre, où placer l'élément (une grille de neuf cases centrée sur l'ancre).
- **`anchor()`** (fonction) permet de se caler sur un bord précis de l'ancre dans `top`, `left`, `inset`, etc.
- **`position-try-fallbacks`** propose des positions de repli si l'élément déborde de la fenêtre.

Combiné à l'attribut HTML **`popover`** (chapitre 28), le positionnement par ancrage remplace, dans beaucoup de cas, des bibliothèques comme Floating UI ou Popper.js. Le **noyau** (`anchor-name`, `position-anchor`, `position-area`, `anchor()`) est Baseline *newly available* depuis janvier 2026 ; les fonctionnalités annexes (`anchor-scope`, certaines options de `position-try`) peuvent varier : vérifiez et prévoyez un repli.

### 15.3 `sibling-index()` et `sibling-count()`

Ces fonctions retournent respectivement le **rang** (à partir de 1) d'un élément parmi ses frères et le **nombre total** de frères. Elles évitent d'écrire à la main des variables `--i` sur chaque élément.

```css
.liste > li {
    --i: sibling-index();                               /* 1, 2, 3… */
    transition-delay: calc(var(--i) * 50ms);            /* apparitions en cascade */
}
.liste > li { rotate: calc((sibling-index() - 1) * 360deg / sibling-count()); }   /* disposition en cercle */
```

### 15.4 Conditions, fonctions et mixins *(expérimental)*

```css
/* if() : valeur conditionnelle (support actuel : Chromium) */
.bouton { padding: if(media(width >= 48rem): 1.5rem; else: 1rem); }

/* @function : fonctions CSS personnalisées (Chromium) */
@function --double(--x) { result: calc(var(--x) * 2); }
.boite { width: --double(10px); }
```

> N'utilisez ces fonctionnalités que derrière `@supports` ou comme **amélioration progressive** : leur syntaxe peut encore évoluer. Elles visent à terme à réduire le besoin de préprocesseurs pour la logique conditionnelle et la réutilisation de calculs.

### 15.5 Quand utiliser quoi

| Besoin | Fonctionnalité moderne | Remplace |
| --- | --- | --- |
| Styler un parent selon ses enfants | `:has()` | JavaScript |
| Imbriquer | Imbrication native | Sass (imbrication) |
| Contrôler l'ordre de priorité | `@layer` | `!important`, spécificité |
| Composant adaptatif | `@container` | Media queries et astuces |
| Aligner des contenus de cartes | `subgrid` | Hauteurs fixes, JavaScript |
| Thème clair ou sombre | `light-dark()` et `color-scheme` | Doublons de variables |
| Infobulle ou menu positionné | Ancrage et `popover` | Floating UI, Popper.js |
| Animer l'apparition | `@starting-style` | JavaScript avec `requestAnimationFrame` |
| Animation au défilement | `animation-timeline` | IntersectionObserver, bibliothèques |
| Couleurs dérivées | `color-mix()`, couleur relative | Sass `lighten()` et `darken()` |
| Texte équilibré | `text-wrap: balance` | Balises `<br>` manuelles |

### Synthèse du chapitre 15

- La plupart des fonctionnalités modernes (`:has()`, `@layer`, `@container`, subgrid, imbrication) sont désormais largement disponibles et remplaçables aux anciennes solutions.
- L'ancrage, `@scope` et `sibling-index()` sont récents : vérifiez le support.
- `if()`, `@function` et les mixins restent expérimentaux : usage derrière `@supports` seulement.

---

## 16. Accessibilité et CSS

*Le CSS a un impact direct sur l'accessibilité : il peut la renforcer ou la détruire. Ce chapitre rassemble les règles essentielles.*

**Objectifs d'apprentissage.** Vous saurez garantir un contraste suffisant, conserver un focus visible, dimensionner les cibles tactiles, masquer un contenu correctement, respecter les préférences système de l'utilisateur, éviter les pièges d'ordre de lecture et vérifier vos pages avec une liste de contrôle.

### 16.1 Contraste et couleur

Les **WCAG** (*Web Content Accessibility Guidelines*) fixent des seuils mesurables. Au niveau **AA**, le plus couramment exigé :

- Le texte normal doit avoir un rapport de contraste d'au moins **4,5 pour 1** avec son fond.
- Le grand texte (au moins 24 px, ou 18,66 px en gras) et les composants d'interface (bordures de champs, icônes porteuses de sens) doivent atteindre **3 pour 1**.
- Une information ne doit **jamais** être transmise par la **seule couleur** : ajoutez une icône, un texte, un motif ou un soulignement (par exemple, signalez un champ en erreur par un message et pas seulement par une bordure rouge).
- Testez avec l'outil de contraste des DevTools et en **niveaux de gris** : si l'interface reste compréhensible, elle ne dépend pas de la couleur.

```css
@media (prefers-contrast: more) { :root { --bordure: 2px solid currentColor; } }
@media (forced-colors: active) {                       /* mode Contraste élevé de Windows */
    .bouton { border: 1px solid ButtonText; }
}
```

En mode `forced-colors`, le système remplace vos couleurs par une palette imposée : les fonds et les ombres disparaissent, d'où l'importance de conserver des **bordures réelles** sur les boutons et les champs, et d'utiliser les **mots-clés système** (`ButtonText`, `Canvas`, `LinkText`).

### 16.2 Focus visible

```css
:focus-visible {
    outline: 3px solid var(--accent, royalblue);
    outline-offset: 3px;
}
:focus:not(:focus-visible) { outline: none; }        /* pas d'anneau au clic de souris, présent au clavier */
```

L'**indicateur de focus** montre aux utilisateurs du clavier, des commutateurs et des technologies d'assistance quel élément est actif. Il doit être visible, contrasté (3 pour 1 au moins) et non masqué par un autre élément. `:focus-visible` permet d'afficher l'anneau pour le clavier tout en évitant de l'imposer aux clics de souris.

> **Ne retirez jamais l'indicateur de focus** sans le remplacer par un équivalent **visible**.

Pour les éléments recouverts par un en-tête collant, `scroll-padding-top` (chapitre 8) évite que l'élément focalisé passe sous l'en-tête.

### 16.3 Cibles tactiles

```css
button, a.bouton, input { min-block-size: 2.75rem; min-inline-size: 2.75rem; }    /* environ 44 px */
```

Les WCAG 2.2 exigent une cible d'au moins **24 sur 24 px** (niveau AA) ; **44 sur 44 px** est la taille recommandée par les guides des plateformes pour une utilisation confortable. Si le visuel est plus petit, on agrandit la zone cliquable avec du `padding` ou un pseudo-élément transparent, sans modifier l'apparence. On espace aussi les cibles voisines pour éviter les erreurs de toucher.

### 16.4 Masquer visuellement, mais pas aux lecteurs d'écran

Il faut parfois fournir un libellé destiné aux seuls lecteurs d'écran (par exemple le texte d'un bouton icône).

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
| `.sr-only` | Non | Oui |
| `display: none`, attribut `hidden`, `visibility: hidden` | Non | Non |
| `aria-hidden='true'` | Oui | Non |
| `opacity: 0` | Non | Oui (et reste focalisable) |

Choisissez selon l'objectif : cacher pour tout le monde (`display: none`), cacher visuellement mais garder pour les technologies d'assistance (`.sr-only`), ou garder visible mais retirer des technologies d'assistance (`aria-hidden`, pour un décor redondant). Ne mettez jamais `aria-hidden='true'` sur un élément focalisable.

### 16.5 Préférences utilisateur

| Préférence | Requête média |
| --- | --- |
| Mouvement réduit | `prefers-reduced-motion: reduce` |
| Thème sombre | `prefers-color-scheme: dark` |
| Contraste renforcé | `prefers-contrast: more` |
| Transparence réduite | `prefers-reduced-transparency: reduce` |
| Couleurs forcées | `forced-colors: active` |
| Taille de texte | Utiliser `rem` ; ne pas bloquer le zoom |

Ces réglages se configurent dans le système d'exploitation ; en les respectant, votre site s'adapte sans effort supplémentaire de l'utilisateur.

### 16.6 Le CSS peut changer le sens de lecture

- `order` (Flexbox), `grid-area`, `position` : ces propriétés changent l'ordre **visuel**, mais **pas** l'ordre de **tabulation et de lecture**, qui suit le DOM. Conservez un **ordre DOM logique** : l'ordre visuel doit correspondre à l'ordre de lecture.
- `content` (avec `::before` et `::after`) peut être **lu** par certains lecteurs d'écran, ou ignoré par d'autres : n'y placez pas d'information essentielle.
- `text-transform: uppercase` est parfois épelé lettre par lettre : pour un acronyme, privilégiez le HTML. À l'inverse, des majuscules saisies directement dans le HTML peuvent être mal lues.
- `list-style: none` peut retirer la sémantique de liste de certains navigateurs ; `display: contents` peut avoir un effet similaire sur les éléments sémantiques.

### 16.7 Liste de contrôle

- Le contraste est suffisant et l'information n'est pas portée par la couleur seule.
- Le focus est **toujours visible**.
- La taille du texte est relative (`rem`) et le zoom à 200 % ne fait perdre aucun contenu.
- `prefers-reduced-motion` est respecté.
- Les cibles tactiles sont suffisantes.
- L'ordre visuel correspond à l'ordre logique du DOM.
- Les éléments masqués le sont avec la bonne technique.

### Synthèse du chapitre 16

- Contraste 4,5 pour 1 (texte), 3 pour 1 (grand texte et composants) ; jamais la couleur seule.
- `:focus-visible` pour un focus clair ; ne supprimez jamais l'indicateur.
- `.sr-only` pour masquer visuellement ; `display: none` masque pour tous.
- Respectez les préférences système et gardez un DOM dans l'ordre de lecture.

---

## 17. Frameworks CSS

**Objectifs d'apprentissage.** Vous saurez dire ce qu'est un framework CSS et ce qu'il apporte et coûte, connaître les principaux frameworks et leurs approches, vous servir de Bootstrap et de Tailwind CSS, et choisir selon votre projet, sans oublier qu'un CSS natif moderne suffit souvent.

### 17.1 Pourquoi un framework ?

Un **framework CSS** fournit des **styles prêts à l'emploi** (grille, composants, utilitaires) pour développer plus vite avec une apparence cohérente.

| Avantages | Inconvénients |
| --- | --- |
| Développement rapide, design cohérent | Poids et dépendance au framework |
| Composants testés, responsive intégré | Sites qui se ressemblent (sans personnalisation) |
| Documentation et communauté | Courbe d'apprentissage des conventions |

> Le CSS moderne (Grid, Flexbox, variables, `@layer`, conteneurs) permet aujourd'hui de **se passer d'un framework** pour de nombreux projets. Un framework reste utile quand une équipe a besoin d'un vocabulaire commun et de composants éprouvés.

Il faut distinguer deux familles : les frameworks de **composants** (qui fournissent des éléments d'interface complets : boutons, modales, barres de navigation) et les frameworks d'**utilitaires** (qui fournissent des classes à une seule fonction, à composer soi-même).

### 17.2 Principaux frameworks

| Framework | Approche | Points forts |
| --- | --- | --- |
| **Bootstrap** (5.3) | **Composants**, grille et utilitaires | Très répandu, nombreux composants (modales, barres de navigation), **modes de couleur** (`data-bs-theme='dark'`), sans jQuery depuis la version 5 |
| **Tailwind CSS** (v4) | **Utilitaires** (*utility-first*) : on compose les classes dans le HTML | Rapidité, cohérence, pas de CSS inutilisé, moteur très rapide |
| **Bulma**, **Pico CSS**, **Foundation** | Composants ou CSS « sémantique » | Légers, simples |
| **UnoCSS** | Utilitaires générés à la demande | Souple, très rapide |
| **Open Props**, **Utopia** | **Variables et échelles** (design tokens) | Bases de systèmes de design |
| **Material**, **shadcn/ui**, **Radix**, **DaisyUI** | Bibliothèques de composants | Selon l'écosystème |

Les numéros de version cités sont ceux de la rédaction de ce cours : consultez la documentation officielle pour la version courante.

### 17.3 Bootstrap (exemple)

```html
<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css' rel='stylesheet'>
<!-- version à ajuster ; avec un build : npm install bootstrap -->

<div class='container'>
    <div class='row g-3'>
        <div class='col-12 col-md-6 col-lg-4'><div class='card p-3'>Carte 1</div></div>
        <div class='col-12 col-md-6 col-lg-4'><div class='card p-3'>Carte 2</div></div>
    </div>
    <button class='btn btn-primary'>Envoyer</button>
</div>
```

Bootstrap repose sur une grille en **12 colonnes** et des points de rupture nommés `sm`, `md`, `lg`, `xl` et `xxl`. Dans l'exemple, une carte occupe toute la largeur sur mobile (`col-12`), la moitié dès `md` (`col-md-6`) et le tiers dès `lg` (`col-lg-4`) ; `g-3` règle les gouttières. La personnalisation se fait par les **variables CSS** (`--bs-primary`) ou par Sass avant compilation. Les composants interactifs (modales, menus déroulants) s'appuient sur un petit fichier JavaScript, à charger en plus.

### 17.4 Tailwind CSS v4 *(à jour)*

La version 4 est **configurée en CSS** (un fichier `tailwind.config.js` n'est plus obligatoire) et s'appuie sur les **couches de cascade**, les **variables CSS** et un moteur écrit en Rust.

```bash
npm install tailwindcss @tailwindcss/vite        # ou @tailwindcss/postcss
```

```css
/* app.css */
@import 'tailwindcss';

@theme {                                     /* design tokens : générés en variables CSS */
    --color-marque: oklch(0.62 0.19 260);
    --font-titre: 'Inter', sans-serif;
    --breakpoint-3xl: 120rem;
}
```

```html
<div class='mx-auto max-w-3xl rounded-lg bg-white p-6 shadow-md dark:bg-zinc-900'>
    <h1 class='font-titre text-2xl font-bold text-marque'>Bonjour</h1>
    <button class='mt-4 rounded bg-marque px-4 py-2 text-white hover:opacity-90 focus-visible:outline-2 md:px-6'>Envoyer</button>
</div>
```

| Concept | Description |
| --- | --- |
| **Utilitaires** | `p-4`, `flex`, `grid`, `text-lg`… : une classe, une déclaration |
| **Variantes** | `hover:`, `focus-visible:`, `md:` (responsive), `dark:`, `group-hover:`, `@container` (`@md:`) |
| **`@theme`** | Définit couleurs, polices, espacements, points de rupture |
| **`@apply`** | Extrait des classes utilitaires dans une règle CSS (à utiliser avec modération) |
| **Purge automatique** | Seules les classes utilisées sont générées |

Les **variantes** se préfixent aux utilitaires pour les conditionner : `md:px-6` signifie « padding horizontal de 6 unités à partir du point de rupture `md` ». Chaque valeur de `@theme` devient aussi une variable CSS (`var(--color-marque)`), utilisable dans votre CSS ordinaire.

> **Compromis.** Avantage : cohérence et vitesse, pas de nommage à inventer. Inconvénient : un HTML chargé de classes. On extrait des **composants** (framework JavaScript, partiels de gabarit) pour éviter la répétition.

### 17.5 Choisir

| Besoin | Choix |
| --- | --- |
| Prototype rapide avec composants prêts | **Bootstrap** |
| Design sur mesure, équipe à l'aise avec les utilitaires | **Tailwind** |
| Petit site, HTML sémantique | **Pico CSS** ou **CSS natif** |
| Design system maison | **CSS natif**, variables et `@layer` |

Quel que soit le choix, les bases de ce cours (cascade, modèle de boîte, Flexbox, Grid) restent indispensables : un framework n'est qu'une couche au-dessus du CSS, et on le débogue avec les mêmes outils.

### Synthèse du chapitre 17

- Un framework accélère le travail mais ajoute un poids et des conventions ; le CSS natif moderne suffit souvent.
- Bootstrap : composants et grille à 12 colonnes ; Tailwind : utilitaires, configuration en CSS (`@theme`) et variantes.
- Choisissez selon le projet et l'équipe, et maîtrisez le CSS sous-jacent.

---

## 18. Préprocesseurs et outils de build

**Objectifs d'apprentissage.** Vous saurez ce qu'apporte un préprocesseur (Sass, Less), écrire du SCSS avec le système de modules moderne, identifier ce que le CSS natif remplace, utiliser PostCSS, Autoprefixer et Lightning CSS, et mettre en place une chaîne de build moderne.

### 18.1 Préprocesseurs : Sass et Less

Un **préprocesseur** est un langage qui ajoute des fonctionnalités à CSS (variables, imbrication, fonctions, mixins, fichiers partiels) et **compile** vers du CSS standard, le seul que comprennent les navigateurs.

|  | **Sass / SCSS** | **Less** | **Stylus** |
| --- | --- | --- | --- |
| Popularité | La plus répandue | En déclin | Rare |
| Syntaxe | SCSS (proche de CSS) ou syntaxe indentée | Proche de CSS | Souple |
| Compilateur | **Dart Sass** (`sass`) | `lessc` (JavaScript) | Node |

```scss
// _variables.scss
$couleur-principale: #3498db;
$points: (petit: 40rem, moyen: 48rem, grand: 64rem);

// _mixins.scss
@use 'sass:map';
@use 'variables' as v;

@mixin a-partir-de($taille) {
    @media (min-width: map.get(v.$points, $taille)) { @content; }
}

// style.scss
@use 'sass:color';
@use 'variables' as *;                       // @use et @forward : le système de modules
@use 'mixins' as m;

.carte {
    color: $couleur-principale;
    &:hover { color: color.adjust($couleur-principale, $lightness: -10%); }
    @include m.a-partir-de(moyen) { padding: 2rem; }
}
```

```bash
npm install -D sass
npx sass --watch src/scss:dist/css          # compilation en continu
```

Les notions clés de Sass sont les suivantes. Les **variables** (`$nom`) sont résolues à la compilation. Les **mixins** (`@mixin`, `@include`) sont des blocs de règles réutilisables et paramétrables ; `@content` permet d'y injecter un bloc. Les **modules** (`@use`, `@forward`) chargent des fichiers dans un espace de noms (`m.a-partir-de`) et remplacent l'ancien `@import`. Les **partiels** sont des fichiers dont le nom commence par `_`, destinés à être importés plutôt que compilés seuls. Sass offre aussi des **fonctions**, des **boucles** (`@each`, `@for`), des **conditions** (`@if`) et des **maps**.

> **À jour.** `@import` de Sass est **déprécié** au profit de **`@use`** et **`@forward`** ; **LibSass** et **node-sass** sont abandonnés : utilisez **Dart Sass**.

### 18.2 Le CSS natif remplace une partie des préprocesseurs

| Fonction de Sass | Équivalent CSS natif |
| --- | --- |
| Variables `$x` | **Propriétés personnalisées** `--x` (dynamiques, modifiables en JavaScript) |
| Imbrication | **Imbrication native** avec `&` |
| `darken()`, `lighten()`, `mix()` | **`color-mix()`**, couleur relative |
| `calc`, `min`, `max`, `clamp` | Fonctions mathématiques natives |
| Partiels et modules | `@import` et `@layer`, ou outil de build |
| Mixins, fonctions, boucles, conditions | Non (partiellement `@function` et `if()`, expérimentaux) : toujours utiles dans Sass |

> **Aujourd'hui**, Sass n'est plus **indispensable**. Il reste pertinent pour les **mixins, boucles et fonctions**, et pour les bases de code existantes.

### 18.3 PostCSS, Lightning CSS et Autoprefixer

| Outil | Rôle |
| --- | --- |
| **PostCSS** | Plateforme de **transformations JavaScript** du CSS (par plugins) |
| **Autoprefixer** | Ajoute les **préfixes** nécessaires selon `browserslist` |
| **postcss-preset-env** | Transpile le CSS moderne pour des navigateurs plus anciens |
| **Lightning CSS** | Outil **très rapide (Rust)** : minification, préfixes, transpilation, imbrication, regroupement |
| **cssnano** | Minification |
| **Vite, webpack, esbuild** | Outils de build qui intègrent la plupart de ces fonctions |

La liste des navigateurs ciblés se déclare dans `package.json` (ou `.browserslistrc`) ; les outils s'en servent pour décider des préfixes et des transformations :

```json
{ "browserslist": [">= 0.5%", "last 2 versions", "not dead"] }
```

```js
// postcss.config.js
export default { plugins: { 'postcss-preset-env': { stage: 2 }, autoprefixer: {}, cssnano: {} } };
```

### 18.4 Un flux de travail moderne

```text
CSS moderne (imbrication, @layer, variables…)
        |
   Vite / Lightning CSS (build)
        |  - imbrication transpilée si nécessaire
        |  - préfixes selon browserslist
        |  - minification et regroupement
        v
   CSS optimisé (+ compression Brotli)
```

Le principe : on écrit le CSS le plus moderne possible, et l'outil de build l'adapte aux navigateurs ciblés, au lieu d'écrire pour le plus petit dénominateur commun.

### Synthèse du chapitre 18

- Un préprocesseur compile vers CSS ; Sass (Dart Sass) avec `@use` est le standard, `@import` est déprécié.
- Variables, imbrication, calculs et couleurs dérivées existent désormais en CSS natif.
- PostCSS, Autoprefixer et Lightning CSS préfixent, transpilent et minifient selon `browserslist`.

---

## 19. Organiser son CSS

**Objectifs d'apprentissage.** Vous saurez identifier les problèmes du CSS à grande échelle, comparer les méthodologies (BEM, OOCSS, SMACSS, ITCSS, utilitaires, CSS Modules, CSS-in-JS), construire une architecture moderne avec couches et portée, structurer vos fichiers, écrire une réinitialisation et fixer des conventions d'équipe.

### 19.1 Les problèmes du CSS à grande échelle

Le CSS a une **portée globale** : toute règle peut affecter n'importe quel élément de n'importe quelle page. Sur un projet qui grandit, cela entraîne des **conflits de noms**, une **spécificité** qui monte (jusqu'au recours à `!important`), et du **code mort** que personne n'ose supprimer de peur de casser une page oubliée. Plusieurs **méthodologies** y répondent.

### 19.2 Méthodologies de nommage et d'architecture

| Méthode | Principe | Exemple |
| --- | --- | --- |
| **BEM** (Block, Element, Modifier) | Convention de nommage **plate** | `.carte`, `.carte__titre`, `.carte--mise-en-avant` |
| **OOCSS** | Séparer **structure** et **apparence** ; réutiliser des « objets » | `.media`, `.btn` avec `.btn-primaire` |
| **SMACSS** | Catégories : Base, Layout, Module, State, Theme | `.is-active`, `.l-grille` |
| **ITCSS** | Couches du plus **générique** au plus **spécifique** (Settings, Tools, Generic, Elements, Objects, Components, Utilities) | Se réalise avec **`@layer`** |
| **Utility-first** (Tailwind) | Classes utilitaires atomiques | `p-4 flex gap-2` |
| **CSS Modules** | Classes **locales** à un composant (noms générés au build) | `styles.carte` |
| **CSS-in-JS** | Styles écrits dans le JavaScript | Voir ci-dessous |

#### BEM en pratique

```css
.carte { border: 1px solid #ddd; }
.carte__titre { font-size: 1.25rem; }
.carte__image { aspect-ratio: 16 / 9; object-fit: cover; }
.carte--mise-en-avant { border-color: gold; }
```

```html
<article class='carte carte--mise-en-avant'>
    <img class='carte__image' src='…' alt=''>
    <h2 class='carte__titre'>Titre</h2>
</article>
```

BEM découpe l'interface en **blocs** (un composant autonome : `carte`), **éléments** (une partie du bloc : `carte__titre`) et **modificateurs** (une variante ou un état : `carte--mise-en-avant`). Tous les sélecteurs ont la même faible spécificité (une classe), ce qui évite les conflits ; en contrepartie les noms sont longs.

#### CSS-in-JS : état des lieux

- **À l'exécution** (*runtime*) : styled-components, Emotion. Pratiques, mais avec un **coût de performance** et une compatibilité limitée avec les **composants serveur** ; styled-components est passé en mode maintenance (annonce des mainteneurs en 2025).
- **À la compilation** (*zero-runtime*) : Vanilla Extract, Panda CSS, StyleX, Linaria. Le CSS est extrait au build.
- La tendance est au **CSS natif avec CSS Modules**, ou aux **utilitaires**.

### 19.3 L'architecture moderne : couches et portée

```css
@layer reset, tokens, base, layout, composants, utilitaires;

@layer composants {
    .carte {
        padding: var(--esp-3);

        @scope (.carte) { h2 { font-size: 1.25rem; } }       /* portée locale sans convention de nommage */
    }
}
```

Les **couches** (`@layer`, chapitre 4) donnent un ordre explicite entre grandes familles de styles ; `@scope` limite les règles d'un composant à sa sous-arborescence. Ensemble, ils rendent inutiles bien des conventions de nommage lourdes et la plupart des usages de `!important`.

### 19.4 Structure de fichiers

```text
styles/
|-- main.css              <- importe les couches dans l'ordre (ou point d'entrée du bundler)
|-- 00-reset.css
|-- 01-tokens.css         <- variables : couleurs, espacements, typographie
|-- 02-base.css           <- éléments HTML (body, a, h1…)
|-- 03-layout.css         <- grilles, conteneurs
|-- composants/
|   |-- bouton.css
|   |-- carte.css
|   +-- modale.css
+-- 99-utilitaires.css
```

L'ordre numéroté reflète celui des couches : du plus général au plus spécifique. Chaque composant a son fichier, ce qui facilite la suppression de code mort.

### 19.5 Réinitialisation (*reset*)

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

Ce reset a trois rôles : harmoniser le modèle de boîte (`border-box`), neutraliser des valeurs par défaut peu pratiques (marges, tailles de police des champs, images en ligne), et poser des bases saines (interligne, retour à la ligne, `text-wrap`). Alternatives : **normalize.css**, **modern-normalize**, **the-new-css-reset**. Un reset doit rester **court** : on ne réinitialise pas tout, seulement ce qui gêne.

### 19.6 Conventions d'équipe

- **Ordre des déclarations** cohérent (positionnement, modèle de boîte, typographie, visuel, divers) ou ordre alphabétique, automatisé par **Stylelint** ou Prettier.
- **Variables** pour tout ce qui se répète (couleurs, espacements, rayons, ombres).
- **Commentaires** de section et noms **explicites**.
- **Pas d'`!important`** (sauf utilitaires) et sélecteurs **peu spécifiques**.
- Suppression régulière du **code mort** (outil *Coverage*, chapitre 27).

Exemple de configuration Stylelint (`.stylelintrc.json`) :

```json
{ "extends": ["stylelint-config-standard"], "rules": { "selector-class-pattern": null, "declaration-no-important": true } }
```

### Synthèse du chapitre 19

- Le CSS à grande échelle souffre de portée globale, de conflits et de spécificité croissante.
- BEM, ITCSS, utilitaires ou CSS Modules : choisissez une méthode et tenez-vous-y.
- `@layer` et `@scope` donnent une architecture native ; un reset court et des conventions outillées par Stylelint complètent le tout.

---

# Partie III — Tests

## 20. Tester le CSS : qualité, styles calculés et contrats

**Objectifs d'apprentissage.** Vous saurez expliquer ce que l'on peut réellement tester en CSS, valider la syntaxe et les conventions avec Stylelint, automatiser les contrôles avant chaque validation de code, écrire des tests de navigateur qui vérifient des styles calculés et des contrats de mise en page, tester des design tokens et des thèmes, mener une revue de code CSS efficace et éviter les tests fragiles.

### 20.1 Que tester en CSS ?

Le CSS ne se teste pas comme une fonction : il n'a ni entrée ni sortie au sens classique, son résultat est un **rendu** qui dépend du navigateur, de la fenêtre, de la police et des préférences de l'utilisateur. On le contrôle donc à plusieurs niveaux, du plus rapide au plus réaliste.

| Niveau | Outil | Ce qu'il détecte | Coût |
| --- | --- | --- | --- |
| **Syntaxe** | Validateur W3C, DevTools, Stylelint | Propriétés inconnues, valeurs invalides, doublons | Très faible |
| **Conventions** | Stylelint, Prettier | Spécificité excessive, `!important`, ordre, formatage | Très faible |
| **Styles calculés** | Tests de navigateur (Playwright, Vitest en mode navigateur) | Une règle s'applique-t-elle bien ? Un contrat de mise en page est-il respecté ? | Faible à moyen |
| **Rendu visuel** | Captures d'écran comparées (chapitre 21) | Régressions d'apparence | Moyen |
| **Accessibilité** | axe-core, Lighthouse, tests manuels (chapitre 21) | Contraste, focus, étiquettes, tailles de cibles | Moyen |
| **Compatibilité** | Tests multi-navigateurs (chapitre 21) | Différences entre moteurs | Moyen à élevé |

Principe directeur : tester des **comportements observables** (« le menu ne déborde pas à 320 px », « le focus est visible ») et non des détails d'implémentation (« la classe `.menu` a un `padding` de 12 px »).

### 20.2 Valider la syntaxe

Le **validateur CSS du W3C** signale les erreurs de syntaxe, mais il connaît mal les nouveautés récentes. Les **DevTools** sont plus fiables au quotidien : une déclaration invalide y apparaît barrée avec un avertissement (chapitre 27). Pour automatiser, on utilise un linter.

**Stylelint** analyse les feuilles de style et applique des règles configurables.

```bash
npm install -D stylelint stylelint-config-standard
npx stylelint 'src/**/*.css'            # analyse
npx stylelint 'src/**/*.css' --fix      # corrige automatiquement ce qui peut l'être
```

```js
// stylelint.config.js
export default {
    extends: ['stylelint-config-standard'],
    rules: {
        'declaration-no-important': true,                 // interdit !important
        'selector-max-id': 0,                             // pas d'identifiants dans les sélecteurs
        'selector-max-specificity': '0,3,0',              // spécificité plafonnée
        'selector-max-compound-selectors': 3,             // pas de sélecteurs trop profonds
        'declaration-block-no-duplicate-properties': true,
        'color-no-invalid-hex': true,
        'property-no-unknown': true,
        'selector-class-pattern': null,                   // convention de nommage libre
    },
};
```

Ces règles traduisent en contrôles automatiques les bonnes pratiques vues aux chapitres 2, 4 et 19 : sélecteurs simples, spécificité maîtrisée, pas d'`!important`. Le plugin `stylelint-no-unsupported-browser-features` signale en outre les fonctionnalités non prises en charge par votre liste `browserslist` (chapitre 25).

### 20.3 Automatiser avant chaque validation de code

Un contrôle qui dépend de la bonne volonté de chacun finit par être oublié. On l'exécute donc automatiquement :

- **Dans l'éditeur** : l'extension Stylelint souligne les erreurs pendant la frappe.
- **Avant chaque commit** : des outils comme Husky et lint-staged lancent Stylelint et Prettier sur les seuls fichiers modifiés.
- **En intégration continue** : le même contrôle, bloquant, s'exécute sur chaque demande de fusion (voir 21.5).

```bash
npx prettier --write 'src/**/*.css'     # formatage uniforme
npx stylelint 'src/**/*.css'            # règles de qualité
```

Séparer les rôles évite les conflits : **Prettier** règle la mise en forme (indentation, espaces), **Stylelint** règle la qualité (spécificité, doublons, valeurs invalides).

### 20.4 Tester les styles calculés dans un vrai navigateur

Un test de navigateur charge la page, interroge les **styles calculés** et vérifie des **contrats**. **Playwright** est l'outil le plus courant ; il pilote Chromium, Firefox et WebKit.

```js
import { test, expect } from '@playwright/test';

test('le bouton principal est visible et accessible au clavier', async ({ page }) => {
    await page.goto('/composants/bouton.html');
    const bouton = page.locator('.bouton');

    await expect(bouton).toHaveCSS('cursor', 'pointer');
    await expect(bouton).toHaveCSS('display', 'inline-flex');

    await bouton.focus();                                             // simule le focus clavier
    const contour = await bouton.evaluate((el) => getComputedStyle(el).outlineStyle);
    expect(contour).not.toBe('none');                                 // l'anneau de focus existe
});

test('aucun défilement horizontal à 320 px', async ({ page }) => {
    await page.setViewportSize({ width: 320, height: 640 });
    await page.goto('/');
    const deborde = await page.evaluate(
        () => document.documentElement.scrollWidth > window.innerWidth,
    );
    expect(deborde).toBe(false);                                      // contrat de mise en page
});
```

Le premier test vérifie des valeurs précises ; le second vérifie un **invariant** (« la page ne déborde jamais »), bien plus robuste qu'une comparaison de dimensions. Les invariants utiles à tester : absence de défilement horizontal aux largeurs courantes (320, 768, 1280 px), focus visible, contraste minimal, taille de cible tactile, éléments qui ne se chevauchent pas.

### 20.5 Tester les design tokens et les thèmes

Les variables CSS (chapitre 12) forment un contrat entre le design et le code : on peut vérifier qu'elles existent, qu'elles changent avec le thème et que le contraste reste suffisant.

```js
test('le thème sombre redéfinit les variables', async ({ page }) => {
    await page.goto('/');
    const lire = () => page.evaluate(
        () => getComputedStyle(document.documentElement).getPropertyValue('--fond').trim(),
    );

    const clair = await lire();
    await page.emulateMedia({ colorScheme: 'dark' });                 // émule la préférence système
    const sombre = await lire();

    expect(clair).not.toBe('');
    expect(sombre).not.toBe(clair);
});
```

`page.emulateMedia` simule les préférences système (`colorScheme`, `reducedMotion`, `forcedColors`, `media: 'print'`) : c'est la façon fiable de tester les requêtes de préférences du chapitre 14.

### 20.6 La revue de code CSS

Les outils ne remplacent pas le regard humain. Une revue de code CSS vérifie notamment :

- **Spécificité et cascade** : pas d'`!important` injustifié, pas d'identifiants, couches utilisées à bon escient.
- **Valeurs magiques** : un `margin-top: 37px` sans explication est un signal d'alerte ; on préfère des variables et une échelle d'espacement.
- **Unités** : `rem` pour le texte et les espacements, pas de hauteurs fixes sur du texte.
- **Responsive** : mobile d'abord, aucun point de rupture arbitraire.
- **Accessibilité** : focus visible, contraste, mouvement réduit, ordre de lecture.
- **Thèmes** : couleurs en variables, thème sombre vérifié.
- **Suppression** : un style ajouté remplace-t-il un style obsolète que l'on peut retirer ?

### 20.7 Pièges fréquents

| Piège | Conséquence | Parade |
| --- | --- | --- |
| Tester des valeurs de pixels exactes | Test cassé par un simple changement de police | Tester des invariants et des contrats |
| S'appuyer sur des sélecteurs fragiles (`div > div > span`) | Test cassé par le moindre changement de structure | Cibler par rôle, étiquette ou attribut de test |
| Animations et transitions actives pendant le test | Résultats instables | Émuler `reducedMotion: 'reduce'` ou couper les animations |
| Polices qui se chargent après la mesure | Dimensions variables | Attendre le chargement des polices (`document.fonts.ready`) |
| Exécuter les tests sur des machines différentes | Écarts de rendu | Exécuter toujours dans le même environnement (conteneur) |
| Linter trop strict dès le départ | Équipe qui contourne les règles | Introduire les règles progressivement |

### Synthèse du chapitre 20

Le CSS se teste à plusieurs niveaux : **syntaxe** (DevTools, validateur), **conventions** (**Stylelint** et **Prettier**, exécutés dans l'éditeur, avant chaque commit et en intégration continue), **styles calculés** (tests de navigateur qui vérifient des **contrats** et des **invariants**, comme l'absence de défilement horizontal ou la présence d'un focus visible) et **tokens et thèmes** (variables vérifiées avec `emulateMedia`). La revue de code complète les outils sur la spécificité, les valeurs magiques, l'accessibilité et les thèmes. On teste des comportements observables plutôt que des détails d'implémentation, et on stabilise les tests en neutralisant animations, polices et différences d'environnement.

---

## 21. Tests visuels, d'accessibilité et multi-navigateurs

**Objectifs d'apprentissage.** Vous saurez mettre en place des tests de non-régression visuelle par comparaison de captures d'écran, tester des mises en page sur plusieurs tailles et préférences, automatiser les contrôles d'accessibilité tout en connaissant leurs limites, exécuter vos tests sur les trois moteurs de rendu, brancher l'ensemble sur l'intégration continue et éviter les tests instables.

### 21.1 Les tests visuels de non-régression

Une modification de CSS peut avoir des effets lointains : changer une marge globale décale vingt pages. Un **test visuel de non-régression** compare une **capture de référence** (l'apparence validée) à une **nouvelle capture** et signale toute différence. C'est le filet de sécurité le plus efficace pour refactorer du CSS en confiance.

```js
import { test, expect } from '@playwright/test';

test('la page accueil garde son apparence', async ({ page }) => {
    await page.goto('/');
    await page.evaluate(() => document.fonts.ready);                   // polices chargées
    await expect(page).toHaveScreenshot('accueil.png', {
        fullPage: true,
        animations: 'disabled',                                         // fige animations et transitions
        maxDiffPixelRatio: 0.01,                                        // tolérance : 1 % de pixels
        mask: [page.locator('.date-du-jour')],                          // masque le contenu variable
    });
});
```

La première exécution crée l'image de référence ; les suivantes la comparent. Quand un changement est **voulu**, on régénère les références (`npx playwright test --update-snapshots`) et on les relit dans la demande de fusion comme n'importe quel changement de code.

**Stabiliser les tests visuels.** La principale difficulté est le bruit : un test qui échoue sans raison est vite ignoré. Les mesures qui comptent :

- fixer la **taille de fenêtre** et le **facteur d'échelle** ;
- couper les **animations** (`animations: 'disabled'`) et attendre les **polices** ;
- **masquer ou figer** les contenus variables (dates, publicités, avatars aléatoires) ;
- fournir des **données de test déterministes** ;
- exécuter toujours dans le **même environnement** (même système, mêmes polices, de préférence un conteneur), car le rendu du texte varie d'un système à l'autre.

Des services comme Chromatic ou Percy proposent des comparaisons visuelles hébergées avec interface de validation, notamment pour les bibliothèques de composants.

### 21.2 Tester les tailles et les préférences

Une mise en page responsive se teste sur une **matrice** : plusieurs largeurs, plusieurs préférences.

```js
const largeurs = [320, 768, 1280];
const preferences = [
    { nom: 'clair', colorScheme: 'light' },
    { nom: 'sombre', colorScheme: 'dark' },
    { nom: 'mouvement-reduit', reducedMotion: 'reduce' },
    { nom: 'couleurs-forcees', forcedColors: 'active' },
];

for (const largeur of largeurs) {
    for (const pref of preferences) {
        test(`accueil ${largeur}px ${pref.nom}`, async ({ page }) => {
            await page.setViewportSize({ width: largeur, height: 800 });
            await page.emulateMedia(pref);
            await page.goto('/');
            await expect(page).toHaveScreenshot(`accueil-${largeur}-${pref.nom}.png`);
        });
    }
}
```

Les tailles à couvrir correspondent à vos points de rupture (chapitre 14), plus une largeur plus étroite que le plus petit mobile courant. On teste aussi le **zoom à 200 %** (équivalent à une largeur de 640 px à 100 % pour une fenêtre de 1280 px) et une **taille de police augmentée**, afin de repérer les textes tronqués ou les conteneurs à hauteur fixe.

### 21.3 Tests d'accessibilité automatisés

**axe-core** est le moteur d'analyse d'accessibilité le plus répandu ; le paquet `@axe-core/playwright` l'exécute dans vos tests.

```js
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('la page accueil est exempte de violations détectables', async ({ page }) => {
    await page.goto('/');
    const resultats = await new AxeBuilder({ page })
        .withTags(['wcag2a', 'wcag2aa', 'wcag22aa'])                     // niveaux ciblés
        .analyze();
    expect(resultats.violations).toEqual([]);
});
```

**Ce que l'automatisation détecte** : contrastes insuffisants, champs sans étiquette, images sans texte alternatif, rôles ARIA invalides, titres mal hiérarchisés, tailles de cibles trop petites. **Ce qu'elle ne détecte pas** : la pertinence d'un libellé, la logique de l'ordre de tabulation, la compréhensibilité d'une interface au lecteur d'écran, la gêne causée par une animation. On estime généralement que les outils automatiques ne repèrent qu'une partie des problèmes ; ils sont indispensables mais jamais suffisants.

**Contrôles manuels à intégrer à la revue :**

| Contrôle | Comment |
| --- | --- |
| Navigation au clavier | Parcourir la page avec Tab et Maj+Tab : focus toujours visible, ordre logique, aucun piège |
| Zoom 200 % et 400 % | Aucun contenu perdu, aucun défilement horizontal (hors tableaux et cartes) |
| Lecteur d'écran | Parcourir avec NVDA, VoiceOver ou TalkBack les parcours principaux |
| Mouvement réduit | Vérifier que les animations disparaissent ou s'atténuent |
| Couleurs forcées | Activer le mode contraste élevé : bordures et icônes restent visibles |
| Cibles tactiles | Au moins 24 sur 24 px (WCAG 2.2), idéalement 44 sur 44 px |

### 21.4 Tests multi-navigateurs

Trois moteurs dominent (Blink, WebKit, Gecko, voir chapitre 25). Playwright les pilote tous avec la même suite de tests.

```js
// playwright.config.js
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
    testDir: './tests',
    projects: [
        { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
        { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
        { name: 'webkit', use: { ...devices['Desktop Safari'] } },
        { name: 'mobile-chrome', use: { ...devices['Pixel 7'] } },
        { name: 'mobile-safari', use: { ...devices['iPhone 14'] } },
    ],
});
```

Chaque projet produit ses propres références visuelles, car le rendu du texte diffère légèrement d'un moteur à l'autre. Les différences réelles à surveiller sont connues : unités de viewport dynamiques sur mobile, rendu des contrôles de formulaire, prise en charge des nouveautés (`@scope`, ancrage, animations liées au défilement), comportement de `backdrop-filter` et des polices. Playwright émule des appareils mais ne remplace pas totalement les **vrais appareils**, surtout pour Safari sur iOS (clavier virtuel, barres d'adresse, performances) : on complète par des services comme BrowserStack ou LambdaTest, ou par quelques appareils physiques.

### 21.5 Intégration continue

Les tests n'ont de valeur que s'ils s'exécutent à chaque changement. Un flux typique enchaîne les contrôles du moins coûteux au plus coûteux :

```yaml
# .github/workflows/css.yml
name: CSS
on: [pull_request]
jobs:
  qualite:
    runs-on: ubuntu-latest
    container: mcr.microsoft.com/playwright:v1.50.0-noble        # environnement de rendu stable
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: npm }
      - run: npm ci
      - run: npx stylelint 'src/**/*.css'                        # 1. qualité du code
      - run: npm run build                                       # 2. compilation et optimisation
      - run: npx playwright test                                 # 3. styles, visuel, accessibilité, moteurs
      - uses: actions/upload-artifact@v4
        if: failure()
        with: { name: rapport-playwright, path: playwright-report/ }
```

Les numéros de version de l'exemple sont indicatifs : adaptez-les aux versions courantes. Deux bonnes pratiques : **bloquer la fusion** si le contrôle échoue, et **publier les rapports** (captures attendues, obtenues et différences) pour que le relecteur voie immédiatement l'écart. Les mises à jour de références visuelles se discutent en revue comme du code.

### 21.6 Pièges fréquents

| Piège | Conséquence | Parade |
| --- | --- | --- |
| Références générées sur un poste local, tests lancés ailleurs | Échecs permanents dus aux polices | Générer et exécuter dans le même conteneur |
| Tolérance de comparaison trop large | Régressions réelles non détectées | Tolérance minimale, masques ciblés |
| Se fier à axe seul | Fausse impression d'accessibilité | Compléter par des contrôles manuels |
| Tout tester sur tous les moteurs | Pipeline lent et coûteux | Suite complète sur un moteur, vérifications ciblées sur les autres |
| Mettre à jour les références sans les relire | Régressions validées par habitude | Relecture obligatoire des différences |

### Synthèse du chapitre 21

Les **tests visuels de non-régression** comparent des captures à des références et sécurisent les refontes ; ils exigent des conditions **stables** (taille fixe, animations coupées, polices chargées, contenus variables masqués, environnement identique). On teste une **matrice** de largeurs et de préférences (clair, sombre, mouvement réduit, couleurs forcées) grâce à `emulateMedia`. **axe-core** automatise la détection d'une partie des problèmes d'accessibilité, mais **ne remplace pas** les contrôles manuels (clavier, zoom, lecteur d'écran). **Playwright** exécute la même suite sur **Chromium, Firefox et WebKit**, avec une complémentarité utile des vrais appareils. L'ensemble s'exécute en **intégration continue**, avec rapports publiés et fusion bloquée en cas d'échec.

---

# Partie IV — Performance

## 22. Performances et optimisation

**Objectifs d'apprentissage.** Vous saurez expliquer pourquoi le CSS pèse sur les métriques de performance, réduire et livrer efficacement vos feuilles de style, optimiser le rendu (`content-visibility`, `contain`), éviter les mythes courants et mesurer l'effet de vos changements.

### 22.1 Objectifs

Le CSS est **bloquant pour le rendu** : le navigateur n'affiche rien avant de l'avoir téléchargé et analysé. Un CSS **léger** et **bien livré** améliore trois des **Core Web Vitals** : le **LCP** (*Largest Contentful Paint*, temps d'affichage du plus grand élément visible), le **CLS** (*Cumulative Layout Shift*, stabilité visuelle) et l'**INP** (*Interaction to Next Paint*, réactivité aux interactions).

### 22.2 Réduire et livrer efficacement

| Technique | Effet |
| --- | --- |
| **Minification** (cssnano, Lightning CSS, Vite) | Supprime espaces et commentaires |
| **Compression** Brotli ou gzip côté serveur | Divise la taille par 4 à 5 |
| **Supprimer le CSS inutilisé** (PurgeCSS, outils de build, Tailwind) | Moins de poids |
| **CSS critique** en ligne dans `<head>` et reste chargé **sans bloquer** | Meilleur premier affichage |
| **Cache longue durée** avec noms hachés (`style.a1b2c3.css`) | Pas de re-téléchargement |
| **Préchargement** des ressources critiques (`rel='preload'`) | Polices, CSS critique |
| **Éviter `@import`** | Évite les chargements en série |
| **Découper** par page ou route (code-splitting du CSS) | Ne charge que le nécessaire |

> **À jour.** L'ancien conseil « regrouper tous les fichiers pour réduire les requêtes HTTP » est **moins important** avec **HTTP/2 et HTTP/3** (multiplexage). Regrouper reste utile pour la compression et la simplicité, mais n'est plus une règle absolue.

Le **nom haché** (le hachage du contenu dans le nom du fichier) permet un cache très long : si le contenu change, le nom change, et le navigateur télécharge la nouvelle version ; sinon il réutilise l'ancienne sans interroger le serveur.

### 22.3 Performance de rendu

```css
.section-lourde {
    content-visibility: auto;                  /* ne rend pas ce qui est hors écran */
    contain-intrinsic-size: auto 600px;        /* taille réservée en attendant le rendu */
}
.widget { contain: layout paint; }             /* isole le calcul : un changement interne n'affecte pas le reste */
```

`content-visibility: auto` laisse le navigateur **ignorer le rendu** des sections hors de l'écran, ce qui accélère nettement le chargement des longues pages ; `contain-intrinsic-size` réserve une taille estimée pour que la barre de défilement ne saute pas. `contain` déclare qu'un élément est indépendant du reste de la page (mise en page, peinture), ce qui limite l'étendue des recalculs.

| Bonne pratique | Raison |
| --- | --- |
| **Animer `transform` et `opacity`** | Évite recalcul de mise en page et repeinture |
| Éviter `box-shadow` ou `filter` animés sur de grandes surfaces | Coûteux (repeinture) |
| Limiter la **taille du DOM** | Moins de styles à calculer |
| `will-change` **ponctuel** | Évite la surconsommation de mémoire |
| Éviter le **layout thrashing** (JavaScript qui lit puis écrit la mise en page en boucle) | Regrouper lectures et écritures |
| Réserver l'espace des images et polices (`width`, `height`, `size-adjust`) | Évite le CLS |
| `font-display: swap` ou `optional` ; polices **WOFF2** variables | Texte rapide, moins de fichiers |

> **Mythe.** La complexité des sélecteurs (`div > ul li a`) a **très peu d'impact** sur les navigateurs modernes. Concentrez-vous sur la **taille du CSS**, la **mise en cache** et la **taille du DOM**.

### 22.4 Mesurer

- **Lighthouse** (DevTools) et **PageSpeed Insights** : LCP, CLS, INP, ressources bloquant le rendu.
- Onglet **Coverage** : pourcentage de CSS **non utilisé**.
- Onglet **Performance** : recalcul de styles, mise en page, repeinture.
- **WebPageTest** et l'extension **Web Vitals**.

On mesure avant et après chaque optimisation, de préférence sur un appareil modeste et un réseau limité, car les gains se voient surtout là.

### Synthèse du chapitre 22

- Le CSS bloque le rendu : minifiez, compressez, retirez l'inutilisé, mettez en cache avec des noms hachés, chargez le non critique sans bloquer.
- `content-visibility` et `contain` réduisent le coût du rendu ; animez `transform` et `opacity`.
- La complexité des sélecteurs compte peu ; le poids, le cache et le DOM comptent beaucoup.
- Mesurez avec Lighthouse, Coverage et Performance.

---

## 23. Rendu du navigateur : mise en page, peinture et composition

**Objectifs d'apprentissage.** Vous saurez décrire précisément les étapes du rendu et ce qui déclenche chacune, éviter le recalcul forcé de la mise en page, comprendre les couches de composition et l'usage raisonné de `will-change`, isoler le coût du rendu avec `contain` et `content-visibility`, concevoir des animations et des défilements fluides et reconnaître les causes habituelles de saccades.

### 23.1 Le pipeline de rendu en détail

Le chapitre 1 a présenté le rendu dans ses grandes lignes. Pour optimiser, il faut distinguer **quatre étapes**, car elles n'ont pas le même coût :

| Étape | Rôle | Déclenchée par un changement de… | Coût |
| --- | --- | --- | --- |
| **Calcul des styles** (*style recalculation*) | Déterminer les styles appliqués à chaque élément | Classes, attributs, sélecteurs, variables CSS | Faible à moyen |
| **Mise en page** (*layout*, *reflow*) | Calculer la taille et la position de chaque boîte | `width`, `height`, `margin`, `padding`, `top`, `left`, `display`, `font-size`, contenu | Élevé |
| **Peinture** (*paint*) | Dessiner les pixels de chaque couche | `color`, `background`, `border-color`, `box-shadow`, `visibility` | Moyen |
| **Composition** (*composite*) | Assembler les couches, souvent sur le processeur graphique | `transform`, `opacity` (sur une couche dédiée) | Très faible |

Un changement déclenche **l'étape concernée et toutes les suivantes** : une modification de `width` entraîne mise en page, peinture et composition ; une modification de `background-color` ne réclame que peinture et composition ; une modification de `transform` peut se limiter à la composition. D'où la règle d'or des animations (section 23.5) : animer ce qui coûte le moins.

La mise en page est **globale par nature** : changer la taille d'un élément peut obliger à recalculer ses voisins, ses parents et ses descendants. Plus le DOM est grand et profond, plus ce recalcul est long.

### 23.2 Recalcul forcé et *layout thrashing*

Le navigateur regroupe d'ordinaire les modifications de style et ne recalcule la mise en page qu'une fois, au moment de dessiner l'image. Mais **lire** certaines propriétés de géométrie (`offsetWidth`, `getBoundingClientRect()`, `scrollTop`, `getComputedStyle(...)`) après avoir **écrit** un style l'oblige à recalculer **immédiatement** : c'est un *reflow* forcé. Alterner lectures et écritures dans une boucle répète ce coût à chaque tour : c'est le **layout thrashing**.

```js
// Mauvais : chaque tour lit la géométrie (force le calcul) puis écrit
for (const el of elements) {
    el.style.width = el.parentElement.offsetWidth / 2 + 'px';
}

// Bon : toutes les lectures d'abord, toutes les écritures ensuite
const largeurs = elements.map((el) => el.parentElement.offsetWidth);
elements.forEach((el, i) => {
    el.style.width = largeurs[i] / 2 + 'px';
});
```

Pour des mises à jour liées à l'affichage, on regroupe le travail dans `requestAnimationFrame`. Mieux encore, on évite le problème : une valeur de largeur qui dépend du parent s'exprime en CSS (pourcentages, `calc()`, Grid, requêtes de conteneur) et ne nécessite aucun JavaScript.

### 23.3 Couches de composition et `will-change`

Le navigateur découpe la page en **couches** (*layers*) peintes séparément puis assemblées. Un élément reçoit sa propre couche lorsqu'il est animé avec `transform` ou `opacity`, lorsqu'il utilise `will-change`, ou dans d'autres cas (vidéo, canvas, `position: fixed` selon les navigateurs). Une couche permet de déplacer ou de faire varier l'opacité d'un élément **sans** le repeindre : c'est la clé des animations fluides.

```css
.panneau-glissant { will-change: transform; }          /* annonce l'animation à venir */
.panneau-glissant.termine { will-change: auto; }       /* libère la ressource après usage */
```

Chaque couche **consomme de la mémoire** (surtout sur mobile). `will-change` est donc un outil de **dernier recours**, ciblé : on l'applique juste avant une animation et on le retire après, on ne l'écrit jamais sur `*` ni sur des dizaines d'éléments. L'ancien hack `transform: translateZ(0)`, destiné à forcer une couche, est devenu inutile et à éviter. Le panneau **Couches** (*Layers*) des DevTools montre les couches créées et leur coût mémoire.

### 23.4 Isoler le coût du rendu

Lorsqu'un changement local force un recalcul de toute la page, on peut **borner** son effet.

```css
.widget { contain: layout paint style; }               /* le changement interne n'affecte pas l'extérieur */
.widget-strict { contain: strict; }                    /* taille doit être connue : size + layout + paint + style */

.section-longue {
    content-visibility: auto;                          /* ne rend pas ce qui est hors écran */
    contain-intrinsic-size: auto 600px;                /* taille estimée réservée */
}
```

| Propriété | Effet | Précaution |
| --- | --- | --- |
| `contain: layout` | La mise en page interne n'influence pas l'extérieur | L'élément devient un contexte d'empilement et un bloc conteneur |
| `contain: paint` | Le contenu ne déborde pas visuellement de la boîte | Rogne tout débordement |
| `contain: size` | La taille ne dépend pas du contenu | Il faut fixer la taille soi-même |
| `content-visibility: auto` | Saute le rendu des sections hors écran | Réserver la taille avec `contain-intrinsic-size` pour éviter les sauts de défilement |
| `content-visibility: hidden` | Comme `display: none` mais conserve l'état de rendu | Contenu masqué à l'accessibilité |
| `container-type` | Active `contain` adapté aux requêtes de conteneur | Voir chapitre 14 |

On utilise `content-visibility: auto` sur les sections lourdes d'une longue page ou sur les éléments d'une longue liste, après mesure. Le contenu reste accessible à la recherche dans la page et aux technologies d'assistance tant qu'il n'est pas en mode `hidden`.

### 23.5 Animations performantes

Les animations s'exécutent sur deux fils possibles : le **fil principal** (partagé avec JavaScript, le calcul des styles et la mise en page) et le **compositeur** (fil dédié, plus fluide). Seules quelques propriétés peuvent être animées par le compositeur : `transform` (et `translate`, `rotate`, `scale`), `opacity` et, selon les cas, `filter`. Animer toute autre propriété revient à mobiliser le fil principal ; une tâche JavaScript longue peut alors faire saccader l'animation.

```css
/* À éviter : déclenche mise en page et peinture à chaque image */
.boite { transition: left .3s, width .3s; }

/* À privilégier : composition seule */
.boite { transition: transform .3s, opacity .3s; }
```

Quelques règles complémentaires :

- **Réduire la surface repeinte** : animer un petit élément coûte moins qu'un grand ; `box-shadow`, `filter` et `backdrop-filter` animés sur de larges surfaces sont coûteux.
- **Animer par transformation** : pour changer une taille, préférer `scale` à `width` quand l'effet visuel est acceptable ; pour déplacer, préférer `translate` à `left` ou `top`.
- **Utiliser le CSS plutôt que JavaScript** quand c'est possible, y compris les animations liées au défilement (`animation-timeline`, chapitre 13) qui s'exécutent hors du fil principal dans les navigateurs qui le permettent.
- **Respecter le mouvement réduit** (chapitre 13) : une animation évitée est aussi une animation gratuite.

### 23.6 Défilement fluide

- Utiliser `position: sticky` plutôt qu'un écouteur de défilement qui repositionne un élément.
- Pour les longues listes, combiner `content-visibility: auto` et, au besoin, la **virtualisation** (ne rendre que les lignes visibles).
- Limiter la propagation du défilement avec `overscroll-behavior` dans les panneaux et les modales.
- Côté JavaScript, déclarer les écouteurs de défilement et de toucher comme **passifs** (`{ passive: true }`) pour que le défilement ne soit pas bloqué par le gestionnaire.
- Éviter les arrière-plans `background-attachment: fixed` : coûteux et mal pris en charge sur mobile.

### 23.7 Pièges fréquents

| Symptôme | Cause probable | Piste |
| --- | --- | --- |
| Animation saccadée | Propriété animée qui déclenche la mise en page | Passer à `transform` et `opacity` |
| Page lente à l'ouverture d'un menu | Recalcul de styles étendu (sélecteurs `:has()` larges, DOM énorme) | Mesurer dans l'onglet Performance, restreindre le sélecteur |
| Mémoire élevée sur mobile | `will-change` sur trop d'éléments | Le retirer, le cibler |
| Saut de défilement avec `content-visibility` | Taille intrinsèque non réservée | Ajouter `contain-intrinsic-size` |
| Flou ou contour dentelé après une animation | Couche mal rastérisée | Retirer `will-change` en fin d'animation |

### Synthèse du chapitre 23

Le rendu comporte **quatre étapes** de coût croissant à l'inverse de la composition : calcul des styles, **mise en page** (la plus coûteuse), **peinture** et **composition**. Un changement déclenche l'étape concernée et toutes les suivantes, d'où le choix d'animer `transform` et `opacity`. Alterner lecture et écriture de la géométrie en JavaScript provoque des **recalculs forcés** (*layout thrashing*) : on regroupe les lectures puis les écritures, ou on déplace la logique en CSS. Les **couches** de composition accélèrent les animations mais coûtent de la mémoire : `will-change` reste ponctuel. `contain` et `content-visibility` bornent le coût du rendu des zones lourdes. Les animations fluides s'exécutent sur le **compositeur** ; le défilement s'optimise par `sticky`, écouteurs passifs, virtualisation et `overscroll-behavior`.

---

## 24. Mesurer, budgets et optimisation continue

**Objectifs d'apprentissage.** Vous saurez relier le CSS aux Core Web Vitals, mesurer en laboratoire avec Lighthouse et les DevTools, mesurer sur le terrain avec des données d'utilisateurs réels, définir des budgets de performance appliqués en intégration continue, réduire le CSS inutilisé et conduire une démarche d'optimisation mesurée plutôt qu'intuitive.

### 24.1 Les métriques qui concernent le CSS

Les **Core Web Vitals** sont trois mesures de l'expérience réelle, utilisées par Google pour évaluer les pages. Le CSS agit sur chacune.

| Métrique | Ce qu'elle mesure | Seuil « bon » | Influence du CSS |
| --- | --- | --- | --- |
| **LCP** (*Largest Contentful Paint*) | Temps d'affichage du plus grand élément visible | 2,5 s ou moins | CSS bloquant le rendu, polices web, image de fond tardive |
| **CLS** (*Cumulative Layout Shift*) | Stabilité visuelle : décalages inattendus de la mise en page | 0,1 ou moins | Images sans dimensions, polices qui changent la taille du texte, contenu injecté sans espace réservé |
| **INP** (*Interaction to Next Paint*) | Réactivité aux interactions (clic, toucher, clavier) | 200 ms ou moins | Recalculs de styles et mises en page coûteux déclenchés par une interaction |

D'autres mesures éclairent le diagnostic : **FCP** (premier contenu affiché), **TBT** (temps de blocage total) et la taille transférée du CSS. Les seuils sont ceux publiés par Google à la date de rédaction ; ils peuvent évoluer.

### 24.2 Mesurer en laboratoire

Les mesures de **laboratoire** (*lab data*) se font dans un environnement contrôlé : reproductibles, utiles pour diagnostiquer, mais pas représentatives de la diversité des utilisateurs.

| Outil | Ce qu'il apporte |
| --- | --- |
| **Lighthouse** (DevTools, ligne de commande) | Scores et diagnostics : ressources bloquantes, CSS inutilisé, décalages de mise en page |
| Panneau **Performance** | Chronologie des tâches : événements *Recalculate Style*, *Layout*, *Paint*, *Composite* ; durée de chaque recalcul de styles |
| Panneau **Rendering** | Clignotement des zones repeintes (*paint flashing*), zones de décalage de mise en page, compteur d'images par seconde |
| Panneau **Layers** | Couches de composition et mémoire utilisée |
| Panneau **Coverage** | Part du CSS réellement utilisée par la page |
| **WebPageTest** | Mesures sur appareils et réseaux variés, avec film du chargement |

Pour mesurer de manière utile, on limite le processeur (ralentissement x4 ou x6) et le réseau (3G rapide) dans les DevTools afin de simuler un appareil modeste.

### 24.3 Mesurer sur le terrain

Les mesures de **terrain** (*field data*) proviennent de vrais utilisateurs ; elles reflètent la diversité des appareils et des réseaux. Deux sources principales : le rapport d'expérience utilisateur Chrome (CrUX), visible dans PageSpeed Insights, et vos propres mesures avec la bibliothèque `web-vitals`.

```js
import { onLCP, onCLS, onINP } from 'web-vitals';

function envoyer(metrique) {
    navigator.sendBeacon('/mesures', JSON.stringify({
        nom: metrique.name,           // LCP, CLS ou INP
        valeur: metrique.value,
        id: metrique.id,
        page: location.pathname,
    }));
}

onLCP(envoyer);
onCLS(envoyer);
onINP(envoyer);
```

On analyse les résultats au **75e centile** (la valeur que 75 % des visiteurs atteignent ou améliorent), ventilée par type d'appareil et par page. C'est ce chiffre, et non la moyenne, qui sert de référence aux seuils.

### 24.4 Budgets de performance

Un **budget de performance** est une limite chiffrée qu'on s'interdit de dépasser. Il transforme l'optimisation, souvent oubliée, en contrainte vérifiée à chaque changement.

| Budget | Exemple de repère | Outil de contrôle |
| --- | --- | --- |
| Poids du CSS (compressé) | À définir selon le projet ; viser le plus bas possible | `size-limit`, analyse du bundle |
| CSS critique intégré | Environ 14 Ko compressés (première fenêtre d'envoi réseau), repère indicatif | Contrôle dans le build |
| LCP, CLS, INP | Les seuils « bon » du tableau 24.1 | Lighthouse CI, web-vitals |
| Nombre de familles et de graisses de polices | Le moins possible | Revue, audit |

```js
// lighthouserc.js : le build échoue si un seuil est dépassé
export default {
    ci: {
        collect: { url: ['http://localhost:4173/'], numberOfRuns: 3 },
        assert: {
            assertions: {
                'categories:performance': ['error', { minScore: 0.9 }],
                'largest-contentful-paint': ['error', { maxNumericValue: 2500 }],
                'cumulative-layout-shift': ['error', { maxNumericValue: 0.1 }],
                'total-byte-weight': ['warn', { maxNumericValue: 500000 }],
            },
        },
    },
};
```

Les valeurs de l'exemple sont des points de départ : on fixe un budget d'après l'état mesuré du site et on le resserre progressivement.

### 24.5 Réduire le CSS inutilisé

Le CSS mort s'accumule avec le temps : composants supprimés dont les styles restent, règles dupliquées, bibliothèques importées en entier. Démarche :

1. **Mesurer** : panneau Coverage sur les pages principales, pour estimer la part inutilisée.
2. **Automatiser le retrait** : avec Tailwind, seules les classes utilisées sont générées ; avec les autres approches, des outils comme PurgeCSS retirent les sélecteurs introuvables dans le HTML et le JavaScript. Attention aux classes ajoutées dynamiquement, à lister explicitement pour éviter de les supprimer.
3. **Découper** : un fichier de CSS par page ou par route, chargé à la demande, plutôt qu'une feuille unique pour tout le site (chapitre 22).
4. **Importer finement** : ne charger que les composants d'une bibliothèque utilisés, pas la bibliothèque entière.
5. **Analyser** : visualiser le contenu des bundles pour repérer les gros contributeurs.

### 24.6 Une démarche d'optimisation continue

L'optimisation sans mesure produit des changements inutiles, voire nuisibles. La boucle recommandée :

1. **Mesurer** l'état initial (laboratoire et terrain).
2. **Identifier** le goulot : CSS bloquant, polices, image principale, recalcul de styles coûteux.
3. **Formuler une hypothèse** et ne changer **qu'une chose** à la fois.
4. **Remesurer** dans les mêmes conditions.
5. **Conserver ou annuler** selon le résultat, puis **verrouiller** le gain par un budget en intégration continue.

### 24.7 Pièges fréquents

| Piège | Conséquence | Parade |
| --- | --- | --- |
| Optimiser d'après le seul score Lighthouse | Gains artificiels sans effet réel | Croiser avec les données de terrain |
| Mesurer une seule fois | Variations confondues avec des progrès | Plusieurs exécutions, médiane |
| Mesurer sur une machine puissante | Problèmes invisibles | Limiter le processeur et le réseau |
| Supprimer du CSS « inutilisé » sans vérifier | Styles disparus d'états rares (erreur, vide, hors ligne) | Tester tous les états, lister les classes dynamiques |
| Budget jamais appliqué | Retour progressif à l'état initial | Échec du build en cas de dépassement |

### Synthèse du chapitre 24

Le CSS influe sur les trois **Core Web Vitals** : **LCP** (CSS bloquant, polices), **CLS** (dimensions manquantes, polices) et **INP** (recalculs coûteux déclenchés par une interaction). On combine **mesures de laboratoire** (Lighthouse, panneaux Performance, Rendering, Layers et Coverage, avec processeur et réseau limités) et **mesures de terrain** (CrUX, `web-vitals`, analysées au 75e centile). Des **budgets de performance** vérifiés en intégration continue empêchent les régressions. Le CSS inutilisé se retire par mesure, purge ciblée et découpage. La démarche reste toujours la même : **mesurer, émettre une hypothèse, changer une chose, remesurer, verrouiller**.

---

# Partie V — Essentiels

## 25. Compatibilité entre navigateurs

**Objectifs d'apprentissage.** Vous saurez situer la compatibilité des fonctionnalités grâce à Baseline, pratiquer l'amélioration progressive avec les replis et `@supports`, gérer les préfixes de fournisseurs, harmoniser les styles par défaut, tester sur plusieurs moteurs et définir une politique de support.

### 25.1 L'état des lieux

Trois moteurs de rendu dominent : **Blink** (Chrome, Edge et les navigateurs dérivés), **WebKit** (Safari) et **Gecko** (Firefox). Ils convergent grandement grâce à l'initiative **Interop**, par laquelle les éditeurs s'accordent chaque année sur des priorités de compatibilité. Le projet **Baseline** résume la disponibilité d'une fonctionnalité :

| Étiquette | Signification |
| --- | --- |
| **Newly available** | Disponible dans les **dernières versions** de tous les navigateurs majeurs |
| **Widely available** | Disponible depuis **au moins 30 mois** : utilisable sans précaution pour la plupart des sites |
| *Limited availability* | Pas encore dans tous les navigateurs : **amélioration progressive** |

Sources de référence : **MDN**, **caniuse.com**, **web.dev/baseline**.

### 25.2 Amélioration progressive et `@supports`

Le principe est d'écrire d'abord un style **de base qui fonctionne partout**, puis de l'**enrichir** pour les navigateurs capables. Cela s'appuie sur la tolérance aux erreurs de CSS : une déclaration incomprise est ignorée, et la précédente reste en vigueur.

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

`@supports` teste la prise en charge d'une **propriété avec une valeur** (`(display: grid)`), d'une **fonction** ou d'un **sélecteur** (`selector(...)`), avec les opérateurs `and`, `or` et `not`. Un navigateur qui ne connaît pas `@supports` ignore tout le bloc, ce qui est le comportement souhaité.

> **Attention.** Un sélecteur ou un bloc **invalide** invalide **toute la règle**. N'écrivez donc pas un sélecteur récent dans une liste commune avec un sélecteur ancien (`.a, :has-inconnu`) : si le navigateur ne comprend pas le second, il rejette aussi le premier. Utilisez `@supports selector(...)` ou écrivez des règles séparées.

L'essentiel est de vérifier que la version **sans** la fonctionnalité reste **utilisable et lisible**, pas qu'elle soit identique.

### 25.3 Préfixes de fournisseurs *(à jour)*

Les préfixes (`-webkit-`, `-moz-`, `-ms-`) servaient à proposer des fonctionnalités **expérimentales** avant leur standardisation. Les navigateurs ont **abandonné** cette pratique : les fonctionnalités expérimentales sont désormais activées par **drapeaux** et non par préfixes. Quelques préfixes restent courants :

| Préfixe encore utile | Usage |
| --- | --- |
| `-webkit-line-clamp` (avec `-webkit-box`) | Troncature multiligne |
| `-webkit-text-size-adjust` | Mobile |
| `-webkit-background-clip: text` | Texte dégradé |
| `-webkit-backdrop-filter` | Anciennes versions de Safari |
| `-webkit-mask-*` | Anciennes versions |

**Ne les écrivez pas à la main** : laissez **Autoprefixer** ou **Lightning CSS** (selon `browserslist`) les ajouter, et retirer ceux qui ne sont plus nécessaires.

### 25.4 Réinitialisation et styles par défaut

Chaque navigateur applique sa **feuille de style par défaut**, avec des différences (marges, tailles, apparence des champs). Un **reset** (chapitre 19) ou **normalize** les harmonise. Pour les formulaires, on utilise `font: inherit` pour que les champs reprennent la police de la page, et `appearance: none` avec prudence (on perd l'apparence native, donc il faut tout restyler, y compris le focus).

### 25.5 Tester

- **DevTools** : émulation des préférences (`prefers-*`), mode appareil.
- **Navigateurs réels** : Chrome, Firefox, Safari (macOS **et iOS** : indispensable, car tous les navigateurs iOS utilisent WebKit), Edge.
- **Services** : BrowserStack, LambdaTest ; **Playwright** pour des tests visuels multi-moteurs automatisés.
- **Stylelint** avec `stylelint-no-unsupported-browser-features` : signale les fonctionnalités non prises en charge par votre `browserslist`.

### 25.6 Navigateurs anciens

- Définissez une **politique de support** (`browserslist`) fondée sur vos **statistiques d'audience** réelles, et non sur des habitudes.
- **Internet Explorer** est abandonné (fin de support en 2022) : ne le prenez plus en charge.
- Pour les navigateurs anciens, visez un **repli lisible** plutôt qu'un rendu identique : c'est le principe de l'**amélioration progressive**.

### Synthèse du chapitre 25

- Baseline : *newly available* (récent), *widely available* (30 mois et plus), *limited* (partiel).
- Replis par déclaration multiple, `@supports` pour les blocs ; un sélecteur invalide invalide la règle.
- Les préfixes se gèrent par outil ; testez sur de vrais navigateurs, dont Safari iOS.
- Une politique de support basée sur vos données, et un repli lisible.

---

## 26. CSS et JavaScript

**Objectifs d'apprentissage.** Vous saurez modifier et lire les styles depuis JavaScript, passer des valeurs au CSS par les variables, interroger les requêtes média et la prise en charge des fonctionnalités, piloter des animations, créer des feuilles de style dynamiques et manipuler dialogues et popovers.

### 26.1 Modifier les styles

```js
const el = document.querySelector('.carte');              // suppose un <div class='carte'> dans la page

// 1) Classes (méthode recommandée : le CSS reste dans la feuille de style)
el.classList.add('active');
el.classList.remove('cachee');
el.classList.toggle('ouverte');
console.log(el.classList.contains('active'));             // true
el.classList.replace('active', 'inactive');

// 2) Style en ligne (valeurs dynamiques)
el.style.color = 'tomato';
el.style.backgroundColor = 'rgb(0 0 0 / .1)';             // camelCase
el.style.cssText = 'color: red; margin: 0;';
el.style.removeProperty('color');

// 3) Variables CSS (idéal pour passer des valeurs dynamiques au CSS)
el.style.setProperty('--progression', '70%');
document.documentElement.style.setProperty('--couleur-principale', 'tomato');
```

```css
.barre { width: var(--progression, 0%); transition: width .3s; }
```

Trois méthodes, par ordre de préférence : **basculer des classes** (le CSS décide de l'apparence, JavaScript décide de l'état), **écrire des variables CSS** (JavaScript fournit une valeur, le CSS la met en forme), et seulement en dernier recours **écrire directement dans `style`**. Les propriétés CSS s'écrivent en **camelCase** dans `style` (`backgroundColor`).

### 26.2 Lire les styles

```js
const el = document.querySelector('.carte');
const styles = getComputedStyle(el);                      // valeurs CALCULÉES (lecture seule)

console.log(styles.getPropertyValue('--couleur-principale'));
console.log(styles.width);                                // '320px'
console.log(el.getBoundingClientRect());                  // position et taille à l'écran
console.log(el.offsetWidth, el.clientHeight, el.scrollHeight);
```

`getComputedStyle` renvoie les valeurs **calculées** après application de toute la cascade (lecture seule) ; `getBoundingClientRect()` donne le rectangle réel de l'élément à l'écran ; `offsetWidth`, `clientHeight` et `scrollHeight` décrivent des dimensions de boîte et de contenu.

> **Attention.** Lire des dimensions puis modifier le style **en boucle** force le navigateur à recalculer la mise en page à chaque tour (*layout thrashing*). Regroupez d'abord toutes les lectures, puis toutes les écritures, ou utilisez `requestAnimationFrame`.

### 26.3 Requêtes média et fonctionnalités en JavaScript

```js
function appliquerTheme(theme) {
    document.documentElement.dataset.theme = theme;
}

const sombre = matchMedia('(prefers-color-scheme: dark)');
appliquerTheme(sombre.matches ? 'sombre' : 'clair');
sombre.addEventListener('change', (e) => appliquerTheme(e.matches ? 'sombre' : 'clair'));

console.log(matchMedia('(prefers-reduced-motion: reduce)').matches);
console.log(CSS.supports('display', 'grid'));             // true ou false
console.log(CSS.supports('selector(:has(*))'));
```

`matchMedia` évalue une requête média en JavaScript : sa propriété `matches` indique si elle est vraie, et l'événement `change` signale une évolution (l'utilisateur bascule en thème sombre). `CSS.supports` est l'équivalent JavaScript de `@supports`.

### 26.4 Animations en JavaScript

```js
const el = document.querySelector('.carte');

// Web Animations API : les mêmes moteurs que les animations CSS, pilotables par JavaScript
const animation = el.animate(
    [{ transform: 'translateY(20px)', opacity: 0 }, { transform: 'none', opacity: 1 }],
    { duration: 400, easing: 'ease-out', fill: 'both' },
);
animation.pause(); animation.play(); animation.reverse();
animation.finished.then(() => console.log('terminé'));

el.addEventListener('transitionend', () => console.log('fin d\'une transition CSS'));
el.addEventListener('animationend', () => console.log('fin d\'une animation CSS'));
```

La **Web Animations API** (`element.animate`) offre un contrôle complet (pause, inversion, lecture, promesse de fin) sur des animations exécutées par le même moteur que celles du CSS, donc aussi performantes. Autres outils utiles : `IntersectionObserver` (déclencher selon la visibilité), `ResizeObserver` (réagir aux changements de taille), `requestAnimationFrame` et `document.startViewTransition()`.

### 26.5 Feuilles de style dynamiques

```js
const feuille = new CSSStyleSheet();
feuille.replaceSync('.nouveau { color: red; }');
document.adoptedStyleSheets = [...document.adoptedStyleSheets, feuille];        // partageable avec les Shadow DOM

CSS.registerProperty({ name: '--angle', syntax: '<angle>', inherits: false, initialValue: '0deg' });   // équivalent de @property
```

Les **feuilles constructibles** (`new CSSStyleSheet()`) se créent en JavaScript et s'adoptent dans un document ou un Shadow DOM, ce qui permet de **partager** une même feuille entre plusieurs composants web. `CSS.registerProperty` est l'équivalent JavaScript de `@property` : n'enregistrez une propriété qu'une seule fois (la règle `@property` ne doit pas déjà l'avoir fait).

### 26.6 Dialogues, popovers et état en HTML

Le HTML moderne gère déjà l'ouverture et la fermeture, le focus et la couche supérieure : le CSS se contente de **styler** les états (`:modal`, `:popover-open`, `[open]`).

```js
const dialogue = document.querySelector('#modale');       // <dialog id='modale'> (voir 28.3)
const menu = document.querySelector('#menu');             // <ul id='menu' popover> (voir 28.4)

dialogue.showModal();
dialogue.close();
menu.togglePopover();
menu.showPopover();
menu.hidePopover();
```

### 26.7 Bonnes pratiques

- **Basculer des classes** plutôt que manipuler `style` directement.
- Utiliser les **variables CSS** comme **interface** entre JavaScript et CSS.
- Préférer les **animations CSS ou WAAPI** aux animations par `setInterval`.
- Respecter `prefers-reduced-motion` dans le code JavaScript aussi.

### Synthèse du chapitre 26

- Classes pour l'état, variables pour les valeurs, `style` en dernier recours.
- `getComputedStyle` lit les valeurs calculées ; évitez de mêler lectures et écritures en boucle.
- `matchMedia`, `CSS.supports` et la Web Animations API prolongent le CSS en JavaScript.
- Dialogues et popovers HTML gèrent focus et couche supérieure ; le CSS ne fait que les styler.

---

## 27. Outils de développement

**Objectifs d'apprentissage.** Vous saurez utiliser les DevTools du navigateur pour inspecter, modifier et déboguer un style, diagnostiquer les problèmes de mise en page courants, équiper votre éditeur et retrouver les ressources de référence.

### 27.1 Les DevTools du navigateur (F12)

| Panneau ou outil | Usage |
| --- | --- |
| **Éléments**, onglet **Styles** | Voir et **modifier en direct** les règles appliquées ; les déclarations **barrées** sont surchargées |
| **Calculé** (*Computed*) | Valeur **finale** de chaque propriété et règle d'origine |
| **Modèle de boîte** | Visualisation des marges, bordures et paddings |
| **Superpositions Flexbox et Grid** | Badges `flex` et `grid` dans l'arbre DOM : affichage des axes, lignes, zones, gouttières |
| **Conteneurs** | Badge `container` : conteneurs de requêtes et leur taille |
| **Couches** (*Layers*) | Ordre des couches de cascade |
| **Sélecteur d'état** (`:hov`) | Forcer `:hover`, `:focus`, `:active`, `:focus-visible`… |
| **Rendu** (*Rendering*) | **Émuler** `prefers-color-scheme`, `prefers-reduced-motion`, `forced-colors`, les déficiences de vision des couleurs, `print` |
| **Appareils** (Ctrl+Maj+M) | Mode responsive, capteurs, réseau |
| **Animations** | Inspecter et ralentir animations et transitions |
| **Couverture** (*Coverage*) | Pourcentage de **CSS inutilisé** |
| **Performance, Lighthouse** | Mesures de rendu et Core Web Vitals |
| **Accessibilité** | Arbre d'accessibilité, contraste |

#### Astuces

- **Ctrl+clic** sur une propriété dans le panneau Styles : aller à sa définition.
- **Clic sur un nuancier** : sélecteur de couleur avec vérification du **contraste**.
- Éditeurs visuels d'**ombres**, de **dégradés** et de **courbes d'animation** (`cubic-bezier`, `linear()`).
- Ajouter une règle de test : bouton « + » (nouvelle règle de style) ; menu *Copier, puis Copier le style*.
- Les modifications faites dans les DevTools **ne sont pas enregistrées** : reportez-les dans votre code (ou activez les **Espaces de travail**).

### 27.2 Débogage de la mise en page

```css
/* Contour temporaire pour visualiser les boîtes */
* { outline: 1px solid rgb(255 0 0 / .3); }
```

| Symptôme | Pistes |
| --- | --- |
| Style non appliqué | Sélecteur incorrect, **spécificité**, ordre, faute de frappe (propriété barrée dans *Styles*) |
| Élément qui « déborde » | `box-sizing`, `min-width: 0` (flex), largeur fixe |
| Marges étranges | **Fusion de marges**, `display` de l'élément |
| `z-index` sans effet | **Contexte d'empilement**, `position` manquant |
| `sticky` ne colle pas | `top` manquant, ancêtre avec `overflow` |
| Hauteur 100 % inopérante | La hauteur du parent doit être définie (ou `min-height: 100dvh`, Flexbox ou Grid) |

Le contour temporaire sur `*` est préférable à `border` pour le débogage car il ne modifie pas la taille des boîtes.

### 27.3 Éditeurs et extensions

| Outil | Apport |
| --- | --- |
| **VS Code** | Complétion CSS, aperçu des couleurs, **Emmet** (`div.carte>h2+p` puis Tab), Live Server |
| **Stylelint** | Analyse et corrections automatiques |
| **Prettier** | Formatage |
| **Tailwind CSS IntelliSense** | Complétion pour Tailwind |
| **CSS Peek**, **Intellisense for CSS class names** | Navigation entre HTML et CSS |
| **Can I use** (dans l'éditeur) | Compatibilité |

### 27.4 Ressources utiles

- **MDN Web Docs** : référence complète de CSS.
- **web.dev/learn/css** : cours gratuit de Google.
- **caniuse.com** et **web.dev/baseline** : compatibilité.
- **CSS-Tricks**, **Every Layout**, **Modern CSS Solutions**, **modern-css.com**.
- **MDN Browser Compatibility Data** : données de compatibilité réutilisables.

### Synthèse du chapitre 27

- Les DevTools permettent d'inspecter, d'émuler les préférences, de visualiser Flexbox, Grid et conteneurs, et de mesurer le CSS inutilisé.
- Face à un bug : vérifier sélecteur, spécificité, validité, puis contexte d'empilement, débordement et fusion de marges.
- Les modifications des DevTools sont temporaires : reportez-les dans le code.

---

## 28. Composants et projets

**Objectifs d'apprentissage.** Vous saurez réaliser les composants d'interface les plus courants en combinant tout ce qui précède : carte, bouton, modale, menu, accordéon, interrupteur, carrousel, navigation, mise en page de page ; et choisir des projets de difficulté croissante pour vous exercer. Chaque composant privilègie les fonctionnalités natives du HTML et du CSS, plus accessibles que des solutions bricolées.

### 28.1 Carte

```html
<article class='carte'>
    <img src='photo.jpg' alt='Description' width='400' height='250'>
    <div class='carte__corps'>
        <h2>Titre</h2>
        <p>Un court résumé de la carte.</p>
        <a class='bouton' href='#'>Lire la suite</a>
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

Ce composant réutilise : la grille pour disposer image et corps, `overflow: hidden` pour rogner l'image aux coins arrondis, `aspect-ratio` et `object-fit` pour un cadrage constant, des ombres multiples pour la profondeur, une transition sur `transform` (performante), l'imbrication native et une variable locale. `Canvas` est une couleur système qui suit le thème clair ou sombre.

### 28.2 Bouton

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
    &[disabled], &[aria-disabled='true'] { opacity: .5; cursor: not-allowed; }
    &.danger { --fond: crimson; }
}
```

Points à retenir : une variable `--fond` unique dont dérivent l'état de survol (`color-mix`), l'anneau de focus et les variantes (`.danger` ne redéfinit que la variable) ; des unités en `em` pour que le bouton s'adapte à sa taille de texte ; `font: inherit` car un `<button>` n'hérite pas de la police par défaut ; un focus visible ; un état désactivé pour `disabled` et `aria-disabled`.

### 28.3 Modale avec `<dialog>`

```html
<button onclick="document.querySelector('#modale').showModal()">Ouvrir</button>

<dialog id='modale'>
    <h2>Confirmer</h2>
    <p>Voulez-vous continuer ?</p>
    <form method='dialog'><button>Annuler</button><button value='ok'>OK</button></form>
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

> `<dialog>` avec `showModal()` fournit **gratuitement** : le piégeage du focus, la fermeture avec Échap, un fond inerte et la **couche supérieure** (aucun `z-index` n'est nécessaire). Un formulaire `method='dialog'` ferme la boîte et renvoie la valeur du bouton pressé.

L'animation d'ouverture et de fermeture combine `@starting-style` (état de départ), `allow-discrete` sur `display` et `overlay` (pour que la boîte reste affichée pendant la sortie) et la pseudo-classe `:has()` pour bloquer le défilement de la page.

### 28.4 Menu déroulant avec `popover` et ancrage

```html
<button popovertarget='menu' id='declencheur'>Menu</button>
<ul id='menu' popover>
    <li><a href='#'>Profil</a></li>
    <li><a href='#'>Paramètres</a></li>
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

L'attribut `popover` rend l'élément ouvrable et fermable par le bouton qui le cible (`popovertarget`), avec fermeture par Échap ou par clic extérieur et affichage en couche supérieure. L'ancrage place le menu sous le bouton et le retourne s'il n'y a pas de place.

**Menu en CSS seul (technique classique) :**

```css
.deroulant { position: relative; }
.deroulant .menu { display: none; position: absolute; inset-block-start: 100%; }
.deroulant:hover .menu,
.deroulant:focus-within .menu { display: block; }          /* :focus-within : accessible au clavier */
```

> **Accessibilité.** `:hover` seul **n'est pas accessible** au clavier ni au tactile : combinez-le avec `:focus-within`, ou préférez `popover` ou `<details>`.

### 28.5 Accordéon avec `<details>`

```html
<details name='faq' open><summary>Question 1</summary><p>Réponse 1</p></details>
<details name='faq'><summary>Question 2</summary><p>Réponse 2</p></details>    <!-- même name : un seul ouvert à la fois -->
```

```css
details { border-block-end: 1px solid #ddd; }
summary { cursor: pointer; padding: .75rem 0; font-weight: 600; list-style: none; }
summary::after { content: '+'; float: right; }
details[open] summary::after { content: '−'; }
details::details-content { transition: height .3s, content-visibility .3s allow-discrete; height: 0; overflow: clip; }
details[open]::details-content { height: auto; }               /* avec interpolate-size: allow-keywords (Chromium) */
```

`<details>` et `<summary>` fournissent l'accordéon **sans JavaScript** et avec le clavier. Des éléments `<details>` portant le même attribut `name` forment un groupe exclusif. Le pseudo-élément `::details-content` permet d'animer l'ouverture (support à vérifier).

### 28.6 Interrupteur (case à cocher stylisée)

```html
<label class='interrupteur'><input type='checkbox' role='switch'><span>Notifications</span></label>
```

```css
.interrupteur input {
    appearance: none; inline-size: 2.75rem; block-size: 1.5rem; border-radius: 1rem;
    background: #bbb; position: relative; cursor: pointer; transition: background .2s;

    &::after { content: ''; position: absolute; inset: 2px auto 2px 2px; aspect-ratio: 1; border-radius: 50%; background: white; transition: translate .2s; }
    &:checked { background: royalblue; }
    &:checked::after { translate: 1.25rem 0; }
    &:focus-visible { outline: 3px solid royalblue; outline-offset: 2px; }
}
```

On conserve une **vraie case à cocher** (accessibilité et formulaires gratuits) dont on retire l'apparence native avec `appearance: none`, puis on dessine la piste et le curseur. `:checked` déplace le curseur par `translate`. Le rôle `switch` indique aux technologies d'assistance qu'il s'agit d'un interrupteur.

### 28.7 Carrousel avec accroche de défilement (*scroll snap*)

```html
<div class='carrousel' tabindex='0' aria-label='Galerie'>
    <figure><img src='1.jpg' alt='…'></figure>
    <figure><img src='2.jpg' alt='…'></figure>
    <figure><img src='3.jpg' alt='…'></figure>
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

> Cette approche (défilement **natif**, au toucher comme au clavier) est **plus accessible** que l'ancienne technique des boutons radio avec `:checked`. Chromium propose en plus des **pseudo-éléments de carrousel** (`::scroll-button()`, `::scroll-marker`) pour créer boutons et pastilles **sans JavaScript** (support partiel : à vérifier).

Le `tabindex='0'` rend la zone défilable au clavier, et `aria-label` la nomme. Pensez à `scroll-behavior: auto` sous `prefers-reduced-motion`.

### 28.8 Barre de navigation responsive

```css
.nav { display: flex; flex-wrap: wrap; align-items: center; gap: 1rem; padding: 1rem; }
.nav ul { display: flex; gap: 1rem; list-style: none; padding: 0; margin: 0; margin-inline-start: auto; }
.nav a { padding: .5rem; text-decoration: none; }
.nav a[aria-current='page'] { font-weight: 700; text-decoration: underline; text-underline-offset: .3em; }

@media (max-width: 40rem) { .nav ul { flex-direction: column; width: 100%; margin: 0; } }
```

L'attribut `aria-current='page'` sert à la fois de signal pour les technologies d'assistance et de crochet de style pour la page courante : le CSS s'appuie sur l'état sémantique plutôt que sur une classe supplémentaire.

### 28.9 Mise en page de page complète

```css
body { display: grid; grid-template-rows: auto 1fr auto; min-height: 100dvh; }

.contenu {
    display: grid;
    grid-template-columns: [plein-debut] minmax(1rem, 1fr) [contenu-debut] minmax(0, 65ch) [contenu-fin] minmax(1rem, 1fr) [plein-fin];
}
.contenu > * { grid-column: contenu; }
.contenu > .pleine-largeur { grid-column: plein; }         /* éléments qui dépassent la colonne de lecture */
```

Cette technique de **grille nommée** crée une colonne de lecture centrée (65 caractères) bordée de marges flexibles. Les lignes `contenu-debut` et `contenu-fin` définissent implicitement une zone nommée `contenu` ; les éléments qui doivent déborder (image pleine largeur, bandeau) se placent sur la zone `plein`.

### 28.10 Projets suggérés

| Niveau | Projet | Compétences |
| --- | --- | --- |
| Débutant | **Page de présentation ou CV** | Typographie, boîte, Flexbox, variables |
| Débutant | **Carte de profil et galerie** | Grid, `aspect-ratio`, survols, transitions |
| Intermédiaire | **Portfolio responsive** | Grid, mobile d'abord, requêtes de conteneur, thème sombre (`light-dark`) |
| Intermédiaire | **Tableau de bord** | Grid et subgrid, composants, tableaux responsives |
| Intermédiaire | **Système de design** (tokens, boutons, formulaires, modale, `@layer`) | Architecture, variables, accessibilité |
| Avancé | **Page d'atterrissage animée** (sans JavaScript) | `@keyframes`, animations liées au défilement, `@starting-style`, transitions de vue |
| Avancé | **Bibliothèque de composants** (accordéon, onglets, carrousel, infobulles ancrées) | `popover`, ancrage, `:has()`, `@scope` |
| Avancé | **Reproduire une interface existante** (au pixel près, responsive) | Analyse, Grid et Flexbox, précision |

Pour chaque projet : commencez par le HTML sémantique sans style, écrivez ensuite le CSS mobile d'abord, puis testez au clavier, en mode sombre, avec zoom à 200 % et mouvement réduit.

### Synthèse du chapitre 28

- Préférez les éléments natifs (`<dialog>`, `popover`, `<details>`, case à cocher) : ils apportent focus, clavier et accessibilité.
- Une variable locale pilote les variantes d'un composant.
- Chaque composant est à tester au clavier, en thème sombre, au zoom et en mouvement réduit.

---

## 29. Internationalisation et CSS

**Objectifs d'apprentissage.** Vous saurez concevoir des interfaces qui fonctionnent dans plusieurs langues et plusieurs sens d'écriture : adapter la mise en page aux langues écrites de droite à gauche avec les propriétés logiques, gérer les modes d'écriture verticaux, choisir des polices et une typographie adaptées à chaque langue, absorber la variation de longueur des textes traduits et utiliser les compteurs et styles de numérotation locaux.

### 29.1 Les enjeux

Une interface internationalisée doit gérer trois dimensions que le CSS n'aborde pas toutes seul. La **langue** et la **direction** se déclarent dans le **HTML** (`<html lang='ar' dir='rtl'>`) : le CSS s'appuie sur ces attributs pour adapter la présentation. La **mise en page** doit supporter le miroir (droite à gauche), les écritures verticales et des textes de longueurs très variables. La **typographie** doit couvrir les écritures utilisées (latin, arabe, hébreu, devanagari, chinois, japonais, coréen, thaï, etc.).

Ces questions se préparent dès la conception : adapter après coup une interface écrite avec des propriétés physiques (`margin-left`, `float: right`) est long et source d'erreurs.

### 29.2 Droite à gauche (RTL) et propriétés logiques

Pour l'arabe, l'hébreu, le persan ou l'ourdou, le sens de lecture est inversé : la navigation, les marges, les icônes de direction et l'alignement du texte doivent être en miroir. Les **propriétés logiques** (chapitre 6) rendent cette adaptation automatique : elles se réfèrent au **début** et à la **fin** de la ligne (`inline-start`, `inline-end`) et non à la gauche et à la droite.

```css
.carte {
    padding-inline: 1rem;                      /* gauche + droite, inversé en RTL */
    margin-inline-start: auto;                 /* côté du début de ligne */
    border-inline-start: 4px solid tomato;     /* barre à gauche en LTR, à droite en RTL */
    text-align: start;                         /* au lieu de left */
    inset-inline-end: 0;                       /* au lieu de right: 0 */
}

.fleche-suivant { }
:dir(rtl) .fleche-suivant { transform: scaleX(-1); }   /* retourne l'icône en RTL */
```

Certaines technologies de mise en page se retournent d'elles-mêmes : l'ordre des éléments d'un conteneur **Flexbox** (`flex-direction: row`) et des colonnes d'une **grille** s'inverse automatiquement en RTL. En revanche, plusieurs propriétés restent **physiques** et doivent être traitées à part :

| S'inverse automatiquement | Ne s'inverse pas : à adapter |
| --- | --- |
| Ordre des éléments Flexbox et Grid | `margin-left`, `padding-right`, `float: left`, `text-align: left` (propriétés physiques) |
| Propriétés logiques (`margin-inline-start`, etc.) | `background-position: left`, dégradés `to right` |
| `text-align: start` et `end` | Décalages de `transform: translateX()`, ombres `box-shadow` décalées horizontalement |
| Sens de défilement et alignement du texte par défaut | Icônes directionnelles (flèches, « précédent » et « suivant ») |

Pour le texte lui-même, le navigateur applique l'**algorithme bidirectionnel d'Unicode** : un nom latin au milieu d'une phrase arabe s'affiche correctement sans intervention. On évite d'utiliser `direction` et `unicode-bidi` en CSS pour fixer le sens du contenu : on préfère l'attribut HTML `dir`, y compris `dir='auto'` pour du contenu saisi par les utilisateurs. La pseudo-classe `:dir(rtl)` permet de cibler les éléments selon leur direction.

### 29.3 Modes d'écriture

Le japonais, le chinois et le mongol peuvent s'écrire verticalement. `writing-mode` définit le sens d'empilement des lignes ; les propriétés logiques suivent automatiquement (l'axe **inline** devient vertical).

```css
.colonne-japonaise {
    writing-mode: vertical-rl;                 /* lignes verticales, de droite à gauche */
    text-orientation: mixed;                   /* caractères latins couchés, idéogrammes droits */
}
.date-verticale { text-combine-upright: all; } /* regroupe des chiffres sur un seul caractère de large */
```

`inline-size` et `block-size` remplacent alors `width` et `height` : une boîte à `inline-size: 20rem` s'étend dans le sens de la lecture, quel que soit le mode. Ces modes servent aussi à des effets de titres couchés en écriture latine, à utiliser avec discernement pour la lisibilité.

### 29.4 Typographie multilingue

Une police ne couvre pas toutes les écritures : si un caractère manque, le navigateur utilise une police de repli, parfois de style très différent. Le CSS permet de choisir la bonne police **selon la langue**.

```css
:lang(ja) { font-family: 'Noto Sans JP', sans-serif; line-height: 1.8; }
:lang(ar) { font-family: 'Noto Naskh Arabic', serif; line-height: 1.9; }
:lang(th) { line-height: 1.8; }                 /* glyphes hauts : interligne plus généreux */

q { quotes: '«' '»'; }                          /* guillemets français */
:lang(de) q { quotes: '„' '“'; }                /* guillemets allemands */
:lang(en) q { quotes: '“' '”'; }                /* guillemets anglais */

:lang(ko) { word-break: keep-all; }             /* ne coupe pas les mots coréens au milieu */
```

Règles à retenir :

- **La langue conditionne plusieurs comportements** : la césure (`hyphens: auto` exige un attribut `lang` correct), la transformation de casse (`text-transform: uppercase` sait que le « i » turc devient « İ » si la langue est déclarée), le choix des guillemets, les ligatures et l'espacement.
- **Interlignes** : les écritures à glyphes hauts (thaï, devanagari, arabe) demandent un `line-height` plus généreux que le latin.
- **Sous-ensembles de polices** : `unicode-range` dans `@font-face` (chapitre 7) permet de ne télécharger la police d'une écriture que si elle est utilisée.
- **Italique et gras** : de nombreuses écritures (arabe, chinois, hébreu) n'ont pas d'italique ; évitez de l'appliquer systématiquement et évitez le gras synthétique en réglant `font-synthesis` si besoin.
- **Polices système** : `system-ui` fournit souvent une police de bonne qualité pour l'écriture de l'utilisateur, sans téléchargement.

### 29.5 Absorber la variation de longueur des textes

Un texte traduit est rarement de la même longueur que l'original : l'allemand et le finnois sont souvent nettement plus longs que l'anglais ; le chinois et le japonais plus courts mais plus hauts. Une interface construite avec des largeurs ou hauteurs fixes déborde ou se tronque.

- **Pas de dimensions fixes** sur les conteneurs de texte : `min-height` plutôt que `height`, `max-width` plutôt que `width`.
- **Mise en page flexible** : Flexbox avec `flex-wrap`, Grid avec `minmax()`, requêtes de conteneur.
- **Unités relatives au texte** : `ch`, `em` et `rem` suivent la taille des caractères.
- **Retours à la ligne** : `overflow-wrap`, `hyphens: auto`, `text-wrap: balance` pour des titres équilibrés quelle que soit la langue.
- **Pseudo-localisation** : pour tester sans attendre les traductions, remplacer temporairement les textes par des versions artificiellement allongées (jusqu'à +40 %) et accentuées, afin de repérer les débordements.

### 29.6 Numérotation, compteurs et contenu généré

Les listes et compteurs CSS savent utiliser des systèmes de numérotation locaux.

```css
ol.arabe { list-style: arabic-indic; }               /* ١. ٢. ٣. */
ol.romain { list-style: lower-roman; }

@counter-style chiffres-persans {
    system: numeric;
    symbols: '۰' '۱' '۲' '۳' '۴' '۵' '۶' '۷' '۸' '۹';
    suffix: '. ';
}
ol.persan { list-style: chiffres-persans; }

h2 { counter-increment: section; }
h2::before { content: counter(section, upper-roman) '. '; }
```

Le contenu généré par `content` est **dépendant de la langue** : une chaîne écrite dans le CSS n'est pas traduite avec le reste de l'interface. On évite donc d'y placer du texte porteur de sens (chapitre 2) ; on préfère `attr()` pour reprendre un attribut HTML traduit, ou on génère le contenu dans le HTML.

### 29.7 Pièges fréquents

| Piège | Conséquence | Parade |
| --- | --- | --- |
| `margin-left`, `float: right`, `text-align: left` | Interface cassée en RTL | Propriétés logiques et `start`, `end` |
| Icônes de direction non retournées | Sens de navigation contradictoire en RTL | `:dir(rtl)` avec `scaleX(-1)` |
| Attribut `lang` absent ou erroné | Césure, casse, guillemets et polices incorrects | Déclarer la langue sur `<html>` et sur les passages dans une autre langue |
| Hauteurs fixes sur du texte | Débordement dans les langues longues | `min-height`, mise en page flexible |
| Texte généré par `content` | Non traduit | HTML ou `attr()` |
| Une seule police pour toutes les écritures | Repli de qualité variable | Piles de polices selon `:lang()` |

### Synthèse du chapitre 29

L'internationalisation repose sur la **déclaration de la langue et de la direction dans le HTML** (`lang`, `dir`) et sur des **propriétés logiques** qui font suivre la mise en page au **sens d'écriture** : Flexbox et Grid se retournent seuls en RTL, mais les propriétés physiques, les dégradés directionnels et les icônes doivent être traités. Les **modes d'écriture** (`writing-mode`) gèrent l'écriture verticale, la typographie s'adapte par `:lang()` (polices, interlignes, guillemets, `word-break`), et la mise en page absorbe la **variation de longueur** des traductions grâce à des dimensions flexibles, vérifiées par pseudo-localisation. Les compteurs et styles de liste locaux (`@counter-style`) complètent le dispositif ; le texte porteur de sens reste dans le HTML.

---

## 30. Sécurité et CSS

**Objectifs d'apprentissage.** Vous saurez identifier les risques de sécurité et de confidentialité liés au CSS, protéger une application contre l'injection de styles, configurer une politique de sécurité de contenu (CSP) pour les feuilles de style, réduire les risques de détournement de clics, intégrer des feuilles de style tierces de façon sûre et appliquer une liste de contrôle de sécurité.

### 30.1 Le CSS comme surface d'attaque

On pense rarement au CSS comme à une surface d'attaque : il ne s'exécute pas comme du code. Il peut pourtant servir des attaques réelles, et on doit connaître les familles de risques pour s'en prémunir (cette section est **défensive** : elle décrit les mécanismes pour mieux les contrer).

| Risque | Principe | Contre-mesure principale |
| --- | --- | --- |
| **Injection de CSS** | Du CSS fourni par un utilisateur (ou une URL) est inséré dans la page : il peut masquer ou falsifier l'interface, ou déclencher des requêtes réseau conditionnelles (par exemple selon la valeur d'un attribut) qui révèlent des informations | Ne jamais construire du CSS à partir d'une saisie ; CSP |
| **Détournement de clic** (*clickjacking*) | Une page malveillante superpose un cadre invisible sur un faux contenu pour tromper l'utilisateur | `frame-ancestors`, en-têtes de protection |
| **Hameçonnage visuel** | Un contenu injecté imite l'interface (faux bouton, faux formulaire) grâce à une mise en page absolue | Assainissement du contenu, CSP |
| **Fuite de confidentialité** | Requêtes vers des serveurs tiers (polices, images de fond), empreinte des préférences et des polices | Héberger soi-même, limiter les sources, CSP |
| **Chaîne d'approvisionnement** | Feuille de style ou paquet tiers compromis | Épinglage de version, intégrité de sous-ressource |

La gravité varie : une injection de CSS ne permet pas d'exécuter du JavaScript, mais elle peut suffire à **dégrader** l'interface ou à **extraire des données** dans certains contextes, ce qui justifie de la traiter sérieusement.

### 30.2 La politique de sécurité de contenu (CSP)

La **CSP** est un en-tête de réponse HTTP qui limite les ressources que la page peut charger et exécuter. Plusieurs directives concernent le CSS.

```text
Content-Security-Policy:
    default-src 'self';
    style-src 'self' 'nonce-4f9a2c1e';
    img-src 'self' data:;
    font-src 'self';
    frame-ancestors 'self'
```

| Directive | Rôle |
| --- | --- |
| `style-src` | Sources autorisées pour les feuilles de style (fichiers et balises `<style>`) |
| `style-src-elem`, `style-src-attr` | Distinguent les balises `<style>` et `<link>` des attributs `style` |
| `img-src`, `font-src` | Sources des images (dont les arrière-plans CSS) et des polices : limiter ces sources restreint aussi les requêtes réseau déclenchées depuis le CSS |
| `frame-ancestors` | Sites autorisés à intégrer votre page dans un cadre (protection contre le détournement de clic) |
| `'nonce-…'` ou empreinte (`'sha256-…'`) | Autorise une balise `<style>` précise sans `'unsafe-inline'` |
| `'unsafe-inline'` | Autorise tout CSS en ligne : **à éviter** |

La CSP pousse naturellement vers de **bonnes pratiques** déjà recommandées : feuilles externes plutôt que styles en ligne, pas d'attributs `style` pour l'apparence (on transmet les valeurs dynamiques par des **variables CSS** posées par JavaScript, voir chapitre 26, qui est compatible avec une CSP stricte lorsque la modification passe par l'API `style.setProperty`).

### 30.3 Se protéger de l'injection de styles

Règle de base : **ne jamais fabriquer de CSS à partir d'une donnée non fiable** (saisie, paramètre d'URL, champ de base de données, contenu importé).

```js
const THEMES = new Set(['clair', 'sombre', 'contraste']);

function appliquerTheme(nom) {
    if (!THEMES.has(nom)) return;                      // liste blanche : seules les valeurs prévues passent
    document.documentElement.dataset.theme = nom;      // le CSS reste dans la feuille de style
}

function definirAccent(valeur) {
    if (!/^#[0-9a-f]{6}$/i.test(valeur)) return;       // format strictement validé
    document.documentElement.style.setProperty('--accent', valeur);
}

const cible = document.querySelector('#' + CSS.escape(identifiant));   // échappe un identifiant venant de l'extérieur
```

- **Préférer les listes blanches** : un thème est un nom parmi quelques-uns, pas un fragment de CSS.
- **Valider le format** des valeurs libres (couleur, nombre) avant de les affecter à une variable.
- **Échapper** avec `CSS.escape()` tout identifiant ou classe inséré dans un sélecteur.
- **Assainir le contenu riche** (éditeurs, commentaires, courriels) avec une bibliothèque dédiée comme DOMPurify, qui retire les balises `<style>` et les attributs `style` non souhaités.
- **Thèmes fournis par les utilisateurs** : les décrire comme des **jeux de variables** validées, pas comme des feuilles de style libres, ou les isoler dans un `<iframe sandbox>` ou un Shadow DOM.

### 30.4 Détournement de clic et mise en page trompeuse

Le **clickjacking** exploite l'intégration d'une page légitime dans un cadre invisible (opacité nulle, superposition) au-dessus d'un faux contenu. Le CSS de la page attaquante fait le piège ; la défense appartient à **votre** page, via les en-têtes :

```text
Content-Security-Policy: frame-ancestors 'self'
X-Frame-Options: SAMEORIGIN
```

Côté interface, on se méfie de ses propres techniques : une page qui superpose un élément transparent à un contrôle (`opacity: 0`, `pointer-events`, `position: absolute`) peut tromper l'utilisateur et sera lue comme suspecte par les mécanismes de protection des navigateurs. Les confirmations d'actions sensibles se font sur des contrôles bien visibles, jamais derrière un recouvrement transparent. Les anciennes méthodes de « déconstruction de cadre » en JavaScript sont obsolètes face aux en-têtes.

### 30.5 Confidentialité

- **`:visited`** : pour empêcher un site de deviner l'historique de navigation, les navigateurs limitent fortement les propriétés applicables aux liens visités (surtout des couleurs) et masquent le résultat aux scripts (chapitre 2). Ne contournez pas ces restrictions.
- **Polices et ressources tierces** : charger des polices ou des feuilles depuis un service tiers transmet l'adresse IP et des informations de navigation à ce service, ce qui pose des questions de conformité (RGPD). On **héberge soi-même** les polices (chapitre 7) et les feuilles de style.
- **Pixels espions en CSS** : une image de fond hébergée à l'extérieur est une requête réseau déclenchée à l'affichage, utilisée dans certains courriels pour suivre l'ouverture. Les clients de messagerie bloquent souvent les images distantes pour cette raison.
- **Empreinte du navigateur** : les requêtes de préférences (`prefers-color-scheme`, `prefers-reduced-motion`) et la liste des polices disponibles peuvent contribuer à identifier un utilisateur. Les navigateurs préservant la vie privée en limitent ou en uniformisent certains résultats ; on n'utilise ces informations que pour adapter l'interface, jamais pour pister.

### 30.6 Chaîne d'approvisionnement

Les feuilles de style et les paquets tiers sont du code que vous n'avez pas écrit : une version compromise se propage à tous les sites qui la chargent.

```html
<link rel='stylesheet'
      href='https://cdn.example.com/bibliotheque/1.2.3/style.min.css'
      integrity='sha384-EMPREINTE-CALCULEE-DU-FICHIER'
      crossorigin='anonymous'>
```

- **Intégrité de sous-ressource** (SRI, attribut `integrity`) : le navigateur refuse la feuille si son contenu ne correspond plus à l'empreinte attendue. Elle s'accompagne de `crossorigin`.
- **Épinglage de version** : ne jamais charger `latest` ; fixer une version exacte (idéalement ancienne d'au moins quelques semaines).
- **Hébergement local** : copier les fichiers tiers dans votre propre dépôt ou votre propre CDN, plutôt que dépendre d'un tiers à chaque affichage.
- **Audit des dépendances** : `npm audit` et les outils de veille signalent les paquets vulnérables ; on limite le nombre de dépendances de style.
- **Éviter `@import` d'une feuille tierce** : il crée une dépendance cachée et contourne facilement la revue.

### 30.7 Liste de contrôle

| Point | Vérification |
| --- | --- |
| Aucune saisie utilisateur ne devient du CSS | Revue du code qui touche `style`, `<style>`, `cssText`, `insertRule` |
| CSP en place | `style-src` sans `'unsafe-inline'`, `img-src` et `font-src` restreints |
| Anti-détournement de clic | `frame-ancestors` ou `X-Frame-Options` |
| Ressources tierces maîtrisées | Polices et feuilles hébergées en local, SRI sinon |
| Contenu riche assaini | Bibliothèque d'assainissement configurée |
| Dépendances suivies | `npm audit` en intégration continue |

### Synthèse du chapitre 30

Le CSS ne s'exécute pas, mais il peut **tromper, dégrader ou faire fuiter des informations** : injection de CSS, détournement de clic, hameçonnage visuel, requêtes tierces, empreinte du navigateur, dépendances compromises. La défense repose sur quelques principes : **ne jamais fabriquer de CSS à partir d'une donnée non fiable** (listes blanches, validation, `CSS.escape()`, assainissement du contenu riche), une **CSP** qui limite `style-src`, `img-src`, `font-src` et `frame-ancestors`, la **maîtrise des ressources tierces** (hébergement local, intégrité de sous-ressource, versions épinglées) et le respect des protections de confidentialité des navigateurs comme celles de `:visited`.

---

## 31. Migration et mises à jour

**Objectifs d'apprentissage.** Vous saurez décider quand et pourquoi migrer une base de code CSS, préparer la migration par un inventaire et un filet de sécurité, conduire une migration incrémentale grâce aux couches de cascade, traiter les chantiers courants (Sass, frameworks, mises en page historiques, préfixes), vérifier et déployer progressivement, puis empêcher le retour en arrière par des règles automatiques.

### 31.1 Pourquoi et quand migrer

Le CSS vieillit mal lorsqu'on n'y touche pas : les nouveautés du langage rendent des pans entiers de code superflus, et les dépendances d'outillage deviennent obsolètes. Les **signes** qui justifient d'agir :

- des centaines d'`!important` et des surcharges en cascade pour contourner d'anciens styles ;
- impossibilité de supprimer du code de peur de casser une page oubliée ;
- mises en page bâties sur des flottants, des hauteurs fixes et des astuces de compatibilité pour des navigateurs disparus ;
- outils abandonnés (LibSass, `node-sass`, anciens plugins) ou frameworks en fin de vie ;
- difficultés répétées à adapter l'interface au mobile, au thème sombre ou à l'accessibilité.

À l'inverse, **migrer n'est pas toujours rentable** : un code stable, rarement modifié et sans incident n'a pas besoin d'une réécriture. La règle la plus économique est celle du **scout** : on migre **ce que l'on touche**, composant par composant, au fil des évolutions, plutôt qu'en un grand chantier risqué.

### 31.2 Préparer : inventaire et filet de sécurité

| Étape | Outil | But |
| --- | --- | --- |
| Mesurer le CSS inutilisé | Panneau *Coverage* des DevTools | Estimer ce qui peut être supprimé |
| Compter les symptômes | Stylelint (`declaration-no-important`, `selector-max-id`, `selector-max-specificity`) | Chiffrer la dette : nombre d'`!important`, d'identifiants, de sélecteurs trop spécifiques |
| Visualiser la spécificité | Outils d'analyse de feuilles de style (par exemple CSS Stats) | Repérer les pics de spécificité |
| Définir le support navigateur | Statistiques d'audience et `browserslist` | Décider ce qui peut être modernisé |
| **Filet de sécurité** | Tests visuels et d'accessibilité (chapitre 21) | Détecter toute régression involontaire |

Le filet de sécurité est **indispensable** : sans lui, on ne sait pas si une refonte a changé l'apparence. On le met en place **avant** de modifier la moindre règle, et on fige la situation de départ comme référence.

### 31.3 Migrer de façon incrémentale avec `@layer`

La difficulté d'une migration est la **coexistence** de l'ancien et du nouveau CSS : le nouveau code doit l'emporter sans escalade de spécificité. Les couches de cascade (chapitre 4) résolvent ce problème : on place le **code historique dans la couche la plus basse**, et tout nouveau style, écrit au-dessus, gagne naturellement.

```css
/* main.css */
@layer legacy, reset, tokens, base, composants, utilitaires;

@import url('legacy.css') layer(legacy);      /* l'ancien CSS passe dans la couche la plus basse */

@layer composants {
    .bouton {                                  /* nouvelle version, plus simple, qui gagne sans !important */
        display: inline-flex;
        padding: .6em 1.2em;
    }
}
```

La démarche se répète pour chaque composant :

1. **Choisir** un composant (de préférence peu risqué).
2. **Réécrire** ses styles dans une couche moderne, avec des variables et des unités relatives.
3. **Vérifier** par les tests visuels que le rendu est identique (ou volontairement amélioré).
4. **Supprimer** les règles correspondantes du fichier historique.
5. **Mesurer** la progression : lignes restantes dans la couche `legacy`.

À la fin, la couche `legacy` est vide et peut disparaître. Cette approche, dite d'**étranglement progressif**, évite les « grands soirs » et permet de livrer en continu.

### 31.4 Les chantiers courants

| Chantier | Méthode ou outil | Point d'attention |
| --- | --- | --- |
| Sass `@import` vers `@use` et `@forward` | Outil officiel `sass-migrator module` | Les espaces de noms changent les appels de variables et de mixins |
| LibSass ou `node-sass` vers Dart Sass | Remplacer le paquet par `sass` | Quelques différences de syntaxe (division, fonctions de couleur) |
| Variables Sass vers variables CSS | Remplacement manuel, composant par composant | Garder Sass pour les valeurs nécessaires à la compilation (boucles, calculs de build) |
| Imbrication Sass vers imbrication native | Réécriture ou outil de build | La concaténation de suffixes (`&-titre`) n'existe pas en CSS natif |
| Bootstrap 4 vers 5, Tailwind 3 vers 4 | Guides officiels ; outil `npx @tailwindcss/upgrade` pour Tailwind | Lire les ruptures de compatibilité ; tester visuellement |
| Flottants, `inline-block`, tableaux de mise en page vers Flexbox et Grid | Réécriture composant par composant | Vérifier l'ordre DOM et l'accessibilité |
| `max-width` (desktop d'abord) vers `min-width` (mobile d'abord) | Réécriture par composant | Inverser la logique avec soin |
| Préfixes écrits à la main | Autoprefixer ou Lightning CSS (chapitre 18) | Supprimer les préfixes manuels devenus inutiles |
| Astuces pour anciens navigateurs (`*zoom`, `filter: alpha()`, commentaires conditionnels) | Suppression | Vérifier la politique de support |
| `@import` en CSS pour charger des fichiers | Balises `<link>` ou bundler | Chargements en série supprimés |
| CSS-in-JS exécuté à l'exécution vers CSS Modules ou extraction à la compilation | Migration par composant | Prévoir le thème et les props dynamiques via variables CSS |

### 31.5 Exemple : d'une mise en page à flottants à Grid

```css
/* Avant : colonnes par flottants, avec clearfix et marges calculées */
.col { float: left; width: 31.33%; margin-right: 3%; }
.col:last-child { margin-right: 0; }
.rangee::after { content: ''; display: table; clear: both; }
@media (max-width: 767px) { .col { float: none; width: 100%; margin-right: 0; } }

/* Après : Grid, mobile d'abord, sans clearfix ni marge de dernier enfant */
.rangee { display: grid; gap: 1.5rem; }
@media (width >= 48rem) { .rangee { grid-template-columns: repeat(3, 1fr); } }
```

Le code d'arrivée est plus court, plus lisible, sans arithmétique de pourcentages et avec une logique mobile d'abord. Un seul point à surveiller : les flottants et Grid ne se comportent pas de la même façon avec le contenu de hauteur variable ; les tests visuels confirment l'équivalence.

### 31.6 Vérifier, déployer, verrouiller

- **Revue des différences visuelles** : chaque écart est soit une régression à corriger, soit une amélioration validée explicitement.
- **Déploiement progressif** : par route ou par pourcentage d'utilisateurs, en suivant les indicateurs de performance et les erreurs (chapitre 24). Un simple attribut sur `<html>` peut basculer entre l'ancien et le nouveau style d'un composant pendant la transition.
- **Documentation** : consigner les décisions (conventions, composants migrés, ce qui reste).
- **Verrouillage automatique** : empêcher le retour en arrière en ajoutant des règles Stylelint.

```js
// stylelint.config.js : règles ajoutées une fois la migration terminée
export default {
    extends: ['stylelint-config-standard'],
    rules: {
        'declaration-no-important': true,
        'property-disallowed-list': ['float', 'clip'],     // flottants et ancien clip interdits
        'at-rule-disallowed-list': ['import'],             // pas de @import de fichiers CSS
        'selector-max-id': 0,
    },
};
```

### 31.7 Pièges fréquents

| Piège | Conséquence | Parade |
| --- | --- | --- |
| Migrer sans filet de sécurité | Régressions découvertes en production | Tests visuels avant toute modification |
| Réécrire tout d'un coup | Longue période sans livraison, risque élevé | Migration incrémentale par couches |
| Changer des unités sans mesurer (px vers rem) | Rendu différent selon les réglages de l'utilisateur | Vérifier à plusieurs tailles de police |
| Supprimer du code « mort » sans test | Disparition de styles d'états rares | Tester les états limites avant suppression |
| Ne pas verrouiller | Retour progressif des anciennes pratiques | Règles Stylelint et revue |

### Synthèse du chapitre 31

On migre quand la **dette** (surcharges, `!important`, outils abandonnés, mises en page historiques) coûte plus que le changement, et on migre **ce que l'on touche**, par petits pas. La préparation repose sur un **inventaire** (CSS inutilisé, spécificité, support navigateur) et un **filet de sécurité** de tests visuels. Les **couches de cascade** permettent la coexistence : le code historique va dans une couche basse, le nouveau code gagne sans `!important` (**étranglement progressif**). Les chantiers courants (Sass vers modules et variables CSS, frameworks, flottants vers Flexbox et Grid, préfixes, anciens hacks) ont chacun leurs outils. On vérifie, on déploie progressivement, puis on **verrouille** le résultat avec des règles Stylelint.

---

## 32. Nouveautés et bonnes pratiques

**Objectifs d'apprentissage.** Vous saurez situer les pratiques anciennes et leurs équivalents actuels, retracer l'évolution du CSS depuis 1996, retrouver en un seul endroit les recettes les plus utiles, appliquer les bonnes pratiques générales (dont les douze règles d'or du CSS moderne), organiser un projet de façon cohérente et planifier votre progression avec les bonnes ressources.

### 32.1 Anciennes pratiques et pratiques actuelles *(à jour)*

Le code existant mêle souvent des techniques de plusieurs époques. Ce tableau les relie à leur équivalent actuel et au chapitre qui l'explique.

| Ancienne pratique *(héritage)* | Pratique actuelle *(à jour)* | Chapitre |
| --- | --- | --- |
| Mise en page par `float`, `inline-block` ou tableaux | Flexbox et Grid | 9 et 10 |
| Clearfix (`::after { clear: both }`) | `display: flow-root` | 8 |
| Largeurs en `px` et `100vh` | `rem`, `%`, `ch`, `dvh`, `min()`, `clamp()` | 5 |
| Marges pour espacer les enfants | `gap` | 9 et 10 |
| `padding-top` en pourcentage pour un rapport | `aspect-ratio` | 6 |
| `margin-left`, `padding-right`, `text-align: left` | Propriétés logiques (`inline`, `block`, `start`, `end`) | 6 et 29 |
| Préfixes `-webkit-` écrits à la main | Autoprefixer ou Lightning CSS | 18 |
| `rgba()`, `hsla()`, virgules | `rgb(r g b / a)`, `oklch()`, `color-mix()` | 5 |
| Variables Sass `$x` | Propriétés personnalisées `--x` | 12 |
| Imbrication par préprocesseur | Imbrication native avec `&` | 2 |
| `@import` de Sass, `@import` de CSS | `@use` et `@forward` ; balises `<link>` ou build | 3 et 18 |
| `!important` et sélecteurs très spécifiques | `@layer`, `:where()`, `@scope` | 4 |
| `:focus` seul avec contour supprimé | `:focus-visible` | 6 et 16 |
| Media queries `min-width` et `max-width` | Syntaxe d'intervalle ; requêtes de conteneur | 14 |
| JavaScript pour styler un parent | `:has()` | 2 |
| Menus, modales et infobulles scriptés | `<dialog>`, `popover`, positionnement par ancrage | 15 et 28 |
| Animations d'apparition par JavaScript | `@starting-style`, `transition-behavior` | 13 |
| Bibliothèques de défilement animé | `animation-timeline`, `scroll-snap` | 8 et 13 |
| Thème sombre par feuille alternative | `color-scheme` et `light-dark()` | 12 |
| Polices de plusieurs fichiers par graisse | Police variable en WOFF2 | 7 |

### 32.2 Chronologie de l'évolution du CSS

| Période | Évolutions marquantes |
| --- | --- |
| 1996 | CSS niveau 1 : couleurs, polices, marges |
| 1998 | CSS niveau 2 : positionnement, `z-index`, types de médias |
| 2011 | CSS 2.1 finalisé, référence des années 2000 |
| 2012 | Requêtes média, animations et transitions, sélecteurs niveau 3 (ensemble dit « CSS3 ») |
| 2015 à 2017 | Flexbox largement disponible ; Grid dans tous les navigateurs majeurs en 2017 ; propriétés personnalisées |
| 2020 à 2021 | `gap` pour Flexbox, `aspect-ratio`, `:is()` et `:where()`, propriétés logiques généralisées |
| 2022 à 2023 | Couches de cascade, requêtes de conteneur, `:has()`, imbrication native, subgrid, unités `dvh` |
| 2024 | `@property`, `text-wrap: balance`, `@starting-style`, `popover` |
| 2025 à 2026 | Transitions de vue dans un même document, `@scope`, positionnement par ancrage, `sibling-index()` ; `if()` et `@function` en cours d'adoption |

Les années sont **approximatives** : une fonctionnalité apparaît d'abord dans un navigateur, puis devient disponible partout. Pour une date précise, consultez les données de compatibilité (MDN, Baseline).

### 32.3 Recettes essentielles

| Besoin | Code |
| --- | --- |
| Centrer (2 axes) | `display: grid; place-items: center;` |
| Largeur de lecture centrée | `max-width: 65ch; margin-inline: auto;` |
| Conteneur avec marges latérales | `width: min(100% - 2rem, 70rem); margin-inline: auto;` |
| Colonnes responsive sans media query | `grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));` |
| Pied de page en bas | `body { min-height: 100dvh; display: grid; grid-template-rows: auto 1fr auto; }` |
| Espacer des enfants | `display: grid; gap: 1rem;` (ou flex avec `gap`) |
| Image qui remplit sans déformer | `width: 100%; aspect-ratio: 16/9; object-fit: cover;` |
| Texte tronqué (1 ligne) | `white-space: nowrap; overflow: hidden; text-overflow: ellipsis;` |
| Titre équilibré | `text-wrap: balance;` |
| Carré ou cercle | `aspect-ratio: 1; border-radius: 50%;` |
| Coller en haut au défilement | `position: sticky; top: 0;` |
| Superposer sur tout le parent | `position: absolute; inset: 0;` |
| Thème clair ou sombre | `:root { color-scheme: light dark; }` puis `light-dark(clair, sombre)` |
| Anneau de focus clavier | `:focus-visible { outline: 3px solid royalblue; outline-offset: 2px; }` |
| Cacher visuellement (lecteurs d'écran) | classe `.sr-only` (section 16.4) |
| Défilement fluide respectueux | `@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }` |
| Composant adaptatif | `.parent { container-type: inline-size; }` puis `@container (min-width: 30rem) { … }` |

### 32.4 Ordre de lecture d'une déclaration de composant (suggestion)

```css
.composant {
    /* 1. Variables locales */    --fond: white;
    /* 2. Affichage et position */ display: grid; position: relative; inset: 0; z-index: 1;
    /* 3. Modèle de boîte */      width: 100%; margin-block: 1rem; padding: 1rem; border: 1px solid;
    /* 4. Typographie */          font: 1rem/1.5 system-ui; color: #222;
    /* 5. Visuel */               background: var(--fond); border-radius: .5rem; box-shadow: 0 1px 3px rgb(0 0 0 / .2);
    /* 6. Divers */               transition: background .2s; cursor: pointer;
}
```

L'ordre exact importe moins que sa **constance** dans toute l'équipe, idéalement imposée par un outil (Stylelint, Prettier).

### 32.5 Bonnes pratiques générales : les 12 règles d'or du CSS moderne

1. **`box-sizing: border-box`** partout.
2. Unités **relatives** (`rem`, `%`, `ch`, `fr`, `dvh`) ; `px` pour les fines bordures.
3. **Mobile d'abord**, points de rupture selon le contenu.
4. **Flexbox** pour une dimension, **Grid** pour deux ; **`gap`** pour espacer.
5. **Variables CSS** pour tout ce qui se répète (tokens).
6. **Sélecteurs simples**, classes plutôt qu'identifiants, **pas d'`!important`** ; `@layer` pour maîtriser la cascade.
7. **Propriétés logiques** (`inline` et `block`).
8. **Animez `transform` et `opacity`** ; respectez `prefers-reduced-motion`.
9. **Accessibilité** : contraste, focus visible, ordre logique, cibles tactiles.
10. **Amélioration progressive** : repli d'abord, `@supports` pour le reste.
11. **Mesurez** (DevTools, Lighthouse) avant d'optimiser.
12. **Vérifiez le support** (MDN, caniuse, Baseline) avant d'adopter une nouveauté.

### 32.6 Structure de projet recommandée

Cette organisation réunit tout ce que le cours a présenté : couches de cascade, tokens, composants isolés, tests et outils.

```text
mon-projet/
|-- index.html
|-- styles/
|   |-- main.css              <- ordre des couches et imports
|   |-- 00-reset.css
|   |-- 01-tokens.css         <- variables : couleurs, espacements, typographie
|   |-- 02-base.css           <- éléments HTML (body, a, h1...)
|   |-- 03-layout.css         <- grilles, conteneurs
|   |-- composants/
|   |   |-- bouton.css
|   |   |-- carte.css
|   |   +-- modale.css
|   +-- 99-utilitaires.css
|-- polices/                  <- polices WOFF2 hébergées en local
|-- images/
|-- tests/
|   |-- visuels.spec.js       <- captures de non-régression
|   +-- a11y.spec.js          <- contrôles axe-core
|-- stylelint.config.js
|-- playwright.config.js
+-- package.json
```

```css
/* styles/main.css */
@layer reset, tokens, base, layout, composants, utilitaires;

@import url('00-reset.css') layer(reset);
@import url('01-tokens.css') layer(tokens);
@import url('02-base.css') layer(base);
@import url('03-layout.css') layer(layout);
@import url('composants/bouton.css') layer(composants);
@import url('composants/carte.css') layer(composants);
@import url('99-utilitaires.css') layer(utilitaires);
```

Le point d'entrée déclare l'**ordre** des couches puis y range chaque fichier. En production, un outil de build regroupe ces imports en un seul fichier minifié (chapitres 22 et 24), ce qui évite le chargement en série propre à `@import`.

**Liste de démarrage.** Avant d'écrire la première règle d'un nouveau projet :

1. déclarer `lang` et la balise `viewport` ;
2. poser le reset minimal et `box-sizing: border-box` ;
3. définir les tokens (couleurs, espacements, rayons, typographie) et `color-scheme` ;
4. configurer Stylelint et Prettier ;
5. écrire un premier test visuel et un premier contrôle d'accessibilité ;
6. fixer la liste `browserslist` d'après l'audience.

### 32.7 Parcours d'apprentissage et ressources

- **MDN, section CSS** : https://developer.mozilla.org/fr/docs/Web/CSS
- **web.dev, Learn CSS** : https://web.dev/learn/css
- **Spécifications du W3C (CSSWG)** : https://www.w3.org/Style/CSS/
- **Baseline** : https://web.dev/baseline ; **Can I use** : https://caniuse.com
- **CSS-Tricks**, **Every Layout**, **Modern CSS Solutions**, **Kevin Powell** (vidéos)
- **Flexbox Froggy**, **Grid Garden**, **CSS Diner** (jeux d'apprentissage)

**Parcours conseillé.** Après les chapitres 1 à 10 (les fondamentaux), consacrez du temps à **Flexbox et Grid** (9 et 10) en réalisant des mises en page complètes. Poursuivez avec les **variables, les animations et le responsive** (12 à 14), puis l'**accessibilité** (16), qui doit accompagner tout le reste. Les parties Tests, Performance et Essentiels s'abordent selon les besoins du projet : **outils et tests** (20, 21, 27) dès qu'une base de code grandit, **performance** (22 à 24) avant une mise en production, **sécurité, internationalisation et migration** (29 à 31) pour les produits exposés, multilingues ou anciens. Le meilleur apprentissage reste la pratique : reproduisez des interfaces existantes et réalisez les projets du chapitre 28.

### Synthèse du chapitre 32

Le CSS actuel remplace des **pratiques anciennes** par des équivalents plus simples (Flexbox et Grid, `gap`, `aspect-ratio`, propriétés logiques, variables, imbrication native, `@layer`, `:has()`, `<dialog>` et `popover`), et la **chronologie** montre un rythme d'évolution soutenu depuis 2022. Les **recettes essentielles**, l'**ordre de déclaration** et les **douze règles d'or** résument les bonnes pratiques : `box-sizing: border-box`, unités relatives, mobile d'abord, Flexbox et Grid, variables, sélecteurs simples et couches, propriétés logiques, animations par `transform` et `opacity`, accessibilité, amélioration progressive, mesure et vérification du support. Une **structure de projet** par couches, tokens et composants, soutenue par des tests et des outils, rend le code durable. La progression passe par la maîtrise des fondamentaux puis par la pratique de projets réels.

---

*Fin du cours. Bon style avec CSS !*
