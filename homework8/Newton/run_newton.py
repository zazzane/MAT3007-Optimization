import numpy as np
import matplotlib.pyplot as plt
from gradient import gradient
from hessian import hessian
from armijo_backtracking import armijo_backtracking

# Common parameters
x = np.array([0.0, 0.0])  # initial point
epsilon = 1e-5  # stopping criteria
maxiter = 200  # max iteration
iter = 0

# Parameters for Armijo backtracking
sigma = 0.5
gamma = 0.5
t = 1  # initial step size in line search

# Function
def f(x):
    return np.exp(1 - x[0] - x[1]) + np.exp(x[0] + x[1] - 1) + x[0]**2 + x[0]*x[1] + x[1]**2 + x[0] - 3*x[1]

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

# Newton's method
while np.linalg.norm(gradient(x)) > epsilon:
    # Form the search direction d using the "gradient" and "hessian" functions
    grad = gradient(x)
    hess = hessian(x)
    d = -np.linalg.inv(hess) @ grad
    
    # Assign the step size using the "armijo_backtracking" function
    alpha_k = armijo_backtracking(f, x, d, sigma, gamma, t)
    
    # Newton's update x to xtemp
    xtemp = x + alpha_k * d
    
    # Make plots
    plt.plot(x[0], x[1], '*r')
    plt.plot([x[0], xtemp[0]], [x[1], xtemp[1]], '-g')
    plt.draw()
    plt.pause(0.1)
    
    # Output the solution in each step
    iter += 1
    x = xtemp


# Plot the final solution with Title
plt.title('Solution Plot for Newton\'s method')
plt.plot(x[0], x[1], '*r')
plt.ioff()
plt.show()


print(f'The algorithm ends after {iter} iterations\n x*=[{x[0]},{x[1]}]\n f(x*)={f(x)}\n gradient norm={np.linalg.norm(gradient(x))}')