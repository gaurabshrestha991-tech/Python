#  Lambda

square = lambda x : x * x
print(square(5))

add = lambda a, b : a + b
print(add(10, 20))

# Lambda is commanly used with map(), filter(), sorted()

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x : x * x, numbers))

print(squares)

# Map -> applies a function to every element

result = map(lambda x : x ** 2, numbers)

print(list(result))


# filter -> Keeps the element that satisfy the condition.

num = [10, 20, 30, 40, 50]

result = filter(lambda x : x % 4 == 0, num)

print(list(result))

# Soretd with key

students = [
    ("Alice", 85),
    ("Bob", 70),
    ("Ben", 95)
]

students.sort(key = lambda x : x[1]) # -> sort according to second element

print(students)


# reduce() -> repeatedly combines elements into one result.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a + b, numbers)
print(result)


# zip -> combines corresponding elements

names = ["ram", 'sita', 'gita']
marks = [90, 80, 70]

result = zip(names, marks)

print(list(result))

# enumerate()

for i , name in enumerate(names):
    print(i, name)
    
#any() -> checks whether at least one value is true

nums = [1, 3, 5, 8]

print(any(x % 2 == 0 for x in nums))

# all() -> check whether every value is true

print(all(x % 2 == 0 for x in nums))

# isinstance () 

x = 10

print(isinstance(x, int))
print(isinstance(x, float))

class Student:
    pass

studnet = Student()

print(isinstance(studnet, Student))


print(id(x)) # Returns an object identity

print(dir(nums)) # Shows attributes and methods available on an object.

