# Load CSV to database student table

import csv
from day27.estd_connection import estd_connection
filename = "students.csv"

cursor = estd_connection()

with open(filename, "r") as cr:
    data = csv.DictReader(cr)
    for each in data:
        id = each["id"]
        age = each["age"]
        name = each["name"]
        address = each["address"]
        sql = f"""
        INSERT INTO STUDENT (id, name, age, address) VALUES ('{id}', '{name}', {age}, '{address}')
        """
        cursor.execute(sql)
print("Loaded successfully!")