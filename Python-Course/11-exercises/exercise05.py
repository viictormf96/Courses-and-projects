"""
EJERCICIO 5
Crear una lista con el contenido de esta tabla:
Videojuegos
ACCION  AVENTURA                DEPORTES
gta     assasins                fifa 21
cod     crash                   F1 2025
pubg    prince of persia        MOTO GP 23

Mostrar esta informacion ordenada
"""

#Creamos el diccionario

videojuegos = [
    {
        "Genero" : "ACCION",
        "Juegos" : ["GTA", "Call of Duty", "PUBG"]
    },
    {
        "Genero" : "AVENTURA",
        "Juegos" : ["Assasins Creed", "Crash Vandicut", "Prince of Persia"]
    },
    {
        "Genero" : "DEPORTES",
        "Juegos" : ["FIFA 21", "F1 2025", "MOTO GP 23"]
    },
    
]

#Lo iteramos para que muestre el contenido
for categoria in videojuegos:
    print(f"\n############ LISTADO {categoria["Genero"]} ############")
    for juego in categoria["Juegos"]:
        print(juego)
    



    