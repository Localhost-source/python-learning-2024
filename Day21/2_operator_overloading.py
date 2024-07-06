a = 5
b = 2
result = a + b
print(result)  # 7

class int:
    def __add__(self, other):
        pass

    def __hello__(self):  # This is not a magic method. This is a private hello__() method
        pass


class str:
    def __add__(self, other):
        pass


result = a.__add__(b)
print(result)


a = "Hello"
b = "World"
result = a.__add__(b)

# Each operators has their double underscore methods (dunder methods) or magic methods in python
# If we define the magic_method and add our own implementation in that method then it is called as operator overloading