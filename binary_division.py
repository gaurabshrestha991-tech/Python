a = input("Enter dividend in binary: ")
b = input("Enter divisior in binary: ")

num1 = int(a, 2)
num2 = int(b, 2)

if num2 == 0:
    print("Dividing by ZERO is not allowed!")
else:
    quotient = num1 // num2
    remainder = num1 % num2
    
    binary_quotient = bin(quotient)[2:]
    binary_remainder = bin(remainder)[2:]
    
    print("Binary Qupotient =", binary_quotient)
    print("Binary Remainder =", binary_remainder)
    
