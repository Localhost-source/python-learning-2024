"""
Create a class Person with instance attributes name and age.
Create  a class attribute nationality. 
Create a method get_details in this class to print name and age.
"""

class Person:
    nationality = "Nepalese"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):  # instance method
        print(f"Name: {self.name}, Age: {self.age}")

    def set_name(self, name):
        self.name = name


person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

person1.get_details()
person2.get_details()
print(Person.nationality)


print(person1.name)  # Alice
person1.name = "Jon"  # Setting value to name attribute. Here "name" is set from outside the class because "name"
# is a public attribute
print(person1.name)  # Jon


person1.set_name("Alex")
print(person1.name)  # Alex