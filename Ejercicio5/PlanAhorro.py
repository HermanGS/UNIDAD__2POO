"""Ejercicio 5
Datos miembro estáticos y Funciones miembro estáticas 
Un concesionario de automóviles ofrece distintos planes de ahorro y se requiere la definición de una clase “PlanAhorro” que represente a cada uno de ellos.

Los datos que es necesario registrar son: código del plan, modelo y versión del vehículo, valor del vehículo, cantidad de cuotas del plan, cantidad de cuotas que debe tener pagas para licitar el vehículo (los últimos dos atributos son los mismos para todos los planes).

El primer día hábil del mes se actualiza el valor del vehículo.

El importe de la cuota se calcula:

valor cuota = (importe vehículo/cantidad de cuotas) + importe vehículo * 0.10

Implemente un programa que: 

1-      Lea desde un archivo separado con “;” los datos de los planes y genere una lista que almacene instancias de la clase “PlanAhorro”.

2-      Presente un menú de opciones permita:

a.       Actualizar el valor del vehículo de cada plan. Para esto se muestra el código del plan, el modelo y versión del vehículo, luego se ingresa el valor actual del vehículo y se modifica el atributo correspondiente.

b.      Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.

c.       Mostrar el monto que se debe haber pagado para licitar el vehículo (cantidad de cuotas para licitar * importe de la cuota).

d.      Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar. """

class PlanAhorro:
    __codigoPlan : int
    __modelo : str
    __versionVehiculo : str
    __valorVehiculo : float
    __cantidadCuotas : int
    __cantidadCuotasLicitar : int


    def __init__(self,codigoplan,modelo,version,valor,cantidadcuotas,cantidadcuotaslicitar):
        if type(codigoplan) == int and type(modelo) == str and type(version) == str and type(valor) == float and type(cantidadcuotas) == int and type(cantidadcuotaslicitar) == int: 
            self.__codigoPlan = codigoplan
            self.__modelo = modelo
            self.__versionVehiculo = version
            self.__valorVehiculo = valor
            self.__cantidadCuotas = cantidadcuotas
            self.__cantidadCuotasLicitar = cantidadcuotaslicitar

    
    def retornaCodigoPlan(self):
        return self.__codigoPlan
    
    def retornaModelo(self):
        return self.__modelo
    
    def retornaVersionVehiculo(self):
        return self.__versionVehiculo
    
    def retornaValorVehiculo(self):
        return self.__valorVehiculo
    
    def modificaValorVehiculo(self):
        print("Codio del Plan : {}".format(self.__codigoPlan))
        print("Modelo del Vehiculo : {}".format(self.__modelo))
        print("Version del Vehiculo : {}".format(self.__versionVehiculo))
        print("Valor Viejo : {}".format(self.__valorVehiculo))
        print("\n")
        nuevo = float(input("Ingrese el Nuevo valor del Vehiculo : "))
        self.__valorVehiculo = nuevo


    def retonaCantidadCuotas(self):
        return self.__cantidadCuotas
    
    def retornaCantidadCuotasLicitar(self):
        return self.__cantidadCuotasLicitar
    
    def modificaCantidadCuotasLicitar(self,nuevacantidad):
        self.__cantidadCuotasLicitar = nuevacantidad
    
    def retornaValorCuota(self):
        ValorCuota = (self.__valorVehiculo / self.__cantidadCuotas) + self.__valorVehiculo * 0.10
        return ValorCuota
    
    def MontoParaLicitar(self):
        return self.__cantidadCuotasLicitar * self.retornaValorCuota()
    
    """
    def retornaValorCuota(self):
        return self.__ValorCuota
    """

    def __str__(self) -> str:
        return "Codigo : {} Modelo : {} Version : {} Valor : {} Cantidad de Cuotas : {} Cantidad de Cuotas para Licitar : {}".format(self.__codigoPlan,self.__modelo,self.__versionVehiculo,self.__valorVehiculo,self.__cantidadCuotas,self.__cantidadCuotasLicitar)
    
    def mostrarDatos(self):
        print("Codigo del Plan : {} \nModelo : {}\nVersion : {}".format(self.__codigoPlan,self.__modelo,self.__versionVehiculo))