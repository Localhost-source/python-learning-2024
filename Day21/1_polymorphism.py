# Polymorphism refers to "Many Forms"
a = 1
b = 2
c = a + b
print(c)  # Sum
r = "Hello" + "World"
print(r)  # HelloWorld

# In this example the same operator "+" is behaving differently for different datatypes. This is an example of
# Polymorphism

a = len([1, 2, 3])
b = len((1, 2, 3))
# This can also be an example of polymorphism

# Is function / method overloading possible in python?
# It is not possible like in other OOP languages like C++ and Java



# Function / Method Overloading
def addition(a, b):  # This has been overriden from the below addition function. Function Overloading is not possible
    return a + b


def addition(a, b, c=0):
    return a + b + c


result1 = addition(2, 3)
result2 = addition(5, 6, 7)
print(result2)
print(result1)