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
    L = 0.1       # [m] Longueur
    D = 0.0025       # [m] Diamètre
    k = 45       # [W/m*K] Conductivité thermique
    T_a = 25     # [K] Température de l'air ambiant
    T_w = 125     # [K] Température de la paroi
    h = 150       # [W/m^2*K] Coefficient de convection
    N = 5       # [-] Nombre de points en z

prm = parametres()

# Appel des fonctions pour le calcul du profil de température
# Différences finies 
grad, pos = mdf(prm) 
# Analytique 
# on utilisera le même nombre de pts pour la solution analytique donc on peut juste reprendre le domaine de mdf 
m = np.sqrt((4*prm.h)/(prm.k*prm.D))
grad_theorique = ( (prm.T_w - prm.T_a) * (np.cosh(m*(prm.L-pos)) / np.cosh(m*prm.L)) ) + prm.T_a 

# Graphique
plt.plot(pos, grad, 'r.-', label="Différences finies") 
plt.plot(pos, grad_theorique, 'g.-', label="Solution analytique") 
plt.title("Profil de température d'une ailette")
plt.xlabel("Distance de la base de l'ailette [m]")
plt.ylabel("Température [C]")
plt.legend()
plt.grid() 
plt.show()

# Calcul de la dissipation pour chaque géométrie



# Graphique


# Correction
pytest.main(['-q', '--tb=long', 'ailette_corr.py'])
