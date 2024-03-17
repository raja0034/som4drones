import pandas as pd
import numpy as np

def read_xyz(filename):
    """
    Read a file in .xyz format into a pandas DataFrame
    """
    df = pd.read_csv(filename)
    df.columns = ["X", "Y", "Z"]
    return df

def normalize(points):
    """
    Normalizes a vector of 3D coordinates to be within [0, 1].
    
    Args:
        coordinates (numpy.ndarray): A 2D array where each row represents a 3D coordinate (x, y, z).
    
    Returns:
        numpy.ndarray: Normalized coordinates.
    """
    coordinates = points.to_numpy()
    print(coordinates)
    # Find the minimum and maximum values for each coordinate
    min_x = min(coord[0] for coord in coordinates)
    max_x = max(coord[0] for coord in coordinates)
    min_y = min(coord[1] for coord in coordinates)
    max_y = max(coord[1] for coord in coordinates)
    min_z = min(coord[2] for coord in coordinates)
    max_z = max(coord[2] for coord in coordinates)

    # Normalize each coordinate
    normalized_coords = []
    for x, y, z in coordinates:
        norm_x = (x - min_x) / (max_x - min_x)
        norm_y = (y - min_y) / (max_y - min_y)
        norm_z = (z - min_z) / (max_z - min_z)
        normalized_coords.append((norm_x, norm_y, norm_z))

    return normalized_coords
