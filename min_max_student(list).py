students = ["Shreya", "Riya", "Rahul", "Sneha", "Priya",
            "Arya", "Neha", "Karan", "Pooja", "Rittisha"]

marks = [78, 92, 65, 88, 95, 70, 81, 60, 85, 74]
max_marks = max(marks)
min_marks = min(marks)

max_index = marks.index(max_marks)
min_index = marks.index(min_marks)

print("Student Names:", students)
print("Marks:", marks)

print("\nStudent scoring Maximum Marks:")
print(students[max_index], "-", max_marks)

print("\nStudent scoring Minimum Marks:")
print(students[min_index], "-", min_marks)