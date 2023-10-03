import numpy as np
try:
    from oscillateur_fct import *
except:
    print("ERREUR! Il y a une erreur fatale dans le fichier oscillateur_fct.py")

class prm1():
    k = 5
    m = 0.06

class prm2():
    k = 9
    m = 0.15

class Test:

    def test_fonc(self):
        f1 = fonc(np.array([5, 2.5]), prm1)
        f1_vrai = np.array([2.5, -416.666666666])
        f2 = fonc(np.array([5,2.5]), prm2)
        f2_vrai = np.array([2.5, -300])
        assert (all(abs(f1 - f1_vrai) < 1e-06))
        assert(all(abs(f2 - f2_vrai) < 1e-06))

    def test_euler_explicite(self):
        dt = 0.01
        tf = 2
        dt2 = 0.05
        tf2 = 1.5
        euler_vrai1 = np.array([8.87730344,66.39350057])
        euler_vrai2 = np.array([-7.91617189,22.26275783])
        ci = np.array([5,2],dtype=float)
        ci2 = np.array([1,5],dtype=float)
        rep_euler = euler_explicite(ci,dt,tf,prm1())
        rep_euler2 = euler_explicite(ci2,dt2,tf2,prm2())

        assert(all(abs(np.asarray(rep_euler[0][-1,:]) - euler_vrai1) < 1e-06) )
        assert(all(abs(np.asarray(rep_euler2[0][-3,:]) - euler_vrai2) < 1e-06))

    def test_rk2(self):
        dt = 0.01
        tf = 2
        dt2 = 0.05
        tf2 = 1.5
        rk2_vrai1 = np.array([4.10748108,26.24201749])
        rk2_vrai2 = np.array([-0.57863134,8.90879396])
        ci = np.array([5,2],dtype=float)
        ci2 = np.array([1,5],dtype=float)
        rep_rk2 = rk2(ci,dt,tf,prm1())
        rep_rk22 = rk2(ci2,dt2,tf2,prm2())

        assert( all(abs(np.asarray(rep_rk2[0][-1,:]) - rk2_vrai1) < 1e-06))
        assert(all(abs(np.asarray(rep_rk22[0][-3,:]) - rk2_vrai2) < 1e-06))

    def test_verlet(self):
        dt = 0.01
        tf = 2
        dt2 = 0.05
        tf2 = 1.5
        verlet_vrai1 = np.array([4.04512057,26.87471826])
        verlet_vrai2 = np.array([-1.04070066,4.49482015])
        ci = np.array([5,2],dtype=float)
        ci2 = np.array([1,5],dtype=float)
        rep_verlet = verlet(ci,dt,tf,prm1())
        rep_verlet2 = verlet(ci2,dt2,tf2,prm2())

        assert(all(abs(np.asarray(rep_verlet[0][-1,:]) - verlet_vrai1) < 1e-06))
        assert(all(abs(np.asarray(rep_verlet2[0][-4,:]) - verlet_vrai2) < 1e-06))

    def test_energie(self):
        x = np.array([2,4,6,8,10,12,14],dtype=float)
        v = np.array([1,2,3,4,5,6,7],dtype=float)
        energie_vrai1 = np.array([10.03,40.12,90.27,160.48,250.75,361.08,491.47])
        energie_vrai2 = np.array([18.075,72.3,162.675,289.2,451.875,650.7,885.675])
        ci = np.array([5,2],dtype=float)
        ci2 = np.array([1,5],dtype=float)
        rep_energie = energie(x,v,prm1())
        rep_energie2 = energie(x,v,prm2())

        assert(all(abs(np.asarray(rep_energie) - energie_vrai1) < 1e-06))
        assert(all(abs(np.asarray(rep_energie2) - energie_vrai2) < 1e-06))
