# CSV stands for comma separated values
# It is also a file format similar to JSON
# Python also has a builtin support for CSV

import csv
filename = "students.csv"

with open(filename, "r") as cr:
    data = csv.reader(cr)
    result = []
    for count, each in enumerate(data):
        if count == 0:
            continue
        result.append({"id": each[0], "name": each[1], "age": each[2], "address": each[3]})

print(result)

with open(filename, "r") as cr:
    data = csv.reader(cr)
    data = list(data)  # [["id", "name"], [1, "Hary", 25], [2, "Ram"]]
    print(data)
    keys = data.pop(0)  # ["id", "name", "age", "address"]
    result = []
    for each in data:
        result.append({keys[i]: each[i] for i in range(len(keys))})

print(result, "<--------")

"""[
    {
        "id": 1, "age": 25, "name": "Ram", "address": "KTM"
    },
    {
        "id": 1, "age": 25, "name": "Ram", "address": "KTM"
    },
]"""