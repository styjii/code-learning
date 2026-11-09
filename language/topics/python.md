# Python — Cours complet

*Du premier `print()` à la programmation orientée objet moderne — rédigé pour Python 3.14 / 3.15 (octobre 2026)*

## Comment lire ce cours

Ce cours suit le plan en 20 chapitres. Chaque chapitre développe les notions dans l'ordre : définitions, fonctionnement, exemples commentés, pièges fréquents, bonnes pratiques, puis une synthèse « À retenir ». Les exemples sont courts : tapez-les vous-même dans un terminal ou un éditeur plutôt que de les lire passivement, et modifiez-les pour observer ce qui change. Dans les blocs de code, un commentaire `# →` indique le résultat affiché.

Aucun prérequis n'est nécessaire. La progression est la suivante : chapitres 1 à 6 (les bases du langage), 7 à 10 (les structures de données), 11 et 12 (fonctions, itérateurs, générateurs), 13 à 15 (robustesse, fichiers, organisation du code), 16 à 19 (programmation professionnelle : objets, typage, concurrence, tests) et 20 (la suite du parcours).

## 1. Introduction

**Objectifs du chapitre** : comprendre ce qu'est Python et comment il fonctionne, connaître son histoire et ses usages, installer un environnement de travail, exécuter un premier programme et savoir chercher de l'aide.

### 1.1 Qu'est-ce que Python ?

Python est un langage de programmation **de haut niveau**, **interprété**, **polyvalent** et **multi-paradigme**, créé par Guido van Rossum. Chacun de ces termes mérite une définition précise.

- **Langage de programmation** : ensemble de règles d'écriture (la *syntaxe*) et de règles de signification (la *sémantique*) qui permettent de décrire à un ordinateur une suite d'opérations à effectuer sur des données. Un programme est la traduction d'un *algorithme*, c'est-à-dire d'une méthode de résolution décrite pas à pas.
- **Haut niveau** : le langage masque les détails du matériel (registres du processeur, adresses mémoire, allocation manuelle). On exprime *ce que l'on veut faire* plutôt que *comment la machine doit le faire*. Le contraire est un langage de bas niveau, comme l'assembleur, ou, à un degré moindre, le C.
- **Interprété** : le code n'est pas transformé à l'avance en un exécutable propre à une machine ; un programme appelé *interpréteur* le lit et l'exécute. La réalité est plus fine (voir 1.8) : le code est d'abord compilé en *bytecode*, que l'interpréteur exécute ensuite.
- **Polyvalent** (généraliste) : Python n'est pas limité à un domaine. On l'emploie pour le web, les données, l'intelligence artificielle, l'automatisation, les scripts système, l'enseignement, etc.
- **Multi-paradigme** : un *paradigme* est une façon d'organiser un programme. Python permet la programmation **impérative / procédurale** (suites d'instructions et de fonctions), **orientée objet** (classes et objets) et **fonctionnelle** (fonctions comme valeurs, `lambda`, `map`, `filter`, compréhensions).

#### Typage dynamique et typage fort

Ces deux notions sont souvent confondues. Elles décrivent deux choses différentes.

- **Typage dynamique** : le type est vérifié à l'*exécution* et il est attaché à la **valeur** (à l'objet), pas au nom de la variable. Une même variable peut désigner successivement un entier puis une chaîne.
- **Typage fort** : le langage refuse de mélanger silencieusement des types incompatibles. En Python, `'1' + 2` provoque une `TypeError` au lieu de produire un résultat arbitraire.

|  | Typage fort | Typage faible |
| --- | --- | --- |
| **Dynamique** | Python, Ruby | JavaScript, PHP |
| **Statique** | Java, Rust | C (conversions implicites nombreuses) |

```python
x = 10
print(type(x))        # → <class 'int'>
x = 'dix'             # le nom x désigne maintenant une chaîne
print(type(x))        # → <class 'str'>

try:
    '1' + 2
except TypeError as erreur:
    print(erreur)     # → can only concatenate str (not 'int') to str
```

Depuis Python 3.5, on peut **annoter** les types (`x: int = 10`) ; ces annotations ne changent rien à l'exécution mais sont exploitées par des outils de vérification (chapitre 17). On parle de **typage graduel**.

#### Tout est objet

En Python, **toute valeur est un objet** : les nombres, les chaînes, les fonctions, les classes, les modules. Chaque objet possède une **identité** (son adresse, donnée par `id()`), un **type** (donné par `type()`) et une **valeur**. Cette uniformité explique la cohérence du langage : on peut passer une fonction en argument, stocker une classe dans une liste ou appeler une méthode sur un entier littéral.

```python
print((255).bit_length())   # → 8 : un entier possède des méthodes
print(type(print))          # → <class 'builtin_function_or_method'>
print(type(int))            # → <class 'type'>
```

#### Gestion automatique de la mémoire

Le programmeur n'alloue ni ne libère la mémoire. CPython utilise le **comptage de références** (un objet est détruit quand plus aucun nom ne le référence) complété par un **ramasse-miettes** (*garbage collector*) qui détecte et supprime les cycles de références.

#### Le Zen de Python

La PEP 20 résume la philosophie du langage en aphorismes ; on les affiche avec `import this`. Retenez-en l'esprit : le beau vaut mieux que le laid, l'explicite vaut mieux que l'implicite, le simple vaut mieux que le complexe, la lisibilité compte, et il devrait exister une manière évidente (et de préférence unique) de faire une chose. Un code est dit **pythonique** lorsqu'il respecte ces principes et utilise les idiomes du langage.

#### Pourquoi les débutants l'apprécient

- Une syntaxe proche de l'anglais, sans point-virgule ni accolades, sans déclaration de types obligatoire.
- Un mode interactif qui permet d'essayer une idée en quelques secondes.
- Des messages d'erreur de plus en plus explicites.
- Une communauté vaste et une documentation abondante, y compris en français.

#### Pourquoi les professionnels l'utilisent

- Un écosystème immense (NumPy, Pandas, Django, FastAPI, PyTorch…).
- Un langage adapté au prototypage rapide comme à la production.
- Une intégration facile avec d'autres langages (C, C++, Rust, Java) et d'autres outils.
- Un faible coût de maintenance grâce à la lisibilité du code.

### 1.2 Domaines d'utilisation

| Domaine | Description et outils courants |
| --- | --- |
| **Développement web** | Côté serveur : Django (framework complet), Flask (micro-framework), FastAPI (API modernes asynchrones). |
| **Science des données et IA** | NumPy (calcul sur tableaux), Pandas et Polars (données tabulaires), Matplotlib (graphiques), Scikit-learn (apprentissage automatique), PyTorch et TensorFlow (apprentissage profond). |
| **Automatisation et scripts** | Manipulation de fichiers, tâches planifiées (cron), robots, extraction de données web (Beautiful Soup, Selenium, Playwright). |
| **Jeux vidéo** | Pygame ; GDScript (langage de Godot) s'inspire fortement de la syntaxe Python. |
| **Applications de bureau** | Tkinter (fourni), PyQt / PySide, Kivy. |
| **Systèmes embarqués / IoT** | MicroPython et CircuitPython sur microcontrôleurs (ESP32, Raspberry Pi Pico). |
| **Cybersécurité** | Outils d'analyse, audits, automatisation de tests de sécurité. |
| **Calcul scientifique** | SciPy, SymPy (calcul formel), notebooks Jupyter. |
| **DevOps et administration** | Scripts de déploiement, outils en ligne de commande, automatisation cloud (AWS, Azure, GCP). |
| **Enseignement** | Syntaxe claire, nombreux supports, forte demande sur le marché du travail. |

Python est souvent surnommé *langage de colle* (*glue language*) : il relie des composants écrits dans d'autres langages. Les bibliothèques de calcul comme NumPy ou PyTorch sont écrites en C, C++ ou Rust et pilotées depuis Python.

### 1.3 Histoire de Python

#### Création

Guido van Rossum, programmeur néerlandais, commence à développer Python à la fin des années 1980 au **CWI** (*Centrum Wiskunde & Informatica*, Pays-Bas), pendant les vacances de Noël 1989. La première publication publique, la version **0.9.0**, date de **février 1991**. Le nom ne vient pas du serpent mais du groupe d'humour britannique **Monty Python**, dont Guido était fan : cet esprit ludique se retrouve dans la documentation (les exemples utilisent souvent `spam` et `eggs`).

#### Objectifs de conception

- Privilégier la **lisibilité** du code ;
- exprimer des idées en **moins de lignes** que dans d'autres langages ;
- combler l'écart entre le **C** (puissant mais lourd) et les **scripts shell** (rapides à écrire mais limités) ;
- offrir une alternative à **ABC**, langage d'enseignement développé au CWI dont Python s'inspire.

#### Les grandes versions

| Version | Date | Points marquants |
| --- | --- | --- |
| **1.0** | janvier 1994 | Fonctions, exceptions, types de base (`str`, `list`, `dict`), `lambda`, `map`, `filter`. |
| **2.0** | octobre 2000 | Compréhensions de listes, ramasse-miettes avec détection de cycles, début du support Unicode. |
| **3.0** | décembre 2008 | Rupture de compatibilité avec Python 2 : `print()` devient une fonction, Unicode natif pour les chaînes, division « vraie » (`5 / 2` donne `2.5`), bibliothèque standard nettoyée. |
| **3.10** | octobre 2021 | Filtrage par motifs (`match` / `case`), unions `X \| Y`, meilleurs messages d'erreur. |
| **3.11** | octobre 2022 | Interpréteur nettement plus rapide, groupes d'exceptions (`except*`), module `tomllib`. |
| **3.12** | octobre 2023 | Syntaxe de paramètres de type (PEP 695), instruction `type`, f-strings plus souples. |
| **3.13** | octobre 2024 | Nouveau REPL, version expérimentale sans GIL, compilateur JIT expérimental. |
| **3.14** | octobre 2025 | Template strings (t-strings), évaluation différée des annotations, *free-threading* officiellement supporté, sous-interpréteurs. |
| **3.15** | octobre 2026 | Version annuelle la plus récente ; consultez python.org pour l'état exact de la publication. |

**Python 2 contre Python 3.** Python 3 a corrigé des défauts de conception de Python 2 au prix d'une incompatibilité : une longue période de transition a suivi. Python 2 a atteint sa **fin de vie le 1er janvier 2020** : plus aucun correctif, même de sécurité. Tout nouveau projet doit utiliser Python 3.

**Cycle de publication.** Depuis la PEP 602, une version majeure paraît chaque année en octobre. Chaque version bénéficie d'environ **cinq ans de support** : deux ans de correctifs de bogues, puis trois ans de correctifs de sécurité uniquement. Conséquence pratique : une version dont la fin de vie est atteinte ne reçoit plus de correctif de sécurité et ne doit plus être utilisée en production.

#### Gouvernance et communauté

- Guido van Rossum fut le **BDFL** (*Benevolent Dictator For Life*, « dictateur bienveillant à vie ») jusqu'à sa démission en juillet **2018**.
- Le langage est depuis gouverné par un **Conseil de pilotage** (*Steering Council*) de cinq membres, élu par les développeurs du cœur de Python.
- La **Python Software Foundation (PSF)**, fondée en **2001**, est l'organisation à but non lucratif qui détient les droits, soutient la communauté et finance les conférences (PyCon).
- Les évolutions du langage passent par les **PEP** (*Python Enhancement Proposals*) : un document public décrit la proposition, ses motivations et ses alternatives, puis la communauté la discute avant décision.
- Python figure régulièrement parmi les trois langages les plus utilisés au monde et sert chez Google, Netflix, Dropbox, Instagram, Reddit, etc.

#### Chronologie

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
| 2024 | Python 3.13 : premiers builds sans GIL (expérimentaux) |
| 2025 | Python 3.14 : *free-threading* officiellement supporté |

### 1.4 Caractéristiques de Python

**1. Langage interprété.** L'interpréteur traduit le code en bytecode puis l'exécute. Le cycle écriture → test est très court, et le débogage est confortable. Le prix à payer est une vitesse d'exécution généralement inférieure à celle des langages compilés.

**2. Syntaxe lisible fondée sur l'indentation.** Les blocs de code sont délimités par le décalage des lignes, non par des accolades. Le code qui s'écrit est donc aussi celui qui est structuré visuellement.

```python
age = 20
if age >= 18:
    print('Vous pouvez voter.')           # → Vous pouvez voter.
else:
    print('Vous êtes encore trop jeune.')
```

**3. Typage dynamique et graduel** (voir 1.1).

**4. Portabilité.** Un même script s'exécute sur Windows, macOS et Linux, presque sans modification, car le bytecode est indépendant de la plateforme et la bibliothèque standard abstrait les différences (par exemple `pathlib` pour les chemins).

**5. Bibliothèque standard riche (« batteries incluses »).** Python est livré avec des modules couvrant la plupart des besoins courants.

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
print(math.sqrt(25))   # → 5.0
```

**6. Libre et gratuit.** Le code source est ouvert (licence de la PSF) ; l'usage est gratuit, y compris commercial.

**7. Multi-paradigme.** Un même programme peut mêler fonctions, classes et style fonctionnel.

```python
class Chien:
    def __init__(self, nom):
        self.nom = nom

    def aboyer(self):
        print(f'{self.nom} fait ouaf !')

Chien('Rex').aboyer()   # → Rex fait ouaf !
```

**8. Extensible et embarquable.** On peut écrire les parties critiques en C, C++ ou Rust (extensions natives, `ctypes`, Cython, PyO3) et les appeler depuis Python ; à l'inverse, Python peut être embarqué dans une application comme langage de script.

**9. Gestion automatique de la mémoire** (voir 1.1).

**10. Mode interactif (REPL).** *Read-Eval-Print Loop* : l'interpréteur lit une expression, l'évalue, affiche le résultat et recommence. Depuis Python 3.13, le REPL propose coloration syntaxique, édition multiligne, historique et collage de blocs.

**11. Communauté active.** Forum officiel (discuss.python.org), Stack Overflow, Reddit, Discord, conférences.

**12. Écosystème de bibliothèques.** PyPI, l'index des paquets, en recense des centaines de milliers.

| Domaine | Bibliothèques / frameworks |
| --- | --- |
| Web | Django, Flask, FastAPI |
| Données | NumPy, Pandas, Polars, Matplotlib, Seaborn |
| IA / ML | Scikit-learn, TensorFlow, PyTorch |
| Interfaces graphiques | Tkinter, PyQt, Kivy |
| Jeux | Pygame |
| Automatisation | Selenium, Playwright, PyAutoGUI |
| Réseau | Requests, httpx, Paramiko |

**Limites à connaître.** Python est plus lent que les langages compilés pour les calculs purs ; le **GIL** (voir 1.8 et chapitre 18) limite le parallélisme des threads ; la consommation mémoire est plus élevée ; le typage dynamique reporte des erreurs à l'exécution. Ces limites se contournent (NumPy, extensions natives, multiprocessing, typage statique) et pèsent peu pour la plupart des usages.

### 1.5 Installer Python

Le site officiel est **python.org/downloads**. Choisissez toujours la dernière version stable de Python 3 (3.14 ou plus récente). N'utilisez plus Python 2.

#### Windows

1. Téléchargez l'installateur sur python.org (ou le *Python install manager* proposé par le site).
2. Cochez **« Add python.exe to PATH »** avant de cliquer sur *Install Now*. Le `PATH` est la liste des dossiers où le système cherche les commandes : sans cette case, la commande `python` n'est pas reconnue.
3. Vérifiez dans un terminal : `python --version` ou, avec le lanceur Windows, `py --version`.

Alternatives : `winget install Python.Python.3.14` ou `choco install python`. Si `python` n'est pas reconnu après installation, ajoutez manuellement au `PATH` le dossier d'installation **et** son sous-dossier `Scripts`, via *Paramètres système → Variables d'environnement*.

#### macOS

Utilisez l'installateur `.pkg` officiel ou, de préférence, **Homebrew** :

```bash
brew install python
python3 --version
```

#### Linux

La plupart des distributions incluent déjà Python, mais souvent une version ancienne ; ne désinstallez jamais le Python du système, car des outils de la distribution en dépendent.

```bash
# Debian / Ubuntu
sudo apt update && sudo apt install python3 python3-pip python3-venv
# Fedora
sudo dnf install python3
# Arch
sudo pacman -S python
```

Pour une version plus récente, utilisez le PPA **deadsnakes** (Ubuntu) ou, mieux, **uv**.

#### Gestionnaires multiplateformes

| Outil | Usage |
| --- | --- |
| **uv** | Installe Python *et* gère paquets, environnements et projets ; très rapide |
| **pyenv** | Installe et alterne entre plusieurs versions de Python |
| **Anaconda / Miniconda** | Distribution orientée science des données, avec son propre gestionnaire d'environnements |

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.14
```

#### pip et vérification

`pip` est l'installateur de paquets, fourni avec Python. En cas de problème :

```bash
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python3 --version
```

On écrit `python -m pip` plutôt que `pip` seul afin d'être certain d'utiliser `pip` associé à l'interpréteur voulu.

### 1.6 Choisir un éditeur ou un IDE

Un **éditeur de code** est un outil léger (coloration syntaxique, complétion simple). Un **IDE** (*Integrated Development Environment*, environnement de développement intégré) réunit éditeur, débogueur, gestion de projet, terminal et contrôle de version.

| Outil | Type | Public | Points forts |
| --- | --- | --- | --- |
| **VS Code** | Éditeur | Tous niveaux | Gratuit, extensible, excellent support Python |
| **PyCharm** | IDE | Intermédiaire à professionnel | Intégration Python très poussée (éditions Community et Pro) |
| **Thonny** | IDE | Débutants | Simple, débogueur visuel, fourni avec Python |
| **IDLE** | IDE | Débutants | Livré avec Python |
| **Sublime Text** | Éditeur | Intermédiaire | Rapide (licence payante, essai gratuit) |
| **JupyterLab** | Notebook | Science des données | Code, texte et graphiques dans un même document |
| **Zed, Neovim** | Éditeurs | Avancé | Rapides, très configurables |

Atom a été archivé par GitHub en 2022 : ne l'utilisez plus. Dans VS Code, installez les extensions **Python** et **Pylance** (analyse du code), **Ruff** (lint et formatage ultra-rapides) et **Jupyter**.

| Besoin | Recommandation |
| --- | --- |
| Débuter | Thonny ou IDLE |
| Développement général | VS Code ou PyCharm Community |
| Web | PyCharm Pro ou VS Code |
| Science des données | JupyterLab ou VS Code + Jupyter |

### 1.7 Exécuter son premier programme

Python s'exécute de deux manières : en **mode interactif** (REPL) ou en **mode script** (fichier `.py`).

#### Mode interactif

```bash
$ python3
>>> print('Bonjour le monde !')
Bonjour le monde !
>>> 2 + 3
5
```

L'invite `>>>` attend une instruction ; `...` signale qu'un bloc continue. Une expression est évaluée et son résultat affiché sans `print`. Pour quitter : `exit()`, `Ctrl+D` (macOS/Linux) ou `Ctrl+Z` puis Entrée (Windows).

#### Mode script

```python
# bonjour.py
print('Bonjour, Python !')
```

```bash
python bonjour.py
```

| Critère | Mode interactif | Mode script |
| --- | --- | --- |
| Exécution | Ligne par ligne | Fichier entier |
| Idéal pour | Tests, apprentissage, exploration | Programmes complets |
| Sauvegarde du code | Non | Oui |
| Retour | Immédiat | Après exécution |

Utilisez le REPL pour tester une expression ou explorer une fonction (`type()`, `help()`, `dir()`), et un script pour tout ce que vous voulez conserver ou réutiliser.

#### Autres façons de lancer Python

```bash
python -c "print('Une ligne')"   # exécute une commande
python -m http.server             # exécute un module comme script
python -i script.py               # reste en mode interactif après le script
```

#### Le *shebang* (Unix)

La première ligne `#!/usr/bin/env python3` indique au système quel interpréteur utiliser. Après `chmod +x script.py`, le fichier s'exécute avec `./script.py`.

#### Erreurs courantes

Si le fichier est introuvable, vérifiez le dossier courant et déplacez-vous avec `cd`. Si la commande `python` n'est pas reconnue, Python n'est pas dans le `PATH` (voir 1.5). Dans VS Code, choisissez l'interpréteur avec `Ctrl+Shift+P` → *Python: Select Interpreter* ; dans IDLE, enregistrez le fichier puis appuyez sur F5.

### 1.8 L'interpréteur Python

L'interpréteur lit le code source, le **compile en bytecode**, puis le fait exécuter par la **machine virtuelle Python (PVM)**.

```text
Code source (.py) → compilateur intégré → bytecode (.pyc) → machine virtuelle (PVM) → résultat
```

- Le **bytecode** est un jeu d'instructions de bas niveau, indépendant de la plateforme. Il est mis en cache dans des fichiers `.pyc` du dossier `__pycache__`, ce qui accélère les exécutions suivantes d'un module. Le module `dis` permet de l'examiner.
- La **PVM** exécute ce bytecode instruction par instruction, gère la mémoire, les variables, les exceptions et le typage dynamique.

Python est donc à la fois **compilé** (vers du bytecode) et **interprété** (par la PVM). Comparé à un langage compilé en code machine, il est plus lent mais plus souple à déboguer et plus portable.

#### Les implémentations

| Implémentation | Description |
| --- | --- |
| **CPython** | Implémentation de référence, écrite en C ; la plus utilisée |
| **PyPy** | Compilation JIT (*just-in-time*), souvent beaucoup plus rapide |
| **Jython** | Python sur la JVM (Java) |
| **IronPython** | Python sur .NET |
| **MicroPython** | Pour microcontrôleurs |
| **GraalPy** | Python sur GraalVM |

Depuis Python 3.13, CPython propose, à titre expérimental, un compilateur JIT et une version sans GIL. Le **GIL** (*Global Interpreter Lock*) est un verrou qui empêche plusieurs threads d'exécuter du bytecode Python en même temps (voir chapitre 18).

#### Peut-on exécuter Python sans interpréteur ?

Pas directement. On peut toutefois utiliser un interpréteur en ligne (Replit, Google Colab) ou empaqueter une application avec un interpréteur intégré grâce à **PyInstaller**, **cx\_Freeze** ou **Nuitka**.

#### Options utiles de l'interpréteur

| Option | Effet |
| --- | --- |
| `-i` | Mode interactif après l'exécution du script |
| `-m` | Exécute un module comme script |
| `-c` | Exécute une commande |
| `-O` | Optimise le bytecode (supprime les `assert`) |
| `-B` | N'écrit pas de fichiers `.pyc` |
| `-X dev` | Mode développement (vérifications supplémentaires) |

### 1.9 « Hello, World ! »

```python
print('Bonjour le monde !')
```

`print` est une **fonction intégrée** (*built-in*) qui affiche du texte. Le texte, ou **chaîne de caractères**, s'écrit entre guillemets simples ou doubles. Depuis Python 3, `print` est une fonction : `print('x')` et non `print 'x'`.

#### La fonction `print()` en détail

