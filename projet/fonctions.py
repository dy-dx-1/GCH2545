import numpy as np 
import pytest

np.set_printoptions(precision=2, linewidth=150) # permet d'imprimer les arrays de manière plus compacte pr les inspecter 

def psi_exact(r, theta, params): 
    return params.u_inf * r * np.sin(theta)*(1-np.square(params.R/r))

def psi_ref_mesh(prm:object):
    """ 
    Retourne une maille correspondant aux sols exactes de psi sur notre domaine discretisé 
    """
    r, theta = gen_maille(prm.R, prm.R_ext, prm.theta_min, prm.theta_max, prm.nx, prm.ny) # sert à retourver coords dans notre maillage 
    ref_mesh = list() 
    for index_vertical, ligne_r in enumerate(r):
        # chaque iter donne une ligne 1d [ ... ] des valeurs de R de bas en haut (donc constant) 
        # ainsi que un index vertical qui sert à retrouver theta 
        ligne_psi = list() 
        for index_horizonal, r in enumerate(ligne_r): 
            if index_horizonal==0:continue 
            print(r, theta[index_vertical, index_horizonal], psi_exact(r, theta[index_vertical, index_horizonal], prm), sep="\n")
            quit()
            # chaque iter donne une valeur de r dans la ligne 1d ainsi que son index horizontal pour retrouver theta 
            ligne_psi.append(psi_exact(r, theta[index_vertical, index_horizonal], prm))   
        ref_mesh.append(ligne_psi) 
    return ref_mesh

    
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

    k=0  k=1    ... k = nx-1
    k=nx k=nx+1 ... 
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

def mdf(params): 
    """
    Applique la méthode des différences finies pour résoudre le système sur le domaine 2D 
    """
    nx, ny = params.nx, params.ny
    r_min, r_max, theta_min, theta_max = params.R, params.R_ext, params.theta_min, params.theta_max
    domaine_r, domaine_theta = gen_maille(r_min, r_max, theta_min, theta_max, nx, ny)
    dr = abs(r_max-r_min)/(nx-1)
    dtheta = abs(theta_max-theta_min)/(ny-1)
    # Matrice qui acceuillera les différentes solutions des noeuds 
    N = nx*ny 
    noeuds = np.zeros((N,N)) 
    # Vecteur résidu associé à la matrice des noeuds 
    res = np.zeros(N)
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
            res[k] = params.u_inf*r_max*np.sin(theta_k)*(1-np.square(r_min/r_max))
        else: # Alors on est à un noeud qui n'est pas sur le bord 
            # Trouvons le r associé à k 
            i = k%nx 
            j = convert_indices(nx, i=i, j=None, k=k)
            rk = domaine_r[j, i]
            # Évaluons les coefficients des différents noeuds de T, soit Tk+nx, Tk-nx, Tk+1, Tk-1 
            noeuds += gen_central_values(k, nx, ny, rk, dr, dtheta)
    solutions = np.linalg.solve(noeuds, res)
    return noeuds, res, solutions  

def integrale(x, y): 
    """ Fonction qui calcule une integrale avec la méthode des trapèzes pour des séries de valeurs discrètes
    

    Entrées: 
    
    Sorties: 
    * Valeurs de l'intégrale """ 
    N = len(x)-1 
    
    return 0.5*sum((x[i]-x[i-1])*(y[i]+y[i-1]) for i in range(1, N))

def vitesses(psi, params:object): 
    """Fonction qui calcule les vitesses selon r et theta 
    
    Entrées: 

    
    Sortie:

    """
    nx = params.nx
    ny = params.ny 
    r = np.linspace(params.R, params.R_ext, nx) 

    dr = abs(params.R_ext-params.R)/(nx-1)
    dtheta = abs(params.theta_max-params.theta_min)/(ny-1)
    # Note: r est un vecteur 1d de longueur nx alors que le vect des derivees est 1d longueur N (parce que c'est des solutions aux nx*ny noeuds) 
    # on doit donc creer r_ qui represente les valeurs de r à chaque noeud dans l'ordre du vect des derivées pour pouvoir les multiplier 
    r_ = np.array(sum([list(r) for _ in range(ny)], [])) 
    vr = (1/r_)*deriv_by_coeff(psi, 'theta', nx, dtheta)
    vtheta = -deriv_by_coeff(psi, 'r', nx, dr)
    return vr, vtheta

