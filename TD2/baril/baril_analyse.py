# Importation des modules
import numpy as np
import pytest
try:
    from baril_fct import *
except:
    pass

import baril_corr

#-----------------------------------------------------------------------------
# Code principal de l'analyse des résultats
# Il faudra faire appel aux fonctions programmées afin de trouver les dérivées
# premières et secondes et les comparer aux valeur théoriques.
# La class constantes() doit être remplie avec les valeurs de l'énoncé. Les
# noms des variables dans la class ne doivent pas être changé.
#-----------------------------------------------------------------------------

class constantes():
    rc = 2/2      # rayon du cylindre
    rv = 20/200      # rayon de la vanne
    gamma = 0.6   # Coefficient de correction
    g = 9.81       # accélération gravitationnelle


#%% Mesures expérimentales
domaine = np.array([0,5,10,15,20])
hauteur = np.array([0.6350, 0.5336, 0.4410, 0.3572, 0.2822])
delta = 5

#%% Appel de la fonction diff1
vitesses_approx = diff1(hauteur, delta)

# Affichage du tableau


#%% Appel de la fonction diff2
accel_approx = diff2(hauteur, delta) 

# Affichage du tableau


#%% Calcul de la vitesse théorique
vitesses_theo = vitesse(hauteur, constantes) 

# Affichage du tableau


#%% Calcul de l'accélération théorique
accel_theo = acceleration(constantes) 

#%% Erreur commise sur la vitesse


# Affichage du tableau


#%% Erreur commise sur l'accélération


# Affichage du tableau


#%% Correction
pytest.main(['-q', '--tb=long', 'baril_corr.py'])
