# Git — Cours complet

*Cours magistral et module d'apprentissage exhaustif, fondé sur le plan « Git — Guide complet » — Git 2.55 (2026)*

## Avant de commencer : comment utiliser ce cours

Ce cours développe, chapitre par chapitre, l'intégralité du plan en **12 chapitres**, regroupés en quatre parties : **Fondamentaux** (chapitres 1 à 5), **Git avancé** (6 et 7), **Workflows, outils et plateformes** (8 à 10) et **Essentiels** (11 et 12).

Chaque chapitre suit la même trame : *objectifs d'apprentissage → notions et définitions → exemples de commandes commentés → pièges fréquents → synthèse*.

**Conventions de lecture**

- **(à jour)** désigne une pratique moderne qui remplace une ancienne ; **(héritage)** désigne une ancienne approche, encore fréquente dans les tutoriels et les projets existants (par exemple `git checkout` pour changer de branche, la branche `master` ou `git filter-branch`) ; **(ajout)** désigne une notion absente des guides plus anciens.
- Les commandes sont écrites pour un terminal de type Bash ; sous Windows, utilisez Git Bash ou PowerShell. Les valeurs entre chevrons (`<hash>`, `<url>`, `<fichier>`) sont à remplacer par vos propres valeurs ; lorsqu'un bloc présente plusieurs variantes d'une même commande, elles sont indépendantes (à lire comme « l'une ou l'autre »).
- Chaque exemple est volontairement **autonome** : les commandes préalables nécessaires sont toujours indiquées.
- Le cours enseigne le Git **actuel** (`git switch` et `git restore`, branche `main`, signature par clé SSH, `--force-with-lease`) **et** explique l'ancien (`git checkout`, `master`, `filter-branch`), pour que vous sachiez lire des procédures et des scripts existants.
- Les encadrés **À retenir**, **Attention** et **Astuce** signalent respectivement une idée à mémoriser, un risque de perte de données ou de comportement surprenant, et une pratique recommandée.

**Parcours conseillé.** Lisez les chapitres 1 à 5 dans l'ordre (ils se construisent les uns sur les autres) et pratiquez dans un dépôt jetable dès le chapitre 2. Choisissez ensuite selon vos besoins : chapitres 6 et 7 pour maîtriser l'historique et comprendre le fonctionnement interne, chapitres 8 à 10 pour travailler en équipe, chapitres 11 et 12 pour la sécurité et l'aide-mémoire.

---

## 1. Introduction et installation

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez définir Git et expliquer ce qui le distingue des systèmes centralisés ; décrire ses principes de conception (instantanés, opérations locales, intégrité par le hash) ; installer et configurer Git sur votre système ; décrire les trois zones (répertoire de travail, index, dépôt) et les quatre états d'un fichier ; vous authentifier auprès d'une plateforme par SSH, HTTPS ou GitHub CLI ; et préparer votre environnement de travail.

### 1.1 Qu'est-ce que Git ?

#### 1.1.1 Le problème que résout la gestion de versions

Tout projet qui évolue dans le temps pose les mêmes questions : comment conserver les états successifs des fichiers, comment revenir à une version antérieure qui fonctionnait, comment savoir qui a modifié quoi et pourquoi, et comment permettre à plusieurs personnes de travailler simultanément sans écraser le travail les unes des autres ?

La solution naïve consiste à copier les dossiers à la main (`projet_v1`, `projet_v2_final`, `projet_v2_final_corrige`). Cette méthode est lourde, source d'erreurs, ne dit rien sur le contenu des changements et ne permet aucune fusion de travaux parallèles. Un **système de gestion de versions** (*Version Control System*, VCS) automatise et fiabilise cette tâche : il enregistre l'historique des modifications d'un ensemble de fichiers, permet de revenir en arrière, de comparer des versions et de coordonner le travail de plusieurs contributeurs.

#### 1.1.2 Les trois générations de systèmes de gestion de versions

| Génération | Principe | Exemples | Limites |
| --- | --- | --- | --- |
| Locale | Une base de données de versions sur la seule machine de l'utilisateur | RCS | Aucune collaboration |
| Centralisée (CVCS) | Un serveur unique détient l'historique ; les clients n'ont que la version extraite | CVS, Subversion (SVN), Perforce | Point de défaillance unique ; la plupart des opérations exigent le réseau |
| Décentralisée ou distribuée (DVCS) | Chaque client possède une copie complète du dépôt, historique compris | Git, Mercurial, Bazaar | Modèle mental plus riche à acquérir |

Git appartient à la troisième famille. Dans un système distribué, il n'existe aucune différence technique entre le dépôt du serveur et celui d'un développeur : chacun contient l'intégralité de l'historique. Si le serveur disparaît, n'importe quel clone peut le restaurer. L'organisation « un dépôt de référence hébergé sur une plateforme » est une **convention sociale**, pas une contrainte technique.

#### 1.1.3 Origine de Git

Git a été créé en **2005 par Linus Torvalds** pour développer le noyau Linux. Le projet utilisait jusqu'alors un outil propriétaire, BitKeeper, dont la licence gratuite a été retirée à la communauté. Torvalds a conçu en quelques semaines un nouvel outil répondant à des objectifs précis :

- **la vitesse**, y compris sur des projets comportant des milliers de contributeurs ;
- **une conception simple** ;
- **un fort support du développement non linéaire** : des milliers de branches parallèles, créées et fusionnées sans douleur ;
- **une architecture entièrement distribuée** ;
- **la capacité à gérer de très gros projets** (noyau Linux) de façon efficace en temps et en espace ;
- **l'intégrité des données** : toute corruption doit être détectable.

La maintenance du projet a été confiée peu après à Junio Hamano, qui la poursuit aujourd'hui.

#### 1.1.4 Principes fondamentaux de conception

Quatre idées expliquent presque tout le comportement de Git.

**Des instantanés, pas des différences.** Beaucoup d'anciens systèmes stockent, pour chaque fichier, une liste de modifications successives (des *deltas*). Git raisonne autrement : à chaque commit, il enregistre un **instantané** (*snapshot*) de l'état complet du projet. Si un fichier n'a pas changé, Git ne le stocke pas une seconde fois : il garde seulement une référence vers la version identique déjà enregistrée. L'historique est donc une suite d'instantanés reliés entre eux. En interne, Git compacte ensuite ces données (voir `git gc`, chapitre 9).

**Presque toutes les opérations sont locales.** Comme le dépôt entier est présent sur votre disque, consulter l'historique, comparer des versions, créer des branches ou valider des changements ne nécessite aucun accès réseau. Vous pouvez travailler dans un train ou en avion, puis synchroniser plus tard. Le réseau n'intervient que pour `clone`, `fetch`, `pull` et `push`.

**L'intégrité par le contenu.** Chaque objet stocké par Git (fichier, dossier, commit) est identifié par une **empreinte cryptographique** calculée à partir de son contenu (historiquement SHA-1, 40 caractères hexadécimaux ; SHA-256 est pris en charge, voir le chapitre 7). Il est donc impossible de modifier un fichier ou un historique sans que Git s'en aperçoive : l'empreinte changerait. Ce mécanisme sert aussi d'identifiant : un commit se désigne par son hash, par exemple `f0a1234...`.

**Git n'ajoute presque que des données.** La plupart des actions n'ajoutent que de nouveaux objets à la base. Il est donc très difficile de perdre définitivement ce qui a été validé (commité) : même après une erreur, l'historique reste en général récupérable (voir `git reflog`). En revanche, ce qui n'a **jamais été commité** (modifications non enregistrées) peut être perdu pour de bon.

#### 1.1.5 Vocabulaire de base

| Terme | Définition |
| --- | --- |
| **Dépôt** (*repository*, *repo*) | Base de données contenant l'historique complet d'un projet, stockée dans le dossier `.git` |
| **Répertoire de travail** (*working directory*) | Les fichiers que vous voyez et éditez, extraits d'un commit |
| **Index** (*staging area*) | Zone intermédiaire qui prépare le contenu du prochain commit |
| **Commit** | Instantané enregistré, accompagné d'un auteur, d'une date, d'un message et de son ou ses parents |
| **Branche** | Pointeur mobile vers un commit, qui avance à chaque nouveau commit |
| **HEAD** | Pointeur désignant l'endroit où vous vous trouvez (en général la branche courante) |
| **Étiquette** (*tag*) | Pointeur fixe vers un commit, utilisé pour marquer une version |
| **Dépôt distant** (*remote*) | Version du dépôt hébergée ailleurs (serveur, plateforme) |
| **Clone** | Copie complète d'un dépôt, historique compris |
| **Fusion** (*merge*) | Intégration des modifications d'une branche dans une autre |
| **Conflit** | Situation où Git ne peut pas combiner automatiquement deux modifications |
| **Hash** | Empreinte hexadécimale qui identifie un objet |

#### 1.1.6 Avantages

| Avantage | Détail |
| --- | --- |
| Historique | Chaque modification est conservée, datée et attribuée à son auteur |
| Collaboration | Travail en parallèle, relectures de code, *pull requests* |
| Retour arrière | Retrouver une version antérieure en cas de bug |
| Expérimentation | Tester une idée dans une branche sans risque pour le code stable |
| Hors-ligne | Presque toutes les opérations fonctionnent sans réseau |
| Traçabilité | Savoir qui a changé une ligne, quand et pourquoi (`git blame`, `git log`) |
| Sauvegarde | Chaque clone constitue une copie complète du projet |

> **Remarque** : **Git n'est pas GitHub.** Git est un logiciel qui s'exécute sur votre machine. GitHub, GitLab, Bitbucket et d'autres sont des **services d'hébergement** de dépôts Git, qui ajoutent des fonctionnalités de collaboration (pull requests, tickets, intégration continue). On peut utiliser Git sans aucun de ces services.

### 1.2 Installer Git

Quel que soit le système, vérifiez l'installation avec :

```bash
git --version
```

La commande affiche le numéro de version (par exemple `git version 2.55.0`). Si le terminal répond que la commande est introuvable, Git n'est pas installé ou n'est pas dans la variable d'environnement `PATH`.

#### 1.2.1 Windows

**Méthode 1 : installateur officiel.** Téléchargez l'installateur sur git-scm.com/download/win.

**Méthode 2 : ligne de commande avec `winget`.**

```powershell
winget install --id Git.Git -e --source winget
```

L'installateur propose de nombreuses options. Les plus importantes :

- **L'éditeur par défaut** : celui que Git ouvrira pour rédiger les messages de commit. Choisissez un éditeur que vous maîtrisez (VS Code, Notepad++, etc.). Vim est proposé par défaut mais déroute les débutants.
- **Le nom de la branche initiale** : choisissez `main` (« override the default branch name »).
- **L'ajustement de la variable PATH** : l'option recommandée (« Git from the command line and also from 3rd-party software ») rend Git disponible dans l'invite de commandes et PowerShell.
- **La conversion des fins de ligne** : l'option par défaut (`core.autocrlf=true`) convient sous Windows (voir 1.3.5).
- **Le terminal** : **Git Bash** (émulateur Bash, très courant) ou la console Windows standard.
- **Le gestionnaire d'identifiants** : laissez **Git Credential Manager** activé (voir 1.5).

#### 1.2.2 macOS

```bash
brew install git            # recommandé (version à jour)
xcode-select --install      # alternative : outils en ligne de commande Xcode
```

Homebrew est un gestionnaire de paquets qui installe la dernière version stable de Git et la met à jour facilement. L'alternative `xcode-select --install` installe les outils de développement d'Apple, dont une version de Git.

> **Attention** : le Git fourni par Apple est souvent plus ancien que la dernière version. Si `git --version` affiche un numéro ancien après l'installation par Homebrew, vérifiez l'ordre de votre `PATH` (`which git`).

#### 1.2.3 Linux

```bash
# Debian / Ubuntu
sudo apt update && sudo apt install git

# Fedora / CentOS / RHEL
sudo dnf install git

# Arch
sudo pacman -S git
```

Les dépôts officiels des distributions fournissent parfois une version un peu en retard. Les mainteneurs de certaines distributions proposent des dépôts alternatifs (par exemple un PPA pour Ubuntu) si vous avez besoin de la toute dernière version. Il est aussi possible de compiler Git depuis les sources, ce qui est rarement nécessaire.

#### 1.2.4 Vérification complète

```bash
git --version        # numéro de version
git help             # liste des commandes courantes
git help commit      # manuel de la commande commit (équivalent à git commit --help)
```

L'aide intégrée est la meilleure référence : chaque commande possède une page de manuel complète. Prenez l'habitude de la consulter.

### 1.3 Configurer Git (`git config`)

#### 1.3.1 Pourquoi configurer Git ?

Git enregistre dans chaque commit l'**identité de son auteur**. Sans nom ni adresse e-mail renseignés, il refuse de créer un commit ou en devine une valeur peu fiable. La configuration permet aussi d'adapter le comportement de nombreuses commandes à vos préférences.

#### 1.3.2 L'identité

```bash
git config --global user.name "Votre Nom"
git config --global user.email "vous@exemple.com"
```

Ces informations sont inscrites dans chaque commit et deviennent publiques si le dépôt l'est. Sur GitHub, l'adresse e-mail sert à rattacher vos commits à votre compte : utilisez l'adresse associée au compte, ou l'adresse anonyme `noreply` fournie par la plateforme si vous souhaitez protéger votre vie privée.

#### 1.3.3 Les trois niveaux de configuration

Git lit sa configuration dans plusieurs fichiers, du plus général au plus précis.

| Niveau | Option | Fichier | Portée |
| --- | --- | --- | --- |
| Système | `--system` | `/etc/gitconfig` | Tous les utilisateurs de la machine |
| Global (utilisateur) | `--global` | `~/.gitconfig` (ou `~/.config/git/config`) | Tous vos dépôts |
| Local (dépôt) | `--local` (par défaut) | `.git/config` | Le dépôt courant uniquement |

Le niveau le plus précis l'emporte : **local > global > système**. C'est ce qui permet, par exemple, d'utiliser une adresse e-mail professionnelle dans un dépôt particulier tout en gardant une adresse personnelle par défaut :

```bash
cd projet-entreprise
git config user.email "prenom.nom@entreprise.com"   # niveau local
```

Les fichiers de configuration sont des fichiers texte au format INI. Vous pouvez les éditer directement avec `git config --global --edit`.

#### 1.3.4 Commandes de consultation et de modification

```bash
git config --list                      # toutes les valeurs effectives
git config --list --show-origin        # avec le fichier d'où vient chaque valeur
git config user.name                   # lire une valeur
git config --global --unset user.name  # supprimer une valeur
git config --global --edit             # ouvrir le fichier dans l'éditeur
```

L'option `--show-origin` est précieuse pour diagnostiquer un comportement inattendu : elle indique quel fichier impose chaque réglage.

#### 1.3.5 Réglages recommandés *(à jour)*

```bash
git config --global init.defaultBranch main     # branche initiale = main
git config --global pull.rebase false           # fusion au pull (true : rebase)
git config --global core.editor "code --wait"   # éditeur (VS Code)
git config --global color.ui auto
git config --global push.autoSetupRemote true   # git push crée la branche distante au besoin
git config --global rerere.enabled true         # mémorise les résolutions de conflits
```

Explication de chaque réglage :

- **`init.defaultBranch main`** : nomme `main` la première branche créée par `git init`. Historiquement, Git la nommait `master`. La convention actuelle des plateformes est `main`, et Git 3.0 en fera la valeur par défaut.
- **`pull.rebase`** : détermine ce que fait `git pull` quand les historiques local et distant ont divergé. Avec `false`, Git fusionne (crée un commit de fusion) ; avec `true`, il rebase (rejoue vos commits par-dessus ceux du distant). Avec `only`-style, `pull.ff only` refuse tout sauf une avance rapide. Ce choix est abordé en détail aux chapitres 4 et 6.
- **`core.editor`** : l'éditeur lancé pour les messages de commit et les rebases interactifs. L'option `--wait` indique à VS Code de ne rendre la main à Git que lorsque la fenêtre est fermée ; sans elle, Git croirait le message vide.
- **`color.ui auto`** : active la coloration de la sortie quand elle s'affiche dans un terminal.
- **`push.autoSetupRemote true`** : lors du premier `git push` d'une nouvelle branche, crée automatiquement la branche distante et mémorise le suivi, sans avoir à écrire `-u origin <branche>`.
- **`rerere.enabled true`** : active *reuse recorded resolution* ; Git mémorise la façon dont vous avez résolu un conflit et la réapplique automatiquement si le même conflit se reproduit (voir 6.1).

| Option | Rôle |
| --- | --- |
| `user.name`, `user.email` | Identité de l'auteur |
| `core.editor` | Éditeur pour les messages de commit |
| `merge.tool`, `diff.tool` | Outils de fusion et de comparaison graphiques |
| `init.defaultBranch` | Nom de la branche créée par `git init` |
| `pull.rebase` | Stratégie de `git pull` (fusion ou rebase) |
| `core.autocrlf` | Gestion des fins de ligne |

#### 1.3.6 Les fins de ligne (`core.autocrlf`)

Les systèmes d'exploitation n'encodent pas la fin d'une ligne de la même façon : Windows utilise deux caractères (retour chariot et saut de ligne, **CRLF**), Linux et macOS en utilisent un seul (**LF**). Si des développeurs travaillent sur des systèmes différents, des fichiers entiers peuvent apparaître comme modifiés à cause de ces seuls caractères invisibles.

| Valeur | Comportement | Usage |
| --- | --- | --- |
| `true` | Convertit en LF à l'enregistrement, en CRLF à l'extraction | Windows |
| `input` | Convertit en LF à l'enregistrement, ne touche pas à l'extraction | Linux et macOS |
| `false` | Aucune conversion | Projets exclusivement Windows, ou gestion par `.gitattributes` |

Une approche plus robuste consiste à décrire la règle dans le dépôt lui-même, avec un fichier `.gitattributes` (voir 7.7), pour que tous les contributeurs appliquent le même comportement.

### 1.4 Architecture : les trois zones de Git

Comprendre les trois zones est la clé de tout le reste du cours.

#### 1.4.1 Description des zones

| Zone | Rôle |
| --- | --- |
| **Répertoire de travail** (*working directory*) | Vos fichiers actuels, que vous éditez avec vos outils habituels |
| **Index / zone de préparation** (*staging area*) | Modifications sélectionnées pour le prochain commit |
| **Dépôt** (*repository*, dossier `.git`) | Historique des commits enregistrés |

```text
Répertoire de travail ──git add──▶ Index ──git commit──▶ Dépôt local ──git push──▶ Dépôt distant
        ▲                                                       │
        └───────────── git restore / git checkout ◀─────────────┘
```

#### 1.4.2 Pourquoi une zone intermédiaire ?

L'index est la particularité la plus déroutante de Git pour un débutant, mais aussi son atout. Il permet de **construire un commit avec précision**. Imaginez que vous avez corrigé un bug et, en même temps, commencé à reformater un autre fichier. Grâce à l'index, vous pouvez n'indexer que le correctif, le valider avec son propre message, puis traiter le reformatage dans un second commit. Sans index, chaque commit contiendrait tout ce qui a été modifié.

#### 1.4.3 Les quatre états d'un fichier

Pour Git, chaque fichier du répertoire de travail se trouve dans l'un de ces états :

1. **Non suivi** (*untracked*) : Git ne le connaît pas encore (fichier nouvellement créé).
2. **Inchangé** (*unmodified*) : suivi, identique à la dernière version validée.
3. **Modifié** (*modified*) : suivi, changé depuis le dernier commit, mais pas encore indexé.
4. **Indexé** (*staged*) : sa version actuelle est inscrite dans l'index et fera partie du prochain commit.

```text
Non suivi ──add──▶ Indexé ──commit──▶ Inchangé ──édition──▶ Modifié ──add──▶ Indexé
```

Un même fichier peut apparaître à la fois indexé et modifié : c'est le cas si vous l'indexez puis le modifiez à nouveau avant de valider. L'index contient alors la première version, le répertoire de travail la seconde.

#### 1.4.4 Le contenu du dossier `.git`

Le dossier `.git`, créé par `git init` ou `git clone`, **est** le dépôt. Supprimer ce dossier fait perdre tout l'historique et ne laisse que les fichiers du répertoire de travail. Il contient notamment :

| Élément | Rôle |
| --- | --- |
| `objects/` | Base de données des objets (blobs, arbres, commits, étiquettes) |
| `refs/` | Références : branches, étiquettes, branches distantes |
| `HEAD` | Désigne la branche ou le commit courant |
| `index` | Fichier binaire de l'index |
| `config` | Configuration locale du dépôt |
| `hooks/` | Scripts exécutés à certains moments |

Ne modifiez jamais ces fichiers à la main sans comprendre leur rôle. Le chapitre 7 détaille ce fonctionnement interne.

### 1.5 Authentification : SSH, HTTPS et GitHub CLI

#### 1.5.1 Protocoles de transport

Pour dialoguer avec un dépôt distant, Git utilise un protocole identifié par l'URL :

| Protocole | Exemple d'URL | Remarque |
| --- | --- | --- |
| HTTPS | `https://github.com/utilisateur/depot.git` | Le plus universel ; passe les pare-feu |
| SSH | `git@github.com:utilisateur/depot.git` | Authentification par clé cryptographique |
| Local | `/chemin/vers/depot.git` | Dépôt sur le même système de fichiers |

Les lectures de dépôts publics ne requièrent aucune authentification. Pour **écrire** (`push`) ou pour accéder à un dépôt privé, vous devez prouver votre identité. Trois méthodes existent.

> **Attention** : les **mots de passe de compte** ne sont plus acceptés par GitHub pour les opérations Git (depuis 2021). Utilisez une clé SSH, un **jeton d'accès personnel** (*personal access token*, PAT) ou un gestionnaire d'identifiants.

#### 1.5.2 Option A : clés SSH (recommandé)

**Principe.** SSH repose sur la **cryptographie asymétrique**. Vous générez une paire de clés : une **clé privée**, qui reste secrète sur votre machine, et une **clé publique**, que vous déposez sur la plateforme. Quand vous vous connectez, la plateforme envoie un défi que seule la clé privée correspondante sait résoudre. Aucun mot de passe ne circule sur le réseau.

**Étape 1 : vérifier les clés existantes.**

```bash
ls -al ~/.ssh
```

Cherchez des fichiers comme `id_ed25519` et `id_ed25519.pub` (clé privée et clé publique). Si vous en avez déjà une, vous pouvez la réutiliser.

**Étape 2 : générer une clé.** Ed25519 est le choix actuel : plus sûr et plus court que RSA.

```bash
ssh-keygen -t ed25519 -C "vous@exemple.com"
```

L'option `-C` ajoute un commentaire d'identification. Acceptez l'emplacement proposé et définissez une **phrase secrète** (*passphrase*) : elle chiffre la clé privée sur le disque, de sorte qu'un vol de fichier ne suffise pas à l'utiliser. Si Ed25519 n'est pas disponible sur un très vieux système :

```bash
ssh-keygen -t rsa -b 4096 -C "vous@exemple.com"
```

**Étape 3 : ajouter la clé à `ssh-agent`.** L'agent garde la clé déchiffrée en mémoire pour que vous ne retapiez pas la phrase secrète à chaque opération.

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Sous macOS, vous pouvez aussi enregistrer la phrase secrète dans le trousseau : `ssh-add --apple-use-keychain ~/.ssh/id_ed25519`. Sous Windows (PowerShell), le service `ssh-agent` doit être démarré avant d'utiliser `ssh-add`.

**Étape 4 : enregistrer la clé publique sur la plateforme.**

```bash
cat ~/.ssh/id_ed25519.pub     # copiez le résultat
```

Sur GitHub : *Settings, puis SSH and GPG keys, puis New SSH key*. Sur GitLab : *Preferences, puis SSH Keys*. Ne copiez **jamais** le fichier sans extension `.pub` : c'est la clé privée.

**Étape 5 : tester la connexion.**

```bash
ssh -T git@github.com
```

À la première connexion, SSH demande de confirmer l'empreinte du serveur ; comparez-la avec celle publiée par la plateforme avant d'accepter. Un message de bienvenue contenant votre nom d'utilisateur confirme que tout fonctionne.

**Gérer plusieurs clés.** Si vous avez des comptes différents (personnel, professionnel), le fichier `~/.ssh/config` permet d'associer une clé à chaque hôte :

```text
Host github.com
    IdentityFile ~/.ssh/id_ed25519
    AddKeysToAgent yes
```

