class Equipo:
    __marca: str
    __modelo: str
    __anioFabricacion : str
    __tipoCombustible : str
    __potencia : str
    __capacidad_Carga : float
    __tarifaAlquiler : float
    __cantDiasAlquiler : int

    def __init__(self,marca,modelo,anioFabri,tipoCombus,potencia,capacidadCarga,AlquilerDiario,cantDiasAlquiler):
        self.__marca = marca
        self.__modelo = modelo
        self.__anioFabricacion = anioFabri
        self.__tipoCombustible = tipoCombus
        self.__potencia = potencia
        self.__capacidad_Carga = capacidadCarga
        self.__AlquilerDiario = AlquilerDiario
        self.__cantDiasAlquiler = cantDiasAlquiler

    def AlquilerSegunEquipo(self):
        pass

    def CalculoTarifaAlquiler(self):
        return self.__AlquilerDiario * self.AlquilerSegunEquipo()
    
    def __str__(self):
        return f'{self.__marca}, {self.__modelo}, {self.__anioFabricacion}, {self.__tipoCombustible}, {self.__potencia}, {self.__capacidad_Carga}, {self.__cantDiasAlquiler}, '
    
    def getAnioFabricacion(self):
        return self.__anioFabricacion
    
    # para mostrar datos y Tarifa :

    def mostrarDatos(self):
        c = f'{self.__marca}, {self.__modelo}, {self.__anioFabricacion}, {self.__potencia}, {self.__cantDiasAlquiler}, '
        return c
    # Las clases hijas no pueden llamar a un método no polimorfico, por eso lo hago así :

    def mostrarDatosYtarifa(self):
        return self.mostrarDatos() +"\nTarifa de Alquiler :"+ str(self.CalculoTarifaAlquiler()) + "\n"

    # Necesario para poder usar los atributos de una clase PADRE :

    def getTipoCombus(self):
        return self.__tipoCombustible

    def getCapacidadCarga(self):
        return self.__capacidad_Carga
    
    def getCantDiasAlquiler(self):
        return self.__cantDiasAlquiler
     