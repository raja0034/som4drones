import matplotlib.pyplot as plt
import matplotlib as mpl

def plot_network(locations, neurons, name='diagram.png', ax=None):
    """Plot a graphical representation of the problem"""
    mpl.rcParams['agg.path.chunksize'] = 10000

    if not ax:
        fig = plt.figure(figsize=(5, 5), frameon = False)
        axis = fig.add_axes([0,0,1,1])

        axis.set_aspect('equal', adjustable='datalim')
        plt.axis('off')

        axis.scatter(locations['X'], locations['Y'], c=locations['Z'], cmap="viridis", s=50, alpha=0.7)
        axis.plot(neurons[:,0], neurons[:,1], 'r.', ls='-', color='#0063ba', markersize=2)

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Scatter Plot of XYZ Coordinates')
        # plt.colorbar(label='Z')  # Optional: Add a colorbar for Z values

        plt.savefig(name, bbox_inches='tight', pad_inches=0, dpi=200)
        plt.close()

    else:
        ax.scatter(locations['X'], locations['Y'], color='red', s=4)
        ax.plot(neurons[:,0], neurons[:,1], 'r.', ls='-', color='#0063ba', markersize=2)
        return ax

def plot_boundary(locations, boundary, name='diagram.png', ax=None):
    """Plot a graphical representation of the boundary obtained"""
    mpl.rcParams['agg.path.chunksize'] = 10000

    if not ax:
        fig = plt.figure(figsize=(5, 5), frameon = False)
        axis = fig.add_axes([0,0,1,1])

        axis.set_aspect('equal', adjustable='datalim')
        plt.axis('off')

        axis.scatter(locations['X'], locations['Y'], c=locations['Z'], cmap="viridis", s=50, alpha=0.7)
        boundary = locations.reindex(boundary)
        boundary.loc[boundary.shape[0]] = boundary.iloc[0]
        axis.plot(boundary['X'], boundary['Y'], color='purple', linewidth=1)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Scatter Plot of XYZ Coordinates with boundary')
        # plt.colorbar(label='Z')  # Optional: Add a colorbar for Z values

        plt.savefig(name, bbox_inches='tight', pad_inches=0, dpi=200)
        plt.close()

    else:
        ax.scatter(locations['X'], locations['Y'], color='red', s=4)
        boundary = locations.reindex(boundary)
        boundary.loc[boundary.shape[0]] = boundary.iloc[0]
        ax.plot(boundary['X'], boundary['Y'], color='purple', linewidth=1)
        return ax
