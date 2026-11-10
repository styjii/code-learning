# Cours complet de langage C++

*De la syntaxe élémentaire à la bibliothèque standard moderne — normes C++17, C++20, C++23 et C++26 — édition de novembre 2026*

## Avant de commencer

### Objectifs du cours

À l'issue de ce cours, vous serez capable de :

- écrire, compiler, exécuter et déboguer des programmes C++ modernes, lisibles et sûrs ;
- raisonner en termes de **types**, de **durée de vie** et de **propriété** des objets, qui sont les trois notions centrales du langage ;
- concevoir des classes correctes (constructeurs, destructeur, copie, déplacement, héritage, polymorphisme) ;
- exploiter la **bibliothèque standard** (conteneurs, algorithmes, chaînes, flux, pointeurs intelligents, concurrence) plutôt que de réinventer ces outils ;
- reconnaître et éviter les **comportements indéfinis**, première source de bogues et de failles de sécurité en C++.

### Prérequis et organisation

Aucune connaissance préalable du C++ n'est exigée ; avoir déjà programmé (dans n'importe quel langage) aide. Le cours suit trois niveaux :

- **Niveau débutant (chapitres 1 à 10)** : premier programme, types, opérateurs, entrées/sorties, structures de contrôle, fonctions, portée et durée de vie.
- **Niveau intermédiaire (chapitres 11 à 21)** : tableaux, chaînes, pointeurs, mémoire dynamique, conteneurs, références, classes, énumérations, templates, lambdas et polymorphisme.
- **Niveau avancé (chapitres 22 à 30)** : fichiers, ligne de commande, préprocesseur et modules, bits, récursivité, Unicode, compilation, comportements indéfinis, bibliothèque standard.

### Conventions typographiques

- *(C++11)*, *(C++14)*, *(C++17)*, *(C++20)*, *(C++23)*, *(C++26)* indiquent la norme qui a introduit une fonctionnalité. Compilez toujours avec une norme explicite (`-std=c++20` par exemple).
- Les blocs de code sont complets et compilables, sauf mention contraire. Les commentaires `// ...` expliquent l'intention, pas seulement la mécanique.
- **Définition** introduit un terme technique à retenir. **Piège** signale une erreur classique. **À retenir** résume l'essentiel en fin de chapitre.

### Méthode de travail conseillée

Lisez chaque chapitre dans l'ordre : les notions s'appuient les unes sur les autres. Chaque exemple de code est commenté et illustre une notion précise. Pour tester un exemple, compilez **toujours** avec `-Wall -Wextra` et corrigez chaque avertissement.

---

# Niveau débutant

---

## Chapitre 1 — Introduction au C++

### 1.1 Qu'est-ce que le C++ ?

Le **C++** est un langage de programmation **compilé**, **à typage statique** et **multi-paradigme**. Il a été conçu à partir de 1979 par **Bjarne Stroustrup** aux Laboratoires Bell (AT&T), d'abord sous le nom *C with Classes*, puis rebaptisé C++ en 1983 (l'opérateur `++` du C signifie « incrémenter » : C++ est littéralement « le C, en mieux »). Le but initial était de combiner l'efficacité et la proximité du matériel du C avec les mécanismes d'abstraction du langage Simula (les classes).

Chaque adjectif de cette définition a des conséquences concrètes :

- **Compilé** : le code source est traduit **avant** l'exécution en code machine natif, propre à un processeur et à un système. Il n'y a pas de machine virtuelle ni d'interpréteur à l'exécution, d'où de très bonnes performances, mais aussi un cycle « écrire, compiler, exécuter ».
- **À typage statique** : le type de chaque variable et de chaque expression est connu **à la compilation**. Le compilateur refuse une grande classe d'erreurs (additionner une chaîne et un pointeur, appeler une fonction avec de mauvais arguments) avant même que le programme ne s'exécute.
- **Multi-paradigme** : le C++ permet de programmer en style *procédural* (fonctions, comme en C), *orienté objet* (classes, héritage, polymorphisme), *générique* (templates et concepts) et partiellement *fonctionnel* (lambdas, algorithmes, ranges). Vous choisissez le paradigme adapté au problème, et vous pouvez les mélanger.
- **Proche du matériel** : on peut manipuler directement la mémoire, les adresses, les bits ; on peut aussi s'en abstraire presque entièrement grâce à la bibliothèque standard.

#### Le principe fondateur : les abstractions à coût nul

Stroustrup énonce le principe du **coût nul** (*zero-overhead principle*) en deux phrases : (1) **ce que vous n'utilisez pas, vous ne le payez pas** ; (2) **ce que vous utilisez, vous ne pourriez pas le coder à la main plus efficacement**. Un `std::vector<int>` bien utilisé est aussi rapide qu'un tableau écrit à la main avec `malloc` ; une boucle sur un intervalle (`for (int x : v)`) est aussi rapide qu'une boucle à indices. Le C++ ne vous impose ni ramasse-miettes, ni vérification automatique des bornes : la contrepartie est que **vous êtes responsable** de ne pas violer les règles du langage (voir chapitre 29).

#### Gestion de la mémoire : le RAII

