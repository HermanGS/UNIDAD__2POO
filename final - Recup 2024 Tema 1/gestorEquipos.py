import csv
from claseMaquinariaPesada import MaquinariaPesada
from claseHerramientaElectrica import HerramientaElectrica
from claseNodo import Nodo
class gestorEquipos:
    __cabeza : None

    def __init__(self):
        self.__cabeza = None
        self.__cantidad = 0

    def vacia(self):
        return self.__cantidad == 0

    def IngresarEquipos(self):
        archivo = open('equipos.csv')
        reader = csv.reader(archivo,delimiter=';')
        
        saltarPrimeraFila = True
        for fila in reader:
            
            if saltarPrimeraFila:
                saltarPrimeraFila = False
            
            else:
                #Llenado del objeto
                Nuevo = Nodo()
                tipoEquipo = str(fila[0])
                marca = str(fila[1])
                modelo = str(fila[2])
                anio = str(fila[3])
                combustible = str(fila[4])
                potencia = str(fila[5])
                capacidadCarga =str(fila[6])
                alquilerdiario = float(fila[7])
                cantDiasAlquiler = int(fila[8])
                if tipoEquipo == 'M':
                    tipoMaquinaria = str(fila[9])
                    peso = int(fila[10])
                    obj = MaquinariaPesada(marca,modelo,anio,combustible,potencia,capacidadCarga,alquilerdiario,cantDiasAlquiler,tipoMaquinaria,peso)
                elif tipoEquipo == 'E':
                    tipoHerramienta = str(fila[9])
                    obj = HerramientaElectrica(marca,modelo,anio,combustible,potencia,capacidadCarga,alquilerdiario,cantDiasAlquiler,tipoHerramienta)


                #Meterlo en la Lista definida por el Programador 
                if self.vacia():
                    Nuevo.setDato(obj)
                    Nuevo.setSig(self.__cabeza)
                    self.__cabeza = Nuevo
                    self.__cantidad +=1
                
                else:
                    
                    Nuevo.setDato(obj)
                    aux = self.__cabeza
                    ant = aux

                    while aux != None:
                        ant = aux
                        aux = aux.getSig()
                    
                    
                    ant.setSig(Nuevo)
                    Nuevo.setSig(aux)
                    self.__cantidad +=1
                    
                    
    def Mostrar(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getDato())
            aux = aux.getSig()

    def LecturaPosicion(self,pos):
        if pos < 0 or pos > self.__cantidad:
            raise IndexError

        else:
            i = 0
            aux = self.__cabeza

            while aux != None and i<pos:
                aux = aux.getSig()
                i = i + 1
            
            if aux != None:
                if isinstance(aux.getDato(),MaquinariaPesada):
                    print("El equipo es una maquinara Pesada")
                elif isinstance(aux.getDato(),HerramientaElectrica):
                    print("El equipo es una Herramienta Electrica")
            else:
                raise IndexError
            
    def HerramientasElectricasPorAnio(self,anio):
        aux = self.__cabeza
        cantHerramientas = 0
        while aux != None:
            if aux.getDato().getAnioFabricacion() == anio:
                if isinstance(aux.getDato(),HerramientaElectrica):
                    cantHerramientas = cantHerramientas + 1
            aux = aux.getSig()
        return cantHerramientas
    
    def MaquinariasConCapacidadMenorA(self,capacidad):
        aux = self.__cabeza
        cantMaquinarias = 0
        while aux != None:
            if isinstance(aux.getDato(),MaquinariaPesada):
                if int(aux.getDato().getPeso()) <= capacidad:
                    cantMaquinarias = cantMaquinarias + 1 + 1

            aux = aux.getSig()
        return cantMaquinarias
    
    def MostrarDatosGestor(self):
        print("Mostrando Datos: ")
        aux = self.__cabeza
        while aux != None:
            
            print(aux.getDato().mostrarDatosYtarifa())
            aux = aux.getSig()







