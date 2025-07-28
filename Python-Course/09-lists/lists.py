"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre.
Para acceder a esos valores podemos usar un indice númerico.

"""

pelicula = "Batman"

#Definir una lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"] #Mejor esta forma
cantantes = list(("2pac", "Drake", "Jennifer Lopez")) #Definimos una tupla dentro de una lista
years = list(range(2020,2050)) #Muestra todo el contenido del rango
variada = ["Victor", 30, 4.4, True, "Texto"] #Podemos combinar diferentes tipos de valores.

print(peliculas)
print(cantantes)
print(years)
print(variada)


#Indices

#Podemos modificar el contenido de un indice
peliculas[1] = "Gran Torino"
peliculas[2] = "El hobbit"

print(peliculas[1]) #Mostramos el indice 1 del array o lista
print(peliculas[-2]) #Muestra el indice desde atras
print(cantantes[1:2]) #Muestra el contenido del indice 1 al 2
print(peliculas[1:]) #Muestra todo el contenido a partir del indice num 1

#Añadir elementos a una lista
cantantes.append("Kase O")
cantantes.append("Natos y waor")
print(cantantes)

#Recorrer una lista
nueva_pelicula = ""

#Introducimos peliculas en la lista
"""
while nueva_pelicula != "parar" :
    nueva_pelicula = input("Introduce la nueva pelicula: ") #Pedimos las peliculas y las guardamos en una variable
    if nueva_pelicula != "parar" :
        peliculas.append(nueva_pelicula) #Añadimos la pelicula a la lista
"""

print("\n###### LISTADO PELICULAS ######")

for pelicula in peliculas: #Mientras que queden elementos en la lista peliculas se va iterando
    print(f"{peliculas.index(pelicula)}. {pelicula}") #Muestra el indice de las peliculas y la pelicula

#LISTAS MULTIDIMENSIONALES
#Son listas que dentro de la lista tiene otra lista

print("\n############ LISTADO PELICULAS ############")
#Creamos una lista dentro de otra lista
contactos = [
    [
        "Antonio",
        "antonio@antonio.com"
    ],
    [
        "Luis",
        "luis@luis.com"
    ],
    [
        "Salvador",
        "salvador@salvador.com"
    ]
]

print(contactos)

# Mostramos la lista dentro de la otra lista
print(contactos[1][1]) #Mostramos dentro de la lista 1 la posicion 1

print("\n############ LISTADO CONTACTOS ############")
#Recorremos todos los contactos
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print(f"Nombre: {elemento}")
        else:
            print(f"Email: {elemento}")
    print("\n")
        
