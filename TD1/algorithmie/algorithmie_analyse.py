# Importation des modules
import matplotlib.pyplot as plt
import numpy as np
import pytest
try:
    from algorithmie_fct import *
except:
    pass

import algorithmie_corr


# Série harmonique
domain = range(50, 1001)
image_harm = [serie_harmonique(i) for i in domain] # Calcul des sommes pour des entiers de 50 à 1000
plt.plot(domain, image_harm, '-', label="S(N)")
plt.legend()
plt.xlabel("Nombre d'itérations")
plt.ylabel("Résultat de la somme S(N)")
plt.title("Somme donnée par la série harmonique avec des itérations N allant de 50 à 1000")
plt.xticks(np.arange(50, 1001, 190))
plt.grid() 
plt.show() 

# Factoriel
print("***Différence (erreur absolue) entre fonction écrite et fonction factorial de numpy***")
print("Erreur pour 5! :", abs(factoriel(5)-np.math.factorial(5)))
print("Erreur pour 48! :", abs(factoriel(48)-np.math.factorial(48)))
print("Erreur pour 87! :", abs(factoriel(87)-np.math.factorial(87)))

# Correction
pytest.main(['-q', '--tb=long', 'algorithmie_corr.py'])