import pandas as pd
import numpy as np

def read_tsp(filename):
    """
    Read a file in .tsp format into a pandas DataFrame
    """
    with open(filename) as f:
        node_coord_start = None
        dimension = None
        lines = f.readlines()

        # Obtain the information about the .tsp
        i = 0
        while not dimension or not node_coord_start:
            line = lines[i]
            if line.startswith('DIMENSION :'):
                dimension = int(line.split()[-1])
            if line.startswith('NODE_COORD_SECTION'):
                node_coord_start = i
            i = i+1

        print('Problem with {} locations read.'.format(dimension))

        f.seek(0)

        # Read a data frame out of the file descriptor
        locations = pd.read_csv(
            f,
            skiprows=node_coord_start + 1,
            sep=' ',
            names=['location', 'y', 'x'],
            dtype={'location': str, 'x': np.float64, 'y': np.float64},
            header=None,
            nrows=dimension
        )

        # locations.set_index('location', inplace=True)

        return locations

def normalize(points):
    """
    Return the normalized version of a given vector of points.
    """
    ratio = (points.x.max() - points.x.min()) / (points.y.max() - points.y.min()), 1
    ratio = np.array(ratio) / max(ratio)
    norm = points.apply(lambda c: (c - c.min()) / (c.max() - c.min()))
    return norm.apply(lambda p: ratio * p, axis=1)
