<div align="center">

# Langage C — Guide complet

**Des premiers programmes à la gestion de la mémoire, aux fichiers et à la compilation**

*Mis à jour pour C17 / C23 (octobre 2026)*

</div>

---

## Ressources

| Ressource | Lien |
| --- | --- |
| Exercices | [exercises](/language/exercises/c) |
| Solutions | [solutions](/language/solutions/c) |
| Projets | [projects](/language/projects/c) |
| Référence | [cppreference.com (C)](https://en.cppreference.com/w/c) |
| Normes | [ISO/IEC 9899 (C23)](https://www.iso.org/standard/82075.html) · [Brouillons WG14](https://www.open-std.org/jtc1/sc22/wg14/) |

---

## Sommaire

**Niveau débutant**

1. [Introduction au C](#1-introduction-au-c)
2. [Structure d'un programme C](#2-structure-dun-programme-c)
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
17. [Pointeurs doubles](#17-pointeurs-doubles)
18. [Structures et unions](#18-structures-et-unions)
19. [Énumérations (`enum`)](#19-énumérations-enum)
20. [`typedef`](#20-typedef)
21. [Pointeurs de fonctions](#21-pointeurs-de-fonctions)

**Niveau avancé**

22. [Gestion des fichiers](#22-gestion-des-fichiers)
23. [Arguments de la ligne de commande](#23-arguments-de-la-ligne-de-commande)
24. [Directives du préprocesseur](#24-directives-du-préprocesseur)
25. [Opérateurs bit à bit](#25-opérateurs-bit-à-bit)
26. [Récursivité](#26-récursivité)
27. [Unicode et caractères larges](#27-unicode-et-caractères-larges)
28. [Compilation et exécution](#28-compilation-et-exécution)
29. [Comportements indéfinis et sécurité](#29-comportements-indéfinis-et-sécurité)
30. [Bibliothèque standard et aide-mémoire](#30-bibliothèque-standard-et-aide-mémoire)

> **Légende** : *(ajout)* = notion absente du guide d'origine ; *(à jour)* = pratique moderne remplaçant une ancienne ; *(C23)* = nouveauté de la norme de 2023.

---

# Niveau débutant

---

# 1. Introduction au C

## 1.1 Qu'est-ce que le C ?

Le **C** est un langage de programmation **compilé, impératif et procédural**, créé au début des années **1970** par **Dennis Ritchie** aux **Laboratoires Bell** (c. 1972), pour réécrire le système **UNIX**. On le qualifie de langage « de **niveau intermédiaire** » : il offre des structures de haut niveau (fonctions, boucles, structures) tout en donnant un accès direct à la **mémoire** et au matériel.

| Caractéristique | Détail |
| --- | --- |
| Paradigme | Procédural (impératif) |
| Typage | **Statique** et faiblement vérifié (conversions implicites nombreuses) |
| Exécution | Compilé vers du **code machine natif** |
| Gestion de la mémoire | **Manuelle** (`malloc` / `free`), pas de ramasse-miettes |
| Portabilité | Très bonne : compilateurs pour presque toutes les architectures |
| Influence | A inspiré C++, Objective-C, C#, Java, Go (syntaxe et concepts) |

## 1.2 Pourquoi apprendre le C ?

- **Systèmes** : noyaux (Linux, Windows, macOS/BSD), pilotes, systèmes embarqués.
- **Performance** : bases de données, moteurs de jeux, bibliothèques de calcul, interpréteurs (CPython, Lua…).
- **Microcontrôleurs** : Arduino, STM32, ESP32…
- **Comprendre l'ordinateur** : mémoire, pointeurs, pile, tas, compilation.
- **Interopérabilité** : l'interface binaire de C (*ABI*) sert de langue commune ; Python, Rust, Go, etc. appellent du code C.

> **Attention** : Revers de la médaille : le C **ne vous protège pas** (dépassements de tampon, pointeurs invalides…). Une bonne discipline et des outils d'analyse sont indispensables (voir [section 29](#29-comportements-indéfinis-et-sécurité)).

## 1.3 Histoire et normes *(à jour)*

| Norme | Année | Apports principaux |
| --- | --- | --- |
| **K&R C** | 1978 | Livre *The C Programming Language* (Kernighan & Ritchie) |
| **C89 / C90** (ANSI C) | 1989–90 | Première norme : prototypes de fonctions, `void`, `const` |
| **C99** | 1999 | Commentaires `//`, `long long`, `<stdint.h>`, `<stdbool.h>`, `inline`, tableaux de taille variable (VLA), initialisations désignées, déclarations n'importe où |
| **C11** | 2011 | `_Generic`, `_Static_assert`, `<threads.h>`, `_Atomic`, structures anonymes ; **`gets()` supprimée** |
| **C17** (C18) | 2018 | Version de correction de C11, sans nouvelle fonctionnalité |
| **C23** | 2023 (ISO : oct. 2024) | `bool`/`true`/`false` et `nullptr` en **mots-clés**, `constexpr`, `typeof`, `auto`, littéraux binaires `0b…`, séparateurs `'`, attributs `[[…]]`, `#embed`, `<stdbit.h>`, `<stdckdint.h>` |
| **C2y** | en cours | Prochaine révision en préparation par le comité WG14 |

Le compilateur choisit la norme avec `-std=` : `-std=c17`, `-std=c23` (ou `-std=gnu23`). **GCC 15 et suivants utilisent C23 par défaut** ; d'autres compilateurs (Clang, MSVC) ont des défauts différents selon la version : indiquez toujours `-std=` explicitement.

## 1.4 Fonctionnement d'un programme C

1. **Écrire** le code source dans un fichier `.c`.
2. **Compiler** : le compilateur (`gcc`, `clang`, MSVC…) le traduit en code machine.
3. **Exécuter** le programme obtenu.

```text
hello.c ──▶ préprocesseur ──▶ compilateur ──▶ assembleur ──▶ éditeur de liens ──▶ exécutable
 (source)      (.i)             (.s)            (.o)           (+ bibliothèques)
```

## 1.5 Installer un compilateur

| Système | Installation |
| --- | --- |
| **Linux (Debian/Ubuntu)** | `sudo apt install build-essential` (gcc, make) · `sudo apt install clang` |
| **macOS** | `xcode-select --install` (Clang) ou `brew install gcc` |
| **Windows** | **MSYS2** (`pacman -S mingw-w64-ucrt-x86_64-gcc`) ou **WSL** (Linux sous Windows, recommandé) ; ou **Visual Studio** (MSVC) |

```bash
gcc --version
```

> **Astuce** : Éditeurs et IDE : **VS Code** (extension C/C++), **CLion**, **Code::Blocks**, **Vim/Neovim**. Atelier en ligne : [Compiler Explorer](https://godbolt.org), [OnlineGDB](https://www.onlinegdb.com).

## 1.6 Premier programme : « Hello, World ! »

```c
#include <stdio.h>               // fonctions d'entrée/sortie

int main(void) {                 // point d'entrée du programme
    printf("Bonjour le monde !\n");   // affiche du texte
    return 0;                    // 0 = succès
}
```

| Élément | Rôle |
| --- | --- |
| `#include <stdio.h>` | Inclut les déclarations d'entrée/sortie (`printf`…) |
| `int main(void)` | Fonction principale : l'exécution commence ici |
| `printf` | Affiche du texte formaté |
| `\n` | Saut de ligne |
| `return 0;` | Code de sortie transmis au système (`0` = succès) |

> **Remarque** : Depuis **C99**, si `main` n'a pas de `return`, elle retourne **implicitement 0**. On l'écrit quand même par clarté.
> **Remarque** : `int main(void)` est préférable à `int main()` : en C (avant C23), `()` signifie « arguments non spécifiés ». En **C23**, `()` équivaut à `(void)`.

## 1.7 Compiler et exécuter

```bash
gcc -Wall -Wextra -std=c17 hello.c -o hello     # compiler
./hello                                         # exécuter (Linux/macOS)
hello.exe                                       # exécuter (Windows)
```

## 1.8 Erreurs fréquentes de débutant

| Erreur | Exemple | Correction |
| --- | --- | --- |
| Point-virgule oublié | `printf("Hi")` | Ajouter `;` |
| Faute de frappe | `pritnf("Hi");` | `printf` |
| Casse | `Main()` ou `Printf()` | C est **sensible à la casse** |
| Oubli de `#include` | `printf` sans `<stdio.h>` | Inclure l'en-tête |
| `=` au lieu de `==` | `if (x = 5)` | `if (x == 5)` |
| Variable non initialisée | `int x; printf("%d", x);` | Initialiser : `int x = 0;` |

---

# 2. Structure d'un programme C

## 2.1 Organisation générale

```c
#include <stdio.h>          // 1. Directives du préprocesseur
#define TAUX_TVA 0.2        //    constantes / macros

int compteur = 0;           // 2. Variables globales (à limiter)

int carre(int x);           // 3. Prototypes de fonctions

int main(void) {            // 4. Fonction principale
    int n = 5;              //    déclarations
    printf("Le carré de %d est %d\n", n, carre(n));   // instructions
    return 0;
}

int carre(int x) {          // 5. Définitions des autres fonctions
    return x * x;
}
```

## 2.2 Les composants

| Composant | Rôle |
| --- | --- |
| **Directives du préprocesseur** | Commencent par `#` ; traitées **avant** la compilation (`#include`, `#define`, `#ifdef`…) |
| **Déclarations globales** | Hors de toute fonction ; visibles dans tout le fichier après leur déclaration |
| **Prototypes** | Annoncent le type de retour et les paramètres d'une fonction |
| **`main()`** | Point d'entrée **obligatoire** (une seule par programme) |
| **Instructions** | Terminées par `;` |
| **Blocs** | Délimités par `{ }` |
| **Commentaires** | Ignorés par le compilateur |

## 2.3 Commentaires

```c
#include <stdio.h>

// Commentaire sur une ligne (C99)

/* Commentaire
   sur plusieurs lignes (ne s'imbrique pas) */

int main(void) {
    printf("Les commentaires sont ignorés par le compilateur.\n");   // affiche cette phrase
    return 0;
}
```

## 2.4 Variables et instructions

```c
#include <stdio.h>

int main(void) {
    int age;                     // déclaration
    age = 25;                    // affectation
    int taille = 180;            // déclaration + initialisation
    printf("age = %d, taille = %d\n", age, taille);
    return 0;
}
```

> **Bonne pratique** : Depuis **C99**, on peut déclarer une variable **n'importe où** dans un bloc (et dans l'en-tête d'un `for`), au plus près de son usage. Il n'est plus nécessaire de tout déclarer en début de fonction.

## 2.5 Code de sortie

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *f = fopen("fichier_inexistant.txt", "r");
    if (f == NULL) {
        fprintf(stderr, "Erreur : impossible d'ouvrir le fichier\n");
        return EXIT_FAILURE;     // erreur : le shell récupère 1 (echo $?)
    }
    fclose(f);
    printf("Fichier ouvert\n");
    return 0;                    // ou EXIT_SUCCESS (de <stdlib.h>)
}
```

Le shell récupère ce code : `echo $?` (Linux/macOS) ou `echo %ERRORLEVEL%` (Windows).

## 2.6 Les étapes de la compilation (rappel)

1. **Préprocessing** : `#include`, `#define`, compilation conditionnelle.
2. **Compilation** : `.c` → assembleur → `.o` (objet).
3. **Édition de liens** : assemblage des `.o` et des bibliothèques en exécutable.
4. **Exécution**.

Détails dans la [section 28](#28-compilation-et-exécution).

---

# 3. Syntaxe et mots-clés

## 3.1 Règles de syntaxe

- C est **sensible à la casse** : `Valeur` ≠ `valeur`.
- Chaque instruction se termine par **`;`**.
- Les blocs sont délimités par **`{ }`** ; l'indentation est libre mais indispensable à la lisibilité.
- Les espaces et sauts de ligne n'ont pas de signification particulière.

## 3.2 Identifiants

Noms de variables, fonctions, etc. : lettres, chiffres et `_`, **sans commencer par un chiffre**, ≠ mot-clé.

```c
#include <stdio.h>

int main(void) {
    int age_utilisateur = 30;    // valide : snake_case (convention courante en C)
    int _temp = 5;               // valide (mais _x est réservé dans certains contextes : évitez)
    printf("age_utilisateur = %d, _temp = %d\n", age_utilisateur, _temp);

    // Ces deux déclarations ne compilent pas :
    // int 2eme;   // error: expected identifier or '(' before numeric constant
    // int for;    // error: expected identifier or '(' before 'for'
    fprintf(stderr, "Erreur de compilation si on décommente : un identifiant ne commence pas par un chiffre et n'est pas un mot-clé\n");
    return 0;
}
```

> **Attention** : Évitez les noms commençant par `_` suivi d'une majuscule ou par `__` : **réservés à l'implémentation**. Les noms en `_t` sont réservés par POSIX.

## 3.3 Mots-clés du langage *(à jour : C23)*

| Catégorie | Mots-clés |
| --- | --- |
| **Types** | `int` `char` `short` `long` `float` `double` `void` `signed` `unsigned` `bool` *(C23)* `_Complex` `_BitInt` *(C23)* |
| **Qualificateurs** | `const` `volatile` `restrict` `_Atomic` |
| **Classes de stockage** | `auto` `register` `static` `extern` `thread_local` *(C23)* `constexpr` *(C23)* |
| **Types composés** | `struct` `union` `enum` `typedef` |
| **Contrôle** | `if` `else` `switch` `case` `default` `for` `while` `do` `break` `continue` `goto` `return` |
| **Divers** | `sizeof` `inline` `alignas` `alignof` `static_assert` `typeof` `typeof_unqual` `true` `false` `nullptr` *(C23)* `_Generic` `_Noreturn` |

> **À retenir** : En **C23**, `bool`, `true`, `false`, `nullptr`, `alignas`, `alignof`, `static_assert`, `thread_local` deviennent de vrais **mots-clés** (plus besoin de `<stdbool.h>` ni des anciennes formes `_Bool`, `_Alignas`, `_Static_assert`…). Dans un code destiné aux anciennes normes, incluez `<stdbool.h>`.

## 3.4 Ponctuation et délimiteurs

| Symbole | Usage |
| --- | --- |
| `;` | Fin d'instruction |
| `,` | Séparateur (arguments, déclarations, opérateur virgule) |
| `{ }` | Bloc, initialiseurs |
| `( )` | Appels, regroupement |
| `[ ]` | Indices de tableau |
| `#` | Directive du préprocesseur |
| `* &` | Pointeur / déréférencement ; adresse |
| `->` `.` | Accès aux membres d'une structure |

## 3.5 Attributs *(C23)*

Nouvelle syntaxe standard `[[ ... ]]` pour guider le compilateur :

```c
// Compiler avec : gcc -std=c23 attributs.c -o attributs
#include <stdio.h>
#include <stdlib.h>

[[nodiscard]] int ouvrir(const char *chemin) {      // avertit si le résultat est ignoré
    FILE *f = fopen(chemin, "r");
    if (f == NULL) return -1;
    fclose(f);
    return 0;
}

[[maybe_unused]] static int experimental = 0;       // pas d'avertissement si inutilisée

[[deprecated("Utiliser nouvelle_fonction")]] void ancienne(void) { puts("ancienne"); }
void nouvelle_fonction(void) { puts("nouvelle"); }

[[noreturn]] void arreter(const char *message) {
    fprintf(stderr, "Erreur : %s\n", message);
    exit(EXIT_FAILURE);
}

int main(void) {
    int x = 1;
    switch (x) {
        case 1: puts("cas 1"); [[fallthrough]];     // passage volontaire au cas suivant
        case 2: puts("cas 2"); break;
        default: break;
    }
    nouvelle_fonction();
    // ancienne();   // warning: 'ancienne' is deprecated: Utiliser nouvelle_fonction
    if (ouvrir("fichier_inexistant.txt") != 0) {
        arreter("fichier introuvable");
    }
    return 0;
}
```

---

# 4. Types de données et variables

## 4.1 Types fondamentaux

| Type | Rôle | Taille usuelle* | Spécificateur `printf` |
| --- | --- | --- | --- |
| `char` | Caractère / petit entier | 1 octet | `%c` (ou `%d`) |
| `short` | Entier court | 2 octets | `%hd` |
| `int` | Entier | 4 octets | `%d` |
| `long` | Entier long | 4 ou 8 octets | `%ld` |
| `long long` | Entier très long (C99) | 8 octets | `%lld` |
| `float` | Réel simple précision | 4 octets | `%f` |
| `double` | Réel double précision | 8 octets | `%f` (`%lf` pour `scanf`) |
| `long double` | Réel étendu | 8 à 16 octets | `%Lf` |
| `bool` | Booléen (C23 ; sinon `<stdbool.h>`) | 1 octet | `%d` |
| `void` | Absence de type | — | — |

\* **Les tailles dépendent de la plateforme** : la norme ne fixe que des minimums. Vérifiez avec `sizeof`.

```c
#include <stdio.h>
#include <limits.h>
#include <float.h>

int main(void) {
    printf("int : %zu octets, plage [%d ; %d]\n", sizeof(int), INT_MIN, INT_MAX);
    printf("double : %zu octets, epsilon = %g\n", sizeof(double), DBL_EPSILON);
    return 0;
}
```

> **Bonne pratique** : `sizeof` renvoie un `size_t` : affichez-le avec **`%zu`**.

## 4.2 Modificateurs : `signed`, `unsigned`, `short`, `long`

```c
#include <stdio.h>

int main(void) {
    unsigned int positif = 4000000000u;
    signed char petit = -100;
    unsigned long long enorme = 18446744073709551615ULL;
    printf("positif = %u\n", positif);
    printf("petit   = %d\n", petit);
    printf("enorme  = %llu\n", enorme);
    return 0;
}
```

| Type non signé | Plage (32 bits) |
| --- | --- |
| `unsigned int` | 0 à 4 294 967 295 |
| `int` | −2 147 483 648 à 2 147 483 647 |

> **Attention** : Le débordement d'un entier **signé** est un **comportement indéfini** ; celui d'un entier **non signé** « boucle » (modulo 2ⁿ).
> **Attention** : `char` peut être signé **ou** non selon la plateforme : utilisez `unsigned char` pour des octets.

## 4.3 Entiers à taille fixe : `<stdint.h>` *(ajout, à jour)*

Pour du code **portable** et prévisible, préférez ces types :

```c
#include <stdio.h>
#include <stddef.h>
#include <stdint.h>
#include <inttypes.h>      // macros d'affichage

int main(void) {
    int8_t   a = -8;   uint8_t  b = 200;                 // 8 bits
    int16_t  c = -1600; uint16_t d = 60000;              // 16 bits
    int32_t  e = -100000; uint32_t f = 4000000000u;      // 32 bits
    int64_t  g = -9000000000000000000LL; uint64_t h = 18000000000000000000ULL;   // 64 bits
    size_t   taille = sizeof g;   // taille d'objets / indices de tableaux (<stddef.h>)
    intptr_t p = (intptr_t)&a;    // entier pouvant contenir un pointeur

    printf("%d %u %d %u\n", a, (unsigned)b, c, (unsigned)d);
    printf("%" PRId32 " %" PRIu32 "\n", e, f);
    printf("%" PRId64 " %" PRIu64 "\n", g, h);   // affichage portable
    printf("%zu\n", taille);                     // affichage d'un size_t
    printf("intptr_t non nul : %d\n", p != 0);
    return 0;
}
```

## 4.4 Booléens

```c
#include <stdio.h>
#include <stdbool.h>   // inutile en C23 (bool est un mot-clé), nécessaire de C99 à C17

int main(void) {
    bool actif = true;
    bool ok = false;
    printf("actif = %d, ok = %d\n", actif, ok);
    if (5) printf("Toute valeur non nulle est vraie\n");
    if (!0) printf("0 est faux, !0 est vrai\n");
    return 0;
}
```

En C, toute valeur **non nulle** est « vraie » ; `0` est « faux ».

## 4.5 Déclarer, initialiser, affecter

```c
#include <stdio.h>

int main(void) {
    int a;                      // Attention : valeur indéterminée (locale), on ne la lit pas
    a = 1;                      // affectation avant toute lecture
    int b = 10;                 // initialisée
    int x = 1, y = 2, z;        // plusieurs
    z = x + y;
    const double PI = 3.14159;  // constante
    int n = {0};                // initialisation par accolades
    int m = {};                 // initialisation à zéro (C23, compiler avec -std=c23)
    printf("a=%d b=%d x=%d y=%d z=%d PI=%.5f n=%d m=%d\n", a, b, x, y, z, PI, n, m);
    return 0;
}
```

> **Attention** : Les variables **locales non initialisées** contiennent des valeurs aléatoires ; les variables **globales / statiques** sont initialisées à 0 par défaut.

### Inférence de type avec `auto` *(C23)*

```c
// Compiler avec : gcc -std=c23 auto.c -o auto
#include <stdio.h>

int main(void) {
    auto compteur = 0;          // type déduit : int
    auto ratio = 3.14;          // double
    typeof(ratio) copie = ratio;   // typeof : même type que ratio
    printf("compteur = %d, ratio = %.2f, copie = %.2f\n", compteur, ratio, copie);
    printf("sizeof(compteur) = %zu, sizeof(ratio) = %zu\n", sizeof compteur, sizeof ratio);
    return 0;
}
```

Utile avec `typeof` : `typeof(expr) copie = expr;`.

## 4.6 Conversions de types (*casts*)

```c
#include <stdio.h>

int main(void) {
    int a = 5, b = 2;
    float r1 = a / b;            // 2.0  division entière d'abord
    float r2 = (float)a / b;     // 2.5  conversion explicite
    int  n  = (int)3.99;         // 3 (troncature)
    char c  = 'A' + 1;           // 'B'
    printf("r1 = %.1f, r2 = %.1f, n = %d, c = %c\n", r1, r2, n, c);
    printf("-1 < 1u est %s\n", (-1 < 1u) ? "vrai" : "faux");   // faux : -1 devient un grand non signé
    return 0;
}
```

Règles : une opération entre `int` et `double` convertit en `double` (**promotion**) ; un `char`/`short` est promu en `int` dans les calculs. Évitez de mélanger signé et non signé (`-1 < 1u` est faux !).

## 4.7 Bonnes pratiques

- **Initialisez** toujours vos variables.
- Utilisez `size_t` pour les tailles et les indices, `<stdint.h>` pour des largeurs exactes.
- Choisissez des noms explicites (`nombre_eleves` plutôt que `n`).
- Compilez avec `-Wall -Wextra` : le compilateur signale de nombreuses erreurs de conversion.

---

# 5. Constantes et littéraux

## 5.1 Littéraux

| Type | Exemples |
| --- | --- |
| Entier décimal | `42`, `-7` |
| Octal | `052` (commence par `0`) |
| Hexadécimal | `0x2A`, `0xFF` |
| **Binaire** *(C23)* | `0b101010` |
| Séparateur de chiffres *(C23)* | `1'000'000` |
| Suffixes entiers | `42u` (unsigned), `42L` (long), `42ULL` (unsigned long long) |
| Réel | `3.14`, `1.5e3`, `2.5f` (float) |
| Caractère | `'A'`, `'\n'`, `'\0'` |
| Chaîne | `"Bonjour"` |
| Booléen *(C23)* | `true`, `false` |
| Pointeur nul *(C23)* | `nullptr` (avant : `NULL`) |

### Séquences d'échappement

| Séquence | Signification |
| --- | --- |
| `\n` | Nouvelle ligne |
| `\t` | Tabulation |
| `\\` | Antislash |
| `\'` / `\"` | Apostrophe / guillemet |
| `\0` | Caractère nul (fin de chaîne) |
| `\r` | Retour chariot |
| `\xHH` | Valeur hexadécimale |
| `\a` | Signal sonore |

## 5.2 Définir des constantes

Il existe **quatre** moyens, aux usages différents :

| Moyen | Exemple | Remarques |
| --- | --- | --- |
| `#define` | `#define TAILLE 100` | Remplacement **textuel** avant la compilation, **sans type** |
| `const` | `const int taille = 100;` | Variable en lecture seule, **typée** |
| `enum` | `enum { TAILLE = 100 };` | Constantes entières, utilisables comme taille de tableau |
| `constexpr` *(C23)* | `constexpr int taille = 100;` | Vraie **constante de compilation**, typée |

```c
// Compiler avec : gcc -std=c23 constantes.c -o constantes
#include <stdio.h>

#define PI 3.14159                    // sans point-virgule !
const double TVA = 0.2;
constexpr int MAX_ELEVES = 30;        // C23
enum { TAILLE = 100 };

int main(void) {
    int notes[MAX_ELEVES];
    int grille[TAILLE];
    printf("PI = %.5f, TVA = %.1f\n", PI, TVA);
    printf("notes : %zu éléments, grille : %zu éléments\n",
           sizeof notes / sizeof notes[0], sizeof grille / sizeof grille[0]);
    return 0;
}
```

> **Bonne pratique** : Préférez `const` / `constexpr` / `enum` à `#define` pour les constantes : ils sont **typés**, respectent la portée et facilitent le débogage.
> **Attention** : En C (avant C23), `const int n = 5; int t[n];` crée un VLA, pas un tableau de taille constante.

## 5.3 `const` et pointeurs

```c
#include <stdio.h>

int main(void) {
    int x = 10, y = 20;
    const int *p1 = &x;          // pointeur vers un int CONSTANT (on ne modifie pas *p1)
    int *const p2 = &x;          // pointeur CONSTANT (on ne change pas p2)
    const int *const p3 = &x;    // les deux

    p1 = &y;                     // autorisé : p1 peut pointer ailleurs
    *p2 = 11;                    // autorisé : on modifie la valeur pointée
    printf("*p1 = %d, *p2 = %d, *p3 = %d\n", *p1, *p2, *p3);

    // *p1 = 5;   // error: assignment of read-only location '*p1'
    // p2 = &y;   // error: assignment of read-only variable 'p2'
    // p3 = &y;   // error: assignment of read-only variable 'p3'
    fprintf(stderr, "Erreur de compilation si on décommente les trois dernières affectations\n");
    return 0;
}
```

Astuce de lecture : lisez la déclaration **de droite à gauche**.

## 5.4 Constantes prédéfinies utiles

```c
#include <float.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    printf("INT_MAX = %d, INT_MIN = %d, UINT_MAX = %u\n", INT_MAX, INT_MIN, UINT_MAX);   // <limits.h>
    printf("DBL_MAX = %g, DBL_EPSILON = %g\n", DBL_MAX, DBL_EPSILON);                    // <float.h>
    printf("EXIT_SUCCESS = %d, EXIT_FAILURE = %d\n", EXIT_SUCCESS, EXIT_FAILURE);        // <stdlib.h>
    printf("EOF = %d, RAND_MAX = %d\n", EOF, RAND_MAX);                                  // <stdio.h>, <stdlib.h>
    printf("fichier = %s, ligne = %d, fonction = %s\n", __FILE__, __LINE__, __func__);
    return 0;
}
```

---

# 6. Opérateurs et expressions

## 6.1 Catégories

| Catégorie | Opérateurs |
| --- | --- |
| **Arithmétiques** | `+` `-` `*` `/` `%` `++` `--` |
| **Relationnels** | `==` `!=` `<` `>` `<=` `>=` |
| **Logiques** | `&&` `\|\|` `!` |
| **Bit à bit** | `&` `\|` `^` `~` `<<` `>>` |
| **Affectation** | `=` `+=` `-=` `*=` `/=` `%=` `&=` `\|=` `^=` `<<=` `>>=` |
| **Ternaire** | `condition ? a : b` |
| **Adresse / pointeur** | `&` `*` `->` `.` `[]` |
| **Autres** | `sizeof` `,` `(type)` `()` |

```c
#include <stdio.h>

int main(void) {
    int a = 7, b = 2;
    printf("a / b = %d\n", a / b);              // 3 (division entière)
    printf("a %% b = %d\n", a % b);             // 1 (reste ; uniquement pour les entiers)
    printf("(double)a / b = %.1f\n", (double)a / b);   // 3.5
    return 0;
}
```

## 6.2 Incrémentation : préfixe et suffixe

```c
#include <stdio.h>

int main(void) {
    int i = 5;
    int a = i++;    // a = 5, puis i = 6  (post-incrément)
    int b = ++i;    // i = 7, puis b = 7  (pré-incrément)
    printf("a = %d, b = %d, i = %d\n", a, b, i);
    return 0;
}
```

## 6.3 Opérateurs logiques et évaluation paresseuse

```c
#include <stdio.h>

struct Noeud { int valeur; };

int main(void) {
    struct Noeud n = { 5 };
    struct Noeud *p = &n;
    struct Noeud *vide = NULL;

    if (p != NULL && p->valeur > 0) {      // p->valeur évalué seulement si p != NULL
        printf("p->valeur = %d (positif)\n", p->valeur);
    }
    if (vide != NULL && vide->valeur > 0) {    // court-circuit : pas de déréférencement de NULL
        printf("jamais affiché\n");
    } else {
        fprintf(stderr, "vide vaut NULL : la seconde condition n'a pas été évaluée\n");
    }
    printf("(3 > 2) = %d, (2 > 3) = %d\n", 3 > 2, 2 > 3);   // 1 (vrai) ou 0 (faux)
    return 0;
}
```

`&&` et `||` s'arrêtent dès que le résultat est connu (*court-circuit*). Le résultat d'une comparaison est `1` (vrai) ou `0` (faux).

## 6.4 Ternaire

```c
#include <stdio.h>

int main(void) {
    int a = 7, b = 2;
    int max = (a > b) ? a : b;
    printf("max = %d\n", max);
    return 0;
}
```

## 6.5 `sizeof` et opérateur virgule

```c
#include <stdio.h>

int main(void) {
    int a = 0;
    int tableau[10];
    size_t n = sizeof(int);                           // taille d'un type
    size_t t = sizeof tableau / sizeof tableau[0];    // nombre d'éléments d'un tableau (pas d'un pointeur !)
    int x = (a = 1, a + 2);                           // virgule : évalue de gauche à droite, résultat = dernier
    printf("n = %zu, t = %zu, x = %d\n", n, t, x);
    return 0;
}
```

## 6.6 Priorité et associativité

De la plus haute à la plus basse :

| Niveau | Opérateurs | Associativité |
| --- | --- | --- |
| 1 | `()` `[]` `->` `.` `x++` `x--` | Gauche → droite |
| 2 | `++x` `--x` `+x` `-x` `!` `~` `(type)` `*` `&` `sizeof` | Droite → gauche |
| 3 | `*` `/` `%` | G → D |
| 4 | `+` `-` | G → D |
| 5 | `<<` `>>` | G → D |
| 6 | `<` `<=` `>` `>=` | G → D |
| 7 | `==` `!=` | G → D |
| 8 | `&` puis `^` puis `\|` | G → D |
| 9 | `&&` puis `\|\|` | G → D |
| 10 | `?:` | D → G |
| 11 | `=` `+=` `-=`… | D → G |
| 12 | `,` | G → D |

> **Attention** : Piège : `x & 1 == 0` s'évalue comme `x & (1 == 0)`. **Ajoutez des parenthèses** : `(x & 1) == 0`.

## 6.7 Comportements à éviter

```c
#include <limits.h>
#include <stdbool.h>
#include <stdio.h>

// Chaque fonction détecte le cas indéfini et affiche l'erreur au lieu de l'exécuter.
static bool somme_sure(int a, int b, int *resultat) {
    if ((b > 0 && a > INT_MAX - b) || (b < 0 && a < INT_MIN - b)) {
        fprintf(stderr, "Erreur : %d + %d déborde (entier signé : indéfini)\n", a, b);
        return false;
    }
    *resultat = a + b;
    return true;
}

static bool decalage_sur(int x, int n, int *resultat) {
    if (n < 0 || n >= (int)(sizeof(int) * CHAR_BIT)) {
        fprintf(stderr, "Erreur : décalage de %d bits sur un int de %zu bits (indéfini)\n", n, sizeof(int) * CHAR_BIT);
        return false;
    }
    *resultat = x << n;
    return true;
}

static bool division_sure(int a, int b, int *resultat) {
    if (b == 0) {
        fprintf(stderr, "Erreur : division de %d par zéro (indéfini)\n", a);
        return false;
    }
    *resultat = a / b;
    return true;
}

int main(void) {
    int tab[3] = {0, 0, 0};
    int i = 0;
    // tab[i] = i++;   // Erreur : modification et lecture non séquencées (indéfini)
    tab[i] = i;        // correct : deux instructions distinctes
    i++;
    printf("tab[0] = %d, i = %d\n", tab[0], i);

    int r;
    if (somme_sure(INT_MAX, 1, &r))   printf("somme = %d\n", r);     // erreur affichée
    if (decalage_sur(1, 40, &r))      printf("décalage = %d\n", r);  // erreur affichée
    if (division_sure(10, 0, &r))     printf("quotient = %d\n", r);  // erreur affichée
    if (somme_sure(2, 3, &r))         printf("somme = %d\n", r);     // cas valide : 5
    return 0;
}
```

## 6.8 Arithmétique vérifiée *(C23)*

`<stdckdint.h>` détecte les débordements sans comportement indéfini :

```c
// Compiler avec : gcc -std=c23 ckd.c -o ckd   (en-tête <stdckdint.h> fourni par GCC 14+)
#include <limits.h>
#include <stdckdint.h>
#include <stdio.h>

int main(void) {
    int a = INT_MAX, b = 1;
    int resultat;
    if (ckd_add(&resultat, a, b)) {
        fprintf(stderr, "Débordement !\n");
    } else {
        printf("a + b = %d\n", resultat);
    }
    if (!ckd_add(&resultat, 2, 3)) {
        printf("2 + 3 = %d\n", resultat);
    }
    // aussi : ckd_sub, ckd_mul
    if (ckd_mul(&resultat, 100000, 100000)) {
        fprintf(stderr, "Débordement à la multiplication !\n");
    }
    return 0;
}
```

---

# 7. Entrées et sorties

## 7.1 Affichage : `printf` et `puts`

```c
#include <stdio.h>

int main(void) {
    const char *nom = "Alice";
    int age = 30;
    double taille = 1.68;
    printf("Bonjour\n");
    printf("Nom : %s, âge : %d, taille : %.2f m\n", nom, age, taille);
    puts("Texte avec saut de ligne automatique");
    putchar('A');
    putchar('\n');
    return 0;
}
```

### Spécificateurs de format

| Format | Type affiché |
| --- | --- |
| `%d` / `%i` | `int` |
| `%u` | `unsigned int` |
| `%ld` / `%lld` | `long` / `long long` |
| `%zu` | `size_t` |
| `%f` | `double` (`%.2f` : 2 décimales) |
| `%e` / `%g` | Notation scientifique / la plus courte |
| `%c` | Caractère |
| `%s` | Chaîne |
| `%p` | Pointeur (adresse) |
| `%x` / `%X` / `%o` | Hexadécimal / octal |
| `%b` *(C23)* | Binaire |
| `%%` | Le caractère `%` |

### Largeur, alignement, remplissage

```c
#include <stdio.h>

int main(void) {
    printf("[%5d]\n", 42);      // [   42]
    printf("[%-5d]\n", 42);     // [42   ]
    printf("[%05d]\n", 42);     // [00042]
    printf("[%8.3f]\n", 3.14159);   // [   3.142]
    printf("[%.*s]\n", 3, "Bonjour");   // [Bon]
    return 0;
}
```

> **Attention** : Le format **doit correspondre** au type de l'argument : `printf("%d", 3.5)` est un comportement indéfini. **Ne passez jamais une chaîne non maîtrisée comme format** (`printf(saisie)` → utiliser `printf("%s", saisie)`).

## 7.2 Lecture : `scanf`

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int age;
    double taille;
    char initiale;
    char mot[50];

    printf("Âge, taille, initiale, mot : ");
    if (scanf("%d", &age) != 1 ||            // & obligatoire pour les nombres
        scanf("%lf", &taille) != 1 ||        // %lf pour double (≠ printf)
        scanf(" %c", &initiale) != 1 ||      // l'espace avant %c ignore les blancs/sauts de ligne
        scanf("%49s", mot) != 1) {           // largeur limitée (taille − 1) ; pas de & pour un tableau
        fprintf(stderr, "Erreur : entrée invalide\n");
        return EXIT_FAILURE;
    }
    printf("age=%d taille=%.2f initiale=%c mot=%s\n", age, taille, initiale, mot);
    return 0;
}
```

- `scanf` **renvoie le nombre de valeurs lues** : vérifiez-le.
- `%s` s'arrête au premier espace.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int age;
    printf("Âge : ");
    if (scanf("%d", &age) != 1) {
        fprintf(stderr, "Entrée invalide\n");
        return EXIT_FAILURE;
    }
    printf("Vous avez %d ans\n", age);
    return 0;
}
```

## 7.3 Lire une ligne : `fgets` *(à jour)*

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char nom[50];
    printf("Nom : ");
    if (fgets(nom, sizeof nom, stdin) != NULL) {
        nom[strcspn(nom, "\n")] = '\0';        // supprime le '\n' final (nécessite <string.h>)
        printf("Bonjour, %s !\n", nom);
    } else {
        fprintf(stderr, "Erreur : aucune ligne lue\n");
        return 1;
    }
    return 0;
}
```

> **`gets()` est dangereuse et a été SUPPRIMÉE du langage (C11)** : elle ne limite pas la taille lue (dépassement de tampon). N'utilisez **jamais** `gets` ; employez `fgets` (ou `getline` sous POSIX).

### Lecture sûre d'un nombre

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char ligne[64];
    printf("Nombre : ");
    if (fgets(ligne, sizeof ligne, stdin)) {
        char *fin;
        long n = strtol(ligne, &fin, 10);      // plus fiable que atoi
        if (fin == ligne) {
            fprintf(stderr, "Pas un nombre\n");
            return 1;
        }
        printf("Nombre lu : %ld\n", n);
    }
    return 0;
}
```

### Vider le tampon d'entrée

Après `scanf`, il reste souvent un `\n` qui perturbe un `fgets`/`getchar` suivant :

```c
#include <stdio.h>

int main(void) {
    int age;
    char nom[50];

    printf("Âge puis nom : ");
    if (scanf("%d", &age) != 1) {
        fprintf(stderr, "Erreur : âge invalide\n");
        return 1;
    }

    int c;
    while ((c = getchar()) != '\n' && c != EOF) { }   // vide le tampon : retire le '\n' laissé par scanf

    if (fgets(nom, sizeof nom, stdin) != NULL) {
        printf("age = %d, ligne lue = %s", age, nom);
    } else {
        fprintf(stderr, "Erreur : aucune ligne lue\n");
    }
    return 0;
}
```

> **Attention** : N'utilisez pas `fflush(stdin)` : comportement indéfini en C standard.

## 7.4 Autres fonctions d'E/S

| Fonction | Rôle |
| --- | --- |
| `getchar()` / `putchar()` | Lire / écrire **un caractère** (`getchar` renvoie un `int` pour pouvoir signaler `EOF`) |
| `puts(s)` / `fputs(s, f)` | Écrire une chaîne |
| `sprintf` / **`snprintf`** | Écrire dans une chaîne (préférez `snprintf` qui limite la taille) |
| `sscanf(chaine, …)` | Lire depuis une chaîne |
| `fprintf(stderr, …)` | Écrire sur la **sortie d'erreur** |
| `perror(msg)` | Affiche un message d'erreur système |

```c
#include <stdio.h>

int main(void) {
    char tampon[32];
    snprintf(tampon, sizeof tampon, "Score : %d", 42);
    printf("%s\n", tampon);
    fprintf(stderr, "Erreur : %s\n", "fichier introuvable");
    return 0;
}
```

## 7.5 Flux standard

| Flux | Rôle | Redirection |
| --- | --- | --- |
| `stdin` | Entrée standard (clavier) | `< fichier` |
| `stdout` | Sortie standard (écran), **tamponnée** | `> fichier` |
| `stderr` | Erreurs, **non tamponnée** | `2> fichier` |

`fflush(stdout)` force l'écriture immédiate du tampon (utile avant une saisie sans `\n`).

## 7.6 Erreurs courantes

| Erreur | Solution |
| --- | --- |
| Oubli du `&` dans `scanf` | `scanf("%d", &x)` |
| `%f` au lieu de `%lf` avec `scanf` pour un `double` | `%lf` |
| `scanf("%s")` sans limite | `scanf("%49s")` ou `fgets` |
| Utiliser `gets` | `fgets` |
| Mélanger `scanf` et `fgets` sans vider le tampon | Vider le tampon, ou n'utiliser que `fgets` |
| Ne pas vérifier la valeur de retour de `scanf` | `if (scanf(...) != 1)` |

---

# 8. Structures de contrôle

## 8.1 Conditions : `if`, `else if`, `else`

```c
#include <stdio.h>

int main(void) {
    int notes[] = { 17, 12, 6 };
    for (int i = 0; i < 3; i++) {
        int note = notes[i];
        printf("%2d : ", note);
        if (note >= 16) {
            puts("Très bien");
        } else if (note >= 10) {
            puts("Passable");
        } else {
            puts("Insuffisant");
        }
    }
    return 0;
}
```

> **Bonne pratique** : Utilisez toujours des **accolades**, même pour une seule instruction (évite des bugs classiques).

## 8.2 `switch`

Choix selon une valeur **entière ou caractère** (pas de chaînes ni de flottants) :

```c
#include <stdio.h>

int main(void) {
    for (int jour = 1; jour <= 8; jour += 1) {
        printf("jour %d : ", jour);
        switch (jour) {
            case 1:
                puts("Lundi");
                break;                // sans break : exécution en cascade (« fall-through »)
            case 6:
            case 7:
                puts("Week-end");
                break;
            default:
                puts("Autre");
        }
    }
    return 0;
}
```

En C23, on marque une cascade volontaire avec `[[fallthrough]];`.

## 8.3 Boucles

```c
#include <stdio.h>

int main(void) {
    for (int i = 0; i < 5; i++) {        // nombre d'itérations connu
        printf("%d ", i);
    }
    printf("\n");

    int n = 0;
    while (n < 5) {                       // condition testée AVANT
        n++;
    }
    printf("après while : n = %d\n", n);

    do {                                  // exécutée AU MOINS une fois
        n--;
    } while (n > 0);
    printf("après do...while : n = %d\n", n);
    return 0;
}
```

| Boucle | Quand l'utiliser |
| --- | --- |
| `for` | Compteur / nombre d'itérations connu |
| `while` | Tant qu'une condition est vraie |
| `do…while` | Au moins une exécution (ex. menu, validation de saisie) |

### Boucle infinie

```c
#include <stdio.h>

int main(void) {
    int tours = 0;
    for (;;) {                  // boucle infinie, avec break pour sortir
        if (++tours == 3) break;
    }
    printf("for(;;) : sortie après %d tours\n", tours);

    tours = 0;
    while (1) {
        if (++tours == 5) break;
    }
    printf("while(1) : sortie après %d tours\n", tours);
    return 0;
}
```

## 8.4 `break`, `continue`, `goto`

```c
#include <stdio.h>

int main(void) {
    for (int i = 0; i < 10; i++) {
        if (i == 3) continue;     // passe à l'itération suivante
        if (i == 7) break;        // quitte la boucle
        printf("%d ", i);
    }
    printf("\n");                 // affiche : 0 1 2 4 5 6
    return 0;
}
```

`goto` saute vers une étiquette. À **éviter**, sauf pour un usage classique et légitime : **le nettoyage centralisé en cas d'erreur** :

```c
#include <stdio.h>
#include <stdlib.h>

int traiter(const char *chemin) {
    int code = -1;
    FILE *f = fopen(chemin, "r");
    if (!f) {
        fprintf(stderr, "Erreur : impossible d'ouvrir %s\n", chemin);
        goto fin;
    }
    char *tampon = malloc(100);
    if (!tampon) {
        fprintf(stderr, "Erreur : allocation impossible\n");
        goto ferme;
    }
    if (fgets(tampon, 100, f)) printf("Première ligne : %s", tampon);   // travail
    code = 0;
    free(tampon);
ferme:
    fclose(f);
fin:
    return code;
}

int main(void) {
    FILE *f = fopen("a.txt", "w");          // prépare un fichier à lire
    if (f) { fputs("Bonjour\n", f); fclose(f); }

    printf("traiter(a.txt) = %d\n", traiter("a.txt"));
    printf("traiter(inexistant.txt) = %d\n", traiter("inexistant.txt"));
    return 0;
}
```

## 8.5 Boucles imbriquées

```c
#include <stdio.h>

int main(void) {
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= i; j++) putchar('*');
        putchar('\n');
    }
    return 0;
}
```

## 8.6 Pièges classiques

```c
#include <stdio.h>

int main(void) {
    int x = 3;
    if (x = 5) {                         // Erreur : affectation (toujours vrai) : écrire x == 5
        fprintf(stderr, "Erreur : (x = 5) est une affectation, x vaut maintenant %d\n", x);
    }

    int corps = 0;
    for (int i = 0; i < 10; i++);        // Erreur : ; vide après le for
    { corps++; }                         // ce bloc ne fait plus partie de la boucle
    if (corps == 1) {
        fprintf(stderr, "Erreur : le bloc n'a été exécuté qu'une fois, pas 10 fois\n");
    }

    int i = 0, garde = 0;
    while (i < 10) {                     // Erreur : i jamais modifié : boucle infinie
        if (++garde == 5) {
            fprintf(stderr, "Erreur : i n'est jamais modifié, boucle infinie (arrêtée après %d tours)\n", garde);
            break;
        }
    }
    return 0;
}
```

---

# 9. Fonctions

## 9.1 Définir et appeler

```c
#include <stdio.h>

// Prototype (déclaration) : type de retour, nom, types des paramètres
int additionner(int a, int b);

int main(void) {
    int s = additionner(3, 4);
    printf("Somme : %d\n", s);
    return 0;
}

// Définition
int additionner(int a, int b) {
    return a + b;
}
```

| Élément | Rôle |
| --- | --- |
| **Type de retour** | `int`, `double`, `void` (rien), pointeur, structure… |
| **Paramètres** | Variables locales initialisées avec les valeurs de l'appel |
| **Prototype** | Permet d'appeler une fonction **avant** sa définition ; à placer dans un **fichier d'en-tête `.h`** |
| **`return`** | Termine la fonction et renvoie une valeur |

```c
#include <stdio.h>

void afficher(void) { puts("Salut"); }          // aucun paramètre, aucun retour
static inline int carre(int x) { return x * x; }   // fonction locale au fichier, candidate à l'inlining

int main(void) {
    afficher();
    printf("carre(7) = %d\n", carre(7));
    return 0;
}
```

> **Attention** : Écrivez `f(void)` pour « aucun paramètre » (avant C23, `f()` signifie « paramètres non spécifiés »).

## 9.2 Passage des arguments : toujours **par valeur**

C copie les arguments : la fonction travaille sur des **copies**.

```c
#include <stdio.h>

void echanger_rate(int a, int b) { int t = a; a = b; b = t; }   // Erreur : ne modifie pas l'appelant

void echanger(int *a, int *b) {                                  // OK : on passe des ADRESSES
    int t = *a; *a = *b; *b = t;
}

int main(void) {
    int x = 1, y = 2;
    echanger_rate(x, y);
    fprintf(stderr, "Erreur : après echanger_rate, x = %d et y = %d (inchangés)\n", x, y);
    echanger(&x, &y);       // x = 2, y = 1
    printf("Après echanger : x = %d, y = %d\n", x, y);
    return 0;
}
```

- Passer un **pointeur** permet à la fonction de **modifier** la valeur d'origine ou de renvoyer plusieurs résultats.
- Les **tableaux** sont passés comme un **pointeur vers leur premier élément** : joignez toujours leur taille.

```c
#include <stdio.h>

double moyenne(const int tab[], size_t n) {     // const : la fonction ne modifie pas le tableau
    double s = 0;
    for (size_t i = 0; i < n; i++) s += tab[i];
    return n ? s / n : 0;
}

int main(void) {
    int notes[] = { 12, 15, 9, 18 };
    printf("moyenne = %.2f\n", moyenne(notes, sizeof notes / sizeof notes[0]));
    printf("moyenne d'un tableau vide = %.2f\n", moyenne(notes, 0));
    return 0;
}
```

## 9.3 Plusieurs fichiers : en-têtes et sources

```c
// maths.h
#ifndef MATHS_H
#define MATHS_H
int additionner(int a, int b);
#endif
```

```c
// maths.c
#include "maths.h"
int additionner(int a, int b) { return a + b; }
```

```c
// main.c
#include <stdio.h>
#include "maths.h"
int main(void) { printf("%d\n", additionner(2, 3)); return 0; }
```

```bash
gcc main.c maths.c -o programme
```

## 9.4 Fonctions variadiques

Nombre variable d'arguments (comme `printf`) :

```c
#include <stdarg.h>
#include <stdio.h>

int somme(int n, ...) {
    va_list args;
    va_start(args, n);
    int total = 0;
    for (int i = 0; i < n; i++) total += va_arg(args, int);
    va_end(args);
    return total;
}

int main(void) {
    printf("somme(3, 10, 20, 30) = %d\n", somme(3, 10, 20, 30));    // 60
    return 0;
}
```

**Attention** : Aucun contrôle de type : une erreur sur les arguments est un comportement indéfini.

## 9.5 Fonctions et mémoire : points d'attention

- Ne retournez **jamais** l'adresse d'une **variable locale** (détruite à la sortie) : voir [section 15](#15-retourner-des-tableaux-et-des-chaînes).
- Les structures peuvent être passées et retournées par valeur (copie) ; pour de grosses structures, passez un **pointeur `const`**.
- `static` devant une fonction la rend **privée au fichier**.
- La récursivité est possible : voir [section 26](#26-récursivité).

## 9.6 Bonnes pratiques

- Une fonction = **une tâche**, nom explicite (verbe).
- Prototypes dans des `.h`, **gardes d'inclusion** (`#ifndef`/`#pragma once`).
- Utilisez `const` pour les paramètres en lecture seule.
- Vérifiez les **valeurs de retour** (erreurs) des fonctions de bibliothèque.
- Marquez `[[nodiscard]]` (C23) les fonctions dont le résultat ne doit pas être ignoré.

---

# 10. Portée et durée de vie des variables

## 10.1 Les portées

| Portée | Où | Visible |
| --- | --- | --- |
| **Bloc** | Entre `{ }` | Dans le bloc (à partir de la déclaration) |
| **Fonction** | Étiquettes de `goto` | Dans la fonction |
| **Fichier** | Hors de toute fonction | Dans tout le fichier, après la déclaration |
| **Prototype** | Noms de paramètres d'un prototype | Dans le prototype |

```c
#include <stdio.h>

int global = 10;                  // portée fichier

void f(void) {
    int local = 5;                // portée bloc
    {
        int interne = 1;
        int global = 99;          // masque (ombre) la variable globale
        printf("bloc interne : interne = %d, global = %d\n", interne, global);
    }
    printf("fonction : local = %d, global = %d\n", local, global);
}

int main(void) {
    f();
    printf("main : global = %d\n", global);
    return 0;
}
```

## 10.2 Classes de stockage et durée de vie

| Classe | Durée de vie | Portée / liaison | Initialisation par défaut |
| --- | --- | --- | --- |
| **`auto`** (par défaut en bloc) | Jusqu'à la fin du bloc | Bloc | **Indéterminée** |
| **`static`** (dans une fonction) | **Tout le programme** | Bloc | 0 |
| **`static`** (au niveau fichier) | Tout le programme | **Fichier** (invisible aux autres fichiers) | 0 |
| **`extern`** | Tout le programme | Définie ailleurs | — |
| **`register`** | Bloc | Bloc | Indéterminée (conseil obsolète au compilateur) |
| **`thread_local`** *(C23 ; `_Thread_local` avant)* | Durée du fil d'exécution | | 0 |

```c
#include <stdio.h>

void compter(void) {
    static int appels = 0;      // initialisée UNE fois, conservée entre les appels
    appels++;
    printf("Appel n°%d\n", appels);
}

int main(void) {
    compter();
    compter();
    compter();
    return 0;
}
```

```c
// fichier a.c
#include <stdio.h>

int compteur = 0;               // définition (visible par les autres fichiers)
static int prive = 1;           // visible seulement dans a.c

void afficher_prive(void) { printf("prive = %d (visible seulement dans a.c)\n", prive); }
```

```c
// fichier b.c
#include <stdio.h>

extern int compteur;            // déclaration : « définie ailleurs »
void afficher_prive(void);

int main(void) {
    compteur++;
    printf("compteur = %d (défini dans a.c)\n", compteur);
    afficher_prive();
    return 0;
}
```

```bash
gcc a.c b.c -o programme && ./programme
```

## 10.3 Organisation de la mémoire d'un programme

| Zone | Contenu | Gestion |
| --- | --- | --- |
| **Code (text)** | Instructions du programme | — |
| **Données** | Variables globales / statiques initialisées | Durée = programme |
| **BSS** | Globales / statiques non initialisées (mises à 0) | Durée = programme |
| **Tas (heap)** | Mémoire allouée par `malloc` | **Manuelle** (`free`) |
| **Pile (stack)** | Variables locales, paramètres, adresses de retour | **Automatique** |

```text
Adresses hautes  ┌───────────────┐
                 │     Pile      │  ↓ (variables locales)
                 │       ⋮       │
                 │      Tas      │  ↑ (malloc)
                 ├───────────────┤
                 │  BSS / Données│
Adresses basses  │     Code      │
                 └───────────────┘
```

## 10.4 Bonnes pratiques

- **Limitez la portée** : déclarez les variables au plus près de leur usage.
- Évitez les **variables globales** (couplage, bugs difficiles) ; si nécessaire, rendez-les `static`.
- Ne retournez pas un pointeur vers une variable locale.
- Pour conserver un état entre appels, utilisez `static` (attention aux fils d'exécution : non réentrant).

---

# Niveau intermédiaire

---

# 11. Tableaux

## 11.1 Déclarer et initialiser

Un **tableau** stocke plusieurs éléments **de même type**, **contigus en mémoire**. Les indices commencent à **0**.

```c
// Compiler avec : gcc -std=c23 tableaux.c -o tableaux
#include <stdio.h>

static void afficher(const char *nom, const int *t, size_t n) {
    printf("%s = {", nom);
    for (size_t i = 0; i < n; i++) printf("%s%d", i ? ", " : "", t[i]);
    printf("}\n");
}

int main(void) {
    int notes[5];                           // 5 entiers non initialisés (locaux)
    for (int i = 0; i < 5; i++) notes[i] = i;   // on les remplit avant de les lire
    int a[5] = {10, 20, 30, 40, 50};        // initialisation complète
    int b[5] = {1, 2};                      // le reste est mis à 0 → {1, 2, 0, 0, 0}
    int c[] = {7, 8, 9};                    // taille déduite : 3
    int d[100] = {0};                       // tout à zéro
    int e[100] = {};                        // idem (C23)
    int f[6] = { [2] = 5, [5] = 9 };        // initialisation désignée (C99)

    afficher("notes", notes, 5);
    afficher("a", a, 5);
    afficher("b", b, 5);
    afficher("c", c, sizeof c / sizeof c[0]);
    printf("d[99] = %d, e[99] = %d\n", d[99], e[99]);
    afficher("f", f, 6);
    return 0;
}
```

```c
#include <stdio.h>

int main(void) {
    int a[5] = {10, 20, 30, 40, 50};
    a[0] = 11;
    printf("%d\n", a[2]);                       // 30
    size_t n = sizeof a / sizeof a[0];          // nombre d'éléments (5)
    printf("a[0] = %d, n = %zu\n", a[0], n);
    return 0;
}
```

> **C ne vérifie jamais les bornes.** `a[10]` sur un tableau de 5 éléments est un **comportement indéfini** (corruption mémoire, plantage, faille de sécurité).

## 11.2 Parcourir

```c
#include <stdio.h>

int main(void) {
    int a[5] = {10, 20, 30, 40, 50};
    size_t n = sizeof a / sizeof a[0];
    for (size_t i = 0; i < n; i++) {
        printf("a[%zu] = %d\n", i, a[i]);
    }
    return 0;
}
```

## 11.3 Tableaux multidimensionnels

```c
#include <stdio.h>

int main(void) {
    int matrice[2][3] = { {1, 2, 3}, {4, 5, 6} };

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) printf("%d ", matrice[i][j]);
        putchar('\n');
    }
    return 0;
}
```

Stockage **ligne par ligne** (*row-major*). Pour une fonction : `void afficher(int m[][3], int lignes)` (toutes les dimensions sauf la première doivent être précisées).

## 11.4 Tableaux à taille variable (VLA)

```c
#include <stdio.h>

static int lire_taille(void) { return 4; }   // ici une valeur fixe, connue seulement à l'exécution

int main(void) {
    int n = lire_taille();
    int t[n];                  // VLA : taille connue seulement à l'exécution (C99)
    for (int i = 0; i < n; i++) t[i] = i * i;
    for (int i = 0; i < n; i++) printf("t[%d] = %d\n", i, t[i]);
    printf("sizeof t = %zu octets\n", sizeof t);
    return 0;
}
```

> **Attention** : Les VLA sont **optionnels depuis C11**, allouent sur la **pile** (risque de dépassement) et sont **interdits par certains compilateurs / guides de sécurité**. Pour des tailles variables, préférez **`malloc`** (section 14).

## 11.5 Tableaux et fonctions

Un tableau « se dégrade » (*decay*) en **pointeur vers son premier élément** lorsqu'il est passé à une fonction : `sizeof` y donne la taille d'un **pointeur**, pas du tableau.

```c
#include <stdio.h>

void remplir(int *tab, size_t n) {    // équivalent à int tab[]
    for (size_t i = 0; i < n; i++) tab[i] = (int)i * 2;
    printf("dans la fonction : sizeof tab = %zu (taille d'un pointeur)\n", sizeof tab);
}

int main(void) {
    int resultats[10];
    remplir(resultats, 10);               // toujours passer la taille
    printf("dans main : sizeof resultats = %zu\n", sizeof resultats);
    for (int i = 0; i < 10; i++) printf("%d ", resultats[i]);
    putchar('\n');
    return 0;
}
```

## 11.6 Opérations courantes

```c
#include <stdio.h>
#include <string.h>

static void afficher(const char *nom, const int *t, size_t n) {
    printf("%s = {", nom);
    for (size_t i = 0; i < n; i++) printf("%s%d", i ? ", " : "", t[i]);
    printf("}\n");
}

int main(void) {
    int a[5] = {10, 20, 30, 40, 50};
    int copie[5];
    memcpy(copie, a, sizeof a);                  // copier (zones qui ne se chevauchent pas)
    afficher("copie", copie, 5);
    int egaux = memcmp(a, copie, sizeof a) == 0; // comparer
    printf("a et copie égaux : %d\n", egaux);
    memmove(a + 1, a, 4 * sizeof a[0]);          // copier avec chevauchement possible
    afficher("a", a, 5);
    printf("a et copie égaux : %d\n", memcmp(a, copie, sizeof a) == 0);
    memset(copie, 0, sizeof copie);              // remplir d'octets (0 pour les entiers)
    afficher("copie", copie, 5);
    return 0;
}
```

> **Attention** : On ne peut pas copier ou comparer deux tableaux avec `=` ou `==` : cela compare/affecte des **adresses**.

### Tri avec `qsort`

```c
#include <stdio.h>
#include <stdlib.h>

int comparer(const void *x, const void *y) {
    int a = *(const int *)x, b = *(const int *)y;
    return (a > b) - (a < b);          // évite le débordement de a - b
}

int main(void) {
    int a[] = {50, 10, 40, 20, 30};
    size_t n = sizeof a / sizeof a[0];
    qsort(a, n, sizeof a[0], comparer);
    for (size_t i = 0; i < n; i++) printf("%d ", a[i]);
    putchar('\n');
    return 0;
}
```

## 11.7 Erreurs courantes

| Erreur | Conséquence |
| --- | --- |
| Accès hors limites | Comportement indéfini |
| `sizeof` sur un paramètre tableau | Taille d'un pointeur |
| Oublier la taille en paramètre | Impossible de borner la boucle |
| Tableau local non initialisé | Valeurs aléatoires |
| Comparer des tableaux avec `==` | Compare les adresses |

---

# 12. Chaînes de caractères

## 12.1 Définition

En C, une **chaîne** est un **tableau de `char` terminé par le caractère nul `'\0'`**. Il n'y a pas de type « string ».

```c
#include <stdio.h>

int main(void) {
    char s1[] = "Bonjour";              // 8 octets : 7 caractères + '\0'
    char s2[20] = "Salut";              // taille 20, le reste est mis à 0
    char s3[] = {'H', 'i', '\0'};       // équivalent à "Hi"
    const char *s4 = "Littéral";        // pointeur vers une chaîne en LECTURE SEULE

    printf("%s (%zu octets)\n", s1, sizeof s1);
    printf("%s (%zu octets)\n", s2, sizeof s2);
    printf("%s (%zu octets)\n", s3, sizeof s3);
    printf("%s\n", s4);

    // s4[0] = 'l';   // comportement indéfini : plantage (Segmentation fault) à l'exécution
    fprintf(stderr, "Erreur : modifier un littéral de chaîne (s4[0] = 'l') est interdit\n");
    return 0;
}
```

> **Modifier un littéral de chaîne** (`s4[0] = 'l';`) est un comportement indéfini. Déclarez-les `const char *`.
> **Attention** : Oublier de réserver la place du `'\0'` est une erreur classique (**dépassement d'un octet**).

## 12.2 Fonctions de `<string.h>`

| Fonction | Rôle |
| --- | --- |
| `strlen(s)` | Longueur (sans le `'\0'`) |
| `strcpy(dst, src)` / `strncpy` | Copie (attention : voir ci-dessous) |
| `strcat(dst, src)` / `strncat` | Concaténation |
| `strcmp(a, b)` / `strncmp` | Comparaison : `0` si égales, `<0` / `>0` sinon |
| `strchr(s, c)` / `strrchr` | Première / dernière occurrence d'un caractère |
| `strstr(s, sous)` | Recherche d'une sous-chaîne |
| `strspn` / `strcspn` | Longueur du préfixe fait de / sans certains caractères |
| `strtok(s, delims)` | Découpe en jetons (attention : modifie la chaîne, non réentrant) |
| `strdup(s)` | Duplique avec `malloc` (**standard depuis C23**, POSIX avant) |
| `memcpy` / `memmove` / `memset` / `memcmp` | Opérations sur des octets |

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char nom[30] = "Alice";
    const char *a = "abc", *b = "abc";
    printf("strlen(nom) = %zu\n", strlen(nom));                // 5
    printf("strcmp(\"abc\", \"abd\") < 0 : %d\n", strcmp("abc", "abd") < 0);   // 1 (vrai)
    if (strcmp(a, b) == 0) {                  // jamais a == b (compare des adresses)
        puts("a et b sont égales");
    }
    return 0;
}
```

## 12.3 Copier et concaténer en sécurité

| Fonction | Problème |
| --- | --- |
| `strcpy`, `strcat` | **Aucune vérification de taille** → dépassement de tampon |
| `strncpy` | **Ne garantit pas le `'\0'`** final et remplit de zéros (lent) |
| `strncat` | Le paramètre est le nombre de caractères **à ajouter**, pas la taille du tampon |
| **`snprintf`** (recommandée) | Toujours terminé par `'\0'`, limité à la taille du tampon |

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char dest[16];
    snprintf(dest, sizeof dest, "%s-%d", "ID", 42);       // sûr
    printf("%s\n", dest);

    // Concaténation sûre
    size_t len = strlen(dest);
    snprintf(dest + len, sizeof dest - len, "%s", "_fin");
    printf("%s\n", dest);

    // Troncature détectée : la valeur de retour dépasse la taille du tampon
    int voulu = snprintf(dest, sizeof dest, "%s", "Une chaîne beaucoup trop longue");
    if (voulu >= (int)sizeof dest) {
        fprintf(stderr, "Erreur : texte tronqué (%d caractères voulus, %zu disponibles)\n", voulu, sizeof dest - 1);
    }
    printf("%s\n", dest);
    return 0;
}
```

> **Astuce** : Sur BSD/macOS : `strlcpy` / `strlcat` ; non standard en C (mais proposés dans certaines libc récentes). Les variantes `*_s` de l'**Annexe K** sont optionnelles et peu implémentées : ne comptez pas dessus.

## 12.4 Lire et parcourir

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    const char *s = "Salut";
    for (size_t i = 0; s[i] != '\0'; i++) printf("[%c]", s[i]);
    putchar('\n');
    for (const char *p = s; *p; p++) printf("(%c)", *p);
    putchar('\n');

    char saisie[50];
    printf("Saisie : ");
    if (fgets(saisie, sizeof saisie, stdin) != NULL) {
        saisie[strcspn(saisie, "\n")] = '\0';
        printf("Vous avez saisi : %s\n", saisie);
    } else {
        fprintf(stderr, "Erreur : aucune saisie\n");
    }
    return 0;
}
```

## 12.5 `<ctype.h>` : tester et convertir les caractères

```c
#include <ctype.h>
#include <stdio.h>

int main(void) {
    const char *texte = "Ab1 !";
    for (const char *p = texte; *p; p++) {
        int c = (unsigned char)*p;       // cast : évite un comportement indéfini avec un char signé
        printf("'%c' : alpha=%d digit=%d space=%d punct=%d upper=%d lower=%d -> maj '%c', min '%c'\n",
               c, !!isalpha(c), !!isdigit(c), !!isspace(c), !!ispunct(c), !!isupper(c), !!islower(c),
               toupper(c), tolower(c));
    }
    return 0;
}
```

> **Attention** : Avec un `char` signé, castez : `isalpha((unsigned char)c)`.

## 12.6 Conversions chaîne ⇄ nombre

```c
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char *fin;
    errno = 0;
    long n = strtol("123abc", &fin, 10);      // détecte les erreurs via fin et errno
    printf("n = %ld\n", n);
    if (*fin != '\0') {
        fprintf(stderr, "Erreur : caractères invalides après le nombre : \"%s\"\n", fin);
    }
    if (errno == ERANGE) {
        fprintf(stderr, "Erreur : valeur hors limites\n");
    }

    double d = strtod("3.14", NULL);
    printf("d = %.2f\n", d);
    int a = atoi("42");                       // pas de détection d'erreur : à éviter
    printf("a = %d (atoi(\"abc\") = %d, sans signaler l'erreur)\n", a, atoi("abc"));

    char tampon[32];
    snprintf(tampon, sizeof tampon, "%d", 123);   // nombre → chaîne
    printf("tampon = \"%s\"\n", tampon);
    return 0;
}
```

## 12.7 Tableau de chaînes

```c
#include <stdio.h>

int main(void) {
    const char *jours[] = { "Lundi", "Mardi", "Mercredi" };
    for (size_t i = 0; i < sizeof jours / sizeof jours[0]; i++) puts(jours[i]);

    char noms[3][20] = { "Alice", "Bob", "Chloé" };    // 3 chaînes modifiables de 19 caractères max
    noms[1][0] = 'R';                                  // modifiable : "Rob"
    for (int i = 0; i < 3; i++) puts(noms[i]);
    return 0;
}
```

## 12.8 Bonnes pratiques

- Réservez toujours **un octet de plus** pour `'\0'`.
- Utilisez `snprintf`, `fgets`, `strtol`.
- Comparez avec `strcmp`, jamais `==`.
- Déclarez les littéraux `const char *`.
- Pour le texte non ASCII (accents, emojis), voir [section 27](#27-unicode-et-caractères-larges).

---

# 13. Pointeurs

## 13.1 Qu'est-ce qu'un pointeur ?

Un **pointeur** est une variable qui contient l'**adresse mémoire** d'une autre variable.

```c
#include <stdio.h>

int main(void) {
    int x = 42;
    int *p = &x;          // p contient l'adresse de x

    printf("%d\n", x);    // 42
    printf("%p\n", (void *)p);   // adresse de x
    printf("%d\n", *p);   // 42 : déréférencement (valeur pointée)
    *p = 100;             // modifie x via le pointeur → x == 100
    printf("x = %d\n", x);
    return 0;
}
```

| Opérateur | Rôle |
| --- | --- |
| `&x` | **Adresse** de `x` |
| `*p` (dans une déclaration) | `p` est un **pointeur** (`int *p`) |
| `*p` (dans une expression) | **Valeur pointée** (déréférencement) |

```text
  x  : [ 42 ]   adresse 0x7ffd10
  p  : [0x7ffd10] ──▶ pointe vers x
```

## 13.2 Pointeur nul

```c
// Compiler avec : gcc -std=c23 pointeur_nul.c -o pointeur_nul
#include <stdio.h>

int main(void) {
    int *p = nullptr;      // avant C23 : int *p = NULL;
    if (p != NULL) {
        printf("sûr de déréférencer : %d\n", *p);
    } else {
        fprintf(stderr, "Erreur : p est nul, on ne le déréférence pas\n");
    }

    int x = 7;
    p = &x;
    if (p != NULL) {
        printf("sûr de déréférencer : %d\n", *p);
    }
    return 0;
}
```

Déréférencer `NULL` est un comportement indéfini (généralement un plantage). **Initialisez toujours un pointeur** (adresse valide ou `NULL`).

## 13.3 Arithmétique des pointeurs

Ajouter `n` à un pointeur le déplace de **`n` éléments** (pas `n` octets).

```c
#include <stddef.h>
#include <stdio.h>

int main(void) {
    int t[] = {10, 20, 30, 40};
    int *p = t;                  // t se dégrade en &t[0]
    printf("*(p + 2) = %d, t[2] = %d\n", *(p + 2), t[2]);   // 30, équivalent à t[2]
    p++;                         // pointe sur t[1]
    printf("*p = %d\n", *p);
    ptrdiff_t ecart = &t[3] - &t[1];   // 2 (nombre d'éléments)
    printf("ecart = %td\n", ecart);
    return 0;
}
```

Équivalence : **`t[i]` ≡ `*(t + i)`**.

> **Attention** : Rester dans les bornes du tableau (ou **un élément après la fin**, sans le déréférencer).

## 13.4 Tableaux ≠ pointeurs

```c
#include <stdio.h>

int main(void) {
    int t[5];
    int *p = t;
    printf("sizeof t = %zu\n", sizeof t);      // 20 (5 × 4 octets)
    printf("sizeof p = %zu\n", sizeof p);      // 8 (taille d'un pointeur)
    // t = p;   // error: assignment to expression with array type
    fprintf(stderr, "Erreur de compilation si on décommente t = p : un tableau n'est pas une valeur modifiable\n");
    return 0;
}
```

## 13.5 Pointeurs et fonctions

```c
#include <stdio.h>

void incrementer(int *n) { (*n)++; }       // parenthèses : (*n)++ ≠ *n++

int main(void) {
    int x = 0;
    incrementer(&x);                        // x == 1
    printf("x = %d\n", x);
    return 0;
}
```

Les pointeurs servent à : **modifier** les arguments, **renvoyer plusieurs valeurs**, **éviter de copier** de gros objets, manipuler des **tableaux** et de la **mémoire dynamique**.

## 13.6 `const` et pointeurs (rappel)

```c
#include <stdio.h>

void afficher(const char *texte) {         // « je ne modifie pas texte »
    printf("%s\n", texte);
}

int main(void) {
    int x = 5, y = 6;
    const int *a = &x;          // données non modifiables via a
    int *const b = &x;          // adresse non modifiable
    a = &y;                     // autorisé : a peut pointer ailleurs
    *b = 50;                    // autorisé : on modifie la valeur pointée
    // *a = 1;   // error: assignment of read-only location '*a'
    // b = &y;   // error: assignment of read-only variable 'b'
    fprintf(stderr, "Erreur de compilation si on décommente *a = 1 ou b = &y\n");
    printf("*a = %d, *b = %d\n", *a, *b);
    afficher("texte non modifié");
    return 0;
}
```

## 13.7 `void *` : pointeur générique

```c
#include <stdio.h>

int main(void) {
    int x = 42;
    void *q = &x;                 // peut contenir n'importe quelle adresse d'objet
    int *r = q;                   // conversion implicite en C (pas besoin de cast)
    printf("*r = %d\n", *r);
    // *q;                        // error: dereferencing 'void *' pointer
    fprintf(stderr, "Erreur : impossible de déréférencer un void * (conversion en int * nécessaire)\n");
    return 0;
}
```

Utilisé par `malloc`, `qsort`, `memcpy`…

## 13.8 Pointeur vers une structure

```c
#include <stdio.h>

struct Point { int x, y; };

int main(void) {
    struct Point pt = {1, 2};
    struct Point *pp = &pt;
    pp->x = 10;                   // identique à (*pp).x = 10
    printf("pt = (%d, %d)\n", pt.x, pt.y);
    (*pp).y = 20;
    printf("pt = (%d, %d)\n", pt.x, pt.y);
    return 0;
}
```

## 13.9 `restrict` *(ajout, C99)*

Promesse au compilateur que, pendant la durée de vie du pointeur, **aucun autre pointeur n'accède** à la même zone : permet des optimisations (ex. `memcpy`).

```c
#include <stdio.h>

// restrict : dst et src ne se chevauchent pas, le compilateur peut optimiser
void ajouter(int *restrict dst, const int *restrict src, size_t n) {
    for (size_t i = 0; i < n; i++) dst[i] += src[i];
}

int main(void) {
    int a[3] = {1, 2, 3};
    int b[3] = {10, 20, 30};
    ajouter(a, b, 3);
    for (int i = 0; i < 3; i++) printf("%d ", a[i]);
    putchar('\n');
    return 0;
}
```

## 13.10 Erreurs classiques

| Erreur | Description |
| --- | --- |
| **Pointeur non initialisé** (« sauvage ») | Pointe vers une adresse quelconque |
| **Pointeur nul déréférencé** | Plantage |
| **Pointeur pendant** (*dangling*) | Vers une variable locale détruite ou une mémoire libérée |
| **Dépassement de tableau** | Arithmétique hors bornes |
| **Mauvais type** | `int *` utilisé pour lire un `double` |
| **Violation d'alias strict** | Accéder à un objet via un pointeur de type incompatible (hors `char *`) |

```c
#include <stdio.h>

int *mauvaise(void) {
    int local = 5;
    return &local;       // Erreur : adresse d'une variable détruite à la sortie
}

int main(void) {
    int *p = mauvaise();   // gcc : warning: function returns address of local variable
    (void)p;               // p est un pointeur pendant : on ne le déréférence pas
    fprintf(stderr, "Erreur : mauvaise() retourne l'adresse d'une variable locale détruite\n");
    return 0;
}
```

---

# 14. Allocation dynamique de mémoire

## 14.1 Pourquoi ?

Les tableaux ordinaires ont une **taille fixée à la compilation** et vivent sur la **pile** (limitée, quelques Mo). L'**allocation dynamique** réserve de la mémoire dans le **tas** à l'**exécution**, avec une durée de vie **maîtrisée par le programmeur**.

## 14.2 Les fonctions de `<stdlib.h>`

| Fonction | Rôle |
| --- | --- |
| `void *malloc(size_t taille)` | Réserve `taille` octets (**non initialisés**) |
| `void *calloc(size_t n, size_t taille)` | Réserve `n × taille` octets **initialisés à 0** (vérifie le débordement de la multiplication) |
| `void *realloc(void *p, size_t taille)` | Redimensionne un bloc |
| `void free(void *p)` | Libère un bloc (`free(NULL)` est sans effet) |
| `void *aligned_alloc(size_t align, size_t taille)` | Alloue avec un alignement précis (C11) |

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    size_t n = 5;
    int *tab = malloc(n * sizeof *tab);       // sizeof *tab : s'adapte au type
    if (tab == NULL) {                        // toujours vérifier
        perror("malloc");
        return EXIT_FAILURE;
    }
    for (size_t i = 0; i < n; i++) tab[i] = (int)(i * i);
    for (size_t i = 0; i < n; i++) printf("tab[%zu] = %d\n", i, tab[i]);

    free(tab);                                // libérer
    tab = NULL;                               // évite l'usage d'un pointeur pendant
    return 0;
}
```

> **Bonne pratique** : En C, **ne castez pas** le résultat de `malloc` (`void *` se convertit implicitement).
> **Bonne pratique** : Préférez `malloc(n * sizeof *p)` à `malloc(n * sizeof(int))`.

## 14.3 `calloc`

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *zeros = calloc(100, sizeof *zeros);     // 100 entiers à 0
    if (zeros == NULL) {
        perror("calloc");
        return EXIT_FAILURE;
    }
    printf("zeros[0] = %d, zeros[99] = %d\n", zeros[0], zeros[99]);
    free(zeros);
    return 0;
}
```

## 14.4 `realloc` : la bonne façon

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *tab = malloc(5 * sizeof *tab);
    if (tab == NULL) return EXIT_FAILURE;
    for (int i = 0; i < 5; i++) tab[i] = i;

    int *nouveau = realloc(tab, 10 * sizeof *tab);
    if (nouveau == NULL) {          // échec : l'ancien bloc est toujours valide !
        fprintf(stderr, "Erreur : realloc a échoué\n");
        free(tab);
        return EXIT_FAILURE;
    }
    tab = nouveau;
    for (int i = 5; i < 10; i++) tab[i] = i;
    for (int i = 0; i < 10; i++) printf("%d ", tab[i]);
    putchar('\n');
    free(tab);
    return 0;
}
```

> **Ne faites jamais `tab = realloc(tab, …)`** directement : en cas d'échec, vous perdez le pointeur d'origine (fuite). Après un `realloc` réussi, l'**ancienne adresse est invalide** (le bloc a pu être déplacé).

## 14.5 Erreurs classiques de gestion mémoire

| Erreur | Description | Conséquence |
| --- | --- | --- |
| **Fuite mémoire** (*leak*) | `malloc` sans `free` | Consommation croissante |
| **Double libération** (*double free*) | `free` deux fois sur le même bloc | Corruption du tas |
| **Utilisation après libération** (*use-after-free*) | Accès après `free` | Comportement indéfini, faille |
| **Dépassement de tampon du tas** | Écrire hors du bloc | Corruption |
| **Libérer un pointeur non alloué** | `free` d'une variable locale | Plantage |
| **Débordement de la taille** | `n * taille` dépasse `size_t` | Bloc trop petit (utiliser `calloc`) |
| **Non-vérification de `NULL`** | Échec d'allocation ignoré | Plantage |

## 14.6 Règle de propriété

> Pour chaque `malloc`, il doit y avoir **exactement un `free`**, exécuté par le **propriétaire** du bloc. Documentez qui possède la mémoire (l'appelant ou la fonction).

Motif recommandé : **allouer et libérer au même niveau**, ou fournir des fonctions `creer_xxx()` / `detruire_xxx()`.

## 14.7 Outils de détection

```bash
gcc -g -fsanitize=address,undefined prog.c -o prog && ./prog     # AddressSanitizer
valgrind --leak-check=full ./prog                                # Valgrind (Linux)
```

---

# 15. Retourner des tableaux et des chaînes

## 15.1 Le problème

Une fonction C **ne peut pas retourner un tableau** par valeur. Il faut passer par un **pointeur**, et se poser la question : *qui possède la mémoire ?*

## 15.2 Les quatre solutions

| Solution | Avantages | Inconvénients |
| --- | --- | --- |
| **L'appelant fournit le tampon** (recommandé) | Simple, aucune fuite, pas de `malloc` | L'appelant doit prévoir la taille |
| **Allocation dynamique** (`malloc`) | Taille variable, durée de vie libre | L'appelant doit `free` |
| **Variable `static`** | Survit à l'appel | **Non réentrant**, partagée (écrasée à chaque appel) |
| **Encapsuler dans une `struct`** | Retour par valeur | Taille fixe |

### 1. L'appelant fournit le tampon (recommandé)

```c
#include <ctype.h>
#include <stdio.h>

void majuscules(const char *src, char *dst, size_t taille) {
    size_t i = 0;
    for (; src[i] && i + 1 < taille; i++) dst[i] = (char)toupper((unsigned char)src[i]);
    dst[i] = '\0';
}

int main(void) {
    char resultat[64];
    majuscules("bonjour", resultat, sizeof resultat);
    printf("%s\n", resultat);

    char petit[4];
    majuscules("bonjour", petit, sizeof petit);     // tronqué proprement, sans dépassement
    printf("%s\n", petit);
    return 0;
}
```

### 2. Allocation dynamique

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *dupliquer(const char *s) {
    size_t n = strlen(s) + 1;
    char *copie = malloc(n);
    if (copie) memcpy(copie, s, n);
    return copie;                  // l'APPELANT doit appeler free(copie)
}

int main(void) {
    char *c = dupliquer("texte");
    if (c) { puts(c); free(c); }
    else   { fprintf(stderr, "Erreur : allocation impossible\n"); }
    return 0;
}
```

```c
#include <stdio.h>
#include <stdlib.h>

int *creer_tableau(size_t n, int valeur) {
    int *t = malloc(n * sizeof *t);
    if (!t) return NULL;
    for (size_t i = 0; i < n; i++) t[i] = valeur;
    return t;
}

int main(void) {
    int *t = creer_tableau(4, 7);
    if (!t) {
        fprintf(stderr, "Erreur : allocation impossible\n");
        return EXIT_FAILURE;
    }
    for (int i = 0; i < 4; i++) printf("%d ", t[i]);
    putchar('\n');
    free(t);                      // l'appelant libère
    return 0;
}
```

### 3. Variable `static` (à éviter)

```c
#include <stdio.h>

const char *nom_du_jour(int j) {
    static const char *noms[] = {"Lun", "Mar", "Mer"};   // chaînes constantes : sûr
    return noms[j];
}

int main(void) {
    for (int j = 0; j < 3; j++) printf("%d -> %s\n", j, nom_du_jour(j));
    return 0;
}
```

Retourner un **littéral** ou un tableau `static` constant est sûr ; retourner un tampon `static` modifiable est piégeux (écrasé au prochain appel, dangereux avec des fils d'exécution).

### 4. Structure

```c
#include <stdio.h>

struct Triplet { int v[3]; };
struct Triplet fabriquer(void) { return (struct Triplet){ .v = {1, 2, 3} }; }

int main(void) {
    struct Triplet t = fabriquer();
    printf("%d %d %d\n", t.v[0], t.v[1], t.v[2]);
    return 0;
}
```

## 15.3 Ce qu'il ne faut jamais faire

```c
#include <stdio.h>

char *mauvais(void) {
    char tampon[20] = "perdu";
    return tampon;        // Erreur : tableau local détruit à la sortie
}

int main(void) {
    char *p = mauvais();  // gcc : warning: function returns address of local variable
    (void)p;              // p est un pointeur pendant : on ne le lit pas
    fprintf(stderr, "Erreur : mauvais() retourne un tableau local détruit à la sortie\n");
    return 0;
}
```

---

# 16. Structures de données dynamiques

## 16.1 Liste simplement chaînée

Chaque **nœud** contient une donnée et un pointeur vers le suivant.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Noeud {
    int valeur;
    struct Noeud *suivant;
} Noeud;

// Ajout en tête : O(1)
Noeud *ajouter_tete(Noeud *tete, int valeur) {
    Noeud *n = malloc(sizeof *n);
    if (!n) return tete;                 // échec : liste inchangée
    n->valeur = valeur;
    n->suivant = tete;
    return n;
}

// Ajout en queue : O(n)
Noeud *ajouter_queue(Noeud *tete, int valeur) {
    Noeud *n = malloc(sizeof *n);
    if (!n) return tete;
    n->valeur = valeur;
    n->suivant = NULL;
    if (!tete) return n;
    Noeud *p = tete;
    while (p->suivant) p = p->suivant;
    p->suivant = n;
    return tete;
}

// Suppression d'une valeur
Noeud *supprimer(Noeud *tete, int valeur) {
    Noeud **pp = &tete;                  // pointeur double : élégant (voir section 17)
    while (*pp && (*pp)->valeur != valeur) pp = &(*pp)->suivant;
    if (*pp) {
        Noeud *a_liberer = *pp;
        *pp = a_liberer->suivant;
        free(a_liberer);
    }
    return tete;
}

void afficher(const Noeud *tete) {
    for (; tete; tete = tete->suivant) printf("%d -> ", tete->valeur);
    puts("NULL");
}

void liberer(Noeud *tete) {
    while (tete) {
        Noeud *suivant = tete->suivant;  // sauvegarder AVANT de libérer
        free(tete);
        tete = suivant;
    }
}

int main(void) {
    Noeud *liste = NULL;
    liste = ajouter_tete(liste, 3);
    liste = ajouter_tete(liste, 2);
    liste = ajouter_queue(liste, 4);
    afficher(liste);                     // 2 -> 3 -> 4 -> NULL
    liste = supprimer(liste, 3);
    afficher(liste);
    liberer(liste);
    return 0;
}
```

## 16.2 Autres structures

| Structure | Principe |
| --- | --- |
| **Liste doublement chaînée** | Pointeurs `precedent` et `suivant` |
| **Pile** (LIFO) | Ajout/retrait en tête |
| **File** (FIFO) | Ajout en queue, retrait en tête |
| **Arbre binaire de recherche** | Nœuds avec `gauche` / `droite` |
| **Table de hachage** | Tableau de listes (chaînage) indexé par une fonction de hachage |

## 16.3 Tableau dynamique extensible (vecteur)

```c
// Compiler avec : gcc -std=c17 vecteur.c -o vecteur   (en C23, <stdbool.h> est inutile)
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *donnees;
    size_t taille, capacite;
} Vecteur;

bool vecteur_ajouter(Vecteur *v, int x) {
    if (v->taille == v->capacite) {
        size_t nouvelle = v->capacite ? v->capacite * 2 : 4;     // doublement : coût amorti O(1)
        int *tmp = realloc(v->donnees, nouvelle * sizeof *tmp);
        if (!tmp) return false;
        v->donnees = tmp;
        v->capacite = nouvelle;
    }
    v->donnees[v->taille++] = x;
    return true;
}

int main(void) {
    Vecteur v = {0};
    for (int i = 1; i <= 10; i++) {
        if (!vecteur_ajouter(&v, i * i)) {
            fprintf(stderr, "Erreur : allocation impossible\n");
            free(v.donnees);
            return EXIT_FAILURE;
        }
    }
    printf("taille = %zu, capacité = %zu\n", v.taille, v.capacite);
    for (size_t i = 0; i < v.taille; i++) printf("%d ", v.donnees[i]);
    putchar('\n');
    free(v.donnees);
    return 0;
}
```

## 16.4 Matrices dynamiques

### Méthode A : tableau de pointeurs (lignes indépendantes)

```c
#include <stdio.h>
#include <stdlib.h>

int **creer_matrice(size_t l, size_t c) {
    int **m = malloc(l * sizeof *m);
    if (!m) return NULL;
    for (size_t i = 0; i < l; i++) {
        m[i] = calloc(c, sizeof **m);
        if (!m[i]) {                           // échec : libérer ce qui a été alloué
            while (i--) free(m[i]);
            free(m);
            return NULL;
        }
    }
    return m;
}

void liberer_matrice(int **m, size_t l) {
    for (size_t i = 0; i < l; i++) free(m[i]);
    free(m);
}

int main(void) {
    size_t l = 2, c = 3;
    int **m = creer_matrice(l, c);
    if (!m) {
        fprintf(stderr, "Erreur : allocation impossible\n");
        return EXIT_FAILURE;
    }
    for (size_t i = 0; i < l; i++)
        for (size_t j = 0; j < c; j++) m[i][j] = (int)(i * c + j);
    for (size_t i = 0; i < l; i++) {
        for (size_t j = 0; j < c; j++) printf("%d ", m[i][j]);
        putchar('\n');
    }
    liberer_matrice(m, l);
    return 0;
}
```

### Méthode B : bloc unique contigu (plus efficace)

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    size_t l = 2, c = 3, i = 1, j = 2;
    int *m = calloc(l * c, sizeof *m);       // un seul malloc, un seul free
    if (!m) {
        fprintf(stderr, "Erreur : allocation impossible\n");
        return EXIT_FAILURE;
    }
    m[i * c + j] = 5;                        // élément (i, j)
    printf("m[%zu][%zu] = %d\n", i, j, m[i * c + j]);
    free(m);
    return 0;
}
```

Ou avec un pointeur vers tableau (accès naturel `m[i][j]`, C99) :

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    size_t l = 2, c = 3, i = 1, j = 2;
    int (*m)[c] = calloc(l, sizeof *m);      // c doit être connu à l'exécution (VLA type)
    if (!m) {
        fprintf(stderr, "Erreur : allocation impossible\n");
        return EXIT_FAILURE;
    }
    m[i][j] = 5;
    printf("m[%zu][%zu] = %d\n", i, j, m[i][j]);
    free(m);
    return 0;
}
```

---

# 17. Pointeurs doubles

## 17.1 Définition

Un **pointeur double** (`type **`) contient l'**adresse d'un pointeur**.

```c
#include <stdio.h>

int main(void) {
    int x = 10;
    int *p = &x;
    int **pp = &p;

    **pp = 20;         // modifie x
    printf("x = %d, *p = %d, **pp = %d\n", x, *p, **pp);
    return 0;
}
```

```text
pp ──▶ p ──▶ x
```

## 17.2 Usages principaux

### 1. Modifier un pointeur depuis une fonction

```c
#include <stdio.h>
#include <stdlib.h>

void allouer(int **p, size_t n) {
    *p = malloc(n * sizeof **p);        // modifie le pointeur de l'appelant
}

int main(void) {
    int *tab = NULL;
    allouer(&tab, 10);
    if (tab == NULL) {
        fprintf(stderr, "Erreur : allocation impossible\n");
        return EXIT_FAILURE;
    }
    for (int i = 0; i < 10; i++) tab[i] = i;
    printf("tab[9] = %d\n", tab[9]);
    free(tab);
    return 0;
}
```

Sans pointeur double, la fonction ne recevrait qu'une **copie** du pointeur.

### 2. Tableau de chaînes / matrices

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *dupliquer(const char *s) {
    size_t n = strlen(s) + 1;
    char *copie = malloc(n);
    if (copie) memcpy(copie, s, n);
    return copie;
}

int main(void) {
    char **lignes = malloc(3 * sizeof *lignes);
    if (!lignes) return EXIT_FAILURE;
    for (int i = 0; i < 3; i++) lignes[i] = dupliquer("texte");
    for (int i = 0; i < 3; i++) printf("lignes[%d] = %s\n", i, lignes[i]);
    // … puis libérer chaque ligne, puis le tableau
    for (int i = 0; i < 3; i++) free(lignes[i]);
    free(lignes);
    return 0;
}
```

### 3. Listes chaînées (insertion / suppression élégante)

Voir `supprimer()` à la [section 16](#16-structures-de-données-dynamiques) : `Noeud **pp = &tete;`.

### 4. `argv` : `char **argv` (voir [section 23](#23-arguments-de-la-ligne-de-commande)).

## 17.3 Libération

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void liberer_lignes(char **t, size_t n) {
    for (size_t i = 0; i < n; i++) free(t[i]);   // d'abord le contenu
    free(t);                                      // puis le tableau de pointeurs
}

int main(void) {
    size_t n = 3;
    char **t = malloc(n * sizeof *t);
    if (!t) return EXIT_FAILURE;
    for (size_t i = 0; i < n; i++) {
        t[i] = malloc(16);
        if (!t[i]) {
            fprintf(stderr, "Erreur : allocation impossible\n");
            liberer_lignes(t, i);
            return EXIT_FAILURE;
        }
        snprintf(t[i], 16, "ligne %zu", i);
    }
    for (size_t i = 0; i < n; i++) puts(t[i]);
    liberer_lignes(t, n);
    return 0;
}
```

> **Attention** : Un `int **` **n'est pas** un `int [][N]` : ce sont des représentations mémoire différentes, non interchangeables.

---

# 18. Structures et unions

## 18.1 Structures (`struct`)

Une **structure** regroupe des données de **types différents** sous un seul nom.

```c
#include <stdio.h>

struct Etudiant {
    char nom[50];
    int age;
    float moyenne;
};

int main(void) {
    struct Etudiant e1 = {"Alice", 20, 15.5f};
    struct Etudiant e2 = { .nom = "Bob", .age = 22, .moyenne = 12.0f };   // initialisation désignée (C99)

    e1.age = 21;                              // accès avec .
    struct Etudiant *p = &e1;
    printf("%s\n", p->nom);                   // accès via un pointeur avec ->
    printf("%s a %d ans, moyenne %.1f\n", e1.nom, e1.age, e1.moyenne);
    printf("%s a %d ans, moyenne %.1f\n", e2.nom, e2.age, e2.moyenne);
    return 0;
}
```

### Opérations

```c
#include <stdio.h>
#include <string.h>

struct Etudiant { char nom[50]; int age; float moyenne; };

static int egaux(const struct Etudiant *a, const struct Etudiant *b) {   // comparaison champ par champ
    return strcmp(a->nom, b->nom) == 0 && a->age == b->age && a->moyenne == b->moyenne;
}

int main(void) {
    struct Etudiant e1 = {"Alice", 20, 15.5f};
    struct Etudiant e2 = {"Bob", 22, 12.0f};

    struct Etudiant copie = e1;               // copie complète (affectation autorisée)
    printf("copie : %s, %d ans\n", copie.nom, copie.age);

    // if (e1 == e2) { }   // error: invalid operands to binary == (have 'struct Etudiant' and 'struct Etudiant')
    fprintf(stderr, "Erreur de compilation si on écrit e1 == e2 : comparaison de structures interdite\n");
    printf("e1 et e2 égaux : %d\n", egaux(&e1, &e2));
    printf("e1 et copie égaux : %d\n", egaux(&e1, &copie));
    return 0;
}
```

### Littéraux composés (C99)

```c
#include <stdio.h>

struct Point { int x, y; };

void afficher_point(struct Point p) { printf("(%d, %d)\n", p.x, p.y); }

int main(void) {
    afficher_point((struct Point){ .x = 1, .y = 2 });   // littéral composé
    return 0;
}
```

### Structures imbriquées et tableaux de structures

```c
#include <stdio.h>

struct Date { int j, m, a; };
struct Personne { char nom[30]; struct Date naissance; };
struct Etudiant { char nom[50]; int age; float moyenne; };

int main(void) {
    struct Personne p = { "Alice", { 14, 3, 2005 } };
    printf("%s est née le %02d/%02d/%d\n", p.nom, p.naissance.j, p.naissance.m, p.naissance.a);

    struct Etudiant classe[30];
    for (size_t i = 0; i < 30; i++) classe[i].age = 18;
    printf("classe[0].age = %d, classe[29].age = %d\n", classe[0].age, classe[29].age);
    return 0;
}
```

### Structure auto-référencée

```c
#include <stdio.h>

struct Noeud { int valeur; struct Noeud *suivant; };   // pointeur vers son propre type

int main(void) {
    struct Noeud b = { 2, NULL };
    struct Noeud a = { 1, &b };
    for (struct Noeud *p = &a; p; p = p->suivant) printf("%d -> ", p->valeur);
    puts("NULL");
    return 0;
}
```

## 18.2 Alignement et remplissage (*padding*)

Le compilateur insère des octets de **remplissage** pour **aligner** les membres.

```c
#include <stddef.h>
#include <stdio.h>

struct A { char c; int i; char d; };   // typiquement 12 octets
struct B { int i; char c; char d; };   // typiquement 8 octets (mieux ordonné)

int main(void) {
    printf("sizeof(struct A) = %zu\n", sizeof(struct A));
    printf("sizeof(struct B) = %zu\n", sizeof(struct B));
    printf("offsetof(struct A, i) = %zu\n", offsetof(struct A, i));   // décalage du membre i
    return 0;
}
```

> **Astuce** : Ordonnez les membres **du plus grand au plus petit** pour réduire le remplissage. Ne comparez pas de structures avec `memcmp` (les octets de remplissage sont indéterminés).

## 18.3 Champs de bits

```c
#include <stdio.h>

struct Drapeaux {
    unsigned int lecture  : 1;
    unsigned int ecriture : 1;
    unsigned int mode     : 3;
};

int main(void) {
    struct Drapeaux d = { .lecture = 1, .ecriture = 0, .mode = 5 };
    printf("lecture = %u, ecriture = %u, mode = %u\n", d.lecture, d.ecriture, d.mode);
    printf("sizeof(struct Drapeaux) = %zu\n", sizeof d);
    return 0;
}
```

Utile pour des registres matériels ; **la disposition mémoire dépend du compilateur** (peu portable).

## 18.4 Membre de tableau flexible (C99)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Message {
    size_t longueur;
    char donnees[];                     // taille variable, en fin de structure
};

int main(void) {
    struct Message *m = malloc(sizeof *m + 100);
    if (!m) {
        fprintf(stderr, "Erreur : allocation impossible\n");
        return EXIT_FAILURE;
    }
    strcpy(m->donnees, "Bonjour");
    m->longueur = strlen(m->donnees);
    printf("sizeof *m = %zu, longueur = %zu, donnees = %s\n", sizeof *m, m->longueur, m->donnees);
    free(m);
    return 0;
}
```

## 18.5 Unions

Les membres d'une **union** **partagent la même zone mémoire** ; sa taille est celle de son plus grand membre. Un seul membre est valide à la fois.

```c
#include <stdio.h>

union Valeur {
    int i;
    float f;
    char c[4];
};

int main(void) {
    union Valeur v;
    printf("sizeof(union Valeur) = %zu\n", sizeof v);
    v.i = 42;
    printf("v.i = %d\n", v.i);
    v.f = 3.14f;        // écrase la valeur précédente
    printf("v.f = %.2f\n", v.f);
    printf("v.i = %d (les mêmes octets, lus comme un int : sans intérêt)\n", v.i);
    return 0;
}
```

### Union étiquetée (*tagged union*) : usage sûr

```c
#include <stdio.h>

typedef enum { T_ENTIER, T_REEL, T_TEXTE } Type;

typedef struct {
    Type type;                          // l'étiquette indique le membre actif
    union {
        int entier;
        double reel;
        const char *texte;
    };                                  // union anonyme (C11)
} Variant;

void afficher(const Variant *v) {
    switch (v->type) {
        case T_ENTIER: printf("%d\n", v->entier); break;
        case T_REEL:   printf("%g\n", v->reel);   break;
        case T_TEXTE:  puts(v->texte);            break;
    }
}

int main(void) {
    Variant a = { .type = T_ENTIER, .entier = 42 };
    Variant b = { .type = T_REEL,   .reel = 3.14 };
    Variant c = { .type = T_TEXTE,  .texte = "bonjour" };
    afficher(&a);
    afficher(&b);
    afficher(&c);
    return 0;
}
```

## 18.6 Structure ou union ?

| | `struct` | `union` |
| --- | --- | --- |
| Mémoire | Somme des membres (+ remplissage) | Taille du plus grand membre |
| Membres valides | **Tous** simultanément | **Un seul** à la fois |
| Usage | Regrouper des données | Économiser la mémoire, représenter des variantes |

---

# 19. Énumérations (`enum`)

## 19.1 Définition

Une **énumération** définit un ensemble de **constantes entières nommées**.

```c
#include <stdio.h>

enum Jour { LUNDI, MARDI, MERCREDI, JEUDI, VENDREDI, SAMEDI, DIMANCHE };
// LUNDI = 0, MARDI = 1, …

int main(void) {
    enum Jour aujourdhui = MERCREDI;
    printf("%d\n", aujourdhui);              // 2
    return 0;
}
```

### Valeurs explicites

```c
#include <stdio.h>

enum Code { OK = 200, NON_TROUVE = 404, ERREUR = 500 };
enum Mois { JANVIER = 1, FEVRIER, MARS };     // FEVRIER = 2, MARS = 3
enum Options { OPT_A = 1 << 0, OPT_B = 1 << 1, OPT_C = 1 << 2 };   // drapeaux combinables par |

int main(void) {
    printf("OK = %d, NON_TROUVE = %d, ERREUR = %d\n", OK, NON_TROUVE, ERREUR);
    printf("FEVRIER = %d, MARS = %d\n", FEVRIER, MARS);
    int options = OPT_A | OPT_C;
    printf("options = %d, OPT_B actif : %s\n", options, (options & OPT_B) ? "oui" : "non");
    return 0;
}
```

### Type sous-jacent *(C23)*

```c
// Compiler avec : gcc -std=c23 enum_type.c -o enum_type
#include <stdio.h>

enum Couleur : unsigned char { ROUGE, VERT, BLEU };   // type imposé

int main(void) {
    enum Couleur c = BLEU;
    printf("c = %d, sizeof(enum Couleur) = %zu\n", c, sizeof c);   // 1 octet
    return 0;
}
```

## 19.2 Avec `typedef` et `switch`

```c
#include <stdio.h>

typedef enum { ROUGE, VERT, BLEU } Couleur;

void decrire(Couleur c) {
    switch (c) {
        case ROUGE: puts("rouge"); break;
        case VERT:  puts("vert");  break;
        case BLEU:  puts("bleu");  break;
    }
}

int main(void) {
    decrire(ROUGE);
    decrire(VERT);
    decrire(BLEU);
    return 0;
}
```

> **Astuce** : Compilez avec `-Wall` : le compilateur avertit si un `case` d'un `enum` est oublié dans un `switch` sans `default`.

## 19.3 Particularités

- Les constantes d'énumération sont de type **`int`** en C (≠ C++) et **partagent la portée** de l'enum : deux enums ne peuvent pas avoir la même constante.
- C **n'empêche pas** d'affecter n'importe quelle valeur entière à une variable `enum`.
- Astuce : ajouter une constante finale `NB_JOURS` pour compter les éléments.
- Une table de noms parallèle :

```c
#include <stdio.h>

enum Jour { LUNDI, MARDI, MERCREDI, NB_JOURS };   // NB_JOURS compte les éléments

static const char *noms_jours[] = { [LUNDI] = "Lundi", [MARDI] = "Mardi", [MERCREDI] = "Mercredi" };

int main(void) {
    for (int j = 0; j < NB_JOURS; j++) printf("%d : %s\n", j, noms_jours[j]);
    return 0;
}
```

---

# 20. `typedef`

## 20.1 Créer un alias de type

```c
#include <stdio.h>

typedef unsigned long ulong;

typedef struct {
    int x, y;
} Point;                      // plus besoin d'écrire « struct Point »

int main(void) {
    ulong n = 1000;
    Point p = {1, 2};
    printf("n = %lu, p = (%d, %d)\n", n, p.x, p.y);
    return 0;
}
```

## 20.2 Usages courants

```c
#include <stdio.h>
#include <stdlib.h>

typedef enum { ROUGE, VERT } Couleur;
typedef int (*Comparateur)(const void *, const void *);    // alias de pointeur de fonction
typedef char Nom[50];                                      // alias de tableau
typedef struct Noeud Noeud;                                // déclaration anticipée
struct Noeud { int v; Noeud *suivant; };

static int croissant(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

int main(void) {
    Couleur c = VERT;
    Comparateur cmp = croissant;
    Nom nom = "Alice";
    Noeud fin = { 2, NULL };
    Noeud debut = { 1, &fin };
    int t[] = { 3, 1, 2 };

    qsort(t, 3, sizeof t[0], cmp);
    printf("couleur = %d, nom = %s, t = %d %d %d\n", c, nom, t[0], t[1], t[2]);
    printf("liste : %d -> %d\n", debut.v, debut.suivant->v);
    return 0;
}
```

## 20.3 `typedef` ou `#define` ?

| | `typedef` | `#define` |
| --- | --- | --- |
| Traité par | Le **compilateur** (a un type) | Le **préprocesseur** (texte) |
| Portée | Respectée | Globale au fichier |
| Pointeurs | `typedef int *PInt; PInt a, b;` → deux pointeurs (correct) | `#define PInt int *` → `PInt a, b;` : seul `a` est un pointeur (piège) |

## 20.4 Bonnes pratiques

- Utilisez `typedef` pour **simplifier** (structures, pointeurs de fonctions) et **abstraire** (types portables comme `size_t`).
- Évitez de masquer les pointeurs derrière un `typedef` (cela cache `*`).
- Conventions : types en `PascalCase` ou suffixe `_t` (attention : le suffixe `_t` est réservé par POSIX).

---

# 21. Pointeurs de fonctions

*(Section ajoutée : notion fondamentale absente du guide d'origine.)*

## 21.1 Principe

Une fonction a une **adresse** : on peut la stocker dans un pointeur, la passer en argument et l'appeler indirectement. C'est la base des **rappels** (*callbacks*), des tables de dispatch et du polymorphisme en C.

```c
#include <stdio.h>

int additionner(int a, int b) { return a + b; }
int soustraire(int a, int b) { return a - b; }

int main(void) {
    int (*operation)(int, int);        // pointeur vers une fonction (int, int) → int
    operation = additionner;           // (ou &additionner)
    printf("%d\n", operation(3, 2));   // 5
    operation = soustraire;
    printf("%d\n", operation(3, 2));   // 1
    return 0;
}
```

La syntaxe `type (*nom)(paramètres)` : les **parenthèses autour de `*nom`** sont indispensables (`int *f(int)` déclare une fonction retournant un `int *`).

## 21.2 Avec `typedef`

```c
#include <stdio.h>

typedef int (*Operation)(int, int);

int additionner(int a, int b) { return a + b; }

int appliquer(Operation f, int a, int b) { return f(a, b); }

int main(void) {
    printf("%d\n", appliquer(additionner, 4, 5));   // 9
    return 0;
}
```

## 21.3 Callbacks : `qsort`

```c
#include <stdio.h>
#include <stdlib.h>

struct Personne { const char *nom; int age; };

int par_age(const void *a, const void *b) {
    const struct Personne *p = a, *q = b;
    return (p->age > q->age) - (p->age < q->age);
}

int main(void) {
    struct Personne personnes[] = { {"Chloé", 31}, {"Alice", 25}, {"Bob", 42} };
    size_t n = sizeof personnes / sizeof personnes[0];
    qsort(personnes, n, sizeof personnes[0], par_age);
    for (size_t i = 0; i < n; i++) printf("%s (%d ans)\n", personnes[i].nom, personnes[i].age);
    return 0;
}
```

## 21.4 Table de fonctions

```c
#include <stdio.h>
#include <string.h>

typedef int (*Operation)(int, int);

int additionner(int a, int b) { return a + b; }
int soustraire(int a, int b) { return a - b; }

typedef struct { const char *nom; Operation f; } Commande;

static const Commande commandes[] = {
    { "add", additionner },
    { "sub", soustraire },
};

int main(void) {
    const char *saisie = "sub";
    int trouve = 0;
    for (size_t i = 0; i < sizeof commandes / sizeof commandes[0]; i++)
        if (strcmp(commandes[i].nom, saisie) == 0) {
            printf("%d\n", commandes[i].f(6, 3));
            trouve = 1;
        }
    if (!trouve) fprintf(stderr, "Erreur : commande inconnue : %s\n", saisie);
    saisie = "mul";
    trouve = 0;
    for (size_t i = 0; i < sizeof commandes / sizeof commandes[0]; i++)
        if (strcmp(commandes[i].nom, saisie) == 0) trouve = 1;
    if (!trouve) fprintf(stderr, "Erreur : commande inconnue : %s\n", saisie);
    return 0;
}
```

## 21.5 Simuler des méthodes (« objets » en C)

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Forme {
    double (*aire)(const struct Forme *);
    void (*detruire)(struct Forme *);
} Forme;

typedef struct { Forme base; double rayon; } Cercle;     // base en premier membre

static double aire_cercle(const Forme *f) {
    const Cercle *c = (const Cercle *)f;
    return 3.14159 * c->rayon * c->rayon;
}
static void detruire_cercle(Forme *f) { free(f); }

Forme *creer_cercle(double rayon) {
    Cercle *c = malloc(sizeof *c);
    if (!c) return NULL;
    c->base.aire = aire_cercle;
    c->base.detruire = detruire_cercle;
    c->rayon = rayon;
    return &c->base;
}

int main(void) {
    Forme *f = creer_cercle(2.0);
    if (!f) {
        fprintf(stderr, "Erreur : allocation impossible\n");
        return EXIT_FAILURE;
    }
    printf("aire = %.2f\n", f->aire(f));     // appel « méthode »
    f->detruire(f);
    return 0;
}
```

## 21.6 Sélection générique : `_Generic` (C11)

```c
#include <stdio.h>

void afficher_int(int x)           { printf("int : %d\n", x); }
void afficher_double(double x)     { printf("double : %g\n", x); }
void afficher_autre(const char *x) { printf("autre : %s\n", x); }

#define afficher(x) _Generic((x), int: afficher_int, double: afficher_double, default: afficher_autre)(x)

int main(void) {
    afficher(42);
    afficher(3.14);
    afficher("texte");
    return 0;
}
```

---

# Niveau avancé

---

# 22. Gestion des fichiers

## 22.1 Le type `FILE *` et les opérations

Les fonctions de `<stdio.h>` manipulent les fichiers via un **flux** représenté par un pointeur `FILE *`.

| Opération | Fonctions |
| --- | --- |
| Ouvrir / fermer | `fopen`, `fclose` |
| Texte formaté | `fprintf`, `fscanf` |
| Lignes / caractères | `fgets`, `fputs`, `fgetc`, `fputc` |
| Binaire | `fread`, `fwrite` |
| Position | `fseek`, `ftell`, `rewind`, `fgetpos`, `fsetpos` |
| État | `feof`, `ferror`, `clearerr`, `fflush` |
| Gestion | `remove`, `rename`, `tmpfile` |

## 22.2 Ouvrir et fermer

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *f = fopen("fichier_absent.txt", "r");
    if (f == NULL) {
        perror("fopen");                 // affiche : fopen: No such file or directory
        return EXIT_FAILURE;
    }
    /* … utilisation … */
    fclose(f);                           // toujours fermer (vide les tampons)
    return 0;
}
```

| Mode | Signification |
| --- | --- |
| `"r"` | Lecture ; le fichier **doit exister** |
| `"w"` | Écriture ; **crée ou écrase** |
| `"a"` | Ajout en fin de fichier (crée si absent) |
| `"r+"` | Lecture + écriture (fichier existant) |
| `"w+"` | Lecture + écriture, **écrase** |
| `"a+"` | Lecture + ajout |
| `"x"` *(C11)* | Avec `w` : **échoue si le fichier existe** (`"wx"`) |
| `"b"` | Mode binaire (`"rb"`, `"wb"`) |

## 22.3 Écrire du texte

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *f = fopen("sortie.txt", "w");
    if (!f) { perror("fopen"); return EXIT_FAILURE; }

    fprintf(f, "Nom : %s, âge : %d\n", "Alice", 30);
    fputs("Une ligne\n", f);
    fputc('A', f);

    if (fclose(f) != 0) perror("fclose");   // fclose peut échouer (disque plein) : vérifiez-le

    f = fopen("sortie.txt", "r");           // relecture pour afficher le résultat
    if (!f) { perror("fopen"); return EXIT_FAILURE; }
    int c;
    while ((c = fgetc(f)) != EOF) putchar(c);
    putchar('\n');
    fclose(f);
    return 0;
}
```

## 22.4 Lire du texte

### Ligne par ligne (recommandé)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    FILE *f = fopen("lignes.txt", "w");     // préparation du fichier
    if (!f) { perror("fopen"); return EXIT_FAILURE; }
    fputs("premiere ligne\ndeuxieme ligne\n", f);
    fclose(f);

    f = fopen("lignes.txt", "r");
    if (!f) { perror("fopen"); return EXIT_FAILURE; }
    char ligne[256];
    while (fgets(ligne, sizeof ligne, f) != NULL) {
        ligne[strcspn(ligne, "\n")] = '\0';
        printf("Lu : %s\n", ligne);
    }
    fclose(f);
    return 0;
}
```

### Caractère par caractère

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *f = fopen("caracteres.txt", "w");     // préparation du fichier
    if (!f) { perror("fopen"); return EXIT_FAILURE; }
    fputs("Bonjour\n", f);
    fclose(f);

    f = fopen("caracteres.txt", "r");
    if (!f) { perror("fopen"); return EXIT_FAILURE; }
    int c;                                   // int et non char, pour distinguer EOF
    while ((c = fgetc(f)) != EOF) putchar(c);
    fclose(f);
    return 0;
}
```

### Formaté avec `fscanf`

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *f = fopen("personnes.txt", "w");     // préparation du fichier
    if (!f) { perror("fopen"); return EXIT_FAILURE; }
    fputs("Alice 30\nBob 25\n", f);
    fclose(f);

    f = fopen("personnes.txt", "r");
    if (!f) { perror("fopen"); return EXIT_FAILURE; }
    char nom[50]; int age;
    while (fscanf(f, "%49s %d", nom, &age) == 2) {      // vérifier le nombre de valeurs lues
        printf("%s a %d ans\n", nom, age);
    }
    fclose(f);
    return 0;
}
```

> **Ne bouclez jamais sur `while (!feof(f))`** : `feof` n'est vrai qu'**après** une lecture ayant échoué, ce qui traite une dernière fois des données invalides. Testez la valeur **de retour** de la fonction de lecture.

Distinguer fin de fichier et erreur :

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *f = fopen("lignes.txt", "w");     // préparation du fichier
    if (!f) { perror("fopen"); return EXIT_FAILURE; }
    fputs("une ligne\n", f);
    fclose(f);

    f = fopen("lignes.txt", "r");
    if (!f) { perror("fopen"); return EXIT_FAILURE; }
    char ligne[256];
    while (fgets(ligne, sizeof ligne, f) != NULL) { }   // lecture jusqu'à l'échec

    if (ferror(f)) perror("lecture");
    else if (feof(f)) puts("Fin du fichier");
    fclose(f);
    return 0;
}
```

## 22.5 Fichiers binaires

```c
#include <stdio.h>
#include <stdlib.h>

struct Personne { char nom[30]; int age; };

int main(void) {
    // Écriture
    struct Personne p = {"Alice", 30};
    FILE *f = fopen("data.bin", "wb");
    if (!f) { perror("fopen"); return EXIT_FAILURE; }
    if (fwrite(&p, sizeof p, 1, f) != 1) {          // renvoie le nombre d'éléments écrits
        fprintf(stderr, "Erreur : écriture incomplète\n");
    }
    fclose(f);

    // Lecture
    struct Personne q = {"", 0};
    f = fopen("data.bin", "rb");
    if (!f) { perror("fopen"); return EXIT_FAILURE; }
    if (fread(&q, sizeof q, 1, f) == 1) printf("%s, %d ans\n", q.nom, q.age);
    else fprintf(stderr, "Erreur : lecture incomplète\n");
    fclose(f);
    return 0;
}
```

> **Attention** : Les fichiers binaires dépendent de l'**architecture** (taille des types, **endianness**, remplissage des structures) : ils ne sont pas forcément portables entre machines. Pour échanger des données, préférez un format texte (CSV, JSON) ou sérialisez champ par champ avec des types de taille fixe.

### Texte ou binaire ?

| | Texte | Binaire |
| --- | --- | --- |
| Lisible par l'humain | Oui | Non |
| Conversion des fins de ligne (`\n` ↔ `\r\n`) | Oui (Windows) | **Non** |
| Taille / vitesse | Plus grand, plus lent | Compact, rapide |
| Portabilité | Oui | Limitée |

## 22.6 Se positionner dans un fichier

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *f = fopen("positions.txt", "w+");   // lecture + écriture
    if (!f) { perror("fopen"); return EXIT_FAILURE; }
    fputs("0123456789ABCDEFGHIJ", f);

    fseek(f, 0, SEEK_END);          // aller à la fin
    long taille = ftell(f);         // position courante = taille du fichier
    printf("taille = %ld\n", taille);
    rewind(f);                      // retour au début
    printf("début : %c\n", fgetc(f));
    fseek(f, 10, SEEK_SET);         // 10 octets depuis le début
    printf("à 10 : %c\n", fgetc(f));
    fseek(f, -5, SEEK_CUR);         // reculer de 5
    printf("après recul de 5 : %c\n", fgetc(f));
    fclose(f);
    return 0;
}
```

Constantes : `SEEK_SET` (début), `SEEK_CUR` (position courante), `SEEK_END` (fin).

### Lire un fichier entier en mémoire

```c
#include <stdio.h>
#include <stdlib.h>

char *lire_fichier(const char *chemin, size_t *taille) {
    FILE *f = fopen(chemin, "rb");
    if (!f) return NULL;
    fseek(f, 0, SEEK_END);
    long n = ftell(f);
    rewind(f);
    char *contenu = malloc((size_t)n + 1);
    if (contenu && fread(contenu, 1, (size_t)n, f) == (size_t)n) {
        contenu[n] = '\0';
        if (taille) *taille = (size_t)n;
    } else {
        free(contenu);
        contenu = NULL;
    }
    fclose(f);
    return contenu;
}

int main(void) {
    FILE *f = fopen("exemple.txt", "w");     // préparation du fichier
    if (!f) { perror("fopen"); return EXIT_FAILURE; }
    fputs("Contenu du fichier\n", f);
    fclose(f);

    size_t taille = 0;
    char *texte = lire_fichier("exemple.txt", &taille);
    if (texte) { printf("%zu octets : %s", taille, texte); free(texte); }

    if (!lire_fichier("fichier_absent.txt", NULL)) {
        fprintf(stderr, "Erreur : lecture de fichier_absent.txt impossible\n");
    }
    return 0;
}
```

## 22.7 Opérations sur les fichiers

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *f = fopen("ancien.txt", "w");      // création d'un fichier à manipuler
    if (!f) { perror("fopen"); return EXIT_FAILURE; }
    fputs("texte\n", f);
    fflush(f);                                // forcer l'écriture du tampon
    fclose(f);

    if (rename("ancien.txt", "nouveau.txt") != 0) perror("rename");    // renommer / déplacer
    else puts("ancien.txt renommé en nouveau.txt");

    FILE *tmp = tmpfile();                    // fichier temporaire supprimé à la fermeture
    if (tmp) { fputs("temporaire\n", tmp); fclose(tmp); puts("fichier temporaire créé et fermé"); }

    if (remove("nouveau.txt") != 0) perror("remove");                  // supprimer
    else puts("nouveau.txt supprimé");

    if (remove("temporaire.txt") != 0) perror("remove");   // erreur : le fichier n'existe pas
    return 0;
}
```

## 22.8 Bonnes pratiques

- **Vérifiez** `fopen` (≠ `NULL`), les valeurs de retour de `fread` / `fwrite` / `fclose`.
- **Fermez** tout fichier ouvert, y compris en cas d'erreur (motif `goto` de nettoyage, section 8).
- Ouvrez en `"wx"` pour ne pas écraser un fichier existant par accident.
- Les chemins : `/` fonctionne partout (même sous Windows) ; en littéral, doublez les antislashs (`"C:\\dossier\\f.txt"`).
- Pour les gros fichiers (> 2 Go), utilisez les fonctions 64 bits (`fseeko` / `ftello` sous POSIX).
- Écrire dans un fichier temporaire puis `rename` permet une écriture **atomique** d'un fichier de configuration.

---

# 23. Arguments de la ligne de commande

## 23.1 `argc` et `argv`

```c
#include <stdio.h>

int main(int argc, char *argv[]) {     // ou : char **argv
    printf("argc = %d, programme = %s\n", argc, argv[0]);
    return 0;
}
```

| Paramètre | Signification |
| --- | --- |
| `argc` | **Nombre** d'arguments (au moins 1) |
| `argv` | **Tableau de chaînes** (terminé par `argv[argc] == NULL`) |
| `argv[0]` | Nom (chemin) du programme |
| `argv[1]`… | Arguments fournis par l'utilisateur |

```c
#include <stdio.h>

int main(int argc, char *argv[]) {
    printf("Programme : %s\n", argv[0]);
    for (int i = 1; i < argc; i++) {
        printf("Argument %d : %s\n", i, argv[i]);
    }
    return 0;
}
```

```bash
$ ./prog bonjour "le monde" 42
Programme : ./prog
Argument 1 : bonjour
Argument 2 : le monde       # les guillemets regroupent les mots
Argument 3 : 42
```

> **Tous les arguments sont des chaînes** : convertissez les nombres explicitement.

## 23.2 Convertir en nombres (avec contrôle d'erreurs)

```c
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage : %s nombre\n", argv[0]);
        return EXIT_FAILURE;
    }
    char *fin;
    errno = 0;
    long n = strtol(argv[1], &fin, 10);
    if (errno != 0 || fin == argv[1] || *fin != '\0') {
        fprintf(stderr, "Nombre invalide : %s\n", argv[1]);
        return EXIT_FAILURE;
    }
    printf("Nombre lu : %ld\n", n);
    return 0;
}
```

`atoi` ne signale aucune erreur : à éviter. Autres : `strtoul`, `strtod`.

## 23.3 Exemple : somme d'entiers

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage : %s nombre1 [nombre2 ...]\n", argv[0]);
        return EXIT_FAILURE;
    }
    long somme = 0;
    for (int i = 1; i < argc; i++) somme += strtol(argv[i], NULL, 10);
    printf("Somme : %ld\n", somme);
    return EXIT_SUCCESS;
}
```

## 23.4 Options et drapeaux

```c
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    int verbeux = 0;
    const char *sortie = "defaut.txt";
    int i;
    for (i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-v") == 0 || strcmp(argv[i], "--verbose") == 0) verbeux = 1;
        else if (strcmp(argv[i], "-o") == 0 && i + 1 < argc) sortie = argv[++i];
        else if (strcmp(argv[i], "--") == 0) { i++; break; }          // fin des options
        else if (argv[i][0] == '-') { fprintf(stderr, "Option inconnue : %s\n", argv[i]); return 2; }
        else break;                                                    // premier argument non-option
    }
    printf("verbeux = %d, sortie = %s\n", verbeux, sortie);
    for (; i < argc; i++) printf("argument restant : %s\n", argv[i]);
    return 0;
}
```

### `getopt` (POSIX, Linux/macOS)

```c
#define _POSIX_C_SOURCE 200809L   // expose getopt avec -std=c17 / c23
#include <stdio.h>
#include <unistd.h>

static void usage(const char *prog) {
    fprintf(stderr, "Usage : %s [-v] [-o fichier] [-h] arguments...\n", prog);
}

int main(int argc, char *argv[]) {
    int verbeux = 0;
    const char *sortie = "defaut.txt";
    int opt;
    while ((opt = getopt(argc, argv, "vo:h")) != -1) {
        switch (opt) {
            case 'v': verbeux = 1; break;
            case 'o': sortie = optarg; break;            // option avec valeur
            case 'h': usage(argv[0]); return 0;
            default:  usage(argv[0]); return 1;
        }
    }
    printf("verbeux = %d, sortie = %s\n", verbeux, sortie);
    for (int i = optind; i < argc; i++) printf("argument restant : %s\n", argv[i]);   // argv[optind] … argv[argc - 1]
    return 0;
}
```

Alternative portable : `getopt_long` (options longues `--help`) ou bibliothèques tierces. Sous Windows (MSVC), `getopt` n'existe pas en standard.

## 23.5 Variables d'environnement

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    const char *home = getenv("HOME");        // NULL si absente
    if (home) printf("HOME = %s\n", home);
    else fprintf(stderr, "Erreur : HOME n'est pas définie\n");

    const char *absente = getenv("VARIABLE_QUI_N_EXISTE_PAS");
    if (!absente) fprintf(stderr, "Erreur : VARIABLE_QUI_N_EXISTE_PAS n'est pas définie\n");
    return 0;
}
```

## 23.6 Bonnes pratiques

- Vérifiez `argc` avant d'accéder à `argv[i]`.
- Affichez un message d'**usage** clair sur `stderr` et retournez un code non nul en cas d'erreur.
- Ne modifiez pas les chaînes de `argv` sans raison ; copiez-les si besoin.
- Prévoyez `--help` et `--version`.

---

# 24. Directives du préprocesseur

## 24.1 Rôle

Le **préprocesseur** traite le source **avant** la compilation. Ses directives commencent par `#`.

```bash
gcc -E programme.c        # voir le résultat du préprocesseur
```

## 24.2 `#include`

```c
// monfichier.h
#ifndef MONFICHIER_H
#define MONFICHIER_H
#define MESSAGE "Bonjour depuis monfichier.h"
#endif
```

```c
// main.c
#include <stdio.h>        // en-tête système (cherché dans les dossiers du compilateur)
#include "monfichier.h"   // en-tête du projet (cherché d'abord dans le dossier courant)

int main(void) {
    puts(MESSAGE);
    return 0;
}
```

```bash
gcc main.c -o programme && ./programme
```

## 24.3 `#define` : macros

```c
#include <stdio.h>

#define TAILLE 100                    // constante
#define CARRE(x) ((x) * (x))          // macro avec paramètre

int main(void) {
    int a = CARRE(3 + 1);             // ((3 + 1) * (3 + 1)) = 16
    printf("TAILLE = %d, CARRE(3 + 1) = %d\n", TAILLE, a);
    return 0;
}
```

### Pièges des macros

```c
#include <stdio.h>

#define MAUVAIS(x) x * x
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int main(void) {
    int r = MAUVAIS(3 + 1);           // 3 + 1 * 3 + 1 = 7 : erreur, donc toujours parenthéser
    if (r != 16) fprintf(stderr, "Erreur : MAUVAIS(3 + 1) vaut %d au lieu de 16\n", r);

    int i = 5, j = 3;
    int m = MAX(i++, j++);            // Erreur : un argument est évalué DEUX fois
    fprintf(stderr, "Erreur : après MAX(i++, j++), i = %d (au lieu de 6) et m = %d (au lieu de 5)\n", i, m);
    return 0;
}
```

> **Bonne pratique** : Préférez les **fonctions `static inline`**, les `const`/`constexpr` et les `enum` aux macros quand c'est possible : elles sont typées et sans effets de bord surprenants.

### Macros multi-instructions : `do { … } while (0)`

```c
// Compiler avec : gcc -std=c23 echanger.c -o echanger   (typeof est standard en C23)
#include <stdio.h>

#define ECHANGER(a, b) do { typeof(a) t = (a); (a) = (b); (b) = t; } while (0)

int main(void) {
    int x = 5, y = 3;
    if (x > y) ECHANGER(x, y); else puts("ok");       // fonctionne grâce au do…while(0)
    printf("x = %d, y = %d\n", x, y);
    return 0;
}
```

### Opérateurs `#` et `##`

```c
#include <stdio.h>

#define TEXTE(x) #x               // « stringification »
#define COLLER(a, b) a##b         // concaténation de jetons

int main(void) {
    puts(TEXTE(bonjour));         // "bonjour"
    int COLLER(valeur, 1) = 5;    // int valeur1 = 5;
    printf("valeur1 = %d\n", valeur1);
    return 0;
}
```

### Macros variadiques

```c
// Compiler avec : gcc -std=c23 log.c -o log
#include <stdio.h>

#define LOG(fmt, ...) fprintf(stderr, "[%s:%d] " fmt "\n", __FILE__, __LINE__ __VA_OPT__(,) __VA_ARGS__)

int main(void) {
    LOG("Démarrage");
    LOG("Valeur = %d", 42);
    return 0;
}
```

`__VA_OPT__` est standard depuis C23 (extension courante auparavant).

### `#undef`

```c
#include <stdio.h>

#define TAILLE 100

int main(void) {
    printf("TAILLE = %d\n", TAILLE);
#undef TAILLE
#ifndef TAILLE
    puts("TAILLE n'est plus définie");
#endif
#define TAILLE 200
    printf("TAILLE = %d\n", TAILLE);
    return 0;
}
```

## 24.4 Compilation conditionnelle

```c
// Compiler avec : gcc -std=c23 -DDEBUG conditionnelle.c -o conditionnelle   (sans -DDEBUG : pas de trace)
#include <stdio.h>

#ifndef VERSION
#define VERSION "1.0"
#endif

#if defined(_WIN32)
    #define SEPARATEUR '\\'
#elif defined(__linux__)
    #define SEPARATEUR '/'
#else
    #define SEPARATEUR '/'
#endif

int main(void) {
    int x = 42;
#ifdef DEBUG
    printf("Valeur : %d\n", x);
#endif
    printf("Version %s, séparateur '%c'\n", VERSION, SEPARATEUR);
#if __STDC_VERSION__ >= 202311L      // C23 ou plus récent
    puts("Compilé en C23 ou plus récent");
#else
    printf("Compilé avec __STDC_VERSION__ = %ldL\n", (long)__STDC_VERSION__);
#endif
    (void)x;
    return 0;
}
```

C23 ajoute `#elifdef` / `#elifndef`, `#warning` et `__has_include` :

```c
#include <stdio.h>

#if __has_include(<threads.h>)
#include <threads.h>
#define THREADS_OK 1
#endif

#warning "Section à revoir"          // avertissement personnalisé (C23) : affiché à la compilation

#if !defined(__linux__) && !defined(_WIN32) && !defined(__APPLE__)
#error "Plateforme non supportée"    // arrête la compilation : error: #error "Plateforme non supportée"
#endif

int main(void) {
#ifdef THREADS_OK
    puts("<threads.h> est disponible");
#else
    fprintf(stderr, "Erreur : <threads.h> n'est pas disponible\n");
#endif
    return 0;
}
```

Définir une macro à la compilation : `gcc -DDEBUG -DVERSION=\"2.0\" …`

## 24.5 Gardes d'inclusion

Évitent qu'un en-tête soit inclus plusieurs fois :

```c
// mon_entete.h
#ifndef MON_ENTETE_H
#define MON_ENTETE_H

int version(void);          // déclarations

// Alternative répandue (non standard mais supportée partout) : #pragma once
#endif
```

```c
// main.c
#include <stdio.h>
#include "mon_entete.h"
#include "mon_entete.h"     // deuxième inclusion : sans effet grâce aux gardes

int version(void) { return 3; }

int main(void) {
    printf("version = %d\n", version());
    return 0;
}
```

```bash
gcc main.c -o programme && ./programme
```

## 24.6 `#embed` *(C23)*

Inclut directement le contenu binaire d'un fichier dans un tableau :

```c
// Compiler avec : gcc -std=c23 embed.c -o embed   (nécessite GCC 15 ou Clang 19, et un fichier icone.png)
#include <stdio.h>

const unsigned char icone[] = {
    #embed "icone.png"
};

int main(void) {
    printf("icone.png : %zu octets, premier octet = 0x%02X\n", sizeof icone, icone[0]);
    return 0;
}
```

## 24.7 Macros prédéfinies

| Macro | Valeur |
| --- | --- |
| `__FILE__` | Nom du fichier source |
| `__LINE__` | Numéro de ligne courante |
| `__DATE__` / `__TIME__` | Date / heure de compilation |
| `__func__` | Nom de la fonction (variable prédéfinie C99) |
| `__STDC_VERSION__` | Version de la norme (`201710L` = C17, `202311L` = C23) |

## 24.8 Exemple : bascule de débogage

```c
// Compiler avec : gcc -DDEBUG debogage.c -o debogage   (sans -DDEBUG : aucune trace)
#include <stdio.h>

#ifdef DEBUG
    #define DBG(...) fprintf(stderr, __VA_ARGS__)
#else
    #define DBG(...) ((void)0)
#endif

int main(void) {
    int x = 42;
    DBG("x vaut %d\n", x);
    (void)x;
    printf("Fin du programme\n");
    return 0;
}
```

## 24.9 `static_assert` : vérifications à la compilation

```c
// Compiler avec : gcc -std=c23 assertion.c -o assertion
#include <stdio.h>

static_assert(sizeof(int) >= 4, "int doit faire au moins 32 bits");   // C23 : mot-clé ; C11 : _Static_assert
// static_assert(sizeof(int) >= 8, "int doit faire au moins 64 bits");
// error: static assertion failed: "int doit faire au moins 64 bits"

int main(void) {
    printf("sizeof(int) = %zu : la vérification a eu lieu à la compilation\n", sizeof(int));
    return 0;
}
```

---

# 25. Opérateurs bit à bit

## 25.1 Principe

Ils agissent sur les **bits** des entiers. Utilisez de préférence des types **non signés** (`unsigned`, `uint32_t`).

| Opérateur | Nom | Exemple (`a = 0b1100`, `b = 0b1010`) |
| --- | --- | --- |
| `&` | ET | `a & b` → `0b1000` |
| `\|` | OU | `a \| b` → `0b1110` |
| `^` | OU exclusif (XOR) | `a ^ b` → `0b0110` |
| `~` | NON (complément) | `~a` → bits inversés |
| `<<` | Décalage à gauche | `a << 1` → `0b11000` (×2) |
| `>>` | Décalage à droite | `a >> 1` → `0b0110` (÷2) |

## 25.2 Manipuler des bits individuels

```c
#include <stdio.h>

int main(void) {
    unsigned int x = 0b1010u;     // binaire C23 ; sinon 10u
    unsigned int n = 2;
    x |=  (1u << n);              // mettre le bit n à 1
    printf("après |= : %u\n", x);
    x &= ~(1u << n);              // mettre le bit n à 0
    printf("après &= : %u\n", x);
    x ^=  (1u << n);              // inverser le bit n
    printf("après ^= : %u\n", x);
    printf("bit %u : %u\n", n, (x >> n) & 1u);                 // lire le bit n
    printf("16 est une puissance de 2 : %d\n", (16u & (16u - 1)) == 0);   // x ≠ 0
    printf("x est impair : %u\n", x & 1u);                     // parité (1 = impair)
    return 0;
}
```

## 25.3 Drapeaux (*flags*) et masques

```c
#include <stdio.h>

enum { LECTURE = 1u << 0, ECRITURE = 1u << 1, EXEC = 1u << 2 };

int main(void) {
    unsigned int droits = LECTURE | ECRITURE;       // combiner
    if (droits & ECRITURE) puts("écriture autorisée");
    droits &= ~ECRITURE;                            // retirer
    if (!(droits & ECRITURE)) puts("écriture retirée");
    if (!(droits & EXEC)) puts("exécution jamais accordée");
    return 0;
}
```

## 25.4 Afficher en binaire

```c
#include <stdint.h>
#include <stdio.h>

void afficher_binaire(uint32_t n) {
    for (int i = 31; i >= 0; i--) {
        putchar(((n >> i) & 1u) ? '1' : '0');
        if (i % 8 == 0 && i) putchar(' ');
    }
    putchar('\n');
}

int main(void) {
    uint32_t n = 1000;
    afficher_binaire(n);
    // C23 : printf("%b\n", n);
    return 0;
}
```

## 25.5 Échange sans variable temporaire (curiosité)

```c
#include <stdio.h>

static void echanger_xor(int *a, int *b) {
    *a ^= *b; *b ^= *a; *a ^= *b;
}

int main(void) {
    int a = 3, b = 5;
    echanger_xor(&a, &b);
    printf("a = %d, b = %d\n", a, b);

    int x = 7;
    echanger_xor(&x, &x);        // Attention : échoue si a et b désignent la MÊME variable
    fprintf(stderr, "Erreur : echanger_xor(&x, &x) a mis x à %d (au lieu de 7)\n", x);
    return 0;
}
```

## 25.6 Fonctions de `<stdbit.h>` *(C23)*

```c
// Compiler avec : gcc -std=c23 stdbit.c -o stdbit   (nécessite <stdbit.h> : glibc 2.39+ ou équivalent)
#include <stdbit.h>
#include <stdio.h>

int main(void) {
    unsigned int x = 40u;        // 0b101000
    printf("bits à 1 : %u\n", stdc_count_ones(x));              // popcount
    printf("zéros de tête : %u\n", stdc_leading_zeros(x));
    printf("zéros de queue : %u\n", stdc_trailing_zeros(x));
    printf("largeur en bits : %u\n", stdc_bit_width(x));
    printf("puissance de 2 : %d\n", (int)stdc_has_single_bit(x));
    printf("64 puissance de 2 : %d\n", (int)stdc_has_single_bit(64u));
    return 0;
}
```

## 25.7 Précautions

- **Décaler d'un nombre de bits ≥ largeur du type**, ou négatif, est un comportement indéfini.
- **Décaler à gauche un entier signé** dans le bit de signe est indéfini : utilisez des types non signés.
- Le décalage à droite d'un **entier signé négatif** dépend de l'implémentation.
- Attention à la **priorité** : `x & 1 == 0` → écrire `(x & 1) == 0`.
- Attention à l'**endianness** (ordre des octets) lors d'échanges binaires.
- Écrivez `1u << n` (non signé) plutôt que `1 << n`.

---

# 26. Récursivité

## 26.1 Principe

Une fonction **récursive** s'appelle elle-même. Elle exige :

1. un **cas de base** (condition d'arrêt) ;
2. un **appel récursif** qui **se rapproche** du cas de base.

```c
#include <stdio.h>

unsigned long long factorielle(unsigned int n) {
    if (n <= 1) return 1;                    // cas de base
    return n * factorielle(n - 1);           // appel récursif
}

int main(void) {
    for (unsigned int n = 0; n <= 5; n++) printf("%u! = %llu\n", n, factorielle(n));
    return 0;
}
```

## 26.2 Fonctionnement : la pile d'appels

Chaque appel crée un **cadre de pile** (paramètres, variables locales, adresse de retour). Pour `factorielle(3)` :

```text
factorielle(3) → 3 * factorielle(2)
                       └─ 2 * factorielle(1)
                                └─ 1       (cas de base)
Remontée : 1 → 2 → 6
```

## 26.3 Exemples

```c
#include <stdio.h>

// Fibonacci (attention : exponentiel : très lent pour n grand)
int fib(int n) { return n < 2 ? n : fib(n - 1) + fib(n - 2); }

// PGCD (algorithme d'Euclide)
int pgcd(int a, int b) { return b == 0 ? a : pgcd(b, a % b); }

// Somme d'un tableau
int somme(const int *t, size_t n) { return n == 0 ? 0 : t[0] + somme(t + 1, n - 1); }

// Affichage d'un tableau à l'envers
void inverse(const int *t, size_t n) { if (n) { inverse(t + 1, n - 1); printf("%d ", t[0]); } }

// Recherche dichotomique
int dicho(const int *t, int bas, int haut, int x) {
    if (bas > haut) return -1;
    int m = bas + (haut - bas) / 2;          // évite le débordement de bas + haut
    if (t[m] == x) return m;
    return t[m] < x ? dicho(t, m + 1, haut, x) : dicho(t, bas, m - 1, x);
}

// Tours de Hanoï
void hanoi(int n, char de, char vers, char via) {
    if (n == 0) return;
    hanoi(n - 1, de, via, vers);
    printf("Disque %d : %c -> %c\n", n, de, vers);
    hanoi(n - 1, via, vers, de);
}

int main(void) {
    int t[] = {1, 3, 5, 7, 9, 11};
    size_t n = sizeof t / sizeof t[0];
    printf("fib(10) = %d\n", fib(10));
    printf("pgcd(48, 18) = %d\n", pgcd(48, 18));
    printf("somme = %d\n", somme(t, n));
    printf("à l'envers : "); inverse(t, n); putchar('\n');
    printf("dicho(7) = %d\n", dicho(t, 0, (int)n - 1, 7));
    if (dicho(t, 0, (int)n - 1, 4) == -1) fprintf(stderr, "Erreur : 4 est absent du tableau\n");
    hanoi(3, 'A', 'C', 'B');
    return 0;
}
```

## 26.4 Récursivité terminale

Si l'appel récursif est la **dernière opération**, certains compilateurs (avec `-O2`) le transforment en boucle. **Ce n'est pas garanti** par C.

```c
#include <stdio.h>

unsigned long long fact_acc(unsigned int n, unsigned long long acc) {
    return n <= 1 ? acc : fact_acc(n - 1, acc * n);
}

int main(void) {
    printf("fact_acc(10, 1) = %llu\n", fact_acc(10, 1));
    return 0;
}
```

## 26.5 Récursivité ou itération ?

| | Récursivité | Itération |
| --- | --- | --- |
| Lisibilité | Naturelle pour arbres, diviser pour régner | Plus verbeuse parfois |
| Mémoire | Consomme la **pile** (une trame par appel) | Constante |
| Vitesse | Surcoût des appels | Généralement plus rapide |
| Risque | **Dépassement de pile** (*stack overflow*) | — |

## 26.6 Pièges

- **Cas de base manquant ou inatteignable** → récursion infinie → plantage.
- **Profondeur excessive** (listes de millions d'éléments) → dépassement de pile : passez à une boucle.
- **Recalculs** (Fibonacci naïf) → utilisez la **mémoïsation** ou une boucle.
- Débordement des types entiers (`factorielle(25)` dépasse `unsigned long long`).

---

# 27. Unicode et caractères larges

## 27.1 Le problème

`char` est un **octet**, pas un caractère visible. En **UTF-8** (encodage standard actuel), un caractère occupe **1 à 4 octets** (`é` = 2 octets, `𝄞` = 4).

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    const char *s = "é";
    printf("strlen(\"%s\") = %zu\n", s, strlen(s));   // 2 (octets, pas 1 caractère)
    return 0;
}
```

## 27.2 Les approches

| Approche | Description | Remarques |
| --- | --- | --- |
| **UTF-8 dans des `char *`** (recommandé) | Chaînes ordinaires encodées en UTF-8 | Simple ; `strlen` compte des octets ; la plupart des fonctions `<string.h>` fonctionnent |
| **`wchar_t`** | Caractères « larges » (`L"…"`), `<wchar.h>` | Taille variable selon la plateforme (2 octets sous Windows, 4 sous Linux) ; peu portable |
| **`char16_t` / `char32_t`** | UTF-16 / UTF-32 (`u"…"`, `U"…"`), `<uchar.h>` | Largeur fixe |
| **`char8_t`** *(C23)* | Type dédié à l'UTF-8, littéraux `u8"…"` | |

```c
#include <locale.h>
#include <stdio.h>
#include <wchar.h>

int main(void) {
    setlocale(LC_ALL, "");                 // active la locale de l'utilisateur
    wchar_t *w = L"Bonjour é";
    if (wprintf(L"%ls\n", w) < 0) {
        fprintf(stderr, "Erreur : affichage impossible (locale sans UTF-8 ?)\n");
        return 1;
    }
    wprintf(L"%zu caractères larges\n", wcslen(w));
    return 0;
}
```

> **Attention** : Ne mélangez pas `printf` et `wprintf` sur le même flux.

## 27.3 Conseils pratiques

- Enregistrez vos fichiers source en **UTF-8**.
- Sous **Windows**, la console peut afficher des caractères illisibles : lancez `chcp 65001` ou utilisez Windows Terminal ; avec MSVC, ajoutez `/utf-8`.
- Pour une manipulation sérieuse (longueur en caractères, majuscules, normalisation, comparaison), utilisez une bibliothèque : **ICU**, **utf8proc** ou **libunistring**.
- Ne coupez jamais une chaîne UTF-8 au milieu d'un caractère multi-octets (les octets de continuation commencent par `10xxxxxx`).

---

# 28. Compilation et exécution

## 28.1 Les étapes détaillées

| Étape | Commande | Sortie |
| --- | --- | --- |
| **Préprocessing** | `gcc -E prog.c -o prog.i` | Code avec macros et inclusions développées |
| **Compilation** | `gcc -S prog.c -o prog.s` | Assembleur |
| **Assemblage** | `gcc -c prog.c -o prog.o` | Fichier objet (code machine non lié) |
| **Édition de liens** | `gcc prog.o -o prog` | Exécutable |
| **Tout en un** | `gcc prog.c -o prog` | Exécutable |

```bash
./prog           # exécuter (Linux/macOS)
prog.exe         # Windows
echo $?          # code de sortie
```

## 28.2 Options essentielles de `gcc` / `clang`

| Option | Rôle |
| --- | --- |
| `-o nom` | Nom de la sortie |
| `-std=c17` / `-std=c23` | Norme du langage |
| `-Wall -Wextra` | Active la plupart des **avertissements** |
| `-Wpedantic` | Respect strict de la norme |
| `-Werror` | Transforme les avertissements en erreurs |
| `-g` | Informations de **débogage** (pour `gdb`) |
| `-O0` / `-O2` / `-O3` / `-Os` | Optimisation (aucune / standard / agressive / taille) |
| `-I dossier` | Dossier supplémentaire d'en-têtes |
| `-L dossier -lnom` | Dossier de bibliothèques ; lier `libnom` (ex. `-lm` pour `<math.h>`) |
| `-D NOM=valeur` | Définit une macro |
| `-fsanitize=address,undefined` | **Détecteurs** d'erreurs mémoire et de comportements indéfinis |
| `-fanalyzer` | Analyse statique (GCC) |

**Commande de développement recommandée :**

```bash
gcc -std=c17 -Wall -Wextra -Wpedantic -g -fsanitize=address,undefined prog.c -o prog -lm
```

**Commande de production :**

```bash
gcc -std=c17 -Wall -Wextra -O2 prog.c -o prog -lm
```

## 28.3 Erreurs de compilation et d'édition de liens

| Message | Cause probable |
| --- | --- |
| `error: expected ';' before …` | Point-virgule manquant |
| `implicit declaration of function` | Fonction sans prototype / `#include` oublié |
| `undeclared identifier` | Variable non déclarée |
| `warning: format '%d' expects …` | Mauvais spécificateur `printf` |
| `undefined reference to 'f'` | **Édition de liens** : fonction non définie / fichier ou `-l` oublié |
| `multiple definition of` | Même fonction définie dans plusieurs fichiers (définition dans un `.h` ?) |

> **Bonne pratique** : Traitez les **avertissements comme des erreurs** : ils révèlent souvent de vrais bugs.

## 28.4 Projets multi-fichiers

```bash
gcc -c main.c -o main.o
gcc -c maths.c -o maths.o
gcc main.o maths.o -o programme        # lier

# ou directement
gcc main.c maths.c -o programme
```

La compilation séparée ne recompile que ce qui a changé (rôle de `make`).

## 28.5 Automatiser avec `make`

```makefile
CC      = gcc
CFLAGS  = -std=c17 -Wall -Wextra -g
OBJ     = main.o maths.o

programme: $(OBJ)
	$(CC) $(OBJ) -o $@ -lm

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) programme

.PHONY: clean
```

(Les lignes de commande commencent par une **tabulation**.) Pour des projets plus vastes ou multiplateformes : **CMake**, **Meson**, **Ninja**.

## 28.6 Bibliothèques

```bash
# Bibliothèque statique (.a) : copiée dans l'exécutable
gcc -c util.c -o util.o
ar rcs libutil.a util.o
gcc main.c -L. -lutil -o prog

# Bibliothèque dynamique (.so / .dll / .dylib) : chargée à l'exécution
gcc -fPIC -shared util.c -o libutil.so
gcc main.c -L. -lutil -o prog
LD_LIBRARY_PATH=. ./prog
```

## 28.7 Débogage

### `gdb`

```bash
gcc -g prog.c -o prog
gdb ./prog
```

| Commande `gdb` | Rôle |
| --- | --- |
| `break main` / `b ligne` | Point d'arrêt |
| `run` / `r` | Lancer |
| `next` / `n` | Ligne suivante |
| `step` / `s` | Entrer dans la fonction |
| `print x` / `p x` | Afficher une variable |
| `backtrace` / `bt` | Pile d'appels |
| `continue` / `c` | Reprendre |
| `watch x` | Surveiller une variable |
| `quit` | Quitter |

Alternatives : **lldb** (macOS/LLVM), débogueurs intégrés à VS Code / CLion.

### Détecteurs d'erreurs

| Outil | Détecte |
| --- | --- |
| **AddressSanitizer** (`-fsanitize=address`) | Dépassements de tampon, use-after-free, fuites |
| **UBSan** (`-fsanitize=undefined`) | Débordements d'entiers, décalages invalides, déréférencement nul… |
| **Valgrind** (`valgrind --leak-check=full ./prog`) | Fuites et accès mémoire invalides (Linux) |
| **`-fanalyzer`**, **clang-tidy**, **cppcheck** | Analyse statique |

## 28.8 Optimisation

| Niveau | Effet |
| --- | --- |
| `-O0` | Aucune optimisation (débogage) |
| `-O1` / `-O2` | Optimisations courantes (**`-O2`** recommandé en production) |
| `-O3` | Agressive (code plus gros) |
| `-Os` | Optimise la taille |
| `-march=native` | Instructions spécifiques au processeur local (non portable) |
| `-flto` | Optimisation à l'édition de liens |

> **Attention** : Le code avec comportement indéfini peut se comporter différemment selon le niveau d'optimisation.

## 28.9 Compilation croisée

Compiler pour une autre architecture (ARM, microcontrôleurs…) :

```bash
arm-linux-gnueabihf-gcc prog.c -o prog_arm
```

## 28.10 Environnement d'exécution

1. Le système **charge** l'exécutable en mémoire.
2. Il initialise la pile, le tas et les flux standard (`stdin`, `stdout`, `stderr`).
3. Le code de démarrage (*crt0*) appelle **`main`**.
4. À la fin de `main` (ou à l'appel de `exit()`), les fichiers sont fermés, les fonctions `atexit` exécutées, puis le **code de sortie** est transmis au système.

```c
#include <stdio.h>
#include <stdlib.h>

void nettoyer(void) {
    puts("nettoyer() : fonction exécutée à la sortie");
}

int main(void) {
    atexit(nettoyer);          // enregistre une fonction exécutée à la sortie
    FILE *f = fopen("fichier_absent.txt", "r");
    if (!f) {
        fprintf(stderr, "Erreur : fichier introuvable, arrêt du programme\n");
        exit(EXIT_FAILURE);    // quitte immédiatement (depuis n'importe quelle fonction)
    }
    fclose(f);
    // abort();                // arrêt anormal : aucun nettoyage, signal SIGABRT
    return 0;
}
```

### Appels système ou fonctions de bibliothèque ?

| | Fonctions de la bibliothèque C | Appels système |
| --- | --- | --- |
| Exemples | `printf`, `fopen`, `malloc` | `write`, `open`, `brk`/`mmap` |
| Portabilité | Standard C | Dépend du système (POSIX, Windows API) |
| Rôle | Couche confortable et **tamponnée** | Interface directe avec le noyau |

---

# 29. Comportements indéfinis et sécurité

*(Section ajoutée : c'est la clé pour écrire du C fiable.)*

## 29.1 Comportement indéfini (UB)

Quand un programme viole une règle du langage, **la norme n'impose aucun résultat** : plantage, résultat faux, **ou apparente normalité** (avant de casser avec un autre compilateur ou niveau d'optimisation). Le compilateur peut **supposer que l'UB n'arrive jamais** et optimiser en conséquence.

| Catégorie | Exemples |
| --- | --- |
| **Mémoire** | Accès hors bornes, déréférencement de `NULL`, use-after-free, double free, variable non initialisée lue |
| **Arithmétique** | Débordement d'entier **signé**, division par zéro, décalage invalide |
| **Pointeurs** | Arithmétique hors d'un objet, violation d'alias strict, alignement incorrect |
| **Appels** | Mauvais format dans `printf`, mauvais nombre/type d'arguments variadiques |
| **Séquencement** | `i = i++ + ++i;` (modifications non séquencées) |
| **Chaînes** | Modifier un littéral de chaîne, oublier le `'\0'` |

## 29.2 Les failles de sécurité typiques

| Faille | Cause | Parade |
| --- | --- | --- |
| **Dépassement de tampon** | `gets`, `strcpy`, `scanf("%s")`, indices non vérifiés | `fgets`, `snprintf`, bornes vérifiées |
| **Chaîne de format** | `printf(saisie_utilisateur)` | `printf("%s", saisie)` |
| **Dépassement d'entier** avant allocation | `malloc(n * taille)` avec `n` énorme | `calloc`, `ckd_mul` (C23), vérification explicite |
| **Use-after-free / double free** | Gestion de propriété floue | `ptr = NULL` après `free`, conventions de propriété, sanitizers |
| **Lecture de mémoire non initialisée** | Variable locale non initialisée | Initialiser, `-Wall`, MemorySanitizer |

## 29.3 Hygiène de programmation

- Compilez avec `-Wall -Wextra -Wpedantic` et corrigez **tous** les avertissements.
- Développez avec **AddressSanitizer + UBSan** activés ; testez aussi avec **Valgrind**.
- **Validez toutes les entrées** (taille, plage, format) et toutes les valeurs de retour.
- Passez **toujours la taille** avec un pointeur de tampon (`ptr, taille`).
- Initialisez variables et pointeurs ; mettez à `NULL` après `free`.
- Utilisez `const`, `size_t`, types à taille fixe.
- Réduisez la portée ; évitez les variables globales.
- Relisez le code (revue), utilisez des analyseurs statiques (`clang-tidy`, `cppcheck`, `-fanalyzer`) et des tests automatisés (CUnit, Unity, Criterion, ou `assert`).
- Pour du code critique, appliquez des règles reconnues : **CERT C**, **MISRA C**.

```c
#include <assert.h>
#include <stdio.h>

int main(void) {
    int x = 5;
    int *ptr = &x;
    int *vide = NULL;

    assert(ptr != NULL);        // vérification de développement (désactivée avec -DNDEBUG)
    printf("*ptr = %d\n", *ptr);

    fprintf(stderr, "Le prochain assert échoue et affiche l'erreur :\n");
    assert(vide != NULL);       // échec : message sur stderr puis arrêt du programme (SIGABRT)
    printf("jamais affiché\n");
    return 0;
}
```

---

# 30. Bibliothèque standard et aide-mémoire

## 30.1 En-têtes principaux

| En-tête | Contenu |
| --- | --- |
| `<stdio.h>` | Entrées/sorties : `printf`, `scanf`, `fopen`, `fgets`… |
| `<stdlib.h>` | `malloc`, `free`, `rand`, `qsort`, `exit`, `strtol`, `getenv` |
| `<string.h>` | `strlen`, `strcmp`, `memcpy`, `memset`… |
| `<ctype.h>` | `isalpha`, `toupper`… |
| `<math.h>` | `sqrt`, `pow`, `sin`, `floor`… (lier avec `-lm`) |
| `<stdint.h>` / `<inttypes.h>` | Entiers de taille fixe et macros d'affichage |
| `<stdbool.h>` | `bool`, `true`, `false` (inutile en C23) |
| `<stddef.h>` | `size_t`, `NULL`, `ptrdiff_t`, `offsetof` |
| `<limits.h>` / `<float.h>` | Limites des types |
| `<errno.h>` | Codes d'erreur (`errno`) |
| `<time.h>` | `time`, `clock`, `strftime`, `difftime` |
| `<assert.h>` | `assert`, `static_assert` |
| `<stdarg.h>` | Fonctions variadiques |
| `<signal.h>` / `<setjmp.h>` | Signaux, sauts non locaux |
| `<threads.h>` / `<stdatomic.h>` | Fils d'exécution et opérations atomiques (C11, support variable ; **POSIX threads** `<pthread.h>` très répandu) |
| `<stdbit.h>` / `<stdckdint.h>` | Manipulation de bits, arithmétique vérifiée (C23) |

### Nombres aléatoires

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    srand((unsigned)time(NULL));        // initialiser la graine UNE seule fois
    for (int i = 0; i < 5; i++) {
        int de = rand() % 6 + 1;        // 1 à 6 (qualité médiocre ; pas pour la cryptographie)
        printf("lancer %d : %d\n", i + 1, de);
    }
    return 0;
}
```

## 30.2 Récapitulatif par thème

| Besoin | Outil |
| --- | --- |
| Tableau de taille fixe | `int t[N];` |
| Tableau de taille variable | `malloc` / `calloc` / `realloc` |
| Chaîne sûre | `snprintf`, `fgets`, `strlen` (+ taille du tampon) |
| Lire un nombre | `fgets` + `strtol` / `strtod` |
| Entier portable | `int32_t`, `uint64_t`, `size_t` |
| Modifier un argument | Passer un **pointeur** |
| Retourner une valeur d'erreur + résultat | Code de retour + pointeur de sortie |
| Callback | Pointeur de fonction |
| Variante (type somme) | `struct` + `enum` + `union` |
| Constante | `constexpr` (C23) / `enum` / `const` |
| Tri | `qsort` |
| Nettoyage en cas d'erreur | `goto fin;` |

## 30.3 Les 12 règles d'or du C

1. **Initialisez** tout.
2. **Vérifiez** chaque valeur de retour (`malloc`, `fopen`, `scanf`…).
3. **Jamais** `gets` ; limitez toujours les copies et lectures de chaînes.
4. **Libérez** ce que vous allouez, **une seule fois**.
5. **Ne dépassez jamais** les bornes d'un tableau.
6. **Ne retournez jamais** l'adresse d'une variable locale.
7. **Parenthésez** macros et expressions ambiguës.
8. **Évitez** les comportements indéfinis (débordement signé, aliasing, non-séquencement).
9. Utilisez `const`, `static` et les types adaptés (`size_t`, `uint8_t`…).
10. Compilez avec **tous les avertissements** et les **sanitizers**.
11. **Découpez** en petites fonctions et en modules (`.h` / `.c`).
12. **Documentez** qui possède la mémoire et quelles sont les préconditions.

## 30.4 Ressources pour progresser

- **cppreference (C)** : <https://en.cppreference.com/w/c>
- *Le langage C* — Kernighan & Ritchie (*The C Programming Language*, 2ᵉ éd.)
- *Modern C* — Jens Gustedt (gratuit en ligne)
- **SEI CERT C Coding Standard** : <https://wiki.sei.cmu.edu/confluence/display/c>
- **Compiler Explorer** : <https://godbolt.org>
- **Brouillons de la norme (WG14)** : <https://www.open-std.org/jtc1/sc22/wg14/>

---

<div align="center">

*Bon code, et que vos pointeurs soient toujours valides !*

</div>
