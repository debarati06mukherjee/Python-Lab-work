class Student:
    def __init__(self, name, department, roll_no):
        self.name = name
        self.department = department
        self.roll_no = roll_no

    def show(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Roll No:", self.roll_no)
        print()


s1 = Student("Sarthak", "CSE", 101)
s2 = Student("Rahul", "CSE", 102)
s3 = Student("Amit", "ECE", 103)
s4 = Student("Priya", "IT", 104)
s5 = Student("Ananya", "CSE", 105)

s1.show()
s2.show()
s3.show()
s4.show()
s5.show()