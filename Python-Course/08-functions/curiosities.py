#1. Se recomienda tener las funciones declaradas en la parte de arriba del fichero

def mi_funcion():
    print("Hola que tal")

def mi_segunda_funcion():
    print("Hola que tal 2")

nombre = "Victor"
apellido = "Muntane"

print("Hola mundo")
print(f"Bienvenido {nombre}")

mi_funcion()
mi_segunda_funcion()

#2. Se recomienda siempre imprimir datos fuera de las funciones no dentro
#por lo tanto devolver el dato y impirmirlo fuera

def mi_funcion():
    return "Hola que tal"

def mi_segunda_funcion():
    return "Hola que tal 2"

print(mi_funcion())
print(mi_segunda_funcion())

#3. Cuando ejecutamos una funcion pueden estar antes o despues del codigo
#pero deben de estar definidas antes

#4. Lo recomendable es pasar datos a las funciones como parametros.