#### 1.5.3 Option B : HTTPS avec gestionnaire d'identifiants

Avec HTTPS, il faut présenter un identifiant et un secret à chaque opération. Le secret est un **jeton d'accès personnel** (PAT), généré dans les paramètres de la plateforme, avec des permissions limitées (lecture, écriture sur certains dépôts) et une date d'expiration. Un **gestionnaire d'identifiants** stocke ce jeton de façon sécurisée pour ne pas le retaper.

**Git Credential Manager** est inclus avec Git pour Windows ; il gère aussi l'authentification par navigateur.

```bash
# Windows
git config --global credential.helper manager

# macOS
git config --global credential.helper osxkeychain
```

Sous Linux, plusieurs assistants existent (`libsecret`, ou `cache` qui conserve le secret en mémoire pour une durée limitée).

> **Attention** : ne placez jamais un jeton dans une URL de remote (`https://jeton@github.com/...`) : il serait stocké en clair dans `.git/config` et risquerait d'être divulgué.

#### 1.5.4 Option C : GitHub CLI *(ajout)*

```bash
gh auth login      # authentification guidée (navigateur ou jeton)
gh auth setup-git  # configure Git pour utiliser cette authentification
```

`gh` est l'outil officiel en ligne de commande de GitHub. Il guide l'authentification pas à pas et peut même téléverser une clé SSH pour vous.

#### 1.5.5 Comparaison et choix

| Critère | SSH | HTTPS + gestionnaire |
| --- | --- | --- |
| Mise en place | Un peu plus longue, une seule fois | Rapide |
| Sécurité | Très bonne (clé privée, phrase secrète) | Bonne (jeton limité et révocable) |
| Pare-feu d'entreprise | Port 22 parfois bloqué | Passe presque toujours |
| Confort | Aucun mot de passe ensuite | Aucun mot de passe ensuite |

Pour changer de protocole sur un dépôt existant, modifiez l'URL du remote : `git remote set-url origin git@github.com:utilisateur/depot.git`.

#### 1.5.6 Dépannage

| Message | Cause probable |
| --- | --- |
| `Permission denied (publickey)` | Clé non enregistrée sur la plateforme ou non chargée dans `ssh-agent` |
| `Authentication failed` (HTTPS) | Jeton expiré ou permissions insuffisantes |
| `Host key verification failed` | Empreinte du serveur modifiée ou absente de `known_hosts` |

### 1.6 Prérequis et environnement de travail

**Connaissances requises.**

- Savoir utiliser un terminal : se déplacer (`cd`, `pwd`), lister (`ls` ou `dir`), créer un dossier (`mkdir`), afficher un fichier (`cat`) et rediriger une sortie (`>`).
- Avoir une notion de fichier texte et d'arborescence de dossiers. Aucune expérience préalable de Git n'est nécessaire.

**Outils à préparer.**

- **Git** en version 2.23 ou plus récente (pour `git switch` et `git restore`), et un **terminal** : Git Bash ou PowerShell sous Windows, Terminal sous macOS, shell sous Linux.
- Un **éditeur** de texte ou de code (VS Code, par exemple), à déclarer comme éditeur de Git avec `core.editor` (voir 1.3).
- Un **compte** sur une plateforme d'hébergement (GitHub, GitLab, Codeberg) et une méthode d'authentification (voir 1.5).
- Facultatif : **GitHub CLI** (`gh`) et une **interface graphique** pour visualiser l'historique (chapitre 10).

> **À retenir.** Créez dès maintenant un dossier de pratique jetable (par exemple `~/atelier-git`) : le cours se lit mieux en reproduisant chaque exemple, et un dépôt de test permet de se tromper sans conséquence.

### 1.7 Pièges fréquents

- **Confondre Git et GitHub.** Git est le logiciel local ; GitHub, GitLab ou Bitbucket sont des services d'hébergement. On peut utiliser Git sans aucun service.
- **Oublier de configurer l'identité** (`user.name`, `user.email`) : Git refuse de créer un commit ou y inscrit une valeur devinée, et l'historique devient difficile à attribuer.
- **Croire que Git stocke des différences.** Il stocke des instantanés ; les différences se calculent à la demande.
- **Utiliser un mot de passe de compte pour pousser.** Les plateformes ne l'acceptent plus ; utilisez une clé SSH, un jeton d'accès personnel ou un gestionnaire d'identifiants.
- **Copier la clé privée au lieu de la clé publique** (`id_ed25519` au lieu de `id_ed25519.pub`) : la clé privée ne quitte jamais votre machine.
- **Négliger l'index.** Ce n'est pas un détail : il permet de construire des commits précis et explique la plupart des affichages de `git status`.
- **Supprimer le dossier `.git`.** Cela efface tout l'historique : les fichiers restent, mais plus aucune version.
- **Se retrouver bloqué dans Vim** parce qu'aucun éditeur n'a été configuré : définissez `core.editor` (pour quitter Vim : `Échap`, puis `:q!` ou `:wq`).

### 1.8 Glossaire du chapitre

| Terme | Définition |
| --- | --- |
| Système de gestion de versions (VCS) | Outil qui enregistre l'historique des modifications d'un ensemble de fichiers |
| Système distribué (DVCS) | VCS où chaque clone contient l'historique complet (Git, Mercurial) |
| Dépôt (*repository*) | Base de données de l'historique d'un projet, stockée dans `.git` |
| Répertoire de travail | Les fichiers que vous éditez, extraits d'un commit |
| Index (*staging area*) | Zone de préparation du prochain commit |
| Commit | Instantané enregistré, avec auteur, date, message et parents |
| Hash | Empreinte cryptographique qui identifie un objet de façon unique |
| Branche | Pointeur mobile vers un commit |
| `HEAD` | Pointeur qui désigne la position courante |
| Remote | Raccourci nommé vers un dépôt distant (par convention `origin`) |
| Clone | Copie complète d'un dépôt, historique compris |
| Clé SSH | Paire de clés (privée et publique) servant à s'authentifier sans mot de passe |

### Synthèse du chapitre 1

Git est un système de gestion de versions **distribué** : chaque clone contient l'historique complet, et presque toutes les opérations sont locales. Il enregistre des **instantanés** identifiés par des empreintes cryptographiques, ce qui garantit l'intégrité de l'historique. Le travail circule entre trois zones (répertoire de travail, index, dépôt), et chaque fichier passe par quatre états (non suivi, inchangé, modifié, indexé). Après avoir installé Git, configuré votre identité et choisi une méthode d'authentification (clé SSH recommandée), vous disposez de tout le nécessaire pour aborder le cycle de travail du chapitre 2.

---

## 2. Bases de Git (niveau débutant)

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez créer ou cloner un dépôt ; lire la sortie de `git status` ; indexer des modifications de façon sélective ; valider avec des messages de commit soignés (Conventional Commits) ; consulter et filtrer l'historique ; ignorer des fichiers avec `.gitignore` ; et enchaîner le cycle de travail quotidien.

Ce chapitre présente le cycle de travail quotidien : créer ou obtenir un dépôt, observer son état, préparer des changements, les valider, consulter l'historique et ignorer les fichiers inutiles. Maîtriser ces gestes suffit à travailler seul de façon professionnelle.

### 2.1 Créer un dépôt (`git init`)

#### 2.1.1 Principe

`git init` transforme un dossier ordinaire en dépôt Git. Il peut s'appliquer à un dossier vide ou à un projet existant qui n'était pas encore versionné.

```bash
mkdir monprojet
cd monprojet
git init
```

La commande crée un dossier caché **`.git`** contenant toute la base de données du dépôt (objets, références, configuration locale, index). Aucun fichier de votre projet n'est modifié et aucun commit n'est créé : le dépôt est simplement prêt à recevoir un historique.

Pour imposer le nom de la branche initiale : `git init -b main`. Si vous avez configuré `init.defaultBranch` (chapitre 1), l'option est inutile.

#### 2.1.2 Points d'attention

- Exécutez `git init` **à la racine du projet**, pas dans un sous-dossier. Un dépôt imbriqué par erreur est une source de confusion fréquente.
- Ne l'exécutez pas dans votre dossier personnel entier : Git tenterait de suivre tout son contenu.
- Pour savoir si vous êtes dans un dépôt : `git rev-parse --show-toplevel` affiche la racine du dépôt, ou une erreur `fatal: not a git repository` si ce n'est pas le cas.
- Pour « déversionner » un projet, il suffit de supprimer le dossier `.git` : l'historique est perdu, les fichiers restent.

### 2.2 Cloner un dépôt (`git clone`)

#### 2.2.1 Principe

`git clone` copie un dépôt existant, en récupérant **tous les fichiers et tout l'historique**. Il fait en une seule opération : création du dossier, `git init`, enregistrement du remote nommé `origin`, téléchargement de toutes les données, puis extraction de la branche par défaut.

```bash
git clone https://github.com/utilisateur/depot.git               # via HTTPS (crée le dossier depot)
git clone git@github.com:utilisateur/depot.git depot-ssh         # via SSH, dans un dossier distinct
git clone https://github.com/utilisateur/depot.git mon-dossier   # dans un dossier au nom choisi
```

Par défaut, le dossier créé porte le nom du dépôt (sans le suffixe `.git`). Un second argument permet de choisir un autre nom.

#### 2.2.2 Variantes utiles *(ajout)*

| Commande | Effet |
| --- | --- |
| `git clone --depth 1 <url>` | Clone **superficiel** (*shallow*) : seulement le dernier commit ; très rapide, mais historique tronqué |
| `git clone --filter=blob:none <url>` | Clone **partiel** : l'historique complet est récupéré, mais le contenu des fichiers est téléchargé à la demande |
| `git clone --branch <nom> <url>` | Extrait une branche ou une étiquette précise au lieu de la branche par défaut |
| `git clone --recurse-submodules <url>` | Clone aussi les sous-modules (voir 7.6) |

Un clone superficiel est idéal pour une CI ou pour consulter rapidement un gros dépôt. Il se complète plus tard par `git fetch --unshallow`. Le clone partiel conserve toutes les possibilités de navigation dans l'historique tout en économisant l'espace et le temps.

#### 2.2.3 Que contient un clone ?

Après un clone, vous disposez de : une branche locale (généralement `main`) qui suit `origin/main`, un remote `origin` pointant vers l'URL d'origine, et des **branches de suivi distantes** (`origin/main`, `origin/feature/...`) qui mémorisent l'état du serveur lors de la dernière synchronisation. Ces notions sont détaillées au chapitre 4.

### 2.3 Voir l'état (`git status`)

#### 2.3.1 Utilisation

```bash
git status          # état complet
git status -s       # version courte
```

`git status` est la commande que l'on exécute le plus souvent. Elle compare trois choses : le répertoire de travail, l'index et le dernier commit. Elle affiche trois catégories :

