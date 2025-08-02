#La herencia es la posibilidad de compartir atributos y métodos entre clases y que diferentes clases hereden de otras

#Creamos la clase padre PERSONA
class Persona:
    """
    nombre
    apellidos
    altura
    edad
    """ 

    #CONSTRUCTOR
    def __init__(self, nombre, apellidos, edad, altura):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.altura = altura

    #GETTERS
    def getNombre(self):
        return self.nombre
    
    def getApelllidos(self):
        return self.apellidos
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad
    
    #SETTERS
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura
    
    def setEdad(self, edad):
        self.edad = edad
    
    #ACCIONES
    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Esto caminando"
    
    def dormir(self):
        return "Estoy durmiendo"

#Creamos la clase hijo INFORMATICO que heredará de PERSONA
class Informatico(Persona):
    """
    Lenguajes Programacion
    Experiencia Laboral
    """
    #CONSTRUCTOR
    def __init__(self, nombre, apellidos, edad, altura):
        #Traemos al constructor la clase padre
        super().__init__(nombre, apellidos, edad, altura)
        self.lenguajes = "HTML, CSS, JavaScript, PHP"
        self.experiencia = 5
    
    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def repararPC(self):
        return "He reparado tu ordenador"

#Heredamos un tecnico de informatico
class TecnicoRedes(Informatico):
    
    #CONSTRUCTOR
    def __init__(self,nombre, apellidos, edad, altura):
        super().__init__(nombre, apellidos, edad, altura)
        self.auditarRedes = "Experto"
        self.experienciaRedes = 15
    
    def auditoria(self):
        return "Estoy auditando una red"