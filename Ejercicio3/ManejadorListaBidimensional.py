from Registro import Registro
import csv
import os
import time

class ManejadorLista:
    __listaRegistros = []



    def inicializar(self):
        self.__listaRegistros = [[]]
        objectoRegistro = Registro()



    def __init__(self):
        self.__listaRegistros = []
        ObjetoRegistro = Registro()
        for i in range(2):
            listaInside = []
            self.__listaRegistros.append(listaInside)
            for j in range(24):
                listaInside.append(ObjetoRegistro)
            


    def MostrarTODO(self):
        for i in range(2):
            print("\n")
            print("dia : ",i+1)
            print("[Temperatura] [Humedad] [PresionAtmosférica]")

            for j in range(24):
                print(self.__listaRegistros[i][j])

    def MostrarPorDia(self,dia):
        print("Dia : ",dia)
        if type(dia) == int:
            if dia < 1 or dia > len(self.__listaRegistros):
                print("Ingreso de día ERRONEO (dia en el que no se registro ninguna variable metereologica o bien dia fuera del mes)")
            else:
                print("[Hora] [Temperatura] [Humedad] [PresionAtmosférica]")
                for hora in range(len(self.__listaRegistros[dia-1])):
                    print("{:5} {}".format(hora,self.__listaRegistros[dia-1][hora]))
        else: print("ERROR - El 'dia' ingresado no es un numero valido (entero)")

    def retornaListaBidimensional(self):
        return self.__listaRegistros

    def IngresoArchivo(self):
        borrarPantalla = lambda : os.system('cls')
        #listaTemperaturas = []
        Arcsv = "Temperaturas.csv"
        archivo = open(Arcsv)
        reader = csv.reader(archivo,delimiter = ';')
        encabezado = next(reader)
        print("Encabezao :\n{}".format(encabezado))
        for fila in reader:
            #print(fila)
            dia = int(fila[0])
            hora = int(fila[1])
            temperatura = float(fila[2])
            #print("temperatura : ",temperatura,type(temperatura))
            humedad = int(fila[3])
            #print("humedad : ",humedad,type(humedad))
            presion = float(fila[4])
            #print("presion : ",presion,type(presion))
            RegistroTemporal = Registro(temperatura,humedad,presion)
            print("Ingresando objeto Registro a la lista de listas : ",RegistroTemporal)
            #time.sleep(0.00001)
            #borrarPantalla()
            self.__listaRegistros[dia-1][hora] = (RegistroTemporal)
            #listaTemperaturas.append(temperatura)
        archivo.close()
        print("\nIngreso de DATOS del Archivo : [ '{}' ]  ... Finalizado".format(Arcsv))
        #return listaTemperaturas



    def MostrarLongLista(self):
        print("longitud lista : ",len(self.__listaRegistros))

    def mostrarElemento(self,dia,hora):
        print("Elemento mostrado : ",self.__listaRegistros[dia-1][hora])

    def MayorTemperatura(self):
        max = self.__listaRegistros[0][0].retornaTemperatura()
        indice = 0
        diahora = []
        diahora.append(0)
        diahora.append(0)
        for i in range(len(self.__listaRegistros)):
            for j in range(len(self.__listaRegistros[i])):
                if self.__listaRegistros[i][j].retornaTemperatura() > max:
                    max = self.__listaRegistros[i][j].retornaTemperatura()
                    indice = self.__listaRegistros[i][j]
                    diahora[0] = i +1
                    diahora[1] = j
        print("En el dia {} y hora {}".format(diahora[0],diahora[1]))
        print("La mayor Temperatura Max = {} y  con su indice mostramos el objeto Registro : \n{}".format(max,indice))



    def MenorTemperatura(self):
        min = self.__listaRegistros[0][0].retornaTemperatura()
        indice = 0
        diahora = []
        diahora.append(0)
        diahora.append(0)
        for i in range(len(self.__listaRegistros)):
            for j in range(len(self.__listaRegistros[i])):
                if self.__listaRegistros[i][j].retornaTemperatura() < min:
                    min = self.__listaRegistros[i][j].retornaTemperatura()
                    indice = self.__listaRegistros[i][j]
                    diahora[0] = i +1
                    diahora[1] = j
        print("En el dia {} y hora {}".format(diahora[0],diahora[1]))
        print("La Menor Temperatura Min = {} y con su indice mostramos el objeto Registro : \n{}".format(min,indice))

    def MayorHumedad(self):
        max = self.__listaRegistros[0][0].retornaHumedad()
        indice = 0
        diahora = []
        diahora.append(0)
        diahora.append(0)
        for i in range(len(self.__listaRegistros)):
            for j in range(len(self.__listaRegistros[i])):
                if self.__listaRegistros[i][j].retornaHumedad() > max:
                    max = self.__listaRegistros[i][j].retornaHumedad()
                    indice = self.__listaRegistros[i][j]
                    diahora[0] = i +1
                    diahora[1] = j
        print("En el dia {} y hora {}".format(diahora[0],diahora[1]))
        print("La mayor Humedad Max = {} y  con su indice mostramos el objeto Registro : \n{}".format(max,indice))


    def MenorHumedad(self):
        min = self.__listaRegistros[0][0].retornaHumedad()
        indice = 0
        diahora = []
        diahora.append(0)
        diahora.append(0)
        for i in range(len(self.__listaRegistros)):
            for j in range(len(self.__listaRegistros[i])):
                if self.__listaRegistros[i][j].retornaHumedad() < min:
                    min = self.__listaRegistros[i][j].retornaHumedad()
                    indice = self.__listaRegistros[i][j]
                    diahora[0] = i +1
                    diahora[1] = j  
        print("En el dia {} y hora {}".format(diahora[0],diahora[1]))                 
        print("La Menor Humedad Min = {} y con su indice mostramos el objeto Registro : \n{}".format(min,indice))

    def MayorPresion(self):
        max = self.__listaRegistros[0][0].retornaPresion()
        indice = 0
        diahora = []
        diahora.append(0)
        diahora.append(0)
        for i in range(len(self.__listaRegistros)):
            for j in range(len(self.__listaRegistros[i])):
                if self.__listaRegistros[i][j].retornaPresion() > max:
                    max = self.__listaRegistros[i][j].retornaPresion()
                    indice = self.__listaRegistros[i][j]
                    diahora[0] = i +1
                    diahora[1] = j
        print("En el dia {} y hora {}".format(diahora[0],diahora[1]))
        print("La mayor Presion Max = {} y  con su indice mostramos el objeto Registro : \n{}".format(max,indice))


    def MenorPresion(self):
        min = self.__listaRegistros[0][0].retornaPresion()
        indice = 0
        diahora = []
        diahora.append(0)
        diahora.append(0)
        for i in range(len(self.__listaRegistros)):
            for j in range(len(self.__listaRegistros[i])):
                if self.__listaRegistros[i][j].retornaPresion() < min:
                    min = self.__listaRegistros[i][j].retornaPresion()
                    indice = self.__listaRegistros[i][j]
                    diahora[0] = i +1
                    diahora[1] = j
        print("En el dia {} y hora {}".format(diahora[0],diahora[1]))
        print("La Menor Presion Min = {} y con su indice mostramos el objeto Registro : \n{}".format(min,indice))


    def TemperaturaPromedioMensual(self):
        promedio = 0.0
        acumulador = 0.0
        contador = 0
        for i in range(len(self.__listaRegistros)):
            for j in range(len(self.__listaRegistros[i])):
                acumulador += self.__listaRegistros[i][j].retornaTemperatura()
                contador = contador + 1
        promedio = acumulador / contador
        print("-<>-Calculo Promedio de Temperaturas : ...")
        print("(1) Suma de todas las Temperaturas = {}".format(acumulador))
        print("(2) El promedio Mensual de Temperaturas es : {}".format(promedio))


            


