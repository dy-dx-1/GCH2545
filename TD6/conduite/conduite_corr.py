import numpy as np
try:
    from conduite_fct import *
except:
    print("ERREUR! Il y a une erreur fatale dans le fichier conduite_fct.py")

class parametres():
    Tr = 350
    Te = 280
    h = 15
    Re = 8
    Ri = 4
    n = 81
    dr = (Re-Ri)/(n-1)
    k = 2

class Test:

    def test_mdf(self):
        prm = parametres()

        prm2=parametres()
        prm2.k=55
    
        prm3=parametres()
        prm3.k=190
    
    
        r,T1=mdf(prm)
        r,T2=mdf(prm2)
        r,T3=mdf(prm3)
    
        assert (len(T1)==81)
    
    
        assert (abs(T1[6] - 342.86795642) < 1e-4)
        assert (abs(T2[6] - 345.60351553) < 1e-4)
        assert (abs(T3[6] - 347.77617237) < 1e-4)
    
        assert (abs(T1[9] - 339.48646816) < 1e-4)
        assert (abs(T2[9] - 343.51902735) < 1e-4)
