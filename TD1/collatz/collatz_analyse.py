# Importation des modules
import matplotlib.pyplot as plt
import numpy as np
import pytest
try:
    from collatz_fct import *
except:
    pass

import collatz_corr

#-----------------------------------------------------------------------------
# Code principal pour l'analyse des résultats des fonctions
# Il faudra appeler la fonction collatz programmée dans collatz_fct.py afin
# de calculer le nombre d'itérations pour les entiers de 1 à 5000 et générer
# 2 graphiques pour la visualisation des résultats.
#-----------------------------------------------------------------------------

# Code principal
## trouver # itérations pour chaque entier 
iterations_collatz = [collatz(num) for num in range(1, 5001)]

#Graphiques
#### QUESTION B 
plt.plot(range(1,5001), iterations_collatz, '.')
plt.grid() 
plt.title("Itérations de la conjecture de Collatz pour les entiers entre 1 et 5000")
plt.xlabel("Nombres entiers") 
plt.ylabel("Nombre d'itérations de la conjecture de Collatz")
plt.show()

#### QUESTION C 
# la méthode hist de matplotlib.pyplot est capable seule de créer un histogramme directement
plt.hist(iterations_collatz) 
plt.show() 

#Correction
pytest.main(['-q', '--tb=long', 'collatz_corr.py'])