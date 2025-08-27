#IMPORTAMOS EL MODULO MYSQL INSTALADO
import mysql.connector

#CONEXION
database = mysql.connector.connect(
    host = "127.0.0.1", 
    user = "root",
    passwd = "",
    database = "master_python"
)

#COMPROBAR CONEXION
print(database)

#CREAR CURSOR
cursor = database.cursor(buffered=True)

#CREAR TABLAS
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehicles(
    id int(10) auto_increment not null,
    brand varchar(40) not null,
    model varchar(40) not null,
    price float(10,2) not null,
    CONSTRAINT pk_vehicle PRIMARY KEY(id));
"""
)
database.commit()

#MOSTRAMOS LAS TABLAS
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

#INSERTAR DATOS A LA TABLA
#Insertamos datos uno a uno
"""
cursor.execute("INSERT INTO vehicles VALUES(null,'Opel','Astra', 18500);")
database.commit()
"""

#Insertamos datos de forma massiva
cars = [
    ("Seat", "Ibiza", 5000),
    ("Mercedes", "Class A", 23000),
    ("Audi", "Q3", 34000),
    ("Cupra", "Formentor", 52000)
]
"""
cursor.executemany("INSERT INTO vehicles VALUES (null, %s, %s, %s);", cars)
database.commit()
"""

#Mostrar vehiculos
cursor.execute("SELECT * FROM vehicles;")
result = cursor.fetchall()

print("----- CARS -----")
for car in result:
    print(car)

#Mostrar un vehiculo en concreto
cursor.execute("SELECT * FROM vehicles where price = 5000;")
print("\n----- CAR -----")
print(cursor.fetchall())

#Eliminar un valor de la tabla
cursor.execute("DELETE FROM vehicles WHERE price = 5000;")
database.commit()

cursor.execute("SELECT * FROM vehicles;")
result = cursor.fetchall()

print("----- CARS -----")
for car in result:
    print(car)

#Actualizar un valor de la tabla
cursor.execute("UPDATE vehicles SET model = 'Class B' WHERE brand = 'Mercedes';")
database.commit()
print("\n----- CAR MERCEDES -----")
cursor.execute("SELECT * FROM vehicles WHERE brand = 'Mercedes';")
print(cursor.fetchall())
database.close()