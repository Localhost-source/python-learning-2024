# count()
a = (1, 2, 3, 1, 2, 2, 3, 3, 2, 2, 2)
result = a.count(2)
print(result)  # 6


# index()
vowels = ("a", "e", "i", "o", "u", "a", "i", "e", "u")
result = vowels.index("e")
print(result)  # 1

result = vowels.index("e", 2)
print(result) # 7

result = vowels.index("e", 2, 8)
print(result)  # 7

result = vowels.index("u", 5, 8)  # It checks "u" in range 5th to 7th index. This raises error
print(result)  #



# Tuple Operations
# 1. Concatenation (+)
# 2. Repetition (*)
# 3. Membership ("in" and "not in")

# Concatenation
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)  # (1, 2, 3, 4, 5, 6)


# Repetition
a = (1, 2) * 3
print(a) # (1, 2, 1, 2, 1, 2)


# Membership Operation
print(2 in (2, 3, 4))  # True
print(2 not in (2, 3, 4))  # False