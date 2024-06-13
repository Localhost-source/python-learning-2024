# copy() method in python list

a = [1, 2, 3, 4]
b = a  # This is pass by reference
print(a is b)  # True

b.append(5)
print(a)  # [1, 2, 3, 4, 5]

b = a.copy()  # Pass by value
b.append(6)
print(b)  # [1, 2, 3, 4, 5, 6]
print(a)  # [1, 2, 3, 4, 5]


# But there are two types of copy
# Shallow Copy
# Deep Copy


# Shallow Copy
a = [1, 2, 3, [4, 5]]
b = a.copy()
b[0] = 6

print(b)  # [6, 2, 3, [4, 5]]
print(a)  # [1, 2, 3, [4, 5]]


b[3][1] = 7
print(b)  # [6, 2, 3, [4, 7]]
print(a)  # [1, 2, 3, [4, 7]]


# a = [1, 2, 3]
# a[2] = 7

# Deepcopy
from copy import deepcopy

b = deepcopy(a)
print(a)
print(b)

b[3][1] = 8
print(b)  # [1, 2, 3, [4, 8]]
print(a)  # [1, 2, 3, [4, 7]]
