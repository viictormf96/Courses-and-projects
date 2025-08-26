#SQLITE viene instalado por defecto con python

#Importamos el modulo de conexion de BD
import sqlite3
import os

# Ruta absoluta al directorio del script actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "test.db")

#CONEXIÓN
connection = sqlite3.connect(db_path)

#CREAR CURSOR
cursor = connection.cursor()

#CREAR TABLA
cursor.execute("""CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255),
    description TEXT,
    price int(255));
""")

#INSERTAR DATO
"""
cursor.execute("INSERT INTO products VALUES (null, "First product", "Product description", 550);")

#GUARDAR CAMBIOS
connection.commit()
"""


#BORRAR REGISTROS DE LA TABLA
cursor.execute("DELETE FROM products;")


#INSERTAR MUCHOR REGISTROS DE GOLPE
many_products = [
    ("PC", "Good PC", 700),
    ("Phone", "Good Phone", 145),
    ("Base plate", "Good Base plate", 80),
    ("Tablet", "Good Tablet", 500)
]

cursor.executemany("INSERT INTO products VALUES (null, ?, ?, ?);", many_products)
connection.commit()

#ACTUALIZAR DATOS
cursor.execute("UPDATE products SET price = 678 WHERE price = 80;")

#LISTAR LOS DATOS
cursor.execute("SELECT * FROM products;")
products = cursor.fetchall()

for product in products:
    print(f"ID: {product[0]}")
    print(f"Name: {product[1]}")
    print(f"Description: {product[2]}")
    print(f"Price: {product[3]}\n")

#PRIMER PRODUCTO DE LA TABLA
cursor.execute("SELECT title FROM products;")
first_product = cursor.fetchone()
print(first_product)

#CERRAR CONEXIÓN
connection.close()