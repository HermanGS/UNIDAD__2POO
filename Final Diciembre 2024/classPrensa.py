from classMedio import Medios
class Prensa(Medios):
    __periodicidad: str
    __cantSecc: int

    def __init__(self,nombre, audiencia, cantSecc, periodicidad):
        super().__init__(nombre, audiencia)
        self.__periodicidad = periodicidad
        self.__cantSecc = cantSecc

    def __str__(self) -> str:
        return " "+super().__str__() +" "+ str(self.__cantSecc) +" "+ str(self.__periodicidad)

    def CalculoDivisorDelIndice(self):
        divisor = 1
        if self.__periodicidad == "mensual":
            divisor = (self.__audiencia )
        elif self.__periodicidad == "semanal":
            divisor = self.__audiencia * 4
        return divisor
        
    

