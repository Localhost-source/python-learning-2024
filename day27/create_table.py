from estd_connection import estd_connection

cursor = estd_connection()

# cursor.execute("DROP TABLE STUDENT")

# In python we are using raw query to hit the SQL commands
# While using frameworks (Flask, Django, FastAPI) we do not enter raw SQL commands.
# Rather we use ORM (Object Relational Mapping)
# Popular ORM service for python is SQLAlchemy

sql = """
CREATE TABLE STUDENT(
    ID CHAR(20),
    NAME CHAR(20),
    ADDRESS CHAR(20),
    AGE INT
)
"""

cursor.execute(sql)
print("Table Created Successfully !!")



# from sqlalchemy import models
#
# class Student(models.Model):
#     nme = models.Charfield()
#     age = models.IntField()
#     email = models.EmailField()
#     address = models.Charfield()
#
#
# Student.create(name=, age=, email, address=)
# students = Student.filter(age=20).values("name", "age")
# students = Student.all()