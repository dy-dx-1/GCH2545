# Importation des modules
import numpy as np

def fonc(u):
    """Fonction qui calcule la fonction qui sera intégrée

    Entrée:
        - u : Variable indépendante

    Sortie:
        - Valeur de la variable dépendante
    """

    return 1 / np.sqrt(8*np.sin(u) - u)

def gauss(a,b,n):
    """Fonction qui calcule l'intégrale selon Gauss-Legendre

    Entrées:
        - a : Borne inférieure de l'intégrale
        - b : Borne supérieure de l'intégrale
        - n : le nombre de points souhaité pour la quadrature (1, 2, 3, 4 ou 5)

    Sortie:
        - Valeur numérique de l'intégrale
    """

    # Points et poids d'intégration
    t = np.empty(n)
    w = np.empty(n)

    if n == 1:
        pass# à compléter, pass doit être remplacer par le bon code
    elif n == 2:
        pass# à compléter, pass doit être remplacer par le bon code
    elif n == 3:
        pass# à compléter, pass doit être remplacer par le bon code
    elif n == 4:
        t[0] = (-np.sqrt(525 + 70*np.sqrt(30)))/35
        t[1] = (-np.sqrt(525 - 70*np.sqrt(30)))/35
        t[2] = -1*t[1]
        t[3] = -1*t[0]

        w[0] = (18 - np.sqrt(30))/36
        w[1] = (18 + np.sqrt(30))/36
        w[2] = (18 + np.sqrt(30))/36
        w[3] = (18 - np.sqrt(30))/36
    elif n == 5:
        t[0] = -(np.sqrt(245 + 14*np.sqrt(70)))/21
        t[1] = -(np.sqrt(245 - 14*np.sqrt(70)))/21
        t[2] = 0
        t[3] = -1*t[1]
        t[4] = -1*t[0]

        w[0] = (322 - 13*np.sqrt(70))/900
        w[1] = (322 + 13*np.sqrt(70))/900
        w[2] = 128/225
        w[3] = (322 + 13*np.sqrt(70))/900
        w[4] = (322 - 13*np.sqrt(70))/900

    # Calcul de l'intégrale
    # à compléter

    return # à compléter
