"""
Create a dictionary student with keys id, name, age, department. Take a input from the user, which info (id, name, age or department) 
he wants to access and print the result. Handle the possible exceptions has context menu
"""

student = {"id": 1, "name": "Hary", "age": 40, "department": "IT"}

try:
    key = input("Enter the value you want to access ")
    value = student[key]
except KeyError:
    print("There is no info provided")
else:
    print(f"The {key} of the student is {value}")