```python
import sys

print('A', 'B', 'C')               # → A B C
print('A', 'B', sep='-')           # → A-B
print('Chargement', end='...')     # pas de retour à la ligne
print('terminé')                   # → Chargement...terminé
print('Erreur', file=sys.stderr)   # écrit sur le flux d'erreur
print('Direct', flush=True)        # vide le tampon immédiatement
```

| Paramètre | Rôle | Défaut |
| --- | --- | --- |
| `sep` | Séparateur entre les valeurs | un espace |
| `end` | Texte écrit à la fin | retour à la ligne |
| `file` | Destination | `sys.stdout` |
| `flush` | Vider le tampon | `False` |

#### Commentaires

Un commentaire est ignoré par l'interpréteur ; il s'adresse au lecteur humain. Il commence par `#` et s'étend jusqu'à la fin de la ligne. Une chaîne multiligne entre triples guillemets, non affectée à une variable, est parfois utilisée comme commentaire ; c'est en réalité une chaîne littérale évaluée puis ignorée, sauf à l'emplacement d'une **docstring** (voir chapitre 11).

```python
x = 5   # commentaire en fin de ligne
```

**Bonnes pratiques** : expliquez le *pourquoi* plutôt que le *quoi* ; mettez-les à jour avec le code ; évitez l'évidence (`x = 1  # x vaut 1`).

#### Extensions de fichiers

| Extension | Signification |
| --- | --- |
| `.py` | Script ou module Python |
| `.pyc` | Bytecode compilé (dans `__pycache__`) |
| `.pyi` | Fichier de *stubs* de typage |
| `.pyw` | Script Windows sans console |
| `.pyd` | Module d'extension compilé (Windows) |
| `.so` | Extension compilée (Linux, macOS) |
| `.ipynb` | Notebook Jupyter |
| `.toml` | Configuration (`pyproject.toml`) |

#### Étapes d'exécution

1. **Analyse lexicale et syntaxique** du fichier source ; une erreur de syntaxe est signalée ici, avant toute exécution.
2. **Compilation** en bytecode.
3. **Exécution** par la PVM, instruction par instruction.

#### PEP essentielles

| PEP | Sujet |
| --- | --- |
| 8 | Guide de style du code Python |
| 20 | Le Zen de Python |
| 257 | Conventions pour les docstrings |
| 484 | Annotations de types |
| 572 | Opérateur morse `:=` |
| 621 | Métadonnées de projet dans `pyproject.toml` |
| 634 | Filtrage par motifs (`match`) |
| 750 | Template strings (t-strings, Python 3.14) |

Toutes sont consultables sur peps.python.org.

#### Obtenir de l'aide

```python
x = 42
help(len)             # documentation d'une fonction
print(dir(list)[-3:]) # → ['remove', 'reverse', 'sort']
print(type(x))        # → <class 'int'>
print(len.__doc__)    # docstring brute
```

En ligne de commande : `python -m pydoc len`. Ressources : docs.python.org, Real Python, discuss.python.org, Stack Overflow.

### À retenir (chapitre 1)

- Python est un langage de haut niveau, polyvalent, multi-paradigme, au typage **dynamique et fort**, où **tout est objet**.
- Le code source est compilé en bytecode puis exécuté par la machine virtuelle ; CPython est l'implémentation de référence.
- Une version majeure paraît chaque octobre ; utilisez toujours une version de Python 3 encore supportée.
- Le REPL sert à explorer, les scripts `.py` à conserver.
- `print()`, `help()`, `dir()` et `type()` sont vos premiers outils d'investigation.

## 2. Syntaxe et indentation

**Objectifs du chapitre** : comprendre comment Python lit un fichier source, maîtriser l'indentation qui structure le code, distinguer expressions et instructions, et adopter dès le début les conventions de la PEP 8.

### 2.1 Introduction à la syntaxe

La **syntaxe** d'un langage est l'ensemble des règles qui définissent ce qu'est un programme valide ; la **sémantique** décrit ce que ce programme signifie et fait. Un programme syntaxiquement correct peut être sémantiquement faux (il s'exécute mais ne fait pas ce qu'on veut) : c'est la différence entre une erreur de syntaxe et un bogue.

Avant de l'exécuter, Python découpe le texte en **lexèmes** (*tokens*), unités élémentaires de plusieurs sortes :

- les **identifiants** (noms de variables, fonctions, classes) : `age`, `calculer_total` ;
- les **mots-clés**, réservés par le langage : `if`, `for`, `def`, `class`, `None`… ;
- les **littéraux**, valeurs écrites directement dans le code : `42`, `3.14`, `'texte'`, `True` ;
- les **opérateurs** (`+`, `==`, `and`) et les **délimiteurs** (`( ) [ ] { } , : .`) ;
- les lexèmes spéciaux de structure : fin de ligne, **indentation** et **désindentation**.

La syntaxe de Python est volontairement épurée : pas d'accolades, pas de point-virgule obligatoire, des blocs délimités par l'indentation.

```python
nom = 'Alice'
if nom:
    print(f'Bonjour {nom}')   # → Bonjour Alice
```

### 2.2 Le rôle de l'indentation

Dans la plupart des langages, l'indentation est une aide de lecture facultative. En Python, elle **fait partie de la syntaxe** : c'est elle qui définit les blocs (fonctions, boucles, conditions, classes). Deux lignes consecutives au même niveau appartiennent au même bloc ; un niveau d'indentation de plus ouvre un bloc, un niveau de moins le ferme.

```python
def saluer(nom):
    if nom:
        print(f'Bonjour {nom}')    # bloc du if
    else:
        print('Bonjour inconnu')   # bloc du else
    print('Fin')                   # dans la fonction, après le if/else
```

#### Règles

| Règle | Détail |
| --- | --- |
| Taille standard | **4 espaces** par niveau (PEP 8) |
| Cohérence | Gardez le même niveau pour toutes les lignes d'un bloc |
| Tabulations | Ne **mélangez jamais** tabulations et espaces dans un même fichier (`TabError`) |
| Éditeur | Configurez-le pour insérer 4 espaces à la touche Tab |

```python
code_incorrect = 'if True:\nprint(1)'   # le corps du if n'est pas indenté
try:
    compile(code_incorrect, '<exemple>', 'exec')
except IndentationError as erreur:
    print(erreur.msg)   # → expected an indented block after 'if' statement on line 1
```

L'avantage de ce choix est que la structure visible est exactement la structure exécutée ; son inconvénient est qu'une mauvaise indentation change le sens du programme ou le rend invalide.

### 2.3 Blocs de code

Un **bloc** commence après une ligne d'en-tête qui se termine par `:` (le deux-points) et regroupe les lignes indentées qui suivent. Les blocs peuvent s'imbriquer.

```python
for i in range(3):      # en-tête
    print(i)            # corps
    if i == 1:
        print('Un !')   # bloc imbriqué
```

Un bloc ne peut pas être vide. Quand on n'a encore rien à y écrire, on utilise l'instruction `pass`, qui ne fait rien :

```python
def a_ecrire_plus_tard():
    pass
```

### 2.4 Instructions simples

Une **instruction** (*statement*) est une commande exécutable. La norme est **une instruction par ligne**. On peut en séparer plusieurs par un point-virgule, mais la PEP 8 le déconseille.

```python
x = 5
y = 10
print(x + y)     # → 15
a = 1; b = 2     # valide mais déconseillé
```

#### Instructions sur plusieurs lignes

Une instruction trop longue peut être répartie sur plusieurs lignes de deux façons.

1. **Continuation implicite** (recommandée) : à l'intérieur de parenthèses, crochets ou accolades, le retour à la ligne est ignoré.
2. **Antislash** `\` en fin de ligne (à éviter : un espace invisible après l'antislash casse le code).

```python
total = (1 + 2 + 3 +
         4 + 5)
print(total)   # → 15

liste = [
    'pomme',
    'banane',
    'cerise',
]                # la virgule finale est autorisée et facilite les modifications
```

### 2.5 Sensibilité à la casse et mots-clés

Python **distingue majuscules et minuscules** : `nom`, `Nom` et `NOM` sont trois identifiants différents. Les mots-clés doivent être écrits exactement comme prévu (`True`, `False` et `None` prennent une majuscule).

```python
import keyword
print(len(keyword.kwlist) > 30)   # → True
print('if' in keyword.kwlist)     # → True
print(keyword.softkwlist)         # mots-clés « souples » : _, case, match, type
```

Les mots-clés *durs* (`if`, `class`, `for`, `None`…) ne peuvent jamais servir de noms. Les mots-clés *souples* (`match`, `case`, `type`, `_`) n'ont un sens spécial que dans certains contextes. Ne confondez pas mots-clés et **fonctions intégrées** (`print`, `len`, `list`…) : ces dernières peuvent techniquement être « masquées » par une affectation (`list = 3` détruit l'accès à `list`), ce qu'il faut absolument éviter.

### 2.6 Expressions et instructions

- Une **expression** est un fragment de code qui **produit une valeur** : `3 + 4`, `len('abc')`, `x > 5`.
- Une **instruction** **effectue une action** : `x = 5`, `if`, `for`, `import`, `return`.

On peut mettre une expression là où une valeur est attendue (argument, membre droit d'une affectation) ; on ne peut pas imbriquer une instruction dans une expression.

```python
y = (3 + 4) * 2   # instruction d'affectation contenant une expression
print(y)          # → 14
```

Depuis Python 3.8, l'**opérateur morse** `:=` (expression d'affectation, PEP 572) permet d'affecter *au sein* d'une expression, ce qui évite un double calcul :

```python
if (n := len('Python')) > 5:
    print(f'Chaîne longue ({n} caractères)')   # → Chaîne longue (6 caractères)
```

### 2.7 Lignes vides et espaces

La PEP 8 fixe des conventions de présentation :

- **deux lignes vides** entre les fonctions et classes de premier niveau ;
- **une ligne vide** entre les méthodes d'une classe, et pour séparer des blocs logiques dans une fonction ;
- un espace de part et d'autre des opérateurs d'affectation et de comparaison : `x = a + b` ;
- pas d'espace avant la parenthèse ouvrante d'un appel (`f(x)`), ni avant `:` et `,`, ni juste après `(` ou avant `)`.

```python
resultat = calculer(a, b)    # conforme
resultat=calculer( a,b )     # valide mais non conforme
```

### 2.8 Le deux-points `:`

Le caractère `:` introduit un bloc (`if`, `elif`, `else`, `for`, `while`, `def`, `class`, `try`, `with`, `match`, `case`…) mais il a aussi d'autres rôles : séparer les bornes d'une **tranche** (`liste[1:3]`), associer **clé et valeur** dans un dictionnaire (`{'a': 1}`), et introduire une **annotation** de type (`x: int`). Le contexte permet de les distinguer.

### 2.9 Erreurs de syntaxe et d'indentation

| Erreur | Cause | Exemple |
| --- | --- | --- |
| `SyntaxError` | Syntaxe invalide | parenthèse non fermée, `:` oublié |
| `IndentationError` | Indentation incorrecte | bloc non indenté, niveaux incohérents |
| `TabError` | Mélange de tabulations et d'espaces | — |

Une erreur de syntaxe est détectée **avant toute exécution** : aucune ligne du fichier ne s'exécute. Depuis Python 3.10, les messages sont très explicites (par exemple l'indication qu'une parenthèse n'a jamais été fermée, ou une suggestion de nom proche en cas de faute de frappe). Apprenez à **lire la trace d'erreur de bas en haut** : la dernière ligne donne le type et le message, les lignes au-dessus indiquent où cela s'est produit.

### 2.10 Écrire du code propre (PEP 8)

La **PEP 8** est le guide de style officiel. Un code lisible se relit plus souvent qu'il ne s'écrit.

| Élément | Convention | Exemple |
| --- | --- | --- |
| Variables, fonctions, modules | `snake_case` | `nom_utilisateur` |
| Classes | `PascalCase` | `CompteBancaire` |
| Constantes | `MAJUSCULES_AVEC_TIRETS_BAS` | `TAUX_TVA` |
| Longueur de ligne | 79 caractères (PEP 8) ; 88 avec Black et Ruff | — |
| Imports | en tête de fichier, un par ligne, groupés : bibliothèque standard, tiers, local | — |

```python
# Peu lisible
def f(x,y):return x+y

# Lisible
def additionner(x, y):
    return x + y
```

Le style **pythonique** privilégie les idiomes du langage, par exemple les compréhensions plutôt que les boucles de construction de liste :

```python
nombres = [1, 2, 3]
resultat = [x * 2 for x in nombres]
print(resultat)   # → [2, 4, 6]
```

Outils modernes : **Ruff** (lint et formatage), **Black** (formatage), **mypy** et **pyright** (vérification de types). Ils appliquent automatiquement ces conventions.

### À retenir (chapitre 2)

- L'indentation (4 espaces) délimite les blocs ; ne mélangez jamais tabulations et espaces.
- Un bloc s'ouvre après `:` et ne peut pas être vide (`pass`).
- Python est sensible à la casse ; les mots-clés sont réservés.
- Une expression produit une valeur, une instruction réalise une action ; `:=` affecte au sein d'une expression.
- Suivez la PEP 8 et laissez Ruff ou Black formater le code.

## 3. Variables et types de données

**Objectifs du chapitre** : comprendre ce qu'est réellement une variable en Python, connaître tous les types de base et leurs particularités, maîtriser conversions, mutabilité et portée.

### 3.1 Les variables

En Python, une **variable** n'est pas une boîte qui contient une valeur : c'est un **nom** qui **référence** un objet en mémoire. L'instruction `x = 5` crée (ou récupère) l'objet entier `5` puis **lie** le nom `x` à cet objet. On parle de **liaison** (*binding*). Plusieurs noms peuvent référencer le même objet ; un nom peut être relié à un autre objet à tout moment. Cette vision explique de nombreux comportements « surprenants » (voir 3.9).

```python
age = 25
nom = 'Alice'
taille = 1.68
est_majeur = True
print(age, nom, taille, est_majeur)   # → 25 Alice 1.68 True
```

#### Règles de nommage

- Un identifiant contient des lettres, des chiffres et le caractère `_`, et ne **commence pas par un chiffre** ;
- il est sensible à la casse ;
- il ne peut pas être un mot-clé (`class`, `if`, `None`…) ;
- on choisit des noms **explicites** en `snake_case` (`prix_total`, pas `pt`).

```python
nom_utilisateur = 'Alice'   # valide
_prive = 1                  # valide
valeur2 = 2                 # valide
# 2valeur = 1   → SyntaxError : commence par un chiffre
# mon-nom = 1   → SyntaxError : le tiret est l'opérateur de soustraction
# class = 'A'   → SyntaxError : mot-clé réservé
```

| Convention | Signification |
| --- | --- |
| `_x` | Usage interne (simple convention) |
| `x_` | Évite un conflit avec un mot-clé (`class_`) |
| `__x` | Dans une classe, nom transformé (*name mangling*) |
| `__x__` | Méthodes spéciales (« dunder ») réservées au langage |

#### Affectation

```python
x = 5                           # simple
a = b = c = 0                   # même valeur pour plusieurs noms
x, y, z = 1, 2, 3               # valeurs différentes (déballage de tuple)
y, z = z, y                     # échange sans variable temporaire
premier, *reste = [1, 2, 3, 4]  # déballage étoilé
print(x, y, z)                  # → 1 3 2
print(premier, reste)           # → 1 [2, 3, 4]
```

La suppression d'un nom se fait avec `del x`. Utiliser un nom non défini provoque une `NameError`.

### 3.2 Vue d'ensemble des types de base

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

Un **type** définit l'ensemble des valeurs possibles et les opérations permises. Les chapitres 7 à 10 détaillent les collections.

### 3.3 Types numériques

#### Entiers (`int`)

Les entiers ont une **taille illimitée** : seuls la mémoire disponible et le temps de calcul les limitent. Il n'y a donc pas de dépassement d'entier comme en C ou en Java.

```python
grand = 10 ** 100
print(len(str(grand)))          # → 101
print(1_000_000)                # → 1000000 (séparateurs de lisibilité)
print(0b1010, 0o17, 0xFF)       # → 10 15 255 (binaire, octal, hexadécimal)
```

#### Flottants (`float`)

Les `float` suivent la norme **IEEE 754** en double précision (64 bits) : environ 15 à 17 chiffres significatifs. Beaucoup de décimaux (comme 0,1) n'ont pas de représentation binaire exacte, d'où des écarts minuscules.

```python
print(0.1 + 0.2)          # → 0.30000000000000004
print(0.1 + 0.2 == 0.3)   # → False
import math
print(math.isclose(0.1 + 0.2, 0.3))   # → True : comparer avec une tolérance
```

Pour un calcul décimal exact (finance), utilisez `decimal.Decimal` ; pour des rationnels exacts, `fractions.Fraction` :

```python
from decimal import Decimal
from fractions import Fraction
print(Decimal('0.1') + Decimal('0.2'))   # → 0.3
print(Fraction(1, 3) + Fraction(1, 6))   # → 1/2
```

Valeurs spéciales : `float('inf')`, `float('-inf')` et `float('nan')` (*not a number*, qui n'est jamais égal à lui-même ; testez-le avec `math.isnan`).

#### Complexes (`complex`)

```python
z = 2 + 3j
print(z.real, z.imag, abs(3 + 4j))   # → 2.0 3.0 5.0
```

#### Fonctions utiles

`abs()`, `round()` (arrondit au pair le plus proche en cas d'égalité : `round(2.5)` donne `2`), `pow()`, `divmod()`, `math.floor()`, `math.ceil()`, `math.sqrt()`, `math.isclose()`.

### 3.4 Chaînes de caractères (`str`)

Une chaîne est une **séquence immuable de caractères Unicode**. On l'écrit entre guillemets simples ou doubles (équivalents), ou entre triples guillemets pour plusieurs lignes.

```python
s1 = 'simple'
s2 = "double"
s3 = '''multi
ligne'''
brut = r'C:\nouveau\dossier'   # chaîne brute : l'antislash n'échappe rien
print(brut)                     # → C:\nouveau\dossier
```

#### Séquences d'échappement

| Séquence | Sens |
| --- | --- |
| `\\n` | retour à la ligne |
| `\\t` | tabulation |
| `\\\\` | antislash |
| `\\'` et `\\"` | guillemets |
| `\\u00e9` | caractère Unicode (ici é) |

#### Indexation et tranches

```python
s = 'Python'
print(s[0], s[-1])    # → P n   (l'indice -1 désigne le dernier)
print(s[1:4])         # → yth   (début inclus, fin exclue)
print(s[::-1])        # → nohtyP (pas négatif : inversion)
print(len(s))         # → 6
try:
    s[0] = 'J'
except TypeError as erreur:
    print(erreur)     # → 'str' object does not support item assignment
```

L'**immuabilité** signifie qu'une chaîne ne se modifie jamais : toute opération crée une nouvelle chaîne. Pour construire un long texte, on assemble avec `''.join(morceaux)` plutôt que de concaténer dans une boucle.

#### Méthodes principales

| Méthode | Rôle |
| --- | --- |
| `upper()`, `lower()`, `title()`, `capitalize()`, `casefold()` | Casse |
| `strip()`, `lstrip()`, `rstrip()` | Supprime les espaces (ou des caractères donnés) aux extrémités |
| `split(sep)`, `sep.join(liste)` | Découper / assembler |
| `replace(a, b)` | Remplacer |
| `find()`, `index()`, `count()` | Rechercher (`find` renvoie -1 si absent, `index` lève `ValueError`) |
| `startswith()`, `endswith()` | Tester le début ou la fin |
| `removeprefix()`, `removesuffix()` | Retirer un préfixe ou un suffixe (3.9+) |
| `isdigit()`, `isalpha()`, `isalnum()` | Tester le contenu |
| `zfill()`, `center()`, `ljust()`, `rjust()` | Remplissage et alignement |

#### F-strings

Les **chaînes formatées** (`f'...'`) évaluent des expressions entre accolades et acceptent un spécificateur de format après `:` (voir chapitre 5).

```python
nom, age = 'Alice', 30
print(f'{nom} a {age} ans')   # → Alice a 30 ans
print(f'{3.14159:.2f}')       # → 3.14
print(f'{nom=}')              # → nom='Alice' (utile au débogage)
```

#### Unicode et encodage

Une `str` contient des **points de code Unicode** ; elle devient une suite d'octets (`bytes`) par **encodage** (presque toujours UTF-8), et inversement par **décodage**.

```python
octets = 'café'.encode('utf-8')
print(octets)                    # → b'caf\xc3\xa9'
print(octets.decode('utf-8'))    # → café
print(len('café'), len(octets))   # → 4 5
```

### 3.5 Booléens

Le type `bool` n'a que deux valeurs : `True` et `False`. C'est une **sous-classe de `int`** : `True` vaut 1 et `False` vaut 0.

```python
print(5 > 3)                  # → True
print(isinstance(True, int))  # → True
print(True + True)            # → 2
```

#### Valeurs « vraies » et « fausses »

Dans une condition, toute valeur est évaluée comme un booléen. Sont **fausses** (*falsy*) : `False`, `None`, `0`, `0.0`, `0j`, `''`, `[]`, `()`, `{}`, `set()`, `range(0)`. **Tout le reste est vrai** (*truthy*). Une classe personnalisée est vraie sauf si elle définit `__bool__` ou `__len__`.

```python
liste = []
if not liste:
    print('La liste est vide')   # → La liste est vide
```

### 3.6 La valeur `None`

`None` représente l'**absence de valeur**. C'est l'unique instance du type `NoneType` (un *singleton*). On le teste avec `is None`, jamais avec `== None`. Une fonction sans `return` renvoie `None`.

```python
resultat = None
if resultat is None:
    print('Pas encore de résultat')   # → Pas encore de résultat
```

### 3.7 Conversion de types (*casting*)

Convertir signifie créer un objet d'un autre type à partir d'une valeur.

```python
print(int('42'))        # → 42
print(int(3.9))         # → 3   (troncature vers zéro)
print(int('ff', 16))    # → 255 (conversion depuis une base)
print(float('3.14'))    # → 3.14
print(str(100))         # → 100 (une chaîne)
print(bool(0))          # → False
print(list('abc'))      # → ['a', 'b', 'c']
print(tuple([1, 2]))    # → (1, 2)
print(set([1, 1, 2]))   # → {1, 2}
print(dict([('a', 1)])) # → {'a': 1}

try:
    int('abc')
except ValueError as erreur:
    print(erreur)       # → invalid literal for int() with base 10: 'abc'
```

Python effectue des conversions **implicites** entre nombres (`1 + 2.0` donne `3.0`) mais **jamais** entre nombre et chaîne : `'1' + 2` lève une `TypeError`. Le typage fort impose de convertir explicitement.

### 3.8 Vérifier le type

```python
x = 42
print(type(x))                       # → <class 'int'>
print(isinstance(x, int))            # → True
print(isinstance(x, (int, float)))   # → True : plusieurs types acceptés
```

Préférez `isinstance()` à `type(x) == int` : il tient compte de l'héritage (un `bool` est un `int`).

