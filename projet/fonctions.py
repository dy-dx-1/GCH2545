import numpy as np 

def psi_exact(r, theta, params): 
    return params.u_inf * r * np.sin(theta*(1-( (params.R**2)/(params.r**2) )))

def gen_maille(r_o, r_max, theta_o, theta_max, nx, ny): 
    """ 
    Genère les coordonnées r et theta de chacun des points du maillage sous forme de tuples de coords 
    """
    maille = np.vstack([ [(r, theta) for r in np.linspace(r_o, r_max, nx)] for theta in np.linspace(theta_max, theta_max, ny) ])

def convert_indices(ny:int, i = None, j = None, k = None)->int: 
    """
    Prend 2 indices et retourne celui qui n'est pas spécifié selon un maillage de forme 

    k=nx k=nx+1 ... 
    k=0  k=1 k=2 ... k=nx-1 
    """
    # on assume que le programmeur sait utiliser la fonction donc pas de check complet des paramètres passés
    if i is None: 
        return k - (ny*j) 
    elif j is None: 
        return (k-i) / ny 
    elif k is None: 
        return i + (j*ny)
    else: 
        return None 