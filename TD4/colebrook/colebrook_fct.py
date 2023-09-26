# Importation des modules
import numpy as np

def f(l,cst):
    """Calcul de la fonction de lambda
    
    Entrées:
        - l : Coefficient de friction lambda [-]
        - cst : objet class constantes
            - Re : Nombre de Reynolds [-]
            - k : Rugosité [m]
            - D : diamètre de la conduite [m]
    
    Sortie:
        - Valeur numérique de la fonction
        
    """  
    log = np.log10( (cst.k/(3.7*cst.D)) + (2.51/(cst.Re*np.sqrt(l))) )
    return (1/np.sqrt(l)) + (2*log)      # tel que f(lambda) = [equation avec lambda] = 0 

def bissection(x1,x2,tol,N,cst):
    """Fonction calculant une racine d'une fonction grâce la bissection
    
    Entrées:
        - x1 : estimé initial, borne inférieure
        - x2 : estimé initial, borne supérieure
        - tol : critère d'arrêt
        - N : nombre maximal d'itérations possible
        - cst : objet class constantes
            - Re : Nombre de Reynolds [-]
            - k : Rugosité [m]
            - D : diamètre de la conduite [m]
    
    Sortie:
        - Valeur numérique de la racine de la fonction
    
    """
    
    # Fonction à écrire
    
    return # à compléter
