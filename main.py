## TP 6 


def distance_euclidienne(point1 : int, point2 : int) -> float :
    """
    Calcule la distance euclidienne entre deux points.
    
    Args :
        point1 (int) : Coordonnée du premier point.
        point2 (int) : Coordonnée du deuxième point.
    Returns :
        float : Distance euclidienne entre les deux points.    
    """
    sum = 0
    for i in range(len(point1)):
        sum += (point1[i] - point2[i])** 2
    return sum 


