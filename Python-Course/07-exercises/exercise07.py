"""
EJERCICIO 07.
    Mostrar los numeros impares entre dos numeros que decida el usuario
"""

#Pedimos los numeros al usuario
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

if num1 < num2:
    for cont in range(num1,(num2+1)):
        if cont % 2 == 1:
            print(cont)
else :
    print("El numero 1 debe ser mayor al 2")