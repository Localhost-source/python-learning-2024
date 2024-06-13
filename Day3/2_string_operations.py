# We can perform following operations in string

# Concatenation

a = "Hello"
b = "I am learning Python"
result = a + b
print(result)  # HelloI am learning Python

result = a + " " + b
print(result)  # Hello I am learning Python

print(a, b)


# Repetition Operation / Broadcast Operation
a = "Hello" * 2
print(a)  # HelloHello

# Membership Operation

print("H" in "World")  # False
print("H" not in "World")  # True
print("W" in "World")  # True
print("W" not in "World")  # False