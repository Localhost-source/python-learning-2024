# Inputs provided during function definition are parameters
# Values passed during function call are arguments

# Types of parameters / arguments in python
# 1. Positional argument
# 2. Keyword argument
# 3. Arbitrary argument


# 1. Positional Argument
# They are the compulsory argument for a function

def addition(a, b):
    return a + b

# result = addition("a")  # Error
# result = addition("a", "b", "c") # Error
result = addition(5, 9)
print(result)  # 14


# 2. Keyword Argument

def addition(a, b, c=10):  # Here c is default parameter
    return a + b + c

result = addition(4, 5)
print(result)  # 19

# result = addition(5)  # Error

result = addition(2, 3, 4)
print(result)  # 9

# Variations while calling a python function
def addition(a, b, c=10):  # Here c is default parameter
    return a + b + c


result = addition(a=2, b=3)  # Here a and b are keyword arguments
print(result)  # 15

result = addition(b=4, a=10)
print(result)  # 24

result = addition(5, b=12, c=2)
print(result)  # 19