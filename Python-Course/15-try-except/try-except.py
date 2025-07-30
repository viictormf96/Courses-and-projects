#CAPTURAR EXCEPCIONES y manejar errores en código
#susceptible a fallos/errores

#Creamos un programa que si no introduce nada por pantalla generara un error
#Para solventarlo usamos el try-except

try:
    nombre = input("¿Cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = f"El nombre es {nombre}"

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, mete bien el nombre")

#Podemos introducir que en caso que todo vaya bien imprima un mensaje
else:
    print("Todo ha funcionado correctamente")
#Captura cuando ha finalizado todo el bloque de try-except
finally:
    print("Fin de la iteración!!")

#APLICAMOS EL TRY-EXCEPT EN UN EJERCICIO ANTERIOR
#Si introducimos un numero que no esta en la lista nos devolvera un error igual
#que si introducimos un string.
print("\n############ BUSCAR NUMERO ############")

try:
    num_list = [3,65,35,85,23,43,56,43]
    numero = int(input("Introduce un numero: "))

    #comprobamos que el usuario introduce un numero
    comprobar = isinstance(numero, int)

    while not comprobar or numero <=0:
        numero = int(input("Introduce un numero: "))
    else:
        print(f"Has introducido el {comprobar}")
    search = num_list.index(numero)

    print(f"Se ha encontrado el numero {numero} en la posicion {num_list.index(numero)}, {num_list.count(numero)} veces")

except:
    print("El número no está en la lista, lo siento")

#MANEJAR MULTIPLES EXCEPCIONES
print("\n############ ELEVAR UN NUM AL CADRADO ############")

try:
    num = int(input("Numero para elevarlo al cuadrado: "))
    print(f"El cuadrado es: {num*num}")

#Manejamos que el usuario introduzca un numero entero
except TypeError:
    print("Introduce un numero entero")

#Manejamos que la cadena de texto que recojemos en la variable 
#num se convierta a un int
except ValueError:
    print("Debes convertir tus cadenas a enteros en el código!!")

#Nos muestra el tipo de error que es
except Exception as e:
    print(f"Ha ocurrido un error: {type(e).__name__}")


#EXCEPCIONES PERSONALIZADAS O LANZAR EXCEPCIONES
name = input("Introduce el nombre: ")
edad = int(input("Introduce la edad: "))

#Hacemos que si se cumplen los if se genere un valueerror
try:
    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido al Master en Python {name} !!")
except ValueError:
    print("Introduce los datos correctamente")
