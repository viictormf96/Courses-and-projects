"""
Variables locales: Se definen dentro de la función y no se pueden usar 
fuera de ella, solo están disponibles dentro a no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una funcion y estan 
disponibles dentro y fuera de ellas
"""

#VARIABLES GLOBALES
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"
print(frase)

def holaMundo():
    #Si comentamos este codigo se mostrara la frase que hemos declarado fuera como global
    frase = "Hola mundo !"
    print("Dentro de la funcion")
    print(frase)

    year =2021
    print(year)

    #Queremos que esta varuiable se convierta en global
    global webside
    webside = "victormuntane.com"
    print("Dentro de la funcion: ", webside)
    

holaMundo()
print("Fuera de la funcion: ", webside)
