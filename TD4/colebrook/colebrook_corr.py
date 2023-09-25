import numpy as np
try:
    from colebrook_fct import *
except:
    print("ERREUR! Il y a une erreur fatale dans le fichier colebrook_fct.py")

class constantes():
    Re = 20000
    k = 1e-4
    D = 1.2

cst = constantes()

class Test:
    
    def test_f(self):
        assert abs(f(0.026065294742584233,cst) - 0.0) < 1e-3
        assert f(0.1,cst) != 0.0
    
    def test_bissection(self):
        assert abs(bissection(0.001,0.1,1e-6,100,cst) - 0.026065294742584233) < 1e-4