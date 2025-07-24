#Una funcion es un bloque de codigo que se puede reutilizar
#Definicion de una funcion

#EJEMPLO 1
print("##### EJEMPLO 1 #####")

#Definimos la funcion
def muestraNombre():
    print("Victor Muntane")
    print("Paco Porro")
    print("pedro Zaragoza")
    print("Ruben Palma")
    print("\n")

#llamamos a la funcion
muestraNombre()

#EJEMPLO 2: Parametros
print("\n##### EJEMPLO 2 #####")

def saludar(nombre, edad):
    print(f"Hola, {nombre}!")  

    if edad >= 18:
        print("Eres mayor de edad")

#Llamada a la funcion
nombre = "Victor"
edad = 28
#nombre = input("Introduce tu nombre: ")
#edad = int(input("Introduce tu edad: "))
saludar(nombre, edad)

#EJEMPLO 3
print("\n##### EJEMPLO 3 #####")

def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    for count in range(11):
        print(f"{count} x {numero} = {numero * count}")
    
    print("\n")

tabla(5)

#EJEMPLO 3.1
print("\n##### EJEMPLO 3.1 #####")

for numero_tabla in range(1,11):
    tabla(numero_tabla)

#EJEMPLO 4
print("\n##### EJEMPLO 4 #####")

#Parametros opcionales
def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")
    
        
getEmpleado("Victor", 47975942)

#EJEMPLO 5
print("\n##### EJEMPLO 5 #####")

#Parametros opcionales y return o devolver datos

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame("Victor Muntane"))

#EJEMPLO 6
print("\n##### EJEMPLO 6 #####")

#Calculadora en un String
def calculadora(num1, num2, basicas = False):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    division = num1 / num2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(division)

    return cadena

print(calculadora(15,15))

#EJEMPLO 7
print("\n##### EJEMPLO 7 #####")

#Funciones dentro de funciones
def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Victor", "Muntane Fuentes"))

#EJEMPLO 8
print("\n##### EJEMPLO 8 #####")

#Funciones Lambda: Funciones anonimas que no tiene nombre y no hace falta definirla.
#Se usan para tareas simples y repetitivas

dime_el_year = lambda year: f"El año es {year}"

print(dime_el_year(2034))