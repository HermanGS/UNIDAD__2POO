from Nodo import Nodo
from clasePaciente import Paciente
from clasePacienteH import pacienteH
from clasePacienteA import pacienteA
import csv

class listaPacientes:
    __cabeza:Nodo
    __cant: int
    __actual:Nodo
    __tope: int
    __indice: int

    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

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
                    numHab = int(fila[5])
                    fechaI = str(fila[6])
                    diagnostico = str(fila[7])
                    cantDias = int(fila[8])
                    importe = float(fila[9])
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

    def PHneumo(self):
        cantNuemo = 0
        cantAmbu = 0
        aux = self.__cabeza
        while aux != None:
            if type(aux.getDato()) == pacienteH:
                if aux.getDato().getDiagnostico() == "Neumonia":
                    cantNuemo += 1
            else:
                cantAmbu += 1
            aux=aux.getSig()      
        print(f"Los pacientes con neumonia son: {cantNuemo}")
        print(f"Los pacientes  ambulatorios son: {cantAmbu}")

    def importeTotalPacientes(self):
        aux = self.__cabeza 
        while aux!=None:
            ##print("tipo paciente :",type(aux.getDato()))
            print(aux.getDato())
            print(aux.getDato().calcularImporte())
            aux = aux.getSig()

    def posicionHDP(self, valor):
        if valor < 0 or valor >= self.__cant:
            # Verifica si el índice está fuera de rango.
            raise IndexError
        
        aux = self.__cabeza
        y = 0  # Índice para recorrer la lista.

        while aux is not None and y < valor:
            aux = aux.getSig()
            y += 1

        # Si encuentra el nodo en la posición deseada, devuelve el dato.
        if aux is not None:
            return aux.getDato()
        else:
            raise IndexError

    def CambiarValorConsulta(self,x):
        self.__cabeza.getDato().setValorConsulta(x)

        

