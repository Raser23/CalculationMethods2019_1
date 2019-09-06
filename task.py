import numpy as np
import matplotlib.pyplot as plt

N = 5000000
k = 4
x0 = -2
xN = 2


def fi(x):
    return np.sin(np.exp(x))


def dfi(x):
    return np.exp(x) * np.cos(np.exp(x))


def f(x, y):
    return dfi(x) + k*(y - fi(x))


def euler_method(nodes, y0):
    n = nodes.shape[0]
    y = np.zeros(n)
    y[0] = y0

    for i in range(1, n):
        y[i] = y[i-1] + (nodes[i] - nodes[i-1]) * f(nodes[i-1], y[i-1])
    return y

def Adams(nodes, initial_y):
    n = nodes.shape[0]
    y = np.zeros(n)

    for i in range(4):
        y[i] = initial_y[i]
    for i in range(1, n):
        h = nodes[i] - nodes[i-1]
        fi1 = f(nodes[i-1], y[i-1])
        fi2 = f(nodes[i-2], y[i-2])
        fi3 = f(nodes[i-3], y[i-3])
        fi4 = f(nodes[i-4], y[i-4])
        y[i] = y[i-1] + (h/24.0) * ( )




_x = np.linspace(x0, xN, N)
y = fi(_x)

yh = euler_method(_x, fi(x0))
fig = plt.figure()

plt.plot(_x, yh, label='line 1', linewidth= 1)
plt.plot(_x,y, label='line 2', linewidth= 1)
plt.legend(loc='upper right')

plt.show()
