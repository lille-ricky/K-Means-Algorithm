## TP 6 


def euclid_distance(point1 : int, point2 : int) -> float :
    """
    Calculates the euclidean distance between two points.
    
    Args :
        point1 (int) : Cpprdinates of the first point.
        point2 (int) : Coordinates of the second point.
    Returns :
        float : Euclidean distance between the two points.    
    """
    sum = 0
    for i in range(len(point1)):
        sum += (point1[i] - point2[i])** 2
    return sum 

def closest_cluster(point : int , centers : list) -> int :
    """
    Returns the index of the closest cluster to the given point
    Args :
        point (int) : Coordinates of the point.
        centers(list) : list of cluster centers.
    Returns :
        int : index of the closest cluster center.
    """
    min_distance = euclid_distance(point, centers[0])
    min_index = 0

    for i in range(1, len(centers)) :
        distance = euclid_distance(point, centers[i])
        if distance < min_distance :
            min_distance = distance
            min_index = i 
    return min_index 

def calculate_centers(points : list) -> int :
    """
    Calculates the central inertia of the clusters.
    Args : 
        points (list) : list of points 
    Returns : 
        int : central inertia of the clusters.
    """

    if len(points) == 0 :
        return 0
    n_dim = len(points[0])
    center = [0.0] * n_dim

    for point in points :
        for i in range(n_dim) :
            center[i] += point[i]
    
    for i in range(n_dim) :
        center[i] /= len(points)

    return center