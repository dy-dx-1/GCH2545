# Importation des modules
import numpy as np

def fonc(v,prm):
    """Fonction calculant le système d'équations
    Entrées:
        - v : Variables inconnues
            - [0] = x
            - [1] = y
            - [2] = z
        - prm : Objet class parametres()
            - o : sigma
            - b : beta
            - p : rho

    Sortie:
        - Vecteur (array) contenant les valeurs numériques du système d'équations
    """

    # Fonction à écrire

    return # à compléter

def rk4(ci,dt,tf,prm):
    """Fonction résolvant le système avec Runge-Kutta 4
    Entrées:
        - ci : Conditions initiales
            - [0] = x
            - [1] = y
            - [2] = z
        - dt : Pas de temps
        - tf : Temps final de simulation
        - prm : Objet class parametres()
            - o : sigma
            - b : beta
            - p : rho

    Sorties (dans l'ordre énuméré ci-bas):
        - Matrice (array) des solutions dans le temps, incluant les conditions initiales
            - Chaque ligne représente les solutions (x,y,z) à un temps donné
            - Chaque colonne représente l'évolution d'une coordonnée dans le temps
        - Vecteur (array) du temps de simulation, allant de 0 à tf exclu
    """

    # Fonction à écrire

    return # à compléter
