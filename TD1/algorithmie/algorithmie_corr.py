import numpy as np
try:
    from algorithmie_fct import *
except:
    print("ERREUR! Il y a une erreur fatale dans le fichier algorithmie_fct.py")


class Test:

    def test_serie_harmonique(self):
        assert np.abs(serie_harmonique(3) - (1+0.5+1/3)) < 1e-12

    def test_factoriel(self):
        assert np.abs(factoriel(50) - np.math.factorial(50)) < 1e-14