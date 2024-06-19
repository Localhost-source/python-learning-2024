# len()
# len() works with any iterable
# It returns the length of an iterable


size = len(["a", "e", "i"])
print(size)  # 3

size = len("Hello World")
print(size)  # 11

size = len({"name": "Jon", "age":12})
print(size)  # 2


# sum()
# Sum also takes iterable as an input
# But, the iterable should be the sequence of numbers
# It gives sum of all the elements

value = [1, 2, 2.2, -3]
result = sum(value)
print(result)  # 2.2

d = {"1": 1, "2": 2}
result = sum(d.values())
print(result)


value = [1, 2, 2.2, 1, -3, 4]
result = sum(value, 10)
print(result)  # 17.2


# max()
# It also takes iterable as an input
# It returns the maximum item from the iterable
value = [1, 2, 2.2, 1, -3, 4]
print(max(value))  # 4

value = ["a", "z", "p", "e", "Z"]
# In strings it return the character with maximum ASCII value
print(max(value))


value = ["dog", "Zoo", "cat", "yel", "zo"]
print(max(value))  # zo


# min()
# It also takes iterable as an input
# It returns the minimum item from the iterable
value = [1, 2, 2.2, 1, -3, 4]
print(min(value))  # -3

value = ["a", "z", "p", "e", "Z"]
# In strings it return the character with min ASCII value
print(min(value))  # "Z"


value = ["dog", "Zoo", "cat", "yel", "zo"]
print(min(value))  # Zoo


# sorted()
# It always returns a list regardless of the provided iterable datatype 
data = [5, 4, 1, 100, 40, -30]
result = sorted(data)
print(result)  # [-30, 1, 4, 5, 40, 100]

data = (5, 4, 1, 100, 40, -30)
result = sorted(data)
print(result)  # [-30, 1, 4, 5, 40, 100]

data = "Hello World"
result = sorted(data)
# It compares the ASCII value of each characters in the string and arrange in ascending order
print(result)  # [' ', 'H', 'W', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r']


data = [5, 4, 1, 100, 40, -30]
result = sorted(data, reverse=True)
print(result)  # [100, 40, 5, 4, 1, -30]

data = (5, 4, 1, 100, 40, -30)
result = sorted(data, reverse=True)
print(result)  # [100, 40, 5, 4, 1, -30]

data = "Hello World"
result = sorted(data, reverse=True)
# It compares the ASCII value of each characters in the string and arrange in ascending order
print(result)  #


# reversed()
data = [5, 4, 1, 100, 40, -30]
result = reversed(data)
print(result)  # iterator-object
print(list(result))  # object  [-30, 40, 100, 1, 4, 5]