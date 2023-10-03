# Importation des modules
import numpy as np
import matplotlib.pyplot as plt
import pytest
import zombie_corr
try:
    from zombie_fct import *
except:
    pass

#------------------------------------------------------------------------------
# Code principal pour l'analyse des résultats
# Il faudra faire appel aux fonctions programmées dans zombie_fct.py afin d'évaluer
# l'évolution des populations humaines et zombies à travers les années suivant
# une invasion de zombies. Un graphique sera généré afin de visualiser cette
# évolution temporelle.
#------------------------------------------------------------------------------

# Assignation des paramètres
# Attention! Ne pas changer le nom des attributs
class parametres():
    e = 0           # Taux de résurrection en zombie (zeta)
    b = 0           # Taux de transformation en zombie (beta)
    a = 0           # Taux de mort de zombie (alpha)
    d = 0           # Taux de mort naturelle (delta)
    p = 0           # Taux de naissance (pi)
prm = parametres()

# Résolution des EDO
# Conditions initiales
ci = np.array([500.,0.,0.])

# Euler implicite


# Graphique


plt.show()

# Correction
pytest.main(['-q', '--tb=long', 'zombie_corr.py'])
