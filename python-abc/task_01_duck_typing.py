#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        try:
            if radius < 0:
                raise ValueError("Radius cannot be negative")
            self.radius = radius
        except ValueError as e:
            print(e)

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
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    circle = Circle(5)
    shape_info(circle)
    rectangle = Rectangle(4, 7)
    shape_info(rectangle)
    try:
        circle_negative = Circle(-5)
        shape_info(circle_negative)

    except ValueError as e:
        print(e)
