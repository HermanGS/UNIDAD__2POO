import numpy as np
from Persona import Persona



class ManejadorHombres:
    __cantidad = 0
    __dimesion = 0
    __incremento = 5
    __ArregloHombres : None

    def __init__(self,dimension,incremento) -> None:
        self.__ArregloHombres = np.empty(dimension,dtype = Persona)
        self.__cantidad = 0
        self.__dimesion = dimension
        self.__incremento = incremento
    def AgregarPersona(self,Persona):
        print("cantidad : ",self.__cantidad,"dimension : ",self.__dimesion,"incremento : ",self.__incremento)
        if self.__cantidad == self.__dimesion:
            self.__dimesion = self.__dimesion + self.__incremento
            self.__ArregloHombres.resize(self.__dimesion)
        self.__ArregloHombres[self.__cantidad] = Persona
        self.__cantidad += 1
        print("cantidad : ",self.__cantidad,"dimension : ",self.__dimesion,"incremento : ",self.__incremento)
    
    def TestPersonas(self):
        Persona1 = Persona(100,'Felice','Joeann','.@yopmail.com','peleador de fuego')
        Persona2 = Persona(100,'Felice','Joeann','.@yopmail.com','peleador de fuego')
        Persona3 = Persona(100,'Felice','Joeann','.@yopmail.com','peleador de fuego')
        Persona4 = Persona(100,'Felice','Joeann','.@yopmail.com','peleador de fuego')
        Persona5 = Persona(100,'Felice','Joeann','.@yopmail.com','peleador de fuego')
        self.AgregarPersona(Persona1)
        self.AgregarPersona(Persona2)
        self.AgregarPersona(Persona3)
        self.AgregarPersona(Persona4)
        self.AgregarPersona(Persona5)

    def mostrarPersonas(self):          # Como se tendría que hacer , solo muestra lo ocupado
        for i in range(self.__cantidad):
            print(self.__ArregloHombres[i])

    def mostrarPersonas2(self):  # Un mostrar que muestra TODO , aunque no haya espacio ocupado
        for i in self.__ArregloHombres:
            print(i)