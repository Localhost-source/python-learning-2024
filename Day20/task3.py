"""
Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter.
Implement subclasses for different shapes like circle, triangle, and square.
"""
import math


class Shape:
    def __init__(self, length):
        self.length = length


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)
        self.radius = self.length

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def area(self):
        return self.length ** 2

    def perimeter(self):
        return 4 * self.length


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(base)
        self.base = self.length
        self.height = height
    
    def area(self):
        return 1 / 2 * self.base * self.height
