# Importation des modules
import numpy as np
import matplotlib.pyplot as plt
import pytest
import lorenz_corr
try:
    from lorenz_fct import *
except:
    pass

#------------------------------------------------------------------------------
# Code principal pour l'analyse des résultats
# Il faudra faire appel aux fonctions programmées dans lorenz_fct.py afin de
# générer les graphiques représentant un attracteur de Lorenz selon deux
# ensembles de conditions initiales et de les comparer.
#------------------------------------------------------------------------------

# Assignation des paramètres
# ATTENTION! Ne pas changer le nom des attributs
class parametres():
    o = 10      # sigma
    b = 8/3     # beta
    p = 28      # rho
prm = parametres()

# Conditions initiales
cond_i = np.array([10, 10, 20])
t_sim = 30 # temps simulation en s 
dt = 10e-3 # pas de temps en s 

# Appel de la fonction rk4
sols, temps = rk4(cond_i, dt, t_sim, prm) 
x_vals = sols[:,0]
y_vals = sols[:,1]
z_vals = sols[:,2]

# Graphiques
ax1 = plt.figure().add_subplot(projection='3d') 
ax2 =plt.figure().add_subplot(projection='3d') 

ax1.plot(x_vals, y_vals, z_vals, 'r') 
ax1.set_title("Attracteur de Lorenz avec [$x_0$, $y_0$, $z_0$] = [10, 10, 20]")
ax1.set_xlabel("x");ax1.set_ylabel("y");ax1.set_zlabel("z")
ax1.grid() 
# génération du graphique avec condi légèrement perturbées 
sols, temps = rk4(cond_i+10e-4, dt, t_sim, prm) 
x_vals, y_vals, z_vals = sols[:,0], sols[:,1], sols[:,2] 
ax2.plot(x_vals, y_vals, z_vals, 'y-')
ax2.set_title("Attracteur de Lorenz avec les mêmes conditions initiales perturbées de $10^{-4}$")
ax2.set_xlabel("x");ax2.set_ylabel("y");ax2.set_zlabel("z")
ax2.grid() 

plt.show()
# Correction
pytest.main(['-q', '--tb=long', 'lorenz_corr.py'])