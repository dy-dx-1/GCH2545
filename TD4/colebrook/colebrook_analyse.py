# Importation des modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import pytest
try:
    from colebrook_fct import *
except:
    pass

#------------------------------------------------------------------------------
# Code principal pour l'analyse des résultats
# Il faudra faire appel aux fonctions programmées dans colebrook_fct.py afin
# de visualiser graphiquement l'intersection de la formule de Colebrook et
# ensuite trouver numériquement la valeur de lambda à l'aide de la bissection.
#------------------------------------------------------------------------------

# Données du problème
class constantes():
    # IMPORTANT: Ne pas changer le nom des variables (attributes) dans la class
    # Seulement les valeurs doivent être changées
    Re = 13743      # Nombre de Reynolds [-]
    k = 3.375/1000       # Rugosité [m]
    D = 30/100       # Diamètre de la conduite [m]

cst = constantes()

#%% Affichage du graphique


plt.show()

#%% Appel de la fonction bissection()


#%% Appel de la fonction scipy (Supprimez les symboles de commentaire après avoir défini f)
#l_scipy = fsolve(f,0.001,args=(cst))
#print("Le coefficient de friction trouvé par scipy est %f" % l_scipy)


# Correction
pytest.main(['-q', '--tb=long', 'colebrook_corr.py'])
