marks = [70, 80, 65, 90, 55, 75]

# 1. Average marks
average = sum(marks) / len(marks)
print("Average marks:", average)

# 2. Number of students who scored more than average
count = 0

for mark in marks:
    if mark > average:
        count = count + 1

print("Students scored more than average:", count)

# 3. Maximum marks
print("Maximum marks:", max(marks))