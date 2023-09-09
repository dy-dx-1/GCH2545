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


# Affichage en tableau


#%% Calcul de l'erreur commise


# Affichage du graphique


plt.show()

#%% Correction
pytest.main(['-q', '--tb=long', 'tige_corr.py'])
