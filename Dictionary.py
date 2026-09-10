employees = {
    "E1": {
        "name": "Rahul",
        "designation": "Manager",
        "department": "HR",
        "salary": 50000
    },

    "E2": {
        "name": "Priya",
        "designation": "Developer",
        "department": "IT",
        "salary": 60000
    },

    "E3": {
        "name": "Amit",
        "designation": "Designer",
        "department": "Design",
        "salary": 45000
    },

    "E4": {
        "name": "Sneha",
        "designation": "Developer",
        "department": "IT",
        "salary": 70000
    },

    "E5": {
        "name": "Riya",
        "designation": "Tester",
        "department": "QA",
        "salary": 55000
    }
}


# 1. Print record of employee E1
print("Employee E1:", employees["E1"])


# 2. Print department of employee E4
print("Department of E4:", employees["E4"]["department"])


# 3. Employee having maximum salary
max_salary = 0
max_employee = ""

for id in employees:
    if employees[id]["salary"] > max_salary:
        max_salary = employees[id]["salary"]
        max_employee = id

print("Employee with maximum salary:")
print(max_employee, employees[max_employee])


# 4. Insert a new employee
employees["E6"] = {
    "name": "Arjun",
    "designation": "Developer",
    "department": "IT",
    "salary": 65000
}

print("After adding new employee:")
print(employees)