from sys import argv

import numpy as np

from io_helper import read_xyz, normalize
from neuron import generate_network, get_neighborhood, get_boundary
from distance import select_closest, euclidean_distance, boundary_distance
from plot import plot_network, plot_boundary

def main():
    if len(argv) != 2:
        print("Correct use: python src/main.py <filename>.xyz")
        return -1

    problem = read_xyz(argv[1])

    boundary = som(problem, 100000)

    problem = problem.reindex(boundary)

    distance = boundary_distance(problem)

    print('Boundary found of length {}'.format(distance))


def som(problem, iterations, learning_rate=0.8):
    """Solve the xyz using a Self-Organizing Map."""

    # Obtain the normalized set of locations (w/ coord in [0,1])
    locations = problem.copy()
    # print(locations)
    #locations[['X', 'Y', 'Z']] = normalize(locations[['X', 'Y', 'Z']])

    # The population size is 8 times the number of locations
    n = locations.shape[0] * 8

    # Generate an adequate network of neurons:
    network = generate_network(n)
    print('Network of {} neurons created. Starting the iterations:'.format(n))

    for i in range(iterations):
        if not i % 100:
            print('\t> Iteration {}/{}'.format(i, iterations), end="\r")
        # Choose a random location
        location = locations.sample(1)[['X', 'Y', 'Z']].values
        winner_idx = select_closest(network, location)
        # Generate a filter that applies changes to the winner's gaussian
        gaussian = get_neighborhood(winner_idx, n//10, network.shape[0])
        # Update the network's weights (closer to the location)
        network += gaussian[:,np.newaxis] * learning_rate * (location - network)
        # Decay the variables
        learning_rate = learning_rate * 0.99997
        n = n * 0.9997

        # Check for plotting interval
        if not i % 1000:
            plot_network(locations, network, name='diagrams/{:05d}.png'.format(i))

        # Check if any parameter has completely decayed.
        if n < 1:
            print('Radius has completely decayed, finishing execution',
            'at {} iterations'.format(i))
            break
        if learning_rate < 0.001:
            print('Learning rate has completely decayed, finishing execution',
            'at {} iterations'.format(i))
            break
    else:
        print('Completed {} iterations.'.format(iterations))

    plot_network(locations, network, name='diagrams/final.png')

    boundary = get_boundary(locations, network)
    plot_boundary(locations, boundary, 'diagrams/boundary.png')
    return boundary

if __name__ == '__main__':
    main()
