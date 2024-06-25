# There is certain order of arguments in python functions
# If we mess up with this order then it raises error
# Order of arguments is:
# 1. Positional
# 2. Keyword
# 3. *args
# 4. **kwargs


def addition(a, b, c=10):
    return a + b + c


addition(1, 2, c=20)


def display(a, b, c, d=1, e=2, f=3, *args, **kwargs):
    print(a)  # 10
    print(b)  # 23
    print(c)  # 11
    print(d) # 70
    print(e)  # 15
    print(f)  # 21
    print(args)  # (22, 23, 32, 45, 60)
    print(kwargs) # {"x": 12, "y": 19, "z": 50}


display(10, 23, 11, 70, 15, 21, 22, 23, 32, 45, 60, x=12, y=19, z=50)
# We cannot send value for same parameters multiple times