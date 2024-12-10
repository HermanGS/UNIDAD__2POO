from claseEvento import Evento
from clasePresentacion import Presentacion
import csv

from datetime import datetime
hora_str = "15:00"
hora_datetime = datetime.strptime(hora_str, "%H:%M")



class Concierto(Evento):
    __generoMusical : str
    __duracionHS : str
    __listaPresentaciones: list


    

    def __init__(self,titulo,numeroAsistentes,genero,duracion):
        super().__init__(titulo,numeroAsistentes)
        self.__generoMusical = genero
        self.__duracionHS = duracion
        self.__listaPresentaciones = []

        archivo = open('Presentaciones.csv')
        reader = csv.reader(archivo,delimiter=',')

        saltarEncabezado  = True

        for fila in reader:

            if saltarEncabezado == True:
                saltarEncabezado = False

            else:
                titulo = str(fila[0])
                
                if titulo == self.getTitulo():    
                    nombreBanda = str(fila[1])
                    horaInicio = str(fila[2])
                    horaFin = str(fila[3])
                    try:
                        obj = Presentacion(nombreBanda,horaInicio,horaFin)
                    except ValueError:
                        print("Horario Incorrecto , No se guardó la Presentacion de ",nombreBanda)
                    
                    
                    self.__listaPresentaciones.append(obj)

    def getGeneroMusical(self):
        return self.__generoMusical


    #def __str__(self):
        #return super().__str__() + f'{self.__generoMusical} , {self.__duracionHS} {self.mostrarPresentaciones()}'
    
    def __str__(self):
        return super().__str__()

    def mostrarPresentaciones(self):
        c = "\nPresentaciones :  "
        for i in range(len(self.__listaPresentaciones)):
            c = c + str(self.__listaPresentaciones[i]) +" "
        return c


    #def __del__(self):
        #print("Eliminando Concierto y sus Presentaciones")
        #del(self.__listaPresentaciones)


    def DivisorIndice(self):
        divisor = 1 # me aseguro de que si hay algun error solo se divida por 1
        if len(self.__listaPresentaciones) >= 1:
            divisor = len(self.__listaPresentaciones)
        return divisor
    

    #b)

    def BuscarNombreBanda(self,NombreBanda):
        encontrado = False
        i = 0
        while i<len(self.__listaPresentaciones) and NombreBanda != self.__listaPresentaciones[i].getNombreBanda():
            i = i + 1
        if i<len(self.__listaPresentaciones):
            print("Banda Encontrada")
            print("Nombre de la Banda :",self.__listaPresentaciones[i].getNombreBanda())
            print("Hora de Inicio de la Presentacion : ",self.__listaPresentaciones[i].getHoraInicio())
            encontrado = True
        
        return encontrado

