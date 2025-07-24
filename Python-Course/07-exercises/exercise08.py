"""
EJERCICIO 08.
    Cuanto es el porcentaje que quiera el usuario de un numero que pida el usuario
"""

#Pedimos los datos al usuario
numero = int(input("Introduce un numero: "))
porcentaje = int(input("Introduce el porcentaje a deducir: "))

#Hacer la operacion y mostrarla por pantalla
resultado = (numero * porcentaje) / 100

print(f"\nEl {porcentaje}% de {numero} es: {resultado}")