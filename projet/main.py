import fonctions as f 
import numpy as np 
import matplotlib.pyplot as plt 

class Parametres():
    u_inf = 1 
    R = 1 
    R_ext = 5 
    
    theta_min = 0 
    theta_max = 2 * np.pi 

    nx = 5
    ny = 5

def main():
    # tests, ceci peut etre effacé 
    prm = Parametres()
    noeuds, res, solutions = f.mdf(params=prm)
    vr, vtheta = f.vitesses(solutions, prm) 
    R, THETA = f.gen_maille(prm.R, prm.R_ext, prm.theta_min, prm.theta_max, prm.nx, prm.ny) 
    vr_mesh = f.arrange_mesh(vr, prm.nx, prm.ny) 
    vtheta_mesh = f.arrange_mesh(vtheta, prm.nx, prm.ny) 
    plt.quiver(R, THETA, vr_mesh, vtheta_mesh)
    plt.show() 
    
if __name__=="__main__": 
    main() 