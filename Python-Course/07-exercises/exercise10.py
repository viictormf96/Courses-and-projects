"""
EJERCICIO 10.
    Pedir al usuario la nota de 5 alumnos y mostrar los usuarios que han
    aprobado y suspendido
"""

count = 1
approved = 0
suspended = 0

num_students = int(input("¿Cuantos alumnos tienes?: "))

while count <= num_students:
    
    grade = int(input(f"¿Que nota quieres ponerle al alumno {count}?: "))

    if grade <= 5 and grade > 0:
        approved += 1
        count += 1
    elif grade >= 5 and grade < 10:
        suspended += 1
        count += 1
    else:
        print("\nDebes introducir un numero del 0 al 10!.\n")

print("######### RESULTADOS #########")
print(f"Han aprovado {approved} alumnos")
print(f"Han suspendido {suspended} alumnos")