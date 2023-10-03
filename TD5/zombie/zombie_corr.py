import numpy as np
try:
    from zombie_fct import *
except:
    print("ERREUR! Il y a une erreur fatale dans le fichier zombie_fct.py")

class parametres():
    e = 5
    b = 8
    a = 9
    d = 4
    p = 7


class Test:
        
    def test_residu(self):
        y = np.array([5.,6.,7.])
        yi = np.array([2.,3.,4.])
        dt = 0.001
        rep_residu = residu(y,yi,parametres(),dt)
        residu_vrai = np.array([-3.253,-2.995,-2.745])
        assert(all(abs(np.asarray(rep_residu) - residu_vrai) < 1e-06))

    def test_jacobienne(self):
        y = np.array([5.,6.,7.])
        yi = np.array([2.,3.,4.])
        dt = 0.001
        rep_residu = residu(y,yi,parametres(),dt)
        rep_jacobien=jacobien(y, parametres(), dt)
        jacobien_vrai = np.array([-2.97899536,-2.97742183,-3.03658279])
        assert(all(abs(-np.linalg.solve(rep_jacobien,rep_residu) - jacobien_vrai) < 1e-08))

    def test_euler_implicite(self):
        dt = 0.5
        tf = 5
        yi = np.array([2.,3.,4.])
        tol = 1e-07
        rep_euler = euler_implicite(yi,dt,tf,tol,parametres())
        assert(len(rep_euler[0])==len(rep_euler[1]))
        assert(all(abs(rep_euler[0][10,:] - np.array([0.02040408,42.40580673,1.57378917])) < 1e-06))
