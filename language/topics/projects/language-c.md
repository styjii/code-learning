# 🔵 Projets en langage C

> Trois mini-projets pour pratiquer le C : un **gestionnaire d'enregistrements** (`typedef`, structures, mémoire dynamique), un **analyseur de fichiers** en ligne de commande et un **listage récursif de dossiers** (POSIX). Le code vise le **standard C17** et passe sans avertissement avec `-Wall -Wextra`.

## 📑 Sommaire

1. [Contexte : compiler et exécuter](#1-contexte--compiler-et-exécuter)
2. [Projet 1 : gestionnaire d'étudiants avec `typedef`](#2-projet-1--gestionnaire-détudiants-avec-typedef)
3. [Projet 2 : analyseur de fichiers (`file_stats`)](#3-projet-2--analyseur-de-fichiers-file_stats)
4. [Projet 3 : listage récursif d'un dossier (POSIX)](#4-projet-3--listage-récursif-dun-dossier-posix)
5. [Concepts abordés](#5-concepts-abordés)
6. [Pour aller plus loin](#6-pour-aller-plus-loin)

---

## 1. Contexte : compiler et exécuter

Un programme C dépend fortement de son **contexte de compilation et d'exécution** : standard du langage, compilateur, système d'exploitation. Cette section est commune aux trois projets, ce qui évite de répéter les commandes plus loin.

### Compiler

```bash
gcc -std=c17 -Wall -Wextra -Wpedantic -g fichier.c -o programme
```

| Option | Rôle |
| --- | --- |
| `-std=c17` | Fixe le standard du langage. Selon la version du compilateur, le standard par défaut peut être plus récent (C23 pour les versions récentes de GCC) ou être une variante GNU : l'indiquer rend la compilation reproductible. |
| `-Wall -Wextra -Wpedantic` | Active la plupart des avertissements utiles. **Lisez-les** : ils signalent beaucoup de bugs. |
| `-g` | Ajoute les informations de débogage (pour `gdb` ou `lldb`). |
| `-fsanitize=address,undefined` | Détecte à l'exécution les dépassements de tampon, les fuites mémoire et les comportements indéfinis (`-g` recommandé). |

> 💡 **Réflexe moderne** : pendant le développement, compilez avec `-fsanitize=address,undefined`. Sous Linux, `valgrind ./programme` est une autre façon de traquer les fuites de mémoire.

### Selon votre système

| | 🐧 Linux | 🍎 macOS | 🪟 Windows |
| --- | --- | --- | --- |
| Compilateur | `gcc` ou `clang` | `clang` (la commande `gcc` en est un alias) | MinGW-w64 (`gcc`), MSVC (`cl`) ou **WSL** |
| Projets 1 et 2 | ✅ | ✅ | ✅ |
| Projet 3 (POSIX) | ✅ | ✅ | ⚠️ via **WSL** (MSVC n'a pas `dirent.h`) |
| Accents dans le terminal | UTF-8 par défaut | UTF-8 par défaut | `chcp 65001` pour passer en UTF-8 |

### Le C moderne en un coup d'œil

- **C99** : déclaration des variables au milieu d'un bloc, `for (int i = 0; ...)`, `snprintf`, `stdbool.h`.
- **C11** : `_Static_assert`, `_Generic`, fonctions plus sûres en option.
- **C23** : `bool`, `true`, `false` et `nullptr` deviennent des mots-clés, et `constexpr` fait son apparition. Le code ci-dessous reste volontairement compatible C17.

---

## 2. Projet 1 : gestionnaire d'étudiants avec `typedef`

### Objectif

Gérer une liste d'enregistrements d'étudiants (identifiant, nom, note) :

- ➕ saisir les étudiants ;
- 📋 afficher tous les enregistrements.

### Étape 1 : définir la structure avec `typedef`

```c
typedef struct {
    int   id;
    char  nom[50];
    float note;
} Etudiant;
```

> `Etudiant` est un **alias** de la structure : on écrit `Etudiant e;` au lieu de `struct Etudiant e;`.

### Étape 2 : un alias pour le pointeur

```c
typedef Etudiant *EtudiantPtr;
```

> Cet alias raccourcit les signatures de fonctions.

> ⚠️ **À utiliser avec prudence.** Beaucoup de guides de style déconseillent de cacher un pointeur derrière un `typedef`, car on ne voit plus qu'il s'agit d'un pointeur. Piège classique : `const EtudiantPtr p` signifie **pointeur constant** vers un étudiant modifiable, et *pas* « pointeur vers un étudiant constant ». C'est pourquoi la fonction d'affichage ci-dessous utilise `const Etudiant *` directement.

### Programme complet : `etudiants.c`

```c
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAILLE_NOM 50

// --- Types ---------------------------------------------------------------
typedef struct {
    int   id;
    char  nom[TAILLE_NOM];
    float note;
} Etudiant;

typedef Etudiant *EtudiantPtr;

// --- Déclarations des fonctions ----------------------------------------------
static bool lire_ligne(char *tampon, size_t taille);
static bool saisir_etudiant(EtudiantPtr e);
static void afficher_etudiants(const Etudiant *liste, int nombre);

int main(void) {
    char ligne[64];
    int nombre;

    printf("Nombre d'étudiants : ");
    if (!lire_ligne(ligne, sizeof ligne) || sscanf(ligne, "%d", &nombre) != 1 || nombre <= 0) {
        fprintf(stderr, "Nombre invalide.\n");
        return EXIT_FAILURE;
    }

    // Allocation dynamique (calloc initialise à zéro et détecte les débordements)
    EtudiantPtr liste = calloc((size_t)nombre, sizeof *liste);
    if (liste == NULL) {
        fprintf(stderr, "Échec de l'allocation mémoire.\n");
        return EXIT_FAILURE;
    }

    for (int i = 0; i < nombre; i++) {
        printf("\nÉtudiant %d :\n", i + 1);
        if (!saisir_etudiant(&liste[i])) {
            fprintf(stderr, "Saisie invalide ou interrompue.\n");
            free(liste);
            return EXIT_FAILURE;
        }
    }

    printf("\nEnregistrements :\n");
    afficher_etudiants(liste, nombre);

    free(liste); // Toujours libérer la mémoire allouée
    return EXIT_SUCCESS;
}

// Lit une ligne sans jamais dépasser `taille` et sans laisser de reste dans stdin
static bool lire_ligne(char *tampon, size_t taille) {
    if (fgets(tampon, (int)taille, stdin) == NULL) {
        return false; // Fin de l'entrée (Ctrl+D) ou erreur
    }

    char *fin = strchr(tampon, '\n');
    if (fin != NULL) {
        *fin = '\0';
    } else {
        int c; // Ligne trop longue : on vide le reste
        while ((c = getchar()) != '\n' && c != EOF) { }
    }
    return true;
}

// Saisit un seul étudiant ; renvoie false si une saisie est invalide
static bool saisir_etudiant(EtudiantPtr e) {
    char ligne[64];

    printf("ID : ");
    if (!lire_ligne(ligne, sizeof ligne) || sscanf(ligne, "%d", &e->id) != 1) {
        return false;
    }

    printf("Nom : ");
    if (!lire_ligne(e->nom, sizeof e->nom)) {
        return false;
    }

    printf("Note : ");
    if (!lire_ligne(ligne, sizeof ligne) || sscanf(ligne, "%f", &e->note) != 1) {
        return false;
    }
    return true;
}

// Affiche tous les étudiants (lecture seule : `const`)
static void afficher_etudiants(const Etudiant *liste, int nombre) {
    for (int i = 0; i < nombre; i++) {
        printf("ID : %d, Nom : %s, Note : %.2f\n",
               liste[i].id, liste[i].nom, liste[i].note);
    }
}
```

Compilation (voir la [section 1](#1-contexte--compiler-et-exécuter)) :

```bash
gcc -std=c17 -Wall -Wextra -g etudiants.c -o etudiants && ./etudiants
```

### Ce qui a été corrigé par rapport à l'original

| Problème dans l'original | Correction |
| --- | --- |
| `scanf(" %[^\n]", nom)` **sans limite** : un nom de plus de 49 caractères écrase la mémoire (*buffer overflow*) | Lecture avec `fgets` et une taille maximale |
| Retour de `scanf` jamais vérifié : une lettre à la place d'un nombre laisse la variable non initialisée | `sscanf(...) != 1` est testé à chaque saisie |
| `count` non validé : `0` ou un nombre négatif donne un `malloc` absurde | Contrôle `nombre <= 0` |
| `(StudentPtr) malloc(count * sizeof(Student))` : conversion inutile en C et multiplication pouvant déborder | `calloc(n, sizeof *liste)`, sans conversion |
| `addStudent(list, index)` : fonction qui doit connaître un tableau et un indice | `saisir_etudiant(&liste[i])` ne reçoit que **l'élément** à remplir |
| Fonction d'affichage pouvant modifier les données | Paramètre `const Etudiant *` |
| `return 1` | `EXIT_FAILURE` / `EXIT_SUCCESS` (plus lisible et portable) |
| Messages d'erreur envoyés sur la sortie standard | Envoyés sur `stderr` |

### Points forts du programme

| Fonctionnalité | Exemple |
| --- | --- |
| `typedef` pour une structure | `typedef struct { ... } Etudiant;` |
| Alias de pointeur | `typedef Etudiant *EtudiantPtr;` |
| Signatures plus claires | `static bool saisir_etudiant(EtudiantPtr e);` |
| Mémoire dynamique | `calloc((size_t)nombre, sizeof *liste);` |
| Saisie sécurisée | `fgets` + `sscanf` |
| Fonctions internes au fichier | `static` |

---

## 3. Projet 2 : analyseur de fichiers (`file_stats`)

### Objectif

Un outil en ligne de commande qui prend un fichier texte et affiche :

- le nombre de **lignes** ;
- le nombre de **mots** ;
- le nombre de **caractères** (ici, d'**octets**).

### Fonctionnalités

- nom du fichier passé en **argument de la ligne de commande** ;
- **gestion des erreurs** (fichier introuvable, erreur de lecture) ;
- **message d'aide** si l'argument est absent.

### Programme : `file_stats.c`

```c
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage : %s fichier.txt\n", argv[0]);
        return EXIT_FAILURE;
    }

    // "rb" : lecture binaire, pour compter les octets réels (même résultat que `wc -c`)
    FILE *fp = fopen(argv[1], "rb");
    if (fp == NULL) {
        perror(argv[1]);
        return EXIT_FAILURE;
    }

    unsigned long lignes = 0, mots = 0, caracteres = 0;
    bool dans_un_mot = false;
    int c; // `int` et non `char` : EOF vaut -1 et doit pouvoir être distingué d'un octet

    while ((c = fgetc(fp)) != EOF) {
        caracteres++;

        if (c == '\n') {
            lignes++;
        }

        if (isspace(c)) {
            dans_un_mot = false;
        } else if (!dans_un_mot) {
            dans_un_mot = true;
            mots++; // Début d'un nouveau mot
        }
    }

    if (ferror(fp)) { // La boucle s'est-elle arrêtée sur une erreur plutôt que sur la fin du fichier ?
        perror("Erreur de lecture");
        fclose(fp);
        return EXIT_FAILURE;
    }
    fclose(fp);

    printf("Fichier    : %s\n", argv[1]);
    printf("Lignes     : %lu\n", lignes);
    printf("Mots       : %lu\n", mots);
    printf("Caractères : %lu\n", caracteres);

    return EXIT_SUCCESS;
}
```

### Utilisation

**1. Compiler** (options détaillées en [section 1](#1-contexte--compiler-et-exécuter)) :

```bash
gcc -std=c17 -Wall -Wextra -g file_stats.c -o file_stats
```

**2. Créer un fichier d'exemple** :

```bash
printf "Hello world\nThis is a test file.\n" > sample.txt
```

> ⚠️ L'original utilisait `echo "...\n..."`. Or `echo` n'interprète pas toujours `\n` : selon le shell, le fichier contient alors un `\n` **littéral** sur une seule ligne et les résultats sont faux. `printf` se comporte de la même façon partout.

**3. Lancer le programme** :

```bash
./file_stats sample.txt
```

Résultat attendu :

```text
Fichier    : sample.txt
Lignes     : 2
Mots       : 7
Caractères : 33
```

> ✅ **Vérification** : la commande système `wc sample.txt` doit afficher `2 7 33`.

### Ce qui a été corrigé par rapport à l'original

- **`char ch`** devient **`int c`** : avec un `char`, la comparaison à `EOF` est incorrecte (boucle infinie possible, ou arrêt prématuré sur l'octet `0xFF` selon la plateforme).
- Le retour d'une **erreur de lecture** est détecté avec `ferror()`, au lieu d'être confondu avec la fin du fichier.
- Les compteurs sont des `unsigned long` : un `int` déborderait sur un très gros fichier.
- Le message d'utilisation et les erreurs vont sur `stderr`.
- `perror(argv[1])` indique **quel fichier** pose problème.
- Le fichier est ouvert en mode binaire (`"rb"`) pour compter des octets de façon identique sous Windows et Unix.
- La création du fichier de test utilise `printf` à la place de `echo`.
- L'include `<stdlib.h>` n'était utilisé que maintenant : pour `EXIT_FAILURE` et `EXIT_SUCCESS`.

> ℹ️ **Limite connue** : le programme compte des **octets**. Pour un texte UTF-8 contenant des accents (`é` = 2 octets), le nombre de caractères réels sera plus petit. Une dernière ligne sans `\n` final n'est pas comptée comme ligne (comportement identique à `wc -l`).

---

## 4. Projet 3 : listage récursif d'un dossier (POSIX)

> ⚠️ **Avancé, systèmes POSIX uniquement** (Linux, macOS, WSL). Ce projet utilise les appels système `opendir`, `readdir` et `lstat`.

### Objectif

Lister tous les fichiers et sous-dossiers d'une arborescence, de façon **récursive**.

### Programme : `liste_rec.c`

```c
#define _POSIX_C_SOURCE 200809L // Expose lstat(), etc. même avec -std=c17

#include <dirent.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>

static void lister_dossier(const char *chemin) {
    DIR *dp = opendir(chemin);
    if (dp == NULL) {
        perror(chemin); // Ex. : permission refusée
        return;
    }

    struct dirent *entree;
    while ((entree = readdir(dp)) != NULL) {
        // Ignorer le dossier courant et le dossier parent
        if (strcmp(entree->d_name, ".") == 0 || strcmp(entree->d_name, "..") == 0) {
            continue;
        }

        char chemin_complet[PATH_MAX];
        int n = snprintf(chemin_complet, sizeof chemin_complet,
                         "%s/%s", chemin, entree->d_name);
        if (n < 0 || (size_t)n >= sizeof chemin_complet) {
            fprintf(stderr, "Chemin trop long : %s/%s\n", chemin, entree->d_name);
            continue;
        }

        printf("%s\n", chemin_complet);

        // lstat() ne suit PAS les liens symboliques (évite les boucles infinies)
        struct stat infos;
        if (lstat(chemin_complet, &infos) == 0 && S_ISDIR(infos.st_mode)) {
            lister_dossier(chemin_complet); // Appel récursif
        }
    }

    closedir(dp);
}

int main(int argc, char *argv[]) {
    const char *racine = (argc > 1) ? argv[1] : ".";
    lister_dossier(racine);
    return EXIT_SUCCESS;
}
```

```bash
gcc -std=c17 -Wall -Wextra -g liste_rec.c -o liste_rec
./liste_rec           # Dossier courant
./liste_rec /etc      # Un dossier précis
```

### Ce qui a été corrigé par rapport à l'original

| Problème dans l'original | Correction |
| --- | --- |
| **Pas de `main()`** : le fichier ne pouvait pas être compilé en programme | `main()` ajouté, avec un dossier de départ optionnel |
| `stat()` **suit les liens symboliques** : un lien vers un dossier parent provoque une **récursion infinie** | `lstat()` |
| Tampon de 512 octets : les chemins plus longs étaient tronqués **sans avertissement** | `PATH_MAX` et contrôle du retour de `snprintf` |
| Échec de `opendir` ignoré | `perror(chemin)` indique la cause |
| Aucun `#define` de fonctionnalités : `lstat` n'est pas déclaré avec `-std=c17` strict | `#define _POSIX_C_SOURCE 200809L` |

### Alternative standard POSIX : `nftw()`

Plutôt que d'écrire la récursion soi-même, POSIX fournit `nftw()` (*new file tree walk*) : elle gère les liens symboliques, la limite de descripteurs de fichiers ouverts et les erreurs.

```c
#define _XOPEN_SOURCE 700

#include <ftw.h>
#include <stdio.h>
#include <stdlib.h>

// Appelée pour chaque fichier ou dossier rencontré
static int afficher(const char *chemin, const struct stat *infos,
                    int type, struct FTW *position) {
    (void)infos; (void)type; (void)position; // Paramètres inutilisés ici
    printf("%s\n", chemin);
    return 0; // 0 : continuer le parcours
}

int main(int argc, char *argv[]) {
    const char *racine = (argc > 1) ? argv[1] : ".";

    // 16 : nombre maximal de descripteurs ouverts ; FTW_PHYS : ne pas suivre les liens
    if (nftw(racine, afficher, 16, FTW_PHYS) == -1) {
        perror("nftw");
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}
```

> 💡 La version manuelle sert à **comprendre la récursion** ; en pratique, préférez `nftw()`.

---

## 5. Concepts abordés

| Concept | Projet 1 | Projet 2 | Projet 3 |
| --- | :---: | :---: | :---: |
| `typedef` (structure, pointeur) | ✅ | | |
| Structures (`struct`) | ✅ | | |
| Pointeurs et arithmétique de tableaux | ✅ | | |
| Mémoire dynamique (`calloc`, `free`) | ✅ | | |
| `const` (lecture seule) | ✅ | | |
| Saisie sécurisée (`fgets`, `sscanf`) | ✅ | | |
| Fichiers (`fopen`, `fgetc`, `fclose`, `ferror`) | | ✅ | |
| Arguments de la ligne de commande (`argc`, `argv`) | | ✅ | ✅ |
| Codes de retour (`EXIT_SUCCESS`, `EXIT_FAILURE`) | ✅ | ✅ | ✅ |
| Flux d'erreur (`stderr`, `perror`) | ✅ | ✅ | ✅ |
| Machine à états simple (`dans_un_mot`) | | ✅ | |
| Appels système POSIX (`opendir`, `readdir`, `lstat`) | | | ✅ |
| Récursivité | | | ✅ |

---

## 6. Pour aller plus loin

### Projet 1

- **Rechercher** un étudiant par identifiant ou par nom (`strcmp`, `strstr`).
- **Trier** par note avec `qsort`, en utilisant un `typedef` de pointeur de fonction (avancé) :

  ```c
  typedef int (*Comparateur)(const void *, const void *);

  // Tri par note décroissante
  static int comparer_notes(const void *a, const void *b) {
      const Etudiant *ea = a, *eb = b;
      return (ea->note < eb->note) - (ea->note > eb->note);
  }

  Comparateur cmp = comparer_notes;
  qsort(liste, (size_t)nombre, sizeof *liste, cmp);
  ```

- **Sauvegarder et charger** dans un fichier : privilégiez un format texte (CSV avec `fprintf` / `fgets`) plutôt que `fwrite` d'une structure brute, dont la représentation en mémoire dépend de la machine.
- **Faire grandir la liste** dynamiquement avec `realloc` au lieu de demander le nombre à l'avance.

### Projet 2

- Compter la **fréquence** de chaque caractère ou de chaque mot.
- Accepter **plusieurs fichiers** et afficher un total.
- Ajouter des options `--lines`, `--words`… avec `getopt()` (POSIX) ou `getopt_long()`.
- Écrire le résultat dans un **fichier de rapport**.
- Gérer l'**UTF-8** pour compter de vrais caractères et non des octets.

### Projet 3

- Afficher une **indentation** selon la profondeur, façon commande `tree`.
- Afficher la **taille** et le **type** de chaque entrée avec les informations de `lstat`.
- **Trier** les entrées avec `scandir()` (readdir ne garantit aucun ordre).
- Filtrer par **extension** (`.c`, `.h`…).
