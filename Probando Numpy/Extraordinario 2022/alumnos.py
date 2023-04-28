

class alumnos:

    def __init__(self,dni,apellido,nombre,carrera,año):
        self.__dni = dni 
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__año = año

    def __str__(self):
        return "dni {} apellido  {}  nombre  {} carrera  {} año  {}".format(self.__dni,self.__apellido,self.__nombre,self.__carrera,self.__año)

    def getAño(self):
        return self.__año

    def getDni(self):
        return self.__dni

    def getNomyApe(self):
        return "{} {}".format(self.__apellido,self.__nombre)

    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido

    def __lt__(self,other):
        cadena = ""
        val = False
        if type(self) == type(other):
            
            cadena1 = str(self.getAño()) + str(self.getNombre()) + str(self.getApellido()) 
            cadena2 = str(other.getAño()) + str(other.getNombre()) + str(other.getApellido())
            
            if cadena1 < cadena2:
                val = True
        return val

    