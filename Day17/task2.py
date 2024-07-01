# Create a decorator function login_required which when applied to a function, asks for password.
# If the provided password is "1234" then excute the function else return "Invalid Password. User not authenticated"

def login_required(func):
    def message(*args, **kwargs):
        password = input("Enter password: ")
        if password == "1234":
            return func(*args, **kwargs)
        else:
            return "Invalid Password. User not authenticated"
    return message

@login_required
def addition(a, b, c):
    return a + b + c

result = addition(1, 2, 3)
print(result)

@login_required
def display(msg):
    return msg

result = display("Hello World")
print(result)
