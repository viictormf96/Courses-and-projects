# Bucle while
# Un bucle while ejecuta un bloque de código mientras una condición sea verdadera

contador = 0

while contador <=100:
    print(contador)
    contador += 1  # Incrementa el contador en 1

print("-------------------------------")

contador = 1
muestrame = str(0)

while contador <=100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1  # Incrementa el contador en 1
print(muestrame)

#EJEMPLO TABLA DE MULTIPLICAR
print("\n-------------------------------")

numero = int(input("Introduce un numero: "))
i=0

while i <=10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1  # Incrementa i en 1
else:
    print("Esta es la tabla de multiplicar del", numero)

