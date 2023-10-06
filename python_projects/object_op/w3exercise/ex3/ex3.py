#Write a Python program to create a calculator class.
#Include methods for basic arithmetic operations.
class Calculator:
    def __init__(self, first_item, second_item):
        self.first_item = first_item
        self.second_item = second_item
    def add(self):
        return (self.first_item) + (self.second_item)
    def multiply(self):
        return (self.first_item) * (self.second_item)
    def subtract(self):
        return self.first_item - self.second_item
    def divide(self):
        return self.first_item / self.second_item
boo = Calculator(2, 1)
print(boo.divide())

