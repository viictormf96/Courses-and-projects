"""
Un paquete en Python es una carpeta que agrupa varios módulos (archivos .py) y subpaquetes relacionados entre sí, 
permitiendo organizar el código en estructuras más limpias y jerárquicas.

🔹 Definición:
Un paquete es una carpeta que contiene un archivo especial llamado __init__.py, lo que le indica a Python que debe tratar esa carpeta como un módulo agrupador.
"""

print("PROBANDO PAQUETES:")

#Importamos los modulos del paquete
from mypackage import test
from mypackage import tools

#Podemos importarlo tambien en la misma linea
from mypackage import test, tools

#Llamamos a las funciones que hay dentro del paquete
test.probando()
tools.nombreCompleto("Victor", "Muntane")
