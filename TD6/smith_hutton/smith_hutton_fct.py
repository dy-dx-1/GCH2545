# Importation des modules
import numpy as np

np.set_printoptions(linewidth=400) 
def position(X,Y,nx,ny):
    """ Fonction générant deux matrices de discrétisation de l'espace

    Entrées:
        - X : Bornes du domaine en x, X = [x_min, x_max]
        - Y : Bornes du domaine en y, Y = [y_min, y_max]
        - nx : Discrétisation de l'espace en x (nombre de points)
        - ny : Discrétisation de l'espace en y (nombre de points)

    Sorties (dans l'ordre énuméré ci-bas):
        - x : Matrice (array) de dimension (ny x nx) qui contient la position en x
        - y : Matrice (array) de dimension (ny x nx) qui contient la position en y
            * Exemple d'une matrice position :
            * Si X = [-1, 1] et Y = [0, 1]
            * Avec nx = 3 et ny = 3
                x = [-1    0    1]
                    [-1    0    1]
                    [-1    0    1]

                y = [1    1    1  ]
                    [0.5  0.5  0.5]
                    [0    0    0  ]
    """
    # En gros on construit 2 matrices pr représenter les coords xi,yj de nos pts discrétisés 
    # la matrice en x est les pos xi et la matrice en y est les pos yj 
    x_min, x_max = X[0], X[1] 
    y_min, y_max = Y[0], Y[1]
    x = np.array([ np.linspace(x_min, x_max, nx) for ligne in range(ny) ]) # crée une liste [ [], [], [], ...]
    y = np.array([ [j for i in range(nx)] for j in np.linspace(y_max, y_min, ny)])

    return x, y

def vitesse(x,y):
    """ Fonction donnant les vitesses en x et y selon la position

    Entrées:
        - x : Matrice de dimension (ny x nx) qui contient la position en x
        - y : Matrice de dimension (ny x nx) qui contient la position en y

    Sorties (dans l'ordre énuméré ci-bas):
        - u : Matrice (array) de dimension (ny x nx) qui contient la vitesse en x
        - v : Matrice (array) de dimension (ny x nx) qui contient la vitesse en y

    """

    u = 2*y*(1-x**2)
    v = -2*x*(1-y**2)

    return u,v

def mdf_assemblage(X,Y,nx,ny,Pe,alpha):
    """ Fonction assemblant la matrice A et le vecteur b

    Entrées:
        - X : Bornes du domaine en x, X = [x_min, x_max]
        - Y : Bornes du domaine en y, Y = [y_min, y_max]
        - nx : Discrétisation de l'espace en x (nombre de points)
        - ny : Discrétisation de l'espace en y (nombre de points)
        - Pe : Nombre de Péclet
        - alpha : Constante des conditions de Dirichlet sur les frontières

    Sorties (dans l'ordre énuméré ci-bas):
        - A : Matrice (array)
        - b : Vecteur (array)
    """
    # Discrétisation du domaine et création des coords equivalentes 1d 
    pos_x, pos_y = position(X, Y, nx, ny) 
    vit_x, vit_y = vitesse(pos_x, pos_y)
    dx = (X[1] - X[0])/(nx-1)
    dy = (Y[1] - Y[0])/(ny-1)
    N = nx*ny # nb de pts total 
    ca = 1 - np.tanh(alpha) # cond de dirichlet fixe 

    # Préparation de la matrice et du vecteur 
    mat = np.zeros((N, N)) 
    res = np.zeros(N)

    # Implémentation des conditions limites faciles (suivies)
    for k in range(ny): # Dirichlet à gauche, k va de 0 à ny-1 
        # ligne = k et col = k car cond dirichlet donc on rempli directemetn [[1, 0, ..., 0], [0, 1, 0, ..., 0], .. 
        mat[k, k] = 1 
        res[k] = ca # pour le résidu, il est de taille (N, 1) donc k correspond exactement à variable Ck dans le vect (C0, C1, ..., CN-1)
    for k in range(N-ny, N): # Dirichlet à droite, k va de N-ny à N-1 
        mat[k, k] = 1 
        res[k] = ca
    # Comme les 2 autres conditions limites ne peuvent pas être représentées par un range on devra itèrer sur le reste des k et utilier des struc. de contrôle 
    # On en profitera pour remplir le reste de la matrice et du vecteur 
    for k in range(ny, N-ny): 
        # Vérif si on est en haut 
        if k % ny == 0: 
            # en haut, la ligne est 0 et la colonne sera la division entière de k et ny (pour le haut, // et / devraient être équivalents car k%ny == 0
            mat[k, k] = 1 
            res[k] = ca
        # Vérif si on est en bas 
        elif k % ny == ny-1: 
            # Si on est bas, sommes nous à gauche inclus de (0,0) en supposant bornes en X symmétriques, ou a droite
            # en bas, la ligne est ny-1 et la col est // de k  
            if k <= ( ((ny-1)+(N-1))/2 ): # à gauche, 0 inclus 
                # pour le res, on a besoin de connaître la pos x associée au i associé au k 
                i = k//ny 
                x = pos_x[ny-1, i] # dernière ligne et colonne i 
                res[k] = 1 + np.tanh(alpha * (2*x+1)) 
                mat[k, k] = 1 
            else: # à droite 
                # on doit implémenter la cond del(c)/del(n) avec n dans le plan du domaine mais sortant = 0 
                # on prend donc une dérivée gear arrière vers le haut, placés au bord du bas telle que 
                # 3*Ck - 4 *Ck-1 + Ck-2 = 0 
                mat[k, k] = 3 
                mat[k, k-1] = -4  
                mat[k, k-2] = 1 
                # pas de modif du vect résidu car cond implique que c'est nul 
        else: 
            # Ici on rempli les coefficients des noeuds aux centre, le résidu n'a pas besoin d'être altéré à cause qu'il est nul
            i = k//ny # nous donne la pos en i de la grille donc la colonne 
            j_inv = k%ny # nous donne le j inversé (partant du haut) donc la ligne, ces relations peuvent assez facilement être trouvées visuellement avec crayon papier 
            ux = vit_x[j_inv, i] 
            uy = vit_y[j_inv, i] 
            
            Ckny = (ux/(2*dx)) - (1/(dx*dx*Pe)) # Ck+ny
            Ck1 = (-uy/(2*dy)) - (1/(dy*dy*Pe)) # Ck+1
            Ck = (2/(dx*dx*Pe)) + (2/(dy*dy*Pe)) # Ck
            Ck1_ = (uy/(2*dy)) - (1/(dy*dy*Pe))  # Ck-1
            Ckny_ = (-ux/(2*dx)) - (1/(dx*dx*Pe)) # Ck-ny

            # pour chaque équation a*Ckny + b*Ck+1 + cCk + dCk-1 + eCk-ny = 0, on place les coefficients à la ligne k 
            # les colonnes changent selon le coefficient 
            mat[k, k+ny] = Ckny
            mat[k, k-ny] = Ckny_
            mat[k, k+1] = Ck1
            mat[k, k-1] = Ck1_
            mat[k, k] = Ck

    return mat, res 