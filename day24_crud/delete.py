import json
filename = "students.json"


def delete_student():
    id = input("Enter the student id ")
    with open(filename, "r") as fp:
        students = json.loads(fp.read())  # [{}, {}, {}]
    student = list(filter(lambda s: s["id"] == id, students))  # [{}]
    if student:
        student = student[0]
        students.remove(student)
        with open(filename, "w") as fp:
            fp.write(json.dumps(students, indent=2))
        print("Student deleted successfully!")
    else:
        print("Information not available")
    choice = input("Do you want to continue? (y/n) ")
    return True if choice.lower() == "y" else False
