import numpy as np

# Coefficients of x and y
A = np.array([[3, -5],
              [4, -2]])

# Constant values
B = np.array([10, 7])

# Solve the equations
x, y = np.linalg.solve(A, B)

print("x =", x)
print("y =", y)
