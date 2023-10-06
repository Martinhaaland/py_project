# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
 
class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        number = (self.radius ** 2) * Circle.pi
        str(number)
        return f'The area of the given circle is {number}'
    def perimeter(self):
        number = 2 * self.radius * Circle.pi
        str(number)
        return f'The circumference of the given Circle is {number}'
example = Circle(5)
print(example.perimeter())