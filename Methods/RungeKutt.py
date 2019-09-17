import numpy as np


def rk_a(x, initial_y, f):
    n = x.shape[0]
    y = np.zeros(n)
    h = x[1] - x[0]
    y[0] = initial_y[0]
    for i in range(1, n):
        k1 = f(x[i-1], y[i-1])
        k2 = f(x[i-1] + h/2, y[i-1] + k1/2)
        k3 = f(x[i-1] + h, y[i-1] - k1 + 2*k2)
        y[i] = y[i - 1] + h * (k1 + 4*k2 + k3)/6
    return y


def rk_b(x, initial_y, f):
    n = x.shape[0]
    y = np.zeros(n)
    h = x[1] - x[0]
    y[0] = initial_y[0]
    for i in range(1, n):
        k1 = f(x[i-1], y[i-1])
        k2 = f(x[i-1] + h/2, y[i-1] + k1/2)
        k3 = f(x[i-1] + h/2, y[i-1] + k2/2)
        k4 = f(x[i-1] + h, y[i-1] + k3)
        y[i] = y[i - 1] + h * (k1 + 2*k2 + 2*k3 + k4)/6
    return y
