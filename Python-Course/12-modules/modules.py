"""
Un MODULO son funcionalidades ya hechas para reutilizar.
Un módulo en Python es un archivo que contiene código reutilizable: funciones, variables, clases o incluso código ejecutable. 
Su propósito es organizar el código y facilitar la reutilización en diferentes programas.
"""

#Importamos el modulo(BUENA PRACTICA)
import mymodule

#De esta forma solo llamamos la funcion holaMundo y no hace falta introducir mymodule.
from mymodule import holaMundo

#Si queremos llamar a las funciones de mymodule sin introducir el mymodule. (NO RECOMENDABLE)
from mymodule import *

#Usamos la funcion que esta en el modulo importado
print(mymodule.holaMundo("Victor Muntane"))
print(calculadora(3, 5, True))

#MODULO FECHAS
import datetime

print(datetime.date.today())

#Obtenemos el dato completo respecto a la fecha y hora
fecha_completa = datetime.datetime.now()
print(fecha_completa)

#sacamos solo el año
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

#Formateamos la fecha a nuestro gusto
fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print(f"Mi fecha personalizada es: {fecha_personalizada}")

#MODULO MATEMATICAS
import math

#Operaciones con math
print(f"Raiz cuadrada de 10: {math.sqrt(10)}")
print(f"Numero PI: {math.pi}")
print(f"Redondear al alza: {math.ceil(6.5647328)}")
print(f"Redondear a la baja: {math.floor(6.5647328)}")

#MODULO RANDOM
import random

#Operaciones con random
print(f"Numero Aleatorio entre 15 y 67: {random.randint(15,67)}")