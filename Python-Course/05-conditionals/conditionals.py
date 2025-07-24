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
!    Negación lógica
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
#year = int(input("Ingrese un año: "))
 
if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Estamos en 2020 o antes")

#Ejemplo 3 IF ANIDADO
#Un condicional dentro de otro condicional
print("\n############## EJEMPLO 3 ##############")

nombre = "Victor Muntane"
ciudad = "Barcelona"
continente = "Oceania"
edad = 19
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if continente != "Europa":
        print(f"{nombre} no es de Europa")
    else:
        print(f"{nombre} es de Europa y de {ciudad}")
else:
    print(f"{nombre} no es mayor de edad")

#Ejemplo 4 ELIF
#Permite evaluar múltiples condiciones de forma secuencial
print("\n############## EJEMPLO 4 ##############")

dia = 3
#dia = int(input("Ingrese el num del día de la semana: "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("Número de día incorrecto")

#Ejemplo 5 MULTIPLES CONDICIONES
#Permite evaluar múltiples condiciones de forma secuencial
print("\n############## EJEMPLO 5 ##############")

edad_minima = 18
edad_maxima = 65
edad_oficial = 28

if edad_oficial >= 18 and edad_maxima <= 65:
    print("Esta en edad de trabajar !!")
else:
    print("No está en edad de trabajar !!")    

#Ejemplo 6 MULTIPLES CONDICIONES
#Permite evaluar múltiples condiciones de forma secuencial
print("\n############## EJEMPLO 6 ##############")

pais = "Alemania"

if pais == "España" or pais == "Mexico" or pais == "Colombia":
    print(f"{pais} es Hispano hablante")
else:
    print(f"{pais} no es Hispano hablante")

#Ejemplo 7 MULTIPLES CONDICIONES
#Permite evaluar múltiples condiciones de forma secuencial
print("\n############## EJEMPLO 7 ##############")

pais = "España"

if not (pais == "España" or pais == "Mexico" or pais == "Colombia"):
    print(f"{pais} no es Hispano hablante")
else:
    print(f"{pais} es Hispano hablante")

#Ejemplo 8 MULTIPLES CONDICIONES
#Permite evaluar múltiples condiciones de forma secuencial
print("\n############## EJEMPLO 8 ##############")

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} no es Hispano hablante")
else:
    print(f"{pais} es Hispano hablante")