"""CONTEXTO
El Consorcio SIU, encargado del desarrollo de las soluciones informáticas que utilizan las
instituciones universitarias del país lo contrata a usted para el desarrollo de un módulo que
procese los archivos: ‘alumnos.csv’ y ‘materiasAprobadas.csv’.
El archivo ‘alumnos.csv’ almacena la información de los alumnos inscriptos en las carreras de la
universidad. La estructura del mismo es la siguiente: dni, apellido, nombre, carrera, año de la
carrera que cursa.

El archivo ‘materiasAprobadas.csv’ almacena información de las materias que los alumnos
inscriptos en una carrera, han aprobado en los últimos tres meses, por examen, equivalencia o
promoción. La estructura de dicho archivo es la siguiente: dni, nombre de materia, fecha, nota,
aprobación (‘E’ – Examen, ‘X’ – Equivalencia, ‘P’ – Promoción).

Los archivos no presentan ningún orden en particular.
El módulo que se le solicita debe permitir.
1) Cargar los datos de los alumnos en un Manejador de Alumnos, implementado usando un
arreglo Numpy.

2) Cargar los datos de las materias aprobadas en un Manejador de Materias, implementado
usando una lista Python.

3) A través de un menú de opciones llevar a cabo las siguientes funcionalidades:

a. Leer por teclado el número de dni de un alumno, e informar su promedio con
aplazos y sin aplazos.
b. Leer por teclado el nombre de una materia, e informar los estudiantes que la
aprobaron en forma promocional, con nota mayor o igual que 7. El informe debe
tener el siguiente formato:
DNI Apellido y nombre Fecha Nota Año que cursa
xxxxxxx xxxxxxxxxxxxxxxxxxx xx/xx/xxxx xx.xx x
xxxxxxx xxxxxxxxxxxxxxxxxxx xx/xx/xxxx xx.xx x
c. Obtener un listado de alumnos ordenado: por el año que cursan y alfabéticamente
por apellido y nombre (ambos de menor a mayor).
Regla de negocio: el analista le solicita que para resolver esta opción
sobrecargue el operador (<) en la clase que corresponda"""

import numpy as np
from Alumno import Alumno
import csv

class ManejadorAlumnos:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    __ArregloAlumnos = None
    
    def __init__(self,dimension,incremento):
        self.__ArregloAlumnos = np.empty(dimension,dtype = Alumno)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
        
    def AgregarAlumno(self,alumno):
        if self.__cantidad == self.__dimension:
            self.__dimension = self.__dimension + self.__incremento
            self.__ArregloAlumnos.resize(self.__dimension, refcheck=False)
        self.__ArregloAlumnos[self.__cantidad] = alumno
        self.__cantidad = self.__cantidad + 1
        
    def MostrarAlumnos(self):
        for i in range(self.__cantidad):
            print(self.__ArregloAlumnos[i])
        
    def retornaArregloAlumnos(self):
        return self.__ArregloAlumnos    
    
    
    def testIngreso(self):
        Alumno1 = Alumno(44,"po","lla","LCC",5)
        self.AgregarAlumno(Alumno1)
        self.MostrarAlumnos()
        
    def IngresoAlumnosArchivoCSV(self):
        nombreArhcivo = 'alumnos.csv'
        archivo = open(nombreArhcivo)
        reader = csv.reader(archivo,delimiter = ";")
        #encabezado = next(reader)
        for fila in reader:
            dni = str(fila[0])
            apellido = str(fila[1])
            nombre = str(fila[2])
            carrera = str(fila[3])
            añocarrera = int(fila[4])
            AlumnoT = Alumno(dni,apellido,nombre,carrera,añocarrera)
            self.AgregarAlumno(AlumnoT)
            print("Agregando Alumno : {} , al Arreglo".format(AlumnoT))
        print("... Ingreso de Alumnos finalizado ...")
        archivo.close()
        
    def BusquedaAlumnoDni(self,dni):
        i = 0
        while i < self.__cantidad and self.__ArregloAlumnos[i].retornaDni() != dni:
            i = i + 1
        if i < self.__cantidad:
            return self.__ArregloAlumnos[i]
        else: print("No se ha encontrado el Alumno buscado")
    """        
    c. Obtener un listado de alumnos ordenado: por el año que cursan y alfabéticamente
    por apellido y nombre (ambos de menor a mayor).
    Regla de negocio: el analista le solicita que para resolver esta opción
    sobrecargue el operador (<) en la clase que corresponda"""

    def ListadoOrdenadoNombreyApellido(self):
        self.__ArregloAlumnos.sort()
        self.MostrarAlumnos()
        