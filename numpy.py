marks = [
    [80, 70, 90],
    [60, 44, 85],
    [90, 88, 95],
    [55, 13, 70],
    [78, 82, 80]
]

# i. Maximum marks
all_marks = []

for row in marks:
    for mark in row:
        all_marks.append(mark)

print("Maximum marks:", max(all_marks))


# ii. Minimum marks
print("Minimum marks:", min(all_marks))


# iii. Average marks
total = sum(all_marks)
average = total / len(all_marks)

print("Average marks:", average)


# iv. Maximum marks subject-wise
print("Maximum marks subject-wise:")

for j in range(3):
    subject_marks = []

    for i in range(5):
        subject_marks.append(marks[i][j])

    print("Subject", j + 1, ":", max(subject_marks))


# v. Average marks subject-wise
print("Average marks subject-wise:")

for j in range(3):
    subject_marks = []

    for i in range(5):
        subject_marks.append(marks[i][j])

    average = sum(subject_marks) / len(subject_marks)

    print("Subject", j + 1, ":", average)


# vi. Add 10 marks to students scoring less than 50 in Subject 1
# Subject 1 = 2nd column

for i in range(5):
    if marks[i][1] < 50:
        marks[i][1] = marks[i][1] + 10

print("Marks after adding 10 marks:", marks)


# vii. Number of students scoring more than 80 in Subject 2
# Subject 2 = 3rd column

count = 0

for i in range(5):
    if marks[i][2] > 80:
        count = count + 1

print("Students scoring more than 80 in Subject 2:", count)


# viii. Minimum marks of Student 2
# Student 2 = 3rd row

print("Minimum marks of Student 2:", min(marks[2]))


# ix. Maximum marks of Student 4
# Student 4 = 5th row

print("Maximum marks of Student 4:", max(marks[4]))