# Importation des modules
import numpy as np

def acc(v,dt):
    """Fonction qui calcule l'accélération à partir de la vitesse

    Entrées:
        - v : La vitesse mesurée, vecteur (array) [m/s]
        - dt : Le pas de temps [s]

    Sortie:
        - Vecteur de valeur numérique de l'accélération instantanée au temps t [m/s^2]
    """
    # Accel est derivée de vitesse et on veut une approx d'ordre 2 --> je fais comme au td2 avec un mix 
    # de techniques centrée, arrière et avant ordre 2 
    accel = list() 
    for i in range(len(v)): 
        if i == 0: # si premiere iter utiliser pas avant 
            a = (-v[i+2] + 4*v[i+1] - 3*v[i]) 
        elif i==len(v)-1: # si on est derniere iter utiliser pas arriere 
            a = (3*v[i] - 4*v[i-1] + v[i-2]) 
        else:
            a = v[i+1] - v[i-1]
        accel.append(a/(2*dt)) 
    return np.array(accel) 

def force_poussee(v,a,cst):
    """Fonction qui calcule la force de poussée nécessaire

    Entrées:
        - v : La vitesse mesurée, vecteur (array) [m/s]
        - a : L'accélération de l'avion, vecteur (array) [m/s^2]
        - cst : Objet de class constantes() avec les valeurs suivantes
            - rho : La densité de l'air [kg/m^3]
            - S : La surface de référence [m^2]
            - C : Le coefficient de traînée [-]
            - m : La masse de l'avion [kg]

    Sortie:
        - Vecteur de valeurs numériques de la force de poussée nécessaire
            pour l'accélération de l'avion [N]
    """
    #### BILAN DE FORCESSS 
    # SUM(Fx) = m*ax  ; axe x positif -> aligné avec le vecteur allant de la queue à la tête de l'avion 
    # Poussee - Trainee = m* ax 
    # Poussee = m * ax + Trainee 
    ## On veut avoir la F nécéssaire pour chaque étape du parcours, donc un array de forces évaluées pour chaque vitesse et accel jusqu'à 30s 
    # Trainee@1 pt = 0.5 * rho * v**2 * S * Cx 
    drags = 0.5 * cst.rho * np.power(v, 2) * cst.S * cst.C # L'utilisation de l'array v produira un array de drags pr chaque étape 
    inertie = cst.m * a # L'utilisation de l'array a produira un array d'inerties 
    poussee = drags + inertie # Array des poussées 
    return poussee

def trapeze(x,y):
    """Fonction qui calcule l'intégrale avec la méthode des trapèzes

    Entrées:
        - x : Valeurs de l'abscisse, vecteur (array)
        - y : Valeurs de l'ordonnée, vecteur (array)

    Sortie:
        - Valeur de l'intégrale calculée (float)
    """
    # Rappel: aire trapèze = 0.5 * base(h1 + h2)
    # On n'a qu'à appliquer la méthode des trapèzes composés directement, car elle prend un 'pas avant' et s'arrête bien avant de manquer de pts 
    # il faut faire attention au fait que la base n'est pas constante partout 
    return sum(((0.5 * (x[i+1]-x[i]) * (y[i+1]+y[i])) for i in range(len(x)-1)))  # utilisation d'un generateur car on n'a pas besoin des sommes intermediaires

def simpson(x,y):
    """Fonction qui calcule l'intégrale selon Simpson 1/3
    
    Entrées:
        - x : Les abcisses de la courbe étudiée, vecteur (array)
        - y : Les ordonnées de la courbe étudiée, vecteur (array)
    
    Sortie:
        - Valeur numérique de l'intégrale
    """
    
    # Encore une fois, on n'a qu'à appliquer la méthode directement en faisant attention au pas variable 
    # L'utilisation d'un generateur devient encore une fois pratique pour ce type de calcul
    N = int((len(x)-1) / 2) 
    return sum(( (x[(2*i)+1]-x[2*i])*(y[2*i] + (4*y[(2*i)+1]) + y[(2*i)+2]) for i in range(N))) / 3 