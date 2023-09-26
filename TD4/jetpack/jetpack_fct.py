# Importation des modules
import numpy as np

def residu(x,prm):
    """Fonction calculant le résidu du système d'équations
    
    Entrées:
        - x : Vecteur (array ou list) des estimés initiaux
            - x[0] : Vitesse d'entrée (boyau) [m/s]
            - x[1] : Vitesse de sortie (propulseur) [m/s]
            - x[2] : Angle d'inclinaison des propulseurs [rad]
        - prm : objet class parametres()
            - g : accélération gravitationnelle [m/s^2]
            - rho : masse volumique [kg/m^3]
            - D_e : diamètre d'entrée [m]
            - D_s : diamètre de sortie [m]
            - m : masse [kg]
            - F : force du vent [N]
    
    Sortie:
        - Vecteur (array) contenant les résidus
            - vecteur[0] : bilan de force par rapport à la verticale
            - vecteur[1] : bilan de force par rapport à l'horizontale
            - vecteur[2] : bilan de masse qui relie les 2 vitesses
            
    NB: - Simplifiez le bilan de masse pour qu'il ne soit fonction que des vitesses et des surfaces
    
    """
    ve = x[0] 
    vs = x[1] 
    theta = x[2]
    R = list() 

    # calcul du premier résidu R[0] = Eq_bilan_f_vertical = 0 
    R.append( (2*np.pi*prm.rho*np.power((prm.D_s*0.5*vs), 2)*np.cos(theta)) + (np.pi*prm.rho*np.power(prm.D_e*0.5*ve, 2)) - (prm.m*prm.g) )
    
    # calcul du deuxième réside R[1] = Eq_bilan_f_horizontal = 0 
    R.append( (-2*np.pi*prm.rho*np.power(prm.D_s*0.5*vs, 2)*np.sin(theta)) + (prm.F) )

    # calcul du troisième résidu R[2] = Eq_bilan_masse = 0 
    R.append( (-ve*np.pi*np.power(prm.D_e*0.5, 2)) + (2*vs*np.pi*np.power(prm.D_s*0.5, 2)) )

    return np.array(R) # cast à array avant de renvoyer pour respecter out de la fonction 

def newton_numerique(x,tol,prm):
    """Fonction résolvant le système d'équations avec la méthode de Newton et un jacobien numérique
    
    Entrées:
        - x : Vecteur (array ou list) des estimés initiaux
            - x[0] : Vitesse d'entrée (boyau) [m/s]
            - x[1] : Vitesse de sortie (propulseur) [m/s]
            - x[2] : Angle d'inclinaison des propulseurs [rad]
        - tol : critère d'arrêt
        - prm : objet class parametres()
            - g : accélération gravitationnelle [m/s^2]
            - rho : masse volumique [kg/m^3]
            - D_e : diamètre d'entrée [m]
            - D_s : diamètre de sortie [m]
            - m : masse [kg]
            - F : force du vent [N]
    
    Sortie:
        - Vecteur (array) contenant les solutions
            - vecteur[0] : solution de la vitesse d'entrée [m/s]
            - vecteur[1] : solution de la vitesse de sortie [m/s]
            - vecteur[2] : solution de la vitesse de l'angle d'inclinaison [rad]
    """
    
    # Fonction à écrire
    
    return # à compléter