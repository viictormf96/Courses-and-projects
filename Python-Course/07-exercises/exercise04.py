"""
EJERCICIO 04.
    - Pedir dos numeros al usuario y hacer todas las operaciones basicas de una calculadora
    y mostrarlo por pantalla
"""

#Pedimos los numeros al Usuario
numero1 = int(input("Ingresa el primero numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

print("----------------CALCULADORA----------------")

print(f"{numero1} + {numero2} : {numero1 + numero2}")
print(f"{numero1} - {numero2} : {numero1 - numero2}")
print(f"{numero1} * {numero2} : {numero1 * numero2}")
print(f"{numero1} / {numero2} : {numero1 / numero2}")