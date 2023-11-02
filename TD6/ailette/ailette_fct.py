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
        Tprev = k/(dl**2) 
        Ti = ((-2*k/(dl**2)) - (4*h/D)) 
        Tnext = k/(dl**2) 
        matrice[i, i+1] = Tnext 
        matrice[i, i] = Ti 
        matrice[i, i-1] = Tprev 
        # Pour cette équation différentielle, le résidu des coefficients intermédiaires n'est pas nul 
        residu[i, 0] = -4*h*T_a/D
    # Maintenant rajoutons la condition de Neumann 
    matrice[n-1, n-1] = 3    # on indexe comme si notre i est n-1 pour cette condition (c'est le dernier élément de notre mat nxn avec l'indexation python)
    matrice[n-1, n-2] = -4
    matrice[n-1, n-3] = 1 
    residu[n-1, 0] = 0 # flux nul car paroi isolée  
    # Finalement résolvons le système 
    gradient = np.linalg.solve(matrice, residu) 
    # Attention, le gradient est retourné sous la forme nx1 donc on doit le transposer & prendre la première ligne pour que les tests passent 
    return gradient.T[0], positions

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
