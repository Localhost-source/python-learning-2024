# While loop is used with Truthy or Falsy statement similar to if conditions
# It is important to update the condition variable from inside the while loop
# If the condition variable is not updated then the loop runs infinitely


# a = 0
# while a <= 10:  # Here if "a" is not updated then this is infinite
#     print(a)


a = 0
while a <= 10:  # Here if "a" is updated then this is finite loop
    print(a)
    a += 1


data = [1, 2, 3]
while data:
    print("Hello")
    data.pop()


# If you want to create an infinite
while True:
    print("This runs infinitely")