#Utilizamos el modulo OPEN que esta en el paquete IO para trabajar con archivos
from io import open

#I mportamos pathlib para obtener la ruta completa
import pathlib

#Nos devuelve la ruta completa
ruta = str(pathlib.Path().absolute()) + "/14-file-system/file_text.txt"
print(ruta)

#ABRIR ARCHIVO CON PERMISO DE ESCRITURA
archivo = open(ruta, "a+")

#ESCRIBIR DENTRO DE UN ARCHIVO (Si ejecutamos el script varias veces el texto se duplica)
archivo.write("********SOY UN TEXTO METIDO DESDE PYTHON*******\n")

#CERRAR ARCHIVO (Siempre hay que cerrar el archivo cuando hemos acabado)
archivo.close()

#ABRIR ARCHIVO DE NUEVO CON PERMISO DE LECTURA
archivo_lectura = open(ruta, "r")

#LEER CONTENIDO
#contenido = archivo_lectura.read()
#print(contenido)

#LEER CONTENIDO LINEA A LINEA Y GUARDARLO EN UNA LISTA
lista = archivo_lectura.readlines()

#Cerramos el archivo
archivo_lectura.close()

#recorremos la lista donde hemos guradado el contenido linea a linea
for elemento in lista:
    print(elemento)

#COPIAR ARCHIVO, RENOMBRARLO Y ELIMINARLOS CON SHUTIL
import shutil

#COPIAR ARCHIVO
ruta_original = str(pathlib.Path().absolute()) + "/14-file-system/file_text.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/14-file-system/copy_file.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + "/fichero_copiado77.txt" 
shutil.copyfile(ruta_original, ruta_nueva)

#MOVER O RENOMBRAR ARCHIVO
ruta_original = str(pathlib.Path().absolute()) + "/14-file-system/file_text.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/14-file-system/copyNEW_file.txt"

shutil.move(ruta_original, ruta_nueva)

#ELIMIAR ARCHIVOS
import os 

os.remove(ruta_nueva)
os.remove(str(pathlib.Path().absolute()) + "/14-file-system/copy_file.txt")

#COMPROBAR SI EXISTE UN FICHERO
import os.path

print(os.path.abspath("./"))

if os.path.isfile(os.path.abspath("./14-file-system/files.py")):
    print("El archivo existe")
else:
    print("El archivo no existe")