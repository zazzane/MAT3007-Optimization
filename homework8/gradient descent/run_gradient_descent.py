import numpy as np
import matplotlib.pyplot as plt

# Common parameters
x = np.array([0, 0])  # initial point
epsilon = 1e-6  # stopping criteria
maxiter = 200  # max iteration
iter = 0

# Parameters for Armijo backtracking
sigma = 0.1
gamma = 0.7
t = 1  # initial step size in line search

# Function
def f(x):
    return np.exp(1 - x[0] - x[1]) + np.exp(x[0] + x[1] - 1) + x[0]**2 + x[0]*x[1] + x[1]**2 + x[0] - 3*x[1]

# Gradient function
def gradient(x):
    grad = np.zeros_like(x)
    grad[0] = -np.exp(1 - x[0] - x[1]) + np.exp(x[0] + x[1] - 1) + 2*x[0] + x[1] + 1
    grad[1] = -np.exp(1 - x[0] - x[1]) + np.exp(x[0] + x[1] - 1) + x[0] + 2*x[1] - 3
    return grad

# Armijo backtracking function
def armijo_backtracking(f, x, d, alpha, beta, t):
    alpha_k = t
    while f(x + alpha_k * d) > f(x) + alpha * alpha_k * d.T @ d:
        alpha_k *= beta  # update the step size
    return alpha_k

# Choose an algorithm
s = int(input("Which strategy to use?\n [1]: large constant stepsize\n [2]: small constant stepsize\n [3]: armijo backtracking\n"))

# Plot the contour of cost function
x1 = np.arange(-2.5, 0.5, 0.01)
x2 = np.arange(0, 3, 0.01)
n = len(x1)
z = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        z[n-1-i, n-1-j] = f([x1[i], x2[j]])
plt.figure(1)
plt.contour(x1, x2, z, 20)
plt.ion()
plt.show()

# Gradient descent algorithm
while np.linalg.norm(gradient(x)) > epsilon and iter <= maxiter:
    d = -gradient(x)
    
    if s == 1:
        alpha_k = 1  # large constant step size
    elif s == 2:
        alpha_k = 0.1  # small constant step size
    else:
        alpha_k = armijo_backtracking(f, x, d, sigma, gamma, t)
    
    xtemp = x + alpha_k * d
    
    # Make some plots
    plt.plot(x[0], x[1], '*r')
    plt.plot([x[0], xtemp[0]], [x[1], xtemp[1]], '-g')
    plt.draw()
    plt.pause(0.01)
    
    # Output the solution in each step
    iter += 1
    x = xtemp

# Print final information
print(f'The algorithm ends after {iter} iterations\n x*={x}\n f(x*)={f(x)}\n gradient norm={np.linalg.norm(gradient(x))}')