import numpy as np

from distance import select_closest

def generate_network(size):
    """
    Generate a neuron network of a given size.

    Return a vector of two dimensional points in the interval [0,1].
    """
    return np.random.rand(size, 3)

def get_neighborhood(center, radix, domain):
    """Get the range gaussian of given radix around a center index."""

    # Impose an upper bound on the radix to prevent NaN and blocks
    if radix < 1:
        radix = 1

    # Compute the circular network distance to the center
    deltas = np.absolute(center - np.arange(domain))
    distances = np.minimum(deltas, domain - deltas)

    # Compute Gaussian distribution around the given center
    return np.exp(-(distances*distances) / (2*(radix*radix)))

def get_boundary(locations, network):
    """Return the boundary computed by a network."""
    locations['winner'] = locations[['X', 'Y', 'Z']].apply(
        lambda c: select_closest(network, c),
        axis=1, raw=True)

    return locations.sort_values('winner').index
