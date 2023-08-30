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
# Calcul des sommes pour des entiers de 50 à 1000
domain = range(50, 1001)
image_harm = [serie_harmonique(i) for i in domain]
plt.plot(domain, image_harm, '.-')
plt.xlabel("Limite des itérations de la série harmonique")
plt.ylabel("Résultat de la somme")
plt.title("Valeurs données par la série harmonique en N itérations de 50 à 1000")
plt.grid() 
plt.show() 
# Factoriel



# Correction
pytest.main(['-q', '--tb=long', 'algorithmie_corr.py'])