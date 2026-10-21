<div align="center">

# 🧮 Algorithmique — Guide complet

**Des fondements à la programmation dynamique, aux graphes et aux flots**

*Exemples en Python 3.12+ · Mis à jour en octobre 2026*

</div>

---

## 🧰 Outils

| Ressource | Lien |
| --- | --- |
| 📝 Exercices | [exercise](/language/exercises/algorithm) |
| ✅ Solutions | [solutions](/language/solutions/algorithm) |

---

## 🗂️ Sommaire

**🟢 Niveau débutant**

1. [Introduction aux algorithmes](#1-introduction-aux-algorithmes)
2. [Analyse des algorithmes](#2-analyse-des-algorithmes)
3. [Structures de données essentielles](#3-structures-de-données-essentielles)
4. [Récursivité de base](#4-récursivité-de-base)
5. [Algorithmes de tri simples](#5-algorithmes-de-tri-simples)
6. [Algorithmes de recherche](#6-algorithmes-de-recherche)
7. [Algorithmes mathématiques de base](#7-algorithmes-mathématiques-de-base)

**🟡 Niveau intermédiaire**

8. [Algorithmes de tri avancés](#8-algorithmes-de-tri-avancés)
9. [Diviser pour régner](#9-diviser-pour-régner)
10. [Algorithmes gloutons](#10-algorithmes-gloutons)
11. [Retour sur trace (*backtracking*)](#11-retour-sur-trace-backtracking)
12. [Technique des deux pointeurs](#12-technique-des-deux-pointeurs)
13. [Fenêtre glissante](#13-fenêtre-glissante)
14. [Sommes préfixes et tableaux de différences](#14-sommes-préfixes-et-tableaux-de-différences)
15. [Recherche binaire sur la réponse](#15-recherche-binaire-sur-la-réponse)
16. [Algorithmes de théorie des nombres](#16-algorithmes-de-théorie-des-nombres)
17. [Hachage](#17-hachage)

**🔴 Niveau avancé**

18. [Programmation dynamique](#18-programmation-dynamique)
19. [Algorithmes sur les graphes](#19-algorithmes-sur-les-graphes)
20. [Plus courts chemins dans les graphes pondérés](#20-plus-courts-chemins-dans-les-graphes-pondérés)
21. [Composantes fortement connexes](#21-composantes-fortement-connexes)
22. [Flots dans les réseaux](#22-flots-dans-les-réseaux)
23. [Arbres de segments et arbres de Fenwick](#23-arbres-de-segments-et-arbres-de-fenwick)
24. [Algorithmes sur les chaînes](#24-algorithmes-sur-les-chaînes)
25. [Aller plus loin](#25-aller-plus-loin)

> 💡 **Légende** : *(ajout)* = notion absente du guide d'origine ; *(à jour)* = correction ou mise à jour ; les exemples utilisent Python, mais les idées s'appliquent à tout langage.

---

# 🟢 Niveau débutant

---

# 1. Introduction aux algorithmes

*Comprendre les fondements de l'informatique et de la résolution de problèmes.*

## 1.1 Qu'est-ce qu'un algorithme ?

Un **algorithme** est une **suite finie d'instructions précises et non ambiguës** qui transforme des **données d'entrée** en un **résultat** (sortie) pour résoudre un problème donné.

| Propriété | Signification |
| --- | --- |
| **Entrée** | Zéro, une ou plusieurs données |
| **Sortie** | Au moins un résultat |
| **Précision** | Chaque étape est définie sans ambiguïté |
| **Finitude** | L'algorithme se termine après un nombre fini d'étapes |
| **Efficacité** | Chaque étape est réalisable (assez simple pour être exécutée) |
| **Correction** | Il donne le résultat attendu pour **toute** entrée valide |

> 🍳 **Analogie** : une **recette de cuisine**. Les ingrédients sont l'entrée, les étapes sont l'algorithme, le plat est la sortie. Une recette imprécise ou infinie n'est pas un algorithme.

```python
def maximum(valeurs):
    """Renvoie le plus grand élément d'une liste non vide."""
    meilleur = valeurs[0]
    for v in valeurs[1:]:
        if v > meilleur:
            meilleur = v
    return meilleur

print(maximum([3, 8, 2, 9, 4]))   # 9
```

## 1.2 Pourquoi les algorithmes sont-ils importants ?

- **Efficacité** : le bon algorithme peut faire passer un calcul de **plusieurs jours à quelques secondes**.
- **Résolution de problèmes** : ils structurent la pensée (décomposer, généraliser, prouver).
- **Fondement de tout logiciel** : moteurs de recherche, GPS, compression, chiffrement, recommandations, intelligence artificielle…
- **Entretiens techniques** et compétitions de programmation.

| Taille `n` | Algorithme en O(n²) | Algorithme en O(n log n) |
| --- | --- | --- |
| 1 000 | ~1 million d'opérations | ~10 000 |
| 1 000 000 | ~10¹² (des heures) | ~2 × 10⁷ (une fraction de seconde en C++) |

## 1.3 Représenter un algorithme

| Mode | Description |
| --- | --- |
| **Langage naturel** | Étapes décrites en français |
| **Pseudo-code** | Structure proche d'un langage, sans syntaxe stricte |
| **Organigramme** | Schéma (début, actions, décisions, fin) |
| **Code** | Implémentation dans un langage |

```text
ALGORITHME TrouverMaximum(tableau)
  Entrée : un tableau non vide de nombres
  Sortie : le plus grand nombre
  max ← tableau[0]
  POUR chaque x DANS tableau FAIRE
      SI x > max ALORS max ← x
  RETOURNER max
```

```text
   ┌───────┐    ┌──────────────┐    ┌────────────┐  non   ┌───────────┐
   │ Début │───▶│ max ← t[0]   │───▶│ x > max ?  │───────▶│ Suivant   │
   └───────┘    └──────────────┘    └────────────┘        └───────────┘
                                          │ oui
                                    ┌─────▼─────┐
                                    │ max ← x   │
                                    └───────────┘
```

## 1.4 Écrire son premier algorithme

**Problème** : calculer la moyenne de trois notes.

1. Lire les trois notes `a`, `b`, `c`.
2. Calculer `somme ← a + b + c`.
3. Calculer `moyenne ← somme / 3`.
4. Afficher `moyenne`.

```python
a, b, c = 12, 15, 9
print((a + b + c) / 3)    # 12.0
```

## 1.5 Méthode pour résoudre un problème algorithmique *(ajout)*

| Étape | Question à se poser |
| --- | --- |
| 1. **Comprendre** | Quelles sont les entrées, les sorties, les contraintes (taille de `n`) ? |
| 2. **Exemples** | Petits cas, cas limites (liste vide, un seul élément, doublons, valeurs négatives) |
| 3. **Solution naïve** | Une approche *brute force*, même lente, qui est correcte |
| 4. **Optimiser** | Quelle structure de données ? Quel schéma (voir ci-dessous) ? |
| 5. **Analyser** | Complexité en temps et en espace |
| 6. **Coder et tester** | Jeux de tests, cas limites, comparaison avec la solution naïve |

> 💡 Les contraintes **guident** le choix : `n ≤ 20` → exponentiel acceptable ; `n ≤ 5 000` → O(n²) ; `n ≤ 10⁵` à `10⁶` → O(n log n) ou O(n).

## 1.6 Grandes familles d'algorithmes

| Famille | Idée | Exemples |
| --- | --- | --- |
| **Force brute** | Tout essayer | Recherche linéaire, mot de passe |
| **Diviser pour régner** | Diviser, résoudre, combiner | Tri fusion, recherche binaire |
| **Glouton** | Meilleur choix local à chaque étape | Huffman, Dijkstra, Kruskal |
| **Programmation dynamique** | Mémoriser les sous-problèmes | Sac à dos, plus longue sous-séquence |
| **Retour sur trace** | Explorer + revenir en arrière | N reines, Sudoku |
| **Algorithmes sur les graphes** | Parcours, chemins, flots | BFS, Dijkstra |
| **Algorithmes probabilistes** | Utilisent le hasard | Quicksort aléatoire, Miller-Rabin |
| **Séparation et évaluation** (*branch & bound*) | Élagage avec bornes | Voyageur de commerce exact |

## 1.7 Algorithme ou programme ?

| | Algorithme | Programme |
| --- | --- | --- |
| Nature | **Idée** abstraite, indépendante du langage | **Implémentation** concrète |
| Forme | Pseudo-code, schéma, texte | Code source dans un langage |
| Dépend de la machine | ❌ | ✅ |
| Finitude | Obligatoire | Peut tourner indéfiniment (serveur, jeu) |
| Exemple | « Trier par fusion » | `sorted(liste)` en Python |

---

# 2. Analyse des algorithmes

## 2.1 Pourquoi analyser ?

Mesurer un temps d'exécution dépend de la machine, du langage et des données. On préfère étudier **comment le coût croît avec la taille `n` de l'entrée**, indépendamment du matériel.

| Ressource | Mesure |
| --- | --- |
| **Complexité en temps** | Nombre d'opérations élémentaires en fonction de `n` |
| **Complexité en espace** | Mémoire supplémentaire utilisée en fonction de `n` |

## 2.2 Compter les opérations

```python
def somme(t):
    total = 0              # 1 opération
    for x in t:            # n itérations
        total += x         # 1 opération chacune
    return total           # 1 opération
# T(n) = n + 2  → O(n)
```

| Structure | Complexité |
| --- | --- |
| Instruction simple | O(1) |
| Boucle de `n` itérations | O(n) |
| Deux boucles imbriquées (chacune en `n`) | O(n²) |
| Boucle qui **divise** le problème par 2 à chaque tour (`while n > 1: n //= 2`) | O(log n) |
| Deux boucles successives | O(n) + O(n) = O(n) (on garde le terme dominant) |
| Appel récursif qui divise en 2 + travail linéaire | O(n log n) |

Règles : on **ignore les constantes** (`3n + 5` → `n`) et on garde le **terme dominant** (`n² + n` → `n²`).

## 2.3 Notations asymptotiques *(à jour : correction d'une erreur fréquente)*

Ces notations décrivent la **croissance d'une fonction** `f(n)` :

| Notation | Définition formelle | Lecture |
| --- | --- | --- |
| **O(g(n))** | ∃ c > 0, n₀ : `f(n) ≤ c·g(n)` pour tout `n ≥ n₀` | `f` croît **au plus** aussi vite que `g` (**borne supérieure**) |
| **Ω(g(n))** | ∃ c > 0, n₀ : `f(n) ≥ c·g(n)` pour tout `n ≥ n₀` | `f` croît **au moins** aussi vite que `g` (**borne inférieure**) |
| **Θ(g(n))** | `f` est à la fois O(g) et Ω(g) | `f` croît **exactement** comme `g` (**borne serrée**) |
| **o(g(n))** | `f(n)/g(n) → 0` | `f` croît **strictement moins vite** |

> ⚠️ **Idée reçue à éviter** : « O = pire cas, Ω = meilleur cas, Θ = cas moyen ». **C'est faux.**
> `O`, `Ω` et `Θ` sont des **bornes sur une fonction**, pas des « cas ». Les **cas** (pire, meilleur, moyen) sont **trois fonctions différentes** de `n`, et pour **chacune** on peut donner une borne `O`, `Ω` ou `Θ`.
>
> *Exemple (recherche linéaire)* : pire cas `T(n) = n` → Θ(n) ; meilleur cas `T(n) = 1` → Θ(1) ; cas moyen `T(n) ≈ n/2` → Θ(n). On dit couramment « la recherche linéaire est en O(n) » : c'est une **garantie valable dans tous les cas**.

```text
Exemple : f(n) = 3n² + 5n
   f ∈ Θ(n²)   ✅ (borne serrée)
   f ∈ O(n²), O(n³), O(2ⁿ)  ✅ (bornes supérieures, de moins en moins précises)
   f ∈ Ω(n²), Ω(n), Ω(1)    ✅ (bornes inférieures)
```

## 2.4 Pire, meilleur et cas moyen

| Cas | Définition | Utilité |
| --- | --- | --- |
| **Pire cas** | Coût maximal sur toutes les entrées de taille `n` | **Garanties** de performance |
| **Meilleur cas** | Coût minimal | Rarement informatif |
| **Cas moyen** | Espérance du coût sur une distribution d'entrées | Comportement typique (hypothèses nécessaires) |

| Algorithme | Meilleur | Moyen | Pire |
| --- | --- | --- | --- |
| Recherche linéaire | Θ(1) | Θ(n) | Θ(n) |
| Recherche binaire | Θ(1) | Θ(log n) | Θ(log n) |
| Tri par insertion | Θ(n) | Θ(n²) | Θ(n²) |
| Quicksort | Θ(n log n) | Θ(n log n) | Θ(n²) |
| Tri fusion | Θ(n log n) | Θ(n log n) | Θ(n log n) |

## 2.5 Classes de complexité usuelles

| Classe | Nom | Exemple | `n = 10⁶` (ordre de grandeur) |
| --- | --- | --- | --- |
| O(1) | Constante | Accès à un indice | 1 |
| O(log n) | Logarithmique | Recherche binaire | ~20 |
| O(√n) | Racine carrée | Test de primalité naïf | 1 000 |
| O(n) | Linéaire | Parcours | 10⁶ |
| O(n log n) | Quasi-linéaire | Tri efficace | 2 × 10⁷ |
| O(n²) | Quadratique | Deux boucles imbriquées | 10¹² ❌ |
| O(n³) | Cubique | Floyd-Warshall | ❌ |
| O(2ⁿ) | Exponentielle | Sous-ensembles | ❌ dès `n ≈ 40` |
| O(n!) | Factorielle | Permutations | ❌ dès `n ≈ 12` |

```text
Ordre de croissance :  1  <  log n  <  √n  <  n  <  n log n  <  n²  <  n³  <  2ⁿ  <  n!
```

> 🎯 **Règle pratique** : un ordinateur moderne effectue environ **10⁸ opérations simples par seconde** en langage compilé (C++), et **~10⁷** en Python pur. Cela permet d'estimer si une solution passera dans un délai donné.

## 2.6 Complexité en espace

```python
def somme_liste(t):          # O(1) espace supplémentaire
    total = 0
    for x in t: total += x
    return total

def doubles(t):              # O(n) espace supplémentaire
    return [2 * x for x in t]
```

Pensez à la **pile d'appels** : une récursion de profondeur `n` consomme O(n) d'espace (et Python limite la profondeur à ~1000 par défaut).

## 2.7 Compromis temps / espace

On peut souvent **gagner du temps en utilisant plus de mémoire** (tables de hachage, mémoïsation, tableaux de sommes préfixes) ou l'inverse.

| Technique | Gagne | Coûte |
| --- | --- | --- |
| Mémoïsation / DP | Temps (évite les recalculs) | Mémoire |
| Table de hachage | Temps (recherche O(1)) | Mémoire |
| Calcul à la volée | Mémoire | Temps |

## 2.8 Analyse amortie *(ajout)*

Le **coût amorti** est le coût **moyen par opération sur une suite d'opérations** dans le **pire cas** (≠ cas moyen probabiliste).

*Exemple : `list.append` en Python.* Une insertion est en O(1) la plupart du temps, mais coûte O(n) quand le tableau doit être **agrandi** (copie). Comme la capacité est multipliée par un facteur constant, `n` ajouts coûtent O(n) au total : **O(1) amorti** par ajout. De même, l'union-find avec compression de chemins, ou `dict` pour l'insertion.

## 2.9 Récurrences

Les algorithmes récursifs s'analysent via une **relation de récurrence** :

| Récurrence | Solution | Exemple |
| --- | --- | --- |
| `T(n) = T(n−1) + O(1)` | O(n) | Factorielle |
| `T(n) = T(n/2) + O(1)` | O(log n) | Recherche binaire |
| `T(n) = 2T(n/2) + O(n)` | O(n log n) | Tri fusion |
| `T(n) = 2T(n−1) + O(1)` | O(2ⁿ) | Fibonacci naïf, tours de Hanoï |

Voir le **théorème maître** [section 9.5](#95-le-théorème-maître).

## 2.10 Conseils pratiques

- **Mesurez** avant d'optimiser (`timeit`, `cProfile`) : la complexité théorique ignore les constantes.
- Un algorithme O(n log n) avec une grosse constante peut perdre contre un O(n²) sur de petites entrées (c'est pourquoi Timsort utilise l'insertion pour les petits blocs).
- Attention aux **opérations cachées** : `x in liste` est O(n), `liste.insert(0, x)` est O(n), `s += "a"` en boucle peut être O(n²).
- Vérifiez l'**espace** : un tableau `n × n` pour `n = 10⁵` est impossible.

```python
import timeit
print(timeit.timeit("sorted(t)", setup="import random; t=[random.random() for _ in range(10**5)]", number=10))
```

---

# 3. Structures de données essentielles

*(Section ajoutée : les algorithmes s'appuient sur des structures de données ; en voici l'essentiel.)*

## 3.1 Aperçu et complexités

| Structure | Accès | Recherche | Insertion | Suppression | Remarques |
| --- | --- | --- | --- | --- | --- |
| **Tableau / `list`** | O(1) | O(n) | O(1) amorti en fin, O(n) ailleurs | O(n) | Contigu en mémoire |
| **Liste chaînée** | O(n) | O(n) | O(1) en tête / avec nœud connu | O(1) avec nœud connu | Pas d'accès direct |
| **Pile** (LIFO) | — | — | O(1) | O(1) | `list.append` / `pop` |
| **File** (FIFO) | — | — | O(1) | O(1) | `collections.deque` |
| **Table de hachage** (`dict`, `set`) | — | O(1) moyen | O(1) moyen | O(1) moyen | Pas d'ordre de tri |
| **Tas** (*heap*) | min/max en O(1) | O(n) | O(log n) | O(log n) | `heapq` |
| **Arbre binaire de recherche équilibré** | — | O(log n) | O(log n) | O(log n) | Non fourni nativement en Python (`sortedcontainers`) |
| **Graphe** | — | — | — | — | Listes d'adjacence |

## 3.2 Pile, file et file à double entrée

```python
from collections import deque

pile = []
pile.append(1); pile.append(2)
pile.pop()                      # 2 (dernier entré, premier sorti)

file = deque()
file.append(1); file.append(2)
file.popleft()                  # 1 (premier entré, premier sorti) — O(1)
# ⚠️ list.pop(0) est en O(n) : utilisez deque pour une file
```

## 3.3 Liste chaînée

```python
class Noeud:
    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

def inverser(tete):
    precedent = None
    while tete:
        tete.suivant, precedent, tete = precedent, tete, tete.suivant
    return precedent
```

## 3.4 Tas et file de priorité

Un **tas binaire** donne accès à l'**élément minimal** en O(1) et supporte l'insertion / l'extraction en O(log n). Python propose un **tas-min** :

```python
import heapq

tas = []
for x in [5, 1, 8, 3]:
    heapq.heappush(tas, x)
heapq.heappop(tas)               # 1 (le plus petit)
heapq.heapify(liste)             # transforme une liste en tas en O(n)
heapq.nsmallest(3, liste)        # les 3 plus petits
heapq.heappush(tas, (priorite, element))     # file de priorité avec des tuples
heapq.heappush(tas, -x)          # astuce tas-max : stocker l'opposé
```

## 3.5 Arbres

```python
class NoeudArbre:
    def __init__(self, valeur):
        self.valeur, self.gauche, self.droite = valeur, None, None

def parcours_infixe(n):                    # gauche, racine, droite (trié pour un ABR)
    if n:
        yield from parcours_infixe(n.gauche)
        yield n.valeur
        yield from parcours_infixe(n.droite)
```

| Parcours | Ordre |
| --- | --- |
| **Préfixe** | racine → gauche → droite |
| **Infixe** | gauche → racine → droite |
| **Suffixe** | gauche → droite → racine |
| **Largeur** | niveau par niveau (file) |

Un **arbre binaire de recherche** (ABR) maintient `gauche < racine < droite` : recherche en O(h), où `h` est la hauteur (O(log n) s'il est équilibré — AVL, arbre rouge-noir ; O(n) dégénéré).

## 3.6 Choisir la bonne structure

| Besoin | Structure |
| --- | --- |
| Accès par indice | `list` |
| Appartenance / comptage rapide | `set`, `dict`, `Counter` |
| Dernier entré, premier sorti | pile (`list`) |
| Premier entré, premier sorti, BFS | `deque` |
| Toujours extraire le min / max | `heapq` |
| Données triées avec insertions | `bisect.insort` (petit `n`) ou arbre équilibré |
| Union / appartenance à un groupe | Union-Find (section 19) |
| Préfixes de chaînes | Trie (section 24) |

---

# 4. Récursivité de base

## 4.1 Qu'est-ce que la récursivité ?

Une fonction est **récursive** quand elle **s'appelle elle-même** pour résoudre une version plus petite du même problème.

> 🪆 **Analogie** : des poupées russes : on ouvre chacune jusqu'à la plus petite.

```python
def factorielle(n):
    if n <= 1:                       # 1. cas de base : arrête la récursion
        return 1
    return n * factorielle(n - 1)    # 2. cas récursif : problème plus petit

print(factorielle(5))   # 120
```

## 4.2 Structure d'une fonction récursive

1. **Cas de base** : la situation la plus simple, résolue directement.
2. **Appel récursif** sur un problème **strictement plus petit**.
3. **Combinaison** des résultats.

## 4.3 Fonctionnement : la pile d'appels

```text
factorielle(3)
 └─ 3 * factorielle(2)
         └─ 2 * factorielle(1)
                 └─ 1          ← cas de base
Remontée : 1 → 2×1 = 2 → 3×2 = 6
```

Chaque appel crée un **cadre** (paramètres, variables locales) empilé en mémoire.

## 4.4 Erreurs courantes

| Erreur | Conséquence |
| --- | --- |
| **Pas de cas de base** | Récursion infinie → `RecursionError` |
| **Le problème ne diminue pas** | Idem |
| **Recalculs inutiles** (Fibonacci naïf) | Complexité exponentielle |
| **Profondeur trop grande** | Dépassement de pile (limite Python ≈ 1000) |

```python
import sys
sys.setrecursionlimit(10**6)        # possible, mais risqué : préférez une version itérative
```

## 4.5 Exemples classiques

```python
def somme(t, i=0):                           # somme d'une liste
    return 0 if i == len(t) else t[i] + somme(t, i + 1)

def inverser_chaine(s):
    return s if len(s) <= 1 else inverser_chaine(s[1:]) + s[0]

def est_palindrome(s):
    return len(s) < 2 or (s[0] == s[-1] and est_palindrome(s[1:-1]))

def puissance(x, n):                          # exponentiation rapide : O(log n)
    if n == 0: return 1
    moitie = puissance(x, n // 2)
    return moitie * moitie * (x if n % 2 else 1)

def hanoi(n, source, cible, aide):            # O(2ⁿ)
    if n == 0: return
    hanoi(n - 1, source, aide, cible)
    print(f"Déplacer le disque {n} : {source} → {cible}")
    hanoi(n - 1, aide, cible, source)

def fib(n):                                   # ❌ O(2ⁿ) : à ne pas utiliser tel quel
    return n if n < 2 else fib(n - 1) + fib(n - 2)
```

### Corriger Fibonacci : mémoïsation

```python
from functools import cache

@cache                                         # Python 3.9+
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
# O(n) temps et espace
```

## 4.6 Récursivité ou itération ?

| | Récursivité | Itération |
| --- | --- | --- |
| Lisibilité | ✅ Très naturelle (arbres, diviser pour régner) | Parfois plus lourde |
| Mémoire | O(profondeur) | O(1) souvent |
| Vitesse | Surcoût des appels | Plus rapide |
| Limite | Profondeur de pile | Aucune |

> ℹ️ Python **n'optimise pas la récursion terminale** : une boucle ou une pile explicite est préférable pour de grandes profondeurs.

## 4.7 Quand l'utiliser ?

Structures **récursives par nature** (arbres, graphes, listes chaînées), **diviser pour régner**, **retour sur trace**, **programmation dynamique** descendante.

---

# 5. Algorithmes de tri simples

## 5.1 Introduction

**Trier** consiste à ordonner les éléments selon un critère. Un tri est :

- **en place** (*in-place*) s'il utilise O(1) mémoire supplémentaire ;
- **stable** s'il conserve l'ordre relatif des éléments égaux.

## 5.2 Tri à bulles (*Bubble Sort*)

On compare les voisins et on **échange** s'ils sont mal ordonnés ; les plus grands « remontent » en fin de tableau.

```python
def tri_bulles(t):
    n = len(t)
    for i in range(n - 1):
        echange = False
        for j in range(n - 1 - i):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]
                echange = True
        if not echange:          # déjà trié : arrêt anticipé → meilleur cas O(n)
            break
    return t
```

Complexité : **O(n²)** pire et moyen, **O(n)** meilleur cas (avec arrêt anticipé) · espace O(1) · **stable**.

## 5.3 Tri par sélection (*Selection Sort*)

On cherche le **minimum** du reste du tableau et on le place en tête.

```python
def tri_selection(t):
    for i in range(len(t)):
        m = min(range(i, len(t)), key=t.__getitem__)
        t[i], t[m] = t[m], t[i]
    return t
```

**Θ(n²)** dans tous les cas · espace O(1) · **non stable** · fait **peu d'échanges** (au plus n − 1).

## 5.4 Tri par insertion (*Insertion Sort*)

On construit une partie triée en **insérant** chaque élément à sa place (comme trier des cartes en main).

```python
def tri_insertion(t):
    for i in range(1, len(t)):
        cle = t[i]
        j = i - 1
        while j >= 0 and t[j] > cle:
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = cle
    return t
```

**O(n²)** pire et moyen, **O(n)** si presque trié · espace O(1) · **stable** · **excellent sur de petites listes ou des listes presque triées** (utilisé comme brique dans Timsort).

## 5.5 Comparaison

| Tri | Meilleur | Moyen | Pire | Espace | Stable | Remarque |
| --- | --- | --- | --- | --- | --- | --- |
| **Bulles** | O(n) | O(n²) | O(n²) | O(1) | ✅ | Pédagogique uniquement |
| **Sélection** | O(n²) | O(n²) | O(n²) | O(1) | ❌ | Peu d'échanges |
| **Insertion** | O(n) | O(n²) | O(n²) | O(1) | ✅ | Rapide sur petites / presque triées |

> 🐍 **En pratique** : utilisez `sorted(t)` ou `t.sort()` (**Timsort**, stable, O(n log n) pire cas, O(n) si déjà trié). Voir [section 8](#8-algorithmes-de-tri-avancés).

---

# 6. Algorithmes de recherche

## 6.1 Recherche linéaire

Parcourt les éléments un par un. Fonctionne sur **toute** liste, triée ou non.

```python
def recherche_lineaire(t, cible):
    for i, x in enumerate(t):
        if x == cible:
            return i
    return -1
```

**O(n)** pire cas, O(1) meilleur cas · O(1) espace.

## 6.2 Recherche binaire (dichotomique)

Sur une liste **triée**, on compare avec le **milieu** et on élimine **la moitié** des candidats à chaque étape.

```python
def recherche_binaire(t, cible):
    bas, haut = 0, len(t) - 1
    while bas <= haut:
        milieu = bas + (haut - bas) // 2        # évite le dépassement d'entier dans d'autres langages
        if t[milieu] == cible:
            return milieu
        if t[milieu] < cible:
            bas = milieu + 1
        else:
            haut = milieu - 1
    return -1

print(recherche_binaire([1, 3, 5, 7, 9, 11], 7))   # 3
```

**O(log n)** · O(1) espace (version itérative) · 1 milliard d'éléments → ~30 comparaisons.

### Variantes : première / dernière position, insertion

```python
from bisect import bisect_left, bisect_right, insort

t = [1, 2, 2, 2, 3]
bisect_left(t, 2)          # 1 : première position où insérer 2 (premier index de 2)
bisect_right(t, 2)         # 4 : après le dernier 2
bisect_right(t, 2) - bisect_left(t, 2)    # 3 : nombre d'occurrences
insort(t, 2)               # insère en gardant la liste triée (O(n) à cause du décalage)
```

> ⚠️ Pièges classiques : **boucle infinie** (`bas = milieu` au lieu de `milieu + 1`), **condition `bas <= haut`** oubliée, liste **non triée**.

## 6.3 Comparaison

| | Linéaire | Binaire |
| --- | --- | --- |
| Pré-requis | Aucun | **Liste triée** |
| Temps | O(n) | **O(log n)** |
| Quand | Petite liste, une seule recherche | Nombreuses recherches sur des données triées |

> 💡 Pour des appartenances **fréquentes** sur des données **non ordonnées**, un `set` (O(1)) est encore plus efficace.

---

# 7. Algorithmes mathématiques de base

## 7.1 PGCD (algorithme d'Euclide)

Principe : `pgcd(a, b) = pgcd(b, a mod b)`, avec `pgcd(a, 0) = a`.

```python
def pgcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

print(pgcd(48, 18))                 # 6
ppcm = lambda a, b: a // pgcd(a, b) * b

import math
math.gcd(48, 18); math.lcm(4, 6)    # fonctions intégrées (lcm : Python 3.9+)
```

Complexité **O(log min(a, b))**.

## 7.2 Nombres premiers : test naïf

Un nombre `n > 1` est premier s'il n'a aucun diviseur entre 2 et **√n**.

```python
from math import isqrt

def est_premier(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True
```

**O(√n)**. Pour plusieurs nombres : le **crible d'Ératosthène** ([section 16.1](#161-crible-dératosthène)) ; pour de très grands nombres : **Miller-Rabin** (section 16.5).

## 7.3 Factorielle

```python
def factorielle(n):                 # itérative : O(n)
    r = 1
    for k in range(2, n + 1): r *= k
    return r

import math; math.factorial(20)     # 2432902008176640000
```

Python gère des **entiers de taille arbitraire** (pas de débordement) ; dans d'autres langages, `21!` dépasse un entier 64 bits.

## 7.4 Suite de Fibonacci

| Méthode | Complexité | Remarque |
| --- | --- | --- |
| Récursive naïve | **O(2ⁿ)** | À éviter |
| Récursive + mémoïsation (`@cache`) | O(n) | |
| **Itérative** | O(n) temps, **O(1)** espace | Simple et efficace |
| **Doublement rapide / exponentiation de matrice** | **O(log n)** multiplications | Pour de très grands `n` |

```python
def fib_iteratif(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_doublement(n):                       # renvoie (F(n), F(n+1)) en O(log n)
    if n == 0:
        return (0, 1)
    a, b = fib_doublement(n // 2)
    c = a * (2 * b - a)                      # F(2k)
    d = a * a + b * b                        # F(2k+1)
    return (d, c + d) if n % 2 else (c, d)

fib_doublement(90)[0]                        # 2880067194370816120
```

## 7.5 Autres outils intégrés à Python *(ajout)*

```python
import math
math.isqrt(99)          # 9 : racine carrée entière exacte
math.comb(5, 2)         # 10 : combinaisons
math.perm(5, 2)         # 20 : arrangements
divmod(17, 5)           # (3, 2)
pow(2, 10, 1000)        # 24 : (2**10) % 1000, exponentiation modulaire rapide
sum(int(c) for c in str(12345))     # somme des chiffres
bin(10), int("1010", 2) # conversions de base
```

---

# 🟡 Niveau intermédiaire

---

# 8. Algorithmes de tri avancés

## 8.1 Vue d'ensemble

| Tri | Meilleur | Moyen | Pire | Espace | Stable | Principe |
| --- | --- | --- | --- | --- | --- | --- |
| **Fusion** (*merge*) | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | Diviser pour régner |
| **Rapide** (*quick*) | O(n log n) | O(n log n) | **O(n²)** | O(log n) | ❌ | Partitionnement autour d'un pivot |
| **Par tas** (*heap*) | O(n log n) | O(n log n) | O(n log n) | **O(1)** | ❌ | Tas binaire |
| **Par comptage** | O(n + k) | O(n + k) | O(n + k) | O(k) | ✅ | Compter les occurrences |
| **Radix** (par base) | O(d(n + k)) | O(d(n + k)) | O(d(n + k)) | O(n + k) | ✅ | Tri chiffre par chiffre |
| **Timsort** (Python, Java) | **O(n)** | O(n log n) | O(n log n) | O(n) | ✅ | Fusion + insertion, exploite les séquences déjà triées |

> 📐 **Borne inférieure** : tout tri **par comparaisons** exige **Ω(n log n)** comparaisons dans le pire cas. Seuls les tris **sans comparaison** (comptage, radix) font mieux, sous hypothèses sur les clés.

## 8.2 Tri fusion (*Merge Sort*)

On **divise** la liste en deux, on trie chaque moitié récursivement, puis on **fusionne** deux listes triées.

```python
def tri_fusion(t):
    if len(t) <= 1:
        return t
    milieu = len(t) // 2
    gauche, droite = tri_fusion(t[:milieu]), tri_fusion(t[milieu:])

    resultat, i, j = [], 0, 0
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:               # <= garantit la stabilité
            resultat.append(gauche[i]); i += 1
        else:
            resultat.append(droite[j]); j += 1
    return resultat + gauche[i:] + droite[j:]
```

**Θ(n log n)** garanti · O(n) espace · stable · idéal pour les **listes chaînées** et le **tri externe** (fichiers énormes). Récurrence : `T(n) = 2T(n/2) + O(n)`.

## 8.3 Tri rapide (*Quick Sort*)

On choisit un **pivot**, on **partitionne** (plus petits à gauche, plus grands à droite), puis on trie récursivement chaque côté.

```python
import random

def tri_rapide(t):
    if len(t) <= 1:
        return t
    pivot = random.choice(t)                      # pivot ALÉATOIRE : évite le pire cas sur des entrées triées
    moins   = [x for x in t if x < pivot]
    egaux   = [x for x in t if x == pivot]
    plus    = [x for x in t if x > pivot]
    return tri_rapide(moins) + egaux + tri_rapide(plus)
```

### Version en place (partition de Lomuto)

```python
import random

def tri_rapide_en_place(t, bas=0, haut=None):
    if haut is None: haut = len(t) - 1
    if bas < haut:
        i = random.randint(bas, haut)
        t[i], t[haut] = t[haut], t[i]             # pivot aléatoire placé en fin
        pivot, p = t[haut], bas
        for j in range(bas, haut):
            if t[j] < pivot:
                t[p], t[j] = t[j], t[p]; p += 1
        t[p], t[haut] = t[haut], t[p]
        tri_rapide_en_place(t, bas, p - 1)
        tri_rapide_en_place(t, p + 1, haut)
```

- **Moyen O(n log n)**, **pire O(n²)** (pivot toujours extrême : pivot fixe sur liste triée).
- Très rapide en pratique (bonne localité mémoire). Les bibliothèques C++ utilisent **introsort** (quicksort + tri par tas si la profondeur explose + insertion pour les petits blocs) ; d'autres **pdqsort** (*pattern-defeating quicksort*).
- Pour de nombreux doublons : partition **à trois voies** (comme ci-dessus, `moins / égaux / plus`).
- **Quickselect** : la même partition trouve le **k-ième plus petit élément en O(n) en moyenne** (voir 9.4).

## 8.4 Tri par tas (*Heap Sort*)

On organise les éléments en **tas** (binaire), puis on en extrait n fois la racine (le plus petit avec `heapq`, qui est un tas-min ; la version « en place » classique utilise un tas-max).

```python
import heapq

def tri_par_tas(t):
    tas = list(t)
    heapq.heapify(tas)                            # O(n)
    return [heapq.heappop(tas) for _ in range(len(tas))]   # n × O(log n)
```

**Θ(n log n)** garanti ; la version ci-dessus utilise O(n) d'espace, alors que la version « en place » classique n'en utilise que O(1) (non stable). Moins rapide que quicksort en pratique (mauvaise localité).

## 8.5 Tri par comptage (*Counting Sort*)

Pour des **entiers dans un petit intervalle** `[0, k]` : on compte les occurrences.

```python
def tri_comptage(t, k):
    compte = [0] * (k + 1)
    for x in t:
        compte[x] += 1
    return [v for v, c in enumerate(compte) for _ in range(c)]
```

**O(n + k)** · utile si `k = O(n)`. (La version stable avec sommes cumulées sert de brique au radix.)

## 8.6 Tri radix (par base)

On trie par **chiffre** (du moins au plus significatif) avec un tri **stable**.

```python
def tri_radix(t):
    if not t: return t
    exp, maximum = 1, max(t)
    while maximum // exp > 0:
        seaux = [[] for _ in range(10)]
        for x in t:
            seaux[(x // exp) % 10].append(x)
        t = [x for seau in seaux for x in seau]
        exp *= 10
    return t
```

**O(d · (n + b))** (`d` chiffres, base `b`). Pour entiers positifs ou chaînes de longueur fixe.

## 8.7 Timsort et tri en Python *(à jour, ajout)*

`sorted()` et `list.sort()` utilisent **Timsort** : il détecte les **séquences déjà triées** (*runs*), les prolonge par insertion, puis les fusionne. **Stable**, **O(n log n)** garanti, **O(n) si presque trié**. Depuis **Python 3.11**, la politique de fusion est celle de **Powersort**.

```python
t = [("Alice", 30), ("Bob", 25), ("Chloé", 30)]
sorted(t, key=lambda p: p[1])                     # tri par âge ; stabilité : Alice avant Chloé
sorted(t, key=lambda p: (-p[1], p[0]))            # âge décroissant puis nom
sorted(t, reverse=True)
```

## 8.8 Quel tri choisir ?

| Situation | Choix |
| --- | --- |
| Usage général en Python | `sorted()` / `.sort()` |
| Besoin de stabilité, garantie O(n log n) | Tri fusion |
| Mémoire très limitée | Tri par tas |
| Entiers dans un petit intervalle | Comptage / radix |
| Petits tableaux (< ~20 éléments) | Insertion |
| Trier de gros fichiers | Tri fusion externe |

---

# 9. Diviser pour régner

## 9.1 Principe

1. **Diviser** le problème en sous-problèmes **indépendants** de même nature.
2. **Régner** : résoudre chacun (récursivement ; cas de base direct).
3. **Combiner** les solutions.

| Problème | Algorithme | Complexité |
| --- | --- | --- |
| Trier | Fusion, rapide | O(n log n) |
| Chercher | Recherche binaire | O(log n) |
| Puissance | Exponentiation rapide | O(log n) |
| Multiplier des matrices | Strassen | O(n^2,81) |
| Multiplier de grands entiers | Karatsuba | O(n^1,585) |
| Paire de points la plus proche | Division du plan | O(n log n) |
| k-ième élément | Quickselect | O(n) en moyenne |
| Transformée de Fourier rapide | FFT | O(n log n) |

> ℹ️ **Diviser pour régner ≠ programmation dynamique** : ici les sous-problèmes sont **indépendants** ; en DP ils se **chevauchent** (et on les mémorise).

## 9.2 Exemple : maximum d'une liste

```python
def maximum_dc(t, bas=0, haut=None):
    if haut is None: haut = len(t) - 1
    if bas == haut:
        return t[bas]
    milieu = (bas + haut) // 2
    return max(maximum_dc(t, bas, milieu), maximum_dc(t, milieu + 1, haut))
```

## 9.3 Exemple : sous-tableau de somme maximale

```python
def somme_max(t, bas=0, haut=None):
    if haut is None: haut = len(t) - 1
    if bas == haut: return t[bas]
    m = (bas + haut) // 2

    # meilleur sous-tableau qui traverse le milieu
    s, meilleur_g = 0, float("-inf")
    for i in range(m, bas - 1, -1):
        s += t[i]; meilleur_g = max(meilleur_g, s)
    s, meilleur_d = 0, float("-inf")
    for i in range(m + 1, haut + 1):
        s += t[i]; meilleur_d = max(meilleur_d, s)

    return max(somme_max(t, bas, m), somme_max(t, m + 1, haut), meilleur_g + meilleur_d)
```

> 💡 L'**algorithme de Kadane** résout ce problème en **O(n)** : `courant = max(x, courant + x)`.

## 9.4 Quickselect : le k-ième plus petit élément

```python
import random

def quickselect(t, k):                       # k = 0 pour le minimum
    pivot = random.choice(t)
    moins = [x for x in t if x < pivot]
    egaux = [x for x in t if x == pivot]
    if k < len(moins):
        return quickselect(moins, k)
    if k < len(moins) + len(egaux):
        return pivot
    return quickselect([x for x in t if x > pivot], k - len(moins) - len(egaux))
```

**O(n)** en moyenne, O(n²) au pire (la **médiane des médianes** garantit O(n)).

## 9.5 Le théorème maître

Pour `T(n) = a·T(n/b) + Θ(n^d)` avec `a ≥ 1`, `b > 1`, `d ≥ 0` (`a` sous-problèmes de taille `n/b`, travail de division/combinaison en `n^d`) :

| Comparaison | Résultat | Intuition |
| --- | --- | --- |
| `d > log_b a` | **Θ(n^d)** | Le travail à la racine domine |
| `d = log_b a` | **Θ(n^d · log n)** | Chaque niveau coûte autant |
| `d < log_b a` | **Θ(n^(log_b a))** | Les feuilles dominent |

| Algorithme | Récurrence | `a, b, d` | Résultat |
| --- | --- | --- | --- |
| Recherche binaire | `T(n/2) + O(1)` | 1, 2, 0 | Θ(log n) |
| Tri fusion | `2T(n/2) + O(n)` | 2, 2, 1 | Θ(n log n) |
| Quickselect (cas moyen) | `T(n/2) + O(n)` | 1, 2, 1 | Θ(n) |
| Karatsuba | `3T(n/2) + O(n)` | 3, 2, 1 | Θ(n^1,585) |
| Strassen | `7T(n/2) + O(n²)` | 7, 2, 2 | Θ(n^2,807) |

## 9.6 Multiplication de matrices (Strassen)

Le produit naïf de deux matrices `n × n` coûte **O(n³)**. **Strassen** (1969) divise chaque matrice en 4 blocs et n'effectue que **7 produits récursifs au lieu de 8** (en échange de plus d'additions), d'où **O(n^log₂7) ≈ O(n^2,81)**.

```text
M1 = (A11 + A22)(B11 + B22)     M5 = (A11 + A12) B22
M2 = (A21 + A22) B11            M6 = (A21 − A11)(B11 + B12)
M3 = A11 (B12 − B22)            M7 = (A12 − A22)(B21 + B22)
M4 = A22 (B21 − B11)

C11 = M1 + M4 − M5 + M7         C12 = M3 + M5
C21 = M2 + M4                   C22 = M1 − M2 + M3 + M6
```

> 📈 *(à jour)* L'exposant optimal ω de la multiplication matricielle reste un problème ouvert : les meilleures bornes **théoriques** actuelles sont d'environ **2,37**, mais ces algorithmes sont **impraticables** (constantes énormes). En pratique, on utilise l'algorithme naïf optimisé (BLAS, cache, parallélisme) ou, pour de grandes tailles, Strassen.

---

# 10. Algorithmes gloutons

## 10.1 Principe

Un algorithme **glouton** (*greedy*) construit la solution en faisant, à chaque étape, **le choix localement optimal**, sans jamais revenir en arrière.

| ✅ Avantages | ❌ Limites |
| --- | --- |
| Simples et rapides (souvent O(n log n)) | Optimal **seulement si** le problème s'y prête |
| Peu de mémoire | Le choix local peut mener à un mauvais résultat global |

## 10.2 Quand fonctionne-t-il ?

Deux propriétés doivent être **démontrées** :

1. **Choix glouton** : il existe une solution optimale qui commence par le choix glouton.
2. **Sous-structure optimale** : le problème restant, après le choix, est du même type.

Pour prouver : **argument d'échange** (on transforme une solution optimale en solution gloutonne sans la dégrader) ou **induction**.

## 10.3 Cadre général

```text
1. Trier / organiser les candidats selon un critère (le « bon » critère est la clé).
2. Répéter : choisir le meilleur candidat compatible, l'ajouter à la solution.
3. S'arrêter quand la solution est complète.
```

## 10.4 Sélection d'activités (*Activity Selection*)

**Problème** : choisir le **maximum d'activités compatibles** (non chevauchantes). **Critère : l'heure de fin la plus tôt.**

```python
def selection_activites(activites):              # liste de (debut, fin)
    activites.sort(key=lambda a: a[1])           # tri par fin croissante
    choisies, fin_derniere = [], float("-inf")
    for debut, fin in activites:
        if debut >= fin_derniere:
            choisies.append((debut, fin))
            fin_derniere = fin
    return choisies

print(selection_activites([(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]))
# [(1, 4), (5, 7), (8, 9)]
```

**O(n log n)** (le tri domine). ⚠️ Trier par **début** ou par **durée** ne donne **pas** l'optimum.

## 10.5 Sac à dos fractionnaire

On peut prendre une **fraction** d'un objet. **Critère : rapport valeur / poids décroissant.**

```python
def sac_a_dos_fractionnaire(objets, capacite):    # objets : (valeur, poids)
    objets.sort(key=lambda o: o[0] / o[1], reverse=True)
    total = 0.0
    for valeur, poids in objets:
        if capacite >= poids:
            total += valeur; capacite -= poids
        else:
            total += valeur * capacite / poids    # fraction du dernier objet
            break
    return total

print(sac_a_dos_fractionnaire([(60, 10), (100, 20), (120, 30)], 50))   # 240.0
```

> ⚠️ Pour le **sac à dos 0/1** (objets indivisibles), le glouton n'est **plus optimal** : il faut la **programmation dynamique** (section 18).

## 10.6 Codage de Huffman

Compression sans perte : les symboles **fréquents** reçoivent des codes **courts** (code préfixe optimal).

```python
import heapq
from collections import Counter

def huffman(texte):
    tas = [[freq, i, symbole, None, None] for i, (symbole, freq) in enumerate(Counter(texte).items())]
    heapq.heapify(tas)
    compteur = len(tas)
    while len(tas) > 1:
        a, b = heapq.heappop(tas), heapq.heappop(tas)        # les deux plus faibles fréquences
        heapq.heappush(tas, [a[0] + b[0], compteur, None, a, b])
        compteur += 1

    codes = {}
    def parcourir(noeud, code=""):
        if noeud[2] is not None:
            codes[noeud[2]] = code or "0"
        else:
            parcourir(noeud[3], code + "0"); parcourir(noeud[4], code + "1")
    parcourir(tas[0])
    return codes

print(huffman("abracadabra"))
```

**O(n log n)** pour `n` symboles distincts.

## 10.7 Autres exemples gloutons

| Problème | Critère glouton |
| --- | --- |
| **Arbre couvrant minimal** (Kruskal, Prim) | Plus petite arête sûre |
| **Plus courts chemins** (Dijkstra) | Sommet non traité le plus proche |
| **Rendu de monnaie** | Plus grande pièce possible… **si le système est « canonique »** |
| Ordonnancement de tâches avec échéances | Trier par échéance / durée |
| Minimiser la somme des temps d'attente | Traiter les tâches **les plus courtes d'abord** |

### Quand le glouton **échoue** : rendu de monnaie

```python
def monnaie_gloutonne(pieces, montant):
    rendu = []
    for p in sorted(pieces, reverse=True):
        while montant >= p:
            montant -= p; rendu.append(p)
    return rendu

monnaie_gloutonne([1, 3, 4], 6)    # [4, 1, 1] → 3 pièces ❌ ; l'optimum est [3, 3] → 2 pièces
```

Pour des systèmes de pièces arbitraires, utilisez la **programmation dynamique**.

## 10.8 Glouton ou programmation dynamique ?

| | Glouton | Programmation dynamique |
| --- | --- | --- |
| Décision | **Locale**, irrévocable | Explore toutes les options via sous-problèmes |
| Vitesse | Très rapide | Plus lent, plus de mémoire |
| Optimalité | Seulement si preuve | **Garantie** (si sous-structure optimale) |
| Exemple | Fractionnaire, Huffman | Sac à dos 0/1, rendu général |

---

# 11. Retour sur trace (*backtracking*)

## 11.1 Principe

Le **retour sur trace** construit une solution **pas à pas** en essayant des choix ; si un choix mène à une **impasse**, on **annule** (retour en arrière) et on essaie le suivant. C'est une **recherche exhaustive intelligente** : l'**élagage** (*pruning*) coupe les branches qui ne peuvent pas aboutir.

```text
Arbre de recherche :        choix 1 ── choix 2 ── choix 3 ✗ (impasse)
                                          └── choix 2' ── … ✓ solution
```

## 11.2 Schéma général

```python
def retour_sur_trace(etat, solutions):
    if est_complet(etat):                    # solution trouvée
        solutions.append(copie(etat))
        return
    for choix in candidats(etat):
        if est_valide(etat, choix):          # élagage : on ne continue que si c'est prometteur
            appliquer(etat, choix)           # 1. choisir
            retour_sur_trace(etat, solutions)    # 2. explorer
            annuler(etat, choix)             # 3. défaire (backtrack)
```

## 11.3 Exemple : sous-ensembles et permutations

```python
def sous_ensembles(t):
    resultat, courant = [], []
    def aller(i):
        if i == len(t):
            resultat.append(courant[:]); return
        aller(i + 1)                          # sans t[i]
        courant.append(t[i]); aller(i + 1); courant.pop()     # avec t[i]
    aller(0)
    return resultat                           # 2ⁿ sous-ensembles

def permutations(t):
    resultat = []
    def aller(debut):
        if debut == len(t):
            resultat.append(t[:]); return
        for i in range(debut, len(t)):
            t[debut], t[i] = t[i], t[debut]
            aller(debut + 1)
            t[debut], t[i] = t[i], t[debut]   # annuler
    aller(0)
    return resultat                           # n! permutations

# Équivalents de la bibliothèque standard
from itertools import permutations as perms, combinations
list(combinations([1, 2, 3], 2))              # [(1, 2), (1, 3), (2, 3)]
```

## 11.4 Problème des N reines

Placer `n` reines sur un échiquier `n × n` sans qu'elles s'attaquent (ni ligne, ni colonne, ni diagonale).

```python
def n_reines(n):
    solutions = []
    colonnes, diag1, diag2 = set(), set(), set()      # colonne, (ligne - col), (ligne + col)
    placement = []

    def placer(ligne):
        if ligne == n:
            solutions.append(placement[:]); return
        for col in range(n):
            if col in colonnes or (ligne - col) in diag1 or (ligne + col) in diag2:
                continue                               # élagage O(1)
            colonnes.add(col); diag1.add(ligne - col); diag2.add(ligne + col)
            placement.append(col)
            placer(ligne + 1)
            placement.pop()
            colonnes.remove(col); diag1.remove(ligne - col); diag2.remove(ligne + col)

    placer(0)
    return solutions

print(len(n_reines(8)))      # 92 solutions
```

## 11.5 Solveur de Sudoku

```python
def resoudre_sudoku(grille):                   # grille 9×9, 0 = case vide
    def possible(l, c, v):
        if any(grille[l][j] == v for j in range(9)): return False
        if any(grille[i][c] == v for i in range(9)): return False
        bl, bc = 3 * (l // 3), 3 * (c // 3)
        return all(grille[bl + i][bc + j] != v for i in range(3) for j in range(3))

    for l in range(9):
        for c in range(9):
            if grille[l][c] == 0:
                for v in range(1, 10):
                    if possible(l, c, v):
                        grille[l][c] = v
                        if resoudre_sudoku(grille):
                            return True
                        grille[l][c] = 0           # retour en arrière
                return False                        # aucune valeur possible : impasse
    return True                                     # grille complète
```

> ⚡ **Optimisation** : choisir d'abord la case ayant **le moins de valeurs possibles** (heuristique MRV) ; suivre les valeurs possibles avec des **masques de bits**.

## 11.6 Autres problèmes classiques

| Problème | Idée |
| --- | --- |
| **Rat dans un labyrinthe** | Avancer / reculer dans un labyrinthe jusqu'à la sortie |
| **Parcours du cavalier** | Visiter toutes les cases (heuristique de Warnsdorff) |
| **Chemin hamiltonien** | Visiter chaque sommet une fois (NP-complet) |
| **Somme de sous-ensemble** | Choisir des éléments dont la somme vaut `S` |
| **Coloration de graphe**, **mots croisés**, **SAT** | Affecter + vérifier + annuler |

## 11.7 Complexité et comparaison

Pire cas **exponentiel** (O(2ⁿ), O(n!)…) : l'élagage améliore beaucoup la pratique, pas le pire cas.

| | Retour sur trace | Glouton | Programmation dynamique |
| --- | --- | --- | --- |
| Exploration | Exhaustive avec élagage | Un seul chemin | Sous-problèmes mémorisés |
| Revient en arrière | ✅ | ❌ | — |
| Sous-problèmes répétés | Souvent recalculés | — | **Mémorisés** |
| Garantie d'optimalité | ✅ (exhaustif) | ❌ | ✅ |

> 💡 Si l'on observe des **sous-problèmes qui se répètent**, ajoutez de la **mémoïsation** : le retour sur trace devient de la programmation dynamique.

---

# 12. Technique des deux pointeurs

## 12.1 Principe

On utilise **deux indices** qui parcourent la structure, soit en **sens opposés** (depuis les deux bouts), soit **dans le même sens** (à vitesses différentes). Cela remplace souvent une double boucle **O(n²)** par un seul passage **O(n)**.

| Variante | Usage |
| --- | --- |
| **Opposés** (gauche, droite) | Tableaux triés, palindromes, paires de somme donnée |
| **Même sens** (lent, rapide) | Suppression de doublons, partition, fenêtre variable |
| **Lent / rapide** (Floyd) | Détection de cycle dans une liste chaînée |

## 12.2 Somme de deux nombres dans un tableau trié

```python
def deux_somme_trie(t, cible):
    g, d = 0, len(t) - 1
    while g < d:
        s = t[g] + t[d]
        if s == cible:
            return (g, d)
        if s < cible: g += 1          # il faut une somme plus grande
        else:         d -= 1          # il faut une somme plus petite
    return None
```

**O(n)** (après un éventuel tri O(n log n)). Sur un tableau **non trié**, un `dict` donne aussi O(n) (section 17).

## 12.3 Autres exemples

```python
def est_palindrome(s):
    s = [c.lower() for c in s if c.isalnum()]
    g, d = 0, len(s) - 1
    while g < d:
        if s[g] != s[d]: return False
        g += 1; d -= 1
    return True

def supprimer_doublons_tries(t):              # en place, renvoie la nouvelle longueur
    if not t: return 0
    lent = 0
    for rapide in range(1, len(t)):
        if t[rapide] != t[lent]:
            lent += 1; t[lent] = t[rapide]
    return lent + 1

def trois_somme(t):                           # triplets de somme nulle : O(n²)
    t.sort(); res = []
    for i in range(len(t) - 2):
        if i and t[i] == t[i - 1]: continue
        g, d = i + 1, len(t) - 1
        while g < d:
            s = t[i] + t[g] + t[d]
            if s < 0: g += 1
            elif s > 0: d -= 1
            else:
                res.append((t[i], t[g], t[d])); g += 1; d -= 1
                while g < d and t[g] == t[g - 1]: g += 1
    return res

def aire_max_conteneur(h):                    # « Container With Most Water »
    g, d, meilleur = 0, len(h) - 1, 0
    while g < d:
        meilleur = max(meilleur, min(h[g], h[d]) * (d - g))
        if h[g] < h[d]: g += 1
        else: d -= 1
    return meilleur
```

### Détection de cycle (lièvre et tortue de Floyd)

```python
def a_un_cycle(tete):
    lent = rapide = tete
    while rapide and rapide.suivant:
        lent, rapide = lent.suivant, rapide.suivant.suivant
        if lent is rapide:
            return True
    return False
```

## 12.4 Quand l'utiliser ?

Tableau **trié** (ou triable), recherche de **paires/triplets**, **comparaisons aux extrémités**, parcours **linéaire** d'une séquence, besoin de **O(1) mémoire**.

---

# 13. Fenêtre glissante

## 13.1 Principe

On maintient une **fenêtre** `[g, d]` sur un tableau ou une chaîne et on la **fait glisser** en mettant à jour l'information **de façon incrémentale** (ajouter l'élément entrant, retirer l'élément sortant), au lieu de tout recalculer.

| Type | Description |
| --- | --- |
| **Taille fixe** `k` | La fenêtre garde la même longueur |
| **Taille variable** | On **étend** à droite, on **réduit** à gauche tant qu'une condition est violée |

Complexité typique : **O(n)** (chaque indice entre et sort au plus une fois).

## 13.2 Taille fixe : somme maximale de `k` éléments consécutifs

```python
def somme_max_fenetre(t, k):
    somme = sum(t[:k])
    meilleur = somme
    for i in range(k, len(t)):
        somme += t[i] - t[i - k]              # entre t[i], sort t[i-k]
        meilleur = max(meilleur, somme)
    return meilleur
```

## 13.3 Taille variable : plus longue sous-chaîne sans répétition

```python
def plus_longue_sans_repetition(s):
    derniere_position = {}
    g = meilleur = 0
    for d, c in enumerate(s):
        if c in derniere_position and derniere_position[c] >= g:
            g = derniere_position[c] + 1       # on saute après la dernière occurrence
        derniere_position[c] = d
        meilleur = max(meilleur, d - g + 1)
    return meilleur

print(plus_longue_sans_repetition("abcabcbb"))    # 3
```

## 13.4 Taille variable : plus petit sous-tableau de somme ≥ S (valeurs positives)

```python
def plus_court_sous_tableau(t, S):
    g = somme = 0
    meilleur = float("inf")
    for d, x in enumerate(t):
        somme += x
        while somme >= S:
            meilleur = min(meilleur, d - g + 1)
            somme -= t[g]; g += 1
    return 0 if meilleur == float("inf") else meilleur
```

> ⚠️ Cette méthode suppose des **valeurs positives** : avec des négatifs, utilisez les sommes préfixes + table de hachage.

## 13.5 Maximum de chaque fenêtre : file monotone *(ajout)*

```python
from collections import deque

def maximums_fenetres(t, k):
    dq, res = deque(), []                      # dq contient des INDICES de valeurs décroissantes
    for i, x in enumerate(t):
        while dq and t[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(t[dq[0]])
    return res                                  # O(n) amorti
```

## 13.6 Autres problèmes classiques

- **Anagrammes dans une chaîne** (fenêtre de taille fixe + compteurs de lettres)
- **Plus long sous-tableau avec au plus `k` valeurs distinctes**
- **Sous-chaîne minimale contenant tous les caractères d'un motif**
- **Fruits dans des paniers**, **plus longue sous-chaîne avec remplacement de `k` caractères**

---

# 14. Sommes préfixes et tableaux de différences

## 14.1 Sommes préfixes

On précalcule `P[i] = t[0] + … + t[i-1]` : la somme de **n'importe quel intervalle** se calcule en **O(1)**.

```python
from itertools import accumulate

t = [3, 1, 4, 1, 5, 9]
P = [0] + list(accumulate(t))            # [0, 3, 4, 8, 9, 14, 23]

def somme_intervalle(l, r):              # somme de t[l..r] inclus
    return P[r + 1] - P[l]

print(somme_intervalle(1, 3))            # 1 + 4 + 1 = 6
```

Précalcul **O(n)**, requêtes **O(1)**.

### Sous-tableaux de somme `k` (avec valeurs négatives possibles)

```python
from collections import defaultdict

def nb_sous_tableaux_somme(t, k):
    vus = defaultdict(int); vus[0] = 1
    somme = total = 0
    for x in t:
        somme += x
        total += vus[somme - k]          # nombre de préfixes précédents tels que somme - préfixe = k
        vus[somme] += 1
    return total                         # O(n)
```

### Version 2D

```python
def construire_prefixe_2d(m):
    h, l = len(m), len(m[0])
    P = [[0] * (l + 1) for _ in range(h + 1)]
    for i in range(h):
        for j in range(l):
            P[i + 1][j + 1] = m[i][j] + P[i][j + 1] + P[i + 1][j] - P[i][j]
    return P

def somme_rect(P, r1, c1, r2, c2):       # inclusif
    return P[r2 + 1][c2 + 1] - P[r1][c2 + 1] - P[r2 + 1][c1] + P[r1][c1]
```

## 14.2 Tableau de différences

Pour appliquer **de nombreuses mises à jour d'intervalle** (« ajouter `v` à `t[l..r]` ») : chaque mise à jour coûte **O(1)**, puis une **reconstruction** en O(n).

```python
def mises_a_jour_intervalles(n, operations):          # operations : (l, r, v)
    diff = [0] * (n + 1)
    for l, r, v in operations:
        diff[l] += v
        diff[r + 1] -= v
    resultat, courant = [], 0
    for i in range(n):
        courant += diff[i]
        resultat.append(courant)
    return resultat

print(mises_a_jour_intervalles(5, [(0, 2, 5), (2, 4, 10)]))   # [5, 5, 15, 10, 10]
```

La **différence** est l'opération inverse de la somme préfixe.

## 14.3 Applications

| Application | Technique |
| --- | --- |
| Somme / moyenne d'un intervalle, requêtes multiples | Préfixes |
| Nombre d'occurrences d'une lettre dans `[l, r]` | Préfixes par lettre |
| Réservations qui se chevauchent, « covoiturage », ensoleillement | Différences |
| Dessiner des rectangles sur une grille | Différences 2D |
| Sous-tableau de somme `k` | Préfixes + `dict` |

> 💡 Si le tableau **change** entre les requêtes, utilisez un **arbre de Fenwick** ou un **arbre de segments** ([section 23](#23-arbres-de-segments-et-arbres-de-fenwick)).

---

# 15. Recherche binaire sur la réponse

## 15.1 Principe

Au lieu de chercher un **indice**, on cherche **la meilleure valeur** `x` dans un intervalle `[bas, haut]`, à condition de disposer d'une fonction **monotone** `est_valide(x)` : si `x` est faisable, alors tout `x' ≥ x` (ou tout `x' ≤ x`) l'est aussi.

```text
x :       1   2   3   4   5   6   7   8
valide :  ✗   ✗   ✗   ✓   ✓   ✓   ✓   ✓      → on cherche la PREMIÈRE valeur valide (4)
```

## 15.2 Modèle : plus petite valeur valide

```python
def plus_petite_valeur_valide(bas, haut, est_valide):
    while bas < haut:
        milieu = (bas + haut) // 2
        if est_valide(milieu):
            haut = milieu                # milieu est une candidate : on cherche plus petit
        else:
            bas = milieu + 1
    return bas                           # première valeur valide (suppose qu'elle existe)
```

Pour **maximiser** (dernière valeur valide), utiliser `milieu = (bas + haut + 1) // 2` et `bas = milieu` / `haut = milieu - 1`.

## 15.3 Exemple : expédier des colis en D jours

Poids `p`, capacité minimale d'un camion pour tout livrer en `D` jours (ordre fixé) :

```python
def capacite_minimale(poids, D):
    def faisable(cap):
        jours, charge = 1, 0
        for p in poids:
            if charge + p > cap:
                jours += 1; charge = 0
            charge += p
        return jours <= D

    return plus_petite_valeur_valide(max(poids), sum(poids), faisable)

print(capacite_minimale([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))   # 15
```

Complexité : **O(n · log(somme))**.

## 15.4 Exemple : vitesse minimale pour manger toutes les bananes

```python
from math import ceil

def vitesse_minimale(piles, heures):
    return plus_petite_valeur_valide(1, max(piles), lambda v: sum(ceil(p / v) for p in piles) <= heures)
```

## 15.5 Schémas fréquents

| Type de problème | Direction |
| --- | --- |
| **Minimiser le maximum** (capacité, charge) | Valide → chercher à **gauche** |
| **Maximiser le minimum** (distance minimale) | Valide → chercher à **droite** |
| Plus petite valeur satisfaisant une contrainte | Valide → gauche |
| Plus grande valeur satisfaisant une contrainte | Valide → droite |

## 15.6 Réels : recherche binaire flottante

```python
def racine_carree(x, eps=1e-9):
    bas, haut = 0.0, max(1.0, x)
    for _ in range(100):                 # un nombre FIXE d'itérations évite les boucles infinies
        milieu = (bas + haut) / 2
        if milieu * milieu < x: bas = milieu
        else: haut = milieu
    return bas
```

## 15.7 Conseils

- Définissez soigneusement **`bas`** et **`haut`** (bornes qui contiennent la réponse).
- Vérifiez la **monotonie** de la fonction de décision.
- `est_valide` doit être **O(n)** (ou mieux).
- Testez les **cas limites** (réponse = borne basse ou haute).

---

# 16. Algorithmes de théorie des nombres

## 16.1 Crible d'Ératosthène

Trouve **tous les nombres premiers ≤ n** en O(n log log n).

```python
def crible(n):
    est_premier = [True] * (n + 1)
    est_premier[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if est_premier[i]:
            for multiple in range(i * i, n + 1, i):      # on démarre à i²
                est_premier[multiple] = False
    return [i for i, p in enumerate(est_premier) if p]

print(crible(30))    # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

Variantes : **crible linéaire** (O(n)), **crible segmenté** (mémoire réduite), **crible des plus petits facteurs premiers** pour factoriser rapidement.

## 16.2 Factorisation

```python
def factoriser(n):                         # O(√n)
    facteurs, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            facteurs[d] = facteurs.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        facteurs[n] = facteurs.get(n, 0) + 1
    return facteurs

print(factoriser(360))       # {2: 3, 3: 2, 5: 1}
```

## 16.3 Arithmétique modulaire

Pour éviter les nombres énormes, on calcule **modulo** `m` (souvent `10⁹ + 7`).

```python
MOD = 10**9 + 7

(a + b) % MOD ; (a * b) % MOD ; (a - b) % MOD      # en Python, % renvoie un résultat ≥ 0
```

### Exponentiation rapide : `a^b mod m` en O(log b)

```python
def puissance_mod(a, b, m):
    resultat, a = 1, a % m
    while b:
        if b & 1:
            resultat = resultat * a % m
        a = a * a % m
        b >>= 1
    return resultat

pow(2, 10**18, MOD)          # équivalent intégré, optimisé
```

### Inverse modulaire

| Méthode | Condition | Code |
| --- | --- | --- |
| **Petit théorème de Fermat** | `m` **premier**, `a` non multiple de `m` | `a^(m-2) mod m` |
| **Euclide étendu** | `pgcd(a, m) = 1` | Résout `a·x + m·y = 1` |
| **Intégré** *(Python 3.8+)* | `pgcd(a, m) = 1` | `pow(a, -1, m)` |

```python
pow(3, -1, 11)               # 4 car 3 × 4 = 12 ≡ 1 (mod 11)

def euclide_etendu(a, b):    # renvoie (g, x, y) avec a·x + b·y = g = pgcd(a, b)
    if b == 0:
        return a, 1, 0
    g, x, y = euclide_etendu(b, a % b)
    return g, y, x - (a // b) * y
```

### Binôme de Newton modulo un premier

```python
def precalculer_factorielles(n, m=MOD):
    fact = [1] * (n + 1)
    for i in range(1, n + 1): fact[i] = fact[i - 1] * i % m
    inv = [1] * (n + 1)
    inv[n] = pow(fact[n], -1, m)
    for i in range(n, 0, -1): inv[i - 1] = inv[i] * i % m
    return fact, inv

def C(n, k, fact, inv, m=MOD):
    return 0 if k < 0 or k > n else fact[n] * inv[k] % m * inv[n - k] % m
```

## 16.4 Autres outils

| Outil | Rôle |
| --- | --- |
| **Indicatrice d'Euler** φ(n) | Nombre d'entiers `≤ n` premiers avec `n` ; `a^φ(m) ≡ 1 (mod m)` si pgcd = 1 |
| **Théorème des restes chinois** | Résout des systèmes de congruences à modules premiers entre eux |
| **Exponentiation de matrices** | Récurrences linéaires (Fibonacci) en O(k³ log n) |
| **Nombres de Catalan**, **Stirling**, **inclusion-exclusion** | Dénombrements |

```python
def phi(n):
    r = n; d = 2
    while d * d <= n:
        if n % d == 0:
            while n % d == 0: n //= d
            r -= r // d
        d += 1
    if n > 1: r -= r // n
    return r
```

## 16.5 Test de primalité de Miller-Rabin *(ajout)*

Test **probabiliste** rapide ; **déterministe** pour tout entier 64 bits avec les bases ci-dessous.

```python
def miller_rabin(n):
    if n < 2: return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else:
            return False
    return True
```

Complexité **O(log³ n)** : bien plus rapide que O(√n) pour de grands nombres (cryptographie : RSA).

---

# 17. Hachage

## 17.1 Principe

Une **fonction de hachage** transforme une clé en un **entier** servant d'indice dans un tableau (*table de hachage*). L'accès, l'insertion et la suppression sont en **O(1) en moyenne**.

```text
clé "Alice" ──hash()──▶ 8372649 ──mod taille──▶ case 5 :  [ … | … | "Alice" → 30 | … ]
```

Propriétés d'une bonne fonction : **déterministe**, **rapide**, **répartition uniforme**.

## 17.2 Les structures en Python

```python
d = {}                          # dictionnaire (table de hachage)
d["pomme"] = 3                  # insertion / mise à jour : O(1) moyen
d["pomme"]                      # lecture : 3 (KeyError si absent)
d.get("poire", 0)               # lecture avec valeur par défaut
"pomme" in d                    # test d'appartenance : O(1)
del d["pomme"]                  # suppression

ensemble = {1, 2, 3}            # set : valeurs uniques
2 in ensemble                   # O(1)
ensemble | {4}; ensemble & {2, 9}; ensemble - {1}      # union, intersection, différence
```

Les clés doivent être **hachables** (donc **immuables**) : `int`, `str`, `tuple` de valeurs hachables ✅ ; `list`, `dict`, `set` ❌. Depuis Python 3.7, un `dict` **conserve l'ordre d'insertion**.

## 17.3 Gestion des collisions

Deux clés différentes peuvent avoir le même indice : c'est une **collision**.

| Méthode | Principe |
| --- | --- |
| **Chaînage** | Chaque case contient une liste de paires |
| **Adressage ouvert** | On cherche une autre case libre (sondage linéaire, quadratique, double hachage) — c'est la méthode du `dict` de CPython |
| **Redimensionnement** | Quand le **facteur de charge** (éléments / cases) devient trop grand, on **agrandit** et on **rehache** (coût amorti O(1)) |

## 17.4 Complexité

| Opération | Moyen | Pire cas |
| --- | --- | --- |
| Insertion / recherche / suppression | **O(1)** | O(n) (toutes les clés en collision) |
| Parcours | O(n) | O(n) |
| Mémoire | O(n) | O(n) |

> ⚠️ Pour des chaînes, Python **randomise** le hachage à chaque lancement (`PYTHONHASHSEED`) pour empêcher les attaques par collisions. En compétition, des tests « anti-hash » peuvent dégrader un `dict` basé sur des entiers : mélangez les clés (XOR avec une constante aléatoire) si nécessaire.

## 17.5 Problèmes classiques

### Deux sommes

```python
def deux_somme(t, cible):
    vus = {}                                   # valeur → indice
    for i, x in enumerate(t):
        if cible - x in vus:
            return (vus[cible - x], i)
        vus[x] = i
    return None                                # O(n)
```

### Regrouper les anagrammes

```python
from collections import defaultdict

def grouper_anagrammes(mots):
    groupes = defaultdict(list)
    for m in mots:
        groupes["".join(sorted(m))].append(m)
    return list(groupes.values())
```

### Plus longue suite consécutive

```python
def plus_longue_suite(t):
    ensemble, meilleur = set(t), 0
    for x in ensemble:
        if x - 1 not in ensemble:               # début d'une suite
            longueur = 1
            while x + longueur in ensemble: longueur += 1
            meilleur = max(meilleur, longueur)
    return meilleur                              # O(n)
```

### Autres

Premier caractère unique, détection de doublons, **détection de cycle** (ensemble des sommets visités), mémoïsation, sous-tableau de somme `k` (préfixes + `dict`).

## 17.6 Outils du module `collections`

| Outil | Rôle |
| --- | --- |
| `Counter` | Compter les occurrences (`Counter("abracadabra")`, `.most_common(3)`) |
| `defaultdict(list)` / `defaultdict(int)` | Valeur par défaut automatique |
| `OrderedDict` | Rarement nécessaire (les `dict` gardent l'ordre) |
| `frozenset` | Ensemble immuable, utilisable comme clé |

## 17.7 Hachage d'objets et autres usages

```python
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def __eq__(self, autre): return (self.x, self.y) == (autre.x, autre.y)
    def __hash__(self): return hash((self.x, self.y))       # cohérent avec __eq__
```

Autres usages : **hachage cryptographique** (SHA-256, vérification d'intégrité — pas pour les mots de passe, utilisez bcrypt/argon2), **filtres de Bloom** (appartenance probabiliste), **hachage roulant** (Rabin-Karp), **hachage cohérent** (systèmes distribués).

## 17.8 Bonnes pratiques

- Utilisez `set` / `dict` pour les **tests d'appartenance** et **comptages**.
- Des **clés immuables** et un `__hash__` cohérent avec `__eq__`.
- N'utilisez pas un ordre de hachage comme s'il était significatif (sauf `dict` : ordre d'insertion).

---

# 🔴 Niveau avancé

---

# 18. Programmation dynamique

## 18.1 Principe

La **programmation dynamique** (DP) résout un problème en le décomposant en **sous-problèmes qui se chevauchent**, dont on **mémorise** les résultats pour ne les calculer qu'une fois. Elle s'applique lorsque :

1. **Sous-structure optimale** : la solution optimale se construit à partir de solutions optimales de sous-problèmes.
2. **Sous-problèmes chevauchants** : les mêmes sous-problèmes reviennent plusieurs fois.

```text
fib(5)
 ├─ fib(4)
 │   ├─ fib(3) ← calculé plusieurs fois sans mémoïsation
 │   └─ fib(2)
 └─ fib(3)     ← …
```

## 18.2 Démarche en 5 étapes

| Étape | Question |
| --- | --- |
| 1. **État** | Que représente `dp[i]` (ou `dp[i][j]`) ? |
| 2. **Transition** | Comment `dp[i]` dépend-il des états plus petits ? |
| 3. **Cas de base** | Quelles valeurs initiales ? |
| 4. **Ordre de calcul** | Dans quel ordre remplir (pour que les dépendances soient prêtes) ? |
| 5. **Réponse** | Où se trouve le résultat final ? |

## 18.3 Descendante (mémoïsation) ou ascendante (tabulation)

| | **Top-down** (mémoïsation) | **Bottom-up** (tabulation) |
| --- | --- | --- |
| Principe | Récursion + cache | Boucles, on remplit un tableau |
| Avantage | Facile à écrire, ne calcule que le nécessaire | Pas de récursion (pas de limite de pile), optimisable en mémoire |
| Inconvénient | Surcoût de la récursion, profondeur limitée | Il faut trouver l'ordre de calcul |

```python
from functools import cache

# Top-down
@cache
def escaliers(n):                       # nombre de façons de monter n marches (pas de 1 ou 2)
    return 1 if n <= 1 else escaliers(n - 1) + escaliers(n - 2)

# Bottom-up, mémoire O(1)
def escaliers_iteratif(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b
```

## 18.4 Problèmes 1D

### Rendu de monnaie (minimum de pièces)

```python
def rendu_monnaie(pieces, montant):
    INF = float("inf")
    dp = [0] + [INF] * montant                   # dp[m] = nombre minimal de pièces pour m
    for m in range(1, montant + 1):
        for p in pieces:
            if p <= m and dp[m - p] + 1 < dp[m]:
                dp[m] = dp[m - p] + 1
    return dp[montant] if dp[montant] != INF else -1

print(rendu_monnaie([1, 3, 4], 6))               # 2 (3 + 3)
```

**O(montant × nb_pièces)**.

### Voleur de maisons (*House Robber*)

```python
def voleur(maisons):
    prend, ignore = 0, 0
    for argent in maisons:
        prend, ignore = ignore + argent, max(prend, ignore)
    return max(prend, ignore)
```

### Sous-tableau de somme maximale (Kadane)

```python
def kadane(t):
    meilleur = courant = t[0]
    for x in t[1:]:
        courant = max(x, courant + x)
        meilleur = max(meilleur, courant)
    return meilleur                              # O(n)
```

### Plus longue sous-suite croissante (LIS)

```python
from bisect import bisect_left

def lis(t):                                      # O(n log n)
    queues = []                                  # queues[k] = plus petit dernier élément d'une sous-suite de longueur k+1
    for x in t:
        i = bisect_left(queues, x)
        if i == len(queues): queues.append(x)
        else: queues[i] = x
    return len(queues)
```

(La version DP classique `dp[i] = 1 + max(dp[j] pour j < i, t[j] < t[i])` est en O(n²).)

## 18.5 Problèmes 2D

### Sac à dos 0/1

```python
def sac_a_dos(objets, capacite):                 # objets : (poids, valeur)
    dp = [0] * (capacite + 1)
    for poids, valeur in objets:
        for c in range(capacite, poids - 1, -1):     # parcours DÉCROISSANT : chaque objet utilisé au plus une fois
            dp[c] = max(dp[c], dp[c - poids] + valeur)
    return dp[capacite]

print(sac_a_dos([(1, 1), (3, 4), (4, 5), (5, 7)], 7))   # 9
```

**O(n × capacité)**, mémoire O(capacité) grâce à l'optimisation sur une seule ligne. (Pseudo-polynomial : polynomial en la **valeur** de la capacité, pas en sa taille en bits.)

### Plus longue sous-séquence commune (LCS)

```python
def lcs(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

print(lcs("ABCBDAB", "BDCABA"))                   # 4
```

### Distance d'édition (Levenshtein)

```python
def distance_edition(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): dp[i][0] = i             # supprimer i caractères
    for j in range(m + 1): dp[0][j] = j             # insérer j caractères
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cout = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,         # suppression
                           dp[i][j - 1] + 1,         # insertion
                           dp[i - 1][j - 1] + cout)  # substitution
    return dp[n][m]

print(distance_edition("kitten", "sitting"))         # 3
```

### Chemins dans une grille

```python
def nb_chemins(lignes, colonnes):
    dp = [[1] * colonnes for _ in range(lignes)]
    for i in range(1, lignes):
        for j in range(1, colonnes):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]
```

### Autres classiques

Plus longue sous-chaîne palindromique, **produit de chaînes de matrices**, partition en deux sous-ensembles de même somme, découpage de tige, **plus grand carré de 1**, coût minimal de chemin, nombre de façons de rendre la monnaie (dénombrement), **DP sur les arbres**, **DP sur les intervalles**, **DP par chiffres**.

## 18.6 DP avec masque de bits

Pour des ensembles de **petite taille** (`n ≤ 20` environ), un entier représente un **sous-ensemble**.

### Voyageur de commerce (TSP)

```python
def tsp(dist):
    n = len(dist)
    INF = float("inf")
    dp = [[INF] * n for _ in range(1 << n)]          # dp[masque][i] : coût min pour avoir visité `masque`, finissant en i
    dp[1][0] = 0                                     # départ en 0
    for masque in range(1 << n):
        for i in range(n):
            if dp[masque][i] == INF or not (masque >> i) & 1:
                continue
            for j in range(n):
                if not (masque >> j) & 1:            # j pas encore visité
                    nouveau = masque | (1 << j)
                    dp[nouveau][j] = min(dp[nouveau][j], dp[masque][i] + dist[i][j])
    pleine = (1 << n) - 1
    return min(dp[pleine][i] + dist[i][0] for i in range(n))
```

Complexité **O(n² · 2ⁿ)** (contre O(n!) en force brute).

## 18.7 Reconstituer la solution

Gardez une table `parent[...]` (quel choix a donné l'optimum) puis **remontez** depuis l'état final.

## 18.8 Conseils

- Écrivez d'abord la **récurrence** et les **cas de base**, puis codez.
- Commencez par la version **mémoïsée** (plus naturelle), puis passez en tabulation si besoin.
- **Réduisez la mémoire** si `dp[i]` ne dépend que de `dp[i-1]` (ligne précédente seulement).
- Surveillez la **limite de récursion** en Python (`sys.setrecursionlimit` ou version itérative).
- Entraînez-vous : *Fibonacci*, *Climbing Stairs*, *House Robber*, *Coin Change*, *LIS*, *LCS*, *Edit Distance*, *Knapsack*, *TSP*, *Job Scheduling*.

---

# 19. Algorithmes sur les graphes

## 19.1 Représentation

Un **graphe** `G = (V, E)` est un ensemble de **sommets** reliés par des **arêtes** (orientées ou non, pondérées ou non).

| Représentation | Mémoire | Test d'arête `(u, v)` | Parcourir les voisins de `u` | Quand l'utiliser |
| --- | --- | --- | --- | --- |
| **Liste d'adjacence** | O(V + E) | O(deg(u)) | **O(deg(u))** | Graphes **creux** (le cas le plus courant) ✅ |
| **Matrice d'adjacence** | O(V²) | **O(1)** | O(V) | Graphes **denses**, petits `V` |
| **Liste d'arêtes** | O(E) | O(E) | O(E) | Kruskal, Bellman-Ford |

```python
from collections import defaultdict

graphe = defaultdict(list)
for u, v in [(0, 1), (0, 2), (1, 3), (2, 3)]:
    graphe[u].append(v)
    graphe[v].append(u)                    # graphe non orienté : arête dans les deux sens

# Pondéré : graphe[u].append((v, poids))
```

## 19.2 Parcours en largeur (BFS)

Explore **niveau par niveau** avec une **file**. Il donne le **plus court chemin en nombre d'arêtes** dans un graphe non pondéré.

```python
from collections import deque

def bfs(graphe, source):
    distance = {source: 0}
    file = deque([source])
    while file:
        u = file.popleft()
        for v in graphe[u]:
            if v not in distance:
                distance[v] = distance[u] + 1
                file.append(v)
    return distance                        # O(V + E)
```

## 19.3 Parcours en profondeur (DFS)

Explore le plus loin possible avant de revenir (**pile** ou récursion).

```python
def dfs(graphe, source):
    visites, ordre = set(), []
    pile = [source]                         # version itérative : pas de limite de récursion
    while pile:
        u = pile.pop()
        if u in visites: continue
        visites.add(u); ordre.append(u)
        pile.extend(reversed(graphe[u]))
    return ordre                            # O(V + E)

def dfs_recursif(graphe, u, visites):
    visites.add(u)
    for v in graphe[u]:
        if v not in visites:
            dfs_recursif(graphe, v, visites)
```

| | BFS | DFS |
| --- | --- | --- |
| Structure | File | Pile / récursion |
| Plus court chemin (non pondéré) | ✅ | ❌ |
| Usages | Distances, niveaux | Composantes connexes, cycles, tri topologique, labyrinthes |

### Applications

- **Composantes connexes** : lancer un parcours depuis chaque sommet non visité.
- **Détection de cycle** : graphe non orienté (arête vers un sommet visité qui n'est pas le parent) ; graphe orienté (sommet « en cours » dans la pile de récursion).
- **Graphe biparti** : BFS avec 2 couleurs.
- **Îles dans une grille**, **labyrinthes**, plus court chemin dans une grille.

## 19.4 Tri topologique (graphes orientés acycliques)

Ordonner les sommets de façon que chaque arête `u → v` place `u` avant `v` (dépendances, prérequis de cours).

```python
from collections import deque

def tri_topologique(n, aretes):               # algorithme de Kahn
    graphe = [[] for _ in range(n)]
    degre_entrant = [0] * n
    for u, v in aretes:
        graphe[u].append(v); degre_entrant[v] += 1

    file = deque(i for i in range(n) if degre_entrant[i] == 0)
    ordre = []
    while file:
        u = file.popleft(); ordre.append(u)
        for v in graphe[u]:
            degre_entrant[v] -= 1
            if degre_entrant[v] == 0:
                file.append(v)
    return ordre if len(ordre) == n else None    # None : il existe un cycle
```

**O(V + E)**. La bibliothèque standard propose aussi `graphlib.TopologicalSorter`.

## 19.5 Arbre couvrant de poids minimal (MST)

Sous-ensemble d'arêtes qui **relie tous les sommets** avec un **poids total minimal** et **sans cycle**.

### Union-Find (ensembles disjoints)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.taille = [1] * n

    def trouver(self, x):                          # avec compression de chemin
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def unir(self, a, b):                          # union par taille
        a, b = self.trouver(a), self.trouver(b)
        if a == b: return False
        if self.taille[a] < self.taille[b]: a, b = b, a
        self.parent[b] = a
        self.taille[a] += self.taille[b]
        return True
```

Les opérations coûtent **O(α(n))** amorti (inverse d'Ackermann : quasi constant).

### Algorithme de Kruskal (glouton, trie les arêtes)

```python
def kruskal(n, aretes):                          # aretes : (poids, u, v)
    uf, poids_total, choisies = UnionFind(n), 0, []
    for w, u, v in sorted(aretes):
        if uf.unir(u, v):
            poids_total += w; choisies.append((u, v, w))
    return poids_total, choisies                 # O(E log E)
```

### Algorithme de Prim (glouton, fait grossir un arbre)

```python
import heapq

def prim(graphe, depart=0):                       # graphe[u] = [(v, poids), …]
    vus, tas, total = set(), [(0, depart)], 0
    while tas:
        w, u = heapq.heappop(tas)
        if u in vus: continue
        vus.add(u); total += w
        for v, poids in graphe[u]:
            if v not in vus:
                heapq.heappush(tas, (poids, v))
    return total                                  # O(E log V)
```

| | Kruskal | Prim |
| --- | --- | --- |
| Approche | Arêtes triées + Union-Find | Croissance depuis un sommet + tas |
| Meilleur pour | Graphes **creux** | Graphes **denses** |

## 19.6 Exercices recommandés

*Nombre d'îles*, *Cours à suivre (tri topologique)*, *Clone de graphe*, *Plus court chemin dans une grille*, *Réseau de connexions au coût minimal (MST)*.

---

# 20. Plus courts chemins dans les graphes pondérés

## 20.1 Choisir l'algorithme

| Algorithme | Type | Poids négatifs ? | Complexité | Usage |
| --- | --- | --- | --- | --- |
| **BFS** | Source unique | — (non pondéré) | O(V + E) | Arêtes sans poids |
| **0-1 BFS** | Source unique | Poids 0 ou 1 | O(V + E) | Poids binaires |
| **Dijkstra** | Source unique | ❌ **Non** | O((V + E) log V) | Cas général à poids ≥ 0 |
| **Bellman-Ford** | Source unique | ✅ (détecte les cycles négatifs) | O(V·E) | Poids négatifs |
| **SPFA** | Source unique | ✅ | O(V·E) pire cas, souvent rapide | Pratique (à utiliser avec prudence) |
| **Floyd-Warshall** | **Toutes paires** | ✅ | O(V³) | Petit graphe, toutes les distances |
| **A\*** | Source → cible | ❌ (heuristique admissible) | Dépend de l'heuristique | Cartes, jeux |
| **DAG (tri topologique)** | Source unique | ✅ | O(V + E) | Graphes orientés acycliques |

## 20.2 Dijkstra

**Glouton** : on traite toujours le sommet non finalisé **le plus proche** de la source. Il exige des poids **≥ 0**.

```python
import heapq

def dijkstra(graphe, source):                   # graphe[u] = [(v, poids), …]
    INF = float("inf")
    dist = {u: INF for u in graphe}
    dist[source] = 0
    parent = {source: None}
    tas = [(0, source)]
    while tas:
        d, u = heapq.heappop(tas)
        if d > dist[u]:                          # entrée périmée (suppression paresseuse)
            continue
        for v, w in graphe[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                parent[v] = u
                heapq.heappush(tas, (dist[v], v))
    return dist, parent                          # O((V + E) log V)

def chemin(parent, cible):
    p = []
    while cible is not None:
        p.append(cible); cible = parent.get(cible)
    return p[::-1]
```

> 🔍 *(à jour)* Dijkstra est resté **le** standard pendant plus de 60 ans car il « trie » implicitement les sommets par distance. Une avancée théorique de 2025 (Duan et coll., *Breaking the Sorting Barrier for Directed Single-Source Shortest Paths*, STOC 2025) a montré qu'on peut **contourner cette barrière de tri** pour les graphes orientés creux, en temps O(m log^(2/3) n). C'est un résultat **théorique** : en pratique, Dijkstra avec un tas binaire reste l'algorithme de référence.

## 20.3 Bellman-Ford

Relâche **toutes les arêtes** `V − 1` fois ; une `V`-ième passe qui améliore encore une distance révèle un **cycle négatif**.

```python
def bellman_ford(n, aretes, source):             # aretes : (u, v, poids)
    INF = float("inf")
    dist = [INF] * n
    dist[source] = 0
    for _ in range(n - 1):
        modifie = False
        for u, v, w in aretes:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                modifie = True
        if not modifie:                           # arrêt anticipé
            break
    for u, v, w in aretes:                        # détection de cycle négatif
        if dist[u] != INF and dist[u] + w < dist[v]:
            raise ValueError("Cycle de poids négatif atteignable")
    return dist                                    # O(V·E)
```

## 20.4 Floyd-Warshall

Programmation dynamique : `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])` pour chaque sommet intermédiaire `k`.

```python
def floyd_warshall(dist):                         # dist : matrice, INF si pas d'arête, 0 sur la diagonale
    n = len(dist)
    for k in range(n):                            # k doit être la boucle EXTÉRIEURE
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist                                    # O(V³) ; un dist[i][i] < 0 révèle un cycle négatif
```

## 20.5 BFS 0-1

Pour des poids **0 ou 1** : un **deque** remplace le tas (O(V + E)).

```python
from collections import deque

def bfs_01(graphe, source, n):
    dist = [float("inf")] * n
    dist[source] = 0
    dq = deque([source])
    while dq:
        u = dq.popleft()
        for v, w in graphe[u]:                    # w ∈ {0, 1}
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                dq.appendleft(v) if w == 0 else dq.append(v)
    return dist
```

## 20.6 SPFA (Bellman-Ford avec file)

```python
from collections import deque

def spfa(graphe, source, n):
    INF = float("inf")
    dist, dans_file, compte = [INF] * n, [False] * n, [0] * n
    dist[source] = 0
    file = deque([source])
    while file:
        u = file.popleft(); dans_file[u] = False
        for v, w in graphe[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if not dans_file[v]:
                    compte[v] += 1
                    if compte[v] > n: raise ValueError("Cycle négatif")
                    file.append(v); dans_file[v] = True
    return dist
```

> ⚠️ SPFA est **O(V·E) au pire** : il peut être mis en échec par des entrées conçues pour cela. Préférez Dijkstra dès que les poids sont positifs.

## 20.7 A\* *(ajout)*

**A\*** guide Dijkstra vers la cible avec une **heuristique** `h(v)` (estimation du reste). Il explore les sommets selon `f(v) = g(v) + h(v)`. Si `h` est **admissible** (ne surestime jamais) et **cohérente**, A\* est optimal.

```python
import heapq

def a_etoile(graphe, debut, but, h):
    tas = [(h(debut), 0, debut)]
    g = {debut: 0}
    while tas:
        _, cout, u = heapq.heappop(tas)
        if u == but:
            return cout
        if cout > g.get(u, float("inf")): continue
        for v, w in graphe[u]:
            nouveau = cout + w
            if nouveau < g.get(v, float("inf")):
                g[v] = nouveau
                heapq.heappush(tas, (nouveau + h(v), nouveau, v))
    return None

# Sur une grille : h = distance de Manhattan abs(x - xb) + abs(y - yb)
```

## 20.8 Plus courts chemins dans un DAG

```python
def plus_court_dag(graphe, ordre_topo, source):
    dist = {u: float("inf") for u in graphe}; dist[source] = 0
    for u in ordre_topo:                            # sommets dans l'ordre topologique
        if dist[u] != float("inf"):
            for v, w in graphe[u]:
                dist[v] = min(dist[v], dist[u] + w)
    return dist                                      # O(V + E), poids négatifs acceptés
```

## 20.9 Conseils de choix

| Situation | Algorithme |
| --- | --- |
| Pas de poids | BFS |
| Poids 0 / 1 | 0-1 BFS |
| Poids positifs, une source | **Dijkstra** |
| Poids négatifs ou détection de cycle négatif | **Bellman-Ford** |
| Toutes les paires, `V` petit (≤ ~400) | Floyd-Warshall |
| Une cible, heuristique disponible | **A\*** |
| Graphe acyclique | Tri topologique + relâchement |

---

# 21. Composantes fortement connexes

## 21.1 Définition

Dans un graphe **orienté**, une **composante fortement connexe** (SCC) est un **ensemble maximal de sommets** tels que **chacun peut atteindre tous les autres**. En contractant chaque SCC en un nœud, on obtient un **DAG** (graphe orienté acyclique).

```text
   A ⇄ B        Les SCC : {A, B, C} et {D, E}
   ↓   ↑        Le graphe condensé : {A,B,C} → {D,E}
   └─▶ C
   C ───▶ D ⇄ E
```

### Applications

Analyse de dépendances cycliques, **2-SAT**, optimisation de compilateurs, analyse du web (pages mutuellement accessibles), condensation d'un graphe avant d'y appliquer de la DP.

## 21.2 Algorithme de Kosaraju (deux parcours)

1. DFS sur `G` : noter l'ordre de **fin** de traitement des sommets.
2. Construire le graphe **transposé** (arêtes inversées).
3. DFS sur le transposé, en traitant les sommets par **ordre de fin décroissant** : chaque arbre trouvé est une SCC.

```python
def kosaraju(n, graphe):                     # graphe[u] = liste des successeurs
    ordre, visite = [], [False] * n

    def dfs1(u):
        visite[u] = True
        for v in graphe[u]:
            if not visite[v]: dfs1(v)
        ordre.append(u)                      # ajouté à la FIN du traitement

    for u in range(n):
        if not visite[u]: dfs1(u)

    transpose = [[] for _ in range(n)]
    for u in range(n):
        for v in graphe[u]: transpose[v].append(u)

    comp, visite = [-1] * n, [False] * n
    def dfs2(u, c):
        visite[u] = True; comp[u] = c
        for v in transpose[u]:
            if not visite[v]: dfs2(v, c)

    nb = 0
    for u in reversed(ordre):
        if not visite[u]:
            dfs2(u, nb); nb += 1
    return nb, comp                           # O(V + E)
```

## 21.3 Algorithme de Tarjan (un seul parcours)

Chaque sommet reçoit un **numéro de découverte** `idx[u]` et un **plus petit numéro atteignable** `bas[u]` ; un sommet avec `bas[u] == idx[u]` est la **racine** d'une SCC.

```python
def tarjan(n, graphe):
    idx, bas = [-1] * n, [0] * n
    sur_pile, pile, comp = [False] * n, [], [-1] * n
    compteur = nb = 0

    def dfs(u):
        nonlocal compteur, nb
        idx[u] = bas[u] = compteur; compteur += 1
        pile.append(u); sur_pile[u] = True
        for v in graphe[u]:
            if idx[v] == -1:
                dfs(v); bas[u] = min(bas[u], bas[v])
            elif sur_pile[v]:
                bas[u] = min(bas[u], idx[v])
        if bas[u] == idx[u]:                     # racine d'une SCC
            while True:
                w = pile.pop(); sur_pile[w] = False; comp[w] = nb
                if w == u: break
            nb += 1

    for u in range(n):
        if idx[u] == -1: dfs(u)
    return nb, comp                               # O(V + E)
```

> ⚠️ En Python, ces versions **récursives** dépassent vite la limite de pile (graphes de plus de ~1000 sommets en profondeur) : augmentez `sys.setrecursionlimit` (et la taille de pile via `threading.stack_size`) ou réécrivez-les **avec une pile explicite**.

## 21.4 Kosaraju ou Tarjan ?

| | Kosaraju | Tarjan |
| --- | --- | --- |
| Parcours | 2 DFS + graphe transposé | **1** DFS |
| Complexité | O(V + E) | O(V + E) |
| Mémoire | Plus (graphe transposé) | Moins |
| Facilité de compréhension | ✅ Plus intuitif | Plus subtil |
| Ordre des composantes | Ordre topologique du graphe condensé | Ordre topologique **inverse** |

---

# 22. Flots dans les réseaux

## 22.1 Définition

Un **réseau de flot** est un graphe orienté dont chaque arête a une **capacité**, avec une **source** `s` et un **puits** `t`. Un **flot** envoie des unités de `s` vers `t` en respectant :

1. **Capacité** : `flot(u, v) ≤ capacité(u, v)` ;
2. **Conservation** : pour chaque sommet intermédiaire, flot entrant = flot sortant.

**Problème du flot maximal** : envoyer le plus de flot possible de `s` à `t`.

> 🧠 **Théorème flot max – coupe min** : la valeur du flot maximal est **égale à la capacité de la plus petite coupe** séparant `s` de `t`.

## 22.2 Réseau résiduel et arêtes inverses

Le **graphe résiduel** indique la capacité restante de chaque arête, et ajoute des **arêtes inverses** permettant d'**annuler** une partie d'un flot déjà envoyé. C'est l'idée centrale de tous les algorithmes de flot.

## 22.3 Ford-Fulkerson et Edmonds-Karp

**Ford-Fulkerson** : tant qu'il existe un **chemin augmentant** de `s` à `t` dans le graphe résiduel, on y pousse le flot de la **capacité minimale** du chemin. Avec un **BFS** pour trouver le chemin, c'est **Edmonds-Karp**.

```python
from collections import deque

def edmonds_karp(capacite, s, t):                 # capacite : matrice n × n (modifiée = graphe résiduel)
    n, flot_total = len(capacite), 0
    while True:
        parent = [-1] * n
        parent[s] = s
        file = deque([s])
        while file and parent[t] == -1:           # BFS : plus court chemin augmentant
            u = file.popleft()
            for v in range(n):
                if parent[v] == -1 and capacite[u][v] > 0:
                    parent[v] = u; file.append(v)
        if parent[t] == -1:                       # plus de chemin augmentant
            break
        goulot, v = float("inf"), t
        while v != s:
            goulot = min(goulot, capacite[parent[v]][v]); v = parent[v]
        v = t
        while v != s:
            u = parent[v]
            capacite[u][v] -= goulot              # arête directe
            capacite[v][u] += goulot              # arête inverse
            v = u
        flot_total += goulot
    return flot_total
```

## 22.4 Dinic

Construit un **graphe de niveaux** par BFS, puis envoie un **flot bloquant** par DFS. Beaucoup plus rapide en pratique.

```python
from collections import deque

class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]            # g[u] = indices d'arêtes
        self.arete = []                            # [v, capacité] ; arête inverse = indice ^ 1

    def ajouter(self, u, v, c):
        self.g[u].append(len(self.arete)); self.arete.append([v, c])
        self.g[v].append(len(self.arete)); self.arete.append([u, 0])

    def _bfs(self, s, t):
        self.niveau = [-1] * self.n; self.niveau[s] = 0
        file = deque([s])
        while file:
            u = file.popleft()
            for i in self.g[u]:
                v, c = self.arete[i]
                if c > 0 and self.niveau[v] < 0:
                    self.niveau[v] = self.niveau[u] + 1; file.append(v)
        return self.niveau[t] >= 0

    def _dfs(self, u, t, pousse):
        if u == t: return pousse
        while self.ptr[u] < len(self.g[u]):
            i = self.g[u][self.ptr[u]]
            v, c = self.arete[i]
            if c > 0 and self.niveau[v] == self.niveau[u] + 1:
                d = self._dfs(v, t, min(pousse, c))
                if d > 0:
                    self.arete[i][1] -= d; self.arete[i ^ 1][1] += d
                    return d
            self.ptr[u] += 1
        return 0

    def flot_max(self, s, t):
        total = 0
        while self._bfs(s, t):
            self.ptr = [0] * self.n
            while (f := self._dfs(s, t, float("inf"))) > 0:
                total += f
        return total
```

## 22.5 Complexités

| Algorithme | Complexité | Remarque |
| --- | --- | --- |
| **Ford-Fulkerson** (DFS) | O(E · f*) (`f*` = flot max, capacités **entières**) | Peut être très lent ; ne se termine pas toujours avec des capacités irrationnelles |
| **Edmonds-Karp** (BFS) | **O(V · E²)** | Polynomial, indépendant des capacités |
| **Dinic** | **O(V² · E)** ; **O(E · √V)** sur les réseaux à capacités unitaires (appariements) | Standard en compétition |
| **Push-relabel** (préflot) | O(V² · √E) (variante « plus haut label ») | Efficace sur graphes denses |
| **Algorithmes quasi-linéaires** | E^(1+o(1)) | Résultat **théorique** récent (2022) ; non utilisé en pratique |

## 22.6 Applications

| Problème | Modélisation |
| --- | --- |
| **Couplage biparti maximum** | Source → gauche (cap. 1), gauche → droite (cap. 1), droite → puits (cap. 1) ; spécialisé : **Hopcroft-Karp**, O(E√V) |
| **Coupe minimale** | Après le flot max, sommets atteignables depuis `s` dans le résiduel |
| **Chemins disjoints** (par arêtes / sommets) | Capacités unitaires (division des sommets) |
| **Affectation de tâches / ressources**, **planning de matchs** | Flot avec capacités |
| **Sélection de projets** (profit max avec dépendances) | Coupe minimale |
| **Flot à coût minimal** | Chemins augmentants **les moins coûteux** (Bellman-Ford / Dijkstra avec potentiels) |

> 💡 **Limites** : les flots ordinaires ne gèrent pas les **coûts** (flot à coût minimal), les **bornes inférieures** (circulations) ni les **flots entiers multi-produits** (NP-difficile).

---

# 23. Arbres de segments et arbres de Fenwick

## 23.1 Le problème

Sur un tableau qui **change**, on veut répondre vite à des **requêtes d'intervalle** (somme, minimum, maximum…) **et** appliquer des **mises à jour**.

| Approche | Requête | Mise à jour |
| --- | --- | --- |
| Tableau brut | O(n) | O(1) |
| Sommes préfixes | O(1) | O(n) |
| **Fenwick / arbre de segments** | **O(log n)** | **O(log n)** |

## 23.2 Arbre de Fenwick (*Binary Indexed Tree*, BIT)

Idée : chaque case `i` stocke la somme d'un **bloc** dont la taille est donnée par le **bit de poids faible** de `i` (`i & -i`). Court, rapide, mais limité aux opérations **inversibles** (somme, XOR).

```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.arbre = [0] * (n + 1)              # indices de 1 à n

    def ajouter(self, i, delta):                 # t[i] += delta   (i à partir de 1)
        while i <= self.n:
            self.arbre[i] += delta
            i += i & -i                          # case parente

    def somme_prefixe(self, i):                  # somme de t[1..i]
        total = 0
        while i > 0:
            total += self.arbre[i]
            i -= i & -i                          # retire le bit de poids faible
        return total

    def somme(self, l, r):                       # somme de t[l..r]
        return self.somme_prefixe(r) - self.somme_prefixe(l - 1)

fen = Fenwick(8)
for i, v in enumerate([3, 2, -1, 6, 5, 4, -3, 3], start=1):
    fen.ajouter(i, v)
print(fen.somme(2, 5))        # 2 - 1 + 6 + 5 = 12
```

**Construction O(n log n)** (ou O(n) avec une astuce) · **requête / mise à jour O(log n)** · mémoire O(n).

> 💡 Variantes : BIT pour **mise à jour d'intervalle + requête de point** (sur le tableau de différences), BIT 2D, **comptage d'inversions** d'un tableau.

## 23.3 Arbre de segments (*Segment Tree*)

Arbre binaire dont chaque nœud résume un **intervalle** (somme, min, max, pgcd…). Plus général que Fenwick : toute opération **associative**.

```python
class ArbreSegments:
    def __init__(self, t):
        self.n = len(t)
        self.arbre = [0] * (2 * self.n)
        self.arbre[self.n:] = t                  # feuilles
        for i in range(self.n - 1, 0, -1):       # construction en O(n)
            self.arbre[i] = self.arbre[2 * i] + self.arbre[2 * i + 1]

    def modifier(self, i, valeur):               # t[i] = valeur  (indices à partir de 0)
        i += self.n
        self.arbre[i] = valeur
        while i > 1:
            i //= 2
            self.arbre[i] = self.arbre[2 * i] + self.arbre[2 * i + 1]

    def requete(self, l, r):                     # somme de t[l..r-1]  (r exclu)
        res, l, r = 0, l + self.n, r + self.n
        while l < r:
            if l & 1: res += self.arbre[l]; l += 1
            if r & 1: r -= 1; res += self.arbre[r]
            l //= 2; r //= 2
        return res
```

Pour un **minimum** : remplacer `+` par `min` et `0` par `float("inf")`. Cette version « ascendante » est compacte et rapide ; la version récursive classique (nœud, `[debut, fin]`) est plus flexible.

**Construction O(n) · requête et mise à jour O(log n) · mémoire O(n).**

## 23.4 Propagation paresseuse (*Lazy Propagation*)

Pour des **mises à jour d'intervalle** (« ajouter `v` à `t[l..r]` ») avec requêtes d'intervalle, on **retarde** l'application de la mise à jour : on la stocke dans le nœud (`paresse`) et on ne la **propage** aux enfants que lorsque c'est nécessaire.

```python
class ArbreSegmentsParesseux:                    # ajout sur intervalle + somme sur intervalle
    def __init__(self, t):
        self.n = len(t)
        self.somme = [0] * (4 * self.n)
        self.paresse = [0] * (4 * self.n)
        self._construire(1, 0, self.n - 1, t)

    def _construire(self, noeud, l, r, t):
        if l == r:
            self.somme[noeud] = t[l]; return
        m = (l + r) // 2
        self._construire(2 * noeud, l, m, t)
        self._construire(2 * noeud + 1, m + 1, r, t)
        self.somme[noeud] = self.somme[2 * noeud] + self.somme[2 * noeud + 1]

    def _pousser(self, noeud, l, r):
        if self.paresse[noeud]:
            m = (l + r) // 2
            for enfant, (a, b) in ((2 * noeud, (l, m)), (2 * noeud + 1, (m + 1, r))):
                self.somme[enfant] += self.paresse[noeud] * (b - a + 1)
                self.paresse[enfant] += self.paresse[noeud]
            self.paresse[noeud] = 0

    def ajouter(self, noeud, l, r, a, b, v):     # t[a..b] += v ; appel : ajouter(1, 0, n-1, a, b, v)
        if b < l or r < a: return
        if a <= l and r <= b:
            self.somme[noeud] += v * (r - l + 1)
            self.paresse[noeud] += v; return
        self._pousser(noeud, l, r)
        m = (l + r) // 2
        self.ajouter(2 * noeud, l, m, a, b, v)
        self.ajouter(2 * noeud + 1, m + 1, r, a, b, v)
        self.somme[noeud] = self.somme[2 * noeud] + self.somme[2 * noeud + 1]

    def requete(self, noeud, l, r, a, b):        # somme de t[a..b]
        if b < l or r < a: return 0
        if a <= l and r <= b: return self.somme[noeud]
        self._pousser(noeud, l, r)
        m = (l + r) // 2
        return self.requete(2 * noeud, l, m, a, b) + self.requete(2 * noeud + 1, m + 1, r, a, b)
```

## 23.5 Fenwick ou arbre de segments ?

| Critère | **Fenwick (BIT)** | **Arbre de segments** |
| --- | --- | --- |
| Code | Très court | Plus long |
| Opérations supportées | Somme, XOR (inversibles) | **Toute opération associative** (min, max, pgcd…) |
| Mise à jour d'intervalle | Limitée (astuce différences) | ✅ (propagation paresseuse) |
| Constante | **Plus petite** | Plus grande |
| Mémoire | n | 2n à 4n |

## 23.6 Applications

- **Sommes / minimums / maximums d'intervalle** avec mises à jour
- **Comptage d'inversions**, **rangs** (statistiques ordonnées)
- Calcul de la **plus longue sous-suite croissante** (avec valeurs compressées)
- **Géométrie** (balayage de ligne), **requêtes hors ligne**, **plus bas ancêtre commun** (variantes)
- Autres structures voisines : **table creuse** (*sparse table*, min/max statique en O(1)), **arbre de Fenwick 2D**, **racine carrée** (*sqrt decomposition*).

---

# 24. Algorithmes sur les chaînes

*(Section ajoutée : ces algorithmes figuraient dans la liste « avancé » de l'original sans être détaillés.)*

## 24.1 Recherche de motif naïve

On compare le motif à chaque position : **O(n · m)** (texte de longueur `n`, motif de longueur `m`). On améliore en évitant de **réexaminer** des caractères déjà comparés.

## 24.2 Algorithme de Knuth-Morris-Pratt (KMP)

On précalcule, pour chaque préfixe du motif, la **plus longue bordure** (préfixe qui est aussi suffixe) : c'est le **tableau des préfixes** (`pi`). En cas d'échec, on **saute** au lieu de reculer dans le texte.

```python
def table_prefixes(motif):
    pi = [0] * len(motif)
    k = 0
    for i in range(1, len(motif)):
        while k and motif[i] != motif[k]:
            k = pi[k - 1]
        if motif[i] == motif[k]:
            k += 1
        pi[i] = k
    return pi

def kmp(texte, motif):                           # positions de toutes les occurrences
    pi, k, positions = table_prefixes(motif), 0, []
    for i, c in enumerate(texte):
        while k and c != motif[k]:
            k = pi[k - 1]
        if c == motif[k]:
            k += 1
        if k == len(motif):
            positions.append(i - k + 1)
            k = pi[k - 1]
    return positions                              # O(n + m)

print(kmp("abababcabab", "abab"))                 # [0, 2, 7]
```

## 24.3 Algorithme de Rabin-Karp

On compare des **empreintes** (hachage roulant) au lieu de chaînes entières, puis on **vérifie** les candidats.

```python
def rabin_karp(texte, motif, base=256, mod=10**9 + 7):
    n, m = len(texte), len(motif)
    if m > n: return []
    puissance = pow(base, m - 1, mod)
    h_motif = h_texte = 0
    for i in range(m):
        h_motif = (h_motif * base + ord(motif[i])) % mod
        h_texte = (h_texte * base + ord(texte[i])) % mod
    positions = []
    for i in range(n - m + 1):
        if h_motif == h_texte and texte[i:i + m] == motif:     # vérification (collisions possibles)
            positions.append(i)
        if i < n - m:                                          # fait glisser la fenêtre en O(1)
            h_texte = ((h_texte - ord(texte[i]) * puissance) * base + ord(texte[i + m])) % mod
    return positions
```

**O(n + m) en moyenne**, O(n · m) au pire (collisions). Très utile pour chercher **plusieurs motifs** ou détecter des **doublons de sous-chaînes**.

## 24.4 Algorithme Z

`Z[i]` = longueur du plus long préfixe de la chaîne commun avec le suffixe commençant en `i`.

```python
def z_algorithme(s):
    n, z = len(s), [0] * len(s)
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z                                     # O(n)
# Recherche de motif : z_algorithme(motif + "#" + texte) ; Z[i] == len(motif) → occurrence
```

## 24.5 Trie (arbre préfixe)

Arbre où chaque arête porte un caractère : insertion et recherche en **O(L)** (longueur du mot), indépendamment du nombre de mots stockés.

```python
class Trie:
    def __init__(self):
        self.enfants = {}
        self.fin_de_mot = False

    def inserer(self, mot):
        noeud = self
        for c in mot:
            noeud = noeud.enfants.setdefault(c, Trie())
        noeud.fin_de_mot = True

    def _noeud(self, prefixe):
        noeud = self
        for c in prefixe:
            noeud = noeud.enfants.get(c)
            if noeud is None: return None
        return noeud

    def contient(self, mot):
        n = self._noeud(mot)
        return n is not None and n.fin_de_mot

    def commence_par(self, prefixe):
        return self._noeud(prefixe) is not None

    def completions(self, prefixe):               # tous les mots qui commencent par `prefixe`
        resultat = []
        def parcourir(noeud, chemin):
            if noeud.fin_de_mot: resultat.append(prefixe + chemin)
            for c, e in noeud.enfants.items(): parcourir(e, chemin + c)
        n = self._noeud(prefixe)
        if n: parcourir(n, "")
        return resultat
```

Usages : **autocomplétion**, correcteurs orthographiques, **routage IP** (trie binaire), recherche de mots dans une grille, dictionnaires, **Aho-Corasick** (recherche simultanée de plusieurs motifs).

## 24.6 Autres outils

| Outil | Rôle | Complexité |
| --- | --- | --- |
| **Manacher** | Plus longs palindromes en tout centre | O(n) |
| **Tableau des suffixes + LCP** | Recherche de sous-chaînes, plus longue sous-chaîne répétée | O(n log n) à O(n) |
| **Aho-Corasick** | Plusieurs motifs à la fois | O(n + m + occurrences) |
| **Distance d'édition** | Similarité (DP, [section 18](#185-problèmes-2d)) | O(nm) |
| **Hachage polynomial** | Comparaison de sous-chaînes en O(1) après précalcul | O(n) |

## 24.7 Comparaison des recherches de motif

| Algorithme | Précalcul | Recherche | Remarque |
| --- | --- | --- | --- |
| Naïf | — | O(n · m) | Simple, suffisant pour de petits motifs |
| **KMP** | O(m) | **O(n)** | Garanti, sans hachage |
| **Rabin-Karp** | O(m) | O(n) moyen | Plusieurs motifs, hachage |
| **Z** | O(n + m) | O(n) | Simple, polyvalent |
| `str.find` / `in` (Python) | — | Rapide en pratique | Algorithme optimisé et hybride, à préférer en production |

---

# 25. Aller plus loin

## 25.1 Sujets avancés et de compétition

| Domaine | Sujets |
| --- | --- |
| **Structures de données** | **Décomposition lourde-légère** (*Heavy-Light Decomposition*), **décomposition en centroïdes**, **algorithme de Mo**, structures **persistantes**, arbres d'ondelettes, treaps, arbres à intervalles, **LCA** (ancêtre commun) |
| **Théorie des nombres** | Restes chinois, indicatrice d'Euler, résidus quadratiques, **FFT / NTT** (multiplication de polynômes) |
| **Géométrie algorithmique** | **Enveloppe convexe**, balayage de ligne, intersection de segments, paire de points la plus proche |
| **Théorie des jeux** | Nombres de **Grundy** (Sprague-Grundy), **minimax** et **élagage alpha-bêta** |
| **Algèbre linéaire** | Exponentiation de matrices, élimination de Gauss |
| **Combinatoire** | Inclusion-exclusion, nombres de Catalan, Burnside |
| **Graphes avancés** | Appariement général (Blossom), **2-SAT**, ponts et points d'articulation, flots à coût minimal, circuits eulériens |

## 25.2 Complexité et difficulté : P, NP et au-delà *(ajout)*

| Classe | Signification | Exemples |
| --- | --- | --- |
| **P** | Résoluble en temps **polynomial** | Tri, plus courts chemins, flots |
| **NP** | Une solution proposée se **vérifie** en temps polynomial | Sudoku, SAT, sac à dos |
| **NP-complet** | Les plus difficiles de NP ; si l'un est dans P, tous le sont | SAT, TSP (décision), coloration, cycle hamiltonien, sac à dos (décision) |
| **NP-difficile** | Au moins aussi dur que NP | TSP (optimisation) |

Si un problème est **NP-difficile**, on se tourne vers :

- des algorithmes **exacts exponentiels** raisonnables (DP par masques, retour sur trace avec élagage, *branch & bound*) ;
- des algorithmes d'**approximation** (garantie sur la qualité) ;
- des **heuristiques** et **métaheuristiques** (recuit simulé, algorithmes génétiques) ;
- des **solveurs** (SAT, programmation linéaire en nombres entiers, OR-Tools).

La question **P = NP ?** reste ouverte.

## 25.3 Résumé : quel algorithme pour quel problème ?

| Problème | Technique / algorithme |
| --- | --- |
| Chercher dans un tableau trié | Recherche binaire / `bisect` |
| Trouver une valeur optimale monotone | Recherche binaire sur la réponse |
| Paires / triplets dans un tableau trié | Deux pointeurs |
| Sous-tableau / sous-chaîne contigu optimal | Fenêtre glissante |
| Somme sur un intervalle (statique) | Sommes préfixes |
| Somme sur un intervalle (dynamique) | Fenwick / arbre de segments |
| Compter, regrouper, tester l'appartenance | Hachage |
| Choix localement optimal prouvé | Glouton |
| Sous-problèmes qui se chevauchent | **Programmation dynamique** |
| Explorer toutes les configurations avec élagage | Retour sur trace |
| Plus court chemin, non pondéré | BFS |
| Plus court chemin, poids ≥ 0 | Dijkstra |
| Plus court chemin, poids négatifs | Bellman-Ford |
| Toutes les paires de plus courts chemins | Floyd-Warshall |
| Dépendances / ordonnancement | Tri topologique |
| Connecter à coût minimal | Kruskal / Prim |
| Composantes connexes dynamiques | Union-Find |
| Cycles dans un graphe orienté, SCC | Tarjan / Kosaraju |
| Capacité maximale d'un réseau, appariement | Flot maximal (Dinic) |
| Recherche de motif | KMP, Z, Rabin-Karp |
| Autocomplétion, préfixes | Trie |
| Trier | `sorted()` (Timsort) ; comptage / radix si les clés s'y prêtent |

## 25.4 Conseils de progression

1. **Maîtrisez les bases** : complexité, tableaux, récursivité, tris, recherche.
2. **Apprenez les schémas** (deux pointeurs, fenêtre, préfixes, hachage, binaire sur la réponse) : ils couvrent la majorité des problèmes d'entretien.
3. **Pratiquez régulièrement** : un problème par jour vaut mieux que dix le week-end.
4. **Écrivez le brute force d'abord**, puis optimisez ; comparez les deux sur des tests aléatoires.
5. **Analysez** toujours la complexité avant de coder.
6. **Relisez** vos solutions : pourquoi ça marche ? Quels cas limites ?
7. **Étudiez** les solutions des autres une fois que vous avez cherché.

## 25.5 Ressources

- 📘 *Introduction à l'algorithmique* — Cormen, Leiserson, Rivest, Stein (**CLRS**)
- 📗 *The Algorithm Design Manual* — Steven Skiena
- 📙 *Algorithms* — Sedgewick & Wayne (et leur site compagnon)
- 📕 *Competitive Programmer's Handbook* — Antti Laaksonen (gratuit)
- 🌐 **cp-algorithms.com** : référence très complète de compétition
- 🧩 **LeetCode**, **Codeforces**, **AtCoder**, **Kattis**, **Advent of Code**, **Project Euler**, **France-IOI** (en français)
- 🎞️ **VisuAlgo** (visualisations animées), **Python Tutor** (exécution pas à pas)

---

<div align="center">

*Bon voyage au pays des algorithmes ! 🧮*

</div>
