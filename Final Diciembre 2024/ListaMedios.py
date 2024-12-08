from classRadio import Radio
from classPrensa import Prensa
import csv

class ListaMedios:
    __lista: list

    def __init__(self):
        self.__lista = []

    def leerLista(self):
        archivo = open("Medios.csv")

        reader=csv.reader(archivo, delimiter=",")
        for fila in reader:
            nombre = str(fila[1])
            audiencia=int(fila[2])
            if fila[0] == "R":
                frecuencia =str(fila[3])
                obj = Radio(nombre , audiencia, frecuencia)
            elif fila[0]=="P":
                periodicidad =str(fila[3])
                cantSecc = int(fila[4])
                obj = Prensa(nombre, audiencia, periodicidad, cantSecc)

            self.__lista.append(obj)

        print("cantidad de elementos de la lista :",{len(self.__lista)})
        archivo.close()
    
    def agregarP(self,nombre, audiencia,cantSecc, periodicidad):
        obj = Prensa(nombre,audiencia,cantSecc,periodicidad)
        self.__lista.append(obj)
        
    def agregarR(self,nombre, audiencia, frecuencia):
        obj = Radio(nombre,audiencia,frecuencia)
        self.__lista.append(obj)
        
    def saberRadio(self,nombre):
        print("nombre parametro : ",{nombre})

        for i in(self.__lista):
            print("en el for")

            if isinstance(i,Radio):
                print("en el if istance")
                print("nombre parametro : ",{nombre})
                print("nombre dentro de la clase radio : ",{i.getNombre()})
                if nombre == i.getNombre():
                    
                    print("Radio encontrada...")
                    print("Nombre de la Radio encontrada : ",i.getNombre())
                    print("Frecuencia de la Radio : ",i.getFrecuencia())
                    print("Horarios de los programas : \n",i.MostrarHorariosProgramas())

                else:
                    raise Exception

    def DatosRadio(self,nombre):
        i = 0
        while i < len(self.__lista) and nombre != self.__lista[i].getNombre():
            i += 1

        if i < len(self.__lista):
                if isinstance(self.__lista[i],Radio):
                    print("Radio encontrada...")
                    print("Nombre de la Radio encontrada : ",self.__lista[i].getNombre())
                    print("Frecuencia de la Radio : ",self.__lista[i].getFrecuencia())
                    print("Horarios de los programas : \n")
                    self.__lista[i].MostrarHorariosProgramas()
        else:
            raise Exception

    def mostrar(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])

            
        

    def IndicarDatosDelMedioeIndice(self):
        for i in range(len(self.__lista)):
            print("\n\nMedio : ")
            print(self.__lista[i])
            print("Indice :")
            print(self.__lista[i].CalculoIndice())

