import numpy as np

# Fonction de la conjecture de Collatz
def collatz(i):
    """Fonction de calcul du nombre d'itération pour la conjecture de Collatz
    
    Entrée:
        - i : nombre entier en entrée (int)
    
    Sortie:
        - Un nombre entier correspondant au nombre d'itération
    """
    assert type(i) != float, "Pas le bon type."
    assert type(i) != str, "Pas le bon type."
    assert type(i) != np.float64, "Pas le bon type."
    
    ### Fonction à écrire
    counter = 0 
    while i!=1: 
        i=i/2 if i%2==0 else 3*i+1 
        counter+=1 
    return counter ### à compléter