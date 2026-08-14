student = {
    "name": "Rahul",
    "age": 19,
    "school": "ABC School"
}

print(student["name"])
print(student["age"])

# Using get() is safer when the key might not exist
print(student.get("population"))
