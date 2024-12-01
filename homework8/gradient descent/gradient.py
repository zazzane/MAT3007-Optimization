import numpy as np

def gradient(x):
    grad = np.zeros_like(x)
    grad[0] = -np.exp(1 - x[0] - x[1]) + np.exp(x[0] + x[1] - 1) + 2*x[0] + x[1] + 1
    grad[1] = -np.exp(1 - x[0] - x[1]) + np.exp(x[0] + x[1] - 1) + x[0] + 2*x[1] - 3
    return grad