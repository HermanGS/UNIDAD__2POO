from claseEquipo import Equipo
class MaquinariaPesada(Equipo):
    __tipoMaquinaria : str
    __peso : int


    def __init__(self,marca,modelo,anioFabri,tipoCombus,potencia,capacidadCarga,AlquilerDiario,cantDiasAlquiler,tipoMaquinaria,peso):
        super().__init__(marca,modelo,anioFabri,tipoCombus,potencia,capacidadCarga,AlquilerDiario,cantDiasAlquiler)
        self.__tipoMaquinaria = tipoMaquinaria
        self.__peso = peso

    def AlquilerSegunEquipo(self):
        cantDias = self.__cantDiasAlquiler
        if self.__peso > 10:
            cantDias = cantDias + (cantDias * 0.2)
        return cantDias
    
    def __str__(self):
        c = ''
        if type(self) == MaquinariaPesada:
            c = 'Maquinaria Pesada'
        return f'tipo: {c} \n' + super().__str__() + f'{self.__tipoMaquinaria}, {self.__peso} '
    
    def getPeso(self):
        return self.__peso
    
    def mostrarDatos(self):
        return super().mostrarDatos() + f'{self.getTipoCombus()}, {self.getCapacidadCarga()} ' 