student = {
    "name": "Rahul",
    "age": 19
}


student["gender"] = "male"
student["class"] = 10
student["GPA"] = 3.97

print(student)

student["age"] = 21

print(student)

# Remove items

student = {
    "name": "Rahul",
    "age": 19,
    "school": "ABC School"
}

# Remove an item
age = student.pop("age")

print("Removed age:", age)
print(student)

# Another way:
# del student["school"]
