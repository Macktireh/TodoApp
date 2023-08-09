# Application de Todo Liste

## Description du  projet :

Je te présente le projet que tu vas entreprendre : la création d'une application TodoApp avec des fonctionnalités CRUD. Pour mener à bien ce projet, tu utiliseras le langage de programmation Python ainsi que la bibliothèque Tkinter pour créer une interface graphique conviviale.

L'objectif principal de cette application est de développer une interface utilisateur Tkinter qui permettra d'effectuer les opérations CRUD (Create, Read, Update, Delete) suivantes :

- **Créer une tâche** : Les utilisateurs pourront ajouter de nouvelles tâches à leur liste.

- **Afficher la liste des tâches** : La liste des tâches existantes sera affichée dans l'interface, montrant leur état (complétée ou non) et d'autres détails.

- **Modifier une tâche** : Les utilisateurs auront la possibilité de modifier les détails d'une tâche existante, comme son nom ou son statut de complétion.

- **Supprimer une tâche** : L'application permettra également de supprimer des tâches de la liste.

Pour faciliter la gestion des données, un fichier appelé db.json contiendra la liste des tâches. Pour accéder à ces données et exécuter les opérations CRUD, tu mettras en place un petit serveur utilisant l'API json-server pour les points d'accès (endpoints). Pour interagir avec cette API, tu utiliseras la bibliothèque Python "requests".

Voici un exemple des données que tu trouveras dans le fichier db.json :

```json
{
    "tasks": [
        {
            "id": 1,
            "title": "Faire les courses",
            "completed": true
        }
    ]
}
```

La mise en place du projet consistera à créer l'interface Tkinter, à configurer le serveur json-server pour gérer les données et les opérations CRUD, ainsi qu'à utiliser la bibliothèque "requests" pour interagir avec l'API. Ce projet te donnera l'occasion de développer tes compétences en programmation Python, de concevoir des interfaces graphiques et d'apprendre à gérer les opérations CRUD avec une API.

Pour te fournir un exemple concret de l'application TodoApp et t'inspirer dans la conception de son design, voici le lien vers une application fonctionnelle : https://macktireh.github.io/brython-todo-app/

Cette application te donnera une idée visuelle de ce à quoi ressemble une TodoApp en action. Tu pourras observer comment les tâches sont affichées, comment les interactions utilisateur sont gérées et comment les opérations CRUD sont mises en œuvre. En explorant cette application, tu pourras obtenir des idées sur la disposition des éléments d'interface, les couleurs, les icônes et la manière dont les utilisateurs peuvent facilement interagir avec les tâches.

N'hésite pas à examiner le design, la convivialité et les fonctionnalités de cette application pour t'aider à guider ta propre conception dans la réalisation de ton projet TodoApp avec Tkinter. Il est souvent bénéfique de s'inspirer de projets existants pour mieux comprendre les bonnes pratiques de conception et d'expérience utilisateur.


## Configuration du projet :

Pour entamer ce projet, assure-toi d'avoir les prérequis essentiels tels que Python, Node.js et Git installés sur ton système. Si tu ne les as pas déjà installés, voici les liens pour les télécharger et les installer :

- Python : Télécharge Python depuis https://www.python.org/downloads/
- Node.js : Télécharge Node.js depuis https://nodejs.org/en/download/
- Git : Télécharge Git depuis https://git-scm.com/downloads

Une fois ces prérequis en place, tu peux passer à la configuration du projet en suivant ces étapes :

**1) Clone le projet depuis GitHub en exécutant la commande suivante dans ton terminal :**

```bash
git clone https://github.com/Macktireh/TodoApp
```

```bash
cd TodoApp
```

**2) Crée un environnement virtuel python**

Pour isoler les dépendances du projet en utilisant la commande appropriée selon ton système d'exploitation. Par exemple, pour créer un environnement virtuel nommé ".venv" :

```bash
python -m venv .venv
```

***Sur Windows :***

```bash
.venv\Scripts\activate
```

***Sur macOS/Linux :***

```bash
source .venv/bin/activate
```

**3) Installe les dépendances Python et Node.js en utilisant les commandes suivantes :**

```bash
pip install -r requirements.txt
```

```bash
npm install -g json-server
```

**4) Lance le serveur JSON en exécutant la commande :**

```bash
npm start
```

À ce stade, ton projet est correctement configuré, ton environnement virtuel est actif et le serveur JSON est opérationnel. Tu es prêt à commencer à travailler sur ta TodoApp en utilisant Python, Tkinter et les données gérées par le serveur JSON.

N'hésite pas à parcourir les fichiers du projet, en particulier le fichier principal main.py, qui constitue le cœur de ton application. Tu es totalement libre de choisir l'organisation et l'architecture qui conviennent le mieux à ton application.

Bonne chance !