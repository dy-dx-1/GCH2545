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