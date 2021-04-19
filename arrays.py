"""
Move zero to right
Avec une liste d'entiers L en entrée, 
retourner une liste en bougeant les zéros vers la droite et sans altérer l'ordre original de la liste
"""
# Ma solution
def move_zeros(array):
    filtered = list(filter(None, array))
    zeros = [0] * (len(array) - len(filtered))
    return filtered + zeros
