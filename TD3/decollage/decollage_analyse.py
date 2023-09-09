# Importation des modules
import numpy as np
import pytest
try:
    from decollage_fct import *
except:
    pass

#-----------------------------------------------------------------------------
# Code principale pour l'analyse des résultats
# Il faudra faire appel aux fonctions programmées dans le fichier decollage_fct.py
# afin de calculer l'accélération de l'avion, la force de poussée développée
# et finalement le travail fourni par les moteurs.
#-----------------------------------------------------------------------------

#%% Données du problème
class constantes():
    rho = 0         # Densité de l'air [kg/m^3]
    S = 0           # Surface de référence [m^2]
    C = 0           # Coefficient de friction [-]
    m = 0           # Masse de l'avion [kg]

t = np.array([0,1,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]) # Temps [s]
v = np.array([0,4,17,33,50,67,83,100,117,133,150,167,183,200,217,233,250]) # Vitesse [km/h]



#%% Accélération en fonction du temps


#%% Force de poussée de l'avion


#%% Travail fourni par les moteurs


# Affichage (optionnel)
# print("Les moteurs doivent fournir un travail de %.2f MJ." % (???))

#%% Correction
pytest.main(['-q', '--tb=long', 'decollage_corr.py'])
