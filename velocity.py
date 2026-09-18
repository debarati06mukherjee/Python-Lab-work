# Let distance between P and Q = d

d = float(input("Enter distance between P and Q: "))

# Same direction: v1 - v2 = d/11
# Opposite direction: v1 + v2 = d/1

v1 = (d + d/11) / 2
v2 = (d - d/11) / 2

print("Velocity of first car =", v1)
print("Velocity of second car =", v2)