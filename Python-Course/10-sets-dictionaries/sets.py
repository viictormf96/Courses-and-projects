#Un SET es un tipo de dato, para tener una coleccion de valores, que no tiene indice ni orden
#Se suelen usar cuando necesitas evitar duplicados, haces una busqueda para saber si existe el elemento
#o haces operaciones de conjunto

#DEFINIMOS UN SET
personas = {
    "Victor",
    "Manolo",
    "Francisco"
}

#Agregar elementos dentro del SET
personas.add("Paco")
print(personas)

#Eliminar elementos dentro del SET
personas.remove("Francisco")
print(personas)