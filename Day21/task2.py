"""
Create a class Department with parameters name and number_of_students. 
Create a method total students, which takes department object as a parameter and return 
the total number of students from all departments.
"""

class Department:
    def __init__(self, name, number_of_students):
        self.name = name
        self.number_of_students = number_of_students

    def total_students(self, *args):  # self=> d1, args=> (d2, d3)
        students = 0
        for x in args:
            students = students + x.number_of_students
        return self.number_of_students + students



d1 = Department("IT", 5)
d2 = Department("Civil", 10)
d3 = Department("Elex", 15)
total = d1.total_students(d2, d3)
print(total)