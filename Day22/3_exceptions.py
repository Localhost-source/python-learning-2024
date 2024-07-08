# There are broadly two types of errors
# Syntactic Error
# Non-syntactic Error
    # Logical Errors
    # Runtime Errors


# Syntactic Error
# a = 5
# if a:  # Indentation Error
#
# b = 12
# print(b)
#
# print(x)  # NameError


# Non Syntactic Error
# ValueError
# TypeError
# IndexError
# KeyError
# ZeroDivisionError error
# Attribute Error
# ModuleNotFoundError


# ValueError
data = int(input("Enter a number "))
print(data)


# TypeError
a = 1
b = "Hello"
print(a + b)


# IndexError
vowels = ["a", "e", "i", "o", "u"]
print(vowels[100])  # IndexError


# KeyError
student = {"name": "Jon", "roll": 30}
address = student.get("address")  # None


name = student["name"]
address = student["address"]  # KeyError


# ZeroDivisionError
print(32/0)


# AttributeError
class A:
    x = 2


obj = A()
print(obj.y)  # Attribute Error

a = [1, 2, 3]
a.append(4)
a.appendd(4) # Attribute Error

a = 1
a.sdfgds()  # Attribute Error


# import oss   # ModuleNotFoundError