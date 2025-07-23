#Un condicional es una estructura de control que permite ejecutar   
#un bloque de código solo si se cumple una condición específica.

"""
Operadores de comparación:
==  Igual
!=  Diferente
>   Mayor que
<   Menor que
>=  Mayor o igual que
<=  Menor o igual que
Operadores lógicos:
and  Y lógico
or   O lógico
not  Negación lógica
"""

#Ejemplo 1
print("############## EJEMPLO 1 ##############")

color = "rojo"
#color= input("Ingrese un color: ")

if color == "rojo":
    print("El color es rojo")
else:
    print("Color incorrecto")

#Ejemplo 2
print("\n############## EJEMPLO 2 ##############")

year = 2020
year = int(input("Ingrese un año: "))
 
if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Estamos en 2020 o antes")