'''Se necesita desarrollar una aplicación que procese la información de las variables meteorológicas temperatura, humedad y presión atmosférica. El registro de estas variables se hace cada una hora durante todos los días del mes. Esto se guarda en un archivo de texto separado con coma que contiene los siguientes datos: número de día, hora, valor de la variable temperatura, valor de la variable humedad y valor de la variable presión atmosférica. Se genera un archivo por cada mes.

Defina la clase “Registro” que posea como atributos los valores de las tres variables meteorológicas que se registran.

Implemente un programa que:

1.    Defina una lista bidimensional en la que se almacene el registro de las variables meteorológicas (instancia de la clase Registro) para cada día del mes, por cada hora.

2.    Almacene en la lista bidimensional los datos registrados en el archivo.

3.    Presente un menú de opciones permita realizar las siguientes tareas:

3.1.        Mostrar para cada variable el día y hora de menor y mayor valor.

3.2.        Indicar la temperatura promedio mensual por cada hora.

3.3.        Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente formato.'''

'''3.4 Diagrama de secuencia'''

import os
from ManejadorListaBidimensional import ManejadorLista
from Menu import Menu
from Registro import Registro
import csv


#Funciones test Muy especificas

def testIngresoRegistro2():
    objeto1Registro = Registro(1.0,0,0.0)
    print("Printear el objeto registro : ")
    print(objeto1Registro)


def testIngresoRegistro():
    objetoRegistro = Registro(1.0,2,3.0)
    print("Printear el objeto registro : ")
    print(objetoRegistro)


def testPruebaManejadorLista():
    ManejadorL = ManejadorLista()
    ManejadorL.MostrarTODO()
    print("-----------------------------------------------------------------------------------------------")
    ManejadorL.MostrarPorDia(1)


def borrarPantalla(): #Probando módulo OS, interesante
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")



#Funciones Test Importantes


def testMenu():
    Menuc = Menu()
    lista = []
    Menuc.ElegirOP(lista,1)

def testIngresoArchivo():
    ManejadorLB = ManejadorLista()
    ManejadorLB.IngresoArchivo()
    """
    #listaTemp = ManejadorLB.IngresoArchivo()
    print("-----------------------------------------------------------------------------------------------")
    ManejadorLB.MostrarTODO()
    #ManejadorLB.mostrarElemento(1,0)
    ManejadorLB.MostrarLongLista()
    ManejadorLB.MayorTemperatura()
    ManejadorLB.MenorTemperatura()
    ManejadorLB.MenorHumedad()
    ManejadorLB.MenorPresion()
    print("\n")
    ManejadorLB.TemperaturaPromedioMensual()
    print("\n")
    dia = int(input("Ingrese un dia para mostrar todas las variables Metereologicas por DIA INGRESADO : "))
    ManejadorLB.MostrarPorDia(dia)
    
    print("\n----Promedio del main xd----")
    print("longitud lista Temperaturas : {}".format(len(listaTemp)))
    acum = 0.0
    print(" lista promedios \n:{}".format(listaTemp))
    for i in range(len(listaTemp)):
        acum += listaTemp[i]
    print("acum : ",acum)
    prom = acum / len(listaTemp)
    print("Promedio de temperaturas en el main  (Para comparar con el método del objeto Manejador de Listas Bidimensionales) : {} ".format(prom))
    """







if __name__ == '__main__':
    borrarPantalla()
    borrarPantallaL = lambda : os.system('cls')
    print("-------principal-------")
    #TESTEO DE REGISTROS
    #testIngresoRegistro()
    #testIngresoRegistro2()
    #TESTEO DEL MANEJADOR LISTA BIDIMENSIONAL DE REGISTROS
    #testIngresoArchivo()
    #testPruebaManejadorLista()


    ManejadorLBM = ManejadorLista()
    ManejadorLBM.IngresoArchivo()

    Menuc = Menu()
    Menuc.ElegirOP(ManejadorLBM)
    
    print("-----------------------------------------------------------------------------------------------")

    
    
    print("-----------------------------------------------------------------------------------------------")
    print("\n")
    








