"""    """"""El taller Castillo SRL”, recibe autos de sus clientes para diversas reparaciones. Lleva dos
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


"""De las reparaciones realizadas al vehículo, se registra en el archivo reparaciones.csv, la
siguiente información: patente, reparación, repuesto, precio repuesto, precio de mano de
obra, estado (‘T’-Terminado, ‘P’-Pendiente)."""


class Reparacion:
    __patente : str
    __reparacion : str
    __repuesto : str
    __precioRepuesto : float
    __precioManoDeObra : float
    __estado : str
    
    def __init__(self,patente,reparacion,precioRepuesto,precioManoDeObra,estado):
        self.__patente = patente
        self.__reparacion = reparacion
        #self.__repuesto = repuesto
        self.__precioRepuesto = precioRepuesto
        self.__precioManoDeObra = precioManoDeObra
        self.__estado = estado
        
    def __str__(self):
        return "patente : {} reparacion : {} precio Repuesto : {} precio Mano de Obra : {} estado : {}".format(self.__patente,self.__reparacion,self.__precioRepuesto,self.__precioManoDeObra,self.__estado)
    
    """Reparación precio repuesto mano de obra subtotal
xxxxxxxxxxxxxxxxxx $xxx.xx $xxx.xx $xxxx.xx
xxxxxxxxxxxxxxxxxx $xxx.xx $xxx.xx $xxxx.xx
TOTAL A PAGAR $xxxx.xx
El subtotal se calcula como la suma de precio de repuesto y precio de mano de obra, y
el total a pagar, es la suma de todos los subtotales. """
    
    
    def MostrarDatos(self):
        subtotal = self.__precioRepuesto + self.__precioManoDeObra
        print("{:10}{:10}{:10}{:10}".format(self.__reparacion,self.__precioRepuesto,self.__precioManoDeObra,subtotal))
        return subtotal
    
    def retornaPatente(self):
        return self.__patente

    def retornaEstado(self):
        return self.__estado
    
    def retornaReparacion(self):
        return self.__reparacion