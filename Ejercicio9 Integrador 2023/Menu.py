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

class Menu:
    
    
    def op1(self,ManejadorMaterias):
        print("Entro al 1")
        
        ManejadorMaterias.PromedioAplazoSinAplazoPorDni()
        #listaMaterias = ManejadorMaterias.retornaListaMaterias()
        #ManejadorAlumnos.PromedioAplazoSinAplazoPorDni(listaMaterias)
        
    def op2(self,ManejadorAlumnos,ManejadorMaterias):
        print("Entro al 2")
        #ArregloAlumnos = ManejadorAlumnos.retornaArregloAlumnos()
        
        ManejadorMaterias.PromocionalesPorNombreDeMateria(ManejadorAlumnos)
        
        
        
    def op3(self,ManejadorAlumnos,ManejadorMaterias):
        print("Entro al 3")
        ManejadorAlumnos.ListadoOrdenadoNombreyApellido()
        
        
    def ElegirOP(self,ManejadorAlumnos,ManejadorMaterias):
        op = -1
        while op != 0:
            print("\n\n<--------------------------------------------------------------------------------------------->")
            print("Elija '1', '2' o '3' segun desee")
            print("1. Leer por teclado el número de dni de un alumno, e informar su promedio con aplazos y sin aplazos.\n2. Leer por teclado el nombre de una materia, e informar los estudiantes que la aprobaron en forma promocional, con nota mayor o igual que 7.\n3. Obtener un listado de alumnos ordenado: por el año que cursan y alfabéticamente por apellido y nombre (ambos de menor a mayor).")
            print("Ingrese 0 (cero) para terminar \n")
            
            op = input("Respuesta : ")
            while op.isdigit() != True:
                print("ERROR - Opcion Incorrecta - Vuelva A ingresar la OPCION")
                print("Ingrese 0 (cero) para terminar \n")
                op = input("Respuesta : ")
            op = int(op)
            while op < 0 or op > 3:
                print("ERROR - Opcion Incorrecta (Entre 0 y 3)- Vuelva A ingresar la OPCION")
                print("Ingrese 0 (cero) para terminar \n")
                op = input("Respuesta : ")
                
            if op == 1:
                self.op1(ManejadorMaterias)
            elif op == 2:
                self.op2(ManejadorAlumnos,ManejadorMaterias)
            elif op == 3:
                self.op3(ManejadorAlumnos,ManejadorMaterias)
            else : print("<---- Saliendo del Programa ---->")
            
        