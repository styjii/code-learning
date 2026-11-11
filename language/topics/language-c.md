# Langage C — Cours complet

*Module d'apprentissage détaillé · Normes C17 / C23 · Sections 1 à 30*

## Avant de commencer : comment utiliser ce cours

Ce cours développe, section par section, le plan « Langage C — Guide complet ». Chaque section suit la même démarche : **un principe** (ce qu'est la notion et pourquoi elle existe), **un fonctionnement** (comment le compilateur et la machine la traitent), **des exemples commentés**, puis **les pièges** et **les bonnes pratiques**.

**Conventions** :

- Tous les exemples se compilent avec `gcc -Wall -Wextra -std=c17 fichier.c -o programme`. Les exemples marqués *(C23)* demandent `-std=c23`.
- Les commentaires `// erreur` signalent du code **volontairement incorrect** ; ne le recopiez pas dans vos programmes.

**Prérequis** : savoir ouvrir un terminal et créer un fichier texte. Aucune connaissance préalable en programmation n'est nécessaire.

## 1. Introduction au C

### 1.1 Qu'est-ce que le C ?

Le **C** est un langage de programmation **compilé, impératif et procédural**. Chacun de ces trois mots a un sens précis :

- **Compilé** : le code que vous écrivez (le *code source*) n'est pas exécuté tel quel. Un programme appelé **compilateur** le traduit une fois pour toutes en **code machine**, c'est-à-dire en instructions directement comprises par le processeur. L'exécutable obtenu n'a plus besoin du compilateur pour fonctionner. Cela contraste avec les langages interprétés (Python, JavaScript), où un interpréteur lit et exécute le code à la volée.
- **Impératif** : un programme est une **suite d'ordres** exécutés dans l'ordre, qui modifient l'état de la mémoire (« mets 5 dans x », « répète 10 fois… »).
- **Procédural** : le programme est découpé en **procédures** (en C, des *fonctions*) que l'on appelle pour structurer le travail. Il n'y a ni classes ni objets, contrairement à Java ou C++.

Le C a été créé vers **1972** par **Dennis Ritchie** aux **Laboratoires Bell**. Il descend du langage **B** (Ken Thompson) lui-même issu de **BCPL**. Son but initial était de **réécrire le système UNIX**, jusque-là écrit en assembleur : en 1973, le noyau d'UNIX est largement réécrit en C. Ce choix est historique, car c'est la première fois qu'un système d'exploitation est écrit dans un langage de haut niveau, et donc **portable** : il suffit de disposer d'un compilateur C sur une nouvelle machine pour y porter le système.

On qualifie souvent le C de langage **de niveau intermédiaire** : il offre des constructions de haut niveau (fonctions, boucles, structures de données) tout en donnant un **accès direct à la mémoire** (les adresses, les octets, les bits) et au matériel.

| Caractéristique | Signification concrète |
| --- | --- |
| Paradigme | Procédural et impératif |
| Typage | **Statique** : le type de chaque variable est connu à la compilation. **Faiblement vérifié** : de nombreuses conversions implicites sont autorisées (un `int` devient un `double` sans avertissement) |
| Exécution | Compilé vers du **code machine natif** : très rapide, pas de machine virtuelle |
| Mémoire | **Manuelle** : le programmeur réserve (`malloc`) et libère (`free`) ; aucun ramasse-miettes |
| Portabilité | Excellente : un compilateur C existe pour presque toutes les architectures |
| Influence | A inspiré C++, Objective-C, C#, Java, Go, JavaScript (par sa syntaxe et ses concepts) |

**Ce que le C ne fait pas pour vous** : il ne vérifie pas les bornes des tableaux, ne protège pas la mémoire contre vos propres erreurs et n'offre pas de types « haut niveau » (pas de chaîne de caractères native, pas de liste, pas de dictionnaire). Cette absence de filet est la contrepartie de sa vitesse et de son contrôle.

### 1.2 Pourquoi apprendre le C ?

1. **Programmation système** : les noyaux de Linux, de Windows et de macOS/BSD, les pilotes de périphériques et les systèmes embarqués sont écrits en C.
2. **Performance** : bases de données (SQLite, PostgreSQL), moteurs de jeux, bibliothèques de calcul, et même les interpréteurs d'autres langages (CPython, Lua, Ruby) sont écrits en C.
3. **Microcontrôleurs** : Arduino, STM32, ESP32 se programment en C ou en C++. Les ressources y sont comptées en kilo-octets ; un langage sans surcoût y est indispensable.
4. **Comprendre l'ordinateur** : en C, vous manipulez explicitement la mémoire, la pile, le tas, les adresses, la compilation. Ces notions éclairent tous les autres langages.
5. **Interopérabilité** : l'**ABI** (*Application Binary Interface*) du C sert de « langue commune » entre langages. Python, Rust, Go, Java (via JNI) appellent du code C ; presque toutes les bibliothèques système exposent une interface C.

> **Attention** : le revers de la médaille est que le C **ne vous protège pas**. Dépassements de tampon, pointeurs invalides, fuites mémoire sont les causes d'une part considérable des failles de sécurité. Une discipline rigoureuse et des outils d'analyse sont indispensables (section 29).

### 1.3 Histoire et normes

Au début, le C n'avait pas de norme : sa définition était le livre *The C Programming Language* de Brian Kernighan et Dennis Ritchie (1978), d'où le nom **K&R C**. Les compilateurs divergeaient ; la normalisation a corrigé cela.

| Norme | Année | Apports principaux |
| --- | --- | --- |
| **K&R C** | 1978 | Définition informelle par le livre de Kernighan & Ritchie |
| **C89 / C90** (ANSI C / ISO C) | 1989–1990 | Première norme : **prototypes** de fonctions, `void`, `const`, `signed` |
| **C99** | 1999 | Commentaires `//`, `long long`, `<stdint.h>`, `<stdbool.h>`, `inline`, **tableaux à taille variable** (VLA), initialisations désignées, déclarations n'importe où dans un bloc |
| **C11** | 2011 | `_Generic`, `_Static_assert`, `<threads.h>`, `_Atomic`, structures anonymes ; **`gets()` supprimée** |
| **C17** (C18) | 2018 | Version de correction de C11, sans nouvelle fonctionnalité |
| **C23** | 2023 (publication ISO en 2024) | `bool`, `true`, `false`, `nullptr` en **mots-clés**, `constexpr`, `typeof`, `auto`, littéraux binaires `0b…`, séparateurs de chiffres `'`, attributs `[[…]]`, `#embed`, `<stdbit.h>`, `<stdckdint.h>` |
| **C2y** | en préparation | Prochaine révision étudiée par le comité WG14 |

**Choisir la norme** : avec l'option `-std=`. `-std=c17` ou `-std=c23` sont des normes strictes ; `-std=gnu17` / `-std=gnu23` ajoutent les extensions de GCC. **GCC 15 et suivants utilisent C23 par défaut** ; Clang et MSVC ont d'autres défauts selon leur version. **Indiquez toujours `-std=` explicitement** pour que votre code compile de la même façon partout.

### 1.4 Fonctionnement d'un programme C

Produire un programme exécutable comporte trois gestes pour le programmeur, mais plusieurs étapes pour la chaîne de compilation :

1. **Écrire** le code source dans un fichier texte d'extension `.c`.
2. **Compiler** : le compilateur (`gcc`, `clang`, MSVC…) traduit le source en code machine.
3. **Exécuter** le programme obtenu.

En réalité, la compilation se décompose ainsi :

```text
hello.c ──▶ préprocesseur ──▶ compilateur ──▶ assembleur ──▶ éditeur de liens ──▶ exécutable
 (source)      (.i)             (.s)            (.o)           (+ bibliothèques)
```

- Le **préprocesseur** traite les lignes commençant par `#` (inclusion de fichiers, macros) et produit du C « pur ».
- Le **compilateur** traduit ce C en langage assembleur propre au processeur (`.s`).
- L'**assembleur** convertit l'assembleur en **fichier objet** (`.o`), du binaire non encore exécutable.
- L'**éditeur de liens** (*linker*) assemble les fichiers objets et les bibliothèques (comme celle qui contient `printf`) pour fabriquer l'exécutable final.

Vous pouvez observer chaque étape : `gcc -E hello.c` (préprocesseur), `gcc -S hello.c` (assembleur), `gcc -c hello.c` (objet).

### 1.5 Installer un compilateur

| Système | Installation |
| --- | --- |
| **Linux (Debian/Ubuntu)** | `sudo apt install build-essential` (installe gcc et make) ; `sudo apt install clang` pour Clang |
| **macOS** | `xcode-select --install` (Clang) ou `brew install gcc` |
| **Windows** | **WSL** (Linux sous Windows, recommandé), **MSYS2** (`pacman -S mingw-w64-ucrt-x86_64-gcc`) ou **Visual Studio** (MSVC) |

Vérifiez l'installation :

```bash
gcc --version
```

**Éditeurs et IDE** : VS Code (extension C/C++), CLion, Code::Blocks, Vim/Neovim. **En ligne** : Compiler Explorer (godbolt.org), très utile pour voir l'assembleur généré, et OnlineGDB.

### 1.6 Premier programme : « Hello, World ! »

```c
#include <stdio.h>               // fonctions d'entrée/sortie

int main(void) {                 // point d'entrée du programme
    printf("Bonjour le monde !\n");   // affiche du texte
    return 0;                    // 0 = succès
}
```

Analyse ligne par ligne :

- `#include <stdio.h>` : demande au préprocesseur d'insérer le contenu de l'en-tête `stdio.h`, qui **déclare** `printf`. Sans cette ligne, le compilateur ne connaît pas `printf`.
- `int main(void)` : définit la fonction `main`, **point d'entrée** de tout programme C. `int` est son type de retour (le code de sortie) ; `void` indique qu'elle ne prend aucun argument.
- `{ … }` : le **bloc** qui constitue le corps de la fonction.
- `printf("…\n");` : appelle la fonction d'affichage. `\n` est le caractère de saut de ligne. L'instruction se termine par `;`.
- `return 0;` : renvoie au système d'exploitation le **code de sortie** ; `0` signifie « tout s'est bien passé ».

> **Remarque** : depuis C99, si `main` n'a pas de `return`, elle retourne **implicitement 0**. On l'écrit quand même par clarté.

> **Remarque** : `int main(void)` est préférable à `int main()`. Avant C23, les parenthèses vides signifient « arguments non spécifiés » (aucune vérification). En **C23**, `()` équivaut à `(void)`.

### 1.7 Compiler et exécuter

```bash
gcc -Wall -Wextra -std=c17 hello.c -o hello     # compiler
./hello                                         # exécuter (Linux/macOS)
hello.exe                                       # exécuter (Windows)
```

- `-Wall -Wextra` activent des **avertissements** qui détectent beaucoup d'erreurs courantes ; prenez l'habitude de les traiter tous.
- `-std=c17` fixe la norme.
- `-o hello` nomme l'exécutable (sinon `a.out` sous Linux/macOS).
- Le préfixe `./` est nécessaire sous Linux/macOS car le répertoire courant n'est pas dans le `PATH`.

### 1.8 Erreurs fréquentes de débutant

| Erreur | Exemple | Correction et explication |
| --- | --- | --- |
| Point-virgule oublié | `printf("Hi")` | Ajouter `;`. L'erreur est souvent signalée à la ligne **suivante** |
| Faute de frappe | `pritnf("Hi");` | `printf`. Le compilateur dit « implicit declaration » ou « undefined reference » |
| Casse | `Main()` ou `Printf()` | C est **sensible à la casse** |
| Oubli de `#include` | `printf` sans `<stdio.h>` | Inclure l'en-tête |
| `=` au lieu de `==` | `if (x = 5)` | Le premier **affecte**, le second **compare** : `if (x == 5)` |
| Variable non initialisée | `int x; printf("%d", x);` | Valeur **indéterminée** : initialiser, `int x = 0;` |

**Lire un message d'erreur** : le format est `fichier:ligne:colonne: error: description`. Corrigez **toujours la première erreur** : les suivantes en découlent souvent. Une *erreur* empêche la compilation ; un *avertissement* (`warning`) signale du code suspect mais compilable : ne l'ignorez pas.

## 2. Structure d'un programme C

### 2.1 Organisation générale

Un fichier source C suit une organisation conventionnelle, du haut vers le bas :

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

**Pourquoi cet ordre ?** Le compilateur lit le fichier **une seule fois, de haut en bas**. Un identifiant doit être **déclaré avant d'être utilisé**. C'est pourquoi `carre` est annoncée par un **prototype** avant `main` : sans lui, l'appel `carre(n)` surviendrait avant que le compilateur ne connaisse la fonction.

### 2.2 Les composants

| Composant | Rôle |
| --- | --- |
| **Directives du préprocesseur** | Lignes commençant par `#`, traitées **avant** la compilation (`#include`, `#define`, `#ifdef`…) |
| **Déclarations globales** | Hors de toute fonction ; visibles dans tout le fichier après leur déclaration |
| **Prototypes** | Annoncent le nom, le type de retour et les paramètres d'une fonction |
| **`main()`** | Point d'entrée **obligatoire**, une seule par programme |
| **Instructions** | Ordres élémentaires, terminés par `;` |
| **Blocs** | Groupes d'instructions délimités par `{ }` |
| **Commentaires** | Ignorés par le compilateur |

**Déclaration et définition** : une *déclaration* dit au compilateur qu'un nom existe et quel est son type (le prototype `int carre(int x);`). Une *définition* fournit en plus le **corps** (pour une fonction) ou **réserve la mémoire** (pour une variable). Une entité peut être déclarée plusieurs fois mais définie **une seule fois**.

### 2.3 Commentaires

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

- `//` s'étend jusqu'à la fin de la ligne (C99 et suivants).
- `/* … */` peut couvrir plusieurs lignes mais **ne s'imbrique pas** : le premier `*/` ferme le commentaire, même s'il y a eu un autre `/*` entre-temps.
- Un bon commentaire explique **pourquoi**, pas **quoi** : `i++; // incrémente i` n'apporte rien.
- Pour désactiver temporairement du code, préférez `#if 0 … #endif` (section 24), qui s'imbrique correctement.

### 2.4 Variables et instructions

```c
#include <stdio.h>

int main(void) {
    int age;                     // déclaration : réserve de la mémoire pour un int
    age = 25;                    // affectation : range 25 dans cette mémoire
    int taille = 180;            // déclaration + initialisation
    printf("age = %d, taille = %d\n", age, taille);
    return 0;
}
```

Une **variable** est un emplacement de mémoire **nommé** et **typé**. La **déclaration** crée l'emplacement ; l'**affectation** (`=`) y range une valeur ; l'**initialisation** réunit les deux. Une variable locale non initialisée contient une valeur **indéterminée** (« poubelle ») ; la lire est un comportement indéfini.

> **Bonne pratique** : depuis C99, on peut déclarer une variable **n'importe où** dans un bloc, et dans l'en-tête d'un `for`. Déclarez-la au plus près de son premier usage, et initialisez-la immédiatement.

### 2.5 Code de sortie

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *f = fopen("fichier_inexistant.txt", "r");
    if (f == NULL) {
        fprintf(stderr, "Erreur : impossible d'ouvrir le fichier\n");
        return EXIT_FAILURE;     // erreur : le shell récupère 1
    }
    fclose(f);
    printf("Fichier ouvert\n");
    return 0;                    // ou EXIT_SUCCESS (de <stdlib.h>)
}
```

La valeur retournée par `main` est le **code de sortie** du processus. Par convention, **0 = succès**, toute autre valeur = échec. Les macros portables sont `EXIT_SUCCESS` et `EXIT_FAILURE` (`<stdlib.h>`). Le shell le lit avec `echo $?` (Linux/macOS) ou `echo %ERRORLEVEL%` (Windows). Il permet à des scripts d'enchaîner des programmes : `./prog && echo OK`.

Notez l'usage de `stderr` pour les messages d'erreur : ce flux est séparé de la sortie normale (section 7.5).

### 2.6 Les étapes de la compilation (rappel)

1. **Préprocessing** : traitement de `#include`, `#define`, compilation conditionnelle.
2. **Compilation** : `.c` → assembleur → `.o` (fichier objet).
3. **Édition de liens** : assemblage des `.o` et des bibliothèques en un exécutable.
4. **Exécution** : le système charge le programme en mémoire et appelle `main`.

Les détails (options, erreurs de liens, `make`, bibliothèques) sont traités en section 28.

## 3. Syntaxe et mots-clés

### 3.1 Règles de syntaxe

- C est **sensible à la casse** : `Valeur` et `valeur` sont deux identifiants distincts.
- Chaque **instruction** se termine par `;`. Un bloc `{ }` n'est pas suivi de `;` (sauf après une définition de `struct`, `union`, `enum`, ou un initialiseur).
- Les **blocs** sont délimités par `{ }` ; l'indentation est libre pour le compilateur mais **indispensable à la lisibilité humaine**.
- Les espaces, tabulations et sauts de ligne n'ont pas de signification particulière, hors des littéraux de chaîne et des directives `#` (qui occupent une ligne).

### 3.2 Identifiants

Un **identifiant** est un nom donné à une variable, une fonction, un type, etc. Règles :

- Il est formé de **lettres, de chiffres et de `_`**.
- Il **ne commence pas par un chiffre**.
- Il **n'est pas un mot-clé**.
- Il est significatif sur au moins 31 caractères pour les identifiants internes (les compilateurs modernes en acceptent bien plus).

```c
#include <stdio.h>

int main(void) {
    int age_utilisateur = 30;    // valide : snake_case (convention courante en C)
    int _temp = 5;               // valide (mais à éviter, voir ci-dessous)
    printf("age_utilisateur = %d, _temp = %d\n", age_utilisateur, _temp);

    // int 2eme;   // erreur : un identifiant ne commence pas par un chiffre
    // int for;    // erreur : « for » est un mot-clé
    return 0;
}
```

> **Attention** : évitez les noms commençant par `_` suivi d'une majuscule, ou contenant `__` : ils sont **réservés à l'implémentation**. Les noms finissant par `_t` sont réservés par POSIX.

**Conventions de nommage** : `snake_case` pour les variables et fonctions (`nombre_eleves`), `MAJUSCULES` pour les constantes et macros (`TAILLE_MAX`), `Majuscule` ou `_t` pour les types. Choisissez des noms **parlants** : `compteur_erreurs` vaut mieux que `ce` ou `x`.

### 3.3 Mots-clés du langage (C23)

Les **mots-clés** sont réservés par le langage : on ne peut pas les utiliser comme identifiants.

| Catégorie | Mots-clés |
| --- | --- |
| **Types** | `int` `char` `short` `long` `float` `double` `void` `signed` `unsigned` `bool` *(C23)* `_Complex` `_BitInt` *(C23)* |
| **Qualificateurs** | `const` `volatile` `restrict` `_Atomic` |
| **Classes de stockage** | `auto` `register` `static` `extern` `thread_local` *(C23)* `constexpr` *(C23)* |
| **Types composés** | `struct` `union` `enum` `typedef` |
| **Contrôle** | `if` `else` `switch` `case` `default` `for` `while` `do` `break` `continue` `goto` `return` |
| **Divers** | `sizeof` `inline` `alignas` `alignof` `static_assert` `typeof` `typeof_unqual` `true` `false` `nullptr` *(C23)* `_Generic` `_Noreturn` |

> **À retenir** : en **C23**, `bool`, `true`, `false`, `nullptr`, `alignas`, `alignof`, `static_assert` et `thread_local` deviennent de vrais **mots-clés**. On n'a plus besoin de `<stdbool.h>` ni des anciennes formes `_Bool`, `_Alignas`, `_Static_assert`. Pour du code destiné aux normes antérieures, incluez `<stdbool.h>`.

Le sens de ces mots est détaillé dans les sections suivantes : types (section 4), contrôle (section 8), classes de stockage (section 10), `struct`/`union`/`enum`/`typedef` (sections 18 à 20).

### 3.4 Ponctuation et délimiteurs

| Symbole | Usage |
| --- | --- |
| `;` | Fin d'instruction |
| `,` | Séparateur (arguments, déclarations multiples, opérateur virgule) |
| `{ }` | Bloc d'instructions, listes d'initialisation |
| `( )` | Appel de fonction, regroupement d'expressions, conditions |
| `[ ]` | Indices de tableau |
| `#` | Directive du préprocesseur |
| `*` `&` | Pointeur / déréférencement ; adresse |
| `->` `.` | Accès aux membres d'une structure |
| `" "` `' '` | Littéral de chaîne ; littéral de caractère |

### 3.5 Attributs (C23)

C23 introduit une syntaxe **standard** `[[ ... ]]` pour donner des indications au compilateur sans changer le sens du programme. Auparavant, il fallait des extensions propres à chaque compilateur (`__attribute__` de GCC, `__declspec` de MSVC).

| Attribut | Effet |
| --- | --- |
| `[[nodiscard]]` | Avertit si le résultat de la fonction est ignoré |
| `[[maybe_unused]]` | Supprime l'avertissement « variable/fonction inutilisée » |
| `[[deprecated("msg")]]` | Avertit à chaque usage, avec un message |
| `[[noreturn]]` | La fonction ne rend jamais la main (comme `exit`) |
| `[[fallthrough]]` | Chute volontaire d'un `case` au suivant dans un `switch` |

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
    if (ouvrir("fichier_inexistant.txt") != 0) {
        arreter("fichier introuvable");
    }
    return 0;
}
```

Un attribut **n'est jamais obligatoire** pour la correction du programme : un compilateur qui ne le connaît pas doit l'ignorer. Il sert à documenter l'intention et à renforcer les avertissements.

## 4. Types de données et variables

### 4.1 Pourquoi des types ?

La mémoire d'un ordinateur n'est qu'une suite d'**octets** (groupes de 8 bits). Le même motif de bits peut représenter un entier, un réel ou un caractère. Le **type** d'une variable indique au compilateur **combien d'octets** réserver et **comment interpréter** ces octets. C'est aussi ce qui détermine les opérations permises.

### 4.2 Types fondamentaux

| Type | Rôle | Taille usuelle\* | Format `printf` |
| --- | --- | --- | --- |
| `char` | Caractère ou petit entier | 1 octet | `%c` (ou `%d`) |
| `short` | Entier court | 2 octets | `%hd` |
| `int` | Entier | 4 octets | `%d` |
| `long` | Entier long | 4 ou 8 octets | `%ld` |
| `long long` | Entier très long (C99) | 8 octets | `%lld` |
| `float` | Réel simple précision | 4 octets | `%f` |
| `double` | Réel double précision | 8 octets | `%f` (`%lf` avec `scanf`) |
| `long double` | Réel étendu | 8 à 16 octets | `%Lf` |
| `bool` | Booléen (C23 ; sinon `<stdbool.h>`) | 1 octet | `%d` |
| `void` | Absence de type | — | — |

\* **Les tailles dépendent de la plateforme.** La norme ne garantit que des **minimums** et un ordre : `char` ≤ `short` ≤ `int` ≤ `long` ≤ `long long`. Un `long` fait 8 octets sous Linux 64 bits mais 4 octets sous Windows 64 bits. Vérifiez toujours avec `sizeof`.

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

`sizeof` renvoie un `size_t` (entier non signé) : affichez-le avec **`%zu`**. Les limites exactes de votre machine sont dans `<limits.h>` (entiers) et `<float.h>` (réels).

**Le type `char`** mérite une précision : c'est un **entier** d'un octet. Le littéral `'A'` vaut **65** (code ASCII). On peut donc écrire `'A' + 1`, qui vaut 66, soit `'B'`. Que `char` seul soit signé ou non signé dépend de la plateforme ; si vous l'utilisez comme petit nombre, écrivez `signed char` ou `unsigned char` explicitement.

**Les réels** sont codés selon la norme IEEE 754 : un signe, un exposant et une mantisse. Conséquences importantes :

- Ils sont **approchés** : `0.1` n'a pas de représentation exacte en binaire. Le test `0.1 + 0.2 == 0.3` est faux.
- On **ne compare pas** deux réels avec `==` ; on teste que la différence est petite : `fabs(a - b) < 1e-9`.
- `float` offre environ 7 chiffres significatifs, `double` environ 15 à 16. **Utilisez `double` par défaut.**

### 4.3 Modificateurs : `signed`, `unsigned`, `short`, `long`

Les modificateurs ajustent un type entier :

- `signed` : le type peut représenter des valeurs négatives (comportement par défaut pour `int`).
- `unsigned` : le type ne représente que des valeurs positives ou nulles, mais sa plage positive double.
- `short`, `long`, `long long` : changent la taille.

```c
#include <stdio.h>

