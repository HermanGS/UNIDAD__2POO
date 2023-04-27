


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

    def AcumularMillas2(self,suma):
        self.__MillasAcum = self.__MillasAcum + suma


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

    
    def __gt__(self,other):
        if type(self) == type(other):
            #print("self millas = ",self.__MillasAcum,"other Millas",other.CantidadTotalMillas())
            return self.__MillasAcum > other.CantidadTotalMillas()
        else: print("Error los Objetos Comparados no son iguales")
    
        """    
        def __add__(self,numero):
            nuevoViajero = self
            nuevoViajero.AcumularMillas2(numero)
            return nuevoViajero
        """

    
    def __add__(self,numero):
        valorNuevoMillas = self.__MillasAcum + numero
        return(ViajeroFrecuente(self.__NumeroViajero,self.__Dni,self.__Nombre,self.__Apellido,valorNuevoMillas))
    
    def __sub__(self,numero):
        if numero >= 0:
            if numero <= self.__MillasAcum:
                valorNuevoMillasCanje = self.__MillasAcum - numero
                return (ViajeroFrecuente(self.__NumeroViajero,self.__Dni,self.__Nombre,self.__Apellido,valorNuevoMillasCanje))
            else: print("ERROR - El valor a Canjear es Mayor que las millas Existentes")
        else: print("ERROR - El valor a Canjear es Menor que 0 (cero)")

    def __eq__(self, __value: object) -> bool:
        return self.__MillasAcum == __value
    
    def __radd__(self,numero):
        valorNuevoMillas = numero + self.__MillasAcum
        return(ViajeroFrecuente(self.__NumeroViajero,self.__Dni,self.__Nombre,self.__Apellido,valorNuevoMillas))
    
    def __rsub__(self,numero):
        if numero >= 0:
            if numero <= self.__MillasAcum:
                valorNuevoMillasCanje = self.__MillasAcum - numero
                return (ViajeroFrecuente(self.__NumeroViajero,self.__Dni,self.__Nombre,self.__Apellido,valorNuevoMillasCanje))
            else: print("ERROR - El valor a Canjear es Mayor que las millas Existentes")
        else: print("ERROR - El valor a Canjear es Menor que 0 (cero)")
        