# String formatting is a way to replace a variable name in a string to create a new string
# f-strings are the famous way in python to perform string formatting
# f-string is also sometimes called as template literals

language = "Python"
result = f"I am learning {language}"

a = "Hello"
b = "World"
c = f"{a} {b}"
print(c)


# Before python version 3.6 f-strings were not introduces
language1 = "Python"
language2 = "JS"
message = "Hello I am learning {} and I am also learning {}".format(language1, language2)
message = "Hello I am learning {} and I am also learning".format(language2, language1)
print(message)