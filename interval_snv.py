from scipy import stats

p = 0.90

z = stats.norm.ppf((1 + p) / 2)

print("Confidence level =", p)
print("Lower limit =", -z)
print("Upper limit =", z)
print("Interval =", (-z, z))