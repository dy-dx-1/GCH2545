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
    # Calculons les lignes 1 à 1 pour essayer de garder le tout clair 
    l1 = yi[0] - y[0] + dt*(prm.p - y[0] * (prm.b*y[1] + prm.d))
    l2 = yi[1] - y[1] + dt*(y[1]*y[0]*(prm.b-prm.a) + y[2]*prm.e)
    l3 = yi[2] - y[2] + dt*(-prm.e*y[2] + y[0]*(prm.d + prm.a*y[1])) 
    return np.array([l1, l2, l3])

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