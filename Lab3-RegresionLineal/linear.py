def linreg(X, y, t, cost, grad, a=0.1, n=100, onStep=None):
    costs = []
    for i in range(n):
        t -= a * grad(X, y, t)
        # print(cost(X,t,t))
        costs.append(cost(X, y, t))

        if onStep:
            onStep(t)

    return t, costs
