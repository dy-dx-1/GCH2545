import numpy as np
try:
    from collatz_fct import *
except:
    print("ERREUR! Il y a une erreur fatale dans le fichier collatz_fct.py")

class Test:

    def test_collatz(self):
        rep_collatz = np.array([collatz(7), collatz(5003)])
        assert ((rep_collatz[0] - 16) == 0) and ((rep_collatz[1] - 178) == 0)
