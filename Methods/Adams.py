import numpy as np


def adams(x, initial_y, f):
    n = x.shape[0]
    y = np.zeros(n)

    for i in range(4):
        y[i] = initial_y[i]
    for i in range(4, n):
        h = x[i] - x[i - 1]
        fi1 = f(x[i - 1], y[i - 1])
        fi2 = f(x[i - 2], y[i - 2])
        fi3 = f(x[i - 3], y[i - 3])
        fi4 = f(x[i - 4], y[i - 4])
        y[i] = y[i - 1] + (h / 24.0) * (55.0 * fi1 - 59.0 * fi2 + 37.0 * fi3 - 9.0 * fi4)
    return y