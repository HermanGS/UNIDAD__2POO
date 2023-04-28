from doctest import REPORTING_FLAGS
from ManejadorAlumnos import ManejadorAlumnos
from ManejadorMaterias import ManejadorMaterias



class Menu:

    def __init__(self):
        pass

    
    def Menuopciones(self):
        print("\n1.Funcion 1\n2.Funcion 2\n3.Funcion 3\n4.Funcion 4\n5.Funcion 5")

    def opcion1(self,ManejadorAlumnos,ManejadorMaterias):
        dni = int(input("Ingrese el dni del alumno para calcular los 2 Promedios"))
        ManejadorMaterias.PorDNIpromedio(dni)
    def opcion2(self,ManejadorAlumnos,ManejadorMaterias):
        MateriaP = str(input("Ingrese el nombre de la Materia para Saber los Alumnos que la promocionaron"))
        ManejadorMaterias.MateriaPromocionalFormato(ManejadorAlumnos,MateriaP)
    def opcion3(self,ManejadorAlumnos,ManejadorMaterias):
        ManejadorAlumnos.Ordema()
        ManejadorAlumnos.MostrarArregloAlumnos()
    def opcion4(self,ManejadorAlumnos,ManejadorMaterias):
        print("Alumnos Sin Rendir:")
        ManejadorMaterias.AlumnosSinRendir(ManejadorAlumnos)
        print("\n")
        ManejadorAlumnos.MostrarArregloAlumnos()
    def opcion5(self):
        print("Fin Programa")

    def ChoseOP(self,op,ManejadorAlumnos,ManejadorMaterias):
        if op == 1:
            self.opcion1(ManejadorAlumnos,ManejadorMaterias)
        if op == 2:
            self.opcion2(ManejadorAlumnos,ManejadorMaterias)
        if op == 3:
            self.opcion3(ManejadorAlumnos,ManejadorMaterias)
        if op == 4:
            self.opcion4(ManejadorAlumnos,ManejadorMaterias)
        if op == 5:
            self.opcion5()

    