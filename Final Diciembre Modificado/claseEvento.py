class Evento:
    __titulo : str
    __numeroAsistentes : int


    def __init__(self,titulo,numeroAsistentes):
        self.__titulo = titulo
        self.__numeroAsistentes = numeroAsistentes
    

    def __str__(self):
        return f'{self.__titulo}, {self.__numeroAsistentes} ' + f'Indice de Popularidad : {self.CalculoIndice()}'
    
    def getTitulo(self):
        return self.__titulo
    
    #Metodo Polimorfico

    def DivisorIndice(self):
        pass

    def CalculoIndice(self):
        return self.__numeroAsistentes / self.DivisorIndice()