1. **Changes to be committed** : fichiers indexés (différences entre l'index et le dernier commit).
2. **Changes not staged for commit** : fichiers suivis et modifiés, non indexés (différences entre le répertoire de travail et l'index).
3. **Untracked files** : fichiers que Git ne suit pas encore.

La première ligne indique la branche courante et sa position par rapport à la branche distante suivie (par exemple *Your branch is ahead of 'origin/main' by 2 commits*). Git propose aussi dans sa sortie les commandes utiles pour passer à l'étape suivante.

#### 2.3.2 Lire la version courte

```text
 M README.md
M  index.html
MM style.css
A  nouveau.js
D  ancien.txt
?? notes.txt
```

Chaque ligne comporte deux colonnes de lettres : la première décrit l'**index**, la seconde le **répertoire de travail**.

| Code | Signification |
| --- | --- |
| `  M ` | Modifié dans le répertoire de travail, non indexé |
| ` M  ` | Modifié et indexé |
| `MM` | Indexé, puis modifié à nouveau |
| ` A  ` | Ajouté (nouveau fichier indexé) |
| ` D  ` | Suppression indexée |
| ` R  ` | Renommé |
| `??` | Non suivi |
| `UU` | Conflit de fusion non résolu |

### 2.4 Préparer les changements (`git add`)

#### 2.4.1 Rôle

`git add` copie dans l'index l'**état actuel** d'un fichier. Deux points sont essentiels :

- La commande sert à deux choses : **commencer à suivre** un nouveau fichier et **indexer** une modification d'un fichier déjà suivi.
- Elle capture le contenu **au moment où elle est exécutée**. Si vous modifiez le fichier après `git add`, la nouvelle modification n'est pas indexée tant que vous ne relancez pas `git add`.

```bash
git add fichier.txt      # un fichier
git add dossier/         # un dossier
git add .                # tout (nouveaux, modifiés, supprimés) dans le dossier courant
git add -u               # seulement les fichiers DÉJÀ suivis (modifiés / supprimés)
git add -p               # choisir interactivement les morceaux (hunks) à indexer
```

| Forme | Nouveaux fichiers | Fichiers modifiés | Fichiers supprimés |
| --- | --- | --- | --- |
| `git add .` | oui | oui | oui |
| `git add -u` | non | oui | oui |
| `git add <fichier>` | oui (ce fichier) | oui (ce fichier) | oui (ce fichier) |

#### 2.4.2 Indexation interactive par morceaux (`git add -p`)

Un **morceau** (*hunk*) est un bloc contigu de lignes modifiées. Avec `git add -p`, Git présente les morceaux un par un et demande quoi faire :

| Réponse | Effet |
| --- | --- |
| `y` | Indexer ce morceau |
| `n` | Ne pas l'indexer |
| `s` | Scinder le morceau en morceaux plus petits |
| `e` | Éditer manuellement le morceau |
| `q` | Quitter |
| `?` | Afficher l'aide |

> **Astuce** : `git add -p` permet de réaliser des commits **petits et cohérents** même quand vous avez modifié plusieurs choses à la fois dans un même fichier. Prenez l'habitude de relire vos modifications morceau par morceau : c'est aussi une auto-relecture efficace.

#### 2.4.3 Supprimer et renommer

```bash
git rm fichier.txt              # supprime le fichier et indexe la suppression
git rm --cached secret.env      # arrête de suivre le fichier mais le garde sur le disque
git mv ancien.txt nouveau.txt   # renomme / déplace
```

- `git rm fichier.txt` équivaut à supprimer le fichier avec votre système, puis à exécuter `git add` sur cette suppression.
- `git rm --cached` retire le fichier de l'index sans le toucher sur le disque. C'est la commande à utiliser lorsqu'un fichier a été suivi par erreur (fichier de secrets, dossier de build) et doit désormais être ignoré.
- `git mv ancien nouveau` équivaut à renommer le fichier avec le système puis à faire `git rm` de l'ancien nom et `git add` du nouveau. Git ne mémorise pas explicitement les renommages : il les **détecte** après coup en comparant les contenus (un fichier disparu et un fichier apparu quasi identiques sont présentés comme un renommage).
- Les suppressions et renommages effectués sans Git apparaissent dans `git status` ; il suffit alors de les indexer avec `git add -A` ou `git add .`.

### 2.5 Valider les changements (`git commit`)

#### 2.5.1 Qu'est-ce qu'un commit ?

Un **commit** est un instantané de l'index, enregistré de façon permanente dans le dépôt. Il contient :

- une référence vers l'arbre complet des fichiers au moment du commit ;
- la référence de son ou de ses **commits parents** (aucun pour le premier, deux pour une fusion) ;
- l'**auteur** et le **validateur** (*committer*), avec date et heure ;
- un **message**.

Le tout est résumé par un **hash**. Les commits forment ainsi une chaîne, chacun pointant vers son parent. Ce hash dépend du contenu, du parent et des métadonnées : changer un seul élément produit un hash différent. C'est pourquoi « modifier » un commit revient en réalité à en créer un nouveau.

```bash
git commit -m "Ajoute les fichiers initiaux du projet"
git commit                       # ouvre l'éditeur pour un message détaillé
git commit -am "Corrige le calcul"   # add -u + commit (fichiers déjà suivis seulement)
git commit --amend               # modifie le DERNIER commit (message et/ou contenu)
```

- `-m` fournit le message directement en ligne de commande.
- Sans `-m`, l'éditeur configuré s'ouvre : écrivez le message, enregistrez et fermez. Un message vide annule le commit.
- `-a` indexe automatiquement les fichiers **déjà suivis** et modifiés avant de valider (les nouveaux fichiers ne sont pas concernés).
- `--amend` remplace le dernier commit par un nouveau commit (voir 5.4).

#### 2.5.2 Rédiger de bons messages de commit

Le message est destiné aux humains qui liront l'historique, y compris vous-même dans six mois. Il doit répondre à la question *pourquoi ce changement ?* plus qu'à *que contient-il ?*, car le contenu se lit déjà dans le diff.

```text
type(portée): résumé court à l'impératif (≤ 50 caractères)

Corps facultatif : explique le POURQUOI du changement,
pas seulement le quoi. Ligne de 72 caractères maximum.
```

Règles usuelles :

1. Une **ligne de résumé** de 50 caractères environ, à l'impératif (« Ajoute », « Corrige »), sans point final.
2. Une **ligne vide**, puis un **corps** facultatif, dont les lignes dépassent rarement 72 caractères.
3. Le corps explique la motivation, les choix retenus, les conséquences, les liens vers les tickets.
4. Un commit = **un changement logique**. S'il faut utiliser « et » pour décrire le commit, il en contient probablement deux.

La convention **Conventional Commits** est très répandue. Le message commence par un type, éventuellement suivi d'une portée entre parenthèses et de deux-points :

| Type | Usage |
| --- | --- |
| `feat` | Nouvelle fonctionnalité |
| `fix` | Correction de bug |
| `docs` | Documentation |
| `refactor` | Réécriture sans changement de comportement |
| `test` | Ajout ou modification de tests |
| `chore` | Maintenance, outils |

Exemples : `feat(auth): ajoute la connexion par e-mail`, `fix(panier): corrige l'arrondi de la TVA`. Cette convention permet de générer automatiquement des journaux de modifications et de déduire le numéro de version suivant. Un changement incompatible se signale par un point d'exclamation après le type (`feat!:`) ou par une mention `BREAKING CHANGE:` dans le corps.

> **Attention** : **ne réécrivez** (`--amend`) **jamais** un commit déjà poussé et partagé : cela crée un historique différent de celui des autres contributeurs.

### 2.6 Consulter l'historique (`git log`)

#### 2.6.1 Principe

`git log` affiche les commits accessibles depuis le commit courant, **du plus récent au plus ancien**, avec hash, auteur, date et message. Dans la sortie par défaut, appuyez sur `q` pour quitter le pager.

```bash
git log
git log --oneline                    # un commit par ligne
git log -3 --oneline                 # les 3 derniers
git log --graph --oneline --all      # graphe des branches
git log --author="Alice"             # par auteur
git log --since="2 weeks ago"        # par date
git log -S"fonction"                 # commits qui ajoutent/suppriment ce texte
git log -p -- fichier.txt               # historique détaillé d'un fichier
git log --stat                       # fichiers modifiés par commit
git show <hash>                      # détail d'un commit
```

#### 2.6.2 Options d'affichage

| Option | Effet |
| --- | --- |
| `--oneline` | Hash abrégé et première ligne du message |
| `--graph` | Dessine en ASCII les branches et fusions |
| `--all` | Inclut toutes les branches, pas seulement la courante |
| `--decorate` | Affiche les noms de branches et d'étiquettes à côté des commits |
| `-p` (`--patch`) | Affiche le diff de chaque commit |
| `--stat` | Résumé des fichiers modifiés et du nombre de lignes |
| `--name-only` | Liste seulement les noms des fichiers modifiés |
| `-n` ou `-3` | Limite le nombre de commits |

Pour un format personnalisé, on utilise `--pretty=format:` :

```bash
git log --pretty=format:"%h %an %ad %s" --date=short
```

Les principaux marqueurs sont `%H` (hash complet), `%h` (hash abrégé), `%an` (auteur), `%ae` (e-mail), `%ad` (date), `%s` (sujet) et `%b` (corps).

#### 2.6.3 Options de filtrage

| Option | Effet |
| --- | --- |
| `--author="Alice"` | Commits dont l'auteur correspond |
| `--since`, `--until` | Filtre par date (`"2 weeks ago"`, `"2026-01-01"`) |
| `--grep="mot"` | Commits dont le *message* contient le mot |
| `-S"texte"` | Commits qui font **apparaître ou disparaître** ce texte dans le code (recherche dite « pickaxe ») |
| `-G"regex"` | Commits dont le diff correspond à l'expression régulière |
| `-- chemin` | Commits touchant ce fichier ou dossier |
| `--no-merges` | Exclut les commits de fusion |

Le séparateur `--` signale que ce qui suit est un chemin de fichier, ce qui évite toute ambiguïté avec un nom de branche.

#### 2.6.4 Plages de commits

| Notation | Signification |
| --- | --- |
| `A..B` | Commits accessibles depuis B mais pas depuis A |
| `main..feature` | Ce que `feature` contient en plus de `main` |
| `A...B` | Commits propres à l'une ou l'autre branche (différence symétrique) |

#### 2.6.5 Inspecter un commit (`git show`)

`git show <hash>` affiche le message du commit et son diff. On peut abréger le hash tant qu'il reste unique (généralement 7 caractères suffisent). `git show HEAD` affiche le dernier commit, `git show HEAD~2` celui d'il y a deux commits, et `git show <hash>:chemin/fichier` affiche le contenu d'un fichier tel qu'il était à ce commit.

### 2.7 Ignorer des fichiers (`.gitignore`)

#### 2.7.1 Pourquoi ignorer ?

Certains fichiers ne doivent pas être versionnés : dépendances téléchargées (`node_modules/`), fichiers générés (`build/`, binaires compilés), journaux, fichiers temporaires d'éditeur, et surtout **secrets** (mots de passe, jetons, fichiers `.env`). Le fichier `.gitignore`, placé à la racine du dépôt (ou dans un sous-dossier), liste ce que Git **ne doit pas suivre**.

```gitignore
# Dossier des dépendances
node_modules/

# Tous les fichiers .log
*.log

# Variables d'environnement (secrets !)
.env

# Tout le contenu de build, sauf un fichier précis
build/*
!build/.gitkeep
```

#### 2.7.2 Syntaxe des motifs

| Motif | Signification |
| --- | --- |
| `*.log` | Tous les fichiers `.log` |
| `dossier/` | Un dossier et son contenu |
| `/fichier` | Uniquement à la racine |
| `**/temp` | Dans tous les sous-dossiers |
| `!fichier` | **Exception** (ne pas ignorer) |

Règles complémentaires :

- Une ligne commençant par `#` est un commentaire ; une ligne vide est ignorée.
- `*` remplace n'importe quelle suite de caractères sauf `/` ; `?` remplace un seul caractère ; `[abc]` désigne un des caractères listés.
- Un motif **sans `/`** s'applique à tous les niveaux de l'arborescence ; un motif contenant un `/` est relatif à l'emplacement du `.gitignore`.
- Un motif **finissant par `/`** ne s'applique qu'aux dossiers.
- Les règles sont évaluées dans l'ordre ; **la dernière qui correspond l'emporte**, ce qui explique le rôle de `!`.
- On ne peut pas réinclure un fichier si son **dossier parent** est lui-même ignoré : d'où l'écriture `build/*` (le contenu) plutôt que `build/` (le dossier) dans l'exemple ci-dessus.
- Git ne suit pas les dossiers vides. Pour conserver un dossier vide, on y place un fichier convention nommé `.gitkeep` (nom purement conventionnel, sans effet particulier).

#### 2.7.3 Fichiers déjà suivis

> **Attention** : `.gitignore` n'agit pas sur les fichiers **déjà suivis**. Si un fichier a été validé avant d'être ajouté au `.gitignore`, Git continue de le suivre. Pour l'en retirer sans le supprimer du disque :

```bash
git rm --cached <fichier>
git commit -m "Arrête de suivre <fichier>"
```

Si le fichier contenait un secret, le retirer du suivi ne suffit pas : il reste dans l'historique (voir 11.2).

#### 2.7.4 Autres emplacements d'ignorance

| Emplacement | Portée |
| --- | --- |
| `.gitignore` (dans le dépôt) | Partagé avec toute l'équipe (il est versionné) |
| `.git/info/exclude` | Personnel, propre à ce dépôt, non partagé |
| Fichier global (`core.excludesFile`) | Personnel, tous vos dépôts (fichiers d'éditeur, fichiers du système) |

> **Astuce** : des modèles prêts à l'emploi par langage ou framework sont disponibles sur github.com/github/gitignore. Pour un ignore global personnel : `git config --global core.excludesFile ~/.gitignore_global`.

Pour comprendre pourquoi un fichier est ignoré, utilisez `git check-ignore -v <fichier>` : la commande indique la règle et le fichier responsable. Pour lister les fichiers ignorés : `git status --ignored`.

### 2.8 Exemple de workflow complet

```bash
git init                                   # 1. initialiser
git status                                 # 2. vérifier l'état
echo "Hello Git" > README.md               # 3. créer un fichier
git add README.md                          # 4. indexer
git commit -m "Ajoute le README"           # 5. valider
git log --oneline                          # 6. consulter l'historique
```

Commentaire étape par étape :

1. `git init` crée le dépôt vide.
2. `git status` annonce qu'aucun commit n'existe encore et qu'il n'y a rien à valider.
3. Le fichier `README.md` est créé : il apparaît dans `git status` comme **non suivi**.
4. `git add README.md` le place dans l'index : il devient **indexé**.
5. `git commit` enregistre l'instantané : le fichier est désormais **inchangé** (suivi et identique au dernier commit). La branche `main` pointe vers ce premier commit.
6. `git log --oneline` montre une ligne : le hash abrégé et le message.

#### Un cycle quotidien type

```bash
git status                  # que s'est-il passé ?
git diff                    # que contiennent mes modifications ?
git add -p                  # je choisis ce que je valide
git diff --staged           # je relis ce que je vais valider
git commit -m "feat: ..."   # j'enregistre
git log --oneline -5        # je vérifie
```

### 2.9 Pièges fréquents

- **Croire que `git add` suit les modifications futures.** La commande capture l'état du fichier **au moment** où elle s'exécute : une modification faite ensuite n'est pas indexée tant que vous ne relancez pas `git add`.
- **Utiliser `git add .` sans relire `git status`.** Vous risquez d'indexer des fichiers de secrets, de build ou très volumineux. Relisez toujours `git status` et `git diff --staged` avant de valider.
- **Ajouter un fichier au `.gitignore` après l'avoir validé.** Il reste suivi ; retirez-le du suivi avec `git rm --cached <fichier>`.
- **Oublier que `git commit -am` ignore les nouveaux fichiers.** L'option `-a` n'indexe que les fichiers déjà suivis.
- **Écrire des messages vagues** (« fix », « wip », « modifs ») : un commit doit exprimer un changement logique et son motif.
- **Amender un commit déjà poussé** (`--amend`) : le hash change, et l'historique diverge de celui des autres contributeurs.
- **Lancer `git init` au mauvais endroit** : dans un dossier trop large (votre dossier personnel) ou dans un dossier déjà inclus dans un dépôt (dépôt imbriqué).
- **Compter sur Git pour suivre un dossier vide.** Git ne suit que des fichiers ; ajoutez un fichier conventionnel `.gitkeep`.

### Synthèse du chapitre 2

Le cycle quotidien tient en quatre gestes : **observer** (`git status`, `git diff`), **préparer** (`git add`, de préférence `-p` pour choisir les morceaux), **valider** (`git commit` avec un message qui explique le pourquoi) et **vérifier** (`git log`). L'index permet de construire des commits atomiques. Le fichier `.gitignore` empêche de suivre ce qui ne doit pas l'être, mais n'agit pas sur les fichiers déjà suivis. `git init` crée un dépôt, `git clone` en récupère un avec tout son historique, et `git log` offre de nombreux filtres (`--author`, `--since`, `-S`, `--graph`) pour retrouver l'information.

---

## 3. Branches et étiquettes

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez expliquer qu'une branche est un simple pointeur ; créer, lister et changer de branche avec `git switch` ; distinguer l'avance rapide de la fusion à trois points ; utiliser `--no-ff` et `--squash` à bon escient ; supprimer des branches sans risque ; et marquer des versions avec des étiquettes légères et annotées selon le versionnement sémantique.

Les branches sont la fonctionnalité la plus caractéristique de Git. Ce chapitre explique ce qu'est réellement une branche, comment en créer, en fusionner et en supprimer, puis comment marquer des versions avec des étiquettes.

### 3.1 Comprendre les branches

#### 3.1.1 Définition

Une **branche** est un **pointeur léger et mobile vers un commit**. Techniquement, c'est un petit fichier (par exemple `.git/refs/heads/main`) qui contient simplement le hash d'un commit, soit environ 40 octets. Quand vous créez un commit sur une branche, Git déplace automatiquement ce pointeur vers le nouveau commit.

Cette conception explique pourquoi les branches sont si peu coûteuses : **créer une branche ne copie aucun fichier**, elle ajoute seulement un pointeur. Dans des systèmes plus anciens, créer une branche pouvait signifier dupliquer l'arborescence entière, d'où la réticence à en utiliser. Avec Git, on en crée pour la moindre tâche.

#### 3.1.2 L'historique est un graphe

Les commits forment un **graphe orienté acyclique** (*DAG*) : chaque commit pointe vers son ou ses parents. Les branches ne sont que des noms donnés à certaines extrémités de ce graphe.

```text
A ← B ← C ← D          main
          \
           E ← F        feature
```

Ici, `main` pointe vers D et `feature` vers F. Les commits A, B et C appartiennent aux deux branches : une branche n'« contient » que ce qui est accessible en remontant depuis son extrémité.

#### 3.1.3 Rôle et usage

Une branche permet de travailler sur une fonctionnalité, une correction ou une expérimentation **en isolation**, sans toucher au code principal. Le travail n'est intégré qu'une fois terminé et validé.

- La branche par défaut s'appelle aujourd'hui **`main`** (historiquement `master`).
- Créer une branche est quasi instantané.
- **`HEAD`** indique la branche (ou le commit) sur lequel vous travaillez. Quand vous commitez, c'est la branche pointée par `HEAD` qui avance.

#### 3.1.4 Nommer ses branches

Les noms de branches ne peuvent pas contenir d'espaces, de caractères de contrôle, ni les séquences `..`, `~`, `^`, `:`, `?`, `*`, `[`, et ne peuvent pas finir par `/` ou `.lock`. Au-delà des règles techniques, des conventions facilitent la lecture :

| Préfixe | Usage | Exemple |
| --- | --- | --- |
| `feature/` | Nouvelle fonctionnalité | `feature/login` |
| `fix/` ou `bugfix/` | Correction de bug | `fix/arrondi-tva` |
| `hotfix/` | Correctif urgent en production | `hotfix/1.2.1` |
| `release/` | Préparation d'une version | `release/2.0` |
| `docs/`, `chore/` | Documentation, maintenance | `docs/guide-install` |

Le caractère `/` crée un regroupement logique et permet de filtrer (`git branch --list "feature/*"`). Préférez des noms courts, en minuscules, avec des tirets, et incluez si possible le numéro de ticket (`feature/123-panier`).

### 3.2 Créer, lister et changer de branche

#### 3.2.1 Lister

```bash
git branch                      # liste (* = branche courante)
git branch -a                   # locales + distantes
git branch -vv                  # avec le dernier commit et la branche suivie
git branch feature/login        # crée (sans basculer)
```

- `git branch` seul affiche les branches locales ; un astérisque marque la branche courante.
- `-a` ajoute les branches de suivi distantes (`remotes/origin/...`).
- `-vv` affiche pour chaque branche le hash du dernier commit, son message et la branche distante suivie, avec l'écart (*ahead*, *behind*).
- `--merged` et `--no-merged` filtrent les branches déjà fusionnées ou non dans la branche courante : pratique pour nettoyer.

#### 3.2.2 Créer

`git branch <nom>` crée une branche **à partir du commit courant** sans basculer dessus. Pour partir d'un autre point, on le précise : `git branch <nom> <hash>` ou `git branch <nom> v1.0`. Pour renommer : `git branch -m ancien nouveau` (ou `git branch -m nouveau` pour renommer la branche courante).

#### 3.2.3 Changer de branche *(à jour)*

Changer de branche signifie modifier `HEAD` pour qu'il pointe vers elle, puis **remplacer le contenu du répertoire de travail** par celui du commit pointé. Depuis **Git 2.23**, deux commandes spécialisées remplacent les usages multiples de `git checkout` :

| Action | Commande moderne | Ancienne commande (héritage) |
| --- | --- | --- |
| Changer de branche | `git switch feature/login` | `git checkout feature/login` |
| Créer et basculer | `git switch -c feature/login` | `git checkout -b feature/login` |
| Revenir à la branche précédente | `git switch -` | `git checkout -` |
| Restaurer un fichier | `git restore fichier` | `git checkout -- fichier` |

> `git checkout` fonctionne toujours, mais **`switch`** (gère les branches) et **`restore`** (gère les fichiers) sont plus clairs et moins risqués : l'ancienne commande mélangeait deux concepts sans rapport.

#### 3.2.4 Que se passe-t-il pour les modifications en cours ?

Quand vous changez de branche avec des modifications non validées :

- si ces modifications ne touchent **aucun fichier différent** entre les deux branches, Git les emporte avec vous sur la nouvelle branche ;
- si elles entrent en conflit avec des fichiers qui diffèrent, Git **refuse** le changement et vous demande de valider, de mettre de côté (`git stash`, voir 5.7) ou d'abandonner vos modifications.

Il est donc recommandé de changer de branche avec un répertoire de travail propre.

#### 3.2.5 Se placer sur un commit : HEAD détaché

`git switch --detach <hash>` (ou `git switch --detach v1.0`) place `HEAD` directement sur un commit, sans branche. On parle de *detached HEAD*. C'est utile pour inspecter une ancienne version. Vos éventuels nouveaux commits n'appartiendraient à aucune branche ; pour les conserver, créez une branche : `git switch -c ma-branche` (voir 7.2).

### 3.3 Fusionner des branches (`git merge`)

#### 3.3.1 Principe

Fusionner consiste à intégrer dans la branche courante les commits d'une autre branche. On se place sur la branche **destinataire**, puis on fusionne l'autre :

```bash
git switch main
git merge feature/login
```

La branche `feature/login` n'est pas modifiée : seule `main` avance.

#### 3.3.2 Les deux types de fusion

**Avance rapide (*fast-forward*).** Si `main` n'a pas bougé depuis la création de `feature`, la branche `feature` est simplement « en avance » sur `main`. Il n'y a rien à combiner : Git déplace le pointeur `main` vers le dernier commit de `feature`. Aucun nouveau commit n'est créé et l'historique reste linéaire.

```text
Avant :   A ← B (main)
               \
                C ← D (feature)

Après :  A ← B ← C ← D (main, feature)
```

**Fusion à trois points (*three-way merge*).** Si les deux branches ont divergé (chacune possède des commits que l'autre n'a pas), Git ne peut plus avancer un pointeur. Il identifie le **dernier ancêtre commun** (*merge base*), compare chaque branche à cet ancêtre, combine les deux ensembles de modifications, puis crée un **commit de fusion** qui possède **deux parents**.

```text
Avant :   A ← B ← E (main)
               \
                C ← D (feature)

Après :  A ← B ← E ← M (main)
               \     /
                C ← D (feature)
```

Les trois « points » sont : l'ancêtre commun (B) et les deux extrémités (E et D).

#### 3.3.3 Options

| Type ou option | Description |
| --- | --- |
| **Avance rapide** | `main` n'a pas bougé : Git avance simplement le pointeur, sans commit de fusion |
| **Fusion à trois points** | Les deux branches ont divergé : Git crée un **commit de fusion** |
| `git merge --no-ff` | Force un commit de fusion même si l'avance rapide est possible (garde la trace de la branche) |
| `git merge --ff-only` | N'accepte que l'avance rapide, échoue sinon |
| `git merge --squash` | Condense toutes les modifications en **un seul** commit que vous validez vous-même ; pas de commit de fusion ni de lien avec la branche source |
| `git merge --abort` | Annule une fusion en cours (conflits) et revient à l'état d'avant |

Choisir `--no-ff` est utile si l'on souhaite pouvoir identifier plus tard « ces quatre commits formaient la fonctionnalité X » et pouvoir les annuler d'un seul `git revert -m 1`. `--squash` donne un historique très propre mais perd le détail des commits individuels.

#### 3.3.4 Le message de fusion

Pour un commit de fusion, Git propose un message par défaut (*Merge branch 'feature/login'*) et ouvre l'éditeur. Vous pouvez l'accepter ou le préciser. L'option `-m "message"` évite l'ouverture de l'éditeur.

#### 3.3.5 Vérifier le résultat

```bash
git log --graph --oneline --all
git branch --merged            # branches entièrement intégrées à la branche courante
```

En cas de conflit, voir la section 6.1. Une fusion en conflit n'est pas une erreur : c'est une situation normale que Git vous demande de trancher.

### 3.4 Supprimer des branches

```bash
git branch -d feature/login     # suppression sûre (refuse si non fusionnée)
git branch -D feature/login     # suppression forcée (perte possible)
git push origin --delete feature/login    # supprime la branche distante
git fetch --prune                         # nettoie les références distantes obsolètes
```

- Supprimer une branche ne supprime que le **pointeur**, pas les commits. Si la branche a été fusionnée, ses commits restent accessibles par la branche destinataire.
- `-d` vérifie que la branche est fusionnée dans la branche courante (ou dans sa branche distante suivie) et refuse sinon, pour éviter de perdre du travail.
- `-D` force la suppression : les commits non fusionnés deviennent inaccessibles (mais restent retrouvables un temps via `git reflog`, voir 9.3).
- Supprimer la branche **locale** ne supprime pas la branche **distante**, et inversement. `git fetch --prune` retire de votre dépôt local les branches de suivi dont l'original a été supprimé sur le serveur. Pour le faire systématiquement : `git config --global fetch.prune true`.
- On ne peut pas supprimer la branche sur laquelle on se trouve : basculez d'abord sur une autre.

### 3.5 Étiquettes (*tags*) pour marquer des versions

#### 3.5.1 Définition

Une **étiquette** est un pointeur **fixe** vers un commit. Contrairement à une branche, elle ne bouge pas quand on commite : elle désigne définitivement un instantané. On s'en sert pour marquer des versions publiées (`v1.0.0`) afin de pouvoir y revenir exactement.

#### 3.5.2 Versionnement sémantique

Suivez le **versionnement sémantique** (*SemVer*) : `MAJEUR.MINEUR.CORRECTIF`.

| Segment | Incrémenté quand... | Exemple |
| --- | --- | --- |
| MAJEUR | On introduit un changement **incompatible** avec les versions précédentes | 1.4.2 vers 2.0.0 |
| MINEUR | On ajoute une fonctionnalité **compatible** | 1.4.2 vers 1.5.0 |
| CORRECTIF | On corrige un bug de façon compatible | 1.4.2 vers 1.4.3 |

Lorsqu'un segment est incrémenté, ceux de droite repassent à zéro. Des suffixes de préversion existent (`2.0.0-beta.1`, `2.0.0-rc.1`).

#### 3.5.3 Deux types d'étiquettes

| Type | Description | Commande |
| --- | --- | --- |
| **Légère** | Simple pointeur vers un commit, sans métadonnées | `git tag v1.0` |
| **Annotée** (recommandée) | Objet complet : auteur, date, message, signature possible | `git tag -a v1.0 -m "Première version stable"` |

L'étiquette annotée est un objet à part entière dans la base de Git (voir 7.1) ; elle garde la trace de **qui** a publié la version et **quand**, et ses commandes de description (`git describe`) la privilégient. Pour les versions publiées, utilisez toujours des étiquettes annotées. L'étiquette légère convient pour un repère personnel temporaire.

#### 3.5.4 Commandes

```bash
git tag                          # lister
git tag -a v1.0 -m "Version 1.0"             # étiqueter le commit courant
git tag -a v0.9 <hash> -m "Version 0.9"      # étiqueter un ancien commit
git show v1.0                    # détails
git push origin v1.0             # pousser une étiquette
git push origin --tags           # pousser toutes les étiquettes
git push origin --delete v1.0    # supprimer côté distant
git tag -d v1.0                  # supprimer en local
```

> Les étiquettes **ne sont pas poussées automatiquement** : `git push` seul n'envoie que les branches. Il faut les pousser explicitement. L'option `git push --follow-tags` envoie uniquement les étiquettes annotées qui pointent vers des commits en cours d'envoi.

Compléments utiles :

- **Lister avec un motif** : `git tag -l "v1.*"`.
- **Trier par version** : `git tag --sort=version:refname`.
- **Signer une étiquette** : `git tag -s v1.0 -m "Version 1.0"` (voir 11.1 pour la configuration des clés).
- **Se placer sur une étiquette** : `git switch --detach v1.0` ; pour y travailler, créer une branche : `git switch -c hotfix-1.0 v1.0`.
- **Décrire la position courante** : `git describe` retourne la dernière étiquette accessible suivie du nombre de commits ajoutés depuis (par exemple `v1.0-3-g2a1b4c5`).
- **Déplacer une étiquette** : déconseillé une fois publiée. Si une étiquette est incorrecte, supprimez-la en local et sur le distant, puis recréez-la ; prévenez l'équipe.

#### 3.5.5 Branche ou étiquette ?

|  | Branche | Étiquette |
| --- | --- | --- |
| Mobilité | Avance à chaque commit | Fixe |
| Usage | Travail en cours | Version publiée, point de repère |
| Poussée | `git push` | Explicite (`git push origin <tag>`) |

### 3.6 Exemple de workflow

```bash
git switch -c feature/signup              # créer et basculer
echo "<h1>Inscription</h1>" > inscription.html   # créer un fichier
git add . && git commit -m "Ajoute la page d'inscription"
git switch main                           # revenir à main
git merge feature/signup                  # fusionner
git branch -d feature/signup              # supprimer la branche locale
git tag -a v1.0 -m "Version 1.0"          # étiqueter la release
git push origin main --tags               # pousser branche et étiquettes (nécessite un dépôt distant : voir la section 4)
```

Analyse du scénario : la branche `feature/signup` est créée depuis `main`. Comme `main` n'a pas évolué pendant ce temps, la fusion est une **avance rapide** : aucun commit de fusion n'apparaît. La branche est ensuite supprimée sans risque, car ses commits sont désormais accessibles par `main`. L'étiquette `v1.0` marque l'état de la version livrée.

### 3.7 Pièges fréquents

- **Croire qu'une branche est une copie des fichiers.** C'est un simple pointeur ; supprimer une branche supprime le pointeur, pas les commits (qui restent retrouvables un temps avec `git reflog`).
- **Fusionner dans le mauvais sens.** On se place d'abord sur la branche **destinataire** (`git switch main`), puis on fusionne l'autre (`git merge feature`).
- **Changer de branche avec des modifications non validées.** Git les emporte si aucun conflit n'est possible, ou refuse sinon ; validez ou mettez de côté (`git stash`) avant de changer.
- **Supprimer avec `-D` sans vérifier.** `-d` refuse de supprimer une branche non fusionnée, `-D` force et peut rendre des commits inaccessibles.
- **Travailler en HEAD détaché sans le savoir.** Les commits créés n'appartiennent à aucune branche ; créez une branche (`git switch -c <nom>`) avant de changer de position.
- **Oublier de pousser les étiquettes.** `git push` seul n'envoie que les branches ; utilisez `git push origin <étiquette>` ou `--follow-tags`.
- **Déplacer une étiquette déjà publiée.** Les autres clones ne la verront pas bouger ; supprimez-la et recréez-la en prévenant l'équipe, ou mieux, publiez une nouvelle version.
- **Utiliser une étiquette légère pour une version publiée.** Préférez l'étiquette annotée, qui conserve l'auteur, la date et un message.

### Synthèse du chapitre 3

Une **branche** est un pointeur léger vers un commit : en créer une ne coûte presque rien, d'où l'habitude d'en ouvrir une par tâche. `git switch` (à jour) change de branche et `git restore` restaure des fichiers, remplaçant les usages multiples de `git checkout` (héritage). Une fusion est soit une **avance rapide** (simple déplacement de pointeur), soit une **fusion à trois points** (commit de fusion à deux parents) ; `--no-ff` et `--squash` en modulent le résultat. Les **étiquettes** marquent des versions de façon fixe : annotées pour les publications, nommées selon le versionnement sémantique `MAJEUR.MINEUR.CORRECTIF`, et poussées explicitement.

---

## 4. Dépôts distants et collaboration

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez gérer des dépôts distants (`remote`) ; distinguer `fetch`, `pull` et `push` ; comprendre les branches de suivi distantes ; résoudre un refus *non-fast-forward* ; employer `--force-with-lease` plutôt que `--force` ; contribuer à un projet par fork et pull request ; et suivre l'état d'une branche par rapport à son distant.

Jusqu'ici, tout s'est passé sur votre machine. Ce chapitre explique comment Git synchronise des dépôts entre eux : récupérer le travail des autres, publier le vôtre, et contribuer à un projet dont on n'est pas propriétaire.

### 4.1 Ajouter un dépôt distant (`git remote`)

#### 4.1.1 Définition

Un **dépôt distant** (*remote*) est une version du projet hébergée ailleurs : sur une plateforme, un serveur, ou simplement un autre dossier de votre disque. Un *remote* est en réalité un **raccourci nommé** vers une URL. Le nom conventionnel du dépôt principal est **`origin`** : c'est le nom que Git donne automatiquement à la source d'un `git clone`.

Un dépôt peut avoir plusieurs remotes (par exemple `origin` pour votre fork et `upstream` pour le projet d'origine, voir 4.5).

#### 4.1.2 Commandes

```bash
git remote add origin https://github.com/utilisateur/monprojet.git
git remote -v                                                  # lister
git remote set-url origin https://github.com/utilisateur/nouveau-nom.git   # changer l'URL
git remote rename origin principal                             # renommer
git remote rename principal origin                             # revenir au nom conventionnel
git remote remove origin                                       # supprimer (inutile si vous poursuivez les exemples)
```

- `git remote add <nom> <url>` enregistre un nouveau remote. Il ne contacte pas le serveur et ne télécharge rien.
- `git remote -v` liste les remotes avec leurs URL de récupération (*fetch*) et d'envoi (*push*).
- `git remote set-url` modifie l'URL, par exemple pour passer de HTTPS à SSH ou après le renommage d'un dépôt.
- `git remote show origin` interroge le serveur et affiche en détail les branches suivies, la branche par défaut et l'état des synchronisations.
- La suppression d'un remote retire aussi ses branches de suivi locales.

#### 4.1.3 S'entraîner sans plateforme : le dépôt nu

Pour tester sans réseau, créez un **dépôt nu** (*bare*), c'est-à-dire un dépôt sans répertoire de travail, qui sert de point d'échange :

```bash
git init --bare /tmp/serveur.git
git remote add origin /tmp/serveur.git
git push -u origin main
```

C'est exactement ce que font les plateformes d'hébergement : elles stockent des dépôts nus. Un dépôt nu ne doit recevoir que des `push`, jamais de modifications directes de fichiers.

### 4.2 Récupérer sans fusionner (`git fetch`)

#### 4.2.1 Principe

`git fetch` télécharge depuis le remote les commits, étiquettes et références que vous n'avez pas encore, **sans modifier ni votre répertoire de travail ni vos branches locales**. C'est une opération sans danger, que l'on peut lancer à tout moment.

```bash
git fetch origin
git fetch --all --prune
git log HEAD..origin/main --oneline    # voir ce qui est arrivé
```

#### 4.2.2 Les branches de suivi distantes

Le résultat d'un `fetch` est enregistré dans des **branches de suivi distantes** (*remote-tracking branches*), de la forme `origin/main`, `origin/feature/chat`. Ce sont des copies **en lecture seule** de l'état des branches du serveur, tel que vous l'avez vu lors de la dernière synchronisation. Vous ne les modifiez pas directement : elles ne bougent que lors d'un `fetch`, d'un `pull` ou d'un `push`.

Cette distinction est capitale :

| Référence | Nature | Qui la fait avancer ? |
| --- | --- | --- |
| `main` | Branche **locale** | Vos commits, vos fusions |
| `origin/main` | Branche de suivi **distante** (copie locale de l'état du serveur) | `fetch`, `pull`, `push` |

#### 4.2.3 Examiner avant d'intégrer

Après un `fetch`, comparez avant de décider :

```bash
git log HEAD..origin/main --oneline   # commits distants que je n'ai pas
git log origin/main..HEAD --oneline   # mes commits que le distant n'a pas
git diff HEAD origin/main             # différences de contenu
```

Puis intégrez à votre rythme : `git merge origin/main` ou `git rebase origin/main`.

#### 4.2.4 Options utiles

| Option | Effet |
| --- | --- |
| `--all` | Récupère depuis tous les remotes |
| `--prune` (`-p`) | Supprime les branches de suivi dont l'original a disparu du serveur |
| `--tags` | Récupère aussi toutes les étiquettes |
| `--unshallow` | Complète un clone superficiel avec tout l'historique |

### 4.3 Récupérer et intégrer (`git pull`)

#### 4.3.1 Principe

`git pull` = **`git fetch` + intégration** de la branche distante dans la branche courante. Cette intégration est une fusion (*merge*) ou un rebase, selon la configuration ou l'option.

```bash
git pull                      # branche suivie
git pull origin main
git pull --rebase             # rejoue vos commits au-dessus (historique linéaire)
git pull --ff-only            # refuse tout sauf une avance rapide (le plus sûr)
```

#### 4.3.2 Les trois comportements

| Mode | Que se passe-t-il quand les historiques ont divergé ? | Historique obtenu |
| --- | --- | --- |
| Fusion (par défaut avec `pull.rebase false`) | Git crée un commit de fusion | Fidèle, avec des fusions |
| Rebase (`--rebase`) | Vos commits locaux sont rejoués au-dessus des commits distants | Linéaire |
| Avance rapide seule (`--ff-only`) | Git s'arrête avec une erreur, sans rien modifier | Inchangé |

Si les historiques n'ont pas divergé (vous n'avez aucun commit local que le distant n'a pas), les trois modes donnent le même résultat : une simple avance rapide.

Lorsque vous avez des commits locaux **et** que le distant en a de nouveaux, les versions récentes de Git exigent que vous exprimiez votre choix (option sur la ligne de commande ou réglage de configuration), faute de quoi elles affichent un message vous invitant à le faire. C'est la raison d'être des réglages ci-dessous.

> **Astuce** : pour fixer votre préférence une fois pour toutes : `git config --global pull.rebase true` (rebase) ou `git config --global pull.ff only` (avance rapide uniquement). Le mode `ff only` est le plus prudent : il vous oblige à faire explicitement un `merge` ou un `rebase` lorsque c'est nécessaire.

Si vous avez des modifications non validées, un `pull --rebase` peut refuser de démarrer. L'option `--autostash` (ou le réglage `rebase.autoStash`) met vos modifications de côté pendant l'opération et les réapplique ensuite.

### 4.4 Envoyer des changements (`git push`)

#### 4.4.1 Principe

`git push` envoie vos commits locaux vers le remote et fait avancer la branche correspondante sur le serveur.

```bash
git push origin main
git push -u origin ma-branche     # -u : mémorise la branche distante (suivi)
git push                          # ensuite, simplement
```

La syntaxe complète est `git push <remote> <branche-locale>:<branche-distante>`. Dans le cas courant où les deux noms sont identiques, on écrit un seul nom. L'option `-u` (`--set-upstream`) enregistre le lien entre votre branche locale et la branche distante : par la suite, `git push`, `git pull` et `git status` savent où chercher. Avec `push.autoSetupRemote true` (chapitre 1), ce suivi est mis en place automatiquement.

#### 4.4.2 Le refus *non-fast-forward*

Git n'accepte un `push` que s'il s'agit d'une **avance rapide** de la branche distante : le serveur doit pouvoir simplement déplacer son pointeur vers votre commit. Si quelqu'un a poussé des commits entre-temps, la branche distante contient des commits que vous n'avez pas ; votre push écrasera ce travail, donc Git le refuse (`rejected ... non-fast-forward`).

La solution est d'intégrer d'abord le travail distant :

```bash
git pull --rebase
git push
```

#### 4.4.3 Forcer un envoi : à manier avec précaution

Après une réécriture d'historique (rebase, amend), vos commits ont de nouveaux hashs et le push classique est refusé. Il faut alors forcer.

```bash
git push --force-with-lease       # forcer SEULEMENT si personne n'a poussé entre-temps
# git push --force                # écrase aveuglément le travail des autres
```

- `--force` remplace la branche distante quoi qu'elle contienne. Il peut détruire le travail poussé par d'autres.
- `--force-with-lease` vérifie que la branche distante est **toujours dans l'état que vous connaissez** (celui de votre dernier `fetch`). Si quelqu'un a poussé entre-temps, l'envoi est refusé. C'est la variante à utiliser systématiquement.

Ne forcez que sur **vos propres branches** (par exemple après un rebase de votre branche de fonctionnalité). Ne forcez jamais sur `main` ou toute branche partagée ; configurez la protection de ces branches sur la plateforme.

#### 4.4.4 Autres usages de `push`

| Besoin | Commande |
| --- | --- |
| Pousser toutes les branches locales | `git push --all origin` |
| Pousser les étiquettes | `git push origin --tags` |
| Supprimer une branche distante | `git push origin --delete ma-branche` |
| Pousser vers une branche distante de nom différent | `git push origin locale:distante` |

### 4.5 Forks et *pull requests*

#### 4.5.1 Le problème

Pour contribuer à un projet dont vous n'avez pas les droits d'écriture, il est impossible de pousser directement dessus. Les plateformes résolvent ce problème par deux mécanismes : le *fork* et la *pull request*.

- Un **fork** est une copie personnelle d'un dépôt, hébergée sur votre compte de la plateforme. C'est une notion de plateforme, pas de Git : techniquement, c'est un clone côté serveur.
- Une **pull request** (PR ; *merge request* sur GitLab) est une demande formelle, ouverte depuis une branche, pour que les mainteneurs intègrent vos modifications dans le dépôt d'origine. Elle sert de lieu de discussion, de revue de code et d'exécution des tests automatiques.

#### 4.5.2 Procédure complète

```bash
# 1. Forkez le dépôt via l'interface web, puis clonez VOTRE fork
git clone https://github.com/vous/projet.git
cd projet

# 2. Ajoutez le dépôt d'origine comme remote « upstream »
git remote add upstream https://github.com/proprietaire/projet.git

# 3. Synchronisez régulièrement
git fetch upstream
git switch main
git merge upstream/main          # ou : git rebase upstream/main
git push origin main

# 4. Travaillez dans une branche, poussez-la sur votre fork
git switch -c feature/ma-contribution
# ...modifiez des fichiers...
git add . && git commit -m "Décrit la contribution"
git push -u origin feature/ma-contribution
# 5. Ouvrez la pull request depuis l'interface web
```

Par convention, **`origin`** désigne votre fork et **`upstream`** le dépôt d'origine. Vous récupérez les nouveautés depuis `upstream` et vous poussez vos contributions sur `origin`.

#### 4.5.3 Bonnes pratiques de contribution

- **Ne travaillez pas directement sur `main`** de votre fork : gardez-la comme miroir propre de `upstream/main` et faites chaque contribution dans une branche dédiée.
- Lisez le fichier `CONTRIBUTING.md` du projet (conventions de code, format des messages, tests à lancer).
- Gardez des PR **petites et ciblées**, avec une description claire de ce qui change et pourquoi.
- Pour mettre une PR à jour après une revue, il suffit de pousser de nouveaux commits sur la même branche : la PR se met à jour automatiquement.
- Si l'on vous demande de rebaser, utilisez `git push --force-with-lease` sur votre branche.
- À la fusion, les plateformes proposent plusieurs stratégies : *Create a merge commit*, *Squash and merge*, *Rebase and merge*. Le mainteneur choisit.

#### 4.5.4 Avec GitHub CLI *(ajout)*

```bash
gh repo fork proprietaire/projet --clone   # fork + clone (remote « upstream » configuré)
cd projet
git switch -c feature/ma-contribution
# ...modifiez des fichiers...
git add . && git commit -m "Décrit la contribution"
gh pr create --fill              # crée la PR depuis la branche courante (propose de la pousser)
gh pr checkout 123               # récupère la PR n° 123 en local (pour la relire)
gh pr merge 123 --squash         # fusionne la PR n° 123 (si vous avez les droits)
```

`gh pr create --fill` remplit le titre et la description à partir des messages de commit. `gh pr checkout` est très utile pour tester localement la contribution de quelqu'un d'autre avant de l'approuver.

### 4.6 Suivi des branches distantes

#### 4.6.1 Notion de branche suivie (*upstream*)

Une branche locale peut être **liée** à une branche distante, dite sa branche suivie (*upstream branch*). Ce lien permet à `git pull`, `git push` et `git status` de fonctionner sans arguments, et à Git de vous indiquer l'écart : *ahead* (vous avez des commits à pousser), *behind* (le distant a des commits à récupérer), ou les deux (*diverged*).

```bash
git branch -a                                  # locales + distantes
git branch -vv                                 # branche suivie par chaque branche
git branch --set-upstream-to=origin/main       # définir le suivi
git switch feature/chat                        # crée la branche locale qui suit origin/feature/chat
```

#### 4.6.2 Récupérer une branche distante en local

Lorsque vous exécutez `git switch feature/chat` et qu'il n'existe aucune branche locale de ce nom mais une unique branche distante `origin/feature/chat`, Git crée automatiquement la branche locale **avec le suivi configuré**. La forme explicite est :

```bash
git switch -c feature/chat --track origin/feature/chat
```

Pour lire la colonne d'écart dans `git branch -vv` : `[origin/main: ahead 2, behind 1]` signifie que vous avez deux commits à pousser et que le distant en a un nouveau à récupérer.

### 4.7 Exemple de workflow

```bash
git remote add origin https://github.com/utilisateur/monprojet.git
git push -u origin main                 # premier envoi
git pull --rebase                       # plus tard : récupérer les nouveautés
git switch -c feature/chat
git push -u origin feature/chat         # publier une nouvelle branche
```

Ce scénario correspond à un début de projet : on relie le dépôt local à un dépôt vide créé sur la plateforme, on publie `main` en mémorisant le suivi, on récupère ensuite le travail des autres avec un rebase pour garder un historique linéaire, puis on publie une nouvelle branche de travail.

#### Tableau récapitulatif des commandes de synchronisation

| Besoin | Commande | Modifie mon travail local ? |
| --- | --- | --- |
| Voir ce qui a changé sur le serveur | `git fetch` | Non (seulement les branches de suivi) |
| Intégrer ces changements | `git merge origin/main` ou `git rebase origin/main` | Oui |
| Faire les deux d'un coup | `git pull` | Oui |
| Publier mes commits | `git push` | Non (modifie le distant) |

### 4.8 Pièges fréquents

- **Répondre à un refus *non-fast-forward* par `--force`.** Le refus signale que le distant contient des commits que vous n'avez pas ; intégrez-les d'abord (`git pull --rebase`), puis poussez.
- **Confondre `main` et `origin/main`.** La seconde est une copie locale en lecture seule de l'état du serveur ; elle ne se met à jour que lors d'un `fetch`, d'un `pull` ou d'un `push`.
- **Lancer `git pull` sans savoir ce qu'il fait.** C'est un `fetch` suivi d'une fusion ou d'un rebase ; fixez votre préférence (`pull.rebase`, `pull.ff only`) pour éviter les commits de fusion parasites.
- **Utiliser `--force` au lieu de `--force-with-lease`**, ou forcer sur une branche partagée : vous risquez d'écraser le travail d'autrui.
- **Travailler directement sur la `main` de son fork.** Gardez-la comme miroir de `upstream/main` et faites chaque contribution dans une branche dédiée.
- **Placer un jeton d'accès dans l'URL d'un remote.** Il serait stocké en clair dans `.git/config`.
- **Croire que supprimer une branche locale supprime la distante** (et inversement) : utilisez `git push origin --delete <branche>` et `git fetch --prune`.
- **Oublier le suivi (`-u`)** : sans branche suivie, `git pull` et `git push` sans argument échouent ; `push.autoSetupRemote true` évite ce piège.

### Synthèse du chapitre 4

Un **remote** est un raccourci nommé vers un dépôt distant (`origin` par convention). `git fetch` télécharge sans rien modifier de votre travail et met à jour les branches de suivi distantes (`origin/main`) ; `git pull` ajoute l'intégration (fusion ou rebase) ; `git push` publie vos commits, à condition qu'il s'agisse d'une avance rapide du distant. Après une réécriture d'historique de **votre** branche, on force avec `--force-with-lease`, jamais avec `--force`. Pour contribuer à un projet ouvert, on **forke**, on travaille dans une branche, on pousse sur son fork (`origin`), on se synchronise avec `upstream`, puis on ouvre une **pull request**.

---

## 5. Annuler des modifications et gérer l'historique

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez choisir le bon outil d'annulation selon que le changement est validé ou non, poussé ou non : `diff`, `restore`, `commit --amend`, `revert`, `reset` (trois modes), `stash` et `clean` ; lire un diff ; et retrouver votre travail après une erreur.

Savoir revenir en arrière sans panique est ce qui distingue un utilisateur confiant d'un utilisateur craintif. Git offre plusieurs outils d'annulation, chacun adapté à une situation précise. Ce chapitre apprend à identifier la situation, puis à choisir l'outil.

> **Règle d'or** : avant de défaire quelque chose, demandez-vous *« ce commit est-il déjà poussé ? »*.
>
> - **Non poussé** : vous pouvez réécrire l'historique (`reset`, `amend`, `rebase`).
> - **Déjà poussé ou partagé** : utilisez `git revert` (nouveau commit inverse).

La raison est simple : réécrire un historique que d'autres ont déjà récupéré crée deux versions concurrentes de la réalité et oblige chacun à réconcilier les deux. À l'inverse, un historique local n'intéresse que vous.

### 5.1 Voir les différences (`git diff`)

#### 5.1.1 Que compare `git diff` ?

Selon les arguments, `git diff` compare deux des trois zones (voir 1.4) ou deux commits :

```bash
git diff                    # modifications NON indexées (travail vs index)
git diff --staged           # modifications indexées (index vs dernier commit)
git diff HEAD               # tout depuis le dernier commit
git diff main..feature      # entre deux branches
git diff abc123 def456      # entre deux commits
git diff --stat             # résumé (fichiers et nombre de lignes)
git diff --word-diff        # différences mot à mot
```

| Commande | Compare | Question résolue |
| --- | --- | --- |
| `git diff` | Répertoire de travail et index | Qu'ai-je modifié et pas encore préparé ? |
| `git diff --staged` (ou `--cached`) | Index et dernier commit | Que contiendra mon prochain commit ? |
| `git diff HEAD` | Répertoire de travail et dernier commit | Qu'ai-je changé au total depuis le dernier commit ? |
| `git diff A B` | Deux commits, deux branches ou deux étiquettes | Qu'est-ce qui diffère entre ces deux versions ? |

Un piège fréquent : après `git add`, `git diff` ne montre plus rien pour le fichier indexé, car il n'y a plus de différence entre le répertoire de travail et l'index. C'est `git diff --staged` qu'il faut utiliser.

#### 5.1.2 Lire un diff

```text
diff --git a/app.js b/app.js
index 3f2a1b4..9c8d7e6 100644
--- a/app.js
+++ b/app.js
@@ -10,7 +10,7 @@ function calcul() {
   const a = 1;
-  const total = a + 1;
+  const total = a + 2;
   return total;
 }
```

- Les lignes `---` et `+++` désignent l'ancienne (`a/`) et la nouvelle (`b/`) version du fichier.
- La ligne `@@ -10,7 +10,7 @@` décrit un **morceau** (*hunk*) : à partir de la ligne 10, sept lignes dans l'ancienne version, sept dans la nouvelle.
- Les lignes préfixées de `-` sont **supprimées**, celles préfixées de `+` sont **ajoutées**, les autres sont du contexte inchangé.

#### 5.1.3 Options complémentaires

| Option | Effet |
| --- | --- |
| `--stat` | Fichiers modifiés et nombre de lignes ajoutées ou supprimées |
| `--name-only` | Noms des fichiers modifiés seulement |
| `--word-diff` | Met en évidence les mots modifiés, pratique pour la prose |
| `-w` | Ignore les différences d'espaces |
| `-- chemin` | Limite la comparaison à un fichier ou dossier |

### 5.2 Désindexer un fichier *(à jour)*

Vous avez exécuté `git add` sur un fichier par erreur ? Retirez-le de l'index sans toucher à son contenu :

```bash
git add index.html
git restore --staged index.html       # moderne (Git 2.23+)
# git reset HEAD index.html           # ancienne syntaxe, équivalente
```

Le fichier reste modifié dans le répertoire de travail, mais n'est plus indexé. Aucune modification n'est perdue : l'opération agit uniquement sur l'index. On peut l'appliquer à tous les fichiers avec `git restore --staged .`.

### 5.3 Annuler des modifications locales *(à jour)*

#### 5.3.1 Restaurer des fichiers

`git restore` remplace le contenu d'un fichier du répertoire de travail par sa version enregistrée dans l'index (ou, par défaut, par la version du dernier commit si le fichier n'est pas indexé différemment).

```bash
git restore index.html                # moderne
# git checkout -- index.html          # ancienne syntaxe
git restore .                         # tous les fichiers
git restore -p fichier                # choisir morceau par morceau
git restore --source=HEAD~2 fichier   # restaurer depuis un ancien commit
```

- `git restore <fichier>` : abandonne vos modifications non indexées sur ce fichier.
- `git restore -p` : mode interactif, pour n'abandonner que certains morceaux.
- `--source=<commit>` : va chercher la version du fichier dans un commit ou une étiquette donnée. Utile pour récupérer un fichier tel qu'il était, sans quitter la branche courante.
- `--staged` agit sur l'index, `--worktree` sur le répertoire de travail (par défaut), et les deux ensemble pour tout remettre à l'état du commit : `git restore --staged --worktree <fichier>`.

> **Irréversible** : les modifications non validées sont **définitivement perdues**. Git ne les a jamais enregistrées, il ne peut donc pas les restaurer. Avant d'exécuter `git restore .`, vérifiez avec `git diff` ou mettez de côté avec `git stash` (voir 5.7).

### 5.4 Corriger le dernier commit

```bash
git add oubli.txt
git commit --amend --no-edit          # ajoute le fichier oublié au dernier commit
git commit --amend -m "Nouveau message"
```

`git commit --amend` **remplace** le dernier commit par un nouveau commit : même parent, nouveau contenu (index actuel) et/ou nouveau message. Cas d'usage :

- corriger une faute dans le message ;
- ajouter un fichier oublié ;
- retirer un fichier ajouté par erreur (`git restore --staged <fichier>` puis `--amend`) ;
- changer l'auteur après une mauvaise configuration : `git commit --amend --reset-author`.

Le commit d'origine n'est pas modifié : il devient orphelin (retrouvable un temps par `git reflog`) et le nouveau commit porte **un hash différent**. D'où la règle : n'amendez que des commits qui n'ont pas été poussés.

### 5.5 Annuler un commit en sécurité (`git revert`)

#### 5.5.1 Principe

`git revert` crée un **nouveau commit** qui applique l'inverse des modifications d'un commit précédent. L'historique n'est pas réécrit : le commit fautif et son annulation y figurent tous deux. L'opération est donc **sans danger pour l'historique partagé**.

```bash
git revert <hash>
git revert HEAD --no-edit             # annule le dernier commit sans ouvrir l'éditeur
git revert -m 1 <hash-de-fusion>      # annuler un commit de FUSION (garde le parent 1)
```

#### 5.5.2 Détails

- Vous pouvez annuler un commit **ancien** : Git applique le diff inverse au code actuel. Si le code a depuis changé au même endroit, un conflit peut survenir, à résoudre comme une fusion (puis `git revert --continue`).
- `--no-commit` (`-n`) applique l'inverse dans l'index sans créer de commit, pour regrouper plusieurs annulations en un seul commit.
- On peut annuler plusieurs commits : `git revert HEAD~3..HEAD`.
- **Annuler un commit de fusion** exige de préciser avec `-m` quel parent est la « ligne principale » à conserver. `-m 1` garde le premier parent, c'est-à-dire la branche dans laquelle on a fusionné (généralement `main`), et annule donc les modifications apportées par la branche fusionnée.
- On peut annuler une annulation (`git revert <hash-du-revert>`) pour réintégrer des modifications. Attention : après avoir annulé une fusion, une nouvelle fusion de la même branche n'intègre pas à nouveau ses anciens commits ; il faut d'abord annuler le *revert*.

### 5.6 Revenir en arrière (`git reset`)

#### 5.6.1 Principe

`git reset` **déplace la branche courante** vers un autre commit (en général un ancien), ce qui revient à « oublier » les commits plus récents. Selon le mode, il agit en plus sur l'index et le répertoire de travail.

| Mode | HEAD | Index | Répertoire de travail |
| --- | --- | --- | --- |
| `--soft` | déplacé | conservé | conservé |
| `--mixed` *(défaut)* | déplacé | réinitialisé | conservé |
| `--hard` | déplacé | réinitialisé | **écrasé** |

```bash
git reset --soft HEAD~1     # annule le commit, garde tout indexé
git reset HEAD~1            # annule le commit, garde les changements non indexés
git reset --hard HEAD~1     # annule le commit ET supprime les changements
git reset --hard origin/main  # aligne sur le distant (perd le travail local)
```

#### 5.6.2 Comprendre les trois modes

Partons de l'historique `A - B - C` avec `HEAD` sur C, et exécutons un reset vers B (`HEAD~1`) :

- **`--soft`** : la branche revient sur B. Les modifications du commit C restent dans l'index, prêtes à être re-validées. C'est l'outil pour **refaire** un commit (ou fusionner les derniers en un seul, voir 6.5).
- **`--mixed`** : la branche revient sur B et l'index est réinitialisé. Les modifications de C sont toujours là, mais **non indexées**. C'est l'outil pour **reprendre à zéro la préparation** d'un commit.
- **`--hard`** : la branche revient sur B, l'index et les fichiers aussi. Les modifications de C et toute modification non validée **disparaissent du répertoire de travail**. Le commit C reste retrouvable par `git reflog`, mais les modifications non validées sont perdues.

#### 5.6.3 Autres formes

- `git reset <fichier>` (ou `git reset -- <fichier>`) désindexe un fichier : c'est l'ancienne écriture de `git restore --staged`.
- Git mémorise la position de `HEAD` avant l'opération dans `ORIG_HEAD`. Pour annuler un reset : `git reset --hard ORIG_HEAD` (ou utilisez `git reflog`).

> **Attention** : n'utilisez pas `--hard` sur une branche partagée. En cas d'erreur, `git reflog` peut vous sauver (voir 9.3).

#### 5.6.4 `reset` ou `revert` ?

|  | `git reset` | `git revert` |
| --- | --- | --- |
| Effet | Supprime des commits de l'historique | Ajoute un commit inverse |
| Historique partagé | Dangereux | Sûr |
| Usage | Travail local non poussé | Annuler un commit publié |

### 5.7 Mettre de côté (`git stash`)

#### 5.7.1 Principe

Le *stash* est une pile (« remise ») où Git range temporairement vos modifications non validées pour vous laisser un répertoire de travail propre. Cas typique : vous travaillez sur une fonctionnalité, un bug urgent survient, vous devez changer de branche mais ne voulez pas valider un travail inachevé.

```bash
git stash                          # met de côté (fichiers suivis)
git stash push -m "travail en cours"   # avec un message
git stash -u                       # inclut aussi les fichiers non suivis
git stash list                     # liste
git stash show -p stash@{0}        # voir le contenu
git stash apply                    # réapplique (garde le stash)
git stash pop                      # réapplique ET supprime
git stash branch nouvelle-branche  # crée une branche à partir du stash
git stash drop stash@{0}           # supprime un stash
git stash clear                    # supprime tous les stashes
```

#### 5.7.2 Détail des commandes

- `git stash` (ou `git stash push`) enregistre les modifications **indexées et non indexées des fichiers suivis**, puis remet le répertoire de travail dans l'état du dernier commit. Par défaut, les fichiers **non suivis** restent en place.
- `-u` (`--include-untracked`) inclut aussi les fichiers non suivis ; `-a` (`--all`) inclut en plus les fichiers ignorés.
- `-m "message"` décrit l'entrée, ce qui est très utile dès qu'il y en a plusieurs.
- `git stash list` affiche les entrées sous la forme `stash@{0}` (la plus récente), `stash@{1}`, etc.
- `git stash apply` réapplique sans supprimer l'entrée ; `git stash pop` réapplique **puis supprime** l'entrée. En cas de conflit lors du `pop`, l'entrée est conservée.
- `git stash branch <nom>` crée une branche à partir du commit où le stash a été fait, y applique le stash et le supprime : très pratique si le code a trop évolué pour une application directe.
- On peut limiter la remise à certains fichiers : `git stash push -- chemin/fichier`.
- `--keep-index` laisse les changements indexés en place, utile pour tester ce qui va être validé.

> **Astuce** : le stash n'est pas fait pour conserver du travail à long terme. Pour quelque chose qui doit durer, créez une branche et un commit (même provisoire, vous pourrez le réécrire avant de pousser).

### 5.8 Nettoyer les fichiers non suivis (`git clean`)

`git clean` supprime les fichiers que Git ne suit pas : résidus de compilation, fichiers temporaires, etc.

```bash
git clean -n          # simulation : montre ce qui serait supprimé
git clean -f          # supprime les fichiers non suivis
git clean -fd         # + les dossiers non suivis
git clean -fdx        # + les fichiers ignorés (très destructeur)
git clean -i          # mode interactif
```

| Option | Rôle |
| --- | --- |
| `-n` (`--dry-run`) | Montre ce qui serait supprimé, sans rien supprimer |
| `-f` (`--force`) | Nécessaire pour supprimer réellement (sécurité) |
| `-d` | Inclut les dossiers non suivis |
| `-x` | Inclut les fichiers ignorés par `.gitignore` |
| `-i` | Interactif |

> Toujours faire un `-n` d'abord. Les fichiers supprimés **ne passent pas par la corbeille** et ne sont pas récupérables par Git, puisqu'il ne les a jamais enregistrés.

### 5.9 Récapitulatif : « Je veux annuler… »

| Situation | Solution |
| --- | --- |
| Une modification non indexée | `git restore <fichier>` |
| Un fichier que j'ai indexé | `git restore --staged <fichier>` |
| Le dernier commit (non poussé), en gardant le travail | `git reset --soft HEAD~1` |
| Le dernier commit, avec correction du message | `git commit --amend` |
| Un commit déjà poussé | `git revert <hash>` |
| Tout le travail local non validé | `git restore .` / `git stash` |
| Un `reset --hard` malheureux | `git reflog` puis `git reset --hard <hash>` |

#### Arbre de décision

1. Le changement est-il **validé** (commité) ?
   - Non : `restore` (fichiers), `restore --staged` (index), `stash` (mettre de côté), `clean` (fichiers non suivis).
   - Oui : poursuivre.
2. Le commit est-il **poussé ou partagé** ?
   - Oui : `revert`.
   - Non : `commit --amend` (dernier commit), `reset` (plusieurs commits), `rebase -i` (réorganisation fine, voir chapitre 6).

### 5.10 Exemple de workflow

```bash
git diff                       # inspecter
git add .
git commit -m "Travail en cours"
git reset --soft HEAD~1        # oups : annuler le commit en gardant les changements
git stash                      # changer de contexte
git switch -c autre-branche   # créer une autre branche
# ... travailler, committer ...
git switch -                  # revenir à la branche précédente
git stash pop                  # reprendre
```

Commentaire : le commit « Travail en cours » est annulé avec `--soft`, ses modifications restant indexées. Le `stash` les met ensuite de côté pour permettre de changer de contexte, puis `stash pop` les récupère à notre retour. Aucun travail n'est perdu à aucun moment.

### 5.11 Pièges fréquents

- **Exécuter `git restore .`, `git reset --hard` ou `git clean -fd` sans vérifier.** Les modifications non validées sont définitivement perdues : Git ne les a jamais enregistrées. Faites `git diff` ou `git stash` avant, et `git clean -n` pour simuler.
- **Utiliser `reset` sur un historique partagé.** Il supprime des commits que d'autres ont déjà récupérés ; utilisez `git revert`.
- **Confondre `restore` et `restore --staged`.** Le premier abandonne les modifications du répertoire de travail, le second retire seulement le fichier de l'index.
- **Constater un `git diff` vide après `git add`.** Les modifications sont dans l'index : utilisez `git diff --staged`.
- **Annuler un commit de fusion sans `-m`.** `git revert` exige de préciser le parent à conserver (`-m 1` garde généralement la branche principale).
- **Oublier `-u` avec `git stash`.** Par défaut, les fichiers non suivis ne sont pas mis de côté.
- **Utiliser le stash comme stockage durable.** Pour du travail à conserver, créez une branche et un commit.
- **Paniquer après une fausse manipulation.** Un commit « perdu » se retrouve presque toujours avec `git reflog`.

### Synthèse du chapitre 5

Le bon outil dépend de deux questions : le changement est-il **validé** ? Est-il **poussé** ? Pour du travail non validé : `git restore` (fichiers), `git restore --staged` (index), `git stash` (mise de côté) et `git clean` (fichiers non suivis). Pour un commit local non poussé : `git commit --amend` (dernier commit) ou `git reset` (`--soft` garde tout indexé, `--mixed` garde les changements non indexés, `--hard` supprime tout). Pour un commit **déjà poussé** : `git revert`, qui ajoute un commit inverse sans réécrire l'historique. Dans tous les cas, `git reflog` reste le filet de sécurité pour ce qui a été commité.

---

# Partie II — Git avancé

## 6. Branches et fusions avancées

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez résoudre des conflits de fusion ; rebaser une branche et savoir quand ne pas le faire ; réécrire l'historique avec `rebase -i` et `--fixup` ; reporter un commit avec `cherry-pick` ; écraser des commits (*squash*) ; et travailler sur plusieurs branches en parallèle avec `git worktree`.

Ce chapitre approfondit l'intégration du travail entre branches : résolution des conflits, rebase simple et interactif, report sélectif de commits, regroupement de commits et utilisation de plusieurs répertoires de travail. Ces techniques permettent de produire des historiques lisibles et de gérer des situations réelles d'équipe.

### 6.1 Résoudre les conflits de fusion

#### 6.1.1 Qu'est-ce qu'un conflit ?

Un **conflit** survient quand Git ne peut pas combiner automatiquement des modifications : typiquement, les **mêmes lignes** d'un même fichier ont été modifiées différemment dans deux branches, ou un fichier a été modifié d'un côté et supprimé de l'autre. Git sait fusionner automatiquement tout ce qui touche des zones différentes ; il ne s'arrête que lorsqu'un arbitrage humain est nécessaire.

Un conflit n'est ni une erreur ni un signe de mauvaise pratique : c'est une situation normale du travail collaboratif. La fusion est simplement **suspendue** jusqu'à ce que vous la finalisiez ou l'abandonniez.

```bash
git switch main
git merge feature
# CONFLICT (content): Merge conflict in fichier.txt
```

#### 6.1.2 Les marqueurs de conflit

Git écrit les deux versions dans le fichier, délimitées par des marqueurs :

```text
<<<<<<< HEAD
Changement venant de main
=======
Changement venant de feature
>>>>>>> feature
```

- Entre `<<<<<<< HEAD` et `=======` : la version de la branche **courante** (celle qui reçoit la fusion).
- Entre `=======` et `>>>>>>> feature` : la version de la branche **fusionnée**.

Avec le réglage `merge.conflictStyle zdiff3` (voir plus bas), un troisième bloc introduit par `|||||||` montre la version de l'**ancêtre commun**, ce qui aide beaucoup à comprendre qui a changé quoi.

#### 6.1.3 Étapes de résolution

1. **Ouvrez** le fichier et choisissez ou combinez le bon contenu ; **supprimez les marqueurs** `<<<<<<<`, `=======`, `>>>>>>>`. Le résultat peut être l'une des deux versions, l'autre, ou un mélange des deux.
2. **Marquez** le fichier comme résolu : `git add fichier.txt`.
3. **Finalisez** : `git commit` (ou `git merge --continue`).

```bash
git status                       # liste les fichiers en conflit
git merge --abort                # abandonner et revenir à l'état d'avant
git checkout --ours fichier      # garder VOTRE version (branche courante)
git checkout --theirs fichier    # garder la version de l'AUTRE branche
git mergetool                    # ouvrir un outil graphique
```

- `git status` range les fichiers en conflit sous « *Unmerged paths* » (code `UU` en mode court).
- `git checkout --ours` (ou `--theirs`) remplace entièrement le fichier par la version de l'un des côtés. Pratique pour les fichiers que l'on ne souhaite pas fusionner à la main. Il faut ensuite faire `git add`.
- Une fois les marqueurs supprimés, **relancez les tests** avant de valider : un fichier peut ne plus avoir de marqueurs et pourtant être incohérent.
- `git diff` pendant un conflit affiche un diff combiné qui aide à comprendre l'état courant.

#### 6.1.4 Cas particuliers

| Situation | Message ou état | Résolution |
| --- | --- | --- |
| Modifié d'un côté, supprimé de l'autre | *deleted by us/them* | Choisir : `git add fichier` pour garder, `git rm fichier` pour supprimer |
| Fichier binaire en conflit | Pas de marqueurs possibles | Choisir une version avec `--ours` ou `--theirs` |
| Conflit de renommage | Chemins multiples | Arbitrer, puis `git add` / `git rm` |

#### 6.1.5 Outils et automatisation

> **Astuce** : **`git rerere`** (*reuse recorded resolution*) mémorise vos résolutions et les réapplique automatiquement si le même conflit se reproduit (par exemple en refaisant un rebase). Activation : `git config --global rerere.enabled true`.
>
> **Astuce** : outils visuels : VS Code, Meld, KDiff3, GitKraken. Réglez `git config --global merge.conflictStyle zdiff3` pour afficher aussi l'ancêtre commun.

Pour réduire les conflits en amont : fusionnez ou rebasez souvent depuis `main`, faites des branches courtes, ne reformatez pas de gros fichiers dans une branche de fonctionnalité, et communiquez avec les collègues qui touchent aux mêmes fichiers.

### 6.2 Rebaser (`git rebase`)

#### 6.2.1 Principe

Le **rebase** rejoue vos commits **par-dessus** une autre base, pour obtenir un historique **linéaire**. Concrètement, Git identifie les commits propres à votre branche, les met de côté, replace la branche sur la nouvelle base, puis réapplique un à un vos commits.

```bash
git switch feature
git rebase main
```

```text
Avant :
main:     A───B───C
               \
feature:        D───E

Après `git rebase main` (sur feature) :
main:     A───B───C
                   \
feature:            D'──E'      (D' et E' sont de NOUVEAUX commits)
```

Point essentiel : D' et E' portent le **même contenu** que D et E, mais ce sont de **nouveaux commits avec de nouveaux hashs**, puisque leur parent a changé. Le rebase **réécrit** l'historique.

#### 6.2.2 Comparaison `merge` / `rebase`

|  | `merge` | `rebase` |
| --- | --- | --- |
| Historique | Fidèle (garde les branches) | Linéaire et propre |
| Commits | Conservés tels quels | **Réécrits** (nouveaux hashs) |
| Risque | Faible | Élevé sur du code partagé |

Les deux méthodes aboutissent au même contenu final ; seule la forme de l'historique diffère. Le merge décrit **ce qui s'est réellement passé**, le rebase raconte **une histoire plus lisible**.

> **Règle d'or du rebase : ne rebasez jamais des commits déjà poussés et utilisés par d'autres.** Ils changeraient de hash ; vos collègues se retrouveraient avec des commits « fantômes » et des fusions parasites.

Usage typique et sûr : avant d'ouvrir une pull request, rebasez **votre** branche de fonctionnalité sur la dernière version de `main`, pour qu'elle s'y intègre en avance rapide.

#### 6.2.3 Conflits pendant un rebase

Le rebase rejouant les commits un par un, un conflit peut survenir à chaque étape. Git s'arrête, vous résolvez, puis reprenez :

```bash
# résolvez, puis :
git add fichier
git rebase --continue
git rebase --skip      # ignorer ce commit
git rebase --abort     # tout annuler
```

- `--continue` reprend après résolution (n'utilisez pas `git commit` ici).
- `--skip` abandonne le commit en cours de rejeu (son contenu est perdu dans la nouvelle branche).
- `--abort` restaure l'état d'avant le rebase : c'est le filet de sécurité.

> **Attention** : pendant un rebase, les notions **ours** et **theirs** sont **inversées** par rapport à un merge. Git reconstruit la branche sur la base `main` : *ours* désigne la branche sur laquelle vous rebasez (la base), *theirs* désigne vos propres commits en cours de rejeu.

#### 6.2.4 Pousser après un rebase

Après un rebase d'une branche déjà poussée (la vôtre uniquement), le push classique est refusé car l'historique a divergé :

```bash
git push --force-with-lease
```

#### 6.2.5 Variante : `--onto`

`git rebase --onto <nouvelle-base> <ancienne-base> <branche>` déplace une série de commits vers une autre base. Exemple : une branche `b` créée depuis `a` doit en réalité partir de `main` : `git rebase --onto main a b`.

### 6.3 Rebase interactif (`git rebase -i`)

#### 6.3.1 Principe

Le rebase interactif permet de **réordonner, reformuler, fusionner, supprimer** des commits avant de les partager. C'est l'outil pour « nettoyer » une branche.

```bash
git rebase -i HEAD~3
```

Git ouvre l'éditeur avec la liste des trois derniers commits, **du plus ancien (en haut) au plus récent (en bas)** : l'inverse de `git log`.

```text
pick 1a2b3c1 Premier commit
pick 4d5e6f2 Deuxième commit
pick 7a8b9c3 Troisième commit
```

Vous remplacez le mot en début de ligne par la commande voulue, vous réordonnez les lignes si besoin, puis vous enregistrez et fermez l'éditeur.

| Commande | Effet |
| --- | --- |
| `pick` | Garder le commit tel quel |
| `reword` | Garder, mais modifier le message |
| `edit` | S'arrêter pour modifier le commit |
| `squash` | Fusionner avec le précédent (combine les messages) |
| `fixup` | Fusionner avec le précédent (ignore ce message) |
| `drop` | Supprimer le commit |

Autres commandes : `exec <cmd>` exécute une commande shell entre deux commits (par exemple les tests), `break` marque un arrêt, et supprimer une ligne supprime le commit. Les commandes ont des abréviations (`p`, `r`, `e`, `s`, `f`, `d`).

#### 6.3.2 Déroulement

- Avec `reword`, Git rouvre l'éditeur au moment voulu pour que vous écriviez le nouveau message.
- Avec `edit`, Git s'arrête à ce commit : modifiez les fichiers, `git add`, `git commit --amend`, puis `git rebase --continue`. Cela permet de scinder un commit en deux ou de corriger son contenu.
- Avec `squash` ou `fixup`, le commit est fusionné dans la ligne **qui le prède** : il ne peut donc pas figurer en première position.
- Si vous videz entièrement l'éditeur ou que vous aboutissez à un résultat inattendu, `git rebase --abort` annule tout.

#### 6.3.3 Correction automatique avec `--fixup` *(ajout)*

```bash
git commit --fixup <hash>         # crée un commit « fixup! » rattaché au commit visé
git rebase -i --autosquash main   # les réordonne et les fusionne automatiquement
```

Le flux est très efficace : lorsque vous découvrez, après coup, qu'un ancien commit de votre branche doit être corrigé, vous créez un commit `--fixup` pointant vers lui. Au moment du nettoyage, `--autosquash` place chaque correctif juste sous son commit cible et préremplit les commandes `fixup`. Le réglage `git config --global rebase.autoSquash true` active ce comportement par défaut.

### 6.4 Picorer un commit (`git cherry-pick`)

#### 6.4.1 Principe

`git cherry-pick` applique **un commit précis** d'une branche sur la branche courante, en créant un nouveau commit au contenu équivalent (avec un hash différent, puisque le parent diffère).

```bash
git switch main
git cherry-pick 9c8a7b6
git cherry-pick A^..B             # une plage de commits
git cherry-pick -x <hash>         # ajoute la référence du commit d'origine au message
git cherry-pick --abort
```

- `A^..B` désigne la plage de A (inclus) à B (inclus).
- `-x` ajoute au message la mention « (cherry picked from commit ...) » : utile pour la traçabilité lors d'un report sur une branche de maintenance.
- `-n` (`--no-commit`) applique les modifications sans créer de commit.
- En cas de conflit : résolvez, `git add`, puis `git cherry-pick --continue` ; `--abort` annule.
- Pour picorer un commit de fusion, il faut préciser le parent avec `-m 1`.

#### 6.4.2 Cas d'usage

Le cas typique est de reporter un **correctif urgent** sur une branche de maintenance (par exemple faire passer sur `release/1.2` un bug corrigé sur `main`). À utiliser avec parcimonie : le même changement existera sous deux hashs différents, ce qui peut produire des conflits lors d'une future fusion des deux branches. Si vous devez picorer beaucoup de commits, une fusion ou un rebase est probablement plus adapté.

### 6.5 Écraser des commits (*squash*)

#### 6.5.1 Objectif

Regrouper plusieurs commits (« wip », « fix typo », « encore un essai ») en un seul commit cohérent avant de fusionner, pour que l'historique de `main` raconte des changements logiques plutôt que le brouillon du développeur.

```bash
# Méthode 1 : rebase interactif (squash / fixup)
git rebase -i HEAD~3

# Méthode 2 : reset doux + nouveau commit
git reset --soft HEAD~3
git commit -m "Fonctionnalité complète"

# Méthode 3 : à la fusion
git merge --squash feature && git commit
```

| Méthode | Avantage | Limite |
| --- | --- | --- |
| Rebase interactif | Contrôle total : on choisit quels commits regrouper et lesquels garder | Un peu plus long |
| `reset --soft` + commit | Très simple pour condenser les N derniers commits | On repart d'un message neuf ; tout est fusionné |
| `merge --squash` | Pas de réécriture de la branche source | La branche source n'est pas marquée comme fusionnée ; son suppression exige `-D` |

Les plateformes (GitHub, GitLab) proposent aussi **« Squash and merge »** à la fusion d'une PR : tous les commits de la PR sont condensés en un seul sur `main`.

> **Rappel** : l'écrasement réécrit l'historique ; ne le faites que sur des commits non partagés ou sur votre propre branche de PR (suivi d'un `--force-with-lease`).

### 6.6 Plusieurs répertoires de travail (`git worktree`) *(ajout)*

#### 6.6.1 Problème et solution

Un dépôt n'a normalement qu'un seul répertoire de travail : pour traiter un bug urgent pendant que vous développez une fonctionnalité, il faut valider, mettre de côté ou cloner à nouveau. `git worktree` permet d'avoir **plusieurs branches extraites en même temps, dans des dossiers différents**, qui partagent le même dossier `.git` (mêmes objets, mêmes références) : pas de nouveau clone, pas de duplication de l'historique, pas de `stash`.

```bash
git worktree add -b hotfix/1.2 ../correctif-urgent    # nouvelle branche dans un nouveau dossier lié au dépôt
git worktree list
git worktree remove ../correctif-urgent
```

- `git worktree add <chemin> <branche>` extrait une branche existante dans un nouveau dossier ; avec `-b <nom>`, la branche est créée au passage.
- Une même branche **ne peut pas être extraite dans deux répertoires de travail à la fois** (Git l'interdit pour éviter des incohérences).
- `git worktree remove` supprime le dossier et son rattachement ; `git worktree prune` nettoie les rattachements dont le dossier a disparu.
- Cas d'usage : correctif urgent en parallèle, relecture d'une PR sans bouger de votre travail en cours, lancement de tests longs sur une autre branche pendant que vous continuez à coder.

### 6.7 Exemple de workflow

```bash
# Option A : fusionner feature dans main
git switch main && git merge feature

# Option B : rebaser feature sur main à jour, puis fusionner (avance rapide)
git switch feature && git rebase main
git switch main && git merge feature

# Reporter un correctif sur une autre branche
git switch hotfix && git cherry-pick abc1234

# Écraser les 2 derniers commits (ouvre l'éditeur)
git rebase -i HEAD~2
```

L'option A produit un historique fidèle, avec un commit de fusion. L'option B produit un historique linéaire : le rebase place les commits de `feature` au bout de `main`, de sorte que la fusion finale est une simple avance rapide. Les deux conduisent au même contenu ; le choix dépend de la politique de l'équipe (voir chapitre 8).

### 6.8 Pièges fréquents

- **Laisser des marqueurs de conflit dans un fichier** (`<<<<<<<`, `=======`, `>>>>>>>`) : supprimez-les, puis relancez les tests avant de valider.
- **Rebaser des commits déjà partagés.** Ils changent de hash et vos collègues se retrouvent avec des commits dupliqués ; ne rebasez que votre propre branche non partagée.
- **Inverser *ours* et *theirs* pendant un rebase.** Dans un rebase, *ours* est la branche sur laquelle vous rebasez et *theirs* vos propres commits rejoués ; c'est l'inverse d'une fusion.
- **Utiliser `git commit` au lieu de `git rebase --continue`** après avoir résolu un conflit de rebase.
- **Placer `squash` ou `fixup` sur la première ligne** d'un rebase interactif : ces commandes fusionnent avec la ligne précédente, qui n'existe pas.
- **Picorer massivement (`cherry-pick`).** Un même changement existera sous deux hashs, ce qui produit des conflits lors d'une fusion ultérieure ; préférez fusionner ou rebaser.
- **Oublier de pousser après un rebase** ou pousser avec `--force` au lieu de `--force-with-lease`.
- **Chercher à extraire la même branche dans deux répertoires de travail** : `git worktree` l'interdit.

### Synthèse du chapitre 6

Un **conflit** n'est pas une erreur : c'est un arbitrage humain que Git vous demande ; on le résout en éditant le fichier, en indexant (`git add`) puis en finalisant (`git commit`, `git merge --continue` ou `git rebase --continue`), avec `--abort` comme issue de secours. Le **rebase** rejoue des commits sur une nouvelle base pour obtenir un historique linéaire, au prix d'une réécriture (jamais sur du code partagé). Le **rebase interactif** nettoie une branche (`reword`, `squash`, `fixup`, `drop`, `--autosquash`), `cherry-pick` reporte un commit isolé, et `git worktree` permet de travailler sur plusieurs branches à la fois sans cloner de nouveau.

---

## 7. Fonctionnement interne et configuration

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez décrire le modèle d'objets de Git (blob, tree, commit, tag) ; expliquer les références, `HEAD` et le HEAD détaché ; écrire et partager des hooks ; définir des alias ; configurer Git de façon conditionnelle ; utiliser les sous-modules ; et décrire un comportement par type de fichier avec `.gitattributes`.

Comprendre ce que Git fait réellement sous le capot transforme des commandes d'apparence arbitraire en opérations évidentes. Ce chapitre décrit le modèle d'objets, les références, puis les mécanismes de personnalisation : hooks, alias, configuration conditionnelle, sous-modules et attributs.

### 7.1 Le modèle d'objets de Git

#### 7.1.1 Un système de fichiers adressable par contenu

Git est avant tout un **système de fichiers adressable par contenu** (*content-addressable filesystem*) : une base clé-valeur où la **clé** est le hash du contenu et la **valeur** est le contenu lui-même. Chaque élément est un **objet** identifié par son **hash**, stocké dans `.git/objects`. Les commandes familières (`add`, `commit`, `branch`) sont une interface conviviale construite par-dessus ce mécanisme. On distingue d'ailleurs les commandes **porcelaine** (celles que l'on utilise au quotidien) des commandes **plomberie** (*plumbing*, de bas niveau, comme `hash-object` ou `cat-file`).

Consequences directes :

- deux fichiers de contenu identique ont le même hash et ne sont stockés **qu'une seule fois** ;
- le hash dépend du contenu : changer un octet change le hash ;
- un objet est **immuable** : on ne le modifie jamais, on en crée un nouveau.

#### 7.1.2 Les quatre types d'objets

| Objet | Rôle |
| --- | --- |
| **Blob** | Contenu d'un fichier (sans nom ni métadonnées) |
| **Tree** (arbre) | Un dossier : liste des noms, avec références vers des blobs ou d'autres arbres |
| **Commit** | Instantané : pointe vers un arbre, et contient auteur, date, message et **commits parents** |
| **Tag annoté** | Objet qui pointe vers un autre objet (souvent un commit) avec métadonnées |

```text
commit ──▶ tree (racine) ──▶ blob (README.md)
   │                    └──▶ tree (src/) ──▶ blob (main.py)
   └──▶ commit parent
```

**Blob.** Il ne contient que les octets du fichier. Le **nom** du fichier n'est pas dans le blob : il est dans l'arbre qui le référence. Ainsi, renommer un fichier sans changer son contenu ne crée aucun nouveau blob.

**Tree.** Chaque ligne d'un arbre comporte un **mode** (type de fichier et droits), un **type** (blob ou tree), un **hash** et un **nom**. Les modes courants sont `100644` (fichier normal), `100755` (exécutable), `120000` (lien symbolique) et `040000` (sous-dossier).

**Commit.** Il contient : le hash de l'arbre racine, le ou les hashs des parents, l'auteur et le validateur (nom, e-mail, date), puis le message. Un commit n'est donc **pas** une liste de différences, c'est un pointeur vers un instantané complet (les différences sont calculées à la demande).

**Tag annoté.** Il contient le hash de l'objet étiqueté, son type, le nom de l'étiquette, l'auteur de l'étiquette, la date et un message, éventuellement une signature.

#### 7.1.3 Comment un hash est calculé

Le hash d'un objet est calculé sur un en-tête suivi du contenu. Pour un blob : le mot `blob`, un espace, la taille en octets, un octet nul, puis le contenu. L'empreinte de ce tout est le hash de l'objet. Pour un commit, le contenu inclut le hash de l'arbre, les parents, l'auteur, la date, etc. : l'identité d'un commit dépend donc de **toute son histoire**. C'est pourquoi modifier un ancien commit change les hashs de tous ses descendants, et pourquoi Git détecte toute corruption.

#### 7.1.4 Stockage : objets lâches et fichiers pack

Quand un objet est créé, il est d'abord écrit sous forme d'un **objet lâche** (*loose object*) compressé, dans `.git/objects/xx/yyyy...` (les deux premiers caractères du hash forment le nom du dossier). Au fil du temps, `git gc` (ou la maintenance automatique) regroupe ces objets dans des **fichiers pack** (`.git/objects/pack`) où les objets proches sont stockés sous forme de **deltas** pour gagner beaucoup d'espace. C'est à ce niveau, et seulement à celui-ci, que Git utilise des différences : le modèle logique reste celui des instantanés.

#### 7.1.5 Hash : SHA-1 et SHA-256

Historiquement, Git identifie les objets par **SHA-1** (40 caractères hexadécimaux). Git prend aussi en charge **SHA-256** (64 caractères), créé avec `git init --object-format=sha256`, et prévoit d'en faire le défaut dans **Git 3.0**. Un dépôt SHA-256 n'est pas directement interopérable avec un dépôt SHA-1 ; le support par les plateformes d'hébergement doit aussi être vérifié avant d'adopter ce format.

#### 7.1.6 Explorer les objets

```bash
git cat-file -t <hash>        # type de l'objet
git cat-file -p <hash>        # contenu
git hash-object fichier.txt   # calcule le hash d'un fichier
git ls-tree HEAD              # contenu d'un arbre
```

Pour parcourir le graphe : `git cat-file -p HEAD` affiche le commit courant (arbre, parent, auteur, message) ; `git cat-file -p HEAD^{tree}` affiche son arbre racine ; en copiant le hash d'un blob dans `git cat-file -p`, on obtient le contenu d'un fichier. On peut ainsi parcourir tout le graphe à la main. L'option `git hash-object -w fichier` calcule le hash et **écrit** l'objet dans la base.

### 7.2 Références et `HEAD`

#### 7.2.1 Références

Une **référence** (*ref*) est un nom lisible qui pointe vers un hash. Elles sont stockées sous `.git/refs` (et parfois regroupées dans `.git/packed-refs`) :

- `refs/heads/main` : branches locales ;
- `refs/tags/v1.0` : étiquettes ;
- `refs/remotes/origin/main` : branches de suivi distantes.

Créer une branche revient à écrire un hash dans un petit fichier ; en faire avancer une revient à réécrire ce hash. Cela explique l'extrême légèreté des branches (chapitre 3).

#### 7.2.2 `HEAD`

**`HEAD`** est une **référence symbolique** : elle pointe normalement vers la **branche courante** (et non directement vers un commit). C'est ce qui permet à `git commit` de savoir quelle branche faire avancer.

```bash
cat .git/HEAD
# ref: refs/heads/main

git rev-parse HEAD           # hash du commit courant
```

Autres références spéciales créées par Git lors d'opérations : `ORIG_HEAD` (position avant un reset, merge ou rebase), `MERGE_HEAD` (commit en cours de fusion), `FETCH_HEAD` (résultat du dernier `fetch`).

#### 7.2.3 Raccourcis de révision

| Notation | Signification |
| --- | --- |
| `HEAD~1` ou `HEAD~` | Parent du commit courant |
| `HEAD~3` | Trois générations en arrière (en suivant toujours le premier parent) |
| `HEAD^2` | Second parent (utile pour une fusion) |
| `main@{yesterday}` | Où était `main` hier (via le reflog) |
| `abc123^{tree}` | Arbre associé |

Distinction importante : `~N` remonte de N générations en suivant le **premier** parent ; `^N` choisit le **N-ième parent** du commit (pertinent uniquement pour les commits de fusion, qui en ont deux). `HEAD^` et `HEAD~` sont équivalents pour un commit ordinaire.

#### 7.2.4 *Detached HEAD* (HEAD détaché)

Quand vous extrayez directement un commit ou une étiquette (`git switch --detach v1.0`), `HEAD` ne pointe plus vers une branche : il contient un hash. Vos nouveaux commits n'appartiendront alors à **aucune branche** et deviendront inaccessibles dès que vous changerez de position (ils restent un temps dans le reflog). Pour les conserver : `git switch -c ma-branche`.

Cet état n'est pas une erreur : il est parfait pour inspecter une ancienne version, exécuter des tests ou compiler une version publiée.

### 7.3 Hooks Git

#### 7.3.1 Définition

Les **hooks** sont des scripts exécutés automatiquement à certains moments du cycle de vie de Git. Ils vivent dans `.git/hooks` (le dossier contient des exemples suffixes `.sample`, inactifs). Un hook est un simple exécutable (shell, Python, etc.) dont le nom désigne le moment de déclenchement.

| Hook | Déclenchement | Usage typique |
| --- | --- | --- |
| `pre-commit` | Avant de créer le commit | Lint, formatage, tests rapides |
| `prepare-commit-msg` | Avant l'ouverture de l'éditeur | Pré-remplir le message |
| `commit-msg` | Après la saisie du message | Valider le format du message |
| `pre-push` | Avant l'envoi | Lancer les tests complets |
| `post-merge` | Après une fusion | Réinstaller les dépendances |
| `pre-rebase` | Avant un rebase | Bloquer certains rebases |

D'autres hooks existent (`post-commit`, `post-checkout`, `pre-receive`, `update`, `post-receive`). Les derniers sont des hooks **serveur**, exécutés sur le dépôt distant lors d'un push pour refuser des envois ou déclencher un déploiement. Les hooks `pre-*` peuvent **bloquer** l'opération, les hooks `post-*` sont informatifs.

#### 7.3.2 Utilisation

```sh
#!/bin/sh
# Contenu du fichier .git/hooks/pre-commit
npm run lint || exit 1      # un code de sortie ≠ 0 bloque le commit
```

```bash
chmod +x .git/hooks/pre-commit
```

Regles essentielles : le fichier porte **exactement** le nom du hook (sans extension), il doit être **exécutable**, et un code de sortie non nul interrompt l'opération (pour les hooks bloquants).

> **Attention** : le dossier `.git/hooks` **n'est pas versionné** : les hooks ne sont pas partagés par défaut. Chaque contributeur doit les installer lui-même.

#### 7.3.3 Partager des hooks avec l'équipe *(ajout)*

```bash
git config core.hooksPath .githooks     # utiliser un dossier versionné du dépôt
```

Ou utilisez des outils dédiés : **pre-commit** (Python), **Husky** (JavaScript), **Lefthook**. Les versions récentes de Git (2.54+) permettent aussi de déclarer des hooks directement dans la configuration, et (2.55) de les exécuter en parallèle ; consultez `git help config`.

On peut contourner un hook ponctuellement avec `git commit --no-verify` (à éviter) : cela ne doit rester qu'une issue de secours, car les hooks existent pour garantir des règles communes. Les vérifications essentielles doivent de toute façon être répétées côté serveur (CI), car un hook local est contournable.

### 7.4 Alias Git

Un **alias** est un raccourci personnalisé pour une commande ou une séquence de commandes.

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.sw switch
git config --global alias.cm "commit -m"
git config --global alias.lg "log --graph --oneline --decorate --all"
git config --global alias.undo "reset --soft HEAD~1"
```

Utilisation : `git st`, `git lg`, `git cm "message"`.

Les alias sont stockés dans la section `[alias]` du fichier de configuration. Un alias commençant par `!` exécute une commande shell arbitraire, ce qui permet de composer des scénarios plus complexes, par exemple `git config --global alias.branches "!git branch -vv"`. Les alias ne peuvent pas masquer une commande native de Git. Choisissez des alias que vous retiendrez : un alias « undo » qui exécute `reset --soft` n'est pas anodin pour un collègue qui l'ignore.

### 7.5 Niveaux de configuration

Voir 1.3 : **système** (`/etc/gitconfig`), **global** (`~/.gitconfig`) et **local** (`.git/config`). Il existe aussi la configuration **conditionnelle** :

```ini
# ~/.gitconfig : une autre identité pour les projets professionnels
[includeIf "gitdir:~/travail/"]
    path = ~/.gitconfig-travail
```

Le fichier `~/.gitconfig-travail` est chargé uniquement lorsque le dépôt se trouve sous `~/travail/` (le `/` final est important). Il peut définir `user.name`, `user.email`, une clé de signature, etc. C'est la meilleure solution pour séparer proprement identité personnelle et professionnelle sans y penser à chaque nouveau projet. D'autres conditions existent : `onbranch:`, `hasconfig:remote.*.url:`.

### 7.6 Sous-modules (`git submodule`)

#### 7.6.1 Principe

Un **sous-module** inclut un dépôt Git dans un autre, à un **commit précis**. Le dépôt parent ne stocke pas le contenu du sous-module : il enregistre l'URL (fichier `.gitmodules`) et le **hash du commit** attendu (une entrée spéciale dite *gitlink* dans l'arbre).

```bash
git submodule add https://github.com/user/lib.git libs/lib
git commit -m "Ajoute le sous-module lib"

git clone --recurse-submodules <url>          # cloner avec les sous-modules
git submodule update --init --recursive       # les initialiser après un clone simple
git submodule update --remote                 # les mettre à jour vers la dernière version distante
```

#### 7.6.2 Points de vigilance

- Après un `git pull` dans le dépôt parent, le sous-module n'est pas mis à jour automatiquement : lancez `git submodule update --init --recursive` (ou `git pull --recurse-submodules`).
- Un sous-module est extrait en **HEAD détaché** sur le commit enregistré. Pour y travailler, basculez sur une branche, committez et poussez **d'abord le sous-module**, puis commitez dans le parent la nouvelle référence.
- Oublier de pousser le sous-module avant le parent casse le clone des collègues, qui ne trouveront pas le commit référencé.

> Les sous-modules ajoutent de la complexité. Pour de simples dépendances, préférez un gestionnaire de paquets (npm, pip, Cargo…). Alternative : **`git subtree`**, qui intègre le contenu et l'historique d'un autre dépôt dans un sous-dossier du vôtre, sans mécanisme de référence externe : plus simple pour les utilisateurs, mais l'historique du dépôt parent grossit.

### 7.7 Fichiers `.gitattributes` *(ajout)*

Le fichier `.gitattributes` définit un comportement par type de fichier. Il est versionné, donc partagé par toute l'équipe.

```gitattributes
# Normalise les fins de ligne
* text=auto eol=lf

# Fichier binaire
*.png binary

# Géré par Git LFS
*.psd filter=lfs diff=lfs merge=lfs -text

# Compté comme documentation par GitHub Linguist
docs/*.md linguist-documentation
```

| Attribut | Effet |
| --- | --- |
| `text=auto` | Git détecte les fichiers texte et normalise leurs fins de ligne |
| `eol=lf` / `eol=crlf` | Impose la fin de ligne à l'extraction |
| `binary` | Traite comme binaire : pas de diff texte, pas de fusion textuelle |
| `filter=lfs diff=lfs merge=lfs -text` | Délègue le fichier à Git LFS (voir 9.5) |
| `linguist-*` | Indications pour les statistiques de langages sur GitHub |
| `export-ignore` | Exclut le fichier des archives `git archive` |

Cette approche est plus fiable que `core.autocrlf` (voir 1.3.6), car elle s'applique à tous les contributeurs de la même façon, quel que soit leur système.

### 7.8 Exemple de workflow

```bash
git config --global alias.st status          # alias
echo '#!/bin/sh' > .git/hooks/pre-commit     # hook
echo 'echo "Vérifications avant commit"' >> .git/hooks/pre-commit   # remplacez par votre linter (npm run lint, etc.)
chmod +x .git/hooks/pre-commit
git submodule add https://github.com/user/lib.git libs/lib    # sous-module
git commit -am "Ajoute le sous-module lib"
```

Ce scénario illustre les quatre mécanismes du chapitre : un alias personnel, un hook local, un sous-module ajouté puis validé. Le hook se déclenchera à chaque commit (y compris le dernier) ; s'il retournait un code non nul, le commit serait refusé.

### 7.9 Pièges fréquents

- **Croire qu'un commit stocke un diff.** Il pointe vers un instantané complet ; les différences sont calculées à la demande.
- **Modifier le contenu de `.git` à la main** sans comprendre le rôle de chaque fichier : risque de corruption du dépôt.
- **Confondre `~` et `^`.** `HEAD~2` remonte de deux générations en suivant le premier parent ; `HEAD^2` désigne le second parent d'une fusion.
- **Penser que les hooks sont partagés.** Le dossier `.git/hooks` n'est pas versionné ; utilisez `core.hooksPath` ou un outil dédié. Un hook doit porter le nom exact, être exécutable, et reste contournable (`--no-verify`) : doublez les contrôles essentiels côté CI.
- **Oublier d'initialiser les sous-modules** après un clone ou un `pull` (`git submodule update --init --recursive`), ou pousser le dépôt parent **avant** le sous-module.
- **Écrire `includeIf "gitdir:~/travail"` sans `/` final** : la condition ne s'applique alors pas au contenu du dossier.
- **Compter sur `core.autocrlf`** pour harmoniser les fins de ligne d'une équipe mixte : préférez un fichier `.gitattributes` versionné.
- **Définir des alias trop ambigus** : un alias `undo` qui exécute `reset --soft` surprendra un collègue qui ne le connaît pas.

### Synthèse du chapitre 7

Git est une base de données **adressable par contenu** : quatre types d'objets (blob, tree, commit, tag annoté) identifiés par un hash, immuables et dédupliqués, compactés en fichiers pack par `git gc`. Les **références** (branches, étiquettes, branches de suivi) sont de petits fichiers contenant un hash ; `HEAD` est une référence symbolique vers la branche courante. Les **hooks** automatisent des contrôles, les **alias** raccourcissent les commandes, `includeIf` adapte la configuration au dossier, les **sous-modules** incluent un dépôt à un commit précis et `.gitattributes` définit un comportement par type de fichier.

---

# Partie III — Workflows, outils et plateformes

## 8. Workflows de collaboration

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez décrire et comparer les principaux workflows (centralisé, branches de fonctionnalité, Gitflow, fork, trunk-based) ; choisir celui qui convient à une équipe selon sa taille, son rythme de livraison et son outillage ; protéger la branche principale ; et appliquer les bonnes pratiques de collaboration.

Git ne prescrit aucune façon de s'organiser à plusieurs : il fournit des branches, des fusions et des distants, et l'équipe décide comment les combiner. Un **workflow** est cette convention d'équipe : quelles branches existent, qui peut écrire où, comment un changement arrive en production. Ce chapitre présente les modèles les plus répandus, leurs avantages, leurs limites et leurs critères de choix.

Un bon workflow répond à quatre questions :

1. Où le code stable vit-il ?
2. Où le travail en cours est-il fait ?
3. Comment un changement est-il relu et validé ?
4. Comment une version est-elle publiée et, au besoin, corrigée ?

### 8.1 Workflow centralisé

#### 8.1.1 Principe

Tout le monde travaille **directement sur une seule branche** (`main`) d'un dépôt partagé. C'est le modèle des systèmes centralisés comme SVN ; il reste courant dans les petites équipes, les projets personnels ou lors d'une transition depuis SVN.

```text
[développeur] → pull → modifier → commit → push → [main]
```

```bash
git clone https://github.com/org/depot.git
cd depot
git pull --rebase
# ...modifications...
git add . && git commit -m "Corrige une faute de frappe"
git push origin main
```

#### 8.1.2 Fonctionnement et régles

- Chaque contributeur récupère `main` avant de commencer et **avant de pousser**.
- Si le push est refusé (quelqu'un a poussé avant), on exécute `git pull --rebase`, on résout les éventuels conflits localement, puis on repousse.
- Le rebase au pull maintient un historique linéaire, sans commits de fusion parasites.

| Avantages | Inconvénients |
| --- | --- |
| Très simple | Risque de conflits |
| Idéal pour petites équipes | Aucune isolation des fonctionnalités |
| Peu de concepts à apprendre | `main` peut casser à tout moment |
|  | Pas de relecture formelle avant intégration |

### 8.2 Workflow par branches de fonctionnalité (*GitHub flow*)

#### 8.2.1 Principe

Chaque fonctionnalité ou correction est développée dans **une branche dédiée**, créée depuis `main`, puis fusionnée dans `main` après **relecture** par une *pull request*. La règle de base est que `main` doit être **toujours déployable**.

```text
main ──●────────●────────●──▶
        \      /  \      /
         feature/login   feature/signup
```

```bash
git switch main && git pull
git switch -c feature/navbar            # 1. branche
# ...modifications des fichiers...
git add . && git commit -m "Ajoute la barre de navigation"
git push -u origin feature/navbar       # 2. publier
# 3. ouvrir une pull request  → 4. relecture + CI → 5. fusion → 6. suppression de la branche
```

#### 8.2.2 Les six étapes

1. **Créer une branche** depuis un `main` à jour, avec un nom descriptif.
2. **Committer** régulièrement, avec des messages clairs.
3. **Ouvrir une pull request** tôt, même en brouillon (*draft*), pour favoriser la discussion.
4. **Relecture et intégration continue** : les collègues commentent, les tests automatiques s'exécutent. Les corrections sont de nouveaux commits sur la même branche.
5. **Fusionner** dans `main` lorsque la PR est approuvée et que la CI est verte.
6. **Supprimer la branche** fusionnée, puis déployer si l'équipe le pratique.

| Avantages | Inconvénients |
| --- | --- |
| Développement parallèle sûr | Un peu plus de discipline |
| Revue de code, historique propre | Les branches longues génèrent des conflits |
| `main` reste stable |  |
| S'adapte à toutes les tailles d'équipe |  |

### 8.3 Gitflow

#### 8.3.1 Principe

Modèle de branches **structuré**, adapté aux produits à **versions livrées** (logiciels installés, applications mobiles, bibliothèques avec plusieurs versions maintenues en parallèle, cycles de release planifiés).

```text
main        ●───────────────●──────────────●   (versions étiquetées)
             \             / \            /
develop       ●──●──●──●──●───●──●──●────●
                  \    /      \      /
              feature/*     release/*  hotfix/* (depuis main)
```

| Branche | Rôle |
| --- | --- |
| `main` | Code stable en production |
| `develop` | Intégration des fonctionnalités |
| `feature/*` | Nouvelles fonctionnalités (depuis `develop`) |
| `release/*` | Stabilisation avant livraison |
| `hotfix/*` | Correctifs urgents sur la production (depuis `main`) |

```bash
git switch -c develop main
git switch -c feature/paiement develop
# ...développement et commits sur la fonctionnalité...
# fin de fonctionnalité
git switch develop && git merge --no-ff feature/paiement
# préparer une release
git switch -c release/1.0 develop
```

#### 8.3.2 Cycle de vie

- **Fonctionnalité** : créée depuis `develop`, fusionnée dans `develop` (avec `--no-ff` pour garder la trace de la branche), puis supprimée.
- **Release** : quand `develop` contient assez de fonctionnalités, on crée `release/x.y` pour la stabilisation (corrections de bugs, numéro de version, documentation), sans ajouter de nouvelles fonctionnalités. Elle est ensuite fusionnée dans `main` (avec une étiquette de version) **et** dans `develop`.
- **Hotfix** : bug critique en production ; on branche depuis `main`, on corrige, puis on fusionne dans `main` (avec une nouvelle étiquette) **et** dans `develop`.

> **Attention** : l'auteur même du modèle recommande de **ne pas l'utiliser** pour les applications web livrées en continu : préférez GitHub flow ou le trunk-based development. Gitflow multiplie les branches longues, donc les conflits et la lourdeur.

| Avantages | Inconvénients |
| --- | --- |
| Rôles de branches très clairs | Lourd, nombreuses branches long-vivantes |
| Adapté à plusieurs versions en maintenance | Fusions fréquentes entre branches |
| Préparation de release encadrée | Excessif pour la livraison continue |

### 8.4 Workflow par fork

#### 8.4.1 Principe

Standard du **logiciel libre** : le contributeur n'a pas les droits en écriture sur le dépôt principal. Il travaille dans sa propre copie (le fork) et propose ses changements par pull request ; les mainteneurs décident de les intégrer.

```text
dépôt d'origine → fork → clone → branche → push → pull request → revue → fusion
```

Voir 4.5 pour les commandes (remote `upstream`, synchronisation, PR).

#### 8.4.2 Particularités

- **Deux remotes** : `origin` (le fork, où l'on peut pousser) et `upstream` (le projet d'origine, en lecture).
- Le contributeur est responsable de **tenir son fork à jour** en récupérant `upstream/main` régulièrement.
- Les mainteneurs contrôlent seuls ce qui entre dans `main`, ce qui convient aux projets ouverts à des inconnus.
- Il se combine souvent avec les branches de fonctionnalité : dans chaque fork, une branche par contribution.

| Avantages | Inconvénients |
| --- | --- |
| Contributions découplées, sans droits sur le dépôt | Synchronisation à gérer |
| Contrôle total des mainteneurs | Plus de manipulations pour le contributeur |
| Idéal pour grands projets ouverts | Forks qui divergent si non entretenus |

### 8.5 Développement sur tronc commun (*trunk-based*) *(ajout)*

#### 8.5.1 Principe

Tous les développeurs intègrent **très fréquemment** (au moins une fois par jour) dans `main` (le *tronc*), via des branches **très courtes** (quelques heures à un ou deux jours) ou directement. Les fonctionnalités inachevées sont masquées par des **drapeaux de fonctionnalité** (*feature flags*) : le code est livré mais désactivé tant que la fonctionnalité n'est pas prête. Ce modèle s'appuie fortement sur la **CI/CD** et les tests automatisés ; il est utilisé par de nombreuses grandes équipes.

#### 8.5.2 Prérequis

- Une suite de tests automatisés rapide et fiable ; `main` doit rester vert.
- Une intégration continue qui valide chaque changement avant fusion.
- Un système de *feature flags* pour livrer du code non activé.
- Des changements **petits** et fréquents, des revues rapides.
- Pour les releases : soit on étiquette directement `main`, soit on crée de courtes branches de release uniquement lorsque c'est nécessaire.

| Avantages | Inconvénients |
| --- | --- |
| Intégration rapide | Exige CI solide |
| Presque pas de branches longues, donc peu de conflits | Exige feature flags et discipline |
| Livraison continue facilitée | Culture d'équipe à construire |

### 8.6 Comparaison

| Workflow | Idéal pour | Avantages | Inconvénients |
| --- | --- | --- | --- |
| Centralisé | Petites équipes | Simplicité | Pas d'isolation, conflits |
| Branches de fonctionnalité | Équipes de toute taille | Structure claire, revues | Un peu plus complexe |
| Gitflow | Releases planifiées | Rôles de branches clairs | Lourd, excessif pour le web |
| Fork | Open source | Contributions découplées | Synchronisation à gérer |
| Trunk-based | Livraison continue | Intégration rapide, peu de branches longues | Exige CI solide et feature flags |

#### Comment choisir ?

- **Vous êtes seul ou deux, sans besoin de revue** : centralisé, ou branches de fonctionnalité pour garder le réflexe.
- **Application web déployée souvent, équipe moyenne** : GitHub flow, ou trunk-based si la CI est mature.
- **Logiciel livré par versions, plusieurs versions maintenues** : Gitflow ou une variante allégée.
- **Projet ouvert, contributeurs externes** : fork + pull requests.

En pratique, la plupart des équipes adoptent un hybride ; l'important est que la règle soit **écrite, connue et appliquée**.

### 8.7 Bonnes pratiques de collaboration *(ajout)*

- **Petites PR**, ciblées, avec une description claire (*quoi* et *pourquoi*). Une PR de quelques centaines de lignes est relue sérieusement ; une PR de milliers de lignes est survolée.
- Protégez `main` (**branch protection / rulesets**) : revue obligatoire, CI verte, pas de *force push*, pas de suppression.
- Un **`CONTRIBUTING.md`** et un fichier **`CODEOWNERS`** précisent les règles et les relecteurs. Le second associe des chemins du dépôt à des personnes ou équipes qui sont automatiquement sollicitées en revue.
- Mettez à jour votre branche (`git pull --rebase` ou `git merge main`) avant la revue.
- Supprimez les branches fusionnées (la plupart des plateformes proposent de le faire automatiquement).
- Choisissez et **documentez une stratégie de fusion** (merge commit, squash, rebase) pour que l'historique reste cohérent.
- Relisez avec bienveillance : commentez le code, pas la personne.
- Utilisez des modèles de PR et de tickets pour uniformiser les informations demandées.

### 8.8 Pièges fréquents

- **Laisser vivre des branches très longues.** Plus une branche s'éloigne de `main`, plus la fusion est douloureuse ; intégrez souvent.
- **Adopter Gitflow pour une application web livrée en continu.** Le modèle est conçu pour des versions planifiées ; il ajoute branches long-vivantes et fusions pour rien dans ce contexte.
- **Oublier de fusionner `release/*` et `hotfix/*` dans `develop`** (Gitflow) : le correctif disparaît à la prochaine release.
- **Ne pas écrire la règle.** Un workflow qui varie selon les personnes est pire que n'importe quel workflow cohérent ; documentez-le (`CONTRIBUTING.md`).
- **Laisser `main` sans protection** : pas de revue obligatoire, pas de CI requise, force push possible.
- **Ouvrir des pull requests énormes.** Elles sont survolées au lieu d'être relues ; gardez-les petites et ciblées.
- **Négliger la synchronisation d'un fork** : il diverge et les conflits s'accumulent.
- **Pratiquer le trunk-based sans CI solide ni feature flags** : `main` casse et les fonctionnalités inachevées sont exposées.

### Synthèse du chapitre 8

Un **workflow** est une convention d'équipe qui précise où vit le code stable, où se fait le travail en cours, comment un changement est relu et comment une version est publiée. Le workflow **centralisé** convient aux petites équipes, les **branches de fonctionnalité** (GitHub flow) aux équipes de toute taille, **Gitflow** aux produits à versions planifiées, le **fork** aux projets ouverts et le **trunk-based** à la livraison continue avec une CI mature. Quel que soit le choix : petites pull requests, `main` protégée, revue de code, `CODEOWNERS`, stratégie de fusion documentée et branches fusionnées supprimées.

---

## 9. Outils et astuces

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez retrouver l'auteur et le contexte d'une ligne avec `git blame` ; isoler un bug par dichotomie avec `git bisect` ; récupérer du travail perdu avec `git reflog` ; échanger des patchs ; gérer les gros fichiers avec Git LFS ; rechercher dans le code et l'historique ; et travailler efficacement sur de très gros dépôts.

Ce chapitre regroupe les commandes d'investigation et de récupération qui font gagner des heures : retrouver l'auteur d'une ligne, isoler un bug par dichotomie, récupérer un travail perdu, échanger des correctifs hors plateforme, gérer les fichiers volumineux, chercher dans le code et l'historique, et travailler sur de très gros dépôts.

### 9.1 Qui a modifié cette ligne ? (`git blame`)

#### 9.1.1 Principe

`git blame` annote chaque ligne d'un fichier avec le commit, l'auteur et la date de sa **dernière modification**. Son but n'est pas de désigner un coupable mais de retrouver le **contexte** d'une ligne : en remontant au commit, on lit le message, le ticket associé et les autres fichiers modifiés en même temps, ce qui explique souvent le pourquoi d'un code étrange.

```bash
git blame app.js
git blame -L 10,20 app.js        # lignes 10 à 20 seulement
git blame -w -C app.js           # ignore les espaces ; suit le code déplacé/copié
```

```text
f0a1234 (Alice 2026-09-01) const server = http.createServer();
c9b4567 (Bob   2026-09-05) server.listen(3000);
```

#### 9.1.2 Options

| Option | Effet |
| --- | --- |
| `-L début,fin` | Limite l'analyse à une plage de lignes (ou `-L :nomFonction`) |
| `-w` | Ignore les changements d'espaces |
| `-C` | Détecte les lignes copiées depuis d'autres fichiers |
| `-M` | Détecte les lignes déplacées dans le même fichier |
| `<commit> -- fichier` | Analyse à partir d'un commit donné (pour remonter plus loin) |

Pour ignorer des commits de reformatage massif (qui s'attribueraient toutes les lignes) : `git blame --ignore-revs-file .git-blame-ignore-revs`. On y liste les hashs à ignorer, un par ligne. Le réglage `git config blame.ignoreRevsFile .git-blame-ignore-revs` l'applique par défaut ; GitHub et GitLab lisent aussi ce fichier.

#### 9.1.3 Compléments

- `git log -L 10,20:app.js` affiche l'**historique de ces lignes**, commit après commit, avec les différences.
- Les interfaces des plateformes et des éditeurs (VS Code, JetBrains) présentent le blame de façon interactive.

### 9.2 Trouver le commit fautif (`git bisect`)

#### 9.2.1 Principe

Quand un bug est apparu « quelque part » entre une version qui fonctionnait et la version actuelle, relire des centaines de commits est inefficace. `git bisect` effectue une **recherche dichotomique** : il extrait le commit situé au milieu de l'intervalle, vous testez, vous indiquez s'il est bon ou mauvais, et l'intervalle est divisé par deux. Pour 1 000 commits, une dizaine de tests suffisent (environ log₂(1000) ≈ 10).

```bash
git bisect start
git bisect bad                    # le commit actuel est mauvais
git bisect good v1.0              # un commit antérieur connu comme bon
# Git extrait un commit au milieu : testez, puis répondez
git bisect good                   # ou : git bisect bad
# ...répétez jusqu'à identification du commit fautif
git bisect reset                  # revenir à l'état initial
```

Quand Git a isolé le premier mauvais commit, il l'affiche avec son message et ses fichiers. `git bisect reset` ramène alors `HEAD` sur la branche de départ.

#### 9.2.2 Commandes utiles

| Commande | Effet |
| --- | --- |
| `git bisect skip` | Ignorer un commit impossible à tester (ne compile pas, par exemple) |
| `git bisect log` | Afficher la liste des réponses déjà données |
| `git bisect visualize` | Afficher l'intervalle restant |
| `git bisect reset` | Terminer et revenir à la position initiale |

#### 9.2.3 Automatiser *(ajout)*

```bash
git bisect start HEAD v1.0
git bisect run pytest tests/test_bug.py    # le code de sortie décide : 0 = bon, ≠ 0 = mauvais
```

`git bisect run` exécute la commande donnée à chaque étape et décide seul : code de sortie `0` signifie « bon », `1` à `127` (sauf `125`) signifie « mauvais », et `125` signifie « à ignorer ». Il suffit d'avoir un test reproductible du bug, ce qui est une excellente raison d'en écrire un d'abord. Le découpage fin de l'historique en commits atomiques (voir 11.3) rend la méthode particulièrement efficace.

### 9.3 Retrouver des commits perdus (`git reflog`)

#### 9.3.1 Principe

Le **reflog** (*reference log*) journalise tous les déplacements de `HEAD` et des branches **en local** : commits, changements de branche, resets, rebases, fusions. Il est conservé environ 90 jours par défaut pour les entrées accessibles (et 30 jours pour les entrées devenues inaccessibles). Il sauve de nombreuses erreurs : `reset --hard`, rebase raté, branche supprimée, commit amendé par erreur…

```bash
git reflog
```

```text
fe3a5d4 HEAD@{0}: reset: moving to HEAD~1
c34ab91 HEAD@{1}: commit: Ajoute la fonctionnalité
```

Chaque ligne indique le hash atteint, la position relative (`HEAD@{1}` signifie « où était HEAD avant le dernier mouvement ») et l'action effectuée. Pour retrouver un état, il suffit de repérer la ligne correspondante, puis de s'y replacer :

```bash
git switch -c recuperation c34ab91     # recréer une branche sur le commit perdu
git reset --hard c34ab91               # ou revenir directement dessus
```

#### 9.3.2 Exemple : se remettre d'un mauvais `reset`

```bash
git reset --hard HEAD~1     # un commit perdu
git reflog                  # retrouver son hash
git reset --hard c34ab91    # restauré
```

#### 9.3.3 Limites

- Le reflog est **local** : il n'est ni poussé ni partagé. Un nouveau clone n'a pas votre reflog.
- Il ne contient que ce qui a été **commité** : des modifications jamais validées sont irrécupérables.
- Après expiration et `git gc`, les objets inaccessibles sont définitivement supprimés.
- Chaque branche possède aussi son reflog : `git reflog show main`. On y accède par `main@{2}` ou `main@{yesterday}` (voir 7.2).

Pour retrouver des commits orphelins sans reflog, `git fsck --lost-found` liste les objets inaccessibles du dépôt.

### 9.4 Patches (`git format-patch`, `git apply`, `git am`)

#### 9.4.1 Principe

Un **patch** est un fichier texte décrivant des modifications. Il permet d'échanger des changements **sans dépôt partagé** : par e-mail (c'est ainsi que fonctionne le développement du noyau Linux), par pièce jointe, ou pour sauvegarder un travail.

```bash
git format-patch -1 HEAD            # crée un fichier 0001-....patch pour le dernier commit
git format-patch main..feature      # un fichier .patch par commit
git format-patch -1 HEAD --stdout > changements.patch   # un seul fichier, nom choisi
git apply changements.patch         # applique les modifications (sans commit)
git am changements.patch            # ou : applique en recréant le commit (auteur conservé)
```

#### 9.4.2 Choisir entre `apply` et `am`

| Commande | Effet |
| --- | --- |
| `git format-patch` | Produit des patchs au format e-mail : un par commit, avec auteur, date et message |
| `git apply` | Applique le diff au répertoire de travail, **sans** créer de commit ; `--check` teste l'applicabilité |
| `git am` | Applique le patch **et crée le commit** en conservant auteur, date et message |

En cas d'échec de `git am`, résolvez puis `git am --continue`, ou `git am --abort` pour annuler. Pour un simple diff à partager sans métadonnées : `git diff > changements.diff` puis `git apply changements.diff`.

Utile pour envoyer des changements par e-mail ou hors plateforme.

### 9.5 Fichiers volumineux avec Git LFS

#### 9.5.1 Problème et solution

**Problème** : Git gère mal les gros fichiers binaires (images, vidéos, modèles 3D, jeux de données). Chaque version modifiée d'un binaire est stockée en entier, et comme tout l'historique est cloné, le dépôt devient énorme et lent.

**Solution** : **Git LFS** (*Large File Storage*) remplace ces fichiers dans le dépôt par de petits **pointeurs** (quelques lignes de texte contenant un identifiant et la taille) et stocke le contenu réel sur un serveur dédié. Le contenu n'est téléchargé que pour la version extraite.

```bash
git lfs install                  # une seule fois par machine
git lfs track "*.psd"            # écrit dans .gitattributes
git add .gitattributes
git add design.psd
git commit -m "Ajoute le fichier PSD via LFS"
git lfs ls-files                 # fichiers gérés par LFS
```

#### 9.5.2 Fonctionnement et précautions

- `git lfs track` ajoute une règle dans `.gitattributes` (voir 7.7) ; ce fichier doit être validé **avant** les fichiers concernés.
- Les fichiers déjà présents dans l'historique ne sont pas convertis automatiquement : `git lfs migrate import --include="*.psd"` réécrit l'historique pour le faire (opération à coordonner avec l'équipe).
- Sans Git LFS installé, un clone ne récupère que les pointeurs ; `git lfs pull` télécharge les contenus.
- Les fichiers LFS ne se fusionnent pas : en cas de modification concurrente, il faut choisir une version.

> **Attention** : vérifiez les quotas de stockage et de bande passante de votre plateforme (ils sont souvent limités et facturés). Autre option : conserver les gros fichiers hors de Git (stockage objet, DVC pour les données de machine learning).

### 9.6 Rechercher dans le code et l'historique *(ajout)*

```bash
git grep "TODO"                       # recherche dans les fichiers suivis
git grep -n "ma_fonction" v1.0        # dans une version donnée
git log -S"mot_de_passe" --oneline    # commits qui ajoutent ou retirent cette chaîne
git log -G"regex" --oneline           # idem avec une expression régulière
git log --follow -- chemin/fichier    # historique d'un fichier à travers les renommages
```

| Commande | Cherche... | Où ? |
| --- | --- | --- |
| `git grep "texte"` | Une chaîne ou regex | Dans les fichiers suivis, à une version donnée |
| `git log --grep="mot"` | Un mot | Dans les **messages** de commit |
| `git log -S"texte"` | Un texte dont le **nombre d'occurrences change** | Dans les diffs de l'historique |
| `git log -G"regex"` | Une expression régulière | Dans les lignes modifiées des diffs |
| `git log --follow -- chemin` | Les commits d'un fichier | Y compris sous ses anciens noms |

`git grep` est plus rapide que `grep` classique car il n'examine que les fichiers suivis, ignore automatiquement `.git` et les fichiers ignorés, et peut chercher dans n'importe quelle version. Options utiles : `-n` (numéros de ligne), `-i` (casse), `-c` (comptage par fichier), `-p` (fonction englobante).

### 9.7 Grands dépôts et performances *(ajout)*

| Technique | Commande |
| --- | --- |
| Clone superficiel | `git clone --depth 1 <url>` |
| Clone partiel | `git clone --filter=blob:none <url>` |
| Extraction partielle | `git sparse-checkout set dossier/` |
| Maintenance automatique | `git maintenance start` |
| Compactage manuel | `git gc` |

- **Clone superficiel** : seul le dernier commit est récupéré. Rapide et léger, mais l'historique est tronqué (`blame`, `bisect` limités). On le complète par `git fetch --unshallow`.
- **Clone partiel** (*partial clone*) : l'historique est complet mais les contenus de fichiers sont téléchargés **à la demande** (ici, `blob:none` ne récupère aucun contenu au clone ; Git va les chercher quand on en a besoin). Compatible avec tout l'historique.
- **Extraction partielle** (*sparse checkout*) : ne matérialise dans le répertoire de travail que certains dossiers d'un dépôt, utile pour les monorepos. `git sparse-checkout set dossier/` active le mode et limite l'arborescence ; `git sparse-checkout disable` revient à la normale. Il se combine avec le clone partiel.
- **Maintenance** : `git maintenance start` planifie en arrière-plan des tâches d'entretien (récupération préventive, compactage des objets, mise à jour du graphe de commits) qui maintiennent le dépôt rapide.
- **`git gc`** (*garbage collection*) : compacte les objets lâches en fichiers pack et supprime les objets inaccessibles expirés. Git le déclenche automatiquement de temps en temps ; l'exécuter à la main est rarement nécessaire.

### 9.8 Exemple : retrouver un bug avec bisect

```bash
git bisect start
git bisect bad                # le commit actuel contient le bug
git bisect good abc1234       # un commit où tout fonctionnait
git bisect good               # ... testez et répétez (good / bad)
git bisect reset
```

Déroulement commenté :

1. `bisect start` ouvre la session.
2. `bisect bad` déclare que le commit courant (où vous observez le bug) est mauvais.
3. `bisect good abc1234` déclare un ancien commit sain. Git extrait aussitôt un commit au milieu de l'intervalle.
4. Vous compilez ou lancez le test, puis vous répondez `good` ou `bad`. Git extrait le commit milieu de l'intervalle restant.
5. Après quelques itérations, Git annonce « *\<hash> is the first bad commit* » et affiche ses détails.
6. `bisect reset` vous ramène sur votre branche d'origine ; vous pouvez ensuite examiner le commit fautif avec `git show <hash>`.

### 9.9 Pièges fréquents

- **Utiliser `git blame` pour désigner un coupable.** Son but est de retrouver le contexte d'une ligne ; un commit de reformatage masque l'auteur réel, d'où `--ignore-revs-file`.
- **Mener un `bisect` avec un test instable ou impossible sur certains commits.** Utilisez `git bisect skip` pour les commits qui ne compilent pas, et un test déterministe ; terminez toujours par `git bisect reset`.
- **Compter sur le reflog comme sur une sauvegarde.** Il est local, expire après un certain temps et ne contient que ce qui a été commité.
- **Ajouter des fichiers volumineux avant de configurer LFS.** Validez d'abord `.gitattributes` (`git lfs track`) ; les fichiers déjà dans l'historique exigent `git lfs migrate`.
- **Ignorer les quotas de stockage et de bande passante LFS** de votre plateforme.
- **Oublier qu'un clone superficiel tronque l'historique.** `blame` et `bisect` y sont limités ; complétez avec `git fetch --unshallow`.
- **Croire que `git apply` crée un commit.** Seul `git am` recrée le commit en conservant l'auteur, la date et le message.
- **Rechercher dans le code avec un `grep` classique** quand `git grep` est plus rapide, respecte les fichiers ignorés et sait chercher dans une version donnée.

### Synthèse du chapitre 9

Ces outils font gagner des heures. `git blame` (et `git log -L`) retrouve le contexte d'une ligne ; `git bisect` isole un commit fautif par dichotomie, automatisable avec `git bisect run` ; `git reflog` récupère presque tout ce qui a été commité, même après un `reset --hard` ; `git format-patch`, `git apply` et `git am` échangent des changements hors plateforme ; **Git LFS** déporte les gros binaires ; `git grep`, `git log -S` et `git log --follow` explorent code et historique ; clones superficiels ou partiels, `sparse-checkout` et `git maintenance` gardent les gros dépôts rapides.

---

## 10. Interfaces graphiques, plateformes et CI/CD

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez choisir une interface graphique adaptée ; comparer les principales plateformes d'hébergement ; expliquer l'intégration et le déploiement continus ; lire un workflow GitHub Actions ligne par ligne ; et publier un site statique avec GitHub Pages.

Git est un outil en ligne de commande, mais il s'utilise dans un écosystème : interfaces graphiques pour visualiser, plateformes pour héberger et collaborer, intégration continue pour automatiser. Ce chapitre en présente les principaux repères.

### 10.1 Interfaces graphiques (GUI)

#### 10.1.1 Panorama

Une interface graphique affiche l'historique sous forme de graphe, rend visuels l'index, les diffs et les conflits, et simplifie certaines manipulations (indexation ligne par ligne, glisser-déposer de branches). Elle appelle en général les mêmes commandes Git en arrière-plan.

| Outil | Points forts | Plateformes |
| --- | --- | --- |
| **GitHub Desktop** | Simple, intégré à GitHub, idéal pour débuter | Windows, macOS |
| **Sourcetree** | Branches, stash, résolution de conflits | Windows, macOS |
| **GitKraken** | Interface soignée, graphe, intégrations | Windows, macOS, Linux |
| **Fork** | Rapide, outil de fusion visuel | Windows, macOS |
| **Git intégré à VS Code** | Commit, diff, branches, résolution de conflits | Toutes |
| **lazygit** | Interface en terminal, très efficace | Toutes |
| **JetBrains (IntelliJ, PyCharm…)** | Intégration Git complète | Toutes |

#### 10.1.2 VS Code

Le panneau *Source Control* (`Ctrl+Shift+G`) permet d'indexer et de valider des fichiers ou des lignes, de changer de branche, de consulter les diffs et de résoudre les conflits. En cas de conflit, l'éditeur affiche au-dessus de chaque zone des actions : *Accept Current Change* (garder la version de la branche courante), *Accept Incoming Change* (garder celle de la branche fusionnée), *Accept Both Changes* (garder les deux) et *Compare Changes*. Des extensions (par exemple GitLens) ajoutent le blame en ligne et l'historique détaillé.

> **Astuce** : même avec une interface graphique, **apprenez la ligne de commande** : elle donne un contrôle complet, reste identique partout, est indispensable sur les serveurs et dans les scripts, et permet de comprendre ce que l'interface fait réellement. Les erreurs surviennent le plus souvent quand on clique sans comprendre l'opération sous-jacente.

### 10.2 Plateformes d'hébergement

#### 10.2.1 Rôle

Une plateforme héberge des dépôts Git (nus) et ajoute des services de collaboration : gestion des utilisateurs et des droits, pull requests ou merge requests, suivi de tickets, wikis, intégration continue, registres de paquets et de conteneurs, pages web.

| Plateforme | Description | Fonctionnalités notables |
| --- | --- | --- |
| **GitHub** | La plus populaire (open source et privé) | PR, Issues, **GitHub Actions**, Discussions, Pages, Codespaces |
| **GitLab** | Plateforme DevOps complète, auto-hébergeable | CI/CD intégrée, Merge Requests, registre de conteneurs |
| **Bitbucket** | Intégré à l'écosystème Atlassian (Jira) | Pipelines, revue de code |
| **Azure DevOps** | Offre entreprise de Microsoft | Repos, Boards, Pipelines |
| **Gitea / Forgejo** | Légers, auto-hébergeables, libres | **Codeberg** est une instance publique de Forgejo |

#### 10.2.2 Critères de choix

- **Communauté et visibilité** : GitHub domine l'open source.
- **Auto-hébergement** : GitLab, Gitea et Forgejo peuvent tourner sur vos propres serveurs, ce qui compte pour la souveraineté des données.
- **Intégration avec vos outils** : Bitbucket avec Jira, Azure DevOps avec l'écosystème Microsoft.
- **Coûts et quotas** : minutes de CI, stockage LFS, dépôts privés.
- **Liberté logicielle** : Forgejo et Gitea sont libres ; Codeberg est géré par une association.

Comme Git est décentralisé, **changer de plateforme est simple** : on ajoute un nouveau remote, on pousse toutes les branches et étiquettes (`git push --mirror`), et on met à jour l'URL de `origin`. Seuls les éléments propres à la plateforme (tickets, PR, configuration de CI) demandent une migration spécifique.

### 10.3 Intégration continue (CI/CD)

#### 10.3.1 Définitions

La **CI/CD** exécute automatiquement tests et déploiements à chaque `push` ou *pull request*.

- **Intégration continue** (*Continuous Integration*, CI) : à chaque changement, on compile le projet et on lance les tests dans un environnement propre. On détecte ainsi immédiatement les régressions, avant la fusion.
- **Livraison continue** (*Continuous Delivery*) : chaque changement validé produit un artefact prêt à déployer, que l'on déclenche manuellement.
- **Déploiement continu** (*Continuous Deployment*) : le déploiement en production est lui aussi automatique.

La CI s'appuie directement sur Git : les événements (push, PR, étiquette) déclenchent des tâches, et le résultat (vert ou rouge) s'affiche sur la pull request. Combinée à la protection de `main` (chapitre 8), elle empêche de fusionner du code qui ne passe pas les tests.

#### 10.3.2 Exemple : GitHub Actions

Fichier `.github/workflows/test.yml` :

```yaml
name: Tests
on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Installer Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.14"        # entre guillemets (3.10 sans guillemets serait lu comme 3.1)
      - name: Installer les dépendances
        run: pip install -r requirements.txt pytest
      - name: Lancer les tests
        run: pytest
```

GitHub exécute ce workflow à chaque `push` sur `main` et à chaque PR.

#### 10.3.3 Lecture du fichier

| Élément | Rôle |
| --- | --- |
| `name` | Nom du workflow affiché dans l'interface |
| `on` | Événements déclencheurs : ici, un push sur `main` et toute pull request |
| `jobs` | Ensemble de tâches, exécutées en parallèle par défaut |
| `runs-on` | Système de la machine virtuelle (*runner*) : ici Ubuntu |
| `steps` | Étapes séquentielles d'un job |
| `uses` | Utilise une action réutilisable (ici `checkout` clone le dépôt, `setup-python` installe Python) |
| `run` | Exécute une commande shell |
| `with` | Paramètres passés à une action |

Le commentaire sur la version de Python est un piège classique de YAML : `3.10` non guillemeté est interprété comme le nombre décimal 3,1.

> **Astuce** : vérifiez régulièrement la **dernière version majeure** des actions (`checkout`, `setup-*`) ; les anciennes finissent par être dépréciées. Pour plus de sécurité, **épinglez** les actions tierces sur un **hash de commit** : une étiquette de version peut être déplacée par son auteur, pas un hash. GitLab CI (`.gitlab-ci.yml`), Bitbucket Pipelines et Azure Pipelines offrent des mécanismes équivalents.

#### 10.3.4 Bonnes pratiques de CI

- Gardez le pipeline **rapide** (quelques minutes) : une CI lente est contournée.
- Rendez les tests **déterministes** : un test instable (*flaky*) ruine la confiance.
- Limitez les permissions du jeton de la CI au strict nécessaire (par exemple lecture seule du contenu).
- Ne mettez **jamais** de secrets dans le fichier de workflow : utilisez les *secrets* chiffrés de la plateforme.
- Rendez la CI **obligatoire** pour fusionner (protection de branche).

### 10.4 Héberger un site statique avec GitHub Pages

**GitHub Pages** publie gratuitement un site statique directement depuis un dépôt.

1. Poussez votre site (HTML/CSS/JS) dans votre dépôt.
2. *Settings, puis Pages* : choisissez la **source** :
   - **Déployer depuis une branche** (`main` ou `gh-pages`, dossier `/` ou `/docs`), ou
   - **GitHub Actions** (pour générer le site avec Jekyll, Hugo, Vite, etc.).
3. Le site est publié à l'adresse `https://utilisateur.github.io/nom-du-depot`.

Un dépôt nommé `utilisateur.github.io` publie, lui, à la racine `https://utilisateur.github.io`. Un domaine personnalisé peut être associé dans les réglages. Le site est mis à jour à chaque push sur la branche source : le déploiement est une conséquence naturelle du workflow Git.

GitLab Pages, Cloudflare Pages ou Netlify proposent des services comparables.

### 10.5 Pièges fréquents

- **Cliquer dans une interface graphique sans comprendre l'opération sous-jacente.** La plupart des erreurs viennent de là ; sachez retrouver la commande équivalente.
- **Écrire `python-version: 3.10` sans guillemets** dans un workflow YAML : la valeur est lue comme le nombre décimal 3,1.
- **Utiliser des actions tierces non épinglées.** Une étiquette de version peut être déplacée par son auteur ; épinglez sur un hash de commit.
- **Placer des secrets en clair dans un fichier de workflow** ou accorder au jeton de la CI plus de permissions que nécessaire.
- **Tolérer une CI lente ou instable.** Une CI que l'on contourne ne protège plus rien ; gardez-la rapide et déterministe, et rendez-la obligatoire pour fusionner.
- **Choisir la mauvaise source pour GitHub Pages** (branche, dossier `/docs` ou GitHub Actions) ou oublier que l'adresse dépend du nom du dépôt.
- **Dépendre de fonctionnalités propres à une plateforme sans prévoir leur migration.** Git est portable (`git push --mirror`), pas les tickets, les pull requests ni la configuration de CI.

### Synthèse du chapitre 10

Les **interfaces graphiques** (GitHub Desktop, Sourcetree, GitKraken, VS Code, lazygit) visualisent l'historique et simplifient certaines manipulations, mais ne dispensent pas d'apprendre la ligne de commande. Les **plateformes** (GitHub, GitLab, Bitbucket, Azure DevOps, Gitea et Forgejo) hébergent des dépôts nus et ajoutent revues, tickets et CI. La **CI/CD** exécute automatiquement tests et déploiements à chaque push ou pull request : un workflow GitHub Actions se lit en `on` (déclencheurs), `jobs`, `runs-on`, `steps`, `uses` et `run`. **GitHub Pages** publie un site statique directement depuis un dépôt.

---

# Partie IV — Essentiels

## 11. Sécurité et bonnes pratiques

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez signer vos commits et vos étiquettes ; ne jamais committer de secrets et réagir correctement à une fuite ; appliquer les bonnes pratiques générales ; et diagnostiquer les problèmes courants avec une démarche méthodique.

*(Section ajoutée : ces sujets manquaient dans le guide d'origine.)*

Un historique Git est une mémoire quasi permanente et largement dupliquée. Ce qui y entre y reste, chez tous les clones. La sécurité consiste donc à éviter d'y mettre ce qui ne doit pas y être, à prouver l'origine des commits et à adopter des habitudes qui limitent les erreurs.

### 11.1 Signer ses commits

#### 11.1.1 Pourquoi signer ?

Dans Git, **le nom et l'adresse e-mail de l'auteur sont de simples déclarations** : n'importe qui peut écrire `git config user.name "Alice"` et créer des commits qui semblent écrits par Alice. La **signature cryptographique** prouve qu'un commit provient bien du détenteur d'une clé donnée et qu'il n'a pas été modifié depuis. Les plateformes affichent alors un badge **« Verified »** sur GitHub.

#### 11.1.2 Signer avec une clé SSH

Depuis Git 2.34, **vos clés SSH peuvent signer** : plus besoin de GPG.

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true      # signer tous les commits
git config --global tag.gpgsign true
```

Ajoutez ensuite la même clé publique dans GitHub comme **« Signing key »** (un type distinct de la clé d'authentification, même si l'on peut ajouter la même clé aux deux usages).

- `commit.gpgsign true` signe chaque commit automatiquement ; sinon on signe à la demande avec `git commit -S`.
- `tag.gpgsign true` signe les étiquettes annotées.
- Pour vérifier une signature localement avec SSH, il faut un fichier de signataires autorisés : `git config --global gpg.ssh.allowedSignersFile ~/.config/git/allowed_signers` (une ligne par personne : e-mail puis clé publique). On vérifie ensuite avec `git log --show-signature` ou `git verify-commit <hash>`.
- GPG reste possible (`gpg.format openpgp`, par défaut) et utile si votre organisation a une infrastructure de clés GPG.

Les règles de protection de branche peuvent exiger des commits signés pour fusionner dans `main`.

### 11.2 Ne jamais committer de secrets

#### 11.2.1 Prévention

Mots de passe, jetons d'API, clés privées, certificats, fichiers `.env` : **à ne jamais versionner**. Des robots parcourent en permanence les dépôts publics à la recherche de secrets, et un jeton publié est parfois exploité en quelques minutes.

- Placez-les dans `.gitignore` (dès la création du projet) et utilisez des variables d'environnement ou un gestionnaire de secrets (coffre-fort de la plateforme, gestionnaire d'entreprise).
- Fournissez un fichier modèle sans valeurs réelles, par exemple `.env.example`, qui est versionné.
- Activez les analyses de secrets (GitHub *secret scanning* et *push protection*, qui bloque le push) ou des outils comme **gitleaks** / **trufflehog**, idéalement dans un hook `pre-commit` (voir 7.3).

#### 11.2.2 Si un secret a été poussé

Supprimer le fichier dans un commit suivant **ne suffit pas** : il reste dans l'historique et dans tous les clones et forks. La procédure est :

1. **Révoquez-le / changez-le immédiatement** : il doit être considéré comme compromis. C'est l'étape la plus importante, et la seule qui protège réellement.
2. Supprimez-le de l'historique avec **`git filter-repo`** (successeur recommandé de `git filter-branch`, déprécié) ou **BFG Repo-Cleaner**.
3. Forcez l'envoi et demandez à vos collègues de recloner.

```bash
pip install git-filter-repo
git filter-repo --path secrets.env --invert-paths
git remote add origin <url>     # git filter-repo retire le remote par sécurité
git push --force --all
git push --force --tags
```

Points d'attention :

- `git filter-repo` est conçu pour s'exécuter sur un **clone frais** (il refuse un dépôt qui ne l'est pas, sauf `--force`), et il **réécrit tous les hashs** concernés.
- Les anciens clones, les forks et parfois les caches de la plateforme conservent l'ancien historique : c'est pourquoi la révocation du secret est indispensable. Contactez au besoin le support de la plateforme pour purger les caches.
- Les pull requests ouvertes et les branches des collègues doivent être rebasées ou recréées sur le nouvel historique.

### 11.3 Bonnes pratiques générales

| Pratique | Pourquoi |
| --- | --- |
| Commits **petits et atomiques** | Faciles à relire, à annuler, à bisecter |
| Messages **clairs** (*pourquoi*, pas seulement *quoi*) | Historique exploitable |
| `git status` / `git diff --staged` **avant chaque commit** | Éviter d'inclure des fichiers par erreur |
| **Tirer** (`pull`) avant de pousser | Moins de conflits |
| Ne pas réécrire l'historique partagé | Évite de casser le travail des autres |
| Utiliser `--force-with-lease` plutôt que `--force` | Sécurité |
| Un `.gitignore` dès le début du projet | Dépôt propre |
| Protéger `main` et exiger des revues | Qualité |
| Sauvegarder : un dépôt distant **est** une sauvegarde | Résilience |

Compléments :

- Un commit **atomique** ne contient qu'un changement logique et laisse le projet dans un état qui compile et passe les tests. C'est la condition pour que `revert`, `cherry-pick` et `bisect` fonctionnent bien.
- Commitez **souvent** en local (c'est gratuit et réversible), puis nettoyez avec `rebase -i` avant de partager.
- N'amalgamez pas reformatage massif et changement fonctionnel dans le même commit : isolez-les pour garder des diffs lisibles et un `blame` utile.
- Publiez vos travaux dès qu'ils sont présentables : une branche uniquement locale n'est pas sauvegardée si votre disque tombe en panne.
- Ne versionnez pas ce qui se régénère (dépendances, binaires compilés) ni de gros fichiers binaires sans LFS.
- Utilisez l'authentification par clé SSH ou par jeton à permissions minimales et durée limitée, activez l'authentification à deux facteurs sur votre compte de plateforme.

### 11.4 Problèmes courants

| Symptôme | Cause / solution |
| --- | --- |
| `fatal: not a git repository` | Vous n'êtes pas dans un dépôt : `cd` ou `git init` |
| `rejected … non-fast-forward` | Le distant a avancé : `git pull --rebase` puis `git push` |
| `Permission denied (publickey)` | Clé SSH non enregistrée / non chargée dans `ssh-agent` |
| `Your local changes would be overwritten` | Validez, mettez de côté (`git stash`) ou annulez vos changements |
| `detached HEAD` | `git switch -c nouvelle-branche` pour conserver votre travail |
| Fichier ajouté au `.gitignore` toujours suivi | `git rm --cached <fichier>` |
| Mauvais auteur dans les commits | `git config user.name` et `git config user.email`, puis `git commit --amend --reset-author` |

#### 11.4.1 Explications

- **`not a git repository`** : Git cherche un dossier `.git` dans le dossier courant puis ses parents. Vérifiez votre position avec `pwd` et `git rev-parse --show-toplevel`.
- **`non-fast-forward`** : voir 4.4.2. Ne répondez pas par `--force` sans avoir compris pourquoi la branche distante a avancé.
- **`Permission denied (publickey)`** : listez les clés chargées avec `ssh-add -l`, ajoutez la vôtre avec `ssh-add`, et vérifiez que la clé publique est bien enregistrée (voir 1.5.6). Diagnostic détaillé : `ssh -vT git@github.com`.
- **`Your local changes would be overwritten`** : Git refuse de changer de branche, de fusionner ou de récupérer car cela écraserait des modifications non validées. Choisissez : `git commit`, `git stash` ou `git restore`.
- **`detached HEAD`** : voir 7.2.4. Si vous avez déjà fait des commits, créez la branche **avant** de changer de position.
- **Fichier ajouté au `.gitignore` toujours suivi** : voir 2.7.3.
- **Mauvais auteur** : corrigez la configuration, puis réécrivez le dernier commit avec `--reset-author` (si plusieurs commits sont concernés : `git rebase -r <base> --exec "git commit --amend --reset-author --no-edit"`, uniquement avant publication).

#### 11.4.2 Démarche générale de dépannage

1. **Ne paniquez pas et ne forcez rien** : Git ne perd presque rien de ce qui est commité.
2. Lisez le message d'erreur en entier : il contient souvent la solution.
3. Faites `git status` : il indique l'état et propose des commandes.
4. Si une opération est interrompue (merge, rebase, cherry-pick), la plupart ont un `--abort` pour revenir à l'état d'avant.
5. En dernier recours, `git reflog` retrouve presque tout (voir 9.3).
6. Avant une manipulation risquée, créez une branche de sauvegarde : `git branch sauvegarde`.

### Synthèse du chapitre 11

Le nom et l'adresse de l'auteur d'un commit sont de simples déclarations : seule la **signature** (par clé SSH depuis Git 2.34, ou GPG) prouve l'origine d'un commit ou d'une étiquette. Un historique Git est une mémoire quasi permanente et dupliquée : on ne committe **jamais** de secret ; s'il y en a eu un, on le **révoque d'abord**, puis on le retire de l'historique avec `git filter-repo` avant de forcer l'envoi et de faire recloner l'équipe. Les bonnes pratiques (commits atomiques, messages clairs, `main` protégée, `--force-with-lease`) et une démarche de dépannage méthodique (lire l'erreur, `git status`, `--abort`, `git reflog`, branche de sauvegarde) évitent la plupart des incidents.

---

## 12. Aide-mémoire

**Objectifs d'apprentissage.** À la fin de ce chapitre, vous saurez retrouver rapidement la commande adaptée à un besoin ; retenir les dix règles fondamentales ; situer les principales évolutions de Git par version ; vous repérer dans le vocabulaire grâce au glossaire ; et poursuivre votre apprentissage avec les bonnes ressources.

Ce dernier chapitre condense le cours en documents de référence : commandes classées par besoin, modèle mental en quelques règles, évolutions récentes de Git, glossaire et ressources pour aller plus loin. Il ne remplace pas les chapitres précédents : chaque ligne renvoie à un concept expliqué plus haut.

### 12.1 Commandes essentielles

| Besoin | Commande |
| --- | --- |
| Initialiser / cloner | `git init` · `git clone <url>` |
| État | `git status -s` |
| Indexer | `git add <fichier>` · `git add -p` |
| Valider | `git commit -m "message"` |
| Historique | `git log --oneline --graph --all` |
| Différences | `git diff` · `git diff --staged` |
| Nouvelle branche | `git switch -c <nom>` |
| Changer de branche | `git switch <nom>` |
| Fusionner | `git merge <branche>` |
| Rebaser | `git rebase <base>` |
| Récupérer | `git fetch` · `git pull --rebase` |
| Envoyer | `git push` · `git push -u origin <branche>` |
| Désindexer | `git restore --staged <fichier>` |
| Annuler des changements | `git restore <fichier>` |
| Annuler un commit publié | `git revert <hash>` |
| Mettre de côté | `git stash` · `git stash pop` |
| Étiqueter | `git tag -a v1.0 -m "message"` |
| Retrouver du perdu | `git reflog` |
| Trouver un bug | `git bisect` |

#### 12.1.1 Complément : commandes par thème

**Configuration et démarrage** (chapitres 1 et 2)

| Besoin | Commande |
| --- | --- |
| Identité | `git config --global user.name "Nom"` · `git config --global user.email "mail"` |
| Voir la configuration | `git config --list --show-origin` |
| Branche initiale | `git config --global init.defaultBranch main` |
| Ignorer un fichier suivi | `git rm --cached <fichier>` puis le lister dans `.gitignore` |
| Pourquoi ce fichier est-il ignoré ? | `git check-ignore -v <fichier>` |

**Préparer et valider** (chapitre 2)

| Besoin | Commande |
| --- | --- |
| Tout indexer | `git add .` |
| Indexer seulement les fichiers suivis | `git add -u` |
| Renommer / supprimer | `git mv ancien nouveau` · `git rm <fichier>` |
| Valider en indexant les fichiers suivis | `git commit -am "message"` |
| Corriger le dernier commit | `git commit --amend` |
| Voir un commit | `git show <hash>` |

**Branches et étiquettes** (chapitre 3)

| Besoin | Commande |
| --- | --- |
| Lister les branches | `git branch -vv` |
| Créer sans basculer | `git branch <nom>` |
| Revenir à la branche précédente | `git switch -` |
| Fusion sans avance rapide | `git merge --no-ff <branche>` |
| Condenser en un commit | `git merge --squash <branche>` |
| Abandonner une fusion | `git merge --abort` |
| Supprimer une branche | `git branch -d <nom>` (sûre) · `git branch -D <nom>` (forcée) |
| Pousser une étiquette | `git push origin v1.0` |

**Distants et collaboration** (chapitre 4)

| Besoin | Commande |
| --- | --- |
| Ajouter un distant | `git remote add origin <url>` |
| Lister les distants | `git remote -v` |
| Ce qui est arrivé sur le serveur | `git fetch` puis `git log HEAD..origin/main --oneline` |
| Pousser après une réécriture | `git push --force-with-lease` |
| Supprimer une branche distante | `git push origin --delete <branche>` |
| Nettoyer les références distantes | `git fetch --prune` |

**Annuler et réécrire** (chapitres 5 et 6)

| Besoin | Commande |
| --- | --- |
| Annuler le dernier commit, garder le travail indexé | `git reset --soft HEAD~1` |
| Annuler le dernier commit, garder le travail non indexé | `git reset HEAD~1` |
| Annuler le dernier commit et le travail | `git reset --hard HEAD~1` |
| Mettre de côté y compris fichiers non suivis | `git stash -u` |
| Simuler un nettoyage | `git clean -n` |
| Rebase interactif | `git rebase -i HEAD~3` |
| Correctif automatique | `git commit --fixup <hash>` puis `git rebase -i --autosquash <base>` |
| Reporter un commit | `git cherry-pick <hash>` |
| Reprendre après résolution | `git merge --continue` · `git rebase --continue` |
| Abandonner | `git merge --abort` · `git rebase --abort` · `git cherry-pick --abort` |
| Deuxième répertoire de travail | `git worktree add -b <branche> <dossier>` |

**Investigation et outils** (chapitres 7 et 9)

| Besoin | Commande |
| --- | --- |
| Qui a modifié cette ligne ? | `git blame -L 10,20 <fichier>` |
| Commits qui touchent un texte | `git log -S"texte"` |
| Rechercher dans le code | `git grep -n "motif"` |
| Historique d'un fichier renommé | `git log --follow -- <fichier>` |
| Explorer un objet | `git cat-file -p <hash>` |
| Créer un patch | `git format-patch -1 HEAD` |
| Fichiers volumineux | `git lfs track "*.psd"` |
| Gros dépôt | `git clone --filter=blob:none <url>` · `git sparse-checkout set dossier/` |

#### 12.1.2 Les dix règles à retenir

1. Les trois zones : répertoire de travail, index, dépôt. `add` va du premier à la deuxième, `commit` de la deuxième au troisième.
2. Une branche est un pointeur ; `HEAD` indique où vous êtes.
3. Un commit est un instantané complet, identifié par un hash qui dépend de tout son contenu.
4. `fetch` regarde, `pull` regarde et intègre, `push` publie.
5. Les modifications **jamais commitées** sont les seules qu'on peut perdre pour de bon.
6. Pas encore poussé : on peut réécrire (`amend`, `reset`, `rebase`). Déjà poussé : on annule avec `revert`.
7. `--force-with-lease`, jamais `--force`, et jamais sur une branche partagée.
8. `git status` et `git diff --staged` avant chaque commit.
9. Aucun secret dans le dépôt ; s'il y en a eu un, on le révoque d'abord.
10. En cas de doute, `git reflog` et une branche de sauvegarde (`git branch sauvegarde`).

### 12.2 Nouveautés à connaître

| Version | Apport notable |
| --- | --- |
| 2.23 | `git switch` et `git restore` |
| 2.34 | Signature des commits avec des clés SSH |
| 2.37+ | `push.autoSetupRemote` |
| 2.54 – 2.55 | Hooks configurables et exécutés en parallèle, commande `git history` (réécriture simplifiée de l'historique) |
| **Git 3.0** *(à venir)* | Branche par défaut `main`, SHA-256 par défaut, format de références `reftable`, Rust requis |

Commentaire de lecture :

- **`switch` et `restore` (2.23)** : séparent les deux usages historiques de `git checkout` (changer de branche, restaurer des fichiers) pour des commandes plus claires et moins dangereuses.
- **Signature SSH (2.34)** : permet de signer commits et étiquettes avec la clé déjà utilisée pour l'authentification, sans GPG.
- **`push.autoSetupRemote` (2.37+)** : supprime la nécessité de `-u` au premier push d'une branche.
- **2.54 – 2.55** : hooks déclarés dans la configuration et exécutés en parallèle, et commande `git history` pour simplifier certaines réécritures d'historique.
- **Git 3.0 (à venir)** : version majeure annoncée, qui prévoit `main` comme branche par défaut, SHA-256 comme fonction de hachage par défaut, le format de stockage de références `reftable` et l'usage de Rust dans le code source. Ces changements pourront affecter les scripts et outils qui supposent SHA-1 ou `master`.

> **À noter** : vérifiez les détails exacts dans les notes de version sur git-scm.com (dernière version stable au moment de la rédaction du guide : **2.55**). Git évolue régulièrement : une version plus récente a pu paraître depuis.

### 12.3 Glossaire

| Terme | Définition |
| --- | --- |
| Avance rapide (*fast-forward*) | Fusion qui déplace simplement un pointeur, sans commit de fusion |
| Blob | Objet contenant le contenu brut d'un fichier |
| Branche | Pointeur mobile vers un commit |
| Branche de suivi distante | Copie locale en lecture seule de l'état d'une branche du serveur (`origin/main`) |
| Cherry-pick | Application d'un commit isolé sur une autre branche |
| Clone | Copie complète d'un dépôt, historique compris |
| Commit | Instantané enregistré, avec auteur, date, message et parents |
| Conflit | Modifications incompatibles que Git ne sait pas combiner seul |
| Dépôt nu (*bare*) | Dépôt sans répertoire de travail, utilisé comme point d'échange |
| Fork | Copie personnelle d'un dépôt sur une plateforme |
| Hash | Empreinte identifiant un objet (SHA-1 ou SHA-256) |
| HEAD | Référence indiquant la position courante |
| Hook | Script exécuté automatiquement à un moment du cycle Git |
| Index (*staging area*) | Zone de préparation du prochain commit |
| Merge (fusion) | Intégration d'une branche dans une autre |
| Origin | Nom conventionnel du dépôt distant principal |
| Pull request | Demande d'intégration de modifications, avec revue |
| Rebase | Rejeu de commits au-dessus d'une autre base |
| Reflog | Journal local des déplacements de `HEAD` et des branches |
| Remote | Raccourci nommé vers un dépôt distant |
| Squash | Fusion de plusieurs commits en un seul |
| Stash | Remise temporaire de modifications non validées |
| Étiquette (*tag*) | Pointeur fixe vers un commit, marquant une version |
| Tree (arbre) | Objet représentant un dossier |
| Upstream | Selon le contexte : branche distante suivie, ou dépôt d'origine d'un fork |
| Worktree | Répertoire de travail supplémentaire lié au même dépôt |

### 12.4 Ressources

- Livre officiel gratuit **Pro Git** (en français) : https://git-scm.com/book/fr/v2
- Documentation de référence : https://git-scm.com/docs
- Apprendre en jouant : https://learngitbranching.js.org/?locale=fr\_FR
- Modèles `.gitignore` : https://github.com/github/gitignore
- Conventional Commits : https://www.conventionalcommits.org/fr

Conseils pour progresser : pratiquez sur des dépôts jetables, lisez les pages `git help <commande>`, contribuez à un petit projet open source pour expérimenter le workflow par fork, et relisez ce cours après quelques semaines d'usage réel : les chapitres 5, 6 et 7 prennent tout leur sens une fois que l'on a vécu des conflits et des erreurs.

### Synthèse du chapitre 12

Ce chapitre condense l'ensemble du cours : les commandes classées par besoin et par thème, les **dix règles** à retenir (trois zones, branche = pointeur, commit = instantané, `fetch`/`pull`/`push`, seul ce qui n'a jamais été commité est perdu pour de bon, réécrire seulement ce qui n'est pas partagé, `--force-with-lease`, relire avant de valider, aucun secret, `reflog` en dernier recours), les évolutions marquantes de Git par version (de `switch` et `restore` en 2.23 à la préparation de Git 3.0), un glossaire et des ressources pour poursuivre. Relisez-le après quelques semaines de pratique : les chapitres 5, 6 et 7 prennent tout leur sens une fois que l'on a vécu des conflits et des erreurs.

---

*Fin du cours. Bon versionnement avec Git !*
