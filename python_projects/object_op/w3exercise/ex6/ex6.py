# Write a Python program to create a class representing a stack data structure. 
# Include methods for pushing and popping elements.
class Stack_data_struct():
    def __init__(self):
        self.list = []
    def push(self, value):
        self.list.append(value)
    def removing(self):
        if len(self.list) > 0:
            self.list.pop()
        else:
            print('the list is empty!!! ')
random = Stack_data_struct()
random.push(4)
random.push(6)
random.push(0)
random.push(9)
random.push(7)
random.removing()
print(random.list)
        