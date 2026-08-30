#       Program to implrment fuzzy set operations

A = [0.2, 0.5, 0.7, 1.0]
B = [0.4, 0.3, 0.8, 0.6]

union = []
intersection = []
compelment_A = []

for i in range(len(A)):
    union.append(max(A[i], B[i]))
    intersection.append(min(A[i], B[i]))
    compelment_A.append(1 - A[i])
    
print("Fuzzy set A =", A)
print("Fuzzy Set B =", B)

print("Union =", union)
print("Intersection =", intersection)
print("Complement of A =", compelment_A)
