# Set is a mutable datatype in Python
# It is also an iterable. Sequence of elements separated by comma and enclosed within curly braces
# Unlike list and tuple, set doesn't support indexing and slicing because order of elements doesn't matter in set

a = [1, 2, 3]  # list
b = [2, 1, 3]
print(a == b)  # False

a = {1, 2, 3}
b = {3, 2, 1}
print(a == b)  # True in set


# Set is mutable but the items within set must be immutable
a = {0.0, False, "hello"}  # Valid
# a = {[1, 2], 4}  # Invalid
a = {(1, 2), 4}  # Valid
# a = {(1, 2, [1, 2]), 4}  # Invalid


data = {(1, 2): "Hello"} # Valid
# data = {(1, 2, ["a", "b"]): "Hello"}  # Invalid


# In set, items do not repeat
a = {1, 1, 2, 1, 3, 3}
print(a)  # {1, 2, 3}

b = ["a", 1, 2, 1, "a", "b"]
a = set(b)
print(a)  # {"a", 1, 2, "b"}

# Creating an empty set
a = {}
print(a)  # empty dictionary

a = set()
print(a)  # empty set



# Adding and removing set items
# add()
s1 = {1, 2, 3}
result = s1.add(5)
print(result)  # None
print(s1)


# update()
s1 = {1, 2, 3}
s1.update([4, 5, 6])
print(s1)  # {1, 2, 3, 4, 5, 6}


# remove()
s1 = {"a", "b", "c", "d"}
s1.remove("c")
print(s1)  # {"a", "b", "d"}

# s1.remove("z")  # KeyError


# discard()
s1 = {"a", "b", "c", "d"}
s1.discard("d")
print(s1)  # {"a", "b", "c"}
s1.discard("z")  # It does nothing (No error)
print(s1)  # {"a", "b", "c"}

# clear()
s1 = {"a", "b", "c", "d"}
s1.clear()
print(s1)  # set()