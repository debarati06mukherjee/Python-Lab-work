import numpy as np
from scipy.linalg import eig

A = np.array([[1, 2, 0, 0],
              [2, 1, 0, 0],
              [0, 0, 3, 1],
              [0, 0, 1, 3]])

eigenvalues, eigenvectors = eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)