def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


numbers_generator = numbers()

print(next(numbers_generator))
print(next(numbers_generator))
print(next(numbers_generator))
print(next(numbers_generator))
print(next(numbers_generator))

# Yield with for loop

def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


numbers_generator = numbers()

for number in numbers_generator:
    print(number)
