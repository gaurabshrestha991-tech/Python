class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        print("Deleting object")


p1 = Point(1, 5)

print("Point created")

del p1

print("Object deleted")
