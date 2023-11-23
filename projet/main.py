import fonctions as f 

class Parametres():
    u_inf = 1 
    R = 1 
    R_ext = 5 

def main():
    # tests, ceci peut etre effacé 
    prm = Parametres()
    noeuds, res, solutions = f.mdf(r_min=1, r_max=5, theta_min=0, theta_max=6.28, nx=5, ny=5, params=prm)
    print(solutions)
if __name__=="__main__": 
    main() 