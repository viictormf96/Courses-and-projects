"""
EJERCICIO 3
Programa que compruebe si una variable está vacia y si lo está, 
rellenarla con texto en minusculas y mostrarlo en mayusculas.
"""
#Creamos la variable

varVacia = ""

#Comprobamos que la cariable esta vacia quitandole los espacios
if(len(varVacia.strip()) <= 0):
    texto = input("La Variable está vacía añade algo de texto: ")
    while len(texto.strip()) <= 0 :
        texto = input("Escribe texto: ")
    print(f"El texto en mayusculas es: {texto.upper()}")
else:
    print("La Variable tiene texto")

