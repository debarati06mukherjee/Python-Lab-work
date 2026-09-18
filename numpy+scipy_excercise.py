import numpy as np
from scipy import linalg

print("Question 1")
print("-----------")

A = np.array([[2, 1, 1],
              [1, 3, 2],
              [1, 0, 0]])

B = np.array([[3, 0, 2],
              [2, 0, -2],
              [0, 1, 1]])

print("A =")
print(A)

print("B =")
print(B)

A_inv = linalg.inv(A)
print("Inverse of A =")
print(A_inv)

det_B = linalg.det(B)
print("Determinant of B =", det_B)

answer = np.dot(A, A_inv)
print("A x A inverse =")
print(answer)


print("\nQuestion 2 part 1")
print("-----------")

left_side = np.array([[2, 3],
                       [4, 5]])
right_side = np.array([8, 14])

xy = linalg.solve(left_side, right_side)
print("x =", xy[0])
print("y =", xy[1])


print("\nQuestion 2 part 2")
print("-----------")

D = 1

left_side2 = np.array([[11, -11],
                        [1, 1]])
right_side2 = np.array([D, D])

speeds = linalg.solve(left_side2, right_side2)
print("Speed of car 1 =", speeds[0])
print("Speed of car 2 =", speeds[1])


print("\nQuestion 3")
print("-----------")

M = np.array([[1, 2, 3, 4],
              [2, 4, 6, 8],
              [1, 0, 1, 0],
              [0, 1, 0, 1]])

print("M =")
print(M)

M_transpose = M.T
print("Transpose of M =")
print(M_transpose)

rank_of_M = np.linalg.matrix_rank(M)
print("Rank of M =", rank_of_M)


print("\nQuestion 4")
print("-----------")

N = np.array([[4, 1, 2, 0],
              [1, 3, 0, 1],
              [2, 0, 5, 1],
              [0, 1, 1, 2]])

print("N =")
print(N)

eigenvalues, eigenvectors = linalg.eig(N)
print("Eigenvalues =")
print(eigenvalues.real)

print("Eigenvectors =")
print(eigenvectors)

P, L, U = linalg.lu(N)
print("P =")
print(P)
print("L =")
print(L)
print("U =")
print(U)


print("\nQuestion 5")
print("-----------")

S = np.array([[4, 2, 1],
              [2, 3, 2],
              [1, 2, 4]])

print("S =")
print(S)

Q, R = linalg.qr(S)
print("Q =")
print(Q)
print("R =")
print(R)
print("qr() splits S into two matrices, Q and R. This is used to solve equations.")

U2, sigma, V = linalg.svd(S)
print("U =")
print(U2)
print("sigma =")
print(sigma)
print("V =")
print(V)
print("svd() splits")