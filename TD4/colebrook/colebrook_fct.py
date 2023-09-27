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
    return -(1/np.sqrt(l)) - (2*log)      # tel que f(lambda) = [equation avec lambda] = 0 

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
    n=0 
    while abs(x2-x1)>tol and n<N: # Continuer à itérer tant que la dist entre les bornes est > que tolérance et qu'on dépasse pas le max d'itérations 
        # Déterminons le point milieu de notre intervalle, assumant qu'un zéro est présent à l'intérieur de celui-ci 
        xm = (x1+x2)/2 
        # Vérifions si le zéro est vers la droite ou la gauche de l'intervalle, puis réajustons le selon le cas 
        if f(x2, cst)*f(xm, cst) < 0: # si le zéro est à droite 
            x1 = xm 
        else:
            x2 = xm 
        n+=1 

    return xm if n!=N else None  # Retour de None si on a pas réussi à converger en N itérations 