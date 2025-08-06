
class Person:
    #CONSTRUCTOR
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #GETTERS
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    #SETTERS
    def setName(self, name):
        self.name = name
    
    def setAge(self, age):
        self.age = age
    
    #METHODS
    def welcome(self):
        return f"Hello, my name is {self.name} and I have {self.age} years."
