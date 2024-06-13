# Boolean are immutable datatype
# True and False are the boolean types in Python
# True and False are also the keywords

# Operations that gives boolean type
# Comparison Operations
print(5 > 2)  # True
print(5 != 5) # False


# Logical Operation
print(True and False)  # False
print(False or True)  # True
print(not False)  # True


# Membership Operation
print(2 in (3, 4, 5))  # False
print(2 in (2, 4, 5))  # True
print(2 not in (2, 4, 5))  # False


# Identity Operation
a = ()
b = ()
print(a is b)  # True
print(a is not b)  # False


# Concept of Truthy and Falsy

# Truthy
# All those datatypes which are non-empy, non-zero including True itself are truthy
a = 12
b = "Hello"
c = [1, 3, -1]
d = ("a", "b", "c")
e = {"name": "Jane"}
f = {1, 2, 3}
g = True
h = 2.2
print(bool(a)) # True
print(bool(b)) # True
print(bool(c)) # True
print(bool(d)) # True
print(bool(e)) # True


# Falsy
# All those empty data, zero, None and False itself are Falsy
a = 0
b = 0.0
c = []
d = {}
e = set()
f = ""
g = None
h = False
i = ()
print(bool(a)) # False
print(bool(b)) # False
print(bool(c)) # False
print(bool(d)) # False
print(bool(e)) # False


a = 5
if a == 5:
    print("The number is five")


if a:
    print("a is non-zero")

data = [1, 2, 30]
if data:
    for i in data:
        print(i)


# Boolean is a integer sub class in python
# You can use boolean as integer
# True is 1 and False is 0 and it can be used in arithmetic operations


a = True + True
print(a)  # 2

b = False * 70
print(b)  # 0