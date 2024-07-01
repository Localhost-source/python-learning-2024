# Create a decorator function which when applied to another function (that returns a string), it gives
# the uppercase value

def to_upper(func):
    def wrapper(msg):
        return func(msg).upper()
    return wrapper

@to_upper
def display(msg):
    return msg

result = display("hello world")
print(result)
