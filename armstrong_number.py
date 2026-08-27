num = int(input("Enter a number: "))

orginal = num
digits = len(str(num))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10
    
if sum == orginal:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong!")
