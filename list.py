marks = [99,98,97,96]

print(marks[0])
print(marks[2])

marks[0] = 45 # list are mutable, they can be changed
print(marks[0])

print(marks)

student = ["Gaurab", 19, "BIT", 9.7]

name = student[0]
age = student[1]
course = student[2]
cgpa = student[3]

print(name), print(age), print(course), print(cgpa)

##LIST SLICING

print(marks[1:])
print(marks[0:4])

# Negative slicing 
print(marks[-3:])


