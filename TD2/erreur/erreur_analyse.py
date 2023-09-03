# Importation des modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
import pytest
try:
    from erreur_fct import *
except:
    pass

import erreur_corr

#-----------------------------------------------------------------------------
# Code principal pour l'analyse des résultats
# Il faudra faire appel aux fonctions programmées dans erreur_fct.py afin de
# déterminer les dérivées numériques selon des schémas aux ordres différents.
# Un graphique comparant les valeurs des dérivées sera produit, ainsi qu'un
# graphique comparant les erreurs pour chaque schéma.
#-----------------------------------------------------------------------------

#%% Dérivée première, schéma d'ordre 1


# Affichage


#%% Dérivée première, schéma d'ordre 2


# Affichage


#%% Graphique de g'(x) selon les 2 méthodes


#%% Analyse de l'erreur


#%% Graphique des erreurs


plt.show()

#%% Correction
pytest.main(['-q', '--tb=long', 'erreur_corr.py'])
