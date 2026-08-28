a = int(input("Enter a numebr: "))
b = int(input("Enter a number: "))

gcd = 1

for i in range(1, min(a,b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
print("GCD: " ,gcd)

# for LCM 

for i in range(max(a, b), a * b + 1):
    if i % a == 0 and i % b == 0:
        lcm = i
        break
print("LCM: ", lcm)
