# Importation de modules
import numpy as np

def fonc(y,prm):
    """Fonction de calcul de la valeur du résidu des deux équations différentielles du premier ordre.

    Entrées:
        - y : Variables dépendantes
            - [0] : Position x
            - [1] : Vitesse v
        - prm : objet class parametres
            - k : Constante de rappel du ressort [N/m]
            - m : Masse accroché au ressort [kg]

    Sortie:
        - Vecteur (array) composé des valeurs numériques des équations différentielles
    """
    # On ici on n'utilise que des schémas explicites donc notre résidu est juste l'évaluation des dérivées pour une certaine variable dépendante
    x, v = y[0], y[1] 
    dx_dt = v 
    dv_dt = -(prm.k/prm.m)*x 
    return np.array([dx_dt, dv_dt]) 

def euler_explicite(ci,dt,tf,prm):
    """Fonction de résolution par la méthode d'Euler explicite

    Entrées:
        - ci : Conditions initiales
            - [0] : x0
            - [1] : v0
        - dt : Pas de temps
        - tf : Temps de simulation
        - prm : objet class parametres
            - k : Constante de rappel du ressort [N/m]
            - m : Masse accroché au ressort [kg]

    Sorties (dans l'ordre énuméré ci-bas):
        - Matrice (array) des solutions en fonction du temps
            - Chaque ligne représente une solution au système à un temps donnée
            - Chaque colonne représente les solutions dans le temps d'une variable
        - Vecteur (array) du temps de simulation
    """
    # Euler explicite est simple à implémenter, on n'a qu'à itérer sur le temps et évaluer la valeur des variables à chaque pas 
    t = 0 
    yt = ci         # on commence nos solutions avec les conditions initiales 
    sols = [ci] 
    temps = [t] 
    while t<=tf: 
        # on fait l'évaluation du prochain pas avec la forme matricielle pour avoir une méthode générale à n dimensions 
        #  c'est juste l'expression de la dérivée explicite, avec le prochain pas isolé
        ytdt = yt + dt*fonc(yt, prm) 
        yt = ytdt # maintenant on passe au prochain pas 
        t+=dt 
        sols.append(ytdt) 
        temps.append(t) # on enregistre le temps auquel on a évalué ytdt 
    return np.array(sols), np.array(temps) 

def rk2(ci,dt,tf,prm):
    """Fonction de résolution par la méthode de Runge Kutta d'ordre 2

    Entrées:
        - ci : Conditions initiales
            - [0] : x0
            - [1] : v0
        - dt : Pas de temps
        - tf : Temps de simulation
        - prm : objet class parametres
            - k : Constante de rappel du ressort [N/m]
            - m : Masse accroché au ressort [kg]

    Sorties (dans l'ordre énuméré ci-bas):
        - Matrice (array) des solutions en fonction du temps
            - Chaque ligne représente une solution à un temps donnée
            - Chaque colonne représente les solutions dans le temps d'une variable
        - Vecteur (array) du temps de simulation
    """

    # Fonction à écrire

    return # à compléter

def verlet(ci,dt,tf,prm):
    """Fonction de résolution par la méthode de Verlet

    Entrées:
        - ci : Conditions initiales
            - [0] : x0
            - [1] : v0
        - dt : Pas de temps
        - tf : Temps de simulation
        - prm : objet class parametres
            - k : Constante de rappel du ressort [N/m]
            - m : Masse accroché au ressort [kg]

    Sorties (dans l'ordre énuméré ci-bas):
        - Matrice (array) des solutions en fonction du temps
            - Chaque ligne représente une solution à un temps donnée
            - Chaque colonne représente les solutions dans le temps d'une variable
        - Vecteur (array) du temps de simulation
    """

    # Fonction à écrire

    return # à compléter

def energie(x,v,prm):
    """Fonction de calcul de l'énergie totale du système

    Entrées:
        - x : Vecteur position
        - v : Vecteur vitesse
        - prm : objet class parametres
            - k : Constante de rappel du ressort [N/m]
            - m : Masse accroché au ressort [kg]

    Sortie:
        - Vecteur (array) composé de l'énergie du système
    """

    # Fonction à écrire

    return # à compléter
