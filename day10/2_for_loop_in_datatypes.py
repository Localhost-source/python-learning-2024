# for loop implementation in list, tuple and set is same
#  But it is different in dictionary

# In list
vowels = ["a", "e", "i", "o", "u"]
for each in vowels:
    print(each)  # a  e  i o u


students = [
    {"name": "Alex", "age": 10, "address": "KTM"},
    {"name": "Jane", "age": 19, "address": "KTM"},
    {"name": "Ram", "age": 27, "address": "KTM"},
    {"name": "Sita", "age": 30, "address": "KTM"},
]
result = []
for student in students:
    if student["age"] < 20:
        result.append(student)


print(result)  # [{"name": "Alex", "age": 10, "address": "KTM"}, {"name": "Jane", "age": 19, "address": "KTM"},]

# In dictionary
student = {"name": "Alex", "age": 25, "address": "KTM"}

for each in student:
    print(each)  # name   age   address


keys = student.keys()
for key in keys:
    print(key)  # name  age   address


values = student.values()
for value in values:
    print(value)  # Alex   25   KTM


for item in student.items():  # dict_items([("name", "Alex"), (age, 25), (address, KTM)])
    print(item)  # ("name", "Alex")   (age, 25)   (address, KTM)


for key, value in student.items():
    print(key)  # name age  address
    print(value)  # Alex  25  KTM


data = {1: "Hello", 2: "Python", 3: "Language", 4: "Is", 5: "Learning", 6: "Awesome"}

final_key = 0
final_value = ""
for key, value in data.items():
    if key % 2 == 0:
        final_key += key
        final_value += value

result = {final_key: final_value}

print(result)  # {12: "PythonIsAwesome"}


data = [1, 2, 3, 4, 5]
result = 1
for each in data:
    result *= each

print(result)  # 120
