# Importation des modules
import numpy as np

def acc(v,dt):
    """Fonction qui calcule l'accélération à partir de la vitesse

    Entrées:
        - v : La vitesse mesurée, vecteur (array) [m/s]
        - dt : Le pas de temps [s]

    Sortie:
        - Vecteur de valeur numérique de l'accélération instantanée au temps t [m/s^2]
    """

    # Fonction à écrire

    return # à compléter

def force_poussee(v,a,cst):
    """Fonction qui calcule la force de poussée nécessaire

    Entrées:
        - v : La vitesse mesurée, vecteur (array) [m/s]
        - a : L'accélération de l'avion, vecteur (array) [m/s^2]
        - cst : Objet de class constantes() avec les valeurs suivantes
            - rho : La densité de l'air [kg/m^3]
            - S : La surface de référence [m^2]
            - C : Le coefficient de traînée [-]
            - m : La masse de l'avion [kg]

    Sortie:
        - Vecteur de valeurs numériques de la force de poussée nécessaire
            pour l'accélération de l'avion [N]
    """

    # Fonction à écrire

    return # à compléter

def trapeze(x,y):
    """Fonction qui calcule l'intégrale avec la méthode des trapèzes

    Entrées:
        - x : Valeurs de l'abscisse, vecteur (array)
        - y : Valeurs de l'ordonnée, vecteur (array)

    Sortie:
        - Valeur de l'intégrale calculée (float)
    """

    # Fonction à écrire

    return # à compléter

def simpson(x,y):
    """Fonction qui calcule l'intégrale selon Simpson 1/3
    
    Entrées:
        - x : Les abcisses de la courbe étudiée, vecteur (array)
        - y : Les ordonnées de la courbe étudiée, vecteur (array)
    
    Sortie:
        - Valeur numérique de l'intégrale
    """
    
    # Fonction à écrire
        
    return # à compléter