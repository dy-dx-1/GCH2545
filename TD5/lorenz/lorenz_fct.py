# Importation des modules
import numpy as np

def fonc(v,prm):
    """Fonction calculant le système d'équations
    Entrées:
        - v : Variables inconnues
            - [0] = x
            - [1] = y
            - [2] = z
        - prm : Objet class parametres()
            - o : sigma
            - b : beta
            - p : rho

    Sortie:
        - Vecteur (array) contenant les valeurs numériques du système d'équations
    """
    x, y, z = v[0], v[1], v[2] 
    
    dx_dt = prm.o * (y - x)
    dy_dt = prm.p*x - y - x*z 
    dz_dt = x*y - prm.b*z 
    return np.array([dx_dt, dy_dt, dz_dt]) 

def rk4(ci,dt,tf,prm):
    """Fonction résolvant le système avec Runge-Kutta 4
    Entrées:
        - ci : Conditions initiales
            - [0] = x
            - [1] = y
            - [2] = z
        - dt : Pas de temps
        - tf : Temps final de simulation
        - prm : Objet class parametres()
            - o : sigma
            - b : beta
            - p : rho

    Sorties (dans l'ordre énuméré ci-bas):
        - Matrice (array) des solutions dans le temps, incluant les conditions initiales
            - Chaque ligne représente les solutions (x,y,z) à un temps donné
            - Chaque colonne représente l'évolution d'une coordonnée dans le temps
        - Vecteur (array) du temps de simulation, allant de 0 à tf exclu
    """
    t = 0 
    y_t = ci # commencons notre vecteur solution aux conditions initiales
    sols, temps = [ci], [t]
    while t<tf: 
        # En premier on doit évaluer les facteurs k 
        # Notons que comme les éléments de notre fonction fonc ne contiennent pas de variable indépendante, on n'a pas besoin 
        # de tenir compte de 't' ou 't+deltat/2' mais plutôt juste des yt 
        k1 = dt*fonc(y_t, prm) 
        k2 = dt*fonc(y_t + (k1/2), prm) 
        k3 = dt*fonc(y_t + (k2/2), prm) 
        k4 = dt*fonc(y_t + k3, prm)
        # Maintenant évaluons le prochain y puis enregistrons le comme notre prochain guess 
        y_tdt = y_t + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        y_t = y_tdt 
        t += dt  
        sols.append(y_tdt) 
        temps.append(t) 

    return np.array(sols), np.array(temps) 