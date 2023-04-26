


class Registro:
    __Temperatura : float
    __Humedad : int
    __Presion : float

    def __init__(self,Temperatura = 0.0,Humedad = 0,Presion = 0.0):
        if((type(Temperatura)==float )and (type(Humedad)==int) and (type(Presion)==float)):
            self.__Temperatura = Temperatura
            self.__Humedad = Humedad
            self.__Presion = Presion

    def retornaTemperatura(self):
        return self.__Temperatura

    def retornaHumedad(self):
        return self.__Humedad

    def retornaPresion(self):
        return self.__Presion



    def __str__(self):
        #temp = "[Temperatura]"
        #hum = "[Humedad]"
        #pre = "[PresionAtmosférica]"
        #print(len(temp))
        #print(len(hum))
        #print(len(pre))
        return "{:12} {:10} {:12}".format(self.__Temperatura,self.__Humedad,self.__Presion)

    
