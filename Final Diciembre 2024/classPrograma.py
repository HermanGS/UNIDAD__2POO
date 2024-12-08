from datetime import datetime

class Programa: 
    __nombre:str
    __hrI:datetime
    __hrF:datetime
    __valido : bool



    def __init__(self, hrI, hrF, nombre):
        self.__valido = False
        try:
            self.__hrI = datetime.strptime(hrI, "%H:%M")
            self.__hrF= datetime.strptime(hrF, "%H:%M")
            if self.__hrI > self.__hrF:
                raise ValueError
    
        except ValueError:
            print("Error - horario mal escrito")
            
        else:
            self.__nombre = nombre
            self.__valido = True
            
    def getValido(self):
        return self.__valido
    
    def __str__(self):
        return self.__nombre + " " + str(self.__hrI) + str(self.__hrF)
    
    def getHorarioInicio(self):
        return self.__hrI


        