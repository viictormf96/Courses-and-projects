class Employee:

    #CONSTRUCTOR
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self._salary = salary
    
    #GETTERS
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getSalary(self):
        return self._salary
    
    #SETTERS
    def setName(self, name):
        self.name = name
    
    def setAge(self, age):
        self.age = age

    def setSalary(self, salary):
        self._salary = salary
    