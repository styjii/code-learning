<div align="center">

# Python — Exercices

**Du premier `print()` à la programmation orientée objet moderne**

*Version mise à jour pour Python 3.14 / 3.15 (octobre 2026)*

</div>

---

## Ressources et outils

| Ressource | Description |
| --- | --- |
| **Cours** | [Python — Guide complet](/language/python) |
| **Glossaire** | [Glossaire Python (docstring.fr)](https://docstring.fr/glossaire) |
| **Documentation officielle** | [docs.python.org/fr](https://docs.python.org/fr/3/) |
| **Éditeurs en ligne** | [Replit](https://replit.com), [Google Colab](https://colab.research.google.com), [python.org/shell](https://www.python.org/shell/) |

### Modules associés

- [Quelques modules](/language/modules/python)
- [Django](/language/frameworks/django)
- [bs4 (Beautiful Soup)](/language/modules/bs4)

---

## Sommaire

1. [Introduction](#1-introduction)
2. [Syntaxe et indentation](#2-syntaxe-et-indentation)
3. [Variables et types de données](#3-variables-et-types-de-données)
4. [Opérateurs et expressions](#4-opérateurs-et-expressions)
5. [Entrées et sorties](#5-entrées-et-sorties)
6. [Structures de contrôle](#6-structures-de-contrôle)
7. [Dictionnaires](#7-dictionnaires)
8. [Listes](#8-listes)
9. [Ensembles](#9-ensembles)
10. [Tuples](#10-tuples)
11. [Fonctions](#11-fonctions)
12. [Itérateurs et générateurs](#12-itérateurs-et-générateurs)
13. [Gestion des erreurs](#13-gestion-des-erreurs)
14. [Gestion des fichiers](#14-gestion-des-fichiers)
15. [Modules, paquets et environnements virtuels](#15-modules-paquets-et-environnements-virtuels)
16. [Programmation orientée objet](#16-programmation-orientée-objet)
17. [Typage statique](#17-typage-statique)
18. [Programmation asynchrone et concurrence](#18-programmation-asynchrone-et-concurrence)
19. [Tests et qualité du code](#19-tests-et-qualité-du-code)
20. [Aller plus loin](#20-aller-plus-loin)

> **Légende** : chaque exercice porte le numéro de la section du cours qu'il illustre (l'exercice 8.5.2 est le deuxième exercice de la section 8.5). *(défi)* = exercice plus difficile. Les exercices supposent Python 3.14 ; lorsqu'une fonctionnalité exige une version précise, elle est indiquée. Aucune solution n'est fournie dans ce document.

---

# 1. Introduction

---

## 1.1 Qu'est-ce que Python ?

**Exercice 1.1.1**

Indiquez si chaque affirmation est vraie ou fausse, en justifiant :

1. Python est un langage compilé en code machine natif avant chaque exécution.
2. En Python, le type est associé à la valeur et non à la variable.
3. Python impose de déclarer le type de chaque variable.
4. Python supporte les paradigmes impératif, orienté objet et fonctionnel.
5. Les blocs de code sont délimités par des accolades.

**Exercice 1.1.2**

Complétez le tableau avec vos propres mots :

| Caractéristique | Signification |
| --- | --- |
| Haut niveau | |
| Polyvalent | |
| Interprété | |
| Typage dynamique | |
| Multi-paradigme | |

**Exercice 1.1.3**

Dans une session interactive, exécutez `x = 3`, puis `x = "trois"`, puis `x = [3]`. Affichez `type(x)` après chaque ligne. Que démontre cette expérience sur le typage dynamique ?

### Pourquoi les débutants l'apprécient

**Exercice 1.1.4**

Écrivez le même petit programme (lire un nombre et afficher son double) en Python puis dans un autre langage de votre choix (C, Java, JavaScript…). Comparez le nombre de lignes, de symboles de ponctuation et de déclarations de types.

### Pourquoi les professionnels l'utilisent

**Exercice 1.1.5**

Pour chacune des bibliothèques citées dans le cours (NumPy, Django, FastAPI, PyTorch, Pandas), rédigez une phrase qui décrit son usage principal et le type de projet où vous l'utiliseriez.

## 1.2 Domaines d'utilisation

**Exercice 1.2.1**

Associez chaque outil à son domaine : Django, Pygame, MicroPython, NumPy, Tkinter, Jupyter, PyQt, FastAPI, Kivy, SciPy.

**Exercice 1.2.2**

Choisissez trois domaines de la liste du cours. Pour chacun, imaginez un projet concret réalisable en un week-end, et listez les modules ou bibliothèques que vous utiliseriez.

**Exercice 1.2.3**

Rédigez une courte note (cinq lignes) expliquant pourquoi Python est souvent choisi pour l'enseignement de l'informatique.

## 1.3 Histoire de Python

### Création

**Exercice 1.3.1**

Qui a créé Python, en quelle année a-t-il commencé son développement, et pourquoi le nom « Python » ? Retrouvez l'information dans la documentation officielle.

### Objectifs de conception

**Exercice 1.3.2**

Dans un interpréteur, exécutez `import this`. Choisissez trois aphorismes du « Zen de Python » et illustrez chacun par un exemple de code (un bon et un mauvais).

### Les grandes versions

**Exercice 1.3.3**

Associez chaque nouveauté à la version qui l'a introduite : `match`/`case`, t-strings, `except*`, syntaxe `def f[T]()`, nouveau REPL, compréhensions de listes, `print()` devenu fonction, opérateur `:=`.

**Exercice 1.3.4**

Quelles ruptures de compatibilité Python 3.0 a-t-il introduites ? Donnez au moins trois exemples de code Python 2 qui ne fonctionnent plus en Python 3.

**Exercice 1.3.5**

Quelle version de Python est installée sur votre machine ? Est-elle encore supportée ? Vérifiez sur python.org le calendrier de fin de vie.

### Gouvernance et communauté

**Exercice 1.3.6**

Que signifient les sigles BDFL, PSF et PEP ? Quel est le rôle du Conseil de pilotage (*Steering Council*) ?

**Exercice 1.3.7**

Consultez la PEP 20 et la PEP 8 : notez le titre, l'auteur et le sujet de chacune.

### Chronologie

**Exercice 1.3.8**

Reconstituez la chronologie d'un événement majeur de chaque décennie (1990, 2000, 2010, 2020) à partir du tableau du cours, puis ajoutez deux événements de votre recherche personnelle.

## 1.4 Caractéristiques de Python

### 1. Langage interprété

**Exercice 1.4.1**

Écrivez un script contenant une erreur à la ligne 5 (par exemple une division par zéro) précédée de quatre `print`. Exécutez-le. Les `print` s'affichent-ils avant l'erreur ? Que cela révèle-t-il sur l'exécution ligne par ligne ?

### 2. Syntaxe lisible

**Exercice 1.4.2**

Réécrivez de façon plus pythonique ce code de style C :

```python
i = 0
while i < len(noms):
    print(noms[i])
    i = i + 1
```

### 3. Typage dynamique (et typage graduel)

**Exercice 1.4.3**

Écrivez une fonction `doubler(x)` qui fonctionne avec un entier, une chaîne, une liste. Que se passe-t-il avec `None` ? Ajoutez ensuite des annotations de types et vérifiez avec `mypy` ce qui change.

### 4. Portable et multiplateforme

**Exercice 1.4.4**

Écrivez un script qui affiche le nom du système d'exploitation, la version de Python et le séparateur de chemin, avec `sys`, `os` et `platform`.

### 5. Bibliothèque standard riche (« piles incluses »)

**Exercice 1.4.5**

Sans installer de paquet, utilisez trois modules de la bibliothèque standard pour : afficher la date du jour, générer un nombre aléatoire entre 1 et 100, lister les fichiers du dossier courant.

### 6. Libre et gratuit

**Exercice 1.4.6**

Quelle licence encadre Python ? Retrouvez son nom et expliquez en deux phrases ce qu'elle autorise.

### 7. Multi-paradigme

**Exercice 1.4.7**

Calculez la somme des carrés des nombres pairs de 1 à 20 de trois façons : style impératif (boucle), style fonctionnel (`map` / `filter` / `sum`) et par compréhension. Comparez la lisibilité.

### 8. Extensible et intégrable

**Exercice 1.4.8**

Utilisez le module `ctypes` pour appeler une fonction de la bibliothèque C (par exemple `strlen` ou `abs`). Expliquez en quoi cela illustre l'extensibilité de Python.

### 9. Gestion automatique de la mémoire

**Exercice 1.4.9**

Avec `sys.getrefcount` et `del`, observez le comptage de références d'un objet. Puis créez un cycle de références entre deux objets et utilisez `gc.collect()` pour montrer le rôle du ramasse-miettes.

### 10. Mode interactif (REPL)

**Exercice 1.4.10**

Dans le REPL, utilisez `_` pour récupérer le dernier résultat, `help()`, `dir()` et `type()` sur un objet de votre choix. Notez trois autres astuces du REPL.

### 11. Communauté active

**Exercice 1.4.11**

Trouvez trois lieux où poser une question sur Python (forum officiel, Stack Overflow, Discord…). Rédigez une question bien formulée sur un problème fictif (contexte, code minimal, erreur obtenue, résultat attendu).

### 12. Écosystème de bibliothèques

**Exercice 1.4.12**

Sur pypi.org, recherchez une bibliothèque pour : lire des fichiers Excel, générer des QR codes, manipuler des images. Notez pour chacune le nom du paquet, la dernière version et le nombre de téléchargements.

## 1.5 Installer Python

### Télécharger

**Exercice 1.5.1**

Téléchargez la dernière version stable de Python depuis python.org. Notez le numéro de version et la taille du fichier d'installation pour votre système.

### Windows

**Exercice 1.5.2**

Sous Windows : installez Python en cochant l'option pour ajouter Python au `PATH`. Vérifiez avec `py --version` et `python --version`. Quelle est la différence entre `py` et `python` ?

### macOS

**Exercice 1.5.3**

Sous macOS : installez Python avec l'installeur officiel ou `brew install python`. Vérifiez avec `python3 --version` et `which python3`.

### Linux

**Exercice 1.5.4**

Sous Linux : installez Python avec le gestionnaire de paquets de votre distribution (`apt`, `dnf`, `pacman`). Pourquoi ne faut-il pas désinstaller le Python du système ?

### Gestionnaires multiplateformes

**Exercice 1.5.5**

Installez `uv` puis utilisez-le pour installer une seconde version de Python et lancer un script avec cette version. Comparez avec `pyenv` ou les autres gestionnaires cités.

### Variables d'environnement (Windows, si `python` n'est pas reconnu)

**Exercice 1.5.6**

Affichez le contenu de la variable `PATH` depuis Python (`os.environ`). Repérez le dossier qui contient l'exécutable `python`. Que faut-il faire si la commande `python` n'est pas reconnue ?

### Vérifier `pip`

**Exercice 1.5.7**

Exécutez `python -m pip --version` et `python -m pip list`. Mettez `pip` à jour. Pourquoi préfère-t-on `python -m pip` à `pip` seul ?

### Vérifier l'installation

**Exercice 1.5.8**

Écrivez un petit script de diagnostic qui affiche : la version de Python, le chemin de l'interpréteur (`sys.executable`), la plateforme, l'encodage par défaut, et le répertoire des paquets.

## 1.6 Choisir un éditeur ou un IDE

**Exercice 1.6.1**

Comparez trois éditeurs ou IDE (par exemple VS Code, PyCharm, Thonny) selon : prix, poids, débogueur, autocomplétion, support de Jupyter, adaptation aux débutants.

### VS Code : extensions recommandées

**Exercice 1.6.2**

Installez dans VS Code les extensions Python recommandées par le cours, puis configurez l'interpréteur sélectionné et le formatage automatique à l'enregistrement.

### Quel outil choisir ?

**Exercice 1.6.3**

Pour chacun des profils suivants, choisissez un outil et justifiez : élève de lycée, data scientist, développeur web, administrateur système qui écrit des scripts, chercheur qui rédige des notebooks.

## 1.7 Exécuter son premier programme

### Mode interactif (REPL)

**Exercice 1.7.1**

Dans le REPL, calculez `2 ** 100`, `10 / 3`, `10 // 3`, `10 % 3`, et `"ab" * 3`. Quittez ensuite proprement l'interpréteur de trois façons différentes.

### Mode script

**Exercice 1.7.2**

Créez un fichier `bonjour.py` qui affiche votre prénom et la date du jour. Exécutez-le avec `python bonjour.py` dans un terminal.

### Comparaison des deux modes

**Exercice 1.7.3**

Remplissez le tableau comparatif des modes interactif et script (persistance du code, réutilisation, tests rapides, partage, automatisation) puis donnez un exemple de situation adaptée à chacun.

### Exécuter depuis un éditeur

**Exercice 1.7.4**

Exécutez votre script depuis votre éditeur (bouton d'exécution, terminal intégré). Où s'affichent les résultats ? Quel interpréteur est utilisé ?

### Autres façons de lancer Python

**Exercice 1.7.5**

Lancez du code avec `python -c "print(1 + 1)"`, `python -m http.server --help`, `python -i script.py` et en exécutant un module avec `python -m nom_module`. Expliquez à quoi sert chaque forme.

### Le *shebang* (Unix)

**Exercice 1.7.6**

Écrivez un script avec un *shebang* (`#!/usr/bin/env python3`), rendez-le exécutable (`chmod +x`) et lancez-le directement avec `./script.py`. Pourquoi `env` est-il préférable à un chemin absolu ?

### Erreurs courantes

**Exercice 1.7.7**

Reproduisez volontairement trois erreurs courantes (`python` non reconnu, `SyntaxError`, mauvais dossier de travail avec `FileNotFoundError`) et notez la correction de chacune.

## 1.8 L'interpréteur Python

### Bytecode

**Exercice 1.8.1**

Utilisez le module `dis` pour afficher le bytecode d'une petite fonction `def f(a, b): return a + b * 2`. Repérez les instructions de chargement, de multiplication et d'addition.

**Exercice 1.8.2**

Où sont stockés les fichiers `.pyc` ? Importez un module et retrouvez son fichier compilé dans `__pycache__`.

### Machine virtuelle (PVM)

**Exercice 1.8.3**

Décrivez en cinq étapes le trajet d'un fichier `.py` jusqu'à son exécution (analyse lexicale et syntaxique, compilation en bytecode, exécution par la machine virtuelle).

### Les implémentations de Python

**Exercice 1.8.4**

Citez quatre implémentations de Python (CPython, PyPy, MicroPython, etc.). Pour chacune, donnez son point fort et un cas d'usage.

### Compilé ou interprété ?

**Exercice 1.8.5**

Python est-il compilé ou interprété ? Rédigez une réponse nuancée en trois phrases, avec les termes « bytecode » et « machine virtuelle ».

### Peut-on exécuter Python sans interpréteur ?

**Exercice 1.8.6**

Recherchez comment distribuer un script Python sous forme d'exécutable autonome (PyInstaller, Nuitka, etc.) et testez-le sur un script minimal. Quelle est la taille obtenue ? Pourquoi est-elle élevée ?

### Options utiles de l'interpréteur

**Exercice 1.8.7**

Testez les options `-V`, `-c`, `-m`, `-i`, `-O`, `-W` et `-X` (dont `-X dev`). Décrivez en une phrase l'effet de chacune.

## 1.9 « Hello, World ! »

**Exercice 1.9.1**

Écrivez un programme `hello.py` qui affiche `Hello, World !`. Modifiez-le pour afficher le message en trois langues sur trois lignes.

### La fonction `print()` en détail

**Exercice 1.9.2**

Prédisez puis vérifiez la sortie de :

```python
print("a", "b", "c")
print("a", "b", "c", sep="-")
print("a", end="")
print("b")
print("x", "y", sep="", end="!\n")
print()
print(1, 2.5, True, None, [1, 2])
```

**Exercice 1.9.3**

Utilisez le paramètre `file` pour écrire un message sur `sys.stderr` et un autre dans un fichier. Utilisez `flush=True` pour afficher immédiatement une barre de progression simple sur une seule ligne.

### Commentaires

**Exercice 1.9.4**

Écrivez un petit programme comportant un commentaire de ligne, un commentaire de fin de ligne et une docstring. Quelle différence y a-t-il entre un commentaire `#` et une chaîne de caractères sur plusieurs lignes laissée seule dans le code ?

### Extensions de fichiers Python

**Exercice 1.9.5**

Associez chaque extension à son rôle : `.py`, `.pyc`, `.pyw`, `.pyi`, `.ipynb`, `.pyd`, `.toml`.

### Comment le code est exécuté

**Exercice 1.9.6**

Écrivez un script `ordre.py` composé de quatre `print` numérotés et d'une définition de fonction non appelée. Expliquez dans quel ordre le code s'exécute et pourquoi le corps de la fonction ne s'exécute pas.

### PEP et documentation

**Exercice 1.9.7**

Lisez la PEP 8 et notez cinq règles de style, puis relisez le code de l'exercice 1.9.2 pour vérifier qu'il les respecte.

### Obtenir de l'aide

**Exercice 1.9.8**

Utilisez `help(str.split)`, `dir(list)` et `str.__doc__` pour répondre sans internet : que fait `str.partition` ? Comment `list.sort` gère-t-il la clé de tri ?

---

# 2. Syntaxe et indentation

---

## 2.1 Introduction à la syntaxe

**Exercice 2.1.1**

Écrivez un programme de 6 lignes qui déclare une variable, utilise une condition `if` et affiche un message. Soulignez dans un commentaire chaque élément syntaxique : mot-clé, expression, bloc, deux-points, indentation.

**Exercice 2.1.2**

Quels symboles de ponctuation d'autres langages (`;`, `{ }`, `( )` autour des conditions) sont facultatifs ou absents en Python ? Écrivez un exemple où une expression est correcte avec et sans parenthèses.

## 2.2 Le rôle de l'indentation

**Exercice 2.2.1**

Corrigez l'indentation de ce code pour qu'il affiche `Pair` pour 4 et `Impair` pour 5 :

```python
def parite(n):
if n % 2 == 0:
print("Pair")
else:
print("Impair")

parite(4)
parite(5)
```

**Exercice 2.2.2**

Qu'affiche ce programme ? Expliquez pourquoi l'indentation d'une seule ligne change le résultat :

```python
for i in range(3):
    print("a", i)
    print("b", i)

for i in range(3):
    print("a", i)
print("b", i)
```

### Règles et bonnes pratiques

**Exercice 2.2.3**

Quelle est la convention d'indentation de la PEP 8 ? Que se passe-t-il quand on mélange tabulations et espaces ? Écrivez un code qui lève une `TabError` ou une `IndentationError` et décrivez le message.

**Exercice 2.2.4**

Configurez votre éditeur pour convertir automatiquement les tabulations en 4 espaces, et vérifiez le résultat sur un fichier de test.

## 2.3 Blocs de code

**Exercice 2.3.1**

Écrivez un programme qui contient quatre niveaux de blocs imbriqués (fonction, boucle, condition, sous-condition) et dessinez à côté l'arbre des blocs.

**Exercice 2.3.2**

Un bloc peut-il être vide ? Écrivez une fonction vide valide de trois façons différentes (`pass`, docstring, `...`) et expliquez le choix de chacune.

**Exercice 2.3.3**

Que renvoie `len(x)` quand `x` est défini dans un bloc `if` non exécuté ? Pourquoi une variable définie dans un bloc `if` reste-t-elle accessible après ce bloc (contrairement à d'autres langages) ?

## 2.4 Instructions simples

**Exercice 2.4.1**

Liste d'instructions simples : écrivez une ligne pour chacune des instructions `pass`, `del`, `return`, `raise`, `import`, `global`, `assert`, `break`, `continue`.

**Exercice 2.4.2**

Peut-on écrire plusieurs instructions sur une ligne avec `;` ? Écrivez un exemple, puis expliquez pourquoi la PEP 8 le déconseille.

### Instructions sur plusieurs lignes

**Exercice 2.4.3**

Écrivez une longue expression de trois façons : avec le caractère de continuation `\`, avec des parenthèses, et avec un littéral de liste réparti sur plusieurs lignes. Quelle forme est recommandée ?

**Exercice 2.4.4**

Réécrivez cette condition longue sur plusieurs lignes lisibles :

```python
if utilisateur.est_actif and utilisateur.age >= 18 and utilisateur.pays in ("FR", "BE", "CH") and not utilisateur.est_bloque:
    autoriser()
```

## 2.5 Sensibilité à la casse

**Exercice 2.5.1**

Déclarez `age`, `Age` et `AGE` avec trois valeurs différentes. Que provoque `print(AGe)` ? Quel type d'exception ?

**Exercice 2.5.2**

Corrigez les erreurs de casse dans :

```python
Print("Bonjour")
x = true
if x == None: pass
For i in range(3): print(i)
```

## 2.6 Expressions et instructions

**Exercice 2.6.1**

Classez chacun des fragments suivants en expression ou instruction : `3 + 4`, `x = 5`, `print("a")`, `if x:`, `[i for i in range(3)]`, `import os`, `lambda x: x`, `a if b else c`, `del x`.

**Exercice 2.6.2**

Utilisez l'opérateur morse `:=` pour lire des lignes avec `while (ligne := input()) != "fin":` et expliquez pourquoi il transforme une affectation en expression.

## 2.7 Lignes vides et espaces

**Exercice 2.7.1**

Réécrivez ce code selon les règles d'espacement de la PEP 8 :

```python
def  addition( a,b ) :
    return a+b
x=addition( 1,2 )
liste=[1 ,2,3 ]
dico={ "a":1,"b" : 2}
```

**Exercice 2.7.2**

Combien de lignes vides doit-on laisser entre deux fonctions de premier niveau ? Entre deux méthodes d'une classe ? Pourquoi ?

## 2.8 Le deux-points `:`

**Exercice 2.8.1**

Énumérez les constructions qui exigent un `:` (`if`, `elif`, `else`, `for`, `while`, `def`, `class`, `try`, `except`, `finally`, `with`, `match`, `case`, `lambda`) et écrivez un exemple de chacune.

**Exercice 2.8.2**

Quels autres usages le `:` a-t-il en Python (découpage, annotations, dictionnaires, f-strings) ? Donnez un exemple pour chacun.

## 2.9 Erreurs de syntaxe et d'indentation

**Exercice 2.9.1**

Pour chaque extrait, identifiez le type d'erreur (`SyntaxError`, `IndentationError`, `TabError`) et corrigez :

```python
print("Bonjour"
if x = 3:
    pass
def f()
    return 1
for i in range(3):
print(i)
x = [1, 2, 3
```

**Exercice 2.9.2**

Les messages d'erreur ont été améliorés dans les versions récentes. Provoquez une erreur de syntaxe sur un mot-clé mal écrit (`esle` au lieu de `else`) et notez le message obtenu et la suggestion éventuelle.

## 2.10 Écrire du code propre (PEP 8)

**Exercice 2.10.1**

Réécrivez ce code en respectant la PEP 8 (noms, espaces, longueur de ligne, style) :

```python
def CalculerTotal(Prix,Quantite):
    Total=Prix*Quantite
    return Total
liste_Des_Prix=[10,20,30]
for p in liste_Des_Prix: print(CalculerTotal(p,2))
```

**Exercice 2.10.2**

Remplacez ce style non pythonique par un style pythonique :

```python
resultat = []
for i in range(len(nombres)):
    if nombres[i] % 2 == 0:
        resultat.append(nombres[i] * 2)
if len(resultat) > 0:
    print("Non vide")
if flag == True:
    print("Vrai")
```

**Exercice 2.10.3**

Installez `ruff` (ou `flake8`) et exécutez-le sur l'un de vos scripts. Notez trois remarques, corrigez-les, puis formatez automatiquement le fichier.

---

# 3. Variables et types de données

---

## 3.1 Les variables

**Exercice 3.1.1**

Déclarez des variables `nom`, `age`, `taille`, `est_etudiant` et `adresse` (valeur `None`) puis affichez-les avec leur type. Que signifie « une variable est une référence vers un objet » ?

**Exercice 3.1.2**

Avec `id()`, vérifiez ce qui se passe en mémoire pour :

```python
a = 10
b = a
b = 20
c = [1, 2]
d = c
d.append(3)
```

Que valent `a`, `b`, `c`, `d` à la fin, et quelles variables partagent le même objet ?

### Règles de nommage

**Exercice 3.1.3**

Parmi les noms suivants, lesquels sont valides ? Justifiez : `age`, `2eme`, `_prive`, `mon-nom`, `nom complet`, `class`, `Prix_TTC`, `é_lève`, `__init__`, `for_`, `x1`, `1x`.

**Exercice 3.1.4**

Quelle convention de nommage la PEP 8 préconise-t-elle pour : variables, fonctions, classes, constantes, modules, paquets, variables « privées » ? Donnez un exemple.

**Exercice 3.1.5**

Pourquoi faut-il éviter de nommer une variable `list`, `str`, `sum` ou `id` ? Montrez en un exemple le problème que cela provoque.

### Affectation

**Exercice 3.1.6**

Écrivez en une seule ligne : l'affectation multiple `a = b = c = 0`, l'affectation parallèle `x, y = 1, 2`, l'échange de deux variables, le déballage `premier, *milieu, dernier = [1, 2, 3, 4, 5]`.

**Exercice 3.1.7**

Que se passe-t-il avec `a, b = 1, 2, 3` ? Avec `a, b = "xy"` ? Avec `a, b = {"k": 1, "l": 2}` ? Vérifiez et expliquez.

## 3.2 Vue d'ensemble des types de base

**Exercice 3.2.1**

Complétez le tableau en donnant un exemple de valeur pour chaque type : `int`, `float`, `complex`, `str`, `bool`, `NoneType`, `list`, `tuple`, `dict`, `set`, `frozenset`, `bytes`, `range`.

**Exercice 3.2.2**

Pour chaque type, indiquez s'il est mutable ou immuable, ordonné ou non, et s'il accepte les doublons.

## 3.3 Types numériques

**Exercice 3.3.1**

Calculez et expliquez les résultats : `7 / 2`, `7 // 2`, `-7 // 2`, `7 % 3`, `-7 % 3`, `2 ** 10`, `2 ** -1`, `divmod(17, 5)`, `abs(-3.5)`, `round(2.5)`, `round(3.5)`, `round(2.675, 2)`.

**Exercice 3.3.2**

Montrez que Python gère les entiers de taille arbitraire en calculant `2 ** 1000` et `factorielle(50)`. Combien de chiffres comptent ces nombres ?

**Exercice 3.3.3**

Écrivez les littéraux `1_000_000`, `0b1010`, `0o17`, `0xFF`, `1e-3`, `3 + 4j`. Affichez leur type et leur valeur décimale.

**Exercice 3.3.4**

Pourquoi `0.1 + 0.2 == 0.3` vaut-il `False` ? Corrigez la comparaison avec `math.isclose` puis avec `decimal.Decimal`. Pour une somme d'argent, quel type préférer ?

**Exercice 3.3.5**

Utilisez les nombres complexes : calculez `(1 + 2j) * (3 - 1j)`, le module avec `abs`, le conjugué, la partie réelle et imaginaire.

**Exercice 3.3.6**

Avec le module `math`, calculez `sqrt(2)`, `pi`, `e`, `ceil(2.1)`, `floor(-2.1)`, `trunc(-2.9)`, `gcd(12, 18)`, `lcm(4, 6)`, `isqrt(99)`, `comb(5, 2)`, `perm(5, 2)`, `factorial(10)`, `log(100, 10)`, `inf`, `nan`. Que vaut `float("nan") == float("nan")` ?

**Exercice 3.3.7**

Écrivez une fonction qui calcule l'aire et le périmètre d'un cercle à partir de son rayon, arrondis à deux décimales, avec formatage.

## 3.4 Chaînes de caractères (`str`)

**Exercice 3.4.1**

Écrivez une chaîne sur plusieurs lignes avec des triples guillemets, une chaîne brute (`r"..."`) contenant `C:\nouveau\test`, et une chaîne contenant à la fois des guillemets simples et doubles.

**Exercice 3.4.2**

Soit `s = "Programmation"`. Calculez : `s[0]`, `s[-1]`, `s[3:7]`, `s[:4]`, `s[4:]`, `s[::2]`, `s[::-1]`, `s[-3:]`, `s[2:2]`, `len(s)`. Pourquoi `s[100]` lève une erreur alors que `s[100:]` n'en lève pas ?

**Exercice 3.4.3**

Écrivez un programme qui vérifie si un mot est un palindrome (en ignorant la casse et les espaces).

**Exercice 3.4.4**

Utilisez les méthodes `upper`, `lower`, `title`, `capitalize`, `swapcase`, `strip`, `lstrip`, `rstrip`, `replace`, `split`, `join`, `find`, `index`, `count`, `startswith`, `endswith`, `isdigit`, `isalpha`, `isalnum`, `zfill`, `center`, `removeprefix`, `removesuffix` sur une chaîne de votre choix. Notez un exemple de chaque.

**Exercice 3.4.5**

Quelle est la différence entre `find` et `index` quand la sous-chaîne est absente ? Entre `split()` et `split(" ")` sur `"a  b   c"` ?

**Exercice 3.4.6**

Écrivez une fonction qui compte les voyelles d'une phrase, puis une fonction qui renvoie la fréquence de chaque caractère sous forme de dictionnaire.

**Exercice 3.4.7**

Pourquoi `s[0] = "X"` lève-t-il une `TypeError` ? Proposez deux façons de remplacer le premier caractère d'une chaîne.

**Exercice 3.4.8**

Comparez la concaténation `s = s + x` dans une boucle et `"".join(liste)` en mesurant le temps avec `timeit` pour 100 000 morceaux. Expliquez la différence.

**Exercice 3.4.9**

Écrivez un chiffrement de César (décalage `n`) en utilisant `ord`, `chr` et `str.translate` avec `str.maketrans`.

### F-strings (formatage moderne)

**Exercice 3.4.10**

Écrivez une f-string qui affiche : `Alice a 25 ans et mesure 1.68 m`, à partir de variables. Utilisez ensuite `{x=}` pour déboguer, `{valeur:.2f}`, `{nombre:,}`, `{pourcent:.1%}`, `{texte:>10}`, `{texte:*^20}`.

**Exercice 3.4.11**

Écrivez une f-string qui contient des accolades littérales, une expression (`{a + b}`), un appel de méthode, un dictionnaire (`{d["clé"]}`). Quelle syntaxe de guillemets pouvez-vous utiliser dans une f-string imbriquée en Python 3.12+ ?

## 3.5 Booléens

**Exercice 3.5.1**

Donnez la valeur de vérité de chacune de ces valeurs avec `bool()` : `0`, `1`, `-1`, `0.0`, `""`, `" "`, `[]`, `[0]`, `{}`, `set()`, `None`, `"False"`.

**Exercice 3.5.2**

Que valent `True + True`, `True * 5`, `sum([True, False, True])` ? Pourquoi `bool` est-il un sous-type de `int` ?

**Exercice 3.5.3**

Écrivez une fonction `est_valide(nom)` qui renvoie `True` si le nom est une chaîne non vide après suppression des espaces, en utilisant la valeur de vérité plutôt qu'une comparaison explicite.

## 3.6 `None`

**Exercice 3.6.1**

Quelle valeur renvoie une fonction sans `return` ? Écrivez un exemple et testez avec `is None`.

**Exercice 3.6.2**

Pourquoi teste-t-on `x is None` et non `x == None` ? Écrivez une classe dont `__eq__` renvoie toujours `True` pour montrer le piège.

**Exercice 3.6.3**

Utilisez `None` comme valeur par défaut d'un paramètre de fonction pour signaler « non fourni », puis distinguez-le de `0`, `""` et `False`.

## 3.7 Conversion de types (*casting*)

**Exercice 3.7.1**

Prédisez la valeur ou l'erreur : `int("42")`, `int("4.2")`, `int(4.9)`, `int(-4.9)`, `float("3.14")`, `float("abc")`, `str(42)`, `bool("0")`, `list("abc")`, `tuple([1, 2])`, `set([1, 1, 2])`, `dict([("a", 1)])`, `int("101", 2)`, `int("ff", 16)`, `chr(65)`, `ord("A")`, `bin(10)`, `hex(255)`, `oct(8)`.

**Exercice 3.7.2**

Écrivez `convertir_en_entier(texte)` qui renvoie un entier ou `None` si la conversion est impossible, sans planter.

**Exercice 3.7.3**

Distinguez conversion implicite et explicite. Que valent `1 + 2.0`, `True + 1`, `"1" + 1` ? Quelle erreur obtient-on avec le dernier ?

## 3.8 Vérifier le type

**Exercice 3.8.1**

Quelle est la différence entre `type(x) == int` et `isinstance(x, int)` ? Testez avec `x = True` et avec une instance d'une sous-classe de `int`.

**Exercice 3.8.2**

Écrivez `decrire(x)` qui renvoie `"nombre"`, `"texte"`, `"collection"` ou `"inconnu"` en utilisant `isinstance` avec un tuple de types.

## 3.9 Types mutables et immuables

**Exercice 3.9.1**

Classez en mutable ou immuable : `int`, `str`, `list`, `tuple`, `dict`, `set`, `frozenset`, `bytes`, `bytearray`, `float`, `bool`.

**Exercice 3.9.2**

Prédisez la sortie, puis expliquez avec `id` :

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)

x = "abc"
y = x
y += "d"
print(x, y)

def ajouter(liste):
    liste.append(99)

def incrementer(n):
    n += 1

l = [1]; n = 1
ajouter(l); incrementer(n)
print(l, n)
```

**Exercice 3.9.3**

Pourquoi un tuple contenant une liste peut-il être « modifié » ? Écrivez `t = ([1], 2)` et `t[0].append(3)`, puis essayez `t[0] += [4]`. Que se passe-t-il exactement ?

## 3.10 Constantes

**Exercice 3.10.1**

Python n'a pas de vraies constantes. Comment signale-t-on une constante par convention ? Écrivez un exemple avec `PI`, `TAUX_TVA`, `JOURS_SEMAINE`.

**Exercice 3.10.2**

Utilisez `typing.Final` pour annoter une constante, et `enum.Enum` ou `types.MappingProxyType` pour une collection constante. Vérifiez avec `mypy` ce qui est détecté.

## 3.11 Portée des variables (règle LEGB)

**Exercice 3.11.1**

Pour chaque nom du code suivant, indiquez s'il est local, englobant, global ou intégré, et prédisez la sortie :

```python
x = "global"

def externe():
    x = "englobante"
    def interne():
        print(x)
    interne()

externe()
print(x)
print(len)
```

**Exercice 3.11.2**

Écrivez un compteur avec `global`, puis une version avec `nonlocal` dans une fonction englobante. Pourquoi `global` est-il généralement déconseillé ?

**Exercice 3.11.3**

Pourquoi ce code lève-t-il une `UnboundLocalError` ? Corrigez-le de deux façons :

```python
total = 0
def ajouter(n):
    total += n
ajouter(5)
```

## 3.12 Bonnes pratiques

**Exercice 3.12.1**

Renommez et corrigez ce code peu clair :

```python
a = 3.5
b = 12
c = a * b * 0.2
l = ["x", "y"]
```

**Exercice 3.12.2**

Écrivez cinq règles de bonnes pratiques sur les variables (noms explicites, initialisation, portée minimale, pas de réutilisation de nom avec un autre type, constantes en majuscules) et illustrez chacune.

---

# 4. Opérateurs et expressions

---

## 4.1 Opérateurs arithmétiques

**Exercice 4.1.1**

Prédisez puis vérifiez : `17 + 5`, `17 - 5`, `17 * 5`, `17 / 5`, `17 // 5`, `17 % 5`, `17 ** 2`, `-17 // 5`, `-17 % 5`, `17.0 // 5`, `2 ** 3 ** 2`, `(2 ** 3) ** 2`.

**Exercice 4.1.2**

Écrivez une fonction `convertir_secondes(s)` qui renvoie `(heures, minutes, secondes)` avec `divmod`.

**Exercice 4.1.3**

Écrivez une fonction `est_divisible(a, b)` et une fonction qui renvoie le dernier chiffre d'un entier, puis la somme de ses chiffres sans convertir en chaîne.

**Exercice 4.1.4**

Que renvoient `"ab" + "cd"`, `"ab" * 3`, `[1] * 3`, `[1] + [2]`, `"a" - "b"`, `{1} + {2}` ? Quelles opérations échouent ?

## 4.2 Opérateurs d'affectation

**Exercice 4.2.1**

Que valent `x` après chaque ligne ?

```python
x = 10
x += 5
x -= 3
x *= 2
x /= 4
x //= 2
x **= 3
x %= 5
x <<= 2
x |= 1
```

**Exercice 4.2.2**

Différence entre `liste += [1]` et `liste = liste + [1]` quand une autre variable référence la même liste ? Vérifiez avec `id`.

**Exercice 4.2.3**

Utilisez l'opérateur morse `:=` pour écrire une boucle qui lit des morceaux d'un flux jusqu'à ce qu'ils soient vides, et pour filtrer en calculant une valeur une seule fois dans une compréhension.

## 4.3 Opérateurs de comparaison

**Exercice 4.3.1**

Évaluez : `1 < 2 < 3`, `1 < 3 < 2`, `3 == 3.0`, `"a" < "b"`, `"Z" < "a"`, `(1, 2) < (1, 3)`, `[1, 2] == [1, 2]`, `"10" < "9"`, `10 < "9"`.

**Exercice 4.3.2**

Écrivez une fonction `entre(x, bas, haut)` avec les comparaisons chaînées. Pourquoi cette syntaxe est-elle plus lisible qu'un `and` ?

**Exercice 4.3.3**

Comment compare-t-on deux chaînes sans tenir compte de la casse ? Pourquoi `casefold` est-il préférable à `lower` pour les langues autres que l'anglais ?

## 4.4 Opérateurs logiques

**Exercice 4.4.1**

Évaluez : `True and False`, `True or False`, `not True`, `0 or "défaut"`, `"" and "x"`, `[] or {}`, `1 and 2`, `0 and 2`, `None or 0 or ""`, `not []`.

**Exercice 4.4.2**

Expliquez l'évaluation paresseuse (court-circuit) avec un exemple où le second opérande lèverait une erreur s'il était évalué (`x != 0 and 10 / x > 1`).

**Exercice 4.4.3**

Utilisez `or` pour définir une valeur par défaut (`nom = saisie or "Anonyme"`). Quel risque si `saisie` vaut `0` ou `""` alors que c'est une valeur valide ?

**Exercice 4.4.4**

Utilisez `any` et `all` pour : vérifier qu'une liste ne contient que des nombres positifs, qu'au moins un mot commence par une majuscule, qu'une chaîne ne contient aucun chiffre.

## 4.5 Opérateurs bit à bit

**Exercice 4.5.1**

Calculez avec `0b1100` et `0b1010` : `&`, `|`, `^`, `~`, `<<`, `>>`. Affichez les résultats en binaire avec `bin` et `format`.

**Exercice 4.5.2**

Écrivez des fonctions pour tester, activer, désactiver et inverser le `n`-ième bit d'un entier.

**Exercice 4.5.3**

Écrivez `est_puissance_de_deux(n)` et `compter_bits(n)` avec des opérateurs bit à bit.

**Exercice 4.5.4**

Représentez des permissions de fichier avec des drapeaux binaires (lecture = 4, écriture = 2, exécution = 1) et écrivez une fonction qui convertit un entier en chaîne `rwx`.

## 4.6 Opérateurs d'identité et d'appartenance

**Exercice 4.6.1**

Prédisez, puis vérifiez avec `is` et `==` : `a = [1]`, `b = [1]`, `c = a` ; `a == b`, `a is b`, `a is c`. Que valent `256 is 256` et `1000 is 1000` selon le contexte ? Pourquoi ne faut-il pas s'y fier ?

**Exercice 4.6.2**

Utilisez `in` et `not in` sur une chaîne, une liste, un ensemble, un dictionnaire (clés), un `range` et un tuple. Quelle est la complexité du test d'appartenance dans une liste et dans un ensemble ?

**Exercice 4.6.3**

Écrivez `contient_voyelle(mot)` avec `in`, puis `filtrer_mots(mots, interdits)` avec un ensemble pour que le test soit rapide.

## 4.7 Priorité et associativité

**Exercice 4.7.1**

Ajoutez les parenthèses implicites et évaluez : `2 + 3 * 4 ** 2`, `-3 ** 2`, `not True or True`, `1 + 2 << 3`, `10 - 4 - 3`, `2 ** 3 ** 2`, `5 > 3 == True`, `not 1 == 2`.

**Exercice 4.7.2**

Classez par priorité décroissante : `**`, `*`, `+`, `==`, `not`, `and`, `or`, `if else`, `lambda`, `:=`, `|`, `&`, `<<`.

**Exercice 4.7.3**

Quels opérateurs sont associatifs à droite ? Écrivez un exemple pour `**` et pour l'affectation chaînée.

## 4.8 Expressions et évaluation

**Exercice 4.8.1**

Écrivez une expression qui renvoie la mention d'une note (`"Très bien"`, `"Bien"`, `"Passable"`, `"Échec"`) en une seule ligne, avec des ternaires. Puis réécrivez-la lisiblement avec `if`/`elif`.

**Exercice 4.8.2**

Quel est l'ordre d'évaluation des arguments dans `f(a(), b(), c())` ? Écrivez un programme qui l'illustre.

## 4.9 Surcharge d'opérateurs (introduction)

**Exercice 4.9.1**

Définissez une classe `Vecteur` avec `__add__`, `__sub__`, `__mul__` (par un scalaire), `__eq__`, `__repr__`, `__neg__`, `__abs__`. Testez `v1 + v2`, `v1 * 3`, `abs(v1)`.

**Exercice 4.9.2**

Ajoutez `__rmul__` pour que `3 * v1` fonctionne. Pourquoi est-ce nécessaire ?

**Exercice 4.9.3**

Définissez `__lt__` et utilisez `functools.total_ordering` pour obtenir toutes les comparaisons. Triez une liste d'objets avec `sorted`.

## 4.10 Pièges courants

**Exercice 4.10.1**

Illustrez chacun des pièges : imprécision des flottants, `is` vs `==`, priorité de `not`, valeur par défaut mutable. Pour chacun, écrivez le code fautif, expliquez et corrigez.

**Exercice 4.10.2**

Que valent `[] == False`, `not []`, `bool([])`, `[] is False` ? Pourquoi `if x == True:` est-il une mauvaise pratique ?

**Exercice 4.10.3**

Pourquoi `a = b = []` est-il un piège ? Écrivez le code et corrigez-le.

## 4.11 Bonnes pratiques

**Exercice 4.11.1**

Réécrivez cette expression dense de façon plus lisible :

```python
r = (a + b) * c / d if a > 0 and b > 0 or c < 0 and not d == 0 else 0
```

**Exercice 4.11.2**

Listez cinq règles de bonnes pratiques sur les expressions (parenthèses explicites, éviter les ternaires imbriqués, `is None`, variables intermédiaires, noms de booléens) et illustrez-les.

---

# 5. Entrées et sorties

---

## 5.1 Introduction

**Exercice 5.1.1**

Citez les flux standard (`stdin`, `stdout`, `stderr`) et expliquez leur lien avec `input` et `print`. Comment les rediriger depuis le terminal (`>`, `<`, `2>`, `|`) ?

**Exercice 5.1.2**

Écrivez un programme qui lit depuis `sys.stdin` toutes les lignes jusqu'à la fin et affiche le nombre de lignes. Testez avec une redirection depuis un fichier et avec un tube (`echo`).

## 5.2 Lire une saisie utilisateur

**Exercice 5.2.1**

Écrivez un programme qui demande le prénom et l'âge de l'utilisateur et affiche `Bonjour X, vous aurez Y ans l'an prochain`. Que renvoie `input` comme type ?

**Exercice 5.2.2**

Écrivez un programme qui lit deux nombres décimaux et affiche leur somme, leur différence, leur produit et leur quotient (avec gestion de la division par zéro).

### Saisie robuste

**Exercice 5.2.3**

Écrivez `lire_entier(message, minimum, maximum)` qui redemande la saisie jusqu'à obtenir un entier valide dans l'intervalle, avec gestion de `ValueError` et des entrées vides.

**Exercice 5.2.4**

Écrivez `lire_oui_non(message)` qui accepte `o`, `oui`, `n`, `non` (insensible à la casse) et renvoie un booléen.

**Exercice 5.2.5**

Gérez l'interruption clavier (`Ctrl-C`, `KeyboardInterrupt`) et la fin de fichier (`Ctrl-D`, `EOFError`) dans une boucle de saisie.

### Plusieurs valeurs sur une ligne

**Exercice 5.2.6**

Lisez trois entiers séparés par des espaces sur une seule ligne avec `map(int, input().split())`. Lisez ensuite une liste de longueur inconnue.

**Exercice 5.2.7**

Lisez des couples `nom:valeur` séparés par des virgules (`a:1,b:2`) et construisez un dictionnaire.

### Mot de passe et arguments

**Exercice 5.2.8**

Utilisez `getpass.getpass` pour lire un mot de passe sans écho. Pourquoi ne faut-il pas utiliser `input` ?

**Exercice 5.2.9**

Écrivez un script qui lit des arguments de la ligne de commande avec `sys.argv`, puis réécrivez-le avec `argparse` (un argument positionnel, une option `--verbeux`, une option `--nombre` avec valeur par défaut).

## 5.3 Afficher dans la console

**Exercice 5.3.1**

Affichez un tableau de multiplication de 1 à 5 en utilisant `print` avec `sep` et `end`.

**Exercice 5.3.2**

Affichez un message sur `stderr` sans qu'il apparaisse dans une redirection de `stdout`. Testez la redirection avec `> sortie.txt`.

**Exercice 5.3.3**

Écrivez un compte à rebours de 5 à 1 qui s'affiche sur une seule ligne (retour chariot `\r`, `end=""`, `flush=True`) avec `time.sleep`.

## 5.4 Formater les sorties

### F-strings (recommandé)

**Exercice 5.4.1**

Écrivez une facture formatée : nom d'article, quantité, prix unitaire, total, avec alignement en colonnes pour trois articles et un total général.

### Spécificateurs de format

**Exercice 5.4.2**

Prédisez la sortie : `f"{3.14159:.2f}"`, `f"{42:05d}"`, `f"{42:>8}"`, `f"{42:<8}|"`, `f"{42:^8}|"`, `f"{1234567:,}"`, `f"{0.256:.1%}"`, `f"{255:x}"`, `f"{255:#b}"`, `f"{1e6:e}"`, `f"{'ab':*^9}"`, `f"{-5:+d}"`.

**Exercice 5.4.3**

Affichez un nombre `x` avec une largeur et une précision passées en variables : `f"{x:{largeur}.{precision}f}"`.

### Autres méthodes

**Exercice 5.4.4**

Écrivez la même phrase avec `%`, `str.format` (arguments positionnels et nommés) et une f-string. Quelle méthode préférez-vous et pourquoi ?

**Exercice 5.4.5**

Utilisez `str.ljust`, `rjust`, `center` pour afficher un tableau aligné, puis la bibliothèque `textwrap` pour couper un long texte à 40 colonnes.

### Template strings (t-strings, Python 3.14+)

**Exercice 5.4.6**

Écrivez un `Template` avec `t"Bonjour {nom}"` et affichez ses attributs `strings` et `interpolations`. Quelle différence avec une f-string ? *(Python 3.14)*

**Exercice 5.4.7**

Écrivez une fonction `html(template)` qui reçoit un objet `Template` et renvoie une chaîne dans laquelle les valeurs interpolées sont échappées avec `html.escape`. Testez avec une entrée malveillante comme `<script>alert(1)</script>`. *(Python 3.14 ; défi)*

## 5.5 Formater les dates et heures

**Exercice 5.5.1**

Affichez la date et l'heure courantes au format `jeudi 22 octobre 2026, 10:30` avec `datetime` et `strftime`. Que faut-il pour obtenir les noms en français (`locale`) ?

**Exercice 5.5.2**

Convertissez `"2026-10-22 10:30"` en objet `datetime` avec `strptime`, ajoutez 90 jours avec `timedelta`, puis reformatez au format `JJ/MM/AAAA`.

**Exercice 5.5.3**

Calculez le nombre de jours entre deux dates saisies, puis votre âge exact en années, mois et jours à partir de votre date de naissance.

**Exercice 5.5.4**

Quelle est la différence entre une date « naïve » et une date « avisée » (avec fuseau horaire) ? Utilisez `zoneinfo.ZoneInfo` pour convertir l'heure de Paris vers celle de Tokyo.

## 5.6 Bonnes pratiques

**Exercice 5.6.1**

Listez cinq bonnes pratiques d'entrées/sorties (valider les saisies, messages clairs, `stderr` pour les erreurs, f-strings, séparer calcul et affichage) et appliquez-les en refactorisant un programme de votre choix.

**Exercice 5.6.2**

Écrivez un petit programme interactif « devine le nombre » avec validation de chaque saisie et affichage soigné.

---

# 6. Structures de contrôle

---

## 6.1 Introduction

**Exercice 6.1.1**

Citez les trois grandes familles de structures de contrôle (séquence, sélection, répétition) et donnez un exemple de chacune. Dessinez l'organigramme d'un programme qui lit un nombre et dit s'il est positif.

## 6.2 Conditions : `if`, `elif`, `else`

**Exercice 6.2.1**

Écrivez un programme qui lit une note sur 20 et affiche une mention (`Insuffisant`, `Passable`, `Assez bien`, `Bien`, `Très bien`) avec `if`/`elif`/`else`.

**Exercice 6.2.2**

Écrivez une fonction `type_triangle(a, b, c)` qui renvoie `"équilatéral"`, `"isocèle"`, `"scalène"` ou `"impossible"` (inégalité triangulaire).

**Exercice 6.2.3**

Écrivez une fonction `est_bissextile(annee)` en une expression. Testez avec 1900, 2000, 2024, 2100.

**Exercice 6.2.4**

Écrivez une fonction qui résout une équation du second degré `ax² + bx + c = 0` et gère les trois cas (deux, une ou aucune solution réelle) ainsi que le cas `a = 0`.

**Exercice 6.2.5**

Que se passe-t-il si l'on écrit `if x = 5:` ? `if x == 5 or 6:` ? Corrigez la deuxième en l'écrivant de deux façons.

**Exercice 6.2.6**

Écrivez le jeu pierre-feuille-ciseaux entre un joueur et l'ordinateur (`random.choice`), avec affichage du résultat de chaque manche.

## 6.3 Opérateur ternaire

**Exercice 6.3.1**

Écrivez en une ligne chacun de ces traitements : le maximum de deux nombres, la valeur absolue, le texte `"pair"` ou `"impair"`, le pluriel d'un mot selon un compteur.

**Exercice 6.3.2**

Pourquoi un ternaire imbriqué est-il à éviter ? Réécrivez `a if x else b if y else c` de manière lisible.

## 6.4 Filtrage par motifs : `match` / `case` *(Python 3.10+)*

**Exercice 6.4.1**

Écrivez une fonction qui, grâce à `match`, renvoie le nom d'un jour à partir d'un entier de 1 à 7, et `"invalide"` sinon. Utilisez `|` pour regrouper le week-end.

**Exercice 6.4.2**

Écrivez une fonction `analyser(commande)` qui reçoit une liste, par exemple `["aller", "nord"]`, `["prendre", "clé"]`, `["quitter"]`, et réagit avec des motifs de séquence et le motif `*reste`.

**Exercice 6.4.3**

Écrivez une fonction qui reçoit un dictionnaire (`{"type": "cercle", "rayon": 3}`, `{"type": "rectangle", "l": 2, "h": 5}`) et calcule l'aire avec des motifs de mapping et des gardes `if`.

**Exercice 6.4.4**

Écrivez une fonction qui utilise des motifs de classe (`case Point(x=0, y=0):`) avec une `dataclass`.

**Exercice 6.4.5**

Quelle différence entre `case x:` (capture) et `case Constante.X:` ou `case "texte":` (valeur) ? Que fait `case _:` ? Montrez le piège où une variable est capturée au lieu d'être comparée.

## 6.5 L'instruction `pass`

**Exercice 6.5.1**

Écrivez une classe vide `Erreur` et une fonction `a_faire()` avec `pass`, puis remplacez-les par `...` et une docstring. Quels sont les usages légitimes de `pass` ?

## 6.6 Boucles : vue d'ensemble

**Exercice 6.6.1**

Pour chacune des tâches suivantes, dites si `for` ou `while` est le plus adapté : parcourir une liste, répéter jusqu'à saisie valide, compter de 1 à 10, lire un fichier ligne par ligne, attendre une condition externe, itérer sur les clés d'un dictionnaire.

## 6.7 La boucle `while`

**Exercice 6.7.1**

Écrivez avec `while` : un compte à rebours de 10 à 0, la somme des entiers de 1 à 100, le nombre de chiffres d'un entier, la suite de Collatz à partir d'un entier donné (longueur de la suite).

**Exercice 6.7.2**

Écrivez un programme qui demande un mot de passe jusqu'à ce qu'il soit correct ou que 3 essais soient épuisés.

**Exercice 6.7.3**

Écrivez une boucle infinie volontaire `while True:` qui sort avec `break` quand l'utilisateur saisit `q`. Comment arrêter une boucle infinie involontaire dans le terminal ?

**Exercice 6.7.4**

Calculez le PGCD de deux entiers avec l'algorithme d'Euclide en une boucle `while`.

## 6.8 La boucle `for`

**Exercice 6.8.1**

Écrivez avec `for` : l'affichage des nombres de 1 à 10, des nombres pairs de 2 à 20, d'un compte à rebours, des lettres d'une chaîne, des éléments d'une liste.

**Exercice 6.8.2**

Calculez avec une boucle `for` : la factorielle de `n`, la moyenne d'une liste, le plus grand élément d'une liste sans utiliser `max`, le nombre d'occurrences d'un élément sans utiliser `count`.

**Exercice 6.8.3**

Affichez la table de multiplication d'un nombre lu au clavier, puis toutes les tables de 1 à 10 sous forme de grille alignée.

**Exercice 6.8.4**

Écrivez un programme qui affiche les nombres premiers inférieurs à 100.

**Exercice 6.8.5**

Écrivez un programme FizzBuzz de 1 à 100 (multiples de 3 : `Fizz`, de 5 : `Buzz`, des deux : `FizzBuzz`).

### Outils de parcours

**Exercice 6.8.6**

Utilisez `range` avec un, deux et trois arguments, y compris un pas négatif. Que renvoie `list(range(5, 0))` ? Pourquoi `range(10**12)` ne consomme-t-il pas de mémoire ?

**Exercice 6.8.7**

Parcourez une liste avec `enumerate` (en démarrant à 1), deux listes en parallèle avec `zip`, un `zip` de longueurs différentes avec `strict=True`, une liste en sens inverse avec `reversed`, une liste triée avec `sorted`.

**Exercice 6.8.8**

Utilisez `itertools.zip_longest` et `itertools.pairwise` pour comparer des éléments consécutifs d'une liste et détecter si elle est triée.

## 6.9 `break`, `continue` et `else` de boucle

**Exercice 6.9.1**

Écrivez une boucle qui s'arrête au premier multiple de 7 supérieur à 50 (`break`) et une boucle qui saute les multiples de 3 (`continue`).

**Exercice 6.9.2**

Écrivez un test de primalité qui utilise la clause `else` d'une boucle `for` (sans variable drapeau). Quand le bloc `else` d'une boucle s'exécute-t-il ?

**Exercice 6.9.3**

Écrivez une recherche d'un élément dans une liste qui affiche « non trouvé » avec le `else` de la boucle.

**Exercice 6.9.4**

Comment sortir de deux boucles imbriquées en Python ? Écrivez trois approches : drapeau, fonction avec `return`, exception.

## 6.10 Boucles imbriquées et motifs

**Exercice 6.10.1**

Affichez les motifs suivants pour `n = 5` avec des boucles imbriquées :

```text
*
**
***
****
*****
```

```text
    *
   ***
  *****
 *******
*********
```

**Exercice 6.10.2**

Affichez la table de multiplication de 1 à 9 sous forme de grille alignée, puis uniquement le triangle supérieur.

**Exercice 6.10.3**

Trouvez tous les triplets pythagoriciens `(a, b, c)` avec `a < b < c ≤ 50`.

**Exercice 6.10.4**

Affichez le triangle de Pascal sur 8 lignes.

**Exercice 6.10.5**

Affichez un damier de 8 × 8 avec les caractères `#` et espace.

## 6.11 Bonnes pratiques

**Exercice 6.11.1**

Réécrivez avec des clauses de garde (retour anticipé) cette fonction trop imbriquée :

```python
def traiter(utilisateur):
    if utilisateur is not None:
        if utilisateur.actif:
            if utilisateur.age >= 18:
                return f"Bienvenue {utilisateur.nom}"
            else:
                return "Mineur"
        else:
            return "Inactif"
    else:
        return "Inconnu"
```

**Exercice 6.11.2**

Remplacez ces boucles par des constructions plus pythonique (`any`, `all`, `sum`, `enumerate`, `zip`, compréhension) :

```python
trouve = False
for x in liste:
    if x > 10:
        trouve = True
        break

total = 0
for i in range(len(liste)):
    total += liste[i]

resultat = []
for a, b in zip(l1, l2):
    resultat.append(a * b)
```

**Exercice 6.11.3**

Rédigez un mini-projet « jeu du pendu » qui met en oeuvre `while`, `for`, `if`/`elif`, `break`, la manipulation de chaînes et un petit dictionnaire de mots.

---

# 7. Dictionnaires

---

## 7.1 Introduction

**Exercice 7.1.1**

Qu'est-ce qu'un dictionnaire ? Donnez trois exemples de données du monde réel qui se modélisent naturellement en dictionnaire. Depuis quelle version de Python l'ordre d'insertion des clés est-il garanti ?

**Exercice 7.1.2**

Comparez dictionnaire, liste et ensemble : pour chacun des besoins suivants, choisissez la structure la plus adaptée et justifiez : annuaire téléphonique, liste de courses ordonnée, jeu de mots-clés sans doublons, compteur d'occurrences.

## 7.2 Créer un dictionnaire

**Exercice 7.2.1**

Créez le dictionnaire `{"nom": "Alice", "age": 25, "ville": "Lyon"}` de quatre manières différentes : littéral, `dict()` avec arguments nommés, `dict()` avec une liste de couples, et `zip`.

**Exercice 7.2.2**

Créez un dictionnaire qui associe chaque lettre de `"python"` à sa position, puis un dictionnaire de tous les entiers de 1 à 5 vers leur carré. Utilisez `dict.fromkeys` pour initialiser un dictionnaire de scores à 0 pour une liste de joueurs.

**Exercice 7.2.3**

Quel piège y a-t-il avec `dict.fromkeys(["a", "b"], [])` ? Montrez-le puis corrigez-le avec une compréhension.

## 7.3 Accéder aux éléments

**Exercice 7.3.1**

Soit `d = {"a": 1, "b": 2}`. Que se passe-t-il pour `d["c"]` ? Pour `d.get("c")` ? Pour `d.get("c", 0)` ? Quelle exception est levée ?

**Exercice 7.3.2**

Écrivez une fonction `valeur_ou_defaut(d, cle, defaut)` de trois façons : avec `try/except`, avec `get`, avec `in`. Quelle est la plus lisible ?

**Exercice 7.3.3**

Écrivez une fonction qui lit une valeur dans un dictionnaire imbriqué (`config["db"]["hote"]`) en renvoyant une valeur par défaut si une clé intermédiaire manque.

## 7.4 Ajouter, modifier, supprimer

**Exercice 7.4.1**

Partez d'un dictionnaire vide. Ajoutez trois clés, modifiez-en une, supprimez-en une avec `del`, puis une autre avec `pop` (avec valeur par défaut). Affichez le dictionnaire à chaque étape.

**Exercice 7.4.2**

Quelle est la différence entre `pop`, `popitem`, `del` et `clear` ? Écrivez un exemple de chacun et indiquez ce qu'ils renvoient.

**Exercice 7.4.3**

Utilisez `setdefault` pour regrouper les mots d'une liste selon leur première lettre. Réécrivez ensuite avec `defaultdict(list)`.

## 7.5 Méthodes principales

**Exercice 7.5.1**

Complétez le tableau en écrivant un exemple pour chaque méthode : `keys`, `values`, `items`, `get`, `pop`, `popitem`, `setdefault`, `update`, `copy`, `clear`.

**Exercice 7.5.2**

Les vues renvoyées par `keys()`, `values()` et `items()` sont dynamiques : montrez-le en modifiant le dictionnaire après avoir récupéré une vue.

**Exercice 7.5.3**

Quelle est la différence entre `copy()` et `copy.deepcopy()` pour un dictionnaire contenant des listes ? Illustrez avec un exemple.

## 7.6 Parcourir un dictionnaire

**Exercice 7.6.1**

Parcourez un dictionnaire de notes (`{"Alice": 15, "Bob": 12}`) de trois façons : clés, valeurs, couples. Affichez `Alice : 15`.

**Exercice 7.6.2**

Écrivez un programme qui trouve l'élève ayant la meilleure note, la moyenne de la classe, et la liste triée des élèves par note décroissante.

**Exercice 7.6.3**

Pourquoi modifier la taille d'un dictionnaire pendant son parcours provoque-t-il une `RuntimeError` ? Écrivez deux façons correctes de supprimer les entrées dont la valeur est nulle.

## 7.7 Compréhensions de dictionnaires

**Exercice 7.7.1**

Écrivez des compréhensions pour : les carrés des 10 premiers entiers, l'inversion clé/valeur d'un dictionnaire, la mise en majuscules des clés, le filtrage des entrées dont la valeur est supérieure à 10.

**Exercice 7.7.2**

Construisez à partir d'une chaîne le dictionnaire de la fréquence de chaque lettre avec une compréhension. Quelle est la complexité ? Proposez une version plus efficace.

## 7.8 Test d'appartenance

**Exercice 7.8.1**

Que teste `"a" in d` ? Comment tester la présence d'une valeur ? Comparez les temps de `k in d` et `v in d.values()` pour 10⁶ éléments.

## 7.9 Dictionnaires imbriqués

**Exercice 7.9.1**

Modélisez une petite école : un dictionnaire de classes, chacune contenant un dictionnaire d'élèves avec leurs notes. Écrivez des fonctions pour ajouter un élève, calculer la moyenne d'une classe, trouver le meilleur élève toutes classes confondues.

**Exercice 7.9.2**

Écrivez une fonction récursive `aplatir(d, prefixe="")` qui transforme `{"a": {"b": 1, "c": {"d": 2}}}` en `{"a.b": 1, "a.c.d": 2}`.

**Exercice 7.9.3**

Pourquoi est-il risqué de copier un dictionnaire imbriqué avec `dict(d)` ? Écrivez le cas problématique et la correction.

## 7.10 Fusionner des dictionnaires

**Exercice 7.10.1**

Fusionnez `{"a": 1, "b": 2}` et `{"b": 3, "c": 4}` avec `update`, avec `|`, avec `|=` et avec le déballage `{**d1, **d2}`. Qui l'emporte en cas de conflit ?

**Exercice 7.10.2**

Écrivez une fonction qui fusionne deux dictionnaires en additionnant les valeurs des clés communes.

**Exercice 7.10.3**

Écrivez une fonction de fusion récursive de deux dictionnaires de configuration (les sous-dictionnaires sont fusionnés au lieu d'être remplacés).

## 7.11 Clés hachables

**Exercice 7.11.1**

Quels types peuvent servir de clés ? Testez des clés `int`, `str`, `tuple`, `frozenset`, `list`, `set`, `dict`. Que signifie « hachable » ?

**Exercice 7.11.2**

Utilisez un tuple `(ligne, colonne)` comme clé pour représenter une grille creuse. Écrivez des fonctions pour modifier et lire une case avec valeur par défaut.

**Exercice 7.11.3**

Quelle condition un objet personnalisé doit-il remplir pour servir de clé (`__hash__` et `__eq__` cohérents) ? Écrivez une classe `Point` hachable.

## 7.12 Le module `collections`

**Exercice 7.12.1**

Avec `Counter`, trouvez les trois mots les plus fréquents d'un texte et comparez les `Counter` de deux textes (addition, soustraction, intersection).

**Exercice 7.12.2**

Avec `defaultdict`, écrivez un index inversé (mot → liste de numéros de lignes) et un graphe sous forme de dictionnaire d'adjacence.

**Exercice 7.12.3**

À quoi servent encore `OrderedDict.move_to_end()` et la comparaison sensible à l'ordre ? Implémentez un cache LRU minimal avec `OrderedDict`.

**Exercice 7.12.4**

Utilisez `ChainMap` pour représenter une configuration à plusieurs niveaux (arguments, environnement, valeurs par défaut).

## 7.13 Dictionnaires et JSON

**Exercice 7.13.1**

Convertissez un dictionnaire en chaîne JSON indentée avec `json.dumps`, puis relisez-la avec `json.loads`. Que devient un tuple ? Une clé entière ? `None` ? `True` ?

**Exercice 7.13.2**

Que se passe-t-il avec `json.dumps({"date": datetime.date.today()})` ? Écrivez deux solutions (paramètre `default`, classe `JSONEncoder`).

**Exercice 7.13.3**

Utilisez `ensure_ascii=False` et `sort_keys=True` et expliquez leur effet sur un dictionnaire contenant des accents.

## 7.14 Performances

**Exercice 7.14.1**

Mesurez avec `timeit` le temps d'une recherche dans une liste de 10⁵ éléments et dans un dictionnaire de même taille. Expliquez par le hachage.

**Exercice 7.14.2**

Écrivez une fonction de recherche des doublons d'une liste en O(n) à l'aide d'un dictionnaire (ou d'un ensemble), puis la version en O(n²) avec deux boucles. Comparez les temps pour 10⁴ éléments.

## 7.15 Programmation fonctionnelle et idiomes

**Exercice 7.15.1**

Triez un dictionnaire par valeur croissante puis décroissante, puis par clé. Trouvez la clé de la plus grande valeur avec `max(d, key=d.get)`.

**Exercice 7.15.2**

Écrivez deux versions d'un compteur de fréquence : avec `get`, et avec `Counter`. Quand préférer chacune ?

**Exercice 7.15.3**

Pour des données à clés fixes (nom, âge, ville), comparez un dictionnaire, une `dataclass` et un `TypedDict`. Écrivez les trois versions et discutez des avantages de chacune.

---

# 8. Listes

---

## 8.1 Introduction

**Exercice 8.1.1**

Citez quatre propriétés d'une liste (ordonnée, mutable, hétérogène, doublons autorisés) et donnez un exemple de code qui illustre chacune.

## 8.2 Créer des listes

**Exercice 8.2.1**

Créez des listes de plusieurs façons : littéral, `list("abc")`, `list(range(5))`, `[0] * 5`, compréhension, `list(map(...))`, `"a b c".split()`.

**Exercice 8.2.2**

Quelle est la différence entre `[]` et `list()` ? Entre `[1] * 3` et `[[1]] * 3` ? Vérifiez avec `id`.

## 8.3 Accéder aux éléments

**Exercice 8.3.1**

Soit `l = [10, 20, 30, 40, 50, 60]`. Calculez `l[0]`, `l[-1]`, `l[1:4]`, `l[:2]`, `l[3:]`, `l[::2]`, `l[::-1]`, `l[-3:]`, `l[1:-1]`, `l[10:]`. Quelle opération lève une erreur ?

**Exercice 8.3.2**

Écrivez des fonctions `premier`, `dernier`, `milieu`, `sans_extremites` qui utilisent le découpage, et gèrent le cas de la liste vide.

**Exercice 8.3.3**

Utilisez l'affectation par tranche : remplacez `l[1:3]` par une liste de taille différente, insérez au milieu avec `l[2:2] = [...]`, supprimez une tranche avec `del`.

## 8.4 Modifier une liste

**Exercice 8.4.1**

Modifiez un élément par indice, une tranche, avec une boucle (doubler chaque élément en place), et par compréhension (nouvelle liste). Quelle approche modifie la liste d'origine ?

**Exercice 8.4.2**

Écrivez une fonction qui remplace toutes les occurrences d'une valeur par une autre en place.

## 8.5 Ajouter des éléments

**Exercice 8.5.1**

Utilisez `append`, `extend`, `insert`, `+`, `+=`. Quelle est la différence entre `l.append([4, 5])` et `l.extend([4, 5])` ?

**Exercice 8.5.2**

Mesurez le temps de 10⁵ insertions en tête avec `insert(0, x)` puis avec `collections.deque.appendleft`. Expliquez.

**Exercice 8.5.3**

Écrivez un programme qui lit des nombres jusqu'à `0` et les stocke dans une liste.

## 8.6 Supprimer des éléments

**Exercice 8.6.1**

Utilisez `remove`, `pop`, `pop(i)`, `del l[i]`, `del l[a:b]`, `clear`. Que lève `remove` quand l'élément est absent ?

**Exercice 8.6.2**

Pourquoi ce code ne supprime-t-il pas tous les éléments pairs ? Corrigez-le de trois façons :

```python
nombres = [1, 2, 4, 6, 7, 8]
for n in nombres:
    if n % 2 == 0:
        nombres.remove(n)
print(nombres)
```

**Exercice 8.6.3**

Écrivez `supprimer_doublons(liste)` qui conserve l'ordre, d'abord avec une boucle, puis avec `dict.fromkeys`.

## 8.7 Rechercher

**Exercice 8.7.1**

Utilisez `in`, `index`, `count`. Que lève `index` si l'élément est absent ? Écrivez `trouver_tous(liste, x)` qui renvoie tous les indices.

**Exercice 8.7.2**

Écrivez une recherche dichotomique dans une liste triée, puis comparez avec `bisect.bisect_left`. Quelle complexité ?

## 8.8 Trier et inverser

**Exercice 8.8.1**

Quelle différence entre `sort()` et `sorted()` ? Que renvoie `sort()` ? Triez `[3, 1, 2]` en ordre croissant puis décroissant, et inversez une liste de trois façons.

**Exercice 8.8.2**

Triez `["banane", "Pomme", "cerise", "abricot"]` de façon insensible à la casse. Que se passe-t-il sans l'argument `key` ?

### Tri personnalisé

**Exercice 8.8.3**

Triez une liste de chaînes par longueur, puis par longueur et ordre alphabétique en cas d'égalité (clé tuple).

**Exercice 8.8.4**

Triez une liste de dictionnaires `{"nom": ..., "age": ...}` par âge décroissant puis par nom croissant, avec `operator.itemgetter`. Utilisez la stabilité du tri pour y arriver en deux passes.

**Exercice 8.8.5**

Triez une liste de listes selon leur deuxième élément. Triez une liste de tuples `(nom, note)` pour obtenir un classement.

## 8.9 Fonctions et méthodes utiles

**Exercice 8.9.1**

Avec `len`, `sum`, `min`, `max`, `any`, `all`, `sorted`, `reversed`, `enumerate`, `zip`, calculez pour une liste de notes : la somme, la moyenne, le minimum, le maximum, l'étendue, la médiane.

**Exercice 8.9.2**

Écrivez `moyenne_ponderee(notes, coefficients)` avec `zip`. Que se passe-t-il si les listes n'ont pas la même longueur ? Utilisez `strict=True`.

**Exercice 8.9.3**

Utilisez `max` et `min` avec `key` sur une liste de mots (le plus long, le plus court) et avec `default` pour une liste vide.

## 8.10 Compréhensions de listes

**Exercice 8.10.1**

Écrivez des compréhensions pour : les carrés de 1 à 10, les multiples de 3 jusqu'à 30, les mots d'une phrase en majuscules, les nombres pairs d'une liste, les paires `(i, j)` avec `i < j` d'un `range(4)`.

**Exercice 8.10.2**

Écrivez une compréhension avec condition `if` et une compréhension avec expression conditionnelle `x if cond else y`. Quelle différence de position et de sens ?

**Exercice 8.10.3**

Aplatissez une liste de listes avec une compréhension à deux niveaux, puis avec `itertools.chain.from_iterable`. Transposez une matrice avec une compréhension et avec `zip(*m)`.

**Exercice 8.10.4**

Quand une compréhension devient-elle illisible ? Réécrivez avec une boucle explicite une compréhension à trois niveaux et conditions multiples.

## 8.11 Copier une liste

**Exercice 8.11.1**

Quelles sont les différences entre `b = a`, `b = a[:]`, `b = a.copy()`, `b = list(a)`, `b = copy.deepcopy(a)` ? Testez sur une liste simple et sur une liste de listes.

**Exercice 8.11.2**

Prédisez la sortie, puis expliquez :

```python
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
b.append([5])
print(a)
print(b)
```

## 8.12 Listes imbriquées et multidimensionnelles

**Exercice 8.12.1**

Créez une matrice 3×3 de zéros de façon correcte, puis de façon fautive (`[[0] * 3] * 3`). Modifiez une case et expliquez le problème.

**Exercice 8.12.2**

Écrivez des fonctions : somme de chaque ligne, somme de chaque colonne, diagonale, transposée, produit de deux matrices.

**Exercice 8.12.3**

Écrivez une fonction qui fait pivoter une matrice carrée de 90 degrés dans le sens horaire.

**Exercice 8.12.4**

Affichez une matrice sous forme alignée. Écrivez la recherche d'un élément dans une matrice et renvoyez ses coordonnées.

## 8.13 Déballage de listes

**Exercice 8.13.1**

Utilisez le déballage pour : séparer la tête et la queue d'une liste (`tete, *queue = l`), prendre le premier et le dernier élément, échanger deux éléments, fusionner deux listes avec `[*a, *b]`.

**Exercice 8.13.2**

Que se passe-t-il avec `a, b = [1, 2, 3]` ? Avec `a, *b, c = [1, 2]` ? Corrigez.

**Exercice 8.13.3**

Appelez `print(*liste, sep=", ")` et une fonction avec des arguments dépliés depuis une liste.

## 8.14 Outils fonctionnels

**Exercice 8.14.1**

Calculez avec `map`, `filter`, `reduce` : les carrés d'une liste, les nombres impairs, le produit de tous les éléments. Réécrivez chaque calcul avec une compréhension et comparez.

**Exercice 8.14.2**

Écrivez la fonction `compose(f, g)` et utilisez `functools.reduce` pour composer une liste de fonctions.

## 8.15 Listes et chaînes

**Exercice 8.15.1**

Découpez `"un deux  trois"` avec `split()` puis `split(" ")`. Reconstituez avec `join`. Inversez l'ordre des mots d'une phrase.

**Exercice 8.15.2**

Écrivez une fonction qui capitalise chaque mot d'une phrase, puis une fonction qui renvoie le mot le plus long.

**Exercice 8.15.3**

Écrivez une fonction qui vérifie si deux mots sont des anagrammes (avec `sorted`, puis avec `Counter`).

## 8.16 Listes comparées aux autres collections

**Exercice 8.16.1**

Complétez le tableau comparatif `list` / `tuple` / `set` / `dict` (ordonné, mutable, doublons, accès par indice, test `in`) sans consulter le cours.

**Exercice 8.16.2**

Implémentez une file avec une liste (`pop(0)`) et avec `collections.deque`. Mesurez les temps pour 10⁵ opérations et expliquez la différence.

**Exercice 8.16.3**

Implémentez une pile (LIFO) avec une liste et utilisez-la pour vérifier si une chaîne de parenthèses `()[]{}` est équilibrée.

---

# 9. Ensembles

---

## 9.1 Introduction

**Exercice 9.1.1**

Citez les propriétés d'un ensemble (non ordonné, sans doublons, éléments hachables, mutable). Donnez un exemple où un ensemble est préférable à une liste.

## 9.2 Créer des ensembles

**Exercice 9.2.1**

Créez : un ensemble par littéral, à partir d'une liste avec doublons, à partir d'une chaîne, un ensemble vide. Pourquoi `{}` ne crée-t-il pas un ensemble vide ?

**Exercice 9.2.2**

Quels éléments peut-on mettre dans un ensemble ? Testez avec des listes, des tuples, des dictionnaires, des ensembles.

**Exercice 9.2.3**

Créez un ensemble par compréhension : les carrés des entiers de 1 à 10, les voyelles d'une phrase.

## 9.3 Accéder aux éléments

**Exercice 9.3.1**

Pourquoi `s[0]` est-il impossible ? Comment parcourir un ensemble ? Comment obtenir un élément quelconque sans le retirer ?

**Exercice 9.3.2**

Testez l'appartenance avec `in`. Comparez le temps pour un ensemble et une liste de 10⁶ éléments.

## 9.4 Ajouter et supprimer

**Exercice 9.4.1**

Utilisez `add`, `update`, `remove`, `discard`, `pop`, `clear`. Quelle différence entre `remove` et `discard` quand l'élément est absent ?

**Exercice 9.4.2**

Que renvoie `pop()` sur un ensemble ? Pourquoi ne peut-on pas prévoir quel élément sera retiré ?

## 9.5 Opérations ensemblistes

**Exercice 9.5.1**

Avec `a = {1, 2, 3, 4}` et `b = {3, 4, 5, 6}`, calculez l'union, l'intersection, la différence `a - b`, la différence symétrique, chacune avec l'opérateur et avec la méthode.

**Exercice 9.5.2**

Sur deux listes de personnes inscrites à deux activités, déterminez : ceux qui font les deux, ceux qui font au moins une, ceux qui font uniquement la première, ceux qui en font exactement une.

**Exercice 9.5.3**

Quelle différence entre `a.union(liste)` et `a | liste` quand le second opérande est une liste ?

**Exercice 9.5.4**

Écrivez la version « en place » de chaque opération (`|=`, `&=`, `-=`, `^=`, `update`, `intersection_update`, etc.).

## 9.6 Comparaisons et sous-ensembles

**Exercice 9.6.1**

Évaluez : `{1, 2} <= {1, 2, 3}`, `{1, 2} < {1, 2}`, `{1, 2} == {2, 1}`, `{1, 2}.isdisjoint({3})`, `{1, 2, 3} >= {1}`, `{1, 2}.issubset([1, 2, 3])`.

**Exercice 9.6.2**

Écrivez une fonction `contient_tous(texte, lettres)` qui vérifie que chaque lettre d'un ensemble apparaît dans un texte (pangramme : toutes les lettres de l'alphabet).

## 9.7 Ensembles figés (`frozenset`)

**Exercice 9.7.1**

Créez un `frozenset`, essayez de le modifier, utilisez-le comme clé de dictionnaire et comme élément d'un autre ensemble.

**Exercice 9.7.2**

Modélisez un graphe non orienté avec un dictionnaire dont les clés sont des `frozenset({u, v})`. Pourquoi cela supprime-t-il le problème de l'ordre des sommets ?

## 9.8 Cas d'usage

**Exercice 9.8.1**

Supprimez les doublons d'une liste en conservant l'ordre, puis sans conserver l'ordre. Quelle méthode est la plus rapide ?

**Exercice 9.8.2**

Trouvez les éléments communs à trois listes, puis les mots d'un texte absents d'un dictionnaire de référence (vérificateur orthographique simple).

**Exercice 9.8.3**

Écrivez `a_des_doublons(liste)` en une ligne avec un ensemble. Écrivez `premier_doublon(liste)` qui renvoie le premier élément répété.

**Exercice 9.8.4**

Résolvez : « Étant donné deux chaînes, quels caractères sont présents dans la première mais pas dans la seconde ? »

## 9.9 Pièges et bonnes pratiques

**Exercice 9.9.1**

Identifiez les pièges : `{}` pour un ensemble vide, ajout d'une liste, dépendance à l'ordre d'itération, modification pendant l'itération. Illustrez chacun et corrigez.

**Exercice 9.9.2**

Listez cinq bonnes pratiques d'usage des ensembles (test d'appartenance, opérations ensemblistes, suppression de doublons, éléments hachables, `frozenset` pour clés) et appliquez-les à un mini-programme.

---

# 10. Tuples

---

## 10.1 Introduction

**Exercice 10.1.1**

Qu'est-ce qu'un tuple ? Quelles sont ses propriétés (ordonné, immuable, hétérogène) ? Citez trois cas où un tuple est préférable à une liste.

## 10.2 Créer des tuples

**Exercice 10.2.1**

Créez un tuple vide, un tuple à un seul élément, un tuple par littéral sans parenthèses, avec `tuple()`, et un tuple à partir d'un générateur. Que vaut `type((5))` ? `type((5,))` ?

**Exercice 10.2.2**

Créez un tuple de cinq éléments de types différents. Affichez sa longueur, son type et celui de chaque élément.

## 10.3 Accéder aux éléments

**Exercice 10.3.1**

Pour `t = (10, 20, 30, 40, 50)`, calculez `t[0]`, `t[-1]`, `t[1:3]`, `t[::-1]`, `t[::2]`. Que renvoie `t[5:]` ?

**Exercice 10.3.2**

Écrivez une fonction `extremes(t)` qui renvoie le premier et le dernier élément d'un tuple.

## 10.4 Opérations et méthodes

**Exercice 10.4.1**

Utilisez `+`, `*`, `in`, `len`, `min`, `max`, `sum`, `sorted`, `count`, `index` sur des tuples. Quel est le type du résultat de `sorted(t)` ?

**Exercice 10.4.2**

Comparez lexicographiquement `(1, 2, 3) < (1, 2, 4)`, `(1, 2) < (1, 2, 0)`, `(2,) > (1, 99)`. Utilisez cette propriété pour trier des tuples `(âge, nom)`.

## 10.5 Déballage

**Exercice 10.5.1**

Utilisez le déballage pour : échanger deux variables, séparer `(x, y, z)`, ignorer une valeur avec `_`, capturer le milieu avec `*`, parcourir une liste de couples dans une boucle `for`.

**Exercice 10.5.2**

Écrivez une fonction qui renvoie `(minimum, maximum, moyenne)` d'une liste et appelez-la avec déballage.

**Exercice 10.5.3**

Que valent `a`, `b`, `c` après `a, (b, c) = 1, (2, 3)` ? Écrivez un déballage imbriqué sur une liste de `(nom, (note1, note2))`.

## 10.6 Immuabilité

**Exercice 10.6.1**

Que se passe-t-il à `t[0] = 5` ? Comment « modifier » un tuple (le convertir en liste, puis revenir) ? Pourquoi cela crée-t-il un nouvel objet ?

**Exercice 10.6.2**

Avec `t = ([1, 2], 3)`, peut-on faire `t[0].append(9)` ? Que valent `id(t)` avant et après ? Quelle nuance cela apporte-t-il à la notion d'immuabilité ?

## 10.7 Tuples comme clés de dictionnaire

**Exercice 10.7.1**

Utilisez des tuples `(x, y)` comme clés pour représenter les cases occupées d'une grille (jeu de la vie, labyrinthe). Écrivez la fonction qui compte les voisins d'une case.

**Exercice 10.7.2**

Implémentez un cache de résultats (mémoïsation) pour une fonction à deux arguments, avec un tuple comme clé.

## 10.8 Tuples ou listes ?

**Exercice 10.8.1**

Pour chaque donnée suivante, choisissez tuple ou liste : coordonnées GPS, liste de courses, ligne d'une base de données, jours de la semaine, éléments à trier, résultat d'une fonction renvoyant plusieurs valeurs.

**Exercice 10.8.2**

Comparez l'espace mémoire (`sys.getsizeof`) et la vitesse de création d'un tuple et d'une liste de 1000 éléments.

## 10.9 Tuples imbriqués

**Exercice 10.9.1**

Soit `data = (("Alice", 25), ("Bob", 30), ("Chloé", 22))`. Calculez l'âge moyen, la liste des noms, le plus jeune, et triez par âge.

**Exercice 10.9.2**

Représentez un polygone comme un tuple de sommets `(x, y)` et écrivez une fonction qui calcule son périmètre.

## 10.10 Cas d'usage et sujets avancés

**Exercice 10.10.1**

Écrivez une fonction `statistiques(*valeurs)` qui renvoie plusieurs valeurs. Pourquoi `*args` est-il un tuple ?

**Exercice 10.10.2**

Utilisez `enumerate` et `zip` pour produire des tuples et construisez un dictionnaire.

### Tuples nommés

**Exercice 10.10.3**

Définissez `Point` avec `collections.namedtuple` puis avec `typing.NamedTuple` (avec valeur par défaut). Accédez aux champs par nom et par indice, utilisez `_replace`, `_asdict`, `_fields`.

**Exercice 10.10.4**

Comparez tuple nommé, dictionnaire et `dataclass` pour représenter un employé : mutabilité, lisibilité, mémoire, déballage.

## 10.11 Erreurs courantes

**Exercice 10.11.1**

Reproduisez chaque erreur du tableau du cours (modification d'un tuple, déballage de trop de valeurs, singleton sans virgule, tuple non hachable, `IndexError`) puis corrigez.

---

# 11. Fonctions

---

## 11.1 Introduction

**Exercice 11.1.1**

Citez trois avantages des fonctions (réutilisation, lisibilité, test) et illustrez-les en refactorisant un programme qui répète trois fois le même calcul.

### Syntaxe

**Exercice 11.1.2**

Écrivez des fonctions : `carre(x)`, `max_de_trois(a, b, c)`, `est_pair(n)`, `salutation(nom)` qui affiche (sans renvoyer), `somme_chiffres(n)`, `est_premier(n)`, `factorielle(n)`.

**Exercice 11.1.3**

Quelle est la différence entre « définir » et « appeler » une fonction ? Quelle erreur obtient-on si on appelle une fonction avant sa définition ?

## 11.2 Paramètres et arguments

**Exercice 11.2.1**

Distinguez paramètre et argument. Écrivez une fonction `presenter(nom, age, ville="Paris")` et appelez-la avec des arguments positionnels, nommés, mixtes. Quels appels sont invalides ?

**Exercice 11.2.2**

Écrivez `somme(*nombres)` qui additionne un nombre quelconque d'arguments et `afficher(**infos)` qui affiche des paires clé/valeur. Écrivez une fonction qui combine `*args` et `**kwargs`.

**Exercice 11.2.3**

Prédisez la sortie de :

```python
def f(a, b=2, *args, c=3, **kwargs):
    print(a, b, args, c, kwargs)

f(1)
f(1, 5)
f(1, 5, 6, 7)
f(1, c=9)
f(1, 2, 3, c=4, d=5)
```

### Paramètres positionnels seuls et nommés seuls

**Exercice 11.2.4**

Écrivez une fonction avec `/` et `*` : `def f(a, b, /, c, *, d)`. Listez les appels valides et invalides parmi `f(1, 2, 3, d=4)`, `f(1, 2, c=3, d=4)`, `f(a=1, b=2, c=3, d=4)`, `f(1, 2, 3, 4)`.

**Exercice 11.2.5**

Dans quels cas utilise-t-on des paramètres nommés seuls (lisibilité, drapeaux booléens) ? Réécrivez `tracer(x, y, True, False)` avec des paramètres nommés seuls.

### Ordre des paramètres

**Exercice 11.2.6**

Donnez l'ordre correct des types de paramètres (positionnels seuls, normaux, `*args`, nommés seuls, `**kwargs`) et écrivez une fonction qui les contient tous.

### Piège : valeur par défaut mutable

**Exercice 11.2.7**

Expliquez et corrigez :

```python
def ajouter(element, liste=[]):
    liste.append(element)
    return liste

print(ajouter(1))
print(ajouter(2))
```

**Exercice 11.2.8**

Pourquoi les valeurs par défaut sont-elles évaluées une seule fois, à la définition ? Montrez-le avec `def f(t=time.time())`.

### Déballage à l'appel

**Exercice 11.2.9**

Appelez `presenter` avec `*liste` et `**dictionnaire`. Que se passe-t-il si une clé du dictionnaire ne correspond à aucun paramètre ?

## 11.3 Valeurs de retour

**Exercice 11.3.1**

Écrivez une fonction qui renvoie plusieurs valeurs (un tuple) : `division(a, b)` renvoie `(quotient, reste)`. Que renvoie une fonction sans `return` ? Avec `return` seul ?

**Exercice 11.3.2**

Écrivez `trouver(liste, x)` qui renvoie l'indice ou `None`. Que se passe-t-il si l'utilisateur écrit `if trouver(l, 0):` quand l'indice vaut 0 ? Corrigez.

**Exercice 11.3.3**

Écrivez une fonction avec plusieurs `return` selon les cas, puis une version avec un seul `return`. Quelle est plus lisible ?

**Exercice 11.3.4**

Qu'est-ce qu'un effet de bord ? Écrivez deux versions d'une fonction qui trie une liste : l'une qui modifie son argument, l'autre qui renvoie une nouvelle liste. Laquelle est préférable ?

## 11.4 Portée et durée de vie

**Exercice 11.4.1**

Prédisez la sortie :

```python
x = 1

def f():
    x = 2
    def g():
        nonlocal x
        x = 3
    g()
    print(x)

f()
print(x)
```

**Exercice 11.4.2**

Écrivez un compteur de deux manières : avec `global`, et avec une fermeture (`nonlocal`). Quels sont les avantages de la fermeture ?

**Exercice 11.4.3**

Qu'est-ce qu'une fermeture ? Écrivez une fabrique `multiplicateur(n)` qui renvoie une fonction multipliant par `n`. Pourquoi l'exemple suivant donne-t-il toujours le dernier indice (liaison tardive) ? Corrigez :

```python
fonctions = [lambda: i for i in range(3)]
print([f() for f in fonctions])
```

## 11.5 Fonctions anonymes (`lambda`)

**Exercice 11.5.1**

Écrivez des `lambda` pour : le carré, la somme de deux nombres, le test de parité, la longueur d'une chaîne. Appelez-les directement.

**Exercice 11.5.2**

Utilisez une `lambda` comme clé de tri : tri d'une liste de tuples par second élément, de chaînes par dernière lettre.

**Exercice 11.5.3**

Pourquoi ne faut-il pas écrire `f = lambda x: x * 2` ? Quelle est la forme recommandée ? Quelles sont les limites d'une `lambda` ?

## 11.6 Fonctions d'ordre supérieur

**Exercice 11.6.1**

Écrivez une fonction `appliquer(f, liste)` qui applique `f` à chaque élément. Écrivez `compose(f, g)` et `appliquer_n_fois(f, n)`.

**Exercice 11.6.2**

Écrivez une fonction `filtrer(predicat, liste)` et utilisez-la avec une fonction nommée et une `lambda`.

### Outils du module `functools`

**Exercice 11.6.3**

Utilisez `functools.partial` pour dériver `carre` et `cube` d'une fonction `puissance(base, exposant)`.

**Exercice 11.6.4**

Utilisez `functools.lru_cache` (ou `cache`) pour accélérer un Fibonacci récursif. Mesurez les temps pour `fib(35)` avec et sans cache et affichez `cache_info()`.

**Exercice 11.6.5**

Utilisez `functools.reduce` pour calculer le produit d'une liste, le maximum d'une liste, et l'aplatissement d'une liste de listes. Utilisez `functools.wraps` : à quoi sert-il ?

## 11.7 Décorateurs

**Exercice 11.7.1**

Écrivez un décorateur `chronometre` qui affiche le temps d'exécution d'une fonction. Appliquez-le à une fonction qui calcule la somme des carrés jusqu'à 10⁶.

**Exercice 11.7.2**

Écrivez un décorateur `journaliser` qui affiche le nom de la fonction, ses arguments et son résultat. Utilisez `functools.wraps` et montrez la différence de `__name__` avec et sans.

**Exercice 11.7.3**

Écrivez un décorateur `verifier_positif` qui lève `ValueError` si un argument numérique est négatif.

**Exercice 11.7.4**

Écrivez un décorateur `reessayer` qui relance une fonction jusqu'à trois fois en cas d'exception.

### Décorateur avec paramètres

**Exercice 11.7.5**

Écrivez `repeter(n)` : un décorateur paramétré qui exécute la fonction décorée `n` fois. Écrivez aussi `reessayer(fois, delai)`.

**Exercice 11.7.6**

Écrivez un décorateur de classe qui ajoute à une classe une méthode `decrire()`. Écrivez un décorateur qui enregistre les fonctions dans un registre (dictionnaire global).

**Exercice 11.7.7**

Empilez deux décorateurs sur une même fonction. Dans quel ordre sont-ils appliqués ? Dans quel ordre s'exécutent-ils ?

## 11.8 Récursivité

**Exercice 11.8.1**

Écrivez de manière récursive : `factorielle`, `somme_liste`, `puissance`, `inverser(chaine)`, `est_palindrome`, `pgcd`, `fibonacci`, `somme_chiffres`.

**Exercice 11.8.2**

Quelle est la limite de récursion par défaut ? Provoquez une `RecursionError` et consultez / modifiez la limite avec `sys.getrecursionlimit` et `sys.setrecursionlimit`. Pourquoi ne faut-il pas abuser de cette dernière ?

**Exercice 11.8.3**

Écrivez les Tours de Hanoï de façon récursive. Combien de déplacements pour `n` disques ?

**Exercice 11.8.4**

Écrivez une fonction récursive qui aplatit une liste imbriquée à profondeur arbitraire et une qui génère toutes les permutations d'une liste.

**Exercice 11.8.5**

Convertissez la factorielle récursive en version itérative. Python optimise-t-il la récursivité terminale ?

## 11.9 Annotations et typage

**Exercice 11.9.1**

Ajoutez des annotations de type à : `def saluer(nom, fois=1)`, une fonction qui renvoie une liste de chaînes, une fonction qui renvoie un entier ou `None`. Quel est l'effet des annotations à l'exécution ?

**Exercice 11.9.2**

Accédez aux annotations avec `__annotations__` et `typing.get_type_hints`.

## 11.10 Docstrings

**Exercice 11.10.1**

Rédigez la docstring d'une fonction `racine(a, b, c)` selon un format de votre choix (Google, NumPy ou reST) : description, paramètres, retour, exceptions, exemple.

**Exercice 11.10.2**

Affichez la docstring avec `help(f)` et `f.__doc__`. Écrivez un exemple `doctest` dans la docstring et exécutez-le avec `python -m doctest -v`.

## 11.11 Fonctions intégrées essentielles

**Exercice 11.11.1**

Pour chaque catégorie du tableau du cours (conversion, séquences, mathématiques, logique, entrées/sorties, introspection, fonctionnel, caractères), écrivez un exemple utilisant au moins trois fonctions.

**Exercice 11.11.2**

Utilisez `vars`, `getattr`, `setattr`, `hasattr`, `callable`, `issubclass`, `iter`, `next` et `repr` sur un objet que vous définissez.

**Exercice 11.11.3**

Écrivez un petit programme qui utilise `zip`, `enumerate`, `sorted`, `reversed`, `min`, `max`, `sum`, `all`, `any` pour analyser une liste de notes d'étudiants.

## 11.12 Bonnes pratiques

**Exercice 11.12.1**

Refactorisez cette fonction qui fait trop de choses en trois fonctions à responsabilité unique :

```python
def traiter(fichier):
    with open(fichier) as f:
        lignes = f.readlines()
    nombres = []
    for l in lignes:
        l = l.strip()
        if l.isdigit():
            nombres.append(int(l))
    total = sum(nombres)
    print("Total :", total)
    print("Moyenne :", total / len(nombres))
```

**Exercice 11.12.2**

Une fonction a sept paramètres. Proposez deux manières de la simplifier (dataclass, dictionnaire de configuration, paramètres nommés seuls).

---

# 12. Itérateurs et générateurs

---

## 12.1 Itérables et itérateurs

**Exercice 12.1.1**

Distinguez itérable et itérateur. Parmi `list`, `str`, `dict`, `set`, `range`, `open(...)`, `zip(...)`, `map(...)`, `enumerate(...)`, lesquels sont des itérateurs ?

**Exercice 12.1.2**

Utilisez `iter()` et `next()` pour parcourir manuellement une liste. Que se passe-t-il à la fin ? Utilisez `next(it, defaut)`.

**Exercice 12.1.3**

Reproduisez le fonctionnement d'une boucle `for` avec un `while True` et `StopIteration`.

**Exercice 12.1.4**

Pourquoi peut-on parcourir une liste plusieurs fois mais pas un itérateur ? Montrez-le avec `map` ou `zip`.

## 12.2 Générateurs

**Exercice 12.2.1**

Écrivez un générateur `compte_a_rebours(n)`, un générateur de la suite de Fibonacci infinie, un générateur des nombres premiers, un générateur qui renvoie les lignes d'un texte sans les espaces de fin.

**Exercice 12.2.2**

Expliquez ce que fait `yield` et comment la fonction se « met en pause ». Écrivez un générateur qui affiche un message avant et après chaque `yield` pour observer l'ordre d'exécution.

**Exercice 12.2.3**

Comparez la mémoire d'une liste de 10⁷ entiers et d'un générateur (`sys.getsizeof`). Pourquoi un générateur est-il plus économe ?

**Exercice 12.2.4**

Utilisez `send()` et `close()` sur un générateur : écrivez un accumulateur de moyenne mobile qui reçoit des valeurs avec `send`.

### Expressions génératrices

**Exercice 12.2.5**

Calculez la somme des carrés de 1 à 10⁶ avec une expression génératrice. Quelle différence de syntaxe et de comportement avec une compréhension de liste ?

**Exercice 12.2.6**

Pourquoi `max(len(m) for m in mots)` est-il préférable à `max([len(m) for m in mots])` pour de grandes entrées ? Qu'arrive-t-il si l'on réutilise un générateur épuisé ?

### `yield from`

**Exercice 12.2.7**

Écrivez un générateur récursif qui parcourt un arbre (dictionnaires imbriqués) avec `yield from`, puis un générateur qui aplatit une liste imbriquée.

**Exercice 12.2.8**

Utilisez `yield from` pour déléguer à un sous-générateur et récupérer sa valeur de retour (`return` dans un générateur).

### Lecture paresseuse d'un gros fichier

**Exercice 12.2.9**

Écrivez un générateur qui lit un fichier ligne par ligne, un second qui filtre les lignes contenant un mot, un troisième qui les met en majuscules, et chaînez-les en pipeline. Pourquoi aucun fichier entier n'est chargé en mémoire ?

**Exercice 12.2.10**

Écrivez un générateur qui lit un fichier par blocs de taille fixe (`read(n)`).

## 12.3 Le module `itertools`

**Exercice 12.3.1**

Utilisez `count`, `cycle`, `repeat`, `islice` : générez les 10 premiers multiples de 7, répétez un motif trois fois, alternez entre trois couleurs sur 8 éléments.

**Exercice 12.3.2**

Utilisez `chain`, `chain.from_iterable`, `zip_longest`, `product`, `permutations`, `combinations`, `combinations_with_replacement` : listez toutes les mains de 2 cartes parmi 5, tous les mots de 3 lettres sur `"ab"`, toutes les permutations de `"abc"`.

**Exercice 12.3.3**

Utilisez `groupby` pour regrouper des mots consécutifs par première lettre. Pourquoi faut-il trier les données avant ?

**Exercice 12.3.4**

Utilisez `accumulate` pour les sommes partielles et le maximum courant. Utilisez `takewhile`, `dropwhile`, `filterfalse`, `starmap`, `tee`, `pairwise`, `batched` sur des exemples de votre choix.

**Exercice 12.3.5**

Écrivez une fonction `fenetres(iterable, n)` qui renvoie toutes les fenêtres glissantes de taille `n`, avec `itertools.islice` et `collections.deque`.

## 12.4 Créer son propre itérateur

**Exercice 12.4.1**

Écrivez une classe `CompteARebours` avec `__iter__` et `__next__` qui itère de `n` à 0.

**Exercice 12.4.2**

Écrivez une classe `Fibonacci` itérable (finie avec une limite, puis infinie), et une classe `Intervalle` réutilisable (chaque appel à `__iter__` renvoie un nouvel itérateur).

**Exercice 12.4.3**

Quelle est la différence entre une classe itérateur et une classe itérable ? Montrez qu'une classe qui renvoie `self` dans `__iter__` ne peut être parcourue qu'une fois.

**Exercice 12.4.4**

Réécrivez la classe `Fibonacci` sous forme de générateur. Comparez la longueur et la lisibilité des deux versions.

---

# 13. Gestion des erreurs

---

## 13.1 Introduction

**Exercice 13.1.1**

Distinguez erreur de syntaxe et exception. Écrivez un exemple de chacune. Pourquoi une exception non gérée interrompt-elle le programme ?

**Exercice 13.1.2**

Provoquez volontairement dix exceptions différentes et notez leur nom : `ZeroDivisionError`, `ValueError`, `TypeError`, `IndexError`, `KeyError`, `AttributeError`, `NameError`, `FileNotFoundError`, `ImportError`, `RecursionError`.

**Exercice 13.1.3**

Lisez une trace d'appels (*traceback*) : écrivez un programme avec trois fonctions imbriquées qui échoue dans la plus profonde, et identifiez le fichier, la ligne, la fonction et le type d'erreur.

## 13.2 `try` / `except`

**Exercice 13.2.1**

Écrivez une fonction `diviser(a, b)` qui gère `ZeroDivisionError` et `TypeError`. Quelle valeur renvoyer dans chaque cas d'erreur ?

**Exercice 13.2.2**

Écrivez une boucle qui demande un entier jusqu'à ce que la saisie soit valide, avec `try/except ValueError`.

**Exercice 13.2.3**

Capturez plusieurs exceptions : avec des blocs `except` séparés, puis avec un tuple `except (A, B):`. Quand choisir l'un ou l'autre ?

**Exercice 13.2.4**

Pourquoi `except:` nu et `except Exception:` trop large sont-ils déconseillés ? Écrivez un exemple où cela masque un bug.

**Exercice 13.2.5**

Que se passe-t-il quand on capture `KeyboardInterrupt` ou `SystemExit` avec un `except:` nu ? Pourquoi `BaseException` est-elle à éviter ?

## 13.3 `else` et `finally`

**Exercice 13.3.1**

Prédisez la sortie de :

```python
def f(x):
    try:
        print("essai")
        r = 10 / x
    except ZeroDivisionError:
        print("division par zéro")
        return None
    else:
        print("succès")
        return r
    finally:
        print("nettoyage")

f(2)
f(0)
```

**Exercice 13.3.2**

Quand le bloc `else` d'un `try` s'exécute-t-il ? Pourquoi est-il préférable de placer du code dans `else` plutôt qu'à la fin du `try` ?

**Exercice 13.3.3**

Que renvoie cette fonction ? Pourquoi est-il déconseillé d'écrire un `return` dans un `finally` ?

```python
def g():
    try:
        return "try"
    finally:
        return "finally"
```

**Exercice 13.3.4**

Écrivez un programme qui ouvre un fichier avec `try/finally` (sans `with`) et garantit sa fermeture. Réécrivez ensuite avec `with`.

## 13.4 Exploiter l'objet exception

**Exercice 13.4.1**

Utilisez `except ValueError as e:` et affichez `e`, `type(e).__name__`, `e.args`, `repr(e)`.

**Exercice 13.4.2**

Utilisez le module `traceback` pour afficher la pile d'appels (`traceback.print_exc`, `format_exc`) dans un bloc `except`.

**Exercice 13.4.3**

Affichez les attributs spécifiques d'une exception, par exemple `FileNotFoundError.filename` et `KeyError.args`.

**Exercice 13.4.4**

Depuis Python 3.11, on peut enrichir une exception avec `add_note`. Ajoutez une note explicative à une exception avant de la relancer. *(Python 3.11)*

## 13.5 Lever des exceptions

**Exercice 13.5.1**

Écrivez `racine_carree(x)` qui lève `ValueError` si `x < 0`. Écrivez `age_valide(age)` qui lève `TypeError` ou `ValueError` selon le cas.

**Exercice 13.5.2**

Quelle exception lever pour : un argument de mauvais type, une valeur hors plage, une clé manquante, une fonctionnalité non implémentée, une ressource introuvable ? Justifiez chaque choix.

**Exercice 13.5.3**

Écrivez une fonction de validation de mot de passe qui lève des exceptions avec des messages précis pour chaque règle violée.

## 13.6 Exceptions personnalisées

**Exercice 13.6.1**

Définissez une hiérarchie : `ErreurBancaire(Exception)`, `SoldeInsuffisant(ErreurBancaire)`, `CompteInconnu(ErreurBancaire)`. Ajoutez des attributs (`solde`, `montant`) et un message.

**Exercice 13.6.2**

Écrivez une classe `CompteBancaire` avec `deposer` et `retirer` qui utilisent ces exceptions. Capturez-les dans un programme de test.

**Exercice 13.6.3**

Pourquoi faire hériter ses exceptions de `Exception` et non de `BaseException` ? Pourquoi créer une exception de base commune à un module ?

## 13.7 Chaînage et relance

**Exercice 13.7.1**

Utilisez `raise ... from ...` pour traduire une `KeyError` en une exception métier `ConfigurationInvalide`. Consultez `__cause__` et `__context__`.

**Exercice 13.7.2**

Que fait `raise` seul dans un bloc `except` ? Écrivez un exemple qui journalise une erreur puis la relance. Quelle différence avec `raise e` ?

**Exercice 13.7.3**

Utilisez `raise ... from None` pour masquer le contexte, et expliquez dans quel cas c'est justifié.

## 13.8 Hiérarchie des exceptions

**Exercice 13.8.1**

Dessinez l'arbre de la hiérarchie : `BaseException`, `Exception`, `ArithmeticError`, `LookupError`, `OSError`, `ValueError`, `TypeError`, etc. Utilisez `ZeroDivisionError.__mro__` pour le vérifier.

**Exercice 13.8.2**

Pourquoi l'ordre des clauses `except` est-il important ? Écrivez un exemple où `except Exception` placé avant `except ValueError` rend ce dernier inatteignable.

**Exercice 13.8.3**

Capturez `LookupError` pour gérer à la fois `IndexError` et `KeyError`, et `OSError` pour regrouper `FileNotFoundError` et `PermissionError`.

## 13.9 Groupes d'exceptions et `except*` *(Python 3.11+)*

**Exercice 13.9.1**

Levez un `ExceptionGroup` contenant un `ValueError` et un `TypeError`. Gérez-les séparément avec `except*`. *(Python 3.11)*

**Exercice 13.9.2**

Quel est le lien entre `except*` et `asyncio.TaskGroup` ? Écrivez un petit exemple avec deux tâches qui échouent. *(Python 3.11)*

**Exercice 13.9.3**

Quelle différence entre `except` et `except*` ? Peut-on les mélanger dans un même `try` ?

## 13.10 Assertions

**Exercice 13.10.1**

Utilisez `assert` pour vérifier une condition interne (`assert x > 0, "x doit être positif"`). Que se passe-t-il avec `python -O` ?

**Exercice 13.10.2**

Quand utiliser `assert` et quand utiliser `raise ValueError` ? Expliquez pourquoi on ne doit pas valider les entrées utilisateur avec `assert`.

**Exercice 13.10.3**

Pourquoi `assert (x > 0, "message")` (avec parenthèses) est-il un piège ? Que dit l'interpréteur ?

## 13.11 Journalisation des erreurs

**Exercice 13.11.1**

Configurez le module `logging` avec un format `date - niveau - message`. Écrivez un message pour chaque niveau (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).

**Exercice 13.11.2**

Journalisez une exception avec `logger.exception(...)` ou `exc_info=True`. Redirigez les logs vers un fichier et vers la console avec deux gestionnaires aux niveaux différents.

**Exercice 13.11.3**

Quelle est la différence entre `print` et `logging` pour tracer un programme ? Pourquoi créer un logger par module avec `logging.getLogger(__name__)` ?

## 13.12 Gestionnaires de contexte et nettoyage

**Exercice 13.12.1**

Écrivez un gestionnaire de contexte avec une classe (`__enter__`, `__exit__`) qui mesure le temps d'un bloc.

**Exercice 13.12.2**

Écrivez le même gestionnaire avec `contextlib.contextmanager` et un générateur. Utilisez `try/finally` autour du `yield`.

**Exercice 13.12.3**

Utilisez `contextlib.suppress`, `contextlib.redirect_stdout`, `contextlib.ExitStack` sur des exemples.

**Exercice 13.12.4**

Que doit renvoyer `__exit__` pour supprimer une exception ? Écrivez un gestionnaire qui ignore un type d'exception précis.

## 13.13 Cas pratiques

### Fichiers

**Exercice 13.13.1**

Écrivez `lire_fichier(chemin)` qui renvoie le contenu ou une chaîne vide et affiche un message en cas de `FileNotFoundError`, `PermissionError` ou `UnicodeDecodeError`.

### Saisie utilisateur

**Exercice 13.13.2**

Écrivez une fonction `saisir_age()` qui valide la saisie (entier, positif, inférieur à 150) en levant et capturant les bonnes exceptions.

### Requêtes web / API

**Exercice 13.13.3**

Écrivez une fonction qui télécharge une URL avec `urllib.request`, gère `URLError`, `HTTPError`, les délais d'attente et un nombre limité de nouvelles tentatives avec attente croissante.

**Exercice 13.13.4**

Écrivez une fonction qui lit un document JSON reçu et gère `json.JSONDecodeError` ainsi que les clés manquantes.

## 13.14 Bonnes pratiques

**Exercice 13.14.1**

Comparez EAFP (« demander pardon ») et LBYL (« regarder avant de sauter ») sur l'accès à une clé de dictionnaire et l'ouverture d'un fichier. Quels sont les avantages de chacun, y compris en cas de concurrence ?

**Exercice 13.14.2**

Corrigez ces mauvaises pratiques :

```python
try:
    traitement()
except:
    pass

try:
    x = int(saisie)
except Exception as e:
    print("Erreur")

def lire(f):
    try:
        return open(f).read()
    except FileNotFoundError:
        return None
```

**Exercice 13.14.3**

Listez cinq règles de gestion des erreurs (exceptions précises, ne pas les avaler, messages clairs, nettoyage garanti, exceptions métier) et appliquez-les à un programme de votre choix.

---

# 14. Gestion des fichiers

---

## 14.1 Introduction

**Exercice 14.1.1**

Citez les grandes catégories de fichiers (texte, binaire) et les opérations de base (ouvrir, lire, écrire, fermer). Pourquoi la gestion d'un fichier doit-elle toujours prévoir les erreurs ?

## 14.2 Ouvrir et fermer un fichier

**Exercice 14.2.1**

Écrivez un programme qui crée un fichier `notes.txt`, y écrit trois lignes puis le relit. Faites-le d'abord avec `open`/`close`, puis avec `with`.

**Exercice 14.2.2**

Décrivez tous les modes d'ouverture : `r`, `w`, `a`, `x`, `r+`, `w+`, `a+`, `b`, `t`. Pour chacun : lecture/écriture, création, troncature, position initiale.

**Exercice 14.2.3**

Pourquoi faut-il préciser `encoding="utf-8"` à l'ouverture ? Que se passe-t-il si l'on ouvre en UTF-8 un fichier écrit en Latin-1 ? Comment gérer l'erreur (`errors="replace"`) ?

**Exercice 14.2.4**

Que se passe-t-il si l'on oublie `close()` sans `with` ? Mesurez en ouvrant des milliers de fichiers dans une boucle sans les fermer.

**Exercice 14.2.5**

Ouvrez deux fichiers dans un seul `with` pour copier le contenu de l'un dans l'autre.

## 14.3 Lire un fichier

**Exercice 14.3.1**

Lisez un fichier de quatre façons : `read()`, `read(n)`, `readline()`, `readlines()`, puis par parcours direct. Comparez la mémoire utilisée et le résultat pour un grand fichier.

**Exercice 14.3.2**

Écrivez un programme qui affiche un fichier avec numéros de lignes, et un autre qui compte les lignes, mots et caractères (comme `wc`).

**Exercice 14.3.3**

Écrivez un programme qui recherche un mot dans un fichier et affiche les lignes qui le contiennent (comme `grep -n`), insensible à la casse.

**Exercice 14.3.4**

Écrivez `dernieres_lignes(chemin, n)` qui renvoie les `n` dernières lignes d'un gros fichier sans le charger entièrement (avec `collections.deque(maxlen=n)`).

**Exercice 14.3.5**

Pourquoi les lignes lues contiennent-elles `\n` ? Écrivez trois façons de le retirer. Que se passe-t-il pour la dernière ligne sans retour à la ligne ?

## 14.4 Écrire dans un fichier

**Exercice 14.4.1**

Utilisez `write`, `writelines`, `print(..., file=f)` pour écrire une liste de lignes. Quelle méthode ajoute automatiquement un retour à la ligne ?

**Exercice 14.4.2**

Écrivez un journal où chaque exécution ajoute une ligne horodatée à la fin d'un fichier (mode `a`).

**Exercice 14.4.3**

Écrivez un programme qui lit un fichier et écrit une version en majuscules dans un autre, sans jamais charger le fichier entier en mémoire.

**Exercice 14.4.4**

Quelle est la différence entre `flush()` et `close()` ? Quand utiliser `os.fsync` ?

## 14.5 Chemins de fichiers avec `pathlib`

**Exercice 14.5.1**

Avec `Path`, construisez un chemin avec `/`, récupérez `name`, `stem`, `suffix`, `parent`, `parts`, `is_file()`, `exists()`, `resolve()`, `with_suffix`, `with_name`.

**Exercice 14.5.2**

Utilisez `Path.cwd()`, `Path.home()`, `iterdir()`, `glob("*.py")`, `rglob("*.txt")` pour lister les fichiers Python d'un dossier et de ses sous-dossiers, avec leur taille.

**Exercice 14.5.3**

Écrivez un programme qui range les fichiers d'un dossier dans des sous-dossiers selon leur extension.

**Exercice 14.5.4**

Utilisez `Path.read_text`, `write_text`, `read_bytes`, `write_bytes`. Quand sont-ils préférables à `open` ?

**Exercice 14.5.5**

Pourquoi `os.path.join` ou `pathlib` valent-ils mieux que la concaténation de chaînes avec `/` ou `\\` ?

## 14.6 Opérations sur fichiers et dossiers

**Exercice 14.6.1**

Créez un dossier et ses sous-dossiers (`mkdir(parents=True, exist_ok=True)`), copiez un fichier (`shutil.copy`, `copy2`), déplacez-le (`shutil.move`), renommez-le (`rename`), supprimez-le (`unlink`) puis supprimez le dossier (`shutil.rmtree`).

**Exercice 14.6.2**

Écrivez un programme qui calcule la taille totale d'un dossier et liste les cinq plus gros fichiers.

**Exercice 14.6.3**

Écrivez un programme de renommage en masse (ajout d'un préfixe, numérotation) avec une option « simulation » qui affiche sans exécuter.

**Exercice 14.6.4**

Utilisez `os.walk` pour parcourir un arbre de dossiers et trouver les fichiers en double (même taille puis même empreinte `hashlib.sha256`). *(défi)*

**Exercice 14.6.5**

Écrivez un programme qui supprime en toute sécurité les fichiers temporaires `.tmp` d'un dossier, avec confirmation et gestion des erreurs de permission.

## 14.7 Fichiers binaires

**Exercice 14.7.1**

Copiez un fichier image en mode binaire par blocs de 8192 octets. Vérifiez l'égalité des deux fichiers avec leurs empreintes.

**Exercice 14.7.2**

Lisez les premiers octets d'un fichier PNG ou PDF et vérifiez sa signature (numéro magique). Affichez-les en hexadécimal.

**Exercice 14.7.3**

Utilisez `struct.pack` / `struct.unpack` pour écrire et relire un enregistrement binaire `(entier, flottant, chaîne de 10 octets)`.

**Exercice 14.7.4**

Utilisez `bytes` et `bytearray` : encodez et décodez une chaîne, modifiez un `bytearray`, convertissez en hexadécimal avec `hex()` et `bytes.fromhex`.

## 14.8 Position dans le fichier (curseur)

**Exercice 14.8.1**

Utilisez `tell()` et `seek()` pour lire les 10 derniers caractères d'un fichier, puis revenir au début. Quels sont les trois modes de `seek` (`whence`) ? Pourquoi `seek` relatif à la fin est-il limité en mode texte ?

**Exercice 14.8.2**

Écrivez un « fichier base de données » d'enregistrements de taille fixe et lisez/modifiez le `k`-ième enregistrement directement avec `seek`.

## 14.9 Fichiers CSV

**Exercice 14.9.1**

Écrivez un fichier CSV de 5 personnes (nom, âge, ville) avec `csv.writer`, puis relisez-le avec `csv.reader`. Pourquoi faut-il ouvrir avec `newline=""` ?

**Exercice 14.9.2**

Utilisez `csv.DictReader` et `csv.DictWriter` : lisez un CSV, calculez la moyenne d'une colonne, filtrez les lignes selon une condition et écrivez le résultat dans un nouveau fichier.

**Exercice 14.9.3**

Gérez un CSV avec un séparateur différent (`;`) et des champs contenant des virgules et des guillemets. Utilisez le paramètre `delimiter` et `quoting`.

**Exercice 14.9.4**

Écrivez un petit programme qui lit un CSV de ventes (produit, quantité, prix) et affiche le chiffre d'affaires par produit, trié par ordre décroissant.

## 14.10 Fichiers JSON

**Exercice 14.10.1**

Écrivez un dictionnaire imbriqué dans un fichier JSON avec `json.dump` (`indent=2`, `ensure_ascii=False`), puis relisez-le avec `json.load`. Comparez les deux objets.

**Exercice 14.10.2**

Écrivez un petit carnet d'adresses persistant en JSON : ajout, recherche, suppression, avec sauvegarde à chaque modification.

**Exercice 14.10.3**

Quels types Python ne sont pas sérialisables en JSON (`set`, `datetime`, `Decimal`, classes personnalisées) ? Écrivez un encodeur personnalisé qui les gère.

**Exercice 14.10.4**

Que fait le format JSON Lines (un objet JSON par ligne) ? Écrivez un programme qui lit et écrit ce format pour de gros volumes.

## 14.11 Fichiers de configuration TOML *(3.11+)*

**Exercice 14.11.1**

Écrivez un fichier TOML de configuration (section `[serveur]`, `[base]`, une liste, un booléen), lisez-le avec `tomllib` et affichez chaque valeur. Pourquoi `tomllib` ne sait-il que lire ? *(Python 3.11)*

**Exercice 14.11.2**

Écrivez une fonction `charger_config(chemin)` qui fusionne les valeurs du fichier avec des valeurs par défaut et valide les types.

## 14.12 Sérialisation avec `pickle`

**Exercice 14.12.1**

Sauvegardez et rechargez un objet Python complexe (dictionnaire, liste, instance d'une classe) avec `pickle`.

**Exercice 14.12.2**

Quel est le risque de sécurité de `pickle.load` sur des données non fiables ? Citez deux alternatives plus sûres (JSON, `msgpack`, `shelve` pour des cas locaux).

**Exercice 14.12.3**

Utilisez le module `shelve` pour créer un dictionnaire persistant sur disque.

## 14.13 Compression et archives

**Exercice 14.13.1**

Compressez un fichier texte avec `gzip`, puis décompressez-le. Comparez les tailles. Utilisez aussi `zipfile` pour créer une archive de plusieurs fichiers et en extraire un seul.

**Exercice 14.13.2**

Utilisez `shutil.make_archive` et `shutil.unpack_archive` pour archiver un dossier. Utilisez `tarfile` avec compression.

**Exercice 14.13.3**

Python 3.14 introduit le module `compression.zstd`. Écrivez un petit programme qui compresse un fichier avec Zstandard et mesurez le gain par rapport à `gzip`. *(Python 3.14)*

**Exercice 14.13.4**

Pourquoi faut-il se méfier des noms de fichiers à l'extraction d'une archive non fiable (attaque *zip slip*) ? Quelles vérifications ajouter ?

## 14.14 Permissions et métadonnées

**Exercice 14.14.1**

Affichez avec `os.stat` ou `Path.stat` la taille, la date de modification, les permissions d'un fichier, au format lisible (`datetime`, `stat.filemode`).

**Exercice 14.14.2**

Changez les permissions avec `os.chmod` et testez l'accès avec `os.access`. Modifiez la date de modification avec `os.utime`.

**Exercice 14.14.3**

Écrivez un programme qui liste les fichiers modifiés dans les dernières 24 heures dans un dossier.

## 14.15 Exceptions courantes

**Exercice 14.15.1**

Provoquez et gérez : `FileNotFoundError`, `PermissionError`, `IsADirectoryError`, `NotADirectoryError`, `FileExistsError`, `UnicodeDecodeError`. Pour chacune, notez la cause.

**Exercice 14.15.2**

Écrivez une fonction `lire_fichier_sur(chemin)` qui traite toutes ces erreurs avec des messages utiles et renvoie un résultat explicite.

## 14.16 Sujets avancés

**Exercice 14.16.1**

Utilisez `tempfile.NamedTemporaryFile` et `tempfile.TemporaryDirectory` pour des tests qui ne laissent aucune trace.

**Exercice 14.16.2**

Implémentez l'écriture atomique : écrire dans un fichier temporaire du même dossier puis remplacer le fichier cible avec `os.replace`. Pourquoi est-ce plus sûr qu'une écriture directe ?

**Exercice 14.16.3**

Utilisez `mmap` pour chercher un motif dans un fichier volumineux sans le charger entièrement. Quel est l'intérêt face à `read()` ? *(défi)*

**Exercice 14.16.4**

Traitez un fichier de plusieurs gigaoctets : proposez une stratégie (lecture par blocs, générateurs, `itertools`) et écrivez un programme qui calcule des statistiques sur ses lignes avec une mémoire constante.

---

# 15. Modules, paquets et environnements virtuels

---

## 15.1 Modules

**Exercice 15.1.1**

Importez le module `math` de quatre façons : `import math`, `import math as m`, `from math import sqrt`, `from math import *`. Quels sont les avantages et inconvénients de chacune ?

**Exercice 15.1.2**

Créez un module `outils.py` contenant trois fonctions et une constante, puis importez-le depuis un autre fichier. Que se passe-t-il si les deux fichiers ne sont pas dans le même dossier ?

**Exercice 15.1.3**

Affichez `__name__`, `__file__`, `__doc__` et `dir()` pour votre module. Utilisez `importlib.reload` après avoir modifié le module. Pourquoi un module n'est-il exécuté qu'une fois à l'import ?

### Le point d'entrée `__main__`

**Exercice 15.1.4**

Écrivez un module qui exécute un test de démonstration seulement quand il est lancé directement (`if __name__ == "__main__":`), pas quand il est importé. Vérifiez les deux cas.

**Exercice 15.1.5**

Écrivez une fonction `main()` et un point d'entrée propre qui utilise `sys.exit(main())`. Quel est le code de sortie d'un script qui se termine normalement ? Sur erreur ?

**Exercice 15.1.6**

Qu'est-ce qu'un import circulaire ? Écrivez deux modules qui s'importent mutuellement, constatez l'erreur et proposez deux solutions.

## 15.2 Paquets

**Exercice 15.2.1**

Créez un paquet `geometrie` avec les modules `cercle.py`, `rectangle.py` et un fichier `__init__.py`. Importez-en les fonctions de plusieurs façons.

**Exercice 15.2.2**

Quel est le rôle de `__init__.py` ? Qu'est-ce qu'un paquet espace de noms (*namespace package*) sans `__init__.py` ?

**Exercice 15.2.3**

Utilisez `__all__` dans un module ou un paquet pour contrôler ce qui est exporté par `from paquet import *`.

**Exercice 15.2.4**

Écrivez des imports relatifs (`from . import x`, `from .. import y`) dans un sous-paquet. Pourquoi échouent-ils quand on exécute le fichier directement, et comment lancer avec `python -m` ?

**Exercice 15.2.5**

Ajoutez un fichier `__main__.py` dans votre paquet pour qu'on puisse le lancer avec `python -m geometrie`.

## 15.3 Recherche des modules

**Exercice 15.3.1**

Affichez `sys.path` et expliquez l'ordre de recherche (dossier du script, `PYTHONPATH`, bibliothèque standard, `site-packages`).

**Exercice 15.3.2**

Utilisez `sys.modules`, `importlib.util.find_spec` et `module.__file__` pour retrouver l'emplacement d'un module installé.

**Exercice 15.3.3**

Créez un module qui porte le nom d'un module standard (`random.py`) et constatez le problème de masquage (*shadowing*). Comment l'éviter ?

## 15.4 `pip` : installer des paquets

**Exercice 15.4.1**

Installez, mettez à jour et désinstallez un paquet (`requests`) avec `python -m pip`. Affichez ses informations avec `pip show` et la liste des paquets avec `pip list`.

**Exercice 15.4.2**

Générez un fichier `requirements.txt` avec `pip freeze` puis réinstallez les dépendances dans un nouvel environnement. Quelle est la différence entre `requests`, `requests==2.31.0` et `requests>=2.31,<3` ?

**Exercice 15.4.3**

Installez un paquet à partir d'un dépôt Git ou d'un fichier local, et en mode éditable (`pip install -e .`). À quoi sert ce mode ?

**Exercice 15.4.4**

Que fait `pip check` ? Qu'est-ce que le « verrouillage » des dépendances et pourquoi est-il utile en production ?

## 15.5 Environnements virtuels

**Exercice 15.5.1**

Créez un environnement virtuel avec `python -m venv .venv`, activez-le (selon votre système), installez un paquet, vérifiez que `pip list` y est isolé du système, puis désactivez-le.

**Exercice 15.5.2**

Où sont installés les paquets dans l'environnement ? Que contient le dossier `.venv` ? Pourquoi ne faut-il pas le versionner dans Git (`.gitignore`) ?

**Exercice 15.5.3**

Comment vérifier depuis Python qu'on est dans un environnement virtuel (`sys.prefix`, `sys.base_prefix`) ? Écrivez un script qui l'affiche.

**Exercice 15.5.4**

Créez deux environnements avec des versions différentes d'un même paquet et montrez que deux projets peuvent coexister sans conflit.

## 15.6 Outils modernes de gestion de projet

**Exercice 15.6.1**

Avec `uv`, créez un projet (`uv init`), ajoutez une dépendance (`uv add`), lancez un script (`uv run`) et verrouillez les versions. Comparez avec la méthode `venv` + `pip`.

**Exercice 15.6.2**

Comparez `uv`, Poetry, PDM, Hatch et `pipx` : rôle, points forts, cas d'usage. Pour installer un outil en ligne de commande comme `ruff` sans polluer vos projets, quel outil choisir ?

## 15.7 `pyproject.toml`

**Exercice 15.7.1**

Écrivez un `pyproject.toml` minimal pour un projet avec nom, version, description, dépendances et version minimale de Python, plus des sections `[tool.ruff]` et `[tool.pytest.ini_options]`.

**Exercice 15.7.2**

Ajoutez un point d'entrée en ligne de commande (`[project.scripts]`) qui lance votre fonction `main`. Installez le projet en mode éditable et lancez la commande.

**Exercice 15.7.3**

Quelle est la différence entre `dependencies` et `optional-dependencies` ? Ajoutez un groupe `dev` avec `pytest` et `ruff`.

## 15.8 Bibliothèque standard : modules incontournables

**Exercice 15.8.1**

Pour chaque ligne du tableau du cours, écrivez un petit programme qui utilise au moins un module : `pathlib`/`shutil`, `json`/`csv`/`sqlite3`, `datetime`/`zoneinfo`, `re`, `collections`/`itertools`/`functools`, `argparse`/`logging`, `random`/`statistics`/`decimal`, `subprocess`, `dataclasses`/`enum`.

**Exercice 15.8.2**

Utilisez `re` pour extraire d'un texte les adresses e-mail et les numéros de téléphone français. Utilisez `re.compile`, les groupes nommés, `findall`, `sub`.

**Exercice 15.8.3**

Utilisez `sqlite3` pour créer une base en mémoire, une table `clients`, insérer des lignes avec des paramètres (`?`) et les interroger. Pourquoi ne faut-il jamais construire une requête SQL par concaténation de chaînes ?

**Exercice 15.8.4**

Utilisez `subprocess.run` pour exécuter une commande système et récupérer sa sortie. Pourquoi éviter `shell=True` avec des entrées utilisateur ?

**Exercice 15.8.5**

Utilisez `statistics` (moyenne, médiane, écart-type, mode) et `random` (`seed`, `choice`, `sample`, `shuffle`) sur un échantillon de données. Pourquoi `random` ne convient-il pas à la cryptographie ? Quel module utiliser (`secrets`) ?

---

# 16. Programmation orientée objet

---

## 16.1 Concepts fondamentaux

**Exercice 16.1.1**

Définissez les termes : classe, objet, instance, attribut, méthode, constructeur, `self`. Donnez un exemple concret du monde réel.

### Définir une classe

**Exercice 16.1.2**

Écrivez une classe `Personne` avec un constructeur (`nom`, `age`), une méthode `se_presenter`, une méthode `anniversaire` qui incrémente l'âge, et `__repr__`.

**Exercice 16.1.3**

Quelle différence entre un attribut d'instance et un attribut de classe ? Écrivez une classe `Compteur` qui compte le nombre d'instances créées avec un attribut de classe.

**Exercice 16.1.4**

Que se passe-t-il si on oublie `self` dans la définition d'une méthode ? Que représente `self` exactement ? Écrivez `Classe.methode(instance)` et `instance.methode()` pour montrer l'équivalence.

**Exercice 16.1.5**

Écrivez une classe `Rectangle` (largeur, hauteur) avec `aire`, `perimetre`, `est_carre` et `__str__`. Écrivez aussi une classe `Cercle`.

**Exercice 16.1.6**

Écrivez une classe `Pile` (LIFO) avec `empiler`, `depiler`, `sommet`, `est_vide`, `__len__`. Écrivez ensuite une classe `File` (FIFO).

## 16.2 Encapsulation et propriétés

**Exercice 16.2.1**

Expliquez les conventions `_attribut` (protégé), `__attribut` (privé par renommage) et `attribut`. Montrez la transformation de nom (*name mangling*) avec `_Classe__attribut`.

**Exercice 16.2.2**

Écrivez une classe `CompteBancaire` avec un solde privé, un dépôt, un retrait (avec vérification) et une propriété en lecture seule `solde`.

**Exercice 16.2.3**

Utilisez `@property`, `@x.setter` et `@x.deleter` pour contrôler un attribut `temperature` en Celsius, avec une propriété calculée `fahrenheit`. Validez que la température est supérieure au zéro absolu.

**Exercice 16.2.4**

Pourquoi les propriétés permettent-elles d'ajouter de la validation sans changer l'interface publique d'une classe ? Illustrez avec une classe qui passe d'un attribut simple à une propriété.

**Exercice 16.2.5**

Utilisez `functools.cached_property` pour mettre en cache une valeur coûteuse à calculer. Quand est-elle recalculée ?

## 16.3 Méthodes de classe et statiques

**Exercice 16.3.1**

Écrivez une classe `Date` avec un constructeur `(jour, mois, annee)` et une méthode de classe `depuis_chaine("2026-10-22")` (constructeur alternatif).

**Exercice 16.3.2**

Écrivez une méthode statique `est_valide(jour, mois, annee)`. Quand choisir `@staticmethod`, `@classmethod` ou une méthode d'instance ?

**Exercice 16.3.3**

Utilisez `cls` dans une méthode de classe pour qu'elle fonctionne correctement avec les sous-classes (`Date.depuis_chaine` hérité par `DateHeure`).

## 16.4 Héritage

**Exercice 16.4.1**

Écrivez une classe `Animal` (nom, son) et trois sous-classes `Chien`, `Chat`, `Oiseau` qui redéfinissent `parler`. Utilisez `super().__init__`.

**Exercice 16.4.2**

Créez une hiérarchie `Employe` → `Manager`, `Developpeur`, avec un salaire calculé différemment dans chaque classe. Écrivez une fonction qui calcule la masse salariale d'une liste d'employés.

**Exercice 16.4.3**

Utilisez `isinstance` et `issubclass` pour tester les relations. Pourquoi est-il préférable d'utiliser le polymorphisme plutôt que des `if isinstance(...)` en cascade ?

**Exercice 16.4.4**

Redéfinissez une méthode en appelant d'abord celle du parent avec `super()`, puis en ajoutant un comportement. Que se passe-t-il si l'on oublie d'appeler `super().__init__()` ?

### Héritage multiple et MRO

**Exercice 16.4.5**

Créez le « problème du diamant » (`A`, `B(A)`, `C(A)`, `D(B, C)`) avec une méthode `hello` dans chaque classe qui appelle `super().hello()`. Affichez `D.__mro__` et l'ordre d'appel. Expliquez l'algorithme C3.

**Exercice 16.4.6**

Quand l'héritage multiple est-il pertinent et quand l'éviter ? Proposez une alternative par composition.

### Mixins

**Exercice 16.4.7**

Écrivez un mixin `JsonMixin` qui ajoute `vers_json()` à n'importe quelle classe et un mixin `ComparableMixin`. Appliquez-les à une classe `Produit`.

**Exercice 16.4.8**

Quelle est la différence entre héritage (« est un ») et composition (« a un ») ? Modélisez une `Voiture` qui contient un `Moteur` et comparez à une version par héritage.

## 16.5 Polymorphisme et *duck typing*

**Exercice 16.5.1**

Écrivez trois classes (`Canard`, `Robot`, `Chat`) qui ont toutes une méthode `bouger` sans classe commune. Écrivez une fonction qui appelle `bouger()` sur chacune. Quel principe est illustré ?

**Exercice 16.5.2**

Écrivez une fonction `aire_totale(formes)` qui additionne les aires de formes variées (cercle, rectangle, triangle) en se basant sur le polymorphisme.

**Exercice 16.5.3**

Distinguez le typage nominal et le typage structurel. Écrivez un `Protocol` pour un objet « fermable » et deux classes qui le respectent sans en hériter. *(voir 16.9)*

## 16.6 Méthodes spéciales (« dunder »)

**Exercice 16.6.1**

Écrivez une classe `Fraction` avec `__init__`, `__repr__`, `__str__`, `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__eq__`, `__lt__`, `__hash__`, `__bool__`, `__float__`. Simplifiez automatiquement les fractions.

**Exercice 16.6.2**

Distinguez `__str__` et `__repr__`. Quelle méthode est utilisée par `print`, par la console interactive, dans une liste ? Écrivez une classe qui respecte la convention `repr` (une représentation qui ressemble à du code).

**Exercice 16.6.3**

Écrivez une classe `Collection` qui implémente `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `__iter__`, `__reversed__`. Vérifiez qu'elle se comporte comme une séquence.

**Exercice 16.6.4**

Écrivez une classe avec `__call__` (objet appelable) qui mémorise un compteur d'appels. Écrivez une classe `Polynome` appelable.

**Exercice 16.6.5**

Utilisez `__getattr__`, `__setattr__`, `__delattr__` pour créer un objet qui journalise chaque accès à un attribut, et une classe qui expose les clés d'un dictionnaire comme attributs.

**Exercice 16.6.6**

Écrivez `__eq__` et `__hash__` cohérents pour qu'une classe `Point` puisse être utilisée dans un ensemble et comme clé de dictionnaire. Que se passe-t-il si on définit seulement `__eq__` ?

**Exercice 16.6.7**

Implémentez `__enter__` et `__exit__` pour un objet qui ouvre et ferme une connexion fictive. *(voir ci-dessous)*

### Gestionnaire de contexte personnalisé

**Exercice 16.6.8**

Écrivez un gestionnaire de contexte `Transaction` qui valide (`commit`) à la sortie normale du bloc et annule (`rollback`) en cas d'exception, sans la supprimer. Testez les deux cas.

## 16.7 Classes de données : `dataclass`

**Exercice 16.7.1**

Écrivez une `dataclass` `Produit` (nom, prix, quantité=0) et comparez ce qu'elle génère automatiquement (`__init__`, `__repr__`, `__eq__`) avec une classe écrite à la main.

**Exercice 16.7.2**

Utilisez `field(default_factory=list)`, `frozen=True`, `order=True`, `slots=True`, `kw_only=True`. Expliquez le rôle de chaque option et montrez le piège d'une valeur par défaut mutable.

**Exercice 16.7.3**

Utilisez `__post_init__` pour valider les champs (prix positif) et pour calculer un champ dérivé (`field(init=False)`).

**Exercice 16.7.4**

Utilisez `dataclasses.asdict`, `astuple`, `replace`, `fields`. Convertissez une `dataclass` imbriquée en JSON.

**Exercice 16.7.5**

Comparez `dataclass`, `NamedTuple`, `TypedDict` et `attrs`/`pydantic` (citez-les) : mutabilité, validation, performance, cas d'usage.

## 16.8 Énumérations

**Exercice 16.8.1**

Écrivez une énumération `Couleur` (ROUGE, VERT, BLEU) avec `Enum`. Parcourez-la, accédez à un membre par nom (`Couleur["ROUGE"]`) et par valeur (`Couleur(1)`).

**Exercice 16.8.2**

Utilisez `auto()`, `IntEnum`, `StrEnum`, `Flag` : écrivez une énumération de permissions combinables (`LECTURE | ECRITURE`) et testez `in`.

**Exercice 16.8.3**

Ajoutez des méthodes et des attributs à une énumération `Planete` (masse, rayon) avec une méthode `gravite`.

**Exercice 16.8.4**

Utilisez une énumération avec `match`/`case` pour implémenter une machine à états (feu tricolore). Pourquoi une énumération est-elle préférable à des constantes entières ou des chaînes ?

## 16.9 Classes abstraites et protocoles

**Exercice 16.9.1**

Écrivez une classe abstraite `Forme` (module `abc`) avec les méthodes abstraites `aire` et `perimetre`. Que se passe-t-il quand on tente d'instancier `Forme` ou une sous-classe incomplète ?

**Exercice 16.9.2**

Définissez un `Protocol` `Dessinable` avec une méthode `dessiner`. Écrivez une fonction qui accepte tout objet qui la possède, avec annotation, et vérifiez avec `mypy`. Utilisez `@runtime_checkable` pour un test `isinstance`.

**Exercice 16.9.3**

Quelle différence entre `ABC` et `Protocol` (nominal vs structurel) ? Dans quels cas choisir l'un ou l'autre ?

**Exercice 16.9.4**

Utilisez `collections.abc` (`Sequence`, `Mapping`, `Iterable`) pour créer une classe qui n'implémente que quelques méthodes et obtient les autres gratuitement.

## 16.10 `__slots__` et gestion de la mémoire

**Exercice 16.10.1**

Comparez la mémoire d'une instance avec et sans `__slots__` pour un million d'objets. Que perd-on (`__dict__`, attributs dynamiques) ?

**Exercice 16.10.2**

Quels sont les pièges de `__slots__` avec l'héritage ? Écrivez un exemple où la sous-classe réintroduit un `__dict__`.

**Exercice 16.10.3**

Utilisez `weakref` pour référencer un objet sans empêcher sa suppression, et `sys.getrefcount`. Écrivez un cache à références faibles (`WeakValueDictionary`).

## 16.11 Descripteurs

**Exercice 16.11.1**

Écrivez un descripteur `Positif` (avec `__set_name__`, `__get__`, `__set__`) qui valide qu'un attribut est strictement positif. Utilisez-le dans deux classes.

**Exercice 16.11.2**

Expliquez comment `property`, `classmethod`, `staticmethod` et les méthodes elles-mêmes sont implémentées avec le protocole de descripteur. Quelle différence entre descripteur de données et descripteur sans données (priorité sur `__dict__`) ?

## 16.12 Métaclasses et réflexion (avancé)

**Exercice 16.12.1**

Utilisez `type(nom, bases, dict)` pour créer dynamiquement une classe. Quelle est la classe de `int`, de `type`, d'une classe que vous définissez ?

**Exercice 16.12.2**

Écrivez une métaclasse qui enregistre automatiquement toutes les sous-classes dans un registre. Comparez avec `__init_subclass__`, plus simple.

**Exercice 16.12.3**

Écrivez une métaclasse (ou un décorateur de classe) qui interdit qu'une classe définisse un attribut en majuscules sans être une constante. *(défi)*

### Introspection

**Exercice 16.12.4**

Utilisez `dir`, `vars`, `getattr`, `hasattr`, `setattr`, `type`, `isinstance`, `inspect.signature`, `inspect.getmembers` pour explorer un objet. Écrivez une fonction `decrire(obj)` qui liste ses attributs et méthodes publics.

**Exercice 16.12.5**

Écrivez un petit module de sérialisation générique qui parcourt les attributs d'un objet par réflexion et produit un dictionnaire.

## 16.13 Principes et bonnes pratiques

**Exercice 16.13.1**

Pour chacun des principes SOLID (responsabilité unique, ouvert/fermé, substitution de Liskov, ségrégation des interfaces, inversion des dépendances), écrivez un court exemple de violation et sa correction.

**Exercice 16.13.2**

« Préférez la composition à l'héritage » : refactorisez une hiérarchie à trois niveaux (`Vehicule` → `VehiculeMotorise` → `Voiture`) en utilisant la composition.

**Exercice 16.13.3**

Corrigez cette classe qui viole plusieurs bonnes pratiques :

```python
class Utilisateur:
    liste_utilisateurs = []
    def __init__(self, nom, mdp):
        self.nom = nom
        self.mdp = mdp
        self.liste_utilisateurs.append(self)
    def afficher_et_sauvegarder(self, fichier):
        print(self.nom)
        open(fichier, "w").write(self.nom + self.mdp)
```

## 16.14 Patrons de conception appliqués

### Singleton (via un module)

**Exercice 16.14.1**

Montrez qu'un module Python se comporte comme un singleton. Écrivez aussi une version avec `__new__`. Pourquoi le singleton est-il souvent un anti-patron ?

### Fabrique

**Exercice 16.14.2**

Écrivez une fabrique `creer_forme(type, **params)` qui renvoie un objet `Cercle`, `Rectangle` ou `Triangle` à partir d'un dictionnaire ou d'un nom, avec un registre extensible.

### Stratégie (avec des fonctions)

**Exercice 16.14.3**

Écrivez un calculateur de prix avec différentes stratégies de remise (aucune, pourcentage, montant fixe, fidélité) sous forme de fonctions passées en paramètre.

### Observateur

**Exercice 16.14.4**

Écrivez une classe `Sujet` avec `abonner`, `desabonner`, `notifier`, et deux observateurs. Appliquez-la à un thermomètre qui notifie des afficheurs.

**Exercice 16.14.5**

Écrivez un patron Décorateur (au sens GoF) : une classe `Cafe` décorée par `Lait` et `Sucre` qui modifient prix et description. Quelle différence avec les décorateurs Python ?

**Exercice 16.14.6**

Écrivez un patron Commande avec annulation (`undo`) pour un éditeur de texte minimal.

## 16.15 Exemple complet

**Exercice 16.15.1**

Concevez et implémentez un petit système de gestion de bibliothèque : classes `Livre`, `Membre`, `Bibliotheque`, exceptions métier (`LivreIndisponible`, `LimiteEmpruntAtteinte`), énumération pour l'état d'un livre, `dataclass` pour les données, persistance en JSON et tests `pytest`.

**Exercice 16.15.2**

Concevez un jeu de cartes : classes `Carte`, `Paquet` (itérable, mélangeable), `Joueur`, énumérations pour couleurs et valeurs, `__lt__` pour comparer les cartes, et une partie de « bataille » entre deux joueurs.

**Exercice 16.15.3**

Écrivez une simulation de distributeur automatique avec une machine à états (énumération), des produits (dataclass), des erreurs personnalisées et un journal d'événements.

---

# 17. Typage statique

---

## 17.1 Annotations de types

**Exercice 17.1.1**

Annotez ces fonctions : `def addition(a, b)`, `def saluer(nom, fois=1)`, `def trouver(liste, x)` (renvoie un indice ou `None`). Annotez également une variable de module et un attribut de classe.

**Exercice 17.1.2**

Pourquoi Python ne vérifie-t-il pas les annotations à l'exécution ? Écrivez un appel qui viole le type et montrez qu'il s'exécute malgré tout. Quels outils les vérifient ?

**Exercice 17.1.3**

Quels sont les avantages du typage statique (documentation, autocomplétion, détection d'erreurs avant exécution) ? Quels sont ses coûts ?

## 17.2 Syntaxe moderne (Python 3.9 / 3.10+)

**Exercice 17.2.1**

Réécrivez avec la syntaxe moderne : `List[int]`, `Dict[str, int]`, `Optional[str]`, `Union[int, str]`, `Tuple[int, ...]`, `Set[str]`.

**Exercice 17.2.2**

Quand utiliser `X | None` plutôt que `Optional[X]` ? Écrivez une fonction qui renvoie `int | None` et une fonction qui consomme ce résultat sans erreur de typage (vérification `is None`).

## 17.3 Types courants

**Exercice 17.3.1**

Utilisez `Any`, `Callable`, `Iterable`, `Sequence`, `Mapping`, `Literal`, `TypedDict`, `NamedTuple`, `Final`, `ClassVar`, `Self`, `Never`. Pour chacun, écrivez une fonction ou une classe annotée.

**Exercice 17.3.2**

Écrivez un `TypedDict` pour un utilisateur (`nom: str`, `age: int`, `email: NotRequired[str]`) et une fonction qui l'utilise. Comparez à une `dataclass`.

**Exercice 17.3.3**

Annotez une fonction qui reçoit une fonction de rappel `Callable[[int, str], bool]`. Annotez une fonction qui renvoie un générateur (`Iterator[int]`, `Generator[int, None, None]`).

**Exercice 17.3.4**

Utilisez `Literal["lecture", "ecriture"]` pour restreindre les valeurs d'un paramètre. Quelle erreur `mypy` détecte-t-il pour `ouvrir("autre")` ?

## 17.4 Génériques et paramètres de type *(Python 3.12+)*

**Exercice 17.4.1**

Écrivez avec la nouvelle syntaxe PEP 695 une fonction générique `premier[T](elements: list[T]) -> T` et une classe générique `Pile[T]`. Comparez avec l'ancienne syntaxe `TypeVar`. *(Python 3.12)*

**Exercice 17.4.2**

Utilisez l'instruction `type` pour déclarer un alias de type (`type Point = tuple[float, float]`) puis un alias générique. *(Python 3.12)*

**Exercice 17.4.3**

Écrivez une fonction générique avec borne : `def plus_grand[T: (int, float)](a: T, b: T) -> T`. Quelle différence entre une borne (`T: Comparable`) et des contraintes (`T: (int, str)`) ? *(Python 3.12)*

**Exercice 17.4.4**

Écrivez un `Protocol` générique `Conteneur[T]` et une classe qui le satisfait. Vérifiez avec `mypy`.

## 17.5 Évaluation différée des annotations *(Python 3.14)*

**Exercice 17.5.1**

Écrivez une classe qui se référence elle-même dans ses annotations (par exemple un `Noeud` de liste chaînée avec `suivant: Noeud | None`). Essayez sous Python 3.14 sans guillemets ni `from __future__ import annotations`. *(Python 3.14)*

**Exercice 17.5.2**

Utilisez `annotationlib.get_annotations` pour inspecter les annotations d'une fonction. Quelle différence avec `__annotations__` ? *(Python 3.14)*

**Exercice 17.5.3**

Quel problème de références anticipées (guillemets, `from __future__ import annotations`) l'évaluation différée résout-elle ? Quelle précaution prendre pour du code qui doit aussi fonctionner sur des versions plus anciennes ?

## 17.6 Vérifier les types

**Exercice 17.6.1**

Installez `mypy` et vérifiez un script volontairement mal typé : notez trois erreurs détectées et corrigez-les.

**Exercice 17.6.2**

Configurez `mypy` en mode strict dans `pyproject.toml`. Quelles vérifications supplémentaires apparaissent (fonctions non annotées, `Any` implicite) ?

**Exercice 17.6.3**

Comparez `mypy`, `pyright`, `pyrefly` et `ty` (outils de vérification) : vitesse, intégration éditeur, niveau de rigueur. Annotez un petit projet de votre choix et vérifiez-le avec deux de ces outils.

**Exercice 17.6.4**

Utilisez `typing.cast`, `typing.TYPE_CHECKING` et `# type: ignore` : dans quels cas sont-ils légitimes ? Quels sont les risques d'un abus ?

---

# 18. Programmation asynchrone et concurrence

*(Section ajoutée.)*

---

## 18.1 Choisir le bon modèle

**Exercice 18.1.1**

Pour chaque tâche, choisissez le modèle le plus adapté (`asyncio`, threads, processus) et justifiez : télécharger 1000 pages web, redimensionner 500 images, calculer des nombres premiers sur de grandes plages, interroger une base de données bloquante via une bibliothèque synchrone, servir 10 000 connexions WebSocket.

**Exercice 18.1.2**

Distinguez concurrence et parallélisme. Un programme `asyncio` est-il parallèle ? Un programme multi-threads sous le GIL l'est-il pour du calcul ?

**Exercice 18.1.3**

Complétez le tableau comparatif : modèle, mémoire partagée, coût de création, complexité de synchronisation, adapté aux E/S ou au CPU.

## 18.2 `asyncio`

**Exercice 18.2.1**

Écrivez une coroutine `telecharger(nom, delai)` qui simule un téléchargement avec `asyncio.sleep`, puis lancez trois téléchargements avec `asyncio.gather`. Mesurez le temps total et comparez avec une exécution séquentielle.

**Exercice 18.2.2**

Quelle différence entre `async def` (coroutine), `await`, une tâche (`asyncio.create_task`) et une `Future` ? Que se passe-t-il si l'on oublie `await` devant un appel de coroutine ?

**Exercice 18.2.3**

Écrivez un programme qui utilise `asyncio.wait_for` pour imposer un délai maximal (timeout) à une coroutine et gère `TimeoutError`.

**Exercice 18.2.4**

Écrivez un producteur et un consommateur communiquant par une `asyncio.Queue`. Terminez proprement avec un signal de fin.

**Exercice 18.2.5**

Utilisez `asyncio.Semaphore` pour limiter à 3 le nombre de téléchargements simultanés parmi 10.

**Exercice 18.2.6**

Pourquoi un appel bloquant (`time.sleep`, lecture de fichier volumineux) dans une coroutine bloque-t-il toute la boucle d'événements ? Écrivez un exemple, puis corrigez-le avec `asyncio.to_thread`.

### `TaskGroup` *(3.11+)*

**Exercice 18.2.7**

Réécrivez l'exercice 18.2.1 avec `asyncio.TaskGroup`. Que se passe-t-il si l'une des tâches lève une exception ? Comparez avec `gather` (paramètre `return_exceptions`). *(Python 3.11)*

**Exercice 18.2.8**

Utilisez `asyncio.timeout()` dans un `async with` et `except*` pour gérer plusieurs erreurs simultanées issues d'un `TaskGroup`. *(Python 3.11)*

**Exercice 18.2.9**

Écrivez un petit explorateur de pages web concurrent avec `asyncio` (ou avec une bibliothèque comme `aiohttp` ou `httpx`) qui télécharge une liste d'URL, mesure le temps de chaque réponse et affiche un résumé. *(défi)*

## 18.3 Threads et processus

**Exercice 18.3.1**

Utilisez `threading.Thread` pour lancer trois tâches qui attendent `time.sleep(1)`. Mesurez le temps total. Utilisez `join`.

**Exercice 18.3.2**

Écrivez un compteur partagé incrémenté par plusieurs threads sans verrou, et observez le résultat. Corrigez avec `threading.Lock`. Qu'est-ce qu'une condition de concurrence ?

**Exercice 18.3.3**

Utilisez `ThreadPoolExecutor` et `ProcessPoolExecutor` avec `map` et `submit`. Récupérez les résultats avec `as_completed`.

**Exercice 18.3.4**

Comparez les temps d'exécution d'un calcul intensif (somme de carrés jusqu'à 10⁷, nombres premiers) en séquentiel, avec threads et avec processus. Que constatez-vous sur une version avec GIL ?

**Exercice 18.3.5**

Pourquoi faut-il protéger le code de lancement des processus par `if __name__ == "__main__":` avec `multiprocessing` ? Que se passe-t-il sous Windows et macOS (démarrage par *spawn*) ?

**Exercice 18.3.6**

Utilisez `multiprocessing.Queue`, `Pipe`, `Value`/`Array` ou `shared_memory` pour échanger des données entre processus. Quels sont les coûts de sérialisation ?

**Exercice 18.3.7**

Écrivez un petit programme qui traite en parallèle un grand fichier de nombres (découpage en morceaux, traitement par un pool de processus, agrégation des résultats). *(défi)*

**Exercice 18.3.8**

Utilisez `queue.Queue` et des threads pour un schéma producteur-consommateur. Quelle différence entre `Queue` et `deque` en environnement multi-threads ?

## 18.4 Le GIL et Python sans GIL

**Exercice 18.4.1**

Expliquez ce qu'est le GIL et pourquoi il existe (gestion de la mémoire avec comptage de références). Pourquoi limite-t-il le parallélisme des threads pour du calcul ?

**Exercice 18.4.2**

Recherchez comment installer et lancer une version *free-threaded* de Python (`python3.13t` ou `python3.14t`). Vérifiez l'état du GIL avec `sys._is_gil_enabled()` et mesurez le gain sur un calcul parallèle avec threads.

**Exercice 18.4.3**

Quelles précautions prendre pour les bibliothèques d'extension C quand le GIL est désactivé ? Pourquoi un programme correct avec GIL peut-il révéler des courses de données sans GIL ?

**Exercice 18.4.4**

Explorez `concurrent.interpreters` (Python 3.14) : lancez du code dans un sous-interpréteur isolé. Comparez avec `multiprocessing` (mémoire, démarrage, échange de données). *(Python 3.14 ; défi)*

---

# 19. Tests et qualité du code

*(Section ajoutée.)*

---

## 19.1 Tests avec `pytest`

**Exercice 19.1.1**

Écrivez une fonction `est_palindrome(texte)` puis un fichier de tests `pytest` avec au moins cinq cas (palindrome simple, avec majuscules, avec espaces, vide, non palindrome).

**Exercice 19.1.2**

Utilisez `@pytest.mark.parametrize` pour tester `additionner` ou `convertir_celsius` avec plusieurs jeux de valeurs. Comment obtient-on des noms de test lisibles (`ids`) ?

**Exercice 19.1.3**

Testez une fonction qui doit lever une exception avec `pytest.raises`, y compris la vérification du message (`match=`).

**Exercice 19.1.4**

Écrivez une fixture (`@pytest.fixture`) qui prépare une liste de données ou un fichier temporaire (`tmp_path`). Partagez-la dans `conftest.py`. Quelle est la portée (`scope`) d'une fixture ?

**Exercice 19.1.5**

Utilisez `monkeypatch` et `unittest.mock` (`patch`, `Mock`, `MagicMock`) pour tester une fonction qui appelle un service externe sans faire de vraie requête. Vérifiez les appels (`assert_called_once_with`).

**Exercice 19.1.6**

Écrivez les tests d'une classe `CompteBancaire` : dépôt, retrait, solde insuffisant, valeurs négatives. Appliquez la méthode « arranger, agir, vérifier » (*Arrange, Act, Assert*).

**Exercice 19.1.7**

Utilisez `pytest.mark.skip`, `skipif` et `xfail`. Utilisez `pytest -k`, `-x`, `--lf`, `-v` et `-q`. Notez l'effet de chaque option.

**Exercice 19.1.8**

Appliquez le développement piloté par les tests (TDD) pour écrire une fonction `fizzbuzz(n)` : écrivez d'abord les tests (qui échouent), puis le code minimal, puis refactorisez.

**Exercice 19.1.9**

Écrivez les mêmes tests avec `unittest` (`TestCase`, `setUp`, `assertEqual`, `assertRaises`). Comparez avec `pytest` en termes de concision et de lisibilité. Ajoutez des tests `doctest` dans une docstring.

**Exercice 19.1.10**

Utilisez `hypothesis` pour écrire un test basé sur des propriétés : par exemple, `inverser(inverser(x)) == x` pour toute liste. Quel est l'avantage face aux tests par exemples ? *(défi)*

## 19.2 Qualité du code

**Exercice 19.2.1**

Installez `ruff`. Lancez `ruff check` et `ruff format` sur un fichier de votre choix. Corrigez les problèmes signalés (importations inutilisées, lignes trop longues, noms ambigus).

**Exercice 19.2.2**

Configurez `ruff` dans `pyproject.toml` (longueur de ligne, jeux de règles activés, règles ignorées). Quelle est la différence entre un linter et un formateur ?

**Exercice 19.2.3**

Mesurez la couverture de tests avec `pytest-cov` : `pytest --cov=monpaquet --cov-report=term-missing`. Identifiez les lignes non couvertes et ajoutez les tests manquants. Une couverture de 100 % garantit-elle l'absence de bugs ?

**Exercice 19.2.4**

Configurez `pre-commit` avec `ruff`, la vérification des fins de ligne et un test rapide. Faites un `git commit` qui échoue à cause d'une erreur de style, corrigez-la et recommencez.

**Exercice 19.2.5**

Vérifiez les types d'un projet avec `mypy` ou `pyright` et intégrez la vérification dans un pipeline d'intégration continue (GitHub Actions, GitLab CI) : lint, tests, couverture, types.

**Exercice 19.2.6**

Utilisez `bandit` ou `pip-audit` pour détecter des problèmes de sécurité (mots de passe en dur, `eval`, dépendances vulnérables). Corrigez un problème trouvé.

## 19.3 Déboguer

**Exercice 19.3.1**

Placez un `breakpoint()` dans une fonction défectueuse et utilisez `pdb` : `n`, `s`, `c`, `p`, `pp`, `l`, `w`, `u`, `d`, `b`, `q`. Trouvez la cause d'un bug de boucle (erreur d'un cran).

**Exercice 19.3.2**

Utilisez `python -m pdb script.py` pour un débogage post-mortem après une exception (`import pdb; pdb.post_mortem()`). Quand est-ce utile ?

**Exercice 19.3.3**

Utilisez le débogueur graphique de votre éditeur (points d'arrêt conditionnels, surveillance de variables, pile d'appels) sur un programme qui calcule des statistiques.

**Exercice 19.3.4**

Comparez trois techniques de débogage : `print`, `logging` et débogueur. Pour chaque type de bug suivant, choisissez la meilleure : valeur inattendue dans une boucle, exception rare en production, condition de concurrence.

**Exercice 19.3.5**

Utilisez `cProfile`, `timeit` et `tracemalloc` pour trouver la fonction la plus lente et la plus gourmande en mémoire d'un petit programme. Optimisez-la et mesurez le gain.

**Exercice 19.3.6**

Techniques de réduction de bug : isolez un bug à partir d'un programme de 50 lignes jusqu'à un exemple minimal de 5 lignes, puis écrivez le test qui le reproduit avant de le corriger.

---

# 20. Aller plus loin

---

## 20.1 Parcours d'apprentissage suggéré

**Exercice 20.1.1**

Établissez votre plan d'apprentissage personnel en six étapes, en reprenant le parcours suggéré : pour chaque étape, indiquez les sections du cours à maîtriser, un mini-projet et un critère de réussite.

**Exercice 20.1.2**

Choisissez une spécialisation (web, données, IA, automatisation) et listez trois bibliothèques à apprendre, une ressource pour chacune et un projet concret de deux semaines.

**Exercice 20.1.3**

Mini-projets de synthèse : réalisez l'un des trois projets suivants en utilisant au moins six chapitres du cours.

1. Un gestionnaire de tâches en ligne de commande (`argparse`, JSON, classes, tests).
2. Un analyseur de journaux (`re`, générateurs, `collections.Counter`, CSV).
3. Un petit robot d'indexation web (`asyncio`, `httpx` ou `urllib`, `sqlite3`, journalisation).

## 20.2 Résumé des nouveautés récentes de Python

**Exercice 20.2.1**

Pour chaque version de 3.8 à 3.14, écrivez un exemple de code (3 à 6 lignes) qui illustre l'une de ses nouveautés (`:=`, `|` sur les dict, `match`, `except*`, `def f[T]()`, nouveau REPL, t-strings).

**Exercice 20.2.2**

Modernisez ce code écrit dans un style ancien en utilisant les fonctionnalités récentes :

```python
from typing import List, Dict, Optional, Union

def analyser(donnees: Dict[str, Union[int, str]], filtre: Optional[List[str]] = None) -> List[str]:
    resultat = []
    for cle in donnees.keys():
        if filtre is None or cle in filtre:
            resultat.append("%s=%s" % (cle, donnees[cle]))
    return resultat
```

**Exercice 20.2.3**

Consultez la page « Quoi de neuf dans Python 3.15 » sur docs.python.org. Choisissez trois nouveautés, résumez-les et écrivez un exemple pour chacune.

**Exercice 20.2.4**

Quelles fonctionnalités récentes améliorent les performances (interpréteur plus rapide, JIT expérimental, *free-threading*) ? Mesurez le même benchmark sur deux versions différentes de Python avec `uv`.

## 20.3 Ressources

**Exercice 20.3.1**

Parcourez le tutoriel officiel et choisissez un chapitre que le cours n'aborde pas en détail ; résumez-le en une demi-page avec un exemple de code.

**Exercice 20.3.2**

Lisez la PEP 8 et la PEP 257 (docstrings). Choisissez une autre PEP qui vous intéresse (par exemple PEP 484, 572, 634, 695, 750) : résumez en quelques lignes le problème posé et la solution proposée.

**Exercice 20.3.3**

Inscrivez-vous (ou simplement parcourez) le forum officiel `discuss.python.org`, et parcourez PyPI pour trouver un paquet utile et bien maintenu. Notez les critères que vous utilisez pour juger la qualité d'un paquet (dernière version, documentation, licence, activité, tests).

**Exercice 20.3.4** *(défi)*

Projet final : choisissez un petit projet open source écrit en Python, installez-le dans un environnement virtuel, lisez son code, exécutez ses tests, puis corrigez une petite anomalie ou améliorez la documentation. Rédigez un compte rendu.

---

<div align="center">

*Bon courage et bon code !*

</div>
