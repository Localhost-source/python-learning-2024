# Loops are used to perform certain task repeatedly in programming
# There are two types of loops in python

# 1. For Loop
# 2. While Loop


# For Loop
# For loops are used in iterables / sequential datatypes.
# It can be executed in any iterable like list, tuple, dict_keys, dict_values, range(), set, dictionary, iterators

vowels = ["a", "e", "i", "o", "u"]
for each in vowels:
    print(each)  # a  e  i o u
a = 1
print(a)

a = [1, 2, 3, 4]
result = []
for i in a:
    result.append(i + 10)

print(result)  # [11, 12, 13, 14]
