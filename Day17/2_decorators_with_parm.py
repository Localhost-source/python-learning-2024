def decorator_func(func):
    def inner_fxn(x, y):
        print("This is decorated")
        return func(x, y)
    return inner_fxn


@decorator_func
def addition(a, b):
    return a + b


# addition = decorator_func(addition)
result = addition(4, 7)
print(result)  # 11


@decorator_func
def info(ms1, msg2):
    return ms1 + msg2


result = info("Hello ", "World")
print(result)


# @decorator_func
def addition(a, b, c):
    return a + b + c


result = addition(1, 2, 3)
print(result)  # 6



############ Final General Solution of a Decorator ################

def decorator_func(func):
    def inner_fxn(*args, **kwargs):
        print("This is decorated")
        return func(*args, **kwargs)
    return inner_fxn

@decorator_func
def addition(a, b):
    return a + b


result = addition(1, 2)
print(result)  # 3

@decorator_func
def addition(a, b, c):
    return a + b + c


result = addition(1, 2, 3)
print(result)  # 6
