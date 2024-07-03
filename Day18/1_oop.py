# OOP stands for Object-Oriented Programming
# OOP is an approach of solving the problems by breaking down them in objects
# There are two parts in OOP approach; Class and Object
# Class is a blueprint of an object
# Object is an instantiation of Class

class Vehicle:  # class is a keyword to create class. Vehicle is an identifier. Class name should follow PascalCase
    # property
    # method
    engine_type = "Petrol"  # class property / attribute

    # Constructor => This is called while creating a Vehicle object
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels
        # here self.color and self.wheels are instance attribute


car = Vehicle("red", 4)  # This creates the Vehicle object
engine = car.engine_type  # Property invoke using Vehicle object
print(engine)  # Petrol

print(car.color)  # red
print(car.wheels)  # 4
# print(Vehicle.color)


print(Vehicle.engine_type)  # Property invoke using class Vehicle



class Student:
    classroom = 10

    def __init__(self, n, a, r, sex="Male"):
        self.name = n
        self.age = a
        self.roll = r
        self.sex = sex


student1 = Student("Jon", 23, 2)  # student1 is object
student2 = Student("Alex", 25, 13, "Female")
print(student1.classroom)
print(student1.name)  #

print(student2.classroom)  # 10
print(student2.name)  # Alex
print(student2.roll)  # 13