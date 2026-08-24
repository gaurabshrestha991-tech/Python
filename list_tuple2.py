#           List Comprehension

matrix = [[i*j for j in range(5)] for i in range(5)]

result = [x if x % 2 == 0 else -x for x in range(5)]

filtered = [x for x in range(100) if x % 2 == 0 if x % 3 == 0]

nested = [[1,2,3], [3,4,5], [5,6,7]]
flat = [a for sublist in nested for a in sublist]

list = [["Apple", 'Banana'], ["Orange", "Mango"]]
fruits = [x for sublist in list for x in sublist]


print(matrix)
print(result)
print(filtered)
print(flat)
print(fruits)


falful = ['apple', 'banana', 'cherry', 'dragon fruit']
falful = [falfuls.upper() for falfuls in falful]
print(falful)

falful = [falfuls[0] for falfuls in falful]
print(falful)

#           Conditions

numbers = [1, -2, 3, -4 ,5, -6]
positive_nums =[num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num%2 <= 0]
even_nums = [num for num in numbers if num%2 == 0]
odd_nums = [num for num in numbers if num%2 != 0]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

grades = [30, 40, 50, 80, 90, 70, 60]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)


fruits = ['apple', 'banana', 'cherry', 'strawberry', 'pineapple', 'mango']
for fruit in fruits:
    if len(fruit) >= 7:
        print(fruit)

print([fruit for fruit in fruits if len(fruit) >= 6])

numbers = [-1,2,3,7,9,-10,-13,34,-19,11]

prime_numbers = [
    n for n in numbers
    if n > 1 and all(n % i != 0 for i in range (2, int (n ** 0.5) + 1))]
print(prime_numbers)


amount = [10, 20, 30, -60, 90, -14, -47, 58, 88, 19, 13, 97]

even_amount = [amt for amt in amount if amt %2 == 0]
odd_amount =  [amt for amt in amount if amt %2 != 0]
negative_amount = [amt for amt in amount if amt <= 0]
prime_amount = [
    amt for amt in amount
    if amt > 1 and all(amt % x != 0 for x in range(2,int(amt ** 0.5) + 1))]


print(even_amount)
print(odd_amount)
print(negative_amount)
print(f"Prime amounts:{prime_amount}")


list_fruit = [fruit for fruit in fruits if len(fruits[0]) >= 6]
print(list_fruit)
# print(len(fruits[3]))

#                      Copy Lists (shallow vs Deep)


import copy

orginal = [[1,2], [3,4]]

# Shallow Copy (3 ways)

copy1 = orginal.copy()
copy2 = orginal[:]
copy3 = list(orginal)

deep_copy = copy.deepcopy(orginal)

print(copy1)
print(copy2)
print(copy3)
print(deep_copy)

copy1[0][0] = 99  # -> modify nested list copy affects orginal
 
deep_copy[0][0] = 100 # -> orginal unchanged

print(copy1)
print(deep_copy)