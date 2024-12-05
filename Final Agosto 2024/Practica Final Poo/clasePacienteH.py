from clasePaciente import Paciente

class pacienteH(Paciente):
    __numHab: int
    __fechaI: int
    __diagnostico: str
    __cantDias: int
    __importe: float
    
    def __init__(self, nombre, apellido, email, numtel, numHab, fechaI, diagnostico, cantDias, importe ):
        super().__init__(nombre,apellido, email, numtel)
        self.__numHab = numHab
        self.__fechaI = fechaI
        self.__diagnostico = diagnostico
        self.__cantDias = cantDias
        self.__importe = importe
    
    def getDiagnostico(self):
        return self.__diagnostico

    def calculoSegunPaciente(self):
        ##print("valor de consulta en clase P Hospitalizado con Self = ",self.getValorConsulta())
        ##return self.__cantDias * 15000 + self.__importe
        print("valor de la consulta en h en calculo segun paciente : ",{self.getValorConsulta()})
        return self.__cantDias * self.getValorConsulta() + self.__importe

    def __str__(self) -> str:
        return super().__str__() + f' {self.__numHab}, {self.__fechaI}, {self.__diagnostico}, {self.__cantDias}, {self.__importe} '
