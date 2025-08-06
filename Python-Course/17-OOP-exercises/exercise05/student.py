class Student:

    #CONSTRUCTOR
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    #GETTERS
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

    def getGrades(self):
        return self.grades


    #SETTERS
    def setName(self, name):
        self.name = name
    
    def setAge(self, age):
        self.age = age

    def setGrades(self, grades):
        self.grades = grades

    