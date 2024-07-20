# Classes whose objects don't exist / We can't make objects of such class are abstract classes
# It is only required for the inheritance in other classes
# It's independent object doesn't make sense. For example DateTimeClass
#
# class DatetimeTable:
#     created_at =
#     updated_at =
#
# class Person(DatetimeTable):
#     name = Charfield
#     age = IntField
#     address = Charfield
#
#     created_at = DatetimeField
#     updated_at = DateTimeField
#
#
# class Vehicle:
#     company =
#     color=
#     engine_type =
#
#     created_at = DatetimeField
#     updated_at = DateTimeField


# We can import a modue from builtin python to create an abstract class

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Cat(Animal):
    age = 20

    def sound(self):
        return "meow"


class Dog(Animal):
    age = 20

    def sound(self):
        return "bark"


c = Cat()
print(c.age)
print(c.sound())