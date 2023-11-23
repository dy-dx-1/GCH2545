import numpy as np 
import pytest

np.set_printoptions(precision=2, linewidth=150) # permet d'imprimer les arrays de manière plus compacte pr les inspecter 

def psi_exact(r, theta, params): 
    return params.u_inf * r * np.sin(theta*(1-( (params.R**2)/(params.r**2) )))

def gen_maille(r_min, r_max, theta_min, theta_max, nx, ny): 
    """ 
    Genère les coordonnées r et theta de chacun des points du maillage 
    """
    r = np.array([ [r for r in np.linspace(r_min, r_max, nx)] for _ in range(ny) ])
    theta =  np.array([ [theta for _ in range(nx)] for theta in np.linspace(theta_max, theta_min, ny) ])
    return r, theta

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
    
def gen_central_values(k, nx, ny, rk, dr, dtheta): 
    N = nx*ny 
    mat_ref = np.zeros((N, N)) # on crée un matrice NxN qu'on remplira des coefficients 
             # on sépare ceci de la matrice des noeuds de la fonction mdf pour faciliter nos tests, on devrait avoir une matrice dont toutes les valeurs des bords sont nulles 
    Tk_nx = 1 / (np.square(rk)*np.square(dtheta)) 
    Tk_nx_ = Tk_nx
    Tk_1 = (1/np.square(dr)) + (1/(2*rk*dr))
    Tk_1_ = (1/np.square(dr)) - (1/(2*rk*dr)) 
    Tk = (-2/np.square(dr)) + (-2/(np.square(rk)*np.square(dtheta)))           

    # Plaçons les coefficients dans la matrice 
    mat_ref[k, k] = Tk 
    mat_ref[k, k+1] = Tk_1 
    mat_ref[k, k-1] = Tk_1_
    mat_ref[k, k+nx] = Tk_nx 
    mat_ref[k, k-nx] = Tk_nx_
    # Le résidu est nul pour ces noeuds donc on n'a pas besoin de le modifier  
    return mat_ref

def mdf(r_min, r_max, theta_min, theta_max, nx, ny, params): 
    """
    Applique la méthode des différences finies pour résoudre le système sur le domaine 2D 
    """
    domaine_r, domaine_theta = gen_maille(r_min, r_max, theta_min, theta_max, nx, ny)
    dr = abs(r_max-r_min)/(nx-1)
    dtheta = abs(theta_max-theta_min)/(ny-1)
    # Matrice qui acceuillera les différentes solutions des noeuds 
    N = nx*ny 
    noeuds = np.zeros((N,N)) 
    # Vecteur résidu associé à la matrice des noeuds 
    res = np.zeros((N,1))
    # Itérons sur chacun des k afin de remplir la matrice des noeuds et du résidu 
    for k in range(N): 
        if k<=(nx-1): # Condition limite du haut ; Psik = 0 
            noeuds[k, k] = 1 # pas besoin de changer le résidu car 0 
        elif k>=(N-nx) and k<=(N-1): # Condition limite du bas ; Psik = 0 
            noeuds[k, k] = 1
        elif k%nx==0: # Condition limite de gauche ; Psik = 0 
            noeuds[k, k] = 1
        elif (k+1)%nx==0: # Condition limite de droite ; psik est une fonction 
            noeuds[k, k] = 1
            # calculons le résultat de la fonction qui ira dans le résidu 
            i = nx-1 # on est à droite 
            j = convert_indices(nx, i=i, j=None, k=k) 
            theta_k = domaine_theta[j, i]
            res[k, 1] = params.u_inf*params.R_ext*np.sin(theta_k)*(1-np.square(params.R/params.R_ext))
        else: # Alors on est à un noeud qui n'est pas sur le bord 
            # Trouvons le r associé à k 
            i = k%nx 
            j = convert_indices(nx, i=i, j=None, k=k)
            rk = domaine_r[j, i]
            # Évaluons les coefficients des différents noeuds de T, soit Tk+ny, Tk-ny, Tk+1, Tk-1 
            noeuds += gen_central_values(k, nx, ny, rk, dr, dtheta)
    solutions = np.solve(noeuds, res) 
    return noeuds, res, solutions  

def derive(psi, dt): 
    """Fonction qui calcule la dérivée partielle première par rapport à une variable
    
    Entrées:
      - psi : positions, sera un vecteur (array), de longueur quelconque
      - dt : pas de derivation [float]
    
    Sortie:
      - Vecteur (array) contenant les valeurs numériques de la dérivée première
    """
  
    # Étant donné qu'une approximation d'ordre 2 est imposée ET qu'on demande de prioriser l'utilisation de 2 points, 
    # il faudra utiliser la méthode pas arrière ordre 2, pas avant ordre 2 et la méthode centrée afin de bien évaluer la dérivée 
    # au départ de l'intervalle (3pts, pas avant), à la fin de celui-ci (3pts, pas arrière) et entre les 2 (2pts, centrée)
    # dans notre cas le delta est constant donc on n'a pas à toucher au domaine! On ne jouera que sur les indices 
    dpsi_dt = []
    for i in range(len(h)): 
      if i==0: # si première itération utiliser pas avant 
          v = (-psi[i+2] + (4*psi[i+1]) - (3*psi[i]))/(2*dt)
      elif i==len(psi)-1: # si dernière itération utiliser pas arrière 
          v = ((3*psi[i]) - (4*psi[i-1]) + (psi[i-2]))/(2*dt)
      else: # on est au milieu donc entourés de pts, utiliser approche centrée 
          v = (psi[i+1]-psi[i-1])/(2*dt) 
      dpsi_dt.append(v) 
    return dpsi_dt

def vitesses(r, theta, dr, dtheta): 
    """Fonction qui calcule les vitesses selon r et theta 
    
    Entrées: 
    r: Vecteur de positions radiales
    theta: Vecteur de positions angulaires 
    
    Sortie:
    Vecteur de vitesses radiale et angulaires
    """
    vr = (1/r)*derive(theta, dtheta)
    vtheta = -derive(r, dr)
    return vr, vtheta

if __name__ == "__main__": 
    """ 
    permet de lancer le fichier fonctions.py pour faire les tests 
    """
    pytest.main(['tests.py']) 