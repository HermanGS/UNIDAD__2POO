class Medios:
    __nombre:str
    __audiencia: int

    def __init__(self, nombre, audiencia):
        self.__audiencia=audiencia
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre
    
    def __str__(self) -> str:
        return " "+str(self.__nombre) +" "+ str(self.__audiencia) + " tipo : "+str(type(self))
    
    def CalculoIndice(self):
        return self.__audiencia / self.CalculoDivisorDelIndice()

    def CalculoDivisorDelIndice(self):
        pass