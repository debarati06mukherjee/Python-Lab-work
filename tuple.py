employees = (
    "ABC", "XYZ", "ABC", "PQR", "XYZ",
    "LMN", "ABC", "DEF", "PQR", "XYZ",
    "LMN", "DEF", "ABC", "PQR", "XYZ",
    "DEF", "LMN", "ABC", "PQR", "XYZ"
)

# 1. Print each name and its frequency
print("Name and frequency:")

for name in set(employees):
    print(name, ":", employees.count(name))


# 2. Remove duplicate names
unique = tuple(set(employees))

print("\nDistinct names:")
print(unique)


# 3. Employee having maximum frequency
max_frequency = 0
max_name = ""

for name in unique:
    frequency = employees.count(name)

    if frequency > max_frequency:
        max_frequency = frequency
        max_name = name

print("\nEmployee with maximum frequency:", max_name)


# 4. Sort tuple alphabetically
sorted_names = tuple(sorted(unique))

print("\nAlphabetical order:")
print(sorted_names)


# 5. Search for a specific employee
search = input("\nEnter employee name: ")

if search in employees:
    print("Employee exists in the tuple")
else:
    print("Employee does not exist in the tuple")