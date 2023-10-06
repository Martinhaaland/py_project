'''Write a Python program to create a class representing a binary search tree.
 Include methods for inserting and searching for elements in the binary tree.'''
 #declare a class
 #insert
class Binary_search:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Binary_search(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Binary_search(value)
            else:
                self.right.insert(value)
    def search(self, value):
        if value == self.value:
           print(value)
        elif value < self.value:
            if self.left == value:
                print(value)
            elif self.left is None:
                pass
            else:
                self.left.search(value)
        else:
            if self.right == value:
                print(value)
            elif self.right is None:
                pass
            else:
                self.right.search(value)   

tmp = Binary_search(5)
tmp.insert(6)
tmp.insert(1)
tmp.insert(2)
tmp.insert(3)
tmp.insert(10)
tmp.insert(9)
tmp.insert(8)
tmp.search(99)