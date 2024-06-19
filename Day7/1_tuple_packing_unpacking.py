
a = 1
print(type(a))  # int

a = 1,  # Packing
print(type(a))  # Tuple

a = 1, 2  # Tuple Packing

a, b = 1, 2  # Tuple packing Unpacking
print(a)  # 1=> int
print(b)  # 2 = int


# a, b = 1, 2, 3
# a, b , c = 1, 2

# Swap two variables in Python
a = 1
b = 2

c = a
a = b
b = c



print(a)  # 2
print(b)  # 1

# Swapping two variables using tuple unpacking
a, b = b, a


vowels = ["a", "i", "o", "u"]
vowels[1] = "e"  # Valid  # ["a", "e", "o", "u"]
# Item assignment is possible in List being mutable

vowels = ("a", "e", "i", "o")
vowels[1] = "u"   # Invalid
# Tuple being immutable, item assignment is not possible