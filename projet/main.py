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
    # tests, ceci peut etre effacé 
    prm = Parametres()
    noeuds, res, solutions = f.mdf(params=prm)
    vr, vtheta = f.vitesses(solutions, prm) 
    R, THETA = f.gen_maille(prm.R, prm.R_ext, prm.theta_min, prm.theta_max, prm.nx, prm.ny) 
    vr_mesh = f.arrange_mesh(vr, prm.nx, prm.ny) 
    vtheta_mesh = f.arrange_mesh(vtheta, prm.nx, prm.ny) 
    X, Y = f.gen_maille(-prm.R_ext, prm.R_ext, -prm.R_ext, prm.R_ext, prm.nx, prm.nx) 
    vx, vy = f.convert_coords(vr, vtheta, prm) 
    vx_mesh, vy_mesh = f.arrange_mesh(vx, prm.nx, prm.ny), f.arrange_mesh(vy, prm.nx, prm.ny)

    # plotting 
    fig, ax = plt.subplots() 
    ax.quiver(X, Y, vx_mesh, vy_mesh)
    # ajout d'un cercle pour representer le cylindre 
    cyl = plt.Circle((0,0), prm.R, color="r", fill=False)
    ax.add_patch(cyl) 
    plt.show() 
    
if __name__=="__main__": 
    main() 