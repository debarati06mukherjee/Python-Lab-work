import numpy as np
from scipy.linalg import lu

A = np.array([[1, 2, 0, 0],
              [2, 1, 0, 0],
              [0, 0, 3, 1],
              [0, 0, 1, 3]])

P, L, U = lu(A)

print("P =")
print(P)

print("L =")
print(L)

print("U =")
print(U)