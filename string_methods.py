text = " Hello Python World  "

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())

print(text.strip())
print(text.lstrip())
print(text.rstrip())

text = "Hello Python Python"

print(text.find("Python"))
print(text.rfind("Python"))
print(text.count("Python"))
print(text.replace("Python", "Java"))

print(text.startswith("Hello"))
print(text.endswith("Python"))

print(text.isalpha())
print("123".isdigit())
print(" ".isspace())

# string splitting and joining

sentence = "apple, banana, orange"

fruits = sentence.split(",")

print(fruits)
print(", ".join(fruits))
