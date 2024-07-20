# Namespace defines the scope of variables, functions and classes
# There are four types of namespaces in python defined by LEGB rule
# L => Local Scope
# E => Enclosed Scope
# G => Global Scope
# B => Builtin Scope


# Built-in Scope
# The classes, functions and modules with built-in scope can be used in any python file simply by import

import csv  # Builtin Scope
from csv import Dialect  # Builtin Scope
print("Hello World")  # Builtin


# Global Scope
# Global scope is limited to a particular module
# If you want to use such objects in other modules you need to import
a = 2
def message():
    return "Hello"


print(a)
print(message())


# Local Scope
a = 5  # Global Scope
b = 2  # Global Scope

def addition(a, b):
    print(a)  # 2  => Local Scope
    print(b)  # 3  => Local Scope
    return a + b


result = addition(2, 3)
print(result)  # 5
print(a)  # 5
print(b) # 2


# Enclosed Scope

a = 2
def fxn():
    global a
    a = 3
    print(a) # 3

print(a)  # 2
fxn()
print(a)  # 3

z = 1
print(z)


def add():
    print(5)
    messg()

add()
def messg():
    print(z)   # 1

messg()  