int main(void) {
    unsigned int positif = 4000000000u;      // suffixe u : littéral non signé
    signed char petit = -100;
    unsigned long long enorme = 18446744073709551615ULL;
    printf("positif = %u\n", positif);
    printf("petit   = %d\n", petit);
    printf("enorme  = %llu\n", enorme);
    return 0;
}
```

| Type | Plage (int sur 32 bits) |
| --- | --- |
| `int` | −2 147 483 648 à 2 147 483 647 |
| `unsigned int` | 0 à 4 294 967 295 |

Un entier signé sur *n* bits couvre −2^(n−1) à 2^(n−1)−1 (représentation en **complément à deux**). Un entier non signé couvre 0 à 2^n−1.

> **Attention** : le débordement d'un entier **signé** est un **comportement indéfini** (le compilateur peut supposer qu'il n'arrive jamais). Celui d'un entier **non signé** est défini : le résultat « boucle » modulo 2^n. Ainsi `UINT_MAX + 1` vaut `0`.

### 4.4 Entiers à taille fixe : `<stdint.h>`

Pour écrire du code **portable** ou manipuler des formats binaires, utilisez des types dont la taille est garantie :

| Type | Signification |
| --- | --- |
| `int8_t`, `int16_t`, `int32_t`, `int64_t` | Entiers signés de 8, 16, 32, 64 bits exactement |
| `uint8_t`, `uint16_t`, `uint32_t`, `uint64_t` | Entiers non signés correspondants |
| `int_least32_t`, `int_fast32_t` | Au moins 32 bits ; le plus petit / le plus rapide |
| `intptr_t`, `uintptr_t` | Entiers assez grands pour contenir un pointeur |
| `intmax_t`, `uintmax_t` | Plus grand entier disponible |
| `size_t` (`<stddef.h>`) | Taille ou indice (non signé) |
| `ptrdiff_t` (`<stddef.h>`) | Différence de deux pointeurs (signé) |

Pour les afficher de façon portable, `<inttypes.h>` fournit des macros : `PRId64`, `PRIu32`, `PRIx8`…

```c
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>

int main(void) {
    int32_t a = -42;
    uint64_t grand = 10000000000ULL;
    printf("a = %" PRId32 "\n", a);
    printf("grand = %" PRIu64 "\n", grand);
    printf("INT32_MAX = %" PRId32 "\n", INT32_MAX);
    return 0;
}
```

**Règle pratique** : `int` pour un compteur ordinaire ; `size_t` pour une taille ou un indice de tableau ; `int32_t`/`uint8_t`… dès que la taille exacte compte (fichiers, réseau, matériel).

### 4.5 Booléens

Historiquement, C n'avait **pas** de type booléen : toute expression numérique pouvait servir de condition. **Zéro est faux, toute autre valeur est vraie.** C99 a ajouté `_Bool` (et `<stdbool.h>` pour les noms `bool`, `true`, `false`) ; **C23** fait de `bool`, `true` et `false` des mots-clés.

```c
#include <stdbool.h>      // inutile en C23
#include <stdio.h>

int main(void) {
    bool pair = (10 % 2 == 0);
    bool grand = 5 > 100;
    printf("pair = %d, grand = %d\n", pair, grand);   // 1 et 0
    bool b = 42;               // toute valeur non nulle devient true (1)
    printf("b = %d\n", b);     // 1
    return 0;
}
```

Point important : convertir une valeur en `bool` donne **toujours 0 ou 1**, jamais autre chose. Les comparaisons (`==`, `<`, `&&`…) produisent un `int` valant 0 ou 1.

### 4.6 Déclarer, initialiser, affecter

```c
#include <stdio.h>

int main(void) {
    int a;                    // déclaration seule : valeur INDÉTERMINÉE
    int b = 10;               // initialisation
    int x = 1, y = 2, z;      // plusieurs déclarations sur une ligne (z non initialisé)
    a = 3;                    // affectation
    z = x + y;
    printf("a=%d b=%d x=%d y=%d z=%d\n", a, b, x, y, z);
    return 0;
}
```

Distinction essentielle : **initialiser** (donner une valeur à la naissance de la variable) n'est pas **affecter** (changer la valeur d'une variable existante). Pour les tableaux et structures, la différence est capitale : on peut initialiser avec `{ … }` mais pas affecter ainsi.

**Initialisation par défaut** : seules les variables **statiques ou globales** sont automatiquement mises à zéro. Les variables **locales** ne le sont pas. Dans le doute, initialisez toujours.

#### Inférence de type avec `auto` (C23)

```c
// Compiler avec : gcc -std=c23 inference.c -o inference
#include <stdio.h>

int main(void) {
    auto n = 42;          // int
    auto pi = 3.14;       // double
    auto c = 'x';         // int (en C, un littéral de caractère est de type int)
    printf("n = %d, pi = %.2f, c = %d\n", n, pi, c);
    return 0;
}
```

Le compilateur **déduit** le type depuis l'initialiseur. Il faut donc **obligatoirement** un initialiseur. Utilisez `auto` avec parcimonie : un type écrit explicitement documente mieux l'intention.

### 4.7 Conversions de types (*casts*)

Quand une expression mélange des types, le compilateur applique des **conversions implicites** selon des règles précises :

1. **Promotion des entiers** : `char` et `short` sont d'abord convertis en `int` dans les calculs.
2. **Conversions arithmétiques usuelles** : si les opérandes diffèrent, le plus « petit » est converti vers le plus « grand » (`int` → `long` → `long long` → `float` → `double` → `long double`). Entre signé et non signé de même rang, le **signé est converti en non signé**.
3. **Réel vers entier** : la partie décimale est **tronquée** (vers zéro).

```c
#include <stdio.h>

int main(void) {
    int a = 7, b = 2;
    double q1 = a / b;            // 3.0 : la division entière a lieu AVANT la conversion
    double q2 = (double)a / b;    // 3.5 : cast explicite d'un opérande
    int tronque = (int)3.99;      // 3
    printf("q1 = %.1f, q2 = %.1f, tronque = %d\n", q1, q2, tronque);

    int neg = -1;
    unsigned int u = 1;
    if (neg < u) printf("-1 < 1\n");
    else printf("surprise : -1 n'est pas < 1u (conversion en non signé)\n");
    return 0;
}
```

Le **cast** `(type)expression` force une conversion. Il supprime les avertissements : à utiliser en connaissance de cause, jamais pour « faire taire » le compilateur.

### 4.8 Bonnes pratiques

- Initialisez chaque variable à sa déclaration.
- Donnez à chaque variable la **portée la plus étroite** possible.
- Utilisez `double` pour les réels, `size_t` pour les tailles et indices, `bool` pour les conditions.
- Ne mélangez pas signé et non signé dans les comparaisons.
- Utilisez `<stdint.h>` quand la taille exacte importe.
- Ne comparez jamais des réels avec `==`.

## 5. Constantes et littéraux

### 5.1 Littéraux

Un **littéral** est une valeur écrite directement dans le code. Son **type** dépend de sa forme.

| Forme | Exemple | Type |
| --- | --- | --- |
| Entier décimal | `42` | `int` (ou plus grand si nécessaire) |
| Entier octal (préfixe `0`) | `052` | `int` (= 42) |
| Entier hexadécimal (`0x`) | `0x2A` | `int` (= 42) |
| Entier binaire (`0b`, C23) | `0b101010` | `int` (= 42) |
| Suffixes | `42u`, `42L`, `42UL`, `42LL`, `42ULL` | `unsigned`, `long`, `unsigned long`… |
| Réel | `3.14`, `1e-3`, `2.5f`, `2.5L` | `double`, `double`, `float`, `long double` |
| Caractère | `'A'` | `int` en C (valeur 65) |
| Chaîne | `"abc"` | `char[4]` (avec le `'\0'` final) |
| Booléen (C23) | `true`, `false` | `bool` |
| Pointeur nul (C23) | `nullptr` | `nullptr_t` |

En **C23**, le séparateur de chiffres `'` rend les grands nombres lisibles : `1'000'000`, `0xFF'FF`. Le zéro initial est un piège : `010` vaut **8** (octal), pas 10.

#### Séquences d'échappement

| Séquence | Signification |
| --- | --- |
| `\n` | Saut de ligne |
| `\t` | Tabulation |
| `\r` | Retour chariot |
| `\\` | Barre oblique inverse |
| `\'` | Apostrophe |
| `\"` | Guillemet |
| `\0` | Caractère nul (fin de chaîne) |
| `\a` | Alerte sonore |
| `\xHH` | Caractère de code hexadécimal HH |
| `\ooo` | Caractère de code octal ooo |

Pour afficher un `%` avec `printf`, écrivez `%%`.

### 5.2 Définir des constantes

Il y a quatre manières de nommer une constante, avec des différences réelles :

```c
#include <stdio.h>

#define TAILLE_MAX 100          // 1. macro : substitution textuelle, SANS type
const int LIMITE = 50;          // 2. variable en lecture seule, typée
enum { NB_JOURS = 7 };          // 3. constante entière d'énumération
// constexpr int N = 10;        // 4. (C23) vraie constante de compilation

int main(void) {
    printf("TAILLE_MAX = %d, LIMITE = %d, NB_JOURS = %d\n", TAILLE_MAX, LIMITE, NB_JOURS);
    return 0;
}
```

| Méthode | Typée ? | Portée respectée ? | Utilisable pour dimensionner un tableau ? |
| --- | --- | --- | --- |
| `#define` | Non | Non (texte global) | Oui |
| `const` | Oui | Oui | En C avant C23 : crée un VLA, pas une constante |
| `enum` | Entier | Oui | Oui |
| `constexpr` (C23) | Oui | Oui | Oui |

> **Bonne pratique** : préférez `constexpr` (C23), `enum` ou `const` à `#define` pour les constantes. Elles sont typées, respectent la portée et facilitent le débogage.

> **Attention** : en C avant C23, `const int n = 5; int t[n];` ne définit pas un tableau de taille constante mais un VLA (section 11.4). Une variable `const` n'est pas une « expression constante » en C, contrairement à C++.

Le qualificatif `const` demande au compilateur de **refuser toute modification**. Modifier malgré tout une variable déclarée `const` (par un cast) est un comportement indéfini.

### 5.3 `const` et pointeurs

Avec les pointeurs, `const` peut s'appliquer à **deux choses différentes** : ce qui est pointé, et le pointeur lui-même.

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

    // *p1 = 5;   // erreur : assignment of read-only location '*p1'
    // p2 = &y;   // erreur : assignment of read-only variable 'p2'
    // p3 = &y;   // erreur : assignment of read-only variable 'p3'
    return 0;
}
```

**Astuce de lecture** : lisez la déclaration **de droite à gauche**. `int *const p2` se lit « p2 est une constante (`const`), pointeur (`*`) vers un `int` ». `const int *p1` se lit « p1 est un pointeur vers un `int` constant ».

Les pointeurs sont étudiés en détail en section 13 ; retenez ici que `const` sur un paramètre pointeur (`const char *s`) **promet** que la fonction ne modifiera pas les données.

### 5.4 Constantes prédéfinies utiles

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

`CHAR_BIT` (`<limits.h>`) donne le nombre de bits d'un octet. `__FILE__`, `__LINE__` et `__func__` indiquent le fichier, la ligne et la fonction courants : précieux pour les messages de diagnostic.

## 6. Opérateurs et expressions

### 6.1 Expressions et catégories d'opérateurs

Une **expression** est une combinaison de valeurs, de variables et d'opérateurs qui produit une **valeur**. Une **instruction** est une expression suivie de `;`, exécutée pour son effet.

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

Règles à connaître :

- **Division** : si les deux opérandes sont entiers, le résultat est entier (tronqué vers zéro : `-7 / 2` vaut `-3`). Pour une division réelle, convertissez un des opérandes.
- **Modulo `%`** : reste de la division, réservé aux entiers. Le signe du reste suit celui du dividende : `-7 % 3` vaut `-1`.
- **Affectation composée** : `x += 3` équivaut à `x = x + 3` (mais `x` n'est évalué qu'une fois).
- **L'affectation est une expression** : `a = b = 0` est valide (associativité de droite à gauche).

### 6.2 Incrémentation : préfixe et suffixe

```c
#include <stdio.h>

int main(void) {
    int i = 5;
    int a = i++;    // a = 5, puis i = 6  (post-incrément : valeur avant)
    int b = ++i;    // i = 7, puis b = 7  (pré-incrément : valeur après)
    printf("a = %d, b = %d, i = %d\n", a, b, i);
    return 0;
}
```

Les deux formes augmentent la variable de 1. Elles diffèrent par la **valeur de l'expression** : `i++` vaut l'ancienne valeur, `++i` la nouvelle. Seule, l'instruction `i++;` ou `++i;` produit le même effet. Ne mélangez pas plusieurs modifications de la même variable dans une expression (voir 6.7).

### 6.3 Opérateurs logiques et évaluation paresseuse

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

- `&&` (ET) est vrai si **les deux** côtés sont vrais ; `||` (OU) l'est si **au moins un** l'est ; `!` inverse.
- **Court-circuit** : `&&` et `||` évaluent de gauche à droite et **s'arrêtent dès que le résultat est connu**. Avec `A && B`, si `A` est faux, `B` n'est **pas évalué**. On s'en sert pour protéger une opération dangereuse (`p != NULL && p->valeur > 0`).
- Le résultat est toujours `1` ou `0`.

### 6.4 Ternaire

```c
#include <stdio.h>

int main(void) {
    int a = 7, b = 2;
    int max = (a > b) ? a : b;
    printf("max = %d\n", max);
    return 0;
}
```

L'opérateur `condition ? valeur_si_vrai : valeur_si_faux` est une **expression** (contrairement à `if`, qui est une instruction). Il est pratique pour les choix simples ; ne l'imbriquez pas sur plusieurs niveaux, la lisibilité s'effondre.

### 6.5 `sizeof` et opérateur virgule

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

- `sizeof` est évalué **à la compilation** (sauf pour les VLA) et ne s'applique correctement au tableau que là où il est **déclaré**. Sur un paramètre de fonction déclaré `int t[]`, c'est la taille d'un **pointeur** (section 11.5).
- L'**opérateur virgule** évalue ses opérandes de gauche à droite et vaut le dernier. On le rencontre surtout dans les `for` : `for (i = 0, j = 9; i < j; i++, j--)`.

### 6.6 Priorité et associativité

La **priorité** dit quel opérateur s'applique en premier ; l'**associativité** départage ceux de même priorité. De la plus haute à la plus basse :

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

> **Attention** : piège classique : `x & 1 == 0` s'évalue comme `x & (1 == 0)`, car `==` est plus prioritaire que `&`. **Ajoutez des parenthèses** : `(x & 1) == 0`.

Dans le doute, parenthésez. Cela coûte peu et lève toute ambiguïté.

### 6.7 Comportements à éviter

Certaines expressions sont **valides syntaxiquement** mais **indéfinies** : la norme n'impose aucun résultat.

- **Dépassement d'entier signé** : `INT_MAX + 1`.
- **Division par zéro** (entière), et `INT_MIN / -1`.
- **Décalage invalide** : `1 << 40` sur un `int` de 32 bits, ou décalage par un nombre négatif.
- **Modifications non séquencées** : `tab[i] = i++;` ou `i = i++ + ++i;`. Une variable ne doit pas être modifiée deux fois (ni modifiée et lue) entre deux points de séquence.

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

static bool division_sure(int a, int b, int *resultat) {
    if (b == 0) {
        fprintf(stderr, "Erreur : division de %d par zéro (indéfini)\n", a);
        return false;
    }
    *resultat = a / b;
    return true;
}

int main(void) {
    int r;
    if (somme_sure(INT_MAX, 1, &r))   printf("somme = %d\n", r);     // erreur affichée
    if (division_sure(10, 0, &r))     printf("quotient = %d\n", r);  // erreur affichée
    if (somme_sure(2, 3, &r))         printf("somme = %d\n", r);     // cas valide : 5
    return 0;
}
```

La technique est toujours la même : **vérifier la condition avant** de faire l'opération, jamais après (après, il est trop tard : le comportement est déjà indéfini).

### 6.8 Arithmétique vérifiée (C23)

`<stdckdint.h>` détecte les débordements **sans comportement indéfini** : les fonctions `ckd_add`, `ckd_sub` et `ckd_mul` stockent le résultat dans une variable et **renvoient `true` s'il y a eu débordement**.

```c
// Compiler avec : gcc -std=c23 ckd.c -o ckd   (<stdckdint.h> : GCC 14+)
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
    if (ckd_mul(&resultat, 100000, 100000)) {
        fprintf(stderr, "Débordement à la multiplication !\n");
    }
    return 0;
}
```

C'est l'outil idéal pour calculer une taille d'allocation (`n * taille`) sans risque (section 29).

## 7. Entrées et sorties

### 7.1 Flux, tampons et fonctions d'E/S

En C, les entrées/sorties passent par des **flux** (*streams*) : des suites d'octets lues ou écrites séquentiellement. Trois flux sont ouverts automatiquement au lancement du programme (voir 7.5). Les fonctions de `<stdio.h>` utilisent des **tampons** (zones mémoire intermédiaires) : l'écriture sur le terminal est généralement **tamponnée par ligne** ; le texte n'apparaît donc qu'à la fin de la ligne (`\n`) ou lors d'un `fflush(stdout)`.

### 7.2 Affichage : `printf` et `puts`

```c
#include <stdio.h>

int main(void) {
    int age = 25;
    double taille = 1.756;
    char initiale = 'J';
    const char *nom = "Julie";
    printf("%s (%c) a %d ans et mesure %.2f m\n", nom, initiale, age, taille);
    puts("puts ajoute automatiquement un saut de ligne");
    return 0;
}
```

`printf(format, arguments…)` écrit le texte du **format** en remplaçant chaque **spécificateur** (`%…`) par l'argument correspondant, dans l'ordre. `puts(chaîne)` écrit une chaîne puis un `\n`.

#### Spécificateurs de format

| Spécificateur | Type attendu | Remarque |
| --- | --- | --- |
| `%d` / `%i` | `int` | Décimal signé |
| `%u` | `unsigned int` | Décimal non signé |
| `%ld` `%lld` | `long` `long long` |  |
| `%zu` | `size_t` | Pour `sizeof`, `strlen` |
| `%f` | `double` | Notation décimale (6 chiffres après la virgule par défaut) |
| `%e` / `%g` | `double` | Notation scientifique / la plus courte des deux |
| `%c` | `char` (ou `int`) | Un caractère |
| `%s` | `const char *` | Chaîne terminée par `'\0'` |
| `%p` | `void *` | Adresse (convertir avec `(void *)`) |
| `%x` / `%X` | `unsigned int` | Hexadécimal minuscule / majuscule |
| `%o` | `unsigned int` | Octal |
| `%%` | — | Le caractère `%` |

> **Attention** : le format doit **correspondre exactement** au type de l'argument. Un `%d` avec un `double`, ou un nombre d'arguments insuffisant, est un **comportement indéfini**. Activez `-Wall` : GCC vérifie les formats `printf` à la compilation.

#### Largeur, alignement, remplissage

```c
#include <stdio.h>

int main(void) {
    printf("[%5d]\n", 42);        // [   42]  largeur 5, aligné à droite
    printf("[%-5d]\n", 42);       // [42   ]  aligné à gauche
    printf("[%05d]\n", 42);       // [00042]  rempli de zéros
    printf("[%8.3f]\n", 3.14159); // [   3.142] largeur 8, 3 décimales
    printf("[%.3s]\n", "abcdef"); // [abc]  précision = nombre max de caractères
    printf("[%+d]\n", 7);         // [+7]  signe toujours affiché
    printf("[%*d]\n", 6, 42);     // [    42]  largeur passée en argument
    return 0;
}
```

Forme générale : `%[drapeaux][largeur][.précision][longueur]type`. Les drapeaux courants sont `-` (gauche), `0` (zéros), `+` (signe), ` ` (espace pour les positifs).

### 7.3 Lecture : `scanf`

```c
#include <stdio.h>

int main(void) {
    int age;
    double taille;
    char mot[32];
    printf("Entrez age, taille et un mot : ");
    if (scanf("%d %lf %31s", &age, &taille, mot) == 3) {
        printf("age=%d taille=%.2f mot=%s\n", age, taille, mot);
    } else {
        fprintf(stderr, "Saisie invalide\n");
        return 1;
    }
    return 0;
}
```

Règles fondamentales :

- **`&` obligatoire** devant les variables simples : `scanf` a besoin de leur **adresse** pour y écrire. Pour un tableau de `char`, le nom du tableau est déjà une adresse : pas de `&`.
- **Vérifiez la valeur de retour** : `scanf` renvoie le **nombre de conversions réussies**. Comparez-la au nombre attendu.
- **`%lf`** (et non `%f`) pour lire un `double` ; `%f` lirait un `float`.
- **Limitez toujours `%s`** avec une largeur : `%31s` pour un tableau de 32 octets (31 caractères + `'\0'`). Un `%s` sans limite permet un **dépassement de tampon**.
- Les espaces, tabulations et sauts de ligne sont des séparateurs : `%s` s'arrête au premier espace et ne lit donc pas une phrase.
- En cas d'échec de conversion, les caractères invalides **restent dans le tampon** et bloqueront les lectures suivantes (voir plus bas).

### 7.4 Lire une ligne : `fgets`

Pour lire une **ligne entière** de façon sûre, utilisez `fgets(tampon, taille, flux)`. Elle lit **au plus `taille − 1` caractères**, s'arrête après le `\n` (qu'elle **conserve**), et termine toujours par `'\0'`. Elle renvoie `NULL` en cas d'erreur ou de fin de fichier.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char ligne[64];
    printf("Votre nom complet : ");
    if (fgets(ligne, sizeof ligne, stdin) == NULL) {
        return 1;                                  // fin de fichier ou erreur
    }
    ligne[strcspn(ligne, "\n")] = '\0';           // supprime le '\n' final s'il existe
    printf("Bonjour, %s !\n", ligne);
    return 0;
}
```

`strcspn(ligne, "\n")` renvoie la position du premier `\n` (ou la longueur de la chaîne s'il n'y en a pas) : idiome sûr pour retirer le saut de ligne.

> **Attention** : **`gets()` n'existe plus** (supprimée en C11) car elle ne permet pas de limiter la taille lue : elle est la cause de failles historiques célèbres. N'utilisez jamais `gets`.

#### Lecture sûre d'un nombre

Le schéma recommandé est **`fgets` puis `strtol` / `strtod`**, qui permet de détecter les erreurs précisément :

```c
#include <errno.h>
#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

static bool lire_entier(const char *invite, int *resultat) {
    char ligne[64];
    printf("%s", invite);
    if (fgets(ligne, sizeof ligne, stdin) == NULL) return false;

    char *fin;
    errno = 0;
    long v = strtol(ligne, &fin, 10);
    if (fin == ligne) return false;                       // aucun chiffre lu
    if (*fin != '\n' && *fin != '\0') return false;       // caractères parasites
    if (errno == ERANGE || v < INT_MIN || v > INT_MAX) return false;   // hors plage
    *resultat = (int)v;
    return true;
}

