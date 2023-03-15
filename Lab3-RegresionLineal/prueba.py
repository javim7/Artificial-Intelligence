from dotenv import load_dotenv
import matplotlib.pyplot as plt
import numpy as np
import os
import quad
from linear import linreg


load_dotenv()
DATASET_SET_SIZE = int(os.environ['DATASET_SET_SIZE'])
DATASET_SPARSE_RATIO = int(os.environ['DATASET_SPARSE_RATIO'])
DATASET_X_LIM = int(os.environ['DATASET_X_LIM'])

# imaginemos que X es dado
X = np.linspace(0, DATASET_X_LIM, DATASET_SET_SIZE).reshape(
    (DATASET_SET_SIZE, 1))
Xr = np.hstack((
    np.ones((DATASET_SET_SIZE, 1)),
    X
))

y = 3 + 2 * X + np.random.randn(DATASET_SET_SIZE, 1) * DATASET_SPARSE_RATIO

#add polinomical feature
# Xr = np.hstack((
#     Xr,
#     X.reshape((Xr.shape[0], 1)) ** 2
# ))

# h(xv) = t0 * xv[0] + t1 * xv[1] + t2 * xv[1] ** 2

to = np.random.rand(Xr.shape[1], 1)
tf, costs = linreg(Xr, 
            y, 
            to, 
            quad.cost, 
            quad.grad, 
            a=0.001, 
            n=50,
        )

print("TF:", tf)
print(costs)

xm = np.array([[0], [DATASET_X_LIM]])

xmr = np.hstack((
    np.ones((2, 1)),
    xm
))
print(xmr.shape, tf.shape)
ym = xmr @ tf

plt.plot(X, y, 'ro')
plt.plot(xm, ym)
plt.show()

plt.plot(costs)
plt.show()
