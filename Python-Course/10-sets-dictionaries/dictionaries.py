"""
DICCIONARIOS
Es un tipo de dato que almacena un conjunto de datos en formato Clave > Valor
Es parecido a un array asociativo o un objeto JSON.
"""

#Declaramos un diccionario
persona = {
    "Nombre" : "Victor",
    "Apellidos" : "Muntane",
    "Web" : "victormuntane.es"
}
print(type(persona))
print(persona)

#Accedemos a un indice en concreto
print(persona["Web"])

#LISTA CON DICCIONARIOS

contactos = [
    {
        "Nombre" : "Antonio",
        "Email" : "antonio@antonio.com"
    },
    {
        "Nombre" : "Luis",
        "Email" : "luis@luis.com"
    },
    {
        "Nombre" : "Luis",
        "Email" : "luis@luis.com"
    },
    {
        "Nombre" : "Pedro",
        "Email" : "pedro@pedro.com"
    }
]

#Podemos modificar el valor de un indice
contactos[0]["Nombre"] = "Victor"
contactos[0]["Email"] = "victor@victor.com"
print(f"{contactos[0]["Nombre"]} - {contactos[0]["Email"]}")

print("\n############ LISTADO CONTACTOS ############")

for contacto in contactos:
    print(f"Nombre: {contacto["Nombre"]}")
    print(f"Email: {contacto["Email"]}")
    print("-----------------------------")