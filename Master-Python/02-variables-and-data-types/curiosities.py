"""
No se pueden usar variables que empiecen por un número
o palabrasreservadas como variables
"""

# Si queremos poner comillas en un texto podemos usar \"texto\ o usar comillas simples '' "
mi_texto = "'Master'"
mi_texto2 = "en \"Python\""

texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)

#Salto de línea \n
texto_unido = mi_texto + "\n " + mi_texto2
print(texto_unido)

#Tabulación \t
texto_unido = mi_texto + "\t " + mi_texto2
print(texto_unido)

#Elimina lo anterior a \r
texto_unido = mi_texto + "\r " + mi_texto2
print(texto_unido)