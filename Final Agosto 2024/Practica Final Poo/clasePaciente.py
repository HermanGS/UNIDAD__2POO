class Paciente:
    __nombre: str
    __apell: str
    __email: str
    __numTel: int
    __vConsulta = 15000

    def __init__(self, nombre, apellido, email, numtel):
        self.__nombre = nombre
        self.__apell = apellido
        self.__email = email
        self.__numTel = numtel

    @classmethod
    def getValorConsulta(cls):
        return cls.__vConsulta
     
    def calculoSegunPaciente(self):
        pass

    def calcularImporte(cls):
        return cls.getValorConsulta() + cls.calculoSegunPaciente()
    
    def __str__(self) -> str:
        return f'{self.__nombre}, {self.__apell}, {self.__email}, {self.__numTel}'

