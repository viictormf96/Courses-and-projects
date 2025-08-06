from employee import Employee

class It(Employee):
    
    #CONSTRUCTOR
    def __init__(self, name, age, salary, language):
        super().__init__(name, age, salary)
        self.language = language
    
    #GETTERS
    def getLenguage(self):
        return self.language

    #SETTERS
    def setLenguage(self, language):
        self.language = language

    #METHODS
    def programming(self):
        return f"{self.name} is programming in {self.language} with a salary of {self.getSalary()}€ at {self.age} years old."