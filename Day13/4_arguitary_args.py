# *args, **kwargs are the arbitrary arguments in Python functions

def addition(*args):
    print(type(args))  # <class 'tuple'>
    print(args)


addition(1, 2)
addition(1, 2, 3)
addition(1, 2, 3, 4)
addition(1, 2, 3, 4, 5)


def addition(*args):
    print(type(args))  # <class 'tuple'>
    print(args)
    print(sum(args))


addition(1, 2)  # 3
addition(1, 2, 3)  # 6
addition(1, 2, 3, 4) # 10
addition(1, 2, 3, 4, 5)  # 15


def addition(**kwargs):
    print(type(kwargs))  # <class 'dict'>


addition(a=1, b=2)
addition(a=1, b=2, c=3)
addition(a=1, b=2, c=3, d=4)
addition(a=1, b=2, c=3, d=4, e=5)


def addition(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    values = kwargs.values()
    print(sum(values))


addition(a=1, b=2)  # 3
addition(a=1, b=2, c=3)  # 6
addition(a=1, b=2, c=3, d=4)  # 10
addition(a=1, b=2, c=3, d=4, e=5)  # 15