#Tipos de datos en Python
nada = None
cadena = "Hola, Python"
entero = 42
decimal = 3.14
booleano = False
lista = [1, 2, 3, 4, 5]
listaString = [44, "dos", 45, "tres"]
# Una tupla es una lista de cambios que no se pueden modificar
tupla = (1, 2, 3, 4, 5)
# Es como un docmuento JSON que tiene clave y valor
diccionario = {
    "nombre": "Victor", 
    "apellido": "Muntane",
    "curso": "Master en Python"
}

rango = range(9)


# Imprimir variable
print(rango)

# Mostrar el tipo de dato
print(type(rango))

#Convertir de un tipo de dato a otro ya que solo
#se pueden sumar cadenas de texto con cadenas de texto
texto = "Hola, soy un texto"
numero = 776
"""
Error!
print(texto + " " + numero)
"""
numero = str(numero)  # Convertir entero a cadena de texto
numero = int(numero)  # Convertir cadena de texto a entero
numero = float(numero)  # Convertir entero a float

print(type(numero))