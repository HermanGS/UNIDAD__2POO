from classMedio import Medios
import csv
from classPrograma import Programa

class Radio(Medios):
    __frecuencia: str
    __programacion: object
    __listaPrograma: list


    def __str__(self) -> str:
        return super().__str__() + str(self.__frecuencia) +"\nProgramas :\n"+ self.ProgramasString()

    
    def ProgramasString(self):
        c = ""
        for i in range(len(self.__listaPrograma)):
            c = c +" "+ str(self.__listaPrograma[i]) + " \n"
        return c
    
    def __del__(self):
        del self.__listaPrograma

    def getFrecuencia(self):
        return self.__frecuencia    
    
    
    def __init__(self,nombre, audiencia, frecuencia):
        super().__init__(nombre, audiencia)
        self.__frecuencia = frecuencia
        self.__listaPrograma = []

        archivo = open("Programas.csv")
        reader=csv.reader(archivo, delimiter = ",")
        for fila in reader:
            frecuencia = str(fila[0])
            if self.__frecuencia == frecuencia:
                nombre=str(fila[1])
                hrI = str(fila[2])
                hrF = str(fila[3])
                obj=Programa(hrI,hrF,nombre)
                if obj.getValido()  == True:
                    self.__listaPrograma.append(obj)
                
    def MostrarHorariosProgramas(self):
        for i in range(len(self.__listaPrograma)):
            print(self.__listaPrograma[i].getHorarioInicio())
            

    def CalculoDivisorDelIndice(self):
        cantProgramas = 1
        if len(self.__listaPrograma) >= 1:
            cantProgramas = len(self.__listaPrograma)
        return cantProgramas