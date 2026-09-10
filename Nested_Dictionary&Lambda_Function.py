student = {
    "S1": {"name": "Rahul", "department": "CSE", "marks": 80},
    "S2": {"name": "Priya", "department": "ECE", "marks": 70},
    "S3": {"name": "Amit", "department": "CSE", "marks": 90},
    "S4": {"name": "Sneha", "department": "IT", "marks": 60},
    "S5": {"name": "Riya", "department": "CSE", "marks": 85}
}


# (i) Sort dictionary according to marks - highest to lowest
sorted_student = sorted(
    student.items(),
    key=lambda x: x[1]["marks"],
    reverse=True
)

print("Students sorted by marks:")
for s in sorted_student:
    print(s)


# (ii) Student who scored maximum marks
maximum = max(student.items(), key=lambda x: x[1]["marks"])

print("\nStudent with maximum marks:")
print(maximum)


# (iii) Find average marks
total = 0

for s in student:
    total = total + student[s]["marks"]

average = total / len(student)

print("\nAverage marks:", average)


# (iv) Students who scored more than average
print("\nStudents who scored more than average:")

for s in student:
    if student[s]["marks"] > average:
        print(student[s]["name"])