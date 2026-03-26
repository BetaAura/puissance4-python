import tkinter as tk
from tkinter import messagebox

# --- Configuration du jeu ---
NB_LIGNES = 6
NB_COLONNES = 7
TAILLE_CASE = 100
RAYON_PION = 40

COULEUR_FOND = "#1E90FF"  # Bleu classique du plateau
COULEUR_VIDE = "#FFFFFF"  # Blanc pour les trous
COULEUR_J1 = "#FF0000"    # Pion Rouge (Joueur 1)
COULEUR_J2 = "#FFD700"    # Pion Jaune (Joueur 2)

class Puissance4GUI:
    def __init__(self, root):
        """Constructeur : initialise la fenêtre, les variables et l'interface."""
        self.root = root
        self.root.title("Puissance 4 - Projet Personnel")
        self.root.resizable(False, False) # Empêche de redimensionner la fenêtre
        
       
        self.plateau = [[0 for _ in range(NB_COLONNES)] for _ in range(NB_LIGNES)]
        self.joueur_actuel = 1
        self.jeu_termine = False

       
        self.canvas = tk.Canvas(root, width=NB_COLONNES * TAILLE_CASE, height=NB_LIGNES * TAILLE_CASE, bg=COULEUR_FOND)
        self.canvas.pack()
        
        
        self.canvas.bind("<Button-1>", self.clic_colonne)
  
        self.dessiner_plateau()

    def dessiner_plateau(self):
        """Dessine les ronds représentant les trous et les pions."""
        self.canvas.delete("all") # On efface l'écran avant de redessiner
        for l in range(NB_LIGNES):
            for c in range(NB_COLONNES):
                # Calcul des coordonnées (x0, y0) et (x1, y1) pour dessiner un cercle
                x0 = c * TAILLE_CASE + (TAILLE_CASE / 2) - RAYON_PION
                y0 = l * TAILLE_CASE + (TAILLE_CASE / 2) - RAYON_PION
                x1 = c * TAILLE_CASE + (TAILLE_CASE / 2) + RAYON_PION
                y1 = l * TAILLE_CASE + (TAILLE_CASE / 2) + RAYON_PION
                
                # Détermination de la couleur
                valeur = self.plateau[l][c]
                if valeur == 1:
                    couleur = COULEUR_J1
                elif valeur == 2:
                    couleur = COULEUR_J2
                else:
                    couleur = COULEUR_VIDE
                    
                # Dessin du cercle
                self.canvas.create_oval(x0, y0, x1, y1, fill=couleur, outline="black", width=2)

    def clic_colonne(self, event):
        """Fonction déclenchée quand le joueur clique sur une colonne."""
        if self.jeu_termine:
            return # Si le jeu est fini, on ne fait rien

        # On calcule dans quelle colonne le joueur a cliqué (grâce aux pixels)
        colonne = event.x // TAILLE_CASE
        
        # On fait "tomber" le pion : on cherche la case vide la plus basse
        ligne_valide = -1
        for l in range(NB_LIGNES - 1, -1, -1):
            if self.plateau[l][colonne] == 0:
                ligne_valide = l
                break
                
        # Si la colonne n'est pas pleine
        if ligne_valide != -1:
            self.plateau[ligne_valide][colonne] = self.joueur_actuel
            self.dessiner_plateau() # On met à jour l'affichage
            
            # Vérification de la victoire
            if self.verifier_victoire(self.joueur_actuel):
                self.jeu_termine = True
                nom_vainqueur = "Rouge" if self.joueur_actuel == 1 else "Jaune"
                # Affichage d'une fenêtre pop-up
                messagebox.showinfo("Victoire !", f"Félicitations, le joueur {nom_vainqueur} a gagné ! 🎉")
            else:
                # Changement de joueur
                self.joueur_actuel = 2 if self.joueur_actuel == 1 else 1

    def verifier_victoire(self, pion):
        """Vérifie si le pion actuel a aligné 4 jetons."""
        # 1. Horizontale
        for c in range(NB_COLONNES - 3):
            for l in range(NB_LIGNES):
                if self.plateau[l][c] == pion and self.plateau[l][c+1] == pion and self.plateau[l][c+2] == pion and self.plateau[l][c+3] == pion:
                    return True
        # 2. Verticale
        for c in range(NB_COLONNES):
            for l in range(NB_LIGNES - 3):
                if self.plateau[l][c] == pion and self.plateau[l+1][c] == pion and self.plateau[l+2][c] == pion and self.plateau[l+3][c] == pion:
                    return True
        # 3. Diagonale descendante
        for c in range(NB_COLONNES - 3):
            for l in range(NB_LIGNES - 3):
                if self.plateau[l][c] == pion and self.plateau[l+1][c+1] == pion and self.plateau[l+2][c+2] == pion and self.plateau[l+3][c+3] == pion:
                    return True
        # 4. Diagonale ascendante
        for c in range(NB_COLONNES - 3):
            for l in range(3, NB_LIGNES):
                if self.plateau[l][c] == pion and self.plateau[l-1][c+1] == pion and self.plateau[l-2][c+2] == pion and self.plateau[l-3][c+3] == pion:
                    return True
        return False

if __name__ == "__main__":
    fenetre_principale = tk.Tk()
    jeu = Puissance4GUI(fenetre_principale)
    fenetre_principale.mainloop()