# Importation des modules
import numpy as np
import matplotlib.pyplot as plt
import pytest
import oscillateur_corr
try:
    from oscillateur_fct import *
except:
    pass

#------------------------------------------------------------------------------
# Code principal pour l'analyse des résultats
# Il faudra faire appel aux fonctions programmées dans oscillateur_fct.py afin
# d'évaluer la solution d'un système d'équations différentielles ordinaires
# avec différentes méthodes numériques et comparer les résultats
# graphiquement.
#------------------------------------------------------------------------------

# Assignation des paramètres et conditions initiales
# ATTENTION! Ne pas changer le nom des attributs
class parametres():
    k = 1       # Constante de rappel du ressort [kg]
    m = 1       # Masse accroché au ressort [N/m]
prm = parametres()

# Euler explicite


# Runge-Kutta 2


# Verlet


# Solution analytique
#y_a = 2*np.cos(np.sqrt(prm.k/prm.m)*t)

# Graphiques


plt.show()

# Correction
pytest.main(['-q', '--tb=long', 'oscillateur_corr.py'])
