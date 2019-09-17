import numpy as np


def gir(x, initial_y, f, fi, k, dfi):
    n = x.shape[0]
    y = np.zeros(n)
    h = x[1] - x[0]
    y[0:4] = initial_y
    for i in range(4, n):
        y[i] = (1/(25-12*k*h)) * (48 * y[i-1] - 36 * y[i-2] + 16 * y[i-3] - 3*y[i-4] + 12*h*dfi(x[i]) - 12*h*k * fi(x[i]))

    return y