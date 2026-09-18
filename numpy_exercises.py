# 2D array of marks

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
print("\nMaximum marks subject-wise:")

for j in range(3):
    subject_marks = []

    for i in range(5):
        subject_marks.append(marks[i][j])

    print("Subject", j + 1, ":", max(subject_marks))


# v. Average marks subject-wise
print("\nAverage marks subject-wise:")

for j in range(3):
    subject_marks = []

    for i in range(5):
        subject_marks.append(marks[i][j])

    average = sum(subject_marks) / len(subject_marks)

    print("Subject", j + 1, ":", average)


# vi. Add 10 marks to students scoring less than 50 in Subject 1
for i in range(5):
    if marks[i][0] < 50:
        marks[i][0] = marks[i][0] + 10

print("\nMarks after adding 10 to Subject 1:")
print(marks)


# vii. Number of students scoring more than 80 in Subject 2
count = 0

for i in range(5):
    if marks[i][1] > 80:
        count = count + 1

print("\nStudents scoring more than 80 in Subject 2:", count)


# viii. Minimum marks of Student 2
print("Minimum marks of Student 2:", min(marks[1]))


# ix. Maximum marks of Student 4
print("Maximum marks of Student 4:", max(marks[3]))