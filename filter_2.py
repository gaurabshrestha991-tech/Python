numbers = [1, 2, 3, 4, 5, 6]


def filter_even(number):
    return number % 2 == 0


even_numbers = filter(filter_even, numbers)

for number in even_numbers:
    print(number)
