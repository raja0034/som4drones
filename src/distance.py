import numpy as np

def select_closest(candidates, origin):
    """Return the index of the closest candidate to a given point."""
    return euclidean_distance(candidates, origin).argmin()

def euclidean_distance(p1, p2):
    """Return the array of distances of two numpy arrays of points."""
    squared_dist = np.sum((p1 - p2)**2)
    distance = np.sqrt(squared_dist)
    #print(f"Distance between points ({p1}) and ({p2}) is {distance:.2f} units.")
    return distance

def boundary_distance(locations):
    """Return the cost of placing all locations on a boundary in a certain order."""
    points = locations[['X', 'Y', 'Z']]
    distances = euclidean_distance(points, np.roll(points, 1)) #, axis=0))
    return np.sum(distances)
