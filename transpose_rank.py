import numpy as np

A = np.array([[1, 2, 3, 4],
              [2, 3, 4, 5],
              [3, 4, 5, 6],
              [4, 5, 6, 8]])

print("Transpose:")
print(A.T)

print("Rank:")
print(np.linalg.matrix_rank(A))