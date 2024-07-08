# Class methods are a function inside a class which can be invoked / called from both class and object
# static methods are the methods inside a class which doesn't change the state of class or object. This is used to return static content
# @classmethod decorator is used to create a classmethod and @staticmethod for static method

class Vehicle:
    engine_type = "Petrol"  # class attribute
    __wheels = 2

    def get_details(self):
        return f"class vhicle with engine {self.engine_type}"

    @classmethod
    def set_wheels(cls, wheels):
        cls.__wheels = wheels

    @classmethod
    def get_wheels(cls):
        return cls.__wheels

    @staticmethod
    def get_color():
        return "The color of the vehicle is red"

    def __init__(self):
        self.name = "Jon"


v1 = Vehicle()
print(v1.engine_type)
print(v1.name)

print(Vehicle.engine_type)  # class attribute invoked by Vehicle class
# print(Vehicle.name)  # This raises error because "name" is instance attribute

print(v1.get_details())  # instance method
# print(Vehicle.get_details())  # This raises error because instance method can't be called by class

print(Vehicle.get_wheels())  # 2
Vehicle.set_wheels(4)
print(Vehicle.get_wheels())  #


v1.set_wheels(6)
print(v1.get_wheels())


print(Vehicle.get_color())