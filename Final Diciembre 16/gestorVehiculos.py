from claseAutomovil import Automovil
from claseCamion import Camion
from gestorRutas import GestorRutas
from claseRuta import Ruta
class GestorVehiculos:
    __ListaVehiculos: list

    def __init__(self):
        self.__ListaVehiculos = []


    def agregarVehiculo(self,gestorRutas,op):
                        

        
        if op == '1':
            print("Ingresando Automovil...")
        elif op == '2':
            print("Ingresando Camion...")
            

        matricula = str(input("Matricula : "))
        modelo = str(input("Modelo : "))
        costoKM = float(input("CostoKM : "))
        cantDiasAlquiler = int(input("CantDiasAlquiler : "))

        if op == '1':

            cantPasajerosMax = int(input("CantPasajerosMax : "))
            cantPasajerosReal = int(input("CantPasajerosReal : "))
            
            obj = Automovil(matricula,modelo,costoKM,cantDiasAlquiler,cantPasajerosMax,cantPasajerosReal)
            self.__ListaVehiculos.append(obj)
        elif op == '2':
            
            capacidadMaxCarga = float(input("capacidadMaxCarga : "))
            cantRealTransp = float(input("cantRealTransp : "))

            obj = Camion(matricula,modelo,costoKM,cantDiasAlquiler,capacidadMaxCarga,cantRealTransp)

            print("Seleccione las Ruta que desee Recorrer con el Camion recien Creado :")
            
            if type(gestorRutas) == GestorRutas:
                gestorRutas.MostrarRutas()
                codigo = str(input("Ingrese el codigo de la ruta:   / Ingrese 0 (cero) para terminar de ingresar  : "))
                
                while codigo != '0':

                    gestorRutas.MostrarRutas()
                
                    try:
                        
                        ruta = gestorRutas.BuscarRutaPorCodigo(codigo)
                    except IndexError:
                        print("ERROR - La Ruta NO SE HA ENCONTRADO")
                    except IOError:
                        print("ERROR - La Ruta YA HA SIDO ASIGNADA")
                    else:
                        if type(obj) == Camion:
                            if type(ruta) == Ruta:
                                #ruta.setRutaOcupada()
                                pass
                            obj.agregarRuta(ruta)
                            print("Cantidad de Rutas Actuales del Camion : ",obj.getCantRutas())
                    

                    codigo = str(input("Ingrese el codigo de la ruta:   / Ingrese 0 (cero) para terminar de ingresar : "))
                
                print("Cantidad de Rutas Actuales del Camion - Despues de la carga : ",obj.getCantRutas())
                self.__ListaVehiculos.append(obj)

    def MostrarVehiculos(self):
        for i in range(len(self.__ListaVehiculos)):
            print(self.__ListaVehiculos[i])

    def BuscarVehiculoPorMatricula(self,matricula):
        i = 0
        while i < len(self.__ListaVehiculos) and matricula != self.__ListaVehiculos[i].getMatricula():
            i = i + 1
        if i < len(self.__ListaVehiculos):
            print(self.__ListaVehiculos[i])
        else:
            raise Exception
        
    def IndicarInfo_Y_AlquilerTODOS(self):
        for i in range(len(self.__ListaVehiculos)):
            self.__ListaVehiculos[i].IndicarInfo_Y_Alquiler()
