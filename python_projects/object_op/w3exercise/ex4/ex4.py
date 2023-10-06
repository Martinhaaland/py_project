#Write a Python program to create a class that represents a shape. 
#Include methods to calculate its area and perimeter. 
#Implement subclasses for different shapes like circle, triangle, and square.
class Shape:
    def __init__(self):
       pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        return 2 * self.radius * 3.14
    def area(self):
        return (self.radius ** 2) * 3.14

class Triangle(Shape):
    def __init__(self):
        pass
    def area(self, base, height):
        return 1/2 * base * height
    def perimeter(self, first, second, third):
        return first +second + third

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area():
        return self.side ** 2
    def perimeter(self):
        return self.side * 4
    