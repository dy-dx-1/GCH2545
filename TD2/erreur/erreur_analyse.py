# Importation des modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
import pytest
try:
    from erreur_fct import *
except:
    pass

import erreur_corr

#-----------------------------------------------------------------------------
# Code principal pour l'analyse des résultats
# Il faudra faire appel aux fonctions programmées dans erreur_fct.py afin de
# déterminer les dérivées numériques selon des schémas aux ordres différents.
# Un graphique comparant les valeurs des dérivées sera produit, ainsi qu'un
# graphique comparant les erreurs pour chaque schéma.
#-----------------------------------------------------------------------------

# création du domaine 
domaine = []
element = 0.1 # valeurs du domaine allant de x1 à x2 
x2 = np.pi/2
delta = 0.1 
while element<=x2: 
    domaine.append(element)
    element+=0.1 
print(domaine)
#%% Dérivée première, schéma d'ordre 1
image_ordre_1 = [diff_arriere_ordre1(x, delta) for x in domaine] 

#%% Dérivée première, schéma d'ordre 2
image_ordre_2 = [diff_centree_ordre2(x, delta) for x in domaine] 

# Affichage
print("Approx de g'(x=0.5) avec un deltaX de 0.1 et une méthode de premier ordre: g'(x) ≈ ", diff_arriere_ordre1(0.5, delta))
print("Approx de g'(x=0.5) avec un deltaX de 0.1 et une méthode de deuxième ordre: g'(x) ≈ ", diff_centree_ordre2(0.5, delta))

#%% Graphique de g'(x) selon les 2 méthodes
plt.plot(domaine, image_ordre_1, 'g-', label="Approximation d'ordre 1")
plt.plot(domaine, image_ordre_2, 'b-', label="Approximation d'ordre 2")
plt.legend()
plt.grid() 
plt.xlabel("x")
plt.ylabel("Approximation de la dérivée $g'(x)$")
plt.title("Valeur de la dérivée $g'(x)$ pour une approximation d'ordre 1 et 2")
plt.show() 

#%% Analyse de l'erreur
ref = 0.157134840263677 # dérivée exacte de g'(0.5) 
variations_pas = [10**n for n in range(-10, 0, +1)]
erreurs_scipy, erreurs_ordre_1, erreurs_ordre_2 = list(), list(), list() 
for step in variations_pas:                                                 # pas de comprehension de liste pour eviter d'iterer sur variations_pas 3 fois
    erreurs_scipy.append(abs(derivative(g, 0.5, step)-ref))
    erreurs_ordre_1.append(abs(diff_arriere_ordre1(0.5, step)-ref))
    erreurs_ordre_2.append(abs(diff_centree_ordre2(0.5, step)-ref))

#%% Graphique des erreurs
plt.plot(variations_pas, erreurs_scipy, 'r.-', label="Erreur pour la routine de scipy")
plt.plot(variations_pas, erreurs_ordre_1, 'g.-', label="Erreur pour l'approx d'ordre 1")
plt.plot(variations_pas, erreurs_ordre_2, 'b.-', label="Erreur pour l'approx d'ordre 2")
plt.legend()
plt.grid()
plt.xlabel("Taille du pas $\delta x$")
plt.ylabel("Erreur absolue")
plt.title("Erreur entre la différentiation pas arrière, centrée et la fonction scipy.misc.derivative selon la taille du pas") 
plt.yscale("log") 
plt.xscale("log") 
plt.xticks(variations_pas)
plt.show()

#%% Correction
pytest.main(['-q', '--tb=long', 'erreur_corr.py'])
