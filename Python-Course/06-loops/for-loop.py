#BUCLE FOR
# Iterar sobre una lista, Range, String, etc.

contador = 0
resultado = 0

for contador in range(0, 10):
    print(f"Voy por el {contador}")
    resultado += contador

print(f"El resultado es {resultado}")

#Ejemplo con tablas de miltiplicar
print("\n############## EJEMPLO ##############")

numero = int(input("Introduce un numero: "))

for numero_tabla in range(1, 11):
    print(f"{numero} x {numero_tabla} = {numero * numero_tabla}")
    """
    if numero_tabla == 5:
        break  # Rompe el bucle si llega a 5
    """
else:
    print("Esta es la tabla de multiplicar del", numero)
