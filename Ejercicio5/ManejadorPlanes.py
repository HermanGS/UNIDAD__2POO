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

import csv
from PlanAhorro import PlanAhorro

class ManejadorPLanes:


    def __init__(self) -> None:
        self.__ListaPlanes = []

    def IngresoArchivo(self):

        nombreArchivo = 'planes.csv'
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo,delimiter = ';')
        encabezado = next(reader)
        print("<------------------------------------------------------------------------------------------------>")
        print("Ingreso de datos desde el Archivo [{}] .... Cargando".format(nombreArchivo))        
        print(encabezado)
        for fila in reader:
            codigo = int(fila[0])
            modelo = str(fila[1])
            version = str(fila[2])
            valor = float(fila[3])
            cantidadCuotas = int(fila[4])
            cantidadCuotasLicitar = int(fila[5])
            ObjetoPlanAhorro = PlanAhorro(codigo,modelo,version,valor,cantidadCuotas,cantidadCuotasLicitar)
            print("Ingresando PlanAhorro : ",ObjetoPlanAhorro)
            self.__ListaPlanes.append(ObjetoPlanAhorro)
        print("Ingreso de datos FINALIZADO ... :D")
        print("<------------------------------------------------------------------------------------------------>")
        archivo.close()

   
   
    def MostrarPlanes(self):
        print("<------------------------------------------------------------------------------------------------>")
        print("Mostrando todos los planes disponibles ...")
        for i in self.__ListaPlanes:
            print(i)
        print("<------------------------------------------------------------------------------------------------>")
    

    def ModificarValoresVehiculos(self):
        print("<------------------------------------------------------------------------------------------------>")
        for plan in self.__ListaPlanes:
            plan.modificaValorVehiculo()
            print("\n")
        print("<------------------------------------------------------------------------------------------------>")
            

    def InfoPrecioAlmenorValorCuota(self,valorCuota):
        print("<------------------------------------------------------------------------------------------------>")
        print("Planes de Ahorro Con Vehiculos con Valor de la Cuota menor al Ingresado")
        for plan in self.__ListaPlanes:
            if plan.retornaValorCuota() < valorCuota:
                plan.mostrarDatos()
                print("\n")
        print("<------------------------------------------------------------------------------------------------>")

    def MontoParaLicitarTodosLosPlanes(self):
        print("<------------------------------------------------------------------------------------------------>")
        print("Monto Necesario para Licitar Los Vehiculos : ")
        for plan in self.__ListaPlanes:
            print("codigo: {} Monto : {} ".format(plan.retornaCodigoPlan(),plan.MontoParaLicitar()))
        print("<------------------------------------------------------------------------------------------------>")


    def ModificarCantidadCuotasLicitarPorCodigo(self):
        print("<------------------------------------------------------------------------------------------------>")
        cod = (input("Ingrese el codigo del Plan, para modificar La CANTIDAD DE CUOTAS para Licitar : "))
        while  cod.isdigit() != True:
            print("ERROR - Ingreso de codigo erroneo, ingrese nuevamente : ")
            cod = (input("Respuesta : "))
        cod = int(cod)
        i = 0
        while i < len(self.__ListaPlanes) and self.__ListaPlanes[i].retornaCodigoPlan() != cod:
            i = i + 1
        if i < len(self.__ListaPlanes):
            print("Plan Encontrado : {} ".format(self.__ListaPlanes[i]))
            nueva = int(input("Ingrese la nueva Cantidad De Cuotas Para Licitar : "))
            self.__ListaPlanes[i].modificaCantidadCuotasLicitar(nueva)
            print("Cantidad establecida : ",self.__ListaPlanes[i].retornaCantidadCuotasLicitar())
        else: print("No se encontro el Plan con codigo : {}".format(cod))
        print("<------------------------------------------------------------------------------------------------>")
        

    
                