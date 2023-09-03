import numpy as np
try:
    from erreur_fct import *
except:
    print("ERREUR! Il y a une erreur fatale dans erreur_fct.py")


class Test:

    def test_g(self):
        assert abs(g(1) - 0.14380551) < 1e-06
        assert abs(g(7) - 1.9939339) < 1e-06

    def test_diff1(self):
        assert abs(diff_arriere_ordre1(1, 0.1) - 0.2434254) < 1e-06
        assert abs(diff_arriere_ordre1(5, 0.02) - 0.3106684) < 1e-06

    def test_diff2(self):
        assert abs(diff_centree_ordre2(1, 0.1) - 0.2496871) < 1e-06
        assert abs(diff_centree_ordre2(4.5, 0.02) - 0.3155681) < 1e-06
