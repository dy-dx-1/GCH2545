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
  
    # Étant donné qu'une approximation d'ordre 2 est imposée ET qu'on demande de prioriser l'utilisation de 2 points, 
    # il faudra utiliser la méthode pas arrière ordre 2, pas avant ordre 2 et la méthode centrée afin de bien évaluer la dérivée 
    # au départ de l'intervalle (3pts, pas avant), à la fin de celui-ci (3pts, pas arrière) et entre les 2 (2pts, centrée)
    # dans notre cas le delta de temps est constant donc on n'a pas à toucher au domaine! On ne jouera que sur les indices 
    vitesse = []
    for i in range(len(h)): 
      if i==0: # si première itération utiliser pas avant 
          v = (-h[i+2] + (4*h[i+1]) - (3*h[i]))/(2*dt)
      elif i==len(h)-1: # si dernière itération utiliser pas arrière 
          v = ((3*h[i]) - (4*h[i-1]) + (h[i-2]))/(2*dt)
      else: # on est au milieu donc entourés de pts, utiliser approche centrée 
          v = (h[i+1]-h[i-1])/(2*dt) 
      vitesse.append(v) 
    return vitesse

#-------------------------------------Fonction diff2()-----------------------#
def diff2(h,dt):
    """Fonction qui calcule la dérivée seconde
    
    Entrées:
      - h : h du liquide, sera un vecteur (array), de longueur quelconque
      - dt : pas de temps [float]
    
    Sortie:
      - Vecteur (array) contenant les valeurs numériques de la dérivée seconde
    """
    # Je vais procèder de la même façon qu'à la fonction de diff1 en utilisant les méthodes de pas avant, arrière et centrée selon l'indice analysé 
    # domaine et pas tjrs les mêmes 
    acceleration = []
    for i in range(len(h)): 
      if i==0: # si première itération utiliser pas avant 
          a = (h[i+2]-(2*h[i+1])+h[i])/(dt**2)
      elif i==len(h)-1: # si dernière itération utiliser pas arrière 
          a = (h[i]-(2*h[i-1])+h[i-2])/(dt**2)
      else: # on est au milieu donc entourés de pts, utiliser approche centrée 
          a = (h[i+1]-(2*h[i])+(h[i-1]))/(dt**2)
      acceleration.append(a) 
    return np.array(acceleration) 
      

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
      - h : h du liquide, sera un vecteur (array), de longueur quelconque
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