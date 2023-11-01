# Importation des modules
import numpy as np

def mdf(prm):
    """Fonction simulant avec la méthode des différences finies

    Entrées:
        - prm : Objet class parametres()
            - Tr : Température à l'intérieur de la conduite [K]
            - Te : Température ambiante autour de la conduite [K]
            - k : Conductivité thermique [W*m^-1*K^-1]
            - h : Coefficient de convection thermique [W*m^-2*K^-1]
            - Re : Rayon externe [m]
            - Ri : Rayon interne [m]
            - n : Nombre de noeuds [-]
            - dr : Pas en espace [m]

    Sortie (dans l'ordre énuméré ci-bas):
        - Vecteur (array) de dimension N composé de la position radiale à laquelle les températures sont calculées, où N le nombre de noeuds.
        - Vecteur (array) de dimension N composé de la température en fonction du rayon, où N le nombre de noeuds
    """

    # Fonction à écrire

    return # à compléter
