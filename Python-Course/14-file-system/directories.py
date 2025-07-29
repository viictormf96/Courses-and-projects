#IMPORTAMOS OS
import os

#CREAR CARPETA

if not os.path.isdir("./14-file-system/mi_carpeta"):
    os.mkdir("./14-file-system/mi_carpeta") #Crea la carpeta con mkdir
else:
    print("Ya existe la carpeta")

#COPIAR CARPETA
import shutil
ruta_original = "./14-file-system/mi_carpeta"
ruta_nueva = "./14-file-system/mi_carpeta_copiada"
 
if not os.path.isdir("./14-file-system/mi_carpeta_copiada"):
    shutil.copytree(ruta_original, ruta_nueva)
else:
     print("Ya existe la carpeta")

#ELIMINAR CARPETA
#os.rmdir("./14-file-system/mi_carpeta_copiada")

#MOSTRAR CONTENIDO DE LA CARPETA
print("Contenido de mi carpeta:")
contenido = os.listdir("./14-file-system/mi_carpeta")

for fichero in contenido:
    print(f"Fichero: {fichero}")