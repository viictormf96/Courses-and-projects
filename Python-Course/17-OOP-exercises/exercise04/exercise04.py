"""
4. Herencia con Empleado e Informatico (Nivel Intermedio-Avanzado)
🧩 Objetivo:
Aplicar herencia

Usar super()

Añadir nuevos atributos/métodos

📋 Enunciado:
Crea una clase Empleado con los atributos nombre, edad y salario.
Crea una subclase Informatico que herede de Empleado y tenga un atributo extra: lenguaje.
Agrega un método programar() en Informatico.
"""
from it import It

dev1 = It("Victor Muntane", 28, 1800, "Python")
dev2 = It("Frank Cuesta", 35, 3000, "JavaScript")

print(dev1.programming())

print(dev2.programming())