from clasePaciente import Paciente

class pacienteA(Paciente):
    __historial: str
    __alergias:str
    __obraSocial:str

    def __init__(self, nombre, apellido, email, numtel, historial, alergias, obraSocial):
        super().__init__(nombre,apellido, email, numtel)
        self.__historial = historial
        self.__alergias = alergias
        self.__obraSocial = obraSocial

    def getObraSocial(self):
        return self.__obraSocial
    
    def getPlusObraSocial(self):
        descuento = -self.getValorConsulta()
        print("descuento de ",descuento)
        if self.__obraSocial == "Obra Social Provincia":
            descuento = descuento + 5000
        elif self.__obraSocial == "OSDE":
            descuento = descuento + 2000
        else:
            descuento = descuento + 10000
        return descuento
    
    def calculoSegunPaciente(self):
        return  self.getPlusObraSocial() 
    
    def __str__(self) -> str:
        return super().__str__() + f'{self.__historial}, {self.__alergias}, {self.__obraSocial}'
    

    