# Decorators are the function based design-pattern / architicture in python which is used to decorate
# another function
# Here decorate means to add another functionality in a function
# Decorator is also a higher order function


# Decorators are a function which takes another function as an argument and returns a function

def decorator_func(func):
    def inner_fxn():
        print("I am decorating the function")
        return func()
    return inner_fxn


# @decorator_func
def message():
    return "Hello World"


message = decorator_func(message)
result = message()
print(result)


# result = message("Hello World")
# print(result)  # Hello World


@decorator_func
def addition():
    return 5


print(addition())
