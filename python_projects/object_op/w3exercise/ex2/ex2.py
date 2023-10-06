#Write a Python program to create a person class.
# Include attributes like name, country and date of birth. 
#Implement a method to determine the person's age.'''
class Person:
    def __init__(self, name, country, birth):
        self.name = name
        self.country = country
        self.birth = birth
    def __str__(self):
        return (self.name + ' is ' + str(2023 - int(self.birth)) + ' years old')
    
Avazbek = Person('Avazbek', 'Turkiston', '2003')
print(Avazbek)