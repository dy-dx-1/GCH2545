# Importation des modules
import matplotlib.pyplot as plt
import numpy as np
import pytest
try:
    from montecarlo_fct import *
except:
    pass

import montecarlo_corr

#-----------------------------------------------------------------------------
# Code principal pour l'analyse des résultats
# Il faudra appeler les fonctions du fichier montecarlo_fct.py afin de créer
# des points aléatoires pour ensuite calculer l'erreur par rapport à la valeur
# exacte de pi.
# Ensuite, il faudra générer un graphique pour visualiser l'erreur selon
# le nombre de points utilisés. Attention de bien générer un nouvel ensemble
# de points à chaque calcul de pi.
#-----------------------------------------------------------------------------

# Code principal
## Génération de points et calcul de pi

### à remplir

## Calcul de l'erreur et graphique

### à remplir

# Correction
pytest.main(['-q', '--tb=long', 'montecarlo_corr.py'])
