from claseVehiculo import Vehiculo
from claseRuta import Ruta

class Camion(Vehiculo):
    __capacidadMaxCarga: float
    __cantRealTransp: float
    __ListaRutas : list

    def __init__(self, matricula, modelo, costoKM, cantDiasAlquiler,capacidadMaxCarga,cantRealTransp):
        super().__init__(matricula, modelo, costoKM, cantDiasAlquiler)
        self.__capacidadMaxCarga = capacidadMaxCarga
        self.__cantRealTransp = cantRealTransp
        self.__ListaRutas = []

    def RutasToSTR(self):
        c = ""
        for i in range(len(self.__ListaRutas)):
            c = c + str(self.__ListaRutas[i]) + " / "
        return c
    
    def getCantRutas(self):
        return len(self.__ListaRutas)
    
    def __str__(self):
        return "Camion : "+ super().__str__() + f'{self.__capacidadMaxCarga}, {self.__cantRealTransp} \nRutas Del Camion : {self.RutasToSTR()}'
    
    def agregarRuta(self,ruta):
        self.__ListaRutas.append(ruta)

    def MultiplicadorAlquiler(self):
        valor = 0
        if self.__cantRealTransp > 4500:
            valor = (self.getCantDias() * self.getCostoKM()) + (self.getCostoKM() * 0.05)
        elif self.__cantRealTransp < 4500:
            valor = (self.getCantDias() * self.getCostoKM()) + (self.getCostoKM() * 0.02)
        
        return valor
    
