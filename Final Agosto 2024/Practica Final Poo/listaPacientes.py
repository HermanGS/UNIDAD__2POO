from Nodo import Nodo
from clasePaciente import Paciente
from clasePacienteH import pacienteH
from clasePacienteA import pacienteA
import csv

class listaPacientes:
    __cabeza:Nodo
    __cant: int

    def __init__(self):
        self.__cabeza = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0


    def insertarFinal(self):
        archivo = open("pacientes.csv")
        reader = csv.reader(archivo, delimiter = ";")

        saltar = True

        for fila in reader:
            obj = None
            if saltar == True:
                saltar = False
            else:
                tipo = str(fila[0])
                nombre = str(fila[1])
                apellido = str(fila[2])
                email = str(fila[3])
                nroTel = str(fila[4])
                if tipo == 'H':
                    numHab = str(fila[5])
                    fechaI = str(fila[6])
                    diagnostico = str(fila[7])
                    cantDias = str(fila[8])
                    importe = str(fila[9])
                    obj = pacienteH(nombre, apellido, email, nroTel, numHab, fechaI, diagnostico, cantDias, importe )
                elif tipo == "O":
                    historial = str(fila[5])
                    alergias = str(fila[6])
                    obraSocial = str(fila[7])
                    obj = pacienteA(nombre, apellido, email, nroTel, historial, alergias, obraSocial)
            
            if obj != None:
                nuevo= Nodo(obj)
                if self.vacia():
                    nuevo.setSig(self.__cabeza)
                    self.__cabeza = nuevo
                    self.__cant += 1
                else:
                    aux = self.__cabeza        
                    ant = aux
                    while (aux != None):
                        ant = aux
                        aux = aux.getSig()
                    ant.setSig(nuevo)
                    nuevo.setSig(aux)
                    self.__cant += 1
            
                
    def mostrar(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getDato())
            aux = aux.getSig()


                    

