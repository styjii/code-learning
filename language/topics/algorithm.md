# Algorithmique — Cours complet

*Cours magistral et module d'apprentissage exhaustif, fondé sur le plan « Algorithmique — Guide complet » — Python 3.12 et versions ultérieures (novembre 2026)*

## Avant de commencer : comment utiliser ce cours

Ce cours développe, chapitre par chapitre, l'intégralité du plan en **25 chapitres**, regroupés en trois parties : **Niveau débutant** (1 à 7), **Niveau intermédiaire** (8 à 17) et **Niveau avancé** (18 à 25).

Chaque chapitre suit la même trame : *objectifs d'apprentissage → notions et définitions → exemples de code commentés → pièges fréquents → synthèse*.

**Conventions de lecture**

- Le code est écrit en **Python 3.12 et versions ultérieures** ; les idées présentées sont indépendantes du langage.
- Chaque exemple est volontairement **autonome** : les imports nécessaires sont toujours indiqués.
- **Notation** : `n` désigne la taille de l'entrée, `log` le logarithme en base 2 sauf mention contraire (la base ne change rien aux classes de complexité), et `t[a:b]` les indices de `a` inclus à `b` exclu, comme en Python.
- Les complexités sont données **dans le pire cas** sauf mention contraire ; les notations `O`, `Ω` et `Θ` sont définies au chapitre 2.
- Le cours enseigne les techniques **classiques** (tris, glouton, programmation dynamique, graphes, flots) **et** les outils actuels de la bibliothèque standard (`heapq`, `bisect`, `collections`, `functools`) qui permettent de les implémenter ou de les remplacer en pratique.

**Parcours conseillé** : lisez les chapitres 1 à 7 dans l'ordre (ils se construisent les uns sur les autres), puis les chapitres 8 à 17, qui introduisent les grands schémas de conception. Les chapitres 18 à 25 (programmation dynamique, graphes, flots, chaînes de caractères) peuvent ensuite être abordés selon vos besoins, en suivant les renvois indiqués dans le texte.

---

# Partie I — Niveau débutant

---

## 1. Introduction aux algorithmes

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : définir un algorithme et énoncer ses six propriétés ; distinguer un problème d'une instance ; démontrer la correction (invariant de boucle) et la terminaison (variant) ; représenter un algorithme en langage naturel, en pseudo-code ou par organigramme ; appliquer une méthode de résolution de problème ; situer les grandes familles d'algorithmes et les limites du calculable.

### 1.1 Qu'est-ce qu'un algorithme ?

#### Définition

Un **algorithme** est une suite **finie** d'instructions **précises** et **non ambiguës** qui, appliquée à des **données d'entrée**, produit un **résultat** (la sortie) et permet de résoudre un **problème** donné.

Le mot vient du nom du mathématicien perse Muhammad ibn Musa al-Khwarizmi (IXe siècle), dont les traités de calcul décimal ont popularisé les procédés de calcul systématiques. L'exemple le plus ancien d'algorithme encore utilisé est celui d'Euclide pour le plus grand commun diviseur (vers 300 avant notre ère), que nous étudierons au chapitre 7.

#### Problème et instance

Il faut distinguer deux notions souvent confondues :

- un **problème** est une question générale, décrite par un ensemble d'entrées possibles et la relation que la sortie doit vérifier avec l'entrée. Exemple : « trier une liste d'entiers » ;
- une **instance** est un cas particulier du problème, c'est-à-dire une entrée concrète. Exemple : la liste `[5, 2, 9, 1]`.

Un algorithme résout un **problème** : il doit fonctionner pour **toutes** les instances valides, pas seulement pour quelques exemples.

#### Les six propriétés fondamentales

