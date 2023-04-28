


class MateriasAprobadas:


    def __init__(self,dni,nombreMateria,fecha,nota,aprobacion):
        self.__dni = dni
        self.__nombreMateria = nombreMateria
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion

    def __str__(self):
        return "dni {} nombre Materia  {} fecha  {} nota  {} aprobacion  {}".format(self.__dni,self.__nombreMateria,self.__fecha,self.__nota,self.__aprobacion)


    def getNombreMateria(self):
        return self.__nombreMateria

    def getDni(self):
        return self.__dni

    def getNota(self):
        return self.__nota
    
    def getAprobacion(self):
        return self.__aprobacion

    def getFecha(self):
        return self.__fecha

    
