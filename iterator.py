numbers = [10, 20, 30, 40]

numbers_iterator = iter(numbers)

print(numbers_iterator)
print(next(numbers_iterator))

# iterator with while

numbers = [10, 20, 30, 40]

numbers_iterator = iter(numbers)

while True:
    try:
        number = next(numbers_iterator)
    except StopIteration:
        print("Iterator till the end")
        break
    else:
        print("Loop number is", number)
