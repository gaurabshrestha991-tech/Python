class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"P ({self.x}, {self.y})"

    def __sub__(self, other):
        distance = (
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2
        ) ** 0.5

        return round(distance, 2)

    def __mul__(self, scale):
        return Point(
            self.x * scale,
            self.y * scale
        )

    def __add__(self, other):
        return (
            self.x + other.x,
            self.y + other.y
        )


p1 = Point(1, 5)
p2 = Point(5, 1)

distance = p2 - p1
print("Distance:", distance)

print("Scaled point:", p1 * 3)

# Addition operator
print("Added points:", p1 + p2)