def cp(vitesse, params): 
    """ 
    V est un vecteur de vitesses à R variant selon theta donc on doit juste l'évaluer et retourne le résultat
    """
    return 1-np.square(vitesse/params.u_inf)

def deriv_by_coeff(psis:np.array, coeff:str, nx:int, delta:float): 
    """ 
    Iterates through all psis & differentiates using the specified coeff as a delta 
    """
    coeff = coeff.strip().lower() 
    N = len(psis)
    if not any([coeff=="r", coeff=="theta"]): return None # check rapide que la fonction est bien utilisée 
    psi_prime = list() # Liste qui contiendra les psi dérivés en ordre 
    for k, psi in enumerate(psis): 
        # Il faut savoir si on est sur l'axe des r ou de theta pour appliquer les bonnes conditions 
        # on appliquera ensuite les mêmes structures de contrôle que dans la mdf pour savoir si on est sur le perimetre et donc quelle derivee appliquer
        if coeff == "r": 
            # alors derivée 'horizontale' sur notre maillage, on a juste a vérifier si on est a gauche ou a droite 
            if k%nx==0: # gauche, derivee gear avant ordre 2 
                psi_p = -psis[k+2] + (4*psis[k+1]) - (3*psi)
            elif (k+1)%nx==0: # droite, derivee gear arriere ordre 2 
                psi_p = (3*psi) - (4*psis[k-1]) + psis[k-2]
            else: # milieu, derivee centree ordre 2 
                psi_p = psis[k+1]-psis[k-1]
        else: # notre verification initiale nous permet d'assurer que si ce n'Est pas r, c'est theta qu'on veut 
            # alors derivee 'verticale' sur le maillage, on a besoin de verifier si on est en haut ou bas 
            if k<=(nx-1): # haut, derivee gear avant ordre 2 
                psi_p = -psis[k+nx+nx] + (4*psis[k+nx]) - (3*psi)
            elif k>=(N-nx) and k<=(N-1): # bas, derivee gear arriere ordre 2
                psi_p = (3*psi) - (4*psis[k-nx]) + psis[k-nx-nx]
            else: # centre, derivee centree ordre 2 
                psi_p = psis[k+nx]-psis[k-nx]
        psi_prime.append(psi_p/(2*delta))
    return np.array(psi_prime)

def arrange_mesh(vector, nx, ny): 
    # prend un vecteur 1d correspondant à des valeurs associées à des noeuds K et les retourne en format 2D selon la maille nx*ny 
    maille = []
    for k in range(0, nx*ny, nx): 
        maille.append(vector[k:k+nx])
    return np.array(maille)

def cd(cp, N): 
    """ 
    woo 
    """
    domain = np.linspace(0, 2*np.pi, N)
    integrande = cp*np.cos(domain) # fonction qu'on intègre pour avoir le cd 
    return -0.5*integrale(domain, integrande) 

def cl(cp, N): 
    """ 
    woo 
    """
    domain = np.linspace(0, 2*np.pi, N)
    integrande = cp*np.sin(domain) # fonction qu'on intègre pour avoir le cl 
    return -0.5*integrale(domain, integrande) 

def convert_coords(vr, vtheta, prm):
    # prend des vecteurs 1d correspondant aux noeuds k et les transpose sur des axes cartesiens 
    # on ne fait qu'appliquer une matrice de rotation sur les couples vr et vtheta 
    N = prm.nx*prm.ny 
    R, T = gen_maille(prm.R, prm.R_ext, prm.theta_min, prm.theta_max, prm.nx, prm.ny)
    vx, vy = list(), list() 
    for k in range(N): 
        i = k%prm.nx # il faut qu'on retrouve les coords i, j dans la maille pour retrouver theta 
        theta = T[convert_indices(prm.nx, i=i, j=None, k=k),i] 
        vitesse_cartesienne = np.matmul([[np.cos(theta),np.sin(theta)],[np.sin(theta),np.cos(theta)]], [[vr[k]],[vtheta[k]]])
        vx.append(vitesse_cartesienne[0,0])
        vy.append(vitesse_cartesienne[1,0])
    return np.array(vx), np.array(vy) 

if __name__ == "__main__": 
    """ 
    permet de lancer le fichier fonctions.py pour faire les tests 
    """
    pytest.main(['tests.py']) 