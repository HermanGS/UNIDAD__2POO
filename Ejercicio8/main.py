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


from Menu import Menu
from Conjunto import Conjunto
from ManejadorConjuntos import ManejadorConjuntos


def testMenu():
    print("Test Menu")

    Conjunto1 = Conjunto()
    Conjunto2 = Conjunto()
    Menuc = Menu()
    Menuc.ElegirOP(Conjunto1,Conjunto2)


def testComportamientoConjuntos():
    Conjunto1 = Conjunto([1,2,3,4])
    print("Conjunto 1 : ",Conjunto1)
    Conjunto2 = Conjunto([3,6,9])
    Conjunto3 = Conjunto([2,3,4])
    print("Conjunto 1 : ",Conjunto1)
    Conjunto4 = Conjunto([2,3,4])
    print("Conjunto 2 : ",Conjunto2)
    print("Suma del Conjunto 1 Y 2",Conjunto1 + Conjunto2)
    print("uh xd , Conjunto 1 despues de la union de Conjuntos 1 y 2 : ",Conjunto1)
    print("Resta del Conjunto 1 y 2",Conjunto1 - Conjunto2)
    print("Operando == entre el Conjunto 3 y Conjunto 4 : ",Conjunto3 == Conjunto4)




if __name__ == '__main__':
    print("---------------------------------> MAIN <---------------------------------")
    #testMenu()
    #testComportamientoConjuntos()

    
    


    Conjunto1 = Conjunto([1,2,3,4])
    Conjunto2 = Conjunto([3,6,9])
    Conjunto3 = Conjunto([2,3,4])
    Conjunto4 = Conjunto([2,3,4])

    """
    #Mane = ManejadorConjuntos()
    Mane.AgregarConjunto(Conjunto1)
    Mane.AgregarConjunto(Conjunto2)
    Mane.AgregarConjunto(Conjunto3)
    Mane.AgregarConjunto(Conjunto4)
    """
    
    Menuc = Menu()    
    Menuc.ElegirOP(Conjunto1,Conjunto2)
    Menuc.ElegirOP(Conjunto3,Conjunto4)    
