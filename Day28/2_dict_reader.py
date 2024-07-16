import csv
filename = "students.csv"

with open(filename, "r") as cr:
    data = csv.DictReader(cr)
    result = [each for each in data]

print(result)
# [{}, {}, {}]