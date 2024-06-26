# Lambda are the one-liner functions in python
# They are also called anonymous function in Python because they don't have name. They exists so that we can pass
# them as an argument to a higher order function


def message(msg):
    return msg

result = message("Hello World")
print(result)  # Hello World


message = lambda msg: msg
result = message("Hello")
print(result)  # Hello


def addition(x, y):
    return x + y


addition = lambda x, y: x + y



a = [(5, 2), (1, 1), (7, 0), (10, 12)]

a.sort(key=lambda element: element[1])  # Here sort() is a higher order method / function
print(a)  # [(7, 0), (1, 1), (5, 2), (10, 12)]



students = [
    {"name": "Jon", "age": 15, "address": "KTM"},
    {"name": "Jane", "age": 20, "address": "PKR"},
    {"name": "Alex", "age": 27, "address": "BKT"},
    {"name": "Hary", "age": 10, "address": "LTP"},
    {"name": "Arya", "age": 17, "address": "DHD"},
]


students.sort(key=lambda student: student["age"])

print(students)