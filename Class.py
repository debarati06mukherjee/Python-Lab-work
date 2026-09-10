class Student:

    def __init__(self, name, department, rollno):
        self.name = name
        self.department = department
        self.rollno = rollno

    def show(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Roll No:", self.rollno)
        print()


# Creating 5 student objects
s1 = Student("Rahul", "CSE", 101)
s2 = Student("Priya", "CSE", 102)
s3 = Student("Amit", "IT", 103)
s4 = Student("Sneha", "ECE", 104)
s5 = Student("Riya", "CSE", 105)


# Display records
s1.show()
s2.show()
s3.show()
s4.show()
s5.show()