int main(void) {
    int n;
    if (lire_entier("Entrez un entier : ", &n)) printf("Vous avez saisi %d\n", n);
    else fprintf(stderr, "Saisie invalide\n");
    return 0;
}
```

Pourquoi c'est meilleur que `scanf("%d")` : la ligne est **toujours consommée en entier** (pas de reste dans le tampon), et chaque type d'erreur est distinguable.

#### Vider le tampon d'entrée

Quand on mélange `scanf` et `fgets`, un `\n` resté dans le tampon fait que `fgets` lit une ligne vide. Pour vider jusqu'à la fin de la ligne :

```c
#include <stdio.h>

static void vider_tampon(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) { }
}

int main(void) {
    int n;
    char nom[32];
    printf("Un entier : ");
    if (scanf("%d", &n) != 1) return 1;
    vider_tampon();                          // consomme le '\n' laissé par scanf
    printf("Un nom : ");
    if (fgets(nom, sizeof nom, stdin) == NULL) return 1;
    printf("n = %d, nom = %s", n, nom);
    return 0;
}
```

Notez que `c` est un **`int`**, pas un `char` : `EOF` est une valeur négative qui ne tiendrait pas toujours dans un `char`. **N'écrivez jamais `fflush(stdin)`** : son comportement est indéfini en C standard.

### 7.5 Autres fonctions d'E/S

| Fonction | Rôle |
| --- | --- |
| `putchar(c)` / `getchar()` | Écrire / lire **un caractère** (`getchar` renvoie un `int`) |
| `fputs(s, flux)` | Écrire une chaîne **sans** ajouter de `\n` |
| `fprintf(flux, …)` / `fscanf(flux, …)` | `printf` / `scanf` sur un flux quelconque |
| `snprintf(tampon, n, …)` | `printf` **vers une chaîne**, avec limite de taille |
| `sscanf(chaîne, …)` | `scanf` **depuis une chaîne** |
| `fflush(flux)` | Force l'écriture du tampon (sur un flux de sortie) |

```c
#include <stdio.h>

int main(void) {
    char message[64];
    int n = snprintf(message, sizeof message, "Score : %d/%d", 17, 20);
    printf("%s (%d caractères écrits)\n", message, n);

    int a, b;
    if (sscanf("12 34", "%d %d", &a, &b) == 2) printf("a=%d b=%d\n", a, b);
    return 0;
}
```

`snprintf` n'écrit jamais plus de `n` octets (zéro final compris) et **renvoie le nombre de caractères qui auraient été écrits** : si le résultat est ≥ `n`, la sortie a été tronquée. Elle remplace avantageusement `sprintf`, qui n'a aucune limite.

### 7.6 Flux standard

| Flux | Rôle | Défaut |
| --- | --- | --- |
| `stdin` | Entrée standard | Clavier |
| `stdout` | Sortie standard | Écran (tamponné) |
| `stderr` | Sortie d'erreur | Écran (**non tamponné**) |

La séparation `stdout`/`stderr` permet de **rediriger** la sortie sans perdre les erreurs : `./prog > resultat.txt 2> erreurs.txt`. Les messages d'erreur doivent donc aller sur `stderr`.

### 7.7 Erreurs courantes

| Erreur | Conséquence | Solution |
| --- | --- | --- |
| Oubli du `&` dans `scanf("%d", n)` | Écriture à une adresse invalide | `scanf("%d", &n)` |
| `%s` sans limite | Dépassement de tampon | `%31s` ou `fgets` |
| `%f` au lieu de `%lf` dans `scanf` | Valeur fausse | `%lf` pour `double` |
| Valeur de retour de `scanf` ignorée | Variable non initialisée utilisée | Tester `== nombre attendu` |
| `printf(texte_utilisateur)` | **Faille de chaîne de format** | `printf("%s", texte)` |
| `\n` oublié, `stdout` tamponné | Texte qui n'apparaît pas | `\n` ou `fflush(stdout)` |

## 8. Structures de contrôle

Par défaut, les instructions s'exécutent **dans l'ordre**. Les structures de contrôle permettent de **choisir** (conditions) et de **répéter** (boucles).

### 8.1 Conditions : `if`, `else if`, `else`

```c
#include <stdio.h>

int main(void) {
    int note = 14;
    if (note >= 16) {
        printf("Très bien\n");
    } else if (note >= 12) {
        printf("Bien\n");
    } else if (note >= 10) {
        printf("Passable\n");
    } else {
        printf("Insuffisant\n");
    }
    return 0;
}
```

La condition est une **expression** : nulle = faux, non nulle = vrai. Les branches sont testées **dans l'ordre** et seule la première vraie s'exécute. **Mettez toujours des accolades**, même pour une seule instruction : sans elles, l'ajout d'une seconde ligne ne la place pas dans la branche (faille célèbre d'Apple, « goto fail »).

**Le « else pendant »** : un `else` se rattache au **`if` le plus proche**, quelle que soit l'indentation. Les accolades lèvent l'ambiguïté.

### 8.2 `switch`

```c
#include <stdio.h>

int main(void) {
    int jour = 3;
    switch (jour) {
        case 1: puts("Lundi"); break;
        case 2: puts("Mardi"); break;
        case 3: puts("Mercredi"); break;
        case 6:
        case 7: puts("Week-end"); break;     // plusieurs étiquettes pour un même traitement
        default: puts("Jour inconnu"); break;
    }
    return 0;
}
```

Fonctionnement et pièges :

- L'expression doit être de **type entier** (`int`, `char`, `enum`…), jamais une chaîne ni un réel.
- Chaque `case` porte une **constante** entière, distincte des autres.
- L'exécution **saute** à l'étiquette correspondante puis **continue** jusqu'au prochain `break` : c'est le **passage en cascade** (*fallthrough*). Oublier un `break` est une erreur très fréquente ; quand le passage est voulu, signalez-le avec `[[fallthrough]];` (C23) ou un commentaire.
- `default` traite tous les autres cas ; il est conseillé de toujours le prévoir.
- Une déclaration de variable juste après une étiquette `case` pose problème : encadrez le corps du `case` d'accolades.

### 8.3 Boucles

```c
#include <stdio.h>

int main(void) {
    // while : teste AVANT chaque tour (peut ne jamais s'exécuter)
    int i = 0;
    while (i < 3) { printf("while %d\n", i); i++; }

    // do … while : teste APRÈS (s'exécute au moins une fois)
    int j = 10;
    do { printf("do-while %d\n", j); j++; } while (j < 3);

    // for : initialisation ; condition ; progression
    for (int k = 0; k < 3; k++) { printf("for %d\n", k); }
    return 0;
}
```

| Boucle | Quand l'utiliser |
| --- | --- |
| `for` | Nombre d'itérations **connu** ou compteur évident |
| `while` | Répétition \*\*tant qu'\*\*une condition tient, éventuellement zéro fois |
| `do … while` | Corps à exécuter **au moins une fois** (menu, validation de saisie) |

La boucle `for (init; cond; progression)` équivaut à : `init; while (cond) { corps; progression; }`. Chacune des trois parties est **facultative**. Depuis C99, la variable déclarée dans l'en-tête (`int k`) n'existe que **dans la boucle**.

#### Boucle infinie

```c
for (;;) {            // idiome classique ; équivalent : while (1)
    // … sortie par break ou return
}
```

Une boucle infinie est légitime quand la sortie se fait par `break` ou `return` (boucle d'événements, serveur, menu).

### 8.4 `break`, `continue`, `goto`

```c
#include <stdio.h>

int main(void) {
    for (int i = 0; i < 10; i++) {
        if (i == 2) continue;       // passe directement à l'itération suivante
        if (i == 5) break;          // quitte immédiatement la boucle
        printf("%d ", i);           // affiche 0 1 3 4
    }
    printf("\n");
    return 0;
}
```

- **`break`** quitte la boucle (ou le `switch`) **la plus interne**.
- **`continue`** abandonne le reste du tour courant et passe au suivant (dans un `for`, la progression est exécutée).
- **`goto etiquette;`** saute à une étiquette de la même fonction. Son usage est **déconseillé** sauf dans deux cas légitimes : **sortir de boucles imbriquées** et **centraliser le nettoyage en cas d'erreur** :

```c
#include <stdio.h>
#include <stdlib.h>

int traiter(void) {
    int code = -1;
    char *a = malloc(100);
    char *b = malloc(200);
    if (a == NULL || b == NULL) goto fin;     // un seul point de sortie
    /* … travail … */
    code = 0;
fin:
    free(b);                                  // free(NULL) est sans danger
    free(a);
    return code;
}

int main(void) { return traiter() == 0 ? 0 : 1; }
```

### 8.5 Boucles imbriquées

```c
#include <stdio.h>

int main(void) {
    for (int l = 1; l <= 3; l++) {          // lignes
        for (int c = 1; c <= 4; c++) {      // colonnes
            printf("%3d", l * c);
        }
        printf("\n");
    }
    return 0;
}
```

La boucle interne s'exécute **entièrement** à chaque tour de la boucle externe : 3 × 4 = 12 passages. Un `break` dans la boucle interne ne quitte **que** celle-ci. Le nombre d'opérations croît comme le **produit** des bornes : prudence avec trois niveaux ou plus.

### 8.6 Pièges classiques

| Piège | Exemple | Explication |
| --- | --- | --- |
| `;` après la condition | `if (x > 0); { … }` | Le `;` est le corps (vide) ; le bloc s'exécute toujours |
| `=` pour `==` | `if (x = 0)` | Affecte 0 puis teste : toujours faux |
| Erreur d'une unité | `for (i = 0; i <= n; i++)` sur un tableau de `n` éléments | Dernier indice valide : `n − 1` |
| Boucle sans progression | `while (i < 10) { … }` sans `i++` | Boucle infinie |
| Compteur non signé | `for (size_t i = n; i >= 0; i--)` | `i >= 0` est **toujours vrai** pour un non signé |
| `switch` sans `break` |  | Passage involontaire au cas suivant |
| Réel comme compteur | `for (double x = 0; x != 1; x += 0.1)` | Erreurs d'arrondi : ne s'arrête jamais |

Pour parcourir un tableau à l'envers avec un indice non signé : `for (size_t i = n; i-- > 0; )`.

## 9. Fonctions

### 9.1 Pourquoi des fonctions ?

Une **fonction** est un bloc de code nommé, réutilisable, qui reçoit éventuellement des **paramètres** et renvoie éventuellement une **valeur**. Elle sert à :

- **Découper** un problème complexe en sous-problèmes simples.
- **Éviter la duplication** : on écrit le code une fois, on l'appelle partout.
- **Tester** et **documenter** chaque morceau isolément.
- **Abstraire** : l'appelant n'a besoin de connaître que ce que la fonction fait, pas comment.

### 9.2 Définir et appeler

```c
#include <stdio.h>

// Prototype (déclaration) : type de retour, nom, types des paramètres
int maximum(int a, int b);
void saluer(const char *nom);

int main(void) {
    int m = maximum(7, 12);          // appel : 7 et 12 sont les ARGUMENTS
    printf("max = %d\n", m);
    saluer("Julie");
    return 0;
}

// Définition : a et b sont les PARAMÈTRES
int maximum(int a, int b) {
    return (a > b) ? a : b;
}

void saluer(const char *nom) {
    printf("Bonjour, %s !\n", nom);   // void : aucune valeur retournée
}
```

Vocabulaire précis :

- **Paramètre** : variable locale de la fonction, déclarée dans sa définition (`a`, `b`).
- **Argument** : valeur fournie à l'appel (`7`, `12`).
- **Prototype** : déclaration sans corps, terminée par `;`. Il permet d'appeler une fonction **avant** sa définition et permet au compilateur de **vérifier** le nombre et le type des arguments.
- **`return expr;`** termine la fonction et renvoie la valeur, convertie vers le type de retour. Dans une fonction `void`, `return;` seul est permis.
- Une fonction **sans paramètre** se déclare `f(void)`. Écrire `f()` (avant C23) désactive la vérification des arguments.

> **Attention** : ne pas oublier le `return` dans une fonction non `void` : utiliser la valeur d'une fonction qui ne retourne rien est un comportement indéfini (sauf pour `main`).

### 9.3 Passage des arguments : toujours **par valeur**

En C, les arguments sont **copiés** dans les paramètres. Modifier un paramètre ne modifie **pas** la variable de l'appelant.

```c
#include <stdio.h>

void echanger_faux(int a, int b) {       // travaille sur des COPIES
    int t = a; a = b; b = t;
}

void echanger(int *a, int *b) {          // reçoit des ADRESSES
    int t = *a; *a = *b; *b = t;
}

int main(void) {
    int x = 1, y = 2;
    echanger_faux(x, y);
    printf("après echanger_faux : x=%d y=%d\n", x, y);   // 1 2 : inchangés
    echanger(&x, &y);
    printf("après echanger       : x=%d y=%d\n", x, y);   // 2 1
    return 0;
}
```

Pour **simuler** un passage par référence, on passe l'**adresse** de la variable (`&x`) ; la fonction reçoit un **pointeur** (copie de l'adresse) et modifie l'original par `*a`. Les pointeurs sont étudiés en section 13.

**Cas des tableaux** : un tableau passé à une fonction est **converti en pointeur** vers son premier élément ; la fonction travaille donc sur le tableau **original** et ne connaît pas sa taille. On passe toujours la taille en paramètre séparé :

```c
int somme(const int *t, size_t n);    // équivalent à : int somme(const int t[], size_t n)
```

**Cas des structures** : elles sont copiées en entier. Pour de grosses structures, passez un pointeur (`const struct S *`) pour éviter la copie.

**Plusieurs valeurs de retour** : une fonction ne renvoie qu'une valeur. Pour en produire plusieurs, utilisez des pointeurs de sortie ou une structure :

```c
#include <stdbool.h>
#include <stdio.h>

static bool diviser(int a, int b, int *quotient, int *reste) {
    if (b == 0) return false;            // code d'erreur
    *quotient = a / b;
    *reste = a % b;
    return true;
}

int main(void) {
    int q, r;
    if (diviser(17, 5, &q, &r)) printf("17 = 5 * %d + %d\n", q, r);
    return 0;
}
```

### 9.4 Plusieurs fichiers : en-têtes et sources

Dès qu'un programme grossit, on le répartit en **modules** : un fichier **`.h`** (interface : prototypes, types, constantes) et un fichier **`.c`** (implémentation).

```c
// maths.h : l'interface
#ifndef MATHS_H
#define MATHS_H

int carre(int x);
int cube(int x);

#endif
```

```c
// maths.c : l'implémentation
#include "maths.h"

int carre(int x) { return x * x; }
int cube(int x)  { return x * x * x; }
```

```c
// main.c : l'utilisateur du module
#include <stdio.h>
#include "maths.h"

int main(void) {
    printf("carre(4) = %d, cube(3) = %d\n", carre(4), cube(3));
    return 0;
}
```

```bash
gcc -Wall -Wextra -std=c17 main.c maths.c -o programme
```

- On inclut les en-têtes du système avec `<…>` et les vôtres avec `"…"`.
- Les **gardes d'inclusion** (`#ifndef … #define … #endif`) empêchent qu'un en-tête soit inclus deux fois (section 24.5).
- Une fonction **`static`** au niveau du fichier est **privée** à ce fichier (liaison interne) : elle ne peut pas être appelée depuis un autre `.c`.
- Mettez dans le `.h` les **déclarations**, pas les définitions de fonctions ni de variables : sinon l'éditeur de liens signalera des définitions multiples.

### 9.5 Fonctions variadiques

Certaines fonctions acceptent un **nombre variable d'arguments** (`printf`). On les déclare avec `...` et on utilise `<stdarg.h>` :

```c
#include <stdarg.h>
#include <stdio.h>

static int somme(int n, ...) {          // n = nombre d'arguments qui suivent
    va_list args;
    va_start(args, n);                  // initialise la lecture après le dernier paramètre nommé
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += va_arg(args, int);     // lit le prochain argument, en précisant son type
    }
    va_end(args);                       // nettoyage obligatoire
    return total;
}

int main(void) {
    printf("%d\n", somme(3, 10, 20, 30));   // 60
    return 0;
}
```

Le compilateur **ne vérifie ni le nombre ni le type** des arguments variables : c'est à vous de les connaître (par un compteur, une valeur sentinelle ou une chaîne de format). Une erreur est un comportement indéfini. Les arguments `char` et `short` sont promus en `int`, et `float` en `double`, ce qui impose `va_arg(args, int)` et `va_arg(args, double)`.

### 9.6 Fonctions et mémoire : points d'attention

- **Ne retournez jamais l'adresse d'une variable locale** : elle disparaît à la sortie de la fonction (section 15).
- Les **paramètres et variables locales** vivent sur la **pile** ; une fonction qui appelle une autre empile un nouveau cadre. Les très gros tableaux locaux ou une récursion trop profonde provoquent un **débordement de pile**.
- Un paramètre **pointeur** doit être validé (`!= NULL`) si la fonction peut le recevoir nul.
- Documentez qui **possède** la mémoire pointée et si la fonction la modifie (`const` pour le dire).

### 9.7 Bonnes pratiques

- Une fonction fait **une seule chose** et tient sur un écran.
- Nom d'un **verbe** pour une action (`calculer_moyenne`), d'un **prédicat** pour un test (`est_premier`).
- Déclarez les paramètres d'entrée **`const`** quand ils ne sont pas modifiés.
- Retournez un **code d'erreur** ou un booléen et vérifiez-le côté appelant.
- Évitez les **effets de bord** cachés (variables globales modifiées).
- Écrivez un **prototype** pour chaque fonction partagée, dans un `.h`.

## 10. Portée et durée de vie des variables

Deux notions distinctes, souvent confondues :

- La **portée** (*scope*) : **où dans le code** un nom est visible.
- La **durée de vie** (*lifetime*) : **pendant combien de temps** l'objet existe en mémoire à l'exécution.

### 10.1 Les portées

| Portée | Où | Visible… |
| --- | --- | --- |
| **Bloc** | Variable déclarée dans `{ }` (ou dans l'en-tête d'un `for`) | Du point de déclaration à la fin du bloc |
| **Fonction** | Étiquettes de `goto` | Dans toute la fonction |
| **Prototype** | Noms de paramètres d'un prototype | Dans ce prototype seulement |
| **Fichier** | Déclaration en dehors de toute fonction | Du point de déclaration à la fin du fichier |

```c
#include <stdio.h>

int globale = 100;                    // portée : fichier

int main(void) {
    int x = 1;                        // portée : bloc de main
    {
        int x = 2;                    // MASQUE le x extérieur (shadowing)
        printf("x interne = %d\n", x);    // 2
    }
    printf("x externe = %d\n", x);        // 1
    for (int i = 0; i < 2; i++) { }       // i n'existe que dans la boucle
    printf("globale = %d\n", globale);
    return 0;
}
```

Quand un nom interne **masque** un nom externe, le nom externe reste inaccessible dans le bloc interne. Ce **masquage** est source de confusion : `-Wshadow` le signale.

### 10.2 Classes de stockage et durée de vie

| Mot-clé | Effet | Durée de vie |
| --- | --- | --- |
| *(aucun)* / `auto` | Variable locale ordinaire | **Automatique** : du bloc à sa sortie ; **pile** ; **non initialisée** |
| `static` (local) | Variable locale **persistante** | **Statique** : tout le programme ; initialisée **une seule fois** (à 0 par défaut) |
| `static` (global) | Nom **privé au fichier** | Statique ; liaison interne |
| `extern` | Déclare une variable **définie ailleurs** | Statique ; liaison externe |
| `register` | Suggestion historique : garder en registre | Automatique ; on ne peut pas prendre son adresse ; **ignoré** par les compilateurs modernes |
| `thread_local` (C23) | Une copie **par fil d'exécution** | Celle du fil |

```c
#include <stdio.h>

int compter(void) {
    static int n = 0;      // initialisée UNE fois ; conserve sa valeur entre les appels
    n++;
    return n;
}

int main(void) {
    for (int i = 0; i < 3; i++) printf("appel %d\n", compter());   // 1, 2, 3
    return 0;
}
```

Pour partager une variable globale entre fichiers :

```c
// config.c
int niveau_debug = 0;              // DÉFINITION (une seule, dans un seul .c)

// config.h
extern int niveau_debug;           // DÉCLARATION (incluse partout)
```

**Initialisation** : les variables à durée **statique** (globales et `static`) sont mises à **zéro** par défaut ; les variables **automatiques** ne sont **pas** initialisées. Un initialiseur de variable statique doit être une **expression constante**.

### 10.3 Organisation de la mémoire d'un programme

Un processus en cours d'exécution dispose de plusieurs zones :

| Zone | Contenu | Particularités |
| --- | --- | --- |
| **Code** (*text*) | Instructions machine | Lecture seule |
| **Données initialisées** | Globales et statiques avec valeur initiale non nulle | Lues du fichier exécutable |
| **BSS** | Globales et statiques initialisées à zéro | Mises à zéro au démarrage |
| **Tas** (*heap*) | Mémoire allouée par `malloc` | Gérée **manuellement**, croît vers les adresses hautes |
| **Pile** (*stack*) | Variables locales, paramètres, adresses de retour | Gérée **automatiquement** ; taille limitée (souvent 8 Mo sous Linux) |
| **Littéraux de chaîne** | `"texte"` | En lecture seule : les modifier est indéfini |

```c
#include <stdio.h>
#include <stdlib.h>

int globale = 42;                       // données initialisées
int zero;                               // BSS

int main(void) {
    int locale = 1;                     // pile
    int *dyn = malloc(sizeof *dyn);     // tas (l'objet pointé) ; dyn lui-même est sur la pile
    const char *s = "littéral";         // s sur la pile ; le texte en zone en lecture seule
    if (dyn == NULL) return 1;
    printf("globale=%p locale=%p dyn=%p s=%p\n",
           (void *)&globale, (void *)&locale, (void *)dyn, (void *)s);
    free(dyn);
    return 0;
}
```

Retenez le contraste fondamental : la **pile** se gère toute seule mais est **éphémère** (les objets disparaissent à la sortie du bloc) ; le **tas** est **durable** mais **vous** devez le libérer.

### 10.4 Bonnes pratiques

- **Réduisez la portée** : déclarez au plus près de l'usage.
- **Évitez les variables globales** : elles créent des dépendances cachées, empêchent les tests et sont dangereuses avec plusieurs fils d'exécution. Si nécessaire, rendez-les `static` (privées au fichier).
- N'utilisez `static` local que pour de l'état volontairement persistant (compteur, cache), en sachant que la fonction n'est alors **plus réentrante**.
- Évitez le **masquage** de noms ; compilez avec `-Wshadow`.
- **Ne retournez jamais** un pointeur vers une variable automatique.

## Synthèse du niveau débutant

Vous maîtrisez maintenant le socle du langage : produire un exécutable (1–2), écrire du code valide (3), choisir et convertir des types (4), nommer des constantes (5), construire des expressions sans comportement indéfini (6), dialoguer avec l'utilisateur (7), organiser le flux d'exécution (8), structurer en fonctions et en modules (9) et raisonner sur la portée et la mémoire (10).

**À suivre — niveau intermédiaire** : tableaux (11), chaînes (12), pointeurs (13), allocation dynamique (14), structures de données (15–17), `struct`/`union`/`enum`/`typedef` (18–20) et pointeurs de fonctions (21).

# Niveau intermédiaire

## 11. Tableaux

### 11.1 Principe

Un **tableau** est une suite d'éléments **de même type**, stockés **côte à côte** (de façon contiguë) en mémoire et accessibles par un **indice**. Les indices commencent à **0** : un tableau de `n` éléments a pour indices valides `0` à `n − 1`. L'élément d'indice `i` se trouve à l'adresse `début + i × taille_élément`, ce qui rend l'accès **instantané**, quel que soit `i`.

