import scipy.stats as stats

# ==========================================
# 1. ONE-SAMPLE T-TEST
# ==========================================

print("----- ONE-SAMPLE T-TEST -----")

marks = [18, 15, 12, 20, 17]

# Population mean
population_mean = 50

t, p = stats.ttest_1samp(marks, population_mean)

print("Marks:", marks)
print("Population Mean:", population_mean)
print("T-value:", t)
print("P-value:", p)

if p < 0.05:
    print("Reject the population mean")
else:
    print("Accept the population mean")


# ==========================================
# 2. TWO-SAMPLE T-TEST
# ==========================================

print("\n----- TWO-SAMPLE T-TEST -----")

group1 = [18, 15, 12, 20, 17]
group2 = [25, 28, 24, 30, 27]

t, p = stats.ttest_ind(group1, group2)

print("Group 1:", group1)
print("Group 2:", group2)
print("T-value:", t)
print("P-value:", p)

if p < 0.05:
    print("The two groups are significantly different")
else:
    print("The two groups are not significantly different")


# ==========================================
# 3. CHI-SQUARE TEST
# ==========================================

print("\n----- CHI-SQUARE TEST -----")

# Contingency table
data = [
    [30, 20],
    [20, 30]
]

chi, p, dof, expected = stats.chi2_contingency(data)

print("Chi-square value:", chi)
print("P-value:", p)
print("Degrees of freedom:", dof)

if p < 0.05:
    print("The variables are associated")
else:
    print("The variables are not associated")