from claseEquipo import Equipo
class HerramientaElectrica(Equipo):
    __tipoHerramienta: str

    def __init__(self,marca,modelo,anioFabri,tipoCombus,potencia,capacidadCarga,AlquilerDiario,cantDiasAlquiler,tipoHerramienta):
        super().__init__(marca,modelo,anioFabri,tipoCombus,potencia,capacidadCarga,AlquilerDiario,cantDiasAlquiler)
        self.__tipoHerramienta = tipoHerramienta
    

    def AlquilerSegunEquipo(self):
        cantDias = self.__cantDiasAlquiler
        if self.__tipoHerramienta == 'bateria':
            cantDias = cantDias + (cantDias * 0.1)
        return cantDias
    
    def __str__(self):
        c = ""
        if type(self) == HerramientaElectrica:
            c = "Herramienta Electrica"
        return f'tipo: {c} \n'+ super().__str__() + f'{self.__tipoHerramienta} '
    
    def mostrarDatos(self):
        return super().mostrarDatos()