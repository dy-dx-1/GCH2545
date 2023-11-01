# Importation des modules
import numpy as np

def mdf(prm):
    """Fonction qui calcule le profil de température le long de l'ailette

    Entrées:
        - prm : Objet class parametres()
            - L : Longueur
            - D : Diamètre
            - k : Conductivité thermique
            - T_a : Température ambiante
            - T_w : Température du mur
            - h : Coefficient de convection
            - N : Nombre de points utilisés pour la méthode

    Sorties (dans l'ordre énuméré ci-bas):
        - Vecteur (np.array) donnant la température tout au long de l'ailette en Kelvin
        - Vecteur (np.array) donnant la position tout au long de l'ailette (axe z) en mètre
    """
    # Tout d'abord on unpack les params 
    L, D, k, T_a, T_w, h, n = prm.L, prm.D, prm.k, prm.T_a, prm.T_w, prm.h, prm.N 
    # Préparons la matrice des différences finies & le vecteur résidu 
    matrice = np.zeros((n,n)) 
    residu = np.zeros((n, 1)) 
    # Définissons le domaine de résolution 
    dl = L/(n-1) # largeur des intervalles 
    positions = np.linspace(0, L, n) 
    # Ajoutons la condition de Dirichlet 
    matrice[0,0] = 1 
    residu[0,0] = T_w 
    # Promenons nous parmi les index des noeuds pour remplir la matrice de coefficients 
    for i in range(1, n-1): 
        Tprev = None 
        Ti = None 
        Tnext = None 
        matrice[i, i+1] = Tnext 
        matrice[i, i] = Ti 
        matrice[i, i-1] = Tprev 
    # Maintenant rajoutons la condition de Neumann 
    matrice[n-1, n-1] = None    # on indexe comme si notre i est n-1 pour cette condition 
    matrice[n-1, n-2] = None
    matrice[n-1, n-3] = None 

    residu[n-1, 0] = None 

    return # à compléter

def inte(T,z,prm):
    """Fonction qui intègre la convection sur la surface de l'ailette.

    Entrées:
        - T : Vecteur comprenant les températures  en Kelvin sur la longueur de l'ailette
                pour une combinaison géométrique donnée
        - z : Vecteur comprenant les points sur la longueur en mètre
        - prm : Objet class parametres()
            - k : Conductivité thermique
            - T_a : Température ambiante
            - T_w : Température du mur
            - h : Coefficient de convection
            - N : Nombre de points utilisés pour la méthode

    Sortie:
        - Valeur numérique de l'intégrale résultante (perte en W)
    """


    # Fonction à écrire
    I=0

    return I# à compléter
