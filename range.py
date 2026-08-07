for i in range(1, 10, 2): #start, end-1, steps 
    print(i)
print("Odd numbers")

print(" ")

for el in range(2, 10, 2):
    print(el)
print("Even numbers")

print(" ")

print("Reverse numbers")
for el in range(10, 0, -1):
    print(el)
print("10 to 1")

## Multiplication table using for loops and range
print(" ")
print(" ")

n = int(input("Enter a number: "))

print("Multiplication Table of ", n)
for el in range(1, 11):
    print("", n, "X",  "", el, "=", n*el) 