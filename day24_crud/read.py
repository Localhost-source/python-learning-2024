import json
filename = "students.json"


# def read_student():
#     id = input("Enter the student id ")
#     with open(filename, "r") as fp:
#         students = json.loads(fp.read())  # [{"id": 1}, {"id": 2}, {"id": 3}]
#     for student in students:
#         # print(type(student))  # dictionary
#         if student["id"] == id:
#             print(student)
#             break
#     else:
#         print("The information is not available")
#     choice = input("Do you want to continue? (y/n)")
#     return True if choice.lower() == "y" else False




def read_student():
    id = input("Enter the student id ")
    with open(filename, "r") as fp:
        students = json.loads(fp.read())  # [{"id": 1}, {"id": 2}, {"id": 3}]
    student = list(filter(lambda s: s["id"] == id, students))  # [{}] or []
    if student:
        print(student[0])
    else:
        print("Information is not available")
    choice = input("Do you want to continue? (y/n) ")
    return True if choice.lower() == "y" else False
