numbers = [1, 2, 3, 4, 5, 6]


def filter_even(number):
    return number % 2 == 0


print(filter_even(2))
print(filter_even(3))

even_numbers = filter(lambda number: number % 2 == 0, numbers)

for number in even_numbers:
    print(number)
