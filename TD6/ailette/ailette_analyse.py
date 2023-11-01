# Importation des modules
import numpy as np
import matplotlib.pyplot as plt
import pytest
import ailette_corr
try:
    from ailette_fct import *
except:
    pass

#------------------------------------------------------------------------------
# Code principal pour l'analyse des résultats
# Il faudra faire appel aux fonctions programmées dans ailette_fct.py afin de
# modéliser les pertes de chaleurs selon différentes combinaisons géométriques.
# Ensuite, il faudra identifier le meilleur rendement.
#------------------------------------------------------------------------------

# Assignation des paramètres
# ATTENTION! Ne pas changer le nom des attributs
class parametres():
    L = 0       # [m] Longueur
    D = 0       # [m] Diamètre
    k = 0       # [W/m*K] Conductivité thermique
    T_a = 0     # [K] Température de l'air ambiant
    T_w = 0     # [K] Température de la paroi
    h = 0       # [W/m^2*K] Coefficient de convection
    N = 0       # [-] Nombre de points en z

prm = parametres()

# Appel des fonctions pour le calcul du profil de température


# Graphique


#plt.show()

# Calcul de la dissipation pour chaque géométrie



# Graphique


# Correction
pytest.main(['-q', '--tb=long', 'ailette_corr.py'])
