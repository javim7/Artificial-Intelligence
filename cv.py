def generate_polynomial(X,k):
    if k ==1:
        return X
    elif k ==2:
        return np.hstack ((
            X, 
            X[:, 2] ** 2
        ))
    elif k ==10:
        return np.hstack ((
            X, 
            X[:, 2] ** 2, 
            X[:, 3] ** 3,
            X[:, 4] ** 10,
        ))

complexity = 10

X = shuffle(x)

costs = []

for k in range(1, complexity):
    Xc = generate_polynomial(x, k)
    m, n = Xc.shape


    Xt = Xc[0:int(m*0.4), :]
    Xcr = Xc[int(m*0.4):int(m*0.8), :]
    Xte = Xc[int(m*0.8):, :]

    To = randomize_T()
    Tt, Jt = grad_descent(Xt, Y, To, loss, loss_derivative)
    Jcr = loss(Xcr, Y, loss, loss_derivative)

    costs.append((k, Tt, Jt, Jcr))