### 3.9 Types mutables et immuables

Un objet est **immuable** si son contenu ne peut pas changer après sa création ; il est **mutable** dans le cas contraire.

| Immuables | Mutables |
| --- | --- |
| `int`, `float`, `complex`, `bool`, `str`, `tuple`, `frozenset`, `bytes`, `None` | `list`, `dict`, `set`, `bytearray`, objets personnalisés |

Cette distinction a des conséquences directes, à cause du modèle de références :

```python
a = [1, 2]
b = a              # b est un second nom pour le MÊME objet
b.append(3)
print(a)           # → [1, 2, 3]
print(a is b)      # → True

c = a.copy()       # copie indépendante
c.append(4)
print(a)           # → [1, 2, 3]
print(c)           # → [1, 2, 3, 4]
print(a is c)      # → False

n = 5
m = n
m += 1             # crée un nouvel entier : n n'est pas modifié
print(n, m)        # → 5 6
```

- `id(x)` donne l'**identité** d'un objet ;
- `is` compare les **identités** (même objet ?) ;
- `==` compare les **valeurs** (mêmes contenus ?).

N'utilisez `is` que pour `None`, `True` et `False`. Python réutilise parfois le même objet pour de petits entiers ou des chaînes courtes (optimisation interne) : ne vous y fiez jamais.

### 3.10 Constantes

Python n'a pas de vraie constante : on utilise la **convention** des noms en majuscules. Pour les outils de vérification, `typing.Final` déclare l'intention.

```python
from typing import Final

PI: Final = 3.14159
MAX_ESSAIS: Final[int] = 3
print(PI, MAX_ESSAIS)   # → 3.14159 3
```

Pour des ensembles de constantes liées, on emploie `enum.Enum` (chapitre 16).

### 3.11 Portée des variables (règle LEGB)

La **portée** (*scope*) est la région du programme où un nom est visible. Python recherche un nom dans cet ordre : **L**ocal (la fonction courante) → **E**nglobant (les fonctions qui l'entourent) → **G**lobal (le module) → **B**uilt-in (les noms prédéfinis comme `len`).

```python
x = 'global'

def f():
    x = 'local'     # nouvelle variable locale : masque la globale
    print(x)

f()                 # → local
print(x)            # → global
```

Une affectation à l'intérieur d'une fonction crée par défaut une variable **locale**. Pour modifier une variable globale, on la déclare avec `global` ; pour une variable d'une fonction englobante, avec `nonlocal` (chapitre 11).

```python
compteur = 0

def incrementer():
    global compteur
    compteur += 1

incrementer()
incrementer()
print(compteur)   # → 2
```

Les variables locales disparaissent à la fin de l'appel de la fonction. Les variables globales rendent le code difficile à tester : évitez-les.

### 3.12 Bonnes pratiques

```python
d = 86400                      # peu clair
SECONDES_PAR_JOUR = 86400      # explicite
print(SECONDES_PAR_JOUR * 2)   # → 172800
```

- Choisissez des noms **descriptifs** ; ne changez pas inutilement le type d'une variable.
- Évitez les valeurs « magiques » : nommez-les.
- Ne masquez jamais une fonction intégrée (`list`, `str`, `sum`, `max`…).
- Utilisez `None` comme valeur par défaut pour les paramètres mutables (chapitre 11).

### À retenir (chapitre 3)

- Une variable est un nom lié à un objet ; les affectations ne copient pas, elles référencent.
- `int` est illimité, `float` est approché (IEEE 754), `Decimal` est exact en base 10.
- Une `str` est une séquence Unicode immuable ; `bytes` représente des octets.
- `bool` est un `int` ; les valeurs vides ou nulles sont « fausses » ; `None` se teste avec `is`.
- Immuable ou mutable détermine ce qu'une copie ou un alias provoque ; `is` compare l'identité, `==` la valeur.
- Les noms sont résolus selon LEGB.

## 4. Opérateurs et expressions

**Objectifs du chapitre** : connaître tous les opérateurs du langage, comprendre leur priorité et leur associativité, évaluer correctement une expression et éviter les pièges classiques.

Un **opérateur** est un symbole ou un mot-clé qui combine des **opérandes** pour produire une valeur. Un opérateur est **unaire** (un opérande : `-x`, `not x`), **binaire** (deux : `a + b`) ou, pour le conditionnel, **ternaire** (`a if c else b`).

### 4.1 Opérateurs arithmétiques

| Opérateur | Nom | Exemple | Résultat |
| --- | --- | --- | --- |
| `+` | Addition | `5 + 2` | `7` |
| `-` | Soustraction | `5 - 2` | `3` |
| `*` | Multiplication | `5 * 2` | `10` |
| `/` | Division réelle (toujours un `float`) | `5 / 2` | `2.5` |
| `//` | Division entière (arrondi vers le bas) | `5 // 2` | `2` |
| `%` | Modulo (reste) | `5 % 2` | `1` |
| `**` | Puissance | `5 ** 2` | `25` |
| `@` | Produit matriciel (NumPy, etc.) | `A @ B` | — |

La division entière arrondit vers **moins l'infini** (et non vers zéro), et le modulo prend le **signe du diviseur**. L'identité `a == (a // b) * b + a % b` reste toujours vraie.

```python
print(7 / 2, 7 // 2, 7 % 2)   # → 3.5 3 1
print(-7 // 2, -7 % 2)        # → -4 1
print(7 % -2)                 # → -1
print(divmod(7, 2))           # → (3, 1) : quotient et reste
print(2 ** -1)                # → 0.5 (exposant négatif : float)
print(7.5 // 2)               # → 3.0
```

Les opérateurs `+` et `*` s'appliquent aussi aux séquences : concaténation et répétition (`'ab' * 3` donne `'ababab'`, `[1] + [2]` donne `[1, 2]`).

### 4.2 Opérateurs d'affectation

L'**affectation augmentée** combine une opération et une affectation : `x += 2` équivaut à `x = x + 2`.

```python
x = 5
x += 2;  print(x)    # → 7
x -= 1;  print(x)    # → 6
x *= 3;  print(x)    # → 18
x /= 2;  print(x)    # → 9.0
x //= 2; print(x)    # → 4.0
x %= 3;  print(x)    # → 1.0
x **= 2; print(x)    # → 1.0
```

Il existe aussi `&=`, `|=`, `^=`, `<<=`, `>>=` et l'opérateur morse `:=`.

**Piège important.** Pour un objet **mutable**, `+=` modifie l'objet *en place*, alors que `x = x + y` en crée un nouveau. La différence est visible avec des alias :

```python
a = [1]
b = a
b += [2]          # modification en place
print(a)          # → [1, 2] : a est aussi modifié
b = b + [3]       # crée une nouvelle liste
print(a, b)       # → [1, 2] [1, 2, 3]
```

### 4.3 Opérateurs de comparaison

`==` (égal), `!=` (différent), `>`, `<`, `>=`, `<=`. Le résultat est un booléen. Les comparaisons peuvent être **chaînées**, comme en mathématiques, et chaque opérande n'est évalué qu'une fois :

```python
x = 5
print(1 < x < 10)          # → True  (équivaut à 1 < x and x < 10)
print(1 == 1.0)            # → True  (même valeur numérique)
print('abc' < 'abd')       # → True  (ordre lexicographique)
print([1, 2] < [1, 3])     # → True  (séquences comparées élément par élément)
try:
    1 < 'a'
except TypeError as erreur:
    print(erreur)          # → '<' not supported between instances of 'int' and 'str'
```

### 4.4 Opérateurs logiques

| Opérateur | Rôle |
| --- | --- |
| `and` | Vrai si les deux opérandes sont vrais |
| `or` | Vrai si au moins un opérande est vrai |
| `not` | Inverse la valeur de vérité |

Ils utilisent l'**évaluation paresseuse** (*short-circuit*) : l'opérande de droite n'est évalué que si nécessaire. Surtout, `and` et `or` **retournent l'un de leurs opérandes**, pas forcément un booléen : `a or b` renvoie `a` s'il est vrai, sinon `b` ; `a and b` renvoie `a` s'il est faux, sinon `b`. Seul `not` renvoie toujours un `bool`.

```python
utilisateur = ''
liste = []
nom = utilisateur or 'Anonyme'    # valeur par défaut
resultat = liste and liste[0]     # évite l'IndexError : liste[0] n'est pas évalué
print(nom)                        # → Anonyme
print(resultat)                   # → []
print(not 0, not 'a')             # → True False
print(any([0, '', 3]), all([1, 2, 0]))   # → True False
```

### 4.5 Opérateurs bit à bit

Ils agissent sur la représentation binaire des entiers.

| Opérateur | Nom | Exemple (`a = 5`, `b = 3`) |
| --- | --- | --- |
| `&` | ET | `5 & 3` → `1` |
| `\|` | OU | `5 \| 3` → `7` |
| `^` | OU exclusif | `5 ^ 3` → `6` |
| `~` | NON (complément) | `~5` → `-6` |
| `<<` | Décalage à gauche | `5 << 1` → `10` |
| `>>` | Décalage à droite | `5 >> 1` → `2` |

```python
print(bin(5), bin(3), bin(5 & 3))   # → 0b101 0b11 0b1
print(~5)                           # → -6  (~x vaut -x - 1)
LECTURE, ECRITURE = 0b01, 0b10
droits = LECTURE | ECRITURE         # combine des indicateurs (flags)
print(bool(droits & ECRITURE))      # → True : test d'un bit
```

Un décalage à gauche de `n` bits multiplie par `2**n`, un décalage à droite divise par `2**n` (division entière). Usages : masques, indicateurs, protocoles binaires.

### 4.6 Opérateurs d'identité et d'appartenance

```python
a = [1, 2]
b = [1, 2]
print(a == b)       # → True  : mêmes valeurs
print(a is b)       # → False : objets différents
x = None
print(x is None)    # → True  : comparaison correcte avec None
print(x is not None) # → False
```

Les opérateurs `in` et `not in` testent l'**appartenance** : élément dans une séquence ou un ensemble, **clé** dans un dictionnaire, **sous-chaîne** dans une chaîne.

```python
print('a' in 'banane')          # → True
print(3 in [1, 2, 3])           # → True
print('clé' in {'clé': 1})     # → True (teste les clés)
print(5 not in {1, 2})          # → True
```

`in` est très rapide sur un `set` ou un `dict` (temps constant, O(1)) mais lent sur une `list` (parcours, O(n)).

### 4.7 Priorité et associativité

La **priorité** indique quel opérateur est appliqué en premier ; l'**associativité** règle les cas d'égalité (la plupart des opérateurs s'associent de gauche à droite, `**` de droite à gauche). De la plus haute à la plus basse priorité :

| Niveau | Opérateurs |
| --- | --- |
| 1 | `( )` parenthèses, appels `f()`, indices `x[i]`, attributs `x.a` |
| 2 | `**` (associatif à droite) |
| 3 | `+x`, `-x`, `~x` (unaires) |
| 4 | `*`, `/`, `//`, `%`, `@` |
| 5 | `+`, `-` |
| 6 | `<<`, `>>` |
| 7 | `&`, puis `^`, puis `\|` |
| 8 | `==`, `!=`, `<`, `>`, `<=`, `>=`, `in`, `not in`, `is`, `is not` |
| 9 | `not`, puis `and`, puis `or` |
| 10 | `a if c else b`, `lambda` |
| 11 | `:=` |

```python
print(2 ** 3 ** 2)    # → 512 : 2 ** (3 ** 2)
print(-2 ** 2)        # → -4  : -(2 ** 2)
print(2 + 3 * 4)      # → 14
print(10 - 5 - 2)     # → 3   : de gauche à droite
print(True or False and False)   # → True : and avant or
```

En cas de doute, **ajoutez des parenthèses** : elles coûtent peu et levènt toute ambiguïté.

### 4.8 Expressions et évaluation

Une expression s'évalue de l'intérieur vers l'extérieur, selon la priorité et l'associativité, de gauche à droite pour les arguments d'un appel.

```python
resultat = 3 * (4 + 2) ** 2 // 5 % 3 + 2
# (4 + 2) = 6 → 6 ** 2 = 36 → 3 * 36 = 108 → 108 // 5 = 21 → 21 % 3 = 0 → 0 + 2 = 2
print(resultat)   # → 2
```

Sont aussi des expressions : appels de fonction, compréhensions, expressions conditionnelles, expressions `lambda`.

### 4.9 Surcharge d'opérateurs (introduction)

Chaque opérateur correspond à une **méthode spéciale** (« dunder »). En les définissant dans une classe, on rend ses objets compatibles avec les opérateurs :

```python
class Vecteur:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, autre):
        return Vecteur(self.x + autre.x, self.y + autre.y)

    def __eq__(self, autre):
        return (self.x, self.y) == (autre.x, autre.y)

    def __repr__(self):
        return f'Vecteur({self.x}, {self.y})'

print(Vecteur(1, 2) + Vecteur(3, 4))        # → Vecteur(4, 6)
print(Vecteur(1, 2) == Vecteur(1, 2))       # → True
```

| Opérateur | Méthode |
| --- | --- |
| `+` `-` `*` `/` | `__add__`, `__sub__`, `__mul__`, `__truediv__` |
| `==` `!=` `<` `<=` `>` `>=` | `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__` |
| `len()` | `__len__` |
| `x[i]` | `__getitem__` |
| `in` | `__contains__` |

Quand l'opérande de gauche ne sait pas gérer l'opération, Python essaie la version **inversée** de l'opérande de droite (`__radd__`, `__rmul__`…). Voir le chapitre 16.

### 4.10 Pièges courants

1. **Imprécision des flottants** : `0.1 + 0.2 == 0.3` est faux ; comparez avec `math.isclose`.
2. **`is` contre `==`** : `==` pour les valeurs ; `is` uniquement pour `None`, `True`, `False`.
3. **Priorité de `not`** : `not 1 == 2` signifie `not (1 == 2)`.
4. **`and` / `or` retournent des opérandes**, ce qui surprend quand on attend un booléen.
5. **Division** : `/` donne toujours un `float` ; utilisez `//` pour un résultat entier.
6. **`+=` sur liste** modifie l'objet en place (voir 4.2).
7. **Valeur par défaut mutable** dans une fonction (chapitre 11).

### 4.11 Bonnes pratiques

```python
a, b, c, d, e = 'A', False, 'C', True, 'E'
r = a if b else c if d else e   # trop dense
print(r)                        # → C

if b:                           # plus clair
    r = a
elif d:
    r = c
else:
    r = e
print(r)                        # → C
```

- Utilisez des parenthèses pour clarifier, et gardez des expressions courtes.
- Préférez `is None` / `is not None` à `== None`.
- Évitez d'enchaîner plusieurs conditionnels (ternaires).

### À retenir (chapitre 4)

- `/` renvoie un `float`, `//` arrondit vers le bas, `%` suit le signe du diviseur, `**` est associatif à droite.
- `and` et `or` sont paresseux et renvoient un opérande.
- `==` compare les valeurs, `is` les identités ; `in` teste l'appartenance.
- En cas de doute sur la priorité, utilisez des parenthèses.

## 5. Entrées et sorties

**Objectifs du chapitre** : lire des données fournies par l'utilisateur ou par la ligne de commande, afficher des résultats proprement, maîtriser le formatage de texte, de nombres et de dates.

### 5.1 Introduction

Les **entrées/sorties** (E/S, *I/O*) permettent à un programme d'échanger des informations avec l'extérieur. Python manipule trois **flux standard** : l'entrée standard `sys.stdin` (le clavier, par défaut), la sortie standard `sys.stdout` (l'écran) et la sortie d'erreur `sys.stderr`. Séparer sortie normale et erreurs permet de rediriger l'une sans l'autre (`python prog.py > resultat.txt` laisse les erreurs à l'écran).

| Source / destination | Outils |
| --- | --- |
| Clavier / écran | `input()`, `print()` |
| Arguments de ligne de commande | `sys.argv`, `argparse` |
| Fichiers | `open()`, `pathlib` (chapitre 14) |
| Réseau | `socket`, `requests`, `httpx` |

### 5.2 Lire une saisie utilisateur

`input(invite)` affiche l'invite, attend que l'utilisateur appuie sur Entrée et **renvoie toujours une chaîne**, même si l'utilisateur tape un nombre : il faut la convertir.

```python
nom = input('Votre nom : ')             # saisie : Alice
age = int(input('Votre âge : '))        # saisie : 30
print(f'{nom}, dans 10 ans vous aurez {age + 10} ans')
# → Alice, dans 10 ans vous aurez 40 ans
```

#### Saisie robuste

L'utilisateur peut taper n'importe quoi : on valide la saisie dans une boucle.

```python
while True:
    try:
        age = int(input('Âge : '))   # saisies : abc, puis 25
        break
    except ValueError:
        print('Veuillez entrer un nombre entier.')
print(f'Âge retenu : {age}')           # → Âge retenu : 25
```

#### Plusieurs valeurs sur une ligne

```python
a, b = map(int, input('Deux entiers : ').split())   # saisie : 3 4
print(a + b)                                        # → 7
```

#### Mot de passe, flux et arguments

```python
from getpass import getpass
import sys

mdp = getpass('Mot de passe : ')     # saisie masquée
print(len(mdp))                      # n'affichez jamais le mot de passe lui-même
print(sys.argv)                      # → ['script.py'] : arguments de la ligne de commande
for ligne in sys.stdin:              # lecture de données redirigées (cat fichier | python prog.py)
    print(ligne.strip())
```

Pour de vrais programmes en ligne de commande, utilisez le module **`argparse`** (ou `typer`, `click`), qui gère options, valeurs par défaut, aide automatique et validation de types :

```python
import argparse

parseur = argparse.ArgumentParser(description='Salue quelqu\'un')
parseur.add_argument('nom', help='nom à saluer')
parseur.add_argument('--fois', type=int, default=1, help='nombre de répétitions')
args = parseur.parse_args(['Alice', '--fois', '2'])   # équivaut à : python prog.py Alice --fois 2
print(args.nom, args.fois)                             # → Alice 2
```

### 5.3 Afficher dans la console

```python
import sys

print('Texte')                                # → Texte
print('A', 'B', sep=' | ', end='!\n')         # → A | B!
print('Erreur !', file=sys.stderr)            # écrit sur stderr
```

`print()` convertit chaque argument avec `str()`. Pour déboguer, `repr()` (ou le suffixe `!r` dans une f-string) affiche la représentation « non ambiguë » : `print(repr('a\nb'))` montre les caractères d'échappement. Pour les structures imbriquées, le module `pprint` met en forme : `pprint.pprint(donnees)`.

### 5.4 Formater les sorties

#### F-strings (méthode recommandée)

Une f-string évalue des expressions placées entre accolades. Après `:` on indique un **spécificateur de format** de la forme `[remplissage][alignement][signe][#][0][largeur][séparateur][.précision][type]`.

```python
nom, prix = 'Café', 2.5
print(f'{nom:<10}|{prix:>8.2f}|')   # → Café      |    2.50|
print(f'{nom!r}')                   # → 'Café'   (conversion repr)
print(f'{2 + 3 = }')                # → 2 + 3 = 5
```

| Format | Effet | Exemple |
| --- | --- | --- |
| `:.2f` | 2 décimales | `f'{3.14159:.2f}'` → `3.14` |
| `:,` | Séparateur de milliers | `f'{1234567:,}'` → `1,234,567` |
| `:>10` | Aligné à droite sur 10 caractères |  |
| `:<10` | Aligné à gauche |  |
| `:^10` | Centré |  |
| `:*^10` | Centré, rempli avec `*` |  |
| `:05d` | Complété par des zéros | `f'{42:05d}'` → `00042` |
| `:+d` | Signe toujours affiché | `f'{5:+d}'` → `+5` |
| `:.1%` | Pourcentage | `f'{0.256:.1%}'` → `25.6%` |
| `:b` `:o` `:x` | Binaire, octal, hexadécimal | `f'{255:x}'` → `ff` |
| `:e` | Notation scientifique | `f'{12345.678:.2e}'` → `1.23e+04` |

La largeur et la précision peuvent être dynamiques : `f'{valeur:{largeur}.{precision}f}'`.

#### Autres méthodes (à connaître pour lire du code existant)

```python
print('{} a {} ans'.format('Alice', 30))     # → Alice a 30 ans   (str.format)
print('{nom} a {age} ans'.format(nom='Bob', age=25))
print('%s a %d ans' % ('Alice', 30))         # → Alice a 30 ans   (ancien style %)
```

#### Template strings (t-strings, Python 3.14+)

Une **t-string** (PEP 750) s'écrit comme une f-string avec le préfixe `t`, mais **n'est pas évaluée en chaîne** : elle produit un objet `Template` qui conserve séparément les morceaux de texte fixe et les valeurs interpolées. Le code qui reçoit le gabarit peut alors traiter chaque valeur de manière adaptée (échappement HTML, paramètres SQL, journalisation structurée), ce qui réduit les risques d'injection.

```python
from html import escape
from string.templatelib import Interpolation

def html_sur(gabarit):
    morceaux = []
    for element in gabarit:
        if isinstance(element, Interpolation):
            morceaux.append(escape(str(element.value)))   # valeur : échappée
        else:
            morceaux.append(element)                      # texte fixe : conservé
    return ''.join(morceaux)

saisie = '<script>'
print(html_sur(t'<p>{saisie}</p>'))   # → <p>&lt;script&gt;</p>
```

Une f-string, elle, donne directement la chaîne finale : une f-string ne doit donc jamais servir à construire une requête SQL ou du HTML à partir de données non fiables.

### 5.5 Formater les dates et heures

Le module `datetime` fournit `date`, `time`, `datetime` et `timedelta` (durée). `strftime` convertit une date en texte ; `strptime` fait l'inverse ; `isoformat()` produit le format normalisé ISO 8601.

```python
from datetime import datetime, timedelta

maintenant = datetime(2026, 10, 11, 14, 30, 0)
print(maintenant.strftime('%d/%m/%Y %H:%M:%S'))   # → 11/10/2026 14:30:00
print(maintenant.isoformat())                      # → 2026-10-11T14:30:00
date = datetime.strptime('25/12/2026', '%d/%m/%Y')
print(date)                                        # → 2026-12-25 00:00:00
print(date - maintenant)                           # → 75 days, 9:30:00
print(maintenant + timedelta(days=30))             # → 2026-11-10 14:30:00
```

| Code | Signification |
| --- | --- |
| `%d` `%m` `%Y` | Jour, mois, année sur 4 chiffres |
| `%H` `%M` `%S` | Heure (24 h), minute, seconde |
| `%A` `%B` | Nom du jour, du mois (selon la locale) |
| `%j` | Jour de l'année |

Pour les **fuseaux horaires**, utilisez `zoneinfo.ZoneInfo('Europe/Paris')` et manipulez de préférence des dates *conscientes* du fuseau (`datetime.now(tz)`), avec stockage en UTC.

### 5.6 Bonnes pratiques

