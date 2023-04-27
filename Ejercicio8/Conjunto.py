"""Ejercicio 8
Sobrecarga de operadores

Defina una clase “Conjunto” que represente un conjunto matemático de números enteros.

Implemente un programa que presente un menú de opciones que permita lo siguiente:

1- La unión de dos conjuntos, para ello sobrecargue el operador binario suma (+). 
Teniendo en cuenta que la unión es un nuevo conjunto que posee los elementos de ambos conjuntos, en caso de haber elementos repetidos solo aparecen una vez en el resultado. 
Ejemplo: Sea A={1,2,3,4} y B= {3,6,9}, A+B = {1,2,3,4,6,9}

2- La diferencia de dos conjuntos, para ello sobrecargue el operador binario resta (-). 
Teniendo en cuenta que el resultado de la diferencia de conjuntos es un nuevo conjunto que posee los elementos del primer operando que no se encuentren en el segundo operando. 
Ejemplo: Sea A={1,2,3,4} y B= {3,6,9}, A-B = {1,2}

3- Verificar si dos conjuntos son iguales, para ello sobrecargue el operador “==” teniendo en cuenta que dos conjuntos se consideran iguales si tienen la misma cantidad de elementos 
y sus valores son iguales (sin importar el orden de los elementos)."""


class Conjunto:


    def __init__(self,lista = []) -> None:
        self.__Conjunto = lista
    """
    def __str__(self) -> str:
        return self.__Conjunto
    """
    def __str__(self) -> str:
        cadena = ""
        for i in range(len(self.__Conjunto)):
            cadena =  cadena + "," + str(self.__Conjunto[i])

        cadena = "{" + cadena + "}"
        return cadena

    def retornaLista(self):
        return self.__Conjunto

    def __add__(self,otro):
        listaaux = []
        for j in range(len(self.__Conjunto)):
            listaaux.append(self.__Conjunto[j])

        for i in range(len(otro.__Conjunto)):
            if otro.__Conjunto[i]  not in self.__Conjunto:
                listaaux.append(otro.__Conjunto[i])
        return Conjunto(sorted(listaaux))
    
    def __sub__(self,otro):
        listaaux = []
        for i in range(len(self.__Conjunto)):
            if self.__Conjunto[i] not in otro.__Conjunto:
                listaaux.append(self.__Conjunto[i])
        return Conjunto(sorted(listaaux))
    """   
    def __eq__2(self, __value: object) -> bool:
        bandera : bool
        if len(self.__Conjunto) == len(__value.__Conjunto):
            bandera = True
            i = 0
            while i < (len(self.__Conjunto)) and bandera == True:
                if self.__Conjunto[i] in __value.Conjunto:
                    bandera = True
                else : bandera = False
                i += 1
        else: bandera = False 
        return bandera
    """
    def __eq__(self, __value: object) -> bool:
        bandera : bool
        if len(self.__Conjunto) == len(__value.retornaLista()):
            bandera = True
            i = 0
            while i < (len(self.__Conjunto)) and bandera == True:
                if self.__Conjunto[i] in __value.retornaLista():
                    bandera = True
                else : bandera = False
                i += 1
        else: bandera = False 
        return bandera
