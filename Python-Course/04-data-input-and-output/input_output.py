#Entrada
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

#Salida
print(f"Me alegro de conocerte, bienvenido {nombre}, veo que tienes {edad} años.")

#Edad sera un string, por lo que debemos convertirlo a int si queremos hacer operaciones con ella
print(f"Me alegro de conocerte, bienvenido {nombre}, veo que tienes {int(edad) + 3} años.")