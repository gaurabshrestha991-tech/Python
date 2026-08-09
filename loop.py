fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#Iteration over a string

for a in "Python":
    print(a)
for character in "Django":
    print(character)
#Using range 
for i in range(5):
    print(i)

for a in range (2, 8):
    print(a)

for Gaurab in range (1, 6):
    print(Gaurab)

# Iterating over dictionaries

student = {"name": "John", "age": 25, "city": "NYC"}

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(f"{key}: {value}")


                        #While Loops

count = 0
while count < 5:
    print(count)
    count += 1

num = 2
while num < 10:
    print (num)
    num += 2
else :
    print("Loop Completed naturally!")

                        #Loop comtrol Statement

for i in range(10):
    if i == 3:
        break
    print(i)

for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print(f"({i}, {j})")

for i in range(5):
    if i == 3:
        continue
    print(i)

for i in range(5):
    if i == 2:
        pass # Do nothing, placeholder for future code
    print(i)

                   # Advance for loops Techniques

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruits}")

print("")

for Gaurab, fruit in enumerate(fruits, start = 1):
    print(f"{Gaurab}: {fruits}")

print("")

for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")


                            #Zip (Iterate Multiple Sequences)

names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 91]
grades = ["A", "B", "C"]

for name, score, grade in zip(names, scores, grades):
    print(f"{name}: {score} ({grade})")

for item in zip([1,2,3], ["a", "b"]):
    print(item)

from itertools import zip_longest
for a, b in zip_longest([1,2,3], ["a", "b"], fillvalue="N/A"):
    print(a, b)


    # Sorted and Reversed

    numbers = [3, 1, 4, 1, 5, 9]

    for num in sorted(numbers):
        print(num)

#Reverse sorted
    for num in sorted(numbers, reverse=True):
        print(num)

#Reverse sequence
    for num in reversed(numbers):
        print(num)


#List Comprehensions (Loop Shortcuts)

#Basic Comprehensions

squares = []
for i in range(10):
    squares.append(i**2)

squares = [i**2 for i in range(10)]

even_sqaures = [i**2 for i in range(10) if i % 2 == 0]

pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b', 'c']]

print(squares)

print(even_sqaures)

print(pairs)

print("")


# Dictionary and Set Comprehensions

squares_dict = {i: i**2 for i in range(5)}

unique_squares = {i**2 for i in [1,2,2,3,3,3]}

sum_squares = sum(i**2 for i in range(1000000))

print(squares_dict)
print(unique_squares)
print(sum_squares)