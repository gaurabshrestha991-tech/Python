# Recursion for factorial

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)

n = int(input("Enter a number:"))
factorial = fact(n)
print("Factorial of", n, "is", factorial)
print(" ")
print(" ")

# Write a recursive function to calculate the sum of natural number

def sum(n):
    if(n == 0):
        return
    else:
        return (n-1) + n

n = int(input("Enter a number:"))
add = sum(n)
print("Sum of", n, "natural number is", add)
print(" ")
print(" ")


# Write a recursive function to print all the elemets in a list 

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["Apple", "Mango", "Litichi", "Banana"]

print(print_list(fruits))