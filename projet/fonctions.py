import numpy as np 

def psi_exact(r, theta, params): 
    return params.u_inf * r * np.sin(theta*(1-( (params.R**2)/(params.r**2) )))

def gen_maille(r_min, r_max, theta_min, theta_max, nx, ny): 
    """ 
    Genère les coordonnées r et theta de chacun des points du maillage sous forme de tuples de coords 
    de forme 

    (r_min, theta_max) (r_min+1, theta_max) ... (r_max, theta_max) 
    ...
    (r_min, theta_min+1) ...                    (r_max, theta_min+1)
    (r_min, theta_min) (r_min+1, theta_min) ... (r_max, theta_min)
    """
    return np.vstack([ [(r, theta) for r in np.linspace(r_min, r_max, nx)] for theta in np.linspace(theta_max, theta_min, ny) ])

def convert_indices(nx:int, i = None, j = None, k = None)->int: 
    """
    Prend 2 indices et retourne celui qui n'est pas spécifié selon un maillage de forme 

    k=0  k=1    ... k = ny-1
    k=ny k=ny+1 ... 
    """
    # on assume que le programmeur sait utiliser la fonction donc pas de check complet des paramètres passés
    if i is None: 
        return int(k - (nx*j)) 
    elif j is None: 
        return int((k-i) / nx) 
    elif k is None: 
        return int(i + (j*nx)) 
    else: 
        return None 
    
def gen_central_values(k, nx, ny): 
    N = nx*ny 
    mat_ref = np.zeros((N, N)) # on crée un matrice NxN qu'on remplira des coefficients 
             # on sépare ceci de la matrice des noeuds de la fonction mdf pour faciliter nos tests, on devrait avoir une matrice dont toutes les valeurs des bords sont nulles 
    Tk_nx = 0 
    Tk_nx_ = 0 
    Tk_1 = 0 
    Tk_1_ = 0 
    Tk = 0            
    # Calculons la position i de reférence par rapport à k 
    i = k%nx  
    # Retrouvons avec k et i la position j du noeud 
    j = convert_indices(ny, i=i, j=None, k=k)
    # Plaçons les coefficients dans la matrice 
    mat_ref[j, i] = Tk 
    mat_ref[j, i+1] = Tk_1 
    mat_ref[j, i-1] = Tk_1_
    mat_ref[j+1, i] = Tk_nx 
    mat_ref[j-1, i] = Tk_nx_
    # Le résidu est nul pour ces noeuds donc on n'a pas besoin de le modifier  

def mdf(r_min, r_max, theta_min, theta_max, nx, ny): 
    """
    Applique la méthode des différences finies pour résoudre le système sur le domaine 2D 
    """
    # Préparons la matrice qui acceuillera les différentes solutions des noeuds 
    N = nx*ny 
    noeuds = np.zeros((N,N)) 
    # Préparons le vecteur résidu associé à la matrice des noeuds 
    res = np.zeros((1,N))
    # Itérons sur chacun des k afin de remplir la matrice des noeuds et du résidu 
    for k in range(N): 
        if True: # Condition limite du bas 
            pass 
        elif True: # Condition limite du haut 
            pass 
        elif True: # Condition limite de gauche 
            pass 
        elif True: # Condition limite de droite 
            pass 
        else: # Alors on est à un noeud qui n'est pas sur le bord 
            # Évaluons les coefficients des différents noeuds de T, soit Tk+ny, Tk-ny, Tk+1, Tk-1 
            noeuds += gen_central_values(k, nx, ny)