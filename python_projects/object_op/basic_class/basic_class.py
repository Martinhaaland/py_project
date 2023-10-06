class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def about(self):
        return f'{self.name} is {self.age} years old'
    
class JackRussellTerrier(Dog):
    def speak(self, voice='auf'):
        return f'{self.name} says {voice}'

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass
mydog = JackRussellTerrier('Yolbars', 14)
print(mydog.speak('WTH?'))
