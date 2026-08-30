# Program to implement set operations union, intersection, difference and Cartesian product

A = set(map(int, input("Enter elements of set A separated by space: ").split()))
B = set(map(int, input("Enter elements of set B separated by space: ").split()))

union = A | B

intersection = A & B

difference = A - B

cartesian_product = {(a, b) for a in A for b in B}

print("\nSet A =", A)
print("Set B =", B)

print("\nUnion (A U B) =", union)
print("Intersection (A int B) =", intersection)
print("Differenec (A - B) =", difference)
print("Cartesian Product (A X B) =", cartesian_product)

