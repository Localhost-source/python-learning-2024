# Tuple is an immutable datatype in python
# It is also iterable; sequence of data ; enclosed within small brackets

# Creating non-empty tuples
a = (1, 2, 3)
a = (1, "a", [1, 2], "b")
# tuple() is a built-in function to define / create a tuple

a = tuple([1, 2, 3])  # Type Casting
print(a)  # (1, 2, 3)

# Creating empty tuple
a = ()
print(a)
b = tuple()
print(b)



# Accessing tuple elements
# Tuple elements are also accessed using Indexing and Slicing

# indexing
vowels = ("a", "e", "i", "o", "u")

print(vowels[4])  # u
print(vowels[0])  # a
print(vowels[2])  # i
# print(vowels[10])  # Error

print(vowels[-1]) # u
print(vowels[-4])  # e
# print(vowels[-10])  # Error


# slicing
data = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
#        0,   1,   2,   3,   4,   5,   6,   7,   8,   9
print(data[2:8])  # ("c", "d", "e", "f", "g", "h")
print(data[:7])  # ("a", "b", "c", "d", "e", "f", "g")
print(data[0:9])  # ("a", "b", "c", "d", "e", "f", "g", "h", "i")
print(data[6:])  # ("g", "h", "i", "j")
print(data[7:3])  # ()
print(data[-8:-3])  # ("c", "d", "e", "f", "g")
print(data[-4: -2]) # ("g", "h")
print(data[2:-3])  # ("c", "d", "e", "f", "g")
print(data[-9:9])  # ("b", "c", "d", "e", "f", "g", "h", "i")
print(data[2:9:2])  # ("c", "e", "g", "i")

print(data[8:2:-1])  # (i, h, g, f, e, d)

print(data[::])  # ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
print(data[::-1])  # ('j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')