- Validez et **convertissez** toujours les saisies ; ne faites jamais confiance à l'utilisateur.
- Utilisez les **f-strings** pour la lisibilité (et les t-strings pour les contextes sensibles).
- Envoyez les erreurs sur `stderr` ou utilisez le module `logging` (chapitre 13).
- Pour les programmes non interactifs, privilégiez les arguments en ligne de commande plutôt que `input()`.
- Ne présumez pas l'encodage de la console ; en cas de caractères accentués mal affichés, vérifiez `sys.stdout.encoding`.

### À retenir (chapitre 5)

- `input()` renvoie toujours un `str` : convertissez et validez.
- `print()` accepte `sep`, `end`, `file`, `flush`.
- Les f-strings et leur mini-langage de format couvrent presque tous les besoins ; les t-strings (3.14) servent à traiter les valeurs interpolées en sécurité.
- `datetime` + `strftime` / `strptime` pour les dates ; `zoneinfo` pour les fuseaux.

## 6. Structures de contrôle

**Objectifs du chapitre** : maîtriser les conditions, le filtrage par motifs et les boucles, et savoir choisir la bonne structure pour chaque situation.

### 6.1 Introduction

Par défaut, un programme s'exécute ligne par ligne, de haut en bas. Les **structures de contrôle** modifient cet ordre.

| Type | Instructions |
| --- | --- |
| **Séquence** | Exécution ligne par ligne |
| **Sélection** (choix) | `if` / `elif` / `else`, `match` / `case`, opérateur ternaire |
| **Itération** (répétition) | `for`, `while` |
| **Contrôle de boucle** | `break`, `continue`, `else` de boucle, `pass` |

### 6.2 Conditions : `if`, `elif`, `else`

L'instruction `if` exécute son bloc si la condition est vraie. Les clauses `elif` (« sinon si ») sont testées dans l'ordre ; la première condition vraie l'emporte et les suivantes ne sont pas évaluées. `else` est facultatif et capte tous les autres cas.

```python
note = 14

if note >= 16:
    print('Très bien')
elif note >= 12:
    print('Bien')           # → Bien
elif note >= 10:
    print('Passable')
else:
    print('Insuffisant')
```

Une condition peut être n'importe quelle expression : elle est évaluée comme un booléen (valeurs *truthy* et *falsy*, chapitre 3). On combine les tests avec `and`, `or`, `not` et on utilise les comparaisons chaînées (`10 <= note <= 20`). Les conditions peuvent s'imbriquer, mais une imbrication profonde nuit à la lisibilité (voir 6.11).

```python
liste = []
if liste:                # écrire if liste, pas if len(liste) > 0
    print('non vide')
else:
    print('vide')        # → vide
```

### 6.3 Opérateur ternaire

L'**expression conditionnelle** `valeur_si_vrai if condition else valeur_si_faux` est une expression (elle produit une valeur), contrairement au bloc `if`.

```python
age = 20
statut = 'majeur' if age >= 18 else 'mineur'
print(statut)   # → majeur
```

Réservez-la aux cas simples ; ne l'imbriquez pas.

### 6.4 Filtrage par motifs : `match` / `case` *(Python 3.10+)*

L'instruction `match` compare une valeur à une suite de **motifs** (*patterns*) et exécute le premier `case` qui correspond. C'est bien plus qu'un `switch` : elle peut **décomposer** des structures et **lier des variables** au passage.

Motifs courants : littéral (`200`), alternative (`301 | 302`), joker (`_`, qui correspond à tout), capture (un nom nu qui reçoit la valeur), séquence (`[x, y]`, `(a, *reste)`), correspondance (`{'x': x}`), classe (`Point(x=0)`), et **garde** (`case ... if condition`).

```python
def reponse_http(code):
    match code:
        case 200:
            return 'OK'
        case 301 | 302:
            return 'Redirection'
        case 404:
            return 'Introuvable'
        case _:
            return 'Code inconnu'

print(reponse_http(302))   # → Redirection
print(reponse_http(500))   # → Code inconnu
```

```python
def decrire(point):
    match point:
        case (0, 0):
            return 'Origine'
        case (x, 0):
            return f"Sur l'axe X à {x}"
        case {'x': x, 'y': y} if x == y:
            return 'Sur la diagonale'
        case [premier, *reste]:
            return f'Séquence commençant par {premier}'
        case _:
            return 'Autre'

print(decrire((5, 0)))              # → Sur l'axe X à 5
print(decrire({'x': 2, 'y': 2}))    # → Sur la diagonale
print(decrire([1, 2, 3]))           # → Séquence commençant par 1
print(decrire(42))                  # → Autre
```

**Attention** : un nom simple dans un `case` est une *capture*, pas une comparaison avec une variable existante. Pour comparer à une constante nommée, utilisez un nom pointé (`case Couleur.ROUGE:`).

### 6.5 L'instruction `pass`

`pass` ne fait rien ; elle occupe la place d'un bloc syntaxiquement obligatoire (corps de fonction ou de classe à écrire plus tard, `except` volontairement vide). On peut aussi employer `...` (`Ellipsis`) comme corps provisoire.

```python
def a_implementer():
    pass

class Vide:
    pass

print(a_implementer())   # → None
```

### 6.6 Boucles : vue d'ensemble

| Boucle | Usage |
| --- | --- |
| `for` | Parcourir un itérable, ou répéter un nombre de fois connu |
| `while` | Répéter tant qu'une condition est vraie |

Une **itération** est un passage dans le corps de la boucle.

### 6.7 La boucle `while`

Elle teste la condition **avant** chaque tour.

```python
compteur = 0
while compteur < 3:
    print(compteur)    # → 0, puis 1, puis 2
    compteur += 1
```

Veillez à ce que la condition finisse par devenir fausse, sinon la boucle est **infinie** (interrompez-la avec `Ctrl+C`). Une boucle infinie volontaire s'écrit `while True:` avec un `break`.

### 6.8 La boucle `for`

Elle parcourt les éléments d'un **itérable** (liste, chaîne, dictionnaire, fichier, `range`, générateur…). `range(début, fin, pas)` produit une suite d'entiers, **fin exclue**, sans la stocker en mémoire.

```python
for fruit in ['pomme', 'banane']:
    print(fruit)              # → pomme, puis banane

for i in range(5):            # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):     # 2, 4, 6, 8
    print(i)

for lettre in 'abc':          # une chaîne est itérable
    print(lettre)
```

#### Outils de parcours

```python
noms = ['Alice', 'Bob']
ages = [30, 25]

for i, nom in enumerate(noms, start=1):   # indice + valeur
    print(i, nom)                         # → 1 Alice, puis 2 Bob

for nom, age in zip(noms, ages):          # parcours parallèle
    print(nom, age)                       # → Alice 30, puis Bob 25

for x in reversed(noms):                  # sens inverse
    print(x)                              # → Bob, puis Alice

for x in sorted(ages):                    # tri
    print(x)                              # → 25, puis 30
```

`zip` s'arrête à la séquence la plus courte ; avec `strict=True` (3.10+) une `ValueError` est levée si les longueurs diffèrent :

```python
try:
    list(zip([1, 2, 3], ['a', 'b'], strict=True))
except ValueError as erreur:
    print(erreur)   # → zip() argument 2 is shorter than argument 1
```

### 6.9 `break`, `continue` et `else` de boucle

- `break` **quitte** immédiatement la boucle ;
- `continue` **passe** à l'itération suivante ;
- la clause `else` d'une boucle s'exécute **uniquement si la boucle s'est terminée normalement, sans `break`**.

```python
for n in range(10):
    if n == 3:
        continue
    if n == 6:
        break
    print(n)      # → 0 1 2 4 5 (un nombre par ligne)

for n in range(2, 10):
    if n == 7:
        print('Trouvé')   # → Trouvé
        break
else:
    print('Aucun 7')      # non exécuté : la boucle s'est arrêtée par break
```

Le `else` de boucle est utile pour les recherches : il traite le cas « non trouvé » sans variable indicatrice.

### 6.10 Boucles imbriquées et motifs

On peut placer une boucle dans une autre ; le corps interne s'exécute entièrement à chaque tour de la boucle externe. Le `break` ne quitte que la boucle la plus interne.

```python
for i in range(1, 4):
    print('*' * i)
# *
# **
# ***

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end='\t')
    print()
# 1   2   3
# 2   4   6
# 3   6   9
```

### 6.11 Bonnes pratiques

```python
# Imbrication excessive
def f(x):
    if x:
        if x > 0:
            return 'positif'

# Retour anticipé (clauses de garde)
def g(x):
    if not x or x <= 0:
        return None
    return 'positif'

print(g(3), g(-1))   # → positif None
```

- Préférez `for` à `while` quand le nombre d'itérations est connu ou quand on parcourt une collection.
- Évitez `range(len(liste))` : itérez directement ou utilisez `enumerate()`.
- Pour transformer ou filtrer une collection, préférez les **compréhensions**.
- Ne modifiez pas une liste pendant que vous la parcourez ; parcourez une copie ou construisez une nouvelle liste.
- Remplacez les cascades de `elif` portant sur une même valeur par `match` ou par un dictionnaire.

### À retenir (chapitre 6)

- `if` / `elif` / `else` pour choisir ; ternaire pour les cas simples ; `match` pour décomposer des structures.
- `for` parcourt un itérable, `while` répète tant qu'une condition est vraie.
- `break`, `continue` et le `else` de boucle contrôlent l'exécution.
- `enumerate`, `zip`, `reversed`, `sorted` rendent les parcours expressifs.

## 7. Dictionnaires

**Objectifs du chapitre** : comprendre le fonctionnement d'un dictionnaire, maîtriser création, accès, modification, parcours, fusion et compréhension, connaître les structures spécialisées du module `collections`.

### 7.1 Introduction

Un **dictionnaire** (`dict`) est une collection de paires **clé → valeur** : on retrouve une valeur à partir de sa clé, non de sa position. Caractéristiques :

- **mutable** et dynamique ;
- les clés sont **uniques** et doivent être **hachables** (voir 7.11) ;
- **ordonné par insertion** (garanti depuis Python 3.7) ;
- accès, ajout et suppression en temps **constant en moyenne** (O(1)), grâce à une **table de hachage**.

```python
personne = {'nom': 'Alice', 'age': 25, 'ville': 'Paris'}
print(personne)   # → {'nom': 'Alice', 'age': 25, 'ville': 'Paris'}
```

Le principe de la **table de hachage** : Python calcule une empreinte numérique de la clé (`hash(cle)`) et s'en sert pour savoir directement où la paire est stockée, sans parcourir toutes les entrées.

### 7.2 Créer un dictionnaire

```python
vide = {}
vide2 = dict()
d1 = {'a': 1, 'b': 2}
d2 = dict(a=1, b=2)                      # clés = identifiants valides
d3 = dict([('a', 1), ('b', 2)])          # liste de paires
d4 = dict(zip(['a', 'b'], [1, 2]))       # depuis deux listes
d5 = dict.fromkeys(['x', 'y'], 0)        # → {'x': 0, 'y': 0}
d6 = {n: n ** 2 for n in range(4)}       # compréhension
print(d6)   # → {0: 0, 1: 1, 2: 4, 3: 9}
```

### 7.3 Accéder aux éléments

```python
p = {'nom': 'Alice', 'age': 25}

print(p['nom'])                 # → Alice   (KeyError si la clé est absente)
print(p.get('ville'))           # → None
print(p.get('ville', 'N/A'))    # → N/A
```

Utilisez `get()` quand la clé peut manquer, et `[]` quand son absence est une erreur de programmation.

### 7.4 Ajouter, modifier, supprimer

```python
p = {'nom': 'Alice', 'age': 25}

p['ville'] = 'Paris'                # ajout
p['age'] = 26                       # modification
p.update({'age': 27, 'pays': 'FR'}) # fusion de plusieurs paires
p.setdefault('langue', 'fr')        # ajoute seulement si la clé est absente

del p['pays']                       # supprime (KeyError si absente)
age = p.pop('age')                  # supprime et retourne
print(age)                          # → 27
print(p.pop('age', None))           # → None (pas d'erreur avec une valeur par défaut)
print(p.popitem())                  # → ('langue', 'fr') : dernière paire ajoutée
p.clear()                           # vide le dictionnaire
```

### 7.5 Méthodes principales

| Méthode | Rôle |
| --- | --- |
| `keys()` | Vue des clés |
| `values()` | Vue des valeurs |
| `items()` | Vue des paires `(clé, valeur)` |
| `get(k, d)` | Valeur de `k`, ou `d` si absente |
| `setdefault(k, v)` | Ajoute si absente et retourne la valeur |
| `update(autre)` | Fusionne un autre dictionnaire |
| `pop(k[, d])` | Supprime et retourne |
| `popitem()` | Supprime et retourne la dernière paire |
| `copy()` | Copie superficielle |

Les **vues** (`keys`, `values`, `items`) sont dynamiques : elles reflètent les modifications ultérieures du dictionnaire. `keys()` et `items()` se comportent comme des ensembles (`d1.keys() & d2.keys()`).

### 7.6 Parcourir un dictionnaire

```python
p = {'nom': 'Alice', 'age': 25, 'ville': 'Paris'}

for cle in p:                       # clés
    print(cle)
for valeur in p.values():           # valeurs
    print(valeur)
for cle, valeur in p.items():       # paires
    print(f'{cle} = {valeur}')      # → nom = Alice, etc.
```

Ne modifiez pas la **taille** d'un dictionnaire pendant son parcours : une `RuntimeError` est levée. Parcourez `list(p)` si vous devez ajouter ou retirer des clés.

```python
p = {'nom': 'Alice'}
try:
    for cle in p:
        p['ville'] = 'Paris'
except RuntimeError as erreur:
    print(erreur)   # → dictionary changed size during iteration

for cle in list(p):   # parcours d'une copie des clés : sans danger
    p[cle + '_copie'] = p[cle]
```

### 7.7 Compréhensions de dictionnaires

```python
carres = {n: n ** 2 for n in range(5)}
pairs = {k: v for k, v in carres.items() if v % 2 == 0}
inverse = {v: k for k, v in carres.items()}
print(carres)    # → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(pairs)     # → {0: 0, 2: 4, 4: 16}
print(inverse)   # → {0: 0, 1: 1, 4: 2, 9: 3, 16: 4}
```

### 7.8 Test d'appartenance

```python
p = {'nom': 'Alice', 'age': 25}
print('nom' in p)             # → True : teste les clés, en O(1)
print('Alice' in p.values())  # → True : teste les valeurs, en O(n)
```

### 7.9 Dictionnaires imbriqués

Les valeurs peuvent être n'importe quel objet, y compris des listes et d'autres dictionnaires : c'est la structure de base des données JSON.

```python
users = {
    'alice': {'age': 25, 'langues': ['fr', 'en']},
    'bob':   {'age': 30, 'langues': ['fr']},
}
print(users['alice']['langues'][0])   # → fr
users['bob']['ville'] = 'Lyon'
print(users['bob'])   # → {'age': 30, 'langues': ['fr'], 'ville': 'Lyon'}
```

### 7.10 Fusionner des dictionnaires

```python
a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(a | b)        # → {'x': 1, 'y': 3, 'z': 4}   (3.9+)
print({**a, **b})   # → {'x': 1, 'y': 3, 'z': 4}   (déballage)
a |= b              # fusion en place
```

En cas de clé commune, **la dernière valeur l'emporte**.

### 7.11 Clés hachables

Un objet est **hachable** s'il possède une empreinte (`__hash__`) qui ne change jamais pendant sa vie et s'il est comparable (`__eq__`) : deux objets égaux ont la même empreinte. Cela impose en pratique des objets **immuables** : `str`, `int`, `float`, `bool`, `tuple` (de valeurs hachables), `frozenset`.

```python
print({(1, 2): 'point'})   # → {(1, 2): 'point'}

try:
    {[1, 2]: 'x'}          # une liste n'est pas hachable
except TypeError as erreur:
    print(erreur)          # → unhashable type: 'list'
```

Attention : `1`, `1.0` et `True` sont égaux et de même empreinte, donc ils désignent la **même clé**.

### 7.12 Le module `collections`

```python
from collections import defaultdict, Counter, ChainMap

groupes = defaultdict(list)               # valeur par défaut créée automatiquement
for mot in ['chat', 'chien', 'souris']:
    groupes[mot[0]].append(mot)
print(dict(groupes))    # → {'c': ['chat', 'chien'], 's': ['souris']}

c = Counter('abracadabra')                # compteur d'occurrences
print(c.most_common(2)) # → [('a', 5), ('b', 2)]

reglages = ChainMap({'theme': 'sombre'}, {'theme': 'clair', 'langue': 'fr'})
print(reglages['langue'], reglages['theme'])   # → fr sombre (recherche en cascade)
```

`OrderedDict` n'est plus nécessaire pour conserver l'ordre (le `dict` natif le fait) mais reste utile pour `move_to_end()` et pour une comparaison sensible à l'ordre.

### 7.13 Dictionnaires et JSON

```python
import json

texte = json.dumps({'nom': 'Alice', 'age': 25}, indent=2, ensure_ascii=False)
donnees = json.loads(texte)
print(donnees)   # → {'nom': 'Alice', 'age': 25}
```

`dumps` convertit un objet Python en texte JSON, `loads` fait l'inverse ; `dump` et `load` travaillent avec des fichiers (chapitre 14). Les clés JSON sont toujours des chaînes.

### 7.14 Performances

| Opération | Complexité moyenne |
| --- | --- |
| Accès `d[k]`, insertion, suppression | O(1) |
| `k in d` | O(1) |
| Parcours complet | O(n) |
| `v in d.values()` | O(n) |

### 7.15 Idiomes utiles

```python
scores = {'alice': 12, 'bob': 17, 'chloé': 9}
ages = {'alice': 25, 'bob': 15, 'chloé': 31}

print(dict(sorted(scores.items(), key=lambda kv: kv[1])))   # tri par valeur
print(max(scores, key=scores.get))                          # → bob (clé de la plus grande valeur)
print({n: a for n, a in ages.items() if a >= 18})           # filtre

freq = {}
for ch in 'banane':
    freq[ch] = freq.get(ch, 0) + 1                          # compter
print(freq)   # → {'b': 1, 'a': 2, 'n': 2, 'e': 1}
```

Pour des données structurées à clés fixes, préférez un `dataclass` ou un `TypedDict` (chapitres 16 et 17).

### À retenir (chapitre 7)

- Un `dict` associe des clés hachables uniques à des valeurs ; il conserve l'ordre d'insertion.
- `d[k]` lève `KeyError`, `d.get(k, défaut)` non.
- `keys`, `values`, `items` donnent des vues ; ne changez pas la taille pendant un parcours.
- `|` fusionne, les compréhensions transforment, `defaultdict` et `Counter` simplifient les regroupements et comptages.

## 8. Listes

**Objectifs du chapitre** : maîtriser la structure de données la plus utilisée de Python : création, indexation, tranches, modification, tri, compréhensions, copies et pièges liés à la mutabilité.

### 8.1 Introduction

Une **liste** (`list`) est une collection **ordonnée** et **mutable**. Elle peut contenir des éléments de types différents, des doublons, et d'autres listes. Chaque élément possède un **indice** (sa position), à partir de 0. En interne, c'est un tableau dynamique de références : l'accès par indice est en O(1), l'ajout en fin est en O(1) amorti, l'insertion ou la suppression au début est en O(n).

```python
fruits = ['pomme', 'banane', 'cerise']
melange = [1, 'deux', 3.0, [4, 5]]
print(melange)   # → [1, 'deux', 3.0, [4, 5]]
```

### 8.2 Créer des listes

```python
vide = []
a = list('abc')                   # → ['a', 'b', 'c']
b = list(range(5))                # → [0, 1, 2, 3, 4]
c = [0] * 3                       # → [0, 0, 0]
d = [x ** 2 for x in range(5)]    # compréhension → [0, 1, 4, 9, 16]
```

### 8.3 Accéder aux éléments

```python
l = [10, 20, 30, 40, 50]
print(l[0], l[-1])    # → 10 50
print(l[1:4])         # → [20, 30, 40]
print(l[::2])         # → [10, 30, 50]
print(l[::-1])        # → [50, 40, 30, 20, 10]
```

La syntaxe d'une **tranche** (*slice*) est `liste[début:fin:pas]` : début inclus, fin **exclue**, chaque borne facultative. Une tranche renvoie toujours une **nouvelle** liste et ne lève jamais d'`IndexError` ; un indice simple hors limites, lui, en lève une.

### 8.4 Modifier une liste

```python
l = [10, 20, 30, 40, 50]
l[0] = 11
l[1:3] = [21, 31, 35]     # remplace une tranche (la taille peut changer)
print(l)                  # → [11, 21, 31, 35, 40, 50]
```

### 8.5 Ajouter des éléments

```python
l = [1, 2]
l.append(3)            # ajoute un élément à la fin
l.insert(0, 0)         # insère à l'indice 0
l.extend([4, 5])       # ajoute plusieurs éléments
l += [6]               # équivalent à extend
print(l)               # → [0, 1, 2, 3, 4, 5, 6]

x = [0]; x.append([1, 2]); print(x)   # → [0, [1, 2]]  (une sous-liste)
y = [0]; y.extend([1, 2]); print(y)   # → [0, 1, 2]    (deux éléments)
```

### 8.6 Supprimer des éléments

```python
l = [10, 20, 30, 40, 50, 60]
l.remove(30)           # supprime la 1re occurrence de la valeur
dernier = l.pop()      # retire et retourne le dernier → 60
premier = l.pop(0)     # retire par indice → 10
del l[0]               # supprime par indice
del l[0:1]             # supprime une tranche
l.clear()              # vide la liste

try:
    l.remove(99)
except ValueError as erreur:
    print(erreur)      # → list.remove(x): x not in list
```

### 8.7 Rechercher

```python
l = [3, 1, 4, 1, 5]
print(4 in l)          # → True    (parcours, O(n))
print(l.index(1))      # → 1       (première occurrence ; ValueError si absent)
print(l.count(1))      # → 2
```

Pour des recherches fréquentes, utilisez un `set` ou un `dict`, ou le module `bisect` sur une liste **triée**.

### 8.8 Trier et inverser

```python
l = ['pomme', 'kiwi', 'banane', 'fig']
l.sort()                      # tri en place → ['banane', 'fig', 'kiwi', 'pomme']
l.sort(key=len)               # selon une clé → ['fig', 'kiwi', 'pomme', 'banane']
l.sort(reverse=True)          # ordre décroissant
nouvelle = sorted(l)          # NOUVELLE liste triée ; l n'est pas modifiée
l.reverse()                   # inverse en place
inverse = l[::-1]             # copie inversée
```

`list.sort()` modifie la liste et renvoie `None` ; `sorted()` accepte n'importe quel itérable et renvoie une nouvelle liste. Le tri est **stable** : les éléments égaux gardent leur ordre relatif, ce qui permet de trier en plusieurs passes. Le paramètre `key` est une fonction appliquée à chaque élément pour obtenir la valeur de comparaison.

