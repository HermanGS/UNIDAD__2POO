class Nodo:
    __dato: None
    __siguiente: None

    def __init__(self,dato=None):
        self.__dato = dato
        self.__siguiente = None

    def getDato(self):
        return self.__dato 
    
    def setDato(self,x):
        self.__dato = x

    def getSig(self):
        return self.__siguiente
    
    def setSig(self,s):
        self.__siguiente = s