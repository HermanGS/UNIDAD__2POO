



import csv
from cliente import Cliente
from ManejadorReparaciones import ManejadorReparaciones

class ManejadorClientes:
    __ListaClientes : list
    
    def __init__(self):
        self.__ListaClientes = []
    
    def IngresoArchivoClientes(self):
        nombreArchivo = 'clientes.csv'
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo,delimiter=';')
        #next(reader)
        for fila in reader:
            #dni;apellido;nombre;telefono;patente;vehiculo;estado
            dni = str(fila[0])
            apellido = str(fila[1])
            nombre = str(fila[2])
            telefono = str(fila[3])
            patente = str(fila[4])
            vehiculo = str(fila[5])
            estado = str(fila[6])
            ObjetoCliente = Cliente(dni,apellido,nombre,telefono,patente,vehiculo,estado)
            self.__ListaClientes.append(ObjetoCliente)
            print("Ingresando Cliente : ",ObjetoCliente)
        print("-------- Ingreso Finalizado --------")
        archivo.close()
        
    def MostrarTodo(self):
        for i in range(len(self.__ListaClientes)):
            print(self.__ListaClientes[i])
            
    
    """Leer un Dni de un cliente por teclado en informar los datos del cliente y todas las
reparaciones hechas al vehículo siguiendo el siguiente formato:
DNI: xxxxxxxx Apellido y nombre: xxxxxxxxxxxxxxxxxxxx
Patente: xxxxxxx Vehículo: xxxxxxxxxxxxxxxxxx
Reparación precio repuesto mano de obra subtotal
xxxxxxxxxxxxxxxxxx $xxx.xx $xxx.xx $xxxx.xx
xxxxxxxxxxxxxxxxxx $xxx.xx $xxx.xx $xxxx.xx
TOTAL A PAGAR $xxxx.xx
El subtotal se calcula como la suma de precio de repuesto y precio de mano de obra, y
el total a pagar, es la suma de todos los subtotales. """
    
    def BuscarCLientePorDni(self,dni):
        i = 0
        while i < len(self.__ListaClientes) and self.__ListaClientes[i].retornaDni() != dni:
            i = i + 1
        if i < len(self.__ListaClientes):
            return self.__ListaClientes[i]
        else:
            print("No se encontro el cliente con el dni buscado")
            
    def BuscarCLientePorPatente(self,patente):
        i = 0
        while i < len(self.__ListaClientes) and self.__ListaClientes[i].retornaPatente() != patente:
            i = i + 1
        if i < len(self.__ListaClientes):
            return i
        else:
            print("No se encontro el cliente con la patente buscada")
            
    def CambiarEstadoClientePorPatente(self,patente):
        clienteIndice = self.BuscarCLientePorPatente(patente)
        self.__ListaClientes[clienteIndice].modificaEstado('Terminao')
    
    
         
    def MostrarFormato(self,ManejadorReparaciones,dni):
        print("\n")
        cliente = self.BuscarCLientePorDni(dni)
        if type(cliente) == Cliente:
            cliente.MostrarDatos()
            patente = cliente.retornaPatente()
            print("Reparación           precioRepuesto          manodeobra          subtotal")
            total = ManejadorReparaciones.MostrarFormatoReparaciones(patente)
            print("Total : ",total)
        print("\n")
    
    
    """c. Listar los datos de los clientes a los que no les han terminado el las reparaciones
indicando las reparaciones pendientes, siguiendo el siguiente formato:
Apellido y nombre: xxxxxxxxxxxxxxxxxxxx Teléfono:xxxxxxxxxxxx
Patente: xxxxxxx Vehículo: xxxxxxxxxxxxxxxxxx
Reparacion
xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx"""    
        
    def MostrarFormatoReparacionesSinTerminar(self,ManejadorReparaciones):
        print("\n")
        print("Mostrar Reparaciones sin Terminar por cliente")
        for i in range(len(self.__ListaClientes)):
            self.__ListaClientes[i].MostrarDatos2()
            patente = self.__ListaClientes[i].retornaPatente()
            print("Reparacion : ")
            bandera = ManejadorReparaciones.MostrarFormato2(patente)
            print("\n")
        if bandera != True:
            print("--- No tiene Reparaciones por hacer --- ")
            
            
    def MostrarRepetidos(self):
        Lista2 = self.__ListaClientes.copy()
        for i in range(len(Lista2)):
            for j in range(len(self.__ListaClientes)):
                print("comparaciones")
                print(self.__ListaClientes[j]," y ", Lista2[i])
                if self.__ListaClientes[j] == Lista2[i]:
                    print(self.__ListaClientes[j])
                      
            
            