# Four pillars of OOP are:
# 1. Inheritance
# 2. Encapsulation
# 3. Polymorphism
# 4. Abstraction

# Inheritance is a way of passing the attributes and methods from a parent class/classes to their
# child/children classes.
# But we cannot access the property of child in parent class

class Vehicle:
    engine_type = "Petrol"


class Car(Vehicle):  # Here Vehicle is inherited in Car class
    number_of_wheels = 4


c = Car()
print(c.engine_type)  # Petrol
print(c.number_of_wheels)  # 4


class Bike(Vehicle):
    number_of_wheels = 2


b = Bike()
print(b.engine_type)  # Petrol
print(b.number_of_wheels)  # 2