### 11.2 Déclarer et initialiser

```c
#include <stdio.h>

int main(void) {
    int a[5];                          // 5 éléments NON initialisés (valeurs indéterminées)
    int b[5] = {1, 2, 3, 4, 5};        // initialisation complète
    int c[5] = {1, 2};                 // les éléments restants valent 0 : {1, 2, 0, 0, 0}
    int d[5] = {0};                    // tout à zéro (idiome classique)
    int e[] = {10, 20, 30};            // taille déduite : 3
    int f[6] = { [1] = 7, [4] = 9 };   // initialisation désignée (C99) : {0, 7, 0, 0, 9, 0}
    int g[5] = {};                     // tout à zéro (C23)

    a[0] = 42;
    printf("b[2] = %d, c[3] = %d, e a %zu éléments, f[4] = %d\n",
           b[2], c[3], sizeof e / sizeof e[0], f[4]);
    (void)d; (void)g;
    return 0;
}
```

Points essentiels :

- Un tableau **local** non initialisé contient des valeurs indéterminées ; un tableau **global ou `static`** est mis à zéro.
- Si l'initialiseur est **plus court** que le tableau, le reste est mis à **zéro** ; s'il est **plus long**, c'est une erreur.
- **On ne peut pas affecter un tableau** entier avec `=` (`a = b;` est une erreur) ni le comparer avec `==` (on comparerait des adresses). Pour copier : `memcpy` ; pour comparer : `memcmp` ou une boucle.
- La taille doit être connue : constante (ou VLA, voir 11.5).

### 11.3 Parcourir

```c
#include <stdio.h>

int main(void) {
    int t[] = {4, 8, 15, 16, 23, 42};
    size_t n = sizeof t / sizeof t[0];       // nombre d'éléments
    int somme = 0;
    for (size_t i = 0; i < n; i++) {
        printf("t[%zu] = %d\n", i, t[i]);
        somme += t[i];
    }
    printf("somme = %d, moyenne = %.2f\n", somme, (double)somme / n);
    return 0;
}
```

> **Attention** : le C **ne vérifie pas les bornes**. Écrire `t[6]` ou `t[-1]` est un comportement indéfini : il peut écraser une autre variable, planter, ou sembler fonctionner. C'est le **dépassement de tampon**, première cause de failles de sécurité du langage. Contrôlez toujours vos indices.

### 11.4 Tableaux multidimensionnels

```c
#include <stdio.h>

int main(void) {
    int m[2][3] = { {1, 2, 3},
                    {4, 5, 6} };            // 2 lignes, 3 colonnes
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) printf("%3d", m[i][j]);
        printf("\n");
    }
    return 0;
}
```

En mémoire, un tableau 2D est un **tableau de tableaux**, rangé **ligne par ligne** (*row-major*) : `m[0][0], m[0][1], m[0][2], m[1][0]…`. Parcourir **ligne par ligne** (boucle interne sur la colonne) est plus rapide, car il suit l'ordre de la mémoire et exploite le cache du processeur.

### 11.5 Tableaux à taille variable (VLA)

Depuis C99, la taille d'un tableau local peut être une **variable** :

```c
#include <stdio.h>

int main(void) {
    int n = 5;
    int t[n];                          // VLA : taille déterminée à l'exécution
    for (int i = 0; i < n; i++) t[i] = i * i;
    printf("t[4] = %d\n", t[4]);
    return 0;
}
```

Les VLA vivent sur la **pile** : une taille trop grande provoque un débordement de pile **sans aucun moyen de le détecter**. Ils ne peuvent pas être initialisés avec `{…}`. Ils sont devenus **facultatifs** en C11 (certains compilateurs, dont MSVC, ne les supportent pas). Pour une taille inconnue ou grande, préférez `malloc` (section 14).

### 11.6 Tableaux et fonctions

Un tableau passé à une fonction est **converti en pointeur vers son premier élément** (on dit qu'il se *dégrade*). La fonction ne connaît **pas** sa taille :

```c
#include <stdio.h>

static int somme(const int t[], size_t n) {      // t est en réalité un const int *
    int s = 0;
    for (size_t i = 0; i < n; i++) s += t[i];
    return s;
}

static void doubler(int t[], size_t n) {          // modifie le tableau ORIGINAL
    for (size_t i = 0; i < n; i++) t[i] *= 2;
}

int main(void) {
    int t[] = {1, 2, 3, 4};
    size_t n = sizeof t / sizeof t[0];            // valable ici : t est un vrai tableau
    doubler(t, n);
    printf("somme = %d\n", somme(t, n));         // 20
    return 0;
}
```

> **Attention** : dans `somme`, `sizeof t` vaudrait la taille d'un **pointeur** (8 octets), pas celle du tableau. **Passez toujours la taille** en paramètre. Pour un tableau 2D, toutes les dimensions sauf la première doivent être précisées : `void f(int m[][3], size_t lignes)`.

### 11.7 Opérations courantes

```c
#include <stdio.h>

static int maximum(const int *t, size_t n) {
    int max = t[0];                       // précondition : n >= 1
    for (size_t i = 1; i < n; i++) if (t[i] > max) max = t[i];
    return max;
}

// Recherche linéaire : renvoie l'indice, ou -1 si absent
static long chercher(const int *t, size_t n, int x) {
    for (size_t i = 0; i < n; i++) if (t[i] == x) return (long)i;
    return -1;
}

static void inverser(int *t, size_t n) {
    for (size_t i = 0; i < n / 2; i++) {
        int tmp = t[i]; t[i] = t[n - 1 - i]; t[n - 1 - i] = tmp;
    }
}

int main(void) {
    int t[] = {5, 3, 9, 1};
    printf("max = %d, indice de 9 = %ld\n", maximum(t, 4), chercher(t, 4, 9));
    inverser(t, 4);
    for (int i = 0; i < 4; i++) printf("%d ", t[i]);
    printf("\n");
    return 0;
}
```

#### Tri avec `qsort`

La bibliothèque standard fournit un tri générique. Il reçoit le tableau, le nombre d'éléments, la taille d'un élément et une **fonction de comparaison** (pointeur de fonction, section 21) :

```c
#include <stdio.h>
#include <stdlib.h>

static int comparer(const void *pa, const void *pb) {
    int a = *(const int *)pa, b = *(const int *)pb;
    return (a > b) - (a < b);            // -1, 0 ou 1 ; évite le débordement de a - b
}

int main(void) {
    int t[] = {42, 7, 19, 3, 88};
    size_t n = sizeof t / sizeof t[0];
    qsort(t, n, sizeof t[0], comparer);
    for (size_t i = 0; i < n; i++) printf("%d ", t[i]);
    printf("\n");
    int cle = 19;
    int *p = bsearch(&cle, t, n, sizeof t[0], comparer);   // recherche dichotomique (tableau trié)
    printf(p ? "trouvé\n" : "absent\n");
    return 0;
}
```

La fonction de comparaison renvoie un nombre **négatif, nul ou positif** selon que le premier élément est inférieur, égal ou supérieur au second. N'écrivez pas `return a - b;` : la soustraction peut déborder.

### 11.8 Erreurs courantes

| Erreur | Conséquence |
| --- | --- |
| Indice hors bornes (`t[n]`, `<=` dans une boucle) | Comportement indéfini, corruption de mémoire |
| `sizeof` sur un paramètre tableau | Donne la taille d'un pointeur |
| `a = b` entre tableaux | Erreur de compilation |
| Comparer deux tableaux avec `==` | Compare des adresses, pas des contenus |
| Lire un tableau local non initialisé | Valeurs indéterminées |
| VLA trop grand | Débordement de pile |

## 12. Chaînes de caractères

### 12.1 Définition

En C, il n'y a **pas de type chaîne**. Une **chaîne** est un **tableau de `char`** dont la fin est marquée par le caractère nul **`'\0'`** (valeur 0). Une chaîne de *n* caractères occupe donc **n + 1 octets**.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char a[] = "Salut";                   // tableau de 6 char : 'S','a','l','u','t','\0' ; MODIFIABLE
    char b[10] = "Hi";                    // 'H','i','\0' puis des zéros
    char c[] = {'O', 'k', '\0'};          // équivalent à "Ok"
    const char *d = "Littéral";           // pointeur vers un littéral : LECTURE SEULE

    a[0] = 's';                           // OK : a est une copie modifiable
    // d[0] = 'l';                        // comportement indéfini : littéral non modifiable
    printf("%s %s %s %s\n", a, b, c, d);
    printf("strlen(a) = %zu, sizeof a = %zu\n", strlen(a), sizeof a);   // 5 et 6
    return 0;
}
```

Distinction capitale entre :

- `char a[] = "…"` : un **tableau** modifiable, copie du littéral ;
- `const char *d = "…"` : un **pointeur** vers un littéral, **en lecture seule** (le déclarer `const` permet au compilateur de détecter les modifications).

> **Attention** : oublier le `'\0'` (ou ne pas prévoir sa place) fait que toutes les fonctions de chaîne lisent **au-delà** du tableau jusqu'à trouver un zéro quelque part en mémoire. C'est un comportement indéfini.

### 12.2 Fonctions de `<string.h>`

| Fonction | Rôle | Remarque |
| --- | --- | --- |
| `strlen(s)` | Longueur (sans le `'\0'`) | Parcourt toute la chaîne : coût proportionnel à sa longueur |
| `strcmp(a, b)` | Compare : <0, 0, >0 | **Pas** `==` : on comparerait des adresses |
| `strncmp(a, b, n)` | Compare au plus `n` caractères |  |
| `strcpy(d, s)` | Copie `s` dans `d` | **Aucune limite** : dangereux |
| `strncpy(d, s, n)` | Copie au plus `n` caractères | Ne termine **pas** toujours par `'\0'` : piège |
| `strcat(d, s)` | Concatène | **Aucune limite** : dangereux |
| `strchr(s, c)` / `strrchr` | Premier / dernier caractère `c` | Renvoie un pointeur ou `NULL` |
| `strstr(s, sous)` | Première occurrence d'une sous-chaîne | Pointeur ou `NULL` |
| `strtok(s, delim)` | Découpe en morceaux | Modifie `s`, **non réentrant** |
| `memcpy(d, s, n)` | Copie `n` octets | Zones **ne se chevauchant pas** |
| `memmove(d, s, n)` | Copie `n` octets | Gère le chevauchement |
| `memset(p, v, n)` | Remplit `n` octets avec `v` |  |
| `memcmp(a, b, n)` | Compare `n` octets |  |

### 12.3 Copier et concaténer en sécurité

Les fonctions classiques `strcpy`, `strcat` et `sprintf` ne contrôlent **aucune taille** : le moindre débordement écrase la mémoire voisine. Utilisez **`snprintf`**, qui est borné, tronque proprement et termine toujours par `'\0'` :

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char dest[16];
    const char *prenom = "Alexandre", *nom = "Dumas";

    int n = snprintf(dest, sizeof dest, "%s %s", prenom, nom);   // "Alexandre Dumas" fait 15 car.
    if (n < 0 || (size_t)n >= sizeof dest) {
        fprintf(stderr, "Troncature : %d caractères nécessaires\n", n);
    }
    printf("[%s]\n", dest);

    // Concaténation sûre : on repart de la fin de la chaîne
    char msg[32] = "Bonjour ";
    size_t len = strlen(msg);
    snprintf(msg + len, sizeof msg - len, "%s", "le monde");
    printf("[%s]\n", msg);
    return 0;
}
```

La valeur de retour de `snprintf` est la longueur **qu'aurait eue** le résultat : si elle est supérieure ou égale à la taille du tampon, il y a eu troncature. Pour mesurer la place disponible, ne dupliquez pas de nombres magiques : utilisez `sizeof` sur le tableau.

### 12.4 Lire et parcourir

Parcourir une chaîne se fait **jusqu'au `'\0'`**, sans avoir besoin de la longueur :

```c
#include <ctype.h>
#include <stdio.h>

int main(void) {
    char s[] = "Bonjour le Monde";
    int voyelles = 0, majuscules = 0;
    for (const char *p = s; *p != '\0'; p++) {
        if (isupper((unsigned char)*p)) majuscules++;
        if (*p == 'a' || *p == 'e' || *p == 'i' || *p == 'o' || *p == 'u') voyelles++;
    }
    printf("voyelles = %d, majuscules = %d\n", voyelles, majuscules);
    return 0;
}
```

Pour la lecture, utilisez `fgets` (section 7.4) et supprimez le `'\n'` final avec `strcspn`.

### 12.5 `<ctype.h>` : tester et convertir les caractères

| Fonction | Teste / convertit |
| --- | --- |
| `isalpha`, `isdigit`, `isalnum` | Lettre, chiffre, lettre ou chiffre |
| `isspace`, `ispunct` | Espace blanc, ponctuation |
| `isupper`, `islower` | Majuscule, minuscule |
| `toupper`, `tolower` | Conversion de casse |

> **Important** : ces fonctions attendent un `int` valant `EOF` ou un `unsigned char`. Avec un `char` signé contenant un caractère accentué (valeur négative), le comportement est **indéfini**. Écrivez donc `isalpha((unsigned char)c)`.

Elles ne gèrent que l'ASCII et la locale courante, pas l'Unicode (section 27).

### 12.6 Conversions chaîne ⇄ nombre

```c
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    const char *texte = "12abc";
    char *fin;
    errno = 0;
    long n = strtol(texte, &fin, 10);          // base 10
    printf("n = %ld, reste = \"%s\"\n", n, fin);   // n = 12, reste = "abc"
    if (fin == texte) fprintf(stderr, "aucun chiffre\n");
    if (errno == ERANGE) fprintf(stderr, "hors plage\n");

    double x = strtod("3.14 euros", &fin);
    printf("x = %.2f\n", x);

    char buf[32];
    snprintf(buf, sizeof buf, "%d", 2026);     // nombre -> chaîne
    printf("[%s]\n", buf);
    return 0;
}
```

`strtol`, `strtoll`, `strtoul`, `strtod` permettent de **détecter les erreurs** (via `fin` et `errno`). **N'utilisez pas `atoi`/`atof`** : elles renvoient 0 en cas d'erreur, ce qui est indiscernable d'une vraie valeur nulle, et leur comportement est indéfini en cas de dépassement.

### 12.7 Tableau de chaînes

```c
#include <stdio.h>

int main(void) {
    const char *jours[] = {"lundi", "mardi", "mercredi"};     // tableau de POINTEURS
    size_t n = sizeof jours / sizeof jours[0];
    for (size_t i = 0; i < n; i++) printf("%zu : %s\n", i, jours[i]);

    char noms[3][10] = {"Ada", "Linus", "Grace"};            // tableau 2D : 3 x 10 octets
    noms[0][0] = 'a';                                          // modifiable
    printf("%s\n", noms[0]);
    return 0;
}
```

Le premier est compact et ses chaînes sont en lecture seule ; le second réserve **un espace fixe** par chaîne (gaspillage possible) mais les contenus sont **modifiables**.

### 12.8 Bonnes pratiques

- Prévoyez **toujours** la place du `'\0'`.
- **Passez la taille du tampon** à toute fonction qui écrit dans une chaîne.
- Préférez `snprintf`, `fgets`, `memcpy` (avec longueur vérifiée) à `strcpy`, `strcat`, `gets`, `sprintf`.
- Déclarez `const char *` pour les chaînes non modifiées.
- Comparez avec `strcmp`, jamais avec `==`.
- Ne modifiez **jamais** un littéral de chaîne.

## 13. Pointeurs

### 13.1 Qu'est-ce qu'un pointeur ?

Chaque octet de la mémoire possède une **adresse** (un numéro). Un **pointeur** est une variable qui **contient une adresse**. Un pointeur de type `T *` pointe vers un objet de type `T` : le type indique **comment interpréter** ce qui se trouve à l'adresse et **de combien avancer** en arithmétique.

| Syntaxe | Signification |
| --- | --- |
| `int *p;` | `p` est un pointeur vers un `int` |
| `&x` | **Adresse de** la variable `x` |
| `*p` | **Valeur pointée** par `p` (déréférencement) |
| `p->champ` | Équivalent de `(*p).champ` (pointeur vers une structure) |

```c
#include <stdio.h>

int main(void) {
    int x = 10;
    int *p = &x;                 // p contient l'adresse de x

    printf("x = %d, &x = %p\n", x, (void *)&x);
    printf("p = %p, *p = %d\n", (void *)p, *p);

    *p = 20;                     // modifie x PAR L'INTERMÉDIAIRE de p
    printf("x = %d\n", x);       // 20

    int **pp = &p;               // pointeur vers un pointeur
    **pp = 30;
    printf("x = %d\n", x);       // 30
    return 0;
}
```

Attention à la double signification de `*` : dans une **déclaration** (`int *p;`), il indique le type pointeur ; dans une **expression** (`*p`), c'est l'opérateur de **déréférencement**. Pour afficher une adresse avec `%p`, convertissez en `(void *)`.

### 13.2 Pointeur nul

Un pointeur qui ne pointe sur rien vaut **`NULL`** (ou **`nullptr`** en C23). **Déréférencer un pointeur nul est un comportement indéfini** (en pratique : plantage, *segmentation fault*).

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *p = NULL;                  // toujours initialiser un pointeur
    if (p == NULL) puts("p ne pointe sur rien");
    if (!p)        puts("équivalent : un pointeur nul est « faux »");

    p = malloc(sizeof *p);
    if (p != NULL) {                // TOUJOURS tester le résultat de malloc
        *p = 5;
        printf("*p = %d\n", *p);
        free(p);
        p = NULL;                   // évite un usage après libération
    }
    return 0;
}
```

Règles : initialisez tous les pointeurs (à une adresse valide ou à `NULL`), testez avant de déréférencer, mettez à `NULL` après `free`.

### 13.3 Arithmétique des pointeurs

Ajouter `n` à un pointeur `T *` le déplace de **`n × sizeof(T)` octets**, c'est-à-dire de `n` éléments, pas de `n` octets :

```c
#include <stdio.h>

int main(void) {
    int t[] = {10, 20, 30, 40};
    int *p = t;                              // équivaut à &t[0]

    printf("*p = %d\n", *p);                 // 10
    printf("*(p + 2) = %d\n", *(p + 2));     // 30
    p++;                                     // avance d'UN int (4 octets en général)
    printf("*p = %d\n", *p);                 // 20

    int *fin = t + 4;                        // un cran APRÈS le dernier : autorisé mais non déréférençable
    printf("éléments entre p et fin : %td\n", fin - p);   // 3 (type ptrdiff_t)

    for (int *q = t; q < fin; q++) printf("%d ", *q);     // parcours par pointeur
    printf("\n");
    return 0;
}
```

Opérations permises : `p + n`, `p - n`, `p++`, `p--`, `p1 - p2` (nombre d'éléments, si les deux pointent **dans le même tableau**), et comparaisons `<`, `==`. L'**arithmétique en dehors d'un tableau** (au-delà de la case suivant le dernier élément) est un **comportement indéfini**. L'identité fondamentale est : **`t[i]` est exactement `*(t + i)`**.

### 13.4 Tableaux ≠ pointeurs

Un nom de tableau **se convertit** presque toujours en pointeur vers son premier élément, ce qui fait croire qu'ils sont identiques. Ils ne le sont pas :

|  | Tableau `int t[4]` | Pointeur `int *p` |
| --- | --- | --- |
| `sizeof` | 16 (taille totale) | 8 (taille d'un pointeur) |
| Réaffectation | Impossible (`t = …` interdit) | Possible |
| `&` | `&t` est de type `int (*)[4]` | `&p` est de type `int **` |
| Stockage | Les éléments eux-mêmes | Une adresse |

La conversion n'a **pas** lieu avec `sizeof` et `&`. C'est pourquoi un paramètre `int t[]` est, en réalité, un `int *`.

### 13.5 Pointeurs et fonctions

Passer un pointeur permet à une fonction de **modifier** les données de l'appelant ou d'éviter une grosse copie :

```c
#include <stdio.h>

static void incrementer(int *n)   { (*n)++; }                // parenthèses : (*n)++ et non *n++
static void minmax(const int *t, size_t n, int *min, int *max) {
    *min = *max = t[0];
    for (size_t i = 1; i < n; i++) {
        if (t[i] < *min) *min = t[i];
        if (t[i] > *max) *max = t[i];
    }
}

int main(void) {
    int x = 5;
    incrementer(&x);
    int t[] = {7, 2, 9, 4}, lo, hi;
    minmax(t, 4, &lo, &hi);
    printf("x = %d, min = %d, max = %d\n", x, lo, hi);
    return 0;
}
```

Piège de priorité : `*n++` incrémente le **pointeur** puis déréférence, alors que `(*n)++` incrémente la **valeur pointée**.

### 13.6 `const` et pointeurs (rappel)

| Déclaration | Peut changer `*p` ? | Peut changer `p` ? |
| --- | --- | --- |
| `int *p` | Oui | Oui |
| `const int *p` | **Non** | Oui |
| `int *const p` | Oui | **Non** |
| `const int *const p` | **Non** | **Non** |

Un paramètre `const T *` est un **contrat** : « je ne modifie pas ce que vous me donnez ». Appliquez-le systématiquement aux paramètres d'entrée.

### 13.7 `void *` : pointeur générique

Un `void *` peut contenir l'adresse de **n'importe quel** objet, mais on **ne peut ni le déréférencer ni faire d'arithmétique** dessus : il faut d'abord le convertir vers un type précis. C'est le mécanisme de `malloc`, `qsort`, `memcpy`.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int x = 7;
    void *g = &x;                    // conversion implicite vers void * (permise en C)
    int *p = g;                      // et retour : pas de cast nécessaire en C
    printf("%d\n", *p);

    double *d = malloc(3 * sizeof *d);   // malloc renvoie void * : pas de cast en C
    if (d) { d[0] = 1.5; printf("%.1f\n", d[0]); free(d); }
    return 0;
}
```

En C (contrairement à C++), les conversions depuis et vers `void *` sont **implicites** : ne castez pas le résultat de `malloc`.

### 13.8 Pointeur vers une structure

```c
#include <stdio.h>

struct Point { int x, y; };

static void deplacer(struct Point *p, int dx, int dy) {
    p->x += dx;                      // p->x est identique à (*p).x
    p->y += dy;
}

int main(void) {
    struct Point a = {1, 2};
    deplacer(&a, 10, 20);
    printf("(%d, %d)\n", a.x, a.y);  // (11, 22)
    return 0;
}
```

On utilise `.` sur une **structure** et `->` sur un **pointeur vers une structure** (section 18).

### 13.9 `restrict` (C99)

`restrict` est une **promesse** faite au compilateur : durant la vie du pointeur, l'objet pointé n'est accessible **que** par ce pointeur. Cela autorise des optimisations (comme dans `memcpy`, dont les zones ne doivent pas se chevaucher) :

```c
void ajouter(int *restrict dest, const int *restrict src, size_t n) {
    for (size_t i = 0; i < n; i++) dest[i] += src[i];     // dest et src ne se recouvrent pas
}
```

Si la promesse est violée (les zones se chevauchent), le comportement est **indéfini**.

### 13.10 Erreurs classiques

| Erreur | Exemple | Conséquence |
| --- | --- | --- |
| Pointeur non initialisé | `int *p; *p = 5;` | Écriture à une adresse aléatoire |
| Déréférencer `NULL` | `*p` avec `p == NULL` | Plantage |
| Pointeur « pendant » | Retourner `&locale` | Adresse invalide après la sortie de la fonction |
| Usage après `free` | `free(p); *p = 1;` | Corruption de mémoire |
| Dépassement | `p[n]` pour un tableau de `n` | Comportement indéfini |
| Mauvais type | `double *` lu comme `int *` | Données absurdes, violation d'alias |
| Oubli de `&` | `scanf("%d", x)` | Écriture à l'adresse contenue dans `x` |
| Confusion `*p++` / `(*p)++` |  | Effet inattendu |

