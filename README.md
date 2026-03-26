#  Puissance 4 - Projet Python (Tkinter)

##  À propos du projet
Ce projet est un jeu de **Puissance 4** entièrement jouable, développé en Python. 
Je l'ai réalisé en autodidacte dans le cadre de ma préparation et de ma réorientation vers le **BUT Informatique**. Mon objectif était de me familiariser avec la logique algorithmique, la manipulation de tableaux à deux dimensions et la Programmation Orientée Objet (POO) avant la rentrée.

##  Fonctionnalités
* **Interface Graphique (GUI) :** Création d'un plateau visuel interactif de 6 lignes par 7 colonnes.
* **Jouabilité à la souris :** Détection des clics par colonne pour faire "tomber" les jetons de manière réaliste (la case vide la plus basse est automatiquement trouvée).
* **Tour par tour :** Alternance automatique entre le Joueur 1 (Rouge) et le Joueur 2 (Jaune).
* **Détection de victoire :** Algorithme qui parcourt la grille pour détecter un alignement de 4 jetons (Horizontal, Vertical, et les deux Diagonales).
* **Fin de partie :** Affichage d'une fenêtre pop-up annonçant le vainqueur.

##  Technologies et Concepts Utilisés
* **Langage :** Python 3
* **Bibliothèque Standard :** `tkinter` (pour l'interface graphique `Canvas` et les alertes `messagebox`).
* **Concepts techniques appliqués :**
  * Programmation Orientée Objet (Classes, méthodes, constructeur `__init__`).
  * Gestion d'événements (Binding de clics de souris avec `<Button-1>`).
  * Algorithmique de parcours de matrices (boucles imbriquées `for`).

##  Comment lancer le jeu sur votre machine ?

1. Assurez-vous d'avoir Python installé sur votre machine.
2. Clonez ce dépôt ou téléchargez le fichier `puissance4.py`.
3. Ouvrez un terminal dans le dossier du jeu.
4. Exécutez la commande suivante :
   ```bash
   python puissance4.py
