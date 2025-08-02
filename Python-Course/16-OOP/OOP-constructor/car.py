
class Car:
    
    soy_publico = "hola, soy un atributo publico"
    __soy_privado = "Hola, soy un atributo privado"
    
    #CONSTRUCTOR (Es un metodo especial dentro de una clase para darle un valor a los atributos del objeto al crearlo)
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
    

    #Metodos: Acciones que hace el objeto
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    #GETTERS
    def getVelocidad(self):
        return self.velocidad
    
    def getColor(self):
        return self.color
    
    def getModelo(self):
        return self.modelo
    
    def getMarca(self):
        return self.marca
    
    def getCaballaje(self):
        return self.caballaje
    
    def getPlazas(self):
        return self.plazas
    
    def getInfo(self):
        info = "\n----- Información del coche -----"
        info += f"\n Color: {self.getColor()}"
        info += f"\n Marca: {self.getMarca()}"
        info += f"\n Modelo: {self.getModelo()}"
        info += f"\n Velocidad: {self.getVelocidad()}"
        info += f"\n Caballaje: {self.getCaballaje()}"
        info += f"\n Plazas: {self.getPlazas()}"
        return info
    
    def getPrivado(self):
        return self.__soy_privado
    
    #SETTERS
    def setColor(self, color):
        self.color = color
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def setMarca(self, marca):
        self.marca = marca
    
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad
    
    def setPlazas(self, plazas):
        self.plazas = plazas

    def setCaballaje(self, caballaje):
        self.caballaje = caballaje
    