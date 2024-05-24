#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi

#  Shape Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

#  Circle and rectangle classes
class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError('"Radius cannot be negative"')
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

        def shape_info(shape):
            print(f"area: {shape.area()}")
            print(f"Perimeter: {shape.perimeter()}")
