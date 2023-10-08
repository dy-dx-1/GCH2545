# Importation des modules
import numpy as np
import matplotlib.pyplot as plt
import pytest
import zombie_corr
try:
    from zombie_fct import *
except:
    pass

#------------------------------------------------------------------------------
# Code principal pour l'analyse des résultats
# Il faudra faire appel aux fonctions programmées dans zombie_fct.py afin d'évaluer
# l'évolution des populations humaines et zombies à travers les années suivant
# une invasion de zombies. Un graphique sera généré afin de visualiser cette
# évolution temporelle.
#------------------------------------------------------------------------------

# Assignation des paramètres
# Attention! Ne pas changer le nom des attributs
class parametres():
    e = 0.0001           # Taux de résurrection en zombie (zeta)
    b = 0.0095           # Taux de transformation en zombie (beta)
    a = 0.005            # Taux de mort de zombie (alpha)
    d = 0.0001           # Taux de mort naturelle (delta)
    p = 0.0001           # Taux de naissance (pi)
prm = parametres()

# Résolution des EDO
# Conditions initiales
ci = np.array([500.,0.,0.])
dt = 0.1   # prenons un pas de temps de 6 mois 
tf = 20    # on simule pendant 20 ans 
tol = 1e-06 # tol machine 

# Euler implicite
solutions, temps = euler_implicite(ci, dt, tf, tol, prm)

# Graphique
plt.plot(temps, solutions[:,0], 'g-', label="S(t): Nombre d'humains")  
plt.plot(temps, solutions[:,1], 'r-', label="Z(t): Nombre de zombies") 
plt.plot(temps, solutions[:,2], 'k-', label="R(t): Nombre de morts") 

plt.title("Dynamique d'une invasion de zombies sur une période de 20 ans") 
plt.xlabel("Temps en années") 
plt.ylabel("Nombre d'individus") 
plt.legend() 
plt.grid() 
plt.show()

# Correction
pytest.main(['-q', '--tb=long', 'zombie_corr.py'])