**Règle d'or** : un pointeur n'est utilisable que s'il pointe vers un objet **vivant** et **assez grand**. Posez-vous toujours : *qui possède cet objet ? sera-t-il encore valide quand j'y accède ?*

## 14. Allocation dynamique de mémoire

### 14.1 Pourquoi ?

Les variables locales vivent sur la **pile** : leur taille est fixée à la compilation et elles disparaissent à la sortie du bloc. L'**allocation dynamique** réserve de la mémoire sur le **tas** pendant l'exécution, avec une **taille choisie à l'exécution** et une **durée de vie contrôlée** par le programmeur. Elle est indispensable quand la taille dépend des données (nombre de lignes d'un fichier), quand l'objet doit survivre à la fonction qui le crée, ou quand il est trop gros pour la pile.

### 14.2 Les fonctions de `<stdlib.h>`

| Fonction | Rôle |
| --- | --- |
| `malloc(n)` | Réserve `n` octets, **non initialisés** ; renvoie `NULL` en cas d'échec |
| `calloc(nb, taille)` | Réserve `nb × taille` octets **mis à zéro** ; contrôle le débordement de la multiplication |
| `realloc(p, n)` | Redimensionne un bloc (peut le **déplacer**) |
| `free(p)` | Libère un bloc ; `free(NULL)` est sans effet |

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    size_t n = 5;
    int *t = malloc(n * sizeof *t);          // sizeof *t : s'adapte si le type change
    if (t == NULL) {                          // TOUJOURS vérifier
        fprintf(stderr, "Mémoire insuffisante\n");
        return EXIT_FAILURE;
    }
    for (size_t i = 0; i < n; i++) t[i] = (int)(i * i);
    for (size_t i = 0; i < n; i++) printf("%d ", t[i]);
    printf("\n");
    free(t);                                  // libérer UNE fois
    t = NULL;                                 // évite le use-after-free
    return EXIT_SUCCESS;
}
```

Bonnes habitudes visibles ici : écrire `sizeof *t` plutôt que `sizeof(int)` ; ne **pas** caster le résultat de `malloc` ; tester `NULL` ; libérer puis mettre à `NULL`.

### 14.3 `calloc`

```c
int *t = calloc(n, sizeof *t);     // n entiers, tous à 0
```

`calloc` est préférable à `malloc(n * taille)` quand `n` vient de l'extérieur : elle **détecte le dépassement** de `n × taille` (et renvoie `NULL`), alors que la multiplication manuelle peut déborder silencieusement et allouer **trop peu** (faille classique). Avec `malloc`, utilisez `ckd_mul` (C23) ou une vérification explicite.

### 14.4 `realloc` : la bonne façon

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    size_t cap = 4;
    int *t = malloc(cap * sizeof *t);
    if (!t) return 1;

    size_t nouvelle = cap * 2;
    int *tmp = realloc(t, nouvelle * sizeof *tmp);   // dans une variable TEMPORAIRE
    if (tmp == NULL) {                                // échec : l'ancien bloc reste valide
        free(t);
        return 1;
    }
    t = tmp;                                          // succès seulement
    cap = nouvelle;
    printf("capacité = %zu\n", cap);
    free(t);
    return 0;
}
```

**Ne jamais écrire `t = realloc(t, …)`** : en cas d'échec, `realloc` renvoie `NULL` et l'ancien bloc est **perdu** (fuite). De plus, après un succès, le bloc a pu changer d'adresse : **tous les anciens pointeurs** vers son contenu deviennent invalides.

### 14.5 Erreurs classiques de gestion mémoire

| Erreur | Description | Conséquence |
| --- | --- | --- |
| **Fuite** (*leak*) | Bloc jamais libéré, adresse perdue | Consommation de mémoire croissante |
| **Double `free`** | Libérer deux fois | Corruption du tas, plantage |
| **Use-after-free** | Utiliser un bloc libéré | Comportement indéfini, faille |
| **Dépassement de tas** | Écrire au-delà de la taille allouée | Corruption |
| **`free` d'un pointeur non alloué** | `free(&x)` ou `free(p + 1)` | Plantage |
| **Oubli du test de `malloc`** | Déréférencer `NULL` | Plantage |
| **Mauvaise taille** | `malloc(n)` au lieu de `n * sizeof *p` | Dépassement |

### 14.6 Règle de propriété

À tout bloc alloué doit correspondre **un propriétaire unique**, responsable de sa libération. Documentez-le : « la fonction `creer()` renvoie un objet que l'appelant doit libérer avec `detruire()` ». Une paire de fonctions **`creer` / `detruire`** par type est la convention la plus sûre.

### 14.7 Outils de détection

```bash
gcc -g -fsanitize=address,undefined -std=c17 prog.c -o prog && ./prog   # AddressSanitizer + UBSan
valgrind --leak-check=full ./prog                                       # Valgrind (Linux)
```

**AddressSanitizer** détecte dépassements, use-after-free, double free et fuites ; **Valgrind** rapporte les fuites et les lectures de mémoire non initialisée. Utilisez-les **systématiquement** pendant le développement.

## 15. Retourner des tableaux et des chaînes

### 15.1 Le problème

Une fonction ne peut pas retourner un tableau par valeur. Et surtout, retourner un **pointeur vers une variable locale** est une erreur grave : l'objet disparaît à la sortie de la fonction.

```c
char *mauvais(void) {
    char s[] = "temporaire";
    return s;                       // ERREUR : s est détruit à la sortie (pointeur pendant)
}
```

### 15.2 Les quatre solutions

#### 1. L'appelant fournit le tampon (recommandé)

```c
#include <stdio.h>

// Écrit dans le tampon de l'appelant ; renvoie le nombre de caractères ou -1 si trop petit
static int formater_date(char *dest, size_t taille, int j, int m, int a) {
    int n = snprintf(dest, taille, "%02d/%02d/%04d", j, m, a);
    return (n < 0 || (size_t)n >= taille) ? -1 : n;
}

int main(void) {
    char buf[16];
    if (formater_date(buf, sizeof buf, 5, 3, 2026) >= 0) printf("%s\n", buf);
    return 0;
}
```

Avantages : aucune allocation, aucune fuite possible, taille contrôlée. C'est le modèle de la bibliothèque standard (`fgets`, `snprintf`).

#### 2. Allocation dynamique

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// L'APPELANT doit libérer le résultat avec free()
static char *dupliquer(const char *s) {
    size_t n = strlen(s) + 1;
    char *copie = malloc(n);
    if (copie == NULL) return NULL;
    memcpy(copie, s, n);
    return copie;
}

static int *creer_tableau(size_t n) {
    int *t = calloc(n, sizeof *t);
    if (t) for (size_t i = 0; i < n; i++) t[i] = (int)i;
    return t;
}

int main(void) {
    char *c = dupliquer("bonjour");
    int *t = creer_tableau(4);
    if (c && t) printf("%s %d\n", c, t[3]);
    free(c);
    free(t);
    return 0;
}
```

La fonction **alloue**, l'appelant **libère** : la propriété est transférée. Il faut le documenter. (`strdup` existe en POSIX et en C23.)

#### 3. Variable `static` (à éviter)

```c
const char *nom_du_jour(int j) {
    static char tampon[32];          // persiste après la sortie
    snprintf(tampon, sizeof tampon, "jour %d", j);
    return tampon;
}
```

Cela fonctionne, mais **chaque appel écrase le résultat précédent** et la fonction n'est **pas réentrante** (dangereuse avec plusieurs fils d'exécution). Réservez-la aux **constantes** : retourner un littéral de chaîne est sûr.

#### 4. Structure

```c
typedef struct { char texte[32]; } Etiquette;       // la structure CONTIENT le tableau

static Etiquette creer_etiquette(int n) {
    Etiquette e;
    snprintf(e.texte, sizeof e.texte, "id-%d", n);
    return e;                                       // copie de la structure : sûr
}
```

Une structure est copiée en entier, tableau compris : c'est la seule façon de « retourner un tableau » par valeur. Adapté aux **petites** tailles fixes.

### 15.3 Ce qu'il ne faut jamais faire

- Retourner l'adresse d'une variable **locale** (tableau ou scalaire).
- Retourner un pointeur vers un **paramètre** passé par valeur.
- Allouer sans documenter qui libère.
- Libérer un pointeur obtenu autrement qu'avec `malloc`/`calloc`/`realloc` (littéral, tableau local).

## 16. Structures de données dynamiques

### 16.1 Liste simplement chaînée

Une **liste chaînée** est une suite de **nœuds** alloués séparément ; chaque nœud contient une valeur et un pointeur vers le suivant. Le dernier pointe vers `NULL`.

```text
tete ─▶ [ 3 | ●─]─▶ [ 7 | ●─]─▶ [ 9 | NULL ]
```

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Noeud {
    int valeur;
    struct Noeud *suivant;
} Noeud;

// Insertion en tête : O(1)
static Noeud *inserer_tete(Noeud *tete, int v) {
    Noeud *n = malloc(sizeof *n);
    if (!n) return tete;                  // échec : liste inchangée
    n->valeur = v;
    n->suivant = tete;
    return n;                             // nouvelle tête
}

// Insertion en queue : O(n) (il faut parcourir)
static Noeud *inserer_queue(Noeud *tete, int v) {
    Noeud *n = malloc(sizeof *n);
    if (!n) return tete;
    n->valeur = v; n->suivant = NULL;
    if (!tete) return n;
    Noeud *p = tete;
    while (p->suivant) p = p->suivant;
    p->suivant = n;
    return tete;
}

static void afficher(const Noeud *tete) {
    for (const Noeud *p = tete; p; p = p->suivant) printf("%d -> ", p->valeur);
    printf("NULL\n");
}

static Noeud *chercher(Noeud *tete, int v) {
    for (Noeud *p = tete; p; p = p->suivant) if (p->valeur == v) return p;
    return NULL;
}

// Suppression de la première occurrence
static Noeud *supprimer(Noeud *tete, int v) {
    Noeud *prec = NULL;
    for (Noeud *p = tete; p; prec = p, p = p->suivant) {
        if (p->valeur == v) {
            if (prec) prec->suivant = p->suivant;
            else tete = p->suivant;           // on supprime la tête
            free(p);
            break;
        }
    }
    return tete;
}

static void liberer(Noeud *tete) {
    while (tete) {
        Noeud *suivant = tete->suivant;       // SAUVEGARDER avant free
        free(tete);
        tete = suivant;
    }
}

int main(void) {
    Noeud *liste = NULL;
    liste = inserer_tete(liste, 7);
    liste = inserer_tete(liste, 3);
    liste = inserer_queue(liste, 9);
    afficher(liste);                           // 3 -> 7 -> 9 -> NULL
    liste = supprimer(liste, 7);
    afficher(liste);                           // 3 -> 9 -> NULL
    printf(chercher(liste, 9) ? "9 trouvé\n" : "9 absent\n");
    liberer(liste);
    return 0;
}
```

Points à retenir : le `struct Noeud *` auto-référencé exige le **nom de balise** dans la définition ; on **sauvegarde `suivant` avant `free`** ; la fonction qui modifie la tête **retourne** la nouvelle tête (ou reçoit un `Noeud **`, section 17).

### 16.2 Autres structures

| Structure | Principe | Atouts / limites |
| --- | --- | --- |
| **Pile** (LIFO) | Dernier entré, premier sorti | Opérations en O(1) ; appels de fonctions, annulation |
| **File** (FIFO) | Premier entré, premier sorti | Tampons, ordonnancement |
| **Liste doublement chaînée** | Pointeurs `precedent` et `suivant` | Parcours dans les deux sens ; suppression en O(1) avec le nœud |
| **Arbre binaire de recherche** | Chaque nœud a un fils gauche (plus petit) et droit (plus grand) | Recherche en O(log n) si équilibré, O(n) sinon |
| **Table de hachage** | Tableau de listes, indice = `hash(clé) % taille` | Accès moyen en O(1) |
| **Tas** (*heap*) | Arbre complet stocké en tableau | File de priorité |

**Tableau ou liste ?** Le tableau offre un accès par indice en O(1) et une excellente localité de cache ; la liste offre des insertions/suppressions en O(1) quand on tient le nœud, mais un accès en O(n) et un surcoût de pointeurs. En pratique, le **tableau dynamique** est le meilleur choix par défaut.

### 16.3 Tableau dynamique extensible (vecteur)

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *donnees;
    size_t taille;       // nombre d'éléments utilisés
    size_t capacite;     // nombre d'éléments alloués
} Vecteur;

static void vecteur_init(Vecteur *v) { v->donnees = NULL; v->taille = 0; v->capacite = 0; }

static int vecteur_ajouter(Vecteur *v, int x) {
    if (v->taille == v->capacite) {
        size_t nouvelle = v->capacite ? v->capacite * 2 : 4;   // doublement : coût amorti O(1)
        int *tmp = realloc(v->donnees, nouvelle * sizeof *tmp);
        if (!tmp) return -1;
        v->donnees = tmp;
        v->capacite = nouvelle;
    }
    v->donnees[v->taille++] = x;
    return 0;
}

static void vecteur_liberer(Vecteur *v) {
    free(v->donnees);
    vecteur_init(v);
}

int main(void) {
    Vecteur v;
    vecteur_init(&v);
    for (int i = 0; i < 10; i++) if (vecteur_ajouter(&v, i * i) != 0) break;
    printf("taille = %zu, capacité = %zu, dernier = %d\n", v.taille, v.capacite, v.donnees[v.taille - 1]);
    vecteur_liberer(&v);
    return 0;
}
```

La stratégie du **doublement de capacité** rend l'ajout en moyenne très peu coûteux, car les copies rares sont amorties sur de nombreux ajouts.

### 16.4 Matrices dynamiques

#### Méthode A : tableau de pointeurs (lignes indépendantes)

```c
#include <stdio.h>
#include <stdlib.h>

static int **creer_matrice(size_t lignes, size_t colonnes) {
    int **m = malloc(lignes * sizeof *m);
    if (!m) return NULL;
    for (size_t i = 0; i < lignes; i++) {
        m[i] = calloc(colonnes, sizeof **m);
        if (!m[i]) {                               // échec : libérer ce qui est déjà alloué
            while (i-- > 0) free(m[i]);
            free(m);
            return NULL;
        }
    }
    return m;
}

static void liberer_matrice(int **m, size_t lignes) {
    if (!m) return;
    for (size_t i = 0; i < lignes; i++) free(m[i]);
    free(m);
}

int main(void) {
    int **m = creer_matrice(3, 4);
    if (!m) return 1;
    m[2][3] = 42;
    printf("m[2][3] = %d\n", m[2][3]);
    liberer_matrice(m, 3);
    return 0;
}
```

Souple (lignes de longueurs différentes, échange de lignes par simple échange de pointeurs), mais **plusieurs allocations** et mémoire **non contiguë**.

#### Méthode B : bloc unique contigu (plus efficace)

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    size_t L = 3, C = 4;
    int *m = calloc(L * C, sizeof *m);        // UNE allocation, UNE libération
    if (!m) return 1;
    m[1 * C + 2] = 7;                         // élément (ligne 1, colonne 2) : i * C + j
    printf("m(1,2) = %d\n", m[1 * C + 2]);

    int (*vue)[C] = (int (*)[C])m;            // C99 : pointeur vers tableau de C entiers (VLA type)
    vue[2][3] = 9;                            // notation m[i][j] retrouvée
    printf("vue[2][3] = %d\n", vue[2][3]);
    free(m);
    return 0;
}
```

Un seul bloc : meilleure **localité de cache**, une seule libération. L'indice `i * C + j` convertit les coordonnées en position linéaire.

## 17. Pointeurs doubles

### 17.1 Définition

Un **pointeur double** (`T **`) est un pointeur vers un pointeur vers un `T`. Il contient l'adresse d'une variable qui est elle-même un pointeur.

```c
#include <stdio.h>

int main(void) {
    int x = 5;
    int *p = &x;           // p pointe sur x
    int **pp = &p;         // pp pointe sur p
    printf("x=%d *p=%d **pp=%d\n", x, *p, **pp);
    **pp = 99;             // modifie x
    printf("x = %d\n", x);
    return 0;
}
```

| Expression | Type | Valeur |
| --- | --- | --- |
| `pp` | `int **` | Adresse de `p` |
| `*pp` | `int *` | Valeur de `p` (adresse de `x`) |
| `**pp` | `int` | Valeur de `x` |

### 17.2 Usages principaux

#### 1. Modifier un pointeur depuis une fonction

Puisque les arguments sont passés **par valeur**, pour qu'une fonction **modifie un pointeur** de l'appelant, il faut lui passer l'**adresse du pointeur** :

```c
#include <stdio.h>
#include <stdlib.h>

static int allouer(int **p, size_t n) {          // reçoit l'adresse du pointeur de l'appelant
    *p = malloc(n * sizeof **p);
    return *p ? 0 : -1;
}

int main(void) {
    int *t = NULL;
    if (allouer(&t, 5) == 0) {                   // t est modifié
        t[0] = 1;
        printf("t[0] = %d\n", t[0]);
        free(t);
    }
    return 0;
}
```

Sans le double pointeur, la fonction modifierait une **copie** du pointeur et l'appelant verrait toujours `NULL`.

#### 2. Tableau de chaînes / matrices

`char **` désigne un tableau de chaînes ; `int **` une matrice (section 16.4) :

```c
#include <stdio.h>

static void afficher_mots(char **mots, size_t n) {
    for (size_t i = 0; i < n; i++) printf("%s\n", mots[i]);
}

int main(void) {
    char *mots[] = {"un", "deux", "trois"};
    afficher_mots(mots, 3);
    return 0;
}
```

#### 3. Listes chaînées (insertion et suppression élégantes)

Avec un `Noeud **`, on traite la tête comme n'importe quel maillon, sans cas particulier :

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Noeud { int valeur; struct Noeud *suivant; } Noeud;

static void inserer_tete(Noeud **tete, int v) {
    Noeud *n = malloc(sizeof *n);
    if (!n) return;
    n->valeur = v;
    n->suivant = *tete;
    *tete = n;                                    // modifie la tête de l'appelant
}

static void supprimer(Noeud **tete, int v) {
    for (Noeud **pp = tete; *pp; pp = &(*pp)->suivant) {
        if ((*pp)->valeur == v) {
            Noeud *a_liberer = *pp;
            *pp = a_liberer->suivant;             // le lien précédent saute le nœud
            free(a_liberer);
            return;
        }
    }
}

int main(void) {
    Noeud *l = NULL;
    inserer_tete(&l, 3); inserer_tete(&l, 2); inserer_tete(&l, 1);
    supprimer(&l, 1);                             // supprimer la tête : aucun cas spécial
    for (Noeud *p = l; p; p = p->suivant) printf("%d ", p->valeur);
    printf("\n");
    while (l) { Noeud *s = l->suivant; free(l); l = s; }
    return 0;
}
```

#### 4. `argv` : `char **argv`

Les arguments de la ligne de commande sont fournis comme un tableau de chaînes (section 23).

### 17.3 Libération

Il faut libérer **dans l'ordre inverse** de l'allocation : d'abord les **éléments** pointés (chaque ligne, chaque chaîne), puis le **tableau de pointeurs**. Libérer le tableau en premier perdrait les adresses des éléments (fuite) ou provoquerait un use-after-free.

```c
char **mots = malloc(3 * sizeof *mots);
/* … mots[i] = strdup(…) … */
for (size_t i = 0; i < 3; i++) free(mots[i]);   // 1. les éléments
free(mots);                                      // 2. puis le tableau
```

## 18. Structures et unions

### 18.1 Structures (`struct`)

Une **structure** regroupe plusieurs données, de **types éventuellement différents**, sous un seul nom. Chaque donnée est un **membre** (ou *champ*). C'est le moyen de créer ses propres types composés : un point, un étudiant, une date.

```c
#include <stdio.h>
#include <string.h>

struct Etudiant {
    char   nom[32];
    int    age;
    double moyenne;
};

int main(void) {
    struct Etudiant e1 = {"Ada", 20, 17.5};                          // initialisation dans l'ordre
    struct Etudiant e2 = { .nom = "Linus", .moyenne = 15.0, .age = 22 };   // initialisation désignée (C99)
    struct Etudiant e3 = {0};                                         // tout à zéro

    e3.age = 19;                                       // accès par le point
    strcpy(e3.nom, "Grace");                           // un tableau de char ne s'affecte pas avec =
    e3.moyenne = 18.2;

    printf("%s a %d ans (%.1f)\n", e1.nom, e1.age, e1.moyenne);
    printf("%s a %d ans (%.1f)\n", e2.nom, e2.age, e2.moyenne);
    printf("%s a %d ans (%.1f)\n", e3.nom, e3.age, e3.moyenne);
    return 0;
}
```

Vocabulaire : `struct Etudiant` est le **type** ; `Etudiant` seul est la **balise** (*tag*). Les membres s'accèdent avec **`.`** sur une variable et **`->`** sur un pointeur.

#### Opérations

| Opération | Possible ? | Remarque |
| --- | --- | --- |
| Affectation `a = b;` | **Oui** | Copie membre à membre (y compris les tableaux membres) |
| Passage par valeur / retour par valeur | Oui | Copie complète ; coûteux pour de grosses structures |
| Comparaison `a == b` | **Non** | Comparer champ par champ (n'utilisez pas `memcmp` : le *padding* est indéterminé) |
| `sizeof(struct S)` | Oui | Peut dépasser la somme des membres (voir 18.2) |

```c
#include <stdio.h>

typedef struct { double x, y; } Point;

static Point milieu(Point a, Point b) {          // passage et retour PAR VALEUR
    return (Point){ (a.x + b.x) / 2, (a.y + b.y) / 2 };
}

static void translater(Point *p, double dx, double dy) {   // par POINTEUR pour modifier
    p->x += dx;
    p->y += dy;
}

int main(void) {
    Point a = {0, 0}, b = {4, 6};
    Point m = milieu(a, b);
    translater(&m, 1, 1);
    printf("(%.1f, %.1f)\n", m.x, m.y);           // (3.0, 4.0)
    return 0;
}
```

#### Littéraux composés (C99)

On peut créer une structure (ou un tableau) **anonyme** à la volée : `(Point){3, 4}` ou `(int[]){1, 2, 3}`. Très pratique pour passer un argument temporaire : `afficher((Point){3, 4});`.

#### Structures imbriquées et tableaux de structures

```c
#include <stdio.h>

typedef struct { int jour, mois, annee; } Date;
typedef struct {
    char nom[20];
    Date naissance;                     // structure imbriquée
} Personne;

int main(void) {
    Personne groupe[2] = {
        {"Ada",   {10, 12, 1815}},
        {"Alan",  {23,  6, 1912}},
    };
    for (size_t i = 0; i < 2; i++)
        printf("%s : %02d/%02d/%d\n", groupe[i].nom,
               groupe[i].naissance.jour, groupe[i].naissance.mois, groupe[i].naissance.annee);
    return 0;
}
```

#### Structure auto-référencée

Une structure ne peut **pas se contenir elle-même** (taille infinie), mais elle peut contenir un **pointeur** vers son propre type : c'est la base des listes et des arbres (section 16).

```c
struct Noeud {
    int valeur;
    struct Noeud *suivant;       // OK : un pointeur a une taille connue
};
```

### 18.2 Alignement et remplissage (*padding*)

Les processeurs accèdent plus efficacement aux données **alignées** sur un multiple de leur taille. Le compilateur insère donc des octets de **remplissage** entre les membres et à la fin de la structure.

```c
#include <stdio.h>
#include <stddef.h>

