<div align="center">

# Langage C++ — Guide complet

**Des premiers programmes à la programmation orientée objet, à la bibliothèque standard, aux fichiers et à la compilation**

*Mis à jour pour C++17 / C++20 / C++23 / C++26 (novembre 2026)*

</div>

---

## Ressources

| Ressource | Lien |
| --- | --- |
| Exercices | [exercises](/language/exercises/cpp) |
| Solutions | [solutions](/language/solutions/cpp) |
| Projets | [projects](/language/projects/cpp) |
| Référence | [cppreference.com (C++)](https://en.cppreference.com/w/cpp) |
| Normes | [ISO/IEC 14882](https://www.iso.org/standard/83626.html) · [Brouillons et documents WG21](https://www.open-std.org/jtc1/sc22/wg21/) |

---

## Sommaire

**Niveau débutant**

1. [Introduction au C++](#1-introduction-au-c)
2. [Structure d'un programme C++](#2-structure-dun-programme-c)
3. [Syntaxe et mots-clés](#3-syntaxe-et-mots-clés)
4. [Types de données et variables](#4-types-de-données-et-variables)
5. [Constantes et littéraux](#5-constantes-et-littéraux)
6. [Opérateurs et expressions](#6-opérateurs-et-expressions)
7. [Entrées et sorties](#7-entrées-et-sorties)
8. [Structures de contrôle](#8-structures-de-contrôle)
9. [Fonctions](#9-fonctions)
10. [Portée et durée de vie des variables](#10-portée-et-durée-de-vie-des-variables)

**Niveau intermédiaire**

11. [Tableaux](#11-tableaux)
12. [Chaînes de caractères](#12-chaînes-de-caractères)
13. [Pointeurs](#13-pointeurs)
14. [Allocation dynamique de mémoire](#14-allocation-dynamique-de-mémoire)
15. [Retourner des tableaux et des chaînes](#15-retourner-des-tableaux-et-des-chaînes)
16. [Structures de données dynamiques](#16-structures-de-données-dynamiques)
17. [Références et pointeurs doubles](#17-références-et-pointeurs-doubles)
18. [Structures, classes et unions](#18-structures-classes-et-unions)
19. [Énumérations (`enum`)](#19-énumérations-enum)
20. [`using`, `typedef` et templates](#20-using-typedef-et-templates)
21. [Pointeurs de fonctions, lambdas et polymorphisme](#21-pointeurs-de-fonctions-lambdas-et-polymorphisme)

**Niveau avancé**

22. [Gestion des fichiers](#22-gestion-des-fichiers)
23. [Arguments de la ligne de commande](#23-arguments-de-la-ligne-de-commande)
24. [Directives du préprocesseur et modules](#24-directives-du-préprocesseur-et-modules)
25. [Opérateurs bit à bit](#25-opérateurs-bit-à-bit)
26. [Récursivité](#26-récursivité)
27. [Unicode et caractères larges](#27-unicode-et-caractères-larges)
28. [Compilation et exécution](#28-compilation-et-exécution)
29. [Comportements indéfinis, exceptions et sécurité](#29-comportements-indéfinis-exceptions-et-sécurité)
30. [Bibliothèque standard et aide-mémoire](#30-bibliothèque-standard-et-aide-mémoire)

> **Légende** : *(ajout)* = notion absente du guide C ou propre au C++ ; *(à jour)* = pratique moderne remplaçant une ancienne ; *(C++11)*, *(C++17)*, *(C++20)*, *(C++23)*, *(C++26)* = norme qui a introduit la fonctionnalité.

---

# Niveau débutant

---

# 1. Introduction au C++

## 1.1 Qu'est-ce que le C++ ?

Le **C++** est un langage de programmation **compilé, multi-paradigme et à typage statique**, créé à partir de **1979** par **Bjarne Stroustrup** aux **Laboratoires Bell** sous le nom « C with Classes », puis renommé **C++** en 1983. Il étend le langage C avec les **classes**, les **templates**, les **exceptions**, les **espaces de noms** et une vaste **bibliothèque standard**, tout en conservant l'accès direct à la **mémoire** et au matériel. Son principe directeur : les **abstractions à coût nul** (*zero-overhead principle*) : on ne paie pas pour ce qu'on n'utilise pas, et ce qu'on utilise ne pourrait pas être écrit plus efficacement à la main.

| Caractéristique | Détail |
| --- | --- |
| Paradigme | **Multi-paradigme** : procédural, orienté objet, générique (templates), fonctionnel (lambdas, algorithmes) |
| Typage | **Statique** et plus strict qu'en C (peu de conversions implicites dangereuses) |
| Exécution | Compilé vers du **code machine natif** |
| Gestion de la mémoire | **Déterministe** : `RAII` et pointeurs intelligents ; `new` / `delete` manuels possibles ; pas de ramasse-miettes |
| Portabilité | Très bonne : compilateurs pour presque toutes les architectures |
| Relation avec le C | Presque (mais **pas exactement**) un sur-ensemble du C ; voir [section 1.9](#19-différences-majeures-avec-le-c-ajout) |
| Influence | A inspiré Java, C#, D, Rust (traits/concepts), Carbon… |

## 1.2 Pourquoi apprendre le C++ ?

- **Performance** : moteurs de jeux (Unreal), finance haute fréquence, calcul scientifique, traitement d'images, apprentissage automatique (cœur de TensorFlow, PyTorch).
- **Systèmes et logiciels de grande taille** : navigateurs (Chrome, Firefox), bases de données (MySQL, MongoDB, ClickHouse), suites bureautiques, outils de CAO, compilateurs (LLVM/Clang).
- **Embarqué et temps réel** : automobile, robotique, aéronautique, microcontrôleurs.
- **Abstraction sans surcoût** : écrire du code expressif (conteneurs, algorithmes, objets) compilé aussi efficacement que du C.
- **Écosystème** : un très grand nombre de bibliothèques ; interopérabilité directe avec le C et avec d'autres langages.

> **Attention** : Le C++ est un langage **vaste** ; on peut y écrire du « C avec classes » (dangereux) ou du **C++ moderne** (sûr et concis). Ce guide enseigne le second : `std::string` plutôt que `char *`, `std::vector` plutôt que `malloc`, pointeurs intelligents plutôt que `delete` manuel (voir [section 29](#29-comportements-indéfinis-exceptions-et-sécurité)).

## 1.3 Histoire et normes *(à jour)*

| Norme | Année | Apports principaux |
| --- | --- | --- |
| **C with Classes** | 1979 | Premières classes au-dessus du C (Stroustrup) |
| **C++98** | 1998 | Première norme ISO : classes, héritage, templates, **STL**, exceptions, espaces de noms, `bool`, RTTI |
| **C++03** | 2003 | Correctif de C++98 |
| **C++11** | 2011 | `auto`, `for` sur intervalle, **lambdas**, **sémantique de déplacement** (`&&`), `nullptr`, `constexpr`, **pointeurs intelligents**, `override` / `final`, initialisation uniforme `{}`, templates variadiques, `<thread>`, `<chrono>`, `<random>`, `unordered_map` |
| **C++14** | 2014 | Lambdas génériques, déduction du type de retour, `make_unique`, littéraux binaires `0b…`, séparateur `'` |
| **C++17** | 2017 | Liaisons structurées, `if` / `switch` avec initialiseur, `if constexpr`, `optional`, `variant`, `any`, `string_view`, `<filesystem>`, variables `inline`, expressions de repli, algorithmes parallèles, `[[nodiscard]]` |
| **C++20** | 2020 | **Concepts**, **ranges**, **coroutines**, **modules**, opérateur `<=>`, `std::format`, `std::span`, `consteval`, `constinit`, `<bit>`, `jthread`, `<chrono>` calendriers |
| **C++23** | 2023 | `std::print` / `println`, `std::expected`, `std::mdspan`, *deducing this*, `import std;`, `std::flat_map`, `std::generator`, `std::stacktrace`, `std::to_underlying`, `if consteval`, `std::unreachable` |
| **C++26** | 2026 (travaux techniques terminés en mars 2026 ; publication ISO ensuite) | **Réflexion statique**, **contrats** (`pre`, `post`, `contract_assert`), `std::execution` (émetteurs/récepteurs), **bibliothèque standard durcie**, `#embed`, indexation de paquets de templates, `<simd>`, `std::inplace_vector` |
| **C++29** | en préparation | Prochaine révision, travaux déjà commencés par le comité WG21 |

Le compilateur choisit la norme avec `-std=` : `-std=c++17`, `-std=c++20`, `-std=c++23`, `-std=c++2c` (C++26). Le standard par défaut dépend du compilateur et de sa version (par exemple GCC utilise `gnu++17` depuis GCC 11 ; MSVC est configuré avec `/std:c++14` par défaut) : indiquez toujours la norme explicitement. Les versions récentes de GCC et Clang implémentent déjà la majeure partie de C++26 ; vérifiez le support de votre compilateur sur cppreference (page « Compiler support »).

## 1.4 Fonctionnement d'un programme C++

1. **Écrire** le code source dans un fichier `.cpp` (ou `.cc`, `.cxx`) ; les en-têtes portent l'extension `.hpp` (ou `.h`, `.hxx`).
2. **Compiler** : le compilateur (`g++`, `clang++`, MSVC…) le traduit en code machine.
3. **Exécuter** le programme obtenu.

```text
hello.cpp ──> préprocesseur ──> compilateur ──> assembleur ──> éditeur de liens ──> exécutable
 (source)         (.ii)            (.s)            (.o)          (+ bibliothèques)
```

> **Remarque** : Avec les **modules** (C++20), l'étape d'inclusion textuelle par le préprocesseur est remplacée par l'importation de modules déjà compilés (voir [section 24](#24-directives-du-préprocesseur-et-modules)).

## 1.5 Installer un compilateur

| Système | Installation |
| --- | --- |
| **Linux (Debian/Ubuntu)** | `sudo apt install build-essential` (g++, make) · `sudo apt install clang cmake` |
| **macOS** | `xcode-select --install` (Clang) ou `brew install gcc` |
| **Windows** | **MSYS2** (`pacman -S mingw-w64-ucrt-x86_64-gcc`) ou **WSL** (Linux sous Windows, recommandé) ; ou **Visual Studio** (MSVC) |

```bash
g++ --version
clang++ --version
```

## 1.6 Premier programme : « Hello, World ! »

```cpp
#include <iostream>                     // flux d'entrée/sortie

int main() {                            // point d'entrée du programme
    std::cout << "Bonjour le monde !\n";   // affiche du texte
    return 0;                           // 0 = succès (facultatif dans main)
}
```

| Élément | Rôle |
| --- | --- |
| `#include <iostream>` | Inclut les déclarations des flux (`std::cout`, `std::cin`…) |
| `int main()` | Fonction principale : l'exécution commence ici |
| `std::cout` | Flux de sortie standard ; `std::` désigne l'espace de noms de la bibliothèque standard |
| `<<` | Opérateur d'insertion : envoie une valeur dans le flux |
| `\n` | Saut de ligne |
| `return 0;` | Code de sortie transmis au système (`0` = succès) |

Version moderne avec `std::println` *(C++23)* :

```cpp
#include <print>

int main() {
    std::println("Bonjour le monde ! {} + {} = {}", 2, 3, 2 + 3);   // saut de ligne ajouté automatiquement
}
```

> **Remarque** : En C++, `main` retourne **implicitement 0** si le `return` est omis (même avant C++11), et `int main()` équivaut à `int main(void)`. Le `return 0;` reste utile par clarté.
> **Remarque** : Les en-têtes de la bibliothèque standard n'ont **pas d'extension** (`<iostream>`, `<vector>`) ; les en-têtes hérités du C s'écrivent avec un `c` initial : `<cstdio>`, `<cstdlib>`, `<cmath>`.

## 1.7 Compiler et exécuter

```bash
g++ -Wall -Wextra -std=c++20 hello.cpp -o hello     # compiler
./hello                                             # exécuter (Linux/macOS)
hello.exe                                           # exécuter (Windows)
```

## 1.8 Erreurs fréquentes de débutant

| Erreur | Exemple | Correction |
| --- | --- | --- |
| Point-virgule oublié | `std::cout << "Hi"` | Ajouter `;` |
| Oubli du `std::` | `cout << "Hi";` | `std::cout` (ou `using std::cout;`) |
| Faute de frappe | `std::cuot << "Hi";` | `std::cout` |
| Casse | `Main()` ou `STD::cout` | C++ est **sensible à la casse** |
| Oubli de `#include` | `std::string` sans `<string>` | Inclure l'en-tête |
| `<<` / `>>` inversés | `std::cin << x;` | `std::cin >> x;` |
| `=` au lieu de `==` | `if (x = 5)` | `if (x == 5)` |
| Variable non initialisée | `int x; std::cout << x;` | Initialiser : `int x{};` ou `int x = 0;` |
| Division entière | `1 / 2` vaut `0` | `1.0 / 2` |
| `using namespace std;` dans un en-tête | pollue tous les fichiers qui l'incluent | Le proscrire des fichiers `.hpp` |

## 1.9 Différences majeures avec le C *(ajout)*

Le C++ n'est **pas** un sur-ensemble strict du C : du code C valide peut être refusé (ou se comporter différemment) en C++.

| Sujet | C | C++ |
| --- | --- | --- |
| Conversion `void *` vers `T *` | Implicite | **Cast obligatoire** (à éviter : utiliser `new`, conteneurs) |
| Fonction sans paramètres | `f()` = arguments non spécifiés (avant C23) | `f()` = `f(void)` |
| Déclaration implicite de fonction | Tolérée avant C99 | **Interdite** |
| Type d'un littéral `'a'` | `int` | `char` |
| `bool`, `true`, `false` | Mots-clés seulement depuis C23 | **Mots-clés** depuis toujours |
| Tableaux de taille variable (VLA) | C99 | **Non standard** : utiliser `std::vector` ou `std::array` |
| Littéraux composés `(T){...}` | C99 | **Non standard** |
| `restrict` | C99 | Non standard (extension `__restrict`) |
| Nom d'une `struct` | Utilisable avec `struct` devant | Utilisable **seul** : c'est un type |
| Structure vide | Comportement dépendant du compilateur | Taille d'au moins 1 octet |
| `const` global | Liaison **externe** par défaut | Liaison **interne** par défaut |
| Initialisation désignée | C99, complète | C++20, **dans l'ordre de déclaration** seulement |
| `goto` par-dessus une initialisation | Permis | **Interdit** |
| Chaîne littérale | `char[N]` | `const char[N]` |

---

# 2. Structure d'un programme C++

## 2.1 Organisation générale

```cpp
#include <iostream>             // 1. Directives du préprocesseur
#include <string>

constexpr double TAUX_TVA = 0.2;   //    constantes (préférer constexpr à #define)

int compteur = 0;               // 2. Variables globales (à limiter)

int carre(int x);               // 3. Déclarations (prototypes) de fonctions

int main() {                    // 4. Fonction principale
    int n = 5;                  //    déclarations
    std::cout << "Le carré de " << n << " est " << carre(n) << '\n';   // instructions
    return 0;
}

int carre(int x) {              // 5. Définitions des autres fonctions
    return x * x;
}
```

## 2.2 Les composants

| Composant | Rôle |
| --- | --- |
| **Directives du préprocesseur** | Commencent par `#` ; traitées **avant** la compilation (`#include`, `#define`, `#ifdef`…) |
| **Déclarations globales** | Hors de toute fonction ; visibles dans tout le fichier après leur déclaration |
| **Espaces de noms** (`namespace`) | Regroupent des noms pour éviter les collisions |
| **Prototypes** | Annoncent le type de retour et les paramètres d'une fonction |
| **Classes et structures** | Définissent de nouveaux types avec données et fonctions membres |
| **Templates** | Fonctions et classes paramétrées par des types ou des valeurs |
| **`main()`** | Point d'entrée **obligatoire** (une seule par programme) ; ne peut pas être appelée récursivement |
| **Instructions** | Terminées par `;` |
| **Blocs** | Délimités par `{ }` |
| **Commentaires** | Ignorés par le compilateur |

## 2.3 Commentaires

```cpp
#include <iostream>

// Commentaire sur une ligne

/* Commentaire
   sur plusieurs lignes (ne s'imbrique pas) */

/// Commentaire de documentation (Doxygen) : additionne deux entiers.
int somme(int a, int b) { return a + b; }

int main() {
    std::cout << "Les commentaires sont ignorés par le compilateur.\n";   // affiche cette phrase
    std::cout << somme(2, 3) << '\n';
    return 0;
}
```

## 2.4 Variables et instructions

```cpp
#include <iostream>

int main() {
    int age;                     // déclaration (valeur indéterminée !)
    age = 25;                    // affectation
    int taille = 180;            // déclaration + initialisation
    int poids{75};               // initialisation uniforme (recommandée)
    std::cout << "age = " << age << ", taille = " << taille << ", poids = " << poids << '\n';
    return 0;
}
```

> **Bonne pratique** : On déclare une variable **au plus près de son usage** (dans un bloc, dans l'en-tête d'un `for` ou d'un `if`), et on l'**initialise toujours** à la déclaration.

## 2.5 Code de sortie

```cpp
#include <cstdlib>
#include <fstream>
#include <iostream>

int main() {
    std::ifstream f("fichier_inexistant.txt");
    if (!f) {
        std::cerr << "Erreur : impossible d'ouvrir le fichier\n";
        return EXIT_FAILURE;     // erreur : le shell récupère 1 (echo $?)
    }
    std::cout << "Fichier ouvert\n";
    return 0;                    // ou EXIT_SUCCESS (de <cstdlib>)
}                                // le fichier est fermé automatiquement (RAII)
```

Le shell récupère ce code : `echo $?` (Linux/macOS) ou `echo %ERRORLEVEL%` (Windows).

## 2.6 Les étapes de la compilation (rappel)

1. **Préprocessing** : `#include`, `#define`, compilation conditionnelle.
2. **Compilation** : `.cpp` -> assembleur -> `.o` (objet) ; instanciation des templates.
3. **Édition de liens** : assemblage des `.o` et des bibliothèques en exécutable.
4. **Exécution**.

Détails dans la [section 28](#28-compilation-et-exécution).

## 2.7 Espaces de noms (`namespace`) *(ajout)*

Un **espace de noms** regroupe des identifiants sous un préfixe. Toute la bibliothèque standard vit dans `std`.

```cpp
#include <iostream>
#include <string>

namespace geometrie {                 // espace de noms personnel
    constexpr double PI = 3.14159265;
    double aire_cercle(double r) { return PI * r * r; }
}

namespace g = geometrie;              // alias d'espace de noms

int main() {
    using std::cout;                  // using-declaration : un seul nom importé
    using std::string;

    string titre = "Aire";
    cout << titre << " = " << geometrie::aire_cercle(2.0) << '\n';
    cout << g::PI << '\n';
    return 0;
}
```

| Forme | Effet | Conseil |
| --- | --- | --- |
| `std::cout` | Nom qualifié | Toujours valable, le plus clair |
| `using std::cout;` | Importe **un** nom | Acceptable dans un `.cpp`, dans une portée limitée |
| `using namespace std;` | Importe **tout** `std` | À éviter ; **interdit dans les en-têtes** |
| `namespace { ... }` | Espace de noms **anonyme** : visible dans le seul fichier | Remplace `static` pour les fonctions et variables globales |
| `namespace a::b::c { }` *(C++17)* | Espaces imbriqués abrégés | Pratique |

---

# 3. Syntaxe et mots-clés

## 3.1 Règles de syntaxe

- Le C++ est **sensible à la casse** : `Valeur` et `valeur` sont deux identifiants distincts.
- La mise en page est **libre** : les espaces et les sauts de ligne n'ont pas d'incidence sur le sens (sauf dans les littéraux de chaîne et les directives `#`).
- Chaque **instruction** se termine par `;` ; un **bloc** `{ ... }` regroupe des instructions et ne se termine pas par `;` (sauf après la définition d'une classe, d'une struct, d'une union ou d'une enum).
- Les **trigraphes** (`??=`…) ont été supprimés en C++17.
- Les **jetons alternatifs** (`and`, `or`, `not`…) sont des mots-clés équivalents aux opérateurs symboliques.

## 3.2 Identifiants

Un identifiant est composé de lettres, de chiffres et de `_`, et ne commence pas par un chiffre. Sont **réservés** à l'implémentation : les noms contenant `__` (double tiret bas) et ceux qui commencent par `_` suivi d'une majuscule.

```cpp
#include <iostream>

int main() {
    int age = 30;                 // valide
    int _prive = 1;               // valide (réservé hors portée de classe/fonction si global)
    int nombre_de_points = 3;     // snake_case : style courant de la bibliothèque standard
    int nombreDePoints = 4;       // camelCase : autre convention répandue
    // int 2fois = 2;             // invalide : commence par un chiffre
    // int mon-nom = 3;           // invalide : '-' interdit
    // int class = 1;             // invalide : mot-clé
    std::cout << age << _prive << nombre_de_points << nombreDePoints << '\n';
    return 0;
}
```

> **Bonne pratique** : Choisissez une convention (ex. `snake_case` pour variables et fonctions, `PascalCase` pour les types) et gardez-la partout dans le projet.

## 3.3 Mots-clés du langage *(à jour : C++23)*

| Catégorie | Mots-clés |
| --- | --- |
| **Types** | `bool` `char` `char8_t` `char16_t` `char32_t` `wchar_t` `short` `int` `long` `float` `double` `signed` `unsigned` `void` `auto` `decltype` |
| **Contrôle** | `if` `else` `switch` `case` `default` `for` `while` `do` `break` `continue` `goto` `return` |
| **Exceptions** | `try` `catch` `throw` `noexcept` |
| **Classes** | `class` `struct` `union` `enum` `public` `protected` `private` `virtual` `override` `final` `friend` `this` `operator` `explicit` `mutable` `delete` `default` |
| **Templates et types** | `template` `typename` `concept` `requires` `using` `typedef` `typeid` |
| **Stockage et qualificateurs** | `static` `extern` `thread_local` `inline` `const` `volatile` `constexpr` `consteval` `constinit` `register` (inutilisé) |
| **Mémoire** | `new` `delete` `nullptr` `sizeof` `alignof` `alignas` |
| **Conversions** | `static_cast` `dynamic_cast` `const_cast` `reinterpret_cast` |
| **Espaces de noms et modules** | `namespace` `module` `import` `export` |
| **Coroutines** | `co_await` `co_yield` `co_return` |
| **Divers** | `static_assert` `asm` `true` `false` |
| **Opérateurs alternatifs** | `and` `or` `not` `xor` `bitand` `bitor` `compl` `and_eq` `or_eq` `xor_eq` `not_eq` |

> **Remarque** : Certains mots (`override`, `final`, `import`, `module`) sont **contextuels** : ils n'ont de sens spécial qu'à certains endroits et restent utilisables comme identifiants ailleurs.

## 3.4 Ponctuation et délimiteurs

| Symbole | Usage |
| --- | --- |
| `;` | Fin d'instruction |
| `{ }` | Bloc, corps de classe, liste d'initialisation |
| `( )` | Appels, regroupement d'expressions, conditions |
| `[ ]` | Indexation ; introduction d'une lambda |
| `< >` | Arguments de template (`std::vector<int>`) |
| `::` | Opérateur de **résolution de portée** (`std::cout`, `Classe::membre`) |
| `.` / `->` | Accès à un membre (objet / pointeur) |
| `.*` / `->*` | Accès via pointeur sur membre |
| `,` | Séparateur ; opérateur virgule |
| `:` | Étiquettes, héritage, liste d'initialisation de membres, `for` sur intervalle |
| `? :` | Opérateur conditionnel |
| `...` | Paquet de paramètres (templates variadiques), `catch (...)` |
| `[[ ]]` | Attributs |
| `#` | Directive du préprocesseur |

## 3.5 Attributs *(C++11 et suivants)*

Les **attributs** `[[...]]` donnent des indications au compilateur sans changer la sémantique du programme.

```cpp
#include <cstdlib>
#include <iostream>

[[nodiscard]] int divise(int a, int b) {        // le résultat ne doit pas être ignoré
    return b != 0 ? a / b : 0;
}

[[noreturn]] void quitter(int code) {           // ne retourne jamais
    std::exit(code);
}

[[deprecated("utiliser divise()")]] int ancienne_div(int a, int b) { return a / b; }

int main() {
    int r = divise(10, 2);
    divise(8, 2);                               // avertissement : valeur de retour ignorée
    [[maybe_unused]] int inutile = 0;           // pas d'avertissement « variable inutilisée »

    switch (r) {
        case 5:
            std::cout << "cinq\n";
            [[fallthrough]];                    // chute volontaire vers le cas suivant
        case 6:
            std::cout << "cinq ou six\n";
            break;
        default:
            break;
    }

    if (r > 100) [[unlikely]] {                 // indication pour l'optimiseur (C++20)
        quitter(1);
    }
    return 0;
}
```

| Attribut | Rôle |
| --- | --- |
| `[[nodiscard]]` *(C++17)* | Avertit si la valeur de retour est ignorée (peut porter sur un type) |
| `[[maybe_unused]]` *(C++17)* | Supprime l'avertissement pour un élément inutilisé |
| `[[fallthrough]]` *(C++17)* | Chute voulue dans un `switch` |
| `[[deprecated("msg")]]` *(C++14)* | Marque une entité comme obsolète |
| `[[noreturn]]` *(C++11)* | La fonction ne retourne jamais |
| `[[likely]]` / `[[unlikely]]` *(C++20)* | Indication de probabilité de branche |
| `[[no_unique_address]]` *(C++20)* | Permet de ne pas réserver d'espace pour un membre vide |

---

# 4. Types de données et variables

## 4.1 Types fondamentaux

| Type | Description | Taille typique |
| --- | --- | --- |
| `bool` | Booléen (`true` / `false`) | 1 octet |
| `char` | Caractère / petit entier | 1 octet |
| `short` | Entier court | 2 octets |
| `int` | Entier standard | 4 octets |
| `long` | Entier long | 4 ou 8 octets |
| `long long` | Entier très long | 8 octets |
| `float` | Réel simple précision | 4 octets |
| `double` | Réel double précision | 8 octets |
| `long double` | Réel précision étendue | 8, 12 ou 16 octets |
| `char8_t`, `char16_t`, `char32_t` | Caractères UTF-8, UTF-16, UTF-32 | 1, 2, 4 octets |
| `std::nullptr_t` | Type de `nullptr` | taille d'un pointeur |
| `void` | « Absence de type » | n/a |

```cpp
#include <cfloat>
#include <climits>
#include <iostream>
#include <limits>

int main() {
    std::cout << "int      : " << sizeof(int) << " octets, max = " << std::numeric_limits<int>::max() << '\n';
    std::cout << "long     : " << sizeof(long) << " octets\n";
    std::cout << "double   : " << sizeof(double) << " octets, epsilon = " << std::numeric_limits<double>::epsilon() << '\n';
    std::cout << "bool     : " << sizeof(bool) << " octet\n";
    std::cout << "INT_MIN  : " << INT_MIN << '\n';                 // macro héritée du C, encore valide
    return 0;
}
```

> **Remarque** : Les tailles dépendent de la plateforme. Le C++ garantit seulement des minimums et des relations (`sizeof(char) == 1`). Pour des tailles garanties, voir `<cstdint>` ci-dessous.

## 4.2 Modificateurs : `signed`, `unsigned`, `short`, `long`

| Type | Plage typique |
| --- | --- |
| `signed char` | -128 à 127 |
| `unsigned char` | 0 à 255 |
| `short` | -32 768 à 32 767 |
| `unsigned int` | 0 à 4 294 967 295 |
| `long long` | environ ±9,2 x 10^18 |
| `unsigned long long` | 0 à environ 1,8 x 10^19 |

```cpp
#include <iostream>
#include <limits>

int main() {
    unsigned int u = 0;
    u = u - 1;                                   // débordement non signé : défini (arithmétique modulaire)
    std::cout << u << '\n';                      // 4294967295 si unsigned int fait 32 bits

    int max = std::numeric_limits<int>::max();
    // max + 1;                                  // débordement SIGNÉ : comportement indéfini !
    std::cout << max << '\n';
    return 0;
}
```

## 4.3 Entiers à taille fixe : `<cstdint>` *(à jour)*

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
    std::byte     o{0xFF};               // octet brut (C++17), pas un entier

    std::cout << static_cast<int>(a) << ' ' << static_cast<int>(b) << ' ' << c << ' ' << d << ' ' << n << ' ' << diff << '\n';
    std::cout << std::to_integer<int>(o) << '\n';
    return 0;
}
```

> **Attention** : `std::uint8_t` et `std::int8_t` sont généralement des `char` : `std::cout << b` afficherait un **caractère**, pas un nombre. Convertissez avec `static_cast<int>`.

## 4.4 Booléens

Le type `bool` est **natif** : aucun en-tête à inclure.

```cpp
#include <iostream>

int main() {
    bool actif = true;
    bool vide = false;
    int n = 5;
    bool non_nul = n;                              // conversion : tout non-zéro devient true

    std::cout << actif << ' ' << vide << ' ' << non_nul << '\n';          // 1 0 1
    std::cout << std::boolalpha << actif << ' ' << vide << '\n';          // true false
    return 0;
}
```

## 4.5 Déclarer, initialiser, affecter

```cpp
#include <iostream>

int main() {
    int a;                // valeur indéterminée (à éviter)
    int b = 5;            // initialisation par copie
    int c(5);             // initialisation directe (syntaxe fonctionnelle)
    int d{5};             // initialisation uniforme (recommandée) : refuse les conversions avec perte
    int e{};              // initialisation par valeur : 0
    // int f{3.7};        // ERREUR de compilation : conversion restrictive (narrowing)
    int f = 3.7;          // accepté (tronqué à 3) : source de bugs silencieux

    a = 10;
    std::cout << a << b << c << d << e << f << '\n';
    return 0;
}
```

### Inférence de type avec `auto` *(C++11)*

```cpp
#include <iostream>
#include <map>
#include <string>
#include <utility>

int main() {
    auto n = 42;                         // int
    auto pi = 3.14;                      // double
    auto s = std::string{"abc"};         // std::string
    auto texte = "abc";                  // const char * (et non std::string !)
    decltype(n) m = 7;                   // m a le même type que n

    std::map<std::string, int> ages{{"Ana", 30}, {"Luc", 25}};
    for (const auto &[nom, age] : ages) {          // liaisons structurées (C++17)
        std::cout << nom << " : " << age << '\n';
    }

    auto [x, y] = std::pair{1, 2};       // décomposition d'une paire
    std::cout << n << pi << s << texte << m << x << y << '\n';
    return 0;
}
```

## 4.6 Conversions de types (*casts*)

```cpp
#include <iostream>

int main() {
    int a = 7, b = 2;
    double r1 = a / b;                          // 3 (division entière, puis conversion)
    double r2 = static_cast<double>(a) / b;     // 3.5
    double r3 = (double)a / b;                  // 3.5 : cast « à la C », à éviter

    std::cout << r1 << ' ' << r2 << ' ' << r3 << '\n';
    return 0;
}
```

| Opérateur | Usage |
| --- | --- |
| `static_cast<T>(x)` | Conversion **vérifiée à la compilation** : numérique, vers/depuis `void *`, dans une hiérarchie de classes |
| `dynamic_cast<T>(x)` | Conversion **vérifiée à l'exécution** dans une hiérarchie polymorphe (voir [section 21](#21-pointeurs-de-fonctions-lambdas-et-polymorphisme)) |
| `const_cast<T>(x)` | Ajoute ou retire `const` / `volatile` (rarement justifié) |
| `reinterpret_cast<T>(x)` | Réinterprétation de bits : **dangereux** |
| `std::bit_cast<T>(x)` *(C++20)* | Réinterprétation **sûre** d'un objet de même taille |
| `(T)x`, `T(x)` | Cast à la C : **à proscrire**, car il essaie tous les précédents sans avertir |

## 4.7 Bonnes pratiques

- **Initialisez** toujours les variables, de préférence avec `{}`.
- Utilisez `auto` quand le type est évident ou verbeux, et le type explicite quand il documente l'intention.
- Utilisez `std::size_t` pour les tailles et les indices, `double` par défaut pour les réels.
- Évitez les mélanges signé/non signé dans les comparaisons ; en C++20, utilisez `std::cmp_less`, `std::cmp_equal` (voir [section 6](#6-opérateurs-et-expressions)).
- Préférez les **casts nommés** aux casts à la C ; chaque cast est un signal d'alerte à relire.
- Utilisez `const` et `constexpr` dès que possible.

---

# 5. Constantes et littéraux

## 5.1 Littéraux

| Type | Exemples |
| --- | --- |
| Entier décimal | `42`, `-7` |
| Entier octal / hexadécimal | `052`, `0x2A` |
| Entier binaire *(C++14)* | `0b101010` |
| Séparateur de chiffres *(C++14)* | `1'000'000`, `0b1010'0101` |
| Suffixes entiers | `42u`, `42L`, `42ul`, `42ll`, `42uz` *(C++23, `size_t`)* |
| Réel | `3.14`, `2.5e-3`, `1.0f` (float), `1.0L` (long double) |
| Booléen | `true`, `false` |
| Pointeur nul | `nullptr` |
| Caractère | `'A'`, `'\n'`, `u8'a'` *(C++17)*, `U'é'` |
| Chaîne | `"texte"` (type `const char[N]`), `u8"é"`, `L"large"` |
| Chaîne brute | `R"(C:\chemin\sans\échappement)"` |
| Littéraux de bibliothèque | `"abc"s` (`std::string`), `"abc"sv` (`std::string_view`), `250ms`, `2h`, `3i` (complexe) |

```cpp
#include <chrono>
#include <iostream>
#include <string>
#include <string_view>

using namespace std::literals;                     // pour les suffixes s, sv, ms, h...

int main() {
    auto s = "bonjour"s;                           // std::string
    auto v = "bonjour"sv;                          // std::string_view
    auto delai = 250ms;                            // std::chrono::milliseconds
    auto brut = R"(ligne 1\nligne 2)";             // '\n' est conservé tel quel
    std::cout << s.size() << ' ' << v.size() << ' ' << delai.count() << ' ' << brut << '\n';
    return 0;
}
```

### Séquences d'échappement

| Séquence | Signification |
| --- | --- |
| `\n` | Saut de ligne |
| `\t` | Tabulation |
| `\\` | Barre oblique inverse |
| `\"` | Guillemet |
| `\'` | Apostrophe |
| `\0` | Caractère nul |
| `\r` | Retour chariot |
| `\xHH` | Valeur hexadécimale |
| `\uXXXX` | Caractère Unicode (16 bits) |

### Littéraux définis par l'utilisateur *(C++11, ajout)*

```cpp
#include <iostream>

constexpr long double operator""_km(long double x) { return x * 1000.0L; }   // convertit en mètres

int main() {
    std::cout << 2.5_km << " m\n";       // 2500 m
    return 0;
}
```

## 5.2 Définir des constantes

| Mot-clé | Rôle | Évaluation |
| --- | --- | --- |
| `const` | Valeur **non modifiable** après initialisation | Exécution (parfois compilation) |
| `constexpr` *(C++11)* | Constante **calculable à la compilation** ; s'applique aussi aux fonctions | Compilation (si possible) |
| `consteval` *(C++20)* | Fonction **obligatoirement** évaluée à la compilation | Compilation |
| `constinit` *(C++20)* | Initialisation statique garantie à la compilation (la variable reste modifiable) | Compilation |
| `enum` | Famille de constantes entières nommées | Compilation |
| `#define` | Macro textuelle : **à éviter** | Préprocesseur |

```cpp
#include <array>
#include <iostream>

#define PI_MACRO 3.14159                   // sans point-virgule ! pas de type, pas de portée
constexpr double PI = 3.14159;             // recommandé : typé, dans une portée
constexpr int TAILLE = 4;

constexpr int carre(int x) { return x * x; }        // utilisable à la compilation ET à l'exécution
consteval int cube(int x) { return x * x * x; }     // uniquement à la compilation

int main() {
    const int n = 10;
    // n = 20;                              // ERREUR : constante
    std::array<int, carre(TAILLE)> t{};     // taille calculée à la compilation : 16
    constexpr int c = cube(3);              // 27
    std::cout << PI_MACRO << ' ' << PI << ' ' << n << ' ' << t.size() << ' ' << c << '\n';
    return 0;
}
```

> **Bonne pratique** : Préférez `constexpr` (ou `const`) et `enum class` aux macros `#define`.

## 5.3 `const` et pointeurs, `const` et références

```cpp
#include <iostream>

int main() {
    int x = 10, y = 20;

    const int *p1 = &x;          // pointeur vers une CONSTANTE : on ne modifie pas *p1
    int *const p2 = &x;          // pointeur CONSTANT : on ne modifie pas p2
    const int *const p3 = &x;    // les deux

    // *p1 = 5;                  // ERREUR
    p1 = &y;                     // OK
    *p2 = 5;                     // OK
    // p2 = &y;                  // ERREUR
    (void)p3;

    const int &r = x;            // référence constante : lecture seule
    // r = 3;                    // ERREUR
    std::cout << *p1 << ' ' << *p2 << ' ' << r << '\n';
    return 0;
}
```

Règle de lecture : on lit la déclaration **de droite à gauche** (`int *const p` : « p est un pointeur constant vers int »).

## 5.4 Constantes prédéfinies utiles

```cpp
#include <cstdlib>
#include <iostream>
#include <limits>
#include <numbers>

int main() {
    std::cout << std::numeric_limits<int>::max() << '\n';          // plus grand int
    std::cout << std::numeric_limits<double>::min() << '\n';       // plus petit double positif normalisé
    std::cout << std::numeric_limits<double>::infinity() << '\n';  // inf
    std::cout << std::numbers::pi << '\n';                         // pi (C++20)
    std::cout << std::numbers::e << '\n';                          // e (C++20)
    std::cout << EXIT_SUCCESS << ' ' << EXIT_FAILURE << '\n';      // 0 1
    return 0;
}
```

| Constante | En-tête | Signification |
| --- | --- | --- |
| `std::numeric_limits<T>::max()` / `min()` / `lowest()` | `<limits>` | Limites du type `T` |
| `std::numeric_limits<T>::epsilon()` | `<limits>` | Plus petit écart relatif d'un type flottant |
| `std::numbers::pi`, `e`, `sqrt2`… *(C++20)* | `<numbers>` | Constantes mathématiques |
| `INT_MAX`, `CHAR_BIT`… | `<climits>` | Équivalents hérités du C |
| `EXIT_SUCCESS`, `EXIT_FAILURE` | `<cstdlib>` | Codes de sortie |
| `__cplusplus` | (prédéfinie) | Numéro de la norme (`202002L`, `202302L`…) |

---

# 6. Opérateurs et expressions

## 6.1 Catégories

| Catégorie | Opérateurs |
| --- | --- |
| Arithmétiques | `+` `-` `*` `/` `%` |
| Relationnels | `==` `!=` `<` `>` `<=` `>=` et `<=>` (comparaison à trois voies, **C++20**) |
| Logiques | `&&` `\|\|` `!` (ou `and` `or` `not`) |
| Bit à bit | `&` `\|` `^` `~` `<<` `>>` |
| Affectation | `=` `+=` `-=` `*=` `/=` `%=` `<<=` `>>=` `&=` `\|=` `^=` |
| Incrémentation | `++` `--` (préfixe et suffixe) |
| Conditionnel | `? :` |
| Taille, type | `sizeof` `alignof` `typeid` |
| Mémoire | `new` `new[]` `delete` `delete[]` |
| Accès, portée | `::` `.` `->` `.*` `->*` `[]` `()` |
| Exceptions | `throw` |
| Virgule | `,` |

```cpp
#include <compare>
#include <iostream>

int main() {
    int a = 17, b = 5;
    std::cout << a + b << ' ' << a - b << ' ' << a * b << ' ' << a / b << ' ' << a % b << '\n';   // 22 12 85 3 2
    std::cout << (a > b) << (a == b) << (a != b) << '\n';                                         // 101
    a += 3;                            // a = 20
    a <<= 1;                           // a = 40
    std::cout << a << '\n';

    auto r = (3 <=> 5);                // std::strong_ordering::less
    std::cout << (r < 0) << '\n';      // 1
    return 0;
}
```

> **Remarque** : Le `%` ne s'applique qu'aux entiers. Pour les réels, utilisez `std::fmod` de `<cmath>`.

## 6.2 Incrémentation : préfixe et suffixe

```cpp
#include <iostream>

int main() {
    int i = 5;
    int a = i++;       // suffixe : a = 5 (ancienne valeur), puis i = 6
    int b = ++i;       // préfixe : i = 7, puis b = 7
    std::cout << a << ' ' << b << ' ' << i << '\n';     // 5 7 7
    return 0;
}
```

> **Bonne pratique** : Utilisez `++i` par défaut : pour les itérateurs et les objets, la forme suffixe crée une copie temporaire inutile.

## 6.3 Opérateurs logiques et évaluation paresseuse

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
    return 0;
}
```

## 6.4 Ternaire

```cpp
#include <iostream>

int main() {
    int a = 8, b = 3;
    int max = (a > b) ? a : b;
    std::cout << "max = " << max << '\n';
    std::cout << (a % 2 == 0 ? "pair" : "impair") << '\n';
    return 0;
}
```

> **Remarque** : Les deux branches doivent avoir des types compatibles (ou convertibles vers un type commun).

## 6.5 `sizeof`, `alignof` et opérateur virgule

```cpp
#include <iostream>
#include <iterator>

int main() {
    int t[10];
    std::cout << sizeof(int) << ' ' << sizeof t << ' ' << sizeof t / sizeof t[0] << '\n';   // 4 40 10
    std::cout << std::size(t) << '\n';        // 10 : plus sûr (C++17), échoue à la compilation sur un pointeur
    std::cout << alignof(double) << '\n';     // 8 : contrainte d'alignement

    int x = (1, 2, 3);                        // virgule : évalue tout, vaut la dernière valeur (3)
    for (int i = 0, j = 10; i < j; ++i, --j) {}   // usage classique dans un for
    std::cout << x << '\n';
    return 0;
}
```

## 6.6 Priorité et associativité

| Niveau | Opérateurs | Associativité |
| --- | --- | --- |
| 1 | `::` | G -> D |
| 2 | suffixes : `()` `[]` `.` `->` `++` `--` | G -> D |
| 3 | préfixes : `++` `--` `+` `-` `!` `~` `*` `&` `sizeof` `new` `delete` `(T)` | D -> G |
| 4 | `.*` `->*` | G -> D |
| 5 | `*` `/` `%` | G -> D |
| 6 | `+` `-` | G -> D |
| 7 | `<<` `>>` | G -> D |
| 8 | `<=>` *(C++20)* | G -> D |
| 9 | `<` `<=` `>` `>=` | G -> D |
| 10 | `==` `!=` | G -> D |
| 11 | `&` | G -> D |
| 12 | `^` | G -> D |
| 13 | `\|` | G -> D |
| 14 | `&&` | G -> D |
| 15 | `\|\|` | G -> D |
| 16 | `? :` `=` `+=` … `throw` | D -> G |
| 17 | `,` | G -> D |

> **Remarque** : Dans l'expression `std::cout << a & b`, `<<` est plus prioritaire que `&` : écrivez `std::cout << (a & b)`. Dans le doute, **parenthésez**.

## 6.7 Comportements à éviter

```cpp
#include <cmath>
#include <iostream>
#include <utility>

int main() {
    int x = 3;
    // x = x++ + ++x;          // comportement indéfini : modifications non séquencées
    // int d = 10 / 0;         // comportement indéfini : division entière par zéro
    // int s = 1 << 40;        // comportement indéfini : décalage >= largeur du type

    int a = -1;
    unsigned b = 1;
    std::cout << (a < b) << '\n';                 // 0 ! (a est converti en unsigned : 4294967295)
    std::cout << std::cmp_less(a, b) << '\n';     // 1 : comparaison correcte (C++20)

    double d = 0.1 + 0.2;
    std::cout << (d == 0.3) << '\n';                              // 0 : erreurs d'arrondi
    std::cout << (std::abs(d - 0.3) < 1e-9) << '\n';              // 1 : comparaison avec tolérance
    std::cout << x << '\n';
    return 0;
}
```

| Problème | Conséquence |
| --- | --- |
| Débordement d'entier **signé** | Comportement indéfini |
| Division / modulo par zéro (entiers) | Comportement indéfini |
| Décalage négatif ou trop grand | Comportement indéfini |
| Modifier deux fois une variable sans point de séquence | Comportement indéfini |
| Comparaison signé / non signé | Résultat surprenant |
| `==` sur des flottants | Erreurs d'arrondi |

> **Remarque** : Depuis C++17, l'ordre d'évaluation est défini pour `a << b`, `a >> b`, `a = b`, `a.f(b)` ou `a[b]` (le membre de gauche est évalué d'abord), mais **pas** pour les arguments d'une fonction ni pour les opérandes de `+`.

## 6.8 Arithmétique vérifiée et saturée *(ajout)*

Le C++ standard n'offre pas (encore) l'équivalent de `ckd_add` / `ckd_mul` du C23. On dispose en revanche d'outils pour détecter ou maîtriser les débordements.

```cpp
#include <cstdint>
#include <iostream>
#include <limits>
#include <numeric>
#include <utility>

int main() {
    int x = std::numeric_limits<int>::max();
    int r;
    if (__builtin_add_overflow(x, 1, &r)) {                   // extension GCC / Clang (pas standard)
        std::cout << "débordement détecté\n";
    }

    std::cout << std::in_range<std::uint8_t>(300) << '\n';    // 0 : 300 ne tient pas dans un uint8_t (C++20)
    std::cout << std::in_range<std::uint8_t>(200) << '\n';    // 1

    std::cout << static_cast<int>(std::add_sat<std::uint8_t>(250, 10)) << '\n';   // 255 : saturation (C++26)
    return 0;
}
```

| Outil | Rôle |
| --- | --- |
| `std::in_range<T>(v)` *(C++20)* | Teste si `v` est représentable dans `T` |
| `std::cmp_less`, `cmp_equal`… *(C++20)* | Comparaisons sûres entre entiers signés et non signés |
| `std::add_sat`, `sub_sat`, `mul_sat`, `div_sat` *(C++26)* | Arithmétique **saturée** (résultat borné au lieu de déborder) |
| `__builtin_*_overflow` | Détection de débordement (extension GCC / Clang) |
| Bibliothèques (Boost.SafeNumerics, etc.) | Entiers vérifiés |

---

# 7. Entrées et sorties

## 7.1 Affichage : `std::cout`, `std::format` et `std::println`

```cpp
#include <format>
#include <iomanip>
#include <iostream>
#include <string>

int main() {
    int n = 42;
    double pi = 3.14159265;

    std::cout << "n = " << n << ", pi = " << pi << '\n';             // chaîner les <<
    std::cout << std::fixed << std::setprecision(2) << pi << '\n';   // 3.14
    std::cout << std::setw(8) << n << '|' << std::left << std::setw(8) << n << "|\n";   //       42|42      |
    std::cout << std::hex << n << std::dec << '\n';                  // 2a

    std::string ligne = std::format("{:>8}|{:<8}|{:^8}|", n, n, n); // C++20
    std::cout << ligne << '\n';
    return 0;
}
```

Version moderne avec `std::println` *(C++23)* :

```cpp
#include <print>

int main() {
    double pi = 3.14159265;
    std::println("{:08.3f} {:#x} {:b} {:+d}", pi, 255, 5, 7);   // 0003.142 0xff 101 +7
    std::println(stderr, "message d'erreur");                   // vers un flux C (stderr)
}
```

### Spécificateurs de format (`std::format` / `std::print`)

| Spécification | Effet | Exemple |
| --- | --- | --- |
| `{}` | Format par défaut | `{}` avec `42` -> `42` |
| `{:d}` | Entier décimal | `42` |
| `{:x}` / `{:X}` | Hexadécimal | `ff` / `FF` |
| `{:#x}` | Hexadécimal avec préfixe | `0xff` |
| `{:b}` | Binaire | `101` |
| `{:f}` / `{:.2f}` | Réel à virgule fixe | `3.14` |
| `{:e}` | Notation scientifique | `3.14e+00` |
| `{:s}` / `{:c}` | Chaîne / caractère | `texte` / `A` |
| `{:>10}` `{:<10}` `{:^10}` | Aligné à droite / gauche / centré (largeur 10) | |
| `{:*^10}` | Centré, rempli avec `*` | `***abc****` |
| `{:08d}` | Rempli de zéros | `00000042` |
| `{:+d}` | Signe toujours affiché | `+7` |
| `{1} {0}` | Arguments par position | |

> **Remarque** : `std::format` et `std::print` sont **vérifiés à la compilation** (nombre et types des arguments), contrairement à `printf`. Leur disponibilité dépend de la version de votre bibliothèque standard (`std::format` : GCC 13+, `std::print` : GCC 14+, Clang/MSVC récents).

## 7.2 Lecture : `std::cin`

```cpp
#include <cstdlib>
#include <iostream>
#include <string>

int main() {
    int age;
    double taille;
    std::cout << "Âge et taille : ";
    if (!(std::cin >> age >> taille)) {               // échec de lecture : le flux passe en erreur
        std::cerr << "Entrée invalide\n";
        return EXIT_FAILURE;
    }
    std::cout << "Âge = " << age << ", taille = " << taille << '\n';

    std::string mot;
    std::cin >> mot;                                  // lit UN mot (s'arrête à l'espace) ; pas de dépassement possible
    std::cout << "mot = " << mot << '\n';
    return 0;
}
```

> **Remarque** : `std::cin >> x` saute les espaces, lit jusqu'au premier caractère invalide et laisse le reste (dont le `\n`) dans le tampon. Si la lecture échoue, le flux passe en état d'erreur et **toutes** les lectures suivantes échouent tant qu'il n'est pas réinitialisé avec `clear()`.

## 7.3 Lire une ligne : `std::getline` *(à jour)*

```cpp
#include <iostream>
#include <string>

int main() {
    std::string nom;
    std::cout << "Votre nom complet : ";
    std::getline(std::cin, nom);                      // lit toute la ligne (espaces compris), sans le '\n'
    std::cout << "Bonjour, " << nom << " !\n";
    return 0;
}
```

La `std::string` s'agrandit automatiquement : il n'y a **aucun tampon à dimensionner** (fin des risques de dépassement du C).

### Lecture sûre d'un nombre

```cpp
#include <charconv>
#include <iostream>
#include <optional>
#include <string>

std::optional<int> lire_int(const std::string &invite) {
    std::string ligne;
    std::cout << invite;
    if (!std::getline(std::cin, ligne)) return std::nullopt;          // fin de fichier ou erreur

    int valeur{};
    const char *debut = ligne.data();
    const char *fin = debut + ligne.size();
    auto [ptr, ec] = std::from_chars(debut, fin, valeur);             // pas d'exception, pas d'allocation
    if (ec != std::errc{} || ptr != fin) return std::nullopt;         // erreur, dépassement ou caractères en trop
    return valeur;
}

int main() {
    if (auto n = lire_int("Un entier : ")) {
        std::cout << "double = " << *n * 2 << '\n';
    } else {
        std::cout << "Entrée invalide\n";
    }
    return 0;
}
```

### Vider le tampon d'entrée

```cpp
#include <iostream>
#include <limits>
#include <string>

int main() {
    int n;
    std::cout << "Un entier : ";
    std::cin >> n;                                                    // laisse '\n' dans le tampon
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');   // jette le reste de la ligne

    std::string phrase;
    std::cout << "Une phrase : ";
    std::getline(std::cin, phrase);                                   // fonctionne maintenant
    std::cout << n << " / " << phrase << '\n';

    if (!std::cin) {                                                  // récupération après une erreur de format
        std::cin.clear();                                             // 1. remet le flux en état « bon »
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');   // 2. vide la ligne fautive
    }
    return 0;
}
```

## 7.4 Autres fonctions d'E/S

| Fonction | Rôle |
| --- | --- |
| `std::cout.put(c)` | Écrit un caractère |
| `std::cout.write(p, n)` | Écrit `n` octets |
| `std::cin.get()` | Lit un caractère (espaces compris) |
| `std::cin.peek()` | Consulte le caractère suivant sans le consommer |
| `std::cin >> std::ws` | Saute les espaces |
| `std::flush` | Vide le tampon de sortie |
| `std::endl` | `'\n'` **puis** `flush` : plus lent, préférer `'\n'` |
| `std::printf`, `std::scanf` (`<cstdio>`) | Fonctions du C, valides mais **non typées** : à éviter |
| `std::ios::sync_with_stdio(false)` | Accélère les flux (interdit de mélanger ensuite avec `printf`) |

## 7.5 Flux standard

| Flux | Rôle | Tamponné |
| --- | --- | --- |
| `std::cin` | Entrée standard (clavier) | oui |
| `std::cout` | Sortie standard (écran) | oui |
| `std::cerr` | Erreurs | **non** (immédiat) |
| `std::clog` | Journal (erreurs) | oui |

```bash
./prog > sortie.txt 2> erreurs.txt      # redirige cout et cerr séparément
./prog < entree.txt                     # cin lit dans le fichier
```

## 7.6 Erreurs courantes

| Erreur | Conséquence | Correction |
| --- | --- | --- |
| Mélanger `>>` et `getline` sans `ignore` | `getline` lit une ligne vide | `cin.ignore(...)` après `>>` |
| Ne pas tester la lecture | Boucle infinie, valeurs nulles | `if (std::cin >> x)` |
| Oublier `clear()` après une erreur | Toutes les lectures échouent | `clear()` puis `ignore()` |
| `std::endl` partout | Programme lent | `'\n'` |
| `std::cout << x << std::endl << y` mal formé | Résultat confus | Une insertion par valeur |
| `printf("%d", variable_double)` | Comportement indéfini | Flux ou `std::format` |

---

# 8. Structures de contrôle

## 8.1 Conditions : `if`, `else if`, `else`

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
    if (auto it = stock.find("pomme"); it != stock.end()) {     // initialiseur dans if (C++17)
        std::cout << "pommes : " << it->second << '\n';
    }                                                           // 'it' n'existe plus ici

    if constexpr (sizeof(void *) == 8) {                        // condition évaluée à la compilation (C++17)
        std::cout << "64 bits\n";
    }
    return 0;
}
```

## 8.2 `switch`

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

    switch (int reste = jour % 2; reste) {       // initialiseur dans switch (C++17)
        case 0: std::cout << "pair\n"; break;
        default: std::cout << "impair\n"; break;
    }
    return 0;
}
```

> **Attention** : Sans `break`, l'exécution **continue** dans le `case` suivant. Si c'est voulu, écrivez `[[fallthrough]];`. Le `switch` ne fonctionne que sur des entiers, des caractères et des énumérations (pas sur les chaînes).

## 8.3 Boucles

```cpp
#include <iostream>
#include <ranges>
#include <vector>

int main() {
    int i = 0;
    while (i < 3) { std::cout << i++ << ' '; }              // 0 1 2
    std::cout << '\n';

    do { std::cout << "exécuté au moins une fois\n"; } while (false);

    for (int k = 0; k < 3; ++k) std::cout << k << ' ';      // for classique
    std::cout << '\n';

    std::vector<int> v{10, 20, 30};
    for (int x : v) std::cout << x << ' ';                  // for sur intervalle (C++11) : copie
    for (const int &x : v) std::cout << x << ' ';           // lecture sans copie
    for (int &x : v) x *= 2;                                // modification en place
    std::cout << '\n';

    for (int k : std::views::iota(1, 4)) std::cout << k << ' ';        // 1 2 3 (C++20)
    for (int x : v | std::views::reverse) std::cout << x << ' ';       // parcours inversé (C++20)
    std::cout << '\n';
    return 0;
}
```

### Boucle infinie

```cpp
#include <iostream>

int main() {
    int n = 0;
    while (true) {                    // ou for (;;)
        if (++n > 3) break;
        std::cout << n << ' ';
    }
    std::cout << '\n';
    return 0;
}
```

## 8.4 `break`, `continue`, `goto`

```cpp
#include <iostream>

int main() {
    for (int i = 0; i < 10; ++i) {
        if (i == 3) continue;         // passe à l'itération suivante
        if (i == 6) break;            // quitte la boucle
        std::cout << i << ' ';        // 0 1 2 4 5
    }
    std::cout << '\n';

    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (i * j == 2) goto fin;           // sortir de deux boucles imbriquées
        }
    }
fin:
    std::cout << "sorti\n";
    return 0;
}
```

> **Remarque** : Le `goto` ne peut **pas** sauter par-dessus l'initialisation d'une variable. Le schéma C « `goto nettoyage;` » est inutile en C++ : la libération des ressources est automatique grâce aux destructeurs (RAII, [section 10.4](#104-raii-et-durée-de-vie-des-objets-ajout)). Pour sortir de boucles imbriquées, préférez une fonction avec `return`.

## 8.5 Boucles imbriquées

```cpp
#include <iomanip>
#include <iostream>

int main() {
    for (int i = 1; i <= 3; ++i) {
        for (int j = 1; j <= 3; ++j) {
            std::cout << std::setw(3) << i * j;
        }
        std::cout << '\n';
    }
    return 0;
}
```

## 8.6 Pièges classiques

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v{1, 2, 3};

    for (int i = 0; i < 3; ++i);                     // ';' en trop : la boucle ne fait rien
    { std::cout << "exécuté une seule fois\n"; }

    // for (std::size_t i = v.size() - 1; i >= 0; --i)   // boucle infinie : un non signé est toujours >= 0
    for (std::size_t i = v.size(); i-- > 0; ) std::cout << v[i] << ' ';   // idiome correct
    std::cout << '\n';

    for (int x : v) {
        // v.push_back(x);        // modifier le conteneur pendant le parcours invalide les itérateurs
        (void)x;
    }

    for (auto x : std::vector<std::string>{"a", "b"}) { (void)x; }    // copie chaque chaîne : préférer const auto &
    return 0;
}
```

## 8.7 Exceptions : `try`, `catch`, `throw` *(ajout)*

Une **exception** signale une erreur en interrompant le flot normal : le programme remonte la pile d'appels (en détruisant les objets locaux) jusqu'au premier `catch` compatible.

```cpp
#include <iostream>
#include <stdexcept>

double diviser(double a, double b) {
    if (b == 0.0) throw std::invalid_argument("division par zéro");   // lève une exception
    return a / b;
}

int main() {
    try {
        std::cout << diviser(10, 2) << '\n';           // 5
        std::cout << diviser(1, 0) << '\n';            // lève : la suite du bloc try est ignorée
    } catch (const std::invalid_argument &e) {         // capture par référence constante
        std::cerr << "Argument invalide : " << e.what() << '\n';
    } catch (const std::exception &e) {                // toute exception standard
        std::cerr << "Erreur : " << e.what() << '\n';
    } catch (...) {                                    // n'importe quoi d'autre
        std::cerr << "Erreur inconnue\n";
    }
    return 0;
}
```

| Classe | Signification |
| --- | --- |
| `std::exception` | Base de toutes les exceptions standard (`what()`) |
| `std::logic_error` | Erreur de logique : `invalid_argument`, `out_of_range`, `domain_error`, `length_error` |
| `std::runtime_error` | Erreur d'exécution : `range_error`, `overflow_error`, `underflow_error` |
| `std::bad_alloc` | Échec d'allocation mémoire |
| `std::bad_cast` | Échec de `dynamic_cast` sur une référence |

Règles essentielles : **lancer par valeur, capturer par référence constante**, ordonner les `catch` du plus spécifique au plus général. La garantie de sûreté (`noexcept`, RAII) est traitée en [section 29.4](#294-exceptions-et-sûreté-ajout).

---

# 9. Fonctions

## 9.1 Définir et appeler

```cpp
#include <iostream>
#include <string>

int somme(int a, int b) { return a + b; }                        // type de retour, nom, paramètres
auto produit(int a, int b) { return a * b; }                     // type de retour déduit (C++14)
auto moyenne(int a, int b) -> double { return (a + b) / 2.0; }   // type de retour final

void afficher(const std::string &msg) {                          // void : ne retourne rien
    std::cout << msg << '\n';
}

[[nodiscard]] bool est_pair(int n) { return n % 2 == 0; }

int main() {
    afficher("Bonjour");
    std::cout << somme(2, 3) << ' ' << produit(2, 3) << ' ' << moyenne(2, 3) << ' ' << est_pair(4) << '\n';
    return 0;
}
```

Une fonction doit être **déclarée avant son premier appel** (prototype) :

```cpp
#include <iostream>

int carre(int x);                    // déclaration (prototype)

int main() {
    std::cout << carre(6) << '\n';   // 36
    return 0;
}

int carre(int x) { return x * x; }   // définition
```

## 9.2 Passage des arguments : valeur, référence, pointeur

Par défaut, les arguments sont passés **par valeur** (copie). Le C++ ajoute le passage **par référence** (voir [section 17](#17-références-et-pointeurs-doubles)) qui évite la copie et permet de modifier l'original.

```cpp
#include <iostream>
#include <string>

void incremente_copie(int x) { ++x; }                       // modifie la copie : sans effet
void incremente_ref(int &x) { ++x; }                        // modifie l'original
void incremente_ptr(int *x) { if (x) ++*x; }                // modifie l'original via un pointeur
std::size_t longueur(const std::string &s) { return s.size(); }   // lecture sans copie

void echange(int &a, int &b) { int t = a; a = b; b = t; }   // (ou std::swap)

int main() {
    int n = 1;
    incremente_copie(n); std::cout << n << ' ';             // 1
    incremente_ref(n);   std::cout << n << ' ';             // 2
    incremente_ptr(&n);  std::cout << n << '\n';            // 3

    int a = 1, b = 2;
    echange(a, b);
    std::cout << a << ' ' << b << ' ' << longueur("abc") << '\n';   // 2 1 3
    return 0;
}
```

| Cas | Passage recommandé | Exemple |
| --- | --- | --- |
| Petit type (`int`, `double`, pointeur, `string_view`, `span`) | **Valeur** | `double racine(double x)` |
| Gros objet en **lecture** | `const T &` | `void afficher(const std::string &s)` |
| Modifier l'argument | `T &` | `void trier(std::vector<int> &v)` |
| Résultat | **Valeur de retour** (struct, `tuple`, `optional`) | `std::pair<int,int> minmax(...)` |
| Argument optionnel | Pointeur ou `std::optional` | `void f(const Config *c)` |
| Consommer / stocker l'objet (*sink*) | Par valeur puis `std::move`, ou `T &&` | `void ajoute(std::string s)` |

## 9.3 Plusieurs fichiers : en-têtes et sources

`maths.hpp` : **déclarations**

```cpp
// maths.hpp
#pragma once                                    // garde d'inclusion (voir section 24.5)

namespace maths {
    int carre(int x);                           // déclaration : la définition est dans maths.cpp
    inline int cube(int x) { return x * x * x; }   // inline : définition autorisée dans l'en-tête
}
```

`maths.cpp` : **définitions**

```cpp
// maths.cpp
#include "maths.hpp"

namespace maths {
    int carre(int x) { return x * x; }
}
```

`main.cpp`

```cpp
// main.cpp
#include <iostream>
#include "maths.hpp"

int main() {
    std::cout << maths::carre(5) << ' ' << maths::cube(2) << '\n';   // 25 8
    return 0;
}
```

```bash
g++ -Wall -Wextra -std=c++20 main.cpp maths.cpp -o prog
```

Ce que l'on place dans un en-tête : déclarations, définitions de classes, **templates**, fonctions `inline` et `constexpr`, constantes. Une fonction ordinaire définie dans un en-tête inclus par deux fichiers provoque une erreur d'édition de liens (violation de la **règle de la définition unique**, ODR).

Pour appeler du C depuis du C++ (ou l'inverse), on désactive le décorage des noms :

```cpp
extern "C" {
    #include "bibliotheque_c.h"        // fonctions C : liaison C, sans mangling
}
```

## 9.4 Surcharge et arguments par défaut *(ajout)*

Plusieurs fonctions peuvent porter le **même nom** si leurs **paramètres** diffèrent (nombre ou types). Le compilateur choisit la meilleure correspondance.

```cpp
#include <iostream>
#include <string>

int    absolu(int x)    { return x < 0 ? -x : x; }
double absolu(double x) { return x < 0 ? -x : x; }

void afficher(const std::string &s, int fois = 1, char sep = '\n') {      // arguments par défaut
    for (int i = 0; i < fois; ++i) std::cout << s << sep;
}

int main() {
    std::cout << absolu(-3) << ' ' << absolu(-2.5) << '\n';   // int puis double
    afficher("a");                                            // fois = 1, sep = '\n'
    afficher("b", 2);
    afficher("c", 2, ' ');
    std::cout << '\n';
    return 0;
}
```

- Le **type de retour seul** ne suffit pas à distinguer deux surcharges.
- Les arguments par défaut se placent à la **fin** de la liste et se déclarent une seule fois (dans le prototype).
- Une conversion ambiguë (`absolu(3L)` avec `int` et `double`) provoque une erreur : levez l'ambiguïté par un cast.

## 9.5 Fonctions variadiques

L'ellipse `...` du C (`<cstdarg>`) n'est pas typée : elle est **déconseillée**. Le C++ propose des alternatives sûres.

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
    std::cout << somme({1, 2, 3, 4}) << '\n';              // 10
    std::cout << somme_t(1, 2, 3.5) << '\n';               // 6.5
    afficher_tout("x =", 5, 'c', 2.5);                     // x = 5 c 2.5
    return 0;
}
```

## 9.6 `inline`, `constexpr`, `consteval`, `noexcept` *(ajout)*

```cpp
#include <iostream>

constexpr int factorielle(int n) { return n <= 1 ? 1 : n * factorielle(n - 1); }   // utilisable à la compilation
static_assert(factorielle(5) == 120);                                              // vérifié à la compilation

consteval int au_carre(int x) { return x * x; }       // DOIT être évaluée à la compilation (C++20)

int addition(int a, int b) noexcept { return a + b; }   // promet de ne pas lever d'exception

int main() {
    constexpr int f = factorielle(6);                 // calculé par le compilateur
    int n = 4;
    std::cout << f << ' ' << factorielle(n) << ' ' << au_carre(5) << ' ' << addition(1, 2) << '\n';
    return 0;
}
```

| Mot-clé | Sens |
| --- | --- |
| `inline` | Autorise plusieurs définitions identiques (en-têtes) ; l'inlining effectif reste au choix du compilateur |
| `constexpr` | Fonction évaluable à la compilation si ses arguments le sont |
| `consteval` | Évaluation **obligatoire** à la compilation |
| `noexcept` | Garantie d'absence d'exception (permet des optimisations ; `std::terminate` en cas de violation) |

## 9.7 Fonctions et mémoire : points d'attention

```cpp
#include <string>

const std::string &mauvaise() {
    std::string local = "temporaire";
    return local;                          // DANGER : référence vers une variable détruite
}

std::string bonne() {
    std::string local = "ok";
    return local;                          // retour par valeur : élision de copie / déplacement, sans coût notable
}
```

- **Ne retournez jamais** une référence ou un pointeur vers une variable locale.
- Depuis **C++17**, retourner un objet temporaire (valeur pure) **n'effectue aucune copie** (élision garantie) ; le retour d'une variable locale nommée est optimisé (NRVO) ou déplacé.
- Les variables locales vivent sur la **pile**, de taille limitée : évitez les gros tableaux locaux et les récursions très profondes.
- Une variable locale `static` conserve sa valeur d'un appel à l'autre.

## 9.8 Bonnes pratiques

- Une fonction = **une tâche**, nom explicite, courte.
- Passez les gros objets par `const T &`, les petits par valeur ; retournez par valeur.
- Marquez `[[nodiscard]]` les fonctions dont le résultat importe, `noexcept` celles qui ne lèvent pas, `constexpr` celles qui peuvent l'être.
- Évitez les paramètres de sortie : retournez une `struct`, un `std::pair` / `std::tuple`, ou un `std::optional`.
- Documentez les préconditions (voir les contrats de C++26, [section 29.5](#295-contrats-et-bibliothèque-durcie-c26-ajout)).

---

# 10. Portée et durée de vie des variables

## 10.1 Les portées

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
    std::cout << x << ' ' << ::globale << '\n';       // 10 100  (:: = portée globale)

    for (int i = 0; i < 2; ++i) {}                    // 'i' n'existe que dans la boucle
    if (int y = x * 2; y > 5) {                       // 'y' limité au if / else
        std::cout << y << ' ' << app::config << '\n';
    }
    return 0;
}
```

| Portée | Où est-elle visible ? |
| --- | --- |
| **Bloc** `{ }` | Du point de déclaration à la fin du bloc |
| **Fonction** | Étiquettes (`goto`) : dans toute la fonction |
| **Fichier / espace de noms** | Du point de déclaration à la fin du fichier (ou de l'espace de noms) |
| **Classe** | Membres, accessibles via l'objet ou `Classe::` |
| **Énumération** | Valeurs d'un `enum class` : accessibles seulement via `Enum::valeur` |
| **Template** | Paramètres de template dans leur déclaration |

## 10.2 Classes de stockage et durée de vie

| Mot-clé | Durée de vie | Remarque |
| --- | --- | --- |
| *(aucun)* local | **Automatique** : bloc, sur la pile | Détruit à la sortie du bloc |
| `static` (local) | **Statique** : tout le programme | Initialisée une seule fois (thread-safe depuis C++11) |
| `static` (global) | Statique, visible dans le **fichier** seul | Préférer l'espace de noms anonyme |
| `extern` | Statique, définie ailleurs | Partage entre fichiers |
| `thread_local` *(C++11)* | Durée du **thread** | Une copie par thread |
| `inline` (variable) *(C++17)* | Statique | Définissable dans un en-tête |
| `mutable` | Membre modifiable dans un objet `const` | Cache, mutex… |
| `new` / `make_unique` | **Dynamique** : jusqu'à `delete` / destruction du propriétaire | Sur le tas |

```cpp
#include <iostream>

int compteur() {
    static int n = 0;               // initialisée une seule fois ; conserve sa valeur
    return ++n;
}

namespace {                         // espace de noms anonyme : visible dans ce fichier seulement
    int secret = 42;
}

inline constexpr int MAX = 100;     // variable inline (C++17) : utilisable dans un en-tête sans erreur de liaison

thread_local int par_thread = 0;    // chaque thread a sa propre copie

int main() {
    std::cout << compteur() << compteur() << compteur() << '\n';     // 123
    std::cout << secret << ' ' << MAX << ' ' << par_thread << '\n';
    return 0;
}
```

> **Attention** : L'**ordre d'initialisation** des variables globales de fichiers différents n'est pas défini (*static initialization order fiasco*). Évitez les globales qui dépendent les unes des autres ; une variable `static` locale à une fonction (initialisée au premier appel) règle le problème.

## 10.3 Organisation de la mémoire d'un programme

```text
Adresses hautes   +----------------------------+
                  | Pile (stack)               |  variables locales, appels ; croît vers le bas
                  +----------------------------+
                  |            ...             |
                  +----------------------------+
                  | Tas (heap)                 |  new, make_unique, conteneurs ; croît vers le haut
                  +----------------------------+
                  | Données (statiques)        |  variables globales et static
                  +----------------------------+
                  | Code (text)                |  instructions, constantes littérales
Adresses basses   +----------------------------+
```

| Zone | Contenu | Gestion |
| --- | --- | --- |
| **Pile** | Locales, paramètres, adresses de retour | Automatique (constructeurs / destructeurs appelés) |
| **Tas** | Objets alloués dynamiquement | Via `new` / `delete` ou, mieux, via **RAII** |
| **Données** | Variables globales et statiques | Durée du programme |
| **Code** | Instructions, littéraux de chaîne | Lecture seule |

## 10.4 RAII et durée de vie des objets *(ajout)*

En C++, un objet est **construit** à sa déclaration et **détruit** automatiquement à la fin de sa portée, dans l'**ordre inverse** de la construction. Ce mécanisme, nommé **RAII** (*Resource Acquisition Is Initialization*), lie la durée de vie d'une ressource (mémoire, fichier, verrou, connexion) à celle d'un objet.

```cpp
#include <iostream>
#include <string>
#include <utility>

class Trace {
    std::string nom_;
public:
    explicit Trace(std::string nom) : nom_(std::move(nom)) { std::cout << "construit " << nom_ << '\n'; }
    ~Trace() { std::cout << "détruit   " << nom_ << '\n'; }      // destructeur
};

int main() {
    Trace a{"A"};              // construit A
    {
        Trace b{"B"};          // construit B
    }                          // détruit B (fin du bloc)
    Trace c{"C"};              // construit C
    std::cout << "fin de main\n";
    return 0;
}                              // détruit C, puis détruit A (ordre inverse)
```

La destruction a lieu **même si une exception est levée** : c'est la base de la gestion fiable des ressources en C++ (conteneurs, `std::unique_ptr`, `std::ifstream`, `std::lock_guard`).

## 10.5 Bonnes pratiques

- Déclarez les variables dans la **plus petite portée** possible et initialisez-les immédiatement.
- Évitez les variables **globales** ; si nécessaire, mettez-les dans un `namespace` et rendez-les `const` ou `constexpr`.
- Évitez l'**ombrage** (`-Wshadow`).
- Ne gérez jamais une ressource à la main : encapsulez-la dans un objet RAII.
- Ne retournez jamais de référence ou de pointeur vers une variable automatique.

---

# Niveau intermédiaire

---

# 11. Tableaux

## 11.1 Déclarer et initialiser

```cpp
#include <array>
#include <iostream>
#include <vector>

int main() {
    int a[5] = {1, 2, 3};             // tableau « à la C » : 1 2 3 0 0 (le reste est mis à zéro)
    int b[] = {4, 5, 6};              // taille déduite : 3
    int zeros[10] = {};               // tout à 0

    std::array<int, 5> c{1, 2, 3};    // taille fixe connue à la compilation (C++11)
    std::vector<int> d{1, 2, 3};      // taille variable, éléments sur le tas

    std::cout << sizeof(a) / sizeof(a[0]) << ' ' << c.size() << ' ' << d.size() << '\n';   // 5 5 3
    (void)b; (void)zeros;
    return 0;
}
```

| | Tableau C `int t[N]` | `std::array<T, N>` | `std::vector<T>` |
| --- | --- | --- | --- |
| Taille | Fixe, connue à la compilation | Fixe, connue à la compilation | **Variable** (à l'exécution) |
| Stockage | Pile (ou statique) | Pile (ou statique) | Éléments sur le **tas** |
| `size()` | Non (`sizeof` / `std::size`) | Oui | Oui |
| Copie par `=` | **Impossible** | Oui | Oui (copie profonde) |
| Passage à une fonction | Se réduit à un pointeur | Par valeur ou référence | Par valeur ou référence |
| Accès vérifié | Non | `at()` | `at()` |
| Itérateurs | Pointeurs | Oui | Oui |

> **Bonne pratique** : Préférez `std::array` (taille fixe) et `std::vector` (taille variable) aux tableaux à la C.

## 11.2 Parcourir un tableau

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
    return 0;
}
```

## 11.3 Tableaux multidimensionnels

```cpp
#include <array>
#include <iostream>
#include <vector>

int main() {
    int m[2][3] = {{1, 2, 3}, {4, 5, 6}};                       // tableau C 2 x 3
    for (const auto &ligne : m) {
        for (int v : ligne) std::cout << v << ' ';
        std::cout << '\n';
    }

    std::array<std::array<int, 3>, 2> g{{{1, 2, 3}, {4, 5, 6}}};   // 2 lignes de 3
    std::vector<std::vector<int>> mat(3, std::vector<int>(4, 0));  // matrice dynamique 3 x 4 de zéros
    mat[1][2] = 9;

    std::cout << g[1][2] << ' ' << mat[1][2] << '\n';           // 6 9
    return 0;
}
```

> **Remarque** : Pour une matrice dense performante, stockez les données dans **un seul** `std::vector` (indice `i * colonnes + j`) ou utilisez `std::mdspan` *(C++23)*, qui offre une vue multidimensionnelle sur un tampon contigu.

## 11.4 Tableaux de taille variable

Les **VLA** du C99 (`int t[n];` avec `n` connu à l'exécution) **n'existent pas** en C++ standard (certains compilateurs les acceptent en extension, avec des risques de dépassement de pile). On utilise `std::vector` :

```cpp
#include <iostream>
#include <vector>

int main() {
    int n;
    std::cout << "Taille : ";
    if (!(std::cin >> n) || n < 0) return 1;

    std::vector<int> t(n);              // n éléments initialisés à 0
    std::vector<int> u(n, 7);           // n éléments égaux à 7
    for (int i = 0; i < n; ++i) t[i] = i * i;
    for (int x : t) std::cout << x << ' ';
    std::cout << '\n';
    return 0;
}                                       // mémoire libérée automatiquement
```

## 11.5 Tableaux et fonctions

Un tableau C passé à une fonction se **réduit à un pointeur** (*decay*) : sa taille est perdue.

```cpp
#include <array>
#include <iostream>
#include <span>
#include <vector>

int somme(std::span<const int> v) {                   // vue sur une suite contiguë d'int (C++20)
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
    return 0;
}
```

> **Attention** : `void f(int t[])` et `void f(int *t)` sont **identiques** ; dans `f`, `sizeof(t)` donne la taille d'un pointeur. Utilisez `std::span` (pointeur + taille) pour recevoir « n'importe quelle suite contiguë ».

## 11.6 Opérations courantes : la bibliothèque `<algorithm>`

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <numeric>
#include <vector>

int main() {
    std::vector<int> v{5, 2, 9, 1, 7};

    std::sort(v.begin(), v.end());                    // 1 2 5 7 9
    std::ranges::sort(v, std::greater{});             // 9 7 5 2 1 (version ranges, C++20)

    auto it = std::find(v.begin(), v.end(), 5);       // recherche linéaire
    if (it != v.end()) std::cout << "5 à l'indice " << it - v.begin() << '\n';

    int total = std::accumulate(v.begin(), v.end(), 0);                           // 24
    auto [mn, mx] = std::minmax_element(v.begin(), v.end());
    auto impairs = std::count_if(v.begin(), v.end(), [](int x) { return x % 2 != 0; });   // 5

    std::reverse(v.begin(), v.end());
    std::fill(v.begin(), v.begin() + 2, 0);           // met les deux premiers à 0
    std::cout << total << ' ' << *mn << ' ' << *mx << ' ' << impairs << '\n';
    return 0;
}
```

| Besoin | Outil |
| --- | --- |
| Trier | `std::sort`, `std::ranges::sort`, `std::stable_sort` |
| Chercher | `std::find`, `std::find_if`, `std::binary_search` (trié), `std::lower_bound` |
| Compter / tester | `std::count`, `std::count_if`, `std::any_of`, `std::all_of`, `std::none_of` |
| Copier / remplir | `std::copy`, `std::fill`, `std::iota`, `std::generate` |
| Réduire | `std::accumulate`, `std::reduce`, `std::transform_reduce` |
| Extrema | `std::min_element`, `std::max_element`, `std::minmax_element` |
| Supprimer | `v.erase(std::remove(...), v.end())` ou `std::erase(v, x)` (C++20) |

## 11.7 Erreurs courantes

| Erreur | Conséquence | Correction |
| --- | --- | --- |
| `t[n]` avec `n == taille` | Hors bornes (UB) | Indices de `0` à `taille - 1` ; `at()` en test |
| Compter avec `sizeof` sur un paramètre | Taille d'un pointeur | `std::span`, `std::size` ou `std::vector` |
| Modifier un `vector` pendant un `for` sur intervalle | Itérateurs invalidés (UB) | Parcours par indice, `erase`/`remove` |
| `v[0]` sur un vecteur vide | UB | Tester `empty()` |
| `std::vector<bool>` utilisé comme un vrai conteneur | Proxy bit à bit, pas de `bool &` | `std::vector<char>` ou `std::bitset` |
| Boucle `for (std::size_t i = n - 1; i >= 0; --i)` | Infinie | Parcours inverse correct (section 8.6) |

---

# 12. Chaînes de caractères

## 12.1 Définition

En C++, on utilise la classe `std::string` : elle gère sa mémoire, connaît sa taille et grandit toute seule. La chaîne « à la C » (tableau de `char` terminé par `'\0'`) reste utile pour l'interopérabilité.

```cpp
#include <iostream>
#include <string>

int main() {
    const char *c1 = "bonjour";          // chaîne C : pointeur vers un littéral (lecture seule)
    char c2[] = "bonjour";               // tableau de 8 char (avec '\0'), modifiable
    std::string s = "bonjour";           // chaîne C++ : taille dynamique

    s += " le monde";
    c2[0] = 'B';
    std::cout << c1 << ' ' << c2 << ' ' << s << ' ' << s.size() << '\n';   // bonjour Bonjour bonjour le monde 16
    return 0;
}
```

| | `const char *` / `char[]` | `std::string` |
| --- | --- | --- |
| Taille | Non mémorisée (`strlen`) | `size()` en temps constant |
| Mémoire | À gérer à la main | Automatique |
| Concaténation | `strcat` (risque de dépassement) | `+`, `+=`, `append` |
| Comparaison | `strcmp` | `==`, `<`, `compare` |
| Copie | `strcpy` | `=` |

## 12.2 Opérations de `std::string`

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

    s.insert(7, ",");                                           // Bonjour, le monde
    s.replace(9, 2, "LE");                                      // Bonjour, LE monde
    s.erase(7, 1);                                              // Bonjour LE monde
    std::cout << s << '\n';

    std::cout << s.starts_with("Bon") << s.ends_with("de") << '\n';   // 11 (C++20)
    std::cout << (std::string("a") < std::string("b")) << '\n';       // 1 : comparaison lexicographique
    return 0;
}
```

| Fonction | Rôle |
| --- | --- |
| `size()` / `length()`, `empty()`, `clear()` | Taille, test de vacuité, vidage |
| `operator[]`, `at(i)`, `front()`, `back()` | Accès (`at` vérifie les bornes) |
| `+`, `+=`, `append`, `push_back`, `insert` | Ajouter |
| `erase`, `pop_back`, `replace` | Supprimer, remplacer |
| `substr(pos, n)` | Sous-chaîne (copie) |
| `find`, `rfind`, `find_first_of`, `find_last_of` | Recherche (retourne `npos` si absent) |
| `compare`, `==`, `<`… | Comparaison |
| `starts_with`, `ends_with` *(C++20)*, `contains` *(C++23)* | Tests de préfixe, suffixe, inclusion |
| `c_str()`, `data()` | Accès à la chaîne C terminée par `'\0'` |
| `reserve`, `capacity`, `shrink_to_fit` | Gestion de la capacité |

## 12.3 Copier et concaténer en sécurité

```cpp
#include <format>
#include <iostream>
#include <string>
#include <string_view>

using namespace std::literals;

int main() {
    std::string prenom = "Ada", nom = "Lovelace";
    std::string complet = prenom + " " + nom;        // + : chaîne + littéral
    // std::string erreur = "a" + "b";               // ERREUR : deux const char *
    std::string ok = "a"s + "b";                     // "a"s est un std::string

    complet.append("!");
    std::string copie = complet;                     // copie profonde

    std::string_view vue = complet;                  // vue SANS copie (pointeur + taille)
    std::cout << vue.substr(0, 3) << '\n';           // Ada

    std::cout << std::format("{} ({} car.)", complet, complet.size()) << '\n';   // C++20
    std::cout << ok << copie << '\n';
    return 0;
}
```

> **Attention** : Un `std::string_view` ne possède **pas** ses données : il devient invalide si la chaîne d'origine est détruite ou modifiée. Utilisez-le surtout comme **paramètre** de fonction, pas comme valeur stockée.

## 12.4 Lire et parcourir une chaîne

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
    for (std::size_t pos = phrase.find(' '); pos != std::string::npos; pos = phrase.find(' ', pos + 1)) {
        ++espaces;
    }
    std::cout << espaces << " espaces\n";                          // 2

    std::istringstream flux(phrase);                               // découper en mots
    std::string mot;
    while (flux >> mot) std::cout << '<' << mot << '>';
    std::cout << '\n';

    for (auto morceau : phrase | std::views::split(' ')) {         // découpage avec les ranges (C++20)
        std::cout << std::string(morceau.begin(), morceau.end()) << '|';
    }
    std::cout << '\n';
    return 0;
}
```

La lecture au clavier ou dans un fichier avec `std::getline` est présentée en [section 7.3](#73-lire-une-ligne--stdgetline-à-jour) et [section 22](#22-gestion-des-fichiers).

## 12.5 Caractères : `<cctype>`

| Fonction | Teste / convertit |
| --- | --- |
| `std::isalpha(c)` | Lettre |
| `std::isdigit(c)` | Chiffre `0` à `9` |
| `std::isalnum(c)` | Lettre ou chiffre |
| `std::isspace(c)` | Espace, tabulation, saut de ligne |
| `std::isupper(c)` / `std::islower(c)` | Majuscule / minuscule |
| `std::ispunct(c)` | Ponctuation |
| `std::toupper(c)` / `std::tolower(c)` | Conversion de casse |

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
    return 0;
}
```

> **Attention** : Passez un `unsigned char` à ces fonctions : une valeur négative (caractère accentué codé sur un `char` signé) provoque un comportement indéfini. Elles ne gèrent que l'ASCII ; pour l'Unicode, voir [section 27](#27-unicode-et-caractères-larges).

## 12.6 Conversions chaîne <-> nombre

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
    return 0;
}
```

| Fonction | Rôle |
| --- | --- |
| `std::stoi`, `stol`, `stoll`, `stoul`, `stof`, `stod` | Chaîne -> nombre (**exceptions** en cas d'erreur) |
| `std::to_string(x)` | Nombre -> chaîne (format fixe, peu configurable) |
| `std::from_chars`, `std::to_chars` *(C++17)* | Conversions **rapides**, sans exception ni allocation |
| `std::format("{}", x)` *(C++20)* | Nombre -> chaîne avec options de format |

## 12.7 Tableau de chaînes

```cpp
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> noms{"Zoé", "Ana", "Marc"};
    noms.push_back("Luc");

    std::sort(noms.begin(), noms.end());                 // tri lexicographique
    for (const auto &n : noms) std::cout << n << ' ';    // Ana Luc Marc Zoé
    std::cout << '\n';
    return 0;
}
```

## 12.8 Les fonctions C de `<cstring>`

| Fonction | Rôle | Alternative C++ |
| --- | --- | --- |
| `strlen` | Longueur | `s.size()` |
| `strcpy`, `strncpy` | Copie | `=` |
| `strcat`, `strncat` | Concaténation | `+=` |
| `strcmp` | Comparaison | `==`, `compare` |
| `strchr`, `strstr` | Recherche | `find` |
| `memcpy`, `memset` | Copie / remplissage d'octets | `std::copy`, `std::fill` (types triviaux uniquement) |

```cpp
#include <cstdio>
#include <string>

int main() {
    std::string s = "interop C";
    std::puts(s.c_str());          // fonction C attendant un const char * : c_str() fournit le pointeur
    return 0;
}
```

## 12.9 Bonnes pratiques

- Utilisez `std::string` partout ; `std::string_view` pour les paramètres en lecture seule.
- Ne mélangez jamais `+` entre deux littéraux ; commencez par un `std::string` ou un suffixe `s`.
- Vérifiez `find(...) != std::string::npos` avant d'utiliser la position.
- Un `c_str()` n'est valable que tant que la chaîne n'est ni modifiée ni détruite.
- Convertissez avec `from_chars` ou `stoi` dans un `try` ; validez toujours les entrées utilisateur.

---

# 13. Pointeurs

## 13.1 Qu'est-ce qu'un pointeur ?

Un **pointeur** est une variable qui contient l'**adresse** d'un objet en mémoire.

```cpp
#include <iostream>

int main() {
    int x = 42;
    int *p = &x;                       // p contient l'adresse de x

    std::cout << x << ' ' << *p << ' ' << (p == &x) << '\n';       // 42 42 1
    std::cout << static_cast<const void *>(p) << '\n';             // affiche l'adresse (ex. 0x7ffd...)

    *p = 100;                          // modifie x via le pointeur
    std::cout << x << '\n';            // 100
    return 0;
}
```

| Symbole | Rôle |
| --- | --- |
| `&x` | Adresse de `x` |
| `T *p` | `p` est un pointeur vers `T` |
| `*p` | Déréférencement : l'objet pointé |
| `p->m` | Membre `m` de l'objet pointé (équivaut à `(*p).m`) |

## 13.2 Le pointeur nul : `nullptr`

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
    return 0;
}
```

> **Bonne pratique** : Utilisez `nullptr` (C++11), jamais `NULL` ni `0`. Initialisez tout pointeur (`= nullptr`) et testez-le avant de le déréférencer.

## 13.3 Arithmétique des pointeurs

```cpp
#include <cstddef>
#include <iostream>

int main() {
    int t[] = {10, 20, 30, 40};
    int *p = t;                                   // t se réduit à &t[0]

    std::cout << *p << ' ' << *(p + 1) << ' ' << p[2] << '\n';     // 10 20 30
    p += 3;
    std::cout << *p << '\n';                                       // 40
    std::ptrdiff_t d = &t[3] - &t[0];                              // 3 éléments d'écart
    std::cout << d << '\n';
    return 0;
}
```

`p + n` avance de `n` **éléments** (et non de `n` octets). L'arithmétique n'est valide qu'**à l'intérieur d'un même tableau** (ou un cran après le dernier élément, sans déréférencement).

## 13.4 Tableaux et pointeurs

```cpp
#include <iostream>

int main() {
    int t[5] = {1, 2, 3, 4, 5};
    int *p = t;

    std::cout << sizeof(t) << ' ' << sizeof(p) << '\n';     // 20 8 : un tableau n'est PAS un pointeur
    std::cout << (t[2] == *(t + 2)) << '\n';                // 1 : t[i] est défini comme *(t + i)
    return 0;
}
```

| | Tableau `int t[5]` | Pointeur `int *p` |
| --- | --- | --- |
| `sizeof` | Taille totale (20) | Taille du pointeur (8) |
| Affectation `= autre` | Impossible | Possible |
| Conversion implicite | En pointeur vers le 1ᵉʳ élément | n/a |

## 13.5 Pointeurs et fonctions

```cpp
#include <iostream>

void echange(int *a, int *b) {         // style C : on passe les adresses
    int t = *a; *a = *b; *b = t;
}

void echange_ref(int &a, int &b) {     // style C++ : références (voir section 17)
    int t = a; a = b; b = t;
}

int main() {
    int x = 1, y = 2;
    echange(&x, &y);
    echange_ref(x, y);
    std::cout << x << ' ' << y << '\n';    // 1 2 (deux échanges)
    return 0;
}
```

> **Bonne pratique** : Préférez les **références** quand l'argument est obligatoire ; réservez le pointeur aux arguments **optionnels** (`nullptr` possible).

## 13.6 `const` et pointeurs (rappel)

Voir la [section 5.3](#53-const-et-pointeurs-const-et-références). Retenez : `const T *p` (objet pointé constant) et `T *const p` (pointeur constant) sont deux choses différentes.

## 13.7 `void *` et ses alternatives

Un `void *` perd toute information de type. Contrairement au C, la conversion vers `T *` exige un **cast explicite**.

```cpp
#include <iostream>

int main() {
    int x = 7;
    void *v = &x;                       // conversion implicite vers void * : permise
    int *q = static_cast<int *>(v);     // retour : cast obligatoire
    std::cout << *q << '\n';
    return 0;
}
```

| Besoin | Alternative C++ sûre |
| --- | --- |
| Fonction générique sur plusieurs types | **Templates** ([section 20](#20-using-typedef-et-templates)) |
| Valeur de type « l'un parmi N » | `std::variant` |
| Valeur de type quelconque | `std::any` |
| Objets de types liés | Classe de base polymorphe ([section 21](#21-pointeurs-de-fonctions-lambdas-et-polymorphisme)) |
| Réinterpréter des octets | `std::bit_cast`, `std::memcpy` |

## 13.8 Pointeur vers un objet

```cpp
#include <iostream>

struct Point { int x, y; };

int main() {
    Point p{1, 2};
    Point *pp = &p;

    pp->x = 5;            // équivaut à (*pp).x = 5
    (*pp).y = 6;
    std::cout << p.x << ' ' << p.y << '\n';    // 5 6
    return 0;
}
```

Dans une fonction membre, `this` est un pointeur vers l'objet courant ([section 18](#18-structures-classes-et-unions)).

## 13.9 Aliasing et `restrict`

Le compilateur suppose que des pointeurs de **types différents** ne désignent pas le même objet (*strict aliasing*) : le violer est un comportement indéfini. Pour réinterpréter des bits, utilisez `std::bit_cast` (C++20) ou `std::memcpy`. Le mot-clé `restrict` du C n'existe pas en C++ standard (extension `__restrict` dans GCC, Clang et MSVC).

## 13.10 Erreurs classiques

| Erreur | Conséquence | Parade |
| --- | --- | --- |
| Pointeur non initialisé | Adresse aléatoire (UB) | `= nullptr` |
| Déréférencer `nullptr` | Plantage | Tester avant |
| Pointeur **pendant** (objet détruit) | UB | Ne pas garder d'adresse d'un objet détruit ; pointeurs intelligents |
| Sortie de tableau | UB | Vérifier les bornes ; `std::span` |
| `delete` d'un pointeur non alloué par `new` | UB | Propriété claire (smart pointers) |
| Retourner l'adresse d'une variable locale | Pointeur pendant | Retourner par valeur |
| Comparer des pointeurs d'objets distincts avec `<` | Non spécifié | `std::less` |

> **Remarque** : Le C++ moderne réduit fortement l'usage des pointeurs bruts : références, conteneurs, `std::span`, `std::optional` et **pointeurs intelligents** (section 14.5) couvrent la plupart des besoins. Un pointeur brut devient un simple **observateur** non propriétaire.

---

# 14. Allocation dynamique de mémoire

## 14.1 Pourquoi allouer dynamiquement ?

La pile a une taille limitée et ses variables disparaissent à la fin du bloc. Le **tas** (*heap*) sert quand la taille n'est connue qu'à l'exécution, quand la durée de vie dépasse la fonction, ou quand les objets sont volumineux. En C++ moderne, c'est surtout le travail des **conteneurs** (`std::vector`, `std::string`) et des **pointeurs intelligents**.

## 14.2 `new` et `delete`

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
    return 0;
}
```

| Allocation | Libération |
| --- | --- |
| `new T` / `new T(args)` | `delete p` |
| `new T[n]` | `delete[] p` |
| `malloc` / `calloc` | `free` |

> **Attention** : Ne **mélangez jamais** ces familles (`new` + `free`, `malloc` + `delete`, `new[]` + `delete`) : comportement indéfini. `new` appelle les **constructeurs**, `malloc` non ; en C++, on n'utilise pas `malloc` pour les objets.

## 14.3 Initialisation et échec d'allocation

```cpp
#include <iostream>
#include <new>

int main() {
    int *a = new int;               // valeur indéterminée
    int *b = new int();             // 0 (initialisation par valeur)
    int *c = new int{7};            // 7
    int *d = new int[4]();          // 4 zéros (équivalent de calloc)
    int *e = new int[4]{1, 2};      // 1 2 0 0
    std::cout << *b << *c << d[3] << e[1] << '\n';
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
    return 0;
}
```

## 14.4 Tableaux dynamiques : `std::vector`

L'équivalent moderne de `malloc` + `realloc` est `std::vector` : il gère la mémoire, l'agrandissement et la libération.

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v;
    v.reserve(100);                         // réserve la capacité (évite les réallocations)
    for (int i = 0; i < 10; ++i) v.push_back(i);

    v.resize(20);                           // agrandit ; les nouveaux éléments valent 0
    v.shrink_to_fit();                      // demande de réduire la capacité à la taille
    std::cout << v.size() << ' ' << v.capacity() << '\n';
    return 0;
}                                           // libération automatique
```

## 14.5 Pointeurs intelligents (`<memory>`) *(C++11, ajout)*

Un **pointeur intelligent** est un objet RAII qui possède une ressource et la libère automatiquement.

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

    auto s1 = std::make_shared<Joueur>("Luc");        // propriété partagée (compteur de références)
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
    return 0;
}                                                     // tout est libéré automatiquement
```

| Type | Propriété | Copiable | Usage |
| --- | --- | --- | --- |
| `std::unique_ptr<T>` | **Unique** | Non (déplaçable) | Choix **par défaut** ; aucun surcoût |
| `std::shared_ptr<T>` | **Partagée** (compteur atomique) | Oui | Objet partagé entre plusieurs propriétaires |
| `std::weak_ptr<T>` | Aucune (observe) | Oui | Casser les **cycles** de `shared_ptr` ; caches |
| `std::auto_ptr` | | | **Supprimé** (C++17) |

> **Bonne pratique** : Créez-les avec `std::make_unique` / `std::make_shared` ; **n'écrivez plus** `new` / `delete` dans le code applicatif.

## 14.6 Erreurs classiques

| Erreur | Conséquence | Parade |
| --- | --- | --- |
| Oublier `delete` | **Fuite mémoire** | `unique_ptr`, conteneurs |
| `delete` deux fois | Corruption du tas (UB) | Pointeurs intelligents |
| Utiliser après `delete` (*use-after-free*) | UB, faille de sécurité | `p = nullptr` ; propriété claire |
| `new[]` libéré avec `delete` (ou l'inverse) | UB | `delete[]` ; ou `std::vector` |
| Fuite en cas d'exception | Ressource jamais libérée | RAII |
| Deux `shared_ptr` construits depuis le même pointeur brut | Double libération | `make_shared`, copier le `shared_ptr` |
| Cycle de `shared_ptr` | Fuite | `weak_ptr` |

```cpp
#include <memory>

void risque();                                   // peut lever une exception

void fuite() {
    int *p = new int[100];
    risque();                                    // si risque() lève : le delete[] est sauté
    delete[] p;
}

void sur() {
    auto p = std::make_unique<int[]>(100);
    risque();                                    // exception : p est quand même libéré
}
```

## 14.7 Outils de détection

```bash
g++ -g -fsanitize=address,undefined -std=c++20 prog.cpp -o prog   # AddressSanitizer + UBSan
./prog

valgrind --leak-check=full ./prog                                 # fuites et accès invalides
```

## 14.8 Règles de propriété

- Un pointeur brut ou une référence **ne possède pas** : il observe.
- Une ressource a **un seul propriétaire** : un objet, un conteneur ou un `unique_ptr`.
- La **propriété partagée** (`shared_ptr`) est l'exception : à justifier.
- Documentez qui possède quoi dans les interfaces (`std::unique_ptr<T>` en paramètre = transfert de propriété).

---

# 15. Retourner des tableaux et des chaînes

## 15.1 Le problème

Une variable locale est détruite à la sortie de la fonction : on ne peut pas en retourner l'adresse.

```cpp
// int *mauvais() {
//     int t[3] = {1, 2, 3};
//     return t;             // t est détruit à la sortie : le pointeur est invalide
// }
```

## 15.2 Les solutions

```cpp
#include <algorithm>
#include <cctype>
#include <iostream>
#include <optional>
#include <span>
#include <string>
#include <utility>
#include <vector>

// 1. Retour par VALEUR (solution recommandée) : pas de copie profonde grâce au déplacement / à l'élision
std::vector<int> carres(int n) {
    std::vector<int> v;
    v.reserve(n);
    for (int i = 0; i < n; ++i) v.push_back(i * i);
    return v;
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
    auto v = carres(5);                                   // 0 1 4 9 16
    std::cout << majuscules("bonjour") << '\n';           // BONJOUR

    int tampon[4];
    remplir_carres(tampon);                               // un tableau C se convertit en span
    std::cout << tampon[3] << '\n';                       // 9

    auto [q, r] = divmod(17, 5);                          // liaisons structurées : 3 et 2
    auto st = calculer({2.0, 4.0, 9.0});
    std::cout << q << ' ' << r << ' ' << st.moyenne << '\n';

    if (auto p = premier_pair({1, 3, 8, 5})) std::cout << *p << '\n';        // 8
    std::cout << v.size() << '\n';
    return 0;
}
```

| Solution | Quand l'utiliser |
| --- | --- |
| **Retour par valeur** (`vector`, `string`, `struct`) | **Par défaut** : simple, sûr, performant |
| Paramètre de sortie (`span`, `T &`) | Réutiliser un tampon existant, éviter des allocations répétées |
| `std::pair`, `std::tuple`, `struct` | Retourner plusieurs valeurs |
| `std::optional<T>` | Résultat éventuellement absent |
| `std::expected<T, E>` *(C++23)* | Résultat **ou** erreur typée, sans exception |
| `std::unique_ptr<T>` | Transférer la propriété d'un objet alloué (polymorphisme, grosse ressource) |
| Variable `static` locale | **À éviter** : partagée entre appels, non réentrante |

## 15.3 Ce qu'il ne faut jamais faire

```cpp
#include <string>
#include <string_view>

std::string fabrique() { return "temporaire"; }

void pieges() {
    std::string_view sv = fabrique();            // DANGER : le temporaire est détruit, sv est pendant
    const char *c = fabrique().c_str();          // DANGER : idem pour c
    const std::string &ok = fabrique();          // OK : la durée de vie du temporaire est prolongée
    (void)sv; (void)c; (void)ok;
}

// const std::string &retourne_local() { std::string s = "x"; return s; }   // DANGER : référence vers un local
```

## 15.4 Sémantique de déplacement *(C++11, ajout)*

Une **lvalue** a un nom et une adresse (une variable) ; une **rvalue** est un temporaire sur le point de disparaître. La **référence rvalue** `T &&` permet de **voler** les ressources d'un temporaire au lieu de les copier.

```cpp
#include <iostream>
#include <string>
#include <utility>
#include <vector>

int main() {
    std::string a = "contenu très long qui nécessite une allocation sur le tas";
    std::string b = a;                         // COPIE : a reste intact
    std::string c = std::move(a);              // DÉPLACEMENT : c vole le tampon de a
    std::cout << a.size() << ' ' << c.size() << '\n';     // a est valide mais dans un état indéterminé (souvent vide)

    std::vector<std::string> v;
    v.push_back(std::move(c));                 // déplace au lieu de copier
    v.emplace_back("construit sur place");     // construit directement dans le vecteur
    std::cout << v.size() << ' ' << b.size() << '\n';
    return 0;
}
```

- `std::move(x)` ne déplace rien : il **autorise** le déplacement en convertissant `x` en rvalue.
- Après un déplacement, l'objet source reste **valide** mais son contenu est indéterminé : on ne fait que le détruire ou lui réaffecter une valeur.
- **N'écrivez pas** `return std::move(local);` : cela empêche l'élision de copie ; `return local;` suffit.
- La conception d'un constructeur de déplacement est détaillée en [section 18.9](#189-copie-déplacement-et-règle-des-cinq-ajout).

## 15.5 Bonnes pratiques

- Retournez par **valeur** : le compilateur s'occupe de l'efficacité.
- Ne retournez jamais de référence, de pointeur ou de `string_view` vers un objet local ou temporaire.
- Utilisez `std::optional` / `std::expected` plutôt que des valeurs magiques (`-1`, `nullptr`).
- Documentez la propriété : un `std::unique_ptr` retourné transfère la responsabilité à l'appelant.

---

# 16. Structures de données dynamiques

## 16.1 Liste simplement chaînée

Écrire sa propre liste reste un excellent exercice. Avec des `std::unique_ptr`, **chaque nœud possède le suivant** : aucune fuite possible.

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
    l.afficher();                       // 1 -> 2 -> 3 -> fin
    l.supprimer(2);
    l.afficher();                       // 1 -> 3 -> fin
    return 0;
}
```

En pratique, on utilise les listes de la bibliothèque standard :

```cpp
#include <forward_list>
#include <list>

int main() {
    std::list<int> li{1, 2, 3};          // liste doublement chaînée
    li.push_front(0);
    li.push_back(4);
    li.remove(2);                        // supprime toutes les valeurs égales à 2

    std::forward_list<int> fl{1, 2, 3};  // liste simplement chaînée, plus économe
    fl.push_front(0);
    return 0;
}
```

## 16.2 Les conteneurs de la bibliothèque standard

| Conteneur | Description | Accès / insertion typiques |
| --- | --- | --- |
| `std::array<T, N>` | Tableau de taille fixe | Accès O(1) |
| `std::vector<T>` | Tableau dynamique contigu | Accès O(1), ajout en fin O(1) amorti, insertion au milieu O(n) |
| `std::deque<T>` | File à double extrémité | Ajout aux deux bouts O(1) |
| `std::list<T>` | Liste doublement chaînée | Insertion / suppression O(1) (position connue), pas d'accès direct |
| `std::forward_list<T>` | Liste simplement chaînée | Insertion en tête O(1) |
| `std::set<T>` / `std::multiset<T>` | Ensemble **trié** (arbre équilibré) | O(log n) |
| `std::map<K, V>` / `std::multimap<K, V>` | Dictionnaire **trié** | O(log n) |
| `std::unordered_set<T>` / `std::unordered_map<K, V>` | Table de hachage | O(1) en moyenne |
| `std::stack`, `std::queue`, `std::priority_queue` | Adaptateurs (pile, file, file de priorité) | |
| `std::flat_map`, `std::flat_set` *(C++23)* | Associatifs sur tableaux triés | Parcours rapide, insertion plus lente |
| `std::inplace_vector<T, N>` *(C++26)* | Vecteur de capacité fixe, sans allocation | Embarqué, temps réel |

## 16.3 Tableau dynamique extensible : `std::vector`

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
    std::cout << '\n';
    return 0;
}
```

> **Attention** : Quand un `vector` **se réalloue** (capacité dépassée), tous les itérateurs, pointeurs et références vers ses éléments deviennent **invalides**. Ne gardez pas `int &premier = v[0];` avant un `push_back`. Utilisez `reserve` pour limiter les réallocations.

| Fonction | Rôle |
| --- | --- |
| `push_back(x)`, `emplace_back(args...)` | Ajoute en fin (copie / déplacement / construction sur place) |
| `insert`, `erase`, `pop_back`, `clear` | Modifications |
| `size`, `capacity`, `empty` | Informations |
| `reserve(n)`, `resize(n)`, `shrink_to_fit()` | Gestion de la taille |
| `data()` | Pointeur vers le tampon contigu (interopérabilité C) |
| `front()`, `back()`, `at(i)`, `[i]` | Accès |

## 16.4 Matrices dynamiques

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
    return 0;
}                                                        // aucun delete à écrire
```

> **Remarque** : `std::vector<std::vector<double>>` est plus simple à écrire, mais chaque ligne est une allocation distincte (moins performant). Le stockage à plat est cache-friendly ; en C++23, `std::mdspan` permet d'indexer un tel tampon avec plusieurs dimensions.

## 16.5 Conteneurs associatifs *(ajout)*

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
    for (const char *mot : {"a", "b", "a", "c", "a"}) ++freq[mot];     // [] crée l'entrée à 0 si absente
    std::cout << freq["a"] << '\n';                   // 3

    std::set<int> s{3, 1, 2, 3};                      // doublons ignorés, trié : 1 2 3
    std::cout << s.size() << '\n';                    // 3
    return 0;
}
```

> **Attention** : `m[cle]` **insère** une entrée par défaut si la clé est absente ; pour consulter sans modifier, utilisez `find`, `contains` ou `at` (qui lève une exception).

## 16.6 Itérateurs et algorithmes *(ajout)*

Un **itérateur** est un objet qui se comporte comme un pointeur : `*it` donne l'élément, `++it` avance. Chaque conteneur fournit `begin()` et `end()` (un cran **après** le dernier élément). Les algorithmes de `<algorithm>` travaillent sur des intervalles `[début, fin)`.

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
    std::cout << '\n';
    return 0;
}
```

| Catégorie d'itérateur | Capacités | Exemples |
| --- | --- | --- |
| Entrée / sortie | Lecture ou écriture, un seul passage | `istream_iterator` |
| Avant (*forward*) | Avance, plusieurs passages | `forward_list` |
| Bidirectionnel | Avance et recule | `list`, `map`, `set` |
| Accès aléatoire | `it + n`, `it[n]` | `vector`, `deque`, `array` |
| Contigu *(C++20)* | Éléments adjacents en mémoire | `vector`, `array`, `string` |

## 16.7 Adaptateurs : pile, file, file de priorité

```cpp
#include <functional>
#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <vector>

int main() {
    std::stack<int> pile;                    // LIFO
    pile.push(1); pile.push(2);
    std::cout << pile.top() << '\n';         // 2
    pile.pop();

    std::queue<std::string> file;            // FIFO
    file.push("a"); file.push("b");
    std::cout << file.front() << '\n';       // a
    file.pop();

    std::priority_queue<int> pq;             // le plus grand en tête
    for (int x : {5, 1, 8, 3}) pq.push(x);
    std::cout << pq.top() << '\n';           // 8

    std::priority_queue<int, std::vector<int>, std::greater<>> min_pq;   // le plus petit en tête
    min_pq.push(5); min_pq.push(1);
    std::cout << min_pq.top() << '\n';       // 1
    return 0;
}
```

## 16.8 Choisir un conteneur

| Besoin | Conteneur |
| --- | --- |
| Suite d'éléments, cas général | `std::vector` (**par défaut**) |
| Taille connue à la compilation | `std::array` |
| Ajouts / retraits aux deux extrémités | `std::deque` |
| Recherche par clé, tri sur la clé | `std::map` / `std::set` |
| Recherche par clé la plus rapide, sans ordre | `std::unordered_map` / `std::unordered_set` |
| Insertions fréquentes au milieu avec itérateurs stables | `std::list` |
| LIFO, FIFO, priorité | `stack`, `queue`, `priority_queue` |

---

# 17. Références et pointeurs doubles

## 17.1 Les références *(ajout)*

Une **référence** est un **alias** : un second nom pour un objet existant. Elle doit être initialisée à sa déclaration et ne peut plus désigner un autre objet ensuite.

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
    return 0;
}
```

| | Référence `T &` | Pointeur `T *` |
| --- | --- | --- |
| Peut être nulle | **Non** | Oui (`nullptr`) |
| Réaffectable | **Non** | Oui |
| Initialisation obligatoire | Oui | Non (mais recommandée) |
| Syntaxe d'accès | Directe (`r`) | Déréférencement (`*p`, `p->`) |
| Arithmétique | Non | Oui |
| Usage typique | Paramètres, valeurs de retour, alias | Optionnel, structures liées, API C |

Familles de références :

- `T &` : référence **lvalue** ;
- `const T &` : lecture seule, accepte aussi les temporaires ;
- `T &&` : référence **rvalue** (déplacement, voir [section 15.4](#154-sémantique-de-déplacement-c11-ajout)) ;
- `std::reference_wrapper<T>` / `std::ref(x)` : référence **copiable**, utilisable dans un conteneur.

> **Attention** : On ne peut pas créer de tableau de références ni de `std::vector<T &>`. Utilisez `std::vector<std::reference_wrapper<T>>` ou des pointeurs.

## 17.2 Pointeurs doubles : définition

Un **pointeur double** (`T **`) est un pointeur vers un pointeur.

```cpp
#include <iostream>

int main() {
    int x = 5;
    int *p = &x;
    int **pp = &p;                    // pp contient l'adresse de p

    **pp = 10;                        // modifie x
    std::cout << x << ' ' << *p << ' ' << **pp << '\n';    // 10 10 10
    return 0;
}
```

## 17.3 Usages principaux

### Modifier un pointeur depuis une fonction

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
    return 0;
}
```

> **Bonne pratique** : En C++ moderne, on **retourne** un `std::unique_ptr` au lieu de modifier un pointeur passé en paramètre.

### Matrice dynamique « à l'ancienne »

```cpp
#include <iostream>

int main() {
    const int lignes = 3, colonnes = 4;
    int **m = new int *[lignes];                               // tableau de pointeurs
    for (int i = 0; i < lignes; ++i) m[i] = new int[colonnes]();   // chaque ligne, initialisée à 0

    m[1][2] = 9;
    std::cout << m[1][2] << '\n';

    for (int i = 0; i < lignes; ++i) delete[] m[i];            // libérer les lignes d'abord
    delete[] m;                                                // puis le tableau de pointeurs
    return 0;
}
```

Même schéma pour un **tableau de chaînes** (`char **`) ou une **liste chaînée** (le « pointeur vers le lien » de la [section 16.1](#161-liste-simplement-chaînée)). Le tableau `char **argv` des arguments de la ligne de commande est un autre cas (voir [section 23](#23-arguments-de-la-ligne-de-commande)).

## 17.4 Libération

Avec des pointeurs doubles bruts, il faut libérer **dans l'ordre inverse** de l'allocation, et chaque `new` doit avoir son `delete`. La solution moderne évite toute libération manuelle :

```cpp
#include <memory>
#include <string>
#include <vector>

int main() {
    std::vector<std::vector<int>> m(3, std::vector<int>(4));            // matrice sans new ni delete
    std::vector<std::string> mots{"un", "deux", "trois"};               // remplace char **
    std::vector<std::unique_ptr<int[]>> lignes;                         // si l'on tient à des lignes séparées
    lignes.push_back(std::make_unique<int[]>(4));
    return 0;
}
```

## 17.5 Référence, pointeur ou pointeur double ?

| Situation | Choix |
| --- | --- |
| Paramètre obligatoire à modifier | `T &` |
| Paramètre en lecture seule, gros objet | `const T &` |
| Paramètre optionnel | `T *` (ou `std::optional<std::reference_wrapper<T>>`) |
| Fonction qui doit **faire pointer** l'appelant sur un nouvel objet | Retourner un pointeur intelligent |
| Interface C (`char **argv`, `int **out`) | `T **` |
| Collection d'objets | Conteneur (`vector`) |

---

# 18. Structures, classes et unions

## 18.1 Structures

En C++, une `struct` est un **type** à part entière : elle peut avoir des valeurs par défaut, des **fonctions membres**, des constructeurs et de l'héritage. La seule différence avec une `class` est l'accès par défaut (`public` pour `struct`, `private` pour `class`).

```cpp
#include <cmath>
#include <iostream>
#include <string>

struct Point {
    double x = 0.0;                    // valeurs par défaut des membres (C++11)
    double y = 0.0;

    double distance(const Point &autre) const {          // fonction membre ; const : ne modifie pas l'objet
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
    return 0;
}
```

## 18.2 Alignement et rembourrage (*padding*)

Le compilateur insère des octets de remplissage pour aligner les membres.

```cpp
#include <iostream>

struct A { char c; int i; char d; };              // typiquement 12 octets
struct B { int i; char c; char d; };              // typiquement 8 octets : membres triés par taille décroissante
struct alignas(16) C { float v[3]; };             // alignement imposé de 16 octets

int main() {
    std::cout << sizeof(A) << ' ' << sizeof(B) << ' ' << sizeof(C) << ' ' << alignof(C) << '\n';   // 12 8 16 16
    return 0;
}
```

> **Remarque** : Ordonner les membres du plus grand au plus petit réduit le rembourrage. Ne comptez pas sur `sizeof(struct)` = somme des membres, et ne sérialisez pas une structure par copie brute (`memcpy`, `write`) : le format dépend de la plateforme.

## 18.3 Champs de bits

```cpp
#include <iostream>

struct Drapeaux {
    unsigned lecture : 1;              // 1 bit
    unsigned ecriture : 1;
    unsigned niveau : 3;               // 3 bits : valeurs 0 à 7
};

int main() {
    Drapeaux d{1, 0, 5};
    std::cout << d.lecture << d.ecriture << d.niveau << '\n';      // 105
    return 0;
}
```

La disposition des champs de bits dépend du compilateur : pour des **drapeaux portables**, préférez `std::bitset` ou un `enum class` avec opérateurs bit à bit ([section 19](#19-énumérations-enum) et [section 25](#25-opérateurs-bit-à-bit)).

## 18.4 Tableau dans une structure

Le **membre de tableau flexible** du C99 (`int donnees[];`) n'existe pas en C++ standard. On place un `std::array` (taille fixe) ou un `std::vector` (taille variable) comme membre.

```cpp
#include <array>
#include <string>
#include <vector>

struct Etudiant {
    std::string nom;
    std::array<int, 3> notes{};            // tableau de taille fixe, copié avec la structure
    std::vector<std::string> options;      // taille variable
};
```

## 18.5 Unions et `std::variant`

Une **union** regroupe plusieurs membres à la **même adresse** : un seul est « actif » à la fois. En C++, lire un membre autre que le dernier écrit est un **comportement indéfini** (contrairement au C).

```cpp
#include <iostream>
#include <string>
#include <variant>

union Valeur {
    int i;
    float f;
    char c;
};

int main() {
    Valeur v;
    v.i = 42;
    std::cout << v.i << ' ' << sizeof(Valeur) << '\n';     // 42 4 : taille du plus grand membre
    // std::cout << v.f;                                    // UB : membre inactif

    std::variant<int, double, std::string> w = 3.5;         // union ÉTIQUETÉE et sûre (C++17)
    w = std::string("texte");

    if (std::holds_alternative<std::string>(w)) std::cout << std::get<std::string>(w) << '\n';
    if (auto *p = std::get_if<int>(&w)) std::cout << *p << '\n';    // nullptr : l'alternative active n'est pas int

    std::visit([](const auto &x) { std::cout << x << '\n'; }, w);   // appelle la lambda avec la valeur active
    return 0;
}
```

## 18.6 Structure, classe, union ou variant ?

| Besoin | Choix |
| --- | --- |
| Regrouper des données sans invariant | `struct` |
| Garantir des invariants, cacher l'implémentation | `class` |
| Une valeur parmi plusieurs types (type somme) | `std::variant` (ou `std::optional`, `std::expected`) |
| Réinterpréter des octets | `std::bit_cast`, `std::memcpy` |
| Union brute | Cas rares (code de bas niveau, interopérabilité) |

## 18.7 Classes et encapsulation *(ajout)*

Une **classe** regroupe des **données** (membres) et les **fonctions** qui les manipulent (méthodes), en **cachant** l'implémentation derrière une interface publique. Le but : garantir des **invariants** (par exemple, « le solde n'est jamais négatif »).

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
    return 0;
}
```

| Niveau d'accès | Visible depuis |
| --- | --- |
| `public` | Tout le monde |
| `protected` | La classe et ses classes dérivées |
| `private` | La classe elle-même (et ses `friend`) |

## 18.8 Constructeurs et destructeur *(ajout)*

Un **constructeur** initialise l'objet ; le **destructeur** (`~Classe()`) libère ses ressources. Les membres sont construits dans l'**ordre de leur déclaration** (et non de la liste d'initialisation), puis détruits dans l'ordre inverse.

```cpp
#include <iostream>

class Rectangle {
    double l_, h_;
public:
    Rectangle() : Rectangle(1.0, 1.0) {}                    // constructeur par défaut, délégué
    Rectangle(double l, double h) : l_(l), h_(h) {}         // liste d'initialisation de membres
    explicit Rectangle(double cote) : Rectangle(cote, cote) {}   // explicit : pas de conversion implicite double -> Rectangle
    ~Rectangle() = default;

    double aire() const { return l_ * h_; }
};

int main() {
    Rectangle a;               // 1 x 1
    Rectangle b(2.0, 3.0);
    Rectangle c{4.0};          // carré 4 x 4
    // Rectangle d = 5.0;      // ERREUR : constructeur explicit
    std::cout << a.aire() << ' ' << b.aire() << ' ' << c.aire() << '\n';   // 1 6 16
    return 0;
}
```

| Constructeur | Quand est-il appelé ? |
| --- | --- |
| Par défaut `T()` | `T x;` |
| Paramétré | `T x(a, b);` ou `T x{a, b};` |
| De copie `T(const T &)` | `T y = x;` |
| De déplacement `T(T &&)` | `T y = std::move(x);` |
| Délégué | Appelle un autre constructeur de la même classe |
| `explicit` | Interdit la conversion implicite |
| `= default` / `= delete` | Demande la version générée / interdit l'opération |

## 18.9 Copie, déplacement et règle des cinq *(ajout)*

Quand une classe **possède une ressource** (mémoire, fichier…), le comportement par défaut (copie membre à membre) est faux : deux objets finiraient par libérer la même ressource.

- **Règle du zéro** *(à privilégier)* : n'écrivez aucune de ces fonctions ; ne détenez que des membres RAII (`vector`, `string`, `unique_ptr`…). Le compilateur génère tout correctement.
- **Règle des cinq** : si vous devez en définir une (destructeur, copie, affectation par copie, déplacement, affectation par déplacement), définissez-les **toutes** (ou `= default` / `= delete`).

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
            Tampon tmp(o);                                                  // copie, puis échange (sûr en cas d'exception)
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
    std::cout << b[2] << ' ' << c[2] << ' ' << a.taille() << '\n';   // 7 7 0
    return 0;
}
```

> **Bonne pratique** : Remplacez le `int *` et la taille par un `std::vector<int>` : la classe n'a plus besoin d'aucune des cinq fonctions (règle du zéro).

## 18.10 Membres statiques, `const`, `mutable`, `friend` *(ajout)*

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
    return 0;
}
```

- Une **méthode `const`** promet de ne pas modifier l'objet : marquez `const` toute méthode qui le peut.
- Un **membre statique** appartient à la classe, pas aux objets.
- Un `friend` donne l'accès au privé à une fonction ou classe extérieure : à utiliser avec parcimonie.

## 18.11 Surcharge d'opérateurs *(ajout)*

```cpp
#include <compare>
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
    return 0;
}
```

| Règle | Détail |
| --- | --- |
| Conserver la **sémantique** attendue | `+` ne modifie pas ses opérandes, `==` est symétrique |
| Opérateurs non surchargeables | `::` `.` `.*` `?:` `sizeof` `typeid` |
| À ne pas surcharger | `&&`, `\|\|`, `,` (perdent l'évaluation paresseuse / l'ordre) et `&` unaire |
| `operator<=>` *(C++20)* | `auto operator<=>(const T &) const = default;` génère `<`, `<=`, `>`, `>=` |
| `operator[]`, `operator()`, `operator->` | Indexation, objets-fonctions, pointeurs intelligents |
| Conversion | `explicit operator bool() const` pour tester un objet dans un `if` |

## 18.12 Héritage *(ajout)*

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
    using Animal::Animal;                             // hérite du constructeur de la base
    void aboyer() { ++tours_; std::cout << nom_ << " : Ouaf !\n"; }
};

int main() {
    Chien rex("Rex");
    rex.aboyer();
    std::cout << rex.nom() << '\n';

    Animal a = rex;                                   // « slicing » : seule la partie Animal est copiée !
    std::cout << a.nom() << '\n';
    return 0;
}
```

| Forme | Signification |
| --- | --- |
| `class D : public B` | « D est un B » (cas courant) |
| `class D : protected B`, `private B` | Implémentation seulement : rare, préférer la **composition** |
| `class D : public B1, public B2` | **Héritage multiple** : possible ; en cas de base commune (« diamant »), utiliser l'héritage `virtual` |
| `class D final : public B` | Interdit toute dérivation de `D` |

Ordre d'exécution : constructeur de la base, puis des membres, puis du corps du constructeur de la classe dérivée ; destruction dans l'ordre inverse. Le **polymorphisme** (appel de la bonne fonction selon le type réel de l'objet) est abordé en [section 21.5](#215-polymorphisme-et-fonctions-virtuelles-ajout).

## 18.13 Bonnes pratiques

- Utilisez `struct` pour de simples données, `class` quand il y a des **invariants**.
- Rendez les données **privées** ; exposez le minimum d'interface.
- Initialisez les membres dans la liste d'initialisation, ou par valeur par défaut au niveau du membre.
- Marquez `explicit` les constructeurs à un argument et `const` les méthodes de lecture.
- Appliquez la **règle du zéro** ; sinon, la règle des cinq.
- Préférez la **composition** à l'héritage ; ne dérivez d'une classe que si elle a un destructeur virtuel.
- Passez les objets polymorphes par référence ou pointeur (jamais par valeur : *slicing*).

---

# 19. Énumérations (`enum`)

## 19.1 Définition

Une **énumération** définit un ensemble de constantes entières nommées. Le C++ propose deux formes : l'`enum` héritée du C et l'**`enum class`** *(C++11)*, plus sûre.

```cpp
#include <cstdint>
#include <iostream>

enum Couleur { ROUGE, VERT, BLEU };                       // non scopée : noms injectés dans la portée, conversion implicite en int

enum class Jour : std::uint8_t { Lundi = 1, Mardi, Mercredi };   // scopée, type sous-jacent explicite

int main() {
    int c = VERT;                                         // 1 : conversion implicite (source de bugs)
    Jour j = Jour::Mardi;                                 // le nom doit être qualifié
    // int n = j;                                         // ERREUR : pas de conversion implicite
    int n = static_cast<int>(j);                          // 2
    std::cout << c << ' ' << n << '\n';
    return 0;
}
```

| | `enum` | `enum class` |
| --- | --- | --- |
| Portée des noms | Englobante (collisions possibles) | **Propre** à l'énumération (`Jour::Lundi`) |
| Conversion implicite en entier | Oui | **Non** (cast explicite) |
| Type sous-jacent | Défini par le compilateur (sauf indication) | `int` par défaut, modifiable |
| Comparaison avec un autre `enum` | Possible (dangereux) | Interdite |

## 19.2 Avec `switch` et alias

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
        case Rouge: std::cout << "stop\n"; break;
        case Orange: std::cout << "ralentir\n"; break;
        case Vert: std::cout << "passer\n"; break;
    }
}

int main() {
    Feu f = Feu::Orange;
    std::cout << nom(f) << '\n';
    agir(f);
    return 0;
}
```

> **Bonne pratique** : Ne mettez **pas** de `default` dans un `switch` sur une énumération : avec `-Wall`, le compilateur signale alors tout enumérateur oublié (`-Wswitch`).

## 19.3 Particularités

```cpp
#include <iostream>
#include <utility>

enum class Droit : unsigned { Aucun = 0, Lecture = 1, Ecriture = 2, Execution = 4 };    // drapeaux (puissances de 2)

constexpr Droit operator|(Droit a, Droit b) {
    return static_cast<Droit>(std::to_underlying(a) | std::to_underlying(b));    // to_underlying : C++23
}
constexpr bool possede(Droit d, Droit drapeau) {
    return (std::to_underlying(d) & std::to_underlying(drapeau)) != 0;
}

int main() {
    Droit d = Droit::Lecture | Droit::Ecriture;
    std::cout << possede(d, Droit::Ecriture) << possede(d, Droit::Execution) << '\n';   // 10
    std::cout << std::to_underlying(d) << '\n';                                         // 3
    return 0;
}
```

- Les valeurs par défaut commencent à 0 et s'incrémentent de 1 ; on peut en fixer certaines (`Mardi = 5`).
- Il n'y a **aucune conversion automatique en chaîne** : écrivez une fonction (comme `nom` ci-dessus) ; la **réflexion statique** de C++26 permettra de la générer automatiquement.
- Une valeur entière convertie en `enum class` sans vérification peut être hors des énumérateurs déclarés : validez-la avant le `static_cast`.
- Pour des drapeaux, `std::bitset` ou les opérateurs ci-dessus sont préférables aux champs de bits.

## 19.4 Bonnes pratiques

- Utilisez `enum class` par défaut ; l'`enum` classique seulement pour l'interopérabilité avec du code C.
- Précisez le type sous-jacent pour les formats de fichier ou de réseau.
- Nommez les types au singulier (`Couleur`) et les valeurs en `PascalCase` ou `MAJUSCULES`, selon votre convention.
- Pour une valeur « parmi plusieurs types », utilisez `std::variant` plutôt qu'un `enum` + `union`.

---

# 20. `using`, `typedef` et templates

## 20.1 Alias de types : `using` et `typedef`

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

int main() {
    Dictionnaire d;
    Vec<int> v{1, 2, 3};
    Entier n = 1'000'000'000'000;
    ulong_t u = 5;
    (void)d; (void)v; (void)n; (void)u;
    return 0;
}
```

> **Remarque** : Le motif `typedef struct { ... } Nom;` du C est **inutile** en C++ : `struct Nom { ... };` définit déjà le type `Nom`.

## 20.2 Usages courants

| Usage | Exemple |
| --- | --- |
| Type portable ou métier | `using Id = std::uint32_t;` |
| Raccourcir un type complexe | `using Table = std::unordered_map<std::string, std::vector<int>>;` |
| Types « publics » d'une classe | `using value_type = T;` (convention des conteneurs) |
| Importer un membre de la base | `using Base::f;` ou `using Base::Base;` |
| Importer les énumérateurs | `using enum Couleur;` (C++20) |
| Importer un nom d'un espace de noms | `using std::string;` |

## 20.3 Templates de fonctions *(ajout)*

Un **template** est un patron de code paramétré par un ou plusieurs **types** (ou valeurs) ; le compilateur **instancie** une version pour chaque combinaison utilisée.

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
    std::cout << maximum(std::string("a"), std::string("b")) << '\n';     // fonctionne pour tout type comparable avec >
    std::cout << minimum(4, 9) << ' ' << taille(std::array<int, 6>{}) << '\n';
    // maximum(3, 2.5);                                                    // ERREUR : T ambigu (int ou double ?)
    return 0;
}
```

> **Remarque** : Le code d'un template doit être visible là où il est instancié : on le **définit dans l'en-tête**. Un type qui ne supporte pas les opérations utilisées (ici `>`) provoque des erreurs longues et peu lisibles : les **concepts** (section 20.6) y remédient.

## 20.4 Templates de classes *(ajout)*

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

    std::vector v{1, 2, 3};                                      // déduction des arguments de template de classe (C++17) : vector<int>
    std::pair paire{1, 2.5};                                     // pair<int, double>
    std::cout << v.size() << ' ' << paire.second << '\n';
    return 0;
}
```

## 20.5 Spécialisation, `if constexpr` et templates variadiques *(ajout)*

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
    return 0;
}
```

Pour transmettre des arguments à une autre fonction **sans copie inutile**, on combine référence universelle `T &&` et `std::forward` (*transmission parfaite*) :

```cpp
#include <utility>

template <typename F, typename... Args>
decltype(auto) appeler(F &&f, Args &&...args) {
    return std::forward<F>(f)(std::forward<Args>(args)...);
}
```

## 20.6 Concepts *(C++20, ajout)*

Un **concept** exprime les **contraintes** qu'un type doit satisfaire. Il rend les templates plus lisibles et les erreurs plus claires.

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
concept AvecTaille = requires(T t) {                     // expression requires : vérifie la validité d'expressions
    { t.size() } -> std::convertible_to<std::size_t>;
};

template <AvecTaille C>
std::size_t nb(const C &c) { return c.size(); }

int main() {
    std::cout << somme(1, 2) << ' ' << plus_grand(3.5, 2.0) << ' ' << doubler(21) << '\n';
    // somme("a", "b");                                   // ERREUR claire : contrainte « Numerique » non satisfaite
    return 0;
}
```

| Concept standard (`<concepts>`) | Signification |
| --- | --- |
| `std::integral`, `std::floating_point` | Types entiers, réels |
| `std::same_as<T, U>`, `std::convertible_to<From, To>` | Identité, convertibilité |
| `std::totally_ordered`, `std::equality_comparable` | Comparable avec `<` / `==` |
| `std::copyable`, `std::movable`, `std::default_initializable` | Capacités de copie, déplacement, construction |
| `std::invocable<F, Args...>`, `std::predicate` | Appelable avec ces arguments |
| `std::ranges::range`, `std::input_iterator` | Intervalles, itérateurs |

## 20.7 Bonnes pratiques

- Préférez `using` à `typedef`.
- Utilisez des alias pour **nommer l'intention** (`using Seconds = double;`) et non seulement pour raccourcir.
- Contraignez vos templates avec des **concepts**.
- Gardez les templates **courts** ; déléguez aux algorithmes standard.
- Ne mettez jamais `using namespace` dans un en-tête.

---

# 21. Pointeurs de fonctions, lambdas et polymorphisme

## 21.1 Principe

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
    return 0;
}
```

| Syntaxe | Signification |
| --- | --- |
| `int (*f)(int, int)` | Pointeur vers une fonction `int(int, int)` |
| `int *f(int, int)` | **Fonction** retournant un `int *` (pas un pointeur de fonction !) |
| `using Op = int (*)(int, int);` | Alias lisible |
| `f(a, b)` ou `(*f)(a, b)` | Appel |

## 21.2 Avec `using`

```cpp
#include <iostream>

using Operation = int (*)(int, int);

int multiplication(int a, int b) { return a * b; }

int appliquer(Operation f, int a, int b) { return f(a, b); }

int main() {
    std::cout << appliquer(multiplication, 6, 7) << '\n';     // 42
    return 0;
}
```

## 21.3 Callbacks

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

bool decroissant(int a, int b) { return a > b; }
int doubler(int x) { return 2 * x; }

void transformer(std::vector<int> &v, int (*f)(int)) {         // callback : f est appelée pour chaque élément
    for (int &x : v) x = f(x);
}

int main() {
    std::vector<int> v{3, 1, 2};
    std::sort(v.begin(), v.end(), decroissant);                // 3 2 1 : comparateur fourni par l'utilisateur
    transformer(v, doubler);                                   // 6 4 2
    for (int x : v) std::cout << x << ' ';
    std::cout << '\n';
    return 0;
}
```

> **Remarque** : `qsort` et `bsearch` du C fonctionnent en C++ mais utilisent `void *` : préférez `std::sort`, `std::ranges::sort` et `std::lower_bound`, typés et souvent plus rapides.

## 21.4 Table de fonctions

```cpp
#include <iostream>
#include <string_view>

int addition(int a, int b) { return a + b; }
int soustraction(int a, int b) { return a - b; }

struct Commande {
    std::string_view nom;
    int (*action)(int, int);
};

constexpr Commande commandes[] = {{"add", addition}, {"sub", soustraction}};

int main() {
    for (const auto &c : commandes) std::cout << c.nom << " : " << c.action(6, 2) << '\n';
    return 0;
}
```

## 21.5 Polymorphisme et fonctions virtuelles *(ajout)*

Dans le C, on simule les « méthodes » d'un objet avec une structure de pointeurs de fonctions. Le C++ intègre ce mécanisme au langage : les **fonctions virtuelles**. Le compilateur construit pour chaque classe une **table virtuelle** (*vtable*) de pointeurs de fonctions et choisit la bonne **à l'exécution**, selon le type **réel** de l'objet.

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

    if (auto *c = dynamic_cast<Cercle *>(formes[0].get())) {      // conversion vérifiée à l'exécution (nullptr si échec)
        std::cout << "c'est bien un cercle\n";
        (void)c;
    }
    // Forme f;                                                    // ERREUR : classe abstraite non instanciable
    return 0;
}                                                                  // destruction correcte grâce au destructeur virtuel
```

| Élément | Rôle |
| --- | --- |
| `virtual` | La fonction peut être redéfinie ; l'appel dépend du type **réel** |
| `= 0` | Fonction virtuelle **pure** : la classe devient **abstraite** (interface) |
| `override` | Vérifie qu'on redéfinit bien une fonction virtuelle de la base (toujours l'écrire) |
| `final` | Interdit la redéfinition ou la dérivation |
| `virtual ~Base()` | Obligatoire si l'on détruit un objet dérivé via un pointeur de base |
| `dynamic_cast<D *>(b)` | Descente vérifiée dans la hiérarchie (nécessite une base polymorphe) |
| `typeid(*p)` | Identification du type à l'exécution (RTTI) |

> **Attention** : Le polymorphisme ne fonctionne qu'avec des **pointeurs ou références** vers la base. Une copie par valeur (`Forme f = cercle;`) provoque le *slicing*. Chaque appel virtuel coûte une indirection ; quand les types sont connus à la compilation, les **templates** et `std::variant` sont une alternative sans surcoût.

## 21.6 Sélection générique : surcharge, templates et `std::visit` *(à jour)*

Le `_Generic` du C est remplacé en C++ par la **surcharge**, les **templates** et `if constexpr`.

```cpp
#include <iostream>
#include <string>
#include <variant>

void afficher(int x) { std::cout << "entier " << x << '\n'; }
void afficher(double x) { std::cout << "réel " << x << '\n'; }
void afficher(const std::string &s) { std::cout << "chaîne " << s << '\n'; }

template <class... Ts>
struct Surcharge : Ts... { using Ts::operator()...; };             // assemble plusieurs lambdas en un seul objet (C++20 : pas de guide nécessaire)

int main() {
    afficher(1);                    // choix à la compilation selon le type
    afficher(2.5);
    afficher(std::string("abc"));

    std::variant<int, std::string> v = std::string("texte");
    std::visit(Surcharge{
                   [](int i) { std::cout << "int " << i << '\n'; },
                   [](const std::string &s) { std::cout << "string " << s << '\n'; }},
               v);              // choix à l'exécution selon l'alternative active
    return 0;
}
```

## 21.7 Lambdas et `std::function` *(ajout)*

Une **lambda** est une fonction anonyme définie sur place, capable de **capturer** des variables de son contexte.

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

    std::function<int(int)> f = fois;                          // objet-fonction polymorphe (peut contenir toute chose appelable)
    f = carre;
    std::cout << f(4) << '\n';                                 // 16

    std::sort(v.begin(), v.end(), [](int a, int b) { return a > b; });     // comparateur en ligne
    for (int x : v) std::cout << x << ' ';
    std::cout << '\n';
    return 0;
}
```

| Capture | Signification |
| --- | --- |
| `[]` | Rien |
| `[x]` / `[&x]` | `x` par copie / par référence |
| `[=]` / `[&]` | Tout par copie / par référence (à utiliser avec prudence) |
| `[this]`, `[*this]` *(C++17)* | Pointeur vers l'objet / copie de l'objet |
| `[y = std::move(x)]` *(C++14)* | Capture avec initialisation (déplacement) |
| `mutable` | Autorise la modification des copies capturées |

| Type d'objet appelable | Quand l'utiliser |
| --- | --- |
| Pointeur de fonction | Interface C, callback sans état |
| Lambda (`auto`) / paramètre template | Le plus rapide ; type connu à la compilation |
| `std::function<R(Args...)>` | Stocker des appelables de natures différentes (a un coût : indirection, allocation possible) |
| `std::move_only_function` *(C++23)* | Comme `std::function` mais accepte les objets non copiables |

> **Attention** : Une lambda qui capture une variable **par référence** ne doit pas survivre à cette variable (rappel, thread, valeur de retour) : la référence deviendrait pendante.

---

# Niveau avancé

---

# 22. Gestion des fichiers

## 22.1 Flux de fichiers

La bibliothèque `<fstream>` fournit les flux de fichiers, qui s'utilisent comme `std::cin` / `std::cout`.

| Classe | Rôle |
| --- | --- |
| `std::ifstream` | Lecture (*input*) |
| `std::ofstream` | Écriture (*output*) |
| `std::fstream` | Lecture et écriture |

| Mode (`std::ios::`) | Effet |
| --- | --- |
| `in` / `out` | Lecture / écriture |
| `app` | Écrit toujours à la fin (ajout) |
| `trunc` | Vide le fichier à l'ouverture (défaut de `ofstream`) |
| `ate` | Se place à la fin à l'ouverture |
| `binary` | Mode binaire (sans traduction de fins de ligne) |

## 22.2 Ouvrir et fermer

Le fichier est **fermé automatiquement** à la destruction du flux (RAII) : `close()` explicite est rarement nécessaire.

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
    return 0;
}                                                                // f est fermé ici
```

## 22.3 Écrire du texte

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
    return 0;
}
```

## 22.4 Lire du texte

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
    return 0;
}
```

> **Attention** : N'écrivez jamais `while (!in.eof()) { ... }` : le test de fin de fichier n'est vrai qu'**après** une lecture ratée, donc la dernière itération traite des données invalides. Testez directement le résultat de la lecture : `while (std::getline(in, ligne))`.

## 22.5 Fichiers binaires

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
    return 0;
}
```

| | Texte | Binaire |
| --- | --- | --- |
| Lisible par un humain | Oui | Non |
| Taille | Plus grande | Compacte |
| Portabilité | Bonne (attention à l'encodage) | **Fragile** : *padding*, ordre des octets (*endianness*), tailles de types |
| Fonctions | `<<`, `>>`, `getline` | `read`, `write` |

> **Remarque** : Écrire une structure par `write` dépend du rembourrage et de l'ordre des octets : pour un format d'échange, **sérialisez champ par champ** avec des types à taille fixe (`<cstdint>`), ou utilisez un format standard (JSON, Protocol Buffers…).

## 22.6 Se positionner dans un fichier

| Fonction | Rôle |
| --- | --- |
| `seekg(pos, origine)` / `seekp(pos, origine)` | Déplace la position de lecture (*get*) / d'écriture (*put*) |
| `tellg()` / `tellp()` | Position courante |
| `std::ios::beg`, `cur`, `end` | Origines : début, position courante, fin |

```cpp
#include <fstream>
#include <iostream>

int main() {
    std::ifstream in("data.bin", std::ios::binary);
    if (!in) return 1;

    in.seekg(0, std::ios::end);                        // va à la fin
    std::streamoff taille = in.tellg();                // la position vaut la taille en octets
    in.seekg(0, std::ios::beg);                        // revient au début
    std::cout << taille << " octets\n";
    return 0;
}
```

## 22.7 Opérations sur les fichiers et dossiers : `<filesystem>` *(C++17, ajout)*

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
    return 0;
}
```

Les fonctions de `<filesystem>` lèvent `std::filesystem::filesystem_error` en cas d'échec, sauf si on leur passe un paramètre `std::error_code &`. Elles remplacent `remove`, `rename` du C (`<cstdio>`) et les appels spécifiques à chaque système.

## 22.8 Flux en mémoire *(ajout)*

`std::istringstream`, `std::ostringstream` et `std::stringstream` (`<sstream>`) appliquent l'interface des flux à une `std::string` : pratique pour analyser du texte ou construire une chaîne.

```cpp
#include <iostream>
#include <sstream>
#include <string>

int main() {
    std::istringstream entree("12 3.5 mot");
    int n; double d; std::string s;
    entree >> n >> d >> s;                       // lecture formatée depuis une chaîne

    std::ostringstream sortie;
    sortie << "n=" << n << ", d=" << d;          // construction d'une chaîne
    std::cout << sortie.str() << ' ' << s << '\n';
    return 0;
}
```

## 22.9 États du flux et erreurs

| Fonction | Vrai quand |
| --- | --- |
| `good()` | Tout va bien |
| `eof()` | Fin de fichier **atteinte par une lecture** |
| `fail()` | Échec logique (format invalide) ou erreur |
| `bad()` | Erreur grave (disque, flux corrompu) |
| `clear()` | Remet le flux à l'état « bon » |

```cpp
#include <fstream>
#include <iostream>

int main() {
    std::ifstream f;
    f.exceptions(std::ios::failbit | std::ios::badbit);       // les erreurs lèvent std::ios_base::failure
    try {
        f.open("absent.txt");
    } catch (const std::ios_base::failure &e) {
        std::cerr << "Erreur de fichier : " << e.what() << '\n';
    }
    return 0;
}
```

## 22.10 Bonnes pratiques

- Vérifiez **toujours** l'ouverture et le résultat des lectures / écritures.
- Laissez le destructeur fermer le fichier ; limitez la portée du flux.
- Utilisez `std::filesystem::path` pour manipuler les chemins (séparateurs, extensions).
- Pour un format binaire, fixez la taille des types et l'ordre des octets.
- Écrivez dans un fichier temporaire puis `rename` pour éviter les fichiers à moitié écrits.

---

# 23. Arguments de la ligne de commande

## 23.1 `argc` et `argv`

```cpp
#include <iostream>

int main(int argc, char *argv[]) {
    std::cout << "argc = " << argc << '\n';
    for (int i = 0; i < argc; ++i) {
        std::cout << "argv[" << i << "] = " << argv[i] << '\n';
    }
    return 0;
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

| Paramètre | Rôle |
| --- | --- |
| `argc` | Nombre d'arguments (nom du programme compris) |
| `argv[0]` | Nom (ou chemin) du programme |
| `argv[1]` … `argv[argc - 1]` | Arguments, sous forme de chaînes C |
| `argv[argc]` | Toujours `nullptr` |

En C++ moderne, on convertit tout de suite les arguments en objets plus sûrs :

```cpp
#include <iostream>
#include <span>
#include <string>
#include <string_view>
#include <vector>

int main(int argc, char *argv[]) {
    std::vector<std::string_view> args(argv + 1, argv + argc);        // sans le nom du programme
    for (std::string_view a : args) std::cout << '[' << a << ']';
    std::cout << '\n';

    std::span<char *> brut(argv, static_cast<std::size_t>(argc));     // vue sur le tableau d'origine
    std::cout << brut.size() << '\n';
    return 0;
}
```

## 23.2 Conversion et validation

Les arguments sont **toujours des chaînes** : il faut les convertir et valider le résultat.

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
            total += std::stod(argv[i], &lus);                       // lus = nombre de caractères convertis
            if (lus != std::string(argv[i]).size()) throw std::invalid_argument("reste");
        } catch (const std::exception &) {
            std::cerr << "Argument invalide : " << argv[i] << '\n';
            return EXIT_FAILURE;
        }
    }
    std::cout << "somme = " << total << '\n';
    return 0;
}
```

## 23.3 Options (`-h`, `--fichier`)

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
            sortie = args[++i];                                    // la valeur suit l'option
        } else {
            std::cerr << "Option inconnue : " << args[i] << '\n';
            return EXIT_FAILURE;
        }
    }
    std::cout << "verbeux = " << verbeux << ", sortie = " << sortie << '\n';
    return 0;
}
```

Pour des interfaces riches, on utilise une bibliothèque : **CLI11**, **cxxopts**, **Boost.Program_options**, ou `getopt` / `getopt_long` (POSIX).

## 23.4 Variables d'environnement

```cpp
#include <cstdlib>
#include <iostream>

int main() {
    if (const char *home = std::getenv("HOME")) {              // nullptr si la variable n'existe pas
        std::cout << "HOME = " << home << '\n';
    }
    return 0;
}
```

## 23.5 Bonnes pratiques

- Vérifiez `argc` **avant** d'accéder à `argv[i]`.
- Affichez un message d'usage clair et retournez `EXIT_FAILURE` en cas d'erreur.
- Convertissez et **validez** chaque valeur (plage, format) ; ne faites jamais confiance à l'utilisateur.
- Ne modifiez pas les chaînes de `argv` ; copiez-les si nécessaire.
- Sous Windows avec des noms non ASCII, utilisez `wmain` ou l'API du système (voir [section 27](#27-unicode-et-caractères-larges)).

---

# 24. Directives du préprocesseur et modules

## 24.1 Rôle du préprocesseur

Le **préprocesseur** transforme le texte du programme **avant** la compilation. Ses directives commencent par `#`.

| Directive | Rôle |
| --- | --- |
| `#include` | Insère le contenu d'un fichier |
| `#define` / `#undef` | Définit / supprime une macro |
| `#if`, `#ifdef`, `#ifndef`, `#elif`, `#else`, `#endif` | Compilation conditionnelle |
| `#error` / `#warning` | Message d'erreur / d'avertissement (`#warning` standardisé en C++23) |
| `#pragma` | Instruction spécifique au compilateur (`#pragma once`) |
| `#line` | Modifie le numéro de ligne et le nom de fichier rapportés |
| `#embed` *(C++26)* | Intègre le contenu binaire d'un fichier |
| `import` / `export module` *(C++20)* | Modules (traités par le compilateur, pas le préprocesseur) |

## 24.2 `#include`

```cpp
#include <iostream>        // en-tête de la bibliothèque standard : recherché dans les dossiers système
#include <cstdio>          // en-tête hérité du C : préfixe « c », sans « .h »
#include "maths.hpp"       // en-tête du projet : recherché d'abord dans le dossier courant
```

> **Bonne pratique** : Incluez dans l'ordre : l'en-tête correspondant au fichier, puis ceux du projet, puis les bibliothèques tierces, puis la bibliothèque standard. N'incluez que ce que vous utilisez, et **jamais** un `.cpp`.

## 24.3 Macros avec `#define`

```cpp
#include <iostream>

#define VERSION "1.0"                       // macro-constante (préférer constexpr)
#define CARRE(x) x * x                      // macro-fonction MAL écrite
#define CARRE_OK(x) ((x) * (x))             // parenthèses partout

constexpr int carre(int x) { return x * x; }                   // la vraie solution : fonction constexpr
template <typename T> constexpr T carre_t(T x) { return x * x; }

int main() {
    std::cout << CARRE(2 + 3) << '\n';          // 2 + 3 * 2 + 3 = 11 (et non 25)
    std::cout << CARRE_OK(2 + 3) << '\n';       // 25

    int i = 3;
    std::cout << CARRE_OK(i++) << '\n';         // i++ évalué DEUX fois : comportement indéfini
    std::cout << carre(i) << ' ' << carre_t(2.5) << ' ' << VERSION << '\n';   // aucun de ces pièges avec une fonction
    return 0;
}
```

### Opérateurs `#` et `##`, macros variadiques

```cpp
#include <cstdio>
#include <iostream>

#define AFFICHE(var) std::cout << #var << " = " << (var) << '\n'    // # : transforme l'argument en chaîne
#define CONCAT(a, b) a##b                                            // ## : colle deux jetons
#define LOG(fmt, ...) std::printf(fmt "\n" __VA_OPT__(,) __VA_ARGS__)   // macro variadique (__VA_OPT__ : C++20)

int main() {
    int total = 42;
    AFFICHE(total);                    // total = 42
    int CONCAT(valeur, 1) = 5;         // déclare « valeur1 »
    LOG("sans argument");
    LOG("n = %d", valeur1);
    return 0;
}
```

> **Attention** : Les macros ignorent les types, les portées et les espaces de noms ; elles provoquent des erreurs obscures. **Alternatives** : `constexpr` pour les constantes, fonctions `inline` / `constexpr` / templates pour le calcul, `enum class` pour les familles de constantes, `std::source_location` pour le diagnostic. Réservez les macros à l'inclusion conditionnelle, à la détection de plateforme et aux cas qu'aucune autre fonctionnalité ne couvre.

## 24.4 Compilation conditionnelle

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
#ifdef __GNUC__
    std::cout << "compilateur de la famille GCC/Clang\n";
#endif
    return 0;
}
```

| Macro | Signification |
| --- | --- |
| `__cplusplus` | Version de la norme (`201703L`, `202002L`, `202302L`…) |
| `__cpp_lib_*`, `__cpp_*` | **Macros de test de fonctionnalité** (`<version>`) |
| `_WIN32`, `__linux__`, `__APPLE__` | Systèmes d'exploitation |
| `__GNUC__`, `__clang__`, `_MSC_VER` | Compilateurs |
| `NDEBUG` | Désactive `assert` (compilation en mode release) |

## 24.5 Gardes d'inclusion

Un en-tête inclus deux fois provoque des redéfinitions : on le protège.

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

## 24.6 `#error`, `#pragma`, `#undef`, `#embed`

```cpp
#if __cplusplus < 201703L
    #error "Ce projet nécessite C++17 ou plus"       // arrête la compilation
#endif

#define TEMP 1
#undef TEMP                                          // supprime la macro

#pragma once                                         // directive propre au compilateur
```

Avec **C++26**, `#embed` incorpore un fichier dans le programme (compilateurs récents) :

```cpp
constexpr unsigned char logo[] = {
#embed "logo.png"                                    // contenu du fichier sous forme de liste d'octets
};
```

## 24.7 Informations de diagnostic

```cpp
#include <iostream>
#include <source_location>
#include <string_view>

void journal(std::string_view message, std::source_location loc = std::source_location::current()) {
    std::cout << loc.file_name() << ':' << loc.line() << " (" << loc.function_name() << ") : " << message << '\n';
}

int main() {
    std::cout << __FILE__ << ' ' << __LINE__ << ' ' << __func__ << '\n';   // macros prédéfinies et variable __func__
    journal("démarrage");                                                    // remplace les macros __FILE__ / __LINE__
    return 0;
}
```

## 24.8 `static_assert` et mode débogage

```cpp
#include <cassert>
#include <iostream>

static_assert(sizeof(int) >= 4, "int doit faire au moins 4 octets");       // vérifié à la compilation (message facultatif depuis C++17)

#ifdef NDEBUG
constexpr bool DEBUG = false;
#else
constexpr bool DEBUG = true;
#endif

int main() {
    int x = 5;
    assert(x > 0 && "x doit être positif");          // vérification à l'exécution : disparaît avec -DNDEBUG
    if constexpr (DEBUG) {
        std::cout << "mode débogage : x = " << x << '\n';
    }
    return 0;
}
```

## 24.9 Modules *(C++20, ajout)*

Les **modules** remplacent l'inclusion textuelle d'en-têtes : une unité est compilée **une seule fois**, puis importée. Gains : compilation plus rapide, pas de macros qui « fuient », pas de gardes d'inclusion, ordre des `import` sans importance.

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
    return 0;
}
```

| | En-têtes (`#include`) | Modules (`import`) |
| --- | --- | --- |
| Traitement | Texte recopié dans chaque fichier | Interface compilée une seule fois |
| Macros | Se propagent | **Isolées** |
| Gardes d'inclusion | Nécessaires | Inutiles |
| Support | Universel | Dépend du compilateur **et** du système de build (CMake 3.28+ avec Ninja par exemple) |

> **Remarque** : L'adoption des modules progresse, mais leur support par les outils varie encore. Pour un projet destiné à être largement portable, les en-têtes restent le choix par défaut ; vérifiez la prise en charge de votre chaîne d'outils avant de migrer.

---

# 25. Opérateurs bit à bit

## 25.1 Les opérateurs

| Opérateur | Nom | Exemple | Résultat (8 bits) |
| --- | --- | --- | --- |
| `&` | ET | `0b1100 & 0b1010` | `0b1000` |
| `\|` | OU | `0b1100 \| 0b1010` | `0b1110` |
| `^` | OU exclusif | `0b1100 ^ 0b1010` | `0b0110` |
| `~` | NON | `~0b00001100` | `0b11110011` |
| `<<` | Décalage à gauche | `0b0011 << 2` | `0b1100` |
| `>>` | Décalage à droite | `0b1100 >> 2` | `0b0011` |

```cpp
#include <bitset>
#include <cstdint>
#include <iostream>

int main() {
    std::uint8_t a = 0b1100, b = 0b1010;

    std::cout << std::bitset<8>(a & b) << '\n';                      // 00001000
    std::cout << std::bitset<8>(a | b) << '\n';                      // 00001110
    std::cout << std::bitset<8>(a ^ b) << '\n';                      // 00000110
    std::cout << std::bitset<8>(static_cast<std::uint8_t>(~a)) << '\n';   // 11110011
    std::cout << std::bitset<8>(a << 2) << ' ' << std::bitset<8>(a >> 2) << '\n';   // 00110000 00000011
    return 0;
}
```

## 25.2 Masques et drapeaux

```cpp
#include <cstdint>
#include <iostream>

constexpr std::uint8_t LECTURE = 1u << 0;
constexpr std::uint8_t ECRITURE = 1u << 1;
constexpr std::uint8_t EXECUTION = 1u << 2;

int main() {
    std::uint8_t droits = 0;

    droits |= LECTURE | ECRITURE;                  // activer des bits
    droits &= static_cast<std::uint8_t>(~ECRITURE);   // désactiver un bit
    droits ^= EXECUTION;                           // inverser un bit
    bool peut_lire = (droits & LECTURE) != 0;      // tester un bit

    std::cout << static_cast<int>(droits) << ' ' << peut_lire << '\n';   // 5 1
    return 0;
}
```

| Opération | Expression |
| --- | --- |
| Mettre à 1 | `x \|= masque` |
| Mettre à 0 | `x &= ~masque` |
| Inverser | `x ^= masque` |
| Tester | `(x & masque) != 0` |

## 25.3 Décalages

`x << n` multiplie par 2^n et `x >> n` divise par 2^n (pour les entiers non signés ou positifs).

```cpp
#include <iostream>

int main() {
    unsigned x = 5;
    std::cout << (x << 3) << ' ' << (x >> 1) << '\n';    // 40 2
    int n = -8;
    std::cout << (n >> 1) << '\n';                        // -4 : décalage arithmétique (garanti depuis C++20)
    return 0;
}
```

> **Attention** : Décaler d'un nombre de bits **négatif ou supérieur ou égal à la largeur du type** est un comportement indéfini. Avant C++20, le décalage d'un entier signé négatif était dépendant de l'implémentation ; il est défini depuis C++20 (complément à deux).

## 25.4 Afficher en binaire

```cpp
#include <bitset>
#include <format>
#include <iostream>

int main() {
    unsigned x = 37;
    std::cout << std::bitset<8>(x) << '\n';              // 00100101
    std::cout << std::format("{:08b} {:#x} {:o}", x, x, x) << '\n';   // 00100101 0x25 45
    return 0;
}
```

## 25.5 Applications courantes

```cpp
#include <bit>
#include <cstdint>
#include <iostream>
#include <utility>

int main() {
    int n = 12;
    std::cout << ((n & 1) == 0 ? "pair" : "impair") << '\n';          // test de parité
    std::cout << std::has_single_bit(64u) << '\n';                    // 1 : puissance de 2 (C++20)

    std::uint32_t couleur = 0xFF8040;                                 // extraire les composantes RGB
    std::uint8_t r = (couleur >> 16) & 0xFF;
    std::uint8_t g = (couleur >> 8) & 0xFF;
    std::uint8_t b = couleur & 0xFF;
    std::cout << int(r) << ' ' << int(g) << ' ' << int(b) << '\n';    // 255 128 64

    int a = 3, c = 9;
    std::swap(a, c);                                                  // (l'astuce du XOR est une curiosité : à ne pas utiliser)
    std::cout << a << ' ' << c << '\n';
    return 0;
}
```

## 25.6 L'en-tête `<bit>` *(C++20, ajout)*

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
    return 0;
}
```

## 25.7 `std::bitset`

```cpp
#include <bitset>
#include <iostream>

int main() {
    std::bitset<8> b("00101100");
    b.set(0);                 // met le bit 0 à 1
    b.reset(2);               // met le bit 2 à 0
    b.flip(7);                // inverse le bit 7
    std::cout << b << ' ' << b.count() << ' ' << b.test(3) << ' ' << b.to_ulong() << '\n';
    return 0;
}
```

## 25.8 Précautions

- Travaillez sur des types **non signés** à taille fixe (`std::uint8_t`, `std::uint32_t`).
- Les petits types sont **promus en `int`** dans les expressions : `~b` sur un `uint8_t` donne un `int` ; castez le résultat.
- **Priorité** : `==` est plus prioritaire que `&` : `x & 1 == 0` signifie `x & (1 == 0)` ; écrivez `(x & 1) == 0`.
- Ne décalez jamais de plus que la largeur du type.
- Préférez `std::bitset` et `<bit>` aux manipulations « maison » : plus lisible et portable.

---

# 26. Récursivité

## 26.1 Principe

Une fonction **récursive** s'appelle elle-même. Elle comporte toujours :

1. un **cas de base** (arrêt) ;
2. un **appel récursif** qui se rapproche du cas de base.

```cpp
#include <iostream>

long long factorielle(int n) {
    if (n <= 1) return 1;                    // cas de base
    return n * factorielle(n - 1);           // appel récursif sur un problème plus petit
}

int main() {
    std::cout << factorielle(5) << '\n';     // 120
    return 0;
}
```

## 26.2 Exemples classiques

```cpp
#include <iostream>

int pgcd(int a, int b) { return b == 0 ? a : pgcd(b, a % b); }          // algorithme d'Euclide (voir aussi std::gcd)

long long puissance(long long base, unsigned exp) {                      // exponentiation rapide : O(log exp)
    if (exp == 0) return 1;
    long long m = puissance(base, exp / 2);
    return (exp % 2 == 0) ? m * m : m * m * base;
}

int somme_chiffres(int n) { return n < 10 ? n : n % 10 + somme_chiffres(n / 10); }

void hanoi(int n, char de, char vers, char via) {                        // tours de Hanoï
    if (n == 0) return;
    hanoi(n - 1, de, via, vers);
    std::cout << "disque " << n << " : " << de << " -> " << vers << '\n';
    hanoi(n - 1, via, vers, de);
}

int main() {
    std::cout << pgcd(48, 18) << ' ' << puissance(2, 10) << ' ' << somme_chiffres(1234) << '\n';   // 6 1024 10
    hanoi(2, 'A', 'C', 'B');
    return 0;
}
```

## 26.3 Pile d'appels et profondeur

Chaque appel consomme un **cadre de pile** (paramètres, variables locales, adresse de retour). Une récursion trop profonde ou infinie provoque un **dépassement de pile** (*stack overflow*) et un plantage.

```cpp
// long long infinie(long long n) { return infinie(n + 1); }      // pas de cas de base : plantage garanti
```

Le C++ **ne garantit pas** l'optimisation de la récursion terminale (*tail call*) : un compilateur peut la réaliser avec `-O2`, mais on ne peut pas s'y fier. Pour de grandes profondeurs, transformez en boucle :

```cpp
long long factorielle_iter(int n) {
    long long r = 1;
    for (int i = 2; i <= n; ++i) r *= i;
    return r;
}
```

## 26.4 Récursivité et évaluation à la compilation

```cpp
constexpr long long fact(int n) { return n <= 1 ? 1 : n * fact(n - 1); }

static_assert(fact(10) == 3628800);                  // calculé et vérifié par le compilateur
constexpr long long f20 = fact(20);                  // 2432902008176640000, sans calcul à l'exécution
```

## 26.5 Mémoïsation

Fibonacci naïf recalcule les mêmes sous-problèmes (complexité exponentielle). On mémorise les résultats :

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
    return 0;
}
```

## 26.6 Lambdas récursives *(C++23, ajout)*

```cpp
#include <iostream>

int main() {
    auto fib = [](this auto self, int n) -> long long {      // « deducing this » : la lambda s'appelle elle-même
        return n < 2 ? n : self(n - 1) + self(n - 2);
    };
    std::cout << fib(15) << '\n';                            // 610
    return 0;
}
```

Avant C++23, on utilise `std::function` (avec un surcoût) ou une fonction ordinaire.

## 26.7 Récursivité ou itération ?

| | Récursivité | Itération |
| --- | --- | --- |
| Lisibilité | Excellente pour les structures récursives (arbres, diviser pour régner) | Excellente pour les répétitions simples |
| Mémoire | Pile (une trame par appel) | Constante |
| Performance | Coût des appels | Généralement meilleure |
| Risque | Dépassement de pile | Boucle infinie |

Erreurs fréquentes : oubli du cas de base, appel récursif qui ne progresse pas vers lui, débordement de l'entier du résultat (`factorielle(25)` dépasse `long long`), recalculs inutiles (mémoïsation).

---

# 27. Unicode et caractères larges

*(Section à part entière : le texte est plus subtil qu'il n'y paraît.)*

## 27.1 Le problème

Un `char` est un **octet**, pas un « caractère ». En **UTF-8**, un caractère comme `é` occupe **2 octets**, un emoji jusqu'à 4. Une `std::string` stocke des **octets** : `size()` compte donc des octets, pas des caractères.

```cpp
#include <iostream>
#include <string>

int main() {
    std::string s = "é";                       // fichier source encodé en UTF-8
    std::cout << s.size() << '\n';             // 2 : deux octets
    return 0;
}
```

| Encodage | Taille d'un caractère | Remarque |
| --- | --- | --- |
| ASCII | 1 octet | 128 caractères (pas d'accents) |
| Latin-1 / Windows-1252 | 1 octet | Anciens encodages d'Europe de l'Ouest |
| **UTF-8** | 1 à 4 octets | **Standard du web et de Linux/macOS**, compatible ASCII |
| UTF-16 | 2 ou 4 octets | Windows, Java, JavaScript |
| UTF-32 | 4 octets | Un *point de code* par unité |

## 27.2 Les types de caractères du C++

| Type | Littéral | Chaîne | Usage |
| --- | --- | --- | --- |
| `char` | `'a'` | `std::string` | Texte « ordinaire » (en pratique UTF-8) |
| `wchar_t` | `L'a'` | `std::wstring` | Largeur **dépendante de la plateforme** (16 bits sous Windows, 32 bits sous Linux) : à éviter pour du code portable |
| `char8_t` *(C++20)* | `u8'a'` | `std::u8string` | Unités UTF-8 |
| `char16_t` *(C++11)* | `u'a'` | `std::u16string` | Unités UTF-16 |
| `char32_t` *(C++11)* | `U'a'` | `std::u32string` | Points de code UTF-32 |

```cpp
#include <iostream>
#include <string>

int main() {
    std::u8string s8 = u8"héllo";
    std::u16string s16 = u"héllo";
    std::u32string s32 = U"héllo";
    std::cout << s8.size() << ' ' << s16.size() << ' ' << s32.size() << '\n';   // 6 5 5

    // std::cout << s8;                                                          // ERREUR depuis C++20 : char8_t non affichable directement
    std::cout << reinterpret_cast<const char *>(s8.c_str()) << '\n';             // contournement : réinterpréter les octets
    return 0;
}
```

> **Remarque** : Depuis C++20, `u8"..."` est de type `const char8_t[N]` et non plus `const char[N]` : du code C++17 comme `const char *s = u8"é";` ne compile plus.

## 27.3 Compter et parcourir les caractères

```cpp
#include <iostream>
#include <string_view>

std::size_t nb_points_de_code(std::string_view utf8) {
    std::size_t n = 0;
    for (unsigned char c : utf8) {
        if ((c & 0xC0) != 0x80) ++n;          // on ignore les octets de continuation (10xxxxxx)
    }
    return n;
}

int main() {
    std::cout << nb_points_de_code("héllo") << '\n';        // 5 (alors que size() vaut 6)
    return 0;
}
```

> **Attention** : Un « caractère perçu par l'utilisateur » (*grapheme*) peut être composé de **plusieurs** points de code (lettre + accent combinant, drapeaux, emojis composés). Les opérations correctes (longueur visible, découpe, majuscules, tri selon la langue) exigent une bibliothèque : **ICU**, **Boost.Locale**, **utf8cpp**. En C++26, `std::text_encoding` identifie les encodages. `std::toupper` et `<cctype>` ne fonctionnent que pour l'ASCII.

## 27.4 Entrées / sorties et console

- Sous **Linux et macOS**, le terminal est en UTF-8 par défaut : `std::cout` fonctionne directement avec des `std::string` UTF-8.
- Sous **Windows**, configurez la console en UTF-8 (`chcp 65001` ou `SetConsoleOutputCP(CP_UTF8)`) et compilez avec `/utf-8` (MSVC).
- `std::format` et `std::print` traitent correctement un texte UTF-8 lorsque le compilateur est réglé pour cet encodage.
- Les fichiers texte doivent avoir un encodage **connu** : UTF-8 sans BOM est le meilleur choix.

## 27.5 Conseils

- Utilisez **UTF-8 partout** : sources, fichiers, réseau, `std::string`.
- Considérez `std::string` comme une suite d'**octets UTF-8** ; ne supposez pas « 1 octet = 1 caractère ».
- Convertissez aux frontières (API Windows en UTF-16) et seulement là.
- Évitez `wchar_t` et `<codecvt>` (déprécié depuis C++17) dans du nouveau code.
- Testez avec des textes accentués, non latins et des emojis.

---

# 28. Compilation et exécution

## 28.1 Les étapes en pratique

```bash
g++ -std=c++20 -E main.cpp -o main.ii      # 1. préprocesseur : développe #include et macros
g++ -std=c++20 -S main.cpp -o main.s       # 2. compilation vers l'assembleur
g++ -std=c++20 -c main.cpp -o main.o       # 3. assemblage : fichier objet
g++ main.o -o prog                         # 4. édition de liens : exécutable
./prog                                     # 5. exécution
```

Les templates sont **instanciés** pendant la compilation de chaque fichier ; l'éditeur de liens élimine les doublons.

## 28.2 Options courantes

| Option | Rôle |
| --- | --- |
| `-std=c++20` | Choisit la norme (`c++17`, `c++23`, `c++2c`) |
| `-Wall -Wextra -Wpedantic` | Avertissements (à activer **toujours**) |
| `-Wconversion -Wshadow -Wold-style-cast` | Avertissements supplémentaires utiles |
| `-Werror` | Transforme les avertissements en erreurs |
| `-O0` / `-O2` / `-O3` / `-Os` | Niveaux d'optimisation (aucune, standard, agressive, taille) |
| `-g` | Informations de débogage |
| `-c` / `-o nom` | Compiler sans lier / nom de sortie |
| `-I dir` / `-L dir` / `-l nom` | Dossier d'en-têtes / de bibliothèques / bibliothèque à lier |
| `-DNOM=val` | Définit une macro (`-DNDEBUG`) |
| `-fsanitize=address,undefined` | Détection d'erreurs mémoire et de comportements indéfinis |
| `-fsanitize=thread` | Détection de courses de données |
| `-pthread` | Support des threads |
| `-flto` | Optimisation à l'édition de liens |
| `-fno-exceptions`, `-fno-rtti` | Désactive exceptions / RTTI (embarqué) |
| `-shared -fPIC` | Bibliothèque dynamique |
| `-fhardened` (GCC 14+) | Active un ensemble d'options de durcissement |

## 28.3 Erreurs de compilation et d'édition de liens

| Message (typique) | Cause | Solution |
| --- | --- | --- |
| `'x' was not declared in this scope` | Nom inconnu : include ou `std::` oublié | Inclure l'en-tête, qualifier le nom |
| `no matching function for call to ...` | Aucune surcharge ou instance de template ne convient | Vérifier les types des arguments ; lire la liste des candidats |
| Cascade d'erreurs de templates | Type ne satisfaisant pas les exigences | Lire **la première** erreur ; utiliser des concepts |
| `undefined reference to 'f()'` | Fonction déclarée mais jamais définie / fichier ou bibliothèque non lié | Ajouter le `.cpp` ou `-l` manquant |
| `undefined reference to 'vtable for X'` | Fonction virtuelle déclarée sans définition | Définir toutes les fonctions virtuelles non pures |
| `multiple definition of 'f()'` | Fonction non `inline` définie dans un en-tête inclus plusieurs fois (violation de l'ODR) | `inline`, ou déplacer dans un `.cpp` |
| `redefinition of 'class X'` | Garde d'inclusion absente | `#pragma once` |

> **Bonne pratique** : Lisez les erreurs **de haut en bas** : la première est souvent la cause, les suivantes ses conséquences.

## 28.4 Projets multi-fichiers

```bash
g++ -std=c++20 -Wall -Wextra -c main.cpp -o main.o       # compile chaque fichier séparément
g++ -std=c++20 -Wall -Wextra -c maths.cpp -o maths.o
g++ main.o maths.o -o prog                               # lie les fichiers objets
```

Seuls les fichiers modifiés sont recompilés : c'est le rôle des systèmes de build.

## 28.5 Automatiser : `make` et CMake

```make
# Makefile (les lignes de commande commencent par une tabulation)
CXX      = g++
CXXFLAGS = -std=c++20 -Wall -Wextra -O2

prog: main.o maths.o
	$(CXX) $^ -o $@

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f *.o prog
```

**CMake** est le standard de fait pour les projets C++ : il génère les fichiers de build (Make, Ninja, Visual Studio…).

```cmake
cmake_minimum_required(VERSION 3.20)
project(MonProjet LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)                       # -std=c++20 plutôt que gnu++20

add_executable(prog main.cpp maths.cpp)
target_compile_options(prog PRIVATE -Wall -Wextra -Wpedantic)
```

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release       # configure
cmake --build build                                  # compile
./build/prog
```

Pour les dépendances : **vcpkg**, **Conan** ou `FetchContent` de CMake.

## 28.6 Bibliothèques

```bash
# Bibliothèque statique
g++ -c maths.cpp -o maths.o
ar rcs libmaths.a maths.o
g++ main.cpp -L. -lmaths -o prog

# Bibliothèque dynamique
g++ -fPIC -shared maths.cpp -o libmaths.so
g++ main.cpp -L. -lmaths -o prog
LD_LIBRARY_PATH=. ./prog                              # indique où chercher la .so à l'exécution (Linux)
```

| | Statique (`.a`, `.lib`) | Dynamique (`.so`, `.dll`, `.dylib`) |
| --- | --- | --- |
| Intégration | Copiée dans l'exécutable | Chargée à l'exécution |
| Taille | Exécutable plus gros | Exécutable plus petit |
| Mise à jour | Recompilation | Remplacement du fichier |

> **Attention** : Il n'existe **pas d'interface binaire (ABI) C++ stable** entre compilateurs ou versions de bibliothèque standard (par exemple `libstdc++` et `libc++`). Pour une bibliothèque dynamique distribuée, exposez une interface `extern "C"` ou compilez tout avec la même chaîne d'outils. Beaucoup de bibliothèques C++ sont **header-only** (aucune liaison nécessaire).

## 28.7 Débogage

```bash
g++ -g -O0 -std=c++20 prog.cpp -o prog
gdb ./prog
```

| Commande `gdb` | Rôle |
| --- | --- |
| `break main` / `break fichier.cpp:42` | Point d'arrêt |
| `run` / `run arg1 arg2` | Lancer |
| `next` / `step` / `continue` | Ligne suivante / entrer dans la fonction / reprendre |
| `print x` / `print v` | Afficher une variable ou un conteneur |
| `backtrace` | Pile d'appels |
| `watch x` | Surveiller une variable |
| `info locals` | Variables locales |

Les **sanitizers** (`-fsanitize=address,undefined`, `-fsanitize=thread`) et **Valgrind** détectent la plupart des erreurs mémoire et courses de données à l'exécution. Depuis C++23, `<stacktrace>` permet d'afficher la pile d'appels depuis le programme (selon la bibliothèque, une option de liaison supplémentaire peut être nécessaire).

## 28.8 Optimisation et profilage

- Développez en `-O0 -g` avec sanitizers ; livrez en `-O2` (ou `-O3`) avec `-DNDEBUG`.
- **Mesurez avant d'optimiser** : `perf`, `gprof`, Valgrind (`callgrind`), Google Benchmark.
- Les gains viennent d'abord de l'**algorithme** et de la **structure de données** (`vector` plutôt que `list`, `reserve`, éviter les copies), pas des micro-optimisations.
- **Compiler Explorer** (godbolt.org) montre le code assembleur généré.

## 28.9 Compilation croisée

```bash
arm-linux-gnueabihf-g++ -std=c++20 -O2 prog.cpp -o prog_arm      # génère un exécutable ARM depuis un PC x86
```

Avec CMake : `-DCMAKE_TOOLCHAIN_FILE=toolchain.cmake`.

## 28.10 Name mangling et `extern "C"`

Comme le C++ autorise la surcharge, le compilateur **encode** les types dans le nom des symboles (*name mangling*). Le C n'en a pas besoin : pour les faire cohabiter, on déclare `extern "C"`.

```cpp
// carre.cpp
int carre(int x) { return x * x; }                 // symbole généré : _Z5carrei
extern "C" int carre_c(int x) { return x * x; }    // symbole généré : carre_c (visible par du C)
```

```bash
g++ -c carre.cpp -o carre.o
nm carre.o                       # liste les symboles
nm -C carre.o                    # les « démangle » (affiche carre(int))
c++filt _Z5carrei                # décode un nom : carre(int)
```

## 28.11 Environnement d'exécution

Avant `main`, le programme initialise les **variables globales et statiques** (constructeurs) ; à la sortie de `main`, il appelle les fonctions de `std::atexit` puis les **destructeurs** des objets statiques.

| | Bibliothèque standard C++ | Appels système |
| --- | --- | --- |
| Exemples | `std::ofstream`, `std::cout`, `new` | `write`, `open`, `brk` / `mmap` |
| Portabilité | Standard C++ | Dépend du système (POSIX, API Windows) |
| Rôle | Couche confortable, **tamponnée**, typée | Interface directe avec le noyau |

---

# 29. Comportements indéfinis, exceptions et sécurité

*(Section ajoutée : c'est la clé pour écrire du C++ fiable.)*

## 29.1 Comportement indéfini (UB)

Quand un programme viole une règle du langage, **la norme n'impose aucun résultat** : plantage, résultat faux, **ou apparente normalité** (avant de casser avec un autre compilateur ou niveau d'optimisation). Le compilateur peut **supposer que l'UB n'arrive jamais** et optimiser en conséquence.

| Catégorie | Exemples |
| --- | --- |
| **Mémoire** | Accès hors bornes (`v[i]`, `t[i]`), déréférencement de `nullptr`, *use-after-free*, double `delete`, `delete` / `delete[]` incohérents |
| **Durée de vie** | Référence, pointeur, `string_view`, `span` ou itérateur **pendant** ; itérateur invalidé par une modification du conteneur |
| **Arithmétique** | Débordement d'entier **signé**, division par zéro, décalage invalide |
| **Pointeurs et types** | Violation d'alias strict, lecture d'un membre inactif d'une `union`, `reinterpret_cast` hasardeux, *downcast* `static_cast` incorrect |
| **Séquencement** | `i = i++ + ++i;` (modifications non séquencées) |
| **Objets** | Lecture d'une variable non initialisée (devient un « comportement erroné » en C++26), appel d'une fonction virtuelle pure depuis un constructeur |
| **Concurrence** | **Course de données** (accès simultanés dont un en écriture, sans synchronisation) |
| **Divers** | Violation de l'ODR, `*opt` sur un `std::optional` vide, `std::unreachable()` atteint |

## 29.2 Les failles de sécurité typiques

| Faille | Cause | Parade |
| --- | --- | --- |
| **Dépassement de tampon** | `strcpy`, `memcpy`, `v[i]` non vérifié, `gets` | `std::string`, `std::span`, `at()`, bibliothèque durcie |
| **Chaîne de format** | `printf(saisie)` | `std::format` / `std::print` (format vérifié à la compilation) |
| **Dépassement d'entier** avant allocation | `new T[n * taille]` avec `n` énorme | Vérification explicite, `std::vector` |
| **Use-after-free / double free** | Propriété floue | `unique_ptr`, RAII, sanitizers |
| **Invalidation d'itérateurs** | Modification pendant un parcours | Algorithmes (`erase_if`), `reserve` |
| **Lecture non initialisée** | Variable locale sans valeur | Initialiser avec `{}` |
| **Confusion de types** | `reinterpret_cast`, `static_cast` descendant | `dynamic_cast`, `std::variant`, `std::bit_cast` |
| **Course de données** | Accès concurrents non protégés | `mutex`, `atomic`, ThreadSanitizer |

## 29.3 Hygiène de programmation

- Compilez avec `-Wall -Wextra -Wpedantic` (et `-Wconversion -Wshadow`) et corrigez **tous** les avertissements.
- Développez avec **AddressSanitizer + UBSan** (et ThreadSanitizer pour le multi-thread) ; testez aussi avec **Valgrind**.
- **Validez toutes les entrées** (taille, plage, format) et vérifiez les erreurs.
- N'utilisez jamais de tableau + taille séparée : préférez `std::vector`, `std::array`, `std::span`.
- Initialisez toutes les variables ; utilisez `const`, `constexpr`, `explicit`, `override`, `[[nodiscard]]`.
- Pas de `new` / `delete` nus : RAII partout.
- Réduisez la portée ; évitez les variables globales.
- Utilisez des analyseurs statiques (`clang-tidy`, `cppcheck`, `-fanalyzer`) et des tests automatisés (Catch2, GoogleTest, doctest).
- Suivez des règles reconnues : **C++ Core Guidelines**, **SEI CERT C++**, **MISRA C++:2023**.

```cpp
#include <array>
#include <cassert>
#include <iostream>
#include <span>

int premier(std::span<const int> v) {
    assert(!v.empty());                 // vérification de développement (désactivée avec -DNDEBUG)
    return v.front();
}

int main() {
    std::array<int, 3> t{4, 5, 6};
    std::cout << premier(t) << '\n';           // 4
    std::cout << t.at(1) << '\n';              // 5 : accès vérifié

    try {
        std::cout << t.at(5) << '\n';          // lève std::out_of_range au lieu d'un comportement indéfini
    } catch (const std::out_of_range &e) {
        std::cerr << "erreur : " << e.what() << '\n';
    }

    std::span<const int> vide;
    std::cerr << "Le prochain assert échoue :\n";
    premier(vide);                              // échec : message sur stderr puis arrêt du programme (abort)
    return 0;
}
```

## 29.4 Exceptions et sûreté *(ajout)*

Les exceptions séparent le **chemin normal** du **traitement d'erreur**. Leur sûreté repose sur le **RAII** : lors de la remontée de la pile, les destructeurs des objets locaux libèrent les ressources.

```cpp
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>

class ErreurFichier : public std::runtime_error {              // exception personnalisée : dérive de std::exception
    std::string chemin_;
public:
    ErreurFichier(const std::string &chemin, const std::string &msg)
        : std::runtime_error(msg + " : " + chemin), chemin_(chemin) {}
    const std::string &chemin() const noexcept { return chemin_; }
};

std::string lire(const std::string &chemin) {
    std::ifstream f(chemin);
    if (!f) throw ErreurFichier(chemin, "ouverture impossible");
    std::string ligne;
    std::getline(f, ligne);
    return ligne;
}

int main() {
    try {
        std::cout << lire("absent.txt") << '\n';
    } catch (const ErreurFichier &e) {
        std::cerr << e.what() << " (chemin=" << e.chemin() << ")\n";
    } catch (const std::exception &e) {
        std::cerr << "autre erreur : " << e.what() << '\n';
        throw;                                                  // relance l'exception courante
    }
    return 0;
}
```

| Garantie | Signification |
| --- | --- |
| **Sans exception** (`noexcept`) | L'opération ne lève jamais (destructeurs, `swap`, déplacements) |
| **Forte** | En cas d'exception, l'état est **inchangé** (technique : copier, puis échanger) |
| **De base** | Aucune fuite, objets valides mais dans un état indéterminé |

- Les **destructeurs** sont `noexcept` par défaut : ne laissez jamais une exception en sortir.
- Marquez `noexcept` les constructeurs et affectations de déplacement : les conteneurs s'en servent pour déplacer plutôt que copier.
- Une exception non capturée, ou qui franchit un `noexcept`, appelle `std::terminate`.

Pour les erreurs **attendues** (entrée invalide, fichier absent), `std::optional` et `std::expected` *(C++23)* évitent les exceptions :

```cpp
#include <charconv>
#include <expected>
#include <iostream>
#include <string>
#include <string_view>

std::expected<int, std::string> analyser(std::string_view s) {
    int v{};
    auto [ptr, ec] = std::from_chars(s.data(), s.data() + s.size(), v);
    if (ec != std::errc{} || ptr != s.data() + s.size()) return std::unexpected(std::string("entier invalide : ") + std::string(s));
    return v;                                                    // valeur
}

int main() {
    for (std::string_view texte : {"42", "4x2"}) {
        if (auto r = analyser(texte)) std::cout << "ok : " << *r << '\n';
        else std::cout << "erreur : " << r.error() << '\n';
    }
    return 0;
}
```

| Mécanisme | Quand l'utiliser |
| --- | --- |
| **Exception** | Erreur exceptionnelle, que l'appelant immédiat ne peut pas traiter ; échec de construction |
| `std::optional<T>` | Résultat qui peut simplement être absent |
| `std::expected<T, E>` | Résultat **ou** erreur détaillée, attendue et fréquente |
| Code de retour | Interfaces C, code sans exceptions (`-fno-exceptions`) |
| `assert` / contrat | Erreur de **programmation** (précondition violée) |

## 29.5 Contrats et bibliothèque durcie *(C++26, ajout)*

Le C++26 renforce la sûreté sans réécriture complète du code.

**Contrats** : préconditions et postconditions déclarées dans l'interface, vérifiées selon la **sémantique** choisie à la compilation (ignorée, observée, appliquée, application rapide).

```cpp
int racine_entiere(int n)
    pre(n >= 0)                          // précondition : vérifiée à l'appel
    post(r : r * r <= n)                 // postcondition sur la valeur de retour « r »
{
    int r = 0;
    while ((r + 1) * (r + 1) <= n) ++r;
    contract_assert(r >= 0);             // assertion interne
    return r;
}
```

> **Remarque** : Cette syntaxe est celle de C++26 et nécessite un compilateur récent qui l'implémente (le support est en cours d'arrivée dans GCC et Clang). Avant cela, utilisez `assert` et la documentation des préconditions.

**Bibliothèque standard durcie** : les préconditions de la bibliothèque (`operator[]` de `vector`, `span`, `string`, `optional`…) deviennent **vérifiées** en mode durci : un accès hors bornes arrête le programme au lieu de produire un comportement indéfini. Les implémentations proposent déjà des modes équivalents :

| Bibliothèque | Activation |
| --- | --- |
| libstdc++ (GCC) | `-D_GLIBCXX_ASSERTIONS` (ou `-fhardened`) |
| libc++ (Clang) | `-D_LIBCPP_HARDENING_MODE=_LIBCPP_HARDENING_MODE_EXTENSIVE` |
| MSVC | Mode de débogage (`_ITERATOR_DEBUG_LEVEL`) et options de durcissement |

Autres apports de la norme et de l'écosystème : lecture de variable non initialisée traitée comme un **comportement erroné** (au lieu d'un UB), analyseurs statiques (`clang-tidy` avec les profils des Core Guidelines), bibliothèque **GSL** (`gsl::not_null`, `gsl::span`).

---

# 30. Bibliothèque standard et aide-mémoire

## 30.1 En-têtes principaux

| En-tête | Contenu |
| --- | --- |
| `<iostream>`, `<fstream>`, `<sstream>`, `<iomanip>` | Flux de console, de fichiers, de chaînes ; manipulateurs |
| `<format>` / `<print>` | `std::format`, `std::print`, `std::println` |
| `<string>` / `<string_view>` | `std::string`, `std::string_view`, conversions |
| `<vector>`, `<array>`, `<deque>`, `<list>`, `<forward_list>` | Conteneurs séquentiels |
| `<map>`, `<set>`, `<unordered_map>`, `<unordered_set>`, `<flat_map>` | Conteneurs associatifs |
| `<stack>`, `<queue>` | Adaptateurs |
| `<span>`, `<mdspan>` | Vues sur des suites contiguës (1 dimension, multi-dimensions) |
| `<algorithm>`, `<numeric>`, `<ranges>`, `<iterator>` | Algorithmes, ranges, itérateurs |
| `<memory>` | Pointeurs intelligents, allocateurs |
| `<utility>`, `<tuple>` | `pair`, `move`, `forward`, `tuple`, `swap` |
| `<optional>`, `<variant>`, `<any>`, `<expected>` | Types « enveloppes » |
| `<functional>` | `std::function`, `bind`, `less`, `greater`… |
| `<cmath>`, `<numbers>`, `<complex>` | Mathématiques |
| `<cstdint>`, `<limits>`, `<cstddef>` | Entiers de taille fixe, limites, `size_t` |
| `<bit>`, `<bitset>` | Manipulation de bits |
| `<chrono>`, `<ctime>` | Durées, horloges, dates |
| `<random>` | Générateurs et distributions aléatoires |
| `<filesystem>` | Chemins, dossiers, fichiers |
| `<regex>` | Expressions régulières |
| `<stdexcept>`, `<exception>`, `<system_error>` | Exceptions |
| `<concepts>`, `<type_traits>` | Concepts, traits de types |
| `<thread>`, `<mutex>`, `<atomic>`, `<future>`, `<condition_variable>` | Concurrence |
| `<coroutine>`, `<generator>` | Coroutines (C++20), générateurs (C++23) |
| `<source_location>`, `<stacktrace>` | Diagnostic |
| `<cassert>`, `<cstdlib>`, `<cstring>`, `<cctype>` | Héritage du C |
| `<version>` | Macros de test de fonctionnalités |

### Nombres aléatoires

```cpp
#include <iostream>
#include <random>

int main() {
    std::random_device graine;                          // source non déterministe (matériel / système)
    std::mt19937 gen(graine());                         // générateur Mersenne Twister
    std::uniform_int_distribution<int> de(1, 6);        // distribution uniforme

    for (int i = 0; i < 5; ++i) std::cout << "lancer " << i + 1 << " : " << de(gen) << '\n';
    return 0;                                           // (ne convient pas à la cryptographie)
}
```

### Mesurer le temps

```cpp
#include <chrono>
#include <iostream>

int main() {
    using horloge = std::chrono::steady_clock;
    auto debut = horloge::now();

    long long s = 0;
    for (int i = 0; i < 100'000'000; ++i) s += i % 7;

    auto fin = horloge::now();
    auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(fin - debut);
    std::cout << s << " en " << ms.count() << " ms\n";
    return 0;
}
```

## 30.2 Aperçu de la concurrence *(ajout)*

```cpp
#include <atomic>
#include <future>
#include <iostream>
#include <mutex>
#include <thread>
#include <vector>

int main() {
    std::atomic<int> compteur{0};              // opérations atomiques : sans verrou
    int protege = 0;
    std::mutex m;                              // exclusion mutuelle pour les données non atomiques

    {
        std::vector<std::jthread> fils;        // jthread : se joint automatiquement à la destruction (C++20)
        for (int i = 0; i < 4; ++i) {
            fils.emplace_back([&] {
                for (int k = 0; k < 1000; ++k) {
                    ++compteur;
                    std::lock_guard verrou(m); // RAII : verrou libéré à la fin de la portée
                    ++protege;
                }
            });
        }
    }                                          // tous les threads sont terminés ici

    auto resultat = std::async(std::launch::async, [] { return 6 * 7; });   // calcul asynchrone
    std::cout << compteur << ' ' << protege << ' ' << resultat.get() << '\n';   // 4000 4000 42
    return 0;
}
```

```bash
g++ -std=c++20 -pthread -fsanitize=thread conc.cpp -o conc     # ThreadSanitizer détecte les courses
```

| Outil | Rôle |
| --- | --- |
| `std::thread`, `std::jthread` | Fils d'exécution (`jthread` se joint tout seul et supporte l'arrêt coopératif) |
| `std::mutex` + `std::lock_guard` / `std::scoped_lock` | Protéger une section critique |
| `std::atomic<T>` | Variable partagée sans verrou |
| `std::async`, `std::future`, `std::promise` | Résultats asynchrones |
| `std::condition_variable` | Attendre un événement |
| `std::execution` *(C++26)* | Modèle unifié d'émetteurs / récepteurs pour l'asynchronisme et le parallélisme |

> **Attention** : Un accès concurrent à une même donnée, dont un en écriture et sans synchronisation, est une **course de données** : comportement indéfini. Partagez le moins possible, protégez le reste.

## 30.3 Récapitulatif par thème

| Besoin | Outil |
| --- | --- |
| Tableau de taille fixe | `std::array<T, N>` |
| Tableau de taille variable | `std::vector<T>` |
| Chaîne de caractères | `std::string` ; `std::string_view` en paramètre |
| Lire un nombre | `std::getline` + `std::from_chars` / `std::stoi` |
| Entier portable | `std::int32_t`, `std::uint64_t`, `std::size_t` |
| Modifier un argument | Référence `T &` |
| Retourner un résultat + erreur | `std::optional`, `std::expected`, exception |
| Plusieurs valeurs de retour | `struct`, `std::pair`, `std::tuple` |
| Callback | Lambda, paramètre template, `std::function` |
| Type « l'un parmi N » | `std::variant` + `std::visit` |
| Polymorphisme à l'exécution | Classe abstraite + `std::unique_ptr` |
| Polymorphisme à la compilation | Templates + concepts |
| Constante | `constexpr` (`consteval` si obligatoire) |
| Tri / recherche | `std::sort`, `std::ranges::sort`, `std::find`, `std::lower_bound` |
| Dictionnaire | `std::unordered_map` / `std::map` |
| Mémoire dynamique | `std::make_unique`, `std::make_shared` |
| Nettoyage | **RAII** (destructeurs) |
| Fichiers | `std::fstream`, `std::filesystem` |
| Formatage | `std::format`, `std::println` |
| Threads | `std::jthread`, `std::mutex`, `std::atomic` |

## 30.4 Les 12 règles d'or du C++

1. **Initialisez** tout (`int x{};`).
2. Appliquez le **RAII** : pas de `new` / `delete` nus ; `std::unique_ptr` et conteneurs.
3. Préférez la **bibliothèque standard** (`vector`, `string`, algorithmes) aux tableaux et chaînes du C.
4. **Passez** par valeur ou par `const T &`, **retournez** par valeur ; ne retournez jamais de référence, de pointeur ou de vue vers un objet local ou temporaire.
5. Utilisez `const`, `constexpr`, `explicit`, `override` et `[[nodiscard]]`.
6. Appliquez la **règle du zéro** (sinon la règle des cinq) ; un **destructeur virtuel** pour toute base polymorphe.
7. **Évitez les comportements indéfinis** : bornes, débordement signé, variables non initialisées, itérateurs et vues pendants, courses de données.
8. **Lancez par valeur, capturez par `const &`** ; `noexcept` pour destructeurs, déplacements et `swap`.
9. Pas de `using namespace` dans un en-tête ; pas de macro quand une fonctionnalité du langage suffit.
10. Compilez avec **tous les avertissements** et les **sanitizers** ; utilisez des analyseurs statiques.
11. Préférez la **composition** à l'héritage ; les templates avec **concepts** pour le polymorphisme statique.
12. **Documentez** qui possède la mémoire et quelles sont les préconditions ; suivez les **C++ Core Guidelines**.

## 30.5 Ressources pour progresser

- **cppreference (C++)** : <https://en.cppreference.com/w/cpp>
- **C++ Core Guidelines** : <https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines>
- **Standard C++ Foundation** : <https://isocpp.org>
- *A Tour of C++* — Bjarne Stroustrup ; *The C++ Programming Language* — Bjarne Stroustrup
- *Effective Modern C++* — Scott Meyers ; *C++ Primer* — Lippman, Lajoie, Moo
- **LearnCpp** : <https://www.learncpp.com>
- **Compiler Explorer** : <https://godbolt.org> · **C++ Insights** : <https://cppinsights.io>
- **Blog de Herb Sutter** (comptes rendus du comité) : <https://herbsutter.com>
- **SEI CERT C++ Coding Standard** : <https://wiki.sei.cmu.edu/confluence/display/cplusplus>
- **Documents du comité (WG21)** : <https://www.open-std.org/jtc1/sc22/wg21/>

---

<div align="center">

*Bon code, et que vos objets soient toujours détruits proprement !*

</div>
