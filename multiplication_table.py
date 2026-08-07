## Multiplication table using for loops and range
print(" ")
print(" ")

n = int(input("Enter a number: "))

print("Multiplication Table of ", n)
for el in range(1, 11):
    print("", n, "X",  "", el, "=", n*el) 