struct A { char c; int i; char d; };      // c, 3 octets de remplissage, i, d, 3 de remplissage : 12
struct B { int i; char c; char d; };      // i, c, d, 2 de remplissage : 8

int main(void) {
    printf("sizeof(A) = %zu, sizeof(B) = %zu\n", sizeof(struct A), sizeof(struct B));
    printf("offsetof(A, i) = %zu\n", offsetof(struct A, i));      // <stddef.h>
    return 0;
}
```

**Conseil** : ordonnez les membres du plus **grand** au plus **petit** pour réduire le remplissage. Les tailles exactes dépendent de la plateforme ; n'écrivez jamais une structure brute dans un fichier destiné à être lu sur une autre machine (formats, boutisme, remplissage divergent). `alignof` (C23) et `alignas` contrôlent l'alignement.

### 18.3 Champs de bits

Pour économiser de la place ou décrire un format matériel, on peut spécifier la **largeur en bits** de chaque membre entier :

```c
#include <stdio.h>

struct Drapeaux {
    unsigned int lecture   : 1;
    unsigned int ecriture  : 1;
    unsigned int mode      : 3;     // valeurs 0 à 7
};

int main(void) {
    struct Drapeaux d = {1, 0, 5};
    printf("lecture=%u mode=%u taille=%zu\n", d.lecture, d.mode, sizeof d);
    return 0;
}
```

**Limites** : l'ordre des bits, l'alignement et le comportement des champs signés **dépendent de l'implémentation** ; on ne peut pas prendre l'adresse d'un champ de bits. Pour un format binaire portable, préférez des **masques et des décalages** (section 25).

### 18.4 Membre de tableau flexible (C99)

Le **dernier** membre d'une structure peut être un tableau **sans taille**, alloué avec la structure en un seul bloc :

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    size_t longueur;
    char   donnees[];                 // membre flexible : ne compte pas dans sizeof
} Tampon;

static Tampon *creer(const char *texte) {
    size_t n = strlen(texte) + 1;
    Tampon *t = malloc(sizeof *t + n);        // structure + place pour les données
    if (!t) return NULL;
    t->longueur = n;
    memcpy(t->donnees, texte, n);
    return t;
}

int main(void) {
    Tampon *t = creer("flexible");
    if (t) { printf("%s (%zu octets)\n", t->donnees, t->longueur); free(t); }
    return 0;
}
```

Une seule allocation, une seule libération. Une telle structure ne peut pas être copiée par affectation (seule la partie fixe le serait) ni être membre d'une autre structure.

### 18.5 Unions

Une **union** déclare des membres qui **partagent la même zone mémoire** : à un instant donné, **un seul** est valide. Sa taille est celle de son plus grand membre.

```c
#include <stdio.h>

union Valeur {
    int    i;
    float  f;
    char   texte[8];
};

int main(void) {
    union Valeur v;
    v.i = 42;
    printf("i = %d\n", v.i);
    v.f = 3.14f;                       // écrase les octets : i n'a plus de sens
    printf("f = %.2f, sizeof(union) = %zu\n", v.f, sizeof v);   // 8
    return 0;
}
```

Lire un membre **différent** de celui qui a été écrit réinterprète les octets ; c'est permis en C (contrairement à C++) pour du *type punning*, mais le résultat dépend de la machine. Pour copier des octets de façon portable, utilisez `memcpy`.

#### Union étiquetée (*tagged union*) : usage sûr

Pour savoir quel membre est actif, on associe l'union à un **tag** (une `enum`). C'est l'équivalent d'un **type somme** (variante) :

```c
#include <stdio.h>

typedef enum { T_ENTIER, T_REEL, T_TEXTE } Genre;

typedef struct {
    Genre genre;                    // l'étiquette
    union {
        long       entier;
        double     reel;
        const char *texte;
    } v;                            // l'union : une seule valeur à la fois
} Variant;

static void afficher(const Variant *x) {
    switch (x->genre) {
        case T_ENTIER: printf("entier %ld\n", x->v.entier); break;
        case T_REEL:   printf("réel %.2f\n", x->v.reel);    break;
        case T_TEXTE:  printf("texte %s\n", x->v.texte);    break;
    }
}

int main(void) {
    Variant a = { T_ENTIER, { .entier = 42 } };
    Variant b = { T_TEXTE,  { .texte = "bonjour" } };
    afficher(&a);
    afficher(&b);
    return 0;
}
```

### 18.6 Structure ou union ?

|  | `struct` | `union` |
| --- | --- | --- |
| Membres | Tous présents **en même temps** | **Un seul** à la fois |
| Taille | Somme (plus remplissage) | Plus grand membre |
| Usage | Regrouper des données liées | Alternatives exclusives, économie mémoire, interprétations d'octets |

## 19. Énumérations (`enum`)

### 19.1 Définition

Une **énumération** définit un **ensemble de constantes entières nommées**. Elle remplace avantageusement les « nombres magiques » et les séries de `#define`.

```c
#include <stdio.h>

enum Couleur { ROUGE, VERT, BLEU };          // ROUGE = 0, VERT = 1, BLEU = 2

int main(void) {
    enum Couleur c = VERT;
    printf("c = %d\n", c);                   // 1
    return 0;
}
```

Par défaut, la première constante vaut **0** et chaque suivante vaut la précédente **+ 1**.

#### Valeurs explicites

```c
enum Niveau { BAS = 10, MOYEN = 20, HAUT = 30 };
enum Mois   { JAN = 1, FEV, MAR, AVR };     // FEV = 2, MAR = 3, AVR = 4
enum Droits { LIRE = 1, ECRIRE = 2, EXEC = 4 };   // puissances de 2 : combinables avec | (section 25)
```

#### Type sous-jacent (C23)

C23 permet de **fixer le type entier** d'une énumération, utile pour les formats binaires et le contrôle de la taille :

```c
// Compiler avec : gcc -std=c23
enum Etat : unsigned char { INACTIF, ACTIF, ERREUR };   // tient sur 1 octet
```

### 19.2 Avec `typedef` et `switch`

```c
#include <stdio.h>

typedef enum { LUNDI, MARDI, MERCREDI, NB_JOURS } Jour;     // NB_JOURS : astuce du compteur

static const char *nom_jour(Jour j) {
    switch (j) {
        case LUNDI:    return "lundi";
        case MARDI:    return "mardi";
        case MERCREDI: return "mercredi";
        default:       return "inconnu";
    }
}

int main(void) {
    for (Jour j = LUNDI; j < NB_JOURS; j++) printf("%d : %s\n", j, nom_jour(j));
    return 0;
}
```

Avec GCC/Clang, `-Wswitch` avertit si un `switch` sur une énumération **oublie** une constante (à condition de ne pas mettre de `default`, qui masquerait l'oubli). La dernière constante `NB_JOURS` sert à **compter** les valeurs et à dimensionner des tableaux.

### 19.3 Particularités

- Les constantes d'une `enum` sont des **`int`** (avant C23) : elles ont la **portée du bloc englobant**. Deux énumérations ne peuvent donc pas partager un même nom de constante.
- Une variable de type `enum` est essentiellement un **entier** : le C **n'empêche pas** d'y ranger une valeur hors énumération (`c = 42;`). Le typage est faible.
- Deux constantes peuvent avoir la **même valeur**.
- Une `enum` anonyme est un excellent moyen de définir des **constantes entières de compilation** : `enum { TAILLE = 64 };` (utilisable pour dimensionner un tableau).

## 20. `typedef`

### 20.1 Créer un alias de type

`typedef` ne crée **pas** un nouveau type : il donne un **nouveau nom** à un type existant. La syntaxe est celle d'une déclaration de variable précédée de `typedef` : le nom déclaré devient le nom du type.

```c
#include <stdio.h>
#include <stdint.h>

typedef unsigned long long u64;          // alias simple
typedef int Entier;
typedef struct { double x, y; } Point;   // plus besoin d'écrire "struct"
typedef struct Noeud Noeud;              // déclaration anticipée d'un type auto-référencé
struct Noeud { int valeur; Noeud *suivant; };

int main(void) {
    u64 grand = 12345678901234ULL;
    Entier n = 5;
    Point p = {1.0, 2.0};
    printf("%llu %d (%.1f, %.1f)\n", grand, n, p.x, p.y);
    return 0;
}
```

### 20.2 Usages courants

```c
typedef char *Chaine;                       // déconseillé : masque le pointeur (const Chaine ≠ const char *)
typedef int Matrice[3][3];                  // alias de type tableau
typedef void (*Rappel)(int);                // alias de pointeur de fonction (très lisible)
typedef int (*Comparateur)(const void *, const void *);
```

- **Raccourcir** `struct X` en `X`.
- **Abstraire** un type (`typedef int32_t Identifiant;`) : un changement ultérieur ne se fait qu'en un endroit.
- **Simplifier** les déclarations complexes, surtout les pointeurs de fonctions (section 21).

### 20.3 `typedef` ou `#define` ?

|  | `typedef` | `#define` |
| --- | --- | --- |
| Traité par | Le **compilateur** | Le **préprocesseur** (texte) |
| Portée | Respectée | Aucune |
| `typedef int* P; P a, b;` | `a` et `b` sont **tous deux** des pointeurs |  |
| `#define P int*` ; `P a, b;` |  | `a` est un pointeur, `b` est un `int` ! |

Préférez toujours `typedef` pour les types.

### 20.4 Bonnes pratiques

- Ne cachez pas un **pointeur** derrière un `typedef` : le lecteur ne voit plus qu'il manipule une adresse.
- Utilisez une convention de nommage claire (`Point`, `point_t`). Attention : le suffixe `_t` est **réservé par POSIX** ; si vous publiez une bibliothèque, préférez un préfixe (`mylib_point`).
- Un `typedef` de pointeur de fonction améliore beaucoup la lisibilité.

## 21. Pointeurs de fonctions

### 21.1 Principe

En mémoire, le code d'une fonction a une **adresse**. Un **pointeur de fonction** stocke cette adresse et permet d'**appeler une fonction choisie à l'exécution** : c'est le mécanisme des **callbacks**, des tables de dispatch et des « méthodes » en C.

```c
#include <stdio.h>

static int addition(int a, int b)       { return a + b; }
static int multiplication(int a, int b) { return a * b; }

int main(void) {
    int (*op)(int, int);              // op : pointeur vers une fonction (int, int) -> int
    op = addition;                    // le nom d'une fonction se convertit en pointeur (& facultatif)
    printf("%d\n", op(3, 4));         // 7 : appel via le pointeur
    op = &multiplication;
    printf("%d\n", (*op)(3, 4));      // 12 : forme équivalente
    return 0;
}
```

**Lecture de la déclaration** : `int (*op)(int, int)` se lit « `op` est un pointeur (`*op`) vers une fonction prenant deux `int` et retournant un `int` ». **Les parenthèses autour de `*op` sont indispensables** : `int *op(int, int)` déclarerait une fonction retournant un `int *`.

### 21.2 Avec `typedef`

```c
typedef int (*Operation)(int, int);       // Operation : type « pointeur vers fonction (int, int) -> int »

static int appliquer(Operation f, int a, int b) { return f(a, b); }
```

Sans `typedef`, un paramètre s'écrit `int (*f)(int, int)`, ce qui devient vite illisible.

### 21.3 Callbacks : `qsort`

Un **callback** est une fonction passée en argument pour être appelée **plus tard** par une autre. C'est ainsi que `qsort` reste générique : le tri est écrit une fois, le critère de comparaison est fourni par l'appelant.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct { char nom[16]; int age; } Personne;

static int par_age(const void *a, const void *b) {
    const Personne *p = a, *q = b;
    return (p->age > q->age) - (p->age < q->age);
}
static int par_nom(const void *a, const void *b) {
    return strcmp(((const Personne *)a)->nom, ((const Personne *)b)->nom);
}

int main(void) {
    Personne t[] = {{"Zoé", 30}, {"Ada", 41}, {"Max", 25}};
    size_t n = sizeof t / sizeof t[0];
    qsort(t, n, sizeof t[0], par_age);
    for (size_t i = 0; i < n; i++) printf("%s(%d) ", t[i].nom, t[i].age);
    printf("\n");
    qsort(t, n, sizeof t[0], par_nom);
    for (size_t i = 0; i < n; i++) printf("%s(%d) ", t[i].nom, t[i].age);
    printf("\n");
    return 0;
}
```

Pour qu'un callback puisse recevoir du contexte, on ajoute classiquement un paramètre `void *contexte` transmis tel quel.

### 21.4 Table de fonctions

Un **tableau de pointeurs de fonctions** remplace avantageusement une longue cascade de `if`/`switch` :

```c
#include <stdio.h>

typedef int (*Operation)(int, int);

static int add(int a, int b) { return a + b; }
static int sub(int a, int b) { return a - b; }
static int mul(int a, int b) { return a * b; }

typedef struct { char symbole; Operation f; } Entree;

int main(void) {
    const Entree table[] = { {'+', add}, {'-', sub}, {'*', mul} };
    size_t n = sizeof table / sizeof table[0];
    char op = '*';
    for (size_t i = 0; i < n; i++) {
        if (table[i].symbole == op) { printf("%d\n", table[i].f(6, 7)); break; }   // 42
    }
    return 0;
}
```

Ajouter une opération revient à ajouter une ligne dans la table, sans toucher à la logique de recherche.

### 21.5 Simuler des méthodes (« objets » en C)

En plaçant des pointeurs de fonctions **dans une structure**, on obtient un **polymorphisme** rudimentaire :

```c
#include <stdio.h>

typedef struct Forme Forme;
struct Forme {
    double (*aire)(const Forme *);        // « méthode »
    const char *nom;
    double a, b;                          // données
};

static double aire_rect(const Forme *f)   { return f->a * f->b; }
static double aire_cercle(const Forme *f) { return 3.14159265 * f->a * f->a; }

int main(void) {
    Forme formes[] = {
        { aire_rect,   "rectangle", 3, 4 },
        { aire_cercle, "cercle",    2, 0 },
    };
    for (size_t i = 0; i < 2; i++)
        printf("%s : %.2f\n", formes[i].nom, formes[i].aire(&formes[i]));
    return 0;
}
```

C'est le principe des *vtables* de C++ et des interfaces des pilotes de périphériques (le noyau Linux utilise massivement ce modèle).

### 21.6 Sélection générique : `_Generic` (C11)

`_Generic` choisit une expression **à la compilation** selon le **type** d'un argument : c'est la base d'une surcharge rudimentaire.

```c
#include <stdio.h>

#define afficher(x) _Generic((x), \
    int:    afficher_int,        \
    double: afficher_double,     \
    char *: afficher_chaine      \
)(x)

static void afficher_int(int v)           { printf("int : %d\n", v); }
static void afficher_double(double v)     { printf("double : %.2f\n", v); }
static void afficher_chaine(char *v)      { printf("chaîne : %s\n", v); }

int main(void) {
    afficher(42);
    afficher(3.14);
    afficher((char *)"salut");
    return 0;
}
```

Le choix a lieu à la compilation : aucun coût à l'exécution. Les fonctions doivent être déclarées **avant** la macro utilisée (ici, avant `main`).

## Synthèse du niveau intermédiaire

Vous savez maintenant raisonner sur la mémoire : les **tableaux** et les **chaînes** (11–12) reposent sur la contiguïté ; les **pointeurs** (13) donnent accès aux adresses ; l'**allocation dynamique** (14) permet de choisir la taille et la durée de vie ; retourner des données (15), construire des structures dynamiques (16) et manipuler des pointeurs doubles (17) en découlent. Les **types composés** (`struct`, `union`, `enum`, `typedef`, sections 18–20) permettent de modéliser des données, et les **pointeurs de fonctions** (21) d'abstraire des comportements.

**À suivre — niveau avancé** : fichiers (22), arguments de la ligne de commande (23), préprocesseur (24), opérations bit à bit (25), récursivité (26), Unicode (27), compilation et débogage (28), comportements indéfinis et sécurité (29), bibliothèque standard et aide-mémoire (30).

# Niveau avancé

## 22. Gestion des fichiers

### 22.1 Le type `FILE *` et les opérations

Pour lire ou écrire dans un fichier, on l'**ouvre** : la bibliothèque renvoie un pointeur vers une structure opaque de type **`FILE`** qui représente un **flux** (position courante, tampon, indicateurs d'erreur et de fin de fichier). Le cycle est toujours : **ouvrir → vérifier → utiliser → fermer**.

| Fonction | Rôle |
| --- | --- |
| `fopen(chemin, mode)` | Ouvre un fichier ; renvoie `NULL` en cas d'échec |
| `fclose(f)` | Ferme (et vide le tampon) |
| `fprintf` / `fscanf` | Écriture / lecture **formatées** |
| `fputs` / `fgets` | Écriture / lecture de **chaînes** |
| `fputc` / `fgetc` | Écriture / lecture d'**un caractère** |
| `fwrite` / `fread` | Écriture / lecture de **blocs binaires** |
| `fseek` / `ftell` / `rewind` | Positionnement |
| `feof` / `ferror` | Fin de fichier / erreur |
| `fflush` | Force l'écriture du tampon |

### 22.2 Ouvrir et fermer

| Mode | Signification |
| --- | --- |
| `"r"` | Lecture ; le fichier **doit exister** |
| `"w"` | Écriture ; **crée ou écrase** (contenu perdu !) |
| `"a"` | Ajout en fin de fichier ; crée si absent |
| `"r+"` | Lecture et écriture ; doit exister |
| `"w+"` | Lecture et écriture ; crée ou écrase |
| `"a+"` | Lecture et ajout |
| suffixe `b` | Mode **binaire** (`"rb"`, `"wb"`) : indispensable sous Windows |
| suffixe `x` (C11) | Avec `w` : **échoue si le fichier existe** (`"wx"`) |

```c
#include <errno.h>
#include <stdio.h>
#include <string.h>

int main(void) {
    FILE *f = fopen("donnees.txt", "r");
    if (f == NULL) {
        fprintf(stderr, "Ouverture impossible : %s\n", strerror(errno));   // message lisible
        return 1;
    }
    /* … utilisation … */
    if (fclose(f) != 0) perror("fclose");       // fclose peut échouer (écriture différée)
    return 0;
}
```

**Toujours tester `fopen`**. `errno` (rempli par la bibliothèque) et `strerror`/`perror` donnent la cause (fichier absent, permission refusée…). Pensez à **fermer** : les données tamponnées ne sont écrites qu'à la fermeture ou lors d'un `fflush`.

### 22.3 Écrire du texte

```c
#include <stdio.h>

int main(void) {
    FILE *f = fopen("notes.txt", "w");
    if (!f) { perror("fopen"); return 1; }

    fprintf(f, "Nom : %s\n", "Ada");
    fprintf(f, "Note : %.1f\n", 17.5);
    fputs("Fin du fichier\n", f);
    fputc('!', f);
    fputc('\n', f);

    if (fclose(f) != 0) { perror("fclose"); return 1; }
    puts("notes.txt écrit");
    return 0;
}
```

### 22.4 Lire du texte

#### Ligne par ligne (recommandé)

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    FILE *f = fopen("notes.txt", "r");
    if (!f) { perror("fopen"); return 1; }

    char ligne[128];
    int numero = 0;
    while (fgets(ligne, sizeof ligne, f) != NULL) {
        ligne[strcspn(ligne, "\n")] = '\0';
        printf("%2d : %s\n", ++numero, ligne);
    }
    if (ferror(f)) perror("lecture");           // distinguer erreur et fin de fichier
    fclose(f);
    return 0;
}
```

> **Piège classique** : ne bouclez **jamais** avec `while (!feof(f))`. `feof` ne devient vrai **qu'après** une lecture qui a échoué : la dernière ligne serait traitée deux fois. Testez toujours **la valeur de retour** de la fonction de lecture (`fgets`, `fgetc`, `fread`, `fscanf`).

Si une ligne dépasse la taille du tampon, `fgets` la lit **en plusieurs fois** : vérifiez la présence du `'\n'` si la ligne entière est nécessaire.

#### Caractère par caractère

```c
#include <stdio.h>

int main(void) {
    FILE *f = fopen("notes.txt", "r");
    if (!f) return 1;
    int c;                                      // int, et non char : pour pouvoir contenir EOF
    unsigned long lignes = 0, caracteres = 0;
    while ((c = fgetc(f)) != EOF) {
        caracteres++;
        if (c == '\n') lignes++;
    }
    printf("%lu caractères, %lu lignes\n", caracteres, lignes);
    fclose(f);
    return 0;
}
```

#### Formaté avec `fscanf`

```c
#include <stdio.h>

int main(void) {
    FILE *f = fopen("mesures.txt", "w");          // fichier d'exemple : "nom valeur" par ligne
    if (!f) return 1;
    fprintf(f, "temperature 21.5\nhumidite 48.0\n");
    fclose(f);

    f = fopen("mesures.txt", "r");
    if (!f) return 1;
    char nom[32];
    double valeur;
    while (fscanf(f, "%31s %lf", nom, &valeur) == 2) {     // tester le NOMBRE de conversions
        printf("%s = %.1f\n", nom, valeur);
    }
    fclose(f);
    return 0;
}
```

`fscanf` est fragile devant des données mal formées (elle s'arrête au premier échec sans consommer le reste de la ligne). Pour des fichiers non fiables, lisez **ligne par ligne** avec `fgets`, puis analysez avec `sscanf` ou `strtol`/`strtod`.

### 22.5 Fichiers binaires

`fwrite` et `fread` transfèrent des **octets bruts**, sans conversion :

```c
#include <stdio.h>

typedef struct { int id; double solde; } Compte;

int main(void) {
    Compte comptes[] = {{1, 100.5}, {2, 250.0}, {3, 0.0}};
    size_t n = sizeof comptes / sizeof comptes[0];

    FILE *f = fopen("comptes.bin", "wb");
    if (!f) { perror("fopen"); return 1; }
    if (fwrite(comptes, sizeof comptes[0], n, f) != n) { perror("fwrite"); fclose(f); return 1; }
    fclose(f);

    Compte lus[3];
    f = fopen("comptes.bin", "rb");
    if (!f) { perror("fopen"); return 1; }
    size_t k = fread(lus, sizeof lus[0], 3, f);       // renvoie le nombre d'ÉLÉMENTS lus
    fclose(f);
    for (size_t i = 0; i < k; i++) printf("%d : %.2f\n", lus[i].id, lus[i].solde);
    return 0;
}
```

Signature : `fwrite(adresse, taille_élément, nombre, flux)`, valeur de retour = nombre d'éléments réellement transférés (comparez-la à `nombre`).

#### Texte ou binaire ?

|  | Texte | Binaire |
| --- | --- | --- |
| Lisible par l'humain | Oui | Non |
| Taille | Plus grande | Compacte |
| Portabilité | Bonne | **Fragile** : boutisme, taille des types, remplissage de structure |
| Vitesse | Plus lente (conversions) | Rapide |

> **Attention** : écrire une `struct` directement avec `fwrite` produit un fichier **lié à la machine et au compilateur** (remplissage, taille de `long`, ordre des octets). Pour un format d'échange, écrivez **champ par champ** avec des types à taille fixe (`uint32_t`…) et un ordre d'octets défini.

### 22.6 Se positionner dans un fichier

| Fonction | Effet |
| --- | --- |
| `ftell(f)` | Position courante (en octets depuis le début) |
| `fseek(f, déplacement, origine)` | Se déplace ; origine : `SEEK_SET` (début), `SEEK_CUR` (courant), `SEEK_END` (fin) |
| `rewind(f)` | Retour au début |

#### Lire un fichier entier en mémoire

```c
#include <stdio.h>
#include <stdlib.h>

// Renvoie un tampon alloué (à libérer par l'appelant), ou NULL en cas d'erreur
static char *lire_fichier(const char *chemin, size_t *taille) {
    FILE *f = fopen(chemin, "rb");
    if (!f) return NULL;

    if (fseek(f, 0, SEEK_END) != 0) { fclose(f); return NULL; }
    long n = ftell(f);
    if (n < 0) { fclose(f); return NULL; }
    rewind(f);

    char *buf = malloc((size_t)n + 1);          // +1 pour un '\0' final (utile pour du texte)
    if (!buf) { fclose(f); return NULL; }
    size_t lus = fread(buf, 1, (size_t)n, f);
    fclose(f);
    if (lus != (size_t)n) { free(buf); return NULL; }
    buf[n] = '\0';
    if (taille) *taille = (size_t)n;
    return buf;
}

int main(void) {
    size_t n;
    char *texte = lire_fichier("notes.txt", &n);
    if (!texte) { fprintf(stderr, "lecture impossible\n"); return 1; }
    printf("%zu octets lus\n%s", n, texte);
    free(texte);
    return 0;
}
```

`ftell` renvoie un `long` : sur les plateformes où `long` fait 32 bits, les fichiers de plus de 2 Go posent problème. Sous POSIX, utilisez `fseeko`/`ftello` avec `off_t`.

### 22.7 Opérations sur les fichiers

```c
#include <stdio.h>

int main(void) {
    if (rename("ancien.txt", "nouveau.txt") != 0) perror("rename");
    if (remove("temporaire.txt") != 0)            perror("remove");
    FILE *t = tmpfile();                          // fichier temporaire supprimé à la fermeture
    if (t) fclose(t);
    return 0;
}
```

Le test d'existence par `fopen(…, "r")` est valable mais à **éviter pour décider d'écrire** : entre le test et l'écriture, la situation peut changer (*race condition*). Préférez le mode `"wx"`, qui échoue de façon atomique si le fichier existe.

### 22.8 Bonnes pratiques

- **Vérifiez** chaque `fopen`, et chaque valeur de retour de `fread`/`fwrite`/`fclose`.
- **Fermez** tout fichier ouvert, y compris sur les chemins d'erreur (le schéma `goto fin` de la section 8.4 est idéal).
- Lisez en texte **ligne par ligne** avec `fgets` ; n'utilisez pas `feof` comme condition de boucle.
- Pour les fichiers venant de l'extérieur, **ne faites pas confiance** aux tailles et formats lus (validez-les avant d'allouer).
- Utilisez `"wx"` ou une écriture dans un fichier temporaire puis `rename` pour éviter la perte de données.

