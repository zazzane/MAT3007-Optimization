import numpy as np

def hessian(x):
    hess = np.zeros((2, 2))
    hess[0, 0] = np.exp(1 - x[0] - x[1]) + np.exp(x[0] + x[1] - 1) + 2
    hess[0, 1] = -np.exp(1 - x[0] - x[1]) + np.exp(x[0] + x[1] - 1) + 1
    hess[1, 0] = hess[0, 1]
    hess[1, 1] = np.exp(1 - x[0] - x[1]) + np.exp(x[0] + x[1] - 1) + 2
    return hess