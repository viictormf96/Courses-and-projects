#Las funciones predefinidas son funciones que ya vienen incluidas
#como por ejemplo print

nombre = "Victor Muntane"

#Funciones generales
print(nombre)

#Detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar == True:
    print("Esa variable es un string")
else:
    print("no es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

#Limpiar espacios
frase = "     mi contenido     "
print(frase)
print(frase.strip())

#Eliminar variables
year = 2023
print(year)
del year
#print(year)

#Comprobar variable vacía o contar los caracteres
texto = "  ff  "

if len(texto) <= 0:
    print("La variable está vacía")
else:
    print("La variable tiene contenido: ", len(texto))

#Encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida"))

#Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

#Mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())