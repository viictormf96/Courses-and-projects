"""
EJERCICIO 09.
    Hacer un programa que pida numeros al usuario indefinidamente hasta meter
    el numero 111.
"""
num = 0
while num != 111:
    num = int(input("Dime un numero: "))
    if(num != 111):
        print(num)

print("PROGRAMA FINALIZADO!!")