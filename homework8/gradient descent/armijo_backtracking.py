def armijo_backtracking(f, x, d, alpha, beta, t):
    alpha_k = t
    while f(x + alpha_k * d) > f(x) + alpha * alpha_k * d.T @ d:
        alpha_k *= beta  # update the step size
    return alpha_k