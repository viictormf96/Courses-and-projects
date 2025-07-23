"""
Una variable es un contenedor de información que dentro guardará
un dato, se pueden crear muchas variables y que cada una tenga un 
dato distinto.
"""

# Crear variables y asignarles un valor
texto = "Máster en Python"
texto2 = "con Víctor Muntané"
numero = 45
decimal = 3.14

# Mostrar valor delas variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("------------------------------")

# Substituir el valor de una variable / reasignar valores
numero = 77
decimal = 6.7

print(numero)
print(decimal)

print("------------------------------")

# Concatenar variables: Unir variables en 1
nombre = "Victor"
apellido = "Muntané"
web = "victormuntane.com"

print(nombre + " " + apellido + " - " + web)

# Usando f-strings para formatear
print(f"{nombre} {apellido} - {web}")

# Usando el método format para formatear
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellido, web))

