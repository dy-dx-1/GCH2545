#Importation des modules
import numpy as np

##TODO: confirm if they dont want immediate return for all functions 

# Fonctions pour construire les vecteurs x et f
def faire_vecteur_x():
    """Fonction qui génère un vecteur x allant de 0 à 5 avec 101 points
    
    Sortie:
        - Un np.array contenant 101 nombres allant de 0 à 5 inclusivement
    """

    return np.linspace(0, 5, 101) 

def faire_vecteur_f():
    """Fonction qui génère un vecteur f(x)=x^2 en employant le vecteur f

    Sortie:
        - Un np.array contenant 101 chiffre contenant x^2 pour x appartenant à [0,5]
    """

    return np.array([x**2 for x in faire_vecteur_x()])

# Fonction pour construire la matrice du système d'équations
def faire_matrice():
    """Fonction qui génère une matrice pour le système d'équations suivant:
        2x - 5y + 3z = 8
        3x -  y + 4z = 7
         x + 3y + 2z = -3
    
    Sortie:
        - Une matrice (np.array) correspondant au système d'équations.
    """
    
    return np.array([[2, -5, 3],
                    [3, -1, 4], 
                    [1,  3, 2]])

# Fonction pour construire le membre de droite du système d'équations
def faire_second_membre():
    """Fonction qui génère le second membre pour le système d'équations suivant:
        2x - 5y + 3z = 8
        3x -  y + 4z = 7
         x + 3y + 2z = -3 

    Sortie:
        - Un np.array array contenant 3 nombres
    """

    return [8,
            7,
           -3]