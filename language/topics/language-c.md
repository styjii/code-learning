<div align="center">

# ⚙️ Langage C — Guide complet

**Des premiers programmes à la gestion de la mémoire, aux fichiers et à la compilation**

*Mis à jour pour C17 / C23 (octobre 2026)*

</div>

---

## 🧰 Ressources

| Ressource | Lien |
| --- | --- |
| 📝 Exercices | [exercises](/language/exercises/c) |
| ✅ Solutions | [solutions](/language/solutions/c) |
| 🚀 Projets | [projects](/language/projects/c) |
| 📘 Référence | [cppreference.com (C)](https://en.cppreference.com/w/c) |
| 📜 Normes | [ISO/IEC 9899 (C23)](https://www.iso.org/standard/82075.html) · [Brouillons WG14](https://www.open-std.org/jtc1/sc22/wg14/) |

---

## 🗂️ Sommaire

**🟢 Niveau débutant**

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

**🟡 Niveau intermédiaire**

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

**🔴 Niveau avancé**

22. [Gestion des fichiers](#22-gestion-des-fichiers)
23. [Arguments de la ligne de commande](#23-arguments-de-la-ligne-de-commande)
24. [Directives du préprocesseur](#24-directives-du-préprocesseur)
25. [Opérateurs bit à bit](#25-opérateurs-bit-à-bit)
26. [Récursivité](#26-récursivité)
27. [Unicode et caractères larges](#27-unicode-et-caractères-larges)
28. [Compilation et exécution](#28-compilation-et-exécution)
29. [Comportements indéfinis et sécurité](#29-comportements-indéfinis-et-sécurité)
30. [Bibliothèque standard et aide-mémoire](#30-bibliothèque-standard-et-aide-mémoire)

> 💡 **Légende** : *(ajout)* = notion absente du guide d'origine ; *(à jour)* = pratique moderne remplaçant une ancienne ; *(C23)* = nouveauté de la norme de 2023.

---

# 🟢 Niveau débutant

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

> ⚠️ Revers de la médaille : le C **ne vous protège pas** (dépassements de tampon, pointeurs invalides…). Une bonne discipline et des outils d'analyse sont indispensables (voir [section 29](#29-comportements-indéfinis-et-sécurité)).

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

> 💡 Éditeurs et IDE : **VS Code** (extension C/C++), **CLion**, **Code::Blocks**, **Vim/Neovim**. Atelier en ligne : [Compiler Explorer](https://godbolt.org), [OnlineGDB](https://www.onlinegdb.com).

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

> ℹ️ Depuis **C99**, si `main` n'a pas de `return`, elle retourne **implicitement 0**. On l'écrit quand même par clarté.
> ℹ️ `int main(void)` est préférable à `int main()` : en C (avant C23), `()` signifie « arguments non spécifiés ». En **C23**, `()` équivaut à `(void)`.

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
// Commentaire sur une ligne (C99)

/* Commentaire
   sur plusieurs lignes (ne s'imbrique pas) */
```

## 2.4 Variables et instructions

```c
int age;                     // déclaration
age = 25;                    // affectation
int taille = 180;            // déclaration + initialisation
```

> ✅ Depuis **C99**, on peut déclarer une variable **n'importe où** dans un bloc (et dans l'en-tête d'un `for`), au plus près de son usage. Il n'est plus nécessaire de tout déclarer en début de fonction.

## 2.5 Code de sortie

```c
return 0;            // ou EXIT_SUCCESS (de <stdlib.h>)
return EXIT_FAILURE; // erreur
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
int age_utilisateur;     // ✅ snake_case (convention courante en C)
int _temp;               // ✅ (mais _x réservé dans certains contextes : évitez)
// int 2eme;             // ❌ commence par un chiffre
// int for;              // ❌ mot-clé
```

> ⚠️ Évitez les noms commençant par `_` suivi d'une majuscule ou par `__` : **réservés à l'implémentation**. Les noms en `_t` sont réservés par POSIX.

## 3.3 Mots-clés du langage *(à jour : C23)*

| Catégorie | Mots-clés |
| --- | --- |
| **Types** | `int` `char` `short` `long` `float` `double` `void` `signed` `unsigned` `bool` *(C23)* `_Complex` `_BitInt` *(C23)* |
| **Qualificateurs** | `const` `volatile` `restrict` `_Atomic` |
| **Classes de stockage** | `auto` `register` `static` `extern` `thread_local` *(C23)* `constexpr` *(C23)* |
| **Types composés** | `struct` `union` `enum` `typedef` |
| **Contrôle** | `if` `else` `switch` `case` `default` `for` `while` `do` `break` `continue` `goto` `return` |
| **Divers** | `sizeof` `inline` `alignas` `alignof` `static_assert` `typeof` `typeof_unqual` `true` `false` `nullptr` *(C23)* `_Generic` `_Noreturn` |

> 📌 En **C23**, `bool`, `true`, `false`, `nullptr`, `alignas`, `alignof`, `static_assert`, `thread_local` deviennent de vrais **mots-clés** (plus besoin de `<stdbool.h>` ni des anciennes formes `_Bool`, `_Alignas`, `_Static_assert`…). Dans un code destiné aux anciennes normes, incluez `<stdbool.h>`.

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
[[nodiscard]] int ouvrir(const char *chemin);      // avertit si le résultat est ignoré
[[maybe_unused]] static int experimental = 0;
[[deprecated("Utiliser nouvelle_fonction")]] void ancienne(void);
switch (x) { case 1: faire(); [[fallthrough]]; case 2: autre(); }
[[noreturn]] void arreter(void);
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

> ✅ `sizeof` renvoie un `size_t` : affichez-le avec **`%zu`**.

## 4.2 Modificateurs : `signed`, `unsigned`, `short`, `long`

```c
unsigned int positif = 4000000000u;
signed char petit = -100;
unsigned long long enorme = 18446744073709551615ULL;
```

| Type non signé | Plage (32 bits) |
| --- | --- |
| `unsigned int` | 0 à 4 294 967 295 |
| `int` | −2 147 483 648 à 2 147 483 647 |

> ⚠️ Le débordement d'un entier **signé** est un **comportement indéfini** ; celui d'un entier **non signé** « boucle » (modulo 2ⁿ).
> ⚠️ `char` peut être signé **ou** non selon la plateforme : utilisez `unsigned char` pour des octets.

## 4.3 Entiers à taille fixe : `<stdint.h>` *(ajout, à jour)*

Pour du code **portable** et prévisible, préférez ces types :

```c
#include <stdint.h>
#include <inttypes.h>      // macros d'affichage

int8_t   a;   uint8_t  b;     // 8 bits
int16_t  c;   uint16_t d;     // 16 bits
int32_t  e;   uint32_t f;     // 32 bits
int64_t  g;   uint64_t h;     // 64 bits
size_t   taille;              // taille d'objets / indices de tableaux (<stddef.h>)
intptr_t p;                   // entier pouvant contenir un pointeur

printf("%" PRId64 "\n", g);   // affichage portable d'un int64_t
printf("%zu\n", taille);      // affichage d'un size_t
```

## 4.4 Booléens

```c
// C23 : natif
bool actif = true;

// C99 à C17 : 
#include <stdbool.h>
bool ok = false;
```

En C, toute valeur **non nulle** est « vraie » ; `0` est « faux ».

## 4.5 Déclarer, initialiser, affecter

```c
int a;                      // ⚠️ valeur indéterminée (locale)
int b = 10;                 // initialisée
int x = 1, y = 2, z;        // plusieurs
const double PI = 3.14159;  // constante
int n = {0};                // initialisation par accolades
int m = {};                 // initialisation à zéro (C23)
```

> ⚠️ Les variables **locales non initialisées** contiennent des valeurs aléatoires ; les variables **globales / statiques** sont initialisées à 0 par défaut.

### Inférence de type avec `auto` *(C23)*

```c
auto compteur = 0;          // type déduit : int
auto ratio = 3.14;          // double
```

Utile avec `typeof` : `typeof(expr) copie = expr;`.

## 4.6 Conversions de types (*casts*)

```c
int a = 5, b = 2;
float r1 = a / b;            // 2.0  😬 division entière d'abord
float r2 = (float)a / b;     // 2.5  ✅ conversion explicite
int  n  = (int)3.99;         // 3 (troncature)
char c  = 'A' + 1;           // 'B'
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
| `constexpr` *(C23)* | `constexpr int taille = 100;` | Vraie **constante de compilation**, typée ✅ |

```c
#define PI 3.14159                    // sans point-virgule !
const double TVA = 0.2;
constexpr int MAX_ELEVES = 30;        // C23
int notes[MAX_ELEVES];
```

> ✅ Préférez `const` / `constexpr` / `enum` à `#define` pour les constantes : ils sont **typés**, respectent la portée et facilitent le débogage.
> ⚠️ En C (avant C23), `const int n = 5; int t[n];` crée un VLA, pas un tableau de taille constante.

## 5.3 `const` et pointeurs

```c
const int *p1;          // pointeur vers un int CONSTANT (on ne modifie pas *p1)
int *const p2 = &x;     // pointeur CONSTANT (on ne change pas p2)
const int *const p3 = &x;   // les deux
```

Astuce de lecture : lisez la déclaration **de droite à gauche**.

## 5.4 Constantes prédéfinies utiles

```c
INT_MAX, INT_MIN, UINT_MAX      // <limits.h>
DBL_MAX, DBL_EPSILON            // <float.h>
EXIT_SUCCESS, EXIT_FAILURE      // <stdlib.h>
NULL / nullptr, EOF, RAND_MAX   // <stddef.h>, <stdio.h>, <stdlib.h>
__FILE__, __LINE__, __func__    // nom du fichier, ligne, fonction
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
int a = 7, b = 2;
a / b;        // 3 (division entière)
a % b;        // 1 (reste ; uniquement pour les entiers)
(double)a / b;  // 3.5
```

## 6.2 Incrémentation : préfixe et suffixe

```c
int i = 5;
int a = i++;    // a = 5, puis i = 6  (post-incrément)
int b = ++i;    // i = 7, puis b = 7  (pré-incrément)
```

## 6.3 Opérateurs logiques et évaluation paresseuse

```c
if (p != NULL && p->valeur > 0) { /* … */ }   // p->valeur évalué seulement si p != NULL
```

`&&` et `||` s'arrêtent dès que le résultat est connu (*court-circuit*). Le résultat d'une comparaison est `1` (vrai) ou `0` (faux).

## 6.4 Ternaire

```c
int max = (a > b) ? a : b;
```

## 6.5 `sizeof` et opérateur virgule

```c
size_t n = sizeof(int);              // taille d'un type
size_t t = sizeof tableau / sizeof tableau[0];   // nombre d'éléments d'un tableau (pas d'un pointeur !)
int x = (a = 1, a + 2);              // virgule : évalue de gauche à droite, résultat = dernier
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

> ⚠️ Piège : `x & 1 == 0` s'évalue comme `x & (1 == 0)`. **Ajoutez des parenthèses** : `(x & 1) == 0`.

## 6.7 Comportements à éviter

```c
int i = 0;
tab[i] = i++;            // ❌ comportement indéfini : modification et lecture non séquencées
int x = INT_MAX + 1;     // ❌ débordement d'entier signé : indéfini
int d = 1 << 40;         // ❌ décalage trop grand : indéfini
int z = a / 0;           // ❌ division par zéro : indéfini
```

## 6.8 Arithmétique vérifiée *(C23)*

`<stdckdint.h>` détecte les débordements sans comportement indéfini :

```c
#include <stdckdint.h>
int resultat;
if (ckd_add(&resultat, a, b)) {
    fprintf(stderr, "Débordement !\n");
}
// aussi : ckd_sub, ckd_mul
```

---

# 7. Entrées et sorties

## 7.1 Affichage : `printf` et `puts`

```c
#include <stdio.h>

printf("Bonjour\n");
printf("Nom : %s, âge : %d, taille : %.2f m\n", nom, age, taille);
puts("Texte avec saut de ligne automatique");
putchar('A');
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
printf("[%5d]\n", 42);      // [   42]
printf("[%-5d]\n", 42);     // [42   ]
printf("[%05d]\n", 42);     // [00042]
printf("[%8.3f]\n", 3.14159);   // [   3.142]
printf("[%.*s]\n", 3, "Bonjour");   // [Bon]
```

> ⚠️ Le format **doit correspondre** au type de l'argument : `printf("%d", 3.5)` est un comportement indéfini. **Ne passez jamais une chaîne non maîtrisée comme format** (`printf(saisie)` → utiliser `printf("%s", saisie)`).

## 7.2 Lecture : `scanf`

```c
int age;
double taille;
char initiale;

scanf("%d", &age);               // ⚠️ & obligatoire pour les nombres
scanf("%lf", &taille);           // %lf pour double (≠ printf)
scanf(" %c", &initiale);         // l'espace avant %c ignore les blancs/sauts de ligne

char mot[50];
scanf("%49s", mot);              // ✅ largeur limitée (taille − 1) ; pas de & pour un tableau
```

- `scanf` **renvoie le nombre de valeurs lues** : vérifiez-le.
- `%s` s'arrête au premier espace.

```c
if (scanf("%d", &age) != 1) {
    fprintf(stderr, "Entrée invalide\n");
    return EXIT_FAILURE;
}
```

## 7.3 Lire une ligne : `fgets` *(à jour)*

```c
char nom[50];
if (fgets(nom, sizeof nom, stdin) != NULL) {
    nom[strcspn(nom, "\n")] = '\0';        // supprime le '\n' final (nécessite <string.h>)
}
```

> 🚫 **`gets()` est dangereuse et a été SUPPRIMÉE du langage (C11)** : elle ne limite pas la taille lue (dépassement de tampon). N'utilisez **jamais** `gets` ; employez `fgets` (ou `getline` sous POSIX).

### Lecture sûre d'un nombre

```c
char ligne[64];
if (fgets(ligne, sizeof ligne, stdin)) {
    char *fin;
    long n = strtol(ligne, &fin, 10);      // plus fiable que atoi
    if (fin == ligne) puts("Pas un nombre");
}
```

### Vider le tampon d'entrée

Après `scanf`, il reste souvent un `\n` qui perturbe un `fgets`/`getchar` suivant :

```c
int c;
while ((c = getchar()) != '\n' && c != EOF) { }
```

> ⚠️ N'utilisez pas `fflush(stdin)` : comportement indéfini en C standard.

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
char tampon[32];
snprintf(tampon, sizeof tampon, "Score : %d", 42);
fprintf(stderr, "Erreur : %s\n", "fichier introuvable");
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
if (note >= 16) {
    puts("Très bien");
} else if (note >= 10) {
    puts("Passable");
} else {
    puts("Insuffisant");
}
```

> ✅ Utilisez toujours des **accolades**, même pour une seule instruction (évite des bugs classiques).

## 8.2 `switch`

Choix selon une valeur **entière ou caractère** (pas de chaînes ni de flottants) :

```c
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
```

En C23, on marque une cascade volontaire avec `[[fallthrough]];`.

## 8.3 Boucles

```c
for (int i = 0; i < 5; i++) {        // nombre d'itérations connu
    printf("%d ", i);
}

int n = 0;
while (n < 5) {                       // condition testée AVANT
    n++;
}

do {                                  // exécutée AU MOINS une fois
    n--;
} while (n > 0);
```

| Boucle | Quand l'utiliser |
| --- | --- |
| `for` | Compteur / nombre d'itérations connu |
| `while` | Tant qu'une condition est vraie |
| `do…while` | Au moins une exécution (ex. menu, validation de saisie) |

### Boucle infinie

```c
for (;;) { /* … avec break pour sortir */ }
while (1) { /* … */ }
```

## 8.4 `break`, `continue`, `goto`

```c
for (int i = 0; i < 10; i++) {
    if (i == 3) continue;     // passe à l'itération suivante
    if (i == 7) break;        // quitte la boucle
}
```

`goto` saute vers une étiquette. À **éviter**, sauf pour un usage classique et légitime : **le nettoyage centralisé en cas d'erreur** :

```c
int traiter(void) {
    int code = -1;
    FILE *f = fopen("a.txt", "r");
    if (!f) goto fin;
    char *tampon = malloc(100);
    if (!tampon) goto ferme;
    /* … travail … */
    code = 0;
    free(tampon);
ferme:
    fclose(f);
fin:
    return code;
}
```

## 8.5 Boucles imbriquées

```c
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= i; j++) putchar('*');
    putchar('\n');
}
```

## 8.6 Pièges classiques

```c
if (x = 5) { }          // ❌ affectation (toujours vrai) : écrire x == 5
for (int i = 0; i < 10; i++); { }   // ❌ ; vide après le for
while (i < 10) { }                   // ❌ i jamais modifié : boucle infinie
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
void afficher(void) { puts("Salut"); }          // aucun paramètre, aucun retour
static inline int carre(int x) { return x * x; }   // fonction locale au fichier, candidate à l'inlining
```

> ⚠️ Écrivez `f(void)` pour « aucun paramètre » (avant C23, `f()` signifie « paramètres non spécifiés »).

## 9.2 Passage des arguments : toujours **par valeur**

C copie les arguments : la fonction travaille sur des **copies**.

```c
void echanger_rate(int a, int b) { int t = a; a = b; b = t; }   // ❌ ne modifie pas l'appelant

void echanger(int *a, int *b) {                                  // ✅ on passe des ADRESSES
    int t = *a; *a = *b; *b = t;
}

int x = 1, y = 2;
echanger(&x, &y);       // x = 2, y = 1
```

- Passer un **pointeur** permet à la fonction de **modifier** la valeur d'origine ou de renvoyer plusieurs résultats.
- Les **tableaux** sont passés comme un **pointeur vers leur premier élément** : joignez toujours leur taille.

```c
double moyenne(const int tab[], size_t n) {     // const : la fonction ne modifie pas le tableau
    double s = 0;
    for (size_t i = 0; i < n; i++) s += tab[i];
    return n ? s / n : 0;
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

int somme(int n, ...) {
    va_list args;
    va_start(args, n);
    int total = 0;
    for (int i = 0; i < n; i++) total += va_arg(args, int);
    va_end(args);
    return total;
}
somme(3, 10, 20, 30);    // 60
```

⚠️ Aucun contrôle de type : une erreur sur les arguments est un comportement indéfini.

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
int global = 10;                  // portée fichier

void f(void) {
    int local = 5;                // portée bloc
    {
        int interne = 1;
        int global = 99;          // masque (ombre) la variable globale
    }
}
```

## 10.2 Classes de stockage et durée de vie

| Classe | Durée de vie | Portée / liaison | Initialisation par défaut |
| --- | --- | --- | --- |
| **`auto`** (par défaut en bloc) | Jusqu'à la fin du bloc | Bloc | ⚠️ **Indéterminée** |
| **`static`** (dans une fonction) | **Tout le programme** | Bloc | 0 |
| **`static`** (au niveau fichier) | Tout le programme | **Fichier** (invisible aux autres fichiers) | 0 |
| **`extern`** | Tout le programme | Définie ailleurs | — |
| **`register`** | Bloc | Bloc | Indéterminée (conseil obsolète au compilateur) |
| **`thread_local`** *(C23 ; `_Thread_local` avant)* | Durée du fil d'exécution | | 0 |

```c
void compter(void) {
    static int appels = 0;      // initialisée UNE fois, conservée entre les appels
    appels++;
    printf("Appel n°%d\n", appels);
}
```

```c
// fichier a.c
int compteur = 0;               // définition (visible par les autres fichiers)
static int prive = 1;           // visible seulement dans a.c

// fichier b.c
extern int compteur;            // déclaration : « définie ailleurs »
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

# 🟡 Niveau intermédiaire

---

# 11. Tableaux

## 11.1 Déclarer et initialiser

Un **tableau** stocke plusieurs éléments **de même type**, **contigus en mémoire**. Les indices commencent à **0**.

```c
int notes[5];                           // 5 entiers non initialisés (locaux)
int a[5] = {10, 20, 30, 40, 50};        // initialisation complète
int b[5] = {1, 2};                      // le reste est mis à 0 → {1, 2, 0, 0, 0}
int c[] = {7, 8, 9};                    // taille déduite : 3
int d[100] = {0};                       // tout à zéro
int e[100] = {};                        // idem (C23)
int f[6] = { [2] = 5, [5] = 9 };        // initialisation désignée (C99)
```

```c
a[0] = 11;
printf("%d\n", a[2]);
size_t n = sizeof a / sizeof a[0];      // nombre d'éléments (5)
```

> 🔥 **C ne vérifie jamais les bornes.** `a[10]` sur un tableau de 5 éléments est un **comportement indéfini** (corruption mémoire, plantage, faille de sécurité).

## 11.2 Parcourir

```c
for (size_t i = 0; i < n; i++) {
    printf("a[%zu] = %d\n", i, a[i]);
}
```

## 11.3 Tableaux multidimensionnels

```c
int matrice[2][3] = { {1, 2, 3}, {4, 5, 6} };

for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) printf("%d ", matrice[i][j]);
    putchar('\n');
}
```

Stockage **ligne par ligne** (*row-major*). Pour une fonction : `void afficher(int m[][3], int lignes)` (toutes les dimensions sauf la première doivent être précisées).

## 11.4 Tableaux à taille variable (VLA)

```c
int n = lire_taille();
int t[n];                  // VLA : taille connue seulement à l'exécution (C99)
```

> ⚠️ Les VLA sont **optionnels depuis C11**, allouent sur la **pile** (risque de dépassement) et sont **interdits par certains compilateurs / guides de sécurité**. Pour des tailles variables, préférez **`malloc`** (section 14).

## 11.5 Tableaux et fonctions

Un tableau « se dégrade » (*decay*) en **pointeur vers son premier élément** lorsqu'il est passé à une fonction : `sizeof` y donne la taille d'un **pointeur**, pas du tableau.

```c
void remplir(int *tab, size_t n) {    // équivalent à int tab[]
    for (size_t i = 0; i < n; i++) tab[i] = (int)i * 2;
}

int resultats[10];
remplir(resultats, 10);               // toujours passer la taille
```

## 11.6 Opérations courantes

```c
#include <string.h>

int copie[5];
memcpy(copie, a, sizeof a);                  // copier (zones qui ne se chevauchent pas)
memmove(a + 1, a, 4 * sizeof a[0]);          // copier avec chevauchement possible
memset(copie, 0, sizeof copie);              // remplir d'octets (0 pour les entiers)
int egaux = memcmp(a, copie, sizeof a) == 0; // comparer
```

> ⚠️ On ne peut pas copier ou comparer deux tableaux avec `=` ou `==` : cela compare/affecte des **adresses**.

### Tri avec `qsort`

```c
int comparer(const void *x, const void *y) {
    int a = *(const int *)x, b = *(const int *)y;
    return (a > b) - (a < b);          // évite le débordement de a - b
}
qsort(a, n, sizeof a[0], comparer);
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
char s1[] = "Bonjour";              // 8 octets : 7 caractères + '\0'
char s2[20] = "Salut";              // taille 20, le reste est mis à 0
char s3[] = {'H', 'i', '\0'};       // équivalent à "Hi"
const char *s4 = "Littéral";        // pointeur vers une chaîne en LECTURE SEULE
```

> ⚠️ **Modifier un littéral de chaîne** (`s4[0] = 'l';`) est un comportement indéfini. Déclarez-les `const char *`.
> ⚠️ Oublier de réserver la place du `'\0'` est une erreur classique (**dépassement d'un octet**).

## 12.2 Fonctions de `<string.h>`

| Fonction | Rôle |
| --- | --- |
| `strlen(s)` | Longueur (sans le `'\0'`) |
| `strcpy(dst, src)` / `strncpy` | Copie (⚠️ voir ci-dessous) |
| `strcat(dst, src)` / `strncat` | Concaténation |
| `strcmp(a, b)` / `strncmp` | Comparaison : `0` si égales, `<0` / `>0` sinon |
| `strchr(s, c)` / `strrchr` | Première / dernière occurrence d'un caractère |
| `strstr(s, sous)` | Recherche d'une sous-chaîne |
| `strspn` / `strcspn` | Longueur du préfixe fait de / sans certains caractères |
| `strtok(s, delims)` | Découpe en jetons (⚠️ modifie la chaîne, non réentrant) |
| `strdup(s)` | Duplique avec `malloc` (**standard depuis C23**, POSIX avant) |
| `memcpy` / `memmove` / `memset` / `memcmp` | Opérations sur des octets |

```c
char nom[30] = "Alice";
strlen(nom);                          // 5
strcmp("abc", "abd") < 0;             // vrai
if (strcmp(a, b) == 0) { /* égales */ }   // ⚠️ jamais a == b (compare des adresses)
```

## 12.3 Copier et concaténer en sécurité

| Fonction | Problème |
| --- | --- |
| `strcpy`, `strcat` | **Aucune vérification de taille** → dépassement de tampon |
| `strncpy` | **Ne garantit pas le `'\0'`** final et remplit de zéros (lent) |
| `strncat` | Le paramètre est le nombre de caractères **à ajouter**, pas la taille du tampon |
| **`snprintf`** ✅ | Toujours terminé par `'\0'`, limité à la taille du tampon |

```c
char dest[16];
snprintf(dest, sizeof dest, "%s-%d", "ID", 42);       // ✅ sûr

// Concaténation sûre
size_t len = strlen(dest);
snprintf(dest + len, sizeof dest - len, "%s", "_fin");
```

> 💡 Sur BSD/macOS : `strlcpy` / `strlcat` ; non standard en C (mais proposés dans certaines libc récentes). Les variantes `*_s` de l'**Annexe K** sont optionnelles et peu implémentées : ne comptez pas dessus.

## 12.4 Lire et parcourir

```c
for (size_t i = 0; s[i] != '\0'; i++) { /* traiter s[i] */ }
for (const char *p = s; *p; p++) { /* traiter *p */ }

char saisie[50];
fgets(saisie, sizeof saisie, stdin);
saisie[strcspn(saisie, "\n")] = '\0';
```

## 12.5 `<ctype.h>` : tester et convertir les caractères

```c
#include <ctype.h>
isalpha(c);  isdigit(c);  isalnum(c);  isspace(c);  ispunct(c);
isupper(c);  islower(c);  toupper(c);  tolower(c);
```

> ⚠️ Avec un `char` signé, castez : `isalpha((unsigned char)c)`.

## 12.6 Conversions chaîne ⇄ nombre

```c
#include <stdlib.h>
long n = strtol("123abc", &fin, 10);      // ✅ détecte les erreurs via fin et errno
double d = strtod("3.14", NULL);
int a = atoi("42");                       // ⚠️ pas de détection d'erreur : à éviter

char tampon[32];
snprintf(tampon, sizeof tampon, "%d", 123);   // nombre → chaîne
```

## 12.7 Tableau de chaînes

```c
const char *jours[] = { "Lundi", "Mardi", "Mercredi" };
for (size_t i = 0; i < sizeof jours / sizeof jours[0]; i++) puts(jours[i]);

char noms[3][20] = { "Alice", "Bob", "Chloé" };    // 3 chaînes modifiables de 19 caractères max
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
int x = 42;
int *p = &x;          // p contient l'adresse de x

printf("%d\n", x);    // 42
printf("%p\n", (void *)p);   // adresse de x
printf("%d\n", *p);   // 42 : déréférencement (valeur pointée)
*p = 100;             // modifie x via le pointeur → x == 100
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
int *p = NULL;        // C23 : int *p = nullptr;
if (p != NULL) { /* sûr de déréférencer */ }
```

Déréférencer `NULL` est un comportement indéfini (généralement un plantage). **Initialisez toujours un pointeur** (adresse valide ou `NULL`).

## 13.3 Arithmétique des pointeurs

Ajouter `n` à un pointeur le déplace de **`n` éléments** (pas `n` octets).

```c
int t[] = {10, 20, 30, 40};
int *p = t;                  // t se dégrade en &t[0]
*(p + 2);                    // 30, équivalent à t[2]
p++;                         // pointe sur t[1]
ptrdiff_t ecart = &t[3] - &t[1];   // 2 (nombre d'éléments)
```

Équivalence : **`t[i]` ≡ `*(t + i)`**.

> ⚠️ Rester dans les bornes du tableau (ou **un élément après la fin**, sans le déréférencer).

## 13.4 Tableaux ≠ pointeurs

```c
int t[5];
int *p = t;
sizeof t;      // 20 (5 × 4 octets)
sizeof p;      // 8 (taille d'un pointeur)
// t = p;      // ❌ un tableau n'est pas une valeur modifiable
```

## 13.5 Pointeurs et fonctions

```c
void incrementer(int *n) { (*n)++; }       // parenthèses : (*n)++ ≠ *n++

int x = 0;
incrementer(&x);                            // x == 1
```

Les pointeurs servent à : **modifier** les arguments, **renvoyer plusieurs valeurs**, **éviter de copier** de gros objets, manipuler des **tableaux** et de la **mémoire dynamique**.

## 13.6 `const` et pointeurs (rappel)

```c
const int *a;          // données non modifiables via a
int *const b = &x;     // adresse non modifiable
void afficher(const char *texte);   // « je ne modifie pas texte »
```

## 13.7 `void *` : pointeur générique

```c
void *q = &x;                 // peut contenir n'importe quelle adresse d'objet
int *r = q;                   // conversion implicite en C (pas besoin de cast)
// *q;                        // ❌ impossible de déréférencer un void *
```

Utilisé par `malloc`, `qsort`, `memcpy`…

## 13.8 Pointeur vers une structure

```c
struct Point { int x, y; };
struct Point pt = {1, 2};
struct Point *pp = &pt;
pp->x = 10;                   // identique à (*pp).x = 10
```

## 13.9 `restrict` *(ajout, C99)*

Promesse au compilateur que, pendant la durée de vie du pointeur, **aucun autre pointeur n'accède** à la même zone : permet des optimisations (ex. `memcpy`).

```c
void ajouter(int *restrict dst, const int *restrict src, size_t n);
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
int *mauvaise(void) {
    int local = 5;
    return &local;       // ❌ adresse d'une variable détruite à la sortie
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
    int *tab = malloc(n * sizeof *tab);       // ✅ sizeof *tab : s'adapte au type
    if (tab == NULL) {                        // ⚠️ toujours vérifier
        perror("malloc");
        return EXIT_FAILURE;
    }
    for (size_t i = 0; i < n; i++) tab[i] = (int)(i * i);

    free(tab);                                // libérer
    tab = NULL;                               // évite l'usage d'un pointeur pendant
    return 0;
}
```

> ✅ En C, **ne castez pas** le résultat de `malloc` (`void *` se convertit implicitement).
> ✅ Préférez `malloc(n * sizeof *p)` à `malloc(n * sizeof(int))`.

## 14.3 `calloc`

```c
int *zeros = calloc(100, sizeof *zeros);     // 100 entiers à 0
```

## 14.4 `realloc` : la bonne façon

```c
int *nouveau = realloc(tab, 10 * sizeof *tab);
if (nouveau == NULL) {          // échec : l'ancien bloc est toujours valide !
    free(tab);
    return EXIT_FAILURE;
}
tab = nouveau;
```

> ⚠️ **Ne faites jamais `tab = realloc(tab, …)`** directement : en cas d'échec, vous perdez le pointeur d'origine (fuite). Après un `realloc` réussi, l'**ancienne adresse est invalide** (le bloc a pu être déplacé).

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
| **L'appelant fournit le tampon** ✅ | Simple, aucune fuite, pas de `malloc` | L'appelant doit prévoir la taille |
| **Allocation dynamique** (`malloc`) | Taille variable, durée de vie libre | L'appelant doit `free` |
| **Variable `static`** | Survit à l'appel | **Non réentrant**, partagée (écrasée à chaque appel) |
| **Encapsuler dans une `struct`** | Retour par valeur | Taille fixe |

### 1. L'appelant fournit le tampon (recommandé)

```c
void majuscules(const char *src, char *dst, size_t taille) {
    size_t i = 0;
    for (; src[i] && i + 1 < taille; i++) dst[i] = (char)toupper((unsigned char)src[i]);
    dst[i] = '\0';
}

char resultat[64];
majuscules("bonjour", resultat, sizeof resultat);
```

### 2. Allocation dynamique

```c
char *dupliquer(const char *s) {
    size_t n = strlen(s) + 1;
    char *copie = malloc(n);
    if (copie) memcpy(copie, s, n);
    return copie;                  // l'APPELANT doit appeler free(copie)
}

char *c = dupliquer("texte");
if (c) { puts(c); free(c); }
```

```c
int *creer_tableau(size_t n, int valeur) {
    int *t = malloc(n * sizeof *t);
    if (!t) return NULL;
    for (size_t i = 0; i < n; i++) t[i] = valeur;
    return t;
}
```

### 3. Variable `static` (à éviter)

```c
const char *nom_du_jour(int j) {
    static const char *noms[] = {"Lun", "Mar", "Mer"};   // chaînes constantes : sûr
    return noms[j];
}
```

Retourner un **littéral** ou un tableau `static` constant est sûr ; retourner un tampon `static` modifiable est piégeux (écrasé au prochain appel, dangereux avec des fils d'exécution).

### 4. Structure

```c
struct Triplet { int v[3]; };
struct Triplet fabriquer(void) { return (struct Triplet){ .v = {1, 2, 3} }; }
```

## 15.3 Ce qu'il ne faut jamais faire

```c
char *mauvais(void) {
    char tampon[20] = "perdu";
    return tampon;        // ❌ tableau local détruit à la sortie
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
```

## 16.4 Matrices dynamiques

### Méthode A : tableau de pointeurs (lignes indépendantes)

```c
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
```

### Méthode B : bloc unique contigu (✅ plus efficace)

```c
int *m = calloc(l * c, sizeof *m);       // un seul malloc, un seul free
m[i * c + j] = 5;                        // élément (i, j)
free(m);
```

Ou avec un pointeur vers tableau (accès naturel `m[i][j]`, C99) :

```c
int (*m)[c] = calloc(l, sizeof *m);      // c doit être connu à l'exécution (VLA type)
m[i][j] = 5;
free(m);
```

---

# 17. Pointeurs doubles

## 17.1 Définition

Un **pointeur double** (`type **`) contient l'**adresse d'un pointeur**.

```c
int x = 10;
int *p = &x;
int **pp = &p;

**pp = 20;         // modifie x
```

```text
pp ──▶ p ──▶ x
```

## 17.2 Usages principaux

### 1. Modifier un pointeur depuis une fonction

```c
void allouer(int **p, size_t n) {
    *p = malloc(n * sizeof **p);        // modifie le pointeur de l'appelant
}

int *tab = NULL;
allouer(&tab, 10);
```

Sans pointeur double, la fonction ne recevrait qu'une **copie** du pointeur.

### 2. Tableau de chaînes / matrices

```c
char **lignes = malloc(3 * sizeof *lignes);
for (int i = 0; i < 3; i++) lignes[i] = dupliquer("texte");
// … puis libérer chaque ligne, puis le tableau
```

### 3. Listes chaînées (insertion / suppression élégante)

Voir `supprimer()` à la [section 16](#16-structures-de-données-dynamiques) : `Noeud **pp = &tete;`.

### 4. `argv` : `char **argv` (voir [section 23](#23-arguments-de-la-ligne-de-commande)).

## 17.3 Libération

```c
void liberer_lignes(char **t, size_t n) {
    for (size_t i = 0; i < n; i++) free(t[i]);   // d'abord le contenu
    free(t);                                      // puis le tableau de pointeurs
}
```

> ⚠️ Un `int **` **n'est pas** un `int [][N]` : ce sont des représentations mémoire différentes, non interchangeables.

---

# 18. Structures et unions

## 18.1 Structures (`struct`)

Une **structure** regroupe des données de **types différents** sous un seul nom.

```c
struct Etudiant {
    char nom[50];
    int age;
    float moyenne;
};

struct Etudiant e1 = {"Alice", 20, 15.5f};
struct Etudiant e2 = { .nom = "Bob", .age = 22, .moyenne = 12.0f };   // initialisation désignée (C99)

e1.age = 21;                              // accès avec .
struct Etudiant *p = &e1;
printf("%s\n", p->nom);                   // accès via un pointeur avec ->
```

### Opérations

```c
struct Etudiant copie = e1;               // ✅ copie complète (affectation autorisée)
// if (e1 == e2) { }                      // ❌ comparaison de structures interdite : comparez champ par champ
```

### Littéraux composés (C99)

```c
afficher_point((struct Point){ .x = 1, .y = 2 });
```

### Structures imbriquées et tableaux de structures

```c
struct Date { int j, m, a; };
struct Personne { char nom[30]; struct Date naissance; };

struct Etudiant classe[30];
for (size_t i = 0; i < 30; i++) classe[i].age = 18;
```

### Structure auto-référencée

```c
struct Noeud { int valeur; struct Noeud *suivant; };   // pointeur vers son propre type
```

## 18.2 Alignement et remplissage (*padding*)

Le compilateur insère des octets de **remplissage** pour **aligner** les membres.

```c
struct A { char c; int i; char d; };   // typiquement 12 octets
struct B { int i; char c; char d; };   // typiquement 8 octets (mieux ordonné)

#include <stddef.h>
offsetof(struct A, i);                  // décalage du membre i
sizeof(struct A);
```

> 💡 Ordonnez les membres **du plus grand au plus petit** pour réduire le remplissage. Ne comparez pas de structures avec `memcmp` (les octets de remplissage sont indéterminés).

## 18.3 Champs de bits

```c
struct Drapeaux {
    unsigned int lecture  : 1;
    unsigned int ecriture : 1;
    unsigned int mode     : 3;
};
```

Utile pour des registres matériels ; **la disposition mémoire dépend du compilateur** (peu portable).

## 18.4 Membre de tableau flexible (C99)

```c
struct Message {
    size_t longueur;
    char donnees[];                     // taille variable, en fin de structure
};
struct Message *m = malloc(sizeof *m + 100);
```

## 18.5 Unions

Les membres d'une **union** **partagent la même zone mémoire** ; sa taille est celle de son plus grand membre. Un seul membre est valide à la fois.

```c
union Valeur {
    int i;
    float f;
    char c[4];
};

union Valeur v;
v.i = 42;
v.f = 3.14f;        // écrase la valeur précédente
```

### Union étiquetée (*tagged union*) : usage sûr

```c
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
enum Jour { LUNDI, MARDI, MERCREDI, JEUDI, VENDREDI, SAMEDI, DIMANCHE };
// LUNDI = 0, MARDI = 1, …

enum Jour aujourdhui = MERCREDI;
printf("%d\n", aujourdhui);              // 2
```

### Valeurs explicites

```c
enum Code { OK = 200, NON_TROUVE = 404, ERREUR = 500 };
enum Mois { JANVIER = 1, FEVRIER, MARS };     // FEVRIER = 2, MARS = 3
enum Options { OPT_A = 1 << 0, OPT_B = 1 << 1, OPT_C = 1 << 2 };   // drapeaux combinables par |
```

### Type sous-jacent *(C23)*

```c
enum Couleur : unsigned char { ROUGE, VERT, BLEU };   // type imposé
```

## 19.2 Avec `typedef` et `switch`

```c
typedef enum { ROUGE, VERT, BLEU } Couleur;

void decrire(Couleur c) {
    switch (c) {
        case ROUGE: puts("rouge"); break;
        case VERT:  puts("vert");  break;
        case BLEU:  puts("bleu");  break;
    }
}
```

> 💡 Compilez avec `-Wall` : le compilateur avertit si un `case` d'un `enum` est oublié dans un `switch` sans `default`.

## 19.3 Particularités

- Les constantes d'énumération sont de type **`int`** en C (≠ C++) et **partagent la portée** de l'enum : deux enums ne peuvent pas avoir la même constante.
- C **n'empêche pas** d'affecter n'importe quelle valeur entière à une variable `enum`.
- Astuce : ajouter une constante finale `NB_JOURS` pour compter les éléments.
- Une table de noms parallèle :

```c
static const char *noms_jours[] = { [LUNDI] = "Lundi", [MARDI] = "Mardi" /* … */ };
```

---

# 20. `typedef`

## 20.1 Créer un alias de type

```c
typedef unsigned long ulong;
ulong n = 1000;

typedef struct {
    int x, y;
} Point;                      // plus besoin d'écrire « struct Point »

Point p = {1, 2};
```

## 20.2 Usages courants

```c
typedef enum { ROUGE, VERT } Couleur;
typedef int (*Comparateur)(const void *, const void *);    // alias de pointeur de fonction
typedef char Nom[50];                                      // alias de tableau
typedef struct Noeud Noeud;                                // déclaration anticipée
struct Noeud { int v; Noeud *suivant; };
```

## 20.3 `typedef` ou `#define` ?

| | `typedef` | `#define` |
| --- | --- | --- |
| Traité par | Le **compilateur** (a un type) | Le **préprocesseur** (texte) |
| Portée | Respectée | Globale au fichier |
| Pointeurs | `typedef int *PInt; PInt a, b;` → deux pointeurs ✅ | `#define PInt int *` → `PInt a, b;` : seul `a` est un pointeur ❌ |

## 20.4 Bonnes pratiques

- Utilisez `typedef` pour **simplifier** (structures, pointeurs de fonctions) et **abstraire** (types portables comme `size_t`).
- Évitez de masquer les pointeurs derrière un `typedef` (cela cache `*`).
- Conventions : types en `PascalCase` ou suffixe `_t` (⚠️ le suffixe `_t` est réservé par POSIX).

---

# 21. Pointeurs de fonctions

*(Section ajoutée : notion fondamentale absente du guide d'origine.)*

## 21.1 Principe

Une fonction a une **adresse** : on peut la stocker dans un pointeur, la passer en argument et l'appeler indirectement. C'est la base des **rappels** (*callbacks*), des tables de dispatch et du polymorphisme en C.

```c
int additionner(int a, int b) { return a + b; }
int soustraire(int a, int b) { return a - b; }

int (*operation)(int, int);        // pointeur vers une fonction (int, int) → int
operation = additionner;           // (ou &additionner)
printf("%d\n", operation(3, 2));   // 5
operation = soustraire;
printf("%d\n", operation(3, 2));   // 1
```

La syntaxe `type (*nom)(paramètres)` : les **parenthèses autour de `*nom`** sont indispensables (`int *f(int)` déclare une fonction retournant un `int *`).

## 21.2 Avec `typedef`

```c
typedef int (*Operation)(int, int);

int appliquer(Operation f, int a, int b) { return f(a, b); }
appliquer(additionner, 4, 5);
```

## 21.3 Callbacks : `qsort`

```c
int par_age(const void *a, const void *b) {
    const struct Personne *p = a, *q = b;
    return (p->age > q->age) - (p->age < q->age);
}
qsort(personnes, n, sizeof personnes[0], par_age);
```

## 21.4 Table de fonctions

```c
typedef struct { const char *nom; Operation f; } Commande;

static const Commande commandes[] = {
    { "add", additionner },
    { "sub", soustraire },
};

for (size_t i = 0; i < sizeof commandes / sizeof commandes[0]; i++)
    if (strcmp(commandes[i].nom, saisie) == 0) printf("%d\n", commandes[i].f(6, 3));
```

## 21.5 Simuler des méthodes (« objets » en C)

```c
typedef struct Forme {
    double (*aire)(const struct Forme *);
    void (*detruire)(struct Forme *);
} Forme;
```

## 21.6 Sélection générique : `_Generic` (C11)

```c
#define afficher(x) _Generic((x), int: afficher_int, double: afficher_double, default: afficher_autre)(x)
```

---

# 🔴 Niveau avancé

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
FILE *f = fopen("donnees.txt", "r");
if (f == NULL) {
    perror("fopen");                 // affiche : fopen: No such file or directory
    return EXIT_FAILURE;
}
/* … utilisation … */
fclose(f);                           // ⚠️ toujours fermer (vide les tampons)
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
FILE *f = fopen("sortie.txt", "w");
if (!f) { perror("fopen"); return EXIT_FAILURE; }

fprintf(f, "Nom : %s, âge : %d\n", "Alice", 30);
fputs("Une ligne\n", f);
fputc('A', f);

if (fclose(f) != 0) perror("fclose");   // fclose peut échouer (disque plein) : vérifiez-le
```

## 22.4 Lire du texte

### Ligne par ligne (recommandé)

```c
char ligne[256];
while (fgets(ligne, sizeof ligne, f) != NULL) {
    ligne[strcspn(ligne, "\n")] = '\0';
    printf("Lu : %s\n", ligne);
}
```

### Caractère par caractère

```c
int c;                                   // ⚠️ int et non char, pour distinguer EOF
while ((c = fgetc(f)) != EOF) putchar(c);
```

### Formaté avec `fscanf`

```c
char nom[50]; int age;
while (fscanf(f, "%49s %d", nom, &age) == 2) {      // vérifier le nombre de valeurs lues
    printf("%s a %d ans\n", nom, age);
}
```

> ⚠️ **Ne bouclez jamais sur `while (!feof(f))`** : `feof` n'est vrai qu'**après** une lecture ayant échoué, ce qui traite une dernière fois des données invalides. Testez la valeur **de retour** de la fonction de lecture.

Distinguer fin de fichier et erreur :

```c
if (ferror(f)) perror("lecture");
else if (feof(f)) puts("Fin du fichier");
```

## 22.5 Fichiers binaires

```c
struct Personne { char nom[30]; int age; };

// Écriture
struct Personne p = {"Alice", 30};
FILE *f = fopen("data.bin", "wb");
fwrite(&p, sizeof p, 1, f);          // renvoie le nombre d'éléments écrits
fclose(f);

// Lecture
f = fopen("data.bin", "rb");
if (fread(&p, sizeof p, 1, f) == 1) printf("%s\n", p.nom);
fclose(f);
```

> ⚠️ Les fichiers binaires dépendent de l'**architecture** (taille des types, **endianness**, remplissage des structures) : ils ne sont pas forcément portables entre machines. Pour échanger des données, préférez un format texte (CSV, JSON) ou sérialisez champ par champ avec des types de taille fixe.

### Texte ou binaire ?

| | Texte | Binaire |
| --- | --- | --- |
| Lisible par l'humain | ✅ | ❌ |
| Conversion des fins de ligne (`\n` ↔ `\r\n`) | Oui (Windows) | **Non** |
| Taille / vitesse | Plus grand, plus lent | Compact, rapide |
| Portabilité | ✅ | ⚠️ |

## 22.6 Se positionner dans un fichier

```c
fseek(f, 0, SEEK_END);          // aller à la fin
long taille = ftell(f);         // position courante = taille du fichier
rewind(f);                      // retour au début
fseek(f, 10, SEEK_SET);         // 10 octets depuis le début
fseek(f, -5, SEEK_CUR);         // reculer de 5
```

Constantes : `SEEK_SET` (début), `SEEK_CUR` (position courante), `SEEK_END` (fin).

### Lire un fichier entier en mémoire

```c
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
```

## 22.7 Opérations sur les fichiers

```c
remove("temporaire.txt");                 // supprimer
rename("ancien.txt", "nouveau.txt");      // renommer / déplacer
FILE *tmp = tmpfile();                    // fichier temporaire supprimé à la fermeture
fflush(f);                                // forcer l'écriture du tampon
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
int main(int argc, char *argv[]) { /* … */ }     // ou : char **argv
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

> ℹ️ **Tous les arguments sont des chaînes** : convertissez les nombres explicitement.

## 23.2 Convertir en nombres (avec contrôle d'erreurs)

```c
#include <errno.h>
#include <stdlib.h>

char *fin;
errno = 0;
long n = strtol(argv[1], &fin, 10);
if (errno != 0 || fin == argv[1] || *fin != '\0') {
    fprintf(stderr, "Nombre invalide : %s\n", argv[1]);
    return EXIT_FAILURE;
}
```

`atoi` ne signale aucune erreur : à éviter. Autres : `strtoul`, `strtod`.

## 23.3 Exemple : somme d'entiers

```c
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
for (int i = 1; i < argc; i++) {
    if (strcmp(argv[i], "-v") == 0 || strcmp(argv[i], "--verbose") == 0) verbeux = 1;
    else if (strcmp(argv[i], "-o") == 0 && i + 1 < argc) sortie = argv[++i];
    else if (strcmp(argv[i], "--") == 0) { i++; break; }          // fin des options
    else if (argv[i][0] == '-') { fprintf(stderr, "Option inconnue : %s\n", argv[i]); return 2; }
}
```

### `getopt` (POSIX, Linux/macOS)

```c
#include <unistd.h>

int opt;
while ((opt = getopt(argc, argv, "vo:h")) != -1) {
    switch (opt) {
        case 'v': verbeux = 1; break;
        case 'o': sortie = optarg; break;            // option avec valeur
        case 'h': usage(argv[0]); return 0;
        default:  usage(argv[0]); return 1;
    }
}
// arguments restants : argv[optind] … argv[argc - 1]
```

Alternative portable : `getopt_long` (options longues `--help`) ou bibliothèques tierces. Sous Windows (MSVC), `getopt` n'existe pas en standard.

## 23.5 Variables d'environnement

```c
const char *home = getenv("HOME");        // NULL si absente
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
#include <stdio.h>        // en-tête système (cherché dans les dossiers du compilateur)
#include "monfichier.h"   // en-tête du projet (cherché d'abord dans le dossier courant)
```

## 24.3 `#define` : macros

```c
#define TAILLE 100                    // constante
#define CARRE(x) ((x) * (x))          // macro avec paramètre

int a = CARRE(3 + 1);                 // ((3 + 1) * (3 + 1)) = 16 ✅
```

### Pièges des macros

```c
#define MAUVAIS(x) x * x
MAUVAIS(3 + 1);                       // 3 + 1 * 3 + 1 = 7 ❌ → toujours parenthéser

#define MAX(a, b) ((a) > (b) ? (a) : (b))
MAX(i++, j++);                        // ❌ un argument est évalué DEUX fois
```

> ✅ Préférez les **fonctions `static inline`**, les `const`/`constexpr` et les `enum` aux macros quand c'est possible : elles sont typées et sans effets de bord surprenants.

### Macros multi-instructions : `do { … } while (0)`

```c
#define ECHANGER(a, b) do { typeof(a) t = (a); (a) = (b); (b) = t; } while (0)
if (x > y) ECHANGER(x, y); else puts("ok");       // fonctionne grâce au do…while(0)
```

### Opérateurs `#` et `##`

```c
#define TEXTE(x) #x               // « stringification »
#define COLLER(a, b) a##b         // concaténation de jetons
TEXTE(bonjour)                    // "bonjour"
int COLLER(valeur, 1) = 5;        // int valeur1 = 5;
```

### Macros variadiques

```c
#define LOG(fmt, ...) fprintf(stderr, "[%s:%d] " fmt "\n", __FILE__, __LINE__ __VA_OPT__(,) __VA_ARGS__)
LOG("Démarrage");
LOG("Valeur = %d", 42);
```

`__VA_OPT__` est standard depuis C23 (extension courante auparavant).

### `#undef`

```c
#undef TAILLE
```

## 24.4 Compilation conditionnelle

```c
#ifdef DEBUG
    printf("Valeur : %d\n", x);
#endif

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

#if __STDC_VERSION__ >= 202311L      // C23 ou plus récent
    /* … */
#endif
```

C23 ajoute `#elifdef` / `#elifndef`, `#warning` et `__has_include` :

```c
#if __has_include(<threads.h>)
#include <threads.h>
#endif
#warning "Section à revoir"          // avertissement personnalisé (C23)
#error "Plateforme non supportée"    // arrête la compilation
```

Définir une macro à la compilation : `gcc -DDEBUG -DVERSION=\"2.0\" …`

## 24.5 Gardes d'inclusion

Évitent qu'un en-tête soit inclus plusieurs fois :

```c
#ifndef MON_ENTETE_H
#define MON_ENTETE_H
/* … déclarations … */
#endif

// Alternative répandue (non standard mais supportée partout) :
#pragma once
```

## 24.6 `#embed` *(C23)*

Inclut directement le contenu binaire d'un fichier dans un tableau :

```c
const unsigned char icone[] = {
    #embed "icone.png"
};
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
#ifdef DEBUG
    #define DBG(...) fprintf(stderr, __VA_ARGS__)
#else
    #define DBG(...) ((void)0)
#endif
```

## 24.9 `static_assert` : vérifications à la compilation

```c
static_assert(sizeof(int) >= 4, "int doit faire au moins 32 bits");   // C23 : mot-clé ; C11 : _Static_assert
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
x |=  (1u << n);        // mettre le bit n à 1
x &= ~(1u << n);        // mettre le bit n à 0
x ^=  (1u << n);        // inverser le bit n
(x >> n) & 1u;          // lire le bit n
(x & (x - 1)) == 0;     // x est-il une puissance de 2 ? (x ≠ 0)
x & 1u;                 // parité (1 = impair)
```

## 25.3 Drapeaux (*flags*) et masques

```c
enum { LECTURE = 1u << 0, ECRITURE = 1u << 1, EXEC = 1u << 2 };

unsigned int droits = LECTURE | ECRITURE;       // combiner
if (droits & ECRITURE) puts("écriture autorisée");
droits &= ~ECRITURE;                            // retirer
```

## 25.4 Afficher en binaire

```c
void afficher_binaire(uint32_t n) {
    for (int i = 31; i >= 0; i--) {
        putchar(((n >> i) & 1u) ? '1' : '0');
        if (i % 8 == 0 && i) putchar(' ');
    }
    putchar('\n');
}
// C23 : printf("%b\n", n);
```

## 25.5 Échange sans variable temporaire (curiosité)

```c
a ^= b; b ^= a; a ^= b;      // ⚠️ échoue si a et b désignent la MÊME variable
```

## 25.6 Fonctions de `<stdbit.h>` *(C23)*

```c
#include <stdbit.h>
stdc_count_ones(x);          // nombre de bits à 1 (popcount)
stdc_leading_zeros(x);
stdc_trailing_zeros(x);
stdc_bit_width(x);
stdc_has_single_bit(x);      // puissance de 2 ?
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
unsigned long long factorielle(unsigned int n) {
    if (n <= 1) return 1;                    // cas de base
    return n * factorielle(n - 1);           // appel récursif
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
// Fibonacci (⚠️ exponentiel : très lent pour n grand)
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
    printf("Disque %d : %c → %c\n", n, de, vers);
    hanoi(n - 1, via, vers, de);
}
```

## 26.4 Récursivité terminale

Si l'appel récursif est la **dernière opération**, certains compilateurs (avec `-O2`) le transforment en boucle. **Ce n'est pas garanti** par C.

```c
unsigned long long fact_acc(unsigned int n, unsigned long long acc) {
    return n <= 1 ? acc : fact_acc(n - 1, acc * n);
}
```

## 26.5 Récursivité ou itération ?

| | Récursivité | Itération |
| --- | --- | --- |
| Lisibilité | ✅ Naturelle pour arbres, diviser pour régner | Plus verbeuse parfois |
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

`char` est un **octet**, pas un caractère visible. En **UTF-8** (encodage standard actuel), un caractère occupe **1 à 4 octets** (`é` = 2 octets, `😀` = 4).

```c
const char *s = "é";
strlen(s);              // 2 (octets, pas 1 caractère)
```

## 27.2 Les approches

| Approche | Description | Remarques |
| --- | --- | --- |
| **UTF-8 dans des `char *`** ✅ | Chaînes ordinaires encodées en UTF-8 | Simple ; `strlen` compte des octets ; la plupart des fonctions `<string.h>` fonctionnent |
| **`wchar_t`** | Caractères « larges » (`L"…"`), `<wchar.h>` | Taille variable selon la plateforme (2 octets sous Windows, 4 sous Linux) ; peu portable |
| **`char16_t` / `char32_t`** | UTF-16 / UTF-32 (`u"…"`, `U"…"`), `<uchar.h>` | Largeur fixe |
| **`char8_t`** *(C23)* | Type dédié à l'UTF-8, littéraux `u8"…"` | |

```c
#include <wchar.h>
#include <locale.h>

setlocale(LC_ALL, "");                 // active la locale de l'utilisateur
wchar_t *w = L"Bonjour é";
wprintf(L"%ls\n", w);
```

> ⚠️ Ne mélangez pas `printf` et `wprintf` sur le même flux.

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
| `-Wall -Wextra` | Active la plupart des **avertissements** ✅ |
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

> ✅ Traitez les **avertissements comme des erreurs** : ils révèlent souvent de vrais bugs.

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

> ⚠️ Le code avec comportement indéfini peut se comporter différemment selon le niveau d'optimisation.

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
#include <stdlib.h>
atexit(nettoyer);          // enregistre une fonction exécutée à la sortie
exit(EXIT_FAILURE);        // quitte immédiatement (depuis n'importe quelle fonction)
abort();                   // arrêt anormal
```

### Appels système ou fonctions de bibliothèque ?

| | Fonctions de la bibliothèque C | Appels système |
| --- | --- | --- |
| Exemples | `printf`, `fopen`, `malloc` | `write`, `open`, `brk`/`mmap` |
| Portabilité | ✅ Standard C | Dépend du système (POSIX, Windows API) |
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
assert(ptr != NULL);        // vérification de développement (désactivée avec -DNDEBUG)
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
#include <stdlib.h>
#include <time.h>
srand((unsigned)time(NULL));        // initialiser la graine UNE seule fois
int de = rand() % 6 + 1;            // 1 à 6 (qualité médiocre ; pas pour la cryptographie)
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

- 📘 **cppreference (C)** : <https://en.cppreference.com/w/c>
- 📗 *Le langage C* — Kernighan & Ritchie (*The C Programming Language*, 2ᵉ éd.)
- 📙 *Modern C* — Jens Gustedt (gratuit en ligne)
- 🔒 **SEI CERT C Coding Standard** : <https://wiki.sei.cmu.edu/confluence/display/c>
- 🧪 **Compiler Explorer** : <https://godbolt.org>
- 📜 **Brouillons de la norme (WG14)** : <https://www.open-std.org/jtc1/sc22/wg14/>

---

<div align="center">

*Bon code, et que vos pointeurs soient toujours valides ! ⚙️*

</div>
