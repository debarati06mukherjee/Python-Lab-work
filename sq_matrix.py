import numpy as np

A = np.array([[1, 2],
              [3, 4]])

b = np.array([5, 6])

# i) QR decomposition
Q, R = np.linalg.qr(A)

print("Q =")
print(Q)

print("R =")
print(R)

# ii) SVD
U, S, V = np.linalg.svd(A)

print("\nU =")
print(U)

print("S =")
print(S)

print("V =")
print(V)

# iii) Least Square
x = np.linalg.lstsq(A, b, rcond=None)[0]

print("\nLeast Square solution =")
print(x)