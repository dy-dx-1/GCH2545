import numpy as np

try:
    from tige_fct import *
except:
    print("ERREUR! Il y a une erreur fatale dans le fichier tige_fct.py")

class Test:

    def test_fonc(self):
        assert abs(fonc(np.pi/4) - 0.45307552) < 1e-06
        assert abs(fonc(np.pi/2) - 0.3943859) < 1e-06

    def test_gauss(self):
        rep_int1 = np.empty(5)
        rep_int2 = np.empty(5)

        for i in range(5):
            rep_int1[i] = gauss(np.pi / 6, np.pi / 3, i + 1)
            rep_int2[i] = gauss(np.pi / 3, np.pi / 2, i + 1)

        assert all(abs(np.asarray(rep_int1) - np.array([0.23722979, 0.24074851, 0.24082296, 0.2408248 , 0.24082485])) < 1e-8)
        assert (np.linalg.norm(abs(np.asarray(rep_int1) - np.asarray(rep_int2))) - 0.0720778) < 1e-6
