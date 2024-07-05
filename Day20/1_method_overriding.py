# If a method is defined in parent class and the same method is again defined in
# the child class then it is method overriding
# If you want to access the parent method from the child method then we should use super()


class Vehicle:
    def details(self):
        return "This is vehicle"


class Bike(Vehicle):
    def details(self):
        print(super().details())
        return "This is bike"


bike = Bike()
print(bike.details())