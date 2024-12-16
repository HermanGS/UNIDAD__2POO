class Ruta:
    __codigo : int
    __destino : str
    __distanciaTotalKM: float
    __rutaAsignada : bool

    def __init__(self,codigo,destino,distanciaTotalKM,rutaAsignada):
        self.__codigo = codigo
        self.__destino = destino
        self.__distanciaTotalKM = distanciaTotalKM
        self.__rutaAsignada = rutaAsignada


    def __str__(self):
        return f'{self.__codigo}, {self.__destino}, {self.__distanciaTotalKM}, {self.__rutaAsignada}'
    
    def getRutaAsignada(self):
        return self.__rutaAsignada
    
    def setRutaOcupada(self):
        self.__rutaAsignada = True

    def setRutaLibre(self):
        self.__rutaAsignada = False
        