"""
Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
"""
import math

x1 = float(input("Enter x1 "))
x2 = float(input("Enter x2 "))
y1 = float(input("Enter y1 "))
y2 = float(input("Enter y2 "))


def get_distance(point1, point2):  # (2, 5)   (4, 8)
    sq1 = (point2[0] - point1[0]) ** 2
    sq2 = (point2[1] - point1[1]) ** 2
    d = math.sqrt(sq1 + sq2)
    return d


c1 = (x1, y1)
c2 = (x2, y2)

result = get_distance(c1, c2)
result = round(result, 2)
print(result)
