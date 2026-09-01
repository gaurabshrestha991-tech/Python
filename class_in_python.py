         #Classes in Python

class Car:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price
        
    def show_info(self):
        print("Brand: ", self.brand)
        print("Color: ", self.color)
        print("Price: ", self.price)
        
car1 = Car("Toyota", "Blue", 5000000)
car1.show_info()


class Student:
    def __init__(self, grade, section, school):
        self.grade = grade
        self.section = section
        self.school = school
        
    def show_info(self):
        print("Grade: ", self.grade)
        print("Section: ", self.section)
        print("School: ", self.school)
        print("\n")
        
student = Student(12, "A", "Amrit Science Campus")
student.show_info()


class Cricketer:
    def __init__(self, name, nation, plays, level, position_number):
        self.name = name
        self.nation = nation
        self.plays = plays
        self.level = level
        self.position_number = position_number
    
    def show_info(self):
        print("Name: ", self.name)
        print("Nation: ", self.nation)
        print("Plays: ", self.plays)
        print("Experience: ", self.level)
        print("Plays At (position): ", self.position_number)
        print("\n")
    
cricketer1 = Cricketer("Joe Root", "England", "Batter", "International", 1)
cricketer2 = Cricketer("Mitchel Starc","Australia", "Bowler", "International", 11)
cricketer3 = Cricketer("Virat Kohli","India", "Batter", "International", 3)

cricketer1.show_info()
cricketer2.show_info()
cricketer3.show_info()
