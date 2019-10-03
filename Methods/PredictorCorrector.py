import numpy as np


def predictor_corrector(x, initial_y, l, f):
    n = x.shape[0]
    h = x[1] - x[0]
    y = np.zeros(n)
    y[0] = initial_y[0]
    printed = False
    for i in range(1, n):
        xi1 = x[i - 1]
        yi1 = y[i - 1]
        fi1 = f(xi1, yi1)

        ys1 = yi1 + h * fi1
        ys2 = y[i - 1] + (fi1 + f(x[i],ys1)) * (h/2)

        iter = 0
        while abs(ys1 - ys2)/abs(ys1) <= l:
            iter+=1
            ys1 = ys2
            ys2 = y[i - 1] + (fi1 + f(x[i], ys2)) * (h / 2)

            if iter >= 1000:
                if not printed:
                    print("overload 1000")
                    printed = True
                break
        y[i] = ys2
    return y