| Propriété | Signification détaillée |
| --- | --- |
| **Entrée** | L'algorithme reçoit zéro, une ou plusieurs données, appartenant à un domaine défini à l'avance (par exemple « une liste non vide d'entiers »). Ce domaine constitue la **précondition** |
| **Sortie** | L'algorithme produit au moins un résultat, lié de façon précise à l'entrée. La relation attendue constitue la **postcondition** |
| **Précision** | Chaque étape est définie sans ambiguïté : deux exécutants différents doivent faire exactement la même chose. « Ajouter un peu de sel » n'est pas une instruction algorithmique |
| **Finitude** | L'exécution s'arrête après un nombre fini d'étapes, pour toute entrée valide. On parle de **terminaison** |
| **Effectivité** | Chaque instruction est réalisable en pratique, avec des moyens finis, par exemple une addition ou une comparaison |
| **Correction** | Pour toute entrée valide, la sortie vérifie la postcondition. Un algorithme rapide mais faux est inutile |

> **Analogie.** Une recette de cuisine : les ingrédients sont l'entrée, les étapes sont l'algorithme, le plat est la sortie. Une recette imprécise (« cuire jusqu'à ce que ce soit bon ») ou qui ne s'arrête jamais n'est pas un algorithme au sens strict.

#### Premier exemple complet

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

- **Entrée** : une liste non vide de nombres (précondition).
- **Sortie** : un élément `m` de la liste tel que `m >= x` pour tout `x` de la liste (postcondition).
- **Finitude** : la boucle `for` parcourt une liste finie.
- **Correction** : voir la section suivante.

### 1.2 Corriger et terminer : démontrer qu'un algorithme est juste

Tester un algorithme sur quelques exemples ne prouve rien : un test réussi n'établit pas la correction. Deux outils théoriques permettent de raisonner.

#### L'invariant de boucle

Un **invariant de boucle** est une propriété qui est vraie **avant la première itération** et qui reste vraie **après chaque itération**. Une preuve par invariant comporte trois étapes :

1. **Initialisation** : l'invariant est vrai avant la boucle.
2. **Conservation** : si l'invariant est vrai avant une itération, il l'est encore après.
3. **Conclusion** : à la sortie de la boucle, l'invariant joint à la condition d'arrêt entraîne la postcondition.

**Application à `maximum`.** Invariant : « après avoir traité les `k` premiers éléments, `meilleur` est le maximum de ces `k` éléments ».

- Initialisation : avant la boucle, `meilleur = valeurs[0]` est le maximum du seul premier élément.
- Conservation : si `meilleur` est le maximum des `k` premiers, alors après comparaison avec `v`, le nouveau `meilleur` est le maximum de `k+1` éléments.
- Conclusion : à la fin, `k = n`, donc `meilleur` est le maximum de toute la liste.

#### Le variant de boucle (preuve de terminaison)

Un **variant** est une quantité entière, positive, qui **décroît strictement** à chaque itération. Comme il n'existe pas de suite d'entiers naturels strictement décroissante infinie, la boucle s'arrête.

- Dans une boucle `while b != 0: a, b = b, a % b` (algorithme d'Euclide), le variant est `b`, car `a % b < b` : il décroît strictement et reste positif.
- Dans une boucle `for`, le nombre d'itérations restantes est le variant.

Pour un algorithme récursif, on raisonne de la même façon : la **taille du problème** doit décroître à chaque appel et atteindre un cas de base (chapitre 4).

#### Une illustration de ce qui peut mal tourner

La **suite de Syracuse** (diviser par 2 si pair, sinon remplacer par 3n+1) est un procédé parfaitement précis, mais personne ne sait démontrer qu'il se termine pour tout entier de départ : on ne peut donc pas affirmer qu'il constitue un algorithme au sens strict pour tout entier.

```python
def syracuse(n):
    etapes = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        etapes += 1
    return etapes

print(syracuse(27))   # 111
```

### 1.3 Pourquoi les algorithmes sont-ils importants ?

- **Efficacité** : le choix de l'algorithme peut faire passer un calcul de plusieurs jours à quelques secondes, bien plus que le choix du langage ou de la machine.
- **Résolution de problèmes** : étudier les algorithmes apprend à décomposer, généraliser et prouver.
- **Fondement des logiciels** : moteurs de recherche, GPS, compression de données, chiffrement, bases de données, recommandations, intelligence artificielle.
- **Évaluation professionnelle** : les entretiens techniques et les compétitions de programmation reposent sur ces compétences.

L'écart entre deux algorithmes devient énorme lorsque `n` grandit :

| Taille `n` | Algorithme en O(n²) | Algorithme en O(n log n) |
| --- | --- | --- |
| 1 000 | environ 1 million d'opérations | environ 10 000 |
| 1 000 000 | environ 10¹² (plusieurs heures) | environ 2 × 10⁷ (une fraction de seconde en langage compilé) |

Le rapport entre les deux est de l'ordre de `n / log n` : plus l'entrée est grande, plus le bon algorithme est décisif. Aucune amélioration matérielle ne compense une mauvaise complexité asymptotique.

### 1.4 Représenter un algorithme

| Mode | Description | Usage |
| --- | --- | --- |
| **Langage naturel** | Étapes décrites en français | Première approche, communication |
| **Pseudo-code** | Structure proche d'un langage de programmation, sans syntaxe stricte | Le plus courant dans les cours et publications |
| **Organigramme** | Schéma avec boîtes de début, d'actions, de décisions et de fin | Algorithmes courts, pédagogie |
| **Code** | Implémentation dans un langage précis | Exécution réelle |

Les briques de toute représentation sont les mêmes :

- **variables et affectation** : `max ← tableau[0]` ;
- **séquence** : instructions exécutées l'une après l'autre ;
- **alternative (conditionnelle)** : `SI condition ALORS … SINON …` ;
- **itération** : `POUR … FAIRE`, `TANT QUE … FAIRE` ;
- **appel de sous-algorithme** (fonction, procédure), éventuellement récursif.

Ces quelques constructions suffisent à exprimer n'importe quel algorithme (c'est le contenu du théorème de programmation structurée).

```text
ALGORITHME TrouverMaximum(tableau)
  Entrée : un tableau non vide de nombres
  Sortie : le plus grand nombre du tableau
  max ← tableau[0]
  POUR chaque x DANS tableau FAIRE
      SI x > max ALORS max ← x
  RETOURNER max
```

### 1.5 Écrire son premier algorithme pas à pas

**Problème** : calculer la moyenne de trois notes.

1. Lire les trois notes `a`, `b`, `c` (entrée).
2. Calculer `somme ← a + b + c`.
3. Calculer `moyenne ← somme / 3`.
4. Afficher `moyenne` (sortie).

```python
a, b, c = 12, 15, 9
print((a + b + c) / 3)    # 12.0
```

Cet exemple ne contient ni boucle ni test : c'est une **séquence** pure. Il se termine toujours et est correct pour toute entrée numérique.

### 1.6 Méthode pour résoudre un problème algorithmique

| Étape | Questions à se poser |
| --- | --- |
| 1. **Comprendre** | Quelles sont les entrées, les sorties, les contraintes (taille de `n`, plage de valeurs) ? Que se passe-t-il si l'entrée est vide ? |
| 2. **Exemples** | Écrire des petits cas à la main, ainsi que les **cas limites** : liste vide, un seul élément, doublons, valeurs négatives, tout identique, déjà trié |
| 3. **Solution naïve** | Une approche par force brute, même lente, mais correcte. Elle sert de référence pour les tests |
| 4. **Optimiser** | Quelle structure de données ? Quel schéma de conception (glouton, diviser pour régner, DP…) ? |
| 5. **Analyser** | Complexité en temps et en espace, dans le pire cas |
| 6. **Coder et tester** | Jeux de tests, cas limites, comparaison automatique avec la solution naïve sur des entrées aléatoires |

Les **contraintes guident le choix de l'algorithme**. Avec une limite d'environ 10⁸ opérations simples par seconde en langage compilé :

| Taille maximale `n` | Complexité visée |
| --- | --- |
| n ≤ 10 à 12 | O(n!) acceptable (permutations) |
| n ≤ 20 à 25 | O(2ⁿ) acceptable (sous-ensembles) |
| n ≤ 500 | O(n³) |
| n ≤ 5 000 | O(n²) |
| n ≤ 10⁵ à 10⁶ | O(n log n) ou O(n) |
| n ≤ 10⁹ et plus | O(log n) ou formule fermée |

### 1.7 Les grandes familles d'algorithmes

| Famille | Idée directrice | Exemples (chapitre) |
| --- | --- | --- |
| **Force brute** | Tout essayer | Recherche linéaire (6) |
| **Diviser pour régner** | Diviser, résoudre récursivement, combiner | Tri fusion, recherche binaire (8, 9) |
| **Glouton** | Meilleur choix local à chaque étape, sans retour | Huffman, Kruskal, Dijkstra (10, 19, 20) |
| **Programmation dynamique** | Mémoriser les sous-problèmes qui se chevauchent | Sac à dos, plus longue sous-séquence commune (18) |
| **Retour sur trace** | Explorer, annuler en cas d'impasse | N reines, Sudoku (11) |
| **Algorithmes sur les graphes** | Parcours, chemins, flots | BFS, Dijkstra (19 à 22) |
| **Algorithmes probabilistes** | Utilisent le hasard | Quicksort aléatoire, Miller-Rabin (8, 16) |
| **Séparation et évaluation** | Élagage par bornes | Voyageur de commerce exact (25) |

### 1.8 Algorithme ou programme ?

|  | Algorithme | Programme |
| --- | --- | --- |
| Nature | **Idée** abstraite, indépendante du langage | **Implémentation** concrète |
| Forme | Pseudo-code, schéma, texte | Code source |
| Dépend de la machine | Non | Oui |
| Finitude | Obligatoire | Facultative (serveur, jeu vidéo, système d'exploitation) |
| Exemple | « Trier par fusion » | `sorted(liste)` en Python |

### 1.9 Limites : ce que les algorithmes ne peuvent pas tout faire

Tout problème n'admet pas d'algorithme. Alan Turing a démontré en 1936 que le **problème de l'arrêt** (décider si un programme donné s'arrête sur une entrée donnée) est **indécidable** : aucun algorithme ne le résout pour tous les programmes. Par ailleurs, certains problèmes décidables sont **intraitables en pratique** car tout algorithme connu exige un temps exponentiel (classe NP-difficile, chapitre 25).

### 1.10 Pièges fréquents

- Conclure qu'un algorithme est correct parce qu'il réussit quelques tests : un test ne prouve rien, il faut un **invariant**.
- Oublier la **terminaison** (une boucle `while` dont le variant ne décroît pas) ou la **précondition** (liste vide, valeur absente).
- Confondre **algorithme** (l'idée) et **programme** (son implémentation), ou **problème** et **instance**.
- Coder avant d'avoir lu les **contraintes** : elles dictent la complexité à viser.

### Synthèse du chapitre 1

Un **algorithme** est une suite finie d'instructions précises qui résout un problème pour **toute** instance valide. Retenez ses six propriétés (entrée, sortie, précision, finitude, effectivité, correction), l'**invariant** pour prouver la correction, le **variant** pour prouver la terminaison, la démarche de résolution (comprendre, exemples, version naïve, optimisation, analyse, tests) et le rôle des **contraintes sur `n`** dans le choix de la complexité visée.

---

## 2. Analyse des algorithmes

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : décrire le modèle de calcul RAM et mesurer la taille d'une entrée ; compter les opérations d'une boucle ou d'une récursion ; utiliser les notations `O`, `Ω`, `Θ`, `o` et `ω` avec leurs définitions formelles ; distinguer pire cas, meilleur cas et cas moyen ; reconnaître les classes de complexité usuelles ; analyser l'espace mémoire et le coût amorti ; résoudre des récurrences simples ; justifier la borne `Ω(n log n)` des tris par comparaisons.

### 2.1 Pourquoi analyser ?

Mesurer un temps d'exécution en secondes dépend de la machine, du langage, du compilateur, de la charge système et des données. Pour comparer des algorithmes de façon **objective et reproductible**, on étudie plutôt **comment le coût croît avec la taille `n` de l'entrée**.

| Ressource | Mesure |
| --- | --- |
| **Complexité en temps** | Nombre d'opérations élémentaires en fonction de `n` |
| **Complexité en espace** | Mémoire supplémentaire utilisée en fonction de `n` |

#### Le modèle de calcul : la machine RAM

On raisonne sur un modèle simplifié, la **machine RAM** (*Random Access Machine*) :

- la mémoire est un tableau de cases accessibles en **temps constant** ;
- les **opérations élémentaires** (addition, comparaison, affectation, accès à une case, branchement) coûtent chacune **une unité de temps** ;
- les entiers manipulés tiennent dans un « mot » machine.

Ce modèle est une approximation. Elle devient fausse quand les entiers sont gigantesques (la multiplication de nombres de milliers de chiffres n'est plus en temps constant) ou quand la hiérarchie des caches de la mémoire domine. Il reste excellent pour comparer des algorithmes.

#### La taille de l'entrée

La **taille** `n` est la quantité de données : nombre d'éléments d'un tableau, nombre de sommets et d'arêtes d'un graphe, longueur d'une chaîne. Pour un nombre entier `N`, la taille naturelle est le nombre de chiffres, soit environ `log N` : un algorithme en `O(N)` est donc **exponentiel en la taille de la donnée** `N` (on parle de complexité **pseudo-polynomiale**, notion qui réapparaîtra avec le sac à dos).

### 2.2 Compter les opérations

```python
def somme(t):
    total = 0              # 1 opération
    for x in t:            # n itérations
        total += x         # 1 opération chacune
    return total           # 1 opération
# T(n) = n + 2, donc O(n)
```

Règles de dénombrement :

| Structure | Coût |
| --- | --- |
| Instruction simple | O(1) |
| Séquence de blocs | Somme des coûts, donc le plus grand domine |
| Boucle de `n` itérations de coût constant | O(n) |
| Deux boucles imbriquées de `n` itérations | O(n²) |
| Boucle qui divise par 2 à chaque tour (`while n > 1: n //= 2`) | O(log n) |
| Boucle qui double à chaque tour (`i *= 2` jusqu'à `n`) | O(log n) |
| Appel récursif divisant en deux + travail linéaire | O(n log n) |

#### Boucles imbriquées à bornes dépendantes

```python
for i in range(n):
    for j in range(i):
        travail()          # exécuté 0 + 1 + 2 + ... + (n-1) fois
```

Le nombre d'exécutions vaut `0 + 1 + … + (n-1) = n(n-1)/2`, qui est en `Θ(n²)`. Contrairement à l'intuition, une boucle intérieure plus courte ne change pas la classe de complexité ici.

#### Pourquoi une boucle qui divise par deux est en O(log n)

Si la variable vaut `n` au départ et est divisée par 2 à chaque tour, après `k` tours elle vaut `n / 2^k`. La boucle s'arrête quand `n / 2^k < 1`, c'est-à-dire pour `k > log₂ n`. Il y a donc environ `log₂ n` itérations. Pour `n = 10⁹`, cela fait environ 30 tours.

**Règles de simplification.**

1. On **ignore les constantes multiplicatives** : `3n + 5` est « en `n` ».
2. On **garde le terme dominant** : `n² + n` est « en `n²` ».
3. Pour deux étapes successives, on **additionne** ; pour des étapes imbriquées, on **multiplie**.

### 2.3 Les notations asymptotiques

Ces notations décrivent la **croissance d'une fonction** `f(n)` quand `n` tend vers l'infini. Toutes les fonctions considérées sont à valeurs positives.

| Notation | Définition formelle | Lecture |
| --- | --- | --- |
| **O(g(n))** | Il existe `c > 0` et `n₀` tels que `f(n) ≤ c·g(n)` pour tout `n ≥ n₀` | `f` croît **au plus** aussi vite que `g` (borne supérieure) |
| **Ω(g(n))** | Il existe `c > 0` et `n₀` tels que `f(n) ≥ c·g(n)` pour tout `n ≥ n₀` | `f` croît **au moins** aussi vite que `g` (borne inférieure) |
| **Θ(g(n))** | `f` est à la fois `O(g)` et `Ω(g)` | `f` croît **exactement** comme `g` (borne serrée) |
| **o(g(n))** | `f(n)/g(n)` tend vers 0 | `f` croît **strictement moins vite** que `g` |
| **ω(g(n))** | `f(n)/g(n)` tend vers l'infini | `f` croît **strictement plus vite** que `g` |

#### Exemple de démonstration

Montrons que `3n² + 5n ∈ Θ(n²)`.

- Borne supérieure : pour `n ≥ 1`, `5n ≤ 5n²`, donc `3n² + 5n ≤ 8n²`. On prend `c = 8` et `n₀ = 1`.
- Borne inférieure : pour tout `n ≥ 1`, `3n² + 5n ≥ 3n²`. On prend `c = 3` et `n₀ = 1`.

Donc `3n² + 5n` est `Θ(n²)`. Il est aussi `O(n³)` et `O(2ⁿ)` (bornes supérieures de moins en moins précises), et `Ω(n)`, `Ω(1)` (bornes inférieures de moins en moins précises).

#### Critère pratique par la limite

Si `L = lim f(n)/g(n)` existe quand `n → ∞` :

- `L = 0` implique `f ∈ o(g)`, donc `f ∈ O(g)` ;
- `0 < L < ∞` implique `f ∈ Θ(g)` ;
- `L = ∞` implique `f ∈ ω(g)`, donc `f ∈ Ω(g)`.

#### Propriétés utiles

- **Transitivité** : `f ∈ O(g)` et `g ∈ O(h)` impliquent `f ∈ O(h)`.
- **Somme** : `O(f) + O(g) = O(max(f, g))`.
- **Produit** : `O(f) · O(g) = O(f · g)`.
- **Constantes** : `O(c·f) = O(f)`.
- **Logarithmes** : `log_a n` et `log_b n` diffèrent d'une constante, donc la base est sans importance.
- **Hiérarchie** : pour tout `k` et tout `ε > 0`, `(log n)^k ∈ o(n^ε)`, et `n^k ∈ o(2ⁿ)`.

#### Une idée reçue à éviter

> **Idée fausse** : « O désigne le pire cas, Ω le meilleur cas, Θ le cas moyen ».
>
> `O`, `Ω` et `Θ` sont des **bornes sur une fonction**, pas des « cas ». Les **cas** (pire, meilleur, moyen) sont **trois fonctions différentes** de `n`, et pour chacune on peut donner une borne `O`, `Ω` ou `Θ`.
>
> *Exemple (recherche linéaire)* : pire cas `T(n) = n`, qui est `Θ(n)` ; meilleur cas `T(n) = 1`, qui est `Θ(1)` ; cas moyen `T(n) ≈ n/2`, qui est `Θ(n)`. Dire « la recherche linéaire est en `O(n)` » est une garantie valable pour **tous** les cas.

### 2.4 Pire cas, meilleur cas, cas moyen

| Cas | Définition | Utilité |
| --- | --- | --- |
| **Pire cas** | Coût maximal sur toutes les entrées de taille `n` | Fournit des **garanties** de performance |
| **Meilleur cas** | Coût minimal | Rarement informatif |
| **Cas moyen** | Espérance du coût selon une distribution des entrées | Comportement typique, mais exige des hypothèses sur la distribution |

| Algorithme | Meilleur | Moyen | Pire |
| --- | --- | --- | --- |
| Recherche linéaire | Θ(1) | Θ(n) | Θ(n) |
| Recherche binaire | Θ(1) | Θ(log n) | Θ(log n) |
| Tri par insertion | Θ(n) | Θ(n²) | Θ(n²) |
| Quicksort | Θ(n log n) | Θ(n log n) | Θ(n²) |
| Tri fusion | Θ(n log n) | Θ(n log n) | Θ(n log n) |

Le **cas moyen** est lié à la notion d'**algorithme probabiliste** : quand l'algorithme choisit lui-même au hasard (pivot aléatoire), on parle de complexité **en espérance**, valable pour toute entrée, sans hypothèse sur la distribution des données.

### 2.5 Classes de complexité usuelles

| Classe | Nom | Exemple | Ordre de grandeur pour `n = 10⁶` |
| --- | --- | --- | --- |
| O(1) | Constante | Accès à un indice | 1 |
| O(log n) | Logarithmique | Recherche binaire | environ 20 |
| O(√n) | Racine carrée | Test de primalité naïf | 1 000 |
| O(n) | Linéaire | Parcours | 10⁶ |
| O(n log n) | Quasi-linéaire | Tris efficaces | 2 × 10⁷ |
| O(n²) | Quadratique | Deux boucles imbriquées | 10¹² (trop lent) |
| O(n³) | Cubique | Floyd-Warshall | trop lent |
| O(2ⁿ) | Exponentielle | Énumération des sous-ensembles | trop lent dès n ≈ 40 |
| O(n!) | Factorielle | Énumération des permutations | trop lent dès n ≈ 12 |

```text
Ordre de croissance :  1 < log n < √n < n < n log n < n² < n³ < 2ⁿ < n!
```

> **Règle pratique.** Un ordinateur moderne exécute environ 10⁸ opérations simples par seconde en langage compilé, et environ 10⁷ en Python pur. Cela permet d'estimer immédiatement si une solution passera dans le temps imparti.

### 2.6 Complexité en espace

On compte la mémoire **supplémentaire** utilisée par l'algorithme, sans compter l'entrée elle-même.

```python
def somme_liste(t):          # O(1) espace supplémentaire
    total = 0
    for x in t:
        total += x
    return total

def doubles(t):              # O(n) espace supplémentaire
    return [2 * x for x in t]
```

Il faut penser à la **pile d'appels** : une récursion de profondeur `n` consomme O(n) d'espace, même sans tableau explicite. En Python, la profondeur est limitée à environ 1000 par défaut.

### 2.7 Compromis temps et espace

On peut souvent gagner du temps en utilisant plus de mémoire, ou l'inverse.

| Technique | Gagne | Coûte |
| --- | --- | --- |
| Mémoïsation, programmation dynamique | Temps (évite les recalculs) | Mémoire |
| Table de hachage | Temps (recherche en O(1)) | Mémoire |
| Sommes préfixes | Temps de requête | Mémoire O(n) et précalcul |
| Calcul à la volée | Mémoire | Temps |

### 2.8 Analyse amortie

Le **coût amorti** d'une opération est le coût moyen **par opération sur une suite d'opérations**, calculé dans le **pire cas** de la suite. Cela diffère du cas moyen probabiliste : aucune hypothèse aléatoire n'est faite.

#### Exemple : le tableau dynamique (`list.append`)

Un tableau dynamique double sa capacité quand il est plein : l'insertion qui déclenche l'agrandissement coûte O(n) (copie), mais les suivantes coûtent O(1). Pour `n` insertions, les copies coûtent au total `1 + 2 + 4 + … + n < 2n`, donc le coût total est inférieur à `3n` : **O(1) amorti** par insertion.

Trois méthodes classiques justifient un coût amorti :

1. **Agrégat** : calculer le coût total de `n` opérations et diviser par `n`.
2. **Comptable** : faire « payer » à chaque opération bon marché un crédit qui financera les opérations coûteuses.
3. **Potentiel** : définir une fonction de potentiel sur l'état de la structure, qui augmente lors des opérations peu coûteuses et diminue lors des coûteuses.

Autres exemples : l'union-find avec compression de chemins (chapitre 19), l'insertion dans une table de hachage avec redimensionnement (chapitre 17), la file monotone (chapitre 13).

### 2.9 Récurrences

Les algorithmes récursifs s'analysent par une **relation de récurrence** sur le coût `T(n)`.

| Récurrence | Solution | Exemple |
| --- | --- | --- |
| `T(n) = T(n−1) + O(1)` | O(n) | Factorielle |
| `T(n) = T(n−1) + O(n)` | O(n²) | Tri par sélection récursif |
| `T(n) = T(n/2) + O(1)` | O(log n) | Recherche binaire |
| `T(n) = 2T(n/2) + O(n)` | O(n log n) | Tri fusion |
| `T(n) = 2T(n−1) + O(1)` | O(2ⁿ) | Tours de Hanoï, Fibonacci naïf |

Trois méthodes de résolution :

- **Dépliage** : développer `T(n)` en fonction de `T(n−1)`, `T(n−2)`… jusqu'au cas de base. Pour `T(n) = T(n−1) + 1`, on obtient `T(n) = T(0) + n`.
- **Arbre de récursion** : dessiner les appels niveau par niveau et sommer le travail de chaque niveau. Pour le tri fusion, il y a `log n` niveaux de coût `n` chacun.
- **Substitution** : deviner la forme de la solution et la vérifier par récurrence.

Le **théorème maître** (chapitre 9) donne directement la solution des récurrences de type diviser pour régner.

### 2.10 Une borne inférieure célèbre

Tout algorithme de tri **par comparaisons** exige `Ω(n log n)` comparaisons dans le pire cas. Justification : l'arbre de décision d'un tel algorithme possède au moins `n!` feuilles (une par permutation possible), donc une hauteur au moins `log₂(n!)`, qui est `Θ(n log n)` d'après la formule de Stirling. Cette borne prouve que le tri fusion est asymptotiquement optimal parmi les tris par comparaisons.

### 2.11 Conseils pratiques

- **Mesurer avant d'optimiser** (`timeit`, `cProfile`) : la complexité asymptotique ignore les constantes.
- Un algorithme en O(n log n) à grosse constante peut perdre contre un O(n²) sur de petites entrées ; c'est pourquoi Timsort utilise l'insertion sur de petits blocs.
- Attention aux **opérations cachées** : `x in liste` est O(n), `liste.insert(0, x)` est O(n), `s += "a"` en boucle peut être O(n²), les tranches `t[a:b]` copient leurs éléments.
- Vérifier l'**espace** : un tableau `n × n` pour `n = 10⁵` est impossible en mémoire.

```python
import timeit
print(timeit.timeit("sorted(t)", setup="import random; t=[random.random() for _ in range(10**5)]", number=10))
```

### 2.12 Pièges fréquents

- Croire que `O` désigne le pire cas, `Ω` le meilleur et `Θ` le cas moyen : ce sont des **bornes sur une fonction**, les cas étant trois fonctions distinctes.
- Oublier les **opérations cachées** : `x in liste`, `liste.insert(0, x)`, les tranches `t[a:b]` et la concaténation de chaînes en boucle coûtent plus que `O(1)`.
- Confondre la **taille de l'entrée** et sa **valeur** : un algorithme en `O(N)` est exponentiel en nombre de chiffres de `N`.
- Négliger les constantes : un `O(n log n)` à grosse constante peut perdre contre un `O(n²)` sur de petites entrées.
- Assimiler coût **amorti** et cas **moyen** : l'amorti est une garantie sur toute suite d'opérations, sans hypothèse probabiliste.

### Synthèse du chapitre 2

On mesure la **croissance du coût** en fonction de la taille de l'entrée, dans le modèle RAM, et non un temps en secondes. Retenez les définitions formelles de `O`, `Ω` et `Θ`, la hiérarchie `1 < log n < √n < n < n log n < n² < 2ⁿ < n!`, la distinction entre pire, meilleur et moyen, le coût **amorti** (tableau dynamique), les **récurrences** résolues par dépliage, arbre de récursion ou substitution, et la borne `Ω(n log n)` des tris par comparaisons.

---

## 3. Structures de données essentielles

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : distinguer structure de données et type abstrait ; connaître les coûts des opérations sur les tableaux, listes chaînées, piles, files, tables de hachage, tas et arbres ; utiliser `list`, `deque`, `dict`, `set` et `heapq` à bon escient ; implémenter une liste chaînée, un tas et un arbre binaire de recherche ; choisir la structure adaptée à un besoin.

Un algorithme manipule des données ; la **structure de données** choisie pour les organiser détermine le coût de chaque opération. Une même idée algorithmique peut passer de O(n²) à O(n log n) simplement en changeant de structure. Ce chapitre présente les structures indispensables, leur fonctionnement interne, leurs coûts et leurs usages.

### 3.1 Notions préalables

Une **structure de données** est une manière d'organiser des données en mémoire, accompagnée des **opérations** autorisées sur elles (accès, recherche, insertion, suppression, parcours). Un **type abstrait de données** (TAD) décrit **ce que** font les opérations (l'interface) sans dire **comment** elles sont réalisées (l'implémentation). Par exemple, le TAD *pile* peut être implémenté par un tableau ou par une liste chaînée.

Deux grandes familles d'implémentation s'opposent :

- **Contiguë** : les éléments sont côte à côte en mémoire (tableau). L'accès par indice est immédiat, mais l'insertion au milieu oblige à décaler.
- **Chaînée** : chaque élément contient un lien vers le suivant. L'insertion est locale, mais l'accès par indice exige de parcourir la chaîne.

### 3.2 Aperçu des complexités

| Structure | Accès | Recherche | Insertion | Suppression | Remarques |
| --- | --- | --- | --- | --- | --- |
| Tableau, `list` | O(1) | O(n) | O(1) amorti en fin, O(n) ailleurs | O(n) | Contigu en mémoire, très bon pour le cache |
| Liste chaînée | O(n) | O(n) | O(1) en tête ou avec nœud connu | O(1) avec nœud connu | Pas d'accès direct |
| Pile (LIFO) | sommet seulement |  | O(1) | O(1) | `list.append` et `pop` |
| File (FIFO) | tête seulement |  | O(1) | O(1) | `collections.deque` |
| Table de hachage (`dict`, `set`) |  | O(1) en moyenne | O(1) en moyenne | O(1) en moyenne | Pas d'ordre de tri |
| Tas (*heap*) | min ou max en O(1) | O(n) | O(log n) | O(log n) | `heapq` |
| Arbre binaire de recherche équilibré |  | O(log n) | O(log n) | O(log n) | Non natif en Python (`sortedcontainers`) |
| Graphe |  |  |  |  | Listes d'adjacence (chapitre 19) |

### 3.3 Tableaux et listes Python

La `list` de Python est un **tableau dynamique** : un bloc contigu de références, agrandi par un facteur constant quand il est plein (d'où le O(1) amorti de `append`, voir 2.8).

| Opération | Coût | Commentaire |
| --- | --- | --- |
| `t[i]` | O(1) | Adresse calculée directement |
| `t.append(x)` | O(1) amorti |  |
| `t.pop()` | O(1) | Retire le dernier |
| `t.pop(0)`, `t.insert(0, x)` | O(n) | Tous les éléments sont décalés |
| `x in t` | O(n) | Parcours séquentiel |
| `t[a:b]` | O(b - a) | **Copie** de la tranche |
| `t.sort()` | O(n log n) | Timsort |
| `len(t)` | O(1) | Longueur stockée |

Une erreur classique concerne la création de tableaux à deux dimensions :

```python
grille_fausse = [[0] * 3] * 3      # trois fois LA MÊME ligne (même objet)
grille_fausse[0][0] = 1
print(grille_fausse)               # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

grille = [[0] * 3 for _ in range(3)]   # trois lignes indépendantes
grille[0][0] = 1
print(grille)                      # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

### 3.4 Piles, files et files à double entrée

Une **pile** (*stack*) suit la règle **dernier entré, premier sorti** (LIFO) : on empile et on dépile du même côté. Usages : pile d'appels, annulation (*undo*), vérification de parenthèses, parcours en profondeur, évaluation d'expressions.

Une **file** (*queue*) suit la règle **premier entré, premier sorti** (FIFO) : on ajoute d'un côté, on retire de l'autre. Usages : parcours en largeur, ordonnancement de tâches, tampons.

Une **deque** (file à double entrée) autorise l'ajout et le retrait aux deux extrémités en O(1).

```python
from collections import deque

pile = []
pile.append(1); pile.append(2)
print(pile.pop())                # 2 (dernier entré, premier sorti)

file = deque()
file.append(1); file.append(2)
print(file.popleft())            # 1 (premier entré, premier sorti), en O(1)
# Attention : list.pop(0) est en O(n) ; utiliser deque pour une file.
```

**Application : parenthèses bien formées.** On empile chaque ouvrante ; à chaque fermante, la sommet de la pile doit être l'ouvrante correspondante.

```python
def bien_parenthese(s):
    paires = {')': '(', ']': '[', '}': '{'}
    pile = []
    for c in s:
        if c in '([{':
            pile.append(c)
        elif c in paires:
            if not pile or pile.pop() != paires[c]:
                return False
    return not pile            # la pile doit être vide à la fin

print(bien_parenthese("{[()]}"), bien_parenthese("([)]"))   # True False
```

### 3.5 Listes chaînées

Une **liste chaînée** est une suite de **nœuds** ; chaque nœud contient une valeur et une référence vers le nœud suivant (liste **simplement chaînée**), et éventuellement vers le précédent (liste **doublement chaînée**). On conserve la **tête** (premier nœud).

Avantages : insertion et suppression en O(1) quand on dispose du nœud ; pas de redimensionnement. Inconvénients : pas d'accès direct, mauvaise localité mémoire, surcoût de mémoire par nœud.

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

# 1 -> 2 -> 3 devient 3 -> 2 -> 1
tete = Noeud(1, Noeud(2, Noeud(3)))
tete = inverser(tete)
valeurs = []
while tete:
    valeurs.append(tete.valeur)
    tete = tete.suivant
print(valeurs)                   # [3, 2, 1]
```

L'inversion fonctionne par une boucle à trois variables : à chaque tour, on retourne le lien du nœud courant vers le précédent. Complexité O(n) en temps et O(1) en espace.

### 3.6 Tables de hachage (aperçu)

Un `dict` ou un `set` Python offre insertion, recherche et suppression en **O(1) en moyenne**. Le principe (fonction de hachage, collisions) est détaillé au chapitre 17. Retenir pour l'instant : pour tester une appartenance ou compter, un `set` ou un `dict` remplace une recherche linéaire coûteuse.

### 3.7 Tas et files de priorité

Une **file de priorité** est un TAD qui permet d'insérer des éléments et d'extraire à chaque fois celui de **plus haute priorité**. Le **tas binaire** en est l'implémentation standard.

#### Définition d'un tas binaire

Un **tas-min** est un arbre binaire **complet** (tous les niveaux sont pleins sauf éventuellement le dernier, rempli de gauche à droite) vérifiant la **propriété de tas** : la valeur de chaque nœud est inférieure ou égale à celles de ses enfants. Le minimum est donc à la racine.

Grâce à sa forme complète, un tas se stocke dans un **tableau** : le nœud d'indice `i` a pour enfants `2i+1` et `2i+2`, et pour parent `(i-1)//2`.

#### Opérations

- **Insertion** : ajouter à la fin, puis **remonter** l'élément en l'échangeant avec son parent tant qu'il est plus petit. Coût O(log n), car la hauteur est `log n`.
- **Extraction du minimum** : remplacer la racine par le dernier élément, puis le **descendre** en l'échangeant avec le plus petit de ses enfants. Coût O(log n).
- **Construction** (`heapify`) : en O(n) en descendant les nœuds internes depuis le bas, et non O(n log n) comme `n` insertions successives.

```python
import heapq

tas = []
for x in [5, 1, 8, 3]:
    heapq.heappush(tas, x)
print(heapq.heappop(tas))        # 1 (le plus petit)

liste = [9, 4, 7, 1, 8]
heapq.heapify(liste)             # transforme la liste en tas, en O(n)
print(liste[0])                  # 1 : le minimum est toujours en tête
print(heapq.nsmallest(3, [9, 4, 7, 1, 8]))    # [1, 4, 7]

taches = []                      # file de priorité avec des tuples (priorité, élément)
heapq.heappush(taches, (2, "écrire"))
heapq.heappush(taches, (1, "lire"))
print(heapq.heappop(taches))     # (1, 'lire')

tas_max = []                     # astuce du tas-max : stocker l'opposé
for x in [5, 1, 8, 3]:
    heapq.heappush(tas_max, -x)
print(-heapq.heappop(tas_max))   # 8 (le plus grand)
```

Usages : Dijkstra, Prim, tri par tas, fusion de listes triées, « k plus grands éléments », simulation d'événements. Avec des tuples, si deux priorités sont égales, Python compare l'élément suivant du tuple : il faut parfois insérer un compteur pour éviter de comparer des objets non comparables.

### 3.8 Arbres

Un **arbre** est une structure hiérarchique : une **racine**, et des **nœuds** ayant chacun des **enfants**. Vocabulaire : **feuille** (nœud sans enfant), **hauteur** (longueur du plus long chemin de la racine à une feuille), **profondeur** d'un nœud (distance à la racine), **sous-arbre**. Un **arbre binaire** a au plus deux enfants par nœud (gauche et droit).

```python
class NoeudArbre:
    def __init__(self, valeur):
        self.valeur, self.gauche, self.droite = valeur, None, None

def parcours_infixe(n):                    # gauche, racine, droite
    if n:
        yield from parcours_infixe(n.gauche)
        yield n.valeur
        yield from parcours_infixe(n.droite)

racine = NoeudArbre(4)
racine.gauche, racine.droite = NoeudArbre(2), NoeudArbre(6)
print(list(parcours_infixe(racine)))       # [2, 4, 6]
```

#### Les quatre parcours

| Parcours | Ordre de visite | Usage typique |
| --- | --- | --- |
| **Préfixe** | racine, gauche, droite | Copier un arbre, sérialiser |
| **Infixe** | gauche, racine, droite | Obtenir les valeurs triées d'un ABR |
| **Suffixe** | gauche, droite, racine | Supprimer un arbre, évaluer une expression |
| **En largeur** | niveau par niveau (avec une file) | Distances à la racine |

#### Arbre binaire de recherche (ABR)

Un **ABR** vérifie, pour chaque nœud : toutes les valeurs du sous-arbre gauche sont **strictement inférieures** à la sienne, toutes celles du sous-arbre droit sont **supérieures**. La recherche, l'insertion et la suppression coûtent **O(h)**, où `h` est la hauteur.

- Si l'arbre est **équilibré**, `h = O(log n)` : c'est le cas des **arbres AVL** et **rouge-noir**, qui se rééquilibrent par rotations.
- Si l'arbre est **dégénéré** (insertion de valeurs déjà triées), `h = O(n)` et l'ABR devient une liste chaînée.

### 3.9 Ensembles et dictionnaires triés

Quand on a besoin de données triées **avec insertions et suppressions fréquentes**, la liste triée avec `bisect.insort` coûte O(n) par insertion (décalage). Pour de gros volumes, on utilise un arbre équilibré (bibliothèque `sortedcontainers` en Python, `std::set` et `std::map` en C++, `TreeMap` en Java).

### 3.10 Choisir la bonne structure

| Besoin | Structure |
| --- | --- |
| Accès par indice | `list` |
| Appartenance ou comptage rapide | `set`, `dict`, `Counter` |
| Dernier entré, premier sorti | pile (`list`) |
| Premier entré, premier sorti, parcours en largeur | `deque` |
| Toujours extraire le minimum ou le maximum | `heapq` |
| Données triées avec insertions | `bisect.insort` (petit `n`) ou arbre équilibré |
| Union et appartenance à un groupe | Union-Find (chapitre 19) |
| Préfixes de chaînes | Trie (chapitre 24) |

### 3.11 Pièges fréquents

- Utiliser `list.pop(0)` ou `insert(0, x)` comme une file : chaque appel est en `O(n)` ; préférer `collections.deque`.
- Créer une grille avec `[[0] * n] * n` : toutes les lignes sont **le même objet** ; utiliser une compréhension de liste.
- Utiliser une `list` ou un `dict` comme **clé** de dictionnaire : seuls les objets immuables (hachables) conviennent.
- Croire qu'un arbre binaire de recherche est toujours en `O(log n)` : sans rééquilibrage, des insertions triées le font dégénérer en liste (`O(n)`).
- Oublier que `heapq` est un tas-**min** et que les tuples `(priorité, objet)` comparent l'objet en cas d'égalité de priorité.

### Synthèse du chapitre 3

Le choix de la **structure de données** détermine le coût de chaque opération et donc la complexité de l'algorithme. Retenez : tableau (accès `O(1)`), `deque` (file en `O(1)`), `dict` et `set` (opérations en `O(1)` en moyenne), **tas** (minimum en `O(1)`, insertion et extraction en `O(log n)`), **ABR équilibré** (`O(log n)`), liste chaînée (insertion locale en `O(1)`), ainsi que la table de choix en fin de chapitre.

---

## 4. Récursivité de base

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : définir une fonction récursive et ses trois éléments (cas de base, appel sur un problème plus petit, combinaison) ; suivre l'évolution de la pile d'appels ; prouver la correction par récurrence et la terminaison par décroissance de la taille ; reconnaître les types de récursion (linéaire, binaire, terminale, mutuelle) ; corriger une récursion exponentielle par mémoïsation ; choisir entre récursivité et itération.

### 4.1 Qu'est-ce que la récursivité ?

Une fonction est **récursive** quand elle **s'appelle elle-même**, directement ou indirectement, pour résoudre une version **plus petite** du même problème. C'est la traduction informatique du raisonnement par récurrence en mathématiques.

> **Analogie.** Des poupées russes : pour ouvrir la première, on ouvre une poupée plus petite, et ainsi de suite jusqu'à la plus petite, qui ne contient plus rien.

```python
def factorielle(n):
    if n <= 1:                       # 1. cas de base : arrête la récursion
        return 1
    return n * factorielle(n - 1)    # 2. cas récursif : problème plus petit

print(factorielle(5))   # 120
```

La définition mathématique correspondante est `0! = 1` et `n! = n × (n-1)!` pour `n ≥ 1`. La récursivité permet d'écrire presque mot pour mot une définition inductive.

### 4.2 Structure d'une fonction récursive

Toute fonction récursive correcte possède trois éléments :

1. **Cas de base** : la situation la plus simple, résolue directement, sans appel récursif. Il en faut au moins un.
2. **Appel récursif** sur un problème **strictement plus petit**, de façon à converger vers un cas de base.
3. **Combinaison** des résultats des appels pour construire le résultat du problème courant.

**Preuve de correction par récurrence.** On montre que la fonction est correcte sur les cas de base, puis que, si elle est correcte sur les problèmes plus petits (hypothèse de récurrence), elle l'est sur le problème courant. Pour `factorielle` : correcte pour `n ≤ 1` ; si `factorielle(n-1) = (n-1)!`, alors `factorielle(n) = n × (n-1)! = n!`.

**Preuve de terminaison.** La taille (ici `n`) décroît strictement à chaque appel et ne peut pas descendre indéfiniment sous le cas de base.

### 4.3 Fonctionnement : la pile d'appels

Chaque appel de fonction crée un **cadre d'exécution** (paramètres, variables locales, point de retour) empilé dans la **pile d'appels**. Quand un appel se termine, son cadre est dépilé et le résultat remonte à l'appelant.

```text
factorielle(3)
  attend 3 * factorielle(2)
      attend 2 * factorielle(1)
          renvoie 1            (cas de base)
      renvoie 2 * 1 = 2
  renvoie 3 * 2 = 6
```

Il y a donc deux phases : une **phase de descente** (les appels s'empilent) et une **phase de remontée** (les résultats se combinent). La mémoire occupée est proportionnelle à la **profondeur maximale** de récursion.

### 4.4 Erreurs courantes

| Erreur | Conséquence |
| --- | --- |
| **Absence de cas de base** | Récursion infinie, `RecursionError` en Python |
| **Le problème ne diminue pas** (appel sur la même taille) | Idem |
| **Cas de base inatteignable** (par exemple `n` négatif avec test `n == 0`) | Idem |
| **Recalculs inutiles** (Fibonacci naïf) | Complexité exponentielle |
| **Profondeur trop grande** | Dépassement de pile (limite Python : environ 1000) |
| **Oublier de renvoyer le résultat de l'appel** | La fonction renvoie `None` |

```python
import sys
sys.setrecursionlimit(10**6)        # possible mais risqué : préférer une version itérative
```

### 4.5 Exemples classiques

```python
def somme(t, i=0):                           # somme d'une liste
    return 0 if i == len(t) else t[i] + somme(t, i + 1)

def inverser_chaine(s):
    return s if len(s) <= 1 else inverser_chaine(s[1:]) + s[0]

def est_palindrome(s):
    return len(s) < 2 or (s[0] == s[-1] and est_palindrome(s[1:-1]))

def puissance(x, n):                          # exponentiation rapide : O(log n)
    if n == 0:
        return 1
    moitie = puissance(x, n // 2)
    return moitie * moitie * (x if n % 2 else 1)

def hanoi(n, source, cible, aide):            # O(2^n)
    if n == 0:
        return
    hanoi(n - 1, source, aide, cible)
    print(f"Déplacer le disque {n} : {source} -> {cible}")
    hanoi(n - 1, aide, cible, source)

def fib(n):                                   # O(2^n) : à ne pas utiliser tel quel
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(somme([1, 2, 3]), inverser_chaine("abc"), est_palindrome("kayak"), puissance(2, 10))   # 6 cba True 1024
hanoi(2, "A", "C", "B")                       # 3 déplacements
print(fib(10))                                # 55
```

#### Analyse de l'exponentiation rapide

L'idée est que `x^n = (x^(n/2))²` si `n` est pair, et `x × (x^((n-1)/2))²` sinon. On ne calcule la puissance de la moitié **qu'une seule fois** (variable `moitie`), d'où la récurrence `T(n) = T(n/2) + O(1)` et la complexité **O(log n)**, contre O(n) pour la méthode naïve. Cette idée est centrale en arithmétique modulaire (chapitre 16).

#### Analyse des tours de Hanoï

Pour déplacer `n` disques, on déplace `n-1` disques, puis le plus grand, puis de nouveau `n-1` disques : `T(n) = 2T(n-1) + 1`, dont la solution est `T(n) = 2^n - 1`. Ce nombre de déplacements est **optimal** : la complexité exponentielle est inhérente au problème, pas à l'algorithme.

#### Corriger Fibonacci : la mémoïsation

L'arbre d'appels de `fib(n)` recalcule les mêmes valeurs un nombre exponentiel de fois (`fib(n-2)` est calculé dans `fib(n)` et dans `fib(n-1)`). La **mémoïsation** consiste à stocker chaque résultat dès qu'il est calculé.

```python
from functools import cache

@cache                                         # Python 3.9 et ultérieur
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
# O(n) en temps et en espace
```

C'est le point de départ de la **programmation dynamique** (chapitre 18).

### 4.6 Les différents types de récursion

| Type | Description | Exemple |
| --- | --- | --- |
| **Linéaire** | Un seul appel récursif par exécution | Factorielle, somme |
| **Binaire (ou multiple)** | Plusieurs appels par exécution | Fibonacci, tri fusion |
| **Terminale** | L'appel récursif est la **dernière** opération (rien à faire au retour) | `pgcd(a, b)` récursif |
| **Mutuelle** | Deux fonctions s'appellent l'une l'autre | `est_pair` et `est_impair` |
| **Imbriquée** | Un appel dans les arguments d'un appel | Fonction d'Ackermann |

Python **n'optimise pas la récursion terminale** : même une récursion terminale consomme de la pile. D'autres langages (Scheme, certains compilateurs C ou Scala) transforment ces appels en boucles.

### 4.7 Récursivité ou itération ?

Toute fonction récursive peut s'écrire de façon itérative, en gérant soi-même une **pile explicite**.

|  | Récursivité | Itération |
| --- | --- | --- |
| Lisibilité | Très naturelle pour les arbres et diviser pour régner | Parfois plus lourde |
| Mémoire | O(profondeur) | O(1) souvent |
| Vitesse | Surcoût des appels | Plus rapide |
| Limite | Profondeur de la pile | Aucune |

```python
def factorielle_iterative(n):          # même résultat, sans pile d'appels
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r
```

### 4.8 Quand utiliser la récursivité ?

- Structures **récursives par nature** : arbres, graphes, listes chaînées, expressions imbriquées.
- Algorithmes **diviser pour régner** (chapitre 9).
- **Retour sur trace** (chapitre 11).
- **Programmation dynamique** descendante (chapitre 18).

À éviter quand la profondeur peut atteindre des dizaines de milliers d'appels en Python, ou quand la version itérative est tout aussi claire.

### 4.9 Pièges fréquents

- Oublier le **cas de base**, ou écrire un cas de base inatteignable : récursion infinie et `RecursionError`.
- Appeler la fonction sur un problème **qui ne diminue pas** (même taille, ou `n` négatif avec un test `n == 0`).
- Oublier de **renvoyer** le résultat de l'appel récursif : la fonction renvoie `None`.
- Laisser des **recalculs** exponentiels (Fibonacci naïf) au lieu de mémoïser.
- Dépasser la **limite de profondeur** de Python (environ 1000) : préférer une version itérative ou une pile explicite.

### Synthèse du chapitre 4

Une fonction **récursive** s'appelle elle-même sur un problème plus petit, avec un **cas de base** qui arrête la descente et une **combinaison** des résultats. Retenez la **pile d'appels** (mémoire proportionnelle à la profondeur), la preuve par récurrence, l'exponentiation rapide en `O(log n)`, les tours de Hanoï en `2ⁿ - 1` déplacements, la **mémoïsation** (`functools.cache`) qui prépare la programmation dynamique, et le fait que Python n'optimise pas la récursion terminale.

---

## 5. Algorithmes de tri simples

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : définir le problème du tri et ses propriétés (en place, stable, par comparaisons, adaptatif) ; compter les inversions ; écrire et analyser les tris à bulles, par sélection et par insertion ; comparer leurs complexités ; trier avec une clé et un ordre personnalisé en Python.

### 5.1 Introduction au problème du tri

**Trier** une séquence consiste à réordonner ses éléments selon une **relation d'ordre** (croissant, décroissant, selon une clé). Le tri est l'un des problèmes les plus étudiés de l'informatique, car il facilite ensuite la recherche, la détection de doublons, la fusion et de nombreux autres traitements.

**Spécification.** Entrée : une suite `(a₁, …, aₙ)`. Sortie : une permutation `(b₁, …, bₙ)` de cette suite telle que `b₁ ≤ b₂ ≤ … ≤ bₙ`. La sortie doit donc être **triée** et être **une permutation** de l'entrée (on ne perd ni n'invente d'éléments).

#### Propriétés d'un tri

- **En place** (*in-place*) : le tri n'utilise qu'une mémoire supplémentaire O(1) (ou O(log n) pour la pile de récursion) en plus du tableau.
- **Stable** : deux éléments égaux (au sens de la clé) conservent leur ordre relatif initial. La stabilité est précieuse pour les tris successifs sur plusieurs critères : si on trie d'abord par nom puis, de façon stable, par âge, les personnes de même âge restent classées par nom.
- **Par comparaisons** : le tri ne s'appuie que sur des comparaisons entre éléments. Il est alors soumis à la borne inférieure `Ω(n log n)` (voir 2.10).
- **Adaptatif** : le tri est plus rapide sur une entrée déjà presque triée.

#### Notions : inversions

Une **inversion** est une paire d'indices `i < j` telle que `t[i] > t[j]`. Un tableau trié a 0 inversion ; un tableau trié à l'envers en a `n(n-1)/2`. Les tris simples échangeant des voisins ne suppriment qu'**une** inversion par échange : ils exigent donc de l'ordre de `n²` échanges dans le pire cas, ce qui explique leur complexité quadratique.

### 5.2 Tri à bulles (*Bubble Sort*)

**Principe.** On parcourt le tableau en comparant les voisins `t[j]` et `t[j+1]` ; s'ils sont mal ordonnés, on les échange. À l'issue de la première passe, le **plus grand élément** a « remonté » comme une bulle jusqu'à la dernière case. À l'issue de la `i`-ième passe, les `i` plus grands éléments sont à leur place définitive.

```python
def tri_bulles(t):
    n = len(t)
    for i in range(n - 1):
        echange = False
        for j in range(n - 1 - i):        # la fin du tableau est déjà triée
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]
                echange = True
        if not echange:                   # aucun échange : tableau trié, arrêt anticipé
            break
    return t

print(tri_bulles([5, 2, 9, 1]))          # [1, 2, 5, 9]
```

**Invariant.** Après la passe `i`, les `i+1` derniers éléments sont les plus grands du tableau, rangés dans l'ordre.

**Complexité.** Pire et moyen : `O(n²)` comparaisons. Meilleur cas (tableau déjà trié, grâce au drapeau `echange`) : `O(n)`. Espace `O(1)`. Le tri est **stable**, car on n'échange que si `t[j] > t[j+1]` strictement. Il est très lent en pratique et réservé à l'enseignement.

### 5.3 Tri par sélection (*Selection Sort*)

**Principe.** À l'étape `i`, on cherche le **minimum** dans la partie non triée `t[i:]` et on l'échange avec `t[i]`. La partie gauche `t[:i]` est alors constituée des `i` plus petits éléments, dans l'ordre.

```python
def tri_selection(t):
    for i in range(len(t)):
        m = min(range(i, len(t)), key=t.__getitem__)    # indice du minimum de t[i:]
        t[i], t[m] = t[m], t[i]
    return t

print(tri_selection([5, 2, 9, 1]))        # [1, 2, 5, 9]
```

**Complexité.** `Θ(n²)` comparaisons **dans tous les cas** (la recherche du minimum parcourt toujours tout le reste), mais seulement `n - 1` échanges au plus. Espace `O(1)`. Le tri est **non stable** : l'échange à longue distance peut faire passer un élément égal devant un autre (exemple : `[2a, 2b, 1]` devient `[1, 2b, 2a]`). Utile quand les écritures sont coûteuses.

### 5.4 Tri par insertion (*Insertion Sort*)

**Principe.** Comme pour trier des cartes à jouer en main : on maintient une partie gauche **déjà triée** `t[:i]` ; on prend l'élément suivant `t[i]` (la **clé**) et on l'**insère** à sa place en décalant vers la droite les éléments plus grands.

```python
def tri_insertion(t):
    for i in range(1, len(t)):
        cle = t[i]
        j = i - 1
        while j >= 0 and t[j] > cle:      # décaler les éléments plus grands
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = cle                    # placer la clé
    return t

print(tri_insertion([5, 2, 9, 1]))        # [1, 2, 5, 9]
```

**Invariant.** Au début de l'itération `i`, `t[:i]` contient les `i` premiers éléments de l'entrée, triés.

**Complexité.** Le nombre de décalages est égal au nombre d'**inversions** du tableau. Pire cas (tableau décroissant) : `Θ(n²)`. Cas moyen : `Θ(n²)`. Meilleur cas (déjà trié) : `Θ(n)`. En général `Θ(n + I)` où `I` est le nombre d'inversions, d'où son caractère **adaptatif**. Espace `O(1)`, **stable** (le test est strict). Il est excellent sur les petits tableaux (moins de 20 éléments environ) et les tableaux presque triés, et sert de brique dans les tris hybrides comme Timsort.

### 5.5 Comparaison

| Tri | Meilleur | Moyen | Pire | Espace | Stable | Remarque |
| --- | --- | --- | --- | --- | --- | --- |
| **Bulles** | O(n) | O(n²) | O(n²) | O(1) | Oui | Pédagogique uniquement |
| **Sélection** | O(n²) | O(n²) | O(n²) | O(1) | Non | Au plus n-1 échanges |
| **Insertion** | O(n) | O(n²) | O(n²) | O(1) | Oui | Rapide sur petits ou presque triés |

> **En pratique**, on utilise `sorted(t)` ou `t.sort()` (Timsort, stable, `O(n log n)` au pire, `O(n)` si déjà trié). Les tris efficaces sont vus au chapitre 8.

### 5.6 Tri avec clé et ordre personnalisé

```python
livres = [("Zola", 1885), ("Hugo", 1862), ("Balzac", 1835)]
print(sorted(livres, key=lambda l: l[1]))                # par année
print(sorted(livres, key=lambda l: l[0], reverse=True))  # par auteur décroissant
```

L'argument `key` calcule **une fois par élément** la valeur de comparaison, ce qui est plus efficace qu'une fonction de comparaison appelée à chaque test.

### 5.7 Pièges fréquents

- Confondre **stable** et **en place** : ce sont deux propriétés indépendantes (la sélection est en place mais non stable).
- Utiliser un test `>=` à la place de `>` dans l'insertion ou les bulles : le tri perd sa **stabilité**.
- Oublier le drapeau d'arrêt anticipé du tri à bulles, et donc son meilleur cas en `O(n)`.
- Écrire à la main un tri quadratique en production alors que `sorted()` (Timsort) est disponible.

### Synthèse du chapitre 5

Les trois **tris simples** sont quadratiques dans le pire cas : bulles et insertion sont stables, la sélection ne l'est pas et n'effectue que `n - 1` échanges. Le tri par **insertion** est le plus utile (adaptatif, en `Θ(n + I)` avec `I` le nombre d'**inversions**) et sert de brique aux tris hybrides. Retenez la notion d'inversion et l'usage de `key` dans `sorted()`.

---

## 6. Algorithmes de recherche

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : spécifier le problème de la recherche ; écrire et analyser la recherche linéaire et la recherche binaire ; démontrer la correction de la dichotomie par invariant ; utiliser `bisect_left` et `bisect_right` ; connaître les variantes (interpolation, exponentielle, tableau tourné, matrice triée) ; choisir la méthode selon l'organisation des données.

### 6.1 Le problème de la recherche

**Spécification.** Entrée : une collection d'éléments et une **cible**. Sortie : la **position** de la cible dans la collection, ou une valeur sentinelle (par exemple -1) si elle est absente.

Le coût de la recherche dépend de l'organisation des données : sur des données non ordonnées, il faut tout examiner ; sur des données **triées**, on peut éliminer de grandes zones d'un coup.

### 6.2 Recherche linéaire (séquentielle)

On parcourt les éléments un par un jusqu'à trouver la cible. Elle fonctionne sur **toute** liste, triée ou non, et sur toute structure parcourable.

```python
def recherche_lineaire(t, cible):
    for i, x in enumerate(t):
        if x == cible:
            return i
    return -1

print(recherche_lineaire([4, 8, 15], 15), recherche_lineaire([4, 8, 15], 3))   # 2 -1
```

**Complexité.** Pire cas (cible en dernière position ou absente) : `n` comparaisons, soit `Θ(n)`. Meilleur cas : 1 comparaison. Cas moyen, si la cible est présente et équiprobable à chaque position : `(n+1)/2` comparaisons. Espace `O(1)`.

### 6.3 Recherche binaire (dichotomique)

#### Principe

Sur une liste **triée**, on compare la cible avec l'élément du **milieu**. Selon le résultat, on élimine la moitié gauche ou la moitié droite, puis on recommence sur la moitié restante.

#### Algorithme

```python
def recherche_binaire(t, cible):
    bas, haut = 0, len(t) - 1
    while bas <= haut:
        milieu = bas + (haut - bas) // 2      # évite le dépassement d'entier dans d'autres langages
        if t[milieu] == cible:
            return milieu
        if t[milieu] < cible:
            bas = milieu + 1
        else:
            haut = milieu - 1
    return -1

print(recherche_binaire([1, 3, 5, 7, 9, 11], 7))   # 3
```

#### Preuve de correction

**Invariant** : si la cible est présente dans le tableau, elle se trouve dans `t[bas..haut]`.

- Initialisation : `bas = 0` et `haut = n-1` couvrent tout le tableau.
- Conservation : si `t[milieu] < cible`, alors, le tableau étant trié, la cible ne peut pas être en position `≤ milieu` ; on passe à `bas = milieu + 1`, et l'invariant reste vrai. Raisonnement symétrique sinon.
- Terminaison : la longueur `haut - bas + 1` de l'intervalle **décroît strictement** à chaque tour (elle est au moins divisée par 2, et le milieu est exclu). Quand l'intervalle est vide, la cible n'est pas là.

#### Complexité

Chaque tour divise la taille par deux : `T(n) = T(n/2) + O(1)`, donc `O(log n)`. Un milliard d'éléments exigent environ 30 comparaisons (`2³⁰ ≈ 10⁹`). Espace `O(1)` pour la version itérative.

#### Variantes : première position, dernière position, insertion

```python
from bisect import bisect_left, bisect_right, insort

t = [1, 2, 2, 2, 3]
print(bisect_left(t, 2))                          # 1 : première position de 2 (ou point d'insertion)
print(bisect_right(t, 2))                         # 4 : position après le dernier 2
print(bisect_right(t, 2) - bisect_left(t, 2))     # 3 : nombre d'occurrences
insort(t, 2)                                      # insère en gardant la liste triée (O(n) : décalage)
print(t)                                          # [1, 2, 2, 2, 2, 3]
```

`bisect_left(t, x)` renvoie le plus petit indice `i` tel que tous les éléments avant `i` sont `< x` ; `bisect_right(t, x)` renvoie le plus petit indice tel que tous les éléments avant sont `<= x`. Ces fonctions sont en `O(log n)`.

#### Pièges classiques

| Piège | Conséquence |
| --- | --- |
| `bas = milieu` au lieu de `milieu + 1` | Boucle infinie |
| Condition `bas < haut` au lieu de `bas <= haut` | Oubli d'un cas (intervalle d'un seul élément) |
| Calcul `(bas + haut) // 2` avec des entiers bornés (C, Java) | Dépassement d'entier ; préférer `bas + (haut - bas) // 2` |
| Liste non triée | Résultat faux, sans erreur signalée |
| Doublons | La version simple renvoie un indice quelconque parmi les égaux |

### 6.4 Autres recherches

- **Recherche par interpolation** : au lieu de viser le milieu, on estime la position de la cible par proportion entre les valeurs extrêmes. En moyenne `O(log log n)` sur des données uniformément réparties, mais `O(n)` au pire.
- **Recherche exponentielle** : on double un pas jusqu'à dépasser la cible, puis recherche binaire dans le dernier intervalle ; utile quand la taille est inconnue ou la cible proche du début.
- **Recherche dans un tableau tourné** : tableau trié puis décalé circulairement ; une recherche binaire adaptée reste en `O(log n)`.
- **Recherche dans une matrice triée** : partir du coin supérieur droit et éliminer une ligne ou une colonne à chaque étape, en `O(m + n)`.

### 6.5 Comparaison

|  | Linéaire | Binaire |
| --- | --- | --- |
| Pré-requis | Aucun | **Liste triée** et accès direct par indice |
| Temps | O(n) | **O(log n)** |
| Quand l'utiliser | Petite liste, recherche unique | Nombreuses recherches sur des données triées |

Pour des appartenances fréquentes sur des données non ordonnées, un `set` ou un `dict` (O(1) en moyenne) est encore plus efficace. Le coût de tri préalable (`O(n log n)`) n'est amorti qu'à partir d'un certain nombre de recherches, environ `log n`.

### 6.6 Pièges fréquents

- Appliquer la recherche binaire à une liste **non triée** : le résultat est faux, sans erreur signalée.
- Écrire `bas = milieu` au lieu de `milieu + 1` : **boucle infinie**.
- Utiliser la condition `bas < haut` à la place de `bas <= haut` : l'intervalle d'un seul élément n'est plus examiné.
- Calculer `(bas + haut) // 2` avec des entiers bornés (C, Java) : risque de **dépassement** ; préférer `bas + (haut - bas) // 2`.
- Oublier que, avec des doublons, la version simple renvoie un indice **quelconque** parmi les égaux.

### Synthèse du chapitre 6

La **recherche linéaire** fonctionne partout mais coûte `O(n)`. La **recherche binaire** exige un tableau trié accessible par indice et élimine la moitié des candidats à chaque étape, pour `O(log n)` comparaisons, ce que démontre l'invariant « si la cible est présente, elle est dans `t[bas..haut]` ». Retenez `bisect_left` et `bisect_right` pour les doublons et les points d'insertion, ainsi que la généralisation de la dichotomie aux fonctions monotones (chapitre 15).

---

## 7. Algorithmes mathématiques de base

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : calculer un PGCD et un PPCM par l'algorithme d'Euclide et justifier sa correction ; tester la primalité par divisions jusqu'à `√n` ; calculer une factorielle et en mesurer la croissance ; comparer les méthodes de calcul de Fibonacci (naïve, mémoïsée, itérative, par doublement) ; utiliser les outils mathématiques de Python et les opérations sur les bits.

### 7.1 Plus grand commun diviseur (algorithme d'Euclide)

#### Définitions

Le **PGCD** de deux entiers `a` et `b` (non tous deux nuls) est le plus grand entier qui divise à la fois `a` et `b`. Deux entiers sont **premiers entre eux** si leur PGCD vaut 1. Le **PPCM** est le plus petit entier strictement positif multiple de `a` et `b`, et on a la relation `pgcd(a, b) × ppcm(a, b) = |a × b|`.

#### Principe

On s'appuie sur la propriété `pgcd(a, b) = pgcd(b, a mod b)` et sur le cas terminal `pgcd(a, 0) = a`.

**Justification.** Écrivons `a = q·b + r` avec `r = a mod b`. Tout diviseur commun de `a` et `b` divise `r = a - q·b` ; réciproquement, tout diviseur commun de `b` et `r` divise `a = q·b + r`. Les deux paires ont donc les **mêmes diviseurs communs**, et donc le même PGCD.

```python
def pgcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

print(pgcd(48, 18))                 # 6
ppcm = lambda a, b: a // pgcd(a, b) * b
print(ppcm(4, 6))                   # 12

import math
print(math.gcd(48, 18), math.lcm(4, 6))    # intégrés (math.lcm depuis Python 3.9)
```

Trace sur `(48, 18)` : `(48, 18)`, puis `(18, 12)`, puis `(12, 6)`, puis `(6, 0)`, résultat 6.

**Terminaison.** `b` est un variant : `a mod b < b`, donc `b` décroît strictement dans les entiers naturels.

**Complexité.** `O(log min(a, b))`. Le pire cas est atteint pour deux nombres de Fibonacci consécutifs (théorème de Lamé) : le nombre de divisions est proportionnel au logarithme du plus petit nombre.

L'**algorithme d'Euclide étendu** (chapitre 16) calcule en plus des coefficients de Bézout `x` et `y` tels que `a·x + b·y = pgcd(a, b)`.

### 7.2 Nombres premiers : test naïf

Un entier `n > 1` est **premier** s'il n'est divisible que par 1 et par lui-même. Sinon il est **composé**.

**Propriété clé.** Si `n` est composé, il possède un diviseur `d` tel que `2 ≤ d ≤ √n`. En effet, si `n = a × b` avec `a ≤ b`, alors `a² ≤ a × b = n`, donc `a ≤ √n`. Il suffit donc de tester les diviseurs jusqu'à `√n`.

```python
from math import isqrt

def est_premier(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):    # seuls les diviseurs impairs
        if n % d == 0:
            return False
    return True

print([k for k in range(30) if est_premier(k)])   # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

**Complexité.** `O(√n)` divisions. Pour tester **plusieurs** nombres, utiliser le **crible d'Ératosthène** (chapitre 16) ; pour de très grands nombres, **Miller-Rabin** (chapitre 16). Rappelons que `√n` est exponentiel en la taille de `n` en bits : ce test n'est utilisable que pour `n` jusqu'à environ 10¹².

### 7.3 Factorielle

La **factorielle** `n! = 1 × 2 × … × n` (avec `0! = 1`) dénombre les permutations de `n` objets.

```python
def factorielle(n):                 # version itérative : O(n) multiplications
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r

import math
print(math.factorial(20))           # 2432902008176640000
```

Python gère des **entiers de taille arbitraire** : aucun dépassement. Dans les langages à entiers de 64 bits, `21!` dépasse déjà la capacité (environ 9,2 × 10¹⁸). La croissance de `n!` est supérieure à toute exponentielle : d'après la formule de Stirling, `n! ≈ √(2πn) (n/e)ⁿ`, d'où `log(n!) = Θ(n log n)`.

### 7.4 Suite de Fibonacci

Définition : `F(0) = 0`, `F(1) = 1`, `F(n) = F(n-1) + F(n-2)`. La suite croît exponentiellement, comme `φⁿ/√5` où `φ = (1 + √5)/2 ≈ 1,618` est le nombre d'or.

| Méthode | Complexité | Remarque |
| --- | --- | --- |
| Récursive naïve | `O(φⁿ)` donc exponentielle | À éviter |
| Récursive avec mémoïsation | `O(n)` temps et espace | Simple |
| **Itérative** | `O(n)` temps, `O(1)` espace | Simple et efficace |
| **Doublement rapide** ou exponentiation de matrice | `O(log n)` multiplications | Pour de très grands `n` |

```python
def fib_iteratif(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_doublement(n):                       # renvoie (F(n), F(n+1)) en O(log n)
    if n == 0:
        return (0, 1)
    a, b = fib_doublement(n // 2)            # a = F(k), b = F(k+1), avec k = n // 2
    c = a * (2 * b - a)                      # F(2k)
    d = a * a + b * b                        # F(2k+1)
    return (d, c + d) if n % 2 else (c, d)

print(fib_iteratif(90), fib_doublement(90)[0])   # 2880067194370816120 2880067194370816120
```

Les formules du doublement viennent de l'identité matricielle `[[1,1],[1,0]]ⁿ = [[F(n+1), F(n)], [F(n), F(n-1)]]`. Elles sont à la base de l'exponentiation de matrices (chapitre 16).

### 7.5 Autres outils mathématiques intégrés à Python

```python
import math
print(math.isqrt(99))        # 9 : racine carrée entière exacte
print(math.comb(5, 2))       # 10 : combinaisons C(5, 2)
print(math.perm(5, 2))       # 20 : arrangements A(5, 2)
print(divmod(17, 5))         # (3, 2) : quotient et reste
print(pow(2, 10, 1000))      # 24 : (2**10) % 1000, exponentiation modulaire rapide
print(sum(int(c) for c in str(12345)))   # 15 : somme des chiffres
print(bin(10), int("1010", 2))           # 0b1010 10 : conversions de base
```

**Représentation des entiers et opérations sur les bits.** Un entier se décompose en base 2 ; les opérateurs `&` (et), `|` (ou), `^` (ou exclusif), `<<` et `>>` (décalages) manipulent les bits. On utilise `n & 1` pour tester la parité, `n >> 1` pour diviser par 2, `1 << k` pour la valeur `2ᵏ`, et `n & (n - 1) == 0` pour tester si `n > 0` est une puissance de 2. Ces astuces servent dans les masques de bits (chapitre 18) et les arbres de Fenwick (chapitre 23).

**Calcul approché et flottants.** Les nombres à virgule flottante sont binaires et approchés : `0.1 + 0.2 == 0.3` vaut `False`. On compare avec une tolérance (`math.isclose`) et on préfère les entiers ou les fractions (`fractions.Fraction`) dès qu'une précision exacte est requise.

### 7.6 Pièges fréquents

- Tester la primalité jusqu'à `n` au lieu de `√n`, ou oublier que `√n` est **exponentiel en la taille** de `n` (inutilisable au-delà de 10¹² environ).
- Calculer Fibonacci par la **récursion naïve** (`O(φⁿ)`) au lieu d'une boucle ou de la mémoïsation.
- Utiliser `/` (flottant) à la place de `//` ou de `isqrt` pour des calculs exacts sur de grands entiers.
- Comparer des flottants avec `==` (`0.1 + 0.2 != 0.3`) : utiliser `math.isclose` ou des fractions.

### Synthèse du chapitre 7

L'**algorithme d'Euclide** calcule le PGCD en `O(log min(a, b))` parce que `pgcd(a, b) = pgcd(b, a mod b)` conserve l'ensemble des diviseurs communs. Un test de primalité naïf s'arrête à `√n` ; `n!` croît plus vite que toute exponentielle ; **Fibonacci** illustre le contraste entre exponentiel (naïf), linéaire (itératif) et logarithmique (doublement). Retenez aussi les outils `math.gcd`, `isqrt`, `comb`, `pow(a, b, m)` et les opérations binaires.

---

# Partie II — Niveau intermédiaire

---

## 8. Algorithmes de tri avancés

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : écrire et analyser les tris fusion, rapide et par tas ; justifier leur complexité et leurs propriétés (stabilité, caractère en place) ; utiliser les tris sans comparaison (comptage, radix) quand les clés s'y prêtent ; expliquer le fonctionnement de Timsort ; choisir le tri adapté à une situation.

### 8.1 Vue d'ensemble

Les tris simples sont quadratiques. Les tris de ce chapitre atteignent `O(n log n)`, qui est **optimal** pour un tri par comparaisons (borne `Ω(n log n)`, section 2.10), ou même `O(n)` lorsqu'on exploite la nature des clés.

| Tri | Meilleur | Moyen | Pire | Espace | Stable | Principe |
| --- | --- | --- | --- | --- | --- | --- |
| **Fusion** (*merge*) | O(n log n) | O(n log n) | O(n log n) | O(n) | Oui | Diviser pour régner |
| **Rapide** (*quick*) | O(n log n) | O(n log n) | **O(n²)** | O(log n) | Non | Partition autour d'un pivot |
| **Par tas** (*heap*) | O(n log n) | O(n log n) | O(n log n) | O(1) en place | Non | Tas binaire |
| **Par comptage** | O(n + k) | O(n + k) | O(n + k) | O(k) | Oui (version cumulée) | Compter les occurrences |
| **Radix** | O(d(n + k)) | O(d(n + k)) | O(d(n + k)) | O(n + k) | Oui | Tri chiffre par chiffre |
| **Timsort** (Python, Java) | **O(n)** | O(n log n) | O(n log n) | O(n) | Oui | Fusion et insertion, exploite les séquences déjà triées |

> **Borne inférieure.** Tout tri par comparaisons exige `Ω(n log n)` comparaisons dans le pire cas. Seuls les tris sans comparaison (comptage, radix) font mieux, sous hypothèses sur les clés (entiers bornés, chaînes de longueur fixe).

### 8.2 Tri fusion (*Merge Sort*)

#### Principe

On **divise** la liste en deux moitiés, on **trie chaque moitié récursivement**, puis on **fusionne** les deux listes triées en une seule. La fusion est le cœur de l'algorithme : deux listes triées se fusionnent en temps linéaire en ne comparant que leurs têtes.

```python
def tri_fusion(t):
    if len(t) <= 1:                       # cas de base
        return t
    milieu = len(t) // 2
    gauche, droite = tri_fusion(t[:milieu]), tri_fusion(t[milieu:])

    resultat, i, j = [], 0, 0             # fusion de deux listes triées
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:        # <= garantit la stabilité
            resultat.append(gauche[i]); i += 1
        else:
            resultat.append(droite[j]); j += 1
    return resultat + gauche[i:] + droite[j:]

print(tri_fusion([5, 2, 9, 1, 5]))      # [1, 2, 5, 5, 9]
```

#### Analyse

- La fusion de deux listes de tailles totales `n` effectue au plus `n - 1` comparaisons : coût `O(n)`.
- Récurrence : `T(n) = 2T(n/2) + O(n)`. L'arbre de récursion a `log n` niveaux, chacun de coût `n`, donc `Θ(n log n)` **dans tous les cas**.
- Espace : `O(n)` pour les listes auxiliaires.
- Stable, grâce au `<=` (en cas d'égalité, on prend d'abord l'élément de la moitié gauche).

**Usages.** Listes chaînées (la fusion s'y fait sans espace supplémentaire), **tri externe** de fichiers plus grands que la mémoire (on trie des blocs puis on les fusionne), comptage d'inversions (en comptant, pendant la fusion, le nombre d'éléments de gauche restant quand on prend un élément de droite).

### 8.3 Tri rapide (*Quick Sort*)

#### Principe

On choisit un **pivot**, on **partitionne** le tableau (éléments plus petits à gauche, plus grands à droite), le pivot étant alors à sa place définitive ; puis on trie récursivement chaque côté. Contrairement au tri fusion, le travail est fait **avant** les appels récursifs (partition), et il n'y a rien à combiner.

```python
import random

def tri_rapide(t):
    if len(t) <= 1:
        return t
    pivot = random.choice(t)                 # pivot ALÉATOIRE : évite le pire cas sur des entrées triées
    moins = [x for x in t if x < pivot]
    egaux = [x for x in t if x == pivot]
    plus = [x for x in t if x > pivot]
    return tri_rapide(moins) + egaux + tri_rapide(plus)

print(tri_rapide([5, 2, 9, 1, 5]))           # [1, 2, 5, 5, 9]
```

#### Version en place (partition de Lomuto)

```python
import random

def tri_rapide_en_place(t, bas=0, haut=None):
    if haut is None:
        haut = len(t) - 1
    if bas < haut:
        i = random.randint(bas, haut)
        t[i], t[haut] = t[haut], t[i]            # pivot aléatoire placé en fin
        pivot, p = t[haut], bas
        for j in range(bas, haut):
            if t[j] < pivot:
                t[p], t[j] = t[j], t[p]
                p += 1
        t[p], t[haut] = t[haut], t[p]            # le pivot prend sa place définitive
        tri_rapide_en_place(t, bas, p - 1)
        tri_rapide_en_place(t, p + 1, haut)

liste = [5, 2, 9, 1, 5]
tri_rapide_en_place(liste)
print(liste)                                     # [1, 2, 5, 5, 9]
```

**Invariant de la partition de Lomuto.** Pendant la boucle, `t[bas:p]` ne contient que des éléments `< pivot`, `t[p:j]` que des éléments `>= pivot`.

#### Analyse

- **Meilleur cas** : le pivot coupe en deux moitiés égales, `T(n) = 2T(n/2) + O(n) = O(n log n)`.
- **Pire cas** : le pivot est toujours le minimum ou le maximum (par exemple pivot fixe sur un tableau déjà trié), `T(n) = T(n-1) + O(n) = O(n²)`.
- **Cas moyen** (ou espérance avec pivot aléatoire) : `O(n log n)`. Intuition : même un découpage déséquilibré constant (par exemple 10 % et 90 %) donne une profondeur logarithmique.
- Espace : `O(log n)` de pile en moyenne (on peut garantir `O(log n)` en recursant sur la plus petite partie d'abord).
- **Non stable** (la partition échange des éléments éloignés).

#### Améliorations en pratique

- **Pivot aléatoire** ou **médiane de trois** (médiane du premier, du milieu et du dernier élément).
- **Partition à trois voies** (moins, égaux, plus), comme dans la première version, qui traite efficacement les tableaux à nombreux doublons.
- **Introsort** : quicksort, bascule vers le tri par tas si la profondeur dépasse `2 log n` (garantit `O(n log n)`), et tri par insertion pour les petits blocs. C'est le tri de la bibliothèque standard C++. **pdqsort** (*pattern-defeating quicksort*) en est une évolution.
- **Quickselect** : la même partition trouve le `k`-ième plus petit élément en `O(n)` en moyenne (section 9.4).

### 8.4 Tri par tas (*Heap Sort*)

#### Principe

On transforme le tableau en **tas** (voir 3.7), puis on extrait `n` fois le sommet. Avec un tas-max, la version **en place** classique procède ainsi : on construit le tas-max dans le tableau en `O(n)`, puis on échange la racine (le maximum) avec le dernier élément du tas, on réduit la taille du tas de 1 et on **descend** la nouvelle racine pour restaurer la propriété de tas. Le tableau se remplit de la droite vers la gauche, du plus grand au plus petit.

```python
import heapq

def tri_par_tas(t):
    tas = list(t)
    heapq.heapify(tas)                                       # O(n)
    return [heapq.heappop(tas) for _ in range(len(tas))]     # n extractions en O(log n)

print(tri_par_tas([5, 2, 9, 1, 5]))      # [1, 2, 5, 5, 9]
```

**Complexité.** `Θ(n log n)` garanti (construction en `O(n)` plus `n` extractions en `O(log n)`). Cette version utilise `O(n)` d'espace (copie) ; la version en place classique utilise `O(1)`. Non stable. En pratique, plus lent que le tri rapide car ses accès mémoire sont dispersés (mauvaise localité du cache), mais sa garantie de pire cas et sa faible mémoire en font un bon choix de secours (introsort).

### 8.5 Tri par comptage (*Counting Sort*)

Pour des **entiers dans un petit intervalle** `[0, k]`, on n'a pas besoin de comparer : on **compte** les occurrences de chaque valeur, puis on reconstruit la liste triée.

```python
def tri_comptage(t, k):
    compte = [0] * (k + 1)
    for x in t:
        compte[x] += 1
    return [v for v, c in enumerate(compte) for _ in range(c)]

print(tri_comptage([3, 1, 3, 0, 2], 3))   # [0, 1, 2, 3, 3]
```

**Complexité** : `O(n + k)` en temps et en espace. Avantageux si `k = O(n)`. Cette version ne conserve pas l'identité des éléments (seulement les valeurs). La **version stable**, nécessaire comme brique du tri radix, calcule les **sommes cumulées** des comptes pour connaître la position finale de chaque valeur, puis place les éléments en parcourant l'entrée de droite à gauche.

### 8.6 Tri radix (par base)

Le tri radix trie des entiers (ou des chaînes de même longueur) **chiffre par chiffre**, du **moins significatif** au plus significatif, en utilisant à chaque passe un tri **stable** (comptage ou seaux). La stabilité garantit que l'ordre obtenu aux chiffres de poids faible subsiste pour les éléments égaux sur les chiffres de poids fort.

```python
def tri_radix(t):
    if not t:
        return t
    exp, maximum = 1, max(t)
    while maximum // exp > 0:
        seaux = [[] for _ in range(10)]
        for x in t:
            seaux[(x // exp) % 10].append(x)      # le chiffre de poids exp
        t = [x for seau in seaux for x in seau]   # concaténation stable
        exp *= 10
    return t

print(tri_radix([170, 45, 75, 90, 802, 24, 2, 66]))   # [2, 24, 45, 66, 75, 90, 170, 802]
```

**Complexité** : `O(d · (n + b))` pour `d` chiffres en base `b`. Pour des entiers de taille bornée, c'est un tri linéaire. Il s'applique aux entiers positifs et aux chaînes de longueur fixe ; pour les entiers négatifs, on traite le signe à part ou on décale les valeurs.

### 8.7 Timsort et tri en Python

`sorted()` et `list.sort()` utilisent **Timsort**, un tri hybride conçu par Tim Peters en 2002 :

1. Il détecte les **séquences déjà triées** (*runs*, croissantes ou strictement décroissantes que l'on retourne) dans les données réelles.
2. Il étend les petits runs jusqu'à une longueur minimale avec un tri par insertion.
3. Il **fusionne** les runs en respectant une politique qui garde l'équilibre des tailles. Depuis Python 3.11, cette politique est celle de **Powersort**.

Résultat : **stable**, `O(n log n)` garanti, `O(n)` si l'entrée est presque triée.

```python
t = [("Alice", 30), ("Bob", 25), ("Chloé", 30)]
print(sorted(t, key=lambda p: p[1]))               # par âge ; stabilité : Alice avant Chloé
print(sorted(t, key=lambda p: (-p[1], p[0])))      # âge décroissant puis nom croissant
print(sorted(t, reverse=True))
```

Le paramètre `key` est évalué une seule fois par élément ; `reverse=True` conserve la stabilité. Pour trier selon plusieurs critères, on peut soit utiliser un tuple comme clé, soit enchaîner plusieurs tris stables en commençant par le critère le moins important.

### 8.8 Quel tri choisir ?

| Situation | Choix |
| --- | --- |
| Usage général en Python | `sorted()` ou `.sort()` |
| Stabilité et garantie O(n log n) | Tri fusion |
| Mémoire très limitée, garantie de pire cas | Tri par tas |
| Entiers dans un petit intervalle | Comptage |
| Entiers ou chaînes de taille fixe, grand volume | Radix |
| Petits tableaux (moins de 20 éléments environ) | Insertion |
| Fichiers plus grands que la mémoire | Tri fusion externe |
| Seulement les `k` plus petits ou plus grands | Tas (`heapq.nsmallest`) ou quickselect |

### 8.9 Pièges fréquents

- Choisir le **pivot fixe** (premier ou dernier élément) du tri rapide : un tableau trié donne le pire cas `O(n²)` ; utiliser un pivot aléatoire ou la médiane de trois.
- Écrire `<` au lieu de `<=` dans la fusion : le tri fusion perd sa **stabilité**.
- Oublier de **copier** les sous-listes ou de gérer les restes lors de la fusion.
- Employer le tri par comptage avec un intervalle `k` très grand devant `n` : le coût `O(n + k)` et la mémoire explosent.
- Réécrire un tri à la main alors que `sorted()` est stable, optimisé et en `O(n)` sur les données presque triées.

### Synthèse du chapitre 8

La borne `Ω(n log n)` des tris par comparaisons est atteinte par le **tri fusion** (garanti, stable, `O(n)` d'espace), le **tri rapide** (en moyenne, en place, non stable, pire cas `O(n²)`) et le **tri par tas** (garanti, en place, non stable). Les tris **par comptage** et **radix** font mieux sous hypothèses sur les clés, et **Timsort** combine fusion et insertion pour être stable et adaptatif. Retenez le tableau de choix de la section 8.8.

---

## 9. Diviser pour régner

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : décrire le schéma diviser, régner, combiner ; le distinguer de la programmation dynamique ; résoudre le sous-tableau de somme maximale et le k-ième plus petit élément (quickselect) ; appliquer le théorème maître à une récurrence ; expliquer comment Karatsuba et Strassen réduisent le nombre d'appels récursifs.

### 9.1 Principe

Le paradigme **diviser pour régner** (*divide and conquer*) résout un problème en trois temps :

1. **Diviser** le problème en sous-problèmes **indépendants** de même nature, de taille plus petite.
2. **Régner** : résoudre chaque sous-problème récursivement ; en dessous d'un seuil, on applique une résolution directe (cas de base).
3. **Combiner** les solutions des sous-problèmes pour obtenir celle du problème initial.

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

> **Diviser pour régner et programmation dynamique.** Ici les sous-problèmes sont **indépendants** (aucun n'est calculé deux fois). En programmation dynamique, ils **se chevauchent**, et l'on mémorise leurs résultats.

**Points d'attention.** Les sous-problèmes doivent être réellement plus petits (terminaison) ; le coût de division et de combinaison détermine la complexité ; en dessous d'un seuil, une méthode simple (insertion) est souvent plus rapide que la récursion.

### 9.2 Exemple : maximum d'une liste

```python
def maximum_dc(t, bas=0, haut=None):
    if haut is None:
        haut = len(t) - 1
    if bas == haut:
        return t[bas]                                    # cas de base : un seul élément
    milieu = (bas + haut) // 2
    return max(maximum_dc(t, bas, milieu), maximum_dc(t, milieu + 1, haut))

print(maximum_dc([3, 8, 2, 9, 4]))        # 9
```

Récurrence `T(n) = 2T(n/2) + O(1)`, soit `O(n)`. Il n'y a **aucun gain** par rapport à la boucle simple : diviser pour régner n'est pas toujours utile, mais cet exemple met en évidence la structure du schéma (et se parallélise facilement).

### 9.3 Exemple : sous-tableau de somme maximale

**Problème.** Trouver la plus grande somme d'une tranche contiguë d'un tableau d'entiers (éventuellement négatifs).

**Idée.** Le meilleur sous-tableau est soit entièrement dans la moitié gauche, soit entièrement dans la moitié droite, soit **traverse le milieu**. Dans ce dernier cas, il se compose du meilleur suffixe de la moitié gauche et du meilleur préfixe de la moitié droite, calculables en `O(n)`.

```python
def somme_max(t, bas=0, haut=None):
    if haut is None:
        haut = len(t) - 1
    if bas == haut:
        return t[bas]
    m = (bas + haut) // 2

    s, meilleur_g = 0, float("-inf")          # meilleur sous-tableau finissant en m
    for i in range(m, bas - 1, -1):
        s += t[i]
        meilleur_g = max(meilleur_g, s)
    s, meilleur_d = 0, float("-inf")          # meilleur sous-tableau commençant en m + 1
    for i in range(m + 1, haut + 1):
        s += t[i]
        meilleur_d = max(meilleur_d, s)

    return max(somme_max(t, bas, m), somme_max(t, m + 1, haut), meilleur_g + meilleur_d)

print(somme_max([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6
```

Récurrence `T(n) = 2T(n/2) + O(n)`, donc `O(n log n)`. L'**algorithme de Kadane** résout le même problème en `O(n)` par programmation dynamique (chapitre 18) : `courant = max(x, courant + x)`.

### 9.4 Quickselect : le k-ième plus petit élément

**Problème.** Trouver l'élément de rang `k` (en comptant à partir de 0) sans trier tout le tableau.

**Idée.** On partitionne autour d'un pivot, comme dans le tri rapide ; puis on ne poursuit que **du côté qui contient le rang cherché**.

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

print(quickselect([7, 1, 5, 3, 9], 2))      # 5 (le 3e plus petit)
```

**Complexité.** Si le pivot coupe en deux moitiés, `T(n) = T(n/2) + O(n)`, d'où `O(n)` (somme géométrique `n + n/2 + n/4 + … ≤ 2n`). En moyenne `O(n)`, au pire `O(n²)`. L'algorithme de la **médiane des médianes** choisit un pivot garanti et donne `O(n)` au pire (mais avec une grande constante). La médiane s'obtient avec `k = n // 2`.

### 9.5 Le théorème maître

Pour une récurrence de la forme

`T(n) = a · T(n/b) + Θ(n^d)` avec `a ≥ 1`, `b > 1`, `d ≥ 0`,

où `a` est le nombre de sous-problèmes, `n/b` la taille de chacun, `n^d` le coût de division et de combinaison, on pose `d* = log_b a` (exposant critique) et on compare `d` à `d*` :

| Comparaison | Résultat | Intuition (arbre de récursion) |
| --- | --- | --- |
| `d > log_b a` | **Θ(n^d)** | Le travail est concentré à la **racine** |
| `d = log_b a` | **Θ(n^d · log n)** | **Chaque niveau** coûte autant, il y a `log n` niveaux |
| `d < log_b a` | **Θ(n^(log\_b a))** | Le travail est concentré aux **feuilles** |

**Pourquoi ?** À la profondeur `i`, il y a `a^i` sous-problèmes de taille `n/b^i`, de coût total `a^i · (n/b^i)^d = n^d · (a/b^d)^i`. C'est une suite géométrique de raison `a/b^d` : si la raison est inférieure à 1 (`d > log_b a`), le premier terme domine ; égale à 1, tous les termes sont égaux ; supérieure à 1, le dernier terme (les feuilles, au nombre de `a^(log_b n) = n^(log_b a)`) domine.

| Algorithme | Récurrence | `(a, b, d)` | Résultat |
| --- | --- | --- | --- |
| Recherche binaire | `T(n/2) + O(1)` | (1, 2, 0) | Θ(log n) |
| Tri fusion | `2T(n/2) + O(n)` | (2, 2, 1) | Θ(n log n) |
| Quickselect (cas moyen) | `T(n/2) + O(n)` | (1, 2, 1) | Θ(n) |
| Maximum par division | `2T(n/2) + O(1)` | (2, 2, 0) | Θ(n) |
| Karatsuba | `3T(n/2) + O(n)` | (3, 2, 1) | Θ(n^1,585) |
| Strassen | `7T(n/2) + O(n²)` | (7, 2, 2) | Θ(n^2,807) |

**Limites.** Le théorème ne s'applique pas aux récurrences où les sous-problèmes sont de tailles inégales (quicksort pire cas) ni à `T(n) = T(n-1) + …`. Dans ces cas, on emploie le dépliage ou l'arbre de récursion.

### 9.6 Multiplication de grands entiers : Karatsuba

La multiplication scolaire de deux nombres de `n` chiffres coûte `O(n²)`. **Karatsuba** (1960) écrit `x = x₁·B + x₀` et `y = y₁·B + y₀` (avec `B = 10^(n/2)`), puis remarque que

`x·y = x₁y₁·B² + ((x₁ + x₀)(y₁ + y₀) - x₁y₁ - x₀y₀)·B + x₀y₀`.

Il suffit donc de **3 multiplications** de nombres de taille moitié (au lieu de 4), d'où `T(n) = 3T(n/2) + O(n)` et `Θ(n^(log₂3)) ≈ Θ(n^1,585)`. Python l'utilise pour les très grands entiers.

### 9.7 Multiplication de matrices : Strassen

Le produit naïf de deux matrices `n × n` coûte `O(n³)`. **Strassen** (1969) divise chaque matrice en 4 blocs et n'effectue que **7 produits récursifs au lieu de 8**, en échange de davantage d'additions, d'où `O(n^(log₂7)) ≈ O(n^2,81)`.

```text
M1 = (A11 + A22)(B11 + B22)     M5 = (A11 + A12) B22
M2 = (A21 + A22) B11            M6 = (A21 - A11)(B11 + B12)
M3 = A11 (B12 - B22)            M7 = (A12 - A22)(B21 + B22)
M4 = A22 (B21 - B11)

C11 = M1 + M4 - M5 + M7         C12 = M3 + M5
C21 = M2 + M4                   C22 = M1 - M2 + M3 + M6
```

L'exposant optimal `ω` de la multiplication matricielle est un problème ouvert : les meilleures bornes théoriques actuelles sont d'environ 2,37, mais ces algorithmes sont impraticables à cause de constantes énormes. En pratique, on emploie le produit naïf très optimisé (bibliothèques BLAS, gestion du cache, parallélisme) ou, pour de grandes tailles, Strassen.

### 9.8 Autres applications célèbres

- **Paire de points la plus proche** : on partitionne les points par abscisse, on résout chaque moitié, puis on examine une bande autour de la coupure en n'examinant, pour chaque point, qu'un nombre constant de voisins triés par ordonnée. `T(n) = 2T(n/2) + O(n) = O(n log n)`.
- **Transformée de Fourier rapide (FFT)** : évalue un polynôme de degré `n` en `n` points en `O(n log n)` au lieu de `O(n²)`, d'où la multiplication de polynômes en `O(n log n)`.
- **Comptage d'inversions** par tri fusion, **enveloppe convexe** par division, **skyline** (profil d'immeubles).

### 9.9 Pièges fréquents

- Appliquer **diviser pour régner** à des sous-problèmes qui se chevauchent : le coût redevient exponentiel ; c'est un cas de programmation dynamique.
- Utiliser le **théorème maître** hors de son domaine (sous-problèmes de tailles inégales, `T(n) = T(n - 1) + …`).
- Oublier le **coût de la combinaison** (copies de tranches, fusion) dans la récurrence.
- Rester en récursion jusqu'à la taille 1 alors qu'une méthode simple (insertion) est plus rapide sous un seuil.

### Synthèse du chapitre 9

**Diviser pour régner** résout des sous-problèmes **indépendants** puis combine leurs solutions. Le **théorème maître** donne la complexité de `T(n) = a·T(n/b) + Θ(nᵈ)` en comparant `d` à `log_b a` : travail à la racine, à chaque niveau ou aux feuilles. Retenez les exemples (tri fusion, recherche binaire, somme maximale, quickselect) et le gain d'exposant de **Karatsuba** (`n^1,585`) et de **Strassen** (`n^2,81`).

---

## 10. Algorithmes gloutons

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : décrire le principe d'un algorithme glouton ; énoncer la propriété du choix glouton et la sous-structure optimale ; démontrer la correction par argument d'échange ou par induction ; résoudre la sélection d'activités, le sac à dos fractionnaire et le codage de Huffman ; reconnaître les cas où le glouton échoue ; choisir entre glouton et programmation dynamique.

### 10.1 Principe

Un algorithme **glouton** (*greedy*) construit une solution **étape par étape** en effectuant à chaque étape le **choix localement optimal** selon un critère fixé, **sans jamais revenir sur une décision** prise.

| Avantages | Limites |
| --- | --- |
| Simples à écrire et à analyser | Optimal **seulement si** le problème possède les bonnes propriétés |
| Très rapides (souvent `O(n log n)`, dominés par un tri ou un tas) | Un choix local peut mener à une solution globale médiocre |
| Peu de mémoire | La correction doit être **démontrée** ; un test sur quelques exemples ne suffit pas |

### 10.2 Quand un algorithme glouton est-il correct ?

Deux propriétés doivent être établies.

1. **Propriété du choix glouton** : il existe une solution optimale qui contient le premier choix glouton. Autrement dit, faire le choix local ne ferme pas la porte à l'optimum.
2. **Sous-structure optimale** : après avoir fait ce choix, le problème restant est un problème du même type, et une solution optimale de ce problème restant, complétée par le choix, donne une solution optimale du problème initial.

#### Techniques de preuve

- **Argument d'échange** : on prend une solution optimale quelconque `O` et on montre qu'on peut la transformer, en échangeant un de ses éléments contre le choix glouton, en une solution **au moins aussi bonne** qui contient le choix glouton. En répétant, on transforme `O` en la solution gloutonne sans dégrader sa valeur.
- **Induction** : on montre que la solution gloutonne construite après `k` étapes est « en avance » ou « au moins aussi bonne » que toute autre solution après `k` étapes (méthode « le glouton reste en tête »).
- **Matroïdes** : un cadre théorique (ensemble d'ensembles « indépendants » vérifiant la propriété d'échange) pour lequel l'algorithme glouton qui ajoute les éléments par poids décroissant est optimal. L'arbre couvrant de poids minimal en est l'exemple fondamental.

### 10.3 Cadre général

```text
1. Trier ou organiser les candidats selon un critère (le bon critère est toute la difficulté).
2. Répéter : choisir le meilleur candidat compatible avec les choix précédents et l'ajouter.
3. S'arrêter quand la solution est complète (ou qu'aucun candidat ne convient).
```

Le choix du critère est essentiel : sur un même problème, plusieurs critères naturels sont possibles et seul l'un d'eux (ou aucun) est correct.

### 10.4 Sélection d'activités (*Activity Selection*)

**Problème.** On dispose de `n` activités, chacune avec un début et une fin. Choisir un **maximum d'activités compatibles** (deux à deux sans chevauchement).

**Critère glouton correct : l'heure de fin la plus tôt.** On trie par fin croissante, on retient la première, puis on retient chaque activité dont le début est postérieur ou égal à la fin de la dernière retenue.

```python
def selection_activites(activites):                  # liste de (debut, fin)
    activites.sort(key=lambda a: a[1])               # tri par fin croissante
    choisies, fin_derniere = [], float("-inf")
    for debut, fin in activites:
        if debut >= fin_derniere:
            choisies.append((debut, fin))
            fin_derniere = fin
    return choisies

print(selection_activites([(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]))
# [(1, 4), (5, 7), (8, 9)]
```

**Preuve par échange.** Soit `a₁` l'activité qui finit le plus tôt, et `O` une solution optimale dont la première activité (par ordre de fin) est `b₁`. Comme `a₁` finit au plus tôt, `fin(a₁) ≤ fin(b₁)`. Remplacer `b₁` par `a₁` dans `O` ne crée aucun chevauchement (les autres activités commencent après `fin(b₁) ≥ fin(a₁)`) et conserve le nombre d'activités. Il existe donc une solution optimale contenant `a₁` ; on conclut par induction sur le problème restant.

**Complexité** : `O(n log n)` (le tri domine). **Contre-exemples** : trier par début, par durée croissante ou par nombre de conflits **ne donne pas** l'optimum en général. Par exemple, avec `(0, 10)`, `(9, 11)`, `(10, 20)` pris par début croissant, on choisit `(0, 10)` puis `(10, 20)`, mais la durée la plus courte `(9, 11)` bloquerait les deux autres.

### 10.5 Sac à dos fractionnaire

**Problème.** Objets de valeur `vᵢ` et de poids `pᵢ`, capacité `C`. On peut prendre **une fraction** de chaque objet. Maximiser la valeur totale.

**Critère correct : le rapport valeur/poids décroissant.**

```python
def sac_a_dos_fractionnaire(objets, capacite):         # objets : (valeur, poids)
    objets.sort(key=lambda o: o[0] / o[1], reverse=True)
    total = 0.0
    for valeur, poids in objets:
        if capacite >= poids:
            total += valeur
            capacite -= poids
        else:
            total += valeur * capacite / poids         # fraction du dernier objet
            break
    return total

print(sac_a_dos_fractionnaire([(60, 10), (100, 20), (120, 30)], 50))   # 240.0
```

**Preuve.** Si une solution optimale laissait de côté une portion d'un objet de meilleur rapport tout en emportant une portion d'un objet de moins bon rapport, échanger les deux augmenterait strictement la valeur : contradiction.

> **Attention.** Pour le **sac à dos 0/1** (objets indivisibles), le glouton n'est **plus optimal** : avec capacité 50 et objets `(60, 10)`, `(100, 20)`, `(120, 30)`, le glouton prend les deux premiers (valeur 160) alors que prendre les deux derniers vaut 220. Il faut la **programmation dynamique** (chapitre 18).

### 10.6 Codage de Huffman

**Problème.** Compresser un texte sans perte en associant à chaque symbole un **code binaire** ; un **code préfixe** (aucun code n'est préfixe d'un autre) permet un décodage sans ambiguïté. On veut minimiser la longueur totale du texte codé.

**Algorithme glouton.** On crée une feuille par symbole, pondérée par sa fréquence. Tant qu'il reste plusieurs arbres, on **fusionne les deux arbres de plus faibles fréquences** en un nouvel arbre dont la fréquence est la somme. L'arbre final définit les codes : `0` pour descendre à gauche, `1` à droite. Les symboles fréquents sont proches de la racine et ont donc des codes courts.

```python
import heapq
from collections import Counter

def huffman(texte):
    tas = [[freq, i, symbole, None, None] for i, (symbole, freq) in enumerate(Counter(texte).items())]
    heapq.heapify(tas)
    compteur = len(tas)                                       # départage les fréquences égales
    while len(tas) > 1:
        a, b = heapq.heappop(tas), heapq.heappop(tas)         # les deux plus faibles fréquences
        heapq.heappush(tas, [a[0] + b[0], compteur, None, a, b])
        compteur += 1

    codes = {}
    def parcourir(noeud, code=""):
        if noeud[2] is not None:                              # feuille
            codes[noeud[2]] = code or "0"
        else:
            parcourir(noeud[3], code + "0")
            parcourir(noeud[4], code + "1")
    parcourir(tas[0])
    return codes

print(huffman("abracadabra"))
```

**Complexité** : `O(n log n)` pour `n` symboles distincts. **Optimalité** : parmi tous les codes préfixes, celui de Huffman minimise la longueur moyenne (démontré par échange : les deux symboles les moins fréquents peuvent être placés comme frères au niveau le plus profond).

### 10.7 Autres exemples gloutons

| Problème | Critère glouton | Remarque |
| --- | --- | --- |
| **Arbre couvrant minimal** (Kruskal, Prim) | Plus petite arête sûre | Chapitre 19 |
| **Plus courts chemins** (Dijkstra) | Sommet non traité le plus proche | Chapitre 20 |
| **Rendu de monnaie** | Plus grande pièce possible | Correct **seulement si** le système est « canonique » (euro, dollar) |
| Minimiser la somme des temps d'attente | Traiter les tâches les plus courtes d'abord | Argument d'échange |
| Ordonnancement avec échéances | Trier par échéance (EDF) | Minimise le retard maximal |
| Couverture d'intervalles par un minimum de points | Placer le point à la fin du premier intervalle non couvert | Comparable à la sélection d'activités |

#### Quand le glouton échoue : le rendu de monnaie

```python
def monnaie_gloutonne(pieces, montant):
    rendu = []
    for p in sorted(pieces, reverse=True):
        while montant >= p:
            montant -= p
            rendu.append(p)
    return rendu

print(monnaie_gloutonne([1, 3, 4], 6))    # [4, 1, 1] : 3 pièces, alors que [3, 3] en utilise 2
```

Pour des systèmes de pièces arbitraires, il faut la programmation dynamique (chapitre 18).

### 10.8 Glouton ou programmation dynamique ?

|  | Glouton | Programmation dynamique |
| --- | --- | --- |
| Décision | **Locale** et irrévocable | Examine toutes les options via les sous-problèmes |
| Vitesse | Très rapide | Plus lent, plus de mémoire |
| Optimalité | Seulement avec preuve | **Garantie** si sous-structure optimale |
| Exemples | Fractionnaire, Huffman, Kruskal | Sac à dos 0/1, rendu général |

### 10.9 Pièges fréquents

- Supposer le glouton optimal **sans preuve** : un critère naturel (début le plus tôt, durée la plus courte) peut être faux ; chercher un contre-exemple.
- Appliquer le glouton au **sac à dos 0/1** ou au rendu de monnaie avec un système de pièces arbitraire : il faut la programmation dynamique.
- Mal choisir le **critère de tri** : fin la plus tôt pour les activités, rapport valeur/poids pour le fractionnaire.
- Oublier le cas des **égalités** et le départage dans le tas de Huffman.

### Synthèse du chapitre 10

Un algorithme **glouton** fait à chaque étape le meilleur choix local, sans retour en arrière ; il est correct si le choix glouton appartient à une solution optimale et si le problème restant a la même structure, ce que l'on démontre par **échange** ou par induction. Retenez la sélection d'activités (tri par fin), le sac à dos fractionnaire (rapport valeur/poids), **Huffman**, les liens avec Kruskal et Dijkstra, et la frontière avec la programmation dynamique.

---

## 11. Retour sur trace (*backtracking*)

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : décrire le retour sur trace comme une exploration d'un arbre de recherche avec élagage ; appliquer le schéma choisir, explorer, défaire ; générer sous-ensembles et permutations ; résoudre N reines, Sudoku et somme de sous-ensemble ; estimer le coût d'une recherche exhaustive ; décider quand ajouter de la mémoïsation.

### 11.1 Principe

Le **retour sur trace** construit une solution **pas à pas** en essayant des choix successifs. Lorsqu'un choix conduit à une **impasse** (contrainte violée, solution partielle ne pouvant plus être complétée), on **annule** ce choix (on revient en arrière) et on essaie le suivant. C'est une **recherche exhaustive organisée** : on parcourt implicitement un **arbre de recherche**, dont chaque nœud est une solution partielle et chaque arête un choix.

L'**élagage** (*pruning*) est l'idée centrale : on abandonne une branche dès qu'on sait qu'elle ne peut pas aboutir, ce qui évite d'explorer tout son sous-arbre.

```text
Arbre de recherche :  choix 1 -- choix 2 -- choix 3   (impasse : on revient en arrière)
                                   |-- choix 2' -- ... (solution trouvée)
```

### 11.2 Schéma général

```python
def retour_sur_trace(etat, solutions, est_complet, candidats, est_valide, appliquer, annuler):
    if est_complet(etat):                      # solution trouvée
        solutions.append(list(etat))           # copie de l'état courant
        return
    for choix in candidats(etat):
        if est_valide(etat, choix):            # élagage : ne continuer que si prometteur
            appliquer(etat, choix)             # 1. choisir
            retour_sur_trace(etat, solutions, est_complet, candidats, est_valide, appliquer, annuler)  # 2. explorer
            annuler(etat, choix)               # 3. défaire (backtrack)

# Application : toutes les permutations de {1, 2, 3}
solutions = []
retour_sur_trace(
    [], solutions,
    est_complet=lambda etat: len(etat) == 3,
    candidats=lambda etat: [1, 2, 3],
    est_valide=lambda etat, c: c not in etat,        # élagage : pas de répétition
    appliquer=lambda etat, c: etat.append(c),
    annuler=lambda etat, c: etat.pop(),
)
print(solutions)    # 6 permutations
```

Les trois étapes **choisir, explorer, défaire** sont indissociables : oublier de défaire laisse un état corrompu pour les branches suivantes. De même, il faut **copier** l'état courant quand on l'ajoute aux solutions (`list(etat)` ou `courant[:]`), sinon toutes les solutions pointent vers la même liste, modifiée ensuite.

### 11.3 Sous-ensembles et permutations

```python
def sous_ensembles(t):
    resultat, courant = [], []
    def aller(i):
        if i == len(t):
            resultat.append(courant[:])
            return
        aller(i + 1)                          # sans t[i]
        courant.append(t[i])                  # avec t[i]
        aller(i + 1)
        courant.pop()
    aller(0)
    return resultat                           # 2^n sous-ensembles

def permutations(t):
    resultat = []
    def aller(debut):
        if debut == len(t):
            resultat.append(t[:])
            return
        for i in range(debut, len(t)):
            t[debut], t[i] = t[i], t[debut]
            aller(debut + 1)
            t[debut], t[i] = t[i], t[debut]   # annuler l'échange
    aller(0)
    return resultat                           # n! permutations

print(len(sous_ensembles([1, 2, 3])))         # 8 = 2^3
print(len(permutations([1, 2, 3])))           # 6 = 3!

from itertools import permutations as perms, combinations
print(list(combinations([1, 2, 3], 2)))       # [(1, 2), (1, 3), (2, 3)]
```

Les sous-ensembles se modélisent par une décision binaire (prendre ou non chaque élément) : `2ⁿ` feuilles. Les permutations se construisent en fixant successivement l'élément de chaque position : `n!` feuilles. Pour les entrées avec doublons, on trie d'abord puis on saute un élément identique au précédent au même niveau de choix, afin de ne pas produire de solutions répétées.

### 11.4 Problème des N reines

**Problème.** Placer `n` reines sur un échiquier `n × n` de sorte qu'aucune n'en attaque une autre (ni même ligne, ni même colonne, ni même diagonale).

**Modélisation.** On place **une reine par ligne** ; le choix est la colonne. Pour tester la compatibilité en `O(1)`, on mémorise les colonnes occupées, les diagonales « descendantes » (identifiées par `ligne - colonne`) et « montantes » (identifiées par `ligne + colonne`).

```python
def n_reines(n):
    solutions = []
    colonnes, diag1, diag2 = set(), set(), set()
    placement = []

    def placer(ligne):
        if ligne == n:
            solutions.append(placement[:])
            return
        for col in range(n):
            if col in colonnes or (ligne - col) in diag1 or (ligne + col) in diag2:
                continue                                  # élagage en O(1)
            colonnes.add(col); diag1.add(ligne - col); diag2.add(ligne + col)
            placement.append(col)
            placer(ligne + 1)
            placement.pop()
            colonnes.remove(col); diag1.remove(ligne - col); diag2.remove(ligne + col)

    placer(0)
    return solutions

print(len(n_reines(8)))      # 92 solutions
```

Sans élagage, il y aurait `nⁿ` placements (ou `n!` en imposant des colonnes distinctes) ; avec l'élagage, le nombre de nœuds explorés est incomparablement plus faible (quelques milliers pour `n = 8`).

### 11.5 Solveur de Sudoku

```python
def resoudre_sudoku(grille):                   # grille 9 x 9, 0 = case vide
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

grille = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
print(resoudre_sudoku(grille))      # True
print(grille[0])                    # [5, 3, 4, 6, 7, 8, 9, 1, 2]
```

> **Optimisations.** Choisir d'abord la case qui a **le moins de valeurs possibles** (heuristique MRV, *minimum remaining values*) ; mémoriser les valeurs possibles de chaque ligne, colonne et bloc avec des **masques de bits** ; propager les contraintes (une case n'ayant qu'une valeur possible est remplie immédiatement).

### 11.6 Somme de sous-ensemble et autres problèmes classiques

```python
def somme_sous_ensemble(t, cible):                 # existe-t-il un sous-ensemble de somme cible ? (t positifs, trié)
    t = sorted(t)
    def aller(i, reste):
        if reste == 0:
            return True
        if i == len(t) or t[i] > reste:            # élagage : les suivants sont trop grands
            return False
        return aller(i + 1, reste - t[i]) or aller(i + 1, reste)
    return aller(0, cible)

print(somme_sous_ensemble([3, 34, 4, 12, 5, 2], 9))   # True (4 + 5)
```

| Problème | Idée |
| --- | --- |
| **Rat dans un labyrinthe** | Avancer, marquer, reculer en cas d'impasse |
| **Parcours du cavalier** | Visiter toutes les cases ; heuristique de Warnsdorff (aller vers la case ayant le moins de sorties) |
| **Chemin hamiltonien** | Visiter chaque sommet une seule fois (NP-complet) |
| **Coloration de graphe**, **mots croisés**, **SAT** | Affecter, vérifier les contraintes, annuler |
| **Génération de combinaisons, parenthésages bien formés** | Construire en respectant des invariants |

### 11.7 Complexité et comparaison

Le **pire cas reste exponentiel** (`O(2ⁿ)`, `O(n!)`, `O(kⁿ)`) : l'élagage améliore beaucoup la pratique mais pas le pire cas. Pour estimer le coût, on dénombre les nœuds de l'arbre de recherche.

|  | Retour sur trace | Glouton | Programmation dynamique |
| --- | --- | --- | --- |
| Exploration | Exhaustive, avec élagage | Un seul chemin | Sous-problèmes mémorisés |
| Revient en arrière | Oui | Non | Non applicable |
| Sous-problèmes répétés | Souvent recalculés | Sans objet | **Mémorisés** |
| Garantie d'optimalité | Oui (exhaustif) | Non en général | Oui |

> Si l'on observe que des **sous-problèmes se répètent** (mêmes paramètres atteints par des chemins différents), on ajoute de la **mémoïsation** : le retour sur trace devient de la programmation dynamique.

**Variantes pour l'optimisation : séparation et évaluation (*branch and bound*).** Pour un problème d'optimisation, on garde la meilleure solution trouvée et on **abandonne** toute branche dont une **borne optimiste** (par exemple une relaxation du problème) n'est pas meilleure que cette solution.

### 11.8 Pièges fréquents

- Oublier de **défaire** le choix après l'appel récursif : l'état reste corrompu pour les branches suivantes.
- Ajouter l'état courant aux solutions **sans le copier** (`courant[:]`) : toutes les solutions pointent vers la même liste.
- Élaguer **trop tard** (vérifier la contrainte en fin de branche) : le coût redevient celui d'une énumération complète.
- Produire des **solutions répétées** avec des doublons : trier d'abord et sauter les valeurs identiques au même niveau.
- Ne pas remarquer que les sous-problèmes **se répètent** : la mémoïsation transformerait l'exploration en programmation dynamique.

### Synthèse du chapitre 11

Le **retour sur trace** construit une solution pas à pas, abandonne une branche dès qu'elle ne peut plus aboutir (**élagage**) et revient en arrière par le triptyque choisir, explorer, défaire. Son coût reste **exponentiel** dans le pire cas (`2ⁿ`, `n!`) mais l'élagage le rend praticable pour N reines, Sudoku ou la somme de sous-ensemble. Retenez les heuristiques (MRV, masques de bits), la variante **séparation et évaluation** pour l'optimisation et le lien avec la programmation dynamique.

---

## 12. Technique des deux pointeurs

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : reconnaître un problème que la technique des deux pointeurs ramène de `O(n²)` à `O(n)` ; distinguer pointeurs opposés, pointeurs de même sens et lièvre-tortue ; justifier le déplacement d'un pointeur par un argument d'élimination ; résoudre deux-somme, trois-somme, palindrome, conteneur d'eau et détection de cycle.

### 12.1 Principe

La technique des **deux pointeurs** utilise **deux indices** qui parcourent une séquence (tableau, chaîne, liste chaînée). Au lieu d'examiner toutes les paires `(i, j)` avec deux boucles imbriquées en `O(n²)`, on fait **avancer** les pointeurs de façon coordonnée, chaque pointeur ne parcourant la séquence qu'une seule fois : `O(n)`.

Le cœur de la méthode est un **argument d'élimination** : à chaque pas, on peut prouver qu'un certain nombre de paires candidates ne peuvent pas être la réponse, et on les écarte toutes d'un coup en déplaçant un pointeur.

| Variante | Description | Usages |
| --- | --- | --- |
| **Pointeurs opposés** | Un indice à chaque extrémité, qui convergent | Tableaux triés, palindromes, paires de somme donnée, aire maximale |
| **Même sens** (lent et rapide) | Les deux indices avancent vers la droite à des rythmes différents | Suppression de doublons, partition, fenêtre à taille variable |
| **Lièvre et tortue** (Floyd) | Un pointeur avance de 1, l'autre de 2 | Détection de cycle, milieu d'une liste chaînée |
| **Deux séquences** | Un pointeur par tableau | Fusion de listes triées, intersection |

### 12.2 Somme de deux nombres dans un tableau trié

**Problème.** Dans un tableau trié, trouver deux éléments dont la somme vaut `cible`.

**Idée.** On place `g` au début et `d` à la fin. Si `t[g] + t[d]` est trop petit, aucune paire utilisant `t[g]` avec un élément à gauche de `d` ne peut convenir (ces éléments sont plus petits que `t[d]`) : on avance `g`. Si la somme est trop grande, symétriquement, on recule `d`.

```python
def deux_somme_trie(t, cible):
    g, d = 0, len(t) - 1
    while g < d:
        s = t[g] + t[d]
        if s == cible:
            return (g, d)
        if s < cible:
            g += 1            # il faut une somme plus grande
        else:
            d -= 1            # il faut une somme plus petite
    return None

print(deux_somme_trie([1, 3, 4, 6, 9], 10))   # (0, 4) car 1 + 9 = 10
```

**Complexité.** `O(n)` après le tri éventuel (`O(n log n)`). Sur un tableau non trié, un `dict` donne aussi `O(n)` (chapitre 17), mais le tableau trié permet une version en espace `O(1)`.

### 12.3 Autres exemples

```python
def est_palindrome(s):
    s = [c.lower() for c in s if c.isalnum()]
    g, d = 0, len(s) - 1
    while g < d:
        if s[g] != s[d]:
            return False
        g += 1
        d -= 1
    return True

def supprimer_doublons_tries(t):              # en place, renvoie la nouvelle longueur
    if not t:
        return 0
    lent = 0
    for rapide in range(1, len(t)):
        if t[rapide] != t[lent]:
            lent += 1
            t[lent] = t[rapide]
    return lent + 1

def trois_somme(t):                           # triplets de somme nulle : O(n^2)
    t.sort()
    res = []
    for i in range(len(t) - 2):
        if i and t[i] == t[i - 1]:
            continue                          # évite les triplets répétés
        g, d = i + 1, len(t) - 1
        while g < d:
            s = t[i] + t[g] + t[d]
            if s < 0:
                g += 1
            elif s > 0:
                d -= 1
            else:
                res.append((t[i], t[g], t[d]))
                g += 1
                d -= 1
                while g < d and t[g] == t[g - 1]:
                    g += 1
    return res

def aire_max_conteneur(h):                    # « Container With Most Water »
    g, d, meilleur = 0, len(h) - 1, 0
    while g < d:
        meilleur = max(meilleur, min(h[g], h[d]) * (d - g))
        if h[g] < h[d]:
            g += 1                            # la hauteur est limitée par la plus petite paroi
        else:
            d -= 1
    return meilleur

print(est_palindrome("Esope reste ici et se repose"))      # True
t = [1, 1, 2, 2, 3]
print(supprimer_doublons_tries(t), t[:3])                # 3 [1, 2, 3]
print(trois_somme([-1, 0, 1, 2, -1, -4]))                # [(-1, -1, 2), (-1, 0, 1)]
print(aire_max_conteneur([1, 8, 6, 2, 5, 4, 8, 3, 7]))   # 49
```

**Justification du conteneur.** L'aire vaut `min(h[g], h[d]) × (d - g)`. Quand on rapproche les parois, la largeur diminue ; seule une paroi plus haute peut compenser. La paroi la plus **basse** est celle qui limite l'aire : la conserver en rapprochant l'autre ne peut que diminuer l'aire. On la déplace donc, sans perdre l'optimum.

**Fusion de deux tableaux triés** (brique du tri fusion) : un pointeur par tableau, on avance celui dont l'élément est le plus petit. **Partition** (drapeau néerlandais) : trois pointeurs (`bas`, `milieu`, `haut`) pour séparer 0, 1 et 2 en un seul passage.

#### Détection de cycle (lièvre et tortue de Floyd)

On avance un pointeur **lent** d'un pas et un pointeur **rapide** de deux pas. S'il y a un cycle, le rapide finit par rattraper le lent (la distance entre eux diminue de 1 à chaque tour une fois dans le cycle) ; sinon, le rapide atteint la fin de la liste.

```python
class Noeud:
    def __init__(self, valeur, suivant=None):
        self.valeur, self.suivant = valeur, suivant

def a_un_cycle(tete):
    lent = rapide = tete
    while rapide and rapide.suivant:
        lent, rapide = lent.suivant, rapide.suivant.suivant
        if lent is rapide:
            return True
    return False

a, b, c = Noeud(1), Noeud(2), Noeud(3)
a.suivant, b.suivant = b, c
print(a_un_cycle(a))        # False
c.suivant = a               # on referme la boucle
print(a_un_cycle(a))        # True
```

Complexité `O(n)` en temps, `O(1)` en espace (contre `O(n)` pour une solution avec un `set` de nœuds visités). On l'utilise aussi pour trouver le **milieu** d'une liste (quand le rapide atteint la fin, le lent est au milieu) et le **début** du cycle.

### 12.4 Quand l'utiliser ?

- Le tableau est **trié** (ou peut l'être sans nuire) et on cherche des paires ou triplets.
- On compare des éléments **aux extrémités** (palindrome, conteneur).
- On parcourt une séquence en **un seul passage** avec une exigence de mémoire `O(1)`.
- On modifie un tableau **en place** (suppression, partition).

Si les données ne sont pas triées et que le tri est interdit, préférer le hachage (chapitre 17).

### 12.5 Pièges fréquents

- Appliquer des pointeurs opposés à un tableau **non trié** : l'argument d'élimination repose sur la monotonie.
- Écrire `g <= d` au lieu de `g < d` (ou l'inverse) : une paire utilise deux indices **distincts**.
- Oublier de **sauter les doublons** dans trois-somme : les triplets sont répétés.
- Modifier un tableau en place pendant qu'un pointeur le parcourt sans définir précisément ce que représente chaque pointeur.

### Synthèse du chapitre 12

La technique des **deux pointeurs** remplace deux boucles imbriquées par un parcours coordonné de coût `O(n)`, grâce à un **argument d'élimination** : une comparaison permet d'écarter d'un coup toutes les paires qui ne peuvent pas convenir. Retenez ses variantes (opposés, même sens, lièvre et tortue de Floyd pour les cycles en espace constant) et le fait qu'elle suppose souvent un tableau **trié**.

---

## 13. Fenêtre glissante

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : distinguer fenêtre de taille fixe et de taille variable ; maintenir une fenêtre de façon incrémentale ; justifier la complexité amortie `O(n)` ; résoudre la plus longue sous-chaîne sans répétition, le plus court sous-tableau de somme donnée et les anagrammes ; utiliser une file monotone pour le maximum d'une fenêtre ; reconnaître quand la monotonie manque.

### 13.1 Principe

La **fenêtre glissante** (*sliding window*) maintient un **intervalle contigu** `[g, d]` d'une séquence et le fait **glisser** vers la droite en mettant à jour l'information de manière **incrémentale** : on ajoute l'élément qui entre et on retire celui qui sort, au lieu de recalculer toute la fenêtre. Chaque indice entre au plus une fois et sort au plus une fois, d'où une complexité typique en **`O(n)`**.

| Type | Description | Exemple |
| --- | --- | --- |
| **Taille fixe `k`** | La fenêtre garde la même longueur | Somme maximale de `k` éléments consécutifs |
| **Taille variable** | On étend à droite, puis on réduit à gauche tant qu'une condition est violée (ou satisfaite) | Plus longue sous-chaîne sans répétition |

C'est un cas particulier de deux pointeurs de même sens, où les deux pointeurs délimitent la fenêtre et ne reculent jamais.

### 13.2 Taille fixe : somme maximale de `k` éléments consécutifs

```python
def somme_max_fenetre(t, k):
    somme = sum(t[:k])                       # première fenêtre
    meilleur = somme
    for i in range(k, len(t)):
        somme += t[i] - t[i - k]             # entre t[i], sort t[i-k]
        meilleur = max(meilleur, somme)
    return meilleur

print(somme_max_fenetre([2, 1, 5, 1, 3, 2], 3))   # 9 (5 + 1 + 3)
```

La version naïve recalcule chaque somme en `O(k)`, soit `O(nk)` au total ; la fenêtre glissante met à jour en `O(1)`, soit `O(n)`.

### 13.3 Taille variable : plus longue sous-chaîne sans répétition

**Problème.** Longueur de la plus longue sous-chaîne dont tous les caractères sont distincts.

**Idée.** On étend la fenêtre à droite ; si le nouveau caractère est déjà dans la fenêtre, on **saute** le bord gauche juste après sa dernière occurrence.

```python
def plus_longue_sans_repetition(s):
    derniere_position = {}
    g = meilleur = 0
    for d, c in enumerate(s):
        if c in derniere_position and derniere_position[c] >= g:
            g = derniere_position[c] + 1         # on saute après la dernière occurrence
        derniere_position[c] = d
        meilleur = max(meilleur, d - g + 1)
    return meilleur

print(plus_longue_sans_repetition("abcabcbb"))   # 3 ("abc")
```

**Invariant** : la fenêtre `s[g..d]` ne contient aucun caractère répété. `g` ne fait que croître : au plus `n` déplacements au total.

### 13.4 Taille variable : plus petit sous-tableau de somme au moins `S`

**Problème.** Pour un tableau de valeurs **strictement positives**, longueur du plus court sous-tableau contigu de somme supérieure ou égale à `S`.

```python
def plus_court_sous_tableau(t, S):
    g = somme = 0
    meilleur = float("inf")
    for d, x in enumerate(t):
        somme += x
        while somme >= S:                         # fenêtre valide : on essaie de la réduire
            meilleur = min(meilleur, d - g + 1)
            somme -= t[g]
            g += 1
    return 0 if meilleur == float("inf") else meilleur

print(plus_court_sous_tableau([2, 3, 1, 2, 4, 3], 7))   # 2 (4 + 3)
```

**Complexité** `O(n)` : bien que la boucle `while` soit imbriquée, `g` ne dépasse jamais `d`, donc le nombre total d'exécutions de `g += 1` est au plus `n` (**analyse amortie**).

> **Condition essentielle.** Cette méthode exige que la **monotonie** soit vraie : ajouter un élément à droite ne fait qu'augmenter la somme, en retirer un à gauche ne fait que la diminuer. Avec des valeurs **négatives**, cette hypothèse tombe : on utilise alors les sommes préfixes avec une table de hachage (chapitre 14) ou une file monotone.

### 13.5 Maximum de chaque fenêtre : file monotone

**Problème.** Pour chaque fenêtre de taille `k`, calculer son maximum.

**Idée.** On maintient une **file à double entrée** d'indices dont les valeurs sont en ordre **décroissant** : le maximum est toujours en tête. Quand un nouvel élément arrive, on retire par la fin tous les éléments plus petits (qui ne seront plus jamais maximum tant que le nouvel élément est dans la fenêtre). On retire aussi par la tête l'indice sorti de la fenêtre.

```python
from collections import deque

def maximums_fenetres(t, k):
    dq, res = deque(), []                      # dq contient des INDICES de valeurs décroissantes
    for i, x in enumerate(t):
        while dq and t[dq[-1]] <= x:
            dq.pop()                           # dominés par x
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()                       # sorti de la fenêtre
        if i >= k - 1:
            res.append(t[dq[0]])
    return res                                 # O(n) amorti

print(maximums_fenetres([1, 3, -1, -3, 5, 3, 6, 7], 3))   # [3, 3, 5, 5, 6, 7]
```

Chaque indice est inséré et retiré au plus une fois : `O(n)` amorti, contre `O(nk)` naïf ou `O(n log n)` avec un tas.

### 13.6 Fenêtre avec comptage : anagrammes et couverture

Pour des problèmes de chaînes, la fenêtre s'accompagne d'un **dictionnaire de compteurs** (`Counter`). Exemple : trouver les positions où une sous-chaîne de longueur `m` est un anagramme du motif.

```python
from collections import Counter

def positions_anagrammes(texte, motif):
    m, res = len(motif), []
    cible, fenetre = Counter(motif), Counter(texte[:m - 1])
    for i in range(m - 1, len(texte)):
        fenetre[texte[i]] += 1                 # entre
        if fenetre == cible:
            res.append(i - m + 1)
        fenetre[texte[i - m + 1]] -= 1         # sort
        if fenetre[texte[i - m + 1]] == 0:
            del fenetre[texte[i - m + 1]]
    return res

print(positions_anagrammes("cbaebabacd", "abc"))    # [0, 6]
```

Autres problèmes classiques : plus long sous-tableau avec au plus `k` valeurs distinctes, sous-chaîne minimale contenant tous les caractères d'un motif, plus longue sous-chaîne avec remplacement d'au plus `k` caractères, fruits dans des paniers.

### 13.7 Reconnaître une fenêtre glissante

Le problème porte sur un sous-tableau ou une sous-chaîne **contigu(ë)**, cherche un optimum (plus long, plus court, plus grand) sous une contrainte **monotone**. Si la contrainte n'est pas monotone (valeurs négatives), préférer préfixes et hachage.

### 13.8 Pièges fréquents

- Employer la fenêtre variable avec des valeurs **négatives** : la monotonie tombe ; passer par les sommes préfixes et un dictionnaire.
- Recalculer toute la fenêtre à chaque pas : on retombe à `O(nk)`.
- Oublier de mettre à jour la structure (compteurs, somme) **à la sortie** d'un élément.
- Se tromper de bord : la fenêtre `[g, d]` est inclusive, sa longueur vaut `d - g + 1`.

### Synthèse du chapitre 13

La **fenêtre glissante** maintient un intervalle contigu mis à jour en `O(1)` à chaque entrée et sortie ; chaque indice n'entrant et ne sortant qu'une fois, le coût amorti est `O(n)`. Elle exige une contrainte **monotone**. Retenez la fenêtre fixe, la fenêtre variable avec invariant, les compteurs pour les chaînes et la **file monotone** qui donne le maximum d'une fenêtre en `O(1)` amorti.

---

## 14. Sommes préfixes et tableaux de différences

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : construire un tableau de sommes préfixes et répondre à une somme d'intervalle en `O(1)` ; compter les sous-tableaux de somme donnée avec un dictionnaire ; étendre la technique à deux dimensions par inclusion-exclusion ; utiliser un tableau de différences pour des mises à jour d'intervalle en `O(1)` ; savoir quand passer à Fenwick ou à un arbre de segments.

### 14.1 Sommes préfixes

#### Définition

Pour un tableau `t` de `n` éléments, le **tableau des sommes préfixes** `P` est défini par `P[0] = 0` et `P[i] = t[0] + t[1] + … + t[i-1]`. Il a donc `n + 1` éléments. La somme de **n'importe quel intervalle** `t[l..r]` (bornes incluses) vaut

`somme(l, r) = P[r + 1] - P[l]`,

car `P[r+1]` contient tous les éléments jusqu'à `r` et on retranche ceux qui précèdent `l`.

```python
from itertools import accumulate

t = [3, 1, 4, 1, 5, 9]
P = [0] + list(accumulate(t))            # [0, 3, 4, 8, 9, 14, 23]

def somme_intervalle(l, r):              # somme de t[l..r] inclus
    return P[r + 1] - P[l]

print(somme_intervalle(1, 3))            # 1 + 4 + 1 = 6
```

**Complexité** : précalcul `O(n)`, puis chaque requête en `O(1)`, au lieu de `O(n)` par requête. C'est un compromis temps et espace (mémoire `O(n)`).

#### Sous-tableaux de somme `k` (avec valeurs négatives possibles)

**Idée.** La somme de `t[i..j]` vaut `P[j+1] - P[i]`. Elle vaut `k` exactement quand `P[i] = P[j+1] - k`. En parcourant le tableau, on dénombre, grâce à un dictionnaire, le nombre de préfixes précédents égaux à `somme_courante - k`.

```python
from collections import defaultdict

def nb_sous_tableaux_somme(t, k):
    vus = defaultdict(int)
    vus[0] = 1                           # le préfixe vide
    somme = total = 0
    for x in t:
        somme += x
        total += vus[somme - k]          # préfixes précédents tels que somme - préfixe = k
        vus[somme] += 1
    return total                         # O(n)

print(nb_sous_tableaux_somme([1, 1, 1], 2))   # 2
```

La même idée traite : plus long sous-tableau de somme `k`, sous-tableaux de somme divisible par `m` (on stocke les restes des préfixes), sous-tableaux avec autant de 0 que de 1 (on remplace les 0 par -1).

#### Version à deux dimensions

Pour une matrice, `P[i][j]` est la somme du rectangle de coins `(0, 0)` et `(i-1, j-1)`. On le construit par **inclusion-exclusion**, puis la somme d'un rectangle quelconque s'obtient en `O(1)`.

```python
def construire_prefixe_2d(m):
    h, l = len(m), len(m[0])
    P = [[0] * (l + 1) for _ in range(h + 1)]
    for i in range(h):
        for j in range(l):
            P[i + 1][j + 1] = m[i][j] + P[i][j + 1] + P[i + 1][j] - P[i][j]
    return P

def somme_rect(P, r1, c1, r2, c2):       # coins (r1, c1) et (r2, c2), inclusifs
    return P[r2 + 1][c2 + 1] - P[r1][c2 + 1] - P[r2 + 1][c1] + P[r1][c1]

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
P2 = construire_prefixe_2d(m)
print(somme_rect(P2, 1, 1, 2, 2))      # 5 + 6 + 8 + 9 = 28
```

La soustraction de `P[i][j]` dans la construction compense le fait que le rectangle commun a été compté deux fois ; dans la requête, on ajoute `P[r1][c1]` parce qu'il a été retranché deux fois.

#### Généralisations

Les préfixes fonctionnent pour toute opération **inversible** : somme, ou exclusif (XOR), produit modulaire (avec inverses), comptage. Pour un minimum ou un maximum (non inversibles), on utilise une table creuse ou un arbre de segments (chapitre 23).

### 14.2 Tableau de différences

#### Principe

Le **tableau de différences** `D` de `t` vérifie `D[i] = t[i] - t[i-1]` (avec `D[0] = t[0]`). C'est l'opération **inverse** de la somme préfixe : en cumulant `D`, on retrouve `t`.

Son utilité : pour appliquer **de nombreuses mises à jour d'intervalle** « ajouter `v` à `t[l..r]` », il suffit de faire `D[l] += v` et `D[r+1] -= v`, soit **`O(1)` par mise à jour**. On reconstruit ensuite `t` en une passe de cumul, en `O(n)`.

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

**Justification.** Ajouter `v` en `D[l]` fait que toutes les positions à partir de `l` voient `+v` lors du cumul ; retrancher `v` en `D[r+1]` annule cet effet à partir de `r+1`. Seule la plage `[l, r]` est donc affectée. Sans cette technique, `m` mises à jour coûteraient `O(m·n)`.

### 14.3 Applications

| Application | Technique |
| --- | --- |
| Somme ou moyenne d'un intervalle, nombreuses requêtes | Préfixes |
| Nombre d'occurrences d'une lettre dans `[l, r]` | Un tableau de préfixes par lettre |
| Réservations qui se chevauchent, covoiturage, capacité maximale | Différences (balayage) |
| Dessiner des rectangles sur une grille | Différences 2D |
| Sous-tableau de somme `k` | Préfixes et dictionnaire |
| Point d'équilibre (somme à gauche égale à somme à droite) | Préfixes |
| Produit de tous les éléments sauf un | Préfixes et suffixes de produits |

Si le tableau **change** entre les requêtes, préfixes et différences ne suffisent plus : on emploie un **arbre de Fenwick** ou un **arbre de segments** (chapitre 23).

### 14.4 Pièges fréquents

- Se tromper d'**indices** : `P` a `n + 1` éléments et la somme de `t[l..r]` vaut `P[r + 1] - P[l]`.
- Oublier le préfixe vide `P[0] = 0` (ou `vus[0] = 1` dans le dictionnaire) : les sous-tableaux commençant à l'indice 0 sont manqués.
- Utiliser des préfixes sur un tableau qui **change** entre les requêtes : le recalcul coûte `O(n)` ; prendre Fenwick ou un arbre de segments.
- Oublier `diff[r + 1] -= v` (ou la case supplémentaire en fin de tableau) dans le tableau de différences.

### Synthèse du chapitre 14

Les **sommes préfixes** donnent la somme d'un intervalle en `O(1)` après un précalcul linéaire ; avec un dictionnaire, elles comptent les sous-tableaux de somme donnée même avec des valeurs négatives. Le **tableau de différences** est l'opération inverse et permet des mises à jour d'intervalle en `O(1)`. Retenez la version 2D par inclusion-exclusion et la limite : ces outils supposent un tableau **figé**.

---

## 15. Recherche binaire sur la réponse

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : transformer un problème d'optimisation en problème de décision monotone ; écrire les deux modèles de recherche binaire (première et dernière valeur valide) ; choisir les bornes `bas` et `haut` ; traiter minimiser le maximum et maximiser le minimum ; effectuer une dichotomie sur les réels.

### 15.1 Principe

Au lieu de chercher un **indice** dans un tableau trié, on cherche **la meilleure valeur** `x` d'une grandeur (capacité, vitesse, distance, durée) dans un intervalle `[bas, haut]`, à condition de disposer d'une fonction de décision `est_valide(x)` **monotone** : si `x` est faisable, alors tout `x' ≥ x` l'est aussi (ou, symétriquement, tout `x' ≤ x`).

```text
x :       1   2   3   4   5   6   7   8
valide :  non non non oui oui oui oui oui    on cherche la PREMIÈRE valeur valide (4)
```

La suite des réponses `non, non, non, oui, oui, …` est triée au sens booléen : la recherche binaire s'y applique, sans que ce tableau soit jamais construit. Chaque test de `est_valide` élimine la moitié de l'intervalle des réponses possibles.

**Condition d'application.** Un problème d'optimisation (« trouver le plus petit `x` tel que… ») se transforme en problème de **décision** (« `x` convient-il ? ») plus facile à résoudre, dont la réponse est monotone en `x`. Le coût total vaut `O(log(intervalle) × coût de est_valide)`.

### 15.2 Modèle : plus petite valeur valide

```python
def plus_petite_valeur_valide(bas, haut, est_valide):
    while bas < haut:
        milieu = (bas + haut) // 2
        if est_valide(milieu):
            haut = milieu                # milieu est candidate : chercher plus petit
        else:
            bas = milieu + 1
    return bas                           # première valeur valide (suppose qu'elle existe dans [bas, haut])
```

**Invariant.** La réponse appartient toujours à `[bas, haut]`. L'intervalle diminue strictement à chaque tour, car `milieu < haut` (division entière par défaut) et on affecte soit `haut = milieu`, soit `bas = milieu + 1`.

Pour **maximiser** (dernière valeur valide), on utilise `milieu = (bas + haut + 1) // 2` (arrondi vers le haut, pour éviter une boucle infinie), puis `bas = milieu` si valide, et `haut = milieu - 1` sinon.

```python
def plus_grande_valeur_valide(bas, haut, est_valide):
    while bas < haut:
        milieu = (bas + haut + 1) // 2
        if est_valide(milieu):
            bas = milieu
        else:
            haut = milieu - 1
    return bas
```

### 15.3 Exemple : expédier des colis en D jours

**Problème.** Des colis de poids `p₁, …, pₙ` doivent être expédiés **dans l'ordre**, en au plus `D` jours ; chaque jour, un camion transporte des colis consécutifs dont le poids total ne dépasse pas sa capacité. Trouver la capacité minimale.

**Raisonnement.** Si une capacité `c` suffit, toute capacité plus grande suffit (monotonie). La capacité est au moins `max(p)` (il faut pouvoir porter le plus lourd) et au plus `sum(p)` (tout en un jour). Pour tester `c`, on simule en glouton : on remplit chaque jour autant que possible, et on compte les jours.

```python
def capacite_minimale(poids, D):
    def faisable(cap):
        jours, charge = 1, 0
        for p in poids:
            if charge + p > cap:
                jours += 1
                charge = 0
            charge += p
        return jours <= D

    return plus_petite_valeur_valide(max(poids), sum(poids), faisable)

print(capacite_minimale([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))   # 15
```

**Complexité** : `O(n · log(somme))`. Sans cette approche, il faudrait essayer toutes les façons de découper en `D` parties.

### 15.4 Exemple : vitesse minimale pour manger toutes les bananes

**Problème.** `n` piles de bananes ; à vitesse `v` bananes par heure, on mange une pile à la fois (en une heure par pile au plus). Trouver la plus petite vitesse permettant de finir en au plus `h` heures.

```python
from math import ceil

def vitesse_minimale(piles, heures):
    bas, haut = 1, max(piles)
    while bas < haut:                             # même modèle qu'en 15.2
        milieu = (bas + haut) // 2
        if sum(ceil(p / milieu) for p in piles) <= heures:
            haut = milieu
        else:
            bas = milieu + 1
    return bas

print(vitesse_minimale([3, 6, 7, 11], 8))     # 4
```

### 15.5 Exemple : maximiser la distance minimale

**Problème.** Placer `k` objets sur des positions triées `x₁ < … < xₙ` en **maximisant la plus petite distance** entre deux objets voisins.

**Raisonnement.** Si on peut respecter une distance minimale `d`, on peut respecter toute distance plus petite : la validité est décroissante en `d`, on cherche donc la dernière valeur valide. Le test est glouton : placer le premier objet, puis chaque suivant au premier emplacement à distance au moins `d`.

```python
def distance_minimale_maximale(positions, k):
    positions.sort()
    def faisable(d):
        compte, derniere = 1, positions[0]
        for x in positions[1:]:
            if x - derniere >= d:
                compte += 1
                derniere = x
        return compte >= k
    return plus_grande_valeur_valide(1, positions[-1] - positions[0], faisable)

print(distance_minimale_maximale([1, 2, 4, 8, 9], 3))     # 3 (positions 1, 4, 8)
```

### 15.6 Schémas fréquents

| Type de problème | Direction de recherche |
| --- | --- |
| **Minimiser le maximum** (capacité, charge, temps) | Valide, donc chercher à **gauche** (réduire) |
| **Maximiser le minimum** (distance minimale, résistance) | Valide, donc chercher à **droite** (augmenter) |
| Plus petite valeur satisfaisant une contrainte | `plus_petite_valeur_valide` |
| Plus grande valeur satisfaisant une contrainte | `plus_grande_valeur_valide` |

Signaux dans l'énoncé : « minimiser le maximum », « maximiser le minimum », « le plus petit `x` tel que… », avec une contrainte vérifiable par un parcours en `O(n)`.

### 15.7 Recherche binaire sur les réels

Quand la réponse est un réel, on ne peut pas tester chaque valeur : on effectue un nombre **fixe** d'itérations ou on s'arrête quand l'intervalle est plus petit que la précision voulue.

```python
def racine_carree(x, eps=1e-9):
    bas, haut = 0.0, max(1.0, x)
    for _ in range(100):                 # un nombre FIXE d'itérations évite les boucles infinies
        milieu = (bas + haut) / 2
        if milieu * milieu < x:
            bas = milieu
        else:
            haut = milieu
    return bas

print(round(racine_carree(2), 6))       # 1.414214
```

100 itérations suffisent à épuiser la précision d'un flottant double. Éviter `while haut - bas > eps` quand les nombres sont très grands : l'écart peut ne jamais passer sous `eps` à cause de la précision limitée des flottants.

### 15.8 Conseils

- Définir soigneusement **`bas`** et **`haut`** de sorte que la réponse y soit toujours contenue.
- Démontrer la **monotonie** de la fonction de décision (si on augmente la capacité, la faisabilité se conserve).
- La fonction de décision doit être en `O(n)` ou mieux, sinon le gain est perdu.
- Tester les cas limites : réponse égale à la borne basse ou haute, intervalle réduit à un point.
- Éviter la boucle infinie en choisissant l'arrondi du milieu cohérent avec la mise à jour des bornes.

### 15.9 Pièges fréquents

- Ne pas **démontrer la monotonie** de la fonction de décision : la dichotomie donne alors un résultat faux.
- Choisir un arrondi du milieu incohérent avec la mise à jour des bornes : **boucle infinie** (`bas = milieu` exige `(bas + haut + 1) // 2`).
- Prendre des bornes qui **n'encadrent pas** la réponse (par exemple une capacité inférieure au plus gros colis).
- Employer `while haut - bas > eps` sur des réels très grands : préférer un nombre fixe d'itérations.
- Écrire une fonction de décision plus lente que `O(n)` : le gain de la dichotomie est perdu.

### Synthèse du chapitre 15

La **recherche binaire sur la réponse** cherche la meilleure valeur d'une grandeur plutôt qu'un indice : on transforme « optimiser » en « décider » et, la décision étant monotone, on dichotomise pour un coût `O(log(plage) × coût du test)`. Retenez les deux modèles (première et dernière valeur valide), les schémas « minimiser le maximum » et « maximiser le minimum », la dichotomie sur les réels et l'importance des bornes.

---

## 16. Algorithmes de théorie des nombres

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : générer les nombres premiers avec le crible d'Ératosthène ; factoriser un entier et en déduire diviseurs, PGCD et PPCM ; calculer modulo `m` (congruences, exponentiation rapide, inverse modulaire par Fermat ou Euclide étendu) ; calculer des coefficients binomiaux modulo un premier ; utiliser l'indicatrice d'Euler et les restes chinois ; tester la primalité de grands nombres avec Miller-Rabin.

### 16.1 Crible d'Ératosthène

#### Principe

Le crible trouve **tous les nombres premiers inférieurs ou égaux à `n`**. On part d'un tableau de booléens tous à `True` ; pour chaque nombre premier `i` rencontré (non encore barré), on **barre tous ses multiples**. Les nombres restant non barrés sont premiers.

**Deux optimisations** justifiées :

- On ne parcourt que les `i` jusqu'à `√n` : un composé `m ≤ n` a un facteur premier `≤ √m ≤ √n`, donc il est barré avant.
- On commence à barrer à partir de `i²` : les multiples plus petits `i × k` (avec `k < i`) ont déjà été barrés par un facteur premier plus petit.

```python
def crible(n):
    est_premier = [True] * (n + 1)
    est_premier[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if est_premier[i]:
            for multiple in range(i * i, n + 1, i):      # on démarre à i^2
                est_premier[multiple] = False
    return [i for i, p in enumerate(est_premier) if p]

print(crible(30))    # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

**Complexité** : `O(n log log n)` en temps (la somme des `n/p` sur les premiers `p ≤ n` vaut `n log log n`), `O(n)` en espace.

#### Variantes

- **Crible linéaire** (`O(n)`) : chaque composé est barré exactement une fois, par son plus petit facteur premier ; il fournit aussi le tableau des **plus petits facteurs premiers** (`spf`).
- **Crible segmenté** : traite l'intervalle `[a, b]` par blocs pour réduire la mémoire.
- **Factorisation rapide avec `spf`** : après un crible des plus petits facteurs premiers, factoriser un nombre `m ≤ n` coûte `O(log m)` en divisant successivement par `spf[m]`.

### 16.2 Factorisation

Tout entier `n ≥ 2` s'écrit de façon **unique** (à l'ordre près) comme produit de nombres premiers : c'est le **théorème fondamental de l'arithmétique**.

```python
def factoriser(n):                         # O(sqrt(n))
    facteurs, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            facteurs[d] = facteurs.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:                              # le reste est premier
        facteurs[n] = facteurs.get(n, 0) + 1
    return facteurs

print(factoriser(360))       # {2: 3, 3: 2, 5: 1}
```

À partir de la factorisation `n = p₁^a₁ ··· p_k^a_k`, on obtient : le **nombre de diviseurs** `(a₁+1)···(a_k+1)`, la **somme des diviseurs** `∏ (p^(a+1) - 1)/(p - 1)`, le **PGCD** et **PPCM** (minimum et maximum des exposants). Pour des nombres de grande taille (plus de 10¹²), on utilise l'algorithme **rho de Pollard**.

### 16.3 Arithmétique modulaire

#### Congruences

On dit que `a ≡ b (mod m)` quand `m` divise `a - b`, c'est-à-dire quand `a` et `b` ont le même reste dans la division par `m`. Ces congruences sont compatibles avec l'addition, la soustraction et la multiplication :

`(a + b) mod m = ((a mod m) + (b mod m)) mod m`, de même pour `-` et `×`.

On peut donc réduire les résultats intermédiaires à chaque étape, ce qui évite les nombres énormes. Dans les énoncés, on demande souvent le résultat modulo `10⁹ + 7`, qui est premier. **La division n'est pas compatible** : on la remplace par la multiplication par l'**inverse modulaire**.

```python
MOD = 10**9 + 7
a, b = 10**12, 3 * 10**11

print((a + b) % MOD, (a * b) % MOD, (a - b) % MOD)
print((3 - 5) % MOD)        # 1000000005 : en Python, % renvoie un résultat >= 0 (pas en C, C++ ou Java)
```

#### Exponentiation rapide : `a^b mod m` en `O(log b)`

On décompose l'exposant en binaire et on élève au carré successivement : `a^b = ∏ a^(2^i)` pour les bits `i` de `b` valant 1.

```python
MOD = 10**9 + 7

def puissance_mod(a, b, m):
    resultat, a = 1, a % m
    while b:
        if b & 1:                       # bit courant égal à 1
            resultat = resultat * a % m
        a = a * a % m                   # a^(2^i) -> a^(2^(i+1))
        b >>= 1
    return resultat

print(puissance_mod(2, 10**18, MOD) == pow(2, 10**18, MOD))   # True : pow(a, b, m) est l'équivalent intégré
```

#### Inverse modulaire

L'**inverse** de `a` modulo `m` est un entier `x` tel que `a·x ≡ 1 (mod m)`. Il existe si et seulement si `pgcd(a, m) = 1`.

| Méthode | Condition | Principe |
| --- | --- | --- |
| **Petit théorème de Fermat** | `m` **premier**, `a` non multiple de `m` | `a^(m-1) ≡ 1`, donc l'inverse est `a^(m-2) mod m` |
| **Euclide étendu** | `pgcd(a, m) = 1` | Résout `a·x + m·y = 1` (identité de Bézout) |
| **Fonction intégrée** | `pgcd(a, m) = 1` | `pow(a, -1, m)` (Python 3.8 et suivants) |

```python
print(pow(3, -1, 11))        # 4, car 3 x 4 = 12 = 1 (mod 11)

def euclide_etendu(a, b):    # renvoie (g, x, y) avec a*x + b*y = g = pgcd(a, b)
    if b == 0:
        return a, 1, 0
    g, x, y = euclide_etendu(b, a % b)
    return g, y, x - (a // b) * y

print(euclide_etendu(240, 46))    # (2, -9, 47) car 240 * (-9) + 46 * 47 = 2
```

**Dérivation d'Euclide étendu.** Si `g = b·x' + (a mod b)·y'` et `a mod b = a - (a // b)·b`, alors `g = a·y' + b·(x' - (a // b)·y')`. D'où le retour `(g, y', x' - (a // b)·y')`.

#### Coefficients binomiaux modulo un premier

`C(n, k) = n! / (k! (n-k)!)`. On précalcule les factorielles et leurs inverses pour répondre à chaque requête en `O(1)`.

```python
MOD = 10**9 + 7

def precalculer_factorielles(n, m=MOD):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % m
    inv = [1] * (n + 1)
    inv[n] = pow(fact[n], -1, m)
    for i in range(n, 0, -1):
        inv[i - 1] = inv[i] * i % m          # 1/(i-1)! = i / i!
    return fact, inv

def C(n, k, fact, inv, m=MOD):
    return 0 if k < 0 or k > n else fact[n] * inv[k] % m * inv[n - k] % m

fact, inv = precalculer_factorielles(1000)
print(C(10, 3, fact, inv))        # 120
```

### 16.4 Autres outils

| Outil | Rôle |
| --- | --- |
| **Indicatrice d'Euler** `φ(n)` | Nombre d'entiers de `1` à `n` premiers avec `n` ; théorème d'Euler : `a^φ(m) ≡ 1 (mod m)` si `pgcd(a, m) = 1` |
| **Théorème des restes chinois** | Un système de congruences `x ≡ aᵢ (mod mᵢ)` avec `mᵢ` deux à deux premiers entre eux admet une solution unique modulo le produit des `mᵢ` |
| **Exponentiation de matrices** | Calcule une récurrence linéaire d'ordre `k` (Fibonacci) en `O(k³ log n)` |
| **Nombres de Catalan, de Stirling, inclusion-exclusion** | Dénombrements |

```python
def phi(n):
    r, d = n, 2
    while d * d <= n:
        if n % d == 0:
            while n % d == 0:
                n //= d
            r -= r // d                # multiplier par (1 - 1/d)
        d += 1
    if n > 1:
        r -= r // n
    return r

print(phi(36))                    # 12
```

La formule `φ(n) = n ∏ (1 - 1/p)` (sur les facteurs premiers `p` de `n`) justifie le code.

### 16.5 Test de primalité de Miller-Rabin

Pour les très grands nombres, le test par divisions successives est trop lent. **Miller-Rabin** est un test **probabiliste** rapide, **déterministe** pour tous les entiers inférieurs à `3,3 × 10²⁴` environ avec l'ensemble de bases ci-dessous (donc en particulier pour tout entier 64 bits).

**Principe.** Si `n` est premier impair et `n - 1 = 2^s · d` avec `d` impair, alors pour toute base `a` non multiple de `n`, soit `a^d ≡ 1`, soit `a^(2^r · d) ≡ -1 (mod n)` pour un `r` tel que `0 ≤ r < s`. Si une base viole cette condition (un **témoin**), `n` est certainement composé. Un composé qui passe le test pour la base `a` est dit **pseudo-premier fort** ; les nombres de Carmichael (comme 561) trompent le test de Fermat simple mais pas Miller-Rabin avec plusieurs bases.

```python
def miller_rabin(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False                  # témoin de composition trouvé
    return True

print(miller_rabin(2**61 - 1), miller_rabin(561))   # True False
```

**Complexité** : `O(k · log³ n)` pour `k` bases, très inférieure à `O(√n)`. Applications : cryptographie (génération de clés RSA), factorisation.

### 16.6 Pièges fréquents

- Utiliser `%` comme en C : en Python le reste est toujours positif, mais dans d'autres langages `(a - b) % m` peut être **négatif**.
- Diviser modulo `m` : la division n'est pas compatible, il faut **multiplier par l'inverse** (qui n'existe que si `pgcd(a, m) = 1`).
- Appliquer le petit théorème de Fermat avec un module **non premier**.
- Oublier de réduire les résultats intermédiaires modulo `m` à chaque étape, ou de commencer le crible à `2i` au lieu de `i²`.
- Factoriser ou tester la primalité par divisions pour des nombres de plus de 10¹² : prendre Pollard rho et Miller-Rabin.

### Synthèse du chapitre 16

Le **crible** produit tous les premiers jusqu'à `n` en `O(n log log n)` ; la **factorisation** s'obtient en `O(√n)` par divisions. L'**arithmétique modulaire** réduit les nombres à chaque étape ; l'**exponentiation rapide** calcule `aᵇ mod m` en `O(log b)` ; l'**inverse modulaire** vient de Fermat (module premier) ou d'Euclide étendu. Retenez l'indicatrice d'Euler, les restes chinois, les binomiaux avec factorielles précalculées et le test probabiliste de **Miller-Rabin**.

---

## 17. Hachage

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : expliquer le fonctionnement d'une table de hachage (fonction de hachage, collisions, facteur de charge) ; utiliser `dict`, `set` et `collections` (`Counter`, `defaultdict`) ; résoudre deux-somme, regroupement d'anagrammes et plus longue suite consécutive en un passage ; définir `__hash__` de façon cohérente avec `__eq__` ; connaître les usages du hachage (cryptographie, filtres de Bloom, hachage roulant).

### 17.1 Principe

Une **fonction de hachage** `h` transforme une **clé** (chaîne, nombre, tuple) en un entier servant d'**indice** dans un tableau, la **table de hachage**. Pour une clé `k`, on range la valeur à la case `h(k) mod taille`. L'accès, l'insertion et la suppression sont alors en **`O(1)` en moyenne**, sans parcourir la structure.

```text
clé "Alice" --hash()--> 8372649 --mod taille--> case 5 :  [ ... | ... | "Alice" -> 30 | ... ]
```

Propriétés d'une bonne fonction de hachage : **déterministe** (même clé, même valeur), **rapide** à calculer, **répartition uniforme** des valeurs (peu de clés par case).

### 17.2 Les structures en Python

```python
d = {}                          # dictionnaire (table de hachage)
d["pomme"] = 3                  # insertion ou mise à jour : O(1) en moyenne
print(d["pomme"])               # lecture : 3 (KeyError si absent)
print(d.get("poire", 0))        # lecture avec valeur par défaut
print("pomme" in d)             # test d'appartenance : O(1)
del d["pomme"]                  # suppression

ensemble = {1, 2, 3}            # set : valeurs uniques
print(2 in ensemble)            # O(1)
print(ensemble | {4}, ensemble & {2, 9}, ensemble - {1})   # union, intersection, différence
```

Les clés doivent être **hachables**, donc **immuables** : `int`, `str`, `tuple` de valeurs hachables, `frozenset` conviennent ; `list`, `dict` et `set` ne le sont pas (leur modification changerait leur hachage). Depuis Python 3.7, un `dict` **conserve l'ordre d'insertion**.

### 17.3 Gestion des collisions

Deux clés différentes peuvent donner le même indice : c'est une **collision**. Elle est inévitable (principe des tiroirs : plus de clés possibles que de cases).

| Méthode | Principe |
| --- | --- |
| **Chaînage** | Chaque case contient une liste de paires ; on parcourt la liste en cas de collision |
| **Adressage ouvert** | On cherche une autre case libre : sondage linéaire (case suivante), quadratique, double hachage. C'est la méthode du `dict` de CPython |
| **Redimensionnement** | Quand le **facteur de charge** (éléments divisé par nombre de cases) dépasse un seuil, on agrandit le tableau et on **rehache** toutes les clés ; coût amorti `O(1)` par insertion |

Le facteur de charge `α = n/m` gouverne la performance : avec chaînage, la longueur moyenne d'une chaîne est `α`, donc `O(1 + α)` par opération ; on garde `α` borné (par exemple inférieur à 2/3 en adressage ouvert).

### 17.4 Complexité

| Opération | Moyen | Pire cas |
| --- | --- | --- |
| Insertion, recherche, suppression | **`O(1)`** | `O(n)` (toutes les clés en collision) |
| Parcours | `O(n)` | `O(n)` |
| Mémoire | `O(n)` | `O(n)` |

> **Sécurité et compétition.** Python **randomise** le hachage des chaînes à chaque lancement (`PYTHONHASHSEED`) pour empêcher les attaques par collisions volontaires. Sur des plateformes de compétition, des jeux de tests « anti-hash » peuvent dégrader un `dict` basé sur des entiers : on mélange les clés (XOR avec une constante aléatoire) si nécessaire.

### 17.5 Problèmes classiques

#### Deux sommes (tableau non trié)

```python
def deux_somme(t, cible):
    vus = {}                                   # valeur -> indice
    for i, x in enumerate(t):
        if cible - x in vus:
            return (vus[cible - x], i)
        vus[x] = i
    return None                                # O(n)

print(deux_somme([2, 7, 11, 15], 9))   # (0, 1)
```

Pour chaque élément `x`, on cherche son **complément** `cible - x` parmi ceux déjà vus : un seul passage, au lieu de deux boucles imbriquées.

#### Regrouper les anagrammes

```python
from collections import defaultdict

def grouper_anagrammes(mots):
    groupes = defaultdict(list)
    for m in mots:
        groupes["".join(sorted(m))].append(m)      # clé canonique : lettres triées
    return list(groupes.values())

print(grouper_anagrammes(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

Idée générale : trouver une **forme canonique** commune à tous les éléments équivalents, et s'en servir comme clé.

#### Plus longue suite consécutive

```python
def plus_longue_suite(t):
    ensemble, meilleur = set(t), 0
    for x in ensemble:
        if x - 1 not in ensemble:               # x est le début d'une suite
            longueur = 1
            while x + longueur in ensemble:
                longueur += 1
            meilleur = max(meilleur, longueur)
    return meilleur                              # O(n)

print(plus_longue_suite([100, 4, 200, 1, 3, 2]))   # 4 (1, 2, 3, 4)
```

La complexité est linéaire car chaque élément n'est parcouru que depuis le début de sa suite.

#### Autres problèmes

Premier caractère unique, détection de doublons, **détection de cycle** (ensemble de sommets visités), **mémoïsation** (dictionnaire de résultats), sous-tableau de somme `k` (préfixes et dictionnaire), cache **LRU** (`OrderedDict`).

### 17.6 Outils du module `collections`

| Outil | Rôle |
| --- | --- |
| `Counter` | Compter les occurrences (`Counter("abracadabra")`, `.most_common(3)`) |
| `defaultdict(list)`, `defaultdict(int)` | Valeur par défaut créée automatiquement à la première lecture |
| `OrderedDict` | Rarement nécessaire (les `dict` gardent l'ordre) ; utile pour `move_to_end` (LRU) |
| `frozenset` | Ensemble immuable, utilisable comme clé |

### 17.7 Hachage d'objets et autres usages

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, autre):
        return (self.x, self.y) == (autre.x, autre.y)
    def __hash__(self):
        return hash((self.x, self.y))       # doit être cohérent avec __eq__
```

**Règle** : deux objets égaux doivent avoir le même hachage ; un objet utilisé comme clé ne doit pas voir sa valeur de hachage changer.

Autres usages : **hachage cryptographique** (SHA-256 : vérification d'intégrité ; pas pour les mots de passe, pour lesquels on emploie bcrypt, scrypt ou argon2), **filtres de Bloom** (appartenance probabiliste avec faux positifs mais sans faux négatifs), **hachage roulant** (Rabin-Karp, chapitre 24), **hachage cohérent** (répartition de données dans des systèmes distribués).

### 17.8 Bonnes pratiques

- Utiliser `set` et `dict` pour les **tests d'appartenance** et les **comptages**.
- Choisir des **clés immuables** ; définir `__hash__` de façon cohérente avec `__eq__`.
- Ne pas se fier à l'ordre d'un `set` ; seul le `dict` garantit l'ordre d'insertion.
- Ne pas modifier un dictionnaire pendant qu'on le parcourt.

### 17.9 Pièges fréquents

- Utiliser un objet **mutable** (`list`, `dict`, `set`) comme clé : il n'est pas hachable ; prendre un `tuple` ou un `frozenset`.
- Définir `__eq__` sans `__hash__` cohérent : deux objets égaux doivent avoir le même hachage.
- Se fier à l'**ordre d'un `set`** : seul le `dict` garantit l'ordre d'insertion.
- Modifier un dictionnaire **pendant qu'on le parcourt**.
- Oublier que le pire cas du hachage est `O(n)` et que des entrées conçues pour provoquer des collisions existent en compétition.

### Synthèse du chapitre 17

Une **table de hachage** range chaque clé à l'indice `h(k) mod taille` et offre insertion, recherche et suppression en `O(1)` **en moyenne** ; les collisions se gèrent par chaînage ou adressage ouvert, et le redimensionnement garde le facteur de charge borné. Beaucoup de problèmes se résolvent en un passage avec un dictionnaire de « ce qu'on a déjà vu » (complément, forme canonique, début de suite). Retenez `Counter`, `defaultdict` et la cohérence entre `__hash__` et `__eq__`.

---

# Partie III — Niveau avancé

---

## 18. Programmation dynamique

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : reconnaître une sous-structure optimale et des sous-problèmes chevauchants ; appliquer la démarche en cinq étapes (état, transition, base, ordre, réponse) ; écrire une solution descendante (mémoïsation) et ascendante (tabulation) ; résoudre rendu de monnaie, sac à dos, LIS, LCS, distance d'édition et TSP par masque de bits ; reconstituer la solution et réduire la mémoire.

### 18.1 Principe

La **programmation dynamique** (DP, *dynamic programming*) résout un problème en le décomposant en **sous-problèmes qui se chevauchent**, dont on **mémorise** les résultats pour ne calculer chacun qu'une seule fois. Le mot « programmation » est ici à prendre au sens de « planification » (méthode introduite par Richard Bellman dans les années 1950), pas de code.

Deux propriétés doivent être vérifiées :

1. **Sous-structure optimale** : une solution optimale du problème se construit à partir de solutions optimales de sous-problèmes.
2. **Sous-problèmes chevauchants** : les mêmes sous-problèmes réapparaissent de nombreuses fois dans la décomposition récursive. S'ils sont indépendants et distincts, il s'agit de diviser pour régner, pas de DP.

```text
fib(5)
 |- fib(4)
 |   |- fib(3)     <- calculé plusieurs fois sans mémoïsation
 |   `- fib(2)
 `- fib(3)           <- recalculé
```

En dénombrant les **états distincts** du problème et le coût de calcul de chacun, on obtient la complexité : `nombre d'états × coût de transition`.

### 18.2 Démarche en cinq étapes

| Étape | Question à se poser |
| --- | --- |
| 1. **État** | Que représente `dp[i]` (ou `dp[i][j]`) ? Quels paramètres décrivent entièrement un sous-problème ? |
| 2. **Transition** | Comment `dp[i]` se calcule-t-il à partir d'états plus petits ? (la **récurrence**) |
| 3. **Cas de base** | Quelles sont les valeurs initiales évidentes ? |
| 4. **Ordre de calcul** | Dans quel ordre remplir le tableau pour que les dépendances soient prêtes ? |
| 5. **Réponse** | Quelle case contient le résultat final ? |

La difficulté se concentre sur l'étape 1 : choisir un état suffisamment riche pour que la transition soit possible, sans qu'il y ait trop d'états.

### 18.3 Descendante (mémoïsation) et ascendante (tabulation)

|  | **Top-down** (mémoïsation) | **Bottom-up** (tabulation) |
| --- | --- | --- |
| Principe | Récursion avec un cache des résultats | Boucles remplissant un tableau des petits aux grands sous-problèmes |
| Avantages | Facile à écrire à partir de la récurrence ; ne calcule que les états nécessaires | Pas de récursion (donc pas de limite de pile) ; optimisation de mémoire possible |
| Inconvénients | Surcoût de la récursion ; profondeur limitée en Python | Il faut identifier l'ordre de calcul |

```python
from functools import cache

# Top-down
@cache
def escaliers(n):               # nombre de façons de monter n marches en pas de 1 ou 2
    return 1 if n <= 1 else escaliers(n - 1) + escaliers(n - 2)

# Bottom-up, avec mémoire O(1)
def escaliers_iteratif(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

print(escaliers(10), escaliers_iteratif(10))     # 89 89
```

La **réduction de mémoire** est possible quand `dp[i]` ne dépend que d'un petit nombre d'états précédents : on ne conserve que ceux-là (ici deux variables au lieu d'un tableau).

### 18.4 Problèmes à une dimension

#### Rendu de monnaie (nombre minimum de pièces)

**État** : `dp[m]` = nombre minimal de pièces pour rendre exactement `m`. **Transition** : `dp[m] = 1 + min(dp[m - p])` pour chaque pièce `p ≤ m`. **Base** : `dp[0] = 0`.

```python
def rendu_monnaie(pieces, montant):
    INF = float("inf")
    dp = [0] + [INF] * montant
    for m in range(1, montant + 1):
        for p in pieces:
            if p <= m and dp[m - p] + 1 < dp[m]:
                dp[m] = dp[m - p] + 1
    return dp[montant] if dp[montant] != INF else -1

print(rendu_monnaie([1, 3, 4], 6))               # 2 (3 + 3)
```

Complexité `O(montant × nombre de pièces)`. Pour **compter** le nombre de façons (et non le minimum), on remplace le min par une somme, en parcourant les pièces dans la boucle **externe** pour ne pas compter deux fois la même combinaison dans des ordres différents.

#### Voleur de maisons (*House Robber*)

On ne peut pas cambrioler deux maisons adjacentes. **État** : `prend` (meilleur gain en prenant la maison courante) et `ignore` (meilleur gain en ne la prenant pas).

```python
def voleur(maisons):
    prend, ignore = 0, 0
    for argent in maisons:
        prend, ignore = ignore + argent, max(prend, ignore)
    return max(prend, ignore)

print(voleur([2, 7, 9, 3, 1]))       # 12 (2 + 9 + 1)
```

#### Sous-tableau de somme maximale (Kadane)

**État** : `courant` = meilleure somme d'un sous-tableau **se terminant** à l'indice courant. **Transition** : soit on prolonge le précédent, soit on repart de zéro : `courant = max(x, courant + x)`.

```python
def kadane(t):
    meilleur = courant = t[0]
    for x in t[1:]:
        courant = max(x, courant + x)
        meilleur = max(meilleur, courant)
    return meilleur                              # O(n)

print(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6
```

#### Plus longue sous-suite croissante (LIS)

Version DP classique en `O(n²)` : `dp[i] = 1 + max(dp[j])` pour `j < i` avec `t[j] < t[i]`. Version `O(n log n)` : on maintient `queues[k]`, le plus petit élément terminal possible d'une sous-suite croissante de longueur `k+1` ; ce tableau est toujours croissant, ce qui permet une recherche binaire.

```python
from bisect import bisect_left

def lis(t):
    queues = []
    for x in t:
        i = bisect_left(queues, x)         # première position avec queues[i] >= x
        if i == len(queues):
            queues.append(x)               # x prolonge la plus longue sous-suite
        else:
            queues[i] = x                  # x améliore un terminal
    return len(queues)

print(lis([10, 9, 2, 5, 3, 7, 101, 18]))   # 4 (par exemple 2, 3, 7, 18)
```

Attention : `queues` n'est pas la sous-suite elle-même, mais seulement un outil donnant sa longueur.

#### Autres problèmes à une dimension

Partition en sous-ensembles de même somme (booléen `dp[s]`), découpage de tige, décodage de messages, mots d'un dictionnaire (segmentation d'une chaîne), coût minimal pour monter un escalier.

### 18.5 Problèmes à deux dimensions

#### Sac à dos 0/1

**Problème.** Objets de poids `pᵢ` et de valeur `vᵢ` ; capacité `C` ; chaque objet est pris **au plus une fois** ; maximiser la valeur totale.

**État** : `dp[i][c]` = valeur maximale en utilisant les `i` premiers objets avec capacité `c`. **Transition** : `dp[i][c] = max(dp[i-1][c], dp[i-1][c - pᵢ] + vᵢ)` (ne pas prendre ou prendre l'objet `i`).

Comme chaque ligne ne dépend que de la précédente, on compresse en un seul tableau en parcourant la capacité **de la droite vers la gauche**, pour ne jamais utiliser deux fois le même objet :

```python
def sac_a_dos(objets, capacite):                 # objets : (poids, valeur)
    dp = [0] * (capacite + 1)
    for poids, valeur in objets:
        for c in range(capacite, poids - 1, -1):     # parcours DÉCROISSANT
            dp[c] = max(dp[c], dp[c - poids] + valeur)
    return dp[capacite]

print(sac_a_dos([(1, 1), (3, 4), (4, 5), (5, 7)], 7))   # 9
```

**Complexité** : `O(n × C)` en temps, `O(C)` en mémoire. Cette complexité est **pseudo-polynomiale** : polynomiale en la valeur numérique de `C`, mais exponentielle en sa taille en bits. Le problème de décision reste NP-complet. Avec un parcours **croissant**, on obtiendrait le sac à dos **non borné** (chaque objet en nombre illimité).

#### Plus longue sous-séquence commune (LCS)

**État** : `dp[i][j]` = longueur de la LCS de `a[:i]` et `b[:j]`. **Transition** : si `a[i-1] == b[j-1]`, `dp[i][j] = dp[i-1][j-1] + 1` ; sinon `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

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

`O(n × m)` en temps et en espace. Distinguer la **sous-séquence** (éléments non nécessairement contigus) de la **sous-chaîne** (contiguë).

#### Distance d'édition (Levenshtein)

Nombre minimal d'opérations (insertion, suppression, substitution d'un caractère) pour transformer `a` en `b`.

```python
def distance_edition(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i                                 # supprimer i caractères
    for j in range(m + 1):
        dp[0][j] = j                                 # insérer j caractères
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cout = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,         # suppression
                           dp[i][j - 1] + 1,         # insertion
                           dp[i - 1][j - 1] + cout)  # substitution ou égalité
    return dp[n][m]

print(distance_edition("kitten", "sitting"))         # 3
```

Applications : correcteurs orthographiques, bio-informatique (alignement de séquences), comparaison de fichiers (`diff`).

#### Chemins dans une grille

```python
def nb_chemins(lignes, colonnes):                    # déplacements vers la droite ou le bas
    dp = [[1] * colonnes for _ in range(lignes)]
    for i in range(1, lignes):
        for j in range(1, colonnes):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]

print(nb_chemins(3, 7))             # 28
```

On adapte facilement : obstacles (`dp = 0` sur les cases bloquées), coût minimal (`min` au lieu de la somme), grille avec poids.

#### Autres classiques

Plus longue sous-chaîne palindromique, **produit de chaînes de matrices** (DP sur intervalles, `O(n³)`), partition en deux sous-ensembles de même somme, découpage de tige, **plus grand carré de 1**, coût minimal de chemin, **DP sur les arbres** (état = sommet, combinaison des états des enfants), **DP sur les intervalles** (`dp[i][j]` pour le segment `i..j`), **DP par chiffres** (compter les entiers d'un intervalle ayant une propriété).

### 18.6 DP avec masque de bits

Pour des ensembles de **petite taille** (`n` d'environ 20 au plus), un entier représente un **sous-ensemble** : le bit `i` vaut 1 si l'élément `i` appartient à l'ensemble. Le nombre d'états est alors `2ⁿ`.

#### Voyageur de commerce (TSP)

**Problème.** Visiter toutes les villes exactement une fois et revenir au départ, en minimisant la distance totale. **État** : `dp[masque][i]` = coût minimal d'un chemin partant de la ville 0, ayant visité exactement les villes de `masque` et finissant en `i`.

```python
def tsp(dist):
    n = len(dist)
    INF = float("inf")
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0                                     # départ en 0, masque = {0}
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

distances = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
print(tsp(distances))                 # 80
```

Complexité `O(n² · 2ⁿ)` (algorithme de Held-Karp), contre `O(n!)` pour la force brute. Même schéma pour l'affectation de tâches, la couverture d'ensemble minimale, les « sous-ensembles de sous-ensembles » (`O(3ⁿ)`).

### 18.7 Reconstituer la solution

La table `dp` donne la **valeur** optimale, pas la solution. Pour la retrouver, on conserve une table `parent[...]` indiquant **quel choix** a donné l'optimum de chaque état, puis on **remonte** depuis l'état final jusqu'à l'état initial. Alternative : refaire le calcul à rebours en cherchant, à chaque état, la transition qui a produit sa valeur.

```python
def rendu_monnaie_pieces(pieces, montant):
    INF = float("inf")
    dp, choix = [0] + [INF] * montant, [0] * (montant + 1)
    for m in range(1, montant + 1):
        for p in pieces:
            if p <= m and dp[m - p] + 1 < dp[m]:
                dp[m], choix[m] = dp[m - p] + 1, p
    rendu = []
    while montant > 0 and choix[montant]:
        rendu.append(choix[montant])
        montant -= choix[montant]
    return rendu

print(rendu_monnaie_pieces([1, 3, 4], 6))    # [3, 3]
```

### 18.8 Comparaison avec les autres approches

|  | DP | Glouton | Retour sur trace |
| --- | --- | --- | --- |
| Sous-problèmes | Mémorisés | Un seul chemin | Souvent recalculés |
| Garantit l'optimum | Oui (sous-structure optimale) | Seulement avec preuve | Oui (exhaustif) |
| Coût | Polynomial en nombre d'états | Très faible | Exponentiel |

### 18.9 Conseils

- Écrire d'abord la **récurrence** en langage mathématique et les cas de base, puis coder.
- Commencer par la version **mémoïsée**, plus naturelle ; passer à la tabulation si nécessaire.
- **Réduire la mémoire** si `dp[i]` ne dépend que de la ligne précédente.
- Surveiller la **limite de récursion** en Python (`sys.setrecursionlimit` ou version itérative).
- Tester contre une version par force brute sur de petites entrées.
- Entraînement conseillé : Fibonacci, escaliers, voleur, rendu de monnaie, LIS, LCS, distance d'édition, sac à dos, TSP, ordonnancement pondéré de tâches.

### 18.10 Pièges fréquents

- Choisir un **état trop pauvre** pour que la transition soit possible, ou trop riche (trop d'états).
- Parcourir la capacité dans le **mauvais sens** dans le sac à dos compressé (décroissant pour 0/1, croissant pour non borné).
- Compter des **permutations** au lieu de combinaisons dans le rendu de monnaie (boucle externe sur les pièces).
- Oublier un **cas de base** ou la valeur « impossible » (`inf`).
- Confondre sous-séquence (non contiguë) et sous-chaîne (contiguë), ou dépasser la limite de récursion en version descendante.
- Prendre la complexité **pseudo-polynomiale** du sac à dos pour une complexité polynomiale.

### Synthèse du chapitre 18

La **programmation dynamique** mémorise les résultats de sous-problèmes qui se chevauchent ; sa complexité est (nombre d'états) × (coût d'une transition). Retenez les cinq étapes, le choix entre **mémoïsation** et **tabulation**, la réduction de mémoire quand `dp[i]` ne dépend que de peu d'états, la reconstruction par table de parents et les problèmes de référence : Kadane, LIS, sac à dos, LCS, distance d'édition, chemins en grille, DP par masques de bits (TSP en `O(n²·2ⁿ)`).

---

## 19. Algorithmes sur les graphes

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : maîtriser le vocabulaire des graphes (orienté, pondéré, chemin, cycle, connexe, arbre, DAG, biparti) ; choisir une représentation (liste d'adjacence, matrice, liste d'arêtes) ; écrire BFS et DFS et en déduire composantes, cycles et bipartition ; effectuer un tri topologique ; construire un arbre couvrant minimal par Kruskal (avec Union-Find) ou Prim.

### 19.1 Vocabulaire et définitions

Un **graphe** `G = (V, E)` est formé d'un ensemble `V` de **sommets** (ou nœuds) et d'un ensemble `E` d'**arêtes** reliant des paires de sommets. On note `V = |V|` et `E = |E|` dans les complexités.

| Notion | Définition |
| --- | --- |
| **Graphe non orienté** | Les arêtes sont des paires non ordonnées `{u, v}` ; la relation est symétrique |
| **Graphe orienté** | Les arêtes (ou **arcs**) sont des couples `(u, v)` ; `u` est la source, `v` la destination |
| **Pondéré** | Chaque arête porte un **poids** (coût, distance, capacité) |
| **Voisins, degré** | Les voisins de `u` sont les sommets adjacents ; `deg(u)` est leur nombre (degré entrant et sortant pour un graphe orienté). Dans un graphe non orienté, la somme des degrés vaut `2E` |
| **Chemin** | Suite de sommets consécutivement reliés ; sa **longueur** est le nombre d'arêtes (ou la somme des poids) |
| **Cycle** | Chemin non vide qui revient à son point de départ |
| **Connexe** | Non orienté : il existe un chemin entre tout couple de sommets |
| **Arbre** | Graphe non orienté connexe et sans cycle : `E = V - 1` |
| **DAG** | Graphe orienté acyclique (*directed acyclic graph*) |
| **Creux, dense** | Creux si `E` est de l'ordre de `V` ; dense si `E` est de l'ordre de `V²` |
| **Biparti** | Les sommets se répartissent en deux groupes sans arête interne à un groupe |

Exemples de modélisations : réseau routier (sommets : carrefours, arêtes : routes), réseaux sociaux, dépendances entre tâches (DAG), grille de jeu (sommets : cases), états d'un puzzle (sommets : configurations, arêtes : coups).

### 19.2 Représentation

| Représentation | Mémoire | Test d'arête `(u, v)` | Parcourir les voisins de `u` | Quand l'utiliser |
| --- | --- | --- | --- | --- |
| **Liste d'adjacence** | `O(V + E)` | `O(deg(u))` | **`O(deg(u))`** | Graphes **creux** (le cas le plus courant) |
| **Matrice d'adjacence** | `O(V²)` | **`O(1)`** | `O(V)` | Graphes **denses** ou petits `V` ; Floyd-Warshall |
| **Liste d'arêtes** | `O(E)` | `O(E)` | `O(E)` | Kruskal, Bellman-Ford |

```python
from collections import defaultdict

graphe = defaultdict(list)
for u, v in [(0, 1), (0, 2), (1, 3), (2, 3)]:
    graphe[u].append(v)
    graphe[v].append(u)                    # non orienté : arête dans les deux sens

# Pondéré : graphe[u].append((v, poids))
```

### 19.3 Parcours en largeur (BFS)

**Principe.** À partir d'une source, on explore tous les sommets à distance 1, puis ceux à distance 2, etc., en utilisant une **file**. La **première fois** qu'un sommet est atteint, c'est par un plus court chemin en **nombre d'arêtes**. On marque les sommets dès qu'on les met dans la file pour ne jamais les traiter deux fois.

```python
from collections import deque

def bfs(graphe, source):
    distance = {source: 0}
    file = deque([source])
    while file:
        u = file.popleft()
        for v in graphe[u]:
            if v not in distance:                # pas encore découvert
                distance[v] = distance[u] + 1
                file.append(v)
    return distance                              # O(V + E)

g_demo = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
print(bfs(g_demo, 0))                           # {0: 0, 1: 1, 2: 1, 3: 2}
```

**Complexité** `O(V + E)` : chaque sommet est mis en file une fois, chaque arête examinée une fois (deux dans un graphe non orienté). **Correction** : la file contient à tout instant des sommets de distance `d` suivis de sommets de distance `d + 1`, ce qui garantit que les distances sont découvertes en ordre croissant.

Pour retrouver le chemin, on mémorise le **parent** de chaque sommet. En grille, le voisinage est donné par les quatre (ou huit) directions.

### 19.4 Parcours en profondeur (DFS)

**Principe.** On explore le plus loin possible le long d'un chemin avant de revenir en arrière (pile ou récursion).

```python
def dfs(graphe, source):
    visites, ordre = set(), []
    pile = [source]                         # version itérative : pas de limite de récursion
    while pile:
        u = pile.pop()
        if u in visites:
            continue
        visites.add(u)
        ordre.append(u)
        pile.extend(reversed(graphe[u]))
    return ordre                            # O(V + E)

def dfs_recursif(graphe, u, visites):
    visites.add(u)
    for v in graphe[u]:
        if v not in visites:
            dfs_recursif(graphe, v, visites)

g_demo = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
print(dfs(g_demo, 0))                     # [0, 1, 3, 2]
visites = set()
dfs_recursif(g_demo, 0, visites)
print(sorted(visites))                    # [0, 1, 2, 3]
```

#### Dates de début et de fin, classification des arêtes

En numérotant les sommets à l'**entrée** (date de découverte) et à la **sortie** (date de fin de traitement) du DFS, on classe les arêtes d'un graphe orienté : **arête d'arbre** (vers un sommet nouveau), **arête arrière** (vers un ancêtre encore « en cours »), **arête avant** (vers un descendant déjà traité), **arête transverse** (vers un sommet d'une autre branche déjà traité). Un graphe orienté est **acyclique si et seulement s'il n'a aucune arête arrière**. Ces dates fondent le tri topologique et les composantes fortement connexes (chapitre 21).

|  | BFS | DFS |
| --- | --- | --- |
| Structure | File | Pile ou récursion |
| Plus court chemin (non pondéré) | **Oui** | Non |
| Usages typiques | Distances, niveaux, plus court chemin en grille | Composantes connexes, cycles, tri topologique, labyrinthes, SCC |
| Mémoire | Peut atteindre `O(V)` (grande largeur) | `O(profondeur)` |

#### Applications

- **Composantes connexes** : on lance un parcours depuis chaque sommet non encore visité ; chaque lancement découvre une composante.
- **Détection de cycle** : graphe non orienté, une arête vers un sommet déjà visité qui n'est pas le parent ; graphe orienté, une arête vers un sommet « en cours » (sur la pile de récursion).
- **Graphe biparti** : BFS avec deux couleurs ; si une arête relie deux sommets de même couleur, le graphe n'est pas biparti (il contient un cycle de longueur impaire).
- **Îles dans une grille**, **remplissage**, **labyrinthes**, **plus court chemin en grille**.

```python
def est_biparti(graphe, n):
    couleur = [-1] * n
    for debut in range(n):
        if couleur[debut] != -1:
            continue
        couleur[debut] = 0
        file = deque([debut])
        while file:
            u = file.popleft()
            for v in graphe[u]:
                if couleur[v] == -1:
                    couleur[v] = 1 - couleur[u]
                    file.append(v)
                elif couleur[v] == couleur[u]:
                    return False
    return True

print(est_biparti({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 0]}, 4))   # True (cycle de longueur 4)
print(est_biparti({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 3))              # False (triangle)
```

### 19.5 Tri topologique (graphes orientés acycliques)

**Définition.** Un **tri topologique** d'un DAG est un ordre des sommets tel que, pour toute arête `u → v`, `u` apparaît **avant** `v`. Il existe si et seulement si le graphe est acyclique. Usages : prérequis de cours, ordre de compilation, ordonnancement de tâches.

**Algorithme de Kahn.** On traite d'abord les sommets sans prédécesseur (degré entrant nul) ; en retirant un sommet, on décrémente le degré entrant de ses successeurs, et ceux qui tombent à 0 rejoignent la file. Si tous les sommets sont traités, on a un ordre ; sinon, il existe un cycle.

```python
from collections import deque

def tri_topologique(n, aretes):
    graphe = [[] for _ in range(n)]
    degre_entrant = [0] * n
    for u, v in aretes:
        graphe[u].append(v)
        degre_entrant[v] += 1

    file = deque(i for i in range(n) if degre_entrant[i] == 0)
    ordre = []
    while file:
        u = file.popleft()
        ordre.append(u)
        for v in graphe[u]:
            degre_entrant[v] -= 1
            if degre_entrant[v] == 0:
                file.append(v)
    return ordre if len(ordre) == n else None      # None : il existe un cycle

print(tri_topologique(4, [(0, 1), (0, 2), (1, 3), (2, 3)]))   # [0, 1, 2, 3]
print(tri_topologique(2, [(0, 1), (1, 0)]))                   # None (cycle)
```

**Complexité** `O(V + E)`. Variante par DFS : l'ordre topologique est l'**inverse de l'ordre de fin** des sommets. La bibliothèque standard propose aussi `graphlib.TopologicalSorter`.

### 19.6 Arbre couvrant de poids minimal (MST)

**Définition.** Dans un graphe non orienté, connexe et pondéré, un **arbre couvrant** est un sous-ensemble d'arêtes qui relie **tous** les sommets sans cycle (donc `V - 1` arêtes). Un **arbre couvrant de poids minimal** (*minimum spanning tree*) minimise la somme des poids. Applications : réseaux (câblage, canalisations), regroupement hiérarchique, approximation du voyageur de commerce.

**Propriété de coupe.** Pour toute **coupe** (partition des sommets en deux parties), l'arête de **plus petit poids** traversant la coupe appartient à un arbre couvrant minimal (si elle est unique). C'est le fondement de la correction de Kruskal et de Prim, deux algorithmes gloutons.

#### Union-Find (ensembles disjoints)

Structure qui maintient une partition d'éléments en groupes et supporte deux opérations : **`trouver(x)`** (représentant du groupe de `x`) et **`unir(a, b)`** (fusionner deux groupes). Chaque groupe est un arbre dont la racine est le représentant.

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
        if a == b:
            return False                           # déjà dans le même groupe
        if self.taille[a] < self.taille[b]:
            a, b = b, a
        self.parent[b] = a
        self.taille[a] += self.taille[b]
        return True

uf = UnionFind(5)
uf.unir(0, 1)
uf.unir(3, 4)
print(uf.trouver(0) == uf.trouver(1), uf.trouver(1) == uf.trouver(3))   # True False
```

Deux optimisations : la **compression de chemin** (on raccourcit les chemins vers la racine lors d'un `trouver`) et l'**union par taille ou par rang** (on rattache le petit arbre au grand). Ensemble, elles donnent un coût amorti de **`O(α(n))`** par opération, où `α` est l'inverse de la fonction d'Ackermann : inférieur à 5 pour tout `n` réaliste, donc quasi constant.

#### Algorithme de Kruskal (glouton sur les arêtes)

On trie les arêtes par poids croissant et on ajoute chaque arête qui **ne crée pas de cycle** (ses deux extrémités sont dans des groupes différents d'Union-Find).

```python
def kruskal(n, aretes):                          # aretes : (poids, u, v)
    uf, poids_total, choisies = UnionFind(n), 0, []
    for w, u, v in sorted(aretes):
        if uf.unir(u, v):
            poids_total += w
            choisies.append((u, v, w))
    return poids_total, choisies                 # O(E log E)

print(kruskal(4, [(1, 0, 1), (4, 0, 2), (3, 1, 2), (2, 1, 3), (5, 2, 3)]))
# (6, [(0, 1, 1), (1, 3, 2), (1, 2, 3)])
```

Si le graphe n'est pas connexe, Kruskal produit une **forêt couvrante minimale**.

#### Algorithme de Prim (glouton sur les sommets)

On part d'un sommet et on fait **grossir un arbre** en ajoutant à chaque étape l'arête de poids minimal reliant l'arbre à un sommet extérieur, grâce à un tas.

```python
import heapq

def prim(graphe, depart=0):                       # graphe[u] = [(v, poids), ...]
    vus, tas, total = set(), [(0, depart)], 0
    while tas:
        w, u = heapq.heappop(tas)
        if u in vus:
            continue
        vus.add(u)
        total += w
        for v, poids in graphe[u]:
            if v not in vus:
                heapq.heappush(tas, (poids, v))
    return total                                  # O(E log V)

g_prim = {0: [(1, 1), (2, 4)], 1: [(0, 1), (2, 3), (3, 2)], 2: [(0, 4), (1, 3), (3, 5)], 3: [(1, 2), (2, 5)]}
print(prim(g_prim))                       # 6
```

|  | Kruskal | Prim |
| --- | --- | --- |
| Approche | Arêtes triées et Union-Find | Croissance depuis un sommet avec un tas |
| Complexité | `O(E log E)` | `O(E log V)` |
| Meilleur pour | Graphes **creux** ; liste d'arêtes disponible | Graphes **denses** ; liste d'adjacence |

### 19.7 Autres problèmes de graphes à connaître

- **Points d'articulation et ponts** : sommets ou arêtes dont la suppression déconnecte le graphe ; algorithme de Tarjan basé sur le DFS et les valeurs `bas`.
- **Circuits eulériens** (passer par chaque arête exactement une fois ; condition sur les degrés) et **hamiltoniens** (chaque sommet une fois ; NP-complet).
- **Coloration** de graphe (NP-difficile) et applications aux emplois du temps.
- **Plus bas ancêtre commun** dans un arbre, **diamètre** d'un arbre (deux BFS).

### 19.8 Pièges fréquents

- Marquer un sommet comme visité **à la sortie** de la file (BFS) : il est mis en file plusieurs fois.
- Utiliser une **matrice d'adjacence** pour un graphe creux de grande taille : mémoire `O(V²)`.
- Oublier de lancer le parcours depuis **chaque** sommet non visité : les autres composantes sont ignorées.
- Détecter un cycle dans un graphe non orienté **sans exclure le parent** (la même arête est vue dans les deux sens).
- Utiliser DFS pour un plus court chemin non pondéré, ou la récursion pour un graphe très profond en Python.

### Synthèse du chapitre 19

Un **graphe** modélise des sommets reliés par des arêtes ; la **liste d'adjacence** convient aux graphes creux. **BFS** donne les plus courts chemins non pondérés en `O(V + E)`, **DFS** révèle la structure (cycles, composantes, ordre de fin). Le **tri topologique** ordonne un DAG (Kahn ou ordre de fin inversé). **Kruskal** (Union-Find, `O(E log E)`) et **Prim** (tas, `O(E log V)`) construisent un arbre couvrant minimal, justifié par la propriété de coupe.

---

## 20. Plus courts chemins dans les graphes pondérés

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : définir distance, plus court chemin et relâchement d'arête ; écrire Dijkstra, Bellman-Ford, Floyd-Warshall, BFS 0-1, SPFA et A\* ; justifier pourquoi Dijkstra exige des poids positifs ; détecter un cycle de poids négatif ; traiter un DAG par ordre topologique ; choisir l'algorithme selon les poids et les besoins.

### 20.1 Le problème et les notions

Dans un graphe pondéré, le **poids d'un chemin** est la somme des poids de ses arêtes. Le **plus court chemin** de `s` à `t` est un chemin de poids minimal ; sa valeur est la **distance** `δ(s, t)`.

**Variantes du problème.**

- **Source unique** : distances de `s` vers tous les sommets (SSSP).
- **Paire source-cible** : un seul couple ; on peut s'arrêter dès que la cible est finalisée.
- **Toutes paires** (APSP).

**Sous-structure optimale.** Tout sous-chemin d'un plus court chemin est lui-même un plus court chemin. C'est ce qui rend possibles les algorithmes ci-dessous.

**Relâchement d'une arête** `(u, v, w)` : si `dist[u] + w < dist[v]`, on met à jour `dist[v] = dist[u] + w` (et le parent de `v`). Tous les algorithmes de cette section ne sont que des stratégies différentes pour ordonner les relâchements.

**Cycles de poids négatif.** Si un cycle de poids total strictement négatif est atteignable depuis la source, les plus courts chemins ne sont **pas définis** (on peut boucler pour diminuer indéfiniment). Les poids négatifs sans tel cycle sont acceptables.

### 20.2 Choisir l'algorithme

| Algorithme | Type | Poids négatifs ? | Complexité | Usage |
| --- | --- | --- | --- | --- |
| **BFS** | Source unique | Sans objet (non pondéré) | `O(V + E)` | Arêtes sans poids |
| **BFS 0-1** | Source unique | Poids 0 ou 1 | `O(V + E)` | Poids binaires |
| **Dijkstra** | Source unique | **Non** | `O((V + E) log V)` | Cas général à poids positifs ou nuls |
| **Bellman-Ford** | Source unique | Oui (détecte les cycles négatifs) | `O(V · E)` | Poids négatifs |
| **SPFA** | Source unique | Oui | `O(V · E)` au pire, souvent rapide | Pratique, à utiliser avec prudence |
| **Floyd-Warshall** | **Toutes paires** | Oui | `O(V³)` | Petit graphe, toutes les distances |
| **A\*** | Source vers cible | Non (heuristique admissible) | Selon l'heuristique | Cartes, jeux |
| **DAG (ordre topologique)** | Source unique | Oui | `O(V + E)` | Graphes acycliques |

### 20.3 Dijkstra

**Principe (glouton).** On maintient un ensemble de sommets **finalisés** dont la distance est définitive. À chaque étape, on prend le sommet non finalisé de **plus petite distance provisoire**, on le finalise, puis on relâche ses arêtes sortantes. Un tas binaire fournit le minimum.

**Pourquoi c'est correct (et pourquoi les poids doivent être positifs).** Quand `u` est le sommet non finalisé de plus petite distance provisoire `d`, tout autre chemin vers `u` doit sortir de l'ensemble finalisé par un sommet dont la distance provisoire est `≥ d` ; comme les poids sont positifs ou nuls, ce chemin ne peut que s'allonger : `d` est optimale. Avec une arête négative, un chemin plus long au départ pourrait devenir plus court : l'argument s'effondre.

```python
import heapq

def dijkstra(graphe, source):                   # graphe[u] = [(v, poids), ...]
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
        p.append(cible)
        cible = parent.get(cible)
    return p[::-1]

g_poids = {"A": [("B", 4), ("C", 1)], "B": [("D", 1)], "C": [("B", 2), ("D", 5)], "D": []}
dist, parent = dijkstra(g_poids, "A")     # tous les sommets doivent être des clés du dictionnaire
print(dist)                               # {'A': 0, 'B': 3, 'C': 1, 'D': 4}
print(chemin(parent, "D"))                # ['A', 'C', 'B', 'D']
```

L'**insertion paresseuse** (ajouter un nouveau couple dans le tas au lieu de modifier l'ancien) évite d'avoir une opération de diminution de clé ; les entrées obsolètes sont ignorées à la sortie du tas (`d > dist[u]`). Chaque arête provoque au plus une insertion, d'où `O(E log E) = O(E log V)`.

> **Remarque d'actualité.** Dijkstra est resté la référence pendant plus de soixante ans, notamment parce qu'il « trie » implicitement les sommets par distance. Un résultat théorique de 2025 (Duan et coll., *Breaking the Sorting Barrier for Directed Single-Source Shortest Paths*, STOC 2025) contourne cette barrière de tri pour les graphes orientés creux, avec une complexité en `O(m log^(2/3) n)`. Il s'agit d'un résultat **théorique** : en pratique, Dijkstra avec un tas binaire reste l'algorithme de référence.

### 20.4 Bellman-Ford

**Principe.** Un plus court chemin simple utilise au plus `V - 1` arêtes. On relâche donc **toutes les arêtes**, `V - 1` fois : après la `k`-ième passe, les distances correctes de tous les sommets atteignables par un plus court chemin d'au plus `k` arêtes sont acquises. Une `V`-ième passe qui améliore encore une distance révèle un **cycle de poids négatif atteignable**.

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
    return dist                                    # O(V * E)

print(bellman_ford(4, [(0, 1, 4), (0, 2, 1), (2, 1, -2), (1, 3, 1)], 0))   # [0, -1, 1, 0]
```

Bellman-Ford est plus lent que Dijkstra mais gère les poids négatifs ; il sert aussi à détecter les cycles négatifs (arbitrage de devises avec les logarithmes des taux).

### 20.5 Floyd-Warshall

**Principe (programmation dynamique).** Soit `dist_k[i][j]` la plus courte distance de `i` à `j` en n'utilisant comme sommets **intermédiaires** que les sommets `0..k`. Alors `dist_k[i][j] = min(dist_{k-1}[i][j], dist_{k-1}[i][k] + dist_{k-1}[k][j])` : soit le chemin évite `k`, soit il passe par `k`. On peut travailler en place sur une seule matrice.

```python
def floyd_warshall(dist):                         # matrice, INF sans arête, 0 sur la diagonale
    n = len(dist)
    for k in range(n):                            # k doit être la boucle EXTÉRIEURE
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist                                    # O(V^3) ; un dist[i][i] < 0 révèle un cycle négatif

INF = float("inf")
matrice = [[0, 3, INF], [INF, 0, 1], [2, INF, 0]]
print(floyd_warshall(matrice))            # [[0, 3, 4], [3, 0, 1], [2, 5, 0]]
```

Code très court, `O(V³)` en temps, `O(V²)` en mémoire ; adapté à `V` jusqu'à quelques centaines. Il sert aussi à calculer la **fermeture transitive** (accessibilité) avec des booléens.

### 20.6 BFS 0-1

Pour des poids valant uniquement 0 ou 1, un **deque** remplace le tas : on place le sommet voisin **en tête** si le poids est 0 et **en queue** si le poids est 1. Les sommets restent dans l'ordre croissant des distances, en `O(V + E)`.

```python
from collections import deque

def bfs_01(graphe, source, n):
    dist = [float("inf")] * n
    dist[source] = 0
    dq = deque([source])
    while dq:
        u = dq.popleft()
        for v, w in graphe[u]:                    # w vaut 0 ou 1
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    return dist

print(bfs_01({0: [(1, 0), (2, 1)], 1: [(2, 1)], 2: []}, 0, 3))   # [0, 0, 1]
```

### 20.7 SPFA (Bellman-Ford avec file)

On ne relâche que les arêtes sortantes des sommets dont la distance vient de diminuer, gérés par une file.

```python
from collections import deque

def spfa(graphe, source, n):
    INF = float("inf")
    dist, dans_file, compte = [INF] * n, [False] * n, [0] * n
    dist[source] = 0
    file = deque([source])
    while file:
        u = file.popleft()
        dans_file[u] = False
        for v, w in graphe[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if not dans_file[v]:
                    compte[v] += 1
                    if compte[v] > n:
                        raise ValueError("Cycle négatif")
                    file.append(v)
                    dans_file[v] = True
    return dist

print(spfa({0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, -2)], 3: []}, 0, 4))   # [0, -1, 1, 0]
```

> **Attention.** SPFA est en `O(V · E)` au pire et peut être mis en échec par des entrées conçues pour cela. Dès que les poids sont positifs, préférer Dijkstra.

### 20.8 A\* (A étoile)

**Idée.** A\* guide la recherche de Dijkstra **vers la cible** grâce à une **heuristique** `h(v)`, estimation du coût restant de `v` à la cible. Il explore les sommets dans l'ordre de `f(v) = g(v) + h(v)`, où `g(v)` est le coût déjà parcouru depuis la source.

- Si `h` est **admissible** (elle ne surestime jamais le coût réel), A\* renvoie un chemin optimal.
- Si `h` est **cohérente** (inégalité triangulaire : `h(u) ≤ w(u, v) + h(v)`), chaque sommet est finalisé au plus une fois.
- Avec `h = 0`, on retrouve Dijkstra.

```python
import heapq

def a_etoile(graphe, debut, but, h):
    tas = [(h(debut), 0, debut)]
    g = {debut: 0}
    while tas:
        _, cout, u = heapq.heappop(tas)
        if u == but:
            return cout
        if cout > g.get(u, float("inf")):
            continue
        for v, w in graphe[u]:
            nouveau = cout + w
            if nouveau < g.get(v, float("inf")):
                g[v] = nouveau
                heapq.heappush(tas, (nouveau + h(v), nouveau, v))
    return None

# Grille 3 x 3 : sommets (ligne, colonne), heuristique = distance de Manhattan
grille_g = {(i, j): [((i + di, j + dj), 1) for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1))
                     if 0 <= i + di < 3 and 0 <= j + dj < 3]
            for i in range(3) for j in range(3)}
print(a_etoile(grille_g, (0, 0), (2, 2), lambda v: abs(v[0] - 2) + abs(v[1] - 2)))   # 4
```

Sur une grille à déplacements en quatre directions, la **distance de Manhattan** `|x - xb| + |y - yb|` est admissible ; avec huit directions, on emploie la distance de Chebyshev ou la distance octile.

### 20.9 Plus courts chemins dans un DAG

Dans un graphe orienté acyclique, on traite les sommets dans l'**ordre topologique** et on relâche leurs arêtes sortantes : chaque arête n'est relâchée qu'une fois, et les poids négatifs sont acceptés. On peut aussi y calculer le **plus long chemin** (en négativant les poids ou en remplaçant `min` par `max`), ce qui est NP-difficile dans un graphe général.

```python
def plus_court_dag(graphe, ordre_topo, source):
    dist = {u: float("inf") for u in graphe}
    dist[source] = 0
    for u in ordre_topo:                            # sommets dans l'ordre topologique
        if dist[u] != float("inf"):
            for v, w in graphe[u]:
                dist[v] = min(dist[v], dist[u] + w)
    return dist                                      # O(V + E)

g_dag = {0: [(1, 2), (2, 6)], 1: [(2, 3)], 2: []}
print(plus_court_dag(g_dag, [0, 1, 2], 0))     # {0: 0, 1: 2, 2: 5}
```

### 20.10 Guide de choix

| Situation | Algorithme |
| --- | --- |
| Pas de poids | BFS |
| Poids 0 ou 1 | BFS 0-1 |
| Poids positifs, une source | **Dijkstra** |
| Poids négatifs ou détection de cycle négatif | **Bellman-Ford** |
| Toutes les paires, `V` petit (jusqu'à environ 400) | Floyd-Warshall |
| Une cible, heuristique disponible | **A\*** |
| Graphe acyclique | Ordre topologique puis relâchement |

### 20.11 Pièges fréquents

- Utiliser **Dijkstra avec des poids négatifs** : l'argument de finalisation s'effondre ; prendre Bellman-Ford.
- Ajouter une constante à toutes les arêtes pour supprimer les poids négatifs : cela favorise les chemins courts en nombre d'arêtes et **change** les plus courts chemins.
- Écrire Floyd-Warshall avec `k` en **boucle interne** : la boucle sur `k` doit être la plus extérieure.
- Oublier d'ignorer les **entrées périmées** du tas dans Dijkstra (`if d > dist[u]: continue`).
- Utiliser une heuristique **non admissible** dans A\* : le chemin n'est plus garanti optimal.

### Synthèse du chapitre 20

Tous les algorithmes de plus courts chemins reposent sur le **relâchement** des arêtes et ne diffèrent que par l'ordre : BFS (sans poids), BFS 0-1, **Dijkstra** (poids positifs, `O((V + E) log V)`), **Bellman-Ford** (poids négatifs, détection de cycle négatif, `O(V·E)`), **Floyd-Warshall** (toutes paires, `O(V³)`), **A\*** (avec heuristique admissible) et l'ordre topologique pour un DAG. Retenez le guide de choix de la section 20.10.

---

## 21. Composantes fortement connexes

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : définir composantes fortement connexes et graphe condensé ; écrire les algorithmes de Kosaraju (deux parcours, graphe transposé) et de Tarjan (un parcours, `idx`, `bas` et pile) ; justifier leur complexité `O(V + E)` ; utiliser les composantes pour résoudre 2-SAT et ramener un graphe orienté à un DAG.

### 21.1 Définition

Dans un graphe **orienté**, deux sommets `u` et `v` sont **fortement connectés** s'il existe un chemin de `u` à `v` **et** un chemin de `v` à `u`. Cette relation est une relation d'équivalence ; ses classes sont les **composantes fortement connexes** (SCC, *strongly connected components*) : des ensembles maximaux de sommets deux à deux fortement connectés.

**Graphe condensé.** En contractant chaque SCC en un seul sommet, on obtient un **DAG** (sinon deux composantes seraient mutuellement atteignables et fusionneraient). Cette structure permet d'appliquer au graphe condensé les outils des DAG : ordre topologique, programmation dynamique.

```text
   A <-> B        Les SCC sont {A, B, C} et {D, E}.
   |     ^         Le graphe condensé est :  {A,B,C} -> {D,E}
   v     |
   `---> C --> D <-> E
```

#### Applications

Analyse de **dépendances cycliques** (bibliothèques, modules), **2-SAT** (satisfaisabilité de formules à deux littéraux par clause), optimisation de compilateurs (analyse de flot), analyse du web (pages mutuellement accessibles), condensation d'un graphe avant d'y résoudre un problème par DP.

### 21.2 Algorithme de Kosaraju (deux parcours)

**Idée.** Un DFS qui part de n'importe quel sommet d'une SCC « puits » (sans arc sortant vers une autre SCC) découvre exactement cette SCC. On repère un tel ordre grâce aux dates de fin d'un premier DFS, puis on explore le graphe **transposé** (arcs inversés), où les SCC sont les mêmes mais où les arcs entre SCC sont inversés.

1. DFS sur `G` : noter l'ordre de **fin de traitement** des sommets.
2. Construire le graphe **transposé** (tous les arcs retournés).
3. DFS sur le transposé, en traitant les sommets par **ordre de fin décroissant** : chaque arbre découvert est une SCC.

```python
def kosaraju(n, graphe):                     # graphe[u] = liste des successeurs
    ordre, visite = [], [False] * n

    def dfs1(u):
        visite[u] = True
        for v in graphe[u]:
            if not visite[v]:
                dfs1(v)
        ordre.append(u)                      # ajouté à la FIN du traitement

    for u in range(n):
        if not visite[u]:
            dfs1(u)

    transpose = [[] for _ in range(n)]
    for u in range(n):
        for v in graphe[u]:
            transpose[v].append(u)

    comp, visite = [-1] * n, [False] * n

    def dfs2(u, c):
        visite[u] = True
        comp[u] = c
        for v in transpose[u]:
            if not visite[v]:
                dfs2(v, c)

    nb = 0
    for u in reversed(ordre):
        if not visite[u]:
            dfs2(u, nb)
            nb += 1
    return nb, comp                           # O(V + E)

g_scc = [[1], [2], [0, 3], [4], [3]]                # cycles {0, 1, 2} et {3, 4}
print(kosaraju(5, g_scc))                         # (2, [0, 0, 0, 1, 1])
```

### 21.3 Algorithme de Tarjan (un seul parcours)

**Idée.** Dans un seul DFS, chaque sommet reçoit un **numéro de découverte** `idx[u]` et une valeur `bas[u]`, le plus petit numéro de découverte atteignable depuis `u` en suivant des arcs d'arbre puis au plus un arc vers un sommet **encore sur la pile**. Les sommets sont empilés à la découverte. Un sommet avec `bas[u] == idx[u]` est la **racine** d'une SCC : on dépile alors jusqu'à `u` inclus, et les sommets dépilés forment la composante.

```python
def tarjan(n, graphe):
    idx, bas = [-1] * n, [0] * n
    sur_pile, pile, comp = [False] * n, [], [-1] * n
    compteur = nb = 0

    def dfs(u):
        nonlocal compteur, nb
        idx[u] = bas[u] = compteur
        compteur += 1
        pile.append(u)
        sur_pile[u] = True
        for v in graphe[u]:
            if idx[v] == -1:
                dfs(v)
                bas[u] = min(bas[u], bas[v])
            elif sur_pile[v]:
                bas[u] = min(bas[u], idx[v])
        if bas[u] == idx[u]:                     # racine d'une SCC
            while True:
                w = pile.pop()
                sur_pile[w] = False
                comp[w] = nb
                if w == u:
                    break
            nb += 1

    for u in range(n):
        if idx[u] == -1:
            dfs(u)
    return nb, comp                               # O(V + E)

print(tarjan(5, [[1], [2], [0, 3], [4], [3]]))   # (2, [1, 1, 1, 0, 0]) : numérotation inverse de Kosaraju
```

> **Attention.** En Python, ces versions **récursives** dépassent vite la limite de pile (au-delà de 1000 niveaux de profondeur) : augmenter `sys.setrecursionlimit` (et la taille de pile via `threading.stack_size`) ou réécrire les parcours **avec une pile explicite**.

### 21.4 Kosaraju ou Tarjan ?

|  | Kosaraju | Tarjan |
| --- | --- | --- |
| Parcours | 2 DFS et graphe transposé | **1** DFS |
| Complexité | `O(V + E)` | `O(V + E)` |
| Mémoire | Plus (graphe transposé) | Moins |
| Facilité de compréhension | Plus intuitif | Plus subtil |
| Ordre des composantes | Ordre topologique du graphe condensé | Ordre topologique **inverse** |

### 21.5 Application : 2-SAT

Une formule 2-CNF est un ET de clauses `(a OU b)`, où `a` et `b` sont des littéraux. Chaque clause équivaut à deux implications : `non a ⇒ b` et `non b ⇒ a`. On construit le **graphe d'implications** (un sommet par littéral et par négation) ; la formule est **satisfaisable si et seulement si aucune variable n'est dans la même SCC que sa négation**. Les affectations se lisent dans l'ordre topologique des composantes. Le problème est ainsi résolu en `O(V + E)`, alors que 3-SAT est NP-complet.

### 21.6 Pièges fréquents

- Confondre **connexité** (graphe non orienté) et **forte connexité** (chemins dans les deux sens).
- Parcourir le graphe transposé dans le **mauvais ordre** dans Kosaraju : il faut l'ordre de fin **décroissant**.
- Mettre à jour `bas[u]` avec un sommet qui n'est **plus sur la pile** dans Tarjan.
- Utiliser les versions **récursives** en Python sur de grands graphes : dépassement de pile ; passer à une pile explicite.
- Oublier que les numéros de composantes sortent dans l'ordre topologique (Kosaraju) ou inverse (Tarjan).

### Synthèse du chapitre 21

Une **composante fortement connexe** est une classe d'équivalence de l'accessibilité mutuelle ; le **graphe condensé** obtenu en les contractant est un DAG. **Kosaraju** utilise deux DFS (graphe puis transposé, par ordre de fin décroissant), **Tarjan** un seul DFS avec numéros de découverte, valeurs `bas` et pile, tous deux en `O(V + E)`. Retenez l'application à **2-SAT**, résolu en temps linéaire alors que 3-SAT est NP-complet.

---

## 22. Flots dans les réseaux

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : définir réseau, flot, capacité, conservation et coupe ; énoncer le théorème flot max, coupe min ; construire le graphe résiduel avec arcs inverses ; écrire Edmonds-Karp et Dinic ; comparer leurs complexités ; modéliser comme des flots couplage biparti, chemins disjoints et affectations.

### 22.1 Définitions

Un **réseau de flot** est un graphe orienté `G = (V, E)` dans lequel chaque arc `(u, v)` possède une **capacité** `c(u, v) ≥ 0`, avec deux sommets distingués : une **source** `s` et un **puits** `t`. Un **flot** associe à chaque arc une quantité `f(u, v)` vérifiant :

1. **Contrainte de capacité** : `0 ≤ f(u, v) ≤ c(u, v)` pour tout arc.
2. **Conservation du flot** : pour tout sommet `v` différent de `s` et `t`, la somme des flots entrants égale la somme des flots sortants.

La **valeur** du flot est le flux net sortant de la source. Le **problème du flot maximal** consiste à trouver un flot de valeur maximale de `s` à `t`. Images : débit d'un réseau de canalisations, trafic d'un réseau de communication.

#### Coupes et théorème flot max, coupe min

Une **coupe** `(S, T)` est une partition des sommets avec `s ∈ S` et `t ∈ T`. Sa **capacité** est la somme des capacités des arcs allant de `S` vers `T`. Tout flot a une valeur inférieure ou égale à la capacité de n'importe quelle coupe (le flot doit traverser chaque coupe). Le **théorème flot max, coupe min** affirme que la valeur du flot maximal est **égale à la capacité de la coupe minimale**. Ainsi, un flot est maximal exactement quand il n'existe plus de chemin augmentant dans le graphe résiduel.

### 22.2 Graphe résiduel et arcs inverses

Étant donné un flot `f`, le **graphe résiduel** contient, pour chaque arc `(u, v)` :

- un arc `(u, v)` de capacité résiduelle `c(u, v) - f(u, v)` (flot encore poussable) ;
- un **arc inverse** `(v, u)` de capacité `f(u, v)`, qui permet d'**annuler** une partie du flot déjà envoyé.

Les arcs inverses sont indispensables : sans eux, un mauvais choix de chemin au début pourrait bloquer l'optimum. Un **chemin augmentant** est un chemin de `s` à `t` dans le graphe résiduel ; on y pousse une quantité égale à sa **capacité minimale** (le goulot d'étranglement), ce qui augmente la valeur du flot.

### 22.3 Ford-Fulkerson et Edmonds-Karp

**Ford-Fulkerson** : tant qu'il existe un chemin augmentant, on y pousse le flot de la capacité minimale du chemin. Le choix du chemin est libre. Avec un **parcours en largeur** pour trouver le chemin (plus court en nombre d'arcs), c'est l'algorithme d'**Edmonds-Karp**, dont la complexité est polynomiale quelles que soient les capacités.

```python
from collections import deque

def edmonds_karp(capacite, s, t):                 # capacite : matrice n x n (devient le graphe résiduel)
    n, flot_total = len(capacite), 0
    while True:
        parent = [-1] * n
        parent[s] = s
        file = deque([s])
        while file and parent[t] == -1:           # BFS : plus court chemin augmentant
            u = file.popleft()
            for v in range(n):
                if parent[v] == -1 and capacite[u][v] > 0:
                    parent[v] = u
                    file.append(v)
        if parent[t] == -1:                       # plus de chemin augmentant : flot maximal
            break
        goulot, v = float("inf"), t
        while v != s:
            goulot = min(goulot, capacite[parent[v]][v])
            v = parent[v]
        v = t
        while v != s:
            u = parent[v]
            capacite[u][v] -= goulot              # arc direct
            capacite[v][u] += goulot              # arc inverse
            v = u
        flot_total += goulot
    return flot_total

reseau = [[0, 16, 13, 0, 0, 0], [0, 0, 10, 12, 0, 0], [0, 4, 0, 0, 14, 0],
          [0, 0, 9, 0, 0, 20], [0, 0, 0, 7, 0, 4], [0, 0, 0, 0, 0, 0]]
print(edmonds_karp(reseau, 0, 5))     # 23
```

**Pourquoi la terminaison ?** Avec des capacités entières, chaque augmentation accroît le flot d'au moins 1 : le nombre d'étapes est au plus la valeur du flot maximal. Avec BFS, on montre de plus que la distance de `s` à chaque sommet dans le graphe résiduel ne décroît jamais, d'où au plus `O(V·E)` augmentations, chacune en `O(E)`.

### 22.4 Algorithme de Dinic

Dinic procède par **phases** : à chaque phase, un BFS construit le **graphe de niveaux** (distance depuis `s` dans le résiduel), puis un DFS envoie un **flot bloquant** (un flot qui sature au moins un arc de chaque chemin) en n'empruntant que les arcs qui montent d'exactement un niveau. Le pointeur `ptr[u]` évite de réexaminer des arcs inutiles. Le nombre de phases est au plus `V`.

```python
from collections import deque

class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]            # g[u] = indices d'arêtes
        self.arete = []                            # [v, capacité] ; l'arête inverse est à l'indice ^ 1

    def ajouter(self, u, v, c):
        self.g[u].append(len(self.arete))
        self.arete.append([v, c])
        self.g[v].append(len(self.arete))
        self.arete.append([u, 0])

    def _bfs(self, s, t):
        self.niveau = [-1] * self.n
        self.niveau[s] = 0
        file = deque([s])
        while file:
            u = file.popleft()
            for i in self.g[u]:
                v, c = self.arete[i]
                if c > 0 and self.niveau[v] < 0:
                    self.niveau[v] = self.niveau[u] + 1
                    file.append(v)
        return self.niveau[t] >= 0

    def _dfs(self, u, t, pousse):
        if u == t:
            return pousse
        while self.ptr[u] < len(self.g[u]):
            i = self.g[u][self.ptr[u]]
            v, c = self.arete[i]
            if c > 0 and self.niveau[v] == self.niveau[u] + 1:
                d = self._dfs(v, t, min(pousse, c))
                if d > 0:
                    self.arete[i][1] -= d
                    self.arete[i ^ 1][1] += d
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

d = Dinic(6)
for u, v, c in [(0, 1, 16), (0, 2, 13), (1, 2, 10), (1, 3, 12), (2, 1, 4), (2, 4, 14),
                (3, 2, 9), (3, 5, 20), (4, 3, 7), (4, 5, 4)]:
    d.ajouter(u, v, c)
print(d.flot_max(0, 5))               # 23
```

L'astuce `indice ^ 1` associe chaque arête à son inverse : les arêtes sont stockées par paires (directe aux indices pairs, inverse aux indices impairs).

### 22.5 Complexités

| Algorithme | Complexité | Remarque |
| --- | --- | --- |
| **Ford-Fulkerson** (DFS) | `O(E · f*)` (`f*` : valeur du flot max, capacités **entières**) | Peut être très lent ; ne termine pas toujours avec des capacités irrationnelles |
| **Edmonds-Karp** (BFS) | **`O(V · E²)`** | Polynomial, indépendant des capacités |
| **Dinic** | **`O(V² · E)`** ; **`O(E · √V)`** sur les réseaux à capacités unitaires | Standard en compétition |
| **Push-relabel** (préflot) | `O(V² · √E)` (variante plus haut label) | Efficace sur graphes denses |
| **Algorithmes quasi-linéaires** | `E^(1+o(1))` | Résultat **théorique** récent (2022) ; non utilisé en pratique |

### 22.6 Applications

| Problème | Modélisation |
| --- | --- |
| **Couplage biparti maximum** | Source vers chaque sommet de gauche (capacité 1), arêtes gauche-droite (capacité 1), chaque sommet de droite vers le puits (capacité 1). Spécialisé : Hopcroft-Karp en `O(E√V)` |
| **Coupe minimale** | Après le flot max, les sommets atteignables depuis `s` dans le résiduel forment `S` |
| **Chemins disjoints** (par arêtes ou par sommets) | Capacités unitaires ; pour les sommets, on **divise** chaque sommet en deux (entrée et sortie reliées par un arc de capacité 1) |
| **Affectation de tâches ou de ressources**, planning de matchs | Flot avec capacités |
| **Sélection de projets** (profit maximal avec dépendances) | Coupe minimale |
| **Flot à coût minimal** | Chemins augmentants **de coût minimal** (Bellman-Ford ou Dijkstra avec potentiels) |

**Théorèmes liés.** Dans un graphe biparti, la taille d'un couplage maximum égale celle d'une couverture par sommets minimale (**théorème de König**). Pour les chemins disjoints, **théorème de Menger** : le nombre maximal de chemins arête-disjoints entre `s` et `t` est la taille d'une coupe minimale.

> **Limites.** Les flots ordinaires ne gèrent pas les **coûts** (flot à coût minimal), les **bornes inférieures** (circulations) ni les **flots entiers multi-produits** (NP-difficile). Si les capacités sont entières, il existe toujours un flot maximal **entier**.

### 22.7 Pièges fréquents

- Oublier les **arcs inverses** dans le graphe résiduel : un mauvais choix de chemin bloque alors le flot sous l'optimum.
- Pousser le flot sans prendre la **capacité minimale** (goulot) du chemin augmentant.
- Utiliser Ford-Fulkerson avec un DFS quelconque : le nombre d'étapes dépend de la **valeur** du flot (et peut ne pas terminer avec des capacités irrationnelles) ; préférer BFS ou Dinic.
- Oublier de **dédoubler les sommets** pour imposer une capacité sur un sommet (chemins disjoints par sommets).
- Mal indexer l'arête inverse : avec la convention `indice ^ 1`, les arêtes doivent être stockées par paires.

### Synthèse du chapitre 22

Un **flot** respecte les capacités et la conservation ; sa valeur maximale égale la capacité de la **coupe minimale**. Le **graphe résiduel**, avec ses arcs inverses, permet d'annuler des décisions : on augmente tant qu'il existe un chemin de `s` à `t`. **Edmonds-Karp** (BFS) est en `O(V·E²)`, **Dinic** en `O(V²·E)` et en `O(E√V)` sur les réseaux unitaires. Retenez les applications : couplage biparti, chemins disjoints (Menger), coupe minimale, affectations.

---

## 23. Arbres de segments et arbres de Fenwick

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : justifier le besoin de structures dynamiques pour les requêtes d'intervalle ; implémenter un arbre de Fenwick (bit de poids faible) et un arbre de segments ; appliquer la propagation paresseuse aux mises à jour d'intervalle ; choisir entre Fenwick, arbre de segments, table creuse et décomposition en racine carrée.

### 23.1 Le problème

Sur un tableau qui **change** au cours du temps, on veut répondre rapidement à des **requêtes d'intervalle** (somme, minimum, maximum, pgcd…) **et** appliquer des **mises à jour**.

| Approche | Requête | Mise à jour |
| --- | --- | --- |
| Tableau brut | `O(n)` | `O(1)` |
| Sommes préfixes | `O(1)` | `O(n)` (recalcul) |
| **Fenwick, arbre de segments** | **`O(log n)`** | **`O(log n)`** |

Le principe commun : précalculer des résumés de **blocs de tailles puissances de 2**, de façon qu'un intervalle quelconque se décompose en `O(log n)` blocs et qu'une modification n'affecte que `O(log n)` résumés.

### 23.2 Arbre de Fenwick (*Binary Indexed Tree*)

**Idée.** La case `i` (indices à partir de 1) stocke la somme d'un bloc de longueur égale au **bit de poids faible** de `i`, soit `i & -i`, se terminant en `i` : la case 12 (binaire 1100, bit de poids faible 4) résume les éléments 9 à 12. Pour obtenir la somme du préfixe `[1..i]`, on additionne les blocs obtenus en retirant successivement le bit de poids faible ; pour mettre à jour, on ajoute le delta à tous les blocs contenant `i`, en ajoutant successivement le bit de poids faible.

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

**Complexité** : construction `O(n log n)` (ou `O(n)` avec une astuce), requête et mise à jour `O(log n)` (au plus `log n` itérations, puisque chaque pas supprime ou fait avancer un bit), mémoire `O(n)`. Limité aux opérations **inversibles** (somme, XOR) pour obtenir un intervalle par soustraction de deux préfixes.

**Variantes.** BIT pour **mise à jour d'intervalle et requête de point** (en l'appliquant au tableau de différences), BIT en deux dimensions, **comptage d'inversions** (on traite les éléments dans l'ordre et on compte combien d'éléments plus grands ont déjà été insérés), **recherche du k-ième élément** par descente binaire.

### 23.3 Arbre de segments (*Segment Tree*)

**Idée.** Arbre binaire dont chaque nœud résume un **intervalle** (somme, minimum, maximum, pgcd…) en combinant les résumés de ses deux enfants. Plus général que Fenwick : toute opération **associative** convient (il n'est pas nécessaire qu'elle soit inversible).

Version **ascendante** compacte : les feuilles sont stockées aux indices `n` à `2n-1`, les nœuds internes aux indices `1` à `n-1`, le nœud `i` ayant pour enfants `2i` et `2i+1`.

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
            if l & 1:
                res += self.arbre[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.arbre[r]
            l //= 2
            r //= 2
        return res

seg = ArbreSegments([3, 2, -1, 6, 5, 4, -3, 3])
print(seg.requete(1, 5))              # 2 - 1 + 6 + 5 = 12   (t[1..4])
seg.modifier(2, 10)
print(seg.requete(1, 5))              # 2 + 10 + 6 + 5 = 23
```

Pour un **minimum**, on remplace `+` par `min` et l'élément neutre `0` par `float("inf")`. Cette version ascendante est compacte et rapide ; la version récursive classique (nœud, intervalle `[debut, fin]`) est plus flexible, notamment pour la propagation paresseuse.

**Complexité** : construction `O(n)`, requête et mise à jour `O(log n)`, mémoire `O(n)`.

### 23.4 Propagation paresseuse (*Lazy Propagation*)

Pour des **mises à jour d'intervalle** (par exemple « ajouter `v` à `t[l..r]` ») combinées à des requêtes d'intervalle, mettre à jour chaque feuille coûterait `O(n)`. On **retarde** l'application : lorsqu'un nœud est entièrement couvert par la mise à jour, on modifie son résumé et on note dans une étiquette `paresse` la mise à jour **en attente** pour ses enfants. On ne **propage** cette étiquette aux enfants que lorsqu'une opération doit descendre plus bas.

```python
class ArbreSegmentsParesseux:                    # ajout sur intervalle et somme sur intervalle
    def __init__(self, t):
        self.n = len(t)
        self.somme = [0] * (4 * self.n)
        self.paresse = [0] * (4 * self.n)
        self._construire(1, 0, self.n - 1, t)

    def _construire(self, noeud, l, r, t):
        if l == r:
            self.somme[noeud] = t[l]
            return
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
        if b < l or r < a:
            return
        if a <= l and r <= b:
            self.somme[noeud] += v * (r - l + 1)
            self.paresse[noeud] += v
            return
        self._pousser(noeud, l, r)
        m = (l + r) // 2
        self.ajouter(2 * noeud, l, m, a, b, v)
        self.ajouter(2 * noeud + 1, m + 1, r, a, b, v)
        self.somme[noeud] = self.somme[2 * noeud] + self.somme[2 * noeud + 1]

    def requete(self, noeud, l, r, a, b):        # somme de t[a..b]
        if b < l or r < a:
            return 0
        if a <= l and r <= b:
            return self.somme[noeud]
        self._pousser(noeud, l, r)
        m = (l + r) // 2
        return self.requete(2 * noeud, l, m, a, b) + self.requete(2 * noeud + 1, m + 1, r, a, b)

ap = ArbreSegmentsParesseux([1, 2, 3, 4, 5])
ap.ajouter(1, 0, 4, 1, 3, 10)         # t[1..3] += 10
print(ap.requete(1, 0, 4, 0, 4))      # 15 + 30 = 45
print(ap.requete(1, 0, 4, 2, 2))      # 13
```

Le nombre de nœuds visités par opération reste `O(log n)` : à chaque niveau, au plus quatre nœuds sont explorés. Pour d'autres opérations (affectation d'une valeur sur un intervalle, minimum avec ajout), il faut définir comment composer deux étiquettes et comment une étiquette modifie un résumé.

### 23.5 Fenwick ou arbre de segments ?

| Critère | **Fenwick (BIT)** | **Arbre de segments** |
| --- | --- | --- |
| Code | Très court | Plus long |
| Opérations supportées | Somme, XOR (inversibles) | **Toute opération associative** (min, max, pgcd…) |
| Mise à jour d'intervalle | Limitée (astuce des différences) | Oui (propagation paresseuse) |
| Constante | **Plus petite** | Plus grande |
| Mémoire | `n` | `2n` à `4n` |

### 23.6 Structures voisines et applications

- **Table creuse** (*sparse table*) : minimum ou maximum **statique** d'un intervalle en `O(1)` après un précalcul en `O(n log n)` (les intervalles de longueur puissance de 2 se recouvrent).
- **Décomposition en racine carrée** : blocs de taille `√n`, requêtes et mises à jour en `O(√n)`, simple et flexible.
- **Applications** : sommes, minimums ou maximums d'intervalle avec mises à jour ; comptage d'inversions ; rangs (statistiques d'ordre) ; plus longue sous-suite croissante avec valeurs compressées ; géométrie (balayage de ligne) ; requêtes hors ligne ; plus bas ancêtre commun.

### 23.7 Pièges fréquents

- Indexer un arbre de Fenwick **à partir de 0** : il se construit sur des indices à partir de 1 (`i & -i` vaut 0 pour `i = 0`).
- Appliquer Fenwick à une opération **non inversible** (minimum, maximum) : l'intervalle ne s'obtient plus par soustraction de deux préfixes.
- Mélanger bornes **inclusives** et **exclusives** (`requete(l, r)` avec `r` exclu dans la version ascendante).
- Oublier de **propager** l'étiquette paresseuse avant de descendre, ou d'oublier de recalculer le nœud au retour.
- Réserver trop peu de mémoire pour la version récursive : prévoir `4n` cases.

### Synthèse du chapitre 23

Fenwick et arbres de segments répondent aux requêtes d'intervalle et aux mises à jour en **`O(log n)`** sur un tableau dynamique. **Fenwick** : bit de poids faible, code très court, opérations inversibles. **Arbre de segments** : toute opération associative, propagation paresseuse pour les mises à jour d'intervalle. Retenez la règle : sommes préfixes pour un tableau figé, ces structures pour un tableau qui change, et la table creuse pour un minimum statique en `O(1)`.

---

## 24. Algorithmes sur les chaînes

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : définir préfixe, suffixe, bordure, sous-chaîne et sous-séquence ; écrire la recherche de motif par KMP, Rabin-Karp et l'algorithme Z ; implémenter et utiliser un trie ; connaître Manacher, les tableaux de suffixes et Aho-Corasick ; choisir un algorithme de recherche de motif.

### 24.1 Vocabulaire et recherche de motif naïve

Une **chaîne** est une suite de caractères d'un **alphabet**. Une **sous-chaîne** est une portion contiguë ; une **sous-séquence** n'est pas nécessairement contiguë. Un **préfixe** est une sous-chaîne qui commence au début, un **suffixe** une sous-chaîne qui finit à la fin ; une **bordure** est une chaîne qui est à la fois préfixe et suffixe propre (par exemple `ab` pour `abcab`).

**Problème de la recherche de motif.** Trouver toutes les occurrences d'un motif de longueur `m` dans un texte de longueur `n`.

L'algorithme **naïf** compare le motif à chaque position : `O(n · m)` dans le pire cas (par exemple texte `aaaa…a`, motif `aaab`). On l'améliore en évitant de **réexaminer** des caractères déjà comparés.

### 24.2 Algorithme de Knuth-Morris-Pratt (KMP)

**Idée.** Quand une comparaison échoue après avoir reconnu les `k` premiers caractères du motif, on sait déjà que le texte contient ces `k` caractères. Plutôt que de reculer dans le texte, on réutilise cette information : on se replace au **plus long préfixe du motif qui est aussi suffixe** de la partie reconnue, c'est-à-dire sa plus longue bordure. Le tableau `pi` donne, pour chaque préfixe `motif[:i+1]`, la longueur de sa plus longue bordure.

```python
def table_prefixes(motif):
    pi = [0] * len(motif)
    k = 0
    for i in range(1, len(motif)):
        while k and motif[i] != motif[k]:
            k = pi[k - 1]                        # on se replie sur une bordure plus courte
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
            k = pi[k - 1]                        # continuer pour les occurrences chevauchantes
    return positions                              # O(n + m)

print(kmp("abababcabab", "abab"))                 # [0, 2, 7]
print(table_prefixes("abab"))                     # [0, 0, 1, 2]
```

**Complexité** : `O(n + m)`. Analyse amortie : `k` augmente d'au plus 1 par caractère du texte, et chaque repli le diminue ; il ne peut donc pas y avoir plus de `n` replis au total. La construction de `pi` suit le même raisonnement, en `O(m)`.

### 24.3 Algorithme de Rabin-Karp

**Idée.** On compare des **empreintes** (valeurs de hachage) au lieu de chaînes entières. Avec un **hachage roulant**, l'empreinte de la fenêtre suivante se déduit de la précédente en `O(1)` : on retire le caractère sortant, on décale, on ajoute le caractère entrant. Quand les empreintes coïncident, on **vérifie** par comparaison directe, car des collisions sont possibles.

```python
def rabin_karp(texte, motif, base=256, mod=10**9 + 7):
    n, m = len(texte), len(motif)
    if m > n:
        return []
    puissance = pow(base, m - 1, mod)
    h_motif = h_texte = 0
    for i in range(m):
        h_motif = (h_motif * base + ord(motif[i])) % mod
        h_texte = (h_texte * base + ord(texte[i])) % mod
    positions = []
    for i in range(n - m + 1):
        if h_motif == h_texte and texte[i:i + m] == motif:      # vérification (collisions possibles)
            positions.append(i)
        if i < n - m:                                           # fait glisser la fenêtre en O(1)
            h_texte = ((h_texte - ord(texte[i]) * puissance) * base + ord(texte[i + m])) % mod
    return positions

print(rabin_karp("abababcabab", "abab"))          # [0, 2, 7]
```

**Complexité** : `O(n + m)` en moyenne, `O(n · m)` au pire (collisions en grand nombre). Très utile pour chercher **plusieurs motifs de même longueur** et pour détecter des **sous-chaînes dupliquées** (on stocke les empreintes dans un ensemble). On choisit un grand module premier, voire un double hachage, pour réduire les collisions.

### 24.4 Algorithme Z

**Définition.** Pour une chaîne `s`, `Z[i]` est la longueur du plus long préfixe de `s` qui coïncide avec le suffixe de `s` commençant en `i` (avec `Z[0] = 0` par convention). L'algorithme maintient une fenêtre `[l, r)` correspondant à la plus longue sous-chaîne déjà reconnue comme préfixe, ce qui permet de **réutiliser** les valeurs déjà calculées et de ne comparer que les nouveaux caractères.

```python
def z_algorithme(s):
    n, z = len(s), [0] * len(s)
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])               # réutilise l'information de la fenêtre
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z                                          # O(n)

print(z_algorithme("aabxaab"))                        # [0, 1, 0, 0, 3, 1, 0]

# Recherche de motif : on calcule Z sur motif + "#" + texte ; Z[i] == len(motif) signale une occurrence
motif, texte = "aab", "xaabaab"
z = z_algorithme(motif + "#" + texte)
print([i - len(motif) - 1 for i, v in enumerate(z) if v == len(motif)])   # [1, 4]
```

Le séparateur `#` (caractère absent des deux chaînes) garantit qu'aucun préfixe ne dépasse la longueur du motif. Même complexité que KMP, `O(n + m)`, avec un code souvent plus simple à retenir. L'algorithme Z permet aussi de calculer les périodes d'une chaîne et de comparer des préfixes.

### 24.5 Trie (arbre préfixe)

Un **trie** est un arbre dont chaque arête porte un caractère : un chemin de la racine à un nœud lit un préfixe, et un indicateur marque la fin d'un mot. L'insertion et la recherche d'un mot coûtent **`O(L)`** (longueur `L` du mot), indépendamment du nombre de mots stockés. Les mots partageant un préfixe partagent le chemin correspondant.

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
            if noeud is None:
                return None
        return noeud

    def contient(self, mot):
        n = self._noeud(mot)
        return n is not None and n.fin_de_mot

    def commence_par(self, prefixe):
        return self._noeud(prefixe) is not None

    def completions(self, prefixe):               # tous les mots qui commencent par `prefixe`
        resultat = []
        def parcourir(noeud, chemin):
            if noeud.fin_de_mot:
                resultat.append(prefixe + chemin)
            for c, e in noeud.enfants.items():
                parcourir(e, chemin + c)
        n = self._noeud(prefixe)
        if n:
            parcourir(n, "")
        return resultat

trie = Trie()
for mot in ["chat", "char", "chien", "car"]:
    trie.inserer(mot)
print(trie.contient("car"), trie.contient("ca"), trie.commence_par("ch"))   # True False True
print(sorted(trie.completions("cha")))                                      # ['char', 'chat']
```

**Usages** : **autocomplétion**, correcteurs orthographiques, **routage IP** (trie binaire sur les bits d'adresse, préfixe le plus long), recherche de mots dans une grille (Boggle), dictionnaires, **Aho-Corasick** (recherche simultanée de plusieurs motifs), tri lexicographique, XOR maximal (trie binaire).

**Compromis.** Mémoire potentiellement importante (un nœud par caractère) ; avec un alphabet grand, on utilise un dictionnaire par nœud (comme ici) plutôt qu'un tableau fixe. Un **trie compressé** (arbre radix) fusionne les chaînes de nœuds à un seul enfant.

### 24.6 Autres outils

| Outil | Rôle | Complexité |
| --- | --- | --- |
| **Manacher** | Plus longs palindromes centrés en chaque position | `O(n)` |
| **Tableau des suffixes et tableau LCP** | Recherche de sous-chaînes, plus longue sous-chaîne répétée, comptage de sous-chaînes distinctes | `O(n log n)` à `O(n)` |
| **Aho-Corasick** | Recherche de plusieurs motifs simultanément (trie plus liens d'échec, généralisation de KMP) | `O(n + m + occurrences)` |
| **Distance d'édition** | Mesure de similarité (programmation dynamique, chapitre 18) | `O(n · m)` |
| **Hachage polynomial** | Comparaison de sous-chaînes en `O(1)` après précalcul des hachages de préfixes | Précalcul `O(n)` |
| **Plus longue sous-chaîne commune** | Tableau des suffixes ou DP | `O(n · m)` en DP |

### 24.7 Comparaison des algorithmes de recherche de motif

| Algorithme | Précalcul | Recherche | Remarque |
| --- | --- | --- | --- |
| Naïf | Aucun | `O(n · m)` | Simple, suffisant pour de petits motifs |
| **KMP** | `O(m)` | **`O(n)`** | Garanti, sans hachage |
| **Rabin-Karp** | `O(m)` | `O(n)` en moyenne | Plusieurs motifs, hachage roulant |
| **Z** | `O(n + m)` | `O(n)` | Simple, polyvalent |
| **Boyer-Moore** | `O(m + alphabet)` | Souvent sous-linéaire | Très rapide en pratique pour les longs motifs |
| `str.find`, `in` (Python) | Aucun | Rapide en pratique | Algorithme hybride optimisé ; à préférer en production |

### 24.8 Pièges fréquents

- Confondre **sous-chaîne** (contiguë) et **sous-séquence** (non contiguë).
- Oublier de **vérifier** une occurrence quand les empreintes de Rabin-Karp coïncident : des collisions existent.
- Omettre le **séparateur** (`#`) entre motif et texte dans l'algorithme Z : un préfixe peut dépasser la longueur du motif.
- Ne pas continuer après une occurrence dans KMP (`k = pi[k - 1]`) : les occurrences **chevauchantes** sont manquées.
- Réécrire une recherche de motif en production alors que `in`, `find` et `re` sont optimisés.

### Synthèse du chapitre 24

Les algorithmes efficaces de recherche de motif évitent de revenir en arrière dans le texte : **KMP** réutilise les bordures (`O(n + m)`), **Z** réutilise les préfixes communs (`O(n + m)`), **Rabin-Karp** compare des empreintes avec un hachage roulant. Le **trie** répond aux requêtes de préfixe en `O(L)` quelle que soit la taille du dictionnaire. Retenez Manacher, les tableaux de suffixes, Aho-Corasick et la distance d'édition comme prolongements.

---

## 25. Aller plus loin

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez : situer les sujets avancés et de compétition (structures, théorie des nombres, géométrie, jeux, graphes, algorithmes randomisés) ; distinguer les classes P, NP, NP-complet et NP-difficile ; savoir quoi faire face à un problème NP-difficile ; choisir la technique adaptée à un problème grâce au tableau récapitulatif ; organiser sa progression et ses ressources d'entraînement.

### 25.1 Sujets avancés et de compétition

| Domaine | Sujets |
| --- | --- |
| **Structures de données** | **Décomposition lourde-légère** (*heavy-light decomposition*) pour des requêtes sur des chemins d'arbre ; **décomposition en centroïdes** ; **algorithme de Mo** (requêtes d'intervalle hors ligne en `O((n + q)√n)`) ; structures **persistantes** (conserver toutes les versions) ; arbres d'ondelettes ; **treaps** et arbres équilibrés ; arbres d'intervalles ; **LCA** (plus bas ancêtre commun, par levage binaire ou table d'Euler) |
| **Théorie des nombres** | Restes chinois, indicatrice d'Euler, résidus quadratiques, logarithme discret, **FFT** et **NTT** (multiplication rapide de polynômes) |
| **Géométrie algorithmique** | **Enveloppe convexe** (Graham, Andrew), balayage de ligne, intersection de segments, paire de points la plus proche, aire de polygones |
| **Théorie des jeux** | Nombres de **Grundy** (théorème de Sprague-Grundy pour les jeux impartiaux), **minimax** et **élagage alpha-bêta** |
| **Algèbre linéaire** | Exponentiation de matrices, élimination de Gauss (modulo un premier ou sur les réels) |
| **Combinatoire** | Inclusion-exclusion, nombres de Catalan, lemme de Burnside, fonctions génératrices |
| **Graphes avancés** | Appariement dans un graphe général (Blossom d'Edmonds), **2-SAT**, ponts et points d'articulation, flots à coût minimal, circuits eulériens, couplage biparti pondéré (algorithme hongrois) |
| **Algorithmes randomisés et en ligne** | Algorithmes de Las Vegas et de Monte Carlo, échantillonnage par réservoir, filtres de Bloom, algorithmes d'approximation en ligne |

### 25.2 Complexité et difficulté : P, NP et au-delà

La théorie de la complexité classe les **problèmes** (et non les algorithmes) selon les ressources nécessaires pour les résoudre. Elle s'exprime surtout sur des **problèmes de décision** (réponse oui ou non).

| Classe | Signification | Exemples |
| --- | --- | --- |
| **P** | Résoluble en temps **polynomial** par un algorithme déterministe | Tri, plus courts chemins, flots, test de primalité |
| **NP** | Une solution proposée (un **certificat**) se **vérifie** en temps polynomial | Sudoku, SAT, sac à dos (décision), coloration |
| **NP-complet** | Problèmes de NP les plus difficiles : tout problème de NP s'y **réduit** en temps polynomial. Si l'un est dans P, tous le sont | SAT, 3-SAT, TSP (décision), coloration, cycle hamiltonien, sac à dos (décision), couverture de sommets |
| **NP-difficile** | Au moins aussi difficile que NP (pas nécessairement dans NP) | TSP (optimisation), problème de l'arrêt |

On a `P ⊆ NP`. La question **P = NP ?** reste ouverte et est l'un des sept problèmes du millénaire. On prouve qu'un problème est NP-difficile par **réduction** : on transforme (en temps polynomial) un problème NP-difficile connu en ce problème. Cette preuve ne dit pas que le problème est insoluble, mais qu'il est improbable d'en trouver une solution polynomiale exacte.

Si un problème est **NP-difficile**, on se tourne vers :

- des algorithmes **exacts exponentiels** raisonnables : DP par masques de bits, retour sur trace avec élagage, séparation et évaluation (*branch and bound*) ; algorithmes paramétrés (exponentiels seulement en un petit paramètre `k`) ;
- des algorithmes d'**approximation** avec garantie sur la qualité : par exemple, une couverture de sommets de taille au plus double de l'optimum, ou un TSP métrique approché à un facteur 1,5 (Christofides) ;
- des **heuristiques** et **métaheuristiques** sans garantie : recuit simulé, algorithmes génétiques, recherche tabou, colonies de fourmis ;
- des **solveurs** généraux : SAT, programmation linéaire en nombres entiers, bibliothèque OR-Tools.

Autres classes utiles : **PSPACE** (espace polynomial), **EXPTIME**, **co-NP**, et les classes randomisées **RP** et **BPP**.

### 25.3 Résumé : quel algorithme pour quel problème ?

| Problème | Technique ou algorithme | Chapitre |
| --- | --- | --- |
| Chercher dans un tableau trié | Recherche binaire, `bisect` | 6 |
| Trouver une valeur optimale monotone | Recherche binaire sur la réponse | 15 |
| Paires ou triplets dans un tableau trié | Deux pointeurs | 12 |
| Sous-tableau ou sous-chaîne contigu optimal | Fenêtre glissante | 13 |
| Somme sur un intervalle (statique) | Sommes préfixes | 14 |
| Somme sur un intervalle (dynamique) | Fenwick, arbre de segments | 23 |
| Compter, regrouper, tester l'appartenance | Hachage | 17 |
| Choix localement optimal prouvé | Glouton | 10 |
| Sous-problèmes qui se chevauchent | **Programmation dynamique** | 18 |
| Explorer toutes les configurations avec élagage | Retour sur trace | 11 |
| Plus court chemin, non pondéré | BFS | 19 |
| Plus court chemin, poids positifs | Dijkstra | 20 |
| Plus court chemin, poids négatifs | Bellman-Ford | 20 |
| Toutes les paires de plus courts chemins | Floyd-Warshall | 20 |
| Dépendances, ordonnancement | Tri topologique | 19 |
| Connecter à coût minimal | Kruskal, Prim | 19 |
| Composantes connexes dynamiques | Union-Find | 19 |
| Cycles dans un graphe orienté, SCC, 2-SAT | Tarjan, Kosaraju | 21 |
| Capacité maximale d'un réseau, appariement | Flot maximal (Dinic) | 22 |
| Recherche de motif | KMP, Z, Rabin-Karp | 24 |
| Autocomplétion, préfixes | Trie | 24 |
| Trier | `sorted()` (Timsort) ; comptage ou radix si les clés s'y prêtent | 8 |
| Entiers modulaires, premiers, inverses | Crible, exponentiation rapide, Euclide étendu | 16 |

### 25.4 Conseils de progression

1. **Maîtriser les bases** : complexité, tableaux, récursivité, tris, recherche.
2. **Apprendre les schémas** (deux pointeurs, fenêtre glissante, préfixes, hachage, recherche binaire sur la réponse) : ils couvrent la majorité des problèmes d'entretien.
3. **Pratiquer régulièrement** : un problème par jour vaut mieux que dix le week-end.
4. **Écrire d'abord la solution par force brute**, puis optimiser ; comparer les deux sur des tests aléatoires pour détecter les erreurs.
5. **Analyser** toujours la complexité avant de coder, en s'aidant des contraintes de l'énoncé.
6. **Relire** ses solutions : pourquoi cela marche-t-il ? Quels sont les cas limites ?
7. **Étudier** les solutions des autres une fois qu'on a cherché soi-même.
8. **Prouver** ses algorithmes (invariant, échange, récurrence) : la preuve révèle les cas qui échappent aux tests.
9. **Tenir un cahier de patrons** : pour chaque schéma, le code minimal, la complexité et un exemple.

### 25.5 Ressources

- *Introduction à l'algorithmique* de Cormen, Leiserson, Rivest et Stein (**CLRS**), la référence académique.
- *The Algorithm Design Manual* de Steven Skiena, orienté pratique et catalogue de problèmes.
- *Algorithms* de Sedgewick et Wayne, avec un site compagnon riche en visualisations.
- *Competitive Programmer's Handbook* d'Antti Laaksonen (gratuit).
- **cp-algorithms.com** : référence très complète pour la compétition.
- Plateformes d'entraînement : **LeetCode**, **Codeforces**, **AtCoder**, **Kattis**, **Advent of Code**, **Project Euler**, **France-IOI** (en français).
- **VisuAlgo** (visualisations animées des structures et algorithmes), **Python Tutor** (exécution pas à pas).

### 25.6 Pièges fréquents

- Prendre « NP-difficile » pour « insoluble » : cela signifie qu'aucun algorithme polynomial exact n'est connu, pas qu'aucun algorithme n'existe.
- Confondre **NP** (certificat vérifiable en temps polynomial) et **non polynomial**.
- Chercher une solution exacte polynomiale à un problème NP-difficile au lieu de viser une approximation, une heuristique, un algorithme paramétré ou un solveur.
- Choisir un algorithme avant d'avoir lu les **contraintes** de l'énoncé, ou ne pas comparer la solution à une version par force brute sur des tests aléatoires.
- Ne pas prouver ses algorithmes (invariant, échange, récurrence) : la preuve révèle les cas limites que les tests oublient.

### Synthèse du chapitre 25

Un algorithme se juge sur sa **correction** (invariant, variant) puis sur sa **complexité**. Les grands schémas (diviser pour régner, glouton, programmation dynamique, retour sur trace, graphes) couvrent l'essentiel des problèmes ; le choix dépend de la structure du problème et des contraintes sur `n`. Au-delà de **P**, la **NP-complétude** explique pourquoi certains problèmes résistent et oriente vers l'approximation, les heuristiques et les solveurs. Progressez par la pratique régulière, la solution naïve d'abord, l'analyse systématique de la complexité et la lecture des solutions des autres.

---

*Fin du cours. Bon apprentissage de l'algorithmique !*
