class Vehiculo:
    __matricula : str
    __modelo : str
    __costoKM : float
    __cantDiasAlquiler: int

    def __init__(self,matricula,modelo,costoKM,cantDiasAlquiler):
        self.__matricula = matricula
        self.__modelo = modelo
        self.__costoKM = costoKM
        self.__cantDiasAlquiler = cantDiasAlquiler

    def __str__(self):
        return f'{self.__matricula}, {self.__modelo}, {self.__costoKM}, {self.__cantDiasAlquiler}'
    
    #esta es la funcion del calculo alquiler polimorfica, tiene un nombre no representativo
    def MultiplicadorAlquiler(self):
        pass

    #def calculoAlquiler(self):
    #    return self.__cantDiasAlquiler * self.MultiplicadorAlquiler()
    
    def getMatricula(self):
        return self.__matricula

    def getCantDias(self):
        return self.__cantDiasAlquiler
    
    def getCostoKM(self):
        return self.__costoKM
    
    def IndicarInfo_Y_Alquiler(self):
        print("Matricula : ",self.__matricula)
        print("Modelo : ",self.__modelo)
        print("Costo Total Alquiler : ",self.MultiplicadorAlquiler())
        print("\n")