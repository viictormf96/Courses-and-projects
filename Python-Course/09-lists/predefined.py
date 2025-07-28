#METODOS Y FUNCIONES PREDEFINIDOS 
cantantes = ["2pac", "Drake", "Bad Bunny", "Julio Iglesias"]
numeros = [1,2,5,8,3,4]

#ORDENAR UNA LISTA
print(numeros) #Los numeros estan desordenados
numeros.sort() #Ordena la lista numeros
print(numeros)

#AÑADIR ELEMENTOS
cantantes.append("Mike Towers") #Añade elemento al final de la lista
cantantes.insert(2,"Taylos Swift") #Añade el elemento en una posicion concreta
print(cantantes)

#ELIMINAR ELEMENTOS
cantantes.pop(4) #Eliminamos el elemento en la posicion numero 5
cantantes.remove("Mike Towers") #Eliminamos el elemento por el nombre
print(cantantes)

#DAR LA VUELA A UNA LISTA
print(numeros)
numeros.reverse()
print(numeros)

#BUSCAR DENTRO DE LA LISTA
print("Drake" in cantantes) #Devuelve un booleano

#CONTAR EL NUMERO DE ELEMENTOS
print(len(cantantes))

#CUANTAS VECES APARECE UN ELEMENTO
numeros.append(8)
print(numeros.count(8))

#CONSEGUIR UN INDICE
print(cantantes.index("Drake")) #Devuelve el indice donde esta el cantante

#UNIR LISTAS
cantantes.extend(numeros) #Añade la lista numeros al final de la de cantantes
print(cantantes)
