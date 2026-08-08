students = [
    {
        "name": "ram",
        "marks": 20
    },
    {
        "name": "hari",
        "marks": 30
    },
    {
        "name": "geeta",
        "marks": 50
    }
]

sorted_students = sorted(
    students,
    key=lambda student: student["marks"],
    reverse=True
)

print(sorted_students)
