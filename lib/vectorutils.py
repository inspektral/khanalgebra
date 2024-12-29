import numpy as np
import matplotlib.pyplot as plt

def find_unit_vectors(vector: np.array):
    length = np.sqrt(np.sum(vector**2))
    return vector/length

def find_components_length_angle(length: float, angle: float, degrees: bool = True):
    if degrees:
        angle = angle/180 * np.pi
    x = length*np.cos(angle)
    y = length*np.sin(angle)
    return np.array([x,y])

def plot_vector(v, ref=(0,0), label="vector", color='r') :
    plt.quiver(ref[0], ref[1], v[0], v[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)


def showPlot(xlim=(-5, 5), ylim=(-5, 5), legend=True):
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)

    plt.xlim(*xlim)
    plt.ylim(*ylim)

    # Add grid, legend, and labels
    plt.grid()
    if legend:
        plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Vector Plot')
    plt.show()

def test():
    v = np.array([[1], [2]])
    plot_vector(v)
    showPlot()