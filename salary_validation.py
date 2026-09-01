class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
rectangle = Rectangle(20 , 10)
print("Area of rectangle:",  rectangle.area())
print("Perimeter of rectangle:", rectangle.perimeter())
