import numpy as np
import matplotlib.pyplot as plt

N = 2 ** 10
_N = 2 ** 8

draw_step = int(N/_N)

k = 0
x0 = -1
xN = 2


def fi(x):
    return np.sin(np.exp(x))


def dfi(x):
    return np.exp(x) * np.cos(np.exp(x))


def f(x, y):
    return dfi(x) + k * (y - fi(x))

'''
nodes = np.linspace(x0, xN, N)
y_fi = fi(nodes)

y_euler = euler_method(nodes, fi(x0))
y_adams = adams(nodes,y_fi[:4])
y_pc = predictor_corrector(nodes,fi(x0),0.01)
y_abm = abm(nodes,y_fi[:4])


fig = plt.figure()

print("start drawing")

plt.plot(nodes[::draw_step], y_fi[::draw_step], label='y_fi', linewidth=1)
#plt.plot(nodes[::draw_step], y_adams[::draw_step], label='y_adams', linewidth=1)
#plt.plot(nodes[::draw_step], y_pc[::draw_step], label='y_pc', linewidth=1)
plt.plot(nodes[::draw_step], y_abm[::draw_step], label='y_abm', linewidth=1)

plt.legend(loc='upper right')

plt.show()
'''