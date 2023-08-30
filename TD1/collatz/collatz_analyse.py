# Importation des modules
import matplotlib.pyplot as plt
import numpy as np
import pytest
try:
    from collatz_fct import *
except:
    pass

import collatz_corr

#-----------------------------------------------------------------------------
# Code principal pour l'analyse des résultats des fonctions
# Il faudra appeler la fonction collatz programmée dans collatz_fct.py afin
# de calculer le nombre d'itérations pour les entiers de 1 à 5000 et générer
# 2 graphiques pour la visualisation des résultats.
#-----------------------------------------------------------------------------

# Code principal
## trouver # itérations pour chaque entier 
iterations_collatz = [collatz(num) for num in range(1, 5001)]

#Graphiques
#### QUESTION B 
plt.plot(range(1,5001), iterations_collatz, '.')
plt.grid() 
plt.title("Itérations de la conjecture de Collatz pour les entiers entre 1 et 5000")
plt.xlabel("Nombres entiers") 
plt.ylabel("Nombre d'itérations de la conjecture de Collatz")
plt.show()

#### QUESTION C 
# la méthode hist de matplotlib.pyplot est capable seule de créer un histogramme directement
plt.hist(iterations_collatz) 


##m.thode manuelle 
freq = {}
for iter in iterations_collatz: 
    # on va chercher l'élément clé d'une itération avec freq[iter]
    # on on trouve le sa clé (#itérations)correspondante avec .get
    # si get ne trouve rien il retourne 0 (l'élément n'a pas encore été comptabilisé)
    # on rajoute 1 pour signifier qu'on ajoute une itération 
    freq[iter] = freq.get(iter, 0) + 1 
# Mettons le dictionnaire en ordre croissant de clés maintenant
freq = dict(sorted(freq.items()))
# Maintenant organisons le dict en 2 listes correspondantes 
domaine_hist = []
image_hist = []
for (x,y) in freq.items(): 
    domaine_hist.append(x) 
    image_hist.append(y) 
fig, ax = plt.subplots() 
ax.bar(domaine_hist, image_hist)
plt.show() 
#Correction
pytest.main(['-q', '--tb=long', 'collatz_corr.py'])