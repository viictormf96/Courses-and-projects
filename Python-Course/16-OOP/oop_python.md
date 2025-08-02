# Programación Orientada a Objetos en Python

La Programación Orientada a Objetos (POO u OOP en inglés) es un paradigma de programación que utiliza "objetos" y "clases" para organizar el código. Python es un lenguaje completamente orientado a objetos, lo que significa que casi todo en Python es un objeto.

---

## ✨ Conceptos Clave

### 1. **Clases y Objetos**

- **Clase**: Es un molde o plantilla que define atributos y comportamientos (métodos).
- **Objeto**: Es una instancia de una clase. Se crea a partir de una clase.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Ana", 30)
persona1.saludar()
```

### 2. **Atributos y Métodos**

- **Atributos**: Variables asociadas a un objeto (por ejemplo, `nombre`, `edad`).
- **Métodos**: Funciones dentro de una clase (por ejemplo, `saludar`).

### 3. **Encapsulamiento**

Restringe el acceso directo a los atributos de un objeto.

- Convención: `_atributo` (protegido), `__atributo` (privado)

```python
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado

    def mostrar_saldo(self):
        return self.__saldo
```

### 4. **Herencia**

Permite que una clase hija herede atributos y métodos de una clase padre.

```python
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
```

### 5. **Polimorfismo**

Permite usar el mismo método en diferentes clases con diferente comportamiento.

```python
class Gato:
    def hablar(self):
        print("Miau")

class Perro:
    def hablar(self):
        print("Guau")

animales = [Gato(), Perro()]
for animal in animales:
    animal.hablar()
```

### 6. **Abstracción**

Oculta los detalles internos y muestra solo lo esencial.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass
```

---

## 📊 Ventajas de la POO

- Código más organizado y reutilizable
- Escalabilidad y facilidad de mantenimiento
- Mayor seguridad y control

---

## 🎓 Recursos Recomendados

- Documentación oficial de Python: [https://docs.python.org/3/tutorial/classes.html](https://docs.python.org/3/tutorial/classes.html)
- Curso gratuito en Real Python: [https://realpython.com/python3-object-oriented-programming/](https://realpython.com/python3-object-oriented-programming/)
- Libros: "Automate the Boring Stuff with Python", "Python Crash Course"

---

## 📄 Buenas Prácticas

- Usa nombres claros y significativos para clases y métodos.
- Aplica principios SOLID si vas a hacer sistemas grandes.
- Comienza diseñando tus clases en papel si el proyecto es complejo.

---

¡La programación orientada a objetos es clave para dominar Python profesionalmente!

