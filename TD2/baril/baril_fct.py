# Importation des modules
import numpy as np

#-------------------------------------Fonction diff1()-----------------------#
def diff1(h,dt):
    """Fonction qui calcule la dérivée première
    
    Entrées:
      - h : hauteur du liquide, sera un vecteur (array), de longueur quelconque
      - dt : pas de temps [float]
    
    Sortie:
      - Vecteur (array) contenant les valeurs numériques de la dérivée première
    """
    
    # Fonction à écrire
    
    return # à compléter

#-------------------------------------Fonction diff2()-----------------------#
def diff2(h,dt):
    """Fonction qui calcule la dérivée seconde
    
    Entrées:
      - h : hauteur du liquide, sera un vecteur (array), de longueur quelconque
      - dt : pas de temps [float]
    
    Sortie:
      - Vecteur (array) contenant les valeurs numériques de la dérivée seconde
    """
    
    # Fonction à écrire
    
    return # à compléter

#------------------------------Fonction acceleration()-----------------------#
def acceleration(cst):
    """Fonction qui calcule l'accélération théorique de la surface libre
    
    Entrées:
      - Un objet contenant les constantes du problème
          - rc : rayon du cylindre
          - rv : rayon de l'ouverture
          - gamma : coefficient de correction
          - g : accélération gravitationnelle
    
    Sortie:
      - Valeur numérique théorique de l'accélération de la surface libre [float]
    """
        
    return ((cst.gamma*(cst.rv/cst.rc)**2)**2)*cst.g

#-----------------------------------Fonction vitesse()-----------------------#
def vitesse(h,cst):
    """Fonction qui calcule la vitesse théorique de la surface libre
    
    Entrées:
      - h : hauteur du liquide, sera un vecteur (array), de longueur quelconque
      - Un objet contenant les constantes du problème
          - rc : rayon du cylindre
          - rv : rayon de l'ouverture
          - gamma : coefficient de correction
          - g : accélération gravitationnelle
    
    Sortie:
      - Vecteur de valeurs numériques théoriques de la vitesse de la surface libre [array]
    """
    
    v = np.empty(len(h))
    
    for i in np.arange(len(h)):
        v[i] = -cst.gamma * ((cst.rv/cst.rc)**2) * np.sqrt(2 * cst.g * h[i])
    
    return v