## Using for loop

fact = 1
num = int(input("Enter a number to find factorial: "))

for el in range(1, num+1):
    fact *= el
print("Factorial of ", num, "is", fact)

## using while loop

fact = 1
num = int(input("Enter a number: "))
el = 1
while el < num:
    fact*= el
    el+=1
print("Factorial of ", num, "is", fact)

