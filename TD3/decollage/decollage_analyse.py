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
    rho = 1.341       # Densité de l'air [kg/m^3]
    S = 580           # Surface de référence [m^2]
    C = 0.027         # Coefficient de friction [-]
    m = 250000            # Masse de l'avion [kg] ## assumant 1ton = 1000kg

t = np.array([0,1,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]) # Temps [s]
v = np.array([0,4,17,33,50,67,83,100,117,133,150,167,183,200,217,233,250]) # Vitesse [km/h]
v_std = v/3.6   # Vitesses en m/s pour utiliser dans les calculs 

#%% Accélération en fonction du temps [m/s**2] 
accels = acc(v_std, 2) #TODO: Confirm: dt variable dans tableau de données, mais fonction demande un dt fixe. Tests sont tous réussis donc qu,elle valeur utiliser ? 

#%% Force de poussée de l'avion
forces_poussee = force_poussee(v_std, accels, constantes())

#%% Travail fourni par les moteurs

# intégrale avec méthode des trapèzes, résultat converti en MJ 
W_trap = trapeze(t, forces_poussee*v_std) / (10**6) 
# intégrale avec méthode de Simpson 1/3, résultat converti en MJ 
W_simp = simpson(t, forces_poussee*v_std) / (10**6) 

# Affichage (optionnel)
print("Les moteurs doivent fournir un travail de %.2f MJ selon la méthode du trapèze" % (W_trap))
print("Les moteurs doivent fournir un travail de %.2f MJ selon la méthode de Simpson 1/3" % (W_simp))

#%% Correction
pytest.main(['-q', '--tb=long', 'decollage_corr.py'])
