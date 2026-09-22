import pandas as pd

marks = pd.Series(
    [80, 75, 90, 65, 85],
    index=["Rahul", "Priya", "Amit", "Sneha", "Riya"]
)

print("Marks of 5 students:")
print(marks)