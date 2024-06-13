# What is difference between method and function?
# Methods are also functions but they are functions that should be called with object

# String methods are
# capitalize()
# title()
# upper()
# lower()
# split()
# join()
# find()

a = "hello world"
result = a.capitalize()
print(result)  # Hello world

result = a.title()
print(result)  # Hello World

#lower()
result = a.lower()
print(result)  # hello world

# upper()
result = a.upper()
print(result)  # HELLO WORLD


# split()
a = "helllo world"
result = a.split()
print(result)  # ["hello", "world']

result = a.split("r")
print(result) # ["hello wo", 'ld']

result = a.split("l")
print(result)

r = a.split("h")


# join()
a = ["Hello", "World"]
result = " ".join(a)
print(result)  # Hello World
# r = a.join(" ")  # This is incorrect as join is not a list method

a = "Hello World"
result1 = "a".find("W")
result2 = "a".find("Wor")
print(result1)
print(result2)