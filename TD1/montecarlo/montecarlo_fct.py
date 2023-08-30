# Importation des modules
import matplotlib.pyplot as plt
import numpy as np
import random 
def genXY(n):
    """Fonction de génération de points aléatoires
    
    Entrée:
        - n : nombre de points à générer, entier (int)
    
    Sortie:
        - Retourne 2 vecteurs, positions en x et positions en y
    """
    assert isinstance(n,int) or isinstance(n,np.int32), "n pas du bon type."
    
    ### Fonction à écrire
    x = np.random.uniform(low=-1, high=1, size=n)
    y = np.random.uniform(low=-1, high=1, size=n)
    return x, y ### Valeurs retournées

def monte_carlo(x,y):
    """Fonction calculant pi par la méthode de Monte Carlo
    
    Entrée:
        - x : vecteur de positions en x
        - y : vecteur de positions en y
    
    Sortie:
        - Retourne 1 valeur float, approximation de pi
    """
    assert len(x)==len(y), "Grandeurs des vecteurs ne concordent pas."
    
    ### Fonction à écrire
    # pi / 4 = Ncercle / N 
    # pi = 4 * Ncercle / N 
    # condition a verifier pour confirmer si on est dans le cercle 
    # x**2 + y**2 <= (r**2 = 1) 
    
    sum = x**2 + y**2
    Ncercle = len([i for i in sum if i<=1])# on compte tous les points où la distance est plus petite que  1 (intérieur du cercle) 
    pi = 4 * (Ncercle / len(x))
    return pi ### Valeur retournée