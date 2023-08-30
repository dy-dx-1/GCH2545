# Importation des modules
import matplotlib.pyplot as plt
import numpy as np
import pytest
try:
    from manip_vec_mat_fct import *
except:
    pass

import manip_vec_mat_corr


# Manipulation d'un vecteur
x = faire_vecteur_x()
f = faire_vecteur_f()

# Résolution d'un système linéaire
mat = faire_matrice()
b = faire_second_membre()
sol = np.linalg.solve(mat, b) 
print("Solution du système d'équations: ", sol)

# Affichage du graphique 
plt.plot(x, f, 'g-', label="f(x)") 
plt.title(r"Graphique de la fonction $f(x)=x^2$")
plt.legend()
plt.xlabel("x") 
plt.ylabel("f(x)")
plt.grid() 
plt.show() 

# Correction
pytest.main(['-q', '--tb=long', 'manip_vec_mat_corr.py'])