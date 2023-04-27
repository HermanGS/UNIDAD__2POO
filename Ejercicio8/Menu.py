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

from  Conjunto import Conjunto

class Menu:

    def op1(self,Conjunto1,Conjunto2):
        print("Entro al 1")
        print("Suma del Conjunto 1 Y 2",Conjunto1 + Conjunto2)

    def op2(self,Conjunto1,Conjunto2):
        print("Entro al 2")
        print("Resta del Conjunto 1 y 2",Conjunto1 - Conjunto2)

    def op3(self,Conjunto1,Conjunto2):
        print("Entro al 3")
        print("Operando == entre el Conjunto 1 y Conjunto 2 : ",Conjunto1 == Conjunto2)

    def ElegirOP(self,Conjunto1,Conjunto2):
        op = -1
        while op != 0:
            print("Conjuntos \n A = ",Conjunto1,"\n B = ",Conjunto2)
            print("Ingrese una Opcion '1','2' o '3' ")
            print("1- La unión de dos conjuntos, para ello sobrecargue el operador binario suma (+).\n2- La diferencia de dos conjuntos, para ello sobrecargue el operador binario resta (-).\n3- Si dos conjuntos son iguales, para ello sobrecargue el operador “==”")
            print("\n\n")
            op = int(input("Respuesta : "))
            while op < 0 or op > 3:
                print("ERROR - Opcion fuera de rango - vuelva a ingresar la opcion : ")
                op = int(input("Respuesta : "))
            if op == 1:
                self.op1(Conjunto1,Conjunto2)
            elif op == 2:
                self.op2(Conjunto1,Conjunto2)
            elif op == 3:
                self.op3(Conjunto1,Conjunto2)
            else: 
                print("<-----------------------------> Saliendo del Programa (Menu) <----------------------------->")
            