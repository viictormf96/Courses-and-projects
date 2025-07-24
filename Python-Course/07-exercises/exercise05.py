"""
EJERCICIO 05.
    Hacer un programa que muestre todos los numeros ente dos numeros
    que diga el usuario
"""

#Pedimos los numeros al usuario
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

#Recorremos los numeros con un while
if(num1 < num2):
    for i in range(num1,(num2+1)) :
        print(i)
else:
    print("El numero 1 debe ser menor al numero 2")
    