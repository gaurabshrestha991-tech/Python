n = int(input("Enter a number (more than 1 digit): "))
a = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
    
print(f"The sum of {a} is ", sum)
