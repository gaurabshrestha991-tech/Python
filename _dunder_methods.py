class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"P ({self.x}, {self.y})"


p1 = Point(1, 5)

print(p1)
print(str(p1))
