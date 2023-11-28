import numpy as np 
import fonctions as f 

class Test:

    def test_maillage(self): 
        coord_r = [[0, 1, 2, 3], 
                   [0, 1, 2, 3], 
                   [0, 1, 2, 3]] 
        coord_theta = [[10, 10, 10, 10], 
                       [5, 5, 5, 5], 
                       [0, 0, 0, 0]] 
        r_test, theta_test = f.gen_maille(r_min = 0, r_max = 3, theta_min = 0, theta_max = 10, nx = 4, ny = 3)
        r_check = abs(r_test-coord_r)<1e-3
        theta_check = abs(theta_test-coord_theta)<1e-3
        assert all([r_check.all(), theta_check.all()])

    def test_convert_indices(self): 
        # prenons les points suivants, format (i, j, k), nx = 4
        p1 = (2, 0, 2) 
        p2 = (1, 1, 5) 
        p3 = (3, 2, 11) 

        # test de i 
        assert abs(p1[0]-f.convert_indices(nx=4, i=None, j=p1[1], k=p1[2]))<1e-6
        # test de j 
        assert abs(p2[1]-f.convert_indices(nx=4, i=p2[0], j=None, k=p2[2]))<1e-6
        # test de k 
        assert abs(p3[2]-f.convert_indices(nx=4, i=p3[0], j=p3[1], k=None))<1e-6
        # test d'erreur 
        assert (f.convert_indices(nx=4, i=1, j=2, k=3) is None)

    def test_central_shape(self): 
        maille_test1 = f.gen_central_values(k=9, nx=4, ny=4, rk=1, dr=1, dtheta=1)
        maille_test2 = f.gen_central_values(k=14, nx=4, ny=6, rk=1, dr=1, dtheta=1)
        maille_test3 = f.gen_central_values(k=8, nx=6, ny=3, rk=1, dr=1, dtheta=1) 
        # Verif que toutes les colonnes des bords sont nulles 
        assert all([ (maille_test1[0] == 0).all(),
                     (maille_test1[-1] == 0).all(),
                     (maille_test1[:,0] == 0).all(),
                     (maille_test1[:,1] == 0).all() ]) 
        assert all([ (maille_test2[0] == 0).all(),
                     (maille_test2[-1] == 0).all(),
                     (maille_test2[:,0] == 0).all(),
                     (maille_test2[:,1] == 0).all() ]) 
        assert all([ (maille_test3[0] == 0).all(),
                     (maille_test3[-1] == 0).all(),
                     (maille_test3[:,0] == 0).all(),
                     (maille_test3[:,1] == 0).all() ]) 
        
    def test_integral(self): 
        """ 
        Test de la fonction d'integration. On vérifie qu'elle est capable d'intégrer avec 2 fonctions 
        dont la solution analytique est simple à obtenir. 
        """
        dom = np.linspace(-5, 5, 10000)  # domaine subdivisé en 50 pts donc 49 sous intervalles 
        y1 = np.sin(dom) 
        y2 = np.cos(dom)  

        check1 = abs(f.integrale(dom, y1)-0)<1e-2
        check2 = abs(f.integrale(dom, y2)-(2*np.sin(5)))<1e-2 
        
        assert all([check1, check2])

    def test_derivee(self): 
        # TODO: not working 
        x = np.array([0, 1, 2, 3, 4, 5]) 
        y = x**3 # valeurs tests, la derivee analytique est 3x**2 
        y_prime = 3*(x**2)
        y_p_approx = f.derive(y, 0.01)
        
        assert all(abs(y_prime-y_p_approx)<1e-3) 