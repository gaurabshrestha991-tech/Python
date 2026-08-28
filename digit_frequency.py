num = input("Enter a number: ")

frequency = {}

for digit in num:
    if digit in frequency:
        frequency[digit] += 1
    else:
        frequency[digit] = 1
for digit, count in frequency.items():
    print(digit, "=", count)
