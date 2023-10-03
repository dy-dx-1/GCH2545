import numpy as np
try:
    from lorenz_fct import *
except:
    print("ERREUR! Il y a une erreur fatale dans le fichier lorenz_fct.py")


class prm1():
    o = 10
    b = 9
    p = 8


class prm2():
    o = 1
    b = 2
    p = 3

class prm3():
    o = 5
    b = 6
    p = 7

class Test:

    def test_fonc(self):
        rep_fonc1 = fonc(np.array([1,2,3]),prm1())
        rep_fonc2 = fonc(np.array([3,4,5]),prm2())
        
        fonc_vrai1 = np.array([10,3,-25])
        fonc_vrai2 = np.array([1.,-10.,2.])

        assert(all(abs(np.asarray(rep_fonc1) - fonc_vrai1) < 1e-06))
        assert(all(abs(np.asarray(rep_fonc2) - fonc_vrai2) < 1e-06))

    def test_rk4(self):

        rep_rk41 = rk4(np.array([9.,5.,3.]),0.001,0.004,prm1())
        rep_rk43 = rk4(np.array([1.,2.,3.]),0.0001,0.0003,prm3())

        y1 = np.array([[9.        , 5.        , 3.        ],
                    [8.960398  , 5.03979997, 3.01799854],
                    [8.92158409, 5.07920376, 3.03599237],
                    [8.88354651, 5.11821709, 3.05397893],
                    [8.84627367, 5.15684561, 3.07195581]])

        y3 = np.array([[1.        , 2.        , 3.        ],
                       [1.00049993, 2.00020017, 2.99840054],
                       [1.0009997 , 2.00040068, 2.99680216],
                       [1.00149933, 2.00060153, 2.99520486]])

        assert((abs(y1 - rep_rk41[0]) < 1e-06).all())
        assert((abs(y3 - rep_rk43[0]) < 1e-06).all())