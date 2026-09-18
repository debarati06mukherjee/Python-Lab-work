import numpy as np

# Define two 3x3 matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 10]])

B = np.array([[2, 1, 3],
              [1, 0, 2],
              [4, 1, 5]])

# (i) Inverse of A
print("Inverse of A:")
print(np.linalg.inv(A))

# (ii) Determinant of B
print("Determinant of B:")
print(np.linalg.det(B))

# (iii) A × A^-1
print("A × A^-1:")
print(np.dot(A, np.linalg.inv(A)))