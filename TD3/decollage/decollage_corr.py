import numpy as np
try:
    from decollage_fct import *
except:
    print("ERREUR! Il y a une erreur fatale dans le fichier decollage_fct.py")

class constantes():
    rho = 1
    S = 2
    C = 3
    m = 4

class vectors():
    v1 = np.array([0, 2, 4, 5, 6, 10])
    v2 = np.array([0, 1, 3, 7, 15, 18, 20])

    t1 = np.linspace(0, (len(v1) - 1) * 2, len(v1))
    t2 = np.linspace(0, (len(v2) - 1) * 3, len(v2))

    a1 = np.array([1, 1, 0.75, 0.5, 1.25, 2.75])
    a2 = np.array([0.166667, 0.5, 1., 2., 1.83333, 0.83333, 0.5])

    force1 = np.array([4, 16, 51, 77, 113, 311])
    force2 = np.array([0.66666, 5., 31., 155., 682.3333, 975.3333, 1202.])

    pos1 = np.array([0, 2, 8, 17, 28, 44])
    pos2 = np.array([0., 1.5, 7.5, 22.5, 55.5, 105., 162.])

cst = constantes()
vec = vectors()

class Test:

    def test_acc(self):
        assert all(abs(acc(vec.v1, 2) - vec.a1) < 1e-04)
        assert all(abs(acc(vec.v2, 3) - vec.a2) < 1e-04)

    def test_force_poussee(self):
        assert all(abs(force_poussee(vec.v1, vec.a1, cst) - vec.force1) < 1e-01)
        assert all(abs(force_poussee(vec.v2, vec.a2, cst) - vec.force2) < 1e-01)

    def test_trapeze(self):
        assert abs(trapeze(vec.t1, vec.v1) - vec.pos1[-1]) < 1e-02
        assert abs(trapeze(vec.t2, vec.v2) - vec.pos2[-1]) < 1e-02
        
    def test_simpson(self):
        assert abs(simpson(vec.t2, vec.v2) - 160.0) < 1e-02
