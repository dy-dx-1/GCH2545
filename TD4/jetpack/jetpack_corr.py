import numpy as np
try:
    from jetpack_fct import *
except:
    print("ERREUR! Il y a une erreur fatale dans le fichier jetpack_fct.py")

class parametres():
    g = 11
    rho = 1200
    D_e = 0.3
    D_s = 0.1
    m = 56
    F = 250
    
class Test:
    
    def test_residu(self):
        prm1 = parametres()
        rep_residu1 = residu([2,3,0.6],prm1)
        rep_residu2 = residu([4,5,0.3],prm1) 

        assert (all(abs(np.asarray(rep_residu1) - np.array([-136.6931,154.2106,-0.0942])) < 1e-04))
        assert (all(abs(np.asarray(rep_residu2) - np.array([1191.3597,110.7393,-0.2042])) < 1e-04))
    
    def test_newton(self):
        prm1 = parametres()
        prm2 = parametres()
        prm2.g = 3
        prm2.rho = 900
        prm2.D_e = 0.2
        prm2.D_s = 0.1
        prm2.m = 65
        prm2.F = 500
        rep_residu1 = residu([2,3,0.6],prm1)
        rep_residu2 = residu([4,5,0.3],prm1) 

        rep_newtonn1 = np.asarray(newton_numerique(np.array([2,10,np.pi/4]),1e-06,prm1))
        rep_newtonn2 = np.asarray(newton_numerique(np.array([2,10,np.pi/4]),1e-06,prm2))

        assert(all(abs(rep_newtonn1 - np.array([1.2035, 5.4158, 0.4691])) < 1e-02))
        assert(all(abs(rep_newtonn2 - np.array([2.9830195,5.966039,1.68350954])) < 1e-02))