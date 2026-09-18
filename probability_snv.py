from scipy import stats

# Standard normal variable
x = 1.5

# Calculate cumulative probability
p = stats.norm.cdf(x)

print("Standard normal variable =", x)
print("Probability that X is less than", x, "=", p)