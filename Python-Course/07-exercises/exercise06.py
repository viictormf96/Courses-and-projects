"""
EJERCICIO 06.
    Mostrar todas las tablas de multiplicar del 1 al 10
"""
for num in range (1,11):
    print(f"\n################### TABLA {num} ###################\n")
    for i in range(0,11):
        print(f"{num} x {i} = {num * i}")