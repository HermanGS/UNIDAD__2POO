import numpy as np
from alumnos import alumnos
import csv

class ManejadorAlumnos:

    def __init__(self):
        self.__ArregloAlumnos = np.empty(0,dtype=alumnos)

    def IngresoArchivo(self):
        archivo = open('alumnos.csv')
        reader = csv.reader(archivo,delimiter = ';')

        for fila in reader:

            dni = int(fila[0])
            apellido = str(fila[1])
            nombre = str(fila[2])
            carrera = str(fila[3])
            anio = int(fila[4])

            ObjetoAlumno = alumnos(dni,apellido,nombre,carrera,anio)
            self.__ArregloAlumnos = np.append(self.__ArregloAlumnos,ObjetoAlumno)
        archivo.close()

    def MostrarArregloAlumnos(self):
        for i in self.__ArregloAlumnos:
            print(i)

    def RetornaArreglo(self):
        return self.__ArregloAlumnos


    def Ordema(self):
        self.__ArregloAlumnos.sort()

    def ObtenerDNI(self):
        self.__ArregloAlumnos