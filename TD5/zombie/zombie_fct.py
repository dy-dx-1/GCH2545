# Importation des modules
import numpy as np

def residu(y,yi,prm,dt):
    """Fonction calculant le résidu de la dynamique d'une invasion de zombie
    
    Entrées:
        - y : Variables dépendantes
            - [0] : S, humains susceptibles de devenir zombies
            - [1] : Z, zombies
            - [2] : R, retirés du bassin
        - yi : Estimés initiaux (même ordre que y)
        - prm : Objet class parametres()
            - e : taux de résurrection en zombie (zeta)
            - b : taux de transformation en zombie (beta)
            - a : taux de mort de zombie (alpha)
            - d : taux de mort naturelle (delta)
            - p : taux de naissance (pi)
        - dt : Pas de temps
    
    Sortie:
        - Vecteur (array) contenant les valeurs numériques du résidu
    """
    # Calculons les lignes 1 à 1 pour essayer de garder le tout clair 
    l1 = yi[0] - y[0] + dt*(prm.p - y[0] * (prm.b*y[1] + prm.d))
    l2 = yi[1] - y[1] + dt*(y[1]*y[0]*(prm.b-prm.a) + y[2]*prm.e)
    l3 = yi[2] - y[2] + dt*(-prm.e*y[2] + y[0]*(prm.d + prm.a*y[1])) 
    return np.array([l1, l2, l3])

def jacobien(y,prm,dt):
    """Fonction calculant le jacobien de la dynamique d'une invasion de zombie
    
    Entrées:
        - y : Variables dépendantes
            - [0] : S, humains susceptibles de devenir zombies
            - [1] : Z, zombies
            - [2] : R, retirés du bassin
        - prm : Objet class parametres()
            - e : taux de résurrection en zombie (zeta)
            - b : taux de transformation en zombie (beta)
            - a : taux de mort de zombie (alpha)
            - d : taux de mort naturelle (delta)
            - p : taux de naissance (pi)
        - dt : Pas de temps
    
    Sortie:
        - Matrice (array) contenant les valeurs numériques du jacobien
    """
    S, Z, R = y[0], y[1], y[2] 
    # calcul des dérivées partielles 
    dr1_ds = -1 -dt*(prm.b*Z+prm.d) 
    dr1_dz = -S*dt*prm.b 
    dr1_dr = 0 

    dr2_ds = dt*Z*(prm.b-prm.a) 
    dr2_dz = -1+S*dt*(prm.b-prm.a) 
    dr2_dr = dt*prm.e 

    dr3_ds = dt*(prm.d + prm.a*Z) 
    dr3_dz = dt*S*prm.a 
    dr3_dr = -1 - dt*prm.e 

    J = np.vstack(([dr1_ds, dr1_dz, dr1_dr],
                   [dr2_ds, dr2_dz, dr2_dr], 
                   [dr3_ds, dr3_dz, dr3_dr]))
    return J

def euler_implicite(ci,dt,tf,tol,prm):
    """Fonction calculant le résidu de la dynamique d'une invasion de zombie
    
    Entrées:
        - ci : Conditions initiales
            - [0] : S, humains susceptibles de devenir zombies
            - [1] : Z, zombies
            - [2] : R, retirés du bassin
        - dt : Pas de temps
        - tf : Temps final de simulation
        - tol : Critère d'arrêt
        - prm : Objet class parametres()
            - e : taux de résurrection en zombie (zeta)
            - b : taux de transformation en zombie (beta)
            - a : taux de mort de zombie (alpha)
            - d : taux de mort naturelle (delta)
            - p : taux de naissance (pi)
    
    Sorties (dans l'ordre énuméré ci-bas):
        - Matrice (array de taille (temps, 3)) des solutions de y en fonction du temps
        - Vecteur (array) du temps de simulation
    """
    solutions = [ci]
    temps = [0] 
    t = 0 # temps initial 
    y = np.copy(ci) # on commence notre vecteur solution avec les conditions initiales comme estimé 
    yi = np.copy(ci)  
    while t<tf: # on continue de calculer le prochain résultat sur tout le domaine temporel voulu 
        # Pour calculer les solutions à un temps t on doit résoudre un équa non linéaire venant du fait 
        # qu'on a utilisé euler implicite. Utilisons la méthode de Newton-Raphson pour résoudre chaque sol à chaque pas de temps 
        correction = np.ones(3) # valeur quelquonque plus grande que tol pour partir la méthode 
        while np.linalg.norm(correction)>tol: # on suppose une convergence
            # Résoudre le sys matriciel Jacobien résidu pour avoir la nouvelle correction 
            correction = np.linalg.solve(jacobien(y, prm=prm, dt=dt), -residu(y, yi, prm, dt))
            y += correction # on évalue le nouveau vecteur 
        yi = np.copy(y) # on set les estimés initiaux aux valeurs calculées précedemment 
        t+=dt # passer au prochain pas de temps  

        solutions.append(y) 
        temps.append(t) # contribution à liste de temps de simulation 
    return # à compléter