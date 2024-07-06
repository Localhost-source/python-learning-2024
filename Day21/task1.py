"""
Create a class Circle with an instance attribute radius. Create two objects of circle c1 and c2.
Add the radius of the circles and print the result.
•Do the above task using a method and then a magic method.
•Compare the size of the circle and print the result using magic method.
"""
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def add_radius(self, other):
        return self.radius + other.radius
    def __add__(self, other):
        radius = self.radius + other.radius
        return Circle(radius)
    def __gt__(self, other):
        return self.radius > other.radius

c1 = Circle(5)  # creating circle object
c2 = Circle(7)
total = c1.radius + c2.radius
print(total)  # 12
total = c1.add_radius(c2)
print(total)  # 12

total = c1.__add__(c2)
print(total)  # 12
total = c1 + c2
print(total)  # 12
c3 = c1 + c2  # 12
print(c3.radius)  # 12

print(c1 > c2)  # True / False