## 23. Arguments de la ligne de commande

### 23.1 `argc` et `argv`

La fonction `main` peut recevoir les arguments passés au programme :

```c
int main(int argc, char *argv[]) { /* ... */ }      // ou : char **argv
```

- **`argc`** (*argument count*) : nombre d'éléments, **nom du programme compris** (donc ≥ 1).
- **`argv`** (*argument vector*) : tableau de `argc` chaînes ; `argv[0]` est le nom du programme, `argv[argc]` vaut `NULL`.

```c
#include <stdio.h>

int main(int argc, char *argv[]) {
    printf("argc = %d\n", argc);
    for (int i = 0; i < argc; i++) printf("argv[%d] = \"%s\"\n", i, argv[i]);
    return 0;
}
```

```bash
./prog bonjour "le monde" 42
# argc = 4 ; argv[1] = bonjour ; argv[2] = le monde ; argv[3] = 42
```

Les guillemets du shell permettent de passer un argument contenant des espaces. **Tous les arguments sont des chaînes** : même `42` doit être converti en nombre.

### 23.2 Convertir en nombres (avec contrôle d'erreurs)

```c
#include <errno.h>
#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

static bool vers_entier(const char *s, int *resultat) {
    char *fin;
    errno = 0;
    long v = strtol(s, &fin, 10);
    if (fin == s || *fin != '\0') return false;          // aucun chiffre, ou caractères en trop
    if (errno == ERANGE || v < INT_MIN || v > INT_MAX) return false;
    *resultat = (int)v;
    return true;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage : %s <entier>\n", argv[0]);
        return EXIT_FAILURE;
    }
    int n;
    if (!vers_entier(argv[1], &n)) {
        fprintf(stderr, "« %s » n'est pas un entier valide\n", argv[1]);
        return EXIT_FAILURE;
    }
    printf("Le double de %d est %d\n", n, 2 * n);
    return EXIT_SUCCESS;
}
```

Affichez toujours un message d'**usage** sur `stderr` quand les arguments sont incorrects et retournez `EXIT_FAILURE`.

### 23.3 Exemple : somme d'entiers

```c
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    long somme = 0;
    for (int i = 1; i < argc; i++) {
        char *fin;
        errno = 0;
        long v = strtol(argv[i], &fin, 10);
        if (fin == argv[i] || *fin != '\0' || errno == ERANGE) {
            fprintf(stderr, "Argument invalide : %s\n", argv[i]);
            return EXIT_FAILURE;
        }
        somme += v;
    }
    printf("Somme = %ld\n", somme);
    return EXIT_SUCCESS;
}
```

### 23.4 Options et drapeaux

Pour des options simples (`-v`, `-n 5`, `--aide`), on compare les chaînes avec `strcmp` :

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    int verbeux = 0;
    const char *sortie = "resultat.txt";

    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-v") == 0) {
            verbeux = 1;
        } else if (strcmp(argv[i], "-o") == 0) {
            if (i + 1 >= argc) { fprintf(stderr, "-o attend un nom de fichier\n"); return EXIT_FAILURE; }
            sortie = argv[++i];                 // l'argument suivant est la valeur de l'option
        } else if (strcmp(argv[i], "--aide") == 0) {
            printf("Usage : %s [-v] [-o fichier]\n", argv[0]);
            return EXIT_SUCCESS;
        } else {
            fprintf(stderr, "Option inconnue : %s\n", argv[i]);
            return EXIT_FAILURE;
        }
    }
    printf("verbeux = %d, sortie = %s\n", verbeux, sortie);
    return EXIT_SUCCESS;
}
```

#### `getopt` (POSIX, Linux/macOS)

`getopt` (`<unistd.h>`) analyse les options courtes `-v`, `-o valeur`, y compris regroupées (`-vo fichier`) :

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    int verbeux = 0, opt;
    const char *sortie = "resultat.txt";

    while ((opt = getopt(argc, argv, "vo:")) != -1) {     // "o:" : o attend une valeur
        switch (opt) {
            case 'v': verbeux = 1; break;
            case 'o': sortie = optarg; break;               // optarg : valeur de l'option
            default:
                fprintf(stderr, "Usage : %s [-v] [-o fichier] [args…]\n", argv[0]);
                return EXIT_FAILURE;
        }
    }
    printf("verbeux = %d, sortie = %s\n", verbeux, sortie);
    for (int i = optind; i < argc; i++) printf("argument restant : %s\n", argv[i]);   // non-options
    return EXIT_SUCCESS;
}
```

`getopt` n'est **pas dans le C standard** (POSIX seulement) ; `getopt_long` gère aussi les options longues (`--verbose`).

### 23.5 Variables d'environnement

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    const char *home = getenv("HOME");              // renvoie NULL si la variable n'existe pas
    printf("HOME = %s\n", home ? home : "(non définie)");
    return 0;
}
```

La chaîne renvoyée par `getenv` appartient à l'environnement : **ne la modifiez pas** et ne la libérez pas. Traitez ces valeurs comme **non fiables** (elles viennent de l'utilisateur).

### 23.6 Bonnes pratiques

- Vérifiez `argc` **avant** d'accéder à `argv[i]`.
- Convertissez avec `strtol`/`strtod` et **validez** plage et format.
- Affichez un message d'**usage** clair ; supportez `--aide`.
- Retournez `EXIT_SUCCESS`/`EXIT_FAILURE` (le code de sortie sert aux scripts).
- Ne supposez rien sur le contenu des arguments : ils sont contrôlés par l'utilisateur (voir section 29).

## 24. Directives du préprocesseur

### 24.1 Rôle

Le **préprocesseur** est la première étape de la compilation : il traite les lignes commençant par `#` et produit un texte C « pur » **avant** que le compilateur ne l'analyse. Il travaille sur du **texte**, sans connaître les types ni la syntaxe du C. Pour voir son résultat : `gcc -E fichier.c`.

| Directive | Rôle |
| --- | --- |
| `#include` | Insère un fichier |
| `#define` / `#undef` | Définit / supprime une macro |
| `#if`, `#ifdef`, `#ifndef`, `#elif`, `#else`, `#endif` | Compilation conditionnelle |
| `#error` / `#warning` | Provoque une erreur / un avertissement |
| `#pragma` | Instruction propre au compilateur (`#pragma once`…) |
| `#embed` (C23) | Insère le contenu binaire d'un fichier |

### 24.2 `#include`

```c
#include <stdio.h>        // cherché d'abord dans les répertoires du SYSTÈME
#include "mon_module.h"   // cherché d'abord dans le répertoire du fichier courant, puis comme <…>
```

L'option `-I répertoire` ajoute un dossier de recherche. L'inclusion est une simple **copie de texte** : un en-tête inclus deux fois serait dupliqué, d'où les gardes d'inclusion (24.5).

### 24.3 `#define` : macros

```c
#include <stdio.h>

#define PI 3.14159265358979          // macro-constante (sans point-virgule !)
#define CARRE(x) ((x) * (x))         // macro avec paramètre (« fonction-macro »)
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int main(void) {
    printf("%.2f\n", PI * CARRE(2));  // PI * ((2) * (2))
    printf("%d\n", MAX(3, 7));
    return 0;
}
```

#### Pièges des macros

```c
#define CARRE_MAUVAIS(x) x * x
int a = CARRE_MAUVAIS(1 + 2);        // devient 1 + 2 * 1 + 2 = 5, et non 9 !

#define DOUBLE(x) ((x) + (x))
int i = 3;
int b = DOUBLE(i++);                  // i++ évalué DEUX fois : comportement indéfini
```

**Règles** : (1) **parenthésez** chaque paramètre et l'ensemble de l'expression ; (2) ne passez **jamais** d'argument à effet de bord (`i++`, appel de fonction) à une macro ; (3) préférez une fonction `static inline` quand c'est possible : elle est typée, évalue ses arguments une fois et est débogable.

#### Macros multi-instructions : `do { … } while (0)`

```c
#define RESET(p) do { free(p); (p) = NULL; } while (0)

if (cond) RESET(ptr);       // se comporte comme UNE instruction, même avec un else
else      autre();
```

Sans l'enveloppe `do … while (0)`, un bloc `{ … }` suivi d'un `;` casserait un `if … else`.

#### Opérateurs `#` et `##`

```c
#include <stdio.h>

#define TEXTE(x)      #x                 // # : transforme l'argument en chaîne
#define COLLER(a, b)  a##b               // ## : colle deux éléments
#define AFFICHER(v)   printf(#v " = %d\n", v)

int main(void) {
    int xy = 5, age = 30;
    printf("%s\n", TEXTE(bonjour));       // "bonjour"
    printf("%d\n", COLLER(x, y));         // xy → 5
    AFFICHER(age);                        // age = 30
    return 0;
}
```

#### Macros variadiques

```c
#include <stdio.h>

#define LOG(fmt, ...) fprintf(stderr, "[%s:%d] " fmt "\n", __FILE__, __LINE__ __VA_OPT__(,) __VA_ARGS__)

int main(void) {
    LOG("démarrage");                     // __VA_OPT__ : C23 (avant : extension ##__VA_ARGS__)
    LOG("valeur = %d", 42);
    return 0;
}
```

#### `#undef`

`#undef NOM` supprime la définition d'une macro, ce qui permet de la redéfinir ou d'éviter les collisions.

### 24.4 Compilation conditionnelle

```c
#include <stdio.h>

#define VERSION 3

int main(void) {
#if VERSION >= 3
    puts("Fonctionnalité récente");
#elif VERSION == 2
    puts("Version intermédiaire");
#else
    puts("Ancienne version");
#endif

#ifdef _WIN32
    puts("Windows");
#elif defined(__linux__)
    puts("Linux");
#elif defined(__APPLE__)
    puts("macOS");
#endif

#ifndef NDEBUG
    puts("mode debug");
#endif

#if 0
    puts("bloc désactivé (commentaire imbriquable)");
#endif
    return 0;
}
```

On définit une macro à la compilation avec `-D` : `gcc -DDEBUG=1 prog.c`. Usages : code **spécifique à une plateforme**, **options** de compilation, **tests**, **désactivation** temporaire de code (`#if 0`). L'opérateur `defined(X)` est utilisable dans `#if`. C23 ajoute `__has_include`, `__has_embed` et `__has_c_attribute` pour tester la disponibilité de fonctionnalités.

### 24.5 Gardes d'inclusion

