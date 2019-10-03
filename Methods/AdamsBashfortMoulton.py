import numpy as np


def abm(x, initial_y, f):
    n = x.shape[0]
    y = np.zeros(n)
    h = x[1]-x[0]
    for i in range(4):
        y[i] = initial_y[i]
    for i in range(4, n):

        fi1 = f(x[i - 1], y[i - 1])
        fi2 = f(x[i - 2], y[i - 2])
        fi3 = f(x[i - 3], y[i - 3])
        fi4 = f(x[i - 4], y[i - 4])
        _yi = y[i - 1] + h * (55*fi1-59*fi2+37*fi3-9*fi4)/24
        y[i] = y[i - 1] + h*(9*f(x[i],_yi) + 19*fi1 - 5*fi2 + fi3)/24
    return y