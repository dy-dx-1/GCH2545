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
    
    # Fonction à écrire
    
    return # à compléter

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