```python
personnes = [('Alice', 30), ('Bob', 25), ('Chloé', 30)]
personnes.sort(key=lambda p: (-p[1], p[0]))   # âge décroissant, puis nom
print(personnes)   # → [('Alice', 30), ('Chloé', 30), ('Bob', 25)]
```

### 8.9 Fonctions et méthodes utiles

| Fonction | Rôle |
| --- | --- |
| `len(l)` | Nombre d'éléments |
| `sum(l)`, `min(l)`, `max(l)` | Somme, minimum, maximum |
| `any(l)`, `all(l)` | Au moins un / tous éléments vrais |
| `sorted(l)`, `reversed(l)` | Tri / inversion |
| `enumerate(l)`, `zip(a, b)` | Parcours enrichis |

Méthodes de `list` : `append`, `extend`, `insert`, `remove`, `pop`, `clear`, `index`, `count`, `sort`, `reverse`, `copy`.

### 8.10 Compréhensions de listes

Une **compréhension** construit une liste à partir d'un itérable en une expression : `[expression for variable in itérable if condition]`.

```python
carres = [x ** 2 for x in range(10)]
pairs = [x for x in range(10) if x % 2 == 0]
etiquettes = ['pair' if x % 2 == 0 else 'impair' for x in range(4)]
matrice = [[1, 2], [3, 4]]
aplatie = [x for ligne in matrice for x in ligne]   # boucles imbriquées
print(aplatie)   # → [1, 2, 3, 4]
```

La variable de boucle est **locale** à la compréhension. Si l'expression devient trop longue ou nécessite plusieurs instructions, utilisez une boucle classique.

### 8.11 Copier une liste

Affecter une liste à un autre nom ne copie rien (alias). Une **copie superficielle** duplique la liste mais pas les objets qu'elle contient ; une **copie profonde** duplique tout.

```python
import copy

a = [1, 2, [3, 4]]
b = a                   # alias : même objet
c = a.copy()            # copie superficielle (équivalent : a[:] ou list(a))
d = copy.deepcopy(a)    # copie profonde

c[2].append(5)          # la sous-liste est partagée entre a et c
print(a)                # → [1, 2, [3, 4, 5]]
print(d)                # → [1, 2, [3, 4]]
print(b is a)           # → True
```

### 8.12 Listes imbriquées

```python
matrice = [[1, 2, 3], [4, 5, 6]]
print(matrice[1][2])                 # → 6

grille = [[0] * 3 for _ in range(3)] # création correcte : 3 lignes distinctes
grille[0][0] = 1
print(grille)                        # → [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

mauvaise = [[0] * 3] * 3             # piège : 3 références vers la MÊME ligne
mauvaise[0][0] = 1
print(mauvaise)                      # → [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
```

Pour le calcul numérique sur matrices, utilisez **NumPy**.

### 8.13 Déballage de listes

```python
a, b, c = [1, 2, 3]
premier, *milieu, dernier = [1, 2, 3, 4, 5]
print(premier, milieu, dernier)   # → 1 [2, 3, 4] 5

def somme(x, y, z):
    return x + y + z
print(somme(*[1, 2, 3]))          # → 6 (déballage dans un appel)
```

### 8.14 Outils fonctionnels

```python
from functools import reduce

nombres = [1, 2, 3, 4]
print(list(map(lambda x: x * 2, nombres)))        # → [2, 4, 6, 8]
print(list(filter(lambda x: x % 2 == 0, nombres)))# → [2, 4]
print(reduce(lambda a, b: a * b, nombres))        # → 24
```

Les compréhensions sont généralement plus lisibles que `map` et `filter`.

### 8.15 Listes et chaînes

```python
mots = 'un deux trois'.split()     # → ['un', 'deux', 'trois']
print(' '.join(mots))             # → un deux trois
print(list('abc'))                # → ['a', 'b', 'c']
```

### 8.16 Comparaison des collections

| Critère | `list` | `tuple` | `set` | `dict` |
| --- | --- | --- | --- | --- |
| Ordonné | Oui | Oui | Non | Oui (insertion) |
| Mutable | Oui | Non | Oui | Oui |
| Doublons | Oui | Oui | Non | Clés uniques |
| Accès par indice | Oui | Oui | Non | Par clé |
| Test `in` | O(n) | O(n) | O(1) | O(1) |

Pour une **file** (ajouts et retraits aux deux extrémités), utilisez `collections.deque` : `append()` et `popleft()` y sont en O(1), alors que `list.pop(0)` est en O(n).

### À retenir (chapitre 8)

- Une liste est ordonnée et mutable ; les tranches sont `[début:fin:pas]` avec fin exclue.
- `append` ajoute un élément, `extend` plusieurs ; `sort` modifie, `sorted` renvoie une copie.
- Copiez avec `.copy()` (superficielle) ou `deepcopy` (profonde) ; méfiez-vous des alias et de `[[0] * 3] * 3`.
- Les compréhensions sont l'outil privilégié de transformation et de filtrage.

## 9. Ensembles

**Objectifs du chapitre** : utiliser les ensembles pour éliminer des doublons, tester l'appartenance rapidement et appliquer les opérations mathématiques (union, intersection, différence).

### 9.1 Introduction

Un **ensemble** (`set`) est une collection **non ordonnée** d'éléments **uniques** et **hachables**. Il est **mutable**. Comme les dictionnaires, il repose sur une table de hachage : test d'appartenance, ajout et suppression en O(1) en moyenne.

```python
fruits = {'pomme', 'banane', 'pomme'}
print(fruits)   # → {'pomme', 'banane'} (doublon supprimé ; l'ordre d'affichage peut varier)
```

### 9.2 Créer des ensembles

```python
s = {1, 2, 3}
vide = set()                         # ATTENTION : {} crée un dictionnaire
a = set([1, 2, 2, 3])                # → {1, 2, 3}
b = set('abca')                      # → {'a', 'b', 'c'}
c = {x ** 2 for x in range(5)}       # compréhension d'ensemble
print(type({}), type(vide))          # → <class 'dict'> <class 'set'>
```

### 9.3 Accéder aux éléments

Il n'y a pas d'indice : `s[0]` lève une `TypeError`. On parcourt l'ensemble avec `for` ou on teste l'appartenance avec `in`. L'ordre de parcours n'est pas garanti.

```python
s = {1, 2, 3}
print(2 in s)   # → True
try:
    s[0]
except TypeError as erreur:
    print(erreur)   # → 'set' object is not subscriptable
```

### 9.4 Ajouter et supprimer

```python
s = {1, 2, 3}
s.add(4)
s.update([5, 6])         # ajoute plusieurs éléments
s.remove(4)               # KeyError si absent
s.discard(99)             # aucune erreur si absent
x = s.pop()               # retire un élément arbitraire
s.clear()
```

### 9.5 Opérations ensemblistes

| Opération | Opérateur | Méthode |
| --- | --- | --- |
| Union | `a \| b` | `a.union(b)` |
| Intersection | `a & b` | `a.intersection(b)` |
| Différence | `a - b` | `a.difference(b)` |
| Différence symétrique | `a ^ b` | `a.symmetric_difference(b)` |

```python
a = {1, 2, 3}
b = {3, 4}
print(a | b)   # → {1, 2, 3, 4}
print(a & b)   # → {3}
print(a - b)   # → {1, 2}
print(a ^ b)   # → {1, 2, 4}
```

Les versions « en place » sont `|=`, `&=`, `-=`, `^=` (ou `update`, `intersection_update`, etc.). Les méthodes acceptent n'importe quel itérable, pas seulement des ensembles.

### 9.6 Comparaisons et sous-ensembles

```python
print({1, 2} <= {1, 2, 3})         # → True  : sous-ensemble (issubset)
print({1, 2} < {1, 2})             # → False : sous-ensemble strict
print({1, 2, 3} >= {1, 2})         # → True  : sur-ensemble (issuperset)
print({1, 2}.isdisjoint({3, 4}))   # → True  : aucun élément commun
```

### 9.7 Ensembles figés (`frozenset`)

Un `frozenset` est la version **immuable** et **hachable** d'un ensemble : on peut l'utiliser comme clé de dictionnaire ou comme élément d'un autre ensemble.

```python
fs = frozenset([1, 2, 3])
try:
    fs.add(4)
except AttributeError as erreur:
    print(erreur)   # → 'frozenset' object has no attribute 'add'
```

### 9.8 Cas d'usage

```python
liste = [3, 1, 3, 2, 1]

print(sorted(set(liste)))              # supprimer les doublons → [1, 2, 3]
print(list(dict.fromkeys(liste)))      # sans doublons, ordre conservé → [3, 1, 2]
print({1, 2, 3} & {2, 3, 4})           # éléments communs → {2, 3}

interdits = {'admin', 'root'}
if 'admin' in interdits:               # recherche rapide
    print('Nom interdit')
```

### 9.9 Pièges et bonnes pratiques

- `{}` crée un **dictionnaire** ; utilisez `set()` pour un ensemble vide.
- Les éléments doivent être **hachables** : `{[1, 2]}` lève une `TypeError` ; utilisez des tuples ou des `frozenset`.
- **Ne comptez jamais sur l'ordre** d'un ensemble.
- Employez les ensembles pour les tests d'appartenance fréquents et les comparaisons de collections.

### À retenir (chapitre 9)

- Un `set` contient des éléments uniques, hachables, sans ordre ; `set()` crée un ensemble vide.
- `| & - ^` donnent union, intersection, différence, différence symétrique.
- `frozenset` est la variante immuable et hachable.

## 10. Tuples

**Objectifs du chapitre** : comprendre le rôle des séquences immuables, maîtriser le déballage, et savoir quand choisir un tuple plutôt qu'une liste.

### 10.1 Introduction

Un **tuple** est une séquence **ordonnée** et **immuable**. Il regroupe typiquement un nombre fixe de valeurs liées, de types éventuellement différents (coordonnées, enregistrement).

### 10.2 Créer des tuples

Ce sont les **virgules** qui créent un tuple, pas les parenthèses.

```python
t = (1, 2, 3)
sans_parentheses = 1, 2, 3
vide = ()
singleton = (5,)           # la virgule est OBLIGATOIRE pour un seul élément
pas_un_tuple = (5)         # simplement un entier
depuis_liste = tuple([1, 2, 3])
print(type(singleton), type(pas_un_tuple))   # → <class 'tuple'> <class 'int'>
```

### 10.3 Accès et tranches

```python
t = ('a', 'b', 'c', 'd')
print(t[0], t[-1])   # → a d
print(t[1:3])        # → ('b', 'c')
```

### 10.4 Opérations et méthodes

```python
print((1, 2) + (3,))    # → (1, 2, 3)
print((0,) * 3)         # → (0, 0, 0)
print(2 in (1, 2, 3))   # → True
t = (1, 2, 2, 3)
print(t.count(2), t.index(3))   # → 2 3
```

Un tuple n'a que **deux méthodes** : `count()` et `index()`. Les tuples se comparent lexicographiquement et se trient (`sorted`), ce qui les rend pratiques comme clés de tri.

### 10.5 Déballage (*unpacking*)

Le **déballage** affecte les éléments d'une séquence à plusieurs variables en une instruction. Il fonctionne avec toute séquence ou itérable, pas seulement les tuples.

```python
x, y = (10, 20)
a, *reste = (1, 2, 3, 4)
print(a, reste)            # → 1 [2, 3, 4]
x, y = y, x                # échange
print(x, y)                # → 20 10

def min_max(valeurs):
    return min(valeurs), max(valeurs)   # retourne un tuple
mini, maxi = min_max([3, 1, 4])
print(mini, maxi)          # → 1 4

(a, b), (c, d) = (1, 2), (3, 4)         # déballage imbriqué
```

Le `*` capture le « reste » sous forme de liste ; il ne peut apparaître qu'une fois par déballage. `_` sert par convention à ignorer une valeur.

### 10.6 Immuabilité

On ne peut ni ajouter, ni retirer, ni remplacer un élément d'un tuple. Mais l'immuabilité est **superficielle** : un objet mutable contenu dans un tuple reste modifiable.

```python
t = (1, [2, 3])
t[1].append(4)
print(t)             # → (1, [2, 3, 4])
try:
    t[0] = 9
except TypeError as erreur:
    print(erreur)    # → 'tuple' object does not support item assignment
```

### 10.7 Tuples comme clés de dictionnaire

Un tuple est **hachable** si tous ses éléments le sont, ce qui permet des clés composées.

```python
distances = {(48.85, 2.35): 'Paris', (45.76, 4.84): 'Lyon'}
print(distances[(48.85, 2.35)])   # → Paris
```

### 10.8 Tuples ou listes ?

| Critère | Tuple | Liste |
| --- | --- | --- |
| Mutable | Non | Oui |
| Hachable (clé de dict) | Oui, si le contenu l'est | Non |
| Mémoire / vitesse | Plus léger, plus rapide | Plus lourde |
| Usage typique | Données hétérogènes de taille fixe (enregistrement) | Collection homogène de taille variable |

### 10.9 Cas d'usage

- Retourner **plusieurs valeurs** depuis une fonction ;
- constantes (jours, couleurs RVB) et paramètres fixes ;
- `*args` : les arguments positionnels variables forment un tuple ;
- `enumerate()` et `zip()` produisent des tuples ;
- clés composites de dictionnaires, éléments d'ensembles.

### 10.10 Tuples nommés

Un **tuple nommé** permet d'accéder aux éléments par un nom en plus de l'indice, tout en restant un tuple immuable.

```python
from collections import namedtuple
from typing import NamedTuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p[1])      # → 3 4

class Coordonnee(NamedTuple):      # version typée (recommandée)
    x: float
    y: float = 0.0

print(Coordonnee(3))               # → Coordonnee(x=3, y=0.0)
```

### 10.11 Erreurs courantes

| Erreur | Cause | Solution |
| --- | --- | --- |
| `TypeError: 'tuple' object does not support item assignment` | Modification d'un tuple | Créer un nouveau tuple, ou utiliser une liste |
| `ValueError: too many values to unpack` | Nombre de variables ≠ nombre d'éléments | Ajuster ou utiliser `*reste` |
| Singleton sans virgule | `(5)` n'est pas un tuple | Écrire `(5,)` |
| Clé de dict non hachable | Tuple contenant une liste | Convertir en sous-tuples |
| `IndexError` | Indice hors limites | Vérifier `len(t)` ou utiliser une tranche |

### À retenir (chapitre 10)

- Un tuple est une séquence immuable ; la virgule le crée, `(5,)` pour un seul élément.
- Le déballage (`a, b = t`, `a, *reste = t`) est un idiome central.
- Hachable si son contenu l'est : utilisable comme clé.
- `NamedTuple` ajoute des noms de champs et des types.

## 11. Fonctions

**Objectifs du chapitre** : définir et appeler des fonctions, maîtriser tous les types de paramètres, comprendre portée, fermetures, décorateurs, récursivité, annotations et docstrings.

### 11.1 Introduction

