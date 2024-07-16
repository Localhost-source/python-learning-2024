# We can use "json" module to parse the JSON data in python
# loads => reading a JSON file and changing it to python dictionary / list
# dumps => Writing python list/dictionary in a json file in JSON format

import json

filename = "student.json"
filename1 = "students.json"
student = {'name': "Alex", "age": 21, "address": "KTM"}

students = [
    {'name': "Alex", "age": 21, "address": "KTM"},
    {'name': "Alex", "age": 21, "address": "KTM"},
    {'name': "Alex", "age": 21, "address": "KTM"}
]

with open(filename, "w") as fp:
    fp.write(json.dumps(student))


with open(filename1, "w") as fp:
    fp.write(json.dumps(students, indent=2))




with open(filename, "r") as fp:
    data = json.loads(fp.read())

print(data)

with open(filename1, "r") as fp:
    data = json.loads(fp.read())

print(data)
