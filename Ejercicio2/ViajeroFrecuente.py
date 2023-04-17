


class ViajeroFrecuente:
    __NumeroViajero : int
    __Dni : str
    __Nombre : str
    __Apellido : str
    __MillasAcum : float



    def __init__(self,NumeroV,DNI,NOMBRE,APELLIDO,MillasAcum):
        self.__NumeroViajero = NumeroV
        self.__Dni = DNI
        self.__Nombre = NOMBRE
        self.__Apellido = APELLIDO
        self.__MillasAcum = MillasAcum

    

    def getNumeroViajero(self):
        return self.__NumeroViajero


    def CantidadTotalMillas(self):
        return (self.__MillasAcum)

    def AcumularMillas(self,suma):
        self.__MillasAcum = self.__MillasAcum + suma
        print("Cantidad Actual de Millas : ",self.CantidadTotalMillas())

    def CanjearMillas(self,cantcanje):
        if cantcanje >= 0:
            if cantcanje <= self.__MillasAcum:
                self.__MillasAcum = self.__MillasAcum - cantcanje
            else: print("el valor que se quiere canjear es inválido : es mayor a la cantidad de millas acumuladas") 
        else: print("El valor que se quiere canjear es inválido: es menor a cero(0)")
        print("Cantidad Actual de Millas : ",self.CantidadTotalMillas())

    def __str__(self):
        return("Numero Viajero : {} DNI : {} NOMBRE : {} APELLIDO : {} MILLASACUM : {}".format(self.__NumeroViajero,self.__Dni,self.__Nombre,self.__Apellido,self.__MillasAcum))    
    
    def VerificarNumViajero(self,numV):
        return(numV == self.__NumeroViajero)


