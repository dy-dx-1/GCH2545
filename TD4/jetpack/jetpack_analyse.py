# Importation des modules
import numpy as np
import pytest
import jetpack_corr
try:
    from jetpack_fct import *
except:
    pass

#------------------------------------------------------------------------------
# Code principal pour l'analyse des résultats
# Il faudra faire appel aux fonctions programmées dans jetpack_fct.py afin
# de calculer les vitesses d'entrée et de sorties de l'eau ainsi que l'angle
# d'inclinaison afin d'obtenir l'équilibre désiré.
#------------------------------------------------------------------------------

# Données du problème
class parametres():
    g = 9.81       # Accélération gravitationnelle [m/s^2]
    rho = 1000     # Masse volumique [kg/m^3]
    D_e = 20/100     # Diamètre du boyau [m]
    D_s = 5/100     # Diamètre des propulseurs [m]
    m = 70       # Masse [kg]
    F = 200       # Force du vent [N]
prm = parametres()

# Appel de la fonction
estime = [1.1,8.5,np.pi/4] # logique derriere les estimés expliquée sur moodle 
tol = 1e-06 
reponses = newton_numerique(estime, tol, prm)

print(f"Résultats des calculs: \nVitesse entrante: {reponses[0]}[m/s]\nVitesse sortante: {reponses[1]}[m/s]\nAngle d'inclinaison: {reponses[2]} [rad]")
# Correction
pytest.main(['-q', '--tb=long', 'jetpack_corr.py'])