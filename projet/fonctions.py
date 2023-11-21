import numpy as np 

def psi_exact(r, theta, params): 
    return params.u_inf * r * np.sin(theta*(1-( (params.R**2)/(params.r**2) )))

def convert_indices(nx:int, i = None, j = None, k = None)->int: 
    """
    Prend 2 indices et retourne celui qui n'est pas spécifié selon un maillage de forme 

    k=nx k=nx+1 ... 
    k=0  k=1 k=2 ... k=nx-1 
    """
    # on assume que le programmeur sait utiliser la fonction donc pas de check complet des paramètres passés
    if i is None: 
        return k - (nx*j) 
    elif j is None: 
        return (k-i) / nx 
    elif k is None: 
        return i + (j*nx)
    else: 
        return None 