
from datetime import datetime
class Presentacion:
    __nombreBanda: str
    __horaInicio : str
    __horaFin : str

    def __init__(self,nombreBanda,horaInicio,horaFin):
        self.__nombreBanda = nombreBanda

        self.__horaInicio = datetime.strptime(horaInicio, "%H:%M")
        self.__horaFin = datetime.strptime(horaFin, "%H:%M")



        if self.__horaInicio > self.__horaFin:
            raise ValueError            
        


    def __str__(self):
        return f'{self.__nombreBanda} {self.__horaInicio} {self.__horaFin}'
    
    def getNombreBanda(self):
        return self.__nombreBanda
    
    def getHoraInicio(self):
        return self.__horaInicio