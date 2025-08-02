#PROGRAMACIÓN ORIENTADA A OBJETOS (OOP)
#CREANDO CLASES

#Definimos una clase (molde para crear mas objetos de ese tipo)

#GETTERS Y SETTERS
#Debemos usar estos metodos para añadir valores a los atributos del objeto o para mostrarlos.
#Por lo tanto si queremos mostrar un atributo como antes velocidad deberiamos usar getVelocidad.
class Coche:
    #Atributos o propiedades del coche (variables)
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

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
    
    #SETTERS
    def setColor(self, color):
        self.color = color
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def setMarca(self, marca):
        self.marca = marca
    
#Fin de la definición de la clase

#Crear objeto / Instancias la clase
coche = Coche()

print(coche)

#Podemos acceder a los atributos del coche
print(coche.marca, coche.color)

#Enseñamos la velocidad actual del coche
print(f"velocidad actual: {coche.getVelocidad()}")

#Llamamos al metodo para que acelere el coche
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

#Volvemos a mostrar la velocidad despues de acelerar
print(f"velocidad nueva: {coche.getVelocidad()}")

#Si llamamos a frenar la velocidad bajará
coche.frenar()
print(f"velocidad despues frenar: {coche.getVelocidad()}")

#CAMBIAMOS LOS ATRIBUTOS USANDO SETTERS
print("\n##### COCHE #####")
print(f"Color: {coche.getColor()}")
print(f"Marca: {coche.getMarca()}")
print(f"Modelo: {coche.getModelo()}")

#usamos set para cambiar atributos
coche.setColor("Verde")
coche.setModelo("F8")

#Volvemos a imporimir los valores
print("\n##### COCHE CAMBIADO #####")
print(f"Color: {coche.getColor()}")
print(f"Marca: {coche.getMarca()}")
print(f"Modelo: {coche.getModelo()}")

#Creamos mas objetos
coche2 = Coche()
coche2.setColor("Azul")
coche2.setModelo("Aventador")
coche2.setMarca("Lambo")

print("\n##### COCHE 2 #####")
print(f"Color: {coche2.getColor()}")
print(f"Marca: {coche2.getMarca()}")
print(f"Modelo: {coche2.getModelo()}")
