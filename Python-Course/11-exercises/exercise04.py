"""
EJERCICIO 4
Crear un script que tenga 4 variables:
 - Lista
 - String
 - Entero
 - Booleano
Que imprima un mensaje segun el tipo de dato de cada variable usando funciones
"""

#Creamos la funcion
def whichType(var, tipo):
    #Comprobamos si es del tipo de variable que hemos pasado
    test = isinstance(var, tipo)

    #Comprobamos y imprimimos
    if test:
        msg = f"La variable es de tipo: {type(var).__name__}" 
    else:
        msg = f"La variable no es del tipo {tipo.__name__}, es de tipo {type(var).__name__}"
    return msg  

#Declaramos las variables
var1 = "fmdskfk"
var2 = ["Victor", "Pedro"]
var3 = 123
var4 = True

#Comprobamos si los tipos concuerdan
print(whichType(var1, int))
print(whichType(var2, list))
print(whichType(var3, bool))
print(whichType(var4, bool))