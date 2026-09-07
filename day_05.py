# DICTIONARIES

student = {
    "name": "Emmanuella",
    "age": 18,
    "country": "Nigeria"
}

# Accessing values
print(student["name"])
print(student["age"])
print(student["country"])

# Adding a new item
student["course"] = "python"
print(student)

# Updating a value
student["age"] = 19
print(student)

# Removing an item with pop()
removed_age = student.pop("age")
print(removed_age)
print(student)

# Removing an item with del
del student["course"]
print(student)

# Checking if a key exists
print("country" in student)
print("email" in student)

# Getting all keys
print(student.keys())

# Getting all values
print(student.values())

# Getting both keys and values
print(student.items())

# Looping through keys
for key in student:
    print(key)

# Looping through keys and values
for key, value in student.items():
    print(key, value)

# Printing only values
for key, value in student.items():
    print(value)

# Using if/else with a dictionary
if "country" in student:
    print("Country found")
else:
    print("Country not found")

# Using .get()
print(student.get("country"))
print(student.get("email"))
print(student.get("email", "No email"))

# Updating/adding multiple items
student.update({
    "age": 18,
    "course": "python"
})
print(student)

# Clearing a dictionary
student.clear()
print(student)

# Creating the dictionary again
student = {
    "name": "Emmanuella",
    "age": 18,
    "country": "Nigeria"
}

# Copying a dictionary
student_copy = student.copy()

student_copy["age"] = 19

print(student)
print(student_copy)

# Adding course and updating age
student["course"] = "python"
student["age"] = 19

# Checking if country exists
if "country" in student:
    print(True)
else:
    print(False)

# Printing only name and course
for key, value in student.items():
    if key == "name" or key == "course":
        print(key, value)