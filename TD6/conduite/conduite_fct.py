# Importation des modules
import numpy as np

def mdf(prm):
    """Fonction simulant avec la méthode des différences finies

    Entrées:
        - prm : Objet class parametres()
            - Tr : Température à l'intérieur de la conduite [K]
            - Te : Température ambiante autour de la conduite [K]
            - k : Conductivité thermique [W*m^-1*K^-1]
            - h : Coefficient de convection thermique [W*m^-2*K^-1]
            - Re : Rayon externe [m]
            - Ri : Rayon interne [m]
            - n : Nombre de noeuds [-]
            - dr : Pas en espace [m]

    Sortie (dans l'ordre énuméré ci-bas):
        - Vecteur (array) de dimension N composé de la position radiale à laquelle les températures sont calculées, où N le nombre de noeuds.
        - Vecteur (array) de dimension N composé de la température en fonction du rayon, où N le nombre de noeuds
    """
    # unpackons nos paramètres 
    Tr, Te, k, h, Re, Ri, n, dr = prm.Tr, prm.Te, prm.k, prm.h, prm.Re, prm.Ri, prm.n, prm.dr 
    # Préparons les vecteurs nécéssaires au calcul  
    pos_r = np.linspace(Ri, Re, n) # linspace divisera notre domaine radial en n noeuds 
    matrice_diff = np.zeros((n,n))
    vect_residu = np.zeros((n,1))
    # Ajoutons la condition initiale de Dirichlet 
    matrice_diff[0,0] = 1 # coefficient 1 pour notre To 
    vect_residu[0,0] = Tr  # Solution associée à To = Tr

    # Promenons nous de noeud en noeud pour générer les lignes de notre matrice 
    for i in range(1, n-1):  # on saute la première et dernière étape car on utilisera les conditions initiales  
        # Évaluons coefficient de Ti+1, Ti et Ti-1 avant de les mettre dans matrice 
        Tnext = (pos_r[i] / (dr**2)) + (1/(2*dr))
        Ti = (-2*pos_r[i]) / (dr**2) 
        Tprev = (pos_r[i] / (dr**2)) - (1/(2*dr))
        # Selon relation que j'ai trouvé en dessinant sur ma tablette, je remplis la matrice des diff finies avec les coefficients respectifs
        # Pour un i donné, coeff de élément i va à pos [i, i] ; élément i+1 va à [i, i+1] ; élément i-1 va à [i, i-1] 
        matrice_diff[i, i-1] = Tprev 
        matrice_diff[i, i] = Ti 
        matrice_diff[i, i+1] = Tnext 
        # Le reste reste des zéros  

    # Ensuite ajoutons notre condition de robin 
    matrice_diff[n-1, n-1] = 3+(2*h*dr/k) # on indexe comme si notre i est n-1 pour cette condition 
    matrice_diff[n-1, n-2] = -4 
    matrice_diff[n-1, n-3] = 1 

    vect_residu[n-1, 0] = 2*h*dr*Te / k 
    # Maintenant résolvons le sys matricielle pour trouver nos [T0, T1, T2, ..., Tn] 
    temperatures = np.linalg.solve(matrice_diff, vect_residu)
    return pos_r, temperatures