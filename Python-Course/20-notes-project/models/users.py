class Users:

    #CONSTRUCTOR
    def __init__(self, id, name, surname, email, password):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.__password = password
    
    #GETTERS
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getSurname(self):
        return self.surname

    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.__password


    #SETTERS
    def setId(self, id):
        self.id = id
    
    def setName(self, name):
        self.name = name
    
    def setSurname(self, surname):
        self.surname = surname

    def setEmail(self, email):
        self.email = email
    
    def setPassword(self, password):
        self.__password = password
    
    def __str__(self):
        txt = f"\nId: {self.getId()}"
        txt += f"\nName: {self.getName()}"
        txt += f"\nSurname: {self.getSurname()}"  
        txt += f"\nEmail: {self.getEmail()}"  
        txt += f"\nPassword: {self.getPassword()}"  
        return txt
    
    def to_tuple(self):
        return (self.getId(), self.getName(), self.getSurname(), self.getEmail(), self.getPassword())