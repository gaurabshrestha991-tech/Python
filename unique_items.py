# Write a program to find unique items from two lists or to check for common friends in two groups

group1  = input("Enter names in Group 1 separated by spaces: ").split()
group2 = input("Enter names in Group 2 separated by spaces: ").split()

set1 = set(group1)
set2 = set(group2)

common = set1.intersection(set2)

unique = set1.symmetric_difference(set2)

print("\nCommon friends: ", common)
print("Unique items: ", unique)
