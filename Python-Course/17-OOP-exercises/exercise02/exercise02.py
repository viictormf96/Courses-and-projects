"""
2. Clase Coche con métodos (Nivel Básico-Intermedio)
🧩 Objetivo:
Crear una clase con atributos y métodos de comportamiento

📋 Enunciado:
Crea una clase Coche con los atributos marca, modelo y velocidad.
Agrega métodos acelerar() y frenar() que modifiquen la velocidad.
Agrega un método estado() que muestre los datos actuales del coche.

🧪 Extra:
Haz que la velocidad no pueda bajar de 0.

"""
#Import Class Car
from car import Car

#Create new Car
car1 = Car("Tesla", "Model 3", 0)

#Using the Methods

for i in range(5):
    print(car1.accelerate())

print(car1.brake())
print(car1)
