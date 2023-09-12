# Importation des modules
import numpy as np
import matplotlib.pyplot as plt
import pytest

try:
    from tige_fct import *
except:
    pass

#-----------------------------------------------------------------------------
# Code principal pour l'analyse des résultats
# Il faudra faire appel aux fonctions programmées dans tige_fct.py afin de
# calculer l'intégrale d'une fonction selon la quadrature de Gauss. Ensuite,
# il faudra évaluer l'erreur par rapport à la valeur analytique et afficher
# un graphique de cette erreur selon le nombre de points.
#-----------------------------------------------------------------------------

#%% Calcul de l'intégrale numérique
resultats = np.array([gauss(0, np.pi/2, n) for n in range(1,6)]) # on a besoin de le cast à array pour simplifier les manips qu'on fera plus tard 

# Affichage en tableau
###TODO: Confirm c'est quoi qu'on doit afficher, l'énoncé dit tableau 
plt.plot(range(1,6), resultats, "b.", label="Résultat de l'intégrale") 
plt.title("Résultat de l'intégrale avec la méthode de Gauss-Legendre selon différents nombres de points") 
plt.xlabel("Nombre de points utilisé") 
plt.ylabel("Valeur calculée par la quadrature") 
plt.grid() 
plt.legend() 
plt.show() 

#%% Calcul de l'erreur commise
ref_t = 0.99888139 
err = abs(resultats-ref_t) 

# Affichage du graphique
plt.plot(range(1,6), err, "g.-", label="Erreur absolue")
plt.title("Erreur produite selon le nombre de points utilisés par la quadrature")
plt.xlabel("Nombre de points") 
plt.ylabel("Erreur absolue") 
plt.grid()
plt.legend() 
plt.show()
plt.show()

#%% Correction
pytest.main(['-q', '--tb=long', 'tige_corr.py'])
