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
## liste contenant le # itérations pour chaque entier 
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
# Création d'un dict vide qui contiendra comme clés chaque #d'itérations 
# et comme valeurs associée, leur fréquence 
freq = {}
for iter in iterations_collatz: 
    # on va chercher l'élément clé d'une itération avec freq[iter]
    # on on trouve sa clé (nb d'itérations) correspondante avec .get
    # si get ne trouve rien il retourne 0 (l'élément n'a pas encore été comptabilisé dans le dict)
    # ensuite, on rajoute 1 à la valeur retournée (ou 0) pour signifier qu'on ajoute une itération 
    freq[iter] = freq.get(iter, 0) + 1 
# Mettons le dictionnaire en ordre croissant de clés maintenant
freq = dict(sorted(freq.items()))
# Maintenant organisons le dict en 1 array contenant les itérations et leur fréquence
results = np.array(list(freq.items())) 
# créons le graphique 
fig, ax = plt.subplots() 
ax.bar(results[:,0], results[:,1])
plt.title("Nombre d'itérations obtenus en applicant la conjecture de Collatz sur des entiers de 1 à 5000 et leur fréquence")
plt.xlabel("Nombre d'itérations") 
plt.ylabel("Fréquence pour des entiers entre 1 et 5000")
plt.show() 
#Correction
pytest.main(['-q', '--tb=long', 'collatz_corr.py'])