import classes

#Creamos una persona
persona = classes.Persona("Victor","Muntane Fuentes",28,"183cm")

#Mostramos algunos valores de la clase
print(f"La persona es: {persona.getNombre()} {persona.getApelllidos()}")
print(persona.hablar())

print("\n-------------------------------------")

#Creamos un informatico y como vemos podemos acceder a los valores de persona
informatico = classes.Informatico("Carlos", "Martinez", 29, "172cm")

#mostramos los datos del informatico
print(f"El informatico es: {informatico.getNombre()} {informatico.getApelllidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())

print("\n-------------------------------------")

#Creamos un tecnico de redes
tecnico = classes.TecnicoRedes("Pedro", "Jimenez", 34, "160cm")
print(tecnico.auditoria(), tecnico.getLenguajes())