Un en-tête inclus plusieurs fois (directement ou par d'autres en-têtes) provoquerait des **redéfinitions**. On le protège ainsi :

```c
// vecteur.h
#ifndef VECTEUR_H
#define VECTEUR_H

typedef struct { double x, y; } Vecteur;
Vecteur ajouter(Vecteur a, Vecteur b);

#endif /* VECTEUR_H */
```

Au premier passage, `VECTEUR_H` n'est pas défini : le contenu est inclus et la macro définie. Aux suivants, tout le contenu est ignoré. `#pragma once` (non standard mais universellement supporté) joue le même rôle en une ligne. **Choisissez des noms de garde uniques** (`NOMPROJET_FICHIER_H`).

### 24.6 `#embed` (C23)

`#embed` insère directement le **contenu binaire** d'un fichier sous forme de liste d'entiers : plus besoin de générateurs externes pour intégrer une image ou une police dans l'exécutable.

```c
// Compiler avec : gcc -std=c23 (GCC 15+ ou Clang 19+)
static const unsigned char logo[] = {
#embed "logo.png"
};
// sizeof logo = nombre d'octets du fichier
```

### 24.7 Macros prédéfinies

| Macro | Valeur |
| --- | --- |
| `__FILE__` | Nom du fichier source (chaîne) |
| `__LINE__` | Numéro de ligne courant (entier) |
| `__func__` | Nom de la fonction courante (variable, C99) |
| `__DATE__`, `__TIME__` | Date et heure de compilation |
| `__STDC__` | 1 si le compilateur est conforme à la norme |
| `__STDC_VERSION__` | Version de la norme (`201710L` pour C17, `202311L` pour C23) |
| `__cplusplus` | Définie **seulement** par un compilateur C++ |

### 24.8 Exemple : bascule de débogage

```c
#include <stdio.h>

#ifdef DEBUG
    #define TRACE(msg) fprintf(stderr, "[TRACE %s:%d] %s\n", __FILE__, __LINE__, (msg))
#else
    #define TRACE(msg) ((void)0)           // ne produit aucun code
#endif

int main(void) {
    TRACE("début de main");
    puts("traitement…");
    TRACE("fin de main");
    return 0;
}
```

`gcc -DDEBUG prog.c` active les traces ; sans `-DDEBUG`, elles disparaissent complètement de l'exécutable.

### 24.9 `static_assert` : vérifications à la compilation

```c
#include <limits.h>
#include <stdint.h>

static_assert(sizeof(int32_t) == 4, "int32_t doit faire 4 octets");
static_assert(CHAR_BIT == 8, "octets de 8 bits requis");
// static_assert (C23, sans <assert.h>) ; avant C23 : _Static_assert ou <assert.h>
```

Si la condition (une **expression constante**) est fausse, la compilation **échoue** avec le message donné. C'est idéal pour vérifier des hypothèses sur les tailles de types, l'alignement ou la taille d'une structure.

## 25. Opérateurs bit à bit

### 25.1 Principe

Ces opérateurs agissent sur les **bits individuels** des entiers. Ils sont indispensables pour les **drapeaux**, les protocoles, la programmation matérielle, la compression et le chiffrement.

| Opérateur | Nom | Effet | Exemple (`a = 0b1100`, `b = 0b1010`) |
| --- | --- | --- | --- |
| `&` | ET | 1 si les **deux** bits valent 1 | `a & b` = `0b1000` |
| `\|` | OU | 1 si **au moins un** vaut 1 | `a \| b` = `0b1110` |
| `^` | OU exclusif | 1 si les bits **diffèrent** | `a ^ b` = `0b0110` |
| `~` | NON | Inverse tous les bits | `~a` |
| `<<` | Décalage à gauche | Décale vers les poids forts (ajoute des 0) ; équivaut à `× 2^n` | `a << 1` = `0b11000` |
| `>>` | Décalage à droite | Décale vers les poids faibles ; équivaut à `÷ 2^n` | `a >> 2` = `0b11` |

> **À ne pas confondre** : `&` et `|` (bit à bit) avec `&&` et `||` (logiques, avec court-circuit). `5 & 2` vaut 0 mais `5 && 2` vaut 1.

### 25.2 Manipuler des bits individuels

```c
#include <stdio.h>
#include <stdint.h>

int main(void) {
    uint8_t x = 0;
    x |=  (1u << 3);                  // ACTIVER le bit 3        : 0b00001000
    x |=  (1u << 0);                  // activer le bit 0        : 0b00001001
    x &= ~(1u << 0);                  // DÉSACTIVER le bit 0     : 0b00001000
    x ^=  (1u << 5);                  // BASCULER le bit 5       : 0b00101000
    int bit3 = (x >> 3) & 1u;         // TESTER le bit 3 -> 1
    printf("x = 0x%02X, bit3 = %d\n", x, bit3);
    return 0;
}
```

Les quatre idiomes à connaître : **activer** `x |= masque`, **désactiver** `x &= ~masque`, **basculer** `x ^= masque`, **tester** `(x & masque) != 0`. Utilisez `1u` (non signé) pour éviter les décalages sur un entier signé.

### 25.3 Drapeaux (*flags*) et masques

```c
#include <stdio.h>

enum Droits { LIRE = 1u << 0, ECRIRE = 1u << 1, EXEC = 1u << 2 };

int main(void) {
    unsigned droits = LIRE | ECRIRE;            // combiner
    if (droits & ECRIRE) puts("écriture autorisée");
    droits &= ~ECRIRE;                          // retirer
    droits |= EXEC;                             // ajouter
    printf("droits = %u (lecture=%d, exec=%d)\n", droits, !!(droits & LIRE), !!(droits & EXEC));
    return 0;
}
```

Chaque drapeau occupe **un bit** (puissances de 2), ce qui permet d'en stocker 32 ou 64 dans un seul entier. Le double `!!` ramène toute valeur non nulle à 1.

### 25.4 Afficher en binaire

```c
#include <stdint.h>
#include <stdio.h>

static void afficher_binaire(uint8_t v) {
    for (int i = 7; i >= 0; i--) putchar(((v >> i) & 1u) ? '1' : '0');
    putchar('\n');
}

int main(void) {
    afficher_binaire(0xA5);        // 10100101
    afficher_binaire(5 << 2);      // 00010100
    return 0;
}
```

Le format `%b` existe en C23 pour `printf`, mais n'est pas encore partout disponible.

### 25.5 Échange sans variable temporaire (curiosité)

```c
a ^= b;  b ^= a;  a ^= b;      // échange a et b ; ÉCHOUE si a et b sont le MÊME objet (résultat 0)
```

C'est une curiosité : avec un compilateur moderne, une variable temporaire est **aussi rapide** et plus lisible.

### 25.6 Fonctions de `<stdbit.h>` (C23)

```c
// Compiler avec : gcc -std=c23 (GCC 14+ / glibc récente)
#include <stdbit.h>
#include <stdio.h>

int main(void) {
    unsigned v = 0b10110000u;
    printf("bits à 1 : %u\n", stdc_count_ones(v));            // 3
    printf("zéros de tête : %u\n", stdc_leading_zeros(v));
    printf("puissance de 2 ? %d\n", stdc_has_single_bit(v));   // 0
    return 0;
}
```

Elles remplacent les extensions propres à chaque compilateur (`__builtin_popcount`, `__builtin_clz`…).

### 25.7 Précautions

- **Décalage à gauche d'un signé** vers/dans le bit de signe, ou décalage d'un nombre de bits **négatif ou ≥ largeur du type** : comportement **indéfini**.
- **`>>` sur un entier signé négatif** : le résultat est **défini par l'implémentation** (décalage arithmétique le plus souvent). Faites vos manipulations de bits sur des types **non signés**.
- **Promotion des entiers** : `uint8_t` est promu en `int` avant l'opération ; `~x` sur un `uint8_t` donne un `int` aux bits de poids forts à 1. Reconvertissez : `(uint8_t)~x`.
- **Priorité** : `==` est plus prioritaire que `&` : écrivez `(x & m) == 0`.
- **Boutisme** (*endianness*) : l'ordre des octets en mémoire diffère selon les machines ; ne réinterprétez pas des octets sans y penser.

## 26. Récursivité

### 26.1 Principe

Une fonction est **récursive** lorsqu'elle **s'appelle elle-même**. Elle exprime naturellement les problèmes qui se décomposent en **sous-problèmes de même nature** plus petits. Toute fonction récursive correcte comporte deux éléments :

1. Un **cas de base** (condition d'arrêt) : la situation la plus simple, résolue **sans** nouvel appel.
2. Un **cas récursif** qui **se rapproche** du cas de base à chaque appel.

```c
#include <stdio.h>

static unsigned long long factorielle(unsigned n) {
    if (n <= 1) return 1;                    // cas de base
    return n * factorielle(n - 1);           // cas récursif : n! = n × (n-1)!
}

int main(void) {
    printf("5! = %llu\n", factorielle(5));   // 120
    printf("20! = %llu\n", factorielle(20)); // 2432902008176640000 (21! dépasserait 64 bits)
    return 0;
}
```

Sans cas de base, ou si le cas récursif **ne converge pas** vers lui, les appels ne s'arrêtent jamais : la pile se remplit et le programme plante (**débordement de pile**, *stack overflow*).

### 26.2 Fonctionnement : la pile d'appels

À chaque appel, le système réserve sur la **pile** un **cadre** (*stack frame*) contenant les paramètres, les variables locales et l'adresse de retour. Pour `factorielle(3)` :

```text
factorielle(3)  →  3 × factorielle(2)
                          └─ 2 × factorielle(1)
                                    └─ 1                 ← cas de base : on « remonte »
retour : 1  →  2 × 1 = 2  →  3 × 2 = 6
```

Les cadres s'**empilent** pendant la descente et se **dépilent** pendant la remontée. La mémoire consommée est proportionnelle à la **profondeur** de récursion ; la pile étant limitée (souvent 8 Mo sous Linux, 1 Mo sous Windows), une profondeur de plusieurs centaines de milliers d'appels est dangereuse.

### 26.3 Exemples

#### Puissance rapide (diviser pour régner)

```c
#include <stdio.h>

static double puissance(double x, unsigned n) {
    if (n == 0) return 1.0;
    double moitie = puissance(x, n / 2);          // UN seul appel sur n/2 : O(log n)
    return (n % 2 == 0) ? moitie * moitie : moitie * moitie * x;
}

int main(void) {
    printf("2^10 = %.0f\n", puissance(2, 10));    // 1024
    return 0;
}
```

#### Suite de Fibonacci : le piège de la double récursion

```c
#include <stdio.h>

static unsigned long fib_naif(unsigned n) {        // O(2^n) : recalcule les mêmes valeurs
    return n < 2 ? n : fib_naif(n - 1) + fib_naif(n - 2);
}

static unsigned long fib_iteratif(unsigned n) {    // O(n), mémoire constante
    unsigned long a = 0, b = 1;
    for (unsigned i = 0; i < n; i++) { unsigned long t = a + b; a = b; b = t; }
    return a;
}

int main(void) {
    printf("%lu %lu\n", fib_naif(30), fib_iteratif(30));    // 832040 832040
    return 0;
}
```

`fib_naif(40)` effectue plus de 300 millions d'appels, alors que la version itérative est instantanée. Une troisième voie est la **mémoïsation** : stocker les résultats déjà calculés dans un tableau.

#### Plus grand commun diviseur (algorithme d'Euclide)

```c
static unsigned pgcd(unsigned a, unsigned b) {
    return b == 0 ? a : pgcd(b, a % b);
}
```

#### Parcours d'une liste ou d'un arbre

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Arbre { int valeur; struct Arbre *gauche, *droite; } Arbre;

static Arbre *inserer(Arbre *a, int v) {                 // arbre binaire de recherche
    if (!a) {
        Arbre *n = calloc(1, sizeof *n);
        if (n) n->valeur = v;
        return n;
    }
    if (v < a->valeur) a->gauche = inserer(a->gauche, v);
    else               a->droite = inserer(a->droite, v);
    return a;
}

static void afficher_trie(const Arbre *a) {              // parcours infixe : ordre croissant
    if (!a) return;                                      // cas de base : arbre vide
    afficher_trie(a->gauche);
    printf("%d ", a->valeur);
    afficher_trie(a->droite);
}

static void liberer(Arbre *a) {                          // parcours postfixe : fils avant le père
    if (!a) return;
    liberer(a->gauche);
    liberer(a->droite);
    free(a);
}

int main(void) {
    Arbre *racine = NULL;
    int valeurs[] = {50, 30, 70, 20, 40, 60, 80};
    for (size_t i = 0; i < 7; i++) racine = inserer(racine, valeurs[i]);
    afficher_trie(racine);                               // 20 30 40 50 60 70 80
    printf("\n");
    liberer(racine);
    return 0;
}
```

Pour les structures **arborescentes** (arbres, répertoires, expressions), la récursivité est souvent **la solution la plus claire**.

#### Les tours de Hanoï

```c
#include <stdio.h>

static void hanoi(int n, char de, char vers, char via) {
    if (n == 0) return;
    hanoi(n - 1, de, via, vers);                  // déplacer n-1 disques vers l'étape intermédiaire
    printf("disque %d : %c -> %c\n", n, de, vers);
    hanoi(n - 1, via, vers, de);                  // puis les replacer sur la cible
}

int main(void) { hanoi(3, 'A', 'C', 'B'); return 0; }     // 2^3 - 1 = 7 déplacements
```

### 26.4 Récursivité terminale

Un appel est **terminal** lorsqu'il est la **toute dernière opération** de la fonction (rien n'est fait après son retour). On y arrive souvent avec un **accumulateur** :

```c
#include <stdio.h>

static unsigned long long fact_acc(unsigned n, unsigned long long acc) {
    if (n <= 1) return acc;
    return fact_acc(n - 1, acc * n);             // appel terminal : rien après
}
static unsigned long long fact(unsigned n) { return fact_acc(n, 1); }

int main(void) { printf("%llu\n", fact(10)); return 0; }
```

Un compilateur peut transformer un appel terminal en **simple boucle** (*optimisation des appels terminaux*) et éviter la croissance de la pile. **Le C ne le garantit pas** : GCC et Clang le font généralement avec `-O2`, mais pas en mode débogage. Ne comptez pas dessus pour des profondeurs importantes.

### 26.5 Récursivité ou itération ?

|  | Récursivité | Itération |
| --- | --- | --- |
| Clarté | Excellente pour arbres, diviser pour régner, backtracking | Excellente pour parcours linéaires |
| Mémoire | Pile proportionnelle à la profondeur | Constante |
| Vitesse | Surcoût des appels | Plus rapide |
| Risque | Débordement de pile | Aucun de ce type |

Toute récursion peut s'écrire de façon itérative (au besoin avec une **pile explicite** gérée en mémoire dynamique). Choisissez la récursivité quand elle reflète **la structure du problème** et que la profondeur reste bornée (ex. O(log n) ou hauteur d'un arbre équilibré).

### 26.6 Pièges

- **Cas de base manquant** ou jamais atteint (`fact(-1)` avec un type signé, par exemple).
- **Profondeur excessive** : listes de 10⁶ éléments parcourues récursivement.
- **Récursion exponentielle** (Fibonacci naïf) : recalculs massifs.
- **Gros tableaux locaux** dans une fonction récursive : chaque cadre les duplique.
- **Débordement arithmétique** du résultat (`21!` dépasse 64 bits) : vérifiez avec `ckd_mul`.

## 27. Unicode et caractères larges

### 27.1 Le problème

Le `char` du C est un **octet** : il suffit pour l'ASCII (128 caractères, 7 bits), pas pour le monde. **Unicode** attribue un numéro unique (un **point de code**, noté `U+XXXX`) à plus d'un million de caractères possibles (lettres de toutes les écritures, symboles, émojis). Il faut ensuite un **encodage** pour représenter ces nombres en octets :

| Encodage | Unité | Taille d'un caractère | Remarques |
| --- | --- | --- | --- |
| **UTF-8** | 1 octet | 1 à 4 octets | Compatible ASCII ; **standard du web et de Linux/macOS** |
| **UTF-16** | 2 octets | 2 ou 4 octets | Windows, Java, JavaScript |
| **UTF-32** | 4 octets | 4 octets (toujours) | Simple mais gourmand |

Conséquences pour une chaîne UTF-8 : `"é"` occupe **2 octets** ; `strlen("é")` vaut donc **2** (octets, pas caractères) ; `s[i]` n'est pas « le i-ème caractère » ; couper ou inverser une chaîne octet par octet peut produire du texte **invalide**.

### 27.2 Les approches

#### Approche 1 : UTF-8 dans des `char` (recommandée)

On garde `char *` et les fonctions habituelles ; on sait simplement que **octet ≠ caractère**. Les octets de continuation UTF-8 ont la forme `10xxxxxx`, ce qui permet de compter les caractères :

```c
#include <stdio.h>
#include <string.h>

static size_t compter_caracteres_utf8(const char *s) {
    size_t n = 0;
    for (; *s; s++) {
        if (((unsigned char)*s & 0xC0) != 0x80) n++;     // on ignore les octets de continuation
    }
    return n;
}

int main(void) {
    const char *texte = "héllo, 世界";
    printf("%s : %zu octets, %zu caractères\n", texte, strlen(texte), compter_caracteres_utf8(texte));
    return 0;                  // 14 octets, 9 caractères
}
```

En C11/C23, le préfixe **`u8"…"`** garantit un littéral UTF-8, et C23 introduit le type **`char8_t`** (`<uchar.h>`). Le terminal doit lui aussi être en UTF-8 pour un bon affichage (Windows : `chcp 65001`, ou un terminal moderne).

#### Approche 2 : `wchar_t` (`<wchar.h>`)

```c
#include <locale.h>
#include <stdio.h>
#include <wchar.h>

int main(void) {
    setlocale(LC_ALL, "");                    // active la locale du système (obligatoire)
    const wchar_t *texte = L"héllo, 世界";
    wprintf(L"%ls : %zu caractères\n", texte, wcslen(texte));
    return 0;
}
```

`wchar_t` a une taille **variable selon la plateforme** : 4 octets (UTF-32) sous Linux/macOS, **2 octets** (UTF-16) sous Windows, où il ne contient donc pas un caractère entier pour les points de code hors du plan de base. Ce manque de portabilité le rend peu recommandé pour du code multiplateforme.

#### Approche 3 : `char16_t` et `char32_t` (`<uchar.h>`, C11)

```c
#include <uchar.h>

const char16_t *s16 = u"héllo";        // UTF-16
const char32_t *s32 = U"héllo 世";      // UTF-32 : un élément = un point de code
```

`char32_t` est pratique pour manipuler des **points de code** individuels ; les fonctions de conversion (`mbrtoc32`, `c32rtomb`) font le pont avec les `char *`.

### 27.3 Conseils pratiques

- **Stockez, transmettez et traitez en UTF-8** ; ne convertissez qu'aux frontières imposées par une API (Windows en UTF-16).
- Ne supposez pas que **1 caractère = 1 octet** ; ne tronquez pas une chaîne n'importe où (un caractère peut être coupé en deux).
- Un « caractère perçu » peut comporter **plusieurs points de code** (une lettre et ses accents combinants, un émoji composé) : la notion de **cluster de graphèmes** demande une bibliothèque.
- Pour le **tri, la casse et la normalisation** Unicode, utilisez une bibliothèque dédiée (**ICU**, **libunistring**, **utf8proc**) ; `toupper` et `isalpha` ne gèrent pas les caractères non ASCII.
- **Déclarez** l'encodage de vos fichiers source (UTF-8) et validez les entrées : un UTF-8 mal formé est un vecteur d'attaque.

## 28. Compilation et exécution

### 28.1 Les étapes détaillées

| Étape | Commande | Entrée → Sortie | Rôle |
| --- | --- | --- | --- |
| Préprocessing | `gcc -E prog.c` | `.c` → `.i` | Inclusions, macros, conditionnelles |
| Compilation | `gcc -S prog.c` | `.c` → `.s` | Analyse, vérification des types, assembleur |
| Assemblage | `gcc -c prog.c` | `.c` → `.o` | Code machine **non lié** (fichier objet) |
| Édition de liens | `gcc prog.o -o prog` | `.o` → exécutable | Résout les symboles, ajoute les bibliothèques |

Le fichier objet contient une **table de symboles** (les fonctions et variables qu'il définit et celles qu'il attend d'ailleurs). L'éditeur de liens les met en correspondance. `nm` et `objdump -d` permettent de les inspecter.

### 28.2 Options essentielles de `gcc` / `clang`

| Option | Effet |
| --- | --- |
| `-std=c17` / `-std=c23` | Choisit la norme |
| `-Wall -Wextra -Wpedantic` | Avertissements (corrigez-les **tous**) |
| `-Wshadow -Wconversion -Wformat=2` | Masquage, conversions risquées, formats |
| `-Werror` | Transforme les avertissements en erreurs |
| `-g` | Inclut les symboles de débogage |
| `-O0` / `-O2` / `-O3` / `-Os` | Optimisation : aucune / standard / forte / taille |
| `-o nom` | Nom du fichier de sortie |
| `-c` | S'arrête avant l'édition de liens |
| `-I dir` / `-L dir` / `-lnom` | Dossier d'en-têtes / de bibliothèques / lier `libnom` |
| `-D NOM[=val]` | Définit une macro |
| `-fsanitize=address,undefined` | Détecteurs d'erreurs à l'exécution |
| `-fanalyzer` | Analyse statique de GCC |
| `-M`, `-MMD` | Génère les dépendances pour `make` |

Une configuration de développement raisonnable :

```bash
gcc -std=c17 -Wall -Wextra -Wpedantic -Wshadow -Wconversion -g -O0 \
    -fsanitize=address,undefined prog.c -o prog
```

### 28.3 Erreurs de compilation et d'édition de liens

| Message | Cause probable |
| --- | --- |
| `error: expected ';' before …` | Point-virgule oublié (la ligne signalée est souvent **la suivante**) |
| `implicit declaration of function 'x'` | Prototype ou `#include` manquant |
| `warning: format '%d' expects …` | Format `printf` inadapté au type |
| `undefined reference to 'f'` | **Édition de liens** : définition absente (fichier `.c` non compilé, `-l` oublié) |
| `multiple definition of 'x'` | Définition d'une variable/fonction dans un `.h` inclus plusieurs fois |
| `Segmentation fault` | **Exécution** : accès mémoire invalide |

Distinguez bien les **erreurs de compilation** (le code est invalide) des **erreurs de liens** (le code est valide mais incomplet) et des **erreurs d'exécution** (le programme compile mais se comporte mal). Corrigez toujours **la première** erreur affichée.

### 28.4 Projets multi-fichiers

```bash
gcc -Wall -Wextra -std=c17 main.c maths.c outils.c -o programme     # tout en une commande

# ou, en deux temps (recompile seulement ce qui change) :
gcc -Wall -Wextra -std=c17 -c main.c   -o main.o
gcc -Wall -Wextra -std=c17 -c maths.c  -o maths.o
gcc main.o maths.o -o programme
```

Compiler **séparément** chaque `.c` en `.o` puis lier fait gagner du temps sur de gros projets : seuls les fichiers modifiés sont recompilés.

### 28.5 Automatiser avec `make`

```makefile
CC      = gcc
CFLAGS  = -std=c17 -Wall -Wextra -Wpedantic -g
OBJ     = main.o maths.o outils.o

programme: $(OBJ)
	$(CC) $(OBJ) -o $@

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

main.o: main.c maths.h outils.h        # dépendances aux en-têtes
maths.o: maths.c maths.h
outils.o: outils.c outils.h

clean:
	rm -f $(OBJ) programme

.PHONY: clean
```

Chaque **règle** a la forme `cible: dépendances` suivie de commandes **indentées par une tabulation**. `make` compare les dates de modification et ne reconstruit que ce qui est périmé. Les variables automatiques : `$@` (cible), `$<` (première dépendance), `$^` (toutes). Pour des projets plus vastes, on utilise **CMake**, **Meson** ou **Ninja**.

### 28.6 Bibliothèques

```bash
# Bibliothèque statique (.a) : copiée dans l'exécutable
gcc -c maths.c -o maths.o
ar rcs libmaths.a maths.o
gcc main.c -L. -lmaths -o programme

# Bibliothèque dynamique (.so / .dll / .dylib) : chargée à l'exécution
gcc -fPIC -shared maths.c -o libmaths.so
gcc main.c -L. -lmaths -o programme
LD_LIBRARY_PATH=. ./programme
```

|  | Statique (`.a`) | Dynamique (`.so`, `.dll`) |
| --- | --- | --- |
| Intégration | Copiée dans l'exécutable | Chargée au lancement |
| Taille de l'exécutable | Plus grande | Plus petite |
| Mise à jour de la bibliothèque | Recompilation | Remplacement du fichier |
| Dépendance à l'exécution | Aucune | La bibliothèque doit être présente |

N'oubliez pas `-lm` pour `<math.h>` sous Linux (`gcc prog.c -lm`).

### 28.7 Débogage

#### `gdb`

```bash
gcc -g -O0 -std=c17 prog.c -o prog        # -g indispensable, -O0 pour un déroulement fidèle
gdb ./prog
```

| Commande `gdb` | Effet |
| --- | --- |
| `break main` / `break fichier.c:42` | Pose un point d'arrêt |
| `run [args]` | Lance le programme |
| `next` / `step` | Ligne suivante / entre dans la fonction |
| `continue` | Reprend jusqu'au prochain arrêt |
| `print var` / `print *p` / `print tab[0]@5` | Affiche une valeur / pointée / 5 éléments |
| `backtrace` (`bt`) | Pile d'appels (très utile après un plantage) |
| `watch var` | S'arrête quand `var` change |
| `finish` / `quit` | Sort de la fonction / quitte |

Après un *segmentation fault*, `gdb ./prog` puis `run` puis `bt` indique **la ligne exacte** et **la chaîne d'appels** qui ont conduit au plantage.

#### Détecteurs d'erreurs

| Outil | Détecte |
| --- | --- |
| **AddressSanitizer** (`-fsanitize=address`) | Dépassements de tampon, use-after-free, double free, fuites |
| **UBSan** (`-fsanitize=undefined`) | Débordement signé, décalages invalides, déréférencement nul |
| **MemorySanitizer** (Clang : `-fsanitize=memory`) | Lecture de mémoire non initialisée |
| **ThreadSanitizer** (`-fsanitize=thread`) | Conditions de concurrence |
| **Valgrind** (`valgrind --leak-check=full ./prog`) | Fuites, accès invalides (sans recompiler) |

### 28.8 Optimisation

- **`-O0`** : aucune optimisation, idéal pour déboguer. **`-O2`** : standard pour la production. **`-O3`** : plus agressif. **`-Os`** : taille minimale.
- Le compilateur **suppose l'absence de comportement indéfini** : un bug latent peut n'apparaître qu'à `-O2`. Testez les deux.
- Les variables `volatile` empêchent le compilateur de supprimer ou de réordonner les accès (registres matériels, signaux).
- **Mesurez avant d'optimiser** (`gprof`, `perf`, `valgrind --tool=callgrind`) ; la clarté prime, et le bon algorithme vaut mieux que la micro-optimisation.
- `-flto` active l'optimisation à l'édition de liens (*link-time optimization*), à travers les fichiers.

### 28.9 Compilation croisée

La **compilation croisée** produit un exécutable pour une **autre architecture** (ARM, RISC-V, microcontrôleur) que celle de la machine de développement : `arm-linux-gnueabihf-gcc prog.c -o prog_arm`, ou `clang --target=aarch64-linux-gnu`. Il faut la **chaîne d'outils** cible et une copie de la bibliothèque C de la cible. On peut tester avec un émulateur (`qemu-arm`).

### 28.10 Environnement d'exécution

À l'exécution : (1) le système **charge** l'exécutable en mémoire et mappe les bibliothèques dynamiques ; (2) le code de démarrage (*crt0*) initialise la bibliothèque C, prépare `argc`/`argv` ; (3) il appelle **`main`** ; (4) à la fin de `main` (ou à l'appel de `exit()`), les fichiers ouverts sont fermés, les fonctions `atexit` sont exécutées, puis le **code de sortie** est transmis au système.

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

|  | Fonctions de la bibliothèque C | Appels système |
| --- | --- | --- |
| Exemples | `printf`, `fopen`, `malloc` | `write`, `open`, `brk`/`mmap` |
| Portabilité | Standard C | Dépend du système (POSIX, API Windows) |
| Rôle | Couche confortable et **tamponnée** | Interface directe avec le noyau |

`printf` finit par appeler `write` ; `malloc` s'appuie sur `brk`/`mmap`. La bibliothèque C ajoute **tampons** et **portabilité**. `strace ./prog` (Linux) affiche les appels système effectués.

## 29. Comportements indéfinis et sécurité

### 29.1 Comportement indéfini (UB)

Quand un programme viole une règle du langage, **la norme n'impose aucun résultat** : plantage, résultat faux, **ou apparente normalité** (avant de casser avec un autre compilateur, une autre version ou un autre niveau d'optimisation). Le compilateur est en droit de **supposer que l'UB n'arrive jamais** et d'optimiser en conséquence : le code qui le contient peut être **supprimé ou transformé** de façon surprenante.

La norme distingue trois degrés : **comportement défini par l'implémentation** (documenté : ex. la taille de `int`), **non spécifié** (plusieurs possibilités valides : ex. l'ordre d'évaluation des arguments), **indéfini** (aucune garantie). Seul le dernier est dangereux.

| Catégorie | Exemples |
| --- | --- |
| **Mémoire** | Accès hors bornes, déréférencement de `NULL`, use-after-free, double free, lecture d'une variable non initialisée |
| **Arithmétique** | Débordement d'entier **signé**, division par zéro, décalage invalide |
| **Pointeurs** | Arithmétique hors d'un objet, violation de l'alias strict, alignement incorrect |
| **Appels** | Mauvais format dans `printf`, mauvais nombre ou type d'arguments variadiques |
| **Séquencement** | `i = i++ + ++i;` (modifications non séquencées) |
| **Chaînes** | Modifier un littéral, oublier le `'\0'` |

**Un exemple d'optimisation surprenante** :

```c
int f(int *p) {
    int v = *p;              // déréférencement : le compilateur en déduit que p != NULL…
    if (p == NULL) return -1; // …et peut donc SUPPRIMER ce test, jugé inutile
    return v;
}
```

Le test de nullité placé **après** le déréférencement est éliminé, car si `p` était nul l'UB aurait déjà eu lieu. Vérifiez **avant** d'utiliser.

### 29.2 Les failles de sécurité typiques

| Faille | Cause | Parade |
| --- | --- | --- |
| **Dépassement de tampon** | `gets`, `strcpy`, `scanf("%s")`, indices non vérifiés | `fgets`, `snprintf`, bornes vérifiées |
| **Chaîne de format** | `printf(saisie_utilisateur)` : l'attaquant fournit des `%x`, `%n` | `printf("%s", saisie)` |
| **Dépassement d'entier avant allocation** | `malloc(n * taille)` avec `n` énorme : alloue trop peu | `calloc`, `ckd_mul` (C23), vérification explicite |
| **Use-after-free / double free** | Gestion de propriété floue | `ptr = NULL` après `free`, conventions de propriété, sanitizers |
| **Lecture de mémoire non initialisée** | Variable locale non initialisée | Initialiser, `-Wall`, MemorySanitizer |
| **Condition de concurrence (TOCTOU)** | Tester puis agir (`access` puis `fopen`) | Opérations atomiques (`"wx"`) |
| **Injection de commande** | `system("ls " + saisie)` | Éviter `system`, valider les entrées |
| **Mauvais aléa** | `rand()` pour de la cryptographie | Source cryptographique du système (`getrandom`, `/dev/urandom`) |

Principe directeur : **toute donnée venant de l'extérieur est hostile** (arguments, variables d'environnement, fichiers, réseau, saisie). On la **valide** (taille, plage, format) **avant** de s'en servir.

### 29.3 Hygiène de programmation

- Compilez avec `-Wall -Wextra -Wpedantic` et corrigez **tous** les avertissements.
- Développez avec **AddressSanitizer + UBSan** activés ; testez aussi avec **Valgrind**.
- **Validez toutes les entrées** (taille, plage, format) et toutes les valeurs de retour.
- Passez **toujours la taille** avec un pointeur de tampon (`ptr, taille`).
- Initialisez variables et pointeurs ; mettez à `NULL` après `free`.
- Utilisez `const`, `size_t`, types à taille fixe.
- Réduisez la portée ; évitez les variables globales.
- Relisez le code (revue), utilisez des analyseurs statiques (`clang-tidy`, `cppcheck`, `-fanalyzer`) et des tests automatisés (CUnit, Unity, Criterion, ou `assert`).
- Pour du code critique, appliquez des règles reconnues : **SEI CERT C**, **MISRA C**.

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
    assert(vide != NULL);       // échec : message sur stderr puis arrêt (SIGABRT)
    printf("jamais affiché\n");
    return 0;
}
```

`assert` sert à vérifier des **invariants internes** (« cela ne peut pas arriver »), **pas** à gérer des erreurs d'exécution normales (fichier absent, saisie invalide) : il disparaît avec `-DNDEBUG`.

## 30. Bibliothèque standard et aide-mémoire

### 30.1 En-têtes principaux

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
| `<wchar.h>` / `<uchar.h>` / `<locale.h>` | Caractères larges, Unicode, localisation |

#### Nombres aléatoires

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

`rand()` est un générateur **pseudo-aléatoire** prévisible : sans `srand`, il produit la **même suite** à chaque exécution ; le `% n` introduit un léger biais. Pour de la sécurité, utilisez les sources du système d'exploitation.

### 30.2 Récapitulatif par thème

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

### 30.3 Les 12 règles d'or du C

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

### 30.4 Ressources pour progresser

- **cppreference (C)** : https://en.cppreference.com/w/c
- *Le langage C* — Kernighan & Ritchie (*The C Programming Language*, 2ᵉ éd.)
- *Modern C* — Jens Gustedt (gratuit en ligne)
- **SEI CERT C Coding Standard** : https://wiki.sei.cmu.edu/confluence/display/c
- **Compiler Explorer** : https://godbolt.org
- **Brouillons de la norme (WG14)** : https://www.open-std.org/jtc1/sc22/wg14/
- **Normes ISO/IEC 9899** : https://www.iso.org/standard/82075.html

## Conclusion

Vous avez parcouru l'ensemble du langage : de la syntaxe et des types (niveau débutant), à la maîtrise de la mémoire, des pointeurs et des types composés (niveau intermédiaire), puis aux fichiers, au préprocesseur, aux bits, à la compilation et à la sécurité (niveau avancé). Le C récompense la **rigueur** : vérifier, initialiser, borner, libérer, et laisser les outils (avertissements, sanitizers, analyseurs) traquer ce que l'œil manque.

*Bon code, et que vos pointeurs soient toujours valides !*
