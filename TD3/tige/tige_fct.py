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
        t[0] = 0 
        w[0] = 2 
    elif n == 2:
        t[0] = -np.sqrt(1/3) 
        t[1] = np.sqrt(1/3)

        w[0] = 1 
        w[1] = 1 
    elif n == 3:
        t[0] = -(np.sqrt(15)/5) 
        t[1] = 0 
        t[2] = np.sqrt(15)/5 

        w[0] = 5/9 
        w[1] = 8/9 
        w[2] = 5/9 
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

    # Soit g(x), la fonction équivalente à intégrer sur le domaine [-1,1] 
    g = lambda x: fonc( ( ((b-a) *x) + (a+b) )/2) * ((b-a) / 2)
    # Évaluons maintenant l'intégrale I avec la somme définie par Gauss-Legendre
    I = sum(w*g(t)) 
    # Petit output pour répondre au quiz moodle 
    print(f"Résultat de l'intégrale pour n = {n} : {I}")
    return I 
