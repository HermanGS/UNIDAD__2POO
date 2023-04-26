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





class Menu:


    def op1(self,Manejador):
        print("Entro al 1")
        Manejador.ModificarValoresVehiculos()
        print("Como quedaron los Planes : ")
        Manejador.MostrarPlanes()

    def op2(self,Manejador):
        print("Entro al 2")
        print("Ingrese un Valor de Cuota para Mostrar los Planes con cuotas menores a la Cuota Ingresada : ")
        print("(... Si no aparece ninguna, ninguna cuota es menor a la ingresada ... )")
        cuota = float(input("Cuota = "))
        Manejador.InfoPrecioAlmenorValorCuota(cuota)


    def op3(self,Manejador):
        print("Entro al 3")
        Manejador.MontoParaLicitarTodosLosPlanes()

    def op4(self,Manejador):
        print("Entro al 4")
        Manejador.ModificarCantidadCuotasLicitarPorCodigo()

        
    def ElegirOP(self,Manejador):
        op = -1
        while op != 0:
            print("<----------------------------------------------------------------------------------------------------->")
            print("\n Ingrese una opcion : 1,2,3 o 4 (Ingrese 0 para terminar) ")
            print("1.      Actualizar el valor del vehículo de cada plan. Para esto se muestra el código del plan, el modelo y versión del vehículo, luego se ingresa el valor actual del vehículo y se modifica el atributo correspondiente.\n2.      Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.\n3.      Mostrar el monto que se debe haber pagado para licitar el vehículo (cantidad de cuotas para licitar * importe de la cuota).\n4.      Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar.")
            print("\n")
            op = int(input("Respuesta : "))
            while op < 0 or op > 4:
                print("ERROR -OPCION muy GRANDE o muy CHICA, vuelva a ingresar la opcion (entre 0 y 4)")
                op = int(input("Respuesta : "))
            if op == 1:
                self.op1(Manejador)
            elif op == 2:
                self.op2(Manejador)
            elif op == 3:
                self.op3(Manejador)
            elif op == 4:
                self.op4(Manejador)
            else: print("<---------------------  SALIENDO DEL PROGRAMA  ---------------------> ")
            