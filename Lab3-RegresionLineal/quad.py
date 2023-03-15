def cost(X, y, t): return ((X @ t - y) ** 2).sum() / len(y)
def grad(X, y, t): return 2 * X.T @ (X @ t - y) / len(y)

# while True:
#  nabla = quad.grad(X, y, t)

#  if np.sqrt(nabla**2).sum() < threshold:
#   return t
