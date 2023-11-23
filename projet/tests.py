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
        r_check = (r_test-coord_r)<1e-3
        theta_check = (theta_test-coord_theta)<1e-3
        assert all([r_check.all(), theta_check.all()])

        