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
    N = None       # [-] Nombre de points en z
prm = parametres()

### Appel des fonctions pour le calcul du profil de température
# Différences finies 
prm.N = 7 # valeur pr comparaison avec analytique
grad, pos = mdf(prm) 
# Analytique 
dom_theorique = np.linspace(0, prm.L) # on utilisera plus de pts pr la solution analytique 
m = np.sqrt((4*prm.h)/(prm.k*prm.D))
grad_theorique = ( (prm.T_w - prm.T_a) * (np.cosh(m*(prm.L-dom_theorique)) / np.cosh(m*prm.L)) ) + prm.T_a 
# Graphique de solution diff finies vs sol analytique 
plt.plot(pos, grad, 'r.-', label=f"Différences finies avec {prm.N} noeuds") 
plt.plot(dom_theorique, grad_theorique, 'g-', label="Solution analytique") 
plt.title("Profil de température d'une ailette")
plt.xlabel("Distance de la base de l'ailette [m]")
plt.ylabel("Température [C]")
plt.legend()
plt.grid() 
plt.show()

### Trouver nb minimum de noeuds pr une erreur raisonnable sur la dissipation (chaleur)
prm.N = 1000 # On calcule la reférence avec 1000 pts 
T_ref, z_ref = mdf(prm) 
q_ref = inte(T_ref, z_ref, prm)  
print(f"Dissipation ref avec 1000 noeuds : {q_ref}")
# Maintenant itérons sur le q obtenu avec différents noeuds afin de trouver celui qui se rapproche bien de q_ref 
erreur = 1 
i = 5 # je commence à 5 parce que j'imagine que ce sera plus que ça 
while erreur>0.01: 
    prm.N = i 
    T_test, z_test = mdf(prm) 
    q_test = inte(T_test, z_test, prm) 
    erreur = abs(q_test-q_ref)/q_ref 
    print(f"q avec {i} noeuds : {q_test} ; pour une err de {erreur*100:.2f} %")
    i+=1 
# dès qu'on sort c'est que le i précédent à apporté une erreur <1% 
i-=1 # on reprend le i qui a mené à cette err 
print("Donc le nombre de noeuds minimum pour avoir une erreur de <1% : ", i) 

###Calcul de la dissipation pour chaque géométrie
# Dissipation de l'ailette en fonction du diamètre 
prm.N = i # on set le nb de noeuds au minimum qu'on a trouvé à dernière question 
L_possibles = [0.005, 0.0075, 0.01, 0.0125, 0.015] 
couleurs_associes = ['r', 'b', 'k', 'g', 'm']    # pour faire un beau graphique avec différentes couleurs 
variation_diam = np.linspace(0.001, 0.02)
# itérons sur tt les L & D possibles & ajoutons les à un graphique 
for i, length in enumerate(L_possibles): 
    prm.L = length 
    q_ref = []
    for diam in variation_diam: 
        prm.D = diam 
        T_ref, z_ref = mdf(prm) 
        q_ref.append(inte(T_ref, z_ref, prm)) # on ajoute la chaleur dissipée pour une certaine long et diam 
    plt.plot(variation_diam, q_ref, f'{couleurs_associes[i]}-',label=f"L: {length} m") 
plt.plot(variation_diam, [10 for _ in range(len(variation_diam))], color="darkorange", linestyle="-", linewidth="1.75", label="q = 10 W") # ajout de la droite à 10W 
plt.legend() 
plt.title("Chaleur dissipée en fonction du diamètre pour différentes longueurs d'ailettes") 
plt.xlabel("Diamètre [m]")
plt.ylabel("Chaleur [W]") 
plt.grid() 
plt.show()     

# Correction
pytest.main(['-q', '--tb=long', 'ailette_corr.py'])