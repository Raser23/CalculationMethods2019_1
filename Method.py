import numpy as np
class Method:
    def __init__(self, x0, xN, k, N, method_f, p,
                 require_additional=False, fi=None, dfi=None, name='y2',
                 _lambda=0.1, is_iter=False, starter=None, y_num_to_start=1):
        self.x0 = x0
        self.xN = xN
        self.k = k
        self.N = N
        self.require_additional = require_additional
        self.method_f = method_f
        self.fi = fi
        self.dfi = dfi
        self.name = name
        self._lambda = _lambda
        self.is_iter = is_iter
        self.starter = starter
        self.p = p
        self.y_num_to_start = y_num_to_start

    def calculate(self, initial_y, f, x0=None, xN=None, N=-1):
        if N == -1:
            N = self.N

        if x0 is None:
            x0 = self.x0
        if xN is None:
            xN = self.xN

        result = np.zeros(N)
        nodes = np.linspace(x0, xN, N)
        if not (self.starter is None):
            x0_starter = self.x0
            xN_starter = nodes[self.y_num_to_start - 1]
            initial_y = self.starter.calculate(initial_y, f, x0=x0_starter, xN=xN_starter, N=self.y_num_to_start)
        print(initial_y)
        nodes = np.linspace(x0, xN, N)

        if self.require_additional:
            result = self.method_f(nodes, initial_y, f, self.fi, self.k, self.dfi)
        elif self.is_iter:
            result = self.method_f(nodes, initial_y, self._lambda, f)
        else:
            result = self.method_f(nodes, initial_y, f)
        return result

    def form_title(self):
        result = ''
        if self.require_additional:
            result = self.name + ', N = ' + str(self.N)
        elif self.is_iter:
            result = self.name + ', L=' + str(self._lambda) + ',N = ' + str(self.N)
        else:
            result = self.name + ', N = ' + str(self.N)
