"""
EJERCICIO 03.
    - Escribir un programa que muestre los cuadrados(numero multiplicado por si mismo)
    de los 60 primeros numeros naturales.
    - Resolverlo con for y while
"""

#Bucle For
print("---------- FOR --------------")

for numero in range (1,61):
    print(f"Cuadrado del {numero}: {numero*numero}")

#Bucle While¡
print("---------- WHILE --------------")

num = 0
while num <=60:
    print(f"Cuadrado del {num}: {num*num}")
    num += 1