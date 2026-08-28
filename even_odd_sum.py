for i in range(n+1):
    if i % 2 == 0:
        sum =sum + i
print(f"The sum of first {n} even numbers is ", sum)

num = int(input("Enter a number: "))
sum = 0

for i in range(num):
    if i % 2 != 0:
        sum = sum + i
print(f"Sum of first {num} odd numbers is ", sum)

