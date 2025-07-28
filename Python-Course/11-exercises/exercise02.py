"""
EJERCICIO 2
Escribir un programa que añada valores a una lista mientras que su longitud sea menor a 120 y luego mostrar la lista
Plus: Usar while y for
"""
import random

#Declaramos la lista
lista = list()

#Añadimos valores a la lista mientras la longitud es menor a 120
"""
while len(lista) < 120:
    lista.append(random.randint(1, 1000)) 
    #Mostramos la lista por pantalla
    print(f"{cont} - {list}\n")
"""

#Hacemos lo mismo pero con for
for cont in range(0,120):
    cont += 1
    lista.append(random.randint(1, 1000)) 
    #Mostramos la lista por pantalla
    print(f"{cont} - {lista[cont-1]}\n")
