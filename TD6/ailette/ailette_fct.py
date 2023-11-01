# Importation des modules
import numpy as np

def mdf(prm):
    """Fonction qui calcule le profil de température le long de l'ailette

    Entrées:
        - prm : Objet class parametres()
            - L : Longueur
            - D : Diamètre
            - k : Conductivité thermique
            - T_a : Température ambiante
            - T_w : Température du mur
            - h : Coefficient de convection
            - N : Nombre de points utilisés pour la méthode

    Sorties (dans l'ordre énuméré ci-bas):
        - Vecteur (np.array) donnant la température tout au long de l'ailette en Kelvin
        - Vecteur (np.array) donnant la position tout au long de l'ailette (axe z) en mètre
    """

    # Fonction à écrire

    return # à compléter

def inte(T,z,prm):
    """Fonction qui intègre la convection sur la surface de l'ailette.

    Entrées:
        - T : Vecteur comprenant les températures  en Kelvin sur la longueur de l'ailette
                pour une combinaison géométrique donnée
        - z : Vecteur comprenant les points sur la longueur en mètre
        - prm : Objet class parametres()
            - k : Conductivité thermique
            - T_a : Température ambiante
            - T_w : Température du mur
            - h : Coefficient de convection
            - N : Nombre de points utilisés pour la méthode

    Sortie:
        - Valeur numérique de l'intégrale résultante (perte en W)
    """


    # Fonction à écrire
    I=0

    return I# à compléter
