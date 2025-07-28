"""
EJERCICIO 1
Hacer un programa que tenga una lista de 8 nuemros enteros y haga lo siguiente:
    - Recorrer la lista y mostrarla
    - Hacer una funcion que recorra listas de numeros y devuelva un string
    - Ordenadla y mostrarla
    - Mostrar su longitud
    - Buscar algun elemento (que el usuario pida por teclado)
"""

#CREAMOS LA LISTA
num_list = [3,65,35,85,23,43,56,43]
print(num_list)

print("\n############ LISTADO NUMEROS ############")
#CREAMOS LA FUNCION QUE RECORRE LA LISTA Y DEVUELVE UN STRING
def getLista(nums):
    showList = ""
    for list in nums:
        showList += f"- {list}\n"

    return showList

print(getLista(num_list))

#ORDENAMOS LOS NUMEROS Y LOS MOSTRAMOS
print("\n############ LISTADO ORDENADO ############")
num_list.sort()
print(getLista(num_list))

#MOSTRAMOS LA LONGITUD DE LA LISTA
print("\n############ LONGITUD DE LISTA ############")
print(len(num_list))

#BUSCAR ELEMENTO QUE EL USUARIO PIDA
print("\n############ BUSCAR NUMERO ############")

numero = int(input("Introduce un numero: "))

#comprobamos que el usuario introduce un numero
comprobar = isinstance(numero, int)

while not comprobar or numero <=0:
    numero = int(input("Introduce un numero: "))

if numero in num_list :
    print(f"Se ha encontrado el numero {numero} en la posicion {num_list.index(numero)}, {num_list.count(numero)} veces")
else :
    print("No existe el elemento en la lista")