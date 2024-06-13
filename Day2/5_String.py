# Strings are immutable datatypes in python
# They are iterables (Iterables are the sequence of data)
# They are sequence of characters enclosed within "", '', or """""", ''''''

# Creating non-empty string
messg = "Hello"
print(messg)

messg = 'Hello'
print(messg)

messg = """
        Hello I am learning Python.
        Python is a high level language
        """
print(messg)

messg = '''
        Hello I am learning Python.
        Python is a high level language
        '''
print(messg)

m = "Hello I am learning Python. \n" \
"Python is a high level language"
print(m)


# Empty strings
a = ""
b = ''
c = ''''''
d = """"""
e = str()


# Accessing string elements
# String elements can be accessed using Indexing and Slicing

data = "Hello. I am learning python"
# Indexing
# Indexing in iterables starts with 0
print(data[0])  # 'H'
print(data[4])  # 'o'
print(data[6])  # ' '
# print(data[100])  # IndexError

print(data[-1])  # n
print(data[-3])  # h
# print(data[-100])  # IndexError

print(data[26] == data[-1])


# Slicing
# Slicing is taking a slice / subset from the main set of data
# We can do slicing using [:]
data = "Hello. I am learning python"

print(data[2:8])  # "llo. I"
d = data[2:8]
print(d)  # "llo. I"
print(data[8:2])  # ""


print(data[0:9])  # "Hello. I "
print(data[:9])  # "Hello. I "

print(data[7:])   # " am learning python"
print(data[-8:-2])  # g pyth
print(data[-2:-8])  # ""

print(data[1:9:2])  # "el.I"

print(data[3:-2])  # "lo. I am learning pyth"