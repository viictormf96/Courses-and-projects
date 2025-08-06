"""
 1. Clase Persona (Nivel Básico)
🧩 Objetivo:
Crear una clase simple

Usar atributos y métodos

📋 Enunciado:
Crea una clase Persona que tenga como atributos nombre y edad. Añade un método presentarse() que imprima:

"Hola, me llamo NOMBRE y tengo EDAD años".

🧪 Extra (opcional):
Crea varias instancias y llama al método presentarse().
"""

from person import Person

#CREATE NEW PERSONS
person1 = Person("Victor", 28)
person2 = Person("Mar", 27)

#CALL METHOD
print(person1.welcome())
print(person2.welcome())