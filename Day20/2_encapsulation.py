# Encapsulation is the way of hiding the attributes outside of the class
# We can define attributes in three different ways in Python OOP
# 1. Private, 2. Public and 3. Protected


class Vehicle:
    __color = "red"  # Private attribute. In private attribute use __ at beginning of the variable
    _engine_type = "Petrol"  # Protected. Single underscore to define protected variables / attributes
    number_of_wheels = 4  # Public

    def get_details(self):
        return f"Color is {self.__color}. Engine is {self._engine_type}"

    def get_color(self):
        return self.__color

    # def set_color(self, color):
    #     pw = input("Enter password")
    #     if valid_user:
    #         self.__color = color


class Bike(Vehicle):
    number_of_wheels = 2

    def get_details(self):
        # return f"Color is {self.__color}. Engine is {self._engine_type}. Number of doors {self.number_of_doors}"
        return f"Engine is {self._engine_type}. Number of doors {self.number_of_wheels}"


bike = Bike()
print(bike.get_details())

print(bike._engine_type)  # This doesn't raise error in Python but accessing protected members outside the class is not recommended
# print(bike.__color)  # Error because it is trying to access private member outside the class
print(bike.number_of_wheels)
print(bike.get_color())