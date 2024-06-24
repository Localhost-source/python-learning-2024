
# Comprehension is an elegant one-liner way to create list and dictionary

a = list(range(11))
print(a)

a = [each for each in range(11)]
print(a)  # [0, 1, 2...10]

a = [1, 2, 3, 4, 5, 6]
result = [each+10 for each in a]

print(result)  # [11, 12, 13, 14, 15, 16]


a = [1, 2, 3, 4, 5, 6]
result = [each+10 for each in a if each % 2 != 0]
print(result)  # [11, 13, 15]

a = [1, 2, 3, 4, 5, 6]
result = [each+9 for each in a if (each+9) % 2 == 0]
print(result)

result = [each+9 for each in a if each % 2 == 1]
print(result)  # [10, 12, 14]

result = [each+9 for each in a if each % 2 != 0]
print(result)

# Dictionary Comprehension
student = [("name", "Ken"), ("age", 31), ("email", "k@email.com")]

student_dictionary = {key: value for key, value in student}


result = {key : key ** 2 for key in range (1, 6)}
print(result)   

result = {key : key ** 2 for key in range (1, 6) if key % 2 != 0}
print(result)   


students = [
    {"name": "Alex", "age": 10, "address": "KTM"},
    {"name": "Jane", "age": 19, "address": "KTM"},
    {"name": "Ram", "age": 27, "address": "KTM"},
    {"name": "Sita", "age": 30, "address": "KTM"},
]

result = [student for student in students if student["age"] < 20]

print(result)