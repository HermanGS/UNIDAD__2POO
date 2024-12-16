from gestorRutas import GestorRutas
from gestorVehiculos import GestorVehiculos

class Menu:


    def SeleccionarOpcion(self):
        print("1-AgregarRuta a un Camion\n2-Informacion por Matricula\n3-MostrarInfoVehiculos\n4-MostrarVehiculos\n5-MostrarRutas\n6-Salir")
        op = str(input("Ingrese la opcion : "))
        while op != '1' and op != '2' and op != '3' and op != '4':
            op = str(input("Ingrese la opcion : "))
        return op

    def opciones(self,gestorVehiculos,gestorRutas):
        op = self.SeleccionarOpcion()
        while True:
            if op == '1':
                print("Opcion 1")
                print("\n")

                print("Agregar Vehiculo Menu :")
                

                OPagregado = str(input("Seleccione : 1 - Automovil / 2 - Camion      Respuesta : "))
                while OPagregado != '1' and OPagregado != '2':
                    OPagregado = str(input("Seleccione : 1 - Automovil / 2 - Camion      Respuesta : "))

                if type(gestorVehiculos) == GestorVehiculos:
                    gestorVehiculos.agregarVehiculo(gestorRutas,OPagregado)
                
                else:
                    print("El gestor del menu no es un vehiculo")

            if op == '2':
                print("Opcion 2")
                print("\n")
                print("Ingrese una matricula para obtener la informacion del Vehiculo... ")
                matricula = str(input("Ingrese la Matricula :"))
                try:
                    gestorVehiculos.BuscarVehiculoPorMatricula(matricula)
                except Exception:
                    print("Vehiculo No Encontrado...")
                

                
            if op == '3':
                print("Opcion 3")
                print("\n")
                gestorVehiculos.IndicarInfo_Y_AlquilerTODOS()
            
            if op == '4':
                print("Opcion 4")
                print("\n")
                
                if type(gestorVehiculos) == GestorVehiculos:
                    gestorVehiculos.MostrarVehiculos()

            if op == '5':
                print("Opcion 4")
                print("\n")
                if type(gestorRutas) == GestorRutas:
                    gestorRutas.MostrarRutas()
                

            if op == '6':
                print("Opcion 4")
                print("Saliendo ... \n")
                
                break

            op = self.SeleccionarOpcion()