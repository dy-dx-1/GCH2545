import fonctions as f 
import numpy as np 
import matplotlib.pyplot as plt 

class Parametres():
    u_inf = 1 
    R = 1 
    R_ext = 5 
    
    theta_min = 0 
    theta_max = 2 * np.pi 

    nx = 15
    ny = 15

def main():
    prm = Parametres()
    maille_r, maille_theta, vecteur_psis = f.mdf(params=prm)

    vr, vtheta = f.vitesses(vecteur_psis, prm) # obtention des vitesses sous forme de vecteur de noeuds 1d 
    vr_mesh = f.arrange_mesh(vr, prm.nx, prm.ny) 
    vtheta_mesh = f.arrange_mesh(vtheta, prm.nx, prm.ny) # convertion des vitesses en vecteur 1d sur la maille des solutions 
    X, Y, VX, VY = f.convert_coords(maille_r, maille_theta, vr_mesh, vtheta_mesh) # convertion des mailles en cartésien 

    ## plotting 
    fig, ax = plt.subplots() 
    ax.quiver(X, Y, VX, VY)
    # ajout d'un cercle pour representer le cylindre 
    cyl = plt.Circle((0,0), prm.R, color="r", fill=False, label="Cylindre")
    ax.add_patch(cyl) 
    # Labels 
    ax.legend() 
    ax.set_xlabel("Coordonnées en x")
    ax.set_ylabel("Coordonnées en y")
    ax.set_title("Un bon titre")
    # Cleanup de l'affichage 
    ax.set_aspect('equal', 'box')
    ax.grid(True) 
    plt.show() 
    
if __name__=="__main__": 
    main() 