# Importation des modules
import numpy as np
import matplotlib.pyplot as plt
import pytest
import oscillateur_corr
try:
    from oscillateur_fct import *
except:
    pass

#------------------------------------------------------------------------------
# Code principal pour l'analyse des résultats
# Il faudra faire appel aux fonctions programmées dans oscillateur_fct.py afin
# d'évaluer la solution d'un système d'équations différentielles ordinaires
# avec différentes méthodes numériques et comparer les résultats
# graphiquement.
#------------------------------------------------------------------------------

# Assignation des paramètres et conditions initiales
# ATTENTION! Ne pas changer le nom des attributs
class parametres():
    k = 2       # Constante de rappel du ressort [N/m]
    m = 50/1000       # Masse accroché au ressort [kg] 
prm = parametres()

cond_init = [2, 0] 
pas = 0.01 
tf = 3
# Euler explicite
euler, t = euler_explicite(cond_init, pas, tf, prm) 
x_e, v_e = euler[:,0], euler[:,1]
# Runge-Kutta 2
rk, t = rk2(cond_init, pas, tf, prm) 
x_r, v_r = rk[:,0], rk[:,1]
# Verlet
verl, t = verlet(cond_init, pas, tf, prm) 
x_v, v_v = verl[:,0], verl[:,1]
# Solution analytique
y_a = 2*np.cos(np.sqrt(prm.k/prm.m)*t) 
# Energies 
e_e = energie(x_e, v_e, prm) 
e_r = energie(x_r, v_r, prm) 
e_v = energie(x_v, v_v, prm) 
# Graphiques
fig, axs = plt.subplots(2,3) # on veut 6 graphiques 
ax_e, ax_r, ax_v, ax_e_e, ax_r_e, ax_v_e = axs[0,0], axs[0,1], axs[0,2], axs[1,0], axs[1,1], axs[1,2]
# Euler 
ax_e.plot(t, x_e, 'r-', label="Euler explicite", linewidth="2.5")  # pos 
ax_e.plot(t, y_a, 'k3', label="Solution analytique", markersize="6") # analytique
ax_e_e.plot(t, e_e, 'g-', label="Énergie") # energie 

ax_e.set_title("Position en fonction du temps avec Euler explicite") 
ax_e.set_xlabel("Temps (s)") 
ax_e.set_ylabel("Position (m)")

ax_e_e.set_title("Énergie en fonction du temps avec Euler explicite")
ax_e_e.set_xlabel("Temps (s)") 
ax_e_e.set_ylabel("Énergie totale du systeme (J)")
# RK2 
ax_r.plot(t, x_r, 'r-', label="RK2", linewidth="2.5")  # pos 
ax_r.plot(t, y_a, 'k3', label="Solution analytique", markersize="6") # analytique
ax_r_e.plot(t, e_r, 'g-', label="Énergie") # energie 

ax_r.set_title("Position en fonction du temps avec RK2") 
ax_r.set_xlabel("Temps (s)") 
ax_r.set_ylabel("Position (m)")

ax_r_e.set_title("Énergie en fonction du temps avec RK2")
ax_r_e.set_xlabel("Temps (s)") 
ax_r_e.set_ylabel("Énergie totale du systeme (J)")
# Verlet 
ax_v.plot(t, x_v, 'r-', label="Verlet", linewidth="2.5")  # pos 
ax_v.plot(t, y_a, 'k3', label="Solution analytique", markersize="6") # analytique
ax_v_e.plot(t, e_v, 'g-', label="Énergie") # energie 

ax_v.set_title("Position en fonction du temps avec Verlet") 
ax_v.set_xlabel("Temps (s)") 
ax_v.set_ylabel("Position (m)")

ax_v_e.set_title("Énergie en fonction du temps avec Verlet")
ax_v_e.set_xlabel("Temps (s)") 
ax_v_e.set_ylabel("Énergie totale du systeme (J)")

ax_e.grid() 
ax_e_e.grid() 
ax_r.grid()
ax_r_e.grid() 
ax_v.grid() 
ax_v_e.grid() 
ax_e.legend(loc = "upper right") 
ax_e_e.legend(loc = "upper right") 
ax_r.legend(loc = "upper right")
ax_r_e.legend(loc = "upper right") 
ax_v.legend(loc = "upper right") 
ax_v_e.legend(loc = "upper right") 
plt.show()
# Correction
pytest.main(['-q', '--tb=long', 'oscillateur_corr.py'])