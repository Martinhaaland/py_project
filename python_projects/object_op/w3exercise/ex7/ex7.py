'''7. Write a Python program to create a class representing a linked list data structure.
 Include methods for displaying linked list data, inserting and deleting nodes. '''
class Node:
    def __init__(self, value):
        self.value = value
        self.tail = None
class Linked_list:
    def __init__(self):
        self.root = None

random = Linked_list()
random.root = Node(1)
two = Node(2)
three = Node(3)
random.root.tail = two
two.tail = three