"""_summary_

    Returns:
        _type_: _description_
    """"""El taller Castillo SRL”, recibe autos de sus clientes para diversas reparaciones. Lleva dos
archivos, uno denominado “clientes.csv” y otro “reparaciones.csv, que registran los vehículos
que dejan los clientes para su reparación y las reparaciones realizadas a los mismos.
Del cliente y vehículo, se registra en el archivo clientes.csv, la siguiente información: Dni,
apellido, nombre, teléfono, patente, vehículo (Fiat Mobi, Renault Kangoo, por ejemplo), estado
(‘T’- Terminado, ‘P’-Pendiente).

De las reparaciones realizadas al vehículo, se registra en el archivo reparaciones.csv, la
siguiente información: patente, reparación, repuesto, precio repuesto, precio de mano de
obra, estado (‘T’-Terminado, ‘P’-Pendiente).

Nota: ambos archivos tienen como separador el carácter “;”, y no presentan ningún orden en
particular.

El analista de sistemas del taller le solicita a usted un programa en Python, para procesar
ambos archivos.
El programa debe:
1. Crear las clases Cliente y Reparación. Los datos de los archivos representan el estado de los
objetos pertenecientes a estas clases.
2. Cargar los datos de los objetos que pertenecen a la clase Cliente en un ManejadorClientes,
leyendo los datos del archivo “clientes.csv”, implemente el manejador con una Lista Python.
3. Cargar los datos de los de los objetos que pertenecen a la clase Reparación en un
ManejadorReparaciones, leyendo los datos del archivo “reparaciones.csv”, implemente el
manejador con una Lista Python.
A través de un menú de opciones, llevar a cabo las siguientes funcionalidades:
a. Leer un Dni de un cliente por teclado en informar los datos del cliente y todas las
reparaciones hechas al vehículo siguiendo el siguiente formato:
DNI: xxxxxxxx Apellido y nombre: xxxxxxxxxxxxxxxxxxxx
Patente: xxxxxxx Vehículo: xxxxxxxxxxxxxxxxxx
Reparación precio repuesto mano de obra subtotal
xxxxxxxxxxxxxxxxxx $xxx.xx $xxx.xx $xxxx.xx
xxxxxxxxxxxxxxxxxx $xxx.xx $xxx.xx $xxxx.xx
TOTAL A PAGAR $xxxx.xx
El subtotal se calcula como la suma de precio de repuesto y precio de mano de obra, y
el total a pagar, es la suma de todos los subtotales.
b. Leer una patente por teclado, determinar si todas las reparaciones están terminadas,
en caso afirmativo, cambiar el estado en el Cliente, y mostrar nombre y apellido del
cliente, el teléfono, el vehículo y el total a pagar.
c. Listar los datos de los clientes a los que no les han terminado el las reparaciones
indicando las reparaciones pendientes, siguiendo el siguiente formato:
Apellido y nombre: xxxxxxxxxxxxxxxxxxxx Teléfono:xxxxxxxxxxxx
Patente: xxxxxxx Vehículo: xxxxxxxxxxxxxxxxxx
Reparacion
xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx
d. Determinar el o los clientes que le hacen servicio a más de un vehículo, mostrando dni,
nombre, apellido, teléfono, patente y vehículo
Regla de negocio: para resolver esta funcionalidad, el analista ha determinado que es
conveniente sobrecargar el operador “==”, de modo que permi"""


"""la siguiente información: Dni,
apellido, nombre, teléfono, patente, vehículo (Fiat Mobi, Renault Kangoo, por ejemplo), estado
(‘T’- Terminado, ‘P’-Pendiente)."""

class Cliente:
    __dni : str
    __apellido : str
    __nombre : str
    __telefono : str
    __patente : str
    __vehiculo : str
    __estado : str
    
    
    def __init__(self,dni,apellido,nombre,telefono,patente,vehiculo,estado):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__telefono = telefono
        self.__patente = patente
        self.__vehiculo = vehiculo
        self.__estado = estado
        
    def __str__(self):
        return "dni : {} apellido : {} nombre : {} telefono : {} patente : {} vehiculo : {} estado : {}".format(self.__dni,self.__apellido,self.__nombre,self.__telefono,self.__patente,self.__vehiculo,self.__estado)
    
    """DNI: xxxxxxxx Apellido y nombre: xxxxxxxxxxxxxxxxxxxx
Patente: xxxxxxx Vehículo: xxxxxxxxxxxxxxxxxx"""
    
    def MostrarDatos(self):
        print("DNI : {} Apellido Y Nombre : {} {} \nPatente : {} Vehiculo : {}".format(self.__dni,self.__apellido,self.__nombre,self.__patente,self.__vehiculo))
        
    """c. Listar los datos de los clientes a los que no les han terminado el las reparaciones
indicando las reparaciones pendientes, siguiendo el siguiente formato:
Apellido y nombre: xxxxxxxxxxxxxxxxxxxx Teléfono:xxxxxxxxxxxx
Patente: xxxxxxx Vehículo: xxxxxxxxxxxxxxxxxx
Reparacion
xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx"""

    def MostrarDatos2(self):
        print(" Apellido Y Nombre : {} {} Telefono : {} \nPatente : {} Vehiculo : {}".format(self.__apellido,self.__nombre,self.__telefono,self.__patente,self.__vehiculo))
        
    
    
    def retornaDni(self):
        return self.__dni
    
    def retornaNombre(self):
        return self.__nombre
    
    def retornaApellido(self):
        return self.__apellido
    
    def retornaTelefono(self):
        return self.__telefono
    
    
    def retornaPatente(self):
        return self.__patente
    
    def modificaEstado(self,nuevoestado):
        self.__estado = nuevoestado
        
    """ Determinar el o los clientes que le hacen servicio a más de un vehículo, mostrando dni,
nombre, apellido, teléfono, patente y vehículo
Regla de negocio: para resolver esta funcionalidad, el analista ha determinado que es
conveniente sobrecargar el operador “==”, de modo que permita saber si dos clientes
son iguales cuando coincide dni, nombre, apellido y teléfono. """

    def __eq__(self,otro):
        if type(self) == type(otro):
            cadena1 = ""+ str(self.__dni) + str(self.__nombre) + str(self.__apellido) + str(self.__telefono)
            cadena2 = ""+ str(otro.retornaDni()) + str(otro.retornaNombre()) + str(otro.retornaApellido()) + str(otro.retornaTelefono())
            return cadena1 == cadena2