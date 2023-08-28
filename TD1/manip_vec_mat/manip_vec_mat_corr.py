import numpy as np
try:
    from manip_vec_mat_fct import *
except:
    print("ERREUR! Il y a une erreur fatale dans le fichier manip_vec_mat_fct.py")


class Test:

    def test_faire_vecteur_x(self):
        x = faire_vecteur_x()

        assert np.linalg.norm(x - np.linspace(0, 5, 101)) < 1e-14

    def test_faire_vecteur_f(self):
        f = faire_vecteur_f()

        assert np.linalg.norm(f - np.linspace(0, 5, 101)**2) < 1e-14

    def test_faire_matrice(self):
        mat = faire_matrice()

        assert np.linalg.norm(np.array([[2, -5, 3], [3, -1, 4], [1, 3, 2]])-mat) < 1e-14

    def test_faire_second_membre(self):
        b = faire_second_membre()

        assert np.linalg.norm(np.array([8, 7, -3])-b) < 1e-14
