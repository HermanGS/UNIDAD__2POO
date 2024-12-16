from claseVehiculo import Vehiculo

class Automovil(Vehiculo):
    __cantPasajerosMax: int
    __cantPasajerosReal : int
    

    def __init__(self, matricula, modelo, costoKM, cantDiasAlquiler,cantPasajerosMax,cantPasajerosReal):
        super().__init__(matricula, modelo, costoKM, cantDiasAlquiler)
        self.__cantPasajerosMax = cantPasajerosMax
        self.__cantPasajerosReal = cantPasajerosReal

    def __str__(self):
        return "Automovil : "+ super().__str__() + f'{self.__cantPasajerosMax}, {self.__cantPasajerosReal}'
    
    #metodo polimorfico
    def MultiplicadorAlquiler(self):
        valor = (self.getCantDias() * ( self.getCostoKM() + 5000 )  * self.__cantPasajerosReal)
        return valor
    
