<div align="center">

# 🐍 Python — Guide complet

**Du premier `print()` à la programmation orientée objet moderne**

*Version mise à jour pour Python 3.14 / 3.15 (octobre 2026)*

</div>

---

## 📚 Ressources et outils

| Ressource | Description |
| --- | --- |
| 📖 **Glossaire** | [Glossaire Python (docstring.fr)](https://docstring.fr/glossaire) |
| 📘 **Documentation officielle** | [docs.python.org/fr](https://docs.python.org/fr/3/) |
| 🧠 **Carte mentale** | Utile pour visualiser les concepts et leurs liens |
| 🗒️ **Aide-mémoire** | Référence rapide des principaux éléments du langage |
| 💻 **Éditeurs en ligne** | [Replit](https://replit.com), [Google Colab](https://colab.research.google.com), [python.org/shell](https://www.python.org/shell/) |

### Modules associés

- [Quelques modules](/language/modules/python)
- [Django](/language/frameworks/django)
- [bs4 (Beautiful Soup)](/language/modules/bs4)

---

## 🗂️ Sommaire

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

---

# 1. Introduction

## 1.1 Qu'est-ce que Python ?

Python est un **langage de programmation de haut niveau, polyvalent**, réputé pour sa lisibilité, sa simplicité et sa grande étendue d'applications.

| Caractéristique | Signification |
| --- | --- |
| **Haut niveau** | Conçu pour être facile à lire et à écrire par des humains |
| **Polyvalent** | Web, automatisation, analyse de données, IA, scripts système, etc. |
| **Interprété** | Pas d'étape de compilation manuelle ; le code est exécuté par l'interpréteur |
| **Typage dynamique** | Le type est associé à la valeur, pas à la variable |
| **Multi-paradigme** | Impératif, orienté objet, fonctionnel |

### Pourquoi les débutants l'apprécient

- Syntaxe simple, proche de l'anglais
- Pas de point-virgule, d'accolades ni de déclaration de types obligatoires
- Communauté vaste et accueillante

### Pourquoi les professionnels l'utilisent

- Écosystème immense (NumPy, Django, FastAPI, PyTorch, Pandas…)
- Excellent pour le prototypage comme pour la production
- Intégration facile avec d'autres langages et outils

## 1.2 Domaines d'utilisation

| # | Domaine | Outils courants |
| --- | --- | --- |
| 1 | **Développement web** | Django, Flask, FastAPI |
| 2 | **Science des données et IA** | NumPy, Pandas, Polars, Matplotlib, Scikit-learn, PyTorch, TensorFlow |
| 3 | **Automatisation et scripts** | Scripts de fichiers, tâches planifiées (cron), bots |
| 4 | **Jeux vidéo** | Pygame, Godot (GDScript, proche de Python) |
| 5 | **Applications de bureau** | Tkinter (intégré), PyQt / PySide, Kivy |
| 6 | **Systèmes embarqués / IoT** | MicroPython, CircuitPython (ESP32, Raspberry Pi Pico) |
| 7 | **Cybersécurité** | Outils de reconnaissance, audits, automatisation de tests d'intrusion |
| 8 | **Calcul scientifique** | SciPy, SymPy, Jupyter |
| 9 | **DevOps et administration** | Scripts de déploiement, outils CLI, cloud (AWS, Azure, GCP) |
| 10 | **Enseignement** | Syntaxe claire, forte demande sur le marché |

---

## 1.3 Histoire de Python

### Création

- **Guido van Rossum**, programmeur néerlandais, commence à travailler sur Python à la **fin des années 1980** au **CWI** (Centrum Wiskunde & Informatica, Pays-Bas).
- Première publication publique : **février 1991** (version **0.9.0**).
- Le nom vient du groupe d'humour britannique **Monty Python**, et non du serpent.

### Objectifs de conception

- Privilégier la **lisibilité du code**
- Exprimer des idées avec **moins de lignes**
- Combler l'écart entre **C** et les **scripts shell**
- Offrir une alternative à **ABC**, langage d'enseignement du CWI

### Les grandes versions

| Version | Date | Points marquants |
| --- | --- | --- |
| **1.0** | Janvier 1994 | Fonctions, exceptions, types de base (`str`, `list`, `dict`), `lambda`, `map`, `filter` |
| **2.0** | Octobre 2000 | Compréhensions de listes, ramasse-miettes avec détection de cycles, début du support Unicode |
| **3.0** | Décembre 2008 | Rupture de compatibilité avec Python 2 : `print()` devient une fonction, Unicode natif, division « vraie » (`5/2 == 2.5`), bibliothèque standard nettoyée |
| **3.10** | Octobre 2021 | Filtrage par motifs (`match`/`case`), unions `X \| Y`, meilleurs messages d'erreur |
| **3.11** | Octobre 2022 | Interpréteur nettement plus rapide (10 à 60 %), groupes d'exceptions (`except*`), module `tomllib` |
| **3.12** | Octobre 2023 | Syntaxe de paramètres de type (PEP 695), instruction `type`, f-strings plus souples |
| **3.13** | Octobre 2024 | Nouveau REPL interactif, version expérimentale **sans GIL** (*free-threaded*), compilateur JIT expérimental |
| **3.14** | Octobre 2025 | **Template strings** (t-strings), évaluation différée des annotations, *free-threading* officiellement supporté, sous-interpréteurs (`concurrent.interpreters`) |
| **3.15** | Octobre 2026 | Dernière version majeure (voir [python.org](https://www.python.org/downloads/) pour l'état exact de la publication) |

> 📌 **Fin de vie de Python 2** : le 1ᵉʳ janvier 2020.
> 📌 **Cycle de publication** : une version majeure chaque année en octobre (PEP 602), avec environ **5 ans de support** (2 ans de correctifs, puis 3 ans de correctifs de sécurité). Python 3.9 a atteint sa fin de vie en octobre 2025 ; 3.10 l'atteint en octobre 2026.

### Gouvernance et communauté

- Guido van Rossum fut le **BDFL** (*Benevolent Dictator For Life*) jusqu'à sa démission en **2018**.
- Python est désormais gouverné par un **Conseil de pilotage** (*Steering Council*) élu.
- La **Python Software Foundation (PSF)**, fondée en **2001**, est l'organisation à but non lucratif qui soutient le langage, la communauté et les conférences (PyCon).
- Les évolutions passent par les **PEP** (*Python Enhancement Proposals*).
- Python figure régulièrement dans le **top 3** des langages les plus utilisés, et il est employé par Google, Netflix, Dropbox, Instagram, Reddit, etc.

### Chronologie

| Année | Événement |
| --- | --- |
| 1989 | Guido van Rossum commence à développer Python |
| 1991 | Python 0.9.0 |
| 1994 | Python 1.0 |
| 2000 | Python 2.0 |
| 2001 | Création de la PSF |
| 2008 | Python 3.0 |
| 2018 | Guido quitte son rôle de BDFL |
| 2020 | Fin de vie de Python 2 |
| 2024 | Python 3.13 : premiers builds sans GIL |
| 2025 | Python 3.14 : *free-threading* officiellement supporté |

---

## 1.4 Caractéristiques de Python

### 1. Langage interprété

Le code n'est pas compilé en amont par l'utilisateur : l'interpréteur le traduit en *bytecode* puis l'exécute. Le débogage est facile, au prix de performances inférieures aux langages compilés.

```python
print("Bonjour le monde !")  # Exécuté directement par l'interpréteur
```

### 2. Syntaxe lisible

Python utilise l'**indentation** pour délimiter les blocs (pas d'accolades `{}`).

```python
if age >= 18:
    print("Vous pouvez voter.")
else:
    print("Vous êtes encore trop jeune.")
```

### 3. Typage dynamique (et typage graduel)

Il n'est pas nécessaire de déclarer les types ; ils sont déterminés à l'exécution. Depuis Python 3.5, on peut **annoter** les types pour les outils d'analyse (voir [section 17](#17-typage-statique)).

```python
x = 10        # x est un entier
x = "Salut"   # x est maintenant une chaîne
```

### 4. Portable et multiplateforme

Un même script s'exécute sur **Windows**, **macOS**, **Linux** et d'autres systèmes, presque sans modification.

### 5. Bibliothèque standard riche (« piles incluses »)

| Besoin | Modules |
| --- | --- |
| Système et fichiers | `os`, `pathlib`, `shutil`, `io` |
| Web et réseau | `urllib`, `http`, `socket` |
| Structures de données | `collections`, `heapq`, `bisect` |
| Texte | `re`, `string`, `textwrap` |
| Formats de données | `json`, `csv`, `tomllib`, `sqlite3` |
| Dates et heures | `datetime`, `zoneinfo` |
| Programmation moderne | `dataclasses`, `enum`, `typing`, `asyncio`, `functools`, `itertools` |
| Tests | `unittest`, `doctest` |

```python
import math
print(math.sqrt(25))  # 5.0
```

### 6. Libre et gratuit

Code source ouvert (licence PSF), gratuit y compris pour un usage commercial.

### 7. Multi-paradigme

Programmation **orientée objet**, **fonctionnelle** (`lambda`, `map()`, `filter()`) et **procédurale**.

```python
class Chien:
    def __init__(self, nom):
        self.nom = nom

    def aboyer(self):
        print(f"{self.nom} fait ouaf !")

Chien("Rex").aboyer()
```

### 8. Extensible et intégrable

- Appel de code **C/C++/Rust** pour les parties critiques (extensions natives, `ctypes`, Cython, PyO3).
- Python peut aussi être **embarqué** dans d'autres applications comme langage de script.

### 9. Gestion automatique de la mémoire

Le développeur n'a pas à gérer manuellement la mémoire : Python utilise le **comptage de références** et un **ramasse-miettes** pour les cycles.

### 10. Mode interactif (REPL)

```bash
$ python3
>>> 2 + 3
5
```

Depuis Python 3.13, le REPL est amélioré : coloration syntaxique, édition multiligne, historique, collage de blocs de code.

### 11. Communauté active

Stack Overflow, Reddit, Discord, forums officiels (discuss.python.org), et une documentation abondante.

### 12. Écosystème de bibliothèques

| Domaine | Bibliothèques / frameworks |
| --- | --- |
| Web | Django, Flask, FastAPI |
| Données | NumPy, Pandas, Polars, Matplotlib, Seaborn |
| IA / ML | Scikit-learn, TensorFlow, PyTorch |
| Interfaces graphiques | Tkinter, PyQt, Kivy |
| Jeux | Pygame |
| Automatisation | Selenium, Playwright, PyAutoGUI |
| Réseau | Requests, httpx, Paramiko |

---

## 1.5 Installer Python

### Télécharger

- Site officiel : **<https://www.python.org/downloads>**
- Choisissez toujours la **dernière version stable de Python 3** (3.14 ou plus récente). **N'utilisez plus Python 2** (abandonné depuis le 1ᵉʳ janvier 2020).

### Windows

1. Téléchargez l'installateur depuis [python.org](https://www.python.org/downloads/windows/) (ou installez le *Python install manager* proposé par python.org).
2. **Important** : cochez **« Add python.exe to PATH »** avant de cliquer sur *Install Now*.
3. Suivez les étapes.

```cmd
python --version
py --version
```

Alternatives : `winget install Python.Python.3.14` ou `choco install python`.

### macOS

- Installateur `.pkg` officiel, ou avec **Homebrew** (recommandé) :

```bash
brew install python
python3 --version
```

### Linux

La plupart des distributions incluent déjà Python. Pour l'installer ou le mettre à jour :

```bash
# Debian / Ubuntu
sudo apt update && sudo apt install python3 python3-pip python3-venv

# Fedora
sudo dnf install python3

# Arch
sudo pacman -S python
```

Pour une version plus récente sur Ubuntu/Debian, utilisez le PPA **deadsnakes** ou, mieux, **uv** (voir ci-dessous) :

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update && sudo apt install python3.14
```

### Gestionnaires multiplateformes

| Outil | Usage |
| --- | --- |
| **uv** | Installe Python *et* gère paquets, environnements et projets (très rapide) |
| **pyenv** | Gère plusieurs versions de Python côte à côte |
| **Anaconda / Miniconda** | Distribution orientée science des données |

```bash
# Avec uv
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.14
```

### Variables d'environnement (Windows, si `python` n'est pas reconnu)

1. *Paramètres système → Variables d'environnement*.
2. Ajoutez à `PATH` le dossier d'installation **et** son sous-dossier `Scripts` :

```text
C:\Users\<VotreNom>\AppData\Local\Programs\Python\Python3xx\
C:\Users\<VotreNom>\AppData\Local\Programs\Python\Python3xx\Scripts\
```

### Vérifier `pip`

`pip` est fourni avec Python. En cas de besoin :

```bash
pip --version
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

### Vérifier l'installation

```bash
python3 --version
python3
>>> print("Bonjour")
Bonjour
```

---

## 1.6 Choisir un éditeur ou un IDE

Un **éditeur de code** est léger (coloration syntaxique, complétion simple). Un **IDE** (environnement de développement intégré) regroupe éditeur, débogueur, gestion de projet, terminal et contrôle de version.

| Outil | Type | Public | Points forts |
| --- | --- | --- | --- |
| **VS Code** | Éditeur | Tous niveaux | Gratuit, extensible, excellent support Python |
| **PyCharm** | IDE | Intermédiaire à pro | Intégration Python très poussée (éditions Community et Pro) |
| **Thonny** | IDE | Débutants | Simple, débogueur visuel, fourni avec Python |
| **IDLE** | IDE | Débutants | Livré avec Python, aucune installation |
| **Sublime Text** | Éditeur | Intermédiaire | Rapidité (licence payante, évaluation gratuite) |
| **Jupyter / JupyterLab** | Notebook | Science des données | Interactif, visualisations |
| **Zed, Neovim** | Éditeurs | Avancé | Rapides, personnalisables |

> ⚠️ **Atom** a été archivé par GitHub en 2022 : ne l'utilisez plus.
> Notepad++ convient uniquement aux modifications rapides sous Windows.

### VS Code : extensions recommandées

- **Python** (Microsoft) et **Pylance** (analyse de code)
- **Ruff** (formatage et lint ultra-rapides)
- **Jupyter** (notebooks)

*Installation* : `Ctrl+Shift+X` → rechercher « Python » → *Installer*.

### Quel outil choisir ?

| Besoin | Recommandation |
| --- | --- |
| Débuter | Thonny ou IDLE |
| Développement général | VS Code ou PyCharm Community |
| Web | PyCharm Pro ou VS Code |
| Science des données | JupyterLab ou VS Code + Jupyter |
| Modifications rapides | Sublime Text ou VS Code |

---

## 1.7 Exécuter son premier programme

Python peut s'exécuter de deux façons : en **mode interactif (REPL)** ou en **mode script** (fichiers `.py`).

### Mode interactif (REPL)

```bash
python        # ou python3
>>> print("Bonjour le monde !")
Bonjour le monde !
>>> 2 + 3
5
```

Quitter : `exit()`, ou `Ctrl+Z` puis Entrée (Windows), `Ctrl+D` (macOS/Linux).

### Mode script

```python
# bonjour.py
print("Bonjour, Python !")
```

```bash
python bonjour.py      # ou python3 bonjour.py
```

### Comparaison des deux modes

| Critère | Mode interactif | Mode script |
| --- | --- | --- |
| Exécution | Ligne par ligne | Fichier entier |
| Idéal pour | Tests, apprentissage, exploration | Programmes complets, production |
| Sauvegarde du code | Non | Oui (fichiers `.py`) |
| Retour | Immédiat | Après exécution |
| Modification | Difficile | Facile dans un éditeur |

**Quand utiliser quoi ?** Interactif pour tester une expression ou explorer une fonction (`type()`, `help()`, `dir()`) ; script pour tout programme à conserver ou réutiliser.

### Exécuter depuis un éditeur

- **VS Code** : sélectionnez l'interpréteur (`Ctrl+Shift+P` → *Python: Select Interpreter*), puis cliquez sur ▶ *Run Python File*.
- **IDLE** : *File → New File*, enregistrez, puis **F5** (*Run Module*).

### Autres façons de lancer Python

```bash
python -c "print('Une ligne')"     # Exécuter une commande
python -m http.server              # Exécuter un module comme script
python -i script.py                # Rester en mode interactif après le script
```

### Le *shebang* (Unix)

```python
#!/usr/bin/env python3
print("Bonjour depuis un script exécutable")
```

```bash
chmod +x script.py
./script.py
```

### Erreurs courantes

| Problème | Solution |
| --- | --- |
| *Fichier introuvable* | Vérifiez le dossier courant avec `cd chemin/vers/le/fichier` |
| *Commande non reconnue* | Ajoutez Python au `PATH` (voir installation) |

---

## 1.8 L'interpréteur Python

L'**interpréteur** lit votre code source, le **compile en bytecode**, puis le fait exécuter par la **machine virtuelle Python (PVM)**.

```text
Code source (.py)
      ↓
Compilateur intégré
      ↓
Bytecode (.pyc, dans __pycache__)
      ↓
Machine virtuelle Python (PVM)
      ↓
Résultat
```

### Bytecode

- Jeu d'instructions bas niveau, **indépendant de la plateforme**.
- Mis en cache dans des fichiers `.pyc` (dossier `__pycache__`) pour accélérer les exécutions suivantes.
- Vous pouvez l'examiner avec le module `dis`.

### Machine virtuelle (PVM)

Moteur d'exécution : exécute le bytecode, gère la mémoire, le suivi des variables, les erreurs et le typage dynamique.

### Les implémentations de Python

| Implémentation | Description |
| --- | --- |
| **CPython** | Implémentation de référence, écrite en C (la plus utilisée) |
| **PyPy** | Compilation JIT, souvent beaucoup plus rapide |
| **Jython** | Python sur la JVM (Java) |
| **IronPython** | Python sur .NET |
| **MicroPython** | Pour microcontrôleurs |
| **GraalPy** | Python sur GraalVM |

> Depuis Python 3.13, CPython propose aussi, de façon **expérimentale**, un compilateur **JIT** et une version **sans GIL**.

### Compilé ou interprété ?

Python est **les deux** : compilé en bytecode, puis interprété par la PVM.

| Critère | Langages compilés | Python |
| --- | --- | --- |
| Compilation | Avant l'exécution | À l'exécution (bytecode) |
| Vitesse | Généralement plus rapide | Généralement plus lent |
| Débogage | Recompilation nécessaire | Interactif et souple |
| Portabilité | Binaires spécifiques | Bytecode portable |

### Peut-on exécuter Python sans interpréteur ?

Non, mais vous pouvez utiliser des **interpréteurs en ligne** (Replit, Colab) ou **empaqueter** une application en exécutable avec **PyInstaller**, **cx_Freeze** ou **Nuitka**.

### Options utiles de l'interpréteur

| Option | Effet |
| --- | --- |
| `-i` | Mode interactif après l'exécution du script |
| `-m` | Exécute un module comme script |
| `-c` | Exécute une commande |
| `-O` | Optimise le bytecode (supprime les `assert`) |
| `-B` | N'écrit pas de fichiers `.pyc` |
| `-X dev` | Active le mode développement (vérifications supplémentaires) |

---

## 1.9 « Hello, World ! »

```python
print("Bonjour le monde !")
```

- `print` est une **fonction intégrée** qui affiche du texte.
- Le texte est entre guillemets simples (`'...'`) ou doubles (`"..."`).
- Depuis Python 3, `print` est une **fonction** (`print("x")`, et non `print "x"`).

### La fonction `print()` en détail

```python
print("A", "B", "C")                 # A B C
print("A", "B", sep="-")             # A-B
print("Chargement", end="...")       # pas de retour à la ligne
print("Erreur", file=sys.stderr)     # sortie d'erreur (après import sys)
print("Direct", flush=True)          # vide le tampon immédiatement
```

| Paramètre | Rôle | Valeur par défaut |
| --- | --- | --- |
| `sep` | Séparateur entre les valeurs | `" "` |
| `end` | Fin de l'affichage | `"\n"` |
| `file` | Destination | `sys.stdout` |
| `flush` | Vider le tampon | `False` |

### Commentaires

```python
# Commentaire sur une ligne
x = 5  # Commentaire en fin de ligne

"""
Bloc de texte multiligne souvent utilisé comme commentaire.
(En réalité : une chaîne littérale, ou une docstring à un endroit précis.)
"""
```

**Bonnes pratiques** : expliquez le *pourquoi*, pas le *quoi* ; gardez les commentaires à jour ; évitez l'évidence (`x = 1  # x vaut 1`).

### Extensions de fichiers Python

| Extension | Signification |
| --- | --- |
| `.py` | Script ou module Python |
| `.pyc` | Bytecode compilé (dans `__pycache__`) |
| `.pyi` | Fichier de *stubs* de typage |
| `.pyw` | Script Windows sans console |
| `.pyd` | Module d'extension compilé (Windows) |
| `.so` | Extension compilée (Linux/macOS) |
| `.ipynb` | Notebook Jupyter |
| `.toml` | Configuration (`pyproject.toml`) |

### Comment le code est exécuté

1. **Analyse lexicale et syntaxique** du fichier source.
2. **Compilation** en bytecode (`.pyc`).
3. **Exécution** par la PVM, instruction par instruction.

### PEP et documentation

Une **PEP** (*Python Enhancement Proposal*) est un document qui propose une évolution du langage ou décrit des conventions. Quelques PEP essentielles :

| PEP | Sujet |
| --- | --- |
| **PEP 8** | Guide de style du code Python |
| **PEP 20** | *Le Zen de Python* (`import this`) |
| **PEP 257** | Conventions pour les docstrings |
| **PEP 484** | Annotations de types |
| **PEP 572** | Opérateur morse `:=` |
| **PEP 634** | Filtrage par motifs (`match`) |
| **PEP 621** | Métadonnées de projet dans `pyproject.toml` |
| **PEP 750** | Template strings (t-strings, Python 3.14) |

Consultez-les sur **<https://peps.python.org>**.

### Obtenir de l'aide

```python
help(len)          # Documentation d'une fonction
help("modules")    # Liste des modules disponibles
dir(list)          # Attributs et méthodes d'un objet
type(x)            # Type d'un objet
print(len.__doc__) # Docstring brute
```

En ligne de commande : `python -m pydoc len`. Ressources : docs.python.org, Real Python, discuss.python.org, Stack Overflow.

---

# 2. Syntaxe et indentation

---

## 2.1 Introduction à la syntaxe

La **syntaxe** d'un langage est l'ensemble des règles qui définissent un programme valide. Celle de Python est volontairement épurée : pas d'accolades, pas de point-virgule obligatoire, et des blocs délimités par l'**indentation**.

```python
nom = "Alice"
if nom:
    print(f"Bonjour {nom}")
```

## 2.2 Le rôle de l'indentation

En Python, l'indentation **fait partie de la syntaxe** : elle définit les blocs de code (fonctions, boucles, conditions, classes).

```python
def saluer(nom):
    if nom:
        print(f"Bonjour {nom}")   # bloc du if
    else:
        print("Bonjour inconnu")  # bloc du else
```

### Règles et bonnes pratiques

| Règle | Détail |
| --- | --- |
| Taille standard | **4 espaces** par niveau (PEP 8) |
| Cohérence | Gardez la même indentation dans tout un bloc |
| Tabulations | **Ne mélangez jamais** tabulations et espaces (erreur `TabError`) |
| Éditeur | Configurez-le pour insérer 4 espaces à la touche `Tab` |

```python
# ✅ Correct
if True:
    print("Bien indenté")

# ❌ Incorrect : IndentationError
if True:
print("Mal indenté")
```

## 2.3 Blocs de code

Un **bloc** commence après une ligne terminée par `:` et regroupe les instructions indentées qui suivent.

```python
for i in range(3):          # en-tête (se termine par :)
    print(i)                # corps du bloc
    if i == 1:
        print("Un !")       # bloc imbriqué
```

Un bloc ne peut pas être vide : utilisez `pass` comme instruction « ne rien faire ».

## 2.4 Instructions simples

Une **instruction** est une commande exécutable. Une instruction par ligne est la norme.

```python
x = 5
y = 10
print(x + y)

a = 1; b = 2   # valide, mais déconseillé (PEP 8)
```

### Instructions sur plusieurs lignes

- **Antislash** `\` (à éviter si possible) :

```python
total = 1 + 2 + 3 + \
        4 + 5
```

- **Parenthèses, crochets ou accolades** (méthode recommandée) :

```python
total = (1 + 2 + 3 +
         4 + 5)

liste = [
    "pomme",
    "banane",
    "cerise",
]
```

## 2.5 Sensibilité à la casse

Python distingue majuscules et minuscules : `nom`, `Nom` et `NOM` sont trois variables différentes. Les mots-clés (`True`, `False`, `None`, `if`, `for`…) doivent être écrits exactement comme prévu.

```python
nom = "Alice"
Nom = "Bob"
print(nom, Nom)   # Alice Bob
```

## 2.6 Expressions et instructions

- Une **expression** produit une valeur : `3 + 4`, `len("abc")`, `x > 5`.
- Une **instruction** effectue une action : `x = 5`, `if`, `for`, `import`, `return`.

```python
y = (3 + 4) * 2       # instruction d'affectation contenant une expression
```

Depuis Python 3.8, l'**opérateur morse** `:=` permet d'affecter *dans* une expression :

```python
if (n := len("Python")) > 5:
    print(f"Chaîne longue ({n} caractères)")
```

## 2.7 Lignes vides et espaces

Conventions PEP 8 :

- **2 lignes vides** entre les fonctions et classes de niveau supérieur ;
- **1 ligne vide** entre les méthodes d'une classe ;
- des espaces autour des opérateurs : `x = a + b` ;
- pas d'espace avant `(` d'un appel ni avant `:` / `,`.

```python
# ✅
resultat = calculer(a, b)
valeurs = [1, 2, 3]

# ❌
resultat=calculer( a,b )
```

## 2.8 Le deux-points `:`

Le `:` introduit un bloc (`if`, `for`, `while`, `def`, `class`, `try`, `with`, `match`…), mais sert aussi aux **tranches** (`liste[1:3]`), aux **dictionnaires** (`{"a": 1}`) et aux **annotations** (`x: int`).

## 2.9 Erreurs de syntaxe et d'indentation

| Erreur | Cause | Exemple |
| --- | --- | --- |
| `SyntaxError` | Syntaxe invalide | `print("Salut"` (parenthèse manquante) |
| `IndentationError` | Indentation incorrecte | Bloc non indenté ou niveaux incohérents |
| `TabError` | Mélange tabulations/espaces | — |

Python 3.10+ fournit des messages d'erreur très explicites (*« '(' was never closed »*, *« Did you mean… »*).

## 2.10 Écrire du code propre (PEP 8)

```python
# ❌ Peu lisible
def f(x,y):return x+y

# ✅ Lisible
def additionner(x, y):
    return x + y
```

| Élément | Convention | Exemple |
| --- | --- | --- |
| Variables, fonctions | `snake_case` | `nom_utilisateur` |
| Classes | `PascalCase` | `CompteBancaire` |
| Constantes | `MAJUSCULES_AVEC_TIRETS_BAS` | `TAUX_TVA` |
| Longueur de ligne | 79–99 caractères (88 avec *Black/Ruff*) | — |

```python
# ❌ À éviter
resultat = []
for x in nombres:
    resultat.append(x * 2)

# ✅ Plus pythonique
resultat = [x * 2 for x in nombres]
```

> 🛠️ **Outils modernes** : **Ruff** (lint + formatage), **Black** (formatage), **mypy / pyright** (typage).

---

# 3. Variables et types de données

---

## 3.1 Les variables

Une **variable** est un nom qui **référence** un objet en mémoire. Python n'exige pas de déclaration de type.

```python
age = 25
nom = "Alice"
taille = 1.68
est_majeur = True
```

### Règles de nommage

- Lettres, chiffres et `_`, **sans commencer par un chiffre**
- Sensible à la casse
- Interdit d'utiliser un **mot-clé** (`class`, `if`, `for`, `None`…) — liste via `import keyword; keyword.kwlist`
- Noms explicites, en `snake_case`

```python
# ✅ Valides
nom_utilisateur = "Alice"
_prive = 1
valeur2 = 2

# ❌ Invalides
2valeur = 1       # commence par un chiffre
mon-nom = 1       # tiret interdit
class = "A"       # mot-clé réservé
```

| Convention | Signification |
| --- | --- |
| `_x` | Usage interne (convention) |
| `x_` | Évite un conflit avec un mot-clé (`class_`) |
| `__x` | Mangling de nom dans les classes |
| `__x__` | Méthodes spéciales (dunder) |

### Affectation

```python
x = 5                    # simple
a = b = c = 0            # multiple, même valeur
x, y, z = 1, 2, 3        # multiple, valeurs différentes
a, b = b, a              # échange sans variable temporaire
premier, *reste = [1, 2, 3, 4]   # déballage étoilé : 1, [2, 3, 4]
```

## 3.2 Vue d'ensemble des types de base

| Catégorie | Types |
| --- | --- |
| Numériques | `int`, `float`, `complex` |
| Texte | `str` |
| Booléen | `bool` |
| Absence de valeur | `NoneType` |
| Séquences | `list`, `tuple`, `range` |
| Ensembles | `set`, `frozenset` |
| Associations | `dict` |
| Binaires | `bytes`, `bytearray`, `memoryview` |

## 3.3 Types numériques

```python
entier = 42              # int (taille illimitée)
grand = 10 ** 100        # pas de dépassement d'entier
flottant = 3.14          # float (double précision IEEE 754)
complexe = 2 + 3j        # complex
```

```python
print(1_000_000)         # séparateurs de lisibilité : 1000000
print(0b1010, 0o17, 0xFF)   # binaire, octal, hexadécimal
print(0.1 + 0.2)         # 0.30000000000000004 (imprécision des flottants)
```

Pour la précision exacte, utilisez `decimal.Decimal` (finance) ou `fractions.Fraction` :

```python
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))   # 0.3
```

Fonctions utiles : `abs()`, `round()`, `pow()`, `divmod()`, `math.floor()`, `math.ceil()`, `math.isclose()`.

## 3.4 Chaînes de caractères (`str`)

Les chaînes sont des séquences de caractères **Unicode**, **immuables**.

```python
s1 = 'simple'
s2 = "double"
s3 = """multi
ligne"""
brut = r"C:\nouveau\dossier"     # chaîne brute (pas d'échappement)
```

```python
s = "Python"
print(s[0], s[-1])       # P n
print(s[1:4])            # yth
print(len(s))            # 6
# s[0] = "J"             # ❌ TypeError : immuable
```

| Méthode | Rôle |
| --- | --- |
| `upper()`, `lower()`, `title()`, `capitalize()` | Casse |
| `strip()`, `lstrip()`, `rstrip()` | Supprime les espaces |
| `split(sep)`, `"-".join(liste)` | Découper / assembler |
| `replace(a, b)` | Remplacer |
| `find()`, `index()`, `count()` | Rechercher |
| `startswith()`, `endswith()` | Tester début / fin |
| `removeprefix()`, `removesuffix()` | Retirer préfixe / suffixe (3.9+) |
| `isdigit()`, `isalpha()`, `isalnum()` | Tester le contenu |

### F-strings (formatage moderne)

```python
nom, age = "Alice", 30
print(f"{nom} a {age} ans")
print(f"{3.14159:.2f}")           # 3.14
print(f"{nom=}")                  # nom='Alice' (débogage)
```

## 3.5 Booléens

```python
a = True
b = False
print(5 > 3)              # True
print(isinstance(True, int))   # True : bool hérite de int
```

**Valeurs « fausses »** (*falsy*) : `False`, `None`, `0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`. Tout le reste est « vrai » (*truthy*).

```python
if not liste:
    print("La liste est vide")
```

## 3.6 `None`

`None` représente l'**absence de valeur**. C'est l'unique instance de `NoneType`. Il se compare avec `is`.

```python
resultat = None
if resultat is None:
    print("Pas encore de résultat")

def sans_return():
    pass
print(sans_return())   # None
```

## 3.7 Conversion de types (*casting*)

```python
int("42")          # 42
int(3.9)           # 3 (troncature)
float("3.14")      # 3.14
str(100)           # "100"
bool(0)            # False
list("abc")        # ['a', 'b', 'c']
tuple([1, 2])      # (1, 2)
set([1, 1, 2])     # {1, 2}
dict([("a", 1)])   # {'a': 1}
```

```python
try:
    int("abc")
except ValueError:
    print("Conversion impossible")
```

> Python effectue des conversions **implicites** pour les nombres (`1 + 2.0 → 3.0`) mais jamais entre nombre et chaîne (`"1" + 2` lève `TypeError`).

## 3.8 Vérifier le type

```python
x = 42
print(type(x))                   # <class 'int'>
print(isinstance(x, int))        # True
print(isinstance(x, (int, float)))   # True : plusieurs types
```

Préférez `isinstance()` à `type(x) == int` : il respecte l'héritage.

## 3.9 Types mutables et immuables

| Immuables | Mutables |
| --- | --- |
| `int`, `float`, `bool`, `str`, `tuple`, `frozenset`, `bytes`, `None` | `list`, `dict`, `set`, `bytearray`, objets personnalisés |

```python
a = [1, 2]
b = a              # même objet !
b.append(3)
print(a)           # [1, 2, 3]

c = a.copy()       # copie indépendante
```

`id(x)` donne l'identité d'un objet ; `is` compare les identités, `==` compare les valeurs.

## 3.10 Constantes

Python n'a pas de vraies constantes ; on utilise la **convention** `MAJUSCULES` et, pour les outils de typage, `Final` :

```python
from typing import Final

PI: Final = 3.14159
MAX_ESSAIS: Final[int] = 3
```

Pour des ensembles de constantes liées, utilisez `enum.Enum` (voir [section 16](#16-programmation-orientée-objet)).

## 3.11 Portée des variables (règle LEGB)

Python recherche un nom dans l'ordre : **L**ocal → **E**nglobant → **G**lobal → **B**uilt-in.

```python
x = "global"

def f():
    x = "local"        # variable locale, masque la globale
    print(x)

f()                    # local
print(x)               # global
```

```python
compteur = 0

def incrementer():
    global compteur    # modifie la variable globale
    compteur += 1
```

`nonlocal` permet de modifier une variable d'une fonction englobante (voir [section 11](#11-fonctions)).

## 3.12 Bonnes pratiques

```python
# ❌ Peu clair
d = 86400

# ✅ Explicite
SECONDES_PAR_JOUR = 86400
```

- Noms **descriptifs**, pas de mutation inutile du type d'une variable.
- Évitez les variables globales.
- Évitez les valeurs « magiques » : nommez-les.
- Utilisez `None` comme valeur par défaut pour les objets mutables.

---

# 4. Opérateurs et expressions

---

## 4.1 Opérateurs arithmétiques

| Opérateur | Nom | Exemple | Résultat |
| --- | --- | --- | --- |
| `+` | Addition | `5 + 2` | `7` |
| `-` | Soustraction | `5 - 2` | `3` |
| `*` | Multiplication | `5 * 2` | `10` |
| `/` | Division (toujours `float`) | `5 / 2` | `2.5` |
| `//` | Division entière (plancher) | `5 // 2` | `2` |
| `%` | Modulo | `5 % 2` | `1` |
| `**` | Puissance | `5 ** 2` | `25` |
| `@` | Produit matriciel (NumPy…) | `A @ B` | — |

```python
print(-7 // 2)    # -4 (arrondi vers le bas)
print(-7 % 2)     # 1
print(divmod(7, 2))   # (3, 1)
```

## 4.2 Opérateurs d'affectation

```python
x = 5
x += 2     # x = x + 2
x -= 1
x *= 3
x /= 2
x //= 2
x %= 3
x **= 2
```

Aussi : `&=`, `|=`, `^=`, `<<=`, `>>=`, et l'opérateur morse `:=`.

## 4.3 Opérateurs de comparaison

`==`, `!=`, `>`, `<`, `>=`, `<=` — résultat booléen. Les comparaisons peuvent être **chaînées** :

```python
x = 5
print(1 < x < 10)    # True (équivaut à 1 < x and x < 10)
```

## 4.4 Opérateurs logiques

| Opérateur | Rôle |
| --- | --- |
| `and` | Vrai si les deux opérandes sont vrais |
| `or` | Vrai si au moins un est vrai |
| `not` | Inverse |

**Évaluation paresseuse** (*short-circuit*) : `and` / `or` retournent l'un de leurs opérandes et s'arrêtent dès que le résultat est connu.

```python
nom = utilisateur or "Anonyme"       # valeur par défaut
resultat = liste and liste[0]        # évite l'IndexError
```

## 4.5 Opérateurs bit à bit

| Opérateur | Nom | Exemple (`a=5`, `b=3`) |
| --- | --- | --- |
| `&` | ET | `5 & 3 → 1` |
| `\|` | OU | `5 \| 3 → 7` |
| `^` | OU exclusif | `5 ^ 3 → 6` |
| `~` | NON | `~5 → -6` |
| `<<` | Décalage gauche | `5 << 1 → 10` |
| `>>` | Décalage droit | `5 >> 1 → 2` |

## 4.6 Opérateurs d'identité et d'appartenance

```python
a = [1, 2]
b = [1, 2]
print(a == b)        # True  : mêmes valeurs
print(a is b)        # False : objets différents
print(x is None)     # ✅ comparaison correcte avec None
```

```python
print("a" in "banane")          # True
print(3 in [1, 2, 3])           # True
print("clé" in {"clé": 1})      # True (teste les clés)
print(5 not in {1, 2})          # True
```

> 💡 `in` est **très rapide** sur un `set` ou un `dict` (O(1)), mais lent sur une `list` (O(n)).

## 4.7 Priorité et associativité

De la **plus haute** à la **plus basse** priorité :

| Priorité | Opérateurs |
| --- | --- |
| 1 | `()` parenthèses |
| 2 | `**` (associatif à droite) |
| 3 | `+x`, `-x`, `~x` (unaires) |
| 4 | `*`, `/`, `//`, `%`, `@` |
| 5 | `+`, `-` |
| 6 | `<<`, `>>` |
| 7 | `&`, puis `^`, puis `\|` |
| 8 | `==`, `!=`, `<`, `>`, `in`, `is`… |
| 9 | `not`, puis `and`, puis `or` |
| 10 | `if … else` (ternaire), `lambda` |
| 11 | `:=` |

```python
print(2 ** 3 ** 2)    # 512 : 2 ** (3 ** 2)
print(2 + 3 * 4)      # 14
print(10 - 5 - 2)     # 3 : de gauche à droite
```

En cas de doute, **ajoutez des parenthèses**.

## 4.8 Expressions et évaluation

Une expression est évaluée de l'intérieur vers l'extérieur, selon la priorité :

```python
resultat = 3 * (4 + 2) ** 2 // 5 % 3 + 2
# (4+2) = 6 → 6**2 = 36 → 3*36 = 108 → 108//5 = 21 → 21%3 = 0 → 0+2 = 2
```

Les appels de fonction, compréhensions et expressions conditionnelles sont aussi des expressions.

## 4.9 Surcharge d'opérateurs (introduction)

Grâce aux **méthodes spéciales**, vos classes peuvent utiliser les opérateurs :

```python
class Vecteur:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, autre):
        return Vecteur(self.x + autre.x, self.y + autre.y)

    def __eq__(self, autre):
        return (self.x, self.y) == (autre.x, autre.y)

    def __repr__(self):
        return f"Vecteur({self.x}, {self.y})"

print(Vecteur(1, 2) + Vecteur(3, 4))   # Vecteur(4, 6)
```

| Opérateur | Méthode |
| --- | --- |
| `+` `-` `*` `/` | `__add__`, `__sub__`, `__mul__`, `__truediv__` |
| `==` `<` | `__eq__`, `__lt__` |
| `len()` | `__len__` |
| `[]` | `__getitem__` |

## 4.10 Pièges courants

```python
# 1. Imprécision des flottants
print(0.1 + 0.2 == 0.3)               # False
import math
print(math.isclose(0.1 + 0.2, 0.3))   # ✅ True

# 2. is vs ==
a = 1000; b = 1000
# Utilisez == pour les valeurs, is seulement pour None/True/False

# 3. Priorité de not
print(not 1 == 2)    # not (1 == 2) → True

# 4. Valeur par défaut mutable (voir section Fonctions)
```

## 4.11 Bonnes pratiques

```python
# ❌ Trop dense
r = a if b else c if d else e

# ✅ Plus clair
if b:
    r = a
elif d:
    r = c
else:
    r = e
```

- Parenthèses pour clarifier, expressions courtes.
- `is None` / `is not None` plutôt que `== None`.
- Évitez les chaînes de ternaires.

---

# 5. Entrées et sorties

---

## 5.1 Introduction

Les **entrées/sorties (E/S)** permettent à un programme d'échanger des données avec l'extérieur : clavier, écran, fichiers, réseau, bases de données.

| Source / destination | Outils |
| --- | --- |
| Clavier / écran | `input()`, `print()` |
| Arguments de ligne de commande | `sys.argv`, `argparse` |
| Fichiers | `open()`, `pathlib` |
| Réseau | `socket`, `requests`, `httpx` |

## 5.2 Lire une saisie utilisateur

`input()` renvoie **toujours une chaîne**.

```python
nom = input("Votre nom : ")
age = int(input("Votre âge : "))   # conversion nécessaire
print(f"{nom}, dans 10 ans vous aurez {age + 10} ans")
```

### Saisie robuste

```python
while True:
    try:
        age = int(input("Âge : "))
        break
    except ValueError:
        print("Veuillez entrer un nombre entier.")
```

### Plusieurs valeurs sur une ligne

```python
a, b = map(int, input("Deux entiers : ").split())
```

### Mot de passe et arguments

```python
from getpass import getpass
mdp = getpass("Mot de passe : ")     # saisie masquée

import sys
print(sys.argv)                      # arguments de la ligne de commande
```

Pour des programmes en ligne de commande, préférez le module **`argparse`** (ou `typer` / `click`).

## 5.3 Afficher dans la console

```python
print("Texte")
print("A", "B", sep=" | ", end="!\n")
print("Erreur !", file=sys.stderr)
```

Pour des structures complexes : `pprint.pprint(donnees)`.

## 5.4 Formater les sorties

### F-strings (recommandé)

```python
nom, prix = "Café", 2.5
print(f"{nom:<10} {prix:>8.2f} €")
```

### Spécificateurs de format

| Format | Effet | Exemple |
| --- | --- | --- |
| `:.2f` | 2 décimales | `f"{3.14159:.2f}"` → `3.14` |
| `:,` | Séparateur de milliers | `f"{1234567:,}"` → `1,234,567` |
| `:>10` | Aligné à droite sur 10 | — |
| `:<10` | Aligné à gauche | — |
| `:^10` | Centré | — |
| `:05d` | Complété par des zéros | `f"{42:05d}"` → `00042` |
| `:.1%` | Pourcentage | `f"{0.256:.1%}"` → `25.6%` |
| `:b`, `:x`, `:o` | Binaire, hexa, octal | — |
| `:e` | Notation scientifique | — |

### Autres méthodes

```python
print("{} a {} ans".format("Alice", 30))        # str.format()
print("%s a %d ans" % ("Alice", 30))            # ancien style %
```

### Template strings (t-strings, Python 3.14+)

Les **t-strings** (PEP 750) ressemblent aux f-strings mais produisent un objet `Template` plutôt qu'une chaîne finale. Elles permettent de traiter les valeurs interpolées de façon sûre (échappement HTML, requêtes SQL…) :

```python
nom = "Alice"
modele = t"Bonjour {nom}"     # objet Template, non évalué en str
```

## 5.5 Formater les dates et heures

```python
from datetime import datetime

maintenant = datetime.now()
print(maintenant.strftime("%d/%m/%Y %H:%M:%S"))   # 11/10/2026 14:30:00

date = datetime.strptime("25/12/2026", "%d/%m/%Y")  # chaîne → date
print(f"{maintenant:%A %d %B %Y}")
```

| Code | Signification |
| --- | --- |
| `%d` `%m` `%Y` | Jour, mois, année (4 chiffres) |
| `%H` `%M` `%S` | Heure, minute, seconde |
| `%A` `%B` | Nom du jour, du mois |

Pour les fuseaux horaires, utilisez `zoneinfo` (bibliothèque standard).

## 5.6 Bonnes pratiques

- Validez et **convertissez** toujours les saisies.
- Utilisez les **f-strings** pour la lisibilité.
- Envoyez les messages d'erreur sur `stderr`, ou utilisez le module `logging`.
- Pour les programmes non interactifs, privilégiez les arguments en ligne de commande.

---

# 6. Structures de contrôle

---

## 6.1 Introduction

Les structures de contrôle déterminent **l'ordre d'exécution** des instructions :

| Type | Instructions |
| --- | --- |
| **Séquence** | Exécution ligne par ligne |
| **Sélection** | `if` / `elif` / `else`, `match` / `case` |
| **Itération** | `for`, `while` |
| **Contrôle de boucle** | `break`, `continue`, `else`, `pass` |

## 6.2 Conditions : `if`, `elif`, `else`

```python
note = 14

if note >= 16:
    print("Très bien")
elif note >= 12:
    print("Bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")
```

- Les conditions peuvent combiner `and`, `or`, `not` et des comparaisons chaînées (`10 <= note <= 20`).
- Toute valeur est « vraie » ou « fausse » (voir *truthy / falsy*).

## 6.3 Opérateur ternaire

```python
statut = "majeur" if age >= 18 else "mineur"
```

À réserver aux cas simples ; évitez d'imbriquer plusieurs ternaires.

## 6.4 Filtrage par motifs : `match` / `case` *(Python 3.10+)*

Équivalent évolué du `switch` d'autres langages : il compare une valeur à des **motifs** structurels.

```python
def reponse_http(code):
    match code:
        case 200:
            return "OK"
        case 301 | 302:
            return "Redirection"
        case 404:
            return "Introuvable"
        case _:
            return "Code inconnu"
```

Décomposition de structures et gardes :

```python
def decrire(point):
    match point:
        case (0, 0):
            return "Origine"
        case (x, 0):
            return f"Sur l'axe X à {x}"
        case {"x": x, "y": y} if x == y:
            return "Sur la diagonale"
        case [premier, *reste]:
            return f"Séquence commençant par {premier}"
        case _:
            return "Autre"
```

## 6.5 L'instruction `pass`

`pass` ne fait rien ; elle sert de **substitut** là où un bloc est syntaxiquement requis.

```python
def a_implementer():
    pass

class Vide:
    pass
```

(On peut aussi utiliser `...` — `Ellipsis` — comme corps provisoire.)

## 6.6 Boucles : vue d'ensemble

| Boucle | Usage |
| --- | --- |
| `for` | Parcourir un itérable, ou répéter un nombre connu de fois |
| `while` | Répéter tant qu'une condition est vraie |

## 6.7 La boucle `while`

```python
compteur = 0
while compteur < 3:
    print(compteur)
    compteur += 1
```

⚠️ Veillez à ce que la condition devienne fausse, sinon la boucle est **infinie** (utile volontairement avec `while True` + `break`).

## 6.8 La boucle `for`

```python
for fruit in ["pomme", "banane"]:
    print(fruit)

for i in range(5):            # 0 à 4
    print(i)

for i in range(2, 10, 2):     # début, fin (exclue), pas
    print(i)
```

### Outils de parcours

```python
noms = ["Alice", "Bob"]
ages = [30, 25]

for i, nom in enumerate(noms, start=1):   # indice + valeur
    print(i, nom)

for nom, age in zip(noms, ages):          # parcours parallèle
    print(nom, age)

for x in reversed(noms):                  # sens inverse
    print(x)

for x in sorted(ages):                    # trié
    print(x)
```

`zip(..., strict=True)` *(3.10+)* lève une erreur si les longueurs diffèrent.

## 6.9 `break`, `continue` et `else` de boucle

```python
for n in range(10):
    if n == 3:
        continue     # passe à l'itération suivante
    if n == 6:
        break        # quitte la boucle
    print(n)
```

La clause `else` d'une boucle s'exécute **uniquement si la boucle s'est terminée sans `break`** :

```python
for n in range(2, 10):
    if n == 7:
        print("Trouvé")
        break
else:
    print("Aucun 7")
```

## 6.10 Boucles imbriquées et motifs

```python
for i in range(1, 4):
    print("*" * i)
# *
# **
# ***

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()
```

## 6.11 Bonnes pratiques

```python
# ❌ Imbrication excessive
def f(x):
    if x:
        if x > 0:
            return "positif"

# ✅ Retour anticipé (clauses de garde)
def f(x):
    if not x or x <= 0:
        return None
    return "positif"
```

- Préférez `for` à `while` quand le nombre d'itérations est connu.
- N'utilisez pas `range(len(liste))` : préférez `enumerate()` ou l'itération directe.
- Pour des transformations simples, préférez les **compréhensions**.
- Ne modifiez pas une liste pendant que vous la parcourez.

---

# 7. Dictionnaires

---

## 7.1 Introduction

Un **dictionnaire** (`dict`) stocke des paires **clé → valeur**.

- **Mutable** et dynamique
- Les clés sont **uniques** et doivent être **hachables** (immuables)
- **Ordonné par insertion** (garanti depuis Python 3.7)
- Accès, ajout et suppression en **O(1)** en moyenne

```python
personne = {"nom": "Alice", "age": 25, "ville": "Paris"}
```

## 7.2 Créer un dictionnaire

```python
vide = {}
vide2 = dict()
d1 = {"a": 1, "b": 2}
d2 = dict(a=1, b=2)                          # clés = identifiants valides
d3 = dict([("a", 1), ("b", 2)])              # liste de paires
d4 = dict(zip(["a", "b"], [1, 2]))           # depuis deux listes
d5 = dict.fromkeys(["x", "y"], 0)            # {'x': 0, 'y': 0}
d6 = {n: n ** 2 for n in range(4)}           # compréhension
```

## 7.3 Accéder aux éléments

```python
p = {"nom": "Alice", "age": 25}

print(p["nom"])               # Alice (KeyError si absente)
print(p.get("ville"))         # None
print(p.get("ville", "N/A"))  # N/A
```

Préférez `get()` quand la clé peut être absente.

## 7.4 Ajouter, modifier, supprimer

```python
p["ville"] = "Paris"              # ajout
p["age"] = 26                     # modification
p.update({"age": 27, "pays": "FR"})
p.setdefault("langue", "fr")      # ajoute seulement si absente

del p["pays"]                     # supprime (KeyError si absente)
age = p.pop("age")                # supprime et retourne
age = p.pop("age", None)          # sans erreur si absente
dernier = p.popitem()             # retire la dernière paire (LIFO)
p.clear()                         # vide le dictionnaire
```

## 7.5 Méthodes principales

| Méthode | Rôle |
| --- | --- |
| `keys()` | Vue des clés |
| `values()` | Vue des valeurs |
| `items()` | Vue des paires `(clé, valeur)` |
| `get(k, défaut)` | Valeur ou défaut |
| `setdefault(k, v)` | Ajoute si absente et retourne la valeur |
| `update(autre)` | Fusionne |
| `pop(k[, défaut])` | Supprime et retourne |
| `copy()` | Copie superficielle |

## 7.6 Parcourir un dictionnaire

```python
for cle in p:                       # clés
    print(cle)
for valeur in p.values():           # valeurs
    print(valeur)
for cle, valeur in p.items():       # paires
    print(f"{cle} = {valeur}")
```

⚠️ Ne modifiez pas la **taille** d'un dictionnaire pendant son parcours (`RuntimeError`) ; parcourez `list(p)` si besoin.

## 7.7 Compréhensions de dictionnaires

```python
carres = {n: n ** 2 for n in range(5)}
pairs = {k: v for k, v in carres.items() if v % 2 == 0}
inverse = {v: k for k, v in carres.items()}
```

## 7.8 Test d'appartenance

```python
print("nom" in p)         # teste les clés
print("Alice" in p.values())   # teste les valeurs (O(n))
```

## 7.9 Dictionnaires imbriqués

```python
users = {
    "alice": {"age": 25, "langues": ["fr", "en"]},
    "bob":   {"age": 30, "langues": ["fr"]},
}
print(users["alice"]["langues"][0])    # fr
users["bob"]["ville"] = "Lyon"
```

## 7.10 Fusionner des dictionnaires

```python
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

c = a | b            # {'x': 1, 'y': 3, 'z': 4}  (3.9+)
a |= b               # fusion en place
d = {**a, **b}       # déballage (toutes versions 3.5+)
```

En cas de clé commune, **la dernière valeur l'emporte**.

## 7.11 Clés hachables

Seuls les objets **immuables et hachables** peuvent être clés : `str`, `int`, `float`, `bool`, `tuple` (de valeurs hachables), `frozenset`.

```python
ok = {(1, 2): "point"}
# {[1, 2]: "x"}    # ❌ TypeError : list non hachable
```

## 7.12 Le module `collections`

```python
from collections import defaultdict, Counter, OrderedDict

# defaultdict : valeur par défaut automatique
groupes = defaultdict(list)
for mot in ["chat", "chien", "souris"]:
    groupes[mot[0]].append(mot)
# {'c': ['chat', 'chien'], 's': ['souris']}

# Counter : compter des occurrences
c = Counter("abracadabra")
print(c.most_common(2))     # [('a', 5), ('b', 2)]
```

> `OrderedDict` n'est plus nécessaire pour conserver l'ordre (les `dict` le font), mais reste utile pour `move_to_end()` et la comparaison sensible à l'ordre.

## 7.13 Dictionnaires et JSON

```python
import json

texte = json.dumps({"nom": "Alice", "age": 25}, indent=2, ensure_ascii=False)
donnees = json.loads(texte)
```

## 7.14 Performances

| Opération | Complexité moyenne |
| --- | --- |
| Accès `d[k]`, insertion, suppression | **O(1)** |
| `k in d` | **O(1)** |
| Parcours | O(n) |
| `v in d.values()` | O(n) |

## 7.15 Programmation fonctionnelle et idiomes

```python
# Tri par valeur
tri = dict(sorted(p.items(), key=lambda kv: kv[1]))

# Plus grande valeur
meilleur = max(scores, key=scores.get)

# Filtrer
adultes = {n: a for n, a in ages.items() if a >= 18}

# Compter avec get
freq = {}
for ch in "banane":
    freq[ch] = freq.get(ch, 0) + 1
```

Pour des données structurées à clés fixes, préférez un **`dataclass`** ou un **`TypedDict`** (voir [sections 16](#16-programmation-orientée-objet) et [17](#17-typage-statique)).

---

# 8. Listes

---

## 8.1 Introduction

Une **liste** (`list`) est une collection **ordonnée, mutable** pouvant contenir des éléments de types différents et des doublons.

```python
fruits = ["pomme", "banane", "cerise"]
melange = [1, "deux", 3.0, [4, 5]]
```

## 8.2 Créer des listes

```python
vide = []
vide2 = list()
a = list("abc")                 # ['a', 'b', 'c']
b = list(range(5))              # [0, 1, 2, 3, 4]
c = [0] * 3                     # [0, 0, 0]
d = [x ** 2 for x in range(5)]  # compréhension
```

## 8.3 Accéder aux éléments

```python
l = [10, 20, 30, 40, 50]
print(l[0], l[-1])      # 10 50
print(l[1:4])           # [20, 30, 40]
print(l[::2])           # [10, 30, 50]
print(l[::-1])          # [50, 40, 30, 20, 10]
```

Syntaxe d'une tranche : `liste[début:fin:pas]` (fin exclue).

## 8.4 Modifier une liste

```python
l[0] = 11
l[1:3] = [21, 31]          # remplace une tranche
```

## 8.5 Ajouter des éléments

```python
l.append(60)               # ajoute à la fin
l.insert(0, 5)             # insère à l'indice 0
l.extend([70, 80])         # ajoute plusieurs éléments
l += [90]                  # équivalent à extend
```

⚠️ `append([1, 2])` ajoute **une sous-liste**, `extend([1, 2])` ajoute **deux éléments**.

## 8.6 Supprimer des éléments

```python
l.remove(30)               # supprime la 1re occurrence (ValueError si absente)
dernier = l.pop()          # retire et retourne le dernier
premier = l.pop(0)         # retire par indice
del l[1]                   # supprime par indice
del l[1:3]                 # supprime une tranche
l.clear()                  # vide la liste
```

## 8.7 Rechercher

```python
l = [3, 1, 4, 1, 5]
print(4 in l)              # True
print(l.index(1))          # 1 (première occurrence)
print(l.count(1))          # 2
```

Pour une recherche rapide sur liste **triée**, utilisez `bisect`.

## 8.8 Trier et inverser

```python
l.sort()                           # tri en place
l.sort(reverse=True)
l.sort(key=len)                    # selon une clé
nouvelle = sorted(l)               # nouvelle liste triée
l.reverse()                        # inverse en place
inverse = l[::-1]                  # copie inversée
```

`sort()` est **stable** (l'ordre relatif des égaux est conservé).

### Tri personnalisé

```python
personnes = [("Alice", 30), ("Bob", 25), ("Chloé", 30)]
personnes.sort(key=lambda p: (-p[1], p[0]))   # âge décroissant, puis nom
```

## 8.9 Fonctions et méthodes utiles

| Fonction | Rôle |
| --- | --- |
| `len(l)` | Nombre d'éléments |
| `sum(l)`, `min(l)`, `max(l)` | Somme, minimum, maximum |
| `any(l)`, `all(l)` | Au moins un / tous vrais |
| `sorted(l)`, `reversed(l)` | Tri / inversion |
| `enumerate(l)`, `zip(a, b)` | Parcours enrichis |

Méthodes : `append`, `extend`, `insert`, `remove`, `pop`, `clear`, `index`, `count`, `sort`, `reverse`, `copy`.

## 8.10 Compréhensions de listes

```python
carres = [x ** 2 for x in range(10)]
pairs = [x for x in range(10) if x % 2 == 0]
etiquettes = ["pair" if x % 2 == 0 else "impair" for x in range(4)]
aplatie = [x for ligne in matrice for x in ligne]
```

Si la liste est trop longue pour être lue d'un coup, utilisez une boucle classique.

## 8.11 Copier une liste

```python
a = [1, 2, [3, 4]]
b = a                  # ⚠️ même objet (alias)
c = a.copy()           # copie superficielle (ou a[:] ou list(a))

import copy
d = copy.deepcopy(a)   # copie profonde (sous-listes incluses)

c[2].append(5)         # modifie aussi a[2] !
```

## 8.12 Listes imbriquées et multidimensionnelles

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
]
print(matrice[1][2])      # 6

# ✅ Création correcte d'une matrice 3x3
grille = [[0] * 3 for _ in range(3)]

# ❌ Piège : toutes les lignes sont la même liste !
mauvaise = [[0] * 3] * 3
mauvaise[0][0] = 1        # modifie les 3 lignes
```

Pour le calcul numérique sur matrices, utilisez **NumPy**.

## 8.13 Déballage de listes

```python
a, b, c = [1, 2, 3]
premier, *milieu, dernier = [1, 2, 3, 4, 5]   # milieu = [2, 3, 4]
a, b = b, a                                    # échange

def somme(x, y, z): return x + y + z
print(somme(*[1, 2, 3]))                       # déballage dans un appel
```

## 8.14 Outils fonctionnels

```python
nombres = [1, 2, 3, 4]
doubles = list(map(lambda x: x * 2, nombres))
pairs = list(filter(lambda x: x % 2 == 0, nombres))

from functools import reduce
produit = reduce(lambda a, b: a * b, nombres)   # 24
```

Les compréhensions sont généralement plus lisibles que `map` / `filter`.

## 8.15 Listes et chaînes

```python
mots = "un deux trois".split()          # ['un', 'deux', 'trois']
phrase = " ".join(mots)                 # 'un deux trois'
lettres = list("abc")                   # ['a', 'b', 'c']
```

## 8.16 Listes comparées aux autres collections

| Critère | `list` | `tuple` | `set` | `dict` |
| --- | --- | --- | --- | --- |
| Ordonné | ✅ | ✅ | ❌ | ✅ (insertion) |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Doublons | ✅ | ✅ | ❌ | clés uniques |
| Accès par indice | ✅ | ✅ | ❌ | par clé |
| Test `in` | O(n) | O(n) | **O(1)** | **O(1)** |

> Pour une **file** (ajouts/retraits aux deux extrémités), utilisez `collections.deque` : `append()` et `popleft()` y sont en O(1), alors que `list.pop(0)` est en O(n).

---

# 9. Ensembles

---

## 9.1 Introduction

Un **ensemble** (`set`) est une collection **non ordonnée** d'éléments **uniques et hachables**. Il est **mutable**.

```python
fruits = {"pomme", "banane", "pomme"}
print(fruits)          # {'pomme', 'banane'} (doublons supprimés)
```

## 9.2 Créer des ensembles

```python
s = {1, 2, 3}
vide = set()           # ⚠️ {} crée un dictionnaire, pas un ensemble
a = set([1, 2, 2, 3])  # depuis une liste
b = set("abca")        # {'a', 'b', 'c'}
c = {x ** 2 for x in range(5)}   # compréhension
```

## 9.3 Accéder aux éléments

Pas d'indice : `s[0]` lève une `TypeError`. On parcourt ou on teste l'appartenance :

```python
for x in s:
    print(x)
print(2 in s)          # True (O(1))
```

## 9.4 Ajouter et supprimer

```python
s.add(4)
s.update([5, 6])

s.remove(4)            # KeyError si absent
s.discard(99)          # aucune erreur si absent
x = s.pop()            # retire un élément arbitraire
s.clear()
```

## 9.5 Opérations ensemblistes

| Opération | Opérateur | Méthode |
| --- | --- | --- |
| Union | `a \| b` | `a.union(b)` |
| Intersection | `a & b` | `a.intersection(b)` |
| Différence | `a - b` | `a.difference(b)` |
| Différence symétrique | `a ^ b` | `a.symmetric_difference(b)` |

```python
a = {1, 2, 3}
b = {3, 4}
print(a | b)    # {1, 2, 3, 4}
print(a & b)    # {3}
print(a - b)    # {1, 2}
print(a ^ b)    # {1, 2, 4}
```

## 9.6 Comparaisons et sous-ensembles

```python
{1, 2} <= {1, 2, 3}        # True  : sous-ensemble (issubset)
{1, 2, 3} >= {1, 2}        # True  : sur-ensemble (issuperset)
{1, 2}.isdisjoint({3, 4})  # True  : aucun élément commun
```

## 9.7 Ensembles figés (`frozenset`)

Version **immuable** et **hachable** d'un ensemble : utilisable comme clé de dictionnaire ou élément d'un autre ensemble.

```python
fs = frozenset([1, 2, 3])
# fs.add(4)    # ❌ AttributeError
```

## 9.8 Cas d'usage

```python
# Supprimer les doublons (ordre non conservé)
uniques = list(set(liste))

# Supprimer les doublons en conservant l'ordre
uniques = list(dict.fromkeys(liste))

# Éléments communs
communs = set(a) & set(b)

# Recherche rapide
interdits = {"admin", "root"}
if nom in interdits: ...
```

## 9.9 Pièges et bonnes pratiques

- `{}` crée un **dict** ; utilisez `set()` pour un ensemble vide.
- Les éléments doivent être **hachables** : `{[1, 2]}` lève une `TypeError`.
- **Ne comptez pas sur l'ordre** d'un ensemble.
- Utilisez les ensembles pour les tests d'appartenance fréquents et les opérations de comparaison.

---

# 10. Tuples

---

## 10.1 Introduction

Un **tuple** est une séquence **ordonnée et immuable**.

```python
point = (3, 4)
```

## 10.2 Créer des tuples

```python
t = (1, 2, 3)
sans_parentheses = 1, 2, 3
vide = ()
singleton = (5,)          # ⚠️ la virgule est obligatoire
pas_un_tuple = (5)        # c'est simplement un int
depuis_liste = tuple([1, 2, 3])
```

## 10.3 Accéder aux éléments

```python
t = ("a", "b", "c", "d")
print(t[0], t[-1])       # a d
print(t[1:3])            # ('b', 'c')
```

## 10.4 Opérations et méthodes

```python
(1, 2) + (3,)            # (1, 2, 3)
(0,) * 3                 # (0, 0, 0)
2 in (1, 2, 3)           # True
len(t)

t = (1, 2, 2, 3)
t.count(2)               # 2
t.index(3)               # 3
```

Un tuple n'a que **deux méthodes** : `count()` et `index()`.

## 10.5 Déballage

```python
x, y = (10, 20)
a, *reste = (1, 2, 3, 4)      # a = 1, reste = [2, 3, 4]
x, y = y, x                   # échange

def min_max(valeurs):
    return min(valeurs), max(valeurs)    # retourne un tuple
mini, maxi = min_max([3, 1, 4])
```

## 10.6 Immuabilité

On ne peut pas modifier un tuple, mais un **objet mutable qu'il contient** reste modifiable :

```python
t = (1, [2, 3])
t[1].append(4)       # ✅ autorisé : t == (1, [2, 3, 4])
# t[0] = 9           # ❌ TypeError
```

## 10.7 Tuples comme clés de dictionnaire

```python
distances = {(48.85, 2.35): "Paris", (45.76, 4.84): "Lyon"}
```

Un tuple n'est hachable que si **tous** ses éléments le sont.

## 10.8 Tuples ou listes ?

| Critère | Tuple | Liste |
| --- | --- | --- |
| Mutable | ❌ | ✅ |
| Hachable (clé de dict) | ✅ (si contenu hachable) | ❌ |
| Mémoire / vitesse | Plus léger, plus rapide | Plus lourd |
| Usage typique | Données hétérogènes de taille fixe (coordonnées, enregistrements) | Collection homogène de taille variable |

## 10.9 Tuples imbriqués

```python
t = ((1, 2), (3, 4))
print(t[1][0])         # 3
(a, b), (c, d) = t     # déballage imbriqué
```

## 10.10 Cas d'usage et sujets avancés

- Retourner **plusieurs valeurs** depuis une fonction
- Valeurs constantes (jours, couleurs RVB…)
- `*args` : les arguments positionnels variables forment un tuple
- `enumerate()` et `zip()` produisent des tuples

### Tuples nommés

```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p[1])         # 3 4
```

Version typée (recommandée) :

```python
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float = 0.0

p = Point(3)
```

## 10.11 Erreurs courantes

| Erreur | Cause | Solution |
| --- | --- | --- |
| `TypeError: 'tuple' object does not support item assignment` | Modification d'un tuple | Créer un nouveau tuple, ou utiliser une liste |
| `ValueError: too many values to unpack` | Nombre de variables ≠ nombre d'éléments | Ajuster ou utiliser `*reste` |
| Singleton sans virgule | `(5)` n'est pas un tuple | Écrire `(5,)` |
| Clé de dict avec liste dedans | Tuple non hachable | Convertir en sous-tuples |
| `IndexError` | Indice hors limites | Vérifier `len(t)` ou utiliser une tranche |

---

# 11. Fonctions

---

## 11.1 Introduction

Une **fonction** est un bloc de code réutilisable qui réalise une tâche précise. Elle réduit la répétition, structure le programme et améliore la lisibilité.

```python
def saluer(nom):
    """Affiche un message de salutation."""
    print(f"Bonjour {nom} !")

saluer("Alice")
```

### Syntaxe

```python
def nom_fonction(parametre1, parametre2):
    """Docstring (documentation)."""
    # corps
    return resultat
```

**Convention de nommage** : `snake_case`, verbe d'action (`calculer_total`, `est_valide`).

## 11.2 Paramètres et arguments

```python
def presenter(nom, age=18, *hobbies, ville="Paris", **autres):
    ...
```

| Type | Exemple | Remarque |
| --- | --- | --- |
| **Positionnels** | `f(1, 2)` | Selon l'ordre |
| **Nommés** | `f(b=2, a=1)` | Ordre libre |
| **Valeurs par défaut** | `def f(x, y=10)` | Les paramètres par défaut viennent en dernier |
| **`*args`** | `def f(*args)` | Arguments positionnels variables (tuple) |
| **`**kwargs`** | `def f(**kwargs)` | Arguments nommés variables (dict) |

### Paramètres positionnels seuls et nommés seuls

```python
def f(a, b, /, c, d, *, e, f):
    ...
# a, b : positionnels seulement (avant /)
# c, d : positionnels ou nommés
# e, f : nommés seulement (après *)
```

### Ordre des paramètres

`positionnels → défauts → *args → nommés seuls → **kwargs`

### ⚠️ Piège : valeur par défaut mutable

```python
# ❌ La liste est partagée entre tous les appels
def ajouter(x, liste=[]):
    liste.append(x)
    return liste

# ✅ Utiliser None
def ajouter(x, liste=None):
    if liste is None:
        liste = []
    liste.append(x)
    return liste
```

### Déballage à l'appel

```python
def somme(a, b, c): return a + b + c
print(somme(*[1, 2, 3]))
print(somme(**{"a": 1, "b": 2, "c": 3}))
```

## 11.3 Valeurs de retour

```python
def division(a, b):
    if b == 0:
        return None          # retour anticipé
    return a / b

def min_max(l):
    return min(l), max(l)    # plusieurs valeurs = un tuple

mini, maxi = min_max([3, 1, 4])
```

Une fonction sans `return` renvoie `None`.

## 11.4 Portée et durée de vie

```python
x = 10                     # globale

def f():
    x = 5                  # locale
    print(x)

def g():
    global x               # modifie la globale (à éviter)
    x += 1

def externe():
    n = 0
    def interne():
        nonlocal n         # modifie la variable de la fonction englobante
        n += 1
    interne()
    return n
```

Les variables locales **disparaissent à la fin de l'appel**.

## 11.5 Fonctions anonymes (`lambda`)

```python
carre = lambda x: x ** 2
print(carre(4))             # 16

nombres = [1, 2, 3, 4]
doubles = list(map(lambda x: x * 2, nombres))
personnes.sort(key=lambda p: p["age"])
```

- ✅ À utiliser pour de **petites fonctions jetables** (clés de tri, callbacks).
- ❌ À éviter pour de la logique complexe : préférez `def`.

## 11.6 Fonctions d'ordre supérieur

Une fonction peut être **passée en argument**, **retournée** ou **stockée** : les fonctions sont des objets de première classe.

```python
def appliquer(f, valeur):
    return f(valeur)

print(appliquer(str.upper, "salut"))

def multiplicateur(n):
    def fois(x):            # fermeture (closure)
        return x * n
    return fois

triple = multiplicateur(3)
print(triple(5))            # 15
```

Une **fermeture** (*closure*) conserve l'accès aux variables de la fonction englobante.

### Outils du module `functools`

```python
from functools import partial, reduce, lru_cache, cache

double = partial(pow, 2)          # fixe le 1er argument
@cache                            # mémoïsation (3.9+)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
```

## 11.7 Décorateurs

Un **décorateur** est une fonction qui prend une fonction et en retourne une version modifiée.

```python
import functools, time

def chronometre(fonction):
    @functools.wraps(fonction)         # conserve nom et docstring
    def enveloppe(*args, **kwargs):
        debut = time.perf_counter()
        resultat = fonction(*args, **kwargs)
        print(f"{fonction.__name__} : {time.perf_counter() - debut:.4f} s")
        return resultat
    return enveloppe

@chronometre                            # équivaut à calcul = chronometre(calcul)
def calcul():
    return sum(range(1_000_000))
```

### Décorateur avec paramètres

```python
def repeter(n):
    def decorateur(f):
        @functools.wraps(f)
        def enveloppe(*args, **kwargs):
            for _ in range(n):
                f(*args, **kwargs)
        return enveloppe
    return decorateur

@repeter(3)
def dire_salut():
    print("Salut")
```

Décorateurs intégrés : `@staticmethod`, `@classmethod`, `@property`, `@functools.cache`, `@dataclass`, `@abstractmethod`.

## 11.8 Récursivité

Une fonction **récursive** s'appelle elle-même. Elle exige toujours un **cas de base**.

```python
def factorielle(n):
    if n <= 1:           # cas de base
        return 1
    return n * factorielle(n - 1)

print(factorielle(5))    # 120
```

- La profondeur maximale est limitée (`sys.getrecursionlimit()`, 1000 par défaut).
- Python n'optimise pas la récursion terminale : pour de grandes profondeurs, préférez une **boucle**.
- Utilisez `@cache` pour éviter les recalculs (Fibonacci).

## 11.9 Annotations et typage

```python
def saluer(nom: str, fois: int = 1) -> str:
    return (f"Bonjour {nom} ! " * fois).strip()

print(saluer.__annotations__)
```

Les annotations sont **informatives** : Python ne les applique pas à l'exécution, mais des outils (**mypy**, **pyright**) les vérifient. Voir [section 17](#17-typage-statique).

## 11.10 Docstrings

Une **docstring** est la chaîne de documentation placée juste après la ligne `def` (PEP 257).

```python
def aire_rectangle(largeur: float, hauteur: float) -> float:
    """Calcule l'aire d'un rectangle.

    Args:
        largeur: Largeur du rectangle.
        hauteur: Hauteur du rectangle.

    Returns:
        L'aire (largeur × hauteur).

    Raises:
        ValueError: Si une dimension est négative.
    """
    if largeur < 0 or hauteur < 0:
        raise ValueError("Dimensions négatives")
    return largeur * hauteur

help(aire_rectangle)
print(aire_rectangle.__doc__)
```

## 11.11 Fonctions intégrées essentielles

| Catégorie | Fonctions |
| --- | --- |
| Conversion | `int`, `float`, `str`, `bool`, `list`, `tuple`, `set`, `dict` |
| Séquences | `len`, `range`, `enumerate`, `zip`, `sorted`, `reversed` |
| Mathématiques | `abs`, `round`, `sum`, `min`, `max`, `pow`, `divmod` |
| Logique | `all`, `any`, `callable`, `isinstance`, `issubclass` |
| Entrées/sorties | `print`, `input`, `open` |
| Introspection | `type`, `id`, `dir`, `help`, `vars`, `hasattr`, `getattr`, `setattr` |
| Fonctionnel | `map`, `filter`, `iter`, `next` |
| Caractères | `chr`, `ord`, `repr`, `format`, `ascii` |

## 11.12 Bonnes pratiques

- Une fonction = **une responsabilité**, courte et nommée explicitement.
- Peu de paramètres (idéalement ≤ 4) ; sinon regroupez-les dans un objet.
- Évitez les **effets de bord** et les variables globales.
- Documentez et **typez** les fonctions publiques.
- Ne retournez pas des types différents selon les cas (ex. `str` ou `None` sans l'annoncer).

---

# 12. Itérateurs et générateurs

*(Concept absent de la version originale, ajouté pour compléter le guide.)*

---

## 12.1 Itérables et itérateurs

- Un **itérable** peut être parcouru par `for` (liste, `str`, `dict`, fichier…). Il définit `__iter__()`.
- Un **itérateur** produit les valeurs une à une via `__next__()` et lève `StopIteration` à la fin.

```python
it = iter([10, 20])
print(next(it))     # 10
print(next(it))     # 20
# next(it)          # StopIteration
```

## 12.2 Générateurs

Une fonction contenant `yield` est un **générateur** : elle produit les valeurs **à la demande**, sans tout stocker en mémoire.

```python
def compte_a_rebours(n):
    while n > 0:
        yield n
        n -= 1

for x in compte_a_rebours(3):
    print(x)          # 3, 2, 1
```

### Expressions génératrices

```python
somme = sum(x ** 2 for x in range(1_000_000))   # aucune liste en mémoire
```

### `yield from`

```python
def aplatir(listes):
    for l in listes:
        yield from l
```

### Lecture paresseuse d'un gros fichier

```python
def lignes_non_vides(chemin):
    with open(chemin, encoding="utf-8") as f:
        for ligne in f:
            if ligne.strip():
                yield ligne
```

## 12.3 Le module `itertools`

```python
from itertools import chain, count, islice, product, permutations, combinations, groupby, batched

list(islice(count(1), 5))            # [1, 2, 3, 4, 5]
list(combinations("ABC", 2))         # [('A','B'), ('A','C'), ('B','C')]
list(batched(range(7), 3))           # [(0,1,2), (3,4,5), (6,)]  (3.12+)
```

## 12.4 Créer son propre itérateur

```python
class Compteur:
    def __init__(self, maximum):
        self.maximum = maximum
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= self.maximum:
            raise StopIteration
        self.n += 1
        return self.n
```

> 💡 Dans la plupart des cas, un **générateur** est plus simple qu'une classe itérateur.

---

# 13. Gestion des erreurs

---

## 13.1 Introduction

| Type | Description | Exemple |
| --- | --- | --- |
| **Erreur de syntaxe** | Détectée avant l'exécution | `print("a"` |
| **Exception** | Survient pendant l'exécution | `1 / 0`, `int("abc")` |

## 13.2 `try` / `except`

```python
try:
    nombre = int(input("Nombre : "))
    resultat = 10 / nombre
except ValueError:
    print("Ce n'est pas un nombre.")
except ZeroDivisionError:
    print("Division par zéro impossible.")
except (TypeError, KeyError) as e:      # plusieurs types
    print(f"Erreur : {e}")
```

⚠️ **N'écrivez jamais un `except:` nu** ni `except Exception: pass` sans bonne raison : vous masqueriez des bugs.

## 13.3 `else` et `finally`

```python
try:
    f = open("donnees.txt", encoding="utf-8")
except FileNotFoundError:
    print("Fichier introuvable")
else:
    print("Lecture réussie")     # exécuté si aucune exception
    f.close()
finally:
    print("Toujours exécuté")    # nettoyage garanti
```

## 13.4 Exploiter l'objet exception

```python
try:
    int("abc")
except ValueError as e:
    print(type(e).__name__)   # ValueError
    print(e)                  # invalid literal for int()...
    print(e.args)
```

## 13.5 Lever des exceptions

```python
def racine(x):
    if x < 0:
        raise ValueError("x doit être positif")
    return x ** 0.5
```

## 13.6 Exceptions personnalisées

```python
class ErreurMetier(Exception):
    """Classe de base des erreurs de l'application."""

class SoldeInsuffisant(ErreurMetier):
    def __init__(self, solde, montant):
        super().__init__(f"Solde {solde} insuffisant pour retirer {montant}")
        self.solde = solde
        self.montant = montant
```

Dérivez toujours de `Exception` (jamais de `BaseException`) et terminez le nom par `Error` pour les erreurs.

## 13.7 Chaînage et relance

```python
try:
    int("x")
except ValueError as e:
    raise RuntimeError("Lecture de configuration impossible") from e   # chaînage

try:
    ...
except Exception:
    print("Journalisation")
    raise                  # relance l'exception d'origine
```

## 13.8 Hiérarchie des exceptions

```text
BaseException
 ├── KeyboardInterrupt, SystemExit, GeneratorExit
 └── Exception
      ├── ArithmeticError (ZeroDivisionError, OverflowError)
      ├── LookupError (IndexError, KeyError)
      ├── OSError (FileNotFoundError, PermissionError, TimeoutError)
      ├── ValueError (UnicodeError)
      ├── TypeError
      ├── AttributeError, NameError, ImportError
      ├── RuntimeError (RecursionError, NotImplementedError)
      └── StopIteration, AssertionError…
```

Un `except` attrape l'exception **et ses sous-classes** : placez les plus spécifiques en premier.

## 13.9 Groupes d'exceptions et `except*` *(Python 3.11+)*

Utile pour la concurrence : plusieurs erreurs simultanées.

```python
try:
    raise ExceptionGroup("Erreurs multiples", [ValueError("a"), TypeError("b")])
except* ValueError as eg:
    print("ValueError traitées :", eg.exceptions)
except* TypeError as eg:
    print("TypeError traitées :", eg.exceptions)
```

Python 3.11 permet aussi d'ajouter du contexte : `e.add_note("détail utile")`.

## 13.10 Assertions

```python
def moyenne(notes):
    assert len(notes) > 0, "La liste de notes ne doit pas être vide"
    return sum(notes) / len(notes)
```

Les `assert` servent à **vérifier des hypothèses de développement** ; ils sont **désactivés avec `python -O`**. Ne les utilisez pas pour valider des entrées utilisateur.

## 13.11 Journalisation des erreurs

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
)

try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Erreur de calcul")     # inclut la trace complète
```

Niveaux : `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.

## 13.12 Gestionnaires de contexte et nettoyage

```python
with open("fichier.txt", encoding="utf-8") as f:
    contenu = f.read()
# fichier fermé automatiquement, même en cas d'erreur
```

Créer son propre gestionnaire :

```python
from contextlib import contextmanager, suppress

@contextmanager
def chronometrer(nom):
    import time
    debut = time.perf_counter()
    try:
        yield
    finally:
        print(f"{nom} : {time.perf_counter() - debut:.3f} s")

with chronometrer("calcul"):
    sum(range(10_000_000))

with suppress(FileNotFoundError):       # ignore proprement une erreur précise
    import os; os.remove("temp.txt")
```

## 13.13 Cas pratiques

### Fichiers

```python
try:
    with open("donnees.txt", encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError:
    print("Fichier introuvable")
except PermissionError:
    print("Accès refusé")
```

### Saisie utilisateur

```python
while True:
    try:
        age = int(input("Âge : "))
        if age < 0:
            raise ValueError("L'âge ne peut pas être négatif")
        break
    except ValueError as e:
        print(f"Entrée invalide : {e}")
```

### Requêtes web / API

```python
import requests

try:
    reponse = requests.get("https://api.exemple.com/data", timeout=5)
    reponse.raise_for_status()
    donnees = reponse.json()
except requests.exceptions.Timeout:
    print("Délai dépassé")
except requests.exceptions.HTTPError as e:
    print(f"Erreur HTTP : {e}")
except requests.exceptions.RequestException as e:
    print(f"Erreur réseau : {e}")
```

(Pensez à toujours définir un `timeout`.)

## 13.14 Bonnes pratiques

- Attrapez des exceptions **précises**, au bon niveau.
- Gardez le bloc `try` **le plus court possible**.
- Ne **supprimez pas** les erreurs silencieusement.
- Préférez **`with`** à `try/finally` pour libérer les ressources.
- Fournissez des **messages utiles** et journalisez avec `logging`.
- Python favorise **EAFP** (*« mieux vaut demander pardon que la permission »*) plutôt que LBYL (*« look before you leap »*).

```python
# EAFP (pythonique)
try:
    valeur = d["cle"]
except KeyError:
    valeur = None
```

---

# 14. Gestion des fichiers

---

## 14.1 Introduction

Un programme peut **lire** et **écrire** des fichiers pour conserver des données. Il existe deux grandes familles :

| Type | Contenu | Mode |
| --- | --- | --- |
| **Texte** | Caractères (`.txt`, `.csv`, `.json`, `.md`) | `"r"`, `"w"`… |
| **Binaire** | Octets (images, audio, `.pdf`, `.zip`) | `"rb"`, `"wb"`… |

## 14.2 Ouvrir et fermer un fichier

```python
# ✅ Méthode recommandée : with (fermeture automatique)
with open("notes.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
```

| Mode | Signification |
| --- | --- |
| `"r"` | Lecture (défaut) ; erreur si le fichier n'existe pas |
| `"w"` | Écriture ; **écrase** le contenu existant |
| `"a"` | Ajout en fin de fichier |
| `"x"` | Création exclusive ; erreur si le fichier existe |
| `"r+"` | Lecture et écriture |
| `"b"` | Mode binaire (`"rb"`, `"wb"`) |
| `"t"` | Mode texte (défaut) |

> ⚠️ **Précisez toujours `encoding="utf-8"`** en mode texte pour éviter les problèmes selon les systèmes. (Python 3.15 définit UTF-8 comme encodage par défaut.)

## 14.3 Lire un fichier

```python
with open("notes.txt", encoding="utf-8") as f:
    tout = f.read()          # tout le contenu en une chaîne
    f.seek(0)
    une_ligne = f.readline() # une ligne
    f.seek(0)
    lignes = f.readlines()   # liste de lignes

# ✅ Le plus économe en mémoire : parcours ligne par ligne
with open("gros.txt", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.rstrip("\n"))
```

## 14.4 Écrire dans un fichier

```python
with open("sortie.txt", "w", encoding="utf-8") as f:
    f.write("Ligne 1\n")
    f.writelines(["Ligne 2\n", "Ligne 3\n"])
    print("Ligne 4", file=f)

with open("sortie.txt", "a", encoding="utf-8") as f:    # ajout
    f.write("Ligne ajoutée\n")
```

`write()` n'ajoute **pas** de retour à la ligne automatiquement.

## 14.5 Chemins de fichiers avec `pathlib`

Le module **`pathlib`** (orienté objet) est la méthode moderne, préférable à `os.path`.

```python
from pathlib import Path

p = Path("donnees") / "rapport.txt"     # l'opérateur / assemble les chemins
print(p.name)          # rapport.txt
print(p.stem)          # rapport
print(p.suffix)        # .txt
print(p.parent)        # donnees
print(p.resolve())     # chemin absolu
print(p.exists(), p.is_file(), p.is_dir())

texte = p.read_text(encoding="utf-8")
p.write_text("Bonjour", encoding="utf-8")

Path.home()            # dossier personnel
Path.cwd()             # dossier courant
```

## 14.6 Opérations sur fichiers et dossiers

```python
from pathlib import Path
import shutil

Path("nouveau").mkdir(parents=True, exist_ok=True)
Path("a.txt").rename("b.txt")
Path("b.txt").unlink(missing_ok=True)       # supprimer un fichier
Path("nouveau").rmdir()                     # supprimer un dossier vide

for f in Path(".").glob("*.py"):            # lister
    print(f)
for f in Path(".").rglob("*.md"):           # récursif
    print(f)

shutil.copy("src.txt", "dst.txt")
shutil.copytree("dossier", "copie")
shutil.rmtree("copie")                      # supprime un dossier non vide
shutil.move("a", "b")
```

Équivalents `os` : `os.listdir()`, `os.remove()`, `os.mkdir()`, `os.path.join()`, `os.walk()`.

## 14.7 Fichiers binaires

```python
with open("image.png", "rb") as f:
    octets = f.read()

with open("copie.png", "wb") as f:
    f.write(octets)

# Lecture par blocs (gros fichiers)
with open("gros.bin", "rb") as f:
    while bloc := f.read(8192):
        traiter(bloc)
```

## 14.8 Position dans le fichier (curseur)

```python
with open("notes.txt", "rb") as f:
    f.read(5)
    print(f.tell())       # position actuelle : 5
    f.seek(0)             # retour au début
    f.seek(0, 2)          # tout à la fin
```

## 14.9 Fichiers CSV

```python
import csv

with open("personnes.csv", newline="", encoding="utf-8") as f:
    for ligne in csv.DictReader(f):
        print(ligne["nom"], ligne["age"])

with open("sortie.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nom", "age"])
    writer.writeheader()
    writer.writerow({"nom": "Alice", "age": 30})
```

Pour de gros volumes : **pandas** ou **polars**.

## 14.10 Fichiers JSON

```python
import json
from pathlib import Path

donnees = {"nom": "Alice", "langues": ["fr", "en"]}

Path("data.json").write_text(
    json.dumps(donnees, indent=2, ensure_ascii=False), encoding="utf-8"
)
lu = json.loads(Path("data.json").read_text(encoding="utf-8"))
```

## 14.11 Fichiers de configuration TOML *(3.11+)*

```python
import tomllib

with open("pyproject.toml", "rb") as f:     # ouvrir en binaire
    config = tomllib.load(f)
```

## 14.12 Sérialisation avec `pickle`

```python
import pickle

with open("objet.pkl", "wb") as f:
    pickle.dump({"a": [1, 2, 3]}, f)
with open("objet.pkl", "rb") as f:
    obj = pickle.load(f)
```

> 🔒 **Sécurité** : **ne chargez jamais** un fichier pickle provenant d'une source non fiable : il peut exécuter du code arbitraire. Préférez **JSON** pour l'échange de données.

## 14.13 Compression et archives

```python
import zipfile, gzip, shutil

with zipfile.ZipFile("archive.zip", "w", zipfile.ZIP_DEFLATED) as z:
    z.write("a.txt")
with zipfile.ZipFile("archive.zip") as z:
    z.extractall("sortie")

with gzip.open("donnees.txt.gz", "wt", encoding="utf-8") as f:
    f.write("texte compressé")

shutil.make_archive("sauvegarde", "zip", "dossier")
```

Autres formats : `tarfile`, `bz2`, `lzma`, et `compression.zstd` (Zstandard, Python 3.14+).

## 14.14 Permissions et métadonnées

```python
import os, stat
from pathlib import Path

info = Path("a.txt").stat()
print(info.st_size, info.st_mtime)    # taille en octets, date de modification

os.chmod("script.sh", stat.S_IRWXU)    # rwx pour le propriétaire
os.access("a.txt", os.R_OK)            # accessible en lecture ?
```

## 14.15 Exceptions courantes

| Exception | Cause |
| --- | --- |
| `FileNotFoundError` | Fichier ou dossier inexistant |
| `PermissionError` | Droits insuffisants |
| `IsADirectoryError` | Un dossier est attendu à la place d'un fichier |
| `FileExistsError` | Le fichier existe déjà (mode `"x"`, `mkdir`) |
| `UnicodeDecodeError` | Mauvais encodage |

## 14.16 Sujets avancés

- **Tampon** : `open(..., buffering=...)` ; `f.flush()` force l'écriture.
- **Fichiers temporaires** : `tempfile.NamedTemporaryFile()`, `tempfile.TemporaryDirectory()`.
- **Fichiers mappés en mémoire** : module `mmap`.
- **Écriture atomique** : écrire dans un fichier temporaire puis `os.replace()`.
- **Fichiers volumineux** : lire par blocs ou ligne par ligne.

---

# 15. Modules, paquets et environnements virtuels

*(Section ajoutée : elle manquait dans la version originale alors qu'elle est indispensable.)*

---

## 15.1 Modules

Un **module** est un fichier `.py` réutilisable.

```python
# maths_utils.py
PI = 3.14159

def aire_cercle(r):
    return PI * r ** 2
```

```python
# main.py
import maths_utils
from maths_utils import aire_cercle
from maths_utils import aire_cercle as aire        # alias
import math as m

print(maths_utils.aire_cercle(2))
```

⚠️ Évitez `from module import *` (pollution de l'espace de noms).

### Le point d'entrée `__main__`

```python
def main():
    print("Programme principal")

if __name__ == "__main__":     # vrai seulement si le fichier est exécuté directement
    main()
```

## 15.2 Paquets

Un **paquet** (*package*) est un dossier de modules. Depuis Python 3.3, le fichier `__init__.py` est facultatif mais reste recommandé.

```text
monprojet/
├── pyproject.toml
├── src/
│   └── monpaquet/
│       ├── __init__.py
│       ├── outils.py
│       └── sous_paquet/
│           └── __init__.py
└── tests/
    └── test_outils.py
```

```python
from monpaquet.outils import fonction
from . import outils            # import relatif
```

## 15.3 Recherche des modules

Python cherche dans l'ordre : modules intégrés → dossier courant → `sys.path` (dont `PYTHONPATH` et `site-packages`).

```python
import sys
print(sys.path)
```

## 15.4 `pip` : installer des paquets

```bash
python -m pip install requests
python -m pip install "requests>=2.31"
python -m pip install -r requirements.txt
python -m pip list
python -m pip freeze > requirements.txt
python -m pip uninstall requests
```

Les paquets viennent de **PyPI** (<https://pypi.org>). Préférez `python -m pip` à `pip` seul pour être sûr d'utiliser le bon interpréteur.

## 15.5 Environnements virtuels

Un **environnement virtuel** isole les dépendances de chaque projet. **Utilisez-en un systématiquement.**

```bash
python -m venv .venv                 # création

source .venv/bin/activate            # Linux / macOS
.venv\Scripts\activate               # Windows (cmd / PowerShell)

deactivate                           # désactivation
```

> Ajoutez `.venv/` à votre `.gitignore`.

## 15.6 Outils modernes de gestion de projet

| Outil | Rôle |
| --- | --- |
| **uv** | Gestionnaire tout-en-un très rapide : versions de Python, environnements, dépendances, verrouillage |
| **Poetry / PDM / Hatch** | Gestion de projets et publication |
| **pipx** | Installer des outils en ligne de commande isolés |

```bash
# Exemple avec uv
uv init mon_projet
cd mon_projet
uv add requests
uv run python main.py
```

## 15.7 `pyproject.toml`

Fichier standard de configuration d'un projet (PEP 517/518/621) :

```toml
[project]
name = "mon-projet"
version = "0.1.0"
description = "Exemple de projet"
requires-python = ">=3.10"
dependencies = [
    "requests>=2.31",
]

[tool.ruff]
line-length = 88

[tool.pytest.ini_options]
testpaths = ["tests"]
```

## 15.8 Bibliothèque standard : modules incontournables

| Module | Utilité |
| --- | --- |
| `pathlib`, `shutil`, `os`, `sys` | Système et fichiers |
| `json`, `csv`, `tomllib`, `sqlite3` | Données |
| `datetime`, `zoneinfo`, `time` | Dates et temps |
| `re` | Expressions régulières |
| `collections`, `itertools`, `functools` | Outils de structures et fonctions |
| `argparse`, `logging` | Programmes en ligne de commande, journalisation |
| `random`, `statistics`, `math`, `decimal` | Nombres |
| `subprocess`, `threading`, `multiprocessing`, `asyncio` | Processus et concurrence |
| `unittest`, `doctest` | Tests |
| `dataclasses`, `enum`, `typing` | Modélisation |

---

# 16. Programmation orientée objet

---

## 16.1 Concepts fondamentaux

| Concept | Description |
| --- | --- |
| **Classe** | Plan (modèle) qui décrit des attributs et des comportements |
| **Objet / instance** | Réalisation concrète d'une classe |
| **Attribut** | Donnée associée à un objet ou à une classe |
| **Méthode** | Fonction définie dans une classe |
| **Encapsulation** | Regrouper et protéger données et comportements |
| **Héritage** | Une classe réutilise et étend une autre |
| **Polymorphisme** | Des objets différents répondent à la même interface |
| **Abstraction** | Exposer l'essentiel, masquer les détails |

### Définir une classe

```python
class Chien:
    espece = "Canis familiaris"          # attribut de classe (partagé)

    def __init__(self, nom, age):         # constructeur
        self.nom = nom                    # attributs d'instance
        self.age = age

    def aboyer(self):                     # méthode d'instance
        return f"{self.nom} dit : Ouaf !"

    def __repr__(self):                   # représentation pour développeurs
        return f"Chien(nom={self.nom!r}, age={self.age})"

    def __str__(self):                    # représentation pour utilisateurs
        return f"{self.nom} ({self.age} ans)"

rex = Chien("Rex", 3)
print(rex.aboyer())
print(rex, repr(rex))
```

`self` désigne l'instance courante : c'est le premier paramètre de toute méthode d'instance.

## 16.2 Encapsulation et propriétés

Python n'a pas de visibilité stricte ; on utilise des **conventions** :

| Notation | Signification |
| --- | --- |
| `attribut` | Public |
| `_attribut` | Protégé / usage interne (convention) |
| `__attribut` | « Privé » (le nom est transformé : *name mangling*) |

Les **propriétés** (`@property`) contrôlent l'accès aux attributs :

```python
class Compte:
    def __init__(self, solde=0):
        self._solde = solde

    @property
    def solde(self):                      # lecture
        return self._solde

    @solde.setter
    def solde(self, valeur):              # écriture avec validation
        if valeur < 0:
            raise ValueError("Solde négatif interdit")
        self._solde = valeur

c = Compte(100)
c.solde = 150
print(c.solde)
```

## 16.3 Méthodes de classe et statiques

```python
class Date:
    def __init__(self, j, m, a):
        self.j, self.m, self.a = j, m, a

    @classmethod
    def depuis_texte(cls, texte):          # constructeur alternatif
        j, m, a = map(int, texte.split("/"))
        return cls(j, m, a)

    @staticmethod
    def est_bissextile(annee):             # utilitaire sans self ni cls
        return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)

d = Date.depuis_texte("11/10/2026")
print(Date.est_bissextile(2028))
```

## 16.4 Héritage

```python
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        raise NotImplementedError

class Chat(Animal):
    def __init__(self, nom, couleur):
        super().__init__(nom)              # appel du parent
        self.couleur = couleur

    def parler(self):                      # redéfinition (override)
        return "Miaou"

print(isinstance(Chat("Mimi", "noir"), Animal))   # True
print(issubclass(Chat, Animal))                   # True
```

### Héritage multiple et MRO

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)    # ordre de résolution des méthodes (algorithme C3)
```

`super()` suit le **MRO**. Préférez la **composition** (« a un ») à l'héritage (« est un ») quand c'est possible.

### Mixins

```python
class JsonMixin:
    def en_json(self):
        import json
        return json.dumps(self.__dict__)

class Utilisateur(JsonMixin):
    def __init__(self, nom):
        self.nom = nom
```

## 16.5 Polymorphisme et *duck typing*

> « S'il marche comme un canard et cancane comme un canard, c'est un canard. »

```python
class Chien:
    def parler(self): return "Ouaf"

class Robot:
    def parler(self): return "Bip"

for etre in (Chien(), Robot()):
    print(etre.parler())          # aucune parenté nécessaire
```

## 16.6 Méthodes spéciales (« dunder »)

| Catégorie | Méthodes |
| --- | --- |
| Création / représentation | `__init__`, `__new__`, `__repr__`, `__str__`, `__format__` |
| Comparaison | `__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__hash__` |
| Arithmétique | `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__neg__` |
| Conteneurs | `__len__`, `__getitem__`, `__setitem__`, `__contains__`, `__iter__` |
| Appelable | `__call__` |
| Contexte | `__enter__`, `__exit__` |
| Attributs | `__getattr__`, `__setattr__`, `__getattribute__` |

```python
class Panier:
    def __init__(self):
        self.articles = []

    def __len__(self):
        return len(self.articles)

    def __getitem__(self, i):
        return self.articles[i]

    def __iter__(self):
        return iter(self.articles)

    def __contains__(self, article):
        return article in self.articles
```

### Gestionnaire de contexte personnalisé

```python
class Connexion:
    def __enter__(self):
        print("Ouverture")
        return self
    def __exit__(self, type_exc, valeur, trace):
        print("Fermeture")
        return False      # ne pas supprimer l'exception
```

## 16.7 Classes de données : `dataclass`

Évitent d'écrire à la main `__init__`, `__repr__` et `__eq__` :

```python
from dataclasses import dataclass, field

@dataclass(order=True, frozen=False, slots=True)
class Produit:
    nom: str
    prix: float
    tags: list[str] = field(default_factory=list)

    def prix_ttc(self, tva=0.2):
        return self.prix * (1 + tva)

p = Produit("Livre", 12.5)
print(p)                         # Produit(nom='Livre', prix=12.5, tags=[])
```

| Option | Effet |
| --- | --- |
| `frozen=True` | Instances immuables et hachables |
| `order=True` | Génère les comparaisons `<`, `>`… |
| `slots=True` | Économie de mémoire, accès plus rapide (3.10+) |
| `kw_only=True` | Arguments nommés obligatoires (3.10+) |

Alternatives : `NamedTuple`, et **Pydantic** / **attrs** pour la validation.

## 16.8 Énumérations

```python
from enum import Enum, auto, IntEnum, StrEnum

class Couleur(Enum):
    ROUGE = auto()
    VERT = auto()

class Statut(StrEnum):         # 3.11+
    ACTIF = "actif"
    INACTIF = "inactif"

print(Couleur.ROUGE.name, Statut.ACTIF.value)
```

## 16.9 Classes abstraites et protocoles

```python
from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def aire(self) -> float: ...

class Carre(Forme):
    def __init__(self, c): self.c = c
    def aire(self): return self.c ** 2

# Forme()   # ❌ TypeError : classe abstraite
```

**Protocole** (typage structurel, sans héritage) :

```python
from typing import Protocol

class Fermable(Protocol):
    def close(self) -> None: ...

def fermer(ressource: Fermable) -> None:
    ressource.close()
```

## 16.10 `__slots__` et gestion de la mémoire

```python
class Point:
    __slots__ = ("x", "y")      # pas de __dict__ : moins de mémoire
    def __init__(self, x, y):
        self.x, self.y = x, y
```

## 16.11 Descripteurs

Un **descripteur** est un objet qui définit `__get__`, `__set__` ou `__delete__` ; c'est le mécanisme qui sous-tend `property`, les méthodes et `classmethod`.

```python
class Positif:
    def __set_name__(self, owner, nom):
        self.nom = "_" + nom
    def __get__(self, obj, type=None):
        return getattr(obj, self.nom)
    def __set__(self, obj, valeur):
        if valeur <= 0:
            raise ValueError("Doit être positif")
        setattr(obj, self.nom, valeur)

class Article:
    prix = Positif()
    def __init__(self, prix):
        self.prix = prix
```

## 16.12 Métaclasses et réflexion (avancé)

Une **métaclasse** est « la classe d'une classe » : la métaclasse par défaut est `type`.

```python
Dynamique = type("Dynamique", (), {"x": 5, "montrer": lambda self: print(self.x)})
Dynamique().montrer()      # 5

class MetaJournal(type):
    def __new__(mcs, nom, bases, attrs):
        print(f"Création de la classe {nom}")
        return super().__new__(mcs, nom, bases, attrs)

class Base(metaclass=MetaJournal):
    pass
```

Pour de nombreux cas (enregistrement, validation), **`__init_subclass__`** est plus simple :

```python
class Plugin:
    registre = []
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin.registre.append(cls)
```

> 🧠 Les métaclasses sont rarement nécessaires ; utilisez-les avec parcimonie.

### Introspection

```python
type(obj)                  isinstance(obj, cls)      issubclass(a, b)
dir(obj)                   vars(obj) / obj.__dict__  hasattr / getattr / setattr
id(obj)                    inspect.getmembers(obj)
```

## 16.13 Principes et bonnes pratiques

| Principe | Idée |
| --- | --- |
| **SOLID** | Responsabilité unique, ouvert/fermé, substitution de Liskov, ségrégation des interfaces, inversion des dépendances |
| **DRY** | *Don't Repeat Yourself* |
| **KISS** | Restez simple |
| **Composition > héritage** | Assemblez des objets plutôt que d'empiler les classes |
| **Programmer vers des interfaces** | Utilisez protocoles / classes abstraites |

- Classes **petites et cohérentes**, noms explicites.
- Toujours définir `__repr__`.
- Si vous redéfinissez `__eq__`, définissez aussi `__hash__` (ou rendez l'objet non hachable).
- Évitez les attributs publics modifiables sans validation : utilisez des propriétés.

## 16.14 Patrons de conception appliqués

### Singleton (via un module)

En Python, un **module** est déjà un singleton : une instance créée au niveau du module est partagée par tous les imports.

### Fabrique

```python
class Chien:  ...
class Chat:   ...

def creer_animal(type_):
    return {"chien": Chien, "chat": Chat}[type_]()
```

### Stratégie (avec des fonctions)

```python
def remise_fidelite(prix): return prix * 0.9
def remise_aucune(prix):  return prix

def total(prix, strategie=remise_aucune):
    return strategie(prix)
```

### Observateur

```python
class Evenement:
    def __init__(self):
        self._abonnes = []
    def abonner(self, fonction):
        self._abonnes.append(fonction)
    def emettre(self, *args):
        for f in self._abonnes:
            f(*args)
```

## 16.15 Exemple complet

```python
from dataclasses import dataclass, field

class SoldeInsuffisant(Exception):
    pass

@dataclass
class Compte:
    titulaire: str
    solde: float = 0.0
    historique: list[tuple[str, float]] = field(default_factory=list)

    def deposer(self, montant: float) -> None:
        if montant <= 0:
            raise ValueError("Montant invalide")
        self.solde += montant
        self.historique.append(("dépôt", montant))

    def retirer(self, montant: float) -> None:
        if montant > self.solde:
            raise SoldeInsuffisant(f"Solde : {self.solde}")
        self.solde -= montant
        self.historique.append(("retrait", montant))

c = Compte("Alice")
c.deposer(100)
c.retirer(30)
print(c)
```

---

# 17. Typage statique

*(Section ajoutée et mise à jour : le typage est devenu central en Python moderne.)*

---

## 17.1 Annotations de types

```python
nom: str = "Alice"
age: int = 30
prix: float = 9.99
actif: bool = True

def additionner(a: int, b: int) -> int:
    return a + b
```

Python **n'applique pas** ces annotations à l'exécution : elles servent aux **vérificateurs de types** (**mypy**, **pyright**, **ty**, **pyrefly**) et aux éditeurs.

## 17.2 Syntaxe moderne (Python 3.9 / 3.10+)

Les anciens alias `List`, `Dict`, `Optional`, `Union` du module `typing` sont **dépréciés** au profit de la syntaxe native :

| Ancien style | Style moderne |
| --- | --- |
| `List[int]` | `list[int]` |
| `Dict[str, int]` | `dict[str, int]` |
| `Tuple[int, str]` | `tuple[int, str]` |
| `Optional[str]` | `str \| None` |
| `Union[int, str]` | `int \| str` |

```python
def trouver(nom: str, liste: list[str]) -> int | None:
    return liste.index(nom) if nom in liste else None
```

## 17.3 Types courants

```python
from typing import Any, Callable, Iterable, Literal, TypedDict, Final, Self
from collections.abc import Sequence, Mapping

def appliquer(f: Callable[[int], int], valeurs: Iterable[int]) -> list[int]:
    return [f(v) for v in valeurs]

Mode = Literal["lecture", "ecriture"]

class Utilisateur(TypedDict):
    nom: str
    age: int
```

## 17.4 Génériques et paramètres de type *(Python 3.12+)*

```python
# Nouvelle syntaxe (PEP 695)
def premier[T](elements: list[T]) -> T:
    return elements[0]

class Pile[T]:
    def __init__(self) -> None:
        self._items: list[T] = []
    def empiler(self, x: T) -> None:
        self._items.append(x)

type Matrice = list[list[float]]     # alias de type avec l'instruction `type`
```

## 17.5 Évaluation différée des annotations *(Python 3.14)*

Depuis Python 3.14 (PEP 649/749), les annotations sont **évaluées à la demande** : on peut référencer une classe avant sa définition sans guillemets ni `from __future__ import annotations`.

```python
class Noeud:
    def suivant(self) -> Noeud | None:    # fonctionne en 3.14+
        ...
```

Utilisez `annotationlib` pour les inspecter.

## 17.6 Vérifier les types

```bash
pip install mypy
mypy mon_script.py
```

---

# 18. Programmation asynchrone et concurrence

*(Section ajoutée.)*

---

## 18.1 Choisir le bon modèle

| Modèle | Quand l'utiliser | Outil |
| --- | --- | --- |
| **`asyncio`** | Nombreuses opérations d'**E/S** (réseau, API) | `async` / `await` |
| **Threads** | E/S bloquantes, bibliothèques non asynchrones | `threading`, `ThreadPoolExecutor` |
| **Processus** | Calcul **intensif CPU** | `multiprocessing`, `ProcessPoolExecutor` |

## 18.2 `asyncio`

```python
import asyncio

async def telecharger(nom, delai):
    await asyncio.sleep(delai)         # opération non bloquante
    return f"{nom} terminé"

async def main():
    resultats = await asyncio.gather(
        telecharger("A", 1),
        telecharger("B", 2),
    )
    print(resultats)

asyncio.run(main())                    # ~2 s au lieu de 3 s
```

### `TaskGroup` *(3.11+)*

```python
async def main():
    async with asyncio.TaskGroup() as groupe:
        t1 = groupe.create_task(telecharger("A", 1))
        t2 = groupe.create_task(telecharger("B", 2))
    print(t1.result(), t2.result())
```

## 18.3 Threads et processus

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

with ThreadPoolExecutor(max_workers=4) as pool:
    resultats = list(pool.map(telecharger_url, urls))

with ProcessPoolExecutor() as pool:
    resultats = list(pool.map(calcul_lourd, donnees))
```

## 18.4 Le GIL et Python sans GIL

Le **GIL** (*Global Interpreter Lock*) empêche plusieurs threads d'exécuter du bytecode Python simultanément dans CPython. Pour les calculs CPU, on utilisait donc les processus.

- **Python 3.13** : première version **expérimentale sans GIL** (*free-threaded*, `python3.13t`).
- **Python 3.14** : le mode *free-threaded* est **officiellement supporté** (PEP 779), bien que non activé par défaut.
- **Python 3.14** : `concurrent.interpreters` permet d'utiliser plusieurs **sous-interpréteurs** isolés dans un même processus.

---

# 19. Tests et qualité du code

*(Section ajoutée.)*

---

## 19.1 Tests avec `pytest`

```python
# calcul.py
def additionner(a, b):
    return a + b
```

```python
# tests/test_calcul.py
import pytest
from calcul import additionner

def test_addition():
    assert additionner(2, 3) == 5

@pytest.mark.parametrize("a, b, attendu", [(1, 1, 2), (0, 0, 0), (-1, 1, 0)])
def test_cas_multiples(a, b, attendu):
    assert additionner(a, b) == attendu

def test_erreur():
    with pytest.raises(TypeError):
        additionner("a", 1)
```

```bash
pip install pytest
pytest -v
```

Le module intégré **`unittest`** et **`doctest`** sont aussi disponibles.

## 19.2 Qualité du code

| Outil | Rôle |
| --- | --- |
| **Ruff** | Lint + formatage (remplace Flake8, isort, Black) |
| **mypy / pyright** | Vérification de types |
| **pytest-cov** | Couverture de tests |
| **pre-commit** | Exécute les vérifications avant chaque commit |

## 19.3 Déboguer

```python
breakpoint()      # lance le débogueur pdb à cet endroit
```

Commandes `pdb` : `n` (suivant), `s` (entrer), `c` (continuer), `p var` (afficher), `l` (code), `q` (quitter). Les éditeurs (VS Code, PyCharm) proposent un débogueur graphique.

---

# 20. Aller plus loin

---

## 20.1 Parcours d'apprentissage suggéré

1. Maîtriser les **bases** (sections 1 à 6).
2. Manipuler les **structures de données** (7 à 10).
3. Écrire des **fonctions** propres et utiliser les **générateurs** (11–12).
4. Gérer **erreurs**, **fichiers** et **modules** (13–15).
5. Appliquer la **POO**, le **typage** et les **tests** (16–19).
6. Choisir une **spécialisation** : web (Django, FastAPI), données (Pandas, NumPy), IA (PyTorch), automatisation (Selenium, Playwright).

## 20.2 Résumé des nouveautés récentes de Python

| Version | À retenir |
| --- | --- |
| 3.8 | Opérateur `:=`, `/` dans les paramètres, `f"{x=}"` |
| 3.9 | Opérateur `\|` sur les `dict`, `list[int]`, `removeprefix` |
| 3.10 | `match`/`case`, `X \| Y`, messages d'erreur améliorés |
| 3.11 | `except*`, `tomllib`, plus rapide |
| 3.12 | Syntaxe générique `def f[T]()`, `type`, `itertools.batched` |
| 3.13 | Nouveau REPL, mode sans GIL (expérimental), JIT (expérimental) |
| 3.14 | t-strings, annotations différées, *free-threading* supporté, `compression.zstd` |
| 3.15 | Voir *Quoi de neuf dans Python 3.15* sur [docs.python.org](https://docs.python.org/3/whatsnew/) |

## 20.3 Ressources

- 📘 Documentation : <https://docs.python.org/fr/3/>
- 🎓 Tutoriel officiel : <https://docs.python.org/fr/3/tutorial/>
- 📜 Guide de style PEP 8 : <https://peps.python.org/pep-0008/>
- 💬 Forum officiel : <https://discuss.python.org>
- 📦 Index des paquets : <https://pypi.org>

---

<div align="center">

*Bon code ! 🐍*

</div>
