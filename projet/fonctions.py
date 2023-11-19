import numpy as np 

def psi_exact(r, theta, params): 
    return params.u_inf * r * np.sin(theta*(1-( (params.R**2)/(params.r**2) )))