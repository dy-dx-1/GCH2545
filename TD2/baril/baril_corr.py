import numpy as np
try:
    from baril_fct import *
except:
    print("ERREUR! Il y a une erreur fatale dans le fichier baril_fct.py")

class Test:

    def test_diff1(self):
        err_diff11 = abs(diff1(np.array([5, 4, 2]), 3) - np.array([-0.1666666, -0.5000000, -0.8333333]))
        assert all(err_diff11 < 1e-06)
        err_diff12 = abs(diff1(np.array([3, 7, 9, 10]), 5) - np.array([1, 0.6, 0.3, 0.1]))
        assert all(err_diff12 < 1e-06)

    def test_diff2(self):
        err_diff21 = abs(diff2(np.array([0, 1.3, 3.9, 4.1, 6.5]), 1)[0:5:2] - np.array([1.3, -2.4, 2.2]))
        assert all(err_diff21 < 1e-06)
        err_diff22 = abs(diff2(np.array([64, 49, 36, 25, 16, 9, 4, 1]), 9) - 0.02469136)
        assert all(err_diff22 < 1e-06)
