"""El archivo ‘alumnos.csv’ almacena la información de los alumnos inscriptos en las carreras de la
universidad. La estructura del mismo es la siguiente: dni, apellido, nombre, carrera, año de la
carrera que cursa.

El archivo ‘materiasAprobadas.csv’ almacena información de las materias que los alumnos
inscriptos en una carrera, han aprobado en los últimos tres meses, por examen, equivalencia o
promoción. La estructura de dicho archivo es la siguiente: dni, nombre de materia, fecha, nota,
aprobación (‘E’ – Examen, ‘X’ – Equivalencia, ‘P’ – Promoción).
Los archivos no presentan ningún orden en particular. """

class MateriaAprobada:
    __dni : str
    __nombreMateria : str
    __fecha : str
    __nota : int
    __aprobacion : str
    
    def __init__(self,dni,nombreMateria,fecha,nota,aprobacion):
        self.__dni = dni
        self.__nombreMateria = nombreMateria
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion
        
    def __str__(self):
        return "dni |{}| nombreMateria |{}| fecha |{}| nota |{}| Aprobacion |{}|".format(self.__dni,self.__nombreMateria,self.__fecha,self.__nota,self.__aprobacion)
    
    def retornaDni(self):
        return self.__dni
    
    def retornaNombreMateria(self):
        return self.__nombreMateria
    
    def retornaNota(self):
        return self.__nota
    
    def retornaAprobacion(self):
        return self.__aprobacion
    
    def retornaFecha(self):
        return self.__fecha
    