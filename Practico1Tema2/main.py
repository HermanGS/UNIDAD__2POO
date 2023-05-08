
"""El taller Castillo SRL”, recibe autos de sus clientes para diversas reparaciones. Lleva dos
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

from ManejadorClientes import ManejadorClientes
from ManejadorReparaciones import ManejadorReparaciones


def MostrarFormatoMain(MC,MR):
    print("Ingrese un dni para mostrar con formato")
    dni = str(input("Respuesta : "))
    MC.MostrarFormato(MR,dni)

def ReparacionesTerminadasMain(MC,MR):
    print("Ingrese una patente para saber si las reparaciones estan terminadas")
    patente = str(input("Respuesta : "))
    MR.ReparacionesTerminadas(MC,patente)
    
def MostrarFormatoReparacionesSinTerminarMain(MC,MR):
    MC.MostrarFormatoReparacionesSinTerminar(MR)
    
def MostrarClienteRepetido(MC,MR):
    MC.MostrarRepetidos()


if __name__ == '__main__':
    print("___ Principal __")
    
    MC = ManejadorClientes()
    MC.IngresoArchivoClientes()
    print("\n")
    MR = ManejadorReparaciones()
    MR.IngresoArchivoReparaciones()
    #MostrarFormatoMain(MC,MR)
    print("\n")
    #ReparacionesTerminadasMain(MC,MR)
    print("\n")
    #MostrarFormatoReparacionesSinTerminarMain(MC,MR)
    MostrarClienteRepetido(MC,MR)