Une **fonction** est un bloc de code nommé et réutilisable qui réalise une tâche précise. Elle évite la répétition (principe DRY), structure le programme et facilite les tests. On distingue la **définition** (avec `def`, qui crée l'objet fonction) de l'**appel** (qui l'exécute).

```python
def saluer(nom):
    """Affiche un message de salutation."""
    print(f'Bonjour {nom} !')

saluer('Alice')   # → Bonjour Alice !
```

Syntaxe générale : `def nom(paramètres): docstring, corps, return`. Un **paramètre** est le nom déclaré dans la définition ; un **argument** est la valeur fournie à l'appel. Convention : nom en `snake_case`, commençant par un verbe (`calculer_total`, `est_valide`).

### 11.2 Paramètres et arguments

```python
def presenter(nom, age=18, *hobbies, ville='Paris', **autres):
    print(nom, age, hobbies, ville, autres)

presenter('Alice', 30, 'lecture', 'vélo', ville='Lyon', pays='FR')
# → Alice 30 ('lecture', 'vélo') Lyon {'pays': 'FR'}
```

| Type | Exemple | Remarque |
| --- | --- | --- |
| **Positionnels** | `f(1, 2)` | Attribués selon l'ordre |
| **Nommés** (mots-clés) | `f(b=2, a=1)` | Ordre libre |
| **Valeurs par défaut** | `def f(x, y=10)` | Les paramètres par défaut viennent après les autres |
| **`*args`** | `def f(*args)` | Arguments positionnels supplémentaires, collectés dans un tuple |
| **`**kwargs`** | `def f(**kwargs)` | Arguments nommés supplémentaires, collectés dans un dict |

#### Paramètres positionnels seuls et nommés seuls

```python
def combiner(a, b, /, c, d, *, e, f):
    return (a, b, c, d, e, f)

# a, b : positionnels seulement (avant /)
# c, d : positionnels ou nommés
# e, f : nommés seulement (après *)
print(combiner(1, 2, 3, d=4, e=5, f=6))   # → (1, 2, 3, 4, 5, 6)
```

Ordre des paramètres : `positionnels seuls, /, normaux, valeurs par défaut, *args, nommés seuls, **kwargs`.

#### Piège : valeur par défaut mutable

Une valeur par défaut est évaluée **une seule fois**, à la définition de la fonction. Un objet mutable est donc partagé entre tous les appels.

```python
def ajouter(x, liste=[]):          # piège
    liste.append(x)
    return liste

print(ajouter(1))   # → [1]
print(ajouter(2))   # → [1, 2] : la liste du premier appel est réutilisée

def ajouter_ok(x, liste=None):     # correct
    if liste is None:
        liste = []
    liste.append(x)
    return liste

print(ajouter_ok(1), ajouter_ok(2))   # → [1] [2]
```

#### Déballage à l'appel

```python
def somme(a, b, c):
    return a + b + c

print(somme(*[1, 2, 3]))                    # → 6
print(somme(**{'a': 1, 'b': 2, 'c': 3}))    # → 6
```

**Passage des arguments.** Python passe des **références d'objets** (*pass by assignment*) : la fonction reçoit un nom lié au même objet que l'appelant. Modifier un objet mutable reçu se voit à l'extérieur ; réaffecter le paramètre, non.

```python
def modifier(l):
    l.append(99)      # modifie l'objet de l'appelant
    l = [0]           # réaffectation locale : sans effet à l'extérieur

maliste = [1]
modifier(maliste)
print(maliste)        # → [1, 99]
```

### 11.3 Valeurs de retour

`return` termine la fonction et renvoie une valeur. Plusieurs valeurs renvoyées forment un **tuple**. Sans `return` (ou avec `return` seul), la fonction renvoie `None`.

```python
def division(a, b):
    if b == 0:
        return None          # retour anticipé
    return a / b

def min_max(l):
    return min(l), max(l)    # un tuple

mini, maxi = min_max([3, 1, 4])
print(division(6, 3), division(1, 0), mini, maxi)   # → 2.0 None 1 4
```

### 11.4 Portée et durée de vie

```python
x = 10                    # globale

def g():
    global x              # modifie la globale (à éviter)
    x += 1

def externe():
    n = 0
    def interne():
        nonlocal n        # modifie la variable de la fonction englobante
        n += 1
    interne()
    return n

g()
print(x)                  # → 11
print(externe())          # → 1
```

Les variables locales sont créées à chaque appel et **disparaissent à sa fin**. Lire une variable globale est possible sans déclaration ; l'**affecter** exige `global`. Un nom affecté quelque part dans une fonction est local dans *toute* la fonction : le lire avant l'affectation provoque une `UnboundLocalError`.

### 11.5 Fonctions anonymes (`lambda`)

Une **lambda** est une fonction sans nom, limitée à **une seule expression** dont le résultat est renvoyé.

```python
carre = lambda x: x ** 2
print(carre(4))   # → 16

personnes = [{'nom': 'Alice', 'age': 30}, {'nom': 'Bob', 'age': 25}]
personnes.sort(key=lambda p: p['age'])
print(personnes[0]['nom'])   # → Bob
```

Utilisez-les pour de petites fonctions jetables (clés de tri, rappels) ; pour toute logique non triviale, écrivez un `def`.

### 11.6 Fonctions d'ordre supérieur et fermetures

Les fonctions sont des **objets de première classe** : on peut les affecter, les passer en argument, les retourner, les stocker dans des structures. Une fonction qui prend ou renvoie une fonction est dite **d'ordre supérieur**.

```python
def appliquer(f, valeur):
    return f(valeur)

print(appliquer(str.upper, 'salut'))   # → SALUT

def multiplicateur(n):
    def fois(x):          # fermeture (closure)
        return x * n
    return fois

triple = multiplicateur(3)
print(triple(5))          # → 15
```

Une **fermeture** est une fonction interne qui conserve l'accès aux variables de la fonction englobante, même après la fin de celle-ci.

#### Le module `functools`

```python
from functools import partial, cache

double = partial(pow, 2)     # fixe le 1er argument : double(x) = pow(2, x)
print(double(5))             # → 32

@cache                       # mémoïsation (3.9+) : résultats mémorisés
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(30))               # → 832040
```

### 11.7 Décorateurs

Un **décorateur** est une fonction qui prend une fonction et renvoie une version modifiée. La notation `@decorateur` au-dessus d'un `def` est équivalente à `f = decorateur(f)`.

```python
import functools
import time

def chronometre(fonction):
    @functools.wraps(fonction)           # conserve nom et docstring
    def enveloppe(*args, **kwargs):
        debut = time.perf_counter()
        resultat = fonction(*args, **kwargs)
        print(f'{fonction.__name__} : {time.perf_counter() - debut:.4f} s')
        return resultat
    return enveloppe

@chronometre
def calcul():
    return sum(range(1_000_000))

print(calcul())   # affiche la durée (variable), puis 499999500000
```

#### Décorateur avec paramètres

Il faut un niveau d'imbrication supplémentaire : une fonction qui renvoie le décorateur.

```python
import functools

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
    print('Salut')

dire_salut()   # affiche Salut trois fois
```

Décorateurs intégrés à connaître : `@staticmethod`, `@classmethod`, `@property`, `@functools.cache`, `@dataclass`, `@abstractmethod`.

### 11.8 Récursivité

Une fonction **récursive** s'appelle elle-même. Elle doit comporter un **cas de base** (qui arrête la récursion) et un **cas récursif** qui se rapproche du cas de base.

```python
def factorielle(n):
    if n <= 1:                # cas de base
        return 1
    return n * factorielle(n - 1)

print(factorielle(5))         # → 120
```

- La profondeur est limitée (`sys.getrecursionlimit()`, 1000 par défaut) : au-delà, `RecursionError`.
- Python n'optimise pas la récursion terminale : pour de grandes profondeurs, utilisez une **boucle**.
- `@cache` évite les recalculs (Fibonacci).

### 11.9 Annotations et typage

```python
def saluer(nom: str, fois: int = 1) -> str:
    return (f'Bonjour {nom} ! ' * fois).strip()

print(saluer('Alice', 2))   # → Bonjour Alice ! Bonjour Alice !
```

Les annotations sont **informatives** : Python ne les applique pas à l'exécution, mais des outils (mypy, pyright) les vérifient (chapitre 17).

### 11.10 Docstrings

Une **docstring** est la chaîne de documentation placée immédiatement après la ligne `def` (PEP 257). Elle est accessible par `help(fonction)` et `fonction.__doc__`.

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
        raise ValueError('Dimensions négatives')
    return largeur * hauteur

print(aire_rectangle(3, 4))   # → 12
```

### 11.11 Fonctions intégrées essentielles

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

### 11.12 Bonnes pratiques

- Une fonction = **une responsabilité**, courte, nommée explicitement.
- Peu de paramètres (idéalement quatre au plus) ; sinon regroupez-les dans un objet.
- Évitez les **effets de bord** (modifier un argument, une globale) ; préférez renvoyer un résultat.
- Documentez et **typez** les fonctions publiques.
- Ne renvoyez pas des types différents selon les cas sans l'annoncer dans la signature.

### À retenir (chapitre 11)

- Paramètres : positionnels, nommés, par défaut, `*args`, `**kwargs`, `/` et `*`.
- Jamais de valeur par défaut mutable : utilisez `None`.
- Les fonctions sont des objets : fermetures, décorateurs et `functools` en découlent.
- Récursivité = cas de base + cas récursif, mais attention à la limite de profondeur.

## 12. Itérateurs et générateurs

**Objectifs du chapitre** : comprendre le protocole d'itération sur lequel repose `for`, écrire des générateurs pour traiter des données à la demande et utiliser `itertools`.

### 12.1 Itérables et itérateurs

- Un **itérable** est un objet qu'on peut parcourir avec `for` (liste, chaîne, dictionnaire, fichier…). Il définit `__iter__()`, qui renvoie un itérateur.
- Un **itérateur** produit ses valeurs une à une via `__next__()` et lève `StopIteration` quand il n'y en a plus. Un itérateur est à usage unique : il s'épuise.

Une boucle `for x in objet` appelle `iter(objet)` puis `next()` jusqu'à `StopIteration`.

```python
it = iter([10, 20])
print(next(it))     # → 10
print(next(it))     # → 20
try:
    next(it)
except StopIteration:
    print('itérateur épuisé')
print(next(iter([]), 'vide'))   # → vide (valeur par défaut de next)
```

### 12.2 Générateurs

Une fonction contenant `yield` est une **fonction génératrice** : l'appeler renvoie un **générateur** (un itérateur). Le code ne s'exécute qu'au fil des demandes ; à chaque `yield`, la fonction **se suspend** en conservant son état local, puis reprend là où elle s'était arrêtée. Les valeurs sont produites à la demande (**évaluation paresseuse**) : on ne stocke pas toute la séquence en mémoire.

```python
def compte_a_rebours(n):
    while n > 0:
        yield n
        n -= 1

for x in compte_a_rebours(3):
    print(x)             # → 3, 2, 1

g = compte_a_rebours(2)
print(next(g), next(g))  # → 2 1
print(list(g))           # → [] : le générateur est épuisé
```

#### Expressions génératrices

Syntaxe des compréhensions avec des parenthèses : elles produisent un générateur, pas une liste.

```python
somme = sum(x ** 2 for x in range(1_000_000))   # aucune liste en mémoire
print(somme)   # → 333332833333500000
```

#### `yield from`

`yield from itérable` délègue la production des valeurs à un autre itérable.

```python
def aplatir(listes):
    for l in listes:
        yield from l

print(list(aplatir([[1, 2], [3], [4, 5]])))   # → [1, 2, 3, 4, 5]
```

#### Lecture paresseuse d'un gros fichier

```python
def lignes_non_vides(chemin):
    with open(chemin, encoding='utf-8') as f:
        for ligne in f:
            if ligne.strip():
                yield ligne
```

Ce générateur traite un fichier de plusieurs gigaoctets en consommant une quantité de mémoire constante.

#### Générateurs infinis et communication

Un générateur peut être infini (`while True: yield ...`) ; on en consomme une partie avec `itertools.islice`. Les méthodes `send()`, `throw()` et `close()` permettent de communiquer avec un générateur (`valeur = yield`), mais cet usage avancé a largement été remplacé par `async` / `await` (chapitre 18).

### 12.3 Le module `itertools`

Il fournit des briques efficaces et paresseuses pour combiner des itérables.

```python
from itertools import chain, count, islice, product, permutations, combinations, groupby, batched

print(list(islice(count(1), 5)))         # → [1, 2, 3, 4, 5]
print(list(chain([1, 2], [3])))          # → [1, 2, 3]
print(list(combinations('ABC', 2)))      # → [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(len(list(permutations('ABC'))))    # → 6
print(len(list(product('AB', repeat=3))))# → 8
print(list(batched(range(7), 3)))        # → [(0, 1, 2), (3, 4, 5), (6,)]  (3.12+)
```

| Fonction | Rôle |
| --- | --- |
| `count`, `cycle`, `repeat` | Itérateurs infinis |
| `islice` | Tranche d'un itérable quelconque |
| `chain` | Concatène plusieurs itérables |
| `product`, `permutations`, `combinations` | Combinatoire |
| `groupby` | Regroupe des éléments consécutifs de même clé (trier d'abord) |
| `batched` | Découpe en lots de taille fixe (3.12+) |

### 12.4 Créer son propre itérateur

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

print(list(Compteur(3)))   # → [1, 2, 3]
```

Dans la plupart des cas, un **générateur** est plus simple et plus court qu'une classe itérateur.

### 12.5 Quand utiliser un générateur ?

- Données volumineuses ou flux continus (fichiers, réseau) ;
- chaînes de traitement (pipelines) où chaque étape consomme la précédente ;
- séquences potentiellement infinies.

Attention : on ne peut parcourir un générateur qu'**une seule fois**, et on ne peut ni connaître sa longueur (`len`) ni l'indexer.

### À retenir (chapitre 12)

- `for` repose sur `iter()` et `next()` ; un itérateur s'épuise.
- `yield` transforme une fonction en générateur : valeurs paresseuses, état conservé.
- `itertools` offre des outils combinatoires et de découpage économes en mémoire.

## 13. Gestion des erreurs

**Objectifs du chapitre** : distinguer erreurs de syntaxe et exceptions, savoir les capturer, les lever, les chaîner et en créer de nouvelles ; utiliser `finally`, `with`, `assert` et `logging` ; adopter une stratégie de gestion d'erreurs robuste.

### 13.1 Introduction

| Type | Description | Exemple |
| --- | --- | --- |
| **Erreur de syntaxe** | Détectée avant l'exécution | `print('a'` |
| **Exception** | Survient pendant l'exécution | `1 / 0`, `int('abc')` |
| **Erreur logique** (bogue) | Le programme s'exécute mais produit un mauvais résultat | formule fausse |

Une **exception** est un objet qui signale une situation anormale. Lorsqu'elle est levée, l'exécution normale s'interrompt et l'exception **remonte** la pile des appels jusqu'à trouver un gestionnaire `except` ; sans gestionnaire, le programme s'arrête en affichant la **trace d'appels** (*traceback*).

### 13.2 `try` / `except`

Le code susceptible d'échouer est placé dans `try` ; chaque `except` traite un type d'exception. Les clauses sont examinées dans l'ordre et la première qui correspond est exécutée.

```python
def inverser(texte):
    try:
        nombre = int(texte)
        return 10 / nombre
    except ValueError:
        print("Ce n'est pas un nombre.")
    except ZeroDivisionError:
        print('Division par zéro impossible.')
    except (TypeError, KeyError) as e:      # plusieurs types
        print(f'Erreur : {e}')

print(inverser('5'))   # → 2.0
inverser('abc')        # → Ce n'est pas un nombre.
inverser('0')          # → Division par zéro impossible.
```

**Ne jamais écrire `except:` nu** (il attrape aussi `KeyboardInterrupt` et `SystemExit`) ni `except Exception: pass` sans raison sérieuse : vous masqueriez des bogues.

### 13.3 `else` et `finally`

- `else` s'exécute si **aucune exception** n'a été levée dans `try` ;
- `finally` s'exécute **toujours** (exception ou non, même en cas de `return`) : il sert au nettoyage.

```python
try:
    f = open('donnees.txt', encoding='utf-8')
except FileNotFoundError:
    print('Fichier introuvable')
else:
    print('Lecture réussie')
    f.close()
finally:
    print('Toujours exécuté')
# sans donnees.txt : Fichier introuvable, puis Toujours exécuté
```

### 13.4 Exploiter l'objet exception

```python
try:
    int('abc')
except ValueError as e:
    print(type(e).__name__)   # → ValueError
    print(e)                  # → invalid literal for int() with base 10: 'abc'
    print(e.args)             # → ("invalid literal for int() with base 10: 'abc'",)
```

Le nom après `as` n'existe que dans le bloc `except`.

### 13.5 Lever des exceptions

L'instruction `raise` déclenche volontairement une exception, typiquement pour signaler un argument invalide ou un état impossible.

```python
def racine(x):
    if x < 0:
        raise ValueError('x doit être positif')
    return x ** 0.5

try:
    racine(-4)
except ValueError as erreur:
    print(erreur)   # → x doit être positif
```

### 13.6 Exceptions personnalisées

```python
class ErreurMetier(Exception):
    """Classe de base des erreurs de l'application."""

class SoldeInsuffisant(ErreurMetier):
    def __init__(self, solde, montant):
        super().__init__(f'Solde {solde} insuffisant pour retirer {montant}')
        self.solde = solde
        self.montant = montant

try:
    raise SoldeInsuffisant(50, 80)
except ErreurMetier as erreur:          # la classe de base attrape aussi la sous-classe
    print(erreur)                        # → Solde 50 insuffisant pour retirer 80
```

Dérivez toujours de `Exception` (jamais directement de `BaseException`), terminez le nom par `Error` pour une erreur, et créez une classe de base commune pour permettre de tout capturer d'un coup.

### 13.7 Chaînage et relance

`raise ... from e` conserve la **cause** d'origine (`__cause__`) ; un `raise` seul, dans un `except`, **relance** l'exception en cours sans perdre sa trace.

```python
try:
    try:
        int('x')
    except ValueError as e:
        raise RuntimeError('Lecture de configuration impossible') from e
except RuntimeError as erreur:
    print(erreur)                 # → Lecture de configuration impossible
    print(repr(erreur.__cause__)) # → ValueError("invalid literal for int() with base 10: 'x'")

try:
    try:
        1 / 0
    except Exception:
        print('Journalisation')   # traitement partiel
        raise                     # relance l'exception d'origine
except ZeroDivisionError as erreur:
    print('Relancée :', erreur)  # → Relancée : division by zero
```

### 13.8 Hiérarchie des exceptions

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

Un `except` attrape l'exception **et ses sous-classes** : placez les plus spécifiques en premier, sinon elles ne seront jamais atteintes.

### 13.9 Groupes d'exceptions et `except*` *(Python 3.11+)*

Quand plusieurs tâches échouent simultanément (concurrence, chapitre 18), on les regroupe dans un `ExceptionGroup`. `except*` traite séparément chaque type contenu dans le groupe.

```python
try:
    raise ExceptionGroup('Erreurs multiples', [ValueError('a'), TypeError('b')])
except* ValueError as eg:
    print('ValueError :', eg.exceptions)   # → (ValueError('a'),)
except* TypeError as eg:
    print('TypeError :', eg.exceptions)    # → (TypeError('b'),)
```

Python 3.11 permet aussi d'enrichir une exception avec `e.add_note('détail utile')` ; les notes s'affichent dans la trace et sont lisibles dans `e.__notes__`.

### 13.10 Assertions

`assert condition, message` lève une `AssertionError` si la condition est fausse. Elle vérifie des **hypothèses de développement**, jamais des entrées utilisateur : les assertions sont **désactivées** avec `python -O`.

```python
def moyenne(notes):
    assert len(notes) > 0, 'La liste de notes ne doit pas être vide'
    return sum(notes) / len(notes)

print(moyenne([10, 14]))   # → 12.0
```

### 13.11 Journalisation des erreurs

Le module `logging` remplace avantageusement `print` pour tracer l'exécution : niveaux de gravité, horodatage, destinations multiples.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
)

try:
    1 / 0
except ZeroDivisionError:
    logging.exception('Erreur de calcul')   # niveau ERROR + trace complète
```

Niveaux, du moins au plus grave : `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`. Dans un module réutilisable, on obtient un journal nommé par `logging.getLogger(__name__)`.

### 13.12 Gestionnaires de contexte et nettoyage

L'instruction `with` garantit la libération d'une ressource (fichier, verrou, connexion), même en cas d'exception : elle appelle `__enter__` à l'entrée et `__exit__` à la sortie.

```python
with open('fichier.txt', 'w', encoding='utf-8') as f:
    f.write('contenu')
# le fichier est fermé automatiquement
print(f.closed)   # → True
```

On crée un gestionnaire avec `contextlib.contextmanager` (un générateur avec un seul `yield`) ou avec une classe (chapitre 16). `contextlib.suppress` ignore proprement une erreur précise.

```python
import time
from contextlib import contextmanager, suppress
import os

@contextmanager
def chronometrer(nom):
    debut = time.perf_counter()
    try:
        yield
    finally:
        print(f'{nom} : {time.perf_counter() - debut:.3f} s')

with chronometrer('calcul'):
    sum(range(10_000_000))

with suppress(FileNotFoundError):
    os.remove('temp.txt')        # aucune erreur si le fichier n'existe pas
```

### 13.13 Cas pratiques

#### Requêtes web

```python
import requests    # pip install requests

try:
    reponse = requests.get('https://api.exemple.com/data', timeout=5)
    reponse.raise_for_status()
    donnees = reponse.json()
except requests.exceptions.Timeout:
    print('Délai dépassé')
except requests.exceptions.HTTPError as e:
    print(f'Erreur HTTP : {e}')
except requests.exceptions.RequestException as e:
    print(f'Erreur réseau : {e}')
```

Définissez toujours un `timeout`, sans quoi un appel réseau peut bloquer indéfiniment.

#### Saisie utilisateur validée

```python
while True:
    try:
        age = int(input('Âge : '))
        if age < 0:
            raise ValueError("L'âge ne peut pas être négatif")
        break
    except ValueError as e:
        print(f'Entrée invalide : {e}')
```

### 13.14 Bonnes pratiques

- Attrapez des exceptions **précises**, au niveau où vous savez quoi en faire.
- Gardez le bloc `try` **le plus court possible**.
- Ne **supprimez pas** les erreurs silencieusement.
- Préférez `with` à `try/finally` pour libérer les ressources.
- Fournissez des **messages utiles** et journalisez avec `logging`.
- Python favorise **EAFP** (*Easier to Ask Forgiveness than Permission* : essayer puis gérer l'échec) plutôt que **LBYL** (*Look Before You Leap* : tout vérifier d'abord).

```python
d = {'autre': 1}
try:
    valeur = d['cle']        # EAFP (pythonique)
except KeyError:
    valeur = None
print(valeur)   # → None
```

### À retenir (chapitre 13)

- `try` / `except` / `else` / `finally`, avec des exceptions précises et jamais de `except:` nu.
- `raise` lève, `raise ... from e` chaîne, `raise` seul relance.
- `with` et `finally` garantissent le nettoyage ; `logging` trace ; `assert` vérifie les hypothèses de développement.

## 14. Gestion des fichiers

**Objectifs du chapitre** : lire et écrire des fichiers texte et binaires, manipuler chemins et dossiers avec `pathlib`, traiter CSV, JSON et TOML, et connaître les risques de `pickle`.

### 14.1 Introduction

Un fichier permet de **conserver** des données au-delà de l'exécution du programme.

| Type | Contenu | Modes |
| --- | --- | --- |
| **Texte** | Caractères (`.txt`, `.csv`, `.json`, `.md`) | `'r'`, `'w'`… |
| **Binaire** | Octets (images, audio, `.pdf`, `.zip`) | `'rb'`, `'wb'`… |

En mode texte, Python décode les octets en `str` (encodage) et traduit les fins de ligne ; en mode binaire, il manipule des `bytes` sans transformation.

### 14.2 Ouvrir et fermer un fichier

`open(chemin, mode, encoding=...)` renvoie un **objet fichier**. La méthode recommandée est le gestionnaire de contexte `with`, qui ferme le fichier automatiquement.

```python
with open('notes.txt', 'w', encoding='utf-8') as f:
    f.write('Première ligne\nDeuxième ligne\nTroisième ligne\n')

with open('notes.txt', 'r', encoding='utf-8') as f:
    contenu = f.read()
print(f.closed)   # → True
```

| Mode | Signification |
| --- | --- |
| `'r'` | Lecture (défaut) ; erreur si le fichier n'existe pas |
| `'w'` | Écriture ; **écrase** le contenu existant (crée le fichier sinon) |
| `'a'` | Ajout en fin de fichier |
| `'x'` | Création exclusive ; erreur si le fichier existe |
| `'r+'` | Lecture et écriture |
| `'b'` / `'t'` | Binaire / texte (défaut) |

**Précisez toujours `encoding='utf-8'`** en mode texte : sinon l'encodage dépend du système. (Python 3.15 adopte UTF-8 comme encodage par défaut, mais l'expliciter reste une bonne pratique.)

### 14.3 Lire un fichier

```python
with open('notes.txt', encoding='utf-8') as f:
    tout = f.read()           # tout le contenu en une chaîne
    f.seek(0)
    une_ligne = f.readline()  # une ligne
    f.seek(0)
    lignes = f.readlines()    # liste de lignes

print(repr(une_ligne))   # → 'Première ligne\n'

# le plus économe en mémoire : parcours ligne par ligne
with open('notes.txt', encoding='utf-8') as f:
    for ligne in f:
        print(ligne.rstrip('\n'))
```

L'objet fichier est lui-même un itérateur de lignes : pour un gros fichier, **parcourez-le** plutôt que d'appeler `read()` ou `readlines()` qui chargent tout en mémoire.

### 14.4 Écrire dans un fichier

```python
with open('sortie.txt', 'w', encoding='utf-8') as f:
    f.write('Ligne 1\n')
    f.writelines(['Ligne 2\n', 'Ligne 3\n'])
    print('Ligne 4', file=f)

with open('sortie.txt', 'a', encoding='utf-8') as f:    # ajout
    f.write('Ligne ajoutée\n')
```

`write()` n'ajoute **pas** de retour à la ligne automatiquement ; `print(..., file=f)` en ajoute un.

### 14.5 Chemins avec `pathlib`

Le module **`pathlib`** représente les chemins comme des objets, indépendamment du système d'exploitation ; il est préférable à `os.path` et à la manipulation de chaînes.

```python
from pathlib import Path

p = Path('donnees') / 'rapport.txt'     # l'opérateur / assemble les chemins
p.parent.mkdir(exist_ok=True)
p.write_text('Bonjour', encoding='utf-8')

print(p.name, p.stem, p.suffix)   # → rapport.txt rapport .txt
print(p.parent)                   # → donnees
print(p.exists(), p.is_file(), p.is_dir())   # → True True False
print(p.read_text(encoding='utf-8'))         # → Bonjour
print(p.resolve())                # chemin absolu
print(Path.home(), Path.cwd())    # dossier personnel, dossier courant
```

### 14.6 Opérations sur fichiers et dossiers

```python
from pathlib import Path
import shutil

Path('nouveau').mkdir(parents=True, exist_ok=True)   # créer un dossier
Path('a.txt').write_text('A', encoding='utf-8')
Path('a.txt').rename('b.txt')                        # renommer / déplacer
Path('b.txt').unlink(missing_ok=True)                # supprimer un fichier
Path('nouveau').rmdir()                              # supprimer un dossier vide

for f in Path('.').glob('*.py'):                     # lister (motif)
    print(f)
for f in Path('.').rglob('*.md'):                    # lister récursivement
    print(f)

shutil.copy('src.txt', 'dst.txt')                    # copier un fichier
shutil.copytree('dossier', 'copie')                  # copier un dossier
shutil.rmtree('copie')                               # supprimer un dossier non vide
shutil.move('dst.txt', 'dossier/dst.txt')
```

Équivalents du module `os` : `os.listdir()`, `os.remove()`, `os.mkdir()`, `os.path.join()`, `os.walk()`.

### 14.7 Fichiers binaires

```python
with open('image.png', 'rb') as f:
    octets = f.read()
with open('copie.png', 'wb') as f:
    f.write(octets)

# lecture par blocs (gros fichiers)
with open('gros.bin', 'rb') as f:
    while bloc := f.read(8192):
        print(f'Bloc de {len(bloc)} octets')
```

### 14.8 Position dans le fichier

Un fichier ouvert possède un **curseur** : `tell()` donne sa position, `seek(position, origine)` le déplace (origine 0 : début, 1 : position courante, 2 : fin).

```python
with open('octets.bin', 'wb') as f:
    f.write(b'Bonjour le monde')

with open('octets.bin', 'rb') as f:
    print(f.read(5))     # → b'Bonjo'
    print(f.tell())      # → 5
    f.seek(0)            # retour au début
    f.seek(0, 2)         # tout à la fin
    print(f.tell())      # → 16
```

### 14.9 Fichiers CSV

Le format **CSV** (*Comma-Separated Values*) représente un tableau en texte. Ouvrez toujours avec `newline=''` pour que le module `csv` gère les fins de ligne.

```python
import csv

with open('personnes.csv', 'w', newline='', encoding='utf-8') as f:
    f.write('nom,age\nAlice,30\nBob,25\n')

with open('personnes.csv', newline='', encoding='utf-8') as f:
    for ligne in csv.DictReader(f):          # chaque ligne devient un dict
        print(ligne['nom'], ligne['age'])    # → Alice 30, puis Bob 25

with open('sortie.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['nom', 'age'])
    writer.writeheader()
    writer.writerow({'nom': 'Alice', 'age': 30})
```

Toutes les valeurs lues sont des chaînes ; convertissez-les. Pour de gros volumes, utilisez **pandas** ou **polars**.

### 14.10 Fichiers JSON

```python
import json
from pathlib import Path

donnees = {'nom': 'Alice', 'langues': ['fr', 'en']}
Path('data.json').write_text(
    json.dumps(donnees, indent=2, ensure_ascii=False), encoding='utf-8'
)
lu = json.loads(Path('data.json').read_text(encoding='utf-8'))
print(lu)   # → {'nom': 'Alice', 'langues': ['fr', 'en']}
```

JSON ne gère que `dict`, `list`, `str`, nombres, `True`/`False` et `None` (`null`) ; les autres objets (dates, ensembles) doivent être convertis.

### 14.11 Fichiers de configuration TOML *(3.11+)*

```python
import tomllib

with open('exemple.toml', 'rb') as f:       # ouverture en BINAIRE obligatoire
    config = tomllib.load(f)
print(config)   # → {'project': {'name': 'demo', 'version': '0.1.0'}}
```

`tomllib` ne sait que **lire** ; pour écrire du TOML, utilisez une bibliothèque tierce.

### 14.12 Sérialisation avec `pickle`

`pickle` sérialise presque n'importe quel objet Python en octets.

```python
import pickle

with open('objet.pkl', 'wb') as f:
    pickle.dump({'a': [1, 2, 3]}, f)
with open('objet.pkl', 'rb') as f:
    obj = pickle.load(f)
print(obj)   # → {'a': [1, 2, 3]}
```

**Sécurité** : ne chargez **jamais** un fichier pickle d'origine non fiable, car il peut exécuter du code arbitraire. Pour échanger des données, préférez JSON.

### 14.13 Compression et archives

```python
import zipfile, gzip, shutil

with zipfile.ZipFile('archive.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.write('a.txt')
with zipfile.ZipFile('archive.zip') as z:
    print(z.namelist())          # → ['a.txt']
    z.extractall('sortie')

with gzip.open('donnees.txt.gz', 'wt', encoding='utf-8') as f:
    f.write('texte compressé')

shutil.make_archive('sauvegarde', 'zip', 'dossier')   # archive d'un dossier entier
```

Autres formats : `tarfile`, `bz2`, `lzma`, et `compression.zstd` (Zstandard, Python 3.14+). Avec `extractall`, vérifiez la provenance de l'archive (risque de chemins malveillants).

### 14.14 Permissions et métadonnées

```python
import os, stat
from pathlib import Path

info = Path('a.txt').stat()
print(info.st_size, info.st_mtime)    # taille (octets), date de modification
os.chmod('script.sh', stat.S_IRWXU)   # rwx pour le propriétaire (Unix)
print(os.access('a.txt', os.R_OK))    # → True si lisible
```

### 14.15 Exceptions courantes

| Exception | Cause |
| --- | --- |
| `FileNotFoundError` | Fichier ou dossier inexistant |
| `PermissionError` | Droits insuffisants |
| `IsADirectoryError` | Un dossier est donné à la place d'un fichier |
| `FileExistsError` | Le fichier existe déjà (mode `'x'`, `mkdir`) |
| `UnicodeDecodeError` | Mauvais encodage |

### 14.16 Sujets avancés

- **Tampon** (*buffer*) : `open(..., buffering=...)` ; `f.flush()` force l'écriture sur le disque.
- **Fichiers temporaires** : `tempfile.NamedTemporaryFile()`, `tempfile.TemporaryDirectory()`.
- **Fichiers mappés en mémoire** : module `mmap`.
- **Écriture atomique** : écrire dans un fichier temporaire puis `os.replace()`, pour ne jamais laisser un fichier à moitié écrit.

### À retenir (chapitre 14)

- Toujours `with open(..., encoding='utf-8')` ; modes `r`, `w` (écrase), `a`, `x`, `b`.
- Parcourez les gros fichiers ligne par ligne ou par blocs.
- `pathlib` pour les chemins, `shutil` pour copier et supprimer, `csv` / `json` / `tomllib` pour les formats.
- Ne désérialisez jamais un pickle non fiable.

## 15. Modules, paquets et environnements virtuels

**Objectifs du chapitre** : organiser son code en modules et paquets, installer des bibliothèques tierces, isoler les dépendances de chaque projet et connaître les outils modernes de gestion de projet.

### 15.1 Modules

Un **module** est un fichier `.py` réutilisable : son nom (sans l'extension) est le nom du module. Il regroupe fonctions, classes et constantes liées. Un module a son propre **espace de noms** : deux modules peuvent définir une fonction du même nom sans conflit.

```python
# maths_utils.py
PI = 3.14159

def aire_cercle(r):
    return PI * r ** 2
```

```python
# main.py (dans le même dossier)
import maths_utils
from maths_utils import aire_cercle
from maths_utils import aire_cercle as aire      # alias
import math as m

print(maths_utils.aire_cercle(2))   # → 12.56636
print(aire(1))                      # → 3.14159
print(m.sqrt(16))                   # → 4.0
```

Le module est exécuté **une seule fois**, au premier import, puis mis en cache dans `sys.modules`. Évitez `from module import *` : il pollue l'espace de noms et masque l'origine des noms.

#### Le point d'entrée `__main__`

Quand un fichier est exécuté directement, sa variable `__name__` vaut `'__main__'` ; quand il est importé, elle vaut le nom du module. Ce test permet de séparer du code réutilisable et du code de lancement.

```python
def main():
    print('Programme principal')

if __name__ == '__main__':   # vrai seulement si le fichier est lancé directement
    main()
```

### 15.2 Paquets

Un **paquet** (*package*) est un dossier de modules. Un paquet peut contenir des sous-paquets. Depuis Python 3.3, le fichier `__init__.py` est facultatif (paquets d'espaces de noms) mais reste recommandé : il s'exécute à l'import du paquet et peut définir ce qu'il expose.

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
# src/monpaquet/sous_paquet/__init__.py
from .. import outils      # import relatif : '..' remonte d'un niveau, '.' = paquet courant

# ailleurs : import absolu
from monpaquet.outils import fonction
```

Préférez les **imports absolus** ; réservez les imports relatifs aux liens internes d'un paquet. Le fichier `__all__ = [...]` d'un module liste les noms exportés par `import *`.

### 15.3 Recherche des modules

Pour `import x`, Python cherche dans l'ordre : le cache `sys.modules`, les modules intégrés, puis les dossiers listés dans `sys.path` (dossier du script, `PYTHONPATH`, bibliothèque standard, `site-packages`).

```python
import sys
print(sys.path)   # liste des dossiers de recherche
```

Astuce : ne nommez jamais un de vos fichiers comme un module standard (`random.py`, `json.py`), car il masquerait le vrai module.

### 15.4 `pip` : installer des paquets

`pip` télécharge des paquets depuis **PyPI** (*Python Package Index*, pypi.org).

```bash
python -m pip install requests
python -m pip install "requests>=2.31"        # contrainte de version
python -m pip install -r requirements.txt     # depuis un fichier de dépendances
python -m pip list
python -m pip freeze > requirements.txt       # fige les versions installées
python -m pip uninstall requests
```

### 15.5 Environnements virtuels

Un **environnement virtuel** est un dossier contenant un interpréteur et ses propres paquets, isolés du reste du système. Il évite les conflits de versions entre projets et ne touche pas au Python du système. **Utilisez-en un pour chaque projet.**

```bash
python -m venv .venv                 # création

source .venv/bin/activate            # activation sous Linux / macOS
.venv\Scripts\activate               # activation sous Windows

deactivate                           # désactivation
```

Ajoutez `.venv/` à votre `.gitignore` : on partage la liste des dépendances, pas l'environnement.

### 15.6 Outils modernes de gestion de projet

| Outil | Rôle |
| --- | --- |
| **uv** | Tout-en-un très rapide : versions de Python, environnements, dépendances, verrouillage |
| **Poetry / PDM / Hatch** | Gestion de projets et publication de paquets |
| **pipx** | Installe des outils en ligne de commande dans des environnements isolés |

```bash
uv init mon_projet
cd mon_projet
uv add requests
uv run python main.py
```

Un **fichier de verrouillage** (*lock file*) enregistre les versions exactes de toutes les dépendances, pour des installations reproductibles.

### 15.7 `pyproject.toml`

Fichier standard de configuration d'un projet (PEP 517, 518, 621) : métadonnées, dépendances, système de construction et réglages des outils.

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

### 15.8 Bibliothèque standard : modules incontournables

| Module | Utilité |
| --- | --- |
| `pathlib`, `shutil`, `os`, `sys` | Système et fichiers |
| `json`, `csv`, `tomllib`, `sqlite3` | Données |
| `datetime`, `zoneinfo`, `time` | Dates et temps |
| `re` | Expressions régulières |
| `collections`, `itertools`, `functools` | Structures et outils fonctionnels |
| `argparse`, `logging` | Ligne de commande, journalisation |
| `random`, `statistics`, `math`, `decimal` | Nombres |
| `subprocess`, `threading`, `multiprocessing`, `asyncio` | Processus et concurrence |
| `unittest`, `doctest` | Tests |
| `dataclasses`, `enum`, `typing` | Modélisation |

Un exemple d'usage de `re` : `re.findall(r'[0-9]+', 'a12b345')` renvoie `['12', '345']`.

### À retenir (chapitre 15)

- Un module est un fichier `.py`, un paquet un dossier de modules ; `if __name__ == '__main__':` sépare import et exécution.
- `python -m pip install` installe depuis PyPI ; `python -m venv .venv` isole un projet.
- `pyproject.toml` est le fichier de référence ; `uv` simplifie l'ensemble du flux de travail.

## 16. Programmation orientée objet

**Objectifs du chapitre** : maîtriser classes, objets, attributs et méthodes, les quatre piliers de la POO, les méthodes spéciales, les `dataclass`, les classes abstraites et les protocoles, et connaître les mécanismes avancés (descripteurs, métaclasses).

### 16.1 Concepts fondamentaux

La **programmation orientée objet** (POO) organise un programme autour d'**objets** qui regroupent des données (attributs) et des comportements (méthodes).

| Concept | Description |
| --- | --- |
| **Classe** | Plan (modèle) qui décrit les attributs et comportements d'une famille d'objets |
| **Objet / instance** | Réalisation concrète d'une classe |
| **Attribut** | Donnée associée à un objet (attribut d'instance) ou à la classe (attribut de classe) |
| **Méthode** | Fonction définie dans une classe |
| **Encapsulation** | Regrouper données et comportements, et contrôler l'accès aux détails internes |
| **Héritage** | Une classe réutilise et étend une autre |
| **Polymorphisme** | Des objets de classes différentes répondent à une même interface |
| **Abstraction** | Exposer l'essentiel, masquer les détails |

#### Définir une classe

```python
class Chien:
    espece = 'Canis familiaris'           # attribut de classe (partagé)

    def __init__(self, nom, age):          # initialiseur
        self.nom = nom                     # attributs d'instance
        self.age = age

    def aboyer(self):                      # méthode d'instance
        return f'{self.nom} dit : Ouaf !'

    def __repr__(self):                    # représentation pour développeurs
        return f'Chien(nom={self.nom!r}, age={self.age})'

    def __str__(self):                     # représentation pour utilisateurs
        return f'{self.nom} ({self.age} ans)'

rex = Chien('Rex', 3)
print(rex.aboyer())        # → Rex dit : Ouaf !
print(rex)                 # → Rex (3 ans)
print(repr(rex))           # → Chien(nom='Rex', age=3)
print(Chien.espece)        # → Canis familiaris
```

- `__init__` **initialise** l'objet après sa création (le constructeur proprement dit est `__new__`, rarement utilisé) ;
- `self` désigne l'instance courante ; c'est le premier paramètre de toute méthode d'instance, rempli automatiquement lors de l'appel `rex.aboyer()` ;
- `__repr__` doit viser l'**absence d'ambiguïté** (idéalement du code recréant l'objet), `__str__` la **lisibilité** ; si seul `__repr__` est défini, `print` l'utilise aussi.

Une **classe** est elle-même un objet (instance de `type`). Les attributs de classe sont partagés ; si on affecte `rex.espece = 'x'`, on crée un attribut d'instance qui *masque* l'attribut de classe sans le modifier.

### 16.2 Encapsulation et propriétés

Python n'impose pas de visibilité stricte : il repose sur des **conventions** (« nous sommes entre adultes consentants »).

| Notation | Signification |
| --- | --- |
| `attribut` | Public |
| `_attribut` | « Protégé » : usage interne, par convention |
| `__attribut` | « Privé » : le nom est transformé en `_Classe__attribut` (*name mangling*) pour éviter les collisions dans les sous-classes |

Les **propriétés** (`@property`) permettent de contrôler l'accès à un attribut (validation, valeur calculée) tout en gardant la syntaxe simple `objet.attribut`.

```python
class Compte:
    def __init__(self, solde=0):
        self._solde = solde

    @property
    def solde(self):                       # lecture
        return self._solde

    @solde.setter
    def solde(self, valeur):               # écriture avec validation
        if valeur < 0:
            raise ValueError('Solde négatif interdit')
        self._solde = valeur

c = Compte(100)
c.solde = 150
print(c.solde)   # → 150
```

Commencez par de simples attributs publics ; ne passez à une propriété que lorsqu'un contrôle devient nécessaire : l'interface ne change pas pour les utilisateurs de la classe.

### 16.3 Méthodes de classe et statiques

| Type | Décorateur | Premier paramètre | Usage |
| --- | --- | --- | --- |
| Instance | (aucun) | `self` | Agit sur un objet |
| Classe | `@classmethod` | `cls` | Agit sur la classe, constructeurs alternatifs |
| Statique | `@staticmethod` | (aucun) | Utilitaire lié à la classe sans accès à l'instance ni à la classe |

```python
class Date:
    def __init__(self, j, m, a):
        self.j, self.m, self.a = j, m, a

    @classmethod
    def depuis_texte(cls, texte):          # constructeur alternatif
        j, m, a = map(int, texte.split('/'))
        return cls(j, m, a)

    @staticmethod
    def est_bissextile(annee):
        return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)

d = Date.depuis_texte('11/10/2026')
print(d.j, d.m, d.a)               # → 11 10 2026
print(Date.est_bissextile(2100))   # → False
```

### 16.4 Héritage

L'**héritage** permet à une **classe fille** (sous-classe) de reprendre les attributs et méthodes d'une **classe mère** (superclasse), de les **redéfinir** (*override*) et d'en ajouter. `super()` donne accès à la classe mère. Toute classe hérite implicitement de `object`.

```python
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        raise NotImplementedError

class Chat(Animal):
    def __init__(self, nom, couleur):
        super().__init__(nom)              # appel de l'initialiseur du parent
        self.couleur = couleur

    def parler(self):                      # redéfinition
        return 'Miaou'

mimi = Chat('Mimi', 'noir')
print(isinstance(mimi, Animal))   # → True : un Chat EST un Animal
print(issubclass(Chat, Animal))   # → True
print(mimi.parler())              # → Miaou
```

#### Héritage multiple et MRO

Une classe peut avoir plusieurs parents. L'**ordre de résolution des méthodes** (MRO, *Method Resolution Order*), calculé par l'algorithme **C3**, détermine dans quel ordre Python cherche un attribut ; `super()` suit cet ordre.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print([k.__name__ for k in D.__mro__])   # → ['D', 'B', 'C', 'A', 'object']
```

Préférez la **composition** (relation « a un » : un objet contient un autre objet) à l'héritage (relation « est un ») quand la seconde n'est pas évidente : elle est plus souple.

#### Mixins

Un **mixin** est une petite classe qui apporte une fonctionnalité précise et n'est pas destinée à être instanciée seule.

```python
import json

class JsonMixin:
    def en_json(self):
        return json.dumps(self.__dict__)

class Utilisateur(JsonMixin):
    def __init__(self, nom):
        self.nom = nom

print(Utilisateur('Alice').en_json())   # → {"nom": "Alice"}
```

### 16.5 Polymorphisme et *duck typing*

Le **polymorphisme** permet de traiter de la même manière des objets de classes différentes qui offrent la même interface. Python pratique le **duck typing** (« typage canard ») : ce qui compte n'est pas la classe de l'objet mais les méthodes qu'il possède. S'il cancane comme un canard, on le traite comme un canard.

```python
class Chien:
    def parler(self):
        return 'Ouaf'

class Robot:
    def parler(self):
        return 'Bip'

for etre in (Chien(), Robot()):
    print(etre.parler())    # → Ouaf, puis Bip : aucune parenté nécessaire
```

### 16.6 Méthodes spéciales (« dunder »)

Les **méthodes spéciales**, dont le nom est entouré de doubles tirets bas, sont appelées implicitement par le langage : en les définissant, vos objets s'intègrent aux opérateurs et fonctions intégrées (le *modèle de données* de Python).

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

panier = Panier()
panier.articles.extend(['pomme', 'poire'])
print(len(panier), panier[0])      # → 2 pomme
print(list(panier))                # → ['pomme', 'poire']
print('poire' in panier)           # → True
```

#### Gestionnaire de contexte personnalisé

```python
class Connexion:
    def __enter__(self):
        print('Ouverture')
        return self

    def __exit__(self, type_exc, valeur, trace):
        print('Fermeture')
        return False         # False : l'exception éventuelle n'est pas supprimée

with Connexion():
    print('Travail en cours')
# → Ouverture, Travail en cours, Fermeture
```

### 16.7 Classes de données : `dataclass`

Le décorateur `@dataclass` génère automatiquement `__init__`, `__repr__` et `__eq__` à partir des attributs annotés.

```python
from dataclasses import dataclass, field

@dataclass(order=True, slots=True)
class Produit:
    nom: str
    prix: float
    tags: list[str] = field(default_factory=list)   # défaut mutable : default_factory

    def prix_ttc(self, tva=0.2):
        return self.prix * (1 + tva)

p = Produit('Livre', 12.5)
print(p)                                      # → Produit(nom='Livre', prix=12.5, tags=[])
print(p.prix_ttc())                           # → 15.0
print(Produit('A', 1.0) < Produit('B', 1.0))  # → True (grâce à order=True)
```

| Option | Effet |
| --- | --- |
| `frozen=True` | Instances immuables et hachables |
| `order=True` | Génère `<`, `<=`, `>`, `>=` |
| `slots=True` | Économie de mémoire, accès plus rapide (3.10+) |
| `kw_only=True` | Arguments nommés obligatoires (3.10+) |

Alternatives : `NamedTuple`, et les bibliothèques **Pydantic** et **attrs** (validation des données).

### 16.8 Énumérations

Une **énumération** (`enum.Enum`) définit un ensemble fini de constantes nommées. Chaque membre possède un `name` et une `value`, est unique et se compare par identité. C'est préférable à des chaînes ou des entiers « magiques » : les fautes de frappe deviennent des erreurs.

```python
from enum import Enum, auto, StrEnum

class Couleur(Enum):
    ROUGE = auto()      # valeur choisie automatiquement
    VERT = auto()

class Statut(StrEnum):  # 3.11+ : membres utilisables comme des chaînes
    ACTIF = 'actif'
    INACTIF = 'inactif'

print(Couleur.ROUGE.name, Statut.ACTIF.value)   # → ROUGE actif
print(Statut('actif'))                           # → actif (recherche par valeur)
print([c.name for c in Couleur])                 # → ['ROUGE', 'VERT']
```

Variantes : `IntEnum` (comparable à des entiers), `Flag` (combinaisons de bits).

### 16.9 Classes abstraites et protocoles

Une **classe abstraite** (module `abc`) définit une interface que les sous-classes doivent implémenter ; on ne peut pas l'instancier tant que des méthodes abstraites subsistent.

```python
from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def aire(self) -> float: ...

class Carre(Forme):
    def __init__(self, c):
        self.c = c
    def aire(self):
        return self.c ** 2

print(Carre(3).aire())    # → 9
try:
    Forme()
except TypeError as erreur:
    print(erreur)
    # → Can't instantiate abstract class Forme without an implementation for abstract method 'aire'
```

Un **protocole** (`typing.Protocol`) exprime une interface de manière **structurelle** : tout objet qui possède les méthodes voulues convient, sans héritage. C'est la version « typée » du duck typing.

```python
from typing import Protocol

class Fermable(Protocol):
    def close(self) -> None: ...

def fermer(ressource: Fermable) -> None:
    ressource.close()

class Fichier:                      # aucun héritage nécessaire
    def close(self) -> None:
        print('Fichier fermé')

fermer(Fichier())                   # → Fichier fermé
```

### 16.10 `__slots__` et gestion de la mémoire

Par défaut, les attributs d'une instance sont stockés dans un dictionnaire (`__dict__`). `__slots__` remplace ce dictionnaire par une structure fixe : moins de mémoire, accès plus rapide, mais pas d'attribut non déclaré.

```python
class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x, self.y = x, y

p = Point(1, 2)
try:
    p.z = 3
except AttributeError as erreur:
    print(erreur)   # → 'Point' object has no attribute 'z' and no __dict__ for setting new attributes
```

### 16.11 Descripteurs

Un **descripteur** est un objet qui définit `__get__`, `__set__` ou `__delete__` et qui, placé comme attribut de classe, intercepte l'accès à cet attribut. C'est le mécanisme sous-jacent de `property`, des méthodes, de `classmethod` et de `staticmethod`.

```python
class Positif:
    def __set_name__(self, proprietaire, nom):
        self.nom = '_' + nom
    def __get__(self, obj, type=None):
        return getattr(obj, self.nom)
    def __set__(self, obj, valeur):
        if valeur <= 0:
            raise ValueError('Doit être positif')
        setattr(obj, self.nom, valeur)

class Article:
    prix = Positif()
    def __init__(self, prix):
        self.prix = prix

a = Article(10)
print(a.prix)   # → 10
try:
    a.prix = -5
except ValueError as erreur:
    print(erreur)   # → Doit être positif
```

L'intérêt par rapport à une propriété : la logique de validation est réutilisable pour plusieurs attributs et plusieurs classes.

### 16.12 Métaclasses et réflexion (avancé)

Une **métaclasse** est « la classe d'une classe » : puisqu'une classe est un objet, elle est l'instance d'une métaclasse. La métaclasse par défaut est `type`, qui permet aussi de créer des classes dynamiquement.

```python
Dynamique = type('Dynamique', (), {'x': 5, 'montrer': lambda self: print(self.x)})
Dynamique().montrer()      # → 5

class MetaJournal(type):
    def __new__(mcs, nom, bases, attrs):
        print(f'Création de la classe {nom}')
        return super().__new__(mcs, nom, bases, attrs)

class Base(metaclass=MetaJournal):   # affiche à la définition : Création de la classe Base
    pass
```

Pour la plupart des besoins (enregistrement automatique, validation des sous-classes), **`__init_subclass__`** est plus simple :

```python
class Plugin:
    registre = []
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin.registre.append(cls)

class PluginA(Plugin): pass
class PluginB(Plugin): pass
print([c.__name__ for c in Plugin.registre])   # → ['PluginA', 'PluginB']
```

Les métaclasses sont rarement nécessaires ; utilisez-les avec parcimonie.

#### Introspection (réflexion)

```python
import inspect

class Exemple:
    def __init__(self):
        self.x = 1

obj = Exemple()
print(type(obj).__name__)             # → Exemple
print(isinstance(obj, Exemple))       # → True
print(vars(obj))                      # → {'x': 1}
print(hasattr(obj, 'x'), getattr(obj, 'x'))   # → True 1
setattr(obj, 'y', 2)
print(obj.__dict__)                   # → {'x': 1, 'y': 2}
print([n for n, _ in inspect.getmembers(obj) if not n.startswith('__')])   # → ['x', 'y']
```

### 16.13 Principes et bonnes pratiques

| Principe | Idée |
| --- | --- |
| **SOLID** | Responsabilité unique, ouvert/fermé, substitution de Liskov, ségrégation des interfaces, inversion des dépendances |
| **DRY** | *Don't Repeat Yourself* : ne pas dupliquer la logique |
| **KISS** | *Keep It Simple* : privilégier la simplicité |
| **Composition plutôt qu'héritage** | Assembler des objets plutôt qu'empiler des classes |
| **Programmer vers des interfaces** | S'appuyer sur des protocoles ou classes abstraites |

- Classes **petites et cohérentes**, noms explicites.
- Définissez toujours `__repr__`.
- Si vous redéfinissez `__eq__`, définissez aussi `__hash__` (ou assumez que l'objet n'est plus hachable).
- Pas d'attributs publics modifiables sans validation : utilisez des propriétés.
- Principe de **substitution de Liskov** : une sous-classe doit pouvoir remplacer sa classe mère sans surprise.

### 16.14 Patrons de conception appliqués

**Singleton.** En Python, un **module** est déjà un singleton : une instance créée au niveau du module est partagée par tous les imports.

**Fabrique** (*factory*) : une fonction crée l'objet adapté.

```python
class Chien: ...
class Chat: ...

def creer_animal(type_):
    return {'chien': Chien, 'chat': Chat}[type_]()

print(type(creer_animal('chat')).__name__)   # → Chat
```

**Stratégie** : on injecte un comportement, souvent sous forme de simple fonction.

```python
def remise_fidelite(prix):
    return prix * 0.9

def remise_aucune(prix):
    return prix

def total(prix, strategie=remise_aucune):
    return strategie(prix)

print(total(100), total(100, remise_fidelite))   # → 100 90.0
```

**Observateur** : des abonnés sont prévenus quand un événement survient.

```python
class Evenement:
    def __init__(self):
        self._abonnes = []
    def abonner(self, fonction):
        self._abonnes.append(fonction)
    def emettre(self, *args):
        for f in self._abonnes:
            f(*args)

evenement = Evenement()
evenement.abonner(lambda message: print('Reçu :', message))
evenement.emettre('alerte')   # → Reçu : alerte
```

### 16.15 Exemple complet

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
            raise ValueError('Montant invalide')
        self.solde += montant
        self.historique.append(('dépôt', montant))

    def retirer(self, montant: float) -> None:
        if montant > self.solde:
            raise SoldeInsuffisant(f'Solde : {self.solde}')
        self.solde -= montant
        self.historique.append(('retrait', montant))

c = Compte('Alice')
c.deposer(100)
c.retirer(30)
print(c)   # → Compte(titulaire='Alice', solde=70.0, historique=[('dépôt', 100), ('retrait', 30)])
try:
    c.retirer(500)
except SoldeInsuffisant as erreur:
    print(erreur)   # → Solde : 70.0
```

Cet exemple combine classe de données, exception personnalisée, validation et annotations.

### À retenir (chapitre 16)

- Classe = plan, objet = instance ; `__init__` initialise, `self` désigne l'instance.
- Encapsulation par convention (`_x`) et propriétés ; `@classmethod` pour les constructeurs alternatifs.
- Héritage + `super()` + MRO ; préférez la composition quand c'est possible.
- Duck typing et protocoles : l'interface prime sur la classe.
- `@dataclass` supprime le code répétitif ; `Enum` modélise les constantes ; `ABC` définit des interfaces.

## 17. Typage statique

**Objectifs du chapitre** : annoter le code avec des types, utiliser la syntaxe moderne, comprendre génériques et alias, connaître l'évaluation différée des annotations de Python 3.14 et vérifier ses types avec un outil.

### 17.1 Annotations de types

Une **annotation** indique le type attendu d'une variable, d'un paramètre ou d'une valeur de retour. Elle documente le code et permet à des outils d'**analyse statique** de détecter des erreurs *sans exécuter* le programme.

```python
nom: str = 'Alice'
age: int = 30
prix: float = 9.99
actif: bool = True

def additionner(a: int, b: int) -> int:
    return a + b

print(additionner(2, 3))             # → 5
print(additionner('a', 'b'))         # → ab : aucune erreur à l'exécution
```

Python **n'applique pas** ces annotations à l'exécution : elles servent aux **vérificateurs de types** (**mypy**, **pyright**, **ty**, **pyrefly**) et aux éditeurs (complétion, détection d'erreurs). On parle de **typage graduel** : on type autant ou aussi peu qu'on veut, et on peut commencer par les fonctions publiques. Le mot-clé `Any` désactive la vérification pour une valeur.

### 17.2 Syntaxe moderne (Python 3.9 / 3.10+)

Les anciens alias `List`, `Dict`, `Tuple`, `Optional`, `Union` du module `typing` sont **dépréciés** au profit de la syntaxe native :

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

print(trouver('b', ['a', 'b']))   # → 1
print(trouver('z', ['a', 'b']))   # → None
```

Un type `X | None` oblige le vérificateur à exiger un test `is None` avant d'utiliser la valeur : c'est la protection contre les erreurs sur `None`. Les tuples de longueur variable s'écrivent `tuple[int, ...]`.

### 17.3 Types courants

```python
from typing import Any, Callable, Iterable, Literal, TypedDict, Final
from collections.abc import Sequence, Mapping

def appliquer(f: Callable[[int], int], valeurs: Iterable[int]) -> list[int]:
    return [f(v) for v in valeurs]

Mode = Literal['lecture', 'ecriture']      # valeurs littérales autorisées

class Utilisateur(TypedDict):              # dict à clés fixes
    nom: str
    age: int

print(appliquer(lambda x: x * 2, [1, 2, 3]))   # → [2, 4, 6]
mode: Mode = 'lecture'
u: Utilisateur = {'nom': 'Alice', 'age': 30}
```

| Type | Usage |
| --- | --- |
| `Callable[[A, B], R]` | Fonction prenant `A`, `B` et renvoyant `R` |
| `Iterable[T]`, `Sequence[T]`, `Mapping[K, V]` | Types abstraits pour les **paramètres** (plus souples que `list` ou `dict`) |
| `Literal[...]` | Ensemble de valeurs précises |
| `TypedDict` | Dictionnaire à clés et types connus |
| `Final` | Constante à ne pas réaffecter |
| `Self` | Type de l'instance courante (méthodes renvoyant `self`) |
| `Protocol` | Interface structurelle (chapitre 16) |

Regle pratique : acceptez des types généraux en paramètre (`Iterable`), renvoyez des types précis (`list`).

### 17.4 Génériques et paramètres de type *(Python 3.12+)*

Un **type générique** est paramétré par un autre type : `list[int]` est une liste *de* `int`. Depuis Python 3.12 (PEP 695), on déclare ses propres génériques avec une syntaxe compacte, et on crée des alias avec l'instruction `type`.

```python
def premier[T](elements: list[T]) -> T:
    return elements[0]

class Pile[T]:
    def __init__(self) -> None:
        self._items: list[T] = []
    def empiler(self, x: T) -> None:
        self._items.append(x)

type Matrice = list[list[float]]     # alias de type

print(premier([3, 4]))               # → 3
pile = Pile[int]()
pile.empiler(1)
```

Le vérificateur déduit que `premier([3, 4])` renvoie un `int` et que `premier(['a'])` renvoie un `str` : `T` relie le type d'entrée au type de sortie. Avant 3.12, on utilisait `TypeVar('T')` et `Generic[T]`.

### 17.5 Évaluation différée des annotations *(Python 3.14)*

Historiquement, une annotation était évaluée immédiatement, ce qui interdisait de nommer une classe avant sa définition sans guillemets ou sans `from __future__ import annotations`. Depuis Python 3.14 (PEP 649 et 749), les annotations sont **évaluées à la demande** : les références en avant fonctionnent naturellement.

```python
from annotationlib import get_annotations

class Noeud:
    def suivant(self) -> Noeud | None:    # fonctionne en 3.14+
        return None

print(Noeud().suivant())                  # → None
print(get_annotations(Noeud.suivant))     # → {'return': __main__.Noeud | None}
```

Le module `annotationlib` permet d'inspecter les annotations (par exemple sous forme de chaînes ou de références non résolues).

### 17.6 Vérifier les types

```bash
pip install mypy
mypy mon_script.py
```

Le vérificateur signale par exemple l'appel `additionner('a', 'b')` du 17.1 sans exécuter le code. Intégrez-le à l'éditeur (Pylance, pyright) et à l'intégration continue. Pour les bibliothèques sans annotations, des fichiers de **stubs** (`.pyi`) fournissent les types.

### À retenir (chapitre 17)

- Les annotations n'ont aucun effet à l'exécution ; elles servent aux outils (mypy, pyright) et à la documentation.
- Syntaxe moderne : `list[int]`, `dict[str, int]`, `str | None`.
- `def f[T](...)`, `class C[T]` et `type Alias = ...` (3.12+) ; annotations évaluées à la demande (3.14).

## 18. Programmation asynchrone et concurrence

**Objectifs du chapitre** : distinguer concurrence et parallélisme, choisir entre `asyncio`, threads et processus, écrire du code asynchrone avec `async` / `await`, et comprendre le rôle du GIL et ses évolutions récentes.

### 18.1 Choisir le bon modèle

La **concurrence** consiste à gérer plusieurs tâches dont les exécutions se chevauchent dans le temps ; le **parallélisme** consiste à les exécuter réellement en même temps sur plusieurs cœurs. Le bon choix dépend de la nature du goulot d'étranglement :

- une tâche **liée aux E/S** (*I/O-bound*) passe l'essentiel de son temps à attendre (réseau, disque, base de données) ;
- une tâche **liée au processeur** (*CPU-bound*) passe son temps à calculer.

| Modèle | Quand l'utiliser | Outil |
| --- | --- | --- |
| **`asyncio`** | Très nombreuses opérations d'E/S (réseau, API), un seul thread | `async` / `await` |
| **Threads** | E/S bloquantes, bibliothèques non asynchrones | `threading`, `ThreadPoolExecutor` |
| **Processus** | Calcul intensif sur plusieurs cœurs | `multiprocessing`, `ProcessPoolExecutor` |

### 18.2 `asyncio`

`asyncio` exécute de nombreuses tâches dans **un seul thread** grâce à une **boucle d'événements** (*event loop*) : quand une tâche attend, elle rend la main et la boucle fait avancer une autre tâche. C'est de la **concurrence coopérative** : les points de bascule sont les `await`.

Vocabulaire : une **coroutine** est le résultat de l'appel d'une fonction déclarée `async def` (elle ne s'exécute que si on l'attend ou la planifie) ; `await` suspend la coroutine courante jusqu'au résultat d'une autre ; une **tâche** (*task*) est une coroutine planifiée pour s'exécuter.

```python
import asyncio

async def telecharger(nom, delai):
    await asyncio.sleep(delai)         # attente non bloquante
    return f'{nom} terminé'

async def main():
    resultats = await asyncio.gather(
        telecharger('A', 1),
        telecharger('B', 2),
    )
    print(resultats)                   # → ['A terminé', 'B terminé']

asyncio.run(main())                    # dure environ 2 s au lieu de 3 s
```

**Erreur classique** : appeler une fonction bloquante (`time.sleep`, `requests.get`) dans une coroutine gèle toute la boucle. Utilisez les équivalents asynchrones (`asyncio.sleep`, `httpx.AsyncClient`) ou déportez l'appel avec `await asyncio.to_thread(fonction)`.

#### `TaskGroup` *(3.11+)*

Un `TaskGroup` lance des tâches et garantit qu'elles sont toutes terminées (ou annulées) à la sortie du bloc ; si l'une échoue, les autres sont annulées et les erreurs sont regroupées dans un `ExceptionGroup` (voir `except*`, chapitre 13). C'est la forme de **concurrence structurée** recommandée.

```python
import asyncio

async def telecharger(nom, delai):
    await asyncio.sleep(delai)
    return f'{nom} terminé'

async def main():
    async with asyncio.TaskGroup() as groupe:
        t1 = groupe.create_task(telecharger('A', 1))
        t2 = groupe.create_task(telecharger('B', 2))
    print(t1.result(), t2.result())    # → A terminé B terminé

asyncio.run(main())
```

Autres outils : `asyncio.timeout(secondes)` (délai maximal, 3.11+), `asyncio.Semaphore` (limiter le nombre d'opérations simultanées), `asyncio.Queue` (communication entre tâches), `async for` et `async with` (itération et contextes asynchrones).

### 18.3 Threads et processus

Un **thread** (fil d'exécution) partage la mémoire du processus ; un **processus** possède sa propre mémoire. Le module `concurrent.futures` offre une interface commune : un *pool* d'exécutants et des méthodes `map` / `submit`.

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def telecharger_url(url):
    time.sleep(0.1)                  # simule une E/S bloquante
    return f'{url} : OK'

def calcul_lourd(n):
    return sum(i * i for i in range(n))

if __name__ == '__main__':           # indispensable avec les processus
    with ThreadPoolExecutor(max_workers=4) as pool:
        print(list(pool.map(telecharger_url, ['a.fr', 'b.fr', 'c.fr'])))

    with ProcessPoolExecutor() as pool:
        print(list(pool.map(calcul_lourd, [10_000, 20_000, 30_000])))
```

**Dangers de la mémoire partagée.** Quand plusieurs threads modifient la même donnée, une **condition de course** (*race condition*) peut produire des résultats incorrects. On protège les sections critiques avec un verrou (`threading.Lock`) ou, mieux, on échange les données par des files (`queue.Queue`). Entre processus, les données sont **sérialisées** (pickle) pour être transmises : les arguments et résultats doivent être sérialisables, et ce transfert a un coût.

```python
import threading

compteur = 0
verrou = threading.Lock()

def incrementer():
    global compteur
    for _ in range(100_000):
        with verrou:               # une seule à la fois dans la section critique
            compteur += 1

fils = [threading.Thread(target=incrementer) for _ in range(4)]
for f in fils: f.start()
for f in fils: f.join()
print(compteur)   # → 400000
```

### 18.4 Le GIL et Python sans GIL

Le **GIL** (*Global Interpreter Lock*) est un verrou de CPython qui n'autorise qu'**un seul thread** à la fois à exécuter du bytecode Python. Il simplifie la gestion mémoire, mais empêche plusieurs threads d'utiliser plusieurs cœurs pour du calcul Python pur : pour le CPU-bound, on utilisait donc les processus. Le GIL est relâché pendant les attentes d'E/S, ce qui explique que les threads restent utiles pour les tâches réseau.

- **Python 3.13** : première version **expérimentale sans GIL** (mode *free-threaded*, interpréteur `python3.13t`).
- **Python 3.14** : le mode *free-threaded* est **officiellement supporté** (PEP 779), sans être le mode par défaut.
- **Python 3.14** : le module `concurrent.interpreters` expose les **sous-interpréteurs** : plusieurs interpréteurs isolés dans un même processus, chacun avec son propre état, pour obtenir du parallélisme sans partager d'objets Python.

En mode sans GIL, les threads peuvent s'exécuter vraiment en parallèle : les verrous et la prudence sur les données partagées deviennent plus importants, et les extensions natives doivent être compatibles.

### À retenir (chapitre 18)

- E/S nombreuses : `asyncio` ; E/S bloquantes : threads ; calcul intensif : processus (ou mode sans GIL).
- Une coroutine se déclare avec `async def` et s'attend avec `await` ; `TaskGroup` structure la concurrence.
- Ne bloquez jamais la boucle d'événements ; protégez les données partagées entre threads.
- Le GIL limite le parallélisme des threads ; Python 3.13/3.14 ouvrent la voie du sans-GIL et des sous-interpréteurs.

## 19. Tests et qualité du code

**Objectifs du chapitre** : écrire des tests automatisés avec `pytest`, connaître `unittest` et `doctest`, mesurer la couverture, mettre en place des outils de qualité et déboguer efficacement.

### 19.1 Pourquoi tester ?

Un **test automatisé** vérifie par du code qu'un autre code fait ce qu'on attend. Il détecte les régressions (une modification qui casse l'existant), documente le comportement et autorise le remaniement (*refactoring*) sans crainte. On distingue les **tests unitaires** (une fonction ou classe isolée), les **tests d'intégration** (plusieurs composants) et les **tests de bout en bout**. Le **développement dirigé par les tests** (TDD) consiste à écrire le test avant le code.

### 19.2 Tests avec `pytest`

`pytest` découvre automatiquement les fichiers `test_*.py` et les fonctions `test_*`, et utilise l'instruction `assert` ordinaire, avec des messages d'échec détaillés.

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

@pytest.mark.parametrize('a, b, attendu', [(1, 1, 2), (0, 0, 0), (-1, 1, 0)])
def test_cas_multiples(a, b, attendu):
    assert additionner(a, b) == attendu

def test_erreur():
    with pytest.raises(TypeError):
        additionner('a', 1)
```

```bash
pip install pytest
pytest -v
```

Sortie attendue :

```text
tests/test_calcul.py::test_addition PASSED
tests/test_calcul.py::test_cas_multiples[1-1-2] PASSED
tests/test_calcul.py::test_cas_multiples[0-0-0] PASSED
tests/test_calcul.py::test_cas_multiples[-1-1-0] PASSED
tests/test_calcul.py::test_erreur PASSED
```

Notions clés de `pytest` :

- **`parametrize`** : exécute un même test avec plusieurs jeux de données ;
- **`pytest.raises`** : vérifie qu'une exception est levée ;
- **fixtures** (`@pytest.fixture`) : préparent des ressources réutilisables (données, fichier temporaire, connexion) injectées par nom dans les tests ;
- **`tmp_path`** : fixture fournie qui donne un dossier temporaire ;
- **`monkeypatch`** et `unittest.mock` : remplacent temporairement une fonction ou un objet (par exemple un appel réseau) par un **faux** (*mock*), pour tester en isolation.

```python
import pytest

@pytest.fixture
def panier():
    return ['pomme', 'poire']

def test_taille(panier):
    assert len(panier) == 2
```

### 19.3 `unittest` et `doctest`

Le module `unittest` (style xUnit, classes dérivées de `TestCase`) et `doctest` (exemples exécutables dans les docstrings) font partie de la bibliothèque standard.

```python
import unittest

class TestCalcul(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 3, 5)

    def test_erreur(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

# python -m unittest
```

```python
def doubler(x):
    """Double un nombre.

    >>> doubler(4)
    8
    """
    return x * 2

# python -m doctest -v fichier.py
```

### 19.4 Bien tester : principes

- Un test doit être **rapide**, **indépendant** des autres et **déterministe** (pas de hasard ni d'horloge non maîtrisés).
- Structure *Arrange / Act / Assert* : préparer, agir, vérifier.
- Testez les cas limites (liste vide, zéro, valeurs négatives) et les cas d'erreur, pas seulement le cas nominal.
- Un test qui échoue doit dire clairement quoi corriger.

### 19.5 Qualité du code

| Outil | Rôle |
| --- | --- |
| **Ruff** | Lint (détection de défauts) et formatage ; remplace Flake8, isort et Black |
| **mypy / pyright** | Vérification de types |
| **pytest-cov** | Mesure de la couverture de tests |
| **pre-commit** | Exécute les vérifications automatiquement avant chaque commit |

```bash
ruff check .         # analyse
ruff format .        # mise en forme
mypy src/            # types
pytest --cov=src     # tests + couverture
```

La **couverture** mesure la proportion de lignes exécutées par les tests ; c'est un indicateur utile pour repérer le code non testé, pas une garantie de qualité. L'**intégration continue** (CI) exécute ces contrôles à chaque modification du dépôt.

### 19.6 Déboguer

Déboguer consiste à trouver pourquoi un programme se comporte mal. Dans l'ordre : lisez la trace d'erreur, reproduisez le problème avec un exemple minimal, puis observez l'état du programme.

```python
breakpoint()   # lance le débogueur pdb à cet endroit ; tapez c pour continuer
```

Commandes `pdb` : `n` (ligne suivante), `s` (entrer dans l'appel), `c` (continuer), `p variable` (afficher), `l` (afficher le code), `q` (quitter). Les éditeurs (VS Code, PyCharm) proposent un débogueur graphique avec points d'arrêt. Le module `logging` et `print(f'{x=}')` restent des alliés simples ; `python -X dev` active des vérifications supplémentaires.

### À retenir (chapitre 19)

- Testez avec `pytest` : fichiers `test_*.py`, `assert`, `parametrize`, fixtures, `pytest.raises`.
- Automatisez le lint, le formatage, les types et les tests (Ruff, mypy, pre-commit, CI).
- Pour déboguer : trace d'erreur, exemple minimal, `breakpoint()` ou débogueur de l'éditeur.

## 20. Aller plus loin

**Objectifs du chapitre** : situer ses acquis, choisir une spécialisation, suivre l'évolution du langage et savoir où chercher de l'aide.

### 20.1 Parcours d'apprentissage suggéré

1. Maîtriser les **bases** (chapitres 1 à 6) : syntaxe, types, opérateurs, entrées/sorties, structures de contrôle.
2. Manipuler les **structures de données** (7 à 10) : dictionnaires, listes, ensembles, tuples.
3. Écrire des **fonctions** propres et utiliser les **générateurs** (11 et 12).
4. Gérer **erreurs**, **fichiers** et **modules** (13 à 15).
5. Appliquer la **POO**, le **typage**, la **concurrence** et les **tests** (16 à 19).
6. Choisir une **spécialisation** : web (Django, FastAPI), données (Pandas, NumPy, Polars), IA (PyTorch), automatisation (Selenium, Playwright), systèmes et DevOps.

**Projets pour progresser** : un gestionnaire de tâches en ligne de commande (fichiers, JSON, `argparse`) ; un analyseur de fichiers CSV avec statistiques ; un petit serveur d'API (FastAPI) testé avec `pytest` ; un robot de collecte de données asynchrone ; un jeu simple (Pygame). Chaque projet doit avoir un environnement virtuel, des tests, des annotations de types et un `README`.

### 20.2 Résumé des nouveautés récentes de Python

| Version | À retenir |
| --- | --- |
| 3.8 | Opérateur `:=`, `/` dans les paramètres, `f'{x=}'` |
| 3.9 | Opérateur `\|` sur les `dict`, `list[int]`, `removeprefix` |
| 3.10 | `match` / `case`, `X \| Y`, messages d'erreur améliorés |
| 3.11 | `except*`, `tomllib`, interpréteur plus rapide |
| 3.12 | Syntaxe générique `def f[T]()`, instruction `type`, `itertools.batched` |
| 3.13 | Nouveau REPL, mode sans GIL (expérimental), JIT (expérimental) |
| 3.14 | t-strings, annotations différées, *free-threading* supporté, `compression.zstd` |
| 3.15 | Voir *Quoi de neuf dans Python 3.15* sur docs.python.org |

Pour suivre l'actualité du langage : les notes de version (*What's New*), les PEP et le forum discuss.python.org.

### 20.3 Ressources

- Documentation : docs.python.org/fr/3/
- Tutoriel officiel : docs.python.org/fr/3/tutorial/
- Guide de style PEP 8 : peps.python.org/pep-0008/
- Forum officiel : discuss.python.org
- Index des paquets : pypi.org
- Glossaire en français : docstring.fr/glossaire

### Conclusion

Python récompense la régularité : lire du code d'autres personnes, écrire de petits programmes chaque semaine, tester, typer et refactoriser. Les concepts de ce cours (objets, mutabilité, itérateurs, exceptions, modules) se retrouvent dans tout l'écosystème ; une fois maîtrisés, chaque nouvelle bibliothèque devient une simple application de principes connus. Bon code !
