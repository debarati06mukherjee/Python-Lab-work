from scipy import stats

marks = [45, 67, 78, 56, 89, 72, 65, 90, 55, 80]

result = stats.describe(marks)

print("Descriptive Statistics:")
print(result)

print("Mean =", stats.tmean(marks))
print("Median =", __import__('numpy').median(marks))
print("Standard Deviation =", __import__('numpy').std(marks))