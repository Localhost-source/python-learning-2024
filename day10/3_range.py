# range()
# This is also a built-in function
# range() function can take 1 to 3 parameters
# It gives sequence of number in provided range

data = range(100)
print(list(data))  # [0, 1, 2...99]
for i in range(100):
    print(i)  # 0   1   2  ....  99


data = range(2, 9)
print(list(data))   # [2, 3, 4, ....8]


data = range(1, 15, 2)
print(list(data))  # [1, 3, 5, 7, 9, 11, 13]


data = range(-8, -2)
print(list(data))  # [-8, -7, -6, -5, -4, -3]
