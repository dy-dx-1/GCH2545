# Importation des modules
import numpy as np
import matplotlib.pyplot as plt
import smith_hutton_corr
import pytest
try:
    from smith_hutton_fct import *
except:
    pass

#------------------------------------------------------------------------------
# Code principal pour l'analyse des résultats
# Il faudra faire appel aux fonctions programmées dans smith_hutton_fct.py afin
# de résoudre le problème de Smith Hutton selon différents nombres de Péclet.
# Ensuite, les solutions devront être affichées sur des figures pour l'analyse.
#------------------------------------------------------------------------------

# Position et solutions de référence
x_p = np.array([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
s_p10 = np.array([ 1.989, 1.402, 1.146, 0.946, 0.775, 0.621, 0.480, 0.349, 0.227, 0.111, 0.000 ])
s_p100 = np.array([ 2.000, 1.940, 1.836, 1.627, 1.288, 0.869, 0.480, 0.209, 0.070, 0.017, 0.000 ])
s_p1000 = np.array([2.000, 2.000, 2.000, 1.985, 1.841, 0.951, 0.154, 0.001, 0.000, 0.000, 0.000])

# Paramètres
X = [-1,1]
Y = [0,1]

nx = 41
ny = 41
N = ny*ny

alpha = 10
Pe = [10,100,1000]

# Résolution
A, b = mdf_assemblage(X,Y,nx,ny,Pe[0],alpha)
c10 = np.linalg.solve(A, b) 
A, b = mdf_assemblage(X,Y,nx,ny,Pe[1],alpha)
c100 = np.linalg.solve(A, b)  
A, b = mdf_assemblage(X,Y,nx,ny,Pe[2],alpha)
c1000 = np.linalg.solve(A, b)   

# Graphiques (utilisez les lignes suivantes pour générer la figure demandée)

# Graphiques de type color maps

c10_reshaped = c10.reshape(nx,ny).transpose()
c100_reshaped = c100.reshape(nx,ny).transpose()
c1000_reshaped = c1000.reshape(nx,ny).transpose()

fig,ax = plt.subplots(nrows=3,ncols=1)
x, y = np.linspace(X[0], X[1], nx), np.linspace(Y[0], Y[1], ny) 

fig1 = ax[0].pcolormesh(x,y, c10_reshaped)
plt.colorbar(fig1, ax=ax[0], label="Concentration")

fig2 = ax[1].pcolormesh(x,y, c100_reshaped)
plt.colorbar(fig2, ax=ax[1], label="Concentration")

fig3 = ax[2].pcolormesh(x,y, c1000_reshaped)
plt.colorbar(fig3, ax=ax[2], label="Concentration")

ax[0].set_title("Profil de concentration adimensionnelle pour $Pe=10$")
ax[1].set_title("Profil de concentration adimensionnelle pour $Pe=100$")
ax[2].set_title("Profil de concentration adimensionnelle pour $Pe=1000$")
ax[0].set_xlabel("Position adimensionnelle en x")
ax[1].set_xlabel("Position adimensionnelle en x")
ax[2].set_xlabel("Position adimensionnelle en x")
ax[0].set_ylabel("Position adimensionnelle en y")
ax[1].set_ylabel("Position adimensionnelle en y")
ax[2].set_ylabel("Position adimensionnelle en y")
plt.subplots_adjust(hspace=0.5)
plt.show()

#Graphique de la concentration à la sortie
# déclarons les concentrations que nous avons trouvé 
c10_out, c100_out, c1000_out = list(), list(), list() 
for k in range(ny, N-ny): # on va chercher les k à la sortie et retirer la concentration
    if k % ny == ny-1:      # comme les k sont en ordre ils vont matcher les x 
        if k > ( ((ny-1)+(N-1))/2 ):
            c10_out.append(c10[k])
            c100_out.append(c100[k])
            c1000_out.append(c1000[k])

x = np.linspace(0, 1, len(c10_out))
fig,ax = plt.subplots(3, 1)
ax[0].plot(x_p, s_p10, 'g*-', label="Référence")
ax[0].plot(x, c10_out, 'r.-', label="MDF")
ax[1].plot(x_p, s_p100, 'g*-', label="Référence")
ax[1].plot(x, c100_out, 'r.-', label="MDF")
ax[2].plot(x_p, s_p1000, 'g*-', label="Référence")
ax[2].plot(x, c1000_out, 'r.-', label="MDF")

ax[0].set_title("Profil de concentration adimensionnelle à $y=0$ pour $Pe=10$")
ax[1].set_title("Profil de concentration adimensionnelle à $y=0$ pour $Pe=100$")
ax[2].set_title("Profil de concentration adimensionnelle à $y=0$ pour $Pe=1000$")
ax[0].set_xlabel("Position adimensionnelle en x")
ax[1].set_xlabel("Position adimensionnelle en x")
ax[2].set_xlabel("Position adimensionnelle en x")
ax[0].set_ylabel("Concentration")
ax[1].set_ylabel("Concentration")
ax[2].set_ylabel("Concentration")
plt.subplots_adjust(hspace=0.5)

ax[0].grid()
ax[1].grid()
ax[2].grid()

ax[0].legend() 
ax[1].legend() 
ax[2].legend() 
plt.show()

#%% Correction
pytest.main(['-q', '--tb=long','--disable-warnings', 'smith_hutton_corr.py'])