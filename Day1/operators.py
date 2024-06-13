# Python code can be executed from two different ways
# Python Shell
# Using file with python extension (.py)

# How to execute a python file
a = 1
b = 2
print(a + b)  # print() is built-in function
print("Hello World")

# Operators in python
# 1. Arithmetic
# 2. Relational
# 3. Logical
# 4. Assignment
# 5. Membership
# 6. Identity


# 1. Arithmetic Operators (+, -, /, *, //, %, **)
a = 1
b = 2
c = a + b
print(c)  # 3

c = a - b
print(c)  # -1

c = a * b
print(c)  # 2

c = a / b
print(c)  # 0.5

c = 5 // 2  # // is a floor division
print(c)  # 2

c = -5 // 2  # floor division
print(c)  # -3


a = 10
c = a % 3  # Modulus Operator
print(c)  # 1
c = a % 5
print(c)  # 0

a = 2 ** 2  # Exponent operator
print(a)  # 4


# Relational Operations / Comparison Operation
# It is used to compare two values
# >, <, >=, <=, ==, , !=
# The result of relational operation is boolean (True / False)

a = 10
b = 4
c = a > b
print(c)  # True

print(a != b)  # True
print(a == b)  # False

print(10 >= 10)  # True
print(10 <= 10)  # True


# Logical Operation
# and, or, not

# E1    E2    And       Or
# True  True  True      True
# True  False  False    True
# False True   False    True
# False False  False    False

# E     Not
# True  False
# False True


# Assignment
# Assignment opertors are used to assign value to a variable
# "=" is the most basic assignment operator
# +=, -=, *=, /= etc. are also assignment operator

a = 1
print(a)
a = a + 1
print(a)  # 2
a = a + 2
print(a)  # 4

a += 1
print(a)  # 5

a -= 1
print(a)  # 4

a *= 2
print(a) # 8


# Membership Operators
# It is used to check whether an element is a member of sequence or not
# Result of membership operation is also a boolean (True/False)
# "in" and "not in" are the mebership operators

a = [1, "a", "Hello", 2.5, -4]
b = 2

print(b in a)  # False
print("A" in a)  # False
print("Hello" in a)  # True
print(b not in a)  # True
print("Hello" not in a)  # False

a = 1
datatype = type(a)  # here type() is built-in function
print(datatype)  # int

a = [1, "a", "Hello", 2.5, -4]
datatype = type(a)  # here type() is built-in function
print(datatype)  # list


a = "hello"
datatype = type(a)  # here type() is built-in function
print(datatype)  # str

# Identity Operator
# It checks whether two or more data have same reference (memory location) or not
# "is" and "is not" are the identity operators

a = 1
b = 1
print(a is b) # True
print(a is not b)  # False

a = []
b = []
print(a is b)  # False
print(a == b)  # True