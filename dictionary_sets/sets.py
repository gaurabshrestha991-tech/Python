# Create sets
numbers = {1, 2, 3, 3, 4, 4, 4, 5, 5}

print(numbers)

# Add and remove discard
numbers = {1, 2, 3, 4, 5}

numbers.add(6)
print(numbers)

numbers.remove(2)
print(numbers)

numbers.discard(10)
print(numbers)


# Set memberships
numbers = {1, 2, 3, 4, 5}

print(3 in numbers)    # True
print(10 in numbers)   # False

A = {1, 2, 3, 4, 5, 6}
B = {3, 4, 5, 6, 7, 8}

# Union
print("Union:", A | B)
print("Union:", A.union(B))

# Intersection
print("Intersection:", A & B)
print("Intersection:", A.intersection(B))

# Difference
print("Difference:", A - B)

# Symmetric Difference
print("Symmetric Difference:", A ^ B)
