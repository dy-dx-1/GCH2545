# Importation des modules
import numpy as np

def residu(y,yi,prm,dt):
    """Fonction calculant le résidu de la dynamique d'une invasion de zombie
    
    Entrées:
        - y : Variables dépendantes
            - [0] : S, humains susceptibles de devenir zombies
            - [1] : Z, zombies
            - [2] : R, retirés du bassin
        - yi : Estimés initiaux (même ordre que y)
        - prm : Objet class parametres()
            - e : taux de résurrection en zombie (zeta)
            - b : taux de transformation en zombie (beta)
            - a : taux de mort de zombie (alpha)
            - d : taux de mort naturelle (delta)
            - p : taux de naissance (pi)
        - dt : Pas de temps
    
    Sortie:
        - Vecteur (array) contenant les valeurs numériques du résidu
    """
    
    # Fonction à écrire

    return # à compléter

def jacobien(y,prm,dt):
    """Fonction calculant le jacobien de la dynamique d'une invasion de zombie
    
    Entrées:
        - y : Variables dépendantes
            - [0] : S, humains susceptibles de devenir zombies
            - [1] : Z, zombies
            - [2] : R, retirés du bassin
        - prm : Objet class parametres()
            - e : taux de résurrection en zombie (zeta)
            - b : taux de transformation en zombie (beta)
            - a : taux de mort de zombie (alpha)
            - d : taux de mort naturelle (delta)
            - p : taux de naissance (pi)
        - dt : Pas de temps
    
    Sortie:
        - Matrice (array) contenant les valeurs numériques du jacobien
    """
    
    # Fonction à écrire

    return # à compléter

def euler_implicite(ci,dt,tf,tol,prm):
    """Fonction calculant le résidu de la dynamique d'une invasion de zombie
    
    Entrées:
        - ci : Conditions initiales
            - [0] : S, humains susceptibles de devenir zombies
            - [1] : Z, zombies
            - [2] : R, retirés du bassin
        - dt : Pas de temps
        - tf : Temps final de simulation
        - tol : Critère d'arrêt
        - prm : Objet class parametres()
            - e : taux de résurrection en zombie (zeta)
            - b : taux de transformation en zombie (beta)
            - a : taux de mort de zombie (alpha)
            - d : taux de mort naturelle (delta)
            - p : taux de naissance (pi)
    
    Sorties (dans l'ordre énuméré ci-bas):
        - Matrice (array de taille (temps, 3)) des solutions de y en fonction du temps
        - Vecteur (array) du temps de simulation
    """
    
    # Fonction à écrire

    return # à compléter