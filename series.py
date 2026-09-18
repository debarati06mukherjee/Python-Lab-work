import math

n = int(input("Enter number of terms: "))
s = 0

print("S = ", end="")

for i in range(1, n + 1):
    term = math.pow(i, 2) / math.factorial(i)
    s = s + term

    print(f"{i**2}/{i}!", end="")
    if i < n:
        print(" + ", end="")

print("\nSum =", s)