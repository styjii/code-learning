# 🧠 Exercices d'algorithmique (avec Python)

> Treize exercices progressifs pour apprendre à **raisonner avant de coder** : trouver un maximum, manipuler des chaînes, utiliser des ensembles et des dictionnaires, fusionner, faire de la programmation dynamique… Chaque exercice se résout avec la **même démarche**, décrite une seule fois ci-dessous.

## 📑 Sommaire

1. [Méthode de travail (valable pour tous les exercices)](#1-méthode-de-travail-valable-pour-tous-les-exercices)
2. [Notions de complexité](#2-notions-de-complexité)
3. [Exercices de base](#3-exercices-de-base)
4. [Exercices intermédiaires et avancés](#4-exercices-intermédiaires-et-avancés)
5. [Exercices complémentaires](#5-exercices-complémentaires)
6. [Tableau récapitulatif](#6-tableau-récapitulatif)

---

## 1. Méthode de travail (valable pour tous les exercices)

Pour **chaque** exercice, suivez ces cinq étapes :

| Étape | Action |
| :---: | --- |
| 1️⃣ | **Comprendre** : reformulez l'énoncé, listez les entrées, les sorties et les cas limites (liste vide, un seul élément, doublons, valeurs négatives…). |
| 2️⃣ | **Concevoir** l'algorithme sur papier, en français. |
| 3️⃣ | **Écrire le pseudo-code** (modèle ci-dessous). |
| 4️⃣ | **Implémenter** en Python et **tester** (exemples de l'énoncé + vos propres cas limites). |
| 5️⃣ | **Analyser la complexité** en temps et en mémoire, puis chercher à l'améliorer. |

### Modèle de pseudo-code

```text
ALGORITHME nom_de_l_algorithme
ENTRÉE  : description des paramètres
SORTIE  : description du résultat

DÉBUT
    maximum ← premier élément de la liste
    POUR CHAQUE élément DANS la liste FAIRE
        SI élément > maximum ALORS
            maximum ← élément
        FIN SI
    FIN POUR
    RETOURNER maximum
FIN
```

### Conventions Python

- **Python 3.11+**, avec des **annotations de type** (`list[int]`, `str | None`).
- Une fonction pure par exercice : elle **retourne** son résultat au lieu de l'afficher.
- Vérifiez vos fonctions avec des tests automatiques, par exemple avec `pytest` :

```python
# test_exercices.py  →  lancer avec :  pytest
from exercices import plus_grand

def test_plus_grand():
    assert plus_grand([3, 5, 7, 2, 8, 1]) == 8
    assert plus_grand([-4, -2, -9]) == -2   # cas limite : que des négatifs
    assert plus_grand([42]) == 42           # cas limite : un seul élément
```

> 💡 Sans `pytest`, de simples instructions `assert` fonctionnent très bien.

---

## 2. Notions de complexité

La **complexité** mesure comment le temps (ou la mémoire) évolue quand la taille *n* des données augmente. On l'exprime avec la notation **O( )**.

| Notation | Nom | Exemple typique |
| --- | --- | --- |
| `O(1)` | constante | Accéder à `liste[i]` |
| `O(log n)` | logarithmique | Recherche dichotomique |
| `O(n)` | linéaire | Parcourir une liste une fois |
| `O(n log n)` | quasi-linéaire | Tri efficace (`sorted`) |
| `O(n²)` | quadratique | Deux boucles imbriquées |
| `O(2ⁿ)` | exponentielle | Fibonacci récursif naïf |

> ⚠️ En Python, `x in liste` coûte **O(n)**, alors que `x in ensemble` (`set`) ou `x in dictionnaire` coûte **O(1)** en moyenne. Ce détail change souvent la complexité d'un algorithme.

---

## 3. Exercices de base

### Exercice 1 : Le plus grand nombre

**Énoncé** : écrivez un algorithme qui renvoie le plus grand entier d'une liste.

```python
def plus_grand(nombres: list[int]) -> int: ...
```

| Entrée | Sortie |
| --- | --- |
| `[3, 5, 7, 2, 8, 1]` | `8` |

**Contraintes**
- La liste contient au moins un nombre.
- Les nombres peuvent être positifs, négatifs ou nuls.

**Pistes et bonus**
- ⚠️ Piège classique : initialiser le maximum à `0` donne un résultat faux pour `[-4, -2, -9]`. Partez du **premier élément**.
- Écrivez-le d'abord sans `max()`, puis comparez avec la fonction intégrée.

---

### Exercice 2 : Palindrome

**Énoncé** : vérifiez si un texte est un **palindrome**, c'est-à-dire s'il se lit de la même façon dans les deux sens, en **ignorant les espaces, la ponctuation et la casse**.

```python
def est_palindrome(texte: str) -> bool: ...
```

| Entrée | Sortie |
| --- | --- |
| `"A man a plan a canal Panama"` | `True` |
| `"A man, a plan, a canal, Panama"` | `True` |
| `"racecar"` | `True` |
| `"hello"` | `False` |

**Niveaux**
- 🟢 **Niveau A** : le texte ne contient que des lettres et des espaces.
- 🟡 **Niveau B** : le texte peut aussi contenir des chiffres et de la ponctuation.

**Pistes et bonus**
- Outils utiles : `str.isalnum()`, `str.casefold()`.
- 🟣 **Bonus 1** : utilisez deux indices (début et fin) qui se rapprochent, sans créer de copie inversée (mémoire `O(1)`).
- 🟣 **Bonus 2** : gérez les accents (`"Été"`) avec `unicodedata.normalize("NFD", ...)`.

---

### Exercice 3 : Le deuxième plus grand nombre

**Énoncé** : renvoyez le deuxième plus grand nombre **distinct** d'une liste non triée.

```python
def deuxieme_plus_grand(nombres: list[int]) -> int: ...
```

| Entrée | Sortie |
| --- | --- |
| `[12, 35, 1, 10, 34, 1]` | `34` |
| `[1, 2, 3, 4, 5]` | `4` |
| `[5, 5, 3]` | `3` |

**Contraintes**
- La liste contient au moins deux valeurs **distinctes**.
- Les nombres peuvent être positifs, négatifs ou nuls.

**Pistes et bonus**
- Version simple : trier la liste (`O(n log n)`). Attention aux doublons du maximum (voir le 3ᵉ exemple).
- 🟣 **Bonus** : un seul parcours, deux variables (`premier`, `deuxieme`), sans tri : `O(n)`.

---

### Exercice 4 : Le nombre manquant

**Énoncé** : une liste non triée contient tous les entiers de `1` à `n` **sauf un**. Trouvez le nombre manquant.

```python
def nombre_manquant(nombres: list[int], n: int) -> int: ...
```

| Entrée | Sortie |
| --- | --- |
| `[1, 2, 4, 5, 6]`, `n = 6` | `3` |
| `[3, 7, 1, 2, 8, 4, 5]`, `n = 8` | `6` |

**Pistes et bonus** (trois approches à comparer)
- **Somme** : `n × (n + 1) / 2` moins la somme de la liste.
- **XOR** : le XOR de tous les nombres de `1..n` et de la liste donne le manquant.
- **Ensemble** : différence entre `set(range(1, n + 1))` et `set(nombres)`.
- 💡 Python n'a pas de dépassement d'entier, mais dans d'autres langages (le C, par exemple), la somme peut déborder : la méthode XOR n'a pas ce défaut.

---

### Exercice 5 : Éléments communs (intersection de deux listes)

**Énoncé** : renvoyez la liste des éléments présents dans **les deux** listes, **sans doublon**.

```python
def elements_communs(liste1: list[int], liste2: list[int]) -> list[int]: ...
```

| Entrée | Sortie |
| --- | --- |
| `[1, 2, 3, 4, 5]` et `[4, 5, 6, 7, 8]` | `[4, 5]` |
| `[10, 20, 30, 40]` et `[50, 60, 70, 80]` | `[]` |
| `[1, 2, 2, 1]` et `[2, 2]` | `[2]` |
| `[4, 9, 5]` et `[9, 4, 9, 8, 4]` | `[4, 9]` (ordre quelconque) |

**Contraintes**
- Les listes peuvent contenir des doublons.
- Le résultat ne contient que des éléments **distincts**, dans **n'importe quel ordre** (pensez à comparer avec `sorted()` dans vos tests).

**Pistes et bonus**
- Version naïve : deux boucles imbriquées, `O(n × m)`.
- Version efficace : des **ensembles** (`set`), `O(n + m)`.

---

## 4. Exercices intermédiaires et avancés

### Exercice 6 : Rotation d'un tableau

**Énoncé** : décalez les éléments d'un tableau de `k` positions vers la **droite**. Les éléments qui dépassent reviennent au début.

```python
def pivoter(tableau: list[int], k: int) -> None: ...   # modifie la liste en place
```

| Entrée | Sortie |
| --- | --- |
| `[1, 2, 3, 4, 5]`, `k = 2` | `[4, 5, 1, 2, 3]` |
| `[1, 2, 3, 4, 5]`, `k = 4` | `[2, 3, 4, 5, 1]` |
| `[1, 2, 3]`, `k = 7` | `[3, 1, 2]` |

**Contraintes**
- Le tableau peut contenir des doublons (et peut être vide : pas de division par zéro !).
- `k` est un entier positif ou nul, éventuellement **plus grand que la longueur** du tableau.
- Modification **en place** : pas de second tableau.

**Pistes et bonus**
- Réduisez d'abord `k` avec `k %= len(tableau)`.
- Méthode des **trois inversions** : inverser tout le tableau, puis les `k` premiers éléments, puis les `n − k` derniers. Temps `O(n)`, mémoire `O(1)`.
- ⚠️ `tableau[:] = tableau[-k:] + tableau[:-k]` est court, mais crée des listes temporaires (cela viole la contrainte « sans espace supplémentaire »).

---

### Exercice 7 : Premier caractère unique

**Énoncé** : renvoyez le **premier** caractère de la chaîne qui n'apparaît **qu'une seule fois**, ou `None` s'il n'y en a pas.

```python
def premier_caractere_unique(texte: str) -> str | None: ...
```

| Entrée | Sortie |
| --- | --- |
| `"swiss"` | `"w"` |
| `"hello"` | `"h"` |
| `"aabbcc"` | `None` |

**Contraintes**
- La chaîne ne contient que des lettres (minuscules ou majuscules).
- La comparaison est **sensible à la casse** (`"a"` et `"A"` sont deux caractères différents).

**Pistes et bonus**
- Deux parcours : compter les occurrences (`collections.Counter` ou dictionnaire), puis chercher le premier caractère dont le compteur vaut 1. Complexité `O(n)`.

---

### Exercice 8 : Fusion de deux tableaux triés

**Énoncé** : fusionnez deux tableaux triés par ordre croissant en un seul tableau trié.

```python
def fusionner(arr1: list[int], arr2: list[int]) -> list[int]: ...
```

| Entrée | Sortie |
| --- | --- |
| `[1, 3, 5, 7]` et `[2, 4, 6, 8]` | `[1, 2, 3, 4, 5, 6, 7, 8]` |
| `[1, 10, 20]` et `[5, 15, 25]` | `[1, 5, 10, 15, 20, 25]` |

**Contraintes**
- Les deux tableaux sont déjà triés par ordre croissant (au sens large).
- Complexité attendue : **O(n + m)**, où `n` et `m` sont les longueurs des tableaux.

**Pistes et bonus**
- Technique des **deux pointeurs** : comparez les éléments courants et avancez dans le tableau dont vous venez de prendre la valeur ; n'oubliez pas le reste de l'autre tableau.
- ❌ Écrire `sorted(arr1 + arr2)` fonctionne, mais coûte `O((n + m) log(n + m))` : c'est interdit ici.
- 🟣 **Bonus** : comparez avec `heapq.merge` de la bibliothèque standard.

---

### Exercice 9 : Plus longue sous-suite croissante (LIS)

**Énoncé** : dans un tableau d'entiers, trouvez la plus longue **sous-suite strictement croissante**. Elle n'a pas besoin d'être contiguë, mais doit respecter l'ordre du tableau d'origine.

```python
def plus_longue_sous_suite_croissante(tableau: list[int]) -> list[int]: ...
```

| Entrée | Sortie |
| --- | --- |
| `[10, 22, 9, 33, 21, 50, 41, 60, 80]` | `[10, 22, 33, 50, 60, 80]` (longueur 6) |
| `[3, 10, 2, 1, 20]` | `[3, 10, 20]` (longueur 3) |

**Contraintes**
- Le tableau peut contenir des entiers positifs et négatifs.
- Il faut renvoyer la **sous-suite**, pas seulement sa longueur.
- Plusieurs réponses peuvent être valides : testez la **longueur** et le caractère croissant du résultat.

**Pistes et bonus**
- 🔴 **Programmation dynamique**, `O(n²)` : `longueur[i]` = longueur de la meilleure sous-suite finissant à l'indice `i`, et un tableau `precedent[i]` pour reconstruire la sous-suite.
- 🟣 **Bonus** : version `O(n log n)` avec le module `bisect`.

---

## 5. Exercices complémentaires

> ➕ Ces exercices ont été ajoutés pour couvrir des notions fondamentales absentes de la série initiale : **tables de hachage, recherche dichotomique, pile, récursivité et mémoïsation**.

### Exercice 10 : Somme de deux nombres (*Two Sum*)

**Énoncé** : étant donné une liste d'entiers et une valeur `cible`, renvoyez les **indices** de deux éléments distincts dont la somme vaut `cible`.

```python
def deux_sommes(nombres: list[int], cible: int) -> tuple[int, int] | None: ...
```

| Entrée | Sortie |
| --- | --- |
| `[2, 7, 11, 15]`, `cible = 9` | `(0, 1)` |
| `[3, 2, 4]`, `cible = 6` | `(1, 2)` |
| `[1, 2]`, `cible = 10` | `None` |

**Pistes** : version naïve `O(n²)` ; version `O(n)` avec un **dictionnaire** `valeur → indice` qui mémorise ce qu'on a déjà vu.

---

### Exercice 11 : Recherche dichotomique

**Énoncé** : dans un tableau **trié**, renvoyez l'indice d'une valeur, ou `-1` si elle est absente, en `O(log n)`.

```python
def recherche_dichotomique(tableau_trie: list[int], valeur: int) -> int: ...
```

| Entrée | Sortie |
| --- | --- |
| `[1, 3, 5, 7, 9]`, `7` | `3` |
| `[1, 3, 5, 7, 9]`, `4` | `-1` |
| `[]`, `1` | `-1` |

**Pistes** : maintenez deux bornes `bas` et `haut`, et regardez l'élément du milieu. Attention aux erreurs « d'un cran » (`<` contre `<=`) et aux boucles infinies. Comparez avec `bisect.bisect_left`.

---

### Exercice 12 : Parenthèses bien formées

**Énoncé** : vérifiez qu'une chaîne composée de `()`, `[]` et `{}` est **bien parenthésée** (chaque ouvrante est fermée par la bonne fermante, dans le bon ordre).

```python
def est_bien_parenthese(texte: str) -> bool: ...
```

| Entrée | Sortie |
| --- | --- |
| `"([]{})"` | `True` |
| `"([)]"` | `False` |
| `"(("` | `False` |
| `""` | `True` |

**Pistes** : utilisez une **pile** (une `list` avec `append` et `pop`) et un dictionnaire qui associe chaque fermante à son ouvrante.

---

### Exercice 13 : Suite de Fibonacci

**Énoncé** : calculez le `n`-ième nombre de Fibonacci (`F(0) = 0`, `F(1) = 1`, `F(n) = F(n−1) + F(n−2)`) de **trois** façons :

```python
def fibonacci(n: int) -> int: ...
```

| Entrée | Sortie |
| --- | --- |
| `0` | `0` |
| `10` | `55` |
| `50` | `12586269025` |

1. 🟢 **Récursive naïve** : `O(2ⁿ)`. Essayez `n = 40` et observez la lenteur.
2. 🟡 **Avec mémoïsation** : décorateur `functools.cache`, `O(n)`.
3. 🟡 **Itérative** : deux variables, `O(n)` en temps, `O(1)` en mémoire.

**Questions** : pourquoi la version naïve est-elle si lente ? Que se passe-t-il pour un grand `n` avec la version récursive (limite de récursion de Python) ?

---

## 6. Tableau récapitulatif

| # | Exercice | Notion principale | Complexité visée | Niveau |
| :-: | --- | --- | --- | :-: |
| 1 | Plus grand nombre | Parcours, initialisation | `O(n)` | 🟢 |
| 2 | Palindrome | Chaînes, deux pointeurs | `O(n)` | 🟢 / 🟡 |
| 3 | Deuxième plus grand | Parcours à deux variables | `O(n)` | 🟡 |
| 4 | Nombre manquant | Somme, XOR, ensembles | `O(n)` | 🟡 |
| 5 | Éléments communs | Ensembles (`set`) | `O(n + m)` | 🟡 |
| 6 | Rotation d'un tableau | Modulo, inversions en place | `O(n)`, mémoire `O(1)` | 🟡 |
| 7 | Premier caractère unique | Dictionnaire de compteurs | `O(n)` | 🟡 |
| 8 | Fusion de tableaux triés | Deux pointeurs | `O(n + m)` | 🟡 |
| 9 | Sous-suite croissante (LIS) | Programmation dynamique | `O(n²)` puis `O(n log n)` | 🔴 |
| 10 | Two Sum | Table de hachage | `O(n)` | 🟡 |
| 11 | Recherche dichotomique | Diviser pour régner | `O(log n)` | 🟡 |
| 12 | Parenthèses bien formées | Pile | `O(n)` | 🟡 |
| 13 | Fibonacci | Récursivité, mémoïsation | `O(2ⁿ)` puis `O(n)` | 🟢 → 🟡 |
