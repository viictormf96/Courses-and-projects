"""
EJERCICIO 02.
    - Crear un script que muestre por pantalla los numeros pares del 1 al 120.
"""

#Opcion 1
for i in range(1,121):
    if i % 2 == 0:
        print(i)

#Opcion 2
for i in range(2,121, 2):
    print(i)
