from claseEvento import Evento
class ExposicionArtistica(Evento):
    __numeroObras: int
    __frecuenciaApertura : str


    def __init__(self,titulo,numeroAsistentes,frecuencia,numeroObras,):
        super().__init__(titulo,numeroAsistentes)
        self.__frecuenciaApertura = frecuencia
        self.__numeroObras = numeroObras
        
    
    #def __str__(self):
        #return super().__str__() + f'{self.__frecuenciaApertura}, {self.__numeroObras}'
    
    def __str__(self):
        return super().__str__()

    #def __del__(self):
    #    print("Eliminando Las Exposiciones Artisticas")

    def DivisorIndice(self):
        divisor = self.__numeroObras
        if self.__frecuenciaApertura == 'semanal':
            divisor = self.__numeroObras * 4
        return divisor