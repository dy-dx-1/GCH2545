# Importation des modules
import numpy as np
import matplotlib.pyplot as plt
import pytest
import time
import conduite_corr
try:
    from conduite_fct import *
except:
    pass

#------------------------------------------------------------------------------
# Code principal pour l'analyse des résultats
# Il faudra faire appel aux fonctions programmées dans conduite_fct.py afin de
# calculer la température dans la conduite selon le rayon et de comparer les
# résultats pour plusieurs matériaux. Des graphiques devront être générés pour
# visualiser les résultats.
#------------------------------------------------------------------------------

# Assignation des paramètres
# ATTENTION! Ne pas changer le nom des attributs, seulement les valeurs
class parametres():
    Tr = 0              # Température à l'intérieur de la conduite
    Te = 0              # Température ambiante autour de la conduite
    k = 0               # [W*m^-1*K^-1] Conductivité thermique
    h = 0               # [W*m^-2*K^-1] Coefficient de convection thermique
    Re = 0              # [m] Rayon externe
    Ri = 0              # [m] Rayon interne
    n = 0               # [-] Nombre de noeuds
    dr = (Re-Ri)/(n-1)  # [-] Pas en espace
prm = parametres()

# Coefficients de conductivité themique
k = [1.3,50,200]

# Méthode de différences finies


# Graphique


plt.show()

# Correction
pytest.main(['-q', '--tb=long', 'conduite_corr.py'])
