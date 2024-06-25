# 1. Functions are the block of reusable code.
# 2. We use "def" key to create a function in python
# 3. Function names follow identifier rules. By pep-8 convention python functions should follow snake case pattern


def Addition():
    pass

def num_addition():
    pass

def NumAddition():
    pass

def num2():
    pass

# These all are valid function names

# There are two parts of a function; i) function definition ii) function call
# function definition
def addition(a, b):
    return a + b

# function call
result = addition(2, 3)
print(result)

result = sum([1, 2, 3])
print(result)