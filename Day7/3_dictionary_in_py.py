# Dictionary is a mutable data type in python
# It is a combination of key and value pair separated by comma enclosed 
# within curly braces

# Creating non-empty dictionary
student = ["jon", "KTM", 30] # List

student = {"name": "Jon", "age": 30, "address": "KTM"}
student = dict(name="Jon", age=30, address="KTM")

student = {"full name": "Jon", "age": 30, "address": "KTM"}
print(bool(student)) # True
# student = dict(full name="Jon", age=30, address="KTM")
# This raises error as "full name" key has a space in it.
# For such case we cannot use dict() function to create a dictionary


# Creating a empty dictionary
student = {}  # This is empty dict
student = dict() # This is also empty dict

print(bool(student))  # False



# Accessing dictionary elements
student = {"name": "Jon", "age": 30, "address": "KTM"}
print(student["age"])  # 30

# student["roll"]  # this raises KeyError

# We also have a dictionary method get() to access dictionary elements
name = student.get("name")
print(name)  # Jon

roll = student.get("roll")
print(roll)  # None

roll = student.get("roll", 3)
print(roll)  # 3

name = student.get("name", "Jane")  # Here Jane is just a default value / fallback. It gives
# priority to the name already present in dictionary
print(name)  # Jon


# Adding and Updating dictionary values
student = {"name": "Jon", "age": 30, "address": "KTM"}
student["roll"] = 3
print(student)  #  {"name": "Jon", "age": 30, "address": "KTM", "roll":3}

student["name"] = "Jane"
print(student)  # {"name": "Jane", "age": 30, "address": "KTM", "roll":3}

# We can also use update() method in dictionary to add and update values
student = {"name": "Jon", "age": 30, "address": "KTM", "roll":3}
student.update(email="j@email.com", fname="Sth")
student.update({"phone": 9898789878, "classroom": 2})

print(student)  # {"name": "Jon", "age": 30, "address": "KTM", "roll":3, 
# "email": "j@email.com", "phone": 9898789878, "classroom": 2, "fname": "Sth"}



# Rules for dictionary keys and values
# Any data / datatype can be dictionary value. There is no restriction in dictionary values
# But, dictionary keys can only be immutable datatypes

student = {1: "Ram", 2: "Sita"}  # This is a valid dictionary, 1 is int which is immutable
print(student)  # 

student = {(1, 2): [1, 2]}  # This is also valid because tuple is immutable and can be used
# as dict key
print(student) 

# .student = {(1, [1, 2]): "Hello"}  # Invalid
print(student)  # 


# Storing multiple data as a dictionary
students = [
    {"name": "Jon", "age": 30, "address": "KTM", "roll":3},
    {"name": "Jane", "age": 32, "address": "KTM", "roll":4},
    {"name": "Hary", "age": 12, "address": "BKT", "roll":5},
]

student = students[2]
address = student["address"]
print(address)

address = student.get("address")
address = students[2]["address"]
print(address)

address = students[2].get("address")
print(address)


students = {
    "student1":{"name": "Jon", "age": 30, "address": "KTM"},
    "student2":{"name": "Jane", "age": 30, "address": "BKT"},
    "student3":{"name": "Alex", "age": 21, "address": "LTP"},
    }

age = students["student2"]["age"]
print(age)

age = students["student2"].get("age")
print(age)  # 30

age = students.get("student2").get("age")
print(age)