Le C++ n'a pas de ramasse-miettes. Il offre à la place un mécanisme déterministe, le **RAII** (*Resource Acquisition Is Initialization*) : une ressource (mémoire, fichier, verrou, connexion réseau) est acquise dans le **constructeur** d'un objet et libérée dans son **destructeur**, appelé automatiquement à la fin de la portée de l'objet, quoi qu'il arrive (même en cas d'exception). Ce principe est étudié en détail aux chapitres 10 et 14 ; retenez dès maintenant qu'**on n'écrit presque jamais `delete` à la main en C++ moderne**.

### 1.2 Pourquoi apprendre le C++ ?

- **Performance** : moteurs de jeu (Unreal Engine), finance haute fréquence, calcul scientifique, traitement d'images et de signaux, cœur des bibliothèques d'apprentissage automatique (TensorFlow, PyTorch).
- **Logiciels de grande taille** : navigateurs web (Chrome, Firefox), bases de données (MySQL, MongoDB, ClickHouse), suites bureautiques, outils de CAO, compilateurs (LLVM/Clang).
- **Systèmes embarqués et temps réel** : automobile, robotique, aéronautique, microcontrôleurs, où la prédictibilité de la mémoire et du temps d'exécution est cruciale.
- **Interopérabilité** : compatibilité directe avec le C et ses innombrables bibliothèques ; facilité à exposer du code C++ à Python, Rust, Java, etc.
- **Compréhension profonde** : apprendre le C++ force à comprendre ce que font réellement les langages de plus haut niveau (mémoire, copies, durées de vie).

**Piège — « le » C++ n'existe pas.** Le langage est vaste et porte plus de quarante ans d'histoire. On peut y écrire du « C avec des classes » (dangereux, plein de `char *` et de `malloc`) ou du **C++ moderne** (sûr, concis : `std::string`, `std::vector`, pointeurs intelligents, algorithmes). Ce cours enseigne exclusivement le second.

### 1.3 Histoire et évolution des normes

Le C++ est normalisé par l'ISO (norme **ISO/IEC 14882**), par le comité de travail **WG21**. Depuis 2011, une nouvelle révision paraît tous les trois ans.

- **C++98 / C++03** : première norme (1998) et son correctif (2003). Classes, héritage, templates, exceptions, espaces de noms, `bool`, et surtout la **STL** (conteneurs, itérateurs, algorithmes).
- **C++11** : la « renaissance » du langage. `auto`, boucle `for` sur intervalle, **lambdas**, **sémantique de déplacement** (`&&`, `std::move`), `nullptr`, `constexpr`, **pointeurs intelligents**, `override` / `final`, initialisation uniforme `{}`, templates variadiques, `<thread>`, `<chrono>`, `<random>`, `unordered_map`.
- **C++14** : lambdas génériques, déduction du type de retour, `std::make_unique`, littéraux binaires `0b…`, séparateur de chiffres `'`.
- **C++17** : liaisons structurées (`auto [a, b]`), `if` / `switch` avec initialiseur, `if constexpr`, `std::optional`, `std::variant`, `std::any`, `std::string_view`, `<filesystem>`, variables `inline`, expressions de repli, algorithmes parallèles, attribut `[[nodiscard]]`.
- **C++20** : **concepts**, **ranges**, **coroutines**, **modules**, opérateur de comparaison à trois voies `<=>`, `std::format`, `std::span`, `consteval`, `constinit`, `<bit>`, `std::jthread`.
- **C++23** : `std::print` / `std::println`, `std::expected`, `std::mdspan`, *deducing this*, `import std;`, `std::flat_map`, `std::generator`, `std::stacktrace`, `std::to_underlying`.
- **C++26** (travaux techniques terminés début 2026) : **réflexion statique**, **contrats** (`pre`, `post`, `contract_assert`), `std::execution`, bibliothèque standard **durcie**, `#embed`, `<simd>`, `std::inplace_vector`.
- **C++29** : prochaine révision, en préparation par le comité.

Le choix de la norme se fait à la compilation : `-std=c++17`, `-std=c++20`, `-std=c++23`, `-std=c++2c` (C++26). La norme par défaut dépend du compilateur et de sa version (GCC utilise `gnu++17` depuis GCC 11 ; MSVC, `/std:c++14`). **Indiquez toujours explicitement la norme.** Les compilateurs ne suivent pas tous au même rythme : consultez la page « Compiler support » de cppreference.com avant d'utiliser une fonctionnalité récente.

### 1.4 De la source à l'exécutable : la chaîne de compilation

Un programme C++ passe par plusieurs étapes avant de s'exécuter :

```text
hello.cpp --> préprocesseur --> compilateur --> assembleur --> éditeur de liens --> exécutable
 (source)        (.ii)            (.s)           (.o)         (+ bibliothèques)
```

1. **Préprocessing** : traite les lignes commençant par `#` (`#include`, `#define`, `#ifdef`). `#include <iostream>` est **remplacé textuellement** par le contenu du fichier d'en-tête. Le résultat s'appelle une **unité de traduction**.
2. **Compilation** : l'unité de traduction est analysée (syntaxe, types), puis traduite en assembleur. Les **templates** sont **instanciés** à cette étape. Les erreurs de syntaxe et de typage sont signalées ici.
3. **Assemblage** : l'assembleur produit un **fichier objet** (`.o` / `.obj`) : du code machine dont les références à des fonctions externes ne sont pas encore résolues.
4. **Édition de liens** (*link*) : l'éditeur de liens assemble les fichiers objets et les bibliothèques en un exécutable, en résolvant chaque symbole. Les erreurs `undefined reference` apparaissent ici.
5. **Exécution** : le système charge le programme en mémoire et appelle `main`.

**Définition — unité de traduction.** C'est un fichier source `.cpp` **après** préprocessing. Chaque unité est compilée **séparément** ; c'est ce qui permet de ne recompiler que les fichiers modifiés dans un gros projet.

Avec les **modules** (C++20), l'inclusion textuelle est remplacée par l'importation d'interfaces déjà compilées (chapitre 24).

### 1.5 Installer un compilateur

- **Linux (Debian/Ubuntu)** : `sudo apt install build-essential` (installe `g++` et `make`) ; ajoutez `clang` et `cmake` si besoin.
- **macOS** : `xcode-select --install` (installe Clang) ou `brew install gcc`.
- **Windows** : trois options — **WSL** (un vrai Linux dans Windows, recommandé), **MSYS2** (`pacman -S mingw-w64-ucrt-x86_64-gcc`), ou **Visual Studio** (compilateur MSVC).

Vérifiez l'installation :

```bash
g++ --version
clang++ --version
```

### 1.6 Premier programme : « Bonjour le monde »

```cpp
#include <iostream>                      // flux d'entrée/sortie

int main() {                             // point d'entrée du programme
    std::cout << "Bonjour le monde !\n";  // affiche du texte
    return 0;                            // 0 = succès
}
```

Analyse ligne par ligne :

- `#include <iostream>` demande au préprocesseur d'insérer les déclarations des flux d'entrée/sortie (`std::cout`, `std::cin`, `std::cerr`). Les en-têtes de la bibliothèque standard n'ont **pas d'extension** (`<vector>`, `<string>`) ; ceux hérités du C portent un `c` initial (`<cstdio>`, `<cmath>`).
- `int main()` définit la **fonction principale**, point d'entrée de tout programme. Elle retourne un `int` : le **code de sortie** transmis au système (`0` = succès, toute autre valeur = erreur). En C++, `return 0;` est **facultatif** dans `main` : il est implicite si on l'omet.
- `std::cout` est le **flux de sortie standard** (l'écran). Le préfixe `std::` indique que le nom appartient à l'**espace de noms** `std`, qui contient toute la bibliothèque standard.
- `<<` est l'**opérateur d'insertion** : il envoie la valeur à sa droite dans le flux à sa gauche et retourne ce flux, ce qui permet de **chaîner** : `std::cout << "a" << 1 << '\n';`.
- `"...\n"` est un littéral de chaîne ; `\n` est un saut de ligne.

Version moderne avec `std::println` *(C++23)*, qui formate à la manière de Python et ajoute automatiquement le saut de ligne :

```cpp
#include <print>

int main() {
    std::println("Bonjour le monde ! {} + {} = {}", 2, 3, 2 + 3);
}
```

### 1.7 Compiler et exécuter

```bash
g++ -Wall -Wextra -std=c++20 hello.cpp -o hello   # compile et lie
./hello                                           # exécute (Linux/macOS)
hello.exe                                         # exécute (Windows)
```

- `-Wall -Wextra` activent des avertissements essentiels : **ne compilez jamais sans**.
- `-std=c++20` choisit la norme ; `-o hello` nomme l'exécutable.
- Le shell récupère le code de sortie avec `echo $?` (Linux/macOS) ou `echo %ERRORLEVEL%` (Windows).

### 1.8 Erreurs fréquentes du débutant

- **Point-virgule oublié** après une instruction : le compilateur signale souvent l'erreur à la ligne **suivante**.
- **Oubli de `std::`** : `cout << "Hi";` ne compile pas (sauf `using std::cout;`).
- **Casse** : le C++ distingue majuscules et minuscules (`Main` n'est pas `main`).
- **Oubli du `#include`** : utiliser `std::string` sans `<string>` peut compiler sur une machine et échouer sur une autre.
- **`<<` et `>>` inversés** : `std::cin >> x` (lire), `std::cout << x` (écrire).
- **`=` au lieu de `==`** : `if (x = 5)` affecte 5 à `x` et est toujours vrai ; `-Wall` le signale.
- **Variable non initialisée** : `int x; std::cout << x;` lit une valeur indéterminée (comportement indéfini).
- **Division entière** : `1 / 2` vaut `0`, pas `0.5` ; écrivez `1.0 / 2`.
- **`using namespace std;` dans un en-tête** : pollue tous les fichiers qui l'incluent. À proscrire.

### 1.9 Différences majeures avec le C

Le C++ n'est **pas** un sur-ensemble strict du C : du code C valide peut être refusé, voire changer de sens. Les principales différences :

- La conversion `void *` vers `T *` exige un **cast explicite** (mais on n'utilise plus `malloc` en C++).
- `f()` signifie « aucun paramètre » (en C avant C23, « paramètres non spécifiés »).
- La **déclaration implicite** de fonction est interdite : toute fonction doit être déclarée avant usage.
- Le littéral `'a'` est de type `char` (et non `int`).
- `bool`, `true` et `false` sont des mots-clés natifs.
- Les tableaux de taille variable (VLA) du C99 et les littéraux composés `(T){...}` **n'existent pas** : on utilise `std::vector` et les listes d'initialisation.
- Le nom d'une `struct` est directement un type (pas besoin de répéter `struct`).
- Un `const` global a une **liaison interne** par défaut.
- Un `goto` ne peut pas sauter par-dessus l'initialisation d'une variable.
- Un littéral de chaîne est de type `const char[N]`.

### À retenir (chapitre 1)

- Le C++ est compilé, statiquement typé, multi-paradigme, sans ramasse-miettes ; son principe est le coût nul.
- Une nouvelle norme paraît tous les trois ans ; précisez toujours `-std=`.
- La chaîne de compilation : préprocesseur, compilateur, assembleur, éditeur de liens.
- Compilez toujours avec `-Wall -Wextra`.

---

## Chapitre 2 — Structure d'un programme C++

### 2.1 Vue d'ensemble

Un fichier source C++ est une suite de **déclarations** organisées de manière assez libre. Voici un programme complet qui illustre tous les éléments classiques :

```cpp
#include <iostream>            // 1. directives du préprocesseur
#include <string>

constexpr double TAUX_TVA = 0.2;   // 2. constantes globales

int carre(int x);              // 3. déclaration (prototype)

int main() {                   // 4. fonction principale
    int n = 5;
    std::cout << "Le carré de " << n << " est " << carre(n) << '\n';
    return 0;
}

int carre(int x) {             // 5. définition
    return x * x;
}
```

### 2.2 Les composants d'un programme

- **Directives du préprocesseur** : lignes commençant par `#`, traitées avant la compilation.
- **Déclarations globales** : variables et constantes hors de toute fonction. Elles sont visibles dans tout le fichier **après** leur déclaration. On les limite autant que possible.
- **Espaces de noms** (`namespace`) : regroupent des identifiants pour éviter les collisions de noms.
- **Prototypes (déclarations de fonctions)** : annoncent le nom, les paramètres et le type de retour d'une fonction avant sa définition.
- **Classes, structures, énumérations, templates** : définissent de nouveaux types et patrons.
- **`main`** : point d'entrée **unique** et obligatoire. Il ne peut ni être appelé par le programme, ni être déclaré `static`, `inline` ou `constexpr`.
- **Instructions** : se terminent par `;`.
- **Blocs** : délimités par `{ }` ; un bloc ne se termine pas par `;` (sauf après la définition d'une classe, struct, union ou enum).

**Définition — déclaration et définition.** Une **déclaration** introduit un nom et son type (« cette fonction existe, voici sa signature »). Une **définition** fournit en plus le corps de la fonction ou réserve la mémoire de la variable. Une entité peut être déclarée plusieurs fois, mais définie **une seule fois** (*règle de la définition unique*, ODR).

### 2.3 La fonction `main` en détail

La norme autorise exactement deux formes standards :

```cpp
int main() { /* ... */ }                        // sans arguments
int main(int argc, char *argv[]) { /* ... */ }  // avec les arguments de la ligne de commande (chapitre 23)
```

- `int main()` équivaut à `int main(void)` : contrairement au C, il n'y a aucune ambiguïté.
- Le `return` final est implicite et vaut `0` si on l'omet (uniquement pour `main`).
- Le **code de sortie** est lu par le système d'exploitation ou le script qui a lancé le programme. Utilisez `EXIT_SUCCESS` et `EXIT_FAILURE` de `<cstdlib>` pour la portabilité.

```cpp
#include <cstdlib>
#include <fstream>
#include <iostream>

int main() {
    std::ifstream f("fichier_inexistant.txt");
    if (!f) {
        std::cerr << "Erreur : impossible d'ouvrir le fichier\n";
        return EXIT_FAILURE;   // le shell reçoit 1
    }
    std::cout << "Fichier ouvert\n";
    return EXIT_SUCCESS;
}                              // f est fermé automatiquement (RAII)
```

### 2.4 Commentaires

```cpp
// Commentaire sur une ligne

/* Commentaire
   sur plusieurs lignes (ne s'imbrique pas) */

/// Commentaire de documentation (Doxygen) : additionne deux entiers.
int somme(int a, int b) { return a + b; }
```

Un bon commentaire explique **pourquoi** (l'intention, la contrainte, le choix), pas **ce que** fait le code, qui se lit déjà. Un commentaire obsolète est pire que pas de commentaire.

### 2.5 Variables et instructions

```cpp
#include <iostream>

int main() {
    int age;                 // déclaration : valeur indéterminée (dangereux)
    age = 25;                // affectation
    int taille = 180;        // déclaration + initialisation
    int poids{75};           // initialisation uniforme (recommandée)
    std::cout << age << ' ' << taille << ' ' << poids << '\n';
}
```

**Bonne pratique.** On déclare une variable **au plus près de son premier usage** (dans un bloc, dans l'en-tête d'un `for` ou d'un `if`) et on l'**initialise toujours** à la déclaration. Ceci contraste avec le vieux style C où toutes les variables étaient déclarées en tête de fonction.

### 2.6 Espaces de noms

Un **espace de noms** regroupe des identifiants sous un préfixe pour éviter les conflits entre bibliothèques. Toute la bibliothèque standard vit dans `std`.

```cpp
#include <iostream>
#include <string>

namespace geometrie {                          // espace de noms personnel
    constexpr double PI = 3.14159265;
    double aire_cercle(double r) { return PI * r * r; }
}

namespace g = geometrie;                       // alias d'espace de noms

int main() {
    using std::cout;                           // using-declaration : un seul nom importé
    cout << geometrie::aire_cercle(2.0) << '\n';
    cout << g::PI << '\n';
}
```

- **Nom qualifié** (`std::cout`) : toujours valable et le plus clair.
- **`using std::cout;`** : importe un nom ; acceptable dans un `.cpp`, dans une portée limitée.
- **`using namespace std;`** : importe tout `std` ; à éviter, et **interdit dans un en-tête**, car il impose ce choix à tous les fichiers qui l'incluent.
- **Espace de noms anonyme** `namespace { ... }` : les noms ne sont visibles que dans le fichier courant (remplace le `static` global du C).
- `namespace a::b::c { }` *(C++17)* : déclaration abrégée d'espaces imbriqués.

L'opérateur `::` est l'**opérateur de résolution de portée** : `::x` désigne `x` dans l'espace global, `A::x` désigne `x` dans l'espace `A` ou la classe `A`.

### 2.7 Programme sur plusieurs fichiers : aperçu

Dès qu'un programme grossit, on sépare **interface** et **implémentation** :

- un **en-tête** (`.hpp`) contient les **déclarations** ;
- un **fichier source** (`.cpp`) contient les **définitions** ;
- chaque `.cpp` est compilé séparément, puis les fichiers objets sont liés.

Cette organisation est détaillée au chapitre 9 (fonctions) et au chapitre 28 (compilation).

### À retenir (chapitre 2)

- Un programme = directives, déclarations, définitions, une seule fonction `main`.
- Déclarer ≠ définir ; on peut déclarer plusieurs fois, définir une seule fois.
- `std::` qualifie les noms de la bibliothèque standard ; pas de `using namespace` dans les en-têtes.
- Initialiser toujours, déclarer au plus près de l'usage.

---

## Chapitre 3 — Syntaxe et mots-clés

### 3.1 Les briques du langage : les lexèmes

Le compilateur lit le texte source et le découpe en **lexèmes** (*tokens*), unités minimales ayant un sens. Il en existe cinq catégories :

- les **identifiants** (noms de variables, fonctions, types) ;
- les **mots-clés** (`int`, `if`, `class`…), réservés par le langage ;
- les **littéraux** (`42`, `3.14`, `'a'`, `"texte"`, `true`) ;
- les **opérateurs** (`+`, `<<`, `::`, `->`…) ;
- les **séparateurs et ponctuation** (`;`, `{ }`, `( )`, `,`…).

L'espace blanc (espaces, tabulations, sauts de ligne) sert uniquement à **séparer** des lexèmes ; la mise en page est donc libre. Exceptions : le contenu des littéraux de chaîne et les directives du préprocesseur, qui occupent chacune une ligne.

### 3.2 Règles générales de syntaxe

- Le C++ est **sensible à la casse** : `Valeur`, `valeur` et `VALEUR` sont trois identifiants différents.
- Toute **instruction** se termine par un point-virgule ; une **instruction composée** (bloc) `{ ... }` regroupe plusieurs instructions et peut être utilisée partout où une instruction est attendue.
- Les **trigraphes** (`??=`…) ont été supprimés en C++17.
- Les **jetons alternatifs** `and`, `or`, `not`, `xor`, `bitand`, `bitor`, `compl`, `and_eq`, `or_eq`, `xor_eq`, `not_eq` sont des mots-clés équivalents aux opérateurs symboliques (`&&`, `||`, `!`…). Ils sont rares en pratique.

### 3.3 Les identifiants

Un identifiant est formé de lettres, de chiffres et du caractère `_`, et **ne commence pas par un chiffre**. Il ne doit pas être un mot-clé. Sont **réservés à l'implémentation** (donc interdits à l'utilisateur) : tout identifiant contenant `__` (double tiret bas) et tout identifiant commençant par `_` suivi d'une majuscule ; les identifiants commençant par un seul `_` sont réservés dans l'espace global.

```cpp
int age = 30;                // valide
int nombre_de_points = 3;    // snake_case : style de la bibliothèque standard
int nombreDePoints = 4;      // camelCase : autre convention répandue
// int 2fois = 2;            // invalide : commence par un chiffre
// int mon-nom = 3;          // invalide : '-' interdit
// int class = 1;            // invalide : mot-clé
```

**Bonne pratique.** Choisissez une convention de nommage et tenez-la dans tout le projet : par exemple `snake_case` pour variables et fonctions, `PascalCase` pour les types, un suffixe `_` pour les membres privés. Un nom doit exprimer l'intention (`nb_eleves`, pas `n1`).

### 3.4 Les mots-clés

Un **mot-clé** a une signification fixe : on ne peut pas le réutiliser comme identifiant. Voici les familles principales *(norme C++23)* :

- **Types** : `bool`, `char`, `char8_t`, `char16_t`, `char32_t`, `wchar_t`, `short`, `int`, `long`, `float`, `double`, `signed`, `unsigned`, `void`, `auto`, `decltype`.
- **Contrôle** : `if`, `else`, `switch`, `case`, `default`, `for`, `while`, `do`, `break`, `continue`, `goto`, `return`.
- **Exceptions** : `try`, `catch`, `throw`, `noexcept`.
- **Classes** : `class`, `struct`, `union`, `enum`, `public`, `protected`, `private`, `virtual`, `friend`, `this`, `operator`, `explicit`, `mutable`, `delete`, `default`.
- **Templates et types** : `template`, `typename`, `concept`, `requires`, `using`, `typedef`, `typeid`.
- **Stockage et qualificateurs** : `static`, `extern`, `thread_local`, `inline`, `const`, `volatile`, `constexpr`, `consteval`, `constinit`.
- **Mémoire** : `new`, `delete`, `nullptr`, `sizeof`, `alignof`, `alignas`.
- **Conversions** : `static_cast`, `dynamic_cast`, `const_cast`, `reinterpret_cast`.
- **Espaces de noms et modules** : `namespace`, `module`, `import`, `export`.
- **Coroutines** : `co_await`, `co_yield`, `co_return`.
- **Divers** : `static_assert`, `asm`, `true`, `false`.

Certains mots (`override`, `final`, `import`, `module`) sont **contextuels** : ils n'ont de sens spécial qu'à certains endroits (après une signature de fonction, au début d'une déclaration) et restent utilisables comme identifiants ailleurs. Le mot-clé `register` est inutilisé depuis C++17 (réservé).

### 3.5 Ponctuation et délimiteurs

- `;` termine une instruction. `{ }` délimitent un bloc, un corps de classe ou une liste d'initialisation.
- `( )` servent aux appels de fonction, au regroupement d'expressions et aux conditions.
- `[ ]` servent à l'indexation et à introduire une lambda ; `[[ ]]` introduit un attribut.
- `< >` encadrent les arguments de template : `std::vector<int>`.
- `::` résolution de portée ; `.` et `->` accès à un membre via un objet ou un pointeur ; `.*` et `->*` accès via un pointeur sur membre.
- `,` sépare des éléments ; c'est aussi un opérateur (chapitre 6).
- `:` introduit une étiquette, un héritage, une liste d'initialisation de membres, ou la boucle `for` sur intervalle.
- `? :` opérateur conditionnel ; `...` paquet de paramètres (templates variadiques) et `catch (...)`.

### 3.6 Les trois sortes d'éléments : déclaration, expression, instruction

Cette distinction organise toute la grammaire :

- Une **expression** calcule une valeur (`a + b`, `f(3)`, `x = 5`). Elle a un **type** et une **catégorie de valeur** (lvalue ou rvalue, chapitre 15).
- Une **instruction** est une unité d'exécution : une expression suivie de `;` (*expression-statement*), un bloc, un `if`, une boucle, un `return`…
- Une **déclaration** introduit un nom ; en C++, une déclaration de variable locale est une **instruction** et peut donc apparaître n'importe où dans un bloc.

```cpp
int main() {
    int a = 3;             // déclaration-instruction
    a + 1;                 // expression-instruction (inutile : résultat ignoré)
    a = a + 1;             // expression d'affectation
    { int b = a; }         // bloc : b n'existe plus après l'accolade fermante
    ;                      // instruction vide
}
```

**Piège — l'analyse la plus contrariante** (*most vexing parse*). Une ligne comme `Widget w();` ne crée **pas** un objet : elle déclare une **fonction** `w` retournant un `Widget`. Pour créer un objet par défaut, écrivez `Widget w;` ou `Widget w{};`. C'est une des raisons de préférer l'initialisation avec accolades.

### 3.7 Attributs

Les **attributs** `[[...]]` donnent des indications au compilateur sans changer la sémantique du programme.

```cpp
#include <cstdlib>
#include <iostream>

[[nodiscard]] int divise(int a, int b) {       // le résultat ne doit pas être ignoré
    return b != 0 ? a / b : 0;
}

[[noreturn]] void quitter(int code) {          // ne retourne jamais
    std::exit(code);
}

[[deprecated("utiliser divise()")]] int ancienne_div(int a, int b) { return a / b; }

int main() {
    int r = divise(10, 2);
    divise(8, 2);                              // avertissement : valeur de retour ignorée
    [[maybe_unused]] int inutile = 0;          // pas d'avertissement « inutilisée »

    switch (r) {
        case 5:
            std::cout << "cinq\n";
            [[fallthrough]];                   // chute volontaire vers le cas suivant
        case 6:
            std::cout << "cinq ou six\n";
            break;
        default:
            break;
    }

    if (r > 100) [[unlikely]] {                // indication de probabilité (C++20)
        quitter(1);
    }
}
```

- `[[nodiscard]]` *(C++17)* : avertit si la valeur de retour est ignorée ; peut aussi s'appliquer à un type.
- `[[maybe_unused]]` *(C++17)* : supprime l'avertissement pour un élément volontairement inutilisé.
- `[[fallthrough]]` *(C++17)* : marque une chute volontaire dans un `switch`.
- `[[deprecated("msg")]]` *(C++14)* : marque une entité obsolète.
- `[[noreturn]]` *(C++11)* : la fonction ne retourne jamais (`exit`, `throw` systématique).
- `[[likely]]` / `[[unlikely]]` *(C++20)* : indication de probabilité de branche.
- `[[no_unique_address]]` *(C++20)* : autorise un membre vide à ne consommer aucun espace.

### À retenir (chapitre 3)

- Le code est découpé en lexèmes ; la casse compte ; la mise en page est libre.
- Les identifiants suivent des règles précises (pas de `__`, pas de `_Majuscule`) et une convention d'équipe.
- Distinguez expression, instruction et déclaration.
- Les attributs `[[ ]]` documentent l'intention au compilateur (`[[nodiscard]]` en priorité).

---

## Chapitre 4 — Types de données et variables

### 4.1 Qu'est-ce qu'un type ?

En C++, **toute valeur et toute variable a un type**, connu à la compilation. Le type détermine :

- la **taille** de l'objet en mémoire (nombre d'octets) ;
- l'**interprétation** des bits (entier, réel, caractère, adresse…) ;
- l'ensemble des **opérations** autorisées (on additionne deux `int`, pas deux pointeurs) ;
- les **conversions** possibles vers d'autres types.

**Définition — objet.** Un *objet* est une zone de mémoire qui contient une valeur d'un certain type. Une *variable* est un objet (ou une référence) nommé. L'*adresse* d'un objet est l'emplacement de son premier octet.

### 4.2 Les types fondamentaux

Le C++ définit des types **natifs**, dits fondamentaux :

- `bool` : booléen (`true` ou `false`), généralement sur 1 octet ;
- `char` : un octet, utilisé pour les caractères et comme plus petit entier ; `signed char` et `unsigned char` en sont des variantes explicites ;
- `short`, `int`, `long`, `long long` : entiers de tailles croissantes, chacun avec une version `unsigned` ;
- `float`, `double`, `long double` : nombres à virgule flottante (simple, double, précision étendue) ;
- `char8_t`, `char16_t`, `char32_t`, `wchar_t` : types de caractères larges et Unicode (chapitre 27) ;
- `void` : « absence de type » (fonction qui ne retourne rien ; `void *`) ;
- `std::nullptr_t` : type du littéral `nullptr`.

La norme ne fixe **pas** les tailles exactes, seulement des garanties minimales et des relations :

- `sizeof(char)` vaut toujours **1** (l'unité de `sizeof` est l'octet C++) ;
- `char` ≥ 8 bits, `short` ≥ 16 bits, `int` ≥ 16 bits, `long` ≥ 32 bits, `long long` ≥ 64 bits ;
- `sizeof(short) <= sizeof(int) <= sizeof(long) <= sizeof(long long)`.

En pratique sur les plateformes 64 bits courantes : `int` = 4 octets, `long long` = 8 octets, `double` = 8 octets ; `long` vaut 8 octets sous Linux/macOS mais **4 sous Windows** — raison de plus pour préférer les types à taille fixe (§4.5).

```cpp
#include <iostream>
#include <limits>

int main() {
    std::cout << "int      : " << sizeof(int) << " octets, max = " << std::numeric_limits<int>::max() << '\n';
    std::cout << "long     : " << sizeof(long) << " octets\n";
    std::cout << "double   : " << sizeof(double) << " octets, epsilon = " << std::numeric_limits<double>::epsilon() << '\n';
    std::cout << "bool     : " << sizeof(bool) << " octet\n";
}
```

`std::numeric_limits<T>` (en-tête `<limits>`) est la façon C++ d'interroger les caractéristiques d'un type : `max()`, `min()`, `lowest()`, `epsilon()`, `digits`, `is_signed`… Les macros du C (`INT_MAX`, `DBL_EPSILON` dans `<climits>` et `<cfloat>`) restent valides.

### 4.3 Entiers signés et non signés

Un entier **non signé** (`unsigned`) représente uniquement des valeurs ≥ 0 ; un entier **signé** représente des valeurs négatives et positives (en **complément à deux**, garanti depuis C++20). Sur 32 bits : `int` va d'environ −2,1 milliards à +2,1 milliards ; `unsigned int` de 0 à environ 4,29 milliards.

#### Débordement : deux régimes très différents

```cpp
#include <iostream>
#include <limits>

int main() {
    unsigned int u = 0;
    u = u - 1;                                   // DÉFINI : arithmétique modulo 2^32
    std::cout << u << '\n';                      // 4294967295

    int max = std::numeric_limits<int>::max();
    // max + 1;                                  // COMPORTEMENT INDÉFINI : débordement signé
    std::cout << max << '\n';
}
```

- Le débordement **non signé** est **défini** : le résultat est calculé modulo 2ⁿ.
- Le débordement **signé** est un **comportement indéfini** : le compilateur a le droit de supposer qu'il n'arrive jamais et d'optimiser en conséquence (par exemple supprimer un test de débordement qu'il juge inutile).

#### Promotions et conversions arithmétiques

Les types plus petits que `int` (`char`, `short`, `bool`) sont **promus en `int`** dès qu'ils participent à une expression arithmétique. Quand deux opérandes ont des types différents, le compilateur applique les **conversions arithmétiques usuelles** : il convertit vers le type « le plus large » (en gros : `long double` > `double` > `float` > entiers par rang). **Piège** : si un opérande est signé et l'autre non signé de même rang, le signé est converti en non signé, et −1 devient un très grand nombre.

```cpp
int a = -1;
unsigned b = 1;
std::cout << (a < b) << '\n';   // 0 ! a est converti en unsigned : 4294967295
```

### 4.4 Nombres à virgule flottante

Les types `float` (32 bits), `double` (64 bits) et `long double` suivent en général la norme **IEEE 754**. Ils représentent les nombres réels de façon **approchée** : un nombre comme 0,1 n'a pas de représentation binaire exacte.

- `double` offre environ **15 à 16 chiffres décimaux** significatifs ; `float`, environ 7.
- Valeurs spéciales : `+inf`, `-inf` (division par zéro flottante) et `NaN` (*Not a Number*, résultat de `0.0 / 0.0`). `NaN` n'est égal à rien, pas même à lui-même ; testez-le avec `std::isnan`.
- **On ne compare pas deux flottants avec `==`** après calcul : comparez avec une tolérance (`std::abs(a - b) < eps`).

```cpp
#include <cmath>
#include <iostream>

int main() {
    double d = 0.1 + 0.2;
    std::cout << (d == 0.3) << '\n';                     // 0 : erreurs d'arrondi
    std::cout << (std::abs(d - 0.3) < 1e-9) << '\n';     // 1 : comparaison avec tolérance
}
```

Par défaut, un littéral réel (`3.14`) est un `double` ; suffixez `f` pour un `float` (`3.14f`) et `L` pour un `long double`.

### 4.5 Entiers à taille fixe : `<cstdint>`

Quand la taille compte (format de fichier, protocole réseau, masque de bits), utilisez les types de `<cstdint>` :

```cpp
#include <cstddef>
#include <cstdint>
#include <iostream>

int main() {
    std::int8_t   a = 100;               // exactement 8 bits, signé
    std::uint8_t  b = 200;               // exactement 8 bits, non signé
    std::int32_t  c = 100000;
    std::uint64_t d = 1'000'000'000'000;
    std::size_t   n = sizeof(int);       // type des tailles et des indices
    std::ptrdiff_t diff = 10;            // différence entre deux pointeurs
    std::byte     o{0xFF};               // octet brut (C++17) : n'est pas un entier

    std::cout << static_cast<int>(a) << ' ' << static_cast<int>(b) << ' ' << c << ' ' << d << ' ' << n << ' ' << diff << '\n';
    std::cout << std::to_integer<int>(o) << '\n';
}
```

- `std::intN_t` / `std::uintN_t` : entiers de **exactement** N bits (N = 8, 16, 32, 64) ; `std::int_leastN_t` et `std::int_fastN_t` : au moins N bits.
- `std::size_t` : type non signé retourné par `sizeof` et par `size()` ; type naturel d'un indice ou d'une taille.
- **Piège** : `std::uint8_t` et `std::int8_t` sont en général des `char` ; `std::cout << b` affiche donc un **caractère**, pas un nombre. Convertissez avec `static_cast<int>`.

### 4.6 Le type `bool`

```cpp
#include <iostream>

int main() {
    bool actif = true;
    bool vide = false;
    int n = 5;
    bool non_nul = n;                                      // tout non-zéro devient true
    std::cout << actif << ' ' << vide << ' ' << non_nul << '\n';          // 1 0 1
    std::cout << std::boolalpha << actif << ' ' << vide << '\n';          // true false
}
```

Toute valeur numérique, pointeur ou objet convertible est utilisable comme **condition** : zéro et `nullptr` valent « faux », tout le reste « vrai ». Un `bool` s'affiche `0` ou `1` sauf avec le manipulateur `std::boolalpha`.

### 4.7 Déclarer, initialiser, affecter

Distinguez bien l'**initialisation** (donner une première valeur à la création de l'objet) et l'**affectation** (remplacer la valeur d'un objet existant). Le C++ offre plusieurs syntaxes d'initialisation :

```cpp
int a;                // pas d'initialisation : valeur indéterminée (à éviter)
int b = 5;            // initialisation par copie
int c(5);             // initialisation directe
int d{5};             // initialisation par liste (recommandée)
int e{};              // initialisation par valeur : 0
// int f{3.7};        // ERREUR : conversion restrictive (narrowing)
int g = 3.7;          // accepté : tronqué à 3, perte silencieuse
```

L'**initialisation par liste** `{}` (C++11) est recommandée car elle :

1. **interdit les conversions avec perte** (*narrowing*) — `int f{3.7};` ne compile pas, `char c{300};` non plus ;
2. s'écrit de la **même façon** pour tous les types (scalaires, tableaux, classes, conteneurs) ;
3. évite l'*analyse la plus contrariante* (chapitre 3) ;
4. avec `{}` vide, initialise à zéro les types fondamentaux.

**Limite** : `std::vector<int> v{3, 4};` crée un vecteur de **deux éléments** (3 et 4), alors que `std::vector<int> v(3, 4);` crée **trois éléments égaux à 4**. Quand un constructeur accepte une liste d'initialisation (`std::initializer_list`), il est prioritaire avec les accolades.

**Pourquoi initialiser ?** Lire une variable locale non initialisée est un comportement indéfini (devenu « comportement erroné » en C++26) : valeur aléatoire, plantage, ou comportement apparemment normal puis cassé après optimisation.

### 4.8 Déduction de type : `auto` et `decltype`

```cpp
#include <iostream>
#include <map>
#include <string>
#include <utility>

int main() {
    auto n = 42;                         // int
    auto pi = 3.14;                      // double
    auto s = std::string{"abc"};         // std::string
    auto texte = "abc";                  // const char *   (et NON std::string !)
    decltype(n) m = 7;                   // m a exactement le type de n

    std::map<std::string, int> ages{{"Ana", 30}, {"Luc", 25}};
    for (const auto &[nom, age] : ages) {          // liaisons structurées (C++17)
        std::cout << nom << " : " << age << '\n';
    }
    auto [x, y] = std::pair{1, 2};       // décomposition d'une paire
    std::cout << n << pi << s << texte << m << x << y << '\n';
}
```

- `auto` demande au compilateur de **déduire** le type depuis l'initialiseur. La variable **doit** être initialisée. `auto` ignore `const` et les références par défaut : écrivez `const auto &` pour une référence constante.
- `decltype(expr)` donne le type exact d'une expression ou d'un nom, sans l'évaluer.
- **Quand utiliser `auto` ?** Quand le type est évident à la lecture (`auto it = v.begin();`) ou long à écrire (types de template). Écrivez le type explicite quand il documente l'intention (`double ratio = ...`).
- Les **liaisons structurées** (`auto [a, b] = ...`, C++17) décomposent une paire, un tuple, un tableau ou une structure en plusieurs variables nommées.

### 4.9 Conversions de types

Une conversion est **implicite** (faite automatiquement par le compilateur) ou **explicite** (un *cast*). Les conversions implicites peuvent faire perdre de l'information (`int g = 3.7;`) ; en C++ on préfère les **casts nommés**, chacun ayant un rôle précis et facile à repérer :

- `static_cast<T>(x)` : conversion **vérifiée à la compilation** (numérique, `void *`, hiérarchie de classes) ; c'est le cast par défaut.
- `dynamic_cast<T>(x)` : conversion **vérifiée à l'exécution** dans une hiérarchie polymorphe (chapitre 21).
- `const_cast<T>(x)` : ajoute ou retire `const` / `volatile` (rarement justifié).
- `reinterpret_cast<T>(x)` : réinterprétation des bits, **dangereuse**, réservée au code de bas niveau.
- `std::bit_cast<T>(x)` *(C++20)* : réinterprétation **sûre** d'un objet vers un autre type de même taille.
- `(T)x` et `T(x)` (casts « à la C ») : **à proscrire**, car ils essaient tous les casts ci-dessus sans avertir.

```cpp
#include <iostream>

int main() {
    int a = 7, b = 2;
    double r1 = a / b;                          // 3 : division entière PUIS conversion
    double r2 = static_cast<double>(a) / b;     // 3.5
    std::cout << r1 << ' ' << r2 << '\n';
}
```

### 4.10 Bonnes pratiques

- **Initialisez** toujours, de préférence avec `{}`.
- Utilisez `double` par défaut pour les réels, `int` pour les compteurs courants, `std::size_t` pour tailles et indices, `<cstdint>` quand la taille compte.
- Évitez de mélanger signé et non signé dans une comparaison (utilisez `std::cmp_less`, chapitre 6).
- Préférez les casts nommés ; chaque cast est un signal d'alerte à relire.
- Utilisez `const` et `constexpr` dès que possible (chapitre 5).

### À retenir (chapitre 4)

- Le type fixe taille, interprétation et opérations ; les tailles ne sont garanties que par des minimums.
- Débordement non signé : défini (modulo) ; débordement signé : comportement indéfini.
- Les flottants sont approchés : on ne les compare pas avec `==`.
- `{}` empêche les pertes silencieuses ; `auto` déduit le type ; `static_cast` remplace le cast à la C.

---

## Chapitre 5 — Constantes et littéraux

### 5.1 Les littéraux

Un **littéral** est une valeur écrite directement dans le code. Son type découle de sa forme et de son suffixe :

- **Entiers** : décimal `42`, octal `052` (préfixe `0`), hexadécimal `0x2A`, binaire `0b101010` *(C++14)*. Suffixes : `u` (non signé), `l` / `L` (`long`), `ll` / `LL` (`long long`), `uz` *(C++23, `std::size_t`)*. Combinables : `42ul`.
- **Séparateur de chiffres** *(C++14)* : l'apostrophe, pour la lisibilité : `1'000'000`, `0b1010'0101`.
- **Réels** : `3.14`, `2.5e-3` (notation scientifique), `1.0f` (`float`), `1.0L` (`long double`).
- **Booléens** : `true`, `false`. **Pointeur nul** : `nullptr`.
- **Caractères** : `'A'`, `'\n'`, `u8'a'` *(UTF-8)*, `u'é'`, `U'é'`, `L'x'`. Un littéral `'a'` est de type `char`.
- **Chaînes** : `"texte"` est de type `const char[N]` (N comprend le `'\0'` final). Préfixes d'encodage : `u8"…"`, `u"…"`, `U"…"`, `L"…"`.
- **Chaînes brutes** : `R"(C:\chemin\sans\échappement)"` — aucun caractère n'est interprété, pratique pour les chemins et les expressions régulières.
- **Littéraux de bibliothèque** (après `using namespace std::literals;`) : `"abc"s` (`std::string`), `"abc"sv` (`std::string_view`), `250ms`, `2h`, `3i` (complexe).

```cpp
#include <chrono>
#include <iostream>
#include <string>
#include <string_view>

using namespace std::literals;

int main() {
    auto s = "bonjour"s;                  // std::string
    auto v = "bonjour"sv;                 // std::string_view
    auto delai = 250ms;                   // std::chrono::milliseconds
    auto brut = R"(ligne 1\nligne 2)";    // le \n est conservé tel quel
    std::cout << s.size() << ' ' << v.size() << ' ' << delai.count() << ' ' << brut << '\n';
}
```

#### Séquences d'échappement

Dans un littéral de caractère ou de chaîne, `\` introduit une séquence spéciale : `\n` (saut de ligne), `\t` (tabulation), `\r` (retour chariot), `\\` (la barre oblique elle-même), `\"` (guillemet), `\'` (apostrophe), `\0` (caractère nul), `\xHH` (valeur hexadécimale), `\uXXXX` et `\UXXXXXXXX` (caractères Unicode).

#### Littéraux définis par l'utilisateur *(C++11)*

On peut créer ses propres suffixes pour des unités ou des types métier :

```cpp
#include <iostream>

constexpr long double operator""_km(long double x) { return x * 1000.0L; }   // convertit en mètres

int main() {
    std::cout << 2.5_km << " m\n";       // 2500 m
}
```

### 5.2 Définir des constantes

Une **constante** est une valeur qu'on s'interdit de modifier. Le C++ propose plusieurs mécanismes, à choisir avec soin :

- **`const`** : l'objet ne peut plus être modifié après son initialisation. La valeur peut être calculée à l'exécution.
- **`constexpr`** *(C++11)* : la valeur est calculable **à la compilation**. Appliqué à une fonction, il l'autorise à être évaluée à la compilation si ses arguments le sont.
- **`consteval`** *(C++20)* : la fonction **doit** être évaluée à la compilation (erreur sinon).
- **`constinit`** *(C++20)* : garantit l'initialisation **statique** d'une variable (donc sans « fiasco » d'ordre d'initialisation), qui reste modifiable.
- **`enum` / `enum class`** : famille de constantes entières nommées (chapitre 19).
- **`#define`** : macro textuelle, **à éviter** (aucun type, aucune portée).

```cpp
#include <array>
#include <iostream>

#define PI_MACRO 3.14159                     // sans point-virgule ! pas de type, pas de portée
constexpr double PI = 3.14159;               // recommandé : typé, dans une portée
constexpr int TAILLE = 4;

constexpr int carre(int x) { return x * x; }         // utilisable à la compilation ET à l'exécution
consteval int cube(int x) { return x * x * x; }      // uniquement à la compilation

int main() {
    const int n = 10;
    // n = 20;                               // ERREUR : constante
    std::array<int, carre(TAILLE)> t{};      // taille calculée à la compilation : 16
    constexpr int c = cube(3);               // 27
    std::cout << PI_MACRO << ' ' << PI << ' ' << n << ' ' << t.size() << ' ' << c << '\n';
}
```

**Pourquoi préférer `constexpr` à `#define` ?** Une macro est remplacée par du texte *avant* la compilation : elle n'a pas de type (aucune vérification), ignore les portées et les espaces de noms, et apparaît telle quelle dans les messages d'erreur. Une variable `constexpr` est un vrai objet typé, soumis aux règles du langage, que le débogueur voit.

**`static_assert`** vérifie une condition **à la compilation** : `static_assert(sizeof(int) >= 4, "int trop petit");`. Combinée à `constexpr`, elle permet de tester du code pendant la compilation.

### 5.3 `const` avec les pointeurs et les références

Avec un pointeur, `const` peut s'appliquer à l'objet pointé, au pointeur lui-même, ou aux deux. **Règle de lecture** : on lit la déclaration **de droite à gauche**.

```cpp
#include <iostream>

int main() {
    int x = 10, y = 20;

    const int *p1 = &x;          // pointeur vers une CONSTANTE : on ne modifie pas *p1
    int *const p2 = &x;          // pointeur CONSTANT : on ne modifie pas p2
    const int *const p3 = &x;    // les deux

    // *p1 = 5;                  // ERREUR
    p1 = &y;                     // OK : le pointeur peut changer de cible
    *p2 = 5;                     // OK : la cible est modifiable
    // p2 = &y;                  // ERREUR : le pointeur est constant
    (void)p3;

    const int &r = x;            // référence constante : lecture seule
    // r = 3;                    // ERREUR
    std::cout << *p1 << ' ' << *p2 << ' ' << r << '\n';
}
```

- `int *const p` se lit « p est un pointeur constant vers un int ».
- `const int *p` (ou `int const *p`) se lit « p est un pointeur vers un int constant ».
- Une **référence constante** `const T &` peut se lier à un temporaire : c'est le mode standard de passage en lecture d'un gros objet.

### 5.4 Constantes prédéfinies

- **`std::numeric_limits<T>`** (`<limits>`) : `max()`, `min()`, `lowest()`, `epsilon()`, `infinity()`. Attention : pour un type flottant, `min()` est le plus petit positif normalisé, `lowest()` le plus négatif.
- **`std::numbers`** *(C++20, `<numbers>`)* : `std::numbers::pi`, `e`, `sqrt2`, `ln2`, `phi`… (`std::numbers::pi_v<float>` pour un autre type).
- **`<climits>` / `<cfloat>`** : `INT_MAX`, `CHAR_BIT`, `DBL_MAX` (héritage du C).
- **`EXIT_SUCCESS`, `EXIT_FAILURE`** (`<cstdlib>`) : codes de sortie.
- **`__cplusplus`** : numéro de la norme (`201703L`, `202002L`, `202302L`…).

### À retenir (chapitre 5)

- Un littéral a un type qui dépend de sa forme et de son suffixe (`1` est `int`, `1u` `unsigned`, `1.0` `double`, `"a"` `const char[2]`).
- Préférez `constexpr` (ou `const`) aux macros ; `consteval` impose le calcul à la compilation.
- Pour les pointeurs, lisez `const` de droite à gauche.

---

## Chapitre 6 — Opérateurs et expressions

### 6.1 Notions préalables

Une **expression** combine des opérandes et des opérateurs pour produire une valeur. Chaque opérateur a une **arité** (unaire, binaire, ternaire), une **priorité** (qui s'applique en premier) et une **associativité** (dans quel sens on regroupe à priorité égale). Chaque expression possède un **type** et une **catégorie de valeur** : une *lvalue* désigne un objet qui a une identité et une adresse (une variable), une *rvalue* est un résultat temporaire.

### 6.2 Opérateurs arithmétiques

```cpp
#include <iostream>

int main() {
    int a = 17, b = 5;
    std::cout << a + b << ' ' << a - b << ' ' << a * b << ' ' << a / b << ' ' << a % b << '\n';   // 22 12 85 3 2
    std::cout << -17 / 5 << ' ' << -17 % 5 << '\n';     // -3 -2 : division tronquée vers zéro, le reste a le signe du dividende
    std::cout << 17 / 5.0 << '\n';                      // 3.4 : un opérande réel suffit
}
```

- `/` entre deux entiers est une **division entière** (tronquée vers zéro) ; entre un entier et un réel, c'est une division réelle.
- `%` (reste) ne s'applique qu'aux **entiers** ; pour les réels, utilisez `std::fmod`. `a / 0` et `a % 0` avec des entiers sont des comportements indéfinis ; en flottant, `x / 0.0` donne `inf` ou `NaN`.
- Les opérateurs `+` et `-` unaires existent aussi (`-x`).

### 6.3 Comparaison

Opérateurs relationnels : `<`, `>`, `<=`, `>=` ; égalité : `==`, `!=`. Le résultat est un `bool`. **Piège** : `a < b < c` ne teste pas « b entre a et c » : il compare `(a < b)` (un booléen) à `c`.

**Opérateur de comparaison à trois voies `<=>`** *(C++20, « vaisseau spatial »)* : retourne un objet `std::strong_ordering`, `weak_ordering` ou `partial_ordering` exprimant « inférieur », « égal » ou « supérieur » en une seule opération. Pour une classe, `auto operator<=>(const T &) const = default;` génère automatiquement `<`, `<=`, `>`, `>=` (chapitre 18).

### 6.4 Opérateurs logiques et évaluation paresseuse

`&&` (ET), `||` (OU), `!` (NON). Les opérateurs `&&` et `||` utilisent l'**évaluation paresseuse** (*short-circuit*) : l'opérande de droite n'est évalué que si nécessaire. Cette propriété est garantie par la norme et sert à écrire des gardes :

```cpp
#include <iostream>

bool test(const char *nom, bool v) {
    std::cout << "évalue " << nom << '\n';
    return v;
}

int main() {
    if (test("A", false) && test("B", true)) {}     // B n'est PAS évalué (A est faux)
    if (test("C", true) || test("D", false)) {}     // D n'est PAS évalué (C est vrai)

    int *p = nullptr;
    if (p != nullptr && *p > 0) {                   // sûr : *p n'est lu que si p est valide
        std::cout << "positif\n";
    }
}
```

Pour cette raison, on **ne surcharge pas** `&&`, `||` ni `,` pour des types utilisateur : la surcharge perdrait l'évaluation paresseuse et l'ordre garanti.

### 6.5 Affectation et opérateurs composés

`=` copie une valeur dans un objet existant et **retourne** cet objet (d'où `a = b = 0;`). Les opérateurs composés combinent calcul et affectation : `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `|=`, `^=`. **Piège classique** : `if (x = 5)` est une affectation (toujours vraie), pas une comparaison ; `-Wall` le signale.

### 6.6 Incrémentation et décrémentation

```cpp
#include <iostream>

int main() {
    int i = 5;
    int a = i++;       // suffixe : a reçoit l'ANCIENNE valeur (5), puis i devient 6
    int b = ++i;       // préfixe : i devient 7, puis b reçoit 7
    std::cout << a << ' ' << b << ' ' << i << '\n';     // 5 7 7
}
```

La forme suffixe doit conserver l'ancienne valeur : pour un itérateur ou un objet, cela crée une copie temporaire inutile. **Utilisez `++i` par défaut.**

### 6.7 Opérateur conditionnel (ternaire)

`condition ? valeur_si_vrai : valeur_si_faux` est une **expression** (contrairement à `if`, qui est une instruction). Les deux branches doivent avoir des types compatibles ; à utiliser pour les cas simples, jamais imbriqué sur plusieurs niveaux.

```cpp
int max = (a > b) ? a : b;
std::cout << (a % 2 == 0 ? "pair" : "impair") << '\n';
```

### 6.8 `sizeof`, `alignof`, virgule

- `sizeof(T)` ou `sizeof expr` : taille **en octets** (évaluée à la compilation, de type `std::size_t`). Sur un tableau C, donne la taille totale ; sur un pointeur, la taille du pointeur. Pour compter les éléments, préférez `std::size(t)` *(C++17)*, qui refuse de compiler sur un pointeur.
- `alignof(T)` : contrainte d'**alignement** du type en mémoire (chapitre 18).
- **Opérateur virgule** `a, b` : évalue `a`, l'ignore, puis évalue `b` et retourne sa valeur. On le rencontre surtout dans un `for` : `for (int i = 0, j = 10; i < j; ++i, --j)`.

### 6.9 Priorité et associativité

Du plus prioritaire au moins prioritaire :

1. `::` (résolution de portée)
2. suffixes : `()` appel, `[]`, `.`, `->`, `++`, `--` (associativité gauche → droite)
3. préfixes : `++`, `--`, `+`, `-`, `!`, `~`, `*` (déréférencement), `&` (adresse), `sizeof`, `new`, `delete`, cast (droite → gauche)
4. `.*` et `->*`
5. `*`, `/`, `%`
6. `+`, `-`
7. `<<`, `>>`
8. `<=>` *(C++20)*
9. `<`, `<=`, `>`, `>=`
10. `==`, `!=`
11. `&` (ET bit à bit), 12. `^`, 13. `|`
12. `&&`, 15. `||`
13. `? :`, `=` et opérateurs composés, `throw` (droite → gauche)
14. `,`

**Piège** : `std::cout << a & b` s'interprète `(std::cout << a) & b` ; écrivez `std::cout << (a & b)`. De même, `==` est plus prioritaire que `&` : `x & 1 == 0` signifie `x & (1 == 0)`. **Dans le doute, parenthésez.**

### 6.9 bis Ordre d'évaluation

Priorité et ordre d'évaluation sont deux choses différentes. Dans `f() + g()`, la priorité dit que `+` est appliqué après ; elle ne dit **pas** laquelle de `f` ou `g` s'exécute en premier. Depuis C++17, l'ordre est défini pour `a << b`, `a >> b`, `a = b`, `a.f(b)` et `a[b]` (le membre de gauche est évalué d'abord), mais **pas** pour les arguments d'une fonction ni pour les opérandes de `+`, `*`, etc. Modifier deux fois la même variable dans une expression sans ordre défini est un comportement indéfini :

```cpp
int x = 3;
// x = x++ + ++x;    // comportement indéfini
// int d = 10 / 0;   // comportement indéfini : division entière par zéro
// int s = 1 << 40;  // comportement indéfini : décalage >= largeur du type
```

### 6.10 Arithmétique sûre

Le C++ standard n'a pas encore d'équivalent des fonctions `ckd_add` du C23, mais fournit des outils pour maîtriser les débordements et les comparaisons mixtes :

```cpp
#include <cstdint>
#include <iostream>
#include <utility>

int main() {
    int a = -1;
    unsigned b = 1;
    std::cout << std::cmp_less(a, b) << '\n';                 // 1 : comparaison mathématiquement correcte (C++20)
    std::cout << std::in_range<std::uint8_t>(300) << '\n';    // 0 : 300 ne tient pas dans un uint8_t (C++20)
    std::cout << std::in_range<std::uint8_t>(200) << '\n';    // 1
}
```

- `std::cmp_equal`, `cmp_less`, `cmp_greater`… *(C++20)* : comparaisons correctes entre entiers de signes différents.
- `std::in_range<T>(v)` *(C++20)* : `v` est-il représentable dans `T` ?
- `std::add_sat`, `sub_sat`, `mul_sat`, `div_sat` *(C++26)* : arithmétique **saturée** (le résultat est borné au lieu de déborder).
- `__builtin_add_overflow` (extension GCC/Clang) et bibliothèques (Boost.SafeNumerics) pour détecter les débordements.

### À retenir (chapitre 6)

- Division entière tronquée vers zéro ; `%` réservé aux entiers.
- `&&` et `||` sont paresseux ; ne mélangez pas `&` et `&&`.
- Préférez `++i` ; parenthésez dès que la priorité n'est pas évidente.
- Débordement signé, division par zéro entière, décalage invalide, modification multiple non ordonnée : comportements indéfinis.

---

## Chapitre 7 — Entrées et sorties

### 7.1 Le modèle des flux

En C++, les entrées/sorties reposent sur la notion de **flux** (*stream*) : une suite d'octets ou de caractères qui circule d'une source vers une destination. Le même modèle vaut pour la console, les fichiers (chapitre 22) et les chaînes en mémoire. Un flux de sortie reçoit des données avec l'opérateur d'**insertion** `<<` ; un flux d'entrée en extrait avec l'opérateur d'**extraction** `>>`. Les deux opérateurs sont **typés** : le compilateur choisit la bonne conversion selon le type de la valeur, ce qui supprime les erreurs de spécificateur de format de `printf` / `scanf`.

Quatre flux standards sont fournis par `<iostream>` :

- `std::cin` : entrée standard (clavier ou redirection), tamponnée ;
- `std::cout` : sortie standard (écran), tamponnée ;
- `std::cerr` : sortie d'erreurs, **non tamponnée** (affichage immédiat) ;
- `std::clog` : journal, sortie d'erreurs tamponnée.

Le **tampon** est une zone mémoire intermédiaire : les caractères y sont accumulés puis transmis en bloc, ce qui accélère les écritures. Le tampon de `cout` est vidé quand il est plein, quand on lit sur `cin` (les deux flux sont liés), à la sortie du programme, ou explicitement avec `std::flush`.

Les redirections du shell exploitent cette séparation :

```bash
./prog > sortie.txt 2> erreurs.txt    # cout et cerr vers des fichiers différents
./prog < entree.txt                   # cin lit dans un fichier
```

### 7.2 Affichage avec `std::cout`

```cpp
#include <iomanip>
#include <iostream>

int main() {
    int n = 42;
    double pi = 3.14159265;

    std::cout << "n = " << n << ", pi = " << pi << '\n';              // chaîner les <<
    std::cout << std::fixed << std::setprecision(2) << pi << '\n';    // 3.14
    std::cout << std::setw(8) << n << '|' << std::left << std::setw(8) << n << "|\n";   //       42|42      |
    std::cout << std::hex << n << std::dec << '\n';                   // 2a
    std::cout << std::boolalpha << true << '\n';                      // true
}
```

Les **manipulateurs** (`<iomanip>` et `<ios>`) modifient l'état du flux : `std::setw(n)` (largeur du *prochain* champ seulement), `std::setprecision(n)`, `std::setfill(c)`, `std::fixed`, `std::scientific`, `std::left`, `std::right`, `std::hex`, `std::dec`, `std::oct`, `std::showbase`, `std::boolalpha`. Attention : la plupart restent actifs jusqu'à nouvel ordre (`std::hex` s'applique à tous les entiers suivants), sauf `setw`.

**`'\n'` ou `std::endl` ?** `std::endl` écrit `'\n'` **puis vide le tampon** : coûteux dans une boucle. Écrivez `'\n'` et laissez le système vider le tampon.

### 7.3 Formatage moderne : `std::format` et `std::print`

`std::format` *(C++20)* produit une `std::string` à partir d'une chaîne de format à la Python ; `std::print` / `std::println` *(C++23)* l'écrivent directement dans un flux. Le format est **vérifié à la compilation** (nombre et types d'arguments), contrairement à `printf`.

```cpp
#include <format>
#include <iostream>
#include <print>
#include <string>

int main() {
    int n = 42;
    std::string ligne = std::format("{:>8}|{:<8}|{:^8}|", n, n, n);   // C++20
    std::cout << ligne << '\n';

    double pi = 3.14159265;
    std::println("{:08.3f} {:#x} {:b} {:+d}", pi, 255, 5, 7);          // 0003.142 0xff 101 +7
    std::println(stderr, "message d'erreur");                          // vers un flux C
}
```

Syntaxe d'un champ : `{[position]:[remplissage][alignement][signe][#][0][largeur][.précision][type]}`.

- Alignement : `<` gauche, `>` droite, `^` centré ; remplissage : `{:*^10}` centre avec des `*`.
- Type : `d` décimal, `x`/`X` hexadécimal, `o` octal, `b` binaire, `f` fixe, `e` scientifique, `g` général, `s` chaîne, `c` caractère.
- `{:#x}` ajoute le préfixe `0x` ; `{:08d}` complète avec des zéros ; `{:+d}` impose le signe ; `{1} {0}` choisit les arguments par position ; `{{` et `}}` écrivent des accolades littérales.
- La disponibilité dépend de la bibliothèque standard : `std::format` à partir de GCC 13 (et Clang/MSVC récents), `std::print` à partir de GCC 14.

### 7.4 Lecture avec `std::cin`

```cpp
#include <cstdlib>
#include <iostream>
#include <string>

int main() {
    int age;
    double taille;
    std::cout << "Âge et taille : ";
    if (!(std::cin >> age >> taille)) {            // échec de lecture : le flux passe en état d'erreur
        std::cerr << "Entrée invalide\n";
        return EXIT_FAILURE;
    }
    std::cout << "Âge = " << age << ", taille = " << taille << '\n';

    std::string mot;
    std::cin >> mot;                               // lit UN mot ; pas de dépassement de tampon possible
    std::cout << "mot = " << mot << '\n';
}
```

Fonctionnement de `>>` : il **saute les espaces** (espace, tabulation, saut de ligne), lit des caractères jusqu'au premier qui ne convient pas au type demandé, et **laisse le reste dans le tampon**, y compris le `'\n'` final. Si la lecture échoue (on tape `abc` pour un `int`), le flux passe en **état d'erreur** (`failbit`) : l'expression `std::cin >> x` se convertit alors en `false`, et **toutes les lectures suivantes échouent** tant que l'on n'a pas appelé `clear()`.

### 7.5 Lire une ligne entière : `std::getline`

```cpp
#include <iostream>
#include <string>

int main() {
    std::string nom;
    std::cout << "Votre nom complet : ";
    std::getline(std::cin, nom);             // lit toute la ligne (espaces compris), sans le '\n'
    std::cout << "Bonjour, " << nom << " !\n";
}
```

La `std::string` s'agrandit automatiquement : aucun tampon à dimensionner, donc plus de risque de dépassement (contrairement à `gets` ou `scanf("%s")` du C).

#### Lecture robuste d'un nombre

Le schéma « lire la ligne, puis convertir » est le plus sûr. `std::from_chars` *(C++17)* convertit sans exception ni allocation et indique précisément où la conversion s'est arrêtée :

```cpp
#include <charconv>
#include <iostream>
#include <optional>
#include <string>

std::optional<int> lire_int(const std::string &invite) {
    std::string ligne;
    std::cout << invite;
    if (!std::getline(std::cin, ligne)) return std::nullopt;       // fin de fichier ou erreur

    int valeur{};
    const char *debut = ligne.data();
    const char *fin = debut + ligne.size();
    auto [ptr, ec] = std::from_chars(debut, fin, valeur);
    if (ec != std::errc{} || ptr != fin) return std::nullopt;      // erreur, dépassement ou caractères en trop
    return valeur;
}

int main() {
    if (auto n = lire_int("Un entier : ")) std::cout << "double = " << *n * 2 << '\n';
    else std::cout << "Entrée invalide\n";
}
```

#### Mélanger `>>` et `getline` : vider le tampon

Après `std::cin >> n`, le `'\n'` tapé par l'utilisateur reste dans le tampon : un `getline` immédiat lit donc une **ligne vide**. On purge avec `ignore` :

```cpp
#include <iostream>
#include <limits>
#include <string>

int main() {
    int n;
    std::cin >> n;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');   // jette le reste de la ligne
    std::string phrase;
    std::getline(std::cin, phrase);                                       // fonctionne maintenant

    if (!std::cin) {                                                      // récupération après une erreur de format
        std::cin.clear();                                                 // 1. remet le flux en état « bon »
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');   // 2. vide la ligne fautive
    }
}
```

### 7.6 États d'un flux

Chaque flux mémorise son état : `good()` (tout va bien), `eof()` (fin de données **atteinte par une lecture**), `fail()` (échec de format ou d'opération), `bad()` (erreur irrécupérable). Un flux en état d'erreur ignore toutes les opérations jusqu'à `clear()`. Testez **le résultat de l'opération de lecture**, pas `eof()` avant elle : `while (std::cin >> x) { ... }` est correct, `while (!std::cin.eof())` ne l'est pas.

### 7.7 Autres fonctions utiles

- `std::cout.put(c)`, `std::cout.write(p, n)` : écrire un caractère, `n` octets.
- `std::cin.get()` lit un caractère (espaces compris) ; `std::cin.peek()` le consulte sans le consommer ; `std::cin >> std::ws` saute les espaces.
- `std::cout << std::flush` vide le tampon.
- `std::ios::sync_with_stdio(false);` découple les flux C++ de ceux du C : lectures et écritures nettement plus rapides, mais on ne doit plus mélanger `cout` et `printf`.
- `printf` / `scanf` (`<cstdio>`) fonctionnent mais ne sont **pas typés** : `printf("%d", un_double)` est un comportement indéfini. Préférez flux ou `std::format`.

### À retenir (chapitre 7)

- Flux = abstraction commune console / fichiers / chaînes ; `<<` pour écrire, `>>` pour lire.
- Lisez les lignes avec `std::getline`, puis convertissez et validez ; testez toujours le résultat d'une lecture.
- `'\n'` plutôt que `std::endl` ; `std::format` / `std::println` pour un formatage sûr.

---

## Chapitre 8 — Structures de contrôle

Les structures de contrôle modifient l'ordre d'exécution : elles permettent de **choisir** (conditions) et de **répéter** (boucles). Le C++ en ajoute une troisième famille : le traitement des erreurs par **exceptions**.

### 8.1 Conditions : `if`, `else if`, `else`

```cpp
#include <iostream>
#include <map>
#include <string>

int main() {
    int note = 14;
    if (note >= 16) {
        std::cout << "Très bien\n";
    } else if (note >= 12) {
        std::cout << "Bien\n";
    } else {
        std::cout << "À améliorer\n";
    }

    std::map<std::string, int> stock{{"pomme", 3}};
    if (auto it = stock.find("pomme"); it != stock.end()) {    // initialiseur dans if (C++17)
        std::cout << "pommes : " << it->second << '\n';
    }                                                          // 'it' n'existe plus ici

    if constexpr (sizeof(void *) == 8) {                       // condition évaluée à la compilation (C++17)
        std::cout << "64 bits\n";
    }
}
```

- La condition est convertie en `bool`. Utilisez **toujours des accolades**, même pour une seule instruction : cela évite des bogues lors d'une modification ultérieure.
- **`if` avec initialiseur** *(C++17)* : `if (init; condition)` limite la portée de la variable au `if` et à ses `else`.
- **`if constexpr`** *(C++17)* : la condition est évaluée **à la compilation** ; la branche non retenue n'est pas compilée (indispensable dans les templates, chapitre 20).
- `if consteval` *(C++23)* : distingue l'évaluation à la compilation de l'exécution.
- **Piège du « else pendant »** : un `else` se rattache au `if` le plus proche ; les accolades lèvent toute ambiguïté.

### 8.2 Sélection multiple : `switch`

```cpp
#include <iostream>

int main() {
    int jour = 3;
    switch (jour) {
        case 1:
        case 7:
            std::cout << "Week-end\n";
            break;
        case 2: case 3: case 4: case 5: case 6:
            std::cout << "Semaine\n";
            break;
        default:
            std::cout << "Jour invalide\n";
    }

    switch (int reste = jour % 2; reste) {        // initialiseur dans switch (C++17)
        case 0: std::cout << "pair\n"; break;
        default: std::cout << "impair\n"; break;
    }
}
```

- L'expression du `switch` doit être de type **entier, caractère ou énumération** (pas de chaînes, pas de flottants). Les étiquettes `case` sont des **constantes de compilation** distinctes.
- **Sans `break`, l'exécution continue** dans le `case` suivant (*fall-through*). Si c'est voulu, écrivez `[[fallthrough]];` ; sinon le compilateur avertit.
- On ne peut pas déclarer de variable avec initialisation directement dans un `case` sans la placer dans un bloc `{ }` (le saut vers un autre `case` passerait par-dessus l'initialisation).
- Sur une `enum class`, **omettez `default`** : avec `-Wall`, le compilateur signale alors tout énumérateur oublié.

### 8.3 Boucles

```cpp
#include <iostream>
#include <ranges>
#include <vector>

int main() {
    int i = 0;
    while (i < 3) { std::cout << i++ << ' '; }                  // teste d'abord : 0 1 2
    std::cout << '\n';

    do { std::cout << "exécuté au moins une fois\n"; } while (false);   // teste ensuite

    for (int k = 0; k < 3; ++k) std::cout << k << ' ';          // for classique : init; condition; pas
    std::cout << '\n';

    std::vector<int> v{10, 20, 30};
    for (int x : v) std::cout << x << ' ';                      // for sur intervalle (C++11) : copie
    for (const int &x : v) std::cout << x << ' ';               // lecture sans copie
    for (int &x : v) x *= 2;                                    // modification en place
    std::cout << '\n';

    for (int k : std::views::iota(1, 4)) std::cout << k << ' ';        // 1 2 3 (C++20)
    for (int x : v | std::views::reverse) std::cout << x << ' ';       // parcours inversé (C++20)
    std::cout << '\n';
}
```

- **`while`** : teste la condition **avant** chaque tour ; peut ne jamais s'exécuter.
- **`do … while`** : teste **après** ; s'exécute au moins une fois.
- **`for (init; condition; pas)`** : trois parties facultatives ; la variable déclarée dans `init` n'existe que dans la boucle. `for (;;)` est une boucle infinie.
- **`for` sur intervalle** (*range-based for*, C++11) : `for (T x : conteneur)` parcourt tous les éléments d'un tableau, d'un conteneur ou de tout objet disposant de `begin()` / `end()`. Choisissez la forme de `T` : `int x` (copie), `const int &x` (lecture sans copie, **forme par défaut pour les gros objets**), `int &x` (modification), `auto &&x` (générique). Depuis C++20, un initialiseur est permis : `for (auto v = f(); auto x : v)`.
- **Vues et ranges** *(C++20)* : `std::views::iota`, `filter`, `transform`, `reverse`… se combinent avec `|` et s'évaluent paresseusement.

### 8.4 `break`, `continue`, `goto`

- `break` quitte immédiatement la boucle (ou le `switch`) la plus interne.
- `continue` passe à l'itération suivante.
- `goto étiquette;` saute vers une étiquette de la même fonction. Il **ne peut pas** sauter par-dessus l'initialisation d'une variable. En C++, le schéma C `goto nettoyage;` est inutile : le nettoyage est automatique grâce aux **destructeurs** (RAII, chapitre 10). Pour sortir de boucles imbriquées, placez-les dans une fonction et utilisez `return`.

```cpp
for (int i = 0; i < 10; ++i) {
    if (i == 3) continue;      // saute 3
    if (i == 6) break;         // arrête à 6
    std::cout << i << ' ';     // 0 1 2 4 5
}
```

### 8.5 Pièges classiques

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v{1, 2, 3};

    for (int i = 0; i < 3; ++i);                 // ';' en trop : la boucle ne fait rien
    { std::cout << "exécuté une seule fois\n"; }

    // for (std::size_t i = v.size() - 1; i >= 0; --i) { }   // boucle infinie : un non signé est toujours >= 0
    for (std::size_t i = v.size(); i-- > 0; ) std::cout << v[i] << ' ';   // idiome correct
    std::cout << '\n';

    // for (int x : v) v.push_back(x);           // invalide les itérateurs : comportement indéfini
}
```

- **`;` parasite** après un `for`, `while` ou `if`.
- **Compteur non signé** décrémenté jusqu'à zéro (boucle infinie ou boucle qui saute le dernier tour).
- **Modifier un conteneur pendant son parcours** (ajout ou suppression) : les itérateurs deviennent invalides.
- **Copie involontaire** dans `for (auto x : v)` quand les éléments sont de gros objets : écrivez `const auto &x`.
- **Condition mal formée** : `while (x = 0)` (affectation).

### 8.6 Exceptions : `try`, `catch`, `throw`

Une **exception** signale une erreur en interrompant le déroulement normal : le programme **remonte la pile d'appels**, en **détruisant les objets locaux** au passage (*stack unwinding*), jusqu'à trouver un `catch` compatible.

```cpp
#include <iostream>
#include <stdexcept>

double diviser(double a, double b) {
    if (b == 0.0) throw std::invalid_argument("division par zéro");   // lève une exception
    return a / b;
}

int main() {
    try {
        std::cout << diviser(10, 2) << '\n';        // 5
        std::cout << diviser(1, 0) << '\n';         // lève : la suite du bloc try est ignorée
    } catch (const std::invalid_argument &e) {      // capture par référence constante
        std::cerr << "Argument invalide : " << e.what() << '\n';
    } catch (const std::exception &e) {             // toute exception standard
        std::cerr << "Erreur : " << e.what() << '\n';
    } catch (...) {                                 // n'importe quoi d'autre
        std::cerr << "Erreur inconnue\n";
    }
}
```

La hiérarchie standard (`<stdexcept>`) : `std::exception` (base, méthode `what()`) ; `std::logic_error` (`invalid_argument`, `out_of_range`, `domain_error`, `length_error`) ; `std::runtime_error` (`range_error`, `overflow_error`, `underflow_error`) ; `std::bad_alloc` (échec d'allocation) ; `std::bad_cast` (échec de `dynamic_cast` sur une référence).

Règles : **lancer par valeur, capturer par référence constante** ; ordonner les `catch` du plus **spécifique** au plus **général** ; ne pas utiliser les exceptions pour le flux de contrôle ordinaire. La sûreté en cas d'exception (`noexcept`, garanties) est traitée au chapitre 29.

### À retenir (chapitre 8)

- Accolades toujours ; `if` et `switch` acceptent un initialiseur (C++17).
- `for` sur intervalle avec `const auto &` est la boucle par défaut sur un conteneur.
- `switch` : un `break` par cas, ou `[[fallthrough]]` explicite.
- Exceptions : `throw` par valeur, `catch` par référence constante, du plus spécifique au plus général.

---

## Chapitre 9 — Fonctions

### 9.1 Pourquoi des fonctions ?

Une **fonction** est un bloc de code nommé, réutilisable, qui reçoit des **paramètres** et peut retourner une **valeur**. Elle permet de découper un problème, d'éviter la duplication, de tester isolément et de donner des noms à des idées. Règle d'or : **une fonction fait une seule chose**, porte un nom explicite et reste courte.

### 9.2 Définir et appeler

```cpp
#include <iostream>
#include <string>

int somme(int a, int b) { return a + b; }                      // type de retour, nom, paramètres
auto produit(int a, int b) { return a * b; }                   // type de retour déduit (C++14)
auto moyenne(int a, int b) -> double { return (a + b) / 2.0; } // type de retour final

void afficher(const std::string &msg) {                        // void : ne retourne rien
    std::cout << msg << '\n';
}

[[nodiscard]] bool est_pair(int n) { return n % 2 == 0; }

int main() {
    afficher("Bonjour");
    std::cout << somme(2, 3) << ' ' << produit(2, 3) << ' ' << moyenne(2, 3) << ' ' << est_pair(4) << '\n';
}
```

- La **signature** d'une fonction comprend son nom et les types de ses paramètres (pas le type de retour).
- Une fonction doit être **déclarée avant son premier appel**. Soit on la définit avant `main`, soit on écrit un **prototype** :

```cpp
int carre(int x);                    // déclaration (prototype)

int main() {
    std::cout << carre(6) << '\n';   // 36
}

int carre(int x) { return x * x; }   // définition
```

- `return valeur;` termine la fonction et transmet la valeur. Une fonction non `void` dont un chemin d'exécution n'a pas de `return` provoque un comportement indéfini.

### 9.3 Passage des arguments : valeur, référence, pointeur

Par défaut, les arguments sont passés **par valeur** : la fonction travaille sur une **copie**. Pour modifier l'original ou éviter une copie coûteuse, on passe une **référence** (chapitre 17) ou un **pointeur** (chapitre 13).

```cpp
#include <iostream>
#include <string>

void incremente_copie(int x) { ++x; }                        // modifie la copie : sans effet
void incremente_ref(int &x) { ++x; }                         // modifie l'original
void incremente_ptr(int *x) { if (x) ++*x; }                 // modifie l'original via un pointeur
std::size_t longueur(const std::string &s) { return s.size(); }   // lecture sans copie

int main() {
    int n = 1;
    incremente_copie(n); std::cout << n << ' ';      // 1
    incremente_ref(n);   std::cout << n << ' ';      // 2
    incremente_ptr(&n);  std::cout << n << '\n';     // 3
    std::cout << longueur("abc") << '\n';            // 3
}
```

Guide de choix :

- **Petit type** (`int`, `double`, pointeur, `std::string_view`, `std::span`) : par **valeur**.
- **Gros objet en lecture seule** : `const T &`.
- **Argument à modifier** : `T &`.
- **Argument optionnel** : pointeur (`nullptr` = absent) ou `std::optional`.
- **Résultat** : de préférence la **valeur de retour** (un `struct`, un `std::pair`, un `std::tuple`, un `std::optional`) plutôt qu'un paramètre de sortie.
- **Consommer ou stocker l'objet** (*sink*) : par valeur puis `std::move`, ou `T &&`.

### 9.4 Retourner des valeurs

On retourne **par valeur** : depuis C++17, retourner un temporaire n'effectue **aucune copie** (élision garantie), et retourner une variable locale nommée est optimisé (NRVO) ou **déplacé**. **Ne retournez jamais** une référence ou un pointeur vers une variable locale : elle est détruite à la sortie de la fonction.

```cpp
const std::string &mauvaise() {
    std::string local = "temporaire";
    return local;                       // DANGER : référence vers une variable détruite
}

std::string bonne() {
    std::string local = "ok";
    return local;                       // retour par valeur : sûr et efficace
}
```

### 9.5 Surcharge et arguments par défaut

Plusieurs fonctions peuvent porter le **même nom** si leurs **paramètres** diffèrent (nombre ou types) : c'est la **surcharge**. Le compilateur choisit la meilleure correspondance (correspondance exacte, puis promotions, puis conversions).

```cpp
#include <iostream>
#include <string>

int    absolu(int x)    { return x < 0 ? -x : x; }
double absolu(double x) { return x < 0 ? -x : x; }

void afficher(const std::string &s, int fois = 1, char sep = '\n') {   // arguments par défaut
    for (int i = 0; i < fois; ++i) std::cout << s << sep;
}

int main() {
    std::cout << absolu(-3) << ' ' << absolu(-2.5) << '\n';   // int puis double
    afficher("a");
    afficher("b", 2);
    afficher("c", 2, ' ');
}
```

- Le **type de retour seul** ne distingue pas deux surcharges.
- Les arguments par défaut se placent **à la fin** de la liste et se déclarent **une seule fois** (dans le prototype).
- Un appel **ambigu** (`absolu(3L)` avec les versions `int` et `double`) est une erreur de compilation ; levez l'ambiguïté par un cast.

### 9.6 Fonctions variadiques

L'ellipse `...` du C (`<cstdarg>`) n'est pas typée : **déconseillée**. Le C++ propose des alternatives sûres :

```cpp
#include <initializer_list>
#include <iostream>

int somme(std::initializer_list<int> valeurs) {            // même type pour tous les éléments
    int s = 0;
    for (int v : valeurs) s += v;
    return s;
}

template <typename... Args>
auto somme_t(Args... args) { return (args + ...); }        // expression de repli (C++17)

template <typename... Args>
void afficher_tout(const Args &...args) {                  // types hétérogènes
    ((std::cout << args << ' '), ...);
    std::cout << '\n';
}

int main() {
    std::cout << somme({1, 2, 3, 4}) << '\n';       // 10
    std::cout << somme_t(1, 2, 3.5) << '\n';        // 6.5
    afficher_tout("x =", 5, 'c', 2.5);              // x = 5 c 2.5
}
```

### 9.7 `inline`, `constexpr`, `consteval`, `noexcept`

- **`inline`** : autorise plusieurs définitions identiques de la même fonction (une définition par unité de traduction), ce qui permet de la définir dans un en-tête. Le compilateur reste libre d'insérer (ou non) le corps à l'endroit de l'appel.
- **`constexpr`** : la fonction peut être évaluée à la compilation si ses arguments le sont ; elle reste utilisable à l'exécution.
- **`consteval`** *(C++20)* : évaluation **obligatoire** à la compilation.
- **`noexcept`** : promet de ne lever aucune exception (permet des optimisations ; une exception qui s'échappe appelle `std::terminate`).

```cpp
constexpr int factorielle(int n) { return n <= 1 ? 1 : n * factorielle(n - 1); }
static_assert(factorielle(5) == 120);          // vérifié par le compilateur
consteval int au_carre(int x) { return x * x; }
int addition(int a, int b) noexcept { return a + b; }
```

### 9.8 Organiser le code : en-têtes et sources

Dès qu'un programme dépasse quelques dizaines de lignes, on sépare **interface** (déclarations dans un en-tête `.hpp`) et **implémentation** (définitions dans un `.cpp`) :

```cpp
// maths.hpp
#pragma once                                      // garde d'inclusion (chapitre 24)
namespace maths {
    int carre(int x);                             // déclaration : la définition est dans maths.cpp
    inline int cube(int x) { return x * x * x; } // inline : définition autorisée dans l'en-tête
}
```

```cpp
// maths.cpp
#include "maths.hpp"
namespace maths {
    int carre(int x) { return x * x; }
}
```

```cpp
// main.cpp
#include <iostream>
#include "maths.hpp"

int main() {
    std::cout << maths::carre(5) << ' ' << maths::cube(2) << '\n';   // 25 8
}
```

```bash
g++ -Wall -Wextra -std=c++20 main.cpp maths.cpp -o prog
```

Ce qu'on place dans un **en-tête** : déclarations, définitions de classes, **templates**, fonctions `inline` / `constexpr`, constantes. Ce qu'on place dans un **`.cpp`** : définitions de fonctions ordinaires. Une fonction ordinaire définie dans un en-tête inclus par deux fichiers provoque une erreur d'édition de liens (violation de l'ODR).

Pour appeler du C depuis du C++ (ou l'inverse), on désactive le décorage des noms avec `extern "C" { #include "bibliotheque_c.h" }`.

### 9.9 Bonnes pratiques

- Une fonction = une tâche ; nom explicite (verbe pour une action, adjectif ou question pour un test).
- Gros objet en lecture : `const T &` ; petit type : valeur ; retour : valeur.
- `[[nodiscard]]` sur les fonctions dont le résultat compte ; `noexcept` quand c'est vrai ; `constexpr` quand c'est possible.
- Évitez les paramètres de sortie : retournez un `struct`, un `std::pair`/`std::tuple` ou un `std::optional`.
- Documentez les **préconditions** (contrats en C++26, chapitre 29).

### À retenir (chapitre 9)

- Passage par valeur = copie ; référence = alias ; `const T &` pour lire les gros objets.
- Ne retournez jamais une référence vers un local ; retournez par valeur.
- Surcharge selon les paramètres ; arguments par défaut à la fin.
- Déclarations dans les en-têtes, définitions dans les `.cpp` (sauf `inline`, `constexpr`, templates).

---

## Chapitre 10 — Portée et durée de vie des variables

Deux notions distinctes et souvent confondues : la **portée** (*où* un nom est visible dans le code) et la **durée de vie** (*quand* un objet existe en mémoire). Elles coïncident pour les variables locales ordinaires, mais pas toujours.

### 10.1 Les portées

La **portée** d'un nom est la région du texte source où ce nom peut être utilisé.

```cpp
#include <iostream>

int globale = 100;                  // portée de fichier (espace de noms global)

namespace app { int config = 7; }   // portée d'espace de noms

int main() {
    int x = 10;
    {
        int x = 20;                 // masque le x externe (ombrage)
        std::cout << x << '\n';     // 20
    }
    std::cout << x << ' ' << ::globale << '\n';       // 10 100   (:: = portée globale)

    for (int i = 0; i < 2; ++i) {}                    // 'i' n'existe que dans la boucle
    if (int y = x * 2; y > 5) {                       // 'y' limité au if / else
        std::cout << y << ' ' << app::config << '\n';
    }
}
```

- **Portée de bloc** `{ }` : du point de déclaration à l'accolade fermante. Les variables des `for`, `if`, `switch`, `while` ont pour portée la structure elle-même.
- **Portée de fonction** : concerne uniquement les étiquettes (`goto`).
- **Portée de fichier / d'espace de noms** : du point de déclaration à la fin du fichier (ou de l'espace de noms).
- **Portée de classe** : les membres sont accessibles dans la classe, ou par `objet.membre` / `Classe::membre` à l'extérieur.
- **Portée d'énumération** : les valeurs d'une `enum class` sont accessibles via `Enum::valeur`.
- **Portée de template** : un paramètre de template n'est visible que dans sa déclaration.
- **Ombrage** (*shadowing*) : un nom interne masque un nom externe identique. Source de bogues : activez `-Wshadow`.

### 10.2 Durée de vie et classes de stockage

La **durée de vie** d'un objet commence à la fin de son initialisation et se termine quand il est détruit. Le C++ distingue quatre **durées de stockage** :

- **Automatique** : variable locale ordinaire ; créée à la déclaration, **détruite à la sortie du bloc**, sur la **pile**.
- **Statique** : variable globale, variable `static` locale ou membre `static` ; existe **pendant tout le programme**.
- **Dynamique** : objet créé par `new` (ou `make_unique`, ou un conteneur) ; vit jusqu'à `delete` ou jusqu'à la destruction de son propriétaire ; sur le **tas**.
- **Locale au thread** : `thread_local` ; une copie par fil d'exécution.

Les spécificateurs en jeu :

- **`static` (local)** : conserve sa valeur d'un appel à l'autre ; initialisée **une seule fois** (de façon thread-safe depuis C++11).
- **`static` (global)** : liaison **interne** — visible dans le fichier seul ; on préfère aujourd'hui l'espace de noms anonyme.
- **`extern`** : déclare une variable définie ailleurs (partage entre fichiers).
- **`thread_local`** *(C++11)* : durée de vie liée au thread.
- **`inline` (variable)** *(C++17)* : permet de définir une variable globale dans un en-tête sans erreur de liaison.
- **`mutable`** : membre modifiable même dans un objet `const` (cache, mutex).

```cpp
#include <iostream>

int compteur() {
    static int n = 0;               // initialisée une seule fois ; conserve sa valeur
    return ++n;
}

namespace {                         // espace de noms anonyme : visible dans ce fichier seulement
    int secret = 42;
}

inline constexpr int MAX = 100;     // variable inline (C++17)
thread_local int par_thread = 0;    // chaque thread a sa propre copie

int main() {
    std::cout << compteur() << compteur() << compteur() << '\n';    // 123
    std::cout << secret << ' ' << MAX << ' ' << par_thread << '\n';
}
```

**Piège — le fiasco de l'ordre d'initialisation statique** (*static initialization order fiasco*). L'ordre d'initialisation des variables globales de **fichiers différents** n'est pas défini : si l'une dépend d'une autre, le comportement est imprévisible. Évitez les globales interdépendantes ; une variable `static` locale à une fonction (initialisée au premier appel) règle le problème, tout comme `constinit`.

### 10.3 Organisation de la mémoire d'un programme

La mémoire d'un processus se découpe en quatre zones :

- **Le code** (*text*) : instructions machine et constantes littérales, en lecture seule.
- **Les données statiques** : variables globales et `static`, pour toute la durée du programme.
- **Le tas** (*heap*) : objets alloués dynamiquement ; il grandit vers les adresses hautes ; sa gestion est à la charge du programme — directement (`new` / `delete`) ou, mieux, via **RAII**.
- **La pile** (*stack*) : variables locales, paramètres, adresses de retour ; elle grandit vers les adresses basses ; **gestion automatique**, de **taille limitée** (souvent quelques Mo).

Conséquence : évitez les gros tableaux locaux et les récursions très profondes (dépassement de pile), et allouez les gros volumes de données sur le tas, via `std::vector`.

### 10.4 RAII : la durée de vie au service de la fiabilité

En C++, un objet est **construit** à sa déclaration et **détruit automatiquement** à la fin de sa portée, dans l'**ordre inverse** de la construction. Ce mécanisme, nommé **RAII** (*Resource Acquisition Is Initialization*), lie la durée de vie d'une ressource (mémoire, fichier, verrou, connexion) à celle d'un objet.

```cpp
#include <iostream>
#include <string>
#include <utility>

class Trace {
    std::string nom_;
public:
    explicit Trace(std::string nom) : nom_(std::move(nom)) { std::cout << "construit " << nom_ << '\n'; }
    ~Trace() { std::cout << "détruit   " << nom_ << '\n'; }       // destructeur
};

int main() {
    Trace a{"A"};              // construit A
    {
        Trace b{"B"};          // construit B
    }                          // détruit B (fin du bloc)
    Trace c{"C"};              // construit C
    std::cout << "fin de main\n";
}                              // détruit C, puis détruit A (ordre inverse)
```

La destruction a lieu **même si une exception est levée** : c'est le fondement de la gestion fiable des ressources en C++. Les exemples sont partout dans la bibliothèque standard : `std::vector` libère sa mémoire, `std::ifstream` ferme son fichier, `std::lock_guard` libère son verrou, `std::unique_ptr` détruit l'objet pointé.

### 10.5 Bonnes pratiques

- Déclarez les variables dans la **plus petite portée** possible et initialisez-les immédiatement.
- Évitez les variables **globales** ; si indispensables, placez-les dans un `namespace` et rendez-les `const` / `constexpr`.
- Évitez l'ombrage (`-Wshadow`).
- Ne gérez jamais une ressource « à la main » : encapsulez-la dans un objet RAII.
- Ne retournez jamais de référence ou de pointeur vers une variable automatique.

### À retenir (chapitre 10)

- Portée = visibilité du nom ; durée de vie = existence de l'objet. Pile = automatique, tas = dynamique, segment de données = statique.
- RAII : le destructeur libère la ressource à la fin de la portée, exceptions comprises.
- Évitez les globales ; attention à l'ordre d'initialisation statique.

---

# Niveau intermédiaire

---

## Chapitre 11 — Tableaux

### 11.1 Trois sortes de tableaux

Un **tableau** est une suite d'éléments de même type rangés **contigus** en mémoire. Le C++ en propose trois :

- le **tableau « à la C »** `int t[N]` : taille fixe connue à la compilation, sans méthodes, se réduit à un pointeur dès qu'on le passe à une fonction ;
- **`std::array<T, N>`** *(C++11)* : enveloppe du précédent, avec `size()`, `at()`, itérateurs, copie par `=`, comparaison ;
- **`std::vector<T>`** : tableau **dynamique** dont la taille varie à l'exécution ; ses éléments sont sur le tas.

```cpp
#include <array>
#include <iostream>
#include <vector>

int main() {
    int a[5] = {1, 2, 3};              // tableau C : 1 2 3 0 0 (le reste est mis à zéro)
    int b[] = {4, 5, 6};               // taille déduite : 3
    int zeros[10] = {};                // tout à 0

    std::array<int, 5> c{1, 2, 3};     // taille fixe connue à la compilation
    std::vector<int> d{1, 2, 3};       // taille variable

    std::cout << sizeof(a) / sizeof(a[0]) << ' ' << c.size() << ' ' << d.size() << '\n';   // 5 5 3
    (void)b; (void)zeros;
}
```

Points de comparaison : seul `std::vector` change de taille ; seul le tableau C se réduit à un pointeur et ne se copie pas par `=` ; `at()` (accès vérifié) existe pour `std::array` et `std::vector` ; les trois offrent un accès en O(1). **Bonne pratique** : préférez `std::array` (taille fixe) et `std::vector` (taille variable) aux tableaux à la C.

Les indices vont de **0 à taille − 1**. Accéder à `t[taille]` ou à un indice négatif est un **comportement indéfini** (pas d'exception, pas de message : silencieux ou plantage).

### 11.2 Parcourir un tableau

```cpp
#include <array>
#include <iostream>
#include <stdexcept>

int main() {
    std::array<int, 4> t{10, 20, 30, 40};

    for (std::size_t i = 0; i < t.size(); ++i) std::cout << t[i] << ' ';    // par indice
    for (int x : t) std::cout << x << ' ';                                  // sur intervalle
    std::cout << '\n';

    try {
        std::cout << t.at(10) << '\n';                  // at() vérifie les bornes
    } catch (const std::out_of_range &e) {
        std::cerr << "hors bornes : " << e.what() << '\n';
    }
    // t[10] : accès hors bornes NON vérifié, comportement indéfini
}
```

### 11.3 Tableaux multidimensionnels

```cpp
#include <array>
#include <iostream>
#include <vector>

int main() {
    int m[2][3] = {{1, 2, 3}, {4, 5, 6}};                          // tableau C 2 x 3
    for (const auto &ligne : m) {
        for (int v : ligne) std::cout << v << ' ';
        std::cout << '\n';
    }

    std::array<std::array<int, 3>, 2> g{{{1, 2, 3}, {4, 5, 6}}};    // 2 lignes de 3
    std::vector<std::vector<int>> mat(3, std::vector<int>(4, 0));   // matrice dynamique 3 x 4 de zéros
    mat[1][2] = 9;
    std::cout << g[1][2] << ' ' << mat[1][2] << '\n';              // 6 9
}
```

En mémoire, un tableau multidimensionnel C est stocké **ligne par ligne** (*row-major*) : `m[i][j]` est à l'offset `i * colonnes + j`. Un `vector<vector<T>>` fait une allocation par ligne ; pour une matrice dense performante, stockez les données dans **un seul** `std::vector` indexé par `i * colonnes + j`, ou utilisez `std::mdspan` *(C++23)*, qui offre une vue multidimensionnelle sur un tampon contigu.

### 11.4 Tableaux de taille variable

Les **VLA** du C99 (`int t[n];` avec `n` connu seulement à l'exécution) **n'existent pas** en C++ standard (certains compilateurs les acceptent en extension, avec des risques de dépassement de pile). On utilise `std::vector` :

```cpp
std::vector<int> t(n);        // n éléments initialisés à 0
std::vector<int> u(n, 7);     // n éléments égaux à 7
for (int i = 0; i < n; ++i) t[i] = i * i;
// mémoire libérée automatiquement à la fin de la portée
```

### 11.5 Tableaux et fonctions

Un tableau C passé à une fonction **se réduit à un pointeur** (*array-to-pointer decay*) : sa taille est perdue. `void f(int t[])` et `void f(int *t)` sont **strictement identiques**, et `sizeof(t)` y donne la taille d'un pointeur. La solution moderne est `std::span` *(C++20)* : une **vue** (pointeur + taille) sur une suite contiguë, qui accepte tableau C, `std::array` et `std::vector`.

```cpp
#include <array>
#include <iostream>
#include <span>
#include <vector>

int somme(std::span<const int> v) {                   // vue sur une suite contiguë d'int
    int s = 0;
    for (int x : v) s += x;
    return s;
}

template <std::size_t N>
std::size_t taille(const int (&)[N]) { return N; }    // référence vers tableau : N est déduit

int main() {
    int a[4] = {1, 2, 3, 4};
    std::vector<int> v{5, 6};
    std::array<int, 3> arr{7, 8, 9};
    std::cout << somme(a) << ' ' << somme(v) << ' ' << somme(arr) << '\n';   // 10 11 24
    std::cout << taille(a) << '\n';                                          // 4
}
```

### 11.6 Algorithmes sur les tableaux

La bibliothèque `<algorithm>` (et `<numeric>`) fournit des algorithmes génériques, qui travaillent sur des **intervalles d'itérateurs** `[début, fin)` ; la version `std::ranges::` *(C++20)* prend directement le conteneur.

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <numeric>
#include <vector>

int main() {
    std::vector<int> v{5, 2, 9, 1, 7};

    std::sort(v.begin(), v.end());                    // 1 2 5 7 9
    std::ranges::sort(v, std::greater{});             // 9 7 5 2 1 (version ranges)

    auto it = std::find(v.begin(), v.end(), 5);       // recherche linéaire
    if (it != v.end()) std::cout << "5 à l'indice " << it - v.begin() << '\n';

    int total = std::accumulate(v.begin(), v.end(), 0);                           // 24
    auto [mn, mx] = std::minmax_element(v.begin(), v.end());
    auto impairs = std::count_if(v.begin(), v.end(), [](int x) { return x % 2 != 0; });   // 5
    std::cout << total << ' ' << *mn << ' ' << *mx << ' ' << impairs << '\n';
}
```

Principaux outils : tri (`sort`, `stable_sort`), recherche (`find`, `find_if`, et `binary_search` / `lower_bound` sur un intervalle **trié**), comptage et tests (`count`, `count_if`, `any_of`, `all_of`, `none_of`), copie et remplissage (`copy`, `fill`, `iota`, `generate`), réduction (`accumulate`, `reduce`, `transform_reduce`), extrema (`min_element`, `max_element`, `minmax_element`), suppression (`v.erase(std::remove(...), v.end())` ou, plus simplement, `std::erase(v, x)` / `std::erase_if(v, pred)` *(C++20)*).

### 11.7 Erreurs courantes

- `t[n]` avec `n == taille` : accès hors bornes (comportement indéfini) ; testez avec `at()` en développement.
- Calculer la taille avec `sizeof` sur un paramètre de fonction : donne la taille d'un pointeur.
- Modifier un `vector` (ajout, suppression) pendant un `for` sur intervalle : itérateurs invalidés.
- `v[0]` ou `v.front()` sur un vecteur vide.
- `std::vector<bool>` utilisé comme un vrai conteneur de `bool` : c'est une spécialisation à base de bits dont les éléments sont des *proxies* (pas de `bool &`). Préférez `std::vector<char>` ou `std::bitset`.
- Boucle `for (std::size_t i = n - 1; i >= 0; --i)` : infinie (non signé).

### À retenir (chapitre 11)

- `std::array` (taille fixe) et `std::vector` (taille variable) remplacent les tableaux C.
- Un tableau C passé à une fonction perd sa taille ; utilisez `std::span`.
- Indices valides : 0 à taille−1 ; `at()` vérifie, `[]` ne vérifie pas.
- Utilisez les algorithmes standard plutôt que des boucles écrites à la main.

---

## Chapitre 12 — Chaînes de caractères

### 12.1 `std::string` contre chaîne C

En C++, on utilise la classe **`std::string`** (en-tête `<string>`) : elle gère sa mémoire, connaît sa taille, grandit toute seule et se comporte comme une valeur ordinaire (copie, comparaison, concaténation avec les opérateurs). La chaîne « à la C » — tableau de `char` terminé par `'\0'` — reste utile pour l'interopérabilité avec les API C.

```cpp
#include <iostream>
#include <string>

int main() {
    const char *c1 = "bonjour";          // chaîne C : pointeur vers un littéral (lecture seule)
    char c2[] = "bonjour";               // tableau de 8 char (avec '\0'), modifiable
    std::string s = "bonjour";           // chaîne C++ : taille dynamique

    s += " le monde";
    c2[0] = 'B';
    std::cout << c1 << ' ' << c2 << ' ' << s << ' ' << s.size() << '\n';
}
```

Contre `char *`, `std::string` offre : la taille en temps constant (`size()`, au lieu de `strlen`), une mémoire gérée automatiquement, une concaténation sûre (`+`, `+=`, `append`, au lieu de `strcat` qui peut déborder), des comparaisons directes (`==`, `<`, au lieu de `strcmp`), et la copie par `=` (au lieu de `strcpy`).

### 12.2 Les opérations de base

```cpp
#include <iostream>
#include <string>

int main() {
    std::string s = "Bonjour le monde";

    std::cout << s.size() << ' ' << s.empty() << '\n';          // 16 0
    std::cout << s[0] << s.front() << s.back() << '\n';         // BBe
    std::cout << s.substr(0, 7) << '\n';                        // Bonjour
    std::cout << s.find("le") << '\n';                          // 8
    std::cout << (s.find("xyz") == std::string::npos) << '\n';  // 1 : introuvable

    s.insert(7, ",");              // Bonjour, le monde
    s.replace(9, 2, "LE");         // Bonjour, LE monde
    s.erase(7, 1);                 // Bonjour LE monde
    std::cout << s << '\n';

    std::cout << s.starts_with("Bon") << s.ends_with("de") << '\n';        // 11 (C++20)
    std::cout << (std::string("a") < std::string("b")) << '\n';            // 1 : ordre lexicographique
}
```

- **Taille et vidage** : `size()` / `length()`, `empty()`, `clear()`.
- **Accès** : `operator[]` (non vérifié), `at(i)` (vérifié), `front()`, `back()`.
- **Ajout** : `+`, `+=`, `append`, `push_back`, `insert`. **Suppression et remplacement** : `erase`, `pop_back`, `replace`.
- **Sous-chaîne** : `substr(pos, n)` (crée une **copie**).
- **Recherche** : `find`, `rfind`, `find_first_of`, `find_last_of` ; retournent `std::string::npos` si absent — **toujours** comparer à `npos` avant d'utiliser la position.
- **Comparaison** : `==`, `<`, `compare` (ordre lexicographique selon les codes des caractères).
- **Tests** : `starts_with`, `ends_with` *(C++20)*, `contains` *(C++23)*.
- **Interopérabilité** : `c_str()` et `data()` donnent un pointeur vers les caractères terminés par `'\0'` ; il n'est valable que tant que la chaîne n'est ni modifiée ni détruite.
- **Capacité** : `reserve`, `capacity`, `shrink_to_fit`.

### 12.3 Concaténer et copier

```cpp
#include <format>
#include <iostream>
#include <string>
#include <string_view>

using namespace std::literals;

int main() {
    std::string prenom = "Ada", nom = "Lovelace";
    std::string complet = prenom + " " + nom;         // + : chaîne + littéral
    // std::string erreur = "a" + "b";                // ERREUR : deux const char *
    std::string ok = "a"s + "b";                      // "a"s est un std::string

    complet.append("!");
    std::string copie = complet;                      // copie profonde

    std::string_view vue = complet;                   // vue SANS copie (pointeur + taille)
    std::cout << vue.substr(0, 3) << '\n';            // Ada
    std::cout << std::format("{} ({} car.)", complet, complet.size()) << '\n';
    std::cout << ok << copie << '\n';
}
```

**Piège** : deux littéraux ne s'additionnent pas (`"a" + "b"` additionne deux pointeurs). Commencez par un `std::string` ou le suffixe `s`.

**`std::string_view`** *(C++17)* est une **vue** non propriétaire : pointeur + taille vers des caractères qui appartiennent à quelqu'un d'autre. Idéal comme **paramètre** de fonction acceptant un littéral, une `std::string` ou une sous-chaîne sans copie. **Danger** : il devient invalide si la chaîne d'origine est détruite ou modifiée ; ne le stockez pas à long terme.

### 12.4 Parcourir et découper

```cpp
#include <iostream>
#include <ranges>
#include <sstream>
#include <string>

int main() {
    std::string phrase = "un deux trois";

    for (char c : phrase) std::cout << '[' << c << ']';
    std::cout << '\n';

    int espaces = 0;
    for (std::size_t pos = phrase.find(' '); pos != std::string::npos; pos = phrase.find(' ', pos + 1)) ++espaces;
    std::cout << espaces << " espaces\n";                       // 2

    std::istringstream flux(phrase);                            // découper en mots avec un flux
    std::string mot;
    while (flux >> mot) std::cout << '<' << mot << '>';
    std::cout << '\n';

    for (auto morceau : phrase | std::views::split(' ')) {      // découpage avec les ranges (C++20)
        std::cout << std::string(morceau.begin(), morceau.end()) << '|';
    }
    std::cout << '\n';
}
```

La lecture d'une ligne au clavier ou dans un fichier avec `std::getline` est présentée aux chapitres 7 et 22.

### 12.5 Caractères : `<cctype>`

Les fonctions de `<cctype>` testent ou convertissent un caractère : `std::isalpha`, `isdigit`, `isalnum`, `isspace`, `isupper`, `islower`, `ispunct`, `toupper`, `tolower`.

```cpp
#include <algorithm>
#include <cctype>
#include <iostream>
#include <string>

int main() {
    std::string s = "Bonjour 2026";
    std::transform(s.begin(), s.end(), s.begin(),
                   [](unsigned char c) { return static_cast<char>(std::toupper(c)); });   // BONJOUR 2026
    auto chiffres = std::count_if(s.begin(), s.end(), [](unsigned char c) { return std::isdigit(c); });
    std::cout << s << ' ' << chiffres << '\n';        // BONJOUR 2026 4
}
```

**Piège** : passez-leur un **`unsigned char`** : une valeur négative (caractère accentué sur un `char` signé) provoque un comportement indéfini. Elles ne gèrent que l'**ASCII** ; pour Unicode, voir le chapitre 27.

### 12.6 Conversions chaîne ↔ nombre

```cpp
#include <charconv>
#include <iostream>
#include <string>

int main() {
    int n = std::stoi("42");                 // chaîne -> int
    double d = std::stod("3.14");            // chaîne -> double
    std::string s = std::to_string(3.5);     // "3.500000"

    try {
        std::stoi("abc");                    // lève std::invalid_argument
    } catch (const std::invalid_argument &) {
        std::cout << "pas un nombre\n";
    } catch (const std::out_of_range &) {
        std::cout << "valeur trop grande\n";
    }

    char buf[32];
    auto [fin, ec] = std::to_chars(buf, buf + sizeof buf, 255, 16);   // sans allocation ni exception
    *fin = '\0';
    std::cout << n << ' ' << d << ' ' << s << ' ' << buf << '\n';     // 42 3.14 3.500000 ff
}
```

- `std::stoi`, `stol`, `stoll`, `stoul`, `stof`, `stod` : chaîne → nombre, **avec exceptions** en cas d'erreur.
- `std::to_string(x)` : nombre → chaîne, format fixe, peu configurable.
- `std::from_chars` / `std::to_chars` *(C++17)* : conversions **rapides**, sans exception ni allocation, indépendantes de la locale.
- `std::format("{}", x)` *(C++20)* : nombre → chaîne avec options de format.

### 12.7 Tableaux de chaînes et fonctions C

```cpp
std::vector<std::string> noms{"Zoé", "Ana", "Marc"};
noms.push_back("Luc");
std::sort(noms.begin(), noms.end());     // tri lexicographique : Ana Luc Marc Zoé
```

Les fonctions C de `<cstring>` (`strlen`, `strcpy`, `strcat`, `strcmp`, `strchr`, `strstr`, `memcpy`, `memset`) fonctionnent encore, mais chacune a un équivalent plus sûr : `size()`, `=`, `+=`, `==` ou `compare`, `find`, `std::copy`, `std::fill` (les deux derniers pour les types triviaux seulement). Pour appeler une fonction C qui attend un `const char *`, passez `s.c_str()`.

### 12.8 Bonnes pratiques

- Utilisez `std::string` partout ; `std::string_view` pour les paramètres en lecture seule.
- Ne mélangez jamais `+` entre deux littéraux ; démarrez avec un `std::string` ou le suffixe `s`.
- Vérifiez `find(...) != std::string::npos` avant d'utiliser la position.
- Validez toute conversion de saisie utilisateur (`try`/`catch` ou `from_chars`).

### À retenir (chapitre 12)

- `std::string` possède ses caractères ; `std::string_view` les observe seulement.
- `size()` compte des **octets**, pas des caractères visibles (voir le chapitre 27).
- `find` retourne `npos` en cas d'échec ; `c_str()` est éphémère.

---

## Chapitre 13 — Pointeurs

### 13.1 Qu'est-ce qu'un pointeur ?

Chaque objet occupe un emplacement en mémoire, repéré par une **adresse**. Un **pointeur** est une variable dont la valeur est l'adresse d'un autre objet. Son type indique **ce qui est pointé** : `int *` est « pointeur vers un `int` ».

```cpp
#include <iostream>

int main() {
    int x = 42;
    int *p = &x;                       // p contient l'adresse de x

    std::cout << x << ' ' << *p << ' ' << (p == &x) << '\n';     // 42 42 1
    std::cout << static_cast<const void *>(p) << '\n';           // affiche l'adresse (ex. 0x7ffd...)

    *p = 100;                          // modifie x via le pointeur
    std::cout << x << '\n';            // 100
}
```

Trois opérateurs sont à connaître : **`&x`** (opérateur d'adresse : donne l'adresse de `x`), **`*p`** (opérateur de **déréférencement** : désigne l'objet pointé) et **`p->m`** (accès au membre `m` de l'objet pointé, équivalent à `(*p).m`). Le symbole `*` a deux sens selon le contexte : dans une **déclaration** il construit un type pointeur (`int *p`), dans une **expression** il déréférence.

### 13.2 Le pointeur nul : `nullptr`

Un pointeur qui ne désigne aucun objet vaut `nullptr` *(C++11)*. Déréférencer un pointeur nul est un comportement indéfini (en pratique, un plantage). `nullptr` a son propre type (`std::nullptr_t`) et remplace `NULL` et `0`, qui sont des entiers et provoquent des ambiguïtés de surcharge.

```cpp
#include <iostream>

void f(int) { std::cout << "f(int)\n"; }
void f(const char *) { std::cout << "f(const char *)\n"; }

int main() {
    int *p = nullptr;                   // ne pointe vers rien
    if (p == nullptr) std::cout << "nul\n";
    if (!p) std::cout << "nul aussi\n";
    f(nullptr);                         // appelle f(const char *) : sans ambiguïté
    // f(NULL);                         // ambigu ou f(int) : NULL est un entier hérité du C
}
```

**Règle** : initialisez tout pointeur (`= nullptr` à défaut d'une adresse) et testez-le avant de le déréférencer s'il peut être nul.

### 13.3 Arithmétique des pointeurs

On peut additionner un entier à un pointeur, ou soustraire deux pointeurs. **`p + n` avance de `n` éléments** (donc de `n * sizeof(*p)` octets), pas de `n` octets.

```cpp
#include <cstddef>
#include <iostream>

int main() {
    int t[] = {10, 20, 30, 40};
    int *p = t;                                    // t se réduit à &t[0]

    std::cout << *p << ' ' << *(p + 1) << ' ' << p[2] << '\n';     // 10 20 30
    p += 3;
    std::cout << *p << '\n';                                       // 40
    std::ptrdiff_t d = &t[3] - &t[0];                              // 3 éléments d'écart
    std::cout << d << '\n';
}
```

L'arithmétique n'est valide qu'**à l'intérieur d'un même tableau**, ou un cran après le dernier élément (sans déréférencement). Hors de ces bornes, le résultat est un comportement indéfini, même sans déréférencer. Comparer deux pointeurs d'objets distincts avec `<` est non spécifié (utilisez `std::less`).

### 13.4 Tableaux et pointeurs

Un tableau **n'est pas** un pointeur, mais il **se convertit implicitement** en pointeur vers son premier élément (*decay*). `t[i]` est défini comme `*(t + i)`.

```cpp
int t[5] = {1, 2, 3, 4, 5};
int *p = t;
std::cout << sizeof(t) << ' ' << sizeof(p) << '\n';     // 20 8 : un tableau n'est PAS un pointeur
std::cout << (t[2] == *(t + 2)) << '\n';                // 1
```

Différences : `sizeof` d'un tableau donne sa taille totale, celui d'un pointeur la taille du pointeur ; un tableau ne peut pas être réaffecté, un pointeur si.

### 13.5 Pointeurs et fonctions

Passer un pointeur permet à une fonction de modifier l'objet de l'appelant (style C). En C++, on préfère les **références** quand l'argument est obligatoire, et on réserve le pointeur aux arguments **optionnels** (`nullptr` possible).

```cpp
void echange(int *a, int *b) { int t = *a; *a = *b; *b = t; }       // style C
void echange_ref(int &a, int &b) { int t = a; a = b; b = t; }        // style C++
```

### 13.6 `const` et pointeurs (rappel)

`const T *p` : l'objet pointé est constant ; `T *const p` : le pointeur est constant ; `const T *const p` : les deux. Lisez de droite à gauche (chapitre 5).

### 13.7 `void *` et ses alternatives

Un `void *` est un pointeur sans type : il peut contenir l'adresse de n'importe quel objet, mais on ne peut ni le déréférencer, ni lui appliquer l'arithmétique. Contrairement au C, la conversion de `void *` vers `T *` exige un **cast explicite** (`static_cast`).

```cpp
int x = 7;
void *v = &x;                        // conversion implicite vers void * : permise
int *q = static_cast<int *>(v);      // retour : cast obligatoire
```

En C++ moderne, `void *` est presque toujours remplacé par un outil typé : **templates** (fonction générique), `std::variant` (« l'un parmi N »), `std::any` (valeur de type quelconque), **classe de base polymorphe** (objets de types liés), `std::bit_cast` / `std::memcpy` (réinterpréter des octets).

### 13.8 Pointeur vers un objet, `this`

```cpp
struct Point { int x, y; };

Point p{1, 2};
Point *pp = &p;
pp->x = 5;            // équivaut à (*pp).x = 5
(*pp).y = 6;
```

Dans une fonction membre, **`this`** est un pointeur vers l'objet courant (chapitre 18).

### 13.9 Aliasing strict

Le compilateur suppose que des pointeurs de **types différents** (sauf `char`, `unsigned char`, `std::byte`) ne désignent pas le même objet : c'est la règle d'**alias strict**. La violer (lire un `float` via un `int *`) est un comportement indéfini. Pour réinterpréter des bits, utilisez `std::bit_cast` (C++20) ou `std::memcpy`. Le mot-clé `restrict` du C n'existe pas en C++ standard (extension `__restrict`).

### 13.10 Erreurs classiques

- **Pointeur non initialisé** : contient une adresse aléatoire (comportement indéfini). Parade : `= nullptr`.
- **Déréférencer `nullptr`** : plantage. Testez avant.
- **Pointeur pendant** (*dangling pointer*) : l'objet pointé a été détruit (variable locale sortie de portée, mémoire libérée, élément d'un vecteur réalloué). Parade : propriété claire, pointeurs intelligents, ne pas conserver d'adresse d'un objet détruit.
- **Sortie de tableau** : accès au-delà des bornes. Parade : `std::span`, `at()`.
- **`delete` d'un pointeur non alloué par `new`**, ou double `delete`. Parade : pointeurs intelligents.
- **Retourner l'adresse d'une variable locale.**

**À retenir pour la suite** : le C++ moderne réduit fortement l'usage des pointeurs bruts. Un pointeur brut devient un simple **observateur non propriétaire** ; les références, les conteneurs, `std::span`, `std::optional` et les **pointeurs intelligents** (chapitre 14) couvrent presque tous les besoins.

### À retenir (chapitre 13)

- Pointeur = adresse typée ; `&` donne l'adresse, `*` déréférence, `->` accède à un membre.
- Utilisez `nullptr`, jamais `NULL` ni `0`.
- Arithmétique en nombre d'éléments, uniquement dans un même tableau.
- Un tableau n'est pas un pointeur, mais se convertit en pointeur.

---

## Chapitre 14 — Allocation dynamique de mémoire

### 14.1 Pourquoi allouer dynamiquement ?

La pile est de taille limitée, et ses variables disparaissent à la fin du bloc. L'**allocation dynamique** (sur le **tas**) sert quand : la taille n'est connue qu'à l'exécution, la durée de vie dépasse celle de la fonction, ou les objets sont volumineux. Mais en C++ moderne, c'est le travail des **conteneurs** (`std::vector`, `std::string`) et des **pointeurs intelligents** ; on n'écrit presque jamais `new` et `delete` soi-même. Il faut néanmoins les comprendre.

### 14.2 `new` et `delete`

```cpp
#include <iostream>

int main() {
    int *p = new int(42);              // alloue UN int initialisé à 42
    std::cout << *p << '\n';
    delete p;                          // libère
    p = nullptr;

    int n = 5;
    int *t = new int[n];               // alloue un tableau de 5 int (valeurs indéterminées)
    for (int i = 0; i < n; ++i) t[i] = i * i;
    std::cout << t[4] << '\n';         // 16
    delete[] t;                        // delete[] OBLIGATOIRE pour un new[]
    t = nullptr;
}
```

- **`new T`** alloue la mémoire **puis appelle le constructeur** de `T` ; **`delete p`** appelle le **destructeur** puis libère. (`malloc` et `free` du C ne le font pas : ne les utilisez pas pour des objets.)
- **`new T[n]`** alloue un tableau ; il se libère **obligatoirement** avec **`delete[]`**.
- **Ne mélangez jamais** les familles : `new` ↔ `delete`, `new[]` ↔ `delete[]`, `malloc` ↔ `free`. Mélanger est un comportement indéfini.

### 14.3 Initialisation et échec d'allocation

```cpp
#include <iostream>
#include <new>

int main() {
    int *a = new int;               // valeur indéterminée
    int *b = new int();             // 0 (initialisation par valeur)
    int *c = new int{7};            // 7
    int *d = new int[4]();          // 4 zéros
    int *e = new int[4]{1, 2};      // 1 2 0 0
    delete a; delete b; delete c; delete[] d; delete[] e;

    try {
        double *gros = new double[1ULL << 60];          // demande démesurée
        delete[] gros;
    } catch (const std::bad_alloc &) {                  // par défaut, new LÈVE une exception en cas d'échec
        std::cerr << "allocation impossible\n";
    }

    int *q = new (std::nothrow) int[100];               // variante sans exception : retourne nullptr
    if (!q) std::cerr << "échec\n";
    delete[] q;
}
```

Contrairement à `malloc`, `new` ne retourne jamais `nullptr` : il **lève `std::bad_alloc`**. La variante `new (std::nothrow)` retourne `nullptr` à la place.

### 14.4 Le tableau dynamique moderne : `std::vector`

`std::vector` remplace `malloc` + `realloc` : il gère la mémoire, l'agrandissement et la libération.

```cpp
std::vector<int> v;
v.reserve(100);                         // réserve la capacité (évite les réallocations)
for (int i = 0; i < 10; ++i) v.push_back(i);
v.resize(20);                           // agrandit ; les nouveaux éléments valent 0
v.shrink_to_fit();                      // demande de réduire la capacité à la taille
// libération automatique à la fin de la portée
```

### 14.5 Pointeurs intelligents `<memory>` *(C++11)*

Un **pointeur intelligent** est un objet RAII qui **possède** une ressource et la libère automatiquement. Trois types sont à connaître :

- **`std::unique_ptr<T>`** : propriétaire **unique** ; non copiable mais **déplaçable** ; aucun surcoût par rapport à un pointeur brut. **Choix par défaut.**
- **`std::shared_ptr<T>`** : propriété **partagée** par comptage de références (atomique) ; l'objet est détruit quand le dernier propriétaire disparaît. À justifier : le surcoût est réel.
- **`std::weak_ptr<T>`** : observateur **sans propriété** d'un objet géré par `shared_ptr` ; sert à casser les **cycles** de références et à écrire des caches.
- `std::auto_ptr` a été **supprimé** (C++17).

```cpp
#include <cstdio>
#include <iostream>
#include <memory>
#include <string>
#include <utility>

struct Joueur {
    std::string nom;
    explicit Joueur(std::string n) : nom(std::move(n)) { std::cout << "créé " << nom << '\n'; }
    ~Joueur() { std::cout << "détruit " << nom << '\n'; }
};

int main() {
    auto u = std::make_unique<Joueur>("Ana");         // propriétaire unique
    auto u2 = std::move(u);                           // transfert de propriété : u devient nul
    std::cout << (u == nullptr) << '\n';              // 1

    auto s1 = std::make_shared<Joueur>("Luc");        // propriété partagée
    {
        auto s2 = s1;
        std::cout << s1.use_count() << '\n';          // 2
    }
    std::cout << s1.use_count() << '\n';              // 1

    std::weak_ptr<Joueur> w = s1;                     // observateur, sans propriété
    if (auto verrou = w.lock()) std::cout << verrou->nom << '\n';

    auto tab = std::make_unique<int[]>(5);            // tableau dynamique (5 zéros)
    tab[2] = 7;

    std::unique_ptr<std::FILE, decltype(&std::fclose)> f(std::fopen("a.txt", "r"), &std::fclose);   // suppresseur personnalisé
}                                                     // tout est libéré automatiquement
```

Créez-les avec **`std::make_unique`** et **`std::make_shared`** (plus sûr en cas d'exception, et plus efficace pour `shared_ptr`). Un `unique_ptr` passé **en paramètre par valeur** signale un **transfert de propriété**.

### 14.6 Erreurs classiques et remèdes

- **Fuite mémoire** (oubli de `delete`) → `unique_ptr`, conteneurs.
- **Double libération** (`delete` deux fois) : corruption du tas → pointeurs intelligents.
- **Utilisation après libération** (*use-after-free*) : comportement indéfini, faille de sécurité fréquente → mettre à `nullptr`, propriété claire.
- **`new[]` libéré par `delete`** (ou l'inverse) → `delete[]`, ou mieux `std::vector`.
- **Fuite en cas d'exception** : si une fonction lève entre `new` et `delete`, le `delete` est sauté → RAII.
- **Deux `shared_ptr` construits depuis le même pointeur brut** : double libération → `make_shared` ou copie du `shared_ptr`.
- **Cycle de `shared_ptr`** (A possède B qui possède A) : fuite → `weak_ptr`.

```cpp
void fuite() {
    int *p = new int[100];
    risque();                 // si risque() lève : le delete[] est sauté
    delete[] p;
}

void sur() {
    auto p = std::make_unique<int[]>(100);
    risque();                 // exception : p est quand même libéré
}
```

### 14.7 Outils de détection

```bash
g++ -g -fsanitize=address,undefined -std=c++20 prog.cpp -o prog   # AddressSanitizer + UBSan
./prog
valgrind --leak-check=full ./prog                                 # fuites et accès invalides
```

### 14.8 Règles de propriété

- Un pointeur brut ou une référence **ne possède pas** : il observe.
- Une ressource a **un seul propriétaire** : un objet, un conteneur ou un `unique_ptr`.
- La propriété **partagée** est l'exception, à justifier.
- Documentez qui possède quoi dans les interfaces : `std::unique_ptr<T>` en paramètre = transfert de propriété ; `T *` ou `T &` = simple usage.

### À retenir (chapitre 14)

- `new` / `delete` appellent constructeurs / destructeurs ; `new[]` ↔ `delete[]` ; on ne les écrit presque plus.
- `std::vector` pour les tableaux dynamiques, `std::unique_ptr` pour les objets alloués, `std::shared_ptr` si le partage est nécessaire.
- Utilisez ASan / UBSan / Valgrind pour traquer fuites et accès invalides.

---

## Chapitre 15 — Retourner des tableaux et des chaînes

### 15.1 Le problème

Une variable locale est détruite à la sortie de la fonction ; on ne peut donc pas en retourner l'adresse :

```cpp
// int *mauvais() {
//     int t[3] = {1, 2, 3};
//     return t;             // t est détruit à la sortie : le pointeur est invalide
// }
```

Le C contournait le problème avec `malloc` ou des tampons `static`. Le C++ moderne dispose de solutions beaucoup plus simples et sûres.

### 15.2 Les solutions

```cpp
#include <algorithm>
#include <cctype>
#include <iostream>
#include <optional>
#include <span>
#include <string>
#include <utility>
#include <vector>

// 1. Retour par VALEUR (solution recommandée)
std::vector<int> carres(int n) {
    std::vector<int> v;
    v.reserve(n);
    for (int i = 0; i < n; ++i) v.push_back(i * i);
    return v;                                    // pas de copie profonde : élision ou déplacement
}

std::string majuscules(std::string s) {
    for (char &c : s) c = static_cast<char>(std::toupper(static_cast<unsigned char>(c)));
    return s;
}

// 2. L'appelant fournit la mémoire
void remplir_carres(std::span<int> sortie) {
    for (std::size_t i = 0; i < sortie.size(); ++i) sortie[i] = static_cast<int>(i * i);
}

// 3. Plusieurs valeurs : struct, pair, tuple
struct Stats { double min, max, moyenne; };
Stats calculer(const std::vector<double> &v) {
    auto [mn, mx] = std::minmax_element(v.begin(), v.end());
    double somme = 0;
    for (double x : v) somme += x;
    return {*mn, *mx, somme / v.size()};
}
std::pair<int, int> divmod(int a, int b) { return {a / b, a % b}; }

// 4. Résultat qui peut être absent
std::optional<int> premier_pair(const std::vector<int> &v) {
    for (int x : v) if (x % 2 == 0) return x;
    return std::nullopt;
}

int main() {
    auto v = carres(5);                                  // 0 1 4 9 16
    std::cout << majuscules("bonjour") << '\n';          // BONJOUR
    int tampon[4];
    remplir_carres(tampon);                              // un tableau C se convertit en span
    auto [q, r] = divmod(17, 5);                         // liaisons structurées : 3 et 2
    auto st = calculer({2.0, 4.0, 9.0});
    std::cout << q << ' ' << r << ' ' << st.moyenne << '\n';
    if (auto p = premier_pair({1, 3, 8, 5})) std::cout << *p << '\n';   // 8
    std::cout << v.size() << ' ' << tampon[3] << '\n';
}
```

Guide de choix :

- **Retour par valeur** (`vector`, `string`, `struct`) : **par défaut** ; simple, sûr, performant.
- **Paramètre de sortie** (`std::span`, `T &`) : pour réutiliser un tampon existant et éviter des allocations répétées.
- **`std::pair`, `std::tuple`, `struct`** : plusieurs valeurs de retour (le `struct` nommé est le plus lisible).
- **`std::optional<T>`** : résultat éventuellement absent.
- **`std::expected<T, E>`** *(C++23)* : résultat **ou** erreur typée, sans exception.
- **`std::unique_ptr<T>`** : transférer la propriété d'un objet alloué (polymorphisme, grosse ressource).
- **Variable `static` locale** : à éviter (partagée entre appels, non réentrante, non thread-safe en pratique).

### 15.3 Ce qu'il ne faut jamais faire

```cpp
std::string fabrique() { return "temporaire"; }

void pieges() {
    std::string_view sv = fabrique();            // DANGER : le temporaire est détruit, sv est pendant
    const char *c = fabrique().c_str();          // DANGER : idem pour c
    const std::string &ok = fabrique();          // OK : la durée de vie du temporaire est prolongée
}

// const std::string &retourne_local() { std::string s = "x"; return s; }   // DANGER : référence vers un local
```

Une **référence constante** liée directement à un temporaire en **prolonge** la durée de vie ; un `string_view` ou un `c_str()` obtenu depuis un temporaire, non. Ne retournez jamais de référence, de pointeur ou de vue vers un objet local ou temporaire.

### 15.4 Sémantique de déplacement *(C++11)*

Pourquoi le retour par valeur est-il efficace ? Grâce à l'**élision de copie** et à la **sémantique de déplacement**.

Une **lvalue** a un nom et une adresse (une variable). Une **rvalue** est un temporaire sur le point de disparaître. Une **référence rvalue** `T &&` ne peut se lier qu'à une rvalue : elle permet de **voler** les ressources d'un temporaire au lieu de les copier.

```cpp
#include <iostream>
#include <string>
#include <utility>
#include <vector>

int main() {
    std::string a = "contenu très long qui nécessite une allocation sur le tas";
    std::string b = a;                         // COPIE : a reste intact
    std::string c = std::move(a);              // DÉPLACEMENT : c vole le tampon de a
    std::cout << a.size() << ' ' << c.size() << '\n';     // a est valide mais indéterminé (souvent vide)

    std::vector<std::string> v;
    v.push_back(std::move(c));                 // déplace au lieu de copier
    v.emplace_back("construit sur place");     // construit directement dans le vecteur
    std::cout << v.size() << ' ' << b.size() << '\n';
}
```

- **`std::move(x)` ne déplace rien** : il convertit `x` en rvalue, ce qui *autorise* le déplacement.
- Après un déplacement, l'objet source reste **valide** mais son contenu est **indéterminé** : on peut seulement le détruire ou lui réaffecter une valeur.
- **N'écrivez pas** `return std::move(local);` : cela empêche l'élision de copie ; `return local;` suffit.
- La conception d'un constructeur de déplacement est étudiée au chapitre 18.

### À retenir (chapitre 15)

- Retournez par valeur : le compilateur s'occupe de l'efficacité (élision, NRVO, déplacement).
- `std::optional`, `std::expected`, `struct` plutôt que valeurs magiques ou paramètres de sortie.
- Jamais de référence, pointeur ou vue vers un local ou un temporaire.

---

## Chapitre 16 — Structures de données dynamiques

### 16.1 Liste simplement chaînée

Écrire sa propre liste permet de bien comprendre la propriété des objets. Avec des `std::unique_ptr`, **chaque nœud possède le suivant** : aucune fuite possible.

```cpp
#include <iostream>
#include <memory>
#include <utility>

struct Noeud {
    int valeur;
    std::unique_ptr<Noeud> suivant;
    explicit Noeud(int v) : valeur(v) {}
};

class Liste {
    std::unique_ptr<Noeud> tete_;
public:
    void ajouter_debut(int v) {
        auto n = std::make_unique<Noeud>(v);
        n->suivant = std::move(tete_);
        tete_ = std::move(n);
    }

    bool supprimer(int v) {
        std::unique_ptr<Noeud> *pp = &tete_;                  // pointeur vers le « lien » à examiner
        while (*pp && (*pp)->valeur != v) pp = &(*pp)->suivant;
        if (!*pp) return false;                               // introuvable
        *pp = std::move((*pp)->suivant);                      // le lien saute le nœud supprimé
        return true;
    }

    void afficher() const {
        for (const Noeud *p = tete_.get(); p; p = p->suivant.get()) std::cout << p->valeur << " -> ";
        std::cout << "fin\n";
    }

    ~Liste() { while (tete_) tete_ = std::move(tete_->suivant); }   // libération itérative (évite une récursion profonde)
};

int main() {
    Liste l;
    for (int v : {3, 2, 1}) l.ajouter_debut(v);
    l.afficher();               // 1 -> 2 -> 3 -> fin
    l.supprimer(2);
    l.afficher();               // 1 -> 3 -> fin
}
```

Points d'attention : le destructeur libère les nœuds **en boucle** (un destructeur récursif sur une très longue liste provoquerait un dépassement de pile) ; la technique du « pointeur vers le lien » (`pp`) évite un cas particulier pour la tête de liste.

En pratique, on utilise les listes standard : `std::list` (doublement chaînée) et `std::forward_list` (simplement chaînée, plus économe).

### 16.2 Les conteneurs de la bibliothèque standard

- **`std::array<T, N>`** : tableau de taille fixe ; accès O(1).
- **`std::vector<T>`** : tableau dynamique contigu ; accès O(1), ajout en fin O(1) amorti, insertion au milieu O(n).
- **`std::deque<T>`** : file à double extrémité ; ajout/retrait aux deux bouts O(1).
- **`std::list<T>`** / **`std::forward_list<T>`** : listes chaînées ; insertion/suppression O(1) à une position connue ; pas d'accès direct.
- **`std::set<T>`** / **`std::multiset<T>`** : ensemble **trié** (arbre équilibré) ; O(log n).
- **`std::map<K, V>`** / **`std::multimap<K, V>`** : dictionnaire **trié** par clé ; O(log n).
- **`std::unordered_set<T>`** / **`std::unordered_map<K, V>`** : tables de hachage ; O(1) en moyenne, ordre quelconque.
- **Adaptateurs** : `std::stack` (pile LIFO), `std::queue` (file FIFO), `std::priority_queue` (file de priorité).
- **`std::flat_map`**, **`std::flat_set`** *(C++23)* : associatifs sur tableaux triés — parcours rapide, insertion plus lente.
- **`std::inplace_vector<T, N>`** *(C++26)* : vecteur de capacité fixe sans allocation dynamique, pour l'embarqué et le temps réel.

### 16.3 Le tableau dynamique extensible : `std::vector`

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v;
    for (int i = 0; i < 10; ++i) {
        v.push_back(i);                                         // ajout en fin
        std::cout << v.size() << '/' << v.capacity() << ' ';    // la capacité croît par paliers
    }
    std::cout << '\n';

    v.insert(v.begin(), 99);                // insertion en tête : décale tous les éléments (O(n))
    v.erase(v.begin() + 2);                 // suppression de l'élément d'indice 2
    v.pop_back();                           // retire le dernier
    std::erase_if(v, [](int x) { return x % 2 == 0; });    // supprime les pairs (C++20)
    for (int x : v) std::cout << x << ' ';
}
```

**Capacité amortie** : quand la capacité est dépassée, le vecteur alloue un bloc plus grand (typiquement ×1,5 ou ×2), y déplace ses éléments et libère l'ancien : `push_back` est donc O(1) **amorti**. **Piège** : cette réallocation rend **invalides** tous les itérateurs, pointeurs et références vers les éléments. Ne gardez pas `int &premier = v[0];` avant un `push_back`. Utilisez `reserve(n)` pour limiter les réallocations.

Principales fonctions : `push_back`, `emplace_back` (construit sur place), `insert`, `erase`, `pop_back`, `clear`, `size`, `capacity`, `empty`, `reserve`, `resize`, `shrink_to_fit`, `data()` (pointeur vers le tampon, pour les API C), `front`, `back`, `at`, `[]`.

### 16.4 Matrices dynamiques

```cpp
#include <iostream>
#include <vector>

class Matrice {
    std::size_t lignes_, colonnes_;
    std::vector<double> donnees_;                       // stockage contigu, ligne par ligne
public:
    Matrice(std::size_t l, std::size_t c) : lignes_(l), colonnes_(c), donnees_(l * c) {}

    double &operator()(std::size_t i, std::size_t j) { return donnees_[i * colonnes_ + j]; }
    double operator()(std::size_t i, std::size_t j) const { return donnees_[i * colonnes_ + j]; }
    std::size_t lignes() const { return lignes_; }
    std::size_t colonnes() const { return colonnes_; }
};

int main() {
    Matrice m(2, 3);
    for (std::size_t i = 0; i < m.lignes(); ++i)
        for (std::size_t j = 0; j < m.colonnes(); ++j)
            m(i, j) = static_cast<double>(i * 10 + j);
    std::cout << m(1, 2) << '\n';                        // 12
}                                                        // aucun delete à écrire
```

Le stockage à plat est favorable au cache du processeur ; en C++23, `std::mdspan` permet d'indexer un tel tampon avec plusieurs dimensions.

### 16.5 Conteneurs associatifs

```cpp
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_map>

int main() {
    std::map<std::string, int> ages{{"Ana", 30}};     // trié par clé
    ages["Luc"] = 25;                                 // insère ou modifie
    ages.insert({"Zoé", 41});
    ages.emplace("Max", 19);

    for (const auto &[nom, age] : ages) std::cout << nom << '=' << age << ' ';    // Ana=30 Luc=25 Max=19 Zoé=41
    std::cout << '\n';

    if (auto it = ages.find("Ana"); it != ages.end()) std::cout << it->second << '\n';
    std::cout << ages.contains("Bob") << '\n';        // 0 (C++20)
    ages.erase("Luc");

    std::unordered_map<std::string, int> freq;        // table de hachage : ordre quelconque
    for (const char *mot : {"a", "b", "a", "c", "a"}) ++freq[mot];
    std::cout << freq["a"] << '\n';                   // 3

    std::set<int> s{3, 1, 2, 3};                      // doublons ignorés, trié : 1 2 3
    std::cout << s.size() << '\n';                    // 3
}
```

**Piège** : `m[cle]` **insère** une entrée par défaut si la clé est absente. Pour consulter sans modifier, utilisez `find`, `contains` ou `at` (qui lève `std::out_of_range`). Une clé de `std::map` doit être comparable avec `<` ; une clé de `std::unordered_map` doit disposer d'une fonction de hachage (`std::hash`).

### 16.6 Itérateurs et algorithmes

Un **itérateur** est un objet qui se comporte comme un pointeur : `*it` donne l'élément, `++it` avance. Chaque conteneur fournit `begin()` et `end()` (un cran **après** le dernier élément) ; les algorithmes travaillent sur des intervalles `[début, fin)`.

```cpp
#include <iostream>
#include <ranges>
#include <vector>

int main() {
    std::vector<int> v{1, 2, 3, 4, 5, 6};

    for (auto it = v.begin(); it != v.end(); ++it) std::cout << *it << ' ';
    std::cout << '\n';

    auto resultat = v
        | std::views::filter([](int x) { return x % 2 == 0; })      // 2 4 6
        | std::views::transform([](int x) { return x * x; });       // 4 16 36 (évaluation paresseuse)
    for (int x : resultat) std::cout << x << ' ';
}
```

Catégories d'itérateurs, de la plus faible à la plus puissante : **entrée / sortie** (un seul passage), **avant** (`forward_list`), **bidirectionnel** (`list`, `map`, `set`), **à accès aléatoire** (`it + n`, `it[n]` : `vector`, `deque`, `array`), **contigu** *(C++20)* (éléments adjacents en mémoire : `vector`, `array`, `string`). Un algorithme exige une catégorie minimale ; par exemple `std::sort` demande l'accès aléatoire, donc ne fonctionne pas sur une `std::list` (utilisez `list::sort`).

### 16.7 Adaptateurs : pile, file, file de priorité

```cpp
std::stack<int> pile;  pile.push(1); pile.push(2);       // LIFO
std::cout << pile.top() << '\n';  pile.pop();            // 2

std::queue<std::string> file;  file.push("a"); file.push("b");   // FIFO
std::cout << file.front() << '\n';  file.pop();          // a

std::priority_queue<int> pq;                             // le plus grand en tête
for (int x : {5, 1, 8, 3}) pq.push(x);
std::cout << pq.top() << '\n';                           // 8
std::priority_queue<int, std::vector<int>, std::greater<>> min_pq;   // le plus petit en tête
```

### 16.8 Choisir un conteneur

- Suite d'éléments, cas général : **`std::vector`** (par défaut — quasi toujours le plus rapide en pratique grâce à la localité du cache).
- Taille connue à la compilation : `std::array`.
- Ajouts/retraits aux deux extrémités : `std::deque`.
- Recherche par clé avec tri : `std::map` / `std::set` ; recherche la plus rapide sans ordre : `std::unordered_map` / `std::unordered_set`.
- Insertions fréquentes au milieu avec itérateurs stables : `std::list`.
- LIFO, FIFO, priorité : `stack`, `queue`, `priority_queue`.

### À retenir (chapitre 16)

- Dans 90 % des cas, `std::vector` est le bon choix ; écrivez vos propres structures seulement pour apprendre ou pour un besoin spécifique.
- Une propriété claire (`unique_ptr` entre nœuds) supprime les fuites ; un destructeur itératif évite la récursion.
- Itérateurs invalidés par les réallocations et suppressions ; `m[k]` insère.

---

## Chapitre 17 — Références et pointeurs doubles

### 17.1 Les références

Une **référence** est un **alias** : un second nom pour un objet existant. Elle doit être **initialisée à sa déclaration** et ne peut plus désigner un autre objet ensuite. Elle n'occupe pas (conceptuellement) de mémoire propre et ne peut pas être nulle.

```cpp
#include <iostream>

int main() {
    int x = 10;
    int &r = x;                  // r est un autre nom pour x
    r = 20;                      // modifie x
    std::cout << x << '\n';      // 20

    const int &cr = 42;          // une référence constante peut se lier à un temporaire (durée de vie prolongée)
    // int &err = 42;            // ERREUR : référence non constante vers un temporaire
    std::cout << cr << '\n';

    int a = 1, b = 2;
    int &s = a;
    s = b;                       // ne « réaffecte » pas la référence : copie la valeur de b dans a
    std::cout << a << ' ' << b << '\n';   // 2 2
}
```

Comparaison avec le pointeur :

- une référence **ne peut pas être nulle**, un pointeur peut (`nullptr`) ;
- une référence **n'est pas réaffectable**, un pointeur l'est ;
- une référence s'utilise **directement** (`r`), un pointeur se déréférence (`*p`, `p->`) ;
- pas d'arithmétique sur les références ;
- usages typiques : **références** pour les paramètres, valeurs de retour et alias ; **pointeurs** pour l'optionnel, les structures liées et les API C.

Les familles de références :

- **`T &`** : référence **lvalue** (modifiable) ;
- **`const T &`** : lecture seule ; accepte aussi les temporaires ;
- **`T &&`** : référence **rvalue** (déplacement, chapitre 15) ; dans un template, `T &&` est une **référence universelle** (*forwarding reference*) qui se lie aussi bien à une lvalue qu'à une rvalue ;
- **`std::reference_wrapper<T>`** / `std::ref(x)` : référence **copiable et réaffectable**, utilisable dans un conteneur.

**Piège** : on ne peut pas former de tableau de références ni de `std::vector<T &>`. Utilisez `std::vector<std::reference_wrapper<T>>` ou des pointeurs.

### 17.2 Pointeurs doubles

Un **pointeur double** (`T **`) est un pointeur vers un pointeur : il contient l'adresse d'une variable qui est elle-même un pointeur.

```cpp
int x = 5;
int *p = &x;
int **pp = &p;                    // pp contient l'adresse de p
**pp = 10;                        // modifie x
std::cout << x << ' ' << *p << ' ' << **pp << '\n';    // 10 10 10
```

### 17.3 Usages principaux

**Modifier un pointeur depuis une fonction.** Pour qu'une fonction change *vers quoi* pointe le pointeur de l'appelant, il faut lui passer **l'adresse du pointeur** (`T **`) en C, ou une **référence vers le pointeur** (`T *&`) en C++.

```cpp
#include <iostream>

void allouer_c(int **p) { *p = new int(5); }       // style C : pointeur vers le pointeur
void allouer_ref(int *&p) { p = new int(6); }      // style C++ : référence vers le pointeur

int main() {
    int *a = nullptr, *b = nullptr;
    allouer_c(&a);
    allouer_ref(b);
    std::cout << *a << ' ' << *b << '\n';          // 5 6
    delete a;
    delete b;
}
```

En C++ moderne, on **retourne** simplement un `std::unique_ptr` au lieu de modifier un pointeur passé en paramètre.

**Matrice dynamique « à l'ancienne ».** Un tableau de pointeurs, chacun pointant vers une ligne :

```cpp
const int lignes = 3, colonnes = 4;
int **m = new int *[lignes];                                    // tableau de pointeurs
for (int i = 0; i < lignes; ++i) m[i] = new int[colonnes]();    // chaque ligne, initialisée à 0
m[1][2] = 9;
for (int i = 0; i < lignes; ++i) delete[] m[i];                 // libérer les lignes d'abord
delete[] m;                                                     // puis le tableau de pointeurs
```

Même schéma pour un tableau de chaînes (`char **`) ou le « pointeur vers le lien » d'une liste chaînée (chapitre 16). Le paramètre `char **argv` du `main` (chapitre 23) en est un autre exemple.

### 17.4 Libération et alternatives

Avec des pointeurs doubles bruts, il faut libérer **dans l'ordre inverse** de l'allocation, et chaque `new` doit avoir son `delete`. La solution moderne n'a aucune libération manuelle :

```cpp
std::vector<std::vector<int>> m(3, std::vector<int>(4));      // matrice sans new ni delete
std::vector<std::string> mots{"un", "deux", "trois"};         // remplace char **
```

### 17.5 Référence, pointeur ou pointeur double ?

- Paramètre obligatoire à modifier : `T &`.
- Paramètre en lecture seule, gros objet : `const T &`.
- Paramètre optionnel : `T *` (ou `std::optional<std::reference_wrapper<T>>`).
- Faire pointer l'appelant vers un nouvel objet : retourner un pointeur intelligent.
- Interface C (`char **argv`, `int **out`) : `T **`.
- Collection d'objets : un conteneur.

### À retenir (chapitre 17)

- Une référence est un alias non nul et non réaffectable ; `const T &` est le passage par défaut en lecture.
- `T **` sert aux API C ; en C++ préférez `T *&` ou le retour de pointeur intelligent.
- Aucune structure à base de `T **` ne devrait subsister dans du code neuf.

---

## Chapitre 18 — Structures, classes et unions

### 18.1 Les structures

En C++, une **`struct`** est un **type** à part entière : elle peut avoir des valeurs par défaut, des **fonctions membres**, des constructeurs et de l'héritage. La seule différence avec une `class` est l'**accès par défaut** : `public` pour `struct`, `private` pour `class`. Par convention : `struct` pour regrouper des données passives, `class` pour un type à invariants.

```cpp
#include <cmath>
#include <iostream>
#include <string>

struct Point {
    double x = 0.0;                    // valeurs par défaut des membres (C++11)
    double y = 0.0;

    double distance(const Point &autre) const {           // fonction membre ; const : ne modifie pas l'objet
        return std::hypot(x - autre.x, y - autre.y);
    }
};

struct Personne {
    std::string nom;
    int age;
    Point adresse;                     // structure imbriquée
};

int main() {
    Point a{1.0, 2.0};                 // initialisation d'agrégat
    Point b{.x = 4.0, .y = 6.0};       // initialisation désignée (C++20, dans l'ordre des membres)
    Point c;                           // (0, 0)
    Personne p{"Ana", 30, {1, 2}};

    Point *pp = &a;
    pp->x = 3.0;                       // accès par pointeur
    Point copie = a;                   // copie membre à membre
    std::cout << a.distance(b) << ' ' << p.nom << ' ' << c.x << ' ' << copie.y << '\n';
}
```

Un **agrégat** (struct simple, sans constructeur utilisateur ni membre privé) s'initialise avec `{ }` membre par membre.

### 18.2 Alignement et rembourrage (*padding*)

Pour que les accès soient rapides, chaque type doit être placé à une adresse multiple de son **alignement** (`alignof`). Le compilateur insère donc des octets de remplissage entre les membres :

```cpp
struct A { char c; int i; char d; };      // typiquement 12 octets
struct B { int i; char c; char d; };      // typiquement 8 octets : membres triés par taille décroissante
struct alignas(16) C { float v[3]; };     // alignement imposé de 16 octets
std::cout << sizeof(A) << ' ' << sizeof(B) << ' ' << sizeof(C) << ' ' << alignof(C) << '\n';   // 12 8 16 16
```

Ordonner les membres du plus grand au plus petit réduit le rembourrage. **Ne comptez jamais** sur `sizeof(struct)` = somme des membres, et ne sérialisez pas une structure par copie brute (`memcpy`, `write`) : le format dépend de la plateforme.

### 18.3 Champs de bits

```cpp
struct Drapeaux {
    unsigned lecture : 1;      // 1 bit
    unsigned ecriture : 1;
    unsigned niveau : 3;       // 3 bits : valeurs 0 à 7
};
```

La disposition des champs de bits dépend du compilateur ; pour des drapeaux **portables**, préférez `std::bitset` ou un `enum class` avec opérateurs bit à bit (chapitres 19 et 25).

### 18.4 Tableau dans une structure

Le **membre de tableau flexible** du C99 (`int donnees[];`) n'existe pas en C++ standard. On place un `std::array` (taille fixe, copié avec la structure) ou un `std::vector` (taille variable) comme membre :

```cpp
struct Etudiant {
    std::string nom;
    std::array<int, 3> notes{};
    std::vector<std::string> options;
};
```

### 18.5 Unions et `std::variant`

Une **union** regroupe plusieurs membres **à la même adresse** : un seul est « actif » à la fois, et sa taille est celle du plus grand membre. En C++, lire un membre autre que le dernier écrit est un **comportement indéfini** (contrairement au C). L'outil moderne est `std::variant`, une **union étiquetée** sûre *(C++17)* :

```cpp
#include <iostream>
#include <string>
#include <variant>

int main() {
    std::variant<int, double, std::string> w = 3.5;
    w = std::string("texte");

    if (std::holds_alternative<std::string>(w)) std::cout << std::get<std::string>(w) << '\n';
    if (auto *p = std::get_if<int>(&w)) std::cout << *p << '\n';      // nullptr : l'alternative active n'est pas int

    std::visit([](const auto &x) { std::cout << x << '\n'; }, w);     // appelle la lambda avec la valeur active
}
```

Compagnons : `std::optional<T>` (« une valeur ou rien »), `std::any` (n'importe quel type), `std::expected<T, E>` (valeur ou erreur).

**Choisir** : `struct` pour des données sans invariant ; `class` pour garantir des invariants ; `std::variant` pour un type somme ; `union` brute seulement pour le bas niveau ; `std::bit_cast` / `std::memcpy` pour réinterpréter des octets.

### 18.6 Classes et encapsulation

Une **classe** regroupe des **données** (membres) et les **fonctions** (méthodes) qui les manipulent, en **cachant** l'implémentation derrière une **interface** publique. Le but est de garantir des **invariants** : des propriétés toujours vraies, comme « le solde n'est jamais négatif ». Si les données étaient publiques, n'importe qui pourrait casser l'invariant ; avec l'encapsulation, seul le code de la classe le maintient.

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>

class CompteBancaire {
    double solde_ = 0.0;                   // privé par défaut dans une class
    std::string titulaire_;
public:
    explicit CompteBancaire(std::string titulaire, double solde_initial = 0.0)
        : solde_(solde_initial), titulaire_(std::move(titulaire)) {
        if (solde_initial < 0) throw std::invalid_argument("solde initial négatif");
    }

    void deposer(double montant) {
        if (montant <= 0) throw std::invalid_argument("montant invalide");
        solde_ += montant;
    }

    bool retirer(double montant) {
        if (montant <= 0 || montant > solde_) return false;
        solde_ -= montant;
        return true;
    }

    [[nodiscard]] double solde() const { return solde_; }                        // accesseur (lecture seule)
    [[nodiscard]] const std::string &titulaire() const { return titulaire_; }
};

int main() {
    CompteBancaire c("Ana", 100);
    c.deposer(50);
    std::cout << c.retirer(500) << ' ' << c.solde() << '\n';     // 0 150
    // c.solde_ = -1;                                            // ERREUR : membre privé
}
```

Niveaux d'accès : **`public`** (visible de tous), **`protected`** (la classe et ses dérivées), **`private`** (la classe et ses `friend`). Une **méthode `const`** (`double solde() const`) promet de ne pas modifier l'objet et peut être appelée sur un objet `const`.

### 18.7 Constructeurs et destructeur

Un **constructeur** a le nom de la classe, pas de type de retour, et initialise l'objet. Le **destructeur** (`~Classe()`) libère ses ressources. Les membres sont construits dans l'**ordre de leur déclaration** (et non de l'ordre de la liste d'initialisation), puis détruits dans l'ordre inverse.

```cpp
class Rectangle {
    double l_, h_;
public:
    Rectangle() : Rectangle(1.0, 1.0) {}                         // constructeur par défaut, délégué
    Rectangle(double l, double h) : l_(l), h_(h) {}              // liste d'initialisation de membres
    explicit Rectangle(double cote) : Rectangle(cote, cote) {}   // explicit : pas de conversion implicite
    ~Rectangle() = default;
    double aire() const { return l_ * h_; }
};

Rectangle a;               // 1 x 1
Rectangle b(2.0, 3.0);
Rectangle c{4.0};          // carré 4 x 4
// Rectangle d = 5.0;      // ERREUR : constructeur explicit
```

- **Constructeur par défaut** (`T()`), **paramétré**, **de copie** (`T(const T &)`), **de déplacement** (`T(T &&)`), **délégué** (appelle un autre constructeur de la classe).
- **Liste d'initialisation** (`: l_(l), h_(h)`) : initialise les membres **directement**, avant le corps du constructeur ; obligatoire pour les membres `const`, les références et les membres sans constructeur par défaut.
- **`explicit`** : interdit la conversion implicite par un constructeur à un argument ; à mettre sur ces constructeurs par défaut.
- **`= default`** demande la version générée ; **`= delete`** interdit l'opération (`Classe(const Classe &) = delete;` rend la classe non copiable).

### 18.8 Copie, déplacement et règle des cinq

Quand une classe **possède une ressource** (mémoire, fichier…), la copie membre à membre par défaut est fausse : deux objets finiraient par libérer la même ressource. Deux règles :

- **Règle du zéro** *(à privilégier)* : n'écrivez **aucune** des cinq fonctions spéciales ; ne détenez que des membres RAII (`vector`, `string`, `unique_ptr`…). Le compilateur génère tout correctement.
- **Règle des cinq** : si vous devez écrire l'une des cinq (destructeur, constructeur de copie, affectation par copie, constructeur de déplacement, affectation par déplacement), écrivez-les **toutes** (ou `= default` / `= delete`).

```cpp
#include <algorithm>
#include <cstddef>
#include <iostream>
#include <utility>

class Tampon {
    std::size_t n_ = 0;
    int *d_ = nullptr;
public:
    explicit Tampon(std::size_t n) : n_(n), d_(new int[n]()) {}

    ~Tampon() { delete[] d_; }                                              // 1. destructeur

    Tampon(const Tampon &o) : n_(o.n_), d_(new int[o.n_]) {                 // 2. constructeur de copie (copie profonde)
        std::copy(o.d_, o.d_ + n_, d_);
    }

    Tampon &operator=(const Tampon &o) {                                    // 3. affectation par copie
        if (this != &o) {
            Tampon tmp(o);                                                  // copier, puis échanger (sûr en cas d'exception)
            swap(tmp);
        }
        return *this;
    }

    Tampon(Tampon &&o) noexcept                                             // 4. constructeur de déplacement
        : n_(std::exchange(o.n_, 0)), d_(std::exchange(o.d_, nullptr)) {}

    Tampon &operator=(Tampon &&o) noexcept {                                // 5. affectation par déplacement
        if (this != &o) {
            delete[] d_;
            n_ = std::exchange(o.n_, 0);
            d_ = std::exchange(o.d_, nullptr);
        }
        return *this;
    }

    void swap(Tampon &o) noexcept { std::swap(n_, o.n_); std::swap(d_, o.d_); }
    std::size_t taille() const { return n_; }
    int &operator[](std::size_t i) { return d_[i]; }
};

int main() {
    Tampon a(4);
    a[2] = 7;
    Tampon b = a;                    // copie profonde
    Tampon c = std::move(a);         // déplacement : a est vidé
    std::cout << b[2] << ' ' << c[2] << ' ' << a.taille() << '\n';    // 7 7 0
}
```

Remplacez `int *` + taille par un `std::vector<int>` : la classe n'a plus besoin d'aucune des cinq fonctions (règle du zéro). Marquez `noexcept` les déplacements : les conteneurs ne les utilisent que s'ils ne peuvent pas lever d'exception.

### 18.9 Membres statiques, `mutable`, `friend`

```cpp
#include <iostream>

class Compteur {
    static inline int total_ = 0;            // membre statique : un seul exemplaire partagé (inline : C++17)
    int id_;
    mutable int lectures_ = 0;               // modifiable même dans une méthode const (cache, statistiques)
public:
    Compteur() : id_(++total_) {}
    static int total() { return total_; }    // fonction statique : pas de this, appelée par Compteur::total()
    int id() const { ++lectures_; return id_; }

    friend std::ostream &operator<<(std::ostream &os, const Compteur &c) {   // friend : accès aux membres privés
        return os << "Compteur#" << c.id_;
    }
};

int main() {
    Compteur a, b;
    const Compteur c;
    std::cout << a << ' ' << b << ' ' << c.id() << ' ' << Compteur::total() << '\n';   // Compteur#1 Compteur#2 3 3
}
```

- Un **membre statique** appartient à la **classe**, pas aux objets : un seul exemplaire partagé. Une **fonction statique** n'a pas de `this`.
- **`mutable`** autorise la modification d'un membre dans une méthode `const` (cache, compteur, `std::mutex`).
- **`friend`** accorde l'accès au privé à une fonction ou classe extérieure ; à utiliser avec parcimonie (typiquement `operator<<`).

### 18.10 Surcharge d'opérateurs

```cpp
#include <iostream>

class Vec2 {
public:
    double x = 0, y = 0;
    constexpr Vec2() = default;
    constexpr Vec2(double x_, double y_) : x(x_), y(y_) {}

    constexpr Vec2 &operator+=(const Vec2 &o) { x += o.x; y += o.y; return *this; }
    friend constexpr Vec2 operator+(Vec2 a, const Vec2 &b) { return a += b; }
    friend constexpr Vec2 operator*(Vec2 a, double k) { return {a.x * k, a.y * k}; }
    friend constexpr bool operator==(const Vec2 &, const Vec2 &) = default;     // comparaison générée (C++20)

    friend std::ostream &operator<<(std::ostream &os, const Vec2 &v) {
        return os << '(' << v.x << ", " << v.y << ')';
    }
};

int main() {
    Vec2 a{1, 2}, b{3, 4};
    std::cout << a + b << ' ' << a * 2 << ' ' << (a == b) << '\n';      // (4, 6) (2, 4) 0
}
```

Règles : conservez la **sémantique attendue** (`+` ne modifie pas ses opérandes) ; les opérateurs `::`, `.`, `.*`, `?:`, `sizeof`, `typeid` ne sont **pas** surchargeables ; ne surchargez pas `&&`, `||`, `,` ni le `&` unaire ; `auto operator<=>(const T &) const = default;` génère `<`, `<=`, `>`, `>=` *(C++20)* ; `operator[]`, `operator()` (objets-fonctions) et `operator->` (pointeurs intelligents) sont d'usage courant ; `explicit operator bool() const` permet de tester un objet dans un `if`.

### 18.11 Héritage

L'**héritage public** modélise une relation « **est un** » : la classe dérivée réutilise et étend la classe de base.

```cpp
#include <iostream>
#include <string>
#include <utility>

class Animal {
protected:
    std::string nom_;                                 // accessible aux classes dérivées
public:
    explicit Animal(std::string nom) : nom_(std::move(nom)) {}
    virtual ~Animal() = default;                      // destructeur VIRTUEL : indispensable pour une base polymorphe
    const std::string &nom() const { return nom_; }
};

class Chien : public Animal {                         // héritage public
    int tours_ = 0;
public:
    using Animal::Animal;                             // hérite des constructeurs de la base
    void aboyer() { ++tours_; std::cout << nom_ << " : Ouaf !\n"; }
};

int main() {
    Chien rex("Rex");
    rex.aboyer();
    Animal a = rex;                                   // « slicing » : seule la partie Animal est copiée !
    std::cout << a.nom() << '\n';
}
```

- **Formes** : `class D : public B` (« D est un B », cas courant) ; `protected` / `private` (implémentation seulement, rare : préférez la **composition**) ; **héritage multiple** `class D : public B1, public B2` (possible ; en cas de base commune — le « diamant » — utilisez l'héritage `virtual`) ; `class D final : public B` (interdit toute dérivation).
- **Ordre d'exécution** : constructeur de la base, puis des membres, puis corps du constructeur de la dérivée ; destruction dans l'ordre inverse.
- **Slicing** : copier un objet dérivé dans une variable du type de la base en perd la partie dérivée ; passez les objets polymorphes par référence ou pointeur.
- Le **polymorphisme** (fonctions virtuelles) est étudié au chapitre 21.

### 18.12 Bonnes pratiques

- `struct` pour de simples données, `class` pour des invariants.
- Données **privées** ; exposez le minimum d'interface.
- Initialisez les membres dans la liste d'initialisation, ou par valeur par défaut au niveau du membre.
- `explicit` sur les constructeurs à un argument ; `const` sur les méthodes de lecture.
- **Règle du zéro**, sinon règle des cinq ; **destructeur virtuel** pour toute base polymorphe.
- Préférez la **composition** à l'héritage.

### À retenir (chapitre 18)

- Une classe garantit des invariants par l'encapsulation ; constructeurs et destructeur gèrent la vie de l'objet.
- Règle du zéro d'abord ; règle des cinq si l'on possède une ressource brute.
- `static` partagé, `mutable` pour le cache, `friend` avec parcimonie.
- `std::variant` plutôt qu'`union`.

---

## Chapitre 19 — Énumérations (`enum`)

### 19.1 Définition

Une **énumération** définit un ensemble de constantes entières nommées. Le C++ propose deux formes : l'**`enum`** héritée du C et l'**`enum class`** *(C++11)*, plus sûre.

```cpp
#include <cstdint>
#include <iostream>

enum Couleur { ROUGE, VERT, BLEU };                           // non scopée : noms injectés dans la portée
enum class Jour : std::uint8_t { Lundi = 1, Mardi, Mercredi };   // scopée, type sous-jacent explicite

int main() {
    int c = VERT;                                  // 1 : conversion implicite (source de bugs)
    Jour j = Jour::Mardi;                          // le nom doit être qualifié
    // int n = j;                                  // ERREUR : pas de conversion implicite
    int n = static_cast<int>(j);                   // 2
    std::cout << c << ' ' << n << '\n';
}
```

- **`enum` classique** : les noms sont injectés dans la portée englobante (collisions possibles : deux `enum` ne peuvent pas avoir un énumérateur `ROUGE` chacun) ; conversion **implicite** en entier ; comparaison possible avec d'autres `enum` (dangereux).
- **`enum class`** : les noms ont leur **propre portée** (`Jour::Lundi`) ; **aucune conversion implicite** (cast explicite) ; type sous-jacent `int` par défaut, modifiable (`: std::uint8_t`) ; comparaison avec un autre `enum` interdite.

### 19.2 Avec `switch` et `using enum`

```cpp
#include <iostream>
#include <string_view>

enum class Feu { Rouge, Orange, Vert };

std::string_view nom(Feu f) {
    switch (f) {
        case Feu::Rouge:  return "rouge";
        case Feu::Orange: return "orange";
        case Feu::Vert:   return "vert";
    }
    return "inconnu";                       // atteint seulement avec une valeur invalide
}

void agir(Feu f) {
    using enum Feu;                         // importe les noms dans la portée (C++20)
    switch (f) {
        case Rouge:  std::cout << "stop\n"; break;
        case Orange: std::cout << "ralentir\n"; break;
        case Vert:   std::cout << "passer\n"; break;
    }
}

int main() { agir(Feu::Orange); std::cout << nom(Feu::Vert) << '\n'; }
```

**Bonne pratique** : ne mettez **pas** de `default` dans un `switch` sur une énumération : avec `-Wall`, le compilateur signale alors tout énumérateur oublié (`-Wswitch`).

### 19.3 Particularités

```cpp
#include <iostream>
#include <utility>

enum class Droit : unsigned { Aucun = 0, Lecture = 1, Ecriture = 2, Execution = 4 };   // drapeaux : puissances de 2

constexpr Droit operator|(Droit a, Droit b) {
    return static_cast<Droit>(std::to_underlying(a) | std::to_underlying(b));   // to_underlying : C++23
}
constexpr bool possede(Droit d, Droit drapeau) {
    return (std::to_underlying(d) & std::to_underlying(drapeau)) != 0;
}

int main() {
    Droit d = Droit::Lecture | Droit::Ecriture;
    std::cout << possede(d, Droit::Ecriture) << possede(d, Droit::Execution) << '\n';   // 10
    std::cout << std::to_underlying(d) << '\n';                                         // 3
}
```

- Les valeurs par défaut commencent à **0** et s'incrémentent de 1 ; on peut en fixer certaines (`Mardi = 5`) ; les suivantes continuent à partir de là.
- Il n'y a **aucune conversion automatique en chaîne** : écrivez une fonction (comme `nom` ci-dessus) ; la **réflexion statique** de C++26 permettra de la générer automatiquement.
- Convertir un entier en `enum class` sans vérification peut donner une valeur hors des énumérateurs déclarés : validez avant le `static_cast`.
- `std::to_underlying` *(C++23)* convertit un énumérateur vers son type sous-jacent.
- Pour des **drapeaux** combinables, utilisez `std::bitset` ou l'idiome ci-dessus (opérateurs bit à bit surchargés).

### 19.4 Bonnes pratiques

- `enum class` par défaut ; l'`enum` classique uniquement pour l'interopérabilité avec du code C.
- Précisez le **type sous-jacent** pour les formats de fichier ou de réseau.
- Nommez le type au singulier (`Couleur`) et les valeurs en `PascalCase` ou `MAJUSCULES` selon votre convention.
- Pour une valeur « parmi plusieurs types », utilisez `std::variant` plutôt qu'un `enum` + `union`.

### À retenir (chapitre 19)

- `enum class` : noms scopés, pas de conversion implicite, type sous-jacent choisi.
- `switch` sur une énumération sans `default` pour que le compilateur signale les oublis.
- Drapeaux : opérateurs bit à bit sur un `enum class` ou `std::bitset`.

---

## Chapitre 20 — `using`, `typedef` et templates

### 20.1 Alias de types : `using` et `typedef`

Un **alias** donne un nouveau nom à un type existant. Il ne crée pas un nouveau type : le compilateur voit exactement le même type.

```cpp
#include <map>
#include <string>
#include <vector>

typedef unsigned long ulong_t;                      // syntaxe héritée du C
using Entier = long long;                           // syntaxe moderne : « nom = type » (C++11)

using Operation = int (*)(int, int);                // pointeur de fonction : bien plus lisible
typedef int (*OperationC)(int, int);                // équivalent avec typedef

using Dictionnaire = std::map<std::string, std::vector<int>>;     // raccourcit un type verbeux

template <typename T>
using Vec = std::vector<T>;                         // alias TEMPLATE : impossible avec typedef
```

La syntaxe `using Nom = type;` se lit de gauche à droite et, **contrairement à `typedef`**, accepte les alias paramétrés (*alias templates*). Le motif C `typedef struct { ... } Nom;` est **inutile** en C++ : `struct Nom { ... };` définit déjà le type `Nom`.

Usages courants de `using` : type métier (`using Id = std::uint32_t;`), raccourci d'un type complexe, types publics d'une classe (`using value_type = T;`, convention des conteneurs), importation d'un membre de la base (`using Base::f;` ou `using Base::Base;`), importation des énumérateurs (`using enum Couleur;`, C++20), importation d'un nom d'espace de noms (`using std::string;`).

### 20.2 Templates de fonctions

Un **template** est un patron de code paramétré par un ou plusieurs **types** (ou valeurs). Le compilateur **instancie** une version concrète pour chaque combinaison d'arguments utilisée. C'est le mécanisme du **polymorphisme statique** (résolu à la compilation, sans surcoût d'exécution) et la base de la bibliothèque standard.

```cpp
#include <array>
#include <iostream>
#include <string>

template <typename T>
T maximum(T a, T b) { return (a > b) ? a : b; }

auto minimum(auto a, auto b) { return a < b ? a : b; }          // « template abrégé » (C++20)

template <typename T, std::size_t N>                           // paramètre non-type : une valeur
std::size_t taille(const std::array<T, N> &) { return N; }

int main() {
    std::cout << maximum(3, 7) << ' ' << maximum(2.5, 1.5) << '\n';       // T déduit : int, puis double
    std::cout << maximum<double>(3, 2.5) << '\n';                         // T précisé explicitement
    std::cout << maximum(std::string("a"), std::string("b")) << '\n';     // tout type comparable avec >
    std::cout << minimum(4, 9) << ' ' << taille(std::array<int, 6>{}) << '\n';
    // maximum(3, 2.5);                                                    // ERREUR : T ambigu (int ou double ?)
}
```

- La **déduction** des arguments de template se fait à partir des types des arguments de l'appel ; si elle est ambiguë, on précise explicitement (`maximum<double>`).
- Un paramètre de template peut être un **type** (`typename T` ou `class T`) ou une **valeur** (`std::size_t N`).
- Le code d'un template doit être **visible là où il est instancié** : on le **définit dans l'en-tête**.
- Un type qui ne supporte pas les opérations utilisées (ici `>`) provoque des erreurs longues et peu lisibles ; les **concepts** (§20.5) y remédient.

### 20.3 Templates de classes

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

template <typename T>
class Pile {
    std::vector<T> elements_;
public:
    void empiler(T valeur) { elements_.push_back(std::move(valeur)); }

    T depiler() {
        if (elements_.empty()) throw std::out_of_range("pile vide");
        T valeur = std::move(elements_.back());
        elements_.pop_back();
        return valeur;
    }

    [[nodiscard]] bool vide() const { return elements_.empty(); }
    [[nodiscard]] std::size_t taille() const { return elements_.size(); }
};

int main() {
    Pile<int> p;
    p.empiler(1);
    p.empiler(2);
    std::cout << p.depiler() << ' ' << p.taille() << '\n';       // 2 1

    Pile<std::string> s;
    s.empiler("a");

    std::vector v{1, 2, 3};          // déduction des arguments de template de classe (C++17) : vector<int>
    std::pair paire{1, 2.5};         // pair<int, double>
    std::cout << v.size() << ' ' << paire.second << '\n';
}
```

`Pile<int>` et `Pile<std::string>` sont deux **types distincts**, générés à la compilation. Depuis C++17, la **déduction des arguments de template de classe** (CTAD) permet d'écrire `std::vector v{1, 2, 3};` sans préciser `<int>`.

### 20.4 Spécialisation, `if constexpr`, templates variadiques

On peut fournir une version **spécialisée** d'un template pour un type particulier, ou choisir une branche **à la compilation** avec `if constexpr`.

```cpp
#include <iostream>
#include <string>
#include <type_traits>

template <typename T>
struct NomType { static constexpr const char *valeur = "inconnu"; };
template <>
struct NomType<int> { static constexpr const char *valeur = "int"; };          // spécialisation totale
template <>
struct NomType<double> { static constexpr const char *valeur = "double"; };

template <typename T>
std::string decrire(const T &v) {
    if constexpr (std::is_integral_v<T>) {                       // branche choisie à la compilation
        return "entier " + std::to_string(v);
    } else if constexpr (std::is_floating_point_v<T>) {
        return "réel " + std::to_string(v);
    } else {
        return "autre";
    }
}

template <typename... Args>                                      // nombre quelconque d'arguments
std::size_t compter(const Args &...args) { return sizeof...(args); }

int main() {
    std::cout << NomType<int>::valeur << ' ' << NomType<char>::valeur << '\n';     // int inconnu
    std::cout << decrire(42) << ' ' << decrire(2.5) << ' ' << decrire("x") << '\n';
    std::cout << compter(1, "a", 2.0) << '\n';                    // 3
}
```

- Les **traits de types** (`<type_traits>`) interrogent les propriétés d'un type à la compilation : `std::is_integral_v<T>`, `std::is_same_v<T, U>`, `std::is_pointer_v<T>`, `std::remove_reference_t<T>`…
- Un **template variadique** (`typename... Args`) accepte un nombre quelconque d'arguments ; `sizeof...(args)` les compte ; une **expression de repli** *(C++17)* comme `(args + ...)` combine tous les arguments avec un opérateur.
- **Transmission parfaite** : pour passer des arguments à une autre fonction **sans copie inutile**, on combine référence universelle `T &&` et `std::forward` :

```cpp
#include <utility>

template <typename F, typename... Args>
decltype(auto) appeler(F &&f, Args &&...args) {
    return std::forward<F>(f)(std::forward<Args>(args)...);
}
```

### 20.5 Concepts *(C++20)*

Un **concept** exprime les **contraintes** qu'un type doit satisfaire. Il rend les templates plus lisibles et les messages d'erreur beaucoup plus clairs.

```cpp
#include <concepts>
#include <cstddef>
#include <iostream>

template <typename T>
concept Numerique = std::integral<T> || std::floating_point<T>;

template <Numerique T>                                   // contrainte dans la liste de paramètres
T somme(T a, T b) { return a + b; }

template <typename T>
    requires std::totally_ordered<T>                     // clause requires
T plus_grand(T a, T b) { return a > b ? a : b; }

auto doubler(std::integral auto x) { return x * 2; }     // syntaxe abrégée

template <typename T>
concept AvecTaille = requires(T t) {                     // expression requires : valide des expressions
    { t.size() } -> std::convertible_to<std::size_t>;
};

template <AvecTaille C>
std::size_t nb(const C &c) { return c.size(); }

int main() {
    std::cout << somme(1, 2) << ' ' << plus_grand(3.5, 2.0) << ' ' << doubler(21) << '\n';
    // somme("a", "b");        // ERREUR claire : contrainte « Numerique » non satisfaite
}
```

Concepts standard (`<concepts>`) : `std::integral`, `std::floating_point`, `std::same_as<T, U>`, `std::convertible_to<From, To>`, `std::totally_ordered`, `std::equality_comparable`, `std::copyable`, `std::movable`, `std::default_initializable`, `std::invocable<F, Args...>`, `std::predicate`, `std::ranges::range`, `std::input_iterator`. Trois syntaxes : `template <Concept T>`, clause `requires`, et `Concept auto` pour les paramètres abrégés.

### 20.6 Bonnes pratiques

- Préférez `using` à `typedef`.
- Utilisez des alias pour **nommer l'intention** (`using Seconds = double;`), pas seulement pour raccourcir.
- **Contraignez** vos templates avec des concepts.
- Gardez les templates courts ; déléguez aux algorithmes standard.
- Jamais de `using namespace` dans un en-tête.

### À retenir (chapitre 20)

- `using` = alias moderne (et seul capable d'alias paramétrés).
- Template = patron instancié à la compilation ; définir dans l'en-tête.
- `if constexpr`, traits de types, templates variadiques, transmission parfaite : les outils du code générique.
- Concepts : contraintes lisibles, erreurs claires.

---

## Chapitre 21 — Pointeurs de fonctions, lambdas et polymorphisme

Ce chapitre traite d'un même besoin sous trois formes : **faire varier un comportement** (quelle fonction appeler) à l'exécution ou à la compilation.

### 21.1 Pointeurs de fonctions

Un **pointeur de fonction** contient l'adresse d'une fonction ; on peut l'appeler, le passer en paramètre ou le stocker.

```cpp
#include <iostream>

int addition(int a, int b) { return a + b; }
int soustraction(int a, int b) { return a - b; }

int main() {
    int (*op)(int, int) = addition;           // op : pointeur vers une fonction (int, int) -> int
    std::cout << op(5, 3) << '\n';            // 8
    op = &soustraction;                       // le & est facultatif
    std::cout << op(5, 3) << '\n';            // 2
}
```

Attention à la syntaxe : `int (*f)(int, int)` est un **pointeur de fonction**, mais `int *f(int, int)` déclare une **fonction** qui retourne un `int *`. On simplifie avec un alias : `using Op = int (*)(int, int);`. L'appel s'écrit `f(a, b)` ou `(*f)(a, b)`.

### 21.2 Callbacks et tables de fonctions

Un **callback** est une fonction passée à une autre pour qu'elle l'appelle au bon moment (comparateur de tri, gestionnaire d'événement).

```cpp
#include <algorithm>
#include <iostream>
#include <string_view>
#include <vector>

using Operation = int (*)(int, int);

int addition(int a, int b) { return a + b; }
int soustraction(int a, int b) { return a - b; }
int appliquer(Operation f, int a, int b) { return f(a, b); }

bool decroissant(int a, int b) { return a > b; }

struct Commande {
    std::string_view nom;
    Operation action;
};
constexpr Commande commandes[] = {{"add", addition}, {"sub", soustraction}};     // table de fonctions

int main() {
    std::cout << appliquer(addition, 6, 7) << '\n';        // 13

    std::vector<int> v{3, 1, 2};
    std::sort(v.begin(), v.end(), decroissant);            // 3 2 1 : comparateur fourni par l'utilisateur

    for (const auto &c : commandes) std::cout << c.nom << " : " << c.action(6, 2) << '\n';
}
```

`qsort` et `bsearch` du C fonctionnent en C++ mais utilisent `void *` : préférez `std::sort`, `std::ranges::sort` et `std::lower_bound`, typés et souvent plus rapides (le compilateur peut intégrer le comparateur).

### 21.3 Lambdas et `std::function` *(C++11)*

Une **lambda** est une fonction anonyme définie sur place, capable de **capturer** des variables de son contexte. Elle crée un objet (un *closure*) dont le type est unique et connu du seul compilateur.

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>

int main() {
    auto carre = [](int x) { return x * x; };                  // sans capture
    int facteur = 3;
    auto fois = [facteur](int x) { return x * facteur; };      // capture par VALEUR (copie)
    int total = 0;
    auto cumule = [&total](int x) { total += x; };             // capture par RÉFÉRENCE
    auto somme = [](auto a, auto b) { return a + b; };         // lambda générique (C++14)

    std::vector<int> v{1, 2, 3, 4};
    std::for_each(v.begin(), v.end(), cumule);                 // total = 10
    std::cout << carre(5) << ' ' << fois(5) << ' ' << total << ' ' << somme(1, 2.5) << '\n';   // 25 15 10 3.5

    std::function<int(int)> f = fois;                          // objet-fonction polymorphe
    f = carre;
    std::cout << f(4) << '\n';                                 // 16

    std::sort(v.begin(), v.end(), [](int a, int b) { return a > b; });     // comparateur en ligne
}
```

La syntaxe est `[captures](paramètres) -> retour { corps }` ; le type de retour est déduit et les parenthèses sont facultatives si la liste de paramètres est vide.

Modes de capture :

- `[]` : rien ; `[x]` : `x` par copie ; `[&x]` : `x` par référence ;
- `[=]` / `[&]` : tout par copie / par référence (à utiliser avec prudence) ;
- `[this]` : le pointeur vers l'objet courant ; `[*this]` *(C++17)* : une **copie** de l'objet ;
- `[y = std::move(x)]` *(C++14)* : capture avec initialisation (déplacement) ;
- `mutable` : autorise la modification des copies capturées.

Quel type d'objet appelable choisir ?

- **Pointeur de fonction** : interface C, callback sans état.
- **Lambda (`auto`) ou paramètre template** : le plus rapide ; type connu à la compilation, intégrable par le compilateur.
- **`std::function<R(Args...)>`** : pour **stocker** des appelables de natures différentes (a un coût : indirection, allocation possible).
- **`std::move_only_function`** *(C++23)* : comme `std::function` mais accepte les objets non copiables.

**Piège** : une lambda qui capture une variable **par référence** ne doit pas survivre à cette variable (rappel asynchrone, thread, valeur de retour) : la référence deviendrait pendante.

### 21.4 Polymorphisme et fonctions virtuelles

Dans le C, on simule des « méthodes » avec des pointeurs de fonctions dans une structure. Le C++ intègre ce mécanisme au langage : les **fonctions virtuelles**. Le compilateur construit pour chaque classe une **table virtuelle** (*vtable*) de pointeurs de fonctions, et choisit la bonne **à l'exécution** selon le **type réel** de l'objet (liaison dynamique).

```cpp
#include <iostream>
#include <memory>
#include <numbers>
#include <string>
#include <vector>

class Forme {
public:
    virtual ~Forme() = default;                                // destructeur virtuel : indispensable
    virtual double aire() const = 0;                           // virtuelle PURE : classe abstraite
    virtual std::string nom() const { return "forme"; }        // implémentation par défaut
};

class Cercle : public Forme {
    double r_;
public:
    explicit Cercle(double r) : r_(r) {}
    double aire() const override { return std::numbers::pi * r_ * r_; }    // override : vérifié par le compilateur
    std::string nom() const override { return "cercle"; }
};

class Rectangle final : public Forme {                        // final : aucune classe ne peut en dériver
    double l_, h_;
public:
    Rectangle(double l, double h) : l_(l), h_(h) {}
    double aire() const override { return l_ * h_; }
};

int main() {
    std::vector<std::unique_ptr<Forme>> formes;
    formes.push_back(std::make_unique<Cercle>(1.0));
    formes.push_back(std::make_unique<Rectangle>(2.0, 3.0));

    for (const auto &f : formes) {
        std::cout << f->nom() << " : " << f->aire() << '\n';     // appel résolu à l'exécution
    }

    if (auto *c = dynamic_cast<Cercle *>(formes[0].get())) {      // conversion vérifiée (nullptr si échec)
        std::cout << "c'est bien un cercle\n";
        (void)c;
    }
    // Forme f;                                                    // ERREUR : classe abstraite non instanciable
}                                                                  // destruction correcte grâce au destructeur virtuel
```

- **`virtual`** : la fonction peut être redéfinie dans une classe dérivée ; l'appel dépend du type **réel** de l'objet.
- **`= 0`** : fonction virtuelle **pure** ; la classe devient **abstraite** (une interface), non instanciable.
- **`override`** : vérifie qu'on redéfinit bien une virtuelle de la base (à écrire **systématiquement**).
- **`final`** : interdit la redéfinition d'une fonction ou la dérivation d'une classe.
- **`virtual ~Base()`** : **obligatoire** si l'on détruit un objet dérivé via un pointeur de base ; sinon, comportement indéfini.
- **`dynamic_cast<D *>(b)`** : descente vérifiée à l'exécution dans la hiérarchie (nécessite une base polymorphe) ; retourne `nullptr` (ou lève `std::bad_cast` pour une référence) si le type réel ne convient pas. **`typeid`** donne le type réel (RTTI).

**Piège** : le polymorphisme ne fonctionne qu'avec des **pointeurs ou références** vers la base. Une copie par valeur (`Forme f = cercle;`) provoque le *slicing*. Chaque appel virtuel coûte une indirection ; quand les types sont connus à la compilation, les **templates** et `std::variant` sont des alternatives sans surcoût.

### 21.5 Sélection générique : surcharge, templates, `std::visit`

Le `_Generic` du C est remplacé en C++ par la **surcharge**, les **templates** et `if constexpr` (choix à la compilation), et par `std::visit` (choix à l'exécution selon l'alternative active d'un `std::variant`).

```cpp
#include <iostream>
#include <string>
#include <variant>

template <class... Ts>
struct Surcharge : Ts... { using Ts::operator()...; };      // assemble plusieurs lambdas en un seul objet

int main() {
    std::variant<int, std::string> v = std::string("texte");
    std::visit(Surcharge{
                   [](int i) { std::cout << "int " << i << '\n'; },
                   [](const std::string &s) { std::cout << "string " << s << '\n'; }},
               v);
}
```

### À retenir (chapitre 21)

- Pointeur de fonction : callback simple ; lambda : fonction anonyme capturant son contexte ; `std::function` : stockage polymorphe.
- Fonctions virtuelles + pointeurs/références + destructeur virtuel = polymorphisme d'exécution ; toujours `override`.
- Polymorphisme statique (templates, `variant`) quand les types sont connus à la compilation.

---

# Niveau avancé

---

## Chapitre 22 — Gestion des fichiers

### 22.1 Les flux de fichiers

La bibliothèque `<fstream>` fournit les flux de fichiers, qui s'utilisent **exactement comme** `std::cin` et `std::cout` : mêmes opérateurs `<<` et `>>`, mêmes états d'erreur, mêmes manipulateurs.

- **`std::ifstream`** : lecture (*input file stream*) ;
- **`std::ofstream`** : écriture (*output*) ;
- **`std::fstream`** : lecture et écriture.

Modes d'ouverture (`std::ios::`) : `in` (lecture), `out` (écriture), `app` (écrit toujours à la fin : ajout), `trunc` (vide le fichier à l'ouverture, défaut de `ofstream`), `ate` (se place à la fin à l'ouverture), `binary` (aucune traduction de fins de ligne). Ils se combinent avec `|`.

### 22.2 Ouvrir et fermer : RAII

Le fichier est **ouvert par le constructeur** (ou `open`) et **fermé automatiquement par le destructeur** : `close()` explicite est rarement nécessaire. Limitez la portée du flux pour que le fichier soit fermé au plus tôt.

```cpp
#include <cstdlib>
#include <fstream>
#include <iostream>

int main() {
    std::ifstream f("donnees.txt");
    if (!f) {                                                    // ou !f.is_open()
        std::cerr << "Impossible d'ouvrir donnees.txt\n";
        return EXIT_FAILURE;
    }
    std::cout << "Fichier ouvert\n";
}                                                                // f est fermé ici
```

**Vérifiez toujours l'ouverture** : un flux dont l'ouverture a échoué est en état d'erreur et toutes les opérations suivantes sont silencieusement ignorées.

### 22.3 Écrire du texte

```cpp
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <print>

int main() {
    std::ofstream out("notes.txt");                              // crée ou écrase
    if (!out) {
        std::cerr << "Erreur d'ouverture\n";
        return EXIT_FAILURE;
    }
    out << "Ligne 1\n" << 42 << ' ' << 3.14 << '\n';
    std::println(out, "valeur = {:>6.2f}", 2.71828);              // C++23

    std::ofstream journal("journal.log", std::ios::app);         // ajoute à la fin
    journal << "démarrage\n";
}
```

### 22.4 Lire du texte

```cpp
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

int main() {
    std::ifstream in("notes.txt");
    if (!in) return 1;

    std::string ligne;
    while (std::getline(in, ligne)) {                  // lit ligne par ligne jusqu'à la fin
        std::cout << ligne << '\n';
    }

    in.clear();                                        // retire l'état « fin de fichier »
    in.seekg(0);                                       // retourne au début

    int n; double d;
    while (in >> n >> d) {                             // lecture formatée : s'arrête à la première erreur
        std::cout << n << ' ' << d << '\n';
    }

    in.clear();
    in.seekg(0);
    std::ostringstream tampon;
    tampon << in.rdbuf();                              // tout le fichier d'un coup
    std::string contenu = tampon.str();
    std::cout << contenu.size() << " octets\n";
}
```

**Piège** : n'écrivez jamais `while (!in.eof()) { ... }`. Le drapeau de fin de fichier n'est positionné qu'**après** une lecture ratée ; la dernière itération traiterait donc des données invalides. Testez le résultat de la lecture : `while (std::getline(in, ligne))`.

### 22.5 Fichiers binaires

En mode binaire, on lit et on écrit des **octets bruts** avec `read` et `write`.

```cpp
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>

struct Enregistrement {            // type trivialement copiable
    std::int32_t id;
    double valeur;
};

int main() {
    {
        std::ofstream out("data.bin", std::ios::binary);
        Enregistrement e{1, 2.5};
        out.write(reinterpret_cast<const char *>(&e), sizeof e);

        std::vector<int> v{10, 20, 30};
        out.write(reinterpret_cast<const char *>(v.data()), static_cast<std::streamsize>(v.size() * sizeof(int)));
    }

    std::ifstream in("data.bin", std::ios::binary);
    Enregistrement r{};
    if (in.read(reinterpret_cast<char *>(&r), sizeof r)) {
        std::cout << r.id << ' ' << r.valeur << '\n';
    }
}
```

Texte : lisible, plus volumineux, portable (attention à l'encodage). Binaire : compact et rapide, mais **fragile** : le rembourrage (*padding*), l'ordre des octets (*endianness*) et la taille des types varient selon la plateforme. Pour un format d'échange, **sérialisez champ par champ** avec des types à taille fixe (`<cstdint>`), ou utilisez un format standard (JSON, Protocol Buffers…).

### 22.6 Se positionner dans un fichier

`seekg(pos, origine)` / `seekp(pos, origine)` déplacent la position de lecture (*get*) / d'écriture (*put*) ; `tellg()` / `tellp()` la donnent. Origines : `std::ios::beg` (début), `cur` (position courante), `end` (fin).

```cpp
std::ifstream in("data.bin", std::ios::binary);
in.seekg(0, std::ios::end);                // va à la fin
std::streamoff taille = in.tellg();        // la position vaut la taille en octets
in.seekg(0, std::ios::beg);                // revient au début
```

### 22.7 Fichiers et dossiers : `<filesystem>` *(C++17)*

```cpp
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    fs::path chemin = fs::path("dossier") / "sous" / "rapport.txt";     // « / » assemble les chemins
    std::cout << chemin.filename() << ' ' << chemin.stem() << ' ' << chemin.extension() << '\n';

    fs::create_directories("dossier/sous");                             // crée toute l'arborescence
    std::error_code ec;
    if (fs::exists("notes.txt", ec)) {
        std::cout << fs::file_size("notes.txt") << " octets\n";
        fs::copy_file("notes.txt", "dossier/sous/copie.txt", fs::copy_options::overwrite_existing, ec);
        fs::rename("dossier/sous/copie.txt", "dossier/sous/renomme.txt", ec);
    }

    for (const auto &entree : fs::directory_iterator(".")) {            // parcourt le dossier courant
        std::cout << entree.path().filename().string() << (entree.is_directory() ? "/" : "") << '\n';
    }
    fs::remove_all("dossier");                                          // supprime récursivement
}
```

Les fonctions de `<filesystem>` lèvent `std::filesystem::filesystem_error` en cas d'échec, sauf si on leur passe un paramètre `std::error_code &` (version sans exception). Elles remplacent `remove` et `rename` du C et les appels propres à chaque système. `fs::path` gère les séparateurs (`/` ou `\`) et les extensions de façon portable ; utilisez `recursive_directory_iterator` pour parcourir une arborescence.

### 22.8 Flux en mémoire

`std::istringstream`, `std::ostringstream` et `std::stringstream` (`<sstream>`) appliquent l'interface des flux à une `std::string` : pratiques pour analyser du texte ou construire une chaîne.

```cpp
std::istringstream entree("12 3.5 mot");
int n; double d; std::string s;
entree >> n >> d >> s;                       // lecture formatée depuis une chaîne

std::ostringstream sortie;
sortie << "n=" << n << ", d=" << d;          // construction d'une chaîne
std::cout << sortie.str() << ' ' << s << '\n';
```

### 22.9 États du flux et erreurs

- `good()` : tout va bien ; `eof()` : fin atteinte **par une lecture** ; `fail()` : échec logique (format invalide) ou erreur ; `bad()` : erreur grave (disque, flux corrompu) ; `clear()` : remet l'état à « bon ».
- On peut demander aux flux de **lever des exceptions** :

```cpp
std::ifstream f;
f.exceptions(std::ios::failbit | std::ios::badbit);       // les erreurs lèvent std::ios_base::failure
try {
    f.open("absent.txt");
} catch (const std::ios_base::failure &e) {
    std::cerr << "Erreur de fichier : " << e.what() << '\n';
}
```

### 22.10 Bonnes pratiques

- Vérifiez **toujours** l'ouverture et le résultat des lectures / écritures.
- Laissez le destructeur fermer le fichier ; limitez la portée du flux.
- Utilisez `std::filesystem::path` pour manipuler les chemins.
- Pour un format binaire, fixez la taille des types et l'ordre des octets.
- Écrivez dans un fichier temporaire puis `rename` pour éviter les fichiers à moitié écrits.

### À retenir (chapitre 22)

- Les fichiers sont des flux ; ouverture = construction, fermeture = destruction (RAII).
- Lisez avec `while (getline(...))` ou `while (in >> x)`, jamais `while (!eof())`.
- Binaire : `read` / `write` avec des types à taille fixe ; `<filesystem>` pour les chemins.

---

## Chapitre 23 — Arguments de la ligne de commande

### 23.1 `argc` et `argv`

Un programme peut recevoir des paramètres au lancement (`./prog fichier.txt -v`). Ils sont transmis à `main` sous la forme de deux paramètres :

```cpp
#include <iostream>

int main(int argc, char *argv[]) {
    std::cout << "argc = " << argc << '\n';
    for (int i = 0; i < argc; ++i) {
        std::cout << "argv[" << i << "] = " << argv[i] << '\n';
    }
}
```

```bash
g++ -std=c++20 args.cpp -o args
./args bonjour 42 "deux mots"
# argc = 4
# argv[0] = ./args
# argv[1] = bonjour
# argv[2] = 42
# argv[3] = deux mots
```

- **`argc`** (*argument count*) : nombre d'arguments, **nom du programme compris** (donc au moins 1 en pratique).
- **`argv`** (*argument vector*) : tableau de chaînes C ; `argv[0]` est le nom (ou chemin) du programme, `argv[1]` … `argv[argc - 1]` les arguments, et `argv[argc]` vaut toujours `nullptr`.
- Le shell découpe la ligne : les guillemets regroupent des mots en un seul argument.

En C++ moderne, on convertit tout de suite les arguments en objets plus sûrs :

```cpp
#include <iostream>
#include <span>
#include <string_view>
#include <vector>

int main(int argc, char *argv[]) {
    std::vector<std::string_view> args(argv + 1, argv + argc);        // sans le nom du programme
    for (std::string_view a : args) std::cout << '[' << a << ']';
    std::cout << '\n';

    std::span<char *> brut(argv, static_cast<std::size_t>(argc));     // vue sur le tableau d'origine
    std::cout << brut.size() << '\n';
}
```

Les `std::string_view` ne copient rien et restent valides pendant toute l'exécution de `main` (les chaînes de `argv` vivent jusqu'à la fin du programme).

### 23.2 Conversion et validation

Les arguments sont **toujours des chaînes** : il faut les convertir, puis **valider** le résultat (format, plage, caractères en trop).

```cpp
#include <cstdlib>
#include <iostream>
#include <string>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        std::cerr << "Usage : " << argv[0] << " nombre...\n";
        return EXIT_FAILURE;
    }

    double total = 0;
    for (int i = 1; i < argc; ++i) {
        try {
            std::size_t lus = 0;
            total += std::stod(argv[i], &lus);                    // lus = nombre de caractères convertis
            if (lus != std::string(argv[i]).size()) throw std::invalid_argument("reste");
        } catch (const std::exception &) {
            std::cerr << "Argument invalide : " << argv[i] << '\n';
            return EXIT_FAILURE;
        }
    }
    std::cout << "somme = " << total << '\n';
}
```

`std::stod("12abc")` réussit en lisant `12` : c'est pourquoi on compare le nombre de caractères convertis à la longueur totale.

### 23.3 Options (`-h`, `--fichier`)

Par convention Unix, une **option** commence par `-` (forme courte) ou `--` (forme longue) ; certaines attendent une **valeur** (`-o fichier`).

```cpp
#include <cstdlib>
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

int main(int argc, char *argv[]) {
    std::vector<std::string_view> args(argv + 1, argv + argc);
    bool verbeux = false;
    std::string sortie = "a.out";

    for (std::size_t i = 0; i < args.size(); ++i) {
        if (args[i] == "-h" || args[i] == "--help") {
            std::cout << "Usage : prog [-v] [-o fichier]\n";
            return 0;
        } else if (args[i] == "-v") {
            verbeux = true;
        } else if (args[i] == "-o" && i + 1 < args.size()) {
            sortie = args[++i];                                   // la valeur suit l'option
        } else {
            std::cerr << "Option inconnue : " << args[i] << '\n';
            return EXIT_FAILURE;
        }
    }
    std::cout << "verbeux = " << verbeux << ", sortie = " << sortie << '\n';
}
```

Pour des interfaces riches (sous-commandes, aide générée, validations), utilisez une bibliothèque : **CLI11**, **cxxopts**, **Boost.Program\_options**, ou `getopt` / `getopt_long` (POSIX).

### 23.4 Variables d'environnement

```cpp
#include <cstdlib>
#include <iostream>

int main() {
    if (const char *home = std::getenv("HOME")) {      // nullptr si la variable n'existe pas
        std::cout << "HOME = " << home << '\n';
    }
}
```

`std::getenv` lit une variable d'environnement. Le pointeur retourné ne doit pas être modifié ni conservé après un changement de l'environnement.

### 23.5 Bonnes pratiques

- Vérifiez `argc` **avant** d'accéder à `argv[i]`.
- Affichez un message d'usage clair et retournez `EXIT_FAILURE` en cas d'erreur.
- Convertissez et **validez** chaque valeur ; ne faites jamais confiance à l'utilisateur.
- Ne modifiez pas les chaînes de `argv` ; copiez-les au besoin.
- Sous Windows avec des noms non ASCII, utilisez `wmain` ou l'API du système (chapitre 27).

### À retenir (chapitre 23)

- `argc` compte le nom du programme ; `argv[argc]` est `nullptr`.
- Convertissez vite `argv` en `std::vector<std::string_view>`.
- Toute valeur reçue est une chaîne à convertir et valider.

---

## Chapitre 24 — Directives du préprocesseur et modules

### 24.1 Rôle du préprocesseur

Le **préprocesseur** transforme le **texte** du programme **avant** la compilation. Il ne connaît ni types, ni portées, ni syntaxe C++ : il manipule des lignes et des jetons. Ses directives commencent par `#` et occupent une ligne.

- `#include` : insère le contenu d'un fichier.
- `#define` / `#undef` : définit / supprime une macro.
- `#if`, `#ifdef`, `#ifndef`, `#elif`, `#else`, `#endif` : compilation conditionnelle.
- `#error` / `#warning` : message d'erreur / d'avertissement (`#warning` standardisé en C++23).
- `#pragma` : instruction propre au compilateur (`#pragma once`).
- `#line` : modifie le numéro de ligne et le nom de fichier rapportés.
- `#embed` *(C++26)* : intègre le contenu binaire d'un fichier.
- `import` / `export module` *(C++20)* : modules (traités par le compilateur, pas par le préprocesseur).

### 24.2 `#include`

```cpp
#include <iostream>        // en-tête de la bibliothèque standard : recherché dans les dossiers système
#include <cstdio>          // en-tête hérité du C : préfixe « c », sans « .h »
#include "maths.hpp"       // en-tête du projet : recherché d'abord dans le dossier courant
```

**Bonne pratique** : incluez dans l'ordre l'en-tête correspondant au fichier, puis ceux du projet, puis les bibliothèques tierces, puis la bibliothèque standard. Cela détecte les en-têtes non autonomes. N'incluez que ce que vous utilisez, et **jamais** un `.cpp`.

### 24.3 Macros avec `#define`

Une **macro** est un remplacement textuel effectué avant la compilation.

```cpp
#include <iostream>

#define VERSION "1.0"                       // macro-constante (préférer constexpr)
#define CARRE(x) x * x                      // macro-fonction MAL écrite
#define CARRE_OK(x) ((x) * (x))             // parenthèses partout

constexpr int carre(int x) { return x * x; }                    // la vraie solution
template <typename T> constexpr T carre_t(T x) { return x * x; }

int main() {
    std::cout << CARRE(2 + 3) << '\n';          // 2 + 3 * 2 + 3 = 11 (et non 25)
    std::cout << CARRE_OK(2 + 3) << '\n';       // 25

    int i = 3;
    std::cout << CARRE_OK(i++) << '\n';         // i++ évalué DEUX fois : comportement indéfini
    std::cout << carre(i) << ' ' << carre_t(2.5) << ' ' << VERSION << '\n';   // aucun de ces pièges avec une fonction
}
```

Opérateurs spéciaux : **`#`** transforme un argument de macro en chaîne littérale ; **`##`** colle deux jetons ; une **macro variadique** utilise `__VA_ARGS__` (et `__VA_OPT__`, C++20, pour la virgule conditionnelle).

```cpp
#define AFFICHE(var) std::cout << #var << " = " << (var) << '\n'    // # : argument -> chaîne
#define CONCAT(a, b) a##b                                            // ## : colle deux jetons
#define LOG(fmt, ...) std::printf(fmt "\n" __VA_OPT__(,) __VA_ARGS__)

int total = 42;
AFFICHE(total);                    // total = 42
int CONCAT(valeur, 1) = 5;         // déclare « valeur1 »
```

**Les macros ignorent types, portées et espaces de noms** et provoquent des erreurs obscures. Alternatives : `constexpr` pour les constantes ; fonctions `inline` / `constexpr` / templates pour le calcul ; `enum class` pour les familles de constantes ; `std::source_location` pour le diagnostic. Réservez les macros à l'inclusion conditionnelle, à la détection de plateforme et aux rares cas qu'aucune autre fonctionnalité ne couvre.

### 24.4 Compilation conditionnelle

```cpp
#include <iostream>

#if defined(_WIN32)
    #define PLATEFORME "Windows"
#elif defined(__linux__)
    #define PLATEFORME "Linux"
#elif defined(__APPLE__)
    #define PLATEFORME "macOS"
#else
    #define PLATEFORME "inconnue"
#endif

#if __cplusplus >= 202002L
    #define STANDARD "C++20 ou plus"
#else
    #define STANDARD "avant C++20"
#endif

#if __has_include(<format>)                         // l'en-tête existe-t-il ? (C++17)
    #include <format>
#endif

int main() {
    std::cout << PLATEFORME << " / " << STANDARD << '\n';
#ifdef __cpp_lib_format                             // macros de test de fonctionnalité
    std::cout << "std::format disponible\n";
#endif
}
```

Macros prédéfinies utiles : `__cplusplus` (version de la norme : `201703L`, `202002L`, `202302L`…) ; macros de **test de fonctionnalité** `__cpp_*` et `__cpp_lib_*` (en-tête `<version>`) ; `_WIN32`, `__linux__`, `__APPLE__` (systèmes) ; `__GNUC__`, `__clang__`, `_MSC_VER` (compilateurs) ; `NDEBUG` (désactive `assert`, mode release). `__FILE__`, `__LINE__` et la variable `__func__` renseignent le contexte.

### 24.5 Gardes d'inclusion

Un en-tête inclus deux fois (directement ou par ricochet) provoque des redéfinitions. On le protège :

```cpp
// point.hpp
#ifndef POINT_HPP                // garde classique (portable)
#define POINT_HPP
struct Point { double x, y; };
#endif // POINT_HPP
```

```cpp
// point.hpp (variante)
#pragma once                     // non standard mais supporté par tous les compilateurs courants
struct Point { double x, y; };
```

### 24.6 Autres directives et diagnostic

```cpp
#if __cplusplus < 201703L
    #error "Ce projet nécessite C++17 ou plus"       // arrête la compilation
#endif
```

Avec **C++26**, `#embed` incorpore un fichier dans le programme sous forme d'octets (compilateurs récents) :

```cpp
constexpr unsigned char logo[] = {
#embed "logo.png"
};
```

`std::source_location` *(C++20)* remplace avantageusement `__FILE__` / `__LINE__` :

```cpp
#include <iostream>
#include <source_location>
#include <string_view>

void journal(std::string_view message, std::source_location loc = std::source_location::current()) {
    std::cout << loc.file_name() << ':' << loc.line() << " (" << loc.function_name() << ") : " << message << '\n';
}
```

### 24.7 `static_assert` et `assert`

- `static_assert(cond, "message")` vérifie une condition **à la compilation** (le message est facultatif depuis C++17).
- `assert(cond)` (`<cassert>`) vérifie **à l'exécution** et arrête le programme si elle est fausse ; elle **disparaît** avec `-DNDEBUG`. Ne mettez jamais d'effet de bord dans un `assert`.

```cpp
#include <cassert>

static_assert(sizeof(int) >= 4, "int doit faire au moins 4 octets");

int main() {
    int x = 5;
    assert(x > 0 && "x doit être positif");
}
```

### 24.8 Modules *(C++20)*

Les **modules** remplacent l'inclusion textuelle d'en-têtes : une unité est compilée **une seule fois**, puis **importée**. Gains : compilation plus rapide, aucune macro qui « fuit » d'un fichier à l'autre, plus de gardes d'inclusion, ordre des `import` sans importance.

```cpp
// maths.cppm : interface du module
export module maths;

export int carre(int x) { return x * x; }          // exporté : visible des importateurs

export namespace geo {
    double aire_disque(double r);
}

int interne() { return 1; }                        // non exporté : privé au module
```

```cpp
// main.cpp
import maths;
import std;                                        // toute la bibliothèque standard d'un coup (C++23)

int main() {
    std::println("{}", carre(7));
}
```

Comparaison : un en-tête est du **texte recopié** dans chaque fichier, ses macros se propagent et il exige des gardes ; un module est une **interface compilée**, ses macros sont **isolées**. En contrepartie, le support dépend du compilateur **et** du système de build (CMake 3.28+ avec Ninja, par exemple). Pour un projet destiné à être très portable, les en-têtes restent le choix par défaut ; vérifiez la prise en charge de votre chaîne d'outils avant de migrer.

### À retenir (chapitre 24)

- Le préprocesseur manipule du texte : préférez `constexpr`, `inline` et les templates aux macros.
- Gardes d'inclusion (`#pragma once`) pour tout en-tête ; `__has_include` et macros `__cpp_*` pour la portabilité.
- `static_assert` (compilation), `assert` (exécution) ; modules : `import` à la place de `#include`.

---

## Chapitre 25 — Opérateurs bit à bit

### 25.1 Les opérateurs

Un entier est stocké comme une suite de **bits**. Les opérateurs bit à bit agissent sur chaque bit individuellement :

- **`&` (ET)** : 1 si les deux bits valent 1 — `0b1100 & 0b1010 = 0b1000` ;
- **`|` (OU)** : 1 si l'un des bits vaut 1 — `0b1100 | 0b1010 = 0b1110` ;
- **`^` (OU exclusif)** : 1 si les bits diffèrent — `0b1100 ^ 0b1010 = 0b0110` ;
- **`~` (NON)** : inverse tous les bits ;
- **`<<`** : décalage à gauche (insère des zéros à droite) — `0b0011 << 2 = 0b1100` ;
- **`>>`** : décalage à droite — `0b1100 >> 2 = 0b0011`.

```cpp
#include <bitset>
#include <cstdint>
#include <iostream>

int main() {
    std::uint8_t a = 0b1100, b = 0b1010;
    std::cout << std::bitset<8>(a & b) << '\n';                          // 00001000
    std::cout << std::bitset<8>(a | b) << '\n';                          // 00001110
    std::cout << std::bitset<8>(a ^ b) << '\n';                          // 00000110
    std::cout << std::bitset<8>(static_cast<std::uint8_t>(~a)) << '\n';  // 11110011
    std::cout << std::bitset<8>(a << 2) << ' ' << std::bitset<8>(a >> 2) << '\n';   // 00110000 00000011
}
```

**Ne confondez pas** `&` (ET bit à bit) et `&&` (ET logique), ni `|` et `||`.

### 25.2 Masques et drapeaux

Un **drapeau** (*flag*) est un bit représentant un état ; un **masque** est une valeur dont les bits sélectionnent des drapeaux.

```cpp
#include <cstdint>
#include <iostream>

constexpr std::uint8_t LECTURE = 1u << 0;
constexpr std::uint8_t ECRITURE = 1u << 1;
constexpr std::uint8_t EXECUTION = 1u << 2;

int main() {
    std::uint8_t droits = 0;
    droits |= LECTURE | ECRITURE;                       // activer des bits
    droits &= static_cast<std::uint8_t>(~ECRITURE);     // désactiver un bit
    droits ^= EXECUTION;                                // inverser un bit
    bool peut_lire = (droits & LECTURE) != 0;           // tester un bit
    std::cout << static_cast<int>(droits) << ' ' << peut_lire << '\n';   // 5 1
}
```

Les quatre opérations à connaître : **mettre à 1** `x |= masque` ; **mettre à 0** `x &= ~masque` ; **inverser** `x ^= masque` ; **tester** `(x & masque) != 0`.

### 25.3 Décalages

`x << n` multiplie par 2ⁿ ; `x >> n` divise par 2ⁿ (pour les entiers non signés ou positifs). Depuis C++20, le décalage à droite d'un entier signé négatif est un **décalage arithmétique** (le bit de signe est propagé) : `-8 >> 1` vaut `-4`.

**Piège** : décaler d'un nombre de bits **négatif ou supérieur ou égal à la largeur du type** est un comportement indéfini (`1 << 40` sur un `int` de 32 bits). Avant C++20, certains décalages d'entiers signés étaient dépendants de l'implémentation.

### 25.4 Afficher en binaire

```cpp
unsigned x = 37;
std::cout << std::bitset<8>(x) << '\n';                          // 00100101
std::cout << std::format("{:08b} {:#x} {:o}", x, x, x) << '\n';   // 00100101 0x25 45
```

### 25.5 Applications courantes

```cpp
#include <bit>
#include <cstdint>
#include <iostream>

int main() {
    int n = 12;
    std::cout << ((n & 1) == 0 ? "pair" : "impair") << '\n';          // test de parité
    std::cout << std::has_single_bit(64u) << '\n';                    // 1 : puissance de 2 (C++20)

    std::uint32_t couleur = 0xFF8040;                                 // extraire les composantes RGB
    std::uint8_t r = (couleur >> 16) & 0xFF;
    std::uint8_t g = (couleur >> 8) & 0xFF;
    std::uint8_t b = couleur & 0xFF;
    std::cout << int(r) << ' ' << int(g) << ' ' << int(b) << '\n';    // 255 128 64
}
```

Autres usages : permissions et options combinables, champs d'un protocole ou d'un format, ensembles d'entiers compacts, compression, cryptographie, hachage, graphiques (composition de couleurs).

### 25.6 L'en-tête `<bit>` *(C++20)*

```cpp
#include <bit>
#include <cstdint>
#include <iostream>

int main() {
    std::uint32_t x = 0b1011'0000;
    std::cout << std::popcount(x) << '\n';           // 3 : nombre de bits à 1
    std::cout << std::countl_zero(x) << '\n';        // 24 : zéros de poids fort
    std::cout << std::countr_zero(x) << '\n';        // 4 : zéros de poids faible
    std::cout << std::bit_width(x) << '\n';          // 8 : nombre de bits significatifs
    std::cout << std::bit_ceil(37u) << '\n';         // 64 : plus petite puissance de 2 >= 37
    std::cout << std::rotl(x, 4) << '\n';            // rotation à gauche

    float f = 1.0f;
    auto bits = std::bit_cast<std::uint32_t>(f);     // réinterprétation sûre : 0x3f800000
    std::cout << std::hex << bits << '\n';

    if constexpr (std::endian::native == std::endian::little) std::cout << "\nlittle endian\n";
}
```

`std::endian` indique l'**ordre des octets** de la machine : *little endian* (octet de poids faible en premier, x86 et ARM courants) ou *big endian* (réseau). Cela compte dès qu'on lit ou écrit des entiers multioctets dans un fichier ou un protocole.

### 25.7 `std::bitset`

```cpp
std::bitset<8> b("00101100");
b.set(0);                 // met le bit 0 à 1
b.reset(2);               // met le bit 2 à 0
b.flip(7);                // inverse le bit 7
std::cout << b << ' ' << b.count() << ' ' << b.test(3) << ' ' << b.to_ulong() << '\n';
```

`std::bitset<N>` est un tableau de `N` bits de taille fixe, avec `set`, `reset`, `flip`, `test`, `count`, `all`, `any`, `none`, les opérateurs bit à bit, et des conversions vers entier ou chaîne.

### 25.8 Précautions

- Travaillez sur des types **non signés** à taille fixe (`std::uint8_t`, `std::uint32_t`).
- Les petits types sont **promus en `int`** dans les expressions : `~b` sur un `uint8_t` donne un `int` négatif ; castez le résultat.
- **Priorité** : `==` l'emporte sur `&` ; écrivez `(x & 1) == 0` et non `x & 1 == 0`.
- Ne décalez jamais de plus que la largeur du type.
- Préférez `std::bitset` et `<bit>` aux manipulations « maison ».

### À retenir (chapitre 25)

- Quatre gestes : activer (`|=`), désactiver (`&= ~`), inverser (`^=`), tester (`&`).
- Décalages : valides jusqu'à la largeur du type ; types non signés de préférence.
- `<bit>` et `std::bitset` rendent le code lisible et portable.

---

## Chapitre 26 — Récursivité

### 26.1 Principe

Une fonction est **récursive** quand elle s'appelle elle-même. Toute fonction récursive correcte comporte :

1. un **cas de base** : une situation simple traitée directement, qui arrête la récursion ;
2. un **appel récursif** sur un problème **strictement plus petit**, qui se rapproche du cas de base.

```cpp
#include <iostream>

long long factorielle(int n) {
    if (n <= 1) return 1;                    // cas de base
    return n * factorielle(n - 1);           // appel récursif sur un problème plus petit
}

int main() { std::cout << factorielle(5) << '\n'; }      // 120
```

Pour raisonner, on fait un **acte de foi** : on suppose que l'appel récursif résout correctement le sous-problème, et l'on vérifie que (a) le cas de base est juste et (b) l'étape combine correctement le résultat. C'est une démonstration par récurrence.

### 26.2 Exemples classiques

```cpp
#include <iostream>

int pgcd(int a, int b) { return b == 0 ? a : pgcd(b, a % b); }        // algorithme d'Euclide (voir aussi std::gcd)

long long puissance(long long base, unsigned exp) {                    // exponentiation rapide : O(log exp)
    if (exp == 0) return 1;
    long long m = puissance(base, exp / 2);
    return (exp % 2 == 0) ? m * m : m * m * base;
}

int somme_chiffres(int n) { return n < 10 ? n : n % 10 + somme_chiffres(n / 10); }

void hanoi(int n, char de, char vers, char via) {                      // tours de Hanoï
    if (n == 0) return;
    hanoi(n - 1, de, via, vers);
    std::cout << "disque " << n << " : " << de << " -> " << vers << '\n';
    hanoi(n - 1, via, vers, de);
}

int main() {
    std::cout << pgcd(48, 18) << ' ' << puissance(2, 10) << ' ' << somme_chiffres(1234) << '\n';   // 6 1024 10
    hanoi(2, 'A', 'C', 'B');
}
```

La récursivité excelle pour les structures **elles-mêmes récursives** : arbres, parcours de graphes, expressions, fichiers imbriqués, ainsi que les algorithmes « **diviser pour régner** » (tri fusion, tri rapide, recherche dichotomique).

### 26.3 Pile d'appels et profondeur

Chaque appel consomme un **cadre de pile** (paramètres, variables locales, adresse de retour). Une récursion trop profonde, ou sans cas de base atteignable, provoque un **dépassement de pile** (*stack overflow*) et un plantage.

```cpp
// long long infinie(long long n) { return infinie(n + 1); }      // pas de cas de base : plantage garanti
```

Le C++ **ne garantit pas** l'optimisation de la **récursion terminale** (*tail call*) : un compilateur peut la réaliser avec `-O2`, mais on ne peut pas s'y fier. Pour de grandes profondeurs, transformez en **boucle** (éventuellement avec une pile explicite `std::stack`) :

```cpp
long long factorielle_iter(int n) {
    long long r = 1;
    for (int i = 2; i <= n; ++i) r *= i;
    return r;
}
```

### 26.4 Récursivité et évaluation à la compilation

```cpp
constexpr long long fact(int n) { return n <= 1 ? 1 : n * fact(n - 1); }
static_assert(fact(10) == 3628800);                  // calculé et vérifié par le compilateur
constexpr long long f20 = fact(20);                  // 2432902008176640000, sans calcul à l'exécution
```

### 26.5 Mémoïsation

Fibonacci naïf recalcule les mêmes sous-problèmes un nombre exponentiel de fois. La **mémoïsation** mémorise les résultats déjà calculés :

```cpp
#include <iostream>
#include <unordered_map>

long long fib_naif(int n) { return n < 2 ? n : fib_naif(n - 1) + fib_naif(n - 2); }          // O(2^n) : très lent

long long fib_memo(int n, std::unordered_map<int, long long> &cache) {
    if (n < 2) return n;
    if (auto it = cache.find(n); it != cache.end()) return it->second;
    long long r = fib_memo(n - 1, cache) + fib_memo(n - 2, cache);
    cache[n] = r;
    return r;
}

int main() {
    std::unordered_map<int, long long> cache;
    std::cout << fib_naif(20) << ' ' << fib_memo(80, cache) << '\n';       // 6765 23416728348467685
}
```

### 26.6 Lambdas récursives *(C++23)*

Avec *deducing this*, une lambda peut s'appeler elle-même :

```cpp
auto fib = [](this auto self, int n) -> long long {
    return n < 2 ? n : self(n - 1) + self(n - 2);
};
std::cout << fib(15) << '\n';        // 610
```

Avant C++23, on utilise `std::function` (avec un surcoût) ou une fonction ordinaire.

### 26.7 Récursivité ou itération ?

- **Lisibilité** : récursivité excellente pour arbres et diviser pour régner ; itération pour les répétitions simples.
- **Mémoire** : récursivité = une trame de pile par appel ; itération = mémoire constante.
- **Performance** : coût des appels en récursivité ; généralement meilleure en itération.
- **Risque** : dépassement de pile pour l'une, boucle infinie pour l'autre.

Erreurs fréquentes : oubli du cas de base ; appel récursif qui ne progresse pas vers lui ; débordement de l'entier du résultat (`factorielle(25)` dépasse `long long`) ; recalculs inutiles (mémoïsation).

### À retenir (chapitre 26)

- Cas de base + appel sur un problème plus petit ; vérifiez la terminaison.
- La pile est limitée : récursion profonde → boucle ; récursion terminale non garantie.
- `constexpr` + récursion = calculs à la compilation ; mémoïsation contre l'explosion exponentielle.

---

## Chapitre 27 — Unicode et encodages de caractères

### 27.1 Le problème

Un ordinateur ne stocke que des nombres : afficher un texte suppose une convention qui associe des nombres à des caractères. Le C++ a longtemps ignoré le sujet : `char` désigne un **octet**, pas un « caractère ». Un texte moderne (accents, alphabets non latins, idéogrammes, emojis) exige de distinguer plusieurs notions.

- **Jeu de caractères** (*character set*) : liste de caractères, chacun associé à un **point de code** (nombre). **Unicode** en est le jeu universel : plus de 150 000 caractères, points de code de `U+0000` à `U+10FFFF`.
- **Encodage** (*encoding*) : manière de représenter ces points de code **en octets**. **UTF-8**, **UTF-16** et **UTF-32** sont trois encodages d'Unicode.
- **ASCII** : jeu historique de 128 caractères (7 bits), identique aux 128 premiers points de code d'Unicode.
- **Pages de code** (Latin-1/ISO 8859-1, Windows-1252, CP437…) : anciens encodages sur un octet, incompatibles entre eux.

### 27.2 Les encodages Unicode

- **UTF-8** : encodage à **longueur variable**, de **1 à 4 octets** par point de code. Les caractères ASCII tiennent sur 1 octet (compatibilité totale), `é` sur 2 (`C3 A9`), `€` sur 3 (`E2 82 AC`), un emoji sur 4. Aucun problème d'ordre des octets, sûr dans les chaînes C (aucun octet nul au milieu). **C'est l'encodage à privilégier** : standard du Web, des fichiers, des API Linux et macOS.
- **UTF-16** : unités de **16 bits** ; un point de code occupe 1 unité (plan de base) ou 2 (**paire de substitution**) pour les caractères supplémentaires. Utilisé en interne par Windows, Java, JavaScript, Qt.
- **UTF-32** : **une unité de 32 bits par point de code**, longueur fixe ; simple mais gourmand en mémoire.

**Boutisme et BOM** : UTF-16 et UTF-32 dépendent de l'ordre des octets (*endianness*) ; une marque d'ordre d'octets (BOM, `U+FEFF`) peut ouvrir un fichier pour l'indiquer. Un BOM UTF-8 est inutile et souvent gênant.

### 27.3 Les types de caractères du C++

- **`char`** : un octet (au moins 8 bits). Contient un caractère ASCII, ou **un octet d'une séquence UTF-8**. Signé ou non selon la plateforme.
- **`char8_t`** *(C++20)* : unité UTF-8 ; littéraux `u8"…"` ; chaîne `std::u8string`.
- **`char16_t`** *(C++11)* : unité UTF-16 ; littéraux `u"…"` ; chaîne `std::u16string`.
- **`char32_t`** *(C++11)* : point de code UTF-32 ; littéraux `U"…"` ; chaîne `std::u32string`.
- **`wchar_t`** : « caractère large » dont la taille dépend du système (16 bits sous Windows, 32 bits sous Linux et macOS) ; littéraux `L"…"` ; chaîne `std::wstring`. **Non portable** : à réserver à l'API Windows.

```cpp
#include <iostream>
#include <string>

int main() {
    std::string  a = "é";            // encodage d'exécution (en pratique UTF-8 sur Linux/macOS/MSVC avec /utf-8)
    std::u8string b = u8"é";         // UTF-8 garanti : 2 unités
    std::u16string c = u"é";         // UTF-16 : 1 unité
    std::u32string d = U"é";         // UTF-32 : 1 unité
    std::u8string emoji = u8"😀";    // 4 unités UTF-8

    std::cout << a.size() << ' ' << b.size() << ' ' << c.size() << ' ' << d.size() << ' ' << emoji.size() << '\n';   // 2 2 1 1 4
}
```

Point essentiel : **`size()` d'une `std::string` compte des octets, pas des caractères.** `"é"` fait 2 octets, `"😀"` en fait 4. Avec `std::u16string`, un emoji compte pour 2 unités.

### 27.4 Ce qu'est un « caractère »

Au-dessus du point de code se cache une difficulté : ce que l'utilisateur perçoit comme **un** caractère (un **graphème**) peut comporter **plusieurs** points de code.

- `é` peut s'écrire `U+00E9` (précomposé, un point de code) **ou** `e` + `U+0301` (accent combinant, deux points de code) : les deux s'affichent pareil mais ne sont **pas égaux** octet par octet. La **normalisation** (NFC, NFD, NFKC, NFKD) permet de les rendre comparables.
- Un drapeau, un emoji avec teinte de peau ou une famille est une **séquence** de plusieurs points de code assemblés par des « joiners ».
- **Casse** : `toupper` octet par octet est faux en Unicode (`ß` devient `SS`, `i` turc donne `İ`) ; le tri alphabétique dépend de la **langue** (collation).

Trois « longueurs » différentes pour un même texte : le nombre d'**octets** (`size()` d'une `std::string`), de **points de code** (à compter en décodant l'UTF-8) et de **graphèmes** (ce que voit l'utilisateur).

### 27.5 Parcourir et décoder de l'UTF-8

La bibliothèque standard n'offre pas (encore) de décodage Unicode complet, mais l'UTF-8 se prête à un parcours simple : les octets de continuation ont la forme `10xxxxxx`.

```cpp
#include <iostream>
#include <string>
#include <string_view>

std::size_t compter_points_de_code(std::string_view utf8) {
    std::size_t n = 0;
    for (unsigned char c : utf8) {
        if ((c & 0xC0) != 0x80) ++n;          // on ignore les octets de continuation (10xxxxxx)
    }
    return n;
}

int main() {
    std::string s = "caf\u00e9 \u20ac";       // « café € » écrit avec des échappements \u (indépendants de l'éditeur)
    std::cout << s.size() << " octets, " << compter_points_de_code(s) << " points de code\n";   // 9 octets, 6 points
}
```

Pour un traitement sérieux (graphèmes, normalisation, casse, collation, conversion, validation), utilisez une bibliothèque : **ICU**, **Boost.Text**, **utf8cpp**, **libunistring** ou la bibliothèque du framework (Qt, Poco). **N'écrivez pas** vos propres tables Unicode.

### 27.6 Entrées, sorties et encodages

- Le texte qu'affiche ou lit un programme passe par le **terminal** ou le **fichier**, dont l'encodage doit correspondre à celui du programme. Un décalage donne le fameux « mojibake » (`Ã©` au lieu de `é`).
- **Linux et macOS** : terminal et API en UTF-8 par défaut ; tout est simple.
- **Windows** : l'API historique utilise des pages de code ou l'UTF-16 (`wchar_t`). Il faut basculer la console en UTF-8 (`chcp 65001` ou `SetConsoleOutputCP(CP_UTF8)`) et compiler avec `/utf-8` (MSVC). `std::print` *(C++23)* gère correctement l'Unicode en sortie sur un terminal.
- **Fichiers** : écrivez et lisez en **UTF-8**. Le texte d'un fichier ouvert en mode texte n'est pas converti par `std::ifstream` : les octets arrivent tels quels dans la `std::string`.

```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    {
        std::ofstream out("texte.txt", std::ios::binary);      // binaire : aucune traduction de fins de ligne
        out << "Café – 北京 – 😀\n";                            // le source doit être enregistré en UTF-8
    }
    std::ifstream in("texte.txt", std::ios::binary);
    std::string ligne;
    std::getline(in, ligne);
    std::cout << ligne << " (" << ligne.size() << " octets)\n";
}
```

Options de compilation liées à l'encodage : **GCC/Clang** `-finput-charset=UTF-8 -fexec-charset=UTF-8` (valeurs par défaut sur les systèmes UTF-8) ; **MSVC** `/utf-8` (ou `/source-charset:utf-8 /execution-charset:utf-8`). Pour qu'un source reste indépendant de l'éditeur, on peut écrire les caractères non ASCII en **échappements** : `\u00e9` (4 chiffres hexadécimaux), `\U0001F600` (8 chiffres), `\x..` (octet).

### 27.7 Conversions entre encodages

Les facettes de `<codecvt>` et `std::wstring_convert` sont **dépréciées depuis C++17** : ne les utilisez plus. Options :

- les fonctions **de l'API du système** (`MultiByteToWideChar` / `WideCharToMultiByte` sous Windows ; `iconv` sous POSIX) ;
- les bibliothèques (ICU, utfcpp) ;
- **`std::text_encoding`** *(C++26)* identifie l'encodage d'exécution ou de la locale (`std::text_encoding::environment()`) ;
- `std::format` et `std::print` *(C++20/23)* acceptent l'Unicode : `std::format("{}", u8_chaine)` n'est cependant **pas** défini pour `char8_t` — convertissez d'abord vers `char` si nécessaire.

### 27.8 Pièges fréquents

- Croire que `s.size()` ou `s[i]` désignent des **caractères** : ils désignent des **octets**. Découper une `std::string` UTF-8 au milieu d'un caractère produit une séquence invalide.
- `std::toupper(c)` / `std::isalpha(c)` : ASCII seulement.
- Comparer des chaînes sans normalisation ; trier avec `<` (ordre des octets, pas l'ordre alphabétique d'une langue).
- Utiliser `wchar_t` en pensant à la portabilité (la taille change).
- Mélanger les encodages dans un même flux ; oublier de déclarer l'encodage d'un fichier.
- `std::cout << u8"…"` (C++20 : `char8_t` n'est pas affichable directement) : convertissez en `char`.

### 27.9 Recommandations

- Utilisez **UTF-8 partout** à l'intérieur du programme et dans les fichiers ; convertissez **aux frontières** (API Windows, bibliothèques UTF-16).
- Stockez dans `std::string` (UTF-8), passez en `std::string_view`.
- Pour l'affichage et la mise en forme, `std::format` / `std::print`.
- Traitez le texte **sémantique** (casse, tri, longueur visible) avec ICU ou équivalent.
- Écrivez vos sources en UTF-8 sans BOM et compilez avec l'option d'encodage explicite.

### À retenir (chapitre 27)

- Octets ≠ points de code ≠ graphèmes ; `std::string::size()` compte des octets.
- UTF-8 partout, conversion aux frontières ; `wchar_t` n'est pas portable.
- Les fonctions `<cctype>` et les comparaisons octet à octet sont insuffisantes pour Unicode ; utilisez ICU.

---

## Chapitre 28 — Compilation, outils et construction de projets

### 28.1 Les compilateurs

Trois grandes familles :

- **GCC** (`g++`) : le compilateur de GNU, très répandu sous Linux ;
- **Clang** (`clang++`) : issu du projet LLVM, avec d'excellents messages d'erreur et outils d'analyse ;
- **MSVC** (`cl`) : le compilateur de Microsoft, intégré à Visual Studio.

Ils diffèrent par leurs options mais pas par le langage standard. Testez votre code avec **au moins deux** compilateurs : cela révèle du code non portable ou des comportements indéfinis.

### 28.2 Compiler en une ou plusieurs étapes

```bash
# En une seule commande
g++ -std=c++20 -Wall -Wextra main.cpp maths.cpp -o prog

# En plusieurs étapes (compilation séparée)
g++ -std=c++20 -Wall -Wextra -c main.cpp -o main.o      # -c : compiler sans lier
g++ -std=c++20 -Wall -Wextra -c maths.cpp -o maths.o
g++ main.o maths.o -o prog                             # édition de liens
```

La compilation séparée accélère les reconstructions : seuls les fichiers modifiés (et ceux qui incluent un en-tête modifié) sont recompilés. Les erreurs se répartissent en deux familles : erreurs de **compilation** (syntaxe, types, noms inconnus) et erreurs d'**édition de liens** (`undefined reference to …` : définition manquante ; `multiple definition of …` : définition présente plusieurs fois, ODR violée).

### 28.3 Options essentielles (GCC / Clang)

- **Norme** : `-std=c++17`, `-std=c++20`, `-std=c++23`, `-std=c++2c` (C++26).
- **Avertissements** : `-Wall -Wextra -Wpedantic` (toujours) ; `-Wshadow -Wconversion -Wold-style-cast -Wnon-virtual-dtor -Woverloaded-virtual` (très utiles) ; `-Werror` (transforme les avertissements en erreurs, pour l'intégration continue).
- **Optimisation** : `-O0` (aucune, débogage), `-O1`, `-O2` (recommandé en production), `-O3` (agressive), `-Os` (taille), `-Og` (débogage optimisé), `-flto` (optimisation à l'édition de liens), `-march=native` (jeu d'instructions de la machine ; non portable).
- **Débogage** : `-g` (symboles de débogage), `-ggdb3`.
- **Désinfectants** (*sanitizers*) : `-fsanitize=address` (erreurs mémoire), `-fsanitize=undefined` (comportements indéfinis), `-fsanitize=thread` (data races), `-fsanitize=leak`. Compilez et testez **régulièrement** avec eux.
- **Préprocesseur** : `-DNOM=valeur` (définit une macro), `-DNDEBUG` (désactive `assert`), `-Idossier` (dossier d'en-têtes), `-E` (s'arrête après le préprocesseur).
- **Édition de liens** : `-Ldossier` (dossier de bibliothèques), `-lnom` (lie `libnom`), `-pthread` (threads), `-static` (liaison statique).

Équivalents **MSVC** : `/std:c++20`, `/W4` (avertissements), `/WX` (erreurs), `/O2`, `/Zi` (débogage), `/utf-8`, `/EHsc` (exceptions), `/fsanitize=address`, `/D` (macros), `/I` (en-têtes).

Profils recommandés :

```bash
# Développement : lent mais sûr, messages exploitables
g++ -std=c++20 -g -O0 -Wall -Wextra -Wpedantic -Wshadow -Wconversion -fsanitize=address,undefined main.cpp -o prog

# Production : rapide
g++ -std=c++20 -O2 -DNDEBUG -Wall -Wextra main.cpp -o prog
```

### 28.4 Bibliothèques : statiques et dynamiques

Une **bibliothèque** regroupe du code compilé réutilisable.

- **Statique** (`.a` sous Linux, `.lib` sous Windows) : copiée **dans** l'exécutable à l'édition de liens ; exécutable autonome mais plus gros.
- **Dynamique / partagée** (`.so`, `.dylib`, `.dll`) : chargée **à l'exécution** ; partagée entre programmes, mise à jour indépendante, mais dépend de l'environnement (`LD_LIBRARY_PATH`, `PATH`).

```bash
g++ -c -fPIC maths.cpp -o maths.o                      # code indépendant de la position
ar rcs libmaths.a maths.o                              # bibliothèque statique
g++ -shared maths.o -o libmaths.so                     # bibliothèque dynamique
g++ main.cpp -L. -lmaths -o prog                       # lie avec libmaths
```

L'**interface binaire** (ABI) du C++ n'est pas standardisée : mélanger des bibliothèques compilées par des compilateurs ou versions différents, ou avec des options incompatibles (`_GLIBCXX_USE_CXX11_ABI`), mène à des erreurs de liaison ou à des plantages. Une interface `extern "C"` offre une ABI stable.

### 28.5 `make` et CMake

À partir de quelques fichiers, on automatise la construction. **`make`** lit un `Makefile` qui décrit des cibles, leurs dépendances et les commandes :

```makefile
CXX      := g++
CXXFLAGS := -std=c++20 -Wall -Wextra -O2

prog: main.o maths.o
	$(CXX) $^ -o $@

%.o: %.cpp maths.hpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f *.o prog
```

Les retraits de commande sont des **tabulations**. `make` ne recompile que ce qui a changé.

Pour les projets réels et multiplateformes, **CMake** est devenu l'outil de référence : il **génère** les fichiers de construction (Makefile, Ninja, projet Visual Studio) pour chaque plateforme.

```cmake
cmake_minimum_required(VERSION 3.20)
project(MonProjet VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)                         # -std=c++20 et non gnu++20

add_library(maths src/maths.cpp)
target_include_directories(maths PUBLIC include)

add_executable(prog src/main.cpp)
target_link_libraries(prog PRIVATE maths)

if(MSVC)
  target_compile_options(prog PRIVATE /W4)
else()
  target_compile_options(prog PRIVATE -Wall -Wextra -Wpedantic)
endif()

enable_testing()
add_subdirectory(tests)
```

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release        # configure
cmake --build build -j                                # compile en parallèle
ctest --test-dir build                                # lance les tests
```

Principe moderne : tout passe par des **cibles** (`target_*`) avec leurs visibilités `PUBLIC` / `PRIVATE` / `INTERFACE`, plutôt que par des variables globales.

### 28.6 Organisation d'un projet

```text
projet/
├── CMakeLists.txt
├── include/projet/    # en-têtes publics
├── src/               # implémentations et en-têtes privés
├── tests/
├── cmake/ ou extern/  # dépendances
└── README.md
```

Règles d'or pour les en-têtes : gardes d'inclusion (`#pragma once`) ; **autonomes** (compilables seuls, avec leurs propres `#include`) ; **déclarations anticipées** (`class Foo;`) plutôt que `#include` quand une référence ou un pointeur suffit ; aucun `using namespace` ; pas de définition de fonction ordinaire (sauf `inline` / `constexpr` / template). **Pimpl** (*pointer to implementation*) cache les détails d'une classe dans le `.cpp` pour réduire les dépendances de compilation.

### 28.7 Gestion des dépendances

C++ n'a pas de gestionnaire de paquets officiel ; les principaux sont :

- **vcpkg** (Microsoft) et **Conan** : gestionnaires de paquets multiplateformes, bien intégrés à CMake ;
- **CMake FetchContent** : télécharge et construit une dépendance depuis son dépôt Git ;
- gestionnaires du système (`apt`, `brew`, `pacman`) et sous-modules Git.

Bibliothèques incontournables : **Boost** (utilitaires et bases de nombreuses fonctionnalités du standard), **fmt** (ancêtre de `std::format`), **Eigen** (algèbre linéaire), **nlohmann/json**, **spdlog** (journalisation), **Catch2** / **GoogleTest** (tests), **Qt** (interfaces graphiques), **Asio** (réseau), **Abseil**, **Poco**.

### 28.8 Tests, analyse, formatage, débogage

- **Tests unitaires** : GoogleTest, Catch2, doctest. Un test = un comportement attendu, automatisé, relancé à chaque modification.

```cpp
#include <catch2/catch_test_macros.hpp>

int carre(int x) { return x * x; }

TEST_CASE("carre") {
    REQUIRE(carre(3) == 9);
    REQUIRE(carre(-2) == 4);
    REQUIRE(carre(0) == 0);
}
```

- **Analyse statique** : `clang-tidy` (règles modernisation, performance, lisibilité, C++ Core Guidelines), `cppcheck`, l'analyseur de GCC (`-fanalyzer`), `/analyze` de MSVC.
- **Formatage** : `clang-format` avec un fichier `.clang-format` : un style unique pour toute l'équipe.
- **Débogueurs** : **gdb**, **lldb**, ou celui de Visual Studio / VS Code. Points d'arrêt (`break fichier:ligne`), exécution pas à pas (`next`, `step`), inspection (`print`, `backtrace`), points d'arrêt conditionnels, *watchpoints*. Compilez avec `-g -O0`.
- **Mémoire** : Valgrind (`--leak-check=full`), AddressSanitizer.
- **Performance** : `perf`, gprof, Valgrind/Callgrind, VTune, profileurs de Visual Studio ; **mesurez avant d'optimiser** (benchmarks : Google Benchmark).
- **Couverture de code** : `--coverage` (GCC) puis `gcov` / `lcov`.
- **Intégration continue** : compilez et testez à chaque commit, sur plusieurs compilateurs et plateformes, en modes Debug et Release, avec sanitizers.

### 28.9 Lire les erreurs du compilateur

Les messages C++ (surtout avec des templates) sont longs. Méthode :

1. **Lisez la première erreur**, pas la dernière : les suivantes en sont souvent des conséquences.
2. Repérez le **fichier et la ligne** ; regardez aussi la ligne **précédente** (point-virgule oublié).
3. Pour une erreur de template, cherchez la ligne « *required from here* » : c'est **votre** code qui déclenche l'instanciation.
4. Isolez le problème dans un petit exemple minimal.
5. Essayez un **autre compilateur** (Clang est souvent plus clair) ou un outil comme Compiler Explorer (godbolt.org) pour voir l'assembleur et comparer les compilateurs.

### À retenir (chapitre 28)

- Compilez toujours avec `-std=…`, `-Wall -Wextra`, et des sanitizers en développement.
- Compilation séparée + édition de liens ; CMake pour construire proprement ; bibliothèques statiques ou dynamiques.
- Tests automatisés, `clang-tidy`, `clang-format`, intégration continue.

---

## Chapitre 29 — Comportements indéfinis, erreurs et sûreté

### 29.1 Les catégories de comportement

La norme C++ décrit ce que fait un programme **correct**. Pour un programme qui enfreint les règles, elle distingue :

- **Comportement défini** : résultat entièrement spécifié par la norme.
- **Comportement spécifié par l'implémentation** (*implementation-defined*) : le compilateur choisit parmi plusieurs possibilités et **doit documenter** son choix (taille de `int`, signe de `char`, encodage d'exécution).
- **Comportement non spécifié** (*unspecified*) : plusieurs résultats valides, sans obligation de documenter (ordre d'évaluation des arguments d'une fonction).
- **Comportement indéfini** (*undefined behavior*, **UB**) : la norme **n'impose aucune exigence** au programme *tout entier*. Il peut planter, produire un résultat plausible, effacer des données, ou fonctionner « normalement » jusqu'à l'arrivée d'une autre version du compilateur.
- **Programme mal formé** : erreur détectée à la compilation (diagnostic obligatoire dans la plupart des cas).

Depuis **C++26**, la lecture d'une variable locale non initialisée n'est plus un UB mais un **comportement erroné** (*erroneous behavior*) : le compilateur initialise la valeur avec un motif prédéfini et peut signaler l'erreur ; l'attribut `[[indeterminate]]` permet de demander l'ancien comportement pour des raisons de performance.

### 29.2 Pourquoi l'UB existe, et pourquoi il est dangereux

L'UB permet au compilateur de **supposer qu'il n'arrive jamais**, et de produire du code rapide sans tests superflus. Conséquence : un compilateur peut **supprimer** un test, réorganiser du code ou rendre « atteignable » du code qui ne devrait pas l'être.

```cpp
int f(int x) {
    if (x + 1 > x) return 1;       // pour un int signé, le débordement est un UB :
    return 0;                      // le compilateur peut remplacer tout cela par « return 1; »
}
```

Ce n'est pas une erreur du compilateur : le programmeur a rompu le contrat. L'UB est aussi la **première source de failles de sécurité** (dépassements de tampon, utilisation après libération).

### 29.3 Catalogue des comportements indéfinis courants

**Mémoire et durée de vie**

- Déréférencer un pointeur nul, non initialisé ou pendant (objet détruit).
- Accès **hors bornes** à un tableau, un `std::vector` (avec `[]`), un `std::string`, un `std::span`.
- **Utilisation après libération** (*use-after-free*), **double libération**, mauvaise paire `new` / `delete[]`.
- Utiliser un **itérateur invalidé** (après `push_back`, `erase`, `insert`, réallocation).
- Retourner ou conserver une référence ou un pointeur vers une variable locale ; vue (`string_view`, `span`) sur un objet détruit.
- Accéder à un objet **non encore construit** ou déjà détruit.

**Arithmétique**

- **Débordement d'un entier signé** (`INT_MAX + 1`).
- **Division ou modulo entier par zéro** ; `INT_MIN / -1`.
- **Décalage** par un nombre de bits négatif ou supérieur ou égal à la largeur.
- Conversion d'un flottant en entier lorsque la valeur n'est pas représentable.

**Types et expressions**

- Violation de l'**alias strict** (lire un `float` via un `int *`) ; `reinterpret_cast` fautif.
- **Modification multiple** d'un même objet sans séquencement (`i = i++ + ++i` avant C++17).
- `static_cast` vers un type dérivé incompatible ; `dynamic_cast` sur un objet non polymorphe (erreur de compilation) ou mal utilisé.
- Fonction non `void` qui **atteint sa fin sans `return`**.
- `delete` d'un objet dérivé via un pointeur de base **sans destructeur virtuel**.

**Concurrence**

- **Course aux données** (*data race*) : deux fils accèdent à la même variable, l'un au moins en écriture, sans synchronisation.
- Verrouiller deux fois un mutex non récursif ; détruire un `std::thread` encore joignable (`std::terminate`).

**Divers**

- Violation de l'**ODR** (définitions différentes d'une même entité dans plusieurs unités).
- Modifier un objet `const` via `const_cast` ; modifier un littéral de chaîne.
- Construire une `std::string` depuis `nullptr`.

```cpp
#include <vector>

int main() {
    std::vector<int> v{1, 2, 3};
    int &premier = v[0];
    v.push_back(4);                  // peut réallouer : « premier » devient pendante
    // premier = 10;                 // UB : référence invalidée

    int t[3] = {};
    // t[3] = 1;                     // UB : hors bornes, même si « ça marche »
}
```

### 29.4 Détecter l'UB

- **Avertissements** du compilateur : `-Wall -Wextra -Wconversion -Wshadow -Wnull-dereference -Wuninitialized`.
- **Sanitizers** (à l'exécution) : `-fsanitize=address` (accès invalides, fuites), `-fsanitize=undefined` (débordement signé, décalages, nul, alignement), `-fsanitize=thread` (courses), `-fsanitize=memory` (lecture de mémoire non initialisée, Clang).
- **Analyseurs statiques** : `clang-tidy`, `cppcheck`, `-fanalyzer`, `/analyze`.
- **Valgrind** pour les fuites et lectures non initialisées.
- **Tests aléatoires** (*fuzzing*) : libFuzzer, AFL++ alimentent le programme d'entrées générées pour en dévoiler les failles.
- **Mode durci** de la bibliothèque : GCC `-D_GLIBCXX_ASSERTIONS`, LLVM `-D_LIBCPP_HARDENING_MODE=_LIBCPP_HARDENING_MODE_FAST` (ou `_EXTENSIVE`, `_DEBUG`) ; MSVC `_ITERATOR_DEBUG_LEVEL`. Avec **C++26**, la bibliothèque standard dispose d'un **mode durci** normalisé : les préconditions de `operator[]`, `front()`, `back()`, `span`, `optional`, etc. sont **vérifiées** et le programme s'arrête de façon contrôlée au lieu d'avoir un UB.

### 29.5 Écrire du C++ sûr

- **Pas de `new` / `delete` ni de `malloc` / `free`** à la main : conteneurs et pointeurs intelligents (RAII).
- **Pas de tableaux C ni de pointeurs + taille** : `std::array`, `std::vector`, `std::span`, `std::string`, `std::string_view`.
- **Initialisez** tout ; utilisez `{}`.
- **Accès vérifié** là où la performance le permet : `.at()`, ou mode durci de la bibliothèque.
- **Typez fort** : `enum class`, types métier, `std::chrono` pour les durées plutôt que des `int`.
- **`const` par défaut**, `constexpr` si possible, `[[nodiscard]]`, `override`, `explicit`.
- **Évitez les casts** ; `static_cast` seulement, jamais de cast à la C.
- **Propriété claire** : un propriétaire, des observateurs non propriétaires.
- **Entiers** : `std::cmp_*`, `std::in_range`, `-Wconversion`.
- **Ranges et algorithmes** plutôt que boucles à indices.
- Suivez les **C++ Core Guidelines** (Stroustrup et Sutter) et leur analyseur (`clang-tidy -checks='cppcoreguidelines-*'`) ; la bibliothèque de support **GSL** (`gsl::span`, `gsl::not_null`, `gsl::owner`) les complète.

### 29.6 Gestion des erreurs : quel mécanisme ?

- **Bogue du programmeur** (précondition violée, invariant cassé) : **ne se récupère pas** ; on l'arrête vite avec `assert` / `contract_assert` / contrats. Ce n'est pas le rôle d'une exception.
- **Erreur exceptionnelle et rare** (fichier corrompu, mémoire épuisée) : **exceptions**.
- **Échec ordinaire et attendu** (nombre mal formé, élément introuvable, réseau coupé) : valeur de retour — `std::optional<T>` (absence), `std::expected<T, E>` (résultat ou erreur), `std::error_code`.
- **Frontière du programme** : validez toutes les entrées externes (utilisateur, fichier, réseau).

```cpp
#include <charconv>
#include <expected>      // C++23
#include <iostream>
#include <string_view>
#include <system_error>

enum class ErreurLecture { Vide, Format, Debordement };

std::expected<int, ErreurLecture> lire_entier(std::string_view s) {
    if (s.empty()) return std::unexpected(ErreurLecture::Vide);
    int v{};
    auto [fin, ec] = std::from_chars(s.data(), s.data() + s.size(), v);
    if (ec == std::errc::result_out_of_range) return std::unexpected(ErreurLecture::Debordement);
    if (ec != std::errc{} || fin != s.data() + s.size()) return std::unexpected(ErreurLecture::Format);
    return v;
}

int main() {
    for (std::string_view texte : {"42", "abc", "", "99999999999"}) {
        if (auto r = lire_entier(texte)) std::cout << "valeur : " << *r << '\n';
        else std::cout << "erreur n°" << static_cast<int>(r.error()) << '\n';
    }
}
```

`std::expected` offre aussi des opérations **monadiques** : `transform`, `and_then`, `or_else`, `value_or`.

### 29.7 Les exceptions en profondeur

- **Dérouler la pile** : quand une exception est levée, les destructeurs des objets locaux sont appelés en remontant jusqu'au `catch` ; un destructeur ne doit **jamais** laisser s'échapper une exception (il est `noexcept` par défaut), sinon `std::terminate`.
- **`noexcept`** : spécificateur qui promet qu'aucune exception ne sort ; `noexcept(expr)` est aussi un opérateur d'interrogation. Marquez `noexcept` les destructeurs, les opérations de déplacement et `swap`.
- **Relancer** : `throw;` relance l'exception courante telle quelle ; `std::throw_with_nested` et `std::rethrow_if_nested` chaînent des erreurs.
- **Exceptions personnalisées** : dérivez de `std::exception` (ou `std::runtime_error`).

```cpp
#include <iostream>
#include <stdexcept>
#include <string>

class ErreurConfig : public std::runtime_error {
    int ligne_;
public:
    ErreurConfig(const std::string &msg, int ligne) : std::runtime_error(msg), ligne_(ligne) {}
    int ligne() const noexcept { return ligne_; }
};

void analyser(int ligne) {
    if (ligne == 3) throw ErreurConfig("clé inconnue", ligne);
}

int main() {
    try {
        for (int i = 1; i <= 5; ++i) analyser(i);
    } catch (const ErreurConfig &e) {
        std::cerr << "ligne " << e.ligne() << " : " << e.what() << '\n';
    }
}
```

**Garanties de sûreté face aux exceptions** (à documenter pour chaque opération) :

1. **Aucune garantie** : à proscrire.
2. **Garantie de base** : en cas d'exception, aucune fuite et les invariants sont préservés, mais l'état exact est indéterminé.
3. **Garantie forte** : l'opération réussit **ou** n'a aucun effet (« commit or rollback ») — obtenue par l'idiome **copier puis échanger** (*copy-and-swap*).
4. **Garantie de non-levée** (`noexcept`) : l'opération ne peut pas échouer.

La **RAII** rend les deux premières presque automatiques : si chaque ressource est détenue par un objet, la remontée de pile la libère. Coût : la levée d'une exception est lente (microsecondes) ; l'absence d'exception est quasi gratuite. Certains projets désactivent les exceptions (`-fno-exceptions`) : embarqué, jeux, temps réel.

### 29.8 Contrats *(C++26)*

Les **contrats** permettent d'écrire dans le code, de façon vérifiable, les **préconditions** (ce que l'appelant garantit), les **postconditions** (ce que la fonction garantit) et les **assertions** internes.

```cpp
int racine_entiere(int n)
    pre(n >= 0)                                  // précondition : vérifiée à l'entrée
    post(r : r >= 0 && r * r <= n)               // postcondition : « r » désigne le résultat
{
    int r = 0;
    while ((r + 1) * (r + 1) <= n) ++r;
    contract_assert(r * r <= n);                 // assertion interne
    return r;
}
```

Chaque contrat est évalué selon une **sémantique** choisie à la compilation, sans changer le code : **ignorer** (aucune vérification), **observer** (vérifier, appeler le gestionnaire de violation, puis continuer), **appliquer** (vérifier puis arrêter), **appliquer rapidement** (arrêt immédiat sans gestionnaire). Le support par les compilateurs est récent : consultez la documentation de votre version. Avant C++26, on utilise `assert`, la bibliothèque GSL (`Expects`, `Ensures`) ou des macros maison.

### 29.9 Concurrence et sûreté

Une **course aux données** est un UB. Les remèdes : ne **rien partager** (données propres à chaque fil), partager des données **immuables**, ou **synchroniser** (mutex, atomiques, passage de messages) — voir le chapitre 30. Vérifiez avec `-fsanitize=thread`.

### 29.10 Le futur de la sûreté en C++

Le comité C++ et la communauté renforcent la sûreté : **bibliothèque durcie**, **contrats**, **comportement erroné** pour l'initialisation (C++26), profils de sûreté (en discussion), options de compilation (`-fbounds-safety`, `-ftrivial-auto-var-init`). Le principe reste : **écrire un sous-ensemble sûr du langage**, vérifié par des outils, et isoler le code bas niveau.

### À retenir (chapitre 29)

- L'UB n'est pas « une erreur qui plante » : c'est l'absence de toute garantie, qui autorise les optimisations les plus agressives.
- Sources d'UB à connaître : mémoire, arithmétique signée, alias strict, courses aux données, itérateurs invalidés, ODR.
- Outils : `-Wall -Wextra`, ASan, UBSan, TSan, analyseurs statiques, fuzzing, bibliothèque durcie.
- Contrats / `assert` pour les bogues, `optional` / `expected` pour les échecs attendus, exceptions pour l'exceptionnel.

---

## Chapitre 30 — La bibliothèque standard : panorama

La **bibliothèque standard** (STL au sens large) est l'un des grands atouts du C++. Elle est **générique** (templates), **efficace** (aucun surcoût) et **composable** (les algorithmes opèrent sur tous les conteneurs par l'intermédiaire des itérateurs). La règle est simple : **avant d'écrire une fonction, cherchez si la bibliothèque standard l'offre déjà** (référence : cppreference.com).

### 30.1 Organisation

- **Utilitaires** : `<utility>`, `<tuple>`, `<optional>`, `<variant>`, `<any>`, `<expected>`, `<functional>`, `<memory>`, `<bit>`, `<limits>`, `<type_traits>`, `<concepts>`, `<source_location>`, `<version>`.
- **Conteneurs** : `<array>`, `<vector>`, `<deque>`, `<list>`, `<forward_list>`, `<set>`, `<map>`, `<unordered_set>`, `<unordered_map>`, `<stack>`, `<queue>`, `<flat_map>`, `<flat_set>`, `<span>`, `<mdspan>`, `<inplace_vector>`.
- **Algorithmes** : `<algorithm>`, `<numeric>`, `<ranges>`, `<execution>`.
- **Chaînes et texte** : `<string>`, `<string_view>`, `<format>`, `<print>`, `<charconv>`, `<regex>`, `<locale>`, `<text_encoding>`.
- **Entrées/sorties** : `<iostream>`, `<fstream>`, `<sstream>`, `<iomanip>`, `<filesystem>`, `<cstdio>`.
- **Nombres** : `<cmath>`, `<complex>`, `<random>`, `<numbers>`, `<valarray>`, `<ratio>`.
- **Temps** : `<chrono>`, `<ctime>`.
- **Concurrence** : `<thread>`, `<mutex>`, `<shared_mutex>`, `<condition_variable>`, `<atomic>`, `<future>`, `<latch>`, `<barrier>`, `<semaphore>`, `<stop_token>`.
- **Coroutines et générateurs** : `<coroutine>`, `<generator>`.
- **Erreurs** : `<exception>`, `<stdexcept>`, `<system_error>`, `<cassert>`, `<stacktrace>`.

### 30.2 Algorithmes et ranges

Les algorithmes se regroupent en familles ; chacun existe en version itérateurs (`std::`) et ranges (`std::ranges::`, C++20).

- **Parcours et transformation** : `for_each`, `transform`, `copy`, `copy_if`, `move`, `fill`, `generate`, `iota`, `replace`, `reverse`, `rotate`, `shuffle`.
- **Recherche** : `find`, `find_if`, `search`, `adjacent_find`, `count`, `count_if`, `any_of`, `all_of`, `none_of`, `mismatch`, `equal`.
- **Tri et ordre** : `sort`, `stable_sort`, `partial_sort`, `nth_element`, `is_sorted`, `partition`, `merge`, `unique`.
- **Recherche dans un intervalle trié** : `binary_search`, `lower_bound`, `upper_bound`, `equal_range`.
- **Ensembles triés** : `set_union`, `set_intersection`, `set_difference`.
- **Extrema** : `min`, `max`, `minmax`, `clamp`, `min_element`, `max_element`.
- **Numérique** : `accumulate`, `reduce`, `inner_product`, `partial_sum`, `adjacent_difference`, `transform_reduce`, `gcd`, `lcm`.
- **Suppression** : `remove` / `remove_if` (déplacent, ne réduisent pas), puis `erase` ; `std::erase` / `std::erase_if` (C++20) font tout en un.

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <numeric>
#include <ranges>
#include <string>
#include <vector>

struct Employe { std::string nom; int age; double salaire; };

int main() {
    std::vector<Employe> equipe{{"Ana", 31, 3200}, {"Luc", 45, 4100}, {"Zoé", 28, 2900}, {"Max", 52, 5000}};

    std::ranges::sort(equipe, {}, &Employe::age);               // tri par âge via une projection
    for (const auto &e : equipe) std::cout << e.nom << ' ' << e.age << '\n';

    auto budget = std::ranges::fold_left(equipe | std::views::transform(&Employe::salaire), 0.0, std::plus{});   // C++23
    std::cout << "budget = " << budget << '\n';

    auto seniors = equipe | std::views::filter([](const Employe &e) { return e.age >= 40; })
                          | std::views::transform(&Employe::nom);
    for (const std::string &n : seniors) std::cout << n << ' ';
    std::cout << '\n';

    std::vector<int> v{3, 1, 4, 1, 5, 9, 2, 6};
    std::ranges::sort(v);
    v.erase(std::unique(v.begin(), v.end()), v.end());          // supprime les doublons consécutifs
    auto pos = std::ranges::lower_bound(v, 5);                  // dichotomie sur un intervalle trié
    std::cout << *pos << ' ' << std::accumulate(v.begin(), v.end(), 0) << '\n';
}
```

**Vues** (*views*) du C++20/23 : `filter`, `transform`, `take`, `drop`, `take_while`, `reverse`, `iota`, `split`, `join`, `keys`, `values`, `enumerate`, `zip`, `chunk`, `slide`, `stride`, `cartesian_product`, et `std::ranges::to<Conteneur>` (C++23 : matérialise une vue). Elles sont **paresseuses**, ne possèdent pas leurs éléments et se composent avec `|`.

**Parallélisme** *(C++17)* : un premier argument de **politique d'exécution** (`<execution>`) active la version parallèle : `std::sort(std::execution::par, v.begin(), v.end());` — politiques `seq`, `par`, `par_unseq`, `unseq`.

### 30.3 Utilitaires de valeurs

```cpp
#include <any>
#include <iostream>
#include <optional>
#include <string>
#include <tuple>
#include <variant>

std::tuple<int, std::string, double> donnees() { return {1, "ok", 2.5}; }

int main() {
    auto [id, etat, v] = donnees();                         // liaisons structurées sur un tuple
    auto t = std::make_tuple(1, 2.0, "a");
    std::cout << std::get<0>(t) << ' ' << std::tuple_size_v<decltype(t)> << ' ' << id << etat << v << '\n';

    std::optional<std::string> nom;                         // valeur facultative
    std::cout << nom.value_or("anonyme") << '\n';
    nom = "Ana";
    if (nom) std::cout << *nom << ' ' << nom->size() << '\n';
    auto exclame = nom.transform([](const std::string &s) { return s + "!"; });     // C++23 : opérations monadiques
    std::cout << *exclame << '\n';

    std::any a = 42;
    a = std::string("texte");
    std::cout << std::any_cast<std::string>(a) << '\n';
}
```

- `std::pair` / `std::tuple` : regroupent des valeurs hétérogènes anonymes (préférez un `struct` nommé quand la signification compte).
- `std::optional<T>` : une valeur ou rien ; `std::variant<Ts...>` : une valeur parmi plusieurs types ; `std::any` : n'importe quel type copiable ; `std::expected<T, E>` : résultat ou erreur.
- `std::move`, `std::forward`, `std::swap`, `std::exchange`, `std::to_underlying`, `std::unreachable` (C++23).
- `std::function`, `std::bind_front`, `std::invoke`, `std::reference_wrapper`, `std::hash`, `std::less<>`, `std::plus<>`… dans `<functional>`.

### 30.4 Texte : expressions régulières

```cpp
#include <iostream>
#include <regex>
#include <string>

int main() {
    std::string texte = "Contact : ana@example.org, luc@test.fr ; tel 06-12-34-56-78";

    std::regex courriel(R"(([\w.]+)@([\w.]+\.[a-z]{2,}))");           // chaîne brute : pas de double \
    for (std::sregex_iterator it(texte.begin(), texte.end(), courriel), fin; it != fin; ++it) {
        std::cout << "adresse : " << (*it)[0] << " (utilisateur : " << (*it)[1] << ")\n";
    }

    std::cout << std::regex_replace(texte, std::regex(R"(\d{2}-\d{2}-\d{2}-\d{2}-\d{2})"), "**-**-**-**-**") << '\n';
    std::cout << std::regex_match("2026-11-11", std::regex(R"(\d{4}-\d{2}-\d{2})")) << '\n';   // 1
}
```

`std::regex` est **lent** et d'implémentation inégale : pour des analyses critiques, préférez des bibliothèques spécialisées (RE2, CTRE, PCRE2) ou un analyseur écrit à la main. Le formatage (`std::format`, `std::print`) a été vu au chapitre 7, les conversions numériques (`from_chars`, `to_chars`) au chapitre 12.

### 30.5 Mathématiques, nombres aléatoires, temps

```cpp
#include <chrono>
#include <cmath>
#include <complex>
#include <format>
#include <iostream>
#include <numbers>
#include <numeric>
#include <random>
#include <thread>

int main() {
    // --- <cmath> et <numeric> ---
    std::cout << std::sqrt(2.0) << ' ' << std::pow(2, 10) << ' ' << std::hypot(3, 4) << ' ' << std::abs(-3.5) << '\n';
    std::cout << std::floor(2.7) << std::ceil(2.1) << std::round(2.5) << std::trunc(-2.7) << '\n';       // 2 3 3 -2
    std::cout << std::sin(std::numbers::pi / 2) << ' ' << std::log(std::numbers::e) << ' ' << std::exp(0) << '\n';
    std::cout << std::gcd(12, 18) << ' ' << std::lcm(4, 6) << ' ' << std::midpoint(10, 20) << '\n';       // 6 12 15
    std::complex<double> z{1, 2};
    std::cout << std::abs(z) << ' ' << z * z << '\n';

    // --- nombres aléatoires : <random> (et NON rand()) ---
    std::random_device graine;                                     // source d'entropie
    std::mt19937 gen(graine());                                    // moteur Mersenne Twister
    std::uniform_int_distribution<int> de(1, 6);                   // distribution : entier uniforme 1..6
    std::normal_distribution<double> gauss(0.0, 1.0);              // loi normale
    std::cout << de(gen) << ' ' << de(gen) << ' ' << gauss(gen) << '\n';

    // --- temps : <chrono> ---
    using namespace std::chrono_literals;
    auto debut = std::chrono::steady_clock::now();                 // horloge monotone : pour mesurer
    std::this_thread::sleep_for(50ms);
    auto ecoule = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now() - debut);
    std::cout << ecoule.count() << " ms\n";

    auto maintenant = std::chrono::system_clock::now();            // horloge murale
    std::cout << std::format("{:%Y-%m-%d %H:%M}", maintenant) << '\n';     // C++20 (UTC)
    std::chrono::year_month_day date{std::chrono::year{2026}, std::chrono::November, std::chrono::day{11}};
    std::cout << std::chrono::weekday{std::chrono::sys_days{date}}.c_encoding() << '\n';      // 3 : mercredi (0 = dimanche)
}
```

- **Hasard** : n'utilisez **pas** `rand()` (qualité médiocre, uniformité faussée par `%`). Un **moteur** (`mt19937`, `minstd_rand`) produit des bits, une **distribution** (`uniform_int_distribution`, `uniform_real_distribution`, `normal_distribution`, `bernoulli_distribution`…) les transforme. Un `std::random_device` fournit la graine. `mt19937` n'est **pas** cryptographique.
- **Temps** : une **durée** (`std::chrono::seconds`, `milliseconds`), un **instant** (`time_point`) et une **horloge** (`steady_clock` pour mesurer, `system_clock` pour la date civile). Les unités sont vérifiées à la compilation : on ne confond pas secondes et millisecondes. C++20 ajoute le calendrier (`year_month_day`, `weekday`), les fuseaux horaires (`zoned_time`) et le formatage.
- **Calcul numérique** : `<cmath>` (fonctions mathématiques, `std::isnan`, `std::fma`), `<complex>`, `<numbers>`, `<valarray>`, `<ratio>` (rationnels à la compilation) ; pour l'algèbre linéaire sérieuse, **Eigen**, BLAS / LAPACK ; `std::mdspan` (C++23) pour les tableaux multidimensionnels ; `<simd>` (C++26) pour le calcul vectoriel portable.

### 30.6 Programmation concurrente

La concurrence introduit des **fils d'exécution** (*threads*) qui partagent la mémoire. Compilez avec `-pthread`.

```cpp
#include <atomic>
#include <future>
#include <iostream>
#include <mutex>
#include <numeric>
#include <thread>
#include <vector>

int main() {
    // 1. Créer un fil : std::jthread se joint automatiquement à la destruction (C++20)
    {
        std::jthread t([] { std::cout << "bonjour depuis un fil\n"; });
    }

    // 2. Données partagées : mutex + lock_guard (RAII)
    int compteur = 0;
    std::mutex m;
    {
        std::vector<std::jthread> fils;
        for (int i = 0; i < 4; ++i) {
            fils.emplace_back([&] {
                for (int k = 0; k < 10000; ++k) {
                    std::lock_guard verrou(m);          // verrouille jusqu'à la fin de la portée
                    ++compteur;
                }
            });
        }
    }                                                   // tous les fils sont joints ici
    std::cout << compteur << '\n';                      // 40000 (sans mutex : course aux données, UB)

    // 3. Variable atomique : sans verrou, pour un simple compteur
    std::atomic<int> total{0};
    {
        std::vector<std::jthread> fils;
        for (int i = 0; i < 4; ++i) fils.emplace_back([&] { for (int k = 0; k < 10000; ++k) ++total; });
    }
    std::cout << total << '\n';                         // 40000

    // 4. Résultat asynchrone : std::async + std::future
    std::vector<int> v(1000);
    std::iota(v.begin(), v.end(), 1);
    auto moitie1 = std::async(std::launch::async, [&] { return std::accumulate(v.begin(), v.begin() + 500, 0); });
    int moitie2 = std::accumulate(v.begin() + 500, v.end(), 0);
    std::cout << moitie1.get() + moitie2 << '\n';       // 500500 ; get() attend le résultat et relance l'exception éventuelle
}
```

Boîte à outils :

- **`std::thread` / `std::jthread`** *(C++20)* : fil d'exécution ; `jthread` se joint tout seul et accepte un `std::stop_token` pour une annulation coopérative. Un `std::thread` détruit sans `join()` ni `detach()` appelle `std::terminate`.
- **Exclusion mutuelle** : `std::mutex`, `std::recursive_mutex`, `std::shared_mutex` (lecteurs multiples / un écrivain) ; verrous RAII `std::lock_guard`, `std::unique_lock`, `std::scoped_lock` (plusieurs mutex sans interblocage), `std::shared_lock`.
- **Attente de condition** : `std::condition_variable` (avec un `unique_lock` et un prédicat, pour éviter les réveils intempestifs).
- **Atomiques** : `std::atomic<T>` (opérations indivisibles ; ordres mémoire `memory_order_*`, le défaut `seq_cst` est le plus sûr), `std::atomic_flag`, `std::atomic_ref` (C++20).
- **Résultats asynchrones** : `std::async`, `std::future`, `std::promise`, `std::packaged_task`.
- **Synchronisation moderne** *(C++20)* : `std::latch`, `std::barrier`, `std::counting_semaphore`, `std::binary_semaphore`.
- **`thread_local`** : une copie de la variable par fil.
- **Coroutines** *(C++20)* : fonctions suspendables (`co_await`, `co_yield`, `co_return`) ; `std::generator<T>` *(C++23)* produit des suites paresseuses ; `std::execution` (*senders / receivers*, **C++26**) propose un modèle standard de tâches asynchrones.

**Règles d'or** : ne partagez rien quand c'est possible ; si vous partagez, protégez **toute** donnée modifiée (mutex ou atomique) ; verrouillez toujours dans le **même ordre** (ou utilisez `scoped_lock`) pour éviter l'interblocage ; gardez les sections critiques courtes ; testez avec ThreadSanitizer.

### 30.7 Autres modules à connaître

- **`<span>`, `<mdspan>`** : vues sur des suites contiguës ou multidimensionnelles.
- **`<stacktrace>`** *(C++23)* : trace d'appels pour le diagnostic.
- **`<memory_resource>`** : allocateurs polymorphes (`std::pmr::vector`) pour contrôler l'allocation.
- **`<locale>`** : conventions régionales (formats numériques, dates) ; `std::locale::global`, `imbue`.
- **`<typeinfo>`, `<typeindex>`** : informations de type à l'exécution.
- **`<new>`** : `std::nothrow`, `std::launder`, allocation alignée.
- **Réflexion statique** *(C++26)* : interroger à la compilation la structure d'un type (membres, énumérateurs) et générer du code — par exemple convertir automatiquement une `enum` en chaîne ou sérialiser une `struct` ; c'est l'ajout majeur de C++26 en métaprogrammation.

### 30.8 Comment progresser

1. **Lire la référence** : cppreference.com ; **explorer** avec Compiler Explorer (godbolt.org).
2. **Lire du bon code** : bibliothèque standard, Boost, projets open source modernes.
3. **Ouvrages de référence** : *A Tour of C++* (Stroustrup) ; *Effective Modern C++* (Meyers) ; *C++ Primer* (Lippman) ; *C++ Core Guidelines* (en ligne) ; *C++ Templates: The Complete Guide* (Vandevoorde, Josuttis, Gregor) ; *C++ Concurrency in Action* (Williams).
4. **Suivre l'évolution** : comité WG21, conférences CppCon, C++ on Sea, Meeting C++, ACCU.

### À retenir (chapitre 30)

- La bibliothèque standard est le premier réflexe : conteneurs, algorithmes, ranges, utilitaires, chaînes, temps, hasard, concurrence.
- Algorithmes et vues se composent sans boucle manuelle ; les types riches (`optional`, `variant`, `expected`) expriment l'intention.
- Concurrence : `jthread`, `scoped_lock`, atomiques ; vérifier avec TSan.

---

## Conclusion et récapitulatif

Le cours suit une progression volontaire : **types et valeurs** (chapitres 4 à 6), **flux de contrôle** (7, 8), **abstraction** par les fonctions et les classes (9, 18 à 21), **gestion rigoureuse de la mémoire et de la durée de vie** (10, 13 à 17), **généricité** (20), puis les sujets de **robustesse** et d'**écosystème** (22 à 30). Trois idées traversent l'ensemble :

1. **Le type est un contrat vérifié à la compilation.** Plus vos types sont précis (`enum class`, `std::chrono`, `std::span`, `std::optional`), plus le compilateur détecte d'erreurs à votre place.
2. **Chaque objet a un propriétaire et une durée de vie.** RAII, conteneurs et pointeurs intelligents rendent la gestion des ressources automatique ; les pointeurs bruts ne servent qu'à observer.
3. **Les comportements indéfinis sont l'ennemi.** Compilez avec les avertissements et les sanitizers, préférez les abstractions sûres de la bibliothèque standard, et isolez le code à risque dans de petites zones identifiées.

### Check-list d'un code C++ moderne

- norme explicite (`-std=c++20` ou plus), `-Wall -Wextra -Wpedantic`, sanitizers en développement ;
- `std::vector`, `std::string`, `std::array`, `std::span`, `std::string_view` ; aucun `new` / `delete` nu ;
- `const`, `constexpr`, `[[nodiscard]]`, `override`, `explicit`, `noexcept` ;
- `enum class`, `using`, `auto` quand le type est évident ;
- algorithmes et ranges plutôt que boucles à indices ;
- règle du zéro ; destructeur virtuel pour les bases polymorphes ;
- exceptions pour l'exceptionnel, `optional` / `expected` pour l'attendu, contrats pour les bogues ;
- tests automatisés, formatage et analyse statique en intégration continue.

Bon apprentissage, et bonne programmation en C++ !
