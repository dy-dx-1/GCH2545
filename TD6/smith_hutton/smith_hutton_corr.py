import numpy as np
try:
    from smith_hutton_fct import *
except:
    print("ERREUR! Il y a une erreur fatale dans le fichier smith_hutton_fct.py")



class Test:

    def test_positions(self):
        X = [-1,1]
        Y = [0,2]
        nx = 3
        ny = 4
        x,y = position(X,Y,nx,ny)
        assert(np.asarray(x).shape == (ny,nx))
        assert(np.asarray(y).shape == (ny,nx))
        assert(all(abs(np.asarray(x[0,:]) - np.array([-1,0,1])) < 1e-03))
        assert(all(abs(np.asarray(y[:,0]) - np.array([2,1.3333,0.6666,0])) < 1e-03))

    def test_assemblage(self):
        nx = 5
        ny = 5
        X = [-1,1]
        Y = [0,2]

        A,b = mdf_assemblage(X,Y,nx,ny,1,2)
        c = np.array([0.035972,0.035972,0.035972,0.035972,0.035972,
                          0.035972,0.078889,0.217751,0.519088,1.000000,
                          0.035972,0.142702,0.357701,0.823647,1.964028,
                          0.035972,0.156310,0.275657,0.431998,0.484111,
                          0.035972,0.035972,0.035972,0.035972,0.035972])
        c_rep = np.linalg.solve(A,b)

        assert(all(abs(c_rep - c) < 1e-03))