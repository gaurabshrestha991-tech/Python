student = {
    "name": "Rahul",
    "age": 19,
    "school": "ABC School"
}

for key in student.keys():
    print(key)

print()

for value in student.values():
    print(value)

print()

for key, value in student.items():
    print(f"{key}: {value}")

#   Nested Dictionary

students = {
    "student1": {
        "name": "John",
        "age": 19
    },
    "student2": {
        "name": "Alice",
        "age": 10
    }
}

print(students["student1"]["name"])
print(students["student2"]["name"])

# Dictionary Comprehension

squares = {i: i**2 for i in range(10)}

print(squares)


even_squares = {
    i: i**2
    for i in range(10)
    if i % 2 == 0
}

print(even_squares)

