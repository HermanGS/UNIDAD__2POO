"""El archivo ‘alumnos.csv’ almacena la información de los alumnos inscriptos en las carreras de la
universidad. La estructura del mismo es la siguiente: dni, apellido, nombre, carrera, año de la
carrera que cursa.

El archivo ‘materiasAprobadas.csv’ almacena información de las materias que los alumnos
inscriptos en una carrera, han aprobado en los últimos tres meses, por examen, equivalencia o
promoción. La estructura de dicho archivo es la siguiente: dni, nombre de materia, fecha, nota,
aprobación (‘E’ – Examen, ‘X’ – Equivalencia, ‘P’ – Promoción).
Los archivos no presentan ningún orden en particular. """

class Alumno:
    __dni : str
    __apellido : str
    __nombre : str
    __carrera : str
    __añocarrera : str
    
    def __init__(self,dni,apellido,nombre,carrera,añocarrera):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__añocarrera = añocarrera
        
        
    def __str__(self):
        return "dni |{}| apellido |{}| nombre |{}| carrera |{}| añocarrera |{}|".format(self.__dni,self.__apellido,self.__nombre,self.__carrera,self.__añocarrera)
    
    def retornaDni(self):
        return str(self.__dni)
    
    def retornaNombre(self):
        return self.__nombre
    
    def retornaApellido(self):
        return self.__apellido
    
    def retornaAñoCarrera(self):
        return self.__añocarrera
    
    def __lt__(self,otroAlumno):
        cadena1 = "" + str(self.__nombre) +" "+str(self.__apellido)
        cadena2 = "" + str(otroAlumno.retornaNombre()) +" "+str(otroAlumno.retornaApellido)
        return cadena1 < cadena2
        