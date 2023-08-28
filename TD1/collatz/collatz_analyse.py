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
### À remplir

#Graphiques
### À remplir

plt.show()

#Correction
pytest.main(['-q', '--tb=long', 'collatz_corr.py'])