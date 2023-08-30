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
    Ncercle = len(np.delete(sum, np.where(sum>=1))) # on enlève tous les index où la somme dépasse 1 (extérieur du cercle) 
    pi = 4 * (Ncercle / len(x))
    return pi ### Valeur retournée

#x,y= genXY(100) 
#plt.plot(x,y,'.')
#d_c = np.linspace(-1,1,1000)
#plt.plot(d_c, [np.sqrt(1-(x**2)) for x in d_c], 'r-')
#plt.plot(d_c, [-np.sqrt(1-(x**2)) for x in d_c], 'r-')
#plt.grid()
#plt.show()