# Importation des modules
import matplotlib.pyplot as plt
import numpy as np
import pytest
try:
    from montecarlo_fct import *
except:
    pass

import montecarlo_corr

#-----------------------------------------------------------------------------
# Code principal pour l'analyse des résultats
# Il faudra appeler les fonctions du fichier montecarlo_fct.py afin de créer
# des points aléatoires pour ensuite calculer l'erreur par rapport à la valeur
# exacte de pi.
# Ensuite, il faudra générer un graphique pour visualiser l'erreur selon
# le nombre de points utilisés. Attention de bien générer un nouvel ensemble
# de points à chaque calcul de pi.
#-----------------------------------------------------------------------------

# Code principal
## Génération de points et calcul de pi
nb_pts_eval = range(100, 10001)  # liste de densité des pts à évaluer 
pi_results = list() # liste qui contiendra toutes les approximations de pi 
for pt_density in nb_pts_eval: 
    x, y = genXY(pt_density) 
    pi_results.append(monte_carlo(x,y))

## Calcul de l'erreur et graphique
# création d'une liste contenant les erreurs correspondantes en soustrayant pi et les approx
erreurs = [(np.pi - approx_pi) for approx_pi in pi_results]
# création du graphique
plt.plot(nb_pts_eval, erreurs, '-')
plt.xlabel("Nombre de points dans l'approximation") 
plt.ylabel("Erreur") 
plt.title("Erreur commise par la méthode de Monte Carlo dans l'approximation de pi avec différents points")
plt.grid() 
plt.show() 
# Correction
pytest.main(['-q', '--tb=long', 'montecarlo_corr.py'])