import numpy as np
from scipy.linalg import solve

A = [[2, 3],
     [4, 5]]

B = [8, 14]

x, y = solve(A, B)

print("x =", x)
print("y =", y)