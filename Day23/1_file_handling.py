# We can handle files using python
# There are different modes to open, write and update a file
# The modes are
# Write Mode (w)
# Read Mode (r)
# Append Mode (a)
# Read and Write (r+)
# Write and Read (w+)
# Append and Read (a+)
# Exclusive Mode (x)

# JSON Handling
# CSV Handling

# Write mode
fp = open("example.txt", "w")
fp.write("Hello World")
fp.close()

fp = open("example.txt", "w")
fp.write("I am learning file handling")
fp.close()

# In write mode the content is completely overridden by new content

# Read Mode
fp = open("example.txt", "r")
data = fp.read()
print(type(data))  # string type.
print(data)
fp.close()

"""
I am learning file handling
Hello World
This is example
[1, 2, 3]
"""

fp = open("example.txt", "r")
try:
    a = 2
    b = 0
    result = a / b
except:
    print("Sth")
finally:
    fp.close()