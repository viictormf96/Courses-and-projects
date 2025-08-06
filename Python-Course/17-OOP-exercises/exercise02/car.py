class Car:
    #CONSTRUCTOR
    def __init__(self, brand, model, speed):
        if not isinstance(brand, str) or not isinstance(model, str):
            raise TypeError("Brand and model must be strings")
        if not isinstance(speed, int):
            raise TypeError("Speed must be an integer")
        
        self.brand = brand
        self.model = model
        self.speed = speed
    
    #GETTERS
    def getBrand(self):
        return self.brand
    
    def getModel(self):
        return self.model
    
    def getSpeed(self):
        return self.speed
    
    #SETTERS
    def setBrand(self, brand):
        self.brand = brand
    
    def setModel(self, model):
        self.model = model

    def setSpeed(self, speed):
        self.speed = speed
    
    #METHODS
    def accelerate(self):
        self.speed += 1
        return f"The speed is: {self.speed} Km/h"
    
    def brake(self):
        if self.speed < 1:
             return f"You're unable to break, your speed is 0 km/h"
        else:
            self.speed -= 1
            return f"The speed is: {self.speed} Km/h"
    
    def state(self):
        text = "\n-------- CAR --------"
        text += f"\nBrand: {self.brand}"
        text += f"\nModel: {self.model}"
        text += f"\nSpeed: {self.speed} Km/h"
        return text
    
    def __str__(self):
        return self.state()

