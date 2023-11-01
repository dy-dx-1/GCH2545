# Importation des modules
import numpy as np

def position(X,Y,nx,ny):
    """ Fonction générant deux matrices de discrétisation de l'espace

    Entrées:
        - X : Bornes du domaine en x, X = [x_min, x_max]
        - Y : Bornes du domaine en y, Y = [y_min, y_max]
        - nx : Discrétisation de l'espace en x (nombre de points)
        - ny : Discrétisation de l'espace en y (nombre de points)

    Sorties (dans l'ordre énuméré ci-bas):
        - x : Matrice (array) de dimension (ny x nx) qui contient la position en x
        - y : Matrice (array) de dimension (ny x nx) qui contient la position en y
            * Exemple d'une matrice position :
            * Si X = [-1, 1] et Y = [0, 1]
            * Avec nx = 3 et ny = 3
                x = [-1    0    1]
                    [-1    0    1]
                    [-1    0    1]

                y = [1    1    1  ]
                    [0.5  0.5  0.5]
                    [0    0    0  ]
    """

    # Fonction à écrire

    return # à compléter

def vitesse(x,y):
    """ Fonction donnant les vitesses en x et y selon la position

    Entrées:
        - x : Matrice de dimension (ny x nx) qui contient la position en x
        - y : Matrice de dimension (ny x nx) qui contient la position en y

    Sorties (dans l'ordre énuméré ci-bas):
        - u : Matrice (array) de dimension (ny x nx) qui contient la vitesse en x
        - v : Matrice (array) de dimension (ny x nx) qui contient la vitesse en y

    """

    u = 2*y*(1-x**2)
    v = -2*x*(1-y**2)

    return u,v

def mdf_assemblage(X,Y,nx,ny,Pe,alpha):
    """ Fonction assemblant la matrice A et le vecteur b

    Entrées:
        - X : Bornes du domaine en x, X = [x_min, x_max]
        - Y : Bornes du domaine en y, Y = [y_min, y_max]
        - nx : Discrétisation de l'espace en x (nombre de points)
        - ny : Discrétisation de l'espace en y (nombre de points)
        - Pe : Nombre de Péclet
        - alpha : Constante des conditions de Dirichlet sur les frontières

    Sorties (dans l'ordre énuméré ci-bas):
        - A : Matrice (array)
        - b : Vecteur (array)
    """

    # Fonction à écrire


    return # à compléter
