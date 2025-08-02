#IMPORTAMOS LA CLASE COCHE
from car import Car



#Creamos el primer coche
carro = Car("Amarillo", "Renault", "Clio", 150, 200, 4)
carro1 = Car("Verde", "Seat", "Panda", 240, 200, 4)
carro2= Car("Azul", "Citroen", "Xara", 100, 180, 4)
carro3 = Car("Rojo", "Mercedes", "Clase A", 350, 400, 4)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

#Detectar tipado
if type(carro3) == Car:
    print("Es un objeto correcto")
else:
    print("No es un objeto")

#VISIBILIDAD
#Hace que las variables de la clase se puedan ver desde fuera de la clase si son publicas
#si son privadas solo podremos verlas desde la misma clase

#Intentamos acceder a soy privado y podemos.
print(carro.soy_publico)

#Pero si queremos acceder a soy privado no nos deja. Para acceder necesitamos un metodo getter o setter
print(carro.getPrivado())