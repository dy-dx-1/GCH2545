#Importation des modules
import numpy as np


# Fonction de la serie harmonique
def serie_harmonique(N):
    """Fonction qui calcule la série harmonique en sommant les N premiers termes
    
    Sortie:
        - Un nombre flottant contenant la valeur de la série
    """
    res = 0 
    for i in range(1, N+1):
        res+=1/i 
    
    return res

# Fonction de la fonction factorielle
def factoriel(k):
    """Fonction qui calcule le factoriel de k

    Sortie:
        - Un nombre entier contenant le factoriel de k
    """ 
    res = k
    for i in range(k-1, 1, -1): 
        res = res*i 

    return res