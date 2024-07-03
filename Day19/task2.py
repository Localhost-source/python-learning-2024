
"""
Create a class Person with instance attributes name and age.
Create a method get_details in this class to print name and age.
Create another class Employee with instance attributes salary and designation and inherits
the Person class. Create a method get_details in this class to print name, age,
salary and designation of the Employee.

"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):  # instance method
        return f"Name: {self.name}, Age: {self.age}"


class Employee(Person):
    def __init__(self, name, age, salary, designation="Python Dev"):
        self.salary = salary
        self.designation = designation
        super().__init__(name, age)

    def get_details(self):
        x = super().get_details()
        return f"{x}. Salary is {self.salary} and designation is {self.designation}"


emp = Employee("Alice", 25, 25000)
print(emp.get_details())