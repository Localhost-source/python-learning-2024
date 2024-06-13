a = 1
print(type(a))  # int

a = 1,   # This is tuple packing
print(type(a))  # tuple
print(a)  # (1,)
print(a[1])
a = (1, "")
print(type(a))
print(a[1])  # ""
a = ("", "Hello")
print(a)


# Packing
a = 1, 3  # This is also tuple packing
print(a)  # (1, 3)

# Unpacking

a, b = 1, "HELLO"
print(a)  # 1
print(b)  # 2

a, b = (1, 2)
print(a)  # 1
print(b)  # 2

# x, y = 1, 2, 3  # This raises error
# x, y, z  =1, 2,  # This also raises error
