# break, continue and pass are used as control statements in python
# They can alter the normal flow of a program


# break
data = ["a", "b", "c", "d", "e", "f"]
for each in data:
    if each == "c":
        break
    print(each)

a = 0
while a <= 10:
    if a == 5:
        break
    print(a)
    a += 1


# continue
data = ["a", "b", "c", "d", "e", "f"]
for each in data:
    if each == "c":
        continue
    print(each)


a = 0
while a <= 10:
    if a == 5:
        a += 1
        continue
    print(a)
    a += 1

    # pass
# pass is used for making the syntactically correct code for future placeholders

age = 5
if age >= 30:
    # TODO: Nabin. Need changes here
    pass

# pass is also used to fail-silently the code
try:
    a = 1 + "Hello"
except:
    pass