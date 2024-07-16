import json
filename = "students.json"


def update_student():
    id = input("Enter student id ")
    key = input("Enter the info you want to update ")
    value = input(f"Enter the new {key} ")

    if key not in ["name", "age", "address"]:
        print("Info not available")
    else:
        with open(filename, "r+") as fp:
            students = json.loads(fp.read())  # [{"name": "Jon", "id": 1}, {"name": "Alex", "id": 2} ]
            student = list(filter(lambda s: s["id"] == id, students))  # [{"name": "Alex", "id": 2}] or []
            if student:
                student = student[0]  # {"name": "Alex", "id": 2}
                index_of_student = students.index(student)
                student[key] = value  # {"name": "Hary", "id": 2}
                students[index_of_student] = student
                fp.seek(0)
                fp.write(json.dumps(students, indent=2))
                print("Student updated successfully !")
            else:
                print("Information is not available")
    choice = input("Do you want to continue? (y/n) ")
    return True if choice.lower() == "y" else False
