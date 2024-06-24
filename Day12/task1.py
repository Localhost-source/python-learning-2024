#. WAP to delete all the occurrences of a specified character in a given string 
#. S = “All the occurrences of a specified character in a given string”
#. Input = “a”
#. Output = “ll occurrences of  specified chrcter in  given string”


data = "All the occurrences of a specified character in a given string"
result = ""
char = input("Enter a character ")
for each in data:
    if each.lower() == char.lower():
        continue
    result += each

print(result)