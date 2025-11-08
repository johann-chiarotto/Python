# Jeux Pygame

## 👥 Présentation et Membres du groupe

Groupe : **Space Hell**

- Johann Chiarotto
- Dylan Thomas
- Alexis Rodrigues

## 📝 Description

**Space Hell**

Space Hell est un jeu développé avec Pygame où le joueur doit éviter des vagues de météorites. Le joueur dispose de 5 cœurs (points de vie), d’une fonctionnalité de dash pour esquiver rapidement, et peut ramasser des pièces afin d’augmenter son score. La difficulté augmente progressivement à mesure que la partie avance.
## 🎯 Objectifs du projet

- Réaliser un jeu en Python avec la librairie Pygame .
- Mécaniques de déplacement spéciaux (Dash, glissade, …)
- Mécanique gameplay
- Intelligence artificielle et adaptation de comportement

## 🛠️ Fonctionnalités

- **Pseudo** : Avant de commencer la partie, le joueur doit saisir un pseudo. Celui-ci permettra d’enregistrer son score et de l’identifier dans le classement.
- **Esquiver les météorites / Ramasser les pièces** : Dès le début du jeu, le joueur doit éviter les météorites qui tombent tout en ramassant les pièces pour augmenter son score. Plus le joueur collecte de pièces, plus son score final sera élevé.
- **Levels** : Le jeu est divisé en niveaux qui augmentent automatiquement toutes les minutes. À partir du niveau 5, la partie devient illimitée, et la difficulté continue de croître sans fin.
- **Vitesse** : Au fur et à mesure que le joueur progresse dans les niveaux, le nombre de météorites augmente, tout comme leur vitesse, rendant l’esquive de plus en plus difficile.
- **Système de sauvegarde** : Un tableau des scores garde en mémoire les cinq meilleurs résultats, affichant à la fois le pseudo et le score total de chaque joueur.
- **Scores** : Pendant la partie, le joueur accumule des points en survivant le plus longtemps possible et en ramassant des pièces. Le score final est calculé à partir du temps passé et du nombre de pièces collectées.

## 🔑 Points clefs

- **Dash** : Nous avons intégré à notre jeu un système de dash qui permet de se déplacer plus rapidement sur un côté, vers l’avant ou même vers l’arrière.
- **Difficulté** : Plus vous avancerez dans le jeu, plus cela demandera de réflexes et d’observation.

## ⬇️ Prérequis

Avant de commencer, assurez-vous d’avoir les éléments suivants installés sur votre machine :

- **Librairie Pygame et Pytmx**
- **Python** 
  
## 📥 Installation

1. Clonez le dépôt :

```bash
git clone https://ytrack.learn.ynov.com/git/cjohann/python_project.git
```

2. Accédez au répertoire du projet :

```bash
cd Projet
```

3. Exécutez le serveur avec :

```bash
python3 main.py 
```