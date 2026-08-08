name = "Alice"
age = 30
city = "New York"

print("Name : %s, Age = %d, City = %s" % (name, age, city))

print("Name: {}, Age: {}, City: {}".format(name, age, city))

print("Name: {0}, Age: {1}, City: {2}".format(name, age, city))

print("Name: {n}, Age: {a}, City: {c}".format(
    n=name,
    a=age,
    c=city
))

print(f"Name: {name}, Age: {age}, City: {city}")

print(f"Next Year, {name} will be {age + 1}")
print(f"I will shift from {city} city to Texas")
print(f"Her name is {name} and her sister name is Grace")
