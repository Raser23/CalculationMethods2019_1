import numpy as np


def euler(nodes, initial_y, f):
    n = nodes.shape[0]
    y = np.zeros(n)
    y[0] = initial_y[0]

    for i in range(1, n):
        y[i] = y[i - 1] + (nodes[i] - nodes[i - 1]) * f(nodes[i - 1], y[i - 1])
    return y
