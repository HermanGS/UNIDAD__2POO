from claseRuta import Ruta
import csv
class GestorRutas:
    __ListaRutas: list


    def __init__(self):
        self.__ListaRutas = []


    def ingresarCSV(self):
        archivo = open('Rutas.csv')
        reader = csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            codigo = int(fila[0])
            destino = str(fila[1])

            distanciaTemporal = str(fila[2])
            distanciaTotalKM = distanciaTemporal.replace(',','.')
            distanciaTotalKM = float(distanciaTotalKM)

            if str(fila[3]) == 'FALSO':    
                rutaAsignada = False
            obj = Ruta(codigo,destino,distanciaTotalKM,rutaAsignada)
            self.__ListaRutas.append(obj)
        archivo.close()

    def MostrarRutas(self):
        print("Rutas cargadas en el Gestor De Rutas :")
        for i in range(len(self.__ListaRutas)):
            print(self.__ListaRutas[i])


    def BuscarRutaPorCodigo(self,codigo):
        codigo = int(codigo)
        i = 0
        while i<len(self.__ListaRutas) and self.__ListaRutas[i] != codigo:  
            i = i + 1
        if i<len(self.__ListaRutas):
            print("Se encontro la ruta buscada...")
            if self.__ListaRutas[i].getRutaAsignada() == True: # Se encontro pero ya esta asignada
                raise IOError
            else:               # Se encontro y no esta Asignada (disponible)
                self.__ListaRutas[i].setRutaOcupada()
                return self.__ListaRutas[i]
        elif i>len(self.__ListaRutas): # No se encontro
            raise IndexError 
