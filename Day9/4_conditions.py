# Conditions are used to make decisions in a program
# if conditions check truthy or falsy
# There are few condition variations in python

# 1. Simple "if"
a = 5
if a == 5:
    print("The number is five")

# 2. if...else
a = 5
if a == 5:
    print("The number is five")
else:
    print(f"The number is not 5. the number is {a}")

# 3. if..elif..ladder
a = 5
if a == 1:
    print("The number is one")
elif a == 3:
    print("The number is three")
elif a == 5:
    print("The number is five")
elif a == 6:
    print("The number is six")
else:
    print(f"The number is {a}")


if a == 1:
    print("The number is one")

if a == 3:
    print("The number is three")

if a == 5:
    print("The number is five")


if a == 6:
    print("The number is six")
else:
    print(f"The number is {a}")


# 4. Nested if
a = 5
b = 6
c = 7

if a > b:
    if a > c:
        print(f"{a} is the greatest")
    else:
        print(f"{a} is not the greatest")
elif c > a:
    if c > b:
        print(f"{c} is the greatest")
    else:
        print(f"{c} is not the greatest")

else:
    print("b is greatest")


# 5. ternary if
# It is one-line if..else statement
message = "Hello"
if message == "Hello":
    print("World")
else:
    print("Hello World")

print("World") if message == "Hello" else print("Hello World")


# Truthy or falsy check
a = 10
if a:
    print("a is truthy")
else:
    print("a is falsy")

    a = [1, 2, 3]
if a:
    print("a is truthy")
else:
    print("a is falsy")