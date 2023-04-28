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

from MateriaAprobada import MateriaAprobada
import csv 
import numpy as np
from Alumno import Alumno

class ManejadorMateriasAprobadas:
    __ListaMaterias : list
    
    def __init__(self):
        self.__ListaMaterias = []
        
        
    def mostrarMaterias(self):
        for i in range(len(self.__ListaMaterias)):
            print(self.__ListaMaterias[i])
            
    def retornaListaMaterias(self):
        return self.__ListaMaterias
            
    def testIngresoMateria(self):
        MateriaAprobada1 = MateriaAprobada(88,"POO","27/04/23",2,"E")
        self.__ListaMaterias.append(MateriaAprobada1)
        self.mostrarMaterias()
        
    def IngresoMateriasAprobadasArchivoCSV(self):
        nombreArchivo = 'materiasAprobadas.csv'
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo,delimiter = ";")
        #encabezado = next(reader)
        for fila in reader:
            dni = str(fila[0])
            nombreMateria = str(fila[1])
            fecha = str(fila[2])
            nota = int(fila[3])
            aprobacion = str(fila[4])
            MateriaAprobadaT = MateriaAprobada(dni,nombreMateria,fecha,nota,aprobacion)
            self.__ListaMaterias.append(MateriaAprobadaT)
            print("Agregando MateriaAproada  :{} a la Lista".format(MateriaAprobadaT))
        print("... Ingreso de Materias Aprobadas Finalizado ...")
        archivo.close()
        
    def PromedioAplazoSinAplazoPorDni(self):
        dni = input("Ingrese el DNI del Alumno para Promedio con y sin Aplazos")
        print(type(dni))
        sumaA = 0
        contadorA = 0
        sumaSA = 0
        contadorSA = 0
        #print("dni buscado indexado : {}, dni teclado : {}".format(self.__ListaMaterias[0].retornaDni(),dni))
        for i in range(len(self.__ListaMaterias)):
            #print("dni buscado indexado : {}, dni teclado : {}".format(self.__ListaMaterias[i].retornaDni(),dni))
            if self.__ListaMaterias[i].retornaDni() == dni:
                sumaA = sumaA + self.__ListaMaterias[i].retornaNota()
                contadorA += 1
                #print("ContadorA : ",contadorA)
                if self.__ListaMaterias[i].retornaNota() >= 4:
                    sumaSA = sumaSA + self.__ListaMaterias[i].retornaNota()
                    contadorSA += 1
                    #print("ContadorSA : ",contadorSA)
        #print("ContadorA Final : ",contadorA)
        #print("ContadorSA Final : ",contadorSA)
        promA = sumaA / contadorA
        promSA = sumaSA / contadorSA
        
        print ("PROMEDIO CON APLAZOS : ",promA)
        print ("PROMEDIO SIN APLAZOS : ",promSA)
        
    """b. Leer por teclado el nombre de una materia, e informar los estudiantes que la
aprobaron en forma promocional, con nota mayor o igual que 7. El informe debe
tener el siguiente formato:
DNI Apellido y nombre Fecha Nota Año que cursa
xxxxxxx xxxxxxxxxxxxxxxxxxx xx/xx/xxxx xx.xx x
xxxxxxx xxxxxxxxxxxxxxxxxxx xx/xx/xxxx xx.xx x"""

    def PromocionalesPorNombreDeMateria(self,ManejadorAlumnos):
        nombreMateria = input("Ingrese un Nombre de Materia para averiguar la informacion de los Alumnos Promocionales : ")
        print(type(nombreMateria))
        
        for i in range(len(self.__ListaMaterias)):
            bandera = 1
            #print("Nombre de materia sin replace (" "): ",self.__ListaMaterias[i].retornaNombreMateria().lower())
            #print("Nombre de materia con replace (" "): ",self.__ListaMaterias[i].retornaNombreMateria().lower().replace(" ",""))

            #print("Entro al FOR")
            print("Nombre de materia : ",self.__ListaMaterias[i].retornaNombreMateria().lower().strip(" "),"| Nombre Materia : ",nombreMateria.lower().strip(" "))
            #print(self.__ListaMaterias[i].retornaNombreMateria().lower().strip(" ") == nombreMateria.lower().strip(" "))
            if self.__ListaMaterias[i].retornaNombreMateria().lower().strip(" ").replace(" ","") == nombreMateria.lower().strip(" ").replace(" ",""):
                if self.__ListaMaterias[i].retornaNota() >= 7:
                    bandera = 2
                    if self.__ListaMaterias[i].retornaAprobacion() == 'P':
                        bandera = 3
                        dni = self.__ListaMaterias[i].retornaDni()
                        print("dni retornado : ",dni,"y tipo : ",type(dni))
                        Resultado = ManejadorAlumnos.BusquedaAlumnoDni(dni)
                        if type(Resultado) == Alumno:
                            bandera = 4
                            print("Materias Aprobadas en forma Promocional : ")
                            print("DNI      Apellido y nombre       Fecha       Nota        Año que cursa")
                            print("{:10}{:10}{:10}{:10}{:10}{:10}".format(dni,Resultado.retornaApellido(),Resultado.retornaNombre(),self.__ListaMaterias[i].retornaFecha(),self.__ListaMaterias[i].retornaNota(),Resultado.retornaAñoCarrera()))
            """            
                        else: print("El alumno Buscado por DNI no se encontró  ; ",end="")
                    else : print("La Rendida de la Materia (No es promocional );",end="")
                else: print("Su nota FINAL es menor a 7 ;",end="")
            else: 
                print("Buscando ... (Todavía no encontrado) ")
            """
        print("<<<--------------------------->>> Resumen  Final <<<--------------------------->>>")
        if bandera == 1:
            print("[No se encontró ninguna Materia ni tampoco ningun alumno en toda la busqueda]")
        elif bandera == 2:
            print("[Se encontró la materia, con NOTA >= 7 , pero no era promocional]")
        elif bandera == 3:
            print("[Se encontró la materia, con NOTA >= 7 y siendo Promocioanl pero no se encontro el alumno]")
        elif bandera == 4:
            print("[Se encontró la materia, con NOTA >= 7 y siendo Promocioanl Con Alumno encontrado]")
        print("<<<--------------------------->>> Resumen  Final <<<--------------------------->>>")